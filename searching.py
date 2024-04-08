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

def main():
    pass


if __name__ == '__main__':
    main()