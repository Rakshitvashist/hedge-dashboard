import pandas as pd
import json

def get_new_bench_data():
    df = pd.read_excel('d:/Dashboard/Hedge_Pro_Summary_v1.xlsx', sheet_name='Detailed_Monthly_Summary')
    # Use Month as key, Bench as value
    bench_returns = df.set_index('Month')['Bench'].to_dict()
    
    df_ts = pd.read_excel('d:/Dashboard/Hedge_Institutional_Deep_Dive.xlsx', sheet_name='Time_Series_Analytics')
    bench_equity = df_ts.set_index('Month')['Bench_Equity'].to_dict()
    
    data = {
        "returns": bench_returns,
        "equity": bench_equity
    }
    with open('d:/Dashboard/scratch/bench_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

get_new_bench_data()
