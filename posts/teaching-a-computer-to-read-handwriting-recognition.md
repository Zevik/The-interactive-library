---
title: "ללמד מחשב לקרוא: מסע אל עולם זיהוי כתב יד"
english_slug: teaching-a-computer-to-read-handwriting-recognition
category: "בינה מלאכותית"
tags:
  - למידת מכונה
  - בינה מלאכותית
  - זיהוי תבניות
  - עיבוד תמונה
---
# ללמד מחשב לקרוא: מסע אל עולם זיהוי כתב יד

דמיינו שהמחשב שלכם יכול לקרוא את כתב היד שלכם! איך זה קורה? האם זו קסם, או טכנולוגיה מדהימה? בואו נצא למסע מרתק אל עולם זיהוי כתב היד, ונלמד את המחשב שלנו לזהות ספרות בדיוק כמו שאנחנו עושים. זה כמו משחק שבו אתם המורים והמחשב הוא התלמיד הנלהב!

<div class="app-container">
    <h2>בנו מודל לזיהוי ספרות - השלבים הראשונים</h2>

    <div class="section" id="data-collection-section">
        <h3>שלב 1: לימוד המחשב (איסוף דוגמאות)</h3>
        <p>כדי ללמד את המחשב, אתם צריכים להראות לו הרבה דוגמאות. ציירו ספרה (0-9) על הלוח הלבן וספרו למחשב מה היא. ככל שתספקו יותר דוגמאות מגוונות, כך המחשב ילמד טוב יותר.</p>
        <div class="canvas-container">
             <canvas id="drawingCanvas" width="200" height="200"></canvas>
        </div>
        <div class="controls">
            <label for="digitLabel">זו הספרה:</label>
            <input type="number" id="digitLabel" min="0" max="9" value="0">
            <button id="addSampleBtn" class="action-button">הוסף דוגמה קסומה!</button>
            <button id="clearCanvasBtn" class="secondary-button">נקה לוח</button>
        </div>
        <p class="status-text">אספתם <span id="sampleCount">0</span> דוגמאות לאימון. מצוין!</p>
        <div class="sample-preview" id="lastSamplePreview" style="display: none;">
            <h4>הדוגמה האחרונה שהוספתם:</h4>
            <img src="" alt="Last added sample" id="lastSampleImg" width="50" height="50" style="border: 1px solid #ccc;">
            <span>ספרה: <span id="lastSampleLabel"></span></span>
        </div>
    </div>

    <div class="section" id="training-section">
        <h3>שלב 2: המחשב לומד (אימון)</h3>
        <p>אחרי שאספתם מספיק דוגמאות, המחשב מוכן ללמוד מהן. לחצו על "למד את המחשב" כדי שהוא יעבור על כל הדוגמאות שלכם וימצא את התבניות.</p>
        <button id="trainModelBtn" disabled class="action-button">למד את המחשב</button>
        <p id="trainingStatus" class="status-text"></p>
         <div class="loading-spinner" id="trainingSpinner" style="display: none;"></div>
    </div>

    <div class="section" id="testing-section" style="display: none;">
        <h3>שלב 3: המחשב מנחש (בדיקה)</h3>
        <p>עכשיו הזמן לבחון את המחשב! ציירו ספרה חדשה על הלוח התחתון ובדקו האם הוא מזהה אותה נכון.</p>
         <div class="canvas-container">
            <canvas id="testingCanvas" width="200" height="200"></canvas>
        </div>
        <div class="controls">
            <button id="testDigitBtn" class="action-button">מה ציירתי?</button>
            <button id="clearTestCanvasBtn" class="secondary-button">נקה לוח</button>
        </div>
        <div id="predictionResult" class="prediction-result" style="margin-top: 20px;"></div>

        <div id="closestMatches" style="margin-top: 15px; text-align: center; display: none;">
             <h4>המחשב השווה לדוגמאות האלה:</h4>
             <div class="match-list" style="display: flex; justify-content: center; gap: 10px;">
                <!-- Closest matches will be added here dynamically -->
             </div>
        </div>

        <div id="feedbackButtons" class="feedback-buttons" style="margin-top: 15px; display: none;">
            האם הניחוש נכון?
            <button id="correctBtn" class="success-button">כן! 🎉</button>
            <button id="incorrectBtn" class="danger-button">לא 😞 (תקן אותי והוסף דוגמה)</button>
        </div>

         <div id="correctionForm" class="correction-form" style="display: none;">
            <p>אופס, טעות! מה הייתה הספרה הנכונה באמת? (המודל ניחש <span id="guessedDigitSpan"></span>)</p>
            <label for="correctDigitInput">הספרה הנכונה:</label>
            <input type="number" id="correctDigitInput" min="0" max="9" value="0" style="width: 50px; margin-right: 5px;">
            <button id="submitCorrectionBtn" class="action-button small">תקן והוסף לאימון</button>
        </div>
    </div>
</div>

<button id="toggleExplanationBtn" class="secondary-button toggle-button" style="margin-top: 20px;">הצג הסבר / הסתר הסבר</button>

<div id="explanation" style="display: none; margin-top: 20px; border-top: 1px solid #eee; padding-top: 20px;">
    <h2>הסבר: מסע אל עולם זיהוי כתב יד</h2>

    <p>אז איך המחשב לומד לקרוא? זה לא קסם, זו בינה מלאכותית, ובפרט ענף שנקרא 'למידת מכונה' (Machine Learning). במקום שנכתוב למחשב חוקים נוקשים לכל צורה אפשרית של ספרה (ותאמינו לנו, יש המון צורות!), אנחנו נותנים לו המון דוגמאות ומאפשרים לו למצוא את הדפוסים בעצמו.</p>

    <h3>למידה מונחית (Supervised Learning) - המורה והתלמיד הדיגיטלי</h3>
    <p>ה"משחק" ששיחקתם הוא הדגמה של למידה מונחית. דמיינו שאתם המורים: אתם מראים לתלמיד (המחשב) תמונה של משהו (ספרה שציירתם) ואומרים לו מה זה (התווית - המספר). אחרי שהוא רואה מספיק דוגמאות מתויגות, הוא מתחיל להבין את הקשר בין הצורה לתווית. המודל לומד לזהות מאפיינים משותפים לכל ה"אפסים", מאפיינים אחרים לכל ה"אחדים", וכן הלאה.</p>

    <h3>זיהוי כתב יד כאתגר למחשב</h3>
    <p>למה המחשב לא יודע לזהות כתב יד בלי ללמוד? כי כתב יד משתנה מאוד! כל אחד כותב קצת אחרת, הגדלים שונים, הנטייה שונה, לפעמים הקווים מתחברים. למידת מכונה מספקת פתרון גמיש שיכול להתמודד עם כל השונות הזו. המטרה היא להמיר תמונה (הספרה שציירתם) למידע דיגיטלי (המספר 0-9).</p>

    <h3>ה"טקס" של בניית מודל ML: איסוף, אימון, ובדיקה</h3>
    <p>השלבים שחוויתם בסימולטור הם הלב של תהליך בניית מודלי למידה מונחית:</p>
    <ol>
        <li><strong>איסוף נתונים (אימון):</strong> זה השלב שבו אתם ציירתם ו"תייגתם" את הספרות. ככל שיש יותר דוגמאות, והן מגוונות יותר (כתיבה רגילה, קצת עקומה, גדלים שונים), כך ה"תלמיד" לומד טוב יותר. הדוגמאות המתויגות הן הזהב של למידת המכונה.</li>
        <li><strong>אימון המודל:</strong> זה השלב שבו המחשב מעבד את כל הדוגמאות שאספתם. הוא לא "זוכר" כל תמונה בעל פה, אלא מוצא את התבניות והמאפיינים הכלליים שמגדירים כל ספרה. הסימולטור הציג את זה בצורה מופשטת, אבל מאחורי הקלעים מתבצעים חישובים מורכבים.</li>
        <li><strong>בדיקת המודל:</strong> בשלב זה אתם מראים למחשב ספרות חדשות שהוא מעולם לא ראה ומבקשים ממנו לנחש. אם הוא ניחש נכון – מעולה! הוא למד היטב. אם הוא טעה – זו הזדמנות מצוינת בשבילו ללמוד! זה בדיוק מה שעשיתם כשתיקנתם לו את הטעות והוספתם את הדוגמה החדשה לאימון.</li>
    </ol>

    <h3>למה דוגמאות הן כל כך חשובות?</h3>
    <p>ראיתם שעם מעט דוגמאות, המחשב היה כנראה די גרוע בניחושים. זה כמו לנסות ללמד ילד לזהות חיות רק מציור אחד של חתול. הוא יתקשה לזהות כלבים או אפילו חתולים אחרים! ככל שאספתם יותר דוגמאות, במיוחד כשהמחשב טעה ולימדתם אותו מה הייתה הספרה הנכונה, כך ביצועיו השתפרו. הנתונים הם "ספר הלימוד" של המודל, והתיוג הנכון (הלייבל) הוא המורה שמסביר לו מה הוא רואה.</p>

    <h3>איך המחשב "רואה"? (רמז: לא כמונו)</h3>
    <p>למחשב אין עיניים. הוא "רואה" מספרים. תמונה של ספרה היא מבחינתו רשת של נקודות (פיקסלים), ולכל נקודה יש מספר שמבטא את הצבע או הכהות שלה. המודל לומד לזהות דפוסים בתוך סדרות המספרים האלה. כדי לפשט, לרוב מקטינים את התמונות לגודל סטנדרטי (כמו 28x28 פיקסלים) לפני שמעבירים אותן למודל – זה עוזר לו להתרכז בצורה ולא בגודל המדויק.</p>

    <h3>האתגרים האמיתיים (מעבר לסימולטור)</h3>
    <p>זיהוי כתב יד "אמיתי", כמו פתק שכתבתם במהירות, הוא הרבה יותר מורכב. האתגרים כוללים שונות קיצונית בין כותבים, רעש (כתמים, קווים חלשים), אותיות שמחוברות זו לזו, ולפעמים כתב יד כל כך גרוע שאפילו אנחנו מתקשים לפענח. מודלים מתקדמים, ובמיוחד כאלה שמבוססים על 'למידה עמוקה' (Deep Learning) - סוג מתוחכם יותר של למידת מכונה - מצליחים להתמודד עם האתגרים הללו.</p>

    <h3>למידת מכונה מסביבנו</h3>
    <p>העקרונות הבסיסיים של איסוף נתונים, אימון, ובדיקה שראיתם כאן נמצאים בשימוש בעשרות טכנולוגיות יומיומיות:</p>
    <ul>
        <li><strong>זיהוי פנים</strong> בטלפון או ברשתות חברתיות.</li>
        <li><strong>זיהוי קולי</strong> בעוזרים דיגיטליים כמו סירי או אלקסה.</li>
        <li><strong>סינון מיילים</strong> וזיהוי ספאם.</li>
        <li><strong>מערכות המלצה</strong> בנטפליקס, יוטיוב, או אמזון.</li>
        <li><strong>אבחון רפואי</strong> בסריקות ובצילומי רנטגן.</li>
        <li><strong>נהיגה אוטונומית</strong> שבה המכונית מזהה עצמים בכביש.</li>
    </ul>
    <p>בכל פעם שמערכת "מנחשת" או "מזהה" משהו על בסיס נתונים שקיבלה בעבר, יש סיכוי טוב שלמידת מכונה נמצאת שם מאחורי הקלעים. עכשיו אתם יודעים איך זה מתחיל!</p>
</div>


<style>
/* General Styles */
.app-container {
    font-family: 'Heebo', sans-serif; /* Use Heebo or Arial as fallback */
    direction: rtl;
    text-align: right;
    max-width: 650px; /* Slightly wider */
    margin: 20px auto;
    padding: 30px; /* More padding */
    background-color: #f0f4f8; /* Soft background */
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    border: none; /* Remove old border */
}

.app-container h2 {
    text-align: center;
    color: #2c3e50; /* Darker blue/gray */
    margin-bottom: 25px;
    font-size: 1.8em;
}

.section {
    margin-bottom: 30px;
    padding: 25px;
    border: 1px solid #dcdcdc; /* Lighter border */
    border-radius: 8px;
    background-color: #ffffff; /* White background for sections */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); /* Section shadow */
    transition: box-shadow 0.3s ease-in-out; /* Add transition */
}

.section:hover {
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Hover effect */
}

.section h3 {
    text-align: center;
    color: #34495e; /* Slightly lighter than h2 */
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.4em;
}

.section p {
    text-align: center;
    color: #555;
    margin-bottom: 15px;
    line-height: 1.5;
}

.status-text {
     text-align: center;
     font-size: 1em;
     color: #333;
     min-height: 1.2em; /* Reserve space */
     margin-top: 15px;
}

/* Canvas Styles */
.canvas-container {
    display: flex;
    justify-content: center;
    margin: 20px auto;
}

canvas {
    border: 2px solid #3498db; /* Blue border */
    display: block;
    background-color: #fff; /* Ensure canvas is white */
    touch-action: none; /* Prevent scrolling on mobile */
    border-radius: 8px; /* Match container corners */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Control Styles (Inputs, Buttons) */
.controls {
    text-align: center;
    margin-top: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap; /* Allow wrapping on small screens */
}

.controls label, .controls input, .controls button {
     margin: 5px; /* Adjust margin */
    padding: 10px 15px; /* More padding */
    border-radius: 6px; /* More rounded */
    border: 1px solid #ccc;
    font-size: 1em;
}

input[type="number"] {
     width: 60px; /* Fixed width */
     text-align: center;
}


/* Button Styles */
button {
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
}

button:disabled {
    background-color: #cccccc !important; /* Grey */
    color: #666 !important;
    cursor: not-allowed;
    transform: none !important;
    box-shadow: none !important;
}

.action-button {
    background-color: #3498db; /* Primary Blue */
    color: white;
    border: none;
    box-shadow: 0 4px 6px rgba(52, 152, 219, 0.3);
}

.action-button:hover:not(:disabled) {
    background-color: #2980b9; /* Darker Blue */
    transform: translateY(-2px);
    box-shadow: 0 6px 8px rgba(52, 152, 219, 0.4);
}

.secondary-button {
    background-color: #ecf0f1; /* Light Grey */
    color: #34495e; /* Dark text */
    border: 1px solid #bdc3c7;
}

.secondary-button:hover:not(:disabled) {
    background-color: #bdc3c7; /* Darker Grey */
    transform: translateY(-2px);
}

.toggle-button {
    display: block; /* Make toggle button block */
    width: fit-content;
    margin: 20px auto;
}

.success-button {
    background-color: #2ecc71; /* Green */
    color: white;
    border: none;
    box-shadow: 0 4px 6px rgba(46, 204, 113, 0.3);
}
.success-button:hover:not(:disabled) {
    background-color: #27ae60; /* Darker Green */
     transform: translateY(-2px);
     box-shadow: 0 6px 8px rgba(46, 204, 113, 0.4);
}


.danger-button {
    background-color: #e74c3c; /* Red */
    color: white;
    border: none;
    box-shadow: 0 4px 6px rgba(231, 76, 60, 0.3);
}
.danger-button:hover:not(:disabled) {
    background-color: #c0392b; /* Darker Red */
     transform: translateY(-2px);
     box-shadow: 0 6px 8px rgba(231, 76, 60, 0.4);
}

/* Specific Section Styles */
#data-collection-section p, #training-section p, #testing-section p {
    text-align: right; /* Align section text right */
}

#data-collection-section .status-text, #training-section .status-text {
     text-align: center;
}

/* Prediction Result */
.prediction-result {
    font-size: 1.5em;
    font-weight: bold;
    text-align: center;
    min-height: 1.8em; /* Reserve space */
    color: #2980b9; /* Match primary blue */
}

/* Closest Matches Visualization */
#closestMatches h4 {
    text-align: center;
    color: #555;
    margin-bottom: 10px;
    font-size: 1.1em;
}

.match-item {
    text-align: center;
    font-size: 0.9em;
    color: #666;
}
.match-item img {
    border: 1px solid #bdc3c7;
    margin-bottom: 5px;
    border-radius: 4px;
}


/* Feedback Buttons */
.feedback-buttons {
    text-align: center;
}

.feedback-buttons button {
    margin: 0 5px;
}

/* Correction Form */
.correction-form {
    margin-top: 20px;
    padding: 15px;
    background-color: #f9f9f9;
    border: 1px solid #eee;
    border-radius: 8px;
    text-align: center;
}

.correction-form p {
     margin-bottom: 10px;
     font-size: 1em;
     text-align: center;
     color: #333;
}

.correction-form input {
    vertical-align: middle;
    margin-right: 5px;
}
.correction-form button {
     vertical-align: middle;
}
.small {
    padding: 5px 10px;
    font-size: 0.9em;
}


/* Sample Preview */
.sample-preview {
    text-align: center;
    margin-top: 15px;
    padding-top: 10px;
    border-top: 1px dashed #ccc;
    font-size: 0.9em;
    color: #555;
}
.sample-preview h4 {
    margin: 0 0 10px 0;
    font-size: 1em;
    color: #333;
}
.sample-preview img {
    vertical-align: middle;
    margin-left: 10px;
}
.sample-preview span {
    vertical-align: middle;
}


/* Loading Spinner (Simple CSS animation) */
.loading-spinner {
  border: 4px solid #f3f3f3; /* Light grey */
  border-top: 4px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
  display: inline-block; /* or block */
  vertical-align: middle;
  margin-right: 10px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}


/* Explanation Section */
#explanation {
    background-color: #ecf0f1; /* Light background for explanation */
    padding: 25px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

#explanation h3 {
    margin-top: 20px;
    color: #34495e;
    font-size: 1.3em;
}

#explanation p, #explanation li {
    line-height: 1.7; /* More line height */
    text-align: justify;
    margin-bottom: 12px;
    color: #444;
}

#explanation ol, #explanation ul {
    margin-bottom: 15px;
    padding-right: 20px; /* Indent list */
}

#explanation li strong {
    color: #2c3e50; /* Highlight key terms */
}


/* Responsive adjustments */
@media (max-width: 700px) {
    .app-container {
        padding: 20px;
    }
    .section {
        padding: 15px;
    }
    .controls {
        flex-direction: column;
    }
    .controls label, .controls input, .controls button {
        width: 100%; /* Stack controls */
        box-sizing: border-box; /* Include padding/border in width */
        text-align: center; /* Center button text */
        margin: 5px 0; /* Adjust margin */
    }
    input[type="number"] {
         width: auto; /* Auto width for number input */
         max-width: 80px; /* Max width for number input */
    }
    .feedback-buttons button {
        margin: 5px auto; /* Stack feedback buttons */
        display: block;
        width: 80%; /* Make feedback buttons wider */
    }
     .correction-form input, .correction-form button {
         display: inline-block; /* Keep inline in form */
         width: auto;
         margin: 5px;
     }
}

</style>

<script>
// --- Get elements ---
const drawingCanvas = document.getElementById('drawingCanvas');
const drawingCtx = drawingCanvas.getContext('2d');
const digitLabelInput = document.getElementById('digitLabel');
const addSampleBtn = document.getElementById('addSampleBtn');
const clearCanvasBtn = document.getElementById('clearCanvasBtn');
const sampleCountSpan = document.getElementById('sampleCount');
const lastSamplePreviewDiv = document.getElementById('lastSamplePreview');
const lastSampleImg = document.getElementById('lastSampleImg');
const lastSampleLabelSpan = document.getElementById('lastSampleLabel');


const trainModelBtn = document.getElementById('trainModelBtn');
const trainingStatus = document.getElementById('trainingStatus');
const trainingSpinner = document.getElementById('trainingSpinner');

const testingSection = document.getElementById('testing-section');
const testingCanvas = document.getElementById('testingCanvas');
const testingCtx = testingCanvas.getContext('2d');
const testDigitBtn = document.getElementById('testDigitBtn');
const clearTestCanvasBtn = document.getElementById('clearTestCanvasBtn');
const predictionResultDiv = document.getElementById('predictionResult');
const feedbackButtonsDiv = document.getElementById('feedbackButtons');
const correctBtn = document.getElementById('correctBtn');
const incorrectBtn = document.getElementById('incorrectBtn');
const correctionFormDiv = document.getElementById('correctionForm');
const guessedDigitSpan = document.getElementById('guessedDigitSpan');
const correctDigitInput = document.getElementById('correctDigitInput');
const submitCorrectionBtn = document.getElementById('submitCorrectionBtn');
const closestMatchesDiv = document.getElementById('closestMatches');
const match listrik = closestMatchesDiv.querySelector('.match-list');


const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
const explanationDiv = document.getElementById('explanation');

// --- State Variables ---
let isDrawing = false;
let trainingData = []; // Stores { label: number, imageData: string }
let simulatedModel = null; // The trained model is essentially the trainingData for this simulation
let lastTestImageData = null; // Store data for correction feedback

// --- Canvas Drawing Logic ---
function setupCanvasDrawing(canvas, ctx, clearBtn) {
    let lastX = 0;
    let lastY = 0;
    let localIsDrawing = false; // Local state for this canvas instance

    ctx.lineWidth = 15; // Thicker line for digits
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round'; // Smooth joints
    ctx.strokeStyle = '#000'; // Black color

    // Function to clear canvas and fill with white
    const clearAndFillWhite = () => {
        ctx.fillStyle = '#fff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath(); // Reset path after filling
    };

    function draw(e) {
        if (!localIsDrawing) return;

        const rect = canvas.getBoundingClientRect();
        const x = (e.clientX || e.touches[0].clientX) - rect.left;
        const y = (e.clientY || e.touches[0].clientY) - rect.top;

        ctx.lineTo(x, y);
        ctx.stroke();
        [lastX, lastY] = [x, y];
    }

    function startDrawing(e) {
         const rect = canvas.getBoundingClientRect();
         lastX = (e.clientX || e.touches[0].clientX) - rect.left;
         lastY = (e.clientY || e.touches[0].clientY) - rect.top;
         localIsDrawing = true;
         ctx.beginPath(); // Start a new path
         ctx.moveTo(lastX, lastY);
    }

     function stopDrawing() {
        if (localIsDrawing) {
             localIsDrawing = false;
             // Optional: Add a small circle at the end of a stroke if needed
             // ctx.beginPath();
             // ctx.arc(lastX, lastY, ctx.lineWidth / 2, 0, Math.PI * 2, false);
             // ctx.fillStyle = ctx.strokeStyle;
             // ctx.fill();
        }
     }

    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('touchstart', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('touchmove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('touchend', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing); // Stop drawing if mouse leaves canvas
    canvas.addEventListener('touchcancel', stopDrawing);

    clearBtn.addEventListener('click', clearAndFillWhite);

    // Initial clear to ensure white background on load
    clearAndFillWhite();

    // Return the clear function so it can be used externally if needed
    return clearAndFillWhite;
}

// Setup both canvases
const clearDrawingCanvas = setupCanvasDrawing(drawingCanvas, drawingCtx, clearCanvasBtn);
const clearTestingCanvas = setupCanvasDrawing(testingCanvas, testingCtx, clearTestCanvasBtn);


// --- Helper: Check if canvas is empty ---
function isCanvasEmpty(canvas, ctx) {
    const pixels = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    for(let i = 0; i < pixels.length; i += 4) {
        // Check if not white (R, G, B are not 255) or if alpha is not 0 (for partial drawings)
        if (pixels[i] < 255 || pixels[i+1] < 255 || pixels[i+2] < 255 || pixels[i+3] > 0) {
             return false; // Found a non-white pixel
        }
    }
    return true; // All pixels are white
}


// --- Data Collection ---
addSampleBtn.addEventListener('click', () => {
    const label = parseInt(digitLabelInput.value, 10);
    if (isNaN(label) || label < 0 || label > 9) {
        alert("אנא הכנס ספרה תקינה (0-9).");
        return;
    }

    if (isCanvasEmpty(drawingCanvas, drawingCtx)) {
        alert("אנא צייר ספרה לפני הוספת דוגמה.");
        return;
    }

    const imageData = drawingCanvas.toDataURL();

    trainingData.push({ label: label, imageData: imageData });
    sampleCountSpan.textContent = trainingData.length;

    // Show preview of the last added sample
    lastSampleImg.src = imageData;
    lastSampleLabelSpan.textContent = label;
    lastSamplePreviewDiv.style.display = 'block';

    // Clear canvas for next drawing
    clearDrawingCanvas();

    // Enable train button after at least one sample
    if (trainingData.length > 0) {
        trainModelBtn.disabled = false;
        trainingStatus.textContent = `אספת ${trainingData.length} דוגמאות. המחשב מתחיל להבין!`;
    }
});


// --- Training Simulation ---
trainModelBtn.addEventListener('click', () => {
    if (trainingData.length === 0) {
        alert("אסוף דוגמאות לאימון קודם.");
        return;
    }

    // Simulate training process
    trainingStatus.textContent = "המחשב לומד...";
    trainModelBtn.disabled = true;
    addSampleBtn.disabled = true;
    clearCanvasBtn.disabled = true;
    trainingSpinner.style.display = 'inline-block'; // Show spinner

    // Simulate complex calculation time based on data size (simple)
    const trainingTime = Math.min(3000, 500 + trainingData.length * 10); // Max 3 seconds, min 0.5s

    setTimeout(() => {
        simulatedModel = trainingData; // Model is the data itself for lookup
        trainingStatus.textContent = `🥳 אימון הסתיים! המודל אומן על ${trainingData.length} דוגמאות.`;
        trainModelBtn.disabled = false;
        addSampleBtn.disabled = false;
        clearCanvasBtn.disabled = false;
        trainingSpinner.style.display = 'none'; // Hide spinner

        // Smoothly transition to testing section
        testingSection.style.opacity = '0';
        testingSection.style.display = 'block';
        setTimeout(() => {
            testingSection.style.opacity = '1';
        }, 10); // Small delay for transition to apply

        predictionResultDiv.textContent = 'צייר ספרה כאן לבדיקה 👇';
        feedbackButtonsDiv.style.display = 'none';
        correctionFormDiv.style.display = 'none';
        closestMatchesDiv.style.display = 'none'; // Hide matches initially
        clearTestingCanvas(); // Clear test canvas
    }, trainingTime);
});


// --- Testing ---
testDigitBtn.addEventListener('click', async () => {
    if (!simulatedModel || simulatedModel.length === 0) {
        predictionResultDiv.textContent = "אנא אמן את המודל קודם.";
        return;
    }

    if (isCanvasEmpty(testingCanvas, testingCtx)) {
        predictionResultDiv.textContent = "אנא צייר ספרה לבדיקה על הלוח התחתון.";
        return;
    }


    predictionResultDiv.textContent = "המחשב חושב...";
    predictionResultDiv.style.color = '#2980b9'; // Thinking color
    feedbackButtonsDiv.style.display = 'none';
    correctionFormDiv.style.display = 'none';
    closestMatchesDiv.style.display = 'none'; // Hide previous matches
    matchListDiv.innerHTML = ''; // Clear previous matches

    const testImageData = testingCanvas.toDataURL();
    lastTestImageData = testImageData; // Store for potential correction

    // --- Simple Prediction Logic (Simulation) ---
    const testImg = new Image();
    testImg.onload = async () => {
        const smallSize = 28; // Standard size like MNIST
        const testSmallCanvas = document.createElement('canvas');
        testSmallCanvas.width = smallSize;
        testSmallCanvas.height = smallSize;
        const testSmallCtx = testSmallCanvas.getContext('2d');
         // Draw white background before drawing digit
        testSmallCtx.fillStyle = '#fff';
        testSmallCtx.fillRect(0, 0, smallSize, smallSize);
        testSmallCtx.drawImage(testImg, 0, 0, smallSize, smallSize);
        const testPixels = testSmallCtx.getImageData(0, 0, smallSize, smallSize).data;

        let topMatches = []; // Store top N matches { label, diff, imageData }
        const numMatchesToShow = 5; // Show top 5 matches

        // Load training images async first
        const trainingImages = await Promise.all(simulatedModel.map(sample => {
            return new Promise(resolve => {
                const img = new Image();
                img.onload = () => resolve({ img: img, label: sample.label, imageData: sample.imageData });
                img.src = sample.imageData;
            });
        }));


        for (const { img: trainImg, label: trainLabel, imageData: trainImageData } of trainingImages) {
            const trainSmallCanvas = document.createElement('canvas');
            trainSmallCanvas.width = smallSize;
            trainSmallCanvas.height = smallSize;
            const trainSmallCtx = trainSmallCanvas.getContext('2d');
            // Draw white background before drawing digit
            trainSmallCtx.fillStyle = '#fff';
            trainSmallCtx.fillRect(0, 0, smallSize, smallSize);
            trainSmallCtx.drawImage(trainImg, 0, 0, smallSize, smallSize);
            const trainPixels = trainSmallCtx.getImageData(0, 0, smallSize, smallSize).data;

            let diff = 0;
            // Simple difference based on alpha channel (assuming black drawing on white)
            for (let i = 0; i < testPixels.length; i += 4) {
                 diff += Math.abs(testPixels[i+3] - trainPixels[i+3]); // Compare alpha
            }

            // Keep track of top N matches
            if (topMatches.length < numMatchesToShow) {
                 topMatches.push({ label: trainLabel, diff: diff, imageData: trainImageData });
                 topMatches.sort((a, b) => a.diff - b.diff); // Keep sorted by difference
            } else if (diff < topMatches[numMatchesToShow - 1].diff) {
                 topMatches[numMatchesToShow - 1] = { label: trainLabel, diff: diff, imageData: trainImageData };
                 topMatches.sort((a, b) => a.diff - b.diff);
            }
        }

         // The predicted label is the label of the closest match (first in sorted topMatches)
        let predictedLabel = topMatches.length > 0 ? topMatches[0].label : -1;

        // Simulate processing delay slightly
        setTimeout(() => {
            if (predictedLabel !== -1) {
                predictionResultDiv.textContent = `✨ ניחוש המחשב: ${predictedLabel} ✨`;
                predictionResultDiv.style.color = '#27ae60'; // Success color

                // Display closest matches
                matchListDiv.innerHTML = ''; // Clear previous
                topMatches.forEach(match => {
                    const matchItem = document.createElement('div');
                    matchItem.classList.add('match-item');
                    matchItem.innerHTML = `<img src="${match.imageData}" width="40" height="40" alt="Match Sample"><br> (${match.label})`;
                     matchListDiv.appendChild(matchItem);
                });
                 closestMatchesDiv.style.display = 'block';


                feedbackButtonsDiv.style.display = 'block'; // Show feedback buttons
                guessedDigitSpan.textContent = predictedLabel; // Set guessed digit for correction form

            } else {
                 predictionResultDiv.textContent = "🤔 לא הצלחתי לזהות. אולי תאמנו אותי על עוד דוגמאות דומות?";
                 predictionResultDiv.style.color = '#e67e22'; // Warning color
                 feedbackButtonsDiv.style.display = 'none';
                 closestMatchesDiv.style.display = 'none';
            }
        }, 800); // Simulate short delay
    };
     testImg.src = testImageData; // Trigger image load and comparison
});


// --- Feedback Buttons ---
correctBtn.addEventListener('click', () => {
    predictionResultDiv.textContent = "מעולה! המחשב למד נכון!";
    predictionResultDiv.style.color = '#2ecc71';
    feedbackButtonsDiv.style.display = 'none';
    correctionFormDiv.style.display = 'none';
    closestMatchesDiv.style.display = 'none';
    clearTestingCanvas(); // Clear test canvas
    lastTestImageData = null; // Clear stored test image
});

incorrectBtn.addEventListener('click', () => {
    feedbackButtonsDiv.style.display = 'none'; // Hide feedback buttons
    correctionFormDiv.style.display = 'block'; // Show correction form
    // guessedDigitSpan is already set in testDigitBtn handler
});

submitCorrectionBtn.addEventListener('click', () => {
    const correctLabel = parseInt(correctDigitInput.value, 10);

    if (isNaN(correctLabel) || correctLabel < 0 || correctLabel > 9) {
         predictionResultDiv.textContent = "קלט לא תקין. הדוגמה לא נוספה.";
         predictionResultDiv.style.color = '#e74c3c'; // Error color
         correctionFormDiv.style.display = 'none';
         closestMatchesDiv.style.display = 'none';
         clearTestingCanvas();
         lastTestImageData = null;
         return;
    }

    if (lastTestImageData) {
        trainingData.push({ label: correctLabel, imageData: lastTestImageData });
        sampleCountSpan.textContent = trainingData.length;

        predictionResultDiv.textContent = `👍 הוספתי את הדוגמה עם התווית: ${correctLabel} לאימון! אמן מחדש כדי לשפר אותי.`;
        predictionResultDiv.style.color = '#3498db'; // Info color

        // Clear elements
        correctionFormDiv.style.display = 'none';
        closestMatchesDiv.style.display = 'none';
        clearTestingCanvas();
        lastTestImageData = null;

        // Encourage retraining
        trainModelBtn.disabled = false;
        trainingStatus.textContent = `הוספת דוגמה חדשה (${correctLabel}). מומלץ לאמן מחדש!`;

    } else {
        // Should not happen if flow is correct
        predictionResultDiv.textContent = "שגיאה: אין דוגמה לבדיקה להוספה.";
         predictionResultDiv.style.color = '#e74c3c'; // Error color
         correctionFormDiv.style.display = 'none';
         closestMatchesDiv.style.display = 'none';
    }
});


// --- Explanation Toggle ---
toggleExplanationBtn.addEventListener('click', () => {
    if (explanationDiv.style.display === 'none') {
        explanationDiv.style.display = 'block';
        toggleExplanationBtn.textContent = 'הסתר הסבר 👆';
         explanationDiv.scrollIntoView({ behavior: 'smooth' }); // Scroll to explanation
    } else {
        explanationDiv.style.display = 'none';
        toggleExplanationBtn.textContent = 'הצג הסבר / הסתר הסבר';
    }
});


// --- Initial state setup ---
trainModelBtn.disabled = true; // Initially no data to train
testingSection.style.display = 'none'; // Hide testing until trained
explanationDiv.style.display = 'none'; // Hide explanation initially

// Ensure canvases are white on load (handled by setupCanvasDrawing)

</script>