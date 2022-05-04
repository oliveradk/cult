# AUTOGENERATED! DO NOT EDIT! File to edit: 00b_core.utils.ipynb (unless otherwise specified).

__all__ = ['rec_likelihood', 'kl_div_stdnorm', 'euclidean', 'show', 'show_batch', 'disable_gradient', 'enable_gradient',
           'save_model', 'load_model']

# Cell
import torch
from torch import nn
import torch.nn.functional as F
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from ..config import PARAM_PATH
import os

# Cell
def rec_likelihood(x, x_rec):
    """Returns element wise reconstruction loss across batch"""
    return F.binary_cross_entropy(x_rec, x, reduction='none').flatten(start_dim=1).sum(dim=1)

# Cell
def kl_div_stdnorm(mu, logvar):
    """Returns element wise KL Divergence across batch"""
    return .5 * torch.sum(-(1 + logvar) + logvar.exp() + mu.pow(2), dim=1)#torch.mean(0.5 * (logvar.exp() + mu.pow(2) - 1) - logvar) #NOTE: this might be off, other implementations scale logvar too #-.5 * torch.mean(1 + logvar - mu.pow(2) - logvar.exp()) #

# Cell
def euclidean(x_1, x_2):
    return (x_1-x_2).pow(2).sum(1).sqrt()

# Cell
def show(imgs):
    """
    Plots list of images
    """
    if not isinstance(imgs, list):
        imgs = [imgs]
    fix, axs = plt.subplots(ncols=len(imgs), squeeze=False)
    for i, img in enumerate(imgs):
        img = img.detach()
        img = torchvision.transforms.functional.to_pil_image(img)
        axs[0, i].imshow(np.asarray(img))
        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])

# Cell
def show_batch(batch: torch.Tensor):
    """
    Shows 4D batch of tensors
    """
    grid = torchvision.utils.make_grid(batch)
    show(grid)

# Cell
def disable_gradient(model: nn.Module):
    for layer in model.children():
        layer.requires_grad_(False)

# Cell
def enable_gradient(model: nn.Module):
    for layer in model.children():
        layer.requires_grad_(True)

# Cell
def save_model(model, path):
     torch.save(model.state_dict(), os.path.join(PARAM_PATH, path))

# Cell
def load_model(model, path):
    model.load_state_dict(torch.load(os.path.join(PARAM_PATH, path)))