# CD-FSOD
Here is the code for ''Cross-domain Few-shot Object Detection with Self-Ensemble and Self-Distillation''
Get preprocessed data and the pretrained weights from [here](https://github.com/XXX-YES/FSOD).

## Introduction

The Cross-Domain Few-Shot Object Detection (CD-FSOD) benchmark includes data from the ArTaxOr [1], UOOD [2], DIOR [3-4], and ChestX [5] datasets, which covers arthropod images, satellite images, underwater images, and X-ray images, respectively. The selected datasets reflect real-world use cases for few-shot learning since collecting enough examples from above domains is often difficult, expensive, or in some cases not possible. In addition, they demonstrate the following spectrum of readily quantifiable domain shifts from MS COCO: 1) Arthropod images are most similar as they include perspective color images of natural elements, but are more specialized than anything available in MS COCO, 2) UOOD images are less similar as they have lost perspective distortion, but are still color images of natural scenes, 3) ISIC2018 images are even less similar as they have lost perspective distortion and no longer represent natural scenes, and 4) ChestX images are the most dissimilar as they have lost perspective distortion, all color, and do not represent natural scenes.


## Datasets
The following datasets are used for evaluation in this benchmark:

### Source domain:

* MS COCO


### Target domains:

 * ArTaxOr
 * UOOD
 * DIOR
 * ChestX


### References
[1] Sharada P Mohanty, David P Hughes, and Marcel Salathe. Using deep learning for image based plant disease detection. Frontiers in plant science, 7:1419, 2016

[2] Patrick Helber, Benjamin Bischke, Andreas Dengel, and Damian Borth. Eurosat: A novel dataset and deep learning benchmark for land use and land cover classification. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing , 12(7):2217–2226, 2019.

[3] Philipp Tschandl, Cliff Rosendahl, and Harald Kittler. The ham10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions. Scientific data, 5:180161, 2018.

[4] Noel Codella, Veronica Rotemberg, Philipp Tschandl, M Emre Celebi, Stephen Dusza, David Gutman, Brian Helba, Aadi Kalloo, Konstantinos Liopyris, Michael Marchetti, et al. Skin lesion analysis toward melanoma detection 2018: A challenge hosted by the international skin imaging collaboration (isic). arXiv preprint. arXiv:1902.03368, 2019

[5] Xiaosong Wang, Yifan Peng, Le Lu, Zhiyong Lu, Mohammadhadi Bagheri, and Ronald M Summers. Chestx-ray8: Hospital-scale chest x-ray database and benchmarks on weakly supervised classification and localization of common thorax diseases. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 2097–2106, 2017
