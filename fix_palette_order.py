import json

path = 'Notebooks/datasets_eda.ipynb'
with open(path, 'r') as f:
    data = f.read()

# Fix the countplot so the magma palette is applied sequentially instead of alphabetically
old_str = "palette='magma', hue='Industry', legend=False, ax=axes[1]"
new_str = "palette='magma', hue='Industry', hue_order=merged_df['Industry'].value_counts().index, legend=False, ax=axes[1]"

data = data.replace(old_str, new_str)

with open(path, 'w') as f:
    f.write(data)
