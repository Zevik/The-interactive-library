import os
import re
import yaml

# --- CONFIGURATION ---
POSTS_DIR = 'posts'

def fix_frontmatter(content):
    """
    Parses and fixes the front matter of a markdown file.
    - Wraps problematic values in quotes.
    - Removes redundant 'layout' and 'post' tag.
    """
    try:
        # Regular expression to find the front matter block
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            print(" -> לא נמצא Frontmatter, מדלג.")
            return content, False

        frontmatter_str = match.group(1)
        body_content = content[match.end():]

        # Load the YAML, it might fail here which is ok for some cases
        try:
            data = yaml.safe_load(frontmatter_str)
        except yaml.YAMLError:
            # If loading fails, we'll try to fix it manually
            data = {}
            lines = frontmatter_str.strip().split('\n')
            for line in lines:
                if ':' in line:
                    parts = line.split(':', 1)
                    key = parts[0].strip()
                    value = parts[1].strip()
                    data[key] = value

        if not isinstance(data, dict):
             print(f" -> מבנה Frontmatter לא תקין, מדלג.")
             return content, False

        fixed = False

        # Rule 1: Remove redundant layout
        if 'layout' in data:
            del data['layout']
            fixed = True

        # Rule 2: Remove redundant 'post' tag
        if 'tags' in data and isinstance(data['tags'], list) and 'post' in data['tags']:
            data['tags'].remove('post')
            # If tags list becomes empty, remove it
            if not data['tags']:
                del data['tags']
            fixed = True

        # Rule 3: Ensure problematic strings are quoted
        # We will rebuild the string manually to ensure quotes
        new_frontmatter_lines = []
        for key, value in data.items():
            if key == 'tags':
                # Format list properly
                new_frontmatter_lines.append(f"tags: {value}")
            else:
                # Quote all other string values
                new_frontmatter_lines.append(f'{key}: "{value}"')
        
        new_frontmatter_str = '\n'.join(new_frontmatter_lines)

        fixed_content = f"---\n{new_frontmatter_str}\n---\n{body_content}"
        return fixed_content, fixed

    except Exception as e:
        print(f" !! שגיאה לא צפויה: {e}")
        return content, False


def main():
    """Main function to iterate over files and fix them."""
    print(f"מתחיל סריקה ותיקון של קבצים בתיקייה '{POSTS_DIR}'...")

    if not os.path.isdir(POSTS_DIR):
        print(f"שגיאה: התיקייה '{POSTS_DIR}' לא קיימת.")
        return

    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(POSTS_DIR, filename)
            print(f"\n--- בודק את הקובץ: {filename}")
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    original_content = f.read()

                # Fix potential `--- yaml` issue first
                content_to_fix = re.sub(r'```yaml\s*\n', '', original_content)
                content_to_fix = re.sub(r'```\s*\n', '', content_to_fix)
                
                if original_content != content_to_fix:
                    print("  -> הוסרו תגיות ```yaml מיותרות.")

                fixed_content, was_fixed = fix_frontmatter(content_to_fix)
                
                if was_fixed or original_content != content_to_fix:
                    print(f"  ✔ נמצאו בעיות ותוקנו. שומר את הקובץ מחדש.")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                else:
                    print("  -> הקובץ נראה תקין, אין צורך בשינויים.")
            except Exception as e:
                print(f" !! נכשל בעיבוד הקובץ {filename}: {e}")
    
    print("\n--- הסתיימה פעולת התיקון! ---")
    print("נסה להריץ את 'npx @11ty/eleventy --serve' שוב.")


if __name__ == "__main__":
    # You might need to install PyYAML: pip install pyyaml
    main()