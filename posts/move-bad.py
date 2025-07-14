import os
import shutil
import yaml

folder_path = '.'
bad_dir = 'no-good'

if not os.path.exists(bad_dir):
    os.makedirs(bad_dir)

for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # מחפש frontmatter בפתיחה וסגירה
        if lines and lines[0].strip() == '---':
            # מחפש איפה ה־--- הסוגר
            close_idx = None
            for i, l in enumerate(lines[1:], 1):
                if l.strip() == '---':
                    close_idx = i
                    break
            if close_idx:
                yaml_str = ''.join(lines[1:close_idx])
                try:
                    yaml.safe_load(yaml_str)
                    continue  # YAML תקין, ממשיך הלאה
                except Exception as e:
                    print(f"YAML לא תקין: {filename}: {e}")
            else:
                print(f"חסרה סגירת --- בקובץ: {filename}")
        else:
            # קבצים בלי פתיחת --- פשוט מדלגים, או שמועברים גם הם ל-no-good אם אתה רוצה
            continue

        # אם הגענו לפה – הקובץ לא תקין, מעבירים
        shutil.move(file_path, os.path.join(bad_dir, filename))
        print(f"מעביר ל-no-good: {filename}")
