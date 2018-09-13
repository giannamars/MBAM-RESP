# MBAM-RESP
Manifold Boundary Approximation Method for Heterotrophic Soil Respiration Assays

This repository implements all code needed to reproduce the figures in chapter x of my dissertation.
The code was adapted from \url{https ://github.com/gbohner/MBAM} and updated to be compatible with the Julia v0.6.3 release.

The model definitions of the heterotropic respiration model by Wang et al. 2015, PLoS ONE 9(2): e89252.
doi:10.1371/journal.pone.0089252 are in the BK_functions subfolder. The setup script sets up the base parameters and the measurement grid to evaluate over. The notebook contains the model evaluation functions and the reduced functions that are iteratively found by the MBAM method.

All results are found in the Figures subfolder. The results folder contains .jld results files. These are translated into .csv format by the figure_data_v063 notebook
