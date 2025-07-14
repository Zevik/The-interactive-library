---
title: "נמלים בעבודה: סימולציית מושבת נמלים"
english_slug: ants-at-work-ant-colony-simulation
category: "מדעי החיים / ביולוגיה"
tags:
  - נמלים
  - מושבה
  - ניהול משאבים
  - אקולוגיה
  - התנהגות חברתית
---
# נמלים בעבודה: סימולציית מושבת נמלים

האם תהית אי פעם כמה מורכב הוא עולמה התוסס והמושלם של מושבת נמלים? מאחורי הארגון המופתי שלהן מסתתרות משימות קריטיות להישרדות: איסוף מזון בלתי פוסק, טיפול מסור במלכה המייסדת, והגנה אמיצה מפני סכנות האורבות בחוץ. האם יש לך את מה שצריך כדי להבטיח את שגשוג מושבת הנמלים שלך?

<div id="simulation-container">
    <div id="game-area">
        <div id="nest-view" class="game-section">
            <h4><i class="icon">🏠</i> קן הנמלים</h4>
            <div class="status-item">
                <label><i class="icon">👑</i> מלכה:</label>
                <span id="queen-status" class="status-value">טובה</span>
                <div class="status-bar-container"><div id="queen-health-bar" class="status-bar"></div></div>
            </div>
            <div class="status-item">
                <label><i class="icon">🍔</i> מזון:</label>
                <span id="food-level" class="status-value">100</span>
                 <div class="status-bar-container"><div id="food-bar" class="status-bar"></div></div>
            </div>
            <div class="status-item">
                 <label><i class="icon">🐜</i> אוכלוסייה:</label>
                 <span id="population-size" class="status-value">10</span>
             </div>
             <div id="ant-hatch-progress" class="progress-bar-container" style="display: none;">
                 <label><i class="icon">🥚</i> ביצה:</label>
                 <div class="progress-bar-fill"></div>
             </div>
        </div>
        <div id="outside-view" class="game-section">
            <h4><i class="icon">🌳</i> סביבה חיצונית</h4>
             <div class="status-item">
                <label><i class="icon">🚨</i> איומים:</label>
                <span id="threat-status" class="status-value">אין</span>
                 <div id="threat-timer" class="timer" style="display: none;">זמן: <span class="timer-value"></span></div>
            </div>
            <div class="status-item">
                <label><i class="icon">🍁</i> משאבים בחוץ:</label>
                <span id="external-resources" class="status-value">יש</span>
                <div id="resource-timer" class="timer" style="display: none;">זמן: <span class="timer-value"></span></div>
            </div>
        </div>
    </div>
    <div id="control-panel" class="game-section">
        <h4><i class="icon">🛠️</i> ניהול המושבה</h4>
        <p class="description">הקצה נמלים למשימות השונות. סה"כ נמלים: <span id="available-ants-count">10</span></p>
        <div class="task-assignment">
            <label for="gather-ants"><i class="icon">🧺</i> איסוף מזון:</label>
            <input type="number" id="gather-ants" value="5" min="0">
            <span class="assigned-ants-indicator">(<span class="current-assigned">5</span> הוקצו)</span>
        </div>
        <div class="task-assignment">
            <label for="feed-ants"><i class="icon">💖</i> טיפול במלכה:</label>
            <input type="number" id="feed-ants" value="3" min="0">
             <span class="assigned-ants-indicator">(<span class="current-assigned">3</span> הוקצו)</span>
        </div>
        <div class="task-assignment">
            <label for="defend-ants"><i class="icon">🛡️</i> הגנה:</label>
            <input type="number" id="defend-ants" value="2" min="0">
             <span class="assigned-ants-indicator">(<span class="current-assigned">2</span> הוקצו)</span>
        </div>
        <div id="assignment-feedback" class="feedback-message"></div>
    </div>
    <div id="game-status" class="game-section">
        <h4><i class="icon">📊</i> סטטוס המושבה:</h4>
        <p id="status-message" class="message success">המושבה שגשגה עד כה!</p>
        <button id="restart-button" class="game-button">התחל מחדש</button>
    </div>
</div>

<style>
    /* Fonts - Using system fonts or common web fonts for simplicity within constraints */
    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #f0f0e0; /* Light earthy background */
        color: #333;
        line-height: 1.6;
    }

    #simulation-container {
        border: 2px solid #a0522d; /* Earthy brown border */
        padding: 25px;
        border-radius: 15px; /* More rounded corners */
        max-width: 750px; /* Slightly wider */
        margin: 30px auto;
        background-color: #fdfce0; /* Lighter inner background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2); /* Deeper shadow */
        position: relative; /* For potential absolute positioning of elements later */
        overflow: hidden; /* Keep elements within bounds */
    }

    .game-section {
        background-color: #fff;
        border: 1px solid #d2b48c; /* Tan border */
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #game-area {
        display: flex;
        justify-content: space-between; /* Spread out nest and outside views */
        gap: 20px; /* Space between the two views */
        margin-bottom: 25px;
    }

    #nest-view, #outside-view {
        flex: 1; /* Allow both to grow and take equal space */
         min-width: 0; /* Prevent flex item from overflowing */
         background-color: #e9f5e9; /* Very light green for nest */
         border-color: #8fbc8f; /* Darker green border */
    }

     #outside-view {
         background-color: #e0f2f7; /* Very light blue for outside */
         border-color: #87cefa; /* Lighter blue border */
     }

    h4 {
        margin-top: 0;
        color: #5a3c2a; /* Dark earthy color for headers */
        border-bottom: 1px solid #d2b48c;
        padding-bottom: 10px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
    }

    h4 .icon {
         margin-left: 8px;
         font-size: 1.2em;
    }


    .status-item {
        margin-bottom: 15px;
        display: flex; /* Use flexbox for layout within status item */
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 8px; /* Space between label, value, and bar */
    }

    .status-item label {
        font-weight: bold;
        color: #5a3c2a;
        display: flex;
        align-items: center;
        gap: 5px;
    }

     .status-value {
         font-weight: normal; /* Status value doesn't need to be bold */
         min-width: 30px; /* Ensure space for values */
         text-align: left;
     }

    .icon {
         font-size: 1.1em;
    }

    .status-bar-container, .progress-bar-container {
        flex-grow: 1; /* Bar takes available space */
        height: 15px;
        background-color: #eee;
        border-radius: 8px;
        overflow: hidden; /* Hide overflow from the fill */
        border: 1px solid #ccc;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    .status-bar, .progress-bar-fill {
        height: 100%;
        width: 100%; /* Default width */
        background-color: #4CAF50; /* Default: Green */
        transition: width 0.5s ease-in-out, background-color 0.5s ease-in-out; /* Smooth transitions */
    }

    /* Status Bar Colors */
    #food-bar { background-color: #ffcc00; } /* Yellow for food */
    #food-bar.low { background-color: #ff9900; } /* Orange for low food */
    #food-bar.critical { background-color: #ff0000; } /* Red for critical food */

    #queen-health-bar { background-color: #e57373; } /* Light red/pink for health */
    #queen-health-bar.good { background-color: #81c784; } /* Green for good health */
    #queen-health-bar.excellent { background-color: #4caf50; } /* Darker green for excellent health */


     .timer {
         font-size: 0.9em;
         color: #555;
         margin-right: 10px;
     }

     #threat-timer { color: #d32f2f; } /* Red for threat timer */
     #resource-timer { color: #388e3c; } /* Green for resource timer */


    #control-panel .description {
        font-size: 0.95em;
        color: #555;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px dashed #ccc;
    }

    .task-assignment {
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 15px; /* Space between label, input, and indicator */
    }

    .task-assignment label {
        flex-basis: 140px; /* Fixed width for labels */
        min-width: 100px; /* Minimum width */
        font-weight: bold;
        color: #5a3c2a;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .task-assignment input[type="number"] {
        width: 60px;
        padding: 8px;
        border: 1px solid #d2b48c;
        border-radius: 5px;
        font-size: 1em;
        text-align: center;
        background-color: #fffaf0; /* Very light tan */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

     .task-assignment input[type="number"]:focus {
         outline: none;
         border-color: #a0522d;
         box-shadow: 0 0 5px rgba(160, 82, 45, 0.5);
     }

    .assigned-ants-indicator {
         font-size: 0.9em;
         color: #555;
         min-width: 80px; /* Reserve space */
     }

    #assignment-feedback {
        min-height: 1.5em; /* Reserve space */
        color: #d32f2f; /* Default for errors/warnings */
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }
     #assignment-feedback.success { color: #388e3c; }
     #assignment-feedback.warning { color: #f57c00; }


    #game-status {
        text-align: center;
        background-color: #fff9c4; /* Light yellow */
        border-color: #fbc02d; /* Darker yellow */
    }

    #status-message {
        font-size: 1.1em;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space */
        margin-bottom: 15px;
    }

    #status-message.success { color: #388e3c; } /* Green */
    #status-message.warning { color: #f57c00; } /* Orange */
    #status-message.danger { color: #d32f2f; } /* Red */
     #status-message.info { color: #1976d2; } /* Blue */


    .game-button {
        padding: 10px 20px;
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .game-button:hover {
        background-color: #45a049;
    }
     .game-button:active {
         transform: scale(0.98);
     }

    #restart-button {
         display: none; /* Hidden initially */
         background-color: #d32f2f; /* Red */
         margin-top: 15px;
    }
     #restart-button:hover {
         background-color: #c62828;
     }


    #toggle-explanation {
        display: block;
        margin: 25px auto;
        padding: 12px 25px;
        background-color: #1976d2; /* Blue */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.05em;
         transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #toggle-explanation:hover {
        background-color: #1565c0;
    }
     #toggle-explanation:active {
         transform: scale(0.98);
     }


    #explanation {
        border: 2px solid #1565c0; /* Darker blue border */
        padding: 25px;
        margin-top: 25px;
        border-radius: 10px;
        background-color: #e3f2fd; /* Very light blue background */
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
    }

    #explanation h2, #explanation h3 {
        color: #0d47a1; /* Dark blue */
        margin-bottom: 10px;
    }
     #explanation h3 { margin-top: 20px; }

    #explanation p {
        margin-bottom: 15px;
        color: #333;
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px;
        margin-bottom: 15px;
        color: #333;
    }
     #explanation ul li {
         margin-bottom: 8px;
     }


    /* Animations */
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }

     #outside-view.under-threat {
         animation: shake 0.5s ease-in-out infinite;
         border-color: #d32f2f;
     }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }

    #food-level.warning, #queen-status.warning {
        animation: pulse 1.5s infinite;
    }
    #food-level.critical, #queen-status.critical {
        animation: pulse 1s infinite;
        color: red !important; /* Ensure red color during critical pulse */
    }

     /* Disable spin buttons on number inputs */
     input[type="number"]::-webkit-outer-spin-button,
     input[type="number"]::-webkit-inner-spin-button {
         -webkit-appearance: none;
         margin: 0;
     }
     input[type="number"] {
         -moz-appearance: textfield;
     }

</style>

<button id="toggle-explanation">הצג הסבר על עולמות הנמלים</button>

<div id="explanation" style="display: none;">
    <h2><i class="icon">🧠</i> הצצה אל מוח המושבה: הסבר מורחב</h2>

    <p>מושבת נמלים היא סופר-אורגניזם מרתק, שבו כל נמלה היא חלק קטן ומוקדש למטרה הגדולה יותר: הישרדות ושגשוג המושבה כולה. המורכבות נובעת לא מפקוד מרכזי, אלא מאינטראקציות פשוטות והתמחויות תפקידים, יצירת מערכת עמידה ויעילה להפליא.</p>

    <h3><i class="icon">🏗️</i> מבנה חברתי ותפקידים</h3>
    <p>המושבה מחולקת למעמדות קבועים:</p>
    <ul>
        <li><strong>המלכה (<i class="icon">👑</i>):</strong> היא האם המייסדת. תפקידה הבלעדי הוא הטלת ביצים והבטחת הדור הבא. בריאותה חיונית לקיום המושבה כולה.</li>
        <li><strong>הפועלות (<i class="icon">🐜</i>):</strong> הרוב המכריע. כולן נקבות, אך הן עקרות. הן מבצעות את כל עבודות התחזוקה, האיסוף, הטיפול וההגנה. פועלות צעירות נוטות לעבוד בתוך הקן (טיפול במלכה, בלרוות, ניקיון), בעוד מבוגרות יותר יוצאות החוצה (איסוף מזון, הגנה).</li>
        <li><strong>החיילות (<i class="icon">🛡️</i>):</strong> תת-קבוצה מיוחדת (לא בכל המינים). גדולות וחזקות יותר, מוקדשות בעיקר להגנה מפני איומים גדולים ולאבטחת נתיבי מזון.</li>
         <li><strong>זכרים (<i class="icon">♂️</i>) ומלכות חדשות (<i class="icon"> fledgling 👑</i>):</strong> מיוצרים רק בתנאים אופטימליים, לרוב בעונה מסוימת, ויוצאים מהקן לטיסת כלולות כדי להקים מושבות חדשות. הסימולציה מתמקדת בהישרדות המושבה הקיימת ולא בהקמת חדשות.</li>
    </ul>

    <h3><i class="icon">🍎</i> כלכלת המושבה: ניהול משאבים</h3>
    <p>מזון הוא הדלק של המושבה. פועלות "אספניות" (<i class="icon">🧺</i>) יוצאות לחפש מקורות מזון - זרעים, חרקים מתים, פטריות ועוד - ומביאות אותם חזרה לקן. המזון נאגר ומחולק בין כל חברי המושבה דרך תהליך מורכב של טרופאלקסיס (העברת מזון מפה לפה). מאגר מזון גדול מבטיח עמידות בתקופות מחסור ומאפשר גדילת אוכלוסייה. פועלות "מטפלות" (<i class="icon">💖</i>) דואגות במיוחד להזין את המלכה, שהיא המקור לכל הנמלים החדשות.</p>

    <h3><i class="icon">⚔️</i> הישרדות בסביבה עוינת: הגנה</h3>
    <p>העולם שמחוץ לקן מלא סכנות: טורפים (עכבישים, ציפורים, לטאות), מושבות נמלים יריבות, טפילים ומחלות. נמלים "מגינות" (<i class="icon">🛡️</i>) נשארות בפתחי הקן או סביבו כדי להתריע או להילחם בפולשים. הקצאת מספיק נמלים להגנה חיונית לשלום המושבה, במיוחד כשיש איום חיצוני.</p>

    <h3><i class="icon">⚖️</i> אמנות האיזון: הקצאת תפקידים</h3>
    <p>האתגר בניהול מושבת נמלים הוא להקצות נכון את הפועלות למשימות השונות בהתאם לצרכים המשתנים. יותר מדי פועלות באיסוף? המלכה עלולה לגווע ברעב או שההגנה תיכשל. יותר מדי פועלות בהגנה? לא יהיה מספיק מזון להאכיל את המושבה הגדלה. איזון נכון מוביל לשגשוג. תמותה באוכלוסייה משפיעה מיידית על כוח העבודה הזמין!</p>

    <h3><i class="icon">✨</i> אינטליגנציה קולקטיבית</h3>
    <p>הדבר המדהים ביותר הוא שכל הפעילות הזו אינה מתוכננת על ידי נמלה אחת. היא נובעת מכללים פשוטים שכל נמלה פועלת לפיהם ותקשורת באמצעות פרומונים. הריח של מזון מושך נמלים, ריח של סכנה גורם להתרחקות או לתגובת הגנה. הסימולציה מאפשרת לך לחוות באופן מופשט את התפקיד של "המוח הקולקטיבי" הזה, ולהבין כיצד שינויים קטנים בהקצאת כוח העבודה יכולים להשפיע באופן דרמטי על גורל המושבה כולה.</p>
</div>

<script>
    const populationSizeEl = document.getElementById('population-size');
    const availableAntsCountEl = document.getElementById('available-ants-count');
    const foodLevelEl = document.getElementById('food-level');
    const queenStatusEl = document.getElementById('queen-status');
    const threatStatusEl = document.getElementById('threat-status');
    const externalResourcesEl = document.getElementById('external-resources');
    const gatherAntsInput = document.getElementById('gather-ants');
    const feedAntsInput = document.getElementById('feed-ants');
    const defendAntsInput = document.getElementById('defend-ants');
    const assignedAntsIndicators = document.querySelectorAll('.assigned-ants-indicator .current-assigned');
    const assignmentFeedbackEl = document.getElementById('assignment-feedback');
    const statusMessageEl = document.getElementById('status-message');
    const restartButton = document.getElementById('restart-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const foodBarEl = document.getElementById('food-bar');
    const queenHealthBarEl = document.getElementById('queen-health-bar');
    const outsideViewEl = document.getElementById('outside-view');
    const threatTimerEl = document.getElementById('threat-timer');
    const threatTimerValueEl = threatTimerEl.querySelector('.timer-value');
    const resourceTimerEl = document.getElementById('resource-timer');
    const resourceTimerValueEl = resourceTimerEl.querySelector('.timer-value');
    const antHatchProgressEl = document.getElementById('ant-hatch-progress');
    const antHatchProgressBarFillEl = antHatchProgressEl.querySelector('.progress-bar-fill');


    let gameState = {};
    let gameInterval;
    let eggProgress = 0; // Progress towards the next egg hatching

    const config = {
        initialPopulation: 20, // Start with a slightly larger population
        initialFood: 150, // More initial food
        initialQueenHealth: 100,
        foodGatherRate: 1.5, // Food gained per gathering ant per tick (increased)
        foodConsumptionRate: 0.4, // Food consumed per ant per tick (slightly less)
        queenHealthDecayRate: 0.7, // Queen health lost per tick
        queenHealthGainRate: 3, // Queen health gained per feeding ant per tick (increased)
        eggProgressPerTick: 1, // Base progress towards egg per tick
        eggProgressNeeded: 100, // How much progress for one egg
        eggProgressFromQueenHealth: 1, // Bonus progress based on health (per 10 health points)
        eggProgressFromFeeding: 5, // Bonus progress if queen is fed by at least one ant
        maxFood: 750, // Increased capacity
        maxQueenHealth: 100,
        threatAppearanceChance: 0.015, // Slightly lower chance
        threatDuration: 12, // Ticks a threat lasts
        threatDamagePerTick: 0.8, // Base damage before defense (slightly less but scaled by defense)
        defenseEffectiveness: 1.2, // Threat damage prevented per defending ant (increased)
        resourceSpawnChance: 0.04, // Slightly lower chance
        resourceDuration: 20, // Ticks resources are available (increased)
        ticksPerSecond: 3, // Game speed (faster ticks)
        gameDurationLimit: 300, // Optional: Game ends after X ticks for a 'win' condition
    };

    let gameTickCount = 0;

    function initGame() {
        gameTickCount = 0;
        eggProgress = 0;
        gameState = {
            population: config.initialPopulation,
            food: config.initialFood,
            queenHealth: config.initialQueenHealth,
            antsGathering: 0,
            antsFeedingQueen: 0,
            antsDefending: 0,
            hasThreat: false,
            threatRemaining: 0,
            hasExternalResources: true, // Start with resources
            resourcesRemaining: config.resourceDuration,
            isGameOver: false,
            message: "המושבה שגשגת עד כה!"
        };

        // Set initial assigned ants (or 0 if population is too low)
        const initialGather = Math.min(5, gameState.population);
        const initialFeed = Math.min(3, gameState.population - initialGather);
        const initialDefend = Math.min(2, gameState.population - initialGather - initialFeed);

        gatherAntsInput.value = initialGather;
        feedAntsInput.value = initialFeed;
        defendAntsInput.value = initialDefend;

        assignAnts(); // Perform initial assignment validation and state update
        updateInputMax(); // Set initial maxes based on population
        updateUI();

        assignmentFeedbackEl.textContent = '';
        statusMessageEl.className = 'message success'; // Initial state message class

        if (gameInterval) clearInterval(gameInterval);
        gameInterval = setInterval(gameTick, 1000 / config.ticksPerSecond);
    }

    function updateInputMax() {
         const totalAnts = gameState.population;
         const gathering = parseInt(gatherAntsInput.value) || 0;
         const feeding = parseInt(feedAntsInput.value) || 0;
         const defending = parseInt(defendAntsInput.value) || 0;

         // Calculate remaining ants after current assignments (which might be invalid temporarily)
         const remainingAfterOthersGather = totalAnts - feeding - defending;
         const remainingAfterOthersFeed = totalAnts - gathering - defending;
         const remainingAfterOthersDefend = totalAnts - gathering - feeding;

         // Set max attribute, ensuring it's not negative
         gatherAntsInput.max = Math.max(0, remainingAfterOthersGather);
         feedAntsInput.max = Math.max(0, remainingAfterOthersFeed);
         defendAntsInput.max = Math.max(0, remainingAfterOthersDefend);

         // Clamp current values to the new maxes (browser handles this, but good to be aware)
         // The 'input' event listener already calls this, so inputs update dynamically.
         // The 'change' listener calls assignAnts, which uses the final clamped values.

         // Update displayed available ants
         const assignedSum = parseInt(gatherAntsInput.value) + parseInt(feedAntsInput.value) + parseInt(defendAntsInput.value);
         availableAntsCountEl.textContent = Math.max(0, totalAnts - assignedSum);

          // Update assigned ants indicators next to inputs
         assignedAntsIndicators[0].textContent = gathering;
         assignedAntsIndicators[1].textContent = feeding;
         assignedAntsIndicators[2].textContent = defending;

    }


    function assignAnts() {
        const totalAnts = gameState.population;
        const gathering = parseInt(gatherAntsInput.value) || 0;
        const feeding = parseInt(feedAntsInput.value) || 0;
        const defending = parseInt(defendAntsInput.value) || 0;

        const assignedSum = gathering + feeding + defending;

        // Update state first based on current (potentially clamped by browser max) values
        gameState.antsGathering = gathering;
        gameState.antsFeedingQueen = feeding;
        gameState.antsDefending = defending;


        // Provide feedback if sum exceeds population (should be rare due to max, but double check)
        if (assignedSum > totalAnts) {
            assignmentFeedbackEl.textContent = `לא מספיק נמלים! ניתן להקצות מקסימום ${totalAnts} נמלים. הקצאת ${assignedSum} עולה על המושבה הקיימת.`;
             assignmentFeedbackEl.className = 'feedback-message warning';
        } else if (assignedSum < totalAnts) {
             assignmentFeedbackEl.textContent = `${totalAnts - assignedSum} נמלים פנויות.`;
             assignmentFeedbackEl.className = 'feedback-message info'; // Or success
        }
        else {
            assignmentFeedbackEl.textContent = `כל ${totalAnts} הנמלים הוקצו למשימות.`;
            assignmentFeedbackEl.className = 'feedback-message success';
        }

         // Always update maxes after assignment just in case population changed since last tick
         updateInputMax();
    }

    // Use 'input' for immediate feedback on numbers/maxes, 'change' to finalize assignment state
    gatherAntsInput.addEventListener('input', updateInputMax);
    feedAntsInput.addEventListener('input', updateInputMax);
    defendAntsInput.addEventListener('input', updateInputMax);
    gatherAntsInput.addEventListener('change', assignAnts);
    feedAntsInput.addEventListener('change', assignAnts);
    defendAntsInput.addEventListener('change', assignAnts);


    function gameTick() {
        if (gameState.isGameOver) return;

        gameTickCount++;

        // Ensure assigned ants don't exceed population if it dropped
        assignAnts(); // Re-validate assignments at the start of each tick

        let currentMessage = "המושבה שגשגת."; // Default message
        let messageClass = 'success';

        // 1. Update Food
        const foodGathered = gameState.antsGathering * config.foodGatherRate * (gameState.hasExternalResources ? 1 : 0); // Only gather if resources available
        const foodConsumed = gameState.population * config.foodConsumptionRate;
        gameState.food = Math.min(config.maxFood, gameState.food + foodGathered - foodConsumed);
        gameState.food = Math.max(0, gameState.food);

        // If food is zero, population starts dying faster
        if (gameState.food <= 0) {
            const deathRate = Math.ceil(gameState.population * 0.1); // Lose 10% per tick if starving
            gameState.population = Math.max(0, gameState.population - deathRate);
            currentMessage = "רעב קשה! הנמלים גוועות בהמוניהן...";
            messageClass = 'danger';
             updateInputMax(); // Population changed
        } else if (gameState.food < config.maxFood * 0.15) { // Low food warning
             currentMessage = "מאגרי המזון מתרוקנים במהירות!";
             messageClass = 'warning';
        }


        // 2. Update Queen Health
        const queenHealthGained = gameState.antsFeedingQueen * config.queenHealthGainRate;
        const queenHealthLost = config.queenHealthDecayRate;
        gameState.queenHealth = Math.min(config.maxQueenHealth, gameState.queenHealth + queenHealthGained - queenHealthLost);
        gameState.queenHealth = Math.max(0, gameState.queenHealth);

         if (gameState.queenHealth < config.maxQueenHealth * 0.2) {
             currentMessage = "המלכה חלשה מאוד ונמצאת בסכנה!";
             messageClass = 'danger';
         } else if (gameState.queenHealth < config.maxQueenHealth * 0.5) {
             currentMessage = "המלכה זקוקה לטיפול טוב יותר.";
              messageClass = 'warning';
         }


        // 3. Population Growth (Queen lays eggs)
        // Progress towards egg based on base rate, queen health, and feeding
        const healthFactor = gameState.queenHealth / config.maxQueenHealth; // 0 to 1
        eggProgress += config.eggProgressPerTick + (healthFactor * config.eggProgressFromQueenHealth) + (gameState.antsFeedingQueen > 0 ? config.eggProgressFromFeeding : 0);


        if (eggProgress >= config.eggProgressNeeded) {
            gameState.population += 1;
            eggProgress -= config.eggProgressNeeded; // Keep remainder
            eggProgress = Math.max(0, eggProgress); // Don't go below 0 if remainder is negative (shouldn't happen)
            currentMessage = "ביצה בקעה! נמלה פועלת חדשה הצטרפה למושבה.";
            messageClass = 'info';
            updateInputMax(); // Population changed, update max for assignment inputs
        }
        // Show progress bar only if progress is significant
        if (eggProgress > 1 || gameState.queenHealth > 0) { // Show if any progress or queen alive
            antHatchProgressEl.style.display = 'flex'; // Use flex for alignment
             antHatchProgressBarFillEl.style.width = `${(eggProgress / config.eggProgressNeeded) * 100}%`;
        } else {
             antHatchProgressEl.style.display = 'none';
        }


        // 4. Threat Management
        if (gameState.hasThreat) {
            gameState.threatRemaining--;
            const effectiveDefense = gameState.antsDefending * config.defenseEffectiveness;
            const rawDamage = config.threatDamagePerTick;
            const damageTaken = Math.max(0, rawDamage - effectiveDefense);

            if (damageTaken > 0) {
                // Threats can damage population or queen health
                if (Math.random() < 0.7) { // Higher chance to lose population from generic threat
                     const popDamage = Math.ceil(damageTaken); // Lose at least 1
                     gameState.population = Math.max(0, gameState.population - popDamage);
                     // Only update message if population loss is significant
                     if(popDamage > 0) {
                         currentMessage = `איום קשה! המושבה ספגה פגיעות ואיבדה ${popDamage} נמלים.`;
                         messageClass = 'danger';
                          updateInputMax(); // Population changed
                     }
                } else { // Chance to lose queen health
                    const queenDamage = damageTaken * 10; // Threats hit queen health hard
                    gameState.queenHealth = Math.max(0, gameState.queenHealth - queenDamage);
                     currentMessage = `האיום פוגע קשות בקן! המלכה נפגעה!`;
                      messageClass = 'danger';
                }

            } else if (effectiveDefense > 0 && rawDamage > 0){
                 // Successful defense message
                 currentMessage = "ההגנה הדפה את האיום בהצלחה!";
                 messageClass = 'success';
            } else {
                 // Threat present but no damage (e.g. defense == rawDamage, or no defense needed)
                 currentMessage = `המושבה תחת איום (${gameState.threatRemaining} סבבים נותרו)!`;
                 messageClass = 'warning';
            }


            if (gameState.threatRemaining <= 0) {
                gameState.hasThreat = false;
                 // Only override message if it's still the threat message
                if (messageClass === 'warning' || messageClass === 'danger') {
                    currentMessage = "האיום חלף. המושבה ניצלה!";
                    messageClass = 'success';
                }
                 assignmentFeedbackEl.textContent = "האיום חלף."; // Temporary specific event message
                 assignmentFeedbackEl.className = 'feedback-message info';
                 outsideViewEl.classList.remove('under-threat'); // Remove visual cue
                 threatTimerEl.style.display = 'none';
            } else {
                outsideViewEl.classList.add('under-threat'); // Add visual cue
                 threatTimerEl.style.display = 'block';
                 threatTimerValueEl.textContent = gameState.threatRemaining;
            }
        } else {
             outsideViewEl.classList.remove('under-threat'); // Ensure no visual cue
             threatTimerEl.style.display = 'none';
             // Maybe a threat appears?
             if (Math.random() < config.threatAppearanceChance) {
                 gameState.hasThreat = true;
                 gameState.threatRemaining = config.threatDuration;
                 currentMessage = "איום חדש הופיע בחוץ!";
                 messageClass = 'danger';
                  assignmentFeedbackEl.textContent = "שימו לב! איום חדש בפתח!";
                  assignmentFeedbackEl.className = 'feedback-message danger';
             }
        }

         // 5. External Resources Management
         if (gameState.hasExternalResources) {
             gameState.resourcesRemaining--;
             resourceTimerEl.style.display = 'block';
             resourceTimerValueEl.textContent = gameState.resourcesRemaining;

             if (gameState.resourcesRemaining <= 0) {
                 gameState.hasExternalResources = false;
                  assignmentFeedbackEl.textContent = "המשאבים בחוץ אזלו לעת עתה.";
                  assignmentFeedbackEl.className = 'feedback-message warning';
                   resourceTimerEl.style.display = 'none';
             }
         } else {
             resourceTimerEl.style.display = 'none';
             // Maybe resources reappear?
             if (Math.random() < config.resourceSpawnChance) {
                 gameState.hasExternalResources = true;
                 gameState.resourcesRemaining = config.resourceDuration;
                 assignmentFeedbackEl.textContent = "משאבים חדשים נמצאו בחוץ!";
                 assignmentFeedbackEl.className = 'feedback-message success';
             }
         }

        // Only update main status message if it's not a more critical or recent event message
        if (!assignmentFeedbackEl.textContent || messageClass === 'danger' || messageClass === 'warning' || messageClass === 'info' || statusMessageEl.className === 'success') {
             statusMessageEl.textContent = currentMessage;
             statusMessageEl.className = `message ${messageClass}`; // Update class for styling
        }


        // 6. Check Game Over Conditions
        if (gameState.population <= 0 || gameState.queenHealth <= 0 || gameTickCount > config.gameDurationLimit) {
            gameState.isGameOver = true;
            if (gameState.population <= 0) {
                gameState.message = "המושבה כולה נכחדה ברעב או מאיומים... סוף המשחק.";
            } else if (gameState.queenHealth <= 0) {
                 gameState.message = "המלכה מתה... אין דורות חדשים והמושבה נכחדה לאט לאט.";
            } else { // Game duration limit reached
                 gameState.message = `מזל טוב! המושבה שרדה ושגשגה במשך ${gameTickCount} סבבים!`;
            }
            statusMessageEl.textContent = gameState.message;
            statusMessageEl.className = gameState.queenHealth <= 0 || gameState.population <= 0 ? 'message danger' : 'message success'; // Different class for win/loss
            clearInterval(gameInterval);
            restartButton.style.display = 'block'; // Show restart button
             disableInputs(); // Disable inputs when game is over
        } else {
             restartButton.style.display = 'none'; // Hide restart button if game is not over
             enableInputs(); // Ensure inputs are enabled
        }


        updateUI();

         // Clear temporary feedback after a short delay if it's not an error/warning
        if (assignmentFeedbackEl.textContent && assignmentFeedbackEl.className !== 'feedback-message warning' && assignmentFeedbackEl.className !== 'feedback-message danger') {
             setTimeout(() => { assignmentFeedbackEl.textContent = ''; assignmentFeedbackEl.className = 'feedback-message'; }, 3000); // Clear after 3 seconds
         }
    }

    function updateUI() {
        // Update numerical values
        populationSizeEl.textContent = gameState.population;
        foodLevelEl.textContent = Math.floor(gameState.food);

        // Update Queen Status Text and Color
        let queenText, queenColor, queenClass;
        if (gameState.queenHealth > 85) { queenText = "מצויינת"; queenColor = 'green'; queenClass = 'excellent'; }
        else if (gameState.queenHealth > 60) { queenText = "טובה מאוד"; queenColor = 'darkgreen'; queenClass = 'good'; }
        else if (gameState.queenHealth > 30) { queenText = "יציבה"; queenColor = 'orange'; queenClass = 'warning'; }
        else if (gameState.queenHealth > 0) { queenText = "חלשה מאוד"; queenColor = 'red'; queenClass = 'critical'; }
        else { queenText = "מתה"; queenColor = 'darkred'; queenClass = 'critical'; }
        queenStatusEl.textContent = queenText;
        queenStatusEl.style.color = queenColor;
         // Add/remove warning/critical class for pulsing animation
         queenStatusEl.classList.toggle('warning', queenClass === 'warning');
         queenStatusEl.classList.toggle('critical', queenClass === 'critical');

        // Update Threat Status Text and Color/Class
        threatStatusEl.textContent = gameState.hasThreat ? `קיים! (${gameState.threatRemaining} סבבים)` : "אין";
        threatStatusEl.style.color = gameState.hasThreat ? 'red' : 'green';


        // Update External Resources Text and Color
        externalResourcesEl.textContent = gameState.hasExternalResources ? `יש (${gameState.resourcesRemaining} סבבים)` : "אזלו לעת עתה";
         externalResourcesEl.style.color = gameState.hasExternalResources ? 'green' : 'orange';

        // Update Visual Bars
        foodBarEl.style.width = `${(gameState.food / config.maxFood) * 100}%`;
         // Update food bar color class based on level
         foodBarEl.classList.toggle('low', gameState.food < config.maxFood * 0.3);
         foodBarEl.classList.toggle('critical', gameState.food < config.maxFood * 0.1);


        queenHealthBarEl.style.width = `${(gameState.queenHealth / config.maxQueenHealth) * 100}%`;
         // Update queen health bar color class based on level
         queenHealthBarEl.className = 'status-bar'; // Reset classes
         if (gameState.queenHealth > 85) queenHealthBarEl.classList.add('excellent');
         else if (gameState.queenHealth > 60) queenHealthBarEl.classList.add('good');
         else if (gameState.queenHealth <= 30) queenHealthBarEl.classList.add('critical'); // Critical threshold

        // Ant Hatch Progress Bar
         antHatchProgressBarFillEl.style.width = `${(eggProgress / config.eggProgressNeeded) * 100}%`;


        // Update available ants display - handled in updateInputMax/assignAnts
        // availableAntsCountEl.textContent = gameState.population - gameState.antsGathering - gameState.antsFeedingQueen - gameState.antsDefending;

    }

     function disableInputs() {
        gatherAntsInput.disabled = true;
        feedAntsInput.disabled = true;
        defendAntsInput.disabled = true;
     }

     function enableInputs() {
         if (!gameState.isGameOver) {
            gatherAntsInput.disabled = false;
            feedAntsInput.disabled = false;
            defendAntsInput.disabled = false;
         }
     }


    // Initial assignment validation on load - moved inside initGame
    // assignAnts();
    // updateInputMax(); // Set initial max values


    restartButton.addEventListener('click', initGame);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר על עולמות הנמלים';
    });

    // Start the game on page load
    initGame();

</script>
```