import json
import difflib

def find_json_differences(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    diff = list(difflib.ndiff(json.dumps(data1, indent=2).splitlines(), json.dumps(data2, indent=2).splitlines()))

    for line in diff:
        print(line)
    """
    +表示该行存在于file2中，但不存在于file1中。
    -表示该行存在于file1中，但不存在于file2中。
    ?表示两个文件在这一行有微小的差异，例如空格或者标点符号的不同。
    """

# 指定要比较的两个 JSON 文件路径
file1 = 'researchers.json'
file2 = 'researchers(1).json'
#file2 = r'F:\Desktop\researchers.json'，r表示原始字符串，不会对字符串中的特殊字符进行转义
find_json_differences(file1, file2)