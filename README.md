

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

Under the proposed benchmarks, we evaluate existing FSOD methods, including meta-learning-based methods and fine-tuning learning.  We use their official implementation.

#### meta-learning methods
* [A-RPN](https://github.com/fanq15/FewX) [6]
* [H-GCN](https://github.com/GuangxingHan/QA-FewDet) [7]
* [Meta-RCNN ](https://github.com/guangxinghan/meta-faster-r-cnn) [8]

#### fine-tuned learning
*  [TFA](https://github.com/ucbdrive/few-shot-object-detection) [9]
*  [FSCE](https://github.com/megvii-research/FSCE) [10]
*  [DeFRCN](https://github.com/er-muyue/DeFRCN) [11]

## Quick Start

#### 1. Check Requirements.
* python >= 3.8
* detectron2 == 0.6
* PyTorch >= 1.10 & torchvision that matches the PyTorch version.
* CUDA==11.3
* GCC >= 5.4

#### 2. Build Environment

* Clone Code

```
git clone https://github.com/Paper-ID-1349/CD-FSOD.git
cd CD-FSOD
```

* Install PyTorch 1.10 with CUDA 11.3

```
conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 cudatoolkit=11.3 -c pytorch -c conda-forge
```

* Install [Detectron2](https://github.com/facebookresearch/detectron2)

```
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
```

* Install other requirements.
 
 ```
python -m pip install -r requirements.txt
```

#### 3. Prepare Data and Weights

* Data Preparation
    * Data splits. Download the preprocessed datasets from [here](https://drive.google.com/file/d/1RLfAMTS6Z-ArpqYIO6FoH1xv9JZ1X4HU/view?usp=sharing)
    * Unzip the downloaded data-source to datasets and put it into your project directory:

     ```
     ...
     datasets
       | -- coco (trainval2014/*.jpg, val2014/*.jpg, annotations/*.json)
       | -- cocosplit
       | -- VOC2007
       | -- VOC2012
       | -- vocsplit
     defrcn
     tools
     ...
     ```




#### 4. Fine-tuning and Evaluation

```
    bash run.sh [dataset]
```
    
For example:

```
    bash run.sh DIOR
```

### References
[1] Lin, Tsung-Yi, et al. "Microsoft coco: Common objects in context." ECCV 2014.

[2] https://www.kaggle.com/datasets/mistag/arthropod-taxonomy-orders-object-detection-dataset

[3] Jiang, Lihao, et al. "Underwater species detection using channel sharpening attention." ACM MM 2021.

[4] Li, Ke, et al. "Object detection in optical remote sensing images: A survey and a new benchmark." ISPRS J. Photogramm. Remote Sens. 2020).

[5] Wang, Xiaosong, et al. "Chestx-ray8: Hospital-scale chest x-ray database and benchmarks on weakly-supervised classification and localization of common thorax diseases." CVPR 2017.

[6] Fan, Qi, et al. "Few-shot object detection with attention-RPN and multi-relation detector." CVPR 2020.

[7] Han, Guangxing, et al. "Query adaptive few-shot object detection with heterogeneous graph convolutional networks." ICCV 2021.

[8] Han, Guangxing, et al. "Meta faster r-cnn: Towards accurate few-shot object detection with attentive feature alignment." AAAI 2022.

[9]  Wang, Xin, et al. "Frustratingly Simple Few-Shot Object Detection." ICML 2020.

[10] Sun, Bo, et al. "Fsce: Few-shot object detection via contrastive proposal encoding." CVPR 2021.

[11] Qiao, Limeng, et al. "Defrcn: Decoupled faster r-cnn for few-shot object detection." ICCV 2021.
