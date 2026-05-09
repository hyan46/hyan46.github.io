---
title: "Multiple Tensor-on-Tensor Regression: An Approach for Modeling Processes With Heterogeneous Sources of Data"
author: ["Hao Yan"]
tags: ["Software", "High-dimensional", "Tensor", "Manufacturing"]
draft: false
subtitle: ''
summary: ''
authors:
- Mostafa Reisi Gahrooei
- Hao Yan
- Kamran Paynabar
- Jianjun Shi
categories: []
date: '2020-01-01'
lastmod: 2021-07-09T12:25:37-07:00

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
publishDate: '2021-07-10T08:27:04.158456Z'
publication_types:
- article-journal
abstract: In recent years, measurement or collection of heterogeneous sets of data
  such as those containing scalars, waveform signals, images, and even structured
  point clouds, has become more common. Statistical models based on such heterogeneous
  sets of data that represent the behavior of an underlying system can be used in
  the monitoring, control, and optimization of the system. Unfortunately, available
  methods mainly focus on the scalars and profiles and do not provide a general framework
  for integrating different sources of data to construct a model. This article addresses
  the problem of estimating a process output, measured by a scalar, curve, image,
  or structured point cloud by a set of heterogeneous process variables such as scalar
  process setting, profile sensor readings, and images. We introduce a general multiple
  tensor-on-tensor regression approach in which each set of input data (predictor)
  and output measurements are represented by tensors. We formulate a linear regression
  model between the input and output tensors and estimate the parameters by minimizing
  a least square loss function. To avoid overfitting and reduce the number of parameters
  to be estimated, we decompose the model parameters using several basis matrices
  that span the input and output spaces, and provide efficient optimization algorithms
  for learning the basis and coefficients. Through several simulation and case studies,
  we evaluate the performance of the proposed method. The results reveal the advantage
  of the proposed method over some benchmarks in the literature in terms of the mean
  square prediction error. Supplementary materials for this article are available
  online.
publication: '*Technometrics*'
doi: 10.1080/00401706.2019.1708463
---
