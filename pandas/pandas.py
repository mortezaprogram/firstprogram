import pandas as pd
# pd.options.display.float_format = '{:,.2f}'.format
df = pd.read_csv('salaries_by_college_major.csv')
# df.head()
# df.shape
clean_df = df.dropna()
# clean_df.tail()
# clean_df["Starting Median Salary"].idxmax()
# clean_df['Undergraduate Major'].loc[clean_df["Starting Median Salary"].idxmax()]
# print(clean_df["Mid-Career Median Salary"].max())
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head(10)
clean_df.groupby('Group').count()
clean_df.groupby('Group').mean()