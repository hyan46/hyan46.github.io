---
title: "Multi-Sensor Prognostics Modeling for Applications with Highly Incomplete Signals"
author: ["Hao Yan"]
tags: ["Software", "Matrix-Decomposition", "Prognostics", "Tensor"]
draft: false
authors:
- Xiaolei Fang
- Hao Yan
- Nagi Gebraeel
- Kamran Paynabar
categories: []
date: '2020-07-01'
lastmod: 2021-07-10T09:47:29-07:00

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
publishDate: '2021-07-10T16:47:29.490698Z'
publication_types:
- article-journal
abstract: 'Multi-stream degradation signals have been widely used to predict the residual
  useful lifetime of partially degraded systems. To achieve this goal, most of the
  existing prognostics models assume that degradation signals are complete, i.e.,
  they are observed continuously and frequently at regular time grids. In reality,
  however, degradation signals are often (highly) incomplete, i.e., containing missing
  and corrupt observations. Such signal incompleteness poses a significant challenge
  for the parameter estimation of prognostics models. To address this challenge, this
  article proposes a prognostics methodology that is capable of using highly incomplete
  multi-stream degradation signals to predict the residual useful lifetime of partially
  degraded systems. The method first employs multivariate functional principal components
  analysis to fuse multi-stream signals. Next, the fused features are regressed against
  time-to-failure using (log)-location-scale regression. To estimate the fused features
  using incomplete multi-stream degradation signals, we develop two computationally
  efficient algorithms: subspace detection and signal recovery. The performance of
  the proposed prognostics methodology is evaluated using simulated datasets and a
  degradation dataset of aircraft turbofan engines from the NASA repository.'
publication: '*IISE Transactions*'
doi: 10.1080/24725854.2020.1789779
---
