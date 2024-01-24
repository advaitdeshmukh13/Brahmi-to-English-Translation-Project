import os
from torchvision import transforms
from PIL import Image

# Specify the path to your dataset
dataset_path = "C:/Users/advai/Downloads/internship/data/Dataset/cleaned_d1"

# Specify the path to the augmented dataset
augmented_dataset_path = "C:/Users/advai/Downloads/internship/Dataset/augmented_dataset"

# Create the augmented dataset folder if it doesn't exist
os.makedirs(augmented_dataset_path, exist_ok=True)

# Define the customized transformations
data_transform = transforms.Compose([
    transforms.RandomResizedCrop(224, scale=(0.95, 1.05)),
    transforms.RandomAffine(degrees=1, translate=(0.05, 0.05), shear=5),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    transforms.ToTensor(),
])

# Loop through each subfolder in the original dataset
for subfolder_name in os.listdir(dataset_path):
    subfolder_path = os.path.join(dataset_path, subfolder_name)

    # Create a subfolder in the augmented dataset folder
    augmented_subfolder_path = os.path.join(augmented_dataset_path, subfolder_name)
    os.makedirs(augmented_subfolder_path, exist_ok=True)

    # Loop through each image in the subfolder
    for i, image_name in enumerate(os.listdir(subfolder_path), start=1):
        image_path = os.path.join(subfolder_path, image_name)

        # Open the image
        image = Image.open(image_path)

        # Apply the transformations four times and save each augmented image
        for j in range(4):
            augmented_image = data_transform(image)

            # Save the augmented image to the new subfolder with the desired name format
            augmented_image_name = f"{subfolder_name}_{i}_augmented_{j + 1}.png"
            augmented_image_path = os.path.join(augmented_subfolder_path, augmented_image_name)
            transforms.functional.to_pil_image(augmented_image).save(augmented_image_path)