path = 'Notebooks/datasets_eda.ipynb'
with open(path, 'r') as f:
    data = f.read()
data = data.replace("color='#1f77b4', ax=axes[1]", "palette='magma', hue='Industry', legend=False, ax=axes[1]")
data = data.replace("ax=axes[2], color='#1f77b4'", "ax=axes[2], color='#b5367a'")
with open(path, 'w') as f:
    f.write(data)
