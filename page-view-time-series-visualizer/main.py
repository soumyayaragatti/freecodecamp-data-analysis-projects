import time_series_visualizer as tsv
import matplotlib.pyplot as plt

# Draw the plots
fig1 = tsv.draw_line_plot()
plt.show()

fig2 = tsv.draw_bar_plot()
plt.show()

fig3 = tsv.draw_box_plot()
plt.show()
