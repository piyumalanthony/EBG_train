# Educated Bootstrap Guesser Training

## Description

This repository contains the data and code used to train and evaluate EBG.


## Data
```
├── data
│   └── comparison_results => contains all cpu/wall-clock time comparison data
│       ├── cpu_times
│       │   └── test_times.csv
│       └── wall_clock_times 
│           ├── benchmark_ebg.csv
│           ├── benchmark_rapid_bootstrap.csv
│           ├── benchmark_raxmlng_ml_searches.csv
│           ├── benchmark_sbs.csv
│           └── benchmark_times_ufboot2.csv
├─────── models => final models of EBG
├─────── processed => computed features, bootstrap targets and training dataset
│        ├── features
│        ├── final
│        └── target 
└─────── raw => all datasets (MSA, tree, model file and bootstrap results) as .tar.gz-file      
```
## Usage Example
A simple command line call of EBG looks like this:
```
ebg -msa /test/example.fasta -tree /test/example.bestTree -model /test/example.bestModel -t b -o test 
```
This command will use the MSA in fasta format, and the best tree inferred with RAxML-NG and the model.
By selecting ```-t b```(oth) EBG will ouput the bootstrap predictions as well as the probabilities for exceeding different bootstrap thresholds (70, 75, 80, 85). 
The results will be stored in a folder called test.
### References
* A. M. Kozlov, D. Darriba, T. Flouri, B. Morel, and A. Stamatakis (2019) 
**RAxML-NG: a fast, scalable and user-friendly tool for maximum likelihood phylogenetic inference** 
*Bioinformatics*, 35(21): 4453–4455. 
[https://doi.org/10.1093/bioinformatics/btz305](https://doi.org/10.1093/bioinformatics/btz305)
