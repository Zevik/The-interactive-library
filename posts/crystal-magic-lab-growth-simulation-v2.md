---
title: "קסם הגבישים: סימולטור גידול קריסטלים דינמי"
english_slug: crystal-magic-lab-growth-simulation-v2
category: "מדעים מדויקים / כימיה"
tags: [גבישים, גידול גבישים, סימולציה, מעבדה, כימיה פיזיקלית, קריסטליזציה, נוקלאציה]
---
<div class="simulation-title">
  <h1>קסם הגבישים: סימולטור גידול קריסטלים דינמי</h1>
  <p class="subtitle">איך נוצרת הצורה המופלאה של גביש? צללו לתוך תמיסה סופר-רוויה ובחנו כיצד לשלוט בלידתם וצמיחתם של גבישים יפהפיים.</p>
</div>

<div class="crystal-sim-container">
    <div class="controls">
        <h2>במת המעבדה: הגדרות גידול</h2>
        <div class="control-group">
            <label for="supersaturation" class="control-label">עודף חומר בתמיסה (רוויית יתר):</label>
            <input type="range" id="supersaturation" min="0.1" max="1.0" value="0.5" step="0.05">
            <span id="supersaturation-value" class="slider-value-text">בינונית</span>
            <p class="control-description">ריכוז החומר המומס מעבר לנקודת הרוויה. משפיע על מספר "גרעיני הגיבוש" שנוצרים ועל קצב הצמיחה ההתחלתי.</p>
        </div>
        <div class="control-group">
            <label for="coolingRate" class="control-label">קצב קירור התמיסה:</label>
            <input type="range" id="coolingRate" min="0.1" max="1.0" value="0.5" step="0.05">
            <span id="coolingRate-value" class="slider-value-text">בינוני</span>
             <p class="control-description">הקצב בו התמיסה מתקררת. קירור מהיר מגביר את רוויית היתר ומעודד נוקלאציה, קירור איטי מעודד צמיחה על גרעינים קיימים.</p>
        </div>
        <div class="control-group">
            <label for="impurities" class="control-label">כמות זיהומים בתמיסה:</label>
            <input type="range" id="impurities" min="0.0" max="0.9" value="0.2" step="0.05">
            <span id="impurities-value" class="slider-value-text">נמוכה</span>
             <p class="control-description">חלקיקים לא רצויים בתמיסה. מפריעים לסדר הגבישי, מפחיתים את שקיפות הגבישים ועלולים להאט את הצמיחה.</p>
        </div>
        <button id="startSimulation" class="action-button primary">התחל הדמיה</button>
    </div>
    <div class="simulation-area">
        <canvas id="crystalCanvas"></canvas>
         <div id="simulationStatus" class="status-message">בחר הגדרות ולחץ "התחל הדמיה"...</div>
        <div id="results" class="results-box hidden">
            <h2>תוצאות הגידול הסופיות:</h2>
            <div class="result-item"><span class="result-label">סה"כ גבישים:</span> <span id="result-count"></span></div>
            <div class="result-item"><span class="result-label">גודל ממוצע:</span> <span id="result-size"></span></div>
            <div class="result-item"><span class="result-label">איכות/שקיפות:</span> <span id="result-clarity"></span></div>
             <div class="result-item"><span class="result-label">ציון איכות כולל:</span> <span id="result-score" class="score"></span></div>
            <button id="resetSimulation" class="action-button secondary">הרץ הדמיה חדשה</button>
        </div>

    </div>
</div>

<button id="toggleExplanation" class="toggle-button">הצג/הסתר הסבר על קריסטליזציה</button>

<div id="explanation" class="explanation-box hidden">
    <h2>הקסם שמאחורי הגבישים: תהליך ההתגבשות (קריסטליזציה)</h2>
    <p><strong>מהו גביש?</strong> דמיינו קוביות לגו קטנות, מסודרות באופן מושלם בתלת-ממד שחוזר על עצמו. זהו גביש ברמה האטומית! גביש הוא חומר מוצק שבו החלקיקים הבסיסיים (אטומים, יונים, מולקולות) מסודרים בתבנית מחזורית ויציבה. הסידור המסודר הזה הוא שמעניק לגבישים רבים את צורתם החיצונית היפה והסימטרית (כמו קוביות מלח או משושים של שלג).</p>

    <p><strong>כיצד גבישים "נולדים" וגדלים?</strong> תהליך הקריסטליזציה מתרחש לרוב בתמיסה (חומר מומס בנוזל) או מתוך חומר מותך שמתקרר. כדי שזה יקרה, התמיסה/הנמס חייבים להיות במצב של "רוויית יתר" - כלומר, יש בהם יותר חומר מומס/מותך ממה שהם מסוגלים להכיל בטמפרטורה הנתונה. במצב זה, החומר "ממהר" לצאת מהתמיסה/נמס ולהתארגן מחדש במבנה הגבישי המוצק והיציב שלו. התהליך כולל שני שלבים עיקריים:</p>
    <ol>
        <li><strong>נוקלאציה (לידת הגרעינים):</strong> זהו השלב הראשוני והקריטי בו נוצרים "גרעיני גיבוש" זעירים – אשכולות קטנים של חלקיקים שכבר התחילו להסתדר במבנה הגבישי. הם יכולים להיווצר באופן ספונטני (נוקלאציה ראשונית) או להיתלות על משטחים קיימים (כמו דפנות הכלי או זיהומים – נוקלאציה משנית). תנאים של רוויית יתר גבוהה (עודף גדול של חומר) וקירור מהיר מעודדים לידה של *הרבה* גרעינים כאלה.</li>
        <li><strong>צמיחת גביש:</strong> ברגע שגרעין יציב נוצר, חלקיקים נוספים מהתמיסה/נמס מתחילים "להתיישב" על פני השטח שלו ולהיצמד אליו בצורה מסודרת, תוך המשך בניית הסריג הגבישי. שלב זה הוא שאחראי על הגדלת הגביש. קצב הצמיחה תלוי בזמינות החומר המומס (שמושפעת גם מקצב הפינוי של חום ההתגבשות שמשתחרר).</li>
    </ol>

    <p><strong>איך הגדרות המעבדה משפיעות על התוצאה?</strong></p>
    <ul>
        <li><strong>רוויית יתר גבוהה:</strong> מעודדת מאוד נוקלאציה (יותר גרעינים), וכתוצאה מכך נוצרים המון גבישים קטנים. הצמיחה עשויה להיות מהירה בהתחלה אך החומר המומס אוזל מהר.</li>
        <li><strong>רוויית יתר מתונה:</strong> מעודדת פחות נוקלאציה (פחות גרעינים), אך יותר צמיחה על הגרעינים הקיימים. התוצאה לרוב תהיה פחות גבישים, אבל גדולים יותר. זהו לרוב התנאי המועדף לגידול גבישים גדולים ואיכותיים.</li>
        <li><strong>קצב קירור מהיר:</strong> מגביר את רוויית היתר במהירות ודוחף ליצירת גרעינים רבים בבת אחת. מוביל להרבה גבישים קטנים, בדומה לרוויית יתר גבוהה.</li>
         <li><strong>קצב קירור איטי:</strong> מאפשר לרוויית היתר לעלות בהדרגה, מעודד צמיחה מסודרת על גרעינים קיימים, ומאפשר קבלת גבישים גדולים יותר ואיכותיים יותר.</li>
        <li><strong>כמות זיהומים גדולה:</strong> זיהומים "נתקעים" בתוך הגביש בזמן שהוא גדל, מפריעים לסידור המסודר של החלקיקים וגורמים לגביש להיות מעונן, פגום, או בעל צורה לא מושלמת. כמו כן, זיהומים יכולים לשמש כ"גרעיני גיבוש" לא רצויים ולגרום ליצירת הרבה גבישים קטנים.</li>
        <li><strong>כמות זיהומים נמוכה:</strong> מאפשרת לחלקיקים להתחבר בצורה מסודרת ולבנות סריג גבישי מושלם יותר. התוצאה היא גבישים צלולים, שקופים ואיכותיים יותר.</li>
    </ul>

    <p><strong>מטרת המשחק:</strong> נסו למצוא את שילוב ההגדרות האופטימלי לקבלת גבישים "אידיאליים" – מעט גבישים, גדולים מאוד וצלולים לחלוטין! האם תצליחו לגדל את גביש היהלום שלכם?</p>

    <p>גידול גבישים הוא לא רק קסם טבעי, אלא תהליך מדעי ותעשייתי חשוב ביותר שמשמש לייצור שבבים אלקטרוניים, תרופות, חומרים אופטיים ועוד.</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #28a745;
        --accent-color: #ffc107;
        --background-color: #e9ecef;
        --surface-color: #ffffff;
        --border-color: #ced4da;
        --text-color: #343a40;
        --subtle-text-color: #6c757d;
        --danger-color: #dc3545;
        --canvas-background: #e0f7fa; /* Light blue for solution */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
    }

    .simulation-title {
        text-align: center;
        margin-bottom: 30px;
    }

    .simulation-title h1 {
        color: var(--primary-color);
        margin-bottom: 10px;
    }

    .simulation-title .subtitle {
        color: var(--subtle-text-color);
        font-size: 1.1em;
    }

    .crystal-sim-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        margin-bottom: 30px;
        background-color: var(--surface-color);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        align-items: flex-start; /* Align items to the top */
    }

    .controls {
        flex: 1;
        min-width: 300px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #f8f9fa; /* Lighter surface */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

    .controls h2 {
        margin-top: 0;
        color: var(--primary-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    .control-group {
        margin-bottom: 25px;
    }

    .control-label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: var(--text-color);
    }

    .control-group input[type="range"] {
        width: calc(100% - 70px); /* Adjust width */
        vertical-align: middle;
        -webkit-appearance: none; /* Override default CSS styles */
        appearance: none;
        height: 8px;
        background: var(--border-color);
        outline: none;
        opacity: 0.7;
        transition: opacity .2s ease;
        border-radius: 5px;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--surface-color);
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--surface-color);
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

     .control-group input[type="range"]:hover {
        opacity: 1;
     }

     .slider-value-text {
        display: inline-block;
        width: 60px; /* Fixed width */
        text-align: right;
        vertical-align: middle;
        font-size: 0.9em;
        color: var(--subtle-text-color);
        font-weight: bold;
     }

    .control-description {
        font-size: 0.85em;
        color: var(--subtle-text-color);
        margin-top: 8px;
        padding-top: 5px;
        border-top: 1px dashed #e9ecef;
    }

    .action-button {
        display: block;
        width: 100%;
        padding: 12px 15px;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .action-button.primary {
        background-color: var(--primary-color);
        color: white;
    }
    .action-button.primary:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }
    .action-button.primary:active {
         transform: translateY(0);
    }

     .action-button.secondary {
        margin-top: 15px;
        background-color: var(--secondary-color);
        color: white;
     }
      .action-button.secondary:hover {
        background-color: #218838;
         transform: translateY(-1px);
     }
      .action-button.secondary:active {
         transform: translateY(0);
    }

    .action-button:disabled {
        background-color: var(--border-color);
        cursor: not-allowed;
        opacity: 0.6;
        transform: none;
    }


    .simulation-area {
        flex: 2;
        min-width: 350px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center; /* Center canvas vertically if needed */
        position: relative; /* For absolute positioning of status/results */
    }

    #crystalCanvas {
        border: 2px solid #000; /* Beaker outline */
        background-color: var(--canvas-background); /* Solution color */
        display: block;
        margin-bottom: 15px;
        border-radius: 5px; /* Soften edges */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }

     .status-message {
        text-align: center;
        font-style: italic;
        color: var(--subtle-text-color);
        min-height: 1.5em; /* Prevent layout shift */
        margin-bottom: 15px;
     }

    .results-box {
        width: 100%;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #f8f9fa;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
         margin-top: 10px; /* Space from canvas */
    }

    .results-box h2 {
        margin-top: 0;
        color: var(--primary-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    .result-item {
        margin-bottom: 10px;
        font-size: 1.1em;
    }

    .result-label {
        font-weight: bold;
        margin-right: 5px;
    }

     .score {
         font-weight: bold;
         color: var(--secondary-color); /* Default good score color */
     }

     .score.low { color: var(--danger-color); } /* Low score color */
     .score.medium { color: var(--accent-color); } /* Medium score color */
     .score.high { color: var(--secondary-color); } /* High score color */


    .hidden {
        display: none;
    }

    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 10px 20px;
        background-color: var(--subtle-text-color);
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
    .toggle-button:hover {
        background-color: #5a6268;
         transform: translateY(-1px);
    }
     .toggle-button:active {
         transform: translateY(0);
    }

    .explanation-box {
        border: 1px solid var(--border-color);
        padding: 20px;
        border-radius: 8px;
        background-color: #f8f9fa;
        line-height: 1.7;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }
    .explanation-box h2 {
        margin-top: 0;
        color: var(--primary-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
     .explanation-box p {
        margin-bottom: 1em;
     }
     .explanation-box ul, .explanation-box ol {
        margin-bottom: 1em;
        padding-left: 25px;
     }
     .explanation-box li {
        margin-bottom: 0.7em;
     }

     /* Responsive adjustments */
     @media (max-width: 768px) {
        .crystal-sim-container {
            flex-direction: column;
            align-items: stretch;
        }
        .controls, .simulation-area {
            min-width: auto;
            width: 100%;
        }
         #crystalCanvas {
             width: 100%; /* Make canvas responsive */
             height: auto; /* Maintain aspect ratio */
             max-width: 400px; /* But don't let it get too big */
             margin-left: auto;
             margin-right: auto;
         }
     }

</style>

<script>
    const canvas = document.getElementById('crystalCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startSimulation');
    const resetButton = document.getElementById('resetSimulation');
    const supersaturationSlider = document.getElementById('supersaturation');
    const coolingRateSlider = document.getElementById('coolingRate');
    const impuritiesSlider = document.getElementById('impurities');
    const supersaturationValueSpan = document.getElementById('supersaturation-value');
    const coolingRateValueSpan = document.getElementById('coolingRate-value');
    const impuritiesValueSpan = document.getElementById('impurities-value');
    const resultsDiv = document.getElementById('results');
    const resultCountSpan = document.getElementById('result-count');
    const resultSizeSpan = document.getElementById('result-size');
    const resultClaritySpan = document.getElementById('result-clarity');
     const resultScoreSpan = document.getElementById('result-score');
    const simulationStatusDiv = document.getElementById('simulationStatus');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');

    // Dynamic canvas size (adjusts based on container, but keep aspect ratio)
    const canvasWidth = 400;
    const canvasHeight = 400;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;


    let animationFrameId;
    let particles = []; // Represents dissolved solute molecules
    let crystals = [];
    let simulationRunning = false;
    const simulationDuration = 600; // frames (approx 10-15 seconds)
    let currentFrame = 0;

    const maxParticles = 1500; // Max number of dissolved particles
    let currentParticleCount = 0;

    // Map slider values to descriptive text
    const mapSliderValue = (value, type) => {
        if (type === 'supersaturation') {
            if (value < 0.35) return 'נמוכה מאוד';
            if (value < 0.55) return 'בינונית';
            if (value < 0.8) return 'גבוהה';
            return 'גבוהה מאוד';
        } else if (type === 'coolingRate') {
             if (value < 0.35) return 'איטי מאוד';
            if (value < 0.55) return 'בינוני';
            if (value < 0.8) return 'מהיר';
            return 'מהיר מאוד';
        } else if (type === 'impurities') {
            if (value < 0.15) return 'אפסית';
            if (value < 0.35) return 'נמוכה';
            if (value < 0.65) return 'בינונית';
            if (value < 0.85) return 'גבוהה';
            return 'גבוהה מאוד';
        }
        return '';
    };

     // Update slider value spans and descriptions on input
     const updateSliderDisplay = (slider, span, type) => {
        const value = parseFloat(slider.value);
        span.textContent = mapSliderValue(value, type);
        // No description update needed, they are static in HTML
     };

     supersaturationSlider.addEventListener('input', () => updateSliderDisplay(supersaturationSlider, supersaturationValueSpan, 'supersaturation'));
     coolingRateSlider.addEventListener('input', () => updateSliderDisplay(coolingRateSlider, coolingRateValueSpan, 'coolingRate'));
     impuritiesSlider.addEventListener('input', () => updateSliderDisplay(impuritiesSlider, impuritiesValueSpan, 'impurities'));

    // Initial display of slider values
    updateSliderDisplay(supersaturationSlider, supersaturationValueSpan, 'supersaturation');
    updateSliderDisplay(coolingRateSlider, coolingRateValueSpan, 'coolingRate');
    updateSliderDisplay(impuritiesSlider, impuritiesValueSpan, 'impurities');

    // --- Simulation Logic ---

    function createParticle() {
        return {
            x: Math.random() * canvasWidth,
            y: Math.random() * canvasHeight,
            vx: (Math.random() - 0.5) * 0.5, // Initial random velocity
            vy: (Math.random() - 0.5) * 0.5,
            size: 1,
            color: 'rgba(0, 123, 255, 0.7)' // Blueish for solute
        };
    }

     function createNucleus(x, y, impuritiesValue) {
         return {
             x: x,
             y: y,
             size: 2, // Start size
             impurities: impuritiesValue,
             facets: [], // Store points for polygonal shape
             isGrowing: true // Flag to indicate active growth
         };
     }

    function drawBeaker() {
        ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--canvas-background').trim();
        ctx.fillRect(0, 0, canvasWidth, canvasHeight);

        // No distinct beaker outline needed with canvas background
    }

    function drawParticles() {
        ctx.fillStyle = 'rgba(0, 123, 255, 0.6)'; // Slightly less opaque when drawing all
        particles.forEach(p => {
             ctx.fillRect(p.x, p.y, p.size, p.size); // Draw as tiny squares
        });
    }

    function drawCrystals() {
       crystals.forEach(crystal => {
            const clarity = 1 - crystal.impurities;
            const baseColor = Math.floor(255 * clarity); // Closer to white/clear for pure
            const impurityAlpha = crystal.impurities * 0.8; // Impure crystals are more opaque/cloudy

            if (crystal.size < 5 || crystal.impurities > 0.6) { // Small or very impure crystals are round/blobby
                 ctx.beginPath();
                 ctx.arc(crystal.x, crystal.y, crystal.size, 0, Math.PI * 2);
                 ctx.fillStyle = `rgba(${baseColor}, ${baseColor}, ${baseColor}, ${0.5 + impurityAlpha * 0.5})`; // More opaque/grey with impurities
                 ctx.fill();
                  if (clarity > 0.3) { // Add a subtle outline for clearer ones
                     ctx.strokeStyle = `rgba(0, 0, 0, ${0.2 * clarity})`;
                     ctx.stroke();
                 }
            } else { // Larger, purer crystals get a faceted look
                 ctx.beginPath();
                 // Generate facets if not already generated or if size increased significantly
                 if (crystal.facets.length === 0 || (crystal.size / crystal._lastFacetSizeUpdate > 1.1 && crystal.size > 5)) {
                     crystal.facets = generateFacets(crystal.size, clarity);
                     crystal._lastFacetSizeUpdate = crystal.size;
                 }

                 // Draw polygon based on facets
                 ctx.moveTo(crystal.x + crystal.facets[0].x, crystal.y + crystal.facets[0].y);
                 for (let i = 1; i < crystal.facets.length; i++) {
                     ctx.lineTo(crystal.x + crystal.facets[i].x, crystal.y + crystal.facets[i].y);
                 }
                 ctx.closePath();

                 ctx.fillStyle = `rgba(${baseColor}, ${baseColor}, ${baseColor}, ${0.6 + impurityAlpha * 0.4})`;
                 ctx.fill();

                  if (clarity > 0.4) { // Add a subtle outline
                     ctx.strokeStyle = `rgba(0, 0, 0, ${0.3 * clarity})`;
                     ctx.stroke();
                 }
            }
        });
    }

    function generateFacets(size, clarity) {
         const numFacets = Math.max(4, Math.min(10, Math.floor(size / 4) + Math.floor(clarity * 5))); // More facets for larger/purer
         const angleStep = (Math.PI * 2) / numFacets;
         const facets = [];
         for (let i = 0; i < numFacets; i++) {
             const angle = i * angleStep + (Math.random() - 0.5) * (1 - clarity) * angleStep * 0.5; // Slight randomness based on impurity
             const radius = size * (0.8 + Math.random() * 0.4 * clarity); // Radius variation based on clarity
             facets.push({ x: radius * Math.cos(angle), y: radius * Math.sin(angle) });
         }
         return facets;
     }


    function updateSimulation() {
        if (!simulationRunning) return;

        currentFrame++;
        const progress = currentFrame / simulationDuration;
        simulationStatusDiv.textContent = `גידול בעיצומו... (${Math.round(progress * 100)}%)`;

        const supersaturation = parseFloat(supersaturationSlider.value);
        const coolingRate = parseFloat(coolingRateSlider.value);
        const impurities = parseFloat(impuritiesSlider.value);

        // 1. Manage Dissolved Particles (Solute)
        // Add new particles based on initial supersaturation and cooling rate (represents available solute)
        // The rate of particle generation decreases over time as solute is used up
         const initialParticleRate = supersaturation * (1 + coolingRate * 0.5) * 5; // Higher rate initially
         const particleGenerationDecay = 1 - (currentFrame / simulationDuration); // Decreases over time

        if (currentParticleCount < maxParticles && Math.random() < initialParticleRate * particleGenerationDecay * 0.1) {
             particles.push(createParticle());
             currentParticleCount++;
         }


        // Move particles randomly
        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;

            // Bounce off walls
            if (p.x < 0 || p.x > canvasWidth) p.vx *= -1;
            if (p.y < 0 || p.y > canvasHeight) p.vy *= -1;

             // Add slight random walk
             p.vx += (Math.random() - 0.5) * 0.2;
             p.vy += (Math.random() - 0.5) * 0.2;
             // Limit speed
             const speed = Math.sqrt(p.vx * p.vx + p.vy * p.vy);
             const maxSpeed = 1.5 * coolingRate; // Faster particles with faster cooling
             if (speed > maxSpeed) {
                 p.vx = (p.vx / speed) * maxSpeed;
                 p.vy = (p.vy / speed) * maxSpeed;
             }
        });

        // 2. Nucleation (Birth of new crystals)
        // Chance of nucleation is high with high supersaturation and high cooling rate, but decreases as crystals grow
         const nucleationFactor = supersaturation * coolingRate; // Combined effect
         const existingCrystalInfluence = Math.max(0, 1 - crystals.length / 50); // Less nucleation if many crystals exist
         const nucleationChance = nucleationFactor * existingCrystalInfluence * 0.0015; // Adjust constant

         if (Math.random() < nucleationChance) {
            // Find a particle to become a nucleus (optional, just adds flavour)
            if (particles.length > 0) {
                 const nucleusParticleIndex = Math.floor(Math.random() * particles.length);
                 const nucleusParticle = particles[nucleusParticleIndex];
                 crystals.push(createNucleus(nucleusParticle.x, nucleusParticle.y, impurities));
                 particles.splice(nucleusParticleIndex, 1); // Remove particle, it's now a crystal seed
                 currentParticleCount--;
            } else if (supersaturation > 0.6 && coolingRate > 0.6) { // Allow spontaneous nucleation if highly supersaturated/cooled
                  const x = Math.random() * (canvasWidth - 40) + 20;
                  const y = Math.random() * (canvasHeight - 40) + 20;
                  crystals.push(createNucleus(x, y, impurities));
            }
        }


        // 3. Crystal Growth (Particles attaching to crystals)
        const growthModifier = (1 - impurities * 0.7); // Impurities hinder growth significantly
        const attachmentRadius = 5; // How close a particle needs to be

        crystals.forEach(crystal => {
             if (!crystal.isGrowing) return;

             // Attract nearby particles
             particles = particles.filter(p => {
                 const distSq = (p.x - crystal.x) * (p.x - crystal.x) + (p.y - crystal.y) * (p.y - crystal.y);
                 const effectiveRadius = crystal.size + attachmentRadius;

                 if (distSq < effectiveRadius * effectiveRadius) {
                      // Particle is close enough - attempt to attach
                      const attachmentChance = growthModifier * (1 - (distSq / (effectiveRadius * effectiveRadius))); // Higher chance when closer, reduced by impurities

                      if (Math.random() < attachmentChance) {
                          crystal.size += 0.1 * growthModifier; // Grow slightly, influenced by impurities
                           crystal.size = Math.min(crystal.size, 40); // Max size limit
                           // Check if crystal stopped growing (e.g., too big, or ran out of local particles?)
                           // For simplicity, they just grow until simulation ends or hit max size

                          return false; // Particle is consumed, remove it
                      }
                 }

                 // Particle wasn't consumed, keep it
                 return true;
             });
             currentParticleCount = particles.length; // Update particle count after filtering

            // Slight visual wobble for growing crystals
             if (crystal.size > 5 && crystal.isGrowing) {
                  crystal.x += (Math.random() - 0.5) * 0.1;
                  crystal.y += (Math.random() - 0.5) * 0.1;
                  // Keep them within bounds after wobble
                  crystal.x = Math.max(10, Math.min(canvasWidth - 10, crystal.x));
                  crystal.y = Math.max(10, Math.min(canvasHeight - 10, crystal.y));
             }
        });


        drawBeaker();
        drawParticles(); // Draw particles first, so crystals are on top
        drawCrystals();


        if (currentFrame < simulationDuration) {
            animationFrameId = requestAnimationFrame(updateSimulation);
        } else {
            endSimulation();
        }
    }

    function startSimulation() {
        if (simulationRunning) return;

        crystals = []; // Clear previous crystals
        particles = []; // Clear particles
        currentParticleCount = 0;
        currentFrame = 0;
        simulationRunning = true;
        startButton.disabled = true;
        resetButton.classList.add('hidden');
        resultsDiv.classList.add('hidden');
        simulationStatusDiv.textContent = 'הדמיה מתחילה... ממלאים תמיסה...';

        // Add initial particles based on supersaturation
        const initialParticleDensity = parseFloat(supersaturationSlider.value) * maxParticles * 0.8; // Up to 80% of max
         for (let i = 0; i < initialParticleDensity; i++) {
             particles.push(createParticle());
         }
         currentParticleCount = particles.length;


        // Disable sliders during simulation
        supersaturationSlider.disabled = true;
        coolingRateSlider.disabled = true;
        impuritiesSlider.disabled = true;

        // Initial draw
        drawBeaker();
        drawParticles();
        drawCrystals();

        // Start the animation loop after a short delay to show initial state
        setTimeout(() => {
            updateSimulation();
        }, 500);
    }

    function endSimulation() {
        simulationRunning = false;
        cancelAnimationFrame(animationFrameId);
        startButton.disabled = false;
        resetButton.classList.remove('hidden');
        simulationStatusDiv.textContent = 'הדמיה הסתיימה. בדקו את התוצאות!';

         // Enable sliders after simulation
        supersaturationSlider.disabled = false;
        coolingRateSlider.disabled = false;
        impuritiesSlider.disabled = false;


        // Calculate and display results
        displayResults();
    }

    function displayResults() {
        const numCrystals = crystals.length;
        const totalSize = crystals.reduce((sum, crystal) => sum + crystal.size, 0);
        const averageSize = numCrystals > 0 ? (totalSize / numCrystals) : 0;

        const impurities = parseFloat(impuritiesSlider.value);
        let clarityText = '';
        let clarityScore = 0; // 0-3
        if (impurities < 0.15) {
            clarityText = 'יוצאת דופן (צלולים לחלוטין)';
            clarityScore = 3;
        } else if (impurities < 0.35) {
            clarityText = 'גבוהה (צלולים ברובם)';
             clarityScore = 2.5;
        }
        else if (impurities < 0.65) {
            clarityText = 'בינונית (קצת מעוננים)';
            clarityScore = 1.5;
        } else if (impurities < 0.85) {
            clarityText = 'נמוכה (מעוננים/פגומים)';
             clarityScore = 0.5;
        }
        else {
             clarityText = 'גרועה (קריסטלים קטנים ופגומים)';
             clarityScore = 0;
        }


        // Add context based on number and size for score
        let countScore = 0; // Max 3
        if (numCrystals < 5) countScore = 3; // Few large
        else if (numCrystals < 20) countScore = 2.5; // Moderate number, maybe large
        else if (numCrystals < 50) countScore = 1.5; // Many, medium
        else countScore = 0.5; // Very many, small


        let sizeScore = 0; // Max 3
        if (averageSize > 25) sizeScore = 3; // Very large
        else if (averageSize > 15) sizeScore = 2.5; // Large
        else if (averageSize > 8) sizeScore = 1.5; // Medium
        else if (averageSize > 3) sizeScore = 0.5; // Small
        else sizeScore = 0; // Very small/none


        // Calculate total score (normalize based on max possible score)
        const maxPossibleScore = 3 + 3 + 3; // Size + Count + Clarity (arbitrary weight)
        const totalRawScore = sizeScore * 3 + countScore * 2 + clarityScore * 3; // Give more weight to size and clarity
        const totalScore = Math.round((totalRawScore / (3*3 + 2*3 + 3*3)) * 10); // Scale to 0-10

        let scoreText = `${totalScore}/10`;
        resultScoreSpan.textContent = scoreText;
         resultScoreSpan.classList.remove('low', 'medium', 'high');
         if (totalScore < 4) resultScoreSpan.classList.add('low');
         else if (totalScore < 7) resultScoreSpan.classList.add('medium');
         else resultScoreSpan.classList.add('high');


        resultCountSpan.textContent = `${numCrystals}`;
        resultSizeSpan.textContent = `${averageSize.toFixed(1)} יחידות`; // Using abstract units
        resultClaritySpan.textContent = clarityText;


        resultsDiv.classList.remove('hidden');
    }

    function resetSimulation() {
        crystals = [];
        particles = [];
        currentParticleCount = 0;
        currentFrame = 0;
        simulationRunning = false;
        resultsDiv.classList.add('hidden');
        resetButton.classList.add('hidden');
        simulationStatusDiv.textContent = 'מוכן להדמיה חדשה. שנה הגדרות אם תרצה.';
        drawBeaker(); // Draw initial empty beaker
    }

    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
         // Change button text
        if (explanationDiv.classList.contains('hidden')) {
             toggleExplanationButton.textContent = 'הצג הסבר על קריסטליזציה';
        } else {
             toggleExplanationButton.textContent = 'הסתר הסבר';
        }
    });

    // Initial setup
    drawBeaker();
    resultsDiv.classList.add('hidden'); // Hide results initially
    resetButton.classList.add('hidden'); // Hide reset initially
    // Initial status text is set in HTML

</script>
```