---
title: "גן חיות: הצלת מינים בסכנת הכחדה - סימולציה"
english_slug: zoo-management-endangered-species-conservation-simulation
category: "מדעי הסביבה / כללי"
tags: [שמירת טבע, גן חיות, מינים בסכנת הכחדה, אקולוגיה, ניהול משאבים, סימולציה]
---
# מנהלים גן חיות: הצלת מינים בסכנת הכחדה

ברוכים הבאים לתפקידכם החדש כמנהלי גן חיות החזיתי של המאבק העולמי להצלת מינים בסכנת הכחדה! האם תצליחו לאזן בין תקציב מוגבל, צרכי החיות המורכבים, ומאמצי השימור הדחופים? עתידם של מינים שלמים spאולי תלוי בהחלטות שלכם.

<div id="app" class="zoo-container">
    <h2 class="app-title">סימולציית ניהול אוכלוסייה</h2>
    <div id="stats" class="panel stats-panel">
        <h3>מצב גן החיות</h3>
        <div class="stat-item"><span class="stat-label">שנה:</span> <span id="year" class="stat-value">0</span></div>
        <div class="stat-item"><span class="stat-label">תקציב:</span> <span id="budget" class="stat-value budget-value">$100,000</span></div>
        <div class="stat-item"><span class="stat-label">אוכלוסייה:</span> <span id="population" class="stat-value population-value">0</span> פרטים</div>
        <div class="stat-item"><span class="stat-label">מגוון גנטי:</span> <span id="geneticDiversity" class="stat-value genetic-diversity-value">100%</span></div>
        <div class="stat-item"><span class="stat-label">בריאות האוכלוסייה:</span> <span id="health" class="stat-value health-value">100%</span></div>
    </div>

    <div id="controls" class="panel controls-panel">
        <h3>החלטות אסטרטגיות</h3>
        <div class="control-group purchase-group">
            <h4>רכישת פרטים חדשים (תוספת "דם חדש"):</h4>
            <p class="cost-info">עלות פרט: $<span id="animalCost">10,000</span></p>
            <button id="buyMale" class="control-button buy-button">קנה זכר ♂️</button>
            <button id="buyFemale" class="control-button buy-button">קנה נקבה ♀️</button>
            <p class="info-text">רכישת פרטים חדשים מחוץ לגן החיות מגדילה את המגוון הגנטי.</p>
        </div>

        <div class="control-group enclosure-group">
            <h4>ניהול הכלוב והסביבה:</h4>
            <label for="enclosureSize" class="control-label">גודל כלוב:</label>
            <select id="enclosureSize" class="control-select">
                <option value="small">קטן ($5,000 לשנה)</option>
                <option value="medium">בינוני ($10,000 לשנה)</option>
                <option value="large">גדול ($15,000 לשנה)</option>
            </select><br>
            <label for="enclosureQuality" class="control-label">איכות כלוב:</label>
            <select id="enclosureQuality" class="control-select">
                <option value="basic">בסיסית ($3,000 לשנה)</option>
                <option value="good">טובה ($6,000 לשנה)</option>
                <option value="excellent">מצוינת ($9,000 לשנה)</option>
            </select>
            <p class="info-text">סביבת חיים איכותית משפיעה ישירות על בריאות הסיכוי לרבייה.</p>
        </div>

        <div class="control-group breeding-group">
            <h4>תוכנית רבייה מנוהלת:</h4>
            <input type="checkbox" id="breedingProgram" class="control-checkbox" checked>
            <label for="breedingProgram" class="control-label">הפעל תוכנית רבייה</label>
            <p class="info-text">תוכנית רבייה מנוהלת חיונית להגדלת האוכלוסייה בשבי.</p>
        </div>

        <button id="nextYear" class="next-year-button">עבור לשנה הבאה ⏩</button>
    </div>

    <div id="messages" class="panel messages-panel">
        <h3>יומן גן החיות</h3>
        <ul id="messageList"></ul>
    </div>

    <div id="gameOver" class="end-screen game-over" style="display: none;">
        <h3>Game Over</h3>
        <p id="gameOverMessage"></p>
        <button class="restart-button" onclick="location.reload()">שחק שוב</button>
    </div>
     <div id="win" class="end-screen win-screen" style="display: none;">
        <h3>ניצחון!</h3>
        <p id="winMessage"></p>
        <button class="restart-button" onclick="location.reload()">שחק שוב</button>
    </div>

    <div id="animations-overlay" class="animations-overlay">
        <!-- Visual feedback elements can be added here, e.g., pulsing icons -->
         <div id="birth-animation" class="animation-icon" style="display: none;">👶</div>
         <div id="death-animation" class="animation-icon" style="display: none;">💀</div>
         <div id="money-in-animation" class="animation-icon money-animation" style="display: none;">+💲</div>
         <div id="money-out-animation" class="animation-icon money-animation" style="display: none;">-💲</div>
    </div>
</div>

<button id="toggleExplanation" class="explanation-toggle-button">הצג מידע רקע על שימור</button>

<div id="explanation" class="explanation-panel" style="display: none;">
    <h2>מידע רקע: תפקיד גני החיות בשימור מינים</h2>

    <h3>מתצוגה לשימור: האבולוציה של גן החיות המודרני</h3>
    <p>בעבר, גני חיות נתפסו בעיקר כמקומות בידור. כיום, הם חוד החנית במאמצי שימור עולמיים. הם משמשים כמרכזים למחקר, חינוך, והכי חשוב - כ"תיבות נוח" למינים בסכנת הכחדה, תוך שיתוף פעולה בינלאומי לניהול אוכלוסיות.</p>

    <h3>תוכניות רבייה בשבי (Captive Breeding) - רשת ביטחון לטבע</h3>
    <p>המטרה המרכזית: יצירת אוכלוסיות בריאות ויציבות בשבי. אוכלוסיות אלו מהוות רשת ביטחון מפני הכחדה בטבע. האתגרים עצומים: שמירה על מגוון גנטי חיוני, הבטחת רווחת החיות, והתמודדות עם קשיי רבייה או בעיות בריאות ייחודיות למין.</p>

    <h3>מדוע מגוון גנטי הוא קריטי?</h3>
    <p>מגוון גנטי (השונות הגנטית בתוך אוכלוסייה) הוא עמוד השדרה של חוסנה של אוכלוסייה. באוכלוסיות קטנות בשבי, מגוון זה עלול לרדת במהירות ("קריסת עקה" - Inbreeding depression). רביית קרובים מגדילה סיכון למחלות תורשתיות, פוגעת בפוריות ומצמצמת את היכולת להסתגל לשינויים או למחלות חדשות.</p>

    <h3>ספרי עדר וניהול גלובלי: לתכנן את עתיד המין</h3>
    <p>כדי למנוע פגיעה במגוון הגנטי, גני חיות משתמשים בספרי עדר (Studbooks) - מסד נתונים מפורט על כל פרט בתוכנית הרבייה העולמית. מידע זה (מוצא, קשרים משפחתיים, היסטוריה רפואית) מאפשר למנהלי האוכלוסייה לתכנן העברות חיות בין גני חיות ולהמליץ על זיווגים אופטימליים לשימור מירבי של המגוון הגנטי.</p>

    <h3>החזרה לטבע (Reintroduction) - החלום הגדול</h3>
    <p>הפסגה של מאמצי השימור בשבי היא החזרת פרטים לבית גידולם הטבעי, כשהתנאים בטבע מאפשרים זאת (האיומים הוסרו, בית הגידול שוקם). זהו תהליך מורכב הדורש הכנת החיות לחיים בטבע (כמו לימוד ציד או הימנעות מטורפים) ומעקב צמוד. לא כל תוכנית מסתיימת בהחזרה לטבע, אך גם קיום אוכלוסייה בריאה בשבי הוא הישג שימורי עצום.</p>

    <h3>סיפורי הצלחה: מינים שניצלו בזכות גני החיות</h3>
    <p>היסטורית שימור גני החיות רצופה סיפורי הצלחה מעוררי השראה. מינים כמו הקונדור הקליפורני, סוס פרז'בלסקי, ראם ערבי ועוד, חבים את הישרדותם במידה רבה לתוכניות רבייה והחזרה לטבע שנוהלו על ידי גני חיות וארגוני שימור ברחבי העולם.</p>
</div>


<style>
    /* Global & Layout */
    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: #333;
        background-color: #eef5f1; /* Light nature-inspired background */
        padding: 20px;
    }

    .zoo-container {
        max-width: 800px;
        margin: 20px auto;
        padding: 20px;
        background: linear-gradient(to bottom, #f0fff0, #d0e8d0); /* Subtle gradient */
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border: 1px solid #c0d0c0;
    }

    .app-title {
        text-align: center;
        color: #2a6a4b; /* Dark green */
        margin-bottom: 25px;
        font-size: 2em;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.05);
    }

    /* Panels */
    .panel {
        margin-bottom: 25px;
        padding: 20px;
        background-color: #ffffff;
        border: 1px solid #d8e8d8;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    .panel h3 {
        color: #2a6a4b;
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 2px solid #eef5f1;
        padding-bottom: 10px;
    }

    /* Stats Panel */
    .stats-panel .stat-item {
        margin: 10px 0;
        font-size: 1.1em;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 5px;
        border-bottom: 1px dotted #eee;
    }

     .stats-panel .stat-item:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }

    .stat-label {
        font-weight: bold;
        color: #555;
    }

    .stat-value {
        font-weight: bold;
        color: #007b40; /* Green for positive stats */
        transition: color 0.3s ease-in-out, transform 0.3s ease-in-out; /* Animation for changes */
    }

    /* Specific Stat Colors */
    .budget-value { color: #007bff; } /* Blue */
    .population-value { color: #d9534f; } /* Red/Orange */
    .genetic-diversity-value { color: #f0ad4e; } /* Orange/Yellow */
    .health-value { color: #5cb85c; } /* Green */

     /* Animation class for stat changes */
    .stat-value.changed {
        animation: statChangePulse 0.5s ease-out;
    }

    @keyframes statChangePulse {
        0% { transform: scale(1); color: inherit; }
        50% { transform: scale(1.05); color: #ff4500; } /* Pulse color */
        100% { transform: scale(1); color: inherit; }
    }


    /* Controls Panel */
    .control-group {
        margin-bottom: 20px;
        padding: 15px;
        border: 1px dashed #c0d0c0;
        border-radius: 6px;
        background-color: #f9fcf9;
    }

    .control-group h4 {
        color: #4a8a6b;
        margin-top: 0;
        margin-bottom: 10px;
    }

    .control-label {
        display: inline-block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
    }

    .control-button, .control-select {
        padding: 10px 15px;
        margin: 5px 5px 5px 0;
        cursor: pointer;
        border: 1px solid #c0d0c0;
        border-radius: 5px;
        font-size: 1em;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .control-button:hover {
        background-color: #e8f0e8;
        border-color: #a0b8a0;
    }

    .control-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        background-color: #eee;
    }

    .buy-button {
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
    }

     .buy-button:hover:not(:disabled) {
         background-color: #45a049;
     }

    .control-select {
        background-color: #fff;
    }

    .control-checkbox {
        margin-left: 10px;
        vertical-align: middle;
    }

    .info-text {
        font-size: 0.9em;
        color: #666;
        margin-top: 10px;
        border-top: 1px dotted #eee;
        padding-top: 8px;
    }


    /* Next Year Button */
    .next-year-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #007bff; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.2em;
        margin-top: 20px;
        cursor: pointer;
        transition: background-color 0.3s ease, opacity 0.3s ease;
    }

    .next-year-button:hover:not(:disabled) {
        background-color: #0056b3;
    }

    .next-year-button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
        background-color: #ccc;
    }

    /* Messages Panel */
    .messages-panel ul {
        list-style: none;
        padding: 0;
        max-height: 200px; /* Limit height */
        overflow-y: auto; /* Add scrollbar if needed */
    }

    .messages-panel li {
        margin-bottom: 8px;
        padding: 8px;
        border-bottom: 1px dotted #e0e0e0;
        background-color: #f8f8f8;
        border-radius: 4px;
        font-size: 0.95em;
         opacity: 0; /* Start hidden for fade-in */
         animation: fadeInMessage 0.5s forwards;
    }

    @keyframes fadeInMessage {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* End Screens (Game Over / Win) */
    .end-screen {
        text-align: center;
        padding: 30px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
         animation: scaleIn 0.5s ease-out;
    }

    @keyframes scaleIn {
        from { transform: scale(0.9); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }

    .game-over {
        border: 2px solid #d9534f; /* Red */
        background-color: #fde0df; /* Light red */
        color: #d9534f;
    }

    .win-screen {
         border: 2px solid #5cb85c; /* Green */
         background-color: #e0f2e0; /* Light green */
         color: #2a6a4b;
    }

    .end-screen h3 {
        font-size: 2em;
        margin-bottom: 15px;
         color: inherit; /* Use parent color */
         border-bottom: none;
    }

    .end-screen p {
        font-size: 1.2em;
        margin-bottom: 20px;
    }

    .restart-button {
        padding: 10px 20px;
        font-size: 1.1em;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .restart-button:hover {
        background-color: #0056b3;
    }

    /* Explanation Section */
    .explanation-toggle-button {
        display: block;
        width: 100%;
        padding: 10px;
        margin-top: 20px;
        background-color: #6c757d; /* Grey */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-align: center;
    }

    .explanation-toggle-button:hover {
        background-color: #5a6268;
    }

    .explanation-panel {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #c0d0c0;
        border-radius: 8px;
        background-color: #f9fcf9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    .explanation-panel h2, .explanation-panel h3 {
        color: #2a6a4b;
    }

     .explanation-panel h3 {
         margin-top: 20px;
         border-bottom: 1px dotted #d8e8d8;
         padding-bottom: 5px;
     }

     .explanation-panel p {
         margin-bottom: 15px;
     }

    /* Animations Overlay */
    .animations-overlay {
        position: relative; /* Or absolute, depending on desired layering */
        pointer-events: none; /* Allow clicks to pass through */
        /* You might need to position this over the relevant part of the UI */
    }

    .animation-icon {
        position: absolute;
        font-size: 2em;
        z-index: 100;
        pointer-events: none;
        animation: popUpFade 1s ease-out forwards;
    }

    @keyframes popUpFade {
        0% { transform: translate(-50%, -50%) scale(0.5); opacity: 1; }
        100% { transform: translate(-50%, -150%) scale(1); opacity: 0; }
    }

    .money-animation {
         color: #28a745; /* Green for positive, red for negative */
    }


</style>

<script>
    let year = 0;
    let budget = 100000;
    let population = { males: 0, females: 0 };
    let geneticDiversity = 100; // Start high, decays with inbreeding, improves with new blood
    let health = 100; // Average health
    let enclosureSize = 'small';
    let enclosureQuality = 'basic';
    let breedingProgramEnabled = true;

    const costs = {
        animal: 10000,
        enclosure: {
            small: 5000,
            medium: 10000,
            large: 15000
        },
        quality: {
            basic: 3000,
            good: 6000,
            excellent: 9000
        },
        upkeepPerAnimal: 800 // Slightly reduced upkeep cost per animal
    };

    const maxPopulation = {
        small: 6, // Slightly increased capacity
        medium: 18,
        large: 35
    };

    const healthEffects = {
        small: -8, // Negative effect on health
        medium: 0,
        large: 7,
        basic: -12, // Lower quality hurts more
        good: 5,
        excellent: 12
    };

    const breedingChanceFactors = {
        small: 0.8, // Lower chance in small enclosure
        medium: 1.0,
        large: 1.1,
        basic: 0.6, // Lower chance with basic quality
        good: 1.0,
        excellent: 1.3,
        breedingEnabled: 1.4, // Boost from program
        lowHealth: 0.4, // Penalty for low health
        lowDiversity: 0.6 // Penalty for low diversity
    };

    const naturalDeathChanceBase = 0.02; // Base chance per animal per year


    // UI Elements
    const yearSpan = document.getElementById('year');
    const budgetSpan = document.getElementById('budget');
    const populationSpan = document.getElementById('population');
    const geneticDiversitySpan = document.getElementById('geneticDiversity');
    const healthSpan = document.getElementById('health');
    const messageList = document.getElementById('messageList');
    const gameOverDiv = document.getElementById('gameOver');
    const gameOverMessage = document.getElementById('gameOverMessage');
    const winDiv = document.getElementById('win');
    const winMessage = document.getElementById('winMessage');

    const animalCostSpan = document.getElementById('animalCost');
    const buyMaleBtn = document.getElementById('buyMale');
    const buyFemaleBtn = document.getElementById('buyFemale');
    const enclosureSizeSelect = document.getElementById('enclosureSize');
    const enclosureQualitySelect = document.getElementById('enclosureQuality');
    const breedingProgramCheckbox = document.getElementById('breedingProgram');
    const nextYearBtn = document.getElementById('nextYear');
    const toggleExplanationBtn = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    // Animation Elements (hidden icons)
    const birthAnimation = document.getElementById('birth-animation');
    const deathAnimation = document.getElementById('death-animation');
    const moneyInAnimation = document.getElementById('money-in-animation');
    const moneyOutAnimation = document.getElementById('money-out-animation');


    function updateUI() {
        // Animate stat changes
        animateStatChange(budgetSpan, budget.toFixed(0));
        animateStatChange(yearSpan, year); // Maybe less important to animate year
        animateStatChange(populationSpan, population.males + population.females);
        animateStatChange(geneticDiversitySpan, geneticDiversity.toFixed(1));
        animateStatChange(healthSpan, health.toFixed(1));


        budgetSpan.textContent = `$${budget.toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: 0 })}`; // Format currency
        geneticDiversitySpan.textContent = geneticDiversity.toFixed(1) + '%';
        healthSpan.textContent = health.toFixed(1) + '%';

        const totalPopulation = population.males + population.females;

        // Update button states and text
        animalCostSpan.textContent = costs.animal.toLocaleString();
        buyMaleBtn.disabled = budget < costs.animal || totalPopulation >= maxPopulation[enclosureSizeSelect.value];
        buyFemaleBtn.disabled = budget < costs.animal || totalPopulation >= maxPopulation[enclosureSizeSelect.value];

         // Update enclosure costs displayed in options
         enclosureSizeSelect.options[0].text = `קטן (מקסימום ${maxPopulation.small} פרטים, $${costs.enclosure.small.toLocaleString()} לשנה)`;
         enclosureSizeSelect.options[1].text = `בינוני (מקסימום ${maxPopulation.medium} פרטים, $${costs.enclosure.medium.toLocaleString()} לשנה)`;
         enclosureSizeSelect.options[2].text = `גדול (מקסימום ${maxPopulation.large} פרטים, $${costs.enclosure.large.toLocaleString()} לשנה)`;
         enclosureQualitySelect.options[0].text = `בסיסית ($${costs.quality.basic.toLocaleString()} לשנה)`;
         enclosureQualitySelect.options[1].text = `טובה ($${costs.quality.good.toLocaleString()} לשנה)`;
         enclosureQualitySelect.options[2].text = `מצוינת ($${costs.quality.excellent.toLocaleString()} לשנה)`;

        // Visual feedback for stat levels (optional - needs more CSS/JS)
        // Example: Change color of health/diversity spans based on value
        if (health < 30) healthSpan.style.color = '#d9534f'; // Red
        else if (health < 70) healthSpan.style.color = '#f0ad4e'; // Orange
        else healthSpan.style.color = '#5cb85c'; // Green

        if (geneticDiversity < 30) geneticDiversitySpan.style.color = '#d9534f'; // Red
        else if (geneticDiversity < 60) geneticDiversitySpan.style.color = '#f0ad4e'; // Orange
        else geneticDiversitySpan.style.color = '#5cb85c'; // Green
    }

    function animateStatChange(element, newValue) {
        const oldValue = parseFloat(element.textContent.replace(/[$,%]/g, ''));
        if (oldValue !== parseFloat(newValue)) { // Only animate if value changed
            element.textContent = newValue; // Update value immediately for display
            element.classList.remove('changed'); // Reset animation
            // Use a small timeout to ensure the class removal registers before adding it back
            requestAnimationFrame(() => {
                 requestAnimationFrame(() => {
                    element.classList.add('changed');
                 });
            });
        }
    }


    function addMessage(text, type = 'info') {
        const li = document.createElement('li');
        li.textContent = `[שנה ${year}] ${text}`;
        li.classList.add(type); // Add class for potential styling (e.g., error, success)
        messageList.prepend(li); // Add to top
         // Keep message list from getting too long
         while (messageList.children.length > 20) {
            messageList.removeChild(messageList.lastChild);
        }
    }

    function triggerAnimation(element, event) {
        element.style.display = 'block';
        // Position the animation near where the event happened or relevant UI element
        // Simple example: center it for now. More complex positioning needs event coordinates.
        element.style.left = '50%';
        element.style.top = '50%';
        element.style.transform = 'translate(-50%, -50%)'; // Center it

        element.classList.remove('popUpFade'); // Reset animation
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                element.classList.add('popUpFade');
                 // Hide after animation
                 element.addEventListener('animationend', function handler() {
                     element.style.display = 'none';
                     element.classList.remove('popUpFade');
                      element.removeEventListener('animationend', handler); // Clean up
                 });
            });
        });
    }


    function buyAnimal(type) {
        const totalPop = population.males + population.females;
        if (budget < costs.animal) {
            addMessage('אין מספיק תקציב לרכישת פרט חדש.', 'warning');
            // Trigger negative money animation
            triggerAnimation(moneyOutAnimation, null);
            return;
        }
        if (totalPop >= maxPopulation[enclosureSizeSelect.value]) {
             addMessage(`לא ניתן לרכוש פרט נוסף, הכלוב מלא (מקסימום ${maxPopulation[enclosureSizeSelect.value]} פרטים).`, 'warning');
             return;
         }

        budget -= costs.animal;
        population[type]++;
        addMessage(`רכשת ${type === 'male' ? 'זכר' : 'נקבה'} חדש תמורת $${costs.animal.toLocaleString()}. תוספת "דם חדש" לאוכלוסייה.`);
        // Adding new blood significantly improves genetic diversity
        geneticDiversity = Math.min(100, geneticDiversity + Math.random() * 8 + 7); // Increased boost
        updateUI();
        triggerAnimation(moneyOutAnimation, null); // Trigger negative money animation
    }

    function calculateAnnualCosts() {
        const enclosureCost = costs.enclosure[enclosureSize] + costs.quality[enclosureQuality];
        const upkeepCost = (population.males + population.females) * costs.upkeepPerAnimal;
        return enclosureCost + upkeepCost;
    }

    function advanceYear() {
        year++;
        const totalPop = population.males + population.females;
        addMessage(`מתחילים שנה ${year}...`);

        // Apply costs
        const annualCost = calculateAnnualCosts();
        budget -= annualCost;
        addMessage(`הוצאות שנתיות על כלוב ותחזוקת חיות: $${annualCost.toLocaleString()}.`);
        triggerAnimation(moneyOutAnimation, null); // Trigger negative money animation

        // Check for game over (bankruptcy)
        if (budget < 0) {
            gameOverMessage.textContent = `התקציב אזל! לא הצלחת לשמור על גן החיות מעל המים. נדרשות החלטות קשות, והמין נכחד בשבי.`;
            gameOverDiv.style.display = 'block';
            disableControls();
            return;
        }

        // Update health
        let healthChange = 0;
        healthChange += healthEffects[enclosureSize];
        healthChange += healthEffects[enclosureQuality];

        // Health penalty for low diversity and overcrowding
        if (geneticDiversity < 60) healthChange += (geneticDiversity - 60) * 0.5; // Negative change if < 60
        if (totalPop > maxPopulation[enclosureSize]) healthChange -= (totalPop - maxPopulation[enclosureSize]) * 2; // Significant penalty for overcrowding

        // Apply some randomness and ensure bounds
        health = Math.max(0, Math.min(100, health + healthChange + (Math.random() - 0.5) * 8)); // Less extreme randomness

         if (totalPop > 0) {
             addMessage(`בריאות האוכלוסייה הממוצעת: ${health.toFixed(1)}%.`);
         }


        // Check for deaths
        let deaths = 0;
        let malesDied = 0;
        let femalesDied = 0;

        if (totalPop > 0) {
             // Death chance increases significantly with low health and critical low diversity
             const healthFactor = Math.max(0, 100 - health) / 100; // 0 at health 100, 1 at health 0
             const diversityFactor = Math.max(0, 50 - geneticDiversity) / 50; // 0 at diversity >= 50, 1 at diversity 0

             const baseProb = naturalDeathChanceBase + healthFactor * 0.1 + diversityFactor * 0.05; // Increased chance based on poor stats
             const overcrowdingProb = totalPop > maxPopulation[enclosureSize] ? (totalPop - maxPopulation[enclosureSize]) * 0.05 : 0; // Additional chance from overcrowding

             for(let i = 0; i < totalPop; i++) {
                if (Math.random() < (baseProb + overcrowdingProb)) {
                     if (Math.random() < population.males / (population.males + population.females)) { // Pick random gender based on current ratio
                         if (population.males > 0) { population.males--; malesDied++; }
                     } else {
                         if (population.females > 0) { population.females--; femalesDied++; }
                     }
                 }
             }
             deaths = malesDied + femalesDied;
        }

        if (deaths > 0) {
            addMessage(`טרגדיה! ${deaths} פרט(ים) מתו השנה עקב מחלה או תנאים ירודים.`, 'warning');
             triggerAnimation(deathAnimation, null); // Trigger death animation
        }


         // Check for game over (population crash)
        if (population.males + population.females < 2 && year > 1 && budget >= 0) { // Need at least 2 to survive/breed, only game over if not already bankrupted
             gameOverMessage.textContent = `אוכלוסיית החיות קטנה מדי (< 2 פרטים)! ללא מספיק פרטים, לא ניתן לקיים תוכנית רבייה בת קיימא והמין נכחד בשבי.`;
            gameOverDiv.style.display = 'block';
            disableControls();
            return;
        } else if (population.males + population.females === 0 && year > 0 && budget >= 0) {
             gameOverMessage.textContent = `כל הפרטים מתו! האוכלוסייה הגיעה ל-0.`;
            gameOverDiv.style.display = 'block';
            disableControls();
            return;
        }


        // Attempt breeding
        let births = 0;
        const currentTotalPop = population.males + population.females; // Use updated pop after deaths
        if (breedingProgramEnabled && population.males > 0 && population.females > 0 && currentTotalPop < maxPopulation[enclosureSize]) {
             const pairs = Math.min(population.males, population.females);
             let breedingSuccessChance = 0.15; // Base success chance per year

             breedingSuccessChance *= breedingChanceFactors[enclosureSize];
             breedingSuccessChance *= breedingChanceFactors[enclosureQuality];
             breedingSuccessChance *= breedingChanceFactors.breedingEnabled;
             if (health < 70) breedingSuccessChance *= breedingChanceFactors.lowHealth; // Penalty if health is moderate/low
             if (geneticDiversity < 70) breedingSuccessChance *= breedingChanceFactors.lowDiversity; // Penalty if diversity is moderate/low

            // Simulate births - chance applies to the *possibility* of births happening, not per pair
            if (Math.random() < breedingSuccessChance) {
                // If breeding is successful, determine how many births occur
                const maxPotentialBirths = maxPopulation[enclosureSize] - currentTotalPop;
                 const numBorn = Math.min(maxPotentialBirths, Math.floor(Math.random() * 3) + 1); // 1-3 offspring, limited by space

                 for (let j = 0; j < numBorn; j++) {
                      if (Math.random() < 0.5) { population.males++; } else { population.females++; }
                      births++;
                 }
            }
        }

        if (births > 0) {
            addMessage(`חדשות טובות! נולדו ${births} גורים חדשים!`, 'success');
            // Breeding within population reduces diversity slowly over time
             geneticDiversity = Math.max(0, geneticDiversity - (births / currentTotalPop) * (50 / geneticDiversity)); // Decay based on births relative to pop, faster if diversity is already low
             triggerAnimation(birthAnimation, null); // Trigger birth animation
        } else if (breedingProgramEnabled && population.males > 0 && population.females > 0 && currentTotalPop < maxPopulation[enclosureSize]) {
             addMessage("למרות מאמצי הרבייה, לא היו לידות השנה.");
        }


         // Genetic diversity natural decay if population is small or not growing well
         if (currentTotalPop > 0) {
             const decayRate = (100 - geneticDiversity) * 0.01 + (100 / currentTotalPop) * 0.2; // Faster decay if diversity is low OR population is very small
              geneticDiversity = Math.max(0, geneticDiversity - decayRate);
         }


         // Health affects diversity slightly long term (positive feedback loop)
         geneticDiversity = Math.min(100, geneticDiversity + (health/100 - 0.5) * 1);


         // Win Condition: Sustain a viable population for a significant period
        const winYears = 15;
        const requiredPop = 12; // Need a decent number of individuals
        const requiredDiversity = 60; // Need reasonable diversity
        const requiredHealth = 75; // Need good health
        const minMales = 3; // Need both sexes
        const minFemales = 3;


        if (year >= winYears && population.males + population.females >= requiredPop && geneticDiversity >= requiredDiversity && health >= requiredHealth && population.males >= minMales && population.females >= minFemales) {
             winMessage.textContent = `ברכות, מנהלים מצוינים! לאחר ${year} שנים של עבודה מסורה, הצלחתם לבנות אוכלוסייה יציבה, בריאה, ובעלת מגוון גנטי חיוני. האוכלוסייה מוכנה פוטנציאלית לשלב הבא - הכנה להחזרה לטבע! הצלחתם להבטיח את עתידו של המין בשבי.`;
             winDiv.style.display = 'block';
             disableControls();
             return;
        }

        // More nuanced loss conditions (e.g., prolonged low stats) - Maybe just warnings suffice for a simpler game
        // if (year > 8 && (geneticDiversity < 15 || health < 15)) {
        //      // Too low for too long
        //      gameOverMessage.textContent = `בריאות ומגוון גנטי נמוכים לאורך זמן הרסו את יכולת ההישרדות והרבייה של האוכלוסייה. המין נכחד בשבי.`;
        //     gameOverDiv.style.display = 'block';
        //     disableControls();
        //     return;
        // }


        updateUI();
    }

    function disableControls() {
        nextYearBtn.disabled = true;
        buyMaleBtn.disabled = true;
        buyFemaleBtn.disabled = true;
        enclosureSizeSelect.disabled = true;
        enclosureQualitySelect.disabled = true;
        breedingProgramCheckbox.disabled = true;
    }


    // Event Listeners
    buyMaleBtn.addEventListener('click', () => buyAnimal('male'));
    buyFemaleBtn.addEventListener('click', () => buyAnimal('female'));
    enclosureSizeSelect.addEventListener('change', (e) => {
        enclosureSize = e.target.value;
        const totalPop = population.males + population.females;
        if (totalPop > maxPopulation[enclosureSize]) {
             addMessage(`אזהרה: גודל הכלוב החדש (${enclosureSize}) קטן מכדי להכיל את כל ${totalPop} הפרטים (מקסימום ${maxPopulation[enclosureSize]}). צפיפות יתר תפגע בבריאות!`, 'warning');
        }
        updateUI(); // Update costs/max pop info display
    });
    enclosureQualitySelect.addEventListener('change', (e) => {
        enclosureQuality = e.target.value;
        updateUI(); // Update costs info display
    });
    breedingProgramCheckbox.addEventListener('change', (e) => {
        breedingProgramEnabled = e.target.checked;
        addMessage(`תוכנית רבייה: ${breedingProgramEnabled ? 'מופעלת' : 'מושהית'}.`);
        updateUI();
    });
    nextYearBtn.addEventListener('click', advanceYear);

     toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר מידע רקע' : 'הצג מידע רקע על שימור';
    });


    // Initial setup
    updateUI();
    addMessage("ברוכים הבאים למשימתכם! הצילו את המין מהכחדה ע"י ניהול נבון של גן החיות. התחילו ברכישת פרטים ראשונים.");

</script>
```