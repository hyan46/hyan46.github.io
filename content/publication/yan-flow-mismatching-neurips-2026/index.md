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

{{< figure src="figures/teaser.png" alt="Velocity mismatch in the (x,t) plane: affine paths toward a normal target stay aligned with the learned flow, while paths toward an anomalous target visibly diverge from it." caption="<span class=\"figure-number\">Figure 1: </span>**Velocity mismatch in the $(x,t)$ plane.** Light arrows show the learned flow $v_θ(x,t)$ from noise to normal data. Affine paths from the same starting noise $x_0$ target either a normal sample (green) or an anomalous sample (red). At selected times, the predicted velocity (blue) aligns with the geometric velocity toward normal targets but disagrees for anomalous targets — that disagreement is the anomaly signal Flow Mismatching detects." width="90%" >}}

## Overview {#overview}

**Flow Mismatching** is an **unsupervised anomaly detection** method that does not rely on reconstruction. A **flow matching** model is trained only on normal images. For a test image, we compare the model's learned velocity field with the direct geometric velocity toward that image along paths from noise. Where the two disagree, the image is anomalous; aggregating these **velocity mismatches** across time steps and paths gives pixel-wise anomaly heatmaps and image-level scores.

We also provide a theoretical decomposition of the mismatch, and report results on MVTec-AD and VisA that outperform reconstruction-based and other flow matching-based methods.

Accepted to **NeurIPS 2026**.

---

## Methodology {#methodology}

### Problem setup

We assume access only to a training set of **normal** (anomaly-free) images, drawn from a distribution $p_{\text{data}}$. A conditional flow matching model $v_\theta(x,t)$ is trained on this normal data alone, learning a velocity field that transports a standard Gaussian prior $\mathcal N(0,I)$ to $p_{\text{data}}$ — exactly the model used in the toy demo above. At test time, given a possibly anomalous image $y$, the goal is a pixel-wise anomaly **heatmap** $H$ and an image-level anomaly **score** $S$. No reconstruction, no inversion, no auxiliary memory bank or pretrained feature extractor is involved anywhere in this pipeline — every quantity below is a forward pass through $v_\theta$.

### Velocity mismatch along a single path

Draw one noise seed $x_0 \sim \mathcal N(0,I)$ and form the deterministic affine path toward the test image, together with the **geometric velocity** that path implies:

$$
x_t = (1-t)\,x_0 + t\,y, \qquad g(x_0, y, t) = y - x_0 = \frac{d}{dt}x_t, \qquad t\in[0,1].
$$

If $y$ is anomalous, $g$ is trying to reproduce content the model never saw during training, while $v_\theta$ — having only ever learned to transport toward normal images — keeps pulling toward normal-looking features. The two velocities disagree. If $y$ is normal, both velocities point the same way and agree closely. This is exactly the divergence you can see live in the first interactive demo below: solid arrows ($v_\theta$) track the dashed true heading ($g$) for the normal target, and visibly peel away from it for the off-manifold target.

Concretely, the anomaly indicator at pixel $i$ is the **per-pixel squared discrepancy**

$$
\big\| v_\theta(x_t,t)(i) - g(x_0,y,t)(i) \big\|_2^2,
$$

averaged over the RGB channels at that pixel.

### Aggregating across paths: why minimum voting

A single noise draw $x_0$ is noisy — one unlucky seed can make even a normal image look locally mismatched, or an anomalous one look locally clean. Flow Mismatching draws $K$ **independent** seeds $x_0^1,\dots,x_0^K\sim\mathcal N(0,I)$, forms $K$ independent paths, and combines the $K$ per-pixel discrepancies $Z_t^{(k)}(i)$ with a **path aggregator** $\mathcal A$:

$$
Z_t^{(k)}(i) = \big\|v_\theta(x_t^k,t)(i) - g^k(i)\big\|_2^2, \qquad \delta_t(i) = \mathcal A\big(\{Z_t^{(k)}(i)\}_{k=1}^{K}\big).
$$

Three natural choices for $\mathcal A$: the **average** (unbiased for the population mismatch), an **$\alpha$-percentile**, or the **minimum**, $\delta_t^{\min}(i)=\min_k Z_t^{(k)}(i)$. Flow Mismatching uses **minimum** by default, and deliberately so — it is a conservative consensus vote: a pixel only keeps a high score if it looks anomalous across *every* sampled noise draw, not just one. For a normal pixel, it only takes one of the $K$ seeds to land near a good explanation to drive the score down; for a genuinely anomalous pixel, *no* seed can explain it well, so the minimum stays high. (This is also why the detector's robustness depends on those seeds being **random and uninformed**, not chosen — see "Why random seeds, not a search" below.)

### Aggregating across time: the heatmap and the anomaly score

Different $t$ query the model at different noise levels, with different amounts of signal and different estimator stability (small $t$: path state is dominated by source noise — smooth but weak signal; large $t$: path state sits near the data manifold — sharp but higher-variance). Rather than pick one $t$, Flow Mismatching discretizes $T$ interior time points and combines them with a weight $w(t)$:

$$
H(i) = \frac{1}{|\mathcal T|}\sum_{t\in\mathcal T} w(t)\,\delta_t(i), \qquad S = \max_{i\in\Omega} H(i) \;+\; \frac{1}{|\Omega_{\text{top1}}|}\sum_{i\in\Omega_{\text{top1}}} H(i),
$$

where $\Omega$ is the pixel domain and $\Omega_{\text{top1}}$ the top 1% of heatmap values (a robust stand-in for "max", since any single pixel can be noisy). The weight is $w(t) = t^2$ — not a tuned hyperparameter, but the specific curve that falls out of **inverse-variance weighting** of the endpoint-estimation error in $y$-space once that error is converted to velocity units (the conversion introduces a $(1-t)^2$ scaling, which combined with inverse-variance weighting yields $t^2$; full derivation in the paper, Proposition 3.2). The second interactive demo below shows exactly this trade-off: per-$t$ landscapes on the left (biased-but-smooth at small $t$, sharp-but-speckled at large $t$) and the running $w(t)=t^2$-weighted combination on the right, which stays both sharp and smooth throughout.

### Why it works: a population-level guarantee

This is the part a demo can't show directly, so it's worth stating precisely. Consider the population (infinite-$K$, continuous-$t$) version of the same score, under oracle access to $v_p(t,x):=\mathbb E_p[y-x_0\mid x_t=x]$, the velocity field that conditional flow matching would converge to with infinite normal training data. For a test distribution $q$ (normal data has $q=p$; an anomaly distribution has $q\neq p$), the paper's main theoretical result is an **exact decomposition**:

$$
t^2\,\mathbb E_q\!\left[\|v_p(t,X_t)-(Y-X_0)\|_2^2\right] \;=\; \underbrace{\frac{t^2}{(1-t)^2}D_q(t)}_{\text{weighted denoising error}} \;+\; \underbrace{(1-t)^2\,J(q_t\Vert p_t)}_{\text{Fisher divergence}},
$$

where $D_q(t)=\mathbb E_q\|Y-\mu_q(X_t)\|_2^2$ is an endpoint-estimation error that stays bounded even as $t\to 1$, and $J(q_t\Vert p_t)$ is the Fisher divergence between the score functions of the test-path marginal $q_t$ and the normal-path marginal $p_t$ — it measures how far the *distribution* $y$ was drawn from has drifted from the normal distribution the model was trained on.

**On a normal image** ($q=p$), $q_t\equiv p_t$, so the Fisher term vanishes identically — only the irreducible denoising-error term remains, the same floor every normal image sits on. **On an anomalous image**, the Fisher term is strictly positive and is exactly the quantity that separates anomalies from normal images in the population limit: it doesn't depend on model error at all, only on how different the anomaly's local statistics are from normal. This is also precisely why aggregating across time matters, not just across paths: the decomposition shows early times lean on the Fisher (score-mismatch) term while late times lean on the (bounded) denoising term, so a single $t$ only ever sees part of the signal — the $w(t)=t^2$-weighted sum is the one combination that an inverse-variance argument says is proportioned correctly.

A natural follow-up question — what we actually *deploy* is the **learned** $v_\theta$, not the oracle $v_p$ — is addressed by a companion finite-sample/learned-field extension in the paper (and was independently re-derived and checked on this project's own toy and real 5-seed-trained checkpoints during the rebuttal process): the population identity above still holds with $v_\theta$ in place of $v_p$ up to an explicit, measurable field-approximation-error term, and ranking/false-positive-rate guarantees survive as long as that approximation error doesn't swamp the Fisher signal — which the paper verifies empirically stays true even far off-manifold.

### Adjustable test-time compute

$K$ (paths) and $T$ (time steps) are explicit, orthogonal compute knobs, not architecture choices — both only add independent, parallelizable forward passes through the same frozen $v_\theta$, at a total cost of $O(KT)$ evaluations per image. This gives a single detector that can run at low $K,T$ for high-throughput screening and scale up $K,T$ for accuracy-critical inspection, with no retraining in between — unlike reconstruction- or inversion-based detectors, where more "test-time compute" usually means an iterative optimization loop rather than a batch of independent forward passes.

### Why random seeds, not a search

It's tempting to ask: since minimum-voting over $K$ seeds is just approximating "the seed that best explains $y$," why not solve for that seed directly and skip the $K$ draws? On a simple 1D version of this model, that idea is provably catastrophic. Writing the mismatch as a function of the seed alone, $m(x_0) = \|v_\theta(x_t,t) - (y-x_0)\|^2$, completing the square shows $m(x_0) = b(t)^2\,(x_0 - x_0^\star)^2$ for an explicit $x_0^\star$ — meaning there is *always* some seed that drives the mismatch to exactly zero, for **any** image, normal or anomalous. Solving for it directly would silently defeat detection on every input. The reason minimum-voting works at all is that it only ever gets to pick among $K$ *independently, randomly drawn* seeds, and the zero-mismatch seed for a genuine anomaly sits so far in the tail of $\mathcal N(0,I)$ that $K$ random draws essentially never land near it — while for a normal image, a good-enough explaining seed is common enough that one of the $K$ draws usually finds it. The randomness of the seeds isn't an implementation detail to be optimized away; it's where the method's discriminating power actually comes from.

---

## Toy-Example Demonstrations {#toy-examples}

A live interactive demo illustrates the velocity-mismatch
mechanism on 2D toy data — a flow-matching model trained only on normal data,
run toward a real data point and an off-manifold point from the same starting
noise draws. Solid arrows show the model's predicted velocity; dashed lines
show the true heading. On the normal target they track each other; on the
off-manifold target they visibly diverge, and that growing disagreement is
the anomaly signal.


**Try it yourself** — drag the time slider (or press play). The demo shows the
paper's actual toy setup (Appendix B.1): an upper semicircle manifold, scored on
the paper's own grid and aggregation rule, with a near-manifold anomaly placed
closer to the boundary than a simple off-manifold gap — a harder, more subtle
detection case.

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
