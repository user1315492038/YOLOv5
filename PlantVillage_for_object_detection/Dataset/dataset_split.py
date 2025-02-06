import os
import shutil
import random

image_path = r"C:/Users/13154/Downloads/Documents/YOLOv5/PlantVillage_for_object_detection\Dataset/images"
label_path = r"C:/Users/13154/Downloads/Documents/YOLOv5/PlantVillage_for_object_detection\Dataset/images"

train_image_path = r"C:/Users/13154/Documents/test/TestPlantVillage/TestPlantVillage/train/images"
val_image_path = r"C:/Users/13154/Documents/test/TestPlantVillage/TestPlantVillage/val/images"
test_image_path = r"C:/Users/13154/Documents/test/TestPlantVillage/TestPlantVillage/test/images"

train_label_path = r"C:/Users/13154/Documents/test/TestPlantVillage/TestPlantVillage/train/labels"
val_label_path = r"C:/Users/13154/Documents/test/TestPlantVillage/TestPlantVillage/val/labels"
test_label_path = r"C:/Users/13154/Documents/test/TestPlantVillage/TestPlantVillage/test/labels"

#total_number = 567,大致按照7:2:1划分
train_number = 396
val_number = 114
test_number = 57

def split_dataset(image_path, label_path, train_image_path, val_image_path, test_image_path, train_label_path, val_label_path, test_label_path):
    images = [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]
    random.shuffle(images)

    train_images = images[:train_number]
    val_images = images[train_number:train_number+val_number]
    test_images = images[train_number+val_number:]

    for image in train_images:
        shutil.copy(os.path.join(image_path, image), os.path.join(train_image_path, image))
        shutil.copy(os.path.join(label_path, image[:-4]+".txt"), os.path.join(train_label_path, image[:-4]+".txt"))

    for image in val_images:
        shutil.copy(os.path.join(image_path, image), os.path.join(val_image_path, image))
        shutil.copy(os.path.join(label_path, image[:-4]+".txt"), os.path.join(val_label_path, image[:-4]+".txt"))

    for image in test_images:       
        shutil.copy(os.path.join(image_path, image), os.path.join(test_image_path, image))
        shutil.copy(os.path.join(label_path, image[:-4]+".txt"), os.path.join(test_label_path, image[:-4]+".txt"))
    
    print("数据集划分完成")