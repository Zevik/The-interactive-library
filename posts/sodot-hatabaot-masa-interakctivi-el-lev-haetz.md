---
title: "סודות הטבעות: מסע אינטראקטיבי אל לב העץ"
english_slug: sodot-hatabaot-masa-interakctivi-el-lev-haetz
category: "ביולוגיה"
tags: [בוטניקה, צמחים, גדילה, טבעות שנתיות, סימולציה, אינטראקטיבי, אקלים]
---
# סודות הטבעות: מסע אינטראקטיבי אל לב העץ
דמיינו שהייתם יכולים לקרוא את הסיפור של עץ, שנה אחר שנה, ממש בתוך הגזע שלו. טבעות הגדילה הן בדיוק זה – יומן מסע טבעי המתעד את תנאי הסביבה שעיצבו את חייו. בסימולטור זה, אתם הבמאים! קבעו את מזג האוויר וגורמים אחרים, וצפו כיצד החלטותיכם משפיעות על העץ, שנה אחר שנה. גלו את הקשר המרתק בין הטבע לסיפור שחרות על העץ.

<div class="app-container">
    <div class="app-header">
        <h2>סימולטור גדילת טבעות עץ</h2>
        <div class="year-info">
            <span class="year-label">שנה:</span> <span id="current-year" class="year-number">0</span>
        </div>
    </div>

    <div class="simulator-content">
        <div class="controls-panel">
            <h3>תנאי הסביבה השנתיים:</h3>
            <div class="condition-sliders">
                <div class="slider-group">
                    <label for="precipitation">💦 כמות משקעים:</label>
                    <input type="range" id="precipitation" min="1" max="10" value="5">
                    <span id="precipitation-value" class="slider-value">5</span>
                    <p class="slider-tip">מים הם החיים! ככל שיש יותר גשם, הגדילה מהירה יותר.</p>
                </div>
                <div class="slider-group">
                    <label for="sunlight">☀️ עוצמת קרינת שמש:</label>
                    <input type="range" id="sunlight" min="1" max="10" value="5">
                    <span id="sunlight-value" class="slider-value">5</span>
                    <p class="slider-tip">אור שמש חיוני לפוטוסינתזה. יותר אור = יותר אנרגיה לגדילה.</p>
                </div>
                <div class="slider-group">
                    <label for="temperature">🌡️ טמפרטורה ממוצעת:</label>
                    <input type="range" id="temperature" min="1" max="10" value="5">
                    <span id="temperature-value" class="slider-value">5</span>
                     <p class="slider-tip">כל עץ אוהב טמפרטורה מסוימת. קיצוניות (חום/קור) מאטה את הגדילה.</p>
                </div>
                <div class="slider-group">
                    <label for="pests">🐛 נוכחות מזיקים/מחלות:</label>
                    <input type="range" id="pests" min="1" max="10" value="1">
                    <span id="pests-value" class="slider-value">1</span>
                     <p class="slider-tip">מזיקים ומחלות גוזלים מהעץ אנרגיה ומחלישים אותו.</p>
                </div>
            </div>
            <div class="action-buttons">
                <button id="next-year-btn" class="btn-primary">סיים שנה וצפה בטבעת</button>
                <button id="reset-btn" class="btn-secondary">התחל עץ חדש</button>
            </div>
        </div>

        <div class="visualization-area">
             <div class="canvas-container">
                 <canvas id="tree-canvas" width="400" height="400"></canvas>
                 <div class="canvas-overlay"></div> <!-- For subtle animation effects -->
             </div>
            <div class="history">
                <h4>יומן גדילה:</h4>
                <ul id="year-history-list">
                    <li>בחר תנאים לשנה הראשונה...</li>
                </ul>
            </div>
        </div>
    </div>
     <div class="growth-summary" id="growth-summary"></div> <!-- Area for growth summary -->
</div>

<button id="toggle-explanation-btn" class="btn-toggle-explanation">הצג/הסתר הסבר על טבעות גדילה</button>

<div id="explanation" class="explanation-section hidden">
    <h2>הסבר מפורט: מה העץ מספר לנו בטבעות שלו?</h2>

    <h3>מהן טבעות שנתיות וכיצד הן נוצרות?</h3>
    <p>טבעות הגדילה, או טבעות שנתיות, הן כמו דפים ביומן של העץ. בכל עונת גדילה פעילה, העץ מוסיף שכבה חדשה של עצה (רקמה המובילה מים ותומכת בעץ) סביב השכבות הישנות יותר. כשחותכים גזע, השכבות האלו נראות כטבעות מעגליות.</p>
    <p>באזורים עם עונות מובחנות (כמו קיץ/חורף או עונה יבשה/רטובה), העץ גדל בקצב שונה במהלך השנה. הגדילה המהירה יותר (בדרך כלל באביב/תחילת העונה הרטובה) יוצרת תאי עצה גדולים ובהירים יותר (עץ אביב), והגדילה האיטית יותר (בקיץ/לקראת סוף העונה הרטובה) יוצרת תאי עצה קטנים וצפופים יותר, הנראים כהים יותר (עץ קיץ). המעבר החד בין ה'עץ הכהה' של שנה אחת ל'עץ הבהיר' של השנה שאחריה יוצר את הגבול הברור של הטבעת, ומאפשר לנו לספור שנים.</p>

    <h3>מבנה הגזע: השחקנים הראשיים</h3>
    <ul>
        <li><strong>קמביום (Cambium):</strong> שכבת קסם דקה! נמצאת בין העצה (פנים) לשיפה (חוץ). תאי הקמביום מתחלקים ויוצרים עצה חדשה פנימה ושיפה חדשה החוצה, וכך העץ מתרחב.</li>
        <li><strong>קסילם (Xylem - עצה):</strong> ה"שלד" ומערכת ה"אינסטלציה" של העץ. מוביל מים ומינרלים מהשורשים למעלה, ומספק תמיכה. זה החלק שממנו עשויות הטבעות השנתיות.</li>
        <li><strong>פלואם (Phloem - שיפה):</strong> ה"שליח" של העץ. מוביל סוכרים (תוצר הפוטוסינתזה בעלים) לשאר חלקי העץ. ממוקם בחוץ, ומהווה חלק מהקליפה.</li>
    </ul>

    <h3>סיפור ברוחב הטבעת: איך תנאי הסביבה משפיעים?</h3>
    <p>רוחבה של כל טבעת מספר סיפור על השנה שבה נוצרה:</p>
    <ul>
        <li><strong>מים (משקעים):</strong> הכי קריטי! שנה גשומה במיוחד = טבעת רחבה. שנת בצורת קשה = טבעת דקיקה (או אפילו ללא גדילה כלל).</li>
        <li><strong>אור שמש:</strong> דלק לפוטוסינתזה. הרבה שמש (בלי הצללה) = ייצור סוכרים גבוה = גדילה טובה.</li>
        <li><strong>טמפרטורה:</strong> טמפרטורות מתאימות מאפשרות תהליכים ביולוגיים יעילים. חום או קור קיצוניים יעצרו או יאטו גדילה משמעותית.</li>
        <li><strong>מזיקים ומחלות:</strong> התקפה קשה מחלישה את העץ, גורמת לו "לבזבז" אנרגיה על התגוננות במקום על גדילה, והטבעת תהיה צרה.</li>
    </ul>
    <p>טבעת רחבה היא עדות לשנה טובה, וטבעת צרה היא עדות לשנה קשה.</p>

    <h3>בלשי העצים: שימושים מדהימים בטבעות שנתיות</h3>
    <p>חקר טבעות העץ נקרא דנדרוכרונולוגיה. מה אפשר ללמוד ממנו?</p>
    <ul>
        <li><strong>תיארוך מדויק:</strong> על ידי השוואת דפוסי רוחב טבעות מעצים שונים (חיים, מתים, שרידים ארכיאולוגיים), אפשר לתארך עצים או מבני עץ בדיוק של שנה בודדת!</li>
        <li><strong>שחזור עבר האקלים:</strong> מכיוון שרוחב הטבעת מושפע מאקלים, דפוסי טבעות מעצים עתיקים הם תיעוד מדהים של תנאי האקלים שהיו לפני מאות ואלפי שנים, הרבה לפני שהתחלנו למדוד אותם באופן שיטתי. כך לומדים על תקופות בצורת, גשמים, ועוד.</li>
        <li><strong>תיעוד אירועים:</strong> צלקות משריפות, סימני כפור, או עיוותים שנגרמו על ידי מזיקים או פציעות אחרות נשמרים גם הם בטבעות ומספרים על אירועים ספציפיים בחיי העץ.</li>
    </ul>
</div>

<style>
:root {
    --color-primary: #4a90e2; /* Blue */
    --color-secondary: #f5a623; /* Orange */
    --color-text: #333;
    --color-bg-light: #f8f8f8;
    --color-bg-medium: #e0e0e0;
    --color-bg-dark: #c0c0c0;
    --color-ring-spring: #f0d9b5; /* Warm light brown */
    --color-ring-summer: #8b4513; /* Saddle Brown */
    --color-core: #5a3e2c; /* Darker core */
    --color-success: #7ed321; /* Green */
    --color-warning: #f8e71c; /* Yellow */
    --color-danger: #d0021b; /* Red */
    --border-radius: 8px;
    --box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

body {
     font-family: 'Arial Hebrew', 'Arial', sans-serif;
     direction: rtl;
     line-height: 1.6;
     color: var(--color-text);
     background-color: #f4f4f4;
     margin: 0;
     padding: 20px;
}

.app-container {
    background-color: #fff;
    max-width: 900px;
    margin: 20px auto;
    padding: 30px;
    border-radius: var(--border-radius);
    box-shadow: var(--box-shadow);
    text-align: right;
}

.app-header {
    text-align: center;
    margin-bottom: 20px;
    border-bottom: 2px solid var(--color-bg-medium);
    padding-bottom: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.app-header h2 {
    color: var(--color-primary);
    margin: 0;
    font-size: 1.8em;
}

.year-info {
    font-size: 1.5em;
    color: var(--color-text);
    font-weight: bold;
}

.year-label {
    color: #666;
    font-size: 0.8em;
    font-weight: normal;
}

.year-number {
    color: var(--color-secondary);
    font-size: 1.2em;
}


.simulator-content {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    justify-content: center;
}

.controls-panel {
    flex: 1 1 300px; /* Allows flex item to grow/shrink, basis 300px */
    background-color: var(--color-bg-light);
    padding: 20px;
    border-radius: var(--border-radius);
    box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
    min-width: 300px;
}

.controls-panel h3 {
    text-align: center;
    margin-top: 0;
    color: var(--color-text);
    margin-bottom: 20px;
}

.condition-sliders .slider-group {
    margin-bottom: 25px;
    padding: 10px;
    background-color: #fff;
    border-radius: var(--border-radius);
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.slider-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: var(--color-primary);
    font-size: 1em;
}

.slider-group input[type="range"] {
    width: calc(100% - 60px); /* Adjust width for value span */
    display: inline-block;
    vertical-align: middle;
    -webkit-appearance: none; /* Override default appearance */
    appearance: none;
    height: 8px;
    background: linear-gradient(to right, var(--color-danger) 0%, var(--color-warning) 30%, var(--color-success) 50%, var(--color-warning) 70%, var(--color-danger) 100%); /* Example gradient */
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
    border-radius: 5px;
    outline: none;
    opacity: 0.7;
    transition: opacity .2s ease;
}

.slider-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: var(--color-primary);
    border: 2px solid #fff;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    transition: background 0.3s ease;
}

.slider-group input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: var(--color-primary);
    border: 2px solid #fff;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    transition: background 0.3s ease;
}

.slider-group input[type="range"]:hover {
    opacity: 1;
}

.slider-group .slider-value {
     display: inline-block;
     width: 40px; /* Fixed width for value */
     text-align: center;
     font-weight: bold;
     color: var(--color-text);
     vertical-align: middle;
}

.slider-tip {
    font-size: 0.8em;
    color: #666;
    margin-top: 5px;
    text-align: right;
}

/* Specific gradient adjustments for sliders */
#precipitation::-webkit-slider-runnable-track { background: linear-gradient(to right, var(--color-danger) 0%, var(--color-warning) 20%, var(--color-success) 80%, var(--color-warning) 100%); }
#precipitation::-moz-range-track { background: linear-gradient(to right, var(--color-danger) 0%, var(--color-warning) 20%, var(--color-success) 80%, var(--color-warning) 100%); }

#sunlight::-webkit-slider-runnable-track { background: linear-gradient(to right, var(--color-danger) 0%, var(--color-warning) 20%, var(--color-success) 80%, var(--color-warning) 100%); }
#sunlight::-moz-range-track { background: linear-gradient(to right, var(--color-danger) 0%, var(--color-warning) 20%, var(--color-success) 80%, var(--color-warning) 100%); }

#temperature::-webkit-slider-runnable-track { background: linear-gradient(to right, var(--color-danger) 0%, var(--color-warning) 20%, var(--color-success) 50%, var(--color-warning) 80%, var(--color-danger) 100%); }
#temperature::-moz-range-track { background: linear-gradient(to right, var(--color-danger) 0%, var(--color-warning) 20%, var(--color-success) 50%, var(--color-warning) 80%, var(--color-danger) 100%); }

#pests::-webkit-slider-runnable-track { background: linear-gradient(to right, var(--color-success) 0%, var(--color-warning) 20%, var(--color-danger) 80%, var(--color-danger) 100%); }
#pests::-moz-range-track { background: linear-gradient(to right, var(--color-success) 0%, var(--color-warning) 20%, var(--color-danger) 80%, var(--color-danger) 100%); }


.action-buttons {
    text-align: center;
    margin-top: 20px;
}

button {
    padding: 12px 25px;
    margin: 8px;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1em;
    font-weight: bold;
    transition: transform 0.2s ease-in-out, background-color 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 10px rgba(0,0,0,0.15);
}

button:active {
     transform: translateY(0);
     box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

button.btn-primary {
    background-color: var(--color-primary);
    color: white;
}

button.btn-primary:hover {
    background-color: #3a80d2;
}

button.btn-secondary {
    background-color: var(--color-bg-medium);
    color: var(--color-text);
}

button.btn-secondary:hover {
    background-color: var(--color-bg-dark);
}

button.btn-toggle-explanation {
     display: block;
     width: fit-content;
     margin: 20px auto;
     background-color: #eee;
     color: #333;
     border-radius: var(--border-radius);
     box-shadow: none;
     font-size: 0.9em;
}
button.btn-toggle-explanation:hover {
     background-color: #ddd;
     transform: none;
     box-shadow: none;
}


.visualization-area {
    flex: 1 1 400px; /* Canvas needs space */
    display: flex;
    flex-direction: column;
    align-items: center; /* Center canvas vertically */
    min-width: 400px;
}

.canvas-container {
    position: relative;
    width: 400px;
    height: 400px;
    margin-bottom: 20px;
}

#tree-canvas {
    display: block; /* Remove extra space below canvas */
    border: 2px solid var(--color-core);
    background-color: var(--color-bg-light);
    border-radius: 50%; /* Make it look like a log section */
    box-shadow: var(--box-shadow);
    position: absolute;
    top: 0;
    left: 0;
    animation: appearScale 0.5s ease-out; /* Subtle animation on load/reset */
    transform-origin: center;
}

@keyframes appearScale {
    from { transform: scale(0.8); opacity: 0.6; }
    to { transform: scale(1); opacity: 1; }
}

.canvas-overlay {
     position: absolute;
     top: 0;
     left: 0;
     width: 100%;
     height: 100%;
     border-radius: 50%;
     pointer-events: none; /* Allow clicks to pass through to canvas */
     box-shadow: inset 0 0 20px rgba(0,0,0,0.2); /* Inner shadow for depth */
}


.history {
    width: 100%; /* Take full width in flex container */
    max-height: 200px; /* Reduced height for better layout */
    overflow-y: auto;
    padding: 15px;
    border: 1px solid var(--color-bg-medium);
    border-radius: var(--border-radius);
    background-color: #fff;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
}

.history h4 {
    margin-top: 0;
    color: var(--color-text);
    border-bottom: 1px solid var(--color-bg-light);
    padding-bottom: 10px;
    margin-bottom: 10px;
    text-align: center;
}

.history ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.history li {
    margin-bottom: 10px;
    padding: 8px;
    border-bottom: 1px dashed var(--color-bg-medium);
    font-size: 0.9em;
    color: #555;
    transition: background-color 0.2s ease;
    border-radius: 4px;
}
.history li:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}
.history li:hover {
    background-color: var(--color-bg-light);
}

.history li strong {
    color: var(--color-primary);
}

.growth-summary {
    text-align: center;
    margin-top: 20px;
    padding: 15px;
    border-radius: var(--border-radius);
    background-color: var(--color-bg-light);
    min-height: 1.5em; /* Reserve space */
    color: var(--color-text);
    font-weight: bold;
}


.explanation-section {
    margin-top: 30px;
    padding: 25px;
    border: 1px solid var(--color-bg-medium);
    border-radius: var(--border-radius);
    background-color: #fff;
    box-shadow: var(--box-shadow);
}

.explanation-section h2 {
    color: var(--color-primary);
    border-bottom: 2px solid var(--color-bg-medium);
    padding-bottom: 12px;
    margin-bottom: 20px;
    text-align: center;
    font-size: 1.6em;
}
.explanation-section h3 {
    color: var(--color-secondary);
    margin-top: 25px;
    margin-bottom: 15px;
    font-size: 1.3em;
    border-bottom: 1px dotted var(--color-bg-light);
    padding-bottom: 5px;
}

.explanation-section p,
.explanation-section ul {
    margin-bottom: 15px;
}

.explanation-section p,
.explanation-section li {
    line-height: 1.7;
    color: var(--color-text);
}

.explanation-section ul {
    list-style: disc;
    padding-right: 20px;
}

.explanation-section li {
    margin-bottom: 10px;
}

.explanation-section li strong {
    color: var(--color-primary);
}


.hidden {
    display: none;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .app-container {
        padding: 20px;
    }
    .simulator-content {
        flex-direction: column;
        gap: 20px;
    }
     .controls-panel, .visualization-area {
         min-width: unset;
         width: 100%;
     }
    .app-header {
        flex-direction: column;
        gap: 10px;
    }
    .year-info {
        font-size: 1.2em;
    }

     .canvas-container {
         width: 100%;
         height: auto; /* Adjust height based on width */
         padding-bottom: 100%; /* Maintain aspect ratio */
         position: relative;
     }
    #tree-canvas, .canvas-overlay {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }

    .history {
        max-height: 150px; /* Further reduce height on smaller screens */
    }
}

@media (max-width: 480px) {
    .app-header h2 {
        font-size: 1.5em;
    }
    button {
        width: 100%;
        margin: 5px 0;
    }
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('tree-canvas');
    const ctx = canvas.getContext('2d');
    const currentYearSpan = document.getElementById('current-year');
    const precipitationSlider = document.getElementById('precipitation');
    const sunlightSlider = document.getElementById('sunlight');
    const temperatureSlider = document.getElementById('temperature');
    const pestsSlider = document.getElementById('pests');
    const precipitationValueSpan = document.getElementById('precipitation-value');
    const sunlightValueSpan = document.getElementById('sunlight-value');
    const temperatureValueSpan = document.getElementById('temperature-value');
    const pestsValueSpan = document.getElementById('pests-value');
    const nextYearBtn = document.getElementById('next-year-btn');
    const resetBtn = document.getElementById('reset-btn');
    const yearHistoryList = document.getElementById('year-history-list');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
    const explanationSection = document.getElementById('explanation');
    const growthSummaryDiv = document.getElementById('growth-summary');

    let currentYear = 0;
    let treeRings = []; // Array of {year, conditions, ringWidth, springWoodColor, summerWoodColor, ringSummary}
    const MAX_RADIUS = canvas.width / 2 * 0.9; // Max radius for the rings
    const CENTER_X = canvas.width / 2;
    const CENTER_Y = canvas.height / 2;
    const CORE_RADIUS = 15; // The initial 'pith' or core, slightly larger

    // Function to draw the tree rings
    function drawTree() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw pith/core
        ctx.fillStyle = varToHex('--color-core'); // Using CSS variable
        ctx.beginPath();
        ctx.arc(CENTER_X, CENTER_Y, CORE_RADIUS, 0, Math.PI * 2);
        ctx.fill();

        let currentRadius = CORE_RADIUS;

        // Draw rings from inside out
        treeRings.forEach(ring => {
            const totalRingThickness = ring.ringWidth; // Total width of this year's ring

            // Draw summerwood (darker, inner part of the ring)
            const summerWoodThickness = totalRingThickness * (1 - ring.springWoodRatio);
             if (summerWoodThickness > 0) {
                ctx.fillStyle = ring.summerWoodColor;
                ctx.beginPath();
                ctx.arc(CENTER_X, CENTER_Y, currentRadius + summerWoodThickness, 0, Math.PI * 2);
                ctx.arc(CENTER_X, CENTER_Y, currentRadius, 0, Math.PI * 2, true);
                ctx.fill();
            }
            currentRadius += summerWoodThickness;

            // Draw springwood (lighter, outer part of the ring)
            const springWoodThickness = totalRingThickness * ring.springWoodRatio;
             if (springWoodThickness > 0) {
                ctx.fillStyle = ring.springWoodColor;
                ctx.beginPath();
                ctx.arc(CENTER_X, CENTER_Y, currentRadius + springWoodThickness, 0, Math.PI * 2);
                ctx.arc(CENTER_X, CENTER_Y, currentRadius, 0, Math.PI * 2, true);
                ctx.fill();
             }
            currentRadius += springWoodThickness;
        });

         // Add a subtle border/line between rings for clarity (optional, can be removed if colors create enough contrast)
         currentRadius = CORE_RADIUS; // Reset radius
         ctx.strokeStyle = 'rgba(0,0,0,0.1)'; // Light separator line
         ctx.lineWidth = 0.5;
         treeRings.forEach(ring => {
             const totalRingThickness = ring.ringWidth;
             currentRadius += totalRingThickness; // Move to the outer edge of the current ring
             ctx.beginPath();
             ctx.arc(CENTER_X, CENTER_Y, currentRadius, 0, Math.PI * 2);
             ctx.stroke();
         });

        // Trigger animation on canvas
        canvas.style.animation = 'none'; // Reset animation
        canvas.offsetHeight; // Trigger reflow
        canvas.style.animation = 'appearScale 0.5s ease-out'; // Re-apply animation
    }

    // Function to calculate ring properties based on conditions
    function calculateRingProperties(conditions) {
        const { precipitation, sunlight, temperature, pests } = conditions;

        // Influence of factors on growth rate (0 to 1 scale, 10 is best/worst)
        // Precipitation: strong positive influence, non-linear (low precip is very bad)
        const precipFactor = Math.pow(precipitation / 10, 1.5); // Exponential effect for low values

        // Sunlight: positive influence
        const sunFactor = sunlight / 10;

        // Temperature: peaks around 5, drops off at extremes
        const tempFactor = 1 - Math.pow(Math.abs(temperature - 5) / 5, 2); // Quadratic drop-off

        // Pests: negative influence, non-linear (high pests are very bad)
        const pestFactor = 1 - Math.pow((pests - 1) / 9, 2); // Exponential effect for high values

        // Combine factors - treat precipitation and pests as potential bottlenecks
        // Growth is limited by the minimum of key resources (water, light, suitable temp) AND limited by damage (pests)
        let resourceFactor = Math.min(precipFactor, sunFactor, tempFactor); // Simplified bottleneck logic
        let growthFactor = resourceFactor * pestFactor;

        // Ensure minimum growth even in bad conditions, but severe conditions should significantly limit
        growthFactor = Math.max(0.01, growthFactor); // Absolute minimum

        // Calculate available space and base ring width
        const currentTotalRadius = CORE_RADIUS + treeRings.reduce((sum, r) => sum + r.ringWidth, 0);
        const remainingRadius = MAX_RADIUS - currentTotalRadius;
        const potentialMaxRing = remainingRadius / (30 - currentYear); // Heuristic to ensure space for future years

        let ringWidth = growthFactor * potentialMaxRing * 2; // Scale growth factor to a potential width

        // Cap ring width to prevent overflowing canvas quickly, but allow wide rings
        ringWidth = Math.min(ringWidth, MAX_RADIUS / 15); // Cap max width per year

        // Adjust springwood/summerwood ratio
        // Good conditions (high water/sun, moderate temp) favour springwood formation (larger, thinner cells)
        // Poor conditions (low water/sun, extreme temp) favour summerwood (smaller, thicker cells)
        let springWoodRatio = (precipFactor * 0.5 + sunFactor * 0.3 + (1 - Math.abs(temperature - 5)/5) * 0.2); // More weight on water
        springWoodRatio = Math.min(0.7, Math.max(0.3, springWoodRatio)); // Ratio between 30% and 70%

        // Colors - more yellow/light brown for springwood, darker brown for summerwood
        const baseSpringColor = varToHex('--color-ring-spring');
        const baseSummerColor = varToHex('--color-ring-summer');

        // Simple color variation based on ratio
        const springColor = interpolateColor(baseSpringColor, '#ffebcd', springWoodRatio); // Lighter towards higher ratio
        const summerColor = interpolateColor(baseSummerColor, '#654321', 1 - springWoodRatio); // Darker towards lower ratio

         // Determine growth summary
         let growthSummary = '';
         if (ringWidth < MAX_RADIUS / 60) {
             growthSummary = ' (גדילה דלה מאוד)';
         } else if (ringWidth < MAX_RADIUS / 40) {
             growthSummary = ' (גדילה מועטה)';
         } else if (ringWidth < MAX_RADIUS / 25) {
             growthSummary = ' (גדילה ממוצעת)';
         } else {
             growthSummary = ' (גדילה משמעותית!)';
         }


        return {
            ringWidth: ringWidth,
            springWoodRatio: springWoodRatio,
            springWoodColor: springColor,
            summerWoodColor: summerColor,
            ringSummary: growthSummary
        };
    }

    // Helper: Get CSS variable color
    function varToHex(variable) {
         const style = getComputedStyle(document.documentElement);
         return style.getPropertyValue(variable).trim();
    }

    // Helper function for color interpolation
    function interpolateColor(color1, color2, factor) {
        const c1 = hexToRgb(color1);
        const c2 = hexToRgb(color2);
        const result = c1.map((c, i) => Math.round(c + factor * (c2[i] - c)));
        return rgbToHex(result);
    }

    function hexToRgb(hex) {
        const bigint = parseInt(hex.slice(1), 16);
        const r = (bigint >> 16) & 255;
        const g = (bigint >> 8) & 255;
        const b = bigint & 255;
        return [r, g, b];
    }

    function rgbToHex(rgb) {
        return '#' + rgb.map(x => {
            const hex = x.toString(16);
            return hex.length === 1 ? '0' + hex : hex;
        }).join('');
    }


    // Function to advance to the next year
    function nextYear() {
        currentYear++;
        currentYearSpan.textContent = currentYear;

        const conditions = {
            precipitation: parseInt(precipitationSlider.value),
            sunlight: parseInt(sunlightSlider.value),
            temperature: parseInt(temperatureSlider.value),
            pests: parseInt(pestsSlider.value)
        };

        // Check if we have enough space to grow another ring
        const currentTotalRadius = CORE_RADIUS + treeRings.reduce((sum, r) => sum + r.ringWidth, 0);
        if (currentTotalRadius >= MAX_RADIUS - 5) { // Add a small buffer
             const finalSummary = `העץ הגיע לגודל המקסימלי בסימולציה זו לאחר ${currentYear -1} שנים! התחל עץ חדש כדי לנסות תנאים אחרים.`;
             growthSummaryDiv.textContent = finalSummary;
             growthSummaryDiv.style.color = varToHex('--color-primary');
             nextYearBtn.disabled = true; // Disable button
             return;
        }

        const ringProperties = calculateRingProperties(conditions);

        treeRings.push({
            year: currentYear,
            conditions: conditions,
            ...ringProperties // Spread ring properties
        });

        drawTree();
        updateHistory(currentYear, conditions, ringProperties);
        updateGrowthSummary(ringProperties);

        // Reset sliders to default (average) for the next year, or maybe keep them?
        // Let's keep them so user can tweak from current year's settings.
        // resetSliders(); // Optional: uncomment to reset sliders each year
    }

    // Function to reset the simulation
    function resetSimulation() {
        currentYear = 0;
        treeRings = [];
        currentYearSpan.textContent = currentYear;
        growthSummaryDiv.textContent = ''; // Clear summary
        growthSummaryDiv.style.color = varToHex('--color-text'); // Reset color
        drawTree(); // Draw initial empty state (just core)
        resetSliders();
        resetHistory();
        nextYearBtn.disabled = false; // Enable button
    }

    // Reset sliders to default value
    function resetSliders() {
         precipitationSlider.value = 5;
         sunlightSlider.value = 5;
         temperatureSlider.value = 5;
         pestsSlider.value = 1; // Pests default to low
         updateSliderValues();
    }

    // Update slider value displays
    function updateSliderValues() {
        precipitationValueSpan.textContent = precipitationSlider.value;
        sunlightValueSpan.textContent = sunlightSlider.value;
        temperatureValueSpan.textContent = temperatureSlider.value;
        pestsValueSpan.textContent = pestsSlider.value;
    }

    // Update history list
    function updateHistory(year, conditions, ringProperties) {
        if (year === 1) {
            yearHistoryList.innerHTML = ''; // Clear initial state
        }
        const listItem = document.createElement('li');
         const conditionsText = `גשם: ${conditions.precipitation}/10, שמש: ${conditions.sunlight}/10, טמפ': ${conditions.temperature}/10, מזיקים: ${conditions.pests}/10`;
        listItem.innerHTML = `
            <strong>שנה ${year}:</strong> ${conditionsText} ${ringProperties.ringSummary}
        `;
        yearHistoryList.appendChild(listItem);
        yearHistoryList.scrollTop = yearHistoryList.scrollHeight; // Scroll to bottom
    }

    // Update growth summary text
    function updateGrowthSummary(ringProperties) {
        let summaryText = `<strong>בשנה ${currentYear}</strong>: גדילת הטבעת הייתה ${ringProperties.ringSummary.replace(/[()]/g, '').trim()}.`;
        if (ringProperties.ringSummary.includes('משמעותית')) {
             growthSummaryDiv.style.color = varToHex('--color-success');
        } else if (ringProperties.ringSummary.includes('דלה')) {
            growthSummaryDiv.style.color = varToHex('--color-danger');
        } else {
             growthSummaryDiv.style.color = varToHex('--color-text');
        }
         growthSummaryDiv.innerHTML = summaryText;
    }


    // Reset history list
    function resetHistory() {
        yearHistoryList.innerHTML = '<li>בחר תנאים לשנה הראשונה...</li>';
    }


    // Event listeners
    nextYearBtn.addEventListener('click', nextYear);
    resetBtn.addEventListener('click', resetSimulation);

    precipitationSlider.addEventListener('input', updateSliderValues);
    sunlightSlider.addEventListener('input', updateSliderValues);
    temperatureSlider.addEventListener('input', updateSliderValues);
    pestsSlider.addEventListener('input', updateSliderValues);

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationSection.classList.contains('hidden');
        explanationSection.classList.toggle('hidden', !isHidden); // Toggle hidden class
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'הצג/הסתר הסבר על טבעות גדילה';
    });

    // Initial setup
    resetSimulation(); // Start in the initial state
});
</script>
---