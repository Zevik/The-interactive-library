---
title: "הסכנה השקופה: מדוע עצירה בדרך למעלה מצילה צוללנים?"
english_slug: the-invisible-danger-why-stopping-on-the-way-up-saves-divers
category: "פיזיולוגיה"
tags:
  - צלילה
  - דקומפרסיה
  - לחץ
  - חוק הנרי
  - מחלת לחץ
---
# הצלילה הגדולה: סוד הבועות והדרך הבטוחה מעלה

דמיינו שאתם עמוק בים, מוקפים בלחץ אדיר. האוויר שאתם נושמים מדהים, אבל מה קורה לגזים שלו בתוך הגוף שלכם, כשאתם תחת עומס כזה? ולמה עלייה מהירה מדי לפני השטח היא מתכון לאסון? בואו נצלול לזה!

<div class="diving-simulation">
    <div class="water">
        <div class="surface">
             <div class="waves"></div>
             <span>פני המים (0 מטר)</span>
        </div>
        <div class="safety-stop-line">
             <span>עצירת בטיחות מומלצת (5 מטר)</span>
        </div>
        <div class="diver">
            <div class="diver-body"></div>
            <div class="diver-head"></div>
            <div class="breathing-bubbles"></div> <!-- Bubbles while breathing -->
        </div>
         <div class="seabed">קרקעית הים (30 מטר)</div>
    </div>
    <div class="controls">
        <div class="status">
            <div>עומק: <span id="depth">0.0</span> מטר</div>
            <div>קצב אנכי: <span id="ascent-rate">0.0</span> מטר/דקה</div>
            <div>חנקן מומס: <span id="gas-level">0</span>%</div>
            <div>מצב: <span id="gas-status">מוכן</span></div>
        </div>
        <label for="speed-slider">שלטו על קצב העלייה/ירידה:</label>
        <input type="range" id="speed-slider" min="-15" max="15" value="0" step="0.5">
        <div class="slider-labels">
            <span>ירידה מהירה (-15 מ'/דק')</span>
            <span>עצירה (0 מ'/דק')</span>
            <span>עלייה מהירה (+15 מ'/דק')</span>
        </div>
        <button id="start-dive">התחילו צלילה (ל-30מ')</button>
    </div>
     <div class="danger-indicator" style="display: none;">סכנה! בועות חנקן! האטו מיד!</div>
     <div class="safe-message" style="display: none;">צלילה בטוחה הסתיימה! כל הכבוד!</div>
     <div class="unsafe-message" style="display: none;">סיום צלילה מסוכנת! סיכון למחלת לחץ עקב עלייה מהירה מדי!</div>
</div>

<button id="toggle-explanation" style="margin-top: 20px;">הצג הסבר מדעי</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מדעי: פיזיקה, פיזיולוגיה ובועות קטלניות</h2>

    <h3>איך הלחץ מתגבר כשאנחנו צוללים?</h3>
    <p>מעל פני הים, אנחנו חווים לחץ אטמוספרי אחד (כ-1 בר או 1 אטמ'). כשאנחנו צוללים, עמוד המים מעלינו מוסיף לחץ. כל 10 מטרים עומק מוסיפים לחץ ששווה בערך ללחץ האטמוספרי. לכן, בעומק 10 מטרים הלחץ הכולל הוא 2 אטמ', בעומק 20 מטרים הוא 3 אטמ', ובעומק 30 מטרים הלחץ הוא 4 אטמ'. הלחץ הזה משפיע דרמטית על הגזים שאנו נושמים.</p>

    <h3>הגיבור השקט והרשע הפוטנציאלי: חמצן וחנקן באוויר דחוס</h3>
    <p>האוויר שאנחנו נושמים מורכב בעיקר מחמצן (כ-21%) ומחנקן (כ-78%). בצלילה, אנו נושמים אוויר דחוס בהרכב דומה. החמצן חיוני ומנוצל על ידי הגוף. ה"בעיה" היא החנקן: הוא גז אינרטי שאינו משמש את הגוף, אך התנהגותו תחת לחץ היא המפתח להבנת הסכנה.</p>

    <h3>חוק הנרי בפעולה: החנקן חודר לגוף</h3>
    <p>כאן נכנס לתמונה "חוק הנרי". הוא אומר שככל שלחץ הגז מעל נוזל גבוה יותר, כך יותר גז יתמוסס בנוזל הזה (בהנחה שהטמפרטורה קבועה). תחת לחץ העומק, הלחץ החלקי של החנקן באוויר שאנו נושמים גבוה מאוד. החנקן הזה "נדחף" מהריאות לדם (שהוא נוזל), ומשם לכל רקמות הגוף (בעיקר שומן ושרירים), ומתחיל להצטבר בהן בצורה מומסת. ככל שהצלילה עמוקה וארוכה יותר, כך יותר חנקן מצטבר ברקמות, עד שהן מגיעות ל"רוויה" (Maximum saturation under that pressure).</p>

    <h3>הסכנה האמיתית: ירידת לחץ מהירה ו"רתיחת" החנקן</h3>
    <p>בעת עלייה, הלחץ החיצוני יורד במהירות. אם עולים מהר מדי, הלחץ ברקמות (של החנקן המומס) גבוה בהרבה מהלחץ החיצוני. החנקן העודף, שאינו יכול להישאר מומס בלחץ הנמוך, ממהר לצאת מהתמיסה. במקום להתפזר באיטיות דרך הדם לריאות, הוא יוצר בועות גז קטנות וגדולות בתוך הרקמות ובכלי הדם. תחשבו על פתיחת בקבוק קולה מוגז – כל הבועות שמשתחררות בפתאומיות. בגוף, התהליך הזה מסוכן פי כמה!</p>

    <h3>מחלת הדקומפרסיה (DCS): המחיר של בועות בגוף</h3>
    <p>היווצרות בועות החנקן הזו היא למעשה מחלת הדקומפרסיה (Deco Sickness). הבועות עלולות לחסום זרימת דם, ללחוץ על עצבים, לגרום לדלקת ולפגוע בתפקוד איברים. התסמינים נעים מכאבים קלים, פריחות ועייפות, ועד שיתוק, פגיעה מוחית, קשיי נשימה ובמקרים קיצוניים - מוות. חומרת המחלה תלויה בכמות, גודל ומיקום הבועות.</p>

    <h3>הפתרון המציל חיים: עצירות דקומפרסיה</h3>
    <p>המפתח להימנעות מ-DCS הוא לאפשר לחנקן העודף לצאת מהרקמות בצורה איטית ומבוקרת. זה נעשה באמצעות עלייה איטית מאוד לאורך כל הצלילה, ובעיקר באמצעות עצירות דקומפרסיה יזומות בדרך למעלה. עצירת בטיחות סטנדרטית מתבצעת בעומק 5 מטרים למשך 3-5 דקות בסוף הצלילה. בעומק זה, הלחץ נמוך מספיק כדי שהחנקן יתחיל להתפנות ביעילות דרך הריאות, אך עדיין גבוה מספיק כדי למנוע מהבועות להיווצר בפתאומיות ולהפוך למסוכנות. בצלילות עמוקות או ארוכות יותר, יידרשו עצירות דקומפרסיה נוספות וממושכות יותר בעומקים שונים, בהתאם לכללי הבטיחות.</p>

    <h3>לסיכום: סבלנות שווה חיים</h3>
    <p>הסימולציה מראה בפשטות איך עלייה מהירה מדי גורמת לחנקן "לפרוץ" מהרקמות וליצור בועות מסוכנות. עלייה איטית ועצירות דקומפרסיה נותנות לגוף את הזמן החיוני לפנות את החנקן העודף בבטחה. תכנון נכון, שמירה על קצב עלייה איטי וביצוע עצירות בטיחות הן כללי יסוד חיוניים בכל צלילה, גם רדודה יחסית, והן ההבדל בין חוויה מדהימה למצב מסכן חיים.</p>
</div>

<style>
/* Enhanced Styling */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #e9f5f9; /* Light background */
    padding: 20px;
}

h1, h2, h3 {
    color: #0056b3;
    text-align: center;
    margin-bottom: 15px;
}

h1 {
    color: #003366;
}

.diving-simulation {
    width: 100%;
    max-width: 650px; /* Slightly wider */
    margin: 30px auto;
    border: 1px solid #007bff; /* More prominent border */
    border-radius: 12px; /* More rounded corners */
    overflow: hidden;
    display: flex;
    flex-direction: column;
    background-color: #ffffff; /* White background for controls */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    position: relative; /* For danger indicator overlay */
}

.water {
    position: relative;
    width: 100%;
    height: 450px; /* Represents ~30m depth visually + seabed */
    background: linear-gradient(to bottom, #87CEEB 0%, #1E90FF 50%, #004080 100%); /* Deeper blue gradient */
    overflow: hidden;
    transition: background-color 0.5s ease; /* Smooth transition for danger flash */
}

.water.danger {
     background: linear-gradient(to bottom, #ff6347 0%, #ff0000 100%); /* Red gradient for danger */
}


.surface {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 30px; /* Taller surface area */
    background-color: rgba(135, 206, 235, 0.6); /* Semi-transparent sky blue */
    text-align: center;
    line-height: 30px;
    font-size: 0.9em;
    color: #003366;
    font-weight: bold;
    overflow: hidden;
}

.waves {
    position: absolute;
    top: 0;
    left: 0;
    width: 200%; /* Wider for animation */
    height: 100%;
    background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 10" preserveAspectRatio="none"><path fill="rgba(255,255,255,0.5)" d="M0 5 Q 10 0, 20 5 T 40 5 T 60 5 T 80 5 T 100 5 V 100 H 0 Z"/></svg>') repeat-x bottom;
    background-size: 50% 100%; /* Adjust size */
    animation: wave-motion 10s linear infinite;
}

@keyframes wave-motion {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}


.seabed {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 40px; /* Taller seabed */
    background-color: #8B4513; /* SaddleBrown */
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20"><defs><filter id="f"><feTurbulence type="fractalNoise" baseFrequency="0.01 0.1" numOctaves="2" result="noise"/><feDisplacementMap in="SourceGraphic" in2="noise" scale="5" xChannelSelector="R" yChannelSelector="G"/></filter></defs><rect width="100" height="20" fill="#A0522D"/><rect width="100" height="20" fill="#8B4513" style="filter:url(#f)"/></svg>'); /* Simple sandy texture */
    background-size: cover;
    text-align: center;
    line-height: 40px;
    color: white;
    font-size: 0.9em;
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}

.safety-stop-line {
    position: absolute;
     /* Calculation based on waterVisualHeight = 450 - 40 = 410px for 30m */
     /* 1m = 410/30 = 13.67px */
     /* 5m depth means 25m above seabed (30-5=25) */
     /* bottom = seabedHeight + 25 * visualMeterRatio = 40 + 25 * 13.67 = 40 + 341.75 = 381.75px */
    bottom: calc(40px + (30 - 5) * (410px / 30)); /* Position for 5m mark */
    left: 0;
    width: 100%;
    border-top: 2px dashed #FFD700; /* Gold dashed line */
    text-align: right;
    padding-right: 15px;
    box-sizing: border-box;
    color: #FFD700;
    font-size: 0.85em;
    font-weight: bold;
    z-index: 10;
    transform: translateY(-1px);
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}


.diver {
    position: absolute;
    bottom: 450px; /* Start at surface visually (bottom of water container) */
    left: 50%;
    transform: translateX(-50%) scale(1); /* Center and scale */
    width: 40px; /* Slightly larger diver */
    height: 50px;
    z-index: 15; /* Above lines */
    transition: bottom linear, transform 0.3s ease; /* Smooth movement and potential scaling */
    display: flex;
    flex-direction: column;
    align-items: center;
}

.diver-body {
    width: 30px;
    height: 35px;
    background-color: #00BFFF; /* Deep Sky Blue */
    border-radius: 8px;
    border: 2px solid #000080; /* Navy border */
}

.diver-head {
    width: 20px;
    height: 20px;
    background-color: #FFB6C1; /* Light Pink skin tone */
    border-radius: 50%;
    margin-top: -5px; /* Overlap slightly */
    border: 2px solid #000080;
    position: relative;
}

.breathing-bubbles {
    position: absolute;
    bottom: 0; /* Start from mouth area */
    width: 20px;
    height: 20px;
    left: 50%;
    transform: translateX(-50%);
    overflow: hidden;
    pointer-events: none;
}

.breathing-bubble {
     position: absolute;
     width: 4px;
     height: 4px;
     background-color: rgba(255, 255, 255, 0.7);
     border-radius: 50%;
     opacity: 0;
     animation: breath-bubble-float 3s linear infinite;
}

@keyframes breath-bubble-float {
    0% { transform: translate(-50%, 0) scale(0.5); opacity: 0; }
    10% { opacity: 1; }
    90% { transform: translate(-50%, -50px) scale(1.2); opacity: 0.8; }
    100% { transform: translate(-50%, -70px) scale(1.5); opacity: 0; }
}

.bubble-area {
    position: absolute;
    top: -60px; /* Position above diver */
    left: -30px; /* Around the diver */
    width: 100px;
    height: 100px;
    pointer-events: none; /* Allow clicks through */
    overflow: hidden; /* Hide bubbles outside this area */
    opacity: 0; /* Start hidden */
    transition: opacity 0.5s ease-in-out;
     z-index: 5; /* Below diver */
}

.bubble {
    position: absolute;
    width: 6px; /* Slightly larger bubbles */
    height: 6px;
    background-color: rgba(200, 200, 255, 0.8); /* Lighter blue bubbles */
    border-radius: 50%;
    animation: bubble-float linear infinite;
    box-shadow: 0 0 3px rgba(255,255,255,0.5);
}

@keyframes bubble-float {
    0% { transform: translateY(0) scale(0.8); opacity: 1; }
    100% { transform: translateY(-80px) scale(1.5); opacity: 0; }
}

.controls {
    padding: 20px;
    background-color: #ffffff;
    border-top: 1px solid #ddd;
}

.status {
    margin-bottom: 15px;
    font-size: 1em;
    display: grid;
    grid-template-columns: 1fr 1fr; /* Two columns */
    gap: 10px; /* Space between items */
}

.status div {
    margin-bottom: 0; /* Remove margin */
    padding: 5px;
    background-color: #f8f9fa; /* Light background for status items */
    border-radius: 4px;
    border: 1px solid #e9ecef;
}
.status span {
    font-weight: bold;
    color: #007bff;
}

.status #gas-status {
    font-weight: bold;
     color: inherit; /* Default */
}


#speed-slider {
    width: 100%;
    margin: 10px 0;
     -webkit-appearance: none;
     appearance: none;
     height: 8px;
     background: #ddd;
     outline: none;
     opacity: 0.7;
     transition: opacity .2s;
     border-radius: 5px;
}

#speed-slider::-webkit-slider-thumb {
     -webkit-appearance: none;
     appearance: none;
     width: 20px;
     height: 20px;
     background: #007bff;
     cursor: pointer;
     border-radius: 50%;
     border: 2px solid #fff;
     box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}
#speed-slider::-moz-range-thumb {
     width: 20px;
     height: 20px;
     background: #007bff;
     cursor: pointer;
     border-radius: 50%;
     border: 2px solid #fff;
     box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

.slider-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.8em;
    color: #555;
    margin-bottom: 15px;
    padding: 0 5px;
}

button {
    display: block;
    width: auto;
    padding: 12px 20px;
    margin: 15px auto 0;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

button:hover {
    background-color: #0056b3;
}

button:active {
    transform: scale(0.98);
}

button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}


.danger-indicator, .safe-message, .unsafe-message {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 15px 20px;
    border-radius: 8px;
    font-size: 1.2em;
    font-weight: bold;
    text-align: center;
    z-index: 20;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.danger-indicator {
    background-color: #dc3545; /* Red */
    color: white;
    animation: pulse 1.5s infinite;
}

.safe-message {
     background-color: #28a745; /* Green */
     color: white;
}

.unsafe-message {
     background-color: #ffc107; /* Yellow */
     color: #343a40;
     border: 1px solid #d39e00;
}


@keyframes pulse {
    0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
    50% { transform: translate(-50%, -50%) scale(1.05); opacity: 0.9; }
    100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
}


#toggle-explanation {
    display: block;
    width: auto;
    margin: 20px auto;
    background-color: #6c757d; /* Gray */
}
#toggle-explanation:hover {
     background-color: #5a6268;
}

#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #007bff;
    border-radius: 8px;
    background-color: #e9f5f9; /* Light blueish background */
}

#explanation h2 {
    color: #0056b3;
    margin-top: 0;
    border-bottom: 2px solid #007bff;
    padding-bottom: 10px;
    margin-bottom: 15px;
    text-align: left;
}

#explanation h3 {
    color: #007bff;
    margin-top: 20px;
    margin-bottom: 8px;
    font-size: 1.1em;
}

#explanation p {
    line-height: 1.7;
    margin-bottom: 12px;
    text-align: justify;
}

</style>

<script>
const diver = document.querySelector('.diver');
const water = document.querySelector('.water'); // Get the water div
const depthDisplay = document.getElementById('depth');
const ascentRateDisplay = document.getElementById('ascent-rate');
const gasLevelDisplay = document.getElementById('gas-level');
const gasStatusDisplay = document.getElementById('gas-status');
const dangerIndicator = document.querySelector('.danger-indicator');
const safeMessage = document.querySelector('.safe-message');
const unsafeMessage = document.querySelector('.unsafe-message');
const bubbleArea = document.querySelector('.bubble-area');
const breathingBubblesArea = document.querySelector('.breathing-bubbles');
const speedSlider = document.getElementById('speed-slider');
const startDiveButton = document.getElementById('start-dive');
const explanationDiv = document.getElementById('explanation');
const toggleExplanationButton = document.getElementById('toggle-explanation');

// Simulation parameters
const totalVisualHeight = 450; // Height of .water div
const seabedHeight = 40; // Visual height of seabed
const waterVisualHeight = totalVisualHeight - seabedHeight; // Visual height representing water column
const maxDepth = 30; // Meters
const visualMeterRatio = waterVisualHeight / maxDepth; // Pixels per meter of depth

const surfaceBottomPx = totalVisualHeight - diver.offsetHeight / 2; // Diver center at surface line
const seabedBottomPx = seabedHeight - diver.offsetHeight / 2; // Diver center at seabed line

let currentDepth = 0; // meters
let currentBottomPx = surfaceBottomPx; // pixels
let verticalRate = 0; // meters per minute (+ for ascent, - for descent)
let dissolvedGasLevel = 0; // Simulated percentage 0-100, representing nitrogen supersaturation potential

let isDiving = false;
let animationFrameId = null;
let lastUpdateTime = performance.now();
let timeAtDepthSimulated = 0; // To simulate gas loading before ascent

// Gas simulation parameters (tuned for better effect)
const maxGasAtMaxDepth = 90; // Max theoretical gas level achievable at maxDepth
const gasLoadingRate = 0.05; // Rate factor for gas loading per second (exponential)
const gasUnloadingRate = 0.03; // Base rate factor for gas unloading per second
const ascentAffectsUnloadingFactor = 0.5; // How much rapid ascent hinders unloading (higher = more hindered)

const bubbleThreshold = 25; // Supersaturation level to start generating bubbles
const dangerThreshold = 50; // Supersaturation level for danger warning

function updateSimulation(currentTime) {
    if (!isDiving) return;

    const deltaTime = (currentTime - lastUpdateTime) / 1000; // Delta time in seconds
    lastUpdateTime = currentTime;

    // Update position based on vertical rate
    const verticalRatePxPerSec = (verticalRate / 60) * visualMeterRatio; // Pixels per second
    currentBottomPx += verticalRatePxPxPerSec * deltaTime; // Note: positive rate is ascent, so ADD to bottom px

    // Clamp position between seabed and surface
    currentBottomPx = Math.max(seabedBottomPx, Math.min(surfaceBottomPx, currentBottomPx));
    diver.style.bottom = `${currentBottomPx}px`;

    // Calculate current depth from visual bottom position (diver's center)
    // depth = 30 - (visualBottom - seabedBottomPx) / visualMeterRatio
    currentDepth = maxDepth - (currentBottomPx - seabedBottomPx) / visualMeterRatio;
    currentDepth = Math.max(0, Math.min(maxDepth, currentDepth)); // Ensure depth is within bounds

     // --- Gas Simulation Logic (Exponential Loading/Unloading based on Pressure) ---
    const pressureFactor = (currentDepth / 10) + 1; // Simple pressure model (1 atm per 10m + 1 atm at surface)
    const equilibriumGasLevel = Math.min(pressureFactor * (maxGasAtMaxDepth / ((maxDepth/10)+1)), maxGasAtMaxDepth); // Target level based on current pressure

    if (currentDepth > 1) { // At depth or descending: load gas towards equilibrium
         const loadingSpeed = gasLoadingRate * pressureFactor * (equilibriumGasLevel - dissolvedGasLevel) / maxGasAtMaxDepth;
         dissolvedGasLevel += loadingSpeed * deltaTime * 100; // Scale speed
         dissolvedGasLevel = Math.min(dissolvedGasLevel, maxGasAtMaxDepth); // Don't exceed max possible
    } else { // Near surface or ascending: unload gas
        // Unloading rate depends on current supersaturation and ascent rate
        const superSaturation = dissolvedGasLevel - equilibriumGasLevel;
        if (superSaturation > 0) {
             // Faster ascent hinders unloading, slower ascent helps
             const effectiveUnloadingRate = gasUnloadingRate * (1 - Math.min(1, verticalRate / 15) * ascentAffectsUnloadingFactor);
             const unloadingSpeed = effectiveUnloadingRate * (superSaturation / maxGasAtMaxDepth);
             dissolvedGasLevel -= unloadingSpeed * deltaTime * 100; // Scale speed
             dissolvedGasLevel = Math.max(0, dissolvedGasLevel); // Don't go below 0
        } else {
             // If undersaturated, slowly go towards equilibrium (0 at surface)
             const slowUnloadingSpeed = gasUnloadingRate * (0 - dissolvedGasLevel) / maxGasAtMaxDepth * 0.1; // Very slow unloading
             dissolvedGasLevel += slowUnloadingSpeed * deltaTime * 100;
             dissolvedGasLevel = Math.max(0, dissolvedGasLevel);
        }
    }

    // --- Bubble and Danger Logic ---
    const superSaturation = dissolvedGasLevel - equilibriumGasLevel; // How much gas is 'extra' vs current pressure
    bubbleArea.style.opacity = 0; // Hide bubbles by default

     // Clear old bubbles if not enough are needed
     if (superSaturation < bubbleThreshold - (verticalRate * 1) || verticalRate <= 0.1) {
         bubbleArea.innerHTML = ''; // Clear bubbles when below threshold or descending/stopped
     }

    water.classList.remove('danger'); // Remove danger class from water

    if (verticalRate > 0.1 && currentDepth > 1) { // Only on ascent and not right at surface
        if (superSaturation > bubbleThreshold - (verticalRate * 1)) { // Faster ascent lowers effective bubble threshold
             const bubbleIntensity = Math.min(1, (superSaturation - (bubbleThreshold - (verticalRate * 1))) / (dangerThreshold - bubbleThreshold));
             bubbleArea.style.opacity = bubbleIntensity * 1.5; // More supersaturation = more visible bubbles

             // Generate bubbles proportional to intensity
             const targetBubbles = Math.floor(bubbleIntensity * 30); // Up to 30 bubbles
             // Add new bubbles if needed, but don't remove existing ones within a frame for smoothness
             const currentBubbles = bubbleArea.children.length;
             for(let i = currentBubbles; i < targetBubbles; i++) {
                 const bubble = document.createElement('div');
                 bubble.classList.add('bubble');
                 // Random start position within the area, slightly below center
                 bubble.style.left = `${20 + Math.random() * 60}px`;
                 bubble.style.bottom = `${Math.random() * 20}px`; // Start low
                 // Random animation delay and duration for variety
                 bubble.style.animationDelay = `${Math.random() * 0.8}s`;
                 bubble.style.animationDuration = `${1.5 + Math.random() * 1.5}s`;
                 bubbleArea.appendChild(bubble);
             }

             gasStatusDisplay.textContent = 'בועות מתחילות! האטו!';
             gasStatusDisplay.style.color = 'orange';

             if (superSaturation > dangerThreshold - (verticalRate * 1.5)) { // Higher threshold for danger
                 dangerIndicator.style.display = 'block';
                 water.classList.add('danger'); // Flash water background
                 gasStatusDisplay.textContent = 'סכנת דקומפרסיה מיידית! עצור עלייה!';
                 gasStatusDisplay.style.color = 'red';
             } else {
                 dangerIndicator.style.display = 'none';
             }
        } else {
            dangerIndicator.style.display = 'none';
            gasStatusDisplay.textContent = 'פינוי גז תקין';
            gasStatusDisplay.style.color = 'green';
        }
    } else if (currentDepth > 1) { // At depth or descending
         dangerIndicator.style.display = 'none';
         gasStatusDisplay.textContent = 'טוען חנקן...';
         gasStatusDisplay.style.color = 'inherit';
         bubbleArea.innerHTML = ''; // No ascent bubbles while deep
         breathingBubblesArea.style.opacity = 1; // Show breathing bubbles at depth
         if(breathingBubblesArea.children.length === 0) {
             // Add some breathing bubbles if not already present
             for(let i=0; i<5; i++) {
                 const b = document.createElement('div');
                 b.classList.add('breathing-bubble');
                 b.style.animationDelay = `${i * 0.5}s`;
                 breathingBubblesArea.appendChild(b);
             }
         }
    } else { // At surface (depth <= 1)
         dangerIndicator.style.display = 'none';
         bubbleArea.innerHTML = ''; // Clear ascent bubbles
         breathingBubblesArea.innerHTML = ''; // Clear breathing bubbles
         breathingBubblesArea.style.opacity = 0;

         if (dissolvedGasLevel < bubbleThreshold/2) { // Consider safe if gas level is low on reaching surface
             gasStatusDisplay.textContent = 'סיום צלילה בטוחה';
             gasStatusDisplay.style.color = 'green';
             safeMessage.style.display = 'block';
             unsafeMessage.style.display = 'none';
         } else { // Gas level still high on reaching surface rapidly
             gasStatusDisplay.textContent = 'סיום צלילה מסוכנת!';
             gasStatusDisplay.style.color = 'red';
             unsafeMessage.style.display = 'block';
             safeMessage.style.display = 'none';
         }
         dissolvedGasLevel = 0; // Reset at surface
         stopSimulation(); // Automatically stop at surface
         startDiveButton.disabled = false;
         startDiveButton.textContent = 'התחילו צלילה (ל-30מ')';
    }


    // Update displays
    depthDisplay.textContent = currentDepth.toFixed(1);
    ascentRateDisplay.textContent = verticalRate.toFixed(1);
    gasLevelDisplay.textContent = Math.round(dissolvedGasLevel);


    animationFrameId = requestAnimationFrame(gameLoop);
}

function startDiveSequence() {
    if (isDiving) return;
    isDiving = true;
    dissolvedGasLevel = 0; // Start fresh
    currentDepth = 0; // Start at the surface
    currentBottomPx = surfaceBottomPx;
    diver.style.bottom = `${currentBottomPx}px`;
    verticalRate = -10; // Start descending at 10 m/min
    speedSlider.value = -10 / 1.5; // Match slider visual (max 15 m/min)
    speedSlider.disabled = true; // Disable slider during automatic descent

    safeMessage.style.display = 'none';
    unsafeMessage.style.display = 'none';
    dangerIndicator.style.display = 'none';
    bubbleArea.style.opacity = 0;
    breathingBubblesArea.innerHTML = ''; // Clear bubbles
    breathingBubblesArea.style.opacity = 0;

    gasStatusDisplay.textContent = 'מתחיל ירידה...';
    gasStatusDisplay.style.color = 'inherit';
    gasLevelDisplay.textContent = '0';
    startDiveButton.disabled = true;
    startDiveButton.textContent = 'בצלילה...';
    water.classList.remove('danger'); // Ensure no danger flash initially


    lastUpdateTime = performance.now(); // Reset time

    // Descent loop
    const descentInterval = setInterval(() => {
         updateSimulation(performance.now()); // Run simulation steps

         if (currentDepth >= maxDepth - 0.5) { // Reached bottom
             clearInterval(descentInterval);
             verticalRate = 0; // Stop descent
             currentDepth = maxDepth; // Ensure exact depth
             currentBottomPx = seabedBottomPx; // Ensure exact position
             diver.style.bottom = `${currentBottomPx}px`;
             depthDisplay.textContent = currentDepth.toFixed(1);
             ascentRateDisplay.textContent = verticalRate.toFixed(1);
             startDepthHold(); // Proceed to hold at depth
         }
    }, 50); // Update frequently during descent


}

function startDepthHold() {
     gasStatusDisplay.textContent = 'הגעה לעומק 30 מ\'. טוען חנקן...';
     gasStatusDisplay.style.color = 'inherit';
     breathingBubblesArea.style.opacity = 1; // Start breathing bubbles

     timeAtDepthSimulated = 0;
     const maxHoldTime = 15; // Hold for 15 seconds at bottom

     const holdInterval = setInterval(() => {
         timeAtDepthSimulated += 1;
         // Simulate gas loading during hold (using the same logic as updateSimulation but stepped)
         const pressureFactor = (currentDepth / 10) + 1;
         const equilibriumGasLevel = Math.min(pressureFactor * (maxGasAtMaxDepth / ((maxDepth/10)+1)), maxGasAtMaxDepth);
         const loadingSpeed = gasLoadingRate * pressureFactor * (equilibriumGasLevel - dissolvedGasLevel) / maxGasAtMaxDepth;
         dissolvedGasLevel += loadingSpeed * 1 * 100; // Simulate 1 second pass
         dissolvedGasLevel = Math.min(dissolvedGasLevel, maxGasAtMaxDepth);
         gasLevelDisplay.textContent = Math.round(dissolvedGasLevel);
         gasStatusDisplay.textContent = `ממתין בעומק... (${maxHoldTime - timeAtDepthSimulated} שניות)`;

         if (timeAtDepthSimulated >= maxHoldTime) {
             clearInterval(holdInterval);
             gasStatusDisplay.textContent = 'מוכן לעלייה. שלוט בקצב.';
             gasStatusDisplay.style.color = 'green';
             speedSlider.disabled = false; // Enable slider for ascent control
             lastUpdateTime = performance.now(); // Reset time for rAF loop
             gameLoop(lastUpdateTime); // Start the main simulation loop
         }
     }, 1000); // Update state every second
}


function gameLoop(currentTime) {
     updateSimulation(currentTime);
     if (isDiving) {
         animationFrameId = requestAnimationFrame(gameLoop);
     }
}


function stopSimulation() {
    isDiving = false;
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
    }
     // Ensure any intervals are cleared (though we primarily use rAF now)
     // Any specific descent/hold intervals would need to be handled here if still active
    speedSlider.disabled = true; // Disable slider when not diving
     verticalRate = 0; // Stop movement
     ascentRateDisplay.textContent = verticalRate.toFixed(1);
}

// Event Listeners
startDiveButton.addEventListener('click', startDiveSequence);

speedSlider.addEventListener('input', (event) => {
    // Slider value goes from -15 to 15
    verticalRate = parseFloat(event.target.value); // Map slider value directly to vertical rate m/min
});

toggleExplanationButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מדעי' : 'הצג הסבר מדעי';
});

// Initial state setup on page load
function initializeSimulation() {
    stopSimulation(); // Ensure stopped
    currentDepth = 0;
    currentBottomPx = surfaceBottomPx;
    diver.style.bottom = `${currentBottomPx}px`;
    depthDisplay.textContent = currentDepth.toFixed(1);
    ascentRateDisplay.textContent = 0.0.toFixed(1);
    gasLevelDisplay.textContent = 0;
    gasStatusDisplay.textContent = 'מוכן';
    speedSlider.value = 0;
    speedSlider.disabled = true; // Slider is disabled until dive starts and hold finishes
    safeMessage.style.display = 'none';
    unsafeMessage.style.display = 'none';
    dangerIndicator.style.display = 'none';
    bubbleArea.innerHTML = '';
    breathingBubblesArea.innerHTML = '';
     water.classList.remove('danger');
}

initializeSimulation();

</script>