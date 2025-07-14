---
title: "מתיישבים חדשים: לשרוד בעולם הלא נודע"
english_slug: new-settlers-surviving-the-old-world
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags: [קולוניאליזם, צפון אמריקה, היסטוריה, ניהול משאבים, אסטרטגיה, הישרדות]
---
<h1>מתיישבים חדשים: מסע הישרדות בעולם הלא נודע</h1>
<p>אתה המנהיג! קבוצה של מתיישבים נועזים סומכת עליך שתנווט אותם בשממה הפראית של העולם החדש. אספקה דלה, סכנות אורבות, וכל עונה מביאה אתגרים חדשים. האם תוכל להבטיח את שרידות המושבה שלך?</p>

<div id="simulation-app">
    <div class="app-header">
        <h2>סימולציית הקמת מושבה</h2>
        <div id="current-time">עונה: <span id="current-season" class="stat-value"></span>, שנה: <span id="current-year" class="stat-value"></span></div>
    </div>

    <div id="colony-stats">
        <h3>מצב המושבה</h3>
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-label">אוכלוסייה:</span>
                <span id="stat-population" class="stat-value"></span>
            </div>
            <div class="stat-item">
                <span class="stat-label">מזון:</span>
                <span id="stat-food" class="stat-value food-stat"></span>
            </div>
            <div class="stat-item">
                <span class="stat-label">דיור:</span>
                <span id="stat-housing" class="stat-value"></span> יח' (<span id="stat-housing-capacity" class="stat-value"></span> מקום)
            </div>
            <div class="stat-item">
                <span class="stat-label">בריאות:</span>
                <span id="stat-health" class="stat-value health-stat"></span>%
            </div>
            <div class="stat-item">
                <span class="stat-label">שביעות רצון:</span>
                <span id="stat-satisfaction" class="stat-value satisfaction-stat"></span>%
            </div>
            <div class="stat-item">
                <span class="stat-label">יחסים עם הילידים:</span>
                <span id="stat-natives" class="stat-value natives-stat"></span>%
            </div>
        </div>
    </div>

    <div id="worker-allocation">
        <h3>הקצאת עובדים</h3>
        <p class="unassigned-info">פנויים: <span id="unassigned-workers" class="stat-value"></span> / <span id="total-population-workers" class="stat-value"></span></p>
        <div class="allocation-grid">
            <div class="allocation-item">
                <label for="workers-farm">חקלאות:</label>
                <input type="number" id="workers-farm" value="0" min="0">
            </div>
            <div class="allocation-item">
                <label for="workers-hunt">ציד וליקוט:</label>
                <input type="number" id="workers-hunt" value="0" min="0">
            </div>
            <div class="allocation-item">
                <label for="workers-build">בנייה ותחזוקה:</label>
                <input type="number" id="workers-build" value="0" min="0">
            </div>
            <div class="allocation-item">
                <label for="workers-explore">חקר והגנה:</label>
                <input type="number" id="workers-explore" value="0" min="0">
            </div>
        </div>
        <div id="allocation-warning" class="warning-message" style="display: none;">סה"כ הקצאה עולה על סך האוכלוסייה! אנא תקן.</div>
    </div>

    <button id="advance-season-button" class="game-button">התקדם לעונה הבאה</button>

    <div id="events-log">
        <h3>יומן אירועים</h3>
        <div id="log-output"></div>
    </div>
    <div id="game-over-message" class="game-end-message"></div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    #simulation-app {
        font-family: 'Heebo', sans-serif;
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        background-color: #f0f4f8; /* Soft background */
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        direction: rtl;
        text-align: right;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        color: #333;
    }

    .app-header {
        text-align: center;
        margin-bottom: 25px;
    }

    .app-header h2 {
        color: #2c3e50; /* Dark blue */
        margin-bottom: 5px;
    }

    #current-time {
        font-size: 1.1em;
        color: #555;
    }

    h3 {
        color: #34495e; /* Slightly lighter blue */
        border-bottom: 2px solid #bdc3c7; /* Light grey separator */
        padding-bottom: 8px;
        margin-bottom: 15px;
        text-align: right; /* Align headers right */
    }

    #colony-stats, #worker-allocation, #events-log {
        margin-bottom: 25px;
        padding: 20px;
        background-color: #ffffff; /* White background for sections */
        border: 1px solid #e0e6ed;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .stats-grid, .allocation-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* Responsive grid */
        gap: 15px; /* Spacing between grid items */
    }

    .stat-item, .allocation-item {
        padding: 10px;
        border: 1px solid #eee;
        border-radius: 5px;
        background-color: #f9fbfd;
    }

    .stat-label {
        font-weight: bold;
        color: #555;
        display: inline-block; /* Ensure label takes space */
        width: 100px; /* Fixed width for alignment */
    }

    .stat-value {
        font-weight: 700;
        color: #2980b9; /* Blue */
        transition: color 0.5s ease, transform 0.5s ease; /* Smooth transitions */
    }

    /* Stat Color Feedback */
    .stat-value.low { color: #e74c3c; } /* Red for low */
    .stat-value.medium { color: #f39c12; } /* Orange for medium */
    .stat-value.high { color: #2ecc71; } /* Green for high */

    .unassigned-info {
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 20px;
        color: #34495e;
    }

    #worker-allocation label {
        font-weight: normal; /* Reset label weight */
        color: #333;
        margin-left: 5px;
        display: inline-block; /* Allow label and input on same line */
    }

    #worker-allocation input[type="number"] {
        width: 80px;
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1em;
        text-align: center;
        transition: border-color 0.3s ease;
    }

     #worker-allocation input[type="number"]:focus {
         border-color: #3498db;
         outline: none;
     }

    .warning-message {
        color: #e74c3c; /* Red */
        background-color: #fdeded; /* Light red background */
        border: 1px solid #e74c3c;
        padding: 10px;
        border-radius: 5px;
        margin-top: 15px;
        text-align: center;
        font-weight: bold;
    }


    .game-button {
        display: block;
        width: 100%;
        padding: 12px 20px;
        background-color: #2ecc71; /* Green */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.2em;
        cursor: pointer;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .game-button:hover {
        background-color: #27ad60; /* Darker green */
    }

    .game-button:active {
        transform: scale(0.98); /* Press effect */
    }

    .game-button:disabled {
        background-color: #bdc3c7; /* Grey when disabled */
        cursor: not-allowed;
    }

    #events-log {
        height: 200px; /* Increased height */
        overflow-y: auto;
        background-color: #ecf0f1; /* Light grey */
        border: 1px solid #bdc3c7;
    }

    #log-output div {
        margin-bottom: 10px; /* Increased space */
        padding-bottom: 10px;
        border-bottom: 1px dashed #bdc3c7; /* Dashed separator */
        font-size: 0.95em;
        line-height: 1.4;
        color: #555;
    }
     #log-output div:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }

     /* Log Message Types (Example using classes, added by JS) */
     .log-event.positive { color: #27ae60; font-weight: bold; } /* Green */
     .log-event.negative { color: #c0392b; font-weight: bold; } /* Dark Red */
     .log-event.warning { color: #f39c12; } /* Orange */
     .log-event.info { color: #555; } /* Default grey */


     .game-end-message {
         margin-top: 20px;
         padding: 15px;
         background-color: #e74c3c; /* Red for game over */
         color: white;
         text-align: center;
         border-radius: 5px;
         font-size: 1.5em; /* Larger font */
         font-weight: bold;
         display: none;
         animation: pulse 1.5s infinite alternate; /* Simple pulse animation */
     }

      .game-end-message.win {
         background-color: #2ecc71; /* Green for win */
         animation: pulse-green 1.5s infinite alternate;
      }

     @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.02); }
     }
     @keyframes pulse-green {
         0% { transform: scale(1); }
         100% { transform: scale(1.02); }
     }


     #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 10px 20px;
        background-color: #bdc3c7; /* Grey */
        color: #333;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.3s ease;
     }

     #toggle-explanation:hover {
         background-color: #95a5a6; /* Darker grey */
     }

     #explanation {
        margin-top: 20px;
        padding: 20px;
        background-color: #ecf0f1; /* Light grey background */
        border: 1px solid #bdc3c7;
        border-radius: 8px;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: #333;
     }

     #explanation h2, #explanation h3 {
         color: #2c3e50;
         text-align: right; /* Align explanation headers right */
         border-bottom: 1px solid #bdc3c7;
         padding-bottom: 5px;
         margin-bottom: 10px;
     }

     #explanation ul {
         padding-right: 20px; /* Indent list */
     }
     #explanation li {
         margin-bottom: 8px;
     }


</style>

<button id="toggle-explanation">הצג רקע היסטורי</button>

<div id="explanation" style="display: none;">
    <h2>ההקשר ההיסטורי: לשרוד בעולם החדש</h2>
    <p>הסימולציה שלפניכם מדגימה כמה מהאתגרים המרכזיים שניצבו בפני המתיישבים האירופאים הראשונים שהגיעו לצפון אמריקה במאות ה-16 וה-17. חיי היום יום היו מאבק מתמיד להישרדות אל מול כוחות טבע, מחלות, והתמודדות עם עולם חדש ושונה.</p>

    <h3>רקע היסטורי ומניעים לקולוניזציה:</h3>
    <p>המניעים להקמת מושבות בצפון אמריקה היו מגוונים ושזורים זה בזה: <strong>כלכלה</strong> (חיפוש אוצרות, משאבים כמו פרוות ועץ, נתיבי סחר חדשים וגידולים חקלאיים רווחיים כמו טבק), <strong>דת</strong> (רצון לחופש פולחן לקבוצות מיעוט, כמו הפוריטנים, או הפצת הנצרות), ו<strong>פוליטיקה/חברה</strong> (הרחבת האימפריה, מתן פתרון לעודף אוכלוסייה או חוסר קרקעות באירופה).</p>

    <h3>סיפורי מושבות מוקדמות:</h3>
    <ul>
        <li><strong>ג'יימסטאון (וירג'יניה, 1607):</strong> הוקמה על ידי חברת לונדון למטרות רווח. המתיישבים הראשונים היו ברובם בני אצולה או מחפשי זהב, וחסרו את הכישורים החקלאיים והמעשיים הנחוצים להישרדות. "זמן הרעב" (The Starving Time) בחורף 1609-1610 הפך לסמל לקשיים, כאשר רוב המתיישבים מתו. רק בזכות מנהיגות נוקשה (ג'ון סמית') וגילוי רווחיות הטבק, המושבה שרדה בקושי.</li>
        <li><strong>פלימות' (מסצ'וסטס, 1620):</strong> נוסדה על ידי קבוצת פוריטנים קיצונים (המכונים "האבות הצליינים") שחיפשו חופש דתי. גם הם סבלו קשות בחורף הראשון, אך זכו לסיוע חיוני משבט וואמפנואג המקומי, במיוחד מסקוונטו, שלימד אותם לגדל תירס ולצוד. שיתוף הפעולה הראשוני הזה אפשר את הישרדותם וחג ההודיה הראשון הפך לסמל הישרדות זה.</li>
    </ul>

    <h3>אתגרים מרכזיים בשממה:</h3>
    <ul>
        <li><strong>השגת מזון ומחסה:</strong> חקלאות אירופאית לא תמיד התאימה לאקלים ולקרקעות. תלות בציד, דיג, ליקוט, ולעיתים בילידים, הייתה קריטית. בניית בתים עמידים לקור ולחום דרשה מאמץ עצום.</li>
        <li><strong>מחלות וסניטציה:</strong> מחלות עולם ישן שהובאו על ידי המתיישבים (אבעבועות שחורות, שפעת) ומחלות עולם חדש (מלריה, טיפוס) יחד עם תנאי היגיינה ירודים וחוסר ידע רפואי, גרמו לתמותה נוראית.</li>
        <li><strong>מזג אוויר קיצוני:</strong> חורפים קפואים, סופות, וקיצים לוהטים או יבשים איימו כל העת על אספקת המזון והבריאות.</li>
        <li><strong>יחסים עם אוכלוסיות ילידיות:</strong> מערכת יחסים מורכבת של תלות הדדית, סחר, אך גם מתח גובר על רקע ניצול, פלישה לטריטוריה, והבדלי תרבות, שהובילה לא פעם לעימותים אלימים.</li>
        <li><strong>בידוד ותקשורת:</strong> הניתוק מאירופה היה משמעותי. ספינות אספקה ותגבורת היו איטיות ובלתי סדירות, מה שהפך כל משבר למאיים עוד יותר.</li>
    </ul>

    <h3>לקחים ומשמעות:</h3>
    <p>סיפורי ההישרדות של המושבות הראשונות מלמדים על חשיבותם של כושר הסתגלות, עבודת כפיים קשה, קבלת החלטות אסטרטגיות (כמו הקצאת עובדים!), ומערכות יחסים מורכבות. ההתמודדות עם אתגרים אלו עיצבה את האתוס האמריקאי של עצמאות, כושר עמידה, והיכולת להפוך שממה למולדת – אך גם טמנה בחובה את הזרעים לקונפליקטים עתידיים עם העמים הילידים וסוגיות חברתיות אחרות.</p>
</div>

<script>
    const state = {
        year: 1620,
        season: 'סתיו', // סתיו, חורף, אביב, קיץ
        population: 50,
        food: 200, // יחידות מזון
        housing: 10, // יחידות דיור (כל יחידה מכילה 5 אנשים)
        health: 80, // %
        satisfaction: 70, // %
        natives: 60, // % (0-100)
        workers: {
            total: 50,
            assigned: {
                farm: 0,
                hunt: 0,
                build: 0,
                explore: 0
            }
        },
        gameOver: false
    };

    const housingCapacityPerUnit = 5;
    const foodConsumptionPerPerson = 2; // יחידות מזון לעונה
    // Production rates per worker per season
    const foodProductionPerFarmer = { סתיו: 0, חורף: 0, אביב: 1.5, קיץ: 3.5 }; // Adjusted slightly for balance/feel
    const foodProductionPerHunter = { סתיו: 2.5, חורף: 1.5, אביב: 2, קיץ: 2 }; // Adjusted slightly
    const housingProductionPerBuilder = { סתיו: 0.2, חורף: 0.1, אביב: 0.3, קיץ: 0.3 }; // Added minimal winter building
    const exploreBenefitPerExplorer = { סתיו: 1.2, חורף: 0.8, אביב: 1.5, קיץ: 1.5 }; // Adjusted slightly
    const seasons = ['סתיו', 'חורף', 'אביב', 'קיץ'];

    const $ = (id) => document.getElementById(id);

    const elements = {
        season: $('current-season'),
        year: $('current-year'),
        population: $('stat-population'),
        food: $('stat-food'),
        housing: $('stat-housing'),
        housingCapacity: $('stat-housing-capacity'),
        health: $('stat-health'),
        satisfaction: $('stat-satisfaction'),
        natives: $('stat-natives'),
        unassigned: $('unassigned-workers'),
        totalPopulationWorkers: $('total-population-workers'),
        workersFarm: $('workers-farm'),
        workersHunt: $('workers-hunt'),
        workersBuild: $('workers-build'),
        workersExplore: $('workers-explore'),
        advanceButton: $('advance-season-button'),
        logOutput: $('log-output'),
        gameOverMessage: $('game-over-message'),
        toggleExplanationButton: $('toggle-explanation'),
        explanation: $('explanation'),
        allocationWarning: $('allocation-warning')
    };

    function updateUI() {
        elements.season.textContent = state.season;
        elements.year.textContent = state.year;

        elements.population.textContent = Math.floor(state.population);
        elements.food.textContent = Math.max(0, Math.floor(state.food));
        elements.housing.textContent = Math.floor(state.housing);
        elements.housingCapacity.textContent = Math.floor(state.housing * housingCapacityPerUnit);
        elements.health.textContent = Math.max(0, Math.min(100, Math.floor(state.health)));
        elements.satisfaction.textContent = Math.max(0, Math.min(100, Math.floor(state.satisfaction)));
        elements.natives.textContent = Math.max(0, Math.min(100, Math.floor(state.natives)));

        state.workers.total = Math.floor(state.population * 0.8); // Assume 80% of population are workers
        elements.totalPopulationWorkers.textContent = state.workers.total;
        const assigned = Object.values(state.workers.assigned).reduce((sum, val) => sum + val, 0);
        const unassigned = Math.max(0, state.workers.total - assigned);
        elements.unassigned.textContent = unassigned;

        // Apply color feedback based on stat values
        applyStatColor(elements.food, state.food, state.population * foodConsumptionPerPerson * 2, state.population * foodConsumptionPerPerson * 4); // Low if < 2 seasons, High if > 4 seasons
        applyStatColor(elements.health, state.health, 40, 75); // Low if < 40, High if > 75
        applyStatColor(elements.satisfaction, state.satisfaction, 40, 75); // Low if < 40, High if > 75
        applyStatColor(elements.natives, state.natives, 30, 70); // Low if < 30, High if > 70

        // Ensure input values reflect assigned workers
        elements.workersFarm.value = state.workers.assigned.farm;
        elements.workersHunt.value = state.workers.assigned.hunt;
        elements.workersBuild.value = state.workers.assigned.build;
        elements.workersExplore.value = state.workers.assigned.explore;

        // Disable inputs if game is over
        const inputs = [elements.workersFarm, elements.workersHunt, elements.workersBuild, elements.workersExplore];
        inputs.forEach(input => input.disabled = state.gameOver);
        elements.advanceButton.disabled = state.gameOver;

        if (state.gameOver) {
            elements.gameOverMessage.style.display = 'block';
            elements.advanceButton.style.display = 'none';
             if (state.population <= 0) {
                 elements.gameOverMessage.classList.remove('win');
             } else {
                 elements.gameOverMessage.classList.add('win');
             }
        } else {
             elements.gameOverMessage.style.display = 'none';
             elements.advanceButton.style.display = 'block';
             elements.gameOverMessage.classList.remove('win'); // Reset class
        }

        // Update allocation warning
        if (assigned > state.workers.total) {
             elements.allocationWarning.style.display = 'block';
             elements.unassigned.classList.add('low'); // Highlight unassigned if negative
             elements.advanceButton.disabled = true; // Cannot advance with invalid allocation
        } else {
             elements.allocationWarning.style.display = 'none';
             elements.unassigned.classList.remove('low');
             if (!state.gameOver) elements.advanceButton.disabled = false; // Re-enable button if allocation is valid and not game over
        }
    }

    function applyStatColor(element, value, lowThreshold, highThreshold) {
        element.classList.remove('low', 'medium', 'high');
        if (value < lowThreshold) {
            element.classList.add('low');
        } else if (value > highThreshold) {
            element.classList.add('high');
        } else {
            element.classList.add('medium');
        }
         // Simple pulse animation on change
         element.classList.add('pulse-animation');
         setTimeout(() => {
             element.classList.remove('pulse-animation');
         }, 500); // Animation duration
    }

    function logEvent(message, type = 'info') { // Added type parameter
        const messageElement = document.createElement('div');
        messageElement.textContent = `${state.season} ${state.year}: ${message}`;
        messageElement.classList.add('log-event', type); // Add classes for styling
        elements.logOutput.prepend(messageElement);
        // Optional: scroll to top to see latest message
        // elements.logOutput.scrollTop = 0;
        if (elements.logOutput.children.length > 100) { // Keep log from getting too long
            elements.logOutput.removeChild(elements.logOutput.lastChild);
        }
    }

    function checkGameOver() {
        if (state.population <= 0 || state.food < -(state.population * foodConsumptionPerPerson * 2) || state.health <= 5) { // More strict loss conditions
            state.gameOver = true;
            elements.gameOverMessage.textContent = "המושבה נכשלה. התנאים היו קשים מדי. נסו שוב!";
            logEvent("המושבה חדלה להתקיים.", 'negative');
        } else if (state.year >= 1625 && state.population > 60 && state.housing * housingCapacityPerUnit >= state.population && state.food > state.population * foodConsumptionPerPerson * 3 && state.health > 70 && state.satisfaction > 70) { // More challenging win condition
             state.gameOver = true;
             elements.gameOverMessage.textContent = "המושבה שרדה והתבססה! עתידה מובטח.";
             logEvent("המושבה התבססה והצליחה!", 'positive');
        }
        updateUI();
    }

    function calculateNextSeason() {
        if (state.gameOver) return;

        // --- Process Season Start ---
        logEvent(`תחילת עונת ה${state.season}. נותר מזון: ${Math.max(0, Math.floor(state.food))}, אוכלוסייה: ${Math.floor(state.population)}.`);

        const assignedWorkers = Object.values(state.workers.assigned).reduce((sum, val) => sum + val, 0);
        if (assignedWorkers > state.workers.total) {
            logEvent("אזהרה: הוקצו יותר עובדים מכפי שזמינים. הקצאה לא חוקית נמנעה קודם לכן.", 'warning');
             // This case should ideally be prevented by handleAllocationChange logic
             // But as a fallback, we could adjust or just stop. Let's prevent advancing in handleAllocationChange.
             if (elements.advanceButton.disabled) return; // Stop if button is disabled by warning
        }


        // --- Resource Consumption ---
        let foodConsumed = state.population * foodConsumptionPerPerson;
        state.food -= foodConsumed;
        logEvent(`צריכת מזון: ${Math.floor(foodConsumed)} יחידות.`);

        // --- Resource Production ---
        let foodProduced = 0;
        foodProduced += state.workers.assigned.farm * foodProductionPerFarmer[state.season];
        foodProduced += state.workers.assigned.hunt * foodProductionPerHunter[state.season];
        state.food += foodProduced;
        logEvent(`ייצור מזון: ${Math.floor(foodProduced)} יחידות.`);

        let housingBuilt = state.workers.assigned.build * housingProductionPerBuilder[state.season];
        state.housing += housingBuilt;
        if (housingBuilt > 0) logEvent(`בנייה: הוקמו כ-${housingBuilt.toFixed(1)} יחידות דיור חדשות.`);


        // --- Stat Changes based on Conditions ---
        let healthChange = 0;
        let satisfactionChange = 0;
        let populationChange = 0; // For natural change and events

        const effectiveHousingCapacity = state.housing * housingCapacityPerUnit;
        if (state.population > effectiveHousingCapacity) {
            const overcrowdingFactor = Math.min(1, (state.population - effectiveHousingCapacity) / state.population);
            healthChange -= overcrowdingFactor * 25; // Increased penalty
            satisfactionChange -= overcrowdingFactor * 35; // Increased penalty
            logEvent(`צפיפות יתר (${Math.floor(state.population)} נפש על ${Math.floor(effectiveHousingCapacity)} מקום) פוגעת קשות בבריאות ובשביעות הרצון.`, 'negative');
        } else if (state.population < effectiveHousingCapacity * 0.8) { // Bonus for ample housing
             healthChange += 3;
             satisfactionChange += 3;
        }


        if (state.food < 0) {
            const starvationFactor = Math.min(1, -state.food / (state.population * foodConsumptionPerPerson * 1.5)); // Affects more severely
            healthChange -= starvationFactor * 60; // Severe health drop
            satisfactionChange -= starvationFactor * 50;
            logEvent(`מחסור קריטי במזון! רעב פוגע קשות במושבה.`, 'negative');
             // Population loss due to starvation - more severe
             const deaths = Math.floor(state.population * starvationFactor * 0.3); // Up to 30% of those affected
             state.population = Math.max(0, state.population - deaths);
             populationChange -= deaths;
             if (deaths > 0) {
                  logEvent(`${deaths} אנשים מתו מרעב.`, 'negative');
             }
            state.food = 0;
        } else if (state.food / state.population > foodConsumptionPerPerson * 3) { // Significant surplus food
             healthChange += 4;
             satisfactionChange += 4;
        } else if (state.food / state.population > foodConsumptionPerPerson * 1.5) { // Moderate surplus food
             healthChange += 2;
             satisfactionChange += 2;
        }


        // Exploration/Defense & Native Relations
        let nativeRelationChange = state.workers.assigned.explore * exploreBenefitPerExplorer[state.season]; // Base positive effect
         if (state.workers.assigned.explore < state.workers.total * 0.05 && state.season !== 'חורף') { // Penalty for neglecting exploration/defense outside winter
            nativeRelationChange -= 5;
             logEvent("הזנחת החקר וההגנה מעוררת חששות בסביבה.", 'warning');
         }


        // --- Random Events ---
        if (Math.random() < 0.3) { // Increased chance of events
            const eventType = Math.random();
            if (eventType < 0.35 && state.health < 90) { // Disease (more likely if health is low)
                const severity = Math.random();
                const healthDrop = 20 + Math.floor(severity * 30); // More severe drop
                const populationLossFactor = 0.08 + severity * 0.12; // 8-20% loss
                const deaths = Math.floor(state.population * populationLossFactor * (100 - state.health + 20) / 100); // Disease much worse with low health
                healthChange -= healthDrop;
                state.population = Math.max(0, state.population - deaths);
                 populationChange -= deaths;
                logEvent(`מגפה קטלנית פרצה במושבה! הבריאות צנחה, ו-${deaths} אנשים נפטרו.`, 'negative');
            } else if (eventType < 0.6 && (state.season === 'חורף' || state.season === 'קיץ')) { // Extreme weather
                 const impact = Math.random();
                 const foodImpact = Math.floor(state.food * (0.15 + impact * 0.2)); // Higher food loss
                 const healthImpact = Math.floor(15 + impact * 15); // Higher health impact
                 if (state.season === 'חורף') {
                     state.food = Math.max(0, state.food - foodImpact);
                     healthChange -= healthImpact;
                     logEvent(`חורף מקפיא במיוחד פגע באספקה וגרם לתחלואה.`, 'negative');
                 } else { // Summer drought/heatwave
                      state.food = Math.max(0, state.food - foodImpact);
                      healthChange -= healthImpact;
                      logEvent(`גל חום ויובש קיצוני פגע ביבולים ובבריאות.`, 'negative');
                 }
            } else if (eventType < 0.75 && state.year > 1621) { // New arrivals
                 const arrivals = Math.floor(Math.random() * 15) + 8; // More arrivals
                 state.population += arrivals;
                 state.food += Math.floor(arrivals * foodConsumptionPerPerson * 2.5); // Bring substantial food
                 state.housing += Math.floor(arrivals / housingCapacityPerUnit / 2); // Might bring some simple shelters
                 satisfactionChange += 15; // Significant hope boost
                 logEvent(`${arrivals} מתיישבים חדשים הגיעו בבטחה מאירופה! תקווה חדשה למושבה.`, 'positive');
            } else if (eventType < 0.9 && state.natives < 70) { // Negative Native Event (more likely if relations bad)
                const hostility = 10 + Math.floor(Math.random() * (80 - state.natives)); // Hostility scales with bad relations
                nativeRelationChange -= hostility * 0.3;
                healthChange -= hostility * 0.2; // Small health impact
                 const combatLosses = Math.floor(state.population * (hostility / 100) * 0.05); // Small chance of loss
                 state.population = Math.max(0, state.population - combatLosses);
                 populationChange -= combatLosses;
                 if (combatLosses > 0) {
                     logEvent(`עימות אלים עם שבט ילידי! ${combatLosses} מתיישבים אבדו, והיחסים התדרדרו קשות.`, 'negative');
                 } else {
                     logEvent(`התנגשות עם שבט ילידי על טריטוריה. היחסים התדרדרו.`, 'negative');
                 }
            }
             else { // Positive Events
                if (Math.random() < 0.4 && state.natives > 40) { // Positive Native Event (more likely if relations good)
                     const generosity = 10 + Math.floor(Math.random() * state.natives * 0.3); // Generosity scales with good relations
                    nativeRelationChange += generosity * 0.5;
                    state.food += Math.floor(generosity * 5); // They share food
                    satisfactionChange += generosity * 0.3;
                    logEvent("שבט ילידי סמוך הגיע עם סיוע ומזון! גילויי ידידות מחזקים את הקשר.", 'positive');
                } else if (Math.random() < 0.7) {
                     const finding = Math.floor(Math.random() * 80) + 30;
                    state.food += finding;
                    satisfactionChange += 5;
                    logEvent(`משלחת חקר גילתה מקור מזון חדש ועשיר! התגלה מזון: ${finding} יחידות.`, 'positive');
                } else {
                    state.housing += Math.random() > 0.5 ? 1 : 2;
                    satisfactionChange += 8;
                    logEvent("בניית מחסן או בית משותף גדול הושלמה!");
                }
            }
        }


        // --- Apply Changes and Decay/Recovery ---
        state.health = Math.max(0, Math.min(100, state.health + healthChange));
         // Natural health tendency towards a baseline influenced by satisfaction and food
         state.health += (state.satisfaction/100 * 10 + (state.food / state.population > foodConsumptionPerPerson * 2 ? 10 : 0) - state.health * 0.1);


        state.satisfaction = Math.max(0, Math.min(100, state.satisfaction + satisfactionChange));
         // Natural satisfaction tendency towards a baseline influenced by health and housing
         state.satisfaction += (state.health/100 * 10 + (effectiveHousingCapacity > state.population ? 10 : 0) - state.satisfaction * 0.1);


         state.natives = Math.max(0, Math.min(100, state.natives + nativeRelationChange));
         // Native relations decay over time if not maintained
         state.natives = Math.max(0, state.natives - 2);


        // --- Population Change (Births/Deaths) ---
        // Simple model based on health and satisfaction
        const baseGrowthRate = 0.01; // Base natural growth per season
        const healthFactor = (state.health - 50) / 100; // Negative below 50, positive above
        const satisfactionFactor = (state.satisfaction - 50) / 100;
        const netChange = Math.floor(state.population * baseGrowthRate * (1 + healthFactor + satisfactionFactor));

        state.population = Math.max(0, state.population + netChange);
        populationChange += netChange; // Add natural change to total change this season

        if (netChange > 0) logEvent(`${netChange} לידות חדשות הביאו תקווה למושבה.`, 'positive');
        if (netChange < 0 && populationChange < 0) logEvent(`${Math.abs(netChange)} מתיישבים נוספים נפטרו מתנאים קשים.`, 'negative'); // Only log if total change is negative

        // --- Advance Season/Year ---
        const currentSeasonIndex = seasons.indexOf(state.season);
        if (currentSeasonIndex === seasons.length - 1) {
            state.season = seasons[0]; // Back to Autumn
            state.year++;
        } else {
            state.season = seasons[currentSeasonIndex + 1];
        }

        // --- Prepare for Next Season ---
        // Reset assigned workers for the next season
        state.workers.assigned = { farm: 0, hunt: 0, build: 0, explore: 0 };
        elements.workersFarm.value = 0;
        elements.workersHunt.value = 0;
        elements.workersBuild.value = 0;
        elements.workersExplore.value = 0;


        updateUI();
        checkGameOver();
    }

    function handleAllocationChange(event) {
        const inputs = [elements.workersFarm, elements.workersHunt, elements.workersBuild, elements.workersExplore];
        let totalAssigned = 0;

        // Update state.workers.assigned based on input values
        state.workers.assigned.farm = parseInt(elements.workersFarm.value, 10) || 0;
        state.workers.assigned.hunt = parseInt(elements.workersHunt.value, 10) || 0;
        state.workers.assigned.build = parseInt(elements.workersBuild.value, 10) || 0;
        state.workers.assigned.explore = parseInt(elements.workersExplore.value, 10) || 0;

         totalAssigned = Object.values(state.workers.assigned).reduce((sum, val) => sum + val, 0);

         // Clamp values to be non-negative
         inputs.forEach(input => {
             if (parseInt(input.value, 10) < 0) input.value = 0;
         });

        // Prevent total assigned exceeding total available workers
         totalAssigned = Object.values(state.workers.assigned).reduce((sum, val) => sum + val, 0); // Recalculate after clamping negatives

        if (totalAssigned > state.workers.total) {
            // Calculate the excess
            const excess = totalAssigned - state.workers.total;
            // Find which input was just changed
            const changedInput = event.target;
            let changedValue = parseInt(changedInput.value, 10) || 0;

            // Reduce the changed input value by the excess, but not below 0
            changedInput.value = Math.max(0, changedValue - excess);

             // Update the state again with the corrected value
            state.workers.assigned[changedInput.id.replace('workers-', '')] = parseInt(changedInput.value, 10) || 0;

            // Recalculate total assigned after correction
            totalAssigned = Object.values(state.workers.assigned).reduce((sum, val) => sum + val, 0);

            // Display warning if still somehow over (shouldn't happen with this logic) or just for feedback
            if (totalAssigned > state.workers.total) {
                elements.allocationWarning.style.display = 'block';
            } else {
                 elements.allocationWarning.style.display = 'none';
            }

        } else {
             elements.allocationWarning.style.display = 'none';
        }


        updateUI(); // Always update UI after allocation changes
    }

    function init() {
        updateUI();
        elements.advanceButton.addEventListener('click', calculateNextSeason);

        // Add event listeners for worker allocation inputs
        const inputs = [elements.workersFarm, elements.workersHunt, elements.workersBuild, elements.workersExplore];
         inputs.forEach(input => {
             // Use 'input' event for immediate feedback as user types
             input.addEventListener('input', handleAllocationChange);
             // Also use 'change' for final value commit (e.g., after losing focus)
             input.addEventListener('change', handleAllocationChange);
             // Set max attribute dynamically
             input.setAttribute('max', state.workers.total);
         });


         elements.toggleExplanationButton.addEventListener('click', () => {
             const explanationDiv = elements.explanation;
             const isHidden = explanationDiv.style.display === 'none';
             explanationDiv.style.display = isHidden ? 'block' : 'none';
             elements.toggleExplanationButton.textContent = isHidden ? 'הסתר רקע היסטורי' : 'הצג רקע היסטורי';
         });

         logEvent("ברוכים הבאים למושבה החדשה! הקצו עובדים לכל משימה לקראת העונה הראשונה.", 'info');
    }

    init();

</script>
```