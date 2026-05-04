# Type: Binary, Text
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)

file_path = cur_dir + '/text_file.txt'
print(file_path)

# Read
# r : Read-only mode
# w : Write-only mode
# a : Append mode
# f = open('text_file.txt', 'r')
f = open(file_path, 'w')
f.write("123")
f.close()
# f = open('/Users/huen_oh/00_Developments/eunsung_git_tutorial/advanced/file_handling/text_file.txt', 'r')
f = open(file_path, 'r')
content = f.read()
print(content)
f.close()


# with open('text_file.txt', 'r') as f:
#     # content = f.read()
#     content = f.readlines()
#     print(content)