import chardet
from collections import defaultdict


if __name__ == "__main__":

    # case

    for i in range(1, 116):
        file_name = str(i)
        while len(file_name) != 4:
            file_name = "0" + file_name

        file_name = "A" + file_name + ".txt"
        with open("../data/original_data/case/" + file_name, encoding="GB2312") as f:
            print("*"*50)
            for line in f.readlines():
                print(line)


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