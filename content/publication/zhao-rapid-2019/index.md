---
title: "Rapid Detection of Hot-Spot by Tensor Decomposition with Application to Weekly Gonorrhea Data"
author: ["Hao Yan"]
tags: ["Software", "Health", "Anomaly-Detection", "Tensor"]
draft: false
subtitle: ''
summary: ''
authors:
- Yujie Zhao
- Hao Yan
- Sarah E. Holte
- Roxanne P. Kerani
- Yajun Mei
categories: []
date: '2019-01-01'
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
projects: [hotspot-detection]
publishDate: '2021-07-10T08:27:10.174891Z'
publication_types:
- paper-conference
abstract: 'In many bio-surveillance and healthcare applications, data sources are
  measured from many spatial locations repeatedly over time, say, daily/weekly/monthly.
  In these applications, we are typically interested in detecting hot-spots, which
  are defined as some structured outliers that are sparse over the spatial domain
  but persistent over time. In this paper, we propose a tensor decomposition method
  to detect when and where the hot-spots occur. Our proposed methods represent the
  observed raw data as a three-dimensional tensor including a circular time dimension
  for daily/weekly/monthly patterns, and then decompose the tensor into three components:
  smooth global trend, local hot-spots, and residuals. A combination of LASSO and
  fused LASSO is used to estimate the model parameters, and a CUSUM procedure is applied
  to detect when and where the hot-spots might occur. The usefulness of our proposed
  methodology is validated through numerical simulation and a real-world dataset in
  the weekly number of gonorrhea cases from $2006$ to $2018$ for $50$ states in the
  United States.'
publication: '*The XIIIth International Workshop on Intelligent Statistical Quality
  Control,*'
doi: 10.1080/00224065.2021.1903822
---
