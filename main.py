
def read_data_from_the_file(file_name):
    file_info = []
    with open(file_name) as file:
        for line in file:
            line = line.replace("\n", "")
            file_info.append(line)

    return file_info


def write_data_into_file(file_name, info_to_write):
    file = open(file_name, "w")
    file.truncate()
    for line in info_to_write:
        file.write(line)
    file.close()


def check_same_info_in_lists(list1, list2):
    same_info = []
    for elem in list1:
        if elem in list2:
            same_info.append(elem)
    return same_info


def check_diff_info_in_lists(list1, list2):
    diff_info = []
    for elem in list1:
        if elem not in list2:
            diff_info.append(elem)
    return diff_info

def main(file1_name, file2_name):
    print("Hello world")


if __name__ == '__main__':
    main("file1.txt", "file2.txt")