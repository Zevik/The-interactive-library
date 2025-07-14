---
title: "כנפי פרפר: מסע כאוטי מנקודה לנקודה"
english_slug: butterfly-effect-tiny-change-huge-impact
category: "פיזיקה"
tags: [כאוס, אפקט-הפרפר, רגישות-לתנאי-התחלה, סימולציה, מערכות-דינמיות]
---
<div class="page-container">
    <h1>כנפי פרפר: מסע כאוטי מנקודה לנקודה</h1>
    <p class="intro-text">איך שינוי קטנטן בנקודת ההתחלה יכול לשגר אתכם למסלול שונה לגמרי? היכנסו לעולם של כאוס ותראו במו עיניכם איך תזוזה זעירה אחת יוצרת דרמה אדירה בהמשך הדרך. זו לא קסם, זו פיזיקה במלוא הפלא שלה!</p>

    <div id="app-container">
        <canvas id="chaosCanvas" width="600" height="600"></canvas>
        <div id="controls">
            <p id="instructions" class="instruction-text">המשימה שלך: לחץ איפשהו על הלוח כדי לבחור את נקודת ההתחלה הראשונה (מסלול כחול מסתורי)</p>
            <button id="resetButton" class="control-button" style="display: none;">התחל סימולציה חדשה!</button>
        </div>
    </div>

    <button id="showExplanationButton" class="explanation-button">מה לעזאזל קרה פה? הצג הסבר!</button>
    <div id="explanation" class="explanation-panel" style="display: none;">
        <h2>הקסם (והכאוס) שמאחורי הקלעים</h2>
        <h3>מה זו בעצם מערכת דינמית כאוטית?</h3>
        <p>תארו לכם מערכת שמתפתחת בזמן לפי כללים קשיחים (נוסחאות, חוקי טבע...). מערכת כזו נקראת דינמית. אם ההתפתחות שלה <strong>צפויה לחלוטין</strong> אם יודעים את נקודת ההתחלה <strong>בדיוק אינסופי</strong>, אבל בפועל נראית <strong>בלתי צפויה לחלוטין</strong> גם אם המדידה כמעט מושלמת – זו מערכת כאוטית! כן, גם מערכות פשוטות יכולות להיות כאלה.</p>
        <h3>רגישות לתנאי התחלה: הלב הפועם של הכאוס</h3>
        <p>זה הסוד הגדול: במערכת כאוטית, הבדל <strong>זעיר עד בלתי נתפס</strong> בנקודת ההתחלה הופך במהירות להבדל <strong>עצום ודרמטי</strong> במצב המערכת לאחר זמן מה. הדמיון בין שני מסלולים דועך בקצב מטורף (אקספוננציאלי). זו הסיבה שאנחנו לא יכולים לחזות מערכות כאוטיות לטווח ארוך.</p>
        <h3>אפקט הפרפר: השם האמנותי לתופעה</h3>
        <p>המתמטיקאי אדוארד לורנץ הדביק לתופעה את השם הציורי והמפורסם "אפקט הפרפר". הרעיון הוא שמשהו קטן כמו נפנוף כנף של פרפר במקום אחד בעולם, יכול תיאורטית ליצור שרשרת תגובות שתוביל לשינויי מזג אוויר דרמטיים ואפילו לסופה במקום אחר לגמרי. מזג האוויר הוא דוגמה קלאסית למערכת כאוטית. דוגמאות נוספות כוללות שוק ההון (אאוצ'!), זרימת נוזלים סוערת, ואפילו תנועת כוכבים מסוימים.</p>
        <h3>הדגמה חיה בסימולציה: ראו איך הקסם קורה (והורס את התחזית)</h3>
        <p>הסימולציה שלפניכם היא כמו צעצוע מתמטי שמדגים כאוס. בחרתם שתי נקודות על המסך שהיו <strong>סופר קרובות</strong> בהתחלה. נכון? ובכל זאת, ראיתם איך המסלולים שהתפתחו מהן <strong>התפצלו במהירות מסחררת</strong>! תוך רגעים ספורים, שני ה"גורלות" של הנקודות היו שונים לגמרי. זה בדיוק, אבל בדיוק, אפקט הפרפר בפעולה ויזואלית.</p>
        <h3>השלכות רחבות: למה תחזיות מזג אוויר ל-3 שבועות הן פנטזיה?</h3>
        <p>הבנת הכאוס והרגישות לתנאי התחלה מסבירה למה יש גבול מובנה ליכולת שלנו לחזות מערכות כאוטיות. מכיוון שאין לנו (ולעולם לא תהיה לנו) מדידה מושלמת לחלוטין של מצב העולם (או האטמוספירה, או השוק) ברגע נתון, כל שגיאה קטנה במדידה ההתחלתית גדלה בקצב אקספוננציאלי. לכן, תחזית מזג אוויר מדויקת ליומיים? סביר. לשבועיים? בערך. לחודש? תשכחו מזה. אפקט הפרפר הוא גם הסיבה לזה!</p>
    </div>
</div>

<style>
    /* גופנים ואסתטיקה כללית */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    :root {
        --primary-color: #007bff; /* כחול חי */
        --secondary-color: #dc3545; /* אדום דומיננטי */
        --accent-color: #ffc107; /* צהוב הדגשה */
        --background-light: #f8f9fa; /* רקע בהיר */
        --background-panel: #e9ecef; /* רקע פאנלים */
        --text-color: #343a40; /* צבע טקסט כהה */
        --border-color: #ced4da; /* צבע מסגרת עדין */
        --canvas-bg: #ffffff; /* רקע קנבס לבן */
        --path1-color: #007bff; /* כחול למסלול 1 */
        --path2-color: #dc3545; /* אדום למסלול 2 */
    }

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-light);
        margin: 0;
        padding: 20px;
        direction: rtl; /* כיווניות ימין-לשמאל */
        text-align: right;
    }

    .page-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #fff; /* רקע לבן לתוכן הראשי */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 12px;
    }

    h1, h2, h3 {
        color: #343a40; /* כהה יותר לכותרות */
        text-align: center;
        font-weight: 700;
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2.2em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        margin-bottom: 30px;
    }

    h2 {
        font-size: 1.8em;
        margin-bottom: 15px;
        color: var(--primary-color);
    }

    h3 {
        font-size: 1.4em;
        margin-top: 25px;
        margin-bottom: 10px;
        color: var(--secondary-color);
    }

    .intro-text {
        font-size: 1.1em;
        margin-bottom: 30px;
        text-align: center;
        color: #555;
    }

    #app-container {
        direction: rtl;
        text-align: right;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 10px;
        max-width: 640px; /* תואם רוחב קנבס + פדינג */
        background-color: var(--background-panel);
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    #chaosCanvas {
        border: 2px solid var(--text-color); /* מסגרת בולטת יותר */
        display: block;
        margin: 0 auto 20px; /* רווח גדול יותר מתחת */
        background-color: var(--canvas-bg);
        cursor: crosshair; /* סמן יפה לבחירה */
        border-radius: 5px; /* פינות מעוגלות לקנבס */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    #controls {
        text-align: center;
        font-size: 1.1em;
        min-height: 2em; /* שומר מקום למנוע קפיצות */
        display: flex; /* סידור פריטים במרכז */
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .instruction-text {
        margin-bottom: 15px; /* רווח תחתון מהכפתור */
        color: var(--text-color);
        font-weight: 400;
    }

    .control-button {
        padding: 10px 20px; /* פדינג נדיב יותר */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 5px; /* פינות מעוגלות */
        background-color: var(--primary-color);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציית ריחוף ולחיצה */
    }

    .control-button:hover {
        background-color: #0056b3; /* כהה יותר בריחוף */
        transform: translateY(-2px); /* אנימציית ריחוף קלה */
    }

    .control-button:active {
         background-color: #004085; /* כהה בלחיצה */
         transform: translateY(0); /* אנימציית לחיצה */
    }

    .explanation-button {
        display: block;
        margin: 30px auto; /* רווח נדיב מעל ומתחת */
        padding: 12px 25px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        background-color: var(--secondary-color); /* צבע אחר לכפתור הסבר */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .explanation-button:hover {
        background-color: #c82333;
        transform: translateY(-2px);
    }

     .explanation-button:active {
         background-color: #bd2130;
         transform: translateY(0);
    }


    .explanation-panel {
        direction: rtl;
        text-align: right;
        margin-top: 30px;
        padding: 25px; /* פדינג נדיב */
        border: 1px solid var(--border-color);
        border-radius: 10px;
        background-color: var(--background-panel);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: opacity 0.5s ease-in-out; /* אנימציית הופעה */
        opacity: 1; /* מתחיל גלוי (כשהוא מוצג) */
    }

    .explanation-panel.hidden {
        opacity: 0; /* הופך לשקוף */
        /* height: 0; */ /* אפשר להוסיף גם שינוי גובה אם רוצים אפקט פתיחה/סגירה */
        /* overflow: hidden; */
    }


    .explanation-panel p {
        line-height: 1.7;
        margin-bottom: 15px;
        font-size: 1.05em;
        color: #444;
    }

     .explanation-panel p:last-child {
         margin-bottom: 0;
     }

    /* אנימציה קלה לנקודה בלחיצה */
    @keyframes pulse {
        0% {
            transform: scale(1);
            opacity: 1;
        }
        50% {
            transform: scale(1.2);
            opacity: 0.5;
        }
        100% {
            transform: scale(1);
            opacity: 1;
        }
    }

</style>

<script>
    const canvas = document.getElementById('chaosCanvas');
    const ctx = canvas.getContext('2d');
    const instructions = document.getElementById('instructions');
    const resetButton = document.getElementById('resetButton');
    const showExplanationButton = document.getElementById('showExplanationButton');
    const explanationDiv = document.getElementById('explanation');
    const appContainer = document.getElementById('app-container');

    let state = 'waitingForP1'; // 'waitingForP1', 'waitingForP2', 'simulating'
    let p1 = null;
    let p2 = null;
    const simulationStepsPerFrame = 10; // Number of calculation steps per animation frame for speed
    const totalSteps = 1500; // Total number of steps for simulation
    let currentStep = 0;
    let path1History = [];
    let path2History = [];
    let currentPoint1 = null;
    let currentPoint2 = null;

    // Henon map parameters (standard chaotic values)
    const a = 1.4;
    const b = 0.3;

    // Mapping parameters for canvas -> Henon space
    // Approximate range for Henon attractor: x in [-1.5, 1.5], y in [-0.5, 0.5]
    const minHenonX = -1.5;
    const maxHenonX = 1.5;
    const minHenonY = -0.5;
    const maxHenonY = 0.5;
    const rangeHenonX = maxHenonX - minHenonX;
    const rangeHenonY = maxHenonY - minHenonY;

    function mapCanvasToHenon(canvasX, canvasY) {
        // Adjust for padding in app-container if necessary (not needed if using event.offsetX/Y directly on canvas)
        // Let's assume event.offsetX/Y relative to canvas for simplicity and better practice
        const henonX = (canvasX / canvas.width) * rangeHenonX + minHenonX;
        // Canvas Y is inverted, so we flip it
        const henonY = ((canvas.height - canvasY) / canvas.height) * rangeHenonY + minHenonY;
        return { x: henonX, y: henonY };
    }

    function mapHenonToCanvas(henonX, henonY) {
        const canvasX = ((henonX - minHenonX) / rangeHenonX) * canvas.width;
        // Canvas Y is inverted, so we flip it
        const canvasY = canvas.height - ((henonY - minHenonY) / rangeHenonY) * canvas.height;
        return { x: canvasX, y: canvasY };
    }

    function henonMap(point) {
        const nextX = 1 - a * point.x * point.x + point.y;
        const nextY = b * point.x;
        return { x: nextX, y: nextY };
    }

    function clearCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function drawPoint(point, color, radius = 4, pulsing = false) {
        if (!point) return;
        const canvasPoint = mapHenonToCanvas(point.x, point.y);
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(canvasPoint.x, canvasPoint.y, radius, 0, Math.PI * 2);
        ctx.fill();

        // Add pulsing effect for active point
        if (pulsing) {
             ctx.strokeStyle = color;
             ctx.lineWidth = 1.5;
             ctx.beginPath();
             // A simple pulsating circle outline
             const pulseRadius = radius + Math.sin(currentStep * 0.2) * 2; // Use sin for smooth pulse
             ctx.arc(canvasPoint.x, canvasPoint.y, pulseRadius, 0, Math.PI * 2);
             ctx.stroke();
        }
    }

    function drawPathHistory(pathHistory, color) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 0.5; // Faint path history
        ctx.beginPath();
        if (pathHistory.length > 0) {
            const startCanvas = mapHenonToCanvas(pathHistory[0].x, pathHistory[0].y);
            ctx.moveTo(startCanvas.x, startCanvas.y);
            for (let i = 1; i < pathHistory.length; i++) {
                const currentCanvas = mapHenonToCanvas(pathHistory[i].x, pathHistory[i].y);
                ctx.lineTo(currentCanvas.x, currentCanvas.y);
            }
        }
        ctx.stroke();
    }

    function updateSimulation() {
        if (state !== 'simulating' || currentStep >= totalSteps) {
            if (currentStep >= totalSteps) {
                 instructions.textContent = "וואו! הסימולציה הסתיימה. המסלולים התפצלו לגמרי! לחץ 'התחל סימולציה חדשה' כדי לנסות שוב או קרא את ההסבר.";
                 canvas.style.cursor = 'default';
                 resetButton.style.display = 'block'; // Ensure button is visible at the end
            }
            return;
        }

        // Calculate multiple steps per frame
        for (let i = 0; i < simulationStepsPerFrame && currentStep < totalSteps; i++) {
             if (currentStep === 0) {
                currentPoint1 = p1;
                currentPoint2 = p2;
                path1History.push(p1);
                path2History.push(p2);
            } else {
                currentPoint1 = henonMap(currentPoint1);
                currentPoint2 = henonMap(currentPoint2);
                path1History.push(currentPoint1);
                path2History.push(currentPoint2);
            }
            currentStep++;
        }


        // Draw
        clearCanvas();
        // Draw history faintly
        drawPathHistory(path1History, 'rgba(0, 123, 255, 0.3)'); // Faint blue
        drawPathHistory(path2History, 'rgba(220, 53, 69, 0.3)'); // Faint red

        // Draw current points prominently, maybe with a trail effect
        const trailLength = 10; // Number of recent points to draw as trail
         for (let i = 0; i < trailLength; i++) {
             const p1Index = path1History.length - 1 - i;
             const p2Index = path2History.length - 1 - i;
             if (p1Index >= 0) {
                 const opacity = 1 - (i / trailLength); // Fade out old points
                 drawPoint(path1History[p1Index], `rgba(0, 123, 255, ${opacity})`, 3 + (trailLength - i) * 0.2); // Size decreases with age
             }
             if (p2Index >= 0) {
                  const opacity = 1 - (i / trailLength);
                 drawPoint(path2History[p2Index], `rgba(220, 53, 69, ${opacity})`, 3 + (trailLength - i) * 0.2);
             }
         }


        // Draw the very tip of the path/current location more prominently
        drawPoint(currentPoint1, var(--path1-color), 6, true); // Current points pulse
        drawPoint(currentPoint2, var(--path2-color), 6, true);


        animationFrameId = requestAnimationFrame(updateSimulation);
    }

    function reset() {
        cancelAnimationFrame(animationFrameId);
        state = 'waitingForP1';
        p1 = null;
        p2 = null;
        currentStep = 0;
        path1History = [];
        path2History = [];
        currentPoint1 = null;
        currentPoint2 = null;
        clearCanvas();
        instructions.textContent = "המשימה שלך: לחץ איפשהו על הלוח כדי לבחור את נקודת ההתחלה הראשונה (מסלול כחול מסתורי)";
        resetButton.style.display = 'none';
        canvas.style.cursor = 'crosshair';
         // Hide explanation if visible? Maybe not, user might want it open for context.
         // explanationDiv.style.display = 'none';
         // showExplanationButton.textContent = 'מה לעזאזל קרה פה? הצג הסבר!';
    }

    canvas.addEventListener('click', (event) => {
        if (state === 'simulating') return; // Ignore clicks during simulation

        const rect = canvas.getBoundingClientRect();
        const canvasX = event.offsetX; // Use offsetX/Y relative to padding box
        const canvasY = event.offsetY;
        const henonPoint = mapCanvasToHenon(canvasX, canvasY);

        if (state === 'waitingForP1') {
            p1 = henonPoint;
             // Visual feedback on click location
            drawPoint(p1, var(--path1-color), 6, true); // Draw initial point with pulse
            instructions.textContent = "מצוין! עכשיו לחץ לבחירת נקודה שנייה. נסה לבחור נקודה 🤏 ממש קרוב 🤏 לראשונה! (מסלול אדום סוער)";
            state = 'waitingForP2';
        } else if (state === 'waitingForP2') {
            p2 = henonPoint;
            // Visual feedback on click location
            drawPoint(p2, var(--path2-color), 6, true); // Draw initial point with pulse
            instructions.textContent = "יופי! תתכונן... מדגימים את אפקט הפרפר! עקוב אחר התפצלות המסלולים...";
            state = 'simulating';
            resetButton.style.display = 'block';
            canvas.style.cursor = 'default'; // Change cursor during sim
            setTimeout(updateSimulation, 500); // Small delay before starting animation
        }
    });

    resetButton.addEventListener('click', reset);

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        if (isHidden) {
            explanationDiv.style.opacity = '0'; // Start hidden/transparent for fade-in
            explanationDiv.style.display = 'block';
            setTimeout(() => {
                explanationDiv.style.opacity = '1'; // Fade in
            }, 10); // Small delay to allow display:block to take effect
            showExplanationButton.textContent = 'הבנתי! הסתר הסבר';
        } else {
             explanationDiv.style.opacity = '0'; // Fade out
             // Wait for transition to finish before hiding completely
             explanationDiv.addEventListener('transitionend', function handler() {
                 explanationDiv.style.display = 'none';
                 explanationDiv.removeEventListener('transitionend', handler);
             });
            showExplanationButton.textContent = 'מה לעזאזל קרה פה? הצג הסבר!';
        }
    });

    // Initial state setup
    reset();

    // Add resize listener to potentially handle responsiveness, though canvas is fixed size
    // window.addEventListener('resize', () => {
    //     // Handle resizing if needed, e.g., re-center canvas or scale
    // });

</script>
```