import argparse
import os
import pandas as pd
import time

from tqdm import tqdm
from termcolor import cprint


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
    parser = argparse.ArgumentParser()
    parser.add_argument("time_for_problem", help="Number of seconds for the problem", type=int)
    args = parser.parse_args()

    df = get_all_questions("./data")
    input(f"You will have {args.time_for_problem} seconds to answer the question, press ENTER to start")
    new_df = df.sample(n=1)
    q = list(new_df["Question"])[0]
    t = list(new_df["Title"])[0]
    cprint(f"Title:", "green")
    print(f"\t{t}")
    cprint(f"Question:", "yellow")
    print(f"\t{q}")

    cprint("Time Remaining", 'red')

    for remaining in tqdm(range(args.time_for_problem)):
        time.sleep(1)

    print("\nTime's up!")
