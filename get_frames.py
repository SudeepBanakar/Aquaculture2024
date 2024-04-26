import cv2
from google.colab.patches import cv2_imshow  # Import cv2_imshow

# Open the video file
vidcap = cv2.VideoCapture(r"/content/beforefeeding.mp4")

# Initialize variables
c = 0

while c < 1000:  # Capture 15 frames
    ret, img = vidcap.read()
    if ret:
        # Save the frame as an image with an incrementing number as the file name
        cv2.imwrite('/content/drive/MyDrive/images2/frame%d.jpg' % c, img)

        # Display the image using cv2_imshow
        cv2_imshow(img)

        c += 1

    # Check if the 'q' key is pressed and exit the loop if it is
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
vidcap.release()
