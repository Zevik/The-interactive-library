---
title: "ניהול טלסקופ החלל: ההחלטה בידיים שלך"
english_slug: space-telescope-management-the-decision-is-yours
category: "אווירונאוטיקה וחלל"
tags:
  - אסטרונומיה
  - טלסקופ חלל
  - קבלת החלטות
  - ניהול פרויקטים
  - מדעי החלל
---
# ניהול טלסקופ החלל: ההחלטה בידיים שלך

דמיין שאתה עומד בראש צוות ניהול טלסקופ חלל פורץ דרך, שגורלו המדעי בידיים שלך. יש אינספור תעלומות ביקום שמחכות להיפתר, כוכבי לכת נסתרים לפענח, גלקסיות עמוקות לגלות. אבל הזמן על הטלסקופ יקר להחריד, והתקציב מוגבל. כל שעת תצפית וכל דולר שמושקעים במטרה אחת, באים על חשבון מטרה אחרת. איך תבחר את תוכנית התצפית שתמקסם את התפוקה המדעית של המשימה היקרה הזו?

<div id="app">
    <h2 class="app-title">בניית תוכנית תצפית לטלסקופ החלל</h2>

    <div class="constraints-panel">
        <div class="resources-display">
            <div class="resource-item">
                <strong>זמן טלסקופ כולל:</strong> <span id="total-time"></span> שעות
            </div>
            <div class="resource-item">
                <strong>תקציב כולל:</strong> <span id="total-budget"></span> מיליון דולר
            </div>
        </div>
         <div class="resources-remaining">
            <strong>נותרו:</strong>
            <div class="resource-bar time-bar">
                <span class="bar-label">זמן: <span id="remaining-time"></span> שעות</span>
                 <div class="bar-fill time-fill"></div>
            </div>
            <div class="resource-bar budget-bar">
                 <span class="bar-label">תקציב: <span id="remaining-budget"></span> מיליון דולר</span>
                 <div class="bar-fill budget-fill"></div>
            </div>
        </div>
    </div>

    <div class="target-list-section">
        <h3>מטרות תצפית פוטנציאליות - בחר בחוכמה!</h3>
        <div id="targets-container" class="targets-grid">
            <!-- Targets will be loaded here by JS -->
        </div>
    </div>

    <div class="action-buttons">
        <button id="submit-plan" class="action-button primary">הגש תוכנית תצפית</button>
        <button id="reset-plan" class="action-button secondary">אפס תוכנית</button>
    </div>


    <div id="results" class="results-panel hidden">
        <h3 class="results-title">תוצאות התוכנית שלך</h3>
        <div class="results-summary">
            <p>סה"כ תפוקה מדעית שהושגה: <span id="total-scientific-value" class="highlight-value"></span> נקודות</p>
            <p>סה"כ זמן טלסקופ שנוצל: <span id="used-time" class="highlight-resource"></span> שעות</p>
            <p>סה"כ תקציב שנוצל: <span id="used-budget" class="highlight-resource"></span> מיליון דולר</p>
            <div class="selected-targets-list">
                 <h4>מטרות שנכללו בתוכנית:</h4>
                 <ul id="selected-targets-names">
                      <!-- Selected target names will be listed here -->
                 </ul>
            </div>
        </div>
        <div id="feedback" class="feedback-message"></div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג/הסתר הסבר: ניהול משאבים בטלסקופי חלל</button>

<div id="explanation" class="explanation-section hidden">
    <h2>על ניהול משאבים בטלסקופי חלל</h2>
    <p><strong>מבוא: האתגר של ניהול משאבי חלל מוגבלים</strong></p>
    <p>ניהול פרויקטים מדעיים גדולים כמו טלסקופי חלל כרוך בהתמודדות עם משאבים יקרים ומוגבלים ביותר: זמן תצפית יקר על הטלסקופ, תקציבי ענק לפיתוח, תפעול ועיבוד נתונים, וכוח אדם מדעי והנדסי מומחה. האתגר המרכזי הוא להפיק את מירב התפוקה המדעית האפשרית במסגרת המגבלות הקיימות.</p>

    <p><strong>גורמים מרכזיים המשפיעים על בחירת מטרות תצפית:</strong></p>
    <ul>
        <li><strong>פוטנציאל מדעי ותרומה לידע:</strong> זהו השיקול העיקרי. כל מטרה מוערכת על פי יכולתה להרחיב את הבנתנו את היקום, לענות על שאלות מדעיות פתוחות או לגלות תופעות חדשות.</li>
        <li><strong>עלות (זמן טלסקופ, תקציב עיבוד נתונים):</strong> לכל תצפית נדרש זמן טלסקופ מסוים ומשאבים כספיים לעיבוד וניתוח הנתונים שהתקבלו. מטרות מסוימות עשויות להיות בעלות פוטנציאל מדעי גבוה אך יקרות מאוד מבחינת משאבים.</li>
        <li><strong>דחיפות (אירועים אסטרונומיים חולפים):</strong> אירועים כמו סופרנובות, התפרצויות גמא או מעברי כוכבי לכת חוץ-שמשיים דורשים תצפית מיידית ואינם יכולים לחכות למועד תצפית מתוכנן אחרת. לאירועים כאלה ניתנת לעיתים עדיפות גבוהה מאוד.</li>
        <li><strong>סיכונים (תקלות, קשיים בניתוח):</strong> יש תצפיות הכרוכות בסיכון גבוה יותר - למשל, תצפית על מטרה קשה או רחוקה במיוחד שעשויה שלא להניב נתונים באיכות מספקת, או תצפית שעלולה להיתקל בבעיות טכניות.</li>
        <li><strong>שיקולים אסטרטגיים (איזון בין תחומי מחקר שונים):</strong> סוכנויות חלל ומכוני מחקר שואפים לקדם את כלל תחומי האסטרונומיה (קוסמולוגיה, חקר כוכבים, חקר כוכבי לכת חיצוניים ועוד). לעיתים נבחרות תצפיות כדי להבטיח איזון בין תחומי מחקר שונים, גם אם הפוטנציאל המדעי הספציפי של מטרה אחת נמוך במעט מאחרת.</li>
    </ul>

    <p><strong>תהליך קבלת החלטות בפועל:</strong></p>
    <p>החלטות הקצאת זמן טלסקופ אינן מתקבלות בקלות. בדרך כלל, מדענים מגישים הצעות תצפית תחרותיות לוועדות מומחים (פאנלים) המורכבות ממדענים מובילים בתחומים שונים. פאנלים אלו בוחנים את ההצעות על פי הקריטריונים שהוזכרו וממליצים על תוכנית תצפית אופטימלית. התהליך הוא לרוב בינלאומי, ומערב מדענים ממוסדות רבים. מודלים אופטימיזציה ממוחשבים יכולים לסייע בתכנון התוכנית הסופית בהתאם למגבלות הטכניות של הטלסקופ וזמינותו.</p>

    <p><strong>השוואה למודלים של קבלת החלטות:</strong></p>
    <p>ניתן לראות את תהליך קבלת ההחלטות כניסיון להתקרב למודל רציונלי - בחירה שממקסמת את התועלת (פוטנציאל מדעי) בהינתן מגבלות. עם זאת, בפועל, מדובר לרוב ב"רציונליות מוגבלת" (Bounded Rationality) - ההחלטה מתקבלת בהיעדר מידע מושלם, תחת לחצי זמן, ובהשפעת גורמים נוספים כמו שיקולים פוליטיים או צורך בריצוי קהילות מדעיות שונות.</p>

    <p><strong>דוגמאות מהיסטוריית טלסקופי חלל:</strong></p>
    <p>טלסקופ החלל האבל חולל מהפכה באסטרונומיה, בין השאר בזכות החלטות תצפית אסטרטגיות כמו תצפית "שדה עמוק" (Hubble Deep Field) שנמשכה זמן רב והניבה תמונה של אלפי גלקסיות עמומות ורחוקות מאוד, למרות העלות הגבוהה בזמן טלסקופ. טלסקופ החלל ג'יימס ווב, עם יכולותיו הייחודיות בצפייה באינפרא-אדום, מקדיש חלק ניכר מזמנו לחקר האטמוספרות של כוכבי לכת חוץ-שמשיים ולצפייה בגלקסיות הראשונות שנוצרו ביקום - יעדים שנחשבים בעלי פוטנציאל מדעי עצום אך דורשים זמן תצפית רב.</p>

    <p><strong>ההשפעה ארוכת הטווח של החלטות הקצאת משאבים על התקדמות המדע:</strong></p>
    <p>החלטות המתקבלות היום לגבי הקצאת משאבים לטלסקופי חלל מעצבות את עתיד האסטרונומיה לשנים ואף עשורים קדימה. הן קובעות אילו תגליות יתאפשרו, אילו שאלות יישארו פתוחות, ואילו תחומי מחקר יזכו לקידום משמעותי. זו אחריות כבדה הדורשת שילוב של חזון מדעי, הבנה טכנית ויכולת קבלת החלטות מורכבות.</p>
</div>

<style>
    :root {
        --primary-color: #4a90e2; /* A spacey blue */
        --secondary-color: #50e3c2; /* Teal/Mint */
        --dark-background: #1a2a3a; /* Deep space blue */
        --light-text: #e0e0e0;
        --card-background: #2c3e50; /* Darker blue */
        --card-border: #34495e;
        --value-high: #50e3c2; /* Teal */
        --value-medium: #f5a623; /* Orange */
        --value-low: #d0021b; /* Red */
        --urgency-yes: #bd10e0; /* Purple */
        --risk-high: #d0021b; /* Red */
        --risk-low: #50e3c2; /* Green */
        --button-primary-bg: var(--primary-color);
        --button-primary-hover: #357ABD;
        --button-secondary-bg: #607d8b; /* Greyish blue */
        --button-secondary-hover: #546e7a;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background: linear-gradient(to bottom, #1a2a3a 0%, #2c3e50 100%); /* Subtle gradient background */
        color: var(--light-text);
        min-height: 100vh;
        box-sizing: border-box;
    }

    #app, .explanation-section {
        background-color: rgba(44, 62, 80, 0.9); /* Semi-transparent card background */
        border: 1px solid var(--card-border);
        padding: 30px;
        border-radius: 12px;
        margin: 20px auto;
        max-width: 900px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        animation: fadeIn 0.8s ease-out;
    }

     @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    h1, h2, h3 {
        color: var(--secondary-color);
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }

     .app-title, .results-title {
        font-size: 2em;
        margin-bottom: 30px;
     }

    .constraints-panel, .results-panel {
        border: 1px solid var(--card-border);
        padding: 20px;
        margin-bottom: 30px;
        border-radius: 8px;
        background-color: rgba(52, 73, 94, 0.8); /* Slightly lighter */
    }

     .resources-display, .resources-remaining {
         display: flex;
         flex-wrap: wrap;
         gap: 20px;
         margin-bottom: 15px;
     }

     .resources-display {
        padding-bottom: 15px;
        border-bottom: 1px dashed var(--card-border);
     }

     .resource-item, .resource-bar {
        flex: 1;
        min-width: 200px; /* Ensure they don't get too squashed */
     }

    .resource-bar {
        background-color: rgba(0,0,0,0.3);
        border-radius: 5px;
        overflow: hidden;
        height: 30px;
        position: relative;
        margin-top: 10px;
    }

    .bar-label {
        position: absolute;
        width: 100%;
        text-align: center;
        line-height: 30px;
        color: white;
        z-index: 1;
        font-size: 0.9em;
    }

    .bar-fill {
        height: 100%;
        width: 100%; /* Initial state is full */
        background-color: var(--value-high); /* Start green */
        transition: width 0.5s ease-out, background-color 0.5s ease-out;
    }

    .bar-fill.time-fill { background-color: var(--value-high); }
    .bar-fill.budget-fill { background-color: var(--primary-color); }


    .target-list-section h3 {
        text-align: right;
        margin-bottom: 20px;
        color: var(--light-text);
    }

    .targets-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 20px;
    }

    .target-item {
        border: 1px solid var(--card-border);
        padding: 20px;
        border-radius: 8px;
        background-color: var(--card-background);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.3s ease-out, box-shadow 0.3s ease-out, border-color 0.3s ease-out;
        cursor: pointer; /* Indicate clickable area */
        position: relative; /* For hover/selection effects */
        overflow: hidden; /* For subtle border effects */
    }

     .target-item::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 8px;
        box-shadow: inset 0 0 0 0px var(--secondary-color); /* Glow effect */
        transition: box-shadow 0.3s ease-out;
        pointer-events: none; /* Don't interfere with clicks */
     }


    .target-item.selected {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        border-color: var(--secondary-color);
    }

     .target-item.selected::after {
         box-shadow: inset 0 0 0 2px var(--secondary-color);
     }

     .target-item.disabled {
         opacity: 0.5;
         cursor: not-allowed;
         pointer-events: none; /* Prevent interaction */
     }


    .target-item h4 {
        margin-top: 0;
        margin-bottom: 15px;
        color: var(--light-text);
        font-size: 1.2em;
        text-align: right;
        border-bottom: 1px solid var(--card-border);
        padding-bottom: 10px;
    }

    .target-item p {
        margin: 8px 0;
        font-size: 0.95em;
        text-align: right;
        color: var(--light-text);
    }

    .target-item p strong {
        color: var(--secondary-color);
        font-weight: normal;
    }

    .target-item span {
        font-weight: bold;
    }

    .value-high { color: var(--value-high); }
    .value-medium { color: var(--value-medium); }
    .value-low { color: var(--value-low); }
    .urgency-yes { color: var(--urgency-yes); }
    .risk-high { color: var(--risk-high); }
    .risk-low { color: var(--risk-low); }

     /* Style the custom checkbox look */
    .target-item .checkbox-container {
        margin-top: 15px;
        align-self: flex-end; /* Align to the left in RTL */
        display: flex;
        align-items: center;
        cursor: pointer;
        color: var(--light-text);
        font-size: 1.1em;
     }

    .target-item .checkbox-container input[type="checkbox"] {
        /* Hide the default checkbox */
        position: absolute;
        opacity: 0;
        cursor: pointer;
        height: 0;
        width: 0;
     }

     /* Create a custom checkbox indicator */
    .checkmark {
        height: 24px;
        width: 24px;
        background-color: rgba(255,255,255,0.1);
        border: 2px solid var(--secondary-color);
        border-radius: 4px;
        margin-left: 10px; /* Space between text and checkbox */
        transition: background-color 0.2s ease-out, border-color 0.2s ease-out;
        display: inline-block;
        position: relative;
     }

    .target-item .checkbox-container input:checked ~ .checkmark {
        background-color: var(--secondary-color);
        border-color: var(--secondary-color);
     }

     /* Create the checkmark indicator (hidden when not checked) */
     .checkmark:after {
        content: "";
        position: absolute;
        display: none;
        left: 8px;
        top: 3px;
        width: 5px;
        height: 10px;
        border: solid var(--dark-background);
        border-width: 0 3px 3px 0;
        transform: rotate(45deg);
     }

     /* Show the checkmark when checked */
     .target-item .checkbox-container input:checked ~ .checkmark:after {
        display: block;
     }


    .action-buttons {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px;
    }

    .action-button {
        display: inline-block; /* Allow side-by-side */
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        margin: 0 10px; /* Space between buttons */
        transition: background-color 0.3s ease-out, transform 0.2s ease-out;
        font-weight: bold;
    }

    .action-button.primary {
        background-color: var(--button-primary-bg);
        color: white;
    }

    .action-button.primary:hover {
        background-color: var(--button-primary-hover);
        transform: translateY(-2px);
    }

     .action-button.secondary {
        background-color: var(--button-secondary-bg);
        color: white;
     }

     .action-button.secondary:hover {
        background-color: var(--button-secondary-hover);
        transform: translateY(-2px);
     }


    .results-summary p {
        margin-bottom: 10px;
        font-size: 1.1em;
    }

    .highlight-value {
        color: var(--value-high); /* Green/Teal for value */
        font-weight: bold;
        font-size: 1.2em;
    }

     .highlight-resource {
        color: var(--secondary-color); /* Teal/Mint for resources */
        font-weight: bold;
     }


     .selected-targets-list {
         margin-top: 20px;
         padding-top: 15px;
         border-top: 1px dashed var(--card-border);
     }

     .selected-targets-list h4 {
         margin-top: 0;
         color: var(--light-text);
         font-size: 1em;
         margin-bottom: 10px;
     }

     #selected-targets-names {
         list-style: none;
         padding: 0;
         margin: 0;
         display: flex;
         flex-wrap: wrap;
         gap: 10px;
     }

     #selected-targets-names li {
         background-color: rgba(74, 144, 226, 0.3); /* Semi-transparent primary color */
         padding: 5px 10px;
         border-radius: 4px;
         font-size: 0.9em;
     }


    .feedback-message {
        margin-top: 20px;
        padding: 15px;
        border-top: 1px solid var(--card-border);
        font-weight: bold;
        color: var(--secondary-color); /* Teal/Mint for positive feedback */
        text-align: center;
        animation: slideInUp 0.5s ease-out;
    }

     @keyframes slideInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
     }

     .feedback-message strong {
        color: var(--value-medium); /* Orange for warnings/suggestions */
     }

    .toggle-button {
        display: block;
        width: auto;
        padding: 12px 25px;
        background-color: var(--button-secondary-bg);
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        margin: 30px auto;
        text-align: center;
        transition: background-color 0.3s ease-out, transform 0.2s ease-out;
        font-weight: bold;
    }

    .toggle-button:hover {
        background-color: var(--button-secondary-hover);
        transform: translateY(-2px);
    }

    .explanation-section h2 {
         text-align: right;
         color: var(--primary-color);
    }

    .explanation-section p, .explanation-section ul {
         text-align: right;
         color: var(--light-text);
         margin-bottom: 15px;
    }

    .explanation-section ul {
        list-style: disc inside; /* Ensure list style */
        padding-right: 20px;
    }

    .explanation-section li {
        margin-bottom: 8px;
    }


    .hidden {
        display: none;
    }

     /* Responsive adjustments */
     @media (max-width: 768px) {
         .targets-grid {
             grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
         }

         .resource-item, .resource-bar {
             min-width: 150px;
         }

         .action-button {
             margin: 10px 5px;
         }
         #app, .explanation-section {
             padding: 20px;
         }
     }

      @media (max-width: 480px) {
         .targets-grid {
             grid-template-columns: 1fr; /* Stack items */
         }
         .resource-item, .resource-bar {
             width: 100%;
         }
          .resources-display, .resources-remaining {
              flex-direction: column;
              gap: 10px;
          }
         .action-button {
             display: block;
             margin: 10px auto;
         }
          #app, .explanation-section {
             padding: 15px;
         }
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Constants
        const TOTAL_TIME_HOURS = 500;
        const TOTAL_BUDGET_MILLIONS = 10; // in millions

        // State variables
        let remainingTime = TOTAL_TIME_HOURS;
        let remainingBudget = TOTAL_BUGET_MILLIONS;
        let selectedTargets = [];

        // DOM elements
        const totalTimeEl = document.getElementById('total-time');
        const totalBudgetEl = document.getElementById('total-budget');
        const remainingTimeEl = document.getElementById('remaining-time');
        const remainingBudgetEl = document.getElementById('remaining-budget');
        const timeFillBar = document.querySelector('.time-fill');
        const budgetFillBar = document.querySelector('.budget-fill');
        const targetsContainer = document.getElementById('targets-container');
        const submitButton = document.getElementById('submit-plan');
        const resetButton = document.getElementById('reset-plan');
        const resultsDiv = document.getElementById('results');
        const totalScientificValueEl = document.getElementById('total-scientific-value');
        const usedTimeEl = document.getElementById('used-time');
        const usedBudgetEl = document.getElementById('used-budget');
        const selectedTargetsNamesEl = document.getElementById('selected-targets-names');
        const feedbackEl = document.getElementById('feedback');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');


        // Target Data (Example Data) - Added unique IDs and slightly varied stats
        const allTargets = [
            { id: 1, name: 'גלקסיית אנדרומדה (M31)', scientificValue: 'גבוה', timeCost: 50, budgetCost: 0.5, urgency: 'לא', risk: 'נמוך' },
            { id: 2, name: 'ערפילית אוריון (M42)', scientificValue: 'גבוה', timeCost: 40, budgetCost: 0.4, urgency: 'לא', risk: 'נמוך' },
            { id: 3, name: 'שדה עמוק (Deep Field)', scientificValue: 'גבוה מאוד', timeCost: 150, budgetCost: 2.0, urgency: 'לא', risk: 'בינוני' },
            { id: 4, name: 'כוכב לכת חוץ-שמשי (TRAPPIST-1e) - אטמוספרה', scientificValue: 'גבוה', timeCost: 80, budgetCost: 1.2, urgency: 'לא', risk: 'בינוני' },
            { id: 5, name: 'סופרנובה (התפרצות CRTS-II)', scientificValue: 'גבוה מאוד', timeCost: 30, budgetCost: 0.8, urgency: 'כן', risk: 'נמוך' },
            { id: 6, name: 'צביר גלקסיות (קומא)', scientificValue: 'בינוני', timeCost: 70, budgetCost: 0.6, urgency: 'לא', risk: 'נמוך' },
            { id: 7, name: 'ערפילית פלנטרית (טבעת)', scientificValue: 'בינוני', timeCost: 25, budgetCost: 0.3, urgency: 'לא', risk: 'נמוך' },
            { id: 8, name: 'חור שחור על-מסיבי (ליבת M87)', scientificValue: 'גבוה', timeCost: 60, budgetCost: 1.5, urgency: 'לא', risk: 'בינוני' },
            { id: 9, name: 'קווזאר רחוק', scientificValue: 'בינוני-גבוה', timeCost: 90, budgetCost: 1.0, urgency: 'לא', risk: 'גבוה' },
            { id: 10, name: 'אסטרואיד חדש (דרוש מעקב)', scientificValue: 'נמוך-בינוני', timeCost: 10, budgetCost: 0.1, urgency: 'כן', risk: 'נמוך' },
            { id: 11, name: 'שביל החלב - מרכז הגלקסיה', scientificValue: 'גבוה', timeCost: 100, budgetCost: 0.7, urgency: 'לא', risk: 'נמוך' },
            { id: 12, name: 'התנגשות כוכבי ניוטרון (אירוע GRB)', scientificValue: 'גבוה מאוד', timeCost: 20, budgetCost: 1.0, urgency: 'כן', risk: 'נמוך' },
             { id: 13, name: 'ערפילית עמודים ( Pillars of Creation)', scientificValue: 'גבוה', timeCost: 45, budgetCost: 0.5, urgency: 'לא', risk: 'נמוך' },
             { id: 14, name: 'אקסו-מון (ירח חוץ-שמשי) פוטנציאלי', scientificValue: 'גבוה מאוד', timeCost: 120, budgetCost: 1.8, urgency: 'לא', risk: 'גבוה' },
             { id: 15, name: 'שארית סופרנובה (סרטן)', scientificValue: 'בינוני-גבוה', timeCost: 35, budgetCost: 0.4, urgency: 'לא', risk: 'נמוך' },
        ];

        // Mapping for scientific value text to a numerical score
        const valueScores = {
            'נמוך': 1,
            'נמוך-בינוני': 2,
            'בינוני': 3,
            'בינוני-גבוה': 4,
            'גבוה': 6, // Increased scores for higher levels
            'גבוה מאוד': 10
        };

        // Initialize display
        const initializeApp = () => {
            totalTimeEl.textContent = TOTAL_TIME_HOURS;
            totalBudgetEl.textContent = TOTAL_BUGET_MILLIONS;
            resetPlan(); // Use reset to initialize state and display
            renderTargets();
            resultsDiv.classList.add('hidden'); // Hide results initially
            explanationDiv.classList.add('hidden'); // Hide explanation initially
        };

         // Update resource display and bars
        const updateResourceDisplay = () => {
            remainingTimeEl.textContent = remainingTime.toFixed(1);
            remainingBudgetEl.textContent = remainingBudget.toFixed(1);

            const timePercentage = (remainingTime / TOTAL_TIME_HOURS) * 100;
            const budgetPercentage = (remainingBudget / TOTAL_BUGET_MILLIONS) * 100;

            timeFillBar.style.width = `${timePercentage}%`;
            budgetFillBar.style.width = `${budgetPercentage}%`;

            // Change bar color based on remaining percentage (optional but nice)
            if (timePercentage < 20) {
                 timeFillBar.style.backgroundColor = var('--value-low'); // Red
            } else if (timePercentage < 50) {
                 timeFillBar.style.backgroundColor = var('--value-medium'); // Orange
            } else {
                 timeFillBar.style.backgroundColor = var('--value-high'); // Green/Teal
            }

             if (budgetPercentage < 20) {
                 budgetFillBar.style.backgroundColor = var('--value-low'); // Red
            } else if (budgetPercentage < 50) {
                 budgetFillBar.style.backgroundColor = var('--value-medium'); // Orange
            } else {
                 budgetFillBar.style.backgroundColor = var('--primary-color'); // Blue
            }


            // Disable/enable checkboxes based on remaining resources
            targetsContainer.querySelectorAll('.target-item').forEach(item => {
                 const checkbox = item.querySelector('input[type="checkbox"]');
                 const targetId = parseInt(checkbox.dataset.id);
                 const target = allTargets.find(t => t.id === targetId);

                 if (!selectedTargets.some(t => t.id === targetId)) { // Only check affordability for non-selected items
                     if (remainingTime < target.timeCost || remainingBudget < target.budgetCost) {
                         item.classList.add('disabled');
                         checkbox.disabled = true;
                     } else {
                         item.classList.remove('disabled');
                         checkbox.disabled = false;
                     }
                 } else {
                     // Selected items should not be disabled unless deselection logic is added which is more complex
                     // For this simple model, once selected, they stay selected until reset.
                     // Alternatively, if deselection is allowed, this logic needs adjustment.
                     // Let's stick to "select until resources run out, can deselect any time"
                     item.classList.remove('disabled'); // Selected items are never disabled
                     checkbox.disabled = false;
                 }
            });
        };

        // Render the list of targets
        const renderTargets = () => {
            targetsContainer.innerHTML = ''; // Clear current list
            allTargets.forEach(target => {
                const targetDiv = document.createElement('div');
                targetDiv.classList.add('target-item');
                targetDiv.dataset.id = target.id; // Add data-id to the div for easier selection handling

                let valueClass = '';
                if (target.scientificValue.includes('גבוה')) valueClass = 'value-high';
                else if (target.scientificValue.includes('בינוני')) valueClass = 'value-medium';
                else if (target.scientificValue.includes('נמוך')) valueClass = 'value-low';

                const urgencyClass = target.urgency === 'כן' ? 'urgency-yes' : '';
                const riskClass = target.risk === 'גבוה' ? 'risk-high' : (target.risk === 'נמוך' ? 'risk-low' : '');


                targetDiv.innerHTML = `
                    <h4>${target.name}</h4>
                    <p><strong>ערך מדעי:</strong> <span class="${valueClass}">${target.scientificValue}</span></p>
                    <p><strong>זמן נדרש:</strong> ${target.timeCost} שעות</p>
                    <p><strong>תקציב נדרש:</strong> ${target.budgetCost.toFixed(1)} מיליון דולר</p>
                    <p class="${urgencyClass}"><strong>דחיפות:</strong> ${target.urgency}</p>
                    <p class="${riskClass}"><strong>סיכון:</strong> ${target.risk}</p>
                     <label class="checkbox-container">בחר
                         <input type="checkbox" data-id="${target.id}">
                         <span class="checkmark"></span>
                     </label>
                `;

                // Add event listener to the whole target div, not just the checkbox
                targetDiv.addEventListener('click', handleTargetSelectionClick);


                targetsContainer.appendChild(targetDiv);
            });
        };

         // Handle click on the target item div
         const handleTargetSelectionClick = (event) => {
             const targetDiv = event.currentTarget; // Get the div that was clicked
             const checkbox = targetDiv.querySelector('input[type="checkbox"]');

             // If the div is disabled, do nothing
             if (targetDiv.classList.contains('disabled')) {
                 return;
             }

             // Manually toggle the checkbox state
             checkbox.checked = !checkbox.checked;

             // Trigger the change event on the checkbox to run the logic
             const changeEvent = new Event('change');
             checkbox.dispatchEvent(changeEvent);
         };


        // Handle checkbox change (triggered by the click handler)
        const handleTargetSelection = (event) => {
            const checkbox = event.target;
            const targetId = parseInt(checkbox.dataset.id);
            const target = allTargets.find(t => t.id === targetId);
            const targetDiv = checkbox.closest('.target-item'); // Get the parent div

            if (checkbox.checked) {
                 // Check if resources are sufficient *before* deducting (redundant due to disabled class, but safe)
                 if (remainingTime >= target.timeCost && remainingBudget >= target.budgetCost) {
                    remainingTime -= target.timeCost;
                    remainingBudget -= target.budgetCost;
                    selectedTargets.push(target);
                    targetDiv.classList.add('selected'); // Add selected class for styling/animation
                    updateResourceDisplay();
                    // After selecting, re-evaluate disabled status of *all* targets
                     updateTargetDisabledStates();
                } else {
                    // This case should ideally not happen if disabled class works, but handle as fallback
                    checkbox.checked = false; // Revert state
                     targetDiv.classList.remove('selected');
                    // alert('אין מספיק זמן טלסקופ או תקציב למטרה זו!'); // Remove alert for smoother UX
                }
            } else {
                // Deselecting
                remainingTime += target.timeCost;
                remainingBudget += target.budgetCost;
                selectedTargets = selectedTargets.filter(t => t.id !== targetId);
                 targetDiv.classList.remove('selected'); // Remove selected class
                updateResourceDisplay();
                 // After deselecting, re-evaluate disabled status of *all* targets
                 updateTargetDisabledStates();
            }
        };

         // Function to update disabled state of all targets based on current resources
         const updateTargetDisabledStates = () => {
             targetsContainer.querySelectorAll('.target-item').forEach(item => {
                 const checkbox = item.querySelector('input[type="checkbox"]');
                 const targetId = parseInt(checkbox.dataset.id);
                 const target = allTargets.find(t => t.id === targetId);

                 // If the target is NOT currently selected, check if it's affordable
                 if (!selectedTargets.some(t => t.id === targetId)) {
                     if (remainingTime < target.timeCost || remainingBudget < target.budgetCost) {
                         item.classList.add('disabled');
                         checkbox.disabled = true;
                     } else {
                         item.classList.remove('disabled');
                         checkbox.disabled = false;
                     }
                 } else {
                     // If it IS selected, it's never disabled (can always deselect)
                     item.classList.remove('disabled');
                     checkbox.disabled = false; // Ensure checkbox is enabled for selected items
                 }
             });
         };


        // Handle Submit Plan button click
        const handleSubmitPlan = () => {
            let totalValue = 0;
            let usedTime = TOTAL_TIME_HOURS - remainingTime;
            let usedBudget = TOTAL_BUGET_MILLIONS - remainingBudget;

            selectedTargets.forEach(target => {
                 totalValue += valueScores[target.scientificValue] || 0;
            });

            totalScientificValueEl.textContent = totalValue;
            usedTimeEl.textContent = usedTime.toFixed(1);
            usedBudgetEl.textContent = usedBudget.toFixed(1);

             // List selected target names
             selectedTargetsNamesEl.innerHTML = selectedTargets.map(target => `<li>${target.name}</li>`).join('');
             if (selectedTargets.length === 0) {
                 selectedTargetsNamesEl.innerHTML = '<li>לא נבחרו מטרות.</li>';
             }


            let feedbackText = '';
            let feedbackClass = ''; // To change color/style of feedback

            // Basic validation (shouldn't be needed if JS logic is perfect, but good)
             if (usedTime > TOTAL_TIME_HOURS + 0.01 || usedBudget > TOTAL_BUGET_MILLIONS + 0.01) { // Add small tolerance for float math
                 feedbackText += "<strong>שגיאה: חרגת ממגבלות המשאבים! נא לתקן את התוכנית.</strong><br>";
                 feedbackClass = 'value-low'; // Red feedback
             } else if (selectedTargets.length === 0) {
                 feedbackText = '<strong>לא נבחרו מטרות. לא הושגה תפוקה מדעית.</strong>';
                 feedbackClass = 'value-low';
             }
             else {
                 // More nuanced feedback based on value and resource usage
                 const timeUtilization = usedTime / TOTAL_TIME_HOURS;
                 const budgetUtilization = usedBudget / TOTAL_BUGET_MILLIONS;
                 const resourceUtilization = (timeUtilization + budgetUtilization) / 2; // Average utilization


                if (totalValue >= 60 && resourceUtilization > 0.8) { // High value, high utilization
                     feedbackText = '<strong>תוכנית מצוינת ובעלת תפוקה מדעית גבוהה מאוד! ניצלת את המשאבים ביעילות שיא.</strong>';
                     feedbackClass = 'value-high';
                } else if (totalValue >= 40 && resourceUtilization > 0.7) { // Good value, good utilization
                     feedbackText = '<strong>תוכנית טובה מאוד! השגת תפוקה מדעית משמעותית וניצלת את רוב המשאבים.</strong>';
                     feedbackClass = 'value-high';
                } else if (totalValue >= 25) { // Decent value
                     feedbackText = '<strong>תוכנית טובה. השגת תפוקה מדעית סבירה.</strong>';
                     feedbackClass = 'value-medium';
                } else { // Low value
                     feedbackText = '<strong>התפוקה המדעית נמוכה. נסה לבחור מטרות בעלות פוטנציאל מדעי גבוה יותר.</strong>';
                      feedbackClass = 'value-low';
                }

                 if (remainingTime > TOTAL_TIME_HOURS * 0.2 || remainingBudget > TOTAL_BUGET_MILLIONS * 0.2) { // Significant resources left
                     feedbackText += '<br><strong>שים לב: נותרו לך משאבים משמעותיים שלא נוצלו. אולי יכולת לבחור מטרות נוספות כדי להגדיל את התפוקה?</strong>';
                      if (feedbackClass !== 'value-low') feedbackClass = 'value-medium'; // Change color if not already red
                 } else if (resourceUtilization < 0.99 && totalValue < 60) { // Minor resources left, but not peak performance
                     feedbackText += '<br><strong>ניצול המשאבים היה די יעיל.</strong>';
                 }
                 // If utilization is ~100% and value is high, the first "מצוינת" message covers it.
             }


            feedbackEl.innerHTML = feedbackText;
            feedbackEl.className = 'feedback-message'; // Reset classes first
            feedbackEl.classList.add(feedbackClass); // Add class for color


            resultsDiv.classList.remove('hidden'); // Show results
            resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' }); // Scroll to results
        };

         // Reset the plan
         const resetPlan = () => {
             remainingTime = TOTAL_TIME_HOURS;
             remainingBudget = TOTAL_BUGET_MILLIONS;
             selectedTargets = [];
             updateResourceDisplay();
             // Uncheck all checkboxes and remove 'selected' class
             targetsContainer.querySelectorAll('.target-item input[type="checkbox"]').forEach(checkbox => {
                 checkbox.checked = false;
                  checkbox.closest('.target-item').classList.remove('selected');
             });
             // Re-enable all targets
             targetsContainer.querySelectorAll('.target-item').forEach(item => {
                  item.classList.remove('disabled');
                  item.querySelector('input[type="checkbox"]').disabled = false;
             });
             resultsDiv.classList.add('hidden'); // Hide results
             feedbackEl.innerHTML = ''; // Clear feedback
              feedbackEl.className = 'feedback-message';
              selectedTargetsNamesEl.innerHTML = ''; // Clear selected list
             // Optional: scroll back to top or target list
             // document.getElementById('app').scrollIntoView({ behavior: 'smooth', block: 'start' });
         };

        // Handle explanation toggle
        const toggleExplanation = () => {
            explanationDiv.classList.toggle('hidden');
            if (!explanationDiv.classList.contains('hidden')) {
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        };


        // Event Listeners
        // Listen for the 'change' event on checkboxes inside the targets container
        targetsContainer.addEventListener('change', (event) => {
             if (event.target.type === 'checkbox') {
                 handleTargetSelection(event);
             }
        });
        submitButton.addEventListener('click', handleSubmitPlan);
        resetButton.addEventListener('click', resetPlan); // Add reset button listener
        toggleExplanationButton.addEventListener('click', toggleExplanation);

        // Initialize the application
        initializeApp();
    });
</script>