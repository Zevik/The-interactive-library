---
title: "קרב התאים: בנה וירוס וחזה מגפה"
english_slug: build-a-virus-infection-simulation
category: "ביולוגיה"
tags: [וירוסים, הדבקה, מודל, סימולציה, מיקרוביולוגיה, מגפה]
---
# קרב התאים: בנה וירוס וחזה מגפה

האם תוכל לעצור את ההתפשטות? כיצד וירוס זעיר מצליח להשתלט על תאים ולהתפשט במהירות באוכלוסיה? האם שינויים קטנים במבנהו יכולים לשנות הכל? בנה את הוירוס שלך, קבע את תנאי הסביבה, והרץ סימולציה כדי לגלות!

<div id="app-container">
    <div id="controls" class="panel">
        <h2>🛠️ בנה את הוירוס שלך</h2>
        <div class="control-group">
            <label for="genetic-material">חומר גנטי:</label>
            <select id="genetic-material" title="DNA או RNA - משפיע על קצב השכפול ויציבות גנומית.">
                <option value="RNA">RNA (שכפול מהיר, נוטה למוטציות)</option>
                <option value="DNA">DNA (שכפול איטי יותר, יציב יותר)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="structure">מבנה:</label>
            <select id="structure" title="קפסיד חשוף עמיד יותר בסביבה החיצונית; מעטפת מעניקה הגנה טובה יותר בתוך הגוף ופחות עמידות בחוץ.">
                <option value="naked">קפסיד חשוף (Naked)</option>
                <option value="enveloped">עטוף מעטפת (Enveloped)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="binding-efficiency">יעילות קשירה לתאים (1-10):</label>
            <input type="range" id="binding-efficiency" min="1" max="10" value="5" title="כמה טוב הוירוס נקשר לתאי המטרה. קשירה גבוהה יותר = סיכוי הדבקה גבוה יותר בכל מגע.">
            <span id="binding-efficiency-value">5</span>
        </div>

        <h2>🌍 הגדר את הסביבה</h2>
         <div class="control-group">
            <label for="population-size">גודל אוכלוסיה:</label>
            <input type="number" id="population-size" min="50" max="500" value="200" title="מספר הפרטים בסימולציה.">
        </div>
        <div class="control-group">
            <label for="initial-infections">נדבקים ראשוניים:</label>
            <input type="number" id="initial-infections" min="1" max="5" value="1" title="כמה פרטים נדבקו בתחילת הסימולציה.">
        </div>
        <div class="control-group">
            <label for="density">צפיפות או מגעים (1-10):</label>
            <input type="range" id="density" min="1" max="10" value="5" title="מספר המגעים הממוצע שכל פרט עושה בכל שלב זמן. צפיפות גבוהה = יותר מגעים = התפשטות מהירה יותר.">
             <span id="density-value">5</span>
        </div>
         <div class="control-group">
            <label for="replication-speed">קצב שכפול (1-10):</label>
            <input type="range" id="replication-speed" min="1" max="10" value="5" title="כמה מהר וירוסים חדשים נוצרים בתוך תא נגוע ומוכנים להדביק אחרים. קצב גבוה = הדבקה מהירה יותר.">
            <span id="replication-speed-value">5</span>
        </div>


        <button id="run-simulation" class="action-button">הרץ סימולציה 🦠</button>
         <button id="reset-simulation" class="action-button" style="display: none;">אפס והתחל מחדש 🔄</button>
    </div>

    <div id="simulation-area">
         <div id="simulation-stats" class="panel">
            <h3>נתוני הסימולציה</h3>
             <p>זמן: <span id="current-time">0</span></p>
             <p>נדבקים: <span id="current-infected-count">0</span></p>
             <p>רגישים: <span id="current-susceptible-count">0</span></p>
             <p>התפשטות: <span id="spread-status">ממתין...</span></p>
        </div>
        <div id="canvas-container" class="panel">
             <canvas id="simulation-canvas" width="450" height="450"></canvas>
             <canvas id="graph-canvas" width="450" height="200"></canvas>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג/הסתר הסבר על וירוסים ומודלים 📚</button>

<div id="explanation" class="panel" style="display: none;">
    <h2>💡 וירוסים והדבקה: הצד המדעי</h2>
    <p>וירוסים הם גבול מסקרן בין חי לדומם. הם אינם יכולים להתרבות בכוחות עצמם וחייבים "לחטוף" את מנגנוני התא המארח כדי לשכפל את עצמם. למרות גודלם הזעיר, הם בעלי השפעה עצומה על כל צורות החיים.</p>

    <h3>מבנה בסיסי של וירוס</h3>
    <ul>
        <li>**חומר גנטי:** ה"קוד" הוויראלי. יכול להיות **DNA** (יציב יותר) או **RNA** (נוטה יותר למוטציות מהירות, מה שיכול לעזור לו להשתנות ולהתחמק).</li>
        <li>**קפסיד:** מעטפת חלבון קשיחה המגנה על החומר הגנטי. כמו קופסת מגן.</li>
        <li>**מעטפת (Envelope):** שכבה חיצונית שומנית, הנגזרת לרוב מקרום התא המארח כשהוירוס יוצא. וירוסים עטופים נוטים להיות פגיעים יותר מחוץ לגוף (למשל לחומרי חיטוי או חום), אך המעטפת מסייעת להם להיכנס לתאים חדשים. וירוסים "חשופים" (Naked) עמידים יותר בסביבה.</li>
    </ul>

    <h3>מסע ההדבקה: שלב אחר שלב</h3>
    <ol>
        <li>**קשירה (Attachment):** הוירוס מזהה ונקשר לקולטנים ספציפיים על פני השטח של תא מטרה. כמו מפתח ומנעול. **יעילות הקשירה** משפיעה ישירות על הסיכוי להדביק תא במפגש.</li>
        <li>**חדירה (Entry):** הוירוס או רק החומר הגנטי שלו חודרים לתוך התא.</li>
        <li>**שכפול (Replication):** הוירוס משתלט על מכונות הייצור של התא ומאלץ אותן ליצור עותקים של החומר הגנטי הוויראלי וחלבונים ויראליים. **קצב השכפול** משפיע על כמה מהר נוצרים וירוסים חדשים בתוך התא.</li>
        <li>**הרכבה (Assembly):** החלקים הוויראליים החדשים מתארגנים ומרכיבים וירוסים שלמים.</li>
        <li>**יציאה (Release):** הוירוסים החדשים עוזבים את התא, לרוב תוך הריסתו (במיוחד וירוסים חשופים) או בתהליך הנצה עדינה יותר (וירוסים עטופים, שנושאים איתם חלק מקרום התא המארח).</li>
    </ol>

    <h3>מודלים של הדבקה: לנבא את העתיד</h3>
    <p>סימולציות כמו זו ששיחקת בה עוזרות למדענים ואנשי בריאות הציבור להבין ולחזות התפשטות מחלות. על ידי שינוי פרמטרים (כמו מאפייני הוירוס, **צפיפות אוכלוסיה**, יעילות חיסונים, או אמצעי ריחוק חברתי), ניתן לראות כיצד משתנה קצב ההדבקה, מספר השיא של הנדבקים, ומשך המגפה. זה כלי חיוני לקבלת החלטות אסטרטגיות בזמן אמת.</p>

    <h3>איך הפרמטרים שלך השפיעו?</h3>
    <ul>
        <li>**חומר גנטי (DNA/RNA):** בסימולציה זו, השפעתו מגולמת בעיקר בפרמטר "קצב שכפול" - וירוסי RNA לרוב משתכפלים מהר יותר.</li>
        <li>**מבנה (חשוף/עטוף):** בסימולציה זו, המבנה משפיע על יציבות הוירוס מחוץ לתא, ובכך על **יעילות ההדבקה** הכוללת במגע אקראי. וירוס עטוף פחות עמיד בסביבה החיצונית.</li>
        <li>**יעילות קשירה:** זהו אחד הגורמים המרכזיים לסיכוי הדבקה *אינדיבידואלי* בכל מגע בין וירוס לתא. יעילות גבוהה = סיכוי הדבקה גבוה למרות המגע.</li>
        <li>**גודל אוכלוסיה:** קובע את המספר המקסימלי של נדבקים פוטנציאליים ואת ה"קנבס" שבו הסימולציה מתרחשת.</li>
        <li>**נדבקים ראשוניים:** "נקודת הפתיחה" של המגפה. מספר גבוה יותר יוביל להתחלה מהירה יותר.</li>
        <li>**צפיפות או מגעים:** זהו גורם סביבתי מרכזי המשפיע על **מספר ההזדמנויות** להדבקה. צפיפות גבוהה = יותר מגעים בין פרטים = יותר סיכויים לווירוס לעבור.</li>
        <li>**קצב שכפול:** קובע כמה מהר אדם שנדבק הופך להיות "מדבק" בעצמו ומייצר וירוסים חדשים שיכולים להדביק אחרים. קצב גבוה = התפשטות מהירה יותר בתוך האוכלוסיה.</li>
    </ul>
    <p>שימו לב כיצוב העקומה בגרף: צורתה (עלייה מהירה/איטית, שיא גבוה/נמוך, משך ההתפשטות) מספרת את סיפור המגפה שיצרת!</p>
</div>


<style>
/* General Body & Layout */
body {
    font-family: 'Arial', sans-serif; /* Use a common, clear font */
    line-height: 1.6;
    margin: 0; /* Remove default margin */
    padding: 20px;
    direction: rtl; /* Right-to-left for Hebrew */
    text-align: right;
    background-color: #eef2f7; /* Light background */
    color: #333; /* Darker text */
}

h1, h2, h3 {
    color: #0056b3; /* Primary color */
    margin-bottom: 15px;
}

#app-container {
    display: flex;
    flex-wrap: wrap; /* Allows wrapping on smaller screens */
    gap: 25px; /* Increased gap */
    margin-bottom: 30px; /* Increased margin */
    padding: 20px;
    border-radius: 12px; /* More rounded corners */
    background-color: #ffffff; /* White background for app container */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}

.panel {
    background-color: #f8f9fa; /* Light gray background for panels */
    border: 1px solid #dee2e6; /* Light border */
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}


#controls {
    flex: 1; /* Allows controls to take available space */
    min-width: 300px; /* Minimum width before wrapping */
    max-width: 400px; /* Max width for controls panel */
}

#simulation-area {
    flex: 2; /* Allows simulation area to take more space */
    min-width: 450px; /* Minimum width */
    display: flex;
    flex-direction: column;
    gap: 20px; /* Gap between stats and canvas container */
    align-items: center; /* Center items horizontally */
}

#canvas-container {
     display: flex;
     flex-direction: column;
     gap: 10px;
     width: 100%; /* Take full width of simulation-area */
     align-items: center;
}

#simulation-stats {
    width: 100%; /* Take full width */
}
#simulation-stats h3 {
    margin-bottom: 10px;
    border-bottom: 1px solid #ced4da;
    padding-bottom: 5px;
}
#simulation-stats p {
    margin: 5px 0;
    font-size: 1.1rem;
}
#simulation-stats span {
    font-weight: bold;
    color: #007bff; /* Use a color to highlight values */
}


#simulation-canvas {
    border: 2px solid #adb5bd; /* More prominent border */
    background-color: #e9ecef; /* Slightly darker background */
    border-radius: 8px; /* Match panel border-radius */
    max-width: 100%; /* Ensure responsiveness */
    height: auto; /* Maintain aspect ratio */
}

#graph-canvas {
    border: 2px solid #adb5bd;
    background-color: #ffffff;
    margin-top: 15px; /* Spacing from simulation canvas */
    border-radius: 8px; /* Match panel border-radius */
     max-width: 100%; /* Ensure responsiveness */
    height: auto; /* Maintain aspect ratio */
}

/* Control Group Styling */
.control-group {
    margin-bottom: 20px; /* Increased spacing */
    padding-bottom: 10px;
    border-bottom: 1px dashed #ced4da; /* Separator */
}
.control-group:last-child {
     border-bottom: none; /* No border on last group */
     padding-bottom: 0;
     margin-bottom: 0;
}


.control-group label {
    display: block;
    margin-bottom: 8px; /* Increased spacing */
    font-weight: bold;
    color: #495057; /* Slightly darker label text */
    font-size: 1.05rem;
}

.control-group input[type="number"],
.control-group select {
    width: calc(100% - 24px); /* Adjust for padding/border */
    padding: 10px; /* Increased padding */
    border: 1px solid #ced4da;
    border-radius: 5px; /* Slightly more rounded */
    font-size: 1rem;
    background-color: #ffffff;
}

.control-group input[type="range"] {
    width: calc(100% - 60px); /* Adjust to make space for value */
    vertical-align: middle;
    -webkit-appearance: none; /* Remove default styles */
    appearance: none;
    height: 8px;
    background: #007bff; /* Track color */
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
    border-radius: 5px;
}
.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #0056b3; /* Thumb color */
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #ffffff; /* White border on thumb */
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}
.control-group input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #0056b3;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}


.control-group span {
     vertical-align: middle;
     display: inline-block;
     width: 30px; /* Reserve space for value */
     text-align: center;
     font-weight: bold;
     color: #007bff; /* Use primary color for values */
}


/* Buttons */
button {
    padding: 12px 20px; /* Increased padding */
    color: white;
    border: none;
    border-radius: 5px; /* Match input border-radius */
    cursor: pointer;
    font-size: 1.1rem; /* Slightly larger font */
    transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
    margin-top: 10px; /* Add spacing */
}

.action-button {
    background-color: #28a745; /* Green for action */
    margin-right: 10px; /* For RTL */
}
.action-button:hover {
    background-color: #218838;
    transform: translateY(-1px); /* Subtle hover effect */
}
.action-button:active {
    transform: translateY(1px); /* Subtle active effect */
}

.toggle-button {
    background-color: #6c757d; /* Gray for toggle */
    display: block; /* Make it a block element */
    width: auto; /* Auto width based on content */
    margin: 20px auto; /* Center the button */
    text-align: center;
}
.toggle-button:hover {
    background-color: #5a6268;
}


#explanation {
    margin-top: 20px;
    padding: 20px;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

#explanation h2 {
    margin-top: 0;
    color: #007bff; /* Primary color */
    border-bottom: 2px solid #007bff;
    padding-bottom: 10px;
}
#explanation h3 {
     color: #0056b3;
     margin-top: 15px;
     margin-bottom: 10px;
}


#explanation ul, #explanation ol {
    padding-right: 20px; /* RTL list padding */
    margin-bottom: 15px;
}

#explanation li {
    margin-bottom: 8px;
}

#explanation li strong {
    color: #007bff; /* Highlight terms */
}

/* Responsive adjustments */
@media (max-width: 768px) {
    #app-container {
        flex-direction: column;
        align-items: center; /* Center content in column layout */
    }

    #controls, #simulation-area {
        min-width: unset; /* Remove minimum width */
        width: 100%; /* Take full width */
        max-width: 100%;
    }

     #simulation-area {
         align-items: stretch; /* Stretch items within simulation-area */
     }

     #simulation-stats, #canvas-container {
         width: auto; /* Allow padding/margins */
     }

     #simulation-canvas, #graph-canvas {
         width: 100%; /* Make canvases fill their container */
         height: auto;
     }
}

/* Canvas Drawing Colors */
/* These are set in JS, but adding them here for visual consistency in CSS thought process */
/* .state-0 { fill: #a0e7e5; stroke: #77c4c2; } /* Susceptible - Teal */
/* .state-1 { fill: #ff6b6b; stroke: #e63946; } /* Infected - Red */
/* .state-2 { fill: #c8d7e1; stroke: #aab8c2; } /* (Future) Recovered/Immune - Gray/Blue */

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulationCanvas = document.getElementById('simulation-canvas');
    const simulationCtx = simulationCanvas.getContext('2d');
    const graphCanvas = document.getElementById('graph-canvas');
    const graphCtx = graphCanvas.getContext('2d');

    const runButton = document.getElementById('run-simulation');
    const resetButton = document.getElementById('reset-simulation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    const populationSizeInput = document.getElementById('population-size');
    const initialInfectionsInput = document.getElementById('initial-infections');
    const densityInput = document.getElementById('density');
    const replicationSpeedInput = document.getElementById('replication-speed'); // New input
    const geneticMaterialSelect = document.getElementById('genetic-material');
    const structureSelect = document.getElementById('structure');
    const bindingEfficiencyInput = document.getElementById('binding-efficiency');

    const bindingEfficiencyValueSpan = document.getElementById('binding-efficiency-value');
    const densityValueSpan = document.getElementById('density-value');
    const replicationSpeedValueSpan = document.getElementById('replication-speed-value'); // New span

    const currentTimeSpan = document.getElementById('current-time');
    const currentInfectedCountSpan = document.getElementById('current-infected-count');
    const currentSusceptibleCountSpan = document.getElementById('current-susceptible-count');
     const spreadStatusSpan = document.getElementById('spread-status');


    // Update span values when sliders move
    bindingEfficiencyInput.addEventListener('input', () => {
        bindingEfficiencyValueSpan.textContent = bindingEfficiencyInput.value;
    });
    densityInput.addEventListener('input', () => {
        densityValueSpan.textContent = densityInput.value;
    });
    replicationSpeedInput.addEventListener('input', () => {
        replicationSpeedValueSpan.textContent = replicationSpeedInput.value;
    });


    // Simulation variables
    let population = []; // Array of objects { state: 0/1, pos: {x, y}, infectedTime: 0 }
    // State: 0 = Susceptible, 1 = Infected, 2 = Recovered (Optional, keeping it simple for now: 0=Susceptible, 1=Infected)
    let simulationRunning = false;
    let simulationInterval = null;
    let currentTime = 0;
    let infectedCountHistory = [];
    let susceptibleCountHistory = [];


    // Drawing and Grid variables
    const CELL_SIZE = 25; // Size of each visual representation
    let GRID_WIDTH, GRID_HEIGHT, COLS, ROWS;
    const GRID_PADDING = 15; // Padding inside canvas container

    // Colors
    const COLORS = {
        susceptible: '#a0e7e5', // Light Teal
        infected: '#ff6b6b', // Red-orange
        recovered: '#c8d7e1', // Light Gray-blue (if implemented)
        outline: '#77c4c2', // Teal for susceptible outline
        infectedOutline: '#e63946', // Darker red for infected outline
        background: '#e9ecef',
        graphLine: '#e63946', // Matching infected color
        graphAxes: '#333',
    };

    // --- Simulation Setup ---
    function setupSimulation() {
        const populationSize = parseInt(populationSizeInput.value, 10);
        const initialInfections = parseInt(initialInfectionsInput.value, 10);

        // Validate inputs
        if (initialInfections > populationSize) {
            alert("Initial infections cannot be more than population size!");
            initialInfectionsInput.value = populationSize;
            return; // Stop setup
        }

        // Determine grid size based on population size
        // Aim for a squarish layout within the canvas limits
        const maxCanvasWidth = 450 - 2 * GRID_PADDING;
        const maxCanvasHeight = 450 - 2 * GRID_PADDING;
        const maxCols = Math.floor(maxCanvasWidth / CELL_SIZE);
        const maxRows = Math.floor(maxCanvasHeight / CELL_SIZE);

        COLS = Math.min(maxCols, Math.ceil(Math.sqrt(populationSize)));
        ROWS = Math.ceil(populationSize / COLS);

        // Adjust canvas dimensions
        simulationCanvas.width = COLS * CELL_SIZE + 2 * GRID_PADDING;
        simulationCanvas.height = ROWS * CELL_SIZE + 2 * GRID_PADDING;
        GRID_WIDTH = COLS * CELL_SIZE;
        GRID_HEIGHT = ROWS * CELL_SIZE;


        population = [];
        const allIndices = Array.from({ length: populationSize }, (_, i) => i);
        // Shuffle indices for random initial placement and infection
        shuffleArray(allIndices);

        for (let i = 0; i < populationSize; i++) {
            const index = allIndices[i];
            const row = Math.floor(index / COLS);
            const col = index % COLS;
            const x = col * CELL_SIZE + GRID_PADDING + CELL_SIZE / 2; // Center X
            const y = row * CELL_SIZE + GRID_PADDING + CELL_SIZE / 2; // Center Y

            population.push({
                state: 0, // 0: Susceptible
                pos: { x, y },
                infectedTime: 0 // Time step when infected (or 0 if not infected)
            });
        }

        // Infect initial individuals
        const initialIndices = allIndices.slice(0, initialInfections);
        initialIndices.forEach(index => {
             population[index].state = 1; // 1: Infected
             population[index].infectedTime = 0; // Infected at time 0
        });

        currentTime = 0;
        const initialInfectedCount = population.filter(p => p.state === 1).length;
        const initialSusceptibleCount = population.filter(p => p.state === 0).length;
        infectedCountHistory = [{ time: 0, count: initialInfectedCount }];
        susceptibleCountHistory = [{ time: 0, count: initialSusceptibleCount }];


        // Update stats display
        currentTimeSpan.textContent = currentTime;
        currentInfectedCountSpan.textContent = initialInfectedCount;
        currentSusceptibleCountSpan.textContent = initialSusceptibleCount;
         spreadStatusSpan.textContent = 'ממתין להרצה';


        drawSimulation();
        drawGraph();

        runButton.style.display = 'block';
        resetButton.style.display = 'none';
        // Enable controls before simulation starts
        toggleControls(true);
    }

    // Utility to shuffle array (Fisher-Yates)
    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
        return array;
    }

    // --- Simulation Logic (one step) ---
    function updateSimulation() {
        if (!simulationRunning) return;

        currentTime++;
        let newlyInfectedIndices = [];
        const populationSize = population.length;
        const density = parseInt(densityInput.value, 10); // Max potential contacts per infected individual
        const bindingEfficiency = parseInt(bindingEfficiencyInput.value, 10); // 1-10
        const replicationSpeed = parseInt(replicationSpeedInput.value, 10); // 1-10
        const structure = structureSelect.value; // 'naked' or 'enveloped'

        // Parameters mapping to infection probability / contact
        // Binding efficiency 1-10 -> 0.1 to 1 probability modifier for binding success
        const bindingModifier = bindingEfficiency / 10;
         // Replication speed 1-10 -> 1 to 10 for how many "viral particles" are produced per infected step
         const viralLoadModifier = replicationSpeed; // Represents how "infectious" a person becomes faster/more

        // Structure: Naked is more stable in environment, Enveloped might be better at cell entry
        // Let's model this as Naked having a slightly higher chance of successful transmission *per effective contact*,
        // implying environmental stability or easier cell-to-cell transfer in dense environments.
        // Enveloped might rely more on direct cell binding facilitated by envelope proteins.
        // For this model, simplify: Naked has a base transmission boost per contact.
        const structureModifier = (structure === 'naked') ? 1.2 : 0.8; // Naked 20% boost, Enveloped 20% reduction (relative example)

        // Base probability of transmission *per potential contact opportunity*
        // Combine factors: Binding affects if contact *leads to cell attachment*, Structure affects virus viability/entry.
        // Let's scale the base chance by binding and structure, and scale the NUMBER of *effective* contacts by viral load and density.
         const baseTransmissionChance = bindingModifier * structureModifier; // Probability a *successful binding* leads to infection
         const effectiveContactsPerInfected = density * (viralLoadModifier / 5); // Example scaling: density * (replication/5)

        let currentInfectedCount = 0;

        // Find all currently infected individuals
        const infectedIndices = population
            .map((person, index) => person.state === 1 ? index : -1)
            .filter(index => index !== -1);

        if (infectedIndices.length === 0) {
             // No more infected individuals, stop simulation
             stopSimulation("המגפה הסתיימה - הוירוס נעלם.");
             return;
        }
         if (infectedIndices.length >= populationSize) {
            // Everyone is infected
            stopSimulation("כל האוכלוסיה נדבקה!");
            return;
         }


        // For each infected individual, simulate potential contacts and transmissions
        infectedIndices.forEach(infectedIndex => {
            currentInfectedCount++; // Count current infected

            const numContacts = Math.round(effectiveContactsPerInfected); // Actual number of contact attempts

            for (let i = 0; i < numContacts; i++) {
                // Choose a random person to contact
                const contactIndex = Math.floor(Math.random() * populationSize);

                // Avoid self-contact and contact with already infected/newly infected
                if (population[contactIndex].state === 0 && !newlyInfectedIndices.includes(contactIndex)) {
                    // Calculate probability of transmission for this specific contact
                    // This can be a simple check based on baseTransmissionChance
                    // Or a more complex one incorporating proximity in visual grid (if we wanted physical simulation)
                    // Let's keep it simpler for now, probability is baseTransmissionChance per contact attempt
                     if (Math.random() < baseTransmissionChance) {
                        // This susceptible person gets infected in the *next* step
                        newlyInfectedIndices.push(contactIndex);
                        // Optional: Visual feedback - maybe draw a line for this transmission? Could be too noisy.
                    }
                }
            }
        });

        // Apply new infections *after* all interactions for the current step are calculated
        newlyInfectedIndices.forEach(index => {
            population[index].state = 1; // Change state to infected
            population[index].infectedTime = currentTime; // Mark time of infection
        });


        // Record stats *after* state updates
        const totalInfected = population.filter(state => state.state === 1).length;
        const totalSusceptible = population.filter(state => state.state === 0).length;

         infectedCountHistory.push({ time: currentTime, count: totalInfected });
         susceptibleCountHistory.push({ time: currentTime, count: totalSusceptible });


         // Update stats display
        currentTimeSpan.textContent = currentTime;
        currentInfectedCountSpan.textContent = totalInfected;
        currentSusceptibleCountSpan.textContent = totalSusceptible;
         spreadStatusSpan.textContent = `נדבקו ${newlyInfectedIndices.length} פרטים חדשים`;


         // Check for stop conditions again after updating counts
         if (newlyInfectedIndices.length === 0 && totalInfected > 0) {
             stopSimulation("ההדבקה נעצרה, אך יש עדיין נדבקים.");
         } else if (totalInfected === populationSize) {
             stopSimulation("כל האוכלוסיה נדבקה!");
         } else if (totalInfected === 0) {
              stopSimulation("המגפה הסתיימה - הוירוס נעלם."); // Should be caught by initial check, but good fallback
         }


        // Draw
        drawSimulation();
        drawGraph();
    }

    // --- Drawing Functions ---
    function drawSimulation() {
        simulationCtx.clearRect(0, 0, simulationCanvas.width, simulationCanvas.height);
        simulationCtx.fillStyle = COLORS.background;
        simulationCtx.fillRect(0, 0, simulationCanvas.width, simulationCanvas.height);


        const populationSize = population.length;
        for (let i = 0; i < populationSize; i++) {
            const person = population[i];
            const state = person.state; // 0=Susceptible, 1=Infected
            const pos = person.pos;

            simulationCtx.beginPath();
            simulationCtx.arc(pos.x, pos.y, CELL_SIZE / 3, 0, Math.PI * 2, false); // Draw a circle representing a person

            if (state === 1) {
                simulationCtx.fillStyle = COLORS.infected;
                simulationCtx.strokeStyle = COLORS.infectedOutline;
            } else { // state === 0
                simulationCtx.fillStyle = COLORS.susceptible;
                simulationCtx.strokeStyle = COLORS.outline;
            }
            simulationCtx.lineWidth = 1;
            simulationCtx.fill();
            simulationCtx.stroke();

             // Optional: Animate recently infected individuals (simple pulse)
             if(state === 1 && currentTime - person.infectedTime < 5 && currentTime > 0) { // Pulse for the first few steps
                  const pulseSize = (5 - (currentTime - person.infectedTime)) / 5 * (CELL_SIZE / 3) * 1.5; // pulse gets smaller over time
                   simulationCtx.beginPath();
                   simulationCtx.arc(pos.x, pos.y, CELL_SIZE / 3 + pulseSize, 0, Math.PI * 2, false);
                   simulationCtx.strokeStyle = COLORS.infected;
                   simulationCtx.lineWidth = 2;
                   simulationCtx.globalAlpha = (5 - (currentTime - person.infectedTime)) / 5; // Fade out
                   simulationCtx.stroke();
                   simulationCtx.globalAlpha = 1.0; // Reset alpha
             }
        }

        // Optional: Draw grid lines for clarity
        /*
        simulationCtx.strokeStyle = '#ddd';
        simulationCtx.lineWidth = 0.5;
        for (let i = 0; i <= COLS; i++) {
            simulationCtx.beginPath();
            simulationCtx.moveTo(GRID_PADDING + i * CELL_SIZE, GRID_PADDING);
            simulationCtx.lineTo(GRID_PADDING + i * CELL_SIZE, GRID_PADDING + GRID_HEIGHT);
            simulationCtx.stroke();
        }
         for (let i = 0; i <= ROWS; i++) {
            simulationCtx.beginPath();
            simulationCtx.moveTo(GRID_PADDING, GRID_PADDING + i * CELL_SIZE);
            simulationCtx.lineTo(GRID_PADDING + GRID_WIDTH, GRID_PADDING + i * CELL_SIZE);
            simulationCtx.stroke();
        }
        */
    }

    function drawGraph() {
        graphCtx.clearRect(0, 0, graphCanvas.width, graphCanvas.height);
        graphCtx.fillStyle = COLORS.background; // Background
        graphCtx.fillRect(0, 0, graphCanvas.width, graphCanvas.height);


        // Graph padding and dimensions
        const padding = 35; // Increased padding for labels
        const graphWidth = graphCanvas.width - 2 * padding;
        const graphHeight = graphCanvas.height - 2 * padding;
        const originX = padding;
        const originY = padding + graphHeight;

        // Draw axes
        graphCtx.beginPath();
        graphCtx.moveTo(originX, padding); // Y-axis start
        graphCtx.lineTo(originX, originY); // Y-axis end
        graphCtx.lineTo(originX + graphWidth, originY); // X-axis end
        graphCtx.strokeStyle = COLORS.graphAxes;
        graphCtx.lineWidth = 1.5;
        graphCtx.stroke();

        // Labels
        graphCtx.fillStyle = COLORS.graphAxes;
        graphCtx.font = '12px Arial';

        // X-axis label
        graphCtx.textAlign = 'center';
        graphCtx.fillText("זמן (שלבי סימולציה)", originX + graphWidth / 2, graphCanvas.height - 5);

        // Y-axis label (rotated)
         graphCtx.save(); // Save current state
         graphCtx.translate(padding - 25, padding + graphHeight / 2); // Move origin
         graphCtx.rotate(-Math.PI / 2); // Rotate 90 degrees counter-clockwise
         graphCtx.textAlign = 'center';
         graphCtx.fillText("מספר פרטים", 0, 0); // Draw text at new origin
         graphCtx.restore(); // Restore original state


        // Find max values for scaling
        const maxTime = currentTime > 0 ? currentTime + 5 : 10; // Add some buffer + min time
        const populationSize = parseInt(populationSizeInput.value, 10);
        const maxY = populationSize > 0 ? populationSize : 100; // Max Y is population size


        // Draw Infected count line
        graphCtx.beginPath();
        graphCtx.strokeStyle = COLORS.graphLine; // Red for infected
        graphCtx.lineWidth = 2.5;

        infectedCountHistory.forEach((point) => {
            const x = originX + (point.time / maxTime) * graphWidth;
            const y = originY - (point.count / maxY) * graphHeight;

            if (point.time === infectedCountHistory[0].time) { // First point
                graphCtx.moveTo(x, y);
            } else {
                graphCtx.lineTo(x, y);
            }
        });
        graphCtx.stroke();


        // Draw Susceptible count line (Optional but helpful)
        graphCtx.beginPath();
        graphCtx.strokeStyle = COLORS.outline; // Blue/Teal for susceptible
        graphCtx.lineWidth = 2.5;

         susceptibleCountHistory.forEach((point) => {
             const x = originX + (point.time / maxTime) * graphWidth;
             const y = originY - (point.count / maxY) * graphHeight;

             if (point.time === susceptibleCountHistory[0].time) { // First point
                 graphCtx.moveTo(x, y);
             } else {
                 graphCtx.lineTo(x, y);
             }
         });
         graphCtx.stroke();


        // Draw axis ticks/labels
         graphCtx.fillStyle = COLORS.graphAxes;
         graphCtx.font = '10px Arial';

         // Y-axis ticks (simplified: 0 and MaxY)
         graphCtx.textAlign = 'right';
         graphCtx.textBaseline = 'middle';
         graphCtx.fillText("0", originX - 8, originY);
         graphCtx.fillText(maxY.toString(), originX - 8, padding);
         graphCtx.beginPath(); // Draw small ticks
         graphCtx.moveTo(originX, originY); graphCtx.lineTo(originX + 4, originY);
         graphCtx.moveTo(originX, padding); graphCtx.lineTo(originX + 4, padding);
          graphCtx.strokeStyle = COLORS.graphAxes;
         graphCtx.stroke();


         // X-axis ticks (simplified: 0 and MaxTime)
         graphCtx.textAlign = 'center';
         graphCtx.textBaseline = 'top';
         graphCtx.fillText("0", originX, originY + 8);
         graphCtx.fillText(maxTime.toString(), originX + graphWidth, originY + 8);
          graphCtx.beginPath(); // Draw small ticks
         graphCtx.moveTo(originX, originY); graphCtx.lineTo(originX, originY - 4);
         graphCtx.moveTo(originX + graphWidth, originY); graphCtx.lineTo(originX + graphWidth, originY - 4);
          graphCtx.strokeStyle = COLORS.graphAxes;
         graphCtx.stroke();


         // Legend (simple)
         graphCtx.fillStyle = COLORS.graphAxes;
         graphCtx.font = '11px Arial';
         graphCtx.textAlign = 'left';
         graphCtx.textBaseline = 'top';
         graphCtx.fillRect(originX + graphWidth - 80, padding + 5, 15, 5); // Infected color swatch
         graphCtx.fillStyle = COLORS.graphLine;
         graphCtx.fillRect(originX + graphWidth - 80, padding + 5, 15, 5);
          graphCtx.fillStyle = COLORS.graphAxes;
         graphCtx.fillText("נדבקים", originX + graphWidth - 60, padding + 3);

         graphCtx.fillRect(originX + graphWidth - 80, padding + 20, 15, 5); // Susceptible color swatch
         graphCtx.fillStyle = COLORS.outline;
         graphCtx.fillRect(originX + graphWidth - 80, padding + 20, 15, 5);
          graphCtx.fillStyle = COLORS.graphAxes;
         graphCtx.fillText("רגישים", originX + graphWidth - 60, padding + 18);


    }

    // --- Simulation Control ---
    function startSimulation() {
         if(simulationRunning) return; // Prevent multiple intervals

         // Reset only if not already running
         if(currentTime > 0) {
             setupSimulation();
         }

        simulationRunning = true;
        runButton.style.display = 'none';
        resetButton.style.display = 'block';
         spreadStatusSpan.textContent = 'פועל...';
         toggleControls(false); // Disable controls while running
        simulationInterval = setInterval(updateSimulation, 150); // Run update every Xms (adjust for speed)
    }

     function stopSimulation(statusMessage = "הסימולציה נעצרה.") {
        simulationRunning = false;
        clearInterval(simulationInterval);
        simulationInterval = null;
         runButton.style.display = 'none'; // Keep run hidden after stopping
         resetButton.style.display = 'block'; // Show reset
         spreadStatusSpan.textContent = statusMessage;
         toggleControls(true); // Re-enable controls after stopping
    }

    function resetSimulation() {
        stopSimulation("הסימולציה אופסה.");
        setupSimulation(); // Re-initialize everything
    }

    function toggleControls(enable) {
         const controls = document.querySelectorAll('#controls input, #controls select, #controls button:not(#reset-simulation)');
         controls.forEach(control => {
             control.disabled = !enable;
             control.style.opacity = enable ? '1.0' : '0.6';
             control.style.cursor = enable ? 'pointer' : 'not-allowed';
         });
          // Always keep reset enabled if visible
         const resetButton = document.getElementById('reset-simulation');
         if (resetButton) {
             resetButton.disabled = false;
             resetButton.style.opacity = '1.0';
             resetButton.style.cursor = 'pointer';
         }
    }


    // --- Event Listeners ---
    runButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);


    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר 📖' : 'הצג/הסתר הסבר על וירוסים ומודלים 📚';
    });

    // Initial setup on page load
    setupSimulation();
     toggleControls(true); // Ensure controls are enabled initially

});
</script>