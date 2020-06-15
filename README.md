# Deep-Learning-over-25-million-cinema-tickects
Master Thesis: Deep Learning over 25 million cinema tickets

The source code to my master thesis can be found in this repository.

* [Preprocessing and aggregation](notebooks/01_preprocess/)  
  * These files are the ones used for the preprocessing and for combining the data from the different sources and to calculate extra features
* [Analysis](notebooks/02_analysis/) 
  * In this folder you will find many files, each file checks only the one statistic that its name is related to
* [Neural Network](notebooks/03_neural_nets/)  
  * [Random Fores](notebooks/03_neural_nets/baseline_random_forest.ipynb) is the baseline model we used
  * [TabularModel Default](notebooks/03_neural_nets/tabular_model_default.ipynb) is the TabularModel with default values.
  * [TabularModel tuning](notebooks/03_neural_nets/tabular_model_experimental.ipynb) this file was used for hyperparamer tuning
* [Scheduler](notebooks/04_application/)
  * Contains the scheduler that suggest an alternate movie schedule
