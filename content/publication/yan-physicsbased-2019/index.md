---
title: "Physics-Based Deep Spatio-Temporal Metamodeling for Cardiac Electrical Conduction Simulation"
author: ["Hao Yan"]
tags: ["Software", "Deep-Learning", "Heart", "Cardiac"]
draft: false
subtitle: ''
summary: ''
authors:
- Hao Yan
- Xinyu Zhao
- Zhiyong Hu
- Dongping Du
categories: []
date: '2019-08-01'
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
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2021-07-10T08:27:07.989327Z'
publication_types:
- paper-conference
abstract: Modeling and simulation have been widely used in both cardiac research and
  clinical study to investigate cardiac disease mechanism and develop new treatment
  design. Electrical conduction among cardiac tissue is commonly modeled with a partial
  differential equation, i.e., reaction-diffusion equation, where the reaction term
  describes cellular excitation and diffusion term describes electrical propagation.
  Cellular excitation can be modeled by either detailed human cellular models or simplified
  models such as the FitzHugh-Nagumo model; electrical propagation can be simulated
  using either biodomain or mono-domain tissue model. However, existing cardiac models
  have a great level of complexity, and the simulation is often time-consuming. This
  paper develops a new spatiotemporal model as a surrogate model of the timeconsuming
  cardiac model. Specifically, we propose to investigate the auto-regressive convolutional
  neural network (AR-CNN) and convolutional long short-term memory (Conv-LSTM) to
  model the spatial and temporal structure for the metamodeling. Model predictions
  are compared to the one-dimensional simulation data to validate the prediction accuracy.
  The metamodel can accurately capture the properties of the individual cardiac cell,
  as well as the electrical wave morphology in cardiac fiber at different simulation
  scenarios, which demonstrates its superior performance in modeling and the long-term
  prediction.
publication: '*IEEE International Conference on Automation Science and Engineering*'
doi: 10.1109/COASE.2019.8842902
---
