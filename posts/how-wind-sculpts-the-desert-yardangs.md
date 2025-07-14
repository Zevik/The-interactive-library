---
title: "איך הרוח מפסלת את המדבר: ירדנגים"
english_slug: how-wind-sculpts-the-desert-yardangs
category: "מדעי הסביבה / גאוגרפיה"
tags: [ירדנגים, שחיקת רוח, מדבר, צורות נוף, גאומורפולוגיה]
---
<h1>איך הרוח מפסלת את המדבר: ירדנגים</h1>

<p>דמיינו שאתם עומדים בלב מדבר צחיח, מסביבכם רק חול וסלעים. לפתע, אתם מזהים פסלים טבעיים מדהימים - רכסים ארוכים, מוארכים, מפוסלים בצורה מושלמת, כאילו יד ענקית פיסלה אותם במשך אלפי שנים. מהו הכוח הסודי הזה שיוצר את הפסלים הללו רק באמצעות תנועה בלתי פוסקת?</p>

<div class="simulation-container" dir="rtl">
    <h2>המעבדה המדברית שלך: צור ירדנג</h2>
    <div class="controls">
        <div class="control-group">
            <label for="windStrength">כוח הרוח:</label>
            <input type="range" id="windStrength" min="1" max="10" value="3">
            <span id="windValue" class="slider-value">3</span>
        </div>
        <div class="control-group">
            <label for="timeSteps">זמן השחיקה (צעדים):</label>
            <input type="range" id="timeSteps" min="10" max="200" value="50">
            <span id="timeValue" class="slider-value">50</span>
        </div>
        <div class="buttons-group">
            <button id="startSimulation" class="action-button primary">התחל ליצור!</button>
            <button id="resetSimulation" class="action-button secondary">התחל מהתחלה</button>
        </div>
         <div class="simulation-status">
            צעד נוכחי: <span id="currentStep">0</span>
        </div>
    </div>
    <div class="simulation-area">
        <canvas id="yardangCanvas"></canvas>
        <div class="wind-indicator">← רוח</div>
    </div>
    <p class="simulation-caption">צבע בהיר: חומר רך (נשחק בקלות). צבע כהה: חומר קשה (עמיד יותר). הרוח נושבת מימין לשמאל.</p>
</div>

<button id="toggleExplanation" class="toggle-button">מה זה הדבר המדהים הזה? (הצג הסבר)</button>

<div id="explanation" class="hidden" dir="rtl">
    <h2>פרופיל זיהוי: ירדנגים במדבר</h2>

    <h3>אז... מה בדיוק ראית כאן?</h3>
    <p>ראית תהליך קסום של שחיקת רוח יוצר צורות נוף ייחודיות שנקראות <strong>ירדנגים</strong> (Yardangs). תחשוב עליהם כעל "ספינות מדבר" או "פסלי רוח", שנפוצים במדבריות הצחיחים ביותר בעולם.</p>

    <h3>כוחה הבלתי נראה של הרוח: שחיקה אאולית</h3>
    <p>הרוח היא לא רק אוויר שזז. במדבר, כשהיא אוספת חלקיקי חול ואבק, היא הופכת לכלי פיסול רב עוצמה. התהליך הזה נקרא שחיקה אאולית (Aeolian Erosion), והוא קורה בשתי דרכים:</p>
    <ul>
        <li><strong>דפלציה (Deflation):</strong> הרוח פשוט "מטאטאת" ומעיפה חלקיקים קטנים, כמו אבק וחול דק, ומשאירה מאחור את החומרים הגסים או הדחוסים יותר.</li>
        <li><strong>אברזיה (Abrasion):</strong> זה החלק האמנותי יותר. חלקיקי החול הנישאים ברוח פוגעים במשטחי סלע או קרקע חשופים, בדיוק כמו נייר זכוכית ענק בטבע. הפגיעות האלה שוחקות בהדרגה את פני השטח. השחיקה החזקה ביותר קורית בדרך כלל בגובה נמוך, קרוב לקרקע, כי שם ריכוז החול הגבוה ביותר.</li>
    </ul>

    <h3>למה דווקא הצורה הזו? הסוד הוא בכיוון הרוח ובחומרים שונים</h3>
    <p>כדי שירדנגים ייווצרו, צריך שני דברים עיקריים:</p>
    <ol>
        <li><strong>רוח עקבית:</strong> הרוח צריכה לנשוב מאותו כיוון עיקרי לאורך אלפי (ואפילו מיליוני!) שנים. זה מה שנותן לירדנגים את צורתם המוארכת והמכוונת.</li>
        <li><strong>חומרים שונים:</strong> הקרקע או הסלע חייבים להיות מורכבים משכבות או אזורים בעלי קשיחות שונה – חלק רך שקל לשחוק, וחלק קשה ועמיד יותר. זה המפתח לשחיקה <strong>דיפרנציאלית</strong> (שחיקה שונה בחומרים שונים).</li>
    </ol>
    <p>כשהרוח פוגעת בשטח כזה, היא שוחקת את החומר הרך מהר יותר. החומר הקשה יותר נשחק לאט יותר, וחשוב מכך - הוא מגן על האזור שמאחוריו (בכיוון שאליו הרוח נושבת). האזורים הרכים שסביב החומר הקשה "נעלמים" בקצב מהיר, והחומר הקשה נשאר, ויוצר רכס ארוך ומוארך בכיוון הרוח. הרכסים האלה הם הירדנגים, והעמקים ביניהם הם פשוט המקום שבו החומר הרך נעלם לחלוטין.</p>

    <h3>מסע ההיווצרות: משחיקה קטנה לפסל ענק</h3>
    <p>הכל מתחיל לרוב מבליטה קטנה או אזור מעט קשה יותר על פני השטח. הרוח מתחילה לשחוק את החומר הרך סביב הבליטה. לאט לאט, הבליטה הופכת למגן, והרוח ממשיכה לכרסם בחומר הרך משני הצדדים ומאחור. במשך זמן ארוך מאוד, התהליך הזה מעצב את האזור הקשה לצורה אווירודינמית שמפחיתה את ההתנגדות לרוח ומאפשרת לו "לגדול" ולהתארך בכיוון הנשיבה. זהו תהליך איטי, אבל התוצאות מרשימות!</p>

    <h3>לא רק במדבריות בכדור הארץ</h3>
    <p>צורות דומות לירדנגים נמצאו גם על כוכבי לכת אחרים עם אטמוספירה ורוחות, כמו מאדים! זה מראה שעקרונות הפיסול של הרוח עובדים בכל מקום ביקום.</p>
    <p>אז בפעם הבאה שתראו צורות סלע מוזרות במדבר, זכרו שמאחוריהן מסתתר סיפור מדהים על רוח, חול, וזמן אינסופי.</p>
</div>

<style>
    :root {
        --sand-light: #f5f5dc;
        --sand-medium: #c1b5a3;
        --sand-dark: #a08a70;
        --rock-soft: #d2b48c; /* Tan */
        --rock-hard: #8b4513; /* Saddle Brown */
        --sky-blue: #87ceeb; /* Sky Blue */
        --control-bg: #fff;
        --button-primary: #ff9800; /* Orange */
        --button-primary-hover: #f57c00; /* Darker Orange */
        --button-secondary: #795548; /* Brown */
        --button-secondary-hover: #5d4037; /* Darker Brown */
        --text-color: #333;
        --border-color: #ccc;
        --shadow-color: rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        background-color: var(--sand-light);
        color: var(--text-color);
        min-height: 100vh;
    }

    h1, h2, h3 {
        color: var(--rock-hard);
        text-align: center;
        margin-bottom: 15px;
    }
     h1 { font-size: 2.2em; }
     h2 { font-size: 1.8em; }
     h3 { font-size: 1.4em; }

    p {
        margin-bottom: 15px;
        text-align: justify;
    }

    .simulation-container {
        border: 2px solid var(--sand-dark);
        padding: 20px;
        margin: 30px auto;
        background-color: var(--sand-medium);
        border-radius: 12px;
        box-shadow: 0 8px 16px var(--shadow-color);
        max-width: 700px;
    }

    .controls {
        margin-bottom: 20px;
        text-align: center;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px;
        padding: 10px;
        background-color: var(--control-bg);
        border-radius: 8px;
        box-shadow: inset 0 2px 5px var(--shadow-color);
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: center;
        min-width: 150px;
    }

    .controls label {
        margin-bottom: 5px;
        font-weight: bold;
        color: var(--rock-hard);
        font-size: 0.9em;
    }

    .controls input[type="range"] {
        direction: ltr; /* Sliders are LTR for better usability */
        width: 100%;
        max-width: 200px; /* Limit slider width */
        -webkit-appearance: none; /* Override default appearance */
        appearance: none;
        height: 8px;
        background: var(--sand-dark);
        outline: none;
        opacity: 0.8;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: var(--button-primary);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--button-primary-hover);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: var(--button-primary);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--button-primary-hover);
    }

    .slider-value {
        font-weight: bold;
        color: var(--rock-hard);
        font-size: 1em;
        margin-top: 5px;
    }

    .buttons-group {
        display: flex;
        gap: 10px;
        justify-content: center;
        width: 100%; /* Take full width on small screens */
    }

    .action-button {
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .action-button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }

    .primary {
        background-color: var(--button-primary);
        color: white;
    }

    .primary:not(:disabled):hover {
        background-color: var(--button-primary-hover);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .primary:not(:disabled):active {
         transform: translateY(0);
         box-shadow: none;
    }

    .secondary {
        background-color: var(--button-secondary);
        color: white;
    }

    .secondary:not(:disabled):hover {
        background-color: var(--button-secondary-hover);
         transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
     .secondary:not(:disabled):active {
         transform: translateY(0);
         box-shadow: none;
    }

    .simulation-status {
         width: 100%;
         text-align: center;
         margin-top: 10px;
         font-size: 0.9em;
         color: var(--text-color);
    }

    .simulation-area {
        position: relative; /* Needed for absolute positioning of wind indicator */
        display: flex;
        justify-content: center;
        align-items: center; /* Center canvas vertically */
        margin-top: 15px;
        background-color: var(--sky-blue); /* Sky background */
        border-radius: 8px;
        overflow: hidden; /* Hide parts of wind indicator outside */
         border: 1px solid var(--rock-hard);
    }

    #yardangCanvas {
        display: block; /* Ensure no extra space below */
        background-color: transparent; /* Canvas background is the sky-blue of parent */
    }

    .wind-indicator {
        position: absolute;
        top: 10px;
        left: 10px;
        font-size: 1.2em;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        animation: windFlow 2s linear infinite; /* Add animation */
         pointer-events: none; /* Don't interfere with canvas clicks */
    }

     @keyframes windFlow {
        0% { transform: translateX(0); }
        50% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }

    .simulation-caption {
        text-align: center;
        font-size: 0.9em;
        color: var(--text-color);
        margin-top: 15px;
        font-style: italic;
    }

    .toggle-button {
        display: block;
        margin: 25px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        background-color: var(--button-secondary);
        color: white;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .toggle-button:hover {
        background-color: var(--button-secondary-hover);
         transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .toggle-button:active {
        transform: translateY(0);
         box-shadow: none;
    }

    .hidden {
        display: none;
    }

    #explanation {
        border: 1px solid var(--border-color);
        padding: 20px;
        background-color: var(--control-bg);
        border-radius: 8px;
        box-shadow: 0 4px 8px var(--shadow-color);
        max-width: 700px;
        margin: 20px auto;
    }

    #explanation h2, #explanation h3 {
        color: var(--rock-hard);
        border-bottom: 2px solid var(--sand-medium);
        padding-bottom: 8px;
        margin-bottom: 15px;
        text-align: right; /* Align explanation headings right */
    }

    #explanation ul, #explanation ol {
        margin-right: 25px;
        margin-bottom: 15px;
    }
     #explanation li {
         margin-bottom: 8px;
     }

     #explanation strong {
         color: var(--rock-hard);
     }
</style>

<script>
    const canvas = document.getElementById('yardangCanvas');
    const ctx = canvas.getContext('2d');
    const windStrengthSlider = document.getElementById('windStrength');
    const windValueSpan = document.getElementById('windValue');
    const timeStepsSlider = document.getElementById('timeSteps');
    const timeValueSpan = document.getElementById('timeValue');
    const startButton = document.getElementById('startSimulation');
    const resetButton = document.getElementById('resetSimulation');
    const toggleButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
    const currentStepSpan = document.getElementById('currentStep'); // Added for status display

    const canvasWidth = 600;
    const canvasHeight = 250; // Increased height slightly
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    const gridSize = 2; // Size of each simulation grid cell (pixels)
    const gridWidth = canvasWidth / gridSize;
    const gridHeight = canvasHeight / gridSize;

    let material; // Grid representing material hardness (0=soft, 1=hard)
    let heightMap; // Grid representing presence of material (1=present, 0=air)
    const baseHeightPx = 15; // Height of the solid base in pixels
    const initialGroundLevel = gridHeight - Math.ceil(baseHeightPx / gridSize); // Y index in grid coordinates above base

    function initializeSimulation() {
        // Initialize material and heightMap grids
        material = Array(gridWidth).fill(0).map(() => Array(gridHeight).fill(0));
        heightMap = Array(gridWidth).fill(0).map(() => Array(gridHeight).fill(0));

        // Fill the base layer
        for (let x = 0; x < gridWidth; x++) {
            for (let y = initialGroundLevel; y < gridHeight; y++) {
                heightMap[x][y] = 1;
                material[x][y] = 1; // Base is hard
            }
        }

        // Create an initial block of material on top of the base
        const blockHeightGrid = Math.ceil(80 / gridSize); // Example block height in grid units
        const blockStartLevel = initialGroundLevel - blockHeightGrid;
        const blockWidthGrid = Math.ceil(canvasWidth * 0.8 / gridSize); // Block covers 80% of width
        const blockStartX = Math.ceil(canvasWidth * 0.1 / gridSize); // Centered

        for (let x = blockStartX; x < blockStartX + blockWidthGrid; x++) {
            for (let y = blockStartLevel; y < initialGroundLevel; y++) {
                 if (x >= 0 && x < gridWidth && y >= 0 && y < gridHeight) { // Bounds check
                    heightMap[x][y] = 1;
                    material[x][y] = 0; // Start with soft material
                 }
            }
        }

        // Embed some hard layers/inclusions within the soft block
        for (let x = blockStartX; x < blockStartX + blockWidthGrid; x++) {
            // Wavy horizontal layer
            let layerHeightOffset = Math.sin(x / 10) * 3; // Wavy pattern amplitude 3 grid cells
            let layerY = blockStartLevel + Math.ceil(blockHeightGrid / 3) + Math.floor(layerHeightOffset);
            layerY = Math.max(blockStartLevel, Math.min(initialGroundLevel - 1, layerY)); // Keep layer within the block
            for (let y = layerY; y < Math.min(layerY + 2, initialGroundLevel); y++) { // Layer thickness 2 grid cells
                 if (x >= 0 && x < gridWidth && y >= 0 && y < gridHeight) { // Bounds check
                    material[x][y] = 1; // Make this layer hard
                 }
            }

             // Vertical inclusion (optional, adds variety)
             if (x > blockStartX + blockWidthGrid * 0.3 && x < blockStartX + blockWidthGrid * 0.3 + 5) {
                 let inclusionY = blockStartLevel + Math.ceil(blockHeightGrid / 2);
                 for(let y = inclusionY; y < Math.min(inclusionY + 15, initialGroundLevel); y++){ // Inclusion height 15 grid cells
                      if (x >= 0 && x < gridWidth && y >= 0 && y < gridHeight) { // Bounds check
                        material[x][y] = 1;
                      }
                 }
             }
             if (x > blockStartX + blockWidthGrid * 0.6 && x < blockStartX + blockWidthGrid * 0.6 + 5) {
                 let inclusionY = blockStartLevel + Math.ceil(blockHeightGrid / 2.5);
                 for(let y = inclusionY; y < Math.min(inclusionY + 12, initialGroundLevel); y++){ // Inclusion height 12 grid cells
                       if (x >= 0 && x < gridWidth && y >= 0 && y < gridHeight) { // Bounds check
                        material[x][y] = 1;
                       }
                 }
             }

        }

        currentStepSpan.textContent = '0'; // Reset step counter
        drawSimulation();
    }

    function drawSimulation() {
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Draw the base (always solid)
        ctx.fillStyle = varNameToColor('--rock-hard');
        ctx.fillRect(0, canvasHeight - baseHeightPx, canvasWidth, baseHeightPx);

        // Draw the material based on the current height map and material type
        for (let x = 0; x < gridWidth; x++) {
            for (let y = 0; y < gridHeight; y++) {
                 if (heightMap[x][y] === 1) {
                    if (material[x][y] === 1) {
                        ctx.fillStyle = varNameToColor('--rock-hard'); // Darker for hard material
                    } else {
                        ctx.fillStyle = varNameToColor('--rock-soft'); // Lighter for soft material
                    }
                    ctx.fillRect(x * gridSize, y * gridSize, gridSize, gridSize);
                 }
            }
        }

        // Wind indicator drawn via CSS, so not needed here.

    }

     function erodeStep(windStrength) {
        // Erosion rate is proportional to wind strength
        const erosionRateSoft = windStrength * 0.06; // Higher erosion for soft
        const erosionRateHard = windStrength * 0.015; // Lower erosion for hard

        let removedCells = []; // Keep track of cells to remove in this step

        // Iterate from windward side (right to left in RTL simulation)
        for (let x = gridWidth - 1; x >= 0; x--) {
            // Find the current exposed surface cell at this x coordinate (from top down)
            let surfaceY = -1;
            for(let y = 0; y < gridHeight; y++) {
                if (heightMap[x][y] === 1) {
                    surfaceY = y; // Found the top-most material cell
                    break;
                }
            }

            if (surfaceY !== -1) { // If material exists at this x column
                // Check if this surface point is exposed to wind
                // A point is exposed if there's no material directly to its right at the same or higher elevation
                let exposed = true;
                if (x < gridWidth - 1) { // Not the rightmost column
                    let neighborSurfaceY = -1;
                     // Find the top-most material cell in the column to the right (upwind)
                    for(let ny = 0; ny < gridHeight; ny++) {
                        if (heightMap[x + 1][ny] === 1) {
                            neighborSurfaceY = ny;
                            break;
                        }
                    }
                     // If there is material to the right, and it's at the same or higher level (smaller Y index), it's not exposed
                    if (neighborSurfaceY !== -1 && neighborSurfaceY <= surfaceY) {
                         exposed = false;
                    }
                } else {
                    // The rightmost column is always exposed from the right (where wind comes from)
                    exposed = true;
                }


                if (exposed) {
                    const currentMaterial = material[x][surfaceY];
                    const erosionAmount = (currentMaterial === 0) ? erosionRateSoft : erosionRateHard;

                    // Apply erosion based on probability
                    if (Math.random() < erosionAmount) {
                         removedCells.push({ x: x, y: surfaceY }); // Mark for removal
                    }
                }
            }
        }

        // Apply the removals simultaneously after determining all removals for this step
        removedCells.forEach(cell => {
            if (cell.y < gridHeight) { // Ensure valid index
                 heightMap[cell.x][cell.y] = 0;
            }
        });
    }

    let animationFrameId = null;

    function runSimulation() {
        const windStrength = parseInt(windStrengthSlider.value);
        const totalTimeSteps = parseInt(timeStepsSlider.value);
        let step = 0;

        startButton.disabled = true;
        resetButton.disabled = true;
        windStrengthSlider.disabled = true;
        timeStepsSlider.disabled = true;


        function animate() {
            if (step < totalTimeSteps) {
                erodeStep(windStrength);
                drawSimulation();
                step++;
                currentStepSpan.textContent = step; // Update step counter
                animationFrameId = requestAnimationFrame(animate); // Continue animation
            } else {
                startButton.disabled = false;
                resetButton.disabled = false;
                windStrengthSlider.disabled = false;
                timeStepsSlider.disabled = false;
                currentStepSpan.textContent = `${step} (הסתיים)`;
            }
        }

        // Clear any previous animation frame request
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }

        animate(); // Start the animation loop
    }

    // Helper to get CSS variable color
    function varNameToColor(varName) {
        return getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
    }

    // Event listeners for sliders
    windStrengthSlider.addEventListener('input', () => {
        windValueSpan.textContent = windStrengthSlider.value;
    });

    timeStepsSlider.addEventListener('input', () => {
        timeValueSpan.textContent = timeStepsSlider.value;
    });

    // Event listener for buttons
    startButton.addEventListener('click', runSimulation);
    resetButton.addEventListener('click', () => {
        // Cancel ongoing animation before resetting
         if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null; // Reset the ID
         }
        initializeSimulation();
        startButton.disabled = false;
        resetButton.disabled = false;
        windStrengthSlider.disabled = false;
        timeStepsSlider.disabled = false;
    });

    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.toggle('hidden');
        if (isHidden) {
            toggleButton.textContent = 'מה זה הדבר המדהים הזה? (הצג הסבר)';
        } else {
            toggleButton.textContent = 'הסתר הסבר';
        }
    });

    // Initialize the simulation on page load
    initializeSimulation();
</script>