import chardet



if __name__ == "__main__":

    # question
    question = []
    for i in range(1, 116):
        file_name = str(i)
        while len(file_name) != 4:
            file_name = "0" + file_name

        file_name = "C" + file_name + ".txt"

        with open(file_name, "rb") as f:
            print(chardet.detect(f.read()))

        # with open("../data/original_data/question/"+file_name) as f:
        #     for line in f.readlines():
        #         print(line)