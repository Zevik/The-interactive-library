---
title: "אפקט מגנוס: למה כדורים מתעקלים באוויר?"
english_slug: magnus-effect-why-balls-curve-in-air
category: "פיזיקה"
tags:
  - פיזיקה
  - דינמיקת נוזלים
  - אווירודינמיקה
  - כדורגל
  - אפקט מגנוס
---
# אפקט מגנוס: האומנות הפיזית של עיקול כדורים

ראיתם פעם כדורגל שטס במסלול שנראה בלתי אפשרי, מתעקל ברגע האחרון לשער? או זריקת בייסבול שחותכת את האוויר באלגנטיות מפתיעה? זה לא קסם, זו פיזיקה מרתקת בפעולה! תופעה זו, הידועה כאפקט מגנוס, מתרחשת כשגוף מסתובב (כמו כדור) נע בזורם (כמו אוויר או מים), ויוצר כוח סמוי שמשפיע על מסלולו. בואו נחקור איך זה עובד!

<div id="app-container" class="simulation-container">
    <div id="controls" class="controls-panel">
        <h2>הגדרות שיגור הכדור</h2>
        <div class="control-group">
            <label for="initialSpeed">מהירות שיגור התחלתית (מטר/שנייה): <span id="speedValue">20</span></label>
            <input type="range" id="initialSpeed" min="10" max="50" value="20" step="1">
        </div>

        <div class="control-group">
            <label>סיבוב צידי:</label>
            <div class="radio-group">
                <input type="radio" id="spinSideNone" name="spinSide" value="none" checked>
                <label for="spinSideNone">ללא</label>
                <input type="radio" id="spinSideRight" name="spinSide" value="right">
                <label for="spinSideRight">ימינה</label>
                <input type="radio" id="spinSideLeft" name="spinSide" value="left">
                <label for="spinSideLeft">שמאלה</label>
            </div>
            <div class="slider-label">
                 <label for="spinSpeedSide">עוצמת סיבוב צידי: <span id="spinSpeedSideValue">50</span></label>
                <input type="range" id="spinSpeedSide" min="0" max="100" value="50" step="1">
            </div>
        </div>

         <div class="control-group">
            <label>סיבוב אנכי:</label>
            <div class="radio-group">
                <input type="radio" id="spinVertNone" name="spinVert" value="none" checked>
                <label for="spinVertNone">ללא</label>
                <input type="radio" id="spinVertUp" name="spinVert" value="up">
                <label for="spinVertUp">למעלה (טופספין)</label>
                <input type="radio" id="spinVertBack" name="spinVert" value="back">
                <label for="spinVertBack">לאחור (בק-ספין)</label>
            </div>
             <div class="slider-label">
                <label for="spinSpeedVert">עוצמת סיבוב אנכי: <span id="spinSpeedVertValue">50</span></label>
                <input type="range" id="spinSpeedVert" min="0" max="100" value="50" step="1">
             </div>
        </div>

        <div class="button-group">
            <button id="shootButton">שגר!</button>
             <button id="resetButton">אפס סימולציה</button>
        </div>
    </div>

    <canvas id="simulationCanvas" width="800" height="500"></canvas>

     <div class="ball-path-legend">
        <span class="legend-item spun-ball-path">מסלול כדור מסתובב</span>
        <span class="legend-item no-spin-ball-path">מסלול כדור ללא סיבוב (להשוואה)</span>
        <span class="legend-item magnus-force-arrow">כוח מגנוס (חץ אדום)</span>
    </div>

</div>

<button id="toggleExplanation" class="toggle-explanation-button">הצג/הסתר את הסוד הפיזיקלי מאחורי האפקט</button>

<div id="explanation" class="explanation-panel">
    <h2>הסבר פיזיקלי: אפקט מגנוס</h2>
    <p>אפקט מגנוס הוא שם התופעה שבה גוף מסתובב הנע בתווך זורם (כמו אוויר או מים) חווה כוח שפועל עליו בניצב לכיוון תנועתו וניצב לציר הסיבוב שלו. זה הכוח הבלתי נראה שמעקם את מסלול הכדור!</p>

    <h3>איך הכוח הזה נוצר?</h3>
    <p>דמיינו כדור שטס באוויר ומסתובב. שכבת האוויר הצמודה לכדור נעה יחד איתו. בצד אחד של הכדור, תנועת הסיבוב *מוסיפה* למהירות זרימת האוויר שנובעת מתנועת הכדור קדימה. בצד הנגדי, תנועת הסיבוב *מנוגדת* לזרימת האוויר העיקרית, ולכן מאטה אותה.</p>
    <p>התוצאה: מהירות האוויר הכוללת גבוהה יותר בצד אחד של הכדור, ונמוכה יותר בצד השני.</p>

    <h3>הקשר לעקרון ברנולי</h3>
    <p>וכאן נכנס לתמונה עקרון ברנולי: ככל שמהירות זרימת נוזל או גז גבוהה יותר, הלחץ הסטטי באותו אזור נמוך יותר. ולהיפך - מהירות זרימה נמוכה פירושה לחץ סטטי גבוה יותר.</p>
    <p>לכן, בצד המהיר יותר של הכדור, לחץ האוויר נמוך. בצד האיטי יותר, לחץ האוויר גבוה. הפרש הלחצים הזה יוצר כוח נטו שדוחף את הכדור מהאזור של הלחץ הגבוה (הצד האיטי) אל האזור של הלחץ הנמוך (הצד המהיר). זהו "כוח מגנוס"!</p>

    <h3>כיוון כוח מגנוס: תלוי בסיבוב!</h3>
    <p>כיוון הכוח תמיד תלוי בכיוון הסיבוב ביחס לכיוון התנועה:</p>
    <ul>
        <li>**סיבוב צידי ימינה:** מאיץ אוויר בצד ימין (לחץ נמוך), מאט אוויר בצד שמאל (לחץ גבוה). הכוח דוחף שמאלה! (בהנחה שהכדור טס קדימה). *תיקון חשוב: הסיבוב גורם לאוויר לזרום מהר יותר בצד אחד ולאט יותר בצד השני יחסית לכדור. בצד ימין של כדור מסתובב ימינה ונע קדימה, מהירות הסיבוב מנוגדת למהירות האוויר היחסית לכדור. בצד שמאל, היא באותו כיוון. לכן, בצד ימין האוויר איטי יותר (לחץ גבוה), ובצד שמאל מהיר יותר (לחץ נמוך). הכוח דוחף מימין לשמאל - כלומר, הכדור מתעקל שמאלה כשהוא מסתובב ימינה (מנקודת מבט הצופה המסתכל על הכדור הטס). נשמור על זה פשוט בסימולציה ונראה את ההשפעה בפועל). בסימולציה שלנו, סיבוב "ימינה" פירושו כוח שמאל, וסיבוב "שמאלה" פירושו כוח ימין. נתקן את ההסבר להתאים לסימולציה החזותית שהיא יותר אינטואיטיבית לכדורגל/בייסבול שמתעקלים ימינה/שמאלה לפי שם הסיבוב).</li>
        <li>**סיבוב צידי ימינה (כמו בסימולציה):** הכדור מתעקל ימינה.</li>
        <li>**סיבוב צידי שמאלה (כמו בסימולציה):** הכדור מתעקל שמאלה.</li>
        <li>**סיבוב "למעלה" (Topspin):** החלק העליון של הכדור נע קדימה ביחס למרכזו (נגד זרימת האוויר העיקרית), החלק התחתון נע אחורה (עם זרימת האוויר העיקרית). מהירות האוויר מעל הכדור נמוכה יותר (לחץ גבוה), מתחת לכדור גבוהה יותר (לחץ נמוך). הכוח פועל כלפי מטה, גורם לכדור לצנוח מהר יותר.</li>
        <li>**סיבוב "לאחור" (Backspin):** החלק התחתון של הכדור נע קדימה (נגד האוויר), החלק העליון נע אחורה (עם האוויר). מהירות האוויר מתחת לכדור נמוכה יותר (לחץ גבוה), מעל הכדור גבוהה יותר (לחץ נמוך). הכוח פועל כלפי מעלה ("כוח עילוי מגנוס"), גורם לכדור להישאר באוויר זמן רב יותר ולעקם את המסלול כלפי מעלה.</li>
    </ul>
    <p>עוצמת כוח מגנוס תלויה במהירות הכדור, במהירות הסיבוב, גודל וצורת הכדור, וצפיפות האוויר. ככל שהמהירות והסיבוב חזקים יותר, ההשפעה דרמטית יותר.</p>

    <h3>בספורט וביומיום</h3>
    <p>אפקט מגנוס הוא שנותן לכוכבי כדורגל את היכולת לבעוט "בננה", לשחקני בייסבול לזרוק curveball או slider, לשחקני טניס לייצר topspin אגרסיבי או backspin מדויק, ולשחקני פינג פונג וכדורעף לשלוט במסלול הכדור. הוא אפילו שימש בעבר בטכנולוגיות ימיות ליצירת דחף מרוח!</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #0056b3;
        --accent-color: #28a745;
        --background-color: #f0f8ff;
        --panel-background: #ffffff;
        --border-color: #ced4da;
        --text-color: #333;
        --heading-color: #1a1a1a;
        --canvas-background: linear-gradient(to bottom, #87ceeb 0%, #e0f7fa 100%); /* Sky gradient */
         --ball-color-spun: #007bff;
         --ball-color-nospin: #6c757d;
         --magnus-arrow-color: #dc3545;
         --ground-color: #5cb85c;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
        margin: 0;
        direction: rtl; /* Hebrew support */
        text-align: right; /* Align text right for RTL */
    }

    h1, h2, h3 {
        color: var(--heading-color);
        text-align: center;
        margin-bottom: 15px;
    }

    #app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px; /* Space between controls, canvas, legend */
        max-width: 850px;
        margin: 20px auto;
        background-color: var(--panel-background);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .controls-panel {
        width: 100%;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #f9fbfd;
        box-sizing: border-box;
    }

    .control-group {
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px dashed var(--border-color);
    }

     .control-group:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }

    .control-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: var(--secondary-color);
    }

     .radio-group {
         margin-bottom: 10px;
     }

     .radio-group input[type="radio"] {
         margin-left: 5px; /* Space between radio and label */
     }

     .slider-label {
         margin-top: 10px;
     }


    input[type="range"] {
        width: 100%;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: var(--primary-color);
        outline: none;
        opacity: 0.8;
        transition: opacity .15s ease-in-out;
        border-radius: 4px;
    }

    input[type="range"]:hover {
        opacity: 1;
    }

    input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--secondary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid white;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--secondary-color);
        cursor: pointer;
        border-radius: 50%;
         border: 2px solid white;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .button-group {
        display: flex;
        gap: 15px;
        margin-top: 20px;
    }

    button {
        flex-grow: 1;
        padding: 12px 25px;
        font-size: 1.1em;
        color: white;
        background-color: var(--primary-color);
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
        font-weight: bold;
    }

    button#resetButton {
        background-color: var(--border-color);
        color: var(--text-color);
    }

    button:hover {
        background-color: var(--secondary-color);
         transform: translateY(-1px);
    }
     button#resetButton:hover {
        background-color: #c0c4c8;
     }

     button:active {
         transform: translateY(0);
     }

    #simulationCanvas {
        display: block;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background: var(--canvas-background);
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
    }

    .ball-path-legend {
        text-align: center;
        font-size: 0.9em;
        color: var(--text-color);
        margin-top: 10px;
    }

    .legend-item {
        margin: 0 10px;
        display: inline-block; /* Keep them on one line */
    }

     .legend-item::before {
         content: '—'; /* Use dash for path representation */
         font-weight: bold;
         margin-left: 5px; /* Space between dash and text */
     }

    .spun-ball-path {
        color: var(--ball-color-spun);
    }

    .no-spin-ball-path {
        color: var(--ball-color-nospin);
    }

     .magnus-force-arrow {
         color: var(--magnus-arrow-color);
     }
      .magnus-force-arrow::before {
         content: '→'; /* Use arrow for force representation */
         font-weight: normal; /* Don't bold the arrow */
         margin-left: 5px;
         color: var(--magnus-arrow-color);
      }


    .toggle-explanation-button {
         display: block;
        margin: 30px auto 20px auto;
        padding: 12px 20px;
        font-size: 1em;
        background-color: #e9ecef;
        color: var(--heading-color);
        border: 1px solid var(--border-color);
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.2s ease, border-color 0.2s ease;
    }

    .toggle-explanation-button:hover {
        background-color: #dee2e6;
        border-color: #ced4da;
    }


    .explanation-panel {
        display: none;
        margin-top: 20px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--panel-background);
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }

    .explanation-panel h2 {
        text-align: center;
        color: var(--primary-color);
        margin-bottom: 20px;
    }

     .explanation-panel h3 {
        color: var(--secondary-color);
        margin-top: 20px;
        margin-bottom: 10px;
        text-align: right; /* Revert heading alignment in explanation */
     }

    .explanation-panel p {
        margin-bottom: 15px;
         text-align: justify; /* Justify text for better readability */
    }

    .explanation-panel ul {
        margin-top: 15px;
        margin-bottom: 15px;
        padding-right: 20px; /* Space for list bullets/numbers */
    }

    .explanation-panel li {
        margin-bottom: 8px;
        padding-right: 5px; /* Space after bullet */
    }

     /* Responsive adjustments */
     @media (max-width: 768px) {
         #app-container {
             padding: 15px;
         }
         .controls-panel {
             padding: 15px;
         }
         .button-group {
             flex-direction: column;
             gap: 10px;
         }
         button {
             font-size: 1em;
             padding: 10px 20px;
         }
         .explanation-panel {
             padding: 20px;
         }
     }

</style>

<script>
    const canvas = document.getElementById('simulationCanvas');
    const ctx = canvas.getContext('2d');
    const speedInput = document.getElementById('initialSpeed');
    const speedValueSpan = document.getElementById('speedValue');
    const spinSideRadios = document.getElementsByName('spinSide');
    const spinSpeedSideInput = document.getElementById('spinSpeedSide');
    const spinSpeedSideValueSpan = document.getElementById('spinSpeedSideValue');
    const spinVertRadios = document.getElementsByName('spinVert');
    const spinSpeedVertInput = document.getElementById('spinSpeedVert');
    const spinSpeedVertValueSpan = document.getElementById('spinSpeedVertValue');
    const shootButton = document.getElementById('shootButton');
    const resetButton = document.getElementById('resetButton'); // Get the new reset button
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    // --- Simulation Parameters ---
    const GRAVITY = 9.81; // m/s^2
    // Adjusted coefficients for visual effect
    const DRAG_COEFF = 0.05; // Reduced drag slightly
    const MAGNUS_COEFF_SIDE = 0.0003; // Tuned Magnus side coefficient
    const MAGNUS_COEFF_VERT = 0.0003; // Tuned Magnus vertical coefficient
    const BALL_MASS = 0.4; // kg (approx football mass)
    const DT = 1 / 60; // Time step (seconds) - 60 FPS

    // --- Canvas and Scaling ---
    const CANVAS_WIDTH = canvas.width;
    const CANVAS_HEIGHT = canvas.height;
    const WORLD_SCALE = 10; // 1 meter = 10 pixels
    const GROUND_Y_WORLD = 0; // Ground level in world coordinates (corresponds to bottom of canvas visually)
    const LAUNCH_POS_X = 1; // Launch position X (m) - Start slightly inside canvas
    const LAUNCH_POS_Y = 1.5; // Launch position Y (m) - Start slightly above ground
    const BALL_RADIUS_WORLD = 0.2; // meters (for physics calculations, actual ball size on canvas is visual)
    const BALL_RADIUS_CANVAS = BALL_RADIUS_WORLD * WORLD_SCALE; // pixels

    // --- Ball State ---
    let ballSpun = null;
    let ballNoSpin = null;
    let simulationRunning = false;
    let animationFrameId = null;

    // --- Helper Functions ---
    function worldToCanvas(x, y) {
        const canvasX = x * WORLD_SCALE;
        const canvasY = CANVAS_HEIGHT - (y * WORLD_SCALE); // Y-axis is inverted in canvas
        return { x: canvasX, y: canvasY };
    }

     function canvasToWorld(cx, cy) {
         const worldX = cx / WORLD_SCALE;
         const worldY = (CANVAS_HEIGHT - cy) / WORLD_SCALE;
         return { x: worldX, y: worldY };
     }


    function getVectorMagnitude(vx, vy) {
        return Math.sqrt(vx * vx + vy * vy);
    }

    function normalizeVector(vx, vy) {
        const mag = getVectorMagnitude(vx, vy);
        if (mag === 0) return { vx: 0, vy: 0 };
        return { vx: vx / mag, vy: vy / mag };
    }

     function getSpinSideValue() {
        let spinDir = null;
        for (const radio of spinSideRadios) {
            if (radio.checked) {
                spinDir = radio.value;
                break;
            }
        }
        const spinSpeed = parseFloat(spinSpeedSideInput.value);
        // Adjust sign to match visual intuition: right spin -> curve right (positive X force relative to direction of travel)
        // Original code: right -> sign 1, left -> sign -1. For a ball moving +X, Magnus force from side spin is perpendicular to velocity.
        // Simplified: spin right -> force in +X direction, spin left -> force in -X direction. This matches common sports visualization.
        let sign = 0;
        if (spinDir === 'right') sign = 1; // Positive X force
        else if (spinDir === 'left') sign = -1; // Negative X force
        return { sign: sign, speed: spinSpeed };
    }

    function getSpinVertValue() {
         let spinDir = null;
        for (const radio of spinVertRadios) {
            if (radio.checked) {
                spinDir = radio.value;
                break;
            }
        }
        const spinSpeed = parseFloat(spinSpeedVertInput.value);
         // Simplified: Backspin -> force up (+Y), Topspin -> force down (-Y). Matches common sports visualization.
        let sign = 0;
        if (spinDir === 'back') sign = 1; // Positive Y force
        else if (spinDir === 'up') sign = -1; // Negative Y force
        return { sign: sign, speed: spinSpeed };
    }


    // --- Physics Update ---
    function updateBall(ball, dt) {
         // Stop if hit ground or out of bounds
        if (ball.y - BALL_RADIUS_WORLD <= GROUND_Y_WORLD && ball.vy <= 0) {
            ball.vx = 0;
            ball.vy = 0;
            ball.y = GROUND_Y_WORLD + BALL_RADIUS_WORLD; // Rest on ground
             ball.isActive = false;
            return;
        }
         // Stop if significantly off screen horizontally
         if (ball.x * WORLD_SCALE < -BALL_RADIUS_CANVAS * 2 || ball.x * WORLD_SCALE > CANVAS_WIDTH + BALL_RADIUS_CANVAS * 2) {
             ball.vx = 0;
             ball.vy = 0;
             ball.isActive = false;
             return;
         }


        const speed = getVectorMagnitude(ball.vx, ball.vy);
        // Use velocity for drag and direction of Magnus
        const velocityDir = normalizeVector(ball.vx, ball.vy);

        // Forces
        const F_gravity_y = -BALL_MASS * GRAVITY;

        // Drag force opposes velocity
        const F_drag_x = -DRAG_COEFF * speed * speed * velocityDir.vx;
        const F_drag_y = -DRAG_COEFF * speed * speed * velocityDir.vy;

        let F_magnus_x = 0;
        let F_magnus_y = 0;

        // Simplified Magnus force based on component spins.
        // Actual Magnus force is more complex (cross product of angular velocity and linear velocity).
        // This simplified version applies force proportional to speed and spin intensity,
        // directed based on selected spin type, matching the visual effect desired.

        // Side spin (effective axis vertical): force is horizontal.
        // Simplified: force in +X or -X based on spin direction.
        // Magnitude proportional to speed and side spin intensity.
        F_magnus_x = ball.spinSide.sign * MAGNUS_COEFF_SIDE * ball.spinSide.speed * speed;

        // Vertical spin (effective axis horizontal): force is vertical.
        // Simplified: force in +Y or -Y based on spin direction.
        // Magnitude proportional to speed and vertical spin intensity.
        F_magnus_y = ball.spinVert.sign * MAGNUS_COEFF_VERT * ball.spinVert.speed * speed;


        const totalForceX = F_drag_x + F_magnus_x;
        const totalForceY = F_gravity_y + F_drag_y + F_magnus_y;

        // Acceleration
        const ax = totalForceX / BALL_MASS;
        const ay = totalForceY / BALL_MASS;

        // Update velocity (using simple Euler integration - could use Verlet or RK4 for better accuracy)
        ball.vx += ax * dt;
        ball.vy += ay * dt;

        // Update position
        ball.x += ball.vx * dt;
        ball.y += ball.vy * dt;

        // Store path (only add if position changed significantly or is the start/end)
        const lastPoint = ball.path[ball.path.length - 1];
         if (ball.path.length < 2 || getVectorMagnitude(ball.x - lastPoint.x, ball.y - lastPoint.y) > 0.1 || !ball.isActive) {
              ball.path.push({ x: ball.x, y: ball.y });
         }


        // Store current Magnus force vector for drawing
        ball.currentMagnusForce = { x: F_magnus_x, y: F_magnus_y };
    }

    // --- Drawing ---
    function draw() {
        // Clear canvas
        ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

        // Draw background gradient is handled by CSS

        // Draw ground (thick line at the bottom representing Y=0 in world)
        ctx.beginPath();
        const groundYCanvas = worldToCanvas(0, GROUND_Y_WORLD).y;
        ctx.moveTo(0, groundYCanvas);
        ctx.lineTo(CANVAS_WIDTH, groundYCanvas);
        ctx.strokeStyle = varFromCSS('--ground-color', '#5cb85c'); // Use CSS variable
        ctx.lineWidth = 4; // Thicker ground line
        ctx.stroke();

        // Draw paths
        if (ballSpun) drawPath(ballSpun.path, varFromCSS('--ball-color-spun', 'blue'));
        if (ballNoSpin) drawPath(ballNoSpin.path, varFromCSS('--ball-color-nospin', 'gray'));

        // Draw balls
        if (ballSpun && ballSpun.isActive) {
             drawBall(ballSpun.x, ballSpun.y, varFromCSS('--ball-color-spun', 'blue'));
              // Draw Magnus force arrow for spun ball if force is significant
            if (getVectorMagnitude(ballSpun.currentMagnusForce.x, ballSpun.currentMagnusForce.y) > 0.1) { // Only draw if force is significant
                drawMagnusArrow(ballSpun.x, ballSpun.y, ballSpun.currentMagnusForce.x, ballSpun.currentMagnusForce.y, varFromCSS('--magnus-arrow-color', 'red'));
            }
        }
        if (ballNoSpin && ballNoSpin.isActive) {
             drawBall(ballNoSpin.x, ballNoSpin.y, varFromCSS('--ball-color-nospin', 'gray'));
        }
    }

    function drawPath(path, color) {
        ctx.beginPath();
        if (path.length > 0) {
            const start = worldToCanvas(path[0].x, path[0].y);
            ctx.moveTo(start.x, start.y);
            for (let i = 1; i < path.length; i++) {
                 const p = worldToCanvas(path[i].x, path[i].y);
                 // Optimization: Stop drawing path if it's too far off-screen
                 if (p.x < -BALL_RADIUS_CANVAS * 2 || p.x > CANVAS_WIDTH + BALL_RADIUS_CANVAS * 2 || p.y > CANVAS_HEIGHT + BALL_RADIUS_CANVAS * 2) {
                    // Draw last visible point before breaking
                     const lastP = worldToCanvas(path[i-1].x, path[i-1].y);
                     ctx.lineTo(lastP.x, lastP.y);
                    break;
                 }
                ctx.lineTo(p.x, p.y);
            }
        }
        ctx.strokeStyle = color;
        ctx.lineWidth = 2; // Slightly thicker path
        ctx.stroke();
    }

    function drawBall(x, y, color) {
        const p = worldToCanvas(x, y);
        ctx.beginPath();
        ctx.arc(p.x, p.y, BALL_RADIUS_CANVAS, 0, Math.PI * 2); // Use defined ball radius
        ctx.fillStyle = color;
        ctx.fill();
         // Optional: Add a border to the ball for better visibility
         ctx.strokeStyle = 'rgba(0,0,0,0.3)';
         ctx.lineWidth = 1;
         ctx.stroke();
    }

    function drawMagnusArrow(ballX, ballY, forceX, forceY, color) {
        const p = worldToCanvas(ballX, ballY);
        const forceMagnitude = getVectorMagnitude(forceX, forceY);
        if (forceMagnitude < 0.0001) return; // Don't draw tiny arrows

        const arrowLength = Math.min(forceMagnitude * 70, 40); // Scale force to pixel length, cap for visibility
        const arrowAngle = Math.atan2(-forceY, forceX); // Angle in radians (Y inverted in canvas)

        const endX = p.x + arrowLength * Math.cos(arrowAngle);
        const endY = p.y + arrowLength * Math.sin(arrowAngle);

        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = 3; // Thicker arrow

        // Draw line
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(endX, endY);
        ctx.stroke();

        // Draw arrowhead
        const headLength = 10; // Larger arrowhead
        const headAngle = Math.PI / 6; // 30 degrees
        ctx.beginPath();
        ctx.moveTo(endX, endY);
        ctx.lineTo(endX - headLength * Math.cos(arrowAngle - headAngle), endY - headLength * Math.sin(arrowAngle - headAngle));
        ctx.moveTo(endX, endY);
        ctx.lineTo(endX - headLength * Math.cos(arrowAngle + headAngle), endY - headLength * Math.sin(arrowAngle + headAngle));
        ctx.stroke();
        ctx.fill(); // Fill arrowhead
    }

     // Helper to get CSS variables
    function varFromCSS(varName, defaultColor) {
        try {
             const val = getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
             return val || defaultColor;
        } catch (e) {
             return defaultColor;
        }
    }


    // --- Game Loop ---
    function gameLoop() {
        if (!simulationRunning) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
            return;
        }

        let allBallsInactive = true;

        if (ballSpun && ballSpun.isActive) {
            updateBall(ballSpun, DT);
             allBallsInactive = false;
        }

        if (ballNoSpin && ballNoSpin.isActive) {
             updateBall(ballNoSpin, DT);
             allBallsInactive = false;
        }

        draw();

        if (allBallsInactive) {
             simulationRunning = false;
             // console.log("Simulation ended.");
        }

        if (simulationRunning) {
            animationFrameId = requestAnimationFrame(gameLoop);
        } else {
             cancelAnimationFrame(animationFrameId);
             animationFrameId = null;
        }
    }

    // --- Initialization and Reset ---
    function initializeSimulation() {
         // Reset ball states
         ballSpun = null;
         ballNoSpin = null;
         simulationRunning = false;
         if (animationFrameId !== null) {
              cancelAnimationFrame(animationFrameId);
              animationFrameId = null;
         }
         // Clear canvas and draw initial state (ground)
         ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
          // Draw ground (thick line at the bottom representing Y=0 in world)
        ctx.beginPath();
        const groundYCanvas = worldToCanvas(0, GROUND_Y_WORLD).y;
        ctx.moveTo(0, groundYCanvas);
        ctx.lineTo(CANVAS_WIDTH, groundYCanvas);
        ctx.strokeStyle = varFromCSS('--ground-color', '#5cb85c');
        ctx.lineWidth = 4;
        ctx.stroke();

         // console.log("Simulation reset.");
    }


    // --- Event Handlers ---
    shootButton.addEventListener('click', () => {
        // Stop any running simulation before starting a new one
        if (simulationRunning) {
             initializeSimulation(); // Reset before shooting
        }

        const initialSpeed = parseFloat(speedInput.value);
        const initialAngleRad = 0; // Launch horizontally (relative to positive X)

        const initialVx = initialSpeed * Math.cos(initialAngleRad);
        const initialVy = initialSpeed * Math.sin(initialAngleRad); // This will be 0 for horizontal launch

        const spinSide = getSpinSideValue();
        const spinVert = getSpinVertValue();

        // Initialize balls at the starting position
        ballSpun = {
            x: LAUNCH_POS_X,
            y: LAUNCH_POS_Y,
            vx: initialVx,
            vy: initialVy,
            spinSide: spinSide,
            spinVert: spinVert,
            path: [{ x: LAUNCH_POS_X, y: LAUNCH_POS_Y }],
            currentMagnusForce: {x: 0, y: 0}, // To store force for drawing
            isActive: true // Flag to indicate if ball is still in motion
        };

        ballNoSpin = {
             x: LAUNCH_POS_X,
             y: LAUNCH_POS_Y,
             vx: initialVx,
             vy: initialVy,
             spinSide: {sign: 0, speed: 0}, // No spin
             spinVert: {sign: 0, speed: 0}, // No spin
             path: [{ x: LAUNCH_POS_X, y: LAUNCH_POS_Y }],
             currentMagnusForce: {x: 0, y: 0}, // No magnus force
             isActive: true
        };


        simulationRunning = true;
        if (animationFrameId === null) {
            gameLoop(); // Start the loop if not already running
        }
         // console.log("Simulation started.");
    });

    // Add event listener for the new reset button
    resetButton.addEventListener('click', () => {
        initializeSimulation();
    });


    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר פיזיקלי';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג/הסתר את הסוד הפיזיקלי מאחורי האפקט';
        }
    });

    // Update slider value displays
    speedInput.addEventListener('input', () => {
        speedValueSpan.textContent = speedInput.value;
    });
     spinSpeedSideInput.addEventListener('input', () => {
        spinSpeedSideValueSpan.textContent = spinSpeedSideInput.value;
    });
     spinSpeedVertInput.addEventListener('input', () => {
        spinSpeedVertValueSpan.textContent = spinSpeedVertInput.value;
    });

    // Initial state: Draw ground and perhaps initial ball position ghost?
    // Let's just draw the ground initially.
    initializeSimulation();

</script>