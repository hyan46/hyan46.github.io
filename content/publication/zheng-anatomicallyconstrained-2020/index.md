---
title: "Anatomically-Constrained Deep Learning for Automating Dental CBCT Segmentation and Lesion Detection"
author: ["Hao Yan"]
tags: ["Software", "Segmentation", "Deep-Learning", "Health", "Dental"]
draft: false
# Documentation: https://sourcethemes.com/academic/docs/managing-content/
subtitle: ''
summary: ''
authors:
- Zhiyang Zheng
- Hao Yan
- Frank Setzer
- Katherine Shi
- Mel Mupparapu
- Jing Li
categories: []
date: '2020-01-01'
lastmod: 2021-07-09T12:25:41-07:00

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
publishDate: '2021-07-10T08:27:11.163712Z'
publication_types:
- article-journal
abstract: Compared with the rapidly growing artificial intelligence (AI) research
  in other branches of healthcare, the pace of developing AI capacities in dental
  care is relatively slow. Dental care automation, especially the automated capability
  for dental cone beam computed tomography (CBCT) segmentation and lesion detection,
  is highly needed. CBCT is an important imaging modality that is experiencing ever-growing
  utilization in various dental specialties. However, little research has been done
  for segmenting different structures, restorative materials, and lesions using deep
  learning. This is due to multifold challenges such as content-rich oral cavity and
  significant within-label variation on each CBCT image as well as the inherent difficulty
  of obtaining many high-quality labeled images for training. On the other hand, oral-anatomical
  knowledge exists in dentistry, which shall be leveraged and integrated into the
  deep learning design. In this article, we propose a novel anatomically constrained
  Dense U-Net for integrating oral-anatomical knowledge with data-driven Dense U-Net.
  The proposed algorithm is formulated as a regularized or constrained optimization
  and solved using mean-field variational approximation to achieve computational efficiency.
  Mathematical encoding for transforming descriptive knowledge into a quantitative
  form is also proposed. Our experiment demonstrates that the proposed algorithm outperforms
  the standard Dense U-Net in both lesion detection accuracy and dice coefficient
  (DICE) indices in multilabel segmentation. Benefited from the integration with anatomical
  domain knowledge, our algorithm performs well with data from a small number of patients
  included in the training. Note to Practitioners — This article proposes a novel
  deep learning algorithm to enable the automated capability for cone beam computed
  tomography (CBCT) segmentation and lesion detection. Despite the growing adoption
  of CBCT in various dental specialties, such capability is curren...
publication: '*IEEE Transactions on Automation Science and Engineering*'
doi: 10.1109/TASE.2020.3025871
---
