import os
import re

categories = set()

for filename in os.listdir('.'):
    if filename.endswith('.md') or filename.endswith('.txt'):
        with open(filename, encoding='utf-8') as f:
            for line in f:
                match = re.match(r'category:\s*"(.*?)"', line)
                if match:
                    categories.add(match.group(1))

print('כל הקטגוריות שמצאתי:')
for category in sorted(categories):
    print(category)
