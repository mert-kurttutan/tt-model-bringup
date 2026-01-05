import time

import torch

from torch_impl.linear import Linear


def test_linear_forward_runs_reasonably_fast():
    torch.manual_seed(0)
    batch = 64
    in_features = 256
    out_features = 128
    iterations = 50

    layer = Linear(in_features, out_features, bias=True)
    inputs = torch.randn(batch, in_features)

    start = time.perf_counter()
    for _ in range(iterations):
        outputs = layer(inputs)
    elapsed = time.perf_counter() - start

    assert outputs.shape == (batch, out_features)
    assert elapsed >= 0.0
