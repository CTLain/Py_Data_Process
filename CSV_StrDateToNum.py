import pandas as pd
import os
import glob
import re

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

for i, file in enumerate(csv_files):
    df = pd.read_csv(file)

    df.columns = df.columns.str.replace('Time', 'timestamp')
    df.drop('Date', axis=1, inplace=True) #currently doesn't need date columns

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

    # classify_name = file.split('\\')
    classify_name = re.split(r'( |/|\\)', file)
    list_len = len(classify_name)
    print(classify_name[list_len-1])

    classify_name[list_len-1] = classify_name[list_len-1].split('_')[0] + "_" + str(i)
    print(classify_name[list_len-1])
    file = ''
    for a in classify_name:
        file += a 

    df.to_csv(file + ".csv", index=False)
