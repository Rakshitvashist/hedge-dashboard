import pandas as pd

def inspect_excel(filename):
    print(f"--- Inspecting {filename} ---")
    xl = pd.ExcelFile(filename)
    print(f"Sheets: {xl.sheet_names}")
    for sheet in xl.sheet_names:
        df = pd.read_excel(filename, sheet_name=sheet)
        print(f"\nSheet: {sheet}")
        print(df.head())
        print(df.columns.tolist())

inspect_excel('d:/Dashboard/Hedge_Institutional_Deep_Dive.xlsx')
inspect_excel('d:/Dashboard/Hedge_Pro_Summary_v1.xlsx')
