import os
import torch

# 加载预训练的 YOLOv5 模型
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# 指定图片目录和标签目录
image_dir = r"C:/Users/13154/Downloads/Documents/YOLOv5/yolov5-7.0/yolov5-7.0/data/TrainPlantVliiage/images"
labels_dir = r"C:/Users/13154\Downloads/Documents/YOLOv5/yolov5-7.0/yolov5-7.0/data/TrainPlantVillage/labels"

# 确保标签目录存在
os.makedirs(labels_dir, exist_ok=True)

# 遍历图片目录中的所有图片
for image_file in os.listdir(image_dir):
    if image_file.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(image_dir, image_file)
        
        # 使用 YOLOv5 模型检测图片中的对象
        results = model(image_path)
        
        # 获取检测结果
        detections = results.xywh[0]  # xywh 格式的检测结果
        
        # 获取图片文件名（不带扩展名）
        image_name = os.path.splitext(image_file)[0]
        # 创建对应的标签文件路径
        label_file = os.path.join(labels_dir, f"{image_name}.txt")
        
        # 将检测结果写入标签文件
        with open(label_file, 'w') as f:
            for detection in detections:
                class_id = int(detection[5])  # 类别索引
                x_center, y_center, width, height = detection[:4]
                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

print(f"标签文件已保存到 {labels_dir}")