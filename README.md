# ctci

Serves as a training aid for **Cracking the Coding Interview, 6th Edition**.

Use the included ```environment.yml``` file to create a conda virtual environment

[![](http://img.youtube.com/vi/U8GumpZ9LMk/0.jpg)](http://www.youtube.com/watch?v=U8GumpZ9LMk "Random Interview Question Picker")

# Installation instructions

1. Install [conda](https://www.anaconda.com/download#downloads) for the operating system you will use.
1. Clone this repository
  * `git clone https://github.com/redpanda-ai/ctci.git`
1. Change directories into the newly cloned repository
  * `cd ctci`
1. Create a conda environment from the included environment.yml file
  * `conda env create -f environment.yml`
1. Activate the environment
  * `conda activate ctci`
1. Confirm that it works with the following command
  * `python problem_picker.py 5`
