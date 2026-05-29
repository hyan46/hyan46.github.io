---
title: "Path-Coupled Bellman Flows for Distributional Reinforcement Learning"
author: ["Hao Yan"]
tags: ["Software", "ReinforcementLearning", "DistributionalRL", "FlowMatching", "featured"]
draft: false
featured: true
layout: 'project-page'
authors:
- Boyang Xu
- Qing Zou
- Siqin Yang
- Hao Yan
publication_types:
- paper-conference
publication: '*Proceedings of the International Conference on Machine Learning (ICML)*'
date: '2026-01-01'
year: '2026'
url: /xu-path-coupled-icml-2026/
url_pdf: 'https://arxiv.org/abs/2605.08253'
url_code: 'https://github.com/BoyangASU/path-coupled-bellman-flows'
url_project: '/xu-path-coupled-icml-2026/'
abstract: 'Distributional reinforcement learning (DRL) models the full return distribution, but typically relies on finite-dimensional categorical or quantile approximations, often involving projection or quantile-regression approximations to the Bellman target, together with independently sampled bootstrap targets that obscure transport structure and add variance. We present Path-Coupled Bellman Flows (PCBF), a continuous-time DRL method that encodes Bellman endpoint consistency and pathwise Bellman-coupled geometry within generative flow trajectories. PCBF represents return distributions via flow matching and couples the paths of consecutive states through shared base noise, yielding a geometric Bellman flow relation between velocity fields. This structure enables a lambda-parameterized control-variate target that reduces training variance while preserving the source and Bellman endpoint geometry. Experiments on analytically tractable MRPs, OGBench, and D4RL show improved distributional fidelity, training stability, and competitive offline RL performance.'
summary: 'Flow-matching distributional RL with source-consistent Bellman-coupled paths and shared-noise coupling between current and successor return flows. A lambda-parameterized control variate reduces bootstrap variance while preserving Gaussian source and Bellman endpoint geometry. Strong distributional fidelity on toy MRPs and competitive offline RL on 38 OGBench and D4RL tasks. Accepted to ICML 2026 as a regular presentation.'
---

## Overview {#overview}

**Path-Coupled Bellman Flows (PCBF)** is a continuous-time distributional reinforcement
learning method that learns return distributions with **flow matching** using
**source-consistent Bellman-coupled paths**: the current path starts from the required base
prior at $t{=}0$, reaches the Bellman target at $t{=}1$, and maintains a pathwise affine
relation to the successor flow at intermediate times. PCBF couples current and successor
return flows through **shared base noise** and uses a **$\lambda$-parameterized control
variate** that trades controlled bias for variance reduction in critic training.

Accepted at **[ICML 2026](https://icml.cc)** as a **regular-track presentation**.

{{< figure src="figures/comparison.png" alt="Path-coupled Bellman geometry: uncoupled flows use independent noise; source-inconsistent flows violate the base prior at t=0; PCBF uses shared noise to preserve both the Gaussian source and the Bellman endpoint." caption="<span class=\"figure-number\">Figure 1: </span>**Path-coupled Bellman geometry.** Each panel shows a single current (blue) and successor (orange) return flow. **(a)** Uncoupled: independent source noise — flows are unrelated except in distribution. **(b)** Source-inconsistent: the successor starts from $R+\\gamma X_0$, violating the base prior at $t{=}0$. **(c)** **PCBF:** shared noise drives both flows, preserving the base prior at $t{=}0$ and the Bellman endpoint at $t{=}1$." width="100%" >}}

---

## Animated Demo {#animation}

The animation below visualizes learned return transport on the **Discrete Monte Carlo**
toy environment: particles flow from a Gaussian source at $t{=}0$ to the learned return
distribution at $t{=}1$ along PCBF Bellman-coupled trajectories.

{{< figure src="figures/demo.gif" alt="Demonstration of PCBF learned return transport on the Discrete MC environment" caption="Learned PCBF return transport on the Discrete Monte Carlo environment. Individual particles (colored trajectories) are transported from the base noise distribution at $t{=}0$ to state-dependent return outcomes at $t{=}1$." width="100%" max_width="980px" >}}

---

## Motivation {#motivation}

Distributional reinforcement learning (DRL) models the full distribution of returns rather
than only their expectation, enabling richer uncertainty representations and often better
empirical performance. Most practical DRL algorithms, however, rely on **finite-dimensional
approximations** — categorical projections or quantile assignments — that introduce bias
when the Bellman update does not align with fixed support points.

Reframing DRL as **continuous probability transport** makes flow matching a natural
framework: the distributional Bellman equation defines an affine transport relationship,
and a neural velocity field can transport samples from a simple Gaussian prior to the
return law without heuristic projections.

Directly enforcing an uncorrected pointwise Bellman map inside flow composition fails in
two critical ways:

- **Source boundary mismatch.** Flow matching requires generation to start from a fixed
  simple prior (e.g., $\mathcal{N}(0,1)$), but an uncorrected Bellman update
  $Z_t = R + \gamma Z'_t$ starts from $R + \gamma X_0 \neq X_0$.
- **High-variance bootstrapping.** When current and successor noises are sampled
  independently, intermediate trajectories are not pathwise aligned; Bellman consistency
  can only be enforced at the endpoint, yielding unstable per-sample targets.

PCBF resolves both issues through **source-consistent Bellman path correction** and
**shared-noise path coupling**, cleanly separating geometric flow requirements from
Bellman bootstrapping variance.

---

## Method: Path-Coupled Bellman Flows {#method}

### Shared-noise Bellman paths {#shared-noise-paths}

Given shared base noise $X_0 \sim \mathcal{N}(0,1)$ and a successor return sample
$X' = \psi_{\theta^-}^{1}(X_0 \mid s', a')$ from the target flow map, PCBF defines
time-synchronized linear interpolation paths:

$$
Z^{s'}_t = (1-t)X_0 + t X'
\qquad\text{(successor path)},
$$

$$
Z^{s}_t = (1-t)X_0 + t\bigl(R + \gamma X'\bigr)
\qquad\text{(current path)}.
$$

An equivalent form that reveals the Bellman geometry is:

$$
Z^s_t = t R + \gamma Z^{s'}_t + (1-t)(1-\gamma)X_0.
$$

The residual anchor $(1-t)(1-\gamma)X_0$ guarantees exact alignment at $t{=}0$ regardless
of $\gamma$, while $Z^s_1 = R + \gamma X'$ satisfies the distributional Bellman boundary
at $t{=}1$. Differentiating yields the unbiased BCFM target
$\dot Z^s_t = R + \gamma X' - X_0$.

### Lambda-parameterized control variates {#lambda-target}

To reduce variance from the noisy successor sample $X'$, PCBF forms the training target
$u_t^\lambda$ from two pieces:

- **Sample Bellman velocity (baseline):** $Y = R + \gamma X' - X_0$. This is unbiased but
  can have high variance because it depends directly on the bootstrapped successor return
  $X'$.
- **Control-variate correction:** $\lambda \cdot \bigl( v_{\theta^-}(t, Z^{s'}_t \mid s', a') - (X' - X_0) \bigr)$,
  where $v_{\theta^-}$ is the lagged target velocity field along the successor path
  $Z^{s'}_t$.

Putting them together,

$u_t^\lambda = Y + \lambda \bigl( v_{\theta^-}(t, Z^{s'}_t \mid s', a') - (X' - X_0) \bigr)$.

Setting $\lambda = 0$ recovers the unbiased sample Bellman target. Values $\lambda > 0$
introduce a variance-reducing correction using successor-flow velocity predictions. With
shared-noise coupling, the induced bias stays small: in a linear–Gaussian model, shared
noise ($\rho = 1$) gives bias on the order of $(1-\gamma)(1-t)$, which vanishes when
$\gamma \approx 1$ and at the flow endpoints $t \in \{0, 1\}$.

### Policy extraction for offline RL {#policy-extraction}

At deployment, a behavior-cloned proposal policy samples $K{=}16$ candidate actions; each
is scored by the mean terminal return under the learned flow
$\hat Q_\theta(s,a) = \frac{1}{M}\sum_m \psi_\theta^{1}(X_{0,m}\mid s,a)$, and the
highest-scoring action is executed.

---

## Toy Environments: Distributional Fidelity {#toy-environments}

We validate PCBF on three analytically tractable environments with known return laws:
**Solitaire Dice** (heavy-tailed discrete returns), **Bernoulli MRP** (uniform return on
$[0,2]$), and **Discrete Monte Carlo Chain** (multimodal finite-horizon returns).

{{< figure src="figures/physics_combined.png" alt="Learned PCBF maps on Solitaire, Bernoulli, and Discrete MC toy environments" caption="<span class=\"figure-number\">Figure 2: </span>**Learned PCBF maps on toy environments.** Solitaire (top left), Bernoulli (top right), Discrete MC (bottom). PCBF recovers heavy-tailed, uniform, and multimodal return structures and closely matches ground-truth histograms." width="90%" >}}

{{< figure src="figures/toy22.png" alt="CDF comparison of PCBF vs Value Flows on toy environments" caption="<span class=\"figure-number\">Figure 3: </span>**Distributional accuracy on toy environments.** Learned return CDFs for PCBF and Value Flows (dcfm $\\in \\{0, 0.5, 1\\}$) versus ground-truth references. PCBF consistently tracks the reference CDFs; Value Flows degrades as dcfm increases, systematically underestimating return variance." width="90%" >}}

{{< figure src="figures/two_ablation.png" alt="Hyperparameter sensitivity of PCBF vs Value Flows on Solitaire and Discrete MC" caption="<span class=\"figure-number\">Figure 4: </span>**Hyperparameter sensitivity (PCBF vs. Value Flows).** On Solitaire and Discrete MC, increasing Value Flows' dcfm coefficient degrades Wasserstein error, while PCBF's $\\lambda$-target remains robust across a wide range of values." width="90%" >}}

{{< figure src="figures/variance_reduction.png" alt="Variance reduction via lambda control variates during training" caption="<span class=\"figure-number\">Figure 5: </span>**Variance reduction via $\\lambda$-parameterized control variates.** Larger $\\lambda$ yields smoother Bellman velocity regression loss trajectories (lower within-run standard deviation), validating the control-variate mechanism." width="80%" >}}

---

## Pathwise Bellman Residual and Discretization {#path-consistency}

PCBF enforces the Bellman endpoint at $t{=}1$ by construction, but training uses a
finite-step Euler solver (10 NFE). Shared-noise coupling yields smaller **corrected
Bellman residuals** $r_{\mathrm{corr}}(t,N)$ than independent-noise ablations across
solver budgets $N \in \{4,8,16,32\}$:

{{< figure src="figures/nfe.png" alt="Corrected Bellman residual on Solitaire Dice for shared vs independent noise coupling" caption="<span class=\"figure-number\">Figure 6: </span>**Corrected Bellman residual** $r_{\\mathrm{corr}}(t,N)$ on Solitaire Dice. Shared-noise PCBF (blue) maintains lower residuals than independent-noise coupling (orange) across flow times and Euler budgets." width="80%" >}}

---

## Offline RL Benchmarks {#offline-rl-benchmarks}

We evaluate PCBF on **38 offline RL tasks**: 30 OGBench single-task variants (four
state-based manipulation domains and two pixel-based domains) plus eight D4RL Adroit tasks.
Baselines include distributional methods (IQN, CODAC, Value Flows), flow-based scalar
critics (FloQ, FQL), and IQL.

{{< figure src="figures/ogbench.png" alt="OGBench task illustrations" caption="<span class=\"figure-number\">Figure 7: </span>**OGBench tasks.** State-based cube, scene, and puzzle manipulation environments and pixel-based visual variants used in our evaluation." width="70%" >}}

### Aggregated results {#quantitative}

{{< rawhtml >}}
<style>
  .pcbf-results-wrap { overflow-x: auto; margin: 1.25rem 0; }
  table.pcbf-results {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.92rem;
    font-family: 'Noto Sans', sans-serif;
    background: #fff;
  }
  table.pcbf-results th, table.pcbf-results td {
    padding: 8px 10px;
    text-align: center;
    border-bottom: 1px solid #e6e6e6;
  }
  table.pcbf-results thead tr.group th {
    background: #f5f7fa;
    font-weight: 700;
    border-bottom: 1px solid #d6d9df;
  }
  table.pcbf-results td.domain, table.pcbf-results th.domain {
    text-align: left;
    font-weight: 500;
    white-space: nowrap;
  }
  table.pcbf-results tr.proposed {
    background: #eaf3ff;
    font-weight: 700;
  }
  table.pcbf-results tr.proposed td { border-bottom: 1px solid #c9def5; }
  table.pcbf-results td.best { color: #0a66c2; font-weight: 700; }
  table.pcbf-results caption {
    caption-side: top;
    text-align: left;
    padding: 0.25rem 0 0.75rem 0;
    font-size: 0.95rem;
    color: #444;
  }
</style>

<div class="pcbf-results-wrap">
<table class="pcbf-results">
  <caption><strong>Table 1.</strong> Offline RL results on OGBench and D4RL Adroit.
    Success rates (%) for OGBench domains (5 tasks each) and normalized scores for D4RL.
    Results averaged over 8 seeds (4 for pixel tasks). Bold values are within 95% of the
    best method on each domain; <em>PCBF (Ours)</em> is highlighted.</caption>
  <thead>
    <tr class="group">
      <th class="domain">Domain</th>
      <th>IQN</th>
      <th>CODAC</th>
      <th>FloQ</th>
      <th>FQL</th>
      <th>IQL</th>
      <th>Value Flows</th>
      <th>PCBF (Ours)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="domain">cube-double-play (5 tasks)</td>
      <td>42 ± 8</td><td>61 ± 6</td><td>47 ± 14</td><td>29 ± 6</td><td>7 ± 1</td><td>69 ± 4</td>
      <td class="best">71 ± 5</td>
    </tr>
    <tr>
      <td class="domain">scene-play (5 tasks)</td>
      <td>40 ± 1</td><td>55 ± 1</td><td class="best">58 ± 4</td><td>56 ± 2</td><td>28 ± 3</td><td class="best">59 ± 4</td>
      <td>54 ± 4</td>
    </tr>
    <tr>
      <td class="domain">puzzle-4×4-play (5 tasks)</td>
      <td>27 ± 4</td><td>20 ± 18</td><td>28 ± 6</td><td>17 ± 5</td><td>7 ± 2</td><td>27 ± 4</td>
      <td class="best">30 ± 4</td>
    </tr>
    <tr>
      <td class="domain">cube-triple-play (5 tasks)</td>
      <td>6 ± 0</td><td>2 ± 1</td><td>8 ± 3</td><td>4 ± 2</td><td>1 ± 1</td><td class="best">14 ± 3</td>
      <td>4 ± 1</td>
    </tr>
    <tr>
      <td class="domain">D4RL adroit (8 tasks)</td>
      <td>66 ± 5</td><td>69 ± 0</td><td>70 ± 5</td><td class="best">71 ± 4</td><td>70</td><td>65 ± 2</td>
      <td class="best">69 ± 2</td>
    </tr>
    <tr>
      <td class="domain">visual-antmaze-teleport (5 tasks)</td>
      <td>4 ± 2</td><td>—</td><td>—</td><td>5 ± 2</td><td>6 ± 4</td><td>13 ± 4</td>
      <td class="best">14 ± 4</td>
    </tr>
    <tr>
      <td class="domain">visual-cube-double-play (5 tasks)</td>
      <td>1 ± 0</td><td>—</td><td>—</td><td>6 ± 1</td><td>11 ± 6</td>      <td class="best">13 ± 2</td>
      <td>3 ± 0</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}

**Takeaways.**

- **Selective but strong gains.** PCBF achieves best or near-best aggregate performance on
  **cube-double-play**, **puzzle-4×4-play**, **D4RL Adroit**, and
  **visual-antmaze-teleport**, where critic-side return-law fidelity and variance-controlled
  bootstrapping affect action ranking.
- **Best distributional fidelity on toys.** On analytically tractable MRPs, PCBF closely
  tracks ground-truth CDFs and remains robust to $\lambda$, while Value Flows degrades as
  the DCFM consistency weight increases.
- **Honest limitations.** On **cube-triple-play** and **visual-cube-double-play**, PCBF
  underperforms Value Flows — long-horizon sparse-reward and pixel-based settings remain
  challenging when policy extraction, visual encoders, or $\lambda$ selection become
  bottlenecks.
- **Similar cost to Value Flows.** PCBF uses ~60 GB GPU memory and ~2.5× wall-clock versus
  scalar critics on OGBench (single A100, $10^6$ steps); training requires 10-step Euler
  integration of the velocity field.

---

## Key Contributions {#key-ideas}

- **Source-consistent Bellman-interpolated paths** that resolve the $t{=}0$ boundary mismatch
  of uncorrected pointwise Bellman paths while preserving the Bellman endpoint at $t{=}1$.
- **Shared-noise path coupling** that aligns current and successor return flows pathwise,
  inducing a geometric Bellman relation between velocity fields.
- **$\lambda$-parameterized control-variate target** with a distribution-free $L_2$ bias
  bound and a linear–Gaussian closed form explaining why shared-noise coupling shrinks
  intrinsic bias.
- **Population velocity identification**, shared-noise Bellman contraction, and Euler
  integration sensitivity analysis supporting stable flow-based distributional critics.
- **Comprehensive evaluation** on Solitaire Dice, Bernoulli, and Discrete MC toy MRPs plus
  38 OGBench and D4RL offline RL tasks.

---

## Quick Start {#quickstart}

The reference implementation is available on GitHub:
[**BoyangASU/path-coupled-bellman-flows**](https://github.com/BoyangASU/path-coupled-bellman-flows).

PCBF is implemented in JAX, adapted from the FQL codebase. Key hyperparameters: 10 Euler
integration steps, batch size 256, learning rate $3\times10^{-4}$, and domain-tuned
$\lambda$ (see paper Tables for per-domain values). State-based tasks train for 1M
gradient steps; pixel-based tasks for 500K steps.

---

## Resources {#resources}

- **Paper (arXiv):** [arXiv:2605.08253](https://arxiv.org/abs/2605.08253)
- **Code:** [github.com/BoyangASU/path-coupled-bellman-flows](https://github.com/BoyangASU/path-coupled-bellman-flows)
- **Venue:** ICML 2026 (regular track)

---

## BibTeX {#bibtex}

```bibtex
@inproceedings{xu2026pathcoupled,
  title     = {Path-Coupled Bellman Flows for Distributional Reinforcement Learning},
  author    = {Xu, Boyang and Zou, Qing and Yang, Siqin and Yan, Hao},
  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
  year      = {2026},
  note      = {Regular track},
  eprint    = {2605.08253},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url       = {https://arxiv.org/abs/2605.08253}
}
```
