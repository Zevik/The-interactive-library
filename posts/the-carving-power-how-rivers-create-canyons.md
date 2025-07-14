---
title: "סוד הכוח החורט: כך נהרות אדירים מפַּסלים קניוני ענק"
english_slug: the-carving-power-how-rivers-create-canyons
category: "גיאולוגיה"
tags: [גיאולוגיה, נהרות, קניונים, ארוזיה, גיאומורפולוגיה, תהליכי נוף]
---
<h1>סוד הכוח החורט: כך נהרות אדירים מפַּסלים קניוני ענק</h1>

<p>הקניון הגדול הוא פלא טבעי שמותיר אותנו פעורי פה, ובקרקעיתו זורם לעתים קרובות נהר צנוע למראה. האם ייתכן שהזרם הרגיל לכאורה הזה באמת מסוגל לחצוב עמק עמוק ורחב כל כך? התכוננו לגלות את הכוח העצום החבוי בנהר, וכיצד הוא מעצב את פני כדור הארץ לאורך מיליוני שנים של עבודה בלתי פוסקת.</p>

<div class="simulation-container">
    <canvas id="canyonCanvas" width="800" height="500"></canvas>
    <div class="controls">
        <h3>שליטה בכוח הנהר והזמן</h3>
        <div class="control-group">
            <label for="flowIntensity">עוצמת זרימת מים:</label>
            <input type="range" id="flowIntensity" min="1" max="10" value="5">
            <span id="flowValue" class="value-display">5</span>
            <p class="control-hint">כוח המים והסחף שהם נושאים.</p>
        </div>

        <div class="control-group">
            <label for="simDuration">משך זמן סימולציה (אלפי שנים):</label>
            <input type="range" id="simDuration" min="10" max="2000" value="200" step="10">
            <span id="durationValue" class="value-display">200</span>
             <p class="control-hint">הזמן שבו הנהר עובד (1000 = מיליון שנה).</p>
        </div>

        <div class="button-group">
            <button id="startSimulation"><i class="fas fa-play"></i> התחל לחצוב!</button>
            <button id="resetSimulation"><i class="fas fa-sync-alt"></i> אפס נוף</button>
        </div>
        <p id="simTimeDisplay">זמן סימולציה: 0 אלפי שנים</p>
         <div id="erosionVisualizer"></div> <!-- Element to visualize erosion particles -->
    </div>
</div>

<button id="toggleExplanation" class="toggle-button"><i class="fas fa-book-open"></i> גלו את הסוד: מה באמת קורה כאן?</button>

<div id="explanation" class="hidden">
    <h2>פענוח הסוד: הכוח החורט של הנהרות</h2>

    <h3>אדריכלי העמקים: מי הם הקניונים?</h3>
    <p>דמיינו עמק עמוק-עמוק, עם קירות כמעט אנכיים שצונחים מטה. זהו קניון! הוא שונה מעמק רגיל בכך שהנהר שחצב אותו התמקד בעיקר בלחתור *לעומק* (חתירה לעומק - Downcutting) הרבה יותר מאשר להרחיב את העמק לצדדים. התוצאה: צורה דמויית האות 'V' עמוקה ותלולה במיוחד.</p>

    <h3>הנהר כפסָל: אנרגיה בתנועה</h3>
    <p>למרות מראהו השליו לעתים, נהר הוא כוח דינמי אדיר. כשהמים זורמים, במיוחד בירידות תלולות, הם צוברים אנרגיה עצומה. האנרגיה הזו מאפשרת להם לא רק לנתק חומרים מקרקעית הערוץ ודפנותיו, אלא גם לשאת אותם למרחקים.</p>

    <h3>איך הנהר חורט? שיטות העבודה של המים</h3>
    <p>הנהר משתמש במספר "כלי עבודה" כדי לפַסל את הנוף:</p>
    <ul>
        <li><strong>ליטוש במים (Abrasion):</strong> זהו כלי העבודה העיקרי ליצירת קניונים. דמיינו מיליוני גרגירי חול, אבנים קטנות וחלוקי נחל שהנהר סוחף. כשהם נישאים בזרם המהיר, הם מתנגשים שוב ושוב בקרקעית ובדפנות הערוץ, ושוחקים אותם באיטיות אך בעקביות, כמו נייר זכוכית ענק.</li>
        <li><strong>המסה כימית (Solution):</strong> המים עצמם, במיוחד כשהם חומציים מעט, יכולים להמיס מינרלים מסוימים בסלעים, במיוחד בסלעים כמו גיר ודולומיט. זהו תהליך איטי אך משמעותי לאורך זמן.</li>
        <li><strong>כוח המים הגולמי (Hydraulic Action):</strong> כשהמים נדחפים לתוך סדקים וחריצים בסלע, הם יוצרים לחץ שיכול לשבור פיסות סלע ולנתק אותן. גם אוויר הנלכד בסדקים יכול להשתחרר בפתאומיות ולגרום לשבירה.</li>
        <li><strong>התנגשות ורִסוק (Attrition):</strong> החלקיקים שהנהר נושא מתנגשים לא רק בסלע, אלא גם זה בזה. התנגשויות אלה שוברות אותם לחלקיקים קטנים יותר ויותר, מה שהופך אותם ליעילים יותר בתהליך הליטוש (Abrasion) ומגדיל את כמות החומר הדק שהנהר יכול לשאת.</li>
    </ul>

    <h3>התמחות ב"חתירה לעומק" - כך נולדים קניונים</h3>
    <p>הסיבה העיקרית לצורתו התלולה של הקניון היא שהנהר מתמקד בעיקר בלשחוק את קרקעיתו ולהעמיק את ערוצו (חתירה לעומק). תהליך זה דומיננטי במיוחד כשהנהר זורם במדרון תלול, או כאשר הקרקע באזור מתרוממת (התרוממות טקטונית) במהירות יחסית לקצב הסחיפה. הנהר למעשה "מנסר" את הנוף המתרומם, ושומר על נתיבו היורד. מכיוון שהסחיפה לצדדים איטית יותר משמעותית מהחתירה לעומק במצבים כאלה, דפנות העמק נשארות תלולות וגבוהות.</p>

    <h3>מה משפיע על עומק וצורת הקניון?</h3>
    <p>הנה כמה מהגורמים המכריעים:</p>
    <ul>
        <li><strong>כוח הנהר (כמו שראיתם בסימולציה!):</strong> נהר עם זרימה חזקה ושיטפונות תכופים נושא יותר סחף ויש לו אנרגיה רבה יותר לשחוק ולחצוב.</li>
        <li><strong>סוגי הסלע:</strong> שכבות סלע שונות נשחקות בקצב שונה. סלע קשה מאוד יישחק לאט יותר ויכול ליצור צוקים תלולים, בעוד סלע רך יישחק מהר יותר וייצור מדרונות מתונים יותר. שילוב שכבות שונות יוצר לעתים קניונים מדורגים.</li>
        <li><strong>קצב התרוממות הקרקע:</strong> כפי שהוזכר, אם ההתרוממות הטקטונית מהירה, הנהר חייב לחצוב עמוק יותר כדי לשמור על נתיבו, מה שמאיץ את היווצרות הקניון.</li>
        <li><strong>האקלים:</strong> באקלים יבש, הצמחייה מועטה, מה שמאפשר לבלאי (כמו נפילת סלעים) להרחיב מעט את הקניון. באקלים לח, הצמחייה יכולה לייצב את הדפנות ולשמור על תלילותן.</li>
        <li><strong>מפלס הים/אגם:</strong> מפלס גופי המים שאליהם הנהר נשפך משפיע על האנרגיה שלו במעלה הזרם ועל יכולתו לחצוב לעומק. ירידת מפלס הבסיס מגבירה את יכולת החתירה.</li>
    </ul>

    <h3>קניונים מפורסמים מסביב לעולם (וגם קצת מישראל)</h3>
    <ul>
        <li><strong>הקניון הגדול (אריזונה, ארה"ב):</strong> הדוגמה אולי המפורסמת ביותר, שנחצב על ידי נהר הקולורדו העוצמתי באזור שעבר התרוממות משמעותית. הוא מציג לראווה שכבות סלע עתיקות שנחשפו בתהליך החציבה.</li>
        <li><strong>קניון נחל ערוגות ונחל פרת (יהודה, ישראל):</strong> קניונים מרשימים במדבר יהודה, שנחצבו על ידי נחלים איתנים (זרימה קבועה) במצוק ההעתקים. הם מדגימים כיצד גם באזור צחיח למראה, מים יכולים לפַסל נופים דרמטיים בסלע גיר ודולומיט.</li>
        <li><strong>קניון קוֹפְּרוּלוּ (טור קופרולו, טורקיה):</strong> קניון יפהפה ופופולרי לרפטינג, המדגים גם הוא את כוחו של נהר לחצוב במסלע.</li>
    </ul>

    <h3>לא רק קניונים: יצירות נוף נוספות של הנהר</h3>
    <p>הנהר אינו מוגבל רק ליצירת קניונים. הוא אחראי למגוון עצום של צורות נוף אחרות:</p>
    <ul>
        <li><strong>מפלים ואשדות:</strong> כשהנהר נתקל בסלע קשה או במדרגה גיאולוגית.</li>
        <li><strong>עמקים רחבים:</strong> בשלבים מאוחרים יותר, כשהסחיפה הצדדית מתגברת על החתירה לעומק, העמק מתרחב לצורת 'U' או 'V' רחבה יותר.</li>
        <li><strong>מישורי הצפה:</strong> אזורים שטוחים לצד הנהר המוצפים בשיטפונות ושם שוקעים משקעי הנהר העדינים, מה שהופך אותם לפוריים.</li>
        <li><strong>דלתאות:</strong> צורות משולשות של יבשה הנוצרות בשפך נהר לים או אגם, כשהזרם מאט והסחף שוקע.</li>
    </ul>
     <p>כפי שראיתם בסימולציה, כוחו של הנהר, בשילוב עם משך הזמן העצום, הוא זה שמאפשר את יצירתם של קניונים מרהיבים כמו אלה שראינו. בפעם הבאה שתראו נהר, זכרו את העוצמה הנסתרת שלו!</p>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif; /* More common sans-serif */
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: #f4f7f6; /* Light background */
        color: #333;
    }

    h1, h2, h3 {
        color: #2c3e50; /* Dark blue-gray */
        text-align: center;
        margin-bottom: 15px;
    }

     h1 {
         font-size: 2.2em;
         margin-top: 0;
     }

     h2 {
         font-size: 1.8em;
         border-bottom: 2px solid #3498db; /* Blue underline */
         padding-bottom: 5px;
         margin-bottom: 20px;
     }

     h3 {
         font-size: 1.4em;
         color: #3498db; /* Blue */
         margin-bottom: 10px;
     }


    p {
        margin-bottom: 15px;
    }

    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 30px auto; /* More space */
        padding: 20px;
        border: 1px solid #bdc3c7; /* Light gray border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ecf0f1; /* Very light gray */
        max-width: 800px; /* Wider container for canvas */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    canvas {
        border: 2px solid #34495e; /* Darker border */
        background: linear-gradient(to bottom, #aeeeff, #e0f0ff); /* Sky gradient */
        display: block;
        margin-bottom: 20px; /* More space */
        border-radius: 8px; /* Match container */
    }

    .controls {
        text-align: center;
        margin-top: 15px;
        width: 100%; /* Full width */
    }

    .control-group {
        margin-bottom: 15px; /* Space between controls */
        display: flex;
        align-items: center;
        justify-content: center; /* Center controls */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .controls label {
        display: inline-block;
        width: 180px; /* Wider label for RTL */
        text-align: left; /* Align text to the left */
        margin-bottom: 0; /* Reset margin */
        font-weight: bold;
        color: #555;
        padding-left: 10px; /* Space from input */
    }

    .controls input[type="range"] {
        flex-grow: 1; /* Take available space */
        max-width: 250px; /* Limit max width */
        margin: 0 10px; /* Space around slider */
        vertical-align: middle;
         -webkit-appearance: none; /* Override default CSS styles */
         appearance: none;
         background: #bdc3c7; /* Light gray track */
         outline: none;
         height: 8px;
         border-radius: 4px;
    }

     .controls input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: #3498db; /* Blue thumb */
         cursor: pointer;
         border-radius: 50%; /* Circular thumb */
         border: 2px solid #2980b9; /* Darker blue border */
         transition: background .15s ease-in-out;
     }

     .controls input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #3498db;
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #2980b9;
         transition: background .15s ease-in-out;
     }

     .controls input[type="range"]::-webkit-slider-thumb:hover {
          background: #2980b9;
     }
      .controls input[type="range"]::-moz-range-thumb:hover {
          background: #2980b9;
     }


    .value-display {
        display: inline-block;
        width: 40px;
        text-align: left; /* Value should be LTR */
        font-weight: bold;
        color: #555;
    }

    .control-hint {
         font-size: 0.9em;
         color: #777;
         margin-top: 5px;
         flex-basis: 100%; /* Take full width */
         text-align: center;
    }

    .button-group {
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .controls button {
        margin: 0 8px; /* Space between buttons */
        padding: 12px 25px; /* Larger padding */
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        transition: background-color 0.2s ease, transform 0.1s ease; /* Smooth transitions */
        font-weight: bold;
        display: inline-flex; /* Align icon and text */
        align-items: center;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .controls button i {
        margin-left: 8px; /* Space between icon and text */
    }


    #startSimulation {
        background-color: #2ecc71; /* Green */
        color: white;
    }

    #startSimulation:hover {
        background-color: #27ae60; /* Darker green */
        transform: translateY(-2px); /* Slight lift effect */
    }
     #startSimulation:disabled {
        background-color: #a3d9b8; /* Lighter green */
        cursor: not-allowed;
         transform: none;
         box-shadow: none;
     }


     #resetSimulation {
        background-color: #e74c3c; /* Red */
        color: white;
     }

     #resetSimulation:hover {
         background-color: #c0392b; /* Darker red */
         transform: translateY(-2px);
     }


    #simTimeDisplay {
        margin-top: 15px;
        font-weight: bold;
        color: #34495e; /* Dark blue-gray */
        font-size: 1.1em;
    }

    .toggle-button {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #3498db; /* Blue */
        color: white;
        font-weight: bold;
         transition: background-color 0.2s ease, transform 0.1s ease;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
         display: flex;
        align-items: center;
    }
     .toggle-button i {
        margin-left: 8px;
     }


    .toggle-button:hover {
        background-color: #2980b9; /* Darker blue */
         transform: translateY(-2px);
    }

    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #bdc3c7;
        border-radius: 12px;
        background-color: #ecf0f1;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .hidden {
        display: none;
    }

    #explanation ul {
        list-style: none;
        padding-right: 0; /* Remove default padding */
        margin-top: 10px;
    }

    #explanation li {
         margin-bottom: 8px;
         padding-right: 25px; /* Space for custom bullet */
         position: relative; /* For positioning the bullet */
    }

    #explanation li:before {
        content: "\f061"; /* Font Awesome icon for arrow-right */
        font-family: "Font Awesome 5 Free";
        font-weight: 900; /* Solid icons */
        color: #3498db;
        font-size: 0.9em;
        position: absolute;
        right: 0; /* Position on the right for RTL */
        top: 3px; /* Adjust vertical alignment */
    }

    /* Optional: Add Font Awesome for icons */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

</style>

<script>
    const canvas = document.getElementById('canyonCanvas');
    const ctx = canvas.getContext('2d');
    const flowIntensityInput = document.getElementById('flowIntensity');
    const flowValueSpan = document.getElementById('flowValue');
    const simDurationInput = document.getElementById('simDuration');
    const durationValueSpan = document.getElementById('durationValue');
    const startButton = document.getElementById('startSimulation');
    const resetButton = document.getElementById('resetSimulation');
    const simTimeDisplay = document.getElementById('simTimeDisplay');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
     const erosionVisualizer = document.getElementById('erosionVisualizer'); // Element for particles (if using DOM) - keeping canvas particles for simplicity

    const CANVAS_WIDTH = canvas.width;
    const CANVAS_HEIGHT = canvas.height;
    const INITIAL_GROUND_LEVEL = CANVAS_HEIGHT * 0.6; // Starting height of the ground surface

    // Simulation state
    let groundProfile; // Array of y-coordinates for the ground profile
    let rockLayers; // Define rock layers with different erosion resistance
    let isSimulating = false;
    let currentSimTime = 0; // In thousands of years
    let animationFrameId = null; // To store the requestAnimationFrame ID
    let startTime = null; // To track animation start time
    const animationDurationMs = 8000; // Total animation duration in milliseconds (e.g., 8 seconds)

     // Erosion particle system (simple on canvas)
     let erosionParticles = [];
     const MAX_PARTICLES = 100; // Limit the number of particles

    // Define rock layers: [start_y, end_y, erosion_resistance_factor, color]
    // Lower factor means more resistant
    rockLayers = [
        { startY: 0, endY: CANVAS_HEIGHT * 0.25, resistance: 0.8, color: '#cd853f', name: 'שכבת קרקע עליונה (חול/אדמה)' }, // Softer top layer (e.g., sandstone, soil)
        { startY: CANVAS_HEIGHT * 0.25, endY: CANVAS_HEIGHT * 0.45, resistance: 0.6, color: '#d2b48c', name: 'אבן חול עדינה' }, // Slightly harder
        { startY: CANVAS_HEIGHT * 0.45, endY: CANVAS_HEIGHT * 0.65, resistance: 0.4, color: '#a0522d', name: 'שכבת סלע בינונית (גיר/דולומיט)' }, // Harder middle layer
        { startY: CANVAS_HEIGHT * 0.65, endY: CANVAS_HEIGHT * 0.85, resistance: 0.2, color: '#8b4513', name: 'שכבת סלע קשה (בזלת/גרניט)' }, // Very hard layer
        { startY: CANVAS_HEIGHT * 0.85, endY: CANVAS_HEIGHT, resistance: 0.5, color: '#708090', name: 'שכבת סלע תחתית (פצלים/אבן חול)' } // Moderate resistance layer
    ];

    function resetSimulation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        groundProfile = new Array(CANVAS_WIDTH);
        // Start with a relatively flat surface with some gentle variation
        const initialHeight = INITIAL_GROUND_LEVEL;
        for (let i = 0; i < CANVAS_WIDTH; i++) {
             // Gentle sine wave variation
             groundProfile[i] = initialHeight + Math.sin(i / 40) * 15 - 7;
             // Ensure limits
             if (groundProfile[i] > CANVAS_HEIGHT - 30) groundProfile[i] = CANVAS_HEIGHT - 30;
             if (groundProfile[i] < 30) groundProfile[i] = 30;
        }

        // Create a slight, wider initial dip in the middle for the river to start naturally
        const middle = Math.floor(CANVAS_WIDTH / 2);
        const initialRiverWidth = 40;
        for(let i = -Math.floor(initialRiverWidth/2); i <= Math.floor(initialRiverWidth/2); i++){
            const index = middle + i;
            if(index >= 0 && index < CANVAS_WIDTH){
                // Create a parabolic dip towards the center
                 const dist = Math.abs(i);
                 const dipAmount = (initialRiverWidth/2 - dist) * 0.5; // Max dip at center
                 groundProfile[index] -= dipAmount;
                 // Ensure the dip doesn't go below a reasonable level initially
                 if(groundProfile[index] < initialHeight - 15) groundProfile[index] = initialHeight - 15;
            }
        }


        isSimulating = false;
        currentSimTime = 0;
        simTimeDisplay.textContent = `זמן סימולציה: 0 אלפי שנים`;
        startButton.disabled = false;
         erosionParticles = []; // Clear particles
        drawCanvas(); // Draw initial state
    }

    function drawCanvas() {
        ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

        // Draw Sky (gradient handled by CSS background)
        // Draw Ground and Rock Layers using polygon fill
        ctx.beginPath();
        ctx.moveTo(0, CANVAS_HEIGHT); // Start at bottom left
        ctx.lineTo(0, groundProfile[0]); // Draw up to the ground profile start

        // Draw the top ground profile line
        for (let i = 0; i < CANVAS_WIDTH; i++) {
            ctx.lineTo(i, groundProfile[i]);
        }

        ctx.lineTo(CANVAS_WIDTH, groundProfile[CANVAS_WIDTH - 1]); // Draw to the end of the profile
        ctx.lineTo(CANVAS_WIDTH, CANVAS_HEIGHT); // Draw down to bottom right
        ctx.closePath(); // Complete the shape

        // Fill the entire ground area based on rock layers
        const groundAreaPoly = new Path2D(ctx.currentPath); // Capture the path

        for (let j = 0; j < rockLayers.length; j++) {
            const layer = rockLayers[j];
            ctx.fillStyle = layer.color;

            // Clip to the current layer's vertical bounds
            ctx.save();
            ctx.beginPath();
            ctx.rect(0, layer.startY, CANVAS_WIDTH, layer.endY - layer.startY);
            ctx.clip();

            // Fill the captured ground area path
            ctx.fill(groundAreaPoly);
            ctx.restore(); // Remove clipping path
        }


        // Draw the river dynamically on top of the deepest part of the channel
        // Find the deepest point to determine river Y level
         let riverY = CANVAS_HEIGHT;
         const riverCenterApprox = Math.floor(CANVAS_WIDTH / 2);
         const searchWidth = 50; // Search area around the center for the deepest point
         let minRiverY = CANVAS_HEIGHT;
         let riverXStart = Math.max(0, riverCenterApprox - Math.floor(searchWidth/2));
         let riverXEnd = Math.min(CANVAS_WIDTH-1, riverCenterApprox + Math.floor(searchWidth/2));

         for(let x = riverXStart; x <= riverXEnd; x++){
              if(groundProfile[x] < minRiverY){
                   minRiverY = groundProfile[x];
              }
         }
         riverY = minRiverY; // River flows at the lowest current level

        // Draw the river as a gradient line/shape
        const riverVisualWidth = 15; // Visual width of the river effect
        const riverGradient = ctx.createLinearGradient(0, riverY, 0, riverY + riverVisualWidth * 2);
        riverGradient.addColorStop(0, 'rgba(68, 136, 187, 0.8)'); // Lighter blue, slightly transparent
        riverGradient.addColorStop(0.5, 'rgba(41, 105, 149, 0.9)'); // Deeper blue
        riverGradient.addColorStop(1, 'rgba(26, 66, 94, 0.95)'); // Darkest blue

        ctx.fillStyle = riverGradient;

        // Draw a shape for the river - a simple rectangle based on the lowest point
        // This is a simplification; ideally, the river shape follows the low points of the channel
        const riverDrawWidth = 20; // How wide to draw the river area
        const riverDrawHeight = 8; // Visual depth of the water
        ctx.fillRect(riverCenterApprox - riverDrawWidth/2, riverY - riverDrawHeight + 2, riverDrawWidth, riverDrawHeight);


         // Draw erosion particles
         ctx.fillStyle = '#a0522d'; // Earthy color for particles
         erosionParticles.forEach(p => {
             ctx.fillRect(p.x, p.y, p.size, p.size); // Draw as small squares
         });


    }

    function getErosionResistance(y) {
        for (let i = 0; i < rockLayers.length; i++) {
            const layer = rockLayers[i];
            // Check if the point is within the vertical range of the layer
            if (y >= layer.startY && y < layer.endY) {
                return layer.resistance;
            }
        }
         // Fallback: if y is somehow outside defined layers, treat as highly resistant
        return 10;
    }


    function updateSimulation(deltaTimeSim) { // deltaTimeSim is in thousands of years
        const flow = parseFloat(flowIntensityInput.value);
        // Base erosion rate depends on flow and time step. Higher flow = more erosion.
        // Scale flow (1-10) to a factor (e.g., 0.5 to 5)
        const flowFactor = 0.5 + (flow - 1) * (4.5 / 9); // Map [1, 10] to [0.5, 5]

        // The total erosion work done in this step is proportional to flowFactor * deltaTimeSim
        const totalErosionPotential = flowFactor * deltaTimeSim * 50; // Arbitrary scaling factor

        const riverCenter = Math.floor(CANVAS_WIDTH / 2);
        const downcuttingWidth = 25; // Wider area directly affected by downcutting
        const lateralErosionWidth = 60; // Wider area affected by lateral erosion (banks)
        const lateralErosionFactor = 0.05; // Lateral erosion is much weaker than downcutting


        // Downcutting (deepening) is concentrated under the main river path
        for (let i = -Math.floor(downcuttingWidth/2); i <= Math.floor(downcuttingWidth/2); i++) {
            const x = riverCenter + i;
            if (x >= 0 && x < CANVAS_WIDTH) {
                const currentY = groundProfile[x];
                const resistance = getErosionResistance(currentY);
                // Erosion amount: higher potential, lower resistance -> more erosion
                 // Erosion is concentrated near the very center, fading towards edges of downcutting width
                 const distanceToCenter = Math.abs(i);
                 const centerConcentrationFactor = Math.max(0, 1 - distanceToCenter / (downcuttingWidth/2)); // 1 at center, 0 at edges

                const erosionAmount = (totalErosionPotential / downcuttingWidth) * centerConcentrationFactor / resistance;

                // Apply erosion (increase Y value as Y=0 is top)
                groundProfile[x] += erosionAmount;

                // Cap erosion at canvas bottom
                 if (groundProfile[x] > CANVAS_HEIGHT) {
                     groundProfile[x] = CANVAS_HEIGHT;
                 }

                 // Add particles for visualization
                 const numParticles = Math.min(Math.floor(erosionAmount * 0.5), 5); // More erosion = more particles (up to a limit per step)
                 if (erosionParticles.length < MAX_PARTICLES) {
                     for(let k = 0; k < numParticles; k++) {
                          erosionParticles.push({
                               x: x + (Math.random() - 0.5) * 5, // Randomize position slightly around x
                               y: currentY + Math.random() * erosionAmount, // Start falling from eroded area
                               size: Math.random() * 2 + 1,
                               vy: Math.random() * 0.5 + 0.2, // Vertical velocity
                               vx: (Math.random() - 0.5) * 0.5, // Horizontal velocity
                               alpha: 1 // Opacity
                          });
                     }
                 }
            }
        }

         // Lateral Erosion (widening)
         // Find the deepest point of the river bed dynamically
         let riverbedY = CANVAS_HEIGHT;
         const riverChannelSearchWidth = 50; // Search area around center
         const riverXSearchStart = Math.max(0, riverCenter - Math.floor(riverChannelSearchWidth/2));
         const riverXSearchEnd = Math.min(CANVAS_WIDTH-1, riverCenter + Math.floor(riverChannelSearchWidth/2));
          for(let x = riverXSearchStart; x <= riverXSearchEnd; x++){
               if(groundProfile[x] < riverbedY){
                    riverbedY = groundProfile[x];
               }
          }

         for (let i = -Math.floor(lateralErosionWidth/2); i <= Math.floor(lateralErosionWidth/2); i++) {
             const x = riverCenter + i;
             if (x >= 0 && x < CANVAS_WIDTH) {
                  const currentY = groundProfile[x];
                  // Only erode banks if they are significantly above the current riverbed level
                 if (currentY < riverbedY - 5) { // Arbitrary threshold to consider it a 'bank'
                      const resistance = getErosionResistance(currentY);
                       const distanceToCenter = Math.abs(i);
                      // Erosion decreases with distance from the river center, peaking near the edges of the main channel
                       // Use a factor that peaks around the edges of the downcutting area
                      const distanceFactor = Math.exp(-Math.pow((distanceToCenter - downcuttingWidth/2) / (lateralErosionWidth/3), 2));


                      const erosionAmount = (totalErosionPotential * lateralErosionFactor / lateralErosionWidth) * distanceFactor / resistance;

                      groundProfile[x] += erosionAmount;

                      if (groundProfile[x] > CANVAS_HEIGHT) {
                          groundProfile[x] = CANVAS_HEIGHT;
                      }
                 }
             }
         }

         // Update and clean up particles
         for(let i = erosionParticles.length - 1; i >= 0; i--) {
              const p = erosionParticles[i];
              p.x += p.vx;
              p.y += p.vy;
              p.alpha -= 0.01; // Fade out

              // Remove particles that are off-screen or faded
              if (p.y > CANVAS_HEIGHT || p.x < 0 || p.x > CANVAS_WIDTH || p.alpha <= 0) {
                   erosionParticles.splice(i, 1);
              }
         }


         // Simple smoothing of the ground profile
         const smoothingFactor = 0.1; // How much to smooth (0-1)
         const smoothedProfile = [...groundProfile]; // Copy current profile
         for(let i = 1; i < CANVAS_WIDTH - 1; i++) {
             // Average with neighbors
             const avgY = (groundProfile[i-1] + groundProfile[i+1]) / 2;
             // Apply smoothing
             smoothedProfile[i] = groundProfile[i] * (1 - smoothingFactor) + avgY * smoothingFactor;
         }
         groundProfile = smoothedProfile; // Use the smoothed profile


    }

    function simulateAnimation(currentTime) {
        if (!isSimulating) return;

        if (startTime === null) {
             startTime = currentTime;
        }

        const elapsedAnimationTime = currentTime - startTime;
        const totalDurationSim = parseFloat(simDurationInput.value); // Total simulation time in thousands of years

        // Calculate what simulation time corresponds to the current elapsed animation time
        const targetSimTime = (elapsedAnimationTime / animationDurationMs) * totalDurationSim;

        // Calculate the simulation time delta for *this frame*
        const simTimeDelta = targetSimTime - currentSimTime;

        // Prevent simulating negative or excessive time steps if frame rate is erratic
        if (simTimeDelta <= 0) {
             animationFrameId = requestAnimationFrame(simulateAnimation);
             return;
        }
        // Cap delta if it somehow exceeds the total remaining time (shouldn't happen with this logic but good practice)
        const remainingSimTime = totalDurationSim - currentSimTime;
        const actualSimTimeDelta = Math.min(simTimeDelta, remainingSimTime);


        currentSimTime += actualSimTimeDelta; // Update current sim time

        // Update display
        simTimeDisplay.textContent = `זמן סימולציה: ${Math.round(currentSimTime)} אלפי שנים`;

        // Update simulation state based on the calculated time delta
        updateSimulation(actualSimTimeDelta);
        drawCanvas();

        // Continue animation if not finished
        if (currentSimTime < totalDurationSim) {
             animationFrameId = requestAnimationFrame(simulateAnimation);
        } else {
            // Simulation finished
            currentSimTime = totalDurationSim; // Ensure display shows the exact end time
            simTimeDisplay.textContent = `זמן סימולציה: ${Math.round(currentSimTime)} אלפי שנים (הסתיימה)`;
            drawCanvas(); // Final draw
            isSimulating = false;
            startButton.disabled = false;
            animationFrameId = null;
             startTime = null; // Reset start time for next run
        }
    }


    startButton.addEventListener('click', () => {
        if (!isSimulating) {
             // Reset time and particles before starting a new simulation run
             currentSimTime = 0;
             erosionParticles = [];
             simTimeDisplay.textContent = `זמן סימולציה: 0 אלפי שנים`;
             startTime = null; // Ensure animation starts fresh

            isSimulating = true;
            startButton.disabled = true;
            simulateAnimation(performance.now()); // Pass initial time
        }
    });

    resetButton.addEventListener('click', () => {
        resetSimulation();
    });

    flowIntensityInput.addEventListener('input', () => {
        flowValueSpan.textContent = flowIntensityInput.value;
    });

    simDurationInput.addEventListener('input', () => {
        durationValueSpan.textContent = simDurationInput.value;
    });

    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
         // Change button text based on state
         if (explanationDiv.classList.contains('hidden')) {
              toggleExplanationButton.innerHTML = '<i class="fas fa-book-open"></i> גלו את הסוד: מה באמת קורה כאן?';
         } else {
               toggleExplanationButton.innerHTML = '<i class="fas fa-book"></i> הסתר הסבר';
         }
    });


    // Initial setup
    resetSimulation(); // Draw the initial state
    flowValueSpan.textContent = flowIntensityInput.value;
    durationValueSpan.textContent = simDurationInput.value;


</script>
```