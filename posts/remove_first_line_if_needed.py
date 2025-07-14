import os
import sys

folder_path = sys.argv[1] if len(sys.argv) > 1 else '.'

for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if lines and not lines[0].strip().startswith('---'):
            if len(lines) > 1 and lines[1].strip().startswith('---'):
                lines = lines[1:]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
