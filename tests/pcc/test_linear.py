import torch

from torch_impl.linear import Linear


def test_linear_matches_torch_linear():
    torch.manual_seed(0)
    in_features = 8
    out_features = 4
    batch = 3

    reference = torch.nn.Linear(in_features, out_features, bias=True)
    custom = Linear(in_features, out_features, bias=True)
    custom.weight.data.copy_(reference.weight.data)
    custom.bias.data.copy_(reference.bias.data)

    inputs = torch.randn(batch, in_features)
    expected = reference(inputs)
    actual = custom(inputs)

    torch.testing.assert_close(actual, expected)


def test_linear_without_bias_matches_torch_linear():
    torch.manual_seed(1)
    in_features = 16
    out_features = 6

    reference = torch.nn.Linear(in_features, out_features, bias=False)
    custom = Linear(in_features, out_features, bias=False)
    custom.weight.data.copy_(reference.weight.data)

    inputs = torch.randn(2, in_features)
    expected = reference(inputs)
    actual = custom(inputs)

    torch.testing.assert_close(actual, expected)
