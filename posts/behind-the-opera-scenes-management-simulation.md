---
title: "מאחורי הקלעים של האופרה: סימולציית ניהול"
english_slug: behind-the-opera-scenes-management-simulation
category: "ניהול"
tags:
  - אומנות
  - ניהול תרבות
  - סימולציה
  - כלכלה
  - מוסדות ללא כוונת רווח
---
# מאחורי הקלעים של האופרה: סימולציית ניהול

מה נדרש כדי להריץ בית אופרה בימינו? מעבר לשירה מדהימה ותלבושות מפוארות, מדובר בניהול פיננסי מורכב, קבלת החלטות אסטרטגיות, והתמודדות עם ציפיות סותרות של אמנים, קהל ותורמים. האם יש לכם את מה שצריך כדי לנהל מוסד תרבות יוקרתי?

<div id="opera-simulation-app">
    <div class="game-header">
         <h2 class="season-title">עונה <span id="current-season">1</span></h2>
         <div class="balance-display">יתרה מצטברת: <span id="total-balance" class="financial-value">₪500,000</span></div>
    </div>

    <div id="decisions" class="game-section active">
        <h3 class="section-title">קבל החלטות אסטרטגיות לעונה הקרובה:</h3>
        <div class="decisions-grid">
            <div class="decision-area">
                <h4>רפרטואר <span class="info-icon" title="איזון בין יצירות מוכרות לפחות מוכרות">?</span></h4>
                <label for="repertoire-mix">תמהיל אמנותי: <span id="repertoire-mix-value" class="slider-value">50%</span></label>
                <input type="range" id="repertoire-mix" min="0" max="100" value="50">
                 <p class="tip">0% קלאסי/פופולרי ◀ מושך קהל רחב יותר, סיכון אמנותי נמוך.<br>100% חדש/מודרני ◀ פוטנציאל לביקורות פורצות דרך, מושך קהל נישתי, סיכון גבוה.</p>
            </div>
            <div class="decision-area">
                <h4>ליהוק <span class="info-icon" title="בחירת הזמרים והבמאים">?</span></h4>
                <label for="casting-level">איכות ופרופיל: <span id="casting-level-value" class="slider-value">50%</span></label>
                <input type="range" id="casting-level" min="0" max="100" value="50">
                 <p class="tip">0% כישרונות עולים ◀ עלות נמוכה, סיכון גבוה בביצוע ובביקורות.<br>100% כוכבים בינלאומיים ◀ עלות גבוהה, פוטנציאל למכירות וביקורות מזהירות.</p>
            </div>
            <div class="decision-area">
                <h4>תמחור כרטיסים <span class="info-icon" title="קביעת מחירי הכניסה">?</span></h4>
                <label for="ticket-price">רמת מחיר: <span id="ticket-price-value" class="slider-value">50%</span></label>
                <input type="range" id="ticket-price" min="0" max="100" value="50">
                 <p class="tip">0% נמוך ◀ הכנסה לכרטיס נמוכה, פוטנציאל למכירת כרטיסים גבוהה.<br>100% גבוה ◀ הכנסה לכרטיס גבוהה, פחות מכירות, פוטנציאל לקהל אקסקלוסיבי.</p>
            </div>
            <div class="decision-area">
                <h4>שיווק ופרסום <span class="info-icon" title="השקעה בקידום ההפקות">?</span></h4>
                <label for="marketing-budget">תקציב שיווק: <span id="marketing-budget-value" class="slider-value">50%</span></label>
                <input type="range" id="marketing-budget" min="0" max="100" value="50">
                 <p class="tip">0% תקציב נמוך ◀ חשיפה מוגבלת, סיכון לירידה בקהל ובמכירות.<br>100% תקציב גבוה ◀ עלות גבוהה, פוטנציאל להגדיל מכירות, קהל ומודעות.</p>
            </div>
             <div class="decision-area">
                <h4>גיוס תרומות <span class="info-icon" title="מאמץ להשגת תמיכה כספית חיצונית">?</span></h4>
                <label for="fundraising-effort">מאמץ גיוס: <span id="fundraising-effort-value" class="slider-value">50%</span></label>
                <input type="range" id="fundraising-effort" min="0" max="100" value="50">
                 <p class="tip">0% מאמץ נמוך ◀ עלות נמוכה, פוטנציאל לתרומות נמוכות.<br>100% מאמץ גבוה ◀ עלות גבוהה (משאבים וכוח אדם), פוטנציאל לתרומות גבוהות.</p>
            </div>
        </div>
        <button id="advance-season" class="game-button primary">צאו לדרך!</button>
    </div>

    <div id="results" class="game-section hidden">
        <h3 class="section-title">סיכום עונה <span id="results-season"></span></h3>
        <div class="results-summary">
             <div id="financial-results" class="result-box">
                 <h4><i class="icon fas fa-money-bill-wave"></i> מצב פיננסי</h4>
                 <p>הכנסות מכרטיסים: <span id="income" class="financial-value"></span> <span class="trend-icon" id="income-trend"></span></p>
                 <p>הכנסות מתרומות: <span id="donations" class="financial-value"></span> <span class="trend-icon" id="donations-trend"></span></p>
                 <p>הוצאות תפעול: <span id="expenses" class="financial-value"></span> <span class="trend-icon" id="expenses-trend"></span></p>
                 <div class="separator"></div>
                 <p class="balance-change-row">שינוי יתרה העונה: <span id="balance-change" class="financial-value"></span> <span class="trend-icon" id="balance-change-trend"></span></p>
                 <p class="total-balance-row">יתרה מצטברת: <span id="total-balance-results" class="financial-value"></span> <span class="trend-icon" id="total-balance-trend"></span></p>
             </div>
             <div id="audience-results" class="result-box">
                 <h4><i class="icon fas fa-users"></i> קהל ושביעות רצון</h4>
                 <p>מכירת כרטיסים (% תפוסה): <span id="sales" class="percentage-value"></span>% <span class="trend-icon" id="sales-trend"></span></p>
                 <p>שביעות רצון קהל: <span id="audience-satisfaction" class="percentage-value"></span>% <span class="trend-icon" id="satisfaction-trend"></span></p>
             </div>
             <div id="artistic-results" class="result-box">
                 <h4><i class="icon fas fa-star"></i> מוניטין אמנותי</h4>
                 <p>ביקורות מבקרים: <span id="critic-reviews" class="score-value"></span>/100 <span class="trend-icon" id="reviews-trend"></span></p>
             </div>
        </div>
        <div id="summary-message" class="summary-message"></div>
         <div class="results-actions">
            <button id="next-season" class="game-button secondary hidden">המשך לעונה הבאה</button>
            <button id="restart-game" class="game-button danger hidden">התחל משחק חדש</button>
        </div>
    </div>

    <button id="toggle-explanation" class="explanation-button"><i class="icon fas fa-book"></i> הצג/הסתר הסבר על ניהול מוסדות אופרה</button>

    <div id="explanation" class="explanation-section hidden">
        <h2>הסבר: ניהול מוסד אופרה</h2>
        <p>ניהול מוסד תרבות כמו בית אופרה הוא משימה מורכבת הדורשת איזונים עדינים בין שאיפות אמנותיות, יציבות פיננסית, והתמודדות עם ציפיות מגוונות של בעלי עניין.</p>

        <h3>מהו בית אופרה כמוסד תרבות וכלכלי ייחודי?</h3>
        <p>בית אופרה הוא לרוב מוסד ללא כוונת רווח (מלכ"ר), הפועל למען מטרה ציבורית-תרבותית. המבנה הארגוני כולל בדרך כלל מועצה מנהלת/ועד מנהל, הנהלה אמנותית, והנהלה פיננסית/אדמיניסטרטיבית.
        מקורות ההכנסה העיקריים הם מכירת כרטיסים, תרומות (מאנשים פרטיים, חברות, קרנות), ותמיכה ממשלתית/עירונית. הוצאות עיקריות כוללות עלויות הפקה (שכר אמנים, תפאורה, תלבושות), שכר עובדים אדמיניסטרטיביים וטכניים, שיווק, תחזוקה, וגיוס תרומות.</p>

        <h3>האתגרים המרכזיים בניהול מוסדות אומנות: איזון בין איכות אמנותית לכדאיות כלכלית</h3>
        <p>האתגר הבסיסי הוא לשמור על מצוינות אמנותית (הפקות איכותיות, ליהוק ברמה גבוהה) תוך שמירה על מסגרת תקציבית. החלטות אמנותיות יקרות עלולות לערער את היציבות הפיננסית, בעוד קיצוצים בתקציב האמנותי עלולים לפגוע במוניטין וביכולת למשוך קהל ותורמים.</p>

        <h3>ניהול רפרטואר וליהוק: שיקולים אמנותיים, שיווקיים ותקציביים</h3>
        <p>בחירת היצירות להעלאה (רפרטואר) דורשת איזון בין יצירות מוכרות ופופולריות המושכות קהל רחב, לבין יצירות חדשות או נדירות התורמות למוניטין האמנותי. ליהוק זמרים, מנצחים ובמאים כולל החלטה בין כוכבים בעלי שם עולמי (שכר גבוה, משיכת קהל) לבין כישרונות צעירים ומבטיחים (שכר נמוך יותר, פוטנציאל לביקורות טובות אך פחות משיכה ראשונית). כל החלטה כזו משפיעה ישירות על התקציב ועל הפוטנציאל האמנותי והמסחרי של ההפקה.</p>

        <h3>אסטרטגיות תמחור ומכירה: השפעת מחיר הכרטיס על הכנסות וקהל</h3>
        <p>קביעת מחיר הכרטיס משפיעה על שני גורמים מרכזיים: ההכנסה לכרטיס ומספר הכרטיסים הנמכרים. מחיר גבוה יותר מגדיל את ההכנסה מכל כרטיס שנמכר, אך עלול להרחיק חלק מהקהל ולהוריד את אחוז התפוסה. מחיר נמוך יותר יכול למשוך יותר קהל ולהגדיל את אחוז התפוסה, אך יוריד את ההכנסה הכוללת ממכירת כרטיסים. אסטרטגיית תמחור נכונה חייבת להתחשב בגמישות הביקוש של הקהל.</p>

        <h3>שיווק וגיוס תרומות: חשיבות בניית קהל נאמן ותמיכה חיצונית</h3>
        <p>שיווק אפקטיבי חיוני למשיכת קהל חדש ולשימור קהל קיים. תקציב שיווק משפיע ישירות על החשיפה של ההפקות. גיוס תרומות הוא מקור הכנסה קריטי עבור רוב מוסדות התרבות, ומפצה לרוב על הפער בין הכנסות ממכירת כרטיסים להוצאות תפעול. מאמצי גיוס תרומות (אירועים, קשר אישי עם תורמים) דורשים השקעה של זמן ומשאבים אך חיוניים להישרדות פיננסית.</p>

        <h3>מדדי הצלחה במוסדות תרבות: מעבר למדדים פיננסיים</h3>
        <p>הצלחה של בית אופרה אינה נמדדת רק ברווח כספי (שאינו המטרה במלכ"ר). מדדים נוספים כוללים: אחוז תפוסה וסך מכירת כרטיסים (מעיד על משיכת קהל), שביעות רצון הקהל (נאמנות קהל), ביקורות מבקרים ופרסים (מוניטין אמנותי), ומעל הכל - ההשפעה התרבותית והחברתית של המוסד (נגישות, חינוך, תרומה לקהילה).</p>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'); /* For icons */

    :root {
        --primary-color: #6a1b9a; /* Deep Purple */
        --secondary-color: #ab47bc; /* Lighter Purple */
        --accent-color: #ffee58; /* Bright Yellow */
        --background-color: #f3e5f5; /* Very Light Purple */
        --card-background: #ffffff;
        --text-color: #212121;
        --heading-color: #4a148c; /* Darker Purple */
        --border-color: #e1bee7; /* Light Purple Border */
        --success-color: #4caf50;
        --warning-color: #ff9800;
        --danger-color: #f44336;
        --info-color: #2196f3;
    }

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background-color: var(--background-color);
        color: var(--text-color);
        direction: rtl; /* Hebrew support */
        text-align: right; /* Hebrew support */
    }

    h1, h2, h3, h4 {
        color: var(--heading-color);
        font-weight: 700;
        margin-bottom: 10px;
    }

    h1 { font-size: 2em; margin-bottom: 20px; text-align: center; }
    h2 { font-size: 1.6em; }
    h3 { font-size: 1.3em; }
    h4 { font-size: 1.1em; color: var(--primary-color); margin-bottom: 8px; }

    #opera-simulation-app {
        background-color: var(--card-background);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        max-width: 900px;
        margin: 20px auto;
        overflow: hidden;
        position: relative;
    }

    .game-header {
        text-align: center;
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 2px dashed var(--border-color);
    }

    .season-title {
        color: var(--primary-color);
        display: inline-block;
        margin-left: 20px; /* Space between title and balance */
    }

    .balance-display {
        font-size: 1.2em;
        font-weight: 700;
        color: var(--heading-color);
        display: inline-block;
    }

    .game-section {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        position: absolute;
        top: 150px; /* Adjust based on header height */
        left: 30px;
        right: 30px;
        bottom: 30px; /* Leave space for explanation button */
        overflow-y: auto; /* Enable scrolling if content overflows */
        padding-bottom: 20px; /* Ensure space above explanation button */
    }

    .game-section.active {
        opacity: 1;
        transform: translateY(0);
        position: static; /* Restore normal flow when active */
        height: auto;
    }

    .section-title {
         margin-bottom: 20px;
         text-align: center;
         color: var(--primary-color);
    }

    .decisions-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin-bottom: 20px;
    }

    .decision-area {
        background-color: var(--background-color);
        padding: 15px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

     .decision-area:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
     }

    .decision-area label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: var(--text-color);
    }

    .decision-area input[type="range"] {
        width: calc(100% - 70px); /* Adjust based on span width */
        vertical-align: middle;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: var(--border-color);
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .decision-area input[type="range"]:hover {
        opacity: 1;
    }

    .decision-area input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--secondary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--primary-color);
    }

    .decision-area input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--secondary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--primary-color);
    }


     .slider-value {
        display: inline-block;
        width: 60px;
        text-align: left; /* Align values to the left */
        vertical-align: middle;
        font-weight: bold;
        color: var(--primary-color);
     }

    .tip {
        font-size: 0.85em;
        color: #555;
        margin-top: 8px;
        padding-top: 8px;
        border-top: 1px dashed var(--border-color);
    }

    .game-button {
        display: block;
        width: 100%;
        background-color: var(--primary-color);
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.2em;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
    }

    .game-button.secondary {
        background-color: var(--secondary-color);
    }

    .game-button.danger {
        background-color: var(--danger-color);
        margin-top: 10px; /* Space between next and restart */
    }

    .game-button:hover:not(:disabled) {
        background-color: var(--heading-color);
        transform: translateY(-2px);
    }
     .game-button.secondary:hover:not(:disabled) {
        background-color: var(--primary-color);
     }
      .game-button.danger:hover:not(:disabled) {
        background-color: #d32f2f; /* Darker red */
     }

    .game-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
    }

    .results-summary {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-bottom: 20px;
    }

    .result-box {
        background-color: var(--background-color);
        padding: 15px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        opacity: 0; /* Initial state for animation */
        transform: translateY(10px); /* Initial state for animation */
    }

     .result-box p {
         margin: 8px 0;
         font-size: 1em;
         position: relative; /* For trend icon positioning */
     }

     .result-box h4 {
         margin-top: 0;
         margin-bottom: 10px;
         padding-bottom: 8px;
         border-bottom: 1px dashed var(--border-color);
         display: flex;
         align-items: center;
     }

     .result-box h4 .icon {
         margin-left: 10px; /* Space for RTL */
         color: var(--primary-color);
     }

     .financial-value, .percentage-value, .score-value {
        font-weight: bold;
        color: var(--primary-color);
        transition: color 0.5s ease; /* Animate color change */
     }

     .financial-value.positive { color: var(--success-color); }
     .financial-value.negative { color: var(--danger-color); }
     .financial-value.neutral { color: var(--text-color); }

     .percentage-value.good { color: var(--success-color); }
     .percentage-value.average { color: var(--warning-color); }
     .percentage-value.poor { color: var(--danger-color); }

     .score-value.excellent { color: var(--success-color); }
     .score-value.good { color: var(--secondary-color); }
     .score-value.average { color: var(--warning-color); }
     .score-value.poor { color: var(--danger-color); }

     .trend-icon {
         display: inline-block;
         margin-right: 5px; /* Space for RTL */
         font-size: 0.9em;
         vertical-align: middle;
         transition: opacity 0.5s ease;
     }

     .trend-icon.up { color: var(--success-color); }
     .trend-icon.down { color: var(--danger-color); }
     .trend-icon.neutral { color: #9e9e9e; } /* Grey */


    .separator {
        height: 1px;
        background-color: var(--border-color);
        margin: 10px 0;
    }

    .balance-change-row {
         font-size: 1.1em !important;
    }
    .total-balance-row {
         font-size: 1.2em !important;
         font-weight: bold !important;
         margin-top: 15px !important;
         padding-top: 10px !important;
         border-top: 2px solid var(--border-color);
    }


    .summary-message {
        font-weight: bold;
        margin-top: 20px;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 1.1em;
        transition: background-color 0.5s ease, border-color 0.5s ease;
    }

    .summary-message.success {
        background-color: #e8f5e9;
        border: 1px solid var(--success-color);
        color: var(--success-color);
    }
    .summary-message.warning {
         background-color: #fffde7;
         border: 1px solid var(--warning-color);
         color: var(--warning-color);
    }
     .summary-message.danger {
         background-color: #ffebee;
         border: 1px solid var(--danger-color);
         color: var(--danger-color);
    }

     .results-actions {
         display: flex;
         justify-content: center;
         gap: 20px;
         margin-top: 20px;
         flex-wrap: wrap; /* Ensure buttons wrap on small screens */
     }
    .results-actions button {
        width: auto; /* Override default button width */
        flex-grow: 1;
        max-width: 200px;
         margin-top: 0; /* Reset default button margin */
    }


    .hidden {
        display: none !important; /* Use !important to ensure it overrides .active */
    }

    .explanation-button {
         display: block;
         margin: 30px auto 0; /* Push to bottom, center */
         background-color: var(--info-color);
         width: auto;
         padding: 10px 20px;
         font-size: 1em;
    }
    .explanation-button:hover {
         background-color: #1565c0; /* Darker info color */
    }

    .explanation-section {
        margin-top: 30px;
        padding-top: 25px;
        border-top: 2px dashed var(--border-color);
    }

    .explanation-section h3 {
        color: var(--secondary-color);
        margin-top: 15px;
        margin-bottom: 8px;
    }

    .explanation-section p {
        margin-bottom: 15px;
        text-align: justify;
    }

    .info-icon {
        font-size: 0.8em;
        color: var(--info-color);
        margin-left: 5px;
        cursor: help;
    }

     /* Animation for result boxes */
     .result-box.show {
         opacity: 1;
         transform: translateY(0);
     }

    /* Animation for numbers counting up */
    .number-animation {
        display: inline-block; /* Ensure span doesn't break layout */
    }

     @keyframes pulse {
         0% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.05); opacity: 0.8; }
         100% { transform: scale(1); opacity: 1; }
     }
      .summary-message.success,
      .summary-message.warning,
      .summary-message.danger {
          animation: pulse 1s ease-in-out infinite alternate;
      }
      /* Disable pulse after a few cycles or on hover */
      .summary-message:hover {
          animation: none;
      }


</style>

<script>
    const gameContainer = document.getElementById('opera-simulation-app');
    const currentSeasonSpan = document.getElementById('current-season');
    const totalBalanceHeaderSpan = document.getElementById('total-balance'); // Balance in header

    const decisionsDiv = document.getElementById('decisions');
    const resultsDiv = document.getElementById('results');

    const resultsSeasonSpan = document.getElementById('results-season');
    const incomeSpan = document.getElementById('income');
    const donationsSpan = document.getElementById('donations');
    const expensesSpan = document.getElementById('expenses');
    const balanceChangeSpan = document.getElementById('balance-change');
    const totalBalanceResultsSpan = document.getElementById('total-balance-results'); // Balance in results

    const salesSpan = document.getElementById('sales');
    const audienceSatisfactionSpan = document.getElementById('audience-satisfaction');
    const criticReviewsSpan = document.getElementById('critic-reviews');

    const summaryMessageDiv = document.getElementById('summary-message');
    const advanceSeasonButton = document.getElementById('advance-season');
    const nextSeasonButton = document.getElementById('next-season');
    const restartGameButton = document.getElementById('restart-game');

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    // Trend Icons
    const incomeTrendIcon = document.getElementById('income-trend');
    const donationsTrendIcon = document.getElementById('donations-trend');
    const expensesTrendIcon = document.getElementById('expenses-trend');
    const balanceChangeTrendIcon = document.getElementById('balance-change-trend');
    const totalBalanceTrendIcon = document.getElementById('total-balance-trend');
    const salesTrendIcon = document.getElementById('sales-trend');
    const satisfactionTrendIcon = document.getElementById('satisfaction-trend');
    const reviewsTrendIcon = document.getElementById('reviews-trend');


    // Sliders and their value spans
    const repertoireMixSlider = document.getElementById('repertoire-mix');
    const repertoireMixValue = document.getElementById('repertoire-mix-value');
    const castingLevelSlider = document.getElementById('casting-level');
    const castingLevelValue = document.getElementById('casting-level-value');
    const ticketPriceSlider = document.getElementById('ticket-price');
    const ticketPriceValue = document.getElementById('ticket-price-value');
    const marketingBudgetSlider = document.getElementById('marketing-budget');
    const marketingBudgetValue = document.getElementById('marketing-budget-value');
    const fundraisingEffortSlider = document.getElementById('fundraising-effort');
    const fundraisingEffortValue = document.getElementById('fundraising-effort-value');

    // Initial Game State
    let gameState = {};
    let previousSeasonResults = null; // Store results to show trend

    const initialGameState = {
        season: 1,
        balance: 750000, // Slightly higher starting balance
        audienceSatisfaction: 75, // Out of 100
        artisticReputation: 75, // Out of 100
        baseExpenses: 900000, // Base operational costs per season
        baseTicketPriceEffect: 12000, // Base income multiplier per % attendance at default price (scaled up)
        baseDonations: 250000, // Base donations per season
        baseAttendance: 75, // Base attendance percentage
        baseReviews: 75 // Base review score
    };

    // --- Helper Functions ---

    // Function to update slider value display
    function updateSliderValueDisplay(slider, valueSpan) {
        valueSpan.textContent = `${slider.value}%`;
    }

     // Function to animate number change
    function animateNumber(spanElement, startValue, endValue, duration = 1000) {
        let startTime = null;
        const range = endValue - startValue;
        const start = +startValue; // Ensure startValue is number
        const end = +endValue; // Ensure endValue is number

        // Determine formatting (currency or percentage)
        const isCurrency = spanElement.parentElement.id.includes('financial');
        const isPercentage = spanElement.parentElement.id.includes('audience') && spanElement.id !== 'audience-satisfaction';
        const isScore = spanElement.parentElement.id.includes('artistic');


        function step(timestamp) {
            if (!startTime) startTime = timestamp;
            const progress = Math.min((timestamp - startTime) / duration, 1);
            const currentValue = start + range * progress;

            let formattedValue;
            if (isCurrency) {
                 formattedValue = '₪' + Math.round(currentValue).toLocaleString();
             } else if (isPercentage) {
                 formattedValue = Math.round(currentValue); // % added in HTML
             } else if (isScore) {
                 formattedValue = Math.round(currentValue); // /100 added in HTML
             }
             else {
                 formattedValue = Math.round(currentValue); // Default for satisfaction etc.
             }

            spanElement.textContent = formattedValue;

            if (progress < 1) {
                requestAnimationFrame(step);
            } else {
                 // Ensure final value is exactly endValue after animation
                 if (isCurrency) {
                    spanElement.textContent = '₪' + Math.round(end).toLocaleString();
                 } else if (isPercentage) {
                     spanElement.textContent = Math.round(end);
                 } else if (isScore) {
                     spanElement.textContent = Math.round(end);
                 }
                 else {
                    spanElement.textContent = Math.round(end);
                 }
            }
        }

        requestAnimationFrame(step);
    }

    // Function to update trend icons and colors
    function updateTrend(valueSpan, trendIcon, currentValue, previousValue) {
        trendIcon.classList.remove('up', 'down', 'neutral');
        valueSpan.classList.remove('positive', 'negative', 'neutral', 'good', 'average', 'poor', 'excellent');

        let trend = 0; // 0: neutral, 1: up, -1: down
        if (previousSeasonResults) {
             if (currentValue > previousValue) trend = 1;
             else if (currentValue < previousValue) trend = -1;
        } else {
             // For first season, assume neutral trend
             trendIcon.classList.add('neutral');
             trendIcon.innerHTML = ' '; // No icon initially or just space
        }


        if (trend === 1) {
            trendIcon.classList.add('up');
            trendIcon.innerHTML = '<i class="fas fa-arrow-up"></i>';
        } else if (trend === -1) {
            trendIcon.classList.add('down');
            trendIcon.innerHTML = '<i class="fas fa-arrow-down"></i>';
        } else if (previousSeasonResults) { // Only show neutral icon if it's not the first season
             trendIcon.classList.add('neutral');
             trendIcon.innerHTML = '<i class="fas fa-minus"></i>';
        }


        // Add color classes based on value type
        if (valueSpan.parentElement.id.includes('financial')) {
             if (currentValue > 0) valueSpan.classList.add('positive');
             else if (currentValue < 0) valueSpan.classList.add('negative');
             else valueSpan.classList.add('neutral');
        } else if (valueSpan.parentElement.id.includes('audience')) {
            // Sales & Satisfaction percentages
             if (currentValue >= 85) valueSpan.classList.add('good');
             else if (currentValue >= 60) valueSpan.classList.add('average');
             else valueSpan.classList.add('poor');
        } else if (valueSpan.parentElement.id.includes('artistic')) {
            // Reviews score
             if (currentValue >= 90) valueSpan.classList.add('excellent');
             else if (currentValue >= 75) valueSpan.classList.add('good');
             else if (currentValue >= 50) valueSpan.classList.add('average');
             else valueSpan.classList.add('poor');
        }
    }


    // --- Game Logic Functions ---

    function initializeGame() {
        gameState = {...initialGameState}; // Reset to initial state
        previousSeasonResults = null; // Clear previous results

        currentSeasonSpan.textContent = gameState.season;
        totalBalanceHeaderSpan.textContent = '₪' + Math.round(gameState.balance).toLocaleString();
        totalBalanceHeaderSpan.classList.remove('positive', 'negative', 'neutral');
        if (gameState.balance >= 0) totalBalanceHeaderSpan.classList.add('positive'); else totalBalanceHeaderSpan.classList.add('negative');


        // Reset sliders to default and update display
        repertoireMixSlider.value = 50;
        castingLevelSlider.value = 50;
        ticketPriceSlider.value = 50;
        marketingBudgetSlider.value = 50;
        fundraisingEffortSlider.value = 50;
        updateSliderValueDisplay(repertoireMixSlider, repertoireMixValue);
        updateSliderValueDisplay(castingLevelSlider, castingLevelValue);
        updateSliderValueDisplay(ticketPriceSlider, ticketPriceValue);
        updateSliderValueDisplay(marketingBudgetSlider, marketingBudgetValue);
        updateSliderValueDisplay(fundraisingEffortSlider, fundraisingEffortValue);

        // Hide results, show decisions
        resultsDiv.classList.remove('active');
        decisionsDiv.classList.add('active');
        resultsDiv.classList.add('hidden'); // Ensure hidden for display:none
        decisionsDiv.classList.remove('hidden'); // Ensure not hidden

        nextSeasonButton.classList.add('hidden');
        restartGameButton.classList.add('hidden');
        advanceSeasonButton.disabled = false;

        summaryMessageDiv.classList.remove('success', 'warning', 'danger');
        summaryMessageDiv.textContent = '';

         // Clear previous results values and trends
        incomeSpan.textContent = ''; incomeTrendIcon.innerHTML = ''; incomeSpan.className = '';
        donationsSpan.textContent = ''; donationsTrendIcon.innerHTML = ''; donationsSpan.className = '';
        expensesSpan.textContent = ''; expensesTrendIcon.innerHTML = ''; expensesSpan.className = '';
        balanceChangeSpan.textContent = ''; balanceChangeTrendIcon.innerHTML = ''; balanceChangeSpan.className = '';
        totalBalanceResultsSpan.textContent = ''; totalBalanceTrendIcon.innerHTML = ''; totalBalanceResultsSpan.className = '';
        salesSpan.textContent = ''; salesTrendIcon.innerHTML = ''; salesSpan.className = '';
        audienceSatisfactionSpan.textContent = ''; satisfactionTrendIcon.innerHTML = ''; audienceSatisfactionSpan.className = '';
        criticReviewsSpan.textContent = ''; reviewsTrendIcon.innerHTML = ''; criticReviewsSpan.className = '';

        // Reset result box animations state
        document.querySelectorAll('.result-box').forEach(box => box.classList.remove('show'));

    }

    function advanceSeason() {
        // Disable button immediately
        advanceSeasonButton.disabled = true;

        // Get decisions from sliders (values 0-100)
        const repertoireMix = parseInt(repertoireMixSlider.value); // 0=classic, 100=new
        const castingLevel = parseInt(castingLevelSlider.value); // 0=promising, 100=stars
        const ticketPrice = parseInt(ticketPriceSlider.value); // 0=low, 100=high
        const marketingBudget = parseInt(marketingBudgetSlider.value); // 0=low, 100=high
        const fundraisingEffort = parseInt(fundraisingEffortSlider.value); // 0=low, 100=high

         // Store current state before calculations for trend comparison
        previousSeasonResults = {
             balance: gameState.balance,
             audienceSatisfaction: gameState.audienceSatisfaction,
             artisticReputation: gameState.artisticReputation,
             income: null, // Will calculate these
             donations: null,
             expenses: null,
             balanceChange: null,
             sales: null,
             reviews: null
        };


        // --- Calculate Outcomes ---

        // Expenses: Base + Casting cost + Marketing cost + Fundraising effort cost
        // Casting cost: scales significantly
        // Marketing cost: scales linearly
        // Fundraising cost: scales less linearly, more resources for higher effort
        let seasonExpenses = gameState.baseExpenses;
        seasonExpenses += castingLevel * 6000; // Cost scales significantly with casting level
        seasonExpenses += marketingBudget * 2500; // Cost scales with marketing
        seasonExpenses += Math.pow(fundraisingEffort, 1.5) * 500; // Cost scales non-linearly with fundraising effort


        // Attendance (%): Base + Marketing effect - Price effect + Audience Satisfaction effect + Reputation effect - Repertoire risk + Randomness
        let attendance = gameState.baseAttendance;
        attendance += (marketingBudget - 50) * 0.3; // Marketing boost/drag
        attendance -= (ticketPrice - 50) * 0.4; // Price drag/boost - price is a significant factor
        attendance += (gameState.audienceSatisfaction - initialGameState.audienceSatisfaction) * 0.2; // Past satisfaction boost/drag
        attendance += (gameState.artisticReputation - initialGameState.artisticReputation) * 0.1; // Reputation boost/drag
        attendance -= Math.pow(Math.abs(repertoireMix - 50), 1.2) * 0.08; // Higher penalty for being far from 50/50 mix

         // Add some general randomness to attendance
        attendance += (Math.random() - 0.5) * 5;


        attendance = Math.max(10, Math.min(100, attendance)); // Cap attendance

        // Ticket Income: Attendance % * Base income per % * Price Multiplier
        // Price multiplier: at 0% price = 0.6, at 50% price = 1.0, at 100% price = 1.8 (higher prices can really boost revenue per ticket)
        const priceMultiplier = 0.6 + (ticketPrice / 100) * 1.2;
        let ticketIncome = (attendance / 100) * gameState.baseTicketPriceEffect * priceMultiplier * 100; // Total income based on % and price


        // Donations: Base + Fundraising effect + Balance effect + Reputation effect + Randomness
        let seasonDonations = gameState.baseDonations;
        seasonDonations += (fundraisingEffort - 50) * 4000; // Fundraising effort boost/drag
        // Influence of balance and reputation on donations - donors like stability and prestige
        seasonDonations += (gameState.balance / 500000) * 10000; // Slight boost for stable finances
        seasonDonations += (gameState.artisticReputation - initialGameState.artisticReputation) * 3000; // Good reputation attracts donors
         // Add randomness to donations (donor whims)
        seasonDonations += (Math.random() - 0.5) * 80000;


         seasonDonations = Math.max(100000, seasonDonations); // Minimum donation floor


        // Critic Reviews (Artistic Reputation change): Base + Casting effect + Repertoire effect + Interaction + Randomness
        let newReviewScore = gameState.baseReviews;
        newReviewScore += (castingLevel - 50) * 0.4; // Casting level is significant for reviews
        // Repertoire effect: Modern can be hit or miss, classic is safer
        newReviewScore += (repertoireMix - 50) * 0.1; // Slight boost for modern if successful, drag for classic
        // Interaction: High casting + modern repertoire has potential for very high/low reviews (higher variance)
        // High casting + classic repertoire is safer (lower variance)
         let reviewRandomness = (Math.random() - 0.5) * 15; // Base randomness
         if (repertoireMix > 70 || repertoireMix < 30 || castingLevel > 70 || castingLevel < 30) {
             reviewRandomness *= 1.5; // Increase randomness with more extreme decisions
         }
         newReviewScore += reviewRandomness;


        newReviewScore = Math.max(20, Math.min(100, newReviewScore)); // Cap reviews

        // Audience Satisfaction (changes based on price, repertoire, reviews, sales, casting)
        let newAudienceSatisfaction = gameState.audienceSatisfaction;
        newAudienceSatisfaction -= (ticketPrice - 50) * 0.3; // Price drag - significant factor
        newAudienceSatisfaction += (newReviewScore - gameState.artisticReputation) * 0.4; // Reviews influence satisfaction strongly
        newAudienceSatisfaction += (attendance - gameState.baseAttendance) * 0.2; // Higher attendance correlation
        // Repertoire effect on satisfaction: Extreme repertoire might alienate, classic is safe but potentially boring
        newAudienceSatisfaction -= Math.pow(Math.abs(repertoireMix - 50), 1.1) * 0.08; // Penalty for being too extreme
        // Casting effect on satisfaction: Stars can boost satisfaction, poor talents hurt
        newAudienceSatisfaction += (castingLevel - 50) * 0.15;


         // Add randomness to satisfaction
        newAudienceSatisfaction += (Math.random() - 0.5) * 8;


        newAudienceSatisfaction = Math.max(10, Math.min(100, newAudienceSatisfaction)); // Cap satisfaction


        // Financial Summary
        const seasonIncome = ticketIncome + seasonDonations;
        const balanceChange = seasonIncome - seasonExpenses;

        // Update state for next season
        gameState.balance += balanceChange;
        gameState.season++;
        gameState.audienceSatisfaction = newAudienceSatisfaction;
        gameState.artisticReputation = newReviewScore;

         // Store calculated values for trend comparison in next season
        previousSeasonResults.income = ticketIncome;
        previousSeasonResults.donations = seasonDonations;
        previousSeasonResults.expenses = seasonExpenses;
        previousSeasonResults.balanceChange = balanceChange;
        previousSeasonResults.sales = attendance;
        previousSeasonResults.reviews = newReviewScore;


        // --- Display Results ---

        // Animate transition between sections
        decisionsDiv.classList.remove('active');
        // Delay adding 'hidden' class until after animation starts
         setTimeout(() => decisionsDiv.classList.add('hidden'), 600); // Match CSS transition duration

        resultsDiv.classList.remove('hidden');
        setTimeout(() => resultsDiv.classList.add('active'), 100); // Small delay before making results active

        resultsSeasonSpan.textContent = gameState.season - 1; // Display season just finished

        // Animate numbers and update trends
        animateNumber(incomeSpan, 0, ticketIncome);
        updateTrend(incomeSpan, incomeTrendIcon, ticketIncome, previousSeasonResults.income);

        animateNumber(donationsSpan, 0, seasonDonations);
        updateTrend(donationsSpan, donationsTrendIcon, seasonDonations, previousSeasonResults.donations);

        animateNumber(expensesSpan, 0, seasonExpenses);
        updateTrend(expensesSpan, expensesTrendIcon, seasonExpenses, previousSeasonResults.expenses);

        animateNumber(balanceChangeSpan, 0, balanceChange);
        updateTrend(balanceChangeSpan, balanceChangeTrendIcon, balanceChange, previousSeasonResults.balanceChange);

        // Animate total balance update in both places
        animateNumber(totalBalanceResultsSpan, gameState.balance - balanceChange, gameState.balance);
        animateNumber(totalBalanceHeaderSpan, gameState.balance - balanceChange, gameState.balance);
        updateTrend(totalBalanceResultsSpan, totalBalanceTrendIcon, gameState.balance, previousSeasonResults.balance);
         // Update header balance color immediately
        totalBalanceHeaderSpan.classList.remove('positive', 'negative', 'neutral');
        if (gameState.balance >= 0) totalBalanceHeaderSpan.classList.add('positive'); else totalBalanceHeaderSpan.classList.add('negative');


        animateNumber(salesSpan, 0, attendance);
        updateTrend(salesSpan, salesTrendIcon, attendance, previousSeasonResults.sales);

        animateNumber(audienceSatisfactionSpan, previousSeasonResults.audienceSatisfaction, newAudienceSatisfaction);
        updateTrend(audienceSatisfactionSpan, satisfactionTrendIcon, newAudienceSatisfaction, previousSeasonResults.audienceSatisfaction);

        animateNumber(criticReviewsSpan, previousSeasonResults.artisticReputation, newReviewScore);
        updateTrend(criticReviewsSpan, reviewsTrendIcon, newReviewScore, previousSeasonResults.artisticReputation);


        // Add animations to result boxes
        document.querySelectorAll('.result-box').forEach((box, index) => {
            box.style.animationDelay = `${index * 0.15}s`; // Stagger animation
            box.classList.add('show');
        });


        // --- Game Over Check / Summary ---
        summaryMessageDiv.classList.remove('success', 'warning', 'danger');
        let message = "";
        let isGameOver = false;

        // Game Over Conditions
        if (gameState.balance < -1000000 && gameState.season > 2) { // Significant, prolonged debt
             message = "חובות ענק! בית האופרה נאלץ לסגור את שעריו לצמיתות בשל קשיים פיננסיים.";
             summaryMessageDiv.classList.add('danger');
             isGameOver = true;
        } else if (gameState.audienceSatisfaction < 20 && gameState.season > 2) { // Extremely low satisfaction
             message = "הקהל נוטש בהמוניו. ללא תמיכת הקהל, אין עתיד לבית האופרה.";
             summaryMessageDiv.classList.add('danger');
             isGameOver = true;
        } else if (gameState.artisticReputation < 20 && gameState.season > 2) { // Extremely low reviews
             message = "ביקורות קטלניות פוגעות במוניטין. האמנים והתורמים מתרחקים, ובית האופרה קורס.";
             summaryMessageDiv.classList.add('danger');
             isGameOver = true;
        }
         // Intermediate warnings
        else if (gameState.balance < 0) {
             message = "המצב הפיננסי בגירעון. יש לשקול צעדים להגדלת הכנסות או צמצום הוצאות דחוף.";
             summaryMessageDiv.classList.add('warning');
        } else if (balanceChange < -200000) { // Significant loss this season
              message = "עונה זו הסתיימה בהפסד משמעותי. יתרת הכסף ירדה באופן מדאיג.";
              summaryMessageDiv.classList.add('warning');
        }
        else if (newAudienceSatisfaction < 40) {
             message = "שביעות רצון הקהל נמוכה. ייתכן שהרפרטואר, הליהוק או המחיר לא היו לטעמו.";
             summaryMessageDiv.classList.add('warning');
        }
        else if (newReviewScore < 40) {
             message = "ביקורות המבקרים חלשות. אולי הליהוק או הרפרטואר לא פגעו בול.";
             summaryMessageDiv.classList.add('warning');
        }
        // Success messages
        else if (gameState.balance > 1500000 && balanceChange > 0 && newAudienceSatisfaction > 85 && newReviewScore > 85) {
             message = "עונה מבריקה בכל החזיתות! הצלחה אמנותית, קהל מרוצה ויציבות פיננסית איתנה.";
             summaryMessageDiv.classList.add('success');
        }
         else if (balanceChange > 0) {
             message = "העונה הסתיימה בהצלחה! המצב הפיננסי השתפר/נשמר. המשיכו כך!";
             summaryMessageDiv.classList.add('success');
         }
         else {
              message = "עונה רגועה הסתיימה. שקלו כיצד להמשיך לצמוח ולהשתפר.";
              summaryMessageDiv.classList.add('neutral'); // Add a neutral style
              summaryMessageDiv.style.backgroundColor = '#eeeeee';
              summaryMessageDiv.style.borderColor = '#cccccc';
              summaryMessageDiv.style.color = '#555555';
              summaryMessageDiv.style.animation = 'none'; // Disable pulse for neutral
         }

         summaryMessageDiv.textContent = message;


         if (isGameOver) {
             nextSeasonButton.classList.add('hidden');
             restartGameButton.classList.remove('hidden');
         } else {
             nextSeasonButton.classList.remove('hidden');
             restartGameButton.classList.add('hidden');
             advanceSeasonButton.disabled = false; // Re-enable for next season transition
         }
    }

    function goToNextSeason() {
        // Hide results, show decisions with animation
        resultsDiv.classList.remove('active');
        // Delay adding 'hidden' class
         setTimeout(() => {
             resultsDiv.classList.add('hidden');
             decisionsDiv.classList.remove('hidden');
             decisionsDiv.classList.add('active');
         }, 600); // Match CSS transition duration


        currentSeasonSpan.textContent = gameState.season;
        totalBalanceHeaderSpan.textContent = '₪' + Math.round(gameState.balance).toLocaleString();
        totalBalanceHeaderSpan.classList.remove('positive', 'negative', 'neutral');
        if (gameState.balance >= 0) totalBalanceHeaderSpan.classList.add('positive'); else totalBalanceHeaderSpan.classList.add('negative');


        nextSeasonButton.classList.add('hidden');
        summaryMessageDiv.textContent = ''; // Clear message
        summaryMessageDiv.classList.remove('success', 'warning', 'danger');
         summaryMessageDiv.style.backgroundColor = ''; // Reset neutral style
         summaryMessageDiv.style.borderColor = '';
         summaryMessageDiv.style.color = '';
         summaryMessageDiv.style.animation = '';


        advanceSeasonButton.disabled = false; // Re-enable button for the *next* advanceSeason click


         // Clear result boxes animations state
        document.querySelectorAll('.result-box').forEach(box => box.classList.remove('show'));
         // Clear trend icons and colors
        document.querySelectorAll('.trend-icon').forEach(icon => icon.innerHTML = '');
        document.querySelectorAll('.financial-value, .percentage-value, .score-value').forEach(span => {
             span.classList.remove('positive', 'negative', 'neutral', 'good', 'average', 'poor', 'excellent');
        });
    }

    function toggleExplanation() {
        explanationDiv.classList.toggle('hidden');
        const isHidden = explanationDiv.classList.contains('hidden');
        toggleExplanationButton.innerHTML = isHidden ? '<i class="icon fas fa-book"></i> הצג הסבר על ניהול מוסדות אופרה' : '<i class="icon fas fa-book-open"></i> הסתר הסבר';
    }


    // --- Event Listeners ---
    advanceSeasonButton.addEventListener('click', advanceSeason);
    nextSeasonButton.addEventListener('click', goToNextSeason);
    restartGameButton.addEventListener('click', initializeGame);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Add listeners for sliders to update values
    repertoireMixSlider.addEventListener('input', () => updateSliderValueDisplay(repertoireMixSlider, repertoireMixValue));
    castingLevelSlider.addEventListener('input', () => updateSliderValueDisplay(castingLevelSlider, castingLevelValue));
    ticketPriceSlider.addEventListener('input', () => updateSliderValueDisplay(ticketPriceSlider, ticketPriceValue));
    marketingBudgetSlider.addEventListener('input', () => updateSliderValueDisplay(marketingBudgetSlider, marketingBudgetValue));
    fundraisingEffortSlider.addEventListener('input', () => updateSliderValueDisplay(fundraisingEffortSlider, fundraisingEffortValue));


    // --- Initial Setup ---
    initializeGame();
    toggleExplanation(); // Hide explanation initially

    // Initial slider value display
    updateSliderValueDisplay(repertoireMixSlider, repertoireMixValue);
    updateSliderValueDisplay(castingLevelSlider, castingLevelValue);
    updateSliderValueDisplay(ticketPriceSlider, ticketPriceValue);
    updateSliderValueDisplay(marketingBudgetSlider, marketingBudgetValue);
    updateSliderValueDisplay(fundraisingEffortSlider, fundraisingEffortValue);


</script>