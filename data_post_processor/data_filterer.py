import pandas as pd
import os

# Define the range of file names
start_file_num = 514
end_file_num = 565

THRESHOLD = 12.0  # Minimum change in position (mm) to consider the ball as starting to drop

# Define the output directory and ensure it exists
output_dir = "data_post_processor/filtered_results"
os.makedirs(output_dir, exist_ok=True)

# Iterate over all file numbers in the specified range
for file_num in range(start_file_num, end_file_num + 1):
    input_file = f"image_processor\\results\\P1000{file_num}_results.csv"
    
    # Check if the file exists
    if os.path.exists(input_file):
        print(f"Processing file: {input_file}")
        
        # Load the data from the CSV file
        df = pd.read_csv(input_file)

        start_index = None

        # Check the difference between consecutive rows to find when the balls start moving
        for i in range(1, len(df)):
            if abs(df['red_relative_Y_mm'].iloc[i] - df['red_relative_Y_mm'].iloc[i-1]) > THRESHOLD or \
               abs(df['white_relative_Y_mm'].iloc[i] - df['white_relative_Y_mm'].iloc[i-1]) > THRESHOLD:
                start_index = i - 2
                break

        if start_index is None:
            print(f"No significant drop detected in {input_file}. Skipping.")
        else:
            # Filter the data from the detected start point onward
            df_filtered = df.iloc[start_index:].reset_index(drop=True)

            # Reset the timestamp to start from 0
            df_filtered['timestamp_s'] = round(df_filtered['timestamp_s'] - df_filtered['timestamp_s'].iloc[0], 4)

            # Save the filtered data
            output_file = os.path.join(output_dir, f"P100{file_num}_results_filtered.csv")
            df_filtered.to_csv(output_file, index=False)
            print(f"Filtered data saved to {output_file}")
    else:
        print(f"File {input_file} does not exist. Skipping.")
