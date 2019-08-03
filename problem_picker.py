import pandas as pd
import os
import time
import sys
from termcolor import colored, cprint


def get_questions_df(file_name):
    df = pd.read_csv(file_name, sep="\t")
    return df


def get_all_questions(directory_path):
    dfs = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".tsv"):
            path_to_file = f"{directory_path}/{filename}"
            print(f"Adding {path_to_file}")
            dfs.append(get_questions_df(path_to_file))

    return pd.concat(dfs, sort=False)


if __name__ == "__main__":
    print("Set up a simple CLI to pick a random question, and throw up a timer.")
    df = get_all_questions("./data")
    new_df = df.sample(n=1)
    q = list(new_df["Question"])[0]
    t = list(new_df["Title"])[0]
    cprint(f"Title:", "green")
    print(f"\t{t}")
    cprint(f"Question:", "yellow")
    print(f"\t{q}")

    time_for_problem = 10
    cprint("Time Remaining", 'red')
    for remaining in range(time_for_problem, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"\t{remaining:4d} seconds.")
        sys.stdout.flush()
        time.sleep(1)
