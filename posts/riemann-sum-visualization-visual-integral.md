---
title: "סכום רימן: מסע ויזואלי אל עומק האינטגרל"
english_slug: riemann-sum-visualization-visual-integral
category: "מתמטיקה"
tags: ["חשבון אינטגרלי", "אינטגרל מסוים", "סכום רימן", "גיאומטריה", "ויזואליזציה אינטראקטיבית"]
---
# סכום רימן: מסע ויזואלי אל עומק האינטגרל

דמיינו שאתם מנסים למצוא את השטח המדויק תחת גרף פונקציה, צורה שיכולה להיות מתפתלת ואינה מלבן או עיגול פשוט. איך עושים את זה? סכומי רימן מציעים דרך גאונית לעשות זאת: לבנות מלבנים פשוטים שממלאים את השטח, ולראות מה קורה כשהמלבנים הופכים להיות אינסופיים ודקים ביותר!

צאו למסע ויזואלי מרתק והתנסו בעצמכם: שנו את מספר המלבנים וצפו כיצד האומדן לשטח תחת העקומה הולך ומשתפר, צעד אחר צעד, לקראת הדיוק המושלם של האינטגרל. גלו את הכוח שבחלוקה!

<div class="interactive-container">
    <canvas id="riemannCanvas"></canvas>
    <div class="controls">
        <div class="control-group">
            <label for="numRectangles">מספר המלבנים (n): <span id="nValue" class="value-display">10</span></label>
            <input type="range" id="numRectangles" min="1" max="200" value="10">
        </div>
        <div class="approximation">
            <span class="label">אומדן השטח:</span> <span id="approxArea" class="value-display">-</span>
        </div>
        <div class="function-display">
            הפונקציה: f(x) = x²
        </div>
    </div>
</div>

<button id="showExplanationBtn">גלו את הסוד מאחורי הקסם</button>

<div id="explanation" class="explanation-section">
    <h2>מלבנים שמגלים שטח נסתר</h2>
    <p>מה שראיתם בהדמיה הוא המחשה חיה של רעיון <strong>סכומי רימן</strong>, אבן יסוד בהבנת ה<strong>אינטגרל המסוים</strong>. האינטגרל המסוים של פונקציה הוא הדרך המתמטית למצוא את השטח "נטו" (שטח מעל ציר X פחות שטח מתחתיו) הכלוא בין גרף הפונקציה לציר ה-X בטווח נתון.</p>
    <p>סכומי רימן מאפשרים לנו *לאמוד* את השטח הזה בצורה גאומטרית פשוטה: מחלקים את הטווח שמעניין אותנו למרווחים קטנים ושווים. מעל כל מרווח כזה, בונים מלבן. גובה המלבן נקבע לפי ערך הפונקציה בנקודה מסוימת בתוך המרווח (לרוב משתמשים בקצה הימני, השמאלי או נקודת האמצע של המרווח – כאן השתמשנו בקצה הימני). רוחב המלבן הוא רוחב המרווח הקטן שיצרנו.</p>
    <p>כשאנו מחברים את השטחים של כל המלבנים הללו, מקבלים אומדן לשטח הכולל תחת העקומה. האומדן הזה אינו מושלם, כפי שראיתם, יש "טעויות" - אזורים בהם המלבנים חורגים מעבר לפונקציה או לא ממלאים אותה עד הסוף.</p>
    <p>אבל הנה הקסם: ככל ש<strong>מגדילים את מספר המלבנים (n)</strong>, המלבנים הופכים להיות דקים יותר ויותר. ה"טעויות" הקטנות מצטמצמות, וסכום שטחי המלבנים הולך ומתקרב בצורה דרמטית ל<strong>שטח האמיתי</strong> מתחת לעקומה. רעיון זה, של גבול סכומי רימן כאשר מספר המלבנים שואף לאינסוף (והרוחב שלהם שואף לאפס), הוא בדיוק ההגדרה הפורמלית של האינטגרל המסוים!</p>
    <p>זוהי דוגמה עוצמתית לאופן בו אפשר להתמודד עם בעיות מורכבות (חישוב שטח של צורה לא רגילה) על ידי פירוקן לחלקים פשוטים (מלבנים) ומעבר לגבול אינסופי.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); /* Subtle gradient background */
        color: #333;
        line-height: 1.6;
        margin: 0;
        min-height: 100vh;
    }

    h1, h2 {
        color: #004085; /* Darker blue for headings */
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700;
    }

    p {
        text-align: justify;
        max-width: 800px;
        margin-bottom: 15px;
        font-weight: 400;
    }

    .interactive-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #fff;
        padding: 30px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* More pronounced shadow */
        margin-bottom: 30px;
        width: 100%;
        max-width: 800px;
        border: 1px solid #e0e0e0;
    }

    #riemannCanvas {
        width: 100%;
        height: 450px; /* Slightly increased height */
        border: 1px solid #ccc; /* Keep border for visual separation */
        border-radius: 8px;
        margin-bottom: 25px;
        background-color: #e9ecef; /* Light gray background for canvas */
        display: block;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
    }

    .controls {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .control-group {
        width: 100%;
        margin-bottom: 20px;
        text-align: center;
    }

    .controls label {
        font-size: 1.1em;
        margin-bottom: 8px;
        display: inline-block; /* Align label and value */
        color: #555;
        font-weight: 400;
    }

     .value-display {
        font-weight: 700;
        color: #007bff; /* Blue color for values */
        min-width: 30px; /* Ensure space for numbers */
        display: inline-block;
        text-align: left;
    }

    #numRectangles {
        width: 90%; /* Wider slider */
        margin-top: 5px;
        cursor: pointer;
        -webkit-appearance: none; /* Override default appearance */
        appearance: none;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    #numRectangles:hover {
        opacity: 1;
    }

    #numRectangles::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease;
    }

    #numRectangles::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease;
    }
     #numRectangles:active::-webkit-slider-thumb,
     #numRectangles:focus::-webkit-slider-thumb {
         background: #0056b3; /* Darker blue when active/focused */
     }
      #numRectangles:active::-moz-range-thumb,
      #numRectangles:focus::-moz-range-thumb {
          background: #0056b3; /* Darker blue when active/focused */
      }


    .approximation {
        font-size: 1.3em; /* Slightly larger */
        font-weight: 700;
        color: #28a745; /* Green for area */
        margin-bottom: 15px;
        text-align: center;
        width: 100%;
    }

    .approximation .label {
         font-weight: 400;
         color: #555;
         font-size: 0.9em;
         margin-left: 5px;
    }
    .approximation .value-display {
        color: #28a745; /* Green for area value */
    }

    .function-display {
         font-size: 0.9em;
         color: #777;
         text-align: center;
         margin-top: 10px;
    }

    button {
        padding: 12px 25px; /* More padding */
        font-size: 1.1em; /* Larger font */
        color: #fff;
        background-color: #007bff;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Shadow for button */
        font-weight: 400;
    }

    button:hover {
        background-color: #0056b3;
        transform: translateY(-1px); /* Subtle lift on hover */
    }
     button:active {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 2px 4px rgba(0, 123, 255, 0.5);
     }


    .explanation-section {
        margin-top: 30px; /* More space */
        padding: 30px; /* More padding */
        background-color: #e9ecef;
        border-left: 6px solid #007bff; /* Thicker border */
        border-radius: 8px;
        max-width: 800px;
        transition: all 0.6s ease-in-out; /* Smoother transition */
        opacity: 0;
        max-height: 0; /* Start hidden */
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    .explanation-section h2 {
         color: #0056b3;
         margin-top: 0;
         margin-bottom: 15px;
         font-size: 1.6em;
    }

    .explanation-section.visible {
        opacity: 1;
        max-height: 1500px; /* Sufficiently large value to allow content */
        padding: 30px; /* Restore padding when visible */
    }

     /* Hide utility class */
    .hidden {
        display: none;
    }

     /* Canvas retina support - kept */
    canvas {
        image-rendering: optimizeSpeed;
        image-rendering: -moz-crisp-edges;
        image-rendering: -webkit-optimize-contrast;
        image-rendering: optimize-contrast;
        -ms-interpolation-mode: nearest-neighbor;
    }
</style>

<script>
    const canvas = document.getElementById('riemannCanvas');
    const ctx = canvas.getContext('2d');
    const numRectanglesSlider = document.getElementById('numRectangles');
    const nValueSpan = document.getElementById('nValue');
    const approxAreaSpan = document.getElementById('approxArea');
    const showExplanationBtn = document.getElementById('showExplanationBtn');
    const explanationDiv = document.getElementById('explanation');

    // Function, range, and type (fixed for this example)
    let a = 0; // Lower limit of integration
    let b = 3; // Upper limit of integration
    let func = (x) => x * x; // The function f(x) = x^2

    // Canvas drawing parameters
    let padding = 30;
    let canvasWidth, canvasHeight;
    let xMin = a;
    let xMax = b;
    let yMin, yMax; // Will be calculated based on function range

    // Animation variables
    let targetN = parseInt(numRectanglesSlider.value, 10);
    let currentN = targetN;
    let animationFrameId = null;
    const animationDuration = 400; // ms
    let animationStartTime = null;


    function resizeCanvas() {
        const displayWidth = canvas.clientWidth;
        const displayHeight = canvas.clientHeight;

        // Check if the size changed
        if (canvas.width !== displayWidth || canvas.height !== displayHeight) {
            canvas.width = displayWidth;
            canvas.height = displayHeight;
            canvasWidth = canvas.width;
            canvasHeight = canvas.height;
            // No need to call updateVisualization directly here, animation loop handles redraws
            // If no animation is active, just draw once:
            if (!animationFrameId) {
                 updateVisualization(currentN);
            }
        }
    }

    function calculateYRange() {
        // Find min/max y values in the range [a, b]
        let min = func(a);
        let max = func(b);
        const step = (b - a) / 500; // Check more points for range accuracy
        for (let i = 0; i <= 500; i++) {
            const x = a + i * step;
            const y = func(x);
            if (y < min) min = y;
            if (y > max) max = y;
        }

        // Add some padding to the y-range for better visualization
        const range = max - min;
        const yPadding = range * 0.15; // More padding
        yMin = min - yPadding;
        yMax = max + yPadding;

         // Ensure 0 is visible on y-axis if close or within range
        if (0 > yMax) yMax = 0 + range * 0.1;
        if (0 < yMin) yMin = 0 - range * 0.1;
         if (yMin === yMax) { // Handle flat function case
             yMin -= 1;
             yMax += 1;
         }

         // Adjust y-range if it's very small, to avoid scaling issues
         if (yMax - yMin < 0.01) {
             let avg = (yMax + yMin) / 2;
             yMin = avg - 0.05;
             yMax = avg + 0.05;
         }
    }

    function scaleX(x) {
        return padding + (x - xMin) / (xMax - xMin) * (canvasWidth - 2 * padding);
    }

    function scaleY(y) {
        return canvasHeight - padding - (y - yMin) / (yMax - yMin) * (canvasHeight - 2 * padding);
    }

    function drawAxes() {
        ctx.beginPath();
        ctx.strokeStyle = '#888'; /* Slightly lighter axis color */
        ctx.lineWidth = 1;

        // Draw X axis (where y=0)
        const yAxisAtZero = scaleY(0);
        if (yAxisAtZero >= padding && yAxisAtZero <= canvasHeight - padding) {
             ctx.moveTo(padding, yAxisAtZero);
             ctx.lineTo(canvasWidth - padding, yAxisAtZero);
             // Optional: add small ticks or labels
        } else { // Draw at bottom if 0 is off-screen below
             ctx.moveTo(padding, canvasHeight - padding);
             ctx.lineTo(canvasWidth - padding, canvasHeight - padding);
        }


        // Draw Y axis (where x=0 if in view, otherwise at left edge)
        const xAxisAtZero = scaleX(0);
         if (xAxisAtZero >= padding && xAxisAtZero <= canvasWidth - padding) {
              ctx.moveTo(xAxisAtZero, padding);
              ctx.lineTo(xAxisAtZero, canvasHeight - padding);
               // Optional: add small ticks or labels
         } else { // Draw at left edge if 0 is off-screen left
             ctx.moveTo(padding, padding);
             ctx.lineTo(padding, canvasHeight - padding);
         }

        ctx.stroke();

         // Add boundary lines at a and b
         ctx.beginPath();
         ctx.strokeStyle = '#aaa';
         ctx.lineWidth = 1;
         ctx.setLineDash([4, 4]); // Dashed line
         ctx.moveTo(scaleX(a), padding);
         ctx.lineTo(scaleX(a), canvasHeight - padding);
         ctx.moveTo(scaleX(b), padding);
         ctx.lineTo(scaleX(b), canvasHeight - padding);
         ctx.stroke();
         ctx.setLineDash([]); // Reset line dash

         // Add labels for a and b
        ctx.fillStyle = '#555';
        ctx.font = '12px Heebo';
        ctx.textAlign = 'center';
        const yPosForLabels = scaleY(0) + 15 > canvasHeight - padding ? canvasHeight - padding + 15 : scaleY(0) + 15;
        ctx.fillText('a=' + a, scaleX(a), yPosForLabels);
        ctx.fillText('b=' + b, scaleX(b), yPosForLabels);

         // Add labels for x and y axes
         ctx.textAlign = 'right';
         ctx.fillText('x', canvasWidth - padding + 10, scaleY(0) - 5);
         ctx.textAlign = 'left';
         ctx.fillText('y', scaleX(0) + 10, padding - 5);

    }

    function drawFunction() {
        ctx.beginPath();
        ctx.strokeStyle = '#007bff'; /* Blue function line */
        ctx.lineWidth = 3; /* Thicker line */
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';

        const numPoints = 300; // More points for smoother curve
        const dx = (xMax - xMin) / numPoints;

        ctx.moveTo(scaleX(xMin), scaleY(func(xMin)));

        for (let i = 1; i <= numPoints; i++) {
            const x = xMin + i * dx;
            // Draw only if point is roughly within canvas bounds
            const y = func(x);
            const sx = scaleX(x);
            const sy = scaleY(y);
            if (sx >= padding && sx <= canvasWidth - padding /* && sy >= padding && sy <= canvasHeight - padding */) {
                ctx.lineTo(sx, sy);
            } else {
                 // If line goes off-screen, move to the next valid point
                 ctx.moveTo(sx, sy);
            }
        }

        ctx.stroke();
    }

    function drawRiemannRectangles(n) {
        if (n <= 0) {
             approxAreaSpan.textContent = '0.0000';
            return;
        }

        const intervalWidth = (b - a) / n;
        let totalArea = 0;

        ctx.fillStyle = 'rgba(40, 167, 69, 0.5)'; // Green with more transparency
        ctx.strokeStyle = 'rgba(40, 167, 69, 0.8)'; // Less transparent border
        ctx.lineWidth = 1;

        for (let i = 0; i < n; i++) {
            const xLeft = a + i * intervalWidth;
            const xRight = a + (i + 1) * intervalWidth;

            // Using right endpoint for height (as in original code)
            const height = func(xRight);
            const width = intervalWidth;

            // Area of this rectangle
            const rectArea = height * width;
            totalArea += rectArea;

            // Draw the rectangle
            const canvasX = scaleX(xLeft);
            const canvasY = scaleY(Math.max(0, height)); // Start Y from 0 or height, depending on sign
            const canvasWidthRect = scaleX(xRight) - canvasX;
            const canvasHeightRect = scaleY(Math.min(0, height)) - canvasY; // Height is relative to 0

            ctx.fillRect(canvasX, canvasY, canvasWidthRect, canvasHeightRect);
            ctx.strokeRect(canvasX, canvasY, canvasWidthRect, canvasHeightRect);
        }

        // Display the calculated area
        approxAreaSpan.textContent = totalArea.toFixed(4); // Show with 4 decimal places
    }

    // Animation loop
    function animate(currentTime) {
        if (!animationStartTime) animationStartTime = currentTime;
        const elapsed = currentTime - animationStartTime;
        const progress = Math.min(elapsed / animationDuration, 1);

        // Easing function (e.g., ease-out quad)
        const easedProgress = progress < 0.5 ? 2 * progress * progress : 1 - Math.pow(-2 * progress + 2, 2) / 2;

        // Interpolate N value smoothly
        const prevN = parseFloat(nValueSpan.textContent); // Use displayed value before animation as start
        currentN = prevN + (targetN - prevN) * easedProgress;

        // Update visualization with the interpolated N
        updateVisualization(Math.round(currentN)); // Draw integer number of rectangles

        // Update the displayed N value smoothly
        nValueSpan.textContent = Math.round(currentN); // Show integer value changing

        if (progress < 1) {
            animationFrameId = requestAnimationFrame(animate);
        } else {
            // Animation finished, ensure final state is correct
            currentN = targetN;
             nValueSpan.textContent = targetN;
            updateVisualization(targetN);
            animationFrameId = null;
            animationStartTime = null; // Reset for next animation
        }
    }

    function startAnimation(newTargetN) {
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
         }
        targetN = newTargetN;
        animationStartTime = null; // Reset start time
        animationFrameId = requestAnimationFrame(animate);
    }


    function updateVisualization(nToDraw) {
        calculateYRange();

        // Clear canvas
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Draw background for plot area
        ctx.fillStyle = '#e9ecef';
        ctx.fillRect(padding, padding, canvasWidth - 2 * padding, canvasHeight - 2 * padding);


        drawAxes();
        drawRiemannRectangles(nToDraw); // Draw rectangles first
        drawFunction(); // Draw function curve over rectangles for clarity
    }

    // Event listeners
    numRectanglesSlider.addEventListener('input', () => {
        // Update the value display immediately as slider moves for responsiveness
        nValueSpan.textContent = numRectanglesSlider.value;
         // Start or update animation target when slider value changes
        startAnimation(parseInt(numRectanglesSlider.value, 10));
    });

    // Trigger animation on slider change stop (optional, input is smoother)
    // numRectanglesSlider.addEventListener('change', () => {
    //      startAnimation(parseInt(numRectanglesSlider.value, 10));
    // });


    showExplanationBtn.addEventListener('click', () => {
        const isVisible = explanationDiv.classList.contains('visible');
        if (isVisible) {
            explanationDiv.classList.remove('visible');
             // Use transition end to apply hidden class for accessibility/SEO
             explanationDiv.addEventListener('transitionend', function handler() {
                 explanationDiv.classList.add('hidden');
                 explanationDiv.removeEventListener('transitionend', handler);
             });
            showExplanationBtn.textContent = 'גלו את הסוד מאחורי הקסם';
        } else {
             explanationDiv.classList.remove('hidden'); // Remove hidden before adding visible
             // Force reflow to restart transition if necessary (optional but can help)
             void explanationDiv.offsetWidth;
            explanationDiv.classList.add('visible');
            showExplanationBtn.textContent = 'הסתירו את ההסבר';
        }
    });

    // Initial setup
    resizeCanvas(); // Set initial canvas size
    calculateYRange(); // Calculate initial Y range based on function/limits
    updateVisualization(currentN); // Draw initial state

    window.addEventListener('resize', resizeCanvas);

</script>
---