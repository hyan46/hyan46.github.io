---
title: "Artificial Intelligence for the Computer-Aided Detection of Periapical Lesions in Cone-Beam Computed Tomographic Images"
author: ["Hao Yan"]
tags: ["Software", "Health", "Image", "Segmentation", "Deep-Learning"]
draft: false
authors:
- Frank C. Setzer
- Katherine J. Shi
- Zhiyang Zhang
- Hao Yan
- Hyunsoo Yoon
- Mel Mupparapu
- Jing Li

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2021-10-12T05:30:10.520218Z'
publication_types:
- article-journal
abstract: "Introduction The aim of this study was to use a Deep Learning (DL) algorithm
   for the automated segmentation of cone-beam computed tomographic (CBCT) images
   and the detection of periapical lesions. Methods Limited field of view CBCT volumes
   (n = 20) containing 61 roots with and without lesions were segmented clinician
   dependent versus using the DL approach based on a U-Net architecture. Segmentation
   labeled each voxel as 1 of 5 categories: ``lesion'' (periapical lesion), ``tooth
   structure,'' ``bone,'' ``restorative materials,'' and ``background.'' Repeated
   splits of all images into a training set and a validation set based on 5-fold
   cross validation were performed using Deep Learning segmentation (DLS), and te
   results were averaged. DLS versus clinical-dependent segmentation was assessed
   by dichotomized lesion detection accuracy evaluating sensitivity, specificity,
   positive predictive value, negative predictive value, and voxel-matching accuracy
   using the DICE index for each of the 5 labels. Results DLS lesion detection accuracy
   was 0.93 with specificity of 0.88, positive predictive value of 0.87, and negative
   predictive value of 0.93. The overall cumulative DICE indexes for the individual
   labels were lesion = 0.52, tooth structure = 0.74, bone = 0.78, restorative materias
   = 0.58, and background = 0.95. The cumulative DICE index for all actual true lesions
   was 0.67. Conclusions This DL algorithm trained in a limited CBCT environment
   showed excellent results in lesion detection accuracy. Overall voxel-matching
   accuracy may be benefited by enhanced versions of artificial intelligence."
publication: '*Journal of Endodontics*'
doi: 10.1016/j.joen.2020.03.025
---
