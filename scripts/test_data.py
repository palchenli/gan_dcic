import chardet
import pandas as pd
from collections import defaultdict


if __name__ == "__main__":
    file_name_case = "E0001.txt"
    file_name_question = "F0001.txt"
    single = {
        "case": "",
        "question": [],
        "answer": []
    }

    with open("../data/test_data/case/" + file_name_case, "rb") as f:
        encoding = chardet.detect(f.read())["encoding"]

    try:
        with open("../data/test_data/case/" + file_name_case, encoding=encoding) as f:
            for line in f.readlines():
                single["case"] += (line.strip() + ";")
    except Exception as e:
        with open("../data/test_data/case/" + file_name_case, encoding="gbk") as f:
            for line in f.readlines():
                single["case"] += (line.strip() + ";")

    with open("../data/test_data/question/" + file_name_question, encoding="GB2312") as f:
        for line in f.readlines():
            line = line.strip().split(".")[-1]
            line = line.split("系数")[0]
            single["question"].append(line)

    input_tmp = "你是一个医生，请根据患者的病例回答患者的问题。患者的病例为：{}，患者的问题为：{}".format(single["case"], single["question"][0])

    print(input_tmp)