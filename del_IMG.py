import os

# 原文件名和新文件名
original_filename = '456.md'
new_filename = '去掉IMG段落.md'

# 检查原文件是否存在
if not os.path.isfile(original_filename):
    print(f"文件 {original_filename} 不存在。")
    exit(1)

# 读取原文件内容
with open(original_filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 过滤掉包含 'IMG' 的段落
filtered_lines = [line for line in lines if 'IMG' not in line]

# 将过滤后的内容写入新文件
with open(new_filename, 'w', encoding='utf-8') as file:
    file.writelines(filtered_lines)

print(f"已将处理后的内容保存为 {new_filename} 文件。")
