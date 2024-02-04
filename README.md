# YOLOv7 DeepSORT ReId

![flirbnw1](https://github.com/chronomustard/YOLOv7-DeepSORT-Thermal/assets/70846916/41991daf-637a-4afc-9350-f127e574e55e)

This GitHub repository provides documentation and resources for developers looking to integrate YOLOv7 and DeepSORT for Reidentification tasks, specifically tailored for thermal datasets. The repository includes pretrained weights for a thermal reidentification dataset based on market-1501.

## Features

- **Released Versions**: The repository includes the first release of the pretrained weights for thermal datasets (Pretrained-base v0.1).

- **Architecture**: The Reidentification (ReId) algorithm is built using YOLO and DeepSORT on Python 3.7.16. Dependencies are listed in the `requirements.txt` file.

- **Getting Started**: Detailed information on minimum requirements, Conda installation, and configuration of TensorFlow and PyTorch for GPU support.

- **Datasets and Pretrained Weights**: Utilizes a market-1501-based custom dataset compiled from ThermalDB, RegDB, market-1501, and IndoThermal. Pretrained weights are accessible from a provided URL.

- **DeepSORT-YOLOv7 Reidentification**: Instructions for configuring and running the DeepSORT-YOLOv7 reidentification program, along with the necessary resources.

## How to Use

1. Clone the repository.
2. Follow the detailed documentation for setting up the environment, installing dependencies, and configuring YOLOv7 and DeepSORT.
3. Access pretrained weights and run reidentification algorithms as per the provided guidelines.

## Issues

Open and create issues if you've encountered any. I'll try my best to resolve your issue asap.

## References

- [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
- [YOLOv7-DeepSORT-Thermal Environment](https://github.com/chronomustard/YOLOv7-DeepSORT-Thermal/tree/main/env)
- [CUDA Installation Guide for Microsoft Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)
- [CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- [Get Started with PyTorch - Previous Versions](https://pytorch.org/get-started/previous-versions/)
- [YOLOv7 Custom Dataset Training Tutorial](https://blog.roboflow.com/yolov7-custom-dataset-training-tutorial/)
- [DeepSORT PyTorch](https://github.com/ZQPei/deep_sort_pytorch)
- [Market-1501 Dataset](https://www.kaggle.com/datasets/whurobin/market-1501)
- [YOLOv7-DeepSORT-Thermal Preprocessing Scripts](https://github.com/chronomustard/YOLOv7-DeepSORT-Thermal/tree/main/deepSORT_preprocessing_script)
- [YOLOv7-DeepSORT-Thermal](https://github.com/chronomustard/YOLOv7-DeepSORT-Thermal/tree/main)
- [Scalable Person Re-Identification: A Benchmark](https://openaccess.thecvf.com/content_iccv_2015/html/Zheng_Scalable_Person_Re-Identification_ICCV_2015_paper.html)

Explore the repository for in-depth guides and resources to enhance your reidentification tasks using YOLOv7 and DeepSORT on thermal datasets.
