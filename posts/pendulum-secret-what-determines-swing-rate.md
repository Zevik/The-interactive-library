---
title: "סוד המטוטלת: מה קובע את קצב הנדנוד?"
english_slug: pendulum-secret-what-determines-swing-rate
category: "פיזיקה"
tags: ["מטוטלת", "פיזיקה", "תנועה מחזורית", "זמן מחזור", "הדמיה מדעית"]
---
# סוד המטוטלת: מה קובע את קצב הנדנוד?

האם שמת לב פעם שלכל נדנדה בגן שעשועים יש קצב קבוע? או שתהית למה מטוטלת של שעון עתיק שומרת על תיזמון מדויק? צא למסע גילוי! שחק עם הגורמים השונים המשפיעים על המקצב המסתורי הזה – וגלה בעצמך אילו גורמים מכריעים ואילו מפתיעים במיוחד בכך שאינם משפיעים עליו כלל.

<div id="pendulum-app">
    <div class="controls">
        <h2>מעבדת המטוטלת שלך:</h2>
        <div class="control-group">
            <label for="length-slider">אורך החוט (מטר): <span id="length-value">1.0</span></label>
            <input type="range" id="length-slider" min="0.1" max="3.0" value="1.0" step="0.1">
        </div>

        <div class="control-group">
            <label for="mass-slider">מסת המשקולת (ק"ג): <span id="mass-value">1.0</span></label>
            <input type="range" id="mass-slider" min="0.1" max="5.0" value="1.0" step="0.1">
        </div>

        <div class="control-group">
            <label for="angle-slider">זווית התחלתית (מעלות): <span id="angle-value">15</span></label>
            <input type="range" id="angle-slider" min="5" max="90" value="15" step="1">
        </div>

        <div class="buttons">
            <button id="start-button"><i class="fas fa-play"></i> הפעל/השהה</button>
            <button id="reset-button"><i class="fas fa-redo"></i> איפוס</button>
        </div>

        <div class="period-display">
            <h3>תוצאות המדידה:</h3>
            <p>זמן מחזור נמדד: <span id="measured-period" class="result-value">--</span> שניות</p>
            <p>זמן מחזור צפוי (תיאורטי): <span id="predicted-period" class="result-value">--</span> שניות</p>
            <p class="hint">שנה את אורך החוט וצפה בשינוי הצפוי והנמדד!</p>
        </div>
    </div>

    <div class="simulation-area">
        <canvas id="pendulum-canvas" width="500" height="400"></canvas>
        <div id="origin-point"></div>
    </div>
</div>

<button id="toggle-explanation" class="explanation-toggle-button">הצג/הסתר הסבר מפורט</button>

<div id="explanation" class="explanation-section">
    <h2>הסבר מפורט: סוד המטוטלת נחשף!</h2>

    <p>שיחקת, התנסית ושינית את הפרמטרים. עכשיו הגיע הזמן להבין לעומק את הפיזיקה מאחורי תנועת המטוטלת ולוודא שהתגליות שלך תואמות את התיאוריה!</p>

    <h3>מהי מטוטלת פשוטה? (המודל האידיאלי)</h3>
    <p>דמיין משקולת קטנה ודחוסה התלויה על חוט דקיק, חסר משקל ובלתי נמתח, המחובר לנקודה קבועה. זהו המודל האידיאלי של מטוטלת פשוטה בפיזיקה. נדנדה או משקולת אמיתית הן קירוב טוב למודל זה, בהזנחת חיכוך אוויר והתנגדות בציר הסיבוב.</p>

    <h3>זמן מחזור (<span class="formula">T</span>): קצב הלב של התנועה המחזורית</h3>
    <p>תנועה מחזורית היא כל תנועה שחוזרת על עצמה שוב ושוב במרווחי זמן קבועים. זמן המחזור הוא בדיוק הזמן שלוקח לגוף להשלים מחזור תנועה שלם אחד ולחזור לנקודת המוצא שלו עם אותה מהירות ובאותו כיוון. במטוטלת, מחזור אחד הוא התנועה מצד אחד, דרך נקודת שיווי המשקל, לצד השני, וחזרה לנקודת ההתחלה.</p>

    <h3>התנועה ההרמונית הפשוטה: הסוד לחישובים קלים</h3>
    <p>כאשר המטוטלת מתנדנדת בזוויות קטנות יחסית (בדרך כלל עד כ-15-20 מעלות מהאנך), תנועתה דומה מאוד לתנועה הרמונית פשוטה (תַח"ף). בתנועה כזו, כוח ההחזרה שמחזיר את המטוטלת לנקודת שיווי המשקל פרופורציונלי לגודל הסטייה שלה ממנה. זהו קירוב שמאפשר לנו להשתמש בנוסחאות פשוטות ואלגנטיות לתיאור התנועה וחישוב זמן המחזור.</p>

    <h3>הגורמים שבאמת קובעים את זמן המחזור:</h3>
    <ul>
        <li><strong>אורך החוט (<span class="formula">L</span>):</strong> כמו שוודאי גילית בסימולציה, זהו הגורם המרכזי! ככל שהחוט ארוך יותר, זמן המחזור גדל (הנדנוד איטי יותר). הקשר אינו ליניארי, אלא פרופורציונלי לשורש הריבועי של האורך. הסיבה היא שחוט ארוך יותר "מאפשר" מסלול ארוך יותר באותה זווית, והרכיב המשיקי של כוח הכובד שמחזיר את המטוטלת למרכז יחסי פחות לזווית עבור אותה תזוזה קווית.</li>
        <li><strong>תאוצת הכובד (<span class="formula">g</span>):</strong> כוח הכובד של כדור הארץ (או של כל גרם שמיים אחר) הוא זה שגורם למטוטלת להתנדנד. תאוצת הכובד משתנה מעט ממקום למקום על פני כדור הארץ (והרבה יותר על הירח או מאדים!). בסימולציה, <span class="formula">g</span> קבוע (בערך 9.8 מטר לשנייה בריבוע), אך במקומות בהם <span class="formula">g</span> גבוה יותר, המטוטלת תתנדנד מהר יותר (זמן מחזור קטן יותר).</li>
    </ul>

    <h3>הגורמים שבאופן מפתיע *אינם* משפיעים (עבור זוויות קטנות):</h3>
    <ul>
        <li><strong>מסת המשקולת (<span class="formula">m</span>):</strong> האם שינוי מסת המשקולת שינה את קצב הנדנוד בסימולציה? עבור זוויות קטנות, התשובה היא "כמעט ולא"! הסיבה היא שגם כוח הכובד שמושך את המסה למטה (<span class="formula">F = mg</span>) וגם ההתנגדות של המסה לשינוי בתנועה (האינרציה) – שניהם פרופורציונליים למסה (<span class="formula">m</span>). המסה פשוט "מצטמצמת" מחוץ למשוואות התנועה עבור המודל האידיאלי.</li>
        <li><strong>המשרעת (הזווית ההתחלתית):</strong> זה אולי הכי מפתיע! עבור זוויות התחלתיות קטנות, גודל הנדנוד כמעט ואינו משפיע על הזמן שלוקח להשלים מחזור. זה נקרא "איזוכרוניזם" (שוויון זמנים) והוא מאפיין מפתח של תנועה הרמונית פשוטה. שימו לב שבסימולציה, כשתגדילו מאוד את הזווית (מעל 20 מעלות), תבחינו בכל זאת בשינוי קטן בזמן המחזור - הנוסחה הפשוטה כבר פחות מדויקת שם, והקירוב של תַח"ף פחות תקף.</li>
    </ul>

    <h3>הנוסחה המכריעה (לזוויות קטנות):</h3>
    <p>הנה הנוסחה היפה שמסכמת את כל זה עבור מטוטלת פשוטה וזווית קטנות:</p>
    <p class="formula" style="font-size: 1.5em; text-align: center;">T = 2π * sqrt(L / g)</p>
    <p>הנוסחה מראה בבירור: זמן המחזור (<span class="formula">T</span>) תלוי רק ב- <span class="formula">L</span> (אורך החוט) וב- <span class="formula">g</span> (תאוצת הכובד), ואינו תלוי ב- <span class="formula">m</span> (המסה) או בזווית ההתחלתית (לזוויות קטנות). השתמשו בסימולציה כדי לאמת זאת!</p>

    <h3>איפה פוגשים מטוטלות בחיי היומיום?</h3>
    <ul>
        <li><strong>שעוני מטוטלת עתיקים:</strong> דיוק השעון מבוסס על הקצב הקבוע של המטוטלת.</li>
        <li><strong>מטרונומים:</strong> מכשירים שקובעים קצב אחיד למוזיקאים.</li>
        <li><strong>נדנדות:</strong> פשוט כמו שזה נשמע - נדנדה היא מטוטלת גדולה!</li>
        <li><strong>בדיקת כוח הכובד:</strong> ניתן למדוד את תאוצת הכובד המקומית על ידי מדידת זמן המחזור של מטוטלת באורך ידוע.</li>
    </ul>
    <p>עכשיו, כשאתם מבינים את התיאוריה, חזרו לסימולציה ושחקו שוב. נסו לחזות את זמן המחזור לפני שאתם משנים את אורך החוט, ובדקו אם אתם צודקים!</p>
</div>


<style>
    /* שיפורים עיצוביים כלליים */
    #pendulum-app {
        display: flex;
        flex-direction: row;
        gap: 40px;
        padding: 30px;
        border: none; /* Remove basic border */
        border-radius: 12px; /* Softer corners */
        background: linear-gradient(to bottom right, #eef4f8, #c9d8e1); /* Gentle gradient background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Soft shadow */
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif; /* Clearer font */
        color: #333;
        margin: 20px 0;
    }

    @media (max-width: 768px) {
        #pendulum-app {
            flex-direction: column;
            gap: 20px;
            padding: 20px;
        }
        #pendulum-app .controls {
            min-width: auto;
        }
    }

    #pendulum-app h2 {
        color: #0056b3; /* Darker blue for headings */
        margin-top: 0;
        border-bottom: 2px solid #007bff; /* Highlight heading */
        padding-bottom: 10px;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    #pendulum-app .controls {
        flex: 1;
        min-width: 300px; /* Wider controls area */
        background-color: #ffffff; /* White background for controls */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    #pendulum-app .control-group {
        margin-bottom: 20px; /* More space between control groups */
    }

    #pendulum-app .controls label {
        display: block;
        margin-bottom: 8px; /* More space below label */
        font-weight: bold;
        color: #555;
        font-size: 1.1em;
    }

    #pendulum-app .controls input[type="range"] {
        width: 100%;
        height: 8px; /* Thicker slider track */
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        background: #ddd;
        outline: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background 0.2s ease-in-out;
    }

    #pendulum-app .controls input[type="range"]:hover {
         background: #ccc;
    }

    /* Custom slider thumb */
    #pendulum-app .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* Larger thumb */
        height: 20px; /* Larger thumb */
        background: #007bff;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: background 0.2s ease-in-out, transform 0.1s ease-in-out;
    }

    #pendulum-app .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
         transition: background 0.2s ease-in-out;
    }

    #pendulum-app .controls input[type="range"]::-webkit-slider-thumb:active {
        background: #0056b3;
        transform: scale(1.1);
    }
     #pendulum-app .controls input[type="range"]::-moz-range-thumb:active {
        background: #0056b3;
    }


    #pendulum-app .controls .buttons {
        margin-top: 30px; /* More space above buttons */
        display: flex;
        gap: 15px; /* More space between buttons */
    }

    #pendulum-app .controls button {
        padding: 12px 20px; /* Larger buttons */
        background-color: #28a745; /* Green for Start */
        color: white;
        border: none;
        border-radius: 6px; /* Softer corners */
        cursor: pointer;
        font-size: 1.1em;
        flex-grow: 1;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
        display: flex; /* Align icon and text */
        align-items: center;
        justify-content: center;
        gap: 8px; /* Space between icon and text */
    }
     #pendulum-app .controls button#reset-button {
         background-color: #dc3545; /* Red for Reset */
     }

     #pendulum-app .controls button:hover {
        opacity: 0.9; /* Slight opacity change on hover */
     }

     #pendulum-app .controls button:active {
        transform: scale(0.98); /* Slight press effect */
        background-color: #004085; /* Darker blue when active */
     }
      #pendulum-app .controls button#reset-button:active {
         background-color: #c82333; /* Darker red when active */
     }


    #pendulum-app .period-display {
        margin-top: 30px; /* More space above results */
        padding-top: 20px;
        border-top: 1px dashed #ccc; /* Separator */
        font-size: 1.1em;
        color: #333;
    }

    #pendulum-app .period-display h3 {
        margin-top: 0;
        color: #0056b3;
        margin-bottom: 10px;
    }

    #pendulum-app .period-display p {
        margin-bottom: 8px;
        font-weight: bold;
    }

    #pendulum-app .period-display .result-value {
        color: #007bff; /* Blue for results */
        font-size: 1.2em;
        font-weight: bold;
    }
     #pendulum-app .period-display .hint {
         font-size: 0.9em;
         color: #555;
         font-weight: normal;
         margin-top: 15px;
     }


    #pendulum-app .simulation-area {
        flex: 2;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid #ddd; /* Keep light border for canvas area */
        background-color: #eef7ff; /* Light blue background for simulation */
        position: relative; /* Needed for origin point positioning */
        overflow: hidden; /* Hide overflow from trace */
         border-radius: 8px;
         box-shadow: inset 0 0 8px rgba(0,0,0,0.05); /* Inner shadow */
    }

     #pendulum-canvas {
        display: block;
        background-color: transparent; /* Canvas background handled by parent */
    }

     /* Origin point indicator */
    #origin-point {
        position: absolute;
        top: 50px; /* Should match originY in JS */
        left: 50%;
        transform: translateX(-50%);
        width: 12px;
        height: 12px;
        background-color: #000;
        border-radius: 50%;
        z-index: 1; /* Above canvas */
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }


    /* Style for the explanation section */
    .explanation-section {
        margin-top: 30px;
        padding: 30px; /* More padding */
        border: none;
        border-radius: 12px;
        background-color: #fff; /* White background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        display: none; /* Initially hidden */
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
        line-height: 1.7; /* Better readability */
         color: #333;
    }

    .explanation-section h2 {
        margin-top: 0;
        color: #0056b3;
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

     .explanation-section h3 {
        margin-top: 25px; /* More space above subheadings */
        margin-bottom: 12px;
        color: #007bff; /* Blue for subheadings */
        font-size: 1.3em;
    }

    .explanation-section p, .explanation-section ul {
        margin-bottom: 15px;
    }

    .explanation-section ul {
        padding-right: 25px; /* Deeper indentation */
    }

    .explanation-section li {
        margin-bottom: 10px; /* More space between list items */
        line-height: 1.6;
    }

    .explanation-section .formula {
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace; /* Monospaced font for formulas */
        background-color: #f0f0f0; /* Light grey background */
        padding: 4px 8px; /* Padding around formula */
        border-radius: 4px;
        display: inline-block; /* Allow vertical alignment */
        direction: ltr; /* Formulas are LTR */
        text-align: left;
        margin: 0 4px; /* Small margin around inline formulas */
        color: #c82333; /* Reddish color for formulas */
    }
     .explanation-section .formula.block {
         display: block;
         text-align: center;
         padding: 15px;
         margin: 20px auto; /* Center block formulas */
         background-color: #e9e9e9;
         border-left: 5px solid #007bff; /* Accent border */
         max-width: 400px;
         font-size: 1.3em;
     }


     .explanation-toggle-button {
        display: block;
        margin: 20px auto; /* Center the button */
        padding: 12px 25px;
        background-color: #6c757d; /* Grey button */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease-in-out;
     }

     .explanation-toggle-button:hover {
        background-color: #5a6268;
     }

      .explanation-toggle-button:active {
        background-color: #4e555b;
     }

     /* Add Font Awesome for icons (requires linking the library in the HTML head) */
     /* <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"> */
     /* Assuming the platform supports adding external CSS or has FA available */
     /* If not, remove the <i> tags with class="fas" */

</style>

<script>
    const canvas = document.getElementById('pendulum-canvas');
    const ctx = canvas.getContext('2d');
    const lengthSlider = document.getElementById('length-slider');
    const massSlider = document.getElementById('mass-slider');
    const angleSlider = document.getElementById('angle-slider');
    const lengthValueSpan = document.getElementById('length-value');
    const massValueSpan = document.getElementById('mass-value');
    const angleValueSpan = document.getElementById('angle-value');
    const startButton = document.getElementById('start-button');
    const resetButton = document.getElementById('reset-button');
    const measuredPeriodSpan = document.getElementById('measured-period');
    const predictedPeriodSpan = document.getElementById('predicted-period'); // New element
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    // Pendulum parameters
    let length = parseFloat(lengthSlider.value); // meters
    let mass = parseFloat(massSlider.value);     // kg
    let initialAngleDegrees = parseFloat(angleSlider.value); // degrees
    let initialAngleRadians = initialAngleDegrees * Math.PI / 180;
    const gravity = 9.81;                       // m/s^2 (Earth's gravity)

    // Simulation state
    let angle = initialAngleRadians;            // current angle in radians
    let angularVelocity = 0;                    // current angular velocity
    let isRunning = false;
    let animationFrameId = null;
    let lastTime = 0;

    // Period measurement state
    let crossings = 0; // Count zero crossings (passing vertical)
    let startTime = 0; // Time of the first relevant crossing
    let periodSum = 0; // Sum of measured periods
    let measuredPeriods = 0; // Count of full periods measured
    const CROSSING_ANGLE_THRESHOLD = 0.01; // Angle near vertical (radians)
    const MEASUREMENT_MIN_SWINGS = 2; // Number of swings before starting measurement to avoid transients

    // Drawing parameters
    const originX = canvas.width / 2;
    const originY = 50; // Top of the canvas
    const bobRadius = 25; // Slightly larger bob
    const pixelsPerMeter = 100; // Scaling factor for drawing

    // Trace parameters
    const traceLength = 150; // Number of points in the trace
    const tracePoints = [];

    // --- Helper Functions ---

    // Calculate predicted period based on length and gravity (for small angles)
    function calculatePredictedPeriod(L, g) {
        // T = 2 * pi * sqrt(L / g)
        if (L > 0 && g > 0) {
            return 2 * Math.PI * Math.sqrt(L / g);
        }
        return NaN; // Not a Number if length or gravity is zero/negative
    }


    // Update parameter displays and predicted period
    function updateParameterDisplays() {
        lengthValueSpan.textContent = length.toFixed(1);
        massValueSpan.textContent = mass.toFixed(1);
        angleValueSpan.textContent = initialAngleDegrees.toFixed(0);

        // Update predicted period display
        const predicted = calculatePredictedPeriod(length, gravity);
        predictedPeriodSpan.textContent = isNaN(predicted) ? '--' : predicted.toFixed(2);
    }

    // Draw the pendulum and trace
    function drawPendulum() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Add a subtle background pattern or grid (optional visual flair)
        // ctx.fillStyle = '#eef7ff'; // Parent div color
        // ctx.fillRect(0, 0, canvas.width, canvas.height);
        // ... add grid lines if desired ...

        // Calculate bob position
        const bobX = originX + length * pixelsPerMeter * Math.sin(angle);
        const bobY = originY + length * pixelsPerMeter * Math.cos(angle);

        // Add current position to trace
        tracePoints.push({ x: bobX, y: bobY });
        if (tracePoints.length > traceLength) {
            tracePoints.shift(); // Remove the oldest point
        }

        // Draw trace (fading effect)
        for (let i = 0; i < tracePoints.length - 1; i++) {
            const point1 = tracePoints[i];
            const point2 = tracePoints[i + 1];
            const opacity = (i / tracePoints.length) * 0.7 + 0.1; // Fade from transparent to semi-opaque
            const lineWidth = (i / tracePoints.length) * 2 + 1; // Grow line width slightly

            ctx.beginPath();
            ctx.moveTo(point1.x, point1.y);
            ctx.lineTo(point2.x, point2.y);
            ctx.strokeStyle = `rgba(0, 123, 255, ${opacity})`; // Blueish trace color
            ctx.lineWidth = lineWidth;
            ctx.lineCap = 'round';
            ctx.stroke();
        }


        // Draw string
        ctx.beginPath();
        ctx.moveTo(originX, originY);
        ctx.lineTo(bobX, bobY);
        ctx.strokeStyle = '#555'; // Darker string
        ctx.lineWidth = 3; // Thicker string
        ctx.stroke();

         // Draw origin support (rendered via CSS div #origin-point)
         // The div is positioned absolute based on canvas parent

         // Draw equilibrium line (vertical line through origin)
         ctx.beginPath();
         ctx.moveTo(originX, originY);
         ctx.lineTo(originX, canvas.height);
         ctx.strokeStyle = 'rgba(0, 0, 0, 0.1)'; /* Light grey dashed line */
         ctx.lineWidth = 1;
         ctx.setLineDash([5, 5]); /* Make it dashed */
         ctx.stroke();
         ctx.setLineDash([]); /* Reset line dash */


        // Draw bob
        ctx.beginPath();
        ctx.arc(bobX, bobY, bobRadius, 0, Math.PI * 2);
        ctx.fillStyle = '#007bff'; // Blue color for bob
        ctx.fill();
        ctx.strokeStyle = '#0056b3'; // Darker blue border
        ctx.lineWidth = 2;
        ctx.stroke();

         // Add a subtle highlight/gradient to the bob
         const gradient = ctx.createRadialGradient(bobX - bobRadius/3, bobY - bobRadius/3, bobRadius/8, bobX, bobY, bobRadius);
         gradient.addColorStop(0, 'rgba(255, 255, 255, 0.5)');
         gradient.addColorStop(1, 'rgba(255, 255, 255, 0)');
         ctx.fillStyle = gradient;
         ctx.fill();
    }

    // Reset simulation
    function resetSimulation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        isRunning = false;
        animationFrameId = null;
        lastTime = 0; // Crucial for correct deltaTime on next start

        length = parseFloat(lengthSlider.value);
        mass = parseFloat(massSlider.value); // Mass doesn't affect formula, but reset it
        initialAngleDegrees = parseFloat(angleSlider.value);
        initialAngleRadians = initialAngleDegrees * Math.PI / 180;

        angle = initialAngleRadians;
        angularVelocity = 0;

        // Reset period measurement
        crossings = 0;
        startTime = 0;
        periodSum = 0;
        measuredPeriods = 0;
        measuredPeriodSpan.textContent = '--';

        // Reset trace
        tracePoints.length = 0;

        drawPendulum(); // Draw initial state
        updateParameterDisplays(); // Update displays and predicted period
        startButton.innerHTML = '<i class="fas fa-play"></i> הפעל/השהה'; // Reset button text and icon
        startButton.style.backgroundColor = '#28a745'; // Reset button color
    }

    // Simulation update loop
    function update(currentTime) {
        // Ensure lastTime is set on the first frame
        if (lastTime === 0) {
            lastTime = currentTime;
        }

        const deltaTime = (currentTime - lastTime) / 1000; // delta time in seconds
        lastTime = currentTime;

        if (isRunning) {
            // Calculate angular acceleration using the small angle approximation formula derived from Newton's second law for rotation
            // For large angles, Math.sin(angle) is used, which is the actual physics
            angularAcceleration = (-gravity / length) * Math.sin(angle); // Use actual sin for larger angles

            // Update angular velocity and angle using Euler integration
            angularVelocity += angularAcceleration * deltaTime;
            angle += angularVelocity * deltaTime;

            // Period measurement logic (detecting crossings of angle=0)
            // We count how many times the pendulum crosses the vertical line.
            // A full period is completed when it crosses twice in the SAME direction (e.g., from left to right, then again from left to right).
            // Or equivalently, crosses four times regardless of direction (left-right, right-left, left-right, right-left).
            // We will use the four-crossing method for simplicity, starting timing after the first swing completes.

            const angleThreshold = CROSSING_ANGLE_THRESHOLD;
            const currentAngle = angle;
            const prevAngle = angle - angularVelocity * deltaTime; // Approximate previous angle

            // Check if crossing the vertical (angle changes sign or crosses threshold)
            if ((prevAngle > angleThreshold && currentAngle <= angleThreshold) ||
                (prevAngle < -angleThreshold && currentAngle >= -angleThreshold) ||
                (prevAngle <= angleThreshold && currentAngle > angleThreshold) ||
                 (prevAngle >= -angleThreshold && currentAngle < -angleThreshold)
                )
            {
                // Ensure it's a "significant" crossing near zero, not just small oscillations
                 if (Math.abs(currentAngle) < angleThreshold * 3 ) { // Check if it's close to center
                     crossings++;

                     // Start timing after the pendulum has swung away from the initial large angle and returned to cross the center the first time.
                     // This avoids measuring the initial partial swing or transient effects.
                     // Let's trigger measurement starting from the 2nd crossing (completing the first half-swing from initial release)
                     // and measure periods between every 2 subsequent crossings.
                     if (crossings >= MEASUREMENT_MIN_SWINGS && crossings % 2 === 0) { // Every second crossing AFTER the initial swings
                        if (startTime > 0) {
                             const currentPeriod = (currentTime - startTime) / 1000; // Period in seconds
                             periodSum += currentPeriod;
                             measuredPeriods++;
                             measuredPeriodSpan.textContent = (periodSum / measuredPeriods).toFixed(2);
                             // Optional: Add a visual cue for period measurement (e.g., briefly change text color)
                              measuredPeriodSpan.style.color = '#28a745'; // Green
                              setTimeout(() => { measuredPeriodSpan.style.color = '#007bff'; }, 300); // Revert color
                        }
                        startTime = currentTime; // Reset start time for the next period
                     } else if (crossings >= MEASUREMENT_MIN_SWINGS && startTime === 0) {
                         // If we are past the initial swings and haven't started timing yet, set the start time
                         startTime = currentTime;
                     }
                 }
            }
        }

        drawPendulum();
        animationFrameId = requestAnimationFrame(update);
    }

    // Event listeners for controls
    lengthSlider.addEventListener('input', (event) => {
        length = parseFloat(event.target.value);
        // Note: Mass doesn't affect period formula, but we update display and reset
        resetSimulation(); // Reset simulation on parameter change
    });

    massSlider.addEventListener('input', (event) => {
        mass = parseFloat(event.target.value);
         // Mass doesn't change the period formula, but it might slightly affect *measured* period due to simulation imperfections
        updateParameterDisplays(); // Just update display, don't reset physics state
        // If simulation is running, changing mass *will* affect the simulation slightly
        // in a more complex model (air resistance, non-point mass).
        // In our simple model, mass doesn't affect the motion physics, only the display value.
        // We reset only on Length/Angle changes as they are the core parameters.
    });

    angleSlider.addEventListener('input', (event) => {
        initialAngleDegrees = parseFloat(event.target.value);
        initialAngleRadians = initialAngleDegrees * Math.PI / 180;
         // Reset simulation on parameter change
        resetSimulation();
    });

    // Button event listeners
    startButton.addEventListener('click', () => {
        isRunning = !isRunning;
        if (isRunning) {
            startButton.innerHTML = '<i class="fas fa-pause"></i> השהה'; // Pause icon
            startButton.style.backgroundColor = '#ffc107'; // Yellow color for pause
            if (!animationFrameId) { // Start animation if not running
                 lastTime = 0; // Reset lastTime for smooth start
                 crossings = 0; // Reset period measurement on start
                 startTime = 0;
                 periodSum = 0;
                 measuredPeriods = 0;
                 measuredPeriodSpan.textContent = '--';
                 animationFrameId = requestAnimationFrame(update);
            }
        } else {
            startButton.innerHTML = '<i class="fas fa-play"></i> הפעל'; // Play icon
             startButton.style.backgroundColor = '#28a745'; // Green color for play
        }
    });

    resetButton.addEventListener('click', resetSimulation);

    // Explanation toggle
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג/הסתר הסבר מפורט';
        toggleExplanationButton.style.backgroundColor = isHidden ? '#dc3545' : '#6c757d'; /* Red when expanded, grey when collapsed */
    });

    // Initial setup
    resetSimulation(); // Draw initial state and set initial values
    // Start the animation loop immediately, but the simulation is paused initially (isRunning = false)
    // This allows the initial state to be drawn and updated via sliders before pressing Play
    if (!animationFrameId) {
         lastTime = 0; // Ensure correct delta time on first frame
         animationFrameId = requestAnimationFrame(update);
    }


</script>
```