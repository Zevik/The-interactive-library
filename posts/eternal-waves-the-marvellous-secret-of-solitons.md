---
title: "גלים נצחיים: סודם המופלא של הסוליטונים"
english_slug: eternal-waves-the-marvellous-secret-of-solitons
category: "פיזיקה"
tags: [סוליטונים, גלים סוליטריים, מכניקת זורמים, גלים לא לינאריים, פיזיקה של מים, KdV]
---
# גלים נצחיים: סודם המופלא של הסוליטונים

דמיינו רגע: גל מים יחיד, מושלם בצורתו, שמתקדם בערוץ בלי לאבד גובה, בלי להתפזר, כאילו הזמן עצר מלכת רק עבורו. נשמע כמו קסם? זוהי המציאות המרתקת של הסוליטונים – גלים סוליטריים (בודדים) בעלי יציבות מדהימה. בואו נצלול יחד אל סודם!

<div class="simulation-container">
    <div class="controls interactive-card">
        <h2><i class="icon-wave"></i> צרו גל וגלו את ההבדל:</h2>
        <div class="control-group wave-type-group">
            <label class="control-label">סוג הגל:</label>
            <div class="radio-options">
                <input type="radio" id="wave-type-regular" name="wave-type" value="regular" checked>
                <label for="wave-type-regular"><i class="icon-regular"></i> גל רגיל</label>
                <input type="radio" id="wave-type-soliton" name="wave-type" value="soliton">
                <label for="wave-type-soliton"><i class="icon-soliton"></i> סוליטון</label>
            </div>
        </div>
        <div class="control-group amplitude-control-group">
            <label for="amplitude" class="control-label">עוצמת הגל (אמפליטודה):</label>
             <div class="slider-with-value">
                <input type="range" id="amplitude" name="amplitude" min="20" max="120" value="60" step="5">
                <span id="amplitude-value">60</span>
            </div>
        </div>
        <div class="button-group">
             <button id="create-wave-btn" class="action-button primary-button"><i class="icon-play"></i> צור גל</button>
             <button id="create-two-solitons-btn" class="action-button secondary-button"><i class="icon-compare"></i> צור שני סוליטונים מתנגשים</button>
        </div>
         <button id="reset-btn" class="action-button tertiary-button"><i class="icon-reset"></i> אפס סימולציה</button>
    </div>
    <div class="canvas-container interactive-canvas">
        <canvas id="wave-canvas"></canvas>
         <div class="canvas-label left-label">נקודת יצירה</div>
         <div class="canvas-label right-label">התקדמות הגל &#8594;</div>
          <div id="wave-count" class="wave-counter">גלים פעילים: 0</div>
    </div>
</div>

<button id="toggle-explanation" class="action-button info-button"><i class="icon-info"></i> הצג/הסתר את הסוד שמאחורי הגלים</button>

<div id="explanation" class="explanation-section hidden">
    <h2><i class="icon-book"></i> הסוד מתגלה: מה הופך סוליטון לנצחי?</h2>

    <h3>הבסיס: מהו בכלל גל?</h3>
    <p>דמיינו זרם אנרגיה שנודד במרחב, מטלטל את מה שבדרכו אך בקושי מזיז אותו ממקומו. זהו גל בפעולה! גל במים גורם למולקולות לעלות ולרדת, בעוד צורת הגל עצמה דוהרת קדימה. לגלים יש תעודת זהות: אורך גל (המרווח בין פסגות), תדירות (כמה פסגות חולפות בשנייה), מהירות, וכמובן – אמפליטודה (גובה השיא או עומק השפל).</p>

    <h3>האתגר: גלים 'רגילים' פשוט נשברים ומתפזרים (דיספרסיה)</h3>
    <p>רוב הגלים בטבע אינם מושלמים. תופעה מציקה בשם **דיספרסיה** גורמת לכך שרכיבי גל שונים (בעיקר החלקים החדים יותר) מתקדמים במהירויות שונות. התוצאה? פולס גל יחיד מתרחב, מתשטש, ולבסוף נעלם. הסימולציה מראה זאת בבירור: גל 'רגיל' שנוצר כפסגה חדה, מאבד את צורתו כשהוא מתקדם. זה כמו ציור עדין שמתפזר באוויר.</p>

    <h3>הגילוי המרעיש: סקוט ראסל והגל המושלם</h3>
    <p>הסיפור מתחיל בקיץ 1834. המהנדס הסקוטי, ג'ון סקוט ראסל, צפה בסירת גרר שעצרה לפתע בערוץ מים צר. לפתע, "גוש מים גדול, עגול, חלק ומוגדר היטב" ניתק מחרטום הסירה והחל להתקדם לבדו! ראסל, מוקסם, רכב אחריו על סוסו לאורך מיילים, ונדהם לראות כיצד הגל שומר על צורתו ומהירותו. הוא כינה אותו "הגל הגדול של התרגום" (The Great Wave of Translation) ותיעודו המדוקדק היה הניצוץ שהצית את המחקר המודרני על הסוליטונים.</p>

    <h3>מאפיינים על-טבעיים של הסוליטון</h3>
    <p>מה מייחד את הסוליטון מגל רגיל?</p>
    <ul>
        <li><i class="icon-check"></i> **נצחי בצורתו:** לא מתפשט, לא נשבר, שומר על צורה קבועה כשהוא דוהר קדימה.</li>
        <li><i class="icon-check"></i> **מהירות קבועה... אבל תלויה באמפליטודה:** בניגוד לגלים לינאריים, סוליטון *גבוה יותר* (אמפליטודה גדולה יותר) מתקדם *מהר יותר* מסוליטון נמוך יותר. זהו רמז לאופי הלא-לינארי של התופעה. הסימולציה של שני סוליטונים מדגימה זאת היטב!</li>
        <li><i class="icon-check"></i> **חוצים זה את זה באלגנטיות:** המאפיין הכי מדהים? כאשר שני סוליטונים נפגשים, הם חולפים זה דרך זה כאילו היו רוחות רפאים! הם עשויים לשנות את צורתם לרגע קצרצר בזמן המפגש, אך מיד לאחר מכן, כל אחד ממשיך בדרכו עם צורתו המקורית ומהירותו הקבועה, כאילו דבר לא קרה (למעט שינוי פאזה קטנטן). הדמיית שני הסוליטונים מאפשרת לצפות בריקוד המופלא הזה.</li>
    </ul>

    <h3>האיזון המושלם: הקסם שמאחורי היציבות</h3>
    <p>סוד כוחו של הסוליטון הוא באיזון פנימי עדין בין שני כוחות מנוגדים הפועלים עליו במקביל במערכות דיספרסיביות ולא-לינאריות:</p>
    <ol>
        <li>**הכוח הלא-לינארי:** במים רדודים, למשל, חלקים גבוהים יותר של גל נוטים להתקדם מהר יותר מחלקים נמוכים יותר. אפקט זה, שנובע מאופי המערכת (עומק המים משתנה תחת הגל), מנסה "לחדד" את הגל, להפוך אותו לתלול יותר, ואף לגרום לו להישבר (כמו גל חוף רגיל).</li>
        <li>**כוח הדיספרסיה:** כפי שראינו, כוח זה מנסה לפזר את הגל, להרחיב אותו ולמרוח את צורתו החדה.</li>
    </ol>
    <p>בסוליטון, שני האפקטים הללו מאזנים זה את זה בדיוק מושלם! הכוח הלא-לינארי שמנסה לחדד מאוזן על ידי הדיספרסיה שמנסה לפזר, והתוצאה היא צורה יציבה שלא משתנה. זהו ריקוד עדין של פיזיקה היוצר ישות יציבה באופן מפתיע.</p>

    <h3>התיאוריה: משוואת KdV האגדית</h3>
    <p>התיאוריה המתמטית המודרנית שמסבירה את הסוליטונים במים רדודים מבוססת על משוואה אלגנטית וחזקה בשם **משוואת קורטווג-דה פריז (KdV)**. משוואה זו, שפותחה בסוף המאה ה-19, היא אחת הדוגמאות הראשונות והמפורסמות ביותר למשוואה דיפרנציאלית חלקית לא-לינארית שיש לה פתרונות יציבים דמויי סוליטון. גילוי זה פתח שער לתחום שלם של מתמטיקה ופיזיקה.</p>

    <h3>מעבר למים: היכן עוד נמצא סוליטונים?</h3>
    <p>הסוליטונים אינם נחלתם הבלעדית של המים. הם מתגלים במגוון עצום של מערכות פיזיקליות שבהן מתקיים האיזון הקסום בין אפקטים לא-לינאריים ודיספרסיביים:</p>
    <ul>
        <li><i class="icon-light"></i> **אופטיקה:** פולסי אור בצורת סוליטונים בסיבים אופטיים הם עמוד התווך של תקשורת הנתונים המודרנית למרחקים ארוכים. הם שומרים על צורתם ואינם דורשים הגברה תדירה.</li>
        <li><i class="icon-atom"></i> **פיזיקה גרעינית וחלקיקים:** מופיעים במודלים תאורטיים.</li>
        <li><i class="icon-crystal"></i> **פיזיקת מצב מוצק:** בתנודות אטומיות בסריגים גבישיים.</li>
         <li><i class="icon-bio"></i> **ביולוגיה:** תיאוריות חדשניות מציעות תפקיד אפשרי שלהם בהעברת אותות לאורך ממברנות תאים.</li>
    </ul>
    <p>היכולת שלהם להעביר אנרגיה או מידע בצורה יציבה להפליא הופכת אותם לתופעה בעלת חשיבות עמוקה ומגוונת במדע ובטכנולוגיה.</p>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #6c757d; /* Gray */
        --tertiary-color: #dc3545; /* Red/Reset */
        --info-button-color: #17a2b8; /* Cyan */
        --water-blue: #87CEEB; /* SkyBlue */
        --darker-water-blue: #4682B4; /* SteelBlue */
        --wave-line-color: #00008B; /* DarkBlue */
        --control-bg: #f8f9fa; /* Light background */
        --card-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --border-radius: 8px;
        --padding-medium: 15px;
        --padding-large: 20px;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #343a40;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    h1 {
        text-align: center;
        color: var(--darker-water-blue);
        margin-bottom: 30px;
    }

    p {
        margin-bottom: 15px;
    }

    /* Icons - Placeholder for actual icon implementation */
    .icon-wave::before, .icon-regular::before, .icon-soliton::before,
    .icon-play::before, .icon-compare::before, .icon-reset::before,
    .icon-info::before, .icon-book::before, .icon-check::before,
    .icon-light::before, .icon-atom::before, .icon-crystal::before, .icon-bio::before {
        content: '\2022'; /* Simple bullet as placeholder */
        margin-right: 5px;
        font-weight: bold;
        color: var(--primary-color);
    }
     .icon-play::before { content: '\25B6'; } /* Play arrow */
     .icon-compare::before { content: '\26F2'; } /* Sailboat - abstraction for collision */
     .icon-reset::before { content: '\21BB'; } /* Circled Arrows */
     .icon-info::before { content: '\2139'; } /* Information icon */
     .icon-check::before { content: '\2713'; color: green;} /* Checkmark */
     .icon-wave::before { content: '\FF5E'; } /* Tilde - stylized wave */
     .icon-soliton::before { content: '\25B2'; color: var(--darker-water-blue); } /* Up triangle */
     .icon-regular::before { content: '\25B3'; color: var(--secondary-color); } /* Up triangle outlined */


    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
        margin-bottom: 30px;
        padding: var(--padding-medium);
        background-color: #e9ecef; /* Light gray background for section */
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
    }

    .controls {
        background-color: var(--control-bg);
        padding: var(--padding-medium);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        text-align: center;
        width: 100%;
        max-width: 400px; /* Control panel width */
    }

    .controls h2 {
        margin-top: 0;
        color: var(--darker-water-blue);
        border-bottom: 1px solid #dee2e6;
        padding-bottom: 10px;
        margin-bottom: var(--padding-medium);
    }

    .control-group {
        margin-bottom: var(--padding-medium);
        padding: 10px;
        background-color: #f0f3f5;
        border-radius: 5px;
        border: 1px solid #e2e6ea;
    }

    .control-label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
        text-align: right;
    }

    .radio-options label {
        margin: 0 10px;
        cursor: pointer;
        font-size: 1.1rem;
    }

     .radio-options input[type="radio"] {
         margin-left: 5px;
     }

    .slider-with-value {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .slider-with-value input[type="range"] {
        flex-grow: 1;
        -webkit-appearance: none; /* Override default CSS styles */
        appearance: none;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .slider-with-value input[type="range"]:hover {
        opacity: 1;
    }

    .slider-with-value input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

     .slider-with-value input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .slider-with-value span {
        font-weight: bold;
        color: var(--darker-water-blue);
        min-width: 25px; /* Prevent text jump */
        text-align: left;
    }

    .button-group {
        margin-bottom: 10px;
    }

    .action-button {
        padding: 10px 20px;
        margin: 5px;
        color: white;
        border: none;
        border-radius: var(--border-radius);
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.1s ease;
        min-width: 150px; /* Ensure buttons have minimum width */
        text-align: center;
        display: inline-flex; /* Align icon and text */
        align-items: center;
        justify-content: center;
        gap: 8px;
    }

    .action-button:hover {
        opacity: 0.9;
    }

    .action-button:active {
        transform: scale(0.98);
    }

    .primary-button {
        background-color: var(--primary-color);
    }

    .primary-button:hover {
         background-color: #0056b3;
    }

    .secondary-button {
        background-color: var(--secondary-color);
    }
    .secondary-button:hover {
        background-color: #5a6268;
    }


    .tertiary-button {
         background-color: var(--tertiary-color);
    }
     .tertiary-button:hover {
        background-color: #c82333;
    }

    .info-button {
         background-color: var(--info-button-color);
         display: block; /* Center button below simulation */
         margin: 20px auto;
    }
     .info-button:hover {
        background-color: #138496;
    }


    .canvas-container {
        width: 100%;
        max-width: 800px; /* Limit canvas width */
        border: 2px solid var(--darker-water-blue);
        border-radius: var(--border-radius);
        overflow: hidden; /* Ensure nothing draws outside */
        position: relative; /* For absolute positioning of labels */
        background: linear-gradient(to bottom, #e0f7ff, var(--water-blue)); /* Gradient water background */
        box-shadow: inset 0 0 15px rgba(0, 0, 139, 0.3); /* Inner shadow for depth */
    }

    #wave-canvas {
        display: block;
        width: 100%;
        height: 250px; /* Increased canvas height for better visualization */
        background-color: transparent; /* Let the container gradient show through */
    }

     .canvas-label {
        position: absolute;
        bottom: 10px;
        font-size: 0.9rem;
        color: rgba(0, 0, 0, 0.6);
        z-index: 1; /* Above canvas */
     }
     .left-label { left: 10px; }
     .right-label { right: 10px; }

    .wave-counter {
        position: absolute;
        top: 10px;
        left: 10px;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.9rem;
        color: #333;
         z-index: 1;
    }


    .explanation-section {
        margin-top: 30px;
        padding: var(--padding-large);
        background-color: #ffffff; /* White background for explanation */
        border: 1px solid #dee2e6;
        border-radius: var(--border-radius);
        text-align: justify;
        box-shadow: var(--card-shadow);
         opacity: 1; /* Default state for transition */
         transition: opacity 0.5s ease, transform 0.5s ease;
         transform: translateY(0); /* Default state */
    }

    .explanation-section.hidden {
         display: none; /* Use display:none for initial state */
         opacity: 0;
         transform: translateY(20px); /* Start slightly lower */
    }


    .explanation-section h2, .explanation-section h3 {
        color: var(--darker-water-blue);
        border-bottom: 1px dashed #adb5bd;
        padding-bottom: 5px;
    }

    .explanation-section ul {
        list-style: none; /* Remove default list style */
        padding: 0;
        margin-left: 10px; /* Indent slightly */
    }

     .explanation-section ul li {
        margin-bottom: 10px;
        position: relative;
        padding-right: 20px; /* Space for potential icon */
     }
      .explanation-section ul li i {
          position: absolute;
          right: 0;
          top: 3px;
      }

     .explanation-section ol {
        margin-left: 20px;
     }

    .explanation-section ol li {
        margin-bottom: 10px;
    }

    /* Responsive adjustments */
    @media (min-width: 768px) {
        .simulation-container {
            flex-direction: row;
            align-items: flex-start; /* Align items to the top */
        }

        .controls {
             flex-shrink: 0; /* Prevent controls from shrinking */
            width: 300px; /* Fixed width for controls on wider screens */
             max-width: none; /* Remove max-width */
        }

        .canvas-container {
             flex-grow: 1; /* Canvas takes remaining space */
             max-width: none; /* Remove max-width */
        }
         .button-group {
             display: flex;
             flex-direction: column;
         }
          .button-group button {
             width: 100%;
             margin: 5px 0;
          }
           .action-button.tertiary-button {
             width: 100%;
             margin: 5px 0;
           }
    }

</style>

<script>
    const canvas = document.getElementById('wave-canvas');
    const ctx = canvas.getContext('2d');
    const createWaveBtn = document.getElementById('create-wave-btn');
    const createTwoSolitonsBtn = document.getElementById('create-two-solitons-btn');
    const resetBtn = document.getElementById('reset-btn');
    const waveTypeRadios = document.getElementsByName('wave-type');
    const amplitudeInput = document.getElementById('amplitude');
    const amplitudeValueSpan = document.getElementById('amplitude-value');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const waveCounterSpan = document.getElementById('wave-count');


    let animationFrameId = null;
    let waves = []; // Array to hold active waves/solitons

    // Simulation parameters
    const CANVAS_HEIGHT = 250; // Increased height
    const WATER_LEVEL = CANVAS_HEIGHT * 0.8; // Base water level - lower base for more wave room
    const CHANNEL_LENGTH = 800; // Corresponds to canvas width
    const DT = 0.8; // Time step (arbitrary units for visual simulation) - Adjusted for smoother animation
    const SPREADING_RATE = 0.00005; // Rate for regular wave diffusion - Reduced
    const DAMPING_RATE = 0.00002; // Rate for regular wave damping - Reduced
    const SOLITON_BASE_SPEED = 0.08; // Base speed multiplier for solitons - Slightly faster
    const REGULAR_WAVE_SPEED = SOLITON_BASE_SPEED * 0.4; // Regular waves move slower
    const SOLITON_WIDTH_SCALE = 0.003; // Controls soliton width relative to amplitude

    canvas.height = CANVAS_HEIGHT;
    canvas.width = CHANNEL_LENGTH;

    // Function to draw the simulation state
    function drawSimulation() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw static water body with gradient (container background handles this now, but can add depth here)
        // ctx.fillStyle = 'var(--water-blue)';
        // ctx.fillRect(0, WATER_LEVEL, canvas.width, canvas.height - WATER_LEVEL);

        ctx.beginPath();
        ctx.moveTo(0, WATER_LEVEL);

        // Draw the dynamic wave surface
        for (let i = 0; i < CHANNEL_LENGTH; i++) {
            let totalHeightOffset = 0;
            waves.forEach(wave => {
                if (wave.active) {
                     const wavePos = i - wave.position; // Position relative to wave center

                     if (wave.type === 'soliton') {
                         // Sech^2 shape for soliton
                         // Scale factor based on amplitude for narrower, taller peaks
                         const scale = SOLITON_WIDTH_SCALE * wave.amplitude; // Higher amp = larger scale = narrower peak
                         totalHeightOffset += wave.amplitude * Math.pow(Math.cosh(wavePos * scale), -2);
                     } else {
                         // Spreading Gaussian pulse for regular wave
                         const peakWidth = 30; // Initial width
                         // Spreading and damping over age (time)
                         const spreadFactor = 1 + wave.age * SPREADING_RATE * wave.initialAmplitude/50; // Spread depends on initial amplitude
                         const dampedAmplitude = wave.initialAmplitude * Math.exp(-wave.age * DAMPING_RATE);
                         totalHeightOffset += dampedAmplitude * Math.exp(-Math.pow(wavePos / (peakWidth * spreadFactor), 2));

                         // Fade out if amplitude is very low
                         if (dampedAmplitude < 1) wave.active = false;
                     }
                }
            });
            ctx.lineTo(i, WATER_LEVEL - totalHeightOffset);
        }

        ctx.lineTo(CHANNEL_LENGTH, WATER_LEVEL); // Close the shape
        ctx.strokeStyle = var_to_hex('--wave-line-color'); // Darker blue for the wave line
        ctx.lineWidth = 2;
        ctx.stroke();

        // Optional: Draw base line to separate from water fill if container background is used
        ctx.beginPath();
        ctx.moveTo(0, WATER_LEVEL);
        ctx.lineTo(CHANNEL_LENGTH, WATER_LEVEL);
        ctx.strokeStyle = 'rgba(0,0,0,0.1)'; // Subtle line
        ctx.lineWidth = 1;
        ctx.stroke();


         // Draw wave peaks/markers for better visualization (optional)
         // waves.forEach(wave => {
         //      if (wave.active) {
         //          const peakX = wave.position;
         //          const peakY = WATER_LEVEL - wave.amplitude; // Approx peak height
         //          if (peakX >= 0 && peakX <= CHANNEL_LENGTH) {
         //              ctx.fillStyle = wave.type === 'soliton' ? var_to_hex('--darker-water-blue') : var_to_hex('--secondary-color');
         //              ctx.beginPath();
         //              ctx.arc(peakX, peakY, 5, 0, Math.PI * 2); // Draw a circle at the peak
         //              ctx.fill();
         //          }
         //      }
         //  });

        // Update wave counter
        waveCounterSpan.textContent = `גלים פעילים: ${waves.length}`;
    }

     // Helper to get CSS variable color
     function var_to_hex(variable) {
         return getComputedStyle(document.documentElement).getPropertyValue(variable).trim();
     }


     // Function to update wave positions and properties
    function updateWaves() {
        const now = Date.now();
        waves.forEach(wave => {
            if (wave.active) {
                 // Calculate elapsed time since creation
                 const elapsedTime = (now - wave.startTime) / 1000; // time in seconds
                 wave.age = elapsedTime; // Use actual time for age

                if (wave.type === 'soliton') {
                    // Soliton speed depends on amplitude (simplified KdV-like)
                    // Speed is proportional to amplitude (or sqrt(amp), let's use linear for simplicity)
                    // v = v0 * (1 + c * A)
                    const speed = SOLITON_BASE_SPEED * (1 + wave.amplitude / 80); // Adjusted factor for speed range
                    wave.position += speed * DT;
                } else {
                    // Regular wave moves at a constant speed (slower)
                    wave.position += REGULAR_WAVE_SPEED * DT;
                }

                // Deactivate wave if it goes off screen significantly
                if (wave.position > CHANNEL_LENGTH + 100 || wave.position < -100) {
                    wave.active = false;
                }
            }
        });

        // Filter out inactive waves
        waves = waves.filter(wave => wave.active);
    }

    // Main animation loop
    function animate() {
        updateWaves();
        drawSimulation();
        animationFrameId = requestAnimationFrame(animate);

         // Stop animation if no waves are active
         if (waves.length === 0 && animationFrameId !== null) {
             stopAnimation();
              drawSimulation(); // Final draw to clear canvas fully if needed (though filter+clearRect does this)
         }
    }

    // Stop animation
    function stopAnimation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
    }

    // Reset simulation
    function resetSimulation() {
        stopAnimation();
        waves = [];
        drawSimulation(); // Draw initial flat water
         waveCounterSpan.textContent = `גלים פעילים: 0`;
    }

    // Create a new wave pulse
    function createWave(type, amplitude, startPosition = 50) {
        const now = Date.now();
        // Ensure amplitude is within a reasonable range relative to canvas height
        const clampedAmplitude = Math.max(20, Math.min(amplitude, WATER_LEVEL * 0.8)); // Max amplitude is 80% of water depth

        waves.push({
            type: type,
            amplitude: clampedAmplitude,
            initialAmplitude: clampedAmplitude, // Store initial amp for regular wave spreading
            position: startPosition, // Starting position of the wave center
            active: true,
            startTime: now,
            age: 0 // Simulation age in seconds
        });

         // Start animation only if not already running
         if (animationFrameId === null) {
             animate();
         }
    }

    // Event Listeners
    createWaveBtn.addEventListener('click', () => {
        const selectedType = document.querySelector('input[name="wave-type"]:checked').value;
        const amplitude = parseInt(amplitudeInput.value);
        createWave(selectedType, amplitude);
    });

    createTwoSolitonsBtn.addEventListener('click', () => {
         resetSimulation(); // Clear existing waves

         // Create first (smaller) soliton - starts ahead, moves slower
         createWave('soliton', 60, 200);

         // Create second (larger) soliton that will catch up - starts behind, moves faster
         createWave('soliton', 90, 50);

         // Animation starts automatically when waves are added
    });

    resetBtn.addEventListener('click', resetSimulation);

    amplitudeInput.addEventListener('input', (event) => {
        amplitudeValueSpan.textContent = event.target.value;
    });

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('hidden');
        if (isHidden) {
            explanationDiv.classList.remove('hidden');
            // Trigger reflow to restart transition
            void explanationDiv.offsetWidth;
             explanationDiv.style.opacity = 1;
             explanationDiv.style.transform = 'translateY(0)';

            toggleExplanationBtn.innerHTML = '<i class="icon-info"></i> הסתר הסבר';
        } else {
            explanationDiv.style.opacity = 0;
            explanationDiv.style.transform = 'translateY(20px)';
            // Use transitionend to set display: none AFTER the animation
            explanationDiv.addEventListener('transitionend', function handler() {
                explanationDiv.classList.add('hidden');
                 toggleExplanationBtn.innerHTML = '<i class="icon-info"></i> הצג/הסתר את הסוד שמאחורי הגלים';
                explanationDiv.removeEventListener('transitionend', handler);
            });

        }
    });

    // Initial drawing
    drawSimulation();

</script>
```