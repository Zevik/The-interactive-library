---
title: "מסע הרעיון: סימולטור התפשטות תרבותית"
english_slug: how-ideas-spread-cultural-diffusion-simulator
category: "מדעי החברה / סוציולוגיה ואנתרופולוגיה"
tags:
  - דיפוזיה תרבותית
  - התפשטות רעיונות
  - סימולציה
  - רשתות חברתיות
  - חדשנות
---
<h1>מסע הרעיון: סימולטור התפשטות תרבותית</h1>
<p>האם שאלתם את עצמכם פעם איך רעיונות, טרנדים וחידושים מצליחים לכבוש את העולם (או לפחות את הרשת החברתית שלכם) במהירות מסחררת? מדוע רעיון אחד הופך לשיחת היום, בעוד אחר נעלם כלא היה? הכירו את הכוחות הדינמיים שמניעים את ההתפשטות התרבותית.</p>

<div class="diffusion-simulator">
    <div class="simulator-grid-container">
        <p>לחצו על הצמתים שמהם יתחיל המסע (מאמצים ראשונים), ואז התחילו את הסימולציה:</p>
        <div class="simulator-grid" id="simulatorGrid">
            <!-- Nodes will be generated here by JS -->
        </div>
    </div>
    <div class="simulator-controls">
        <label for="probability">סיכוי מעבר רעיון (0-1):</label>
        <input type="number" id="probability" value="0.3" min="0" max="1" step="0.05">

        <label for="speed">קצב התפשטות (ms):</label>
        <input type="number" id="speed" value="200" min="50" max="1000" step="50">

        <button id="startButton">התחל מסע</button>
        <button id="pauseButton" disabled>השהה</button>
        <button id="resetButton">אפס</button>

        <div class="stats">
            <p>שלב התפשטות: <span id="timeStep">0</span></p>
            <p>אחוז מאמצי הרעיון: <span id="adoptedPercentage">0.00%</span></p>
        </div>
    </div>
</div>

<!-- Button to toggle explanation -->
<button id="toggleExplanationButton">הצג/הסתר את הסיפור המלא מאחורי ההתפשטות</button>

<!-- Explanation Section (hidden by default) -->
<div id="explanationSection" style="display: none;">
    <h2>הסיפור המלא מאחורי ההתפשטות</h2>
    <p>הסימולטור שלפניכם מדגים עיקרון בסיסי בחקר מערכות מורכבות וסוציולוגיה: דיפוזיה תרבותית והתפשטות חידושים. זהו תהליך אוניברסלי שמעצב חברות לאורך ההיסטוריה וגם ברגע זה ממש ברשתות הדיגיטליות.</p>
    <ul>
        <li><strong>מהי דיפוזיה תרבותית?</strong> דמיינו אבן שנזרקת למים, יוצרת אדוות שמתפשטות והלאה. דיפוזיה תרבותית היא התהליך שבו רעיונות, טכנולוגיות, מנהגים, ערכים, או כל חידוש אחר, נעים ממקור אחד לאנשים, קבוצות או תרבויות אחרות, לאורך זמן ובמרחב. זוהי הדרך בה טרנדים נולדים ומתפשטים, טכנולוגיות חדשות מאומצות, ואפילו מחלות מדבקות מתפשטות (מודלים רבים דומים).</li>
        <li><strong>דוגמאות מהחיים (ולא רק מהרשת):</strong> ההיסטוריה מלאה בדוגמאות: התפשטות הכתב, הדתות המרכזיות, טכנולוגיות חקלאיות עתיקות, או מסעות סחר שהפיצו רעיונות. בעידן המודרני, חשבו על התפשטות הסמארטפונים, אופנות לבוש, סגנונות מוזיקה, ממים אינטרנטיים, או אפילו רעיונות פוליטיים. כל אלה הם ביטויים של דיפוזיה.</li>
        <li><strong>הכוחות המניעים את ההתפשטות:</strong> לא כל רעיון מתפשט באותה צורה או באותו קצב. מה משפיע?
            <ul>
                <li><strong>קרבה (פיזית וחברתית):</strong> רעיונות נוטים לעבור קודם כל לשכנים הקרובים ביותר - בין אם גאוגרפית או מבחינת קשרים חברתיים חזקים.</li>
                <li><strong>מבנה הרשת החברתית:</strong> מי מחובר למי? קשרים חזקים מקלים על מעבר מידע עשיר ומורכב, בעוד קשרים חלשים (Weak Ties) יכולים לשמש כ"גשרים" המחברים בין קבוצות או אשכולות נפרדים ברשת, ומאפשרים לרעיון להגיע לקהלים חדשים לגמרי. צמתים "מרכזיים" עם קשרים רבים יכולים להאיץ דרמטית את ההתפשטות.</li>
                <li><strong>מאפייני הרעיון עצמו:</strong> האם הרעיון חדשני מדי או מוכר? קל להבנה או מורכב? האם הוא תואם לערכים ולמנהגים הקיימים בחברה? האם אפשר "לנסות" אותו בקלות לפני שמאמצים אותו לחלוטין? (כמו ניסוי חינם בתוכנה).</li>
                <li><strong>השפעה חברתית ואמון:</strong> לעיתים קרובות, אנשים מאמצים רעיון לא רק כי הוא טוב אלא כי אדם שהם סומכים עליו או מעריכים את דעתו כבר אימץ אותו. משפיענים (Influencers) ברשתות החברתיות הם דוגמה מודרנית להשפעה זו.</li>
                <li><strong>חסמים:</strong> לא הכל זורם בחופשיות. גבולות מדיניים, שפה שונה, הבדלים תרבותיים, עלות כלכלית, או אפילו חוסר רצון פסיכולוגי לשינוי – כל אלה יכולים להאט או לחסום לחלוטין את התפשטות הרעיון.</li>
            </ul>
        </li>
        <li><strong>מודלים וסימולציות:</strong> כדי להבין ולחזות תהליכי דיפוזיה, מפתחים מודלים מתמטיים וחישוביים. הסימולטור שלפניכם מבוסס על מודל פשוט של התפשטות ברשת (במקרה זה, רשת שהיא רשת גריד - כל צומת מחובר לשכניו הקרובים). מודלים אלו מאפשרים לחקור את ההשפעה של שינוי פרמטרים (כמו סיכוי המעבר), שינוי בנקודות ההתחלה (מי ה"מאמצים הראשונים"), או אפילו שינוי במבנה הרשת עצמה. הם מסייעים לנו לבנות אינטואיציה לגבי התנהגות מערכות מורכבות.</li>
        <li><strong>החשיבות של נקודות התחלה:</strong> האנשים או הצמתים שמאמצים ראשונים את הרעיון (לפעמים מכונים innovators או early adopters) הם קריטיים! מיקומם ברשת והמידה בהם הם מחוברים לאחרים יכולים לקבוע אם הרעיון "יתפוס" ויתפשט הלאה, או יישאר בגדר נישה שולית. נסו לבחור נקודות התחלה שונות בסימולטור וראו כיצד זה משפיע על התוצאה הסופית!</li>
    </ul>
     <p style="text-align: center; font-style: italic; margin-top: 25px; color: #555;">הסימולטור הוא כלי פשוט להדמיה, המאפשר לראות את התהליך בפעולה ולפתח הבנה אינטואיטיבית לגבי הכוחות שמעצבים את התפשטות הרעיונות בעולמנו.</p>
</div>

<style>
    /* General Body and Typography */
    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #f4f7f6;
    }

    h1, h2 {
        color: #004085;
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }

    p {
        text-align: center;
        margin-bottom: 20px;
        font-size: 1.1rem;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Simulator Container */
    .diffusion-simulator {
        font-family: 'Arial', sans-serif;
        display: flex;
        flex-direction: column;
        gap: 20px;
        margin: 20px auto;
        max-width: 650px;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Grid Area */
     .simulator-grid-container {
         margin-bottom: 15px;
         text-align: center;
         font-size: 1.1rem;
         color: #555;
         margin-bottom: 10px;
     }

    .simulator-grid {
        display: grid;
        gap: 2px;
        border: 1px solid #ddd;
        padding: 4px;
        max-width: 600px;
        margin: 0 auto;
        background-color: #f8f8f8;
        border-radius: 5px;
    }

    /* Node Styles */
    .node {
        width: 18px;
        height: 18px;
        background-color: #e0e0e0; /* Initial state */
        cursor: pointer;
        border: none;
        box-sizing: border-box;
        transition: background-color 0.4s ease; /* Smooth transition */
        border-radius: 3px;
        box-shadow: inset 0 0 2px rgba(0,0,0,0.1);
    }

    /* Node hover effect before simulation */
    .node:hover:not(.adopted):not(.selected-start) {
        background-color: #c9c9c9;
    }

    /* Style for selected start nodes BEFORE simulation starts */
    .node.selected-start {
         background-color: #ffc107; /* Yellow/Orange */
         box-shadow: 0 0 5px rgba(255,193,7,0.6); /* Glow effect */
    }
    .node.selected-start:hover {
         background-color: #ffa000;
    }


    /* Adopted state */
    .node.adopted {
        background-color: #28a745; /* Green */
        box-shadow: inset 0 0 2px rgba(0,0,0,0.2);
        animation: pulse-once 0.6s ease-out forwards; /* Apply animation */
    }

    /* Pulse animation for newly adopted nodes */
    @keyframes pulse-once {
        0% { transform: scale(0.8); opacity: 0.8; background-color: #ffc107; }
        50% { transform: scale(1.1); opacity: 1; background-color: #28a745; }
        100% { transform: scale(1); opacity: 1; background-color: #28a745; }
    }

    /* Controls Area */
    .simulator-controls {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        align-items: center;
        justify-content: center;
        background-color: #e9ecef;
        padding: 20px;
        border-radius: 8px;
        max-width: 600px;
        margin: 0 auto;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
    }

    .simulator-controls label {
        font-weight: bold;
        color: #555;
        min-width: 120px;
        text-align: left;
    }

    .simulator-controls input[type="number"] {
        padding: 10px;
        border: 1px solid #ced4da;
        border-radius: 5px;
        font-size: 1rem;
        flex-grow: 1;
        max-width: 150px;
    }

    .simulator-controls button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        cursor: pointer;
        background-color: #007bff;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        min-width: 100px;
    }

    .simulator-controls button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-1px);
    }

     .simulator-controls button:active:not(:disabled) {
         transform: translateY(0);
    }

    .simulator-controls button:disabled {
        background-color: #cccccc;
        color: #666;
        cursor: not-allowed;
    }

    /* Stats Area */
    .stats {
        margin-top: 15px;
        font-size: 1.1rem;
        text-align: center;
        width: 100%;
        color: #333;
    }

    .stats p {
        margin: 5px 0;
         display: inline-block;
         margin: 0 15px;
         text-align: center; /* Ensure paragraph inside stats is centered */
    }

    .stats span {
        font-weight: bold;
        color: #004085;
    }

    /* Explanation Toggle Button */
    #toggleExplanationButton {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        font-size: 1.1rem;
        cursor: pointer;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 5px;
        transition: background-color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    #toggleExplanationButton:hover {
         background-color: #e2e6ea;
         border-color: #d6dbdf;
         box-shadow: 0 3px 6px rgba(0,0,0,0.1);
    }

    /* Explanation Section */
    #explanationSection {
        border-top: 1px solid #e0e0e0;
        margin-top: 30px;
        padding-top: 25px;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        text-align: justify; /* Justify text */
        direction: rtl; /* Ensure RTL for list markers */
    }

    #explanationSection h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #004085;
    }

    #explanationSection ul {
        list-style-type: disc;
        margin-right: 25px;
        padding-right: 0;
        margin-bottom: 20px;
    }

     #explanationSection ul ul {
         list-style-type: circle;
         margin-right: 20px;
         padding-right: 0;
         margin-top: 10px;
     }

    #explanationSection li {
        margin-bottom: 12px;
        line-height: 1.7;
        color: #444;
    }

    #explanationSection li strong {
        color: #004085;
    }

    /* Responsive adjustments */
    @media (max-width: 680px) {
         .simulator-grid-container p {
             font-size: 1rem; /* Slightly smaller text on small screens */
             padding: 0 10px;
         }
         .simulator-grid {
             max-width: 100%; /* Allow grid to take full width minus padding */
         }
         .node {
             width: 15px; /* Smaller nodes on very small screens */
             height: 15px;
         }
         .simulator-controls {
             flex-direction: column;
             align-items: stretch;
         }
          .simulator-controls label {
              text-align: center;
              min-width: auto;
          }
          .simulator-controls input[type="number"] {
              max-width: none;
          }
          .simulator-controls button {
              width: 100%; /* Full width buttons */
              min-width: auto;
          }
           .stats p {
               display: block; /* Stack stats vertically */
               margin: 5px 0;
           }
           #explanationSection {
               padding: 15px; /* Less padding on small screens */
           }
            #explanationSection ul {
                 margin-right: 15px; /* Adjust list indent */
            }
            #explanationSection ul ul {
                 margin-right: 10px;
            }
    }


</style>

<script>
    const gridWidth = 30; // Number of columns
    const gridHeight = 20; // Number of rows
    // gridState can be 'initial', 'selected', or 'adopted'
    let gridState = [];
    let gridElements = []; // 2D array to store node div elements
    let simulationInterval = null;
    let timeStep = 0;
    let totalNodes = gridWidth * gridHeight;
    let adoptedCount = 0; // Count of nodes in 'adopted' state

    // DOM Elements
    const simulatorGridEl = document.getElementById('simulatorGrid');
    const probabilityInput = document.getElementById('probability');
    const speedInput = document.getElementById('speed');
    const startButton = document.getElementById('startButton');
    const pauseButton = document.getElementById('pauseButton');
    const resetButton = document.getElementById('resetButton');
    const timeStepSpan = document.getElementById('timeStep');
    const adoptedPercentageSpan = document.getElementById('adoptedPercentage');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');
    const explanationSection = document.getElementById('explanationSection');

    // Set CSS grid columns based on gridWidth
    simulatorGridEl.style.gridTemplateColumns = `repeat(${gridWidth}, 1fr)`;

    // Function to initialize or reset the grid
    function initializeGrid() {
        gridState = [];
        gridElements = [];
        adoptedCount = 0;
        timeStep = 0;
        simulatorGridEl.innerHTML = ''; // Clear previous grid

        for (let i = 0; i < gridHeight; i++) {
            gridState[i] = [];
            gridElements[i] = [];
            for (let j = 0; j < gridWidth; j++) {
                gridState[i][j] = 'initial'; // Initial state
                const nodeEl = document.createElement('div');
                nodeEl.classList.add('node');
                nodeEl.dataset.row = i;
                nodeEl.dataset.col = j;
                nodeEl.addEventListener('click', handleNodeClick); // Add click listener on initial creation
                gridElements[i][j] = nodeEl;
                simulatorGridEl.appendChild(nodeEl);
            }
        }
        updateStats();
         // Ensure buttons are in correct state initially
        startButton.disabled = false;
        pauseButton.disabled = true;
    }

    // Handle clicks on nodes to select start points (only before simulation starts)
    function handleNodeClick(event) {
        // Only allow clicking before simulation starts
        if (simulationInterval === null) {
            const row = parseInt(event.target.dataset.row);
            const col = parseInt(event.target.dataset.col);
            const nodeEl = gridElements[row][col];

            if (gridState[row][col] === 'initial') {
                // Select as potential start node
                gridState[row][col] = 'selected'; // Use a new state 'selected'
                nodeEl.classList.add('selected-start');
            } else if (gridState[row][col] === 'selected') {
                // Deselect
                gridState[row][col] = 'initial';
                nodeEl.classList.remove('selected-start');
            }
             // No stats update needed for selection, only when starting the simulation.
        }
    }

    // Get neighboring nodes for a given node (basic 4-directional grid neighbors)
    function getNeighbors(row, col) {
        const neighbors = [];
        // Up, Down, Left, Right
        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

        for (const [dr, dc] of directions) {
            const newRow = row + dr;
            const newCol = col + dc;

            // Check bounds
            if (newRow >= 0 && newRow < gridHeight && newCol >= 0 && newCol < gridWidth) {
                neighbors.push({ row: newRow, col: newCol });
            }
        }
        return neighbors;
    }

    // Perform one step of the simulation
    function simulateStep() {
        timeStep++;
        const newlyAdopted = []; // Nodes that become adopted in this step

        // Find all currently adopted nodes
        const currentlyAdopted = [];
        for (let i = 0; i < gridHeight; i++) {
            for (let j = 0; j < gridWidth; j++) {
                // Check for 'adopted' state
                if (gridState[i][j] === 'adopted') {
                    currentlyAdopted.push({ row: i, col: j });
                }
            }
        }

        // Iterate through currently adopted nodes and potentially influence neighbors
        for (const { row, col } of currentlyAdopted) {
            const neighbors = getNeighbors(row, col);
            for (const neighbor of neighbors) {
                const { row: nRow, col: nCol } = neighbor;
                // Check if the neighbor is 'initial' and not already marked to be adopted in this step
                // Nodes in 'selected' state (if any remain) will also be eligible
                if ((gridState[nRow][nCol] === 'initial' || gridState[nRow][nCol] === 'selected')
                     && !newlyAdopted.some(n => n.row === nRow && n.col === nCol)) {
                     const probability = parseFloat(probabilityInput.value);
                    if (Math.random() < probability) {
                        newlyAdopted.push({ row: nRow, col: nCol });
                    }
                }
            }
        }

        // Update the state of newly adopted nodes and add 'adopted' class (triggers CSS animation)
        for (const { row, col } of newlyAdopted) {
            gridState[row][col] = 'adopted';
             // Remove selected-start class just in case (shouldn't happen if startSimulation worked)
            gridElements[row][col].classList.remove('selected-start');
            gridElements[row][col].classList.add('adopted'); // Add adopted class - CSS handles visuals/animation
            adoptedCount++;
        }

        updateStats();

        // Stop simulation if no new nodes were adopted or all nodes are adopted
        if (newlyAdopted.length === 0 || adoptedCount === totalNodes) {
            pauseSimulation(); // This will update button states
        }
    }

    // Start the simulation
    function startSimulation() {
        // Find selected start nodes (nodes with 'selected' state)
        const selectedStartNodes = [];
        for (let i = 0; i < gridHeight; i++) {
            for (let j = 0; j < gridWidth; j++) {
                if (gridState[i][j] === 'selected') { // Check for 'selected' state
                    selectedStartNodes.push({ row: i, col: j });
                }
            }
        }

        if (selectedStartNodes.length === 0) {
            alert("אנא בחר נקודת התחלה אחת לפחות על ידי לחיצה על צומת.");
            return;
        }

        // Convert 'selected' nodes to 'adopted' state for the simulation start
         adoptedCount = 0; // Reset adopted count before starting with selected nodes
        for (const { row, col } of selectedStartNodes) {
            gridState[row][col] = 'adopted'; // Change state to adopted
            const nodeEl = gridElements[row][col];
            nodeEl.classList.remove('selected-start'); // Remove selection class visual
            nodeEl.classList.add('adopted'); // Add adopted class (triggers initial animation)
            adoptedCount++; // Count as adopted for stats
        }


        if (simulationInterval === null) { // Prevent starting if already running
            const speed = parseInt(speedInput.value);
            simulationInterval = setInterval(simulateStep, speed);
            startButton.disabled = true;
            pauseButton.disabled = false;

             // Remove click listeners from ALL nodes once simulation starts
             // Cloning is a robust way to remove all attached listeners easily.
            for (let i = 0; i < gridHeight; i++) {
                 for (let j = 0; j < gridWidth; j++) {
                     const oldNode = gridElements[i][j];
                     const newNode = oldNode.cloneNode(true); // Clone without listeners
                     oldNode.parentNode.replaceChild(newNode, oldNode);
                     gridElements[i][j] = newNode; // Update the reference to the new node element
                 }
            }
        }
         updateStats(); // Initial stats update after selected nodes become adopted
    }

    // Pause the simulation
    function pauseSimulation() {
        clearInterval(simulationInterval);
        simulationInterval = null;
        startButton.disabled = false;
        pauseButton.disabled = true;
         // Node clicks are not re-enabled on pause. User must Reset to select new start points.
    }

    // Reset the simulation to initial state
    function resetSimulation() {
        pauseSimulation(); // Stop any running simulation
        initializeGrid(); // Reset state and visuals, which also re-adds click listeners via node creation
    }

    // Update the statistics displayed
    function updateStats() {
        timeStepSpan.textContent = timeStep;
        const percentage = totalNodes > 0 ? (adoptedCount / totalNodes) * 100 : 0;
        adoptedPercentageSpan.textContent = percentage.toFixed(2) + '%';
    }

    // Toggle the visibility of the explanation section
    function toggleExplanation() {
        if (explanationSection.style.display === 'none') {
            explanationSection.style.display = 'block';
            // Optional: Scroll to explanation or button
             // toggleExplanationButton.scrollIntoView({ behavior: 'smooth' });
        } else {
            explanationSection.style.display = 'none';
        }
    }

    // Event Listeners for controls
    startButton.addEventListener('click', startSimulation);
    pauseButton.addEventListener('click', pauseSimulation);
    resetButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Initial setup when the page loads
    initializeGrid();

</script>
```