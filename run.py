from dstricks.cfg import CFG
from dstricks.plot import dist_box_plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')
cat_cols = tips.select_dtypes(include=['object', 'category']).columns.tolist()
num_cols = tips.select_dtypes(include=['number']).columns.tolist()

# # plotting
# cat_plot(data=tips, target="sex", cat_cols=cat_cols, show_legend=True)
# dist_box_plot(data=tips, num_cols=num_cols)
cfg = CFG()
cfg.seed = 42
print(cfg.seed)