---
title: "המירוץ הגדול: חוקי נפילה חופשית בהדמיה מרהיבה"
english_slug: free-fall-simulation
category: "פיזיקה"
tags: ["נפילה חופשית", "התנגדות אוויר", "סימולציה", "מכניקה", "גלילאו", "מהירות סופית"]
---
# המירוץ הגדול: חוקי נפילה חופשית בהדמיה מרהיבה

האם כבד תמיד מנצח קל במרוץ הנפילה? הצטרפו אלינו להדמיה אינטראקטיבית שתגלה לכם את הסודות המרתקים של נפילה חופשית והתנגדות אוויר. שנו את המסה ואת תנאי הסביבה וצפו בתוצאות המפתיעות! מי ינצח במרוץ אל הקרקע?

<div id="simulation-container">
    <div id="controls">
        <div class="control-group">
            <label for="mass1">מסה (אובייקט א'):</label>
            <input type="range" id="mass1" min="0.1" max="10" value="1" step="0.1">
            <span id="mass1-value" class="value-display">1.0</span> ק"ג
        </div>
        <div class="control-group">
            <label for="mass2">מסה (אובייקט ב'):</label>
            <input type="range" id="mass2" min="0.1" max="10" value="5" step="0.1">
            <span id="mass2-value" class="value-display">5.0</span> ק"ג
        </div>
        <div class="control-group">
            <label for="drag-coeff">התנגדות אוויר (מקדם גרר):</label>
            <input type="range" id="drag-coeff" min="0" max="0.5" value="0.1" step="0.01">
            <span id="drag-coeff-value" class="value-display">0.10</span> (קבוע)
        </div>
        <div class="control-group">
            <label>סביבת הנפילה:</label>
            <div class="radio-group">
                <input type="radio" id="mode-vacuum" name="mode" value="vacuum" checked>
                <label for="mode-vacuum">חלל (ריק מוחלט)</label>
                <input type="radio" id="mode-air" name="mode" value="air">
                <label for="mode-air">אוויר (עם גרר)</label>
            </div>
        </div>
        <button id="start-button">הזנק!</button>
        <button id="reset-button" class="secondary-button">אפס והכן</button>
    </div>
    <div id="simulation-area">
        <div id="start-line"></div>
        <div id="ground"></div>
         <div id="object1" class="falling-object"></div>
        <div id="object2" class="falling-object"></div>
        <div id="status-display"></div>
    </div>
</div>

<button id="toggle-explanation" class="secondary-button">הצג את הסודות מאחורי הנפילה</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: הפיזיקה של הנפילה</h2>
    <p>ההדמיה הזו מאפשרת לנו לחקור את כוח הכבידה ואת השפעת התנגדות האוויר על תנועת עצמים. האגדה מספרת שגלילאו גליליי הפיל עצמים ממגדל פיזה כדי להוכיח שבהיעדר אוויר, כל העצמים, ללא קשר למסתם, נופלים באותה תאוצה - תאוצת הכבידה (g), שהיא כ-9.81 מטר/שנייה² על פני כדור הארץ.</p>
    <p>אבל בעולם האמיתי, יש לנו אוויר! התנגדות האוויר היא כוח שפועל נגד כיוון התנועה, והוא תלוי בגורמים כמו מהירות העצם, צורתו, גודלו וצפיפות האוויר. בהדמיה זו, אנו משתמשים במודל פשטני שבו כוח ההתנגדות פרופורציונלי לריבוע המהירות (<span dir="ltr">F<sub>drag</sub> = kv²</span>), כאשר k הוא מקדם גרר המאגד את כל השפעות האוויר על צורת העצם וגודלו.</p>
    <p>הכוח השקול הפועל על העצם באוויר הוא כוח הכבידה פחות התנגדות האוויר (<span dir="ltr">F<sub>net</sub> = mg - kv²</span>). מכאן, התאוצה היא <span dir="ltr">a = g - (k/m)v²</span>. שימו לב! בגלל התנגדות האוויר, התאוצה *כן* תלויה במסה (m)! עצמים קלים יותר (עבור אותו k) מושפעים יותר מכוח הגרר היחסי (המנה <span dir="ltr">k/m</span> גדולה יותר), ולכן התאוצה שלהם קטנה יותר.</p>
    <p>ככל שהעצם מאיץ, כוח ההתנגדות גדל. לבסוף, הוא יכול להשתוות לכוח הכבידה (<span dir="ltr">mg = kv²</span>). בשלב זה, הכוח השקול הוא אפס, אין יותר תאוצה, והעצם נופל במהירות קבועה הנקראת **מהירות סופית** (<span dir="ltr">Terminal Velocity</span>). מהירות זו תהיה גדולה יותר עבור עצמים בעלי יחס מסה/גרר גדול יותר (כלומר, כבדים או "אווירודינמיים" יותר).</p>
    <p>שחקו עם המסה ומקדם הגרר כדי לראות איך הם משפיעים על המרוץ! בריק, המסה לא משנה. באוויר, העצם הכבד יותר (או בעל גרר נמוך יותר) בדרך כלל יגיע ראשון. ההדמיה ממחישה בצורה ויזואלית את ההבדל הדרמטי בין שני המצבים הפיזיקליים הללו.</p>
</div>


<style>
    /* כללי */
    body {
        font-family: 'Arial', sans-serif;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        background-color: #eef4f7; /* Soft background */
        color: #333;
        line-height: 1.6;
        padding: 20px;
        margin: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    h1 {
        color: #0a5275; /* Deep blue-green */
        text-align: center;
        margin-bottom: 15px;
        font-size: 2em;
        font-weight: bold;
    }
     h2 {
        color: #0d6e93; /* Slightly lighter blue-green */
        text-align: right;
        margin-bottom: 15px;
        font-size: 1.5em;
    }

    p {
        margin-bottom: 15px;
        text-align: justify;
    }
    /* מבנה ההדמיה */
    #simulation-container {
        display: flex;
        flex-direction: column;
        gap: 25px;
        max-width: 850px; /* Slightly wider container */
        width: 100%;
        margin: 20px auto;
        background-color: #ffffff;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* More pronounced shadow */
        padding: 25px;
        box-sizing: border-box; /* Include padding in width */
    }

    /* בקרות */
    #controls {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Adjust columns */
        gap: 20px; /* Increased gap */
        padding-bottom: 25px;
        border-bottom: 1px solid #e0e0e0; /* Lighter border */
    }

    .control-group {
        display: flex;
        flex-direction: column;
    }

    .control-group label {
        margin-bottom: 8px; /* Increased space */
        font-weight: bold;
        color: #333;
    }

    .control-group input[type="range"] {
        width: calc(100% - 60px); /* Adjust width to fit value and unit */
        vertical-align: middle;
        -webkit-appearance: none; /* Override default style */
        appearance: none;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #0d6e93; /* Thumb color */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #0d6e93;
        cursor: pointer;
        border-radius: 50%;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .value-display {
        display: inline-block;
        min-width: 40px; /* Enough space for value */
        text-align: left; /* Align value left */
        vertical-align: middle;
        font-weight: bold;
        color: #0a5275; /* Value color */
        margin-left: 5px;
    }
     .control-group span + span { /* For the unit next to value */
         font-weight: normal;
         color: #555;
         margin-right: 0;
         margin-left: 5px;
     }


    .radio-group {
        display: flex;
        align-items: center;
        gap: 15px; /* Space between radio options */
        margin-top: 5px; /* Space below label */
    }

    .control-group input[type="radio"] {
        margin-left: 5px; /* Space between radio and label */
        accent-color: #0a5275; /* Highlight color for radio */
    }
     .control-group label[for^="mode-"] {
         font-weight: normal; /* Radio labels less bold */
         margin-bottom: 0; /* No margin below radio label */
         cursor: pointer;
     }


    button {
        background-color: #0d6e93; /* Primary button color */
        color: white;
        border: none;
        border-radius: 6px;
        padding: 12px 20px; /* Larger padding */
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
        margin-top: 10px;
        font-weight: bold;
    }

    button:hover {
        background-color: #0a5275; /* Darker on hover */
    }

    button:active {
        transform: scale(0.98);
    }

    button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }


    #start-button {
        grid-column: span 2; /* Span across two columns if grid */
        text-align: center;
         background-color: #28a745; /* Green for start */
    }
    #start-button:hover {
        background-color: #218838;
    }

    .secondary-button {
         background-color: #6c757d; /* Grey for secondary actions */
         font-weight: normal;
    }
     .secondary-button:hover {
        background-color: #5a6268;
    }


    /* אזור ההדמיה */
    #simulation-area {
        position: relative;
        width: 100%;
        height: 500px; /* Increased height for longer fall */
        border: 1px solid #b0bec5; /* Soft border */
        background: linear-gradient(to bottom, #bbdefb 0%, #e3f2fd 100%); /* Subtle blue gradient background */
        overflow: hidden; /* Hide objects once they pass the ground */
        margin-top: 20px;
        border-radius: 8px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    #start-line {
        position: absolute;
        top: 40px; /* Starting height (higher up) */
        left: 0;
        right: 0;
        border-top: 2px dashed #555; /* More visible line */
        z-index: 0; /* Ensure line is behind objects */
    }

     #ground {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 30px; /* Thicker ground */
        background: linear-gradient(to bottom, #795548 0%, #5d4037 100%); /* Brown gradient ground */
        box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.2);
        z-index: 2;
    }


    .falling-object {
        position: absolute;
        top: 40px; /* Start position matches start-line */
        width: 35px; /* Slightly larger objects */
        height: 35px;
        border-radius: 50%;
        box-sizing: border-box; /* Include border in size */
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        z-index: 1;
        /* REMOVE CSS TRANSITION FOR TOP - JS HANDLES IT */
        /* transition: top linear; */
    }

    #object1 {
        background: linear-gradient(to bottom right, #ff7043, #e64a19); /* Orange gradient */
        border: 2px solid #bf360c;
        left: 30%; /* Initial horizontal position for obj1 */
        transform: translateX(-50%); /* Center based on left */
    }
     #object1::after { content: 'א'; } /* Label object 1 */


    #object2 {
        background: linear-gradient(to bottom right, #66bb6a, #388e3c); /* Green gradient */
        border: 2px solid #1b5e20;
        left: 70%; /* Initial horizontal position for obj2 */
        transform: translateX(-50%); /* Center based on left */
    }
    #object2::after { content: 'ב'; } /* Label object 2 */


     .falling-object.landed {
         /* Add a subtle animation or style change on landing */
         animation: landed-effect 0.3s ease-out forwards;
     }

     @keyframes landed-effect {
         0% { transform: translateX(-50%) scale(1); opacity: 1; }
         50% { transform: translateX(-50%) scale(1.05); opacity: 1;}
         100% { transform: translateX(-50%) scale(1); opacity: 0.9; } /* Slight fade */
     }

    #status-display {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.8);
        padding: 8px 15px;
        border-radius: 6px;
        font-size: 1.1em;
        font-weight: bold;
        color: #0a5275;
        z-index: 3; /* Above objects */
        min-width: 150px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        visibility: hidden; /* Hidden by default */
    }


    /* הסבר */
    #toggle-explanation {
        display: block; /* Make it a block element */
        margin: 30px auto; /* Center the button */
        background-color: #546e7a; /* Blue-grey for explanation toggle */
        font-weight: normal;
    }
     #toggle-explanation:hover {
         background-color: #455a64;
    }


    #explanation {
        max-width: 850px;
        margin: 20px auto;
        background-color: #eef4f7; /* Matches body background */
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid #d0d9df; /* Subtle border */
    }

    #explanation h2 {
        text-align: right;
        color: #0a5275;
        border-bottom: 1px solid #d0d9df;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    #explanation p {
        margin-bottom: 15px;
        text-align: justify;
    }
     #explanation span[dir="ltr"] {
         direction: ltr;
         display: inline-block; /* Ensure it flows correctly in RTL */
         margin: 0 3px;
         font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; /* Monospaced font for formulas */
         background-color: #f8f8f8;
         padding: 2px 5px;
         border-radius: 4px;
         border: 1px solid #eee;
     }

    /* רספונסיביות בסיסית */
    @media (max-width: 600px) {
        #controls {
            grid-template-columns: 1fr; /* Stack controls on small screens */
        }
        #start-button, #reset-button {
             grid-column: span 1; /* Remove span on small screens */
             width: 100%;
             box-sizing: border-box;
        }
        .radio-group {
            flex-direction: column; /* Stack radio buttons */
            align-items: flex-start;
            gap: 5px;
        }
         body {
             padding: 10px;
         }
         #simulation-container, #explanation {
             padding: 15px;
         }
          h1 {
              font-size: 1.5em;
          }
           h2 {
               font-size: 1.3em;
           }
    }
</style>

<script>
    // Get elements
    const mass1Input = document.getElementById('mass1');
    const mass2Input = document.getElementById('mass2');
    const mass1ValueSpan = document.getElementById('mass1-value');
    const mass2ValueSpan = document.getElementById('mass2-value');
    const dragCoeffInput = document.getElementById('drag-coeff');
    const dragCoeffValueSpan = document.getElementById('drag-coeff-value');
    const modeVacuumRadio = document.getElementById('mode-vacuum');
    const modeAirRadio = document.getElementById('mode-air');
    const startButton = document.getElementById('start-button');
    const resetButton = document.getElementById('reset-button');
    const object1Div = document.getElementById('object1');
    const object2Div = document.getElementById('object2');
    const simulationArea = document.getElementById('simulation-area');
    const statusDisplay = document.getElementById('status-display');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Physics constants
    const g = 9.81; // acceleration due to gravity (m/s^2)
    let dt = 1/60; // time step (s) - aiming for 60 fps

    // Simulation state variables
    let mass1, mass2, dragCoeff;
    let mode; // 'vacuum' or 'air'

    let obj1 = { y: 0, v: 0, m: 0, landed: false };
    let obj2 = { y: 0, v: 0, m: 0, landed: false };

    let simulationRunning = false;
    let animationFrameId = null;
    let startTime = null; // To track simulation time accurately

    // Scale mapping (pixels <-> meters)
    const simulationHeightPx = 500; // Matches CSS height
    const startHeightPx = 40; // Matches CSS start-line top
    const groundHeightPx = 30; // Matches CSS ground height
    const objectSizePx = 35; // Matches CSS object size

    // Define simulation boundaries in meters (using top of object for position y)
    // y = 0 is the top of the simulation area
    const scale = 100; // Pixels per meter. 500px simulation area = 5m simulated height.
    const startYMeters = startHeightPx / scale;
    const groundYMeters = (simulationHeightPx - groundHeightPx - objectSizePx) / scale; // Y position (meters) of the top of the object when it hits the ground


    // --- UI Update Functions ---

    function updateControlsDisplay() {
        mass1 = parseFloat(mass1Input.value);
        mass2 = parseFloat(mass2Input.value);
        dragCoeff = parseFloat(dragCoeffInput.value);
        mode = modeVacuumRadio.checked ? 'vacuum' : 'air';

        mass1ValueSpan.textContent = mass1.toFixed(1);
        mass2ValueSpan.textContent = mass2.toFixed(1);
        dragCoeffValueSpan.textContent = dragCoeff.toFixed(2);

        // Enable/disable drag coefficient slider based on mode
        dragCoeffInput.disabled = mode === 'vacuum' || simulationRunning;
        dragCoeffValueSpan.style.opacity = mode === 'vacuum' ? 0.5 : 1;
        dragCoeffValueSpan.style.pointerEvents = mode === 'vacuum' ? 'none' : 'auto'; // Prevent interaction if disabled
    }

    function setControlsEnabled(enabled) {
        mass1Input.disabled = !enabled || simulationRunning;
        mass2Input.disabled = !enabled || simulationRunning;
        // Drag coeff depends on mode AND enabled state
        dragCoeffInput.disabled = !enabled || mode === 'vacuum' || simulationRunning;
        modeVacuumRadio.disabled = !enabled || simulationRunning;
        modeAirRadio.disabled = !enabled || simulationRunning;
        startButton.disabled = simulationRunning; // Start button is disabled *only* when running
        resetButton.disabled = !enabled && !simulationRunning; // Reset enabled unless completely disabled
    }


    function updateVisuals() {
        // Convert meters (from top of simulation area) to pixels (top offset for the div)
        object1Div.style.top = (obj1.y * scale) + 'px';
        object2Div.style.top = (obj2.y * scale) + 'px';

        // Ensure objects stop visually at the ground level
        if (obj1.landed) {
             object1Div.style.top = groundYMeters * scale + 'px';
             object1Div.classList.add('landed'); // Add landed class for animation
        }
         if (obj2.landed) {
            object2Div.style.top = groundYMeters * scale + 'px';
            object2Div.classList.add('landed'); // Add landed class for animation
        }
    }

    function updateStatusDisplay(message, visible) {
        statusDisplay.textContent = message;
        statusDisplay.style.visibility = visible ? 'visible' : 'hidden';
    }


    // --- Simulation Logic ---

    function resetSimulation() {
        cancelAnimationFrame(animationFrameId);
        simulationRunning = false;
        startButton.textContent = 'הזנק!';
        updateStatusDisplay('', false); // Hide status

        updateControlsDisplay(); // Read latest values from controls

        obj1 = { y: startYMeters, v: 0, m: mass1, landed: false };
        obj2 = { y: startYMeters, v: 0, m: mass2, landed: false };

        // Remove landed class
        object1Div.classList.remove('landed');
        object2Div.classList.remove('landed');

        updateVisuals(); // Place objects at start

        setControlsEnabled(true); // Enable controls after reset
    }

    function stopSimulation() {
        cancelAnimationFrame(animationFrameId);
        simulationRunning = false;
        startButton.textContent = 'הזנק מחדש';
        setControlsEnabled(true); // Re-enable controls
    }

    function checkCollisions() {
         let simulationEnded = false;

        // Check for ground collision for object 1
        if (obj1.y >= groundYMeters && !obj1.landed) {
            obj1.y = groundYMeters; // Snap to ground
            obj1.v = 0; // Stop vertical movement
            obj1.landed = true;
        }

        // Check for ground collision for object 2
        if (obj2.y >= groundYMeters && !obj2.landed) {
            obj2.y = groundYMeters; // Snap to ground
            obj2.v = 0; // Stop vertical movement
            obj2.landed = true;
        }

        // Check if simulation should end (both objects landed)
        if (obj1.landed && obj2.landed) {
             simulationEnded = true;
             let statusText = '';
             if (mode === 'vacuum') {
                 statusText = 'בחלל (ריק) - תוצאת תיקו!';
             } else {
                 // Determine winner based on who landed first, or if it was very close
                 // This simple check might not be perfect if dt is large, but okay for visual sim
                 if (obj1.y === groundYMeters && obj2.y === groundYMeters) {
                      statusText = 'באוויר - תוצאת תיקו!'; // Should be rare unless properties are identical
                 } else if (obj1.y === groundYMeters) {
                      statusText = 'באוויר - אובייקט א\' נחת ראשון!';
                 } else if (obj2.y === groundYMeters) {
                      statusText = 'באוויר - אובייקט ב\' נחת ראשון!';
                 } else {
                      statusText = 'הסימולציה הסתיימה.'; // Fallback
                 }
             }
             updateStatusDisplay(statusText, true);

        }
        return simulationEnded;
    }


    function updatePhysics(deltaTime) {
        // F_net = mg - kv|v| (using v*abs(v) to ensure resistance opposes velocity direction)
        // a = F_net / m = g - (k/m)v|v|
        // Note: In this simulation, objects only fall downwards, so v is always positive (y increases).
        // a = g - (k/m)v^2

        const a1 = (mode === 'vacuum' || obj1.landed) ? (obj1.landed ? 0 : g) : g - (dragCoeff / obj1.m) * obj1.v * obj1.v;
        const a2 = (mode === 'vacuum' || obj2.landed) ? (obj2.landed ? 0 : g) : g - (dragCoeff / obj2.m) * obj2.v * obj2.v;

        // Euler integration (simple, but works for visualization)
        if (!obj1.landed) {
            obj1.v += a1 * deltaTime;
            obj1.y += obj1.v * deltaTime;
        }
         if (!obj2.landed) {
            obj2.v += a2 * deltaTime;
            obj2.y += obj2.v * deltaTime;
        }
    }


    function gameLoop(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsedSeconds = (timestamp - startTime) / 1000;
        startTime = timestamp; // Reset start time for next frame

        // Calculate delta time. If it's very large (e.g., after pause), cap it.
        // Use the fixed dt instead of elapsedSeconds for more stable simulation steps.
        const deltaTime = dt;

        updatePhysics(deltaTime);

        if (checkCollisions()) {
            stopSimulation();
        } else {
            updateVisuals();
            animationFrameId = requestAnimationFrame(gameLoop);
        }
    }

    function startSimulation() {
        if (simulationRunning) return;

        resetSimulation(); // Reset to start and read values again
        simulationRunning = true;
        startButton.textContent = '...במהלך המרוץ';
        updateStatusDisplay('המירוץ החל!', true);

        setControlsEnabled(false); // Disable controls while running
        resetButton.disabled = false; // Ensure reset is enabled
        startButton.disabled = true; // Disable start once clicked

        startTime = null; // Reset start time for the game loop
        animationFrameId = requestAnimationFrame(gameLoop);
    }


    // --- Event Listeners ---

    mass1Input.addEventListener('input', updateControlsDisplay);
    mass2Input.addEventListener('input', updateControlsDisplay);
    dragCoeffInput.addEventListener('input', updateControlsDisplay);

    // Update controls display and reset simulation when mode changes (only if not running)
    modeVacuumRadio.addEventListener('change', () => {
         updateControlsDisplay();
         if (!simulationRunning) {
             resetSimulation();
         }
    });
    modeAirRadio.addEventListener('change', () => {
         updateControlsDisplay();
          if (!simulationRunning) {
             resetSimulation();
         }
    });

    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);

    // Explanation toggle
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר את הסודות מאחורי הנפילה' : 'הצג את הסודות מאחורי הנפילה';
         // Scroll to the explanation if showing it? Maybe not needed, user clicks it.
    });


    // --- Initial Setup ---
    resetSimulation(); // Set initial state, read controls, and display objects
</script>
---