import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
# df.head()
# df.groupby("TAG").sum()
# print(pd.to_datetime(df["DATE"]))
# type(pd.to_datetime(df["DATE"]))
# test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        # 'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        # 'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# pivoted_df = .pivot(index='Age', columns='Actor', values='Power')
pivoted_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
pivoted_df.fillna(0, inplace=True)
# print(pivoted_df)
# pivoted_df.isna().values.any()
plt.figure(figsize=(16,10))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(pivoted_df.index, pivoted_df.java)
plt.plot(pivoted_df.index, pivoted_df.python)
# plt.plot(pivoted_df.index, pivoted_df.go)
for column in pivoted_df.columns:
    plt.plot(pivoted_df.index, pivoted_df[column],
    linewidth=3, label=pivoted_df[column].name)

plt.legend(fontsize=16)

roll_df = pivoted_df.rolling(window=3).mean()

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
