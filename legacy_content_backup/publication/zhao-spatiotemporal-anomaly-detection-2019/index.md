---
title: Spatio-Temporal Anomaly Detection, Diagnostics, and Prediction of the Air-traffic
  Trajectory Deviation Using the Convective Weather
date: '2019-09-01'
draft: true
publishDate: '2023-06-22T16:41:36.765305Z'
authors:
- Xinyu Zhao
- Hao Yan
- Jing Li
- Yutian Pang
- Yongming Liu
publication_types:
- '2'
abstract: With ahead-of-time aircraft management, we are able to re- duce aircraft
  collision and improve air traffic capacity. How- ever, there are various impact
  factors which will cause a large deviation between the actual flight and the original
  flight plan. Such uncertainty will result in an inappropriate decision for flight
  management. In order to solve this problem, most of the existing research attempt
  to build up a stochastic trajec- tory prediction model to capture the influence
  of the weather. However, the complexity of the weather information and vari- ous
  human factors make it hard to build up an accurate trajec- tory prediction framework.
  Our approach considers the prob- lem of trajectory deviation as the ''anomaly''
  and builds up an analytics pipeline for anomaly detection, anomaly diagnos- tics,
  and anomaly prediction. For anomaly detection, we pro- pose to apply the CUSUM chart
  to detect the abnormal tra- jectory point which differs from the flight plan. For
  anomaly diagnostics, we would like to link the entire anomalous trajec- tory sequences
  with the convective weather data and extract important features based on time-series
  feature engineering. Furthermore, XGBoost was applied to detect the anomalous trajectory
  sequences based on the time-series features. For anomaly prediction, we will build
  up a point-wise prediction framework based on the Hidden Markov Model and Convectional
  LSTM to predict the probability that the pilot would deviate from the flight plan.
  Finally, we demonstrate the sig- nificance of the proposed method using real flight
  data from JFK to LAX.
featured: false
publication: '*Annual Conference of the PHM Society*'
tags:
- Anomaly Detection
- Classification
- Traffic
doi: 10.36001/phmconf.2019.v11i1.854
---

