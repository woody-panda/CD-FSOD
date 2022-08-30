# CD-FSOD
Here is the code for ''CD-FSOD: A Benchmark for Cross-domain Few-shot Object Detection''
Get preprocessed data and the pretrained weights from [here](https://drive.google.com/file/d/1RLfAMTS6Z-ArpqYIO6FoH1xv9JZ1X4HU/view?usp=sharing).

## Introduction

The proposed CD-FSOD benchmark includes four target datasets (ArTaxOr[2], UOOD [3], DIOR [4] and ChestX [5]) and a base dataset ( MS COCO [1]). These datasets cover arthropod images, underwater images, satellite images and X-ray images, respectively. The selected datasets reflect well-curated real-world use cases for few-shot object detection. In addition, collecting enough examples from the above domains is often difficult, expensive, or in some cases not possible. Image similarity to natural images is measured by 3 orthogonal criteria: 1) existence of perspective distortion, 2) the semantic data content, and 3) colour depth. According to these criteria, the datasets demonstrate the following spectrum of image types: 1) ArTaxOr images are natural images, but are fine-grained (specific to biology)  2) UOOD images are less similar as the poor visibility and low colour contrast, but are still colour images of natural scenes, 3) DIOR images are even less similar as they have lost perspective distortion, 4) ChestX images are the most dissimilar as they have lost perspective distortion, do not represent natural scenes, and have lost 2 colour channels.


## Datasets
The following datasets are used for evaluation in this benchmark:

### Source domain:

* [MS COCO](https://cocodataset.org/#home)


### Target domains:

 * [ArTaxOr](https://www.kaggle.com/datasets/mistag/arthropod-taxonomy-orders-object-detection-dataset)
 * [UOOD](https://github.com/LehiChiang/Underwater-object-detection-dataset)
 * [DIOR](https://gcheng-nwpu.github.io/#Datasets)
 * [ChestX](https://github.com/TRKuan/cxr8)


### References
[1] Lin, Tsung-Yi, et al. "Microsoft coco: Common objects in context." European conference on computer vision. Springer, Cham, 2014.

[2] https://www.kaggle.com/datasets/mistag/arthropod-taxonomy-orders-object-detection-dataset

[3] Jiang, Lihao, et al. "Underwater species detection using channel sharpening attention." Proceedings of the 29th ACM International Conference on Multimedia. 2021.

[4] Li, Ke, et al. "Object detection in optical remote sensing images: A survey and a new benchmark." ISPRS Journal of Photogrammetry and Remote Sensing 159 (2020): 296-307.

[5] Wang, Xiaosong, et al. "Chestx-ray8: Hospital-scale chest x-ray database and benchmarks on weakly-supervised classification and localization of common thorax diseases." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.
