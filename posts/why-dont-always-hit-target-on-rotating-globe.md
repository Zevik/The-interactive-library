---
title: "למה לא תמיד פוגעים במטרה בגלובוס מסתובב?"
english_slug: why-dont-always-hit-target-on-rotating-globe
category: "פיזיקה"
tags: פיזיקה, אפקט קוריוליס, גלובוס מסתובב, דינמיקה, תנועה יחסית
---
# למה לא תמיד פוגעים במטרה בגלובוס מסתובב?

דמיינו שאתם עומדים על גלובוס ענק ומסתובב במהירות ומנסים לזרוק כדור ישר אל חבר שעומד במרחק. האם הכדור יגיע אליו בקשת ישרה וידידותית? או שאולי... תפספסו לגמרי? בואו נגלה!

<div id="app-container">
    <div id="controls">
        <h2>כוונו את הזריקה שלכם</h2>
        <p>לחצו על הגלובוס לבחירת נקודת ההתחלה והיעד של הזריקה.</p>
        <div class="button-group">
            <button id="set-start-btn" class="active control-button">קבע נקודת התחלה</button>
            <button id="set-end-btn" class="control-button">קבע נקודת יעד</button>
        </div>
        <div class="control-slider">
            <label for="rotation-speed">מהירות סיבוב גלובוס:</label>
            <input type="range" id="rotation-speed" min="0" max="10" value="3" step="0.1">
            <span id="rotation-speed-value">3.0</span>x
        </div>
        <div class="control-slider">
            <label for="throw-speed">מהירות זריקה:</label>
            <input type="range" id="throw-speed" min="5" max="30" value="15" step="0.5">
            <span id="throw-speed-value">15.0</span>
        </div>
        <div class="button-group">
            <button id="throw-btn" class="control-button primary" disabled>זרוק את הכדור!</button>
            <button id="reset-btn" class="control-button secondary">איפוס</button>
        </div>
    </div>
    <div id="globe-container">
        <canvas id="globe-canvas"></canvas>
        <div id="start-marker" class="marker start" style="display: none;"></div>
        <div id="end-marker" class="marker end" style="display: none;"></div>
        <div id="ball-marker" class="marker ball" style="display: none;"></div>
    </div>
     <div id="info">
        <p id="info-text">בחר נקודת התחלה על הגלובוס.</p>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --info-color: #17a2b8;
        --light-color: #f8f9fa;
        --dark-color: #343a40;
        --background-light: #f9f9f9;
        --border-color: #ccc;
        --border-radius: 8px;
        --padding: 20px;
        --marker-size: 24px; /* Slightly larger markers */
        --ball-size: 16px;
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* More modern font */
        line-height: 1.6;
        color: var(--dark-color);
        background-color: #e9ecef; /* Light background for the page */
        padding: 20px;
    }

    #app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: var(--padding);
        padding: var(--padding);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--background-light);
        max-width: 800px; /* Limit width for better readability */
        margin: 20px auto; /* Center the app */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    #controls {
        display: flex;
        flex-direction: column;
        gap: 15px; /* Increased spacing */
        width: 100%;
        max-width: 400px;
    }

    h2 {
        color: var(--dark-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 5px;
        margin-bottom: 15px;
    }

    .control-button {
        padding: 10px 15px; /* Adjusted padding */
        cursor: pointer;
        border: none; /* Remove default border */
        border-radius: 4px;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        font-size: 1em;
        font-weight: bold;
        text-align: center;
    }

     .button-group {
        display: flex;
        gap: 10px;
     }
     .button-group .control-button {
        flex-grow: 1;
     }


    .control-button.primary {
        background-color: var(--primary-color);
        color: white;
    }

    .control-button.secondary {
        background-color: var(--secondary-color);
        color: white;
    }

     .control-button.active {
        background-color: var(--success-color);
        color: white;
     }
      .control-button.active.secondary { /* Handle case where a secondary button might become active */
           background-color: var(--success-color);
      }


    .control-button:hover:not(:disabled) {
        opacity: 0.9;
    }

    .control-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        background-color: var(--secondary-color); /* Indicate disabled state */
    }

    .control-button.active:hover:not(:disabled) {
         background-color: #218838; /* Darker green on hover */
    }


    .control-slider {
        display: flex;
        align-items: center;
        gap: 10px;
        background-color: var(--light-color);
        padding: 8px 12px;
        border-radius: 4px;
        border: 1px solid var(--border-color);
    }

    .control-slider label {
        flex-basis: 150px; /* Give labels more space */
        font-weight: bold;
        color: var(--dark-color);
    }

    .control-slider input[type="range"] {
        flex-grow: 1;
        -webkit-appearance: none; /* Remove default slider styling */
        appearance: none;
        height: 8px;
        background: var(--primary-color); /* Blue track */
        outline: none;
        opacity: 0.8;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .control-slider input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--dark-color); /* Dark thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--light-color);
    }

    .control-slider input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--dark-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--light-color);
    }

    .control-slider input[type="range"]:hover {
        opacity: 1;
    }


    .control-slider span {
        font-weight: bold;
        min-width: 30px; /* Ensure value aligns */
        text-align: right;
    }


    #globe-container {
        position: relative;
        width: 400px; /* Keep size consistent */
        height: 400px;
        border: 3px solid var(--dark-color); /* Thicker border */
        border-radius: 50%;
        overflow: hidden;
        /* More complex background SVG for better detail */
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400"><circle cx="200" cy="200" r="198" fill="#4682B4"/><defs><radialGradient id="globeGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%"><stop offset="0%" stop-color="#4682B4"/><stop offset="100%" stop-color="#1E3A5F"/></radialGradient></defs><circle cx="200" cy="200" r="198" fill="url(%23globeGradient)"/><circle cx="200" cy="200" r="198" fill="none" stroke="#ADD8E6" stroke-width="0.5" stroke-dasharray="4 2"/><path d="M 200 2 V 398 M 2 200 H 398" stroke="#ADD8E6" stroke-width="1" opacity="0.5"/><circle cx="200" cy="200" r="50" stroke="#ADD8E6" stroke-width="1" fill="none" opacity="0.5"/><circle cx="200" cy="200" r="100" stroke="#ADD8E6" stroke-width="1" fill="none" opacity="0.5"/><circle cx="200" cy="200" r="150" stroke="#ADD8E6" stroke-width="1" fill="none" opacity="0.5"/></svg>');
        background-size: cover;
        background-position: center;
        flex-shrink: 0; /* Prevent shrinking */
        box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3); /* Inner shadow for depth */
    }

    #globe-canvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1; /* Draw paths above background */
        cursor: crosshair;
    }

    .marker {
        position: absolute;
        width: var(--marker-size);
        height: var(--marker-size);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        z-index: 2; /* Draw markers above paths */
        box-shadow: 0 0 5px rgba(0,0,0,0.5);
        display: flex; /* Center content */
        justify-content: center;
        align-items: center;
        font-size: 0.8em;
        font-weight: bold;
        color: white;
        text-shadow: 0 0 3px rgba(0,0,0,0.5);
    }

    .marker.start {
        background-color: var(--success-color);
        border: 3px solid darkgreen;
    }

    .marker.end {
        background-color: var(--danger-color);
        border: 3px solid darkred;
    }

     .marker.ball {
        width: var(--ball-size);
        height: var(--ball-size);
        background-color: var(--primary-color);
        border: 2px solid #0056b3;
        z-index: 3; /* Ball is on top */
        animation: pulse 1.5s infinite ease-in-out; /* Add subtle pulse animation */
     }

     @keyframes pulse {
        0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
        50% { transform: translate(-50%, -50%) scale(1.1); opacity: 0.9; }
        100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
     }


     #info {
        margin-top: 10px;
        padding: 10px;
        min-height: 2.5em; /* Reserve space for longer messages */
        text-align: center;
        color: var(--dark-color);
        background-color: var(--light-color);
        border: 1px solid var(--border-color);
        border-radius: 4px;
        width: 100%;
        max-width: 400px;
        font-style: italic;
        font-size: 0.95em;
     }

    .explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto 20px auto; /* More margin */
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        background-color: var(--info-color); /* Info blue */
        color: white;
        border-radius: 4px;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .explanation-button:hover {
         background-color: #138496; /* Darker info blue */
    }

    #explanation {
        display: none; /* Initially hidden */
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid var(--border-color);
        background-color: var(--light-color);
        padding: var(--padding);
        border-radius: var(--border-radius);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    #explanation h2 {
        color: var(--primary-color);
        margin-top: 15px;
        margin-bottom: 10px;
        border-bottom: none; /* Remove border from inner headings */
        padding-bottom: 0;
    }

     #explanation h2:first-child {
        margin-top: 0;
     }

    #explanation p {
        line-height: 1.6;
        margin-bottom: 15px; /* More spacing */
        color: var(--dark-color);
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-left: 20px;
    }

    #explanation li {
        margin-bottom: 8px;
    }

    /* Responsive adjustments */
    @media (min-width: 768px) {
        #app-container {
            flex-direction: row; /* Side-by-side layout on larger screens */
            align-items: flex-start; /* Align items to the top */
            gap: 40px; /* Increased gap */
        }

        #controls {
            max-width: 300px; /* Limit control width */
            flex-shrink: 0; /* Prevent shrinking */
        }

        #globe-container {
            width: 450px; /* Slightly larger globe */
            height: 450px;
        }

         #info {
             align-self: stretch; /* Make info box span height */
             max-width: none; /* Remove max width when beside globe */
             width: 300px; /* Give info box a fixed width */
         }
    }


</style>

<button class="explanation-button" id="toggle-explanation">הצג הסבר מדעי מאחורי הקלעים</button>

<div id="explanation">
    <h2>מהו אפקט קוריוליס? הכוח ה"מדומה" שמבלבל הכל במערכת מסתובבת</h2>
    <p>אפקט קוריוליס הוא לא כוח אמיתי במובן הפיזי כמו כוח כבידה או דחיפה. הוא כוח **מדומה (פיקטיבי)** ש"ממציאים" כדי להסביר למה גופים נעים בדרכים מוזרות כשאנחנו צופים בהם מתוך **מערכת שמסתובבת** – כמו כדור הארץ שלנו. דמיינו שאתם על קרוסלה מסתובבת ומנסים לזרוק משהו ישר. מהנקודת המבט של מי שעומד בחוץ ורואה אתכם מסתובבים, הזריקה אולי נראית ישרה. אבל מנקודת המבט שלכם, בתוך הקרוסלה, נראה שהאובייקט סוטה מהמסלול הישר שציפיתם לו!</p>

    <h2>מערכות ייחוס: אינרציאליות (רגועות) מול מסתובבות (קצת מסובכות)</h2>
    <p>בפיזיקה, אנחנו אוהבים מערכות ייחוס **אינרציאליות**. אלה מערכות (שאינן מאיצות או מסתובבות) שבהן חוקי התנועה של ניוטון עובדים פשוט: גוף שלא פועל עליו כוח ממשי ממשיך לנוע בקו ישר במהירות קבועה (או להישאר במקומו). אבל כדור הארץ, הקרוסלה בלונה פארק, והגלובוס בסימולציה שלנו – כולם **מערכות ייחוס מסתובבות**. צופה בתוך מערכת כזו רואה גופים חופשיים (שאין עליהם כוחות חיצוניים שמאלצים אותם לעקוב אחרי הסיבוב) סוטים מהקו הישר. כדי להסביר את הסטייה הזו באמצעות חוקי ניוטון הרגילים, חייבים להוסיף "כוחות" שלא קיימים במציאות האינרציאלית - אלה הכוחות המדומים.</p>

    <h2>כוחות מדומים במערכות מסתובבות: הכירו את קוריוליס וצנטריפוגלי</h2>
    <p>כשמנתחים תנועה במערכת מסתובבת, משתמשים בשני כוחות מדומים עיקריים:</p>
    <ul>
        <li>**כוח קוריוליס:** זה הכוח שגורם לסטייה הצידה ממסלול ישר במערכת המסתובבת. הוא פועל תמיד **בניצב** לכיוון התנועה של הגוף ביחס למערכת. כיוונו תלוי בכיוון התנועה של הגוף ובכיוון הסיבוב של המערכת. גודלו גדל ככל שהגוף נע מהר יותר ביחס למערכת וככל שהמערכת מסתובבת מהר יותר. בסימולציה שלנו, הסטייה של הכדור מהיעד נובעת בעיקר מאפקט קוריוליס.</li>
        <li>**כוח צנטריפוגלי:** זה הכוח שמרגישים שדוחף אתכם החוצה כשמסתובבים (למשל, בקרוסלת שרשראות). הוא פועל תמיד **החוצה** ממרכז הסיבוב. כוח זה פועל גם על גופים שנחים ביחס למערכת המסתובבת (אם הם לא בדיוק במרכז). בסימולציה זו אנחנו מתמקדים בתנועה הרדיאלית וההיקפית המורכבת שיוצר אפקט קוריוליס.</li>
    </ul>

    <h2>כדור הארץ והקוריוליס: למה רוחות וזרמים מתעקלים?</h2>
    <p>כדור הארץ הוא דוגמה ענקית למערכת ייחוס מסתובבת. אזורים שונים על פני כדור הארץ נעים במהירות שונה סביב ציר הסיבוב (קו המשווה נע מהר יותר מהקוטב). כשגוף (כמו אוויר, מים, או טיל) נע למרחק גדול על פני כדור הארץ, הוא עובר לאזורים בעלי מהירות סיבוב שונה. בגלל שהוא שומר על חלק מ"המומנטום" שלו (קשור לנטייה להמשיך לנוע בקו ישר במערכת אינרציאלית), הוא נראה כאילו הוא סוטה מהקו הישר מנקודת מבטו של צופה על פני כדור הארץ.</p>

    <h2>הסטייה ימינה או שמאלה? תלוי איפה אתם!</h2>
    <p>כיוון הסטייה הנגרמת על ידי אפקט קוריוליס תלוי בחצי הכדור שבו אתם נמצאים:</p>
    <ul>
        <li>**בחצי הכדור הצפוני:** גופים נעים סוטים **ימינה** מכיוון התנועה המקורי שלהם.</li>
        <li>**בחצי הכדור הדרומי:** גופים נעים סוטים **שמאלה** מכיוון התנועה המקורי שלהם.</li>
        <li>**על קו המשווה:** אפקט קוריוליס כמעט לא משפיע על תנועה אופקית.</li>
    </ul>

    <h2>איפה פוגשים את אפקט קוריוליס בטבע ובטכנולוגיה?</h2>
    <p>לאפקט קוריוליס יש השפעות דרמטיות על תופעות רחבות היקף:</p>
    <ul>
        <li>**מזג אוויר:** הוא גורם לסיבוב של מערכות לחץ נמוך (כמו סופות הוריקן וציקלונים) וגבוה. הוא זה שקובע שהם יסתובבו עם כיוון השעון או נגדו, בהתאם לחצי הכדור.</li>
        <li>**אוקיינוסים:** הוא משפיע על זרמי הים העיקריים בעולם, ויוצר מערכות זרימה ענקיות.</li>
        <li>**תעופה וטילים:** כדי לשגר טיל לטווח ארוך או לנווט מטוס במדויק, חייבים לחשב את השפעת אפקט קוריוליס על המסלול.</li>
        <li>**גם בדברים קטנים לכאורה:** הוא יכול להשפיע לאורך זמן על שחיקת מסילות רכבת ארוכות בכיוון צפון-דרום!</li>
    </ul>
    <p>בסימולציה שלנו, למרות שהיא פשטנית (דו-ממדית ובלי כבידה למשל), אתם יכולים לראות את העיקרון הבסיסי בפעולה: מה שנראה כמו זריקה ישרה מההתחלה, סוטה ממסלולה מנקודת מבטכם על הגלובוס המסתובב, והיעד שלכם זז בינתיים!</p>
</div>


<script>
    const canvas = document.getElementById('globe-canvas');
    const ctx = canvas.getContext('2d');
    const startMarker = document.getElementById('start-marker');
    const endMarker = document.getElementById('end-marker');
    const ballMarker = document.getElementById('ball-marker'); // Added ball marker
    const setStartBtn = document.getElementById('set-start-btn');
    const setEndBtn = document.getElementById('set-end-btn');
    const rotationSpeedInput = document.getElementById('rotation-speed');
    const rotationSpeedValue = document.getElementById('rotation-speed-value');
    const throwSpeedInput = document.getElementById('throw-speed');
    const throwSpeedValue = document.getElementById('throw-speed-value');
    const throwBtn = document.getElementById('throw-btn');
    const resetBtn = document.getElementById('reset-btn');
    const infoText = document.getElementById('info-text');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');

    let canvasSize = 400; // Keep size consistent with CSS base
     // Adjust for responsive layout if needed, but code assumes fixed size for simplicity
     const globeContainer = document.getElementById('globe-container');
     const rect = globeContainer.getBoundingClientRect();
     canvasSize = rect.width; // Use actual rendered size
     canvas.width = canvasSize;
     canvas.height = canvasSize;


    const globeRadius = canvasSize / 2;
    const centerX = canvasSize / 2;
    const centerY = canvasSize / 2;

    let startPos = null; // {x, y} in canvas coordinates
    let endPos = null; // {x, y} in canvas coordinates (initial position in rotating frame when set)
    let settingStart = true;
    let animationFrameId = null;
    let simulationTime = 0; // Represents steps/frames
    let simulationRunningTime = 0; // Represents elapsed time in simulation units (e.g., seconds)
    const timeStep = 1 / 60; // Simulate 60 frames per second

    let pathPointsInertial = []; // Path in the inertial frame (straight line)
    let pathPointsRotating = []; // Path traced by the ball *as seen from the rotating frame*
    let targetPathRotating = []; // Path traced by the *target* as seen from the rotating frame

    let isAnimating = false;

    // --- Utility Functions ---

    // Convert canvas coordinates to polar coordinates (radius, angle) relative to center
    function toPolar({ x, y }) {
        const dx = x - centerX;
        const dy = y - centerY;
        const r = Math.sqrt(dx * dx + dy * dy);
        // Adjust angle to be 0 along positive X axis, increasing counter-clockwise
        // Canvas Y is down, so Math.atan2 gives angle relative to positive X axis, increasing clockwise for positive angle
        let angle = Math.atan2(dy, dx);
         // We might want angle relative to UP (negative Y) or positive X depending on convention
         // Let's use standard math angle: 0 = positive X, pi/2 = positive Y, pi = negative X, 3pi/2 = negative Y
         // Canvas Y is inverted, so dy is positive when point is below center
         // If 0 is positive X, increasing CCW: Math.atan2(dy, dx) is correct.
         // If 0 is positive Y (up), increasing CW (like compass): Math.atan2(dx, -dy) or adjust.
         // Let's stick to Math.atan2 standard for internal math.
        return { r, angle };
    }

     // Convert polar coordinates (radius, angle) relative to center to canvas coordinates
     // Angle is standard Math angle (0=pos X, increasing CCW)
    function fromPolar(r, angle) {
        const x = centerX + r * Math.cos(angle);
        const y = centerY + r * Math.sin(angle);
        return { x, y };
    }


    // Clamp position to be within the globe circle
    function clampToGlobe(x, y) {
        const dx = x - centerX;
        const dy = y - centerY;
        const dist = Math.sqrt(dx*dx + dy*dy);
        if (dist > globeRadius) {
            const ratio = globeRadius / dist;
            x = centerX + dx * ratio;
            y = centerY + dy * ratio;
        }
        return { x, y };
    }

    // Place marker element
    function placeMarker(markerElement, { x, y }) {
        markerElement.style.display = 'block';
        // Position CSS element relative to the globe-container
        const containerRect = globeContainer.getBoundingClientRect();
        markerElement.style.left = `${x}px`; // Position relative to container's top-left
        markerElement.style.top = `${y}px`;
    }

    // --- Drawing Functions ---

    function drawGlobe() {
        // Background is handled by CSS image now
        // We only clear the canvas layer for dynamic drawing (paths, ball)
    }

    function drawPathsAndAnimation() {
        ctx.clearRect(0, 0, canvasSize, canvasSize); // Clear only the canvas layer

        // Get current positions based on simulation time
        const currentIndex = Math.floor(simulationRunningTime / timeStep);

        // Draw Inertial Path (Target Line - maybe dashed or less prominent)
        if (pathPointsInertial.length > 0) {
            ctx.beginPath();
            ctx.moveTo(pathPointsInertial[0].x, pathPointsInertial[0].y);
            for (let i = 1; i < pathPointsInertial.length; i++) {
                ctx.lineTo(pathPointsInertial[i].x, pathPointsInertial[i].y);
            }
            ctx.strokeStyle = 'rgba(0, 0, 255, 0.5)'; // Semi-transparent blue
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]); // Make it dashed
            ctx.stroke();
             ctx.setLineDash([]); // Reset dash
        }

        // Draw Rotating Path traced SO FAR
        if (pathPointsRotating.length > 0 && currentIndex > 0) {
            ctx.beginPath();
            ctx.moveTo(pathPointsRotating[0].x, pathPointsRotating[0].y);
             // Draw only up to the current step
            const pointsToDraw = Math.min(currentIndex + 1, pathPointsRotating.length);
            for (let i = 1; i < pointsToDraw; i++) {
                ctx.lineTo(pathPointsRotating[i].x, pathPointsRotating[i].y);
            }
            ctx.strokeStyle = 'orange';
            ctx.lineWidth = 3; // Thicker path for the ball's actual trajectory
            ctx.stroke();
        }

        // Update Ball Marker Position
         if (isAnimating && currentIndex < pathPointsRotating.length) {
             const currentBallPos = pathPointsRotating[currentIndex];
             placeMarker(ballMarker, currentBallPos);
         } else {
             ballMarker.style.display = 'none';
         }

         // Update Target Marker Position in Rotating Frame
         if (isAnimating && currentIndex < targetPathRotating.length) {
              const currentTargetPos = targetPathRotating[currentIndex];
              placeMarker(endMarker, currentTargetPos); // Move the end marker during animation
         } else if (endPos) {
             placeMarker(endMarker, endPos); // Place end marker at initial set position when not animating
         }


    }

    // --- Simulation Logic ---

    function calculatePaths() {
        if (!startPos || !endPos) return;

        pathPointsInertial = [];
        pathPointsRotating = [];
        targetPathRotating = []; // Reset target path

        // We need the initial state in the inertial frame (relative to globe center)
        const startPolar = toPolar(startPos);
        const endPolar = toPolar(endPos); // Target's initial position in inertial frame

        // Direction vector in inertial frame from start to end
        const initialDx = endPos.x - startPos.x;
        const initialDy = endPos.y - startPos.y;
        const distance = Math.sqrt(initialDx * initialDx + initialDy * initialDy);

        // Avoid division by zero if start and end are the same point (should be prevented by UI)
        if (distance < 1) {
             infoText.textContent = "נקודות ההתחלה והיעד קרובות מדי!";
             throwBtn.disabled = true;
             return;
        }

        const throwSpeed = parseFloat(throwSpeedInput.value);
        const throwDuration = distance / throwSpeed; // Time to reach target in inertial frame

        // Ensure minimum steps for smooth path drawing
        const totalSteps = Math.max(100, Math.ceil(throwDuration / timeStep));

        // Rotation speed in radians per simulation time unit
        // rotationSpeedInput value is a multiplier, let's scale it.
        // 1x could be, for example, 1 rotation per 10 seconds simulation time.
        const baseRotationSpeed = 2 * Math.PI / 10; // 1 rotation per 10 sim seconds at 1x
        const rotationSpeedRadPerSec = parseFloat(rotationSpeedInput.value) * baseRotationSpeed;


        for (let i = 0; i <= totalSteps; i++) {
            const t = i * timeStep;
            const progress = t / throwDuration;

            // Position in Inertial Frame (simple linear interpolation)
            const inertialX = startPos.x + initialDx * progress;
            const inertialY = startPos.y + initialDy * progress;
            const inertialPos = { x: inertialX, y: inertialY };
            pathPointsInertial.push(inertialPos);

            // Calculate the current rotation angle of the globe at time t
            // Assuming clockwise rotation in canvas coordinates makes angles increase CW.
            // The globe (frame) rotates by `rotationAngle` CW.
            const globeRotationAngle = rotationSpeedRadPerSec * t;

            // --- Calculate Ball Position in Rotating Frame ---
            // Position of the ball {inertialX, inertialY} relative to the center {centerX, centerY} in inertial frame
            const ballRelCenterX_Inertial = inertialX - centerX;
            const ballRelCenterY_Inertial = inertialY - centerY;

            // To find its position in the rotating frame, we "un-rotate" it by the globe's rotation angle.
            // If the frame rotated by +angle CW, the point appears rotated by -angle CW relative to frame axes.
            // In standard math rotation (CCW positive angle): rotate by -globeRotationAngle.
            // Let's use Math.atan2 convention (positive X, CCW positive angle) for clarity internally.
            // If canvas Y is down, standard Math rotation (CCW positive) around origin (0,0):
            // x' = x cos(a) - y sin(a)
            // y' = x sin(a) + y cos(a)
            // We rotate the inertial position {ballRelCenterX_Inertial, ballRelCenterY_Inertial} by -globeRotationAngle
            const ballRelCenterX_Rotating = ballRelCenterX_Inertial * Math.cos(-globeRotationAngle) - ballRelCenterY_Inertial * Math.sin(-globeRotationAngle);
            const ballRelCenterY_Rotating = ballRelCenterX_Inertial * Math.sin(-globeRotationAngle) + ballRelCenterY_Inertial * Math.cos(-globeRotationAngle);

            // Convert back to canvas coordinates (add center offset)
            const ballRotatingX = centerX + ballRelCenterX_Rotating;
            const ballRotatingY = centerY + ballRelCenterY_Rotating;
            const ballRotatingPos = { x: ballRotatingX, y: ballRotatingY };
            pathPointsRotating.push(ballRotatingPos);


            // --- Calculate Target Position in Rotating Frame ---
            // The target is fixed *on the globe*. Its position in the inertial frame changes due to rotation.
            // Its initial position in the inertial frame is endPos.
            // Relative to center, its initial inertial position is {endPos.x - centerX, endPos.y - centerY}.
            const targetRelCenterX_InitialInertial = endPos.x - centerX;
            const targetRelCenterY_InitialInertial = endPos.y - centerY;

            // At time t, the target's position in the inertial frame is this initial vector rotated by +globeRotationAngle.
            const targetRelCenterX_Inertial = targetRelCenterX_InitialInertial * Math.cos(globeRotationAngle) - targetRelCenterY_InitialInertial * Math.sin(globeRotationAngle);
            const targetRelCenterY_Inertial = targetRelCenterX_InitialInertial * Math.sin(globeRotationAngle) + targetRelCenterY_InitialInertial * Math.cos(globeRotationAngle);
             // Convert back to inertial canvas coords (not needed for display, but for concept)
             // const targetInertialX = centerX + targetRelCenterX_Inertial;
             // const targetInertialY = centerY + targetRelCenterY_Inertial;

            // The target's position *in the rotating frame* is simply its initial position (endPos), because it's fixed *to* that frame.
            // So, targetPathRotating points are all the same: endPos.
             targetPathRotating.push({ x: endPos.x, y: endPos.y }); // Target is fixed in the rotating frame

        }
         // The animation duration in real time will be based on totalSteps and frame rate (approx totalSteps * timeStep)
         // The "throwDuration" calculated above was the time *in the inertial frame* for the ball to cover the straight distance.
         // We use totalSteps to control animation frames, ensuring enough detail regardless of speed/distance.

    }


    function animateThrow() {
        if (!isAnimating) {
            simulationRunningTime = 0; // Reset simulation time
            isAnimating = true;
            calculatePaths(); // Recalculate paths based on current settings
            infoText.textContent = "הכדור בדרכו! צפו במסלול הכתום...";
             throwBtn.disabled = true; // Disable during animation
             setStartBtn.disabled = true;
             setEndBtn.disabled = true;
             rotationSpeedInput.disabled = true;
             throwSpeedInput.disabled = true;
             ballMarker.style.display = 'block'; // Show the ball marker
        }

        // Update simulation time
        simulationRunningTime += timeStep;

        // Get current index based on time
        const currentIndex = Math.floor(simulationRunningTime / timeStep);

        // Draw current frame
        drawPathsAndAnimation();

        // Stop condition: reached end of pre-calculated path points
        if (currentIndex >= pathPointsRotating.length -1) { // Stop on or after the last step
            isAnimating = false;
            cancelAnimationFrame(animationFrameId);
             ballMarker.style.display = 'none'; // Hide ball marker at the end

            // Check for hit/miss (simple check: is the final ball position close to the final target position?)
            const finalBallPos = pathPointsRotating[pathPointsRotating.length - 1];
            const finalTargetPos = targetPathRotating[targetPathRotating.length - 1]; // Which is just endPos

            const hitDistanceThreshold = 20; // Pixels distance to consider a hit

            const dx = finalBallPos.x - finalTargetPos.x;
            const dy = finalBallPos.y - finalTargetPos.y;
            const finalDistance = Math.sqrt(dx*dx + dy*dy);

            if (finalDistance < hitDistanceThreshold) {
                 infoText.textContent = `!פגיעה מדהימה! הצלחתם לפגוע ביעד במערכת המסתובבת`;
                  // Add visual hit effect? Maybe just color info text green
                  infoText.style.color = var(--success-color);

            } else {
                infoText.textContent = `!החטאה... הכדור הגיע לכאן בעוד שהיעד היה שם... שימו לב לסטייה הדרמטית!`;
                 // Highlight miss? Maybe color info text red
                 infoText.style.color = var(--danger-color);
            }

             // Re-enable controls after animation ends
             throwBtn.disabled = false; // Re-enable throw (maybe allow re-throw with same settings?)
             setStartBtn.disabled = false;
             setEndBtn.disabled = false;
              rotationSpeedInput.disabled = false;
             throwSpeedInput.disabled = false;
        } else {
            // Request next frame
            animationFrameId = requestAnimationFrame(animateThrow);
        }
    }

    // --- Event Handlers ---

    function handleCanvasClick(event) {
        if (isAnimating) return; // Don't allow setting points during animation

        const rect = canvas.getBoundingClientRect();
        const clickX = event.clientX - rect.left;
        const clickY = event.clientY - rect.top;

        // Ensure click is within the circular globe area
        const clampedPos = clampToGlobe(clickX, clickY);
        const { x, y } = clampedPos;

        if (settingStart) {
            startPos = { x, y };
            placeMarker(startMarker, startPos);
            startMarker.textContent = 'התחלה'; // Add text label
            settingStart = false;
            setStartBtn.classList.remove('active');
            setEndBtn.classList.add('active');
            infoText.textContent = "בחר נקודת יעד על הגלובוס.";
            infoText.style.color = var(--dark-color); // Reset info color

             // Clear previous paths and ball
            pathPointsInertial = [];
            pathPointsRotating = [];
            targetPathRotating = [];
             ballMarker.style.display = 'none';
            drawPathsAndAnimation(); // Clear canvas paths

        } else {
            endPos = { x, y };
            placeMarker(endMarker, endPos);
             endMarker.textContent = 'יעד'; // Add text label
            settingStart = true; // Reset state to set start next time
            setEndBtn.classList.remove('active');
             // No button is active after setting end point until reset or throw
            infoText.textContent = "נקודות ההתחלה והיעד נבחרו. לחץ על 'זרוק את הכדור!'";
            infoText.style.color = var(--dark-color); // Reset info color
            throwBtn.disabled = false; // Enable throw button
             // Clear previous paths if any were drawn statically
            pathPointsInertial = [];
            pathPointsRotating = [];
            targetPathRotating = [];
            drawPathsAndAnimation(); // Clear canvas before calculating new path

            // Calculate and draw static paths preview
             calculatePaths();
             drawPathsAndAnimation(); // Draw initial static paths
        }
    }

    function handleSetStartClick() {
        if (isAnimating) return;
        settingStart = true;
        setStartBtn.classList.add('active');
        setEndBtn.classList.remove('active');
        infoText.textContent = "בחר נקודת התחלה על הגלובוס.";
        infoText.style.color = var(--dark-color); // Reset info color
        throwBtn.disabled = true;
    }

    function handleSetEndClick() {
         if (isAnimating) return;
        settingStart = false;
        setEndBtn.classList.add('active');
        setStartBtn.classList.remove('active');
        infoText.textContent = "בחר נקודת יעד על הגלובוס.";
        infoText.style.color = var(--dark-color); // Reset info color
         throwBtn.disabled = true;
    }


    function handleRotationSpeedChange() {
        rotationSpeedValue.textContent = parseFloat(rotationSpeedInput.value).toFixed(1);
         if (!isAnimating && startPos && endPos) { // Only recalculate if not animating and points are set
            calculatePaths();
            drawPathsAndAnimation();
         }
    }

    function handleThrowSpeedChange() {
        throwSpeedValue.textContent = parseFloat(throwSpeedInput.value).toFixed(1);
         if (!isAnimating && startPos && endPos) { // Only recalculate if not animating and points are set
            calculatePaths();
            drawPathsAndAnimation();
         }
    }

    function handleThrowClick() {
        if (startPos && endPos && !isAnimating) {
             infoText.style.color = var(--dark-color); // Reset info color
            animateThrow();
             // Buttons/inputs disabled during animation are handled inside animateThrow start block
        } else if (!startPos || !endPos) {
             infoText.textContent = "אנא בחר נקודת התחלה ויעד לפני הזריקה.";
             infoText.style.color = var(--danger-color);
        }
    }

    function handleResetClick() {
        cancelAnimationFrame(animationFrameId);
        isAnimating = false;
        simulationRunningTime = 0;
        startPos = null;
        endPos = null;
        startMarker.style.display = 'none';
        endMarker.style.display = 'none';
        ballMarker.style.display = 'none'; // Hide ball marker
        pathPointsInertial = [];
        pathPointsRotating = [];
         targetPathRotating = [];
        drawPathsAndAnimation(); // Clear canvas
        infoText.textContent = "איפוס בוצע. בחר נקודת התחלה על הגלובוס.";
        infoText.style.color = var(--dark-color); // Reset info color
        settingStart = true;
        setStartBtn.classList.add('active');
        setEndBtn.classList.remove('active');
        throwBtn.disabled = true;
        setStartBtn.disabled = false;
        setEndBtn.disabled = false;
         rotationSpeedInput.disabled = false;
        throwSpeedInput.disabled = false;
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מדעי' : 'הצג הסבר מדעי מאחורי הקלעים';
         // Scroll to explanation if shown?
         if (!isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    }

    // --- Initialization ---

    function init() {
         // Canvas size is already set based on container size detection
        drawGlobe(); // Draw the static background (or rely on CSS)
        drawPathsAndAnimation(); // Clear paths initially
        infoText.textContent = "בחר נקודת התחלה על הגלובוס.";
        infoText.style.color = var(--dark-color); // Ensure initial color

        canvas.addEventListener('click', handleCanvasClick);
        setStartBtn.addEventListener('click', handleSetStartClick);
        setEndBtn.addEventListener('click', handleSetEndClick);
        rotationSpeedInput.addEventListener('input', handleRotationSpeedChange);
        throwSpeedInput.addEventListener('input', handleThrowSpeedChange);
        throwBtn.addEventListener('click', handleThrowClick);
        resetBtn.addEventListener('click', handleResetClick);
        toggleExplanationBtn.addEventListener('click', toggleExplanation);

         // Initial display of speed values
        rotationSpeedValue.textContent = parseFloat(rotationSpeedInput.value).toFixed(1);
        throwSpeedValue.textContent = parseFloat(throwSpeedInput.value).toFixed(1);
         // Set initial active button state
         setStartBtn.classList.add('active');
    }

    // Run initialization once DOM is ready
    document.addEventListener('DOMContentLoaded', init);


    // Optional: Handle window resize to adjust canvas size
    // This makes it more responsive, but the simulation logic assumes fixed size for simplicity.
    // Disabling for strict adherence to fixed size example, but good practice.
     /*
     window.addEventListener('resize', () => {
         const rect = globeContainer.getBoundingClientRect();
         canvasSize = rect.width;
         canvas.width = canvasSize;
         canvas.height = canvasSize;
         globeRadius = canvasSize / 2;
         centerX = canvasSize / 2;
         centerY = canvasSize / 2;
         drawGlobe(); // Redraw background
         if (startPos) placeMarker(startMarker, startPos);
         if (endPos) placeMarker(endMarker, endPos);
         if (isAnimating) {
              // Recalculating paths on resize during animation is complex, maybe just stop
              handleResetClick();
              infoText.textContent = "הסימולציה אותחלה עקב שינוי גודל מסך.";
         } else if (startPos && endPos) {
              // If points are set but not animating, recalculate and redraw static paths
              calculatePaths();
              drawPathsAndAnimation();
         } else {
              drawPathsAndAnimation(); // Clear canvas
         }
     });
    */


</script>
```