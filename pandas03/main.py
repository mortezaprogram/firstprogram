import pandas as pd
import matplotlib.pyplot as plt
colors = pd.read_csv('data/colors.csv')
sets= pd.read_csv('data/sets.csv')
# print(colors)
# colors.head()
# colors['name'].nunique()
# colors.groupby('is_trans').count()
colors.is_trans.value_counts()
sets.sort_values("year",ascending=False).head()
# sets.sort_values('num_parts', ascending=False).head()
sets_by_year=sets.groupby("year").count()
sets_by_year["set_num"].head(100)
# plt.plot(sets_by_year.index, sets_by_year.set_num)
# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
theme_by_year=sets.groupby("year").agg({"theme_id":pd.Series.nunique})
theme_by_year.rename(columns={"theme_id":"nr_theme"},inplace=True)
# theme_by_year.head()
# plt.plot(theme_by_year.index[:-2],theme_by_year.nr_theme[:-2])
ax1 = plt.gca() # get current axes
ax2 = ax1.twinx()
# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# ax2.plot(theme_by_year.index[:-2], theme_by_year.nr_theme[:-2])
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
set_theme_count = sets["theme_id"].value_counts()
set_theme_count[:5]
# <img src="https://i.imgur.com/Sg4lcjx.png">
themes = pd.read_csv('data/themes.csv') # has the theme names!
themes.head()
themes[themes.name == 'Star Wars']
set_theme_count = pd.DataFrame({'id':set_theme_count.index,
                                'set_count':set_theme_count.values})
set_theme_count.head()
merged_df = pd.merge(set_theme_count, themes, on='id')
merged_df.head()
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])