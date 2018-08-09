import json

numbers = [1,2,3,4]

#文件存入
filename = "namubers.json"
# with open(filename, "w") as f_obj:
#     json.dump(numbers, f_obj)

#文件获取

with open(filename) as f_obj:
    get_numbers = json.load(f_obj)
print(get_numbers)