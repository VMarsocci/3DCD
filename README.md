# 3DCD: Inferring 3D change detection from bitemporal optical images

<div align="center">
  <img src="images/logo_3d_cd.png", width="250">
</div>

**3DCD** project has the goal of automatically inferring *2D and 3D change detection (elevation change)* maps of human artefacts from bitemporal optical images, *without the need of relying on DSMs*.

The project is carried out by Virginia Coletta, [Valerio Marsocci](https://sites.google.com/uniroma1.it/valeriomarsocci) and Dr. Roberta Ravanelli, under the supervision of professors Simone Scardapane and Mattia Crespi. 

For more information click on the site **[3DCD](https://sites.google.com/uniroma1.it/3dchangedetection/home-page)** or frame the QR code.
<div align="center">
  <img src="images/qr.png", width="250">
</div>

## Contents
1. [Features](#features)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [Related resources](#relatedresources)
7. [Citation](#citation)
8. [License](#license)

## Features

Change detection is one of the most active research areas in Remote Sensing (RS). Most of the recently developed change detection methods are based on deep learning (DL) algorithms. This kind of algorithms is generally focused on generating two-dimensional (2D) change maps, thus only identifying planimetric changes in land use/land cover (LULC) and not considering nor returning any information on the corresponding *elevation changes*. 

Our work goes one step further, proposing two novel networks, able to solve simultaneously the 2D and 3D CD tasks, and the **3DCD dataset**, a novel and freely available dataset precisely designed for this multitask. Particularly, the aim of this work is to lay the foundations for the development of DL algorithms able to automatically infer an elevation (3D) CD map - together with a standard 2D CD map, starting only from a pair of bitemporal optical images. 

The proposed architecture consists of a transformer-based network, the MultiTask Bitemporal Images Transformer (MTBIT). Particularly, MTBIT is a transformer-based architecture, that makes use of a semantic tokenizer. 
This model is, thus, able to *obtain 3D CD maps from two optical images taken at different time instants, without the need to rely directly on elevation data during the inference step*. Another model capable to solve this problem effectively is SUNet, a modified version of FC-Siam-conc.


## Dataset

At this [link](https://drive.google.com/drive/folders/1XRmUeIevRfZT982verCI4kq_8CRR4ueq?usp=sharing), the dataset is available.
<div align="center"><img src="images/ex1.jpg", width="500"></div>

Main features of the data contained in the proposed dataset in the table below. 

|       **Image**       | **Number of pixels** | **GSD** |
|:---------------------:|:--------------------:|:-------:|
| Orthophotos from 2010 |        400x400       |  0.50 m |
| Orthophotos from 2017 |        400x400       |  0.50 m |
|     DSMs from 2010    |        200x200       |  1.0 m  |
|     DSMs from 2017    |        200x200       |  1.0 m  |
|       2D CD maps      |        400x400       |  0.50 m |
|       3D CD maps      |        200x200       |  1.0 m  |

To use your custom dataset, please respect this structure (and remember to rename the subfolder "2010" and "2017" in the dataloader):

```bash
Custom dataset
├─train
   ├─t1
   ├─t2
   ├─2dcd
   └─3dcd
├─val
   ├─t1
   ├─t2
   ├─2dcd
   └─3dcd
└─test
   ├─t1
   ├─t2
   ├─2dcd
   └─3dcd
```


## Installation

- Download [Python 3](https://www.python.org/)
- Install the packages:
```bash
pip install -r requirements.txt
```

## Usage 

To train the model, prepare a *.yaml* file and put in the ```config``` directory (where you can find an example) and then run the following command:
```bash
python train.py --config="your_config_file"
```
To test your model, follow the same steps for training and then run the following command:
```bash
python test.py --config="your_config_file"
```

## Results
In this section we briefly show the results obtained. We compared our models with other models available in the literature. 

*WARNING*: if you use this code te reproduce MTBIT results, please consider these metrics w.r.t. the one in the paper, due to un update of the way of computing the cRMSE.

|    Architecture  |   F1 (%)  |   IoU (%) | RMSE (m) | cRMSE (m) |
|:----------------:|:---------:|:---------:|:--------:|:---------:|
|   ChangeFormer   |   42.89   |   27.30   |   1.31   |    6.24   |
|       FC-EF      |   46.32   |   30.14   |   1.41   |    6.74   |
|   FC-Siam-conc   |   38.30   |   23.69   |   1.42   |    6.18   |
|       SUNet      |   59.72   |   42.57   |   1.24   |    5.86   |
|     ResNet18     |    7.87   |    4.82   |   1.56   |    7.26   |
|     IM2HEIGHT    |     -     |     -     |   1.57   |    6.71   |
| **MTBIT (ours)** | **62.15** | **45.09** | **1.20** |  **5.76** |

<div align="center"><img src="images/comp.jpg", width="500"></div>

<div align="center"><img src="images/isto.png", width="500"></div>



## Related resources

In this section, we point out some useful repositories, resources and connected projects. 

- [BIT Github repository](https://github.com/justchenhao/BIT_CD) 
- [Organismo Autonomo Centro Nacional de Informacion Geografica](http://centrodedescargas.cnig.es/CentroDescargas/buscadorCatalogo.do?codFamilia=LIDAR#)

Reach us out if you would like to be inserted in this list.

## Citation
If you found our work useful, consider citing these works:

-[Inferring 3D change detection from bitemporal optical images](https://www.sciencedirect.com/science/article/pii/S0924271622003240) ([arXiv version](https://arxiv.org/abs/2205.15903))
```bash
@article{MARSOCCI2023325,
title = {Inferring 3D change detection from bitemporal optical images},
journal = {ISPRS Journal of Photogrammetry and Remote Sensing},
volume = {196},
pages = {325-339},
year = {2023},
issn = {0924-2716},
doi = {https://doi.org/10.1016/j.isprsjprs.2022.12.009},
url = {https://www.sciencedirect.com/science/article/pii/S0924271622003240},
author = {Valerio Marsocci and Virginia Coletta and Roberta Ravanelli and Simone Scardapane and Mattia Crespi},
keywords = {3D change detection, Remote sensing, Deep learning, Elevation change detection, Dataset},
}
```

-[3DCD: a new dataset for 2D and 3D change detection using deep learning techniques](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLIII-B3-2022/1349/2022/)
```bash
@Article{isprs-archives-XLIII-B3-2022-1349-2022,
AUTHOR = {Coletta, V. and Marsocci, V. and Ravanelli, R.},
TITLE = {3DCD: A NEW DATASET FOR 2D AND 3D CHANGE DETECTION USING DEEP LEARNING TECHNIQUES},
JOURNAL = {The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences},
VOLUME = {XLIII-B3-2022},
YEAR = {2022},
PAGES = {1349--1354},
URL = {https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLIII-B3-2022/1349/2022/},
DOI = {10.5194/isprs-archives-XLIII-B3-2022-1349-2022}
}
```

## License

Code is released for non-commercial and research purposes only. For commercial purposes, please contact the authors.
