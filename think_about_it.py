import pandas as pd


def get_questions_df(file_name):
    df = pd.read_csv(file_name, sep="\t")
    return df


if __name__ == "__main__":
    print("Set up a simple CLI to offer hints, and throw up a timer.")
    df = get_questions_df("./data/two.tsv")
    new_df = df.sample(n=1)
    q = list(new_df["Question"])[0]
    t = list(new_df["Title"])[0]
    print(f"Title: {t}\n{q}")
