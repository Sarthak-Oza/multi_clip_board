import sys
import json
import clipboard

filename = "clipboard_data.json"


def save_data(data):
    with open(filename, mode="w") as f:
        json.dump(data, f)


def load_data():
    try:
        with open(filename, mode="r") as f:
            return json.load(f)
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    loaded_json_data = load_data()
    if command == "save":
        key = input("Enter key: ")
        loaded_json_data[key] = clipboard.paste()
        save_data(loaded_json_data)
        print("Saved to the file")
    elif command == "load":
        key = input("Enter key to copy to clipboard: ")
        if key in loaded_json_data:
            clipboard.copy(loaded_json_data[key])
            print("Copied to clipboard")
        else:
            raise Exception("Invalid Key!!")
    elif command == "list":
        if loaded_json_data:
            for key,value in loaded_json_data.items():
                print(f"{key} -> {value}")
        else:
            print("No data!")
    elif command == "delete":
        key = input("Enter key to delete: ")
        if key in loaded_json_data:
            del (loaded_json_data[key])
            save_data(loaded_json_data)
    else:
        print("Invalid command!")
else:
    raise Exception("Enter only one argument command!")
