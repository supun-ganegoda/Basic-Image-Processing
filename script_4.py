# ---------------------------------------------------------
#   Name : Ganegoda G.S.S.S
#   Reg No: EG/2019/3588
#   Take Home Assignment 1
#   Question 4
# ---------------------------------------------------------
# import required libraries
import cv2
import numpy as np

# Read the original image
image = cv2.imread('data/sample.jpg', cv2.IMREAD_COLOR)

# Define block sizes
block_sizes = [3, 5, 7]

# Function to process the image with a given block size
def process_image(image, block_size):
    processed_image = np.copy(image)

    # Iterate over each block
    for y in range(0, image.shape[0], block_size):
        for x in range(0, image.shape[1], block_size):
            # Define the region of interest (ROI)
            roi = image[y:y+block_size, x:x+block_size]
            # Calculate the mean of the ROI
            mean_color = np.mean(roi, axis=(0, 1))
            # Replace the ROI with the mean color
            processed_image[y:y+block_size, x:x+block_size] = mean_color

    return processed_image

# Process the image for each block size
processed_images = [process_image(image, size) for size in block_sizes]

# Display original and processed images in separate windows
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', image)

for i, processed_image in enumerate(processed_images):
    window_name = f'Processed Image {block_sizes[i]}x{block_sizes[i]}'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, processed_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
