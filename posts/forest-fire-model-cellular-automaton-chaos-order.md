---
title: "מודל אש יער: כשהכאוס והסדר נפגשים באוטומט תאי"
english_slug: forest-fire-model-cellular-automaton-chaos-order
category: "מדעים מדויקים / פיזיקה"
tags:
  - אוטומט תאי
  - מודל אש יער
  - מערכות מורכבות
  - פיזיקה סטטיסטית
  - סימולציה
---
# מודל אש יער: כשהכאוס והסדר נפגשים באוטומט תאי

תארו לעצמכם יער אינסופי... שריפה מתחילה לפתע, מתפשטת בעוצמה בלתי צפויה, ואז דועכת כשהיא נתקלת באזורים ריקים. איך יכול אירוע כל כך כאוטי ומורכב לנבוע מכללים בסיסיים ופשוטים? האם אפשר ללכוד את הדינמיקה הפראית הזו במודל חישובי קטנטן? הצטרפו אלינו למסע אל עולם האוטומטים התאיים, שבו פשטות מקומית יוצרת מורכבות גלובלית עוצרת נשימה.

<div class="simulation-container">
    <canvas id="forestCanvas"></canvas>
    <div class="controls">
        <div class="control-group">
            <label for="density">צפיפות עצים התחלתית (%):</label>
            <input type="range" id="density" min="10" max="90" value="50">
            <span id="densityValue">50%</span>
        </div>
        <div class="control-group">
            <label for="growthProb">סיכוי צמיחה (עץ חדש, %):</label>
            <input type="range" id="growthProb" min="0" max="10" value="1" step="0.1">
            <span id="growthProbValue">0.1%</span>
        </div>
        <div class="control-group">
            <label for="lightningProb">סיכוי ברק (מצית אש, %):</label>
            <input type="range" id="lightningProb" min="0" max="1" value="0.001" step="0.001">
            <span id="lightningProbValue">0.001%</span>
        </div>
        <div class="control-group">
            <label for="fireSpreadProb">סיכוי הדבקה (משכן בוער, %):</label>
             <input type="range" id="fireSpreadProb" min="0" max="100" value="100">
            <span id="fireSpreadProbValue">100%</span>
        </div>
        <button id="startButton">התחל 🔥</button>
        <button id="stopButton">עצור ⏸️</button>
        <button id="resetButton">אפס 🌳</button>
    </div>
</div>

<style>
    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px; /* Increased gap */
        padding: 30px; /* Increased padding */
        border: 1px solid #e0e0e0; /* Lighter border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* White background */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        margin-bottom: 30px; /* More space below */
        font-family: 'Arial', sans-serif; /* Standard clean font */
    }

    #forestCanvas {
        border: 1px solid #a0a0a0; /* Subtle canvas border */
        background-color: #f0f0e0; /* Warm beige for empty */
        display: block;
        margin: 0 auto;
        box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.05); /* Inner shadow for depth */
    }

    .controls {
        display: flex;
        flex-wrap: wrap;
        gap: 20px; /* Increased gap in controls */
        justify-content: center;
        width: 100%;
        max-width: 900px; /* Wider control area */
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 200px; /* Adjusted width */
    }

    .control-group label {
        margin-bottom: 8px; /* More space below label */
        font-weight: bold;
        font-size: 0.95em; /* Slightly larger font */
        color: #333; /* Darker text */
    }

    .control-group input[type="range"] {
        width: 100%;
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 8px; /* Thicker slider */
        background: #ddd; /* Slider background */
        outline: none;
        opacity: 0.7;
        transition: opacity 0.2s ease;
        border-radius: 4px;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px; /* Larger thumb */
        height: 18px;
        background: #007bff; /* Thumb color */
        cursor: pointer;
        border-radius: 50%; /* Round thumb */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }


    .control-group span {
        font-size: 0.9em; /* Slightly larger span */
        color: #555;
        margin-top: 4px; /* Space above value */
    }

    button {
        padding: 12px 24px; /* Increased padding */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Added transform for press effect */
        min-width: 120px; /* Ensure consistent button width */
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Button shadow */
    }

    button:hover {
        background-color: #0056b3;
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    }

     button:active {
        background-color: #003f7f;
        transform: scale(0.98); /* Scale down on click */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    #stopButton {
         background-color: #dc3545; /* Red for stop */
    }
    #stopButton:hover {
        background-color: #c82333;
    }
     #stopButton:active {
        background-color: #bd2130;
    }

    #resetButton {
         background-color: #ffc107; /* Yellow/Orange for reset */
         color: #333; /* Dark text for contrast */
    }
     #resetButton:hover {
        background-color: #e0a800;
    }
     #resetButton:active {
        background-color: #d39e00;
    }


    .explanation-button-container {
        text-align: center;
        margin-top: 30px; /* More space above button */
    }

    #explanationContent {
        margin-top: 30px; /* More space above content */
        padding: 30px; /* Increased padding */
        border: 1px solid #e0e0e0; /* Lighter border */
        border-radius: 12px; /* More rounded corners */
        background-color: #fff; /* White background */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        display: none; /* Initially hidden */
        line-height: 1.7; /* Improved readability */
        color: #333; /* Darker text */
    }

    #explanationContent h2 {
        color: #0056b3; /* Blue heading */
        margin-top: 0;
        margin-bottom: 20px; /* More space below heading */
        border-bottom: 2px solid #007bff; /* Underline heading */
        padding-bottom: 10px;
    }

    #explanationContent p {
        margin-bottom: 20px; /* More space between paragraphs */
    }

    #explanationContent ul, #explanationContent ol {
        margin-bottom: 20px;
        padding-right: 25px; /* Adjust for RTL */
        list-style-position: outside; /* Bullets/numbers outside text block */
    }

    #explanationContent li {
        margin-bottom: 10px; /* More space between list items */
    }

    #explanationContent strong {
        color: #0056b3; /* Highlight strong text */
    }

    /* Specific colors for states in explanation */
    .state-empty { color: #a0a0a0; font-weight: bold; }
    .state-tree { color: #1a7f32; font-weight: bold; } /* Darker green */
    .state-burning { color: #d9534f; font-weight: bold; } /* Firebrick red */


</style>

<div class="explanation-button-container">
    <button id="toggleExplanationButton">גלו את הסוד: מה מניע את המודל? 📖</button>
</div>

<div id="explanationContent">
    <h2>הסבר מעמיק: מסע אל ליבת אוטומט היער הבוער</h2>

    <p>הסימולציה ששיחקתם איתה היא דוגמה מהפנטת למושג שנקרא <strong>אוטומט תאי</strong>. דמיינו לוח משחק ענק, מחולק לריבועים קטנים – תאים. כל תא כזה יכול להיות במצב מוגדר מראש (כמו ריק, עץ, או בוער במודל שלנו). המערכת כולה "מתפתחת" בצעדי זמן קבועים, ומה שיקרה בכל תא בצעד הבא תלוי אך ורק במצבו הנוכחי ובמצב השכנים הקרובים שלו.</p>

    <p><strong>מודל אש היער</strong> הוא קלאסיקה שמדגימה איך חוקים מקומיים פשוטים יכולים ליצור התנהגות מורכבת וגלובלית באופן מפתיע. במודל שלנו, כל "פיקסל" על המסך הוא תא, והוא יכול להיות באחד משלושה מצבים:</p>
    <ul>
        <li><strong class="state-empty">ריק (Empty):</strong> פיסת אדמה פנויה, פוטנציאל לצמיחה.</li>
        <li><strong class="state-tree">עץ (Tree):</strong> עץ ירוק ותמים, מוכן לצמוח או להישרף.</li>
        <li><strong class="state-burning">בוער (Burning):</strong> עץ שאוחז באש, מקור להדבקה.</li>
    </ul>

    <p>בכל צעד זמן (כפי שראיתם קופץ על המסך), כל תא בוחן את עצמו ואת סביבתו (במודל זה, בדרך כלל 8 שכנים מסביב, כולל אלכסונים) ומחליט מה יהיה מצבו הבא, לפי החוקים הבאים:</p>
    <ol>
        <li><strong>עץ בוער:</strong> סיים את דרכו. בצעד הבא יהפוך אוטומטית לתא <strong class="state-empty">ריק</strong> (האש כילתה אותו).</li>
        <li><strong>עץ חי:</strong> עתידו פתוח, תלוי בסביבה ובמזל:
            <ul>
                <li>אם יש לפחות שכן אחד ש<strong class="state-burning">בוער</strong>, הוא עלול "להידבק" ולהידלק בעצמו. הסיכוי לכך נקבע על ידי הפרמטר "<strong>סיכוי הדבקה</strong>" (שימו לב, במודלים בסיסיים רבים הסיכוי הזה הוא 100%, כלומר הדבקה ודאית).</li>
                <li>אם אין לו שכנים ש<strong class="state-burning">בוערים</strong>, הוא עדיין יכול להידלק באופן עצמוני בהסתברות קטנטנה, שמייצגת אירוע נדיר כמו <strong class="state-burning">ברק</strong>. הסיכוי הזה נקבע על ידי הפרמטר "<strong>סיכוי ברק</strong>".</li>
                <li>אם אף אחד מהתרחישים הנ"ל לא קורה, העץ נשאר <strong class="state-tree">עץ</strong> חי ובריא.</li>
            </ul>
        </li>
        <li><strong>תא ריק:</strong> האדמה פנויה להתחדשות. בהסתברות נמוכה, הוא יכול להפוך ל<strong class="state-tree">עץ</strong> חדש. הסיכוי לכך נקבע על ידי הפרמטר "<strong>סיכוי צמיחה</strong>". אחרת, הוא נשאר <strong class="state-empty">ריק</strong>.</li>
    </ol>

    <p>הקסם מתרחש כשמריצים את החוקים הפשוטים האלה שוב ושוב, על אלפי תאים במקביל. פתאום רואים גלים של אש מתפשטים, "איים" ירוקים נותרים בלתי פגועים, ואזורים שרופים מתחילים להתאושש לאט לאט. זוהי דוגמה מרהיבה ל<strong>התנהגות אמורגנטית</strong> - תכונות ודפוסים ברמת המערכת כולה שאינם ניתנים לחיזוי ישיר רק מתוך התבוננות בחוקים של תא בודד.</p>

    <p>נסו לשנות את הפרמטרים: מה קורה כשצפיפות העצים גבוהה מאוד? (רמז: אסונות גדולים יותר). מה אם סיכוי הברק גבוה מדי? (היער לעולם לא יירגע). מה אם קצב הצמיחה איטי מדי? (היער יתקשה להתאושש). תגלו ששינויים קטנים בפרמטרים יכולים להשפיע <strong style="color: #dc3545;">דרמטית</strong> על התנהגות היער כולו, תופעה אופיינית למערכות מורכבות רבות, מטקטוניקת לוחות ועד התפשטות מחלות.</p>

    <p>מודלים כמו אש היער הם לא רק משחקים חזותיים. הם כלי מחקר יקרי ערך במדעים רבים - פיזיקה סטטיסטית, אקולוגיה, מדעי המחשב, ועוד. הם עוזרים לנו להבין איך סדר וארגון יכולים לצוץ באופן ספונטני מתוך אינטראקציות מקומיות פשוטות, וכיצד כאוס (תלות רגישה בתנאי ההתחלה ובפרמטרים) הוא לעיתים קרובות תוצאה בלתי נפרדת ממערכות הנשלטות על ידי חוקים דטרמיניסטיים לכאורה. שחקו, נסו, וצפו בפלא הפשטות שיוצר מורכבות!</p>
</div>


<script>
    const canvas = document.getElementById('forestCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const resetButton = document.getElementById('resetButton');
    const densityInput = document.getElementById('density');
    const densityValueSpan = document.getElementById('densityValue');
    const growthProbInput = document.getElementById('growthProb');
    const growthProbValueSpan = document.getElementById('growthProbValue');
    const lightningProbInput = document.getElementById('lightningProb');
    const lightningProbValueSpan = document.getElementById('lightningProbValue');
    const fireSpreadProbInput = document.getElementById('fireSpreadProb');
    const fireSpreadProbValueSpan = document.getElementById('fireSpreadProbValue');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');
    const explanationContent = document.getElementById('explanationContent');

    const GRID_SIZE = 100; // Larger grid for more impressive simulations
    const CELL_SIZE = 6; // Pixels per cell
    canvas.width = GRID_SIZE * CELL_SIZE;
    canvas.height = GRID_SIZE * CELL_SIZE;

    // States: 0: Empty, 1: Tree, 2: Burning
    const STATE_EMPTY = 0;
    const STATE_TREE = 1;
    const STATE_BURNING = 2;

    // Enhanced color palette
    const COLORS = {
        [STATE_EMPTY]: '#f0f0e0', // Warm light beige/earth
        [STATE_TREE]: '#1a7f32', // Rich forest green
        [STATE_BURNING]: '#d9534f' // Firebrick red
    };

    let grid = [];
    let animationFrameId = null;
    let lastUpdateTime = 0;
    const updateInterval = 50; // Faster update interval (milliseconds)

    // Get parameter values
    const getParameters = () => ({
        initialDensity: parseInt(densityInput.value) / 100,
        growthProb: parseFloat(growthProbInput.value) / 100,
        lightningProb: parseFloat(lightningProbInput.value) / 100,
        fireSpreadProb: parseFloat(fireSpreadProbInput.value) / 100
    });

    // Update parameter value displays immediately on input
    densityInput.addEventListener('input', () => {
        densityValueSpan.textContent = `${densityInput.value}%`;
    });
    growthProbInput.addEventListener('input', () => {
        growthProbValueSpan.textContent = `${growthProbInput.value}%`;
    });
    lightningProbInput.addEventListener('input', () => {
        lightningProbValueSpan.textContent = `${lightningProbInput.value}%`;
    });
    fireSpreadProbInput.addEventListener('input', () => {
        fireSpreadProbValueSpan.textContent = `${fireSpreadProbInput.value}%`;
    });


    // Initialize the grid
    function initializeGrid(initialDensity) {
        grid = new Array(GRID_SIZE).fill(null).map(() => new Array(GRID_SIZE));
        for (let y = 0; y < GRID_SIZE; y++) {
            for (let x = 0; x < GRID_SIZE; x++) {
                grid[y][x] = Math.random() < initialDensity ? STATE_TREE : STATE_EMPTY;
            }
        }
    }

    // Draw the current state of the grid
    function drawGrid() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let y = 0; y < GRID_SIZE; y++) {
            for (let x = 0; x < GRID_SIZE; x++) {
                ctx.fillStyle = COLORS[grid[y][x]];
                ctx.fillRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
            }
        }
    }

    // Count burning neighbors (8 neighbors, including diagonals)
    function countBurningNeighbors(x, y, currentGrid) {
        let burningCount = 0;
        for (let dy = -1; dy <= 1; dy++) {
            for (let dx = -1; dx <= 1; dx++) {
                if (dx === 0 && dy === 0) continue;
                const nx = x + dx;
                const ny = y + dy;
                if (nx >= 0 && nx < GRID_SIZE && ny >= 0 && ny < GRID_SIZE) {
                    if (currentGrid[ny][nx] === STATE_BURNING) {
                        burningCount++;
                    }
                }
            }
        }
        return burningCount;
    }

    // Update the grid to the next state based on rules
    function updateGrid(parameters) {
        const nextGrid = new Array(GRID_SIZE).fill(null).map(() => new Array(GRID_SIZE));

        for (let y = 0; y < GRID_SIZE; y++) {
            for (let x = 0; x < GRID_SIZE; x++) {
                const currentState = grid[y][x];
                let nextState = currentState; // Assume state remains the same by default

                switch (currentState) {
                    case STATE_BURNING:
                        // Rule 1: Burning trees become empty
                        nextState = STATE_EMPTY;
                        break;
                    case STATE_TREE:
                        // Rule 2: Trees
                        const burningNeighbors = countBurningNeighbors(x, y, grid);
                        if (burningNeighbors > 0 && Math.random() < parameters.fireSpreadProb) {
                            // Catches fire from a neighbor with fireSpreadProb
                            nextState = STATE_BURNING;
                        } else if (Math.random() < parameters.lightningProb) {
                            // Catches fire from lightning with lightningProb
                            nextState = STATE_BURNING;
                        } else {
                            // Remains a tree
                            nextState = STATE_TREE;
                        }
                        break;
                    case STATE_EMPTY:
                        // Rule 3: Empty spots
                        if (Math.random() < parameters.growthProb) {
                            // Grows a new tree with growthProb
                            nextState = STATE_TREE;
                        } else {
                            // Remains empty
                            nextState = STATE_EMPTY;
                        }
                        break;
                }
                nextGrid[y][x] = nextState;
            }
        }
        grid = nextGrid; // Update the main grid
    }

    // Animation loop using requestAnimationFrame with time-based updates
    function animate(currentTime) {
        if (!lastUpdateTime) lastUpdateTime = currentTime;
        const elapsed = currentTime - lastUpdateTime;

        if (elapsed > updateInterval) {
            // Process multiple steps if elapsed time is large
            const stepsToTake = Math.floor(elapsed / updateInterval);
            for(let i = 0; i < stepsToTake; i++) {
                const parameters = getParameters();
                 // Pass current grid to update function if needed for rule evaluation
                updateGrid(parameters); // This updates 'grid'
            }
            lastUpdateTime = currentTime - (elapsed % updateInterval); // Adjust for lag

            drawGrid(); // Draw only after updates
        }

        animationFrameId = requestAnimationFrame(animate);
    }

    // Start simulation
    function startSimulation() {
        if (animationFrameId === null) { // Prevent starting if already running
             lastUpdateTime = 0; // Reset timer for the first frame after start/resume
             animationFrameId = requestAnimationFrame(animate);
             startButton.disabled = true;
             stopButton.disabled = false;
             resetButton.disabled = false;
        }
    }

    // Stop simulation
    function stopSimulation() {
        if (animationFrameId !== null) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
             startButton.disabled = false;
             stopButton.disabled = true;
             resetButton.disabled = false;
        }
    }

    // Reset simulation
    function resetSimulation() {
        stopSimulation();
        const parameters = getParameters();
        initializeGrid(parameters.initialDensity);
        drawGrid();
        startButton.disabled = false;
        stopButton.disabled = true; // Cannot stop if not started
        resetButton.disabled = false;
    }

    // Event Listeners for buttons
    startButton.addEventListener('click', startSimulation);
    stopButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);

    // Initial setup
    resetSimulation(); // Start with a fresh grid
    stopButton.disabled = true; // Disable stop button initially

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר את הסוד: מה מניע את המודל? 📖' : 'גלו את הסוד: מה מניע את המודל? 📖';
         // Scroll to explanation if showing it
        if (isHidden) {
            explanationContent.scrollIntoView({ behavior: 'smooth' });
        }
    });


</script>
---
```