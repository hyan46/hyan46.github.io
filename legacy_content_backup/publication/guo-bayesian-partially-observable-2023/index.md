---
title: A Bayesian Partially Observable Online Change Detection Approach with Thompson
  Sampling
date: '2023-04-01'
draft: true
publishDate: '2023-06-22T16:41:34.483643Z'
authors:
- Jie Guo
- Hao Yan
- Chen Zhang
publication_types:
- '2'
abstract: This article proposes a Bayesian learning framework for online change detection
  of high-dimensional data streams where only a subset of variables can be observed
  at each time point due to limited sensing capacities. On the one hand, we need to
  build a change detection scheme based on partial observations. On the other, the
  scheme should be able to adaptively and actively select the most critical sensing
  variables to observe to maximize the detection power. To address these two points,
  in this article, first, a novel Bayesian Spike-Slab Composite Decomposition (BSSCD)
  is proposed to decompose the high-dimensional signals onto normal and abnormal bases,
  where the projection coefficients are efficiently estimated via variational Bayesian
  inference. Built upon it, the posterior Bayes factor is constructed as the detection
  statistic. Second, by further formulating the detection statistic as the reward
  function of combinatorial multi-armed bandit (CMAB), a Thompson sampling strategy
  is proposed for selecting the potential changed variables with the balance of exploration
  and exploitation. The efficacy and applicability of our method are demonstrated
  in practice with numerical studies and a real case study.
featured: false
publication: '*Technometrics*'
tags:
- Adaptive sampling
- Combinatorial multi-armed bandit
- Composite decomposition
- Posterior Bayes Factor
- Sparse change detection
- Variational Bayesian inference
doi: 10.1080/00401706.2022.2127914
---

