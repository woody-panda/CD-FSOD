# CD-FSOD
Here is the code for ''Cross-domain Few-shot Object Detection with Self-Ensemble and Self-Distillation''
Get preprocessed data and the pretrained weights from [here](https://github.com/XXX-YES/FSOD).

## Introduction

The Cross-Domain Few-Shot Object Detection (CD-FSOD)  benchmark includes data from the CropDiseases [1], UOOD [2], DIOR [3-4], and ChestX [5] datasets, which covers arthropod images, satellite images, underwater images, and X-ray images, respectively. The selected datasets reflect real-world use cases for few-shot learning since collecting enough examples from above domains is often difficult, expensive, or in some cases not possible. In addition, they demonstrate the following spectrum of readily quantifiable domain shifts from MS COCO: 1) Arthropod images are most similar as they include perspective color images of natural elements, but are more specialized than anything available in MS COCO, 2) UOOD images are less similar as they have lost perspective distortion, but are still color images of natural scenes, 3) ISIC2018 images are even less similar as they have lost perspective distortion and no longer represent natural scenes, and 4) ChestX images are the most dissimilar as they have lost perspective distortion, all color, and do not represent natural scenes.


##Datasets
The following datasets are used for evaluation in this challenge:

###Source domain:

miniImageNet

%Run the code and get the result

    
   % python train_net.py --num-gpus 4 --config-file ./configs/${dataset}/${shot}_shot.yaml 2>&1 | tee log/${dataset}/${shot}_shot.log
    
