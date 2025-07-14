---
title: "להגדיל את הסאונד: מסע לפסגת הפודקאסטים"
english_slug: grow-the-sound-podcast-studio-simulation
category: "ניהול"
tags: [פודקאסטים, ניהול, סימולציה עסקית, אסטרטגיה, מדיה דיגיטלית, משחק לימודי]
---
# להגדיל את הסאונד: מסע לפסגת הפודקאסטים

יש לך את הקול, את הרעיונות, את התשוקה. פתחת אולפן פודקאסטים משלך, אבל זו רק ההתחלה. כדי להפוך לחברת פודקאסטים משפיעה באמת, עליך לנווט בעולם העסקי, לקבל החלטות קריטיות ולבנות אימפריה מהאפס. האם יש לך את מה שנדרש כדי להגדיל את הסאונד ולהגיע לפסגה?

<div class="podcast-simulation-container">
    <div class="stats-panel panel">
        <h2><i class="icon fas fa-chart-line"></i> נתוני האולפן</h2>
        <div class="stat-item">
            <strong>חודש:</strong> <span id="month-stat">1</span>
        </div>
        <div class="stat-item">
            <strong>כסף (<span class="currency">$</span>):</strong> <span id="money-stat" data-value="1000.00">1000.00</span>
        </div>
        <div class="stat-item">
            <strong>מאזינים:</strong> <span id="audience-stat" data-value="100">100</span>
        </div>
        <div class="stat-item">
            <strong>מוניטין:</strong> <span id="reputation-stat" data-value="50">50</span>/100
        </div>
        <div class="stat-item costs">
            <strong>הוצאות חודשיות:</strong> <span id="costs-stat" data-value="0.00">0.00</span><span class="currency">$</span>
        </div>
         <div class="stat-item income">
            <strong>הכנסה חודשית:</strong> <span id="income-stat" data-value="0.00">0.00</span><span class="currency">$</span>
        </div>
    </div>

    <div class="decisions-panel panel">
        <h2><i class="icon fas fa-cogs"></i> קבל החלטות לחודש <span id="current-decision-month">1</span></h2>
        <div class="decision-buttons">
            <button id="decision-content" data-cost="150" data-type="quality">יצירת תוכן חדש (משפר איכות, $150)</button>
            <button id="decision-equipment" data-cost="500" data-type="quality">השקעה בציוד פרימיום (משפר איכות דרמטי, $500)</button>
            <button id="decision-hire-editor" data-cost="200" data-type="staff">העסקת עורך סאונד מקצועי (הוצאות קבועות $200/חודש)</button>
            <button id="decision-hire-marketer" data-cost="250" data-type="staff">העסקת מומחה שיווק (הוצאות קבועות $250/חודש)</button>
             <button id="decision-marketing" data-cost="100" data-type="exposure">קמפיין שיווק ממוקד (מגדיל חשיפה, $100)</button>
             <button id="decision-collaboration" data-cost="300" data-type="exposure">שיתוף פעולה עם פודקאסט מוביל (מגדיל חשיפה ומוניטין, $300)</button>
        </div>
        <p id="decision-message" class="message"></p>
        <button id="next-month-button">התקדמות לחודש הבא <i class="fas fa-arrow-right"></i></button>
    </div>

    <div class="log-panel panel">
        <h2><i class="icon fas fa-book"></i> יומן פעילות</h2>
        <ul id="activity-log">
            <li class="log-entry"><i class="fas fa-microphone"></i> ברוך הבא לאולפן הפודקאסטים החדש שלך! המסע מתחיל עכשיו.</li>
        </ul>
    </div>
     <div id="win-message" class="game-message win-message hidden">
         <h2><i class="fas fa-trophy"></i> ניצחון!</h2>
         <p>הגעת לפסגה! האולפן שלך הפך לכוח משפיע בעולם הפודקאסטים. כל הכבוד על ניהול חכם ואסטרטגיה מבריקה!</p>
         <button onclick="window.location.reload()">התחל משחק חדש</button>
     </div>
     <div id="lose-message" class="game-message lose-message hidden">
         <h2><i class="fas fa-skull-crossbones"></i> הפסד!</h2>
         <p>אוי לא! נגמר לך הכסף והאולפן נאלץ לסגור את שעריו. ניהול פיננסי הוא קריטי להצלחה. נסה שוב!</p>
         <button onclick="window.location.reload()">התחל משחק חדש</button>
     </div>
</div>

<style>
    /* Import Google Fonts and FontAwesome */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');


    :root {
        --primary-color: #6a11cb; /* Deep Purple */
        --secondary-color: #2575fc; /* Bright Blue */
        --text-color: #333;
        --panel-bg: #ffffff;
        --body-bg: #f0f2f5;
        --border-color: #e0e0e0;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --warning-color: #ffc107;
        --info-color: #17a2b8;
        --button-hover-darken: 15%;
        --panel-shadow: rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: var(--body-bg);
        color: var(--text-color);
        line-height: 1.6;
        padding: 20px;
    }

    h1 {
        text-align: center;
        color: var(--primary-color);
        margin-bottom: 30px;
        font-weight: 700;
    }

    .podcast-simulation-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto auto; /* Stats, Decisions, Log */
        gap: 20px;
        margin-top: 20px;
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
    }

    .panel {
        background-color: var(--panel-bg);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 8px 16px var(--panel-shadow);
        display: flex;
        flex-direction: column;
    }

    .stats-panel {
        grid-column: 1 / 2; /* Left column */
        grid-row: 1 / 2; /* Top row */
        justify-content: space-between;
    }

    .decisions-panel {
         grid-column: 2 / 3; /* Right column */
         grid-row: 1 / 2; /* Top row */
    }

    .log-panel {
        grid-column: 1 / 3; /* Span both columns */
        grid-row: 2 / 3; /* Middle row */
        max-height: 300px; /* Limit height */
        overflow-y: auto; /* Add scroll */
    }

     .game-message {
         grid-column: 1 / 3; /* Span both columns */
         grid-row: 3 / 4; /* Bottom row */
         text-align: center;
         padding: 30px;
         border-radius: 12px;
         margin-top: 20px;
         font-size: 1.2em;
         font-weight: 700;
         box-shadow: 0 4px 8px var(--panel-shadow);
         animation: fadeIn 0.5s ease-out;
     }

     .win-message {
         background-color: #d4edda; /* Light green */
         color: var(--success-color);
         border: 1px solid #c3e6cb;
     }

     .lose-message {
         background-color: #f8d7da; /* Light red */
         color: var(--danger-color);
         border: 1px solid #f5c6cb;
     }

     .game-message h2 {
         margin-top: 0;
         color: inherit; /* Use parent color */
         border-bottom: none;
         padding-bottom: 0;
         margin-bottom: 15px;
         display: flex;
         align-items: center;
         justify-content: center;
     }

     .game-message h2 .fas {
         margin-left: 10px; /* Space between icon and text */
     }


    .panel h2 {
        margin-top: 0;
        color: var(--primary-color);
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 15px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }

    .panel h2 .icon {
        margin-left: 10px; /* Space for icon */
        color: var(--secondary-color);
    }

    .stats-panel .stat-item {
        margin: 12px 0;
        font-size: 1.1em;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 5px;
        border-bottom: 1px dotted var(--border-color);
    }
     .stats-panel .stat-item:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }

    .stats-panel .stat-item strong {
        font-weight: 700;
        color: var(--text-color);
    }

    .stats-panel .stat-item span {
         font-weight: 400;
         color: #555;
    }

     .stats-panel .stat-item .currency {
         margin-right: 2px;
         font-size: 0.9em;
     }

     .stats-panel .stat-item.costs span {
         color: var(--danger-color);
     }
     .stats-panel .stat-item.income span {
         color: var(--success-color);
     }


    .decisions-panel .decision-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        margin-bottom: 20px;
    }

    .decisions-panel button, .game-message button {
        padding: 12px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1em;
        font-weight: 700;
        transition: background-color 0.3s ease, transform 0.1s ease;
        flex-grow: 1; /* Allow buttons to grow */
        min-width: 150px; /* Minimum width */
    }

    .decisions-panel button:not(#next-month-button) {
         background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
         color: white;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }


     .decisions-panel button:not(#next-month-button):hover {
         background: linear-gradient(45deg, var(--secondary-color), var(--primary-color));
         transform: translateY(-2px); /* Subtle lift effect */
     }
     .decisions-panel button:not(#next-month-button):active {
          transform: translateY(0); /* Press effect */
     }

     .decisions-panel button:disabled {
        background-color: #cccccc !important; /* Override gradient */
        color: #666 !important;
        cursor: not-allowed !important;
        box-shadow: none !important;
        transform: none !important;
     }


    #next-month-button, .game-message button {
        display: block;
        width: 100%;
        padding: 15px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        background-color: var(--success-color);
        color: white;
        font-size: 1.1em;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    #next-month-button i {
        margin-left: 10px; /* Space for icon */
    }

    #next-month-button:hover, .game-message button:hover {
        background-color: color-mix(in srgb, var(--success-color), black var(--button-hover-darken));
        transform: translateY(-2px);
    }
     #next-month-button:active, .game-message button:active {
          transform: translateY(0);
     }


    .log-panel ul {
        list-style: none;
        padding: 0;
        margin: 0; /* Remove default margin */
    }

    .log-panel li {
        padding: 12px 10px;
        border-bottom: 1px dashed var(--border-color);
        font-size: 0.95em;
        color: #555;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly lower */
        animation: logEntryFadeIn 0.5s ease-out forwards; /* Animation */
    }

    .log-panel li:first-child {
        animation-delay: 0.1s; /* Stagger animations */
    }
    .log-panel li:nth-child(2) { animation-delay: 0.2s; }
    .log-panel li:nth-child(3) { animation-delay: 0.3s; }
    .log-panel li:nth-child(4) { animation-delay: 0.4s; }
    /* Add more delays or use JS for dynamic staggering */


    .log-panel li i {
         margin-left: 8px; /* Space for icon */
         color: var(--primary-color); /* Icon color */
         font-size: 1.1em;
    }


    .log-panel li:last-child {
        border-bottom: none;
    }

    .message {
        color: var(--danger-color);
        font-weight: 700;
        text-align: center;
        min-height: 1.2em; /* Reserve space */
        margin-bottom: 10px;
    }

    .hidden {
        display: none !important;
    }


    #explanation-button {
        display: block;
        margin: 30px auto 20px;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        background-color: var(--info-color);
        color: white;
        font-size: 1em;
        font-weight: 700;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 4px var(--panel-shadow);
    }

    #explanation-button:hover {
         background-color: color-mix(in srgb, var(--info-color), black var(--button-hover-darken));
         transform: translateY(-2px);
    }

     #explanation-button:active {
          transform: translateY(0);
     }


    #explanation {
        margin-top: 30px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--panel-bg);
        box-shadow: 0 4px 8px var(--panel-shadow);
        display: none; /* Initially hidden */
        direction: rtl;
        text-align: right;
    }

    #explanation h2 {
        color: var(--primary-color);
        margin-top: 0;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 15px;
        margin-bottom: 20px;
        font-weight: 700;
    }

    #explanation h3 {
         color: var(--secondary-color);
         margin-top: 25px;
         margin-bottom: 10px;
         font-weight: 700;
    }

     #explanation p {
         margin-bottom: 15px;
         color: #555;
     }

     #explanation ul {
         list-style: disc inside;
         padding-right: 20px;
         margin-bottom: 15px;
     }

     #explanation li {
         margin-bottom: 10px;
         line-height: 1.6;
         color: #555;
     }

     /* Animations */
     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }

     @keyframes logEntryFadeIn {
         to { opacity: 1; transform: translateY(0); }
     }

     /* Responsive adjustments */
     @media (max-width: 768px) {
         .podcast-simulation-container {
             grid-template-columns: 1fr; /* Single column layout */
             grid-template-rows: auto auto auto auto; /* Stack panels */
         }
          .stats-panel, .decisions-panel, .log-panel, .game-message {
             grid-column: 1 / 2; /* All span the single column */
         }
          .stats-panel { grid-row: 1; }
          .decisions-panel { grid-row: 2; }
          .log-panel { grid-row: 3; max-height: 200px; }
          .game-message { grid-row: 4; }

         .decisions-panel .decision-buttons {
             flex-direction: column; /* Stack buttons */
         }
     }

</style>

<button id="explanation-button">הצג/הסתר מידע על ניהול אולפן פודקאסט</button>

<div id="explanation">
    <h2>מדריך למנהל האולפן: האתגר העסקי של פודקאסטים</h2>
    <p>ברכות על שהתחלת את המסע שלך בעולם הפודקאסטים! הסימולציה הזו היא הזדמנות לחוות ממקור ראשון את ההיבטים העסקיים והניהוליים שמעבר ליצירת התוכן עצמה. ניהול אולפן מצליח דורש שילוב של יצירתיות, אסטרטגיה פיננסית חכמה והבנה מעמיקה של השוק.</p>

    <h3>מהו בעצם אולפן פודקאסטים פעיל?</h3>
    <p>מעבר למיקרופון וחדר מבודד, אולפן פודקאסטים הוא מערכת הכוללת תכנון תוכן, הפקה טכנית (הקלטה ועריכה), אסטרטגיית הפצה, פעילויות שיווק, ובניית קהילה נאמנה. הוא יכול להיות פרויקט של יוצר בודד או מיזם עם צוות שלם. האתגר המרכזי הוא להפוך את התשוקה שלך ליצירה לעסק בר-קיימא וצומח.</p>

    <h3>המעבר מיוצר למנהל: נקודת המבט החדשה</h3>
    <p>כשאתה יוצר, המיקוד הוא על הפרק הבא, האורח הבא, והסאונד המושלם. כמנהל, עליך להרים את המבט ולראות את התמונה הגדולה: איך להרחיב את הקהל? מתי להשקיע בציוד יקר יותר? האם לשכור עזרה? ואיך להבטיח שהכסף לא ייגמר לפני שההצלחה מגיעה? הסימולציה מאתגרת אותך לחשוב כמו מנהל, תוך איזון בין השקעות שונות והסיכון הכרוך בהן.</p>

    <h3>החלטות קריטיות בדרך לפסגה:</h3>
    <ul>
        <li>
            <strong>איכות התוכן וההפקה (<span style="color: var(--primary-color); font-weight: bold;">איכות</span>):</strong> הלב הפועם של האולפן. השקעה בתוכן חדש שומרת על האולפן רלוונטי ומביאה מאזינים חדשים. שדרוג ציוד משפר את איכות הסאונד באופן ניכר ומשפיע לטובה על חווית המאזין ועל המוניטין. עורך סאונד מקצועי יכול לקחת את האיכות לרמה הבאה ולפנות לך זמן יקר. השקעות אלו מגדילות את נאמנות הקהל ואת קצב הצמיחה הטבעי.
        </li>
        <li>
            <strong>שיווק וחשיפה (<span style="color: var(--secondary-color); font-weight: bold;">חשיפה</span>):</strong> תוכן מדהים לא ימצא את דרכו למאזינים לבד. קמפיינים שיווקיים ופרסום ממוקד חיוניים להגדלת החשיפה ולהבאת מאזינים חדשים במהירות. שיתופי פעולה אסטרטגיים עם גורמים אחרים בתעשייה יכולים להקפיץ את מספר המאזינים ואף לשדרג את המוניטין שלך באופן משמעותי. מומחה שיווק יכול לתכנן ולהוציא לפועל אסטרטגיות אלו בצורה יעילה יותר.
        </li>
        <li>
            <strong>ניהול פיננסי (<span style="color: var(--danger-color); font-weight: bold;">כסף</span>):</strong> כל החלטה עסקית כרוכה בעלות. עליך לנהל את התקציב שלך בחוכמה, לאזן בין הוצאות להשקעות, ולעקוב אחרי ההכנסות (בסימולציה זו ההכנסה מבוססת על מספר המאזינים הנוכחי). הוצאות קבועות (כמו משכורות לעובדים) מצמצמות את הגמישות הפיננסית שלך אך מאפשרות צמיחה בקנה מידה גדול יותר. ניהול כושל עלול להוביל לפשיטת רגל!
        </li>
        <li>
            <strong>בניית צוות (<span style="color: var(--success-color); font-weight: bold;">צוות</span>):</strong> אי אפשר לעשות הכל לבד לנצח. העסקת אנשי מקצוע (עורך, משווק) מגדילה את ההוצאות החודשיות, אך היא משחררת אותך להתמקד בליבת העשייה או בתכנון האסטרטגיה, ומאפשרת לך לשדרג את התוצר הסופי ואת יכולות ההגעה לקהל.
        </li>
    </ul>

    <h3>מעקב אחר מדדים ואותות הצלחה:</h3>
    <p>מספר המאזינים הוא המדד העיקרי לצמיחה, אך עליך לשים לב גם למוניטין (שמשפיע על צמיחה עתידית ועל הזדמנויות), למצב הפיננסי שלך (יתרה בחשבון), ולהכנסות והוצאות החודשיות. כל החלטה תשפיע על המדדים הללו בדרכים שונות, לעיתים מיידית ולעיתים לאורך זמן.</p>

    <h3>סיכום: האם תצליח לבנות אימפריה?</h3>
    <p>ההצלחה בעולם הפודקאסטים היא ריצת מרתון, לא ספרינט. היא דורשת סבלנות, קבלת החלטות אמיצות, ולעיתים גם קצת מזל. האם תצליח לאזן בין יצירה לבין עסקים, להשקיע נכון, לגייס את האנשים המתאימים, ולבנות קהל נאמן שיעלה אותך לפסגת הפודקאסטים? שיהיה בהצלחה!</p>
</div>


<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Game State
        let gameState = {
            month: 1,
            money: 1000,
            audience: 100,
            reputation: 50, // out of 100
            monthlyCosts: 0,
            monthlyIncome: 0,
            hasEditor: false,
            hasMarketer: false,
            qualityLevel: 1, // Starts at 1, can increase
            exposureLevel: 1, // Starts at 1, can increase
            decisionsMadeThisMonth: new Set(), // To track decisions made in the current month to enable/disable buttons
            pendingEffects: [], // Effects that apply next month
        };

        // Constants and Modifiers
        const baseMonthlyCosts = 50; // Hosting, software etc.
        const incomePerListener = 0.01; // Simple monetization model
        const baseAudienceGrowth = 10; // Base organic growth
        const winAudienceThreshold = 25000; // Audience needed to win

        // UI Elements
        const monthStat = document.getElementById('month-stat');
        const moneyStat = document.getElementById('money-stat');
        const audienceStat = document.getElementById('audience-stat');
        const reputationStat = document.getElementById('reputation-stat');
        const costsStat = document.getElementById('costs-stat');
        const incomeStat = document.getElementById('income-stat');
        const currentDecisionMonth = document.getElementById('current-decision-month');
        const decisionButtons = document.querySelectorAll('.decision-buttons button:not(#next-month-button)');
        const decisionMessage = document.getElementById('decision-message');
        const nextMonthButton = document.getElementById('next-month-button');
        const activityLog = document.getElementById('activity-log');
        const explanationButton = document.getElementById('explanation-button');
        const explanationDiv = document.getElementById('explanation');
        const winMessageDiv = document.getElementById('win-message');
        const loseMessageDiv = document.getElementById('lose-message');
        const simulationContainer = document.querySelector('.podcast-simulation-container');


        // Helper function to animate stat changes
        function animateStat(element, startValue, endValue, duration = 500) {
            const dataAttribute = element.id.replace('-stat', ''); // e.g., 'money', 'audience'
            const isMoneyOrCost = dataAttribute === 'money' || dataAttribute === 'costs' || dataAttribute === 'income';
            const isReputation = dataAttribute === 'reputation';
            const isAudience = dataAttribute === 'audience';

            const startTime = performance.now();
            const start = parseFloat(element.dataset.value);
            const end = parseFloat(endValue);
            element.dataset.value = endValue.toFixed(isMoneyOrCost ? 2 : 0); // Update data value immediately

            function update(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const currentValue = start + (end - start) * progress;

                if (isMoneyOrCost) {
                    element.textContent = currentValue.toFixed(2);
                } else if (isReputation) {
                    element.textContent = currentValue.toFixed(0);
                } else if (isAudience) {
                    element.textContent = currentValue.toFixed(0);
                } else {
                     element.textContent = currentValue.toFixed(0); // Default for others like month
                }


                if (progress < 1) {
                    requestAnimationFrame(update);
                } else {
                     // Ensure final value is set precisely
                     if (isMoneyOrCost) {
                         element.textContent = end.toFixed(2);
                     } else if (isReputation) {
                         element.textContent = end.toFixed(0);
                     } else if (isAudience) {
                        element.textContent = end.toFixed(0);
                     } else {
                         element.textContent = end.toFixed(0);
                     }
                }
            }

            requestAnimationFrame(update);
        }


        // Update UI function
        function updateUI() {
            animateStat(monthStat, parseFloat(monthStat.dataset.value), gameState.month);
            animateStat(moneyStat, parseFloat(moneyStat.dataset.value), gameState.money);
            animateStat(audienceStat, parseFloat(audienceStat.dataset.value), gameState.audience);
            animateStat(reputationStat, parseFloat(reputationStat.dataset.value), gameState.reputation);
            animateStat(costsStat, parseFloat(costsStat.dataset.value), gameState.monthlyCosts);
            animateStat(incomeStat, parseFloat(incomeStat.dataset.value), gameState.monthlyIncome);

            currentDecisionMonth.textContent = gameState.month;

            // Disable buttons for hires if already hired
            document.getElementById('decision-hire-editor').disabled = gameState.hasEditor;
            document.getElementById('decision-hire-marketer').disabled = gameState.hasMarketer;

             // Disable all decision buttons if already made this month (optional, or allow multiple)
             // Let's allow multiple but add visual feedback
            decisionButtons.forEach(button => {
                 if (gameState.decisionsMadeThisMonth.has(button.id)) {
                     button.classList.add('made-decision'); // Add a class for styling
                 } else {
                      button.classList.remove('made-decision');
                 }
            });

        }

        // Add log entry
        function addLog(message, iconClass = 'fas fa-info-circle') {
            const li = document.createElement('li');
            li.classList.add('log-entry');
            li.innerHTML = `<i class="${iconClass}"></i> חודש ${gameState.month}: ${message}`;
            // Add to the top of the list
            if (activityLog.firstChild) {
                 activityLog.insertBefore(li, activityLog.firstChild);
            } else {
                 activityLog.appendChild(li);
            }
             // Apply animation delay to new element - CSS handles this
        }

        // Decision handling
        decisionButtons.forEach(button => {
            button.addEventListener('click', (event) => {
                const cost = parseFloat(event.target.dataset.cost);
                const decisionId = event.target.id;
                const decisionType = event.target.dataset.type; // Use data-type for logic


                // Re-enable button logic (if limiting decisions per month) - not needed with current model, just track for feedback
                // if (gameState.decisionsMadeThisMonth.has(decisionId)) {
                //     decisionMessage.textContent = 'כבר קיבלת החלטה זו החודש!';
                //     return;
                // }


                if (gameState.money < cost) {
                    decisionMessage.textContent = 'אין מספיק כסף לקבלת החלטה זו!';
                    decisionMessage.style.color = var(--danger-color);
                    return;
                }

                gameState.money -= cost;
                gameState.decisionsMadeThisMonth.add(decisionId); // Mark decision as made

                decisionMessage.textContent = ''; // Clear previous message
                decisionMessage.style.color = ''; // Reset color

                let logMessage = '';
                let icon = 'fas fa-check-circle'; // Default icon

                // Effects are now primarily handled as 'pendingEffects' to apply next month
                let effect = { type: decisionType, amount: 0, cost: cost, id: decisionId };


                switch (decisionId) {
                    case 'decision-content':
                        effect.amount = Math.random() * 40 + 30; // Direct audience boost next month
                        effect.qualityBoost = 1; // Small quality boost
                        logMessage = `השקעת בפרק פודקאסט חדשני! (${cost}$) הקהל בהחלט יאהב את זה.`;
                        icon = 'fas fa-microphone-alt';
                        break;
                    case 'decision-equipment':
                        effect.qualityBoost = 5; // Significant quality boost
                         effect.reputationBoost = 5; // Rep boost
                        logMessage = `שדרגת את ציוד האולפן שלך! (${cost}$) איכות הסאונד קפצה מדרגה.`;
                        icon = 'fas fa-headphones-alt';
                        break;
                    case 'decision-hire-editor':
                        if (!gameState.hasEditor) {
                            gameState.hasEditor = true;
                            effect.monthlyCostIncrease = 200; // Monthly cost change
                            effect.qualityBoost = 3; // Permanent quality boost from editor
                             logMessage = `העסקת את עורך הסאונד המוביל בתעשייה! (${cost}$) האולפן שלך נשמע עכשיו מקצועי מתמיד. הוצאות חודשיות גדלו.`;
                            icon = 'fas fa-cut';
                        } else {
                             decisionMessage.textContent = 'כבר העסקת עורך סאונד מקצועי!';
                             decisionMessage.style.color = var(--warning-color);
                             gameState.money += cost; // Refund cost
                             gameState.decisionsMadeThisMonth.delete(decisionId); // Remove from made decisions
                             updateUI();
                             return; // Stop here
                        }
                        break;
                     case 'decision-hire-marketer':
                         if (!gameState.hasMarketer) {
                             gameState.hasMarketer = true;
                             effect.monthlyCostIncrease = 250; // Monthly cost change
                             effect.exposureBoost = 3; // Permanent exposure boost from marketer
                             logMessage = `הצוות גדל! הצטרף מומחה שיווק (${cost$). הגיע הזמן לכבוש את טבלאות ההאזנה. הוצאות חודשיות גדלו.`;
                             icon = 'fas fa-bullhorn';
                         } else {
                              decisionMessage.textContent = 'כבר העסקת מומחה שיווק!';
                              decisionMessage.style.color = var(--warning-color);
                              gameState.money += cost; // Refund cost
                              gameState.decisionsMadeThisMonth.delete(decisionId); // Remove from made decisions
                              updateUI();
                              return; // Stop here
                         }
                         break;
                     case 'decision-marketing':
                          // Effectiveness depends on having a marketer and randomness
                          const baseBoost = gameState.hasMarketer ? 100 : 30;
                          effect.amount = baseBoost + (Math.random() * baseBoost); // Random boost
                          effect.exposureBoost = 1; // Small temporary exposure boost
                          logMessage = `קמפיין שיווקי חדש עלה לאוויר! (${cost}$) מקווים לראות תוצאות בקרוב.`;
                          icon = 'fas fa-share-alt';
                         break;
                     case 'decision-collaboration':
                         // Collaboration outcome is more random and depends on reputation
                         const successChance = 0.4 + (gameState.reputation / 100) * 0.3; // 40% base + up to 30% from rep
                         const success = Math.random() < successChance;

                         if (success) {
                             effect.amount = gameState.audience * (Math.random() * 0.2 + 0.1); // 10-30% audience jump
                             effect.reputationBoost = Math.random() * 8 + 5; // Decent rep boost
                              logMessage = `בום! שיתוף פעולה עם פודקאסט ענק הצליח! (${cost}$) הקהל מזנק והמוניטין בשמיים!`;
                             icon = 'fas fa-handshake';
                         } else {
                              effect.amount = Math.random() * 20; // Small or no boost
                              effect.reputationBoost = Math.random() * 3; // Small or no rep boost
                              logMessage = `ניסית ליזום שיתוף פעולה גדול (${cost}$), אך הוא לא המריא כמצופה...`;
                              icon = 'fas fa-times-circle';
                              // Add small penalty/lesson learned? Maybe not for this sim.
                         }
                         effect.type = 'collaboration'; // Ensure type is correct
                         break;
                }

                // Queue effects for next month's calculation
                gameState.pendingEffects.push(effect);

                addLog(logMessage, icon);
                updateUI(); // Update money and button state immediately
                 // Optional: brief visual feedback on button click (handled in CSS via :active)
            });
        });

        // Next Month Logic
        nextMonthButton.addEventListener('click', () => {
             if (winMessageDiv.classList.contains('hidden') === false || loseMessageDiv.classList.contains('hidden') === false) {
                 // Game is over, do nothing
                 return;
             }

            // --- Apply Effects from previous month's decisions ---
            let totalAudienceBoostFromDecisions = 0;
            let totalReputationBoostFromDecisions = 0;
            let totalMonthlyCostChangeFromDecisions = 0;

            gameState.pendingEffects.forEach(effect => {
                switch (effect.type) {
                    case 'quality': // Content, Equipment
                        // Temporary audience boost applied directly from effect.amount (content)
                        totalAudienceBoostFromDecisions += effect.amount || 0;
                        // Permanent quality boost
                        gameState.qualityLevel += effect.qualityBoost || 0;
                         totalReputationBoostFromDecisions += effect.reputationBoost || 0;
                        break;
                    case 'staff': // Hire Editor, Hire Marketer
                        gameState.monthlyCosts += effect.monthlyCostIncrease || 0; // Permanent cost increase
                         gameState.qualityLevel += effect.qualityBoost || 0; // Permanent quality boost from editor
                         gameState.exposureLevel += effect.exposureBoost || 0; // Permanent exposure boost from marketer
                        break;
                    case 'exposure': // Marketing
                         // Temporary audience boost applied directly from effect.amount
                         totalAudienceBoostFromDecisions += effect.amount || 0;
                         gameState.exposureLevel += effect.exposureBoost || 0; // Small temporary exposure boost from specific campaign
                        break;
                     case 'collaboration':
                         totalAudienceBoostFromDecisions += effect.amount || 0;
                         totalReputationBoostFromDecisions += effect.reputationBoost || 0;
                         break;
                }
            });

             // Clear pending effects after applying
            gameState.pendingEffects = [];


            // --- Calculate monthly changes based on new state ---

            // Calculate costs for the month
            // Base costs + permanent staff costs
            gameState.monthlyCosts = baseMonthlyCosts + (gameState.hasEditor ? 200 : 0) + (gameState.hasMarketer ? 250 : 0);


            // Calculate income for the month (based on current audience)
            gameState.monthlyIncome = gameState.audience * incomePerListener;

            // Calculate audience growth for this month
            let currentAudienceGrowth = baseAudienceGrowth;

            // Organic growth modified by Quality and Reputation
            currentAudienceGrowth += (gameState.audience / 100) * (gameState.qualityLevel * 0.5); // Quality improves % growth
            currentAudienceGrowth += (gameState.reputation / 100) * 50; // Reputation adds up to 50 base listeners

            // Growth boosted by Exposure level (from marketer/marketing actions)
             currentAudienceGrowth += gameState.exposureLevel * 10; // Base boost from exposure level

             // Add temporary boosts from last month's decisions (already summed in totalAudienceBoostFromDecisions)
            currentAudienceGrowth += totalAudienceBoostFromDecisions;

            // Ensure growth is not negative (e.g., if reputation is very low, though unlikely with this model)
            currentAudienceGrowth = Math.max(5, currentAudienceGrowth); // Ensure at least minimal organic growth

            // Apply changes
            gameState.money += gameState.monthlyIncome - gameState.monthlyCosts;
            gameState.audience += currentAudienceGrowth;

             // Apply reputation boost from decisions
            gameState.reputation = Math.min(100, gameState.reputation + totalReputationBoostFromDecisions);
             // Simple reputation decay (optional, adds challenge)
            gameState.reputation = Math.max(1, gameState.reputation - 1); // Small decay


             // Reset temporary levels/effects for next month
             // Note: this simplified model resets exposureLevel each month unless boosted by hiring marketer
             // A more complex model would have decay for temporary boosts. Let's reset temporary parts.
             // Revert temp exposure boost from specific marketing campaigns
             gameState.exposureLevel = (gameState.hasMarketer ? 3 : 1); // Reset to base + marketer effect


            // --- Check Game State (Win/Lose) ---
            if (gameState.money < 0) {
                addLog('נגמר לך הכסף! ניהול האולפן נכשל ונסגר.', 'fas fa-sad-cry');
                 endGame(false); // Lose
                 return;
            }

             if (gameState.audience >= winAudienceThreshold && gameState.reputation >= 80) { // Win condition
                 addLog('הגעת ליעד! האולפן שלך בפסגה!', 'fas fa-trophy');
                 endGame(true); // Win
                 return;
             }


            // --- Prepare for next month ---
            gameState.month++;
            gameState.decisionsMadeThisMonth.clear(); // Reset decisions for the new month


            // --- Update UI and Log ---
            updateUI();

            // Log end of month summary
            const summaryLog = document.createElement('li');
            summaryLog.classList.add('log-entry');
            summaryLog.innerHTML = `<i class="fas fa-calendar-check"></i> <strong>סיכום חודש ${gameState.month - 1}:</strong> מאזינים חדשים: ${currentAudienceGrowth.toFixed(0)}. הכנסה: <span style="color: var(--success-color);">${gameState.monthlyIncome.toFixed(2)}$</span>, הוצאות: <span style="color: var(--danger-color);">${gameState.monthlyCosts.toFixed(2)}$</span>. יתרה בקופה: ${gameState.money.toFixed(2)}$.`;

             if (activityLog.firstChild) {
                 activityLog.insertBefore(summaryLog, activityLog.firstChild);
             } else {
                 activityLog.appendChild(summaryLog);
             }
             // Add a separator or distinct style for summary?
             summaryLog.style.fontWeight = 'bold';
             summaryLog.style.backgroundColor = '#e9ecef';
             summaryLog.style.borderRight = `4px solid ${var(--info-color)}`;


        });

        // End Game function
        function endGame(isWin) {
            decisionButtons.forEach(btn => btn.disabled = true);
            nextMonthButton.disabled = true;
             nextMonthButton.classList.add('disabled'); // Add disabled class for styling
             decisionButtons.forEach(btn => btn.classList.add('disabled'));

            if (isWin) {
                winMessageDiv.classList.remove('hidden');
            } else {
                loseMessageDiv.classList.remove('hidden');
            }

             simulationContainer.scrollTop = simulationContainer.scrollHeight; // Scroll to bottom to show message
        }


        // Explanation button toggle
        explanationButton.addEventListener('click', () => {
            if (explanationDiv.classList.contains('hidden') || explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
                explanationDiv.style.display = 'block'; // Use block to override potential 'hidden' class display: none
                 explanationDiv.classList.remove('hidden');
            } else {
                explanationDiv.style.display = 'none';
                 explanationDiv.classList.add('hidden');
            }
        });

        // Initial UI update
        updateUI();
         // Hide win/lose messages initially
         winMessageDiv.classList.add('hidden');
         loseMessageDiv.classList.add('hidden');
    });
</script>
```