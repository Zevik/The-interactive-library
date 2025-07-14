---
title: "חיתוכי חרוט: הסימולטור הווירטואלי"
english_slug: "conic-sections-virtual-slicer"
category: "מדעים מדויקים / מתמטיקה"
tags: ["גיאומטריה", "חרוט", "חתכים", "אליפסה", "מעגל", "פרבולה", "היפרבולה"]
---

# חיתוכי חרוט: הסימולטור הווירטואלי

צאו למסע ויזואלי מרתק וחקרו כיצד מישור יחיד יכול לחשוף את הצורות הגיאומטריות היפהפיות החבויות בחרוט הכפול. שחקו עם זווית וגובה המישור וראו כיצד חיתוכי החרוט - מעגל, אליפסה, פרבולה והיפרבולה - נוצרים לנגד עיניכם, בזמן אמת!

<div id="interactive-container">
  <div id="simulation-area">
    <div class="canvas-container side-view">
        <canvas id="sideViewCanvas"></canvas>
        <div class="canvas-label">מבט צד</div>
    </div>
     <div class="canvas-container result-view">
        <canvas id="resultCanvas"></canvas>
         <div class="canvas-label">הצורה המתקבלת</div>
     </div>
  </div>
  <div id="controls">
    <div class="control-group">
      <label for="planeAngle">זווית המישור (ביחס לציר):</label>
      <input type="range" id="planeAngle" min="0" max="90" value="45" step="0.1">
      <span id="planeAngleValue">45.0°</span>
    </div>
    <div class="control-group">
      <label for="planePosition">מיקום המישור (ביחס לקודקוד):</label>
      <input type="range" id="planePosition" min="-150" max="150" value="0" step="1">
      <span id="planePositionValue">0</span>
    </div>
     <div class="control-group">
      <label for="coneAngle">זווית החרוט (חצי זווית ראש):</label>
      <input type="range" id="coneAngle" min="10" max="80" value="30" step="0.1">
      <span id="coneAngleValue">30.0°</span>
    </div>
    <div id="shape-info">
        <div id="shape-type">הצורה המתקבלת: <span id="currentShape"></span></div>
        <div id="shape-description"></div>
    </div>
  </div>
</div>

<button id="toggleExplanation" class="modern-button">על חיתוכי חרוט: הסבר מפורט</button>

<div id="explanation">
  <h2>על חיתוכי חרוט</h2>
  <p>חיתוכי חרוט הן עקומות מיוחדות הנוצרות כאשר מישור דו-ממדי חותך חרוט כפול אינסופי (המורכב משני חרוטים המחוברים בקודקודם). הצורה הספציפית של החיתוך תלויה אך ורק בזווית של המישור ובמיקומו ביחס לציר החרוט ולקווי היצרן (הקווים הישרים שיוצרים את מעטפת החרוט).</p>
  <ul>
    <li><b class="shape-circle">מעגל:</b> מתקבל כאשר המישור המשטח חיתוך מאונך (בזווית 90°) לציר החרוט ואינו עובר דרך הקודקוד.</li>
    <li><b class="shape-ellipse">אליפסה:</b> נוצרת כאשר המישור חותך נפח אחד של החרוט בזווית העולה על זווית החרוט (חצי זווית ראש) ביחס לציר, אך קטנה מ-90 מעלות. המישור אינו מקביל לאף קו יצרן.</li>
    <li><b class="shape-parabola">פרבולה:</b> מתקבלת כאשר המישור מקביל בדיוק לקו יצרן אחד של החרוט וחותך נפח אחד בלבד. זווית המישור שווה בדיוק לזווית החרוט ביחס לציר.</li>
    <li><b class="shape-hyperbola">היפרבולה:</b> נוצרת כאשר המישור מקביל לציר החרוט (או בעל זווית קטנה מזווית החרוט ביחס לציר), ולכן חותך את שני הנפחים של החרוט הכפול.</li>
    <li><b class="shape-degenerate">מקרים מנוונים:</b> אם המישור עובר בדיוק דרך קודקוד החרוט, החיתוך המתקבל הוא "מנוון" - נקודה בודדת (מעגל/אליפסה מנוונת), קו ישר בודד (פרבולה מנוונת), או שני קווים ישרים מצטלבים (היפרבולה מנוונת). הסימולטור מתמקד בעיקר במקרים ה"לא מנוונים".</li>
     <li><b>התנסו בעצמכם!</b> שנו את הפרמטרים בעזרת הסליידרים וצפו ביופי הגיאומטרי המתגלה בכל חיתוך.</li>
  </ul>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

body {
    font-family: 'Heebo', sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0;
    padding: 20px;
    background-color: #f0f2f5; /* Softer background */
    direction: rtl;
    text-align: right;
    min-height: 100vh; /* Ensure body takes at least full viewport height */
    display: flex;
    flex-direction: column;
    align-items: center;
}

h1, h2 {
    color: #4a2e80; /* Deeper Purple */
    text-align: center;
    margin-bottom: 20px;
    font-weight: 700;
}

#interactive-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: linear-gradient(135deg, #ffffff, #f9f9f9); /* Subtle gradient */
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1); /* Stronger shadow */
    margin-bottom: 30px;
    width: 100%;
    max-width: 800px; /* Limit max width */
    box-sizing: border-box;
}

#simulation-area {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 30px; /* Increased gap */
    margin-bottom: 30px;
    flex-wrap: wrap;
    width: 100%; /* Take full container width */
}

.canvas-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    transition: transform 0.3s ease;
}

.canvas-container:hover {
    transform: translateY(-5px); /* Lift effect on hover */
}

canvas {
    display: block; /* Remove extra space below canvas */
    background-color: #fefefe; /* Lighter background */
    border-radius: 4px;
}

#sideViewCanvas, #resultCanvas {
    width: 300px;
    height: 300px;
}

.canvas-label {
    margin-top: 8px;
    font-size: 1em;
    color: #555;
    font-weight: 500;
    text-align: center;
}

#controls {
    display: flex;
    flex-direction: column;
    gap: 20px; /* Increased gap */
    width: 100%;
    max-width: 500px;
}

.control-group {
    display: flex;
    flex-direction: column;
    background-color: #f8f8f8;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #eee;
}

.control-group label {
    margin-bottom: 8px; /* Increased margin */
    font-weight: 700;
    color: #555;
    font-size: 1em;
}

.control-group input[type="range"] {
    width: 100%;
    -webkit-appearance: none;
    appearance: none;
    height: 10px; /* Thicker track */
    background: #ddd;
    outline: none;
    opacity: 0.9; /* Slightly less transparent by default */
    transition: opacity .2s, background .2s;
    border-radius: 5px;
    margin: 5px 0;
}

.control-group input[type="range"]::-webkit-slider-runnable-track {
    background: linear-gradient(to right, #a0a0a0, #ddd); /* Gradient track */
    border-radius: 5px;
    height: 10px;
}

.control-group input[type="range"]::-moz-range-track {
     background: linear-gradient(to right, #a0a0a0, #ddd); /* Gradient track */
    border-radius: 5px;
    height: 10px;
}


.control-group input[type="range"]:hover {
    opacity: 1;
}

.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 22px; /* Larger thumb */
    height: 22px; /* Larger thumb */
    background: #6a4db8; /* Slightly brighter purple */
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0,0,0,0.25); /* Enhanced shadow */
    margin-top: -6px; /* Center thumb vertically */
    transition: background 0.2s, box-shadow 0.2s;
}

.control-group input[type="range"]::-moz-range-thumb {
    width: 22px; /* Larger thumb */
    height: 22px; /* Larger thumb */
    background: #6a4db8; /* Slightly brighter purple */
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0,0,0,0.25); /* Enhanced shadow */
     transition: background 0.2s, box-shadow 0.2s;
}

.control-group input[type="range"]::-webkit-slider-thumb:hover,
.control-group input[type="range"]::-moz-range-thumb:hover {
    background: #7b5edb; /* Lighter on hover */
    box-shadow: 0 3px 8px rgba(0,0,0,0.3);
}


.control-group span {
    margin-top: 8px; /* Increased margin */
    font-size: 1em;
    color: #666;
    text-align: center;
    font-weight: 500;
}

#shape-info {
    margin-top: 20px;
    padding: 15px;
    background-color: #eef; /* Light blueish background */
    border-radius: 8px;
    border: 1px solid #dde;
    text-align: center;
}

#shape-type {
    font-size: 1.2em; /* Larger font */
    font-weight: 700;
    color: #4a2e80; /* Deeper Purple */
    margin-bottom: 5px;
}

#currentShape {
     font-weight: 500;
     transition: color 0.3s ease; /* Smooth color transition */
}

#shape-description {
    font-size: 0.9em;
    color: #555;
    min-height: 1.2em; /* Reserve space to prevent layout shifts */
}


.modern-button {
    display: block;
    width: auto;
    margin: 20px auto;
    padding: 14px 30px; /* More padding */
    font-size: 1.15em; /* Slightly larger font */
    color: #fff;
    background-color: #5a3e8a; /* Original Purple */
    border: none;
    border-radius: 8px; /* More rounded corners */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    font-family: 'Heebo', sans-serif;
    font-weight: 500;
}

.modern-button:hover {
    background-color: #6f54a0; /* Darker purple */
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

.modern-button:active {
    transform: scale(0.98);
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#explanation {
    display: none;
    background-color: #e9e4f1; /* Light purple */
    padding: 25px; /* More padding */
    border-radius: 10px; /* More rounded corners */
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    margin-top: 20px;
    border-right: 6px solid #5a3e8a; /* Thicker Purple border on the right */
    width: 100%;
    max-width: 800px;
    box-sizing: border-box;
    transition: opacity 0.5s ease; /* Fade in animation */
    opacity: 0; /* Start hidden for fade in */
}

#explanation.visible {
    display: block;
    opacity: 1;
}


#explanation h2 {
    margin-top: 0;
    text-align: right;
    color: #4a2e80;
    font-weight: 700;
}

#explanation ul {
    padding-right: 20px;
    list-style: disc; /* Use default disc bullets */
}

#explanation li {
    margin-bottom: 12px; /* More space between list items */
}

#explanation b {
    color: #4a2e80; /* Default bold color */
}

/* Shape specific colors */
.shape-circle { color: #007bff; font-weight: 700; }
.shape-ellipse { color: #28a745; font-weight: 700; }
.shape-parabola { color: #ff8800; font-weight: 700; } /* More orange */
.shape-hyperbola { color: #dc3545; font-weight: 700; }
.shape-איןחיתוךמנוון, .shape-degenerate { color: #888; font-weight: 700; }


/* Responsive Adjustments */
@media (max-width: 768px) {
    #simulation-area {
        flex-direction: column;
        gap: 20px; /* Adjusted gap */
    }

    .canvas-container, canvas {
        width: 100%;
        height: auto; /* Allow height to adjust */
        max-width: 350px; /* Slightly larger max width on medium screens */
    }

    #interactive-container {
        padding: 20px;
    }

    .modern-button {
        font-size: 1.05em;
        padding: 12px 25px;
    }

    #explanation {
         padding: 20px;
    }

     #shape-type {
        font-size: 1.1em;
     }

     .control-group {
        padding: 12px;
     }
}

@media (max-width: 480px) {
    body {
        padding: 10px;
    }

     h1 {
        font-size: 1.8em;
     }

    #interactive-container {
        padding: 15px;
    }

    .canvas-container, canvas {
         max-width: 280px; /* Smaller max width on small screens */
    }

    .control-group {
        padding: 10px;
    }

     .modern-button {
        font-size: 1em;
        padding: 10px 20px;
     }

     #explanation {
        padding: 15px;
     }
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const sideViewCanvas = document.getElementById('sideViewCanvas');
    const resultCanvas = document.getElementById('resultCanvas');
    const sideViewCtx = sideViewCanvas.getContext('2d');
    const resultCtx = resultCanvas.getContext('2d');

    const planeAngleSlider = document.getElementById('planeAngle');
    const planePositionSlider = document.getElementById('planePosition');
    const coneAngleSlider = document.getElementById('coneAngle');

    const planeAngleValueSpan = document.getElementById('planeAngleValue');
    const planePositionValueSpan = document.getElementById('planePositionValue');
    const coneAngleValueSpan = document.getElementById('coneAngleValue');
    const currentShapeSpan = document.getElementById('currentShape');
    const shapeDescriptionDiv = document.getElementById('shape-description');

    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    const canvasSize = 300;
    sideViewCanvas.width = canvasSize;
    sideViewCanvas.height = canvasSize;
    resultCanvas.width = canvasSize;
    resultCanvas.height = canvasSize;

    const centerX = canvasSize / 2;
    const centerY = canvasSize / 2;
    const drawingScale = 0.8; // Scale down drawing slightly to fit better
    const coneAxisLength = canvasSize * drawingScale; // Length of the drawn cone axis
    const coneApexY = centerY; // Apex is at the center of the canvas vertically

    let animationFrameId = null; // To manage drawing animation

    // Function to convert degrees to radians
    function degToRad(degrees) {
        return degrees * Math.PI / 180;
    }

    // Function to smoothly interpolate between values (not used for direct simulation but could be for future anim)
    function lerp(a, b, t) {
        return a + (b - a) * t;
    }

     // Function to draw a basic ellipse/circle with animation
    function drawEllipse(ctx, x, y, radiusX, radiusY, rotation, color, duration = 500) {
        return new Promise(resolve => {
            const startTime = performance.now();
            const animate = (currentTime) => {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);

                ctx.save();
                ctx.translate(x, y);
                ctx.rotate(rotation);
                ctx.scale(radiusX / radiusY, 1);
                ctx.beginPath();
                // Draw partial arc based on progress
                ctx.arc(0, 0, radiusY, 0, Math.PI * 2 * progress, false);
                ctx.strokeStyle = color;
                ctx.lineWidth = 5; // Slightly thicker line
                ctx.lineCap = 'round';
                ctx.stroke();
                ctx.restore();

                if (progress < 1) {
                    animationFrameId = requestAnimationFrame(animate);
                } else {
                    resolve(); // Animation complete
                }
            };
             // Clear just the result canvas before drawing
            resultCtx.clearRect(0, 0, canvasSize, canvasSize);
            animationFrameId = requestAnimationFrame(animate);
        });
    }

    // Helper function to draw a basic parabola (stylized) with animation
    function drawParabola(ctx, x, y, size, color, duration = 500) {
         return new Promise(resolve => {
            const startTime = performance.now();
            const animate = (currentTime) => {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);

                ctx.beginPath();
                // Calculate points along the curve based on progress
                const startX = x - size * 0.8;
                const startY = y + size * 0.8;
                const controlX = x;
                const controlY = y - size;
                const endX = x + size * 0.8;
                const endY = y + size * 0.8;

                // Simple linear interpolation along control points for animation path
                const p1x = lerp(startX, controlX, progress);
                const p1y = lerp(startY, controlY, progress);
                const p2x = lerp(controlX, endX, progress);
                const p2y = lerp(controlY, endY, progress);
                 const p3x = lerp(p1x, p2x, progress);
                 const p3y = lerp(p1y, p2y, progress);


                ctx.moveTo(startX, startY);
                // Draw up to the current interpolated point
                ctx.quadraticCurveTo(controlX, controlY, p3x, p3y);


                ctx.strokeStyle = color;
                ctx.lineWidth = 5;
                ctx.lineCap = 'round';
                ctx.stroke();

                if (progress < 1) {
                    animationFrameId = requestAnimationFrame(animate);
                } else {
                    resolve();
                }
            };
             resultCtx.clearRect(0, 0, canvasSize, canvasSize);
             animationFrameId = requestAnimationFrame(animate);
         });
    }

     // Helper function to draw a basic hyperbola (stylized) with animation
    function drawHyperbola(ctx, x, y, sizeA, sizeB, color, duration = 600) {
         return new Promise(resolve => {
            const startTime = performance.now();
            const animate = (currentTime) => {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);

                ctx.strokeStyle = color;
                ctx.lineWidth = 5;
                ctx.lineCap = 'round';

                 // Draw upper curve
                 ctx.beginPath();
                 const uStartX = x - sizeB;
                 const uStartY = y - sizeA * 1.5;
                 const uControlX = x;
                 const uControlY = y - sizeA;
                 const uEndX = x + sizeB;
                 const uEndY = y - sizeA * 1.5;

                 const up1x = lerp(uStartX, uControlX, progress);
                 const up1y = lerp(uStartY, uControlY, progress);
                 const up2x = lerp(uControlX, uEndX, progress);
                 const up2y = lerp(uControlY, uEndY, progress);
                 const up3x = lerp(up1x, up2x, progress);
                 const up3y = lerp(up1y, up2y, progress);

                 ctx.moveTo(uStartX, uStartY);
                 ctx.quadraticCurveTo(uControlX, uControlY, up3x, up3y);
                 ctx.stroke();

                 // Draw lower curve (starts drawing only after upper is half-done?)
                 if (progress > 0.3) { // Start lower curve animation slightly delayed
                     const lowerProgress = Math.min((progress - 0.3) / 0.7, 1); // Normalize progress for lower curve
                     ctx.beginPath();
                     const lStartX = x - sizeB;
                     const lStartY = y + sizeA * 1.5;
                     const lControlX = x;
                     const lControlY = y + sizeA;
                     const lEndX = x + sizeB;
                     const lEndY = y + sizeA * 1.5;

                     const lp1x = lerp(lStartX, lControlX, lowerProgress);
                     const lp1y = lerp(lStartY, lControlY, lowerProgress);
                     const lp2x = lerp(lControlX, lEndX, lowerProgress);
                     const lp2y = lerp(lControlY, lEndY, lowerProgress);
                      const lp3x = lerp(lp1x, lp2x, lowerProgress);
                      const lp3y = lerp(lp1y, lp2y, lowerProgress);

                     ctx.moveTo(lStartX, lStartY);
                     ctx.quadraticCurveTo(lControlX, lControlY, lp3x, lp3y);
                     ctx.stroke();
                 }


                if (progress < 1) {
                    animationFrameId = requestAnimationFrame(animate);
                } else {
                    resolve();
                }
            };
            resultCtx.clearRect(0, 0, canvasSize, canvasSize);
            animationFrameId = requestAnimationFrame(animate);
         });
    }


    // Function to draw the simulation
    function drawSimulation() {
         // Cancel any ongoing animation frame
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }

        // Clear canvases
        sideViewCtx.clearRect(0, 0, canvasSize, canvasSize);
        resultCtx.clearRect(0, 0, canvasSize, canvasSize);

        // Get values from sliders
        const planeAngleDeg = parseFloat(planeAngleSlider.value);
        const planePosition = parseFloat(planePositionSlider.value); // distance from apex Y=0
        const coneAngleDeg = parseFloat(coneAngleSlider.value);

        // Update slider value displays
        planeAngleValueSpan.textContent = `${planeAngleDeg.toFixed(1)}°`;
        planePositionValueSpan.textContent = planePosition;
        coneAngleValueSpan.textContent = `${coneAngleDeg.toFixed(1)}°`;

        const planeAngleRad = degToRad(planeAngleDeg);
        const coneAngleRad = degToRad(coneAngleDeg);

        // --- Draw Side View ---
        sideViewCtx.save();
        sideViewCtx.translate(centerX, coneApexY); // Apex at center of canvas height

        // Draw cone axis
        sideViewCtx.strokeStyle = '#ccc';
        sideViewCtx.lineWidth = 1;
        sideViewCtx.beginPath();
        sideViewCtx.moveTo(0, -coneAxisLength / 2);
        sideViewCtx.lineTo(0, coneAxisLength / 2);
        sideViewCtx.stroke();

        // Draw cone outline (double cone)
        sideViewCtx.strokeStyle = '#555';
        sideViewCtx.lineWidth = 2;

        const coneHalfBase = coneAxisLength / 2 * Math.tan(coneAngleRad);

        // Upper cone
        sideViewCtx.beginPath();
        sideViewCtx.moveTo(0, 0); // Apex
        sideViewCtx.lineTo(coneHalfBase, -coneAxisLength / 2); // Top right edge
        sideViewCtx.moveTo(0, 0); // Apex
        sideViewCtx.lineTo(-coneHalfBase, -coneAxisLength / 2); // Top left edge
        sideViewCtx.stroke();

         // Lower cone
        sideViewCtx.beginPath();
        sideViewCtx.moveTo(0, 0); // Apex
        sideViewCtx.lineTo(coneHalfBase, coneAxisLength / 2); // Bottom right edge
        sideViewCtx.moveTo(0, 0); // Apex
        sideViewCtx.lineTo(-coneHalfBase, coneAxisLength / 2); // Bottom left edge
        sideViewCtx.stroke();

         // Draw Apex point
        sideViewCtx.fillStyle = '#555';
        sideViewCtx.beginPath();
        sideViewCtx.arc(0, 0, 4, 0, Math.PI * 2);
        sideViewCtx.fill();


        // Draw the slicing plane line
        sideViewCtx.strokeStyle = '#007bff'; // Blue for plane
        sideViewCtx.lineWidth = 3;

        // Plane equation in (x', y') relative to apex (0,0), rotated by planeAngleDeg from the y' axis
        // The line passes through (0, -planePosition) on the y' axis.
        // Equation: x' * sin(planeAngleRad) + (y' - (-planePosition)) * cos(planeAngleRad) = 0
        // x' * sin(planeAngleRad) + (y' + planePosition) * cos(planeAngleRad) = 0
        // y' + planePosition = -x' * sin(planeAngleRad) / cos(planeAngleRad) = -x' * tan(planeAngleRad)
        // y' = -tan(planeAngleRad) * x' - planePosition

        // Calculate line endpoints that span the canvas width
        const planeStartX = -centerX;
        const planeEndX = centerX;

        // y = -tan(angle) * x - pos
        const planeStartY = -Math.tan(planeAngleRad) * planeStartX - planePosition;
        const planeEndY = -Math.tan(planeAngleRad) * planeEndX - planePosition;

        sideViewCtx.beginPath();
        sideViewCtx.moveTo(planeStartX, planeStartY);
        sideViewCtx.lineTo(planeEndX, planeEndY);
        sideViewCtx.stroke();


         // Draw visual indicators: Plane angle and Position
        sideViewCtx.strokeStyle = '#e91e63'; // Pink for indicators
        sideViewCtx.lineWidth = 1;
        sideViewCtx.fillStyle = '#e91e63';
        sideViewCtx.font = '12px Heebo, sans-serif';
        sideViewCtx.textAlign = 'center';

        // Position line (vertical line from apex to plane intersection on axis)
        sideViewCtx.beginPath();
        sideViewCtx.moveTo(0, 0);
        sideViewCtx.lineTo(0, -planePosition);
        sideViewCtx.stroke();
         // Position label
         sideViewCtx.fillText(`${planePosition}`, 15, -planePosition - 5); // Offset slightly

        // Angle arc
        sideViewCtx.beginPath();
        sideViewCtx.arc(0, -planePosition, 30, -Math.PI / 2, -Math.PI / 2 + planeAngleRad, false); // Arc from vertical up to plane line
        sideViewCtx.stroke();
        // Angle label
        const angleLabelX = 30 * Math.cos(-Math.PI / 2 + planeAngleRad / 2);
        const angleLabelY = -planePosition + 30 * Math.sin(-Math.PI / 2 + planeAngleRad / 2);
        sideViewCtx.fillText(`${planeAngleDeg}°`, angleLabelX, angleLabelY);


        sideViewCtx.restore();


        // --- Determine and Draw Resulting Shape ---
        let shapeType = '';
        let shapeColor = '#333';
        let shapeDesc = '';

        const angleDifference = planeAngleDeg - coneAngleDeg;
        const tolerance = 0.5; // Degrees tolerance for 'equal'
        const apexTolerance = 10; // Vertical distance tolerance for "through apex"

        // Check for intersection range (simple approximation)
        // Check if the plane line intersects the cone lines within the drawn cone height
        const coneLineYAtCanvasEdge = coneAxisLength / 2;
        const planeYAtLeftEdge = -Math.tan(planeAngleRad) * (-centerX) - planePosition;
        const planeYAtRightEdge = -Math.tan(planeAngleRad) * centerX - planePosition;

        const planeMinY = Math.min(planeStartY, planeEndY);
        const planeMaxY = Math.max(planeStartY, planeEndY);

        const coneTopY = -coneAxisLength / 2;
        const coneBottomY = coneAxisLength / 2;

        // A simple check: does the plane cross the vertical range of the drawn cone?
        // This doesn't check if the plane *actually* intersects the cone surface in 3D space,
        // just if its line on the side view passes through the cone's drawn bounds.
        // For simplicity in this 2D simulation view, we rely primarily on angles and position relative to drawn cone boundaries.
        // A more robust check would involve calculating intersection points.
        // Let's use the planePosition relative to the cone boundary at x=0 (apex) and max X (canvas edge)

         const intersectionY_at_center = -planePosition; // Y-coord of plane at axis

         // Height of cone at canvas edge X=centerX
         const coneY_at_edge = coneAxisLength / 2;


         // Check if plane passes through the cone vertically
         const planePassesThroughCone = (intersectionY_at_center > -coneY_at_edge && intersectionY_at_center < coneY_at_edge)
                                        || (planeMinY < coneBottomY && planeMaxY > coneTopY)
                                        || (planeMinY < coneTopY && planeMaxY > coneBottomY); // Covers cases where the plane spans across the cone

         // Simplified degenerate check based on position relative to the drawn cone height
         const isNearDegeneratePosition = Math.abs(planePosition) > coneAxisLength / 2; // Plane is vertically beyond the drawn cone extent
         const isExactlyApex = Math.abs(planePosition) < apexTolerance; // Within apex tolerance


         if (isNearDegeneratePosition) {
              shapeType = 'אין חיתוך'; // Plane is too high or low relative to the drawn cone height
              shapeColor = '#888';
              shapeDesc = 'המישור רחוק מדי מהקודקוד או לא חותך את החרוט בתחום הנראה.';
              // Clear result canvas if no shape
               resultCtx.clearRect(0, 0, canvasSize, canvasSize);
         } else if (isExactlyApex) {
             shapeType = 'מקרה מנוון'; // Passes through apex
             shapeColor = '#888';
             shapeDesc = 'החיתוך עובר דרך קודקוד החרוט ויוצר צורה מנוונת (נקודה, קו או זוג קווים).';
             // Clear result canvas for degenerate case in this simplified view
             resultCtx.clearRect(0, 0, canvasSize, canvasSize);

         } else if (Math.abs(planeAngleDeg - 90) < tolerance) { // Perpendicular to axis
            shapeType = 'מעגל';
            shapeColor = '#007bff'; // Blue
            shapeDesc = 'המישור מאונך לציר החרוט וחותך נפח אחד בלבד.';
             // Draw a stylized circle. Size based on the 'height' of the cone at the intersection plane's Y.
             // This is still stylized, not mathematically derived radius.
             const circleRadius = (coneAxisLength/2 - Math.abs(planePosition)) * Math.tan(coneAngleRad) * drawingScale;
            drawEllipse(resultCtx, centerX, centerY, Math.max(circleRadius, 10), Math.max(circleRadius, 10), 0, shapeColor); // Ensure min size
        } else if (angleDifference > tolerance) { // Plane angle > cone angle (steeper plane relative to axis)
            shapeType = 'אליפסה';
            shapeColor = '#28a745'; // Green
            shapeDesc = 'המישור חותך נפח אחד בזווית גדולה מזווית החרוט ביחס לציר, ואינו מקביל לקו יצרן.';
             // Draw stylized ellipse. Stretch based on angle difference and intersection position.
            const baseSize = (coneAxisLength/2 - Math.abs(planePosition)) * drawingScale; // Size related to how far from apex (approx)
            const majorAxisScale = 1 / Math.sin(planeAngleRad); // Steeper plane -> more stretched ellipse projection
            const minorAxisScale = 1;
            const ellipseWidth = Math.max(baseSize * majorAxisScale * 0.5, 20); // Arbitrary scaling for visual effect
            const ellipseHeight = Math.max(baseSize * minorAxisScale * 0.5, 15);
             // Rotation relative to horizontal in result canvas based on plane angle
             const resultRotation = degToRad(90 - planeAngleDeg); // 90 deg plane = 0 deg rotation (circle), 0 deg plane = 90 deg rotation
            drawEllipse(resultCtx, centerX, centerY, ellipseWidth, ellipseHeight, resultRotation, shapeColor);
        } else if (Math.abs(angleDifference) < tolerance) { // Plane angle == cone angle (parallel to generator)
            shapeType = 'פרבולה';
            shapeColor = '#ff8800'; // Orange
            shapeDesc = 'המישור מקביל בדיוק לקו יצרן אחד של החרוט וחותך נפח אחד בלבד.';
             // Draw stylized parabola
            const parabolaSize = (coneAxisLength / 2 - Math.abs(planePosition)) * drawingScale * 0.7; // Size based on position
            drawParabola(resultCtx, centerX, centerY + parabolaSize * 0.2, Math.max(parabolaSize, 30), shapeColor); // Shift slightly down
        } else { // planeAngleDeg < coneAngleDeg (flatter plane or vertical), cuts both nappes
            shapeType = 'היפרבולה';
            shapeColor = '#dc3545'; // Red
            shapeDesc = 'המישור מקביל או בעל זווית קטנה מזווית החרוט ביחס לציר, וחותך את שני הנפחים.';
             // Draw stylized hyperbola
             const hyperbolaSize = (coneAxisLength / 2 - Math.abs(planePosition)) * drawingScale * 0.6; // Size based on position
             const sizeA = Math.max(hyperbolaSize * 0.7, 20);
             const sizeB = Math.max(hyperbolaSize * 0.5, 15);
            drawHyperbola(resultCtx, centerX, centerY, sizeA, sizeB, shapeColor);
        }

        // Update shape display
        currentShapeSpan.textContent = shapeType;
        currentShapeSpan.style.color = shapeColor;
        // Convert Hebrew shape names to a simple class slug for CSS
        const shapeClassSlug = shapeType.replace(/[^א-תa-zA-Z0-9]/g, '').replace('אין', 'no').replace('חיתוך', 'intersection').replace('מקרה', 'degenerate'); // handle Hebrew slugs
        currentShapeSpan.className = `shape-${shapeClassSlug}`;

        shapeDescriptionDiv.textContent = shapeDesc; // Update description
    }

    // Add event listeners to sliders
    // Using 'input' event for real-time updates
    planeAngleSlider.addEventListener('input', drawSimulation);
    planePositionSlider.addEventListener('input', drawSimulation);
    coneAngleSlider.addEventListener('input', drawSimulation);

     // Optional: Redraw on window resize to adjust scale? Can be complex.
     // window.addEventListener('resize', drawSimulation); // Uncomment if needed and handle resizing logic

    // Add event listener for the explanation button
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.opacity === '0';
        if (isHidden) {
             explanationDiv.style.display = 'block';
             // Force reflow to make transition work
             explanationDiv.offsetHeight;
             explanationDiv.classList.add('visible');
        } else {
             explanationDiv.classList.remove('visible');
             // Hide element after transition
             explanationDiv.addEventListener('transitionend', function handler() {
                 if (!explanationDiv.classList.contains('visible')) {
                     explanationDiv.style.display = 'none';
                 }
                 explanationDiv.removeEventListener('transitionend', handler);
             });
        }
    });


    // Initial drawing
    drawSimulation();
});
</script>