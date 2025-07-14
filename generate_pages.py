import google.generativeai as genai
import os
import re
from dotenv import load_dotenv
import time

# --- CONFIGURATION ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("שגיאה: לא נמצא מפתח API. ודא שיצרת קובץ .env עם המפתח שלך.")
    exit()

genai.configure(api_key=API_KEY)

TOPICS_FILE = "topics.txt"
OUTPUT_DIR = "posts"
PROCESSED_MARKER = "[DONE] "

PROMPT_TEMPLATE = """
[[[ הנחיה קריטית: עליך להחזיר אך ורק את גוף הקובץ המבוקש. הפלט שלך חייב להתחיל ישירות בשורה "---" ולסיים בסוף הקוד. אל תוסיף שום טקסט, הסבר, הערה, או סימון כמו "START OF FILE" או "```" מחוץ לגוף הקובץ. כל תו נוסף יהרוס את התהליך האוטומטי. ]]]

צור לי דף לימוד אינטראקטיבי בנושא **{topic}**.

הקובץ מיועד לאתר מבוסס Eleventy (SSG) ויש לשמור אותו עם סיומת .md.

## כללים מחמירים למבנה הקובץ:

### 1. Frontmatter (חובה)
בראש הקובץ, כתוב Frontmatter בפורמט YAML.
- הוא חייב להיות מוקף ב-`---` בתחילה ובסוף.
- הוא חייב להכיל **אך ורק** את 3 המפתחות הבאים: `title`, `category`, `tags`.
- **חובה קריטית:** עטוף את הערכים של `title` ו-`category` במירכאות כפולות (לדוגמה: `title: "שם הנושא"`).
- **חובה קריטית:** ברשימת ה-`tags`, **אסור** לכלול את התגית "post". התגית הזו מתווספת אוטומטית. כלול רק תגיות ספציפיות לנושא.

### 2. תוכן (Markdown)
מיד אחרי ה-`---` הסוגר של ה-Frontmatter, כתוב את התוכן בפורמט Markdown הכולל הסבר על הנושא ומטרת האפליקציה.

### 3. אפליקציה אינטראקטיבית (HTML/CSS/JS)
- ישירות אחרי טקסט ההסבר, הדבק את כל קוד האפליקציה המלא (HTML, CSS, JS) בקובץ אחד.
- **אסור להשתמש בשום קוד או משאב חיצוני.**
- עצב את האפליקציה בסגנון מודרני, נקי ורספונסיבי.

---
### דוגמת מבנה קובץ מושלם (עקוב אחריה במדויק):
---
title: "שימור תנע בהתנגשות"
category: "פיזיקה"
tags: [פיזיקה, תנע, התנגשות, שימור אנרגיה]
---

# שימור תנע: ריקוד הכוחות בהתנגשות

הסבר על הנושא...

<!-- כאן יופיע כל קוד ה-HTML+CSS+JS של האפליקציה -->
"""

def generate_filename(topic, model):
    """Asks the AI to generate a URL-friendly filename for the topic."""
    try:
        print(f"  -> יוצר שם קובץ באנגלית עבור '{topic}'...")
        prompt = f"Provide just one single URL-friendly, kebab-case English slug for the Hebrew topic: '{topic}'. Do not add any explanation or decoration. Example: for 'אפקט דופלר', return 'doppler-effect'."
        response = model.generate_content(prompt)
        
        slug = re.sub(r'[^a-z0-9-]', '', response.text.lower().strip())
        if slug:
            return f"{slug}.md"
        else:
            return f"{topic.replace(' ', '-')}.md"
    except Exception as e:
        print(f"  !! שגיאה ביצירת שם קובץ: {e}")
        return None

def generate_page_content(topic, model):
    """Generates the full page content for a given topic."""
    try:
        print(f"  -> יוצר תוכן עבור '{topic}'...")
        full_prompt = PROMPT_TEMPLATE.format(topic=topic)
        response = model.generate_content(full_prompt)
        # Clean the response from potential AI "noise"
        content = response.text.strip()
        if content.startswith("```markdown"):
            content = content.replace("```markdown", "", 1)
        if content.startswith("```"):
             content = content.replace("```", "", 1)
        if content.endswith("```"):
            content = content[:-3]
        return content.strip()
    except Exception as e:
        print(f"  !! שגיאה ביצירת תוכן: {e}")
        return None

def save_content_to_file(filename, content):
    """Saves the content to a file in the output directory."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"יצרתי תיקייה חדשה: '{OUTPUT_DIR}'")

    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✔ התוכן נשמר בהצלחה בקובץ: {filepath}")

def main():
    """Main function to run the script."""
    print("מתחיל את תהליך יצירת הדפים האוטומטי...")

    try:
        with open(TOPICS_FILE, 'r', encoding='utf-8') as f:
            topics = f.readlines()
    except FileNotFoundError:
        print(f"שגיאה: הקובץ '{TOPICS_FILE}' לא נמצא. אנא צור אותו עם רשימת הנושאים שלך.")
        return

    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    updated_topics = []
    has_processed = False

    for topic_line in topics:
        topic_line = topic_line.strip()
        if not topic_line:
            updated_topics.append('')
            continue

        if topic_line.startswith(PROCESSED_MARKER):
            updated_topics.append(topic_line)
            continue

        has_processed = True
        print(f"\n--- מעבד נושא חדש: {topic_line} ---")
        
        filename = generate_filename(topic_line, model)
        time.sleep(2) # Be nice to the API

        if filename:
            content = generate_page_content(topic_line, model)
            time.sleep(2) # Be nice to the API
            
            if content:
                save_content_to_file(filename, content)
                updated_topics.append(f"{PROCESSED_MARKER}{topic_line}")
            else:
                updated_topics.append(topic_line)
        else:
            updated_topics.append(topic_line)

    if has_processed:
        with open(TOPICS_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(updated_topics))
        print("\nקובץ הנושאים 'topics.txt' עודכן.")
    else:
        print("\nלא נמצאו נושאים חדשים לטיפול.")

    print("--- התהליך הסתיים ---")

if __name__ == "__main__":
    main()