import pandas as pd

file_path = './score_uts.xlsx'
xls = pd.ExcelFile(file_path)
df_responses = pd.read_excel(xls, 'Response')
df_answers = pd.read_excel(xls, 'answer')
sheet_names = xls.sheet_names

# Dropping 'NIM' and 'Name'
df_responses_only = df_responses.drop(columns=['NIM', 'Name'])
# Transpose
df_answers_transposed = df_answers.transpose()
correct_answers = df_answers_transposed.iloc[:, 0]
comparison = df_responses_only.eq(correct_answers, axis=1)
# Converting True/False to 1/0
scores = comparison.astype(int)
df_responses['Total Score'] = scores.sum(axis=1)
df_responses[['NIM', 'Name', 'Total Score']]

#Multiple Choice (q1-q10), True/False (q11-q20)
multiple_choice_responses = df_responses.loc[:, 'q1':'q10']
true_false_responses = df_responses.loc[:, 'q11':'q20']
multiple_choice_scores = multiple_choice_responses.eq(correct_answers['q1':'q10'], axis=1).astype(int)
true_false_scores = true_false_responses.eq(correct_answers['q11':'q20'], axis=1).astype(int)
df_responses['Multiple Choice Subtotal'] = multiple_choice_scores.sum(axis=1)
df_responses['True/False Subtotal'] = true_false_scores.sum(axis=1)
df_responses['Overall Total'] = df_responses['Multiple Choice Subtotal'] + df_responses['True/False Subtotal']
df_responses[['NIM', 'Name', 'Multiple Choice Subtotal', 'True/False Subtotal', 'Overall Total']]

#save
output_file_path = 'output_score_uts.xlsx'
df_responses.to_excel(output_file_path, index=False)
