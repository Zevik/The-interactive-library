---
title: "נוירון באקשן: סימולטור פוטנציאל הפעולה"
english_slug: neuron-in-action-action-potential-simulator
category: "מדעי החיים / ביולוגיה"
tags: ["נוירופיזיולוגיה", "נוירון", "פוטנציאל פעולה", "הדמיה", "אינטראקטיבי", "מערכת העצבים"]
---
# נוירון באקשן: הדמיית פוטנציאל הפעולה

הצטרפו למסע מרתק אל תוך עולמו החשמלי של נוירון! בסימולטור אינטראקטיבי זה, תוכלו לשלוט על "קולות" (גירויים) שמגיעים לנוירון ולגלות כיצד הוא מחליט אם לירות את התגובה החשמלית הבסיסית ביותר של המוח - פוטנציאל פעולה! האם תצליחו לגרום לנוירון להגיב, או שהגירויים המתחרים יבלמו אותו?

<div class="neuron-simulator-container">
    <h2>המצב הנוכחי של הנוירון</h2>
    <div class="neuron-display">
        <div class="potential-display">
            <span class="label">פוטנציאל ממברנה:</span> <span id="membranePotentialDisplay" class="value">-70 mV</span>
        </div>
        <div class="threshold-display">
             <span class="label">סף ירייה:</span> <span id="thresholdDisplay" class="value">-55 mV</span>
        </div>
        <div class="state-display">
            <span class="label">מצב:</span> <span id="neuronStateDisplay" class="value">מנוחה</span>
        </div>
        <div class="refractory-indicator" id="refractoryIndicator">
            בתקופה רפרקטורית
        </div>
    </div>

    <div class="graph-area">
        <canvas id="potentialGraph"></canvas>
    </div>

    <div class="controls-area">
        <div class="control-group excitatory">
            <h3>קולות מעוררים (EPSP)</h3>
            <div class="control-row">
                <label for="excitatoryStrength">חוזק:</label>
                <input type="range" id="excitatoryStrength" min="0" max="5" step="0.2" value="0">
                <span id="excitatoryValue" class="value">0</span> mV
            </div>
            <div class="control-row">
                <label for="excitatoryFrequency">תדירות:</label>
                <input type="range" id="excitatoryFrequency" min="0" max="50" step="2" value="0">
                <span id="excitatoryFreqValue" class="value">0</span> Hz
            </div>
        </div>

        <div class="control-group inhibitory">
            <h3>קולות מעכבים (IPSP)</h3>
            <div class="control-row">
                <label for="inhibitoryStrength">חוזק:</label>
                <input type="range" id="inhibitoryStrength" min="0" max="5" step="0.2" value="0">
                <span id="inhibitoryValue" class="value">0</span> mV
            </div>
            <div class="control-row">
                <label for="inhibitoryFrequency">תדירות:</label>
                <input type="range" id="inhibitoryFrequency" min="0" max="50" step="2" value="0">
                <span id="inhibitoryFreqValue" class="value">0</span> Hz
            </div>
        </div>

        <div class="control-buttons">
            <button id="startButton">התחילו לחקור</button>
            <button id="stopButton" disabled>עצרו</button>
            <button id="resetButton">אפסו</button>
        </div>
    </div>
</div>

<button id="toggleExplanationButton" class="explanation-toggle-button">גלו עוד: מה קורה בנוירון?</button>

<div id="explanation" style="display: none;">
    <h2>הצלילה לעומק: מכניקת פוטנציאל הפעולה</h2>
    <p>הסימולטור הזה מאפשר לכם "לדבר" עם נוירון ולראות איך הוא מגיב. כל ההחלטות הגדולות שלו (האם "לירות" או לא) תלויות בפוטנציאל החשמלי של הממברנה שלו. חשבו על זה כעל "מצב רוח" חשמלי.</p>
    <p><strong>פוטנציאל מנוחה (-70mV):</strong> זהו "מצב הרוח" הבסיסי של הנוירון כשהוא שקט. פנים התא שלילי יותר מהחוץ.</p>
    <p><strong>סף ירייה (-55mV):</strong> זהו הקו האדום! אם פוטנציאל הממברנה מטפס ומגיע לסף הזה, הנוירון יורה פוטנציאל פעולה - תגובה חשמלית חזקה ומהירה. זוהי תגובת "הכל או כלום" קלאסית.</p>
    <p><strong>פוטנציאל פעולה - ה"ירייה":</strong> התפרצות חשמלית דרמטית שכוללת מספר שלבים מהירים:
        <ul>
            <li><strong>דפולריזציה (העלייה החדה):</strong> פוטנציאל הממברנה הופך חיובי מאוד לזמן קצר (מגיע לפיק סביב +30mV).</li>
            <li><strong>רפולריזציה (הירידה המהירה):</strong> הפוטנציאל חוזר במהירות להיות שלילי.</li>
            <li><strong>היפרפולריזציה (הצלילה הנמוכה מדי):</strong> לעיתים הפוטנציאל יורד מעט *מתחת* לפוטנציאל המנוחה לפני שהוא מתייצב חזרה.</li>
        </ul>
    </p>
    <p><strong>קולות מעוררים (EPSPs):</strong> אלו גירויים שמקבל הנוירון מנוירונים אחרים שגורמים לפוטנציאל הממברנה *לעלות* ולהתקרב אל סף הירייה. חשבו עליהם כעל "כן, תירה!" קולות.</p>
    <p><strong>קולות מעכבים (IPSPs):</strong> אלו גירויים שמקבל הנוירון וגורמים לפוטנציאל הממברנה *לרדת* ולהתרחק מסף הירייה. אלו הם "לא, אל תירה!" קולות.</p>
    <p>הנוירון כל הזמן "מקשיב" לכל הקולות (מעוררים ומעכבים) ומסכם אותם. אם הסכום הזה מגיע לסף הירייה, הוא יורה.</p>
    <p><strong>תקופה רפרקטורית:</strong> מיד לאחר ירייה, הנוירון נכנס לתקופה קצרה של "התאוששות". בזמן זה, קשה (תקופה רפרקטורית יחסית) או בלתי אפשרי (תקופה רפרקטורית מוחלטת) לגרום לו לירות שוב. הסימולטור מדמה תקופה זו כדי להראות מדוע אין יריות צפופות מדי.</p>
    <p><strong>מה כדאי לנסות?</strong>
        <ul>
            <li>התחילו עם גירוי מעורר בלבד והגבירו את החוזק או התדירות - מתי תגיעו לירייה?</li>
            <li>הוסיפו גירוי מעכב וראו כיצד הוא "מתחרה" עם המעורר ומונע ירייה.</li>
            <li>שחקו עם התדירות - כיצד קולות מהירים משפיעים לעומת קולות איטיים יותר?</li>
            <li>שימו לב לגרף ול"מצב" של הנוירון לאחר ירייה - מה קורה בזמן התקופה הרפרקטורית?</li>
            <li>האם אפשר ליצור ירייה אחת ארוכה או שזה תמיד פולס קצר? (רמז: זה תמיד קצר!).</li>
        </ul>
    </p>
</div>

<style>
    :root {
        --resting-potential: -70; /* Default resting potential */
        --threshold-potential: -55; /* Default threshold */
        --peak-potential: 30; /* Default AP peak */
        --hyperpolarization-potential: -85; /* Default hyperpolarization */
        --potential-range: 130; /* -90 to +40 */
        --potential-min: -90;

        --color-primary: #4e3a8a; /* Deep Purple - neuron color */
        --color-secondary: #e04e39; /* Vibrant Red - action potential */
        --color-excitatory: #5cb85c; /* Green - EPSP */
        --color-inhibitory: #f0ad4e; /* Orange - IPSP */
        --color-threshold: #d9534f; /* Dark Red - Threshold */
        --color-resting: #0275d8; /* Blue - Resting */
        --color-refractory: #d39e00; /* Gold - Refractory */

        --color-bg-main: #f4f7f6; /* Light background */
        --color-bg-card: #ffffff; /* White card */
        --color-bg-controls: #eceeef; /* Lighter background for controls */
        --color-text-main: #373a3c; /* Dark text */
        --color-border: #dddddd; /* Light gray border */

        --animation-speed-fast: 0.2s;
        --animation-speed-medium: 0.4s;
        --animation-speed-slow: 0.6s;
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: var(--color-text-main);
        background-color: var(--color-bg-main);
        padding: 20px;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2, h3 {
        color: var(--color-primary);
        text-align: center; /* Center titles despite RTL body */
        margin-bottom: 15px;
        font-weight: bold;
    }

    h1 { font-size: 2em; }
    h2 { font-size: 1.5em; }
    h3 { font-size: 1.2em; margin-top: 0; }

    p {
        margin-bottom: 15px;
    }

    .neuron-simulator-container {
        background-color: var(--color-bg-card);
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        gap: 30px;
        border: 1px solid var(--color-border);
    }

    .neuron-display {
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 15px 0;
        border-bottom: 2px solid var(--color-border);
        position: relative; /* For refractory indicator */
        flex-wrap: wrap; /* Allow wrapping on small screens */
        gap: 15px; /* Space between flex items */
    }

    .potential-display, .threshold-display, .state-display {
        font-size: 1.2em;
        font-weight: bold;
        display: flex;
        flex-direction: column; /* Stack label and value */
        align-items: center; /* Center text */
        min-width: 120px; /* Give items minimum width */
    }

     .neuron-display .label {
         font-size: 0.8em;
         font-weight: normal;
         color: var(--color-text-main);
         margin-bottom: 4px;
     }

    .potential-display .value { color: var(--color-resting); transition: color var(--animation-speed-medium) ease; }
    .threshold-display .value { color: var(--color-threshold); }
    .state-display .value { color: var(--color-primary); transition: color var(--animation-speed-medium) ease; }

    .refractory-indicator {
        position: absolute;
        top: 0;
        right: 0; /* Position right for RTL */
        left: auto; /* Ensure left is auto */
        background-color: var(--color-refractory);
        color: #373a3c;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 0.9em;
        display: none; /* Initially hidden */
        opacity: 0;
        transform: translateY(-10px); /* Start slightly above */
        transition: opacity 0.4s ease-out, transform 0.4s ease-out;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        z-index: 10; /* Ensure it's above other elements */
    }

    .refractory-indicator.active {
        display: block;
        opacity: 1;
        transform: translateY(0); /* Slide into place */
    }


    .graph-area {
        width: 100%;
        height: 300px; /* Increased height */
        border: 1px solid var(--color-border);
        border-radius: 8px;
        overflow: hidden; /* Ensure graph stays within bounds */
        background-color: #fcfcfc; /* Slightly lighter background for graph */
    }

    #potentialGraph {
        width: 100%;
        height: 100%;
        display: block;
    }

    .controls-area {
        display: flex;
        flex-wrap: wrap;
        gap: 25px; /* Increased gap */
        justify-content: center; /* Center controls */
    }

    .control-group {
        flex: 1; /* Allow groups to grow */
        min-width: 300px; /* Minimum width before wrapping */
        border: 1px solid var(--color-border);
        border-radius: 10px;
        padding: 20px;
        background-color: var(--color-bg-controls);
        display: flex;
        flex-direction: column;
        gap: 15px; /* Space between controls */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05); /* Inner shadow */
    }

     .control-group.excitatory h3 { color: var(--color-excitatory); }
     .control-group.inhibitory h3 { color: var(--color-inhibitory); }


    .control-group h3 {
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.2em;
        text-align: right; /* Titles within group should be right-aligned */
        border-bottom: 1px solid var(--color-border);
        padding-bottom: 10px;
    }

     .control-row {
         display: flex;
         align-items: center;
         gap: 10px;
     }

    .control-group label {
        font-weight: bold;
        font-size: 0.9em;
        flex-basis: 60px; /* Fixed width for labels */
        text-align: left; /* Align label text left in RTL layout */
    }

    .control-group input[type="range"] {
        flex-grow: 1; /* Slider takes available space */
        margin: 0; /* Remove default margin */
        vertical-align: middle;
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 10px; /* Thicker slider */
        background: #ddd;
        outline: none;
        opacity: 0.8;
        transition: opacity .2s;
        border-radius: 5px;
        cursor: pointer;
    }

     .control-group.excitatory input[type="range"]::-webkit-slider-thumb { background: var(--color-excitatory); }
     .control-group.excitatory input[type="range"]::-moz-range-thumb { background: var(--color-excitatory); }
     .control-group.inhibitory input[type="range"]::-webkit-slider-thumb { background: var(--color-inhibitory); }
     .control-group.inhibitory input[type="range"]::-moz-range-thumb { background: var(--color-inhibitory); }


    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* Larger thumb */
        height: 20px; /* Larger thumb */
        background: var(--color-primary); /* Default thumb color */
        cursor: pointer;
        border-radius: 50%;
        transition: background var(--animation-speed-fast) ease;
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--color-primary); /* Default thumb color */
        cursor: pointer;
        border-radius: 50%;
        transition: background var(--animation-speed-fast) ease;
    }

    .control-group .value {
         font-weight: bold;
         font-size: 0.9em;
         vertical-align: middle;
         flex-basis: 30px; /* Fixed width for value */
         text-align: left; /* Align value text left in RTL layout */
    }

    .control-buttons {
        width: 100%; /* Buttons take full width below controls */
        display: flex;
        justify-content: center;
        gap: 20px; /* Increased gap */
        margin-top: 20px;
    }

    button {
        padding: 12px 25px; /* Increased padding */
        font-size: 1.1em;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, opacity 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    button:hover:not(:disabled) {
         transform: translateY(-2px); /* Subtle hover effect */
         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    button:active:not(:disabled) {
         transform: translateY(0); /* Press down effect */
         box-shadow: none;
    }


    #startButton {
        background-color: var(--color-excitatory);
        color: white;
    }

    #startButton:hover:not(:disabled) {
         background-color: #4cae4c; /* Darker green */
    }

    #stopButton {
        background-color: var(--color-threshold);
        color: white;
    }

    #stopButton:hover:not(:disabled) {
        background-color: #c9302c; /* Darker red */
    }

     #resetButton {
        background-color: #6c757d; /* Gray */
        color: white;
    }

    #resetButton:hover:not(:disabled) {
        background-color: #5a6268; /* Darker gray */
    }

    button:disabled {
        opacity: 0.6; /* More visible disabled state */
        cursor: not-allowed;
        transform: none; /* No transform when disabled */
        box-shadow: none;
    }

    .explanation-toggle-button {
        display: block; /* Make button full width */
        width: fit-content; /* Fit content */
        margin: 30px auto 20px auto; /* Center the button and add more space below */
        background-color: var(--color-primary);
        color: white;
        font-size: 1em;
        padding: 10px 20px;
    }

     .explanation-toggle-button:hover {
        background-color: #3a2b6b; /* Darker purple */
    }

    #explanation {
        background-color: var(--color-bg-card);
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        border: 1px solid var(--color-border);
    }

     #explanation h2 {
         text-align: right; /* Align explanation title right */
         color: var(--color-resting);
     }

    #explanation ul {
        list-style-type: disc;
        padding-right: 20px; /* Add padding for list bullets in RTL */
        margin-bottom: 15px;
    }

    #explanation li {
        margin-bottom: 8px;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .neuron-display {
            flex-direction: column;
            gap: 10px;
        }

        .control-group {
            min-width: 250px;
        }

        .controls-area {
            flex-direction: column; /* Stack controls vertically */
            align-items: center;
            gap: 15px;
        }

        .control-group {
            width: 100%; /* Full width on smaller screens */
        }

        .control-buttons {
            flex-direction: column; /* Stack buttons vertically */
            gap: 10px;
        }

        button {
            width: 100%;
            padding: 10px 15px;
        }
    }

    /* Graph drawing styles handled in JS */
</style>

<script>
    const canvas = document.getElementById('potentialGraph');
    const ctx = canvas.getContext('2d');
    const membranePotentialDisplay = document.getElementById('membranePotentialDisplay');
    const thresholdDisplay = document.getElementById('thresholdDisplay');
    const neuronStateDisplay = document.getElementById('neuronStateDisplay');
    const refractoryIndicator = document.getElementById('refractoryIndicator');
    const excitatoryStrengthInput = document.getElementById('excitatoryStrength');
    const excitatoryValueSpan = document.getElementById('excitatoryValue');
    const excitatoryFrequencyInput = document.getElementById('excitatoryFrequency');
    const excitatoryFreqValueSpan = document.getElementById('excitatoryFreqValue');
    const inhibitoryStrengthInput = document.getElementById('inhibitoryStrength');
    const inhibitoryValueSpan = document.getElementById('inhibitoryValue');
    const inhibitoryFrequencyInput = document.getElementById('inhibitoryFrequency');
    const inhibitoryFreqValueSpan = document.getElementById('inhibitoryFreqValue');
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const resetButton = document.getElementById('resetButton');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');

    // Neuron simulation parameters (using CSS variables for default visual refs)
    const restingPotential = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--resting-potential'));
    const thresholdPotential = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--threshold-potential'));
    const peakPotential = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--peak-potential'));
    const hyperpolarizationPotential = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--hyperpolarization-potential'));
    const potentialRange = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--potential-range'));
    const potentialMin = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--potential-min'));

    let membranePotential = restingPotential; // mV
    const potentialDecayRate = 0.02; // How quickly potential returns to rest per step (tuned for visual smoothness)
    const actionPotentialSpeedDepol = 5; // Speed of depolarization phase
    const actionPotentialSpeedRepol = 3; // Speed of repolarization phase
    const actionPotentialSpeedHyper = 0.5; // Speed returning from hyperpolarization

    const refractoryPeriodDuration = 50; // Simulation steps for total refractory period
    const absoluteRefractoryDuration = 20; // Simulation steps where no stimulus works

    let isSimulating = false;
    let simulationFrameId = null;
    let simulationTime = 0; // In simulation steps (arbitrary unit, could be ms)
    const maxGraphTime = 600; // Number of steps to show on graph (increased for more history)
    const simulationStepInterval = 10; // Milliseconds per simulation step (faster simulation)

    let excitatoryStrength = parseFloat(excitatoryStrengthInput.value);
    let excitatoryFrequency = parseInt(excitatoryFrequencyInput.value);
    let inhibitoryStrength = parseFloat(inhibitoryStrengthInput.value);
    let inhibitoryFrequency = parseInt(inhibitoryFrequencyInput.value);

    let refractoryTimer = 0; // Steps remaining in refractory period
    let apPhase = 'resting'; // 'resting', 'depolarizing', 'repolarizing', 'hyperpolarizing'

    const potentialHistory = [];
    let simulationInterval = null; // Use interval for consistent step timing

    // Function to smoothly transition potential display color
    function animatePotentialColor(potential) {
        const displayElement = membranePotentialDisplay.parentElement; // The container div
        const valueElement = membranePotentialDisplay; // The span with the value

        let color = varToRgb('--color-resting'); // Default color

        if (apPhase === 'depolarizing' || apPhase === 'repolarizing') {
            color = varToRgb('--color-secondary'); // Action potential color
        } else if (apPhase === 'hyperpolarizing') {
             color = varToRgb('--color-threshold'); // Indicate low potential
        } else if (potential >= thresholdPotential - 5) { // Near threshold
             color = varToRgb('--color-inhibitory'); // Warning color
        } else {
             color = varToRgb('--color-resting');
        }

        valueElement.style.color = color; // Apply color directly for transition
    }

    function updateDisplay() {
        membranePotentialDisplay.textContent = membranePotential.toFixed(1) + ' mV';
        thresholdDisplay.textContent = thresholdPotential.toFixed(1) + ' mV'; // Static threshold
        neuronStateDisplay.textContent = apPhase === 'resting' && refractoryTimer <= 0 ? 'מנוחה' :
                                        apPhase === 'depolarizing' ? 'דפולריזציה' :
                                        apPhase === 'repolarizing' ? 'רפולריזציה' :
                                        apPhase === 'hyperpolarizing' ? 'היפרפולריזציה' :
                                        'לא זמין (רפרקטורית)'; // Refractory covers all non-resting non-AP states

        animatePotentialColor(membranePotential); // Update display color

        if (refractoryTimer > 0) {
            refractoryIndicator.classList.add('active');
        } else {
            refractoryIndicator.classList.remove('active');
        }

        excitatoryValueSpan.textContent = excitatoryStrength.toFixed(1); // Show one decimal
        excitatoryFreqValueSpan.textContent = excitatoryFrequency;
        inhibitoryValueSpan.textContent = inhibitoryStrength.toFixed(1); // Show one decimal
        inhibitoryFreqValueSpan.textContent = inhibitoryFrequency;
    }

    function drawGraph() {
        const graphWidth = canvas.width;
        const graphHeight = canvas.height;
        ctx.clearRect(0, 0, graphWidth, graphHeight);

        // Calculate Y positions for key potentials
        const getY = (potential) => graphHeight * (1 - (potential - potentialMin) / potentialRange);

        const yResting = getY(restingPotential);
        const yThreshold = getY(thresholdPotential);
        const yZero = getY(0); // Optional: draw 0mV line

        // Draw background grid (optional but nice)
        ctx.strokeStyle = '#eee';
        ctx.lineWidth = 0.5;
        // Horizontal lines (e.g., every 20mV)
         for (let v = -80; v <= 40; v += 20) {
             if (v < potentialMin || v > (potentialMin + potentialRange)) continue;
             const y = getY(v);
             ctx.beginPath();
             ctx.moveTo(0, y);
             ctx.lineTo(graphWidth, y);
             ctx.stroke();
             // Add labels
             ctx.fillStyle = '#888';
             ctx.font = '10px Arial';
             ctx.textAlign = 'left'; // Labels on the left for RTL graph
             ctx.fillText(v + 'mV', 5, y - 2);
         }
         // Vertical lines (e.g., time markers) - more complex with time history


        // Draw key potential lines
        ctx.setLineDash([5, 5]); // Dashed line
        ctx.lineWidth = 1.5;

        // Resting potential line
        ctx.strokeStyle = varToRgb('--color-resting');
        ctx.beginPath();
        ctx.moveTo(0, yResting);
        ctx.lineTo(graphWidth, yResting);
        ctx.stroke();
        ctx.fillStyle = varToRgb('--color-resting');
        ctx.font = '11px Arial';
        ctx.textAlign = 'right'; // Label on the right for RTL graph
        ctx.fillText('מנוחה (' + restingPotential + 'mV)', graphWidth - 5, yResting - 5);

        // Threshold line
        ctx.strokeStyle = varToRgb('--color-threshold');
        ctx.beginPath();
        ctx.moveTo(0, yThreshold);
        ctx.lineTo(graphWidth, yThreshold);
        ctx.stroke();
        ctx.fillStyle = varToRgb('--color-threshold');
        ctx.fillText('סף (' + thresholdPotential + 'mV)', graphWidth - 5, yThreshold + 15); // Position label below threshold


        ctx.setLineDash([]); // Solid line

        // Draw potential history
        ctx.strokeStyle = varToRgb('--color-secondary'); // Action potential color
        ctx.lineWidth = 2.5; // Thicker line for the trace
        ctx.beginPath();

        const startIndex = Math.max(0, potentialHistory.length - maxGraphTime);
        for (let i = startIndex; i < potentialHistory.length; i++) {
            const potential = potentialHistory[i];
            // Map history index to x position on the visible graph area
            const x = graphWidth * (i - startIndex) / Math.min(potentialHistory.length, maxGraphTime);
            const y = getY(potential);

            if (i === startIndex) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        ctx.stroke();
    }

    // Helper function to get CSS variable color
    function varToRgb(variable) {
        const style = getComputedStyle(document.documentElement);
        return style.getPropertyValue(variable).trim();
    }

    function applyStimulus() {
         let stimulusInput = 0;

         // Excitatory Input (based on frequency and strength)
         // FrequencyHz * simulationStepInterval / 1000 = Probability per step
         const excitatoryProbPerStep = excitatoryFrequency * simulationStepInterval / 1000;
         if (Math.random() < excitatoryProbPerStep) { // Probabilistic stimulus delivery
             stimulusInput += excitatoryStrength;
         }

         // Inhibitory Input (based on frequency and strength)
         const inhibitoryProbPerStep = inhibitoryFrequency * simulationStepInterval / 1000;
          if (Math.random() < inhibitoryProbPerStep) { // Probabilistic stimulus delivery
             stimulusInput -= inhibitoryStrength;
         }

         // Apply decay and stimulus
         // The potential decays exponentially back to resting potential over time
         // V_next = V_rest + (V_current - V_rest) * decay_factor + stimulus
         membranePotential = restingPotential + (membranePotential - restingPotential) * (1 - potentialDecayRate) + stimulusInput;

         // Clamp potential to prevent extreme values outside the expected range (unless during AP)
         if (apPhase === 'resting' || apPhase === 'hyperpolarizing') {
             if (membranePotential < hyperpolarizationPotential) membranePotential = hyperpolarizationPotential;
             // Do not clamp above resting potential unless near threshold to allow summation
             if (membranePotential > restingPotential && membranePotential < thresholdPotential && membranePotential > thresholdPotential + 10) {
                 membranePotential = thresholdPotential + 10; // Prevent free rise far above threshold
             }
         }
    }

    function simulateStep() {
        simulationTime++;

        // --- Action Potential & Refractory Logic ---
        if (apPhase === 'depolarizing') {
            membranePotential += actionPotentialSpeedDepol; // Rapid rise
            if (membranePotential >= peakPotential) {
                membranePotential = peakPotential;
                apPhase = 'repolarizing';
            }
        } else if (apPhase === 'repolarizing') {
             membranePotential -= actionPotentialSpeedRepol; // Rapid fall
             if (membranePotential <= hyperpolarizationPotential) { // Fall below rest
                 membranePotential = hyperpolarizationPotential;
                 apPhase = 'hyperpolarizing';
                 refractoryTimer = refractoryPeriodDuration; // Start refractory period
             } else if (membranePotential <= restingPotential && refractoryTimer <= 0) { // Back to rest before hyperpolarization
                 apPhase = 'resting'; // Should not happen if hyperpolarization always follows, but as fallback
             }
        } else if (apPhase === 'hyperpolarizing') {
            // Slowly return from hyperpolarization towards resting potential
            membranePotential = restingPotential + (membranePotential - restingPotential) * (1 - actionPotentialSpeedHyper * potentialDecayRate);
            // Clamp to resting if it crosses or gets very close to prevent oscillation
             if (membranePotential >= restingPotential - 0.1) {
                 membranePotential = restingPotential;
                 apPhase = 'resting';
             }
        } else { // 'resting' phase
             // Only apply stimulus and check threshold in resting phase and outside absolute refractory
             if (refractoryTimer <= absoluteRefractoryDuration) { // Allow stimuli but maybe less effective in relative period? Simplified: no stimuli in refractory.
                 applyStimulus();
             } else {
                 // Even in resting, decay back if somehow moved away without stimuli
                 membranePotential = restingPotential + (membranePotential - restingPotential) * (1 - potentialDecayRate);
             }


             // Check for Threshold crossing (only if fully out of refractory)
             if (refractoryTimer <= 0 && membranePotential >= thresholdPotential) {
                 apPhase = 'depolarizing'; // Trigger action potential
                 membranePotential = thresholdPotential; // Start AP exactly at threshold for visual clarity
             }
        }

        // --- Refractory Period Update ---
        if (refractoryTimer > 0) {
            refractoryTimer--;
        }

        // Add current potential to history
        potentialHistory.push(membranePotential);
        // No need to manually shift if using a fixed length array and circular buffer,
        // but push/shift is simpler for variable length and display history
        if (potentialHistory.length > maxGraphTime) {
            potentialHistory.shift(); // Remove oldest point
        }

        updateDisplay();
        drawGraph();
    }

    function startSimulation() {
        if (!isSimulating) {
            isSimulating = true;
            startButton.disabled = true;
            stopButton.disabled = false;
            resetButton.disabled = true; // Disable reset while simulating
            // Use setInterval for consistent step timing
            simulationInterval = setInterval(simulateStep, simulationStepInterval);
        }
    }

    function stopSimulation() {
        if (isSimulating) {
            isSimulating = false;
            startButton.disabled = false;
            stopButton.disabled = true;
            resetButton.disabled = false; // Enable reset when stopped
            if (simulationInterval) {
                clearInterval(simulationInterval);
                simulationInterval = null;
            }
        }
    }

    function resetSimulation() {
        stopSimulation(); // Ensure simulation is stopped
        membranePotential = restingPotential;
        simulationTime = 0;
        potentialHistory.length = 0; // Clear history
        refractoryTimer = 0;
        apPhase = 'resting';
        // Reset controls visually and internally? Maybe just visually.
        // excitatoryStrengthInput.value = 0; excitatoryStrength = 0;
        // ... reset all control values if desired ...
        updateDisplay();
        setupCanvas(); // Redraw initial state and potential lines
        startButton.disabled = false; // Enable start button
        stopButton.disabled = true;
        resetButton.disabled = false; // Keep reset enabled
    }

    // Event Listeners for controls
    excitatoryStrengthInput.addEventListener('input', (e) => {
        excitatoryStrength = parseFloat(e.target.value);
        excitatoryValueSpan.textContent = excitatoryStrength.toFixed(1);
    });

    excitatoryFrequencyInput.addEventListener('input', (e) => {
        excitatoryFrequency = parseInt(e.target.value);
        excitatoryFreqValueSpan.textContent = excitatoryFrequency;
    });

    inhibitoryStrengthInput.addEventListener('input', (e) => {
        inhibitoryStrength = parseFloat(e.target.value);
        inhibitoryValueSpan.textContent = inhibitoryStrength.toFixed(1);
    });

     inhibitoryFrequencyInput.addEventListener('input', (e) => {
        inhibitoryFrequency = parseInt(e.target.value);
        inhibitoryFreqValueSpan.textContent = inhibitoryFrequency;
    });

    startButton.addEventListener('click', startSimulation);
    stopButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתירו את ההסבר' : 'גלו עוד: מה קורה בנוירון?';
        // Scroll to explanation if showing it
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });


    // Initial setup
    function setupCanvas() {
         // Set canvas dimensions to match display size
         const graphArea = canvas.parentElement;
         canvas.width = graphArea.clientWidth;
         canvas.height = graphArea.clientHeight;
         drawGraph(); // Draw initial state and lines
    }

    // Draw initial state on load
    updateDisplay();
    setupCanvas();
    // Redraw graph on window resize
    window.addEventListener('resize', setupCanvas);

    // Optional: Initial nudge to draw graph lines correctly on load
    // A small timeout might be needed if canvas parent size isn't immediately available
    setTimeout(setupCanvas, 10);

</script>