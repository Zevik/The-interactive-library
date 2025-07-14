import os
import re

def scan_all_files_and_report():
    """
    Scans all markdown files in the current directory.
    For each file with a category, it prints its title, slug, and category.
    At the end, it lists all slugs for files that are missing a category.
    """
    directory_path = '.'
    slugs_without_category = []

    print("מתחיל סריקה של כל הקבצים...\n")

    # Regex patterns to reliably find the frontmatter fields
    # This handles optional quotes and varying whitespace
    title_pattern = re.compile(r'^title\s*:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
    slug_pattern = re.compile(r'^english_slug\s*:\s*(.*?)\s*$', re.MULTILINE)
    category_pattern = re.compile(r'^category\s*:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)

    # Get a sorted list of files for consistent order
    files_to_scan = sorted([f for f in os.listdir(directory_path) if f.endswith(('.md', '.markdown'))])

    for filename in files_to_scan:
        file_path = os.path.join(directory_path, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Search for each field
            title_match = title_pattern.search(content)
            slug_match = slug_pattern.search(content)
            category_match = category_pattern.search(content)

            # Extract values if found, otherwise use a placeholder
            title_val = title_match.group(1).strip() if title_match else "(לא נמצא)"
            slug_val = slug_match.group(1).strip() if slug_match else "(לא נמצא)"
            
            if category_match:
                category_val = category_match.group(1).strip()
                # Print the details for files with a category
                print(f'title: {title_val}')
                print(f'english_slug: {slug_val}')
                print(f'category: "{category_val}"\n')
            else:
                # If category is missing, add the slug to our list
                if slug_val != "(לא נמצא)":
                    slugs_without_category.append(slug_val)

        except Exception as e:
            print(f"---! שגיאה בקריאת הקובץ {filename}: {e}\n")

    # After the loop, print the list of slugs without a category
    print("---------------------------------------------------------")
    print("קבצים ללא קטגוריה (על פי english_slug):")
    print("---------------------------------------------------------")

    if slugs_without_category:
        for slug in slugs_without_category:
            print(slug)
    else:
        print("כל הקבצים שנבדקו מכילים קטגוריה. כל הכבוד!")
        
    print("\nהסריקה הסתיימה.")


if __name__ == "__main__":
    scan_all_files_and_report()