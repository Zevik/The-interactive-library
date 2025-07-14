---
title: "התפשטות הרעיונות: סימולטור דינמיקה חברתית"
english_slug: cultural-memes-spread-simulator
category: "מדעי החברה / כללי"
tags: ממים תרבותיים, התפשטות רעיונות, דינמיקה חברתית, סימולציה, רשתות חברתיות
---
# לגלות את הקוד החבוי: סימולטור התפשטות רעיונות

ממם ויראלי שמשגע את הרשת, דרך טרנד אופנתי שכבש את הרחוב, ועד רעיון מהפכני שמשנה חברה שלמה – לכולם יש מכנה משותף: הם מתפשטים. אבל איך? האם זה מקרי, או שמא ישנם חוקים נסתרים שמנהלים את התפשטות הרעיונות? הצטרפו למסע אינטראקטיבי בזמן וברשתות חברתיות כדי לחשוף את הדינמיקה המפתיעה של אימוץ רעיונות.

<div class="simulator-container">
    <div class="controls-panel">
        <h2>הגדרות המסע</h2>
        <div class="param-group">
            <label for="populationSize">מספר סוכנים באוכלוסייה:</label>
            <input type="number" id="populationSize" value="600" min="100" max="2500" step="50">
            <span class="param-unit">(עד 2500)</span>
        </div>
         <div class="param-group">
            <label for="gridSize">גודל זירת האינטראקציה:</label>
            <input type="number" id="gridSize" value="30" min="10" max="50">
             <span class="param-unit">(ריבוע בגודל X*X)</span>
        </div>
        <div class="param-group">
            <label for="initialInfected">מובילי דעה ראשוניים (%):</label>
            <input type="number" id="initialInfected" value="3" min="1" max="30">
             <span class="param-unit">(אחוז מהאוכלוסייה)</span>
        </div>
        <div class="param-group">
            <label for="spreadProbability">סיכוי הידבקות משכן (%):</label>
            <input type="number" id="spreadProbability" value="40" min="0" max="100">
            <span class="param-unit">(סיכוי לאימוץ מהשפעה ישירה)</span>
        </div>
        <div class="param-group">
            <label for="forgetProbability">סיכוי נטישה/שכחה (%):</label>
            <input type="number" id="forgetProbability" value="1" min="0" max="10">
             <span class="param-unit">(סיכוי לנטוש את הרעיון)</span>
        </div>
        <div class="param-group">
            <label for="steps">משך הסימולציה (דורות):</label>
            <input type="number" id="steps" value="200" min="10" max="500">
            <span class="param-unit">(עד 500 צעדים)</span>
        </div>
        <div class="button-group">
            <button id="startSimulation" class="action-button primary">התחל מסע</button>
            <button id="resetSimulation" class="action-button secondary" disabled>אפס זירה</button>
        </div>
    </div>

    <div class="visualization-area">
        <div class="simulation-grid">
             <div class="grid-title">זירת ההתפשטות</div>
            <canvas id="simulationCanvas"></canvas>
             <div class="simulation-status">דור: <span id="currentStep">0</span></div>
        </div>
        <div class="graph-area">
             <div class="graph-title">מסע האימוץ (אחוז באוכלוסייה)</div>
            <canvas id="graphCanvas"></canvas>
        </div>
    </div>
</div>

<button id="toggleExplanation" class="action-button tertiary">מידע נוסף: הקוד החבוי נחשף</button>

<div id="explanation" style="display: none;">
    <h2>הקוד החבוי נחשף: עקרונות הסימולטור</h2>

    <h3>מהו 'מם תרבותי' וכיצד הוא 'מתפשט'?</h3>
    רעיונות, אופנות, שירים קליטים – כולם סוגים של 'ממים תרבותיים'. המונח, שטבע הביולוג ריצ'רד דוקינס, מתאר יחידות מידע תרבותי שמצליחות לשכפל את עצמן ולהתפשט בתוך חברה, בדומה לגנים ביולוגיים. ה'התפשטות' היא למעשה תהליך של העברה ואימוץ של המם על ידי יותר ויותר אנשים לאורך זמן. בסימולטור שלנו, כל 'סוכן' בודד הוא אדם פוטנציאלי שיכול לאמץ או לנטוש רעיון.

    <h3>השראה מעולם המגפות</h3>
    אחת הדרכים המרתקות לחקור התפשטות תרבותית היא באמצעות מודלים מעולם האפידמיולוגיה (חקר התפשטות מחלות). במודלים כאלה, מחלה עוברת מאדם חולה ל'בריא' בהסתברות מסוימת. הסימולטור הנוכחי מבוסס על אנלוגיה פשוטה זו: ה'רעיון' או ה'מם' הוא המחלה, סוכן ש'אימץ' את הרעיון הוא 'מאומת' (במקום 'חולה'), וסוכן שעדיין לא אימץ הוא 'פוטנציאלי לאימוץ' (במקום 'בריא'). ההעברה מתרחשת דרך 'מגע חברתי' (אינטראקציה בין סוכנים קרובים).

    <h3>כוחם של המספרים והאינטראקציות: פרמטרים קריטיים</h3>
    הסימולטור מאפשר לכם לשחק עם המשתנים העיקריים שמעצבים את גורל הרעיון:
    <ul>
        <li><b>מספר סוכנים באוכלוסייה:</b> כמה אנשים פוטנציאליים יש בזירה? אוכלוסייה גדולה יותר יכולה להכיל התפשטות ענקית, אך גם דורשת יותר מאמץ מהרעיון כדי להגיע לכל פינה.</li>
        <li><b>גודל זירת האינטראקציה:</b> הסוכנים מפוזרים על 'רשת' דמיונית. פרמטר זה קובע את גודל הרשת ובהתאם לכך את הצפיפות והקשרים הפוטנציאליים בין סוכנים שכנים.</li>
        <li><b>מובילי דעה ראשוניים (%):</b> זהו ה"זרע" של הרעיון – אחוז קטן של סוכנים שכבר 'אימצו' את הרעיון מההתחלה. ככל שהזרע גדול יותר, כך הסיכוי להתפרצות מהירה ורחבה גדל.</li>
        <li><b>סיכוי הידבקות משכן (%):</b> זהו הלב של תהליך ההשפעה החברתית. בכל "דור" (צעד סימולציה), סוכן שעדיין לא אימץ את הרעיון ובא במגע עם סוכן שאימץ אותו, יש לו סיכוי מסוים (זה הפרמטר) לאמץ את הרעיון גם הוא. סיכוי גבוה יותר = התפשטות אגרסיבית יותר.</li>
        <li><b>סיכוי נטישה/שכחה (%):</b> לא כל רעיון נשאר לנצח. פרמטר זה מייצג את הסיכוי שסוכן שכבר אימץ את הרעיון יפסיק להחזיק בו מסיבות פנימיות (יצא מאופנה, נשכח, איבד עניין). זהו כוח נגד ההתפשטות, שיכול לגרום לרעיון להיעלם גם אחרי שהתפשט.</li>
        <li><b>משך הסימולציה (דורות):</b> כמה זמן אנו מאפשרים לתהליך ההתפשטות להתרחש?</li>
    </ul>
    שחקו עם הפרמטרים וגלו כיצד שינויים, לעיתים קטנים בלבד, יכולים להכריע את גורל הרעיון – האם הוא יישאר נחלת קומץ, ידשדש, או יהפוך לתופעה גלובלית בתוך האוכלוסייה המדומה.

    <h3>הרשת היא הסיפור: כוחה של אינטראקציה מקומית</h3>
    בסימולטור זה, ההתפשטות מתרחשת *רק* דרך אינטראקציה פיזית/חברתית קרובה (בין שכנים ברשת). זה מדגיש עד כמה המבנה של הרשת החברתית (מי מקושר למי) הוא קריטי. בעולם האמיתי, הרשתות מורכבות הרבה יותר (עם "קפיצות" בין אנשים מרוחקים, משפיענים עם קשרים רבים), והמבנה שלהן מעצב באופן דרמטי את מהירות ודפוס ההתפשטות של כל דבר, משמועות ועד חידושים טכנולוגיים. גם ברשת הפשוטה שלנו, תוכלו לראות איך סוכן 'מאומת' יחיד יכול להדליק שרשרת תגובה דרך שכניו.

    <h3>נקודת המפנה: רגע השינוי הדרמטי</h3>
    שימו לב במיוחד כיצד שילוב מסוים של פרמטרים (למשל, אחוז ראשוני מספיק של מאמצים וסיכוי הדבקה גבוה מספיק) יכול להפוך מצב של דעיכה איטית להתפרצות מהירה שכובשת את רוב האוכלוסייה. הנקודה הזו, שבה שינוי קטן יחסית מוביל לשינוי דרמטי בקנה מידה גדול, נקראת 'נקודת מפנה' (Tipping Point). הבנת נקודות מפנה חיונית לחיזוי והשפעה על תהליכים חברתיים, כלכליים ותרבותיים רחבים.

    <h3>יותר מתיאוריה: יישומים בעולם שלנו</h3>
    העקרונות המודגמים כאן רלוונטיים למגוון עצום של תופעות יומיומיות והיסטוריות:
    <ul>
        <li><b>טרנדים ויראליים:</b> כיצד סרטון טיקטוק או אתגר אינטרנטי הופכים לתופעה עולמית?</li>
        <li><b>אימוץ חדשנות:</b> איך טכנולוגיות חדשות כמו הסמארטפון או האינטרנט התפשטו כה מהר?</li>
        <li><b>שמועות ופייק ניוז:</b> מה מאפשר לשמועות להתפשט כמו אש בשדה קוצים, במיוחד בעידן הרשתות החברתיות?</li>
        <li><b>שינוי נורמות חברתיות:</b> כיצד התפשטו נורמות חדשות לגבי נושאים כמו איכות סביבה, תזונה, או זכויות אדם?</li>
        <li><b>קמפיינים ותנועות:</b> איך רעיונות פוליטיים, שיווקיים או חברתיים צוברים תאוצה ותומכים?</li>
    </ul>

    <h3>גבולות המודל: המציאות תמיד מורכבת יותר</h3>
    חשוב לזכור שהסימולטור הנוכחי הוא פישוט אלגנטי של מציאות סבוכה להפליא. בעולם האמיתי, רעיונות מתפשטים בהשפעת גורמים נוספים רבים: תקשורת המונים, משפיענים מרוחקים, שכנוע אקטיבי, מוטיבציות אישיות עמוקות, והיכולת של הרעיון עצמו להשתנות ולהתפתח. למרות זאת, מודלים בסיסיים כמו זה מספקים לנו כלי חשיבה רב עוצמה להבנת הדינמיקה המהותית של התפשטות המבוססת על אינטראקציה ורשת, ומדגישים את החשיבות של פרמטרים כמו "סיכוי הדבקה" ו"זרע ראשוני".

    <p>עכשיו שאתם מצוידים בידע, חזרו למסע, שחקו עם הפרמטרים, ונסו לחזות או אפילו לעצב את גורל הרעיון בזירה הדיגיטלית!</p>

</div>

<style>
    /* Variables for consistent styling */
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #6c757d; /* Gray */
        --tertiary-color: #28a745; /* Green */
        --infected-color: #dc3545; /* Red */
        --susceptible-color: #17a2b8; /* Teal */
        --background-color: #f8f9fa; /* Light background */
        --card-background: #ffffff; /* White for cards */
        --border-color: #e9ecef; /* Light border */
        --text-color: #343a40; /* Dark grey text */
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --border-radius: 8px;
        --padding-medium: 15px;
        --padding-large: 20px;
    }

    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
        margin: 0;
    }

     h1 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 30px;
        font-size: 2em;
    }

    .simulator-container {
        display: flex;
        flex-wrap: wrap;
        gap: 25px;
        margin-bottom: 30px;
    }

    .controls-panel, .visualization-area {
        flex: 1;
        background-color: var(--card-background);
        padding: var(--padding-large);
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        display: flex;
        flex-direction: column;
        gap: 20px; /* Gap between grid/graph and controls sections */
    }

     .controls-panel {
        min-width: 280px;
        max-width: 350px; /* Give controls a max width on larger screens */
     }

     .visualization-area {
         flex-grow: 2; /* Allow visualization to take more space */
         min-width: 320px;
     }


    .controls-panel h2, #explanation h2 {
        margin-top: 0;
        font-size: 1.5em;
        color: var(--text-color);
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 10px;
        margin-bottom: var(--padding-medium);
    }

    .param-group {
        margin-bottom: var(--padding-medium);
    }

    .param-group label {
        display: block;
        margin-bottom: 6px;
        font-weight: bold;
        font-size: 1em;
        color: var(--text-color);
    }

     .param-group input[type="number"] {
        width: calc(100% - 20px); /* Adjust for padding */
        padding: 10px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        box-sizing: border-box;
        font-size: 1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

     .param-group input[type="number"]:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
        outline: none;
     }

     .param-unit {
         display: block;
         font-size: 0.85em;
         color: var(--secondary-color);
         margin-top: 4px;
         text-align: left; /* Align unit text to the left for clarity */
     }

    .button-group {
        display: flex;
        gap: 10px;
        margin-top: 20px;
    }

     .action-button {
        display: inline-block;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        text-align: center;
     }

    .action-button.primary {
        background-color: var(--primary-color);
        color: white;
    }

    .action-button.secondary {
        background-color: var(--secondary-color);
        color: white;
    }

     .action-button.tertiary {
        background-color: var(--tertiary-color);
        color: white;
        display: block; /* Make the toggle button block level */
        width: fit-content;
        margin: 20px auto;
    }


    .action-button:hover:not(:disabled) {
        opacity: 0.9;
    }

     .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
    }


    .simulation-grid, .graph-area {
         border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        overflow: hidden;
        background-color: var(--background-color); /* Light background for canvas areas */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05); /* Inner shadow for depth */
        position: relative; /* Needed for absolute positioning of titles/status */
    }

     .grid-title, .graph-title {
         position: absolute;
         top: 5px;
         right: 10px;
         font-size: 0.9em;
         color: var(--secondary-color);
         z-index: 1; /* Ensure text is above canvas */
     }

     .simulation-status {
         position: absolute;
         bottom: 5px;
         right: 10px;
         font-size: 0.9em;
         color: var(--secondary-color);
         z-index: 1;
     }


    #simulationCanvas {
        display: block;
        width: 100%; /* Canvas takes full width of its container */
        height: auto; /* Maintain aspect ratio */
        min-height: 200px; /* Minimum height */
    }

     #graphCanvas {
        display: block;
        width: 100%;
        height: 200px; /* Fixed height for graph */
    }


    #explanation {
        margin-top: 30px;
        padding: var(--padding-large);
        background-color: var(--card-background);
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        direction: rtl;
        text-align: right;
        border: 1px solid var(--border-color);
    }

    #explanation h3 {
        font-size: 1.3em;
        color: var(--primary-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
        margin-bottom: 10px;
        margin-top: 20px;
    }

    #explanation ul {
        list-style: disc inside;
        padding-right: 20px;
        margin-bottom: 15px;
    }

    #explanation li {
        margin-bottom: 8px;
        line-height: 1.5;
    }

     #explanation p {
         margin-bottom: 15px;
     }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        .simulator-container {
            flex-direction: column;
            gap: 20px; /* Slightly less gap on smaller screens */
        }
        .controls-panel, .visualization-area {
            width: 100%;
            max-width: none;
            padding: var(--padding-medium); /* Smaller padding */
        }
        .button-group {
             flex-direction: column;
        }
        .action-button {
             width: 100%;
        }
        h1 {
            font-size: 1.5em;
        }
         .controls-panel h2, #explanation h2 {
             font-size: 1.3em;
         }
         #explanation h3 {
             font-size: 1.1em;
         }
         .param-group input[type="number"] {
             width: 100%; /* Full width on small screens */
         }
          .param-unit {
             text-align: right; /* Align unit text back to right */
          }
    }

</style>

<script>
    const simulationCanvas = document.getElementById('simulationCanvas');
    const graphCanvas = document.getElementById('graphCanvas');
    const startButton = document.getElementById('startSimulation');
    const resetButton = document.getElementById('resetSimulation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
    const currentStepSpan = document.getElementById('currentStep'); // Span to display current step

    const ctxSim = simulationCanvas.getContext('2d');
    const ctxGraph = graphCanvas.getContext('2d');

    // Simulation parameters - Get references now, read values on start/reset
    const populationSizeInput = document.getElementById('populationSize');
    const gridSizeInput = document.getElementById('gridSize');
    const initialInfectedInput = document.getElementById('initialInfected');
    const spreadProbabilityInput = document.getElementById('spreadProbability');
    const forgetProbabilityInput = document.getElementById('forgetProbability');
    const stepsInput = document.getElementById('steps');

    let gridSize; // Read from input
    let totalCells; // Calculated
    let cellSize; // Calculated based on canvas size

    let agents = []; // 2D grid: agents[row][col] = state (0=susceptible, 1=infected) or undefined (no agent)
    let agentStatesHistory = []; // To store percentages for the graph
    let newlyInfected = new Set(); // Track agents newly infected in the last step for animation

    let simulationRunning = false;
    let currentStep = 0;
    let maxSteps; // Read from input
    let simulationFrameId = null; // For requestAnimationFrame or setTimeout


    const STATE = {
        SUSCEPTIBLE: 0,
        INFECTED: 1
    };

    const COLORS = {
         BACKGROUND: '#f8f9fa', // Should match CSS .simulation-grid background
         EMPTY_CELL: '#e9ecef', // Subtle background for empty grid cells
         SUSCEPTIBLE: '#17a2b8', // Teal
         INFECTED: '#dc3545', // Red
         INFECTED_PULSE: '#ff7f50', // Lighter red/orange for pulse effect
         GRAPH_LINE: '#dc3545', // Red for graph
         GRAPH_AXES: '#343a40', // Dark text color
    };

    // --- Initialization Function ---
    function initializeSimulation() {
        // Read and validate parameters
        gridSize = parseInt(gridSizeInput.value);
        totalCells = gridSize * gridSize;
        let populationSize = parseInt(populationSizeInput.value);
        let initialInfectedPercent = parseInt(initialInfectedInput.value);
        maxSteps = parseInt(stepsInput.value);

        // Ensure population does not exceed grid capacity
        if (populationSize > totalCells) {
            populationSize = totalCells;
            populationSizeInput.value = totalCells;
        }
         if (populationSize <= 0) populationSize = 1; // Minimum population

        // Stop any ongoing simulation frame
        if (simulationFrameId) {
             clearTimeout(simulationFrameId); // Use clearTimeout as we use setTimeout
             simulationFrameId = null;
        }


        // Setup canvas size and cell size
        const containerWidth = simulationCanvas.parentElement.offsetWidth;
        const canvasSize = Math.min(containerWidth, 600); // Max size for simulation grid
        simulationCanvas.width = canvasSize;
        simulationCanvas.height = canvasSize; // Keep it square
        graphCanvas.width = graphCanvas.parentElement.offsetWidth - 20; // Take parent width minus padding
        graphCanvas.height = 200; // Fixed height for graph

        cellSize = canvasSize / gridSize;

        // Initialize agents grid as empty (undefined)
        agents = Array(gridSize).fill(null).map(() => Array(gridSize).fill(undefined));

        // List all possible cell positions and shuffle them
        const allCells = [];
        for(let r=0; r<gridSize; r++) {
            for(let c=0; c<gridSize; c++) {
                allCells.push({r, c});
            }
        }
        // Fisher-Yates Shuffle
        for (let i = allCells.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [allCells[i], allCells[j]] = [allCells[j], allCells[i]]; // Swap
        }

        // Place exactly `populationSize` agents at random positions
        const agentsToPlace = allCells.slice(0, populationSize);
        const numInitialInfected = Math.round(populationSize * (initialInfectedPercent / 100));

        let currentInfectedCount = 0;
        newlyInfected.clear(); // Clear animation state

        agentsToPlace.forEach((cell, index) => {
            if (index < numInitialInfected) {
                 agents[cell.r][cell.c] = STATE.INFECTED;
                 currentInfectedCount++;
                 // Mark initial infected for a potential intro animation effect
                 // newlyInfected.add(`${cell.r},${cell.c}`); // Could be used for initial pulse
            } else {
                 agents[cell.r][cell.c] = STATE.SUSCEPTIBLE;
            }
        });

         // Ensure at least one agent if population > 0 and initial infected is 0%
         if (populationSize > 0 && currentInfectedCount === 0) {
             // Find the first agent placed and make it infected
             if (agentsToPlace.length > 0) {
                 const firstAgent = agentsToPlace[0];
                 agents[firstAgent.r][firstAgent.c] = STATE.INFECTED;
                 currentInfectedCount = 1;
                 // newlyInfected.add(`${firstAgent.r},${firstAgent.c}`);
             }
         }


        // Reset simulation state
        simulationRunning = false;
        currentStep = 0;
        currentStepSpan.textContent = currentStep;
        agentStatesHistory = [];
         if(populationSize > 0) {
             agentStatesHistory.push({ step: currentStep, percent: (currentInfectedCount / populationSize) * 100 }); // Record initial state
         } else {
             agentStatesHistory.push({ step: currentStep, percent: 0 }); // Handle 0 population
         }


        // Draw initial state
        drawSimulation();
        drawGraph();

        startButton.disabled = false;
        resetButton.disabled = false; // Reset is enabled after init
    }

    // --- Drawing Functions ---
     function drawSimulation() {
         ctxSim.clearRect(0, 0, simulationCanvas.width, simulationCanvas.height);
         // Draw grid background (optional, if agents don't cover full cell)
         ctxSim.fillStyle = COLORS.EMPTY_CELL;
         ctxSim.fillRect(0, 0, simulationCanvas.width, simulationCanvas.height);


        for (let r = 0; r < gridSize; r++) {
            for (let c = 0; c < gridSize; c++) {
                const state = agents[r][c];
                if (state !== undefined) { // Only draw if there's an agent at this cell
                     const x = c * cellSize;
                     const y = r * cellSize;
                     const isNewlyInfected = newlyInfected.has(`${r},${c}`);

                     // Draw agent shape (square for simplicity and grid feel)
                     const agentPadding = 1; // Small padding to show grid lines/background
                     const agentSize = cellSize - 2 * agentPadding;
                     const agentX = x + agentPadding;
                     const agentY = y + agentPadding;

                     ctxSim.fillStyle = (state === STATE.INFECTED) ? COLORS.INFECTED : COLORS.SUSCEPTIBLE;
                     ctxSim.fillRect(agentX, agentY, agentSize, agentSize);

                     // Optional: Add a subtle border
                     // ctxSim.strokeStyle = '#fff';
                     // ctxSim.lineWidth = 0.5;
                     // ctxSim.strokeRect(agentX, agentY, agentSize, agentSize);


                     // Add animation visual for newly infected - a temporary highlight
                     if (isNewlyInfected && simulationRunning) { // Only animate during simulation run
                         ctxSim.strokeStyle = COLORS.INFECTED_PULSE;
                         ctxSim.lineWidth = 2;
                         // Draw a pulsing border that's slightly larger
                          const pulseSize = agentSize + 4;
                          const pulseX = x + cellSize/2 - pulseSize/2;
                          const pulseY = y + cellSize/2 - pulseSize/2;
                         ctxSim.strokeRect(pulseX, pulseY, pulseSize, pulseSize);
                         // The `newlyInfected` set is cleared at the start of runStepRevised,
                         // so this highlight only appears for one frame after infection.
                         // For a sustained pulse animation over time, more complex state or rAF would be needed.
                         // Sticking to simple single-frame highlight for now.
                     }
                }
            }
        }
    }


    function drawGraph() {
        ctxGraph.clearRect(0, 0, graphCanvas.width, graphCanvas.height);
        const width = graphCanvas.width;
        const height = graphCanvas.height;
        const padding = 25; // Increased padding
        const plotWidth = width - 2 * padding;
        const plotHeight = height - 2 * padding;

        // Draw axes
        ctxGraph.strokeStyle = COLORS.GRAPH_AXES;
        ctxGraph.lineWidth = 1;
        ctxGraph.beginPath();
        ctxGraph.moveTo(padding, padding); // Top-left of plot area
        ctxGraph.lineTo(padding, height - padding); // Y-axis (down)
        ctxGraph.lineTo(width - padding, height - padding); // X-axis (right)
        ctxGraph.stroke();

        // Draw axis labels
        ctxGraph.fillStyle = COLORS.GRAPH_AXES;
        ctxGraph.font = '12px Arial';
        ctxGraph.textAlign = 'center';
        ctxGraph.textBaseline = 'top';
        ctxGraph.fillText('דורות (צעדים)', width / 2, height - padding + 15);

        ctxGraph.save();
        ctxGraph.translate(padding - 15, height / 2);
        ctxGraph.rotate(-Math.PI / 2);
        ctxGraph.textAlign = 'center';
        ctxGraph.textBaseline = 'bottom';
        ctxGraph.fillText('אחוז מאמצים (%)', 0, 0);
        ctxGraph.restore();

         // Draw axis ticks and labels
         ctxGraph.textAlign = 'right';
         ctxGraph.textBaseline = 'middle';
         // Y-axis ticks (0%, 50%, 100%)
         ctxGraph.fillText('0', padding - 8, height - padding);
         ctxGraph.fillText('50', padding - 8, height - padding - plotHeight / 2);
         ctxGraph.fillText('100', padding - 8, padding);

         // X-axis ticks (0, maxSteps/2, maxSteps)
         ctxGraph.textAlign = 'center';
         ctxGraph.textBaseline = 'top';
         ctxGraph.fillText('0', padding, height - padding + 5);
         ctxGraph.fillText(Math.floor(maxSteps/2), padding + plotWidth/2, height - padding + 5);
         ctxGraph.fillText(maxSteps, width - padding, height - padding + 5);


        // Draw graph line
        ctxGraph.strokeStyle = COLORS.GRAPH_LINE;
        ctxGraph.lineWidth = 2;
        ctxGraph.beginPath();

        if (agentStatesHistory.length > 0) {
            const firstPoint = agentStatesHistory[0];
            const firstPointX = padding + (firstPoint.step / maxSteps) * plotWidth;
            const firstPointY = height - padding - (firstPoint.percent / 100) * plotHeight;
            ctxGraph.moveTo(firstPointX, firstPointY);

            for (let i = 1; i < agentStatesHistory.length; i++) {
                const point = agentStatesHistory[i];
                 // Ensure the step is mapped correctly within the plot width
                 const x = padding + (Math.min(point.step, maxSteps) / maxSteps) * plotWidth;
                 const y = height - padding - (point.percent / 100) * plotHeight;
                ctxGraph.lineTo(x, y);
            }
            ctxGraph.stroke();
        }
    }

    // --- Simulation Logic ---
    function getNeighbors(r, c) {
        const neighbors = [];
        // Moore neighborhood (8 neighbors, including diagonals)
        for (let dr = -1; dr <= 1; dr++) {
            for (let dc = -1; dc <= 1; dc++) {
                if (dr === 0 && dc === 0) continue; // Skip self

                const nr = r + dr;
                const nc = c + dc;

                // Check bounds and if an agent actually exists at this neighbor position
                if (nr >= 0 && nr < gridSize && nc >= 0 && nc < gridSize && agents[nr][nc] !== undefined) {
                     neighbors.push({ r: nr, c: nc });
                }
            }
        }
        return neighbors;
    }


     function runStep() {
        if (!simulationRunning || currentStep >= maxSteps) {
            simulationRunning = false;
             startButton.disabled = false; // Re-enable start
             resetButton.disabled = false; // Enable reset
             simulationFrameId = null; // Clear animation frame ID
             return;
        }

        // Create a copy of the current agent grid to calculate next states simultaneously
        let nextAgentsGrid = Array(gridSize).fill(null).map(() => Array(gridSize).fill(undefined));
         let infectedCountThisStep = 0;
        let actualPopulationCount = 0;
        newlyInfected.clear(); // Reset newly infected set for this step


        const spreadProb = parseInt(spreadProbabilityInput.value) / 100;
        const forgetProb = parseInt(forgetProbabilityInput.value) / 100;


        // First pass: Determine states for the next step
        for (let r = 0; r < gridSize; r++) {
            for (let c = 0; c < gridSize; c++) {
                const currentState = agents[r][c];

                if (currentState !== undefined) { // Only process if there's an agent
                    actualPopulationCount++; // Count existing agents

                    if (currentState === STATE.INFECTED) {
                        // Infected agents might become susceptible due to forgetting
                        if (Math.random() < forgetProb) {
                            nextAgentsGrid[r][c] = STATE.SUSCEPTIBLE; // Agent forgets/recovers
                        } else {
                            nextAgentsGrid[r][c] = STATE.INFECTED; // Agent remains infected
                            infectedCountThisStep++; // Count for the next step
                        }
                    } else { // currentState === STATE.SUSCEPTIBLE
                        // Susceptible agents might become infected by neighbors
                        const neighbors = getNeighbors(r, c);
                        let infectedNeighborsCount = 0;
                        neighbors.forEach(neighborPos => {
                            // Check the state of the neighbor in the *current* agents grid
                            if (agents[neighborPos.r][neighborPos.c] === STATE.INFECTED) {
                                infectedNeighborsCount++;
                            }
                        });

                        // Probability of getting infected from *at least one* infected neighbor
                        // P(infected) = 1 - P(not infected by any)
                         // P(not infected by any) = Product of P(not infected by neighbor i) for all infected neighbors
                         // P(not infected by neighbor i) = 1 - spreadProb
                         // So, P(not infected by any) = (1 - spreadProb) ^ infectedNeighborsCount
                        const probOfGettingInfected = 1 - Math.pow(1 - spreadProb, infectedNeighborsCount);


                        if (Math.random() < probOfGettingInfected) {
                            nextAgentsGrid[r][c] = STATE.INFECTED; // Agent becomes infected
                            infectedCountThisStep++; // Count for the next step
                             newlyInfected.add(`${r},${c}`); // Mark as newly infected for animation
                        } else {
                            nextAgentsGrid[r][c] = STATE.SUSCEPTIBLE; // Agent remains susceptible
                        }
                    }
                } else {
                     nextAgentsGrid[r][c] = undefined; // Empty cells remain empty
                }
            }
        }

        // If population is zero or no agents are present, stop simulation gracefully
        if (actualPopulationCount === 0) {
             simulationRunning = false;
             startButton.disabled = false;
             resetButton.disabled = false;
             // Add 0% to graph if it wasn't already there
             if (agentStatesHistory.length === 0 || agentStatesHistory[agentStatesHistory.length-1].percent !== 0) {
                  agentStatesHistory.push({ step: currentStep + 1, percent: 0 });
             }
             drawGraph();
             simulationFrameId = null; // Clear frame ID
             return;
        }


        agents = nextAgentsGrid; // Update agents grid for the next step
        currentStep++;
        currentStepSpan.textContent = currentStep;


        // Record state for graph - calculate percentage based on *actual* population
         const infectedPercent = (actualPopulationCount > 0) ? (infectedCountThisStep / actualPopulationCount) * 100 : 0;
         agentStatesHistory.push({ step: currentStep, percent: infectedPercent });


        drawSimulation();
        drawGraph();

        // Schedule next step - using setTimeout for consistent time intervals
        simulationFrameId = setTimeout(runStep, 70); // Adjust delay (milliseconds) as needed for animation speed
     }


    // --- Event Listeners ---
    startButton.addEventListener('click', () => {
        if (!simulationRunning) {
            simulationRunning = true;
            startButton.disabled = true; // Disable Start during run
            resetButton.disabled = true; // Disable Reset during run
            initializeSimulation(); // Re-initialize simulation state
             // Small delay before starting steps allows drawing initial state first
            simulationFrameId = setTimeout(runStep, 200);
        }
    });

    resetButton.addEventListener('click', () => {
        simulationRunning = false; // Stop any running simulation
         if (simulationFrameId) {
            clearTimeout(simulationFrameId); // Clear timeout if it exists
            simulationFrameId = null;
         }
        resetButton.disabled = true; // Disable Reset while initializing
        startButton.disabled = true; // Disable Start briefly until init is done
        initializeSimulation(); // Reset to initial state
         startButton.disabled = false; // Enable Start after init
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        // Optional: Change button text
        toggleExplanationButton.textContent = isHidden ? 'הסתר מידע נוסף' : 'מידע נוסף: הקוד החבוי נחשף';
    });

    // --- Initial Setup & Window Resize ---
    window.addEventListener('load', () => {
        initializeSimulation(); // Setup simulation on page load
    });

    window.addEventListener('resize', () => {
        // Re-calculate canvas sizes and cell size, then redraw
        const containerWidth = simulationCanvas.parentElement.offsetWidth;
        const canvasSize = Math.min(containerWidth, 600); // Max size for simulation grid
        simulationCanvas.width = canvasSize;
        simulationCanvas.height = canvasSize; // Keep it square
        graphCanvas.width = graphCanvas.parentElement.offsetWidth - 20; // Recalculate graph width
        // graphCanvas.height remains fixed at 200

        cellSize = canvasSize / gridSize; // Recalculate cell size based on new canvas size and current gridSize

        // Redraw current state if not running, or the current state if running
        drawSimulation();
        drawGraph();
    });


</script>
```