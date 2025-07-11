---
title: "חוויה אינטראקטיבית: תעלומת אפקט קוריוליס על גלובוס מסתובב"
english_slug: interactive-experience-coriolis-effect-rotating-globe
category: "פיזיקה"
tags: [הדמיה, אינטראקטיבי, דינמיקה, סיבוב, כוח מדומה, מערכת ייחוס]
---
# חוויה אינטראקטיבית: אפקט קוריוליס על גלובוס מסתובב

האם דמיינתם פעם לזרוק כדור על משטח שמסתובב מתחת לרגליכם? מה שנראה כמו קו ישר מנקודת מבט יציבה בחלל, הופך למסלול מסתורי ומעוקל כשצופים בו מתוך המערכת המסתובבת עצמה. צללו לתוך הסימולציה הזו וגלו את אפקט קוריוליס בפעולה – כוח מדומה שמשפיע על הכול, מזרמי אוקיינוסים ועד סופות ענק!

<div class="simulation-container">
    <canvas id="coriolisCanvas"></canvas>
    <div class="controls">
        <button id="startButton">שגר!</button>
        <button id="clearButton">נקה</button>
        <div class="parameter">
            <label for="rotationSpeed">מהירות סיבוב הגלובוס:</label>
            <input type="range" id="rotationSpeed" min="0" max="5" value="1" step="0.1">
            <span id="rotationSpeedValue">1.0</span>
        </div>
        <div class="parameter">
            <label for="launchSpeed">מהירות השיגור:</label>
            <input type="range" id="launchSpeed" min="0.5" max="10" value="4" step="0.1">
            <span id="launchSpeedValue">4.0</span>
        </div>
        <div class="parameter">
            <label for="launchAngle">כיוון השיגור (מעלות):</label>
            <input type="range" id="launchAngle" min="0" max="360" value="45" step="1">
            <span id="launchAngleValue">45</span>
        </div>
         <div class="parameter">
            <label for="startRadius">מרחק נקודת השיגור (ממרכז):</label>
            <input type="range" id="startRadius" min="10" max="130" value="100" step="1">
            <span id="startRadiusValue">100</span>
        </div>
         <div class="parameter">
            <label for="showLaunchPoint">הצג נקודת שיגור:</label>
             <input type="checkbox" id="showLaunchPoint" checked>
        </div>
    </div>
</div>

<style>
    /* שיפורים עיצוביים */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #eef2f7; /* רקע עדין לגוף הדף */
        color: #333;
        line-height: 1.6;
    }

    h1 {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 20px;
    }

    p {
         text-align: center;
         max-width: 700px;
         margin: 0 auto 30px auto;
         font-size: 1.1em;
         color: #555;
    }

    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* מרווח גדול יותר */
        margin: 30px auto; /* מרווח מהכותרת והפסקה */
        padding: 30px; /* פדינג פנימי */
        border: none; /* מסגרת עדיפה יותר */
        border-radius: 12px; /* פינות מעוגלות יותר */
        background: linear-gradient(to bottom right, #ffffff, #f0f4f8); /* רקע עם גרדיאנט */
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15); /* צל עמוק יותר */
        max-width: 750px; /* רוחב מקסימלי */
        transition: transform 0.3s ease; /* אנימציית מעבר בריחוף */
    }

     .simulation-container:hover {
         transform: translateY(-5px); /* אפקט ריחוף */
     }


    canvas {
        border: 1px solid #cce7ff; /* מסגרת עדינה יותר */
        background: radial-gradient(circle at center, #e3f2fd, #90caf9); /* גרדיאנט רדיאלי לכדור הארץ */
        border-radius: 50%; /* Make canvas look like a disk */
        box-shadow: 0 6px 15px rgba(0,0,0,0.2); /* צל עמוק יותר */
        width: 350px; /* גודל גדול יותר */
        height: 350px;
        display: block;
        margin-bottom: 20px; /* מרווח מהבקרות */
    }

    .controls {
        display: flex;
        flex-direction: column;
        gap: 15px; /* מרווח גדול יותר בין בקרות */
        width: 100%;
        max-width: 450px; /* רוחב מקסימלי גדול יותר */
        align-items: stretch;
    }

    .parameter {
        display: flex;
        align-items: center;
        gap: 15px; /* מרווח גדול יותר */
        justify-content: space-between;
        padding: 8px 0; /* פדינג קטן */
        border-bottom: 1px dashed #e0e0e0; /* קו מפריד עדין */
    }

     .parameter:last-child {
         border-bottom: none; /* ללא קו מפריד אחרון */
     }

    .parameter label {
        font-weight: bold;
        flex-shrink: 0;
        color: #555;
        font-size: 1em;
    }

    .parameter input[type="range"] {
        flex-grow: 1;
        -webkit-appearance: none;
        appearance: none;
        height: 10px; /* עובי סליידר */
        background: #bbdefb; /* צבע רקע סליידר */
        outline: none;
        opacity: 0.9; /* שקיפות קלה */
        transition: opacity .2s;
        border-radius: 5px;
    }

    .parameter input[type="range"]:hover {
        opacity: 1;
    }

    .parameter input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* גודל פאלץ */
        height: 20px;
        background: #1e88e5; /* צבע פאלץ כחול עמוק */
        cursor: pointer;
        border-radius: 50%; /* עגול */
        border: 3px solid #e3f2fd; /* מסגרת בהירה */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* צל לפאלץ */
        transition: background-color 0.2s ease;
    }

    .parameter input[type="range"]::-webkit-slider-thumb:hover {
         background-color: #1565c0; /* כחול כהה יותר בריחוף */
    }


    .parameter input[type="range"]::-moz-range-thumb {
        width: 20px; /* גודל פאלץ */
        height: 20px;
        background: #1e88e5; /* צבע פאלץ כחול עמוק */
        cursor: pointer;
        border-radius: 50%; /* עגול */
        border: 3px solid #e3f2fd; /* מסגרת בהירה */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* צל לפאלץ */
        transition: background-color 0.2s ease;
    }

     .parameter input[type="range"]::-moz-range-thumb:hover {
         background-color: #1565c0; /* כחול כהה יותר בריחוף */
    }

    .parameter span {
        width: 40px; /* רוחב רחב יותר לערך */
        text-align: right;
        font-weight: normal; /* לא מודגש */
        color: #333;
    }

    .parameter input[type="checkbox"] {
        margin-right: auto; /* Push checkbox to the left */
        transform: scale(1.2); /* Make checkbox slightly larger */
        accent-color: #1e88e5; /* Color for the checked state */
    }


    button {
        padding: 12px 20px; /* פדינג גדול יותר */
        background-color: #42a5f5; /* כחול בינוני */
        color: white;
        border: none;
        border-radius: 6px; /* פינות מעוגלות */
        cursor: pointer;
        font-size: 1.1em; /* גודל פונט גדול יותר */
        transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציית מעבר וכיווץ */
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* צל לכפתורים */
    }

    button:hover {
        background-color: #2196f3; /* כחול עמוק יותר */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    button:active {
        background-color: #1976d2; /* כחול כהה */
        transform: scale(0.98); /* אפקט לחיצה */
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    #explanationButton {
        display: block;
        margin: 30px auto; /* מרווח מהסימולציה */
        padding: 12px 25px; /* פדינג גדול יותר */
        background-color: #66bb6a; /* ירוק */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    #explanationButton:hover {
        background-color: #4caf50; /* ירוק כהה יותר */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
     #explanationButton:active {
        background-color: #388e3c; /* ירוק כהה */
        transform: scale(0.98);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }


    .explanation {
        margin-top: 30px; /* מרווח מהכפתור */
        padding: 20px; /* פדינג פנימי */
        border: none;
        border-radius: 10px;
        background-color: #e0f2f7; /* רקע תכלת עדין */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* צל */
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        display: none; /* Hidden by default */
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start slightly below for animation */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out; /* Animation */
    }

    .explanation.visible {
        display: block; /* Show when visible */
        opacity: 1; /* Fade in */
        transform: translateY(0); /* Move to final position */
    }


    .explanation p {
        margin-bottom: 15px; /* מרווח בין פסקאות */
        line-height: 1.7; /* רווח שורה גדול יותר */
        text-align: right; /* יישור לימין */
        padding: 0 10px; /* פדינג בצדדים */
    }

    .explanation h3 {
        margin-top: 0;
        color: #1a237e; /* כחול עמוק לכותרת */
        text-align: center;
        margin-bottom: 15px;
    }
</style>

<button id="explanationButton">הצג לי את הסוד!</button>

<div class="explanation" id="explanation">
    <h3>אז מה קרה כאן בעצם? תעלומת אפקט קוריוליס נחשפת!</h3>
    <p>מה שחוויתם בסימולציה הוא המחשה מרתקת של אפקט קוריוליס. חשוב להבין: אפקט קוריוליס <strong>אינו כוח אמיתי</strong> במובן הפיזיקלי הקלאסי, כמו כוח כבידה או כוח אלקטרומגנטי. הוא מכונה "כוח מדומה" או "כוח דמיוני" (Fictitious Force), והוא נובע אך ורק מהעובדה שאנו מתארים את התנועה מתוך <strong>מערכת ייחוס שמסתובבת</strong> – בדיוק כמו הגלובוס בסימולציה, או כדור הארץ במציאות!</p>

    <p>דמיינו שוב את הסימולציה: ה"גלובוס" הוא דיסק שמסתובב ללא הרף. ה"כדור" (הנקודה הצהובה) ששיגרתם למעשה נע בקו ישר לחלוטין ביחס לצופה שנמצא מחוץ לדיסק המסתובב (במערכת ייחוס שאינה מסתובבת – מערכת אינרציאלית). ה"כדור" פשוט ממשיך בתנועתו הישרה בגלל התמד. אולם, בזמן שהכדור מתקדם ישר, הדיסק שמתחתיו <strong>מסתובב</strong>!</p>

    <p>נקודת ההתחלה של הכדור על הדיסק נעה יחד עם הדיסק. נקודת הסיום, אליה היה מגיע הכדור אם הדיסק לא היה מסתובב, גם היא זזה בגלל סיבוב הדיסק. אבל הכדור, בגלל התמדה, לא מגיע לנקודה הזו. הוא ממשיך לנוע בקו ישר במערכת הייחוס האינרציאלית. כשאנו משרטטים את המסלול שלו <strong>על גבי הדיסק המסתובב</strong> (כמו השביל הוורוד בסימולציה), אנחנו בעצם עוקבים אחרי מיקום הכדור ביחס לנקודות שעל הדיסק. מכיוון שהדיסק עצמו מסתובב ו"בורח" מתחת לכדור, המסלול המצטייר על הדיסק נראה לנו כאילו הוא מתעקם – למרות שהכדור עצמו נע ישר!</p>

    <p>אפקט קוריוליס אחראי לתופעות רבות ומשפיע על העולם שסביבנו. בחצי הכדור הצפוני, תנועת גופים ארוכת טווח נוטה לסטות ימינה ביחס לכיוון התנועה המקורי (בגלל סיבוב כדור הארץ נגד כיוון השעון כשמסתכלים מהקוטב הצפוני). בחצי הכדור הדרומי, הסטייה היא שמאלה. זה מה שגורם, למשל, לסופות ציקלון והוריקן להסתובב בכיוונים מנוגדים בחצאי כדור הארץ השונים, משפיע על מסלולי טילים ארוכי טווח, על זרמי אוויר באטמוספירה ועל זרמים ימיים באוקיינוסים. הסימולציה הזו היא מודל פשוט שממחיש את העיקרון המורכב הזה בצורה ויזואלית ואינטואיטיבית.</p>
</div>

<script>
    // שיפורים בפונקציונליות ואינטראקציה

    const canvas = document.getElementById('coriolisCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const clearButton = document.getElementById('clearButton');
    const explanationButton = document.getElementById('explanationButton');
    const explanationDiv = document.getElementById('explanation');

    const rotationSpeedInput = document.getElementById('rotationSpeed');
    const rotationSpeedValueSpan = document.getElementById('rotationSpeedValue');
    const launchSpeedInput = document.getElementById('launchSpeed');
    const launchSpeedValueSpan = document.getElementById('launchSpeedValue');
    const launchAngleInput = document.getElementById('launchAngle');
    const launchAngleValueSpan = document.getElementById('launchAngleValue');
    const startRadiusInput = document.getElementById('startRadius');
    const startRadiusValueSpan = document.getElementById('startRadiusValue');
     const showLaunchPointCheckbox = document.getElementById('showLaunchPoint');


    const width = canvas.width = 350; // גודל קנבס חדש
    const height = canvas.height = 350;
    const center = { x: width / 2, y: height / 2 };
    const diskRadius = width / 2 - 10; // קצת פחות מחצי כדי לאפשר מסגרת וצל

    let rotationAngle = 0; // Current rotation angle of the disk (radians)
    let rotationSpeed = parseFloat(rotationSpeedInput.value); // radians per time step
    let ball = null; // { x: inertialX, y: inertialY, vx: inertialVx, vy: inertialVy, path: [] }
    let animationFrameId = null;
    let time = 0;
    const timeStep = 0.02; // קצב התקדמות זמן עדין יותר
    const physicsSpeedScale = 0.5; // קבוע התאמה לפיזיקה לעומת פיקסלים
    const ballRadius = 6; // רדיוס הכדור

    // Update parameter value displays and variables
    const updateParams = () => {
        rotationSpeed = parseFloat(rotationSpeedInput.value);
        rotationSpeedValueSpan.textContent = rotationSpeed.toFixed(1);

        // Update other spans directly
        launchSpeedValueSpan.textContent = parseFloat(launchSpeedInput.value).toFixed(1);
        launchAngleValueSpan.textContent = launchAngleInput.value;
        startRadiusValueSpan.textContent = startRadiusInput.value;

        // If ball is not null and simulation is running, maybe update mid-sim?
        // Let's decide not to allow changing params mid-sim for simplicity.
        // Just update the displays and redraw the static elements (like potential launch point).
        if (!ball) {
             draw(); // Redraw with potentially new launch point/radius visuals
        }
    };

    rotationSpeedInput.oninput = updateParams;
    launchSpeedInput.oninput = updateParams;
    launchAngleInput.oninput = updateParams;
    startRadiusInput.oninput = updateParams;
     showLaunchPointCheckbox.onchange = draw; // Redraw when checkbox changes

    // Function to convert rotating frame coords (relative to disk center) to canvas coords
    // y-axis is inverted in canvas compared to standard Cartesian
    function rotatingToCanvas(pos_rotating) {
        return {
            x: center.x + pos_rotating.x,
            y: center.y - pos_rotating.y
        };
    }

    // Function to convert canvas coords to rotating frame coords (relative to disk center)
     function canvasToRotating(pos_canvas) {
          return {
              x: pos_canvas.x - center.x,
              y: center.y - pos_canvas.y
          };
     }

     // Convert inertial coords to rotating coords at a specific disk angle
     function inertialToRotating(pos_inertial, angle) {
         const cosA = Math.cos(-angle); // Rotate back by disk angle
         const sinA = Math.sin(-angle);
         return {
             x: pos_inertial.x * cosA - pos_inertial.y * sinA,
             y: pos_inertial.x * sinA + pos_inertial.y * cosA
         };
     }


    function drawDisk() {
        ctx.save();
        ctx.translate(center.x, center.y);

        // Draw disk body
        ctx.beginPath();
        ctx.arc(0, 0, diskRadius, 0, Math.PI * 2);
        const diskGradient = ctx.createRadialGradient(0, 0, 0, 0, 0, diskRadius);
        diskGradient.addColorStop(0, '#e3f2fd'); // Lighter blue center
        diskGradient.addColorStop(1, '#90caf9'); // Darker blue edge
        ctx.fillStyle = diskGradient;
        ctx.fill();
        ctx.strokeStyle = '#64b5f6'; // Medium blue border
        ctx.lineWidth = 3;
        ctx.stroke();

        // Draw grid lines (visualize rotation)
        ctx.rotate(rotationAngle); // Rotate the grid lines
        ctx.strokeStyle = '#bbdefb'; // Light blue grid
        ctx.lineWidth = 1;

        // Draw radial lines
        const numRadialLines = 16; // יותר קווים רדיאליים
        for(let i=0; i<numRadialLines; i++) {
            const angle = (i / numRadialLines) * Math.PI * 2;
            ctx.beginPath();
            ctx.moveTo(0, 0);
            ctx.lineTo(diskRadius * Math.cos(angle), diskRadius * Math.sin(angle));
            ctx.stroke();
        }

        // Draw concentric circles
        const numConcentricCircles = 5; // יותר מעגלים
        for(let r = diskRadius / numConcentricCircles; r <= diskRadius; r += diskRadius / numConcentricCircles) {
            ctx.beginPath();
            ctx.arc(0, 0, r, 0, Math.PI * 2);
            ctx.stroke();
        }

        ctx.restore();

         // Draw center dot
        ctx.beginPath();
        ctx.arc(center.x, center.y, 4, 0, Math.PI * 2); // גודל גדול יותר
        ctx.fillStyle = '#212121'; // כמעט שחור
        ctx.fill();
    }

    function drawBall(ball) {
        if (!ball) return;

        // Calculate ball position in the inertial frame
        const inertialX = ball.x + ball.vx * time;
        const inertialY = ball.y + ball.vy * time;

        // Convert inertial coords to rotating coords relative to the disk's current rotation
        const rotatingPos = inertialToRotating({x: inertialX, y: inertialY}, rotationAngle);

        // Convert rotating coords to canvas coords for drawing
        const ballCanvasPos = rotatingToCanvas(rotatingPos);

        // Check if ball is outside disk radius (with tolerance)
        const distanceToCenter = Math.sqrt(rotatingPos.x*rotatingPos.x + rotatingPos.y*rotatingPos.y);
        const isOutside = distanceToCenter > diskRadius + ballRadius / 2; // Add buffer

        // Store path point ONLY if inside the disk
        if (!isOutside) {
             ball.path.push({ x: rotatingPos.x, y: rotatingPos.y });
        } else {
            // If outside, stop simulation and mark exit point
            stopSimulation();
             ball.exitPos = { ...ballCanvasPos }; // Store where it exited in canvas coords
             ball.exitTime = time; // Store time of exit
        }


        // Draw path (only drawing valid path points)
        ctx.beginPath();
        if (ball.path.length > 0) {
             const firstCanvasPos = rotatingToCanvas(ball.path[0]);
             ctx.moveTo(firstCanvasPos.x, firstCanvasPos.y);
             for (let i = 1; i < ball.path.length; i++) {
                 const p = rotatingToCanvas(ball.path[i]);
                 // Add subtle line animation/thickness change? (Complex with standard canvas lineTo)
                 // Let's just draw a clean path for now.
                 ctx.lineTo(p.x, p.y);
             }
        }
        ctx.strokeStyle = '#e91e63'; // ורוד עז לנתיב
        ctx.lineWidth = 3; // קו עבה יותר
        ctx.stroke();


        // Draw ball if inside
        if (!isOutside) {
            ctx.beginPath();
            ctx.arc(ballCanvasPos.x, ballCanvasPos.y, ballRadius, 0, Math.PI * 2);
             // Gradient for ball
            const ballGradient = ctx.createRadialGradient(ballCanvasPos.x, ballCanvasPos.y, 0, ballCanvasPos.x, ballCanvasPos.y, ballRadius);
            ballGradient.addColorStop(0, '#fff9c4'); // בהיר במרכז
            ballGradient.addColorStop(1, '#fbc02d'); // כתום-צהוב בקצוות
            ctx.fillStyle = ballGradient;
            ctx.fill();
            ctx.strokeStyle = '#f57f17'; // כתום כהה יותר
            ctx.lineWidth = 1.5;
            ctx.stroke();
        } else if (ball.exitPos) {
            // Draw exit marker if ball went outside and exitPos is set
            drawExitMarker(ball.exitPos);
        }
    }

    function drawLaunchPoint(startR) {
         if (!showLaunchPointCheckbox.checked) return;

         // Draw launch point only when simulation is NOT running (ball is null)
         if (ball) return;

         // The standard launch point is on the positive X axis of the *inertial* frame at t=0
         // which is aligned with the rotating frame at t=0.
         // So, in the current rotating frame (angle `rotationAngle`), this point is:
         const initialX_inertial = startR;
         const initialY_inertial = 0;

         // Convert initial inertial position to current rotating position
         const rotatingPos = inertialToRotating({x: initialX_inertial, y: initialY_inertial}, rotationAngle);
         const canvasPos = rotatingToCanvas(rotatingPos);


         // Draw a marker at the launch point
         ctx.beginPath();
         ctx.arc(canvasPos.x, canvasPos.y, ballRadius + 3, 0, Math.PI * 2); // Larger circle than ball
         ctx.strokeStyle = '#f44336'; // אדום
         ctx.lineWidth = 2;
         ctx.setLineDash([5, 5]); // קו מקווקו
         ctx.stroke();
         ctx.setLineDash([]); // Reset line dash
    }

    function drawExitMarker(pos) {
        ctx.save();
        ctx.translate(pos.x, pos.y);
        ctx.strokeStyle = '#f44336'; // אדום
        ctx.lineWidth = 3;
        // Draw an X
        const markerSize = 10;
        ctx.beginPath();
        ctx.moveTo(-markerSize, -markerSize);
        ctx.lineTo(markerSize, markerSize);
        ctx.moveTo(markerSize, -markerSize);
        ctx.lineTo(-markerSize, markerSize);
        ctx.stroke();
        ctx.restore();
    }


    function draw() {
         ctx.clearRect(0, 0, width, height);
         drawDisk();
         if (ball) {
              drawBall(ball);
         } else {
             // If no simulation is running, draw the potential launch point marker
             const startR = parseFloat(startRadiusInput.value);
             drawLaunchPoint(startR);
         }
    }


    function updateSimulation() {
        // Update disk rotation
        // Scale rotation speed and time step
        rotationAngle += rotationSpeed * timeStep;
        if (rotationAngle > Math.PI * 2) rotationAngle -= Math.PI * 2;
        if (rotationAngle < 0) rotationAngle += Math.PI * 2; // Handle negative speeds if allowed

        // Increment time for ball movement
        time += timeStep;

        // Redraw everything
        draw();

        // Continue animation only if ball is still in simulation (checked inside drawBall)
        if (ball && !ball.exitPos) { // Continue only if ball exists and hasn't exited
            animationFrameId = requestAnimationFrame(updateSimulation);
        } else {
             // Simulation ended, maybe draw final state more clearly?
             // draw function already handles drawing the exit marker if it exists.
        }
    }

    function startSimulation() {
        if (animationFrameId) {
            stopSimulation(); // Stop any running simulation
        }

        // Get parameters from inputs
        const speed = parseFloat(launchSpeedInput.value) * physicsSpeedScale; // Apply scaling
        const angleDegrees = parseFloat(launchAngleInput.value);
        const angleRadians = angleDegrees * Math.PI / 180;
        const startR = parseFloat(startRadiusInput.value); // starting distance from center

        // Initial position in inertial frame (starts aligned with rotating frame at t=0)
        // Let's assume initial launch position is on the positive X axis of the *inertial* frame at t=0, at distance startR
        const initialX_inertial = startR;
        const initialY_inertial = 0;

        // Velocity components in inertial frame
        // The launch angle is relative to the *inertial* frame's x-axis.
        const velocityX_inertial = speed * Math.cos(angleRadians);
        const velocityY_inertial = speed * Math.sin(angleRadians);

         // Check if launch point is outside the disk radius initially
         if (startR > diskRadius) {
             alert("נקודת השיגור מחוץ לגלובוס! בחר רדיוס קטן יותר.");
             return; // Don't start simulation
         }

        ball = {
            x: initialX_inertial, // Initial x position in inertial frame at t=0
            y: initialY_inertial, // Initial y position in inertial frame at t=0
            vx: velocityX_inertial, // Velocity x in inertial frame
            vy: velocityY_inertial, // Velocity y in inertial frame
            path: [], // Store path in rotating frame coordinates
             exitPos: null, // To store the position where the ball exited
             exitTime: null // To store the time when the ball exited
        };

        rotationAngle = 0; // Start disk rotation from 0
        time = 0; // Reset time for simulation

        // Start animation loop
        animationFrameId = requestAnimationFrame(updateSimulation);
    }

    function stopSimulation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
    }

    function clearSimulation() {
        stopSimulation();
        ball = null;
        time = 0;
        rotationAngle = 0; // Reset rotation for clear state
        draw(); // Redraw empty disk and potential launch point
    }

    startButton.addEventListener('click', startSimulation);
    clearButton.addEventListener('click', clearSimulation);

    explanationButton.addEventListener('click', () => {
        const isHidden = !explanationDiv.classList.contains('visible');
        if (isHidden) {
            explanationDiv.style.display = 'block'; // Make it block to allow transition
             // Force reflow to make the transition work
            explanationDiv.offsetHeight;
            explanationDiv.classList.add('visible');
             explanationButton.textContent = 'הסתר הסבר';
        } else {
             explanationDiv.classList.remove('visible');
             explanationButton.textContent = 'הצג לי את הסוד!';
            // Hide completely after transition
            explanationDiv.addEventListener('transitionend', function handler() {
                 if (!explanationDiv.classList.contains('visible')) {
                     explanationDiv.style.display = 'none';
                     explanationDiv.removeEventListener('transitionend', handler);
                 }
            });
        }
    });


    // Initial draw of the disk and potential launch point when page loads
    draw();

     // Initial parameter value display
     updateParams();

     // Make sure explanation is hidden on load
     explanationDiv.style.display = 'none';
</script>