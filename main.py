
def read_data_from_the_file(file_path):
    file_info = []
    with open(file_path) as file:
        for line in file:
            file_info.append(line)

    return file_info


def main(file1_path, file2_path):
    print("Hello world")


if __name__ == '__main__':
    main("sjad", "sdjasdk")