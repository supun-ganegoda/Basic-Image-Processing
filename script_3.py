# ---------------------------------------------------------
#   Name : Ganegoda G.S.S.S
#   Reg No: EG/2019/3588
#   Take Home Assignment 1
#   Question 3
# ---------------------------------------------------------
# import required libraries
import cv2

# Read the original image
image = cv2.imread('data/sample.jpg')

# Rotate the image by 45 degrees clockwise
rows, cols = image.shape[:2]
rotation_matrix_45 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated_image_45 = cv2.warpAffine(image, rotation_matrix_45, (cols, rows))

# Rotate the image by 90 degrees clockwise
rotation_matrix_90 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
rotated_image_90 = cv2.warpAffine(image, rotation_matrix_90, (cols, rows))

windows = ['Original Image', 'Rotated Image 45', 'Rotated Image 90']

# Create windows to display images
for window in windows:
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, 640, 480)

# Display images
cv2.imshow(windows[0], image)
cv2.imshow(windows[1], rotated_image_45)
cv2.imshow(windows[2], rotated_image_90)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
