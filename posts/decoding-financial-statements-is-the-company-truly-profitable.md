---
title: "פענוח דוחות כספיים: הצלילה העמוקה אל המספרים"
english_slug: decoding-financial-statements-is-the-company-truly-profitable
category: "מדעי החברה / כלכלה ופיננסים"
tags: [דוחות כספיים, מאזן, דוח רווח והפסד, תזרים מזומנים, ניתוח פיננסי]
---
# פענוח דוחות כספיים: הצלילה העמוקה אל המספרים

חברה מכריזה על רווחי שיא, הכותרות מהללות, והמניה מטפסת לשחקים. האם זה באמת סימן לעסק יציב ומשגשג? או שאולי המספרים מסתירים משהו אחר? דוחות כספיים הם כמו רנטגן פיננסי - הם חושפים את התמונה האמיתית מתחת לפני השטח. בואו נצלול פנימה ונלמד לפענח אותם כמו בלשים פיננסיים!

<div id="app-container">
    <div id="scenario-description"></div>
    <div id="statements-container">
        <div class="statement" id="balance-sheet">
            <h3>מאזן</h3>
            <pre></pre>
        </div>
        <div class="statement" id="pnl-statement">
            <h3>דוח רווח והפסד</h3>
            <pre></pre>
        </div>
        <div class="statement" id="cashflow-statement">
            <h3>דוח תזרים מזומנים</h3>
            <pre></pre>
        </div>
    </div>
    <div id="question-area">
        <div id="question-text"></div>
        <div id="answer-choices"></div>
    </div>
    <div id="feedback-area"></div>
    <button id="next-scenario" class="nav-button" style="display: none;">תרחיש הבא</button>
    <button id="restart-app" class="nav-button" style="display: none;">התחל מחדש</button>
</div>

<style>
    /* Global Styles */
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Support Hebrew */
        text-align: right; /* Support Hebrew */
        background-color: #f4f7f6; /* Soft background */
        color: #333;
    }
    h1 {
        color: #003366; /* Darker blue */
        text-align: center;
        margin-bottom: 30px;
    }
    h3 {
        color: #0056b3; /* Medium blue */
        margin-top: 0;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    /* App Container */
    #app-container {
        border: 1px solid #ddd;
        padding: 25px;
        border-radius: 12px;
        background-color: #ffffff; /* White background for the app */
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
        margin: 20px auto; /* Center the app */
        max-width: 1000px; /* Limit max width */
    }

    #scenario-description {
        margin-bottom: 25px;
        font-weight: bold;
        font-size: 1.1em;
        color: #003366;
    }

    /* Statements Layout */
    #statements-container {
        display: flex;
        flex-wrap: wrap; /* Allow statements to wrap on smaller screens */
        gap: 25px; /* More space between statements */
        margin-bottom: 25px;
    }
    .statement {
        flex: 1; /* Allow statements to grow and shrink */
        min-width: 280px; /* Minimum width before wrapping */
        border: 1px solid #e0e0e0; /* Lighter border */
        padding: 20px;
        border-radius: 8px;
        background-color: #f9f9f9; /* Slightly off-white for contrast */
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        white-space: pre-wrap; /* Preserve formatting but wrap long lines */
        word-wrap: break-word;
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; /* Monospace for alignment */
        font-size: 0.95em;
        overflow-x: auto; /* Add scroll if content is too wide */
        line-height: 1.5;
    }
     .statement pre {
        margin: 0; /* Remove default pre margin */
     }

    /* Question Area */
    #question-area {
        margin-bottom: 25px;
        padding: 20px;
        border: 1px solid #b3e0ff;
        background-color: #e0f2ff; /* Light blue background */
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    #question-text {
        margin-bottom: 20px;
        font-weight: bold;
        font-size: 1.1em;
        color: #003366;
    }
    #answer-choices button {
        display: block; /* Each button on a new line */
        width: 100%; /* Full width */
        padding: 12px;
        margin-bottom: 10px;
        border: none; /* Remove default border */
        border-radius: 6px;
        background-color: #007bff; /* Primary blue */
        color: white;
        cursor: pointer;
        text-align: right; /* Align text to the right */
        font-size: 1em;
        transition: background-color 0.2s ease, transform 0.1s ease; /* Add transitions */
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    #answer-choices button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        transform: translateY(-1px); /* Subtle lift effect */
    }
    #answer-choices button:active {
         background-color: #003d7a; /* Even darker blue on click */
         transform: translateY(0); /* Press down effect */
    }
     #answer-choices button:disabled {
        opacity: 0.7;
        cursor: not-allowed;
        background-color: #cccccc; /* Grey out disabled buttons */
        box-shadow: none;
        transform: none;
    }

    /* Feedback Area */
    #feedback-area {
        margin-top: 25px;
        padding: 20px;
        border-radius: 8px;
        font-weight: bold;
        animation: fadeIn 0.5s ease-in-out; /* Simple fade in animation */
    }
    #feedback-area.correct {
        background-color: #d4edda; /* Light green */
        color: #155724; /* Dark green text */
        border: 1px solid #c3e6cb; /* Green border */
    }
    #feedback-area.incorrect {
        background-color: #f8d7da; /* Light red */
        color: #721c24; /* Dark red text */
        border: 1px solid #f5c6cb; /* Red border */
    }

    /* Navigation Buttons */
    .nav-button {
        padding: 12px 20px;
        margin-top: 15px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    button#next-scenario {
         background-color: #28a745; /* Green */
         color: white;
         margin-left: 10px; /* Add space between buttons if both visible */
    }
     button#next-scenario:hover {
         background-color: #218838; /* Darker green on hover */
         transform: translateY(-1px);
     }
     button#next-scenario:active {
          background-color: #1e7e34;
          transform: translateY(0);
     }

    button#restart-app {
        background-color: #dc3545; /* Red */
        color: white;
    }
    button#restart-app:hover {
        background-color: #c82333; /* Darker red on hover */
         transform: translateY(-1px);
    }
    button#restart-app:active {
         background-color: #bd2130;
         transform: translateY(0);
    }

    /* Explanation Toggle Button */
    button#toggle-explanation {
        display: block; /* Button on its own line */
        width: auto; /* Fit content */
        margin: 20px auto; /* Center the button */
        padding: 10px 20px;
        background-color: #17a2b8; /* Teal */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
     button#toggle-explanation:hover {
         background-color: #138496; /* Darker teal on hover */
         transform: translateY(-1px);
     }
     button#toggle-explanation:active {
          background-color: #117a8b;
          transform: translateY(0);
     }


    /* Explanation Area */
    #explanation {
        margin-top: 30px;
        padding: 30px;
        border: 1px solid #ddd;
        border-radius: 12px;
        background-color: #ffffff; /* White background */
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
        display: none; /* Hidden by default */
        max-width: 1000px; /* Limit max width */
        margin-left: auto;
        margin-right: auto;
    }
    #explanation h2 {
         color: #003366;
         margin-top: 0;
         margin-bottom: 20px;
    }
    #explanation h3 {
        color: #0056b3;
        margin-top: 25px;
        margin-bottom: 15px;
        border-bottom: 1px dashed #eee; /* Dashed border for sub-headings */
    }
    #explanation p, #explanation ul {
        color: #444;
    }
    #explanation ul {
        list-style: none; /* Remove default bullet points */
        padding: 0;
    }
     #explanation li {
        margin-bottom: 12px; /* More space between list items */
        padding-right: 25px; /* Space for potential custom bullet */
        position: relative;
     }
     #explanation li::before {
        content: "•"; /* Custom bullet point */
        color: #007bff; /* Blue bullet */
        font-weight: bold;
        display: inline-block;
        width: 1em; /* Space for the bullet */
        margin-right: 10px; /* Space between bullet and text */
        position: absolute;
        right: 0; /* Align bullet to the right */
        text-align: center;
        font-size: 1.2em;
        top: 0;
     }

    /* Simple Animation */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        body {
            padding: 15px;
        }
        #app-container, #explanation {
            padding: 20px;
        }
        #statements-container {
            flex-direction: column; /* Stack statements vertically */
            gap: 15px;
        }
        .statement {
             min-width: auto; /* Allow full width */
             padding: 15px;
        }
        #question-area {
            padding: 15px;
        }
        #answer-choices button {
            font-size: 0.9em;
            padding: 10px;
        }
         .nav-button, button#toggle-explanation {
             width: 100%; /* Full width on small screens */
             margin-left: 0;
             margin-bottom: 10px;
         }
          button#next-scenario + button#restart-app { /* Adjust spacing if both are visible */
              margin-top: 0; /* No extra margin if stacked */
          }
    }

</style>

<button id="toggle-explanation">הצג / הסתר הסבר מפורט</button>

<div id="explanation">
    <h2>פענוח המספרים: הקשרים הסודיים בין הדוחות</h2>
    <p>כדי להבין באמת את מצבה הפיננסי של חברה, אי אפשר להסתפק במבט שטח על דוח רווח והפסד בלבד. שלושת הדוחות הכספיים העיקריים - מאזן, דוח רווח והפסד, ודוח תזרים מזומנים - מספרים סיפור שלם, וניתוחם יחד חושף תובנות עמוקות.</p>

    <h3>שלושת הדוחות: תפקידים מרכזיים</h3>
    <ul>
        <li><strong>מאזן (Balance Sheet):</strong> זהו "צילום מצב" של החברה בנקודת זמן ספציפית. הוא מראה מה החברה **מחזיקה** (נכסים), מה היא **חייבת** (התחייבויות), ומה **שייך לבעלים** (הון עצמי). זכרו את משוואת הזהב: נכסים = התחייבויות + הון עצמי.</li>
        <li><strong>דוח רווח והפסד (Income Statement / P&L):</strong> זהו "סרטון" שמסכם את **הביצועים** של החברה לאורך **תקופת זמן**. הוא מפרט את ההכנסות, ההוצאות, ובשורה התחתונה - האם החברה הרוויחה או הפסידה בתקופה זו.</li>
        <li><strong>דוח תזרים מזומנים (Cash Flow Statement):</strong> זהו "דוח תנועה" שמראה **מאיפה הגיע הכסף ולאן הלך** בתקופת זמן נתונה. הוא עוקב רק אחר תנועות מזומנים בפועל ומחולק לפעילות שוטפת (מהעסק עצמו), השקעה (קנייה/מכירה של נכסים ארוכי טווח), ומימון (גיוס/פירעון חוב והון). זהו דוח קריטי כי רווחיות על הנייר לא תמיד משתווה למזומן בקופה!</li>
    </ul>

    <h3>הקשרים הקריטיים בין הדוחות:</h3>
    <ul>
        <li><strong>הרווח הנקי מגיע לדוח תזרים מזומנים:</strong> הרווח הנקי מדוח רווח והפסד הוא נקודת הפתיחה לחישוב התזרים מפעילות שוטפת בדוח תזרים מזומנים (בשיטה העקיפה). אבל מכאן מתחילות ההתאמות...</li>
        <li><strong>שינויים במאזן משפיעים על התזרים השוטף:</strong> סעיפים במאזן כמו חייבים, מלאי, וספקים, משקפים פעילות עסקית שאינה מיידית במזומן. גידול בחייבים (מכירה באשראי שטרם נגבה) או מלאי (קניית חומרי גלם/ייצור סחורה שטרם נמכרה) **מקטין** את התזרים השוטף ביחס לרווח הנקי. ירידה בהם **מגדילה** את התזרים. שינויים בספקים פועלים הפוך.</li>
        <li><strong>פעילות השקעה ומימון במאזן ובתזרים:</strong> רכישת רכוש קבוע מופיעה כתזרים שלילי בפעילות השקעה וגם מגדילה את הנכסים הלא שוטפים במאזן. גיוס הלוואה מופיע כתזרים חיובי בפעילות מימון ומגדיל את ההתחייבויות במאזן. תשלום דיבידנד מופיע כתזרים שלילי בפעילות מימון ומקטין את ההון העצמי (דרך רווחים כלואים) במאזן.</li>
        <li><strong>הרווחים הכלואים מקשרים P&L למאזן:</strong> הרווח הנקי (פחות דיבידנדים ששולמו) בסוף התקופה מתווסף לסעיף "רווחים כלואים" תחת ההון העצמי במאזן של סוף התקופה.</li>
    </ul>

    <h3>סימני אזהרה נפוצים (והקשרים שחושפים אותם):</h3>
    <ul>
        <li><strong>רווח נקי גבוה, תזרים שוטף נמוך או שלילי:</strong> לעיתים קרובות נובע מגידול משמעותי בחייבים (מכירות "על הנייר" שלא נגבו), הצטברות מלאי (שלא נמכר), או תשלום מראש של הוצאות גדולות. זהו סימן אזהרה קלאסי לבעיית נזילות פוטנציאלית, גם כשהחברה רווחית תיאורטית. שימו לב להתאמות לרווח הנקי בדוח תזרים מזומנים ולשינויים בסעיפי ההון החוזר במאזן.</li>
        <li><strong>רווח נקי גבוה מרווח תפעולי באופן קבוע:</strong> אם הרווח הנקי מנופח על ידי הכנסות "אחרות" (כמו רווחי השקעה חד פעמיים) לעומת הרווח מפעילות הליבה (רווח תפעולי), ייתכן שפעילות העסקית המרכזית אינה בריאה כפי שנראה ממבט ראשון. השוו את הרווח התפעולי והנקי בדוח רווח והפסד.</li>
        <li><strong>ירידה במזומנים לצד גידול בהתחייבויות שוטפות:</strong> מבט במאזן ובתזרים יחד יכול לחשוף שהחברה נאבקת לעמוד בהתחייבויותיה הקצרות, אולי נאלצת למכור נכסים שוטפים או לקחת הלוואות לטווח קצר רק כדי לשרוד.</li>
    </ul>
    <p>ניתוח פיננסי הוא שילוב של אומנות ומדע. היכולת לקשר בין שלושת הדוחות ולהבין מה כל מספר מסמל בהקשר הרחב של החברה היא המפתח להבחנה בין הצלחה אמיתית לקסמים חשבונאיים או קשיים נסתרים.</p>
</div>

<script>
    const scenarios = [
        {
            description: "<b>תרחיש 1: הרווח על הנייר מול המזומן בפועל.</b><br>החברה מדווחת על רווח נקי מרשים לשנה זו, שגרם לאופטימיות בשוק. אך האם הכסף באמת נכנס לקופה? מבט בדוחות האחרים חושף תמונה מעט שונה.",
            statements: {
                balanceSheet: `מאזן (נתונים נבחרים)
-------------------------
נכסים שוטפים:
  מזומנים:           50,000
  חייבים:          250,000 (+ עלייה משמעותית משנה קודמת)
  מלאי:            200,000 (+ עלייה משמעותית משנה קודמת)
  סה"כ נכסים שוטפים: 500,000

התחייבויות שוטפות:
  ספקים:            150,000
  סה"כ ה. שוטפות:    200,000

הון עצמי:          800,000`,
                pnlStatement: `דוח רווח והפסד
-------------------------
הכנסות:           1,500,000
עלות המכר:          (600,000)
רווח גולמי:          900,000
הוצאות תפעוליות:    (400,000)
רווח תפעולי:        500,000
הוצאות מימון:       ( 50,000)
רווח לפני מס:       450,000
הוצאות מס:          (100,000)
<b>רווח נקי:           350,000</b>`,
                cashflowStatement: `דוח תזרים מזומנים
-------------------------
תזרים מפעילות שוטפת:
  <b>רווח נקי:          350,000</b>
  (+/- התאמות):      <b>(400,000)</b> (בעיקר משינויים בחייבים ומלאי)
  <b>סה"כ תזרים שוטף:  ( 50,000)</b>

תזרים מפעילות השקעה:
  רכישת רכוש קבוע:  (100,000)
  סה"כ תזרים השקעה:(100,000)

תזרים מפעילות מימון:
  פירעון הלוואות:   ( 50,000)
  סה"כ תזרים מימון:( 50,000)

<b>שינוי במזומנים:    (200,000)</b>`
            },
            question: "החברה מציגה רווח נקי גבוה (350,000), אך יתרת המזומנים שלה ירדה משמעותית השנה (שינוי של 200,000-), והתזרים מפעילות שוטפת שלילי (50,000-). מהי הסיבה המרכזית לתזרים השוטף השלילי בפער כה גדול מהרווח הנקי, ומדוע מצב כזה עלול להיות מדאיג?",
            options: [
                "החברה השקיעה הרבה ברכוש קבוע. זה הוציא הרבה מזומנים, אבל זה סימן טוב לצמיחה עתידית, ולא קשור לרווח הנקי.",
                "החברה משלמת הרבה מסים והחזר הלוואות, מה שפוגע בתזרים המזומנים הכולל אך אינו בעיה בפעילות הליבה שיוצרת רווח.",
                "הרווח הנקי נובע ממכירות שעדיין לא נגבו (גידול בחייבים) או מהצטברות מלאי שלא נמכר. הפער בין הרווח לתזרים השוטף נובע מהתאמות שליליות משמעותיות. זה מדאיג כי עלול להעיד על בעיות גבייה/מכירה וליצור קשיי נזילות בפועל, למרות הרווח על הנייר.", // Correct
                "ההכנסות הגבוהות נובעות ממכירת נכסים פיננסיים ולא מפעילות עסקית רגילה."
            ],
            correctAnswerIndex: 2,
            feedback: {
                correct: "🎯 תשובה נכונה! בינגו! למרות הרווח הנקי הגבוה (350,000), התזרים מפעילות שוטפת הוא שלילי (50,000-). הפער הגדול נובע מהתאמות שליליות משמעותיות (400,000-). שימו לב במאזן: 'חייבים' ו'מלאי' עלו משמעותית לעומת שנה קודמת. זה אומר שהחברה רשמה הכנסות בדוח רווח והפסד על מכירות שטרם גבתה (חייבים גדלו), או שהשקיעה במלאי שטרם הפך למזומן. במילים פשוטות, הכסף לא נכנס לקופה למרות שהמכירות נרשמו. מצב כזה עלול לגרום לקשיי נזילות, כלומר קושי לשלם חשבונות, משכורות, או לספקים, גם כשהחברה רווחית על הנייר. זה בהחלט מדאיג אם הבעיה נמשכת.",
                incorrect: "❌ תשובה לא נכונה. בואו ננתח שוב. השקעה ברכוש קבוע (תזרים השקעה) והחזר הלוואות (תזרים מימון) אכן הוציאו מזומנים ותרמו לירידה הכוללת במזומנים, אך השאלה מתמקדת בפער בין <b>הרווח הנקי לתזרים מפעילות שוטפת</b>. פער זה נובע בעיקר מפעילות הליבה של החברה והדרך שבה הכנסות והוצאות הופכות למזומנים. במקרה הזה, הגידול בחייבים ובמלאי (ראו במאזן ובהתאמות בתזרים השוטף) הוא הגורם המרכזי לכך שהרווח הנקי לא הפך למזומן זמין. זוהי נקודה קריטית בהבנת בריאותה הפיננסית של החברה."
            }
        },
         {
            description: "<b>תרחיש 2: רווח יורד, תזרים מזומנים משתפר - פרדוקס?</b><br>החברה עברה תקופה קשה יותר מבחינת מכירות, והרווח הנקי ירד משמעותית לעומת שנה קודמת. האם הכל אבוד? מבט מעמיק יותר חושף נקודות אור מפתיעות.",
            statements: {
                balanceSheet: `מאזן (נתונים נבחרים)
-------------------------
נכסים שוטפים:
  מזומנים:          120,000 (+ עלייה משמעותית משנה קודמת)
  חייבים:           180,000 (- ירידה משנה קודמת)
  מלאי:             150,000 (- ירידה משנה קודמת)
  סה"כ נכסים שוטפים: 450,000

התחייבויות שוטפות:
  ספקים:            100,000 (- ירידה משנה קודמת)
  סה"כ ה. שוטפות:    150,000

הון עצמי:          750,000`,
                pnlStatement: `דוח רווח והפסד
-------------------------
הכנסות:           1,200,000 (- ירידה משמעותית משנה קודמת)
עלות המכר:          (550,000)
רווח גולמי:          650,000
הוצאות תפעוליות:    (450,000) (+ עלייה קלה משנה קודמת)
רווח תפעולי:        200,000 (- ירידה משמעותית משנה קודמת)
הוצאות מימון:       ( 40,000)
רווח לפני מס:       160,000
הוצאות מס:          ( 40,000)
<b>רווח נקי:           120,000</b> (- ירידה משמעותית משנה קודמת)`,
                cashflowStatement: `דוח תזרים מזומנים
-------------------------
תזרים מפעילות שוטפת:
  <b>רווח נקי:          120,000</b>
  (+/- התאמות):      <b>+130,000</b> (בעיקר משינויים בחייבים ומלאי)
  <b>סה"כ תזרים שוטף:   250,000</b>

תזרים מפעילות השקעה:
  מכירת רכוש קבוע:    30,000
  רכישת רכוש קבוע:  ( 70,000)
  סה"כ תזרים השקעה: ( 40,000)

תזרים מפעילות מימון:
  קבלת הלוואה:        80,000
  תשלום דיבידנד:    ( 50,000)
  סה"כ תזרים מימון:   30,000

<b>שינוי במזומנים:     240,000</b>`
            },
            question: "הרווח הנקי של החברה ירד משמעותית השנה. באופן מפתיע, יתרת המזומנים שלה דווקא גדלה בצורה מרשימה (שינוי של 240,000+), וגם התזרים מפעילות שוטפת גבוה מהרווח הנקי. כיצד ניתן להסביר זאת, והאם יש כאן סימן חיובי למרות הירידה ברווח?",
            options: [
                "לא, הירידה בהכנסות וברווח הנקי, יחד עם עלייה קלה בהוצאות התפעוליות, מצביעות על הידרדרות כללית ללא נקודות חיוביות אמיתיות.",
                "כן, המזומנים גדלו בעיקר כי החברה גייסה הלוואה גדולה, מה ששיפר את מצב הנזילות לטווח קצר.",
                "כן, למרות הירידה ברווחים על הנייר, החברה מצליחה לשפר משמעותית את ניהול ההון החוזר (חייבים, מלאי), כפי שמשתקף בהתאמות החיוביות הגדולות בתזרים המזומנים מפעילות שוטפת. זהו סימן חיובי לבריאות התפעולית והנזילות של החברה.", // Correct
                "כן, מכירת רכוש קבוע תרמה משמעותית למזומנים הפנויים, וזה מצביע על אופטימיות ורצון להתמקד בפעילות הליבה."
            ],
            correctAnswerIndex: 2,
            feedback: {
                correct: "🎯 תשובה נכונה! בדיוק! זה נכון שההכנסות והרווח הנקי ירדו (ראו דוח רווח והפסד). זהו אתגר עסקי. אבל שימו לב במאזן ובתזרים השוטף: 'חייבים' ו'מלאי' ירדו לעומת שנה קודמת, וההתאמות לרווח הנקי בתזרים השוטף הן חיוביות ומשמעותיות (130,000+), מה שדחף את התזרים השוטף הרבה מעל הרווח הנקי (250,000 לעומת 120,000). זה מצביע על כך שהחברה שיפרה את תהליכי הגבייה מלקוחות (חייבים ירדו) או הצליחה למכור מלאי ישן (מלאי ירד). במילים אחרות, היא ממירה את ההכנסות (ואפילו הכנסות עבר) למזומן ביעילות רבה יותר. זהו סימן חיובי חשוב ליכולת התפעולית שלה לייצר מזומנים, גם בתקופה של ירידה ברווחים.",
                incorrect: "❌ תשובה לא נכונה. גיוס הלוואה (פעילות מימון) ומכירת רכוש קבוע (פעילות השקעה) אכן השפיעו על יתרת המזומנים הכוללת, אך השאלה מתמקדת בסיבה לכך <b>שהתזרים מפעילות שוטפת</b> גבוה מהרווח הנקי, ולנקודות החיוביות בפעילות <b>העסקית והתפעולית</b> של החברה. הפער החיובי הגדול בין הרווח הנקי לתזרים השוטף נובע משיפור בניהול ההון החוזר (ראו במאזן וב'התאמות' בתזרים השוטף), וזוהי נקודה חיובית מהותית לגבי יכולת החברה לייצר מזומנים מפעילות הליבה שלה, למרות האטה בהכנסות וברווחים על הנייר."
            }
        },
        {
            description: "<b>תרחיש 3: חברת סטארט-אפ בצמיחה מהירה.</b><br>זוהי חברה צעירה שמשקיעה רבות בצמיחה, פיתוח ושיווק. מבט ראשון על דוח רווח והפסד עלול להבהיל, אך דוחות אחרים מספרים סיפור אחר.",
            statements: {
                balanceSheet: `מאזן (נתונים נבחרים)
-------------------------
נכסים שוטפים:
  <b>מזומנים:          500,000</b> (+ עלייה עצומה מגיוס)
  חייבים:           300,000 (+ עלייה משנה קודמת - מכירות גדלות אך טרם נגבו)
  מלאי:              50,000
  סה"כ נכסים שוטפים: 850,000

נכסים לא שוטפים:
  <b>רכוש קבוע נטו:     600,000</b> (+ עלייה משמעותית מהשקעה)
  סה"כ נכסים:      1,450,000

התחייבויות שוטפות:
  ספקים:            250,000 (+ עלייה משנה קודמת)
  סה"כ ה. שוטפות:    300,000

התחייבויות לא שוטפות:
  <b>הלוואות ארוכות:    400,000</b> (+ עלייה מגיוס)
  סה"כ ה. לא שוטפות: 400,000

הון עצמי:          <b>750,000</b> (+ עלייה משמעותית מגיוס הון)`,
                pnlStatement: `דוח רווח והפסד
-------------------------
הכנסות:             800,000 (+ צמיחה יפה לעומת שנה קודמת)
עלות המכר:          (400,000)
רווח גולמי:          400,000
הוצאות תפעוליות:    (550,000) (+ עלייה משמעותית - השקעה בשיווק, מחקר ופיתוח, גיוס עובדים)
<b>רווח תפעולי:       (150,000)</b> (הפסד תפעולי)
הוצאות מימון:       ( 20,000)
רווח לפני מס:      (170,000) (הפסד)
הוצאות מס:               0
<b>רווח נקי:          (170,000)</b> (הפסד נקי)`,
                cashflowStatement: `דוח תזרים מזומנים
-------------------------
תזרים מפעילות שוטפת:
  <b>רווח נקי:         (170,000)</b> (הפסד)
  (+/- התאמות):      +100,000 (בעיקר משינויים בחייבים וספקים)
  <b>סה"כ תזרים שוטף:  ( 70,000)</b> (תזרים שלילי)

תזרים מפעילות השקעה:
  <b>רכישת רכוש קבוע:  (300,000)</b> (השקעה גדולה בפיתוח/תשתיות)
  <b>סה"כ תזרים השקעה:(300,000)</b>

תזרים מפעילות מימון:
  <b>קבלת הלוואה:       400,000</b>
  <b>גיוס הון עצמי:     200,000</b>
  <b>סה"כ תזרים מימון:  600,000</b> (גיוס כספים משמעותי)

<b>שינוי במזומנים:     230,000</b> (עלייה משמעותית במזומנים!)`
            },
            question: "החברה הציגה הפסד נקי והפסד תפעולי משמעותיים השנה, וגם תזרים המזומנים מפעילות שוטפת היה שלילי. למרות זאת, יתרת המזומנים שלה גדלה באופן דרמטי. איך זה קורה, והאם המצב מעיד על כישלון או על שלב טבעי בחיי החברה?",
            options: [
                "המצב מעיד על כישלון. הפסד בכל החזיתות (רווח נקי, תפעולי, תזרים שוטף) הוא סימן ברור לכך שהמודל העסקי אינו עובד והחברה בדרך לפשיטת רגל.",
                "המזומנים גדלו בזכות רווחים גדולים מפעילות השקעה, כמו מכירת נכסים או השקעות פיננסיות מוצלחות.",
                "גידול המזומנים נובע כמעט כולו מפעילות מימון - החברה גייסה סכומים גדולים של חוב והון. למרות ההפסדים התפעוליים והתזרים השוטף השלילי, זהו מצב אופייני לחברה צעירה בצמיחה ששורפת מזומנים לצורך השקעה והתרחבות, ומממנת זאת באמצעות גיוסים חיצוניים. זה לא בהכרח כישלון, אלא שלב שדורש מעקב.", // Correct
                "הפסד הרווח הנקי קוזז על ידי שיפור דרמטי בגביית חייבים וניהול מלאי, מה שהפך את התזרים השוטף לחיובי מאוד וגרם לגידול במזומנים."
            ],
            correctAnswerIndex: 2,
            feedback: {
                correct: "🎯 תשובה נכונה! ניתוח מצוין! אכן, דוח רווח והפסד מראה הפסדים (גם תפעולי וגם נקי), וגם התזרים מפעילות שוטפת שלילי. אלה סימנים לכך שפעילות הליבה עדיין אינה רווחית ומייצרת שריפת מזומנים. אבל המפתח להבנת הגידול במזומנים טמון בדוח תזרים המזומנים, סעיף <b>פעילות מימון</b>. שם רואים בבירור שהחברה גייסה סכום עתק (600,000) גם באמצעות הלוואות וגם באמצעות מכירת מניות (גיוס הון עצמי). במקביל, סעיף <b>פעילות השקעה</b> מראה השקעה גדולה (300,000-) ברכוש קבוע (ראו גם במאזן). זהו פרופיל אופייני לסטארט-אפ או חברה צעירה שגוברת על הפסדים והשקעות על ידי גיוס כספים חיצוני במטרה לבנות עסק גדול ורווחי בעתיד. זהו שלב לגיטימי, אך הוא דורש אמון המשקיעים ויכולת להגיע לרווחיות בסופו של דבר.",
                incorrect: "❌ תשובה לא נכונה. בואו נסתכל שוב על דוח תזרים המזומנים. המזומנים גדלו בזכות סעיף <b>פעילות מימון</b>, לא השקעה רווחית (פעילות ההשקעה שלילית עקב רכישות). גם שיפור בגביית חייבים וניהול מלאי (התאמות בתזרים השוטף) לא הפך את התזרים השוטף לחיובי, הוא נשאר שלילי (70,000-). ההפסדים והתזרים השוטף השלילי אינם בהכרח כישלון עבור חברה צעירה שפועלת במודל של 'צמיחה תחילה, רווחיות אחר כך' ומצליחה לגייס את ההון הדרוש כדי לממן את השקעותיה ואת שריפת המזומנים בטווח הקצר."
            }
        }
        // Add more scenarios here following the same structure
    ];

    let currentScenarioIndex = 0;

    const scenarioDescriptionEl = document.getElementById('scenario-description');
    const balanceSheetEl = document.getElementById('balance-sheet').querySelector('pre');
    const pnlStatementEl = document.getElementById('pnl-statement').querySelector('pre');
    const cashflowStatementEl = document.getElementById('cashflow-statement').querySelector('pre');
    const questionTextEl = document.getElementById('question-text');
    const answerChoicesEl = document.getElementById('answer-choices');
    const feedbackAreaEl = document.getElementById('feedback-area');
    const nextScenarioBtn = document.getElementById('next-scenario');
    const restartAppBtn = document.getElementById('restart-app');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationEl = document.getElementById('explanation');

    function loadScenario(index) {
        if (index < 0 || index >= scenarios.length) {
            endQuiz();
            return;
        }

        const scenario = scenarios[index];

        scenarioDescriptionEl.innerHTML = scenario.description; // Use innerHTML for bold tags etc.
        balanceSheetEl.textContent = scenario.statements.balanceSheet;
        pnlStatementEl.textContent = scenario.statements.pnlStatement;
        cashflowStatementEl.textContent = scenario.statements.cashflowStatement;

        questionTextEl.textContent = scenario.question;
        answerChoicesEl.innerHTML = ''; // Clear previous choices
        scenario.options.forEach((option, i) => {
            const button = document.createElement('button');
            button.textContent = option;
            button.onclick = () => handleAnswer(i, scenario, button); // Pass the button element
            answerChoicesEl.appendChild(button);
        });

        feedbackAreaEl.textContent = ''; // Clear previous feedback
        feedbackAreaEl.className = ''; // Remove feedback classes
        nextScenarioBtn.style.display = 'none';
        restartAppBtn.style.display = 'none';
    }

    function handleAnswer(selectedIndex, scenario, selectedButton) {
        // Disable all buttons immediately upon clicking any button
        Array.from(answerChoicesEl.children).forEach(button => button.disabled = true);

        // Optional: Add a class to the selected button for visual feedback before showing correct/incorrect
        // This could be done with CSS pseudo-classes like :active but a persistent state might be better.
        // For this simple setup, disabling others is enough immediate feedback.

        feedbackAreaEl.textContent = ''; // Clear previous feedback


        if (selectedIndex === scenario.correctAnswerIndex) {
            feedbackAreaEl.innerHTML = scenario.feedback.correct; // Use innerHTML for potential formatting
            feedbackAreaEl.className = 'feedback-area correct'; // Add class for styling
             // Optional: Highlight correct answer button
             selectedButton.style.backgroundColor = '#28a745'; // Green
             selectedButton.style.borderColor = '#28a745';

            currentScenarioIndex++;
            if (currentScenarioIndex < scenarios.length) {
                nextScenarioBtn.style.display = 'block';
            } else {
                // Small delay before ending quiz to show feedback
                 setTimeout(endQuiz, 1500);
            }
        } else {
            feedbackAreaEl.innerHTML = scenario.feedback.incorrect; // Use innerHTML
            feedbackAreaEl.className = 'feedback-area incorrect'; // Add class for styling
            // Optional: Highlight incorrect answer button and maybe the correct one
             selectedButton.style.backgroundColor = '#dc3545'; // Red
             selectedButton.style.borderColor = '#dc3545';

             // Find and highlight the correct button
             const correctButton = answerChoicesEl.children[scenario.correctAnswerIndex];
             correctButton.style.backgroundColor = '#28a745'; // Green
             correctButton.style.borderColor = '#28a745';


             nextScenarioBtn.style.display = 'block'; // Still allow moving on after seeing feedback
        }
         // Always show restart if it was the last scenario, regardless of answer correctness
         if (currentScenarioIndex >= scenarios.length) {
             nextScenarioBtn.style.display = 'none'; // Hide next if finished
             restartAppBtn.style.display = 'block';
         }
    }

    function endQuiz() {
        scenarioDescriptionEl.innerHTML = "<b>סיימת את כל התרחישים!</b> 🎉";
         balanceSheetEl.textContent = '';
         pnlStatementEl.textContent = '';
         cashflowStatementEl.textContent = '';
        questionTextEl.textContent = "עכשיו אתה בלש דוחות מוסמך! מקווה שנהנית ולמדת כיצד לחבר את הנקודות בין הדוחות השונים כדי לקבל תמונה פיננסית שלמה.";
        answerChoicesEl.innerHTML = '';
        feedbackAreaEl.innerHTML = 'כל הכבוד על השלמת המשימה!';
        feedbackAreaEl.className = 'feedback-area correct'; // Green feedback for completion
        nextScenarioBtn.style.display = 'none';
        restartAppBtn.style.display = 'block';
         window.scrollTo({ top: document.getElementById('app-container').offsetTop, behavior: 'smooth' }); // Scroll to top of app
    }

    function restartQuiz() {
        currentScenarioIndex = 0;
        loadScenario(currentScenarioIndex);
        restartAppBtn.style.display = 'none';
         window.scrollTo({ top: document.getElementById('app-container').offsetTop, behavior: 'smooth' }); // Scroll to top of app
    }

    function toggleExplanation() {
        if (explanationEl.style.display === 'none' || explanationEl.style.display === '') {
            explanationEl.style.display = 'block';
             toggleExplanationBtn.textContent = 'הסתר הסבר מפורט';
             window.scrollTo({ top: toggleExplanationBtn.offsetTop - 20, behavior: 'smooth' }); // Scroll to explanation
        } else {
            explanationEl.style.display = 'none';
             toggleExplanationBtn.textContent = 'הצג / הסתר הסבר מפורט';
        }
    }

    nextScenarioBtn.onclick = () => loadScenario(currentScenarioIndex);
    restartAppBtn.onclick = restartQuiz;
    toggleExplanationBtn.onclick = toggleExplanation;


    // Initialize the app
    loadScenario(currentScenarioIndex);

</script>
---