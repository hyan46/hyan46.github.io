---
title: "Path-Coupled Bellman Flows for Distributional Reinforcement Learning"
author: ["Hao Yan"]
tags: ["Software", "ReinforcementLearning", "featured"]
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
publication: '*Proceedings of the International Conference on Machine Learning*'
date: '2026-01-01'
year: '2026'
url_code: 'https://github.com/your-repo'
---

## Abstract {#abstract}

Path-Coupled Bellman Flows (PCBF) introduces a flow-based perspective for
distributional reinforcement learning. Rather than treating each return as an
independent sample, PCBF couples the noise along a Bellman trajectory, yielding
a path-consistent flow-matching objective for the return distribution. The
method was accepted as a regular-track paper at ICML 2026.


## Method Overview {#method-overview}

{{< figure src="figures/pcbf_valueflows_noise_comparison.png" alt="PCBF Architecture" caption="<span class=\"figure-number\">Figure 1: </span>Architecture of Path-Coupled Bellman Flows (PCBF). A shared noise variable is propagated along the Bellman path, producing a path-consistent flow-matching objective for return distributions." width="100%" >}}


## Key Ideas {#key-ideas}

-   **Distributional flow matching:** Learn return distributions through a
    path-coupled flow objective that aligns the conditional flow with the Bellman
    target.
-   **Shared-noise path coupling:** Propagating a shared noise variable along
    Bellman paths reduces the corrected Bellman residual relative to
    independent-noise baselines.
-   **Variance reduction via control variates:** A $\lambda$-parameterized control
    variate decouples variance reduction from distributional bias and remains
    robust across hyperparameter values.
-   **Stable offline RL training:** PCBF improves optimization stability under
    D4RL and OGBench offline benchmarks, including pixel-based tasks.
-   **Policy extraction:** The learned return distribution is used for downstream
    decision-making and policy selection.


## Toy Environments {#toy-environments}

{{< figure src="figures/physics_combined.png" alt="Toy environments" caption="<span class=\"figure-number\">Figure 2: </span>Learned PCBF maps on toy environments. Left top (Solitaire); right top (Bernoulli); bottom (Discrete MC). PCBF recovers the ground-truth return distribution structure across all three settings." width="90%" >}}

{{< figure src="figures/toy22.png" alt="CDF comparison on toy environments" caption="<span class=\"figure-number\">Figure 3: </span>Distributional accuracy comparison on toy environments. Learned return CDFs for PCBF and Value Flows (dcfm $\in \{0, 0.5, 1\}$) versus ground-truth references. PCBF tracks the ground-truth CDF more accurately, particularly in high-variance regimes." width="90%" >}}


## Path Consistency {#path-consistency}

{{< figure src="figures/nfe.png" alt="NFE residual comparison" caption="<span class=\"figure-number\">Figure 4: </span>Corrected Bellman residual $r_{\mathrm{corr}}(t, N)$ on Solitaire Dice. Shared-noise PCBF (blue) maintains lower residuals than independent-noise coupling (orange) across diffusion times and function-evaluation budgets." width="80%" >}}


## Offline RL Benchmarks {#offline-rl-benchmarks}

{{< figure src="figures/ogbench.png" alt="OGBench results" caption="<span class=\"figure-number\">Figure 5: </span>Offline RL results on OGBench. PCBF achieves consistent improvements over distributional and non-distributional baselines across state-based and pixel-based domains." width="90%" >}}

{{< figure src="figures/combined_final_curve.png" alt="Aggregate learning curves" caption="<span class=\"figure-number\">Figure 6: </span>Aggregate offline RL learning curves combining D4RL and OGBench tasks. PCBF (ours) shows faster convergence and higher final performance." width="90%" >}}


## Ablations {#ablations}

{{< figure src="figures/two_ablation.png" alt="Lambda ablation" caption="<span class=\"figure-number\">Figure 7: </span>Hyperparameter sensitivity analysis (PCBF vs. Value Flows) on Solitaire and Discrete MC. Increasing the Value-Flows consistency coefficient (orange, dashed) degrades distributional accuracy, while the PCBF control variate $\lambda$ (blue, solid) remains stable across a wide range of values." width="90%" >}}

{{< figure src="figures/variance_reduction.png" alt="Variance reduction" caption="<span class=\"figure-number\">Figure 8: </span>Variance reduction via $\lambda$-parameterized control variates. The control variate substantially reduces estimator variance without introducing bias." width="80%" >}}


## BibTeX {#bibtex}

```bibtex
@inproceedings{xu2026pathcoupled,
  title={Path-Coupled Bellman Flows for Distributional Reinforcement Learning},
  author={Xu, Boyang and Zou, Qing and Yang, Siqin and Yan, Hao},
  booktitle={Proceedings of the International Conference on Machine Learning},
  year={2026},
  note={ICML 2026 regular track}
}
```
