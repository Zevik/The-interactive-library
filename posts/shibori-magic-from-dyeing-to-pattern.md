---
title: "שיבורי: המסע הקסום מצביעה פשוטה לדפוס מרהיב"
english_slug: shibori-magic-from-dyeing-to-pattern
category: "אמנות ועיצוב / כללי"
tags:
  - שיבורי
  - טקסטיל
  - צביעה
  - אמנות יפנית
  - עשה זאת בעצמך
  - עיצוב
---
<header>
    <h1>שיבורי: המסע הקסום מצביעה פשוטה לדפוס מרהיב</h1>
    <p>כיצד פיסת בד פשוטה יכולה להפוך ליצירת אמנות גיאומטרית מורכבת ומלאת צבע, רק באמצעות קיפול וקשירה? בואו נגלה את הסודות מאחורי הדפוסים המרהיבים שנוצרים בטכניקת השיבורי היפנית העתיקה.</p>
</header>

<div class="shibori-app-container">
    <div class="controls">
        <h2>בחרו את קסם השיבורי שלכם:</h2>
        <p>סמנו את הטכניקות שבהן תשתמשו כדי ליצור את דפוס ההתנגדות על הבד. נסו לשלב!</p>
        <label><input type="checkbox" name="technique" value="accordion"> קיפול אקורדיון (Arashi - פסים אלכסוניים/קווים ארוכים)</label><br>
        <label><input type="checkbox" name="technique" value="boards"> לחיצה בין לוחות (Itajime - צורות גיאומטריות חדות)</label><br>
        <label><input type="checkbox" name="technique" value="pinch"> צביטה וקשירה (Kanoko - נקודות ועיגולים)</label><br>
        <!-- Removed "triangle" and "rod" as separate checkboxes if they overlap significantly with Accordion/Boards/etc or are harder to represent simply. Keeping the core 3 for clarity and better pattern representation. Re-added Rod based on original -->
         <label><input type="checkbox" name="technique" value="rod"> קשירה סביב מוט (Arashi - קווים אלכסוניים)</label><br>
        <label><input type="checkbox" name="technique" value="triangle"> קיפול משולש (Itajime variants - צורות גיאומטריות)</label><br>


        <div class="button-container">
            <button id="dyeButton" class="action-button">צבעו את הבד!</button>
            <button id="resetButton" class="secondary-button">התחלה מחדש</button>
        </div>
    </div>

    <div class="simulation-area">
        <div class="fabric-state">
            <div class="state-message">בחרו טכניקות ולחצו "צבעו את הבד!"</div>
             <div class="selected-techniques-preview"></div>
        </div>
        <div class="dyed-result">
            <!-- The final patterned fabric will appear here -->
        </div>
    </div>
</div>

<button id="toggleExplanation" class="secondary-button toggle-button">הצגת הסבר על שיבורי</button>
<div id="explanation" style="display: none;">
    <h2>מהי טכניקת שיבורי?</h2>
    <p>שיבורי (Shibori) היא טכניקת צביעת בדים יפנית עתיקה שמשמעות שמה היא בערך "לסחוט, ללחוץ, או ללחוץ". זוהי שיטה של צביעה בהתנגדות (resist dyeing), שבה חלקים מהבד מוגנים מצבע על ידי קיפול, קשירה, תפירה, לחיצה או טכניקות אחרות. החלקים המוגנים נשארים בצבעם המקורי (בדרך כלל לבן או צבע הבסיס של הבד), בעוד החלקים החשופים נצבעים, וכך נוצר דפוס ייחודי כשהבד נפתח.</p>

    <h3>מקורותיה של השיבורי ביפן וההיסטוריה שלה</h3>
    <p>טכניקות צביעה בהתנגדות קיימות בתרבויות רבות ברחבי העולם, אך השיבורי היפנית התפתחה לאמנות מורכבת ומתוחכמת. היא הופיעה ביפן כבר במאה ה-8 לספירה. במקור שימשה בעיקר לצביעת משי ובגדי הקסטה (מעמד הלוחמים), אך בהדרגה הפכה נפוצה יותר ושימשה גם לצביעת כותנה ופשתן. בתקופת אדו (1603-1868), השיבורי הגיעה לשיא פריחתה והתפתחו סגנונות אזוריים רבים וטכניקות מורכבות להפליא.</p>

    <h3>העיקרון המדעי/אמנותי מאחורי השיבורי: איך התנגדות לצבע יוצרת דפוסים</h3>
    <p>העיקרון הבסיסי הוא פיזיקלי ואמנותי כאחד: הצבע מתקשר לסיבי הבד בחלקים החשופים, אך אינו יכול לחדור לחלקים שנדחסים, נלחצים או נחסמים באופן פיזי. ככל שההתנגדות חזקה יותר באזור מסוים (למשל, קשר הדוק מאוד, קיפול רב שכבתי, או לחיצה חזקה בין לוחות), כך גדל הסיכוי שהצבע לא יחדור כלל לאזור זה, והוא יישאר בצבע הבסיס. ההפכים – האזורים הצבועים והלא-צבועים – הם שיוצרים יחד את הדפוס. הדפוס הסופי הוא תוצאה ישירה של האופן שבו הבד הושפע ו"התנגד" לצבע.</p>

    <h3>הצגת טכניקות שיבורי נבחרות והסבר קצר על כל אחת</h3>
    <ul>
         <li>
            <h4>אראשי (Arashi):</h4>
            <p>פירוש השם הוא "סערה", והדפוסים המתקבלים לרוב מזכירים גשם נופל באלכסון. הטכניקה כוללת עטיפת הבד סביב מוט גלילי (לרוב עץ או PVC), ולאחר מכן כריכת חוט בחוזקה סביב הבד העטוף. הבד נדחס כלפי מטה על המוט, וכשהוא נצבע, החלקים שנדחסו והוגנו על ידי החוט נשארים לא צבועים, מה שיוצר פסים אלכסוניים או קווים מפותלים לאורך הבד. קיפול אקורדיון לפני העטיפה הוא וריאציה נפוצה ליצירת פסים אחידים יותר.</p>
        </li>
         <li>
            <h4>איטאג'י (Itajime):</h4>
            <p>שיטה זו כוללת קיפול הבד בצורה מסודרת (לרוב קיפול אקורדיון בכיוון אחד ואז קיפול נוסף בכיוון אחר, כמו קיפול נייר לאוריגמי) ולאחר מכן לחיצת הבד המקופל בין שני לוחות נוקשים (לרוב עץ או פלסטיק). הלוחות מוחזקים בחוזקה באמצעות מלחציים או גומיות. הצבע אינו יכול לחדור לאזורים הלחוצים בין הלוחות, וכך נוצרים דפוסים גיאומטריים חדים כמו ריבועים, משולשים או משושים, בהתאם לצורת הקיפול והלוחות.</p>
        </li>
        <li>
            <h4>קנאוקו (Kanoko):</h4>
            <p>הטכניקה הנפוצה ביותר, המזכירה את דפוס הנקודות של עור צבי (קנאוקו פירושו "עור של צבי"). היא כרוכה בצביטה של חלקים קטנים מהבד וקשירתם בחוט חזק כדי ליצור נקודות מוגנות. גודל הנקודות והרווח ביניהן תלויים בגודל חלקי הבד שנצבטו וחוזק הקשירה. זוהי הדוגמה הקלאסית לצביעה בהתנגדות מקומית.</p>
        </li>
         <li>
            <h4>מיורה (Miura): (הוספתי כרפרנס להסבר, למרות שאין כפתור ספציפי)</h4>
            <p>שיטה הכרוכה בלולאת חוט סביב חלקים מהבד מספר פעמים מבלי לקשור קשר הדוק. החוט רק מוחזק על ידי המתח. כתוצאה מכך נוצרים דפוסים מעוגלים ואורגניים יותר, ולעיתים קרובות צבע חודר מעט לחלקים המכורכמים, מה שיוצר גוונים וטקסטורות עדינות.</p>
        </li>
        <li>
            <h4>נויג'י (Nuiage): (הוספתי כרפרנס להסבר, למרות שאין כפתור ספציפי)</h4>
            <p>זוהי טכניקה מדויקת יותר הכרוכה בתפירת הבד ולאחר מכן משיכת החוט בחוזקה כדי לכווץ את הבד באזורים התפורים. החוט התפור מגן על הבד מפני הצבע. ניתן לתפור קווים ישרים, מעוגלים או צורות מורכבות, וכך ליצור קווים וצורות מוגדרות בדפוס הסופי. לעיתים קרובות משאירים את החוט התפור בבד עד לאחר הצביעה.</p>
        </li>
    </ul>

    <h3>הקשר הישיר בין סוג ההתנגדות לדפוס המתקבל</h3>
    <p>הדפוס בשיבורי אינו מקרי. כל טכניקה של קיפול, קשירה, תפירה או לחיצה יוצרת סוג שונה של "התנגדות" לצבע, ולכן מובילה לדפוס אופייני. קשירה יוצרת נקודות או צורות רכות יותר; קיפולים סימטריים יוצרים דפוסים גיאומטריים חוזרים; עטיפה סביב מוט יוצרת קווים אלכסוניים; תפירה מאפשרת יצירת קווים וצורות מוגדרות ומדויקות יותר. ההבנה של קשר זה היא המפתח ליצירת דפוסים מכוונים בשיבורי, וגם לחיזוי התוצאה של שילוב טכניקות.</p>

    <h3>שימושים מודרניים בטכניקת השיבורי</h3>
    <p>שיבורי אינה רק אמנות עתיקה. היא פופולרית מאוד גם כיום בעולם האופנה, עיצוב הבית (כריות, שמיכות, וילונות), ואפילו באמנות פלסטית. מעצבים ואמנים עכשוויים ממשיכים להתנסות בטכניקות המסורתיות וליצור פרשנויות חדשות, לעיתים קרובות בשילוב עם חומרים מודרניים או שיטות צביעה חדשניות. האסתטיקה הייחודית של השיבורי – השילוב בין שליטה (בקיפול והקשירה) לאקראיות מסוימת (בגבולות החדירה של הצבע) – ממשיכה לרתק וליצור תוצאות מרהיבות.</p>
</div>

<style>
    :root {
        --shibori-indigo-dark: #1A237E; /* Darker indigo */
        --shibori-indigo-medium: #3F51B5; /* Medium indigo */
        --shibori-indigo-light: #7986CB; /* Lighter indigo */
        --shibori-white: #F5F5F5; /* Off-white fabric base */
        --shibori-grey: #B0BEC5; /* Light grey for borders/backgrounds */
        --shibori-dark-text: #263238; /* Dark text */
    }

    body {
        font-family: 'Arial', sans-serif; /* Or a more refined web font if available */
        line-height: 1.6;
        color: var(--shibori-dark-text);
        background-color: #ECEFF1; /* Very light grey background */
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure RTL layout */
        text-align: right; /* Default text alignment */
    }

    header h1 {
        color: var(--shibori-indigo-dark);
        text-align: center;
        margin-bottom: 10px;
    }

    header p {
         text-align: center;
         max-width: 700px;
         margin: 0 auto 30px auto;
         color: #546E7A; /* A slightly softer dark text */
    }

    .shibori-app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* More space */
        margin: 20px auto; /* Center the container */
        padding: 30px; /* More padding */
        border: 1px solid var(--shibori-grey);
        border-radius: 12px; /* More rounded corners */
        background-color: var(--shibori-white);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        max-width: 600px; /* Limit container width */
    }

    .controls {
        width: 100%;
        text-align: right;
    }

    .controls h2 {
        color: var(--shibori-indigo-dark);
        margin-top: 0;
        margin-bottom: 10px;
        text-align: center;
    }

    .controls p {
        margin-bottom: 20px;
        color: #546E7A;
        text-align: center;
    }

    .controls label {
        display: block;
        margin-bottom: 10px; /* More space between checkboxes */
        font-size: 1.1rem;
        cursor: pointer;
        transition: color 0.3s ease;
    }

    .controls label:hover {
        color: var(--shibori-indigo-medium);
    }

    .controls input[type="checkbox"] {
         margin-left: 8px; /* Space between checkbox and label text */
          vertical-align: middle;
    }

    .button-container {
        margin-top: 25px; /* More space above buttons */
        display: flex;
        gap: 15px; /* More space between buttons */
        justify-content: center;
        flex-wrap: wrap; /* Allow buttons to wrap on small screens */
    }

    button {
        padding: 12px 20px; /* Larger padding */
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1.1rem; /* Larger font */
        transition: background-color 0.3s ease, transform 0.1s ease;
        min-width: 120px; /* Ensure minimum width */
        text-align: center;
    }

    .action-button {
        background-color: var(--shibori-indigo-medium);
        color: var(--shibori-white);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .action-button:hover {
        background-color: var(--shibori-indigo-dark);
         transform: translateY(-1px); /* Subtle hover effect */
         box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
    }
     .action-button:active {
        background-color: #303F9F; /* Darker on click */
        transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
     }


    .secondary-button {
        background-color: var(--shibori-grey);
        color: var(--shibori-dark-text);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }
     .secondary-button:hover {
        background-color: #90A4AE; /* Darker grey */
         transform: translateY(-1px);
          box-shadow: 0 3px 6px rgba(0, 0, 0, 0.12);
     }
      .secondary-button:active {
        background-color: #78909C; /* Darker grey on click */
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
      }

    .toggle-button {
        display: block;
        margin: 30px auto; /* Center below app container */
        background-color: #607D8B; /* Blue grey */
        color: var(--shibori-white);
    }
     .toggle-button:hover {
         background-color: #546E7A;
     }
     .toggle-button:active {
         background-color: #455A64;
     }

    .simulation-area {
        width: 300px; /* Larger simulation area */
        height: 300px;
        position: relative;
        border: 2px solid var(--shibori-indigo-light); /* More prominent border */
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        background-color: var(--shibori-white); /* Base fabric color */
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05); /* Inner shadow for depth */
    }

    .fabric-state {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        flex-direction: column; /* Stack message and preview */
        justify-content: center;
        align-items: center;
        background-color: rgba(255, 255, 255, 0.9); /* More opaque overlay */
        z-index: 2;
        text-align: center;
        padding: 20px;
        transition: opacity 0.5s ease-in-out; /* Fade state text */
    }

    .state-message {
        font-size: 1.2rem;
        color: var(--shibori-dark-text);
        margin-bottom: 15px; /* Space between message and preview */
    }

     .selected-techniques-preview {
         font-size: 0.9rem;
         color: #546E7A;
         text-align: center;
         line-height: 1.5;
         max-width: 80%;
         word-break: break-word; /* Prevent overflow */
     }

    .dyed-result {
        width: 100%;
        height: 100%;
        background-color: var(--shibori-white); /* Initial fabric color */
        opacity: 0; /* Hidden initially */
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
        /* Transition handled by JS for sequence */
    }

    /* Improved CSS Patterns for techniques */
    /* Use a softer, more organic indigo color */
    /* Accordion / Arashi (Rod wrap): Diagonal Waves */
    .pattern-accordion, .pattern-rod {
        background-color: var(--shibori-white);
       background-image: repeating-linear-gradient(
           45deg,
           var(--shibori-indigo-medium) 0px,
           var(--shibori-indigo-medium) 2px,
           transparent 2px,
           transparent 20px /* Wider transparent gap */
       );
       background-size: 100% 40px; /* Control density */
       /* Add another layer for texture/variation */
       background-image:
           repeating-linear-gradient(
              -45deg,
              rgba(26, 35, 126, 0.1) 0px, /* Semi-transparent dark indigo */
              rgba(26, 35, 126, 0.1) 1px,
              transparent 1px,
              transparent 15px
           ),
           repeating-linear-gradient(
               45deg,
               var(--shibori-indigo-medium) 0px,
               var(--shibori-indigo-medium) 2px,
               transparent 2px,
               transparent 20px
           );
         background-size: 100% 40px, 100% 40px;

    }

    /* Boards / Itajime: Geometric Blocks */
    .pattern-boards, .pattern-triangle {
        background-color: var(--shibori-white);
         background-image:
            linear-gradient(to right, var(--shibori-indigo-medium) 0px, var(--shibori-indigo-medium) 15px, transparent 15px, transparent 35px),
            linear-gradient(to bottom, var(--shibori-indigo-medium) 0px, var(--shibori-indigo-medium) 15px, transparent 15px, transparent 35px);
        background-size: 50px 50px; /* Control grid size */
        /* Add a subtle overlay for depth */
         box-shadow: inset 0 0 15px rgba(26, 35, 126, 0.1);
    }

    /* Pinch / Kanoko: Organic Dots */
     .pattern-pinch {
        background-color: var(--shibori-white);
        /* Use multiple radial gradients for variation */
        background-image:
            radial-gradient(circle at 10px 10px, transparent 5px, var(--shibori-indigo-medium) 5px, var(--shibori-indigo-medium) 7px, transparent 7px),
            radial-gradient(circle at 30px 30px, transparent 4px, var(--shibori-indigo-dark) 4px, var(--shibori-indigo-dark) 6px, transparent 6px),
             radial-gradient(circle at 20px 40px, transparent 6px, var(--shibori-indigo-light) 6px, var(--shibori-indigo-light) 8px, transparent 8px);

        background-size: 40px 40px; /* Control density of dot groups */
        background-position: 0 0, 20px 20px, 10px 0; /* Stagger the dot patterns */
    }


    /* Full Dye: Solid Color */
    .pattern-full-dye {
        background-color: var(--shibori-indigo-medium);
        background-image: none;
    }

    #explanation {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid var(--shibori-grey);
        border-radius: 8px;
        background-color: #E3F2FD; /* Light blue background */
        text-align: right;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }

    #explanation h2,
    #explanation h3,
    #explanation h4 {
        color: var(--shibori-indigo-dark);
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid var(--shibori-indigo-light); /* Subtle separator */
        padding-bottom: 5px;
    }
     #explanation h4 {
         font-size: 1.1rem;
          border-bottom: none;
           padding-bottom: 0;
           margin-bottom: 5px;
     }

    #explanation ul {
        list-style: disc; /* Use standard list style */
        padding-right: 20px; /* Add padding for list items */
        margin-bottom: 15px;
    }
     #explanation ul li {
        margin-bottom: 10px;
        line-height: 1.5;
        color: #37474F; /* Dark grey text */
     }

     #explanation p {
        line-height: 1.7;
        color: #37474F;
     }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const dyeButton = document.getElementById('dyeButton');
        const resetButton = document.getElementById('resetButton');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');
        const dyedResultDiv = document.querySelector('.dyed-result');
        const fabricStateDiv = document.querySelector('.fabric-state');
        const stateMessageDiv = fabricStateDiv.querySelector('.state-message');
        const selectedTechniquesPreviewDiv = fabricStateDiv.querySelector('.selected-techniques-preview');
        const techniqueCheckboxes = document.querySelectorAll('input[name="technique"]');
        const techniqueLabels = {
             accordion: 'קיפול אקורדיון (פסי Arashi)',
             boards: 'לחיצה בין לוחות (Itajime)',
             pinch: 'צביטה וקשירה (Kanoko)',
             rod: 'קשירה סביב מוט (Arashi)',
             triangle: 'קיפול משולש (וריאציית Itajime)'
        };

        const techniquePatterns = {
            accordion: 'pattern-accordion',
            triangle: 'pattern-boards', // triangle folding results in geometric patterns similar to boards
            pinch: 'pattern-pinch',
            rod: 'pattern-rod', // rod wrap for Arashi lines
            boards: 'pattern-boards'
        };

        function applyPatterns(techniques) {
             // Clear previous patterns
            dyedResultDiv.className = 'dyed-result'; // Reset class

            if (techniques.length === 0) {
                dyedResultDiv.classList.add('pattern-full-dye');
            } else {
                 // Add classes for each selected technique pattern
                techniques.forEach(tech => {
                    if (techniquePatterns[tech]) {
                        dyedResultDiv.classList.add(techniquePatterns[tech]);
                    }
                });
                 // Note: CSS layering handles combinations. This is a representation,
                 // not a perfect physical simulation of combined resistances.
            }
        }

        // Update preview text when checkboxes change
        techniqueCheckboxes.forEach(checkbox => {
             checkbox.addEventListener('change', updatePreview);
        });

        function updatePreview() {
             const selectedTechniques = Array.from(techniqueCheckboxes)
                                        .filter(input => input.checked)
                                        .map(input => techniqueLabels[input.value]);

            if (selectedTechniques.length > 0) {
                 selectedTechniquesPreviewDiv.textContent = 'נבחרו: ' + selectedTechniques.join(' | ');
                 selectedTechniquesPreviewDiv.style.display = 'block';
            } else {
                 selectedTechniquesPreviewDiv.textContent = '';
                 selectedTechniquesPreviewDiv.style.display = 'none';
            }
        }


        dyeButton.addEventListener('click', () => {
            const selectedTechniques = Array.from(techniqueCheckboxes)
                                        .filter(input => input.checked)
                                        .map(input => input.value);

            // Disable buttons during simulation
            dyeButton.disabled = true;
            resetButton.disabled = true;
             dyeButton.classList.add('simulating'); // Optional: Add styling for simulating state

            dyedResultDiv.style.opacity = 0; // Hide previous result immediately
            dyedResultDiv.className = 'dyed-result'; // Reset classes for animation
            fabricStateDiv.style.display = 'flex'; // Ensure state text is visible
            fabricStateDiv.style.opacity = 1; // Ensure state text is fully opaque initially
             selectedTechniquesPreviewDiv.style.display = 'none'; // Hide preview during simulation

            if (selectedTechniques.length === 0) {
                 stateMessageDiv.textContent = 'טוב, לא נבחרו טכניקות התנגדות...';
                 setTimeout(() => {
                     stateMessageDiv.textContent = 'זה אומר שצובעים את כל הבד!';
                     setTimeout(() => {
                         stateMessageDiv.textContent = 'טובלים בצבע...';
                         setTimeout(() => {
                            stateMessageDiv.textContent = 'הבד נצבע כולו!';
                             applyPatterns([]); // Apply full dye pattern
                             // Animate result appearance
                            dyedResultDiv.style.transition = 'opacity 1.5s ease-in-out';
                            dyedResultDiv.style.opacity = 1;
                             // Fade out state text after result shows
                            fabricStateDiv.style.transition = 'opacity 1s ease-in-out 1s'; /* Add delay */
                             fabricStateDiv.style.opacity = 0;
                             setTimeout(() => {
                                 fabricStateDiv.style.display = 'none';
                                 dyeButton.disabled = false; // Re-enable buttons
                                 resetButton.disabled = false;
                                  dyeButton.classList.remove('simulating');
                                 updatePreview(); // Restore preview visibility if needed (though usually not after full dye)
                             }, 2500); // Total time: initial message + msg2 + msg3 + dye delay + fade out delay
                         }, 1000); // Simulate dyeing time
                     }, 1500); // Delay before second message
                 }, 1500); // Delay before first message
                 return;
            }

            stateMessageDiv.textContent = 'מכינים את הבד לשיבורי...'; // Step 1: Preparation
            setTimeout(() => {
                stateMessageDiv.textContent = 'מקפלים, קושרים ולוחצים...'; // Step 2: Applying techniques
                 // Show selected techniques again briefly as part of the process
                 selectedTechniquesPreviewDiv.textContent = 'הטכניקות שבחרתם: ' + selectedTechniques.map(tech => techniqueLabels[tech]).join(' | ');
                 selectedTechniquesPreviewDiv.style.display = 'block';

                setTimeout(() => {
                    stateMessageDiv.textContent = 'טובלים באמבט הצבע הקסום!'; // Step 3: Dyeing
                     selectedTechniquesPreviewDiv.style.display = 'none'; // Hide preview during dyeing

                    setTimeout(() => {
                        stateMessageDiv.textContent = 'רגע האמת: פותחים את הבד...'; // Step 4: Unfolding

                        // Apply patterns using CSS classes BEFORE the final reveal animation
                        applyPatterns(selectedTechniques);

                        // Animate result appearance and fade out state
                        setTimeout(() => {
                             stateMessageDiv.textContent = 'הדפוס המרהיב שנוצר!'; // Final state message before hiding
                             dyedResultDiv.style.transition = 'opacity 2s ease-in-out'; /* Longer, dramatic reveal */
                             dyedResultDiv.style.opacity = 1;

                            fabricStateDiv.style.transition = 'opacity 1.5s ease-in-out 1.5s'; /* Add delay matching result fade */
                            fabricStateDiv.style.opacity = 0;


                            setTimeout(() => {
                                fabricStateDiv.style.display = 'none';
                                 dyeButton.disabled = false; // Re-enable buttons
                                 resetButton.disabled = false;
                                 dyeButton.classList.remove('simulating');
                                 updatePreview(); // Ensure preview is updated/shown if state div is hidden
                            }, 3500); // Total time after reveal starts (reveal duration + fade out duration)

                        }, 2000); // Simulate unfolding time (longer)

                    }, 2000); // Simulate dyeing time (longer)
                }, 2000); // Simulate preparation/technique application time
            }, 1000); // Initial delay
        });

        resetButton.addEventListener('click', () => {
            techniqueCheckboxes.forEach(input => input.checked = false);
            dyedResultDiv.style.backgroundImage = '';
            dyedResultDiv.style.backgroundSize = '';
            dyedResultDiv.style.backgroundColor = var(--shibori-white); /* Reset to base fabric color */
            dyedResultDiv.style.opacity = 0;
            dyedResultDiv.className = 'dyed-result'; // Reset classes
            fabricStateDiv.style.display = 'flex';
             fabricStateDiv.style.opacity = 1; /* Ensure state text is visible */
             fabricStateDiv.style.transition = 'none'; /* Remove transition for instant reset */
            stateMessageDiv.textContent = 'בחרו טכניקות ולחצו "צבעו את הבד!"';
            selectedTechniquesPreviewDiv.textContent = ''; // Clear preview
            selectedTechniquesPreviewDiv.style.display = 'none';
             dyeButton.disabled = false; // Ensure buttons are enabled
             resetButton.disabled = false;
             dyeButton.classList.remove('simulating');

        });

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתרת הסבר על שיבורי' : 'הצגת הסבר על שיבורי';
        });

         // Initial update of preview on page load
         updatePreview();
    });
</script>