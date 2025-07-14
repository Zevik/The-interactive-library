---
title: "גלאי מתכות: מבט אל הסודות החבויים"
english_slug: metal-detectors-deciphering-the-secret
category: "פיזיקה"
tags: ["גלאי מתכות", "השראה אלקטרומגנטית", "זרמי מערבולת", "שדות מגנטיים", "אלקטרומגנטיות", "פיזיקה ניסויית"]
---
<div class="intro-text">
<h1>גלאי מתכות: מבט אל הסודות החבויים</h1>

<p>איך קסם ההשראה האלקטרומגנטית מאפשר לנו "לראות" מתכת דרך האדמה או קירות? הצטרפו אלינו למסע ויזואלי אל תוך העולם הנסתר של גלאי המתכות, גלו מה קורה כששדה מגנטי פוגש עצם מתכתי, וחוו בעצמכם איך מוצאים אוצרות (או לפחות סיכות ראש!).</p>
</div>

<div id="simulation-container">
    <svg id="detector-sim" width="600" height="350" viewBox="0 0 600 350">
        <!-- Sky -->
        <rect x="0" y="0" width="600" height="200" fill="#87CEEB" />
        <!-- Ground -->
        <rect x="0" y="200" width="600" height="150" fill="#A0522D" />
         <!-- Subtle ground texture/lines -->
         <g id="ground-texture">
             <line x1="0" y1="210" x2="600" y2="210" stroke="#B0623D" stroke-width="1" opacity="0.3"></line>
             <line x1="0" y1="230" x2="600" y2="230" stroke="#B0623D" stroke-width="1" opacity="0.3"></line>
             <line x1="0" y1="250" x2="600" y2="250" stroke="#B0623D" stroke-width="1" opacity="0.3"></line>
             <line x1="0" y1="270" x2="600" y2="270" stroke="#B0623D" stroke-width="1" opacity="0.3"></line>
         </g>


        <!-- Hidden Objects Layer (underground) -->
        <g id="object-container">
             <!-- Object graphics will be added here by JS -->
             <!-- Objects are visually below the ground rect in z-order by being before it -->
        </g>

        <!-- Detector Head -->
        <g id="detector-head" transform="translate(250, 100)">
            <rect x="0" y="0" width="100" height="25" fill="#B0BEC5" rx="5" ry="5" stroke="#546E7A" stroke-width="2" />
            <rect id="transmitter-coil-graphic" x="8" y="5" width="35" height="15" fill="#42A5F5" rx="3" ry="3" /> <!-- Blue -->
            <rect id="receiver-coil-graphic" x="57" y="5" width="35" height="15" fill="#EF5350" rx="3" ry="3" /> <!-- Red -->
             <text x="25" y="16" text-anchor="middle" fill="white" font-size="9" font-weight="bold">משדר</text>
             <text x="75" y="16" text-anchor="middle" fill="white" font-size="9" font-weight="bold">קולט</text>
             <!-- Indicator light -->
             <circle id="detection-indicator" cx="50" cy="-5" r="5" fill="#FFEB3B" opacity="0.2"/> <!-- Yellow, low opacity initially -->
        </g>

         <!-- Magnetic Field Lines (Transmitter - Animated) -->
        <g id="tx-field">
            <!-- Lines/shapes added and animated by JS -->
        </g>

        <!-- Eddy Currents (Animated) -->
        <g id="eddy-currents">
            <!-- Eddy current loops added and animated by JS -->
        </g>

         <!-- Magnetic Field Lines (Eddy Currents - Animated) -->
         <g id="eddy-field">
            <!-- Lines/shapes added and animated by JS -->
        </g>

        <!-- Detected Signal Indicator -->
        <rect x="400" y="10" width="180" height="30" fill="#ECEFF1" rx="5" ry="5" stroke="#CFD8DC" stroke-width="1"/>
        <text x="490" y="28" text-anchor="middle" font-size="16" fill="#37474F">אות מזוהה:</text>
        <rect x="405" y="45" width="170" height="15" fill="#B0BEC5" rx="3" ry="3"/> <!-- Background bar -->
        <rect id="signal-bar" x="405" y="45" width="0" height="15" fill="#66BB6A" rx="3" ry="3"/> <!-- Signal bar -->
         <text id="signal-value-text" x="490" y="60" text-anchor="middle" font-size="12" fill="#37474F"></text>
        <text id="detection-text" x="490" y="80" text-anchor="middle" font-size="18" fill="#D32F2F" font-weight="bold" opacity="0">נמצא!</text>

    </svg>

    <div id="controls">
        <div class="control-group">
             <label for="detector-pos">הזז גלאי:</label>
             <input type="range" id="detector-pos" min="0" max="500" value="250">
        </div>
        <div class="control-group">
             <label for="object-type">עצם חבוי:</label>
             <select id="object-type">
                 <option value="coin">מטבע (נחושת/פליז)</option>
                 <option value="iron-ring">טבעת ברזל (מגנטי)</option>
                 <option value="aluminum-foil">רדיד אלומיניום (מוליך מאד)</option>
                  <option value="none">כלום</option>
             </select>
        </div>
         <div class="control-group">
             <label for="object-size">גודל:</label>
              <input type="range" id="object-size" min="0.5" max="2.5" value="1" step="0.1">
         </div>
          <div class="control-group">
             <label for="object-depth">עומק:</label>
              <input type="range" id="object-depth" min="10" max="80" value="30" step="5">
         </div>
    </div>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        line-height: 1.6;
        color: #333;
    }

    .intro-text {
        text-align: center;
        margin-bottom: 30px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
     .intro-text h1 {
        color: #2C3E50;
        margin-bottom: 10px;
    }
    .intro-text p {
        color: #555;
        font-size: 18px;
    }

    #simulation-container {
        direction: rtl;
        text-align: center;
        margin: 20px auto;
        border: 1px solid #B0BEC5;
        border-radius: 8px;
        padding: 15px;
        background: linear-gradient(to bottom, #E0F2F7, #B2EBF2); /* Light gradient */
        max-width: 650px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    #detector-sim {
        border: 1px solid #CFD8DC;
        background-color: #E0F2F7; /* Sky background */
        border-radius: 5px;
    }

    /* Ground */
    #detector-sim rect[fill="#A0522D"] {
        fill: #A0522D; /* Soil color */
    }
     #ground-texture line {
        stroke: #B0623D;
        stroke-width: 1;
        opacity: 0.3;
     }


    /* Detector Head */
    #detector-head rect {
        fill: #B0BEC5;
        stroke: #546E7A;
    }
    #transmitter-coil-graphic {
        fill: #42A5F5; /* Blue */
    }
    #receiver-coil-graphic {
        fill: #EF5350; /* Red */
    }
    #detection-indicator {
        transition: opacity 0.3s ease-in-out;
    }

    /* Field Lines & Eddy Currents */
     #tx-field line {
        stroke: #42A5F5; /* Blue */
        stroke-width: 2;
        opacity: 0.8;
        /* Simple animation placeholder */
        animation: tx-pulse 1s infinite linear;
     }
      /* Optional: Different animation delay for lines */
      #tx-field line:nth-child(odd) { animation-delay: 0.2s; }
      #tx-field line:nth-child(even) { animation-delay: 0s; }


     #eddy-currents circle {
        fill: none;
        stroke: #FF9800; /* Orange */
        stroke-width: 3;
        opacity: 0.9;
        animation: eddy-pulse 1s infinite linear;
     }

     #eddy-field line {
        stroke: #8BC34A; /* Green */
        stroke-width: 2;
        opacity: 0.8;
         /* Simple animation placeholder */
        animation: eddy-field-pulse 1s infinite linear;
     }
     /* Optional: Different animation delay for lines */
      #eddy-field line:nth-child(odd) { animation-delay: 0.2s; }
      #eddy-field line:nth-child(even) { animation-delay: 0s; }


    /* Object Styling */
    #object-container circle, #object-container rect {
        fill: #78909C; /* Metallic gray */
        stroke: #263238;
        stroke-width: 2;
         opacity: 0.8; /* Initially slightly transparent */
         transition: opacity 0.5s ease-in-out;
    }

    /* Signal Indicator */
    #signal-bar {
        transition: width 0.2s ease-out;
    }
     #detection-text {
         transition: opacity 0.3s ease-in-out;
     }


    /* Controls */
    #controls {
        margin-top: 20px;
        padding: 15px;
        background-color: #EFEBE9; /* Light brown */
        border-radius: 8px;
        text-align: right; /* Align labels to the right */
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Center control groups */
        gap: 15px; /* Space between control groups */
    }
    .control-group {
        display: flex;
        align-items: center; /* Vertically align items */
        gap: 5px; /* Space between label and input */
        flex-direction: row-reverse; /* Put label on the right for RTL */
    }
     #controls label {
        font-weight: bold;
        color: #4E342E; /* Dark brown */
        white-space: nowrap; /* Prevent label wrapping */
    }
     #controls input[type="range"], #controls select {
         flex-grow: 1; /* Allow input to take available space */
         max-width: 180px; /* Limit max width */
     }
    #controls input[type="range"] {
        direction: ltr; /* Sliders are typically LTR */
    }


    /* Explanation Button */
    #explanation-button {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        font-size: 17px;
        cursor: pointer;
        background-color: #0288D1; /* Light blue */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    #explanation-button:hover {
        background-color: #0277BD; /* Darker blue */
    }

    /* Explanation */
    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #B0BEC5;
        border-radius: 8px;
        background-color: #F5F5F5; /* Light gray */
        text-align: right;
        direction: rtl;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
     #explanation h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #2C3E50;
    }
    #explanation p, #explanation ul {
        margin-bottom: 15px;
        line-height: 1.7;
        color: #444;
    }
     #explanation strong {
        color: #5D4037; /* Brownish */
     }
     #explanation ul {
        padding-right: 20px; /* Indent list for RTL */
     }
     #explanation li {
         margin-bottom: 8px;
     }

     /* Animations */
    @keyframes tx-pulse {
        0% { opacity: 0.8; stroke-width: 2; }
        50% { opacity: 1; stroke-width: 3; }
        100% { opacity: 0.8; stroke-width: 2; }
    }
    @keyframes eddy-pulse {
        0% { stroke-dasharray: 0, 100; stroke-dashoffset: 0; opacity: 0.9; }
        50% { stroke-dasharray: 100, 0; stroke-dashoffset: 0; opacity: 1; }
         50.1% { stroke-dasharray: 100, 0; stroke-dashoffset: 100; opacity: 1; } /* Reset for next cycle */
        100% { stroke-dasharray: 0, 100; stroke-dashoffset: 100; opacity: 0.9; }
    }
     @keyframes eddy-field-pulse {
        0% { opacity: 0.8; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.05); }
        100% { opacity: 0.8; transform: scale(1); }
    }

</style>

<button id="explanation-button">הצג הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>גלאי מתכות בפעולה: מסע לעומק האדמה (בלי ללכלך את הידיים)</h2>

    <p>איך המכשיר הזה יודע לגלות מטבע קטן מתחת לערימת עפר? הסוד טמון בעולם המרתק של ה<strong>אלקטרומגנטיות</strong> ובעיקרון פיזיקלי מדהים בשם <strong>השראה אלקטרומגנטית</strong>.</p>

    <p><strong>מה יש שם בפנים?</strong><br>
    ראש הגלאי, אותו סליל שמזיזים מעל הקרקע, מכיל בדרך כלל שני סלילי נחושת (או יותר). אחד הוא ה<strong>סליל המשדר (Transmit Coil)</strong> והשני הוא ה<strong>סליל הקולט (Receive Coil)</strong>.</p>

    <p><strong>השלב הראשון: יצירת השדה המגנטי</strong><br>
    האלקטרוניקה שבגלאי שולחת זרם חשמלי מיוחד, שמשנה את הכיוון שלו הלוך ושוב (זרם חילופין), אל הסליל המשדר. זרם זה יוצר סביבו שדה מגנטי. מכיוון שהזרם מתחלף כל הזמן, גם השדה המגנטי שהוא יוצר משתנה בהתמדה – הוא גדל, קטן, מחליף כיוון, וחוזר חלילה. השדה המשתנה הזה "נוסע" אל תוך הקרקע.</p>

    <p><strong>השלב השני: מפגש מרתק עם מתכת - זרמי מערבולת!</strong><br>
    כששדה מגנטי משתנה פוגש חתיכת מתכת (שהיא חומר שיכול להוליך חשמל), קורה דבר מעניין: השדה "משרה" זרמים חשמליים בתוך המתכת עצמה! הזרמים הללו נעים במסלולים מעגליים או מערבולתיים בתוך גוף המתכת, ולכן הם נקראים <strong>זרמי מערבולת (Eddy Currents)</strong>. ככל שהמתכת מוליכה חשמל טוב יותר (כמו נחושת, כסף, זהב), וכל שהשדה המגנטי המשתנה חזק יותר, כך זרמי המערבולת יהיו חזקים יותר.</p>

    <p><strong>השלב השלישי: השדה המגנטי של זרמי המערבולת</strong><br>
    כמו כל זרם חשמלי, גם זרמי המערבולת האלה יוצרים שדה מגנטי סביבם! ופה מגיע הטוויסט המרכזי (על פי חוק לנץ): השדה המגנטי החדש שנוצר על ידי זרמי המערבולת הוא בכיוון שמתנגד (באופן חלקי או מלא) לשינוי בשדה המגנטי המקורי שיצר אותם. למעשה, הוא "דוחף" בחזרה נגד השדה המגנטי מהמשדר.</p>

    <p><strong>השלב הרביעי: הקליטה והאזעקה</strong><br>
    עכשיו נכנס לתמונה הסליל השני – ה<strong>סליל הקולט</strong>. הוא ממוקם כך שיקלוט את השדה המגנטי הכולל שחוזר אליו. כשיש מתכת באזור, הסליל הקולט מרגיש לא רק את השדה המקורי של המשדר, אלא גם את השדה המגנטי הנוסף שנוצר על ידי זרמי המערבולת במתכת. השדה הנוסף הזה משנה את השדה הכולל שמגיע לקולט (לרוב מחליש אותו או משנה את המאפיינים שלו). השינוי הזה בשדה המגנטי דרך הסליל הקולט "משרה" בו מתח חשמלי קטן (שוב, השראה אלקטרומגנטית!). האלקטרוניקה של הגלאי רגישה מאוד למתח הזעיר הזה. כשהיא מזהה מתח בעוצמה מסוימת, זה הסימן – <strong>נמצאה מתכת!</strong> ואז שומעים את הצפצוף המיוחל.</p>

     <p><strong>למה לא כל מתכת מגיבה באותה מידה?</strong><br>
     התגובה של גלאי המתכות מושפעת מאוד מתכונות המתכת:
     <ul>
         <li><strong>מוליכות חשמלית:</strong> מתכות שמוליכות חשמל טוב מאוד (כמו זהב, כסף, נחושת) יוצרות זרמי מערבולת חזקים במיוחד, ולכן קלות מאוד לגילוי. ברזל פחות מוליך, אבל...</li>
         <li><strong>חדירות מגנטית (פֵּרְמֵאַבִּילִיוּת):</strong> חומרים כמו ברזל, ניקל, קובלט מתמגנטים בקלות. תכונה זו מוסיפה אינטראקציה נוספת עם השדה המגנטי, ולרוב מגבירה את התגובה, אם כי בצורה מעט שונה ממוליכות בלבד. גלאים מתקדמים יכולים אפילו לנתח את סוג התגובה (מוליכות מול מגנטיות) כדי לתת הערכה על סוג המתכת.</li>
         <li><strong>גודל וצורה:</strong> עצם גדול יותר או כזה עם שטח פנים רחב יפתח זרמי מערבולת משמעותיים יותר.</li>
         <li><strong>עומק:</strong> ככל שהעצם עמוק יותר, השדות המגנטיים (הן מהמשדר והן מהמתכת) נחלשים משמעותית, מה שמקשה על האיתור.</li>
     </ul>
     הסימולציה מציגה באופן פשטני חלק מהאינטראקציות הללו כדי להמחיש את העיקרון הבסיסי.</p>

     <p><strong>איפה פוגשים גלאי מתכות בחיי היומיום?</strong><br>
     מאיתור מטבעות אבודים בחוף הים, דרך בדיקות ביטחוניות בשדות תעופה, איתור צנרת בקירות, ועד עזרה לארכיאולוגים - גלאי המתכות הוא כלי מדהים שמגשר בין פיזיקה לעולם המעשי, ומאפשר לנו לגלות דברים נסתרים מתחת לפני השטח!</p>

</div>

<script>
    const sim = document.getElementById('detector-sim');
    const detectorHead = document.getElementById('detector-head');
    const detectorPosSlider = document.getElementById('detector-pos');
    const objectTypeSelect = document.getElementById('object-type');
    const objectSizeSlider = document.getElementById('object-size');
    const objectDepthSlider = document.getElementById('object-depth'); // New depth slider
    const objectContainer = document.getElementById('object-container');
    const txFieldGroup = document.getElementById('tx-field');
    const eddyCurrentsGroup = document.getElementById('eddy-currents');
    const eddyFieldGroup = document.getElementById('eddy-field');
    const signalBar = document.getElementById('signal-bar');
    const signalValueText = document.getElementById('signal-value-text'); // New text element
    const detectionText = document.getElementById('detection-text'); // New detection text
    const detectionIndicator = document.getElementById('detection-indicator'); // New indicator light
    const explanationDiv = document.getElementById('explanation');
    const explanationButton = document.getElementById('explanation-button');

    const groundLevelY = 200; // Y coordinate of the top of the ground
    const detectorHeadHeight = 25; // Height of the detector graphic
    const detectorY = 100; // Fixed Y position of the detector head

    let currentObjectType = 'coin';
    let currentObjectSizeFactor = 1;
    let currentObjectDepth = parseFloat(objectDepthSlider.value); // Get initial depth
    let objectElement = null; // SVG element representing the object

    // Object position (fixed horizontal position for the hidden object)
    const objectX = 300; // Center the object horizontally

    // Define object properties (conductivity, permeabilityFactor, baseSize)
    const objectProperties = {
        'coin': { conductivity: 0.8, permeabilityFactor: 1.1, baseSize: 20, shape: 'circle' }, // High conductivity, slightly magnetic
        'iron-ring': { conductivity: 0.3, permeabilityFactor: 8, baseSize: 30, shape: 'rect' }, // Lower conductivity, strongly magnetic
        'aluminum-foil': { conductivity: 0.95, permeabilityFactor: 1.05, baseSize: 40, shape: 'rect' }, // Very high conductivity, very slightly magnetic
        'none': { conductivity: 0, permeabilityFactor: 1, baseSize: 0, shape: 'none' } // No object
    };

    const maxSignalThreshold = 10; // Adjust this based on simulation tuning
    const detectionThreshold = 3; // Signal level to trigger visual/text indicator

    function createObjectGraphic(type, sizeFactor, depth) {
        // Remove previous object
        while (objectContainer.firstChild) {
            objectContainer.removeChild(objectContainer.firstChild);
        }

        const props = objectProperties[type];
        if (type === 'none' || !props || props.baseSize === 0) {
            objectElement = null; // Ensure no object reference
            return;
        }

        const size = props.baseSize * sizeFactor;
        const objectY = groundLevelY + depth; // Object Y position depends on depth

        let obj;
        if (props.shape === 'circle') {
            obj = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            obj.setAttribute('cx', objectX);
            obj.setAttribute('cy', objectY);
            obj.setAttribute('r', size / 2);
        } else { // 'rect'
            obj = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            obj.setAttribute('x', objectX - size / 2);
            obj.setAttribute('y', objectY - size / 4); // Rectangular shape, wider
            obj.setAttribute('width', size);
            obj.setAttribute('height', size / 2);
        }

        // Set common attributes
        obj.setAttribute('fill', '#78909C'); // Metallic gray
        obj.setAttribute('stroke', '#263238');
        obj.setAttribute('stroke-width', 2);
        obj.setAttribute('opacity', 0.8); // Slightly transparent initially

        objectContainer.appendChild(obj);
        objectElement = obj; // Store reference
    }

    // Animation state and timing
    let animationFrameId = null;
    let lastUpdateTime = 0;
    const animationSpeed = 0.01; // Controls speed of visual pulsing effects

    function animateSimulation(currentTime) {
        if (!lastUpdateTime) lastUpdateTime = currentTime;
        const elapsed = currentTime - lastUpdateTime;
        lastUpdateTime = currentTime;

        // Update animations here if using JS for that
        // For now, relying on CSS animations for simplicity as requested by structure constraint

        // Re-request animation frame
        animationFrameId = requestAnimationFrame(animateSimulation);
    }

    function updateSimulation() {
        const detectorX = parseFloat(detectorPosSlider.value);
        detectorHead.setAttribute('transform', `translate(${detectorX}, ${detectorY})`);

        // Clear previous field lines and eddy currents graphics
        // Note: Recreating elements is simpler than updating paths/attributes drastically,
        // but less performant for very complex animations. For this scale, it's acceptable.
        while (txFieldGroup.firstChild) txFieldGroup.removeChild(txFieldGroup.firstChild);
        while (eddyCurrentsGroup.firstChild) eddyCurrentsGroup.removeChild(eddyCurrentsGroup.firstChild);
        while (eddyFieldGroup.firstChild) eddyFieldGroup.removeChild(eddyFieldGroup.firstChild);

        const detectorCenterX = detectorX + 50; // Center X of the detector head graphic
        const detectorBottomY = detectorY + detectorHeadHeight; // Bottom Y of the detector head graphic
        const objectY = groundLevelY + currentObjectDepth; // Y position of the object center

        let detectedSignal = 0;
        const props = objectProperties[currentObjectType];
        const objectIsPresent = (currentObjectType !== 'none' && objectElement);

        // Visualize Transmitter Field (More dynamic lines)
        const txCoilCenterX = detectorX + 25;
        const txCoilCenterY = detectorY + 15;
        const numTxLines = 10;
        const txLineLength = 180;
        for (let i = 0; i < numTxLines; i++) {
             // Angles spreading downwards, maybe slightly outwards
            const angle = (i / numTxLines - 0.5) * 0.8 * Math.PI + Math.PI / 2; // Range from ~+45 to +135 deg
            const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
            line.setAttribute('x1', txCoilCenterX);
            line.setAttribute('y1', txCoilCenterY);
            line.setAttribute('x2', txCoilCenterX + txLineLength * Math.cos(angle));
            line.setAttribute('y2', txCoilCenterY + txLineLength * Math.sin(angle));
            txFieldGroup.appendChild(line);
        }


        if (objectIsPresent) {
             // Calculate effective distance from detector center to object center
            const dx = Math.abs(detectorCenterX - objectX);
            const dy = Math.abs(detectorBottomY - objectY); // Vertical distance from detector bottom to object
            const distance = Math.sqrt(dx*dx + dy*dy);

            // Simulate interaction based on distance, size, and properties
            // Inverse square law approximation for field strength reaching object
            const fieldStrengthAtObject = Math.max(0, 1 - distance / 150); // Scales from 1 (close) to 0 (far)

            // Eddy current strength depends on field strength, material properties, and size
            const eddyCurrentStrength = fieldStrengthAtObject * props.conductivity * (props.baseSize * currentObjectSizeFactor / 20) * 0.8; // Conductivity & Size scale

            // Add effect of permeability for magnetic materials
            // This is a simplification: magnetic materials boost/distort the field differently
            const magneticEffect = (props.permeabilityFactor - 1) * fieldStrengthAtObject * (props.baseSize * currentObjectSizeFactor / 30) * 0.5; // Permeability & Size scale

            const totalInteractionStrength = eddyCurrentStrength + magneticEffect;


            if (totalInteractionStrength > 0.05) { // Only visualize/calculate signal if interaction is significant
                 // --- Visualize Eddy Currents (Animated) ---
                 const numEddyLoops = Math.min(7, Math.ceil(totalInteractionStrength * 5)); // More loops for stronger current
                for (let i = 0; i < numEddyLoops; i++) {
                    // Make inner loops smaller, outer larger
                    const r = (i + 1) * (props.baseSize * currentObjectSizeFactor / (numEddyLoops + 2)) * 0.8;
                    const eddyCircle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
                    eddyCircle.setAttribute('cx', objectX);
                    eddyCircle.setAttribute('cy', objectY);
                    eddyCircle.setAttribute('r', r);
                    // Set CSS animation delay for a wave effect
                    eddyCircle.style.animationDelay = `${i * 0.08}s`;
                    eddyCurrentsGroup.appendChild(eddyCircle);
                }

                 // --- Visualize Eddy Current Field (Animated) ---
                 // Lines originating from object towards receiver coil
                 const rxCoilCenterX = detectorX + 75;
                 const rxCoilCenterY = detectorY + 15;
                 const numEddyFieldLines = Math.min(7, Math.ceil(totalInteractionStrength * 5));
                 for (let i = 0; i < numEddyFieldLines; i++) {
                    // Lines pointing upwards towards the receiver coil
                    const angle = (i / numEddyFieldLines - 0.5) * 0.6 * Math.PI - Math.PI / 2; // Range around -90 deg
                    const lineLength = 120 * (totalInteractionStrength / 5); // Length scales with strength, capped
                     const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                    line.setAttribute('x1', objectX);
                    line.setAttribute('y1', objectY);
                    line.setAttribute('x2', objectX + lineLength * Math.cos(angle));
                    line.setAttribute('y2', objectY + lineLength * Math.sin(angle));
                    // Set CSS animation delay for a wave effect
                    line.style.animationDelay = `${i * 0.08}s`;
                    eddyFieldGroup.appendChild(line);
                 }

                 // --- Calculate Detected Signal ---
                 // Signal strength depends on totalInteractionStrength and distance to RX coil
                 const distToObjectRx = Math.sqrt(Math.pow(rxCoilCenterX - objectX, 2) + Math.pow(rxCoilCenterY - objectY, 2));
                 const signalFalloffToRx = Math.max(0, 1 - distToObjectRx / 100); // Distance from object to RX matters

                 // Simple model: Signal is proportional to interaction strength and how much of the eddy field reaches the RX coil
                 detectedSignal = totalInteractionStrength * signalFalloffToRx * 3; // Scale factor

                // Adjust object graphic opacity based on proximity to detector head
                const opacity = Math.min(1, 0.8 + Math.max(0, 1 - Math.abs(detectorCenterX - objectX) / 150) * Math.max(0, 1 - Math.abs(detectorBottomY - objectY) / 80) * 0.5); // More opaque when closer
                objectElement.setAttribute('opacity', opacity);


            } else {
                 // Interaction too weak, object is barely or not detected
                 if (objectElement) objectElement.setAttribute('opacity', 0.8); // Reset opacity if no significant interaction
            }
        } else {
             // No object selected, ensure graphics are clear and signal is 0
             detectedSignal = 0;
        }


        // Clamp signal and update signal bar/text
        detectedSignal = Math.min(maxSignalThreshold, detectedSignal);
        const signalWidth = (detectedSignal / maxSignalThreshold) * 170; // Scale to bar width (170)
        signalBar.setAttribute('width', signalWidth);

        // Update signal value text (optional, for debugging/clarity)
        signalValueText.textContent = `${detectedSignal.toFixed(1)}`; // Show signal value

        // Update detection indicator and text
        if (detectedSignal >= detectionThreshold) {
            detectionText.setAttribute('opacity', 1);
            detectionIndicator.setAttribute('fill', '#FFEB3B'); // Yellow
            detectionIndicator.setAttribute('opacity', 1); // Solid
            // Trigger a pulse animation visually via CSS class or direct manipulation
            // Example: Add/remove a class that has a pulse animation
             // detectionIndicator.classList.add('pulse'); // Needs CSS pulse class definition
             // For simplicity, direct manipulation (blink) could also work
        } else {
            detectionText.setAttribute('opacity', 0);
             detectionIndicator.setAttribute('fill', '#FFEB3B'); // Yellow
             detectionIndicator.setAttribute('opacity', 0.2); // Faded
             // detectionIndicator.classList.remove('pulse');
        }

         // Adjust signal bar color based on signal strength
         if (detectedSignal < detectionThreshold / 2) {
            signalBar.setAttribute('fill', '#FFD700'); // Yellow
         } else if (detectedSignal < detectionThreshold) {
             signalBar.setAttribute('fill', '#FFA500'); // Orange
         }
         else {
            signalBar.setAttribute('fill', '#66BB6A'); // Green
         }


    }

    // Initial setup
    createObjectGraphic(currentObjectType, currentObjectSizeFactor, currentObjectDepth);
    updateSimulation(); // Perform initial calculation and drawing
    // animationFrameId = requestAnimationFrame(animateSimulation); // Start animation loop (if needed for JS animations)

    // Event listeners for controls
    detectorPosSlider.addEventListener('input', updateSimulation);

    objectTypeSelect.addEventListener('change', (event) => {
        currentObjectType = event.target.value;
        createObjectGraphic(currentObjectType, currentObjectSizeFactor, currentObjectDepth); // Recreate object graphic
        updateSimulation();
    });

    objectSizeSlider.addEventListener('input', (event) => {
        currentObjectSizeFactor = parseFloat(event.target.value);
        createObjectGraphic(currentObjectType, currentObjectSizeFactor, currentObjectDepth); // Recreate graphic with new size
        updateSimulation();
    });

    objectDepthSlider.addEventListener('input', (event) => {
        currentObjectDepth = parseFloat(event.target.value);
        createObjectGraphic(currentObjectType, currentObjectSizeFactor, currentObjectDepth); // Recreate graphic with new depth
        updateSimulation();
    });


    // Explanation button toggle
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
    });

     // Clean up animation frame on unload (optional but good practice)
     window.addEventListener('beforeunload', () => {
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
         }
     });


</script>
```