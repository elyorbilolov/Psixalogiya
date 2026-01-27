import pandas as pd

file_path = 'psix.xlsx'
try:
    xl = pd.ExcelFile(file_path)
    print(f"Sheet names: {xl.sheet_names}")
    for sheet in xl.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet)
        print(f"\nSheet: {sheet}")
        print(f"Columns: {df.columns.tolist()}")
        print("First 2 rows:")
        print(df.head(2))
except Exception as e:
    print(f"Error: {e}")
