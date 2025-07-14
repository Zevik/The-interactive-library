---
title: "מקלט אקלימי: סימולטור הישרדות מינים"
english_slug: climate-refuge-building-species-survival-model
category: "אקולוגיה"
tags:
  - שינויי אקלים
  - אקולוגיה
  - שימור טבע
  - מגוון ביולוגי
  - מידול
  - סימולציה
---
# מקלט אקלימי: סימולטור הישרדות מינים

האם דוב הקוטב או צמח נדיר בהר ישרדו את ההתחממות המואצת? מה הופך אזור מסוים ל"מקלט" שיכול להגן על המגוון הביולוגי גם בתנאים קיצוניים? היכנסו למעבדת הסימולציה הווירטואלית ובנו עולמות ותרחישים כדי לחשוף את סודות ההישרדות ולהבין כיצד חוקרים מתכננים את עתיד החיים על כדור הארץ.

<div class="app-container">
    <div class="controls-panel">
        <h2>כלי הסימולציה</h2>
        <div class="param-section">
            <h3>מאפייני המין</h3>
            <label for="tempSensitivity">רגישות לחום (טמפרטורה מקסימלית לסבילות):</label>
            <input type="range" id="tempSensitivity" min="20" max="40" value="30" step="0.5"><span id="tempSensitivityValue">30.0°C</span><br>
            <label for="dispersalAbility">כושר תנועה (מקסימום תאים לצעד):</label>
            <input type="range" id="dispersalAbility" min="0" max="5" value="1"><span id="dispersalAbilityValue">1 תא/שלב</span><br>
        </div>
        <div class="param-section">
            <h3>מאפייני הנוף</h3>
            <label for="landscapeVariation">שונות טופוגרפית (השפעת הגובה על הטמפרטורה):</label>
            <input type="range" id="landscapeVariation" min="0" max="15" value="5" step="0.5"><span id="landscapeVariationValue">5.0 יחידות</span><br>
            <label for="habitatDiversity">מגוון בתי גידול (שיעור אזורים לא מתאימים):</label>
            <input type="range" id="habitatDiversity" min="0" max="70" value="20"><span id="habitatDiversityValue">20% לא מתאים</span><br>
            <label for="obstacles">מחסומים בנוף (שטחים בלתי עבירים):</label>
            <input type="range" id="obstacles" min="0" max="40" value="10"><span id="obstaclesValue">10% חסום</span><br>
        </div>
        <div class="param-section">
            <h3>שינויי אקלים</h3>
            <label for="warmingRate">קצב התחממות (מעלות לשלב זמן):</label>
            <input type="range" id="warmingRate" min="0" max="1.5" step="0.05" value="0.5"><span id="warmingRateValue">0.50°C/שלב</span><br>
            <label for="extremeEvents">תדירות אירועי קיצון (סיכוי לכשלון זמני בתא):</label>
            <input type="range" id="extremeEvents" min="0" max="0.5" step="0.01" value="0.1"><span id="extremeEventsValue">10% סיכוי</span><br>
        </div>
        <button id="runSimulation">הפעל סימולציה</button>
        <button id="resetSimulation">אפס</button>
        <div class="simulation-stats">
             <p>שלב סימולציה: <span id="currentStepDisplay">0</span> מתוך <span id="maxStepsDisplay"></span></p>
             <p>טמפרטורה גלובלית: <span id="currentTempDisplay"></span> °C</p>
             <p>תאים מאוכלסים: <span id="presentCellsDisplay">0</span></p>
             <p id="refugeCountDisplay" style="display: none;">מקלטים פוטנציאליים: <span id="refugeCellsDisplay">0</span></p>
        </div>
    </div>
    <div class="simulation-area">
        <div class="map-legend">
            <span class="legend-item present-color"></span> נוכחות מין
            <span class="legend-item extinct-color"></span> נכחד מקומית / לא הגיע
            <span class="legend-item refuge-color"></span> מקלט אקלימי פוטנציאלי
            <span class="legend-item unsuitable-obstacle-color"></span> בית גידול לא מתאים / מחסום
            <span class="legend-item empty-color"></span> שטח ריק
        </div>
        <div id="simulationMap" class="simulation-map">
            <!-- The grid will be generated here by JS -->
        </div>
    </div>
</div>

<button id="toggleExplanation" class="toggle-button">הצג הסבר מעמיק</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: מקלטים אקלימיים ומודלים להישרדות מינים</h2>

    <h3>מהו בעצם "מקלט אקלימי"?</h3>
    דמיינו עולם שהולך ומתחמם במהירות. רוב השטחים הופכים פחות ופחות נוחים לחיים, אבל אזורים מסוימים, כמו "איים" בתוך הים המשתנה הזה, מצליחים לשמור על תנאים יציבים יחסית. אלו הם ה"מקלטים האקלימיים". הם יכולים להיות הרים גבוהים, עמקים עמוקים, יערות צפופים או אפילו מקווי מים תת-קרקעיים. המשותף להם הוא שהם מציעים מגוון מיקרו-אקלימים קרובים זה לזה, או פשוט מוגנים פיזית מהשינויים הגדולים המתרחשים בסביבתם.

    <h3>מדוע מקלטים אקלימיים קריטיים להישרדות מינים בעידן שינויי האקלים?</h3>
    שינויי האקלים המודרניים כל כך מהירים, שמינים רבים (בעיקר צמחים ובעלי חיים בעלי כושר תנועה נמוך) לא מספיקים להסתגל או לנדוד למקומות מתאימים יותר. מקלטים אקלימיים מספקים להם הזדמנות פז: להישאר באזור שנותר מתאים, לשרוד את "גל החום", ומהם - אולי בעתיד - להתפשט שוב לשטחים שהפכו מתאימים מחדש. הם למעשה שומרים על ה"זרעים" (תרתי משמע) של המגוון הביולוגי.

    <h3>אילו מאפיינים סביבתיים יוצרים מקלט יעיל?</h3>
    הטופוגרפיה משחקת תפקיד ענק. אזורים הרריים, למשל, מאפשרים למינים "לטפס" או "לרדת" במדרון כדי למצוא את טווח הטמפרטורות המועדף עליהם. אזורים עם מקורות מים יציבים, סוגי קרקע מגוונים (שמשפיעים על המיקרו-אקלים המקומי), או כאלה המוגנים פיזית (כמו צוקים או קניונים) יכולים להציע יציבות רבה יותר מפני שינויי טמפרטורה או משקעים.

    <h3>איך מאפייני המין משפיעים על סיכוייו למצוא ולהשתמש במקלט?</h3>
    לא כל מין "מתאים" למקלט באותה מידה.
    *   **כושר תנועה (פיזור):** מינים שיכולים לנוע למרחקים גדולים יותר (כמו ציפורים או זרעים שמתפזרים ברוח) יצליחו להגיע למקלטים פוטנציאליים רחוקים. מינים נייחים או בעלי תנועה מוגבלת תלויים במקלטים קרובים.
    *   **רגישות לתנאים:** מינים עם טווח סבילות רחב לתנאי סביבה (למשל, טווח טמפרטורות גדול שבו הם יכולים לשרוד) יצליחו לשרוד גם בתוך מקלט שהתנאים בו משתנים מעט, או אפילו בשטחים סביב המקלט.
    *   **דרישות בית גידול ספציפיות:** מינים התלויים בסוג קרקע מסוים, צמח פונדקאי יחיד או תנאי תאורה ספציפיים, יהיו מוגבלים יותר ביכולתם להתקיים במקלט, גם אם הטמפרטורה מתאימה.

    <h3>כיצד מודלים כמו זה עוזרים לנו?</h3>
    מודלים אקולוגיים וגנטיים הם כלי חיזוי חיוניים. הם מאפשרים לנו:
    1.  **לשלב מידע:** לקחת נתונים על דרישות המין, מאפייני הנוף, וכיצד האקלים צפוי להשתנות.
    2.  **לצפות תרחישים:** להריץ סימולציות שמראות היכן סביר שהמין יוכל לשרוד בתנאים עתידיים שונים.
    3.  **לאתר מקלטים פוטנציאליים:** לזהות אזורים שמופיעים במודל כבעלי סיכוי גבוה לשמר אוכלוסיות.
    4.  **לתכנן אסטרטגיות שימור:** להבין אילו אזורים חשוב לשמר, היכן כדאי לשקם בתי גידול, והיכן ליצור "מסדרונות ירוקים" שיאפשרו תנועה בין שטחים מתאימים.

    <h3>מה המגבלות של המודלים הללו?</h3>
    המודל שבו התנסיתם פשטני למדי, וגם המודלים המשוכללים ביותר הם ייצוגים חלקיים של המציאות המורכבת. הם לא תמיד כוללים את כל הגורמים: יחסי גומלין בין מינים (תחרות, טריפה), השפעת מחלות, שינויים בשימושי קרקע שאינם קשורים לאקלים, והשפעות גנטיות בטווח הארוך. לכן, תוצאות מודלים הן תמיד כלי עזר שימושי, נקודת מוצא למחקר ותכנון, אך דורשות אימות ובדיקה מעמיקה בשטח.

</div>

<style>
    /* כל סגנונות ה-CSS מרוכזים כאן בלבד */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
        background-color: #f0f4f7;
    }

    h1, h2, h3 {
        color: #2c3e50;
    }

    .app-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    .controls-panel {
        flex: 1 1 300px;
        min-width: 280px;
        padding: 20px;
        background-color: #ecf0f1;
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
    }

    .param-section {
        margin-bottom: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #bdc3c7;
    }
    .param-section:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    .controls-panel label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        font-size: 0.95em;
        color: #34495e;
    }

    .controls-panel input[type="range"] {
        display: inline-block;
        width: calc(100% - 80px); /* Adjust width to accommodate span */
        margin-left: 15px;
        vertical-align: middle;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #bdc3c7;
        outline: none;
        opacity: 0.7;
        -webkit-transition: .2s;
        transition: opacity .2s;
        border-radius: 5px;
    }
     .controls-panel input[type="range"]:hover {
        opacity: 1;
     }
      .controls-panel input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         border-radius: 50%;
         background: #3498db;
         cursor: pointer;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
      }
      .controls-panel input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         border-radius: 50%;
         background: #3498db;
         cursor: pointer;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
      }

    .controls-panel span {
        display: inline-block;
        width: 60px; /* Fixed width for value display */
        text-align: left;
        font-size: 0.9em;
        color: #555;
        vertical-align: middle;
    }

    button {
        display: block; /* Make buttons block elements */
        width: 100%; /* Full width */
        margin-top: 15px; /* More space */
        padding: 12px 20px; /* Larger padding */
        background-color: #3498db; /* Primary button color */
        color: white;
        border: none;
        border-radius: 6px; /* Slightly larger radius */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        text-align: center;
    }
    button:hover:not(:disabled) {
        background-color: #2980b9;
    }
    button:disabled {
         background-color: #bdc3c7;
         cursor: not-allowed;
         opacity: 0.6;
    }

     #resetSimulation {
        background-color: #e74c3c; /* Danger color */
        margin-bottom: 20px;
     }
     #resetSimulation:hover:not(:disabled) {
         background-color: #c0392b;
     }

    .simulation-stats {
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px solid #bdc3c7;
        font-size: 1em;
        color: #34495e;
    }
    .simulation-stats p {
        margin: 8px 0;
        display: flex;
        justify-content: space-between;
    }
     .simulation-stats span {
         font-weight: normal;
         color: #555;
     }


    .simulation-area {
        flex: 2 1 500px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .map-legend {
        display: flex;
        flex-wrap: wrap;
        gap: 15px 25px; /* Increased gap */
        margin-bottom: 20px; /* More space */
        font-size: 0.95em;
        color: #34495e;
    }
    .legend-item {
         display: inline-block;
         width: 18px;
         height: 18px;
         border: 1px solid rgba(0, 0, 0, 0.1); /* Subtle border */
         vertical-align: middle;
         border-radius: 3px;
         box-shadow: inset 0 0 3px rgba(0,0,0,0.1);
    }
     .present-color { background-color: #2ecc71; } /* Green */
     .extinct-color { background-color: #e74c3c; } /* Red */
     .refuge-color { background-color: #3498db; } /* Blue */
     .unsuitable-obstacle-color { background-color: #7f8c8d; } /* Gray */
     .empty-color { background-color: #ecf0f1; border-color: #bdc3c7;} /* Light Gray */


    .simulation-map {
        display: grid;
        border: 1px solid #bdc3c7; /* Grid border */
        gap: 1px; /* Grid line thickness */
        background-color: #bdc3c7; /* Grid lines color */
        /* Dynamic size set by JS based on mapSize */
    }

    .map-cell {
        width: 20px; /* Fixed cell size */
        height: 20px;
        box-sizing: border-box;
        transition: background-color 0.4s ease, box-shadow 0.4s ease; /* Smooth transitions */
        position: relative; /* For potential future animations */
    }

    /* Dynamic classes for cell states */
    .map-cell.empty { background-color: #ecf0f1; } /* Light Gray */
    .map-cell.unsuitable, .map-cell.obstacle { background-color: #7f8c8d; } /* Gray */
    .map-cell.present { background-color: #2ecc71; } /* Green */
    .map-cell.extinct { background-color: #e74c3c; } /* Red */
    .map-cell.refuge { background-color: #3498db; } /* Blue */

     /* Optional: Add a subtle pulse animation for new presence */
    /* .map-cell.newly-present {
        animation: pulse-green 0.8s ease-out forwards;
    }
     @keyframes pulse-green {
         0% { background-color: #ecf0f1; transform: scale(0.9); }
         50% { background-color: #2ecc71; transform: scale(1.05); }
         100% { background-color: #2ecc71; transform: scale(1); }
     } */


    #explanation {
        margin-top: 25px;
        padding: 25px;
        border: 1px solid #bdc3c7;
        border-radius: 8px;
        background-color: #ecf0f1;
        line-height: 1.7;
    }
    #explanation h2, #explanation h3 {
        color: #2c3e50;
        margin-bottom: 15px;
    }
     #explanation p {
         margin-bottom: 1em;
     }
      #explanation strong {
          color: #34495e;
      }


     .toggle-button {
         margin-top: 20px;
         display: block;
         width: fit-content;
         padding: 10px 20px;
         background-color: #95a5a6; /* Muted color for toggle */
         color: white;
         border: none;
         border-radius: 6px;
         cursor: pointer;
         font-size: 1em;
         transition: background-color 0.3s ease;
     }
      .toggle-button:hover {
          background-color: #7f8c8d;
      }


     /* Responsive adjustments */
     @media (max-width: 900px) {
         .app-container {
             flex-direction: column;
             gap: 20px;
             padding: 15px;
         }
         .controls-panel, .simulation-area {
             flex-basis: auto;
             width: 100%;
             padding: 15px;
         }
         .map-legend {
             flex-direction: column;
             gap: 8px;
             align-items: flex-start;
         }
          .controls-panel input[type="range"] {
              width: calc(100% - 70px);
              margin-left: 10px;
          }
          .controls-panel span {
              width: 60px;
          }

     }

     @media (max-width: 400px) {
          .map-cell {
              width: 15px;
              height: 15px;
          }
          .map-legend {
              font-size: 0.9em;
          }
          .legend-item {
              width: 15px;
              height: 15px;
          }
     }


</style>

<script>
    // כל קוד ה-JavaScript מרוכז כאן בלבד
    const mapSize = 35; // Slightly larger map for more detail
    const mapElement = document.getElementById('simulationMap');
    const runButton = document.getElementById('runSimulation');
    const resetButton = document.getElementById('resetSimulation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    const tempSensitivityInput = document.getElementById('tempSensitivity');
    const tempSensitivityValueSpan = document.getElementById('tempSensitivityValue');
    const dispersalAbilityInput = document.getElementById('dispersalAbility');
    const dispersalAbilityValueSpan = document.getElementById('dispersalAbilityValue');
    const landscapeVariationInput = document.getElementById('landscapeVariation');
    const landscapeVariationValueSpan = document.getElementById('landscapeVariationValue');
    const habitatDiversityInput = document.getElementById('habitatDiversity');
    const habitatDiversityValueSpan = document.getElementById('habitatDiversityValue');
    const obstaclesInput = document.getElementById('obstacles');
    const obstaclesValueSpan = document.getElementById('obstaclesValue');
    const warmingRateInput = document.getElementById('warmingRate');
    const warmingRateValueSpan = document.getElementById('warmingRateValue');
    const extremeEventsInput = document.getElementById('extremeEvents');
    const extremeEventsValueSpan = document.getElementById('extremeEventsValue');

    const currentStepDisplay = document.getElementById('currentStepDisplay');
    const maxStepsDisplay = document.getElementById('maxStepsDisplay');
    const currentTempDisplay = document.getElementById('currentTempDisplay');
    const presentCellsDisplay = document.getElementById('presentCellsDisplay');
    const refugeCountDisplay = document.getElementById('refugeCountDisplay');
    const refugeCellsDisplay = document.getElementById('refugeCellsDisplay');


    let grid = []; // Holds the cell elements
    let speciesPresence = []; // Boolean grid: is species present?
    let landscapeTempOffset = []; // Float grid: local temp deviations
    let habitatSuitable = []; // Boolean grid: is habitat suitable?
    let obstacles = []; // Boolean grid: is impassable?

    let initialGlobalTemp = 15;
    let currentGlobalTemp = initialGlobalTemp;
    const MAX_SIMULATION_STEPS = 70; // Increased simulation length

    let simulationInterval;
    let currentStep = 0;
    let isRunning = false;


    // --- Utility Functions ---

    // Update range value displays immediately on input
    tempSensitivityInput.oninput = () => tempSensitivityValueSpan.textContent = `${parseFloat(tempSensitivityInput.value).toFixed(1)}°C`;
    dispersalAbilityInput.oninput = () => dispersalAbilityValueSpan.textContent = `${dispersalAbilityInput.value} תא/שלב`;
    landscapeVariationInput.oninput = () => landscapeVariationValueSpan.textContent = `${parseFloat(landscapeVariationInput.value).toFixed(1)} יחידות`;
    habitatDiversityInput.oninput = () => habitatDiversityValueSpan.textContent = `${parseInt(habitatDiversityInput.value).toFixed(0)}% לא מתאים`;
    obstaclesInput.oninput = () => obstaclesValueSpan.textContent = `${parseInt(obstaclesInput.value).toFixed(0)}% חסום`;
    warmingRateInput.oninput = () => warmingRateValueSpan.textContent = `${parseFloat(warmingRateInput.value).toFixed(2)}°C/שלב`;
    extremeEventsInput.oninput = () => extremeEventsValueSpan.textContent = `${(extremeEventsInput.value * 100).toFixed(0)}% סיכוי`;

    // Function to add/remove classes for cell state
    function setCellState(cell, stateClass, title) {
        cell.className = 'map-cell'; // Reset classes
        cell.classList.add(stateClass);
        cell.title = title;
    }

    // --- Grid Initialization and Display ---

    function createInitialGrid() {
        grid = [];
        speciesPresence = [];
        landscapeTempOffset = [];
        habitatSuitable = [];
        obstacles = [];
        currentGlobalTemp = initialGlobalTemp; // Reset temp
        currentStep = 0;
        refugeCountDisplay.style.display = 'none'; // Hide refuge count until end

        mapElement.innerHTML = ''; // Clear previous grid
        mapElement.style.gridTemplateColumns = `repeat(${mapSize}, 1fr)`;

        const landscapeVar = parseFloat(landscapeVariationInput.value);
        const habitatDiv = parseInt(habitatDiversityInput.value) / 100;
        const obs = parseInt(obstaclesInput.value) / 100;

        let initialSpeciesPlaced = 0;
        const initialAreaSize = 4; // 4x4 square in the center

        for (let i = 0; i < mapSize; i++) {
            grid[i] = [];
            speciesPresence[i] = [];
            landscapeTempOffset[i] = [];
            habitatSuitable[i] = [];
            obstacles[i] = [];
            for (let j = 0; j < mapSize; j++) {
                const cell = document.createElement('div');
                cell.classList.add('map-cell');
                cell.dataset.row = i;
                cell.dataset.col = j;

                // Generate landscape properties
                // Simple height/temp variation simulation - Scale variation relative to input max (15)
                landscapeTempOffset[i][j] = (Math.random() - 0.5) * 2 * (landscapeVar / 15);

                // Habitat suitability
                habitatSuitable[i][j] = Math.random() > habitatDiv;

                // Obstacles
                 obstacles[i][j] = Math.random() < obs;

                // Initial species presence (center of the map) - check if the initial area is suitable/not obstacle
                const isInitialCell = (i >= mapSize / 2 - initialAreaSize/2 && i < mapSize / 2 + initialAreaSize/2 && j >= mapSize / 2 - initialAreaSize/2 && j < mapSize / 2 + initialAreaSize/2);
                const isInitialSuitable = habitatSuitable[i][j] && !obstacles[i][j];

                // Only place species if the cell is suitable and within the initial area
                speciesPresence[i][j] = isInitialCell && isInitialSuitable;
                 if (speciesPresence[i][j]) initialSpeciesPlaced++;

                grid[i][j] = cell;
                mapElement.appendChild(cell);
            }
        }

        // If no species were placed initially (e.g., center is all obstacles/unsuitable),
        // find the first suitable cell and place one species there as a starting point.
        if (initialSpeciesPlaced === 0) {
             for (let i = 0; i < mapSize; i++) {
                 let found = false;
                 for (let j = 0; j < mapSize; j++) {
                     if (habitatSuitable[i][j] && !obstacles[i][j]) {
                         speciesPresence[i][j] = true;
                         found = true;
                         break;
                     }
                 }
                 if (found) break;
             }
        }


        updateMapDisplay(0); // Display initial state
        updateStatsDisplay();
    }

    function updateMapDisplay(step) {
        let presentCount = 0;
        let refugeCount = 0;

        for (let i = 0; i < mapSize; i++) {
            for (let j = 0; j < mapSize; j++) {
                const cell = grid[i][j];
                const isSpeciesPresent = speciesPresence[i][j];
                const isSuitableHabitat = habitatSuitable[i][j];
                const isObstacle = obstacles[i][j];
                const localTemp = currentGlobalTemp + landscapeTempOffset[i][j];

                let title = `שור: ${i}, טור: ${j}\n`;
                title += `סטיית טמפ' מקומית: ${landscapeTempOffset[i][j].toFixed(2)}°C\n`;
                title += `טמפ' מקומית: ${localTemp.toFixed(1)}°C (גלובלי: ${currentGlobalTemp.toFixed(1)}°C)\n`;
                title += `בית גידול מתאים: ${isSuitableHabitat ? 'כן' : 'לא'}\n`;
                title += `מחסום: ${isObstacle ? 'כן' : 'לא'}\n`;

                let stateClass = 'empty'; // Default

                if (isObstacle || !isSuitableHabitat) {
                    stateClass = 'unsuitable'; // Use 'unsuitable' for both obstacle and unsuitable habitat for color coding, check logic for title
                    title += 'מצב: שטח לא מתאים';
                     if(isObstacle && !isSuitableHabitat) title += ' (גם מחסום וגם לא מתאים)';
                     else if(isObstacle) title += ' (מחסום)';
                     else title += ' (בית גידול לא מתאים)';

                } else {
                     // Area is suitable habitat and not an obstacle
                     if (isSpeciesPresent) {
                         presentCount++;
                         if (step === MAX_SIMULATION_STEPS) {
                              stateClass = 'refuge'; // It survived till the end in a suitable cell -> potential refuge
                              refugeCount++;
                              title += 'מצב: מקלט אקלימי פוטנציאלי';
                         } else {
                              stateClass = 'present'; // Currently present
                              title += 'מצב: נוכחות מין';
                         }
                     } else {
                          stateClass = 'extinct'; // Suitable but species is absent (locally extinct or never arrived)
                          title += 'מצב: נכחד מקומית / לא הגיע';
                     }
                }

                 setCellState(cell, stateClass, title);
            }
        }
        presentCellsDisplay.textContent = presentCount;
        refugeCellsDisplay.textContent = refugeCount;

         if (step === MAX_SIMULATION_STEPS) {
             refugeCountDisplay.style.display = 'block'; // Show refuge count at the end
         } else {
              refugeCountDisplay.style.display = 'none'; // Hide during simulation
         }
    }

    function updateStatsDisplay() {
        currentStepDisplay.textContent = currentStep;
        maxStepsDisplay.textContent = MAX_SIMULATION_STEPS;
        currentTempDisplay.textContent = currentGlobalTemp.toFixed(1);
        // Present cells count is updated in updateMapDisplay
    }

    // --- Simulation Logic ---

    function runSimulationStep() {
        const tempSensitivity = parseFloat(tempSensitivityInput.value);
        const dispersalAbility = parseInt(dispersalAbilityInput.value);
        const warmingRate = parseFloat(warmingRateInput.value);
        const extremeEventsFreq = parseFloat(extremeEventsInput.value);

        currentGlobalTemp += warmingRate; // Apply global warming

        // Create a temporary grid for the next state
        let nextSpeciesPresence = [];
        let dispersalSources = []; // Cells that will be sources for dispersal in this step

        for(let i=0; i<mapSize; i++) {
            nextSpeciesPresence[i] = [];
            for(let j=0; j<mapSize; j++) {
                nextSpeciesPresence[i][j] = false; // Assume species is absent initially in the next step
            }
        }

        // Pass 1: Check survival in the current locations and identify dispersal sources
        for (let i = 0; i < mapSize; i++) {
            for (let j = 0; j < mapSize; j++) {
                // Check if species is currently present in this cell
                if (speciesPresence[i][j]) {
                    const localTemp = currentGlobalTemp + landscapeTempOffset[i][j];
                    const isSuitable = habitatSuitable[i][j] && !obstacles[i][j];

                    // Check for extreme event impact
                    const impactedByExtreme = Math.random() < extremeEventsFreq;

                    // Species survives in this cell for the next step if conditions are met
                    if (isSuitable && localTemp <= tempSensitivity && !impactedByExtreme) {
                         nextSpeciesPresence[i][j] = true; // Survived in place, will be present in the next step
                         dispersalSources.push({ r: i, c: j }); // This surviving cell is a source for dispersal
                    }
                    // If it didn't survive, nextSpeciesPresence[i][j] remains false
                }
            }
        }

        // Pass 2: Dispersal from surviving cells (dispersalSources) to populate other cells in nextSpeciesPresence
        for (const source of dispersalSources) {
            const r = source.r;
            const c = source.c;

             // Check cells within dispersal radius around the source
            for (let dr = -dispersalAbility; dr <= dispersalAbility; dr++) {
                for (let dc = -dispersalAbility; dc <= dispersalAbility; dc++) {
                    // Calculate distance (using Manhattan distance as it fits grid movement concept)
                    const distance = Math.abs(dr) + Math.abs(dc);

                    if (distance <= dispersalAbility) { // Check if within dispersal range
                        const neighborR = r + dr;
                        const neighborC = c + dc;

                        // Check bounds
                        if (neighborR >= 0 && neighborR < mapSize && neighborC >= 0 && neighborC < mapSize) {
                             // Check if destination is suitable habitat and not an obstacle
                            if (habitatSuitable[neighborR][neighborC] && !obstacles[neighborR][neighborC]) {
                                // Species successfully disperses to this neighbor.
                                // Mark it as present in the *next* state.
                                nextSpeciesPresence[neighborR][neighborC] = true;
                            }
                        }
                    }
                }
            }
        }

        speciesPresence = nextSpeciesPresence; // Update state for the next step
        currentStep++;

        updateMapDisplay(currentStep); // Update display for the current step
        updateStatsDisplay();
    }

    // --- Simulation Control ---

    function startSimulation() {
        if (isRunning) return; // Prevent multiple intervals
        if (simulationInterval) clearInterval(simulationInterval);

        isRunning = true;
        runButton.disabled = true;
        resetButton.disabled = false;

        // Ensure grid is fresh at start or continues from reset state
        if (currentStep === 0) {
             createInitialGrid();
        } else {
             // If simulation was stopped mid-way and starting again
             updateMapDisplay(currentStep); // Show current state before step 1
        }


        simulationInterval = setInterval(() => {
            if (currentStep >= MAX_SIMULATION_STEPS) {
                clearInterval(simulationInterval);
                isRunning = false;
                runButton.disabled = false;
                console.log("Simulation finished.");
                updateMapDisplay(currentStep); // Final display shows refuges
                updateStatsDisplay();
                return;
            }

            runSimulationStep();

        }, 200); // Adjust interval for speed (milliseconds)
    }

    function resetSimulation() {
        if (simulationInterval) clearInterval(simulationInterval);
        isRunning = false;
        runButton.disabled = false;
        resetButton.disabled = true;

        createInitialGrid(); // Recreate the initial state
        updateMapDisplay(0); // Display initial state
        updateStatsDisplay();
        console.log("Simulation reset.");
    }


    // --- Event Listeners ---

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק';
    });

    runButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);

    // --- Initialization ---
    createInitialGrid(); // Initialize the map on page load
    updateStatsDisplay();
    resetButton.disabled = true; // Reset button is disabled until simulation runs or stops


</script>
---