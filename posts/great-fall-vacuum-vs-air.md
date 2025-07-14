---
title: "הנפילה הגדולה: ריק מול אוויר"
english_slug: great-fall-vacuum-vs-air
category: "מדעים מדויקים / פיזיקה"
tags: כבידה, תנועה, התנגדות אוויר, ניוטון, גלילאו
---
# הנפילה הגדולה: ריק מול אוויר

דמיינו את הסיטואציה: אתם עומדים בראש מגדל גבוה במיוחד, מחזיקים ביד אחת כדור באולינג כבד וביד השנייה נוצה קלילה. מה יקרה אם תשחררו את שניהם בו-זמנית? האינטואיציה שלנו צועקת: "ברור שכדור הבאולינג יתרסק למטה הרבה לפני הנוצה!". אבל האם האינטואיציה תמיד צודקת? האם זה נכון בכל מצב? בואו נצא למסע מדעי קצר כדי לגלות!

<div class="simulation-container">
    <div class="controls">
        <div class="control-group">
            <label for="object1">עצם 1:</label>
            <select id="object1">
                <option value="bowling-ball">כדור באולינג</option>
                <option value="tennis-ball">כדור טניס</option>
                <option value="feather">נוצה</option>
                <option value="brick">לבנה</option>
            </select>
        </div>
        <div class="control-group">
            <label for="object2">עצם 2:</label>
            <select id="object2">
                <option value="tennis-ball">כדור טניס</option>
                <option value="bowling-ball">כדור באולינג</option>
                <option value="feather">נוצה</option>
                <option value="brick">לבנה</option>
            </select>
        </div>
        <div class="control-group">
            <label for="mode">מצב:</label>
            <select id="mode">
                <option value="vacuum">ריק מוחלט</option>
                <option value="air">עם התנגדות אוויר</option>
            </select>
        </div>
        <button id="startButton">התחל נפילה!</button>
        <button id="resetButton" disabled>איפוס</button>
    </div>
    <div class="simulation-area" id="simulationArea">
        <div class="ground"></div>
        <div id="timerDisplay" class="timer-display">0.00 שניות</div>
        <div id="object1Display" class="object-display display-left"></div>
        <div id="object2Display" class="object-display display-right"></div>
        <!-- Objects will be added here by JS -->
    </div>
     <div id="resultDisplay" class="result-display"></div>
</div>

<button id="toggleExplanation" class="toggle-button">הצג/הסתר את סודות הפיזיקה מאחורי הנפילה</button>

<div id="explanation" class="explanation-content" style="display: none;">
    <h2>הסבר מדעי: נפילה חופשית והכוח הבלתי נראה של האוויר</h2>

    <h3>כוח הכבידה - המנוע של הנפילה</h3>
    <p>אחד החוקים המופלאים ביקום הוא חוק הכבידה. כדור הארץ מושך אליו כל גוף עם כוח שעוצמתו תלויה במסה של הגוף ובמסה של כדור הארץ (וגם במרחק ביניהם). מה שמרתק הוא שכוח הכבידה מאיץ את כל העצמים באותה מידה! תאוצת הנפילה החופשית, אותה אנו מסמנים באות g (בערך 9.8 מטר לשנייה בריבוע על פני הים), זהה לכל הגופים באותו מקום ובאותו גובה. זה אומר שאם רק כוח הכבידה פועל, כדור באולינג ונוצה אמורים לצבור מהירות באותו קצב ולהגיע לקרקע יחד.</p>

    <h3>התנגדות אוויר - הבלם המעכב</h3>
    <p>אבל רגע, בניסוי היומיומי נוצה נופלת לאט הרבה יותר מכדור באולינג. למה? התשובה טמונה ב"אוויר" עצמו! כשאנחנו נעים דרך האוויר, חלקיקי האוויר מתנגשים בנו ויוצרים כוח התנגדות, הנקרא גם גרר (Drag). כוח הגרר תמיד פועל בכיוון המנוגד לכיוון התנועה ומנסה להאט את הגוף. עוצמתו של כוח הגרר תלויה בכמה דברים: כמה מהר הגוף נע (ככל שמהירות גבוהה יותר, כך הגרר גדול יותר), צורת הגוף (עד כמה הוא "אווירודינמי"), גודל שטח הפנים של הגוף שפונה לכיוון התנועה, וגם צפיפות האוויר.</p>

    <h3>הדו-קרב: כבידה מול גרר</h3>
    <p>כאשר גוף נופל באוויר, פועלים עליו שני כוחות עיקריים: כוח הכבידה שמושך אותו למטה, וכוח הגרר שדוחף אותו למעלה. הכוח השקול הוא ההפרש בין שני הכוחות הללו. לפי החוק השני של ניוטון (F=ma), הכוח השקול קובע את התאוצה של הגוף. ככל שכוח הגרר גדול יותר יחסית לכוח הכבידה, כך התאוצה תהיה קטנה יותר והגוף יואט יותר.</p>

    <h3>למה הנוצה מפסידה באוויר?</h3>
    <p>לנוצה יש מסה קטנה מאוד, אבל שטח פנים גדול יחסית למסתה. כדור באולינג, לעומת זאת, הוא כבד מאוד ויש לו שטח פנים קטן יחסית למסתו. כוח הכבידה על כדור הבאולינג גדול הרבה יותר מכוח הכבידה על הנוצה. עם זאת, כוח הגרר שנוצר במהלך הנפילה גדל עם שטח הפנים ועם המהירות. עבור הנוצה הקלה, כוח הגרר הופך במהירות למשמעותי מאוד יחסית לכוח הכבידה הקטן הפועל עליה. הוא "בולע" חלק גדול מהתאוצה, ולכן היא נופלת לאט. כדור הבאולינג הכבד צריך להגיע למהירות גבוהה הרבה יותר כדי שכוח הגרר יגיע לגודל משמעותי יחסית לכוח הכבידה הגדול הפועל עליו. לכן הוא מאיץ מהר יותר ונופל מהר יותר באוויר.</p>

    <h3>מהירות סופית - הגבול העליון למהירות הנפילה</h3>
    <p>ככל שגוף נופל מהר יותר, כך כוח הגרר גדל. בשלב מסוים, עבור עצמים רבים שנופלים באוויר, כוח הגרר גדל עד שהוא משתווה בדיוק לכוח הכבידה. במצב זה, הכוח השקול הוא אפס! לפי חוק ניוטון השני, אם הכוח השקול הוא אפס, התאוצה היא אפס. הגוף מפסיק להאיץ וממשיך ליפול במהירות קבועה הנקראת "מהירות סופית" (Terminal Velocity). לכל גוף יש מהירות סופית שונה, התלויה במסה שלו, בצורתו ובשטח הפנים שלו. צנחנים משתמשים במצנח כדי להגדיל באופן דרמטי את שטח הפנים שלהם ולהגיע למהירות סופית נמוכה מספיק כדי לנחות בשלום!</p>

    <h3>הניסויים המפורסמים בהיסטוריה</h3>
    <p>את הרעיון שעצמים נופלים באותה תאוצה בהיעדר אוויר הגה לראשונה גלילאו גליליי במאה ה-16. הוא התנגד לתפיסה של אריסטו (שהייתה מקובלת אלפיים שנה!) שעצמים כבדים נופלים מהר יותר. למרות הסיפור הפופולרי על השלכת עצמים ממגדל פיזה, רוב ההיסטוריונים סבורים שגלילאו לא ביצע בפועל את הניסוי המפורסם שם, אלא הגיע למסקנותיו באמצעות ניסויים אחרים וחשיבה מעמיקה. אבל ההדגמה הדרמטית ביותר התרחשה באמת בשנת 1971, על הירח! האסטרונאוט דייוויד סקוט ממשימת אפולו 15 שיחרר פטיש ונוצה בו-זמנית על פני הירח, שלו אין אטמוספירה (כלומר, הוא ריק מוחלט). וכצפוי, הפטיש והנוצה פגעו בקרקע הירח באותו רגע בדיוק, כמו שגלילאו חזה מאות שנים לפני כן!</p>
</div>

<style>
    /* General container and layout */
    .simulation-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        text-align: right;
        margin: 25px auto;
        padding: 20px;
        border: 1px solid #d0d0d0;
        border-radius: 12px;
        background: linear-gradient(to bottom right, #ffffff, #f0f0f0);
        max-width: 750px;
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        overflow: hidden; /* Contain floating elements */
    }

    /* Controls Section */
    .controls {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        margin-bottom: 25px;
        align-items: flex-end;
        justify-content: center; /* Center controls */
        background-color: #e9ecef;
        padding: 15px;
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    .control-group {
        display: flex;
        flex-direction: column;
        min-width: 120px; /* Ensure controls have minimum width */
    }

    .controls label {
        margin-bottom: 6px;
        font-weight: bold;
        font-size: 0.95em;
        color: #333;
    }

    .controls select, .controls button {
        padding: 10px 12px;
        border: 1px solid #a0a0a0;
        border-radius: 6px;
        font-size: 1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
     .controls select:focus {
         border-color: #007bff;
         box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
         outline: none;
     }

    .controls button {
        background-color: #007bff;
        color: white;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .controls button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-1px);
    }

    .controls button:active:not(:disabled) {
         transform: translateY(0);
         box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
    }

    .controls button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
    }

    /* Simulation Area */
    .simulation-area {
        width: calc(100% - 40px); /* Adjust width for padding/border if needed */
        height: 450px; /* Increased height for better visualization */
        border: 2px solid #a0a0a0;
        background: linear-gradient(to bottom, #87ceeb, #e0f7fa); /* Sky gradient */
        position: relative;
        overflow: hidden; /* Hide objects below ground */
        margin: 0 auto; /* Center the simulation area */
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }

    .ground {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 40px; /* Ground height */
        background: linear-gradient(to top, #5a3a2b, #8b4513); /* Brown earth gradient */
        z-index: 1; /* Make sure it's above objects */
        border-top: 2px solid #4a2a1b;
    }

     .timer-display {
        position: absolute;
        top: 15px;
        left: 50%; /* Center horizontally */
        transform: translateX(-50%);
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        padding: 8px 15px;
        border-radius: 5px;
        font-size: 1.1em;
        font-weight: bold;
        z-index: 15; /* Above everything else */
     }

    .object-display {
        position: absolute;
        top: 10px;
        font-size: 0.9em;
        color: #333;
        z-index: 10; /* Above ground and objects */
        background-color: rgba(255, 255, 255, 0.8);
        padding: 5px 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }

    .display-left { left: 10px; }
    .display-right { right: 10px; }


    /* Object styles (these will be applied via JS) */
    .falling-object {
        position: absolute;
        top: 0; /* Start at the top */
        width: 30px; /* Default size */
        height: 30px; /* Default size */
        z-index: 5; /* Below display, above ground */
        transition: none; /* JS handles position, avoid CSS transitions */
        box-sizing: border-box; /* Include padding/border in size */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5em; /* For potential icons */
        color: rgba(0,0,0,0.8);
    }

    /* Specific object visual styles */
    /* Use Unicode characters or simple CSS shapes for icons */
    .object-bowling-ball {
        width: 45px; height: 45px;
        background: radial-gradient(circle at 30% 30%, #888, #333);
        border-radius: 50%;
        border: 2px solid #222;
        color: transparent; /* Hide potential icon */
        left: 30%; /* Initial position */
        transform: translateX(-50%);
    }

    .object-tennis-ball {
        width: 30px; height: 30px;
        background-color: #90ee90; /* Light green */
        border-radius: 50%;
        border: 1px solid #55aa55;
        left: 70%; /* Initial position */
        transform: translateX(-50%);
        box-shadow: 0 0 5px rgba(144, 238, 144, 0.5);
    }

    .object-feather {
        width: 20px; height: 50px; /* Elongated */
        background: linear-gradient(to right, #eee, #fff, #eee);
        border: 1px solid #ccc;
        border-radius: 0;
        left: 30%; /* Initial position */
        transform: translateX(-50%) rotate(10deg); /* Slightly tilted */
        opacity: 0.9;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }

    .object-brick {
        width: 40px; height: 25px;
        background: linear-gradient(to bottom, #b22222, #8b0000); /* Red brick gradient */
        border-radius: 3px;
        left: 70%; /* Initial position */
        transform: translateX(-50%);
        border: 1px solid #660000;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }

    .object-landed {
        /* Add a subtle effect on landing */
        animation: subtleBounce 0.3s ease-out forwards;
    }

    @keyframes subtleBounce {
        0% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0); }
    }


    /* Result Display */
    .result-display {
        text-align: center;
        margin-top: 20px;
        font-size: 1.3em;
        font-weight: bold;
        color: #0056b3;
        min-height: 1.5em; /* Reserve space */
    }

    /* Explanation Section */
    .toggle-button {
        display: block;
        margin: 25px auto;
        padding: 12px 25px;
        background-color: #17a2b8; /* Info blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .toggle-button:hover {
        background-color: #138496;
        transform: translateY(-1px);
    }
    .toggle-button:active {
         transform: translateY(0);
         box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
    }


    .explanation-content {
        direction: rtl;
        text-align: right;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #d0d0d0;
        border-radius: 12px;
        background-color: #fefefe;
        max-width: 750px;
        box-shadow: 0 5px 10px rgba(0,0,0,0.08);
        line-height: 1.7;
        color: #333;
    }

    .explanation-content h2, .explanation-content h3 {
        color: #0056b3;
        margin-top: 25px;
        margin-bottom: 12px;
        border-bottom: 2px solid #eee;
        padding-bottom: 8px;
        font-weight: bold;
    }
     .explanation-content h2 {
         font-size: 1.8em;
     }
     .explanation-content h3 {
         font-size: 1.4em;
         color: #17a2b8;
     }

    .explanation-content p {
        margin-bottom: 18px;
        font-size: 1.1em;
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const simulationArea = document.getElementById('simulationArea');
        const object1Select = document.getElementById('object1');
        const object2Select = document.getElementById('object2');
        const modeSelect = document.getElementById('mode');
        const startButton = document.getElementById('startButton');
        const resetButton = document.getElementById('resetButton');
        const timerDisplay = document.getElementById('timerDisplay');
        const object1Display = document.getElementById('object1Display');
        const object2Display = document.getElementById('object2Display');
        const resultDisplay = document.getElementById('resultDisplay');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');

        const GROUND_HEIGHT_PX = 40; // Must match .ground height in CSS
        const simHeightPx = simulationArea.clientHeight - GROUND_HEIGHT_PX; // Total pixels for falling area
        const simHeightMeters = 150; // Assume simulation height corresponds to 150 meters for physics scale

        const G = 9.81; // Acceleration due to gravity (m/s^2)
        const AIR_DENSITY = 1.225; // kg/m^3 at sea level (simplified)
        const DRAG_COEFFICIENT = 0.5; // Average drag coefficient (simplified, adjust for feel)
        const TIME_STEP = 0.016; // Simulation time step (approx 1/60 second for 60fps)

        // Object properties (mass in kg, area facing down in m^2 - simplified)
        // Effective area needs to be scaled to real-world values conceptually for drag calculation
        const objectProperties = {
            'bowling-ball': { name: 'כדור באולינג', mass: 6, area: 0.015 }, // Area of a sphere ~pi*r^2
            'tennis-ball': { name: 'כדור טניס', mass: 0.058, area: 0.004 },
            'feather': { name: 'נוצה', mass: 0.0005, area: 0.03 }, // Large area, low mass
            'brick': { name: 'לבנה', mass: 2, area: 0.01 }
        };

        let animationFrameId = null;
        let objects = [];
        let startTime = null;
        let simulationRunning = false;

        function createObjectElement(id, type, initialLeftPercent) {
            const obj = document.createElement('div');
            obj.id = id;
            // Remove any previous object class
            obj.className = 'falling-object'; // Start fresh
            obj.classList.add(`object-${type}`);
            obj.style.left = `${initialLeftPercent}%`;
            // Set initial top position explicitly
            obj.style.top = '0px';
            simulationArea.appendChild(obj);
            return obj;
        }

        function initializeSimulation() {
            // Clear previous objects and results
            simulationArea.querySelectorAll('.falling-object').forEach(el => el.remove());
            resultDisplay.textContent = ''; // Clear result text
            timerDisplay.textContent = '0.00 שניות'; // Reset timer display

            const obj1Type = object1Select.value;
            const obj2Type = object2Select.value;

            // Create object elements
            const obj1Element = createObjectElement('obj1', obj1Type, 30);
            const obj2Element = createObjectElement('obj2', obj2Type, 70);

            // Initialize object state
            objects = [
                {
                    element: obj1Element,
                    display: object1Display,
                    name: objectProperties[obj1Type].name,
                    mass: objectProperties[obj1Type].mass,
                    area: objectProperties[obj1Type].area,
                    positionY: 0, // meters from top
                    velocityY: 0, // m/s
                    accelerationY: 0, // m/s^2
                    landedTime: null, // Time when landed
                    initialLeft: 30 // For reset
                },
                {
                    element: obj2Element,
                    display: object2Display,
                    name: objectProperties[obj2Type].name,
                    mass: objectProperties[obj2Type].mass,
                    area: objectProperties[obj2Type].area,
                    positionY: 0, // meters from top
                    velocityY: 0, // m/s
                    accelerationY: 0, // m/s^2
                    landedTime: null,
                     initialLeft: 70 // For reset
                }
            ];

             // Set initial display text
            updateDisplay(0); // Display initial state (time 0)

            simulationRunning = false;
            startButton.disabled = false;
            resetButton.disabled = true; // Disable reset until simulation starts or finishes
             // Enable selects for object/mode changes
            object1Select.disabled = false;
            object2Select.disabled = false;
            modeSelect.disabled = false;
        }

        function updatePhysics(obj, mode, deltaTime) {
            // Check if object has already landed
            if (obj.landedTime !== null) {
                // Ensure element is exactly at the ground position and doesn't move
                const groundPosYpx = simHeightPx;
                obj.element.style.top = `${groundPosYpx}px`;
                obj.velocityY = 0;
                obj.accelerationY = 0;
                return;
            }

            let forceGravity = obj.mass * G; // Force down (positive)
            let forceDrag = 0; // Force up (negative)

            if (mode === 'air') {
                // Drag formula: F_drag = 0.5 * rho * v^2 * Cd * A
                // rho = AIR_DENSITY, v = obj.velocityY, Cd = DRAG_COEFFICIENT, A = obj.area
                // Drag opposes motion, so if velocity is positive (down), drag is negative (up)
                forceDrag = -0.5 * AIR_DENSITY * obj.velocityY * Math.abs(obj.velocityY) * DRAG_COEFFICIENT * obj.area;
            }

            // Calculate net force (positive is down)
            let netForce = forceGravity + forceDrag; // gravity is positive, drag is negative

            // Calculate acceleration (a = F_net / m)
            obj.accelerationY = netForce / obj.mass;

            // Update velocity and position using numerical integration (Euler method)
            // Using the time step from requestAnimationFrame (deltaTime)
            obj.velocityY += obj.accelerationY * (deltaTime / 1000); // deltaTime is in milliseconds
            obj.positionY += obj.velocityY * (deltaTime / 1000); // deltaTime is in milliseconds

            // Check for landing
            // Convert positionY (meters) to pixels and check against ground pixel position
            const currentPosYpx = obj.positionY * (simHeightPx / simHeightMeters);
            if (currentPosYpx >= simHeightPx) {
                obj.positionY = simHeightMeters; // Cap at ground level in meters
                obj.landedTime = (performance.now() - startTime) / 1000; // Record landing time in seconds
                obj.element.classList.add('object-landed'); // Trigger landing animation
                obj.velocityY = 0; // Stop velocity immediately
                obj.accelerationY = 0; // Stop acceleration
                // Position element exactly at ground
                 obj.element.style.top = `${simHeightPx}px`;
            }
        }

        function updateVisuals() {
            objects.forEach(obj => {
                // Map meters position to pixels position
                const posYpx = obj.positionY * (simHeightPx / simHeightMeters);
                // Position the element, ensuring it doesn't go below the ground pixel level
                obj.element.style.top = `${Math.min(posYpx, simHeightPx)}px`;
            });
        }

        function updateDisplay(elapsedTime) {
             timerDisplay.textContent = `${elapsedTime.toFixed(2)} שניות`; // Update timer

             objects.forEach(obj => {
                 // Display velocity and height from ground
                 const velocityMs = obj.velocityY.toFixed(1);
                 const heightM = (simHeightMeters - obj.positionY); // Height from ground
                 obj.display.textContent = `${obj.name}: מהירות ${velocityMs} מ/ש | גובה ${Math.max(0, heightM).toFixed(1)} מ'`;

                 // If landed, update display to show landed info
                 if (obj.landedTime !== null) {
                     obj.display.textContent = `${obj.name}: נחת בזמן ${obj.landedTime.toFixed(2)} שניות`;
                 }
             });
        }

        function checkSimulationComplete() {
            // Simulation is complete when both objects have landed
            return objects.every(obj => obj.landedTime !== null);
        }

        function displayResults() {
            // Sort objects by landing time
            const sortedObjects = [...objects].sort((a, b) => {
                // Handle cases where one or both haven't landed (shouldn't happen if checkSimulationComplete is true, but for safety)
                if (a.landedTime === null && b.landedTime === null) return 0;
                if (a.landedTime === null) return 1; // b lands first
                if (b.landedTime === null) return -1; // a lands first
                return a.landedTime - b.landedTime;
            });

            const obj1 = sortedObjects[0];
            const obj2 = sortedObjects[1];

            if (obj1.landedTime === obj2.landedTime || Math.abs(obj1.landedTime - obj2.landedTime) < 0.05) { // Consider times very close as a tie
                 resultDisplay.textContent = `תוצאה: נחתו כמעט בו-זמנית! (${obj1.landedTime.toFixed(2)} שניות)`;
                 resultDisplay.style.color = '#28a745'; // Green for tie/close
            } else {
                resultDisplay.textContent = `תוצאה: ${obj1.name} נחת ראשון (${obj1.landedTime.toFixed(2)} שניות) לפני ${obj2.name} (${obj2.landedTime.toFixed(2)} שניות)`;
                 resultDisplay.style.color = '#dc3545'; // Red for difference
            }
        }

        let lastTimestamp = 0;
        function gameLoop(timestamp) {
            if (!startTime) startTime = timestamp;
            const elapsedSinceStart = (timestamp - startTime) / 1000; // Total elapsed time in seconds
            const deltaTime = timestamp - lastTimestamp; // Time since last frame in milliseconds
            lastTimestamp = timestamp;

            // Prevent extremely large delta times if tab was inactive
            const safeDeltaTime = Math.min(deltaTime, 1000/30); // Cap delta to max ~30fps frame time

            objects.forEach(obj => {
                 // Only update physics for objects that haven't landed
                 if (obj.landedTime === null) {
                    updatePhysics(obj, modeSelect.value, safeDeltaTime);
                 }
            });

            updateVisuals();
            updateDisplay(elapsedSinceStart);

            if (checkSimulationComplete()) {
                simulationRunning = false;
                startButton.disabled = true; // Keep start disabled
                resetButton.disabled = false; // Enable reset
                displayResults(); // Show outcome
            } else {
                animationFrameId = requestAnimationFrame(gameLoop);
            }
        }

        startButton.addEventListener('click', () => {
            if (simulationRunning) return; // Prevent multiple clicks

            simulationRunning = true;
            startButton.disabled = true;
            resetButton.disabled = false; // Enable reset once started
             // Disable selects during simulation
            object1Select.disabled = true;
            object2Select.disabled = true;
            modeSelect.disabled = true;

            // Reset object positions visually before starting
            objects.forEach(obj => {
                 obj.element.style.top = '0px';
                 obj.element.classList.remove('object-landed');
            });
            // Reset object state logically
             objects.forEach(obj => {
                obj.positionY = 0;
                obj.velocityY = 0;
                obj.accelerationY = 0;
                obj.landedTime = null;
            });

            resultDisplay.textContent = ''; // Clear previous result
            startTime = performance.now(); // Reset timer start
            lastTimestamp = startTime; // Initialize last timestamp for deltaTime calculation

            animationFrameId = requestAnimationFrame(gameLoop); // Start animation loop
        });

        resetButton.addEventListener('click', () => {
            if (animationFrameId) {
                cancelAnimationFrame(animationFrameId);
            }
             simulationRunning = false;
            initializeSimulation(); // Re-initialize state and visuals
            startButton.disabled = false; // Enable start
            resetButton.disabled = true; // Disable reset
        });

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר את סודות הפיזיקה מאחורי הנפילה' : 'הצג/הסתר את סודות הפיזיקה מאחורי הנפילה';
        });

        // Initial setup
        initializeSimulation();

    });
</script>
---