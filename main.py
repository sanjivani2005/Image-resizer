import cv2

# Read the image
src = cv2.imread("mummy.jpg", cv2.IMREAD_UNCHANGED)

# Check if the image was successfully opened
if src is None:
    print("Error: Could not open or find the image.")
    exit()

# Display the original image
cv2.imshow("Original Image", src)

# Scale the image
scale_percent = 50  # percent of original size
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
dsize = (width, height)

# Resize the image
output = cv2.resize(src, dsize)

# Save the resized image
cv2.imwrite('newImage.png', output)

# Display the resized image
cv2.imshow("Resized Image", output)

# Wait for a key press indefinitely or for a specified amount of time
cv2.waitKey(0)

# Destroy all the windows opened by OpenCV
cv2.destroyAllWindows()
