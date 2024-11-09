# Run the following before executing this script - conda activate yolov8
yolo val model="yolov8n_weights_custom_v2.pt" data=dataset_test.yaml batch=16 imgsz=640
# conda deactivate yolov8