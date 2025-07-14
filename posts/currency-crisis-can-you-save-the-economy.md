---
title: "משבר מטבע: האם תצליח להציל את הכלכלה?"
english_slug: currency-crisis-can-you-save-the-economy
category: "מדעי החברה / כלכלה ופיננסים"
tags: ["כלכלה", "משבר פיננסי", "מטבע", "מדיניות מוניטרית", "שווקים מתפתחים"]
---
# משבר מטבע: האם תצליח להציל את הכלכלה?

שער המטבע של המדינה שלך צונח במהירות, אינפלציה מאיימת לצאת משליטה, והמשקיעים בורחים בבהלה. האם יש לך את מה שנדרש כדי לקבל את ההחלטות הנכונות ולהציל את הכלכלה מהתמוטטות מוחלטת? גורל המדינה בידיים שלך!

<div id="currency-crisis-app">
    <div class="dashboard">
        <h2>לוח מחוונים כלכלי</h2>
        <div class="indicators">
            <div class="indicator"><span class="label">חודש:</span> <span id="current-month" class="value">1</span></div>
            <div class="indicator"><span class="label">שער חליפין (מטבע מקומי/$):</span> <span id="exchange-rate" class="value indicator-danger">---</span></div>
            <div class="indicator"><span class="label">אינפלציה שנתית (%):</span> <span id="inflation" class="value indicator-danger">---</span></div>
            <div class="indicator"><span class="label">יתרות מט"ח (במיליארדי $):</span> <span id="reserves" class="value indicator-danger">---</span></div>
            <div class="indicator"><span class="label">ריבית בנק מרכזי (%):</span> <span id="interest-rate" class="value">---</span></div>
            <div class="indicator"><span class="label">צמיחת תמ"ג שנתית (%):</span> <span id="gdp-growth" class="value indicator-danger">---</span></div>
        </div>
    </div>

    <div class="actions">
        <h2>פעולות מדיניות</h2>
        <button class="policy-button" data-policy="raise-rate">🚀 העלאת ריבית</button>
        <button class="policy-button" data-policy="lower-rate" disabled>📉 הורדת ריבית</button>
        <button class="policy-button" data-policy="intervene-buy">🛡️ התערבות: קניית מטבע מקומי</button>
        <button class="policy-button" data-policy="intervene-sell" disabled>💸 התערבות: מכירת מטבע מקומי</button>
        <button class="policy-button" data-policy="capital-controls">🔒 הטלת פיקוח הון</button>
        <button class="policy-button" data-policy="fiscal-cuts">✂️ קיצוצים תקציביים</button>
    </div>

    <div class="status">
        <h2>מצב ועדכוני החודש</h2>
        <p id="status-message">בחר פעולה לחודש 1 כדי להתחיל להתמודד עם המשבר המשתולל!</p>
        <div class="progress-bar-container hidden">
            <div class="progress-bar"></div>
        </div>
    </div>

    <div id="game-over-overlay" class="hidden">
        <div class="game-over-content">
            <h2 id="game-over-title"></h2>
            <p id="game-over-text"></p>
            <button id="restart-button">🎮 התחל מחדש</button>
        </div>
    </div>
</div>

<button id="toggle-explanation">📚 הצג/הסתר מדריך למשבר</button>

<div id="explanation" class="hidden">
    <h2>הבנת משבר מטבע ודרכי התמודדות</h2>

    <h3>מהו משבר מטבע וכיצד הוא מתחיל?</h3>
    משבר מטבע הוא מצב דרמטי שבו שער החליפין של מטבע מסוים צולל במהירות מסחררת. בדרך כלל, זה קורה במדינות עם שער חליפין שהבנק המרכזי מנסה להגן עליו, אך נאלץ לנטוש את המאמץ מול לחץ אדיר של השוק. המשבר יכול להתפרץ כתוצאה מפאניקה והתמוטטות אמון שמובילות לבריחת הון המונית, או התקפה ספקולטיבית מתוחכמת על המטבע.

    <h3>הכוחות המניעים מאחורי משברי מטבע</h3>
    <ul>
        <li>**בריחת הון (Capital Flight):** כשמשקיעים מקומיים וזרים מאבדים אמון, הם מוכרים נכסים במטבע המקומי ודוהרים לקנות מט"ח (דולרים, יורו). הביקוש הקופץ למט"ח והיצע המטבע המקומי שמוצף בשוק מפילים את ערך המטבע שלך.</li>
        <li>**מתקפות ספקולטיביות:** שחקנים בשווקים הפיננסיים המזהים חולשה במטבע "מהמרים" על נפילתו. הם מוכרים בחדות מטבע מקומי (שלרוב לווי) וקונים מט"ח, ומקווים לקנות בחזרה את המטבע המקומי בזול יותר אחרי הפיחות כדי לגרוף רווח ענק. מתקפות כאלה יכולות לרוקן גם את קופת המט"ח של בנק מרכזי חזק.</li>
        <li>**עול החוב החיצוני:** אם למדינה (או לחברותיה) יש חוב גדול במטבע זר, היחלשות המטבע המקומי מייקרת את החזר החוב בצורה כואבת. זה מגביר את הסיכון לחדלות פירעון ומלבה את הפאניקה.</li>
        <li>**יסודות כלכליים רעועים:** גירעונות ענק בחשבון השוטף (יבוא שגובר בהרבה על יצוא), גירעונות תקציביים כרוניים, אינפלציה דוהרת ומערכת בנקאית חלשה – כל אלה מרוקנים את חוסן הכלכלה והופכים אותה למטרה קלה למשבר.</li>
    </ul>

    <h3>ארגז הכלים שלך כמציל הכלכלה</h3>
    *   **מדיניות מוניטרית (שליטה בריבית):**
        *   **העלאת ריבית:** כמו מכת חשמל לכלכלה. הופכת השקעה במטבע שלך לאטרקטיבית יותר (משקיעים רוצים תשואה גבוהה), מושכת הון בחזרה ותומכת בשער החליפין. גם עוזרת לרסן את האינפלציה, אך מייקרת אשראי ועלולה לבלום צמיחה (או להחמיר מיתון).
        *   **הורדת ריבית:** בדרך כלל לא אופציה במשבר, אלא אם כן רוצים לעודד צמיחה *אחרי* שהמשבר נפתר.
    *   **התערבות בשוק המט"ח:** הבנק המרכזי פותח את קופסת החירום, מוכר את הדולרים/יורו שברשותו וקונה מטבע מקומי. זה מגביר מלאכותית את הביקוש למטבע שלך ומעלה את שערו. כלי מהיר אך מוגבל בגודל יתרות המט"ח שנותרו לך.
    *   **פיקוח הון (Capital Controls):** הטלת מגבלות על כמה כסף יכול להיכנס או לצאת מהמדינה. כמו סכר זמני לבלימת בריחת הון מיידית. יכול להרוויח זמן, אבל פוגע קשות במוניטין של המדינה ומרתיע משקיעים עתידיים.
    *   **מדיניות פיסקלית (תקציב הממשלה):**
        *   **קיצוצים תקציביים והעלאות מיסים:** צמצום הוצאות הממשלה או הגדלת הכנסותיה. מקטין את החוב הלאומי ושולח איתות חיובי לשווקים על אחריות פיסקלית, מה שיכול לשקם אמון. החיסרון: קיצוצים עלולים להעמיק את המיתון.

    <h3>הפשרות הקשות שתצטרך לבצע</h3>
    כמעט לכל פעולה יש מחיר:
    *   **העלאת ריבית:** מצילה את המטבע והאינפלציה, אבל חונקת את הצמיחה ויוצרת אבטלה.
    *   **התערבות במט"ח:** מייצבת את המטבע בטווח המיידי, אבל מרוקנת את יתרות החירום הקריטיות ואינה פותרת את הבעיות המהותיות.
    *   **פיקוח הון:** עוצר דימום הון מיידי, אבל הורס את האמון לטווח ארוך ועלול לבודד את הכלכלה.
    *   **קיצוצים תקציביים:** משפר את תמונת החוב והאמון, אבל עלול להכניס את המשק לתרדמת עמוקה יותר.

    <p>הסימולציה הזו שמה אותך בנעלי קובע המדיניות הראשי. כל חודש עליך לבחור את המהלך הטוב ביותר, לאזן בין סכנות שונות, ולקוות שתצליח לנווט את הכלכלה שלך אל מחוץ לסופה.</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --warning-color: #ffc107;
        --danger-color: #dc3545;
        --info-color: #17a2b8;
        --light-bg: #f8f9fa;
        --dark-bg: #343a40;
        --card-bg: #ffffff;
        --border-color: #dee2e6;
        --text-color: #333;
        --heading-color: #1a1a1a;
        --animation-duration: 0.5s;
    }

    #currency-crisis-app {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 800px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--light-bg);
        display: flex;
        flex-direction: column;
        gap: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        position: relative; /* Needed for overlay positioning */
    }

    .dashboard, .actions, .status {
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 20px;
        background-color: var(--card-bg);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    }

    .dashboard h2, .actions h2, .status h2 {
        margin-top: 0;
        color: var(--heading-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 10px;
        margin-bottom: 15px;
        font-size: 1.4em;
    }

    .indicators {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 15px;
    }

    .indicator {
        background-color: #e9ecef; /* Light grey/blue background */
        padding: 12px;
        border-radius: 6px;
        font-size: 1.1em;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #dee2e6;
        transition: background-color 0.3s ease;
    }
     .indicator:hover {
         background-color: #e2e6ea;
     }

    .indicator .label {
        font-weight: bold;
        color: #555;
    }
     .indicator .value {
         font-weight: bold;
         color: var(--text-color); /* Default color */
         transition: color var(--animation-duration) ease-in-out; /* Smooth color change */
     }

     /* Indicator color states */
     .indicator .value.indicator-success { color: var(--success-color); }
     .indicator .value.indicator-warning { color: var(--warning-color); }
     .indicator .value.indicator-danger { color: var(--danger-color); }
     .indicator .value.indicator-info { color: var(--info-color); } /* E.g., for month */


    .actions {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: center;
    }

    .policy-button {
        padding: 12px 20px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .policy-button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-1px);
    }
     .policy-button:active:not(:disabled) {
        transform: translateY(0);
         box-shadow: none;
     }


    .policy-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
        box-shadow: none;
    }

    .status p {
        margin: 0;
        font-size: 1.1em;
        color: var(--primary-color); /* Default status color */
        min-height: 1.2em; /* Prevent layout shift when message is empty */
        transition: color 0.3s ease;
    }
     .status p.success { color: var(--success-color); }
     .status p.warning { color: var(--warning-color); }
     .status p.danger { color: var(--danger-color); }
     .status p.info { color: var(--info-color); }


    .progress-bar-container {
        width: 100%;
        height: 6px;
        background-color: #e0e0e0;
        border-radius: 3px;
        overflow: hidden;
        margin-top: 10px;
    }

    .progress-bar {
        height: 100%;
        width: 0;
        background-color: var(--primary-color);
        animation: progress-animation 1.5s linear forwards; /* Match simulation timeout */
    }

    @keyframes progress-animation {
        from { width: 0; }
        to { width: 100%; }
    }

    #game-over-overlay {
        position: absolute; /* Changed from fixed to absolute to stay within parent div */
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.85);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.5s ease;
    }
     #game-over-overlay.visible {
         opacity: 1;
         visibility: visible;
     }


    .game-over-content {
        background-color: var(--card-bg);
        padding: 30px;
        border-radius: 8px;
        text-align: center;
        max-width: 400px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        transform: scale(0.9);
        opacity: 0;
        animation: bounceIn 0.6s ease-out forwards 0.5s; /* Delayed animation after overlay appears */
    }
    @keyframes bounceIn {
        0% { transform: scale(0.9); opacity: 0; }
        60% { transform: scale(1.05); opacity: 1; }
        80% { transform: scale(0.97); }
        100% { transform: scale(1); opacity: 1; }
    }


    #game-over-title {
        font-size: 2em;
        margin-top: 0;
        margin-bottom: 15px;
    }
     #game-over-title.win { color: var(--success-color); }
     #game-over-title.lose { color: var(--danger-color); }


    #game-over-text {
        margin-bottom: 25px;
        color: var(--text-color);
        font-size: 1.1em;
    }

    #restart-button {
         padding: 12px 25px;
        background-color: var(--success-color);
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
         transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    #restart-button:hover {
        background-color: #218838;
         transform: translateY(-1px);
    }
    #restart-button:active {
         transform: translateY(0);
         box-shadow: none;
    }


    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
         transition: background-color 0.3s ease;
    }

    #toggle-explanation:hover {
        background-color: #5a6268;
    }


    #explanation {
        max-width: 800px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--card-bg);
        direction: rtl;
        text-align: right;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        transition: max-height 0.5s ease-in-out, opacity 0.5s ease-in-out;
        overflow: hidden;
        max-height: 2000px; /* Sufficiently large for smooth transition */
        opacity: 1;
    }
     #explanation.hidden {
        max-height: 0;
        opacity: 0;
        padding-top: 0;
        padding-bottom: 0;
         border-color: transparent;
     }


    #explanation h2, #explanation h3 {
         color: var(--heading-color);
         margin-top: 15px;
         margin-bottom: 10px;
    }
     #explanation h2 { font-size: 1.5em; }
     #explanation h3 { font-size: 1.2em; color: #555;}


    #explanation ul {
        list-style: disc inside;
         padding-right: 20px;
         line-height: 1.6;
    }

     #explanation li {
        margin-bottom: 8px;
     }
      #explanation p {
          line-height: 1.6;
      }

    .hidden {
        display: none;
    }
    .visible {
        display: flex; /* Or block, depending on layout */
    }

    /* Animation for value changes */
    @keyframes pulse-success { 0% { transform: scale(1); } 50% { transform: scale(1.05); color: var(--success-color); } 100% { transform: scale(1); } }
    @keyframes pulse-danger { 0% { transform: scale(1); } 50% { transform: scale(1.05); color: var(--danger-color); } 100% { transform: scale(1); } }
    @keyframes pulse-warning { 0% { transform: scale(1); } 50% { transform: scale(1.05); color: var(--warning-color); } 100% { transform: scale(1); } }
    @keyframes pulse-info { 0% { transform: scale(1); } 50% { transform: scale(1.05); color: var(--info-color); } 100% { transform: scale(1); } }


     .indicator .value.pulse-success { animation: pulse-success var(--animation-duration) ease-out; }
     .indicator .value.pulse-danger { animation: pulse-danger var(--animation-duration) ease-out; }
     .indicator .value.pulse-warning { animation: pulse-warning var(--animation-duration) ease-out; }
     .indicator .value.pulse-info { animation: pulse-info var(--animation-duration) ease-out; }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const monthSpan = document.getElementById('current-month');
        const exchangeRateSpan = document.getElementById('exchange-rate');
        const inflationSpan = document.getElementById('inflation');
        const reservesSpan = document.getElementById('reserves');
        const interestRateSpan = document.getElementById('interest-rate');
        const gdpGrowthSpan = document.getElementById('gdp-growth');
        const statusMessage = document.getElementById('status-message');
        const policyButtons = document.querySelectorAll('.policy-button');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const gameOverOverlay = document.getElementById('game-over-overlay');
        const gameOverTitle = document.getElementById('game-over-title');
        const gameOverText = document.getElementById('game-over-text');
        const restartButton = document.getElementById('restart-button');
        const progressBarContainer = document.querySelector('.progress-bar-container');
        const progressBar = document.querySelector('.progress-bar');


        let gameState = {};
        const maxMonths = 24; // 2 years
        const simulationDelay = 1500; // milliseconds

        function initializeGame() {
            gameState = {
                month: 0, // Start at month 0, first action takes to month 1
                // Starting in a crisis state (simplified initial values)
                exchangeRate: 10.5, // Local currency per $ (high, getting worse)
                inflation: 12,   // High inflation
                reserves: 60,    // Medium reserves ($ billions)
                interestRate: 8, // Moderate interest rate
                gdpGrowth: -1.5, // Recession
                isCapitalControls: false,
                isCrisis: true, // Flag to influence dynamics
                // Effects that carry over and decay
                policyEffects: {
                    interestRateImpact: 0, // Higher value = more positive impact on ER, negative on Infl/GDP
                    fiscalCutImpact: 0, // Higher value = more positive impact on trust/ER, negative on GDP (short-term)
                    capitalControlPenalty: 0 // Higher value = more negative long-term trust penalty/GDP drag
                },
                 consecutiveStableMonths: 0 // Track stability for win condition
            };
            updateDashboard();
            statusMessage.textContent = "ברוך הבא לתפקיד הנגיד! המצב חמור. בחר את המהלך הראשון לחודש 1.";
            statusMessage.className = ''; // Reset status classes
            gameOverOverlay.classList.remove('visible'); // Use visible class for animation
             gameOverOverlay.classList.add('hidden');
            progressBarContainer.classList.add('hidden');
            enablePolicyButtons();
            gameState.month = 0; // Reset month count display logic
        }

        function updateDashboard() {
             // Store old values for animation comparison
             const oldState = {
                 exchangeRate: parseFloat(exchangeRateSpan.textContent),
                 inflation: parseFloat(inflationSpan.textContent),
                 reserves: parseFloat(reservesSpan.textContent),
                 interestRate: parseFloat(interestRateSpan.textContent),
                 gdpGrowth: parseFloat(gdpGrowthSpan.textContent)
             };


            monthSpan.textContent = gameState.month;
            exchangeRateSpan.textContent = gameState.exchangeRate.toFixed(2);
            inflationSpan.textContent = gameState.inflation.toFixed(1);
            reservesSpan.textContent = gameState.reserves.toFixed(1);
            interestRateSpan.textContent = gameState.interestRate.toFixed(1);
            gdpGrowthSpan.textContent = gameState.gdpGrowth.toFixed(1);


             // Add animation class if value changed significantly
             const indicatorsToAnimate = [
                 { span: exchangeRateSpan, newValue: gameState.exchangeRate, oldValue: oldState.exchangeRate, reverse: true }, // Lower is better
                 { span: inflationSpan, newValue: gameState.inflation, oldValue: oldState.inflation, reverse: true }, // Lower is better
                 { span: reservesSpan, newValue: gameState.reserves, oldValue: oldState.reserves }, // Higher is better
                 { span: interestRateSpan, newValue: gameState.interestRate, oldValue: oldState.interestRate, neutral: true }, // Neutral change animation
                 { span: gdpGrowthSpan, newValue: gameState.gdpGrowth, oldValue: oldState.gdpGrowth } // Higher is better
             ];

            indicatorsToAnimate.forEach(({ span, newValue, oldValue, reverse, neutral }) => {
                 span.classList.remove('pulse-success', 'pulse-warning', 'pulse-danger', 'pulse-info'); // Reset animations
                 // Use a threshold for animation to avoid constant minor pulses
                 const changeThreshold = neutral ? 0.5 : (span === reservesSpan ? 2 : 0.3); // Different threshold for each indicator
                 if (Math.abs(newValue - oldValue) > changeThreshold) {
                     let animationClass = 'pulse-info'; // Default for neutral/month

                     if (!neutral) {
                          if ((newValue > oldValue && !reverse) || (newValue < oldValue && reverse)) {
                             animationClass = 'pulse-success';
                          } else {
                              animationClass = 'pulse-danger';
                          }
                     }
                     span.classList.add(animationClass);
                     // Remove animation class after it finishes
                     setTimeout(() => { span.classList.remove(animationClass); }, simulationDelay);
                 }
            });


            // Update color coding based on current values
            exchangeRateSpan.className = 'value ' + (gameState.exchangeRate > 13 ? 'indicator-danger' : (gameState.exchangeRate < 9 ? 'indicator-success' : 'indicator-warning'));
            inflationSpan.className = 'value ' + (gameState.inflation > 10 ? 'indicator-danger' : (gameState.inflation < 4 ? 'indicator-success' : 'indicator-warning'));
            reservesSpan.className = 'value ' + (gameState.reserves < 25 ? 'indicator-danger' : (gameState.reserves > 70 ? 'indicator-success' : 'indicator-warning'));
            interestRateSpan.className = 'value ' + (gameState.interestRate > 15 ? 'indicator-warning' : (gameState.interestRate < 5 ? 'indicator-warning' : 'indicator-success')); // High/low rates have trade-offs - use success for "normal" range
            gdpGrowthSpan.className = 'value ' + (gameState.gdpGrowth < 0 ? 'indicator-danger' : (gameState.gdpGrowth > 3 ? 'indicator-success' : 'indicator-warning'));

             monthSpan.className = 'value indicator-info'; // Month is just info
        }

        function applyPolicy(policy) {
            let message = "המדיניות לחודש " + (gameState.month + 1) + ": ";
            let policyApplied = true;

            // Reset short-term effects from previous turn's *specific* policy
            // (Carry-over effects handled in simulateNextTurn)

            switch (policy) {
                case 'raise-rate':
                    const rateIncrease = gameState.isCrisis ? 2 + Math.random() * 2 : 1 + Math.random(); // Bigger hikes in crisis
                    gameState.interestRate += rateIncrease;
                    // Add carry-over effect (stronger impact initially)
                     gameState.policyEffects.interestRateImpact += rateIncrease * (gameState.isCrisis ? 0.2 : 0.1);
                    message += `העלאת הריבית ב-${rateIncrease.toFixed(1)} נקודות אחוז. זהו צעד אגרסיבי!`;
                    break;
                case 'lower-rate':
                     const rateDecrease = gameState.interestRate > 2 ? (gameState.isCrisis ? 0.5 + Math.random() : 1 + Math.random()) : 0;
                     if (rateDecrease > 0) {
                        gameState.interestRate = Math.max(1, gameState.interestRate - rateDecrease);
                         // Reduce carry-over effect
                         gameState.policyEffects.interestRateImpact = Math.max(-2, gameState.policyEffects.interestRateImpact - rateDecrease * 0.1); // Can become negative
                        message += `הורדת הריבית ב-${rateDecrease.toFixed(1)} נקודות אחוז. מנסים לעודד צמיחה?`;
                     } else {
                         message = "לא ניתן להוריד את הריבית יותר, היא כבר נמוכה מאוד.";
                         policyApplied = false; // No policy applied
                     }
                    break;
                case 'intervene-buy': // Buy local currency, sell dollars
                    const interventionAmount = gameState.isCrisis ? 10 + Math.random() * 5 : 5 + Math.random() * 3; // Bigger intervention in crisis
                    if (gameState.reserves >= interventionAmount) {
                        gameState.reserves -= interventionAmount;
                        // Immediate effect on currency (stronger) - temporary boost
                        gameState.exchangeRate = Math.max(1, gameState.exchangeRate * (1 - interventionAmount * 0.003));
                        // Small, short-lived carry-over positive impact on ER
                        gameState.policyEffects.interestRateImpact += interventionAmount * 0.03;
                        message += `התערבות מסיבית בשוק המט"ח: קניית מטבע מקומי בהיקף של ${interventionAmount.toFixed(1)} מיליארד $. יתרות המט"ח ירדו.`;
                    } else {
                        message = `אין מספיק יתרות מט"ח (${gameState.reserves.toFixed(1)} מיליארד $) כדי לבצע התערבות משמעותית בהיקף כזה. המהלך נכשל!`;
                        // Add penalty for trying to intervene without reserves? Shows weakness.
                        gameState.exchangeRate *= 1.02; // Small penalty
                        policyApplied = false;
                    }
                    break;
                 case 'intervene-sell': // Sell local currency, buy dollars (usually not during crisis)
                    message = "מכירת מטבע מקומי אינה רלוונטית ואף מזיקה במהלך משבר מטבע קשה.";
                    policyApplied = false;
                    break; // No action in crisis sim
                case 'capital-controls':
                    if (!gameState.isCapitalControls) {
                        gameState.isCapitalControls = true;
                        // Immediate effect: stop capital outflow, strengthen currency significantly initially
                        gameState.exchangeRate = Math.max(1, gameState.exchangeRate * 0.8); // Significant immediate strengthening
                         // Reduces immediate pressure on reserves temporarily
                        gameState.reserves += 8; // Small temporary gain or reduced outflow
                        // Add long-term penalty: lower investor confidence, hurts future growth potential
                        gameState.policyEffects.capitalControlPenalty += 0.8; // Permanent or semi-permanent drag on growth/trust
                        message += "הוטל פיקוח הון הדוק. תנועת ההון מוגבלת! זה יעצור את הדימום המיידי, אך יפגע באמון ארוך טווח.";
                    } else {
                        message = "פיקוח הון כבר מוטל. אין שינוי נוסף כרגע.";
                        policyApplied = false;
                    }
                    break;
                case 'fiscal-cuts':
                    const cutImpact = gameState.isCrisis ? 1.8 + Math.random() : 0.7 + Math.random(); // Bigger cuts possible in crisis
                    // Immediate effect: hurts growth, but can improve trust/debt perception
                    gameState.gdpGrowth -= cutImpact * 0.8;
                    gameState.inflation -= cutImpact * 0.05; // Indirect effect
                    // Add carry-over effect for trust/debt perception (delayed positive for ER/GDP potential)
                     gameState.policyEffects.fiscalCutImpact += cutImpact * 0.15;
                    message += `בוצעו קיצוצים תקציביים נרחבים. זה יכאב לצמיחה בטווח הקצר, אך יאותת לשווקים על רצינות.`;
                    break;
                default:
                    message = "פעולה לא ידועה.";
                    policyApplied = false;
                    break;
            }

            statusMessage.textContent = message;
            statusMessage.className = ''; // Remove old status classes
             if (policyApplied) {
                 statusMessage.classList.add('info'); // Use 'info' for successful policy
                 disablePolicyButtons(); // Disable buttons until next turn simulation is done
                 progressBarContainer.classList.remove('hidden');
                 progressBar.style.width = '0%'; // Reset progress bar
                 progressBar.style.animation = 'none'; // Remove old animation
                 // Force reflow to restart animation
                 void progressBar.offsetWidth;
                 progressBar.style.animation = `progress-animation ${simulationDelay / 1000}s linear forwards`;

                 setTimeout(simulateNextTurn, simulationDelay); // Simulate time passing
             } else {
                 statusMessage.classList.add('warning'); // Use 'warning' for failed/non-applied policy
                 // Re-enable buttons immediately if policy didn't apply
                 enablePolicyButtons();
             }
        }

        function simulateNextTurn() {
            gameState.month++;

             progressBarContainer.classList.add('hidden'); // Hide progress bar after simulation

            let monthUpdateMessage = `**עדכון לחודש ${gameState.month}:** `;
            let exchangeRateChange = 0;
            let inflationChange = 0;
            let reservesChange = 0;
            let gdpChange = 0;
            // Interest rate changes only directly from policy

            // --- Apply Carry-over Effects (decaying over time) ---
            // Interest rate impact: Higher rates support currency/lower inflation, hurt growth
            exchangeRateChange += gameState.policyEffects.interestRateImpact * 0.7; // Strong positive for ER
            inflationChange -= gameState.policyEffects.interestRateImpact * 0.4; // Negative for Inflation
            gdpChange -= gameState.policyEffects.interestRateImpact * 0.1; // Negative for GDP
            gameState.policyEffects.interestRateImpact *= 0.75; // Decay effect

            // Fiscal cuts impact: Improves trust (supports currency, long-term GDP potential), hurts short-term GDP
            exchangeRateChange += gameState.policyEffects.fiscalCutImpact * 0.5; // Positive for ER (trust)
            gdpChange += gameState.policyEffects.fiscalCutImpact * 0.2; // Positive for GDP (delayed potential)
             gdpChange -= gameState.policyEffects.fiscalCutImpact * 0.1; // Short-term pain from cuts
            gameState.policyEffects.fiscalCutImpact *= 0.8; // Decay effect

             // Capital controls penalty: long-term drag on growth and trust
             gdpChange -= gameState.policyEffects.capitalControlPenalty * 0.3;
             exchangeRateChange -= gameState.policyEffects.capitalControlPenalty * 0.2; // Long-term negative for currency (due to lack of trust)
             gameState.policyEffects.capitalControlPenalty *= 0.97; // Very slow decay


            // --- Apply Base Crisis Dynamics (if still in crisis) ---
            // Default: currency keeps weakening, inflation rises, growth is negative, reserves are under pressure
            if (gameState.isCrisis) {
                 // Crisis momentum factors
                 const crisisER_pressure = (gameState.exchangeRate - 8) * 0.3 + Math.random() * 1.5; // More pressure as ER weakens
                 const crisisInflation_pressure = (gameState.inflation - 5) * 0.2 + Math.random() * 0.8; // More pressure as inflation rises
                 const crisisGDP_pressure = (0 - gameState.gdpGrowth) * 0.3 + Math.random() * 0.4; // More pressure if recession deepens
                 const crisisReserves_drain = (gameState.exchangeRate / 10) * 2 + Math.random() * 4; // Reserves drain faster as ER weakens

                 exchangeRateChange -= crisisER_pressure * (gameState.isCapitalControls ? 0.5 : 1); // Capital controls reduce pressure
                 inflationChange += crisisInflation_pressure;
                 gdpChange -= crisisGDP_pressure;
                 reservesChange -= crisisReserves_drain * (gameState.isCapitalControls ? 0.5 : 1); // Capital controls reduce drain

                 monthUpdateMessage += `המשבר ממשיך ללחוץ.`;

            } else {
                 // If crisis is over or stabilizing, mild positive/negative drift
                 exchangeRateChange += (Math.random() - 0.4) * 0.4; // Tendency to appreciate slightly
                 inflationChange += (Math.random() - 0.6) * 0.2; // Tendency for inflation to normalize/undershoot
                 gdpChange += (Math.random() - 0.2) * 0.5; // Tendency towards positive growth
                 reservesChange += (Math.random() - 0.3) * 2; // Tendency towards reserves build-up
                 monthUpdateMessage += `המצב מתייצב, יש סימני התאוששות קלה.`;
            }

             // --- Add Random Events ---
            const event = Math.random();
            if (event < 0.1) { // Bad event
                const badEvent = Math.floor(Math.random() * 3);
                if (badEvent === 0) { monthUpdateMessage += "📉 חדשות רעות: ירידה חדה במחירי סחורות ייצוא מרכזיות. "; exchangeRateChange -= 1.8; gdpChange -= 0.8; reservesChange -= 3;}
                else if (badEvent === 1) { monthUpdateMessage += "🚨 חדשות רעות: סוכנות דירוג בינלאומית הורידה את דירוג האשראי של המדינה. "; exchangeRateChange -= 2.5; reservesChange -= 6; }
                else { monthUpdateMessage += "🔥 חדשות רעות: פרץ של אי שקט פוליטי או משבר ביטחוני מחריף את הפאניקה. "; exchangeRateChange -= 3; reservesChange -= 8; gdpChange -= 0.7;}
            } else if (event > 0.9) { // Good event
                 const goodEvent = Math.floor(Math.random() * 3);
                if (goodEvent === 0) { monthUpdateMessage += "📈 חדשות טובות: עלייה מפתיעה במחירי סחורות עולמיים מועילים לנו. "; exchangeRateChange += 1.5; gdpChange += 0.6; reservesChange += 2; }
                else if (goodEvent === 1) { monthUpdateMessage += "🤝 חדשות טובות: קרן המטבע הבינלאומית או מדינה ידידותית מביעות תמיכה פומבית. "; exchangeRateChange += 2; reservesChange += 12; }
                else { monthUpdateMessage += "✅ חדשות טובות: רפורמה מבנית קריטית אושרה בפרלמנט. "; exchangeRateChange += 1.8; gdpChange += 0.9; }
            } // No significant event case handled in base message

            // --- Apply Updates and Cap/Floor Values ---
            gameState.exchangeRate = Math.max(4, gameState.exchangeRate + exchangeRateChange); // ER can't go below a realistic floor
            gameState.inflation = Math.max(-3, gameState.inflation + inflationChange);
            gameState.reserves = gameState.reserves + reservesChange;
             gameState.gdpGrowth = gameState.gdpGrowth + gdpChange;
             // Interest rate was changed directly by policy

             // --- Check Crisis Status and End Game Conditions ---

            // Check if crisis is potentially over or under control
            const isCurrentlyStable = gameState.exchangeRate < 11 && gameState.inflation < 7 && gameState.reserves > 40 && gameState.gdpGrowth > 0.5;

            if (isCurrentlyStable) {
                 gameState.consecutiveStableMonths++;
                 if (gameState.consecutiveStableMonths >= 3) { // Need a few months of stability
                     gameState.isCrisis = false; // Exit crisis mode formally
                      monthUpdateMessage += " הכלכלה נכנסה למסלול התאוששות ויציבות!";
                 } else {
                     monthUpdateMessage += " יש סימנים חזקים להתייצבות!";
                 }
            } else {
                 gameState.consecutiveStableMonths = 0; // Reset counter if conditions aren't met
                 // Re-enter crisis mode if indicators are bad again, even if briefly stable before
                 if (gameState.exchangeRate > 14 || gameState.inflation > 18 || gameState.reserves < 15 || gameState.gdpGrowth < -2) {
                      gameState.isCrisis = true;
                      monthUpdateMessage += " המצב עדיין שברירי.";
                 }
            }


            if (gameState.reserves <= 0) {
                endGame(false, `חודש ${gameState.month}: יתרות מט"ח אזלו (${gameState.reserves.toFixed(1)}$ מיליארד)! המדינה אינה יכולה לעמוד בהתחייבויותיה החיצוניות. חדלות פירעון, קריסת המטבע והיפר-אינפלציה משתוללת.`);
                return;
            }
             if (gameState.exchangeRate > 25 && gameState.inflation > 30) {
                 endGame(false, `חודש ${gameState.month}: שער החליפין (${gameState.exchangeRate.toFixed(2)}) והאינפלציה (${gameState.inflation.toFixed(1)}%) יצאו מכלל שליטה מוחלטת. השוק איבד אמון לחלוטין. היפר-אינפלציה וקריסה כלכלית.`);
                 return;
             }
            if (gameState.month >= maxMonths) {
                // End game after max months, check final state
                if (gameState.exchangeRate < 11 && gameState.inflation < 7 && gameState.reserves > 40 && gameState.gdpGrowth > 0.5) {
                     endGame(true, `ניצחון! אחרי ${maxMonths} חודשים של קבלת החלטות קשות, הצלחת לייצב את הכלכלה ולהחזיר אותה למסלול צמיחה בר קיימא. שער החליפין בשליטה, האינפלציה נמוכה, יתרות המט"ח מספקות והמשק צומח.`);
                } else if (gameState.exchangeRate < 15 && gameState.inflation < 15 && gameState.reserves > 20) {
                     endGame(true, `הישרדות! אחרי ${maxMonths} חודשים, הצלחת למנוע קריסה מוחלטת ולהשיג יציבות שברירית. המצב עדיין מאתגר (${gameState.exchangeRate.toFixed(2)}$, ${gameState.inflation.toFixed(1)}%, ${gameState.reserves.toFixed(1)}$ מיליארד, ${gameState.gdpGrowth.toFixed(1)}% צמיחה), אבל המדינה שרדה את הסערה הגדולה ביותר.`);
                }
                else {
                     endGame(false, `כישלון. חלפו ${maxMonths} חודשים ולא הצלחת לייצב את הכלכלה באופן משמעותי. המצב בסוף התקופה: שער חליפין ${gameState.exchangeRate.toFixed(2)}, אינפלציה ${gameState.inflation.toFixed(1)}%, יתרות ${gameState.reserves.toFixed(1)}$ מיליארד, צמיחה ${gameState.gdpGrowth.toFixed(1)}%. המשבר עדיין כאן.`);
                }
                 return; // Stop simulation after max months
            }


            statusMessage.textContent = monthUpdateMessage + " בחר פעולה לחודש הבא (" + (maxMonths - gameState.month) + " חודשים נותרו).";
             statusMessage.className = ''; // Reset class
             if (isCurrentlyStable && gameState.consecutiveStableMonths >=3 ) {
                  statusMessage.classList.add('success');
             } else if (gameState.isCrisis) {
                  statusMessage.classList.add('danger');
             } else {
                  statusMessage.classList.add('warning'); // Maybe stabilizing but not fully out
             }


            updateDashboard();
            enablePolicyButtons(); // Re-enable buttons for the next turn
        }

         function enablePolicyButtons() {
             policyButtons.forEach(button => {
                 // Basic logic for enabling/disabling based on state
                 if (button.dataset.policy === 'lower-rate' && gameState.interestRate <= 1.5) { // Don't go below 1.5%
                     button.disabled = true;
                 } else if (button.dataset.policy === 'intervene-buy' && gameState.reserves < 10) { // Need some minimum reserves to attempt
                      button.disabled = true;
                 } else if (button.dataset.policy === 'intervene-sell') { // Never allow this in a crisis sim
                     button.disabled = true;
                 }
                 else {
                    button.disabled = false;
                 }
             });
         }

        function disablePolicyButtons() {
             policyButtons.forEach(button => {
                 button.disabled = true;
             });
        }


        function endGame(isWin, message) {
            disablePolicyButtons();
             gameOverOverlay.classList.remove('hidden');
            gameOverOverlay.classList.add('visible'); // Use visible for animation trigger
            gameOverTitle.textContent = isWin ? "ניצחון!" : "הפסד!";
             gameOverTitle.className = isWin ? 'win' : 'lose'; // Add win/lose class for color
            gameOverText.textContent = message;
        }


        // Event Listeners
        policyButtons.forEach(button => {
            button.addEventListener('click', () => {
                if (!button.disabled) {
                     applyPolicy(button.dataset.policy);
                }
            });
        });

        toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
             // Change button text based on state
             if(explanationDiv.classList.contains('hidden')) {
                 toggleExplanationButton.textContent = '📚 הצג מדריך למשבר';
             } else {
                 toggleExplanationButton.textContent = '📖 הסתר מדריך למשבר';
             }
        });

        restartButton.addEventListener('click', initializeGame);

        // Initial game start
        initializeGame();
    });
</script>
---
```