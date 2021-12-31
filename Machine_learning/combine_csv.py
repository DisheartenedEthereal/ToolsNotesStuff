import os

import pandas as pd
os.chdir("/Users/neginkzm/Desktop/test/")
all_filenames = ["1.csv","2.csv"]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
