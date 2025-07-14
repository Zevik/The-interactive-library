---
title: "מנהל החלל: סימולטור קבלת החלטות אסטרטגיות"
english_slug: space-manager-strategic-decision-simulator
category: "מיומנויות וחינוך / חשיבה ומחקר"
tags: קבלת החלטות, ניהול אסטרטגי, סיכון, הקצאת משאבים, תוכנית חלל, סימולציה אינטראקטיבית
---
<h1>מנהל החלל: סימולטור קבלת החלטות אסטרטגיות</h1>
<p>דמיינו לרגע שאתם ניצבים בראש תוכנית החלל הלאומית. כספי ציבור מוגבלים, שעון החול אוזל, והיקום כולו ממתין לתגליות שישנו את האנושות. שורה ארוכה של משימות חלל עתידניות מוצגות בפניכם – חלקן מבטיחות פריצות דרך מדעיות, אחרות פורצות גבולות טכנולוגיים, ויש כאלו שישבו את לב הציבור. לכל משימה מחיר, זמן פיתוח, רמת סיכון, ופוטנציאל תמורה משלה. המשימה שלכם: לבנות את פורטפוליו המשימות האופטימלי שיניב את ההצלחה המרבית במסגרת האילוצים הנתונים.</p>

<div id="app" class="space-manager-app">
    <h2>לוח הבקרה של מנהל החלל</h2>
    <p class="app-intro">בחר בקפידה את המשימות עבור תוכנית החלל שלך. עקוב אחר האילוצים והפוטנציאל הכולל לפני שאתה משיק!</p>

    <div class="dashboard-section constraints-box">
        <h3><i class="fas fa-sliders-h"></i> אילוצים זמינים</h3>
        <p>🚀 תקציב כולל: <span id="total-budget">100</span> מיליארד דולר</p>
        <p>⏳ זמן כולל: <span id="total-time">15</span> שנים</p>
    </div>

    <div class="dashboard-section missions-section">
        <h3><i class="fas fa-rocket"></i> משימות אפשריות</h3>
        <div class="missions-list-container">
            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th>משימה</th>
                        <th>עלות ($ מיליארד)</th>
                        <th>זמן (שנים)</th>
                        <th>סיכון</th>
                        <th>פוטנציאל מדעי</th>
                        <th>פוטנציאל טכנולוגי</th>
                        <th>פוטנציאל ציבורי</th>
                    </tr>
                </thead>
                <tbody id="missions-table-body">
                    <!-- Mission rows will be added by JS -->
                </tbody>
            </table>
        </div>
    </div>

    <div class="dashboard-section portfolio-summary-box">
        <h3><i class="fas fa-chart-pie"></i> הפורטפוליו הנבחר</h3>
        <p>💰 סה"כ עלות: <span id="selected-cost">0</span> מיליארד דולר</p>
        <p>⏱️ סה"כ זמן: <span id="selected-time">0</span> שנים</p>
        <p>⚠️ רמת סיכון כוללת: <span id="selected-risk">-</span></p>
        <p>🌟 סה"כ פוטנציאל משולב: <span id="selected-potential">0</span></p>
        <p id="constraint-status" class="status"><i class="fas fa-info-circle"></i> בחר משימות כדי להתחיל.</p>
         <button id="run-simulation" class="launch-button" disabled><i class="fas fa-play"></i> הרץ סימולציה</button>
    </div>

    <div id="simulation-results" class="dashboard-section results-box" style="display: none;">
        <h3><i class="fas fa-poll-h"></i> תוצאות שיגור המשימות</h3>
        <div class="simulation-progress">
             <div class="simulation-bar" id="simulation-progress-bar"></div>
        </div>
         <div id="simulation-details" class="mission-results-list">
            <!-- Simulation results per mission will be added here -->
         </div>
        <div class="final-scores">
            <p>💰 עלות כוללת שהושקעה: <span id="final-cost"></span> מיליארד דולר</p>
            <p>🔬 סה"כ נקודות מדע שהושגו: <span id="final-science"></span></p>
            <p>⚙️ סה"כ נקודות טכנולוגיה שהושגו: <span id="final-tech"></span></p>
            <p>📣 סה"כ נקודות ציבורי שהושגו: <span id="final-pr"></span></p>
        </div>
        <p id="simulation-feedback" class="feedback-message"></p>
    </div>
</div>

<button id="toggle-explanation" class="explanation-button"><i class="fas fa-book-open"></i> הצג הסבר: האמנות של קבלת החלטות אסטרטגיות</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2><i class="fas fa-graduation-cap"></i> הסבר: האמנות של קבלת החלטות תחת אילוצים</h2>

    <p class="intro-text">קבלת החלטות אסטרטגיות, במיוחד בתחומי מדע וטכנולוגיה מתקדמים כמו תוכניות חלל, היא מסע מורכב עתיר אי-ודאות, מגבלות משאבים (תקציב, זמן, כוח אדם), ומטרות שלעיתים סותרות זו את זו. הסימולטור הזה נועד להכניס אתכם לנעלי מקבלי ההחלטות ולהמחיש את האתגרים והעקרונות המנחים בתהליך גורלי זה.</p>

    <h3><i class="fas fa-compass"></i> מרכיבי ההחלטה</h3>
    <p>כל החלטה אסטרטגית מושכלת מתחילה במיפוי ברור של:</p>
    <ul>
        <li><strong>מטרות:</strong> לאן אנחנו שואפים להגיע? בתוכנית חלל, זה יכול להיות קידום ידע מדעי פורץ דרך, פיתוח יכולות טכנולוגיות עתידיות, חיזוק מעמדנו בזירה הבינלאומית, או גיוס תמיכה ציבורית רחבה.</li>
        <li><strong>חלופות:</strong> אילו דרכים פתוחות בפנינו? במקרה זה, אלו הן המשימות השונות שניתן לבחור. לכל משימה פרופיל ייחודי: עלות, משך זמן, רמת סיכון ופוטנציאל תמורה בתחומים שונים.</li>
        <li><strong>אילוצים:</strong> מה מגביל את חופש הפעולה שלנו? בדרך כלל אלו מגבלות תקציב ולוחות זמנים נוקשים, אך ייתכנו גם מגבלות טכנולוגיות קיימות או אילוצים פוליטיים.</li>
    </ul>
    <p>השלב הראשון הוא תמיד לאסוף את כל המידע הרלוונטי ולארגנו בצורה שתאפשר ראייה בהירה של התמונה המלאה.</p>

    <h3><i class="fas fa-exclamation-triangle"></i> הערכת סיכונים</h3>
    <p>סיכון הוא בן לוויה קבוע במסע לחלל. כל משימה נושאת בחובה סיכון מסוים – סיכון לכישלון טכני קריטי, סיכון לחריגה דרמטית מתקציב או לוח זמנים, או סיכון שהתוצאות המדעיות שיתקבלו יהיו פחותות מהמצופה. רמת הסיכון משפיעה באופן ישיר על סיכויי ההצלחה ועל התשואה הפוטנציאלית. משימות עם סיכון גבוה יכולות, אם יצליחו, להניב תמורה יוצאת דופן ופריצות דרך משמעותיות. אולם, אם ייכשלו, הן עלולות לגרום לאובדן מוחלט של המשאבים היקרים שהושקעו בהן.</p>

    <h3><i class="fas fa-balance-scale"></i> עקרון הטרייד-אוף</h3>
    <p>בעולם האמיתי, החלטות מושלמות כמעט ואינן קיימות. לרוב, אנו נדרשים לוותר על דבר מסוים כדי להשיג דבר אחר בעל חשיבות גדולה יותר. זוהי מהותו של הטרייד-אוף. למשל:</p>
    <ul>
        <li>פוטנציאל מדעי מרחיק לכת מול סיכון טכני גבוה במיוחד.</li>
        <li>בחירה במשימה מהירה וזולה יחסית, המבטיחה תוצאות סבירות בטווח הקצר, מול השקעה במשימה יקרה וארוכה יותר עם פוטנציאל לשינוי פרדיגמה.</li>
        <li>השקעה כבדה בפיתוח טכנולוגי בסיסי לטווח הארוך מול מיקוד במשימות עם תהודה ציבורית מיידית, המבטיחות תמיכה ומימון עתידי.</li>
    </ul>
    <p>הבנה עמוקה של אילו טרייד-אופים מתחייבים מהאילוצים והמטרות שלך היא קריטית לבניית פורטפוליו מוצלח.</p>

    <h3><i class="fas fa-boxes"></i> ניהול פורטפוליו</h3>
    <p>התבוננות בכל משימה בפני עצמה עלולה להוביל להחלטות לא אופטימליות ברמה הכוללת. ניהול פורטפוליו משמעותו ראיית כל המשימות הנבחרות כמקשה אחת. האם הפורטפוליו הכולל עומד בכל האילוצים? האם רמת הסיכון המצטברת סבירה ומפוזרת נכון? האם יש איזון בין סוגי המשימות השונים (מדע, טכנולוגיה, ציבורי) בהתאם למטרות הכלליות? גישה זו מאפשרת לפזר סיכונים, למקסם סינרגיות בין משימות שונות וליצור תוכנית כוללת שהיא יותר מסך חלקיה.</p>

    <h3><i class="fas fa-question-circle"></i> השפעת אי-ודאות</h3>
    <p>גם התוכנית המחושבת ביותר מתבצעת תחת ענן של אי-ודאות. טכנולוגיות חדשות עלולות להיכשל באופן בלתי צפוי, תקציבים ממשלתיים יכולים להשתנות, ואירועים חיצוניים דרמטיים (כמו אסונות טכניים או שינויים פוליטיים) עלולים לטרוף את הקלפים. הסימולציה ממחישה נקודה זו באמצעות מרכיב אקראי בהצלחה/כישלון של כל משימה, המבוסס על רמת הסיכון שלה. התוצאה הסופית אינה מובטחת מראש, וההימור המושכל שתעשו יבחן אל מול פני המציאות הלא צפויה.</p>

    <h3><i class="fas fa-lightbulb"></i> לקחים מהסימולטור</h3>
    <p>באמצעות הסימולטור, תוכלו לחוות באופן אקטיבי את האתגרים הכרוכים ב:</p>
    <ul>
        <li><strong>איזון:</strong> מציאת האיזון הנכון בין פוטנציאל תמורה גבוה לבין סיכון טכני או פיננסי.</li>
        <li><strong>הקצאה:</strong> הצורך להקצות משאבים יקרים ומוגבלים (כסף וזמן) בין שפע של הזדמנויות מתחרות.</li>
        <li><strong>אסטרטגיה:</strong> הבנה שפורטפוליו מאוזן, המשלב סוגי סיכונים ותמורות שונות, לעיתים קרובות עדיף על השקעה מרוכזת במשימות בודדות (גם אם הן בעלות פוטנציאל תאורטי גבוה מאוד).</li>
        <li><strong>התמודדות עם אי-ודאות:</strong> ההכרה שגם לאחר קבלת ההחלטות הטובה ביותר המבוססת על המידע הקיים, גורמים חיצוניים ואי-ודאות מובנית יכולים להשפיע באופן משמעותי על התוצאה הסופית.</li>
    </ul>
    <p>עקרונות אלו רלוונטיים לא רק לניהול תוכניות חלל שאפתניות, אלא גם לניהול עסקי, השקעות פיננסיות, תכנון פרויקטים מורכבים, ואף קבלת החלטות משמעותיות במסלול החיים האישי והמקצועי.</p>
</div>

<style>
    /* Importing a font for better aesthetics */
     @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');
     /* Font Awesome for icons (basic CDN) */
     @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');


    :root {
        --primary-color: #0056b3; /* Darker blue */
        --secondary-color: #e9f7ff; /* Light blue for boxes */
        --text-color: #333;
        --bg-color: #f0f4f8; /* Lighter background */
        --border-color: #ccc;
        --header-bg: #003366; /* Even darker blue */
        --success-color: #28a745; /* Green */
        --warning-color: #ffc107; /* Yellow/Orange */
        --error-color: #dc3545; /* Red */
        --risk-low: #28a745;
        --risk-medium: #ffc107;
        --risk-high: #dc3545;
    }

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: var(--bg-color);
        color: var(--text-color);
        direction: rtl;
        text-align: right;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: right;
        margin-bottom: 15px;
        font-weight: 700;
    }

    h1 {
        font-size: 2.2em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    h2 {
        font-size: 1.8em;
        color: var(--header-bg);
    }

    h3 {
         font-size: 1.3em;
         margin-bottom: 10px;
         color: var(--primary-color);
    }

     h3 i {
         margin-left: 8px; /* Space between icon and text */
         color: var(--header-bg);
     }

    #app, #explanation {
        background-color: #fff;
        padding: 30px;
        margin-bottom: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid var(--border-color);
    }

    .app-intro, .intro-text {
        font-size: 1.1em;
        margin-bottom: 25px;
        color: #555;
    }


    .dashboard-section {
        border: 1px solid var(--primary-color);
        padding: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        background-color: var(--secondary-color);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }


    .missions-list-container {
        max-height: 450px; /* Slightly taller */
        overflow-y: auto;
        margin-bottom: 15px;
        border-radius: 5px;
        border: 1px solid var(--border-color);
         background-color: #fff; /* White background for table area */
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 0; /* Remove top margin */
    }

    th, td {
        border: 1px solid #ddd;
        padding: 12px; /* More padding */
        text-align: right;
        vertical-align: middle; /* Center vertically */
         font-size: 0.95em;
    }

    th {
        background-color: var(--header-bg);
        color: white;
        position: sticky;
        top: 0;
        z-index: 2; /* Higher z-index */
        font-weight: 400; /* Lighter font weight */
    }

    tbody tr:nth-child(even) {
        background-color: #f8f8f8; /* Lighter stripe */
    }

    tbody tr:hover {
        background-color: #e0e9f3; /* Highlight on hover */
    }

    tbody tr.selected-mission {
         background-color: #cce5ff; /* Highlight selected row */
         font-weight: 700;
    }

    td:nth-child(5) { /* Risk column */
        font-weight: bold;
    }

    td:nth-child(5):contains('Low') { color: var(--risk-low); }
    td:nth-child(5):contains('Medium') { color: var(--risk-medium); }
    td:nth-child(5):contains('High') { color: var(--risk-high); }


    input[type="checkbox"] {
        margin-left: 8px;
        margin-right: 0;
        cursor: pointer;
        transform: scale(1.2); /* Slightly larger checkbox */
    }

    button {
        display: inline-flex; /* Allow icon and text */
        align-items: center; /* Vertically center content */
        background-color: var(--primary-color);
        color: white;
        padding: 12px 25px; /* More padding */
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1.05em;
        margin-top: 15px;
        margin-left: 10px;
        margin-right: 0;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
    }

    button i {
        margin-left: 8px;
    }

     .launch-button {
         background-color: var(--success-color);
         margin-top: 20px;
         font-size: 1.1em;
     }

     .launch-button:hover:not(:disabled) {
         background-color: #218838; /* Darker green */
         transform: translateY(-2px); /* Subtle hover effect */
     }

     .explanation-button {
         background-color: #6c757d; /* Grey */
     }
     .explanation-button:hover:not(:disabled) {
        background-color: #545b62; /* Darker grey */
        transform: translateY(-2px);
     }


    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
         transform: none;
    }

     button:hover:not(:disabled) {
        background-color: var(--primary-color); /* Default hover for main buttons */
    }

    .status {
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        margin-top: 15px;
         display: flex;
         align-items: center;
         font-size: 1.05em;
    }

    .status i {
        margin-left: 8px;
         font-size: 1.2em;
    }

    .status.ok {
        color: var(--success-color);
        background-color: #d4edda; /* Light green background */
        border: 1px solid #c3e6cb;
    }

    .status.warning {
        color: var(--warning-color);
        background-color: #fff3cd; /* Light yellow background */
        border: 1px solid #ffeeba;
    }

     .status.error {
        color: var(--error-color);
        background-color: #f8d7da; /* Light red background */
        border: 1px solid #f5c6cb;
    }

    /* Simulation Results Styling */
    .results-box {
         background-color: #e2f0fb; /* Different light blue for results */
         border-color: var(--header-bg);
    }

     .simulation-progress {
         width: 100%;
         height: 10px;
         background-color: #ddd;
         border-radius: 5px;
         margin-bottom: 20px;
         overflow: hidden;
     }

     .simulation-bar {
         width: 0%;
         height: 100%;
         background-color: var(--success-color);
         transition: width 0.5s ease-in-out;
     }


    .mission-results-list {
        margin-top: 15px;
        padding-top: 10px;
        border-top: 1px dashed var(--border-color);
    }

    #simulation-details p {
        margin-bottom: 10px;
        padding-bottom: 8px;
        border-bottom: 1px dashed #eee;
        display: flex; /* Use flexbox for alignment */
        justify-content: space-between; /* Put name and status on ends */
        align-items: center;
         font-size: 1.05em;
    }
     #simulation-details p:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }

     #simulation-details p strong {
        flex-grow: 1; /* Allow name to take space */
        padding-left: 10px; /* Space between name and status */
     }

    .mission-status {
        font-weight: bold;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.9em;
    }

     .mission-status.success {
        color: white;
        background-color: var(--success-color);
     }

     .mission-status.failure {
        color: white;
        background-color: var(--error-color);
     }

     .final-scores {
         margin-top: 20px;
         padding-top: 20px;
         border-top: 2px solid var(--primary-color);
         font-size: 1.1em;
         font-weight: 700;
     }
     .final-scores p {
         margin-bottom: 10px;
     }
      .final-scores span {
         color: var(--header-bg);
      }

     .feedback-message {
         margin-top: 20px;
         padding: 15px;
         background-color: #fff;
         border: 1px solid var(--border-color);
         border-radius: 8px;
         font-style: italic;
         color: #555;
         font-size: 1em;
     }

    /* Explanation Section Styling */
    .explanation-section h3 {
         color: var(--header-bg);
         margin-top: 20px;
    }
     .explanation-section ul {
         margin-right: 20px; /* Indent list for RTL */
         padding: 0;
         list-style-type: none; /* Remove default bullets */
     }
     .explanation-section li {
         margin-bottom: 10px;
         padding-right: 15px; /* Space for custom bullet */
         position: relative;
     }
     .explanation-section li:before {
         content: '\2022'; /* Unicode bullet character */
         color: var(--primary-color);
         font-weight: bold;
         display: inline-block;
         width: 1em;
         margin-right: -1em; /* Pull bullet left */
         position: absolute;
         right: 0;
         top: 0;
     }

    /* Add a simple animation for selected rows */
    @keyframes highlight {
        0% { background-color: transparent; }
        50% { background-color: #cce5ff; }
        100% { background-color: transparent; }
    }
     .highlight-row {
        animation: highlight 1s ease-in-out;
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const missions = [
            { id: 'm1', name: 'לוויין תצפית מתקדמת על כדור הארץ', cost: 10, time: 3, risk: 'Low', science: 10, tech: 5, pr: 15, description: 'מעקב סביבתי מדויק וניהול אסונות.' },
            { id: 'm2', name: 'נחתת ורובר ירחיים', cost: 15, time: 4, risk: 'Medium', science: 20, tech: 15, pr: 20, description: 'מחקר ראשוני של משאבי ירח וניסויים מדעיים.' },
            { id: 'm3', name: 'מקפת מאדים וניתוח אטמוספירה', cost: 20, time: 5, risk: 'Medium', science: 25, tech: 10, pr: 25, description: 'חיפוש אחר סימני חיים בעבר או בהווה ומחקר אקלים.' },
            { id: 'm4', name: 'גשושית לירחי צדק הקפואים (אירופה)', cost: 30, time: 8, risk: 'High', science: 40, tech: 30, pr: 35, description: 'חיפוש אוקיינוס תת-קרקעי פוטנציאלי ויכולת תמיכה בחיים.' },
            { id: 'm5', name: 'טלסקופ חלל גדול חדש (דור הבא)', cost: 40, time: 10, risk: 'Low', science: 50, tech: 40, pr: 50, description: 'תצפית על היקום הקדום וחקר כוכבי לכת מחוץ למערכת השמש.' },
            { id: 'm6', name: 'משימת החזרת דגימה מאסטרואיד קרוב', cost: 25, time: 7, risk: 'High', science: 35, tech: 25, pr: 30, description: 'הבנה טובה יותר של היווצרות מערכת השמש והכנה להגנה פלנטרית.' },
            { id: 'm7', name: 'גשושית בינכוכבית (יורשת לווייג\'ר)', cost: 50, time: 15, risk: 'High', science: 60, tech: 50, pr: 40, description: 'חקירת גבולות מערכת השמש והחלל הבינכוכבי.' },
            { id: 'm8', name: 'תמיכה בפיתוח תחנת חלל מסחרית', cost: 5, time: 2, risk: 'Low', science: 5, tech: 10, pr: 10, description: 'קידום כלכלת חלל ויכולות תעשייתיות במסלול נמוך.' },
            { id: 'm9', name: 'מערך לווייני תקשורת מהיר גלובלי', cost: 15, time: 3, risk: 'Low', science: 5, tech: 20, pr: 15, description: 'שיפור תקשורת וחיבור אזורים מרוחקים בעולם.' },
            { id: 'm10', name: 'לימוד היתכנות למשימה מאוישת למאדים (שלב 1: תכנון וטכנולוגיה)', cost: 10, time: 3, risk: 'Medium', science: 10, tech: 15, pr: 40, description: 'הכנה לקראת ההישג הגדול הבא של האנושות בחלל.' }
        ];

        const totalBudget = 100; // Billion USD
        const totalTime = 15; // Years

        // Map risk levels to probabilities of success (higher probability means lower risk)
        const riskProbabilities = {
            'Low': 0.95,    // 95% chance of success
            'Medium': 0.75, // 75% chance of success
            'High': 0.40    // 40% chance of success
        };

        // DOM Elements
        const missionsTableBody = document.getElementById('missions-table-body');
        const selectedCostSpan = document.getElementById('selected-cost');
        const selectedTimeSpan = document.getElementById('selected-time');
        const selectedRiskSpan = document.getElementById('selected-risk');
        const selectedPotentialSpan = document.getElementById('selected-potential');
        const constraintStatus = document.getElementById('constraint-status');
        const runSimulationButton = document.getElementById('run-simulation');
        const simulationResultsDiv = document.getElementById('simulation-results');
        const simulationDetailsDiv = document.getElementById('simulation-details');
        const finalCostSpan = document.getElementById('final-cost');
        const finalScienceSpan = document.getElementById('final-science');
        const finalTechSpan = document.getElementById('final-tech');
        const finalPrSpan = document.getElementById('final-pr');
        const simulationFeedback = document.getElementById('simulation-feedback');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const simulationProgressBar = document.getElementById('simulation-progress-bar');
        const appDiv = document.getElementById('app');


        let selectedMissions = [];

        // Set constraints display initially
        document.getElementById('total-budget').textContent = totalBudget;
        document.getElementById('total-time').textContent = totalTime;

        // Render missions table with checkboxes
        function renderMissions() {
            missionsTableBody.innerHTML = '';
            missions.forEach(mission => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td><input type="checkbox" data-id="${mission.id}"></td>
                    <td>${mission.name}</td>
                    <td>${mission.cost}</td>
                    <td>${mission.time}</td>
                    <td>${mission.risk}</td>
                    <td>${mission.science}</td>
                    <td>${mission.tech}</td>
                    <td>${mission.pr}</td>
                `;
                missionsTableBody.appendChild(row);
            });
        }

        // Update summary based on selected missions
        function updateSummary() {
            // Get currently checked checkboxes and find corresponding mission objects
            const checkboxes = Array.from(missionsTableBody.querySelectorAll('input[type="checkbox"]'));
             selectedMissions = checkboxes
                               .filter(checkbox => checkbox.checked)
                               .map(checkbox => missions.find(m => m.id === checkbox.dataset.id));

            // Update selected class for row highlighting
             checkboxes.forEach(checkbox => {
                 const row = checkbox.closest('tr');
                 if (checkbox.checked) {
                     row.classList.add('selected-mission');
                 } else {
                     row.classList.remove('selected-mission');
                 }
             });


            // Calculate totals
            const totalSelectedCost = selectedMissions.reduce((sum, mission) => sum + mission.cost, 0);
            const totalSelectedTime = selectedMissions.reduce((sum, mission) => sum + mission.time, 0);
            const totalSelectedPotential = selectedMissions.reduce((sum, mission) => sum + mission.science + mission.tech + mission.pr, 0);

            // Determine overall risk - use the highest selected risk level for display
            let overallRisk = 'אין'; // Default
            if (selectedMissions.some(m => m.risk === 'High')) {
                overallRisk = 'גבוהה';
            } else if (selectedMissions.some(m => m.risk === 'Medium')) {
                overallRisk = 'בינונית';
            } else if (selectedMissions.some(m => m.risk === 'Low')) {
                 overallRisk = 'נמוכה';
            } else {
                 overallRisk = '-'; // If no missions selected
            }


            // Update UI spans
            selectedCostSpan.textContent = totalSelectedCost;
            selectedTimeSpan.textContent = totalSelectedTime;
            selectedRiskSpan.textContent = overallRisk;
            selectedPotentialSpan.textContent = totalSelectedPotential;

            // Check constraints and update status/button state
            checkConstraints(totalSelectedCost, totalSelectedTime, selectedMissions.length);
        }

        // Check constraints and enable/disable button
        function checkConstraints(cost, time, missionCount) {
            const costOK = cost <= totalBudget;
            const timeOK = time <= totalTime;
            const icon = '<i class="fas fa-exclamation-circle"></i>'; // Default error icon

            if (missionCount === 0) {
                constraintStatus.innerHTML = '<i class="fas fa-info-circle"></i> בחר משימות כדי להתחיל.';
                 constraintStatus.className = 'status';
                runSimulationButton.disabled = true;
            } else if (costOK && timeOK) {
                constraintStatus.innerHTML = '<i class="fas fa-check-circle"></i> עומד באילוצים. מוכן להרצת סימולציה.';
                constraintStatus.className = 'status ok';
                runSimulationButton.disabled = false;
            } else if (!costOK && !timeOK) {
                 constraintStatus.innerHTML = `${icon} חורג מתקציב (עודף ${cost - totalBudget}$ מיליארד) וזמן (עודף ${time - totalTime} שנים).`;
                 constraintStatus.className = 'status error';
                 runSimulationButton.disabled = true;
            }
             else if (!costOK) {
                constraintStatus.innerHTML = `${icon} חורג מתקציב (עודף ${cost - totalBudget}$ מיליארד).`;
                constraintStatus.className = 'status error';
                runSimulationButton.disabled = true;
            } else { // !timeOK
                constraintStatus.innerHTML = `${icon} חורג מזמן (עודף ${time - totalTime} שנים).`;
                constraintStatus.className = 'status error';
                runSimulationButton.disabled = true;
            }
        }

        // Run simulation with animation and feedback
        async function runSimulation() {
             // Disable button and inputs during simulation
             runSimulationButton.disabled = true;
             missionsTableBody.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.disabled = true);

             simulationResultsDiv.style.display = 'block';
             simulationDetailsDiv.innerHTML = ''; // Clear previous results
             simulationFeedback.textContent = ''; // Clear previous feedback
             simulationProgressBar.style.width = '0%'; // Reset progress bar

             let finalCost = 0;
             let finalScience = 0;
             let finalTech = 0;
             let finalPr = 0;
             let failedMissionsCount = 0;
             let successfulMissionsCount = 0;

             const missionsToSimulate = [...selectedMissions]; // Copy array

             // Simulate each mission sequentially with a delay
             for (let i = 0; i < missionsToSimulate.length; i++) {
                 const mission = missionsToSimulate[i];
                 const successProb = riskProbabilities[mission.risk];
                 const isSuccessful = Math.random() < successProb;

                 finalCost += mission.cost; // Cost is always incurred

                 const missionResultElement = document.createElement('p');
                 const statusSpan = document.createElement('span');
                 statusSpan.className = `mission-status ${isSuccessful ? 'success' : 'failure'}`;
                 statusSpan.textContent = isSuccessful ? 'הצלחה! ✅' : 'כישלון ❌';

                 missionResultElement.innerHTML = `<strong>${mission.name}</strong> `;
                 missionResultElement.appendChild(statusSpan);

                 simulationDetailsDiv.appendChild(missionResultElement);

                 if (isSuccessful) {
                     finalScience += mission.science;
                     finalTech += mission.tech;
                     finalPr += mission.pr;
                     successfulMissionsCount++;
                 } else {
                     failedMissionsCount++;
                 }

                 // Update progress bar
                 simulationProgressBar.style.width = `${((i + 1) / missionsToSimulate.length) * 100}%`;

                 // Add a short delay for animation effect
                 await new Promise(resolve => setTimeout(resolve, 700)); // Adjust delay as needed
             }

             // Update final scores
             finalCostSpan.textContent = finalCost.toFixed(1);
             finalScienceSpan.textContent = finalScience;
             finalTechSpan.textContent = finalTech;
             finalPrSpan.textContent = finalPr;

             // Generate and display feedback
             generateFeedback(finalCost, finalScience, finalTech, finalPr, failedMissionsCount, selectedMissions);

             // Re-enable button and inputs
             updateSummary(); // This will re-check constraints and enable/disable button correctly
             missionsTableBody.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.disabled = false);
        }

        function generateFeedback(cost, science, tech, pr, failedCount, missionsPortfolio) {
            let feedback = '<h4><i class="fas fa-clipboard-check"></i> סיכום והמלצות:</h4>';
            const initialTime = missionsPortfolio.reduce((sum, m) => sum + m.time, 0);
            const maxInitialPotential = missionsPortfolio.reduce((sum, m) => sum + m.science + m.tech + m.pr, 0);
            const actualPotential = science + tech + pr;
            const overallRisk = selectedRiskSpan.textContent; // Get the displayed risk level

             feedback += `<p>השקעת ${cost}$ מיליארד ושיגרת פורטפוליו של ${missionsPortfolio.length} משימות שדרשו ${initialTime} שנים לתכנון וביצוע.</p>`;

             // Feedback on outcomes vs potential
             feedback += `<p>🎯 סה"כ נקודות פוטנציאל שהושגו: <strong>${actualPotential}</strong> מתוך ${maxInitialPotential} נקודות פוטנציאל שהיו אפשריות בפורטפוליו שבחרת.</p>`;


             // Feedback based on failures and risk
             if (failedCount > 0) {
                 feedback += `<p>💔 <strong>${failedCount} משימה(ות) נכשלה.</strong> `;
                 if (overallRisk === 'גבוהה') {
                     feedback += `עם פורטפוליו בסיכון גבוה, כישלונות הם חלק מהמשחק. האם התמורה של המשימות שהצליחו הצדיקה את הסיכון?`;
                 } else if (overallRisk === 'בינונית') {
                      feedback += `גם בפורטפוליו בסיכון בינוני עלולים להתרחש כישלונות בלתי צפויים. חשוב ללמוד מכל כישלון להמשך הדרך.`;
                 } else { // Low risk
                      feedback += `אף בפורטפוליו בסיכון נמוך יחסית עלולים להתרחש תקלות. זהו תזכורת שאין אפס סיכון במסע לחלל.`;
                 }
                 feedback += `</p>`;
             } else {
                 feedback += `<p>🎉 <strong>כל המשימות שהרצת הצליחו!</strong> `;
                 if (overallRisk === 'גבוהה') {
                     feedback += `מזל טוב! הצלחת להשיג תוצאות מצוינות חרף הסיכון הגבוה שבחרת. נראה שההימור השתלם הפעם.`;
                 } else {
                      feedback += `נהדר! הפורטפוליו שלך הצליח כצפוי בהתאם לרמת הסיכון. יציבות והצלחה הם שם המשחק.`;
                 }
                  feedback += `</p>`;
             }

            // Add general strategic advice based on outcome
            if (actualPotential < maxInitialPotential * 0.5 && failedCount > selectedMissions.length * 0.3 && overallRisk === 'גבוהה') {
                 feedback += `<p><i class="fas fa-lightbulb"></i> <em>המלצה למשחק הבא:</em> נראה שהסיכון הגבוה לא השתלם הפעם. שקול לבנות פורטפוליו מאוזן יותר, אולי עם פחות משימות בעלות סיכון גבוה במיוחד, כדי להבטיח יותר הצלחות.</p>`;
            } else if (actualPotential === maxInitialPotential && overallRisk === 'נמוכה') {
                 feedback += `<p><i class="fas fa-lightbulb"></i> <em>המלצה למשחק הבא:</em> השגת את מלוא הפוטנציאל עם סיכון נמוך. אולי כדאי לשקול לכלול משימה אחת או שתיים בסיכון בינוני/גבוה בפעם הבאה כדי לראות אם תוכל להגדיל את התמורה הכוללת?</p>`;
            } else if (actualPotential > maxInitialPotential * 0.8 && failedCount < selectedMissions.length * 0.2) {
                feedback += `<p><i class="fas fa-lightbulb"></i> <em>סיכום:</em> פורטפוליו מוצלח מאוד! הצלחת למקסם את הפוטנציאל תוך שמירה על רמת כישלונות נמוכה. אסטרטגיה חזקה.</p>`;
            } else {
                 feedback += `<p><i class="fas fa-lightbulb"></i> <em>נקודות למחשבה:</em> חשוב לנתח את התוצאות ולראות האם ההשקעה (עלות וזמן) עמדה ביחס לפוטנציאל שהושג. האם הפיזור בין מדע, טכנולוגיה וציבור תאם את המטרות שלך?</p>`;
            }


            simulationFeedback.innerHTML = feedback; // Use innerHTML because feedback contains HTML tags
        }


        // Toggle explanation visibility with smooth animation
        function toggleExplanation() {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            if (isHidden) {
                explanationDiv.style.display = 'block';
                setTimeout(() => explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 'px', 10); // Set max height to auto after display block
                explanationDiv.style.opacity = 1;
                toggleExplanationButton.innerHTML = '<i class="fas fa-book-reader"></i> הסתר הסבר';
            } else {
                 explanationDiv.style.maxHeight = '0'; // Animate closing
                 explanationDiv.style.opacity = 0;
                setTimeout(() => explanationDiv.style.display = 'none', 500); // Hide after transition
                toggleExplanationButton.innerHTML = '<i class="fas fa-book-open"></i> הצג הסבר: האמנות של קבלת החלטות אסטרטגיות';
            }
        }

        // Add event listeners
        missionsTableBody.addEventListener('change', (event) => {
            if (event.target.type === 'checkbox') {
                updateSummary();
                 simulationResultsDiv.style.display = 'none'; // Hide previous results on selection change
                 simulationProgressBar.style.width = '0%'; // Reset progress bar
            }
        });

        runSimulationButton.addEventListener('click', runSimulation);
        toggleExplanationButton.addEventListener('click', toggleExplanation);

        // Add some basic animation/transition properties to explanation section
        explanationDiv.style.transition = 'max-height 0.5s ease-in-out, opacity 0.5s ease-in-out';
        explanationDiv.style.overflow = 'hidden';
        explanationDiv.style.maxHeight = '0';
        explanationDiv.style.opacity = 0;


        // Initial render
        renderMissions();
        updateSummary(); // Calculate initial summary (should be 0) and check constraints
    });
</script>
```