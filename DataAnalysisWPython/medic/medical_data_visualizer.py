import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1

df = pd.read_csv("DataAnalysisWPython/medic/medical_examination.csv", na_values=" ?")
# df = pd.read_csv('C:/Users/yashb/OneDrive/Desktop/general/little projects/webdev/sigmaByHarry/learn/DataAnalysisWPython/medic/medical_data_visualizer.py', na_values=" ?")

# 2
df['overweight'] = ((df['weight']/(df['height']/100)**2)>25).astype(int)
# print(df['bmi'].head())
df['overweight'].head()
# 3
# df['cholesterol'] = 1 if df['cholesterol']>1 else 0
# df['gluc'] = 1 if df['gluc']>1 else 0
#can't use if else on series
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# print(df.head())
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')
    

    # 7
    sns.catplot(x='variable', y='total', hue='value', col='cardio',
                      data=df_cat, kind='bar')


    # 8
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                      data=df_cat, kind='bar').figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi'] )
                & (df['height'] >= df['height'].quantile(0.025)) 
                & (df['height'] <= df['height'].quantile(0.975)) 
                & (df['weight'] >= df['weight'].quantile(0.025)) 
                & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr(numeric_only=True)

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        vmax=0.3,
        vmin=-0.1,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )


    # 16
    fig.savefig('heatmap.png')
    return fig
