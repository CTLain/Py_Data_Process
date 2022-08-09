import pandas as pd

df = pd.read_csv('./PTATMonitor_05-08-2022_15H-23-36S399.csv')

for columns in df:
    if columns == 'timestamp':
        df[columns] = df[columns].str.replace(":", "")
    if columns == 'Date':
        df[columns] = pd.to_datetime(df[columns], dayfirst=True)
        df[columns] = df[columns].astype(str)
        df[columns] = df[columns].str.replace("-", "")
        # print(df[columns])
    print(df[columns].dtypes)

# print(df['timestamp'])

df.to_csv('./PTATMonitor_05-08-2022_15H-23-36S399_parse.csv', index=False)