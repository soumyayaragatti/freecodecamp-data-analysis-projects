import medical_data_visualizer as mdv
import matplotlib.pyplot as plt

# Draw the categorical plot
fig1 = mdv.draw_cat_plot()
plt.show()  # This will display the catplot

# Draw the heat map
fig2 = mdv.draw_heat_map()
plt.show()  # This will display the heatmap