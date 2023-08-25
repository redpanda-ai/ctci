# ctci

Serves as a training aid for **Cracking the Coding Interview, 6th Edition**.

Use the included ```environment.yml``` file to create a conda virtual environment

[![](http://img.youtube.com/vi/U8GumpZ9LMk/0.jpg)](http://www.youtube.com/watch?v=U8GumpZ9LMk "Random Interview Question Picker")

## Installation instructions

### Conda

* Install [conda](https://www.anaconda.com/download#downloads) for the operating system you will use.
* Clone this repository
  * `git clone https://github.com/redpanda-ai/ctci.git`
* Change directories into the newly cloned repository
  * `cd ctci`
* Create a conda environment from the included environment.yml file
  * `conda env create -f environment.yml`
* Activate the environment
  * `conda activate ctci`
* Confirm that everything works by issuing the the following command
  * `python problem_picker.py 5`

### Pipenv

Ensure you have `pipenv` installed :)

```sh
# Install all packages from Pipfile
pipenv install

# Spawn a shell within the virtualenv
pipenv shell

# And you're off to the races!
python problem_picker.py
usage: problem_picker.py [-h] time_for_problem
problem_picker.py: error: the following arguments are required: time_for_problem
```

Alternatively, to run it:

```sh
pipenv run problem_picker.py
```
