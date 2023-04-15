dict_ = {
    "father": {
        "name": "jon",
        "age": 40
        },
    "mother": {"name": "mary",
    "age": 38
    }
}

import json

# json_ = json.dumps(dict_)

with open("dict_.json", "w") as f:
    # f.write(json_)
    json.dump(dict_, f)

for parent in dict_:
    print(f"{dict_['parent']['name']['age']}" and "{dict_['parent']['mother']['age']}")
