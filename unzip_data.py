import os
import zipfile
import pandas as pd
from pathlib import Path

# Define the directory containing the ZIP files
zip_dir = "data/zips/2025-02-24"
output_dir = "data/"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Lists to store DataFrames
comercios_dfs = []
productos_dfs = []

# Process each ZIP file
for zip_file in Path(zip_dir).glob("*.zip"):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Extract to a temporary directory using the ZIP filename
        temp_dir = os.path.join(zip_dir, zip_file.stem)
        os.makedirs(temp_dir, exist_ok=True)
        zip_ref.extractall(temp_dir)
        
        # Read CSVs if they exist
        if os.path.exists(os.path.join(temp_dir, "comercio.csv")):
            df = pd.read_csv(
                os.path.join(temp_dir, "comercio.csv"),
                sep='|',
                low_memory=False
            )
            comercios_dfs.append(df)
            
        if os.path.exists(os.path.join(temp_dir, "productos.csv")):
            df = pd.read_csv(
                os.path.join(temp_dir, "productos.csv"),
                sep='|',
                low_memory=False
            )
            productos_dfs.append(df)
        
        # Clean up temporary directory
        for file in Path(temp_dir).glob("*"):
            os.remove(file)
        os.rmdir(temp_dir)

# Combine and save the DataFrames
if comercios_dfs:
    data_comercios = pd.concat(comercios_dfs, ignore_index=True)
    data_comercios.to_csv(
        os.path.join(output_dir, "data_comercios.csv"), 
        sep='|',
        index=False
    )
    print(f"Combined comercios.csv saved with {len(data_comercios)} rows")

if productos_dfs:
    data_productos = pd.concat(productos_dfs, ignore_index=True)
    data_productos.to_csv(
        os.path.join(output_dir, "data_productos.csv"), 
        sep='|',
        index=False
    )
    print(f"Combined productos.csv saved with {len(data_productos)} rows")