---
title: "מסע אל מתחת לפני השטח: איך ראדאר חודר קרקע (GPR) חושף סודות קבורים?"
english_slug: how-ground-penetrating-radar-gpr-works
category: "מדעי הסביבה / גיאולוגיה"
tags: [ראדאר חודר קרקע, GPR, גיאופיזיקה, גלים אלקטרומגנטיים, חקר תת-קרקעי, סימולציה]
---
# מסע אל מתחת לפני השטח: איך ראדאר חודר קרקע (GPR) חושף סודות קבורים?

האם עצרתם פעם לחשוב איך מהנדסים, ארכיאולוגים או חוקרים סביבתיים "רואים" מה קבור עמוק מתחת לרגלינו, מבלי להזיז אפילו גרגר אדמה אחד? דמיינו לרגע שיש לכם עין רנטגן שיכולה לחדור את הקרקע... ובכן, טכנולוגיית GPR (ראדאר חודר קרקע) היא הדבר הקרוב ביותר לכך! היא משתמשת בגלי רדיו חכמים כדי למפות את מה שחבוי מתחת לפני השטח. בואו נצלול לגלות איך זה עובד.

<div id="gpr-simulation-container">
    <div class="controls">
        <label for="antenna-position" class="control-label">מיקום האנטנה:</label>
        <input type="range" id="antenna-position" name="antenna-position" min="50" max="450" value="250">
        <span id="antenna-pos-value">250</span> פיקסלים
        <button id="scan-button" class="control-button">בצע סריקה!</button>
        <div class="soil-control">
             <label for="soil-type" class="control-label">סוג הקרקע:</label>
            <select id="soil-type">
                <option value="dry_sand">חול יבש (מהיר ויבש)</option>
                <option value="wet_soil">קרקע לחה (איטי ורטוב)</option>
                 <option value="clay">חימר מוליך (סופג גלים)</option>
            </select>
        </div>
    </div>
    <canvas id="gpr-canvas" width="500" height="400"></canvas>
    <div class="graph-container">
        <canvas id="gpr-graph-canvas" width="500" height="200"></canvas>
        <div class="graph-labels">
            <span class="graph-xlabel">זמן חזרת הגל / עומק משוער</span>
            <span class="graph-ylabel">עוצמת ההחזר (סיגנל)</span>
        </div>
    </div>
</div>

<style>
    #gpr-simulation-container {
        font-family: 'Arial', sans-serif;
        max-width: 550px; /* Slightly wider for better control layout */
        margin: 20px auto;
        border: 1px solid #d3d3d3; /* Softer border */
        padding: 20px;
        border-radius: 10px; /* More rounded */
        background-color: #f0f0f0; /* Lighter background */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        overflow: hidden; /* Clear floats */
    }

    .controls {
        margin-bottom: 20px;
        text-align: center;
        display: flex; /* Use flexbox for better control alignment */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center; /* Center controls */
        gap: 10px; /* Space between controls */
    }

    .control-label {
        font-weight: bold;
        color: #555;
         flex-basis: 100%; /* Labels take full width on wrap */
         text-align: center;
    }

    .controls label, .controls input[type="range"], .controls button, .controls select {
        vertical-align: middle;
    }

    .controls input[type="range"] {
        width: 250px; /* Make slider a bit wider */
        -webkit-appearance: none; /* Remove default appearance */
        appearance: none;
        height: 8px;
        background: #ddd;
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
        width: 18px;
        height: 18px;
        background: #007bff; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 1px solid #0056b3;
     }

      .controls input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
         border: 1px solid #0056b3;
      }

    .control-button {
        padding: 10px 20px;
        background-color: #007bff; /* Blue button */
        color: white;
        border: none;
        border-radius: 5px; /* More rounded button */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
    }

    .control-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
     .control-button:active {
        transform: scale(0.98); /* Slightly shrink on click */
     }

    .soil-control {
        margin-top: 10px; /* Space above soil control */
        flex-basis: 100%; /* Takes full width below other controls */
         text-align: center;
    }

    select {
        padding: 8px 12px;
        border-radius: 5px;
        border: 1px solid #ccc;
        background-color: #fff;
        font-size: 1em;
         cursor: pointer;
    }

    #gpr-canvas {
        border: 1px solid #000;
        display: block;
        margin: 0 auto 15px auto; /* Space below canvas */
        background-color: #e0f0ff; /* Sky */
        border-radius: 5px;
    }

    .graph-container {
         position: relative; /* For positioning labels */
         width: 500px;
         margin: 0 auto;
         border: 1px solid #000;
         border-radius: 5px;
         overflow: hidden;
         background-color: #fff;
    }

     #gpr-graph-canvas {
        display: block;
        background-color: #fff;
    }

     .graph-labels {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none; /* Allow clicks to pass through */
     }

    .graph-xlabel {
        position: absolute;
        bottom: 5px;
        left: 0;
        right: 0;
        text-align: center;
        font-size: 0.9em;
        color: #555;
    }

    .graph-ylabel {
        position: absolute;
        top: 50%;
        left: 5px; /* Adjust as needed */
        transform: translateY(-50%) rotate(-90deg);
        transform-origin: center;
        font-size: 0.9em;
        color: #555;
    }


    .antenna {
        fill: #dc3545; /* Red antenna */
        stroke: #000;
        stroke-width: 1;
    }

     .antenna text {
         font-family: Arial, sans-serif;
         font-size: 12px;
         text-anchor: middle;
         fill: #000;
     }

    .pulse {
        fill: rgba(0, 123, 255, 0.4); /* Semi-transparent blue */
        stroke: rgba(0, 123, 255, 0.6);
        stroke-width: 1.5;
    }

     .reflection-point {
         fill: orange;
         stroke: #c67605;
         stroke-width: 1;
     }

     .return-wave {
         fill: rgba(102, 16, 242, 0.6); /* Purple return wave dot */
         stroke: rgba(102, 16, 242, 0.8);
         stroke-width: 1.5;
     }


    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #6c757d; /* Grey button */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
         transition: background-color 0.3s ease;
    }

    #toggle-explanation:hover {
        background-color: #5a6268; /* Darker grey on hover */
    }


    #explanation {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        display: none; /* Initially hidden */
    }

    #explanation h2 {
        color: #333;
        border-bottom: 2px solid #eee; /* Lighter border */
        padding-bottom: 8px;
        margin-top: 25px;
        font-size: 1.4em;
    }

     #explanation h2:first-child {
         margin-top: 0;
     }

    #explanation p {
        line-height: 1.7; /* More line spacing */
        margin-bottom: 15px;
        color: #444;
    }

     #explanation ul {
         margin-bottom: 15px;
         padding-left: 20px; /* Indent list */
     }

     #explanation li {
         margin-bottom: 10px; /* Space out list items */
         line-height: 1.6;
         color: #444;
     }

      #explanation strong {
          color: #333;
      }

</style>

<button id="toggle-explanation">גלו את הסודות: הצגת ההסבר על GPR</button>

<div id="explanation">
    <h2>קסם בלתי נראה: מהו ראדאר חודר קרקע (GPR)?</h2>
    <p>דמיינו מכשיר שיכול לשלוח גלים חכמים לתוך האדמה ו"לשמוע" את ההד החוזר מהם, וכך לצייר מפה של כל מה שחבוי שם למטה! זה בדיוק מה שעושה ראדאר חודר קרקע (Ground Penetrating Radar - GPR), הידוע גם כגאוראדאר. זוהי שיטה מדעית מתקדמת המשתמשת בגלים אלקטרומגנטיים כדי לחשוף עולמות תת-קרקעיים נסתרים - תשתיות קבורות, שרידים ארכיאולוגיים, סלעים, חללים ואפילו שינויים דקים בהרכב הקרקע - הכל מבלי לחפור כף אחת!</p>

    <h2>הלב הפועם: שימוש בגלים אלקטרומגנטיים</h2>
    <p>GPR פועל על עקרון דומה מאוד לראדאר או סונאר, רק שהתווך משתנה. במקום גלי רדיו באוויר או גלי קול במים, הוא שולח פולסים קצרים ואינטנסיביים של גלים אלקטרומגנטיים (בדרך כלל בתדרי רדיו) לתוך הקרקע. הגלים הללו מתחילים את מסעם מטה, מתפשטים בתוך האדמה.</p>

    <h2>שידור, מסע וחזרה: תהליך הפעולה</h2>
    <p>מערכת GPR מורכבת מאנטנה אחת או שתיים הממוקמות קרוב לפני השטח. אנטנת השידור שולחת את הפולס העוצמתי אל תוך הקרקע. הגל מתפשט ונע דרך החומרים התת-קרקעיים.</p>

    <h2>"הד" ממעמקי האדמה: מה גורם להחזר גל?</h2>
    <p>כאשר הגל החודר נתקל במעבר בין שני חומרים תת-קרקעיים שיש להם תכונות חשמליות שונות באופן משמעותי - בעיקר שינוי ב<strong>פרימיטיביות דיאלקטרית</strong> (יכולת החומר לאגור אנרגיה חשמלית) או <strong>מוליכות</strong> (יכולת החומר להעביר זרם חשמלי) - חלק מהאנרגיה של הגל מוחזר או מפוזר בחזרה כלפי מעלה. חשבו על גל אור הפוגע במראה או על הד קול החוזר מקיר. ממשקים כאלה יכולים להיות גבול בין שכבות קרקע שונות (למשל, חול מעל חימר), אובייקט קבור (צינור, אבן גדולה, קבר), או אפילו חלל מלא אוויר.</p>

    <h2>מדידת הזמן: סוד העומק</h2>
    <p>מערכת ה-GPR מקשיבה בקשב רב לאנטנת הקליטה ומודדת במדויק את הזמן המזערי שלוקח לכל הד שחוזר להגיע אליה מרגע שידור הפולס. מכיוון שמהירות הגל בקרקע ידועה (או שניתן להעריך ולכייל אותה), המכשיר יכול לחשב את המרחק הכולל שהגל עבר (הלוך ושוב). חלוקת המרחק הכולל בשתיים נותנת את עומק הממשק או האובייקט שגרם להחזר!</p>
    <p>הנוסחה פשוטה: **עומק = (מהירות הגל) * (זמן מעבר כפול) / 2**</p>

    <h2>מהירות הגל: לא הכל שווה באדמה!</h2>
    <p>מהירות הגלים האלקטרומגנטיים בקרקע אינה קבועה - היא משתנה משמעותית בהתאם לתכונות החומרים שהם עוברים דרכם. הגורם המשפיע ביותר הוא לרוב <strong>תכולת המים</strong>. למים יש פרימיטיביות דיאלקטרית גבוהה בהרבה מאוויר או מרוב מינרלי הקרקע. ככל שיש יותר מים בקרקע, הפרימיטיביות הדיאלקטרית הכוללת עולה ו<strong>מהירות הגל יורדת</strong>. קרקע מוליכה מאוד (כמו חימר רטוב או קרקע מלוחה) לא רק מאטה את הגלים, אלא גם בולעת אותם במהירות, ומגבילה מאוד את עומק החדירה.</p>
    <ul>
        <li><strong>חול יבש/חצץ:</strong> מהירות גל גבוהה יחסית, חדירה טובה.</li>
        <li><strong>קרקע לחה/רוויה:</strong> מהירות גל נמוכה משמעותית, חדירה פחותה.</li>
        <li><strong>חימר מוליך/קרקע מלוחה:</strong> מהירות גל נמוכה מאוד, ספיגה גבוהה, חדירה מוגבלת לעומק רדוד.</li>
    </ul>
    <p>הבנת סוג הקרקע והערכת מהירות הגל חיונית כדי לתרגם נכון את זמני ההחזר לעומקים מדויקים.</p>

    <h2>היפרבולות בגרף: חתימת האובייקט הבודד</h2>
    <p>בגרף ה-GPR (המכונה רדארגרם), הד מחתיכת אובייקט בודד (כמו צינור או אבן) שנקלעת לשדה הסריקה לא מופיע רק בנקודה אחת. מכיוון שהגל מתפשט במעין חצי כדור מתחת לאנטנה, האנטנה "תראה" את האובייקט ותקבל ממנו החזר עוד לפני שהיא בדיוק מעליו, ושוב אחרי שהיא עברה אותו. ככל שהאנטנה רחוקה יותר צידית מהאובייקט, הגל צריך לעבור מסלול ארוך יותר, ולכן זמן ההחזר יהיה ארוך יותר. כשמשרטטים את זמני ההחזר הללו כפונקציה של מיקום האנטנה לאורך קו, מתקבלת צורה דמוית קשת או <strong>היפרבולה</strong>. קודקוד ההיפרבולה מצביע על מיקום האובייקט ועומקו המינימלי.</p>

    <h2>מה מגביל את ה-GPR?</h2>
    <p>למרות העוצמה שלו, ל-GPR יש מגבלות:</p>
    <ul>
        <li><strong>עומק החדירה:</strong> המגבלה העיקרית. תלויה מאוד במוליכות הקרקע ובתדר האנטנה. בקרקע מוליכה מאוד, החדירה יכולה להיות רק סנטימטרים בודדים. תדרים נמוכים חודרים עמוק יותר אך רואים פחות פרטים קטנים. תדרים גבוהים נותנים תמונה מפורטת אך רק קרוב לפני השטח.</li>
        <li><strong>רזולוציה:</strong> היכולת להבחין בין אובייקטים סמוכים תלויה באורך הגל (ולכן בתדר ובמהירות).</li>
        <li><strong>קרקעות מוליכות:</strong> כאמור, הן אויב עיקרי של GPR ומגבילות את יכולת השיטה.</li>
    </ul>

    <h2>מגוון שימושים: איפה פוגשים GPR בעולם האמיתי?</h2>
    <p>GPR הוא כלי רב עוצמה במגוון תחומים:</p>
    <ul>
        <li><strong>הנדסה אזרחית:</strong> איתור קווי מים, גז, חשמל ותקשורת תת-קרקעיים לפני חפירה; בדיקת בטון, כבישים וגשרים.</li>
        <li><strong>ארכיאולוגיה:</strong> גילוי מבנים קבורים, קירות, רצפות וקברים ללא פגיעה באתרים עדינים.</li>
        <li><strong>סביבה:</strong> מיפוי גבולות זיהום בקרקע, איתור מכלי דלק תת-קרקעיים ישנים.</li>
        <li><strong>בטחון:</strong> איתור מוקשים, חפצים אסורים קבורים.</li>
        <li><strong>גאולוגיה:</strong> מיפוי שכבות גאולוגיות רדודות, איתור חללים תת-קרקעיים.</li>
    </ul>
</div>

<script>
    const canvas = document.getElementById('gpr-canvas');
    const ctx = canvas.getContext('2d');
    const graphCanvas = document.getElementById('gpr-graph-canvas');
    const graphCtx = graphCanvas.getContext('2d');
    const antennaSlider = document.getElementById('antenna-position');
    const antennaPosValueSpan = document.getElementById('antenna-pos-value');
    const scanButton = document.getElementById('scan-button');
    const soilTypeSelect = document.getElementById('soil-type');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;
    const groundSurfaceY = 50; // Y coordinate for the ground surface
    const antennaSize = 25; // Slightly larger antenna visual

    // Simulation parameters based on soil type
    const soilTypes = {
        dry_sand: {
            name: "חול יבש",
            color: "#c2b280", // Sand color
            waveSpeed: 0.12, // m/ns (higher speed)
            permittivity: 5, // Example relative permittivity
            absorption: 0.04 // Lower absorption (deeper penetration)
        },
        wet_soil: {
            name: "קרקע לחה",
            color: "#8b4513", // Brown soil color
            waveSpeed: 0.05, // m/ns (slower speed)
            permittivity: 20, // Higher permittivity due to water
            absorption: 0.15 // Higher absorption (less penetration)
        },
         clay: {
            name: "חימר מוליך",
            color: "#a0522d", // Clay color
            waveSpeed: 0.03, // m/ns (very slow)
            permittivity: 30, // Very high permittivity
            absorption: 0.6 // Very high absorption (minimal penetration)
        }
    };

    let currentSoilType = soilTypes[soilTypeSelect.value];
    let waveSpeed = currentSoilType.waveSpeed; // Current wave speed
    let absorption = currentSoilType.absorption; // Current absorption

    // Objects below the surface (x, y, type, properties)
    // Y is depth relative to groundSurfaceY
    const objects = [
        { id: 'pipe1', x: 150, y: 100, radius: 15, type: 'metal_pipe', color: '#555', reflectivity: 0.9, permittivity: Infinity }, // Metal pipe
        { id: 'rock1', x: 350, y: 150, radius: 20, type: 'rock', color: '#888', reflectivity: 0.5, permittivity: 8 }, // Large rock
        { id: 'cavity1', x: 250, y: 220, width: 60, height: 30, type: 'cavity', color: '#eee', reflectivity: -0.7, permittivity: 1 }, // Empty space (negative reflection)
        { id: 'pvc1', x: 400, y: 80, radius: 10, type: 'pvc_pipe', color: '#bbb', reflectivity: 0.3, permittivity: 3 }, // PVC pipe
        { id: 'pipe2', x: 100, y: 250, radius: 12, type: 'pvc_pipe', color: '#ccc', reflectivity: 0.2, permittivity: 3 } // Another PVC pipe deeper
    ];

    // Layers (y start, y end, type, properties)
    // Y is depth relative to groundSurfaceY
    const layers = [
        { id: 'topsoil', yStart: 0, yEnd: 150, color: currentSoilType.color, permittivity: currentSoilType.permittivity },
        { id: 'subsoil', yStart: 150, yEnd: canvasHeight - groundSurfaceY, color: '#d2b48c', permittivity: 10 } // Different soil layer below
    ];

    let antennaX = parseInt(antennaSlider.value);

    // Graph parameters
    const graphHeight = graphCanvas.height;
    const graphWidth = graphCanvas.width;
    const graphMargin = 30; // Increased margin for labels
    const graphDataPoints = 500; // Number of samples in the received signal trace

    // Animation variables
    let animationFrameId = null;
    let activeScan = null; // Object holding state for the current scan animation

    // Timing and scaling for animation vs simulation time
    // Map the maximum possible vertical round trip time to a visual duration in real milliseconds
    const maxVisualScanDepth = canvasHeight - groundSurfaceY; // Max depth to show in simulation
    const maxVerticalSimTime = (maxVisualScanDepth * 2) / soilTypes.dry_sand.waveSpeed; // Max sim time (ns) for vertical round trip in fastest medium
    const animationDurationMs = 4000; // Total real time milliseconds for a full scan cycle animation in fastest medium (adjust as needed)
    let simTimePerMs = maxVerticalSimTime / animationDurationMs; // How many simulation nanoseconds correspond to 1 real millisecond of animation

    // --- Drawing Functions ---

    function drawGround() {
        // Draw sky
        ctx.fillStyle = '#e0f0ff';
        ctx.fillRect(0, 0, canvasWidth, groundSurfaceY);

        // Draw layers
        layers.forEach(layer => {
            ctx.fillStyle = layer.color;
            ctx.fillRect(0, groundSurfaceY + layer.yStart, canvasWidth, layer.yEnd - layer.yStart);
            // Add a subtle texture or line for interfaces
             ctx.strokeStyle = 'rgba(0,0,0,0.1)';
             ctx.beginPath();
             ctx.moveTo(0, groundSurfaceY + layer.yStart);
             ctx.lineTo(canvasWidth, groundSurfaceY + layer.yStart);
             ctx.stroke();
        });


        // Draw surface line
        ctx.strokeStyle = '#555'; // Darker surface line
        ctx.lineWidth = 3; // Thicker surface line
        ctx.beginPath();
        ctx.moveTo(0, groundSurfaceY);
        ctx.lineTo(canvasWidth, groundSurfaceY);
        ctx.stroke();
    }

    function drawObjects() {
        objects.forEach(obj => {
            ctx.fillStyle = obj.color;
            ctx.beginPath();
            const objY = groundSurfaceY + obj.y; // Absolute Y position
            if (obj.type === 'metal_pipe' || obj.type === 'rock' || obj.type === 'pvc_pipe') {
                ctx.arc(obj.x, objY, obj.radius, 0, Math.PI * 2);
            } else if (obj.type === 'cavity') {
                ctx.fillRect(obj.x - obj.width / 2, objY - obj.height / 2, obj.width, obj.height);
                ctx.strokeStyle = '#555';
                ctx.lineWidth = 1;
                ctx.strokeRect(obj.x - obj.width / 2, objY - obj.height / 2, obj.width, obj.height);
            }
            ctx.fill();
            ctx.strokeStyle = '#333';
            ctx.lineWidth = 1;
            ctx.stroke();
        });
    }

    function drawAntenna(isScanning = false) {
        const antennaTopY = groundSurfaceY - antennaSize;
        ctx.fillStyle = isScanning ? '#ffc107' : '#dc3545'; // Yellow when scanning, Red otherwise
        ctx.fillRect(antennaX - antennaSize / 2, antennaTopY, antennaSize, antennaSize);
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(antennaX - antennaSize / 2, antennaTopY, antennaSize, antennaSize);

        ctx.fillStyle = '#000';
        ctx.font = '14px Arial'; // Slightly larger font
        ctx.textAlign = 'center';
        ctx.fillText("GPR", antennaX, antennaTopY - 8); // Label position
    }


    function drawGraph(signalData) {
        graphCtx.clearRect(0, 0, graphWidth, graphHeight);
        graphCtx.fillStyle = '#fff';
        graphCtx.fillRect(0, 0, graphWidth, graphHeight);

        // Draw axes
        graphCtx.strokeStyle = '#000';
        graphCtx.lineWidth = 1;
        graphCtx.beginPath();
        // X axis (Time/Depth)
        graphCtx.moveTo(graphMargin, graphHeight - graphMargin);
        graphCtx.lineTo(graphWidth - graphMargin, graphHeight - graphMargin);
        // Y axis (Amplitude)
        graphCtx.moveTo(graphMargin, graphMargin);
        graphCtx.lineTo(graphMargin, graphHeight - graphMargin);
        graphCtx.stroke();

        // Draw the signal trace
        graphCtx.strokeStyle = '#007bff'; // Blue trace
        graphCtx.lineWidth = 2;
        graphCtx.beginPath();

        // Scale graph data: X axis is sample index (time/depth), Y axis is amplitude
        const maxAmplitude = 1; // Normalized reflection coefficients are between -1 and 1. Max possible signal could exceed 1 with multiple overlaps, but visually scale to a fixed max. Let's use 1.5 as a visual max.
        const effectiveMaxAmplitude = 1.5;
        const xScale = (graphWidth - 2 * graphMargin) / graphDataPoints;
        const yScale = (graphHeight - 2 * graphMargin) / (2 * effectiveMaxAmplitude); // Amplitude goes from -max to +max

        for (let i = 0; i < graphDataPoints; i++) {
            const x = graphMargin + i * xScale;
            const y = (graphHeight - graphMargin) - (signalData[i] * yScale); // Invert Y axis for amplitude
            if (i === 0) {
                graphCtx.moveTo(x, y);
            } else {
                graphCtx.lineTo(x, y);
            }
        }
        graphCtx.stroke();

         // Add a zero line for amplitude
        graphCtx.strokeStyle = '#ccc';
        graphCtx.beginPath();
        graphCtx.moveTo(graphMargin, graphHeight - graphMargin - (0 * yScale));
        graphCtx.lineTo(graphWidth - graphMargin, graphHeight - graphMargin - (0 * yScale));
        graphCtx.stroke();
    }


    // --- Simulation Logic ---

     // Function to get effective permittivity and absorption at a specific depth (y relative to surface)
    function getMaterialPropertiesAtDepth(depth) {
        let props = { permittivity: currentSoilType.permittivity, absorption: currentSoilType.absorption };
        for (const layer of layers) {
            if (depth >= layer.yStart && depth < layer.yEnd) {
                props.permittivity = layer.permittivity;
                // Absorption rate might also change per layer, but for simplicity, let's use the topsoil absorption.
                // props.absorption = layer.absorption; // If layers had absorption properties
                 break; // Found the layer
            }
        }
         // Handle objects - not needed for background material properties, only for reflection points
        return props;
    }


    function calculateReflectionCoefficient(material1, material2) {
        // Simplified Fresnel Reflection Coefficient for Perpendicular Incidence
        // R = (sqrt(eps1) - sqrt(eps2)) / (sqrt(eps1) + sqrt(eps2))
        // where eps is relative permittivity
        const eps1 = material1.permittivity;
        const eps2 = material2.permittivity;

        if (eps1 === undefined || eps2 === undefined) return 0;
        if (eps1 === Infinity || eps2 === Infinity) { // Reflection off a perfect conductor (metal) is close to -1
             return -1.0; // Metal reflections are often inverted polarity
        }
        if (eps1 <= 0 || eps2 <= 0) return 0; // Should not happen with physical permittivities

        const reflectionCoefficient = (Math.sqrt(eps1) - Math.sqrt(eps2)) / (Math.sqrt(eps1) + Math.sqrt(eps2));
        return reflectionCoefficient;
    }

     // Calculate two-way travel time and amplitude for a reflection point
     // pointX, pointY (depth relative to surface) are the location of the reflection
     // antennaX, groundSurfaceY is the antenna location
     // currentSoilProperties includes waveSpeed and absorption
     function calculateReflectionEvent(antennaX, pointX, pointY, reflectingMaterialPermittivity, pointType) {
        const dx = pointX - antennaX;
        const dy = pointY; // Depth

        // For simplicity, assume wave travels in a straight line at the *average* speed or speed of the layer it's in.
        // A more complex sim would trace ray paths considering refraction.
        // Let's simplify and use the speed of the layer the reflection point is in for two-way time calculation.
        const materialProps = getMaterialPropertiesAtDepth(pointY);
        const currentWaveSpeed = materialProps.waveSpeed || waveSpeed; // Use layer speed or default
        const currentAbsorption = materialProps.absorption || absorption; // Use layer absorption or default


        const distanceOneWay = Math.sqrt(dx * dx + dy * dy); // Direct line distance
        const travelTimeSim = (distanceOneWay * 2) / currentWaveSpeed; // Total two-way simulation time (ns)

         // Calculate reflection coefficient - need permittivity *before* the reflection point
         // This is complex with ray tracing. Let's simplify: Use the permittivity *at* the reflection point's depth for the 'before' material
         // and the reflectingMaterialPermittivity for the 'after' material. This is a simplification.
         const surroundingPermittivity = materialProps.permittivity;
         const reflectionCoefficient = calculateReflectionCoefficient({permittivity: surroundingPermittivity}, {permittivity: reflectingMaterialPermittivity});

        // Apply absorption based on the total path distance
        // Use exponential decay: Amplitude = InitialAmplitude * exp(-absorption_rate * distance)
        // Absorption rate could be per meter or per pixel. Let's scale based on visual depth.
        // Scale absorption factor so 1 unit of 'absorption' means significant decay over the full depth.
        const absorptionFactor = Math.exp(-currentAbsorption * (distanceOneWay * 2) / maxVisualScanDepth * 1.5); // Scale absorption by depth

        const reflectedAmplitude = reflectionCoefficient * absorptionFactor; // Include object's reflectivity if applicable (already part of coefficient conceptually here)

         if (Math.abs(reflectedAmplitude) < 0.01) { // Threshold for weak signals
             return null; // Signal too weak to detect
         }

         // For animation, we need the hit point and the return path start
         const hitPoint = { x: pointX, y: groundSurfaceY + pointY }; // Absolute canvas coordinates
         // For simplicity, assume return wave starts from the hit point location
         const returnStartPoint = hitPoint;

         return {
             simTime: travelTimeSim, // Total two-way simulation time (ns)
             amplitude: reflectedAmplitude, // Final amplitude for the graph
             hitPoint: hitPoint, // Where the wave hit the object/layer interface visually
             returnStartPoint: returnStartPoint, // Where the visual return wave animation starts
             type: pointType // 'object' or 'layer'
         };
     }


    function startScanAnimation(x) {
        if (activeScan) { // Don't start if already scanning
            return;
        }

        // --- Pre-calculate Reflection Events ---
        const reflectionEvents = [];

        // Layer interfaces
         let previousLayerY = 0; // Relative to groundSurfaceY
         layers.forEach((nextLayer, index) => {
            const interfaceY = nextLayer.yStart; // Y relative to ground surface
            if (interfaceY > previousLayerY && interfaceY <= canvasHeight - groundSurfaceY) {
                 const depth = interfaceY;
                 // Need permittivity of the layer *before* and *after* this interface. Assuming layers are sorted by yStart.
                 const prevLayerPermittivity = (index > 0) ? layers[index-1].permittivity : currentSoilType.permittivity;
                 const nextLayerPermittivity = nextLayer.permittivity;

                 const event = calculateReflectionEvent(
                     x, // Antenna X
                     x, // Reflection point X (assume directly below for layer interface)
                     depth, // Reflection point Y (depth)
                     nextLayerPermittivity, // The material properties *after* the interface
                     'layer'
                 );
                 if (event) reflectionEvents.push(event);

                 previousLayerY = interfaceY; // Update for next iteration
            }
        });


        // Objects
        objects.forEach(obj => {
             const event = calculateReflectionEvent(
                 x, // Antenna X
                 obj.x, // Object X
                 obj.y, // Object Y (depth)
                 obj.permittivity, // Object material permittivity
                 'object'
             );
             if (event) reflectionEvents.push(event);
        });

        // Sort events by the time they arrive back at the antenna
        reflectionEvents.sort((a, b) => a.simTime - b.simTime);


        // --- Initialize Scan State ---
        const currentSimTimePerMs = (maxVerticalSimTime / animationDurationMs) * (soilTypes.dry_sand.waveSpeed / waveSpeed); // Adjust animation speed based on current soil wave speed
        const maxSimTimeRepresentedOnGraph = ((canvasHeight - groundSurfaceY) * 2) / waveSpeed; // Max vertical time in the *current* soil

        activeScan = {
            antennaX: x,
            startTime: performance.now(), // Real time scan started
            reflectionEvents: reflectionEvents,
            receivedSignal: new Array(graphDataPoints).fill(0),
            currentSimTimeReached: 0, // Simulation time reached in animation (ns)
            maxGraphSimTime: maxSimTimeRepresentedOnGraph, // Max sim time on graph (ns)
            simTimePerMs: currentSimTimePerMs, // Sim time units per real ms
            activeReturnWaves: [], // Visual return waves {startX, startY, startSimTime, endSimTime}
            hitPointsVisual: [] // Visual hit points {x, y, displayUntilSimTime}
        };

        // Start the animation loop
         if (!animationFrameId) {
             animate(performance.now());
        }
    }

    // --- Animation Loop ---
    function animate(currentTime) {
        if (!activeScan) { // Stop if no active scan
             animationFrameId = null;
             return;
        }

        const elapsedRealTime = (currentTime - activeScan.startTime);
        // Calculate current simulation time reached based on real elapsed time and wave speed
        activeScan.currentSimTimeReached = elapsedRealTime * activeScan.simTimePerMs;


        // --- Drawing ---
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);
        drawGround();
        drawObjects();
        drawAntenna(true); // Indicate scanning

        // --- Animate Downward Pulse ---
        // The visual distance of the pulse is based on one-way sim time
        const currentOneWaySimTime = activeScan.currentSimTimeReached / 2;
        // Map currentOneWaySimTime to visual distance from antenna.
        // Scale max vertical one-way sim time (maxGraphSimTime / 2) to maxVisualScanDepth
        const maxVerticalOneWaySimTime = activeScan.maxGraphSimTime / 2;
        const visualDistanceScale = maxVisualScanDepth / maxVerticalOneWaySimTime; // Pixels per sim time unit (ns)

        const pulseVisualDistance = currentOneWaySimTime * visualDistanceScale;

        // Draw the pulse spreading downwards from the antenna
        if (pulseVisualDistance > 0) {
             ctx.fillStyle = 'rgba(0, 123, 255, 0.4)'; // Blue wave
             ctx.beginPath();
             // Draw an arc segment that starts below the antenna
             // Angle range can be adjusted for effect
             const startAngle = Math.PI * 0.05; // Narrower spread initially
             const endAngle = Math.PI * 0.95;
             ctx.arc(activeScan.antennaX, groundSurfaceY, pulseVisualDistance, startAngle, endAngle, false);
             ctx.lineTo(activeScan.antennaX, groundSurfaceY); // Close the shape back to antenna
             ctx.fill();

             // Optional: Draw a wave line instead of filled shape
             // ctx.strokeStyle = 'rgba(0, 123, 255, 0.8)';
             // ctx.lineWidth = 2;
             // ctx.beginPath();
             // ctx.arc(activeScan.antennaX, groundSurfaceY, pulseVisualDistance, startAngle, endAngle, false);
             // ctx.stroke();
        }


        // --- Process Reflection Events & Start Return Waves ---
        activeScan.reflectionEvents.forEach(event => {
             // Check if downward pulse reached the reflection point (one-way time)
             if (!event.hit && (event.simTime / 2) <= activeScan.currentSimTimeReached) {
                 event.hit = true; // Mark event as hit

                 // Add visual hit point marker (temporary)
                 activeScan.hitPointsVisual.push({
                     x: event.hitPoint.x,
                     y: event.hitPoint.y,
                     displayUntilSimTime: activeScan.currentSimTimeReached + (activeScan.maxGraphSimTime * 0.05) // Show for a short sim duration
                 });

                 // Start the return wave animation
                 activeScan.activeReturnWaves.push({
                     startX: event.hitPoint.x,
                     startY: event.hitPoint.y,
                     startSimTime: activeScan.currentSimTimeReached, // Return starts when hit
                     endSimTime: event.simTime, // Return ends when signal reaches antenna (total two-way time)
                     amplitude: event.amplitude // Amplitude for adding to graph
                 });
             }

             // Check if return wave reached the antenna (two-way time)
             if (!event.received && event.simTime <= activeScan.currentSimTimeReached) {
                 event.received = true; // Mark event as received

                 // Add signal contribution to the graph
                 const timeIndex = Math.floor((event.simTime / activeScan.maxGraphSimTime) * graphDataPoints);
                 if (timeIndex < graphDataPoints) {
                      // Add a simplified waveform shape instead of just a single point amplitude
                      // Create a small peak/trough around the arrival time
                      const peakWidthSamples = Math.max(2, Math.floor(graphDataPoints / 200)); // Make peak width relative to graph size
                      for (let i = -peakWidthSamples; i <= peakWidthSamples; i++) {
                           const idx = timeIndex + i;
                           if (idx >= 0 && idx < graphDataPoints) {
                                // Use a smooth function like Gaussian or raised cosine for the waveform shape
                                const waveformShape = Math.cos(i / peakWidthSamples * Math.PI / 2); // Raised cosine, peaks at 0, 0 at edges
                                // Add the peak amplitude * waveform shape. Accumulate if multiple reflections arrive at same time.
                                activeScan.receivedSignal[idx] += event.amplitude * waveformShape;
                           }
                      }
                 }
             }
        });

        // Clean up expired hit point visuals
        activeScan.hitPointsVisual = activeScan.hitPointsVisual.filter(hp => hp.displayUntilSimTime > activeScan.currentSimTimeReached);

        // Draw visual hit points
         activeScan.hitPointsVisual.forEach(hp => {
             ctx.fillStyle = 'orange';
             ctx.beginPath();
             ctx.arc(hp.x, hp.y, 5, 0, Math.PI*2);
             ctx.fill();
         });


        // --- Animate Active Return Waves ---
        activeScan.activeReturnWaves = activeScan.activeReturnWaves.filter(returnWave => {
            const returnSimTimeElapsed = activeScan.currentSimTimeReached - returnWave.startSimTime;
            const returnSimDuration = returnWave.endSimTime - returnWave.startSimTime;

            if (returnSimTimeElapsed < 0 || returnSimDuration <= 0) { // Not started yet or instant return?
                return true; // Keep if not started
            }

            const fractionCovered = Math.min(1, returnSimTimeElapsed / returnSimDuration);

            // Calculate current position along the path from start to antenna
            const targetX = activeScan.antennaX;
            const targetY = groundSurfaceY;
            const currentX = returnWave.startX + (targetX - returnWave.startX) * fractionCovered;
            const currentY = returnWave.startY + (targetY - returnWave.startY) * fractionCovered;


            // Draw returning wave visual (dot)
            ctx.fillStyle = 'rgba(102, 16, 242, 0.8)'; // Purple
            ctx.beginPath();
            ctx.arc(currentX, currentY, 5 * (1 - fractionCovered * 0.5), 0, Math.PI*2); // Dot shrinks slightly as it returns
            ctx.fill();

            // Remove wave if it reached the antenna (or slightly past in sim time)
            return fractionCovered < 1;
        });


        // --- Draw Graph (Incremental) ---
        // Find the index on the graph corresponding to the current simulation time
        const currentGraphIndex = Math.floor((activeScan.currentSimTimeReached / activeScan.maxGraphSimTime) * graphDataPoints);
        // Create a temporary signal array up to the current index for drawing
        const signalToDraw = activeScan.receivedSignal.slice(0, currentGraphIndex + 1);
        // Pad the rest with zeros so the graph doesn't shrink
        while(signalToDraw.length < graphDataPoints) {
            signalToDraw.push(0);
        }

        drawGraph(signalToDraw);


        // --- Check for Animation End ---
        // Animation ends when all reflection events have been processed AND all active return waves are finished
        const allEventsReceived = activeScan.reflectionEvents.every(event => event.received);
        const noActiveReturnWaves = activeScan.activeReturnWaves.length === 0;

        // Also, ensure the current simulation time has passed the latest possible reflection time on the graph + buffer
        const maxEventSimTime = activeScan.reflectionEvents.reduce((max, event) => Math.max(max, event.simTime), 0);
        const simulationTimeBuffer = activeScan.maxGraphSimTime * 0.1; // Add 10% buffer time
        const simTimePastMaxEvent = activeScan.currentSimTimeReached > (maxEventSimTime + simulationTimeBuffer);


        if (allEventsReceived && noActiveReturnWaves && simTimePastMaxEvent) {
            activeScan = null; // End the scan
            drawAntenna(false); // Draw antenna not scanning
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
            console.log("Scan finished");
        } else {
             animationFrameId = requestAnimationFrame(animate);
        }
    }


    // --- Event Listeners ---

    antennaSlider.addEventListener('input', (event) => {
        antennaX = parseInt(event.target.value);
        antennaPosValueSpan.textContent = antennaX;
        // Only redraw static scene when moving slider if not scanning
        if (!activeScan) {
             ctx.clearRect(0, 0, canvasWidth, canvasHeight);
             drawGround();
             drawObjects();
             drawAntenna(false);
             // Keep graph as is
        }
    });

    scanButton.addEventListener('click', () => {
        if (!activeScan) { // Only scan if not already scanning
            startScanAnimation(antennaX); // Trigger scan and animation
        } else {
            console.log("Scan already in progress.");
        }
    });

    soilTypeSelect.addEventListener('change', (event) => {
        currentSoilType = soilTypes[event.target.value];
        waveSpeed = currentSoilType.waveSpeed;
        absorption = currentSoilType.absorption;

         // Update layer colors/properties based on the new soil type (only for the relevant layers)
         layers.forEach(layer => {
             if (layer.id === 'topsoil') { // Assume 'topsoil' is the one that changes
                 layer.color = currentSoilType.color;
                 layer.permittivity = currentSoilType.permittivity;
             }
             // Could update other layers too if soil type affects deeper layers
         });


        // Reset and redraw static elements
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);
        drawGround(); // Redraw ground with new colors/properties
        drawObjects();
        drawAntenna(false);

        // Clear the graph
        drawGraph(new Array(graphDataPoints).fill(0));

        // Stop any ongoing animation
        if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
             animationFrameId = null;
        }
        activeScan = null; // Reset scan state
         console.log("Soil type changed. Scan reset.");

    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על GPR' : 'גלו את הסודות: הצגת ההסבר על GPR';
         // Scroll to the explanation section if showing it
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });


    // --- Initial Drawing ---
    drawGround();
    drawObjects();
    drawAntenna(false); // Draw initial antenna not scanning
    drawGraph(new Array(graphDataPoints).fill(0)); // Draw empty graph initially

    // Initial value display for slider
    antennaPosValueSpan.textContent = antennaSlider.value;

</script>
```