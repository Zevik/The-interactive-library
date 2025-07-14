---
title: "לראות את הבלתי נראה: כך עובד מיקרוסקופ אלקטרונים חודר (TEM)"
english_slug: seeing-the-unseen-how-tem-works
category: "מדעים מדויקים / פיזיקה"
tags:
  - מיקרוסקופ אלקטרונים
  - TEM
  - הדמיה מדעית
  - פיזיקה שימושית
  - מדע חומרים
---

# לראות את הבלתי נראה: מסע אל הלב של החומר עם מיקרוסקופ אלקטרונים חודר (TEM)

איך חוקרים פורצים את גבולות הראייה האנושית וחודרים אל העולם הננומטרי, עמוק לתוך מבנה החומר? מיקרוסקופ האור נעצר בגבולות הפיזיקה, אך הצורך לראות אטומים ומבנים זעירים רק גדל. מהו הכלי המופלא שמשגר "אור" בעל אורך גל קצר לאין שיעור ומאפשר לנו לחשוף את סודותיו הפנימיים ביותר של החומר ברזולוציות עוצרות נשימה?

<div class="tem-simulation-container">
    <div class="tem-diagram">
        <div class="component electron-source pulse">מקור אלקטרונים</div>
        <div class="component lens condenser-lens">עדשות עיבוי</div>
        <div class="component sample-holder">דוגמה דקה</div>
         <div class="beam-after-sample" id="beamAfterSample"></div>
        <div class="component lens objective-lens">עדשת אובייקטיב</div>
        <div class="component lens projector-lens">עדשות הטלה</div>
        <div class="component detector">גלאי / מסך פלואורסצנטי</div>

        <div class="electron-beam" id="electronBeam"></div>
        <div class="tem-screen" id="temScreen">
            <div class="screen-image"></div>
        </div>
    </div>

    <div class="controls">
        <button id="startButton" class="control-button primary">הפעל אלומת אלקטרונים</button>
        <button id="stopButton" class="control-button secondary" disabled>עצור אלומה</button>
        <div class="control-group">
            <label for="focusControl">כוון מיקוד (עדשות):</label>
            <input type="range" id="focusControl" min="0.5" max="1.5" step="0.05" value="1">
             <span class="range-value" id="focusValueDisplay">ממוקד</span>
        </div>
        <div class="control-group">
            <label for="sampleDensity">צפיפות דוגמה (להדגמת פיזור):</label>
            <input type="range" id="sampleDensity" min="0" max="10" step="1" value="5">
             <span class="range-value" id="densityValueDisplay">בינונית</span>
        </div>
    </div>
</div>

<style>
:root {
    --electron-beam-color: #4DD0E1; /* Cyan */
    --scatter-beam-color: #FFAB91; /* Light Orange */
    --component-bg: #CFD8DC; /* Light blue-grey */
    --lens-bg: #A5D6A7; /* Light green */
    --source-bg: #FFCCBC; /* Light red */
    --sample-bg: #B39DDB; /* Light purple */
    --detector-bg: #FFF59D; /* Light yellow */
    --screen-bg: #263238; /* Dark blue-grey */
    --container-bg: #ECEFF1; /* Very light blue-grey */
    --control-bg: #FFFFFF;
    --primary-button: #039BE5; /* Blue */
    --secondary-button: #78909C; /* Grey-blue */
    --text-color: #37474F; /* Dark blue-grey */
    --border-color: #B0BEC5; /* Light blue-grey border */
}

.tem-simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: 'Heebo', sans-serif; /* Prefer Heebo for Hebrew */
    background-color: var(--container-bg);
    padding: 30px;
    border-radius: 12px;
    margin: 20px auto;
    max-width: 500px; /* Limit max width for better visual balance */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    color: var(--text-color);
}

.tem-diagram {
    position: relative;
    width: 100%; /* Make diagram responsive within container */
    max-width: 400px; /* Limit diagram width */
    height: 650px; /* Increased height */
    border: 1px solid var(--border-color);
    background-color: var(--screen-bg); /* Dark background for vacuum */
    margin-bottom: 20px;
    border-radius: 8px;
    overflow: hidden; /* Hide overflow from beams */
}

.component {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 180px; /* Wider components */
    text-align: center;
    padding: 10px 5px; /* Increased padding */
    border: 1px solid var(--border-color);
    border-radius: 6px; /* Rounded corners */
    font-size: 0.9em;
    font-weight: bold;
    color: var(--text-color);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.electron-source {
    top: 30px;
    background-color: var(--source-bg);
}

/* Simple pulse animation for source */
.electron-source.pulse {
    animation: pulse-glow 1.5s infinite ease-in-out;
}

@keyframes pulse-glow {
    0% { box-shadow: 0 0 5px var(--source-bg); }
    50% { box-shadow: 0 0 15px var(--source-bg); }
    100% { box-shadow: 0 0 5px var(--source-bg); }
}


.lens {
    height: 30px;
    background-color: var(--lens-bg);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative; /* For potential inner lens visual */
    font-size: 0.8em;
}
.lens::after { /* Visual indicator for magnetic field */
    content: '';
    position: absolute;
    top: -5px; bottom: -5px; left: -5px; right: -5px;
    border: 2px dashed rgba(165, 214, 167, 0.5); /* Lighter dashed border */
    border-radius: 8px;
    z-index: 0;
}


.condenser-lens {
    top: 120px;
}

.sample-holder {
    top: 280px; /* Adjusted position */
    width: 120px; /* Wider sample area */
    height: 25px; /* Thicker sample visual */
    background-color: var(--sample-bg);
    border: 2px solid var(--border-color);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.8em;
    z-index: 1; /* Ensure sample is above beam */
}

/* Container for scattered beams below sample */
.beam-after-sample {
    position: absolute;
    top: 305px; /* Just below sample */
    left: 0;
    width: 100%;
    height: 200px; /* Area where beams diverge */
    overflow: hidden;
     z-index: 0; /* Below components */
}

.objective-lens {
    top: 400px; /* Adjusted position */
}

.projector-lens {
    top: 500px; /* Adjusted position */
}

.detector {
    bottom: 30px; /* Adjusted position */
    width: 220px; /* Wider detector */
    height: 60px; /* Taller detector */
    background-color: var(--detector-bg);
    display: flex;
    justify-content: center;
    align-items: center;
     font-size: 0.8em;
     z-index: 1; /* Ensure detector is above screen */
}

.tem-screen {
    position: absolute;
    bottom: 35px; /* Just above detector */
    left: 50%;
    transform: translateX(-50%);
    width: 210px; /* Matches detector width minus padding */
    height: 50px; /* Matches detector height minus padding */
    background-color: var(--screen-bg);
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 4px;
    overflow: hidden;
    z-index: 2; /* Above detector base */
    border: 2px inset rgba(0,0,0,0.2); /* Give it a recessed look */
}

.screen-image {
    width: 95%;
    height: 90%;
    background-color: #555; /* Default dark state */
    display: none; /* Hidden until beam hits */
    transition: filter 0.3s ease-out, background-image 0.3s ease-out; /* Smooth transitions for visual changes */
    background-size: cover; /* Ensure simulated pattern covers area */
    background-position: center;
    /* Add a simple simulated pattern */
     background-image:
         repeating-linear-gradient(0deg, #333, #333 1px, #555 1px, #555 3px),
         repeating-linear-gradient(90deg, #333, #333 1px, #555 1px, #555 3px);
     filter: brightness(0.5); /* Start dark */
}

.electron-beam {
    position: absolute;
    top: 80px; /* Below source */
    left: 50%;
    transform: translateX(-50%);
    width: 15px; /* Initial beam width */
    height: 520px; /* Goes down to screen area */
    background: linear-gradient(to bottom,
                var(--electron-beam-color) 0%,
                rgba(77, 208, 225, 0.8) 20%,
                rgba(77, 208, 225, 0.5) 50%, /* Fades slightly */
                 rgba(77, 208, 225, 0.2) 80%,
                rgba(77, 208, 225, 0) 100%);
    display: none; /* Initially hidden */
    animation: beam-pulse-flow 1s linear infinite; /* Combined flow and subtle pulse */
    transform-origin: top center; /* Scale/skew from the source */
    will-change: transform; /* Optimize animation */
}

@keyframes beam-pulse-flow {
     0% { background-position-y: 0; opacity: 0.9; }
     50% { opacity: 1; }
    100% { background-position-y: 50px; opacity: 0.9; }
}

/* Scattered beams */
.scattered-beam-line {
    position: absolute;
    bottom: 0; /* Start from below sample */
    left: 50%;
    width: 2px;
    height: 1px; /* Will grow */
    background-color: var(--scatter-beam-color);
    transform-origin: bottom center;
    animation: scatter-animation 0.8s ease-out forwards;
     opacity: 0; /* Start invisible */
}

@keyframes scatter-animation {
    0% { transform: translateX(-1px) rotate(0deg) scaleY(0); opacity: 1; }
    50% { opacity: 1; }
    100% { transform: translateX(-1px) rotate(var(--angle)) scaleY(var(--length)); opacity: 0; } /* Fade out */
}


.controls {
    display: flex;
    flex-direction: column;
    gap: 15px; /* Increased gap */
    width: 100%;
    max-width: 400px;
    padding: 20px; /* Increased padding */
    border: 1px solid var(--border-color);
    background-color: var(--control-bg);
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
}

.control-group {
     display: flex;
     flex-direction: column;
     gap: 8px;
}

.controls label {
    font-weight: bold;
    font-size: 1em;
    color: var(--text-color);
}

.controls input[type="range"] {
    width: 100%;
    -webkit-appearance: none; /* Override default styles */
    appearance: none;
    height: 8px; /* Thicker slider track */
    background: var(--container-bg);
    outline: none;
    border-radius: 4px;
    transition: background 0.2s ease-in-out;
}

.controls input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px; /* Thicker slider thumb */
    height: 20px;
    background: var(--primary-button);
    border-radius: 50%;
    cursor: pointer;
    transition: background 0.2s ease-in-out, transform 0.1s ease-in-out;
     box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}
.controls input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: var(--primary-button);
    border-radius: 50%;
    cursor: pointer;
     transition: background 0.2s ease-in-out, transform 0.1s ease-in-out;
      box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

.controls input[type="range"]:hover::-webkit-slider-thumb {
    background: #0277BD; /* Darker blue */
    transform: scale(1.1);
}
.controls input[type="range"]:hover::-moz-range-thumb {
    background: #0277BD;
     transform: scale(1.1);
}

.range-value {
     display: block;
     text-align: center;
     font-size: 0.9em;
     color: #546E7A; /* Muted grey */
}


.control-button {
    padding: 10px 20px; /* Increased padding */
    color: white;
    border: none;
    border-radius: 6px; /* Rounded buttons */
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.2s ease-in-out, opacity 0.2s ease-in-out;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.control-button.primary {
    background-color: var(--primary-button);
}

.control-button.primary:hover:not(:disabled) {
    background-color: #0277BD; /* Darker blue */
}

.control-button.secondary {
     background-color: var(--secondary-button);
}
.control-button.secondary:hover:not(:disabled) {
     background-color: #546E7A; /* Darker grey-blue */
}


.control-button:disabled {
    background-color: #B0BEC5; /* Lighter grey */
    cursor: not-allowed;
    opacity: 0.7;
     box-shadow: none;
}


#explanation {
    display: none;
    margin-top: 20px;
    padding: 25px; /* Increased padding */
    border: 1px solid var(--border-color);
    border-radius: 12px;
    background-color: var(--control-bg);
    line-height: 1.7; /* Increased line height for readability */
    color: var(--text-color);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
}

#explanation h2, #explanation h3 {
    color: #263238; /* Darker text */
    margin-top: 20px; /* More space above headers */
    margin-bottom: 10px;
     border-bottom: 1px solid var(--container-bg); /* Subtle separator */
     padding-bottom: 5px;
}

#explanation p {
    margin-bottom: 15px; /* More space between paragraphs */
}

#explanation ul {
    margin-bottom: 15px;
    padding-left: 20px;
}
#explanation li {
    margin-bottom: 8px;
}

#toggleExplanation {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #607D8B; /* Muted blue-grey */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease-in-out;
     box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

#toggleExplanation:hover {
    background-color: #546E7A; /* Darker muted blue-grey */
}

</style>

<button id="toggleExplanation">הצג הסבר מפורט</button>

<div id="explanation">
    <h2>המסע הפנימי: פירוט על עקרונות מיקרוסקופ אלקטרונים חודר (TEM)</h2>

    <h3>למה אלקטרונים? מעבר מגבול האור לגבול הקוונטי</h3>
    <p>היכולת לראות פרטים עדינה תלויה באורך הגל של ה"אור" בו משתמשים. מיקרוסקופ האור, המשתמש באור נראה בעל אורך גל של מאות ננומטרים, מוגבל ברזולוציה שלו ולא יכול להבחין בעצמים הקטנים מחצי אורך הגל (כ-200 ננומטר). כדי לפרוץ את המחסום הזה ולהגיע לרזולוציה אטומית, נדרשת "קרינה" בעלת אורך גל קצר בהרבה. כאן נכנסים לתמונה האלקטרונים. על פי עקרונות מכניקת הקוונטים (הידועים כדואליות גל-חלקיק), אלקטרונים בתנועה מתנהגים גם כגלים. כאשר אלקטרונים מואצים במתח גבוה במיוחד (עשרות ואף מאות אלפי וולט), הם מגיעים למהירויות אדירות ואורך הגל שלהם (אורך גל דה ברוגלי) הופך קצר ביותר - לעיתים קטן אפילו מגודל אטום בודד. אורך גל זעיר זה הוא סוד הרזולוציה הפנומנלית של ה-TEM.</p>

    <h3>הארכיטקטורה הקסומה של TEM: מ"תותח" האלקטרונים ועד למסך המואר</h3>
    <p>דמיינו את ה-TEM כמגדל גבוה בתוך ואקום, בו נורים אלקטרונים ומתנהלים במסע מבוקר ליצירת תמונה. מבנהו דומה עקרונית למיקרוסקופ אור, אך ההבדלים הטכנולוגיים מהותיים:</p>
    <ul>
        <li>**מקור האלקטרונים (Electron Source):** בראש המגדל, "תותח" אלקטרונים משחרר זרם יציב של אלקטרונים. בדרך כלל נעשה זאת על ידי חימום חוט (כמו בנורת ליבון, אך בוואקום) או באמצעות שדה חשמלי חזק. האלקטרונים מואצים מיד אחר כך כלפי מטה על ידי מתח גבוה מאוד.</li>
        <li>**עדשות עיבוי (Condenser Lenses):** אלו אינן עדשות זכוכית, אלא סלילים אלקטרומגנטיים שיוצרים שדות מגנטיים חזקים. שדות אלו פועלים כמו עדשות אופטיות, מרכזים ומעצבים את אלומת האלקטרונים המואצת, מכוונים אותה לדוגמה ומקבעים את "שטף" האלקטרונים הפוגעים בה.</li>
        <li>**דוגמת החומר (Sample):** ליבת הסיפור! כאן הדרישה המגבילה ביותר: הדוגמה חייבת להיות דקה במיוחד - סדר גודל של עשרות עד מאות ננומטרים בודדים. הסיבה? האלקטרונים צריכים להיות מסוגלים <b>לעבור</b> דרכה. הדוגמה מונחת על רשת עדינה ומקובעת במחזיק מיוחד המאפשר הזזה ובחירת האזור שייבחן.</li>
        <li>**אינטראקציה עם הדוגמה: מעבר, פיזור ובליעה:** זהו הרגע הקריטי. כשהאלומה פוגעת בדוגמה, רוב האלקטרונים מקיימים אינטראקציה עם האטומים. אלקטרונים יכולים לעבור דרך אזורים דקים או פחות צפופים כמעט ללא סטייה. אך באזורים צפופים יותר, עבים יותר, או המכילים אטומים כבדים, האלקטרונים "יתפזרו" - יסטו ממסלולם המקורי בזוויות שונות עקב אינטראקציה עם גרעיני האטומים ואלקטרוני הליבה. חלק מהאלקטרונים אף ייבלעו לחלוטין או יאבדו אנרגיה רבה.</li>
        <li>**עדשת אובייקטיב (Objective Lens):** העדשה המשמעותית ביותר לרזולוציה. היא יושבת מיד לאחר הדוגמה ואחראית לאסוף את האלקטרונים שיצאו מהדוגמה (אלו שעברו ואלו שהתפזרו בזוויות קטנות) וליצור את התמונה הראשונית (תמונת הביניים). כיוון השדה המגנטי שלה קובע את המיקוד.</li>
        <li>**עדשות הטלה (Projector Lenses):** מערכת נוספת של עדשות אלקטרומגנטיות שמטרתן להגדיל את תמונת הביניים ולהטיל אותה על גלאי או מסך לצפייה. הן שקובעות את ההגדלה הסופית הנראית לעין או נלכדת דיגיטלית.</li>
        <li>**גלאי / מסך (Detector / Screen):** בתחתית המגדל. בעבר ועדיין בשימוש לצפייה מהירה, מסך פלואורסצנטי שפולט אור (זוהר) כאשר אלקטרונים פוגעים בו. כיום, רוב המיקרוסקופים משתמשים במצלמות דיגיטליות רגישות (CCD/CMOS) המסוגלות ללכוד את תמונת האלקטרונים שפגעו בהן ברזולוציה גבוהה לניתוח ממוחשב.</li>
    </ul>

    <h3>יצירת התמונה: הקונטרסט מגלה את המבנה</h3>
    <p>כיצד מתורגמות האינטראקציות של האלקטרונים עם הדוגמה לתמונה ויזואלית? התמונה ב-TEM נוצרת על ידי אלקטרונים ש<b>עברו</b> דרך הדוגמה והמשיכו בדרכם דרך העדשות אל הגלאי. אזורים בדוגמה שגרמו לפיזור רב של אלקטרונים (כלומר, פחות אלקטרונים המשיכו ישר קדימה) ייראו כהים יותר על המסך או הגלאי. הסיבה היא שפחות אלקטרונים פגעו באותו אזור בגלאי. לעומת זאת, אזורים שהאלקטרונים עברו דרכם בקלות יחסית ייראו בהירים יותר. ההבדלים בבהירות (הקונטרסט) בתמונת ה-TEM משקפים ישירות את ההבדלים במידת הפיזור או הבליעה של האלקטרונים באזורים שונים של הדוגמה הדקה. זהו הבסיס לקונטרסט מסה-עובי (Mass-Thickness Contrast) בו אזורים צפופים או עבים יותר נראים כהים יותר.</p>

    <p>סוג קונטרסט חשוב נוסף הוא **קונטרסט עקיפה (Diffraction Contrast)**, המשפיע על הדמיית חומרים גבישיים. כאשר אלומת אלקטרונים פוגעת בגביש, האלקטרונים יכולים לבצע עקיפה בזוויות ספציפיות התלויות במבנה הגבישי. ניתן להשתמש ב"פתח" (aperture) בעדשה כדי לחסום אלקטרונים שעברו עקיפה ולאפשר רק לאלו שלא עברו עקיפה ליצור את התמונה. במקרה כזה, אזורים גבישיים שיגרמו לעקיפה יופיעו כהים מאוד, מה שמאפשר לראות פגמים גבישיים כמו דיסלוקציות.</p>

    <h3>מעבר לתמונה: יכולות נוספות ושימושים</h3>
    <p>TEM מודרניים הם יותר מסתם "מצלמות" עוצמתיות. הם כלים רב-תכליתיים המאפשרים, בנוסף להדמיה ברזולוציה אטומית, גם ניתוח כימי של הרכב החומר (למשל באמצעות ספקטרוסקופיית קרני X הנפלטות מהדוגמה) וניתוח מדויק של המבנה הגבישי (באמצעות יצירת דפוסי עקיפה). יכולות אלו הופכות את ה-TEM לכלי חיוני בקשת רחבה של תחומים, מפיזיקה ומדע חומרים ועד כימיה, ביולוגיה (במיוחד בטכניקות מתקדמות כמו קריו-EM), וגיאולוגיה. הוא מאפשר לחוקרים להבין את הקשר המהותי בין המבנה הננומטרי של חומר לתכונותיו המאקרוסקופיות, ודוחף את גבולות הידע והטכנולוגיה.</p>
</div>

<script>
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const focusControl = document.getElementById('focusControl');
const sampleDensityControl = document.getElementById('sampleDensity');
const focusValueDisplay = document.getElementById('focusValueDisplay');
const densityValueDisplay = document.getElementById('densityValueDisplay');
const electronBeam = document.getElementById('electronBeam');
const temScreenImage = document.querySelector('#temScreen .screen-image');
const beamAfterSampleContainer = document.getElementById('beamAfterSample'); // Use this for scattered beams
const toggleExplanationButton = document.getElementById('toggleExplanation');
const explanationDiv = document.getElementById('explanation');

let isBeamOn = false;
let scatteredBeamInterval;
let scatteredBeams = []; // Array to hold active scattered beam elements

// --- Helper functions for updating visual state ---

function updateBeamVisual() {
    // Simulate beam convergence/divergence using scaleX based on focus
    // focusValue = 1 is ideal focus (minimal spread at screen)
    // focusValue < 1 is under-focused (divergent beam, wide on screen)
    // focusValue > 1 is over-focused (convergent beam, then diverges, also wide)
    const focusValue = parseFloat(focusControl.value);
    // Simple non-linear mapping for visual effect
    // At focus = 1, scaleX is 0.2 (narrow at bottom). At 0.5/1.5, scaleX is 1 (wide at bottom).
    const baseScaleX = 0.2; // ScaleX at perfect focus
    const maxSpreadScaleX = 1.2; // Max ScaleX when very out of focus
    const deviation = Math.abs(focusValue - 1);
    const scaleX = baseScaleX + (maxSpreadScaleX - baseScaleX) * (deviation * 2); // Scale based on deviation from 1

    // Apply transformation: scaleX affects width from center
     // Need to adjust transform-origin if scaling from top
    // Let's keep transform-origin top center and scale
     // The beam div goes from source to screen. Scaling affects its entire length.
    // This isn't physically accurate but visually implies spread.

    // A better approach might be to control clip-path points dynamically based on Y position and focus
    // This is complex. Let's stick to simpler transform scaleX for the single beam element,
    // combined with manipulating the *screen image* for the focus effect.
    // The beam visualization itself will just look like a tapering/spreading cone.

    // Let's adjust the clip-path visually based on focus to show convergence/divergence better
     const topWidth = 15; // px - fixed at source
     const bottomWidthAtFocus = 5; // px - desired width at screen when focused
     const diagramWidth = electronBeam.parentElement.offsetWidth; // Width of .tem-diagram (400px)
     const beamCenterX = diagramWidth / 2; // Center X in pixels
     const topY = 0; // Relative to beam div start (which is 80px from top)
     const bottomY = electronBeam.offsetHeight; // Relative to beam div start (total height)

     // Map focus value to width at the bottom of the beam div
     // At focus=1, bottom width is narrow (bottomWidthAtFocus).
     // At focus=0.5 or 1.5, bottom width is wider.
     const widthDeviation = Math.abs(focusValue - 1); // 0 at focus=1, 0.5 at 0.5/1.5
     const maxBottomWidth = 100; // px - Max width at bottom when very out of focus

     const currentBottomWidth = bottomWidthAtFocus + widthDeviation * (maxBottomWidth - bottomWidthAtFocus) * 2; // Linear scale

     const topOffsetPercent = (beamCenterX - topWidth / 2) / diagramWidth * 100;
     const bottomOffsetPercent = (beamCenterX - currentBottomWidth / 2) / diagramWidth * 100;

     // Clip path points relative to the beam div (top-left 0,0, bottom-right 100%,100%)
     // Polygon points: top-left, top-right, bottom-right, bottom-left
    // Points need to be relative to the beam element's own coordinate system
    // This clip-path polygon is applied to the `electronBeam` div which starts at top: 80px.
    // Let's make the polygon define the shape from its top (0,0) to its bottom (height, width).
    // The percentage coordinates are relative to the beam div's own width/height.
    const beamDivWidth = parseFloat(getComputedStyle(electronBeam).width); // Get its actual width for calculations? No, use percentage.
    // Let's define the shape within the beam's *local* coordinates.
    // Top center: 50% 0%
    // Width at top: fixed (e.g. visual 15px centered) -> x points
    // Width at bottom: varies with focus -> x points
    // Y points: 0% (top) and 100% (bottom)

    // Need to map 15px width at 400px diagram width to percentage of beam div width (which is also 400px initially)
    // Let's simplify: the beam div is 100% width of diagram, but its content (gradient/shape) is centered and varies.
    // Let's use the CSS `width` property for the beam and animate it, centering with transform.
    // Set beam width to 15px, keep transform translateX(-50%). Animate height to grow.
    // The clip-path defines the *taper*.

    // Redefine beam shape using simple transform scaleX and skewY relative to its top origin
     // scaleX makes it wider/narrower. skewY makes sides non-parallel (taper)
    // focusValue = 1 -> minimal skew (parallel or slightly convergent)
    // focusValue < 1 -> skewed outwards (divergent cone)
    // focusValue > 1 -> skewed inwards (convergent cone)

    // Let's map focus value to a skew angle.
    const maxSkew = 5; // Degrees
    const skewAngle = (1 - focusValue) * maxSkew; // Negative skew for > 1 focusValue

     // This is still not ideal for showing lens effect.
     // Let's try another approach: The beam div represents the *central axis* and width variations.
    // Use background gradient to show the width variation.
    // The gradient needs to map Y position to transparency/color density and *also* its width.

    // Simpler visual: The main beam represents the *straight through* path.
    // It narrows at the condenser, is narrow through the sample/objective, widens at the projector.
    // Focus adjusts the final width on the screen.
    // This requires multiple visual segments or animating gradient stops/widths.

    // Let's stick to the single div, animating its opacity/intensity and shape based on sample density.
    // The *focus effect* will be *primarily* shown on the screen image itself (blur/sharpness).
    // The beam visual can maybe just show the "flow" and intensity drop after the sample.

    electronBeam.style.opacity = isBeamOn ? 1 : 0; // Fade in/out
     // Keep the initial clip-path or simplify? Let's simplify clip-path to a basic cone.
    // electronBeam.style.clipPath = 'polygon(40% 0, 60% 0, 100% 100%, 0% 100%)'; // A fixed cone shape

    // Animate opacity based on sample density: Higher density -> less straight through -> lower opacity?
    // This contradicts the diagram visual where the main beam *hits* the sample.
    // Let's make the beam visually *change* below the sample based on density.

    // Let's use the `beam-after-sample` div for the main beam segment after the sample.
    // The `electronBeam` div goes from source to sample.
    // Create a new div or element to represent the beam *after* the sample.
    // Or, reuse electronBeam but change its style drastically after the sample Y coord. This is tricky with CSS.

    // Let's modify the `electronBeam` div to represent the entire path, and its *appearance* changes.
    // Use multiple background layers or gradients?
    // Or, use the `electronBeam` for the path BEFORE sample, and a *new* element for path AFTER sample.

    // Let's try the 2-part beam approach conceptually:
    // .electron-beam (source to sample)
    // .transmitted-beam (sample to screen - this is what forms the image) - This element doesn't exist yet.
    // The scattered beams diverge from the sample.
    // The transmitted beam goes through objective/projector and hits screen. Its focus/intensity changes.

    // Add .transmitted-beam div in HTML
    // Update CSS for .transmitted-beam
    // Update JS to manage this new element.

    // Let's add the `transmitted-beam` element in the HTML.
    // For now, update the existing `electronBeam`'s appearance based on density, even if not perfectly accurate physically.
    // Higher density -> fade out electron beam more below sample?

    const sampleDensity = parseInt(sampleDensityControl.value);
    // This is a simplified model. Density causes scattering, which REMOVES electrons from the straight path.
    // So, higher density should make the *transmitted* beam (the one hitting the screen) *less intense*.
    // The `electronBeam` div visually represents the *potential* path. Its intensity *after* the sample is what matters.
    // We can fade the bottom part of the `electronBeam` gradient based on density.
    // But this requires dynamic gradient points or multiple layers.

    // Let's focus on the *effect* on the screen and scattered beams, as originally planned.
    // The main `electronBeam` visualization can remain a simple animated cone, showing the *presence* of the beam.
    // The *real* simulation happens on the screen-image and scattered beams.

    // Current clip-path is okay as a generic beam shape. Keep it.
    // Animation 'beam-pulse-flow' is okay.
    // Opacity tied to `isBeamOn`.

}

function updateScreenImage() {
    // Simulate image based on focus and sample density/contrast
    const focusValue = parseFloat(focusControl.value);
    const sampleDensity = parseInt(sampleDensityControl.value);

    // Focus simulation: Add blur when not at ideal focus (focusValue = 1)
    // Use a curve: min blur at 1, max blur at 0.5 and 1.5
    const deviation = Math.abs(focusValue - 1); // 0 at 1, 0.5 at 0.5 or 1.5
    const maxBlur = 15; // Maximum blur radius in pixels
    const blurAmount = deviation * 2 * maxBlur; // Scale deviation to max blur (e.g., 0.5 deviation -> 1 * maxBlur)

    temScreenImage.style.filter = `blur(${blurAmount}px)`;
    focusValueDisplay.textContent = focusValue === 1 ? 'ממוקד' : (focusValue < 1 ? 'פוקוס נמוך' : 'פוקוס גבוה');


    // Contrast simulation: Sample density affects overall brightness and contrast
    // Higher density -> more scattering -> less transmission -> darker image / higher contrast
    const baseBrightness = 80; // % brightness for "empty" areas (higher = brighter base)
    const maxDarkening = 60; // Max % reduction in brightness for dense areas
    const scatterDarkening = (sampleDensity / 10) * maxDarkening; // Scale density (0-10) to darkening amount (0-maxDarkening)

    const denseBrightness = Math.max(10, baseBrightness - scatterDarkening); // % brightness for "dense" areas, capped at 10%

    // Update the gradient background to show contrast change
    const gradient = `linear-gradient(to right,
                      hsl(0, 0%, ${baseBrightness}%) 0%,
                      hsl(0, 0%, ${baseBrightness}%) 45%,
                      hsl(0, 0%, ${denseBrightness}%) 55%,
                      hsl(0, 0%, ${denseBrightness}%) 100%)`;
    temScreenImage.style.backgroundImage = gradient;
     // Also adjust overall brightness/contrast slightly via filter based on density?
    const contrastBoost = sampleDensity * 2; // Simple linear boost
    temScreenImage.style.filter += ` brightness(${baseBrightness / 100}) contrast(${1 + contrastBoost / 100})`;
     // Re-apply blur after other filters
     temScreenImage.style.filter = `blur(${blurAmount}px) brightness(${baseBrightness / 100}) contrast(${1 + contrastBoost / 100})`;


    // Update density value display
    let densityText = 'נמוכה מאוד';
    if (sampleDensity > 0) densityText = 'נמוכה';
    if (sampleDensity > 3) densityText = 'בינונית';
    if (sampleDensity > 6) densityText = 'גבוהה';
    if (sampleDensity > 9) densityText = 'גבוהה מאוד';
     densityValueDisplay.textContent = densityText;
}

function createScatteredBeams() {
    // Clear previous scattered beams
    beamAfterSampleContainer.innerHTML = '';
    scatteredBeams = [];

    const sampleDensity = parseInt(sampleDensityControl.value);
    const numberOfScatteredBeams = sampleDensity * 4; // More beams for higher density
    const maxScatterAngle = 60; // Max angle from vertical

    for (let i = 0; i < numberOfScatteredBeams; i++) {
        // Random angle, weighted towards smaller angles (more realistic)
        const angle = (Math.random() * 2 - 1) * maxScatterAngle * (Math.random() * 0.5 + 0.5); // Random angle -max to +max, bias towards center
        const length = Math.random() * 250 + 50; // Random length up to bottom of diagram
        const delay = Math.random() * 0.5; // Random animation delay

        const beamDiv = document.createElement('div');
        beamDiv.classList.add('scattered-beam-line');
        beamDiv.style.setProperty('--angle', `${angle}deg`);
        beamDiv.style.setProperty('--length', `${length}px`);
        beamDiv.style.animationDelay = `${delay}s`; // Stagger animations
        beamDiv.style.opacity = 0.8 - (sampleDensity / 10) * 0.5 + Math.random() * 0.2; // Opacity hint based on density


        // Add the element to the container below the sample
        beamAfterSampleContainer.appendChild(beamDiv);
         scatteredBeams.push(beamDiv);
    }
}

function startBeam() {
    if (isBeamOn) return;
    isBeamOn = true;
    electronBeam.style.display = 'block';
    electronBeam.style.opacity = 1; // Ensure visible
    temScreenImage.style.display = 'block';
    startButton.disabled = true;
    stopButton.disabled = false;
     document.querySelector('.electron-source').classList.add('pulse'); // Start source pulse

    updateBeamVisual();
    updateScreenImage();

    // Start generating scattered beams
    createScatteredBeams(); // Create initial batch
    scatteredBeamInterval = setInterval(createScatteredBeams, 1000); // Regenerate scattered beams periodically
}

function stopBeam() {
    if (!isBeamOn) return;
    isBeamOn = false;
     electronBeam.style.opacity = 0; // Fade out electron beam
    // electronBeam.style.display = 'none'; // Hide after fade
    temScreenImage.style.display = 'none'; // Hide screen image immediately
    startButton.disabled = false;
    stopButton.disabled = true;
    document.querySelector('.electron-source').classList.remove('pulse'); // Stop source pulse


    clearInterval(scatteredBeamInterval);
     // Animate scattered beams fading out (optional, CSS animation already fades out)
     // Or simply clear them
    beamAfterSampleContainer.innerHTML = ''; // Clear scattered beams
    scatteredBeams = [];

     // Reset screen image appearance slightly? Or just hide
}

// --- Event Listeners ---
startButton.addEventListener('click', startBeam);
stopButton.addEventListener('click', stopBeam);

focusControl.addEventListener('input', () => {
    updateBeamVisual(); // Update beam shape visual (if implemented dynamically)
    updateScreenImage(); // Update screen image based on new focus
});

sampleDensityControl.addEventListener('input', () => {
    updateScreenImage(); // Update screen image based on new density (contrast)
    if (isBeamOn) {
         // Regenerate scattered beams visualization with new density
         createScatteredBeams(); // Recreate with new density
    }
});

toggleExplanationButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
});

// --- Initial state setup ---
updateScreenImage(); // Set initial screen appearance (blur/contrast)
updateBeamVisual(); // Set initial beam visual state (hidden)
// Add a subtle initial state effect or message?
// temScreenImage.style.backgroundColor = '#333'; // Dark background
// temScreenImage.textContent = 'לחץ "הפעל אלומה"'; // Placeholder text

// Ensure beam fades out smoothly on stop
electronBeam.addEventListener('transitionend', () => {
    if (!isBeamOn) {
        electronBeam.style.display = 'none';
    }
});

</script>
```