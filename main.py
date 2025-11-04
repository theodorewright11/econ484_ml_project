import pandas as pd

df = pd.read_excel("crash_data_2014_to_2024.xlsx")
df.to_csv("crash_data_2014_to_2024.csv", index=False)
print("done")