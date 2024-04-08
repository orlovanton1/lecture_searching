import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    file_name = "sequential.json"
    with open (file_name, "r") as file_obj:
        data = json.load(file_obj)
        if field in data.keys():
            return data[field]
        else:
            return None

def linear_search(sequence, search_number):
    list_of_times = []
    for index, number in enumerate(sequence):
        if number == search_number:
            list_of_times.append(index)
    return {"position": list_of_times, "count": len(list_of_times)}

def pattern_search(sequence, search_seq):
    list_of_position = []
    pattern_lenght = len(search_seq)
    number_of_operations = 0
    for position in range(len(sequence)-pattern_lenght):
        is_same = True
        for subins in range(len(search_seq)):
            number_of_operations = number_of_operations + 1
            if sequence[position+subins] == search_seq[subind]:
                is_same = is_same and True
            else:
                is_same = is_same and False
        if is_same:
            list_of_position.append(position+pattern_lenght // 2)
    print(number_of_operations)
    return {"position": list_of_position, "count": len(list_of_position)}

def main():
    pass


if __name__ == '__main__':
    main()