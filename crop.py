from PIL import Image
print('start')
# Load the original image
original_image = Image.open("Adobe Scan 27-Dec-2023_page-0002.jpg")

# Define the size of each character (assuming equal spacing)
char_width = original_image.width // 12
char_height = original_image.height // 18

# Counter for file naming
file_counter = 217

# Loop through each row and column to crop individual characters
for row in range(18):
    for col in range(12):
        # Calculate the coordinates for cropping
        left = col * char_width
        upper = row * char_height
        right = left + char_width
        lower = upper + char_height

        # Crop the character
        char_image = original_image.crop((left, upper, right, lower))

        # Save the cropped character to a new file with the desired naming convention
        char_image.save(f"output/char_{file_counter}.jpg")

        # Increment the file counter
        file_counter += 1


print('end')