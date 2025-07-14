---
title: "משימה לחיפוש חיים: הירחים האוקייניים של צדק ושבתאי"
english_slug: life-search-mission-ocean-moons-jupiter-saturn
category: "מדעים מדויקים / אסטרונומיה"
tags: [אסטרוביולוגיה, חיפוש חיים, ירחים, צדק, שבתאי, משימות חלל]
---
# משימה לחיפוש חיים: הירחים האוקייניים של צדק ושבתאי

השאלה האולטימטיבית: האם אנחנו לבד ביקום? התשובה עשויה להיות קרובה מתמיד, חבויה מתחת למיליוני קילומטרים של קרח, על עולמות רחוקים וקפואים. הצטרפו אלינו למסע אל הירחים המסתוריים של צדק ושבתאי ותכננו את משימת החלל שלכם לחיפוש אחר עדויות חיים!

<div id="app" class="mission-simulator">
    <h2>מתכנני משימות, קבלו את האתגר!</h2>
    <p>עמדתם בבקרת איכות הטכנית – עכשיו שדרגו אותה לרמה גלקטית! בחרו את היעד המרתק ביותר, אספו את הכלים המדעיים הקריטיים, ותכננו את המשימה שלכם בתבונה כדי לעמוד במגבלות. מה תגלו במסע שלכם אל מעמקי הירחים הקפואים?</p>

    <div class="section target-select">
        <h3>בחר יעד למשימה:</h3>
        <div class="target-options">
            <label class="target-label" data-target="europa">
                <input type="radio" name="target" value="europa" checked>
                <span class="target-name">אירופה</span>
                <span class="target-description">ירח של צדק | אוקיינוס תת-קרח נרחב | קרינה חזקה | אתגר חדירה לקרח</span>
            </label>
            <label class="target-label" data-target="enceladus">
                <input type="radio" name="target" value="enceladus">
                <span class="target-name">אנסלדוס</span>
                <span class="target-description">ירח של שבתאי | אוקיינוס תת-קרח | גייזרים פעילים | קרינה נמוכה יחסית</span>
            </label>
        </div>
    </div>

    <div class="section tool-select">
        <h3>הרכב חבילת כלים מדעיים למשימה:</h3>
        <p class="section-description">לכל כלי עלות, משקל וזמן הפעלה. בחר בחכמה – משאבים מוגבלים!</p>
        <div class="tool-options">
             <label class="tool-label" data-tool="drill">
                <input type="checkbox" name="tool" value="drill">
                <span class="tool-name">מקדח קרח מתקדם</span>
                <span class="tool-details">עלות: 50 יח', משקל: 300 ק"ג, זמן: 1 שנה | <em>מפתח גישה לאוקיינוס</em></span>
            </label>
             <label class="tool-label" data-tool="submersible">
                <input type="checkbox" name="tool" value="submersible">
                <span class="tool-name">צוללת רובוטית אוטונומית</span>
                <span class="tool-details">עלות: 80 יח', משקל: 500 ק"ג, זמן: 2 שנים | <em>חקר מעמקי האוקיינוס (דורש מקדח)</em></span>
            </label>
            <label class="tool-label" data-tool="spectrometer">
                <input type="checkbox" name="tool" value="spectrometer">
                <span class="tool-name">ספקטרומטר רב-תכליתי</span>
                <span class="tool-details">עלות: 40 יח', משקל: 150 ק"ג, זמן: 0.5 שנה | <em>ניתוח הרכב כימי של חומרים</em></span>
            </label>
            <label class="tool-label" data-tool="biosignatures">
                <input type="checkbox" name="tool" value="biosignatures">
                <span class="tool-name">גלאי סימנים ביולוגיים</span>
                <span class="tool-details">עלות: 70 יח', משקל: 200 ק"ג, זמן: 1 שנה | <em>חיפוש מולקולות ועדויות לחיים (דורש גישה למים)</em></span>
            </label>
             <label class="tool-label" data-tool="camera">
                <input type="checkbox" name="tool" value="camera">
                <span class="tool-name">מצלמות וסנסורים למיפוי</span>
                <span class="tool-details">עלות: 20 יח', משקל: 50 ק"ג, זמן: 0.2 שנה | <em>צילום וניתוח פני השטח ופעילות גייזרים</em></span>
            </label>
        </div>
    </div>

    <div class="section constraints-summary">
        <h3>סיכום ודוח משימה:</h3>
        <div class="constraints-limits">
            <h4>מגבלות המשימה (לפי יעד):</h4>
            <p>תקציב מקסימלי: <span id="max-cost" class="limit-value"></span> יח'</p>
            <p>משקל מקסימלי: <span id="max-weight" class="limit-value"></span> ק"ג</p>
            <p>משך משימה מקסימלי: <span id="max-duration" class="limit-value"></span> שנים</p>
        </div>
        <div class="current-status">
             <h4>מצב המשימה הנוכחי:</h4>
            <p>עלות נוכחית: <span id="current-cost" class="status-value">0</span> יח'</p>
            <p>משקל נוכחי: <span id="current-weight" class="status-value">0</span> ק"ג</p>
            <p>משך משימה משוער: <span id="current-duration" class="status-value">0</span> שנים</p>
        </div>

    </div>

    <div id="constraint-warning" class="warning-message" style="display: none;">
        <p>המשימה חורגת מהמגבלות שהוגדרו ליעד זה. אנא התאם את בחירת הכלים.</p>
    </div>

    <button id="launch-button" class="action-button">שגר משימה!</button>

    <div class="section mission-results" id="results" style="display: none;">
        <h3>תוצאות המשימה:</h3>
        <div id="results-content"></div>
        <button id="reset-mission-button" class="action-button secondary-button">תכנן משימה חדשה</button>
    </div>
</div>

<button id="show-explanation-button" class="explanation-button">גלו עוד: מסע אל הירחים האוקייניים (הצג הסבר)</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <hr>
    <h2>מסע אל הירחים האוקייניים: המדע מאחורי החיפוש</h2>

    <div class="explanation-content">
        <h3>מה הופך ירח ל"מועמד" פוטנציאלי לחיים?</h3>
        <p>כדי שחיים, כפי שאנו מכירים אותם, יוכלו להתפתח ולהתקיים, נדרשים שלושה תנאים עיקריים:</p>
        <ul>
            <li><strong>מים נוזליים:</strong> מים הם הממס האולטימטיבי לתגובות הכימיות המזינות חיים. על ירחים קפואים, המים עשויים לשרוד במצב נוזלי עמוק מתחת לשכבת קרח עבה, מחוממים על ידי כוחות גאות עזים מכוכב הלכת הענק שסביבו הם חגים (חימום גאותי).</li>
            <li><strong>מקור אנרגיה:</strong> לא רק אור שמש! רחוק מהשמש, האנרגיה יכולה להגיע מפעילות גיאותרמית בליבת הירח, או מאנרגיה כימית המשתחררת מאינטראקציות בין מים לסלעים (כמו בפתחי הידרותרמיים בקרקעית האוקיינוסים שלנו).</li>
            <li><strong>מולקולות אורגניות:</strong> אבני הבניין של החיים, מולקולות מבוססות פחמן. אלו יכולות להגיע ממקורות חיצוניים (מטאוריטים, שביטים), להיווצר בתהליכים כימיים ספונטניים, או לנבוע מתוך הירח עצמו.</li>
        </ul>

        <h3>הכירו את הירחים: אירופה (צדק) ואנסלדוס (שבתאי)</h3>
        <p>שני הירחים האלה הם מועמדים מובילים במערכת השמש שלנו לחיפוש חיים מחוץ לכדור הארץ:</p>
        <ul>
            <li><strong>אירופה (ירח של צדק):</strong> משימות קודמות כמו גלילאו והאבל סיפקו עדויות חזקות לקיום אוקיינוס מים מלוחים עצום מתחת למעטפת הקרח החלקה. כוחות הגאות מצדק שומרים על האוקיינוס נוזלי ומחממים את פנים הירח. ישנן עדויות אפשריות (אם כי לא חד משמעיות כמו באנסלדוס) לגייזרים של מים הפורצים מהסדקים בקרח. האתגר העיקרי באירופה הוא שכבת הקרח העבה והקרינה העזה מצדק.</li>
            <li><strong>אנסלדוס (ירח של שבתאי):</strong> ירח קטן בהרבה מאירופה, אך משימת קאסיני גילתה שהוא פעיל בצורה מדהימה! גייזרים עצומים של מים, מולקולות אורגניות ואף חומרים מורכבים פורצים בקביעות מהקוטב הדרומי. גייזרים אלו מאפשרים לחקור את הרכב האוקיינוס התת-קרח ואת החומרים שבו מבלי לחדור את שכבת הקרח. ישנן גם עדויות אפשריות לפעילות הידרותרמית בקרקעית האוקיינוס, מה שמרמז על מקור אנרגיה משמעותי.</li>
        </ul>

        <h3>אתגרי המשימה הבין-כוכבית</h3>
        <p>תכנון משימה לחקר עולמות כה רחוקים וקפואים דורש התמודדות עם מכשולים עצומים:</p>
        <ul>
            <li><strong>מרחק עצום:</strong> מדובר במסעות של מיליוני ואף מיליארדי קילומטרים, האור והתקשורת איתם אורכים דקות ארוכות ושנים רבות למסע עצמו.</li>
            <li><strong>קרינה קיצונית:</strong> במיוחד באירופה, הקרבה לצדק הענק מציבה רמות קרינה גבוהות ביותר, הדורשות מיגון מסיבי למכשור ולחללית.</li>
            <li><strong>טמפרטורות קפאון:</strong> פני השטח של הירחים קפואים מאוד, דורש טכנולוגיה עמידה לתנאים קיצוניים.</li>
            <li><strong>גישה לאוקיינוס:</strong> הדרך הישירה ביותר לחיפוש חיים היא לחקור את המים עצמם. באירופה, זה דורש חדירה דרך עשרות קילומטרים של קרח קשה. באנסלדוס, הגייזרים מציעים מסלול עוקף.</li>
        </ul>

        <h3>כלים מדעיים למסע התת-קרח</h3>
        <p>הכלים שצפיתם בהם בסימולציה מייצגים טכנולוגיות עתידיות שיידרשו לחקר עולמות אלו:</p>
        <ul>
            <li><strong>מקדחים/קריובוטים:</strong> רכבים אוטונומיים שיכולים להתיך או לקדוח את דרכם דרך שכבות קרח עבות כדי להגיע למים.</li>
            <li><strong>צוללות אוטונומיות (Hydrobots):</strong> כלי רכב תת-ימיים שינווטו באוקיינוס התת-קרח, יאספו נתונים ודגימות מהמים ומקרקעית הים.</li>
            <li><strong>ספקטרומטרים:</strong> מנתחים את הרכב החומרים שנאספו – מינרלים, מלחות, מולקולות אורגניות.</li>
            <li><strong>גלאי סימנים ביולוגיים:</strong> מכשירים מתוחכמים הסורקים דגימות בחיפוש אחר מולקולות ספציפיות, מבנים או תהליכים המעידים על נוכחות חיים.</li>
             <li><strong>מצלמות מתקדמות וסנסורים:</strong> למיפוי פני השטח, זיהוי תופעות גיאולוגיות (כמו סדקים פעילים או גייזרים), ולבחירת אתרי נחיתה פוטנציאליים.</li>
        </ul>

        <h3>הקשר בין תקציב, טכנולוגיה ומדע</h3>
        <p>כפי שראיתם בסימולציה, כל משימת חלל היא פשרה. כלים מדעיים מתקדמים ויכולות טכנולוגיות חדשניות (כמו חדירה לקרח) הם יקרים, כבדים וגוזלים זמן פיתוח רב. תכנון המשימה מחייב את המדענים והמהנדסים להחליט מהן השאלות המדעיות החשובות ביותר שניתן לענות עליהן במסגרת המגבלות. לעיתים קרובות, משימות ראשונות נועדו רק לאסוף מידע בסיסי כדי לאפשר תכנון טוב יותר של משימות שאפתניות יותר בעתיד. הסימולציה המחישה את הדילמות המורכבות העומדות בפני מתכנני משימות אלו.</p>
    </div>
</div>

<style>
    /* General Styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right; /* Right-align text */
        background-color: #f0f4f8; /* Soft blue background */
        color: #333;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }
    h1 {
        color: #1a2e42; /* Dark blue */
        text-align: center;
        margin-bottom: 30px;
        font-size: 2.2em;
        position: relative;
    }
     h1::after {
        content: '';
        display: block;
        width: 80px;
        height: 4px;
        background-color: #007bff; /* Blue accent */
        margin: 10px auto 0;
        border-radius: 2px;
     }

    /* App / Simulator Styles */
    .mission-simulator {
        background: linear-gradient(to bottom, #ffffff, #eef4f8); /* Gradient white to soft blue */
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        border: 1px solid #dce4ec;
        animation: fadeIn 0.8s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .mission-simulator h2 {
        color: #1a2e42;
        text-align: center;
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    .mission-simulator p {
        text-align: center;
        margin-bottom: 30px;
        color: #555;
    }

    .section {
        margin-bottom: 25px;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #e0e6ed;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .section:hover {
         transform: translateY(-3px);
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
    }

    .section h3 {
        margin-top: 0;
        color: #33506e; /* Slightly darker blue */
        border-bottom: 2px solid #007bff; /* Blue accent line */
        padding-bottom: 12px;
        margin-bottom: 15px;
        font-size: 1.3em;
    }

     .section-description {
        font-size: 0.95em;
        color: #666;
        margin-top: -10px;
        margin-bottom: 20px;
        text-align: right; /* Ensure description aligns with section title */
     }

    /* Target and Tool Specific Styles */
    .target-options, .tool-options {
        display: flex;
        flex-direction: column;
        gap: 15px; /* Space between options */
    }

    .target-label, .tool-label {
        display: block;
        padding: 15px;
        border: 1px solid #cce0f4; /* Light blue border */
        border-radius: 8px;
        background-color: #f8fcff; /* Very light blue */
        cursor: pointer;
        transition: background-color 0.3s ease, border-color 0.3s ease;
        position: relative;
        overflow: hidden; /* For checkmark */
    }

    .target-label:hover, .tool-label:hover:not(.disabled) {
        background-color: #eef7ff; /* Lighter blue on hover */
        border-color: #a0c8f4; /* Slightly darker blue border */
    }

    .tool-label.disabled {
        opacity: 0.6;
        cursor: not-allowed;
        background-color: #f0f0f0; /* Grey out disabled tools */
        border-color: #ddd;
    }

    .target-label input[type="radio"], .tool-label input[type="checkbox"] {
        margin-left: 10px; /* Space after input */
        vertical-align: middle;
        transform: scale(1.2); /* Slightly larger input */
         /* Hide default input and style it visually */
        position: absolute;
        opacity: 0;
        cursor: pointer;
        height: 100%;
        width: 100%;
        top: 0;
        right: 0; /* Position correctly for RTL */
        z-index: 1; /* Make it clickable */
    }

    /* Custom Checkbox/Radio Appearance (Optional, but enhances design) */
     .target-label input[type="radio"] + .target-name::before,
     .tool-label input[type="checkbox"] + .tool-name::before {
         content: '';
         display: inline-block;
         width: 18px;
         height: 18px;
         margin-left: 10px; /* Space after custom control */
         vertical-align: middle;
         border: 2px solid #007bff;
         border-radius: 4px; /* Slightly rounded corners */
         background-color: #fff;
         transition: all 0.2s ease;
     }

     .target-label input[type="radio"] + .target-name::before {
        border-radius: 50%; /* Circle for radio */
     }

     .target-label input[type="radio"]:checked + .target-name::before,
     .tool-label input[type="checkbox"]:checked + .tool-name::before {
         background-color: #007bff;
         border-color: #0056b3;
     }

     .tool-label input[type="checkbox"]:checked + .tool-name::after {
        /* Custom checkmark */
        content: '\2713'; /* Unicode checkmark */
        font-size: 14px;
        color: #fff;
        position: absolute;
        top: 50%;
        right: calc(100% - 30px); /* Position checkmark inside custom box */
        transform: translateY(-50%);
        z-index: 2;
     }

     .target-label input[type="radio"]:checked + .target-name::after {
        /* Custom radio dot */
        content: '';
        display: block;
        width: 10px;
        height: 10px;
        background-color: #fff;
        border-radius: 50%;
         position: absolute;
        top: 50%;
        right: calc(100% - 26px); /* Position dot inside custom circle */
        transform: translateY(-50%);
        z-index: 2;
     }


    .target-name, .tool-name {
        font-weight: bold;
        color: #1a2e42;
        font-size: 1.1em;
        position: relative; /* Needed for custom checkbox/radio positioning */
        z-index: 0; /* Below the hidden input */
    }

    .target-description, .tool-details {
        display: block;
        font-size: 0.9em;
        color: #555;
        margin-top: 5px;
         position: relative; /* Needed for custom checkbox/radio positioning */
        z-index: 0; /* Below the hidden input */
    }

    /* Constraints and Status Styles */
    .constraints-summary {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 20px; /* Space between limit and status blocks */
        padding: 20px;
        background-color: #e9f2ff; /* Light blue background */
        border: 1px dashed #a0c8f4; /* Dashed border */
        border-radius: 8px;
    }

    .constraints-limits, .current-status {
        flex: 1; /* Allow blocks to grow */
        min-width: 250px; /* Ensure minimum width */
    }

    .constraints-summary h3 {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
         text-align: center;
         width: 100%; /* Make header take full width */
    }

     .constraints-summary h4 {
         color: #33506e;
         margin-top: 0;
         margin-bottom: 10px;
         font-size: 1.1em;
         text-align: center;
     }


    .limit-value, .status-value {
        font-weight: bold;
        color: #007bff;
    }

    /* Warning Message */
    .warning-message {
        background-color: #ffebee; /* Light red */
        color: #d32f2f; /* Dark red */
        border: 1px solid #ef9a9a; /* Red border */
        padding: 15px;
        border-radius: 8px;
        margin: 20px auto;
        text-align: center;
        font-weight: bold;
        animation: pulse 1s infinite alternate;
    }

    @keyframes pulse {
        from { transform: scale(1); opacity: 1; }
        to { transform: scale(1.02); opacity: 0.9; }
    }


    /* Buttons */
    .action-button {
        display: block;
        width: fit-content; /* Button fits content */
        margin: 20px auto; /* Center button */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #007bff; /* Blue */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
        font-weight: bold;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Blue shadow */
    }

    .action-button:hover:not(:disabled) {
        background-color: #0056b3; /* Darker blue */
        transform: translateY(-2px); /* Lift effect on hover */
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
    }

    .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
        transform: none;
    }

    .secondary-button {
        background-color: #6c757d; /* Grey */
        box-shadow: 0 4px 8px rgba(108, 117, 125, 0.3);
    }

     .secondary-button:hover:not(:disabled) {
        background-color: #545b62; /* Darker Grey */
        box-shadow: 0 6px 12px rgba(108, 117, 125, 0.4);
     }


    .explanation-button {
         display: block;
        width: fit-content; /* Button fits content */
        margin: 30px auto; /* Center button */
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #607d8b; /* Grey-blue */
        color: white;
        border: none;
        border-radius: 20px;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .explanation-button:hover {
        background-color: #455a64; /* Darker grey-blue */
         transform: translateY(-1px);
    }


    /* Results Section */
    .mission-results {
        margin-top: 30px;
        background-color: #e8f5e9; /* Light green for success/results */
        border: 1px solid #c8e6c9; /* Green border */
        padding: 25px;
        border-radius: 8px;
         box-shadow: 0 4px 12px rgba(0, 128, 0, 0.1);
         animation: slideInFromTop 0.5s ease-out;
    }

    @keyframes slideInFromTop {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }


    .mission-results h3 {
         color: #2e7d32; /* Dark green */
         border-bottom-color: #4caf50; /* Green accent */
         margin-bottom: 15px;
    }
     #results-content {
         margin-bottom: 20px;
     }

    #results-content ul {
        list-style-type: none; /* Remove default list style */
        padding: 0; /* Remove default padding */
        margin: 0;
    }
    #results-content li {
        background-color: #f1f8e9; /* Lighter green background for list items */
        border-left: 4px solid #81c784; /* Green left border */
        padding: 10px 15px;
        margin-bottom: 10px;
        border-radius: 4px;
        font-size: 1em;
        line-height: 1.5;
    }
     #results-content li strong {
         color: #1b5e20; /* Even darker green for emphasis */
     }


    /* Explanation Section */
    .explanation-section {
        margin-top: 40px;
        padding-top: 30px;
        border-top: 2px dashed #ccc;
        background-color: #fff;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    .explanation-section h2 {
        text-align: center;
        margin-bottom: 30px;
        color: #1a2e42;
         font-size: 2em;
    }

    .explanation-section h3 {
         color: #33506e;
         margin-top: 25px;
         margin-bottom: 15px;
         border-bottom: 1px solid #eee;
         padding-bottom: 8px;
         font-size: 1.2em;
    }

    .explanation-content ul {
        list-style-type: disc;
        margin-right: 25px; /* Adjust for RTL */
        margin-bottom: 15px;
        padding-right: 10px;
    }
     .explanation-content ul li {
        margin-bottom: 10px;
     }
    .explanation-content strong {
        color: #333;
    }

    hr {
        margin: 40px 0;
        border: 0;
        border-top: 1px solid #cfd8dc; /* Light grey */
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        body {
            padding: 15px;
        }
        h1 {
            font-size: 1.8em;
             margin-bottom: 20px;
        }
         h1::after {
            width: 60px;
         }
        .mission-simulator {
            padding: 20px;
        }
        .mission-simulator h2 {
            font-size: 1.5em;
             margin-bottom: 15px;
        }
        .section {
            padding: 15px;
        }
         .section h3 {
            font-size: 1.1em;
            padding-bottom: 8px;
         }
         .target-label, .tool-label {
             padding: 10px;
             font-size: 0.95em;
         }
         .tool-details, .target-description {
             font-size: 0.85em;
         }
        .constraints-summary {
            flex-direction: column;
            gap: 15px;
            padding: 15px;
        }
        .constraints-limits, .current-status {
             min-width: auto;
        }
        .action-button {
            padding: 10px 20px;
            font-size: 1em;
        }
        .explanation-button {
             padding: 8px 15px;
             font-size: 0.9em;
        }
        .explanation-section {
            padding: 20px;
             margin-top: 30px;
             padding-top: 20px;
        }
         .explanation-section h2 {
            font-size: 1.6em;
            margin-bottom: 20px;
         }
         .explanation-section h3 {
            font-size: 1.1em;
            margin-top: 20px;
         }
         #results-content li {
            padding: 8px 10px;
            margin-bottom: 8px;
            font-size: 0.95em;
         }
    }

</style>

<script>
    const tools = {
        drill: { cost: 50, weight: 300, duration: 1, requires: [], name: "מקדח קרח מתקדם" },
        submersible: { cost: 80, weight: 500, duration: 2, requires: ['drill'], name: "צוללת רובוטית אוטונומית" },
        spectrometer: { cost: 40, weight: 150, duration: 0.5, requires: [], name: "ספקטרומטר רב-תכליתי" },
        biosignatures: { cost: 70, weight: 200, duration: 1, requires: ['drill'], name: "גלאי סימנים ביולוגיים" }, // Requires drill for water access in this simulation model
        camera: { cost: 20, weight: 50, duration: 0.2, requires: [], name: "מצלמות וסנסורים למיפוי" }
    };

    const constraints = {
        europa: { cost: 500, weight: 2000, duration: 4, name: "אירופה" },
        enceladus: { cost: 400, weight: 1500, duration: 3, name: "אנסלדוס" } // Slightly lower constraints for smaller moon/mission scope illustration
    };

    const targetRadios = document.querySelectorAll('input[name="target"]');
    const toolCheckboxes = document.querySelectorAll('input[name="tool"]');
    const maxCostSpan = document.getElementById('max-cost');
    const maxWeightSpan = document.getElementById('max-weight');
    const maxDurationSpan = document.getElementById('max-duration');
    const currentCostSpan = document.getElementById('current-cost');
    const currentWeightSpan = document.getElementById('current-weight');
    const currentDurationSpan = document.getElementById('current-duration');
    const launchButton = document.getElementById('launch-button');
    const constraintWarning = document.getElementById('constraint-warning');
    const resultsDiv = document.getElementById('results');
    const resultsContentDiv = document.getElementById('results-content');
    const explanationDiv = document.getElementById('explanation');
    const showExplanationButton = document.getElementById('show-explanation-button');
    const resetMissionButton = document.getElementById('reset-mission-button'); // Added reset button

    let currentTarget = 'europa'; // Default target

    // Function to update displayed constraints based on selected target
    function updateConstraintsDisplay() {
        const targetConstraints = constraints[currentTarget];
        maxCostSpan.textContent = targetConstraints.cost;
        maxWeightSpan.textContent = targetConstraints.weight;
        maxDurationSpan.textContent = targetConstraints.duration;
    }

    // Function to update current totals based on selected tools
    function updateTotals() {
        let totalCost = 0;
        let totalWeight = 0;
        let totalDuration = 0;
        const selectedTools = Array.from(toolCheckboxes).filter(cb => cb.checked).map(cb => cb.value);

        selectedTools.forEach(toolName => {
            const tool = tools[toolName];
            totalCost += tool.cost;
            totalWeight += tool.weight;
            totalDuration += tool.duration;
        });

        currentCostSpan.textContent = totalCost;
        currentWeightSpan.textContent = totalWeight;
        currentDurationSpan.textContent = totalDuration;

        // Visually indicate if limits are exceeded
        const targetConstraints = constraints[currentTarget];
        currentCostSpan.style.color = totalCost > targetConstraints.cost ? 'red' : '#007bff';
        currentWeightSpan.style.color = totalWeight > targetConstraints.weight ? 'red' : '#007bff';
        currentDurationSpan.style.color = totalDuration > targetConstraints.duration ? 'red' : '#007bff';


        checkConstraints(totalCost, totalWeight, totalDuration);
        updateToolDependencies(selectedTools); // Check and update dependencies
    }

    // Function to check if constraints are met and enable/disable launch button
    function checkConstraints(cost, weight, duration) {
        const targetConstraints = constraints[currentTarget];
        const isOver = cost > targetConstraints.cost || weight > targetConstraints.weight || duration > targetConstraints.duration;

        constraintWarning.style.display = isOver ? 'block' : 'none';
        launchButton.disabled = isOver;
        launchButton.textContent = isOver ? 'חריגה ממגבלות' : 'שגר משימה!';
    }

    // Function to handle tool dependencies (e.g., submersible requires drill)
    function updateToolDependencies(selectedTools) {
        toolCheckboxes.forEach(checkbox => {
            const toolName = checkbox.value;
            const tool = tools[toolName];
            const toolLabel = checkbox.parentElement;

            let canEnable = true; // Assume tool can be enabled by default

            if (tool.requires && tool.requires.length > 0) {
                // Check if all required tools are currently selected
                const hasRequired = tool.requires.every(requiredToolName => selectedTools.includes(requiredToolName));

                if (!hasRequired) {
                    canEnable = false;
                }

                 // If tool is checked but a dependency is now missing (e.g., unchecking drill unchecks submersible)
                if (!hasRequired && checkbox.checked) {
                    checkbox.checked = false; // Uncheck the dependent tool
                    // We will call updateTotals again outside this loop if any tool was unchecked
                }
            }

             // Visually disable/enable the label and input
             if (!canEnable) {
                 checkbox.disabled = true;
                 toolLabel.classList.add('disabled');
             } else {
                 checkbox.disabled = false;
                  toolLabel.classList.remove('disabled');
             }
        });
         // Re-check totals and dependencies after any potential unchecks
         updateTotals();
    }


    // Function to simulate mission launch and display results
    function launchMission() {
        const selectedTools = Array.from(toolCheckboxes).filter(cb => cb.checked).map(cb => cb.value);
        const targetName = constraints[currentTarget].name;

        let resultsHtml = `<h4>דוח משימה ליעד: ${targetName}</h4>`;
        resultsHtml += '<ul>';

        if (selectedTools.length === 0) {
            resultsHtml += '<li><strong>סטטוס:</strong> המשימה שוגרה ללא כלים מדעיים. לא ניתן היה לאסוף נתונים או לחפש סימנים לחיים.</li>';
        } else {
             resultsHtml += `<li><strong>כלים שנשלחו:</strong> ${selectedTools.map(toolName => tools[toolName].name).join(', ')}.</li>`;

             // Interpret findings based on selected tools and target
             let accessToWater = selectedTools.includes('drill');
             let analyzedGeysers = currentTarget === 'enceladus' && selectedTools.includes('camera') && selectedTools.includes('spectrometer');
             let directOceanExploration = selectedTools.includes('drill') && selectedTools.includes('submersible');
             let performedChemicalAnalysis = selectedTools.includes('spectrometer') && (accessToWater || analyzedGeysers || selectedTools.includes('camera')); // Spectrometer can analyze surface/geysers or water if accessed
             let searchedBiosignatures = selectedTools.includes('biosignatures'); // Requires drill in this simulation


             if (!accessToWater && !analyzedGeysers) {
                  // Case: No access to water or geyser analysis (only camera/spectrometer on surface)
                 resultsHtml += '<li><strong>ממצאים עיקריים:</strong> המשימה מיפתה את פני השטח ואספה מידע כללי. ללא גישה למים או יכולת ניתוח מעמיקה, לא ניתן להעריך את פוטנציאל החיים התת-קרח.</li>';
             } else {
                  if (accessToWater) {
                      resultsHtml += '<li><strong>ממצאים עיקריים:</strong> המשימה חדרה את שכבת הקרח וסיפקה גישה ישירה לסביבת האוקיינוס התת-קרח!</li>';
                       if (directOceanExploration) {
                           resultsHtml += '<li>- הצוללת הרובוטית חקרה את מעמקי האוקיינוס, סיפקה נתונים על טמפרטורה, לחץ, וזרימות תת-ימיות.</li>';
                       }
                       if (performedChemicalAnalysis) {
                            resultsHtml += '<li>- הספקטרומטר ניתח את הרכב המים, זיהה מלחים, מינרלים, ואולי מולקולות אורגניות פשוטות.</li>';
                       }
                       if (searchedBiosignatures) {
                            resultsHtml += '<li>- גלאי הסימנים הביולוגיים סרק את דגימות המים בחיפוש אחר עדויות מובהקות לחיים (מולקולות מורכבות, יחסים איזוטופיים).</li>';
                       }
                  } else if (analyzedGeysers) { // Case: Enceladus, camera + spec used for geysers
                       resultsHtml += '<li><strong>ממצאים עיקריים:</strong> המשימה טסה דרך גייזרים הפורצים מהירח. המצלמות סיפקו נתונים על מיקום וקצב הפריצה.</li>';
                       resultsHtml += '<li>- הספקטרומטר ניתח את הרכב החומרים בגייזרים, וזיהה מים, קרח, ומולקולות אורגניות שנפלטו מתוך האוקיינוס!</li>';
                        // Biosignatures detector requires drill in this sim, so it won't be listed as used here even if selected.
                        // The design decision was to make biosignatures/submersible require direct water access.
                        // If biosignatures was selected, the user *did* select drill, so the 'accessToWater' block above would run.
                        // This else-if (analyzedGeysers) block runs ONLY IF accessToWater is false (no drill).
                   }
             }


            // Add an overall conclusion based on tool combination and target
            let conclusion = "המשימה סיפקה מידע בסיסי אך לא הצליחה להעריך באופן משמעותי את פוטנציאל החיים ביעד זה.";

            if (searchedBiosignatures) { // Biosignatures require drill selected in this simulation
                if (directOceanExploration) {
                     conclusion = "<strong>המשימה השיגה גישה מלאה לאוקיינוס וחיפשה ישירות סימנים ביולוגיים! נדרש ניתוח נתונים מעמיק, אך הפוטנציאל לגילוי עדויות לחיים גבוה מתמיד!</strong>";
                 } else if (selectedTools.includes('drill') && selectedTools.includes('spectrometer') && selectedTools.includes('biosignatures')) {
                     conclusion = "<strong>המשימה השיגה גישה לאוקיינוס, ביצעה ניתוח כימי וחיפשה סימנים ביולוגיים. נאספו נתונים קריטיים שיאפשרו הערכה משמעותית של פוטנציאל החיים.</strong>";
                 } else {
                     // Biosignatures requires drill, so these cases are unlikely if logic works, but as fallback:
                      conclusion = "המשימה כללה גלאי סימנים ביולוגיים אך אולי לא כל הכלים הנחוצים לניתוח מלא או גישה מיטבית. הנתונים שנאספו חשובים אך דורשים השלמה.";
                 }
            } else if (accessToWater) { // Drill selected, but not biosignatures
                 if (directOceanExploration) {
                     conclusion = "המשימה חדרה לאוקיינוס וחקרה אותו עם צוללת. גיליתם פרטים על הסביבה הפיזית של האוקיינוס, אך לא חיפשתם סימנים ביולוגיים באופן ישיר.";
                 } else if (selectedTools.includes('drill') && selectedTools.includes('spectrometer')) {
                     conclusion = "המשימה חדרה לאוקיינוס וניתחה את הרכב המים. גיליתם פרטים על הכימיה של האוקיינוס, מידע חיוני להבנת הפוטנציאל לחיים.";
                 } else {
                     conclusion = "המשימה השיגה גישה לאוקיינוס, אך ללא כלים נוספים לניתוח או חקר, המידע שנאסף מוגבל.";
                 }
            } else if (analyzedGeysers) { // Enceladus, camera + spec, no drill
                 conclusion = "<strong>עבור אנסלדוס: ניתוח הגייזרים סיפק הצצה מדהימה אל תוך האוקיינוס התת-קרח וחשף נוכחות מולקולות אורגניות. נדרשת משימה עתידית עם יכולות חיפוש חיים ישירות יותר לאישור ממצאים.</strong>";
            } else if (selectedTools.includes('camera') || selectedTools.includes('spectrometer')) {
                 conclusion = "המשימה אספה מידע מפני השטח בלבד. נתונים על גיאולוגיה או הרכב פני השטח יכולים להיות רלוונטיים, אך לא ניתן להסיק מסקנות משמעותיות לגבי האוקיינוס או פוטנציאל החיים בו.";
             } else {
                 conclusion = "לא נבחרו כלים מדעיים שיאפשרו איסוף מידע משמעותי על היעד.";
             }

             resultsHtml += `<li><strong>סיכום המשימה:</strong> ${conclusion}</li>`;


        }

        resultsHtml += '</ul>';
        resultsContentDiv.innerHTML = resultsHtml;
        resultsDiv.style.display = 'block';
        launchButton.style.display = 'none'; // Hide launch button after launch
        resetMissionButton.style.display = 'block'; // Show reset button
        constraintWarning.style.display = 'none'; // Hide warning if it was visible
    }

    // Function to reset the simulation
    function resetMission() {
        // Uncheck all tool checkboxes
        toolCheckboxes.forEach(cb => {
            cb.checked = false;
            cb.parentElement.classList.remove('disabled'); // Ensure labels are not dim
            cb.disabled = false; // Ensure inputs are enabled
        });

        // Reset target to default (Europa) and update display
        document.querySelector('input[name="target"][value="europa"]').checked = true;
        currentTarget = 'europa';
        updateConstraintsDisplay();

        // Update totals and constraints (will be 0)
        updateTotals();

        // Hide results and show launch button
        resultsDiv.style.display = 'none';
        launchButton.style.display = 'block';
        resetMissionButton.style.display = 'none'; // Hide reset button

         // Re-enable launch button and reset text
        launchButton.disabled = false;
        launchButton.textContent = 'שגר משימה!';

        // Hide warning message
        constraintWarning.style.display = 'none';
    }


    // Event Listeners
    targetRadios.forEach(radio => {
        radio.addEventListener('change', (event) => {
            currentTarget = event.target.value;
            updateConstraintsDisplay();
            // Optional: Reset tools when target changes for a fresh start
            // toolCheckboxes.forEach(cb => cb.checked = false);
            updateTotals(); // Update totals based on new constraints
            resultsDiv.style.display = 'none'; // Hide results on target change
            launchButton.style.display = 'block'; // Ensure launch button is visible
            resetMissionButton.style.display = 'none'; // Hide reset button
            // Re-evaluate dependencies as constraints/target changed
             updateToolDependencies(Array.from(toolCheckboxes).filter(cb => cb.checked).map(cb => cb.value));
        });
    });

    toolCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateTotals); // updateTotals calls checkConstraints and updateToolDependencies
    });

    launchButton.addEventListener('click', launchMission);

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        // Simple fade toggle
        if (isHidden) {
            explanationDiv.style.display = 'block';
             explanationDiv.style.opacity = 0;
             let opacity = 0;
             const fadeInterval = setInterval(() => {
                 opacity += 0.1;
                 explanationDiv.style.opacity = opacity;
                 if (opacity >= 1) clearInterval(fadeInterval);
             }, 30);
        } else {
             explanationDiv.style.opacity = 1;
              let opacity = 1;
             const fadeInterval = setInterval(() => {
                 opacity -= 0.1;
                 explanationDiv.style.opacity = opacity;
                 if (opacity <= 0) {
                     explanationDiv.style.display = 'none';
                     clearInterval(fadeInterval);
                 }
             }, 30);
        }

        showExplanationButton.textContent = isHidden ? 'גלו עוד: מסע אל הירחים האוקייניים (הסתר הסבר)' : 'גלו עוד: מסע אל הירחים האוקייניים (הצג הסבר)';
    });

     resetMissionButton.addEventListener('click', resetMission);


    // Initial setup
    updateConstraintsDisplay();
    updateTotals(); // Calculate initial totals and check constraints
    updateToolDependencies([]); // Initialize dependencies based on no tools selected
    resetMissionButton.style.display = 'none'; // Hide reset button initially

    // Add hover effect class to labels (pure CSS handles actual hover)
    toolCheckboxes.forEach(checkbox => {
        checkbox.parentElement.classList.add('tool-label');
    });
     targetRadios.forEach(radio => {
        radio.parentElement.classList.add('target-label');
    });

</script>