# MBAM-RESP
Manifold Boundary Approximation Method for Heterotrophic Soil Respiration Assays

The code was adapted from https://github.com/gbohner/MBAM and updated to be compatible with the [Julia v0.6.4] (https://julialang.org/downloads/oldreleases.html) release.

The model definitions of the heterotropic respiration model by Wang et al. 2015, PLoS ONE 9(2): e89252.
https://doi:10.1371/journal.pone.0089252 are in the *BK_functions* subfolder. The *bk_setup_script* sets up the base parameters and the time grid to evaluate over. The *BK_Functions* notebook contains the model evaluation functions and the reduced functions that are iteratively found by the MBAM method.

The main files are in the *Figures* folder:

* *run_Simulations* runs a synthetic noisy simualtion of respiration given some base parameters and then fits the available models of choice to the noisy data. With default settings this takes about 15 minutes. Best run from the Julia REPL by executing *sim_run.jl*.

* *run_MBAM* runs the MBAM model reductions. This takes approximately 45 minutes.

* The outputs of both are saved in the *Figures/results* folder

The *Figures/results* folder contains .jld results files. These are translated into .csv format by the *figure_data_v063* notebook and placed into the *Figures/CSV* folder

The *PythonPlotting* folder contains the code to reproduce all figures from csv files in chapter x of my thesis.



