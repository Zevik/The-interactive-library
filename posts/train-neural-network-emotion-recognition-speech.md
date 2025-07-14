---
title: "מעבדת אימון: ללמד מכונה להרגיש דרך הקול"
english_slug: train-neural-network-emotion-recognition-speech
category: "בינה מלאכותית"
tags:
  - רשתות עצביות
  - למידת מכונה
  - זיהוי קול
  - רגשות
  - בינה מלאכותית
---
<h1>מעבדת אימון: ללמד מכונה להרגיש דרך הקול</h1>
<p class="intro-text">תארו לעצמכם שיחה שבה המחשב מבין לא רק את המילים שלכם, אלא גם את הרגש שמאחוריהן. הקול שלנו הוא אוצר של מידע רגשי – הטון, הקצב והעוצמה חושפים פחד, שמחה, כעס או עצב. אבל איך גורמים למכונה לחוש את הניואנסים האנושיים העדינים הללו? הצטרפו למעבדה שלנו והתנסו בעצמכם!</p>

<!-- Application Area -->
<div id="app-container">
    <h2>התנסות מעשית: אימון מודל לזיהוי רגשות</h2>
    <p>השתמשו בסימולטור שלנו כדי לאמן רשת עצבית פשוטה לזיהוי רגשות נבחרים (שמחה, עצב, כעס, ניטרלי) על דאטה מפושט. שחקו עם הפרמטרים וראו איך הם משפיעים על תהליך הלמידה והתוצאה הסופית!</p>

    <div class="control-panel">
        <h3>כוונו את מוח המכונה:</h3>
        <div class="controls">
            <div class="control-group">
                <label for="learningRate" title="קצב למידה: קובע כמה 'גדול' יהיה כל צעד למידה. ערך גבוה מדי עלול לגרום לאי-יציבות, נמוך מדי יהפוך את האימון לאיטי מאוד.">קצב למידה (Learning Rate):</label>
                <input type="number" id="learningRate" value="0.01" step="0.001" min="0.001" max="0.1" title="קצב למידה: קובע כמה 'גדול' יהיה כל צעד למידה. ערך גבוה מדי עלול לגרום לאי-יציבות, נמוך מדי יהפוך את האימון לאיטי מאוד.">
            </div>
            <div class="control-group">
                <label for="epochs" title="מספר עידנים: כמה פעמים הרשת תעבור על כל סט נתוני האימון. יותר עידנים לא תמיד טוב יותר (חפשו סימנים להתאמת יתר).">מספר עידנים (Epochs):</label>
                <input type="number" id="epochs" value="50" step="1" min="1" max="200" title="מספר עידנים: כמה פעמים הרשת תעבור על כל סט נתוני האימון. יותר עידנים לא תמיד טוב יותר (חפשו סימנים להתאמת יתר).">
            </div>
             <button id="startTrainingBtn">התחל אימון!</button>
        </div>
    </div>


    <div id="training-area">
         <h3>מסלול הלמידה:</h3>
         <div id="progress-container">
             <div id="progress-output">
                <p>כאן תראו את עדכוני ההתקדמות בזמן אמת...</p>
             </div>
             <div id="accuracy-chart" dir="ltr">
                  <!-- Accuracy chart bars will be added here -->
                  <div class="chart-overlay">
                       <div class="chart-y-axis"><span>100%</span><span>50%</span><span>0%</span></div>
                       <div class="chart-legend">
                            <span class="legend-train"></span> דיוק אימון
                            <span class="legend-val"></span> דיוק ולידציה
                       </div>
                   </div>
             </div>
         </div>
    </div>

    <div id="results" style="display: none;">
        <h3>תוצאות סופיות:</h3>
        <p class="final-accuracy-display">דיוק סופי (על נתוני בחינה): <span id="final-accuracy">-</span></p>
        <h4>מטריצת בלבול (Confusion Matrix):</h4>
        <p class="matrix-note">כמה דגימות מכל רגש *אמיתי* (שורות) סווגו ע"י הרשת כרגש *נחזה* (עמודות).</p>
        <table id="confusion-matrix-table">
            <thead>
                <tr><th></th><th>שמחה<br>(נחזה)</th><th>עצב<br>(נחזה)</th><th>כעס<br>(נחזה)</th><th>ניטרלי<br>(נחזה)</th></tr>
            </thead>
            <tbody>
                <tr><th>שמחה<br>(אמיתי)</th><td data-emotion="happy-happy"></td><td data-emotion="happy-sad"></td><td data-emotion="happy-angry"></td><td data-emotion="happy-neutral"></td></tr>
                <tr><th>עצב<br>(אמיתי)</th><td data-emotion="sad-happy"></td><td data-emotion="sad-sad"></td><td data-emotion="sad-angry"></td><td data-emotion="sad-neutral"></td></tr>
                <tr><th>כעס<br>(אמיתי)</th><td data-emotion="angry-happy"></td><td data-emotion="angry-sad"></td><td data-emotion="angry-angry"></td><td data-emotion="angry-neutral"></td></tr>
                <tr><th>ניטרלי<br>(אמיתי)</th><td data-emotion="neutral-happy"></td><td data-emotion="neutral-sad"></td><td data-emotion="neutral-angry"></td><td data-emotion="neutral-neutral"></td></tr>
            </tbody>
        </table>
    </div>
</div>

<!-- Explanation Toggle Button -->
<button id="toggleExplanationBtn">מעמיק יותר: מה עומד מאחורי הסימולטור?</button>

<!-- Explanation Area -->
<div id="explanation" style="display: none;">
    <h2>מסע אל תוך זיהוי רגשות בקול (SER)</h2>
    <p>**זיהוי רגשות בקול (Speech Emotion Recognition - SER)** הוא תחום מרתק בבינה מלאכותית שמטרתו לפענח את המצב הרגשי של הדובר רק מהאופן שבו הוא מדבר, ללא תלות במילים עצמן. דמיינו את זה כסופר-שמיעה דיגיטלית שמזהה עצב ברעד קל בקול או שמחה בהתרוממות פתאומית בטון.</p>

    <h3>איך הקול שלנו מגלה מה אנחנו מרגישים?</h3>
    <p>רגשות משפיעים עמוקות על האופן הפיזי שבו אנו מפיקים צלילים. רשתות עצביות מאומנות סורקות את אותות הקול ומחפשות דפוסים ב**מאפיינים אקוסטיים** מגוונים:</p>
    <ul>
        <li>**גובה הצליל (Pitch / F0):** הקול נשמע גבוה יותר כשמרגישים התרגשות או כעס, ונמוך יותר בעצב או רוגע.</li>
        <li>**עוצמה (Intensity / Energy):** כעס ושמחה עזים לרוב מתבטאים בדיבור חזק יותר.</li>
        <li>**קצב ושטף דיבור:** מהירות הדיבור, ההפסקות והגמגומים יכולים להעיד על לחץ, התרגשות או חוסר אנרגיה.</li>
        <li>**איכות קול:** מאפיינים כמו צרידות, נשימתיות או רעידות עשויים להיות קשורים למצבים רגשיים מסוימים.</li>
    </ul>

    <h3>המוח הדיגיטלי: מבט על רשתות עצביות</h3>
    <p>בלב הסימולטור (וברוב מערכות ה-SER המתקדמות) עומדת **רשת עצבית מלאכותית**. חשבו עליה כעל אוסף גדול של "נוירונים" דיגיטליים המחוברים ביניהם, בדומה למבנה המוח האנושי. הנוירונים מאורגנים בשכבות:</p>
    <ul>
        <li>**שכבת קלט:** מקבלת את המאפיינים האקוסטיים שחולצו מקטע קול.</li>
        <li>**שכבות נסתרות:** אלו "מוח" הרשת, בהן מתבצע עיבוד מורכב של המידע כדי לזהות דפוסים עדינים.</li>
        <li>**שכבת פלט:** מספקת ציון או סבירות לכל אחד מהרגשות האפשריים (שמחה, עצב, כעס, ניטרלי). הרגש עם הציון הגבוה ביותר הוא הניבוי של הרשת.</li>
    </ul>
    <p>ה"קשרים" בין הנוירונים הם למעשה **משקלים** - מספרים הקובעים את חשיבות הקלט מאותו קשר. תהליך האימון עוסק בעיקר בהתאמת המשקלים הללו.</p>

    <h3>ריקוד הלמידה: איך רשת עצבית לומדת?</h3>
    <p>אימון הרשת הוא תהליך איטרטיבי, כמו ליטוש יהלום. הוא מתבסס על דוגמאות (קטעי קול עם התווית הרגשית הנכונה) וכולל את השלבים החוזרים על עצמם:</p>
    <ol>
        <li>**ניבוי:** הרשת מקבלת קטע קול ומנסה לנחש את הרגש.</li>
        <li>**חישוב שגיאה:** הניבוי מושווה לרגש ה*אמיתי*. ההבדל ביניהם הוא השגיאה.</li>
        <li>**עדכון משקלים (Backpropagation):** השגיאה "מוחזרת לאחור" דרך הרשת, וכל משקל מותאם מעט כדי שהרשת תטעה פחות בפעם הבאה. זה כמו שהמוח שלנו מתאים את עצמו אחרי טעות.</li>
    </ol>
    <p>מעבר אחד על כל הדוגמאות בנתוני האימון נקרא **עידן (Epoch)**. ככל שיש יותר עידנים, לרשת יש יותר הזדמנויות ללמוד, אך גם סיכון גבוה יותר ל"התאמת יתר" (Overfitting).</p>
    <p>**קצב הלמידה (Learning Rate)** הוא המפתח כאן – הוא קובע כמה "אגרסיבי" יהיה עדכון המשקלים בכל שלב. קצב גבוה מדי יכול לגרום לרשת "לדלג" מעל הפתרון הטוב ביותר, בעוד שקצב נמוך מדי יאט את האימון משמעותית.</p>

    <h3>אימון מול בחינה: למה צריך דאטה נפרד?</h3>
    <p>כדי שמודל יהיה שימושי באמת, הוא צריך להיות מסוגל לזהות רגשות גם בקולות *חדשים* שמעולם לא שמע במהלך האימון. לכן, אנו מחלקים את הדאטה לשלושה חלקים (בסימולטור שלנו השתמשנו בנתוני אימון ובחינה/ולידציה מפושטים):</p>
    <ul>
        <li>**נתוני אימון:** עליהם הרשת לומדת ומעדכנת את המשקלים.</li>
        <li>**נתוני ולידציה (בחינה בזמן אימון):** נתונים אלו *אינם* משמשים לאימון ישיר, אלא למעקב אחר ביצועי הרשת *במהלך* האימון. אם הדיוק על נתוני האימון ממשיך לעלות אך הדיוק על נתוני הולידציה מפסיק או יורד, זהו סימן מובהק ל**התאמת יתר** – הרשת בעצם שיננה את נתוני האימון במקום ללמוד להכליל.</li>
        <li>**נתוני טסט (בחינה סופית):** לאחר שהאימון הסתיים, מעריכים את הביצועים הסופיים של המודל על סט נתונים חדש לחלוטין.</li>
    </ul>

    <h3>הערכת המודל: מעבר לדיוק פשוט</h3>
    <p>הדיוק הכולל נותן תמונה כללית, אבל **מטריצת הבלבול** היא כלי עוצמתי יותר להבנת הביצועים. היא חושפת אילו רגשות הרשת מזהה היטב ואילו רגשות היא נוטה לבלבל ביניהם. לדוגמה, ייתכן שהיא תתקשה להבדיל בין קול עצבני לקול שמח מאוד, שכן שניהם יכולים להתאפיין בטון גבוה או עוצמה רבה.</p>

    <h3>למי זה טוב? יישומים בעולם האמיתי</h3>
    <p>טכנולוגיית זיהוי רגשות בקול פותחת דלתות ליישומים רבים:</p>
    <ul>
        <li>**שיפור שירות לקוחות:** זיהוי לקוחות מתוסכלים והעברתם לנציג המתאים.</li>
        <li>**בריאות דיגיטלית:** ניטור שינויים במצב רוח או סימני דיכאון/חרדה באמצעות ניתוח דיבור.</li>
        <li>**חינוך מקוון:** זיהוי תלמידים משועממים או מתוסכלים.</li>
        <li>**שיווק ומדיה:** ניתוח תגובות רגשיות לתוכן.</li>
        <li>**עוזרים קוליים חכמים יותר:** תגובה רגישה יותר לרגשות המשתמש.</li>
    </ul>
    <p class="outro-text">כפי שראיתם בסימולטור, אימון מודלים כאלו דורש איזון עדין של פרמטרים והבנה של תהליך הלמידה. זוהי רק טעימה קטנה מהעולם העשיר של למידת מכונה ובינה מלאכותית!</p>
</div>

<style>
/* --- General Styles --- */
body {
    font-family: 'Heebo', sans-serif; /* Added a modern Hebrew-friendly font (requires linking) */
    line-height: 1.7;
    margin: 0;
    padding: 20px;
    direction: rtl;
    text-align: right;
    color: #333;
    background-color: #f4f7f6; /* Soft background */
}

h1, h2, h3 {
    color: #2c3e50; /* Darker blue-grey */
    text-align: right;
    margin-bottom: 15px;
}

h1 {
    border-bottom: 2px solid #3498db; /* Accent color */
    padding-bottom: 10px;
    margin-bottom: 25px;
}

h2 {
    color: #3498db; /* Accent color */
    margin-top: 25px;
}

h3 {
    color: #555;
    margin-top: 20px;
}

p {
    margin-bottom: 15px;
}

.intro-text, .outro-text {
    font-size: 1.1em;
    color: #555;
    margin-bottom: 25px;
}

/* --- App Container --- */
#app-container, #explanation {
    background-color: #ffffff; /* White background for main sections */
    border: 1px solid #e0e0e0; /* Subtle border */
    border-radius: 12px; /* More rounded corners */
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); /* Soft shadow */
}

/* --- Controls Panel --- */
.control-panel {
    background-color: #ecf0f1; /* Light grey background */
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 30px;
}

.controls {
    display: grid; /* Use grid for more flexible layout */
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive columns */
    gap: 20px; /* Space between grid items */
    align-items: center;
}

.control-group {
    display: flex;
    flex-direction: column; /* Stack label and input */
    gap: 8px; /* Space between stacked items */
}

.controls label {
    font-weight: bold;
    color: #555;
    cursor: help; /* Indicate tooltip */
}

.controls input[type="number"] {
    padding: 10px 12px;
    border: 1px solid #bdc3c7; /* Soft border */
    border-radius: 6px;
    width: 100px; /* Fixed width */
    text-align: left;
    direction: ltr;
    font-size: 1em;
    transition: border-color 0.3s ease;
}

.controls input[type="number"]:focus {
    outline: none;
    border-color: #3498db; /* Highlight on focus */
    box-shadow: 0 0 5px rgba(52, 152, 219, 0.3);
}

button {
    background-color: #2ecc71; /* Green for action */
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    align-self: flex-end; /* Align button to the right */
     margin-top: 10px; /* Add space above button if stacked */
}

button:hover:not(:disabled) {
    background-color: #27ae60; /* Darker green on hover */
    transform: translateY(-1px); /* Subtle lift effect */
}

button:active:not(:disabled) {
     transform: translateY(0); /* Press effect */
}

button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    opacity: 0.7;
}

#toggleExplanationBtn {
    background-color: #95a5a6; /* Grey for less primary action */
    margin-top: 25px;
    margin-left: auto; /* Align right in RTL */
    margin-right: 0;
    display: block;
    width: auto;
    font-size: 1em;
    padding: 10px 20px;
}

#toggleExplanationBtn:hover:not(:disabled) {
     background-color: #7f8c8d;
     transform: none; /* No lift for this button */
}


/* --- Training Area --- */
#training-area {
    margin-top: 30px;
    border-top: 1px dashed #bdc3c7; /* Visual separator */
    padding-top: 20px;
}

#progress-container {
    display: flex;
    flex-direction: column; /* Stack output and chart */
    gap: 20px;
}

#progress-output {
    height: 200px; /* Fixed height */
    overflow-y: auto;
    border: 1px solid #bdc3c7;
    padding: 15px;
    background-color: #ecf0f1; /* Light grey for output */
    border-radius: 8px;
    white-space: pre-wrap;
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; /* Code font */
    font-size: 0.9em;
    color: #34495e; /* Dark text */
    direction: ltr;
    text-align: left;
    position: relative; /* For overlay */
}

/* Simple fading effect at bottom of progress output */
#progress-output::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 30px;
    background: linear-gradient(to bottom, rgba(236, 240, 241, 0), rgba(236, 240, 241, 1));
    pointer-events: none; /* Allow clicking through */
}


#accuracy-chart {
    height: 200px;
    border: 1px solid #bdc3c7;
    border-radius: 8px;
    background-color: #ffffff;
    display: flex;
    flex-direction: row; /* Bars side by side */
    align-items: flex-end; /* Bars grow from bottom */
    overflow-x: auto; /* Scroll if many epochs */
    overflow-y: hidden; /* Hide vertical scroll */
    white-space: nowrap;
    padding: 10px 5px; /* Padding inside chart */
    position: relative; /* For overlay positioning */
}

.chart-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none; /* Ignore clicks on overlay */
}

.chart-y-axis {
    position: absolute;
    top: 0;
    bottom: 0;
    right: 10px; /* Position on the right for RTL */
    width: 40px; /* Width for labels */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start; /* Align labels to the left */
    font-size: 0.8em;
    color: #7f8c8d;
    border-left: 1px dashed #ccc; /* Simple Y axis line */
}

.chart-y-axis span {
     background-color: #ffffff; /* Mask background under text */
     padding: 0 5px;
     transform: translateY(50%); /* Center text vertically */
}

.chart-legend {
     position: absolute;
     top: 10px;
     left: 10px; /* Position on the left */
     font-size: 0.9em;
     color: #555;
     background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
     padding: 5px 10px;
     border-radius: 4px;
     direction: rtl; /* Legend text is RTL */
}

.chart-legend span {
    display: inline-block;
    width: 15px;
    height: 15px;
    margin-left: 5px; /* Space between color box and text */
    vertical-align: middle;
    border-radius: 3px;
}

.legend-train { background-color: #3498db; } /* Train color */
.legend-val { background-color: #e74c3c; } /* Validation color */


.accuracy-bar-group {
    display: flex;
    flex-direction: row-reverse; /* Put train bar on the left, val on the right (in LTR chart direction) */
    height: 100%; /* Takes full height of chart area */
    margin-right: 2px; /* Space between epoch groups */
    align-items: flex-end; /* Bars grow upwards */
     flex-shrink: 0; /* Prevent shrinking */
    width: 8px; /* Total width for the group (e.g., 4px per bar + 0px space) */
}

.accuracy-bar {
    width: 4px; /* Width for each individual bar */
    height: 0%; /* Start at 0 */
    transition: height 0.3s ease-out; /* Smooth growth animation */
}

.accuracy-bar.train {
    background-color: #3498db; /* Train color */
}

.accuracy-bar.validation {
    background-color: #e74c3c; /* Validation color (reddish) */
    margin-left: 0px; /* No space between bars in the group */
}


/* --- Results Area --- */
#results {
    margin-top: 30px;
    border-top: 1px dashed #bdc3c7;
    padding-top: 20px;
}

.final-accuracy-display {
     font-size: 1.2em;
     font-weight: bold;
     color: #27ae60; /* Green accent */
}

.final-accuracy-display span {
    color: #333; /* Keep number color dark */
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
}

/* Confusion Matrix */
#confusion-matrix-table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 15px;
    text-align: center;
    direction: ltr; /* Table layout visually LTR */
    font-size: 0.95em;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

#confusion-matrix-table th,
#confusion-matrix-table td {
    border: 1px solid #dddddd;
    padding: 12px 8px; /* Adjusted padding */
    min-width: 70px; /* Ensure cells are wide enough */
}

#confusion-matrix-table thead tr:first-child th {
     background-color: #e0e0e0; /* Light grey header */
     font-weight: bold;
     color: #333;
}

/* Style for the top-left empty cell */
#confusion-matrix-table thead tr:first-child th:first-child {
     background: none;
     border-top: none;
     border-left: none;
     border-bottom: none;
}

/* Style for the "Actual" labels column */
#confusion-matrix-table tbody th {
     text-align: right;
     background-color: #f2f2f2; /* Slightly darker grey for row headers */
     font-weight: bold;
     color: #555;
}

/* Diagonal cells (correct predictions) */
#confusion-matrix-table td[data-emotion$="-happy"][data-emotion^="happy"],
#confusion-matrix-table td[data-emotion$="-sad"][data-emotion^="sad"],
#confusion-matrix-table td[data-emotion$="-angry"][data-emotion^="angry"],
#confusion-matrix-table td[data-emotion$="-neutral"][data-emotion^="neutral"] {
    background-color: #e8f5e9; /* Very light green */
    font-weight: bold;
    color: #1b5e20; /* Dark green text */
}

/* Off-diagonal cells (incorrect predictions) */
#confusion-matrix-table td:not([data-emotion$="-happy"][data-emotion^="happy"]):not([data-emotion$="-sad"][data-emotion^="sad"]):not([data-emotion$="-angry"][data-emotion^="angry"]):not([data-emotion$="-neutral"][data-emotion^="neutral"]) {
     background-color: #ffebee; /* Very light red */
     color: #c62828; /* Dark red text */
}


.matrix-note {
    font-size: 0.9em;
    color: #555;
    margin-top: 10px;
    text-align: right;
}


/* --- Explanation Area --- */
#explanation {
    background-color: #ebf5fb; /* Light blueish background */
    border-color: #aed6f1;
}

#explanation h2 {
     color: #2980b9; /* Darker blue */
}

#explanation ul {
    list-style-type: disc;
    margin-right: 25px; /* Indent list for RTL */
    padding-right: 0;
}

#explanation li {
    margin-bottom: 12px;
    line-height: 1.6;
}

#explanation strong {
    color: #34495e; /* Dark text for emphasis */
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .controls {
        grid-template-columns: 1fr; /* Stack controls on smaller screens */
    }

    .control-group {
         flex-direction: row; /* Row layout for label and input */
         justify-content: space-between;
         align-items: center;
    }

     .controls input[type="number"] {
          width: 100px; /* Keep fixed width */
     }

    button {
         width: 100%; /* Full width button */
         text-align: center;
         align-self: stretch; /* Stretch in grid item */
    }

    #toggleExplanationBtn {
         width: 100%;
         margin: 20px 0; /* Center button */
         text-align: center;
    }

     #accuracy-chart {
          height: 150px; /* Reduce chart height */
     }

     #confusion-matrix-table th,
     #confusion-matrix-table td {
          padding: 8px 4px; /* Reduce table padding */
          min-width: 50px;
          font-size: 0.9em;
     }

     .chart-y-axis {
          width: 30px; /* Reduce y-axis label width */
     }
}

</style>

<script>
// Function to simulate training progress
function simulateTraining(learningRate, epochs, updateCallback) {
    return new Promise((resolve) => {
        let currentTrainAccuracy = 0.20; // Start with low accuracy
        let currentValidationAccuracy = 0.15;
        const baseTargetAccuracy = 0.80;

        // Calculate target accuracy based on params, with some randomness and caps
        // Higher LR speeds up convergence but might overshoot or oscillate (simulated via randomness later)
        // More epochs allow potentially higher max accuracy, but risk overfitting
        const effectiveLR = Math.pow(learningRate * 10, 0.5); // Non-linear effect of LR
        const epochFactor = Math.min(1, epochs / 150); // Epochs contribute up to a point
        const targetBase = 0.40 + (baseTargetAccuracy - 0.40) * effectiveLR * epochFactor;
        const targetValidationAccuracy = Math.min(0.92, Math.max(0.30, targetBase + (Math.random() - 0.5) * 0.05)); // Add slight randomness to final target

        const interval = 60; // Time between epoch updates in ms - slightly slower for better visual
        const totalSteps = epochs; // Total steps for simulation

        let epoch = 0;
        const intervalId = setInterval(() => {
            epoch++;

            // Simulate progress towards target
            // Train accuracy increases generally faster than validation
            let trainGain = (targetValidationAccuracy * 1.05 - currentTrainAccuracy) * 0.1 * effectiveLR;
            trainGain += (Math.random() - 0.5) * (learningRate * 2); // Add noise scaled by LR
            currentTrainAccuracy += trainGain;
            currentTrainAccuracy = Math.min(currentTrainAccuracy, 0.99); // Cap train accuracy below 100%

            let valGain = (targetValidationAccuracy - currentValidationAccuracy) * 0.08 * effectiveLR;
            valGain += (Math.random() - 0.5) * (learningRate * 1.5); // Add less noise to val scaled by LR
            currentValidationAccuracy += valGain;

            // Simulate overfitting: val accuracy plateaus or drops if epochs are high and train accuracy is much higher
            const overfittingStartEpoch = epochs * 0.6; // Start considering overfitting after 60% of epochs
            if (epoch > overfittingStartEpoch && currentTrainAccuracy > currentValidationAccuracy * 1.05) {
                const overfittingMagnitude = (epoch - overfittingStartEpoch) / (epochs - overfittingStartEpoch) * (currentTrainAccuracy - currentValidationAccuracy) * 0.2;
                 currentValidationAccuracy -= overfittingMagnitude * (learningRate * 5); // Overfitting drop scaled by LR
                 currentValidationAccuracy = Math.max(currentValidationAccuracy, targetValidationAccuracy * 0.8); // Don't drop below a certain point relative to target
            }

             currentValidationAccuracy = Math.min(currentValidationAccuracy, currentTrainAccuracy * 1.01); // Validation can briefly exceed train due to noise, but generally lags
             currentValidationAccuracy = Math.max(0.05, currentValidationAccuracy); // Minimum accuracy

            // Ensure accuracy values stay within reasonable bounds
            currentTrainAccuracy = Math.max(0.05, Math.min(0.99, currentTrainAccuracy));
            currentValidationAccuracy = Math.max(0.05, Math.min(0.95, currentValidationAccuracy));


            updateCallback(epoch, currentTrainAccuracy, currentValidationAccuracy);

            if (epoch >= epochs) {
                clearInterval(intervalId);
                const finalValidationAccuracy = Math.round(currentValidationAccuracy * 1000) / 1000; // Round for display

                // Generate simulated confusion matrix based on final validation accuracy
                const emotions = ['happy', 'sad', 'angry', 'neutral'];
                const matrix = {};
                const totalSamples = 200; // Simulate total validation samples for matrix

                emotions.forEach(actual => {
                    matrix[actual] = {};
                    emotions.forEach(predicted => {
                        matrix[actual][predicted] = 0;
                    });
                });

                const correctPredictions = Math.round(totalSamples * finalValidationAccuracy);
                const incorrectPredictions = totalSamples - correctPredictions;

                // Distribute correct predictions diagonally
                let remainingCorrect = correctPredictions;
                emotions.forEach(emotion => {
                     // Give a base amount, weighted slightly by overall accuracy
                    const base = Math.floor(correctPredictions / emotions.length * (1 + finalValidationAccuracy * 0.5));
                    matrix[emotion][emotion] = base;
                    remainingCorrect -= base;
                });

                // Add/subtract any remaining correct count due to rounding/base distribution
                let emotionIndex = 0;
                while(remainingCorrect !== 0) {
                    const emotion = emotions[emotionIndex % emotions.length];
                    const change = Math.sign(remainingCorrect);
                    matrix[emotion][emotion] += change;
                    remainingCorrect -= change;
                    emotionIndex++;
                    if (emotionIndex > emotions.length * 2) break; // Prevent infinite loop in case of issues
                }

                // Ensure no negative counts and sum is plausible
                 emotions.forEach(emotion => matrix[emotion][emotion] = Math.max(0, matrix[emotion][emotion]));


                // Distribute incorrect predictions off-diagonal
                let remainingIncorrect = incorrectPredictions;
                 const potentialErrors = [];
                 emotions.forEach(actual => {
                      emotions.forEach(predicted => {
                           if (actual !== predicted) {
                              potentialErrors.push({actual: actual, predicted: predicted});
                           }
                      });
                 });

                // Distribute the incorrect count - maybe slightly more common between 'similar' emotions (e.g. angry/happy due to energy, sad/neutral)
                 const confusionPairs = {
                     'angry-happy': 1.2, 'happy-angry': 1.2, // High energy confusion
                     'sad-neutral': 1.3, 'neutral-sad': 1.3, // Low energy/arousal confusion
                     'angry-neutral': 1.1, 'neutral-angry': 1.1,
                     'happy-neutral': 1.0, 'neutral-happy': 1.0
                     // Other pairs get base 1.0 implicitly
                 };

                 let totalWeight = potentialErrors.reduce((sum, pair) => {
                      const key = `${pair.actual}-${pair.predicted}`;
                      return sum + (confusionPairs[key] || 1.0);
                 }, 0);

                 potentialErrors.forEach(pair => {
                      const key = `${pair.actual}-${pair.predicted}`;
                      const weight = confusionPairs[key] || 1.0;
                      const count = Math.round(incorrectPredictions * (weight / totalWeight));
                      matrix[pair.actual][pair.predicted] = count;
                      remainingIncorrect -= count;
                 });

                 // Distribute remaining incorrect count due to rounding
                 let errorIndex = 0;
                  while(remainingIncorrect !== 0) {
                      const pair = potentialErrors[errorIndex % potentialErrors.length];
                       const change = Math.sign(remainingIncorrect);
                      matrix[pair.actual][pair.predicted] += change;
                       remainingIncorrect -= change;
                       errorIndex++;
                       if (errorIndex > potentialErrors.length * 2) break; // Prevent infinite loop
                  }

                 // Ensure no negative counts
                 potentialErrors.forEach(pair => matrix[pair.actual][pair.predicted] = Math.max(0, matrix[pair.actual][pair.predicted]));


                 // Final check on total samples (should be close to totalSamples)
                 let currentTotal = 0;
                  emotions.forEach(actual => {
                      emotions.forEach(predicted => {
                           currentTotal += matrix[actual][predicted];
                      });
                  });

                  // Adjust if total is slightly off due to multiple rounding steps
                  if (currentTotal !== totalSamples) {
                       const diff = totalSamples - currentTotal;
                       // Adjust diagonal entries slightly
                       emotions.forEach((emotion, index) => {
                            if (diff === 0) return;
                            const change = Math.sign(diff);
                            matrix[emotion][emotion] += change;
                            matrix[emotion][emotion] = Math.max(0, matrix[emotion][emotion]);
                            diff -= change;
                       });
                  }


                resolve({ finalAccuracy: finalValidationAccuracy, confusionMatrix: matrix });
            }
        }, interval);
    });
}


document.addEventListener('DOMContentLoaded', () => {
    const startTrainingBtn = document.getElementById('startTrainingBtn');
    const learningRateInput = document.getElementById('learningRate');
    const epochsInput = document.getElementById('epochs');
    const progressOutput = document.getElementById('progress-output');
    const accuracyChart = document.getElementById('accuracy-chart');
    const resultsDiv = document.getElementById('results');
    const finalAccuracySpan = document.getElementById('final-accuracy');
    const confusionMatrixTable = document.getElementById('confusion-matrix-table');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationDiv = document.getElementById('explanation');

     // Append Heebo font link (requires external network access, but improves design)
     const link = document.createElement('link');
     link.href = 'https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap';
     link.rel = 'stylesheet';
     document.head.appendChild(link);


    // Toggle Explanation
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'פחות מעמיק: הסתר הסבר' : 'מעמיק יותר: מה עומד מאחורי הסימולטור?';
         // Scroll to explanation if showing
         if (isHidden) {
              explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });


    startTrainingBtn.addEventListener('click', async () => {
        const learningRate = parseFloat(learningRateInput.value);
        const epochs = parseInt(epochsInput.value);

        if (isNaN(learningRate) || isNaN(epochs) || learningRate <= 0 || epochs <= 0) {
            alert('הו! יש להזין מספרים חיוביים עבור קצב למידה ומספר עידנים כדי שהאימון יוכל להתחיל.');
            return;
        }
         if (learningRate > 0.08 || epochs > 150) {
              // Gentle warning for high values
              progressOutput.innerHTML += `<p style="color:orange; font-weight:bold;">שים לב: ערכים גבוהים מדי עלולים לגרום למודל לזגזג או לפתח "זיכרון יתר" (התאמת יתר) בסימולציה זו.</p>`;
         }


        // Disable controls during training
        startTrainingBtn.disabled = true;
        learningRateInput.disabled = true;
        epochsInput.disabled = true;

        // Reset display areas
        progressOutput.innerHTML = ''; // Clear output
        accuracyChart.innerHTML = ''; // Clear chart
         // Re-add the chart overlay which was cleared
         const chartOverlay = document.createElement('div');
         chartOverlay.className = 'chart-overlay';
         chartOverlay.innerHTML = `
            <div class="chart-y-axis"><span>100%</span><span>50%</span><span>0%</span></div>
            <div class="chart-legend">
                 <span class="legend-train"></span> דיוק אימון
                 <span class="legend-val"></span> דיוק ולידציה
            </div>
         `;
         accuracyChart.appendChild(chartOverlay);

        resultsDiv.style.display = 'none';


        // Add initial message
         const initialP = document.createElement('p');
         initialP.textContent = `מתחיל אימון... מכוון את מוח המכונה עם קצב למידה של ${learningRate} עבור ${epochs} עידנים. צפו במסלול הלמידה!`;
         initialP.style.color = '#34495e'; // Darker initial message
         progressOutput.appendChild(initialP);
         progressOutput.scrollTop = progressOutput.scrollHeight; // Auto-scroll to bottom


        // Simulate training
        const finalResults = await simulateTraining(learningRate, epochs, (epoch, trainAcc, valAcc) => {
             // Append progress message
             const p = document.createElement('p');
             p.textContent = `עידן ${epoch}/${epochs}: אימון=${(trainAcc * 100).toFixed(1)}%, ולידציה=${(valAcc * 100).toFixed(1)}%`;
             progressOutput.appendChild(p);
             // Keep output clean if it gets too long (optional, might remove oldest)
             // if (progressOutput.children.length > epochs + 5) { progressOutput.removeChild(progressOutput.firstElementChild); }
             progressOutput.scrollTop = progressOutput.scrollHeight; // Auto-scroll

             // Add bars to the chart
             const barGroup = document.createElement('div');
             barGroup.className = 'accuracy-bar-group';

             const trainBar = document.createElement('div');
             trainBar.className = 'accuracy-bar train';
             // Set height after appending for CSS transition effect
             setTimeout(() => { trainBar.style.height = `${Math.max(0, trainAcc * 100)}%`; }, 10); // Ensure height update triggers transition

             const valBar = document.createElement('div');
             valBar.className = 'accuracy-bar validation';
              // Set height after appending
             setTimeout(() => { valBar.style.height = `${Math.max(0, valAcc * 100)}%`; }, 10); // Ensure height update triggers transition


             barGroup.appendChild(trainBar);
             barGroup.appendChild(valBar);
             accuracyChart.appendChild(barGroup);

             // Auto-scroll chart to the right to see latest epochs
             accuracyChart.scrollLeft = accuracyChart.scrollWidth;
        });

        // Training finished, display results
        resultsDiv.style.display = 'block';

        finalAccuracySpan.textContent = `${(finalResults.finalAccuracy * 100).toFixed(1)}%`;

        // Update Confusion Matrix table
        const matrix = finalResults.confusionMatrix;
         // Assuming table headers are already in the correct order (שמחה, עצב, כעס, ניטרלי) mapping to (happy, sad, angry, neutral)
        const emotionKeysOrdered = ['happy', 'sad', 'angry', 'neutral'];

        emotionKeysOrdered.forEach(actualKey => {
            emotionKeysOrdered.forEach(predictedKey => {
                // Cell selector uses the data attribute set in HTML
                const cell = confusionMatrixTable.querySelector(`td[data-emotion="${actualKey}-${predictedKey}"]`);
                if (cell) {
                     const value = matrix[actualKey] ? matrix[actualKey][predictedKey] : 0; // Default to 0 if somehow missing
                     cell.textContent = value; // Display the count
                }
            });
        });


        // Re-enable controls
        startTrainingBtn.disabled = false;
        learningRateInput.disabled = false;
        epochsInput.disabled = false;

         // Add final message
         const finalP = document.createElement('p');
         finalP.textContent = `--- האימון הסתיים! המודל הגיע לדיוק סופי של ${(finalResults.finalAccuracy * 100).toFixed(1)}% על נתוני הבחינה. צפו בתוצאות המפורטות למטה. ---`;
         finalP.style.color = '#1b5e20'; /* Green for success */
         finalP.style.fontWeight = 'bold';
         progressOutput.appendChild(finalP);
         progressOutput.scrollTop = progressOutput.scrollHeight;

         // Scroll to results
         resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});
</script>
---