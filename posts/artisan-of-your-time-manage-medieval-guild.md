---
title: "אמן בזמנך: נהל גילדת ימי הביניים"
english_slug: artisan-of-your-time-manage-medieval-guild
category: "היסטוריה כלכלית"
tags:
  - ימי הביניים
  - גילדות
  - כלכלה
  - ניהול
  - היסטוריה חברתית
---
# אמן בזמנך: נהל גילדת ימי הביניים
היכנס לעולם הסדנאות התוסס של ימי הביניים! מה נדרש כדי לפרוח כאומן מוביל בתקופה ללא פטנטים או שיווק דיגיטלי? צלול לתוך המבנה המורכב של גילדות האומנים – עולם ששילב מסורת עתיקה, הכשרה קפדנית, ותחרות עסקית עקובה מזיע. האם תצליח לבנות אימפריית מלאכה שתפאר את שמך ברחבי הממלכה?

<div id="guild-simulation-container">
    <div id="guild-simulation">
        <h2>סדנת האומן: ניהול חודשי (חודש <span id="current-month">1</span> מתוך 24)</h2>

        <div id="guild-stats">
            <div class="stat-card money">
                <span class="stat-label">אוצר הגילדה:</span>
                <span id="guild-money" class="stat-value">500</span> מטבעות זהב
            </div>
            <div class="stat-card reputation">
                <span class="stat-label">יוקרת הגילדה:</span>
                <span id="guild-reputation" class="stat-value">50</span>
            </div>
        </div>

        <div id="guild-controls">
            <div class="control-group">
                <label for="num-apprentices" title="כמה שוליות יתגוררו בסדנה החודש?">שוליות חרוצות (1-5):</label>
                <input type="number" id="num-apprentices" value="2" min="1" max="5">
            </div>
            <div class="control-group">
                <label for="time-per-apprentice" title="כמה זמן ביום תקדיש להכשרת השוליות? (משפיע על מיומנותן העתידית)">זמן הדרכה (שעות/יום):</label>
                <input type="number" id="time-per-apprentice" value="3" min="1" max="5">
            </div>
            <div class="control-group">
                <label for="material-quality" title="בחירת חומרי גלם - משפיע על איכות המוצר ועלויתו.">איכות חומרי גלם:</label>
                <select id="material-quality">
                    <option value="low">צנועה (זול, איכות נמוכה)</option>
                    <option value="medium" selected>רגילה (בינוני)</option>
                    <option value="high">מעולה (יקר, איכות גבוהה)</option>
                </select>
            </div>
             <div class="control-group">
                <label for="product-price" title="המחיר שתדרוש עבור כל יחידת מוצר.">מחיר למוצר (מטבעות):</label>
                <input type="number" id="product-price" value="30" min="10" max="50">
            </div>
             <div class="control-group">
                <label for="marketing-investment" title="השקעה ביחסי ציבור, קשרים בשוק ופניות ללקוחות פוטנציאליים.">השקעה בשיווק/קשרים (מטבעות):</label>
                <input type="number" id="marketing-investment" value="20" min="0" max="100">
            </div>
        </div>
         <div class="progress-group">
            <span class="progress-label">מיומנות שוליות (ממוצע):</span>
            <div class="progress-bar">
                <div id="apprentice-skill-progress" class="progress-fill">
                    <span id="apprentice-skill-text">20%</span>
                </div>
            </div>
        </div>

        <button id="next-month-btn">סוף חודש: ראה תוצאות!</button>

        <div id="monthly-summary">
             <h3>סיכום חודשי:</h3>
             <p id="event-message" class="summary-item event"></p>
             <p id="sales-summary" class="summary-item"></p>
             <p id="profit-summary" class="summary-item"></p>
             <p id="reputation-summary" class="summary-item"></p>
        </div>

        <div id="monthly-results-section" style="display: none;">
            <h3>דוח פעילות (היסטוריה):</h3>
            <table id="monthly-results">
                <thead>
                    <tr>
                        <th>חודש</th>
                        <th>מכירות</th>
                        <th>הכנסות</th>
                        <th>הוצאות</th>
                        <th>רווח/הפסד</th>
                        <th>יוקרה</th>
                        <th>מיומנות (ממוצע)</th>
                        <th>אירועים</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Results rows will be added here -->
                </tbody>
            </table>
        </div>
         <button id="show-history-btn" style="margin-top: 10px;">הצג/הסתר היסטוריית פעילות</button>
          <div id="game-end-message" class="game-end-message" style="display: none;"></div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג רקע היסטורי: עולם הגילדות</button>

<div id="historical-explanation" style="display: none;">
    <h2>רקע היסטורי: עולם הגילדות בימי הביניים</h2>

    <h3>מבוא: מהן גילדות אומנים ומתי פעלו?</h3>
    דמיינו עולם ללא סופרמרקטים או חנויות ענק, שבו כל מוצר - מלחם ועד נעל - נוצר בידי אומנים מיומנים. גילדות האומנים היו הלב הפועם של הכלכלה העירונית בימי הביניים (בעיקר מהמאה ה-12 ואילך). הן איחדו בעלי מלאכה מאותו תחום מקצועי בעיר מסוימת, כמו אופים, סנדלרים או בנאים, ושימשו כמעין שילוב של איגוד מקצועי, לשכת מסחר, ומערכת סוציאלית. מטרתן העיקרית הייתה להגן על האינטרסים של חברי הגילדה, להבטיח הכשרה איכותית, ולשמור על סטנדרטים גבוהים של ייצור.

    <h3>מבנה הגילדה: המסע מ"שוליה" ל"אמן"</h3>
    המסלול המקצועי בתוך הגילדה היה היררכי וקפדני, בדומה למסע אבירים או מסדר דתי:
    <ul>
        <li>**שוליה (Apprentice):** ילדים או נערים צעירים (לרוב בני 10-14) שהצטרפו לסדנת אמן והתגוררו בביתו. הם למדו את רזי המקצוע תוך כדי עזרה בעבודות הסדנה והבית. תקופת השוליות הייתה חוזית וארוכה (לרוב 3-12 שנים), והאמן היה אחראי גם לחינוכם ולפרנסתם הבסיסית.</li>
        <li>**עוזר (Journeyman):** לאחר סיום תקופת השוליות, הנער הפך לעוזר מיומן. עוזרים עבדו בשכר עבור אמנים ראשיים. רבים מהם יצאו ל"מסע עוזרים" בין ערים שונות כדי לצבור ניסיון ממגוון סדנאות ושיטות עבודה. שלב זה נמשך עד שהעוזר הרגיש מוכן - ולרוב גם היה מסוגל מבחינה כלכלית - לעבור לשלב הבא.</li>
        <li>**אמן (Master):** הדרגה העליונה והנחשקת. כדי להפוך לאמן, עוזר נדרש להוכיח בקיאות עילאית במקצוע על ידי יצירת "יצירת מופת" (masterpiece) שתאושר על ידי ועדת האמנים בגילדה. בנוסף, נדרש לרוב לשלם דמי חבר גבוהים ולהוכיח יכולת לנהל סדנה עצמאית. רק אמנים יכלו להחזיק סדנה משלהם, להעסיק עוזרים ולקבל שוליות.</li>
    </ul>

    <h3>תפקידי הגילדה הכלכליים: שומרי הסף של המקצוע</h3>
    הגילדות היו בעלות כוח כלכלי אדיר בערים:
    <ul>
        <li>**הכשרה ובקרת איכות:** הן פיקחו על תהליך ההכשרה, קבעו את משך השוליות ואת תוכנה, והבטיחו שהאמנים החדשים אכן מיומנים. הגילדות גם קבעו סטנדרטים מחייבים לאיכות חומרי הגלם והמוצרים הסופיים, ולעיתים אף ערכו בדיקות פתע בסדנאות.</li>
        <li>**הסדרת השוק:** הגילדות קבעו לעיתים קרובות מחירי מינימום למוצרים, הגבילו את כמות הייצור ואת שעות העבודה. מטרתן הייתה למנוע תחרות פרועה, להבטיח פרנסה סבירה לכל החברים, ולמנוע הפקעת מחירים או עבודה באיכות ירודה.</li>
        <li>**הגנה על המקצוע:** הגילדות שאפו לשלוט בלעדית על המקצוע בעיר מסוימת. הן הגבילו כניסת אומנים מבחוץ, ונקטו צעדים נגד אומנים "פורעים" (שאינם חברים בגילדה) שניסו לפעול בעיר.</li>
        <li>**תמיכה הדדית:** הגילדות שימשו גם כרשת ביטחון. הן סייעו לחברים שחלו, הזדקנו, או נקלעו למצוקה כלכלית, תמכו באלמנות ויתומים, ולעיתים אף סיפקו שירותי קבורה.</li>
    </ul>

    <h3>מעבר לכלכלה: גילדות כגופים חברתיים ופוליטיים</h3>
    הגילדות לא היו רק עסקיות. הן היוו קהילה חברתית תוססת, עם טקסים, חגיגות, סעודות משותפות, ואף פטרונים קדושים משלהן. רבות מהן בנו בתי גילדה מפוארים ששימשו למפגשים. בערים רבות, הגילדות צברו כוח פוליטי משמעותי, וחבריהן השתתפו ואף שלטו במועצות העיר, תוך הגנה על האינטרסים שלהן.

    <h3>אתגרים ושקיעה: סופה של תקופה</h3>
    כוחן של הגילדות לא נשאר לנצח. הן התמודדו עם אומנים פורעים שפעלו בפריפריה, תחרות בין גילדות שונות, ובעיקר עם שינויים כלכליים וטכנולוגיים רחבים. עליית הסחר הבינלאומי, התפתחות שיטות ייצור מורכבות יותר (כמו התעשייה הביתית ומאוחר יותר מפעלי המנופקטורה), והתחזקות המדינה הריכוזית שרצתה לפקח על הכלכלה - כל אלו ערערו את מעמדן. במאות ה-18 וה-19, ממשלות רבות באירופה ביטלו את הגילדות בחוק, כחלק ממגמה ליברלית של הסרת חסמים לסחר ולייצור.

    <h3>ההד המודרני: שרידי הגילדות בעולם של היום</h3>
    בעוד שגילדות האומנים ההיסטוריות נעלמו, עקרונות מסוימים שרדו. ארגונים מקצועיים מודרניים (כמו לשכות עורכי דין, רואי חשבון, או איגודי מהנדסים) עדיין מסדירים את הכניסה למקצוע, קובעים כללי התנהגות ואתיקה, ומפקחים על סטנדרטים מקצועיים. גם במגזר העסקי, ארגונים כמו "לשכת המסחר" ממשיכים לאגד עסקים מתחומים שונים. אלו אינם גילדות במובן ההיסטורי, אך הם נושאים את המורשת של הגנה על מקצועיות ואינטרסים משותפים.

    <button id="hide-explanation-btn" class="toggle-button">הסתר רקע היסטורי</button>
</div>

<style>
    :root {
        --primary-color: #5a4f45; /* Dark brown */
        --secondary-color: #c8a876; /* Gold/Beige */
        --accent-color: #8b0000; /* Deep Red for events/loss */
        --success-color: #4CAF50; /* Green */
        --background-color: #f4f2e7; /* Light parchment */
        --container-bg: #fffbf0; /* Lighter parchment */
        --border-color: #d4c7b1; /* Light brown border */
        --control-bg: #e0d8c6; /* Slightly darker control area */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--primary-color);
        background-color: var(--background-color);
        padding: 20px;
        margin: 0;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 15px;
    }

    #guild-simulation-container {
        max-width: 900px;
        margin: 20px auto;
        padding: 20px;
        background-color: var(--container-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden; /* Needed for potential animations */
    }

    #guild-stats {
        display: flex;
        justify-content: space-around;
        margin-bottom: 25px;
        font-size: 1.2em;
        flex-wrap: wrap;
        gap: 15px;
    }

    .stat-card {
        background-color: var(--control-bg);
        padding: 15px 20px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        min-width: 200px;
        text-align: center;
    }

    .stat-card .stat-label {
        display: block;
        font-size: 0.9em;
        margin-bottom: 5px;
        font-weight: bold;
        color: var(--primary-color);
    }

    .stat-card .stat-value {
        font-size: 1.8em;
        font-weight: bold;
        color: var(--secondary-color);
         transition: color 0.5s ease; /* Animation for value change */
    }

    .stat-card.money .stat-value { color: var(--success-color); }
     .stat-card.reputation .stat-value { color: #007bff; /* Blue for reputation */ }


    #guild-controls {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin-bottom: 25px;
        padding: 20px;
        background-color: var(--control-bg);
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }

    .control-group {
        display: flex;
        flex-direction: column;
    }

    .control-group label {
        margin-bottom: 8px;
        font-weight: bold;
        font-size: 1em;
        color: var(--primary-color);
    }

    .control-group input[type="number"],
    .control-group select {
        padding: 10px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        background-color: #fff;
        font-size: 1em;
         color: var(--primary-color);
    }

    .progress-group {
        margin-bottom: 25px;
    }

     .progress-label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        font-size: 1em;
        color: var(--primary-color);
     }

    .progress-bar {
        width: 100%;
        height: 25px;
        background-color: #eee;
        border-radius: 5px;
        overflow: hidden;
        border: 1px solid var(--border-color);
    }

    .progress-fill {
        height: 100%;
        width: 0%;
        background-color: var(--secondary-color); /* Gold fill */
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--primary-color);
        font-weight: bold;
        transition: width 0.5s ease-in-out;
        font-size: 0.9em;
    }

     .progress-fill span {
         mix-blend-mode: difference; /* Make text visible regardless of background color */
     }


    #next-month-btn {
        display: block;
        width: calc(100% - 40px); /* Adjust for padding */
        margin: 20px auto 0;
        padding: 12px 25px;
        background-color: var(--secondary-color);
        color: var(--primary-color);
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.2em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    }

     #next-month-btn:hover:not(:disabled) {
        background-color: #d9b98a;
        transform: translateY(-1px);
    }

     #next-month-btn:active:not(:disabled) {
        background-color: #c8a876;
        transform: translateY(1px);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }

     #next-month-btn:disabled {
         background-color: #ccc;
         cursor: not-allowed;
         box-shadow: none;
     }

    #monthly-summary {
        margin-top: 25px;
        padding: 15px;
        background-color: var(--control-bg);
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }

     #monthly-summary h3 {
         margin-top: 0;
         margin-bottom: 10px;
         border-bottom: 1px dashed var(--border-color);
         padding-bottom: 5px;
         text-align: left;
         font-size: 1.1em;
     }

    .summary-item {
        margin-bottom: 8px;
         padding: 5px;
         border-radius: 4px;
    }

     .summary-item.event {
        font-weight: bold;
        color: var(--accent-color);
         background-color: #ffebeb; /* Light red background */
     }

     #monthly-results-section {
         margin-top: 25px;
         padding: 15px;
         background-color: var(--control-bg);
         border-radius: 8px;
         border: 1px solid var(--border-color);
     }

      #monthly-results-section h3 {
         margin-top: 0;
         margin-bottom: 10px;
         border-bottom: 1px dashed var(--border-color);
         padding-bottom: 5px;
         text-align: left;
         font-size: 1.1em;
     }


    #monthly-results {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        font-size: 0.9em;
    }

    #monthly-results th,
    #monthly-results td {
        border: 1px solid var(--border-color);
        padding: 10px;
        text-align: center;
    }

    #monthly-results thead th {
        background-color: var(--secondary-color);
        color: var(--primary-color);
        font-weight: bold;
    }

    #monthly-results tbody tr:nth-child(even) {
        background-color: #f9f8f2; /* Slightly different stripe */
    }

     #monthly-results tbody tr:hover {
         background-color: #e0d8c6; /* Highlight on hover */
     }

     #monthly-results td {
         vertical-align: top;
     }

    .toggle-button {
        display: block;
        margin: 20px auto;
        padding: 12px 25px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    }
     .toggle-button:hover {
        background-color: #0056b3;
     }

    #historical-explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--container-bg);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    #historical-explanation h2 {
        color: var(--primary-color);
        border-bottom: 2px solid var(--secondary-color);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    #historical-explanation h3 {
        color: var(--primary-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
        margin-top: 20px;
        margin-bottom: 10px;
    }
     #historical-explanation ul {
         list-style-type: disc;
         margin-left: 20px;
         padding-left: 0;
     }
     #historical-explanation li {
         margin-bottom: 10px;
         color: var(--primary-color);
     }

     #historical-explanation li strong {
         color: var(--primary-color);
     }

     .game-end-message {
         margin-top: 20px;
         padding: 15px;
         border-radius: 8px;
         font-size: 1.2em;
         text-align: center;
         font-weight: bold;
     }

     .game-end-message.win {
         background-color: #d4edda; /* Light green */
         color: #155724; /* Dark green */
         border: 1px solid #c3e6cb;
     }

     .game-end-message.lose {
         background-color: #f8d7da; /* Light red */
         color: #721c24; /* Dark red */
         border: 1px solid #f5c6cb;
     }


    /* Animation for stat change */
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
    }

    .pulsate-money .stat-value {
        animation: pulse 0.5s ease;
        color: var(--success-color) !important; /* Ensure color changes */
    }
     .pulsate-reputation .stat-value {
        animation: pulse 0.5s ease;
        color: #007bff !important; /* Ensure color changes */
     }

    /* Animation for new table row */
     @keyframes fadeIn {
         from { opacity: 0.5; transform: translateY(10px); }
         to { opacity: 1; transform: translateY(0); }
     }

     #monthly-results tbody tr {
         animation: fadeIn 0.4s ease-out;
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Game State
        let currentMonth = 1;
        const totalMonths = 24;
        let guildMoney = 500;
        let guildReputation = 50; // 0-100
        let avgApprenticeSkill = 20; // 0-100
        const apprenticeStipend = 10; // cost per apprentice per month

        // DOM Elements
        const currentMonthSpan = document.getElementById('current-month');
        const guildMoneySpan = document.getElementById('guild-money');
        const guildReputationSpan = document.getElementById('guild-reputation');
        const numApprenticesInput = document.getElementById('num-apprentices');
        const timePerApprenticeInput = document.getElementById('time-per-apprentice');
        const materialQualitySelect = document.getElementById('material-quality');
        const productPriceInput = document.getElementById('product-price');
        const marketingInvestmentInput = document.getElementById('marketing-investment');
        const apprenticeSkillProgress = document.getElementById('apprentice-skill-progress');
        const apprenticeSkillText = document.getElementById('apprentice-skill-text');
        const nextMonthBtn = document.getElementById('next-month-btn');
        const monthlySummaryDiv = document.getElementById('monthly-summary');
        const eventMessageP = document.getElementById('event-message');
        const salesSummaryP = document.getElementById('sales-summary');
        const profitSummaryP = document.getElementById('profit-summary');
        const reputationSummaryP = document.getElementById('reputation-summary');
        const monthlyResultsSection = document.getElementById('monthly-results-section');
        const monthlyResultsBody = document.querySelector('#monthly-results tbody');
        const showHistoryBtn = document.getElementById('show-history-btn');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const historicalExplanationDiv = document.getElementById('historical-explanation');
        const hideExplanationBtn = document.getElementById('hide-explanation-btn');
        const gameEndMessageDiv = document.getElementById('game-end-message');
        const guildMoneyCard = guildMoneySpan.closest('.stat-card');
        const guildReputationCard = guildReputationSpan.closest('.stat-card');


        // --- Helper Functions ---

        // Update stat display with animation
        const updateStatDisplay = (element, value, isMoney = false) => {
            element.textContent = value;
            const card = element.closest('.stat-card');
            if (card) {
                card.classList.remove('pulsate-money', 'pulsate-reputation'); // Remove previous
                // Trigger reflow
                void card.offsetWidth;
                card.classList.add(isMoney ? 'pulsate-money' : 'pulsate-reputation');
            }
        };

        // Update progress bar
        const updateProgressBar = (element, textElement, value) => {
            const percentage = Math.max(0, Math.min(100, value));
            element.style.width = percentage + '%';
            textElement.textContent = Math.round(percentage) + '% מיומנות';
             // Adjust text color if needed based on background (optional, mix-blend-mode helps)
             // if (percentage < 50) { textElement.style.color = 'var(--primary-color)'; }
             // else { textElement.style.color = 'white'; }
        };


        // --- Game Logic ---

        const runMonth = () => {
            if (currentMonth > totalMonths || guildMoney < -200) {
                 displayGameEndMessage();
                 return;
             }

            // Reset summary messages
            eventMessageP.textContent = '';
            salesSummaryP.textContent = '';
            profitSummaryP.textContent = '';
            reputationSummaryP.textContent = '';
            monthlySummaryDiv.style.display = 'block'; // Ensure summary is visible

            // Read Inputs
            const numApprentices = parseInt(numApprenticesInput.value) || 0; // Default to 0 if invalid
            const timePerApprentice = parseInt(timePerApprenticeInput.value) || 1; // Default to 1
            const materialQuality = materialQualitySelect.value;
            const productPrice = parseInt(productPriceInput.value) || 10; // Default to 10
            const marketingInvestment = parseInt(marketingInvestmentInput.value) || 0; // Default to 0

            // Calculations
            // Skill Gain (higher time, more gain, diminishing returns)
            const baseSkillGain = (timePerApprentice / 5) * 6; // Up to 6 base points
            const diminishingReturnFactor = (100 - avgApprenticeSkill) / 100; // Gain slows down as skill increases
            const skillGain = baseSkillGain * diminishingReturnFactor;
            avgApprenticeSkill = Math.min(100, avgApprenticeSkill + skillGain);
            avgApprenticeSkill = parseFloat(avgApprenticeSkill.toFixed(1));

            // Material Cost & Quality Multiplier
            let materialCostPerUnit = 0;
            let qualityMultiplier = 1.0;
            switch (materialQuality) {
                case 'low':
                    materialCostPerUnit = 8;
                    qualityMultiplier = 0.7; // Lower quality impact
                    break;
                case 'medium':
                    materialCostPerUnit = 12;
                    qualityMultiplier = 1.0;
                    break;
                case 'high':
                    materialCostPerUnit = 20;
                    qualityMultiplier = 1.3; // Higher quality impact
                    break;
            }

            // Product Quality (influenced by skill and materials)
            const productQuality = (avgApprenticeSkill / 100) * qualityMultiplier * 100; // Scale to 0-100

            // Sales (influenced by quality, price, reputation, marketing, randomness)
            const baseDemand = 40 + (numApprentices * 5); // More apprentices = higher potential output/demand
            const qualityInfluence = (productQuality / 100 - 0.5) * 0.6 + 1; // Range ~0.7 to 1.3
            const priceInfluence = 1.5 - (productPrice / 50); // Higher price = lower influence (assuming max reasonable price around 50-60). Range ~0.5 to 1.4
            const reputationInfluence = (guildReputation / 100 - 0.3) * 0.8 + 1; // Range ~0.7 to 1.5 (Reputation has stronger influence)
            const marketingInfluence = 1 + (marketingInvestment / 150); // More marketing = more influence, slightly stronger impact
            const randomInfluence = 0.9 + Math.random() * 0.2; // +/- 10% variability

            let sales = Math.max(0, Math.round(baseDemand * qualityInfluence * priceInfluence * reputationInfluence * marketingInfluence * randomInfluence));

            // Clamp sales to a realistic maximum based on apprentices
            const maxSalesPerApprentice = 30; // An apprentice can realistically make up to X items
            sales = Math.min(sales, numApprentices * maxSalesPerApprentice + 10); // +10 for the master's work


            // Random Event
            let eventMessage = "";
            let eventImpact = {}; // Store changes from event
            const eventChance = 0.25; // 25% chance each month
            if (Math.random() < eventChance) {
                const eventType = Math.floor(Math.random() * 5); // 0: Market Boom, 1: Raw Material Shortage, 2: Increased Competition, 3: Royal Commission, 4: Apprentice Sickness
                switch (eventType) {
                    case 0:
                        eventMessage = "🎉 יריד ססגוני בעיר! הביקוש למוצרי איכות מזנק החודש!";
                        eventImpact.salesMultiplier = 1.6; // 60% sales boost
                        eventImpact.reputationChange = 5; // Small reputation boost from visibility
                        break;
                    case 1:
                        eventMessage = "🪵 מחסור בחומרי גלם! עלויות הייצור עולות, והאיכות עלולה להיפגע.";
                        eventImpact.materialCostMultiplier = 1.8; // 80% cost increase
                        eventImpact.qualityMultiplier = 0.8; // 20% quality reduction
                        eventImpact.reputationChange = -3; // Small reputation hit due to lower quality
                        break;
                    case 2:
                        eventMessage = "⚔️ גילדה מתחרה פתחה סדנה ליד! התחרות קשה יותר והמכירות יורדות.";
                        eventImpact.salesMultiplier = 0.6; // 40% sales drop
                        eventImpact.reputationChange = -5; // Reputation hit from perceived weakness
                        break;
                    case 3:
                        eventMessage = "👑 הזמנה מלכותית מיוחדת! הזדמנות פז למכירות ומוניטין.";
                        eventImpact.salesMultiplier = 1.4; // 40% sales boost
                        eventImpact.reputationChange = 12; // Significant reputation boost
                        break;
                    case 4:
                         eventMessage = "🤒 מספר שוליות חלו החודש. היצור מתעכב!";
                         eventImpact.salesMultiplier = 0.8; // 20% sales drop due to reduced labor
                         eventImpact.skillGainMultiplier = 0.5; // Skill gain is slower this month
                         break;
                }
            }

            // Apply event impacts
            if(eventImpact.salesMultiplier) sales = Math.round(sales * eventImpact.salesMultiplier);
            if(eventImpact.materialCostMultiplier) materialCostPerUnit = Math.round(materialCostPerUnit * eventImpact.materialCostMultiplier);
            if(eventImpact.qualityMultiplier) qualityMultiplier *= eventImpact.qualityMultiplier;
            if(eventImpact.reputationChange) guildReputation = Math.min(100, Math.max(0, guildReputation + eventImpact.reputationChange));
             if(eventImpact.skillGainMultiplier) avgApprenticeSkill = Math.min(100, avgApprenticeSkill - skillGain + (skillGain * eventImpact.skillGainMultiplier)); // Recalculate skill based on adjusted gain


            // Revenue and Expenses
            const revenue = sales * productPrice;
            const materialExpense = sales * materialCostPerUnit;
            const apprenticeExpense = numApprentices * apprenticeStipend;
            const totalExpenses = materialExpense + apprenticeExpense + marketingInvestment;

            // Profit
            const profit = revenue - totalExpenses;
            guildMoney += profit;

            // Reputation Update (based on quality, marketing, adjusted by profit/loss and events)
             let reputationChangeBasedOnPerformance = 0;
             reputationChangeBasedOnPerformance += (productQuality - 50) / 8; // Quality impact
             reputationChangeBasedOnPerformance += marketingInvestment / 15; // Marketing impact
             if (profit < -50) {
                 reputationChangeBasedOnPerformance -= 8; // Significant loss hurts a lot
             } else if (profit < 0) {
                 reputationChangeBasedOnPerformance -= 3; // Small loss hurts
             } else if (profit > 150) {
                 reputationChangeBasedOnPerformance += 8; // Big profit helps a lot
             } else if (profit > 50) {
                  reputationChangeBasedOnPerformance += 3; // Small profit helps
             }

             guildReputation = Math.min(100, Math.max(0, Math.round(guildReputation + reputationChangeBasedOnPerformance)));


            // --- Display Results ---

            // Update Summary Display
             salesSummaryP.textContent = `מכירות: ${sales} יחידות`;
             profitSummaryP.textContent = profit >= 0 ? `רווח: ${profit} מטבעות זהב 🎉` : `הפסד: ${Math.abs(profit)} מטבעות זהב 😔`;
             reputationSummaryP.textContent = `יוקרה (סוף חודש): ${guildReputation}`;
             if(eventMessage) eventMessageP.textContent = eventMessage;


            // Add row to detailed history table
            const newRow = monthlyResultsBody.insertRow(0); // Insert at the top
            newRow.innerHTML = `
                <td>${currentMonth}</td>
                <td>${sales}</td>
                <td>${revenue}</td>
                <td>${totalExpenses}</td>
                <td style="color: ${profit >= 0 ? 'var(--success-color)' : 'var(--accent-color)'}; font-weight: bold;">${profit}</td>
                <td>${guildReputation}</td>
                <td>${avgApprenticeSkill.toFixed(1)}%</td>
                <td>${eventMessage || '-'}</td>
            `;

            // Update State Displays
            updateStatDisplay(guildMoneySpan, guildMoney, true);
            updateStatDisplay(guildReputationSpan, guildReputation, false);
            updateProgressBar(apprenticeSkillProgress, apprenticeSkillText, avgApprenticeSkill);

            currentMonth++;
            currentMonthSpan.textContent = currentMonth;


            // Check for game end conditions
            if (currentMonth > totalMonths || guildMoney < -200) {
                 nextMonthBtn.disabled = true;
                 nextMonthBtn.textContent = "הסימולציה הסתיימה";
                 displayGameEndMessage();
            }
        };

         const displayGameEndMessage = () => {
             gameEndMessageDiv.style.display = 'block';
             let message = "";
             let className = "";
             if (guildMoney < -200) {
                 message = "הגילדה פשטה רגל! לא הצלחת לנהל את האוצר. נסו שוב?";
                 className = "lose";
             } else {
                 // Calculate a final score based on Money, Reputation, Skill
                 const finalScore = Math.max(0, guildMoney) + (guildReputation * 10) + (avgApprenticeSkill * 5);
                 message = `הגעת לסוף הסימולציה (24 חודשים)! 🎉<br>אוצר סופי: ${guildMoney} מטבעות, יוקרה: ${guildReputation}, מיומנות שוליות: ${avgApprenticeSkill.toFixed(1)}%.<br>הציון הכולל שלך: ${Math.round(finalScore)}. האם תהפוך לאגדה?`;
                 className = "win";
             }
             gameEndMessageDiv.innerHTML = message;
             gameEndMessageDiv.className = `game-end-message ${className}`;
              monthlySummaryDiv.style.display = 'none'; // Hide monthly summary at the end
             showHistoryBtn.textContent = 'הצג היסטוריה מלאה'; // Change button text

         };


        // --- Event Listeners ---
        nextMonthBtn.addEventListener('click', runMonth);

        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = historicalExplanationDiv.style.display === 'none';
            historicalExplanationDiv.style.display = isHidden ? 'block' : 'none';
             toggleExplanationBtn.style.display = 'none'; // Hide this button
             if(isHidden) {
                 hideExplanationBtn.style.display = 'block'; // Show hide button
             }
        });

         hideExplanationBtn.addEventListener('click', () => {
             historicalExplanationDiv.style.display = 'none';
             hideExplanationBtn.style.display = 'none'; // Hide this button
             toggleExplanationBtn.style.display = 'block'; // Show toggle button again
         });


        showHistoryBtn.addEventListener('click', () => {
            const isHidden = monthlyResultsSection.style.display === 'none';
            monthlyResultsSection.style.display = isHidden ? 'block' : 'none';
            showHistoryBtn.textContent = isHidden ? 'הסתר היסטוריית פעילות' : 'הצג/הסתר היסטוריית פעילות'; // Keep text dynamic
        });


        // --- Initial Setup ---
        updateProgressBar(apprenticeSkillProgress, apprenticeSkillText, avgApprenticeSkill);
        updateStatDisplay(guildMoneySpan, guildMoney, true);
        updateStatDisplay(guildReputationSpan, guildReputation, false);
         hideExplanationBtn.style.display = 'none'; // Initially hide hide button
         monthlySummaryDiv.style.display = 'none'; // Initially hide summary

    });
</script>
---
```