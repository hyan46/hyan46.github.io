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

{{< figure src="figures/teaser.png" alt="Velocity mismatch in the (x,t) plane: affine paths toward a normal target stay aligned with the learned flow, while paths toward an anomalous target visibly diverge from it." caption="<span class=\"figure-number\">Figure 1: </span>**Velocity mismatch in the $(x,t)$ plane.** Light arrows show the learned flow $v_\\theta(x,t)$ from noise to normal data. Affine paths from the same starting noise $x_0$ target either a normal sample (green) or an anomalous sample (red). At selected times, the predicted velocity (blue) aligns with the geometric velocity toward normal targets but disagrees for anomalous targets — that disagreement is the anomaly signal Flow Mismatching detects." width="90%" >}}

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
