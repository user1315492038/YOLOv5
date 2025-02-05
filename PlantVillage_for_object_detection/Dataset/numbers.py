import os

def count_files_in_directory(directory):
    # 获取目录中的所有文件和文件夹
    items = os.listdir(directory)
    # 过滤出文件
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
    # 返回文件数量
    return len(files)

# 示例用法
image_path = "PlantVillage_for_object_detection/Dataset/labels"
txt_path = "PlantVillage_for_object_detection/Dataset/labels"
image_count = count_files_in_directory(image_path)
txt_count = count_files_in_directory(txt_path)
print(f"文件夹中有 {image_count} 个文件")
print(f"文件夹中有 {txt_count} 个文件")