---
title: "מסע האדם הקדמון: הדמיית דפוסי הגירה"
english_slug: ancient-human-migration-patterns-simulation
category: "ארכאולוגיה"
tags:
  - הגירה אנושית
  - פרהיסטוריה
  - מודלים חישוביים
  - אבולוציה
  - ארכיאולוגיה
---
# מסע האדם הקדמון: הדמיית דפוסי הגירה

דמיינו את הערבה האפריקאית, לפני עשרות אלפי שנים. קבוצות קטנות של אנשים נודדות, מחפשות את המקום הבא שיספק להן מחסה ומזון. כיצד החלו אבות אבותינו במסע הכביר שהוביל אותם להתפשט בכל רחבי העולם? האם מסע ההגירה הגדול של האנושות היה רק סדרה של צעדים אקראיים, או שמא הוא נבע מחוקים פשוטים וברורים שהכתיבו את התנועה? בואו נבנה מודל דיגיטלי פשוט ונראה אילו דפוסים עשויים היו להיווצר במסע המרתק הזה.

<div class="simulation-container">
    <div id="simulationGrid" class="grid">
        <!-- Grid cells will be generated here by JavaScript -->
    </div>
    <!-- Agents will be appended directly to simulation-container for smooth movement -->

    <div class="controls-panel">
         <div class="controls">
             <button id="startButton">התחל מסע</button>
             <button id="stopButton" disabled>עצור מנוחה</button>
             <button id="resetButton">אפס הכל</button>
         </div>
         <div class="parameters">
             <div class="param-group">
                 <label for="numAgents">כמה קבוצות יוצאות לדרך?</label>
                 <input type="range" id="numAgents" min="1" max="50" value="10">
                 <span id="numAgentsValue">10</span>
             </div>
              <div class="param-group">
                 <label for="resourceAttraction">משיכה למשאבים:</label>
                 <input type="range" id="resourceAttraction" min="0" max="2" value="1" step="0.1">
                 <span id="resourceAttractionValue">1.0</span>
             </div>
              <div class="param-group">
                 <label for="obstacleCost">עלות מעבר מכשול (הרים):</label>
                 <input type="range" id="obstacleCost" min="0" max="5" value="2" step="0.1">
                 <span id="obstacleCostValue">2.0</span>
             </div>
               <div class="param-group">
                 <label for="simulationSpeed">מהירות הדמיה:</label>
                 <input type="range" id="simulationSpeed" min="50" max="1000" value="200" step="50">
                 <span id="simulationSpeedValue">200ms</span>
             </div>
         </div>
         <div class="stats">
             שלב הדמיה: <span id="simulationStepCount">0</span>
         </div>
         <div class="legend">
            <span class="legend-item"><span class="cell flat"></span> שטח מישורי (מעבר קל)</span>
            <span class="legend-item"><span class="cell mountain"></span> הר (מעבר קשה/חוסם)</span>
            <span class="legend-item"><span class="cell resource"></span> משאב (יעד משיכה)</span>
            <span class="legend-item"><span class="agent"></span> קבוצת נוודים</span>
        </div>
    </div>
</div>

<button id="toggleExplanation" class="toggle-explanation">צוללים לעומק: גלו את ההסבר המלא</button>

<div id="explanationContent" class="explanation" style="display: none;">
    <h2>מסע ההגירה הגדול: ממודלים פשוטים לתובנות על העבר הרחוק</h2>

    <p>איך הצליחו קבוצות קטנות של בני אדם קדמונים לכסות מרחקים עצומים ולהתפשט על פני יבשות שלמות, לפני עשרות ואף מאות אלפי שנים? חקר ההגירה האנושית הפרהיסטורית הוא שדה ידע מסעיר המשלב עדויות אילמות מהעבר - ממצאים ארכיאולוגיים, רמזים גנטיים הטמונים ב-DNA שלנו, ומודלים חישוביים שמנסים לפענח את ההיגיון מאחורי התנועה. האתגר המרכזי טמון כמובן בהיעדר תיעוד ישיר - אנחנו מסתמכים על שרידים מועטים ועל יכולתנו לבנות מודלים שמדמים תהליכים אפשריים.</p>

    <h3>מה הניע אותם לנוע? גורמי "משיכה" ו"דחייה"</h3>
    <p>ההגירה בימי קדם לא הייתה סתמית. היא נבעה ממניעים חיוניים להישרדות ולהתפתחות, שניתן לחלק לשתי קטגוריות ראשיות:</p>
    <ul>
        <li>**כוחות משיכה:** מחפשים אחר הטוב ביותר - מקורות מזון זמינים (אזורי ציד או ליקוט עשירים), גישה נוחה למים, אקלים שנעים יותר לחיות בו, או פשוט אזורים פחות צפופים שבהם התחרות על משאבים נמוכה יותר.</li>
        <li>**כוחות דחייה:** בורחים מפני הסכנה והמחסור - אזורים שבהם משאבים התדלדלו או אזלו כליל, סכנות מצד טורפים גדולים או קבוצות אנושיות יריבות, ותנאי אקלים שהפכו את השטח לעוין וקשה למחייה.</li>
    </ul>

    <h3>ההשפעה הדרמטית של פני השטח</h3>
    <p>הגיאוגרפיה שימשה ככוח מעצב עצום במסלולי ההגירה. רכסי הרים אדירים, מדבריות צחיחים, וימים ואוקיינוסים עצומים פעלו כמחסומים טבעיים, לעיתים בלתי עבירים, שהכתיבו נתיבי תנועה אפשריים. אפילו נהרות גדולים יכלו להוות מכשול רציני עד למציאת נקודות חצייה נוחות. לעומת זאת, עמקי נהרות פוריים או מעברים צרים בין הרים (מעברי הרים) יכלו להפוך לנתיבי תנועה ראשיים, מעין "כבישים מהירים" של התקופה הפרהיסטורית.</p>

    <h3>הצצה למודלים חישוביים: מודלים מבוססי סוכנים (Agent-Based Models)</h3>
    <p>ההדמיה שראיתם היא דוגמה פשוטה אך עוצמתית למודל מבוסס סוכנים (ABM). בשיטה זו, במקום לנסות לחזות את התנהגות המערכת כולה באופן ישיר, אנו מתמקדים ביצירת "סוכנים" וירטואליים (במקרה זה, כל סוכן מייצג קבוצה קטנה של אנשים). כל סוכן מקבל סט פשוט של כללים או "אינסטינקטים" שמכתיבים את התנהגותו בסביבה הדיגיטלית (המפה). ההדמיה מתקדמת בצעדי זמן, ובכל צעד, כל סוכן פועל לפי הכללים שלו, מגיב לסביבה ולסוכנים אחרים (במודלים מורכבים יותר).</p>

    <h3>קסם האמרג'נס (Emergence)</h3>
    <p>אחד הרעיונות המרתקים ביותר שמודלים אלו מדגימים הוא תופעת ה'אמרג'נס' (Emergence - הופעה/התהוות). זוהי התופעה שבה דפוסים מורכבים ומסודרים ברמת המערכת כולה אינם נובעים מתכנון מרכזי או חוקים מסובכים ברמת המערכת, אלא מתהווים באופן ספונטני כתוצאה מאינטראקציות פשוטות ומקומיות בין הסוכנים לבין סביבתם, ובין הסוכנים לבין עצמם. בהדמיית ההגירה, תנועה פשוטה של כל קבוצה המנסה למצוא את דרכה, תוך הימנעות ממכשולים ומשיכה למשאבים, יכולה להוביל להיווצרות רשת של נתיבי הגירה ברורים ודפוסי התיישבות שמכסים את המפה באופן שמזכיר דפוסים אמיתיים שאנו מוצאים בחקר ההיסטוריה האנושית.</p>

    <h3>איך זה קשור למחקר האמיתי?</h3>
    <p>מודלים פשטניים כמו זה מספקים לחוקרים "מעבדת ניסוי" דיגיטלית. הם מאפשרים לבדוק השערות לגבי האופן שבו גורמים בסיסיים - כמו זמינות משאבים, מכשולים גאוגרפיים, ואף סוגים שונים של התנהגות קבוצתית - יכלו לעצב את מסלולי ההגירה שאנו מזהים באמצעות ממצאים ארכיאולוגיים (כלי עבודה, שרידי מבנים) וניתוחים גנטיים של אוכלוסיות בנות זמננו ושל דנ"א עתיק.</p>

    <h3>חשוב לזכור: זהו רק מודל!</h3>
    <p>אין לשכוח שהדמיה זו היא ייצוג פשטני ביותר של מציאות היסטורית סופר-מורכבת. מודלים מתקדמים יותר המשמשים במחקר האמיתי כוללים מגוון רחב של גורמים נוספים: התפתחות טכנולוגית (יכולת לבנות סירות, לשפר כלי ציד), מבנים חברתיים, אינטראקציה ואף סכסוכים בין קבוצות, שינויים סביבתיים דינמיים (תקופות קרח, שיטפונות) ועוד. אך גם מודל בסיסי זה מסייע להמחיש את הרעיון המרכזי: לעיתים, דפוסים גלובליים מורכבים נובעים מיישום עקבי של חוקים מקומיים פשוטים.</p>
</div>

<style>
    :root {
        --grid-background: #e0ffe0; /* Light green for flat land */
        --mountain-color: #a0a0a0; /* Grey for mountains */
        --resource-color: #ffffa0; /* Yellow for resources */
        --agent-color: #ff6666; /* Red for agents */
        --cell-border: #d0d0d0; /* Subtle border */
        --controls-background: #f0f0f0;
        --button-bg: #4CAF50; /* Green button */
        --button-hover-bg: #45a049;
        --button-text: white;
        --disabled-button-bg: #cccccc;
        --disabled-button-text: #666666;
        --border-radius: 5px;
        --padding: 10px;
        --agent-size: 16px; /* Size of the agent circle */
        --cell-size: 20px; /* Size of the grid cell */
    }

    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 30px;
        direction: ltr; /* Grid is LTR */
        position: relative; /* Needed for absolute positioning of agents */
        padding: var(--padding);
        background-color: #ffffff; /* White background for the container */
        border-radius: var(--border-radius);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .grid {
        display: grid;
        border: 1px solid var(--cell-border);
        margin-bottom: var(--padding);
        background-color: var(--grid-background);
        position: relative; /* Ensure cells are positioned correctly */
        overflow: hidden; /* Hide agents moving outside grid bounds (shouldn't happen) */
    }

    .cell {
        width: var(--cell-size);
        height: var(--cell-size);
        box-sizing: border-box;
        border: 1px dotted rgba(0, 0, 0, 0.05); /* Very subtle cell borders */
        position: relative; /* Needed for agent z-index */
    }

    .flat { background-color: var(--grid-background); }
    .mountain {
        background-color: var(--mountain-color);
        background-image: linear-gradient(45deg, rgba(255,255,255,.1) 25%, transparent 25%, transparent 50%, rgba(255,255,255,.1) 50%, rgba(255,255,255,.1) 75%, transparent 75%, transparent);
        background-size: 10px 10px;
    }
    .resource {
        background-color: var(--resource-color);
        /* Add a subtle shimmer or glow effect later if needed */
        border: none; /* Remove dashed border */
    }

    .agent {
        width: var(--agent-size);
        height: var(--agent-size);
        background-color: var(--agent-color);
        border-radius: 50%;
        position: absolute; /* Position relative to simulation-container */
        transform: translate(-50%, -50%); /* Center point of the agent */
        transition: top 0.2s linear, left 0.2s linear; /* Smooth movement */
        box-shadow: 0 1px 3px rgba(0,0,0,0.3);
        z-index: 10; /* Ensure agents are above grid cells */
    }

    .controls-panel {
        background-color: var(--controls-background);
        padding: var(--padding);
        border-radius: var(--border-radius);
        width: 100%; /* Take full width of container */
        max-width: 650px; /* Match grid width or slightly larger */
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        align-items: center;
        direction: rtl; /* Hebrew layout */
        text-align: right;
    }

    .controls {
        display: flex;
        gap: var(--padding);
        margin-bottom: var(--padding);
        flex-wrap: wrap;
        justify-content: center;
        width: 100%;
    }

    .controls button {
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
        border: none;
        border-radius: var(--border-radius);
        background-color: var(--button-bg);
        color: var(--button-text);
        transition: background-color 0.3s ease;
        flex-grow: 1; /* Allow buttons to grow */
        min-width: 100px; /* Minimum width for buttons */
    }

    .controls button:hover:not(:disabled) {
        background-color: var(--button-hover-bg);
    }

     .controls button:disabled {
        background-color: var(--disabled-button-bg);
        color: var(--disabled-button-text);
        cursor: not-allowed;
    }

    .parameters {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: var(--padding);
        margin-bottom: var(--padding);
        width: 100%;
    }

    .param-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .param-group label {
        font-size: 0.9rem;
        margin-bottom: 5px;
        color: #555;
    }

    .param-group input[type="range"] {
        width: 100%;
        -webkit-appearance: none; /* Override default browser styles */
        appearance: none;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .param-group input[type="range"]:hover {
        opacity: 1;
    }

    .param-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: var(--button-bg);
        cursor: pointer;
        border-radius: 50%;
    }

    .param-group input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: var(--button-bg);
        cursor: pointer;
        border-radius: 50%;
    }

    .param-group span {
        font-size: 0.9rem;
        color: #333;
        margin-top: 3px;
    }

    .stats {
         margin-bottom: var(--padding);
         font-size: 1rem;
         color: #333;
         width: 100%;
         text-align: center;
    }

    .legend {
        border-top: 1px solid #ccc;
        padding-top: var(--padding);
        margin-top: var(--padding);
        display: flex;
        flex-wrap: wrap;
        gap: var(--padding);
        font-size: 0.9rem;
        align-items: center;
        justify-content: center; /* Center legend items */
        width: 100%;
    }

    .legend-item {
        display: flex;
        align-items: center;
    }

    .legend-item .cell {
         width: 15px;
         height: 15px;
         margin-left: 8px; /* Space between symbol and text */
         position: static; /* Don't use absolute positioning */
         top: auto; left: auto;
         border-radius: 3px; /* Slightly rounded corners */
         border: none; /* No border in legend */
         flex-shrink: 0; /* Prevent shrinking */
    }
     .legend-item .flat { background-color: var(--grid-background); }
     .legend-item .mountain { background-color: var(--mountain-color); background-image: none;} /* Simplify mountain in legend */
     .legend-item .resource { background-color: var(--resource-color); }


    .legend-item .agent {
         width: 15px;
         height: 15px;
         margin-left: 8px;
         position: static;
         top: auto; left: auto;
         border-radius: 50%;
         background-color: var(--agent-color);
         box-shadow: none;
         flex-shrink: 0; /* Prevent shrinking */
    }


    .toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1rem;
        cursor: pointer;
        border: 1px solid #ccc;
        background-color: #f0f0f0;
        border-radius: var(--border-radius);
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .toggle-explanation:hover {
         background-color: #e0e0e0;
         border-color: #bbb;
    }

    .explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #eee;
        background-color: #f9f9f9;
        direction: rtl; /* Hebrew text */
        text-align: right;
        border-radius: var(--border-radius);
        line-height: 1.6;
        color: #333;
        transition: all 0.5s ease-in-out; /* Smooth transition for display toggle */
        /* Initial state handled by JS style="display: none;" */
    }

    .explanation h2, .explanation h3 {
        color: #1a1a1a;
        margin-bottom: 10px;
    }
     .explanation h2 { margin-top: 0; }

    .explanation p {
        margin-bottom: 15px;
    }

    .explanation ul {
        list-style: disc inside;
        padding-right: 20px;
        margin-bottom: 15px;
    }
     .explanation li {
         margin-bottom: 8px;
         color: #555;
     }

     .explanation strong {
         color: #1a1a1a;
     }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const simulationContainer = document.querySelector('.simulation-container');
        const gridElement = document.getElementById('simulationGrid');
        const startButton = document.getElementById('startButton');
        const stopButton = document.getElementById('stopButton');
        const resetButton = document.getElementById('resetButton');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationContent = document.getElementById('explanationContent');
        const numAgentsInput = document.getElementById('numAgents');
        const numAgentsValueSpan = document.getElementById('numAgentsValue');
        const resourceAttractionInput = document.getElementById('resourceAttraction');
        const resourceAttractionValueSpan = document.getElementById('resourceAttractionValue');
        const obstacleCostInput = document.getElementById('obstacleCost');
        const obstacleCostValueSpan = document.getElementById('obstacleCostValue');
        const simulationSpeedInput = document.getElementById('simulationSpeed');
        const simulationSpeedValueSpan = document.getElementById('simulationSpeedValue');
        const simulationStepCountSpan = document.getElementById('simulationStepCount');


        const GRID_WIDTH = 30;
        const GRID_HEIGHT = 20;
        const CELL_SIZE = 20; // Matches CSS --cell-size
        const AGENT_SIZE = 16; // Matches CSS --agent-size

        // Define cell types and their properties relevant to movement
        const CELL_TYPE = {
            FLAT: 'flat',
            MOUNTAIN: 'mountain',
            RESOURCE: 'resource'
        };

        let grid = [];
        let agents = [];
        let simulationInterval = null;
        let simulationStep = 0;

        // Read parameters from controls
        const getNumAgents = () => parseInt(numAgentsInput.value, 10);
        const getResourceAttraction = () => parseFloat(resourceAttractionInput.value);
        const getObstacleCost = () => parseFloat(obstacleCostInput.value);
        const getSimulationSpeed = () => parseInt(simulationSpeedInput.value, 10);


        function createGrid() {
            gridElement.style.gridTemplateColumns = `repeat(${GRID_WIDTH}, ${CELL_SIZE}px)`;
            gridElement.style.gridTemplateRows = `repeat(${GRID_HEIGHT}, ${CELL_SIZE}px)`;

            // Clear previous grid and agents
            gridElement.innerHTML = '';
             // Remove agent elements that were appended to the container
            simulationContainer.querySelectorAll('.agent').forEach(agentEl => agentEl.remove());


            grid = [];
            for (let y = 0; y < GRID_HEIGHT; y++) {
                grid[y] = [];
                for (let x = 0; x < GRID_WIDTH; x++) {
                    const cellDiv = document.createElement('div');
                    cellDiv.classList.add('cell');
                    cellDiv.dataset.x = x;
                    cellDiv.dataset.y = y;

                    // Assign cell type - improved hardcoded map
                    let type = CELL_TYPE.FLAT;
                    const isBorder = x === 0 || x === GRID_WIDTH - 1 || y === 0 || y === GRID_HEIGHT - 1;
                    const isMountain1 = x > 5 && x < 10 && y > 5 && y < 15;
                    const isMountain2 = x > 22 && x < 25 && y > 8 && y < 18; // Another mountain range
                    const isResource1 = y === 10 && x > 10 && x < 20; // Resource patch
                    const isResource2 = y === 16 && x > 3 && x < 10; // Another resource patch
                     const isResource3 = y === 5 && x > 25 && x < 28; // Another resource patch

                    if (isBorder) type = CELL_TYPE.MOUNTAIN; // Map borders are mountains/impassable
                    else if (isMountain1 || isMountain2) type = CELL_TYPE.MOUNTAIN;
                    else if (isResource1 || isResource2 || isResource3) type = CELL_TYPE.RESOURCE;


                    cellDiv.classList.add(type);
                    grid[y][x] = { type: type, element: cellDiv, agents: [] };
                    gridElement.appendChild(cellDiv);
                }
            }
        }

        function placeAgents(count) {
            agents = [];
            for (let i = 0; i < count; i++) {
                let x, y;
                // Find a random, non-mountain cell to start
                do {
                    x = Math.floor(Math.random() * GRID_WIDTH);
                    y = Math.floor(Math.random() * GRID_HEIGHT);
                } while (grid[y][x].type === CELL_TYPE.MOUNTAIN);

                const agentDiv = document.createElement('div');
                agentDiv.classList.add('agent');
                // Position agent element relative to simulation container
                agentDiv.style.left = `${x * CELL_SIZE + CELL_SIZE / 2}px`;
                agentDiv.style.top = `${y * CELL_SIZE + CELL_SIZE / 2}px`;

                const agent = { id: i, x: x, y: y, element: agentDiv };
                agents.push(agent);
                simulationContainer.appendChild(agentDiv); // Append agent to the container
                grid[y][x].agents.push(agent); // Add agent object to cell data for collision/crowding check
            }
        }

        function updateAgentPosition(agent, newX, newY) {
             // Remove agent from current cell's agent list
            const currentCellAgents = grid[agent.y][agent.x].agents;
            const agentIndex = currentCellAgents.indexOf(agent);
            if (agentIndex > -1) {
                currentCellAgents.splice(agentIndex, 1);
            }

            // Update agent's logical position
            agent.x = newX;
            agent.y = newY;

             // Add agent to new cell's agent list
            grid[agent.y][agent.x].agents.push(agent);

            // Update agent's DOM position with CSS transition
            agent.element.style.left = `${newX * CELL_SIZE + CELL_SIZE / 2}px`;
            agent.element.style.top = `${newY * CELL_SIZE + CELL_SIZE / 2}px`;
        }


        function moveAgents() {
            // Shuffle agents array to avoid artifacts from processing order
            const shuffledAgents = agents.sort(() => Math.random() - 0.5);

            const resourceAttraction = getResourceAttraction();
            const obstacleCost = getObstacleCost();


            shuffledAgents.forEach(agent => {
                const possibleMoves = [];
                // 8 directions including diagonals
                const directions = [
                    { dx: 0, dy: -1 }, { dx: 0, dy: 1 }, { dx: -1, dy: 0 }, { dx: 1, dy: 0 },
                    { dx: -1, dy: -1 }, { dx: -1, dy: 1 }, { dx: 1, dy: -1 }, { dx: 1, dy: 1 }
                ];

                directions.forEach(({ dx, dy }) => {
                    const newX = agent.x + dx;
                    const newY = agent.y + dy;

                    // Check boundary conditions
                    if (newX >= 0 && newX < GRID_WIDTH && newY >= 0 && newY < GRID_HEIGHT) {
                        const targetCell = grid[newY][newX];
                        possibleMoves.push({ x: newX, y: newY, type: targetCell.type, agentsInCell: targetCell.agents.length });
                    }
                });

                if (possibleMoves.length > 0) {
                    let bestMove = null;
                    let highestScore = -Infinity;

                    possibleMoves.forEach(move => {
                         // Calculate score for this move
                         let score = Math.random(); // Basic randomness to break ties and add exploration factor

                         // Add bias for resources
                         if (move.type === CELL_TYPE.RESOURCE) {
                             score += resourceAttraction;
                         }

                         // Penalize moving into or through mountains
                         if (move.type === CELL_TYPE.MOUNTAIN) {
                            score -= obstacleCost; // Subtract a significant cost
                         }

                         // Small penalty for moving into an already crowded cell (optional, simple)
                         // A better model might involve splitting or resource competition, but this is basic.
                         // score -= move.agentsInCell * 0.1; // Example: small penalty per agent already there

                         if (score > highestScore) {
                             highestScore = score;
                             bestMove = move;
                         }
                    });

                    // If the best move's score is not drastically negative (e.g., trying to move into a high-cost mountain)
                    // or if it's better than staying put (score 0 for staying, assuming current cell score isn't negative)
                    // a simple rule: only move if the score is positive (prefers resources, avoids obstacles)
                    // Or simply move to the best available cell, even if it's not ideal, unless it's an impassable mountain (already filtered).
                    // Let's stick to moving to the highest scoring valid cell.
                    if (bestMove && (bestMove.x !== agent.x || bestMove.y !== agent.y)) { // Ensure it's an actual move
                         updateAgentPosition(agent, bestMove.x, bestMove.y);
                    }
                }
            });

            simulationStep++;
            simulationStepCountSpan.textContent = simulationStep;
        }

        function startSimulation() {
            if (simulationInterval === null) {
                const speed = getSimulationSpeed();
                simulationInterval = setInterval(simulationStep, speed);
                startButton.disabled = true;
                stopButton.disabled = false;
                // Disable parameter changes while running (or handle them dynamically, but reset is simpler)
                numAgentsInput.disabled = true;
                resourceAttractionInput.disabled = true;
                obstacleCostInput.disabled = true;
                simulationSpeedInput.disabled = true; // Speed can be changed dynamically, but simplified here
                 // Allow speed change dynamically
                 simulationSpeedInput.disabled = false;

            }
        }

        function stopSimulation() {
            clearInterval(simulationInterval);
            simulationInterval = null;
            startButton.disabled = false;
            stopButton.disabled = true;
            // Enable parameter changes when stopped
            numAgentsInput.disabled = false;
            resourceAttractionInput.disabled = false;
            obstacleCostInput.disabled = false;
            simulationSpeedInput.disabled = false;
        }

        function resetSimulation() {
            stopSimulation(); // Stop if running
            simulationStep = 0;
            simulationStepCountSpan.textContent = simulationStep;
            createGrid(); // Recreate grid (clears old agents)
            placeAgents(getNumAgents()); // Place agents based on current setting
            startButton.disabled = false;
            stopButton.disabled = true;
            // Ensure parameters are enabled after reset
             numAgentsInput.disabled = false;
             resourceAttractionInput.disabled = false;
             obstacleCostInput.disabled = false;
             simulationSpeedInput.disabled = false;
        }

        // Event Listeners
        startButton.addEventListener('click', startSimulation);
        stopButton.addEventListener('click', stopSimulation);
        resetButton.addEventListener('click', resetSimulation);

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'צוללים לעומק: גלו את ההסבר המלא';
        });

         // Parameter input change listeners
         numAgentsInput.addEventListener('input', () => {
             numAgentsValueSpan.textContent = numAgentsInput.value;
         });
          resourceAttractionInput.addEventListener('input', () => {
             resourceAttractionValueSpan.textContent = resourceAttractionInput.value;
         });
          obstacleCostInput.addEventListener('input', () => {
             obstacleCostValueSpan.textContent = obstacleCostInput.value;
         });
          simulationSpeedInput.addEventListener('input', () => {
             simulationSpeedValueSpan.textContent = `${simulationSpeedInput.value}ms`;
             // Update interval speed immediately if simulation is running
             if (simulationInterval !== null) {
                 clearInterval(simulationInterval);
                 simulationInterval = setInterval(simulationStep, getSimulationSpeed());
             }
         });


        // Initial setup
        createGrid(); // Create grid structure first to get gridElement dimensions
        // Set grid dimensions based on calculated cell size and count
        gridElement.style.width = `${GRID_WIDTH * CELL_SIZE}px`;
        gridElement.style.height = `${GRID_HEIGHT * CELL_SIZE}px`;
        simulationContainer.style.width = `${GRID_WIDTH * CELL_SIZE + 2 * var(--padding, 10)}px`; // Adjust container width

        placeAgents(getNumAgents()); // Place initial agents
         // Update value spans initially
        numAgentsValueSpan.textContent = numAgentsInput.value;
        resourceAttractionValueSpan.textContent = resourceAttractionInput.value;
        obstacleCostValueSpan.textContent = obstacleCostInput.value;
        simulationSpeedValueSpan.textContent = `${simulationSpeedInput.value}ms`;


    });
</script>
---