import json

data_file = "data.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

data = load_data()
target_key = 513153492165197835
str_key = str(target_key)

if str_key in data:
    id_data = str_key
    print("指定したキーが見つかりました！")
    print(id_data)
    # print(data[id_data[1]])
    value = data["513153492165197835"]["\u30a2\u30bf\u30c3\u30ab\u30fc"]
    print(value)
else:
    print("指定したキーは見つかりませんでした。")