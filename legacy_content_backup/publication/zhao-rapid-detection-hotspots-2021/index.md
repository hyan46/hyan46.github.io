---
title: Rapid Detection of Hot-spots via Tensor Decomposition with Applications to
  Crime Rate Data
date: '2021-01-01'
draft: true
publishDate: '2023-06-22T16:41:36.676864Z'
authors:
- Yujie Zhao
- Hao Yan
- Sarah Holte
- Yajun Mei
publication_types:
- '2'
abstract: 'We propose an efficient statistical method (denoted as SSR-Tensor) to robustly
  and quickly detect hot-spots that are sparse and temporal-consistent in a spatial-temporal
  dataset through the tensor decomposition. Our main idea is to first build an SSR
  model to decompose the tensor data into a Smooth global trend mean, Sparse local
  hot-spots and Residuals. Next, tensor decomposition is utilized as follows: basis
  are introduced to describe within-dimension correlation and tensor products are
  used for between-dimension interaction. Then, a combination of LASSO and fused LASSO
  is used to estimate the model parameters, where an efficient recursive estimation
  procedure is developed based on the large-scale convex optimization, where we first
  transform the general LASSO optimization into regular LASSO optimization and apply
  FISTA to solve it with the fastest convergence rate. Finally, a CUSUM procedure
  is applied to detect when and where the hot-spot event occurs. We compare the performance
  of the proposed method in a numerical simulation and a real-world dataset, which
  is a collection of three types of crime rates for U.S. mainland states during the
  year 1965-2014. In both cases, the proposed SSR-Tensor is able to achieve the fast
  detection and accurate localization of the hot-spots.'
featured: false
publication: '*Journal of Applied Statistics*'
tags:
- Anomaly Detection
- Social
- Sparse Learning
- Tensor
- Video
doi: 10.1080/02664763.2021.1874892
---

