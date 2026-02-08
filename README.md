# Deep Learning–Based Surface Impedance Modeling (PEC-backed Multilayers)

This repository provides a **pre-publication, inference-focused showcase**
for a deep learning approach to modeling the **complex surface impedance**
of **PEC-backed multilayer dielectric coatings**.

The core idea is a numerically stable real-valued target representation:
- `log10(|Z|)`
- `cos(angle(Z))`
- `sin(angle(Z))`

which avoids phase discontinuities while preserving full complex impedance
information.

---

## Repository scope (pre-publication)

This repository is intentionally **limited in scope**.

It is designed to document the **methodology and representation strategy**
used in the associated journal manuscript, without releasing proprietary
datasets or full training pipelines prior to publication.

---

## What is included
- Stable impedance target encoding and reconstruction utilities
- Inference-related helper functions
- Selected figures from **2-layer lossless and lossy cases** used in the paper

---

## Repository structure
- `src/`
  - `impedance_encoding.py` – target encoding and complex impedance reconstruction
  - `inference_utils.py` – inference-side reconstruction helpers
- `figures/paper_2layer/` – selected paper figures (2-layer cases)
- `data/` – placeholder with data availability notes

---

## License
MIT
