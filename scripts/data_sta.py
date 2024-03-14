import pandas as pd
from collections import defaultdict, Counter



if __name__ == "__main__":
    df = pd.read_csv("../data/data.csv")

    question = []
    for row in df.iterrows():
        row = row[1]
        question += eval(row["question"])

    res = Counter(question)
    print(res)

