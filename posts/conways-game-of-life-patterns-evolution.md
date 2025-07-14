---
title: "משחק החיים של קונוויי: יצירת תבניות ואבולוציה"
english_slug: conways-game-of-life-patterns-evolution
category: "טכנולוגיה / מדעי המחשב"
tags:
  - סימולציה
  - אוטומטים תאיים
  - תכנות אינטראקטיבי
  - הדמיה
---
# משחק החיים של קונוויי: יצירת תבניות ואבולוציה

צללו לעולם הקסום של משחק החיים! ציירו תבניות מדהימות על הלוח וצפו כיצד "החיים" מתעוררים ומתפתחים צעד אחר צעד, על פי חוקים פשוטים אך גאוניים. מה יקרה ליצירות שלכם? האם הן ישרדו, יתנועעו ברחבי הלוח, יעלמו כלא היו, או אולי יפתיעו וייצרו דברים חדשים?

<div class="game-container">
    <canvas id="gameCanvas"></canvas>
    <div class="controls">
        <button id="playBtn" aria-label="הפעל סימולציה"><i class="fas fa-play"></i> הפעל</button>
        <button id="pauseBtn" aria-label="השהה סימולציה"><i class="fas fa-pause"></i> השהה</button>
        <button id="nextBtn" aria-label="צעד הסימולציה הבא"><i class="fas fa-step-forward"></i> צעד הבא</button>
        <button id="clearBtn" aria-label="נקה את הלוח"><i class="fas fa-redo"></i> נקה הכל</button>
    </div>
</div>

<button id="showExplanationBtn" class="show-explanation-button">פשעו את הקוד: גלו את החוקים מאחורי המשחק!</button>

<div id="explanation" class="explanation-content" style="display: none;">
    <h2>הסודות נחשפים: כך עובד משחק החיים</h2>
    <p>זהו סימולטור "משחק החיים" של המתמטיקאי האגדי ג'ון קונוויי, דוגמה מדהימה לאוטומט תאי. ה"עולם" כאן הוא רשת פשוטה של תאים, כאשר כל תא יכול להיות בשני מצבים בלבד: "חי" או "מת". הקסם קורה כאשר העולם מתפתח בצעדים בדידים, וכל צעד נקבע על פי ארבעה חוקים מינימליסטיים החלים בו-זמנית על כל תא, בהתבסס על מצב שכניו החיים (מבין שמונת השכנים המקיפים אותו):</p>
    <ul>
        <li>**לידה (Birth):** תא מת שיש לו <strong>בדיוק 3 שכנים חיים</strong> - קם לתחייה והופך לחי בצעד הבא.</li>
        <li>**הישרדות (Survival):** תא חי שיש לו <strong>2 או 3 שכנים חיים</strong> - שורד ונשאר חי בצעד הבא.</li>
        <li>**מוות מעומס יתר (Overpopulation):** תא חי שיש לו <strong>יותר מ-3 שכנים חיים</strong> - מת בצעד הבא (חנק!).</li>
        <li>**מוות מבדידות (Underpopulation):** תא חי שיש לו <strong>פחות מ-2 שכנים חיים</strong> - מת בצעד הבא (עצוב...).</li>
    </ul>
    <p>היופי של משחק החיים טמון ביכולת שלו להראות כיצד מתוך חוקים מקומיים ופשוטים להפליא, יכולה להיווצר התנהגות גלובלית מורכבת, דינמית ומפתיעה לחלוטין. נסו לצייר תבניות ידועות כמו "מאיר" (Blinker), "גליידר" (Glider) או "בלוק" (Block), ובחנו כיצד הן מתנהגות לאורך זמן! נסו ליצור תבניות משלכם וראו מה יקרה...</p>
</div>

<style>
    /* ייבוא פונטים ועיצוב כללי */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'); /* לשימוש באייקונים */

    :root {
        --primary-color: #3498db; /* כחול רענן */
        --secondary-color: #2c3e50; /* כחול אפור עמוק */
        --success-color: #2ecc71; /* ירוק חיים */
        --danger-color: #e74c3c; /* אדום עצירה */
        --info-color: #f39c12; /* כתום פעולה */
        --background-color: #ecf0f1; /* רקע אפור בהיר מאוד */
        --card-background: #ffffff; /* רקע כרטיס לבן */
        --border-color: #bdc3c7; /* גבול אפור עדין */
        --text-color: #34495e; /* צבע טקסט כהה */
        --canvas-background: #dfe6e9; /* רקע קנבס אפור בהיר */
        --live-cell-color: #34495e; /* צבע תא חי - כהה */
        --button-padding: 10px 20px;
        --border-radius: 8px; /* פינות מעוגלות יותר */
        --transition-speed: 0.3s;
        --box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
        max-width: 800px;
        margin: 20px auto;
        direction: rtl; /* Ensure RTL layout */
        text-align: right; /* Ensure text alignment */
        box-sizing: border-box;
    }

    h1 {
        color: var(--secondary-color);
        text-align: center;
        margin-bottom: 30px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    h2 {
        color: var(--primary-color);
        text-align: right;
        margin-top: 0;
        margin-bottom: 15px;
        font-weight: 700;
    }

    p {
        margin-bottom: 18px;
    }

    .game-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 25px;
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 25px;
        box-shadow: var(--box-shadow);
    }

    canvas {
        border: 1px solid var(--border-color);
        background-color: var(--canvas-background);
        display: block;
        margin-bottom: 25px;
        cursor: crosshair; /* סמן עכבר מותאם לציור */
        border-radius: var(--border-radius);
        transition: box-shadow var(--transition-speed) ease;
    }

    canvas:hover {
        box-shadow: 0 0 20px rgba(52, 152, 219, 0.4); /* זוהר קל על ריחוף */
    }

    .controls {
        display: flex;
        gap: 12px; /* רווח גדול יותר בין כפתורים */
        flex-wrap: wrap;
        justify-content: center;
        width: 100%; /* ממלא רוחב כדי ש-wrap יעבוד טוב */
    }

    button {
        padding: var(--button-padding);
        border: none;
        border-radius: var(--border-radius);
        cursor: pointer;
        font-size: 1rem;
        transition: background-color var(--transition-speed) ease, transform 0.1s ease, box-shadow 0.2s ease;
        font-weight: 700;
        display: inline-flex; /* לאפשר אייקונים ליד טקסט */
        align-items: center;
        gap: 8px; /* רווח בין אייקון לטקסט */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    button:hover {
        transform: translateY(-3px); /* אפקט ריחוף עדין */
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    button:active {
        transform: translateY(0);
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    #playBtn { background-color: var(--success-color); color: white; }
    #playBtn:hover { background-color: #27ae60; } /* ירוק כהה יותר */

    #pauseBtn { background-color: var(--danger-color); color: white; }
    #pauseBtn:hover { background-color: #c0392b; } /* אדום כהה יותר */

    #nextBtn { background-color: var(--info-color); color: white; }
    #nextBtn:hover { background-color: #e67e22; } /* כתום כהה יותר */

    #clearBtn { background-color: var(--secondary-color); color: white; }
    #clearBtn:hover { background-color: #34495e; } /* כחול אפור כהה יותר */

    .show-explanation-button {
        display: block;
        width: fit-content; /* כפתור בגודל התוכן */
        margin: 30px auto; /* ממורכז עם רווח גדול יותר */
        background-color: var(--primary-color);
        color: white;
        text-align: center;
        font-size: 1.1rem;
        padding: 12px 25px;
        box-shadow: var(--box-shadow);
    }
     .show-explanation-button:hover {
         background-color: #2980b9; /* כחול כהה יותר */
     }

    .explanation-content {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 25px;
        margin-top: 20px;
        box-shadow: var(--box-shadow);
        animation: fadeIn 0.6s ease-out; /* אנימציה איטית וחלקה יותר */
    }

    .explanation-content h2 {
        text-align: right;
        color: var(--secondary-color);
        margin-top: 0;
        margin-bottom: 20px;
        border-bottom: 2px solid var(--primary-color); /* קו הפרדה לכותרת */
        padding-bottom: 10px;
    }

    .explanation-content ul {
        list-style-type: none; /* הסתרת תבליטים ברירת מחדל */
        padding-right: 0; /* איפוס padding ברירת מחדל */
        margin-right: 0;
        margin-bottom: 20px;
    }

    .explanation-content li {
        margin-bottom: 12px;
        padding-right: 20px; /* רווח לתבליט מותאם אישית */
        position: relative; /* למיקום התבליט */
    }

    .explanation-content li:before {
        content: '\2022'; /* תו תבליט (נקודה) */
        color: var(--primary-color); /* צבע התבליט */
        font-weight: bold;
        display: inline-block;
        width: 1em;
        margin-right: 10px;
        position: absolute;
        right: 0;
        top: 0;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); } /* אנימציה עם תזוזה גדולה יותר */
        to { opacity: 1; transform: translateY(0); }
    }
</style>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const playBtn = document.getElementById('playBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const nextBtn = document.getElementById('nextBtn');
    const clearBtn = document.getElementById('clearBtn');
    const showExplanationBtn = document.getElementById('showExplanationBtn');
    const explanationDiv = document.getElementById('explanation');

    const GRID_SIZE = 40; // Increased grid size for more complex patterns
    const CELL_SIZE = 15; // Pixel size per cell
    canvas.width = GRID_SIZE * CELL_SIZE;
    canvas.height = GRID_SIZE * CELL_SIZE;

    let grid = createGrid(GRID_SIZE, GRID_SIZE);
    let simulationInterval = null;
    let isDrawing = false;
    let drawState = true; // True for drawing life, false for erasing
    const simulationSpeed = 120; // Milliseconds per generation (faster simulation)

    // --- Grid Initialization ---
    function createGrid(rows, cols) {
        return Array(rows).fill(null).map(() => Array(cols).fill(0));
    }

    function clearGrid() {
        grid = createGrid(GRID_SIZE, GRID_SIZE);
        drawGrid();
        pauseSimulation();
    }

    // --- Drawing ---
    function drawGrid() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw grid lines (subtle)
        ctx.strokeStyle = 'rgba(189, 195, 199, 0.5)'; // Lighter grid lines
        ctx.lineWidth = 0.5; // Thinner lines
        for (let i = 0; i <= GRID_SIZE; i++) {
            ctx.beginPath();
            ctx.moveTo(i * CELL_SIZE, 0);
            ctx.lineTo(i * CELL_SIZE, canvas.height);
            ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(0, i * CELL_SIZE);
            ctx.lineTo(canvas.width, i * CELL_SIZE);
            ctx.stroke();
        }


        ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--live-cell-color').trim(); // Use CSS variable for cell color
        const cellInset = 1; // Pixels to inset the drawn cell from the grid square
        for (let row = 0; row < GRID_SIZE; row++) {
            for (let col = 0; col < GRID_SIZE; col++) {
                if (grid[row][col] === 1) {
                    // Draw cell with a slight gap
                    ctx.fillRect(col * CELL_SIZE + cellInset, row * CELL_SIZE + cellInset, CELL_SIZE - cellInset * 2, CELL_SIZE - cellInset * 2);
                }
            }
        }
    }

    function getMousePos(canvas, evt) {
        const rect = canvas.getBoundingClientRect();
        // Adjust for CSS scaling if any (though none applied here, good practice)
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        return {
            x: (evt.clientX - rect.left) * scaleX,
            y: (evt.clientY - rect.top) * scaleY
        };
    }

    function handleDrawing(event) {
        const pos = getMousePos(canvas, event);
        const col = Math.floor(pos.x / CELL_SIZE);
        const row = Math.floor(pos.y / CELL_SIZE);

        if (row >= 0 && row < GRID_SIZE && col >= 0 && col < GRID_SIZE) {
            // Only proceed if the cell state is different from the initial draw state
            const targetState = drawState ? 1 : 0;
            if (grid[row][col] !== targetState) {
                 grid[row][col] = targetState;
                 drawGrid(); // Redraw immediately when a cell changes state
            }
        }
    }

    canvas.addEventListener('mousedown', (event) => {
         pauseSimulation(); // Pause simulation when user starts drawing
         isDrawing = true;
         const pos = getMousePos(canvas, event);
         const col = Math.floor(pos.x / CELL_SIZE);
         const row = Math.floor(pos.y / CELL_SIZE);

         if (row >= 0 && row < GRID_SIZE && col >= 0 && col < GRID_SIZE) {
             // Determine whether we are drawing life or erasing based on the cell initially clicked
             drawState = (grid[row][col] === 0); // If clicked a dead cell, we draw life (1). If clicked a live cell, we erase (0).
             handleDrawing(event); // Handle the initial click
         }
    });

    canvas.addEventListener('mousemove', (event) => {
        if (isDrawing) {
            handleDrawing(event);
        }
    });

    canvas.addEventListener('mouseup', () => {
        isDrawing = false;
    });

     canvas.addEventListener('mouseleave', () => {
        isDrawing = false; // Stop drawing if mouse leaves the canvas
    });


    // --- Game Logic ---
    function countNeighbors(grid, row, col) {
        let sum = 0;
        for (let i = -1; i <= 1; i++) {
            for (let j = -1; j <= 1; j++) {
                if (i === 0 && j === 0) continue; // Don't count the cell itself

                // Wrap around edges (toroidal grid) - improved for clarity
                const neighborRow = (row + i + GRID_SIZE) % GRID_SIZE;
                const neighborCol = (col + j + GRID_SIZE) % GRID_SIZE;

                sum += grid[neighborRow][neighborCol];
            }
        }
        return sum;
    }

    function nextGeneration() {
        const newGrid = createGrid(GRID_SIZE, GRID_SIZE);
        let changesMade = false; // Track if any cells changed state

        for (let row = 0; row < GRID_SIZE; row++) {
            for (let col = 0; col < GRID_SIZE; col++) {
                const cellState = grid[row][col];
                const neighbors = countNeighbors(grid, row, col);
                let nextState = cellState; // Assume state doesn't change

                if (cellState === 1) { // If cell is currently alive
                    if (neighbors < 2 || neighbors > 3) {
                        nextState = 0; // Dies
                    } else {
                        nextState = 1; // Survives
                    }
                } else { // If cell is currently dead
                    if (neighbors === 3) {
                        nextState = 1; // Becomes alive
                    } else {
                        nextState = 0; // Stays dead
                    }
                }

                newGrid[row][col] = nextState;
                if (newGrid[row][col] !== grid[row][col]) {
                    changesMade = true;
                }
            }
        }
        grid = newGrid;
        drawGrid();

        // Optional: Pause simulation if the grid becomes static (no changes)
        // if (!changesMade && simulationInterval) {
        //     pauseSimulation();
        //     console.log("Simulation became static.");
        // }
    }

    // --- Simulation Controls ---
    function playSimulation() {
        if (!simulationInterval) {
            simulationInterval = setInterval(nextGeneration, simulationSpeed);
            playBtn.disabled = true; // Disable play while playing
            pauseBtn.disabled = false; // Enable pause
        }
    }

    function pauseSimulation() {
        clearInterval(simulationInterval);
        simulationInterval = null;
        playBtn.disabled = false; // Enable play
        pauseBtn.disabled = true; // Disable pause
    }

    // --- Event Listeners ---
    playBtn.addEventListener('click', playSimulation);
    pauseBtn.addEventListener('click', pauseSimulation);
    nextBtn.addEventListener('click', () => {
        pauseSimulation(); // Pause before stepping
        nextGeneration();
    });
    clearBtn.addEventListener('click', clearGrid);

    showExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            showExplanationBtn.textContent = 'להסתיר את החוקים';
             // Scroll smoothly to the explanation
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });

        } else {
            explanationDiv.style.display = 'none';
            showExplanationBtn.textContent = 'פשעו את הקוד: גלו את החוקים מאחורי המשחק!';
        }
    });

    // Initial setup
    pauseBtn.disabled = true; // Pause button starts disabled
    drawGrid();
</script>