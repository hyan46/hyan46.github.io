---
title: "Real-Time Detection of Clustered Events in Video-Imaging Data with Applications to Additive Manufacturing"
author: ["Hao Yan"]
tags: ["Software", "Anomaly-Detection", "High-dimensional", "Additive-Manufacturing", "Image", "Sparse-Learning"]
draft: false
subtitle: ''
summary: ''
authors:
- Hao Yan
- Marco Grasso
- Kamran Paynabar
- Bianca Maria Colosimo
categories: []
date: '2021-01-01'
lastmod: 2021-07-09T12:25:39-07:00

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
#   E.g. `projects = ["internal-project","prognostics-control"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["hotspot-detection"]
publishDate: '2021-07-10T08:27:08.365713Z'
publication_types:
- article-journal
abstract: The use of video-imaging data for in-line process monitoring applications
  has become more and more popular in the industry. In this framework, spatio-temporal
  statistical process monitoring methods are needed to capture the relevant information
  content and signal possible out-of-control states. Video-imaging data are characterized
  by a spatio-temporal variability structure that depends on the underlying phenomenon,
  and typical out-of-control patterns are related to the events that are localized
  both in time and space. In this paper, we propose an integrated spatio-temporal
  decomposition and regression approach for anomaly detection in video-imaging data.
  Out-of-control events are typically sparse spatially clustered and temporally consistent.
  Therefore, the goal is to not only detect the anomaly as quickly as possible ("when")
  but also locate it ("where"). The proposed approach works by decomposing the original
  spatio-temporal data into random natural events, sparse spatially clustered and
  temporally consistent anomalous events, and random noise. Recursive estimation procedures
  for spatio-temporal regression are presented to enable the real-time implementation
  of the proposed methodology. Finally, a likelihood ratio test procedure is proposed
  to detect when and where the hotspot happens. The proposed approach was applied
  to the analysis of video-imaging data to detect and locate local over-heating phenomena
  ("hotspots") during the layer-wise process in a metal additive manufacturing process.
publication: '*IISE Transactions*'
doi: 10.1080/24725854.2021.1882013
---
