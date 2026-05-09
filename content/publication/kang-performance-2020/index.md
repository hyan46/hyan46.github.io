---
title: "Performance Evaluation of Production Systems Using Real-Time Machine Degradation Signals"
author: ["Hao Yan"]
tags: ["Software", "Manufacturing", "Control"]
draft: false
authors:
- Yunyi Kang
- Hao Yan
- Feng Ju
categories: []
date: '2020-01-01'
lastmod: 2021-07-09T12:25:37-07:00

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
projects: ["prognostics-control"]
publishDate: '2021-07-10T08:27:04.720572Z'
publication_types:
- article-journal
abstract: A machine's degradation status directly influences the operational performance
  of the production system, such as productivity and product quality. For example,
  machines associated with different health states may have different remaining life
  before failure, thus impacting the system throughput. Therefore, it is critical
  to analyze the coupling between the overall system performance and the machine degradation
  to better production decision-making, such as maintenance and product dispatch decisions.
  In this paper, we propose a novel model to evaluate the production performance of
  a two-machine-and-one-buffer line, given the real-time machine degradation signals.
  Specifically, a phase-type distribution-based continuous-time Markov chain model
  is formulated to estimate the system throughput by utilizing the remaining life
  prediction from the degradation signals. A case study is provided to demonstrate
  the applicability and effectiveness of the proposed method.Note to Practitioners
  - Machine degradation is commonly observed in many industries, such as automotive,
  semiconductor, and food production, which gradually deteriorates the machine conditions
  in different operating processes and affects the production system performance.
  In practice, sensors are largely deployed on the factory floor to monitor the machine's
  operating condition. However, a gap still exists between machine operating conditions
  and system performance. In this paper, we develop an analytical model to predict
  the machine remaining lifetime and estimate the system performance of a small scale
  production system, using the machine degradation signals from sensors. Furthermore,
  a Bayesian updating scheme is provided, which enables online evaluation by utilizing
  the real-time signals. Such a method provides an effective tool for production engineers
  to analyze the real-time system performance, and further conduct system improvements
  and control.
publication: '*IEEE Transactions on Automation Science and Engineering*'
doi: 10.1109/TASE.2019.2920874
---
