---
title: "איך רעיון טוב הופך לטרנד עולמי? סימולטור השפעה חברתית והתפשטות חדשנות"
english_slug: how-new-technology-conquers-the-world-innovation-diffusion-simulator
category: "מדעי החברה / סוציולוגיה ואנתרופולוגיה"
tags: ["חדשנות", "התפשטות", "טכנולוגיה", "אימוץ", "מודלים חברתיים", "השפעה חברתית", "אפקטים רשתיים"]
---
# איך רעיון טוב הופך לטרנד עולמי? סימולטור השפעה חברתית והתפשטות חדשנות

מכירים את זה שיש מוצר חדש, רעיון מהפכני או טרנד תרבותי שפתאום כולם מדברים עליו, מאמצים אותו ומטמיעים אותו בחייהם? מה גורם לחידושים מסוימים להתפשט כמו אש בשדה קוצים, בעוד אחרים נשארים בגדר סקרנות נקודתית? האם ההצלחה היא רק עניין של המוצר עצמו, או שיש כוחות חברתיים נסתרים הפועלים מתחת לפני השטח, ומשפיעים על האופן שבו רעיונות וטכנולוגיות מתפשטים באוכלוסייה?

מסע מרתק אל לב הרשת החברתית: הסימולטור הזה מזמין אתכם לגלות בעצמכם כיצד אינטראקציות פשוטות בין אנשים יכולות לייצר דפוסים מורכבים של אימוץ, ולחקור את הדינמיקה הנסתרת שמאחורי תופעות כמו התפשטות ויראלית, קבלת חיסונים, או אימוץ סמארטפונים.

<div id="app-container">
    <div id="controls">
        <h2>שליטה במסלול החדשנות</h2>
        <p class="controls-intro">שחקו עם הפרמטרים כדי לראות איך הם משפיעים על קצב וצורת ההתפשטות:</p>
        <div>
            <label for="population-size">גודל הקהילה:</label>
            <input type="number" id="population-size" value="150" min="50" max="400">
             <span class="control-unit">אנשים</span>
        </div>
        <div>
            <label for="network-density">רשת הקשרים (ממוצע קשרים לאדם):</label>
            <input type="range" id="network-density" value="6" min="2" max="25">
            <span id="density-value" class="control-value">6</span>
             <span class="control-unit">קשרים</span>
        </div>
        <div>
            <label for="initial-adopters">החלוצים (אחוז מאמצים ראשוניים):</label>
            <input type="range" id="initial-adopters" value="3" min="1" max="15">
            <span id="initial-adopters-value" class="control-value">3%</span>
             <span class="control-unit">%</span>
        </div>
         <div>
            <label for="adoption-threshold">סף ההשפעה (אחוז שכנים מאמצים לדרישה):</label>
            <input type="range" id="adoption-threshold" value="25" min="0" max="100">
            <span id="threshold-value" class="control-value">25%</span>
             <span class="control-unit">%</span>
        </div>
         <div>
            <label for="adoption-speed">קצב התפשטות (מהירות הסימולציה):</label>
            <input type="range" id="adoption-speed" value="400" min="50" max="1500">
            <span id="speed-value" class="control-value">0.4 שניות</span>
             <span class="control-unit">לצעד</span>
        </div>
        <div class="button-group">
            <button id="start-simulation">התחילו את המהפכה!</button>
            <button id="step-simulation">צעד אחד קדימה</button>
            <button id="reset-simulation">התחילו מחדש</button>
        </div>
    </div>
    <div id="visualization">
        <div id="network-vis-container" class="vis-container">
             <h3>רשת חברתית</h3>
             <canvas id="network-canvas"></canvas>
             <div class="legend">
                 <span class="legend-item"><span class="legend-color unadopted"></span> טרם אימצו</span>
                 <span class="legend-item"><span class="legend-color transitioning"></span> שוקלים אימוץ</span>
                 <span class="legend-item"><span class="legend-color adopted"></span> אימצו</span>
             </div>
        </div>
         <div id="graph-vis-container" class="vis-container">
             <h3>קצב האימוץ לאורך זמן</h3>
            <canvas id="graph-canvas"></canvas>
         </div>
    </div>
</div>

<button id="toggle-explanation">הצג הסבר מעמיק</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: מאחורי הקלעים של התפשטות חידושים</h2>

    <p>הסימולטור ששיחקתם איתו מדגים מודל בסיסי לאופן שבו חידושים (רעיונות, מוצרים, טכנולוגיות, נורמות חברתיות) מתפשטים בתוך קהילה או אוכלוסייה. התהליך הזה, הנקרא "התפשטות חידושים" (Diffusion of Innovations), הוא תחום מחקר מרתק במדעי החברה, הכלכלה והשיווק, ומסייע להבין למה דברים מסוימים הופכים לפופולריים במהירות, בעוד אחרים נכשלים.</p>

    <h3>הכוחות המניעים: חידושים, קשרים וספים</h3>
    <p>בלב הסימולטור עומדים שלושה אלמנטים מרכזיים:</p>
    <ol>
        <li><strong>הרשת החברתית:</strong> הנקודות מייצגות אנשים (או גורמים מאמצים אחרים כמו ארגונים), והקווים מייצגים קשרים או ערוצי תקשורת ביניהם (חברות, משפחה, עמיתים, קשרים עסקיים). החידוש עובר מאדם לאדם דרך הקשרים האלה. צפיפות הקשרים (כמה קשרים ממוצעים יש לכל אדם) משפיעה דרמטית על מהירות ההתפשטות.</li>
        <li><strong>המאמצים הראשוניים:</strong> קבוצה קטנה של "חלוצים" או "מחדשים" המאמצים את החידוש ראשונים, לעיתים ללא השפעה חיצונית משמעותית. הם מקור ההתחלה להתפשטות ברשת.</li>
        <li><strong>סף האימוץ:</strong> זהו "כלל ההחלטה" של כל אדם. הוא מייצג את מידת ההשפעה החברתית שנדרשת כדי שאדם יאמץ את החידוש. בסימולטור, אדם שעדיין לא אימץ את החידוש ישקול לאמץ אותו אם מספיק מחבריו או שכניו ברשת (אחוז מסוים מהקשרים שלו) כבר עשו זאת. סף גבוה יותר אומר שנדרשת השפעה רבה יותר, מה שיאט את קצב ההתפשטות או אף יעצור אותה. סף נמוך יותר יכול להוביל להתפשטות מהירה ואף "ויראלית".</li>
    </ol>
    <p> בכל צעד בסימולציה, כל אדם שעדיין לא אימץ את החידוש בודק את שכניו המאמצים. אם אחוז השכנים המאמצים עולה על סף האימוץ שקבעתם, הוא יחליט לאמץ את החידוש בצעד הבא.</p>


    <h3>הקשר למודל של אוורט רוג'רס (Everett Rogers)</h3>
    <p>מודל זה שואב השראה רבה מעבודתו החלוצית של אוורט רוג'רס, סוציולוג שחקר לעומק את תהליכי התפשטות חידושים. רוג'רס הדגיש את ההיבט החברתי בתהליך וחילק את המאמצים לחמש קטגוריות עיקריות:</p>
    <ul>
        <li><strong>מחדשים (Innovators):</strong> האחוז הקטן של האוכלוסייה המאמץ חידושים מיד כשהם זמינים (בסימולטור: הנקודות שמתחילות בצבע המאומץ).</li>
        <li><strong>מאמצים מוקדמים (Early Adopters):</strong> משפיענים חברתיים שמקבלים את החידוש לאחר שהמחדשים סללו את הדרך. הם קריטיים להעברת החידוש לרוב האוכלוסייה (בסימולטור: אלו המקבלים את החידוש בשלבים הראשונים, מושפעים מהחלוצים ומשפיעים על אחרים).</li>
        <li><strong>רוב מוקדם (Early Majority):</strong> הקבוצה הגדולה שמאמצת חידוש לאחר שהוכיח את עצמו וזכה ללגיטימציה חברתית (בסימולטור: הנקודות שמשנות צבען בחלק המרכזי והתלול של העקומה).</li>
        <li><strong>רוב מאוחר (Late Majority):</strong> קבוצה שמרנית יותר שמאמצת רק כשהחידוש הפך לנורמה או הכרח (בסימולטור: אלו שמאמצים בשלבים המאוחרים יותר של הסימולציה).</li>
        <li><strong>מתמהמהים (Laggards):</strong> האחרונים לאמץ, לרוב חשדנים ובעלי קשרים מוגבלים (בסימולטור: הנקודות הבודדות או המבודדות שמשנות צבען אחרונות, אם בכלל).</li>
    </ul>
    <p>הגרף בסימולטור מציג את עקומת ה-S הקלאסית של התפשטות: אימוץ איטי בהתחלה (החלוצים), התאוצה משמעותית כשהרוב המוקדם מצטרף, ולבסוף האטה כשהשוק מתקרב לרוויה והנותרים הם בעיקר המתמהמהים.</p>

    <h3>פרמטרים ואתגרים בעולם האמיתי</h3>
    <p>בעוד שהסימולטור הוא מודל פשטני, הוא עוזר להמחיש עקרונות יסוד. בעולם האמיתי, קצב ומידת ההתפשטות מושפעים מעוד גורמים רבים, כולל:</p>
    <ul>
        <li><strong>מאפייני החידוש:</strong> עד כמה הוא טוב יותר מהקיים (יתרון יחסי), קל להבנה/שימוש (מורכבות), תואם לערכים והרגלים קיימים (תאימות), ניתן לניסוי (יכולת ניסוי), ותוצאותיו נראות לעין (יכולת צפייה).</li>
        <li><strong>ערוצי תקשורת:</strong> לא רק קשרים ישירים, אלא גם תקשורת המונים (מדיה, פרסום) ותקשורת בין-אישית פורמלית ובלתי פורמלית.</li>
        <li><strong>המערכת החברתית:</strong> הנורמות, הערכים, והמבנה החברתי של הקהילה המאמצת.</li>
        <li><strong>פעילות מכוונת:</strong> מאמצי שיווק, הסברה או מדיניות המעודדים או בולמים את האימוץ.</li>
    </ul>
    <p>נסו לשנות את הפרמטרים בסימולטור וצפו כיצד שינויים קטנים, כמו הגדלת סף האימוץ או הקטנת צפיפות הרשת, יכולים לשנות לחלוטין את תוצאת ההתפשטות - מכישלון לכיסוי מלא של האוכלוסייה.</p>
</div>

<style>
    #app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: 'Arial', sans-serif; /* Using Arial as a safe default */
        direction: rtl;
        text-align: right;
        margin-bottom: 30px;
        background-color: #fafafa; /* Soft background */
        padding: 20px 10px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    }

    #controls {
        background-color: #e0e0e0; /* Lighter control background */
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        width: 98%;
        max-width: 400px; /* More fixed width for controls */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
         box-sizing: border-box; /* Include padding in width */
    }

    #controls h2 {
        margin-top: 0;
        text-align: center;
        color: #333;
        border-bottom: 2px solid #ccc;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

     .controls-intro {
         text-align: center;
         margin-bottom: 20px;
         color: #555;
         font-size: 0.95rem;
     }

    #controls > div {
        margin-bottom: 18px; /* More space between controls */
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    #controls label {
        margin-left: 10px;
        min-width: 180px; /* Ensure labels have enough space */
        text-align: right;
        font-weight: bold;
        color: #555;
    }

    #controls input[type="number"],
    #controls input[type="range"] {
        flex-grow: 1;
        margin-right: 10px;
         vertical-align: middle;
    }

     #controls input[type="number"] {
         max-width: 80px; /* Smaller number input */
         padding: 5px;
         border: 1px solid #ccc;
         border-radius: 4px;
     }

    #controls span.control-value {
        min-width: 40px; /* Space for value display */
        text-align: left;
        font-weight: bold;
        color: #007bff; /* Highlight values */
    }

     #controls span.control-unit {
         min-width: 40px; /* Space for unit */
         text-align: left;
         color: #777;
         font-size: 0.9em;
     }

    .button-group {
        display: flex;
        justify-content: center;
        gap: 10px; /* Space between buttons */
        margin-top: 25px;
        flex-wrap: wrap; /* Allow buttons to wrap on small screens */
    }

    #controls button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.2s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #controls button:hover {
        transform: translateY(-1px); /* Lift button slightly on hover */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    #controls button:active {
         transform: translateY(0);
         box-shadow: none;
    }


    #start-simulation {
        background-color: #4CAF50; /* Green */
        color: white;
    }

    #start-simulation:hover {
        background-color: #45a049;
    }

    #step-simulation {
        background-color: #2196F3; /* Blue */
        color: white;
    }
     #step-simulation:hover {
        background-color: #0b7dda;
    }


    #reset-simulation {
        background-color: #f44336; /* Red */
        color: white;
    }

    #reset-simulation:hover {
        background-color: #da190b;
    }

     button#toggle-explanation {
         display: block;
         width: fit-content;
         margin: 30px auto;
         padding: 12px 25px;
         background-color: #ddd;
         border: none;
         border-radius: 5px;
         cursor: pointer;
         font-size: 1rem;
         transition: background-color 0.2s ease, transform 0.1s ease;
         font-weight: bold;
     }

     button#toggle-explanation:hover {
        background-color: #ccc;
         transform: translateY(-1px);
     }

     button#toggle-explanation:active {
         transform: translateY(0);
     }


    #visualization {
        display: flex;
        flex-direction: column; /* Stack canvases vertically */
        align-items: center;
        width: 98%;
        max-width: 800px;
         box-sizing: border-box;
    }

    .vis-container {
        width: 100%;
        background-color: #fff;
        border: 1px solid #e0e0e0; /* Softer border */
        border-radius: 8px;
        margin-bottom: 20px; /* Space between containers */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        padding: 15px;
         box-sizing: border-box;
    }

    .vis-container h3 {
        text-align: center;
        color: #555;
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.2rem;
    }

    #network-canvas {
        width: 100%; /* Make canvas fill container width */
        height: auto; /* Maintain aspect ratio (set by JS constants) */
        display: block; /* Remove extra space below canvas */
    }

    #graph-canvas {
        width: 100%; /* Make canvas fill container width */
         height: auto; /* Maintain aspect ratio */
         display: block;
    }

     .legend {
         text-align: center;
         margin-top: 15px;
         font-size: 0.9em;
         color: #555;
     }

     .legend-item {
         display: inline-block;
         margin: 0 10px;
     }

     .legend-color {
         display: inline-block;
         width: 12px;
         height: 12px;
         border-radius: 50%;
         margin-left: 5px;
         vertical-align: middle;
         border: 1px solid #333;
     }

     .legend-color.unadopted { background-color: #cccccc; }
     .legend-color.transitioning { background-color: #aed581; } /* Lighter green for pulse */
     .legend-color.adopted { background-color: #4CAF50; }

    #explanation {
        background-color: #f9f9f9; /* Light background */
        padding: 25px;
        margin-top: 20px;
        border-radius: 8px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.7; /* Improved readability */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: #333;
        margin-top: 25px;
        margin-bottom: 12px;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }

     #explanation h2 {
         font-size: 1.8rem;
     }

     #explanation h3 {
         font-size: 1.4rem;
         color: #555;
     }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Indent lists */
        margin-bottom: 15px;
        padding-right: 0; /* Remove default padding */
    }

    #explanation li {
        margin-bottom: 10px; /* More space between list items */
    }

     #explanation p {
         margin-bottom: 15px;
     }

    @media (min-width: 768px) {
         #app-container {
             flex-direction: row;
             align-items: flex-start;
             padding: 30px; /* More padding on larger screens */
         }
        #controls {
            width: 320px; /* Fixed width for controls on larger screens */
            margin-left: 30px; /* Space between controls and visualization */
             margin-bottom: 0;
             flex-shrink: 0; /* Prevent controls from shrinking */
        }
        #visualization {
            flex-grow: 1; /* Visualization takes remaining space */
            max-width: calc(100% - 350px); /* Adjust max-width considering controls */
        }
        .vis-container {
            padding: 20px;
        }
    }

     /* Basic focus outline for accessibility */
     input:focus, button:focus {
         outline: 2px solid #007bff;
         outline-offset: 2px;
     }
</style>

<script>
    const networkCanvas = document.getElementById('network-canvas');
    const graphCanvas = document.getElementById('graph-canvas');
    const ctxNetwork = networkCanvas.getContext('2d');
    const ctxGraph = graphCanvas.getContext('2d');

    const populationSizeInput = document.getElementById('population-size');
    const networkDensityInput = document.getElementById('network-density');
    const densityValueSpan = document.getElementById('density-value');
    const initialAdoptersInput = document.getElementById('initial-adopters');
    const initialAdoptersValueSpan = document.getElementById('initial-adopters-value');
    const adoptionThresholdInput = document.getElementById('adoption-threshold');
    const thresholdValueSpan = document.getElementById('threshold-value');
    const adoptionSpeedInput = document.getElementById('adoption-speed');
    const speedValueSpan = document.getElementById('speed-value');

    const startSimulationButton = document.getElementById('start-simulation');
    const stepSimulationButton = document.getElementById('step-simulation');
    const resetSimulationButton = document.getElementById('reset-simulation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let nodes = [];
    let edges = [];
    let simulationRunning = false;
    let simulationInterval = null;
    let currentStep = 0;
    let adoptionHistory = []; // Stores percentage of adopted nodes at each step

    // Node states
    const STATE_UNADOPTED = 0; // Gray/White
    const STATE_TRANSITIONING = 1; // Indicates node will adopt next step (pulsing/pending color)
    const STATE_ADOPTED = 2; // Green

    // Colors
    const NODE_COLOR_UNADOPTED = '#cccccc'; // Gray
    const NODE_COLOR_TRANSITIONING = '#aed581'; // Light green for pulse/transition
    const NODE_COLOR_ADOPTED = '#4CAF50'; // Green
    const EDGE_COLOR = '#eeeeee'; // Light gray
    const GRAPH_LINE_COLOR = '#4CAF50'; // Green
    const GRAPH_AXIS_COLOR = '#333333'; // Dark gray
    const BACKGROUND_COLOR_NETWORK = '#ffffff'; // White background for network canvas
    const BACKGROUND_COLOR_GRAPH = '#ffffff'; // White background for graph canvas


    // Canvas sizes (proportional, CSS will handle scaling)
    const NETWORK_WIDTH = 600;
    const NETWORK_HEIGHT = 400;
    const GRAPH_WIDTH = 600;
    const GRAPH_HEIGHT = 250; /* Slightly taller graph */

    // Set canvas base dimensions - CSS handles display size
    networkCanvas.width = NETWORK_WIDTH;
    networkCanvas.height = NETWORK_HEIGHT;
    graphCanvas.width = GRAPH_WIDTH;
    graphCanvas.height = GRAPH_HEIGHT;


     // Node drawing parameters
     const NODE_RADIUS = 5;
     const NODE_BORDER_COLOR = '#333333';
     const NODE_BORDER_WIDTH = 1;
     const TRANSITION_PULSE_MAX_RADIUS = 8; // For pulsing animation
     const TRANSITION_PULSE_SPEED = 0.1; // How fast the pulse expands/contracts

    // --- Update slider value displays ---
    networkDensityInput.addEventListener('input', () => {
        densityValueSpan.textContent = networkDensityInput.value;
    });
    initialAdoptersInput.addEventListener('input', () => {
        initialAdoptersValueSpan.textContent = `${initialAdoptersInput.value}%`;
    });
    adoptionThresholdInput.addEventListener('input', () => {
        thresholdValueSpan.textContent = `${adoptionThresholdInput.value}%`;
    });
     adoptionSpeedInput.addEventListener('input', () => {
        speedValueSpan.textContent = `${(adoptionSpeedInput.value / 1000).toFixed(1)} שניות`;
    });


    // --- Network Generation ---
    function createNetwork(numNodes, density, initialAdoptersPercentage) {
        nodes = [];
        edges = [];
        currentStep = 0;
        adoptionHistory = [];

        // Create nodes with random positions
        for (let i = 0; i < numNodes; i++) {
            nodes.push({
                id: i,
                x: Math.random() * NETWORK_WIDTH,
                y: Math.random() * NETWORK_HEIGHT,
                state: STATE_UNADOPTED,
                neighbors: [],
                pendingState: STATE_UNADOPTED, // State for the next step
                 pulse: 0 // For animation
            });
        }

        // Create edges using a simple random approach to approximate density
        // This tries to connect each node to 'density' others. Can result in uneven distribution.
        const potentialEdges = [];
        for (let i = 0; i < numNodes; i++) {
            for (let j = i + 1; j < numNodes; j++) {
                 potentialEdges.push({ from: i, to: j });
            }
        }

        // Shuffle potential edges
        for (let i = potentialEdges.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [potentialEdges[i], potentialEdges[j]] = [potentialEdges[j], potentialEdges[i]];
        }

        // Select edges up to the target number (numNodes * density / 2) or max potential
        const targetEdgeCount = Math.min(potentialEdges.length, Math.floor(numNodes * density / 2));
        for (let i = 0; i < targetEdgeCount; i++) {
             const edge = potentialEdges[i];
             edges.push(edge);
             nodes[edge.from].neighbors.push(nodes[edge.to]);
             nodes[edge.to].neighbors.push(nodes[edge.from]);
        }


        // Assign initial adopters
        const numInitialAdopters = Math.max(1, Math.floor(numNodes * initialAdoptersPercentage / 100));
         // Shuffle nodes to pick initial adopters randomly
        const shuffledNodes = nodes.slice();
        for (let i = shuffledNodes.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffledNodes[i], shuffledNodes[j]] = [shuffledNodes[j], shuffledNodes[i]];
        }
        for (let i = 0; i < numInitialAdopters; i++) {
             // Ensure the node exists before setting state
            if (shuffledNodes[i]) {
                 shuffledNodes[i].state = STATE_ADOPTED;
                 shuffledNodes[i].pendingState = STATE_ADOPTED;
            }
        }
    }

    // --- Drawing ---
    function drawNetwork() {
        ctxNetwork.clearRect(0, 0, NETWORK_WIDTH, NETWORK_HEIGHT);
         ctxNetwork.fillStyle = BACKGROUND_COLOR_NETWORK;
         ctxNetwork.fillRect(0, 0, NETWORK_WIDTH, NETWORK_HEIGHT);


        // Draw edges
        ctxNetwork.strokeStyle = EDGE_COLOR;
        ctxNetwork.lineWidth = 1;
        edges.forEach(edge => {
            const node1 = nodes.find(n => n.id === edge.from);
            const node2 = nodes.find(n => n.id === edge.to);
            if (node1 && node2) {
                ctxNetwork.beginPath();
                ctxNetwork.moveTo(node1.x, node1.y);
                ctxNetwork.lineTo(node2.x, node2.y);
                ctxNetwork.stroke();
            }
        });

        // Draw nodes and handle animations
        nodes.forEach(node => {
            ctxNetwork.beginPath();
            let radius = NODE_RADIUS;
            let color = NODE_COLOR_UNADOPTED;

            if (node.state === STATE_ADOPTED) {
                color = NODE_COLOR_ADOPTED;
            } else if (node.state === STATE_TRANSITIONING) {
                // Pulse animation
                node.pulse = (node.pulse + TRANSITION_PULSE_SPEED) % (Math.PI * 2); // Cycle pulse value
                radius = NODE_RADIUS + (TRANSITION_PULSE_MAX_RADIUS - NODE_RADIUS) * Math.abs(Math.sin(node.pulse / 2)); // Pulse effect
                color = NODE_COLOR_TRANSITIONING;
            }

            ctxNetwork.arc(node.x, node.y, radius, 0, Math.PI * 2);
            ctxNetwork.fillStyle = color;
            ctxNetwork.fill();
            ctxNetwork.lineWidth = NODE_BORDER_WIDTH;
            ctxNetwork.strokeStyle = NODE_BORDER_COLOR;
            ctxNetwork.stroke();
        });

         // Request animation frame if simulation is running and there are transitioning nodes
         if (simulationRunning || nodes.some(node => node.state === STATE_TRANSITIONING)) {
             requestAnimationFrame(drawNetwork);
         }
    }

    function drawGraph() {
        ctxGraph.clearRect(0, 0, GRAPH_WIDTH, GRAPH_HEIGHT);
         ctxGraph.fillStyle = BACKGROUND_COLOR_GRAPH;
         ctxGraph.fillRect(0, 0, GRAPH_WIDTH, GRAPH_HEIGHT);

        // Graph padding
        const PADDING_LEFT = 50;
        const PADDING_BOTTOM = 40;
        const PADDING_TOP = 20;
        const PADDING_RIGHT = 20;

        const graphWidth = GRAPH_WIDTH - PADDING_LEFT - PADDING_RIGHT;
        const graphHeight = GRAPH_HEIGHT - PADDING_TOP - PADDING_BOTTOM;

        // Draw axes
        ctxGraph.strokeStyle = GRAPH_AXIS_COLOR;
        ctxGraph.lineWidth = 1;
        ctxGraph.beginPath();
        ctxGraph.moveTo(PADDING_LEFT, PADDING_TOP); // Y axis start
        ctxGraph.lineTo(PADDING_LEFT, GRAPH_HEIGHT - PADDING_BOTTOM); // Y axis end
        ctxGraph.lineTo(GRAPH_WIDTH - PADDING_RIGHT, GRAPH_HEIGHT - PADDING_BOTTOM); // X axis end
        ctxGraph.stroke();

        // Draw labels
        ctxGraph.fillStyle = GRAPH_AXIS_COLOR;
        ctxGraph.font = '12px Arial';
        ctxGraph.textAlign = 'center';
        ctxGraph.textBaseline = 'top';
         // Y axis label (rotated) - requires advanced canvas or external lib. Simplified: place text near axis.
        ctxGraph.textAlign = 'right';
        ctxGraph.fillText('% אימוץ', PADDING_LEFT - 10, PADDING_TOP + graphHeight / 2 - 20);

        ctxGraph.textAlign = 'center';
        ctxGraph.textBaseline = 'top';
        ctxGraph.fillText('צעדי זמן', PADDING_LEFT + graphWidth / 2, GRAPH_HEIGHT - PADDING_BOTTOM + 15);


        // Draw Y-axis ticks and labels
        ctxGraph.textAlign = 'right';
        ctxGraph.textBaseline = 'middle';
        for (let i = 0; i <= 100; i += 20) {
             const y = GRAPH_HEIGHT - PADDING_BOTTOM - (i / 100) * graphHeight;
             ctxGraph.fillText(i + '%', PADDING_LEFT - 5, y);
             ctxGraph.beginPath();
             ctxGraph.moveTo(PADDING_LEFT - 3, y);
             ctxGraph.lineTo(PADDING_LEFT, y);
             ctxGraph.stroke();
        }

        // Draw X-axis ticks (simplified)
        if (adoptionHistory.length > 0) {
            const maxSteps = adoptionHistory.length > 1 ? adoptionHistory.length - 1 : 1;
            const stepInterval = Math.max(1, Math.floor(maxSteps / 5)); // Show ~5-6 ticks

            ctxGraph.textAlign = 'center';
             ctxGraph.textBaseline = 'top';
            for (let i = 0; i <= maxSteps; i += stepInterval) {
                 const x = PADDING_LEFT + (i / maxSteps) * graphWidth;
                 ctxGraph.fillText(i, x, GRAPH_HEIGHT - PADDING_BOTTOM + 5);
                 ctxGraph.beginPath();
                 ctxGraph.moveTo(x, GRAPH_HEIGHT - PADDING_BOTTOM);
                 ctxGraph.lineTo(x, GRAPH_HEIGHT - PADDING_BOTTOM + 3);
                 ctxGraph.stroke();
            }
             // Ensure the last step is shown if it's not already a tick
             if (maxSteps % stepInterval !== 0 && maxSteps > 0) {
                  const i = maxSteps;
                  const x = PADDING_LEFT + (i / maxSteps) * graphWidth;
                  ctxGraph.fillText(i, x, GRAPH_HEIGHT - PADDING_BOTTOM + 5);
                   ctxGraph.beginPath();
                  ctxGraph.moveTo(x, GRAPH_HEIGHT - PADDING_BOTTOM);
                  ctxGraph.lineTo(x, GRAPH_HEIGHT - PADDING_BOTTOM + 3);
                  ctxGraph.stroke();
             }
        }


        // Draw the adoption curve
        ctxGraph.strokeStyle = GRAPH_LINE_COLOR;
        ctxGraph.lineWidth = 3; /* Thicker line */
        ctxGraph.beginPath();
        if (adoptionHistory.length > 0) {
             const maxSteps = adoptionHistory.length > 1 ? adoptionHistory.length - 1 : 1;
            ctxGraph.moveTo(PADDING_LEFT, GRAPH_HEIGHT - PADDING_BOTTOM - (adoptionHistory[0] / 100) * graphHeight);
            for (let i = 1; i < adoptionHistory.length; i++) {
                const x = PADDING_LEFT + (i / maxSteps) * graphWidth;
                const y = GRAPH_HEIGHT - PADDING_BOTTOM - (adoptionHistory[i] / 100) * graphHeight;
                ctxGraph.lineTo(x, y);
            }
            ctxGraph.stroke();
        }
    }

    // --- Simulation Logic ---
    function calculateNextStep() {
        const adoptionThreshold = parseInt(adoptionThresholdInput.value) / 100; // as percentage
        const numNodes = nodes.length;
        let nodesChanged = 0; // Track if any nodes changed state this step

        // First pass: Determine pending states based on CURRENT states
        nodes.forEach(node => {
            // Only unadopted nodes can change state
            if (node.state === STATE_UNADOPTED) {
                let adoptedNeighborsCount = 0;
                node.neighbors.forEach(neighbor => {
                    // Check neighbor's state at the start of the step
                    if (neighbor.state === STATE_ADOPTED) {
                        adoptedNeighborsCount++;
                    }
                });

                const neighborInfluence = node.neighbors.length > 0 ? adoptedNeighborsCount / node.neighbors.length : 0;

                if (neighborInfluence >= adoptionThreshold) {
                    // Node is ready to adopt next step - transition to PENDING/TRANSITIONING
                    node.pendingState = STATE_TRANSITIONING;
                    nodesChanged++;
                     node.pulse = 0; // Start pulse animation
                } else {
                     // Node stays unadopted
                     node.pendingState = STATE_UNADOPTED;
                }
            } else if (node.state === STATE_TRANSITIONING) {
                 // Node that was transitioning now becomes ADOPTED
                 node.pendingState = STATE_ADOPTED;
                 nodesChanged++;
                 node.pulse = 0; // Stop pulse animation
            } else {
                 // Adopted nodes remain adopted
                 node.pendingState = STATE_ADOPTED;
            }
        });

        // Second pass: Apply the pending state changes simultaneously
        nodes.forEach(node => {
            node.state = node.pendingState;
        });

         currentStep++;
         recordAdoptionPercentage();

         // Check for simulation end (100% adoption or no more changes possible)
         const adoptedCount = nodes.filter(node => node.state === STATE_ADOPTED).length;
         // Simulation ends if all adopted OR if no nodes changed state in the last step (and not all are adopted)
         if (adoptedCount === numNodes || (nodesChanged === 0 && adoptedCount < numNodes)) {
             stopSimulation();
             const finalPercentage = ((adoptedCount / numNodes) * 100).toFixed(1);
             let endMessage = `הסימולציה הסתיימה בצעד ${currentStep} עם ${finalPercentage}% אימוץ.`;
             if (adoptedCount < numNodes) {
                 endMessage += " (אין שינויים נוספים צפויים עם הגדרות אלו).";
             } else {
                  endMessage += " (כל הקהילה אימצה את החידוש!).";
             }
             // Use a more visually appealing way to show this if possible without breaking structure,
             // maybe just log to console or update a status div, but alert is the current pattern.
             console.log(endMessage); // Log instead of alert for less interruption
         }

         // Request redraw regardless to continue animations if any
         requestAnimationFrame(drawNetwork);
         drawGraph(); // Graph redraw doesn't need RAF loop
    }

    function recordAdoptionPercentage() {
        const adoptedCount = nodes.filter(node => node.state === STATE_ADOPTED).length;
        const percentage = (nodes.length > 0 ? (adoptedCount / nodes.length) * 100 : 0);
        adoptionHistory.push(percentage);
    }

    function startSimulation() {
        if (simulationRunning) return;

         // If simulation was already run and finished, reset first
         if (adoptionHistory.length > 0 && (nodes.every(node => node.state === STATE_ADOPTED) || nodes.every(node => node.state !== STATE_UNADOPTED && node.state !== STATE_TRANSITIONING))) {
              resetSimulation(); // Reset if ended
         } else if (currentStep === 0 || nodes.length === 0) {
              // If starting fresh or after a full reset/page load
              resetSimulation(); // Ensure initial state is created
         }
         // If picking up from a paused simulation, just start the interval


        simulationRunning = true;
        const speed = parseInt(adoptionSpeedInput.value);
        simulationInterval = setInterval(() => {
            calculateNextStep();
             // Drawing is now handled by requestAnimationFrame called within calculateNextStep or drawNetwork
        }, speed);

         startSimulationButton.disabled = true; // Disable start while running
         stepSimulationButton.disabled = true; // Disable step while running
    }

    function stopSimulation() {
        simulationRunning = false;
        clearInterval(simulationInterval);
        simulationInterval = null;
         startSimulationButton.disabled = false; // Enable start
         stepSimulationButton.disabled = false; // Enable step
    }

    function stepSimulation() {
        if (simulationRunning) stopSimulation(); // Stop automatic run if stepping manually

         // If simulation was already run and finished, reset first
         if (adoptionHistory.length > 0 && (nodes.every(node => node.state === STATE_ADOPTED) || nodes.every(node => node.state !== STATE_UNADOPTED && node.state !== STATE_TRANSITIONING))) {
             resetSimulation(); // Reset if ended
         } else if (currentStep === 0 || nodes.length === 0) {
              // If starting fresh or after a full reset/page load
              resetSimulation(); // Ensure initial state is created
         }
         // If picking up from a paused simulation, just calculate one step


        calculateNextStep();
         // Drawing is handled by requestAnimationFrame called within calculateNextStep or drawNetwork
    }

    function resetSimulation() {
        stopSimulation();
        const numNodes = parseInt(populationSizeInput.value);
        const density = parseInt(networkDensityInput.value);
        const initialPercentage = parseInt(initialAdoptersInput.value);
        createNetwork(numNodes, density, initialPercentage);
        recordAdoptionPercentage(); // Record initial state (step 0)
        drawNetwork();
        drawGraph();
        currentStep = 0; // Ensure step count resets
         console.log("Simulation reset. Step:", currentStep);

         startSimulationButton.disabled = false;
         stepSimulationButton.disabled = false;
    }

    // --- Event Listeners ---
    startSimulationButton.addEventListener('click', startSimulation);
    stepSimulationButton.addEventListener('click', stepSimulation);
    resetSimulationButton.addEventListener('click', resetSimulation);

    // Reset when parameters change while not running
    populationSizeInput.addEventListener('change', resetSimulation);
    networkDensityInput.addEventListener('change', resetSimulation);
    initialAdoptersInput.addEventListener('change', resetSimulation);
    adoptionThresholdInput.addEventListener('change', resetSimulation);

     // Toggle explanation visibility
     toggleExplanationButton.addEventListener('click', () => {
         const isHidden = explanationDiv.style.display === 'none';
         explanationDiv.style.display = isHidden ? 'block' : 'none';
         toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק';
     });


    // --- Initial Setup ---
    window.onload = () => {
         // Set initial values for sliders/inputs
         densityValueSpan.textContent = networkDensityInput.value;
         initialAdoptersValueSpan.textContent = `${initialAdoptersInput.value}%`;
         thresholdValueSpan.textContent = `${adoptionThresholdInput.value}%`;
         speedValueSpan.textContent = `${(adoptionSpeedInput.value / 1000).toFixed(1)} שניות`;

        resetSimulation(); // Create and draw initial state on load
    };

    // Optional: Stop simulation if tab is inactive
     document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
            stopSimulation();
        }
     });


</script>
```