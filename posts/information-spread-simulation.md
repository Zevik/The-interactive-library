---
title: "מסעו של רעיון ברשת: הדמיית התפשטות מידע"
english_slug: "information-spread-simulation"
category: "כללי"
tags: ["רשתות חברתיות", "מודלים", "התפשטות", "ויזואליזציה", "אינטראקטיבי"]
---
# מסעו של רעיון ברשת: הדמיית התפשטות מידע (או ויראליות)

דמיינו רעיון חדש, טרנד לוהט, או אפילו פיסת מידע (אמיתי או כוזב) שמתחיל את דרכו אצל אדם אחד בלבד. איך הוא מתפשט? אילו גורמים קובעים אם הוא ישאר נישה קטנה או יהפוך לויראלי ויגיע לכל פינה ברשת?

ההדמיה האינטראקטיבית הזו מזמינה אתכם להפוך לחוקרים ולראות במו עיניכם איך מבנה הרשת וההתנהגות משפיעים על ה"ויראליות". שחקו עם ההגדרות, צפו בהתפשטות מתפתחת צעד אחר צעד, וגלו את הכוחות שמניעים את המידע ברשתות חברתיות ומעבר. מוכנים לצאת למסע?

<div class="simulation-container">
    <div class="controls interactive-card">
        <h2>הגדירו את העולם שלכם</h2>
        <p class="controls-intro">קבעו את כללי המשחק לפני שמתחילים:</p>
        <div class="param-group">
            <label for="numNodes">גודל הרשת (מספר משתמשים):</label>
            <input type="number" id="numNodes" value="100" min="10" max="500" step="10">
        </div>
        <div class="param-group">
            <label for="edgeProbability">צפיפות הקשרים (סיכוי ששני משתמשים יהיו חברים):</label>
            <input type="range" id="edgeProbability" min="0.01" max="0.1" step="0.005" value="0.03">
            <span id="edgeProbabilityValue" class="param-value">0.03</span>
        </div>
        <div class="param-group">
            <label for="infectionProbability">סיכוי ההדבקה (סיכוי שמידע יעבור בחברות אחת):</label>
            <input type="range" id="infectionProbability" min="0.1" max="1" step="0.05" value="0.5">
             <span id="infectionProbabilityValue" class="param-value">0.5</span>
        </div>
         <div class="param-group">
            <label for="simulationSpeed">קצב ההתפשטות (מהירות הסימולציה):</label>
            <input type="range" id="simulationSpeed" min="50" max="500" step="10" value="150">
             <span id="simulationSpeedValue" class="param-value">150 מ"ש לצעד</span>
        </div>
        <div class="param-group">
             <label for="startNodeIndex">מוביל הדעה הראשון (מספר משתמש 0-):</label>
            <input type="number" id="startNodeIndex" value="0" min="0">
             <p class="hint">אפשר גם ללחוץ על משתמש ברשת כדי לבחור אותו!</p>
        </div>

        <button id="generateNetworkBtn" class="action-button primary">בנו לי רשת חדשה!</button>
        <button id="startSimulationBtn" class="action-button secondary">התחילו את ההתפשטות</button>
        <button id="resetSimulationBtn" class="action-button tertiary">התחילו מחדש</button>

        <div class="status interactive-card">
            <h3>מצב נוכחי</h3>
            <p>סטטוס רשת: <span id="networkStatus">לא נוצרה</span></p>
            <p>משתמשים מודעים למידע: <span id="infectedCount">0</span></p>
        </div>
        <div class="legend interactive-card">
            <h3>מקרא ויזואלי</h3>
             <div class="legend-item"><span class="legend-color susceptible"></span> עדיין לא נחשפו (פוטנציאליים)</div>
             <div class="legend-item"><span class="legend-color infected"></span> נחשפו ומפיצים (מודעים)</div>
             <div class="legend-item"><span class="legend-color start-node"></span> מוביל הדעה ההתחלתי</div>
        </div>

    </div>
    <div class="canvas-container interactive-card">
        <canvas id="networkCanvas"></canvas>
    </div>
</div>

<button id="toggleExplanationBtn" class="explanation-button action-button secondary">הצגת סיפור הרקע: מה באמת קורה כאן?</button>

<div id="explanation" class="explanation-section interactive-card hidden">
    <h2>הסבר: המדע מאחורי ההתפשטות (מודל SI פשוט)</h2>
    <p>ההדמיה ששיחקתם איתה מבוססת על רעיון מתמטי פשוט ומודל בסיסי בתחום האפידמיולוגיה וחקר רשתות - <strong>מודל SI (Susceptible-Infected)</strong>. למרות פשטותו, הוא כלי רב עוצמה להבנת דינמיקות של התפשטות, בין אם מדובר בנגיף ביולוגי, בטרנד אופנתי, או במידע שרץ ברשת.</p>

    <h3>השחקנים הראשיים במודל זה:</h3>
    <ul>
        <li><strong>צמתים (Nodes):</strong> תחשבו עליהם כעל המשתתפים הפעילים ברשת - אנשים, חשבונות ברשת חברתית, או כל יחידה אחרת שיכולה "להחזיק" ולהעביר את המידע. לכל צומת יש מצב אחד בלבד:
            <ul>
                <li><strong>Susceptible (פוטנציאלי/חשוף):</strong> הצומת שטרם פגש את המידע, אך יכול לקבל אותו מחבר ברשת. הם מוצגים באפור עדין.</li>
                <li><strong>Infected (נגוע/מודע/מפיץ):</strong> הצומת שקיבל את המידע וכעת פעיל בהעברתו הלאה לחבריו. הם מתעוררים לחיים בצבע האדום.</li>
            </ul>
        </li>
        <li><strong>קשרים (Edges):</strong> אלו הצינורות שדרכם המידע זורם - חברות, עוקבים, קשר מקצועי, או כל סוג של אינטראקציה המאפשרת העברה. המידע יכול להתפשט אך ורק לאורך הקשרים הללו.</li>
    </ul>

    <h3>איך ההגדרות שלכם משפיעות?</h3>
    <ul>
        <li><strong>גודל הרשת:</strong> קובע את קהל היעד הפוטנציאלי. רשת גדולה יותר מאפשרת התפשטות רחבה יותר (אם התנאים מאפשרים).</li>
        <li><strong>צפיפות הקשרים:</strong> מגדירה כמה "חברים" יש בממוצע לכל משתמש. רשת "מחוברת" יותר (צפיפות גבוהה) יוצרת יותר נתיבים פוטנציאליים למידע לזרום, ומאפשרת לרוב התפשטות מהירה יותר. ההדמיה כאן משתמשת במודל "ארדש-רניי" שבו קשרים נוצרים באקראי בין כל זוג משתמשים עם הסתברות נתונה.</li>
        <li><strong>סיכוי ההדבקה:</strong> זהו הסיכוי הקריטי שהמידע אכן "ידביק" צומת פוטנציאלי כאשר הוא בא במגע עם צומת מודע. סיכוי גבוה יותר אומר שהמידע "מדבק" יותר או שהמשתמשים "פתוחים" יותר לקבל אותו.</li>
        <li><strong>מוביל הדעה הראשון:</strong> הצומת היחיד שמתחיל עם המידע. מיקום הצומת הזה ברשת (למשל, האם הוא "מרכזי" עם הרבה קשרים?) יכול להשפיע דרמטית על קצב וטווח ההתפשטות ההתחלתי.</li>
        <li><strong>קצב ההתפשטות:</strong> רק קובע את קצב צעדי הסימולציה, לא את הדינמיקה עצמה.</li>
    </ul>

    <h3>מה קורה בכל צעד של ההדמיה?</h3>
    <p>הסימולציה מתחילה כאשר רק "מוביל הדעה הראשון" במצב "מודע", והיתר "פוטנציאליים". בכל "צעד זמן" וירטואלי מתרחש הדבר הבא:</p>
    <ol>
        <li>כל המשתמשים ה"מודעים" בוחנים את חבריהם.</li>
        <li>עבור כל חבר שעדיין "פוטנציאלי", המשתמש ה"מודע" מנסה להעביר לו את המידע.</li>
        <li>ניסיון ההעברה מצליח (והחבר עובר למצב "מודע") בהסתברות שקבעתם כ"סיכוי ההדבקה".</li>
        <li>משתמשים שהפכו ל"מודעים" בצעד הנוכחי יתחילו בעצמם להפיץ את המידע החל מהצעד הבא.</li>
        <li>הדמיה זו מבוססת על מודל SI טהור - אין "שכחה" או "התחסנות". משתמש שנדבק נשאר במצב "מודע" לצמיתות.</li>
    </ol>
    <p>הסימולציה ממשיכה עד שכל מי שיכול להיחשף למידע כבר נחשף (אין יותר משתמשים פוטנציאליים המחוברים למשתמשים מודעים) או שכל המשתמשים מודעים. אתם יכולים לעקוב אחר התהליך על ידי שינוי הצבעים של הצמתים וספירת המשתמשים המודעים בזמן אמת.</p>

    <h3>תובנות שאפשר ללמוד:</h3>
    <ul>
        <li>רשתות "צפופות" יותר (יותר קשרים) ו"מידע מדבק" יותר (סיכוי הדבקה גבוה) לרוב מובילים להתפשטות מהירה ונרחבת יותר.</li>
        <li>בחירת "מוביל הדעה" ההתחלתי משנה: התחלה מצומת "מרכזי" עם הרבה קשרים (hub) יכולה לגרום להתפשטות מהירה ויעילה יותר מאשר התחלה מצומת "שולי".</li>
        <li>אפילו ברשת מחוברת היטב, "מידע" שאינו "מדבק" מספיק (סיכוי הדבקה נמוך) עלול להיכשל מלהתפשט משמעותית ולהגיע לכל המשתמשים הפוטנציאליים.</li>
    </ul>
    <p>זכרו שמודל SI הוא נקודת התחלה. מודלים מורכבים יותר קיימים (כמו SIR, SIS ועוד) וכוללים מצבים נוספים (כמו החלמה או נשאות חבויה) ותכונות נוספות של הרשת והמידע, אך מודל SI מספק יסוד מוצק והדמיה חזותית אינטואיטיבית לכוחות הבסיסיים הפועלים בהתפשטות.</p>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #6c757d; /* Grey */
        --tertiary-color: #28a745; /* Green */
        --susceptible-color: #ced4da; /* Lighter grey */
        --infected-color: #dc3545; /* Red */
        --start-node-color: #ffc107; /* Yellow/Orange */
        --background-color: #e9ecef; /* Light grey background */
        --card-background: #ffffff;
        --border-color: #dee2e6;
        --text-color: #343a40;
        --canvas-background: #f8f9fa; /* White/light background for canvas */
        --edge-color: #adb5bd; /* Medium grey for edges */
        --highlight-pulse-color: rgba(220, 53, 69, 0.5); /* Semi-transparent red for pulse */
    }

    body {
        font-family: 'Heebo', sans-serif; /* Use Heebo for a modern Hebrew feel */
        line-height: 1.7;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700; /* Bold headings */
    }

    h2, h3 {
        text-align: right; /* Align section headings to the right */
    }

    p {
        margin-bottom: 1em;
    }

    .simulation-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
        margin-bottom: 30px;
    }

    .interactive-card {
        background-color: var(--card-background);
        padding: 25px; /* Increased padding */
        border-radius: 10px; /* More rounded corners */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
        border: 1px solid var(--border-color); /* Subtle border */
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effect */
    }

     .interactive-card:hover {
         /* transform: translateY(-3px); */ /* Subtle lift on hover */
         box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
     }

    .controls {
        flex: 1 1 350px; /* Allow controls to be wider */
        min-width: 300px;
        display: flex;
        flex-direction: column;
        gap: 20px; /* Increased gap between control groups */
    }

    .controls-intro {
        font-size: 1.1em;
        color: var(--secondary-color);
        margin-top: -10px; /* Pull closer to heading */
        margin-bottom: 25px;
        text-align: center;
    }

    .canvas-container {
        flex: 2 1 600px; /* Allow canvas to be wider */
        min-width: 500px;
        background-color: var(--canvas-background);
        border-radius: 10px;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid var(--border-color); /* Consistent border */
    }

    canvas {
        max-width: 100%;
        height: auto;
        display: block;
    }

    .param-group {
        display: flex;
        flex-direction: column;
        gap: 8px; /* Increased gap */
        padding-bottom: 15px;
        border-bottom: 1px dashed var(--border-color); /* Subtle separator */
    }

     .param-group:last-of-type {
         border-bottom: none;
         padding-bottom: 0;
     }


    .param-group label {
        font-weight: bold;
        font-size: 1em; /* Slightly larger font */
        color: var(--text-color);
    }

    .param-group input[type="number"],
    .param-group input[type="range"] {
        width: 100%;
        padding: 10px; /* More padding */
        border: 1px solid var(--border-color);
        border-radius: 5px; /* Slightly more rounded */
        box-sizing: border-box;
        font-size: 1em;
    }

     input[type="range"] {
         -webkit-appearance: none;
         appearance: none;
         height: 10px; /* Thicker track */
         background: var(--border-color);
         outline: none;
         opacity: 0.9; /* Slightly less transparent by default */
         transition: opacity .2s, background-color .2s;
         border-radius: 5px;
     }

     input[type="range"]:hover {
         opacity: 1;
         background-color: #ced4da; /* Slightly darker track on hover */
     }

     input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px; /* Larger thumb */
         height: 20px; /* Larger thumb */
         background: var(--primary-color);
         cursor: pointer;
         border-radius: 50%;
         border: 3px solid var(--card-background); /* Clearer border */
         transition: background-color 0.2s ease;
     }

      input[type="range"]::-webkit-slider-thumb:hover {
          background-color: #0056b3;
      }


     input[type="range"]::-moz-range-thumb {
         width: 20px; /* Larger thumb */
         height: 20px; /* Larger thumb */
         background: var(--primary-color);
         cursor: pointer;
         border-radius: 50%;
         border: 3px solid var(--card-background); /* Clearer border */
         transition: background-color 0.2s ease;
     }

     input[type="range"]::-moz-range-thumb:hover {
         background-color: #0056b3;
     }

    .param-group .param-value {
        font-size: 0.9em;
        color: var(--secondary-color);
        text-align: left;
        margin-top: 5px;
    }

    .hint {
        font-size: 0.9em;
        color: var(--secondary-color);
        margin-top: 5px;
    }

    .action-button {
        display: block; /* Make buttons block level for consistent spacing */
        width: 100%;
        background-color: var(--primary-color);
        color: white;
        border: none;
        padding: 12px 20px; /* More padding */
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        font-weight: 600;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 10px; /* Space between buttons */
        text-align: center;
    }

    .action-button.primary {
        background-color: var(--primary-color);
    }

     .action-button.primary:hover {
         background-color: #0056b3;
         transform: translateY(-1px);
     }

    .action-button.secondary {
        background-color: var(--secondary-color);
    }
     .action-button.secondary:hover {
         background-color: #5a6268;
         transform: translateY(-1px);
     }

     .action-button.tertiary {
         background-color: var(--tertiary-color);
     }
      .action-button.tertiary:hover {
          background-color: #218838;
          transform: translateY(-1px);
      }


    button:disabled {
        background-color: #cccccc !important; /* Use important to override other classes */
        cursor: not-allowed;
        transform: none; /* Remove lift effect */
    }

    .status, .legend {
        margin-top: 20px; /* More space */
        padding-top: 20px;
        border-top: 1px dashed var(--border-color);
    }

     .status h3, .legend h3 {
         text-align: right;
         margin-top: 0;
         margin-bottom: 10px;
         color: var(--text-color); /* Status/Legend titles in text color */
         font-weight: 600;
     }

    .status p {
        margin: 8px 0; /* Increased margin */
        font-size: 1em;
    }

    .status span {
        font-weight: bold;
        color: var(--primary-color); /* Highlight status values */
    }

     .legend-item {
         display: flex;
         align-items: center;
         margin-bottom: 8px;
         font-size: 1em;
     }

     .legend-color {
         display: inline-block;
         width: 20px; /* Larger color swatch */
         height: 20px; /* Larger color swatch */
         margin-left: 10px; /* Adjust margin for RTL */
         border-radius: 4px;
         border: 1px solid rgba(0,0,0,0.1); /* Subtle border */
     }

     .legend-color.susceptible { background-color: var(--susceptible-color); }
     .legend-color.infected { background-color: var(--infected-color); }
     .legend-color.start-node { background-color: var(--start-node-color); }


    .explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More space above/below */
        padding: 12px 25px; /* More padding */
    }

    .explanation-section {
        margin-top: 30px; /* More space above */
        padding: 30px; /* More padding */
    }

    .explanation-section ul {
        padding-right: 20px;
        list-style: disc; /* Use discs for list items */
    }

     .explanation-section li {
         margin-bottom: 10px;
     }

    .hidden {
        display: none;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .simulation-container {
            flex-direction: column;
        }

        .controls, .canvas-container {
            flex: 1 1 100%; /* Stack columns */
            min-width: 100%;
        }
         body {
             padding: 10px;
         }
         .interactive-card {
             padding: 15px;
         }
         .param-group {
             padding-bottom: 10px;
             gap: 5px;
         }
         .action-button {
             padding: 10px 15px;
             font-size: 1em;
         }
    }

</style>

<script>
    const canvas = document.getElementById('networkCanvas');
    const ctx = canvas.getContext('2d');

    const numNodesInput = document.getElementById('numNodes');
    const edgeProbabilityInput = document.getElementById('edgeProbability');
    const edgeProbabilityValueSpan = document.getElementById('edgeProbabilityValue');
    const infectionProbabilityInput = document.getElementById('infectionProbability');
    const infectionProbabilityValueSpan = document.getElementById('infectionProbabilityValue');
    const simulationSpeedInput = document.getElementById('simulationSpeed');
    const simulationSpeedValueSpan = document.getElementById('simulationSpeedValue');
    const startNodeIndexInput = document.getElementById('startNodeIndex');
    const generateNetworkBtn = document.getElementById('generateNetworkBtn');
    const startSimulationBtn = document.getElementById('startSimulationBtn');
    const resetSimulationBtn = document.getElementById('resetSimulationBtn');
    const networkStatusSpan = document.getElementById('networkStatus');
    const infectedCountSpan = document.getElementById('infectedCount');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationDiv = document.getElementById('explanation');

    let nodes = [];
    let edges = []; // adjacency list
    let nodeStates = []; // 0: Susceptible, 1: Infected
    let simulationRunning = false;
    let simulationInterval = null;
    let numNodes = 100;
    let edgeProbability = 0.03;
    let infectionProbability = 0.5;
    let simulationSpeed = 150; // ms per step
    let startNodeIndex = 0;
    let newlyInfectedInStep = []; // To highlight nodes newly infected in the current step

    const nodeRadius = 6; // Slightly larger nodes
    const susceptibleColor = 'var(--susceptible-color)';
    const infectedColor = 'var(--infected-color)';
    const startNodeColor = 'var(--start-node-color)';
    const edgeColor = 'var(--edge-color)';
    const highlightPulseColor = 'var(--highlight-pulse-color)'; // For animation effect

    // --- Parameter Updates ---
    edgeProbabilityInput.addEventListener('input', (e) => {
        edgeProbability = parseFloat(e.target.value);
        edgeProbabilityValueSpan.textContent = edgeProbability.toFixed(3); // Display 3 decimal places
    });
     infectionProbabilityInput.addEventListener('input', (e) => {
        infectionProbability = parseFloat(e.target.value);
        infectionProbabilityValueSpan.textContent = infectionProbability.toFixed(2); // Display 2 decimal places
    });
    simulationSpeedInput.addEventListener('input', (e) => {
        simulationSpeed = parseInt(e.target.value, 10);
        simulationSpeedValueSpan.textContent = simulationSpeed + " מ\"ש לצעד";
         if (simulationRunning) {
             // If simulation is running, restart interval with new speed
             clearInterval(simulationInterval);
             simulationInterval = setInterval(runSimulationStep, simulationSpeed);
         }
    });
     numNodesInput.addEventListener('change', (e) => {
         const newValue = parseInt(e.target.value, 10);
         if (!isNaN(newValue) && newValue >= parseInt(numNodesInput.min) && newValue <= parseInt(numNodesInput.max)) {
              numNodes = newValue;
             startNodeIndexInput.max = numNodes > 0 ? numNodes - 1 : 0; // Update max allowed start node index
             if (startNodeIndex >= numNodes) { // Adjust start node if it's out of new bounds
                 startNodeIndex = numNodes > 0 ? 0 : -1; // Use -1 if no nodes possible
                 startNodeIndexInput.value = startNodeIndex > -1 ? startNodeIndex : '';
             }
             // Note: Network is regenerated only on button click, not just number change
         } else {
             e.target.value = numNodes; // Revert if invalid input
         }
     });
     startNodeIndexInput.addEventListener('change', (e) => {
         const newValue = parseInt(e.target.value, 10);
          if (!isNaN(newValue) && newValue >= parseInt(startNodeIndexInput.min) && newValue <= parseInt(startNodeIndexInput.max)) {
             startNodeIndex = newValue;
             // Optionally reset simulation immediately when start node changes via input
             if (!simulationRunning) {
                 resetSimulation();
             }
         } else {
             // Revert if out of bounds or invalid
             startNodeIndexInput.value = startNodeIndex;
         }
     });

    // --- Network Generation ---
    function generateNetwork() {
        numNodes = parseInt(numNodesInput.value, 10);
        edgeProbability = parseFloat(edgeProbabilityInput.value);

        if (numNodes <= 0) {
             alert("מספר הצמתים חייב להיות חיובי.");
             return;
         }

        nodes = [];
        edges = Array.from({ length: numNodes }, () => []); // Adjacency list

        // Place nodes in a circle for visibility
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = Math.min(centerX, centerY) * 0.85; // Use a bit more of the canvas

        for (let i = 0; i < numNodes; i++) {
            const angle = (i / numNodes) * Math.PI * 2;
            nodes.push({
                id: i,
                x: centerX + radius * Math.cos(angle),
                y: centerY + radius * Math.sin(angle),
            });
        }

        // Generate edges (Erdos-Renyi model)
        // Ensure at least a few connections if possible, though Erdos-Renyi can produce isolated nodes
        for (let i = 0; i < numNodes; i++) {
            for (let j = i + 1; j < numNodes; j++) {
                if (Math.random() < edgeProbability) {
                    edges[i].push(j);
                    edges[j].push(i); // Undirected graph
                }
            }
        }

        networkStatusSpan.textContent = `נוצרה בהצלחה (${numNodes} משתמשים, ${getEdgeCount()} קשרים)`;
        resetSimulation(); // Reset state for the new network
        startNodeIndexInput.max = numNodes > 0 ? numNodes - 1 : 0;
         if (startNodeIndex >= numNodes || startNodeIndex < 0) { // Handle case where old index is out of new bounds
             startNodeIndex = numNodes > 0 ? 0 : -1;
             startNodeIndexInput.value = startNodeIndex > -1 ? startNodeIndex : '';
         }
        drawNetwork(); // Draw the initial state
    }

     function getEdgeCount() {
         let count = 0;
         for(let i = 0; i < edges.length; i++) {
             count += edges[i].length;
         }
         return count / 2; // Since it's an undirected graph
     }

    // --- Drawing ---
    function drawNetwork() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw edges
        ctx.strokeStyle = edgeColor;
        ctx.lineWidth = 1;
        for (let i = 0; i < numNodes; i++) {
            for (const neighborIndex of edges[i]) {
                 // Avoid drawing the same edge twice
                 if (i < neighborIndex) {
                    ctx.beginPath();
                    ctx.moveTo(nodes[i].x, nodes[i].y);
                    ctx.lineTo(nodes[neighborIndex].x, nodes[neighborIndex].y);
                    ctx.stroke();
                 }
            }
        }

        // Draw nodes
        nodes.forEach((node, i) => {
             const isNewlyInfected = newlyInfectedInStep.includes(i);
             const isStartNode = i === startNodeIndex;

            ctx.beginPath();
            // Draw a slightly larger circle temporarily for newly infected for a visual pulse
            if (isNewlyInfected) {
                 ctx.arc(node.x, node.y, nodeRadius * 1.5, 0, Math.PI * 2, false);
                 ctx.fillStyle = highlightPulseColor;
                 ctx.fill();
            }


            ctx.beginPath();
            ctx.arc(node.x, node.y, nodeRadius, 0, Math.PI * 2, false);
            ctx.fillStyle = nodeStates[i] === 1 ? infectedColor : susceptibleColor;
            ctx.fill();

            // Draw border, special for start node or newly infected
            ctx.lineWidth = isStartNode ? 3 : (isNewlyInfected ? 2 : 1); // Thicker border for start/newly infected
            ctx.strokeStyle = isStartNode ? startNodeColor : '#fff'; // Yellowish border for start, white for others
            ctx.stroke();
        });

         newlyInfectedInStep = []; // Clear highlight list after drawing

    }

    // --- Simulation Logic ---
    function resetSimulation() {
        stopSimulation(); // Ensure any running simulation stops

        // Use current values from inputs
        startNodeIndex = parseInt(startNodeIndexInput.value, 10);
        numNodes = parseInt(numNodesInput.value, 10); // Ensure consistency if numNodes changed

        if (!nodes || nodes.length !== numNodes || numNodes === 0) {
             // Regenerate network if node count changed or no network exists
             generateNetwork();
             return; // generateNetwork calls resetSimulation again after creating nodes/edges
        }


        nodeStates = Array(numNodes).fill(0); // All susceptible initially
        newlyInfectedInStep = [];

         if (startNodeIndex >= 0 && startNodeIndex < numNodes) {
             nodeStates[startNodeIndex] = 1; // Set start node as infected
         } else if (numNodes > 0) {
             // If chosen start node is invalid, default to 0
             startNodeIndex = 0;
             startNodeIndexInput.value = 0;
             nodeStates[startNodeIndex] = 1;
         }

        infectedCountSpan.textContent = nodeStates.filter(state => state === 1).length;


        startSimulationBtn.disabled = false;
        generateNetworkBtn.disabled = false; // Re-enable generation
         networkStatusSpan.textContent = `מוכן להתפשטות (${numNodes} משתמשים, ${getEdgeCount()} קשרים)`;
        drawNetwork(); // Draw the reset state
    }

    function runSimulationStep() {
        if (!nodes || nodes.length === 0) {
             stopSimulation();
             return;
        }

        const potentiallyNewlyInfected = new Set(); // Use a Set to avoid duplicates and quickly check existence
        let stateChanged = false;

        // Identify potential new infections
        for (let i = 0; i < numNodes; i++) {
            if (nodeStates[i] === 1) { // If node i is infected
                // Iterate through its neighbors
                for (const neighborIndex of edges[i]) {
                    // If the neighbor is susceptible and not already marked for infection in this step
                    if (nodeStates[neighborIndex] === 0 && !potentiallyNewlyInfected.has(neighborIndex)) {
                        // Check if infection occurs based on probability
                        if (Math.random() < infectionProbability) {
                            potentiallyNewlyInfected.add(neighborIndex); // Mark for infection
                        }
                    }
                }
            }
        }

         // Apply infections (only after checking all potential transmissions in this step)
         newlyInfectedInStep = []; // Reset highlight list for this step
         if (potentiallyNewlyInfected.size > 0) {
              stateChanged = true;
             potentiallyNewlyInfected.forEach(nodeIndex => {
                  if (nodeStates[nodeIndex] === 0) { // Double check, shouldn't be necessary with Set but good practice
                     nodeStates[nodeIndex] = 1;
                     newlyInfectedInStep.push(nodeIndex); // Add to highlight list
                  }
             });
         }


        // Update infected count display
        infectedCountSpan.textContent = nodeStates.filter(state => state === 1).length;


        // Redraw network with updated states and highlights
        drawNetwork();

        // Stop simulation if no new infections occurred or all nodes are infected
        if (!stateChanged || nodeStates.filter(state => state === 1).length === numNodes) {
            stopSimulation();
            networkStatusSpan.textContent += ' - ההתפשטות הסתיימה';
        }
    }

    function startSimulation() {
        if (simulationRunning) return; // Prevent starting multiple times
        if (!nodes || nodes.length === 0) {
            alert("אנא צור רשת חדשה תחילה!");
            return;
        }
         if (nodeStates.filter(state => state === 1).length === 0 && numNodes > 0) {
              // Ensure a start node is set if the network exists
             if (startNodeIndex < 0 || startNodeIndex >= numNodes) {
                  startNodeIndex = 0;
                  startNodeIndexInput.value = 0;
             }
             nodeStates[startNodeIndex] = 1; // Set the start node as infected if not already
             infectedCountSpan.textContent = '1';
             drawNetwork(); // Draw with the initial infected node
         }

         if (nodeStates.filter(state => state === 1).length === 0 && numNodes === 0) {
             alert("אנא צור רשת חדשה תחילה!");
             return;
         }
         if (nodeStates.filter(state => state === 0).length === 0) {
             alert("כל הצמתים כבר נגועים. אפס את ההדמיה כדי להתחיל מחדש.");
             return;
         }


        simulationRunning = true;
        startSimulationBtn.disabled = true;
        generateNetworkBtn.disabled = true; // Disable generating new network during simulation
        networkStatusSpan.textContent = 'ההתפשטות בעיצומה...';

        simulationInterval = setInterval(runSimulationStep, simulationSpeed);
    }

    function stopSimulation() {
        if (simulationInterval) {
            clearInterval(simulationInterval);
            simulationInterval = null;
        }
        simulationRunning = false;
        startSimulationBtn.disabled = false;
        generateNetworkBtn.disabled = false; // Re-enable generation
    }

    // --- Canvas Click for Start Node Selection ---
    canvas.addEventListener('click', (event) => {
         if (simulationRunning || !nodes || nodes.length === 0) return;

         const rect = canvas.getBoundingClientRect();
         const scaleX = canvas.width / rect.width;    // Relationship bitmap vs. display pixels
         const scaleY = canvas.height / rect.height;  // Relationship bitmap vs. display pixels

         const mouseX = (event.clientX - rect.left) * scaleX;
         const mouseY = (event.clientY - rect.top) * scaleY;

         // Find the closest node clicked
         let clickedNodeIndex = -1;
         for (let i = 0; i < nodes.length; i++) {
             const node = nodes[i];
             const dist = Math.sqrt((mouseX - node.x)**2 + (mouseY - node.y)**2);
             if (dist < nodeRadius + 5) { // Add a small buffer for easier clicking
                 clickedNodeIndex = i;
                 break;
             }
         }

         if (clickedNodeIndex !== -1) {
             startNodeIndex = clickedNodeIndex;
             startNodeIndexInput.value = startNodeIndex; // Update input field
             resetSimulation(); // Reset with the newly selected start node
         }
    });


    // --- Event Listeners ---
    generateNetworkBtn.addEventListener('click', generateNetwork);
    startSimulationBtn.addEventListener('click', startSimulation);
    resetSimulationBtn.addEventListener('click', resetSimulation);

    toggleExplanationBtn.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
         if (explanationDiv.classList.contains('hidden')) {
             toggleExplanationBtn.textContent = 'הצגת סיפור הרקע: מה באמת קורה כאן?';
             explanationDiv.style.maxHeight = '0'; // Collapse animation preparation
             explanationDiv.style.opacity = '0';
             explanationDiv.style.overflow = 'hidden';
              // Reset styles after transition for proper display when shown again
             explanationDiv.addEventListener('transitionend', function handler() {
                 if (explanationDiv.classList.contains('hidden')) {
                     explanationDiv.style.display = 'none'; // Fully hide
                 }
                 explanationDiv.removeEventListener('transitionend', handler);
             });


         } else {
              explanationDiv.style.display = 'block'; // Show block for height calculation
              // Wait a moment for display:block to take effect before setting height
              requestAnimationFrame(() => {
                 const scrollHeight = explanationDiv.scrollHeight; // Get natural height
                 explanationDiv.style.maxHeight = scrollHeight + 'px';
                 explanationDiv.style.opacity = '1';
                 explanationDiv.style.overflow = 'visible'; // Allow content overflow if needed after expansion
              });
             toggleExplanationBtn.textContent = 'הסתרת סיפור הרקע';
         }
    });

    // Add animation to explanation section
    explanationDiv.style.transition = 'max-height 0.5s ease-in-out, opacity 0.5s ease-in-out';
    explanationDiv.style.overflow = 'hidden'; // Hide overflow during transition
    explanationDiv.style.maxHeight = '0'; // Start collapsed
    explanationDiv.style.opacity = '0'; // Start hidden

    // --- Initial Setup ---
    function initialize() {
         // Set initial canvas size (can be made responsive later)
         const canvasContainer = document.querySelector('.canvas-container');
         canvas.width = canvasContainer.offsetWidth;
         canvas.height = Math.max(canvasContainer.offsetWidth * 0.7, 450); // Maintain aspect ratio, min height 450

        // Sync initial values from inputs to display spans
        edgeProbabilityValueSpan.textContent = parseFloat(edgeProbabilityInput.value).toFixed(3);
        infectionProbabilityValueSpan.textContent = parseFloat(infectionProbabilityInput.value).toFixed(2);
        simulationSpeedValueSpan.textContent = simulationSpeedInput.value + " מ\"ש לצעד";
        startNodeIndexInput.max = numNodes - 1;
         startNodeIndexInput.value = startNodeIndex; // Ensure input reflects default

        generateNetwork(); // Generate a network on page load
    }

     // Make canvas responsive (basic)
     window.addEventListener('resize', () => {
         const canvasContainer = document.querySelector('.canvas-container');
         canvas.width = canvasContainer.offsetWidth;
         canvas.height = Math.max(canvasContainer.offsetWidth * 0.7, 450);
         drawNetwork(); // Redraw network on resize
     });

    initialize(); // Run initial setup
</script>