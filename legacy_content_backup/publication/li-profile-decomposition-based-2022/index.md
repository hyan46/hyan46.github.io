---
title: Profile Decomposition Based Hybrid Transfer Learning for Cold-Start Data Anomaly
  Detection
date: '2022-07-01'
draft: true
publishDate: '2023-06-22T16:41:35.049422Z'
authors:
- Ziyue Li
- Hao Yan
- Fugee Tsung
- Ke Zhang
publication_types:
- '2'
abstract: "Anomaly detection is an essential task for quality management in smart\
  \ manufacturing. An accurate data-driven detection method usually needs enough data\
  \ and labels. However, in practice, there commonly exist newly set-up processes\
  \ in manufacturing, and they only have quite limited data available for analysis.\
  \ Borrowing the name from the recommender system, we call this process a cold-start\
  \ process. The sparsity of anomaly, the deviation of the profile, and noise aggravate\
  \ the detection difficulty. Transfer learning could help to detect anomalies for\
  \ cold-start processes by transferring the knowledge from more experienced processes\
  \ to the new processes. However, the existing transfer learning and multi-task learning\
  \ frameworks are established on task- or domain-level relatedness. We observe instead,\
  \ within a domain, some components (background and anomaly) share more commonality,\
  \ others (profile deviation and noise) not. To this end, we propose a more delicate\
  \ component-level transfer learning scheme, i.e., decomposition-based hybrid transfer\
  \ learning (DHTL): It first decomposes a domain (e.g., a data source containing\
  \ profiles) into different components (smooth background, profile deviation, anomaly,\
  \ and noise); then, each component's transferability is analyzed by expert knowledge;\
  \ Lastly, different transfer learning techniques could be tailored accordingly.\
  \ We adopted the Bayesian probabilistic hierarchical model to formulate parameter\
  \ transfer for the background, and ``L2,1+L1''-norm to formulate low dimension feature-representation\
  \ transfer for the anomaly. An efficient algorithm based on Block Coordinate Descend\
  \ is proposed to learn the parameters. A case study based on glass coating pressure\
  \ profiles demonstrates the improved accuracy and completeness of detected anomaly,\
  \ and a simulation demonstrates the fidelity of the decomposition results."
featured: false
publication: '*ACM Transactions on Knowledge Discovery from Data*'
tags:
- Bayesian probabilistic model and regularization
- Cold-start anomaly detection
- Hybrid Transfer learning
- Profile decomposition
doi: 10.1145/3530990
---

