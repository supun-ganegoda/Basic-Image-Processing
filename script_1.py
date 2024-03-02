# ---------------------------------------------------------
#   Name : Ganegoda G.S.S.S
#   Reg No: EG/2019/3588
#   Take Home Assignment 1
#   Question 1
# ---------------------------------------------------------
# import required libraries
import cv2

# Read the image
image = cv2.imread('data/sample.jpg', cv2.IMREAD_GRAYSCALE)

# Define a window to display the image
window_name = 'Intensity Adjustment Display'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

# Define a track bar to adjust intensity
max_intensity = 8  
initial_intensity = 3  
current_intensity = initial_intensity

def update_intensity(value):
    global current_intensity
    current_intensity = 2 ** value
    # Update the image intensity
    updated_image = (image * (current_intensity / max_intensity)).astype('uint8')
    cv2.imshow(window_name, updated_image)

# Create a track bar
cv2.createTrackbar('Intensity', window_name, initial_intensity, max_intensity, update_intensity)

# Display the initial image
cv2.imshow(window_name, image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
