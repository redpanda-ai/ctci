## What is this tool?

This tool serves as a training aid for those wanting to grab high quality coding interview questions for study. The random pratice questions come from Gayle Laakmann's book, [**Cracking the Coding Interview, 6th Edition**](http://shortn/_y6ydorMcDP), which I highly recommend that you purchase first, since it offers so much more than this tool.

## Demo Reel
This tool operates from the command line, and should work on Windows, Mac OSX, and Linux. 

Click the image below to watch a short YouTube video of the tool in action:

[![](http://img.youtube.com/vi/U8GumpZ9LMk/0.jpg)](http://www.youtube.com/watch?v=U8GumpZ9LMk "Random Interview Question Picker")

## Installing Instructions

### Part 1 - Installing Pipenv

1. Install `pipenv` on your system using by following their [official documentation](https://pipenv.pypa.io/en/latest/installation/).


### Part 2 - Use the terminal to install this software using git and pipenv

2. Open a terminal and enter the following commands in order.
 
3. Clone this repository to get the latest version of the tool
   ```sh
   git clone https://github.com/redpanda-ai/ctci.git
   ```
4. Change your working directory to where the git repository was cloned.
   ```sh
   cd ctci
   ```  
5. Enter this command to install all packages from Pipfile
```sh
pipenv install
```

6. Enter this command to spawn a shell within the virtualenv
```sh
pipenv shell
```

### Part 3 - Confirm your installation

7. Enter this command to confirm that your installation succeeded, by issuing the following command
```sh
python problem_picker.py
```
It may help to see what a successful installation looks like, so I have linked [this](https://gist.github.com/redpanda-ai/0c189909ed021dd86d6a4e2e9547682f) sample installation.

## Still not working? Maybe we can help
Maybe we can help. First, see if your issue is already on our [issues](https://github.com/redpanda-ai/ctci/issues) list. If not, please feel free to file a bug and include the terminal output from your installation attempt, preferably as a gist, along with any other relevant details (e.g., Operating System, software version, etc.).
