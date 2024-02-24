from dstricks import Plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')
cat_cols = tips.select_dtypes(include=['object', 'category']).columns.tolist()
num_cols = tips.select_dtypes(include=['number']).columns.tolist()

# # plotting
# Plot.cat_plot(data=tips, target="sex", cat_cols=cat_cols)
Plot.dist_box_plot(data=tips, num_cols=num_cols)