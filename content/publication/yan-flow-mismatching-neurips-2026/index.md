---
title: "Flow Mismatching: Unsupervised Anomaly Detection via Velocity Discrepancies in Flow Matching Models"
author: ["Hao Yan"]
tags: ["Software", "AnomalyDetection", "FlowMatching", "GenerativeModels", "NeurIPS", "featured"]
draft: false
featured: true
layout: 'project-page'
authors:
- Hao Yan
# [AUTHORS — confirm full author list / order from the paper; only "Hao Yan" was
#  given to us directly, so no co-authors have been added. Add them above in
#  submission order, e.g.:
# - First Last
# - Hao Yan
publication_types:
- paper-conference
publication: '*Advances in Neural Information Processing Systems (NeurIPS)*'
date: '2026-01-01'
year: '2026'
url: /yan-flow-mismatching-neurips-2026/
url_pdf: ''   # [ARXIV / OPENREVIEW LINK — paste link once available]
url_code: ''  # [CODE REPO URL — paste once a public repo exists]
url_project: '/yan-flow-mismatching-neurips-2026/'
abstract: '[ABSTRACT — paste verbatim from the paper (NeurIPS 2026 submission 9856). We could not locate the manuscript text in any accessible location (see Caveats below), so no abstract text has been invented here.]'
summary: '[ONE-TO-TWO SENTENCE SUMMARY — paste or write from the paper abstract once available.]'
---

## Overview {#overview}

**Flow Mismatching** is an **unsupervised anomaly detection** method built on
**flow matching** generative models. The core idea — per the title and submission
metadata available to us — is to detect anomalies from **velocity discrepancies**:
mismatches between a flow-matching model's *predicted* velocity field and the
*true* (or expected) velocity implied by a sample's trajectory, accumulated into an
anomaly score.

> **[OVERVIEW TEXT — PLACEHOLDER.]** We were not able to access the paper's actual
> text (abstract, introduction, or method description), so the paragraph above is
> inferred only from the title and should be **replaced** with real framing once
> the manuscript is available. Do not treat it as a verified description of the
> method.

NeurIPS 2026 Submission **#9856**. [Decision/acceptance status — fill in once known.]

{{< figure src="figures/teaser.png" alt="[TEASER FIGURE PLACEHOLDER] Paste the paper's Figure 1 / teaser figure here." caption="<span class=\"figure-number\">Figure 1: </span>**[PLACEHOLDER]** Replace with the paper's teaser figure and real caption text." width="100%" >}}

---

## Toy-Example Demonstrations {#toy-examples}

A short video and a live interactive version illustrate the velocity-mismatch
mechanism on 2D toy data — a flow-matching model trained only on normal data,
run toward a real data point and an off-manifold point from the same starting
noise draws. Solid arrows show the model's predicted velocity; dashed lines
show the true heading. On the normal target they track each other; on the
off-manifold target they visibly diverge, and that growing disagreement is
the anomaly signal.

{{< video src="figures/flow_mismatching_demo.mp4" caption="<span class=\"figure-number\">Video 1: </span>Predicted-vs-true velocity mismatch over time for a normal-target vs. off-manifold-target flow (two panels), with a cumulative mismatch-score comparison and an end-of-loop anomaly-score landscape reveal." width="100%" max_width="980px" >}}

**Try it yourself** — play/pause, scrub through time, and switch between a 3-cluster
mixture (the video above) and a half-moon manifold with a genuinely near-manifold
anomaly (a harder, more subtle detection case than an off-manifold gap point):

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

---

## Motivation {#motivation}

> **[MOTIVATION — PLACEHOLDER.]** Paste or paraphrase the paper's introduction /
> motivation here: why velocity discrepancies in flow matching models are a
> useful anomaly signal, what existing unsupervised AD methods miss, etc.

---

## Method: Flow Mismatching {#method}

> **[METHOD — PLACEHOLDER.]** Describe the method: how the velocity field is
> learned, how the "true"/expected velocity is defined for a query sample, how
> the mismatch score is computed and aggregated into an anomaly score, and any
> theoretical guarantees (e.g. connections to Tweedie's formula / posterior
> means, as referenced by the in-progress toy demo above).

{{< figure src="figures/method.png" alt="[METHOD FIGURE PLACEHOLDER] Paste the paper's method/architecture figure here." caption="<span class=\"figure-number\">Figure 2: </span>**[PLACEHOLDER]** Replace with the paper's method diagram and real caption." width="90%" >}}

---

## Results {#results}

> **[RESULTS — PLACEHOLDER.]** Paste the paper's quantitative results (benchmarks,
> datasets, AUROC/AUPRC or other metrics, baselines compared against) once the
> manuscript is accessible. Do not fabricate numbers.

{{< figure src="figures/results_table.png" alt="[RESULTS FIGURE/TABLE PLACEHOLDER] Paste the paper's results table/figure here." caption="<span class=\"figure-number\">Table 1 / Figure 3: </span>**[PLACEHOLDER]** Replace with the paper's real results table or figure and caption." width="90%" >}}

{{< figure src="figures/ablation.png" alt="[ABLATION FIGURE PLACEHOLDER, if applicable]" caption="<span class=\"figure-number\">Figure 4: </span>**[PLACEHOLDER, if applicable]** Replace with an ablation figure if the paper has one, or delete this block." width="90%" >}}

---

## Key Contributions {#key-ideas}

- **[CONTRIBUTION 1 — PLACEHOLDER]**
- **[CONTRIBUTION 2 — PLACEHOLDER]**
- **[CONTRIBUTION 3 — PLACEHOLDER]**

---

## Resources {#resources}

- **Paper:** [PLACEHOLDER — arXiv / OpenReview link once available]
- **Code:** [PLACEHOLDER — public repo link once available]
- **Venue:** NeurIPS 2026, Submission #9856

---

## BibTeX {#bibtex}

```bibtex
@inproceedings{yan2026flowmismatching,
  title     = {Flow Mismatching: Unsupervised Anomaly Detection via Velocity Discrepancies in Flow Matching Models},
  author    = {Yan, Hao},  % [CONFIRM FULL AUTHOR LIST AND ORDER]
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2026},
  note      = {Submission 9856}  % [UPDATE once accepted / camera-ready details known]
}
```

---

## Caveats / what this draft could not verify {#caveats}

This page was built from the PCBF project page's exact design and section
structure, but **no real paper content could be found or accessed**:

- No public or private GitHub repo under `hyan46` matched this paper by name
  ("flow", "mismatch", "9856"); `FlowMismatchingDemo` (private) contains only
  toy visualization scripts, not the manuscript.
- An attempt to clone the paper's Overleaf project
  (`git.overleaf.com/69f3a2a4db3f9d1010cea336`) was **blocked by a security
  check** in this session (flagged as exfiltration scouting) before any
  credential prompt or content was seen — this draft has **zero paper text**,
  not a redacted or partial version of it.
- No abstract, author list beyond "Hao Yan", arXiv/OpenReview link, figures, or
  bibtex fields beyond the title/venue/submission number were available from
  any source this draft was permitted to use.
