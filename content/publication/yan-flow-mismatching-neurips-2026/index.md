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
url_code: 'https://github.com/ShengzheC/Flow-Mismatching'
url_project: '/yan-flow-mismatching-neurips-2026/'
abstract: 'We propose Flow Mismatching, an unsupervised anomaly detection method that avoids reconstruction. A flow matching model is trained only on normal images; for a test image, its learned velocity field is compared with the direct geometric velocity toward that image along paths from noise. Mismatches between the two highlight anomalies, and aggregating them across time steps and paths yields pixel-wise heatmaps and image-level scores. We also give a theoretical decomposition of the mismatch, and report results on MVTec-AD and VisA that outperform reconstruction-based and other flow matching-based methods.'
summary: 'Unsupervised anomaly detection from the mismatch between a flow matching model''s learned velocity and the direct velocity toward a test image, giving pixel-wise heatmaps and image-level scores.'
---

Drag the time slider or press play: a flow-matching model trained only on normal data predicts a velocity (solid arrow) toward each target below, against the true heading (dashed). Where they diverge is the anomaly signal Flow Mismatching detects.

{{< rawhtml >}}
<div style="max-width:980px;margin:1.25rem auto;border-radius:10px;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,0.12);">
  <iframe
    id="fm-toy-frame"
    src="/demo/flow-mismatching/index.html"
    title="Flow Mismatching interactive demo"
    style="width:100%;height:900px;border:none;display:block;"
    scrolling="no"
    loading="lazy">
  </iframe>
</div>
{{< /rawhtml >}}

## Overview {#overview}

**Flow Mismatching** is an **unsupervised anomaly detection** method that does not rely on reconstruction. A **flow matching** model is trained only on normal images. For a test image, we compare the model's learned velocity field with the direct geometric velocity toward that image along paths from noise. Where the two disagree, the image is anomalous; aggregating these **velocity mismatches** across time steps and paths gives pixel-wise anomaly heatmaps and image-level scores.

We also provide a theoretical decomposition of the mismatch, and report results on MVTec-AD and VisA that outperform reconstruction-based and other flow matching-based methods.

Accepted to **NeurIPS 2026**.

---

## Methodology {#methodology}

### Problem setup

The model is trained only on **normal** images $p_{\text{data}}$: a conditional flow matching model $v_\theta(x,t)$ learns to transport $\mathcal N(0,I)$ to $p_{\text{data}}$ — the same model as in the demo above. At test time, given image $y$, the goal is a pixel-wise **heatmap** $H$ and a **score** $S$ — no reconstruction, inversion, memory bank, or pretrained features, just forward passes through $v_\theta$.

### Velocity mismatch along a single path

A single pixel's test is simple: does the model's velocity there match the direction a normal image would actually move? Draw $x_0\sim\mathcal N(0,I)$ and form the path toward $y$, with its **geometric velocity**:

$$
x_t = (1-t)\,x_0 + t\,y, \qquad g(x_0, y, t) = y - x_0 = \frac{d}{dt}x_t, \qquad t\in[0,1].
$$

If $y$ is anomalous, $g$ points toward content $v_\theta$ never learned to produce, so the two disagree — exactly the divergence in the demo above, where solid arrows ($v_\theta$) track the dashed true heading ($g$) for normal targets and peel away for anomalous ones. The per-pixel anomaly indicator is

$$
\big\| v_\theta(x_t,t)(i) - g(x_0,y,t)(i) \big\|_2^2,
$$

averaged over RGB channels.

### Two knobs: more seeds, more time points

One path at one $t$ is too noisy to use directly. Flow Mismatching has exactly two knobs for trading compute for reliability, both just repeated forward passes through the same frozen $v_\theta$:

- **$K$ seeds, combined by minimum.** A single seed's $g$ is one arbitrary draw, so an unlucky seed can make a normal pixel look anomalous. Drawing $K$ independent seeds and taking the minimum fixes this: a pixel only scores high if *every* seed agrees. One good seed is enough to clear a normal pixel; no seed clears a genuinely anomalous one.
  $$
  Z_t^{(k)}(i) = \big\|v_\theta(x_t^k,t)(i) - g^k(i)\big\|_2^2, \qquad \delta_t(i) = \min_{k=1,\dots,K} Z_t^{(k)}(i).
  $$
- **$T$ time points, combined by $w(t)=t^2$.** Small $t$ gives a smooth but weak signal; large $t$ a sharp but noisier one. Weighting by $w(t)=t^2$ — derived, not tuned, from inverse-variance weighting of the endpoint error in velocity units (paper, Proposition 3.2) — lets the heatmap draw on both ends of that trade-off at once.
  $$
  H(i) = \frac{1}{|\mathcal T|}\sum_{t\in\mathcal T} w(t)\,\delta_t(i), \qquad S = \max_{i\in\Omega} H(i) \;+\; \frac{1}{|\Omega_{\text{top1}}|}\sum_{i\in\Omega_{\text{top1}}} H(i).
  $$

The demo below shows the $T$ trade-off directly: per-$t$ maps on the left, the running $t^2$-weighted combination on the right. $K$ and $T$ are pure compute knobs — $O(KT)$ forward passes total, no retraining. Low $K,T$ for throughput, higher for accuracy.

### Why it works: a population-level guarantee

Under oracle access to $v_p(t,x):=\mathbb E_p[y-x_0\mid x_t=x]$ — what flow matching converges to with infinite normal data — the paper proves an exact decomposition for any test distribution $q$:

$$
t^2\,\mathbb E_q\!\left[\|v_p(t,X_t)-(Y-X_0)\|_2^2\right] \;=\; \underbrace{\frac{t^2}{(1-t)^2}D_q(t)}_{\text{(I) irreducible noise}} \;+\; \underbrace{(1-t)^2\,J(q_t\Vert p_t)}_{\text{(II) score-field gap, zero iff }q=p}.
$$

(I) is posterior noise present for normal and anomalous inputs alike — it carries no detection power. (II) is strictly positive exactly when $q\ne p$, and *is* the separation signal: it depends only on how different the anomaly's statistics are from normal, not on model error. On normal images ($q=p$) only (I) remains. Early $t$ leans on (II), late $t$ on the bounded (I) — one reason the $t^2$-weighted sum beats reading off a single $t$.

The paper extends this from the oracle $v_p$ to the **learned** $v_\theta$: the identity holds up to an explicit field-approximation-error term, and ranking guarantees survive as long as that error doesn't swamp the (II) signal — verified even far off-manifold (and independently re-checked on this project's own toy and real 5-seed checkpoints during the rebuttal).

---

## More Interactive Demos {#more-demos}

The toy demo above shows the core mismatch mechanism in isolation. The two demos below show it in richer settings: how aggregating across ODE time balances bias against variance, and how the exact same computation looks on a real image.

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

**Drag the slider** to compare, side by side, the per-$t$ landscape (left) against the
running $w(t)=t^2$-weighted combination up to that point (right):

{{< rawhtml >}}
<div style="max-width:900px;margin:1.25rem auto;border-radius:10px;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,0.12);">
  <iframe
    id="fm-bv-frame"
    src="/demo/bias-variance/index.html"
    title="Bias-variance trade-off across ODE time, interactive demo"
    style="width:100%;height:990px;border:none;display:block;"
    scrolling="no"
    loading="lazy">
  </iframe>
</div>
{{< /rawhtml >}}

### Flow mismatching on a real image {#mvtec-example}

The toy examples above use synthetic 2D data so the mechanism is easy to see;
the same method applies directly to real images. Below is the velocity-mismatch
heatmap computed on a real MVTec-AD test image — pick a category with the
selector above the demo (more categories are added as they become available) —
using the trained flow-mismatching model, no synthetic data, same per-$t$
computation and $w(t)=t^2$ time-weighting as the toy demos. The green outline
marks the ground-truth defect region.

{{< rawhtml >}}
<div style="max-width:980px;margin:1.25rem auto;border-radius:10px;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,0.12);">
  <iframe
    id="fm-mvtec-frame"
    src="/demo/mvtec/index.html"
    title="Flow Mismatching on a real MVTec-AD image, interactive demo"
    style="width:100%;height:1500px;border:none;display:block;"
    scrolling="no"
    loading="lazy">
  </iframe>
</div>
{{< /rawhtml >}}

{{< rawhtml >}}
<script>
(function(){
  // the three demo iframes above each postMessage their real content height on load/
  // resize (see each widget's own reportHeight script) -- a fixed CSS aspect-ratio
  // can't track content height here since several layout elements have fixed px
  // height while only some panels scale with width, so required height isn't linear
  // in width. This sets each iframe's height to exactly what its content needs, so
  // there is never an internal scrollbar.
  // debounced: the very first message from a widget can report an inflated
  // transient height (DOM not fully populated by its data-fetch yet) that
  // self-corrects within ~200ms -- waiting for a short quiet period before
  // applying avoids ever visibly flashing that transient size.
  var pending = {};
  window.addEventListener('message', function(ev){
    if (!ev.data || ev.data.type !== 'fm-widget-resize') return;
    var ids = ['fm-toy-frame', 'fm-bv-frame', 'fm-mvtec-frame'];
    for (var i = 0; i < ids.length; i++){
      var id = ids[i];
      var el = document.getElementById(id);
      if (el && el.contentWindow === ev.source){
        var h = Math.ceil(ev.data.height);
        if (pending[id]) clearTimeout(pending[id]);
        pending[id] = setTimeout(function(elRef, hRef){
          return function(){ elRef.style.height = hRef + 'px'; };
        }(el, h), 150);
        break;
      }
    }
  });
})();
</script>
{{< /rawhtml >}}

---

## Resources {#resources}

- **Paper:** [arXiv:2605.23070](https://arxiv.org/abs/2605.23070)
- **Code:** [github.com/ShengzheC/Flow-Mismatching](https://github.com/ShengzheC/Flow-Mismatching)
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
