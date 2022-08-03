import csv



CSV_PATH = 'utilization.csv'

def open_txt(file_path):
    data_list = []
    with open(file_path, 'r') as file_in:
        for row in file_in:
            reader = csv.reader(file_in, delimiter=",")
            data_list.append(row)
    return data_list

print(open_txt(CSV_PATH))

def convert_data_to_dict(data):
    info = {
        "name": data [1],
        "utilization": data [2]
        }
    return info

def plot_utilization(dict):
    pass
