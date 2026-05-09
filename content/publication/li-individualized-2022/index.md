---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Individualized Passenger Travel Pattern Multi-Clustering Based on Graph Regularized
  Tensor Latent Dirichlet Allocation
subtitle: ''
summary: ''
authors:
- Ziyue Li
- Hao Yan
- Chen Zhang
- Fugee Tsung
tags:
- Graph structure
- Individualized analysis
- Online algorithm
- Spatiotemporal data
- Tensor
- Topic model
categories: []
date: '2022-07-01'
lastmod: 2023-06-22T10:03:38-07:00
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
publishDate: '2023-06-22T17:03:38.767640Z'
publication_types:
- article-journal
abstract: "Individual passenger travel patterns have significant value in understanding\
  \ passenger's behavior, such as learning the hidden clusters of locations, time,\
  \ and passengers. The learned clusters further enable commercially beneficial actions\
  \ such as customized services, promotions, data-driven urban-use planning, peak\
  \ hour discovery, and so on. However, the individualized passenger modeling is very\
  \ challenging for the following reasons: 1) The individual passenger travel data\
  \ are multi-dimensional spatiotemporal big data, including at least the origin,\
  \ destination, and time dimensions; 2) Moreover, individualized passenger travel\
  \ patterns usually depend on the external environment, such as the distances and\
  \ functions of locations, which are ignored in most current works. This work proposes\
  \ a multi-clustering model to learn the latent clusters along the multiple dimensions\
  \ of Origin, Destination, Time, and eventually, Passenger (ODT-P). We develop a\
  \ graph-regularized tensor Latent Dirichlet Allocation (LDA) model by first extending\
  \ the traditional LDA model into a tensor version and then applies to individual\
  \ travel data. Then, the external information of stations is formulated as semantic\
  \ graphs and incorporated as the Laplacian regularizations; Furthermore, to improve\
  \ the model scalability when dealing with massive data, an online stochastic learning\
  \ method based on tensorized variational Expectation-Maximization algorithm is developed.\
  \ Finally, a case study based on passengers in the Hong Kong metro system is conducted\
  \ and demonstrates that a better clustering performance is achieved compared to\
  \ state-of-the-arts with the improvement in point-wise mutual information index\
  \ and algorithm convergence speed by a factor of two."
publication: '*Data Mining and Knowledge Discovery*'
doi: 10.1007/s10618-022-00842-3
---
