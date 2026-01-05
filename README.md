# TT Model Bringup

This repo tracks bring-up work for Tenstorrent model implementations and validation.

## Repository layout

- `demo/`: Validation on a small dataset and performance sheet generation using the Tracey command.
- `tests/`: PCC tests for each module and the whole model, plus perf tests for traced modules on a single device and a mesh of devices.
- `torch_impl/`: Reference implementation in PyTorch.
- `ttnn_impl/`: TTNN implementation used for bring-up.

## Notes

- The AGENTS.md section in this repo is adapted from the Facet project: https://github.com/facet-rs/facet/blob/main/AGENTS.md

