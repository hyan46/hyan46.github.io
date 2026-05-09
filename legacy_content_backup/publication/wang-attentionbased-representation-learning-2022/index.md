---
title: Attention-Based Representation Learning for Time Series with Principal and
  Residual Space Monitoring
date: '2022-08-01'
draft: true
publishDate: '2023-06-22T16:41:35.463771Z'
authors:
- Botao Wang
- Fugee Tsung
- Hao Yan
publication_types:
- '1'
abstract: The encoder-decoder network is one of the most common deep learning models
  for time series representation learning and anomaly detection. However, it is hard
  to reconstruct time series, which is complex, correlated, and lacking in common
  patterns. In this paper, we apply the attention mechanism to rescale convolution
  layers and learn representation in the principal and the residual space. To avoid
  the reconstruction process, we define the residual space by the omitted segments
  according to the attention score in the encoder. We introduce the temporal information
  inside the token level and use sparse penalty to improve representation learning.
  We apply the proposed model to anomaly classification and fault detection experiments
  on two datasets, i.e. multivariate bearing fault dataset and UCRArchive profile
  dataset. The result shows that the representation learned by the proposed model
  is more likely to cluster by category, especially in the residual space. Compared
  to the baselines and state-of-the-art models, the proposed model has higher accuracy
  and recall in the limited-labeled situation, which illustrates the stability of
  the learned representation and its superiority in the downstream tasks.
featured: false
publication: '*2022 IEEE 18th International Conference on Automation Science and Engineering
  (CASE)*'
tags:
- Anomaly detection
- attention mechanism
- Convolution
- Deep learning
- Fault detection
- representation learning
- Representation learning
- residual space
- Stability analysis
- Task analysis
- time series
- Time series analysis
doi: 10.1109/CASE49997.2022.9926721
---

