import json
import os.path
import sys


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as data_file:
            return json.load(data_file)
    else:
        return None


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    json_data = load_data(sys.argv[1])
    if json_data:
        pretty_print_json(json_data)
    else:
        print("Не удалось прочитать файл")
