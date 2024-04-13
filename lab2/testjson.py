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
    """
    +表示该行存在于file2中，但不存在于file1中。
    -表示该行存在于file1中，但不存在于file2中。
    空格表示该行在两个文本序列中是相同的。
    ?表示行存在于两个文本序列中，但具体差异不同于上述三种情况，通常表示不可打印的字符等。
    """

# 指定要比较的两个 JSON 文件路径
file1 = 'researchers.json'
file2 = r'F:\Desktop\researchers.json'

find_json_differences(file1, file2)

find_json_differences(file1, file2)