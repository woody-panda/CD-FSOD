

![image](https://github.com/Paper-ID-1349/CD-FSOD/blob/main/figures/fig1.png)

### Introduction
This repo contains the official PyTorch implementation of our paper CD-FSOD: A Benchmark for Cross-domain Few-shot Object Detection.


### Datasets


#### Source domain: 

* [MS COCO](https://cocodataset.org/#home)

#### Target domains: 

* [ArTaxOr](https://www.kaggle.com/datasets/mistag/arthropod-taxonomy-orders-object-detection-dataset)

* [UODD](https://github.com/LehiChiang/Underwater-object-detection-dataset)

* [DIOR](https://drive.google.com/drive/folders/1UdlgHk49iu6WpcJ5467iT-UqNPpx__CC)

* [ChestX](https://github.com/TRKuan/cxr8)

#### Dataset Statistics

| Dataset | classses | train images | test images |
| :-----: | :----: | :----: | :----: |
| ArTaxOr | 7 | 13,991 | 1,383 |
| UODD | 3 | 3,194 | 506 |
| DIOR | 20 | 18,463 | 5,000 |
| ChestX | 8 | 700 | 180 |

### Baselines

Under the proposed benchmarks, we evaluate existing FSOD methods, including meta-learning-based methods and fine-tuning learning.

#### meta-learning methods
* A-RPN [6], the official implementation is [here](https://github.com/fanq15/FewX)
* H-GCN [7], the official implementation is [here](https://github.com/GuangxingHan/QA-FewDet)  
* Meta-RCNN [8],  the official implementation is [here](https://github.com/guangxinghan/meta-faster-r-cnn)

#### fine-tuned learning
* TFA [9], the official implementation is [here](https://github.com/ucbdrive/few-shot-object-detection)
* FSCE [10], the official implementation is [here](https://github.com/megvii-research/FSCE)
* DeFRCN [11], the official implementation is [here](https://github.com/er-muyue/DeFRCN)

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

[6] Fan, Qi, et al. "Few-shot object detection with attention-RPN and multi-relation detector." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.

[7] Han, Guangxing, et al. "Query adaptive few-shot object detection with heterogeneous graph convolutional networks." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.

[8] Han, Guangxing, et al. "Meta faster r-cnn: Towards accurate few-shot object detection with attentive feature alignment." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 36. No. 1. 2022.

[9]  Wang, Xin, et al. "Frustratingly Simple Few-Shot Object Detection." ICML 2020.

[10] Sun, Bo, et al. "Fsce: Few-shot object detection via contrastive proposal encoding." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.

[11] Qiao, Limeng, et al. "Defrcn: Decoupled faster r-cnn for few-shot object detection." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.
