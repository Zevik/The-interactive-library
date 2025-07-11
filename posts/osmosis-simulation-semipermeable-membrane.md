---
title: "הדמיית אוסמוזה: מסע המים בממברנה"
english_slug: osmosis-simulation-semipermeable-membrane
category: "ביולוגיה"
tags: [ביוכימיה, תאים, מדע, הדמיה, אינטראקטיבי]
---
# אוסמוזה: מסע המים הבלתי נראה

צללו לתוך עולם האוסמוזה! חקרו כיצד מים "מחפשים" שיווי משקל כשהם חוצים ממברנה חדירה למחצה, בהשפעת ריכוזי מלח שונים. שחקו עם הריכוזים ההתחלתיים וגלו את כוחה של האוסמוזה בתאים חיים ובמערכות רבות אחרות.

<div id="osmosis-app">
    <div class="app-title">
        <h2>סימולטור אוסמוזה אינטראקטיבי</h2>
    </div>
    <div class="container-setup">
        <div class="compartments-visual">
            <div class="chamber" id="chamber-left">
                 <div class="solute-label" id="solute-left-label">מלח: 0%</div>
                 <div class="water-level" id="water-left"></div>
            </div>
            <div class="membrane-container">
                 <div class="membrane"></div>
                 <div class="flow-indicator" id="flow-indicator"></div>
            </div>
            <div class="chamber" id="chamber-right">
                 <div class="solute-label" id="solute-right-label">מלח: 0%</div>
                 <div class="water-level" id="water-right"></div>
            </div>
        </div>
        <div class="controls">
            <h3>הגדרות התחלתיות</h3>
            <div class="control-group">
                <label for="salt-left">ריכוז מומס (שמאל, %):</label>
                <input type="range" id="salt-left" min="0" max="20" value="1" step="0.1">
                <span id="salt-left-value">1.0%</span>
            </div>
            <div class="control-group">
                <label for="salt-right">ריכוז מומס (ימין, %):</label>
                <input type="range" id="salt-right" min="0" max="20" value="5" step="0.1">
                <span id="salt-right-value">5.0%</span>
            </div>
             <div class="button-group">
                <button id="start-sim">הפעל הדמיה</button>
                <button id="reset-sim" disabled>איפוס</button>
             </div>
        </div>
    </div>
    <div class="status">
        <h3>סטטוס</h3>
        <p id="sim-status">הגדירו ריכוזים והפעילו!</p>
    </div>
</div>

<style>
/* הסטייל כאן עבר שדרוג ויזואלי משמעותי */

#osmosis-app {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    direction: rtl;
    text-align: right;
    padding: 25px;
    border: 1px solid #dcdcdc;
    border-radius: 12px;
    background: linear-gradient(to bottom right, #eef2f7, #d8e2ed); /* Soft gradient background */
    margin-bottom: 30px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    color: #333;
    overflow: hidden; /* Ensure nothing spills out rounded corners */
}

#osmosis-app h1, #osmosis-app h2, #osmosis-app h3 {
    text-align: center;
    color: #004080; /* Deep blue */
    margin-bottom: 15px;
    font-weight: 600;
}
#osmosis-app h2 { font-size: 1.8em; margin-bottom: 5px;}
#osmosis-app h3 { font-size: 1.3em; margin-bottom: 10px;}

.app-title {
    border-bottom: 2px solid #b0c4de; /* Light blue separator */
    padding-bottom: 10px;
    margin-bottom: 20px;
}


.container-setup {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
    margin-bottom: 20px;
}

.compartments-visual {
    display: flex;
    justify-content: center;
    align-items: flex-end; /* Align chambers at the bottom */
    gap: 0px; /* No gap between visual elements */
    margin-bottom: 20px;
}

.chamber {
    position: relative;
    width: 100px; /* Slightly narrower */
    height: 280px; /* Slightly taller */
    border: 2px solid #007bff; /* Primary blue */
    border-top: none;
    background: linear-gradient(to top, #e0f7fa 0%, #80deea 100%); /* Water gradient from light to dark */
    overflow: hidden;
    display: flex;
    flex-direction: column-reverse; /* Water fills from bottom */
    transition: border-color 0.3s ease; /* Smooth transition for border */
}

#chamber-left {
    border-right: none;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
}

#chamber-right {
     border-left: none;
     border-top-right-radius: 10px;
     border-bottom-right-radius: 10px;
}

.membrane-container {
    position: relative;
    width: 40px; /* Space for membrane and flow indicator */
    height: 280px; /* Same height as chambers */
    display: flex;
    justify-content: center;
    align-items: center;
}

.membrane {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 4px; /* Wider membrane */
    background-color: #ff6347; /* Vibrant tomato red */
    box-shadow: 0 0 8px rgba(255, 99, 71, 0.5); /* Subtle glow */
    z-index: 1;
    border-radius: 2px;
}

.flow-indicator {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 2;
    pointer-events: none; /* Allow clicks/interactions to pass through */
    overflow: hidden;
}

.flow-indicator::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 0; /* Managed by JS */
    height: 100%;
    background: rgba(0, 123, 255, 0.4); /* Semi-transparent blue flow */
    transition: width 0.3s ease, background-color 0.3s ease;
     /* Particle animation */
    background: repeating-linear-gradient(
        90deg,
        rgba(0, 123, 255, 0.4),
        rgba(0, 123, 255, 0.4) 3px,
        transparent 3px,
        transparent 10px
    );
    background-size: 200% 100%; /* To enable movement */
     /* Animation controlled by JS via class */
}

/* Classes for flow animation */
.flow-left::before {
    animation: flowLeft 1s linear infinite;
    background-color: rgba(0, 123, 255, 0.6);
}
.flow-right::before {
    animation: flowRight 1s linear infinite;
    background-color: rgba(0, 123, 255, 0.6);
}

@keyframes flowLeft {
    0% { background-position: 100% 0; }
    100% { background-position: 0% 0; }
}

@keyframes flowRight {
    0% { background-position: 0% 0; }
    100% { background-position: 100% 0; }
}


.water-level {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 50%; /* Initial level */
    background: rgba(0, 150, 255, 0.7); /* Slightly deeper blue with transparency */
    /* Add subtle gradient to water surface */
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.2);
    transition: height 0.8s cubic-bezier(0.25, 0.1, 0.25, 1); /* Smoother ease-out */
    border-top: 3px solid rgba(0, 123, 255, 0.9); /* Sharper top line */
    box-sizing: border-box;
     /* Ripple effect placeholder - can be added with pseudo-elements or dynamic divs */
}

.solute-label {
    position: absolute;
    top: 15px; /* Slightly lower */
    left: 50%;
    transform: translateX(-50%);
    color: #333;
    font-size: 1em; /* Slightly larger */
    font-weight: bold;
    z-index: 3; /* Above water and flow */
    text-shadow: 1px 1px 3px rgba(255,255,255,0.9), -1px -1px 3px rgba(255,255,255,0.9); /* Stronger text shadow */
    white-space: nowrap; /* Prevent wrapping */
}

.controls {
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
    max-width: 350px; /* Slightly wider controls */
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
}

.control-group {
    display: flex;
    flex-direction: column; /* Stack label and input on smaller screens */
    gap: 8px;
}

.control-group label {
    flex-shrink: 0;
    width: auto; /* Auto width */
    font-weight: bold;
    color: #555;
}

.control-group input[type="range"] {
    flex-grow: 1;
    width: 100%; /* Full width */
    -webkit-appearance: none; /* Override default look */
    appearance: none;
    height: 8px;
    background: #ddd;
    outline: none;
    opacity: 0.8;
    transition: opacity 0.2s ease;
    border-radius: 4px;
}

.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #007bff; /* Primary blue thumb */
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.control-group input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}


.control-group span {
    flex-shrink: 0;
    width: auto; /* Auto width */
    text-align: right; /* Align value right */
    font-weight: bold;
    color: #007bff; /* Blue text */
}

.button-group {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-top: 10px;
}


button {
    padding: 12px 20px; /* Larger padding */
    background-color: #007bff; /* Primary blue */
    color: white;
    border: none;
    border-radius: 6px; /* More rounded */
    cursor: pointer;
    font-size: 1.1em; /* Slightly larger font */
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
}

button:hover:not(:disabled) {
    background-color: #0056b3; /* Darker blue on hover */
    transform: translateY(-1px); /* Subtle lift effect */
}

button:active:not(:disabled) {
     transform: translateY(0); /* Press effect */
     box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    box-shadow: none;
}

.status {
    text-align: center;
    min-height: 30px;
    font-size: 1.1em;
    color: #004080; /* Deep blue */
    font-weight: bold;
}

#explanation-button {
    display: block;
    width: fit-content;
    margin: 30px auto; /* More margin */
    padding: 14px 25px; /* Larger padding */
    background-color: #28a745; /* Success green */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
}

#explanation-button:hover {
    background-color: #218838; /* Darker green on hover */
    transform: translateY(-1px);
}

#explanation-button:active {
     transform: translateY(0);
     box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}


#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #b0c4de; /* Light blue border */
    border-radius: 12px;
    background-color: #e9f5ff; /* Very light blue */
    display: none; /* Hidden by default */
    text-align: right;
    direction: rtl;
    line-height: 1.7;
    color: #333;
}

#explanation h2 {
    color: #004080;
    margin-top: 0;
    margin-bottom: 15px;
    border-bottom: 2px solid #b0c4de;
    padding-bottom: 8px;
}

#explanation h3 {
    color: #0056b3; /* Medium blue */
    margin-top: 20px;
    margin-bottom: 10px;
}


#explanation p {
    margin-bottom: 1.2em;
}

#explanation ul {
    margin-bottom: 1.2em;
    padding-right: 25px; /* More padding for list */
    list-style: disc; /* Use discs */
}

#explanation li {
    margin-bottom: 0.8em; /* More space between list items */
}

/* Responsive adjustments */
@media (min-width: 768px) { /* Adjusted breakpoint */
    .container-setup {
        flex-direction: row;
        justify-content: center;
        align-items: flex-start;
        gap: 40px; /* More space between visuals and controls */
    }
    .compartments-visual {
         margin-bottom: 0;
         gap: 0px; /* Ensure chambers touch membrane visually */
    }
    .controls {
        width: 350px; /* Fixed width on wider screens */
        max-width: none;
    }
     .control-group {
         flex-direction: row; /* Label and input side-by-side */
         align-items: center;
     }
     .control-group label {
         width: 150px; /* Fixed width for labels */
     }
}

</style>

<button id="explanation-button">מהי אוסמוזה? (הסבר מפורט)</button>

<div id="explanation">
    <h2>מהי אוסמוזה?</h2>
    <p>דמיינו תא חי: הוא מוקף בקרום דק, הממברנה, שמתנהג קצת כמו מסננת סלקטיבית. הוא מאפשר למים לעבור די בקלות, אבל חוסם מולקולות גדולות יותר כמו מלח. אוסמוזה היא התנועה הטבעית, הספונטנית, של מים דרך המסננת הזו! המים נעים תמיד מהצד שבו ריכוז המים גבוה יותר (כלומר, פחות מלח מומס) לצד שבו ריכוז המים נמוך יותר (כלומר, יותר מלח מומס).</p>
    <p>זה קורה כי המים "רוצים" לדלל את הצד המרוכז יותר, לשאוף לשיוויון בריכוז המומסים בשני הצדדים. התנועה הזו יוצרת לחץ, הנקרא "לחץ אוסמוטי", שהוא הכוח המניע מאחורי האוסמוזה.</p>

    <h3>מושגי מפתח:</h3>
    <ul>
        <li>**ממברנה חדירה למחצה:** המסננת החכמה! מאפשרת מעבר מולקולות קטנות (כמו מים) וחוסמת גדולות (כמו מלח).</li>
        <li>**ריכוז מומס:** כמה "צפוף" החומר המומס (כמו מלח) בתוך המים. ריכוז מלח גבוה = פחות מים פנויים = פוטנציאל מים נמוך.</li>
        <li>**פוטנציאל מים:** מדד לאנרגיה הפוטנציאלית של המים. מים נעים תמיד מפוטנציאל מים גבוה (איפה שיש יותר "מים חופשיים", כלומר ריכוז מומסים נמוך) לפוטנציאל מים נמוך (איפה שיש פחות "מים חופשיים", כלומר ריכוז מומסים גבוה). אוסמוזה היא התנועה נטו של מים בהתאם למפל פוטנציאל המים.</li>
        <li>**לחץ אוסמוטי:** הלחץ ש"מושך" את המים לצד המרוכז יותר. ככל שההפרש בריכוזי המומסים גדול יותר, כך הלחץ האוסמוטי (וכוח המשיכה של המים) גדול יותר.</li>
    </ul>

    <h3>כיצד ההדמיה הזו עובדת?</h3>
    <p>ההדמיה שלנו מציגה שני מדורים מלאים במים, מופרדים על ידי ממברנה חדירה למחצה (הקו האדום). אתם קובעים כמה מלח (מומס) יהיה בכל מדור בהתחלה. זכרו: המלח לא יכול לעבור את הממברנה! כשתלחצו "הפעל הדמיה", תראו כיצד המים עצמם זורמים.</p>
    <p><strong>שימו לב:</strong></p>
    <ul>
        <li>בצד עם יותר מלח (ריכוז מומס גבוה = פוטנציאל מים נמוך), מים ייכנסו. מפלס המים יעלה.</li>
        <li>בצד עם פחות מלח (ריכוז מומס נמוך = פוטנציאל מים גבוה), מים ייצאו. מפלס המים ירד.</li>
    </ul>
    <p>המים ימשיכו לנוע נטו עד שההפרש בריכוזי המלח יתקזז על ידי הפרש גובה המים (לחץ הידרוסטטי), או עד שהמערכת תגיע למגבלת הגובה/נפח האפשרית בהדמיה. צפו בקווים הכחולים שחוצים את הממברנה - הם מראים לאן המים זורמים!</p>
</div>

<script>
// קוד ה-JavaScript עבר ליטוש והוספו אנימציות ויזואליות
document.addEventListener('DOMContentLoaded', () => {
    const saltLeftSlider = document.getElementById('salt-left');
    const saltRightSlider = document.getElementById('salt-right');
    const saltLeftValueSpan = document.getElementById('salt-left-value');
    const saltRightValueSpan = document.getElementById('salt-right-value');
    const startButton = document.getElementById('start-sim');
    const resetButton = document.getElementById('reset-sim');
    const waterLeftDiv = document.getElementById('water-left');
    const waterRightDiv = document.getElementById('water-right');
    const soluteLeftLabel = document.getElementById('solute-left-label');
    const soluteRightLabel = document.getElementById('solute-right-label');
    const simStatus = document.getElementById('sim-status');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('explanation');
    const flowIndicator = document.getElementById('flow-indicator'); // Element for flow visualization

    let animationFrameId = null;
    const initialWaterLevelPercent = 50;
    let waterLevelLeft = initialWaterLevelPercent; // % of max height
    let waterLevelRight = initialWaterLevelPercent; // % of max height
    const maxWaterLevelChangePercent = 40; // Max deviation from initial 50% (e.g., levels can go from 10% to 90%)

    // Constants for simulation tuning
    const simulationSpeed = 0.1; // Controls how fast levels change per step (higher is faster)
    const equilibriumThreshold = 0.05; // Stop when delta per frame is below this percentage
    const boundaryThreshold = 0.1; // Stop when water level is this close to a boundary


    // Update displayed value and label when slider moves
    const updateSaltDisplay = (slider, valueSpan, soluteLabel) => {
        const value = parseFloat(slider.value);
        valueSpan.textContent = `${value.toFixed(1)}%`;
        soluteLabel.textContent = `מלח: ${value.toFixed(1)}%`;
    };

    saltLeftSlider.addEventListener('input', () => updateSaltDisplay(saltLeftSlider, saltLeftValueSpan, soluteLeftLabel));
    saltRightSlider.addEventListener('input', () => updateSaltDisplay(saltRightSlider, saltRightValueSpan, soluteRightLabel));

    // Set initial labels
    saltLeftSlider.dispatchEvent(new Event('input'));
    saltRightSlider.dispatchEvent(new Event('input'));

    function updateWaterLevels() {
        // Apply heights directly - CSS transition handles the smooth animation
        waterLeftDiv.style.height = `${waterLevelLeft}%`;
        waterRightDiv.style.height = `${waterLevelRight}%`;
    }

    function setFlowIndicator(direction, strength = 0) {
        // direction: 'left', 'right', 'none'
        // strength: 0-1, controls visual intensity (e.g., width of indicator or speed of animation)
        flowIndicator.classList.remove('flow-left', 'flow-right');
         const flowElement = flowIndicator.querySelector('::before') || flowIndicator; // Use the element itself or pseudo if accessible
         // For pseudo-element, we rely on CSS classes triggering keyframes

        if (direction === 'left') {
            flowIndicator.classList.add('flow-left');
             // Could adjust animation speed or opacity based on strength if needed via CSS variables
             flowIndicator.style.setProperty('--flow-speed', `${1 / (0.5 + strength * 0.5)}s`); // Faster flow for higher strength
             flowIndicator.style.setProperty('--flow-opacity', `${0.4 + strength * 0.6}`); // More visible for higher strength
             flowIndicator.style.setProperty('--flow-width', `${20 + strength * 20}px`); // Wider for higher strength (if background-size allows)
              flowIndicator.style.setProperty('--bg-pos-start', '100%');
              flowIndicator.style.setProperty('--bg-pos-end', '0%');

        } else if (direction === 'right') {
            flowIndicator.classList.add('flow-right');
             flowIndicator.style.setProperty('--flow-speed', `${1 / (0.5 + strength * 0.5)}s`);
             flowIndicator.style.setProperty('--flow-opacity', `${0.4 + strength * 0.6}`);
             flowIndicator.style.setProperty('--flow-width', `${20 + strength * 20}px`);
             flowIndicator.style.setProperty('--bg-pos-start', '0%');
             flowIndicator.style.setProperty('--bg-pos-end', '100%');

        } else {
             // Stop animation and hide indicator
             flowIndicator.style.setProperty('--flow-speed', '0s');
             flowIndicator.style.setProperty('--flow-opacity', '0');
             flowIndicator.style.setProperty('--flow-width', '0px');
        }
    }


    function resetSimulation() {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;

        waterLevelLeft = initialWaterLevelPercent;
        waterLevelRight = initialWaterLevelPercent;
        updateWaterLevels();

        saltLeftSlider.disabled = false;
        saltRightSlider.disabled = false;
        startButton.disabled = false;
        resetButton.disabled = true;
        simStatus.textContent = 'הגדירו ריכוזים והפעילו!';

        // Reset labels based on current slider values
        updateSaltDisplay(saltLeftSlider, saltLeftValueSpan, soluteLeftLabel);
        updateSaltDisplay(saltRightSlider, saltRightValueSpan, soluteRightLabel);

        // Stop flow indicator
        setFlowIndicator('none');
         document.getElementById('chamber-left').style.borderColor = '#007bff';
         document.getElementById('chamber-right').style.borderColor = '#007bff';
    }

    function startSimulation() {
        if (animationFrameId) return; // Simulation already running

        const saltLeft = parseFloat(saltLeftSlider.value);
        const saltRight = parseFloat(saltRightSlider.value);

         // Check for identical concentrations before starting
        if (saltLeft === saltRight) {
             simStatus.textContent = 'ריכוזי המומסים זהים. לא תתרחש אוסמוזה נטו.';
             startButton.disabled = true; // Disable start, force reset
             resetButton.disabled = false;
             setFlowIndicator('none'); // Stop flow animation
             return;
         }

        saltLeftSlider.disabled = true;
        saltRightSlider.disabled = true;
        startButton.disabled = true;
        resetButton.disabled = false;
        simStatus.textContent = 'הדמיה פועלת...';

        // Osmosis force is proportional to concentration difference
        const concentrationDifference = saltRight - saltLeft; // Positive means flow L->R, negative means R->L

        // Determine flow direction and strength
        const flowDirection = concentrationDifference > 0 ? 'right' : 'left';
        // Strength is relative to max possible difference (20% - 0% = 20)
        const flowStrength = Math.abs(concentrationDifference) / 20; // Normalized 0 to 1

        // Start flow indicator animation
        setFlowIndicator(flowDirection, flowStrength);

        // Add a visual cue to the chamber with higher concentration (where water is going)
        if (concentrationDifference > 0) {
             document.getElementById('chamber-right').style.borderColor = '#28a745'; // Highlight green
              document.getElementById('chamber-left').style.borderColor = '#dc3545'; // Highlight red (losing water)
         } else {
             document.getElementById('chamber-left').style.borderColor = '#28a745'; // Highlight green
             document.getElementById('chamber-right').style.borderColor = '#dc3545'; // Highlight red (losing water)
         }


        const step = () => {
            // Calculate the raw potential level change based on initial concentrations
            // Note: A more accurate simulation would dynamically recalculate the driving force
            // based on current *effective* concentrations and hydrostatic pressure difference,
            // but keeping the original structure means a simpler, constant 'pull' towards equilibrium state.
            // Let's stick to a simplified model based on initial difference impacting speed.
            // A better simplified model: water moves towards higher concentration side.
            // The *rate* of movement could slow down as levels equalize OR as the hydrostatic pressure
            // difference builds up counteracting the osmotic pressure.

            // Simple model: water moves from lower to higher salt concentration
            const currentSaltLeft = parseFloat(saltLeftSlider.value); // Use initial values from sliders
            const currentSaltRight = parseFloat(saltRightSlider.value);

             // Simplified osmotic pressure effect + counteracting hydrostatic pressure effect
            const osmoticDrive = (currentSaltRight - currentSaltLeft) * simulationSpeed; // Initial drive
            const hydrostaticPressure = (waterLevelRight - waterLevelLeft) * 0.1; // Counter-pressure based on level difference
                                                                               // Adjust 0.1 constant to tune hydrostatic effect

            let netFlowDelta = osmoticDrive - hydrostaticPressure; // Positive delta -> L to R flow

            // Adjust delta based on boundaries
            const minLevel = initialWaterLevelPercent - maxWaterLevelChangePercent;
            const maxLevel = initialWaterLevelPercent + maxWaterLevelChangePercent;

            // If delta is positive (L->R flow), cap it if right chamber is near max or left is near min
            if (netFlowDelta > 0) {
                 const maxPossiblePositiveDelta = Math.min(maxLevel - waterLevelRight, waterLevelLeft - minLevel);
                 netFlowDelta = Math.min(netFlowDelta, maxPossiblePositiveDelta);
            } else { // If delta is negative (R->L flow), cap its magnitude
                 const maxPossibleNegativeDelta = Math.min(waterLevelRight - minLevel, maxLevel - waterLevelLeft);
                 netFlowDelta = -Math.min(Math.abs(netFlowDelta), maxPossibleNegativeDelta);
            }


            // Stop condition: Net flow is very small OR levels hit boundaries
            const effectiveDeltaMagnitude = Math.abs(netFlowDelta);
            const isNearEquilibrium = effectiveDeltaMagnitude < equilibriumThreshold;

            // Check if levels are at or very near boundaries *and* flow direction is outwards
            const isAtLeftBoundary = (waterLevelLeft <= minLevel + boundaryThreshold && netFlowDelta < 0);
            const isAtRightBoundary = (waterLevelRight <= minLevel + boundaryThreshold && netFlowDelta > 0); // This is wrong logic. Should be: if Left is losing water (netDelta > 0) and is near min
            const isAtLeftBoundaryStop = (waterLevelLeft <= minLevel + boundaryThreshold && netFlowDelta > 0); // Left losing, near min
            const isAtRightBoundaryStop = (waterLevelRight >= maxLevel - boundaryThreshold && netFlowDelta > 0); // Right gaining, near max
             const isAtLeftBoundaryGainStop = (waterLevelLeft >= maxLevel - boundaryThreshold && netFlowDelta < 0); // Left gaining, near max
             const isAtRightBoundaryLoseStop = (waterLevelRight <= minLevel + boundaryThreshold && netFlowDelta < 0); // Right losing, near min


            if (isNearEquilibrium || isAtLeftBoundaryStop || isAtRightBoundaryStop || isAtLeftBoundaryGainStop || isAtRightBoundaryLoseStop) {
                let statusText = '';
                if (isNearEquilibrium) {
                    statusText = 'שיווי משקל אוסמוטי כמעט הושג.';
                     // Nudge levels to exact equilibrium if close? Maybe not needed with smooth transition.
                     // Calculate ideal final state if total volume is conserved (it is in this model)
                     // Ideal final levels would make osmotic drive == hydrostatic pressure
                     // (saltR - saltL)*speed = (levelR - levelL)*0.1
                     // (saltR - saltL)*speed/0.1 = levelR - levelL
                     // (saltR - saltL)*speed/0.1 = (initial + deltaR) - (initial + deltaL) = deltaR - deltaL
                     // Since deltaR = -deltaL, (saltR - saltL)*speed/0.1 = 2*deltaR
                     // deltaR_final = (saltR - saltL)*speed / (0.1 * 2)
                     // Final levelR = initial + deltaR_final
                     // Final levelL = initial - deltaR_final
                     const idealDeltaR = (currentSaltRight - currentSaltLeft) * simulationSpeed / (0.1 * 2);
                     waterLevelRight = Math.max(minLevel, Math.min(maxLevel, initialWaterLevelPercent + idealDeltaR));
                     waterLevelLeft = Math.max(minLevel, Math.min(maxLevel, initialWaterLevelPercent - idealDeltaR));
                     updateWaterLevels(); // Ensure final positions
                } else {
                     statusText = 'המגבלה הושגה (לחץ הידרוסטטי או נפח).';
                      // Nudge levels to exact boundary if close
                     if(isAtLeftBoundaryStop) waterLevelLeft = minLevel;
                     if(isAtRightBoundaryStop) waterLevelRight = maxLevel;
                      if(isAtLeftBoundaryGainStop) waterLevelLeft = maxLevel;
                      if(isAtRightBoundaryLoseStop) waterLevelRight = minLevel;
                     updateWaterLevels(); // Ensure final positions
                }

                simStatus.textContent = statusText;
                cancelAnimationFrame(animationFrameId);
                animationFrameId = null;
                setFlowIndicator('none'); // Stop flow animation
                 document.getElementById('chamber-left').style.borderColor = '#007bff'; // Reset border colors
                 document.getElementById('chamber-right').style.borderColor = '#007bff';
                return;
            }

            // Apply the calculated flow delta
            waterLevelLeft -= netFlowDelta; // Left loses water if netFlowDelta > 0 (flow L->R)
            waterLevelRight += netFlowDelta; // Right gains water if netFlowDelta > 0 (flow L->R)

            // Ensure levels stay within bounds after update, clamping if necessary (this shouldn't happen if delta calculation is correct, but as a safeguard)
            waterLevelLeft = Math.max(minLevel, Math.min(maxLevel, waterLevelLeft));
            waterLevelRight = Math.max(minLevel, Math.min(maxLevel, waterLevelRight));


            updateWaterLevels();

             // Update flow indicator strength based on *current* net flow rate magnitude
             const currentFlowStrength = Math.abs(netFlowDelta) / (Math.abs(osmoticDrive - ( (maxLevel - minLevel) * 0.1 )) || 1); // Normalize against a plausible max flow
              setFlowIndicator(netFlowDelta > 0 ? 'right' : 'left', Math.min(1, currentFlowStrength * 5)); // Scale strength for visibility


            animationFrameId = requestAnimationFrame(step); // Continue animation loop
        };

        // Start the animation loop
        animationFrameId = requestAnimationFrame(step);
    }


    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);

    // Explanation button logic
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'מהי אוסמוזה? (הסבר מפורט)';
         // Scroll to explanation if shown
         if (!isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Initial state setup
    resetSimulation(); // Ensure initial state is correct
});
</script>