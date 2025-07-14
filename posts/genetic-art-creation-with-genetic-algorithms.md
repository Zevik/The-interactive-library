---
title: "אמנות גנטית: כשקוד הופך לאמן"
english_slug: genetic-art-creation-with-genetic-algorithms
category: "מדעי המחשב"
tags: [אלגוריתמים גנטיים, אבולוציה חישובית, אמנות גנרטיבית, בינה מלאכותית, יצירתיות חישובית]
---
# אמנות גנטית: כשקוד הופך לאמן

דמיינו שהקוד שכתבתם לא רק מבצע הוראות, אלא ממש 'יוצר' משהו חדש לגמרי, בלי שתגידו לו מראש איך התוצאה צריכה להיראות. דמיינו שהתהליך דומה יותר לאבולוציה ביולוגית מאשר לתוכנית מפורטת. בואו נצלול לעולם המרתק של אמנות גנטית, שם "גנים דיגיטליים" ותהליך של "הישרדות המתאימים ביותר" מולידים דימויים ויזואליים מפתיעים, דור אחר דור.

זו לא רק תיאוריה – זו סימולציה אינטראקטיבית בה אתם שולטים. צפו איך אוסף אקראי של צורות מתפתח בהדרגה ליצירת אמנות שדומה לתמונת יעד שתבחרו, ממש לנגד עיניכם.

<div id="genetic-art-app" class="app-container">
    <div class="canvases-area">
        <div class="canvas-container">
            <h3>תמונת יעד: המטרה האבולוציונית</h3>
            <canvas id="targetCanvas" width="200" height="200"></canvas>
             <input type="file" id="uploadTargetBtn" accept="image/*" class="upload-button">
             <label for="uploadTargetBtn" class="upload-label">או העלו תמונת יעד משלכם</label>
        </div>
        <div class="canvas-container">
            <h3>היצירה המתפתחת: הפרט ה'טוב' ביותר בכל דור</h3>
            <canvas id="evolvedCanvas" width="200" height="200"></canvas>
        </div>
    </div>

    <div class="controls-area">
        <div class="status-bar">
            <p id="status">טוען את הסטודיו הגנטי...</p>
        </div>

        <div class="param-controls">
             <div class="control-group">
                 <label for="populationSize">גודל אוכלוסייה:</label>
                 <input type="range" id="populationSize" min="10" max="100" value="30">
                 <span id="populationSizeValue">30</span>
             </div>
             <div class="control-group">
                 <label for="maxPolygons">מקסימום 'צורות' לציור:</label>
                 <input type="range" id="maxPolygons" min="10" max="300" value="100">
                  <span id="maxPolygonsValue">100</span>
             </div>
             <div class="control-group">
                 <label for="mutationRate">קצב מוטציה (סבירות שינוי גן):</label>
                 <input type="range" id="mutationRate" min="0.001" max="0.1" value="0.02" step="0.001">
                 <span id="mutationRateValue">0.02</span>
             </div>
        </div>

        <button id="startStopBtn" class="action-button">התחל את האבולוציה!</button>
         <button id="resetBtn" class="secondary-button">אתחל הכל</button>
    </div>

</div>

<style>
/* General body and container styling */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f8f8;
    margin: 0;
    padding: 20px;
    direction: rtl; /* Ensure RTL direction */
    text-align: right;
}

h1, h2, h3 {
    color: #0056b3; /* A nice blue */
    text-align: center;
    margin-bottom: 20px;
}

/* App Container */
.app-container {
    background-color: #fff;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    margin: 20px auto;
    max-width: 800px; /* Limit width for better readability */
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Canvas Area */
.canvases-area {
    display: flex;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
    justify-content: center; /* Center canvases */
    gap: 30px; /* Space between canvases */
    margin-bottom: 30px;
}

.canvas-container {
    text-align: center;
    background-color: #f0f0f0; /* Light background for canvas area */
    padding: 15px;
    border-radius: 8px;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); /* Inner shadow */
    position: relative; /* For positioning upload label */
}

.canvas-container h3 {
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.2em;
    color: #555;
}

canvas {
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: white; /* Ensure canvases are white initially */
    display: block; /* Remove extra space below canvas */
    margin: 0 auto; /* Center canvas within its container */
}

/* File Upload Styling */
.upload-button {
    display: none; /* Hide the actual file input */
}

.upload-label {
    display: inline-block;
    background-color: #e9e9e9; /* Light grey button */
    color: #333;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
    font-size: 0.9em;
    transition: background-color 0.3s ease;
}

.upload-label:hover {
    background-color: #d9d9d9;
}


/* Controls Area */
.controls-area {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
}

.status-bar {
    font-size: 1.1em;
    color: #0056b3;
    font-weight: bold;
    min-height: 1.5em; /* Reserve space */
}

.param-controls {
    width: 100%;
    max-width: 500px; /* Limit width of controls */
}

.control-group {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    gap: 10px;
}

.control-group label {
    flex-basis: 150px; /* Fixed width for labels */
    font-weight: bold;
    text-align: left; /* Align labels to the right */
}

.control-group input[type="range"] {
    flex-grow: 1; /* Take available space */
    direction: ltr; /* Ensure slider direction is LTR */
}

.control-group span {
    flex-basis: 40px; /* Fixed width for value display */
    text-align: center;
    font-weight: normal;
}

/* Buttons */
.action-button, .secondary-button {
    padding: 12px 25px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

.action-button {
    background-color: #28a745; /* Green for start/stop */
    color: white;
}

.action-button:hover {
    background-color: #218838;
}

.action-button:active {
    transform: scale(0.98);
}

.secondary-button {
    background-color: #dc3545; /* Red for reset */
    color: white;
    margin-top: 10px; /* Space below main button */
}

.secondary-button:hover {
    background-color: #c82333;
}

.secondary-button:active {
    transform: scale(0.98);
}


/* Explanation Section */
#toggleExplanationBtn {
    display: block;
    margin: 30px auto 20px;
    padding: 10px 20px;
    border: 1px solid #007bff;
    background-color: #e9f5ff; /* Light blue background */
    color: #007bff; /* Blue text */
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, border-color 0.3s ease;
}

#toggleExplanationBtn:hover {
    background-color: #cce5ff;
    border-color: #0056b3;
}

#explanation {
    margin-top: 30px;
    padding: 25px;
    border: 1px solid #ddd;
    background-color: #fefefe;
    border-radius: 8px;
    display: none; /* Hidden by default */
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

#explanation h2 {
    color: #0056b3;
    border-bottom: 2px solid #0056b3;
    padding-bottom: 10px;
    margin-bottom: 20px;
    text-align: right;
}

#explanation h3 {
    color: #555;
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: right;
}

#explanation p, #explanation ul, #explanation ol {
    line-height: 1.7;
    margin-bottom: 15px;
    text-align: right;
}

#explanation ul, #explanation ol {
    padding-right: 25px; /* RTL list padding */
}

#explanation li {
    margin-bottom: 8px;
}

#explanation strong {
    color: #000; /* Make key terms stand out */
}

/* Responsive adjustments */
@media (max-width: 600px) {
    .canvases-area {
        flex-direction: column; /* Stack canvases */
        gap: 20px;
    }

    .canvas-container {
        width: 100%; /* Full width on small screens */
        padding: 10px;
    }

    canvas {
        width: 100% !important; /* Make canvas responsive */
        height: auto !important;
    }

    .control-group {
        flex-direction: column;
        align-items: flex-start;
        gap: 5px;
    }

    .control-group label {
        flex-basis: auto;
        width: 100%;
        text-align: right;
    }

     .control-group span {
         width: 100%;
         text-align: right;
         font-size: 0.9em; /* Smaller text for value */
     }

    .param-controls, .controls-area {
        max-width: 100%;
    }

    .action-button, .secondary-button, #toggleExplanationBtn {
         width: 100%;
         padding: 10px;
         font-size: 1em;
    }
}

</style>

<button id="toggleExplanationBtn">הצגת/הסתרת מסע אל תוך הקוד והאבולוציה</button>

<div id="explanation">
    <h2>מסע אל תוך הקוד והאבולוציה: איך זה עובד?</h2>

    <p>הסימולציה שראיתם היא יישום חי של <strong>אלגוריתם גנטי (Genetic Algorithm - GA)</strong>. זו טכניקת פתרון בעיות גאונית שמחקה את תהליך האבולוציה הביולוגית הטבעית. במקום לתת למחשב הוראות צעד-אחר-צעד איך לצייר תמונה, אנחנו נותנים לו אוסף כלים בסיסיים (צורות גאומטריות שקופות במקרה שלנו) ותמונת יעד, ומאפשרים לו 'לגלות' בעצמו איך להגיע אליה באמצעות תהליך של ניסוי, שגיאה, רבייה, ומוטציה.</p>

    <h3>למה בכלל להשתמש ב-GA?</h3>
    <p>אלגוריתמים גנטיים מצטיינים בפתרון בעיות שקשה (או בלתי אפשרי) לפתור בשיטות אלגוריתמיות קלאסיות. בעיות כאלה מאופיינות לרוב במרחב פתרונות עצום, או בכאלה שבהן הדרך לפתרון האופטימלי אינה ברורה. במקום לחפש את הפתרון בצורה שיטתית או אקראית לחלוטין, GA מנווט את החיפוש בצורה מושכלת, מעדיף פתרונות שנראים מבטיחים יותר, וכך מוצא פתרונות טובים (לרוב לאו דווקא הפתרון ה*מושלם* היחיד, אבל פתרון *טוב מאוד*) בזמן סביר.</p>
    <p>מעבר לאמנות גנרטיבית, GA משמשים גם ב:</p>
    <ul>
        <li>אופטימיזציה (מציאת התצורה הטובה ביותר של מערכת מורכבת).</li>
        <li>תכנון וניהול לוחות זמנים (טיסות, ייצור).</li>
        <li>עיצוב הנדסי (מבנים, אנטנות).</li>
        <li>בינה מלאכותית ולמידת מכונה.</li>
        <li>פיתוח אסטרטגיות במשחקים.</li>
    </ul>

    <h3>ה'ביולוגיה' של האלגוריתם הגנטי: מונחי מפתח</h3>
    <p>כדי להבין איך האלגוריתם עובד, נכיר כמה מושגים בהשראת עולם החי:</p>
    <ul>
        <li><strong>אוכלוסייה (Population):</strong> קבוצה של פתרונות אפשריים לבעיה. בסימולציה שלנו, זו קבוצה של ציורים שונים. גודל האוכלוסייה הוא פרמטר חשוב שניתן לשלוט עליו. אוכלוסייה גדולה יותר מגדילה את הסיכוי למצוא פתרון טוב, אך דורשת יותר כוח חישוב.</li>
        <li><strong>פרט (Individual):</strong> פתרון יחיד באוכלוסייה. אצלנו, כל ציור הוא 'פרט'.</li>
        <li><strong>כרומוזום (Chromosome):</strong> הייצוג המקודד של הפרט. באמנות גנטית, הכרומוזום הוא רשימה של "גנים" שמתארים את הציור.</li>
        <li><strong>גן (Gene):</strong> יחידת מידע בסיסית בכרומוזום. כאן, גן יחיד מתאר צורה גאומטרית אחת (למשל, משולש שקוף) עם כל המאפיינים שלה: קואורדינטות הנקודות שלו, הצבע (RGB) ורמת השקיפות (Alpha). הציור כולו הוא אוסף של גנים כאלה המצוירים זה על גבי זה.</li>
        <li><strong>התאמה (Fitness):</strong> מדד איכות שמכמת עד כמה פרט מסוים הוא 'טוב' כפתרון לבעיה. אצלנו, פונקציית ההתאמה משווה את הציור שנוצר (על ידי ציור כל ה'גנים' על קנבס) לתמונת היעד, ומעניקה ציון גבוה יותר לציורים שדומים יותר ליעד (למשל, על ידי חישוב סכום הבדלי הצבעים בין הפיקסלים בכל שתי התמונות). ככל שהציור דומה יותר, ציון ההתאמה גבוה יותר.</li>
    </ul>

    <h3>המחזור האבולוציוני: דור אחר דור</h3>
    <p>האלגוריתם פועל במחזורים חוזרים הנקראים <strong>דורות (Generations)</strong>:</p>
    <ol>
        <li>
            <h4>אתחול (Initialization)</h4>
            <p>התחלנו עם אוכלוסייה של ציורים אקראיים לחלוטין. כל ציור מכיל מספר אקראי של צורות אקראיות (מיקום, צבע, שקיפות).</p>
        </li>
        <li>
            <h4>הערכת התאמה (Fitness Evaluation)</h4>
            <p>לכל ציור באוכלוסייה מחושב ציון התאמה - כמה הוא דומה לתמונת היעד. זה השלב שדורש לרוב את מירב החישוב.</p>
        </li>
        <li>
            <h4>סלקציה (Selection)</h4>
            <p>על בסיס ציוני ההתאמה, בוחרים "הורים" מהאוכלוסייה הנוכחית שישמשו ליצירת הדור הבא. הורים עם ציוני התאמה גבוהים יותר (ציורים דומים יותר ליעד) מקבלים סיכוי גבוה יותר להיבחר. בסימולציה שלנו, אנו משתמשים בשיטת "סלקציית טורניר" פשוטה.</p>
        </li>
        <li>
            <h4>רבייה (Crossover / Crossover)</h4>
            <p>ההורים הנבחרים "מרביעים" את ה"כרומוזומים" שלהם כדי ליצור "צאצאים". בפועל, זה אומר שמשלבים את רשימות הצורות (הגנים) משני הורים ליצירת רשימת צורות חדשה עבור הציור-צאצא. הצאצא יירש מאפיינים משני ההורים.</p>
        </li>
        <li>
            <h4>מוטציה (Mutation)</h4>
            <p>לאחר הרבייה (ולעיתים גם לפני), לכל צאצא יש סיכוי קטן לעבור שינוי אקראי באחד או יותר מהגנים שלו. מוטציה יכולה לשנות את מיקום נקודות הצורה, צבעה, שקיפותה, ואף להוסיף או להסיר צורות שלמות. המוטציה מכרחית להזרקת "רעננות" גנטית לאוכלוסייה, למניעת "קיפאון" על פתרון מסוים, ולאפשר לאלגוריתם לחקור פתרונות חדשים שאולי לא היו ניתנים להשגה רק מרבייה של הורים קיימים.</p>
        </li>
        <li>
            <h4>יצירת הדור הבא (Next Generation)</h4>
            <p>הצאצאים שנוצרו (לאחר רבייה ומוטציה) מרכיבים את האוכלוסייה החדשה. האלגוריתם חוזר לשלב 2, ומעריך את ההתאמה של הדור החדש. התהליך ממשיך דור אחר דור, כאשר לאורך זמן, הציורים באוכלוסייה (ובמיוחד הציור ה"טוב" ביותר, המוצג בצד שמאל) הופכים להיות דומים יותר ויותר לתמונת היעד.</p>
        </li>
        <li>
            <h4>קריטריון עצירה (Stopping Condition)</h4>
            <p>התהליך ממשיך עד שמתקיים אחד מהתנאים: הושגה התאמה מספקת, עבר מספר מקסימלי של דורות, או שאין שיפור משמעותי בציון ההתאמה לאורך זמן.</p>
    </ol>

    <h3>הפרמטרים שמשנים את המשחק (ואת האמנות!)</h3>
    <p>בסימולציה למעלה, אתם יכולים לשחק עם מספר פרמטרים. כל פרמטר משפיע באופן דרמטי על האבולוציה האמנותית:</p>
    <ul>
        <li><strong>גודל אוכלוסייה:</strong> כמה ציורים שונים "מתחרים" בכל דור. אוכלוסייה גדולה יותר מאפשרת מגוון גנטי רחב יותר וסיכוי גבוה יותר למצוא פתרונות טובים, אך הסימולציה תרוץ לאט יותר.</li>
        <li><strong>מקסימום 'צורות' לציור:</strong> כמה "גנים" (משולשים שקופים) לכל היותר יכולים להיות בציור אחד. מספר גבוה יותר מאפשר לציור להיות מורכב ומפורט יותר, וקרוב יותר ליעד, אך דורש יותר זמן חישוב וגם יכול להוביל ל"עומס גנטי" שמעכב את ההתקדמות.</li>
        <li><strong>קצב מוטציה:</strong> הסיכוי שגן בודד יעבור שינוי אקראי. קצב מוטציה גבוה מידי עלול להפוך את התהליך לאקראי מדי ולמנוע התכנסות. קצב נמוך מדי עלול לגרום לאוכלוסייה "להיתקע" על פתרון מקומי לא אופטימלי מבלי למצוא פתרונות טובים יותר.</li>
    </ul>
    <p>נסו לשנות את הפרמטרים ולראות איך זה משפיע על מהירות ההתפתחות והאיכות הסופית של היצירה!</p>

    <h3>היופי שבאקראיות מודרכת</h3>
    <p>אמנות גנטית היא דוגמה מרהיבה ליכולת של אלגוריתמים פשוטים, בהינתן מספיק זמן וכוח חישוב, ליצור מורכבות מפתיעה. היא מדגימה כיצד תהליכים המבוססים על עקרונות אבולוציוניים יכולים להוות כלי רב עוצמה לפתרון בעיות, וגם לשמש כמקור ליצירתיות חישובית, שבה המחשב אינו רק כלי ביד האמן, אלא שותף לתהליך היצירה.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const targetCanvas = document.getElementById('targetCanvas');
    const evolvedCanvas = document.getElementById('evolvedCanvas');
    const statusDiv = document.getElementById('status');
    const startStopBtn = document.getElementById('startStopBtn');
    const resetBtn = document.getElementById('resetBtn');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const uploadTargetBtn = document.getElementById('uploadTargetBtn');

    // Parameter controls
    const populationSizeSlider = document.getElementById('populationSize');
    const populationSizeValueSpan = document.getElementById('populationSizeValue');
    const maxPolygonsSlider = document.getElementById('maxPolygons');
    const maxPolygonsValueSpan = document.getElementById('maxPolygonsValue');
    const mutationRateSlider = document.getElementById('mutationRate');
    const mutationRateValueSpan = document.getElementById('mutationRateValue');


    const ctxTarget = targetCanvas.getContext('2d');
    const ctxEvolved = evolvedCanvas.getContext('2d');

    const WIDTH = targetCanvas.width;
    const HEIGHT = targetCanvas.height;

    // --- Genetic Algorithm Parameters ---
    // These will be updated by sliders
    let POPULATION_SIZE = parseInt(populationSizeSlider.value);
    let MAX_POLYGONS = parseInt(maxPolygonsSlider.value);
    let MUTATION_RATE = parseFloat(mutationRateSlider.value);

    const ADD_POLYGON_PROB = 0.05; // Probability of adding a new polygon during mutation
    const REMOVE_POLYGON_PROB = 0.02; // Probability of removing a polygon during mutation
    const POLYGON_VERTICES = 3; // Number of vertices per polygon (triangle)
    const TOURNAMENT_SIZE = 3; // For selection

    let population = [];
    let targetImageData;
    let running = false;
    let generation = 0;
    let animationFrameId;
    let bestFitness = 0;
    let bestIndividual = [];

    // --- Helper Functions ---

    // Creates a random polygon (gene)
    function createRandomPolygon() {
        const points = [];
        for (let i = 0; i < POLYGON_VERTICES; i++) {
            points.push({
                x: Math.random() * WIDTH,
                y: Math.random() * HEIGHT
            });
        }
        const color = {
            r: Math.floor(Math.random() * 256),
            g: Math.floor(Math.random() * 256),
            b: Math.floor(Math.random() * 256),
            a: Math.random() * 0.3 + 0.1 // Start with low transparency
        };
        return { points, color };
    }

    // Draws a set of polygons (an individual) onto a context
    function drawIndividual(ctx, individual) {
        ctx.fillStyle = 'black'; // Start with a black background (or white, depends on desired effect)
        ctx.fillRect(0, 0, WIDTH, HEIGHT);
        // Draw polygons in order
        individual.forEach(polygon => {
            ctx.fillStyle = `rgba(${polygon.color.r},${polygon.color.g},${polygon.color.b},${polygon.color.a})`;
            ctx.beginPath();
            // Draw polygon shape
            if (polygon.points && polygon.points.length >= 2) {
                 ctx.moveTo(polygon.points[0].x, polygon.points[0].y);
                 for (let i = 1; i < polygon.points.length; i++) {
                     ctx.lineTo(polygon.points[i].x, polygon.points[i].y);
                 }
                 ctx.closePath();
                 ctx.fill();
            }
        });
    }

     // Calculates fitness by comparing pixel data
    // Uses sum of squared differences (SSD) or sum of absolute differences (SAD). SSD is common.
    // Lower difference = higher fitness
    function calculateFitness(individual) {
        if (!targetImageData) return 0; // Cannot calculate fitness without a target

        const tempCanvas = document.createElement('canvas');
        tempCanvas.width = WIDTH;
        tempCanvas.height = HEIGHT;
        const tempCtx = tempCanvas.getContext('2d');
        drawIndividual(tempCtx, individual); // Draw the individual to the temporary canvas
        const evolvedImageData = tempCtx.getImageData(0, 0, WIDTH, HEIGHT).data;

        let diffSum = 0;
        for (let i = 0; i < targetImageData.length; i += 4) {
            // Calculate squared difference for R, G, B
            diffSum += Math.pow(targetImageData[i] - evolvedImageData[i], 2);     // Red
            diffSum += Math.pow(targetImageData[i + 1] - evolvedImageData[i + 1], 2); // Green
            diffSum += Math.pow(targetImageData[i + 2] - evolvedImageData[i + 2], 2); // Blue
            // Alpha difference can also be included but often complicates things visually. Let's ignore for now.
        }

        // Fitness is inverse of the difference sum (lower diff = higher fitness)
        // Add 1 to avoid division by zero if diffSum is 0 (perfect match)
        // Using 1 / (1 + diffSum) results in fitness values between 0 and 1.
        // A large constant factor can scale this up, but 1/(1+diff) is standard.
        return 1 / (1 + diffSum);
    }

    // Tournament selection: Pick k random individuals and return the best one
    function selectParent(populationWithFitness) {
        let best = null;
        for (let i = 0; i < TOURNAMENT_SIZE; i++) {
            const randomIndex = Math.floor(Math.random() * populationWithFitness.length);
            const contestant = populationWithFitness[randomIndex];
            if (!best || contestant.fitness > best.fitness) {
                best = contestant;
            }
        }
        // Return a deep copy of the individual to avoid modifying parents
        return JSON.parse(JSON.stringify(best.individual));
    }

    // Simple crossover: Create a child by taking a random number of polygons from parent1
    // and the rest from parent2. Order is maintained.
    function crossover(parent1, parent2) {
        const child = [];
        const splitPoint = Math.floor(Math.random() * Math.max(parent1.length, parent2.length));

        for (let i = 0; i < splitPoint; i++) {
             if (i < parent1.length) {
                 child.push(JSON.parse(JSON.stringify(parent1[i])));
             }
        }
         for (let i = splitPoint; i < Math.max(parent1.length, parent2.length); i++) {
             if (i < parent2.length) {
                 child.push(JSON.parse(JSON.stringify(parent2[i])));
             }
         }

         // Optional: Shuffle layers slightly? Adds complexity. Keep simple for now.

        // Ensure child doesn't exceed MAX_POLYGONS
         while (child.length > MAX_POLYGONS) {
             // Remove a random polygon if over limit
             child.splice(Math.floor(Math.random() * child.length), 1);
         }
         // Ensure child has at least one polygon
         if (child.length === 0) {
             child.push(createRandomPolygon());
         }


        return child;
    }

    // Mutation: random changes to polygons, or adding/removing polygons
    function mutate(individual) {
        // Maybe add a new polygon (gene)
        if (individual.length < MAX_POLYGONS && Math.random() < ADD_POLYGON_PROB) {
            // Add at a random position in the list (affects drawing order)
            individual.splice(Math.floor(Math.random() * (individual.length + 1)), 0, createRandomPolygon());
        }

        // Maybe remove a polygon (gene)
        if (individual.length > 1 && Math.random() < REMOVE_POLYGON_PROB) {
             individual.splice(Math.floor(Math.random() * individual.length), 1);
        }

        // Mutate existing polygons
        individual.forEach(polygon => {
            // Only apply mutation with MUTATION_RATE probability per polygon
            if (Math.random() < MUTATION_RATE) {
                // Mutate points (small random move)
                polygon.points.forEach(point => {
                    if (Math.random() < 0.7) point.x += (Math.random() - 0.5) * 20; // More likely to mutate
                    if (Math.random() < 0.7) point.y += (Math.random() - 0.5) * 20; // More likely to mutate
                    // Clamp points to canvas bounds
                    point.x = Math.max(0, Math.min(WIDTH, point.x));
                    point.y = Math.max(0, Math.min(HEIGHT, point.y));
                });

                // Mutate color and alpha
                if (Math.random() < 0.7) polygon.color.r = Math.max(0, Math.min(255, polygon.color.r + Math.floor((Math.random() - 0.5) * 60))); // Larger potential change
                if (Math.random() < 0.7) polygon.color.g = Math.max(0, Math.min(255, polygon.color.g + Math.floor((Math.random() - 0.5) * 60))); // Larger potential change
                if (Math.random() < 0.7) polygon.color.b = Math.max(0, Math.min(255, polygon.color.b + Math.floor((Math.random() - 0.5) * 60))); // Larger potential change
                if (Math.random() < 0.7) polygon.color.a = Math.max(0.05, Math.min(0.5, polygon.color.a + (Math.random() - 0.5) * 0.15)); // Mutate alpha more significantly within lower range
            }

            // Small chance to reorder polygon (change layer)
            if (individual.length > 1 && Math.random() < 0.01) {
                 const oldIndex = individual.indexOf(polygon);
                 const newIndex = Math.floor(Math.random() * individual.length);
                 // Remove and re-insert at new position
                 const [movedPolygon] = individual.splice(oldIndex, 1);
                 individual.splice(newIndex, 0, movedPolygon);
            }
        });
    }

    // Create the next generation
    function nextGeneration(currentPopulation) {
        if (!targetImageData) {
            statusDiv.textContent = 'אנא הגדירו תמונת יעד לפני ההתחלה.';
            running = false;
            startStopBtn.textContent = 'התחל את האבולוציה!';
            cancelAnimationFrame(animationFrameId);
            return [];
        }

        // 1. Evaluate fitness for the current population
        const populationWithFitness = currentPopulation.map(individual => ({
            individual: individual,
            fitness: calculateFitness(individual)
        }));

        // Sort by fitness descending
        populationWithFitness.sort((a, b) => b.fitness - a.fitness);

        // Update best fitness and individual if current best is better
        if (populationWithFitness.length > 0) {
            if (populationWithFitness[0].fitness > bestFitness) {
                bestFitness = populationWithFitness[0].fitness;
                // Deep copy the best individual
                bestIndividual = JSON.parse(JSON.stringify(populationWithFitness[0].individual));
                // Immediately draw the new best
                drawIndividual(ctxEvolved, bestIndividual);

                // Update status display
                const diff = (1 / bestFitness) - 1; // Calculate difference from fitness
                // A perfect match gives diff = 0. Let's express similarity as a percentage
                // Total possible diff is max_rgb_diff * 3 * width * height = 255 * 3 * 200 * 200 = 30,600,000
                // Fitness is 1 / (1 + diff). Max fitness is 1 (diff=0). Min fitness approaches 0 for huge diff.
                // Let's show the difference itself, or fitness scaled.
                 // Raw diff is more intuitive: Lower is better. Max possible diff is (255*2)^2 * 3 * 200 * 200 roughly.
                 // Let's show the inverse fitness, which is 1 + diff. Smaller is better.
                 const inverseFitness = 1 / bestFitness; // This value is 1 + sum(sq differences)
                 // Or maybe just show the diffSum itself? That's the most direct measure.
                 // Let's recalculate diffSum directly for display.
                 const tempCanvas = document.createElement('canvas');
                 tempCanvas.width = WIDTH;
                 tempCanvas.height = HEIGHT;
                 const tempCtx = tempCanvas.getContext('2d');
                 drawIndividual(tempCtx, bestIndividual);
                 const evolvedImageData = tempCtx.getImageData(0, 0, WIDTH, HEIGHT).data;

                 let currentDiffSum = 0;
                 for (let i = 0; i < targetImageData.length; i += 4) {
                     currentDiffSum += Math.pow(targetImageData[i] - evolvedImageData[i], 2);     // Red
                     currentDiffSum += Math.pow(targetImageData[i + 1] - evolvedImageData[i + 1], 2); // Green
                     currentDiffSum += Math.pow(targetImageData[i + 2] - evolvedImageData[i + 2], 2); // Blue
                 }

                 statusDiv.textContent = `דור: ${generation}, 'טוב' ביותר (מדד שוני - נמוך יותר טוב): ${currentDiffSum.toFixed(0)}`;

            }
        }


        // 2. Create the new population
        const newPopulation = [];
        // Elitism: Add the best individual from the current generation directly to the next
        if (bestIndividual && bestIndividual.length > 0) {
             newPopulation.push(JSON.parse(JSON.stringify(bestIndividual))); // Add the actual best
        } else if (populationWithFitness.length > 0) {
            // If no bestIndividual yet (first generation eval), add the best from this round
             newPopulation.push(JSON.parse(JSON.stringify(populationWithFitness[0].individual)));
        }


        // Fill the rest of the population
        while (newPopulation.length < POPULATION_SIZE) {
            // 3. Selection: Pick two parents
            const parent1 = selectParent(populationWithFitness);
            const parent2 = selectParent(populationWithFitness);

            // 4. Reproduction (Crossover)
            let child = crossover(parent1, parent2);

            // 5. Mutation
            mutate(child);

            newPopulation.push(child);
        }

        generation++;
        return newPopulation;
    }

    // Main GA loop
    function runGA() {
        if (!running) {
            cancelAnimationFrame(animationFrameId);
            return;
        }

        population = nextGeneration(population);

        // Request the next frame
        animationFrameId = requestAnimationFrame(runGA);
    }

    // --- Setup and Event Listeners ---

    function setupTargetImage(imageUrl = null) {
         ctxTarget.fillStyle = 'white'; // Default background
         ctxTarget.fillRect(0, 0, WIDTH, HEIGHT);

        if (imageUrl) {
            const img = new Image();
            img.onload = () => {
                // Draw image scaled to fit canvas
                ctxTarget.drawImage(img, 0, 0, WIDTH, HEIGHT);
                // Get the pixel data for fitness comparison
                targetImageData = ctxTarget.getImageData(0, 0, WIDTH, HEIGHT).data;
                 statusDiv.textContent = 'תמונת יעד נטענה. לחצו "התחל את האבולוציה!"';
                 // Reset simulation state if target changes
                 resetSimulation();
            };
            img.onerror = () => {
                 statusDiv.textContent = 'שגיאה בטעינת התמונה. אנא נסו קובץ אחר.';
                 targetImageData = null; // Clear target data on error
                 resetSimulation(); // Reset to initial state
                 // Draw a default simple target
                 drawDefaultTarget();
                 targetImageData = ctxTarget.getImageData(0, 0, WIDTH, HEIGHT).data;
            }
            img.src = imageUrl;
        } else {
             // Draw a default simple target (e.g., a colored shape)
            drawDefaultTarget();
            // Get the pixel data for fitness comparison
            targetImageData = ctxTarget.getImageData(0, 0, WIDTH, HEIGHT).data;
        }
    }

     function drawDefaultTarget() {
        ctxTarget.fillStyle = '#ffeeba'; // Light yellow background
        ctxTarget.fillRect(0, 0, WIDTH, HEIGHT);
        ctxTarget.fillStyle = 'rgba(0, 123, 255, 0.8)'; // Semi-transparent blue circle
        ctxTarget.beginPath();
        ctxTarget.arc(WIDTH / 2, HEIGHT / 2, Math.min(WIDTH, HEIGHT) / 3, 0, Math.PI * 2);
        ctxTarget.fill();
         ctxTarget.fillStyle = 'rgba(220, 53, 69, 0.7)'; // Semi-transparent red rectangle
         ctxTarget.fillRect(WIDTH * 0.1, HEIGHT * 0.1, WIDTH * 0.3, HEIGHT * 0.3);
     }


    function initializePopulation() {
        running = false; // Stop any running simulation
        cancelAnimationFrame(animationFrameId);
        startStopBtn.textContent = 'התחל את האבולוציה!';

        population = [];
        bestIndividual = [];
        bestFitness = 0;
        generation = 0;

        // Use values from sliders for initial population settings
        POPULATION_SIZE = parseInt(populationSizeSlider.value);
        MAX_POLYGONS = parseInt(maxPolygonsSlider.value);
        MUTATION_RATE = parseFloat(mutationRateSlider.value);


        for (let i = 0; i < POPULATION_SIZE; i++) {
            const individual = [];
            // Start with a minimum number of polygons, up to a small random amount
            const initialPolygons = Math.floor(Math.random() * Math.min(20, MAX_POLYGONS)) + 5;
            for (let j = 0; j < initialPolygons; j++) {
                individual.push(createRandomPolygon());
            }
            population.push(individual);
        }

        statusDiv.textContent = `מוכן להתחלה. אוכלוסייה: ${POPULATION_SIZE}, מקס צורות: ${MAX_POLYGONS}, קצב מוטציה: ${MUTATION_RATE}`;

        // Draw an initial random individual on the evolved canvas
        if (population.length > 0) {
            drawIndividual(ctxEvolved, population[0]);
        } else {
             // Clear evolved canvas if population is empty
             ctxEvolved.fillStyle = 'black';
             ctxEvolved.fillRect(0, 0, WIDTH, HEIGHT);
        }
    }

     function resetSimulation() {
         // This function resets the GA state but keeps the current target image
         running = false;
         cancelAnimationFrame(animationFrameId);
         startStopBtn.textContent = 'התחל את האבולוציה!';
         initializePopulation(); // Re-initialize the population based on current parameters
     }

    // --- Event Listeners ---

    startStopBtn.addEventListener('click', () => {
        if (!targetImageData) {
             statusDiv.textContent = 'אנא הגדירו תמונת יעד לפני ההתחלה (ברירת מחדל או העלאה).';
             return;
        }
        running = !running;
        if (running) {
            startStopBtn.textContent = 'עצור סימולציה';
            // If starting for the first time or after reset, ensure population is initialized
            if (generation === 0 || population.length === 0) {
                 initializePopulation(); // Use current slider values
            }
            runGA(); // Start the GA loop
        } else {
            startStopBtn.textContent = 'התחל את האבולוציה!';
             cancelAnimationFrame(animationFrameId);
        }
    });

     resetBtn.addEventListener('click', () => {
         resetSimulation(); // Resets GA state, keeps target
     });


    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר מסע אל תוך הקוד והאבולוציה' : 'הצגת/הסתרת מסע אל תוך הקוד והאבולוציה';
    });

     uploadTargetBtn.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                setupTargetImage(e.target.result); // Set the uploaded image as target
            };
            reader.onerror = () => {
                 statusDiv.textContent = 'שגיאה בקריאת הקובץ.';
            };
            reader.readAsDataURL(file); // Read file as data URL
        }
    });

    // --- Slider Event Listeners to Update Values ---
    populationSizeSlider.addEventListener('input', (event) => {
        populationSizeValueSpan.textContent = event.target.value;
        POPULATION_SIZE = parseInt(event.target.value); // Update parameter immediately
         if (!running) statusDiv.textContent = `מוכן להתחלה. אוכלוסייה: ${POPULATION_SIZE}, מקס צורות: ${MAX_POLYGONS}, קצב מוטציה: ${MUTATION_RATE}`;
    });

     maxPolygonsSlider.addEventListener('input', (event) => {
         maxPolygonsValueSpan.textContent = event.target.value;
         MAX_POLYGONS = parseInt(event.target.value); // Update parameter immediately
         if (!running) statusDiv.textContent = `מוכן להתחלה. אוכלוסייה: ${POPULATION_SIZE}, מקס צורות: ${MAX_POLYGONS}, קצב מוטציה: ${MUTATION_RATE}`;
     });

     mutationRateSlider.addEventListener('input', (event) => {
         mutationRateValueSpan.textContent = parseFloat(event.target.value).toFixed(3); // Format to 3 decimal places
         MUTATION_RATE = parseFloat(event.target.value); // Update parameter immediately
          if (!running) statusDiv.textContent = `מוכן להתחלה. אוכלוסייה: ${POPULATION_SIZE}, מקס צורות: ${MAX_POLYGONS}, קצב מוטציה: ${MUTATION_RATE}`;
     });


    // --- Initial Setup ---
    setupTargetImage(); // Draw default target image on load
    initializePopulation(); // Initialize population and UI state
});
</script>
```