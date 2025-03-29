import kagglehub
import os
import pandas as pd
import tkinter as tk #GUI library
from tkinter import messagebox

def submit():
    username = name_entry.get()
    key = Key_entry.get()

    if username and key:
        os.environ["KAGGLE_USERNAME"] = username
        os.environ["KAGGLE_KEY"] = key

        #todo:check if credientials are valid
        pathstr = Path_entry.get()
        path = kagglehub.dataset_download(pathstr)

        # Load the dataset
        csvstr = CSV_entry.get()
        csv_file = os.path.join(path, csvstr)
        df = pd.read_csv(csv_file)
        # Display the first few rows
        print(df.head())
    else:
        messagebox.showwarning("Input Error", "Please check your credentials")

# Create the main window
root = tk.Tk()
root.title("User Details Form")
root.geometry("300x200")

# Name label and entry field
tk.Label(root, text="Username:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Key label and entry field
tk.Label(root, text="Key:").pack(pady=5)
Key_entry = tk.Entry(root)
Key_entry.pack(pady=5)

# Dataset path label and entry field
tk.Label(root, text="Data set path:").pack(pady=5)
Path_entry = tk.Entry(root)
Path_entry.pack(pady=5)

# CSV file name label and entry field
tk.Label(root, text="Csv:").pack(pady=5)
CSV_entry = tk.Entry(root)
CSV_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

# Run the application
root.mainloop()








