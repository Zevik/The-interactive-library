import os

folder_path = '.'

for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # בדוק כמה שורות '---' יש ברצף בראש הקובץ
        idx = 0
        while idx < len(lines) and lines[idx].strip() == '---':
            idx += 1

        # אם יש יותר מאחת, השאר רק אחת
        if idx > 1:
            new_lines = ['---\n'] + lines[idx:]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f'Fixed: {filename}')
