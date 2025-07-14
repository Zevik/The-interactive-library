---
title: "מנופים בפעולה: משחק של כוח, מרחק ואיזון"
english_slug: lever-simulation
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה
  - מכניקה
  - מנוף
  - הדמיה
  - אינטראקטיבי
  - מומנט
---
# מנופים בפעולה: משחק של כוח, מרחק ואיזון

האם אי פעם תהיתם איך כלי פשוט יכול להעניק לנו כוחות-על? ממספריים שגוזרים נייר ועד מוט פלדה שמזיז סלעים - כולם מבוססים על אותו עקרון קסום: המנוף. בואו נצלול יחד להדמיה סופר אינטראקטיבית כדי לגלות איך הכוח והמרחק משתלבים ליצירת איזון... או דווקא כדי להפר אותו! שחקו עם המערכת וראו בעצמכם איך זה עובד.

<div class="lever-simulator-container">
    <div class="ground-line"></div>
    <div class="fulcrum-base"></div> <!-- Fulcrum Base positioned relative to container -->
    <div class="lever-bar">
        <div class="load-item item" id="loadItem">
            <div class="item-label weight-label">מטען: 10</div>
            <div class="item-icon weight-icon"></div>
        </div>
        <div class="force-item item" id="forceItem">
            <div class="item-label force-label">כוח: 5</div>
            <div class="item-icon force-icon"></div>
        </div>
         <!-- Optional: Add markers on the bar -->
        <div class="marker marker-0">0%</div>
        <div class="marker marker-25">25%</div>
        <div class="marker marker-50">50%</div>
        <div class="marker marker-75">75%</div>
        <div class="marker marker-100">100%</div>
    </div>


    <div class="controls">
        <h3>שחקו עם המנוף:</h3>
        <div class="control-group">
            <label for="fulcrumPos">מיקום נקודת משען:</label>
            <input type="range" id="fulcrumPos" min="0" max="100" value="50">
            <span class="control-value" id="fulcrumValue">50%</span>
        </div>
        <div class="control-group">
            <label for="loadPos">מיקום מטען:</label>
            <input type="range" id="loadPos" min="0" max="100" value="25">
            <span class="control-value" id="loadPosValue">25%</span>
        </div>
         <div class="control-group">
            <label for="loadWeight">משקל מטען:</label>
            <input type="number" id="loadWeight" min="1" value="10" step="1">
        </div>
        <div class="control-group">
            <label for="forcePos">מיקום כוח:</label>
            <input type="range" id="forcePos" min="0" max="100" value="75">
            <span class="control-value" id="forcePosValue">75%</span>
        </div>
        <div class="control-group">
             <label for="forceStrength">עוצמת כוח:</label>
            <input type="number" id="forceStrength" min="1" value="5" step="1">
        </div>
        <div class="balance-status"></div>
    </div>
</div>

<button id="toggleExplanation">הסבר קצר על מנופים</button>

<div class="explanation">
    <h3>מהו מנוף ואיך הוא עובד?</h3>
    <p>מנוף הוא פלא הנדסי פשוט: בסך הכל מוט קשיח (הנקרא גם "זרוע המנוף") ונקודת תמיכה קבועה שסביבה הוא יכול להסתובב, הנקראת **ציר** או **נקודת משען**. אנחנו מפעילים **כוח** בקצה אחד של המנוף כדי להזיז **מטען** או להתגבר על התנגדות בקצה אחר (או בנקודה אחרת על המוט).</p>

    <h3>סוד המומנטים</h3>
    <p>הקסם של המנוף טמון ב**מומנט**. מומנט הוא האפקט הסיבובי של כוח סביב ציר, ומחשבים אותו כ**כוח כפול מרחק הכוח מהציר**. המנוף יהיה ב**שיווי משקל** בדיוק כשהמומנט שמפעיל המטען שווה למומנט שמפעיל הכוח שאתם מפעילים, אבל בכיוונים מנוגדים.</p>
    <p>במילים אחרות, כשיש איזון, תמיד מתקיים:</p>
    <p><strong>עוצמת הכוח × מרחק הכוח מציר הסיבוב = עוצמת המטען × מרחק המטען מציר הסיבוב</strong></p>
    <p>זה העיקרון שמאפשר לנו להרים דברים כבדים עם פחות מאמץ – פשוט ממקמים את המטען קרוב יותר לציר המשען מאיתנו!</p>

    <h3>מנופים מסוגים שונים</h3>
    <p>אמנם ההדמיה הזו מתמקדת לרוב במה שנקרא "**מנוף סוג 1**" (כשהציר נמצא בין המטען לכוח, כמו בנדנדה או מספריים), חשוב לדעת שיש עוד שני סוגים:</p>
    <ul>
        <li>**מנוף סוג 2:** המטען נמצא בין הציר לכוח (כמו במריצה). מנוף כזה תמיד נותן יתרון בכוח.</li>
        <li>**מנוף סוג 3:** הכוח מופעל בין הציר למטען (כמו בפינצטה או מלקחיים). סוג זה מאפשר תנועה מהירה או רחבה יותר של המטען, על חשבון הכוח.</li>
    </ul>

    <p>ההדמיה מאפשרת לכם לשחק עם כל הפרמטרים - מיקום הציר, מיקום ומשקל המטען, ומיקום ועוצמת הכוח - ולראות באופן מיידי איך כל שינוי משפיע על האיזון של המנוף. נסו למצוא קומבינציות שונות שיוצרות איזון!</p>
</div>

<style>
/* הוספת פונטים מודרניים ושיפור כללי */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

body {
    font-family: 'Heebo', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #eef2f7; /* Soft background */
    padding: 20px;
    direction: rtl; /* Hebrew default */
}

h1, h3 {
    color: #2c3e50; /* Dark blue-gray */
    text-align: center;
    margin-bottom: 20px;
}

h1 {
    font-size: 2em;
}

/* Container enhancements */
.lever-simulator-container {
    position: relative;
    width: 95%;
    max-width: 800px; /* Increased max width */
    height: 500px; /* Increased height */
    margin: 40px auto;
    border-radius: 12px; /* Softer corners */
    background: linear-gradient(to bottom, #ffffff 0%, #f0f4f8 100%); /* Subtle gradient */
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    padding-bottom: 30px; /* More space at bottom */
    box-shadow: 0 8px 20px rgba(0,0,0,0.15); /* Stronger, softer shadow */
    border: 1px solid #dcdcdc; /* Subtle border */
    transition: box-shadow 0.3s ease-in-out;
}

.lever-simulator-container:hover {
     box-shadow: 0 12px 25px rgba(0,0,0,0.2);
}


.ground-line {
    position: absolute;
    bottom: 30px; /* Match padding bottom */
    left: 0;
    width: 100%;
    height: 4px; /* Thicker line */
    background-color: #95a5a6; /* Concrete gray */
    z-index: 0;
}

.fulcrum-base {
    position: absolute;
    bottom: 0; /* Sits on the ground */
    width: 60px; /* Wider base */
    height: 60px; /* Taller base */
     background: repeating-linear-gradient(
        45deg,
        #bdc3c7, /* Silver */
        #bdc3c7 8px,
        #ecf0f1 8px, /* Clouds */
        #ecf0f1 16px
    );
    clip-path: polygon(0% 100%, 50% 0%, 100% 100%);
    left: 50%; /* Initial position */
    transform: translateX(-50%); /* Center the base at the 'left' percentage */
    z-index: 1;
    transition: left 0.5s ease-in-out; /* Animate fulcrum movement */
}

.lever-bar {
    position: absolute;
    bottom: 60px; /* Place above fulcrum base */
    left: 0; /* Bar spans full width conceptually */
    width: 100%;
    height: 25px; /* Thicker bar */
    background: linear-gradient(to right, #8b4513, #a0522d, #8b4513); /* Wooden gradient */
    border-radius: 8px; /* Softer corners */
    transform-origin: 50% 100%; /* Pivot at the bottom center initially */
    transition: transform 0.6s cubic-bezier(0.68, -0.55, 0.27, 1.55); /* More dynamic rotation animation */
    z-index: 2;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3); /* Stronger bar shadow */
    border: 1px solid rgba(0,0,0,0.1);
}

/* Visual markers on the bar */
.lever-bar .marker {
    position: absolute;
    bottom: -25px; /* Position below the bar */
    width: 1px;
    height: 15px;
    background-color: rgba(0,0,0,0.3);
    z-index: 3;
    font-size: 0.7em;
    color: #555;
    transform: translateX(-50%); /* Center the marker line */
    pointer-events: none; /* Don't interfere with clicks */
}

.lever-bar .marker span {
    position: absolute;
    top: 18px;
    left: 50%;
    transform: translateX(-50%);
}

.lever-bar .marker-0 { left: 0%; }
.lever-bar .marker-25 { left: 25%; }
.lever-bar .marker-50 { left: 50%; }
.lever-bar .marker-75 { left: 75%; }
.lever-bar .marker-100 { left: 100%; }


.item {
    position: absolute;
    bottom: 20px; /* Position relative to the bar's bottom, adjusted for bar thickness */
    transform: translate(-50%, -50%) translateY(0); /* Center item and place it above the bar */
    width: 60px; /* Larger items */
    height: 60px;
    border-radius: 10px; /* Softer squares */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 0.9em; /* Larger text */
    font-weight: bold;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    cursor: grab; /* Indicate draggable potential (even if not implemented) */
    transition: left 0.5s ease-in-out, background-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease; /* Animate movement and appearance */
    z-index: 4;
}

.item:active {
    cursor: grabbing;
}

.load-item {
    background: linear-gradient(to bottom right, #e74c3c, #c0392b); /* Alizarin gradient */
    left: 25%; /* Initial position */
}

.force-item {
    background: linear-gradient(to bottom left, #3498db, #2980b9); /* Peter River gradient */
     left: 75%; /* Initial position */
}

.item-label {
    font-size: 0.8em; /* Slightly larger label */
    margin-bottom: 5px;
}

.item-icon {
    width: 25px; /* Larger icons */
    height: 25px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.3)); /* Add shadow to icons */
}

.weight-icon {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M12 2c-3.31 0-6 2.69-6 6v4c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2v-4c0-3.31-2.69-6-6-6zm0 2c2.21 0 4 1.79 4 4v4H8V8c0-2.21 1.79-4 4-4zm-2 13h4v2h-4zM4 17h16v2H4z"/></svg>');
}

.force-icon {
    /* Simple force icon (arrow pointing down with a hand) */
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M18 9V2h-2v7h-2V2H12v7H10V2H8v7H6V2H4v7c0 1.1.9 2 2 2h3.8L8 16h2l1.3-3h2.4l1.3 3h2l-1.8-5H18zm-4 7l1.3 3h2.4l1.3-3h-5zM6 18h12v2H6z"/></svg>');
}


.controls {
    width: 95%;
    max-width: 700px; /* Wider controls area */
    margin-top: 30px; /* More space */
    padding: 20px; /* More padding */
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    direction: rtl;
    text-align: right;
    border: 1px solid #eee;
}

.controls h3 {
    margin-top: 0;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 20px;
}

.control-group {
    display: flex;
    align-items: center;
    margin-bottom: 18px; /* More space between groups */
    flex-wrap: wrap;
}

.control-group label {
    flex: 0 0 140px; /* Wider labels */
    margin-left: 15px; /* More space */
    color: #555;
    font-weight: 700; /* Bolder */
    font-size: 0.95em;
}

.control-group input[type="range"] {
    flex-grow: 1;
    margin: 0 15px; /* More space */
    -webkit-appearance: none;
    appearance: none;
    height: 10px; /* Thicker slider */
    background: #dce4ec; /* Lighter background */
    border-radius: 5px;
    outline: none;
    opacity: 0.9;
    transition: opacity .2s, box-shadow 0.2s ease;
}

.control-group input[type="range"]:hover {
    opacity: 1;
    box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
}

.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 24px; /* Larger thumb */
    height: 24px;
    background: #3498db;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    transition: background-color 0.3s ease, transform 0.1s ease;
}
.control-group input[type="range"]::-webkit-slider-thumb:active {
    transform: scale(1.1);
    background-color: #2980b9;
}


.control-group input[type="range"]::-moz-range-thumb {
    width: 24px;
    height: 24px;
    background: #3498db;
    cursor: pointer;
    border-radius: 50%;
     box-shadow: 0 2px 5px rgba(0,0,0,0.3);
     transition: background-color 0.3s ease, transform 0.1s ease;
}
.control-group input[type="range"]::-moz-range-thumb:active {
     transform: scale(1.1);
     background-color: #2980b9;
}


.control-group input[type="number"] {
    width: 70px; /* Wider number input */
    padding: 8px; /* More padding */
    border: 1px solid #ccc;
    border-radius: 6px; /* Softer corners */
    text-align: center;
    font-size: 1em;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.control-group input[type="number"]:focus {
    border-color: #3498db;
    box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
    outline: none;
}

.control-value {
    flex-shrink: 0;
    min-width: 50px; /* Wider value display */
    text-align: left;
    font-weight: 700;
    color: #2c3e50;
    font-size: 0.95em;
}

.balance-status {
    margin-top: 20px; /* More space */
    padding: 10px;
    border-radius: 6px;
    font-size: 1.2em; /* Larger text */
    font-weight: 700;
    text-align: center;
    min-height: 1.5em; /* Reserve more space */
    transition: color 0.5s ease, background-color 0.5s ease;
}

.balance-status.balanced {
    color: #27ae60; /* Emerald green */
    background-color: #e8f8f5; /* Light green background */
}

.balance-status.tilted-force {
    color: #3498db; /* Peter River blue */
    background-color: #ebf5fb; /* Light blue background */
}

.balance-status.tilted-load {
    color: #e74c3c; /* Alizarin red */
    background-color: #fdedec; /* Light red background */
}


#toggleExplanation {
    display: block;
    margin: 30px auto; /* More space around button */
    padding: 12px 25px; /* More padding */
    font-size: 1.1em; /* Larger text */
    cursor: pointer;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, box-shadow 0.3s ease, transform 0.1s ease;
    font-family: 'Heebo', sans-serif;
}

#toggleExplanation:hover {
    background-color: #2980b9;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
#toggleExplanation:active {
    transform: scale(0.98);
}


.explanation {
    margin-top: 30px;
    padding: 20px;
    border: 1px solid #dcdcdc;
    border-radius: 12px;
    background-color: #fff;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    direction: rtl;
    text-align: right;
    display: none; /* Hidden by default */
}

.explanation h3 {
    margin-top: 0;
    color: #2c3e50;
    text-align: right;
    border-bottom: 2px solid #3498db; /* Underline title */
    padding-bottom: 10px;
    margin-bottom: 15px;
}

.explanation p {
    line-height: 1.7; /* More space between lines */
    color: #555;
    margin-bottom: 15px;
}

.explanation ul {
     line-height: 1.7;
     color: #555;
     margin-bottom: 15px;
     padding-right: 20px; /* Indent list */
}

.explanation li {
    margin-bottom: 8px;
}

.explanation strong {
    color: #2c3e50;
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const leverBar = document.querySelector('.lever-bar');
    const fulcrumBase = document.querySelector('.fulcrum-base');
    const loadItem = document.getElementById('loadItem'); // Use IDs for clarity
    const forceItem = document.getElementById('forceItem');

    const fulcrumPosSlider = document.getElementById('fulcrumPos');
    const loadPosSlider = document.getElementById('loadPos');
    const loadWeightInput = document.getElementById('loadWeight');
    const forcePosSlider = document.getElementById('forcePos');
    const forceStrengthInput = document.getElementById('forceStrength');

    const fulcrumValueSpan = document.getElementById('fulcrumValue');
    const loadPosValueSpan = document.getElementById('loadPosValue');
    const forcePosValueSpan = document.getElementById('forcePosValue');

    const loadWeightLabel = loadItem.querySelector('.weight-label');
    const forceStrengthLabel = forceItem.querySelector('.force-label');

    const balanceStatusDiv = document.querySelector('.balance-status');

    const explanationDiv = document.querySelector('.explanation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');

    function updateLever() {
        const fulcrumPercent = parseFloat(fulcrumPosSlider.value);
        const loadPercent = parseFloat(loadPosSlider.value);
        const forcePercent = parseFloat(forcePosSlider.value);
        const loadWeight = parseFloat(loadWeightInput.value);
        const forceStrength = parseFloat(forceStrengthInput.value);

        // Ensure weights/forces are positive
        const currentLoadWeight = Math.max(1, loadWeight);
        const currentForceStrength = Math.max(1, forceStrength);
        loadWeightInput.value = currentLoadWeight; // Correct input if needed
        forceStrengthInput.value = currentForceStrength; // Correct input if needed


        // Update visual positions with transitions
        fulcrumBase.style.left = `${fulcrumPercent}%`;
        leverBar.style.transformOrigin = `${fulcrumPercent}% 100%`; // Pivot above fulcrum base
        loadItem.style.left = `${loadPercent}%`;
        forceItem.style.left = `${forcePercent}%`;

        // Update value displays
        fulcrumValueSpan.textContent = `${fulcrumPercent}%`;
        loadPosValueSpan.textContent = `${loadPercent}%`;
        forcePosValueSpan.textContent = `${forcePercent}%`;
        loadWeightLabel.textContent = `מטען: ${currentLoadWeight}`;
        forceStrengthLabel.textContent = `כוח: ${currentForceStrength}`;

        // Animate item size briefly when weight/force changes
        loadItem.style.transform = `translate(-50%, -50%) translateY(0) scale(1.05)`;
        forceItem.style.transform = `translate(-50%, -50%) translateY(0) scale(1.05)`;
        requestAnimationFrame(() => { // Use rAF for next frame
             loadItem.style.transform = `translate(-50%, -50%) translateY(0) scale(1)`;
             forceItem.style.transform = `translate(-50%, -50%) translateY(0) scale(1)`;
        });


        // Calculate moments
        // Convert percentages (0-100) to normalized positions (0-1) relative to bar width
        const p_f = fulcrumPercent / 100; // Fulcrum position normalized (0-1)
        const p_l = loadPercent / 100; // Load position normalized (0-1)
        const p_a = forcePercent / 100; // Force position normalized (0-1)

        // Distances from fulcrum (signed)
        const d_l = p_l - p_f; // Load distance from fulcrum
        const d_a = p_a - p_f; // Force distance from fulcrum

        // Calculate signed moments. Assuming positive moment is anti-clockwise.
        // A force/load at position p causes a moment around fulcrum p_f.
        // If position p is > p_f (right of fulcrum), and force is down, it causes a positive (anti-clockwise) moment.
        // If position p is < p_f (left of fulcrum), and force is down, it causes a negative (clockwise) moment.
        // So, moment = force * distance_from_fulcrum (where distance is signed p - p_f)
        const momentLoad = -currentLoadWeight * d_l; // Load pulling down, causes CW moment if d_l > 0, CCW if d_l < 0. Needs negation if positive distance gives CCW. Let's align: positive moment = CCW. If load is right (d_l > 0), it causes CW (negative) moment. If load is left (d_l < 0), it causes CCW (positive) moment. So momentLoad = -weight * d_l.
        const momentForce = -currentForceStrength * d_a; // Force pushing down, causes CW moment if d_a > 0, CCW if d_a < 0. Needs negation if positive distance gives CCW. So momentForce = -strength * d_a.

        // Net moment is the sum of individual signed moments
        const netMoment = momentLoad + momentForce; // Summing signed moments


        // Scale net moment to rotation angle, limit angle
        const angleSensitivity = 50; // Increased sensitivity for more dramatic tilt
        let angle = netMoment * angleSensitivity;

        // Limit the rotation angle for visual stability and realism
        const maxAngle = 25; // Increased max angle
        angle = Math.max(-maxAngle, Math.min(maxAngle, angle));

        // Apply rotation to the lever bar
        leverBar.style.transform = `rotate(${angle}deg)`;

        // Update balance status text and color with classes
        const tolerance = 0.5; // Moment tolerance for "balanced" (adjusted for sensitivity/values)
        balanceStatusDiv.classList.remove('balanced', 'tilted-force', 'tilted-load'); // Remove previous classes

        if (Math.abs(netMoment) < tolerance) {
             balanceStatusDiv.textContent = '✅ מאוזן!';
             balanceStatusDiv.classList.add('balanced');
        } else if (netMoment > 0) { // Positive net moment means CCW rotation (usually Force side goes down, Load side goes up for Class 1)
            // Based on typical Class 1 setup (Load left, Force right):
            // If Force is right (d_a > 0) and causes CCW moment (-strength * d_a < 0), this logic might be reversed.
            // Let's check the visual: positive angle tilts the right side DOWN.
            // If right side is Force (d_a > 0), positive angle is towards Force side going down.
            balanceStatusDiv.textContent = '➡️ נוטה לכוח!'; // Arrow towards Force side
            balanceStatusDiv.classList.add('tilted-force');
        } else { // netMoment < 0 (CW rotation, usually Load side goes down, Force side goes up for Class 1)
            balanceStatusDiv.textContent = '⬅️ נוטה למטען!'; // Arrow towards Load side
            balanceStatusDiv.classList.add('tilted-load');
        }
    }

    // Add event listeners to all controls
    fulcrumPosSlider.addEventListener('input', updateLever);
    loadPosSlider.addEventListener('input', updateLever);
    loadWeightInput.addEventListener('input', updateLever);
    forcePosSlider.addEventListener('input', updateLever);
    forceStrengthInput.addEventListener('input', updateLever);

    // Initial update
    updateLever();

     // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר קצר על מנופים';
    });

    // Prevent negative values in number inputs
    loadWeightInput.addEventListener('change', () => {
         if (parseFloat(loadWeightInput.value) < 1) loadWeightInput.value = 1;
         updateLever();
    });
     forceStrengthInput.addEventListener('change', () => {
         if (parseFloat(forceStrengthInput.value) < 1) forceStrengthInput.value = 1;
         updateLever();
    });
});
</script>
---