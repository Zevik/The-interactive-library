---
title: "העולם התת-ימי הסודי: מסע לגלים הפנימיים של האוקיינוס"
english_slug: the-hidden-waves-internal-waves-in-the-ocean
category: "אוקיינוגרפיה"
tags: [גלים פנימיים, אוקיינוס, שכבות צפיפות, הסתכבות, דינמיקת זורמים, גאות ושפל, אנרגיה אוקיינית]
---
# העולם התת-ימי הסודי: מסע לגלים הפנימיים של האוקיינוס

דמיינו לרגע את האוקיינוס. מה אתם רואים? כנראה גלי שטח מתנפצים על החוף או אדוות קטנות על פני מים שקטים. אבל מה אם נגיד לכם שעמוק בפנים, מתחת לפני הים השלווים לכאורה, מתחוללת תופעה גלית עוצמתית, נסתרת מן העין, שמניעה תהליכים בקנה מידה עולמי?

ברוכים הבאים לעולמם המסתורי של **הגלים הפנימיים** – גלים שמתפשטים לאורך שכבות הצפיפות השונות של המים, ולא על פני השטח. הם ענקיים, איטיים, ובעלי השפעה קריטית על כל מה שקורה במעמקי הים, מפיזור חומרים מזינים ועד השפעה על תנועת צוללות!

בואו נצלול פנימה ונחקור את הגלים הנסתרים הללו באמצעות הסימולציה האינטראקטיבית שלנו.

<div class="app-container">
    <div class="controls">
        <h2>שליטה בגלים הפנימיים</h2>
        <div class="control-group">
            <label for="stratification-strength">חוזק הסתכבות:</label>
            <div class="slider-container">
                <input type="range" id="stratification-strength" min="0.00001" max="0.0001" step="0.00001" value="0.00005">
                <span id="strat-value" class="value-display">0.00005</span>
            </div>
            <p class="control-hint">ככל שהסתכבות חזקה יותר (ערך N² גבוה יותר), כך הגלים הפנימיים נוטים להיות מהירים יותר וקצרים יותר. זהו ה"קפיץ" הפנימי של הזורם.</p>
        </div>

        <div class="control-group">
             <label for="flow-speed">מהירות זרם:</label>
            <div class="slider-container">
                <input type="range" id="flow-speed" min="0.05" max="0.5" step="0.01" value="0.2">
                <span id="flow-value" class="value-display">0.20</span>
            </div>
             <p class="control-hint">מהירות הזרם המניע את המים מעל המכשול התת-ימי. זרם מהיר יותר יכול ליצור גלים גדולים ומורכבים יותר.</p>
        </div>

        <div class="control-group">
            <label for="bump-height">גובה מכשול תת-ימי:</label>
            <div class="slider-container">
                <input type="range" id="bump-height" min="5" max="50" step="1" value="20">
                <span id="bump-value" class="value-display">20 מטר</span>
            </div>
            <p class="control-hint">גובה המכשול בקרקעית הים שמעורר את הגלים. מכשול גבוה יותר ייצור הפרעה גדולה יותר וגלים עם משרעת גבוהה יותר.</p>
        </div>

        <button id="start-sim" class="action-button">התחל/אפס סימולציה</button>
         <p class="simulation-status">לחץ "התחל/אפס" לראות את הגלים נוצרים!</p>
    </div>
    <div class="simulation-area">
        <canvas id="ocean-canvas"></canvas>
         <div class="visual-cue current-arrow">➡️</div>
         <div class="visual-cue stratification-indicator">
             <div class="indicator-bar"></div>
             <span class="indicator-label">N²</span>
         </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג עובדות מרתקות על גלים פנימיים</button>

<div id="explanation" class="explanation-content">
    <h2>מה מסתתר מתחת לפני הים? גלים פנימיים נחשפים!</h2>
    <p>שלא כמו גלי שטח המתפשטים בממשק בין מים לאוויר, גלים פנימיים הם תנודות המתקיימות <strong>בתוך</strong> נוזל או גז. באוקיינוס, הם נוצרים בתוך שכבות המים המסוּתּכּבות – כלומר, כאשר צפיפות המים משתנה עם העומק (לרוב כתוצאה משינויים בטמפרטורה או מליחות). השכבה שבה שינוי הצפיפות גדול במיוחד נקראת **פיקנוקלינה**.</p>

    <h3>מדוע צפיפות היא המפתח? (על כוח הציפה הפנימי)</h3>
    <p>הסתכבות חיונית לגלים פנימיים. דמיינו גוש מים שנמצא בשכבה מסוימת. אם כוח חיצוני (כמו זרם שפוגע במכשול תת-ימי) מזיז אותו מעט אנכית: אם הוא עולה לשכבה פחות צפופה, הוא כבד יותר מסביבתו וישקע חזרה למטה. אם הוא יורד לשכבה צפופה יותר, הוא קל יותר ויצוף חזרה למעלה. התנועה הזו, שנובעת מהפרשי הציפה הפנימיים, היא בדיוק כמו כוח הכבידה הפועל על גלי שטח – היא משמשת כ<strong>כוח מחזיר</strong> ומאפשרת תנודה גלית. ללא הסתכבות, כל הפרעה אנכית הייתה פשוט מתפזרת.</p>

    <h3>מי מעורר את הגלים הנסתרים? מקורות הגלים הפנימיים</h3>
    <p>גלים פנימיים נוצרים כשהשכבות המסותכבות מופרעות. המקורות העיקריים כוללים:</p>
    <ul>
        <li>🌊 **גאות ושפל:** זרמי גאות ושפל הזורמים מעל רכסים תת-ימיים או קצה המדף היבשתי הם מקור אנרגיה אדיר לגלים פנימיים, שיכולים להתפשט לאלפי קילומטרים!</li>
        <li>⛰️ **זרמים ומכשולים:** זרמי אוקיינוס שפוגשים הרי מצולה, רכסים או כל טופוגרפיה בולטת בקרקעית (כמו שמודגם בסימולציה).</li>
        <li>💨 **פעילות רוח וסערות:** למרות שיוצרים בעיקר גלי שטח, רוחות חזקות יכולות גם לעורר תנודות בשכבות העומק.</li>
        <li>🧊 **שינויי צפיפות מקומיים:** התמוססות קרח, מים מתוקים מנהרות או נגר, או התערבבות מי שפכים יכולים ליצור הפרעות צפיפות ראשוניות.</li>
    </ul>

    <h3>ענקים איטיים ועוצמתיים: מאפיינים והשפעות</h3>
    <p>הגלים הפנימיים נבדלים מאוד מגלי שטח:</p>
    <ul>
        <li>📏 **אורך גל:** עצום! יכול לנוע מעשרות מטרים ועד מאות קילומטרים.</li>
        <li>🐢 **מהירות:** איטית מאוד! בדרך כלל סנטימטרים בודדים לשנייה, מה שהופך אותם לקשים לצפייה מרחוק בזמן אמת.</li>
        <li>↕️ **משרעת:** ענקית! למרות שגובהם כמעט אינו מורגש על פני השטח, התנודה האנכית של שכבות הצפיפות יכולה להגיע לעשרות ואף מאות מטרים – עקירה עצומה של מסות מים!</li>
    </ul>
    <p>השפעתם דרמטית: הם מערבבים מים בין שכבות, מעבירים חום, מלחים, חמצן וחומרים מזינים לאורך וברוחב האוקיינוס, משפיעים על פיזור אורגניזמים ימיים (מפלנקטון זעיר ועד יצורים גדולים יותר הנעים עם השכבות), ואף משנים את אופן התפשטות גלי קול במים, מה שחשוב ביותר לסונאר ותקשורת תת-ימית.</p>

     <h3>חשיבות אקולוגית וגלובלית</h3>
    <p>ערבוב המים על ידי גלים פנימיים הוא תהליך קריטי. הוא מביא חומרים מזינים מהעומק אל השכבות העליונות המוארות, ומזין את הפוטוסינתזה שהיא בסיס שרשרת המזון הימית. בלעדיהם, חלקים גדולים מהאוקיינוס היו פחות פרודוקטיביים. הם גם ממלאים תפקיד בהעברת אנרגיה (שמגיעה ממקורות כמו גאות) במערכת האוקיינית כולה.</p>

    <p>אז בפעם הבאה שאתם ליד הים, זכרו: יש עולם שלם של גלים נסתרים ודינמיקות מורכבות שפועלות עמוק מתחת לפני השטח השקטים, ומעצבות את כדור הארץ שלנו בדרכים בלתי נראות אך עוצמתיות!</p>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

body {
    font-family: 'Rubik', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f7f6;
    margin: 0;
    padding: 20px;
}

h1, h2, h3 {
    color: #004080; /* Deep blue */
    margin-bottom: 0.5em;
}

h1 {
    text-align: center;
    color: #002a5c; /* Even deeper blue */
    margin-bottom: 20px;
    font-weight: 700;
}

p {
    margin-bottom: 1em;
}

.app-container {
    display: flex;
    flex-direction: column; /* Default to column on small screens */
    gap: 20px; /* Space between controls and simulation */
    margin: 20px auto;
    padding: 20px;
    border-radius: 12px;
    background-color: #ffffff; /* Clean white background */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    max-width: 900px; /* Max width for better readability */
    width: 100%;
    box-sizing: border-box; /* Include padding in width */
}

@media (min-width: 768px) { /* Arrange side-by-side on wider screens */
    .app-container {
        flex-direction: row;
    }
    .controls {
        flex: 1; /* Controls take 1 part of space */
        min-width: 300px; /* Ensure controls are not too narrow */
        max-width: 350px;
    }
    .simulation-area {
         flex: 2; /* Simulation takes 2 parts of space */
    }
}


.controls {
    padding: 15px;
    border-radius: 8px;
    background-color: #eef5ff; /* Light blue background */
    border: 1px solid #cce0ff; /* Matching border */
    display: flex;
    flex-direction: column;
    gap: 15px; /* Space between control groups */
}

.controls h2 {
    text-align: center;
    color: #0056b3; /* Medium blue */
    margin-top: 0;
    border-bottom: 1px solid #cce0ff;
    padding-bottom: 10px;
}

.control-group {
    margin-bottom: 10px;
}

.controls label {
    display: block; /* Label on its own line */
    margin-bottom: 8px;
    font-weight: 500;
    color: #004080; /* Deep blue */
}

.slider-container {
    display: flex;
    align-items: center;
    gap: 10px;
}

.controls input[type="range"] {
    flex-grow: 1; /* Slider takes available space */
    height: 5px; /* Thinner slider track */
    background: linear-gradient(to right, #007bff, #00c0ff); /* Gradient track */
    border-radius: 3px;
    outline: none;
    -webkit-appearance: none; /* Hide default slider */
    appearance: none;
    cursor: pointer;
}

/* Styling the thumb (handle) of the slider */
.controls input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 18px;
    height: 18px;
    background: #0056b3; /* Darker blue thumb */
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    margin-top: -6.5px; /* Center thumb vertically */
}

.controls input[type="range"]::-moz-range-thumb {
    width: 18px;
    height: 18px;
    background: #0056b3;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}


.value-display {
    display: inline-block;
    width: 70px; /* Fixed width for value */
    text-align: right;
    font-weight: 700;
    color: #0056b3;
    font-variant-numeric: tabular-nums; /* Align numbers */
}

.control-hint {
    font-size: 0.85em;
    color: #555;
    margin-top: 5px;
    padding-top: 5px;
    border-top: 1px dashed #eee;
}


.action-button {
    display: block;
    width: 100%; /* Full width button */
    margin-top: 15px;
    padding: 12px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: 500;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

.action-button:hover {
    background-color: #0056b3;
    transform: translateY(-1px);
}

.action-button:active {
     background-color: #003f80;
     transform: translateY(0);
}

.simulation-status {
    text-align: center;
    font-size: 0.9em;
    color: #555;
    margin-top: 10px;
}


.simulation-area {
    position: relative; /* Needed for absolute positioning of cues */
    background: linear-gradient(to bottom, #a0d8ef 0%, #1a5276 100%); /* Deep blue ocean gradient */
    border: 1px solid #004080; /* Darker border */
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 300px; /* Ensure area has some height */
}

#ocean-canvas {
    display: block;
    background-color: transparent; /* Canvas draws on top of gradient */
}

.visual-cue {
    position: absolute;
    padding: 5px 10px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 4px;
    font-size: 0.9em;
    color: #333;
    pointer-events: none; /* Don't interfere with mouse events on canvas */
    z-index: 10; /* Above canvas */
}

.current-arrow {
    top: 10px;
    left: 10px;
    font-size: 1.5em;
    background: none; /* No background for just the arrow */
    color: white; /* White arrow for visibility */
}

.stratification-indicator {
     bottom: 10px;
     right: 10px;
     background-color: rgba(255, 255, 255, 0.9);
     display: flex;
     align-items: center;
     gap: 5px;
     padding: 5px 8px;
}

.indicator-bar {
     width: 20px;
     height: 30px;
     background: linear-gradient(to top, #1a5276, #a0d8ef); /* Gradient representing density */
     border: 1px solid #333;
     border-radius: 2px;
}


.toggle-button {
    display: block;
    margin: 30px auto;
    padding: 12px 25px;
    background-color: #28a745; /* Green for explanation */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: 500;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

.toggle-button:hover {
    background-color: #218838;
    transform: translateY(-1px);
}
.toggle-button:active {
    background-color: #1e7e34;
    transform: translateY(0);
}


.explanation-content {
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #cce0ff; /* Light blue border */
    border-radius: 8px;
    background-color: #eef5ff; /* Light blue background */
    max-width: 900px;
    width: 100%;
    box-sizing: border-box;
    display: none; /* Initially hidden */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.explanation-content h2 {
    color: #0056b3;
    margin-top: 0;
    margin-bottom: 1em;
    border-bottom: 2px solid #cce0ff;
    padding-bottom: 10px;
}

.explanation-content h3 {
    color: #004080;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
}

.explanation-content ul {
    list-style-type: disc;
    margin-left: 25px;
    margin-bottom: 1em;
}

.explanation-content li {
    margin-bottom: 0.8em;
}

.explanation-content strong {
    color: #004080;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('ocean-canvas');
    const ctx = canvas.getContext('2d');
    const stratStrengthInput = document.getElementById('stratification-strength');
    const stratValueSpan = document.getElementById('strat-value');
    const flowSpeedInput = document.getElementById('flow-speed');
    const flowValueSpan = document.getElementById('flow-value');
    const bumpHeightInput = document.getElementById('bump-height');
    const bumpValueSpan = document.getElementById('bump-value');
    const startButton = document.getElementById('start-sim');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const simulationStatus = document.querySelector('.simulation-status');

    // Simulation parameters
    const canvasWidth = 600; // Fixed canvas size for simulation area
    const canvasHeight = 400;
    const oceanDepth = 300; // meters represented by canvasHeight
    const oceanWidth = 900; // meters represented by canvasWidth (longer than visible area)
    const gravity = 9.81; // m/s^2
    let stratificationN2 = parseFloat(stratStrengthInput.value); // Brunt-Väisälä frequency squared
    let flowSpeed = parseFloat(flowSpeedInput.value); // m/s
    let bumpHeight = parseFloat(bumpHeightInput.value); // meters
    const bumpWidth = 100; // meters (fixed width for simplicity)
    const bumpPositionX = oceanWidth / 3; // Position bump downstream from left edge
    const numDensityLayers = 20; // Fewer layers for clearer visualization
    const layerHeight = oceanDepth / numDensityLayers;

    // Scaling factors
    const xScale = canvasWidth / oceanWidth;
    const yScale = canvasHeight / oceanDepth;

    // Simulation state (vertical displacement of density layer interfaces)
    let layerDisplacements = []; // Array of arrays: layerDisplacements[layerIndex][xIndex]
    let simulationTime = 0; // seconds
    const timeStep = 1; // seconds per simulation step (larger for visual speed)
    const advectionSpeedFactor = 0.8; // Slightly slow down advection visually
    const waveDecayFactor = 0.99; // Decay waves over time
    const initialBumpInfluenceDecay = 0.9; // How fast initial bump influence decays away

    // Particle system (for visual flow and displacement)
    const numParticles = 100;
    let particles = [];

    // Initialize state
    function resetSimulation() {
        stratificationN2 = parseFloat(stratStrengthInput.value);
        flowSpeed = parseFloat(flowSpeedInput.value);
        bumpHeight = parseFloat(bumpHeightInput.value);
        simulationTime = 0;
        simulationStatus.textContent = 'סימולציה פועלת...';

        layerDisplacements = [];
        for (let i = 0; i < numDensityLayers; i++) {
             // Initialize with zero displacement
            layerDisplacements[i] = new Array(canvasWidth).fill(0);
        }

        // Initialize particles
        particles = [];
        for(let i = 0; i < numParticles; i++) {
             particles.push({
                 x: Math.random() * oceanWidth, // Random initial horizontal position
                 y: Math.random() * oceanDepth, // Random initial vertical position
                 color: `rgba(255, 255, 255, ${0.3 + Math.random() * 0.4})`, // Semi-transparent white
                 size: 1 + Math.random() * 1.5 // Random size
             });
        }

        // Apply initial bump displacement - simplified model
        // This creates an initial wave packet that then propagates/advects
        for (let i = 0; i < numDensityLayers; i++) {
             const initialDepth = (i + 0.5) * layerHeight; // Depth of interface i
             const depthFactor = Math.exp(-initialDepth / 100); // Influence decreases with depth

             for (let x = 0; x < canvasWidth; x++) {
                 const oceanX = x / xScale; // Convert canvas x to ocean x
                 const bumpProfile = calculateBumpHeight(oceanX);
                 // Initial displacement proportional to bump height and depth factor, scaled by flow/strat
                 // This is still a simplification, not a physics solution
                 const displacement = bumpProfile * depthFactor * (flowSpeed > 0 ? 1 : 0) * (1000 * stratificationN2 < 0.1 ? 1 : 0.5); // Scale by flow and weakly by strat
                 layerDisplacements[i][x] = -displacement * yScale; // Negative displacement means pushed upwards, scale by yScale
             }
         }
    }

    // Calculate the height of the bump at a given ocean x-coordinate
    function calculateBumpHeight(oceanX) {
        const bumpStartX = bumpPositionX;
        const bumpEndX = bumpPositionX + bumpWidth;
        if (oceanX > bumpStartX && oceanX < bumpEndX) {
            // Smoother bump shape (e.g., Gaussian-like or raised cosine)
            const relativeX = (oceanX - bumpStartX) / bumpWidth; // 0 to 1
            // Use a raised cosine: 0.5 * (1 - cos(2 * PI * relativeX)) gives 0 at start/end, 1 in middle
             return bumpHeight * 0.5 * (1 - Math.cos(Math.PI * relativeX * 2));
        }
        return 0;
    }

    // Update simulation state (simplified propagation and advection)
    function updateSimulation(dt) {
        // Advect displacements horizontally by the flow speed
        const advectionDistanceOcean = flowSpeed * dt * advectionSpeedFactor; // Distance in ocean units moved by flow
        const pixelsToShift = advectionDistanceOcean * xScale;

        const newDisplacements = [];
        for(let i = 0; i < numDensityLayers; i++) {
            newDisplacements[i] = new Array(canvasWidth);
            for(let x = 0; x < canvasWidth; x++) {
                // Calculate source position considering advection
                const sourceX = x - pixelsToShift;
                let value;
                if (sourceX < 0) {
                    // Points entering from the left - assume zero initial displacement or gentle inflow
                    value = 0;
                } else if (sourceX >= canvasWidth - 1) {
                    // Points exiting on the right - extrapolate or assume decay
                    value = layerDisplacements[i][canvasWidth - 1] * waveDecayFactor; // Simple decay
                } else {
                    // Linear interpolation between source pixels
                    const x1 = Math.floor(sourceX);
                    const x2 = x1 + 1;
                    const frac = sourceX - x1;
                    if (x2 < canvasWidth) {
                         value = (1 - frac) * layerDisplacements[i][x1] + frac * layerDisplacements[i][x2];
                    } else {
                         value = layerDisplacements[i][x1]; // Just take the last point if x2 is out
                    }
                    // Apply general wave decay
                    value *= waveDecayFactor;
                }
                newDisplacements[i][x] = value;
            }
        }
        layerDisplacements = newDisplacements;

        // Continuously generate new displacement over the bump for visualization
        // Blend new bump influence with existing displacement near the bump
        const bumpCenterXOcean = bumpPositionX + bumpWidth/2;
        for (let i = 0; i < numDensityLayers; i++) {
            const initialDepth = (i + 0.5) * layerHeight;
            const depthFactor = Math.exp(-initialDepth / 100);
            for (let x = 0; x < canvasWidth; x++) {
                 const oceanX = x / xScale;
                 const bumpProfile = calculateBumpHeight(oceanX);
                 const newBumpDisplacement = -bumpProfile * depthFactor * yScale * (flowSpeed > 0 ? 1 : 0) * (1000 * stratificationN2 < 0.1 ? 1 : 0.5);

                 // Create a blending zone around the bump
                 const distanceToBumpCenter = Math.abs(oceanX - bumpCenterXOcean);
                 const blendZone = bumpWidth * 1.5; // Blend over 3x the bump width
                 const blendFactor = Math.max(0, 1 - distanceToBumpCenter / blendZone); // 1 at center, 0 outside zone

                 // Weighted average: more bump influence near the bump, more advected wave elsewhere
                 layerDisplacements[i][x] = (1 - blendFactor) * layerDisplacements[i][x] + blendFactor * newBumpDisplacement;

                 // Decay the initial wave influence over time/distance from the bump source
                 const distanceAfterBump = Math.max(0, oceanX - (bumpPositionX + bumpWidth));
                 layerDisplacements[i][x] *= Math.exp(-distanceAfterBump / 500 * (1 / Math.sqrt(stratificationN2 * 1000))); // Decay factor sensitive to distance and stratification
            }
        }


        // Update particle positions
        for(let i = 0; i < numParticles; i++) {
             // Advect particle horizontally
             particles[i].x += flowSpeed * dt * advectionSpeedFactor;

             // Find the displacement of the nearest density layer at the particle's x position
             const canvasParticleX = particles[i].x * xScale;
             const canvasParticleY = particles[i].y * yScale;
             const layerIndex = Math.floor(particles[i].y / layerHeight);
             let displacementY = 0;
             if (layerIndex >= 0 && layerIndex < numDensityLayers) {
                 // Linearly interpolate displacement based on canvas X
                 const x1 = Math.floor(canvasParticleX);
                 const x2 = Math.min(canvasWidth - 1, x1 + 1);
                 const frac = canvasParticleX - x1;
                 let d1 = 0, d2 = 0;
                 if (x1 >= 0 && x1 < canvasWidth) d1 = layerDisplacements[layerIndex][x1];
                 if (x2 >= 0 && x2 < canvasWidth) d2 = layerDisplacements[layerIndex][x2];

                 displacementY = (1 - frac) * d1 + frac * d2;
             }

             // Update particle's vertical position based on original depth + displacement
             // The particles follow the *shape* of the wave, not the *velocity* field (simplification)
             const originalDepth = particles[i].y; // Y in ocean coordinates is original depth
             const newOceanY = originalDepth + displacementY / yScale; // Add displacement (converted back to ocean units)

             // Ensure particle stays within reasonable vertical bounds
             particles[i].y = Math.max(0, Math.min(oceanDepth, newOceanY));


             // Wrap particles around horizontally
             if (particles[i].x > oceanWidth) {
                 particles[i].x = 0;
                 particles[i].y = Math.random() * oceanDepth; // Reset y randomly for new inflow
             }
        }


        simulationTime += dt;
    }

    // Draw the simulation state
    function drawSimulation() {
        // Clear canvas
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Draw stratified background gradient is done via CSS on simulation-area div

        // Draw filled density layers
        for (let i = 0; i < numDensityLayers - 1; i++) {
            ctx.beginPath();
            const initialDepth1 = (i + 0.5) * layerHeight;
            const initialDepth2 = (i + 1.5) * layerHeight;

            const initialY1 = initialDepth1 * yScale;
            const initialY2 = initialDepth2 * yScale;

            // Move to the starting point of the upper boundary of the layer
            ctx.moveTo(0, initialY1 + layerDisplacements[i][0]);

            // Draw the upper boundary following the displacement
            for (let x = 1; x < canvasWidth; x++) {
                ctx.lineTo(x, initialY1 + layerDisplacements[i][x]);
            }

            // Draw the right edge down to the lower boundary
            ctx.lineTo(canvasWidth - 1, initialY2 + layerDisplacements[i+1][canvasWidth - 1]);

            // Draw the lower boundary (reversed direction)
            for (let x = canvasWidth - 2; x >= 0; x--) {
                ctx.lineTo(x, initialY2 + layerDisplacements[i+1][x]);
            }

            // Close the path to the starting point of the lower boundary
            ctx.lineTo(0, initialY2 + layerDisplacements[i+1][0]);

            // Set fill style based on layer depth (visual proxy for density)
            // Use a color scale from light blue to dark blue
            const colorIntensity = i / (numDensityLayers - 1); // 0 for top, 1 for bottom
            const r = Math.floor(160 - colorIntensity * 140); // Decrease R
            const g = Math.floor(216 - colorIntensity * 160); // Decrease G
            const b = Math.floor(239 - colorIntensity * 160); // Decrease B
            ctx.fillStyle = `rgba(${r}, ${g}, ${b}, 0.4)`; // Semi-transparent fill

            ctx.fill();

            // Optionally draw the boundaries (lines) for definition
             ctx.strokeStyle = `rgba(255, 255, 255, ${0.2 + colorIntensity * 0.3})`; // Fainter white lines, more visible lower down
             ctx.lineWidth = 0.5;
             ctx.stroke();
        }

         // Draw particles
        ctx.fillStyle = 'white'; // Particles are white
        for(let i = 0; i < numParticles; i++) {
             const p = particles[i];
             const canvasX = p.x * xScale;
             const canvasY = p.y * yScale; // Particle Y is already its actual vertical position

             ctx.beginPath();
             ctx.arc(canvasX, canvasY, p.size, 0, Math.PI * 2);
             ctx.fillStyle = p.color;
             ctx.fill();
        }


        // Draw the bump (fixed obstacle)
        ctx.fillStyle = '#8B4513'; // Brown color for seabed/obstacle
        ctx.beginPath();
        ctx.moveTo(0, canvasHeight); // Start at bottom left

        // Draw the seabed before the bump
        const bumpStartXCanvas = bumpPositionX * xScale;
        ctx.lineTo(bumpStartXCanvas, canvasHeight);

        // Draw points to define the bump profile on the canvas
        const numBumpPoints = 50;
        for(let j = 0; j <= numBumpPoints; j++) {
             const oceanX = bumpPositionX + (bumpWidth * j / numBumpPoints);
             const bumpH = calculateBumpHeight(oceanX);
             const canvasX = oceanX * xScale;
             const canvasY = canvasHeight - bumpH * yScale;
             ctx.lineTo(canvasX, canvasY);
        }

        // Draw the seabed after the bump
        const bumpEndXCanvas = (bumpPositionX + bumpWidth) * xScale;
        ctx.lineTo(canvasWidth, canvasHeight - calculateBumpHeight(oceanWidth) * yScale); // Draw up to the right edge height (should be 0)


        ctx.lineTo(canvasWidth, canvasHeight); // Go to bottom right
        ctx.closePath(); // Close the path back to bottom left
        ctx.fill();
    }

    // Animation loop
    let lastTime = 0;
    let animationFrameId = null;
    let isAnimating = false;

    function animate(currentTime) {
        if (!isAnimating) {
            lastTime = 0; // Reset lastTime when stopping/starting
             return; // Stop the loop if not animating
        }
        if (!lastTime) lastTime = currentTime;
        const elapsed = (currentTime - lastTime) / 1000; // elapsed time in seconds
        lastTime = currentTime;

        const simDt = timeStep; // Use a fixed time step for the simulation update regardless of frame rate
        updateSimulation(simDt); // Update simulation state
        drawSimulation(); // Draw the new state

        animationFrameId = requestAnimationFrame(animate); // Continue animation
    }

    function startSimulation() {
         if (!isAnimating) {
             resetSimulation();
             isAnimating = true;
             simulationStatus.textContent = 'סימולציה פועלת...';
             animationFrameId = requestAnimationFrame(animate);
         } else {
             // If already animating, treat 'Start' as 'Reset'
             resetSimulation();
         }
    }

    function stopSimulation() {
        if (isAnimating) {
            cancelAnimationFrame(animationFrameId);
            isAnimating = false;
            simulationStatus.textContent = 'סימולציה מושהית.';
        }
    }


    // Event Listeners
    stratStrengthInput.addEventListener('input', (event) => {
        stratValueSpan.textContent = parseFloat(event.target.value).toFixed(5);
    });

    flowSpeedInput.addEventListener('input', (event) => {
        flowValueSpan.textContent = parseFloat(event.target.value).toFixed(2);
    });

     bumpHeightInput.addEventListener('input', (event) => {
        bumpValueSpan.textContent = parseFloat(event.target.value).toFixed(0) + ' מטר';
    });


    startButton.addEventListener('click', startSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר עובדות מרתקות' : 'הצג עובדות מרתקות על גלים פנימיים';
    });

    // Initial setup
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;
    // Draw initial state (before simulation starts)
    resetSimulation();
    drawSimulation(); // Draw the initial state with parameters but before any steps
    simulationStatus.textContent = 'מוכן. לחץ "התחל/אפס סימולציה"';
});
</script>
```