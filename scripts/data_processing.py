import chardet
from collections import defaultdict


if __name__ == "__main__":

    # case

    for i in range(1, 116):
        file_name = str(i)
        while len(file_name) != 4:
            file_name = "0" + file_name

        file_name_case = "A" + file_name + ".txt"
        file_name_question = "C" + file_name + ".txt"
        file_name_answer = "D" + file_name + ".txt"

        with open("../data/original_data/case/" + file_name_case, "rb") as f:
            encoding = chardet.detect(f.read())["encoding"]

        print("*"*50)
        print(i)

        single = {
            "case": "",
            "question": [],
            "answer": []
        }

        try:
            with open("../data/original_data/case/" + file_name_case, encoding=encoding) as f:
                for line in f.readlines():
                    single["case"] += line.strip()
        except Exception as e:
            with open("../data/original_data/case/" + file_name_case, encoding="gbk") as f:
                for line in f.readlines():
                    single["case"] += line.strip()

        with open("../data/original_data/question/" + file_name_question, encoding="GB2312") as f:
            for line in f.readlines():
                line = line.strip().split(".")[-1]
                line = line.split("系数")[0]
                single["question"].append(line)

        with open("../data/original_data/answer/" + file_name_answer, "rb") as f:
            encoding = chardet.detect(f.read())["encoding"]

        try:
            with open("../data/original_data/answer/" + file_name_answer, encoding=encoding) as f:
                for line in f.readlines():
                    line = line.strip().split(".")[-1]
                    line = line.replace("\t", "")
                    single["answer"].append(line)
        except Exception as e:
            with open("../data/original_data/answer/" + file_name_answer, encoding="gbk") as f:
                for line in f.readlines():
                    line = line.strip().split(".")[-1]
                    line = line.replace("\t", "")
                    single["answer"].append(line)

        # if i > 20:
        #     break

        print(len(single["case"]))
        print(len(single["question"]))
        print(len(single["answer"]))


    # question
    # question = defaultdict(int)
    # for i in range(1, 116):
    #     file_name = str(i)
    #     while len(file_name) != 4:
    #         file_name = "0" + file_name
    #
    #     file_name = "C" + file_name + ".txt"
    #
    #     # with open("../data/original_data/question/"+file_name, "rb") as f:
    #     #     print(chardet.detect(f.read()))
    #
    #     with open("../data/original_data/question/"+file_name, encoding="GB2312") as f:
    #         for line in f.readlines():
    #             line = line.strip().split(".")[-1]
    #             line = line.split("系数")[0]
    #             question[line] += 1
    #
    # print(question)