---
title: "D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation"
author: ["Hao Yan"]
tags: ["Software", "Segmentation", "CVPR", "ShapePrior", "Convexity", "featured"]
draft: false
featured: true
layout: 'project-page'
authors:
- Shengzhe Chen
- Hao Yan
publication_types:
- paper-conference
publication: '*Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*'
date: '2026-01-01'
year: '2026'
url: /chen-dconvexity-cvpr-2026/
url_pdf: 'https://arxiv.org/abs/2605.19210v1'
url_code: 'https://github.com/ShengzheC/D-Convexity'
url_poster: 'https://cvpr.thecvf.com/virtual/2026/poster/39174'
url_project: '/chen-dconvexity-cvpr-2026/'
abstract: 'Convexity is a fundamental geometric prior that underlies many natural and man-made structures, yet remains challenging to impose effectively in end-to-end trainable segmentation networks. We revisit convexity from a functional perspective and propose a unified, threshold-free convexity prior based on the quasi-concavity of the network''s output mask function u. The first and second-order formulations produce a compact convolutional loss that can be densely applied across the image without thresholding, and integrate seamlessly with modern segmentation networks via the proposed Convex Gradient Projection Module (CGPM).'
summary: 'A unified, threshold-free differentiable convex-shape prior based on quasi-concavity of the segmentation mask function. Zero-, first-, and second-order characterizations yield a midpoint convexification algorithm and compact convolutional losses that integrate seamlessly with modern segmentation networks via the proposed Convex Gradient Projection Module (CGPM). Accepted to CVPR 2026 as a Highlight.'
---

## Overview {#overview}

**D-Convexity** is a unified, **threshold-free**, **fully differentiable** convex-shape prior
for data-driven image segmentation. Instead of constraining the binary mask at a fixed
threshold, we require the *entire* network output $u:\Omega\to[0,1]$ to be
**quasi-concave** — equivalently, *every* super-level set
$S_\gamma=\{\mathbf{x}\in\Omega \mid u(\mathbf{x})\geq\gamma\}$
is convex. From this single principle we derive **zero-, first-, and second-order**
characterizations that turn a hard global geometric constraint into local, differentiable
inequalities, yielding a compact convolutional loss and a drop-in **Convex Gradient
Projection Module (CGPM)**.

Accepted at **[CVPR 2026](https://cvpr.thecvf.com/virtual/2026/poster/39174)** as a **Highlight paper** (top 3%).

{{< figure src="figures/architecture.png" alt="D-Convexity architecture: Swin Transformer backbone produces a feature map o, which is passed through a sigmoid to give a raw mask u. The Convex Gradient Projection Module (CGPM) then iteratively projects u onto the quasi-concave manifold using the convex loss gradient, yielding a strictly convex final mask. Training uses cross-entropy on the raw mask and the quasi-concavity loss on the projected mask." width="100%" >}}

<p class="has-text-centered" style="max-width:900px;margin:0.5rem auto 1.5rem;font-size:0.95rem;color:#444;"><span class="figure-number">Figure 1:</span> Overall framework. A Swin-Transformer encoder–decoder backbone produces feature $o$; a sigmoid yields the raw mask $u=\mathcal{S}(o)$. The <strong>Convex Gradient Projection Module (CGPM)</strong> is an unrolled gradient-descent block ($v^0 \rightarrow v^1 \rightarrow \cdots \rightarrow v^T$) that projects $u$ onto the quasi-concave manifold by descending the convex loss $\nabla\mathcal{L}_{\mathrm{convex}}$. The network is trained with cross-entropy $\mathcal{L}_{\mathrm{CE}}$ on the raw mask and the quasi-concavity loss $\mathcal{L}_{\mathrm{convex}}$ on the projected mask.</p>

---

## Animated Demo: Zero/First/Second-Order Convexification {#animation}

The animation below visualizes the **midpoint (zero-order)**, **first-order gradient**, and
**second-order Hessian** convexification dynamics applied to a non-convex initial mask.
All three orders progressively regularize the shape into a convex region, but with
increasing levels of spatial smoothness.

{{< video src="figures/combined_all_orders.mp4" caption="Convexification dynamics under the proposed zero-, first-, and second-order quasi-concavity priors. Starting from non-convex inputs, the mask function u is iteratively updated by (left) the local midpoint rule (Algorithm 1, zero-order), (middle) the first-order gradient-based supporting-hyperplane condition, and (right) the second-order quadratic-form penalty Q_2(x). Higher-order priors produce progressively smoother convex shapes." width="100%" max_width="980px" >}}

---

## Motivation {#motivation}

Convexity is a fundamental prior: many anatomical structures (optic disc/cup, blood
vessels, organs) and man-made objects are convex or close-to-convex. Enforcing convexity
suppresses holes, fragmented predictions, and irregular boundary artifacts, especially
under **noise, occlusion, and limited training data**.

Existing approaches, however, have significant limitations:

- **Discrete formulations** (e.g. 1–0–1 collinear-triplet penalties, graph-cuts with
  convexity constraints, ILP/multicut decompositions) rely on combinatorial solvers and
  are **hard to differentiate** through.
- **Level-set/curvature methods** (non-negative curvature $\kappa\geq 0$,
  signed-distance Laplacian $\Delta\phi\geq 0$) certify convexity only at *one* chosen
  threshold (e.g. $\phi=0$) and are typically *necessary but not sufficient*.
- **Recent deep shape priors** still lack explicit, principled control over convexity
  at every confidence level.

**D-Convexity** resolves all three issues with a single functional view: the mask
function $u$ itself should be quasi-concave.

---

## Theory: Quasi-Concavity as a Unified Convex Prior {#theory}

We formalize convexity threshold-freely as quasi-concavity of $u$:

$$
u \text{ is quasi-concave} \;\Longleftrightarrow\; \forall \gamma,\; S_\gamma=\{\mathbf{x}\mid u(\mathbf{x})\geq\gamma\}\ \text{is convex}.
$$

{{< figure src="figures/quasi_concave.png" alt="Left: a concave function lies below its tangent plane everywhere. Right: a quasi-concave function may be steeper than any tangent plane, but every horizontal slice (super-level set) is still a convex region. The gradient at a level-set point x defines the supporting hyperplane (y-x) perpendicular to grad u." width="80%" >}}

<p class="has-text-centered" style="max-width:900px;margin:0.5rem auto 1.5rem;font-size:0.95rem;color:#444;"><span class="figure-number">Figure 2:</span> <strong>Concave vs. quasi-concave functions.</strong> A concave function (left) lies below every tangent plane — a <em>strong</em> property that most segmentation masks violate. A <strong>quasi-concave</strong> function (right) is the weaker, <em>threshold-free</em> notion D-Convexity uses: it only requires that every super-level set $S_\gamma$ be a convex region. At any boundary point $\mathbf{x}$, the supporting hyperplane is given by $\nabla u(\mathbf{x})^{\top}(\mathbf{y}-\mathbf{x})=0$ — this is the geometric content of our <strong>first-order condition</strong>.</p>

By considering different smoothness assumptions on $u$, we derive three equivalent (or
sufficient) characterizations:

### Zero-order condition ($u\in C^0$) {#zero-order}

> $u$ is quasi-concave $\Longleftrightarrow$ for all $\mathbf{x},\mathbf{y}\in\Omega,\ \lambda\in[0,1]$:
> $$u(\lambda\mathbf{x}+(1-\lambda)\mathbf{y}) \;\geq\; \min\{u(\mathbf{x}),u(\mathbf{y})\}.$$

A line segment joining two points above a level cannot dip below that level.

### First-order condition ($u\in C^1$) {#first-order}

> $u$ is quasi-concave $\Longleftrightarrow$ if $u(\mathbf{x})\geq u(\mathbf{y})$, then
> $\nabla u(\mathbf{y})^{\top}(\mathbf{x}-\mathbf{y})\geq 0.$

The gradient at every point defines a **supporting hyperplane** of the local
super-level set.

### Second-order condition ($u\in C^2$, sufficient) {#second-order}

> If for all $\mathbf{x}\in\Omega$ with $\nabla u(\mathbf{x})\neq 0$ the Hessian
> $\nabla^2 u(\mathbf{x}) \prec 0$ (strict negative definite) on the tangent space
> $T_\mathbf{x}=\{\mathbf{d}\mid \nabla u(\mathbf{x})^{\top}\mathbf{d}=0\}$,
> then $u$ is quasi-concave.

For 2D images this has the **compact convolutional form**:

$$
Q_2(\mathbf{x}) \;=\; u_x^2\,u_{yy} \;-\; 2\,u_x u_y\,u_{xy} \;+\; u_y^2\,u_{xx} \;<\;0,
$$

a quadratic form in the image gradient that can be evaluated densely as a tiny
fixed-kernel convolution — no thresholding required.

### A unifying lens {#unification}

Following Section 3.6 of the paper, D-Convexity **recovers many existing convex priors as special cases**,
with each prior mapped to one of our zero-, first-, or second-order quasi-concavity conditions.
The mapping below uses the **exact references from the CVPR 2026 paper**
([arXiv:2605.19210v1](https://arxiv.org/abs/2605.19210v1)):

- **Zero-order line-segment prior.**
  [Han, Kwon, Kim & Cho, *Noise-Robust Pupil Center Detection with Shape-Prior Loss*, IEEE Access 2020][han2020]
  require that for every $\mathbf{x},\mathbf{y}$ in the segmentation object, the line segment between them
  also lies inside it — this is exactly our **zero-order** condition (Theorem 1) applied over the
  image domain. Our formulation is more general because it applies to the continuous mask $u$ rather
  than a single thresholded region.

- **Half-disk / binary convexity characterization.**
  The indicator-mask condition $(u-1)(b_r\ast(2u-1))\geq 0$ proposed in
  [Liu, Tai & Luo, *Convex Shape Prior for Deep Neural Convolution Network based Eye Fundus Images Segmentation*, 2020](https://arxiv.org/abs/2005.07476),
  [Luo, Tai & Wang, *A New Binary Representation Method for Shape Convexity*, Analysis & Applications 2022](https://doi.org/10.1142/S0219530521500238), and
  [Luo, Chen, Xiao & Tai, *A Binary Characterization Method for Shape Convexity*, Applied Mathematical Modelling 2023](https://doi.org/10.1016/j.apm.2023.06.008)
  follows directly from our **first-order** supporting-hyperplane condition (Theorem 2): at a background
  pixel $\mathbf{y}$, Lemma 1 forces the foreground into the half-space
  $\nabla u(\mathbf{y})^{\top}(\mathbf{x}-\mathbf{y})\geq 0$, which intersected with a radius-$r$ disk
  gives $|B_r(\mathbf{y})\cap S|\leq \tfrac{1}{2}|B_r(\mathbf{y})|$.

- **Curvature priors** $\kappa\geq 0$.
  [Ukwatta et al., *Efficient Convex Optimization-Based Curvature Dependent Contour Evolution*, SPIE 2013][ukwatta2013] and
  [Yang et al., *A Level Set Method for Convexity Preserving Segmentation of Cardiac Left Ventricle*, ICIP 2017][yang2017]
  constrain non-negative curvature of level-set boundaries — corresponding to $Q_2(\mathbf{x})\leq 0$, the
  **necessary but not sufficient** weakening of our **second-order** condition $Q_2(\mathbf{x})<0$.

- **Signed-distance Laplacian priors** $\|\nabla\phi\|=1$ with $\Delta\phi\geq 0$.
  [Luo, Tai, Huo, Wang & Glowinski, *Convex Shape Prior for Multi-Object Segmentation*, ICCV 2019][luo2019] and
  [Yan, Tai, Liu & Huang, *Convexity Shape Prior for Level Set-Based Image Segmentation*, IEEE TIP 2020][yan2020]
  impose non-negativity of the signed-distance Laplacian. With $\phi=-u$, the curvature identity
  $\kappa=-Q_2/\|\nabla u\|^3$ shows $\kappa\geq 0 \Leftrightarrow Q_2\leq 0$; D-Convexity's strict
  $Q_2<0$ upgrades this into a *sufficient* convexity condition while remaining fully differentiable.

**Related discrete convexity priors** (discussed in Section 2 of the paper, and subsumed at the pixel-graph
scale by our zero-order view) include 1–0–1 collinear-triple penalties
([Gorelick, Veksler, Boykov & Nieuwenhuis, ECCV 2014 / TPAMI 2017][gorelick2014]),
multicut / ILP convexity constraints
([Royer, Richmond, Rother, Andres & Kainmüller, CVPR 2016][royer2016]), and relaxed star-type families
([Veksler, ECCV 2008][veksler2008];
[Gulshan et al., CVPR 2010][gulshan2010];
[Isack, Veksler, Sonka & Boykov, CVPR 2016][isack2016]).

So a single quasi-concavity principle subsumes discrete, half-disk, level-set, and curvature-based
shape priors in **one continuous, differentiable framework**, with each prior corresponding to the
smoothness order ($C^0$ / $C^1$ / $C^2$) at which it operates.

[han2020]: https://doi.org/10.1109/access.2020.2985095 "Han, Kwon, Kim & Cho. Noise-Robust Pupil Center Detection Through CNN-Based Segmentation With Shape-Prior Loss. IEEE Access, 2020."
[liu2020]: https://arxiv.org/abs/2005.07476 "Liu, Tai & Luo. Convex Shape Prior for Deep Neural Convolution Network based Eye Fundus Images Segmentation. arXiv:2005.07476, 2020."
[luo2022]: https://doi.org/10.1142/S0219530521500238
[luo2023]: https://doi.org/10.1016/j.apm.2023.06.008
[ukwatta2013]: https://doi.org/10.1117/12.2006787 "Ukwatta, Yuan, Qiu, Rajchl & Fenster. Efficient Convex Optimization-Based Curvature Dependent Contour Evolution. SPIE Medical Imaging, 2013."
[yang2017]: https://doi.org/10.1109/ICIP.2017.8296678 "Yang, Shi, Yao & Li. A Level Set Method for Convexity Preserving Segmentation of Cardiac Left Ventricle. ICIP, 2017."
[luo2019]: https://www.csd.uoc.gr/~hy471/papers/Convex_Shape_Prior_for_Multi-Object_Segmentation_ICCV_2019.pdf "Luo, Tai, Huo, Wang & Glowinski. Convex Shape Prior for Multi-Object Segmentation Using a Single Level Set Function. ICCV, 2019."
[yan2020]: https://doi.org/10.1109/TIP.2020.2998981 "Yan, Tai, Liu & Huang. Convexity Shape Prior for Level Set-Based Image Segmentation Method. IEEE Transactions on Image Processing, 2020."
[gorelick2014]: https://link.springer.com/chapter/10.1007/978-3-319-10602-1_44 "Gorelick, Veksler, Boykov & Nieuwenhuis. Convexity Shape Prior for Segmentation. ECCV, 2014 (journal version: TPAMI, 2017)."
[royer2016]: https://doi.org/10.1109/CVPR.2016.49 "Royer, Richmond, Rother, Andres & Kainmüller. Convexity Shape Constraints for Image Segmentation. CVPR, 2016."
[veksler2008]: https://doi.org/10.1007/978-3-540-88690-7_34 "Veksler. Star Shape Prior for Graph-Cut Image Segmentation. ECCV, 2008."
[gulshan2010]: https://doi.org/10.1109/CVPR.2010.5539890 "Gulshan, Rother, Criminisi, Blake & Zisserman. Geodesic Star Convexity for Interactive Image Segmentation. CVPR, 2010."
[isack2016]: https://openaccess.thecvf.com/content_cvpr_2016/html/Isack_Hedgehog_Shape_Priors_CVPR_2016_paper.html "Isack, Veksler, Sonka & Boykov. Hedgehog Shape Priors for Multi-Object Segmentation. CVPR, 2016."

---

## Loss Functions and CGPM {#cgpm}

The first- and second-order conditions become **local convolutional losses**, evaluated
densely over the image without any thresholding:

- **First-order loss** ($\mathcal{L}_{\text{1st}}$): penalize the positive part of the
  asymmetric pair inequality $\mathrm{ReLU}\big(\nabla u(\mathbf{y})^{\top}(\mathbf{y}-\mathbf{x})\big)$
  over a small $r$-radius neighborhood $\mathbf{x}\in N_{\mathbf{y}}$.
- **Second-order loss** ($\mathcal{L}_{\text{2nd}}$): penalize the positive part of
  $Q_2(\mathbf{x})+\delta$ weighted by $\|\nabla u(\mathbf{x})\|$:

$$
\mathcal{L}_{\text{2nd}}(u) \;=\; \frac{1}{|\Omega|}\sum_{\mathbf{x}\in\Omega} \|\nabla u(\mathbf{x})\|\cdot \mathrm{ReLU}\big(Q_2(\mathbf{x})+\delta\big).
$$

Both losses cost $\mathcal{O}(r^2|\Omega|)$ for the first-order and $\mathcal{O}(|\Omega|)$
for the second-order condition, are GPU-parallel, and have explicit closed-form gradients
(see Appendix E of the paper).

### Convex Gradient Projection Module (CGPM)

At inference time, the loss alone may not strictly enforce convexity. The **CGPM** solves a
small proximal optimization on the network logits:

$$
u_p \in \arg\min_{v\in[0,1]} \tfrac{1}{2}\|v-u\|^2 + \lambda\cdot \mathcal{L}_{\text{convex}}(v),
$$

with $\mathcal{L}_{\text{convex}}\in\{\mathcal{L}_{\text{1st}},\mathcal{L}_{\text{2nd}}\}$.
Implemented as an **unrolled gradient-descent module** on the logit space, CGPM is a
drop-in projection layer compatible with any segmentation backbone (U-Net, nnU-Net,
TransUNet, etc.):

```python
from CGPM import SegModelWithCGPM

model = UNet2D().to(device)
model.load_state_dict(ckpt)
model.eval()

SegCGPM = SegModelWithCGPM(model, backprop_to_backbone=False)
cgpm_output = SegCGPM(images)
```

CGPM can be used in **train mode** (back-propagated into the backbone) or as a
**post-hoc projection** (frozen backbone, projection only).

---

## Experimental Results {#experiments}

We evaluate D-Convexity on four segmentation benchmarks spanning cardiac MRI
(**ACDC**), iris segmentation (**CASIA**), and retinal optic-disc/cup
segmentation (**REFUGE**, **RIM-ONE-r3**). To assess **out-of-distribution
generalization**, models trained on REFUGE are evaluated *directly* on
RIM-ONE-r3 without fine-tuning. Reported metrics are Dice ↑, IoU ↑, and
Hausdorff Distance HD ↓.

### Qualitative comparison {#qualitative}

{{< figure src="figures/qualitative_comparison.png" alt="Qualitative segmentation comparison across cardiac MRI, eye, and retinal fundus images. Each row is one image; columns show (a) image, (b) ground truth, and predictions from (c) U-Net, (d) Swin-Unet, (e) Dcan, (f) Dmtn, (g) ConvMCD, (h) ActiveBoundary, (i) the proposed D-Convexity. Baselines produce fragmented holes (green false-negatives) and spurious lobes (red false-positives), while D-Convexity returns clean, simply-connected, convex regions that closely follow the ground truth boundary." caption="<span class=\"figure-number\">Figure 3: </span>**Qualitative segmentation comparison.** Rows: cardiac MRI (ACDC), iris (CASIA), and retinal optic-disc/cup (REFUGE & RIM-ONE-r3). Columns: (a) input, (b) ground truth, (c)–(h) six baselines, (i) **Proposed (D-Convexity)**. Color code: ▢ white = true positive, ■ black = true negative, <span style=\"color:#d62728;\">■</span> red = false positive, <span style=\"color:#2ca02c;\">■</span> green = false negative, <span style=\"color:#0a66c2;\">▢</span> blue = predicted boundary. Baselines tend to produce fragmented holes (green) and spurious lobes (red); D-Convexity yields **clean, simply-connected, convex** regions that tightly track the ground-truth boundary." width="100%" >}}

### Quantitative results {#quantitative}

{{< rawhtml >}}
<style>
  .dconv-results-wrap { overflow-x: auto; margin: 1.25rem 0; }
  table.dconv-results {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
    font-family: 'Noto Sans', sans-serif;
    background: #fff;
  }
  table.dconv-results th, table.dconv-results td {
    padding: 8px 10px;
    text-align: center;
    border-bottom: 1px solid #e6e6e6;
  }
  table.dconv-results thead tr.group th {
    background: #f5f7fa;
    font-weight: 700;
    border-bottom: 1px solid #d6d9df;
  }
  table.dconv-results thead tr.metric th {
    background: #fafbfd;
    font-weight: 600;
    color: #555;
    border-bottom: 2px solid #cfd3da;
  }
  table.dconv-results td.method, table.dconv-results th.method {
    text-align: left;
    font-weight: 500;
    white-space: nowrap;
  }
  table.dconv-results tr.proposed {
    background: #eaf3ff;
    font-weight: 700;
  }
  table.dconv-results tr.proposed td { border-bottom: 1px solid #c9def5; }
  table.dconv-results td.best { color: #0a66c2; font-weight: 700; }
  table.dconv-results td .sep { color: #aaa; }
  table.dconv-results caption {
    caption-side: top;
    text-align: left;
    padding: 0.25rem 0 0.75rem 0;
    font-size: 0.95rem;
    color: #444;
  }
</style>

<div class="dconv-results-wrap">
<table class="dconv-results">
  <caption><strong>Table 1.</strong> Performance of baseline and shape-aware methods on the
    ACDC, CASIA, REFUGE, and RIM-ONE-r3 datasets. Models trained on REFUGE are evaluated
    <em>directly</em> on RIM-ONE-r3 to assess cross-dataset generalization.
    Best values per column are in <span style="color:#0a66c2;font-weight:700;">blue</span>;
    our method (<em>Proposed</em>) is highlighted.</caption>
  <thead>
    <tr class="group">
      <th class="method" rowspan="2">Method</th>
      <th colspan="3">ACDC</th>
      <th colspan="3">CASIA</th>
      <th colspan="3">REFUGE</th>
      <th colspan="3">RIM-ONE-r3</th>
    </tr>
    <tr class="metric">
      <th>Dice&nbsp;↑</th><th>IoU&nbsp;↑</th><th>HD&nbsp;↓</th>
      <th>Dice&nbsp;↑</th><th>IoU&nbsp;↑</th><th>HD&nbsp;↓</th>
      <th>Dice&nbsp;↑</th><th>IoU&nbsp;↑</th><th>HD&nbsp;↓</th>
      <th>Dice&nbsp;↑</th><th>IoU&nbsp;↑</th><th>HD&nbsp;↓</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="method">U-Net [28]</td>
      <td>89.52</td><td>81.02</td><td>28.04</td>
      <td>94.65</td><td>89.84</td><td>2.549</td>
      <td>84.66</td><td>73.71</td><td>11.07</td>
      <td>76.48</td><td>61.92</td><td>20.57</td>
    </tr>
    <tr>
      <td class="method">Swin-Unet [3]</td>
      <td>95.42</td><td>91.23</td><td>4.965</td>
      <td>94.76</td><td>90.05</td><td>2.399</td>
      <td>84.00</td><td>72.42</td><td>7.863</td>
      <td>81.00</td><td>68.07</td><td>15.32</td>
    </tr>
    <tr>
      <td class="method">DCAN [4]</td>
      <td>93.38</td><td>87.59</td><td>6.946</td>
      <td>94.90</td><td>90.29</td><td>2.413</td>
      <td>80.66</td><td>67.59</td><td>9.379</td>
      <td>76.23</td><td>61.59</td><td>16.53</td>
    </tr>
    <tr>
      <td class="method">DMTN [31]</td>
      <td>92.60</td><td>86.22</td><td>8.500</td>
      <td>94.92</td><td>90.34</td><td>2.337</td>
      <td>82.36</td><td>70.01</td><td>9.337</td>
      <td>78.39</td><td>64.46</td><td>16.80</td>
    </tr>
    <tr>
      <td class="method">ConvMCD [25]</td>
      <td>93.44</td><td>87.68</td><td>15.53</td>
      <td>95.03</td><td>90.54</td><td>2.323</td>
      <td>78.38</td><td>64.45</td><td>12.51</td>
      <td>76.71</td><td>62.22</td><td>18.18</td>
    </tr>
    <tr>
      <td class="method">Active Boundary [35]</td>
      <td>90.93</td><td>81.38</td><td>24.71</td>
      <td>94.49</td><td>89.55</td><td>2.656</td>
      <td>84.82</td><td>73.63</td><td>10.59</td>
      <td>75.37</td><td>60.48</td><td>20.64</td>
    </tr>
    <tr class="proposed">
      <td class="method">Proposed (D-Convexity)</td>
      <td class="best">95.46</td><td class="best">91.31</td><td class="best">4.702</td>
      <td>94.71</td><td>89.94</td><td class="best">2.288</td>
      <td class="best">88.61</td><td class="best">79.54</td><td class="best">5.859</td>
      <td class="best">83.09</td><td class="best">71.08</td><td class="best">12.59</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}

**Takeaways.**

- **Best overall on 3 of 4 datasets.** D-Convexity is the top performer on
  ACDC, REFUGE, and RIM-ONE-r3 across all three metrics, and is best on
  Hausdorff Distance on CASIA. Dice/IoU on CASIA are essentially saturated
  for all methods (within 0.3% of each other).
- **Largest gains on hard, shape-driven tasks.** On REFUGE, D-Convexity
  improves Dice from 84.82 → **88.61** ( +3.79) and reduces HD from 7.863 →
  **5.859** ( −2.0) versus the strongest baseline, with similar gains on the
  ACDC cardiac task.
- **Strong out-of-distribution generalization.** When the REFUGE-trained
  model is applied *directly* to RIM-ONE-r3 (different acquisition device
  and population), D-Convexity still wins by **+2.1 Dice** and **−2.7 HD**
  over Swin-Unet — evidence that the convex shape prior acts as a robust,
  task-agnostic regularizer rather than overfitting to a particular dataset.
- **Drop-in improvement.** All gains are obtained with the same backbone
  segmentation network as the baselines, with CGPM as a plug-in module — no
  architectural changes are required.

---

## Key Contributions {#key-ideas}

- **Quasi-concavity as a unified convex prior.** We formalize convexity of *all*
  super-level sets as quasi-concavity of the network output $u$, yielding a
  threshold-free, differentiable, image-domain constraint.
- **Multi-order characterizations.** Zero-, first-, and second-order conditions for
  $u\in C^0,C^1,C^2$, corresponding to different mask smoothness regimes.
- **Compact convolutional losses.** The first- and second-order conditions reduce to
  tiny fixed-kernel convolutions, allowing dense evaluation across the image at
  $\mathcal{O}(|\Omega|)$ cost.
- **Convex Gradient Projection Module (CGPM).** A plug-and-play unrolled-optimization
  module that strictly enforces convexity at inference time.
- **Theoretical unification.** Discrete 1–0–1 priors, half-disk convolution priors, and
  curvature / signed-distance Laplacian priors are all recovered as special cases or
  necessary weakenings of our framework.
- **Empirical gains.** Consistent convexity and shape-regularity improvements across
  multiple medical-imaging datasets (retinal fundus, cardiac MRI, iris, etc.),
  outperforming task-specific networks and prior shape-aware methods.

---

## Quick Start {#quickstart}

The reference implementation is available on GitHub:
[**ShengzheC/D-Convexity**](https://github.com/ShengzheC/D-Convexity).

For intuition on the convexification algorithm and the zero-order dynamics, start with
the notebook:

```
Convexification_Algorithm.ipynb
```

The CGPM segmentation framework lives in `CGPM.py`, and the first- and second-order
losses in `loss.py`.

---

## Resources {#resources}

- **Paper (arXiv):** [arXiv:2605.19210](https://arxiv.org/abs/2605.19210v1)
- **Code:** [github.com/ShengzheC/D-Convexity](https://github.com/ShengzheC/D-Convexity)
- **CVPR 2026 virtual poster:** [cvpr.thecvf.com/virtual/2026/poster/39174](https://cvpr.thecvf.com/virtual/2026/poster/39174)
- **Venue:** CVPR 2026 (Highlight, top 3%)

---

## BibTeX {#bibtex}

```bibtex
@inproceedings{chen2026dconvexity,
  title     = {D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation},
  author    = {Chen, Shengzhe and Yan, Hao},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2026},
  note      = {Accepted as Highlight (top 3\%)},
  eprint    = {2605.19210},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  url       = {https://arxiv.org/abs/2605.19210v1}
}
```
