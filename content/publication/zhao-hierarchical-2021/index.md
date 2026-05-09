---
title: "Hierarchical Tree-Based Sequential Event Prediction with Application in the Aviation Accident Report"
author: ["Hao Yan"]
tags: ["Software", "Classification", "Deep-Learning", "Text-Mining", "Aviation"]
draft: false
authors:
- Xinyu Zhao
- Hao Yan
- Yongming Liu
categories: []
date: '2021-01-01'
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
projects: ["aviation-text"]
publishDate: '2021-07-10T08:27:09.923628Z'
publication_types:
- paper-conference
abstract: Sequential event prediction is a well-studied area and has been widely used
  in proactive management, recommender systems and healthcare. One major assumption
  of the existing sequential event prediction methods is that similar event sequence
  patterns in the historical record will repeat themselves, enabling us to predict
  future events. However, in reality, the assumption becomes less convincing when
  we are trying to predict rare or unique sequences. Furthermore, the representation
  of the event may be complex with hierarchical structures. In this paper, we aim
  to solve this issue by taking advantage of the multi-level or hierarchical representation
  of these rare events. We proposed to build a sequential Encoder-Decoder framework
  to predict the event sequences. More specifically, in the encoding layer, we built
  a hierarchical embedding representation for the events. In the decoding layer, we
  first predict the high-level events and the low-level events are generated according
  to a hierarchical graphical structure. We propose to link the encoding decoding
  layers with the temporal models for future event prediction. In this article, we
  further discussed applying the proposed model into the failure event prediction
  according to the aviation accident reports and have shown improved accuracy and
  model interpretability.
publication: '*Proceedings 37th IEEE International Conference on Data Engineering*'
doi: 10.1109/ICDE51399.2021.00178
---
