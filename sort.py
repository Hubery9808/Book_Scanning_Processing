import re

# 定义页码和标记
page_number = 1
mark = '页码加标'

# 生成新文件名
new_file_name = f'{mark}.md'

# 读取文件内容
with open('123.md', 'r', encoding='utf-8') as file:
    content = file.read()

# 定义一个正则表达式来匹配包含连续三位数字的段落
pattern = re.compile(r'^(.*?\d{3}.*)$', re.MULTILINE)

# 定义一个函数来将匹配的段落转换为标题3格式
def replace_with_header(match):
    return f'### {match.group(1)}'

# 替换匹配的段落
updated_content = pattern.sub(replace_with_header, content)

# 在每个换行符后面再加一个换行符
updated_content_with_extra_newlines = re.sub(r'(\n)', r'\1\n', updated_content)

# 将更新后的内容写入新文件
with open(new_file_name, 'w', encoding='utf-8') as file:
    file.write(updated_content_with_extra_newlines)

print(f"更新完成，文件保存为 {new_file_name}。")
