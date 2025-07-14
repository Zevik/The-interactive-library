---
title: "מנגנון המחגר: הלב הפועם, הסוד השומר על קצב הזמן בשעונים מכניים"
english_slug: escapement-mechanism-beating-heart-mechanical-clock
category: "פיזיקה"
tags: שעונים מכניים, מנגנונים, פיזיקה, מכניקה קלאסית, תנועה מחזורית, הנדסה, היסטוריה של המדע
---
# מנגנון המחגר: הלב הפועם של השעון המכני

דמיינו מנוע נצחי קטן, הניזון רק מכוחו של קפיץ מתוח או משקולת יורדת. איך הוא מצליח לשמור על קצב אחיד, מדויק להפליא, רגע אחר רגע, במשך שעות, ימים, ולעיתים אפילו שנים? מהו הסוד המכני שממיר את הכוח הגולמי הזה למחזוריות מדויקת של תקתוקים, המודדים את זרימת הזמן?

הכירו את מנגנון המחגר – הרכיב הגאוני והאלגנטי שנמצא בלב ליבו של כל שעון מכני. הוא לא רק מווסת את האנרגיה אלא גם "סופר" את תנודות קוצב הזמן, ומתרגם אותן לתנועת המחוגים המוכרת לנו. צללו לתוך הסימולציה שלנו וגלו את הפעולה המהפנטת והחיונית הזו!

<div id="app-container">
    <canvas id="escapementCanvas" width="700" height="450"></canvas>
    <div id="controls">
        <button id="startButton" class="control-button play">התחל סימולציה</button>
        <button id="stopButton" class="control-button stop" disabled>עצור סימולציה</button>
        <div class="speed-control">
            <label for="speedSlider">מהירות:</label>
            <input type="range" id="speedSlider" min="0.05" max="3" step="0.05" value="1">
            <span id="speedValue">x1</span>
        </div>
         <button id="resetButton" class="control-button reset">אפס מצב</button>
    </div>
     <div id="status-display">מצב: מוכן</div>
</div>

<style>
    /* גופנים וסגנון כללי */
    body {
        font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
    }

    h1, h2 {
        color: #2c3e50; /* Dark blue-grey */
        text-align: center;
        margin-top: 20px;
    }

    /* מיכל האפליקציה */
    #app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 30px auto;
        padding: 25px;
        background: linear-gradient(145deg, #e2e8ec, #ffffff); /* Soft gradient background */
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15), 0 6px 6px rgba(0,0,0,0.1); /* Deeper shadow */
        max-width: 750px; /* Limit width for better layout */
    }

    /* הקנבס - אזור הסימולציה */
    #escapementCanvas {
        border: 1px solid #a0a0a0; /* Softer border */
        background-color: #e0e5ec; /* Light grey-blue for depth */
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.1); /* Inner shadow */
        width: 100%; /* Make canvas responsive up to max-width */
        height: auto; /* Maintain aspect ratio */
        max-height: 450px; /* Max height */
    }

    /* פקדי הסימולציה */
    #controls {
        display: flex;
        justify-content: center; /* Center controls */
        align-items: center;
        flex-wrap: wrap; /* Allow controls to wrap on smaller screens */
        gap: 20px; /* Increased spacing */
        margin-bottom: 15px;
        width: 100%; /* Full width */
    }

    .control-button {
        padding: 10px 20px;
        font-size: 1.1rem;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: all 0.3s ease; /* Smooth transitions */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Button shadow */
    }

    .control-button:hover:not(:disabled) {
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        transform: translateY(-2px); /* Lift effect */
    }

     .control-button:active:not(:disabled) {
         transform: translateY(1px);
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }

    .control-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        box-shadow: none;
        transform: none;
    }

    .control-button.play {
        background: linear-gradient(145deg, #4CAF50, #66BB6A); /* Green gradient */
        color: white;
    }

    .control-button.stop {
        background: linear-gradient(145deg, #F44336, #E57373); /* Red gradient */
        color: white;
    }

    .control-button.reset {
        background: linear-gradient(145deg, #FFC107, #FFD54F); /* Amber gradient */
        color: #333;
    }

    .speed-control {
        display: flex;
        align-items: center;
        gap: 10px;
        background-color: #e0e0e0;
        padding: 8px 15px;
        border-radius: 20px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    .speed-control label {
        font-weight: bold;
        color: #555;
        font-size: 1rem;
    }

    .speed-control input[type="range"] {
        -webkit-appearance: none; /* Override default appearance */
        appearance: none;
        width: 120px;
        height: 8px;
        background: #b0b0b0;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s ease;
        border-radius: 5px;
    }

    .speed-control input[type="range"]:hover {
        opacity: 1;
    }

    .speed-control input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

     .speed-control input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

     #speedValue {
         font-weight: bold;
         color: #007bff;
         min-width: 30px; /* Ensure space for value */
         text-align: center;
     }

    #status-display {
        font-size: 0.9rem;
        color: #555;
        margin-top: 10px;
        height: 1.2em; /* Reserve space */
    }

    /* כפתור הצג/הסתר הסבר */
    #toggleExplanationButton {
        display: block; /* Make it a block element */
        width: fit-content; /* Button width based on content */
        margin: 20px auto; /* Center the button */
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
        border: none;
        border-radius: 20px;
        background-color: #007bff;
        color: white;
        transition: background-color 0.3s ease, transform 0.2s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #toggleExplanationButton:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }

    #toggleExplanationButton:active {
        transform: translateY(1px);
    }


    /* אזור ההסבר */
    #explanation {
        display: none; /* Initially hidden */
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #b0bec5; /* Softer border color */
        border-radius: 10px;
        background-color: #eceff1; /* Light blue-grey background */
        box-shadow: 0 5px 10px rgba(0,0,0,0.1);
    }

    #explanation h2 {
        color: #2c3e50; /* Dark blue-grey */
        border-bottom: 2px solid #007bff; /* Blue accent */
        padding-bottom: 8px;
        margin-bottom: 20px;
        text-align: right; /* Align right for RTL */
    }

    #explanation ul {
        list-style: none; /* Remove default list style */
        padding: 0; /* Remove default padding */
        margin-left: 0;
    }

    #explanation li {
        margin-bottom: 15px;
        line-height: 1.7;
        padding-right: 25px; /* Space for custom bullet */
        position: relative; /* Needed for custom bullet */
        color: #4f616f; /* Slightly darker text color */
    }

    #explanation li:before {
        content: '•'; /* Custom bullet point */
        position: absolute;
        right: 0;
        top: 0;
        color: #007bff; /* Blue bullet color */
        font-size: 1.2em;
        font-weight: bold;
    }

    #explanation li strong {
        color: #2c3e50; /* Bold text color */
    }

    #explanation ul ul { /* Inner lists */
        margin-top: 10px;
        margin-bottom: 0;
        padding-right: 20px; /* Indent inner list */
    }

     #explanation ul ul li {
         margin-bottom: 8px;
         padding-right: 20px;
     }

     #explanation ul ul li:before {
         content: '-'; /* Different bullet for inner list */
         color: #546e7a; /* Different color */
     }
</style>

<button id="toggleExplanationButton">הצג הסבר מפורט</button>

<div id="explanation">
    <h2>הסבר על מנגנון המחגר</h2>
    <ul>
        <li><strong>מהו מנגנון מחגר ולמה הוא קריטי לשעונים מכניים?</strong>
            המחגר הוא לב ליבו של השעון המכני – הוא הרכיב שמבצע את התנועה המחזורית של ה"תקתוק". תפקידו העיקרי כפול:
            <ul>
                <li><strong>ויסות אנרגיה:</strong> הוא מאפשר לאנרגיה האצורה במקור הכוח (קפיץ או משקולת) להשתחרר לאט ובהדרגה, במקום בבת אחת.</li>
                <li><strong>הנעת קוצב הזמן וספירתו:</strong> הוא מקבל "פקודות" מקוצב הזמן (גלגל התנופה או המטוטלת) מתי לשחרר אנרגיה, ובתמורה מעניק לקוצב הזמן "דחיפה" קטנה כדי לשמור על תנודתו הקבועה. בו זמנית, כל שחרור כזה מייצג יחידת זמן (תקתוק), והמחגר מאפשר למערכת גלגלי השיניים (Train) לספור את היחידות הללו ולהציג את השעה על המחוגים.</li>
            </ul>
            בלעדיו, הקפיץ היה משתחרר מיידית, וכל מנגנון השעון היה ממהר באופן בלתי נשלט או פשוט נעצר.
        </li>
        <li><strong>מרכיבי המחגר העיקריים (בדגם הנפוץ - מחגר ליבר):</strong>
            <ul>
                <li>**גלגל המחגר (Escape Wheel):** גלגל משונן המקבל אנרגיה ממערכת ההנעה (Gear Train). שיניו מעוצבות באופן מיוחד כך שיוכלו להיתפס על ידי הפלטים. הוא "מנסה" להסתובב כל הזמן, אך נבלם על ידי העוגן.</li>
                <li>**העוגן (Pallet Fork):** רכיב בצורת מזלג (או עוגן) הנע על ציר. בקצותיו ישנם "פלטים" (Pallets) – לרוב עשויים אבן אודם סינתטית בשעונים מודרניים – המהווים את נקודות המגע עם שיני גלגל המחגר. תנועת העוגן סיבובית וקצרה.</li>
                <li>**גלגל התנופה (Balance Wheel) וקפיץ השערה (Hairspring):** זהו "המוח" של השעון, קוצב הזמן. גלגל התנופה נע בתנועה סיבובית קדימה ואחורה (תנודה/אוסצילציה), וקפיץ השערה הוא הקפיץ הדקיק שמחזיר אותו למרכז ומבטיח שהתנודה תהיה קבועה ככל האפשר (זוהי מערכת תנודה הרמונית). העוגן מקושר לגלגל התנופה ומקבל ממנו את הקצב.</li>
            </ul>
        </li>
        <li><strong>תהליך הפעולה המחזורי: נעילה (Locking), דחף (Impulse), ושחרור (Release):</strong>
            כל "תקתוק" הוא למעשה מחזור אחד של פעולת המחגר:
            <ul>
                <li><strong>נעילה (Locking):</strong> כשהעוגן נמצא באחד מקצוות תנודתו, אחד הפלטים שלו נוחת ונועל שן של גלגל המחגר, עוצר את סיבובו.</li>
                <li><strong>שחרור (Release):</strong> גלגל התנופה ממשיך את תנודתו ומניף את העוגן. הפלט הנועל מחליק על השן, משחרר אותה, ואילו הפלט השני מתקרב לגלגל המחגר.</li>
                <li><strong>דחף (Impulse):</strong> ברגע שהשן משוחררת, גלגל המחגר מתחיל לנוע מעט. השן המחליקה על משטח הפלט משוחרר נותנת דחיפה קטנה לפלט, דחיפה זו מועברת דרך העוגן לגלגל התנופה ומספקת לו את האנרגיה הדרושה להמשך תנודתו. בו זמנית, הפלט השני נוחת על השן הבאה ומבצע שוב נעילה, וחוזר חלילה בצד השני.</li>
            </ul>
        </li>
        <li><strong>כיצד המחגר מתעל אנרגיה ומודד זמן:</strong>
            המחגר הוא שסתום חכם. הוא מאפשר לגלגל המחגר, המונע בכוח, לנוע רק במנות קטנות ומדודות, כל פעם שקוצב הזמן "מאשר". האנרגיה מועברת אך ורק במהלך שלב הדחף הקצרצר. מספר הדחפים (והנעילות/שחרורים) נספר על ידי מערכת הגלגלים, והוא קובע את מהירות תנועת המחוגים. המחגר למעשה מתרגם את התנודות המדויקות של קוצב הזמן לתנועה סיבובית יציבה ואיטית של מערכת הגלגלים והמחוגים.
        </li>
        <li><strong>חשיבות הדיוק:</strong>
            הדיוק של שעון מכני תלוי בשני גורמים עיקריים: יציבות קצב התנודה של קוצב הזמן (שמושפע מטמפרטורה, מצב אנרגיה, ועוד), ודיוק מנגנון המחגר עצמו (צורת השיניים והפלטים, חיכוך, התאמה נכונה). חיכוך הוא האויב הגדול ביותר, ולכן חומרי גלם איכותיים (כמו אבני אודם לפלטים) ושימון מדויק חיוניים לשמירה על דיוק לאורך זמן.
        </li>
        <li><strong>סוגי מחגרים:</strong>
            המחגר התפתח רבות לאורך מאות שנים. המחגרים הראשונים (כמו מחגר הורז') היו פחות יעילים, אך המציאו את העיקרון. מחגר האנקור (Anchor) שיפר את היעילות והדיוק בשעוני קיר. ומחגר הליבר (Lever) הפך לסטנדרט בשעוני יד בזכות יעילותו ויכולתו לעבוד גם בתנועה. כל סוג מייצג צעד בהנדסת הזמן המדויקת.
        </li>
    </ul>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('escapementCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const resetButton = document.getElementById('resetButton');
    const speedSlider = document.getElementById('speedSlider');
    const speedValueSpan = document.getElementById('speedValue');
    const statusDisplay = document.getElementById('status-display');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');
    const explanationDiv = document.getElementById('explanation');

    let animationFrameId = null;
    let isRunning = false;
    let speedFactor = parseFloat(speedSlider.value);

    // --- Simulation State (Lever Escapement Model) ---
    const state = {
        escapeWheelAngle: 0, // Current angle of the escape wheel
        escapeWheelAngularVelocity: 0, // Velocity (attempts to rotate)
        palletAngle: 0, // Current angle of the pallet fork
        balanceWheelAngle: 0, // Current angle of the balance wheel
        balanceWheelAngularVelocity: 0, // Velocity of the balance wheel

        // Constants for simplified model
        wheelRadius: 80,
        numTeeth: 15, // Number of teeth on escape wheel
        toothAngle: (Math.PI * 2) / numTeeth, // Angle between teeth
        toothLength: 15,
        wheelCenter: { x: canvas.width / 2, y: canvas.height / 2 - 50 }, // Slightly higher center

        palletPivot: { x: canvas.width / 2 - 40, y: canvas.height / 2 + 80 }, // Pallet pivot below and left
        palletArmLength: 100,
        palletAngles: [-Math.PI / 10, Math.PI / 10], // Angles for the two pallets relative to arm
        palletLength: 20, // Length of the pallet face
        palletWidth: 10, // Width of the pallet (visual)

        balanceConnectionOffset: 60, // Distance from pallet pivot to balance connection point
        balanceRadius: 30,
        balanceSpringConstant: 0.01, // Stiffness of the hairspring (simplified)
        friction: 0.003, // Damping for balance wheel
        escapeWheelDriveTorque: 0.005, // Torque from the mainspring/weight (tries to spin wheel)
        impulseMagnitude: 0.3, // How much impulse is given to the balance wheel

        // Simulation state variables for logic
        currentLockingToothIndex: -1, // Index of the tooth currently locked (-1 means none)
        isImpulsing: false,
        impulsePalletIndex: -1, // Index of the pallet giving impulse (0 or 1)
        prevBalanceWheelAngle: 0 // To detect zero crossings
    };

    // --- Drawing Functions ---
    function drawEscapeWheel(ctx, state) {
        const { wheelRadius, numTeeth, toothAngle, toothLength, wheelCenter, escapeWheelAngle } = state;
        ctx.save();
        ctx.translate(wheelCenter.x, wheelCenter.y);
        ctx.rotate(escapeWheelAngle);

        // Draw wheel body
        ctx.fillStyle = '#b0bec5'; // Light grey-blue
        ctx.strokeStyle = '#546e7a'; // Darker blue-grey
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(0, 0, wheelRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Draw spokes (simplified)
        ctx.strokeStyle = '#78909c';
        ctx.lineWidth = 3;
        for(let i = 0; i < 4; i++) {
             const angle = i * Math.PI/2;
             ctx.beginPath();
             ctx.moveTo(0,0);
             ctx.lineTo(wheelRadius * 0.8 * Math.cos(angle), wheelRadius * 0.8 * Math.sin(angle));
             ctx.stroke();
        }


        // Draw teeth
        ctx.fillStyle = '#e0e0e0'; // Light grey
        ctx.strokeStyle = '#757575'; // Grey
        ctx.lineWidth = 1.5;
        for (let i = 0; i < numTeeth; i++) {
            const angle = i * toothAngle;
             // Simplified tooth shape (triangle pointing outwards)
            const x1 = wheelRadius * Math.cos(angle);
            const y1 = wheelRadius * Math.sin(angle);
            const x2 = (wheelRadius + toothLength) * Math.cos(angle + toothAngle / 4);
            const y2 = (wheelRadius + toothLength) * Math.sin(angle + toothAngle / 4);
            const x3 = (wheelRadius + toothLength) * Math.cos(angle - toothAngle / 4);
            const y3 = (wheelRadius + toothLength) * Math.sin(angle - toothAngle / 4);

            ctx.beginPath();
            ctx.moveTo(x1, y1);
            ctx.lineTo(x2, y2);
            ctx.lineTo(x3, y3);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();

            // Highlight the currently locked/impulsing tooth if applicable
            if (state.currentLockingToothIndex === i || (state.isImpulsing && Math.abs(state.escapeWheelAngle - (i * toothAngle + state.toothAngle/2)) < state.toothAngle/4 )) {
                 ctx.fillStyle = '#ff5722'; // Deep Orange
                 ctx.fill(); // Redraw filled part to highlight
             }
        }

        ctx.restore();
    }

    function drawPalletFork(ctx, state) {
         const { palletPivot, palletArmLength, palletAngle, palletAngles, palletLength, palletWidth, balanceConnectionOffset } = state;
        ctx.save();
        ctx.translate(palletPivot.x, palletPivot.y);
        ctx.rotate(palletAngle);

        // Draw pivot
        ctx.fillStyle = '#333';
        ctx.beginPath();
        ctx.arc(0, 0, 6, 0, Math.PI * 2);
        ctx.fill();

        // Draw fork arms
        ctx.strokeStyle = '#007bff'; // Blue
        ctx.lineWidth = 6;
        ctx.lineCap = 'round';
         const armAngle = Math.PI / 2; // Fork points upwards initially
        ctx.beginPath();
        // Center piece
        ctx.moveTo(palletArmLength * Math.cos(armAngle), palletArmLength * Math.sin(armAngle));
        ctx.lineTo(0,0); // To pivot
        ctx.lineTo(palletArmLength * Math.cos(armAngle + Math.PI), palletArmLength * Math.sin(armAngle + Math.PI)); // Other side (simplified)
         ctx.stroke();

        // Draw pallets
        const palletColors = ['#ff6347', '#ff6347']; // Tomato red
         if(state.isImpulsing) {
             palletColors[state.impulsePalletIndex] = '#4CAF50'; // Green when impulsing
         }

        // Pallet 1 (connected to arm end 1)
         let p1Angle = armAngle + palletAngles[0];
         let p1X = palletArmLength * Math.cos(p1Angle);
         let p1Y = palletArmLength * Math.sin(p1Angle);
         drawPallet(ctx, p1X, p1Y, p1Angle - Math.PI/2, palletLength, palletWidth, palletColors[0], '#333'); // Rotate pallet to be tangent-like

        // Pallet 2 (connected to arm end 2)
         let p2Angle = armAngle + palletAngles[1];
         let p2X = palletArmLength * Math.cos(p2Angle);
         let p2Y = palletArmLength * Math.sin(p2Angle);
        drawPallet(ctx, p2X, p2Y, p2Angle - Math.PI/2, palletLength, palletWidth, palletColors[1], '#333'); // Rotate pallet

         // Draw connecting arm to balance wheel
         ctx.strokeStyle = '#555';
         ctx.lineWidth = 4;
         ctx.lineCap = 'round';
         ctx.beginPath();
         // Assuming connection is straight up from pivot in resting position
         ctx.moveTo(0,0);
         ctx.lineTo(0, -balanceConnectionOffset);
         ctx.stroke();


        ctx.restore();
    }

    function drawPallet(ctx, x, y, angle, length, width, fill, stroke) {
        ctx.save();
        ctx.translate(x, y);
        ctx.rotate(angle); // Rotate pallet
        ctx.fillStyle = fill;
        ctx.strokeStyle = stroke;
        ctx.lineWidth = 2;
        // Draw as a rectangle
        ctx.beginPath();
        ctx.rect(-length/2, -width/2, length, width);
        ctx.fill();
        ctx.stroke();
        ctx.restore();
    }


    function drawBalanceWheel(ctx, state) {
        const { palletPivot, palletAngle, balanceConnectionOffset, balanceRadius, balanceWheelAngle } = state;

         // Calculate balance wheel center based on pallet arm connection
         const balanceConnX = palletPivot.x + Math.cos(palletAngle + Math.PI/2) * balanceConnectionOffset;
         const balanceConnY = palletPivot.y + Math.sin(palletAngle + Math.PI/2) * balanceConnectionOffset;


        ctx.save();
        ctx.translate(balanceConnX, balanceConnY);
        ctx.rotate(balanceWheelAngle);

        // Draw wheel body
        ctx.fillStyle = '#ffb300'; // Amber Gold
        ctx.strokeStyle = '#e65100'; // Dark Orange
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(0, 0, balanceRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Add a mark to see rotation
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(balanceRadius, 0);
        ctx.stroke();

        ctx.restore();
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        drawEscapeWheel(ctx, state);
        drawPalletFork(ctx, state);
        drawBalanceWheel(ctx, state);

        // Optional: Draw pivot points and connection lines for clarity
        // ctx.fillStyle = 'purple';
        // ctx.beginPath();
        // ctx.arc(state.palletPivot.x, state.palletPivot.y, 4, 0, Math.PI * 2);
        // ctx.fill();
         // Balance connection point (relative to pallet pivot, then rotated by pallet angle)
         // const balanceConnX_relative = Math.cos(state.palletAngle + Math.PI/2) * state.balanceConnectionOffset;
         // const balanceConnY_relative = Math.sin(state.palletAngle + Math.PI/2) * state.balanceConnectionOffset;
         // const balanceConnX_absolute = state.palletPivot.x + balanceConnX_relative;
         // const balanceConnY_absolute = state.palletPivot.y + balanceConnY_relative;
         // ctx.fillStyle = 'red';
         // ctx.beginPath();
         // ctx.arc(balanceConnX_absolute, balanceConnY_absolute, 4, 0, Math.PI * 2);
         // ctx.fill();


    }

    // --- Simulation Update Logic ---
    function update() {
        if (!isRunning) return;

        const dt = (16 / 1000) * speedFactor; // Delta time in seconds, roughly 60fps * speed factor

        // --- Balance Wheel Motion (Driven by Spring and Impulse) ---
        // Simple Harmonic Motion based on hairspring
        let balanceAngularAcceleration = -state.balanceSpringConstant * state.balanceWheelAngle;

        // Apply acceleration
        state.balanceWheelAngularVelocity += balanceAngularAcceleration * dt;

        // Apply friction/damping
        state.balanceWheelAngularVelocity *= (1 - state.friction);

        // Update balance wheel angle
        state.balanceWheelAngle += state.balanceWheelAngularVelocity * dt;

        // Update pallet angle based directly on balance wheel angle (simplified coupling)
        // Assuming a direct mechanical link that translates balance wheel swing to pallet swing
        // Map balanceWheelAngle (e.g., -0.5 to 0.5 radians) to palletAngle (e.g., -0.1 to 0.1 radians)
         const balanceSwingRange = Math.PI / 4; // Assume balance wheel swings +/- pi/4 radians (example)
         const palletSwingRange = state.palletAngles[1] - state.palletAngles[0]; // Total pallet swing range
         // Map balanceWheelAngle from [-balanceSwingRange, balanceSwingRange] to [-palletSwingRange/2, palletSwingRange/2]
         state.palletAngle = (state.balanceWheelAngle / balanceSwingRange) * (palletSwingRange / 2);
         // Clamp pallet angle to prevent overswing visual issues
         state.palletAngle = Math.max(-palletSwingRange/2, Math.min(palletSwingRange/2, state.palletAngle));


        // --- Escape Wheel & Pallet Interaction (Simplified Collision/State Logic) ---
        // The escape wheel *wants* to turn due to drive torque, but is blocked by the pallets.
        // We need to detect when a pallet releases a tooth and the next tooth gets caught or impulsed.

        let wheelCanMove = true; // Assume it can move unless blocked
        state.isImpulsing = false; // Reset impulse state

        // Calculate the position of each tooth relative to the wheel center, taking rotation into account
        // And check for interaction with pallets relative to the pallet pivot.
        // This is complex geometry. Let's simplify significantly for visual effect.

        // Define "engagement" angles relative to the pallet pivot's frame of reference
        // These angles correspond to where the pallets intercept the escape wheel teeth paths.
        // We need to transform tooth positions into the pallet fork's rotating frame.
        // Or, more simply, determine which tooth is *near* a pallet and which pallet is active.

        // Find the tooth angle that is currently closest to the pallet fork pivot (relative to the wheel center)
         const angleFromWheelToPalletPivot = Math.atan2(
             state.palletPivot.y - state.wheelCenter.y,
             state.palletPivot.x - state.wheelCenter.x
         );

         // We need to consider the angle of the pallets themselves relative to the pivot
         // Let's consider the angles where the pallet tips *would intersect* the escape wheel's tooth path
         // This requires some geometric calculation based on arm lengths and pivot points.
         // For simplicity, let's define angular thresholds based on the pallet fork's angle.

         // Define angles where pallets release/lock, relative to the pallet's zero position
         const releaseAngle = palletSwingRange * 0.4; // Angle offset from center where release happens

         // --- Detect Release and Apply Impulse ---
         // Impulse happens when a pallet unlocks a tooth and the wheel advances.
         // This is often triggered when the balance wheel (and thus pallet fork) swings through a certain angle.

         // Detect zero crossing or crossing a threshold based on balance wheel velocity and position
         // Right swing (Balance angle goes from negative to positive)
         if (state.balanceWheelAngularVelocity > 0 && state.balanceWheelAngle > -releaseAngle && state.prevBalanceWheelAngle <= -releaseAngle) {
             // Potential release on the 'left' pallet (pallet 0)
              // Find the tooth that was likely just released/impulsed
              // This logic is simplified: assume the wheel advances one step on release
              state.escapeWheelAngle -= state.toothAngle / 2; // Advance by half a tooth step (common in lever escapement)
             state.balanceWheelAngularVelocity += state.impulseMagnitude * speedFactor; // Apply impulse
             state.isImpulsing = true;
             state.impulsePalletIndex = 0; // Pallet 0 is giving impulse
             // console.log('Impulse detected: Left pallet, Right swing');
         }

         // Left swing (Balance angle goes from positive to negative)
         if (state.balanceWheelAngularVelocity < 0 && state.balanceWheelAngle < releaseAngle && state.prevBalanceWheelAngle >= releaseAngle) {
             // Potential release on the 'right' pallet (pallet 1)
             state.escapeWheelAngle -= state.toothAngle / 2; // Advance by half a tooth step
             state.balanceWheelAngularVelocity -= state.impulseMagnitude * speedFactor; // Apply impulse (negative direction)
             state.isImpulsing = true;
             state.impulsePalletIndex = 1; // Pallet 1 is giving impulse
             // console.log('Impulse detected: Right pallet, Left swing');
         }

         // --- Apply Drive Torque if Not Locked ---
         // In a real escapement, the wheel tries to turn constantly.
         // Here, we've simplified. We advance the wheel by a fixed step on impulse.
         // A more realistic approach would be to check collision with pallets and only allow rotation
         // when no pallet is blocking. Given the complexity of collision detection vs. the goal
         // of a clear *visual* demo, the impulse-driven step might be sufficient for this level.

         // Let's refine the visual blocking: The wheel should *look* like it's held.
         // We can't simulate the force blocking accurately without geometry.
         // Let's just ensure the visual update of the wheel corresponds to the impulse events.
         // The current logic does this: the wheel only updates when impulse is detected.

         // Store current angle for next frame's detection
         state.prevBalanceWheelAngle = state.balanceWheelAngle;


        // --- Update Status Display ---
        if (state.isImpulsing) {
            statusDisplay.textContent = `מצב: דחף פעיל (pallet ${state.impulsePalletIndex + 1})`;
        } else {
            // Determine if currently "locked" based on pallet angle relative to release angle
            if (Math.abs(state.balanceWheelAngle) <= releaseAngle * 1.1) { // Check close to center (shouldn't be locked here)
                 statusDisplay.textContent = `מצב: מעבר/מנוחה`;
            } else {
                 // Visually, the wheel is locked when balance wheel is near its peak swing
                 statusDisplay.textContent = `מצב: נעילה`;
            }

        }


        draw();
        animationFrameId = requestAnimationFrame(update);
    }

    function startSimulation() {
        if (!isRunning) {
            isRunning = true;
             // Initialize state for a clean start
             state.balanceWheelAngle = 0;
             state.balanceWheelAngularVelocity = 0.8 * speedFactor; // Initial push to start swinging
             state.palletAngle = 0;
             state.escapeWheelAngle = (Math.PI * 2) / (state.numTeeth * 2) / 2; // Position first tooth engaging with pallet
             state.prevBalanceWheelAngle = 0; // Reset prev angle
             state.currentLockingToothIndex = -1;
             state.isImpulsing = false;
             state.impulsePalletIndex = -1;

            update();
            startButton.disabled = true;
            stopButton.disabled = false;
            resetButton.disabled = false;
            statusDisplay.textContent = 'מצב: פועל...';
        }
    }

     function stopSimulation() {
         if (isRunning) {
             isRunning = false;
             cancelAnimationFrame(animationFrameId);
             startButton.disabled = false;
             stopButton.disabled = true;
             statusDisplay.textContent = 'מצב: מושהה';
         }
     }

     function resetSimulation() {
         stopSimulation(); // Stop any running animation
         // Reset state variables
         state.escapeWheelAngle = (Math.PI * 2) / (state.numTeeth * 2) / 2;
         state.escapeWheelAngularVelocity = 0;
         state.palletAngle = 0;
         state.balanceWheelAngle = 0;
         state.balanceWheelAngularVelocity = 0;
         state.prevBalanceWheelAngle = 0;
         state.currentLockingToothIndex = -1;
         state.isImpulsing = false;
         state.impulsePalletIndex = -1;

         draw(); // Draw reset state
         startButton.disabled = false;
         stopButton.disabled = true;
         resetButton.disabled = true; // Disable reset until started again
         statusDisplay.textContent = 'מצב: מוכן';
     }

    // --- Event Listeners ---
    startButton.addEventListener('click', startSimulation);
    stopButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);
    resetButton.disabled = true; // Initially disabled

    speedSlider.addEventListener('input', (event) => {
        const newSpeedFactor = parseFloat(event.target.value);
        // Adjust velocities/forces based on new speed factor
        // Simple scaling might work visually, but not physically accurate
        const speedRatio = newSpeedFactor / speedFactor;
        state.balanceWheelAngularVelocity *= speedRatio;
        // state.impulseMagnitude *= speedRatio; // Could scale impulse too, but might make motion jumpy

        speedFactor = newSpeedFactor;
        speedValueSpan.textContent = `x${speedFactor.toFixed(1)}`;
    });

    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מפורט';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג הסבר מפורט';
        }
    });

     // --- Initial Setup ---
     // Draw initial state
     draw();
     // Ensure explanation is hidden on load
     explanationDiv.style.display = 'none';
      // Display initial speed value
     speedValueSpan.textContent = `x${speedFactor.toFixed(1)}`;

     // Handle canvas resizing (optional, add if needed for responsiveness)
     // window.addEventListener('resize', () => {
     //     canvas.width = canvas.offsetWidth;
     //     canvas.height = canvas.offsetHeight;
     //     // Need to re-calculate positions based on new canvas size or redraw
     //     state.wheelCenter = { x: canvas.width / 2, y: canvas.height / 2 - 50 };
     //     state.palletPivot = { x: canvas.width / 2 - 40, y: canvas.height / 2 + 80 };
     //     draw();
     // });
     // Trigger initial resize logic if responsive
     // window.dispatchEvent(new Event('resize'));


});
</script>
```