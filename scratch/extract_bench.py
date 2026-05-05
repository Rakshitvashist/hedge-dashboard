import pandas as pd
import json

def get_new_bench_data():
    df = pd.read_excel('d:/Dashboard/Hedge_Pro_Summary_v1.xlsx', sheet_name='Detailed_Monthly_Summary')
    # Use Month as key, Bench as value
    bench_returns = df.set_index('Month')['Bench'].to_dict()
    
    df_ts = pd.read_excel('d:/Dashboard/Hedge_Institutional_Deep_Dive.xlsx', sheet_name='Time_Series_Analytics')
    bench_equity = df_ts.set_index('Month')['Bench_Equity'].to_dict()
    
    return bench_returns, bench_equity

returns, equity = get_new_bench_data()
print("--- Returns ---")
print(json.dumps(returns, indent=2))
print("--- Equity ---")
print(json.dumps(equity, indent=2))
