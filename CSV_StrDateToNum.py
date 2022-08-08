import pandas as pd

df = pd.read_csv('./PTATMonitor_05-08-2022_15H-23-36S399.csv')

df['timestamp'] = df['timestamp'].str.replace(":", "")

print(df['timestamp'])

df.to_csv('./PTATMonitor_05-08-2022_15H-23-36S399_parse.csv', index=False)