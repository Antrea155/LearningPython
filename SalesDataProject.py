#Todo : user interface to specify path for dataset / credentials / CSV 
import kagglehub
path = kagglehub.dataset_download("alanjo/graphics-card-full-specs")

print("Path todataset  files:", path)
import os
os.environ["KAGGLE_USERNAME"] = "antreaconstantinou"
os.environ["KAGGLE_KEY"] = "81fc49d96b6b68a44af035f01b8c65f2"

import pandas as pd

# Load the dataset
csv_file = os.path.join(path, "gpu_specs_v6.csv")
df = pd.read_csv(csv_file)

# Display the first few rows
print(df.head())