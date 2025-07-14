import os
import re

def fix_last_typo():
    """
    Fixes one specific remaining typo in the categories.
    """
    directory_path = '.'
    file_to_fix = 'manage-animal-shelter-strategy-resource-game.md' # שם הקובץ הספציפי
    path_to_file = os.path.join(directory_path, file_to_fix)

    old_category_line = 'category: ניהול ומלכ\\'
    new_category_line = 'category: "ניהול מלכ\"רים"'

    print(f"מנסה לתקן את הקטגוריה בקובץ: {file_to_fix}")

    try:
        if os.path.exists(path_to_file):
            with open(path_to_file, 'r', encoding='utf-8') as f:
                content = f.read()

            if old_category_line in content:
                new_content = content.replace(old_category_line, new_category_line)
                
                with open(path_to_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✅ הקובץ '{file_to_fix}' תוקן בהצלחה!")
                print(f"הקטגוריה שונתה מ: 'ניהול ומלכ\\' -> ל: 'ניהול מלכ\"רים'")
            else:
                print("INFO: הקטגוריה הישנה לא נמצאה בקובץ, ייתכן שכבר תוקן.")
        else:
            print(f"ERROR: הקובץ '{file_to_fix}' לא נמצא.")

    except Exception as e:
        print(f"❌ שגיאה בעיבוד הקובץ: {e}")

    print("\nהתהליך הסתיים.")


if __name__ == "__main__":
    fix_last_typo()