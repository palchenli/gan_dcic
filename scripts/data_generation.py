import pandas as pd
import random


if __name__ == "__main__":
    df = pd.read_csv("../data/all_data.csv", sep="|")
    print(df.shape)

    out = []
    for row in df.iterrows():
        row = row[1]

        case = row["case"]
        questions = row["question"]
        answers = row["answer"]

        for i in range(len(questions)):
            input_tmp = "你是一个医生，请根据患者的病例回答患者的问题。患者的病例为：{}，患者的问题为：{}".format(case, questions[i])
            output_tmp = answers[i]
            tmp = {
                "content": input_tmp,
                "summary": output_tmp
            }
            out.append(tmp)

    random.shuffle(out)

    f = open("../data/train_data.json", "w")
    for tmp in out:
        f.write(str(tmp)+"\n")
    f.close()
