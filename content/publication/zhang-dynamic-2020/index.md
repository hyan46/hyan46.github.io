---
title: "Dynamic Multivariate Functional Data Modeling via Sparse Subspace Learning"
author: ["Hao Yan"]
tags: ["Software", "Sparse-Learning", "Functional"]
draft: false
# Documentation: https://sourcethemes.com/academic/docs/managing-content/
subtitle: ''
summary: ''
authors:
- Chen Zhang
- Hao Yan
- Seungho Lee
- Jianjun Shi
categories: []
date: '2020-01-01'
lastmod: 2021-07-09T12:25:40-07:00

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
publishDate: '2021-07-10T08:27:09.269423Z'
publication_types:
- article-journal
abstract: Multivariate functional data from a complex system are naturally high-dimensional
  and have complex cross-correlation structure. The complexity of data structure can
  be observed as that (1) some functions are strongly correlated with similar features,
  while some others may have almost no cross-correlations with quite diverse features;
  and (2) the cross-correlation structure may also change over time due to the system
  evolution. With this regard, this paper presents a dynamic subspace learning method
  for multivariate functional data modeling. In particular, we consider different
  functions come from different subspaces, and only functions of the same subspace
  have cross-correlations with each other. The subspaces can be automatically formulated
  and learned by reformatting the problem as a sparse regression. By allowing but
  regularizing the regression change over time, we can describe the cross-correlation
  dynamics. The model can be efficiently estimated by the fast iterative shrinkage-thresholding
  algorithm (FISTA), and the features of every subspace can be extracted using the
  smooth multi-channel functional PCA. Numerical studies together with case studies
  demonstrate the efficiency and applicability of the proposed methodology.
publication: '*Technometrics*'
doi: 10.1080/00401706.2020.1800516
---
