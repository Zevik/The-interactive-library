---
title: "פרחי כפור: אמנות הקפיאה על זכוכית"
english_slug: frost-flowers-physics-magic-on-window
category: "פיזיקה"
tags: ["התגבשות", "מעבר פאזה", "יווצרות קרח", "תרמודינמיקה", "קירור-על", "דנדריטים"]
---
# פרחי כפור: אמנות הקפיאה על זכוכית

תארו לעצמכם בוקר חורפי קר, ועל חלון ביתכם פורחים ציורים קפואים עוצרי נשימה – דפוסים מורכבים, דמויי נוצות או שרכים, הנראים כאילו נוצרו במכחול של אמן על-טבעי. אלו הם 'פרחי כפור', תופעה פיזיקלית קסומה שמספרת סיפור על מולקולות מים, טמפרטורה ולחץ. מהם התנאים שיוצרים את היצירות הארעיות הללו, ואיזה תהליך מדעי עומד מאחורי היווצרותם?

<div class="simulation-container">
    <h2>צפו בקסם קורה: סימולציית יצירת פרחי כפור</h2>
    <div class="controls">
        <div class="control-group">
            <label for="temp" title="טמפרטורה נמוכה בצד החיצוני מקררת את החלון הפנימי ומעודדת קיפאון">טמפרטורת סביבה חיצונית: <span id="tempValue">קר מאוד</span></label>
            <input type="range" id="temp" min="0" max="100" value="50">
        </div>
        <div class="control-group">
            <label for="humidity" title="כמות אדי המים באוויר הפנימי - דלק להתגבשות הקרח">לחות אוויר פנימית: <span id="humidityValue">בינונית</span></label>
            <input type="range" id="humidity" min="0" max="100" value="50">
        </div>
        <div class="control-group">
            <label for="nucleationSites" title="פגמים זעירים על פני הזכוכית שמשמשים כנקודות התחלה להתגבשות">מוקדי התגבשות: <span id="nucleationSitesValue">בינוני (10)</span></label>
            <input type="range" id="nucleationSites" min="2" max="50" value="10">
        </div>
        <div class="button-group">
             <button id="startSim" class="sim-button primary">התחילו את הקסם</button>
             <button id="resetSim" class="sim-button secondary" style="display: none;">איפוס החלון</button>
        </div>
    </div>
    <div class="window-frame">
        <canvas id="frostCanvas" width="500" height="350"></canvas>
        <div id="nucleationSitesVisual"></div> <!-- Visual representation of sites -->
    </div>
</div>

<button id="toggleExplanation" class="explanation-button">רוצים להבין איך זה קורה? לחצו להסבר המדעי</button>

<div id="explanation" class="explanation-box" style="display: none;">
    <h2>הסבר מדעי: הפיזיקה המופלאה שמאחורי פרחי הכפור</h2>

    <h3>מה מבדיל 'פרחי כפור' מכפור רגיל?</h3>
    <p>כפור שגרתי הוא לרוב ציפוי קרח אחיד ודק הנוצר על משטחים קרים. לעומת זאת, 'פרחי כפור' (Frost Flowers / Ice Flowers / Fern Frost) על חלונות הם יצירות קרח תלת-ממדיות ומורכבות, לרוב בעלות מבנה דנדריטי (דמוי עץ או שרך), שנוצרות בתנאים מדויקים. הם תוצאה של התגבשות ישירה של אדי מים מהאוויר (ריבוץ - Deposition) או קיפאון של שכבת מים בקירור-על, תהליך שצורתו הסופית מושפעת דרמטית מקצב הגידול ותנאי הסביבה.</p>

    <h3>הטריגרים הפיזיקליים: שלושת התנאים ההכרחיים</h3>
    <p>כדי שפרחי כפור יפרחו על חלונכם, נדרש שילוב נדיר של שלושה גורמים עיקריים:
    <ol>
        <li>**קור מקפיא בחוץ:** הצד החיצוני של החלון חייב להיות קר משמעותית מאפס מעלות צלזיוס, ולעיתים קרובות גם קר יותר מנקודת הטל של האוויר שבפנים. הקור העז יוצר מפל טמפרטורות חד שגורם לצד הפנימי של החלון להתקרר אף הוא לטמפרטורות קיפאון או קרוב לכך.</li>
        <li>**לחות נדיבה בפנים:** האוויר בתוך החדר צריך להיות עשיר יחסית באדי מים (לחות גבוהה). כשהאוויר החם והלח הזה פוגש את פני השטח הקרים כקרח של החלון הפנימי, אדי המים מתעבים למים נוזליים בקירור-על או עוברים ישירות למוצק (ריבוץ) על המשטח.</li>
        <li>**משטח בעל סודות:** פני הזכוכית הפנימיים אינם חלקים לחלוטין. שריטות זעירות, שאריות לכלוך, אבק או אפילו פגמים מיקרוסקופיים בזכוכית - כל אלה משמשים כ**מוקדי התגבשות (Nucleation Sites)**, הנקודות הקריטיות בהן הקסם מתחיל.</li>
    </ol></p>

    <h3>הסוד של מוקדי ההתגבשות (Nucleation Sites)</h3>
    <p>יווצרות גביש קרח היא תהליך שדורש אנרגיה התחלתית כדי לסדר את מולקולות המים במבנה גבישי מסודר. על משטח חלק לחלוטין, מולקולות המים עלולות להישאר במצב נוזלי גם הרבה מתחת לאפס מעלות צלזיוס (קירור-על) כי אין "תבנית" או "פיגום" שעליו הגביש יכול להתחיל לצמוח בקלות. מוקדי התגבשות מספקים את ה"פיגום" הזה – הם מורידים את מחסום האנרגיה הדרוש לתחילת ההתגבשות, ומאפשרים לגבישים הראשונים להיווצר דווקא בנקודות אלו, גם כששאר המשטח עדיין במצב קירור-על.</p>

    <h3>מדע הקפיאה: קירור-על ומעברי פאזה</h3>
    <p>כאמור, הטמפרטורה הנמוכה של החלון יכולה לקרר את אדי המים או המים הנוזליים שבאוויר אל מתחת לנקודת הקיפאון הרגילה (0°C) מבלי שהם יקפאו מיד – זוהי תופעת **קירור-על (Supercooling)**. זהו מצב לא יציב. ברגע שמולקולות המים הללו פוגשות מוקד התגבשות או גביש קרח קיים, הן "מבינות" איך להתארגן ומעבר הפאזה מתחיל מיד. לרוב, על חלונות מתרחש תהליך **ריבוץ (Deposition)**, שבו אדי מים עוברים ישירות למצב קרח מוצק, ללא מעבר דרך המים הנוזליים. תהליך זה הוא המאפשר את הצמיחה המהירה והצורנית. במקרים של לחות גבוהה במיוחד, עשויה להיווצר שכבת מים בקירור-על שתקפא במהירות (התמצקות).</p>

    <h3>הדפוסים המסתוריים: כיצד נוצרים הענפים והצורות המורכבות?</h3>
    <p>מרגע שהגביש הראשוני נוצר במוקד ההתגבשות, מולקולות מים נוספות (מאדים או מים בקירור-על) ממהרות להצטרף אליו. צורת הגידול מוכתבת על ידי האיזון בין קצב הגעת המולקולות החדשות לקצה הגביש לבין קצב פיזור החום הנפלט בתהליך ההתגבשות (התגבשות היא תהליך אקסותרמי - פולט חום). בתנאים בהם הקור עז והלחות גבוהה (כמו בחלון חורפי), קצב הגעת המולקולות לקצה הגביש מהיר יותר מקצב פיזור החום מאזורים פנימיים יותר. זה גורם ל"בליטות" או קודקודים בקצה הגביש לגדול מהר יותר מאזורים שקועים. הבליטות הללו מתפתחות לענפים, וקצות הענפים הצעירים הופכים למוקדי גדילה חדשים, וחוזר חלילה. תהליך זה, המכונה **גידול דנדריטי**, יוצר את המבנה המורכב והענפי הכה אופייני לפרחי כפור.</p>

    <h3>מדוע משטחים חלקים פחות "פורחים"?</h3>
    <p>על משטח נקי וחלק במיוחד, כמות מוקדי ההתגבשות זעירה. זה מקשה על תחילת התגבשות הקרח ודורש קירור עז עוד יותר. אם בכל זאת נוצר קרח, הוא לרוב יתחיל ממוקדים ספורים ביותר או כקפיאה ספונטנית שתתבטא בשכבת קרח דקה ואחידה יחסית, ללא המבנה הדנדריטי המרהיב, פשוט כי אין מספיק נקודות התחלה שיאפשרו את הצמיחה הענפית המרובה בו זמנית.</p>

    <h3>מעבר לחלון: איפה עוד פוגשים התגבשות דנדריטית?</h3>
    <p>עקרונות הגידול הדנדריטי אינם ייחודיים לפרחי כפור. הם קיימים בתופעות טבע רבות אחרות כמו היווצרות פתיתי שלג באטמוספרה, יצירת גבישי מלח יפהפיים מתמיסות מרוכזות, ואפילו בתהליכים תעשייתיים כמו ייצור גבישי סיליקון לתעשיית האלקטרוניקה או התמצקות של מתכות וסגסוגות במהלך יציקה.</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --bg-color: #e0f2f7; /* Light blue for window */
        --frost-color: rgba(255, 255, 255, 0.9); /* Opaque white frost */
        --text-color: #333;
        --heading-color: #0056b3;
        --card-bg: #fff;
        --explanation-bg: #e9ecef;
        --border-color: #ccc;
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: #f8f9fa; /* Very light grey background */
        color: var(--text-color);
        direction: rtl; /* Ensure RTL for Hebrew */
        text-align: right; /* Ensure text alignment */
    }

    h1, h2, h3 {
        color: var(--heading-color);
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
        color: #004085; /* Darker blue for main title */
    }

    p {
        margin-bottom: 15px;
    }

    .simulation-container {
        background-color: var(--card-bg);
        padding: 30px;
        border-radius: 12px;
        box-shadow: var(--shadow);
        margin-bottom: 30px;
        text-align: center; /* Center simulation block content */
    }

    .simulation-container h2 {
        margin-top: 0;
        color: var(--heading-color);
    }

    .controls {
        margin-bottom: 30px;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        justify-items: center; /* Center items in grid */
        text-align: right; /* Ensure text aligns correctly within controls */
    }

    .control-group {
        width: 100%;
        max-width: 400px; /* Limit width of individual controls */
    }

    .controls label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
        text-align: right;
    }

    .controls input[type="range"] {
        width: 100%;
        margin-top: 0;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        transition: background-color 0.3s ease;
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        transition: background-color 0.3s ease;
    }

    .button-group {
         grid-column: 1 / -1; /* Span all columns */
         display: flex;
         justify-content: center;
         gap: 15px;
         margin-top: 15px;
    }

    .sim-button {
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .sim-button.primary {
        background-color: var(--success-color);
        color: white;
    }

    .sim-button.primary:hover {
        background-color: #218838;
        transform: translateY(-1px);
    }
     .sim-button.primary:active {
        transform: translateY(0);
    }

    .sim-button.secondary {
         background-color: var(--secondary-color);
         color: white;
    }
     .sim-button.secondary:hover {
        background-color: #5a6268;
        transform: translateY(-1px);
    }
     .sim-button.secondary:active {
        transform: translateY(0);
    }

    .sim-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        transform: none;
    }


    .window-frame {
        border: 15px solid #a0b0c0; /* More realistic frame color */
        border-radius: 8px;
        overflow: hidden;
        position: relative;
        width: fit-content; /* Fit frame to canvas size */
        margin: 20px auto; /* Center the window frame */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.2); /* Inner shadow for depth */
    }

     #nucleationSitesVisual {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Allows clicking canvas underneath */
     }

     .nucleation-dot {
         position: absolute;
         width: 6px;
         height: 6px;
         background-color: rgba(255, 0, 0, 0.5); /* Semi-transparent red dot */
         border-radius: 50%;
         transform: translate(-50%, -50%); /* Center the dot on the coordinates */
         z-index: 1; /* Ensure dots are above canvas */
     }


    #frostCanvas {
        display: block;
        background-color: var(--bg-color); /* Represents a window surface */
        cursor: crosshair; /* Indicate interactive area */
    }

    .explanation-button {
        display: block;
        width: auto;
        margin: 30px auto;
        padding: 15px 30px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .explanation-button:hover {
         background-color: #0056b3;
         transform: translateY(-2px);
    }
     .explanation-button:active {
        transform: translateY(0);
    }

    .explanation-box {
        background-color: var(--explanation-bg);
        padding: 25px;
        border-left: 6px solid var(--primary-color);
        border-radius: 8px;
        margin-top: 30px;
        box-shadow: var(--shadow);
        opacity: 0; /* Start hidden */
        max-height: 0;
        overflow: hidden;
        transition: opacity 0.6s ease-in-out, max-height 0.6s ease-in-out;
    }

    .explanation-box.visible {
        opacity: 1;
        max-height: 2000px; /* Sufficiently large value */
    }

    .explanation-box h3 {
        margin-top: 20px;
        margin-bottom: 8px;
        color: var(--heading-color);
    }
    .explanation-box ol {
        margin-left: 20px;
        padding-right: 0; /* Remove default RTL padding */
    }
    .explanation-box li {
        margin-bottom: 10px;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .controls {
            grid-template-columns: 1fr; /* Stack controls on small screens */
        }
        .window-frame {
            width: 95%; /* Make canvas/frame responsive */
            max-width: 500px;
        }
        #frostCanvas {
             width: 100%;
             height: auto; /* Maintain aspect ratio */
        }
        .explanation-button {
            width: 95%;
            padding: 12px 20px;
            font-size: 1em;
        }
    }

</style>

<script>
    const tempInput = document.getElementById('temp');
    const humidityInput = document.getElementById('humidity');
    const nucleationSitesInput = document.getElementById('nucleationSites');
    const tempValueSpan = document.getElementById('tempValue');
    const humidityValueSpan = document.getElementById('humidityValue');
    const nucleationSitesValueSpan = document.getElementById('nucleationSitesValue');
    const startButton = document.getElementById('startSim');
    const resetButton = document.getElementById('resetSim');
    const canvas = document.getElementById('frostCanvas');
    const ctx = canvas.getContext('2d');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
    const nucleationSitesVisualDiv = document.getElementById('nucleationSitesVisual');


    let simulationInterval = null;
    let frostPoints = new Set(); // Use a Set for faster point lookup
    const pointSize = 1; // Size of each drawn frost point
    const pixelDensity = 2; // Number of potential growth points checked per simulation step
    let growthAreaRadius = 0; // Radius around nucleation sites/existing frost to check for growth

    // Map slider values to descriptive text and simulation parameters
    function updateSliderValues() {
        const temp = parseInt(tempInput.value, 10);
        let tempText = "קר רגיל (פחות ענפים)";
        let tempFactor = temp / 100; // 0 to 1
        if (temp < 30) tempText = "קר מאוד (מבנה עדין)";
        else if (temp < 70) tempText = "קפוא (גידול מהיר)";
        else tempText = "קפוא ממש (מבנה ענפי מובהק)";
        tempValueSpan.textContent = tempText;

        const humidity = parseInt(humidityInput.value, 10);
        let humidityText = "נמוכה (גידול איטי)";
        let humidityFactor = humidity / 100; // 0 to 1
        if (humidity < 30) humidityText = "נמוכה";
        else if (humidity < 70) humidityText = "בינונית (גידול יציב)";
        else humidityText = "גבוהה מאוד (גידול מהיר ומפושט)";
        humidityValueSpan.textContent = humidityText;

        const nucleationSites = parseInt(nucleationSitesInput.value, 10);
        let sitesText = "מעט";
        if (nucleationSites < 10) sitesText = "מעט";
        else if (nucleationSites < 30) sitesText = "בינוני";
        else sitesText = "הרבה";
        nucleationSitesValueSpan.textContent = `${sitesText} (${nucleationSites})`;

        // Calculate growth parameters based on sliders
        // Growth rate influenced by both temp (colder = faster phase transition) and humidity (more water available)
        // Branching influenced by temp (colder = sharper dendrites) and humidity (more available water allows growth in multiple directions)
        simulationParameters.growthSpeed = 1 + tempFactor * 2 + humidityFactor * 2; // How many attempts per step
        simulationParameters.attachmentRadius = 2 + humidityFactor * 5 + tempFactor * 3; // How close a new point must be to stick
        simulationParameters.branchingTendency = 0.01 + (tempFactor + humidityFactor) / 2 * 0.05; // Probability modifier for branching
    }

    const simulationParameters = {
        growthSpeed: 3, // Base attempts per step
        attachmentRadius: 5, // Radius for new points to 'stick'
        branchingTendency: 0.05 // Probability of branching
    };

    // Helper to add points to the set with bounds check
    function addFrostPoint(x, y) {
        const ix = Math.max(0, Math.min(canvas.width - 1, Math.round(x)));
        const iy = Math.max(0, Math.min(canvas.height - 1, Math.round(y)));
        frostPoints.add(`${ix},${iy}`);
    }

    // Helper to check if a point is already frost
    function isFrost(x, y) {
         if (x < 0 || x >= canvas.width || y < 0 || y >= canvas.height) return false;
         return frostPoints.has(`${Math.round(x)},${Math.round(y)}`);
    }

    // Simulation drawing function
    function drawFrost() {
        // Redraw only needed points, or clear and draw all for simplicity initially
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = var(--frost-color); // Defined in CSS

        frostPoints.forEach(pointKey => {
            const [x, y] = pointKey.split(',').map(Number);
            ctx.fillRect(x, y, pointSize, pointSize);
        });
    }

     // Simulation step function (simplified DLA-like growth)
    function simulationStep() {
        const newPointsThisStep = [];
        const pointsToCheck = Array.from(frostPoints); // Get a snapshot of current points

        // Grow outwards from existing frost points
        const growthAttempts = simulationParameters.growthSpeed * 10; // Scale attempts based on speed

        for (let i = 0; i < growthAttempts; i++) {
            // Pick a random existing frost point to grow from (biased towards edges? too complex for now)
            const randFrostPointKey = pointsToCheck[Math.floor(Math.random() * pointsToCheck.length)];
            const [fx, fy] = randFrostPointKey.split(',').map(Number);

            // Attempt to add a point nearby
            const angle = Math.random() * Math.PI * 2;
            // Bias distance slightly outwards or randomly
            const dist = Math.random() * simulationParameters.attachmentRadius * 2; // Potential new point distance
            const nx = fx + Math.cos(angle) * dist;
            const ny = fy + Math.sin(angle) * dist;

            // Check if this potential point is close enough to *any* existing frost point
            let isNearFrost = false;
            // Optimisation: Only check near the point we grew from + a few others?
             for (let j = 0; j < Math.min(pointsToCheck.length, 10); j++) { // Check against this point and 9 random others
                 const [checkFx, checkFy] = pointsToCheck[j].split(',').map(Number);
                 const distToFrost = Math.sqrt(Math.pow(nx - checkFx, 2) + Math.pow(ny - checkFy, 2));
                 if (distToFrost < simulationParameters.attachmentRadius) {
                     isNearFrost = true;
                     break;
                 }
             }
            // If near frost, add it if the spot is empty and within bounds
            if (isNearFrost && !isFrost(nx, ny)) {
                 addFrostPoint(nx, ny);
                 newPointsThisStep.push({x: Math.round(nx), y: Math.round(ny)}); // Keep track for potential drawing optimization later
            }
        }

        if (newPointsThisStep.length > 0) {
            drawFrost(); // Redraw canvas
        }


        // Stop simulation after sufficient density or time
        if (frostPoints.size > canvas.width * canvas.height * 0.15) { // Stop when 15% of area is covered
             clearInterval(simulationInterval);
             simulationInterval = null;
             startButton.textContent = "הקסם הושלם!";
             startButton.disabled = true;
        } else if (pointsToCheck.length === 0 && frostPoints.size > 0) {
             // Should not happen with current logic if pointsToCheck is from frostPoints
        } else if (newPointsThisStep.length === 0 && frostPoints.size > 0) {
            // If no new points were added this step but frost exists, maybe parameters are too low
            // or simulation got stuck. Could add a check for this.
             // console.log("Simulation stalled, adjusting parameters or stopping.");
             // clearInterval(simulationInterval);
             // simulationInterval = null;
             // startButton.textContent = "סימולציה נעצרה (התנאים לא מספיקים לגידול נוסף)";
             // startButton.disabled = true;
        }
    }


    // Start simulation
    startButton.addEventListener('click', () => {
        if (simulationInterval) return; // Prevent multiple intervals

        // Reset canvas and points
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        frostPoints = new Set();
        nucleationSitesVisualDiv.innerHTML = ''; // Clear visual dots

        // Create initial nucleation sites
        const numSites = parseInt(nucleationSitesInput.value, 10);
        for (let i = 0; i < numSites; i++) {
            // Place sites randomly or with some bias
            const x = Math.random() * canvas.width;
            const y = Math.random() * canvas.height;
            addFrostPoint(x, y);

            // Add visual marker for the site
            const dot = document.createElement('div');
            dot.classList.add('nucleation-dot');
            dot.style.left = `${(x / canvas.width) * 100}%`;
            dot.style.top = `${(y / canvas.height) * 100}%`;
            nucleationSitesVisualDiv.appendChild(dot);
        }

        drawFrost(); // Draw initial sites

        startButton.textContent = "הקסם מתרחש...";
        startButton.disabled = true;
        resetButton.style.display = 'inline-block';
        updateSliderValues(); // Ensure parameters are updated based on current slider state

        // Start the simulation steps
        simulationInterval = setInterval(simulationStep, 50); // Adjust interval for speed/smoothness

    });

     // Reset simulation
     resetButton.addEventListener('click', () => {
        clearInterval(simulationInterval);
        simulationInterval = null;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        frostPoints = new Set();
        nucleationSitesVisualDiv.innerHTML = ''; // Clear visual dots
        startButton.textContent = "התחילו את הקסם";
        startButton.disabled = false;
        resetButton.style.display = 'none';
        updateSliderValues(); // Reset values display if needed, or just re-enable sliders
     });

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('visible');
        if (explanationDiv.classList.contains('visible')) {
             toggleExplanationButton.textContent = "הסתרת הסבר מדעי";
        } else {
             toggleExplanationButton.textContent = "רוצים להבין איך זה קורה? לחצו להסבר המדעי";
        }
    });

    // Initial update of slider values
    updateSliderValues();

    // Allow clicking on canvas to add nucleation sites *before* starting simulation
    canvas.addEventListener('click', (event) => {
        if (simulationInterval) return; // Don't add sites if simulation is running

        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;    // Get the ratio of CSS pixels to canvas pixels
        const scaleY = canvas.height / rect.height;  // Get the ratio of CSS pixels to canvas pixels

        const x = (event.clientX - rect.left) * scaleX;
        const y = (event.clientY - rect.top) * scaleY;

        // Add the clicked point as a nucleation site
        addFrostPoint(x, y);

        // Add visual marker
        const dot = document.createElement('div');
        dot.classList.add('nucleation-dot');
        dot.style.left = `${(x / canvas.width) * 100}%`;
        dot.style.top = `${(y / canvas.height) * 100}%`;
        nucleationSitesVisualDiv.appendChild(dot);

        drawFrost(); // Redraw to show the new site
         // Update slider value display to reflect manual additions (optional, could just start sim)
        // nucleationSitesInput.value = frostPoints.size; // This might jump too much if many clicks
        // updateSliderValues();
    });


</script>