---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Image Decomposition-Based Sparse Extreme Pixel-Level Feature Detection Model
  with Application to Medical Images
subtitle: ''
summary: ''
authors:
- Geet Lahoti
- Jialei Chen
- Xiaowei Yue
- Hao Yan
- Chitta Ranjan
- Zhen Qian
- Chuck Zhang
- Ben Wang
tags:
- '"Health"'
- '"High-dimensional"'
- '"Segmentation"'
categories: []
date: '2021-04-01'
lastmod: 2021-07-09T12:25:38-07:00
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
publishDate: '2021-07-10T08:27:05.210126Z'
publication_types:
- article-journal
abstract: Pixel-level feature detection from images is an essential but challenging
  task encountered in domains such as detecting defects in manufacturing systems and
  detecting tumors in medical imaging. Often, the real image contains multiple feature
  types. The types with higher pixel intensities are termed as positive (extreme)
  features and the ones with lower pixel intensities as negative (extreme) features.
  For example, when planning a medical treatment, it is important to identify, (a)
  calcification (a pathological feature which can result in a post-surgical complications)
  as positive features, and (b) soft tissues (organ morphology, knowledge of which
  can support pre-surgical planning) as negative features, from a preoperative computed
  tomography image of the human heart. However, this is not an easy task because (a)
  conventional segmentation techniques require manual intervention and post-processing,
  and (b) existing automatic approaches do not distinguish positive features from
  negative. In this work, we propose a novel, automatic image decomposition-based
  sparse extreme pixel-level feature detection model to decompose an image into mean
  and extreme features. To estimate model parameters, a high-dimensional least squares
  regression with regularization and constraints is utilized. An efficient algorithm
  based on the alternating direction method of multipliers and the proximal gradient
  method is developed to solve the large-scale optimization problem. The effectiveness
  of the proposed model is demonstrated using synthetic tests and a real-world case
  study, where the model exhibits superior performance over existing methods.
publication: '*IISE Transactions on Healthcare Systems Engineering*'
doi: 10.1080/24725579.2021.1910599
---
