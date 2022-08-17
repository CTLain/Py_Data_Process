import pandas as pd
import os
import glob

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

for file in csv_files:
    df = pd.read_csv(file)

    df.columns = df.columns.str.replace('Time', 'timestamp')
    
    for columns in df:
        if columns == 'timestamp':
            df[columns] = df[columns].str.replace(":", "").astype(int)
        if columns == 'Date':
            df[columns] = pd.to_datetime(df[columns], dayfirst=True)
            df[columns] = df[columns].astype(str)
            df[columns] = df[columns].str.replace("-", "").astype(int)
        if df[columns].dtypes == object:
            df[columns] = df[columns].eq('Yes').mul(1)
            # df[columns] = df[columns].map(dict('Yes'=1, 'No'=0), na_action='ignore')

    df.to_csv(file + "_parse", index=False)
