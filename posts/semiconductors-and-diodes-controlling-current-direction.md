---
title: "מוליכים למחצה ודיודות: מאסטרים של כיוון זרם"
english_slug: semiconductors-and-diodes-controlling-current-direction
category: "פיזיקה"
tags: חשמל, אלקטרוניקה, מוליכים למחצה, דיודה, מעגלים חשמליים, סימולציה
---
<p>איך רכיבים אלקטרוניים זעירים שולטים בחשמל וקובעים לאן הוא יזרום? דמיינו שסתום קסם שמאפשר למים לזרום רק בכיוון אחד. בעולם האלקטרוניקה, הרכיב הזה קיים, והוא נקרא "דיודה". בואו נשחק קצת עם מעגל חשמלי ונראה איך הדיודה הופכת את הכיוון של הזרם לחשובה כל כך!</p>

<div class="interactive-app">
    <div class="circuit-container">
        <svg id="circuitSVG" width="600" height="400" viewBox="0 0 600 400">
            <!-- Circuit Paths -->
            <path id="path1" class="circuit-path" d="M 50,200 L 150,200" stroke-linecap="round"/>
            <path id="path2" class="circuit-path" d="M 150,200 L 150,100" stroke-linecap="round"/>
            <path id="path3" class="circuit-path diode-path" d="M 150,100 L 450,100" stroke-linecap="round"/> <!-- Path for diode placement -->
            <path id="path4" class="circuit-path" d="M 450,100 L 450,200" stroke-linecap="round"/>
            <path id="path5" class="circuit-path" d="M 450,200 L 550,200" stroke-linecap="round"/>
            <path id="path6" class="circuit-path" d="M 550,200 L 550,300" stroke-linecap="round"/>
            <path id="path7" class="circuit-path" d="M 550,300 L 50,300" stroke-linecap="round"/>
            <path id="path8" class="circuit-path" d="M 50,300 L 50,200" stroke-linecap="round"/>

            <!-- Component placeholder / snap points -->
            <rect id="diodePlacementRect" x="270" y="85" width="60" height="30" fill="transparent" class="placement-area"></rect>
            <text x="300" y="75" text-anchor="middle" alignment-baseline="middle" font-size="14" fill="#555" class="placement-hint">גרור לכאן את הדיודה</text>


            <!-- Components -->
            <!-- Battery -->
            <g id="battery" transform="translate(50, 250) rotate(-90)" class="circuit-component battery">
                 <rect x="-15" y="-20" width="30" height="40" class="component-body"/>
                 <line x1="-15" y="-10" x2="15" y="-10" class="battery-long"/>
                 <line x1="-15" y="10" x2="15" y="10" class="battery-short"/>
                 <text x="-10" y="-15" font-size="12" fill="#333" id="batteryPlus">+</text>
                 <text x="-10" y="25" font-size="12" fill="#333" id="batteryMinus">-</text>
                 <text x="0" y="55" text-anchor="middle" font-size="14" fill="#333" transform="rotate(90 0 55)">סוללה</text>
            </g>

            <!-- Resistor -->
            <g id="resistor" transform="translate(150, 150)" class="circuit-component resistor">
                <path d="M-30,0 l10,0 l3.3,-10 l6.7,20 l6.7,-20 l6.7,20 l6.7,-20 l6.7,20 l3.3,-10 l10,0" class="component-body"/>
                 <text x="0" y="-20" text-anchor="middle" font-size="14" fill="#333">נגד</text>
            </g>

            <!-- LED -->
            <g id="led" transform="translate(500, 250) rotate(90)" class="circuit-component led">
                 <circle cx="0" cy="0" r="15" class="component-body"/>
                 <line x1="-15" y="0" x2="15" y="0" class="component-line"/>
                 <line x1="0" y="-15" x2="0" y="15" class="component-line"/>
                 <polygon points="-5,-10 0,-15 5,-10" class="component-line"/>
                 <polygon points="-10,-5 -15,0 -10,5" class="component-line"/>
                 <text x="0" y="28" text-anchor="middle" font-size="14" fill="#333" transform="rotate(-90 0 28)">LED</text>
                  <circle cx="0" cy="0" r="18" fill="yellow" opacity="0" class="led-glow"/> <!-- Glow effect -->
            </g>

             <!-- Diode (draggable - initially outside circuit) -->
            <g id="diodePart" class="draggable circuit-component diode" transform="translate(50, 50)" cursor="grab">
                <rect x="-25" y="-15" width="50" height="30" fill="#a8dadc" stroke="#1d3557" stroke-width="1" rx="3" ry="3"/>
                <!-- Diode symbol -->
                <path d="M-15,0 L15,0 M-15,-10 L0,0 L-15,10 M15,-10 L15,10" stroke="#1d3557" stroke-width="2" fill="none" class="diode-symbol"/>
                 <text x="0" y="25" text-anchor="middle" font-size="14" fill="#333">דיודה</text>
            </g>

            <!-- Current flow indicators (dots) -->
            <g id="currentDotsContainer"></g>

        </svg>
    </div>

    <div class="controls">
        <div class="control-group">
            <label for="voltageSlider">מתח סוללה:</label>
            <input type="range" id="voltageSlider" min="0" max="5" step="0.1" value="0">
            <span id="voltageValue" class="value-display">0.0 V</span>
        </div>
        <div class="control-group">
            <label for="polaritySwitch">קוטביות סוללה:</label>
             <div class="switch-container">
                 <span>רגילה</span>
                 <label class="switch">
                  <input type="checkbox" id="polaritySwitch">
                  <span class="slider round"></span>
                </label>
                <span>הפוכה</span>
             </div>
        </div>
         <div class="control-group readings">
            <p>מדדים:</p>
            <p>מתח על הדיודה: <span id="diodeVoltage" class="value-display">0.0 V</span></p>
            <p>זרם במעגל: <span id="circuitCurrent" class="value-display">0.00 mA</span></p>
        </div>
         <div class="control-group diode-controls">
             <button id="rotateDiodeBtn" class="control-button" style="display:none;">סובב דיודה</button>
             <button id="removeDiodeBtn" class="control-button secondary" style="display:none;">הסר דיודה</button>
         </div>
    </div>

</div>

<button id="toggleExplanationBtn" class="toggle-button">הצג הסבר / הסתר הסבר</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: העולם הקטן של מוליכים למחצה והדיודה</h2>
    <p><strong>מוליכים למחצה - לא סתם חומר:</strong> יש חומרים שמוליכים חשמל בקלות (כמו מתכות), ויש כאלה שבקושי (כמו פלסטיק). מוליכים למחצה (סיליקון וגרמניום הם המפורסמים ביותר) הם קצת משניהם. התכונה המדהימה שלהם היא שאפשר לשלוט ביכולת ההולכה שלהם על ידי שינוי קל בהרכב שלהם (תחשבו על זה כעל "תיבול" אטומי). זה מה שהופך אותם לבסיס של כל הטכנולוגיה האלקטרונית המודרנית.</p>

    <p><strong>דיודה - השסתום האלקטרוני:</strong> הדיודה היא אחת הרכיבים הפשוטים והחשובים ביותר שנוצרו ממוליכים למחצה. תפקידה קריטי: היא מאפשרת לזרם חשמלי לזרום רק לכיוון אחד - כמו שסתום חד-כיווני בצינור מים. בכיוון ההפוך? היא חוסמת אותו כמעט לחלוטין.</p>

    <p><strong>מאחורי הקלעים: צומת P-N:</strong> איך היא עושה את זה? דיודה בנויה משני סוגי מוליכים למחצה ש"תובלו" באופן שונה: אזור אחד עם עודף "חורים" (שמתנהגים כנושאי מטען חיוביים - P Type), ואזור שני עם עודף אלקטרונים (נושאי מטען שליליים - N Type). המפגש ביניהם נקרא "צומת P-N". ה"קסם" קורה בדיוק שם.</p>

    <p><strong>זרם עובר או לא עובר? זה תלוי בהטיה:</strong></p>
    <ul>
        <li><strong>הטיה קדמית (Forward Bias) - אור ירוק לזרם:</strong> כשמחברים את הצד החיובי של הסוללה (הפלוס) לאזור ה-P של הדיודה ואת הצד השלילי (המינוס) לאזור ה-N, נושאי המטען נדחפים בכוח אל עבר הצומת. אם המתח של הסוללה מספיק גבוה (מעל "מתח סף" קטן, בערך 0.7V לסיליקון), נושאי המטען מצליחים לחצות את הצומת וזורם זרם משמעותי במעגל. בסימולציה, זה רגע ה"וואו" שבו ה-LED נדלק!</li>
        <li><strong>הטיה אחורית (Reverse Bias) - אור אדום, אין כניסה:</strong> כשמחברים את הקוטביות הפוך - פלוס לאזור ה-N ומינוס לאזור ה-P - נושאי המטען נמשכים דווקא הרחק מהצומת. אזור ליד הצומת מתרוקן מנושאי מטען יעילים, ונוצר מחסום חשמלי. זרם לא יכול לעבור (למעט זרם זליגה זעיר מאוד שניתן להתעלם ממנו). בסימולציה, תראו שה-LED נשאר כבוי, לא משנה כמה תגבירו את המתח (בגבולות הסביר כמובן).</li>
    </ul>

    <p><strong>בסימולציה שלנו:</strong> כאן אתם המהנדסים! הסוללה נותנת את הכוח, הנגד מגביל את הזרם כדי שלא נשרוף את הרכיבים, ה-LED הוא מנורת החיווי שלנו (כשהוא דולק, זורם זרם!). הדיודה שאתם יכולים לגרור למעגל היא השסתום. נסו לשנות את המתח ואת קוטביות הסוללה, לגרור את הדיודה למקום ולסובב אותה, ותראו איך הדיודה שולטת בזרימת הזרם ובאור ה-LED.</p>

    <p><strong>למה זה חשוב?</strong> דיודות נמצאות בכל מקום! הן ממירות זרם חילופין (AC) לזרם ישר (DC) בספקי כוח של כל מכשיר חשמלי, הן מגנות על רכיבים עדינים, משמשות כמתגים מהירים במחשבים ועוד המון יישומים שהפכו את חיינו לנוחים וטכנולוגיים יותר.</p>
</div>

<style>
    /* General Styling */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        direction: rtl; /* Hebrew */
        text-align: right;
    }

    h1, h2 {
        color: #1d3557;
        text-align: center;
    }

    p {
        margin-bottom: 1em;
    }

    /* Interactive App Container */
    .interactive-app {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px auto;
        padding: 20px;
        border-radius: 12px;
        background-color: #f1faee;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 800px;
    }

    /* Circuit SVG Container */
    .circuit-container {
        width: 100%;
        max-width: 600px;
        height: 400px;
        position: relative;
        margin-bottom: 30px;
        background-color: #ffffff;
        border: 2px solid #a8dadc;
        border-radius: 8px;
        overflow: hidden; /* Keep SVG content within bounds */
    }

    #circuitSVG {
         display: block; /* Remove extra space below svg */
         overflow: hidden; /* Ensure content stays within bounds even with dragging */
    }

    /* Circuit Paths */
    .circuit-path {
        stroke: #333;
        stroke-width: 3;
        fill: none;
        transition: stroke 0.3s ease; /* Smooth color change */
    }

    /* Component Styling */
    .circuit-component {
         transition: transform 0.2s ease-out; /* Smooth movement */
    }

    .component-body {
        fill: none;
        stroke: #1d3557;
        stroke-width: 2;
    }

    .component-line {
        stroke: #1d3557;
        stroke-width: 2;
    }

    .battery-long {
        stroke: #e63946;
        stroke-width: 4;
    }
     .battery-short {
        stroke: #1d3557;
        stroke-width: 2;
    }

    .diode .component-body {
         fill: #a8dadc; /* Default fill */
         stroke: #1d3557;
         stroke-width: 1;
         transition: fill 0.3s ease;
    }
     .diode-symbol {
         stroke: #1d3557;
         stroke-width: 2;
     }

     .diode.draggable rect {
         stroke: #457b9d;
         stroke-width: 2;
     }

    .led-glow {
        transition: opacity 0.3s ease-in-out;
    }


    /* Drag and Drop Styling */
    .draggable {
        cursor: grab;
        filter: drop-shadow(0 2px 5px rgba(0,0,0,0.2));
    }

    .draggable:active {
        cursor: grabbing;
    }

    .diode-placed {
        cursor: default;
        filter: none; /* Remove shadow when placed */
    }

    .placement-area {
        stroke-dasharray: 6,6;
        stroke: #457b9d;
        stroke-width: 2;
        transition: stroke 0.3s ease, opacity 0.3s ease;
    }

    .placement-hint {
         fill: #457b9d;
         transition: opacity 0.3s ease;
    }

     .diode-placed + .placement-hint {
        opacity: 0; /* Hide hint when diode is placed */
     }

     .diode-placed + .placement-area {
         stroke: #77cc77; /* Green border when placed */
     }


    /* Current Flow Animation */
    .current-dot {
        r: 4; /* Slightly larger dots */
        fill: #e63946; /* Red color for flow */
        animation: current-flow 2s linear infinite;
        transform-box: fill-box;
        transform-origin: center;
        opacity: 0.8;
        display: none; /* Hidden by default */
    }

     .current-dot.reverse {
        animation-direction: reverse;
     }

    @keyframes current-flow {
        from { motion-offset: 0%; }
        to { motion-offset: 100%; }
    }

    /* Controls Styling */
    .controls {
        width: 100%;
        max-width: 600px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Center controls */
        gap: 20px;
        padding: 20px;
        background-color: #a8dadc;
        border-radius: 8px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        min-width: 180px; /* Give controls more space */
    }

    .control-group label {
        font-weight: bold;
        margin-bottom: 8px;
        color: #1d3557;
    }

    .control-group.readings {
        background-color: #f1faee;
        padding: 15px;
        border-radius: 6px;
        border: 1px solid #457b9d;
    }

    .control-group.readings p {
         margin: 5px 0;
         font-size: 0.95em;
    }

    .value-display {
        font-weight: normal;
        color: #e63946; /* Highlight values */
        font-family: 'Courier New', monospace; /* Monospaced for values */
    }


    #voltageSlider {
        width: 100%;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #457b9d;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    #voltageSlider:hover {
        opacity: 1;
    }

    #voltageSlider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #e63946;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #1d3557;
    }

    #voltageSlider::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #e63946;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #1d3557;
    }

    /* Toggle Switch Styling */
    .switch-container {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .switch-container span {
        font-weight: normal;
        font-size: 0.9em;
        color: #1d3557;
    }

    .switch {
      position: relative;
      display: inline-block;
      width: 40px;
      height: 24px;
    }

    .switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }

    .slider {
      position: absolute;
      cursor: pointer;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #ccc;
      -webkit-transition: .4s;
      transition: .4s;
      border-radius: 24px;
    }

    .slider:before {
      position: absolute;
      content: "";
      height: 16px;
      width: 16px;
      left: 4px;
      bottom: 4px;
      background-color: white;
      -webkit-transition: .4s;
      transition: .4s;
      border-radius: 50%;
    }

    input:checked + .slider {
      background-color: #457b9d;
    }

    input:focus + .slider {
      box-shadow: 0 0 1px #457b9d;
    }

    input:checked + .slider:before {
      -webkit-transform: translateX(16px);
      -ms-transform: translateX(16px);
      transform: translateX(16px);
    }

    /* Buttons */
    .control-button, .toggle-button {
        padding: 10px 15px;
        font-size: 0.95em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        transition: background-color 0.2s ease, opacity 0.2s ease;
        background-color: #457b9d;
        color: white;
    }

    .control-button:hover, .toggle-button:hover {
        background-color: #1d3557;
    }

    .control-button.secondary {
         background-color: #e63946;
    }
     .control-button.secondary:hover {
        background-color: #c0392b;
     }


    /* Explanation Section */
    #explanation {
        margin: 30px auto;
        padding: 20px;
        border: 1px solid #a8dadc;
        border-radius: 8px;
        background-color: #f1faee;
        max-width: 800px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    #explanation h2 {
        margin-top: 0;
        border-bottom: 2px solid #457b9d;
        padding-bottom: 10px;
        margin-bottom: 15px;
        text-align: right; /* Hebrew */
    }

    #explanation p, #explanation ul {
        text-align: right; /* Hebrew */
    }

    #explanation ul {
        list-style: disc inside;
        padding-right: 20px;
    }

    #explanation li {
        margin-bottom: 8px;
    }

     .toggle-button {
        display: block;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 1em;
     }


</style>

<script>
    const svg = document.getElementById('circuitSVG');
    const diodePart = document.getElementById('diodePart');
    const diodePlacementRect = document.getElementById('diodePlacementRect');
    const diodePlacementHint = svg.querySelector('.placement-hint'); // Select the hint text
    const voltageSlider = document.getElementById('voltageSlider');
    const voltageValueSpan = document.getElementById('voltageValue');
    const polaritySwitch = document.getElementById('polaritySwitch');
    const diodeVoltageSpan = document.getElementById('diodeVoltage');
    const circuitCurrentSpan = document.getElementById('circuitCurrent');
    const rotateDiodeBtn = document.getElementById('rotateDiodeBtn');
    const removeDiodeBtn = document.getElementById('removeDiodeBtn'); // Get the new remove button
    const batteryPlus = document.getElementById('batteryPlus');
    const batteryMinus = document.getElementById('batteryMinus');
    const led = document.getElementById('led');
    const ledGlow = led.querySelector('.led-glow'); // Get the glow element
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const currentDotsContainer = document.getElementById('currentDotsContainer'); // Container for dots


    const paths = {
        'path1': document.getElementById('path1'),
        'path2': document.getElementById('path2'),
        'path3': document.getElementById('path3'), // Diode path
        'path4': document.getElementById('path4'),
        'path5': document.getElementById('path5'),
        'path6': document.getElementById('path6'),
        'path7': document.getElementById('path7'),
        'path8': document.getElementById('path8'),
    };

    const pathElements = Object.values(paths);


    // Create multiple current dots dynamically
    const numberOfDots = 8; // More dots for smoother animation
    const currentDots = [];
    for (let i = 0; i < numberOfDots; i++) {
        const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        dot.setAttribute('class', 'current-dot');
        dot.setAttribute('r', '4');
        dot.style.animationDelay = `${i * (2 / numberOfDots)}s`; // Stagger animation
        currentDotsContainer.appendChild(dot);
        currentDots.push(dot);
    }


    let isDragging = false;
    let offset = { x: 0, y: 0 }; // Offset for drag
    let diodePlaced = false;
    let diodeOrientation = 0; // 0 degrees (forward) or 180 degrees (reverse)
    const diodeThresholdVoltage = 0.7; // Silicon diode threshold (V)
    const resistorValue = 100; // Resistor value (Ohms)
    const ledForwardVoltage = 1.8; // Typical LED forward voltage (V)
    const ledSeriesResistance = 10; // Simplify LED model with series resistance (Ohms)
    const diodePosition = { x: 300, y: 100 }; // Target position for the diode


    // --- Helper function to convert screen coords to SVG coords ---
    function getSvgCoords(clientX, clientY) {
        const svgPoint = svg.createSVGPoint();
        svgPoint.x = clientX;
        svgPoint.y = clientY;
        return svgPoint.matrixTransform(svg.getScreenCTM().inverse());
    }

    // --- Drag Start ---
    diodePart.addEventListener('mousedown', (e) => {
        if (diodePlaced) return;
        isDragging = true;
        const svgCoords = getSvgCoords(e.clientX, e.clientY);
        const currentTransform = diodePart.getAttribute('transform');
        const translateMatch = currentTransform.match(/translate\(([^,]+),([^)]+)\)/);
        const currentX = translateMatch ? parseFloat(translateMatch[1]) : 0;
        const currentY = translateMatch ? parseFloat(translateMatch[2]) : 0;
        offset.x = svgCoords.x - currentX;
        offset.y = svgCoords.y - currentY;

        diodePart.style.cursor = 'grabbing';
        diodePart.classList.add('dragging'); // Add dragging class for potential styling
         svg.classList.add('dragging-diode'); // Add class to SVG for styling during drag
    });

    // --- Dragging ---
    svg.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        e.preventDefault(); // Prevent default drag behavior

        const svgCoords = getSvgCoords(e.clientX, e.clientY);
        let newX = svgCoords.x - offset.x;
        let newY = svgCoords.y - offset.y;

         // Optional: Constrain dragging area if needed
         // const svgRect = svg.getBoundingClientRect();
         // const diodeBBox = diodePart.getBBox(); // Get bounding box in local space
         // const diodeWidth = diodeBBox.width;
         // const diodeHeight = diodeBBox.height;
         // // Clamp newX and newY within SVG bounds (considering diode size)
         // newX = Math.max(diodeWidth / 2, Math.min(svgRect.width - diodeWidth / 2, newX));
         // newY = Math.max(diodeHeight / 2, Math.min(svgRect.height - diodeHeight / 2, newY));


        diodePart.setAttribute('transform', `translate(${newX}, ${newY}) rotate(${diodeOrientation})`);

         // Visual feedback for snapping proximity
        const placementCenter = {
             x: parseFloat(diodePlacementRect.getAttribute('x')) + parseFloat(diodePlacementRect.getAttribute('width')) / 2,
             y: parseFloat(diodePlacementRect.getAttribute('y')) + parseFloat(diodePlacementRect.getAttribute('height')) / 2
         };
        const dist = Math.sqrt(Math.pow(newX - placementCenter.x, 2) + Math.pow(newY - placementCenter.y, 2));
        const snapThreshold = 40; // pixels in SVG coordinates

        if (dist < snapThreshold) {
             diodePlacementRect.style.stroke = '#e63946'; // Highlight red when near snap
             diodePlacementHint.style.fill = '#e63946';
        } else {
             diodePlacementRect.style.stroke = '#457b9d'; // Back to blue
             diodePlacementHint.style.fill = '#555';
        }
    });

    // --- Drag End / Snap Logic ---
    svg.addEventListener('mouseup', (e) => {
        if (!isDragging) return;
        isDragging = false;
        diodePart.style.cursor = 'grab';
         diodePart.classList.remove('dragging');
         svg.classList.remove('dragging-diode');


        const placementCenter = {
            x: parseFloat(diodePlacementRect.getAttribute('x')) + parseFloat(diodePlacementRect.getAttribute('width')) / 2,
            y: parseFloat(diodePlacementRect.getAttribute('y')) + parseFloat(diodePlacementRect.getAttribute('height')) / 2
        };

        const currentTransform = diodePart.getAttribute('transform');
        const translateMatch = currentTransform.match(/translate\(([^,]+),([^)]+)\)/);
        const currentDiodeCenter = { x: parseFloat(translateMatch[1]), y: parseFloat(translateMatch[2]) };

        const snapThreshold = 40; // pixels in SVG coordinates
        const dist = Math.sqrt(Math.pow(currentDiodeCenter.x - placementCenter.x, 2) + Math.pow(currentDiodeCenter.y - placementCenter.y, 2));


        if (dist < snapThreshold) {
            // Snap the diode to the exact center of the placement area
            diodePart.setAttribute('transform', `translate(${diodePosition.x}, ${diodePosition.y}) rotate(${diodeOrientation})`);
            diodePlaced = true;
            diodePart.classList.add('diode-placed');
            diodePart.classList.remove('draggable');
            diodePart.style.cursor = 'default';
            diodePlacementRect.style.stroke = '#77cc77'; // Indicate success
             diodePlacementHint.style.opacity = 0; // Hide hint
            rotateDiodeBtn.style.display = 'inline-block'; // Show rotate button
            removeDiodeBtn.style.display = 'inline-block'; // Show remove button
            console.log("Diode snapped");
        } else {
             // Return diode to original position if not snapped (optional, or leave it where dropped)
             // For this example, let's leave it where dropped if not snapped to encourage placing it correctly
             diodePlaced = false;
             diodePart.classList.remove('diode-placed');
             diodePart.classList.add('draggable');
             diodePart.style.cursor = 'grab';
             diodePlacementRect.style.stroke = '#457b9d'; // Back to blue
             diodePlacementHint.style.opacity = 1; // Show hint again
             rotateDiodeBtn.style.display = 'none';
             removeDiodeBtn.style.display = 'none';
             console.log("Diode not snapped");
        }
        updateCircuitState();
    });

    // Prevent default drag behavior outside the SVG as well
     document.addEventListener('mousemove', (e) => {
        if (isDragging) e.preventDefault();
     });
     document.addEventListener('mouseup', (e) => {
        if (isDragging) {
             isDragging = false;
             diodePart.style.cursor = 'grab';
             diodePart.classList.remove('dragging');
             svg.classList.remove('dragging-diode');
             updateCircuitState(); // Update state even if not snapped
        }
     });


    // --- Circuit Simulation Logic ---

    function updateCircuitState() {
        const batteryVoltage = parseFloat(voltageSlider.value);
        const reversePolarity = polaritySwitch.checked;

        voltageValueSpan.textContent = `${batteryVoltage.toFixed(1)} V`;

        // Total effective voltage across the circuit elements (excluding battery internal resistance)
        let circuitVoltage = batteryVoltage;
        let current = 0;
        let diodeVoltage = 0; // Voltage drop across the diode
        let diodeResistance = Infinity; // Diode resistance (high when off)

        // Update battery +/- display based on polarity
        if (reversePolarity) {
             batteryPlus.setAttribute('y', '25'); // Swap positions
             batteryMinus.setAttribute('y', '-15');
             // Conceptual direction is reversed, but simulation uses magnitude for bias check
        } else {
             batteryPlus.setAttribute('y', '-15');
             batteryMinus.setAttribute('y', '25');
        }


        if (!diodePlaced) {
            // No diode: Simple R-LED circuit
            // Check LED forward voltage
            if (circuitVoltage > ledForwardVoltage) {
                current = (circuitVoltage - ledForwardVoltage) / (resistorValue + ledSeriesResistance);
            } else {
                current = 0;
            }
             diodeVoltage = 0; // No diode present
        } else {
            // Diode is placed
            // Determine diode bias based on battery polarity and diode orientation
            // Battery "positive" side is M 50,200 -> 150,200 -> 150,100
            // Diode Anode is the triangle side, Cathode is the bar side.
            // Default diode (0 deg): Anode on left (150,100 side), Cathode on right (450,100 side)
            // Rotated diode (180 deg): Anode on right (450,100 side), Cathode on left (150,100 side)

            let isDiodeForwardBiased = false;
            // Assuming current flows + to -, so from battery.plus (y=-15, rotated 90deg -> + is on left path section)
            // Path goes from 50,200 -> 150,200 -> 150,100 (left of diode spot) -> 450,100 (right of diode spot) -> ... -> 50,200
            // Battery '+' is at (50, ~220) -> current tries to flow CCW in the diagram
            // Diode path is 150,100 to 450,100

            const diodeAnodeSide = diodeOrientation === 0 ? 'left' : 'right'; // left=150,100, right=450,100
            const circuitPositiveSide = reversePolarity ? 'right' : 'left'; // 'left' is the battery '+' end of diode path

             if (diodeAnodeSide === circuitPositiveSide) {
                 isDiodeForwardBiased = true; // Anode connected to positive side of the path
             } else {
                 isDiodeForwardBiased = false; // Anode connected to negative side (reverse biased)
             }

             // Special case: If battery is reversed, the "positive" side of the path is now the other end.
             // Battery '+' in reversed state is at (50, ~280), current tries to flow CW in the diagram.
             // Diode path is 150,100 to 450,100.
             // If reversePolarity is true: current flows from (550,300) -> (550,200) -> (450,200) -> (450,100) -> (150,100) -> ...
             // So, 450,100 is the more positive potential side of the diode path when battery is reversed.

            isDiodeForwardBiased = false;
             if (!reversePolarity && diodeOrientation === 0) { // Normal battery, Diode normal (A to C towards 450,100)
                 isDiodeForwardBiased = true; // + -> Anode (150,100) to Cathode (450,100) -> -
             } else if (reversePolarity && diodeOrientation === 180) { // Reversed battery, Diode reversed (C to A towards 150,100)
                 isDiodeForwardBiased = true; // + -> Anode (450,100) to Cathode (150,100) -> -
             }
             // In other cases, diode is reverse biased

            if (isDiodeForwardBiased) {
                if (circuitVoltage > diodeThresholdVoltage) {
                    // Diode conducting (approximation)
                    diodeVoltage = diodeThresholdVoltage; // Constant voltage drop
                    // Calculate current based on voltage remaining for R and LED
                    let voltageAcrossRL = circuitVoltage - diodeVoltage;
                    if (voltageAcrossRL > ledForwardVoltage) {
                        current = voltageAcrossRL / (resistorValue + ledSeriesResistance);
                    } else {
                        current = 0; // Not enough voltage left for LED
                    }
                } else {
                    // Forward biased but below threshold
                    diodeVoltage = circuitVoltage; // Voltage across diode equals supply voltage
                    current = 0;
                }
            } else {
                // Diode is reverse biased
                diodeVoltage = -circuitVoltage; // Voltage across diode is approx supply voltage (negative)
                current = 0; // Ignore small leakage current
            }
        }

        // Ensure current is not negative due to floating point inaccuracies
        current = Math.max(0, current);

        // Update readings
        diodeVoltageSpan.textContent = `${diodeVoltage.toFixed(1)} V`;
        circuitCurrentSpan.textContent = `${(current * 1000).toFixed(2)} mA`; // Display in mA

        // Update LED state and glow
        const minVisibleCurrent = 0.008; // mA, minimum current for LED to be visibly on
        const maxCurrentForFullBrightness = 0.020; // mA, e.g., 20mA

        if (current > minVisibleCurrent) {
            const brightness = Math.min(1, (current - minVisibleCurrent) / (maxCurrentForFullBrightness - minVisibleCurrent));
             led.style.opacity = 1; // Make LED visible
            ledGlow.style.opacity = brightness * 0.6; // Adjust glow intensity
            ledGlow.style.animation = 'led-pulse 1s infinite alternate'; // Add pulse animation
             led.style.filter = `drop-shadow(0 0 ${brightness * 8}px yellow)`; // Add visual glow effect
             // Change path color to indicate current flow
             pathElements.forEach(p => p.style.stroke = '#e63946'); // Red for current
        } else {
            led.style.opacity = 0.3; // Dim LED when off
             ledGlow.style.opacity = 0; // Hide glow
             ledGlow.style.animation = 'none'; // Stop pulse animation
             led.style.filter = 'none'; // Remove glow effect
             pathElements.forEach(p => p.style.stroke = '#333'); // Black when no current
        }

        // Update current flow animation visibility and direction
        // Get the actual path data string for the current flow
        // Need to connect paths in the correct order based on battery polarity
         let flowPathD = '';
         if (!reversePolarity) { // Current flows from + to - (CCW in diagram)
              // Path order: path8 (bottom left up) -> path1 -> path2 -> path3 (diode) -> path4 -> path5 -> path6 -> path7 (bottom right left) -> path8
              flowPathD = `${paths.path8.getAttribute('d')} ${paths.path1.getAttribute('d')} ${paths.path2.getAttribute('d')} ${paths.path3.getAttribute('d')} ${paths.path4.getAttribute('d')} ${paths.path5.getAttribute('d')} ${paths.path6.getAttribute('d')} ${paths.path7.getAttribute('d')}`;
              currentDots.forEach(dot => dot.classList.remove('reverse'));
         } else { // Current flows from - to + (CW in diagram)
              // Path order: path8 (bottom left up) -> path7 (bottom left right) -> path6 -> path5 -> path4 -> path3 (diode) -> path2 -> path1 -> path8 (back where we started)
              // Wait, the path direction needs to be reversed for CW flow
              // Easiest way: build the string in reverse order of segments and use reverse animation
              // Correct segment order for CW flow: path7 -> path6 -> path5 -> path4 -> path3 -> path2 -> path1 -> path8
             // Reversing the path D string itself is complex. Use reverse animation direction.
              flowPathD = `${paths.path8.getAttribute('d')} ${paths.path1.getAttribute('d')} ${paths.path2.getAttribute('d')} ${paths.path3.getAttribute('d')} ${paths.path4.getAttribute('d')} ${paths.path5.getAttribute('d')} ${paths.path6.getAttribute('d')} ${paths.path7.getAttribute('d')}`;
             currentDots.forEach(dot => dot.classList.add('reverse'));

         }


        if (current > minVisibleCurrent) {
             currentDots.forEach(dot => {
                 dot.style.display = 'block';
                 // Set motion path
                 dot.style.motionPath = `path('${flowPathD}')`;
                 dot.style.webkitMotionPath = `path('${flowPathD}')`; // For compatibility
             });
        } else {
             currentDots.forEach(dot => dot.style.display = 'none');
        }
    }

     // --- Event Listeners ---
    voltageSlider.addEventListener('input', updateCircuitState);
    polaritySwitch.addEventListener('change', updateCircuitState);

    rotateDiodeBtn.addEventListener('click', () => {
        if (diodePlaced) {
            diodeOrientation = diodeOrientation === 0 ? 180 : 0;
             // Update transform for the diode group at its fixed position
            diodePart.setAttribute('transform', `translate(${diodePosition.x}, ${diodePosition.y}) rotate(${diodeOrientation})`);
            updateCircuitState();
        }
    });

     removeDiodeBtn.addEventListener('click', () => {
         if (diodePlaced) {
             diodePlaced = false;
             diodeOrientation = 0; // Reset orientation when removed
             // Move diode back to its initial position (or near it)
             diodePart.setAttribute('transform', `translate(50, 50) rotate(0)`);
             diodePart.classList.remove('diode-placed');
             diodePart.classList.add('draggable');
             diodePart.style.cursor = 'grab';
             diodePlacementRect.style.stroke = '#457b9d'; // Reset placement area border
             diodePlacementHint.style.opacity = 1; // Show hint
             rotateDiodeBtn.style.display = 'none'; // Hide buttons
             removeDiodeBtn.style.display = 'none';
             updateCircuitState(); // Update circuit (now without diode)
             console.log("Diode removed");
         }
     });


    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר / הסתר הסבר';
    });


    // --- Initial state ---
    updateCircuitState(); // Set initial state based on default controls

     // CSS Animation for LED pulse (defined in JS as it's toggled)
     const styleSheet = document.styleSheets[0];
     const pulseKeyframes = `
        @keyframes led-pulse {
            0% { transform: scale(1); opacity: 0.6; }
            100% { transform: scale(1.1); opacity: 1; }
        }
     `;
     styleSheet.insertRule(pulseKeyframes, styleSheet.cssRules.length);


</script>