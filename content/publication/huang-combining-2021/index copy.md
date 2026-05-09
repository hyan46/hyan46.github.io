---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Combining Anatomical Constraints and Deep Learning for 3-D CBCT Dental Image
  Multi-Label Segmentation
subtitle: ''
summary: ''
authors:
- Jiayu Huang
- Hao Yan
- Jing Li
- H. Milton Stewart
- Frank Setzer
tags:
- '"Health"'
- '"Physics Constrain"'
- '"Segmentation"'
categories: []
date: '2021-04-01'
lastmod: 2021-07-10T15:12:57-07:00
featured: false
draft: false

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
publishDate: '2021-07-10T22:12:57.262562Z'
publication_types:
- paper-conference
abstract: 'Machine learning research on medical images is becoming popular as advanced
  imaging technologies and equipment in medicine become more and more available. Dental
  Cone-beam Computed Tomography (Dental CBCT), a frequently-used visualization tool
  for oral diagnosis, provides valuable three-dimensional information, whose development
  for automation of Dental CBCT analysis, on the other hand, is relatively preliminary.
  Generally, there are three important characteristics for analyzing Dental CBCT with
  noisy labels and limited labeled sample size, and availability of oral medicine
  knowledge. Based on those characteristics, we develop an image segmentation method
  for Dental CBCT by integrating domain knowledge into deep U-Net for the 3D segmentation.
  Finally, depending on whether the knowledge can be decomposed into each pixel, the
  knowledge constraints are classified into two types: separable and non-separable
  constraints. All knowledge constraints can be represented as a posterior regularization
  term and solved in different ways in accordance with related types. For separable
  constraints, the mean-field theory is employed to solve an optimization problem
  with the independence assumption about the distributions of output variables on
  each pixel. For non-separable constraints, we propose to combine the importance
  sampling based approach and the stochastic optimization algorithm. Finally, we propose
  to formulate the domain knowledge to the learning stage to improve the accuracy
  and efficiency of automation of Dental CBCT segmentation. Finally, we will apply
  the proposed methods into the real datasets collected and manually labeled by the
  doctors at the University of Pennsylvania'
publication: '*2021 IEEE 37th International Conference on Data Engineering (ICDE)*'
doi: 10.1109/ICDE51399.2021.00319
---
