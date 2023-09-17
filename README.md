## What is this tool?

This tool serves as a training aid for those wanting to grab high quality coding interview questions for study. The random pratice questions come from Gayle Laakmann's book, [**Cracking the Coding Interview, 6th Edition**](http://shortn/_y6ydorMcDP), which I highly recommend that you purchase first, since it offers so much more than this tool.

## Demo Reel
This tool operates from the command line, and should work on Windows, Mac OSX, and Linux. 

Here is an embedded YouTube video of it in action:


[![](http://img.youtube.com/vi/U8GumpZ9LMk/0.jpg)](http://www.youtube.com/watch?v=U8GumpZ9LMk "Random Interview Question Picker")

## Installation instructions

1. Ensure you have `pipenv` installed. A comprehensive guide for installing Pipenv can be found [here](https://pipenv.pypa.io/en/latest/installation/).

2. Open a terminal and enter the following commands in order.
   
3. Enter this command to install all packages from Pipfile
```sh
pipenv install
```

4. Enter this command to spawn a shell within the virtualenv
```sh
pipenv shell
```

5. Enter this command to confirm that your installation succeeded, by issuing the following command
```sh
python problem_picker.py
```
If everything worked you should get a **usage** error similar to this
```sh
usage: problem_picker.py [-h] time_for_problem
problem_picker.py: error: the following arguments are required: time_for_problem
```

## Still not working? Maybe we can help
If something failed along the way, please confirm that you followed all instructions precisely. Also, feel free to file a bug with all of the relevant details, including which operating system, shell, and outputs you received from each command. Thanks!
