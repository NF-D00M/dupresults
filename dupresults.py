import re
import pandas as pd

print("Hello Janine")

# Read lines in each file.
# If string "RESULTS" is in each line print line
results_list1 = []
with open('viclog.txt', 'rt') as file:
    data = file.readlines()
    for line in data:
        if 'RESULTS' in line:
            # print(line)
            results_list1.append(line)
# print(results_list1)

for lines in line:
    df = pd.DataFrame(results_list1)
# print('---------- DataFrame ----------')
# print(df.to_string())

# Split DataFrame into two columns, time & results
df = df[0].str.split('--', n=5, expand=True)
# print(df.to_string())

# Remove regular expression
df[0] = df[0].str.replace(r'REPLY', '')
df[1] = df[1].str.replace(r'%GEN-I-RESULTS,', '')
df[1] = df[1].str.replace(r'\n', '', regex=True)

# Rename columns
df.columns = ['time', 'results']
# Copy column
df['edited'] = df.loc[:, 'results']

# Remove regular expression of newly copied column
df['edited'] = df['edited'].str.replace(r': \d{1,2},\d{1,2},\d{1,2},\d{1,2}|'
                                        r': \d{1,2},\d{1,2},\d{1,2}|'
                                        r': \d{1,2},\d{1,2}|'
                                        r': \d{1,2}|'
                                        r'\+\d{1,2}|'
                                        r',\d|'
                                        r',', '', regex=True)

# Creat two dataframes, first result entry and second result entry
df_first_entry = df[df.duplicated(['edited'], keep='last')]  # Considers first entry as duplicate
df_last_entry = df[df.duplicated(['edited'], keep='first')]  # Considers last entry as duplicate

# print(df_first_entry.to_string())
# print(df_last_entry.to_string())

df_first_entry.columns = ['first_time', 'first_results', 'first_transaction']
df_last_entry.columns = ['last_time', 'last_results', 'last_transaction']

# print(df_first_entry.to_string())
# print(df_last_entry.to_string())
# df_results_change = pd.concat([df_first_entry, df_last_entry], keys=['first_entry', 'last_entry'], axis=1, join='outer', sort=False)
df_results_change = pd.concat([df_first_entry, df_last_entry], axis=1, sort=True)

# Drop NAN cell values
df_results_change = df_results_change.apply(lambda x: pd.Series(x.dropna().values))
# Drop columns
df_results_change = df_results_change.drop(['first_transaction', 'last_transaction'], axis=1)


print(df_results_change.to_string())

# Another Test
# New Test
