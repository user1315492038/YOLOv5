import os
import shutil
from sklearn.model_selection import train_test_split

# 设置数据集目录和目标划分目录
data_dir = "C:/Users/13154/Downloads/Documents/YOLOv5/data/TrainPlantVillage/images/test"  # 原始数据集目录
output_dir = "C:/Users/13154/Downloads/Documents/YOLOv5/data/ReducedPlantVillage/images"  # 输出数据集目录
splits = ["train", "val", "test"]  # 数据划分
split_ratios = (0.7, 0.2, 0.1)  # 比例：70% 训练集，20% 验证集，10% 测试集

# 创建输出目录结构
for split in splits:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# 遍历每个子目录（每个标签）
for label in os.listdir(data_dir):
    label_dir = os.path.join(data_dir, label)
    if not os.path.isdir(label_dir):
        continue  # 跳过非目录

    # 获取该标签下所有文件
    files = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if os.path.isfile(os.path.join(label_dir, f))]

    # 按比例划分数据集
    train_files, temp_files = train_test_split(files, test_size=1 - split_ratios[0], random_state=42)
    valid_files, test_files = train_test_split(temp_files, test_size=split_ratios[2] / (split_ratios[1] + split_ratios[2]), random_state=42)

    # 将文件复制到目标目录
    for split, split_files in zip(splits, [train_files, valid_files, test_files]):
        split_label_dir = os.path.join(output_dir, split, label)
        os.makedirs(split_label_dir, exist_ok=True)
        for file_path in split_files:
            shutil.copy(file_path, os.path.join(split_label_dir, os.path.basename(file_path)))

print("数据集划分完成！")
