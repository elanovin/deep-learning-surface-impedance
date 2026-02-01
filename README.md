# Deep Learning–Based Surface Impedance Modeling (PEC-backed Multilayers)

Deep learning surrogate model for predicting the **complex surface impedance** of **PEC-backed multilayer dielectric coatings**.

The model learns a mapping from material and geometric parameters (e.g., permittivity, conductivity, thicknesses, incidence angle) to surface impedance using a numerically stable real-valued target representation:
- `log10(|Z|)`, `cos(angle(Z))`, `sin(angle(Z))`

## What’s included
- Neural architectures for:
  - **2-layer lossy** coatings
  - **3-layer lossless** coatings
- Stable target encoding and impedance reconstruction
- Inference examples (notebooks) that run without private datasets

## Repository structure
- `src/models/` – model definitions (TensorFlow/Keras)
- `src/training/` – training scripts (expect external/private datasets)
- `src/inference/` – inference scripts
- `src/utils/` – target encoding & reconstruction utilities
- `examples/` – inference-only notebooks
- `docs/` – short theory notes and project scope

## Notes on data
The datasets used for training are not publicly released. Any scripts that expect data will clearly indicate required inputs and file formats.

## License
MIT
