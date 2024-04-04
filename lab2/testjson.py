import json
import difflib

def find_json_differences(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    diff = list(difflib.ndiff(json.dumps(data1, indent=2).splitlines(), json.dumps(data2, indent=2).splitlines()))

    for line in diff:
        if line.startswith('+') or line.startswith('-'):
            print(line)

# 指定要比较的两个 JSON 文件路径
file1 = 'researchers.json'
file2 = 'test.json'

find_json_differences(file1, file2)
