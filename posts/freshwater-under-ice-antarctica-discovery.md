---
title: "מים מתוקים מתחת לקרח: התגלית המפתיעה באנטארקטיקה"
english_slug: freshwater-under-ice-antarctica-discovery
category: "מדעי הסביבה / אוקיינוגרפיה"
tags:
  - אנטארקטיקה
  - מדפי קרח
  - אגמים תת-קרחיים
  - מים מתוקים
  - גלציולוגיה
---
<h1>מים מתוקים מתחת לקרח: התגלית המפתיעה באנטארקטיקה</h1>
<p>דמיינו נוף צחיח וקפוא, אלפי מטרים של קרח דחוס מעליכם. האם הייתם מצפים למצוא כאן מקווה מים תוסס, מלא במי שתייה צלולים? צללו עמוק מתחת למדפי הקרח העצומים של אנטארקטיקה וגלו את הסוד החבוי.</p>
<p>השתמשו בסליידרים כדי לחקור כיצד עומק הקרח, מבנה התחתית וטמפרטורת המים משפיעים על התנאים ויוצרים אגמי מים מתוקים.</p>

<div id="simulation-container">
    <canvas id="iceShelfCanvas" width="800" height="500"></canvas>
    <div id="controls">
        <h2>שליטה בסביבה האנטארקטית</h2>
        <div class="control-group">
            <label for="iceDepth">עובי מדף הקרח (ממוצע, מטרים):</label>
            <input type="range" id="iceDepth" min="500" max="2500" value="1500"> <span id="iceDepthValue">1500</span> מ'
        </div>
         <div class="control-group">
            <label for="depressionDepth">עומק השקע התת-קרחי (מטרים):</label>
            <input type="range" id="depressionDepth" min="0" max="150" value="75"> <span id="depressionDepthValue">75</span> מ'
        </div>
        <div class="control-group">
            <label for="salinity">מליחות מי ים (חלקי אלף):</label>
            <input type="range" id="salinity" min="28" max="36" value="34.5" step="0.1"> <span id="salinityValue">34.5</span> ppt
        </div>
        <div class="control-group">
            <label for="waterTemp">טמפרטורת מי ים (°C):</label>
            <input type="range" id="waterTemp" min="-3.0" max="1.0" value="-1.8" step="0.1"> <span id="waterTempValue">-1.8</span> °C
        </div>
        <div id="info">
            <h3>תנאים בנקודות מפתח:</h3>
            <p><strong>מגע קרח-ים (בסיס רדוד):</strong><br>לחץ משוער: <span id="pressureSeawater">...</span> מגהפסקל<br>נקודת קיפאון מי ים: <span id="freezingPoint">-1.80</span> °C<br>מצב: <span id="statusSeawater"></span></p>
             <p><strong>בתוך שקע המים (בסיס עמוק יותר):</strong><br>לחץ משוער: <span id="pressureFreshwater">...</span> מגהפסקל<br>נקודת קיפאון מים מתוקים: <span id="freshFreezingPoint">0.00</span> °C<br>מצב: <span id="statusFreshwater"></span></p>
        </div>
    </div>
</div>

<button id="toggleExplanation" class="btn-info">מה בעצם קורה כאן? (הסבר)</button>

<div id="explanation" style="display: none;">
    <h2>מים מתוקים מתחת לקרח: כיצד הם נוצרים?</h2>
    <p>מדפי הקרח של אנטארקטיקה הם יריעות קרח עצומות הצפות על פני הים, חלקן מחוברות ליבשת. עוביים יכול להגיע למאות או אלפי מטרים, ושטחם ענק.</p>
    <p>תחתית מדף הקרח נמצאת במגע תמידי עם מי הים. נקודה קריטית להבנת התהליך היא ההשפעה של לחץ על נקודת הקיפאון של מים. ככל שהלחץ גבוה יותר (כתוצאה מעומק הקרח והמים מעל), כך נקודת הקיפאון יורדת. במילים אחרות, מים יכולים להישאר במצב נוזלי גם בטמפרטורות מתחת לאפס מעלות צלזיוס בלחצים גבוהים.</p>
    <p>בגלל הלחץ העצום בתחתית מדף הקרח, נקודת הקיפאון המקומית נמוכה יותר מאשר בלחץ אטמוספרי רגיל. אם טמפרטורת מי הים במגע גבוהה מנקודת הקיפאון המקומית (אף על פי שהיא מתחת לאפס!), הקרח בתחתית המדף נמס.</p>
    <p>תהליך הפשרת קרח מפריד בין מולקולות המים למולקולות המלחים. הקרח עצמו מורכב כמעט אך ורק ממים מתוקים. כשהוא נמס, הוא יוצר מים נוזליים מתוקים.</p>
    <p>מים מתוקים פחות צפופים ממי ים מלוחים. לכן, המים המתוקים המומסים נוטים לעלות כלפי מעלה. אם בתחתית מדף הקרח קיימים שקעים או אזורים נמוכים (כתוצאה מתנועת הקרח, שחיקה או התמוטטות), המים המתוקים הפחות צפופים יכולים להילכד ולהצטבר בשקעים אלו, במקום להתערבב מיד עם מי הים המלוחים.</p>
    <p>בתוך השקעים הלכודים, טמפרטורת המים עשויה לרדת. מכיוון שהם כעת מים מתוקים (או מעט מלוחים), נקודת הקיפאון שלהם גבוהה יותר מנקודת הקיפאון של מי הים המלוחים באותו לחץ. כאשר טמפרטורת המים הלכודים יורדת מתחת לנקודת הקיפאון החדשה (הקרובה ל-0°C בלחץ הגבוה), הם קופאים מחדש ויוצרים שכבות קרח חדשות בתחתית המדף. גם תהליך הקפיאה הזה מפריד מלחים, ולכן הקרח החדש הוא שוב קרח מתוק יחסית.</p>
    <p>התהליך הוא מחזורי: קרח מומס, יוצר מים מתוקים, המים נלכדים, קופאים מחדש ויוצרים קרח מתוק, ותנועת הקרח הכוללת מזיזה את המדף וממשיכה לחשוף אזורים חדשים לתהליכים אלו ולשנות את טופוגרפיית התחתית.</p>
    <p>גילוי אגמי מים מתוקים אלו ותפקידם עדיין נחקר. הם עשויים להשפיע על יציבות מדפי הקרח ועל זרימת הקרח לכיוון הים, ודרכם להשפיע על עליית פני הים ועל מחזור האקלים העולמי.</p>
</div>

<style>
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f7f6;
    padding: 20px;
}

h1, h2, h3 {
    color: #0056b3;
    text-align: center;
    margin-bottom: 15px;
}

p {
    margin-bottom: 15px;
}

#simulation-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    margin-bottom: 30px;
    align-items: stretch; /* Stretch items to fill container height */
    background-color: #fff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

#controls {
    flex: 1;
    min-width: 300px;
    max-width: 400px; /* Give controls a max width */
    padding: 20px;
    border-radius: 8px;
    background-color: #eef7ff; /* Lighter blue background for controls */
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
}

.control-group {
    margin-bottom: 20px;
    background-color: #ffffff; /* White background for each control */
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #cce0ff; /* Light blue border */
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.control-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: #004085; /* Darker blue text */
    font-size: 0.95em;
}

.control-group input[type="range"] {
    width: calc(100% - 70px); /* Adjust width to make space for value */
    vertical-align: middle;
    -webkit-appearance: none; /* Remove default styling */
    appearance: none;
    height: 8px;
    background: #b3d9ff; /* Light blue track */
    outline: none;
    opacity: 0.7;
    transition: opacity .2s;
    border-radius: 5px;
}

.control-group input[type="range"]:hover {
    opacity: 1;
}

.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 18px;
    height: 18px;
    background: #007bff; /* Bright blue thumb */
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

.control-group input[type="range"]::-moz-range-thumb {
    width: 18px;
    height: 18px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}


.control-group span {
    display: inline-block;
    width: 60px; /* Fixed width for values */
    text-align: right;
    vertical-align: middle;
    font-weight: bold;
    color: #004085;
}

#info {
    margin-top: auto; /* Push info to the bottom if controls grow */
    padding-top: 15px;
    border-top: 1px dashed #cce0ff; /* Dashed border */
    color: #004085;
    font-size: 0.9em;
}

#info h3 {
    margin-top: 0;
    color: #004085;
    font-size: 1.1em;
}

#info p {
    margin-bottom: 8px;
}

#info span {
    font-weight: normal; /* Don't bold the values */
}

#iceShelfCanvas {
    background-color: #e0f7fa; /* Very light blue for open ocean/background */
    flex-grow: 1;
    max-width: 100%; /* Ensure canvas is responsive */
    height: auto; /* Maintain aspect ratio */
    border-radius: 8px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
}

.btn-info {
    display: block;
    margin: 20px auto;
    padding: 12px 25px;
    font-size: 1em;
    cursor: pointer;
    background-color: #007bff; /* Primary blue */
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.btn-info:hover {
    background-color: #0056b3; /* Darker blue on hover */
}

.btn-info:active {
     transform: scale(0.98); /* Subtle press effect */
}


#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #cce0ff;
    border-radius: 8px;
    background-color: #eef7ff; /* Same as controls background */
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

#explanation h2 {
    color: #0056b3;
    margin-top: 0;
}

/* Status colors */
.status-green { color: green; font-weight: bold; }
.status-red { color: red; font-weight: bold; }
.status-grey { color: grey; }

@media (max-width: 768px) {
    #simulation-container {
        flex-direction: column;
        align-items: center;
    }
    #controls {
        min-width: 95%;
        max-width: 95%;
    }
    #iceShelfCanvas {
        width: 100%;
    }
}
</style>

<script>
const canvas = document.getElementById('iceShelfCanvas');
const ctx = canvas.getContext('2d');
const iceDepthSlider = document.getElementById('iceDepth');
const iceDepthValueSpan = document.getElementById('iceDepthValue');
const depressionDepthSlider = document.getElementById('depressionDepth');
const depressionDepthValueSpan = document.getElementById('depressionDepthValue');
const salinitySlider = document.getElementById('salinity');
const salinityValueSpan = document.getElementById('salinityValue');
const waterTempSlider = document.getElementById('waterTemp');
const waterTempValueSpan = document.getElementById('waterTempValue');
const freezingPointSpan = document.getElementById('freezingPoint');
const freshFreezingPointSpan = document.getElementById('freshFreezingPoint');
const pressureSeawaterSpan = document.getElementById('pressureSeawater');
const pressureFreshwaterSpan = document.getElementById('pressureFreshwater');
const statusSeawaterSpan = document.getElementById('statusSeawater');
const statusFreshwaterSpan = document.getElementById('statusFreshwater');
const toggleExplanationButton = document.getElementById('toggleExplanation');
const explanationDiv = document.getElementById('explanation');

// Constants for drawing and simulation
const ICE_COLOR = '#B3E5FC'; // Light sky blue for ice
const SEAWATER_COLOR = '#0277BD'; // Deep blue for seawater
const FRESHWATER_COLOR = '#81C784'; // Soft green for freshwater pool
const REFREEZE_COLOR = '#4FC3F7'; // Lighter blue for refrozen ice
const INTERFACE_COLOR = '#455A64'; // Dark grey for ice base line
const MELT_COLOR = '#FF9800'; // Orange for melting effect
const FREEZE_COLOR = '#E1F5FE'; // Very light blue for freezing effect

// Simulation parameters (default values match slider)
let iceDepth = parseInt(iceDepthSlider.value); // meters
let depressionDepth = parseInt(depressionDepthSlider.value); // meters
let salinity = parseFloat(salinitySlider.value); // ppt
let waterTemp = parseFloat(waterTempSlider.value); // °C

// Physical constants (simplified)
const ICE_DENSITY = 920; // kg/m³
const SEAWATER_DENSITY = 1025; // kg/m³
const GRAVITY = 9.81; // m/s²
const ATM_PRESSURE = 101325; // Pascals (approx 1 atm)
const PRESSURE_FREEZING_EFFECT = -7.5e-8; // °C per Pascal (approx)
const SALINITY_FREEZING_EFFECT = -0.057; // °C per ppt (approx)

// Animation variables
let animationTime = 0;
const animationSpeed = 0.05; // Speed of animation changes

function calculatePressure(iceThickness, waterDepthBelowIce) {
    // Simple model: pressure at a point is sum of hydrostatic pressure from ice above it
    // and hydrostatic pressure from the water column *below* the ice base down to that point.
    // For simplicity here, we'll use pressure due to the ice column + a nominal water depth *outside* the depression,
    // or the ice column + the depression depth for the deep point. This is a significant simplification
    // as isostasy and ocean depth below the shelf are complex factors.
    // Let's refine: Pressure at base is dominated by ice thickness.
    // P ≈ ρ_ice * g * h_ice
    return (iceThickness * ICE_DENSITY * GRAVITY) + ATM_PRESSURE; // Add ATM pressure for total pressure
}

function calculatePressureAtDepression(iceThickness, depressionDepth) {
     // Pressure at the bottom of the depression is roughly ice pressure + pressure of water *within* the depression
     // A better approximation: Pressure is from the total column weight above that point.
     // Let's just use ice depth as the dominant factor for pressure variations under the shelf for simplicity.
     // Pressure is higher at the bottom of the depression due to extra water depth there.
     // Simplified: Pressure is proportional to the distance from the top of the ice shelf.
     // Total "depth" = iceThickness + depressionDepth
     return calculatePressure(iceThickness + depressionDepth * (SEAWATER_DENSITY / ICE_DENSITY), 0); // Scale water depth by density ratio to approximate effective ice thickness
}


function calculateSaltwaterFreezingPoint(pressure_pascals, salinity_ppt) {
    // Freezing point relative to pure water at 1 atm (0°C)
    const baseFreeze1atm = SALINITY_FREEZING_EFFECT * salinity_ppt; // Effect of salinity
    const pressureEffect = PRESSURE_FREEZING_EFFECT * (pressure_pascals - ATM_PRESSURE); // Effect of pressure above 1 atm
    return baseFreeze1atm + pressureEffect;
}

function calculateFreshFreezingPoint(pressure_pascals) {
    // Freezing point of pure water at 1 atm is 0°C
    const pressureEffect = PRESSURE_FREEZING_EFFECT * (pressure_pascals - ATM_PRESSURE); // Effect of pressure above 1 atm
    return 0.0 + pressureEffect;
}


function drawSimulation(timestamp) {
    if (!timestamp) timestamp = 0; // Handle initial call
    const deltaTime = timestamp - animationTime;
    animationTime = timestamp;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const canvasHeight = canvas.height;
    const canvasWidth = canvas.width;
    const iceTop = canvasHeight * 0.1; // Top of the ice shelf visual

    // Visual scale: Map ice depth to a visual proportion on the canvas
    const maxVisualIceDepth = canvasHeight * 0.7; // Max height the ice block can take visually
    // Scale ice depth (500-2500m) to visual thickness
    const visualIceThickness = (iceDepth - 500) / (2500 - 500) * maxVisualIceDepth + canvasHeight * 0.1; // Min visual thickness

    // Draw main ice shelf block
    ctx.fillStyle = ICE_COLOR;
    ctx.fillRect(0, iceTop, canvasWidth, visualIceThickness);

    // Draw seawater below
    ctx.fillStyle = SEAWATER_COLOR;
    const averageBaseY = iceTop + visualIceThickness; // Y coordinate representing average base level
    const seawaterVisualDepth = canvasHeight - averageBaseY; // Space available for water

    // Use a slight gradient for water depth
    const seaGradient = ctx.createLinearGradient(0, averageBaseY, 0, canvasHeight);
    seaGradient.addColorStop(0, SEAWATER_COLOR);
    seaGradient.addColorStop(1, '#01579B'); // Darker blue at depth
    ctx.fillStyle = seaGradient;
    ctx.fillRect(0, averageBaseY, canvasWidth, seawaterVisualDepth);


    // --- Draw the ice-ocean interface profile ---
    ctx.beginPath();
    ctx.strokeStyle = INTERFACE_COLOR;
    ctx.lineWidth = 3; // Thicker line for base
    ctx.lineJoin = 'round'; // Smoother corners

    const depressionCenterX = canvasWidth / 2;
    const depressionWidthPx = canvasWidth * 0.5; // Width of the depression area in pixels
    // Scale depression depth (0-150m) to visual depth. Let's map 150m to a significant dip.
    const maxVisualDepressionDepth = seawaterVisualDepth * 0.6; // Max visual depth of depression
    const depressionDepthPx = (depressionDepth / 150) * maxVisualDepressionDepth;

    // Add subtle animation to the base line
    const baseAnimation = Math.sin(animationTime * animationSpeed * 2) * (depressionDepthPx * 0.05); // Small sine wave effect


    ctx.moveTo(0, averageBaseY + baseAnimation);

    for (let x = 0; x <= canvasWidth; x++) {
        let y = averageBaseY;
        // Apply depression shape (smoothed curve)
        const distToCenter = Math.abs(x - depressionCenterX);
        if (distToCenter < depressionWidthPx / 2) {
            const progress = (1 - (distToCenter / (depressionWidthPx / 2))); // 1 at center, 0 at edges
             // Smooth curve: Use a power like progress^2 or progress^3 for a softer dip
            y = averageBaseY + depressionDepthPx * Math.pow(progress, 2);
        }
         ctx.lineTo(x, y + baseAnimation); // Apply base animation
    }
    ctx.stroke();


    // --- Calculate Statuses ---
    // Pressure at the average base level (dominated by ice depth)
    const pressureSeawater = calculatePressure(iceDepth, 0);
    const saltwaterFreezeTemp = calculateSaltwaterFreezingPoint(pressureSeawater, salinity);

    // Pressure at the deepest part of the depression (dominated by ice depth + depression depth)
    // We use a simplified model here, assuming pressure increases roughly linearly with total depth from surface.
    const pressureFreshwater = calculatePressureAtDepression(iceDepth, depressionDepth);
    const freshFreezeTemp = calculateFreshFreezingPoint(pressureFreshwater);

    // Update info panel
    pressureSeawaterSpan.textContent = (pressureSeawater / 1e6).toFixed(2); // Convert Pa to MPa
    pressureFreshwaterSpan.textContent = (pressureFreshwater / 1e6).toFixed(2); // Convert Pa to MPa
    freezingPointSpan.textContent = saltwaterFreezeTemp.toFixed(2);
    freshFreezingPointSpan.textContent = freshFreezeTemp.toFixed(2);


    let meltOccurs = waterTemp > saltwaterFreezeTemp;
    let refreezeOccurs = false;
    let freshwaterPoolExists = false;

    // Update status text
    if (meltOccurs) {
        statusSeawaterSpan.textContent = "המסה (Melt)";
        statusSeawaterSpan.className = 'status-green';
    } else {
        statusSeawaterSpan.textContent = "קפיאה (Freeze)";
        statusSeawaterSpan.className = 'status-red';
    }

    if (depressionDepth > 0 && meltOccurs) {
        freshwaterPoolExists = true;
        // Check for refreezing within the freshwater pool
        if (waterTemp < freshFreezeTemp) { // Water temp below freshwater freezing point
            refreezeOccurs = true;
            statusFreshwaterSpan.textContent = "קפיאה מחדש (Refreeze)";
            statusFreshwaterSpan.className = 'status-red';
        } else {
            statusFreshwaterSpan.textContent = "נוזלי (מים מתוקים)";
            statusFreshwaterSpan.className = 'status-green';
        }
    } else {
         statusFreshwaterSpan.textContent = "אין שקע / אין מים מתוקים";
         statusFreshwaterSpan.className = 'status-grey';
    }


    // --- Draw Simulation Elements based on Status ---

    // Draw freshwater pool if conditions met
    if (freshwaterPoolExists) {
         ctx.fillStyle = FRESHWATER_COLOR;
         const poolHorizontalExtentPx = depressionWidthPx * 0.8; // Pool is slightly narrower visually than depression
         const poolStartX = depressionCenterX - poolHorizontalExtentPx/2;
         const poolEndX = depressionCenterX + poolHorizontalExtentPx/2;

         ctx.beginPath();
         // Draw the top contour of the pool by following the ice base curve within the pool extent
         for(let x = poolStartX; x <= poolEndX; x++) {
              const distToCenter = Math.abs(x - depressionCenterX);
               let y = averageBaseY;
              if (distToCenter < depressionWidthPx / 2) {
                const progress = (1 - (distToCenter / (depressionWidthPx / 2)));
                y = averageBaseY + depressionDepthPx * Math.pow(progress, 2);
              } else if (x < depressionCenterX) { // Left edge transition
                 const transitionProgress = (x - (depressionCenterX - depressionWidthPx / 2)) / (depressionWidthPx/2 - poolHorizontalExtentPx/2);
                 y = averageBaseY + depressionDepthPx * Math.pow(transitionProgress, 2); // Simplified transition curve
              } else { // Right edge transition
                 const transitionProgress = ( (depressionCenterX + depressionWidthPx / 2) - x) / (depressionWidthPx/2 - poolHorizontalExtentPx/2);
                  y = averageBaseY + depressionDepthPx * Math.pow(transitionProgress, 2); // Simplified transition curve
              }
               // Ensure y is within reasonable bounds and follows the depression shape
               const baseCurveY = averageBaseY + (distToCenter < depressionWidthPx/2 ? depressionDepthPx * Math.pow((1 - (distToCenter / (depressionWidthPx / 2))), 2) : 0);
              ctx.lineTo(x, baseCurveY + baseAnimation); // Follow the animated ice base contour
         }

         // Draw the bottom contour of the pool (simplified: a smoothed line below the ice base)
         const poolBottomY = averageBaseY + depressionDepthPx * 0.9; // Fill up to 90% of depression visual depth
         ctx.bezierCurveTo(
             depressionCenterX + poolHorizontalExtentPx/3, poolBottomY + depressionDepthPx*0.1, // Control point 1
             depressionCenterX - poolHorizontalExtentPx/3, poolBottomY + depressionDepthPx*0.1, // Control point 2
             poolStartX, poolBottomY // End point
         );
         ctx.closePath();
         ctx.fill();

         // Add density arrows animation
         if (meltOccurs && depressionDepth > 0) {
             ctx.fillStyle = 'rgba(255, 255, 255, 0.5)'; // White arrows, semi-transparent
             ctx.strokeStyle = 'rgba(255, 255, 255, 0.8)';
             ctx.lineWidth = 1;
             const arrowSize = 8;
             const numArrows = 5;
             for(let i = 0; i < numArrows; i++) {
                 const x = poolStartX + (poolHorizontalExtentPx / numArrows) * i + (poolHorizontalExtentPx / numArrows) / 2;
                 // Y position varies over time and space
                 const arrowBaseY = poolBottomY - (i % 2) * 10 + Math.sin(animationTime * animationSpeed + i * 0.5) * 5;
                 const baseCurveY = averageBaseY + (Math.abs(x - depressionCenterX) < depressionWidthPx/2 ? depressionDepthPx * Math.pow((1 - (Math.abs(x - depressionCenterX) / (depressionWidthPx / 2))), 2) : 0);

                 // Draw arrow pointing up
                 if (arrowBaseY > baseCurveY + baseAnimation + arrowSize*1.5) { // Only draw if space allows
                     ctx.beginPath();
                     ctx.moveTo(x, arrowBaseY);
                     ctx.lineTo(x - arrowSize/2, arrowBaseY - arrowSize);
                     ctx.moveTo(x, arrowBaseY);
                     ctx.lineTo(x + arrowSize/2, arrowBaseY - arrowSize);
                     ctx.stroke();
                     // Optional: fill arrowhead
                     // ctx.lineTo(x, arrowBaseY - arrowSize * 1.5);
                     // ctx.closePath();
                     // ctx.fill();
                 }
             }
         }


        // Draw refrozen layer if conditions met
        if (refreezeOccurs) {
             ctx.fillStyle = REFREEZE_COLOR;
             ctx.beginPath();
             const refreezeThicknessPx = 8; // Visual thickness

             // Draw along the top contour (ice base within pool extent)
             for(let x = poolStartX; x <= poolEndX; x++) {
                 const distToCenter = Math.abs(x - depressionCenterX);
                 const baseCurveY = averageBaseY + (distToCenter < depressionWidthPx/2 ? depressionDepthPx * Math.pow((1 - (distToCenter / (depressionWidthPx / 2))), 2) : 0);
                 ctx.lineTo(x, baseCurveY + baseAnimation);
             }
             // Draw the bottom edge of the refrozen layer (slightly below the ice base contour)
              for(let x = poolEndX; x >= poolStartX; x--) {
                 const distToCenter = Math.abs(x - depressionCenterX);
                 const baseCurveY = averageBaseY + (distToCenter < depressionWidthPx/2 ? depressionDepthPx * Math.pow((1 - (distToCenter / (depressionWidthPx / 2))), 2) : 0);
                 ctx.lineTo(x, baseCurveY + baseAnimation + refreezeThicknessPx * Math.sin(animationTime * animationSpeed * 3 + x * 0.01) * 0.5 + refreezeThicknessPx * 0.5); // Wavy bottom edge animation
             }
             ctx.closePath();
             ctx.fill();
        }
    }

     // Add visual indicators (melt/freeze icons/effects)
    const indicatorSize = 20; // Size of icons/effects
    const indicatorY = averageBaseY - indicatorSize/2;

    ctx.font = 'bold 24px Arial';
    ctx.textAlign = 'center';

    if (meltOccurs) {
         // Draw melting effect (orange drips/shimmer) along the base
         ctx.fillStyle = MELT_COLOR + '80'; // Semi-transparent orange
         const dripHeight = 10;
         const dripWidth = 3;
         const numDrips = canvasWidth / 20; // Number of potential drips
         for (let i = 0; i < numDrips; i++) {
              const x = i * 20 + (animationTime * animationSpeed * 10) % 20; // Animate horizontal movement
              const baseCurveY = averageBaseY + (Math.abs(x - depressionCenterX) < depressionWidthPx/2 ? depressionDepthPx * Math.pow((1 - (Math.abs(x - depressionCenterX) / (depressionWidthPx / 2))), 2) : 0);
              if (Math.random() < 0.1 + Math.sin(animationTime * animationSpeed * 5 + i)*0.05) { // Random drips with slight wave
                  ctx.fillRect(x, baseCurveY + baseAnimation, dripWidth, dripHeight + Math.sin(animationTime * animationSpeed * 7 + i*0.3) * 5);
              }
         }
         // Draw Melt Icon
         // ctx.fillStyle = MELT_COLOR;
         // ctx.fillText('💧', canvasWidth * 0.1, indicatorY);
    } else {
         // Draw freezing effect (light blue crystals/shimmer)
          ctx.fillStyle = FREEZE_COLOR + '80'; // Semi-transparent light blue
           const crystalSize = 5;
           const numCrystals = canvasWidth / 10;
           for (let i = 0; i < numCrystals; i++) {
               const x = i * 10 + (animationTime * animationSpeed * -5) % 10; // Animate horizontal movement
               const baseCurveY = averageBaseY + (Math.abs(x - depressionCenterX) < depressionWidthPx/2 ? depressionDepthPx * Math.pow((1 - (Math.abs(x - depressionCenterX) / (depressionWidthPx / 2))), 2) : 0);
               if (Math.random() < 0.1 + Math.sin(animationTime * animationSpeed * 6 + i)*0.08) { // Random crystals with slight wave
                   ctx.fillRect(x, baseCurveY + baseAnimation - crystalSize, crystalSize, crystalSize);
               }
           }
         // Draw Freeze Icon
         // ctx.fillStyle = SEAWATER_COLOR;
         // ctx.fillText('❄️', canvasWidth * 0.1, indicatorY);
    }

    // Draw status for freshwater pool
    if (freshwaterPoolExists) {
         const poolCenterY = averageBaseY + depressionDepthPx * 0.5;
         if (refreezeOccurs) {
             // Draw Refreeze Icon/Effect
              // ctx.fillStyle = REFREEZE_COLOR;
              // ctx.fillText('❄️', depressionCenterX, poolCenterY);
         } else {
             // Draw Freshwater Icon/Effect
              // ctx.fillStyle = FRESHWATER_COLOR;
              // ctx.fillText('💧', depressionCenterX, poolCenterY);
         }
    }


    // Request next frame
    requestAnimationFrame(drawSimulation);
}

// Event listeners for sliders
iceDepthSlider.addEventListener('input', (event) => {
    iceDepth = parseInt(event.target.value);
    iceDepthValueSpan.textContent = iceDepth;
    // drawSimulation(); // Animation loop handles redrawing
});

depressionDepthSlider.addEventListener('input', (event) => {
    depressionDepth = parseInt(event.target.value);
    depressionDepthValueSpan.textContent = depressionDepth;
    // drawSimulation();
});

salinitySlider.addEventListener('input', (event) => {
    salinity = parseFloat(event.target.value);
    salinityValueSpan.textContent = salinity.toFixed(1);
    // drawSimulation();
});

waterTempSlider.addEventListener('input', (event) => {
    waterTemp = parseFloat(event.target.value);
    waterTempValueSpan.textContent = waterTemp.toFixed(1);
    // drawSimulation();
});

// Event listener for explanation button
toggleExplanationButton.addEventListener('click', () => {
    if (explanationDiv.style.display === 'none') {
        explanationDiv.style.display = 'block';
        toggleExplanationButton.textContent = 'הסתר הסבר';
    } else {
        explanationDiv.style.display = 'none';
        toggleExplanationButton.textContent = 'מה בעצם קורה כאן? (הסבר)';
    }
});


// Initial drawing and start animation loop
drawSimulation(0);

</script>
```