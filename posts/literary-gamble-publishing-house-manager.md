---
title: "הימור ספרותי: להיות מנהל הוצאה לאור"
english_slug: literary-gamble-publishing-house-manager
category: "ניהול ועסקים / ניהול"
tags:
  - הוצאה לאור
  - ניהול
  - סימולציה עסקית
  - קבלת החלטות
  - כלכלה
---
<div id="app">
    <header class="game-header">
        <h1>הימור ספרותי: להיות מנהל הוצאה לאור</h1>
        <p class="subtitle">צללו לעולם המרתק והמסוכן של ניהול הוצאת ספרים. האם תצליחו לבנות אימפריה ספרותית?</p>

        <div class="stats-bar">
            <div class="stat-item">
                <span class="stat-label">שנה:</span>
                <span id="current-round" class="stat-value highlight">1</span>
            </div>
            <div class="stat-item">
                 <span class="stat-label">תקציב:</span>
                <span id="current-budget" class="stat-value budget-value">100,000</span> ש"ח
            </div>
            <div class="stat-item">
                <span class="stat-label">רווח כולל:</span>
                <span id="total-profit" class="stat-value profit-value">0</span> ש"ח
            </div>
        </div>
    </header>

    <div id="game-area">
        <div id="manuscripts-area" class="game-section active">
            <h2>כתבי יד טריים על השולחן</h2>
            <p class="section-description">סיירתם בירידי ספרים וקיבלתם הצעות מסוכנים ספרותיים. אילו כתבי יד תבחרו לקדם השנה?</p>
            <div id="manuscript-list" class="list-container">
                <!-- Manuscripts will be loaded here -->
            </div>
             <div class="section-footer">
                <p>בחר/י לפחות ספר אחד כדי להמשיך.</p>
            </div>
        </div>

        <div id="decisions-area" class="game-section" style="display: none;">
            <h2>השקעה אסטרטגית בספרים נבחרים</h2>
            <p class="section-description">בחרתם את כתבי היד המבטיחים ביותר. עכשיו קבעו את תקציב ההשקעה הנוסף לעריכה מעמיקה ושיווק יצירתי. כל שקל משפיע!</p>
            <div id="accepted-list" class="list-container">
                <!-- Accepted manuscripts and budget allocation options will be loaded here -->
            </div>
            <div class="section-footer">
                 <button id="simulate-button" class="primary-button" disabled>סגור את השנה ופרסם ספרים!</button>
                 <p id="budget-warning" class="warning-message" style="display: none;">שימו לב: ההשקעה הכוללת חורגת מהתקציב הקיים.</p>
            </div>
        </div>

        <div id="results-area" class="game-section" style="display: none;">
            <h2>תוצאות השנה הספרותית <span id="results-round"></span></h2>
            <p class="section-description">הספרים הודפסו והופצו, הקמפיינים השיווקיים הסתיימו. הגיע הזמן לראות מי הפך לרב מכר ומי נשאר על המדף...</p>
            <div id="round-results-list" class="list-container results-list">
                <!-- Round results per book will be loaded here -->
            </div>
             <div class="round-summary">
                <p><strong>רווח/הפסד בשנה זו:</strong> <span id="round-profit" class="stat-value"></span> ש"ח</p>
            </div>
            <div class="section-footer">
                <button id="next-round-button" class="primary-button">התחל שנה חדשה</button>
            </div>
        </div>
    </div>

    <div id="game-over-area" class="game-section" style="display: none;">
        <h2 class="game-over-title">המסע הספרותי הגיע לסופו...</h2>
        <p id="final-message" class="final-message"></p>
        <p class="final-profit">רווח כולל סופי: <span id="final-profit" class="stat-value profit-value"></span> ש"ח</p>
        <button id="restart-button" class="secondary-button">התחל מחדש</button>
    </div>

    <button id="toggle-explanation" class="explanation-toggle-button">מה זה כל הסיפור הזה? (הסבר)</button>

    <div id="explanation" class="explanation-section" style="display: none;">
        <h2>הסבר: עולם ההוצאה לאור - מאחורי הקלעים</h2>
        <p>ניהול הוצאת ספרים הוא תפקיד מרתק ומאתגר, המשלב שיקולים אמנותיים, תרבותיים, כלכליים ושיווקיים. המשחק הזה מדמה חלק מהאתגרים המרכזיים שתפגשו כמנהלי הוצאה.</p>

        <h3>המסע של ספר: מכתב יד למדף</h3>
        <p>הכל מתחיל בכתבי יד שמגיעים להוצאה. צוות הקריאה והעורכים בוחנים אותם ומחליטים אילו מהם בעלי פוטנציאל. לאחר שנבחר כתב יד, מתחיל תהליך ארוך של עבודה: עריכה (לשונית ותוכנית), הגהה, עיצוב כריכה ופנים, ולבסוף הפקה (דפוס או פורמט דיגיטלי). במקביל, בונים אסטרטגיית שיווק כדי שהספר יגיע לקהל הנכון. כל שלב דורש השקעה - זמן, משאבים, וכסף. ההחלטות שתקבלו לגבי אילו ספרים להוציא ולאיזו רמה של עריכה ושיווק להשקיע ישפיעו דרמטית על הצלחת הספר בשוק.</p>

        <h3>המודל העסקי הבסיסי: כסף נכנס, כסף יוצא</h3>
        <p>הכנסות הוצאה לאור מגיעות בעיקר ממכירת ספרים. אבל לפני שמרוויחים, יש המון עלויות:</p>
        <ul>
            <li><strong>עלויות רכישת זכויות:</strong> תשלום ראשוני לכותב או סוכנו.</li>
            <li><strong>עלויות עריכה והפקה:</strong> תשלום לעורכים, מגיהים, מעצבים, בתי דפוס. אלה עלויות משתנות לפי אורך הספר, מורכבות העריכה, וכמות העותקים המודפסים.</li>
            <li><strong>עלויות שיווק והפצה:</strong> פרסום, יחסי ציבור, אירועי השקה, משלוח לחנויות. גם אלה משתנות בהתאם לספר ולהשקעה הרצויה.</li>
             <li><strong>עלויות קבועות (מודל מדויק יותר כולל גם):</strong> שכר דירה, משכורות עובדי מטה שאינם קשורים לספר ספציפי, חשבונות, וכו'. במשחק זה יש עלות קבועה שמקוזזת כל שנה, כדי לדמות את הוצאות התפעול השוטפות.</li>
        </ul>
        <p><strong>רווח = הכנסות ממכירות - עלויות כוללות (לכל הספרים שהוצאו + עלויות קבועות).</strong> המטרה היא, כמובן, שההכנסות יעלו על העלויות!</p>

        <h3>מה גורם לספר להצליח? או להיכשל?</h3>
        <p>אין נוסחת קסם, אבל אלו חלק מהגורמים:</p>
        <ul>
            <li><strong>איכות התוכן:</strong> ספר כתוב וערוך היטב תמיד עם יתרון. עריכה טובה יכולה להציל כתב יד מבטיח אך לא מושלם.</li>
            <li><strong>התאמה לשוק ו'באזז':</strong> האם הסוגה פופולרית? האם הנושא אקטואלי? האם אפשר ליצור עניין ושיח סביב הספר?</li>
            <li><strong>השקעת שיווק נכונה:</strong> ספר מדהים שלאף אחד אין מושג שהוא יצא, לא יימכר. שיווק יעיל מחבר בין הספר לקהל הקוראים הפוטנציאלי.</li>
            <li><strong>תזמון:</strong> יציאה לשוק ברגע הנכון יכולה לעשות פלאים.</li>
            <li><strong>ולא נשכח... מזל:</strong> לפעמים, למרות כל המאמצים, ספר מצליח מעבר לכל הציפיות, או להיפך - נכשל בלי סיבה ברורה. אי אפשר לחסל את אי הוודאות לחלוטין!</li>
        </ul>

        <h3>האיזון: עסק מול תרבות</h3>
        <p>הוצאה לאור היא עסק, והיא צריכה להיות רווחית כדי לשרוד. אבל יש לה גם תפקיד תרבותי חשוב - להביא לקוראים יצירות חדשות, קולות מגוונים, ולשמור על הספרות כפי שהיא. לעיתים, יש מתח בין הרצון להוציא רק ספרים "בטוחים" עם פוטנציאל מכירות גבוה, לבין הרצון לפרסם יצירות ספרותיות או תרבותיות בעלות ערך, גם אם הן נישתיות יותר. מנהל הוצאה טוב מוצא את האיזון הנכון כדי לבנות קטלוג מגוון - גם ספרים שיכניסו כסף ("לחם וחמאה") וגם ספרים שחשוב להוציא לאור מסיבות אמנותיות או חברתיות.</p>
         <p>עכשיו כשאתם מבינים יותר, חזרו למשחק ונסו לנהל את ההוצאה שלכם!</p>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #6c757d; /* Gray */
        --accent-color: #28a745; /* Green */
        --danger-color: #dc3545; /* Red */
        --warning-color: #ffc107; /* Yellow */
        --surface-color: #ffffff;
        --background-color: #f8f9fa; /* Light gray */
        --border-color: #dee2e6; /* Lighter gray */
        --text-color: #343a40; /* Dark gray */
        --text-light: #6c757d;

        --spacing-unit: 15px;
        --border-radius: 8px;
        --card-padding: var(--spacing-unit);
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 0;
        direction: rtl; /* Ensure Right-to-Left */
        text-align: right; /* Ensure text aligns right */
    }

    #app {
        max-width: 900px;
        margin: 20px auto;
        padding: var(--spacing-unit) * 1.5;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--surface-color);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        overflow: hidden; /* Clear floats/margins */
    }

    .game-header {
        text-align: center;
        margin-bottom: var(--spacing-unit) * 2;
        padding-bottom: var(--spacing-unit);
        border-bottom: 2px solid var(--primary-color);
    }

    h1 {
        color: var(--primary-color);
        margin: 0 0 5px 0;
        font-size: 2.2em;
    }

    .subtitle {
        color: var(--text-light);
        margin: 0 0 var(--spacing-unit) 0;
        font-size: 1em;
    }

    .stats-bar {
        display: flex;
        justify-content: space-around;
        margin-top: var(--spacing-unit);
        padding-top: var(--spacing-unit);
        border-top: 1px solid var(--border-color);
    }

    .stat-item {
        text-align: center;
    }

    .stat-label {
        display: block;
        font-size: 0.9em;
        color: var(--text-light);
        margin-bottom: 3px;
    }

    .stat-value {
        font-size: 1.3em;
        font-weight: bold;
        color: var(--text-color);
    }

    .budget-value {
         color: var(--accent-color); /* Green for budget */
    }

    .profit-value {
         color: var(--primary-color); /* Blue for profit */
    }

     .profit-value.loss {
         color: var(--danger-color); /* Red for loss */
     }


    /* Game Sections */
    .game-section {
        margin-bottom: var(--spacing-unit) * 2;
        padding: var(--spacing-unit);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--surface-color);
        transition: opacity 0.5s ease-in-out;
    }

    .game-section:not(.active) {
        opacity: 0;
        height: 0;
        padding-top: 0;
        padding-bottom: 0;
        margin-top: 0;
        margin-bottom: 0;
        overflow: hidden;
    }

    h2 {
        color: var(--primary-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
        margin-top: 0;
        margin-bottom: var(--spacing-unit);
        font-size: 1.6em;
    }

    .section-description {
        color: var(--text-light);
        margin-bottom: var(--spacing-unit) * 1.5;
        font-size: 0.95em;
    }

    .list-container {
        margin-top: var(--spacing-unit);
    }

    .manuscript-item, .accepted-book-item, .result-item {
        border: 1px solid var(--border-color);
        padding: var(--card-padding);
        margin-bottom: var(--spacing-unit);
        border-radius: var(--border-radius);
        background-color: var(--background-color);
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .manuscript-item:hover, .accepted-book-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }


    .manuscript-details, .book-details, .result-details {
        flex-grow: 1;
        margin-right: var(--spacing-unit);
    }

    .manuscript-details h4, .book-details h4 {
        margin-top: 0;
        margin-bottom: 5px;
        color: var(--primary-color);
        font-size: 1.1em;
    }

    .manuscript-details p, .book-details p, .result-details p {
        margin: 3px 0;
        font-size: 0.9em;
        color: var(--text-color);
    }

    .manuscript-details span, .book-details span, .result-details span {
        font-weight: bold;
        color: var(--text-color);
    }

    .manuscript-actions, .book-actions {
        display: flex;
        align-items: center;
        gap: var(--spacing-unit) / 2;
        white-space: nowrap; /* Prevent wrapping */
    }

     /* Custom Checkbox Styling */
    .manuscript-actions input[type="checkbox"] {
        /* Hide default checkbox */
        position: absolute;
        opacity: 0;
        cursor: pointer;
        height: 0;
        width: 0;
    }

    .manuscript-actions label {
        position: relative;
        cursor: pointer;
        padding-right: 25px; /* Space for custom checkbox */
        user-select: none; /* Prevent text selection */
        font-size: 1em;
         color: var(--primary-color);
    }

    .manuscript-actions label::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0; /* Position on the right for RTL */
        width: 18px;
        height: 18px;
        border: 2px solid var(--primary-color);
        border-radius: 4px;
        background-color: var(--background-color);
        transition: all 0.3s ease;
    }

    .manuscript-actions input[type="checkbox"]:checked + label::before {
        background-color: var(--primary-color);
        border-color: var(--primary-color);
    }

    .manuscript-actions label::after {
        content: '';
        position: absolute;
        top: 4px;
        right: 4px; /* Position on the right for RTL */
        width: 10px;
        height: 5px;
        border: solid white;
        border-width: 0 0 2px 2px;
        transform: rotate(-45deg);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

     .manuscript-actions input[type="checkbox"]:checked + label::after {
        opacity: 1;
    }


    .book-actions input[type="number"] {
        width: 80px;
        padding: 8px;
        border: 1px solid var(--border-color);
        border-radius: 4px;
        font-size: 1em;
        text-align: center; /* Center text in number input */
    }

    button {
        padding: 12px 20px;
        border: none;
        border-radius: var(--border-radius) / 2;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: var(--spacing-unit);
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .primary-button {
        background-color: var(--primary-color);
        color: white;
    }

    .primary-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
    }

    .primary-button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-2px);
    }

     .secondary-button {
        background-color: var(--secondary-color);
        color: white;
     }

     .secondary-button:hover:not(:disabled) {
        background-color: #5a6268;
        transform: translateY(-2px);
     }

    .explanation-toggle-button {
         display: block;
         margin: var(--spacing-unit) * 1.5 auto;
         background-color: var(--secondary-color);
         margin-bottom: 0;
         font-size: 1em;
    }

     .explanation-toggle-button:hover:not(:disabled) {
         background-color: #5a6268;
    }


    /* Results Styling */
    .results-list .result-item {
         background-color: var(--background-color); /* Or a slightly different shade */
    }

    .result-item.profit {
        border-right: 5px solid var(--accent-color); /* Green border on the right */
        background-color: #e9f7ef; /* Light green background */
    }
    .result-item.loss {
        border-right: 5px solid var(--danger-color); /* Red border on the right */
        background-color: #fdedee; /* Light red background */
    }
    .result-item.break-even {
        border-right: 5px solid var(--warning-color); /* Orange border on the right */
         background-color: #fff8e1; /* Light yellow background */
    }

     .result-item.profit span.stat-value,
     .result-item.profit .result-details span {
         color: var(--accent-color);
     }
     .result-item.loss span.stat-value,
     .result-item.loss .result-details span {
         color: var(--danger-color);
     }
      .result-item.break-even span.stat-value,
      .result-item.break-even .result-details span {
          color: var(--warning-color);
      }


    .round-summary {
         margin-top: var(--spacing-unit);
         padding-top: var(--spacing-unit);
         border-top: 1px dashed var(--border-color);
         text-align: center;
         font-size: 1.2em;
    }
     .round-summary strong {
         color: var(--primary-color);
     }

    /* Game Over Styling */
    .game-over-area {
        text-align: center;
    }

    .game-over-title {
        color: var(--danger-color);
        font-size: 2em;
        margin-bottom: var(--spacing-unit);
        border-bottom: none; /* Remove border from game over title */
    }

    .final-message {
         font-size: 1.2em;
         margin-bottom: var(--spacing-unit);
         color: var(--text-color);
    }

    .final-profit {
         font-size: 1.5em;
         font-weight: bold;
         margin-bottom: var(--spacing-unit) * 2;
    }
     .final-profit span.stat-value {
         font-size: 1.5em; /* Match parent font size */
         color: var(--primary-color);
     }
      .final-profit span.stat-value.loss {
          color: var(--danger-color);
      }

    /* Explanation Section Styling */
    .explanation-section {
        max-width: 900px;
        margin: 0 auto var(--spacing-unit) * 1.5 auto;
        padding: var(--spacing-unit) * 1.5;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--surface-color);
        line-height: 1.6;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    .explanation-section h2 {
        color: var(--primary-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
        margin-top: 0;
        margin-bottom: var(--spacing-unit);
        font-size: 1.8em;
    }

    .explanation-section h3 {
        color: var(--secondary-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 3px;
        margin-top: var(--spacing-unit) * 1.5;
        margin-bottom: var(--spacing-unit);
        font-size: 1.3em;
    }

    .explanation-section p, .explanation-section ul {
        margin-bottom: var(--spacing-unit);
         color: var(--text-color);
         font-size: 1em;
    }

    .explanation-section ul {
        padding-right: var(--spacing-unit) * 1.5; /* RTL List padding */
        list-style-type: disc; /* Bullet points */
    }
     .explanation-section li {
         margin-bottom: var(--spacing-unit) / 2;
     }

    .warning-message {
        color: var(--danger-color);
        font-weight: bold;
        margin-top: var(--spacing-unit);
        text-align: center;
    }

    .section-footer {
        text-align: center;
        margin-top: var(--spacing-unit) * 1.5;
        padding-top: var(--spacing-unit);
        border-top: 1px solid var(--border-color);
    }

    .section-footer p {
        margin: 0;
        color: var(--text-light);
        font-size: 0.9em;
    }

</style>

<script>
    let currentBudget = 100000;
    let totalProfit = 0;
    let currentRound = 1;
    const maxRounds = 8; // Game lasts 8 years
    const initialManuscriptsCount = 5; // More choices per round
    const roundFixedCosts = 15000; // Costs like rent, basic salaries per year

    const genres = [
        { name: "רומן היסטורי", popularity: 0.6, culturalValue: 0.7 },
        { name: "מותחן", popularity: 0.9, culturalValue: 0.5 },
        { name: "פנטזיה", popularity: 0.8, culturalValue: 0.6 },
        { name: "ספר ילדים", popularity: 0.7, culturalValue: 0.8 },
        { name: "ספר עיון", popularity: 0.5, culturalValue: 0.9 },
        { name: "סיפורת עכשווית", popularity: 0.7, culturalValue: 0.8 },
        { name: "מדריך מעשי", popularity: 0.6, culturalValue: 0.4 },
        { name: "שירה", popularity: 0.1, culturalValue: 1.0 }, // High cultural, low popularity
        { name: "מדע בדיוני", popularity: 0.7, culturalValue: 0.7 }
    ];
    const qualityPotential = ["נמוך", "בינוני", "גבוה", "יוצא מן הכלל"]; // Affects base sales potential
    const baseEditingCost = 6000; // Base cost
    const baseProductionCost = 12000; // Base cost per book (printing, etc.)
    const minExtraBudget = 0;
    const maxExtraBudget = 40000; // Max extra allocation per book for editing/marketing

    // Get DOM elements
    const budgetElement = document.getElementById('current-budget');
    const totalProfitElement = document.getElementById('total-profit');
    const currentRoundElement = document.getElementById('current-round');
    const manuscriptsArea = document.getElementById('manuscripts-area');
    const manuscriptListElement = document.getElementById('manuscript-list');
    const decisionsArea = document.getElementById('decisions-area');
    const acceptedListElement = document.getElementById('accepted-list');
    const simulateButton = document.getElementById('simulate-button');
    const resultsArea = document.getElementById('results-area');
    const resultsRoundElement = document.getElementById('results-round');
    const roundResultsListElement = document.getElementById('round-results-list');
    const roundProfitElement = document.getElementById('round-profit');
    const nextRoundButton = document.getElementById('next-round-button');
    const gameOverArea = document.getElementById('game-over-area');
    const finalMessageElement = document.getElementById('final-message');
    const finalProfitElement = document.getElementById('final-profit');
    const restartButton = document.getElementById('restart-button');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const gameArea = document.getElementById('game-area'); // Container for game sections
    const budgetWarningElement = document.getElementById('budget-warning');


    let currentManuscripts = [];
    let acceptedBooks = [];

    // --- Core Game Logic Functions ---

    function generateManuscript(id) {
        const genre = genres[Math.floor(Math.random() * genres.length)];
        const qualityIndex = Math.floor(Math.random() * qualityPotential.length);
        const potential = qualityPotential[qualityIndex];

        // More complex base sales factor influenced by quality and genre popularity
        const baseSalesFactor = ((qualityIndex + 1) / qualityPotential.length) * 1.5 + genre.popularity * 1.5; // Range roughly 0.5 to 3

        const estimatedEditing = baseEditingCost + Math.floor(Math.random() * 4000) + qualityIndex * 1500;
        const estimatedProduction = baseProductionCost + Math.floor(Math.random() * 2000); // Varies slightly
        const acquisitionCost = Math.floor(Math.random() * 2500) + 500; // Cost based loosely on perceived potential/genre

        return {
            id: id,
            title: `כתב יד מס' ${id}`, // Keep generic title for simulation
            genre: genre.name,
            potential: potential,
            estimatedEditing: estimatedEditing,
            estimatedProduction: estimatedProduction,
            acquisitionCost: acquisitionCost,
            baseSalesFactor: baseSalesFactor, // Internal factor for simulation
            allocatedEditing: 0, // Extra budget split
            allocatedMarketing: 0 // Extra budget split
        };
    }

    function renderManuscripts(manuscripts) {
        manuscriptListElement.innerHTML = '';
        manuscripts.forEach(ms => {
            const item = document.createElement('div');
            item.classList.add('manuscript-item');
            item.innerHTML = `
                <div class="manuscript-details">
                    <h4>${ms.title} - <span style="color: ${getGenreColor(ms.genre)};">${ms.genre}</span></h4>
                    <p>פוטנציאל משוער: <span>${ms.potential}</span></p>
                    <p>עלות רכישה: <span>${ms.acquisitionCost.toFixed(0)} ש"ח</span></p>
                    <p>עלות בסיס הפקה ועריכה: <span>${(ms.estimatedEditing + ms.estimatedProduction).toFixed(0)} ש"ח</span></p>
                </div>
                <div class="manuscript-actions">
                    <input type="checkbox" id="accept-${ms.id}" data-id="${ms.id}" ${currentBudget < (ms.acquisitionCost + ms.estimatedEditing + ms.estimatedProduction) ? 'disabled' : ''}>
                    <label for="accept-${ms.id}">${currentBudget < (ms.acquisitionCost + ms.estimatedEditing + ms.estimatedProduction) ? 'תקציב לא מספיק' : 'בחר לפרסום'}</label>
                </div>
            `;
            manuscriptListElement.appendChild(item);
        });

        document.querySelectorAll('#manuscript-list input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', updateAcceptedList);
        });
         updateAcceptedList(); // Initial check for enabling button
    }

    function updateAcceptedList() {
        const previousAcceptedCount = acceptedBooks.length;
        acceptedBooks = [];
        acceptedListElement.innerHTML = '';
        let currentAcceptedBaseCost = 0;

        const selectedCheckboxes = document.querySelectorAll('#manuscript-list input[type="checkbox"]:checked');

        if (selectedCheckboxes.length === 0) {
            decisionsArea.style.display = 'none';
            simulateButton.disabled = true;
            budgetWarningElement.style.display = 'none';
            // Animate section transition OUT
            manuscriptsArea.classList.add('active');
            decisionsArea.classList.remove('active');

            return;
        } else {
             // Animate section transition IN
            manuscriptsArea.classList.remove('active');
            decisionsArea.classList.add('active');
            decisionsArea.style.display = 'block'; // Ensure display is block for transition
        }

        selectedCheckboxes.forEach(checkbox => {
            const msId = parseInt(checkbox.dataset.id);
            const manuscript = currentManuscripts.find(m => m.id === msId);
            if (manuscript) {
                 const book = { ...manuscript, allocatedEditing: 0, allocatedMarketing: 0 }; // Create a copy for decisions
                 acceptedBooks.push(book);
                 currentAcceptedBaseCost += book.acquisitionCost + book.estimatedEditing + book.estimatedProduction;

                const item = document.createElement('div');
                item.classList.add('accepted-book-item');
                item.innerHTML = `
                    <div class="book-details">
                        <h4>${book.title} - <span style="color: ${getGenreColor(book.genre)};">${book.genre}</span></h4>
                        <p>עלות בסיס משוערת: <span>${(book.acquisitionCost + book.estimatedEditing + book.estimatedProduction).toFixed(0)} ש"ח</span></p>
                        <p>פוטנציאל משוער: <span>${book.potential}</span></p>
                    </div>
                    <div class="book-actions">
                        השקעה נוספת (שיווק/עריכה):
                        <input type="number" min="${minExtraBudget}" max="${maxExtraBudget}" value="0" data-id="${book.id}" class="extra-budget-input">
                        ש"ח
                    </div>
                `;
                acceptedListElement.appendChild(item);
            }
        });

         // Add event listeners to budget inputs AFTER elements are added
        document.querySelectorAll('.extra-budget-input').forEach(input => {
            input.addEventListener('input', updateAllocatedBudget);
             // Trigger initial update if value is not 0
             if(parseInt(input.value) > 0) {
                 updateAllocatedBudget();
             }
        });

        updateAllocatedBudget(); // Calculate total cost and check budget initially

        if (acceptedBooks.length > 0 && previousAcceptedCount === 0) {
             // Basic animation if items were just added
             acceptedListElement.style.opacity = 0;
             setTimeout(() => {
                acceptedListElement.style.opacity = 1;
             }, 10); // Small delay for reflow
        }
    }

    function updateAllocatedBudget() {
        let totalAllocated = 0;
        const acceptedBaseCost = acceptedBooks.reduce((sum, book) => sum + book.acquisitionCost + book.estimatedEditing + book.estimatedProduction, 0);

        document.querySelectorAll('.extra-budget-input').forEach(input => {
            const bookId = parseInt(input.dataset.id);
            let allocated = parseInt(input.value) || 0; // Use 0 if input is empty/invalid

            // Ensure value is within min/max range and is a multiple of 100 for cleaner numbers
            allocated = Math.max(minExtraBudget, Math.min(maxExtraBudget, allocated));
            allocated = Math.round(allocated / 100) * 100; // Round to nearest 100
            input.value = allocated; // Update input value to clamped/rounded value

            const bookIndex = acceptedBooks.findIndex(book => book.id === bookId);
            if (bookIndex !== -1) {
                // Split extra budget - slightly more weight to marketing?
                acceptedBooks[bookIndex].allocatedEditing = Math.floor(allocated * 0.4);
                acceptedBooks[bookIndex].allocatedMarketing = Math.ceil(allocated * 0.6);
                totalAllocated += allocated;
            }
        });

        const totalCostThisRound = acceptedBaseCost + totalAllocated + roundFixedCosts; // Include fixed costs

        if (currentBudget < totalCostThisRound) {
            budgetWarningElement.textContent = `ההשקעה הכוללת (${totalCostThisRound.toFixed(0)} ש"ח) חורגת מהתקציב (${currentBudget.toFixed(0)} ש"ח). הורד את ההקצאה הנוספת או בטל בחירות.`;
            budgetWarningElement.style.display = 'block';
            simulateButton.disabled = true;
        } else {
            budgetWarningElement.style.display = 'none';
            simulateButton.disabled = acceptedBooks.length === 0; // Re-enable only if books are selected and budget is OK
        }
    }

    function simulateRound() {
        // Animate section transition
        decisionsArea.classList.remove('active');
        resultsArea.classList.add('active');
        resultsArea.style.display = 'block'; // Ensure display is block

        resultsRoundElement.textContent = currentRound;
        roundResultsListElement.innerHTML = '';

        let roundTotalCost = roundFixedCosts; // Start with fixed costs
        let roundTotalRevenue = 0;
        let roundProfitLoss = 0;

        // Process each accepted book
        acceptedBooks.forEach(book => {
            const bookTotalCost = book.acquisitionCost + book.estimatedEditing + book.estimatedProduction + book.allocatedEditing + book.allocatedMarketing;
            roundTotalCost += bookTotalCost;

            // Simulation Logic (More nuanced)
            const genreData = genres.find(g => g.name === book.genre);
            const qualityMultiplier = (qualityPotential.indexOf(book.potential) + 1) / qualityPotential.length; // 0.25, 0.5, 0.75, 1.0
            const baseSalesUnits = book.baseSalesFactor * 800; // Base units based on initial analysis

            // Impact of Extra Budget (Non-linear and Random)
            let marketingBoost = (book.allocatedMarketing / maxExtraBudget) * 2000; // Max potential boost from marketing
            let editingBoost = (book.allocatedEditing / maxExtraBudget) * 500; // Max potential boost from editing (quality)

            // Add significant randomness and interplay
            // Base success chance influenced by quality and base potential
            const successChance = (qualityMultiplier * 0.4 + book.baseSalesFactor * 0.3 + genreData.popularity * 0.3) * (1 + Math.random() * 0.5); // Factor 0 to ~1.5

            let potentialSales = baseSalesUnits * successChance;
            potentialSales += marketingBoost * (0.5 + Math.random()); // Marketing impact is variable
            potentialSales += editingBoost * (0.8 + Math.random() * 0.5); // Editing impact is less about raw volume, more about floor

            // Introduce market volatility
            const marketVolatility = (Math.random() * 0.8 + 0.6); // Sales can be 60% to 140% of potential sales
            const actualSalesUnits = Math.max(50, Math.floor(potentialSales * marketVolatility)); // Ensure minimum sales (e.g., library copies)

            // Simplified Revenue: Assume fixed price and margin
            const listPrice = 70; // Example list price
            const revenuePerUnit = listPrice * (0.35 + Math.random() * 0.1); // Publisher margin varies slightly (35-45%)
            const actualRevenue = actualSalesUnits * revenuePerUnit;

            roundTotalRevenue += actualRevenue;

            const bookProfit = actualRevenue - bookTotalCost;

            const item = document.createElement('div');
            item.classList.add('result-item');
            item.classList.add(bookProfit > 0 ? 'profit' : bookProfit < 0 ? 'loss' : 'break-even');
            item.innerHTML = `
                <div class="result-details">
                    <h4>${book.title} - ${book.genre}</h4>
                    <p>עלות כוללת: <span>${bookTotalCost.toFixed(0)} ש"ח</span></p>
                    <p>יחידות מכורות: <span>${actualSalesUnits.toFixed(0)}</span></p>
                    <p>הכנסות: <span>${actualRevenue.toFixed(0)} ש"ח</span></p>
                    <p><strong>רווח/הפסד מהספר: <span class="stat-value ${bookProfit > 0 ? 'profit' : bookProfit < 0 ? 'loss' : ''}">${bookProfit.toFixed(0)} ש"ח</span></strong></p>
                </div>
            `;
            roundResultsListElement.appendChild(item);
        });

        roundProfitLoss = roundTotalRevenue - roundTotalCost;
        currentBudget += roundProfitLoss; // Budget changes based on profit/loss
        totalProfit += roundProfitLoss; // Accumulate total profit

        // Update global stats with animation
        animateNumberChange(roundProfitElement, parseFloat(roundProfitElement.textContent || '0'), roundProfitLoss);
        animateNumberChange(budgetElement, parseFloat(budgetElement.textContent.replace(/,/g, '') || '0'), currentBudget);
        animateNumberChange(totalProfitElement, parseFloat(totalProfitElement.textContent.replace(/,/g, '') || '0'), totalProfit);

        // Update round profit/loss color
         roundProfitElement.classList.remove('profit', 'loss');
         if (roundProfitLoss > 0) roundProfitElement.classList.add('profit');
         else if (roundProfitLoss < 0) roundProfitElement.classList.add('loss');


        acceptedBooks = []; // Clear accepted list for next round
         simulateButton.disabled = true; // Disable until new manuscripts selected
    }

     function animateNumberChange(element, start, end) {
         const duration = 1000; // Animation duration in ms
         const range = end - start;
         const startTime = performance.now();
         let current = start;

         function update() {
             const elapsed = performance.now() - startTime;
             const progress = Math.min(elapsed / duration, 1);

             current = start + range * progress;

             // Update text content
             element.textContent = Math.round(current).toLocaleString('he-IL'); // Use toLocaleString for commas

             // Change color temporarily
             if (range !== 0) {
                 element.style.color = range > 0 ? varColors.accentColor : varColors.dangerColor;
             }


             if (progress < 1) {
                 requestAnimationFrame(update);
             } else {
                 // Ensure final value is exact and reset color
                 element.textContent = Math.round(end).toLocaleString('he-IL');
                 element.style.color = ''; // Reset to default CSS color rule

                 // Update budget/total profit specific colors
                 if (element.id === 'current-budget') {
                     element.classList.remove('loss'); // Budget might turn red if negative
                     if (end < 0) element.classList.add('loss');
                 } else if (element.id === 'total-profit') {
                      element.classList.remove('loss'); // Total profit might turn red if negative
                     if (end < 0) element.classList.add('loss');
                 }
             }
         }
         requestAnimationFrame(update);
     }


    function nextRound() {
        currentRound++;
        if (currentRound > maxRounds || currentBudget <= -50000) { // End game if budget drops significantly negative
            endGame();
            return;
        }

        // Animate section transition
        resultsArea.classList.remove('active');
        manuscriptsArea.classList.add('active');


        currentRoundElement.textContent = currentRound;
        budgetElement.textContent = currentBudget.toFixed(0).toLocaleString('he-IL');
        totalProfitElement.textContent = totalProfit.toFixed(0).toLocaleString('he-IL');

         // Update budget/total profit colors based on current state
         budgetElement.classList.remove('loss');
         if (currentBudget < 0) budgetElement.classList.add('loss');
         totalProfitElement.classList.remove('loss');
         if (totalProfit < 0) totalProfitElement.classList.add('loss');


        generateAndRenderManuscripts();
    }

    function endGame() {
        gameArea.style.display = 'none'; // Hide the main game UI container
        gameOverArea.style.display = 'block'; // Show the game over screen
        gameOverArea.classList.add('active'); // Activate for potential transition

        finalProfitElement.textContent = totalProfit.toFixed(0).toLocaleString('he-IL');

         // Update final profit color
        finalProfitElement.classList.remove('profit', 'loss');
         if (totalProfit > 0) {
             finalProfitElement.classList.add('profit');
             finalMessageElement.textContent = `כל הכבוד! ניהלת את ההוצאה בהצלחה לאורך ${currentRound - 1} שנים והרווחת סכום מרשים!`;
         } else if (totalProfit < 0) {
             finalProfitElement.classList.add('loss');
              finalMessageElement.textContent = currentBudget <= -50000 ?
                 `אוי לא! ההוצאה נקלעה לחובות עמוקים ונסגרה לאחר ${currentRound - 1} שנים.` :
                 `לצערנו, ההוצאה הסתיימה בהפסד לאחר ${currentRound - 1} שנים. אולי בפעם הבאה תצליח יותר?`;
         } else {
              finalMessageElement.textContent = `סיימת את המשחק לאחר ${currentRound - 1} שנים בנקודת איזון. לא הרווחת ולא הפסדת, הישג בפני עצמו בשוק תחרותי!`;
         }
    }

    function restartGame() {
        currentBudget = 100000;
        totalProfit = 0;
        currentRound = 1;
        acceptedBooks = [];

        gameOverArea.style.display = 'none'; // Hide game over
         gameOverArea.classList.remove('active');
        gameArea.style.display = 'block'; // Show the main game UI again

        // Ensure correct initial section is active
        resultsArea.classList.remove('active');
        decisionsArea.classList.remove('active');
        manuscriptsArea.classList.add('active');
         manuscriptsArea.style.display = 'block'; // Ensure display is block


        // Reset stat displays
        budgetElement.textContent = currentBudget.toFixed(0).toLocaleString('he-IL');
        totalProfitElement.textContent = totalProfit.toFixed(0).toLocaleString('he-IL');
        currentRoundElement.textContent = currentRound;

         // Reset stat colors
         budgetElement.classList.remove('loss');
         totalProfitElement.classList.remove('loss');


        generateAndRenderManuscripts();
    }

     // Helper to get genre color (simple example)
     function getGenreColor(genreName) {
         switch (genreName) {
             case "מותחן": return "#dc3545"; // Red
             case "פנטזיה": return "#6f42c1"; // Purple
             case "ספר ילדים": return "#ffc107"; // Yellow
             case "ספר עיון": return "#17a2b8"; // Teal
             case "שירה": return "#fd7e14"; // Orange
             case "מדע בדיוני": return "#007bff"; // Blue
             case "מדריך מעשי": return "#28a745"; // Green
             default: return "#343a40"; // Default dark gray
         }
     }

     // Get CSS variables for JS animation colors
     const varColors = {
        accentColor: getComputedStyle(document.documentElement).getPropertyValue('--accent-color').trim(),
        dangerColor: getComputedStyle(document.documentElement).getPropertyValue('--danger-color').trim()
     };


    function generateAndRenderManuscripts() {
         currentManuscripts = [];
         manuscriptListElement.innerHTML = ''; // Clear previous manuscripts

         for (let i = 0; i < initialManuscriptsCount; i++) {
            currentManuscripts.push(generateManuscript(i + 1 + (currentRound - 1) * initialManuscriptsCount)); // Ensure unique IDs
         }
         renderManuscripts(currentManuscripts);
         decisionsArea.style.display = 'none'; // Hide decisions area until selection
         resultsArea.style.display = 'none'; // Hide results area
         gameOverArea.style.display = 'none'; // Hide game over area
         simulateButton.disabled = true; // Disable simulate button initially
    }

    // Event Listeners
    simulateButton.addEventListener('click', simulateRound);
    nextRoundButton.addEventListener('click', nextRound);
    restartButton.addEventListener('click', restartGame);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';

        // Animate toggle
        if (isHidden) {
            explanationDiv.style.display = 'block';
            // Add a small delay for the display change to register before starting transition
            setTimeout(() => { explanationDiv.style.opacity = 1; }, 10);
            toggleExplanationButton.textContent = 'הסתר הסבר';
        } else {
            explanationDiv.style.opacity = 0;
             // Match the CSS transition duration before hiding completely
            setTimeout(() => { explanationDiv.style.display = 'none'; }, 500); // Should match CSS transition duration
            toggleExplanationButton.textContent = 'מה זה כל הסיפור הזה? (הסבר)';
        }
         explanationDiv.style.transition = 'opacity 0.5s ease-in-out';
    });


    // Initial game setup
    generateAndRenderManuscripts();
     // Initial display updates
     budgetElement.textContent = currentBudget.toFixed(0).toLocaleString('he-IL');
     totalProfitElement.textContent = totalProfit.toFixed(0).toLocaleString('he-IL');


</script>
```