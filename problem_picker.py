import argparse
import os
import pandas as pd
import time

from tqdm import tqdm
from termcolor import cprint


def get_questions_df(file_name):
    """Grabs all questions in a single TSV file"""
    df = pd.read_csv(file_name, sep="\t")
    return df


def get_all_questions(directory_path):
    """Grabs all questions from a directory path and creates a big dataframe"""
    dfs = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".tsv"):
            path_to_file = f"{directory_path}/{filename}"
            print(f"Adding {path_to_file}")
            dfs.append(get_questions_df(path_to_file))

    return pd.concat(dfs, sort=False)


if __name__ == "__main__":
    """This script picks a random question and presents it to the user to solve in a limited amout of time"""
    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("time_for_problem", help="Number of seconds for the problem", type=int)
    args = parser.parse_args()

    # Collect questions from data directory
    df = get_all_questions("./data")

    # Prompt user to start
    input(f"You will have {args.time_for_problem} seconds to answer the question, press ENTER to start")

    # Display a random question
    new_df = df.sample(n=1)
    q = list(new_df["Question"])[0]
    t = list(new_df["Title"])[0]
    cprint(f"Title:", "green")
    print(f"\t{t}")
    cprint(f"Question:", "yellow")
    print(f"\t{q}")

    cprint("Time Remaining", 'red')

    # Show a timer
    for remaining in tqdm(range(args.time_for_problem)):
        time.sleep(1)

    # Sound an audible timer for when the time is up.
    print("\nTime's up!")
    for i in range(5):
        print("\007")
        time.sleep(0.25)
