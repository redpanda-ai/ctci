import argparse
import os
import pandas as pd
import pyperclip
import sys
import time

from termcolor import cprint
from tqdm import tqdm


def main():
    """
    This script picks a random question and presents it to the user to
    solve in a limited amount of time
    """
    args = parse_arguments()

    # Collect questions from data directory
    df = get_all_questions("./data")

    # Prompt user to start
    time_seconds = get_time_in_seconds(args.time_for_problem)
    print(f"You will have {time_seconds} seconds to answer the question, good luck!")
    system_bell()

    new_df = display_random_question(df)
    display_timer(time_seconds)

    chapter = list(new_df["Major"])[0]
    question = list(new_df["Minor"])[0]
    print(f"\nThe program selected Chapter {chapter} Question {question}")


def get_time_in_seconds(time_minutes: int) -> int:
    """
    converts minutes to seconds
    """
    return time_minutes * 60


def copy_to_clipboard(title: str, question: str):
    """Copy the question as a doc-string into the system clipboard"""
    cprint(
        "Your question has been copied to your internal clipboard, you can now paste it into an editor.",
        "magenta",
    )
    pyperclip.copy(f'"""\nTitle:\n\t{title}\nQuestion:\n\t{question}\n"""\n\n')


def display_random_question(df: pd.DataFrame) -> pd.DataFrame:
    """Display a random question selected from the supplied data frame"""
    new_df = df.sample(n=1)
    question = list(new_df["Question"])[0]
    title = list(new_df["Title"])[0]
    cprint("Title:", "green")
    print(f"{title}\n")
    cprint("Question:", "yellow")
    print(f"{question}\n")
    copy_to_clipboard(title, question)

    return new_df


def display_timer(total_time_seconds: int):
    """Display a timer, that can be interrupted with CTRL + C"""
    cprint("You can press CTRL + C at any time to stop the timer", "blue")
    cprint("Elapsed Time", "red")
    keep_running = True
    try:
        while keep_running:
            for counter in tqdm(range(total_time_seconds)):
                time.sleep(1)

            # Sound an audible timer for when the time is up.
            keep_running = False
            for i in range(5):
                system_bell()
                time.sleep(0.25)
    except KeyboardInterrupt:
        system_bell()
        cprint("Processing keyboard interrupt.", "blue")

    if not keep_running:
        print("You ran out of time!")
    else:
        print(f"You finished with {total_time_seconds - counter} seconds remaining.")


def get_all_questions(directory_path: str):
    """Grabs all questions from a directory path and creates a big data frame"""
    dfs = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".tsv"):
            path_to_file = f"{directory_path}/{filename}"
            # print(f"Adding {path_to_file}")
            dfs.append(get_questions_df(path_to_file))

    df = pd.concat(dfs, sort=False)
    print(f"Loading {df.shape[0]} questions from {len(dfs)} files.")
    return df


def get_questions_df(file_name: str):
    """Grabs all questions in a single TSV file"""
    df = pd.read_csv(file_name, sep="\t")
    return df


def parse_arguments():
    """Parses all command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "time_for_problem", help="Integer number of minutes for the problem", type=int
    )
    return parser.parse_args()


def system_bell():
    """Make an audible tone"""
    sys.stdout.write("\007")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
