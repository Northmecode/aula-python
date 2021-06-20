file_name = './base/hc.xlsx'
sheet = 'HC'

import pandas as pd

df = pd.read_excel(io=file_name, sheet_name=sheet)
print(df.head(1))