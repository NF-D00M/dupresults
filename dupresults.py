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
df[1] = df[1].str.replace(r'\n', '',)
# df[1] = df[1].str.repalce(r'', '')

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
                                        r',', '')


df_first_entry = df[df.duplicated(['edited'], keep='last')]
df_last_entry = df[df.duplicated(['edited'], keep='first')]
# df = df.duplicated(['results', 'edited'], keep='first')
print(df_first_entry.to_string())
print(df_last_entry.to_string())








# REGEX example = BNR Sat RACE 2 RESULTS: 1,3,2,4
# duplicates = []
# results_list = []
# results_regex = re.compile(r"[A-Z]{3}[a-zA-Z]{\s3}\sRACE\s(\d{1,2})\sRESULTS:")
# # results_regex = re.compile(r"[A-Z]{3}\s[a-zA-Z]{3}\sRACE\s(\d{1,2})\sRESULTS:\s\d{1,2},\d{1,2},\d{1,2},\d{1,2}")
# # regex_1 = re.compile(r"[A-Z]{3}\s[a-zA-Z]{3}\sRACE\s(\d{1,2})\sRESULTS:")
# # regex_2 = re.compile(r"[A-Z]{3}\s[a-zA-Z]{3}\sRACE\s(\d{1,2})\sRESULTS:")
#
#
# with open('viclog.txt', 'r', encoding='utf-8') as file:
#     contents = file.read()
#     results = results_regex.finditer(contents)
#     for result in results:
#         print(result)
#         results_list.append(result)
#
# print('----------')
# print(results_list)
# print('----------')
#


