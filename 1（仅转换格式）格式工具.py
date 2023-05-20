import os

# 获取目标目录中所有txt文件的文件名
file_list = []
for file in os.listdir("."):
    if file.endswith(".txt"):
        file_list.append(file)

# 针对每个文件逐行处理
for file_name in file_list:
    new_lines = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            # 如果行不包含[或]字符，则进行复制粘贴并加入分号
            if "[" not in line and "]" not in line:
                new_lines.append(";" + line.strip() + "\n" + line.strip() + "\n\n")
            # 否则保留该行不进行处理
            else:
                new_lines.append(line)
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(new_lines)
