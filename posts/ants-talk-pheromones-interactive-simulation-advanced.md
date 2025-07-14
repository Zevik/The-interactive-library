---
title: "נמלים מדברות פרומונים: סימולציה אינטראקטיבית מתקדמת"
english_slug: ants-talk-pheromones-interactive-simulation-advanced
category: "ביולוגיה"
tags:
  - נמלים
  - פרומונים
  - תקשורת כימית
  - התנהגות בעלי חיים
  - ביולוגיה התנהגותית
  - סימולציה
---
# נמלים מדברות פרומונים: סימולציה אינטראקטיבית מתקדמת

איך קהילה ענקית של מיליוני נמלים מתאמת את פעולותיה - מוצאת אוצרות מזון, בונה מנהרות סבוכות, ומזהירה זו את זו מפני סכנות אורבות - והכל בשקט מופתי, בלי להשמיע הגה? בואו נגלה את השפה הסודית והבלתי נראית לעין אנושית של הנמלים: תקשורת באמצעות פרומונים!

צללו לתוך הסימולציה וגלו כיצד שבילי ריח בלתי נראים מנחים את הנמלים במסען ומאפשרים התנהגות קולקטיבית מדהימה.

<div class="simulation-container">
    <canvas id="antSimulationCanvas"></canvas>
    <div class="controls-panel">
        <div class="control-group">
            <button id="startButton" class="control-button start-button">התחל מסע</button>
            <button id="stopButton" class="control-button stop-button" disabled>עצור/השהה</button>
            <button id="resetButton" class="control-button reset-button">אפס מושבה</button>
        </div>
        <div class="control-group slider-group">
            <label for="numAntsSlider">כמות נמלים במושבה:</label>
            <input type="range" id="numAntsSlider" min="10" max="300" value="100">
            <span id="numAntsValue" class="slider-value">100</span> נמלים
        </div>
         <div class="control-group slider-group">
            <label for="simulationSpeedSlider">מהירות זמן בסימולציה:</label>
            <input type="range" id="simulationSpeedSlider" min="1" max="10" value="5">
            <span id="simulationSpeedValue" class="slider-value">x5</span> מהירות
        </div>
        <div class="control-group info-group">
            <div>מזון שנאסף: <span id="foodFoundCount" class="info-value">0</span></div>
             <div>
                <label for="showPheromonesCheckbox">הצג שבילי פרומון:</label>
                <input type="checkbox" id="showPheromonesCheckbox" checked>
            </div>
        </div>
    </div>
</div>

<button id="toggleExplanationButton" class="toggle-explanation">
    הסבר מדעי: הצצה עמוקה לעולם הפרומונים
</button>

<div id="explanationContent" class="explanation-content" style="display: none;">
    <h2>השפה הנסתרת: פרומונים ותקשורת במושבת הנמלים</h2>

    <h3>מהם פרומונים וכיצד הם מניעים את עולם הנמלים?</h3>
    <p>דמיינו עולם שבו תקשורת מתרחשת לא דרך קול או אור, אלא דרך ריח! פרומונים הם בדיוק כאלה: מולקולות כימיות קטנטנות המופרשות על ידי יצור אחד כדי להשפיע על ההתנהגות או הפיזיולוגיה של יצור אחר מאותו המין. אצל נמלים, פרומונים הם עמוד השדרה של החיים החברתיים. הם מאפשרים תיאום מסובך ומדויק, החל ממסעות ציד משותפים ועד להגנה על הקן וזיהוי חברים ואויבים.</p>

    <h3>פרומונים והורמונים: קרובי משפחה כימיים עם תפקידים שונים</h3>
    <p>שניהם אותות כימיים, אך ההבדל מהותי: הורמונים פועלים *בתוך* הגוף (חושבו על גדילה, מצב רוח). פרומונים פועלים *מחוץ* לגוף ומשפיעים על פרטים *אחרים*. חשבו על הורמונים כמיילים פנימיים ועל פרומונים כציוצים ברשת חברתית של נמלים!</p>

    <h3>מגוון הריחות: סוגי פרומונים בנמלים</h3>
    <p>לנמלים יש אוצר מילים כימי מגוון להפליא:</p>
    <ul>
        <li>**פרומוני שביל (Trail Pheromones):** כשהסימולציה מראה נמלה חוזרת עם מזון, היא משאירה אחריה שביל ריח זעיר. נמלים אחרות "קוראות" את הריח הזה ועוקבות אחריו למקור המזון. זהו מנגנון יעיל להפליא לניווט המוני.</li>
        <li>**פרומוני אזהרה (Alarm Pheromones):** כשסכנה אורבת, נמלה מפרישה פרומון אזעקה. הריח הזה מתפשט במהירות וגורם לנמלים סמוכות להיכנס למצב דריכות, להימלט או להתגייס להגנה.</li>
        <li>**פרומוני גיוס (Recruitment Pheromones):** קשורים לפרומוני שביל, אך יכולים לגייס נמלים גם למשימות אחרות, כמו חפירה, סילוק פסולת או התקפה על יצור גדול.</li>
        <li>**פרומוני זיהוי קן (Nestmate Recognition Pheromones):** כל מושבה מפתחת "ריח משפחתי" ייחודי. פרומונים אלו מאפשרים לנמלה לזהות האם נמלה אחרת היא חברה מהקן או פולשת זרה שיש לסלק.</li>
    </ul>

    <h3>איך נמלה "מריחה" פרומון? האנטנות כמעבדה כימית ניידת</h3>
    <p>אנטנות הנמלה הן לא רק גששים פיזיים, אלא איברים מדהימים המכוסים באלפי קולטנים כימיים. כל קולטן "לוכד" מולקולות פרומון ספציפיות ושולח אות עצבי למוח הנמלה, שם המידע מעובד ומתורגם לפעולה (למשל, שינוי כיוון, הגברת מהירות, או תגובת אזעקה). הן כמו אפים זעירים ומתוחכמים ביותר!</p>

    <h3>הדינמיקה של שביל הפרומונים: יצירה, חיזוק והתפוגגות</h3>
    <p>שביל הפרומון המוביל למזון הוא מערכת דינמית. נמלים שמוצאות מזון מחזקות את השביל בחזרתן. ככל שיותר נמלים עוברות על שביל מסוים וחוזרות בהצלחה, כך הוא מתחזק ומושך אליו עוד נמלים. בו בזמן, הפרומונים מתנדפים לאוויר או מתפרקים בסביבה. ההתפוגגות חיונית! היא מונעת הצטברות אינסופית של שבילים ישנים ומאפשרת למושבה להגיב לשינויים - אם מקור מזון נעלם, השביל אליו יתפוגג במהירות יחסית.</p>

    <h3>משוב חיובי: סוד היעילות של נמלים</h3>
    <p>הניווט באמצעות שבילי פרומונים הוא דוגמה מבריקה למנגנון משוב חיובי. הצלחה (מציאת מזון וחזרה לקן) מובילה לחיזוק שביל הפרומון. שביל מחוזק מגדיל את הסיכוי לעוד הצלחות, שבתורן מחזקות עוד יותר את השביל. זהו מעגל שמעצים את עצמו ומוביל לגילוי יעיל ומהיר של מקורות מזון, גם במושבות ענק.</p>

    <h3>למה תקשורת פרומונלית היא מפתח להצלחה קולקטיבית?</h3>
    <p>יתרונותיה של שפה כימית זו עצומים:</p>
    <ul>
        <li>**יעילות בקנה מידה גדול:** תיאום מיליוני פרטים ללא "מנהיג" מרכזי.</li>
        <li>**עמידות:** המערכת מבוזרת. פגיעה בנמלה בודדת אינה משפיעה משמעותית על תפקוד המושבה כולה.</li>
        <li>**גמישות:** המערכת מסתגלת לשינויים בסביבה בזמן אמת.</li>
        <li>**דיסקרטיות:** קשה לטורפים או מתחרים ליירט או להבין את מסרי הפרומונים.</li>
    </ul>
    <p>הסימולציה שלפניכם מאפשרת לכם לצפות מקרוב במנגנון המדהים הזה בפעולה ולראות כיצד כל נמלה בודדת, הפועלת לפי כללים פשוטים יחסית, תורמת ליצירת התנהגות קולקטיבית מורכבת ויעילה.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('antSimulationCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const resetButton = document.getElementById('resetButton');
    const numAntsSlider = document.getElementById('numAntsSlider');
    const numAntsValue = document.getElementById('numAntsValue');
     const simulationSpeedSlider = document.getElementById('simulationSpeedSlider');
    const simulationSpeedValue = document.getElementById('simulationSpeedValue');
    const foodFoundCountSpan = document.getElementById('foodFoundCount');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');
    const explanationContent = document.getElementById('explanationContent');
    const showPheromonesCheckbox = document.getElementById('showPheromonesCheckbox');

    // Simulation parameters
    const GRID_SIZE = 20; // Size of grid cells in pixels
    const CANVAS_WIDTH = 700; // Increased width
    const CANVAS_HEIGHT = 450; // Increased height
    const GRID_WIDTH = CANVAS_WIDTH / GRID_SIZE;
    const GRID_HEIGHT = CANVAS_HEIGHT / GRID_SIZE;
    const NEST_POS_GRID = { x: 2, y: Math.floor(GRID_HEIGHT / 2) }; // Grid coordinates
    const FOOD_POS_GRID = { x: GRID_WIDTH - 3, y: Math.floor(GRID_HEIGHT / 2) }; // Grid coordinates
    const MAX_PHEROMONE = 255;
    let pheromoneFadeRate = 0.99; // Percentage remaining per logic step
    const PHEROMONE_DEPOSIT_AMOUNT = 80; // Amount added when ant returns with food
    const ANT_SPEED_PIXELS_PER_STEP = 2; // Visual speed per frame step
    const RANDOM_MOVE_PROB_BASE = 0.05; // Base probability of random exploration
    const PHEROMONE_SENSE_RADIUS = 2; // Grid cells radius around ant to check for pheromones

    canvas.width = CANVAS_WIDTH;
    canvas.height = CANVAS_HEIGHT;

    let animationFrameId = null;
    let lastLogicTime = 0;
    let logicInterval = 1000 / 15; // Logic updates per second (default 15)
    let pheromoneGrid = []; // Stores pheromone concentration
    let ants = [];
    let foodFoundCount = 0;
    let numAnts = parseInt(numAntsSlider.value);
    let isSimulationRunning = false;
    let showPheromones = showPheromonesCheckbox.checked;


    // Ant Class
    class Ant {
        constructor(gridX, gridY) {
            this.gridX = gridX; // Current grid cell X
            this.gridY = gridY; // Current grid cell Y
            this.visualX = gridX * GRID_SIZE + GRID_SIZE / 2; // Visual pixel X
            this.visualY = gridY * GRID_SIZE + GRID_SIZE / 2; // Visual pixel Y
            this.targetVisualX = this.visualX; // Target pixel X for smooth movement
            this.targetVisualY = this.visualY; // Target pixel Y for smooth movement
            this.carryingFood = false;
            // Simple state: 0 = searching for food, 1 = returning to nest
            this.state = 0;
            this.direction = Math.random() * Math.PI * 2; // Direction in radians for visual (not strictly used for grid move logic)
            this.color = '#333'; // Base color
        }

        // Determine the next grid cell based on state and environment
        determineNextGridCell() {
             const directions = [
                { dx: 0, dy: -1 }, { dx: 1, dy: -1 }, { dx: 1, dy: 0 }, { dx: 1, dy: 1 },
                { dx: 0, dy: 1 }, { dx: -1, dy: 1 }, { dx: -1, dy: 0 }, { dx: -1, dy: -1 }
            ];

            let nextCell = { x: this.gridX, y: this.gridY }; // Stay put by default
            let maxScore = -1;
            let scores = new Array(8).fill(0);
            let totalScore = 0;

            // Calculate scores for neighboring cells
            for (let i = 0; i < 8; i++) {
                const { dx, dy } = directions[i];
                const neighborX = this.gridX + dx;
                const neighborY = this.gridY + dy;

                // Check boundaries
                if (neighborX >= 0 && neighborX < GRID_WIDTH && neighborY >= 0 && neighborY < GRID_HEIGHT) {
                    let score = 0;
                    if (this.state === 0) { // Searching for food, follow pheromones
                        // Check pheromone in neighbor cell
                        score = pheromoneGrid[neighborY][neighborX];
                        // Add a small bias for moving forward or similar directions
                        const angleDiff = Math.abs(this.direction - Math.atan2(dy, dx));
                        // Bonus for directions close to current or preferred direction
                        score += score > 0 ? (MAX_PHEROMONE * 0.1 * (1 - Math.min(angleDiff, Math.PI * 2 - angleDiff) / Math.PI)) : 0;

                    } else { // Returning to nest, move towards nest
                        const targetX = NEST_POS_GRID.x;
                        const targetY = NEST_POS_GRID.y;
                         // Calculate squared distance to nest - closer is better
                        const distSq = (neighborX - targetX)**2 + (neighborY - targetY)**2;
                         // Invert distance to get a score (smaller distance -> higher score)
                        score = (GRID_WIDTH**2 + GRID_HEIGHT**2) - distSq; // Max possible distance squared as base
                    }

                    scores[i] = Math.max(0, score); // Scores must be non-negative
                    totalScore += scores[i];
                }
            }

             // Add exploration probability to all valid moves
            const baseExploreScore = MAX_PHEROMONE * RANDOM_MOVE_PROB_BASE / 8; // Distribute random chance
            for(let i = 0; i < 8; i++) {
                const { dx, dy } = directions[i];
                 const neighborX = this.gridX + dx;
                 const neighborY = this.gridY + dy;
                 if (neighborX >= 0 && neighborX < GRID_WIDTH && neighborY >= 0 && neighborY < GRID_HEIGHT) {
                     scores[i] += baseExploreScore;
                     totalScore += baseExploreScore;
                 }
            }


            // Choose direction probabilistically
            let rand = Math.random() * totalScore;
            let chosenDir = -1;
            for (let i = 0; i < 8; i++) {
                if (rand < scores[i]) {
                    chosenDir = i;
                    break;
                }
                rand -= scores[i];
            }

            // If a direction was chosen, set the next cell
            if (chosenDir !== -1) {
                const { dx, dy } = directions[chosenDir];
                nextCell.x = this.gridX + dx;
                nextCell.y = this.gridY + dy;
                // Update visual direction (optional, for drawing ant orientation)
                 this.direction = Math.atan2(dy, dx);
            } else {
                 // Fallback: if somehow no direction was chosen (shouldn't happen with baseExploreScore), stay put or random?
                 // Let's just stay put.
            }


            // Boundary check again after selection (should be covered by initial checks but good safeguard)
             if (nextCell.x < 0) nextCell.x = 0;
             if (nextCell.x >= GRID_WIDTH) nextCell.x = GRID_WIDTH - 1;
             if (nextCell.y < 0) nextCell.y = 0;
             if (nextCell.y >= GRID_HEIGHT) nextCell.y = GRID_HEIGHT - 1;


            return nextCell;
        }

        // Update ant's state and position in grid
        logicUpdate() {
            const nextCell = this.determineNextGridCell();

            // Update grid position
            this.gridX = nextCell.x;
            this.gridY = nextCell.y;

            // Set target pixel position for smooth drawing
            this.targetVisualX = this.gridX * GRID_SIZE + GRID_SIZE / 2;
            this.targetVisualY = this.gridY * GRID_SIZE + GRID_SIZE / 2;

            // Ant actions based on location
            if (this.state === 0 && this.gridX === FOOD_POS_GRID.x && this.gridY === FOOD_POS_GRID.y) {
                // Found food!
                this.state = 1; // Switch to returning
                this.carryingFood = true;
                this.color = '#ff6347'; // Change color when carrying food
                foodFoundCount++;
                foodFoundCountSpan.textContent = foodFoundCount;
                // Instant visual flip direction back (looks more gamey/reactive)
                 this.direction += Math.PI; // Roughly reverse visual direction
            } else if (this.state === 1 && this.gridX === NEST_POS_GRID.x && this.gridY === NEST_POS_GRID.y) {
                // Returned to nest
                this.state = 0; // Switch to searching
                this.carryingFood = false;
                this.color = '#333'; // Reset color
                // Deposit pheromone at nest (optional, but can reinforce trails near nest entrance)
                // pheromoneGrid[this.gridY][this.gridX] = Math.min(MAX_PHEROMONE, pheromoneGrid[this.gridY][this.gridX] + PHEROMONE_DEPOSIT_AMOUNT);
            }

            // If returning, deposit pheromone in the current cell
            if (this.state === 1) {
                 pheromoneGrid[this.gridY][this.gridX] = Math.min(MAX_PHEROMONE, pheromoneGrid[this.gridY][this.gridX] + PHEROMONE_DEPOSIT_AMOUNT);
            }
        }

        // Update visual position towards target
        visualUpdate() {
             const lerpFactor = 0.1; // How quickly to move towards the target (0 to 1)
             this.visualX += (this.targetVisualX - this.visualX) * lerpFactor;
             this.visualY += (this.targetVisualY - this.visualY) * lerpFactor;

             // Prevent floating point errors making it never reach exactly
             if (Math.abs(this.targetVisualX - this.visualX) < 0.1) this.visualX = this.targetVisualX;
             if (Math.abs(this.targetVisualY - this.visualY) < 0.1) this.visualY = this.targetVisualY;
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
             // Draw ant as a circle
            ctx.arc(this.visualX, this.visualY, GRID_SIZE * 0.3, 0, Math.PI * 2);
            ctx.fill();

             // Optional: Draw orientation line
             // ctx.strokeStyle = 'white';
             // ctx.lineWidth = 1;
             // ctx.beginPath();
             // ctx.moveTo(this.visualX, this.visualY);
             // ctx.lineTo(this.visualX + Math.cos(this.direction) * GRID_SIZE * 0.4, this.visualY + Math.sin(this.direction) * GRID_SIZE * 0.4);
             // ctx.stroke();
        }
    }

    // Initialize simulation grid and ants
    function initializeSimulation() {
        pheromoneGrid = Array(GRID_HEIGHT).fill(null).map(() => Array(GRID_WIDTH).fill(0));
        ants = [];
        for (let i = 0; i < numAnts; i++) {
            ants.push(new Ant(NEST_POS_GRID.x, NEST_POS_GRID.y));
        }
        foodFoundCount = 0;
        foodFoundCountSpan.textContent = foodFoundCount;

         // Ensure initial drawing state is correct
        draw();
    }

    // Draw everything
    function draw() {
        // Draw background (sand/ground color)
        ctx.fillStyle = '#e0d4b0'; // Light sandy color
        ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

        // Draw Pheromones (if visible)
        if (showPheromones) {
             for (let y = 0; y < GRID_HEIGHT; y++) {
                for (let x = 0; x < GRID_WIDTH; x++) {
                    const pheromoneValue = pheromoneGrid[y][x];
                    if (pheromoneValue > 0) {
                         const alpha = pheromoneValue / MAX_PHEROMONE;
                        // Use a warm, slightly translucent orange/yellow for pheromones
                         ctx.fillStyle = `rgba(255, 193, 7, ${alpha * 0.8})`; // Adjust alpha multiplier for intensity
                         ctx.fillRect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE);

                         // Optional: Draw center dot for pheromone origin visually
                         // ctx.fillStyle = `rgba(255, 165, 0, ${alpha})`;
                         // ctx.beginPath();
                         // ctx.arc(x * GRID_SIZE + GRID_SIZE / 2, y * GRID_SIZE + GRID_SIZE / 2, GRID_SIZE * 0.1, 0, Math.PI * 2);
                         // ctx.fill();
                    }
                }
            }
        }


        // Draw Nest (as a circle)
        ctx.fillStyle = '#8b4513'; // Brown color
        ctx.beginPath();
        ctx.arc(NEST_POS_GRID.x * GRID_SIZE + GRID_SIZE / 2, NEST_POS_GRID.y * GRID_SIZE + GRID_SIZE / 2, GRID_SIZE * 0.8, 0, Math.PI * 2);
        ctx.fill();
         ctx.strokeStyle = '#5a2d0c';
         ctx.lineWidth = 2;
         ctx.stroke();


        // Draw Food (as a square/rectangle)
        ctx.fillStyle = '#388e3c'; // Green color
        ctx.fillRect(FOOD_POS_GRID.x * GRID_SIZE, FOOD_POS_GRID.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);
        ctx.strokeStyle = '#1b5e20';
        ctx.lineWidth = 2;
        ctx.strokeRect(FOOD_POS_GRID.x * GRID_SIZE, FOOD_POS_GRID.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);


        // Draw Ants
        ants.forEach(ant => {
            // Update visual position before drawing
            ant.visualUpdate();
            ant.draw();
        });
    }

    // Update simulation state (logic)
    function logicUpdate() {
        // Update Pheromones (fade)
        for (let y = 0; y < GRID_HEIGHT; y++) {
            for (let x = 0; x < GRID_WIDTH; x++) {
                pheromoneGrid[y][x] = Math.max(0, pheromoneGrid[y][x] * pheromoneFadeRate - 0.1); // Fade and small constant decay
            }
        }

        // Update Ants (logic)
        ants.forEach(ant => ant.logicUpdate());
    }

    // Main simulation animation loop
    function gameLoop(currentTime) {
        if (!isSimulationRunning) {
             animationFrameId = null; // Stop the loop if simulation is stopped
             return;
        }

        // Perform logic updates based on speed slider
        if (currentTime - lastLogicTime > logicInterval) {
            logicUpdate();
            lastLogicTime = currentTime;
        }

        // Always draw for smooth animation
        draw();

        animationFrameId = requestAnimationFrame(gameLoop);
    }

    // Control functions
    function startSimulation() {
        if (!isSimulationRunning) {
             isSimulationRunning = true;
             lastLogicTime = performance.now(); // Initialize time for the first logic update
             animationFrameId = requestAnimationFrame(gameLoop); // Start the animation loop
            startButton.disabled = true;
            stopButton.disabled = false;
        }
    }

    function stopSimulation() {
        if (isSimulationRunning) {
             isSimulationRunning = false;
            // The gameLoop itself will stop when isSimulationRunning is false
            startButton.disabled = false;
            stopButton.disabled = true;
        }
    }

    function resetSimulation() {
        stopSimulation(); // Ensure simulation is stopped first
        initializeSimulation();
         // No need to call draw() here, initializeSimulation calls it
        startButton.disabled = false;
        stopButton.disabled = true;
    }

    // Event Listeners
    startButton.addEventListener('click', startSimulation);
    stopButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);

    numAntsSlider.addEventListener('input', (event) => {
        numAnts = parseInt(event.target.value);
        numAntsValue.textContent = numAnts;
        // Only reset if simulation is not running, or maybe always reset for immediate effect?
        // Let's reset for immediate effect on ant count
         resetSimulation();
    });

     simulationSpeedSlider.addEventListener('input', (event) => {
         const speedFactor = parseInt(event.target.value);
         simulationSpeedValue.textContent = `x${speedFactor}`;
         // Adjust the logic update interval
         // Speed 1: 10 updates/sec (100ms interval)
         // Speed 10: 100 updates/sec (10ms interval)
         logicInterval = 1000 / (speedFactor * 10); // Max 100 updates/sec

         // Adjust pheromone fade rate based on speed to maintain visual consistency
         // At higher speeds, pheromone needs to fade more per logic step
         pheromoneFadeRate = 1 - (1 - 0.99) * (speedFactor / 5); // Scale original fade rate (0.99 at speed 5)
         pheromoneFadeRate = Math.max(0.95, Math.min(0.995, pheromoneFadeRate)); // Clamp values
     });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none';
        explanationContent.style.display = isHidden ? 'block' : 'none';
         toggleExplanationButton.textContent = isHidden ?
            'הסבר מדעי: הצצה עמוקה לעולם הפרומונים (הסתר)' :
            'הסבר מדעי: הצצה עמוקה לעולם הפרומונים';
    });

     showPheromonesCheckbox.addEventListener('change', (event) => {
         showPheromones = event.target.checked;
         // Redraw immediately to update visibility
         draw();
     });


    // Initial setup
    initializeSimulation();
    // Initial draw is done by initializeSimulation
});
</script>

<style>
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #f4f4f4;
    }

    h1, h2, h3 {
        color: #333;
        font-weight: bold;
    }

    h1 {
        text-align: center;
        color: #1a4d2e; /* Dark green */
        margin-bottom: 30px;
    }

     p {
         margin-bottom: 1em;
     }

    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px auto;
        border: 1px solid #ccc;
        padding: 20px;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        max-width: 740px; /* Match canvas width + padding */
    }

    canvas {
        border: 2px solid #5a2d0c; /* Brown border to match nest */
        background-color: #e0d4b0; /* Light sandy color */
        display: block;
        margin-bottom: 20px;
        border-radius: 8px;
    }

    .controls-panel {
        display: flex;
        flex-wrap: wrap;
        gap: 15px; /* Increased gap */
        justify-content: center;
        align-items: center;
        width: 100%;
        padding-top: 10px;
         border-top: 1px solid #eee;
    }

    .control-group {
        display: flex;
        align-items: center;
        gap: 8px;
         flex-wrap: wrap; /* Allow wrapping within groups if needed */
    }

     .slider-group {
         flex-grow: 1; /* Allow sliders to take more space */
         min-width: 250px; /* Ensure sliders have minimum width */
     }

     .info-group {
         gap: 20px; /* Larger gap for info items */
     }

    .control-button {
        padding: 10px 18px; /* Increased padding */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded corners */
        font-size: 1rem;
        font-weight: bold;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .start-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }

     .stop-button {
        background-color: #f44336; /* Red */
        color: white;
    }

     .reset-button {
        background-color: #ff9800; /* Orange */
        color: white;
    }

    .control-button:hover:not(:disabled) {
        opacity: 0.9;
         transform: translateY(-1px);
    }

     .control-button:active:not(:disabled) {
         transform: translateY(0);
     }


    .control-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.6;
    }

    .controls-panel label {
        font-weight: normal; /* Less bold */
        color: #555;
         white-space: nowrap; /* Prevent wrapping */
         font-size: 0.95rem;
    }

    .controls-panel input[type="range"] {
        flex-grow: 1; /* Allow slider to take available space */
         -webkit-appearance: none; /* Override default browser styling */
         appearance: none;
         height: 8px;
         background: #ddd;
         outline: none;
         opacity: 0.7;
         transition: opacity .2s;
         border-radius: 4px;
    }

     .controls-panel input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 18px;
         height: 18px;
         background: #4CAF50;
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #fff;
         box-shadow: 0 1px 3px rgba(0,0,0,0.4);
     }

     .controls-panel input[type="range"]::-moz-range-thumb {
        width: 18px;
         height: 18px;
         background: #4CAF50;
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #fff;
         box-shadow: 0 1px 3px rgba(0,0,0,0.4);
     }


    .slider-value {
        font-weight: bold;
        color: #007bff; /* Blue */
        min-width: 30px; /* Reserve space */
        text-align: center;
    }


    .info-value {
        font-weight: bold;
        color: #007bff; /* Blue */
    }

     #showPheromonesCheckbox {
         width: 18px;
         height: 18px;
         cursor: pointer;
         vertical-align: middle; /* Align checkbox better with label */
     }

    .toggle-explanation {
        display: block;
        margin: 30px auto 20px auto; /* Adjust margin */
        padding: 12px 25px; /* Increased padding */
        cursor: pointer;
        border: 1px solid #007bff;
        border-radius: 25px; /* Pill shape */
        background-color: #007bff;
        color: white;
        font-size: 1rem;
        font-weight: bold;
        text-align: center;
        width: fit-content;
        transition: background-color 0.2s ease, border-color 0.2s ease;
    }

    .toggle-explanation:hover {
        background-color: #0056b3;
        border-color: #004085;
    }


    .explanation-content {
        margin: 20px auto;
        padding: 20px; /* Increased padding */
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #fefefe;
        max-width: 800px; /* Limit width for readability */
        line-height: 1.7; /* Increased line height */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .explanation-content h2 {
        color: #1a4d2e; /* Dark green */
        border-bottom: 2px solid #4CAF50; /* Green bottom border */
        padding-bottom: 8px;
        margin-top: 15px;
        margin-bottom: 15px;
    }

     .explanation-content h3 {
        color: #5a2d0c; /* Brown */
        border-bottom: 1px dashed #ccc; /* Dashed border */
        padding-bottom: 5px;
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }

    .explanation-content ul {
        margin-bottom: 15px;
        padding-left: 25px; /* Indent list */
    }

    .explanation-content li {
        margin-bottom: 8px; /* Space out list items */
    }

     /* Responsive adjustments */
    @media (max-width: 768px) {
        body {
            padding: 10px;
        }
        .simulation-container {
            width: 98%;
            padding: 10px;
            border-radius: 8px;
        }
         canvas {
            width: 100%;
            height: auto; /* Maintain aspect ratio */
            margin-bottom: 15px;
            border-radius: 4px;
        }
        .controls-panel {
            flex-direction: column;
            align-items: stretch;
            gap: 10px;
        }
         .control-group {
             flex-direction: column;
             align-items: stretch;
             gap: 5px;
             width: 100%;
         }

         .control-button,
         .controls-panel label,
         .controls-panel input[type="range"],
         .info-group div {
             width: 100%;
             margin-left: 0;
             box-sizing: border-box; /* Include padding/border in element's total width */
         }

         .info-group {
             flex-direction: row; /* Keep info group inline if space allows */
             justify-content: space-around;
         }

         .info-group div {
             width: auto; /* Allow info items to take minimal space */
             text-align: center;
         }

         .slider-group label {
             text-align: center;
         }

         .toggle-explanation {
             margin: 20px auto 15px auto;
             padding: 10px 20px;
             font-size: 0.9rem;
         }

         .explanation-content {
             width: 98%;
             padding: 15px;
         }

         .explanation-content h2 {
             font-size: 1.3rem;
         }
          .explanation-content h3 {
             font-size: 1.1rem;
         }
    }
</style>
```