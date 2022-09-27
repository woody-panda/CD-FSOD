

![image](https://github.com/Paper-ID-1349/CD-FSOD/blob/main/figures/fig1.png)

# Introduction
This repo contains the official PyTorch implementation of our paper CD-FSOD: A Benchmark for Cross-domain Few-shot Object Detection.


### Datasets


### Source domain: 

*[MS COCO](https://cocodataset.org/#home)

### Target domains: 

*[ArTaxOr](https://www.kaggle.com/datasets/mistag/arthropod-taxonomy-orders-object-detection-dataset)
*[UODD](https://github.com/LehiChiang/Underwater-object-detection-dataset)
*[DIOR](https://drive.google.com/drive/folders/1UdlgHk49iu6WpcJ5467iT-UqNPpx__CC)
*[ChestX](https://github.com/TRKuan/cxr8)

## Quick Start

#### 1. Requirements.
* python >= 3.8
* detectron2 == 0.6
* PyTorch >= 1.9 & torchvision that matches the PyTorch version.
* CUDA==11.3
* GCC >= 5.4
#### 2. Download the pre-trained weights (R101-FPN, 3x) from [detectron/model_zoo](https://github.com/facebookresearch/detectron2/blob/main/MODEL_ZOO.md)，put it in the folder pretrained/.

#### 3. Download the pre-processed datasets from [here](https://drive.google.com/file/d/1RLfAMTS6Z-ArpqYIO6FoH1xv9JZ1X4HU/view?usp=sharing), put it in the folder datasets.

#### 4. Fine-tuning and Evaluation

```
    bash run.sh [dataset]
```
    
For example:

```
    bash run.sh DIOR
```

### References
[1] Lin, Tsung-Yi, et al. "Microsoft coco: Common objects in context." European conference on computer vision. Springer, Cham, 2014.

[2] https://www.kaggle.com/datasets/mistag/arthropod-taxonomy-orders-object-detection-dataset

[3] Jiang, Lihao, et al. "Underwater species detection using channel sharpening attention." Proceedings of the 29th ACM International Conference on Multimedia. 2021.

[4] Li, Ke, et al. "Object detection in optical remote sensing images: A survey and a new benchmark." ISPRS Journal of Photogrammetry and Remote Sensing 159 (2020): 296-307.

[5] Wang, Xiaosong, et al. "Chestx-ray8: Hospital-scale chest x-ray database and benchmarks on weakly-supervised classification and localization of common thorax diseases." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.
