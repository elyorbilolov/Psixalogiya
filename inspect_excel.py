import pandas as pd
import json
import os

files = ['sovol-1.xlsx', 'sovol-2.xlsx', 'sovol-3.xlsx', 'sovol-4.xlsx']
result = {}

for i, file in enumerate(files):
    try:
        df = pd.read_excel(file)
        # Assume columns are: Question, Option A, Option B, Option C, Option D, Correct Answer
        # We need to adapt based on actual columns
        print(f"File: {file}")
        print(f"Columns: {df.columns.tolist()}")
        print(df.head(1))
    except Exception as e:
        print(f"Error reading {file}: {e}")
