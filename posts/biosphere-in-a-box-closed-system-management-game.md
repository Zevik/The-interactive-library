---
title: "ביוספרה בקופסה: מסע אל לב מערכת סגורה"
english_slug: biosphere-in-a-box-closed-system-management-game
category: "ביולוגיה"
tags: [אקולוגיה, מערכות סגורות, ביוספרה, מחזוריות, איזון סביבתי, סימולציה]
---
# ביוספרה בקופסה: מסע אל לב מערכת סגורה

האם אפשר ליצור עולם חי ויציב בתוך קופסה אטומה? גלו את האתגר המרתק של ניהול ביוספרה זעירה, שבה כל מרכיב תלוי באחר לאורך זמן וללא עזרה מבחוץ.

<div id="game-container">
    <h2>ניהול ביוספרה זעירה</h2>
    <div id="status">
        <p>זמן שחלף: <span id="time">0</span> ימים</p>
        <p>רמת חמצן (O₂): <span id="oxygen">--</span>%</p>
        <p>רמת פחמן דו-חמצני (CO₂): <span id="co2">--</span>%</p>
        <p>זמינות מים: <span id="water">--</span>%</p>
        <p>בריאות המערכת: <span id="health">--</span>%</p>
        <div id="message" class="message"></div>
    </div>

    <div id="controls">
        <p>שנו את הגורמים המרכזיים כדי להשפיע על האיזון:</p>
        <div class="control-group">
            <label for="plants">צמחייה (פוטוסינתזה):</label>
            <input type="range" id="plants" min="10" max="200" value="100">
            <span id="plants-value">100</span> יח'
        </div>
        <div class="control-group">
            <label for="animals">בעלי חיים (נשימה):</label>
            <input type="range" id="animals" min="5" max="100" value="50">
            <span id="animals-value">50</span> יח'
        </div>
        <div class="control-group">
            <label for="decomposition">תהליכי פירוק:</label>
            <input type="range" id="decomposition" min="10" max="200" value="100">
            <span id="decomposition-value">100</span> יח'
        </div>
         <div class="button-group">
            <button id="start-button" class="btn primary">התחל סימולציה</button>
            <button id="reset-button" class="btn secondary">אפס הכל</button>
         </div>
    </div>
</div>

<button id="toggle-explanation" class="btn tertiary">הסבר: מהי מערכת סגורה?</button>

<div id="explanation" style="display: none;">
    <h2>מערכות אקולוגיות סגורות: מדריך מקוצר</h2>
    <p>מערכת אקולוגית סגורה היא כישות עצמאית כמעט לחלוטין. היא לא מחליפה חומרים עם הסביבה החיצונית, למעט אנרגיה (בדרך כלל אור). כדי לשרוד, כל החומרים החיוניים – מים, פחמן, חמצן וחומרי מזון – חייבים לעבור מחזורים אינסופיים בתוך גבולותיה.</p>

    <h3>למה זה מעניין?</h3>
    <ul>
        <li>**הבנת כדור הארץ:** כדור הארץ עצמו הוא ביוספרה גלובלית סגורה לחומר (כמעט) אך פתוחה לאנרגיה. לימוד מערכות קטנות יותר עוזר להבין את המורכבות של הבית הגדול שלנו.</li>
        <li>**קיום בחלל:** פיתוח מערכות סגורות הוא קריטי ליכולת שלנו לקיים מושבות אדם ארוכות טווח מחוץ לכדור הארץ (כמו בפרויקט ביוספרה 2 ההיסטורי).</li>
        <li>**הנדסה אקולוגית:** אתגר תכנון מערכת בת קיימא דורש הבנה עמוקה של האינטראקציות בין אורגניזמים לסביבתם.</li>
    </ul>

    <h3>השחקנים הראשיים במערכת (ובסימולציה זו):</h3>
    <ul>
        <li>**צמחייה (יצרנים):** קולטים אור, CO₂ ומים, ומייצרים חמצן וחומר אורגני דרך פוטוסינתזה. הם הבסיס האנרגטי והמקור העיקרי לחמצן.</li>
        <li>**בעלי חיים (צרכנים):** אוכלים צמחים (או אורגניזמים אחרים בשרשרת המזון, מפשט פה), צורכים חמצן ומשחררים CO₂ ופסולת בתהליך הנשימה.</li>
        <li>**מפרקים (פטריות וחיידקים):** מפרקים חומר אורגני מת (צמחים ובעלי חיים מתים, פסולת) ומחזירים חומרי מזון חיוניים לקרקע/למים, ובכך מאפשרים לצמחים לגדול שוב. הם גם משחררים CO₂.</li>
    </ul>

    <h3>מחזורים חיוניים לשרידה:</h3>
    <p>כדי שהמערכת תישאר מאוזנת, התהליכים חייבים לפעול בהרמוניה:</p>
    <ul>
        <li>**מחזור הפחמן/חמצן:** צמחים קולטים CO₂ ופולטים O₂, בעלי חיים ומפרקים עושים ההפך. האיזון בין פוטוסינתזה לנשימה קריטי.</li>
        <li>**מחזור המים:** אידוי, התעבות, ומשקעים – המים חייבים להישאר במערכת ולהיות זמינים לאורגניזמים.</li>
        <li>**מחזור חומרי המזון:** מפרקים חייבים להחזיר חנקן, זרחן ועוד מהחומר המת לשימוש הצמחים, אחרת הקרקע תתדלדל.</li>
    </ul>

    <h3>למה המערכת יכולה לקרוס?</h3>
    <p>ניהול ביוספרה סגורה דורש איזון עדין להפליא. כשל באחד המחזורים עלול למוטט את כולם:</p>
    <ul>
        <li>**חנק גזי:** יותר מדי נשימה (בעלי חיים/מפרקים רבים מדי) ביחס לפוטוסינתזה (צמחייה מעטה מדי) יכול להוביל לירידת חמצן או עליית CO₂ לרמות קטלניות.</li>
        <li>**הרעלת פסולת:** פירוק איטי מדי או לא יעיל יכול לגרום להצטברות חומרים רעילים או למחסור בחומרי מזון לצמחים.</li>
        <li>**בעיות מים:** מחסור או עודף קיצוני במים.</li>
        <li>**אובדן מינים:** הכחדת קבוצה חיונית (כמו המפרקים!) תשבש את כל המערכת.</li>
    </ul>
    <p>המשימה שלכם היא לשמור על האיזון הזה לאורך זמן. שימו לב לערכים ולבריאות המערכת, והתאימו את אוכלוסיות הצמחים, החיות והמפרקים באמצעות המחוונים.</p>
</div>

<style>
    :root {
        --primary-color: #4CAF50; /* Green */
        --primary-dark-color: #45a049;
        --secondary-color: #f44336; /* Red */
        --secondary-dark-color: #d32f2f;
        --tertiary-color: #008CBA; /* Blue */
        --tertiary-dark-color: #005f73;
        --background-light: #e8f5e9; /* Very light green */
        --background-medium: #c8e6c9; /* Light green */
        --text-color-dark: #333;
        --text-color-medium: #555;
        --border-color: #a5d6a7; /* Light green border */
        --box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --border-radius: 12px;
        --font-family: 'Arial', sans-serif; /* Keep Arial for Hebrew compatibility, or link a font */
    }

    body {
        font-family: var(--font-family);
        line-height: 1.6;
        color: var(--text-color-dark);
        background: linear-gradient(to bottom right, #e8f5e9, #c8e6c9); /* Subtle gradient background */
        padding: 20px;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: var(--text-color-medium);
        text-align: center;
        margin-bottom: 20px;
    }

    #game-container {
        border: 1px solid var(--border-color);
        padding: 30px;
        max-width: 650px;
        margin: 20px auto;
        background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white */
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        position: relative; /* Needed for potential animations */
    }

    #status {
        margin-bottom: 25px;
        padding: 15px;
        border-bottom: 1px solid var(--border-color);
        background-color: var(--background-light);
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    #status p {
        margin: 8px 0;
        font-size: 1.1em;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    #status span {
        font-weight: bold;
        min-width: 50px; /* Ensure space for value */
        text-align: left; /* Align numbers left for consistency */
        transition: color 0.3s ease, transform 0.1s ease; /* Smooth color change and slight pulse */
    }

    /* Status color indicators */
    #oxygen-status.ok, #co2-status.ok, #water-status.ok, #health-status.ok { color: green; }
    #oxygen-status.warn, #co2-status.warn, #water-status.warn, #health-status.warn { color: orange; }
    #oxygen-status.critical, #co2-status.critical, #water-status.critical, #health-status.critical { color: red; animation: pulse-red 1s infinite; }

    @keyframes pulse-red {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }


    #controls {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid var(--border-color);
    }

    .control-group {
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .control-group label {
        display: inline-block;
        width: 150px; /* Wider label for Hebrew */
        margin-bottom: 5px; /* Space below label on wrap */
        font-weight: bold;
        color: var(--text-color-medium);
    }

     .control-group input[type="range"] {
        flex-grow: 1; /* Take available space */
        margin: 0 15px; /* Space around slider */
        -webkit-appearance: none; /* Remove default style */
        appearance: none;
        height: 8px;
        background: var(--background-medium);
        outline: none;
        border-radius: 5px;
        transition: background 0.2s ease-in-out;
     }

     .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid white;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
        transition: background 0.2s ease-in-out;
     }
      .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid white;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
        transition: background 0.2s ease-in-out;
     }

      .control-group input[type="range"]:hover::-webkit-slider-thumb { background: var(--primary-dark-color); }
      .control-group input[type="range"]:hover::-moz-range-thumb { background: var(--primary-dark-color); }


     .control-group span {
         display: inline-block;
         width: 50px; /* Space for value */
         text-align: left; /* Align numbers left */
         font-weight: bold;
         color: var(--text-color-dark);
     }

    .button-group {
        margin-top: 25px;
        text-align: center;
    }

    .btn {
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.2s ease, opacity 0.2s ease;
        margin: 0 10px;
    }

    .btn.primary {
        background-color: var(--primary-color);
        color: white;
    }
    .btn.primary:hover:not(:disabled) {
        background-color: var(--primary-dark-color);
    }

     .btn.secondary {
         background-color: var(--secondary-color);
         color: white;
     }
     .btn.secondary:hover:not(:disabled) {
         background-color: var(--secondary-dark-color);
     }

     .btn.tertiary {
         display: block; /* Make button a block element */
         width: fit-content; /* Shrink to content width */
         margin: 20px auto; /* Center the button */
         background-color: var(--tertiary-color);
         color: white;
     }
    .btn.tertiary:hover:not(:disabled) {
        background-color: var(--tertiary-dark-color);
    }

    .btn:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }


    .message {
        margin-top: 20px;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space */
        opacity: 0; /* Hide initially */
        transition: opacity 0.3s ease-in-out, background-color 0.3s ease;
    }

    .message.show { opacity: 1; } /* Show when class is added */


    .message.success {
        background-color: #d4edda; /* Light green */
        color: #155724; /* Dark green */
        border: 1px solid #c3e6cb;
    }

    .message.warning {
        background-color: #fff3cd; /* Light yellow */
        color: #856404; /* Dark yellow */
        border: 1px solid #ffeeba;
    }

    .message.error {
        background-color: #f8d7da; /* Light red */
        color: #721c24; /* Dark red */
        border: 1px solid #f5c6cb;
    }

    #explanation {
        margin: 20px auto;
        padding: 30px;
        max-width: 650px;
        border: 1px solid var(--border-color);
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        direction: rtl;
        text-align: right;
        transition: max-height 0.5s ease-in-out, opacity 0.5s ease-in-out;
        overflow: hidden;
        max-height: 0; /* For collapse animation */
        opacity: 0; /* For fade animation */
        padding-top: 0; /* Remove padding when collapsed */
        padding-bottom: 0; /* Remove padding when collapsed */
    }

    #explanation.show {
        max-height: 2000px; /* Sufficiently large value */
        opacity: 1;
        padding-top: 30px; /* Restore padding */
        padding-bottom: 30px; /* Restore padding */
    }


    #explanation h2 {
        margin-top: 0; /* Adjust margin after collapse transition */
        margin-bottom: 15px;
        color: var(--text-color-dark);
    }

    #explanation h3 {
        margin-top: 25px;
        margin-bottom: 10px;
        color: var(--text-color-medium);
    }

    #explanation p, #explanation ul {
        line-height: 1.7;
        margin-bottom: 15px;
        color: var(--text-color-dark);
    }

    #explanation ul {
        padding-right: 25px; /* Adjust padding for RTL list markers */
    }

     #explanation li {
         margin-bottom: 10px;
         color: var(--text-color-dark);
     }

</style>

<script>
    let time = 0;
    let oxygen = 21; // Starting like Earth's atmosphere (%)
    let co2 = 0.04; // Starting approx Earth's atmosphere (%)
    let water = 80; // Arbitrary scale % (represents availability, not total volume)
    let systemHealth = 100; // Arbitrary %

    // Population/Component levels - influenced by sliders & simulation
    let plantMass = 100; // Units
    let animalPopulation = 50; // Units
    let decomposerLevel = 100; // Units (represents effectiveness/biomass)

    let gameInterval;
    let isRunning = false;

    // DOM Elements
    const timeDisplay = document.getElementById('time');
    const oxygenDisplay = document.getElementById('oxygen');
    const co2Display = document.getElementById('co2');
    const waterDisplay = document.getElementById('water');
    const healthDisplay = document.getElementById('health');
    const messageDisplay = document.getElementById('message');

    const plantsSlider = document.getElementById('plants');
    const animalsSlider = document.getElementById('animals');
    const decompositionSlider = document.getElementById('decomposition');

    const plantsValueSpan = document.getElementById('plants-value');
    const animalsValueSpan = document.getElementById('animals-value');
    const decompositionValueSpan = document.getElementById('decomposition-value');

    const startButton = document.getElementById('start-button');
    const resetButton = document.getElementById('reset-button');
    const explanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Keep track of slider values set by user vs values changed by simulation
    let userPlants = 100;
    let userAnimals = 50;
    let userDecomposition = 100;


    // Event Listeners for Sliders (user input)
    plantsSlider.addEventListener('input', (e) => {
        userPlants = parseInt(e.target.value);
        plantsValueSpan.textContent = userPlants;
        // If simulation is running, this input *influences* the population, but doesn't set it directly.
        // For this simpler model, we'll just set the target/influence level.
        // A more complex model might treat sliders as 'carrying capacity' or 'intervention'.
        // Let's make the sliders represent a desired level the system *tries* to reach.
        // However, the current simulateStep directly modifies plantMass etc. based on environment.
        // To preserve structure but add player influence: Let sliders act as 'environmental adjustment'.
        // E.g., increasing plants slider boosts plant growth rate for a while.
        // Or, simpler: Sliders set the *actual* population/level directly on user input, overriding simulation.
        // This is less realistic but fits the current structure better for a "management" feel.
        // Let's stick to sliders setting values directly, as in the original, but update the value span on input.
         plantMass = userPlants; // Sliders override sim dynamics for simplicity as requested by original structure
         updateStatusDisplay(); // Update immediately when user changes slider
    });
     animalsSlider.addEventListener('input', (e) => {
        userAnimals = parseInt(e.target.value);
        animalsValueSpan.textContent = userAnimals;
        animalPopulation = userAnimals;
        updateStatusDisplay();
    });
     decompositionSlider.addEventListener('input', (e) => {
        userDecomposition = parseInt(e.target.value);
        decompositionValueSpan.textContent = userDecomposition;
        decomposerLevel = userDecomposition;
        updateStatusDisplay();
    });


    // Update display elements and add visual feedback
    function updateStatusDisplay() {
        timeDisplay.textContent = time;
        // Use specific spans for color/animation
        oxygenDisplay.innerHTML = `<span id="oxygen-status">${oxygen.toFixed(2)}</span>`;
        co2Display.innerHTML = `<span id="co2-status">${co2.toFixed(2)}</span>`;
        waterDisplay.innerHTML = `<span id="water-status">${water.toFixed(1)}</span>`;
        healthDisplay.innerHTML = `<span id="health-status">${systemHealth.toFixed(0)}</span>%`;

        // Update status colors based on levels
        const oxygenStatusSpan = document.getElementById('oxygen-status');
        const co2StatusSpan = document.getElementById('co2-status');
        const waterStatusSpan = document.getElementById('water-status');
        const healthStatusSpan = document.getElementById('health-status');

        oxygenStatusSpan.className = (oxygen > 18 && oxygen < 25) ? 'ok' : ((oxygen <= 10 || oxygen >= 30) ? 'critical' : 'warn');
        co2StatusSpan.className = (co2 > 0.03 && co2 < 0.1) ? 'ok' : ((co2 >= 0.5 || co2 <= 0.01) ? 'critical' : 'warn');
        waterStatusSpan.className = (water > 30 && water < 95) ? 'ok' : ((water <= 15 || water >= 98) ? 'critical' : 'warn');
        healthStatusSpan.className = (systemHealth > 70) ? 'ok' : (systemHealth > 40 ? 'warn' : 'critical');

        // Update slider value spans based on actual simulation value (if different from user setting,
        // but since sliders override, they should be the same)
        plantsValueSpan.textContent = Math.round(plantMass);
        animalsValueSpan.textContent = Math.round(animalPopulation);
        decompositionValueSpan.textContent = Math.round(decomposerLevel);
    }

    // Check system conditions and update health/messages
    function checkConditions() {
        let msg = '';
        let type = ''; // success, warning, error
        let healthChange = 0; // Change per step

        // Evaluate critical conditions first
        if (oxygen < 12 || co2 > 0.6 || water < 10 || water > 99 || systemHealth <= 10) {
             msg = 'המערכת במצב קריטי!'; type = 'error'; healthChange -= 8;
        } else if (oxygen < 18 || oxygen > 25 || co2 > 0.3 || co2 < 0.02 || water < 20 || water > 95 || plantMass < 30 || animalPopulation < 15 || decomposerLevel < 30 || systemHealth <= 40) {
             msg = 'המערכת במתח גבוה. נדרש איזון.'; type = type === 'error' ? 'error' : 'warning'; healthChange -= 4;
        } else if (plantMass < 50 || animalPopulation < 20 || decomposerLevel < 50) {
             msg = 'אוכלוסיות מסוימות קטנות מדי.'; type = type === 'error' ? 'error' : 'warning'; healthChange -= 2;
        }
        else {
            msg = 'המערכת יציבה ומשגשגת.';
            type = 'success';
            healthChange += 2; // Small health boost for stability
        }

        // Adjust health
        systemHealth = Math.max(0, Math.min(100, systemHealth + healthChange)); // Clamp health between 0 and 100

        // Update message display with potential animation
        messageDisplay.textContent = msg;
        messageDisplay.className = `message ${type} show`;


        // Check for Game Over conditions
        if (systemHealth <= 0 || oxygen <= 5 || co2 >= 1.0 || water <= 5 || water >= 100) {
             gameOver('המערכת קרסה עקב חוסר איזון קיצוני!');
        } else if (time >= 730) { // Survive for 2 years (730 days)
             gameOver('הצלחת לשמור על המערכת יציבה במשך שנתיים! ניהול מעולה!');
        } else if (time >= 365 && time < 730 && systemHealth > 60) {
             // Intermediate success message
              if (!messageDisplay.textContent.includes("שנה")) { // Avoid repeating message
                 messageDisplay.textContent = 'המערכת שרדה שנה שלמה! המשך לשמור על האיזון.';
                 messageDisplay.className = 'message success show';
              }
        }
    }

    // The core simulation loop
    function simulateStep() {
        // --- Core Biological Processes (simplified) ---
        // These are influenced by current levels, but the sliders override the *population* values
        // This makes the game about setting the *right levels* rather than dynamic population control by environment
        // We'll calculate changes based on *slider* values for simplicity, matching original intent.

        // Base Respiration: O2 consumed, CO2 produced by all life
        const respirationRate = (plantMass * 0.05) + (animalPopulation * 0.2) + (decomposerLevel * 0.03);
        oxygen -= respirationRate * 0.005; // Scale effect
        co2 += respirationRate * 0.003; // Scale effect

        // Photosynthesis: CO2 consumed, O2 produced by plants
        // Rate depends on plant mass, light (constant), water, and CO2 availability
        // Less photosynthesis if CO2 or Water are very low
        const lightFactor = 1.0; // Assume constant light
        const waterFactor = Math.max(0, Math.min(1, (water - 10) / 80)); // Scale water availability influence (low below 10%, high above 90%)
        const co2Factor = Math.max(0, Math.min(1, (co2 - 0.01) / 0.5)); // Scale CO2 availability influence (low below 0.01%, high above 0.5%)
        const photosynthesisRate = plantMass * 0.15 * lightFactor * waterFactor * co2Factor;
        oxygen += photosynthesisRate * 0.01; // Scale effect
        co2 -= photosynthesisRate * 0.008; // Scale effect

         // Decomposition: Processes waste, recycles nutrients. Affected by decomposer level, water, oxygen.
         // Simplified: Low decomposition effectiveness impacts health and prevents nutrient recycling.
         const wasteGenerated = (plantMass * 0.03) + (animalPopulation * 0.08);
         const decompositionEffectiveness = decomposerLevel * 0.05 * waterFactor * (oxygen > 10 ? 1 : 0.5); // Decomposition needs water and some oxygen

         // Simulate nutrient availability indirectly via health
         // If decomposition isn't keeping up with waste, health suffers (nutrients aren't recycled, toxins build up)
         if (decompositionEffectiveness < wasteGenerated * 0.9) {
              systemHealth -= (wasteGenerated * 0.9 - decompositionEffectiveness) * 0.2; // More waste/less decomp -> health drop
         } else if (decompositionEffectiveness > wasteGenerated * 1.1) {
              systemHealth += (decompositionEffectiveness - wasteGenerated * 1.1) * 0.08; // Good decomp -> health boost
         }

         // Water Cycle: Simple loss/gain model within closed system (evaporation/condensation)
         // Net effect depends on plants (transpiration), decomposers (soil health/retention), and overall health
         water -= 0.3; // Base slow loss/inefficiency
         water += plantMass * 0.005; // Plants return some water vapor
         water += decomposerLevel * 0.002; // Decomposers help soil retain water
         // Add slight random fluctuation to water cycle
         water += (Math.random() - 0.5) * 0.5; // Small random +/- 0.25 per step

        // --- Clamping Values ---
        oxygen = Math.max(0, Math.min(40, oxygen)); // Don't let levels get absurdly high or negative
        co2 = Math.max(0, Math.min(15, co2));
        water = Math.max(0, Math.min(100, water));
        systemHealth = Math.max(0, Math.min(100, systemHealth)); // Health is already clamped in checkConditions, but double-check

        // --- Population/Component Dynamics (Simplified, based on Sliders as Target) ---
        // In this model, the sliders *set* the levels. Simulation changes are only on gases/water/health.
        // The interaction is: User sets levels -> environment changes -> user adjusts levels based on environment feedback.
        // If we wanted the environment to control population:
        // plantMass += growthRate(env) - deathRate(env);
        // animalPopulation += birthRate(env, food) - deathRate(env);
        // decomposerLevel += growthRate(env, waste) - deathRate(env);
        // and sliders would be 'fertilizer', 'add animals', 'add microbes'.
        // Sticking to the original structure: Sliders ARE the levels. No internal population dynamics here.

        time++;
        checkConditions(); // Check state and update health/message
        updateStatusDisplay(); // Update UI with new values
    }

    function startGame() {
        if (!isRunning) {
            isRunning = true;
            startButton.textContent = 'הסימולציה רצה...';
            startButton.disabled = true;
            resetButton.disabled = false; // Enable reset once started
            plantsSlider.disabled = false;
            animalsSlider.disabled = false;
            decompositionSlider.disabled = false;
            messageDisplay.textContent = 'הסימולציה החלה. צפו בשינויים!';
            messageDisplay.className = 'message success show'; // Show initial message
            gameInterval = setInterval(simulateStep, 200); // Simulate a step every 200ms
        }
    }

    function gameOver(message) {
        clearInterval(gameInterval);
        isRunning = false;
        startButton.textContent = 'סימולציה הסתיימה';
        startButton.disabled = true;
        resetButton.disabled = false; // Ensure reset is possible
        plantsSlider.disabled = true; // Disable controls after game over
        animalsSlider.disabled = true;
        decompositionSlider.disabled = true;

        messageDisplay.textContent = message;
        messageDisplay.className = `message ${message.includes('קרסה') ? 'error' : 'success'} show`;
    }

    function resetGame() {
        clearInterval(gameInterval);
        isRunning = false;
        time = 0;
        oxygen = 21;
        co2 = 0.04;
        water = 80;
        systemHealth = 100;

        // Reset populations to initial default values (and update user values)
        plantMass = 100; userPlants = 100;
        animalPopulation = 50; userAnimals = 50;
        decomposerLevel = 100; userDecomposition = 100;

        plantsSlider.value = plantMass;
        animalsSlider.value = animalPopulation;
        decompositionSlider.value = decomposerLevel;

        plantsValueSpan.textContent = plantMass;
        animalsValueSpan.textContent = animalPopulation;
        decompositionValueSpan.textContent = decomposerLevel;

        startButton.textContent = 'התחל סימולציה';
        startButton.disabled = false;
        resetButton.disabled = true; // Disable reset until started again
        plantsSlider.disabled = true; // Disable sliders until game starts
        animalsSlider.disabled = true;
        decompositionSlider.disabled = true;

        messageDisplay.textContent = 'מוכן להתחלה.';
        messageDisplay.className = 'message'; // Clear message class and hide

        updateStatusDisplay(); // Display initial state
    }

    // Initial state setup on page load
    resetGame(); // Call reset to set initial state and disable controls properly


    startButton.addEventListener('click', startGame);
    resetButton.addEventListener('click', resetGame);

    // Explanation button toggle with animation
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.maxHeight === '0px' || explanationDiv.style.display === 'none';
        if (isHidden) {
            explanationDiv.style.display = 'block'; // Make block before animating height
            // Use a timeout to allow display property to take effect before transition
            setTimeout(() => {
                 explanationDiv.classList.add('show');
                 explanationButton.textContent = 'הסתר הסבר';
            }, 10); // Small delay
        } else {
            explanationDiv.classList.remove('show');
            explanationButton.textContent = 'הסבר: מהי מערכת סגורה?';
            // Use a timeout matching transition duration before setting display to none
            setTimeout(() => {
                 explanationDiv.style.display = 'none';
            }, 500); // Match CSS transition duration
        }
    });

    // Ensure explanation is collapsed initially even if CSS display:none is overridden
    explanationDiv.style.maxHeight = '0px';
    explanationDiv.style.opacity = '0';
    explanationDiv.style.display = 'none'; // Ensure it's hidden visually and by layout

</script>
```