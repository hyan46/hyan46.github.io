---
title: "NIH STTR Phase I, AIDen: An AI-empowered detection and diagnosis system for jaw lesions using CBCT"
author: ["Hao Yan"]
date: 2022-09-01
tags: ["Software", "Funded", "NIH"]
draft: false
summary: "AIDen"
# Optional external URL for project (replaces project detail page).
external_link: "https://www.sbir.gov/sbirsearch/detail/2299159"
image:
  caption: AIDen
  focal_point: Smart

links:
- url: ""
  name: "link"

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
---

## Overall Information {#overall-information}

Dental CBCT is a 3D imaging modality widely adopted to help dentists detect and diagnose jaw lesions. Due to
minimum information loss (compared to conventional 2D radiography) and low radiation exposure (compared to
conventional CT), it has become the “go-to” radiographic technique in various dental fields. Gaps: Accompanying
the clear benefits of dental CBCT is an overwhelming amount of 3D data presented to clinicians. Clinician-based
CBCT interpretation suffers from low inter-/intra-observer agreement and low accuracy. AI/Deep Learning (DL)
holds great promise to automate CBCT image analysis and provide objective, accurate detection and diagnosis
capabilities to support clinical decision. However, limited research has been done due to unique and significant
challenges: (1) Dental CBCT provides 3D images composed of a complicated mix of different oral
structures/contents, preventing the direct use of existing general-purse DL algorithms for image segmentation
and calling for new DL designs. (2) AI/DL is known to be data-hungry. It is very difficult to obtain a large number
of accurately-annotated CBCT images to train DL due to complex oral anatomy and inevitable human errors,
which calls for efficient strategies to reduce annotation effort for DL training. (3) Due to these challenges, the
current software systems used to assist clinicians in dental CBCT interpretation do not provide advanced AI-
based lesion detection and diagnosis capabilities, which makes this STTR project timely and important. We
recently developed a DL algorithm that integrates unique oral anatomy into the DL design, namely
“Anatomically-Constrained dense UNet (AC-UNet)”. In addition to improving accuracy, AC-UNet is also
annotation-efficient as it is not only trained using CBCT images but also constrained by anatomical domain
knowledge through novel mathematical encoding and posterior regularization-based optimization. Applied to a
preliminary dataset of CBCTs with periapical lesions indicative of Apical Periodontitis (AP), AC-UNet achieved
high accuracy in segmentation and lesion detection on CBCT images and outperformed state-of-the-art DL
algorithms. Our long-term goal is to develop the first-ever AI-based software system called “AIDen” to perform
automatic segmentation, lesion detection, and differential diagnosis based on dental CBCT for a variety of jaw
lesions/diseases with high accuracy, reliability, and reproducibility. AIDen will assist clinicians in providing
optimal treatment decision for each patient. Our Phase-I goal is to develop and test the feasibility of AIDen for
lesion detection and differential diagnosis focusing on AP, a highly-prevalent jaw lesion/disease. Three aims
are: (1) Optimize design: to develop an extension of AC-UNet to integrate a broader range of different types of
oral-anatomical knowledge into the DL design; (2) Optimize training: to develop an Active Learning strategy to
further improve annotation efficiency of AC-UNet training; (3) Clinical validation and preliminary assessment of
diagnosis capability for clinical decision support. All aims will lay groundwork for Phase-II when an end-to-end
AIDen system will be built and validated using multi-site datasets and address a variety of jaw lesions/diseases.The public health relevance of this project is to provide an Artificial Intelligence (AI)-based clinical decision
support system, AIDen, to facilitate dental CBCT-based automatic segmentation, lesion detection, and
differential diagnosis for a variety of jaw lesions/diseases with high accuracy, reliability, and reproducibility.
AIDen will assist clinicians to provide optimal treatment decision for each individual patient. Our technology can
be used by clinicians from a variety of dental fields such as endodontics, oral surgery, and oral medicine, and in
a variety of settings including private practices, hospitals/clinics, medical/dental schools, and research institutes.
