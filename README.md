# LightWeight-yolov7

### Features
- Small object detection layer is added.
- The original CBS module including ELAN module is replaced with the Ghost convolution.
- The CBAM attention module is added after the last GhostCBS module.

### References
 - https://github.com/WongKinYiu/yolov7
   Please visit the URL to download the weights.

### Steps to run Code
- Clone the repository.
```
git clone https://github.com/Yoshinori-Asada/LightWeight-yolov7.git
```
- Goto the cloned folder.
```
cd LightWeight-yolov7
```
- Create a virtual envirnoment (optional,but recommended)
```
### For Linux Users
python3 -m venv lightweightyolov7
source lightweightyolov7/bin/activate

### For Window Users
python3 -m venv lightweightyolov7
cd lightweightyolov7
cd Scripts
activate
cd ..
cd ..
```
- Upgrade pip with mentioned command below.
```
pip install --upgrade pip
```
- Install requirements with mentioned command below.
```
pip install -r requirements.txt
```
- Run the code with mentioned command below.
```
# transfer learning
python train.py --workers 8 --device 0 --batch-size 32 --data data/dataset.yaml --img 640 640 --cfg cfg/training/yolov7_lw.yaml --weights 'yolov7_training.pt' --name yolov7-custom --hyp data/hyp.scratch.custom.yaml

# test
python test.py --data data/coco.yaml --img 640 --batch 32 --conf 0.001 --iou 0.65 --device 0 --weights 'yolov7_lw.pt' --name yolov7_640_val

# Inference
python detect.py --weights 'yolov7_lw.pt'  --conf 0.25 --img-size 640 --source inference/images/horses.jpg

# Quantization
Please check tutorial.ipynb file.

