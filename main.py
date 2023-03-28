
def read_data_from_the_file(file_name):
    file_info = []
    with open(file_name) as file:
        for line in file:
            file_info.append(line)

    return file_info


def write_data_into_file(file_name, info_to_write):
    file = open(file_name, "w")
    file.truncate()
    for line in info_to_write:
        file.write(line)
    file.close()


def check_sample_info_in_lists(list1, list2):
    sample_info = []
    for elem in list1:
        if elem in list2:
            sample_info.append(elem)
    return sample_info


def main(file1_name, file2_name):
    print(read_data_from_the_file(file1_name))
    print(read_data_from_the_file(file2_name))


if __name__ == '__main__':
    main("file1.txt", "file2.txt")