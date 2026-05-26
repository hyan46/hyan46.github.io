---
title: "Tensor Completion for Weakly-Dependent Data on Graph for Metro Passenger Flow Prediction"
author: ["Hao Yan"]
tags: ["Software", "Times-Series", "Tensor", "Forecasting", "Traffic"]
draft: false
subtitle: ''
summary: ''
authors:
- Ziyue Li
- Nuretin Dorukhan Sergin
- Hao Yan
- Chen Zhang
- Fugee Tsung
categories: []
date: '2020-12-01'
lastmod: 2021-07-09T12:25:38-07:00

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Different Spatial and Temporal Structures'
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2021-07-10T08:27:05.364372Z'
publication_types:
- paper-conference
abstract: Low-rank tensor decomposition and completion have attracted significant
  interest from academia given the ubiquity of tensor data. However, the low-rank
  structure is a global property, which will not be fulfilled when the data presents
  complex and weak dependencies given specific graph structures. One particular application
  that motivates this study is the spatiotemporal data analysis. As shown in the preliminary
  study, weakly dependencies can worsen the low-rank tensor completion performance.
  In this paper, we propose a novel low-rank CANDECOMP / PARAFAC (CP) tensor decomposition
  and completion framework by introducing the $L_1$-norm penalty and Graph Laplacian
  penalty to model the weakly dependency on graph. We further propose an efficient
  optimization algorithm based on the Block Coordinate Descent for efficient estimation.
  A case study based on the metro passenger flow data in Hong Kong is conducted to
  demonstrate improved performance over the regular tensor completion methods.
publication: '*Thirty-Fourth AAAI Conference on Artificial Intelligence*'
doi: 10.1609/aaai.v34i04.5915
---
