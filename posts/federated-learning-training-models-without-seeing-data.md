---
title: "למידה פדרטיבית: סודות אימון המודלים בלי לאסוף מידע"
english_slug: federated-learning-training-models-without-seeing-data
category: "מדעי המחשב"
tags: [למידה פדרטיבית, למידת מכונה, פרטיות, בינה מלאכותית, אלגוריתמים מבוזרים]
---
<h1>למידה פדרטיבית: סודות אימון המודלים בלי לאסוף מידע</h1>
<p>דמיינו לרגע את המקלדת בסמארטפון שלכם. היא כל הזמן לומדת את ההרגלים הייחודיים שלכם, את המילים שאתם מקלידים, כדי להציע לכם חיזויים והשלמות מדויקות יותר. אבל רגע, האם כל המידע האישי הזה עוזב את הטלפון שלכם ונשלח לשרתים אי שם בעולם? זה מרגיש לא כל כך פרטי, נכון? מה אם נגיד לכם שיש דרך לאמן מודלים חכמים במיוחד על המידע הכי אישי שלכם, מבלי שהמידע עצמו יעזוב את המכשירים שלנו אפילו לרגע?</p>

<div class="federated-simulation-container">
    <div class="server-area">
        <h2>שרת מרכזי</h2>
        <div class="server-block">
             <div class="server-icon">☁️</div> <!-- Changed icon for cloud server feel -->
            <div id="server-status" class="status-text">ממתין לתחילת סבב</div>
            <div class="model-representation">מודל גלובלי</div> <!-- Visual cue -->
        </div>
    </div>
    <div class="clients-area">
        <h2>לקוחות (מכשירים)</h2>
        <div class="clients-container">
            <div class="client-block">
                <h3>לקוח 1</h3>
                <div class="device-icon">📱</div>
                <canvas class="data-canvas" width="200" height="150"></canvas>
                <div class="client-status status-text">ממתין</div>
                <div class="data-hint">המידע שלי</div> <!-- Visual cue -->
            </div>
            <div class="client-block">
                <h3>לקוח 2</h3>
                <div class="device-icon">💻</div>
                <canvas class="data-canvas" width="200" height="150"></canvas>
                <div class="client-status status-text">ממתין</div>
                 <div class="data-hint">המידע שלי</div> <!-- Visual cue -->
            </div>
            <div class="client-block">
                <h3>לקוח 3</h3>
                <div class="device-icon">📱</div>
                <canvas class="data-canvas" width="200" height="150"></canvas>
                <div class="client-status status-text">ממתין</div>
                 <div class="data-hint">המידע שלי</div> <!-- Visual cue -->
            </div>
             <!-- Add more clients if needed, layout will adjust -->
        </div>
    </div>
    <div class="controls-area">
        <div class="controls">
            <button id="run-round-btn">הפעל סבב אימון פדרטיבי</button>
            <div id="round-counter" class="round-text">סבב: 0</div>
        </div>
    </div>
     <!-- This layer is essential for absolute positioning of animations -->
    <div id="animation-layer" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 5;">
        <!-- Animation elements will be added here by JS -->
    </div>
</div>

<button id="toggle-explanation-btn" class="toggle-button">הצג הסבר מלא</button>

<div id="explanation-section" style="display: none;">
    <h2>הסבר מפורט: מסע אל למידה פדרטיבית</h2>
    <p>ברוכים הבאים לעולם הלמידה הפדרטיבית – גישה מהפכנית בלמידת מכונה שמאפשרת לאמן מודלים על כמויות אדירות של נתונים פרטיים, מבלי שהנתונים האלו יעזבו אפילו לרגע את המכשירים שעליהם הם נוצרו. תחשבו על מידע רגיש כמו היסטוריית חיפושים, הרגלי הקלדה, תמונות אישיות או נתונים רפואיים – במקום לשלוח הכל לשרת מרכזי (מה שמסכן את הפרטיות), המודל מגיע אל המידע, ולא להפך.</p>

    <h3>אז איך זה עובד בכלל?</h3>
    <p>במקום לאסוף את כל הנתונים הגולמיים למקום אחד ולאמן שם את המודל (הגישה המסורתית וה"מסוכנת" לפרטיות), בלמידה פדרטיבית התהליך הפוך: השרת שולח עותק של המודל (המודל הגלובלי) למספר מכשירים רנדומליים (לקוחות) שנמצאים במצב מתאים (למשל, מחוברים לוויפיי ובהטענה). הנה שלבי הקסם שחוזרים על עצמם שוב ושוב בסבבים:</p>
    <ol>
        <li><strong>הפצת המודל הגלובלי:</strong> השרת המרכזי (הענן) שולח עותק עדכני של המודל הגלובלי לקבוצה נבחרת של מכשירים שמחוברים כעת. המודל מגיע "ריק" מבחינת הידע על המידע הספציפי של המכשיר, הוא רק יודע מה הוא למד עד כה מכל המכשירים בסבבים קודמים.</li>
        <li><strong>אימון מקומי (בצד הלקוח):</strong> כל מכשיר שקיבל את המודל מבצע עליו מספר קטן של שלבי אימון (למשל, בעזרת אלגוריתם כמו Gradient Descent) תוך שימוש בנתונים הפרטיים שנמצאים עליו בלבד. זה השלב הקריטי: המודל מתעדכן ו"לומד" מהנתונים המקומיים, אבל הנתונים לעולם לא יוצאים מהמכשיר.</li>
        <li><strong>שליחת עדכון המודל (לא נתונים!):</strong> לאחר האימון המקומי, המכשיר לא שולח חזרה את הנתונים האישיים שלו, אלא רק את ה"שינויים" או ה"עדכונים" שהמודל עבר במהלך האימון המקומי. זהו וקטור קטן שמתאר איך המשקולות של המודל השתנו כדי להתאים טוב יותר למידע המקומי. וקטור זה הרבה פחות רגיש מנתונים גולמיים.</li>
        <li><strong>אגרגציה (צבירה ומיצוע) בשרת:</strong> השרת המרכזי אוסף את העדכונים שקיבל ממספר רב של מכשירים. הוא לא מסתכל על עדכון בודד באופן שמסכן פרטיות, אלא מבצע אגרגציה – לרוב, מיצוע משוקלל – של כל העדכונים שהגיעו. זה מייצר עדכון גלובלי משולב שמייצג את הלמידה המשותפת של כל המכשירים שהשתתפו בסבב.</li>
        <li><strong>עדכון המודל הגלובלי:</strong> השרת מיישם את העדכון הגלובלי הממוצע על המודל הגלובלי הקיים. כך נוצרת גרסה חדשה ומשופרת של המודל הגלובלי, שלקחה בחשבון את הלמידה ממגוון רחב של מכשירים, מבלי לראות את הנתונים שלהם.</li>
        <li><strong>חוזרים לסבב חדש:</strong> המודל הגלובלי המעודכן נשלח שוב לקבוצת מכשירים חדשה (או חלקית חופפת), ומתחיל סבב למידה נוסף.</li>
    </ol>
    <p>התהליך הזה חוזר על עצמו מאות או אלפי סבבים. בכל סבב, המודל הגלובלי הולך ומשתפר, משקף את הידע שנצבר ממגוון רחב של משתמשים, כל זאת תוך שמירה קנאית על הפרטיות של הנתונים המקומיים.</p>

    <h3>למה למידה פדרטיבית היא כל כך חשובה?</h3>
    <ul>
        <li><strong>פרטיות ואבטחה אולטימטיבית:</strong> כאמור, הנתונים הרגישים נשארים על המכשיר. הסיכון לדליפת מידע משרת מרכזי פוחת משמעותית.</li>
        <li><strong>חיסכון משמעותי בתקשורת:</strong> שליחת עדכוני מודל קטנים חסכונית בהרבה משליחת כמויות ענק של נתונים גולמיים.</li>
        <li><strong>עמידה ברגולציות:</strong> שיטה זו מסייעת לעמוד בתקנות פרטיות מחמירות כמו GDPR, המחייבות שמידע אישי לא יעזוב את מקורו ללא צורך.</li>
        <li><strong>למידה ממידע מקומי אמיתי:</strong> המודל לומד מהתנהגות משתמש בזמן אמת, על המכשירים עצמם, היכן שהנתונים הכי רלוונטיים ועדכניים נוצרים.</li>
    </ul>

    <h3>איפה פוגשים למידה פדרטיבית?</h3>
    <ul>
        <li><strong>מקלדות חכמות:</strong> כמו Gboard של גוגל, לשיפור חיזוי טקסט והשלמה אוטומטית מבלי לשלוח היסטוריית הקלדה אישית.</li>
        <li><strong>בריאות:</strong> אימון מודלים לזיהוי מחלות או ניתוח תמונות רפואיות על נתונים בבתי חולים שונים, בלי להפר סודיות רפואית.</li>
        <li><strong>מכשירי IoT:</strong> שיפור זיהוי קולי, איתור אנומליות או התאמה אישית במכשירים חכמים בבית או בתעשייה.</li>
        <li><strong>זיהוי אובייקטים ותמונות:</strong> שיפור היכולת לזהות תוכן בתמונות שמאוחסנות באופן פרטי.</li>
    </ul>

    <h3>לא הכל ורוד: אתגרים בלמידה פדרטיבית</h3>
    <ul>
        <li><strong>הטרוגניות נתונים ומכשירים:</strong> המכשירים שונים מאוד ביכולותיהם, והנתונים על כל מכשיר יכולים להיות שונים מאוד בכמות ובמאפיינים (מה שמכונה Non-IID data).</li>
        <li><strong>אתגרי תקשורת:</strong> למרות החיסכון, עדיין נדרשת תקשורת אמינה עם המכשירים, שיכולים להתנתק ("נשירה").</li>
        <li><strong>אבטחה ופרטיות מורכבות:</strong> למרות שנתונים גולמיים לא נחשפים, ישנן התקפות מתקדמות שמנסות לשחזר מידע רגיש מתוך וקטורי העדכון. דורש שימוש בטכניקות נוספות כמו פרטיות דיפרנציאלית או הצפנה.</li>
        <li><strong>מורכבות אלגוריתמית:</strong> פיתוח וניהול אלגוריתמי אימון פדרטיבי יעילים דורש הבנה עמוקה ומחקר מתמשך.</li>
    </ul>

    <p>לסיכום, למידה פדרטיבית היא גישה אלגנטית וחזקה שמאפשרת לנצל את העוצמה של בינה מלאכותית ולמידת מכונה בקנה מידה גדול, תוך מתן עדיפות עליונה לפרטיות ואבטחת המידע האישי שלנו בעולם מרובה מכשירים.</p>

</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #28a745; /* Green */
        --dark-text: #333;
        --light-text: #666;
        --border-color: #e0e0e0;
        --background-light: #f8f9fa; /* Very light gray */
        --background-white: #fff;
        --shadow-subtle: 0 2px 5px rgba(0,0,0,0.08);
        --border-radius: 8px;
        --spacing-medium: 20px;
        --spacing-large: 30px;
    }

    body {
        font-family: 'Arial Hebrew', sans-serif; /* Use a common Hebrew font */
        line-height: 1.7; /* Slightly increased line height */
        direction: rtl;
        text-align: right;
        padding: var(--spacing-medium);
        color: var(--dark-text);
        background-color: var(--background-light);
    }

    h1, h2, h3 {
        color: var(--dark-text);
        text-align: right;
        margin-bottom: 15px;
    }

    h1 { font-size: 2em; margin-bottom: var(--spacing-medium); }
    h2 { font-size: 1.5em; margin-top: var(--spacing-large); }
    h3 { font-size: 1.2em; margin-top: var(--spacing-medium); }

    p, ul, ol {
         text-align: right;
         margin-bottom: 15px;
         color: var(--light-text);
    }

    ul, ol {
        padding-right: 20px; /* Indent lists */
    }

    li {
        margin-bottom: 8px;
    }

    .federated-simulation-container {
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: var(--spacing-medium);
        margin: var(--spacing-large) 0;
        background-color: var(--background-white);
        box-shadow: var(--shadow-subtle);
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative; /* Needed for animation layer */
        overflow: hidden; /* Hide overflowing animation particles */
    }

    .server-area, .clients-area, .controls-area {
        width: 100%;
        margin-bottom: var(--spacing-medium);
        padding-bottom: var(--spacing-medium); /* Add space below each area */
        border-bottom: 1px dashed var(--border-color); /* Visual separator */
    }

    .server-area h2, .clients-area h2 {
        text-align: center; /* Center the area titles */
        margin-bottom: var(--spacing-medium);
        color: var(--primary-color); /* Color area titles */
    }

    .server-area {
        border-bottom: 1px dashed var(--border-color);
        margin-bottom: var(--spacing-large); /* More space after server */
        padding-bottom: var(--spacing-large);
    }

    .server-block {
        text-align: center;
        background-color: var(--background-light); /* Light background for server block */
        padding: var(--spacing-medium);
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
        display: inline-block; /* Center the block itself */
        margin: 0 auto; /* Center the block */
        min-width: 180px;
    }

    .server-icon, .device-icon {
        font-size: 4em; /* Larger icons */
        margin-bottom: 10px;
        line-height: 1; /* Prevent extra space around icon */
    }

    .server-icon { color: var(--primary-color); } /* Blue icon for server/model */
    .device-icon { color: var(--secondary-color); } /* Green icon for clients/data */


    .model-representation, .data-hint {
        font-size: 0.9em;
        color: var(--light-text);
        margin-top: 5px;
    }


    .clients-container {
        display: flex;
        justify-content: center;
        gap: var(--spacing-medium); /* Space between clients */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .client-block {
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 15px;
        background-color: var(--background-white);
        text-align: center;
        width: 220px; /* Fixed width for clients */
        box-shadow: var(--shadow-subtle);
        display: flex; /* Use flex for internal layout */
        flex-direction: column;
        align-items: center;
    }

    .client-block h3 {
        margin-top: 0;
        margin-bottom: 10px;
        color: var(--dark-text);
    }


    .data-canvas {
        border: 1px solid var(--border-color);
        background-color: var(--background-white);
        margin-bottom: 10px;
         /* Ensure canvas fits within flex item */
        max-width: 100%;
        height: auto; /* Maintain aspect ratio or let JS handle height */
    }

    .status-text {
        font-size: 0.9em;
        color: var(--light-text);
        min-height: 1.2em; /* Reserve space */
        transition: color 0.3s ease; /* Smooth transition for status text color */
    }

     #server-status.busy, .client-status.busy {
        color: var(--primary-color); /* Highlight status when busy */
        font-weight: bold;
     }
     #server-status.success, .client-status.success {
         color: var(--secondary-color); /* Highlight status when done/successful */
     }


    .controls-area {
        border-bottom: none; /* No border after controls */
        padding-bottom: 0;
    }

    .controls {
        margin-top: 10px;
        text-align: center;
    }

    #run-round-btn {
        padding: 12px 25px; /* Bigger button */
        font-size: 1.1em;
        cursor: pointer;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        margin-bottom: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #run-round-btn:hover:not(:disabled) {
        background-color: #0056b3; /* Darker blue on hover */
    }
    #run-round-btn:active:not(:disabled) {
         transform: scale(0.98); /* Press effect */
    }


    #run-round-btn:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        opacity: 0.8;
    }

    #round-counter {
        font-weight: bold;
        font-size: 1.1em;
        color: var(--dark-text);
    }

    .toggle-button {
        display: block;
        margin: var(--spacing-large) auto; /* Center the button */
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: var(--background-white);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        color: var(--dark-text);
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .toggle-button:hover {
        background-color: var(--background-light);
        border-color: #ccc;
    }


    #explanation-section {
        margin-top: var(--spacing-large);
        border-top: 1px dashed var(--border-color);
        padding-top: var(--spacing-large);
    }

    /* Animation styles */
    .packet {
        position: absolute;
        width: 18px; /* Slightly larger packets */
        height: 18px;
        border-radius: 50%;
        pointer-events: none;
        z-index: 10;
        opacity: 0; /* Start invisible */
        transition: transform 1.8s ease-in-out, opacity 0.5s ease-in; /* Longer animation, opacity fade */
    }

    .data-packet {
        background-color: var(--secondary-color); /* Green for data/updates */
        box-shadow: 0 0 8px var(--secondary-color); /* Glow effect */
    }

     .model-packet {
        background-color: var(--primary-color); /* Blue for model */
        box-shadow: 0 0 8px var(--primary-color); /* Glow effect */
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const canvases = document.querySelectorAll('.data-canvas');
        const contexts = Array.from(canvases).map(canvas => canvas.getContext('2d'));
        const clientStatuses = document.querySelectorAll('.client-status');
        const serverStatus = document.getElementById('server-status');
        const runRoundBtn = document.getElementById('run-round-btn');
        const roundCounter = document.getElementById('round-counter');
        const animationLayer = document.getElementById('animation-layer');
        const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
        const explanationSection = document.getElementById('explanation-section');

        const numClients = canvases.length;
        const data = []; // Array to hold data for each client
        // Initial model parameters (simple linear regression y = mx + b)
        // Start with parameters that roughly center the initial line in the canvas view
        const globalModel = { m: 0.5, b: 50 };
        const learningRate = 0.0005; // Rate for gradient descent
        const epochsPerRound = 10; // Number of local training steps per client per round
        const animationDuration = 1800; // Milliseconds for packet animation
        const stepDelay = 600; // Delay between major animation steps

        let round = 0;
        let isAnimating = false;

        // --- Data Generation ---
        function generateData(clientIndex, numPoints = 50) {
            const clientData = [];
            // Base line parameters vary slightly per client for a Non-IID effect
            // Spread slopes and intercepts
            const baseM = 0.4 + (clientIndex / numClients) * 0.3; // Slope between 0.4 and 0.7
            const baseB = 40 + (clientIndex / numClients) * 30; // Intercept between 40 and 70
            const noiseLevel = 20; // Increased noise for more realistic scatter

            for (let i = 0; i < numPoints; i++) {
                const normalizedX = Math.random() * 100; // x from 0 to 100
                const trueNormalizedY = baseM * normalizedX + baseB;
                const normalizedY = trueNormalizedY + (Math.random() - 0.5) * 2 * noiseLevel; // Add noise
                 // Clamp Y values to keep them somewhat within a reasonable range for visualization
                clientData.push({ x: normalizedX, y: Math.max(-50, Math.min(150, normalizedY)) });
            }
            // Optional: Sort by x for cleaner drawing if lines connect points
            // clientData.sort((a, b) => a.x - b.x);
            return clientData;
        }

        for (let i = 0; i < numClients; i++) {
            data.push(generateData(i));
        }

        // --- Drawing Functions ---
         // Scales a normalized X value (0-100) to canvas X coordinate
        function scaleXToCanvas(x, canvas) {
            return (x / 100) * canvas.width;
        }

        // Scales a normalized Y value (mapping from data range -50 to 150) to canvas Y coordinate
        // Canvas Y=0 is top, Y=canvas.height is bottom. Data Y=-50 should be near top, 150 near bottom.
         function scaleYToCanvas(y, canvas) {
            const dataMinY = -50;
            const dataMaxY = 150;
            const dataRangeY = dataMaxY - dataMinY;

            // Normalize Y within the data range (0 to 1)
            const normalizedY = (y - dataMinY) / dataRangeY;

            // Map normalized Y to canvas height (0 at top, 1 at bottom)
            // Since canvas Y=0 is top, we use (1 - normalizedY) to invert the scale
            return canvas.height * (1 - normalizedY);
         }


        function drawData(ctx, clientData) {
            ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
            ctx.fillStyle = var('--secondary-color'); // Green for data points
            clientData.forEach(point => {
                const canvasX = scaleXToCanvas(point.x, ctx.canvas);
                const canvasY = scaleYToCanvas(point.y, ctx.canvas);
                 // Draw circle
                ctx.beginPath();
                ctx.arc(canvasX, canvasY, 3, 0, Math.PI * 2); // Slightly larger points
                ctx.fill();
            });
        }

        function drawModel(ctx, model, color = var('--primary-color')) {
            ctx.strokeStyle = color;
            ctx.lineWidth = 3; // Thicker line
            ctx.beginPath();

            // Define two points on the line using the model y = mx + b
            // Use X values corresponding to the edges of our normalized data range (0 and 100)
            const x1 = 0;
            const y1 = model.m * x1 + model.b;
            const x2 = 100;
            const y2 = model.m * x2 + model.b;

            // Scale these points to canvas coordinates
            const canvasX1 = scaleXToCanvas(x1, ctx.canvas);
            const canvasY1 = scaleYToCanvas(y1, ctx.canvas);
            const canvasX2 = scaleXToCanvas(x2, ctx.canvas);
            const canvasY2 = scaleYToCanvas(y2, ctx.canvas);

            ctx.moveTo(canvasX1, canvasY1);
            ctx.lineTo(canvasX2, canvasY2);
            ctx.stroke();
        }

        function drawAllClients(modelToDraw = globalModel) {
             data.forEach((clientData, i) => {
                drawData(contexts[i], clientData);
                // Draw the specified model (global by default) on all clients
                drawModel(contexts[i], modelToDraw);
            });
        }

         // --- Training Logic (Simplified Linear Regression) ---
        // Calculate gradient for a simple linear model (MSE loss)
        function calculateGradient(model, data) {
            let sumGradientsM = 0;
            let sumGradientsB = 0;
            const N = data.length;

            if (N === 0) return { gradM: 0, gradB: 0 }; // Avoid division by zero

            data.forEach(point => {
                const prediction = model.m * point.x + model.b;
                const error = prediction - point.y; // (predicted - actual)

                // Gradient of MSE with respect to m: (1/N) * sum(2 * error * x)
                sumGradientsM += error * point.x;
                 // Gradient of MSE with respect to b: (1/N) * sum(2 * error * 1)
                sumGradientsB += error;
            });

             // Average gradient
            const gradM = (2 / N) * sumGradientsM;
            const gradB = (2 / N) * sumGradientsB;

            return { gradM, gradB };
        }

        // Perform local training steps (Gradient Descent)
        function localTrain(startModel, clientData, epochs, lr) {
            let currentModel = { ...startModel }; // Copy the global model

            // Store intermediate models for visualization
            const intermediateModels = [];
            intermediateModels.push({ ...currentModel }); // Add initial model

            for(let i = 0; i < epochs; i++) {
                 const { gradM, gradB } = calculateGradient(currentModel, clientData);
                 currentModel.m -= lr * gradM;
                 currentModel.b -= lr * gradB;
                 intermediateModels.push({ ...currentModel }); // Store after each step
            }

            // Return the difference/update vector and intermediate steps
            const update = {
                 deltaM: currentModel.m - startModel.m,
                 deltaB: currentModel.b - startModel.b
            };
            return { finalModel: currentModel, update: update, intermediateModels: intermediateModels };
        }

        // Aggregate updates (Simple Averaging)
        function aggregateUpdates(updates) {
            if (updates.length === 0) return { avgDeltaM: 0, avgDeltaB: 0 };

            let sumDeltaM = 0;
            let sumDeltaB = 0;

            updates.forEach(update => {
                sumDeltaM += update.deltaM;
                sumDeltaB += update.deltaB;
            });

            const avgDeltaM = sumDeltaM / updates.length;
            const avgDeltaB = sumDeltaB / updates.length;

            return { avgDeltaM, avgDeltaB };
        }

        // --- Animation Functions ---
        function createPacket(className = 'packet model-packet') { // Default to model packet
             const packet = document.createElement('div');
             packet.className = className;
             animationLayer.appendChild(packet);
             return packet;
        }

         function getElementCenter(element) {
             const rect = element.getBoundingClientRect();
             const containerRect = animationLayer.parentElement.getBoundingClientRect();
             return {
                 x: rect.left + rect.width / 2 - containerRect.left,
                 y: rect.top + rect.height / 2 - containerRect.top
             };
         }

         function animatePacket(packet, startElement, endElement) {
             const startPos = getElementCenter(startElement);
             const endPos = getElementCenter(endElement);

             // Set initial position (using transform for smooth animation)
             packet.style.transform = `translate(${startPos.x}px, ${startPos.y}px)`;
             packet.style.opacity = 1; // Make visible


             // Trigger animation after a small delay to allow initial position to set
             requestAnimationFrame(() => {
                 requestAnimationFrame(() => { // Double rAF for smooth start
                     packet.style.transform = `translate(${endPos.x}px, ${endPos.y}px)`;
                 });
             });

             // Return a promise that resolves when the animation ends
             return new Promise(resolve => {
                 packet.addEventListener('transitionend', () => {
                     packet.remove(); // Clean up the element
                     resolve();
                 }, { once: true });
             });
         }

        // --- Main Training Round Logic ---
        async function runTrainingRound() {
            if (isAnimating) return; // Prevent multiple clicks
            isAnimating = true;
            runRoundBtn.disabled = true;
            round++;
            roundCounter.textContent = `סבב: ${round}`;
            serverStatus.classList.remove('success', 'busy');
            clientStatuses.forEach(s => s.classList.remove('success', 'busy'));


            const currentGlobalModel = { ...globalModel };
            const clientUpdates = [];
            const clientLocalTrainResults = []; // To store updates and intermediate models

            serverStatus.textContent = 'מאפס מודל גלובלי...';
            // Small pause to acknowledge start
            await new Promise(resolve => setTimeout(resolve, stepDelay));

            serverStatus.textContent = 'שולח מודל ללקוחות...';
            serverStatus.classList.add('busy');
            // Animation: Server sending model to clients
            const serverElement = animationLayer.parentElement.querySelector('.server-block .server-icon');
            const clientIconElements = Array.from(animationLayer.parentElement.querySelectorAll('.client-block .device-icon'));

            const sendModelPromises = clientIconElements.map((clientEl, i) => {
                 clientStatuses[i].textContent = 'מקבל מודל...';
                 clientStatuses[i].classList.add('busy');
                 const packet = createPacket('packet model-packet');
                 return animatePacket(packet, serverElement, clientEl);
            });
            await Promise.all(sendModelPromises);
            serverStatus.classList.remove('busy');


            // Phase 1: Local Training on Clients
            serverStatus.textContent = 'ממתין לעדכונים מהלקוחות...';
            const localTrainPromises = data.map(async (clientData, i) => {
                clientStatuses[i].textContent = 'מאמן מקומית...';
                clientStatuses[i].classList.add('busy');

                // Perform local training and get results
                const trainResult = localTrain(currentGlobalModel, clientData, epochsPerRound, learningRate);
                clientLocalTrainResults[i] = trainResult; // Store result

                // --- Animate Local Training on Canvas ---
                const ctx = contexts[i];
                const intermediateModels = trainResult.intermediateModels;
                const drawInterval = animationDuration / epochsPerRound / 1.5; // Time for each little line step

                for (let j = 0; j < intermediateModels.length; j++) {
                    drawData(ctx, clientData); // Redraw data points
                    // Draw the intermediate local model in a different color (e.g., green)
                    drawModel(ctx, intermediateModels[j], var('--secondary-color'));
                    await new Promise(resolve => setTimeout(resolve, drawInterval));
                }

                // --- End Local Training Animation ---

                clientStatuses[i].textContent = 'שולח עדכון לשרת...';
                 clientStatuses[i].classList.remove('busy');
                clientStatuses[i].classList.add('success');


                // Redraw global model line before sending update packet
                drawData(ctx, clientData);
                drawModel(ctx, currentGlobalModel, var('--primary-color'));


                // Animation: Client sending update to Server
                const packet = createPacket('packet data-packet'); // Update packet is green
                return animatePacket(packet, clientIconElements[i], serverElement);
            });

            await Promise.all(localTrainPromises);
            clientStatuses.forEach(s => s.classList.remove('success'));


            // Phase 2: Aggregation on Server
            serverStatus.textContent = 'מבצע אגרגציה של עדכונים...';
             serverStatus.classList.add('busy');
             // Collect all updates after all local training is done
            const allUpdates = clientLocalTrainResults.map(result => result.update);
            const { avgDeltaM, avgDeltaB } = aggregateUpdates(allUpdates);

            // Simulate aggregation visualization (updates swirling before merging)
            const aggregationDelay = animationDuration / 2; // Brief swirl time
            await new Promise(resolve => setTimeout(resolve, aggregationDelay));


            // Update global model
            globalModel.m += avgDeltaM;
            globalModel.b += avgDeltaB;

             serverStatus.classList.remove('busy');
             serverStatus.classList.add('success');
             await new Promise(resolve => setTimeout(resolve, stepDelay)); // Pause after aggregation


            // Phase 3: Server sends updated model back to Clients
            serverStatus.textContent = 'שולח מודל גלובלי מעודכן...';
            serverStatus.classList.remove('success');
             serverStatus.classList.add('busy');

            const sendUpdatedModelPromises = clientIconElements.map((clientEl, i) => {
                 clientStatuses[i].textContent = 'מקבל מודל מעודכן...';
                 clientStatuses[i].classList.add('busy');
                 const packet = createPacket('packet model-packet'); // Model packet is blue
                 return animatePacket(packet, serverElement, clientEl);
            });
            await Promise.all(sendUpdatedModelPromises);


            // Update client views with the new global model and finalize round
            serverStatus.textContent = 'סבב הושלם.';
            serverStatus.classList.remove('busy');
            serverStatus.classList.add('success');

            clientStatuses.forEach(statusEl => {
                statusEl.textContent = 'ממתין לסבב הבא';
                statusEl.classList.remove('busy');
                statusEl.classList.add('success');
            });

            drawAllClients(); // Redraw everything with the final updated global model

             await new Promise(resolve => setTimeout(resolve, stepDelay)); // Pause before enabling button


            isAnimating = false;
            runRoundBtn.disabled = false;
            clientStatuses.forEach(s => s.classList.remove('success'));
             serverStatus.classList.remove('success');
        }

        // --- Initial Drawing ---
        drawAllClients(); // Draw initial state with the starting global model

        // --- Event Listeners ---
        runRoundBtn.addEventListener('click', runTrainingRound);

        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationSection.style.display === 'none';
            explanationSection.style.display = isHidden ? 'block' : 'none';
            toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר מלא';
            // Optional: Scroll to the explanation section if showing it
            if (isHidden) {
                explanationSection.scrollIntoView({ behavior: 'smooth' });
            }
        });

         // --- Handle basic responsiveness (redraw on resize) ---
         // Note: Canvas element itself has fixed width/height attributes in HTML,
         // which limits true responsiveness. This redraw just makes sure
         // drawing scales correctly within the current *rendered* size,
         // but the canvas element won't resize automatically based on CSS alone
         // unless the HTML attributes are removed or managed by JS.
         // For strict structure adherence, we keep attributes and redraw.
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                // Re-get canvas dimensions which might have changed due to CSS layout
                // though fixed attributes might override this.
                drawAllClients(); // Redraw data and model
            }, 100); // Debounce
        });

         // Initial drawing again to ensure everything is rendered after setup
         drawAllClients();

    });
</script>
---