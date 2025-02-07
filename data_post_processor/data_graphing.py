import os
import pandas as pd
import matplotlib.pyplot as plt

def create_plots(csv_file):
    filename = os.path.splitext(os.path.basename(csv_file))[0]
    plot_title = filename[:7]

    graphs_directory = os.path.join(os.getcwd(), 'data_post_processor\\graphs')
    if not os.path.exists(graphs_directory):
        os.makedirs(graphs_directory)

    # Read the CSV file
    data = pd.read_csv(csv_file)

    # First plot: Y measurements vs time
    plt.figure()
    plt.plot(data['timestamp_s'], data['red_relative_Y_mm'], label='Red Y')
    plt.plot(data['timestamp_s'], data['white_relative_Y_mm'], label='White Y')
    plt.xlabel('Time (s)')
    plt.ylabel('Relative Y (mm)')
    plt.title(f'Y Measurements Over Time - {plot_title}')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig(os.path.join(graphs_directory, f'{filename}_Y_vs_time.png'))

    # Second plot: Red velocity vs White velocity
    plt.figure()
    plt.scatter(data['white_velocity_mm_s'], data['red_velocity_mm_s'], c='darkblue', label='Red vs White Velocity', s=10)
    plt.xlabel('White Velocity (mm/s)')
    plt.ylabel('Red Velocity (mm/s)')
    plt.title(f'Red Velocity vs White Velocity - {plot_title}')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig(os.path.join(graphs_directory, f'{filename}_red_vs_white_velocity.png'))

    # Third plot: Velocities over time
    plt.figure()
    plt.plot(data['timestamp_s'], data['red_velocity_mm_s'], label='Red Velocity')
    plt.plot(data['timestamp_s'], data['white_velocity_mm_s'], label='White Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (mm/s)')
    plt.title(f'Velocities Over Time - {plot_title}')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig(os.path.join(graphs_directory, f'{filename}_velocities_vs_time.png'))

    plt.close('all')

csv_directory = 'data_post_processor\\processed_results'

for csv_file in os.listdir(csv_directory):
    if csv_file.endswith('.csv'):
        create_plots(os.path.join(csv_directory, csv_file))
        print(f'Plots created for {csv_file}')
