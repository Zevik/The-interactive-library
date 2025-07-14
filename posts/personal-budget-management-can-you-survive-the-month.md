---
title: "ניהול תקציב אישי: האם תצליח לשרוד את החודש?"
english_slug: personal-budget-management-can-you-survive-the-month
category: "מדעי החברה / כלכלה התנהגותית"
tags: [תקציב אישי, כלכלת המשפחה, התנהגות פיננסית, חיסכון, הוצאות והכנסות]
---
# ניהול תקציב אישי: האם תצליח לשרוד את החודש?

כמה פעמים מצאתם את עצמכם בסוף החודש עם יתרה נמוכה או מינוס מפתיע, למרות שהמשכורת נכנסה והיה נדמה שהכל בשליטה? ניהול תקציב אישי הוא אתגר יומיומי, במיוחד כשהחיים זורקים עלינו הוצאות בלתי צפויות והזדמנויות ספונטניות. האם תצליח לנווט בחודש עמוס אירועים ולקבל את ההחלטות הנכונות כדי לשמור על ראש מעל המים? בואו נראה!

<div id="budget-simulator">
    <h2>סימולטור: חודש במבחן התקציב</h2>
    <div class="controls game-section">
        <p>בחר רמת קושי, קבל משכורת התחלתית, והתחל את הסימולציה!</p>
        <label for="difficulty">רמת קושי:</label>
        <select id="difficulty">
            <option value="easy">קל (תקציב רחב, פחות הפתעות)</option>
            <option value="hard">קשה (תקציב מוגבל, יותר אתגרים)</option>
        </select>
        <button id="start-game">צא לדרך!</button>
    </div>

    <div id="game-area" class="hidden game-section">
        <div class="stats">
            <div class="stat-item">
                <span class="stat-icon">📅</span>
                <span class="stat-label">יום בחודש:</span>
                <span id="current-day">0</span> מתוך 30
            </div>
             <div class="stat-item">
                <span class="stat-icon">💰</span>
                <span class="stat-label">יתרה בחשבון:</span>
                <span id="current-balance" class="balance-display">0.00</span> ש"ח
            </div>
            <div class="stat-item hidden"> <!-- Hide income display in stats for cleaner look -->
                <span class="stat-icon">💳</span>
                <span class="stat-label">הכנסה חודשית:</span>
                <span id="monthly-income">0.00</span> ש"ח
            </div>
        </div>

        <div id="events" class="game-section">
            <h3>יומן אירועים והחלטות</h3>
            <div id="event-log">
                 <div class="event-message default">המשחק מתחיל...</div>
            </div>
             <div id="decision-area" class="hidden">
                <p id="decision-text"></p>
                <button class="decision-button primary" data-choice="yes">כן, שווה את זה!</button>
                <button class="decision-button secondary" data-choice="no">לא הפעם, חוסכים!</button>
            </div>
        </div>

        <div class="actions game-section">
            <p>מה עושים עכשיו?</p>
            <button id="next-day" disabled>🗓️ התקדם יום אחד</button>
            <button id="next-week" disabled>📅 קפוץ שבוע קדימה</button>
        </div>

        <div id="game-result" class="hidden game-section">
            <h3>סוף הסימולציה</h3>
            <p id="result-message"></p>
            <button id="restart-game" class="primary">שחק שוב</button>
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

    #budget-simulator {
        direction: rtl;
        font-family: 'Rubik', sans-serif;
        max-width: 700px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background-color: #f8f8f8;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #333;
    }

    #budget-simulator h2, #budget-simulator h3 {
        text-align: center;
        color: #1a4d2e; /* Dark green */
        margin-bottom: 15px;
    }

    #budget-simulator h2 {
        font-size: 1.8em;
        margin-top: 0;
    }

    #budget-simulator h3 {
         font-size: 1.4em;
         margin-top: 25px;
         border-bottom: 1px solid #eee;
         padding-bottom: 5px;
         color: #555;
    }

    .game-section {
        margin-bottom: 25px;
        padding: 15px;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .controls p, .actions p {
        text-align: center;
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.1em;
        color: #555;
    }

    .controls label {
        margin-left: 10px;
        font-weight: bold;
    }

    .controls select {
        padding: 8px;
        border-radius: 4px;
        border: 1px solid #ccc;
        font-size: 1em;
    }

    button {
        padding: 10px 20px;
        margin: 5px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    button.primary {
        background-color: #4CAF50; /* Green */
        color: white;
    }

     button.primary:hover:not(:disabled) {
        background-color: #45a049;
        transform: translateY(-1px);
    }

     button.secondary {
        background-color: #007bff; /* Blue */
        color: white;
    }

    button.secondary:hover:not(:disabled) {
        background-color: #0056b3;
         transform: translateY(-1px);
    }

    button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        transform: none;
    }

     #start-game, #restart-game {
         display: block;
         width: fit-content;
         margin: 15px auto 0;
         padding: 12px 25px;
         font-size: 1.2em;
     }

    .stats {
        display: flex;
        justify-content: space-around;
        margin-bottom: 20px;
        padding: 15px;
        background-color: #e9f7ef; /* Light green */
        border-radius: 8px;
        border: 1px solid #d4edda;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .stat-item {
        text-align: center;
        margin: 5px 10px;
    }

    .stat-icon {
        font-size: 1.5em;
        margin-right: 5px;
        vertical-align: middle;
    }

    .stat-label {
        font-weight: bold;
        font-size: 1em;
        vertical-align: middle;
    }

    .balance-display {
        font-weight: bold;
        font-size: 1.4em;
        transition: color 0.5s ease; /* Smooth color transition */
    }

     #current-balance.positive { color: #28a745; /* Green */ }
     #current-balance.negative { color: #dc3545; /* Red */ }


    #event-log {
        max-height: 250px;
        overflow-y: auto;
        margin-bottom: 15px;
        padding-right: 10px; /* Space for scrollbar */
    }

    .event-message {
        padding: 10px;
        margin-bottom: 8px;
        border-radius: 6px;
        font-size: 0.95em;
        line-height: 1.5;
        border: 1px solid #eee;
        background-color: #f9f9f9;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly below */
        animation: fadeInSlideUp 0.5s ease forwards; /* Animation */
    }

    @keyframes fadeInSlideUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .event-message.default { background-color: #e9e9e9; color: #333; }
    .event-message.positive { background-color: #d4edda; color: #155724; border-color: #c3e6cb; }
    .event-message.negative { background-color: #f8d7da; color: #721c24; border-color: #f5c6cb; }
    .event-message.decision { background-color: #cfe2ff; color: #084298; border-color: #b9d0f2; font-weight: bold; }


    #decision-area {
        margin-top: 20px;
        padding: 15px;
        border-top: 1px solid #ccc;
        background-color: #fff3cd; /* Light yellow */
        border-radius: 0 0 8px 8px; /* Match parent section border */
        text-align: center;
    }

    #decision-area p {
        margin-bottom: 15px;
        font-weight: bold;
        font-size: 1.1em;
        color: #664d03; /* Dark yellow */
    }

    .decision-button {
        margin: 0 10px;
        padding: 10px 20px;
    }

    .actions {
        text-align: center;
    }

    .actions button {
         min-width: 150px;
    }


    #game-result {
        margin-top: 25px;
        padding: 25px;
        border: 2px solid;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #game-result.win {
        border-color: #28a745; /* Green */
        background-color: #d4edda;
        color: #155724;
    }

    #game-result.lose {
        border-color: #dc3545; /* Red */
        background-color: #f8d7da;
        color: #721c24;
    }

    #game-result h3 {
        margin-top: 0;
        color: inherit; /* Use parent color */
        font-size: 1.6em;
    }

    #result-message {
        font-size: 1.2em;
        margin-bottom: 20px;
        line-height: 1.6;
    }


    .hidden {
        display: none;
    }

    #toggle-explanation {
        display: block;
        margin: 30px auto 20px;
        padding: 12px 25px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        background-color: #6c757d; /* Grey */
        color: white;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #toggle-explanation:hover {
        background-color: #5a6268;
        transform: translateY(-1px);
    }

    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background-color: #fff;
        direction: rtl;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Rubik', sans-serif;
        color: #333;
    }

    #explanation h2 {
         text-align: center;
         color: #1a4d2e;
         margin-bottom: 20px;
         font-size: 1.8em;
    }

    #explanation h3 {
        color: #555;
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.4em;
        border-bottom: 1px solid #eee;
        padding-bottom: 3px;
    }

    #explanation p, #explanation ul {
        line-height: 1.7;
        margin-bottom: 18px;
        font-size: 1em;
    }

    #explanation ul {
        padding-right: 25px;
    }

    #explanation li {
        margin-bottom: 10px;
        line-height: 1.5;
    }
</style>

<button id="toggle-explanation">עקרונות לניהול תקציב יעיל</button>

<div id="explanation" class="hidden">
    <h2>ניהול תקציב אישי: עקרונות וטיפים</h2>

    <h3>מהו תקציב אישי ולמה הוא קריטי?</h3>
    <p>תקציב אישי הוא למעשה מפת דרכים פיננסית. הוא מסייע לך לעקוב אחר כל שקל שנכנס ויוצא, להבין לאן הכסף שלך באמת הולך, לקבל החלטות מושכלות ולהימנע ממלכודות פיננסיות כמו מינוס גבוה או חובות מיותרים. זהו הבסיס האיתן לבניית עתיד פיננסי יציב ובטוח, ומאפשר לך להגדיר ולהשיג יעדים כספיים, קטנים כגדולים.</p>

    <h3>הוצאות: קבועות מול משתנות (והפתעות!)</h3>
    <ul>
        <li>**הוצאות קבועות:** אלו "העוגנים" של התקציב – סכומים ידועים יחסית שחוזרים על עצמם (שכר דירה/משכנתא, ביטוחים, החזרי הלוואה, מנויים קבועים). קל לתכנן אותן מראש.</li>
        <li>**הוצאות משתנות:** אלו הסכומים ש"רוקדים" מחודש לחודש (קניות בסופר, חשבונות חשמל ומים לפי צריכה, דלק, בילויים, קניות פנאי). כאן נדרש מעקב צמוד יותר וגמישות.</li>
        <li>**הוצאות בלתי צפויות:** אלו "קלפי ההפתעה" – תיקון דחוף לרכב, הוצאה רפואית לא מתוכננת, קנס. הסימולטור מדמה אירועים כאלה כדי ללמד איך להתמודד איתם בזמן אמת.</li>
    </ul>

    <h3>"כרית ביטחון" - חומת ההגנה שלך</h3>
    <p>דמיין סכום כסף שיושב בצד, מוכן לשמש כגלגל הצלה ברגע האמת – זו 'כרית הביטחון' הפיננסית שלך (נקראת גם 'קרן חירום'). מטרתה העיקרית היא לכסות הוצאות בלתי צפויות גדולות או לספק רשת ביטחון במקרה של אובדן הכנסה (כמו פיטורים). המטרה היא לבנות כרית שתספיק ל-3-6 חודשי הוצאות מחיה בסיסיות. היא מקנה שקט נפשי ומאפשרת להימנע מפתרונות יקרים כמו הלוואות או אוברדרפט בעת משבר.</p>

    <h3>האמנות של קבלת החלטות פיננסיות</h3>
    <p>ניהול תקציב הוא לא רק מעקב יבש אחרי מספרים, אלא גם תהליך מתמיד של קבלת החלטות. האם ההוצאה הזו באמת נחוצה עכשיו? האם אני יכול לדחות את הקנייה הזו? האם עדיף לוותר על משהו אחד היום כדי לחסוך למשהו חשוב יותר מחר? הסימולטור מציב אותך בפני דילמות יומיומיות שמדגימות כיצד החלטות קטנות מצטברות ומשפיעות על היתרה הסופית שלך בסוף החודש.</p>

    <h3>טיפים מעשיים לשרוד (ולשגשג) פיננסית:</h3>
    <ul>
        <li>**דע את המספרים שלך:** עקוב אחר ההכנסות וההוצאות שלך באופן קבוע. אפליקציות בנק, גיליונות אלקטרוניים או יישומים ייעודיים יכולים להפוך זאת לקל ונגיש.</li>
        <li>**בנה את כרית הביטחון:** התחל גם מסכומים קטנים וצבור בהתמדה. זו ההשקעה החשובה ביותר שלך בשקט הנפשי.</li>
        <li>**היה גמיש ומוכן להתאמות:** החיים דינמיים, והתקציב שלך צריך להיות גם כן. אם צצה הוצאה גדולה, בדוק איפה אפשר לקצץ בהוצאות פחות חיוניות.</li>
        <li>**תעדוף בקפידה:** למד להבדיל בין רצונות לצרכים. במצבים פיננסיים מאתגרים, צרכים בסיסיים באים תמיד קודם.</li>
        <li>**הימנע מחוב מיותר ויקר:** השתדל להימנע משימוש כרוני באוברדרפט או הלוואות לטווח קצר עם ריבית גבוהה.</li>
    </ul>

    <h3>מעקב, גמישות והתמדה</h3>
    <p>ניהול תקציב הוא מסע, לא יעד חד פעמי. הוא דורש מעקב שוטף, נכונות להתאים את התוכנית כשצריך, והתמדה. הסימולטור נותן טעימה מהדינמיקה הזו ומאפשר לפתח את שריר קבלת ההחלטות הפיננסיות בסביבה מבוקרת וללא סיכון אמיתי. בהצלחה!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // --- DOM Elements ---
        const difficultySelect = document.getElementById('difficulty');
        const startGameButton = document.getElementById('start-game');
        const gameArea = document.getElementById('game-area');
        const currentDaySpan = document.getElementById('current-day');
        const currentBalanceSpan = document.getElementById('current-balance');
        const monthlyIncomeSpan = document.getElementById('monthly-income');
        const eventLogDiv = document.getElementById('event-log');
        const decisionArea = document.getElementById('decision-area');
        const decisionText = document.getElementById('decision-text');
        const decisionButtons = document.querySelectorAll('.decision-button');
        const nextDayButton = document.getElementById('next-day');
        const nextWeekButton = document.getElementById('next-week');
        const gameResultDiv = document.getElementById('game-result');
        const resultMessageP = document.getElementById('result-message');
        const restartGameButton = document.getElementById('restart-game');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const controlsDiv = document.querySelector('.controls'); // Select the controls div


        // --- Game State ---
        let currentDay = 0;
        let currentBalance = 0;
        let monthlyIncome = 0;
        let gameRunning = false;
        let currentDecision = null; // { text: '...', yesCost: X, noOutcome: '...' }
        let currentSettings = null; // Store settings for current difficulty

        // --- Difficulty Settings ---
        const difficultySettings = {
            easy: {
                startBalance: 7000, // Higher starting buffer
                monthlyIncome: 9000,
                eventProbability: 0.3, // Less frequent random events
                negativeEventWeight: 0.5, // Equal chance positive/negative random
                eventMagnitude: { min: 50, max: 400 }, // Smaller random events
                flexibleExpenseProbability: 0.15, // More frequent flexible choices
                flexibleExpenseMagnitude: { min: 80, max: 300 }, // Cheaper flexible choices
                unavoidableExpenseDays: [] // No large fixed expenses
            },
            hard: {
                startBalance: 3000, // Lower starting buffer
                monthlyIncome: 10000,
                eventProbability: 0.5, // More frequent random events
                negativeEventWeight: 0.7, // Higher chance of negative random event
                eventMagnitude: { min: 100, max: 800 }, // Larger random events
                flexibleExpenseProbability: 0.08, // Less frequent flexible choices
                flexibleExpenseMagnitude: { min: 200, max: 700 }, // More expensive flexible choices
                unavoidableExpenseDays: [8, 15, 22] // Examples: Rent (part), utilities, large bill
            }
        };

        // --- Event Definitions ---
        // Event types: 'positive', 'negative', 'flexible', 'unavoidable'
        const events = {
             positive: [
                { text: "מצאת ₪{value} במכנס ישן! יום מזל פיננסי.", value: (settings) => Math.random() * 100 + 50 },
                { text: "החזר מס קטן או זיכוי חשבון נכנס. פלוס מפתיע של ₪{value}!", value: (settings) => Math.random() * 150 + 100 },
                { text: "שכן החזיר חוב קטן. ₪{value} חזרו לחשבון.", value: (settings) => Math.random() * 80 + 20 },
                 { text: "הנחה קטנה או קופון חיסכון בקנייה שוטפת. חסכת ₪{value}.", value: (settings) => Math.random() * 70 + 30 }
            ],
            negative: [
                { text: "קנס חניה מעצבן של ₪{value}! הוצאה בלתי צפויה.", value: (settings) => -(Math.random() * 150 + 100) },
                { text: "פנצ'ר ברכב. תיקון קטן הכרחי עלה ₪{value}.", value: (settings) => -(Math.random() * 300 + 150) },
                { text: "מתנה ליום הולדת של חבר קרוב. עלתה ₪{value}.", value: (settings) => -(Math.random() * 200 + 80) },
                { text: "קלקול קטן בבית שדרש איש מקצוע. עלה ₪{value}.", value: (settings) => -(Math.random() * 250 + 100) },
                 { text: "עמלת בנק גבוהה מהצפוי. ₪{value} ירדו מהחשבון.", value: (settings) => -(Math.random() * 50 + 20) },
                 { text: "הוצאה רפואית קטנה או תרופות. ₪{value} ירדו.", value: (settings) => -(Math.random() * 100 + 50) }
            ],
            flexible: [
                {
                    text: "יצא סרט שרצית לראות בקולנוע. כרטיסים ופופקורן יעלו כ-₪{value}. ללכת?",
                    getValue: (settings) => Math.random() * (settings.flexibleExpenseMagnitude.max - settings.flexibleExpenseMagnitude.min) + settings.flexibleExpenseMagnitude.min,
                    noOutcome: "וויתרת על הסרט. נשארת בבית וחסכת כסף."
                },
                {
                    text: "יש מבצע טוב בחנות בגדים על פריט שחשבת עליו. יעלה כ-₪{value}. לקנות?",
                     getValue: (settings) => Math.random() * (settings.flexibleExpenseMagnitude.max - settings.flexibleExpenseMagnitude.min) + settings.flexibleExpenseMagnitude.min,
                    noOutcome: "החלטת לוותר על המבצע. הבגדים הקיימים מספיקים וחסכת."
                },
                 {
                    text: "חברים הזמינו לדרינק ספונטני בבר אחרי העבודה. יעלה כ-₪{value}. להצטרף?",
                     getValue: (settings) => Math.random() * (settings.flexibleExpenseMagnitude.max - settings.flexibleExpenseMagnitude.min) + settings.flexibleExpenseMagnitude.min,
                    noOutcome: "בחרת לנוח בבית במקום. גם חשוב וגם חסכת את הכסף."
                },
                {
                    text: "יש הצעה להזמין ארוחת ערב ממסעדה טובה. יעלה כ-₪{value}. להזמין?",
                    getValue: (settings) => Math.random() * (settings.flexibleExpenseMagnitude.max - settings.flexibleExpenseMagnitude.min) + settings.flexibleExpenseMagnitude.min,
                    noOutcome: "בישלת ארוחה בבית. יצא טעים וחסכת משמעותית."
                }
            ]
        };

         const unavoidableExpenses = {
            hard: [
                { text: "תשלום ראשון של שכר דירה/משכנתא או הוצאת דיור גדולה אחרת.", value: -3000 }, // Example large fixed cost
                { text: "תשלום חשבונות חודשיים גבוהים (חשמל, מים, גז).", value: -1200 }, // Example fixed cost
                 { text: "תשלום גדול על ביטוח שנתי או הוצאה פיננסית קבועה אחרת.", value: -1800 } // Example large fixed cost
            ]
         };


        // --- Game Functions ---
        function startGame() {
            const difficulty = difficultySelect.value;
            currentSettings = difficultySettings[difficulty];

            currentDay = 0;
            currentBalance = currentSettings.startBalance;
            monthlyIncome = currentSettings.monthlyIncome;
            gameRunning = true;
            currentDecision = null;

            // Add initial income on day 1 as a positive event
            // We will add it *after* day 0 starts but conceptually it's the salary
            addEventToLog(`התחלת את הסימולציה! יתרת פתיחה: ${currentSettings.startBalance.toFixed(2)} ש"ח.`, 'default');
             processDay(); // Process day 1 immediately

            // Update UI
            updateDisplay();
            gameArea.classList.remove('hidden');
            controlsDiv.classList.add('hidden'); // Hide controls section
            gameResultDiv.classList.add('hidden');
            decisionArea.classList.add('hidden');
            enableButtons(true);
            restartGameButton.classList.add('hidden'); // Hide restart until game ends
        }

        function endGame(win) {
            gameRunning = false;
            enableButtons(false);
            decisionArea.classList.add('hidden'); // Hide decision area if game ends during decision
            gameResultDiv.classList.remove('hidden');
            gameResultDiv.className = 'game-section ' + (win ? 'win' : 'lose'); // Add game-section class back
            resultMessageP.textContent = win
                ? `🎉 ברכות! הצלחת לנהל את התקציב וששרדת את החודש (יום ${currentDay}) עם יתרה חיובית של ${currentBalance.toFixed(2)} ש"ח!`
                : `💔 לצערי, לא הצלחת לשרוד את החודש. הגעת ליום ${currentDay} עם יתרה שלילית של ${currentBalance.toFixed(2)} ש"ח. ניהול תקציב הוא מאתגר, נסה שוב ולמד מהטעויות!`;
            restartGameButton.classList.remove('hidden'); // Ensure restart button is visible
            // controlsDiv.classList.remove('hidden'); // Option to show controls again, or just show restart
        }

        function updateDisplay() {
            currentDaySpan.textContent = currentDay;
            currentBalanceSpan.textContent = currentBalance.toFixed(2);
            // Add classes for color change animation
            currentBalanceSpan.classList.remove('positive', 'negative');
            currentBalanceSpan.classList.add(currentBalance >= 0 ? 'positive' : 'negative');
            // Monthly income is fixed once game starts, no need to update in stats every day, but can keep the span if needed elsewhere
            // monthlyIncomeSpan.textContent = monthlyIncome.toFixed(2);

            if (!gameRunning) return; // Don't check end conditions if game is already over

            if (currentDay >= 30) {
                setTimeout(() => endGame(currentBalance >= 0), 500); // Small delay before showing end result
            } else if (currentBalance < 0 && currentDay > 0) { // Only fail if balance drops below zero *after* day 0
                 setTimeout(() => endGame(false), 500); // Small delay before showing end result
            }
        }

        function addEventToLog(message, type = 'default') {
            const eventElement = document.createElement('div');
            eventElement.classList.add('event-message', type);
            eventElement.textContent = `יום ${currentDay}: ${message}`;
            eventLogDiv.prepend(eventElement); // Add to top

             // Simple animation trigger by adding the element
             // CSS animation handles the rest
             // Limit log size if it gets too long (not strictly necessary for 30 days)
             // while (eventLogDiv.children.length > 50) {
             //    eventLogDiv.removeChild(eventLogDiv.lastChild);
             //}
             // Scroll to top to see latest events
             eventLogDiv.scrollTop = 0;
        }

         function applyBalanceChange(amount, message, type = 'default') {
             currentBalance += amount;
             addEventToLog(message, type);
             updateDisplay(); // Update immediately after change
         }


        function processDay() {
            if (!gameRunning || currentDecision || currentDay >= 30) return; // Don't process day if game not running, waiting for decision, or month is over

            currentDay++;

             // Handle initial income on Day 1
             if (currentDay === 1) {
                  applyBalanceChange(monthlyIncome, `קיבלת את המשכורת החודשית! (+${monthlyIncome.toFixed(2)} ש"ח). התקציב התחיל לפעול.`, 'positive');
             }


            // Check for unavoidable expenses on specific days (based on difficulty)
            if (currentSettings.unavoidableExpenseDays.includes(currentDay)) {
                 // Find which unavoidable expense matches the day index (simple mapping based on array order)
                 const expenseIndex = currentSettings.unavoidableExpenseDays.indexOf(currentDay);
                 if (unavoidableExpenses[difficultySelect.value] && unavoidableExpenses[difficultySelect.value][expenseIndex]) {
                     const unavoidable = unavoidableExpenses[difficultySelect.value][expenseIndex];
                     applyBalanceChange(unavoidable.value, `${unavoidable.text} (${unavoidable.value.toFixed(2)} ש"ח). זו הוצאה קבועה והכרחית!`, 'negative');
                 }
            }


            // Random Events
            if (Math.random() < currentSettings.eventProbability) {
                 const eventType = Math.random() < currentSettings.negativeEventWeight ? 'negative' : 'positive';
                 const eventList = events[eventType];
                 const event = eventList[Math.floor(Math.random() * eventList.length)];
                 const value = event.value(currentSettings); // Pass settings to value function
                 // Format the value in the message text
                 const formattedMessage = event.text.replace('{value}', Math.abs(value).toFixed(2));
                 applyBalanceChange(value, formattedMessage, eventType);
            }

            // Flexible Expense Decision
            // Trigger only if no other decision is pending and it's not the very last day
            if (Math.random() < currentSettings.flexibleExpenseProbability && !currentDecision && currentDay < 30) {
                const flexibleEvent = events.flexible[Math.floor(Math.random() * events.flexible.length)];
                 const cost = flexibleEvent.getValue(currentSettings);
                currentDecision = {
                    text: flexibleEvent.text.replace('~X', cost.toFixed(2)), // Replace placeholder in text
                    yesCost: cost,
                    noOutcome: flexibleEvent.noOutcome
                };
                 addEventToLog(`התעוררה הזדמנות או דילמה פיננסית!`, 'decision'); // Log that a decision is coming
                showDecision(currentDecision);
                return; // Stop processing day until decision is made
            }

            // Check end conditions after all events for the day are processed
            updateDisplay(); // Update display at the end of the day processing if no decision
        }

        function showDecision(decision) {
            decisionText.textContent = decision.text;
            decisionArea.classList.remove('hidden');
            enableButtons(false); // Disable day/week buttons while deciding
        }

        function handleDecision(choice) {
            if (!currentDecision) return; // Should not happen if decision area is visible

            if (choice === 'yes') {
                // Apply cost for 'yes'
                applyBalanceChange(-currentDecision.yesCost, `החלטת לבצע את ההוצאה! ירדו ${currentDecision.yesCost.toFixed(2)} ש"ח מהחשבון.`, 'negative');
            } else { // choice === 'no'
                // Log outcome for 'no' (positive as it saves money)
                addEventToLog(currentDecision.noOutcome, 'positive');
                // No balance change for saying no
            }

            // Clean up decision state
            currentDecision = null;
            decisionArea.classList.add('hidden');

            // Continue game flow
            enableButtons(true); // Re-enable day/week buttons
             updateDisplay(); // Ensure display is updated and checks for game end
        }

        function enableButtons(enable) {
            nextDayButton.disabled = !enable || currentDay >= 30 || !gameRunning;
            nextWeekButton.disabled = !enable || currentDay >= 30 - 7 || !gameRunning; // Disable week button if less than 7 full days left
        }

        // --- Event Listeners ---
        startGameButton.addEventListener('click', startGame);

        nextDayButton.addEventListener('click', () => {
             if (gameRunning && !currentDecision && currentDay < 30) {
                processDay();
            }
        });

        nextWeekButton.addEventListener('click', () => {
             if (gameRunning && !currentDecision && currentDay < 30) {
                // Process up to 7 days, stopping early if a decision appears or game ends
                const daysToProcess = Math.min(30 - currentDay, 7);
                 for (let i = 0; i < daysToProcess; i++) {
                     processDay();
                     if (currentDecision || !gameRunning || currentDay >= 30) break; // Stop if decision appears, game ends, or reached end of month within loop
                 }
            }
        });

        decisionButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                handleDecision(e.target.dataset.choice);
            });
        });

        restartGameButton.addEventListener('click', startGame); // Restart button just calls startGame

         toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            // Optional: Change button text based on state
            // if (explanationDiv.classList.contains('hidden')) {
            //     toggleExplanationButton.textContent = 'הצג הסבר';
            // } else {
            //      toggleExplanationButton.textContent = 'הסתר הסבר';
            // }
         });

        // --- Initialization ---
        // Initialize state on load (e.g., hide game area, show start button)
        gameArea.classList.add('hidden');
        gameResultDiv.classList.add('hidden');
        restartGameButton.classList.add('hidden'); // Hide restart until game ends
        // Update initial balance color class
        currentBalanceSpan.classList.add(currentBalance >= 0 ? 'positive' : 'negative');
    });
</script>
---