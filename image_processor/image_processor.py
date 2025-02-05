import cv2
import numpy as np
import csv
import os

# Constants
FILE_NAME = 'P1000565.MP4'
DROP_HEIGHT_MM = 500

WHITE_BALL_DIAMETER_MM = 215
WHITE_BALL_RADIUS_MM = WHITE_BALL_DIAMETER_MM / 2
RED_BALL_DIAMETER_MM = 63.5
RED_BALL_RADIUS_MM = RED_BALL_DIAMETER_MM / 2

PIXELS_PER_METRES = 764  # Conversion: 764 pixels = 2.0 meter
MM_PER_PIXEL = 2000 / PIXELS_PER_METRES  # Conversion to millimeters

# Look for the bounding box of the largest red region in the frame
def find_red_ball(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
    mask = mask1 + mask2

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest_contour) > 500:
            x, y, w, h = cv2.boundingRect(largest_contour)
            return x, y, w, h
    return None

# Look for the bounding box that covers most of the green pixels in the frame
# This is detecting the green tape on the white ball
def find_white_ball(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 50, 20])
    upper_green = np.array([85, 255, 150])

    mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.erode(mask, kernel, iterations=1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest_contour) > 500:
            x, y, w, h = cv2.boundingRect(largest_contour)
            return x, y, w, h
    return None


def process_video_with_two_balls(video_path, scale_factor=0.5):
    # Create the output directory
    output_dir = os.path.join('image_processor', 'results')
    os.makedirs(output_dir, exist_ok=True)

    # Open video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    # Output to a CSV file
    csv_filename = os.path.join(output_dir, f"{video_name}_results.csv")

    # Prepare CSV file for writing
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header row for the CSV
        writer.writerow(['frame_no', 'timestamp_s', 
                         'red_absolute_x_px', 'red_absolute_y_px', 'red_relative_X_mm', 'red_relative_Y_mm', 
                         'white_absolute_X_px', 'white_absolute_Y_px', 'white_relative_X_mm', 'white_relative_Y_mm'])

        fps = cap.get(cv2.CAP_PROP_FPS)

        frame_count = 0
        red_start_x, red_start_y = None, None
        white_start_x, white_start_y = None, None

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            timestamp = round(frame_count / fps, 4)

            # Find red ball
            red_bbox = find_red_ball(frame)

            # Find white ball
            white_bbox = find_white_ball(frame)

            # Scale the frame
            frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

            # Initialize red ball data
            red_offset_x_mm = red_offset_y_mm = None

            if red_bbox:
                x, y, w, h = red_bbox
                x = int(x * scale_factor)
                y = int(y * scale_factor)
                w = int(w * scale_factor)
                h = int(h * scale_factor)

                red_bottom_left_x = x
                red_bottom_left_y = y + h

                # Set starting position, if it is the first time it is detected
                if red_start_x is None and red_start_y is None:
                    red_start_x, red_start_y = red_bottom_left_x, red_bottom_left_y

                # Calculate offset in mm
                red_offset_x_mm = round((red_bottom_left_x - red_start_x) * MM_PER_PIXEL, 4)
                red_offset_y_mm = round((red_bottom_left_y - red_start_y) * MM_PER_PIXEL, 4)
                red_offset_x_mm = (DROP_HEIGHT_MM + WHITE_BALL_RADIUS_MM + RED_BALL_RADIUS_MM)- red_offset_x_mm
                red_offset_x_mm = round(red_offset_x_mm, 4)

                # Draw green bounding box for the red ball
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            white_offset_x_mm = white_offset_y_mm = None

            if white_bbox:
                x, y, w, h = white_bbox
                x = int(x * scale_factor)
                y = int(y * scale_factor)
                w = int(w * scale_factor)
                h = int(h * scale_factor)

                white_bottom_left_x = x
                white_bottom_left_y = y + h

                # Set starting position, if it is the first time it is detected
                if white_start_x is None and white_start_y is None:
                    white_start_x, white_start_y = white_bottom_left_x, white_bottom_left_y

                # Calculate offset in mm
                white_offset_x_mm = round((white_bottom_left_x - white_start_x) * MM_PER_PIXEL, 4)
                white_offset_y_mm = round((white_bottom_left_y - white_start_y) * MM_PER_PIXEL, 4)
                white_offset_x_mm = DROP_HEIGHT_MM - white_offset_x_mm
                white_offset_x_mm = round(white_offset_x_mm, 4)

                # Draw red bounding box for the white ball
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


            # Write frame data to the CSV
            writer.writerow([frame_count, timestamp,
                             red_bottom_left_y, red_bottom_left_x, red_offset_y_mm, red_offset_x_mm,
                             white_bottom_left_y, white_bottom_left_x, white_offset_y_mm, white_offset_x_mm])

            # Display the frame with bounding boxes (for visualization)
            cv2.imshow('Ball Tracker', frame)

            # Next frame
            frame_count += 1

            # Allows one to press 'q' to exit
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


# Process the video
video_path = 'image_processor\\videos\\' + FILE_NAME
process_video_with_two_balls(video_path, scale_factor=0.5)
