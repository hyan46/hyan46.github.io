---
title: "Flow Mismatching: Unsupervised Anomaly Detection via Velocity Discrepancies in Flow Matching Models"
author: ["Hao Yan"]
tags: ["Software", "AnomalyDetection", "FlowMatching", "GenerativeModels", "NeurIPS", "featured"]
draft: false
featured: true
layout: 'project-page'
authors:
- Shengzhe Chen
- Mehrdad Moradi
- Kamran Paynabar
- Hao Yan
publication_types:
- paper-conference
publication: '*Advances in Neural Information Processing Systems (NeurIPS)*'
date: '2026-09-01'
year: '2026'
url: /yan-flow-mismatching-neurips-2026/
url_pdf: 'https://arxiv.org/abs/2605.23070'
url_project: '/yan-flow-mismatching-neurips-2026/'
abstract: 'We propose Flow Mismatching, an unsupervised anomaly detection method that avoids reconstruction. A flow matching model is trained only on normal images; for a test image, its learned velocity field is compared with the direct geometric velocity toward that image along paths from noise. Mismatches between the two highlight anomalies, and aggregating them across time steps and paths yields pixel-wise heatmaps and image-level scores. We also give a theoretical decomposition of the mismatch, and report results on MVTec-AD and VisA that outperform reconstruction-based and other flow matching-based methods.'
summary: 'Unsupervised anomaly detection from the mismatch between a flow matching model''s learned velocity and the direct velocity toward a test image, giving pixel-wise heatmaps and image-level scores.'
---

## Overview {#overview}

**Flow Mismatching** is an **unsupervised anomaly detection** method that does not rely on reconstruction. A **flow matching** model is trained only on normal images. For a test image, we compare the model's learned velocity field with the direct geometric velocity toward that image along paths from noise. Where the two disagree, the image is anomalous; aggregating these **velocity mismatches** across time steps and paths gives pixel-wise anomaly heatmaps and image-level scores.

We also provide a theoretical decomposition of the mismatch, and report results on MVTec-AD and VisA that outperform reconstruction-based and other flow matching-based methods.

Accepted to **NeurIPS 2026**.

---

## Toy-Example Demonstrations {#toy-examples}

A live interactive demo illustrates the velocity-mismatch
mechanism on 2D toy data — a flow-matching model trained only on normal data,
run toward a real data point and an off-manifold point from the same starting
noise draws. Solid arrows show the model's predicted velocity; dashed lines
show the true heading. On the normal target they track each other; on the
off-manifold target they visibly diverge, and that growing disagreement is
the anomaly signal.


**Try it yourself** — drag the time slider (or press play), and switch between a
3-cluster mixture and the paper's actual toy setup (Appendix B.1): an upper
semicircle manifold, scored on the paper's own grid and aggregation rule, with
a genuinely near-manifold anomaly (a harder, more subtle detection case than an
off-manifold gap point):

{{< rawhtml >}}
<div style="max-width:980px;margin:1.25rem auto;border-radius:10px;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,0.12);">
  <iframe
    src="/demo/flow-mismatching/index.html"
    title="Flow Mismatching interactive demo"
    style="width:100%;aspect-ratio:1500/1270;border:none;display:block;"
    loading="lazy">
  </iframe>
</div>
{{< /rawhtml >}}

### Bias-variance trade-off across ODE time {#bias-variance}

Flow Mismatching aggregates the velocity mismatch across many ODE times $t$
rather than reading it off a single $t$, because the mismatch signal itself
trades bias for variance as $t$ varies. The figure below reproduces the
paper's own semicircle toy analysis (Appendix B.1): at small $t$,
interpolated states are dominated by source noise, so the low-mismatch
region is a broad blob covering the manifold's interior — biased and poorly
localized. At large $t$, the low-mismatch region localizes tightly to the
manifold but becomes visibly speckled — high variance, since late-time states
are far more sensitive to the specific noise draw. The paper's
$w(t) = t^2$-weighted combination over time balances the two regimes,
yielding a score map that is both sharp and smooth.

{{< figure src="figures/bias_variance_toy.png" alt="Flow-mismatch anomaly score maps on the semicircle toy at five ODE times t = 0.01, 0.25, 0.5, 0.75, 0.99, plus the time-weighted combination. Small t gives a broad, poorly-localized low-score blob (bias); large t localizes tightly to the manifold but is speckled (variance); the weighted combination is sharp and smooth." caption="**Bias-variance trade-off across ODE time.** Darker = lower normalized flow mismatch. The blue arc is the normal manifold (upper semicircle, center (0,3), radius 5)." width="100%" >}}

---

## Resources {#resources}

- **Paper:** [arXiv:2605.23070](https://arxiv.org/abs/2605.23070)
- **Venue:** NeurIPS 2026

---

## BibTeX {#bibtex}

```bibtex
@inproceedings{chen2026flowmismatching,
  title     = {Flow Mismatching: Unsupervised Anomaly Detection via Velocity Discrepancies in Flow Matching Models},
  author    = {Chen, Shengzhe and Moradi, Mehrdad and Paynabar, Kamran and Yan, Hao},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2026},
  note      = {arXiv:2605.23070}
}
```
