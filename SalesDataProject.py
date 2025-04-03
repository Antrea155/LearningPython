import kagglehub
from kaggle.api.kaggle_api_extended import KaggleApi  # Import Kaggle API class for validation
import os
import pandas as pd
import tkinter as tk #GUI library
from tkinter import ttk, filedialog, messagebox
import pdb

def submit():
    username = name_entry.get()
    key = Key_entry.get()

    if username and key:
        os.environ["KAGGLE_USERNAME"] = username
        os.environ["KAGGLE_KEY"] = key
        # Validate Kaggle credentials
        try:
            try:
                api = KaggleApi()
                api.authenticate()
            except Exception as e:
                messagebox.showwarning("Invalid Credentials", f"The credentials you entered are invalid: {e}")
                return
            
            #Authentication is successful, proceed with dataset download
            pathstr = Path_entry.get()
            try:
                path = kagglehub.dataset_download(pathstr)
                # Load the dataset
                csvstr = CSV_entry.get()
                csv_file = os.path.join(path, csvstr)

                # Check if the CSV file exists
                if os.path.exists(csv_file):
                    dataset = pd.read_csv(csv_file)           
                    open_dataset_window(dataset)
                else:
                    messagebox.showwarning("File Error", "CSV file not found in the dataset directory.")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while downloading the dataset: {e}")    

        except Exception as e:
            messagebox.showwarning("Invalid Credentials", "The credentials you entered are invalid.")

    else:
        messagebox.showwarning("Input Error", "Please check your credentials")

def open_dataset_window(dataset):
    new_window = tk.Toplevel(root)
    new_window.title("Dataset")

    tree = ttk.Treeview(new_window)
    #expand=True: makes the widget expand to fill any extra space in new_window.
    #fill=tk.BOTH: makes the widget expand both horizontally and vertically within the new_window.
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    tree["columns"] = list(dataset.columns)
    tree["show"] = "headings"  # show only the column headings as the first row, hine index row

    for col in dataset.columns:
        tree.heading(col, text=col)

    for row, data in dataset.iterrows():
        tree.insert("", "end", values=list(data))

    new_window.geometry("800x600")

#csv format to extract details info
#username,...
#key,...
#path,...
#csv,...
name = ''
key = ''
path = '' 
csv = ''
def MatchInfo(token, string):
    global name, key, path, csv
    match token:
        case "username":
            name = string.strip()
        case "key":
            key = string.strip()
        case "path":
            path = string.strip()
        case "csv":
            csv = string.strip()

def LoadDetails():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])  # Open file dialog
    if file_path:
        with open(file_path, "r") as file:
            for line in file:
                tokens = line.strip().split(",") 
                if len(tokens) >= 2:
                    MatchInfo(tokens[0], tokens[1])           
    if not all([name, key, path, csv]): 
        messagebox.showwarning("Error: Some details are missing!") 
    else:    
        # **Update Entry Fields**
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)

        Key_entry.delete(0, tk.END)
        Key_entry.insert(0, key)

        Path_entry.delete(0, tk.END)
        Path_entry.insert(0, path)

        CSV_entry.delete(0, tk.END)
        CSV_entry.insert(0, csv)

# Create the main window
root = tk.Tk()
root.title("Enter your details:")
root.geometry("300x250") 

# Username label
username_frame = tk.Frame(root)
username_frame.pack(padx=10, pady=5, anchor="w") #leftside
tk.Label(username_frame, text="Username:").pack(side="left")
name_entry = tk.Entry(username_frame)
name_entry.pack(side="left")

# Key label
key_frame = tk.Frame(root)
key_frame.pack(padx=10, pady=5, anchor="w")
tk.Label(key_frame, text="Kaggle API Key:").pack(side="left")
Key_entry = tk.Entry(key_frame, show="*")  # Hide the key
Key_entry.pack(side="left")

# Dataset path label 
path_frame = tk.Frame(root)
path_frame.pack(padx=10, pady=5, anchor="w")
tk.Label(path_frame, text="Dataset Path:").pack(side="left")
Path_entry = tk.Entry(path_frame)
Path_entry.pack(side="left")

# CSV file label
csv_frame = tk.Frame(root)
csv_frame.pack(padx=10, pady=5, anchor="w")
tk.Label(csv_frame, text="CSV File Name:").pack(side="left")
CSV_entry = tk.Entry(csv_frame)
CSV_entry.pack(side="left")

# Load details from a txt file
load_button = tk.Button(root, text="Load Details", command=LoadDetails)
load_button.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

# Run the application
root.mainloop()








