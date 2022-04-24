# AUTOGENERATED! DO NOT EDIT! File to edit: 03a_core.train.ipynb (unless otherwise specified).

__all__ = ['reconstruction_loss', 'kl_div_stdnorm', 'kl_div_target']

# Cell
import torch
from torch import nn
from torch.nn import functional as F
from ..config import DATA_PATH


# Cell
def reconstruction_loss(x, x_rec):
    return F.binary_cross_entropy(x_rec, x, reduce=True)

# Cell
def kl_div_stdnorm(mu, logvar):
    """Returns mean of KL Divergence across batch"""
    return torch.mean(0.5 * (logvar.exp() + mu.pow(2) - 1) - logvar) #NOTE: this might be off, other implementations scale logvar too

# Cell
def kl_div_target(mu, logvar, C=0, gamma=1):
    """Returns target loss: squared difference of mean kldivergence and target C scaled by gamma"""
    return gamma * ((kl_div_stdnorm(mu, logvar) - C).pow(2))