import pandas as pd
import numpy as np
import os

def compute_velocity(position, time_interval, velocity_threshold=5000):
    # Compute the gradient of position
    velocity = np.gradient(position)
    
    # Divide by time_interval, avoid divide-by-zero by setting those points to NaN
    velocity[time_interval == 0] = np.nan
    velocity /= time_interval
    
    # Set velocities above the threshold to NaN (remove them)
    velocity[np.abs(velocity) > velocity_threshold] = np.nan
    
    return velocity

# Create the output directory if it doesn't exist
output_dir = "data_post_processor\\processed_results"
os.makedirs(output_dir, exist_ok=True)

# Iterate through the files
for i in range(100514, 100566):
    input_file = f"data_post_processor\\filtered_results\\P{i}_results_filtered.csv"
    
    if os.path.exists(input_file):
        # Load the CSV data
        df = pd.read_csv(input_file)
        
        # Calculate time interval and adjust length to match position data
        time_interval = np.diff(df['timestamp_s'])
        adjusted_time_interval = np.concatenate(([0], time_interval))  # Add a leading zero

        # Calculate velocity for red and white balls in mm/s
        df['red_velocity_mm_s'] = compute_velocity(df['red_relative_Y_mm'], adjusted_time_interval)
        df['white_velocity_mm_s'] = compute_velocity(df['white_relative_Y_mm'], adjusted_time_interval)

        # Round the velocity values to 4 decimal places, ensuring NaNs are handled properly
        df['red_velocity_mm_s'] = df['red_velocity_mm_s'].round(4)
        df['white_velocity_mm_s'] = df['white_velocity_mm_s'].round(4)

        # Create a new dataframe with the required columns
        output_df = df[['timestamp_s', 'red_relative_Y_mm', 'white_relative_Y_mm', 'red_velocity_mm_s', 'white_velocity_mm_s']]

        # Generate output file path
        output_file = os.path.join(output_dir, f"P{i}_results_processed.csv")
        
        # Output the result to a new CSV file
        output_df.to_csv(output_file, index=False)
        
        print(f"Processed data saved to {output_file}")
    else:
        print(f"File {input_file} not found, skipping...")
