import pandas as pd
import os


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
    print("Set up a simple CLI to offer hints, and throw up a timer.")
    df = get_all_questions("./data")
    new_df = df.sample(n=1)
    q = list(new_df["Question"])[0]
    t = list(new_df["Title"])[0]
    print(f"Title:\n\t{t}\nQuestion:\n\t{q}")
