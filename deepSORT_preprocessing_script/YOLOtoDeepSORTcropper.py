from PIL import Image
import os

from PIL import Image
import os

def crop_images_with_labels(dataset_path, labels_folder, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for label_file in os.listdir(labels_folder):
        label_file_path = os.path.join(labels_folder, label_file)

        with open(label_file_path, 'r') as file:
            lines = file.readlines()

        image_filename = os.path.splitext(label_file)[0] + ".jpg"
        image_path = os.path.join(dataset_path, image_filename)

        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            continue

        try:
            img = Image.open(image_path)
        except Exception as e:
            print(f"Error opening image: {image_path}")
            print(e)
            continue

        for line in lines:
            data = line.strip().split(' ')
            if len(data) < 5:
                print(f"Invalid label format in file {label_file_path}: {line}")
                continue

            label = data[0]
            coordinates = list(map(float, data[1:]))  # x_center, y_center, box_width, box_height

            x_center, y_center, box_width, box_height = coordinates
            image_width, image_height = img.size

            # Convert normalized coordinates to pixel values
            x_min = int((x_center - (box_width / 2)) * image_width)
            y_min = int((y_center - (box_height / 2)) * image_height)
            x_max = int((x_center + (box_width / 2)) * image_width)
            y_max = int((y_center + (box_height / 2)) * image_height)

            # Ensure coordinates are within image boundaries
            x_min = max(0, min(x_min, image_width))
            y_min = max(0, min(y_min, image_height))
            x_max = max(0, min(x_max, image_width))
            y_max = max(0, min(y_max, image_height))

            try:
                cropped_img = img.crop((x_min, y_min, x_max, y_max))

                # Resize cropped image to 64x128
                cropped_img = cropped_img.resize((64, 128))

                # Create directory for each class
                class_output_dir = os.path.join(output_dir, label)
                os.makedirs(class_output_dir, exist_ok=True)

                # Save cropped image to respective class folder
                save_path = os.path.join(class_output_dir, f"{label}_{image_filename}")
                cropped_img.save(save_path)
                print(f"Saved {label} as {save_path}")
            except Exception as e:
                print(f"Error cropping {label} from {image_filename}: {e}")

# Update paths accordingly
dataset_directory = r'C:\Users\USER\Downloads\thermal_infrared.v7i.yolov7pytorch\train\images'
labels_folder = r'C:\Users\USER\Downloads\thermal_infrared.v7i.yolov7pytorch\train\labels'
output_directory = r'C:\Users\USER\Downloads\thermal_infrared.v7i.yolov7pytorch\cropped_images_1'

crop_images_with_labels(dataset_directory, labels_folder, output_directory)
