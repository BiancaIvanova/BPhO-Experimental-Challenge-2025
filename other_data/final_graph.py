import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def create_scatter_plot(csv_file):
    data = pd.read_csv(csv_file)

    white_data = data[data['ball'] == 'white_ball']
    red_data = data[data['ball'] == 'red_ball']

    white_mean_h_max = white_data['mean_h_max'].values
    red_mean_h_max = red_data['mean_h_max'].values
    white_uncertainty = white_data['uncertainty'].values
    red_uncertainty = red_data['uncertainty'].values

    slope, intercept, r_value, p_value, std_err = stats.linregress(white_mean_h_max, red_mean_h_max)
    
    trendline_y = slope * white_mean_h_max + intercept

    print(f"Trendline equation: y = {slope:.4f}x + {intercept:.4f}")

    plt.figure(figsize=(8, 6))
    
    plt.scatter(white_mean_h_max, red_mean_h_max, c='darkblue', s=10)

    plt.errorbar(white_mean_h_max, red_mean_h_max, 
                 xerr=white_uncertainty, yerr=red_uncertainty, 
                 fmt='o', ecolor='lightgray', linestyle='None', capsize=5, elinewidth=1)

    plt.plot(white_mean_h_max, trendline_y, color='gray', linestyle='-', linewidth=1.5, label='Trendline')

    plt.xlabel('White Ball Mean h_max \\mm')
    plt.ylabel('Red Ball Mean h_max \\mm')
    plt.title('Red Ball vs White Ball Mean h_max')

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    plot_filename = os.path.splitext('other_data\\' + os.path.basename(csv_file))[0] + '_scatter_plot.png'
    plt.savefig(plot_filename)

    plt.show()

csv_file = 'other_data\\max_ball_heights.csv'

create_scatter_plot(csv_file)
