---
title: "מסע האור: איך קרן אור משנה כיוון במים?"
english_slug: light-bends-refraction-air-water-simulation-v2
category: "פיזיקה"
tags: ["אופטיקה", "שבירת אור", "חוק סנל", "מים", "הדמיה", "אינטראקטיבי"]
---
# מסע האור: איך קרן אור משנה כיוון במים?

<p>חשבו על רגע... האם שמתם לב פעם שהכף בכוס התה נראית כאילו נשברה בקו המים? או אולי תהיתם למה דייגים לפעמים מחטיאים את המטרה כשהם מנסים לדוג דג שנראה קרוב לפני המים? הסיבה לכל התעלולים האופטיים האלה טמונה בסוד מרתק: האור "מתכופף" כשהוא עובר מחומר לחומר! הצטרפו אלינו למסע ויזואלי כדי לגלות למה זה קורה.</p>

<div id="simulation-container">
    <div class="media-labels">
        <span class="media-label top-label">אוויר (n=1.0)</span>
        <span class="media-label bottom-label">מים (n=1.33)</span>
    </div>
    <canvas id="refractionCanvas"></canvas>
    <div id="controls">
        <label for="angleSlider">כוונו את קרן האור:</label>
        <input type="range" id="angleSlider" min="0" max="89.9" value="30" step="0.1">
        <div id="angleDisplay">
            <p>זווית פגיעה (&theta;₁): <span id="incidenceAngle">30.0</span>°</p>
            <p>זווית שבירה (&theta;₂): <span id="refractionAngle"></span>°</p>
        </div>
    </div>
</div>

<style>
    :root {
        --color-air: #e0f7fa; /* Light cyan */
        --color-water: #81d4fa; /* Light blue */
        --color-boundary: #0277bd; /* Darker blue */
        --color-normal: #555; /* Grey */
        --color-ray: #ffab00; /* Amber */
        --color-ray-glow: rgba(255, 171, 0, 0.5);
        --color-control: #00bcd4; /* Cyan */
        --color-text: #333; /* Dark grey */
        --color-bg-container: #ffffff; /* White */
        --color-border: #e0e0e0; /* Light grey */
        --color-button-bg: #007bff; /* Blue */
        --color-button-hover: #0056b3; /* Darker blue */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--color-text);
    }

    h1, h2 {
        color: var(--color-button-hover);
        text-align: center;
        margin-bottom: 20px;
    }

    #simulation-container {
        margin: 30px auto;
        text-align: center;
        max-width: 700px; /* Slightly narrower for focus */
        border: 1px solid var(--color-border);
        border-radius: 12px; /* More rounded corners */
        padding: 20px;
        background-color: var(--color-bg-container);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        position: relative; /* Needed for absolute positioning of labels */
    }

     .media-labels {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%; /* Cover the canvas area */
        pointer-events: none; /* Allow clicks/drags on canvas below */
        z-index: 1; /* Ensure labels are above background but below rays */
    }

    .media-label {
        position: absolute;
        left: 15px; /* Adjust positioning */
        font-size: 1em;
        font-weight: bold;
        color: var(--color-text);
        opacity: 0.8;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }

    .top-label {
         top: 15px;
    }

    .bottom-label {
         bottom: 15px;
    }


    #refractionCanvas {
        width: 100%;
        height: 450px; /* Slightly increased height */
        display: block; /* Remove extra space below canvas */
        margin: 0 auto;
        border: 1px solid var(--color-boundary);
        border-radius: 8px; /* Match container rounding */
        background: linear-gradient(to bottom, var(--color-air) 0%, var(--color-air) 50%, var(--color-water) 50%, var(--color-water) 100%);
        cursor: grab;
        position: relative; /* Needed for drawing context */
        z-index: 2; /* Ensure canvas drawings are above background/labels */
    }

    #refractionCanvas:active {
        cursor: grabbing;
    }

    #controls {
        margin-top: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    #controls label {
        margin-bottom: 8px;
        font-weight: bold;
        font-size: 1.1em;
    }

    #controls input[type="range"] {
        width: 90%; /* Wider slider */
        margin-bottom: 15px;
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 8px;
        background: var(--color-border);
        border-radius: 5px;
        outline: none;
        transition: opacity .2s;
    }

    #controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--color-button-bg);
        border-radius: 50%;
        cursor: pointer;
        border: 2px solid var(--color-bg-container);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

    #controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--color-button-bg);
        border-radius: 50%;
        cursor: pointer;
        border: 2px solid var(--color-bg-container);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

     #controls input[type="range"]:hover::-webkit-slider-thumb {
         background-color: var(--color-button-hover);
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
     }

      #controls input[type="range"]:hover::-moz-range-thumb {
         background-color: var(--color-button-hover);
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
     }


    #angleDisplay {
        text-align: left;
        min-width: 220px; /* Ensure consistent width */
        background-color: #f0f0f0;
        padding: 10px 15px;
        border-radius: 8px;
        font-size: 1em;
    }

    #angleDisplay p {
        margin: 5px 0;
        font-size: 1em;
        color: var(--color-text);
    }

    #angleDisplay span {
        font-weight: bold;
        color: var(--color-button-hover);
    }


    #explanation-button {
        display: block;
        margin: 30px auto 20px auto; /* More space */
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--color-button-bg);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    #explanation-button:hover {
        background-color: var(--color-button-hover);
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
    }

    #explanation-button:active {
        transform: scale(0.98);
    }

    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--color-border);
        border-radius: 12px;
        background-color: var(--color-bg-container);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    }

    #explanation h2 {
        color: var(--color-button-hover);
        margin-top: 15px;
        margin-bottom: 10px;
        font-size: 1.4em;
        border-bottom: 1px solid var(--color-border);
        padding-bottom: 5px;
    }

    #explanation p {
        margin-bottom: 12px;
        line-height: 1.7;
        color: var(--color-text);
    }

     #explanation ul {
         margin-bottom: 12px;
         padding-left: 20px;
     }

     #explanation li {
         margin-bottom: 5px;
     }

    #explanation strong {
        color: var(--color-button-hover);
    }

    /* Add more responsive adjustments if needed */
    @media (max-width: 600px) {
        #simulation-container {
            padding: 15px;
        }
        #controls input[type="range"] {
            width: 95%;
        }
        #explanation-button {
            padding: 10px 20px;
            font-size: 1em;
        }
         #explanation h2 {
            font-size: 1.2em;
        }
    }

</style>

<button id="explanation-button">גלו את הסוד: מה גורם לאור להתכופף?</button>

<div id="explanation" style="display: none;">
    <h2>מה קורה כאן בעצם? הכירו את "שבירת האור"</h2>
    <p><strong>שבירת אור (Refraction)</strong> היא הפלא הפיזיקלי שגורם לקרן אור לשנות את מסלולה בדיוק ברגע שהיא עוברת מתווך שקוף אחד (כמו האוויר שמעלינו) לתווך שקוף אחר (כמו המים, הזכוכית, או אפילו העדשה במשקפיים שלכם!). זה כאילו האור מקבל "הוראה" להתכופף בנקודת המעבר.</p>

    <h2>למה האור מתכופף בכלל?</h2>
    <p>הסיבה הפשוטה והמדהימה היא ש<strong>האור נע במהירות שונה בחומרים שונים</strong>! בריק (כמו בחלל החיצון), האור טס במהירות שיא של כ-300,000 קילומטר בשנייה – זו המהירות האולטימטיבית שלו. אבל כשהוא נכנס לחומר כמו אוויר, מים או זכוכית, הוא פוגש מולקולות ומאט! מידת ההאטה תלויה בצפיפות האופטית של החומר. שינוי המהירות הזה, שקורה באופן מיידי על פני השטח המפריד בין החומרים, הוא שגורם לקרן האור "להתעקם".</p>

    <h2>איך מודדים את ה"עצלות" של האור בחומר? מקדם השבירה בא לעזרה!</h2>
    <p>כדי לתאר כמה האור מאט בחומר מסוים, משתמשים ב<strong>מקדם שבירה (Refractive Index)</strong>, שמסומן לרוב באות n. זהו פשוט יחס בין מהירות האור בריק (c) למהירות האור בחומר (v): n = c / v.</p>
    <ul>
        <li>לריק יש מקדם שבירה של 1 (הכי מהיר!).</li>
        <li>לאוויר יש מקדם שבירה קרוב מאוד ל-1 (האור עדיין טס כמעט במהירות שיא).</li>
        <li>למים יש מקדם שבירה של כ-1.33 (האור מאט באופן משמעותי).</li>
        <li>לזכוכית יש מקדם שבירה של כ-1.5, ואפילו יותר לאבני יהלום (שם האור מאט מאוד!).</li>
    </ul>
    <p>ככל שמקדם השבירה גבוה יותר, כך האור נע לאט יותר באותו חומר, והחומר נחשב "צפוף אופטית" יותר.</p>

    <h2>החוק שמסדר את הכל: חוק סנל</h2>
    <p>הקשר המדויק בין זווית הכניסה של האור לזווית היציאה שלו בצד השני מתואר על ידי נוסחה אלגנטית שנקראת <strong>חוק סנל (Snell's Law)</strong>:</p>
    <p>n₁ * sin(θ₁) = n₂ * sin(θ₂)</p>
    <p>במילים פשוטות:</p>
    <ul>
        <li>n₁ הוא מקדם השבירה של החומר ממנו מגיע האור.</li>
        <li>θ₁ היא <strong>זווית הפגיעה</strong> (הזווית בין קרן האור הנכנסת לבין קו דמיוני ישר שנקרא ה<strong>נורמל</strong> - אנך למשטח).</li>
        <li>n₂ הוא מקדם השבירה של החומר אליו האור עובר.</li>
        <li>θ₂ היא <strong>זווית השבירה</strong> (הזווית בין קרן האור היוצאת לבין הנורמל בתוך החומר השני).</li>
    </ul>
    <p>הסימולציה שלמעלה מציגה בדיוק את הפעולה של חוק זה. נסו לשחק עם הזווית וראו כיצד הנוסחה "מתקיימת" מול עיניכם!</p>

    <h2>מאוויר למים: למה האור נשבר "לכיוון הנורמל"?</h2>
    <p>בסימולציה שלנו, האור עובר מאוויר (n₁ ≈ 1) למים (n₂ ≈ 1.33). כלומר, הוא עובר מתווך אופטי "דליל" (מהיר לאור) לתווך אופטי "צפוף" (איטי יותר לאור). לפי חוק סנל: sin(θ₂) = (n₁ / n₂) * sin(θ₁).</p>
    <p>מכיוון ש- n₁ קטן מ- n₂, היחס n₁ / n₂ קטן מ-1. לכן, sin(θ₂) חייב להיות קטן יותר מ- sin(θ₁). עבור זוויות בין 0 ל-90 מעלות (כמו שיש לנו כאן), ככל שהזווית קטנה יותר, כך הסינוס שלה קטן יותר. המסקנה היא ש- <strong>θ₂ קטנה מ- θ₁</strong>! זה בדיוק מה שאתם רואים בסימולציה: קרן האור הנשברת מתכופפת (נשברת) לכיוון קו הנורמל (האנך).</p>
     <p>אם הייתם שולחים קרן אור מתוך המים החוצה לאוויר, היה קורה ההפך: האור היה עובר מתווך צפוף לדליל, מהירותו הייתה גדלה, והוא היה נשבר <strong>התרחקות מהנורמל</strong> (n₁ * sin(θ₁) = n₂ * sin(θ₂), הפעם n₁ הוא 1.33 ו- n₂ הוא 1, כך שהיחס n₁/n₂ גדול מ-1, sin(θ₂) > sin(θ₁), ו- θ₂ > θ₁).</p>


    <h2>ראו זאת בעצמכם!</h2>
    <p>הסימולציה מאפשרת לכם לשלוט בזווית הפגיעה ולראות כיצד זווית השבירה משתנה בהתאם לחוק סנל. שימו לב במיוחד מה קורה כשהאור פוגע בניצב למשטח (זווית פגיעה 0°) - האם הוא נשבר?</p>
</div>

<script>
    const canvas = document.getElementById('refractionCanvas');
    const ctx = canvas.getContext('2d');
    const angleSlider = document.getElementById('angleSlider');
    const incidenceAngleSpan = document.getElementById('incidenceAngle');
    const refractionAngleSpan = document.getElementById('refractionAngle');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('explanation');

    // Refractive indices
    const n1_air = 1.0;
    const n2_water = 1.33; // Using a slightly more common value than 1.333

    // Simulation constants
    let W, H; // Canvas width and height
    let originX, originY; // Point where ray hits the boundary
    const boundaryY = 0.5; // Boundary is at 50% of canvas height
    const controlPointRadius = 10; // Radius of the draggable control point
    const rayDrawLength = 0.8; // Length of drawn rays relative to canvas size (longer)
    const controlPointDistance = 0.4; // Distance of the control point from origin relative to canvas size

    let isDragging = false;
    let currentAngleDegrees = parseFloat(angleSlider.value);
    let currentAngleRadians = degreesToRadians(currentAngleDegrees);

    // Animation state
    let animationProgress = 0; // 0 to 1, represents how far the ray has "traveled"
    const animationDuration = 1500; // milliseconds for the ray to travel
    let startTime = null;
    let isAnimating = true;

    // Angle labels positions
    const angleLabelOffset = 30; // distance from origin for angle labels
    const angleValueOffset = 55; // distance for numerical value labels

    // Colors (match CSS variables)
    const colorBoundary = getCssVar('--color-boundary');
    const colorNormal = getCssVar('--color-normal');
    const colorRay = getCssVar('--color-ray');
    const colorRayGlow = getCssVar('--color-ray-glow');
    const colorControl = getCssVar('--color-control');
     const colorText = getCssVar('--color-text');


    function getCssVar(name) {
         return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    }


    // Function to update canvas size based on display size
    function resizeCanvas() {
        const container = canvas.parentElement;
        const rect = container.getBoundingClientRect();
        canvas.width = rect.width;
        canvas.height = 450; // Fixed height

        W = canvas.width;
        H = canvas.height;
        originX = W / 2;
        originY = H * boundaryY;

        draw(); // Redraw after resize
    }

    function degreesToRadians(degrees) {
        return degrees * Math.PI / 180;
    }

    function radiansToDegrees(radians) {
        return radians * 180 / Math.PI;
    }

    function calculateRefractionAngleRadians(incidenceAngleRadians) {
        // Snell's Law: n1 * sin(theta1) = n2 * sin(theta2)
        // sin(theta2) = (n1 / n2) * sin(theta1)
        // theta2 = asin((n1 / n2) * sin(theta1))
        const sinTheta2 = (n1_air / n2_water) * Math.sin(incidenceAngleRadians);
        // Clamp sinTheta2 to [-1, 1] to avoid asin errors near 90 degrees
        const clampedSinTheta2 = Math.max(-1, Math.min(1, sinTheta2));
        return Math.asin(clampedSinTheta2);
    }

    function draw(timestamp) {
        if (!ctx || !canvas) return;

        // Animation logic
        if (isAnimating) {
             if (!startTime) startTime = timestamp;
             const elapsedTime = timestamp - startTime;
             animationProgress = Math.min(1, elapsedTime / animationDuration); // Progress 0 to 1

             if (animationProgress < 1) {
                 requestAnimationFrame(draw); // Continue animating
             } else {
                  isAnimating = false; // Stop animation when done
                  startTime = null; // Reset start time for next animation
             }
        } else {
             // If not animating, just draw the static state
             animationProgress = 1; // Ensure rays are fully drawn when static
        }


        ctx.clearRect(0, 0, W, H);

        // Draw boundary
        ctx.beginPath();
        ctx.moveTo(0, originY);
        ctx.lineTo(W, originY);
        ctx.strokeStyle = colorBoundary;
        ctx.lineWidth = 3;
        ctx.stroke();

        // Draw Normal (dashed)
        ctx.beginPath();
        ctx.setLineDash([8, 6]); // Dashed line
        ctx.moveTo(originX, 0);
        ctx.lineTo(originX, H);
        ctx.strokeStyle = colorNormal;
        ctx.lineWidth = 1.5;
        ctx.stroke();
        ctx.setLineDash([]); // Reset line dash
        ctx.font = '15px Arial';
        ctx.fillStyle = colorNormal;
        ctx.fillText('נורמל', originX + 8, 20); // Label for Normal


        // Convert current angle (degrees) to radians
        currentAngleRadians = degreesToRadians(currentAngleDegrees);
        const refractionAngleRadians = calculateRefractionAngleRadians(currentAngleRadians);
        const refractionAngleDegrees = radiansToDegrees(refractionAngleRadians);

        // Calculate control point position based on angle and distance
        // The angle is from the upwards vertical (0, -1). 0 deg is vertical up.
        const R_cp = controlPointDistance * Math.min(W, H); // Radius for control point circle
        const cpX = originX + R_cp * Math.sin(currentAngleRadians);
        const cpY = originY - R_cp * Math.cos(currentAngleRadians);

        // Calculate refracted ray endpoint
        // Angle is from the DOWNWARDS normal vector (0, 1). Needs same horizontal direction as incoming ray.
        const signedRefractionAngleRadians = refractionAngleRadians * Math.sign(Math.sin(currentAngleRadians)); // Apply direction based on incidence side (left/right)
        const R_refracted = rayDrawLength * Math.min(W, H); // Length for refracted ray
        const refractedX = originX + R_refracted * Math.sin(signedRefractionAngleRadians);
        const refractedY = originY + R_refracted * Math.cos(signedRefractionAngleRadians); // cos is always positive for angle 0-90 from vertical


        // Draw Incoming Ray (animated segment)
        ctx.beginPath();
        // Calculate endpoint based on animation progress
        const rayInX = cpX + (originX - cpX) * animationProgress;
        const rayInY = cpY + (originY - cpY) * animationProgress;
        ctx.moveTo(cpX, cpY);
        ctx.lineTo(rayInX, rayInY);
         // Add a glow effect
        ctx.shadowBlur = 15;
        ctx.shadowColor = colorRayGlow;
        ctx.strokeStyle = colorRay;
        ctx.lineWidth = 4;
        ctx.stroke();
        ctx.shadowBlur = 0; // Reset shadow

        // Draw Refracted Ray (animated segment, starts after incoming hits boundary)
        if (animationProgress > 0.5) { // Start refracted ray animation halfway through total duration
             const refractedAnimationProgress = Math.min(1, (animationProgress - 0.5) * 2); // Scale progress from 0 to 1 for refracted ray
            ctx.beginPath();
            const rayOutX = originX + (refractedX - originX) * refractedAnimationProgress;
            const rayOutY = originY + (refractedY - originY) * refractedAnimationProgress;
            ctx.moveTo(originX, originY);
            ctx.lineTo(rayOutX, rayOutY);
             // Add a glow effect
            ctx.shadowBlur = 15;
            ctx.shadowColor = colorRayGlow;
            ctx.strokeStyle = colorRay;
            ctx.lineWidth = 4;
            ctx.stroke();
            ctx.shadowBlur = 0; // Reset shadow
        }


        // Draw Draggable Control Point
        ctx.beginPath();
        ctx.arc(cpX, cpY, controlPointRadius, 0, Math.PI * 2);
        ctx.fillStyle = colorControl;
        ctx.fill();
        ctx.strokeStyle = var(--color-bg-container); /* White border */
        ctx.lineWidth = 2;
        ctx.stroke();


        // Draw angle arcs and labels
        ctx.strokeStyle = colorNormal;
        ctx.lineWidth = 1.5;
        ctx.fillStyle = colorText;
        ctx.font = 'italic bold 18px Arial'; // Make labels stand out
        const arcRadius = Math.min(W, H) * 0.08;

        // Incidence angle arc and label (from upwards normal to incoming ray)
        if (currentAngleDegrees > 0.1) { // Don't draw arc if angle is zero
             ctx.beginPath();
            // Angle 0 is upwards normal (Math.PI * 1.5). Angle 90 is right (0). Angle -90 is left (PI).
            // Arc goes from normal (1.5*PI) towards ray (atan2(cpY-originY, cpX-originX))
             const normalUpAngle = Math.PI * 1.5; // Angle of upwards normal from +x
             const incomingRayCanvasAngle = Math.atan2(cpY - originY, cpX - originX); // Angle of incoming ray from +x

            if (cpX < originX) { // Left side of normal
                 // Arc from ray to normal (CW)
                 ctx.arc(originX, originY, arcRadius, incomingRayCanvasAngle, normalUpAngle);
            } else { // Right side of normal
                 // Arc from normal to ray (CCW)
                 ctx.arc(originX, originY, arcRadius, normalUpAngle, incomingRayCanvasAngle);
            }
            ctx.stroke();

            // Label position - calculated relative to the angle from the normal
            const angleMidRad = currentAngleRadians / 2; // Mid-angle from normal
            const labelIncX = originX + (arcRadius + angleLabelOffset) * Math.sin(angleMidRad) * Math.sign(cpX - originX);
            const labelIncY = originY - (arcRadius + angleLabelOffset) * Math.cos(angleMidRad);
            ctx.fillText('θ₁', labelIncX, labelIncY);

             // Value Label Position
            const valueIncX = originX + (arcRadius + angleValueOffset) * Math.sin(angleMidRad) * Math.sign(cpX - originX);
            const valueIncY = originY - (arcRadius + angleValueOffset) * Math.cos(angleMidRad);
             ctx.font = '14px Arial';
             ctx.fillText(currentAngleDegrees.toFixed(1) + '°', valueIncX, valueIncY);

        }


        // Refraction angle arc and label (from downwards normal to refracted ray)
        if (refractionAngleDegrees > 0.1) { // Don't draw arc if angle is zero
            ctx.beginPath();
            // Angle 0 is downwards normal (Math.PI * 0.5).
            // Arc goes from normal (0.5*PI) towards ray (atan2(refractedY-originY, refractedX-originX))
             const normalDownAngle = Math.PI * 0.5; // Angle of downwards normal from +x
             const refractedRayCanvasAngle = Math.atan2(refractedY - originY, refractedX - originX); // Angle of refracted ray from +x

             if (refractedX < originX) { // Left side of normal
                 // Arc from normal to ray (CCW)
                  ctx.arc(originX, originY, arcRadius, normalDownAngle, refractedRayCanvasAngle);
             } else { // Right side of normal
                 // Arc from ray to normal (CW)
                  ctx.arc(originX, originY, arcRadius, refractedRayCanvasAngle, normalDownAngle);
             }
            ctx.stroke();

             // Label position - calculated relative to the angle from the normal
            const angleRefMidRad = refractionAngleRadians / 2; // Mid-angle from normal
            const labelRefX = originX + (arcRadius + angleLabelOffset) * Math.sin(angleRefMidMidRad) * Math.sign(refractedX - originX);
            const labelRefY = originY + (arcRadius + angleLabelOffset) * Math.cos(angleRefMidRad);
             ctx.fillText('θ₂', labelRefX, labelRefY);

             // Value Label Position
            const valueRefX = originX + (arcRadius + angleValueOffset) * Math.sin(angleRefMidRad) * Math.sign(refractedX - originX);
            const valueRefY = originY + (arcRadius + angleValueOffset) * Math.cos(angleRefMidRad);
             ctx.font = '14px Arial';
             ctx.fillText(refractionAngleDegrees.toFixed(1) + '°', valueRefX, valueRefY);
        }


        // Update angle displays (for accessibility/clarity outside canvas)
        incidenceAngleSpan.textContent = currentAngleDegrees.toFixed(1);
        refractionAngleSpan.textContent = refractionAngleDegrees.toFixed(1);
    }

    // Function to get incidence angle from mouse position relative to origin and upwards normal
    function getAngleFromMouse(mouseX, mouseY) {
         // Vector from origin to mouse: (mouseX - originX, mouseY - originY)
         // We want the angle relative to the UPWARDS normal (0, -1)
         // atan2(y, x) gives angle relative to positive x-axis.
         // atan2(x, y) gives angle relative to positive y-axis.
         // We want angle relative to NEGATIVE y-axis (upwards).
         const vecX = mouseX - originX;
         const vecY = mouseY - originY;

         // Ensure mouse is above the boundary for angle calculation relevance
         // If mouse is below the boundary, treat its Y as slightly above
         const effectiveMouseY = Math.min(mouseY, originY - 1); // Clamp Y to just above boundary

         const angleRad = Math.atan2(vecX, -(effectiveMouseY - originY)); // Angle relative to -y axis (up)

         // atan2 returns angle in [-PI, PI]. We want 0 to 90 degrees for incidence angle.
         // The absolute value of the angle from the vertical is the incidence angle.
         const absoluteAngleRad = Math.abs(angleRad);

         return radiansToDegrees(absoluteAngleRad);
    }


    // Handle slider input
    angleSlider.addEventListener('input', (event) => {
        currentAngleDegrees = parseFloat(event.target.value);
        startRayAnimation(); // Restart animation on angle change
        draw(); // Draw immediate static state
    });

    // Handle mouse events for dragging the control point
    canvas.addEventListener('mousedown', (event) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = event.clientX - rect.left;
        const mouseY = event.clientY - rect.top;

        const R_cp = controlPointDistance * Math.min(W, H);
        const cpX = originX + R_cp * Math.sin(currentAngleRadians);
        const cpY = originY - R_cp * Math.cos(currentAngleRadians);

        // Check if mouse is over the control point (increase hit area)
        const hitRadius = controlPointRadius * 2;
        const dist = Math.sqrt((mouseX - cpX) ** 2 + (mouseY - cpY) ** 2);
        if (dist < hitRadius) {
            isDragging = true;
            canvas.style.cursor = 'grabbing';
             isAnimating = false; // Stop animation while dragging
        }
    });

    canvas.addEventListener('mousemove', (event) => {
        if (!isDragging) return;

        const rect = canvas.getBoundingClientRect();
        const mouseX = event.clientX - rect.left;
        const mouseY = event.clientY - rect.top;

        let newAngleDegrees = getAngleFromMouse(mouseX, mouseY);

        // Clamp angle to valid range [0, 89.9]
        newAngleDegrees = Math.max(0, Math.min(89.9, newAngleDegrees));

        // Update state only if angle changed significantly
        if (Math.abs(newAngleDegrees - currentAngleDegrees) > 0.1) {
             currentAngleDegrees = newAngleDegrees;
             angleSlider.value = currentAngleDegrees.toFixed(1); // Update slider
             draw(); // Draw static state while dragging
        }
    });

    canvas.addEventListener('mouseup', () => {
        if (isDragging) {
             isDragging = false;
             canvas.style.cursor = 'grab';
             startRayAnimation(); // Restart animation when dragging stops
        }
    });

     canvas.addEventListener('mouseout', () => {
        // Stop dragging if mouse leaves canvas while dragging
        if (isDragging) {
            isDragging = false;
            canvas.style.cursor = 'grab';
            startRayAnimation(); // Restart animation
        }
    });

    function startRayAnimation() {
         isAnimating = true;
         animationProgress = 0;
         startTime = null; // Reset start time
         requestAnimationFrame(draw);
    }


    // Handle explanation button
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'גלו את הסוד: מה גורם לאור להתכופף?';
         // Scroll to explanation if showing it
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial setup
    resizeCanvas(); // Set initial size and draw
    window.addEventListener('resize', resizeCanvas);

    // Start the animation on load
     startRayAnimation();

     // Ensure static draw happens initially in case animation doesn't start immediately
     draw();


</script>