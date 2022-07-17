# CULT: Continual Unsupervised Learning with aTpyicality-based Evironmental Selection



Inspired by [Aachille et al. 2018](https://arxiv.org/abs/1808.06508), we implement a simple continual learning framework with variational autoencoders and generative replay, where new environments are detected using the atypicality score of the latents, where atypicality is given by: 


$$\alpha = D_{KL}(\mathcal{N}(\bar{\mu}_{z}, \bar{\sigma}_z)||\mathcal{N}(0,1))$$



## Install

`pip install cult`

## Experiments

The experiment(s) are run in `03a_experiments.cult_experiments.ipynb`
Result visualizations are produced in `04_visualize_data.ipynb`
