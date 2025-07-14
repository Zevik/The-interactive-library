---
title: "רובוטים רכים בהשראת הטבע: בנה ותכנת תמנון או תולעת"
english_slug: soft-robots-inspired-by-nature-build-and-program-octopus-or-worm
category: "רובוטיקה"
tags: [רובוטיקה רכה, ביומימטיקה, הנדסה, רובוטים, תכנות]
---
# רובוטים רכים בהשראת הטבע: בנה ותכנת תמנון או תולעת

דמיינו מכונות שיכולות להתפתל, להידחק ולהשתחל במקומות הכי בלתי צפויים. רובוטים שלא מפחדים להתנגש בכם כי הם פשוט... רכים! ברוכים הבאים לעולם המרתק של רובוטיקה רכה, ששואבת השראה ישירות מהיצורים הגמישים ביותר בטבע - כמו תמנונים ותולעים. האם תצליחו לבנות ולתכנת רובוט רך משלכם שיבצע משימות?

<div id="app-container">
    <div id="build-section" class="app-section">
        <h2>בנה את הרובוט הרך שלך</h2>
        <p>בחר את סוג הגוף והוסף אקטואטורים - ה"שרירים" שיגרמו לרובוט שלך לזוז.</p>
        <div class="control-group">
            <label for="body-type">בחר סוג גוף:</label>
            <select id="body-type">
                <option value="worm">תולעת</option>
                <option value="octopus">תמנון</option>
            </select>
        </div>
         <div class="control-group">
            <label for="actuator-type">סוג "שריר" (אקטואטור):</label>
            <select id="actuator-type">
                <option value="pneumatic">פניאומטי (מתנפח - דוחף החוצה)</option>
                <option value="smart">חומר חכם (מתכווץ - מושך פנימה)</option>
            </select>
        </div>

        <div id="robot-body-area" class="interactive-area">
            <!-- SVG will be loaded here -->
            <p class="placeholder-text">לחץ על הגוף כדי להוסיף אקטואטורים.</p>
        </div>

        <div id="actuator-tools">
            <h3>האקטואטורים שלך:</h3>
            <ul id="actuator-list">
                 <!-- List of added actuators will appear here -->
                 <li class="placeholder-text">הוסף אקטואטורים לגוף הרובוט.</li>
            </ul>
        </div>
    </div>

    <div id="program-section" class="app-section">
        <h2>תכנת את התנועה</h2>
        <p>צור רצף של פעולות כדי לגרום לרובוט שלך לנוע.</p>
        <div id="program-blocks" class="interactive-area">
            <!-- Program steps will be added here -->
             <p class="placeholder-text">לחץ "הוסף שלב" כדי להתחיל לתכנת.</p>
        </div>
        <button id="add-step-button" class="app-button">הוסף שלב חדש</button>
    </div>

    <div id="simulation-section" class="app-section">
        <h2>צפה בסימולציה</h2>
        <p>הרץ את התוכנית שלך וראה איך הרובוט מתעורר לחיים!</p>
        <div id="simulation-area" class="interactive-area">
            <!-- Robot animation will happen here -->
        </div>
        <button id="run-simulation-button" class="app-button primary">הפעל סימולציה</button>
    </div>
</div>

<button id="toggle-explanation" class="app-button secondary">הצג/הסתר הסבר על רובוטיקה רכה</button>
<div id="explanation" style="display: none;">
    <h2>מהם רובוטים רכים (Soft Robots)?</h2>
    <p>תשכחו מרובוטים קשיחים ומאיימים. רובוטים רכים עשויים מחומרים גמישים כמו סיליקון או גומי, ומחקים את האופן שבו יצורים חיים משנים את צורתם כדי לנוע ולהתמודד עם סביבות מורכבות. הם בטוחים יותר לאינטראקציה עם בני אדם ויכולים להגיע למקומות שרובוטים קשיחים לא יכולים.</p>

    <h2>למה שהטבע ישמש השראה? (ביומימטיקה)</h2>
    <p>תמנונים, תולעים, כוכבי ים - כולם אלופים בשינוי צורה ותנועה חלקה וחסרת מפרקים. רובוטיקה רכה שואבת רעיונות מהביולוגיה הזו כדי ליצור מכונות עם יכולות דומות: התפתלות, אחיזה עדינה, ומעבר במעברים צרים. במקום מנועים גלויים, הם משתמשים ב"שרירים" פנימיים כמו לחץ אוויר או חומרים חכמים המגיבים לגירויים.</p>

    <h2>איך הם זזים? (עקרונות הפעלה - אקטואציה)</h2>
    <p>במקום מנועים חשמליים, רובוטים רכים מופעלים על ידי:</p>
    <ul>
        <li><strong>אקטואטורים פניאומטיים/הידראוליים:</strong> ניפוח או כיווץ של חללים פנימיים באמצעות לחץ אוויר או נוזל, בדומה לבלון שמתנפח.</li>
        <li><strong>שרירים מלאכותיים מחומרים חכמים:</strong> חומרים שמשנים את צורתם או מתכווצים כשהם מקבלים אות חיצוני (חשמל, חום).</li>
    </ul>

    <h2>אתגרים והבטחה עתידית:</h2>
    <p>שליטה מדויקת על גוף גמיש היא אתגר הנדסי משמעותי. בנוסף, פיתוח חיישנים רכים ומקורות כוח קטנים ויעילים עדיין נמצא בחזית המחקר. עם זאת, רובוטיקה רכה מבטיחה מהפכה בתחומים כמו רפואה (ניתוחים זעירים), חיפוש והצלה, אוטומציה עדינה במפעלי ייצור, ואפילו רובוטיקה לבישה שמסייעת בתנועה.</p>
</div>

<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #1a4b5a;
        font-weight: 600;
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
        color: #007bff;
    }

    #app-container {
        display: flex;
        flex-wrap: wrap;
        gap: 25px;
        margin-bottom: 30px;
    }

    .app-section {
        background-color: #fff;
        border: 1px solid #e0e0e0;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        flex: 1;
        min-width: 320px;
        display: flex;
        flex-direction: column;
    }

    .app-section h2 {
        margin-top: 0;
        margin-bottom: 10px;
        border-bottom: 2px solid #007bff;
        padding-bottom: 5px;
        color: #007bff;
    }

    .app-section p {
        margin-bottom: 15px;
        color: #555;
    }

    .control-group {
        margin-bottom: 15px;
    }

    label {
        display: block;
        margin-bottom: 5px;
        font-weight: bold;
        color: #555;
    }

    select, input[type="number"] {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1em;
        width: calc(100% - 22px); /* Account for padding and border */
        box-sizing: border-box; /* Include padding/border in element's total width/height */
    }

    select:focus, input[type="number"]:focus, button:focus {
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.2);
    }


    .interactive-area {
        width: 100%;
        min-height: 250px; /* Increased height for better interaction */
        border: 2px dashed #b0c4de;
        margin-top: 10px;
        position: relative;
        overflow: hidden;
        background-color: #e9f5ff; /* Light blue background */
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 8px;
        transition: border-color 0.3s ease;
    }

     .interactive-area:hover {
         border-color: #007bff;
     }

     .interactive-area .placeholder-text {
         color: #888;
         font-style: italic;
         pointer-events: none; /* Don't block clicks */
     }


    #robot-body-area svg, #simulation-area svg {
         max-width: 95%; /* Slightly larger */
         max-height: 95%; /* Slightly larger */
         pointer-events: auto; /* Make SVG clickable */
         overflow: visible; /* Allow actuators/effects slightly outside main bounds */
         transition: transform 0.5s ease-in-out; /* Smooth transitions for SVG body */
    }

    #robot-body-area svg rect, #robot-body-area svg path,
    #simulation-area svg rect, #simulation-area svg path {
        transition: fill 0.3s ease, transform 0.5s ease; /* Add transitions to SVG parts */
         transform-origin: center; /* Default origin for transforms */
    }


    .actuator {
        position: absolute;
        width: 20px; /* Slightly larger */
        height: 20px; /* Slightly larger */
        border-radius: 50%;
        cursor: pointer;
        border: 3px solid rgba(255, 255, 255, 0.8); /* White border with transparency */
        box-sizing: border-box;
        z-index: 10; /* Above SVG */
        transition: background-color 0.3s ease, transform 0.2s ease;
         box-shadow: 0 0 5px rgba(0,0,0,0.3);
    }

    .actuator.pneumatic {
        background-color: #17a2b8; /* Info blue */
    }

    .actuator.smart {
        background-color: #ffc107; /* Warning yellow */
    }

    .actuator:hover {
        transform: scale(1.2);
    }

     #actuator-tools h3 {
         margin-top: 20px;
         margin-bottom: 5px;
         border-bottom: none;
         color: #333;
     }

    #actuator-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .actuator-list-item {
        background-color: #f8f9fa; /* Light grey background */
        border: 1px solid #e9ecef;
        padding: 8px 10px;
        margin-bottom: 5px;
        border-radius: 4px;
        font-size: 0.9em;
        color: #495057;
    }

    #program-blocks {
        margin-top: 15px;
        padding: 15px;
        min-height: 150px; /* Taller program area */
        background-color: #f0f3f5; /* Very light blue */
        border: 2px dashed #b0c4de;
        border-radius: 8px;
    }

    .program-step {
        background-color: #e9ecef; /* Slightly darker grey */
        border: 1px solid #dee2e6;
        padding: 12px;
        margin-bottom: 12px; /* Increased margin */
        border-radius: 6px;
        display: flex;
        flex-direction: column; /* Stack elements vertically */
        gap: 10px; /* Space between actions */
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .program-step span:first-child {
        font-weight: bold;
        color: #0056b3;
        margin-bottom: 5px;
    }

     .step-actions {
         display: flex;
         flex-wrap: wrap; /* Allow actions to wrap */
         gap: 10px; /* Space between action blocks */
         align-items: center;
     }

    .step-action {
        background-color: #f8f9fa;
        border: 1px solid #ced4da;
        padding: 8px;
        border-radius: 4px;
        display: flex; /* Align items horizontally within action */
        gap: 5px; /* Space between action elements */
        align-items: center;
    }

    .program-step select, .program-step input {
        padding: 6px;
        border: 1px solid #ced4da;
        border-radius: 4px;
        font-size: 0.9em;
         width: auto; /* Auto width for inline elements */
         max-width: 120px; /* Max width for selects/inputs */
    }
    .program-step input[type="number"] {
         width: 70px; /* Specific width for duration */
    }


    .app-button {
        display: inline-block;
        padding: 12px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        margin-top: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
    }

    .app-button:hover {
        background-color: #0056b3;
         transform: translateY(-1px);
    }

     .app-button:active {
         transform: translateY(0);
     }

    .app-button.primary {
        background-color: #28a745; /* Success green */
    }
     .app-button.primary:hover {
         background-color: #218838;
     }

     .app-button.secondary {
         background-color: #6c757d; /* Secondary grey */
     }
      .app-button.secondary:hover {
          background-color: #5a6268;
      }

      .app-button button.remove-button {
           background-color: #dc3545; /* Danger red */
           color: white;
           border: none;
           border-radius: 4px;
           padding: 4px 8px;
           cursor: pointer;
           font-size: 0.8em;
           margin-left: 5px;
           transition: background-color 0.3s ease;
           line-height: 1; /* Prevent extra height */
      }
      .app-button button.remove-button:hover {
           background-color: #c82333;
           transform: none; /* Override button hover transform */
      }


    #explanation {
        margin-top: 25px;
        padding: 20px;
        border: 1px solid #b0c4de;
        border-radius: 10px;
        background-color: #e9f5ff; /* Light blue */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    #explanation h2 {
        margin-top: 0;
        color: #1a4b5a;
        border-bottom: 2px solid #17a2b8; /* Info blue border */
        padding-bottom: 5px;
    }

    #explanation ul {
        list-style: disc;
        margin-left: 25px;
        margin-bottom: 15px;
        color: #555;
    }

    #explanation li {
        margin-bottom: 8px;
    }


    /* --- Simulation Animations --- */

    /* Worm Segments */
     #simulation-area #worm-svg rect {
         /* Default fill */
         fill: #90EE90;
         stroke: #006400;
         transition: fill 0.4s ease-in-out, transform 0.4s ease-in-out;
         transform-origin: center;
     }

     #simulation-area #worm-svg rect.sim-active-pneumatic {
         fill: #4682B4; /* SteelBlue */
         transform: scale(1.05, 1.2); /* Expand slightly more vertically */
         animation: worm-pneumatic-pulse 0.6s infinite alternate ease-in-out;
     }

     #simulation-area #worm-svg rect.sim-active-smart {
         fill: #DC143C; /* Crimson */
         transform: scale(0.95, 0.8); /* Contract vertically, slight horizontal compress */
         animation: worm-smart-pulse 0.6s infinite alternate ease-in-out;
     }

     @keyframes worm-pneumatic-pulse {
         from { transform: scale(1, 1); fill: #90EE90; }
         to { transform: scale(1.05, 1.2); fill: #4682B4; }
     }
     @keyframes worm-smart-pulse {
         from { transform: scale(1, 1); fill: #90EE90;}
         to { transform: scale(0.95, 0.8); fill: #DC143C;}
     }


    /* Octopus Tentacles */
     #simulation-area #octopus-svg path {
         /* Default fill */
         fill: #800080; /* Purple */
         transition: fill 0.4s ease-in-out, transform 0.6s ease-in-out; /* Added transform transition */
          transform-origin: bottom; /* Tentacles bend from base */
     }

     #simulation-area #octopus-svg path.sim-active-pneumatic {
         fill: #BA55D3; /* MediumOrchid */
         /* Simulate extension/thickening */
         transform: scale(1.1, 1.05); /* Slight scale */
         /* No animation for simplicity, just static change */
     }

     #simulation-area #octopus-svg path.sim-active-smart {
         fill: #FF8C00; /* DarkOrange */
         /* Simulate contraction/curl - basic rotation/translate is simpler than complex path bending */
         /* Need to find a way to target origin dynamically per tentacle for realistic bend */
         /* For simplicity, let's use a visual indicator like color change and maybe slight scale */
         transform: scaleY(0.9); /* Simulate slight contraction */
          /* Complex bending requires JS manipulation of SVG path data or more advanced CSS */
          /* Let's stick to color and scale for now */
     }


     /* General active state for simulation visual feedback */
     .simulation-running .actuator {
          /* Maybe pulse the actuator visual itself */
          animation: actuator-pulse 0.8s infinite alternate;
     }
     @keyframes actuator-pulse {
         from { opacity: 1; }
         to { opacity: 0.7; }
     }


</style>

<script>
    const appContainer = document.getElementById('app-container');
    const bodyTypeSelect = document.getElementById('body-type');
    const robotBodyArea = document.getElementById('robot-body-area');
    const actuatorTypeSelect = document.getElementById('actuator-type');
    const actuatorList = document.getElementById('actuator-list');
    const programBlocks = document.getElementById('program-blocks');
    const addStepButton = document.getElementById('add-step-button');
    const simulationArea = document.getElementById('simulation-area');
    const runSimulationButton = document.getElementById('run-simulation-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let actuators = []; // Array to store actuator objects {id: N, x: X, y: Y, type: 'pneumatic'/'smart', attachedTo: 'segment-N'/'tentacle-N'}
    let program = []; // Array of step objects. Each step is an array of actions {actuatorId: N, action: 'activate'/'deactivate', duration: M}
    let nextActuatorId = 1;
    let simulationRunning = false;

    // --- SVG Definitions ---
    // Added more distinct colors and stroke for clarity
    const svgs = {
        worm: `
            <svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg" id="worm-svg">
                <rect id="segment-1" x="10" y="30" width="50" height="40" fill="#90EE90" stroke="#006400" stroke-width="3" rx="8" ry="8"/>
                <rect id="segment-2" x="60" y="30" width="50" height="40" fill="#90EE90" stroke="#006400" stroke-width="3" rx="8" ry="8"/>
                <rect id="segment-3" x="110" y="30" width="50" height="40" fill="#90EE90" stroke="#006400" stroke-width="3" rx="8" ry="8"/>
                <rect id="segment-4" x="160" y="30" width="50" height="40" fill="#90EE90" stroke="#006400" stroke-width="3" rx="8" ry="8"/>
                <rect id="segment-5" x="210" y="30" width="50" height="40" fill="#90EE90" stroke="#006400" stroke-width="3" rx="8" ry="8"/>
                <rect id="segment-6" x="260" y="30" width="30" height="40" fill="#90EE90" stroke="#006400" stroke-width="3" rx="8" ry="8"/>
                <circle cx="10" cy="50" r="6" fill="#006400"/>
                <circle cx="290" cy="50" r="6" fill="#006400"/>
            </svg>
        `,
        octopus: `
            <svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" id="octopus-svg">
                 <path d="M 150,30 C 120,0 180,0 150,30 Z" fill="#663399" stroke="#4B0082" stroke-width="2"/> <!-- Head -->
                 <path d="M 150,30 C 140,50 110,100 80,180 C 70,190 90,190 100,180 L 110,150 C 115,140 135,140 140,150 Z" fill="#800080" stroke="#4B0082" stroke-width="2" id="tentacle-1"/>
                 <path d="M 150,30 C 160,50 190,100 220,180 C 230,190 210,190 200,180 L 190,150 C 185,140 165,140 160,150 Z" fill="#800080" stroke="#4B0082" stroke-width="2" id="tentacle-2"/>
                 <path d="M 150,30 C 130,40 90,80 60,150 C 50,160 70,170 80,160 L 90,130 C 95,120 115,120 120,130 Z" fill="#800080" stroke="#4B0082" stroke-width="2" id="tentacle-3"/>
                 <path d="M 150,30 C 170,40 210,80 240,150 C 250,160 230,170 220,160 L 210,130 C 205,120 185,120 180,130 Z" fill="#800080" stroke="#4B0082" stroke-width="2" id="tentacle-4"/>
                 <!-- Add couple more tentacles for octopus feel -->
                 <path d="M 150,30 C 145,40 125,70 100,130 C 90,140 110,150 120,140 L 130,110 C 135,100 155,100 160,110 Z" fill="#800080" stroke="#4B0082" stroke-width="2" id="tentacle-5"/>
                 <path d="M 150,30 C 155,40 175,70 200,130 C 210,140 190,150 180,140 L 170,110 C 165,100 145,100 140,110 Z" fill="#800080" stroke="#4B0082" stroke-width="2" id="tentacle-6"/>
            </svg>
        `
    };

    // --- Helper Functions ---
    function loadRobotSVG(type) {
        robotBodyArea.innerHTML = svgs[type] || '';
        simulationArea.innerHTML = svgs[type] || ''; // Load same SVG for simulation

        // Clear existing actuators and program
        actuators = [];
        actuatorList.innerHTML = '<li class="placeholder-text">הוסף אקטואטורים לגוף הרובוט.</li>';
        program = [];
        programBlocks.innerHTML = '<p class="placeholder-text">לחץ "הוסף שלב" כדי להתחיל לתכנת.</p>';
        nextActuatorId = 1;

        // Update placeholder text visibility
        updatePlaceholderVisibility();
    }

    function updatePlaceholderVisibility() {
        robotBodyArea.querySelector('.placeholder-text').style.display = actuators.length === 0 ? 'block' : 'none';
        programBlocks.querySelector('.placeholder-text').style.display = programBlocks.querySelectorAll('.program-step').length === 0 ? 'block' : 'none';
        actuatorList.querySelector('.placeholder-text').style.display = actuators.length === 0 ? 'block' : 'none';
    }


     // Function to get the SVG element part that was clicked
     function getTargetSVGElement(svgElement, clientX, clientY) {
         const svgRect = svgElement.getBoundingClientRect();
         const point = svgElement.createSVGPoint();
         point.x = clientX;
         point.y = clientY;

         // Get the transformation matrix from screen coordinates to SVG coordinates
         const ctm = svgElement.getScreenCTM().inverse();
         const svgPoint = point.matrixTransform(ctm);

         // Check if the click is within any of the target elements (rectangles or paths)
         const targets = svgElement.querySelectorAll('rect, path');
         for (const target of targets) {
             // Exclude the main head shape for octopus, maybe by ID or type
             if (svgElement.id === 'octopus-svg' && target.tagName.toLowerCase() === 'path' && target.getAttribute('d').length < 50) { // Simple heuristic for head path
                  continue;
             }
             if (target.isPointInFill(svgPoint)) {
                 return target; // Return the actual SVG element
             }
         }
         return null; // No target element found at click location
     }


    function addActuator(event) {
        const robotSVGArea = document.getElementById('robot-body-area'); // Use build area
        const svgElement = robotSVGArea.querySelector('svg');
        if (!svgElement) return;

        const targetElement = getTargetSVGElement(svgElement, event.clientX, event.clientY);

        if (!targetElement) {
             console.log('Clicked outside a known target element');
             return; // Only add actuator if a segment/tentacle is clicked
         }

         const targetElementId = targetElement.id;
         if (!targetElementId) {
              console.log('Clicked element has no ID');
              return; // Ensure the target element has an ID
         }


        const type = actuatorTypeSelect.value;

        // We store rough position relative to the container for visual div placement
        const containerRect = robotSVGArea.getBoundingClientRect();
        const x = event.clientX - containerRect.left;
        const y = event.clientY - containerRect.top;


        actuators.push({ id: nextActuatorId, x: x, y: y, type: type, attachedTo: targetElementId });

        const actuatorDiv = document.createElement('div');
        actuatorDiv.classList.add('actuator', type);
        actuatorDiv.style.left = `${x - 10}px`; // Center the div visually (div is 20x20)
        actuatorDiv.style.top = `${y - 10}px`; // Center the div visually
        actuatorDiv.dataset.actuatorId = nextActuatorId;
        actuatorDiv.title = `אקטואטור ${nextActuatorId} (${type === 'pneumatic' ? 'פניאומטי' : 'חומר חכם'})`; // Add tooltip
        robotSVGArea.appendChild(actuatorDiv);

        const actuatorListItem = document.createElement('li');
        actuatorListItem.classList.add('actuator-list-item');
        actuatorListItem.textContent = `אקטואטור ${nextActuatorId} (${type === 'pneumatic' ? 'פניאומטי' : 'חומר חכם'}) על ${targetElementId}`;
        actuatorList.appendChild(actuatorListItem);

        nextActuatorId++;
        updatePlaceholderVisibility();
        updateProgramActuatorSelects(); // Update dropdowns in program section

        // Add actuators to simulation SVG area as well (just the visual div markers)
        const simAreaDiv = document.getElementById('simulation-area');
         const simActuatorDiv = document.createElement('div');
         simActuatorDiv.classList.add('actuator', type);
         // Position relative to the simulation area, assuming same layout
         const simContainerRect = simAreaDiv.getBoundingClientRect();
         simActuatorDiv.style.left = `${event.clientX - simContainerRect.left - 10}px`; // Center the div
         simActuatorDiv.style.top = `${event.clientY - simContainerRect.top - 10}px`; // Center the div
         simActuatorDiv.dataset.actuatorId = actuators.length; // Link by index for simplicity or use nextActuatorId-1? Let's use the ID.
         simActuatorDiv.dataset.actuatorId = nextActuatorId - 1;
         simAreaDiv.appendChild(simActuatorDiv);
    }

    function updateProgramActuatorSelects() {
         programBlocks.querySelectorAll('.program-step select:first-child').forEach(select => {
             const selectedValue = select.value; // Keep the currently selected value if possible
             select.innerHTML = '<option value="">בחר אקטואטור</option>';
             actuators.forEach(act => {
                 const option = document.createElement('option');
                 option.value = act.id;
                 option.textContent = `אקטואטור ${act.id} (${act.type === 'pneumatic' ? 'פניאומטי' : 'חומר חכם'})`;
                 select.appendChild(option);
             });
             // Attempt to restore selection
             if ([...select.options].some(opt => opt.value === selectedValue)) {
                 select.value = selectedValue;
             }
         });
    }


    function addProgramStep() {
        const stepIndex = program.length; // This will be the index in the program array
        const stepDiv = document.createElement('div');
        stepDiv.classList.add('program-step');
        stepDiv.dataset.stepIndex = stepIndex; // Use dataset for index

        // Step Label
        const stepLabel = document.createElement('span');
        stepLabel.textContent = `שלב ${stepIndex + 1}:`;
        stepDiv.appendChild(stepLabel);

        // Actions container
        const actionsContainer = document.createElement('div');
        actionsContainer.classList.add('step-actions');
        stepDiv.appendChild(actionsContainer);

        // Add action button for this step
        const addActionButton = document.createElement('button');
        addActionButton.textContent = 'הוסף פעולה';
        addActionButton.classList.add('app-button');
        addActionButton.onclick = () => addActionToStep(stepDiv); // Pass the stepDiv element
        stepDiv.appendChild(addActionButton);

        programBlocks.appendChild(stepDiv);

        // Add the step to the program data structure (initially empty actions)
        program.push([]);
        updatePlaceholderVisibility();
    }

    // Changed to accept stepDiv element
    function addActionToStep(stepDiv) {
        const actionsContainer = stepDiv.querySelector('.step-actions');
        const stepIndex = parseInt(stepDiv.dataset.stepIndex);

        const actionDiv = document.createElement('div');
        actionDiv.classList.add('step-action');

        // Actuator Select
        const actuatorSelect = document.createElement('select');
        actuatorSelect.innerHTML = '<option value="">בחר אקטואטור</option>';
        actuators.forEach(act => {
            actuatorSelect.innerHTML += `<option value="${act.id}">אקטואטור ${act.id}</option>`;
        });
        actionDiv.appendChild(actuatorSelect);

        // Action Type Select
        const actionTypeSelect = document.createElement('select');
        actionTypeSelect.innerHTML = `
            <option value="">בחר פעולה</option>
            <option value="activate">הפעל</option>
            <option value="deactivate">כבה</option>
            <option value="wait">המתן</option>
        `;
        actionDiv.appendChild(actionTypeSelect);

         // Duration/Wait Input
         const durationInput = document.createElement('input');
         durationInput.type = 'number';
         durationInput.placeholder = 'זמן (ms)';
         durationInput.min = 0;
         durationInput.value = 500; // Default duration
         durationInput.style.width = '80px';
         actionDiv.appendChild(durationInput);

        // Remove button
        const removeButton = document.createElement('button');
        removeButton.textContent = 'X';
        removeButton.classList.add('remove-button'); // Use new class
        removeButton.onclick = () => {
            actionDiv.remove();
            // Program array update is done during parseProgram before simulation
        };
        actionDiv.appendChild(removeButton);

        actionsContainer.appendChild(actionDiv);

         // Add a dummy action to the program array structure immediately, details will be parsed later
         // This ensures the program array size matches the UI steps, although the action details aren't here yet
         // A more robust system would update the array state as inputs change. Parsing on run is simpler for this case.
         // program[stepIndex].push({}); // Example: add a placeholder object
    }

    function parseProgramFromUI() {
        const newProgram = [];
        programBlocks.querySelectorAll('.program-step').forEach((stepDiv) => {
            const stepActions = [];
            stepDiv.querySelectorAll('.step-action').forEach(actionDiv => {
                const actuatorId = parseInt(actionDiv.querySelector('select:nth-child(1)').value);
                const action = actionDiv.querySelector('select:nth-child(2)').value;
                const duration = parseInt(actionDiv.querySelector('input[type="number"]').value) || 0;

                // Validate action data
                if (action) {
                     if (action === 'wait' && duration >= 0) {
                          stepActions.push({ actuatorId: null, action: 'wait', duration: duration }); // ActuatorId is null for wait
                     } else if ((action === 'activate' || action === 'deactivate') && actuatorId > 0 && actuators.find(a => a.id === actuatorId)) {
                          stepActions.push({ actuatorId: actuatorId, action: action, duration: duration });
                     }
                }
            });
            newProgram.push(stepActions);
        });
        program = newProgram;
        console.log("Parsed Program:", program);
         return program; // Return the parsed program
    }


    async function runSimulation() {
        if (actuators.length === 0) {
            alert("אנא הוסף אקטואטורים לפני הפעלת הסימולציה.");
            return;
        }
        const currentProgram = parseProgramFromUI(); // Get the latest program from the UI
        if (currentProgram.length === 0 || currentProgram.every(step => step.length === 0)) {
             alert("אנא הוסף שלבים ותנועות לתוכנית.");
             return;
         }

        const simSVG = simulationArea.querySelector('svg');
        if (!simSVG) return;

        simulationRunning = true;
        appContainer.classList.add('simulation-running'); // Add class for visual indicators

        // Reset simulation visual state
        const segments = simSVG.querySelectorAll('rect, path'); // Target segments/tentacles
        segments.forEach(seg => {
            seg.classList.remove('sim-active-pneumatic', 'sim-active-smart');
             // Reset any inline styles applied for simulation state (like fill or transform)
             seg.style.fill = ''; // Reset to original fill from SVG definition (via CSS default)
             seg.style.transform = ''; // Reset any transforms
             // Need to ensure default CSS rules restore the appearance correctly
        });

         // Reset actuator visual states
        simulationArea.querySelectorAll('.actuator').forEach(actDiv => {
             actDiv.classList.remove('sim-active-pneumatic', 'sim-active-smart');
        });


        runSimulationButton.disabled = true; // Disable button during simulation

        // Store current state of actuators/segments
        let currentStates = {}; // { elementId: { pneumatic: boolean, smart: boolean }, ... }

        for (let i = 0; i < currentProgram.length; i++) {
             const step = currentProgram[i];
             console.log(`Running Step ${i + 1}`, step);

             const actionsToExecute = step.filter(action => action.action !== 'wait');
             let maxActionDuration = 0; // Track duration of non-wait actions (if needed for complex anims)
             let waitDuration = 0;

             actionsToExecute.forEach(action => {
                const actuator = actuators.find(a => a.id === action.actuatorId);
                if (!actuator || !actuator.attachedTo) return;

                const targetElement = simSVG.getElementById(actuator.attachedTo);
                if (!targetElement) return;

                const actuatorSimDiv = simulationArea.querySelector(`.actuator[data-actuator-id='${actuator.id}']`);


                // Apply state change immediately based on action
                if (action.action === 'activate') {
                     if (actuator.type === 'pneumatic') {
                          targetElement.classList.add('sim-active-pneumatic');
                          targetElement.classList.remove('sim-active-smart'); // Deactivate opposite
                          if (actuatorSimDiv) actuatorSimDiv.classList.add('sim-active-pneumatic');
                          if (actuatorSimDiv) actuatorSimDiv.classList.remove('sim-active-smart');
                          currentStates[actuator.attachedTo] = { pneumatic: true, smart: false };
                     } else if (actuator.type === 'smart') {
                          targetElement.classList.add('sim-active-smart');
                           targetElement.classList.remove('sim-active-pneumatic'); // Deactivate opposite
                           if (actuatorSimDiv) actuatorSimDiv.classList.add('sim-active-smart');
                           if (actuatorSimDiv) actuatorSimDiv.classList.remove('sim-active-pneumatic');
                           currentStates[actuator.attachedTo] = { pneumatic: false, smart: true };
                     }
                } else if (action.action === 'deactivate') {
                     targetElement.classList.remove('sim-active-pneumatic', 'sim-active-smart');
                     if (actuatorSimDiv) actuatorSimDiv.classList.remove('sim-active-pneumatic', 'sim-active-smart');
                      currentStates[actuator.attachedTo] = { pneumatic: false, smart: false };
                }

                 // In this simplified model, the 'duration' on activate/deactivate actions is ignored.
                 // The visual state applies instantly and lasts until the next step changes it.
                 // The actual time passing is controlled by the 'wait' actions.
            });

            // Find the total wait duration for this step
             step.filter(action => action.action === 'wait').forEach(action => {
                 waitDuration += action.duration;
             });

            // Wait for the total wait duration before proceeding to the next step
            await new Promise(resolve => setTimeout(resolve, waitDuration));

        }

        // Simulation finished - reset state after a short delay
        simulationRunning = false;
         appContainer.classList.remove('simulation-running');
        setTimeout(() => {
             segments.forEach(seg => {
                 seg.classList.remove('sim-active-pneumatic', 'sim-active-smart');
                 // Reset inline styles if they were used instead of just classes
                  seg.style.fill = '';
                  seg.style.transform = '';
             });
             simulationArea.querySelectorAll('.actuator').forEach(actDiv => {
                 actDiv.classList.remove('sim-active-pneumatic', 'sim-active-smart');
            });

             runSimulationButton.disabled = false; // Re-enable button
             // alert("סימולציה הסתיימה!"); // Optional: remove alert for smoother feel
        }, 500); // Keep final state for a brief moment
    }


    // --- Event Listeners ---
    bodyTypeSelect.addEventListener('change', (e) => loadRobotSVG(e.target.value));
    robotBodyArea.addEventListener('click', addActuator);
    addStepButton.addEventListener('click', addProgramStep);
    runSimulationButton.addEventListener('click', runSimulation);
     toggleExplanationButton.addEventListener('click', () => {
         const isHidden = explanationDiv.style.display === 'none';
         explanationDiv.style.display = isHidden ? 'block' : 'none';
         toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג/הסתר הסבר על רובוטיקה רכה';
         // Optional: smooth toggle animation with CSS transitions on max-height/opacity
     });


    // --- Initial Load ---
    loadRobotSVG(bodyTypeSelect.value); // Load default worm SVG

</script>
---
```