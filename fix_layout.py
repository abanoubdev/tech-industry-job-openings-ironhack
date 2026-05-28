path = 'Notebooks/datasets_eda.ipynb'
with open(path, 'r') as f:
    data = f.read()

old_str = "fig, axes = plt.subplots(1, 3, figsize=(20, 6))"
new_str = "fig, axes = plt.subplots(3, 1, figsize=(10, 18))"

data = data.replace(old_str, new_str)

with open(path, 'w') as f:
    f.write(data)
