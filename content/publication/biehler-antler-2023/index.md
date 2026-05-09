---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'ANTLER: Bayesian Nonlinear Tensor Learning and Modeler for Unstructured, Varying-Size
  Point Cloud Data'
subtitle: ''
summary: ''
authors:
- Michael Biehler
- Hao Yan
- Jianjun Shi
tags:
- Data models
- Feature extraction
- Gears
- high-dimensional modeling
- nonlinear point cloud regression
- nonlinear tensor decomposition
- Point cloud compression
- Shape
- Tensors
- Three-dimensional displays
- Unstructured point cloud data
categories: []
date: '2023-01-01'
lastmod: 2023-06-22T10:03:37-07:00
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
publishDate: '2023-06-22T17:03:37.365428Z'
publication_types:
- article-journal
abstract: Unstructured point clouds of varying sizes are increasingly acquired in
  a variety of environments through laser triangulation or Light Detection and Ranging
  (LiDAR). Predicting a vector response based on unstructured point clouds is a common
  problem that arises in a wide variety of applications. The current literature relies
  on several pre-processing steps such as structured subsampling and feature extraction
  to analyze the point cloud data. Those techniques lead to quantization artifacts
  and do not consider the relationship between the regression response and the point
  cloud during pre-processing. Therefore, we propose a general and holistic ``Bayesian
  Nonlinear Tensor Learning and Modeler'' (ANTLER) to model the relationship of unstructured,
  varying-size point cloud data with a vector response. The proposed ANTLER simultaneously
  optimizes a nonlinear tensor dimensionality reduction and a nonlinear regression
  model with a 3D point cloud input and a regression response. ANTLER can consider
  the complex data representation, high-dimensionality, and inconsistent size of the
  3D point cloud data. Note to Practitioners— This paper is motivated by a real-world
  case study concerning the prediction of the transmission error and eccentricity
  based on unstructured point clouds of varying sizes in gear manufacturing. In the
  current state-of-the-art method, those characteristics can only be obtained via
  expensive and time-consuming Finite Element Analysis (FEA) or test benches. The
  proposed ANTLER framework can directly link the measurement point clouds with a
  vector response and serves as a guiding example for the immense potential of the
  ANTLER.
publication: '*IEEE Transactions on Automation Science and Engineering*'
doi: 10.1109/TASE.2022.3230563
---
