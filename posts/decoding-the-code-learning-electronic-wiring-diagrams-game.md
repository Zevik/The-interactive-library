---
title: "פענוח הסכמה: הרכיבו מעגלים אלקטרוניים כמו מקצוענים!"
english_slug: decoding-the-code-learning-electronic-wiring-diagrams-game
category: "הנדסת חשמל"
tags: תרשימי חיווט, סכמות אלקטרוניות, מעגלים אלקטרוניים, אלקטרוניקה בסיסית, רכיבים אלקטרוניים, סימולציה, לימוד אינטראקטיבי
---
# פענוח הסכמה: הרכיבו מעגלים אלקטרוניים כמו מקצוענים!
סכמות אלקטרוניות הן מפת הדרך הסודית לכל מכשיר, מפשוט ועד מורכב. רוצים לדעת לקרוא אותן ולבנות מעגלים משלכם? בואו נצא למשימה לפענח את הקוד החשמלי ולהאיר את הנורה (תרתי משמע)!

<div class="simulation-container">
    <div class="diagram-area">
        <h2>משימת ההרכבה:</h2>
        <p>הצליחו לחבר את הרכיבים שמשמאל כך שיצרו מעגל סדרתי תקין, בדיוק לפי התרשים:</p>
        <div id="target-diagram">
            <!-- Improved SVG representation with clearer labels/style -->
            <svg width="350" height="200" viewBox="0 0 350 200" preserveAspectRatio="xMidYMid meet">
                <!-- Battery -->
                <line x1="50" y1="100" x2="60" y2="100" stroke="#333" stroke-width="3"/>
                <line x1="60" y1="90" x2="60" y2="110" stroke="#333" stroke-width="3"/> <!-- Plus -->
                <line x1="70" y1="95" x2="70" y2="105" stroke="#333" stroke-width="3"/> <!-- Minus -->
                <line x1="70" y1="100" x2="80" y2="100" stroke="#333" stroke-width="3"/>
                <text x="65" y="125" text-anchor="middle" font-size="14" fill="#333">סוללה (+/-)</text>
                <circle cx="50" cy="100" r="4" fill="#333"/>
                <circle cx="80" cy="100" r="4" fill="#333"/>

                <!-- Wire -->
                <line x1="80" y1="100" x2="120" y2="100" stroke="#333" stroke-width="3"/>

                <!-- Resistor -->
                <path d="M120 100 L125 95 L130 105 L135 95 L140 105 L145 95 L150 105 L155 100" fill="none" stroke="#333" stroke-width="3"/>
                <text x="137.5" y="125" text-anchor="middle" font-size="14" fill="#333">נגד (R1)</text>
                 <circle cx="120" cy="100" r="4" fill="#333"/>
                <circle cx="155" cy="100" r="4" fill="#333"/>


                <!-- Wire -->
                <line x1="155" y1="100" x2="190" y2="100" stroke="#333" stroke-width="3"/>

                <!-- LED -->
                <line x1="190" y1="100" x2="210" y2="100" stroke="#333" stroke-width="3"/> <!-- Anode connection -->
                <polygon points="210,100 225,90 225,110" fill="none" stroke="#333" stroke-width="3"/> <!-- Diode triangle -->
                <line x1="225" y1="90" x2="225" y2="110" stroke="#333" stroke-width="3"/> <!-- Cathode line -->
                 <!-- LED arrows -->
                <line x1="235" y1="95" x2="245" y2="85" stroke="#333" stroke-width="2"/>
                <path d="M245 85 L240 85 M245 85 L245 90" stroke="#333" stroke-width="2"/>
                <line x1="240" y1="100" x2="250" y2="90" stroke="#333" stroke-width="2"/>
                 <path d="M250 90 L245 90 M250 90 L250 95" stroke="#333" stroke-width="2"/>

                <text x="220" y="125" text-anchor="middle" font-size="14" fill="#333">LED (D1)</text>
                <circle cx="190" cy="100" r="4" fill="#333"/> <!-- Anode point -->
                 <circle cx="225" cy="100" r="4" fill="#333"/> <!-- Cathode point -->


                <!-- Wire connecting LED Cathode back to loop -->
                <line x1="225" y1="100" x2="250" y2="100" stroke="#333" stroke-width="3"/>

                <!-- Closing loop back to battery -->
                <line x1="50" y1="100" x2="50" y2="150" stroke="#333" stroke-width="3"/>
                <line x1="50" y1="150" x2="250" y2="150" stroke="#333" stroke-width="3"/>
                <line x1="250" y1="150" x2="250" y2="100" stroke="#333" stroke-width="3"/>
            </svg>
        </div>
    </div>

    <div class="toolbox-area">
        <h2>תיבת רכיבים:</h2>
        <p>גררו רכיבים למשטח העבודה:</p>
        <div class="component-toolbox" id="battery-tool" data-component-type="battery" draggable="true">
             <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 50 30'%3E%3Crect x='5' y='10' width='40' height='10' fill='%23555'/%3E%3Cline x1='10' y1='15' x2='10' y2='25' stroke='black' stroke-width='2'/%3E%3Cline x1='15' y1='15' x2='15' y2='25' stroke='black' stroke-width='2'/%3E%3Cline x1='20' y1='15' x2='20' y2='25' stroke='black' stroke-width='2'/%3E%3Cline x1='25' y1='15' x2='25' y2='25' stroke='black' stroke-width='2'/%3E%3Cline x1='30' y1='15' x2='30' y2='25' stroke='black' stroke-width='2'/%3E%3Cline x1='35' y1='15' x2='35' y2='25' stroke='black' stroke-width='2'/%3E%3Crect x='40' y='8' width='5' height='14' fill='%23555'/%3E%3Ctext x='15' y='18' font-size='10' text-anchor='middle' fill='white'%3E-%3C/text%3E%3Ctext x='42.5' y='18' font-size='10' text-anchor='middle' fill='white'%3E%2B%3C/text%3E%3C/svg%3E" alt="סוללה">
             <p>סוללה</p>
        </div>
        <div class="component-toolbox" id="resistor-tool" data-component-type="resistor" draggable="true">
            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 50 30'%3E%3Cpath d='M5 15 L10 10 L15 20 L20 10 L25 20 L30 10 L35 20 L40 15' fill='none' stroke='black' stroke-width='2'/%3E%3Cline x1='5' y1='15' x2='0' y2='15' stroke='black' stroke-width='2'/%3E%3Cline x1='40' y1='15' x2='45' y2='15' stroke='black' stroke-width='2'/%3E%3C/svg%3E" alt="נגד">
            <p>נגד</p>
        </div>
        <div class="component-toolbox" id="led-tool" data-component-type="led" draggable="true">
            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 50 30'%3E%3Cline x1='5' y1='15' x2='15' y2='15' stroke='black' stroke-width='2'/%3E%3Cpolygon points='15,15 30,10 30,20' fill='none' stroke='black' stroke-width='2'/%3E%3Cline x1='30' y1='10' x2='30' y2='20' stroke='black' stroke-width='2'/%3E%3Cline x1='30' y1='15' x2='45' y2='15' stroke='black' stroke-width='2'/%3E%3C/svg%3E" alt="LED">
            <p>LED</p>
        </div>
        <!-- Maybe add a trash can icon later -->
    </div>

    <div class="workspace-area" id="workspace">
        <h2>משטח עבודה:</h2>
        <p>גררו רכיבים לכאן וחברו ביניהם בלחיצה על הנקודות האדומות.</p>
        <svg id="connection-svg"></svg>
        <!-- Dropped components will go here -->
    </div>

    <button id="check-button">בדיקת המעגל</button>
    <div id="feedback-area"></div>
</div>

<button id="show-explanation-button">הצגת מדריך הפענוח</button>

<div id="explanation-area" style="display: none;">
    <h2>מדריך לפענוח סכמות אלקטרוניות</h2>
    <p>סכמה אלקטרונית היא שפה ויזואלית אוניברסלית לתקשורת על מבנה מעגלים. היא משתמשת ב<strong>סמלים סטנדרטיים</strong> לרכיבים וב<strong>קווים</strong> לציון חיבורים חשמליים.</p>

    <h3>יסודות הסכמה:</h3>
    <ul>
        <li><strong>קווים:</strong> מייצגים מוליכים (חוטים) המחברים רכיבים. קווים ישרים הם ברירת מחדל.</li>
        <li><strong>צמתים (Junctions):</strong> נקודות מפגש של מספר קווים. מסומנים בדרך כלל בנקודה מלאה. קווים שחוצים זה את זה ללא נקודה משמעותם שאינם מחוברים חשמלית (כמו גשר).</li>
        <li><strong>סמלים:</strong> כל רכיב אלקטרוני מקבל ייצוג גרפי ייחודי המוסכם בינלאומית.</li>
    </ul>

    <h3>סמלי רכיבים נפוצים (כפי שראינו במשחק):</h3>
    <ul>
        <li><strong>מקור מתח (סוללה, DC):</strong> מיוצג ע"י קווים מקבילים באורכים שונים. הקו הארוך הוא **הקוטב החיובי (+)**, הקצר הוא **השלילי (-)**.</li>
        <li><strong>נגד (Resistor):</strong> מגביל זרם. לרוב מיוצג ע"י קו זיגזג (תקן אמריקאי) או מלבן (תקן אירופי). אין לו קוטביות.</li>
        <li><strong>דיודת LED (Light Emitting Diode):</strong> סוג של דיודה שפולטת אור. מאפשרת לזרם לזרום רק בכיוון אחד - מ<strong>האנודה (+)</strong> (צד המשולש הצר) ל<strong>קתודה (-)</strong> (צד הפס). מסומנת כדיודה רגילה עם חצים היוצאים ממנה.</li>
        <li>רכיבים נוספים שתפגשו בהמשך: קבלים, טרנזיסטורים, מתגים, סלילים, ועוד רבים...</li>
    </ul>

    <h3>קריאת תוויות וערכים:</h3>
    <p>לצד הסמלים מופיעות לרוב תוויות (זיהוי הרכיב, למשל R1, D2) וערכים (הגודל החשמלי, למשל 1kΩ, 10µF). תוויות עוקבות אחר אות המייצגת את סוג הרכיב (R=נגד, C=קבל, D=דיודה, L=סליל, Q=טרנזיסטור, IC=מעגל משולב).</p>

    <h3>איך "עוקבים" אחרי זרם בסכמה?</h3>
    <p>דמיינו את הזרם יוצא מהקוטב החיובי של הסוללה (+), נע לאורך הקווים, עובר דרך הרכיבים (בהתאם לתפקידם וקוטביותם), וחוזר לקוטב השלילי (-). מעגל חייב להיות **סגור** כדי שהזרם יזרום ברציפות.</p>

    <h3>פתרון בעיות בעזרת סכמה:</h3>
    <ul>
        <li>ודאו שכל הרכיבים הנחוצים קיימים.</li>
        <li>עקבו אחר הקווים וודאו שכל רכיב מחובר לנקודות הנכונות.</li>
        <li><strong>הכי חשוב:</strong> בדקו קוטביות ברכיבים כמו סוללות ו-LEDים! חיבור הפוך ימנע מהמעגל לפעול או אף יגרום לנזק.</li>
    </ul>
</div>

<style>
    .simulation-container {
        direction: rtl; /* Set base direction for RTL */
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin-top: 20px;
        border: 1px solid #e0e0e0; /* Softer border */
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f8f8; /* Lighter background */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
         font-family: 'Arial', sans-serif; /* Use a common font */
    }

     .simulation-container h2, .simulation-container p {
         text-align: right;
         width: 100%; /* Ensure they take full width */
     }

    .diagram-area, .toolbox-area, .workspace-area {
        border: 1px solid #d0d0d0; /* Softer border */
        padding: 20px;
        border-radius: 8px;
        background-color: #ffffff; /* White background for inner areas */
        flex: 1; /* Allow areas to grow */
        min-width: 300px; /* Minimum width before wrapping */
        position: relative; /* Needed for SVG overlay */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05); /* Inner shadow */
    }

     .diagram-area h2, .toolbox-area h2, .workspace-area h2 {
         margin-top: 0;
         color: #0056b3; /* Theme color */
         border-bottom: 1px solid #eee;
         padding-bottom: 10px;
         margin-bottom: 15px;
     }

    .toolbox-area {
         min-width: 180px; /* Slightly wider toolbox */
         flex: unset; /* Don't grow, fixed width */
         width: 180px;
         display: flex;
         flex-direction: column;
         align-items: center;
         text-align: center; /* Center text in toolbox */
    }

     .toolbox-area p {
         font-size: 0.9em;
         color: #555;
     }

    .workspace-area {
        min-height: 350px; /* Taller workspace */
        position: relative;
        overflow: hidden; /* Hide overflow for lines */
        background-image: url('data:image/svg+xml,%3Csvg width="15" height="15" xmlns="http://www.w3.org/2000/svg"%3E%3Ccircle cx="7.5" cy="7.5" r="1.5" fill="%23e0e0e0"/%3E%3C/svg%3E'); /* More subtle dot grid */
        background-size: 15px 15px; /* Larger grid size */
        background-position: center; /* Center the grid */
    }

     #connection-svg {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none; /* Allow clicks to pass through to components */
         z-index: 1; /* Below components */
     }

    .component-toolbox {
        border: 1px solid #c0c0c0; /* Softer border */
        padding: 12px; /* More padding */
        margin-bottom: 12px; /* More space */
        cursor: grab;
        background-color: #e9e9e9; /* Light gray */
        border-radius: 8px; /* Rounded corners */
        text-align: center;
        width: 100px; /* Wider toolbox item */
        display: flex;
        flex-direction: column;
        align-items: center;
        font-size: 0.9em;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out; /* Smooth hover effects */
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }

    .component-toolbox:hover {
         transform: translateY(-3px); /* Lift on hover */
         box-shadow: 0 4px 8px rgba(0,0,0,0.15);
         background-color: #e0e0e0;
    }

    .component-toolbox img {
        width: 50px; /* Larger icons */
        height: 25px;
        margin-bottom: 8px; /* More space */
        pointer-events: none; /* Prevent dragging the image instead of the div */
    }

    .component-in-workspace {
        position: absolute;
        border: 1px solid #99aacc; /* Blueish border */
        padding: 10px;
        background-color: #ddeeff; /* Light blueish */
        border-radius: 8px;
        cursor: grab; /* Default cursor */
        z-index: 10; /* Above SVG */
         text-align: center;
        width: 100px; /* Match toolbox size */
         display: flex;
        flex-direction: column;
        align-items: center;
        font-size: 0.8em;
        pointer-events: all; /* Allow clicks on the component container */
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
         transition: box-shadow 0.1s ease-in-out;
    }

     .component-in-workspace.dragging {
         cursor: grabbing; /* Cursor when actually dragging */
         box-shadow: 0 5px 15px rgba(0,0,0,0.2); /* More prominent shadow when dragging */
         z-index: 30; /* Ensure it's on top */
     }

    .component-in-workspace img {
         width: 50px; /* Match toolbox size */
        height: 25px;
        margin-bottom: 5px;
        pointer-events: none; /* Prevent interference with drag */
    }

     .connection-point {
         position: absolute;
         width: 16px; /* Larger click area */
         height: 16px;
         background-color: rgba(255, 0, 0, 0.6); /* Semi-transparent red */
         border-radius: 50%;
         cursor: crosshair;
         z-index: 20; /* Above component */
         transform: translate(-50%, -50%); /* Center the point */
         pointer-events: all; /* Make points clickable */
         border: 2px solid #fff; /* White border */
         transition: background-color 0.1s ease-in-out, transform 0.1s ease-in-out;
     }

     .connection-point:hover {
         background-color: rgba(0, 255, 0, 0.8); /* Green on hover */
         transform: translate(-50%, -50%) scale(1.1); /* Slightly grow on hover */
     }

     /* Position connection points relative to component-in-workspace */
     .component-in-workspace[data-component-type="battery"] .connection-point[data-terminal="plus"] { top: 50%; left: calc(100% + 0px); } /* Adjusted slightly to match SVG points better */
     .component-in-workspace[data-component-type="battery"] .connection-point[data-terminal="minus"] { top: 50%; left: -0px; } /* Adjusted slightly */
    .component-in-workspace[data-component-type="resistor"] .connection-point[data-terminal="1"] { top: 50%; left: -0px; } /* Adjusted slightly */
    .component-in-workspace[data-component-type="resistor"] .connection-point[data-terminal="2"] { top: 50%; left: calc(100% + 0px); } /* Adjusted slightly */
    .component-in-workspace[data-component-type="led"] .connection-point[data-terminal="anode"] { top: 50%; left: -0px; } /* Adjusted slightly */
    .component-in-workspace[data-component-type="led"] .connection-point[data-terminal="cathode"] { top: 50%; left: calc(100% + 0px); } /* Adjusted slightly */


     .connecting {
         background-color: rgba(255, 165, 0, 0.8) !important; /* Orange when starting connection */
         transform: translate(-50%, -50%) scale(1.2); /* Grow slightly */
         box-shadow: 0 0 8px rgba(255, 165, 0, 0.5);
     }

     svg line {
         stroke: #333; /* Darker lines */
         stroke-width: 3; /* Thicker lines */
         pointer-events: none; /* Lines are not interactive (for simplicity) */
         fill: none;
     }

    button {
        margin-top: 15px;
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #007bff;
        color: white;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
    }

    button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
     button:active {
         transform: translateY(0);
         box-shadow: none;
     }


    #feedback-area {
        margin-top: 20px;
        padding: 15px; /* More padding */
        border-radius: 8px;
        min-height: 1.5em; /* Reserve space */
        text-align: center;
        font-weight: bold;
         transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
    }

    .feedback-success {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }

    .feedback-error {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }

    #explanation-area {
        margin-top: 30px;
        border-top: 1px solid #e0e0e0;
        padding-top: 20px;
         font-family: 'Arial', sans-serif;
         line-height: 1.6;
    }

    #explanation-area h2, #explanation-area h3 {
        color: #0056b3; /* Theme color */
        margin-bottom: 10px;
    }

    #explanation-area h3 {
        margin-top: 15px;
        border-bottom: 1px dashed #eee;
        padding-bottom: 5px;
    }

    #explanation-area ul {
        list-style-type: disc;
        margin-right: 25px; /* RTL list indent */
        padding-right: 0;
    }

    #explanation-area li {
        margin-bottom: 10px;
    }

     #explanation-area strong {
         color: #333;
     }

    /* LED lit simulation */
    .component-in-workspace[data-component-type="led"].led-lit {
        background-color: #fffacd; /* Soft yellow */
        box-shadow: 0 0 15px 5px #ffcc00; /* Brighter glow */
        animation: pulse-glow 1.5s infinite alternate; /* Add animation */
    }

     @keyframes pulse-glow {
         from { box-shadow: 0 0 10px 3px #ffcc00; }
         to { box-shadow: 0 0 20px 8px #ffdd00; }
     }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const workspace = document.getElementById('workspace');
        const toolboxItems = document.querySelectorAll('.component-toolbox');
        const checkButton = document.getElementById('check-button');
        const feedbackArea = document.getElementById('feedback-area');
        const connectionSvg = document.getElementById('connection-svg');
        const showExplanationButton = document.getElementById('show-explanation-button');
        const explanationArea = document.getElementById('explanation-area');

        let componentsInWorkspace = []; // { id, type, el, x, y, points: { terminal: pointId, ... } }
        let connections = []; // { point1: pointId, point2: pointId, lineEl: svgLineElement }
        let connectingPoint = null; // To store the first clicked connection point element

        let componentIdCounter = 0;
        let connectionPointIdCounter = 0;
        let dragTarget = null; // Element being dragged

        // --- Drag and Drop functionality ---
        toolboxItems.forEach(item => {
            item.addEventListener('dragstart', (e) => {
                dragTarget = item; // Identify the element being dragged from toolbox
                e.dataTransfer.setData('text/plain', item.dataset.componentType);
                e.dataTransfer.effectAllowed = 'copy';
                 // Add a ghost image if possible, or just rely on default
            });
        });

        workspace.addEventListener('dragover', (e) => {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'copy';
             workspace.style.backgroundColor = '#eef'; // Visual feedback for dragover
        });

        workspace.addEventListener('dragleave', () => {
             workspace.style.backgroundColor = '#ffffff'; // Reset background
        });


        workspace.addEventListener('drop', (e) => {
            e.preventDefault();
             workspace.style.backgroundColor = '#ffffff'; // Reset background
            const rect = workspace.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const type = e.dataTransfer.getData('text/plain');

            // Prevent dropping multiple components of the same type if only one is needed (for this specific circuit)
             const existingComp = componentsInWorkspace.find(c => c.type === type);
             if (existingComp) {
                 feedbackArea.textContent = `יש כבר רכיב מסוג ${type} במשטח העבודה. למעגל זה דרוש רק אחד מכל סוג.`;
                 feedbackArea.classList.add('feedback-error');
                 return;
             }


            addComponentToWorkspace(type, x, y);
        });

        function addComponentToWorkspace(type, x, y) {
            const componentId = `comp-${componentIdCounter++}`;
            const componentEl = document.createElement('div');
            componentEl.classList.add('component-in-workspace');
            componentEl.dataset.componentType = type;
            componentEl.dataset.componentId = componentId;

             // Add component image/text based on type
            let imgHtml = '';
            let componentText = '';
            let connectionPointsConfig = {}; // { terminalName: { left: '%', top: '%'}, ...} - Using left/top percentages for flexibility

            switch(type) {
                case 'battery':
                    imgHtml = '<img src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 50 30\'%3E%3Crect x=\'5\ י=\'10\' width=\'40\' height=\'10\' fill=\'%23555\'/%3E%3Cline x1=\'10\' י1=\'15\' x2=\'10\' י2=\'25\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'15\ י1=\'15\' x2=\'15\' י2=\'25\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'20\ י1=\'15\' x2=\'20\' י2=\'25\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'25\ י1=\'15\' x2=\'25\' י2=\'25\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'30\ י1=\'15\' x2=\'30\' י2=\'25\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'35\ י1=\'15\' x2=\'35\' י2=\'25\' stroke=\'black\' stroke-width=\'2\'/%3E%3Crect x=\'40\ י=\'8\' width=\'5\' height=\'14\' fill=\'%23555\'/%3E%3Ctext x=\'15\ י=\'18\' font-size=\'10\' text-anchor=\'middle\' fill=\'white\'%3E-%3C/text%3E%3Ctext x=\'42.5\ י=\'18\' font-size=\'10\' text-anchor=\'middle\' fill=\'white\'%3E%2B%3C/text%3E%3C/svg%3E" alt="סוללה">';
                    componentText = 'סוללה';
                    connectionPointsConfig = { 'minus': { left: '0%', top: '50%' }, 'plus': { left: '100%', top: '50%' } };
                    break;
                case 'resistor':
                     imgHtml = '<img src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 50 30\'%3E%3Cpath d=\'M5 15 L10 10 L15 20 L20 10 L25 20 L30 10 L35 20 L40 15\' fill=\'none\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'5\' י1=\'15\' x2=\'0\' י2=\'15\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'40\' י1=\'15\' x2=\'45\' י2=\'15\' stroke=\'black\' stroke-width=\'2\'/%3E%3C/svg%3E" alt="נגד">';
                    componentText = 'נגד';
                     connectionPointsConfig = { '1': { left: '0%', top: '50%' }, '2': { left: '100%', top: '50%' } };
                    break;
                case 'led':
                     imgHtml = '<img src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 50 30\'%3E%3Cline x1=\'5\' י1=\'15\' x2=\'15\' י2=\'15\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cpolygon points=\'15,15 30,10 30,20\' fill=\'none\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'30\' י1=\'10\' x2=\'30\' י2=\'20\' stroke=\'black\' stroke-width=\'2\'/%3E%3Cline x1=\'30\' י1=\'15\' x2=\'45\' י2=\'15\' stroke=\'black\' stroke-width=\'2\'/%3E%3C/svg%3E" alt="LED">';
                    componentText = 'LED';
                     connectionPointsConfig = { 'anode': { left: '0%', top: '50%' }, 'cathode': { left: '100%', top: '50%' } };
                    break;
                 default:
                     return; // Unknown component type
            }

            componentEl.innerHTML = imgHtml + `<p>${componentText}</p>`;

            // Position the element relative to the workspace
            // Use getBoundingClientRect to get the *actual* dimensions after adding content
             // Position it temporarily to measure
             componentEl.style.visibility = 'hidden';
             componentEl.style.position = 'absolute';
             componentEl.style.left = '0px';
             componentEl.style.top = '0px';
             workspace.appendChild(componentEl);

             const compWidth = componentEl.offsetWidth;
             const compHeight = componentEl.offsetHeight;

            // Set final position, centered on the drop point
            componentEl.style.left = `${x - compWidth / 2}px`;
            componentEl.style.top = `${y - compHeight / 2}px`;
            componentEl.style.visibility = 'visible';
            componentEl.style.position = 'absolute'; // Restore position style


            // Add connection points
            const points = {}; // { terminal: pointId }
            for (const terminal in connectionPointsConfig) {
                const pointId = `point-${connectionPointIdCounter++}`;
                const pointEl = document.createElement('div');
                pointEl.classList.add('connection-point');
                pointEl.dataset.pointId = pointId;
                pointEl.dataset.componentId = componentId;
                pointEl.dataset.terminal = terminal; // e.g., 'plus', 'minus', 'anode', 'cathode', '1', '2'
                pointEl.style.top = connectionPointsConfig[terminal].top;
                pointEl.style.left = connectionPointsConfig[terminal].left;

                pointEl.addEventListener('click', handleConnectionPointClick);
                 // Prevent dragging component when dragging from a point
                 pointEl.addEventListener('mousedown', (e) => e.stopPropagation());
                 pointEl.addEventListener('touchstart', (e) => e.stopPropagation()); // For touch devices


                componentEl.appendChild(pointEl);
                points[terminal] = pointId;
            }


             // Make the component itself draggable within the workspace
             let isDraggingComponent = false;
             let dragOffsetX, dragOffsetY;

            componentEl.addEventListener('mousedown', (e) => {
                 if (e.target.classList.contains('connection-point')) return; // Don't drag component if clicked on point
                 isDraggingComponent = true;
                 componentEl.classList.add('dragging'); // Visual feedback
                 const compRect = componentEl.getBoundingClientRect();
                 dragOffsetX = e.clientX - compRect.left;
                 dragOffsetY = e.clientY - compRect.top;

                 // Add temporary event listeners to document for dragging
                 document.addEventListener('mousemove', handleComponentMouseMove);
                 document.addEventListener('mouseup', handleComponentMouseUp);
             });

             // Touch events for dragging
             componentEl.addEventListener('touchstart', (e) => {
                 if (e.target.classList.contains('connection-point')) return;
                 isDraggingComponent = true;
                 componentEl.classList.add('dragging');
                 const touch = e.touches[0];
                 const compRect = componentEl.getBoundingClientRect();
                 dragOffsetX = touch.clientX - compRect.left;
                 dragOffsetY = touch.clientY - compRect.top;

                 document.addEventListener('touchmove', handleComponentTouchMove, { passive: false });
                 document.addEventListener('touchend', handleComponentTouchEnd);
                 e.preventDefault(); // Prevent default touch behavior like scrolling
             });


             function handleComponentMouseMove(e) {
                 if (!isDraggingComponent) return;

                 const workspaceRect = workspace.getBoundingClientRect();
                 let newX = e.clientX - workspaceRect.left - dragOffsetX;
                 let newY = e.clientY - workspaceRect.top - dragOffsetY;

                 // Clamp to workspace boundaries
                 newX = Math.max(0, Math.min(newX, workspaceRect.width - componentEl.offsetWidth));
                 newY = Math.max(0, Math.min(newY, workspaceRect.height - componentEl.offsetHeight));

                 componentEl.style.left = `${newX}px`;
                 componentEl.style.top = `${newY}px`;

                 // Update connection lines while dragging
                 updateConnections(componentId);
             }

             function handleComponentMouseUp() {
                 if (isDraggingComponent) {
                     isDraggingComponent = false;
                     componentEl.classList.remove('dragging');
                     componentEl.style.zIndex = 10; // Reset z-index

                      // Find the component in the array and update its stored position (optional, but good practice)
                      const compData = componentsInWorkspace.find(c => c.id === componentId);
                      if(compData) {
                         const compRect = componentEl.getBoundingClientRect();
                         const workspaceRect = workspace.getBoundingClientRect();
                         // Store relative position
                         compData.x = compRect.left - workspaceRect.left;
                         compData.y = compRect.top - workspaceRect.top;
                      }

                     // Clean up event listeners
                     document.removeEventListener('mousemove', handleComponentMouseMove);
                     document.removeEventListener('mouseup', handleComponentMouseUp);
                 }
             }

             function handleComponentTouchMove(e) {
                 if (!isDraggingComponent || e.touches.length !== 1) return;
                 const touch = e.touches[0];

                 const workspaceRect = workspace.getBoundingClientRect();
                 let newX = touch.clientX - workspaceRect.left - dragOffsetX;
                 let newY = touch.clientY - workspaceRect.top - dragOffsetY;

                 // Clamp to workspace boundaries
                 newX = Math.max(0, Math.min(newX, workspaceRect.width - componentEl.offsetWidth));
                 newY = Math.max(0, Math.min(newY, workspaceRect.offsetHeight - componentEl.offsetHeight));


                 componentEl.style.left = `${newX}px`;
                 componentEl.style.top = `${newY}px`;

                 updateConnections(componentId);
                 e.preventDefault(); // Prevent scrolling
             }

             function handleComponentTouchEnd() {
                 if (isDraggingComponent) {
                     isDraggingComponent = false;
                      componentEl.classList.remove('dragging');
                      componentEl.style.zIndex = 10; // Reset z-index

                       const compData = componentsInWorkspace.find(c => c.id === componentId);
                       if(compData) {
                          const compRect = componentEl.getBoundingClientRect();
                          const workspaceRect = workspace.getBoundingClientRect();
                          compData.x = compRect.left - workspaceRect.left;
                          compData.y = compRect.top - workspaceRect.top;
                       }

                     document.removeEventListener('touchmove', handleComponentTouchMove);
                     document.removeEventListener('touchend', handleComponentTouchEnd);
                 }
             }


            componentsInWorkspace.push({
                id: componentId,
                type: type,
                el: componentEl,
                x: x - compWidth / 2, // Store actual position
                y: y - compHeight / 2,
                points: points // Store pointId mapped to terminal name
            });
        }

        function handleConnectionPointClick(e) {
            const pointEl = e.target;
            const pointId = pointEl.dataset.pointId;

            if (!connectingPoint) {
                // First click: Start a connection
                connectingPoint = {
                    id: pointId,
                    el: pointEl
                };
                 pointEl.classList.add('connecting'); // Visual feedback
                 // Maybe add a temporary line following the cursor? Advanced feature, skip for now.

                 // Add a temporary mousemove listener to draw a line preview
                 // This requires significant SVG/JS work to draw and update a temporary line element.
                 // Sticking to just visual point feedback for now.

            } else {
                // Second click: End a connection
                const point1Id = connectingPoint.id;
                const point2Id = pointId;
                const point1El = connectingPoint.el;

                 // Prevent connecting a point to itself
                 if (point1Id === point2Id) {
                      point1El.classList.remove('connecting');
                      connectingPoint = null;
                      feedbackArea.textContent = 'לא ניתן לחבר נקודת חיבור לעצמה.';
                      feedbackArea.classList.add('feedback-error');
                      return;
                 }

                 // Prevent connecting two points on the same component
                 if (point1El.dataset.componentId === pointEl.dataset.componentId) {
                     point1El.classList.remove('connecting');
                     connectingPoint = null;
                      feedbackArea.textContent = 'לא ניתן לחבר שתי נקודות על אותו רכיב.';
                      feedbackArea.classList.add('feedback-error');
                     return;
                 }

                // Check if either point is already connected *to anything else*
                 const p1Connections = connections.filter(conn => conn.point1 === point1Id || conn.point2 === point1Id);
                 const p2Connections = connections.filter(conn => conn.point1 === point2Id || conn.point2 === point2Id);

                 if (p1Connections.length > 0 || p2Connections.length > 0) {
                     point1El.classList.remove('connecting');
                     connectingPoint = null;
                      feedbackArea.textContent = 'נקודת חיבור אחת או יותר כבר מחוברת. למעגל טורי פשוט כל נקודה מתחברת רק פעם אחת.';
                      feedbackArea.classList.add('feedback-error');
                     return;
                 }


                // Check if this connection already exists (either direction) - Redundant with the above check for single connection per point, but good double-check.
                const exists = connections.some(conn =>
                    (conn.point1 === point1Id && conn.point2 === point2Id) ||
                    (conn.point1 === point2Id && conn.point2 === point1Id)
                );

                if (!exists) {
                    // Add the new connection
                     connections.push({ point1: point1Id, point2: point2Id });
                     redrawConnections();
                     feedbackArea.textContent = ''; // Clear feedback on successful connection
                     feedbackArea.classList.remove('feedback-error');
                 } else {
                      feedbackArea.textContent = 'החיבור הזה כבר קיים!';
                      feedbackArea.classList.add('feedback-error');
                 }


                point1El.classList.remove('connecting');
                connectingPoint = null; // Reset
            }
        }

         function redrawConnections() {
             // Clear existing lines
             connectionSvg.innerHTML = '';

             connections.forEach(conn => {
                 const point1El = document.querySelector(`[data-point-id="${conn.point1}"]`);
                 const point2El = document.querySelector(`[data-point-id="${conn.point2}"]`);

                 if (point1El && point2El) {
                     const p1Rect = point1El.getBoundingClientRect();
                     const p2Rect = point2El.getBoundingClientRect();
                     const workspaceRect = workspace.getBoundingClientRect();

                     // Calculate center coordinates relative to SVG (which is relative to workspace)
                     // Adjust slightly to connect visually to the point center circle
                     const x1 = p1Rect.left + p1Rect.width / 2 - workspaceRect.left;
                     const y1 = p1Rect.top + p1Rect.height / 2 - workspaceRect.top;
                     const x2 = p2Rect.left + p2Rect.width / 2 - workspaceRect.left;
                     const y2 = p2Rect.top + p2Rect.height / 2 - workspaceRect.top;

                     const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                     line.setAttribute('x1', x1);
                     line.setAttribute('y1', y1);
                     line.setAttribute('x2', x2);
                     line.setAttribute('y2', y2);
                      // Add data attributes to the line for potential future use (e.g., deletion)
                      line.dataset.point1Id = conn.point1;
                      line.dataset.point2Id = conn.point2;

                     connectionSvg.appendChild(line);

                     // Store the line element reference in the connection object
                     // Find the connection in the array and add the line element
                     const connection = connections.find(c => c.point1 === conn.point1 && c.point2 === conn.point2);
                     if (connection) {
                          connection.lineEl = line;
                     }
                 }
             });
         }

         // Helper to update lines connected to a component being dragged
         function updateConnections(componentId) {
             // Simplest way is to redraw all lines
              redrawConnections();
         }

        // --- Validation and Simulation ---
        checkButton.addEventListener('click', () => {
            feedbackArea.classList.remove('feedback-success', 'feedback-error');
            feedbackArea.textContent = '';

            // Reset LED state before checking
             const ledEl = componentsInWorkspace.find(c => c.type === 'led')?.el;
             if (ledEl) ledEl.classList.remove('led-lit');


            // 1. Check required components count (exactly one of each)
            const requiredComponents = { battery: 1, resistor: 1, led: 1 };
            const componentCounts = componentsInWorkspace.reduce((acc, comp) => {
                acc[comp.type] = (acc[comp.type] || 0) + 1;
                return acc;
            }, {});

            let componentsOK = true;
            for (const type in requiredComponents) {
                if (componentCounts[type] !== requiredComponents[type]) {
                    componentsOK = false;
                    feedbackArea.textContent = `חסרים רכיבים או שיש יותר מדי: דרוש בדיוק 1 סוללה, 1 נגד, 1 LED. `;
                    feedbackArea.classList.add('feedback-error');
                    return; // Stop check if component count is wrong
                }
            }

            // Find the elements once counts are confirmed
            const battery = componentsInWorkspace.find(c => c.type === 'battery');
            const resistor = componentsInWorkspace.find(c => c.type === 'resistor');
            const led = componentsInWorkspace.find(c => c.type === 'led');

            // Map component terminals to point IDs
            const batPlusId = battery.points.plus;
            const batMinusId = battery.points.minus;
            const res1Id = resistor.points['1'];
            const res2Id = resistor.points['2'];
            const ledAnodeId = led.points.anode;
            const ledCathodeId = led.points.cathode;

             // 2. Check connections quantity per point
             const allPoints = [batPlusId, batMinusId, res1Id, res2Id, ledAnodeId, ledCathodeId];
             let connectionCountsOK = true;
             for(const pointId of allPoints) {
                 const count = connections.filter(conn => conn.point1 === pointId || conn.point2 === pointId).length;
                 if (count !== 1) {
                     connectionCountsOK = false;
                     // More specific feedback could identify the problematic point
                     break;
                 }
             }

            if (!connectionCountsOK) {
                 feedbackArea.textContent = 'שגיאה בחיבורים: כל נקודת חיבור צריכה להיות מחוברת לנקודה אחת בלבד כדי ליצור מעגל טורי.';
                feedbackArea.classList.add('feedback-error');
                 return;
            }


            // 3. Check specific connections form the correct loop
            // Expected sequence: Bat+ -> Resistor -> LED Anode -> LED Cathode -> Bat-
            // We need to check the *pairs* that exist match this sequence logic.

             const isConnected = (p1Id, p2Id) => connections.some(conn =>
                 (conn.point1 === p1Id && conn.point2 === p2Id) ||
                 (conn.point1 === p2Id && conn.point2 === p1Id)
             );

             let pathCorrect = false;

             // Check Bat+ to Resistor (either end)
             const batPlusToResistor1 = isConnected(batPlusId, res1Id);
             const batPlusToResistor2 = isConnected(batPlusId, res2Id);

             if (batPlusToResistor1 || batPlusToResistor2) {
                 const resistorPointConnectedToBatPlus = batPlusToResistor1 ? res1Id : res2Id;
                 const otherResistorPoint = batPlusToResistor1 ? res2Id : res1Id;

                 // Check the *other* Resistor end to LED Anode
                 const resToLedAnode = isConnected(otherResistorPoint, ledAnodeId);

                 if (resToLedAnode) {
                      // Check LED Cathode to Bat-
                      const ledCathodeToBatMinus = isConnected(ledCathodeId, batMinusId);

                      if (ledCathodeToBatMinus) {
                          pathCorrect = true; // Found the complete correct path
                      } else {
                           feedbackArea.textContent = 'שגיאה בחיבור: קתודת ה-LED צריכה להתחבר לקוטב השלילי של הסוללה.';
                           feedbackArea.classList.add('feedback-error');
                           return;
                      }
                 } else {
                      feedbackArea.textContent = 'שגיאה בחיבור: הנגד צריך להתחבר לאנודת ה-LED (הצד ללא הפס בסמל).';
                      feedbackArea.classList.add('feedback-error');
                      return;
                 }

             } else {
                  feedbackArea.textContent = 'שגיאה בחיבור: הקוטב החיובי של הסוללה צריך להתחבר לאחד מצידי הנגד.';
                  feedbackArea.classList.add('feedback-error');
                  return;
             }


            // Final check: if path is correct and counts are OK, it's a success!
            if (pathCorrect && connectionCountsOK && componentsOK) {
                 feedbackArea.textContent = 'מצוין! פענחת את הסכמה והרכבת את המעגל בהצלחה. ה-LED נדלק!';
                 feedbackArea.classList.add('feedback-success');
                 // Activate simulation effect
                 if (ledEl) {
                     ledEl.classList.add('led-lit');
                 }
            } else {
                 // Fallback error if something was missed (shouldn't happen with the checks above)
                 feedbackArea.textContent = 'שגיאה בחיבורים. ודא שהמעגל שלם ומחובר כהלכה לפי התרשים: סוללה (+)->נגד->LED (אנודה)->LED (קתודה)->סוללה (-).';
                 feedbackArea.classList.add('feedback-error');
            }
        });


        // --- Explanation Toggle ---
        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationArea.style.display === 'none';
            explanationArea.style.display = isHidden ? 'block' : 'none';
            showExplanationButton.textContent = isHidden ? 'הסתר מדריך הפענוח' : 'הצגת מדריך הפענוח';
        });

        // Optional: Add a way to clear workspace / delete components/connections
        // This requires more complex event handling (e.g., double click to remove, or a dedicated button)
        // Given the strict structure constraint, let's omit for now.
        // A simple "Clear Workspace" button:
        /*
         const clearButton = document.createElement('button');
         clearButton.textContent = 'נקה משטח עבודה';
         clearButton.addEventListener('click', () => {
             componentsInWorkspace.forEach(comp => comp.el.remove());
             componentsInWorkspace = [];
             connections = [];
             connectionSvg.innerHTML = '';
             connectingPoint = null;
             feedbackArea.textContent = '';
             feedbackArea.classList.remove('feedback-success', 'feedback-error');
         });
         simulationContainer.appendChild(clearButton); // Add it somewhere appropriate
        */


        // Initial state setup (optional: place a component or two by default?) - No, start empty as a game.
         redrawConnections(); // Ensure SVG is ready
    });
</script>
---
```