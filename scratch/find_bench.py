import pandas as pd

def find_benchmark(filename):
    print(f"--- Finding Benchmark in {filename} ---")
    xl = pd.ExcelFile(filename)
    for sheet in xl.sheet_names:
        df = pd.read_excel(filename, sheet_name=sheet)
        bench_cols = [c for c in df.columns if 'Bench' in str(c)]
        if bench_cols:
            print(f"Sheet: {sheet}, Bench Columns: {bench_cols}")
            # If there's a Date or Month column, print it too
            date_cols = [c for c in df.columns if 'Month' in str(c) or 'Date' in str(c)]
            if date_cols:
                print(df[date_cols + bench_cols].head(10))
            else:
                print(df[bench_cols].head(10))

find_benchmark('d:/Dashboard/Hedge_Pro_Summary_v1.xlsx')
find_benchmark('d:/Dashboard/Hedge_Institutional_Deep_Dive.xlsx')
