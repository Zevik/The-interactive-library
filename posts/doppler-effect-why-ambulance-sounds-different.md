---
title: "אפקט דופלר: הצליל שמשתנה עם התנועה"
english_slug: doppler-effect-why-ambulance-sounds-different
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה
  - גלים
  - קול
  - תנועה יחסית
  - תדר
---
# אפקט דופלר: הצליל שמשתנה עם התנועה

שמעתם פעם צפירת אמבולנס שמתקרב אליכם במהירות, חולף על פניכם ומתרחק? אם כן, בטח שמתם לב שהצליל שלה משתנה באופן מדהים: גבוה יותר כשהאמבולנס מתקרב, ופתאום נופל ונשמע נמוך יותר כשהוא מתרחק. התופעה המרתקת הזו, שבה התדר הנקלט של גל משתנה כתוצאה מתנועה יחסית בין המקור שפולט את הגל לבין הצופה שקולט אותו, נקראת **אפקט דופלר**. היא לא קורית רק עם צליל - היא משפיעה גם על אור וסוגי גלים אחרים, ויש לה שימושים מפתיעים, מרדאר ועד אסטרונומיה!

בואו נחקור יחד את אפקט דופלר באמצעות סימולציה אינטראקטיבית. תוכלו לשלוט בתנועה של המקור (כמו האמבולנס) ושל הצופה (כמו אתם שעומדים על המדרכה) ולראות כיצד זה משפיע על הגלים ועל התדר שנקלט.

<div id="app-container">
    <canvas id="dopplerCanvas" width="700" height="450"></canvas>
    <div class="controls">
        <div class="control-group">
            <h3>מקור (Source)</h3>
            <label for="sourceSpeed">מהירות:</label>
            <input type="range" id="sourceSpeed" min="0" max="100" value="0">
            <span id="sourceSpeedValue" class="speed-value">0</span>
            <div class="direction-buttons">
                <button data-role="source" data-direction="up" aria-label="Up">▲</button>
                <button data-role="source" data-direction="left" aria-label="Left">◀</button>
                <button data-role="source" data-direction="stop" aria-label="Stop">■</button>
                <button data-role="source" data-direction="right" aria-label="Right">▶</button>
                <button data-role="source" data-direction="down" aria-label="Down">▼</button>
            </div>
             <p class="freq-display">תדר מקור: <span id="sourceFreqDisplay"></span> Hz</p>
        </div>
        <div class="control-group">
            <h3>צופה (Observer)</h3>
            <label for="observerSpeed">מהירות:</label>
            <input type="range" id="observerSpeed" min="0" max="100" value="0">
            <span id="observerSpeedValue" class="speed-value">0</span>
             <div class="direction-buttons">
                <button data-role="observer" data-direction="up" aria-label="Up">▲</button>
                <button data-role="observer" data-direction="left" aria-label="Left">◀</button>
                <button data-role="observer" data-direction="stop" aria-label="Stop">■</button>
                <button data-role="observer" data-direction="right" aria-label="Right">▶</button>
                <button data-role="observer" data-direction="down" aria-label="Down">▼</button>
            </div>
             <p class="freq-display">תדר נקלט: <span id="perceivedFreqDisplay"></span> Hz</p>
        </div>
         <div class="control-group simulation-controls">
            <h3>שליטה בסימולציה</h3>
            <button id="startButton">התחלה/השהייה</button>
            <button id="resetButton">איפוס</button>
        </div>
    </div>
</div>

<style>
    #app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
        margin-bottom: 40px;
        padding: 30px;
        background-color: #f0f4f8; /* Light blue-grey background */
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    canvas {
        display: block;
        margin: 0 auto;
        background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* Gradient sky background */
        border: 2px solid #00bcd4; /* Teal border */
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,188,212,0.2);
    }
    .controls {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 25px;
        width: 100%;
        max-width: 800px;
    }
    .control-group {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        flex-grow: 1;
        min-width: 250px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
     .control-group.simulation-controls {
         justify-content: center;
     }
    .controls h3 {
        margin-top: 0;
        color: #00796b; /* Dark cyan */
        margin-bottom: 15px;
    }
    .controls label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
        width: 100%; /* Make label take full width */
        text-align: left; /* Align label left */
    }
    .controls input[type="range"] {
        width: calc(100% - 50px); /* Adjust width for value span */
        vertical-align: middle;
        -webkit-appearance: none; /* Remove default style */
        appearance: none;
        height: 8px;
        background: #b2ebf2; /* Light teal */
        outline: none;
        opacity: 0.9;
        transition: opacity .2s;
        border-radius: 5px;
    }
     .controls input[type="range"]:hover {
         opacity: 1;
     }
     .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #00796b; /* Dark cyan */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }
     .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #00796b; /* Dark cyan */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }

     .speed-value {
         vertical-align: middle;
         display: inline-block;
         width: 40px; /* Fixed width */
         text-align: right;
         font-weight: bold;
         color: #00796b;
     }
    .direction-buttons {
        display: grid;
        grid-template-areas: ". up ." "left stop right" ". down .";
        gap: 6px;
        margin-top: 15px;
        width: 120px; /* Wider grid */
        margin-left: auto;
        margin-right: auto;
    }
    .direction-buttons button {
        padding: 8px; /* More padding */
        font-size: 1.1em;
        background-color: #00bcd4; /* Teal */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
     .direction-buttons button:hover {
         background-color: #0097a7; /* Darker teal */
         transform: translateY(-1px);
     }
     .direction-buttons button:active {
         transform: translateY(1px);
         box-shadow: 0 1px 2px rgba(0,0,0,0.2);
     }
    .direction-buttons button[data-direction="up"] { grid-area: up; }
    .direction-buttons button[data-direction="left"] { grid-area: left; }
    .direction-buttons button[data-direction="stop"] { grid-area: stop; background-color: #e57373; /* Light red */ }
    .direction-buttons button[data-direction="stop"]:hover { background-color: #ef5350; /* Red */ }
    .direction-buttons button.active {
        background-color: #004d40; /* Darker green/teal for active state */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.3);
    }

    button#startButton, button#resetButton {
        padding: 12px 25px;
        font-size: 1.1em;
        margin: 0 5px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    button#startButton {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    button#startButton:hover {
        background-color: #388E3C; /* Darker green */
        transform: translateY(-1px);
    }
     button#resetButton {
        background-color: #ffb74d; /* Orange */
        color: #333;
     }
     button#resetButton:hover {
        background-color: #ffa726; /* Darker orange */
        transform: translateY(-1px);
     }
     button#startButton:active, button#resetButton:active {
        transform: translateY(1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }

     .freq-display {
         margin-top: 15px;
         font-size: 1em;
         color: #00796b;
         font-weight: bold;
     }
     .freq-display span {
         color: #d32f2f; /* Red for emphasis */
     }

    #explanationButton {
        display: block;
        margin: 30px auto;
        padding: 15px 30px;
        font-size: 1.2em;
        background-color: #1976d2; /* Blue */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    #explanationButton:hover {
        background-color: #1565c0; /* Darker blue */
        transform: translateY(-1px);
    }
     #explanationButton:active {
         transform: translateY(1px);
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }

    #explanation {
        display: none; /* Initially hidden */
        margin-top: 30px;
        padding: 25px;
        background-color: #e3f2fd; /* Lightest blue */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        line-height: 1.6;
        color: #333;
    }
     #explanation h2, #explanation h3 {
         color: #0277bd; /* Deep blue */
         margin-bottom: 15px;
         padding-bottom: 5px;
         border-bottom: 1px solid #b3e5fc; /* Lighter blue border */
     }
     #explanation p, #explanation ul {
         margin-bottom: 15px;
     }
     #explanation ul {
         padding-left: 20px;
     }
     #explanation li {
         margin-bottom: 8px;
     }

    /* Canvas Labels - Positioned via JS for flexibility */
     .canvas-label {
         position: absolute;
         font-weight: bold;
         color: #333;
         text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
     }

     .source-label { color: #d32f2f; /* Red */ }
     .observer-label { color: #1976d2; /* Blue */ }

</style>

<button id="explanationButton">קראו עוד: ההסבר המלא מאחורי אפקט דופלר</button>

<div id="explanation">
    <h2>מהו אפקט דופלר?</h2>
    <p>אפקט דופלר הוא תופעה פיזיקלית קסומה שגורמת לנו לשמוע, לראות או לחוש גלים (כמו קול או אור) בתדר שונה מהתדר שבו הם נפלטים. זה קורה בכל פעם שיש תנועה יחסית בין המקור שפולט את הגל לבין הצופה שקולט אותו. דמיינו זאת: כשהמקור והצופה "רודפים" זה אחרי זה (מתקרבים), הגלים "נדחסים" והתדר הנקלט עולה. כשהם "בורחים" זה מזה (מתרחקים), הגלים "מתרחבים" והתדר הנקלט יורד. בואו נצלול קצת יותר לעומק.</p>

    <h2>כיצד תנועה משפיעה על גלים?</h2>
    <p>כל גל מתאפיין בשלושה דברים עיקריים: <strong>אורך גל</strong> (המרחק בין שתי "פסגות" רצופות), <strong>תדר</strong> (כמה פסגות כאלה עוברות נקודה מסוימת בשנייה), ו<strong>מהירות התקדמות</strong> (כמה מהר הגל נע במדיום, למשל באוויר עבור קול, או בריק עבור אור). מהירות הגל בדרך כלל קבועה עבור מדיום נתון. הנוסחה שמקשרת ביניהם היא פשוטה ואלגנטית: מהירות = תדר × אורך גל.</p>
    <p>כאשר מקור גלים נייח, הוא פולט גלים במרווחים קבועים וזהים בכל הכיוונים. התוצאה היא גלים עגולים (או כדוריים) מושלמים שמרכזם במקור, ואורך הגל זהה לכל צופה. אבל מה קורה כשהמקור מתחיל לזוז? נניח שהוא פולט פסגת גל, ומיד מתחיל לנוע. כשהוא מגיע לנקודה חדשה כדי לפלוט את הפסגה הבאה, הפסגה הקודמת כבר התקדמה קצת. בכיוון שאליו המקור נע, הפסגות "נדחסות" יחד כי המקור "משיג" אותן מעט. בכיוון ההפוך, הפסגות "מתרחבות" כי המקור "בורח" מהן. הצופה שרואה גלים דחוסים (אורך גל קצר יותר) יקלוט תדר גבוה יותר, ואילו הצופה שרואה גלים מורחבים (אורך גל ארוך יותר) יקלוט תדר נמוך יותר. הסימולציה שלנו מציגה בדיוק את האפקט הויזואלי הזה של דחיסה והתרחבות הגלים!</p>

    <h2>אפקט דופלר בגלי קול: שינוי בגובה הצליל!</h2>
    <p>הדוגמה הכי מוכרת לאפקט דופלר היא עם גלי קול. בגלי קול, התדר הוא שקובע את גובה הצליל: תדר גבוה נשמע כצליל "דק" או גבוה, ותדר נמוך נשמע כצליל "עבה" או נמוך. לכן, כאשר מקור קול (כמו אמבולנס) נע, גובה הצליל שלו נשמע שונה לצופה נייח, בהתאם לכיוון התנועה. אבל לא רק תנועת המקור משנה את התדר הנקלט! גם תנועת הצופה ביחס למקור (נייח או נע) תשנה את התדר שהוא קולט.</p>

    <h2>המקרה הקלאסי: מקור נע וצופה נייח.</h2>
    <p>זה המצב שבו אתם עומדים על המדרכה והאמבולנס חולף. כשהאמבולנס מתקרב, הוא נע לכיוונכם. הגלים "נדחסים" בדרכם אליכם, אורך הגל קצר יותר, ולכן התדר הנקלט (וגובה הצליל) גבוה יותר מהתדר המקורי של הצפירה. ברגע שהאמבולנס חולף ומתרחק, הוא נע בכיוון ההפוך. הגלים "מתרחבים", אורך הגל ארוך יותר, והתדר הנקלט (וגובה הצליל) נמוך יותר. בדקו זאת בסימולציה!</p>

    <h2>המקרה הפחות אינטואיטיבי: צופה נע ומקור נייח.</h2>
    <p>מה קורה אם המקור עומד במקום ואתם נעים? למשל, אתם רצים לכיוון פעמון כנסייה שצלצולו קבוע. בזמן שאתם רצים לכיוון המקור הנייח, אתם "פוגשים" יותר גלי קול בשנייה אחת מאשר אם הייתם עומדים במקום. קצב קליטת הגלים עולה, ולכן התדר הנקלט גבוה יותר. אם תרוצו הרחק מהפעמון, תפגשו פחות גלים בשנייה, והתדר הנקלט יהיה נמוך יותר. שימו לב שבמקרה זה, אורך הגל במדיום (האוויר) לא משתנה, אבל הצופה נע בתוך המדיום ומשפיע על הקצב שבו הוא "פוגש" את הפסגות.</p>

    <h2>המקרה הכללי: גם המקור וגם הצופה נעים.</h2>
    <p>כאשר גם המקור וגם הצופה בתנועה, אפקט דופלר מורכב יותר. התדר הנקלט תלוי לא רק במהירות של כל אחד בנפרד, אלא בעיקר במהירות היחסית *ביניהם* לאורך הקו שמחבר אותם. אם המרחק ביניהם קטן לאורך הקו (מתקרבים), התדר עולה. אם המרחק ביניהם גדל לאורך הקו (מתרחקים), התדר יורד. הנוסחה הכללית מתחשבת במהירות הגל במדיום, במהירות הצופה יחסית למדיום (חיובי אם לכיוון המקור, שלילי אם הרחק ממנו), ובמהירות המקור יחסית למדיום (חיובי אם לכיוון הצופה, שלילי אם הרחק ממנו). הסימולציה שלנו מאפשרת לחקור גם את המצב המלא הזה!</p>

    <h2>מעבר לצליל: שימושים מפתיעים של אפקט דופלר</h2>
    <p>אפקט דופלר הוא כלי רב עוצמה בפיזיקה ובהנדסה, עם שימושים רבים מעבר לצפירות אמבולנס:
    <ul>
        <li>**רדאר מהירות:** משטרת התנועה משתמשת באפקט דופלר של גלי רדיו כדי למדוד את מהירות כלי הרכב. מכשיר הרדאר שולח גל רדיו, והגל שמוחזר מהמכונית הנעה מגיע בתדר שונה. גודל השינוי בתדר מעיד על מהירות הרכב.</li>
        <li>**אסטרונומיה:** אסטרונומים משתמשים באפקט דופלר של גלי אור כדי ללמוד על תנועת כוכבים וגלקסיות. כוכבים שמתרחקים מאיתנו מראים "הסטה לאדום" (התדר הנקלט נמוך יותר, לכיוון קצה הספקטרום האדום), ואלה שמתקרבים מראים "הסטה לכחול". מדידות אלה הן עדות מפתח לכך שהיקום מתרחב!</li>
        <li>**אולטרסאונד רפואי:** בבדיקות אולטרסאונד, אפקט דופלר משמש להדמיית ומדידת זרימת דם בגוף. גלי קול נשלחים לעבר כלי דם, וגלי הקול המוחזרים מתאי הדם הנעים מציגים שינוי תדר המאפשר לחשב את מהירות וכיוון הזרימה, וליצור הדמיה צבעונית של הזרימה.</li>
         <li>**חיזוי מזג אוויר (רדאר דופלר):** מאפשר למדוד את מהירות תנועת הגשם וחלקיקים אחרים באטמוספירה, מה שעוזר לחזות סופות ומערכות מזג אוויר.</li>
    </ul>
    </p>
    <p>כפי שאתם רואים, אפקט דופלר הוא לא רק תופעה אקוסטית מוזרה, אלא עיקרון פיזיקלי יסודי עם השפעה רחבה על הבנת העולם סביבנו, מהכביש הקרוב ועד קצוות היקום!</p>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('dopplerCanvas');
    const ctx = canvas.getContext('2d');
    const sourceSpeedInput = document.getElementById('sourceSpeed');
    const sourceSpeedValueSpan = document.getElementById('sourceSpeedValue');
    const observerSpeedInput = document.getElementById('observerSpeed');
    const observerSpeedValueSpan = document.getElementById('observerSpeedValue');
    const directionButtons = document.querySelectorAll('.direction-buttons button');
    const startButton = document.getElementById('startButton');
    const resetButton = document.getElementById('resetButton');
    const explanationButton = document.getElementById('explanationButton');
    const explanationDiv = document.getElementById('explanation');
    const perceivedFreqDisplay = document.getElementById('perceivedFreqDisplay');
    const sourceFreqDisplay = document.getElementById('sourceFreqDisplay');

    const canvasContainer = canvas.parentElement; // Get parent for potential labels

    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;

    let animationFrameId = null;
    let isRunning = true;

    // Simulation parameters
    const waveSpeed = 4; // pixels per frame - Slower for better visual
    const sourceFrequency = 0.15; // waves per frame (Lower frequency means larger interval, easier to see waves)
    const waveEmitInterval = 1 / sourceFrequency; // frames between wave emissions
    const maxWaveRadius = Math.max(canvasWidth, canvasHeight) * 1.2; // waves disappear after reaching this size
    const maxSimSpeed = 3; // Maximum speed in pixels/frame corresponding to slider value 100

    // Objects (Source and Observer)
    const source = {
        x: canvasWidth * 0.2,
        y: canvasHeight / 2,
        vx: 0,
        vy: 0,
        radius: 12, // Slightly larger
        color: '#d32f2f', // Red
        speed: 0, // Speed from slider (0-100)
        direction: 'stop' // 'up', 'down', 'left', 'right', 'stop'
    };

    const observer = {
        x: canvasWidth * 0.8,
        y: canvasHeight / 2,
        vx: 0,
        vy: 0,
        radius: 12, // Slightly larger
        color: '#1976d2', // Blue
        speed: 0, // Speed from slider (0-100)
        direction: 'stop'
    };

    let waveFronts = []; // Stores { x, y, creationFrame }
    let frameCount = 0;
    let lastWaveEmissionFrame = -waveEmitInterval; // Ensure a wave is emitted on the first frame

     // Canvas labels (managed via JS)
    let sourceLabel = document.createElement('div');
    sourceLabel.classList.add('canvas-label', 'source-label');
    sourceLabel.textContent = 'מקור';
    sourceLabel.style.position = 'absolute'; // Ensure absolute positioning relative to container
    canvasContainer.style.position = 'relative'; // Make container position relative
    canvasContainer.appendChild(sourceLabel);

    let observerLabel = document.createElement('div');
    observerLabel.classList.add('canvas-label', 'observer-label');
    observerLabel.textContent = 'צופה';
    observerLabel.style.position = 'absolute';
    canvasContainer.appendChild(observerLabel);


    // Function to calculate perceived frequency
    function calculatePerceivedFrequency() {
        // Use a small epsilon to avoid division by zero or near zero when objects are too close
        const epsilon = 10;
        const dx = source.x - observer.x;
        const dy = source.y - observer.y;
        const distanceSq = dx * dx + dy * dy;

        if (distanceSq < epsilon * epsilon) {
            return "קרוב מדי";
        }

        const distance = Math.sqrt(distanceSq);

        // Unit vector from Observer to Source
        const ux_os = dx / distance;
        const uy_os = dy / distance;

        // Observer velocity component towards Source
        const vo_radial = observer.vx * ux_os + observer.vy * uy_os;

        // Source velocity component towards Observer
        const vs_radial = source.vx * (-ux_os) + source.vy * (-uy_os); // Note the negative sign for towards observer

        // Doppler formula: f' = f * (v + v_o) / (v - v_s)
        // v_o is observer speed TOWARDS source
        // v_s is source speed TOWARDS observer
        // We calculated vo_radial (observer towards source) and vs_radial (source towards observer)

        const denominator = waveSpeed - vs_radial;

        if (denominator <= 0.1) { // Check if source is moving at or faster than wave speed towards observer (allow small margin)
             return "בום על-קולי!";
        }

        const perceivedFreq = sourceFrequency * (waveSpeed + vo_radial) / denominator;

        // Clamp to a reasonable range and format
        if (perceivedFreq > 0 && perceivedFreq < sourceFrequency * 50) { // Avoid extreme values
             return perceivedFreq.toFixed(2);
        } else if (perceivedFreq >= sourceFrequency * 50) {
             return "> " + (sourceFrequency * 50).toFixed(2);
        }
        return "N/A";
    }

    // Drawing function
    function draw() {
        // Clear canvas
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Draw wave fronts with fading effect
        waveFronts.forEach(wave => {
            const radius = waveSpeed * (frameCount - wave.creationFrame);
            const opacity = 1 - (radius / maxWaveRadius); // Fade out as waves expand

            if (radius > 0 && opacity > 0) {
                ctx.strokeStyle = `rgba(0, 123, 255, ${opacity * 0.6})`; // Blue waves with transparency
                ctx.lineWidth = 2; // Thicker waves
                ctx.beginPath();
                ctx.arc(wave.x, wave.y, radius, 0, Math.PI * 2);
                ctx.stroke();
            }
        });

         // Filter out old wave fronts
         waveFronts = waveFronts.filter(wave => waveSpeed * (frameCount - wave.creationFrame) < maxWaveRadius);


        // Draw source
        ctx.fillStyle = source.color;
        ctx.beginPath();
        ctx.arc(source.x, source.y, source.radius, 0, Math.PI * 2);
        ctx.fill();
         ctx.strokeStyle = '#333'; ctx.lineWidth = 1; ctx.stroke(); // Add outline

        // Draw observer
        ctx.fillStyle = observer.color;
        ctx.beginPath();
        ctx.arc(observer.x, observer.y, observer.radius, 0, Math.PI * 2);
        ctx.fill();
         ctx.strokeStyle = '#333'; ctx.lineWidth = 1; ctx.stroke(); // Add outline

         // Draw connecting line
         ctx.strokeStyle = '#555';
         ctx.lineWidth = 1;
         ctx.beginPath();
         ctx.moveTo(source.x, source.y);
         ctx.lineTo(observer.x, observer.y);
         ctx.stroke();

         // Update canvas label positions
         // Position labels near the objects, slightly offset
         sourceLabel.style.left = `${source.x + source.radius + 5}px`;
         sourceLabel.style.top = `${source.y - source.radius - 15}px`;
         observerLabel.style.left = `${observer.x + observer.radius + 5}px`;
         observerLabel.style.top = `${observer.y - observer.radius - 15}px`;
    }

    // Update function
    function update() {
        if (!isRunning) return;

        // Update positions with robust wrapping
        // Use canvas dimensions for wrapping
        source.x = (source.x + source.vx) % canvasWidth;
        source.y = (source.y + source.vy) % canvasHeight;
        observer.x = (observer.x + observer.vx) % canvasWidth;
        observer.y = (observer.y + observer.vy) % canvasHeight;

         // Correct negative wrapping results
         if (source.x < 0) source.x += canvasWidth;
         if (source.y < 0) source.y += canvasHeight;
         if (observer.x < 0) observer.x += canvasWidth;
         if (observer.y < 0) observer.y += canvasHeight;


        // Emit new wave front
        if (frameCount - lastWaveEmissionFrame >= waveEmitInterval) {
            // Store the exact position of the source when the wave is emitted
            waveFronts.push({ x: source.x, y: source.y, creationFrame: frameCount });
            lastWaveEmissionFrame = frameCount;
        }

        // Update frequency display
        perceivedFreqDisplay.textContent = calculatePerceivedFrequency();

        frameCount++;
    }

    // Animation loop
    function animate() {
        update();
        draw();
        animationFrameId = requestAnimationFrame(animate);
    }

    // Helper to update velocity based on speed slider value and direction
    function updateVelocity(obj, speedSliderValue) {
        const speed = (speedSliderValue / 100) * maxSimSpeed; // Scale slider value to simulation speed
        obj.speed = speedSliderValue; // Keep slider value stored

        switch (obj.direction) {
            case 'up': obj.vx = 0; obj.vy = -speed; break;
            case 'down': obj.vx = 0; obj.vy = speed; break;
            case 'left': obj.vx = -speed; obj.vy = 0; break;
            case 'right': obj.vx = speed; obj.vy = 0; break;
            case 'stop': obj.vx = 0; obj.vy = 0; break;
             default: obj.vx = 0; obj.vy = 0; break;
        }
    }

    // Event listeners for controls
    sourceSpeedInput.addEventListener('input', (e) => {
        sourceSpeedValueSpan.textContent = e.target.value;
        // Update velocity based on current direction and new speed slider value
        updateVelocity(source, parseInt(e.target.value));
    });

    observerSpeedInput.addEventListener('input', (e) => {
        observerSpeedValueSpan.textContent = e.target.value;
         // Update velocity based on current direction and new speed slider value
        updateVelocity(observer, parseInt(e.target.value));
    });

    directionButtons.forEach(button => {
        button.addEventListener('click', () => {
            const role = button.dataset.role; // 'source' or 'observer'
            const direction = button.dataset.direction; // 'up', 'down', 'left', 'right', 'stop'
            const obj = role === 'source' ? source : observer;
            const speedInput = role === 'source' ? sourceSpeedInput : observerSpeedInput;
            const speedValueSpan = role === 'source' ? sourceSpeedValueSpan : observerSpeedValueSpan;

            // Update the object's direction state
            obj.direction = direction;

            // Visually highlight the active direction button for this role
            document.querySelectorAll(`.direction-buttons button[data-role="${role}"]`).forEach(btn => {
                btn.classList.remove('active');
            });
             button.classList.add('active');

            // If stopping, set speed to 0 and update slider/span
            if (direction === 'stop') {
                 speedInput.value = 0;
                 speedValueSpan.textContent = 0;
                 obj.speed = 0; // Ensure internal speed state is 0
            }
            // Update velocity based on the new direction and the current speed slider value
             updateVelocity(obj, parseInt(speedInput.value));
        });
    });

    startButton.addEventListener('click', () => {
        if (isRunning) {
            cancelAnimationFrame(animationFrameId);
            isRunning = false;
            startButton.textContent = 'התחלה';
             startButton.style.backgroundColor = '#ff9800'; /* Orange when paused */
             startButton.style.boxShadow = '0 4px 8px rgba(255,152,0,0.2)';
        } else {
            isRunning = true;
            startButton.textContent = 'השהייה';
             startButton.style.backgroundColor = '#4CAF50'; /* Green when running */
             startButton.style.boxShadow = '0 4px 8px rgba(76,175,80,0.2)';
            animate(); // Restart animation loop
        }
    });

    resetButton.addEventListener('click', () => {
        cancelAnimationFrame(animationFrameId); // Stop current animation

        // Reset positions
        source.x = canvasWidth * 0.2;
        source.y = canvasHeight / 2;
        observer.x = canvasWidth * 0.8;
        observer.y = canvasHeight / 2;

        // Reset velocities, speeds, and directions
        source.vx = 0; source.vy = 0; source.speed = 0; source.direction = 'stop';
        observer.vx = 0; observer.vy = 0; observer.speed = 0; observer.direction = 'stop';

        // Reset sliders and spans
        sourceSpeedInput.value = 0; sourceSpeedValueSpan.textContent = 0;
        observerSpeedInput.value = 0; observerSpeedValueSpan.textContent = 0;

        // Remove active class from all direction buttons
         document.querySelectorAll(`.direction-buttons button`).forEach(btn => {
             btn.classList.remove('active');
         });

        // Reset wave fronts and frame count
        waveFronts = [];
        frameCount = 0;
        lastWaveEmissionFrame = -waveEmitInterval; // Ensure wave on first frame

        // Reset frequency display
        perceivedFreqDisplay.textContent = calculatePerceivedFrequency();

        // Ensure start button is 'Start' and pause state
         isRunning = false;
         startButton.textContent = 'התחלה';
         startButton.style.backgroundColor = '#ff9800'; // Orange when paused
         startButton.style.boxShadow = '0 4px 8px rgba(255,152,0,0.2)';


         // Redraw the initial state without animating
         draw();
    });


    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'קראו עוד: ההסבר המלא מאחורי אפקט דופלר';
        // Optional: Scroll to the explanation when shown
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

     // Initial setup
     sourceFreqDisplay.textContent = sourceFrequency.toFixed(2); // Display source frequency
     perceivedFreqDisplay.textContent = calculatePerceivedFrequency(); // Display initial frequency

     // Initialize velocity vectors based on default direction ('stop') and speed (0)
     updateVelocity(source, parseInt(sourceSpeedInput.value));
     updateVelocity(observer, parseInt(observerSpeedInput.value));

     // Set initial active state for stop button
     document.querySelector(`.direction-buttons button[data-role="source"][data-direction="stop"]`).classList.add('active');
     document.querySelector(`.direction-buttons button[data-role="observer"][data-direction="stop"]`).classList.add('active');


     // Initial draw and start animation loop
     draw();
     animate();
});

</script>
```