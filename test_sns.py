import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({'Industry': ['IT', 'IT', 'Finance', 'Finance', 'Finance', 'Retail']})
counts = df['Industry'].value_counts()
print(counts.index)

fig, ax = plt.subplots()
sns.countplot(data=df, y='Industry', order=counts.index, palette='magma', hue='Industry', hue_order=counts.index, legend=False, ax=ax)
for bar in ax.patches:
    print(bar.get_facecolor())
