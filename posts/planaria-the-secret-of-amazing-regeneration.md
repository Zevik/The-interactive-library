---
title: "פלאנריה: סוד ההתחדשות המדהימה"
english_slug: planaria-the-secret-of-amazing-regeneration
category: "מדעי החיים / ביולוגיה"
tags:
  - פלאנריה
  - תולעים שטוחות
  - רגנרציה
  - מחזור חיים
  - ביולוגיה התפתחותית
---
<div class="app-intro">
    <h1>פלאנריה: סוד ההתחדשות המדהימה</h1>
    <p>דמיינו עולם בו איבר חתוך פשוט יכול לצמוח בחזרה! מה שנשמע כמו פנטזיה הופך למציאות מרתקת אצל יצור קטן אחד - תולעת הפלאנריה. היא מומחית בלהצמיח מחדש חלקים שלמים מגופה, מראש ועד זנב. <strong>בואו לגלות איך זה עובד - נסו בעצמכם!</strong></p>
</div>

<div class="planaria-app-container interactive-section">
    <div class="controls">
        <button id="tool-cut" class="active">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><line x1="20" y1="6" x2="10" y2="6"></line><line x1="14" y1="18" x2="4" y2="18"></line><line x1="20" y1="12" x2="10" y2="12"></line></svg>
            כלי חיתוך
        </button>
        <button id="tool-reset">
             <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.65 6.35a7.958 7.958 0 0 0-11.02 0L2 12h4"></path><path d="M6.35 17.65a7.958 7.958 0 0 0 11.02 0L22 12h-4"></path></svg>
             אתחל
        </button>
        <div class="timeline-controls">
            <button id="timeline-play-pause" disabled>
                 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                 התחל רגנרציה
             </button>
            <span id="timeline-status">הפלאנריה ממתינה לחיתוך</span>
        </div>
    </div>
    <div id="planaria-area">
        <canvas id="planaria-canvas"></canvas>
        <div id="cut-line" class="cut-line"></div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-explanation-button">הצג סודות התחדשות הפלאנריה</button>

<div id="explanation-content" class="explanation-section" style="display: none;">
    <div class="explanation-inner">
        <h2>הסבר מעמיק: פלאנריה והתחדשות</h2>

        <h3>הכירו את הפלאנריה: תולעת-העל של הטבע</h3>
        <p>פלאנריה היא תולעת שטוחה (שייכת למערכת התולעים השטוחות, Platyhelminthes) שחיה לרוב במים מתוקים. היא נראית פשוטה, עם גוף שטוח ומוארך, ראש עם שני כתמי עין שרגישים לאור ומערכת עצבים ראשונית מרוכזת בקדמת הגוף. היא ציידת קטנה או ניזונה משאריות.</p>

        <h3>מחזור החיים: לא רק סקס, גם פיצול!</h3>
        <p>לפלאנריה שתי דרכים מרתקות להתרבות:</p>
        <ul>
            <li><strong>רבייה מינית:</strong> למרות שהיא הרמפרודיטית (יש לה איברי רבייה זכריים ונקביים), היא בדרך כלל מחליפה תאי מין עם פלאנריה אחרת. הביצים נשמרות בפקעת מיוחדת.</li>
            <li><strong>רבייה אל-מינית:</strong> והנה החלק המעניין! פלאנריה יכולה פשוט להתפצל לשניים, לרוב באמצע הגוף. כל חלק ממשיך להתקיים באופן עצמאי ומשלים את החלק החסר. זו לא רק רבייה - זו הדגמה חיה ליכולת ההתחדשות הפנומנלית שלה!</li>
        </ul>

        <h3>הכוח הסודי: רגנרציה מדהימה</h3>
        <p>הסופר-כוח של הפלאנריה הוא היכולת שלה לשקם כל חלק בגופה שנחתך או ניזוק. מפיסה קטנה יחסית, אפילו רק 1/279 מגודל הגוף המקורי (!) - בתנאי שיש בה מספיק תאים מיוחדים - יכול לצמוח מחדש יצור שלם ותקין לחלוטין. דמיינו ראש צומח לזנב, או זנב מצמיח ראש, ואפילו חצי גוף שמצמיח את החצי השני!</p>

        <h3>מאחורי הקסם: תאי הגזע הבלתי-מנוצחים (נאובלסטים)</h3>
        <p>הסוד הגדול של הפלאנריה טמון ב"צוות השיפוצים" הפנימי שלה: אוכלוסייה ענקית של תאי גזע פלוריפוטנטיים הנקראים <strong>נאובלסטים (Neoblasts)</strong>. תאים אלו הם קסם של ממש – הם מפוזרים בכל הגוף ויכולים להפוך לכל סוג תא אחר בפלאנריה. כשיש "פציעה" (או חיתוך), הנאובלסטים נוהרים לאזור, מתחילים להתחלק במהירות שיא, ומתמיינים לרקמות ואיברים שחסרים, בונים מחדש את הגוף כמו פאזל ביולוגי מדהים. כל זה קורה תחת ניצוח מדויק של מולקולות ואותות כימיים.</p>

        <h3>ראו בעצמכם: סוגי חיתוך ורגנרציה</h3>
        <p>
        <ul>
            <li><strong>חיתוך רוחבי:</strong> אם חותכים פלאנריה לשניים לרוחב, החלק הקדמי (ראש) ישלים זנב חדש, והחלק האחורי (זנב) ישלים ראש חדש. כל אחד הופך לפלאנריה שלמה!</li>
            <li><strong>חיתוך אורכי:</strong> חיתוך הפלאנריה לאורך, בדרך כלל במרכז, יגרום לכל חצי לשקם את החצי השני שחסר לו, וליצור שתי פלאנריות זהות.</li>
        </ul>
        </p>

        <h3>למה חוקרים אוהבים פלאנריה?</h3>
        <p>הפלאנריה היא מודל מחקר מושלם להבנת תהליכי התפתחות, שיקום וריפוי. חקר הנאובלסטים והאותות המולקולריים המנהלים את הרגנרציה שלה יכול לפתוח דלתות עצומות ברפואה - מפיתוח דרכים לריפוי פצעים כרוניים ושיקום רקמות פגועות, ועד לחלום על רגנרציה של איברים אצל בני אדם.</p>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #28a745; /* Green */
        --background-light: #e0ffe0; /* Very light green */
        --background-container: #ffffff; /* White/light grey */
        --border-color: #cccccc;
        --text-color: #333;
        --heading-color: #0056b3; /* Darker blue */
        --hover-color: #0056b3;
        --active-color: #004085;
        --regeneration-color: #5a9b5a; /* Planaria body green */
        --cut-line-color: #dc3545; /* Red */
    }

    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: var(--text-color);
        background-color: #f4f7f6; /* Soft background */
        padding: 20px;
    }

    h1, h2, h3 {
        color: var(--heading-color);
        margin-bottom: 10px;
    }

    h1 {
        text-align: center;
        margin-bottom: 20px;
        color: var(--primary-color);
    }

    .app-intro {
        max-width: 800px;
        margin: 20px auto;
        padding: 0 15px;
        text-align: center;
    }

    .interactive-section, .explanation-section {
        max-width: 800px;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--background-container);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    .controls {
        margin-bottom: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        flex-wrap: wrap;
    }

    .controls button {
        padding: 10px 18px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        background-color: var(--primary-color);
        color: white;
        font-size: 1rem;
        transition: background-color 0.2s ease, transform 0.1s ease;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .controls button svg {
        width: 18px;
        height: 18px;
        stroke: white;
    }

    .controls button:hover:not(:disabled) {
        background-color: var(--hover-color);
        transform: translateY(-1px);
    }

     .controls button:active:not(:disabled) {
        background-color: var(--active-color);
        transform: translateY(0);
    }

    .controls button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.8;
    }

    .controls button.active {
        background-color: var(--active-color);
    }

    .controls .timeline-controls {
        display: flex;
        align-items: center;
        gap: 10px;
        min-width: 200px; /* Give it some space */
        justify-content: center;
    }

     #timeline-status {
         font-size: 0.9rem;
         color: var(--text-color);
         min-width: 120px; /* Prevent layout shifts */
         text-align: left;
     }

    #planaria-area {
        width: 100%;
        aspect-ratio: 16 / 9; /* Maintain aspect ratio */
        max-height: 350px; /* Max height limit */
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative; /* Needed for cut line positioning */
        overflow: hidden;
        background-color: var(--background-light); /* Water background */
        border: 1px solid var(--border-color);
        border-radius: 5px;
    }

    #planaria-canvas {
        display: block; /* Remove extra space below canvas */
         width: 100%; /* Canvas fills the area */
         height: 100%;
    }

     .cut-line {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none; /* Allow clicks to go through to canvas */
         border: 1px dashed var(--cut-line-color); /* Example style, drawn in JS */
         box-sizing: border-box;
         display: none; /* Hidden by default */
     }


    .toggle-explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        background-color: var(--secondary-color);
        color: white;
        font-size: 1.1rem;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .toggle-explanation-button:hover {
        background-color: #218838;
        transform: translateY(-1px);
    }
     .toggle-explanation-button:active {
        background-color: #1e7e34;
        transform: translateY(0);
    }

    .explanation-section {
        margin-top: 20px;
    }

    .explanation-section h2,
    .explanation-section h3 {
        color: var(--heading-color);
        margin-top: 15px;
    }

    .explanation-section p,
    .explanation-section ul {
        line-height: 1.7;
        margin-bottom: 12px;
        color: var(--text-color);
    }
    .explanation-section ul {
        padding-right: 25px;
        list-style: disc;
    }
     .explanation-section li {
         margin-bottom: 8px;
     }

     .explanation-section strong {
         color: var(--heading-color);
     }

     /* Add some polish to the canvas drawing */
     #planaria-canvas {
         /* Ensure smooth edges if needed, though canvas handles it mostly */
         /* image-rendering: optimizeSpeed; */
         /* image-rendering: pixelated; */
     }

</style>

<script>
    const canvas = document.getElementById('planaria-canvas');
    const ctx = canvas.getContext('2d');
    const cutToolBtn = document.getElementById('tool-cut');
    const resetBtn = document.getElementById('tool-reset');
    const playPauseBtn = document.getElementById('timeline-play-pause');
    const timelineStatus = document.getElementById('timeline-status');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationContent = document.getElementById('explanation-content');
    const cutLineOverlay = document.getElementById('cut-line'); // Use overlay for drawing cut line


    let planariaParts = [];
    let currentTool = 'cut'; // Can add other tools later
    let cutting = false;
    let cutStartPos = { x: 0, y: 0 };
    let cutEndPos = { x: 0, y: 0 };
    let animationFrameId = null;
    let animationStartTime = null;
    const animationDuration = 8000; // 8 seconds for regeneration (slower, more dramatic)
    let isPaused = false;
    let pauseStartTime = 0;

    const COLORS = {
        body: '#5a9b5a', // Planaria body green
        growingBody: '#8fbc8f', // Lighter green for growing part
        eyespot: '#202020' // Dark grey/black
    };

    // Reference sizes of the *initial* full planaria, centered in canvas area
    let initialPlanaria = { x: 0, y: 0, width: 0, height: 0 };

    function getCanvasSize() {
         const container = document.getElementById('planaria-area');
         // Use container dimensions for canvas size
         const containerWidth = container.clientWidth;
         const containerHeight = container.clientHeight;
         canvas.width = containerWidth;
         canvas.height = containerHeight;
         return { width: canvas.width, height: canvas.height };
    }

    function calculateInitialPlanariaSize() {
        const { width, height } = getCanvasSize();
        // Calculate size and position for a single planaria, centered
        const baseWidth = Math.min(width * 0.8, 400); // Max width 400
        const baseHeight = Math.min(height * 0.8, 200); // Max height 200

        initialPlanaria.width = baseWidth;
        initialPlanaria.height = baseHeight;
        initialPlanaria.x = (width - baseWidth) / 2;
        initialPlanaria.y = (height - baseHeight) / 2;
    }

    function initPlanaria() {
        getCanvasSize(); // Set canvas dimensions
        calculateInitialPlanariaSize(); // Calculate where the initial planaria should be

        planariaParts = [{
            x: initialPlanaria.x,
            y: initialPlanaria.y,
            width: initialPlanaria.width,
            height: initialPlanaria.height,
            partType: 'full', // 'full', 'head', 'tail', 'middle-left', 'middle-right'
            regenerationProgress: 0, // 0 = just cut, 1 = fully regenerated
            animationStart: null // Timestamp when animation started for this part
        }];

        drawScene();
        resetCutVisuals();
        playPauseBtn.textContent = 'התחל רגנרציה';
        timelineStatus.textContent = 'הפלאנריה ממתינה לחיתוך';
        playPauseBtn.disabled = true; // Disable play until cut
        isPaused = false;
        pauseStartTime = 0;
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
    }

    function drawScene() {
        const { width, height } = getCanvasSize(); // Recalculate in case of resize
        ctx.clearRect(0, 0, width, height); // Clear canvas

        // Draw background (handled by CSS on #planaria-area)

        planariaParts.forEach(part => {
            drawPlanaria(part);
        });

        // Cut line is now drawn by CSS overlay managed by JS
    }

    function drawPlanaria(part) {
        ctx.save();
        ctx.translate(part.x, part.y); // Translate to the part's starting position

        const { width, height, partType, regenerationProgress } = part;
        const fullWidth = initialPlanaria.width; // Reference to full size before cut
        const fullHeight = initialPlanaria.height; // Reference to full size before cut

        // Calculate the size and position of the *current* shape during growth
        let currentShapeWidth = width;
        let currentShapeHeight = height;
        let offsetX = 0; // Offset for drawing the shape within the part's bounding box
        let offsetY = 0; // Offset for drawing the shape within the part's bounding box

        let isGrowing = regenerationProgress > 0 && regenerationProgress < 1;

        if (isGrowing) {
            ctx.fillStyle = COLORS.growingBody; // Use lighter color for growing part
             ctx.strokeStyle = COLORS.eyespot;

            if (partType === 'head') { // Growing tail onto head (height increases downwards)
                currentShapeHeight = height + (fullHeight - height) * regenerationProgress;
                currentShapeWidth = width; // Width remains constant
                // Drawing starts at part.y, so no offsetY needed for downward growth

            } else if (partType === 'tail') { // Growing head onto tail (height increases upwards)
                currentShapeHeight = height + (fullHeight - height) * regenerationProgress;
                currentShapeWidth = width; // Width remains constant
                // The drawing origin (top-left of the growing shape) shifts upwards
                offsetY = -(currentShapeHeight - height);


            } else if (partType === 'middle-left') { // Growing right side (width increases rightwards)
                currentShapeWidth = width + (fullWidth - width) * regenerationProgress;
                currentShapeHeight = height; // Height remains constant
                // Drawing starts at part.x, no offsetX needed for rightward growth

            } else if (partType === 'middle-right') { // Growing left side (width increases leftwards)
                currentShapeWidth = width + (fullWidth - width) * regenerationProgress;
                currentShapeHeight = height; // Height remains constant
                 // The drawing origin (top-left of the growing shape) shifts leftwards
                offsetX = -(currentShapeWidth - width);
            }
             ctx.lineWidth = 1; // Thinner line during growth?

        } else { // Regeneration complete or not started (progress 0 or 1)
            currentShapeWidth = fullWidth;
            currentShapeHeight = fullHeight;
            ctx.fillStyle = COLORS.body;
            ctx.strokeStyle = COLORS.eyespot;
             ctx.lineWidth = 1.5; // Thicker line for mature planaria
        }

        // Draw the planaria shape based on the calculated current size
        const headWidthRatio = 0.2;
        const tailWidthRatio = 0.1;
        const bodyMidHeight = currentShapeHeight / 2;

        const headBaseX = offsetX + currentShapeWidth * headWidthRatio;
        const tailBaseX = offsetX + currentShapeWidth * (1 - tailWidthRatio);

        ctx.beginPath();
        // Start near the tail base
        ctx.moveTo(tailBaseX, offsetY + bodyMidHeight);
        // Draw tail point
        ctx.lineTo(offsetX + currentShapeWidth, offsetY + bodyMidHeight);
        // Draw body curve towards head
        ctx.bezierCurveTo(
            offsetX + currentShapeWidth * 0.8, offsetY + 0, // Control point 1
            offsetX + currentShapeWidth * 0.2, offsetY + 0, // Control point 2
            headBaseX, offsetY + bodyMidHeight - currentShapeWidth * headWidthRatio / 2 // End point (start of head lobes)
        );
        // Draw head lobes
        ctx.bezierCurveTo(
            offsetX + headBaseX * 0.8, offsetY + bodyMidHeight - currentShapeWidth * headWidthRatio * 0.4,
            offsetX + headBaseX * 0.8, offsetY + bodyMidHeight + currentShapeWidth * headWidthRatio * 0.4,
            headBaseX, offsetY + bodyMidHeight + currentShapeWidth * headWidthRatio / 2
        );
        // Draw body curve back towards tail
         ctx.bezierCurveTo(
             offsetX + currentShapeWidth * 0.2, offsetY + currentShapeHeight,
             offsetX + currentShapeWidth * 0.8, offsetY + currentShapeHeight,
             tailBaseX, offsetY + bodyMidHeight
         );

        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Draw eyespots (simplified), adjust position based on current head size and offset
         const minProgressForEyes = 0.4; // Only draw eyes once the head part is somewhat regenerated
         const isOriginalHeadOrFull = (partType === 'head' || partType === 'full');

         if (regenerationProgress >= minProgressForEyes || (isOriginalHeadOrFull && regenerationProgress < 1) || regenerationProgress === 1) {
             const eyeSpotRadius = currentShapeWidth * 0.02;
             ctx.fillStyle = COLORS.eyespot;
             // Position eyes relative to the head's base and body midline
             const eyeX = offsetX + headBaseX * 0.7; // A bit behind the tip
             const eyeSpread = currentShapeWidth * headWidthRatio * 0.2; // Spread relative to head size
             ctx.beginPath();
             ctx.arc(eyeX, offsetY + bodyMidHeight - eyeSpread, eyeSpotRadius, 0, Math.PI * 2);
             ctx.fill();
             ctx.beginPath();
             ctx.arc(eyeX, offsetY + bodyMidHeight + eyeSpread, eyeSpotRadius, 0, Math.PI * 2);
             ctx.fill();
         }


        ctx.restore();
    }


     function getMousePos(event) {
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        let clientX, clientY;

         if (event.touches && event.touches.length > 0) {
             clientX = event.touches[0].clientX;
             clientY = event.touches[0].clientY;
         } else {
             clientX = event.clientX;
             clientY = event.clientY;
         }

        return {
            x: (clientX - rect.left) * scaleX,
            y: (clientY - rect.top) * scaleY
        };
    }

    function updateCutVisuals(start, end) {
         const { width, height } = getCanvasSize();
         const x1 = Math.min(start.x, end.x);
         const y1 = Math.min(start.y, end.y);
         const x2 = Math.max(start.x, end.x);
         const y2 = Math.max(start.y, end.y);

         // Position and size the overlay div to represent the cut line
         cutLineOverlay.style.display = 'block';
         const dx = x2 - x1;
         const dy = y2 - y1;
         const distance = Math.sqrt(dx * dx + dy * dy);
         const angle = Math.atan2(dy, dx);

         cutLineOverlay.style.width = `${distance}px`;
         cutLineOverlay.style.height = `2px`; /* Thinner line visual */
         cutLineOverlay.style.left = `${x1}px`;
         cutLineOverlay.style.top = `${y1}px`;
         cutLineOverlay.style.transformOrigin = `0 0`;
         cutLineOverlay.style.transform = `rotate(${angle}rad)`;
         cutLineOverlay.style.borderColor = var(--cut-line-color);
         cutLineOverlay.style.borderStyle = 'dashed';
         cutLineOverlay.style.borderWidth = '1px 0 0 0'; /* Only draw top border */
         cutLineOverlay.style.borderRadius = '0'; // No rounding for the line effect
         cutLineOverlay.style.boxSizing = 'content-box';
    }

     function resetCutVisuals() {
         cutLineOverlay.style.display = 'none';
     }


    function performCut(start, end) {
        if (planariaParts.length > 1 || planariaParts[0].partType !== 'full') return false; // Only allow cutting a single full planaria

        const part = planariaParts[0]; // The single full planaria
        const partX = part.x;
        const partY = part.y;
        const partWidth = part.width;
        const partHeight = part.height;

        const cutTolerance = 20; // pixels tolerance for horizontal/vertical check
        const minPartRatio = 0.15; // Minimum ratio of original size for a viable part

        const dx = end.x - start.x;
        const dy = end.y - start.y;

        let newParts = [];
        let validCut = false;

        // Check for horizontal cut
        if (Math.abs(dx) < cutTolerance) { // Mostly vertical line drawn
            const cutX = (start.x + end.x) / 2;
             // Ensure cut is within the planaria horizontally and spans most of its height
            if (cutX > partX + partWidth * minPartRatio && cutX < partX + partWidth * (1 - minPartRatio) &&
                 Math.min(start.y, end.y) < partY + partHeight * (1 - minPartRatio/2) && // Cut starts high enough
                 Math.max(start.y, end.y) > partY + partHeight * (minPartRatio/2) // Cut ends low enough
                 ) {
                // Split into left and right
                const leftPartWidth = cutX - partX;
                const rightPartWidth = (partX + partWidth) - cutX;

                if (leftPartWidth > partWidth * minPartRatio && rightPartWidth > partWidth * minPartRatio) {
                     // Adjust positions slightly so they appear cut apart
                     const separation = 5; // pixels
                     newParts.push({
                         x: partX,
                         y: partY,
                         width: leftPartWidth,
                         height: partHeight,
                         partType: 'middle-left',
                         regenerationProgress: 0,
                         animationStart: null
                     });
                     newParts.push({
                         x: cutX, // Right part starts at the cut X
                         y: partY,
                         width: rightPartWidth,
                         height: partHeight,
                         partType: 'middle-right',
                         regenerationProgress: 0,
                         animationStart: null
                     });
                     validCut = true;
                }
            }
        }
        // Check for vertical cut
        else if (Math.abs(dy) < cutTolerance) { // Mostly horizontal line drawn
             const cutY = (start.y + end.y) / 2;
             // Ensure cut is within the planaria vertically and spans most of its width
             if (cutY > partY + partHeight * minPartRatio && cutY < partY + partHeight * (1 - minPartRatio) &&
                 Math.min(start.x, end.x) < partX + partWidth * (1 - minPartRatio/2) && // Cut starts left enough
                 Math.max(start.x, end.x) > partX + partWidth * (minPartRatio/2) // Cut ends right enough
                 ) {
                 // Split into head and tail
                 const headPartHeight = cutY - partY;
                 const tailPartHeight = (partY + partHeight) - cutY;

                  if (headPartHeight > partHeight * minPartRatio && tailPartHeight > partHeight * minPartRatio) {
                      newParts.push({
                          x: partX,
                          y: partY,
                          width: partWidth,
                          height: headPartHeight,
                          partType: 'head',
                          regenerationProgress: 0,
                          animationStart: null
                      });
                      newParts.push({
                           x: partX,
                           y: cutY, // Tail starts at the cut Y
                           width: partWidth,
                           height: tailPartHeight,
                           partType: 'tail',
                           regenerationProgress: 0,
                           animationStart: null
                       });
                      validCut = true;
                  }
             }
        } else {
            // console.log("Cut is not predominantly horizontal or vertical.");
        }


        if (validCut && newParts.length > 1) {
            planariaParts = newParts;
            // console.log("Cut performed, parts:", planariaParts);
            playPauseBtn.disabled = false;
            timelineStatus.textContent = 'מוכנה לרגנרציה';
            playPauseBtn.querySelector('svg').innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>'; // Play icon
            return true;
        } else {
             // console.log("Invalid cut location or angle.");
            timelineStatus.textContent = 'חיתוך לא תקין. נסו שוב (קו ישר, אופקי או אנכי)'; // Provide feedback
            setTimeout(() => { // Reset status after a delay
                 if(planariaParts.length === 1 && planariaParts[0].partType === 'full') {
                     timelineStatus.textContent = 'הפלאנריה ממתינה לחיתוך';
                 }
            }, 2000);
            return false;
        }
    }

     function startRegenerationAnimation(timestamp) {
         if (!animationStartTime) {
             // Initialize animation start time for all parts the first time
             animationStartTime = timestamp - pauseStartTime;
             planariaParts.forEach(part => {
                 part.animationStart = timestamp - pauseStartTime;
             });
             pauseStartTime = 0; // Reset pause time
         }

         let allComplete = true;
         let totalProgress = 0;

         planariaParts.forEach(part => {
             if (part.regenerationProgress < 1) {
                 const elapsed = timestamp - part.animationStart;
                 part.regenerationProgress = Math.min(elapsed / animationDuration, 1);
                 allComplete = false;
             }
             totalProgress += part.regenerationProgress;
         });

         drawScene(); // Redraw with updated progress

         const averageProgress = totalProgress / planariaParts.length;
         timelineStatus.textContent = `רגנרציה: ${(averageProgress * 100).toFixed(0)}%`;


         if (!allComplete && !isPaused) {
             animationFrameId = requestAnimationFrame(startRegenerationAnimation);
         } else if (allComplete) {
             timelineStatus.textContent = 'רגנרציה הושלמה!';
             playPauseBtn.textContent = 'אתחל להתנסות נוספת';
             playPauseBtn.querySelector('svg').innerHTML = '<path d="M17.65 6.35a7.958 7.958 0 0 0-11.02 0L2 12h4"></path><path d="M6.35 17.65a7.958 7.958 0 0 0 11.02 0L22 12h-4"></path>'; // Reset icon
             playPauseBtn.disabled = false; // Allow resetting
             animationStartTime = null; // Reset for potential replay
             pauseStartTime = 0;

              // Optional: After regeneration, merge parts back or center them
              // For this simple simulation, resetting is easiest:
              // setTimeout(initPlanaria, 2000); // Reset after a short delay to show "complete" state
         } else if (isPaused) {
             timelineStatus.textContent = `מושהה (${(averageProgress * 100).toFixed(0)}%)`;
             playPauseBtn.querySelector('svg').innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>'; // Play icon
         }
     }

     function handlePlayPause() {
         if (planariaParts.length <= 1 || planariaParts.every(p => p.regenerationProgress >= 1)) {
              // If not cut yet, or regeneration complete, the button acts as reset
              initPlanaria();
              return;
         }

         if (isPaused) {
             isPaused = false;
             // Record the time elapsed during the pause so animation can resume correctly
             pauseStartTime = performance.now() - pauseStartTime;
             playPauseBtn.textContent = 'השהה';
             playPauseBtn.querySelector('svg').innerHTML = '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>'; // Pause icon
             animationFrameId = requestAnimationFrame(startRegenerationAnimation);
         } else {
             isPaused = true;
             // Record the time when pause started
             pauseStartTime = performance.now();
             if (animationFrameId) {
                 cancelAnimationFrame(animationFrameId);
                 animationFrameId = null;
             }
             playPauseBtn.textContent = 'המשך';
              playPauseBtn.querySelector('svg').innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>'; // Play icon
         }
     }

    // Event Listeners
    canvas.addEventListener('mousedown', (e) => {
        if (planariaParts.length > 1 || planariaParts[0].partType !== 'full') return; // Only allow cutting a single full planaria
        cutting = true;
        cutStartPos = getMousePos(e);
        cutEndPos = cutStartPos;
         updateCutVisuals(cutStartPos, cutEndPos); // Show initial point/dot
    });

    canvas.addEventListener('mousemove', (e) => {
        if (!cutting) return;
        cutEndPos = getMousePos(e);
        updateCutVisuals(cutStartPos, cutEndPos); // Update line visuals
        // No need to redraw canvas during mousemove unless we want ghost parts
    });

    canvas.addEventListener('mouseup', (e) => {
        if (!cutting) return;
        cutting = false;
        performCut(cutStartPos, cutEndPos);
        resetCutVisuals(); // Hide line visuals
    });

    // Touch event listeners for mobile
    canvas.addEventListener('touchstart', (e) => {
        if (planariaParts.length > 1 || planariaParts[0].partType !== 'full' || e.touches.length > 1) return;
        e.preventDefault(); // Prevent scrolling etc.
        cutting = true;
        cutStartPos = getMousePos(e.touches[0]);
        cutEndPos = cutStartPos;
        updateCutVisuals(cutStartPos, cutEndPos); // Show initial point/dot
    }, { passive: false });

    canvas.addEventListener('touchmove', (e) => {
        if (!cutting || e.touches.length > 1) return;
        e.preventDefault();
        cutEndPos = getMousePos(e.touches[0]);
        updateCutVisuals(cutStartPos, cutEndPos); // Update line visuals
    }, { passive: false });

    canvas.addEventListener('touchend', (e) => {
        if (!cutting) return;
         // touchend doesn't have positions, use the last known cutEndPos
        cutting = false; // Stop the cutting state immediately
        performCut(cutStartPos, cutEndPos);
        resetCutVisuals(); // Hide line visuals
    });


    resetBtn.addEventListener('click', initPlanaria);
    playPauseBtn.addEventListener('click', handlePlayPause);

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר סודות התחדשות הפלאנריה' : 'הצג סודות התחדשות הפלאנריה';
    });

    // Handle canvas resize
    window.addEventListener('resize', initPlanaria);


    // Initial setup
     initPlanaria();


</script>
```