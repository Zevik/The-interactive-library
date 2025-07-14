---
title: "הגרדיומטר: העיניים שרואות את הכבידה המשתנה מתחת לפני השטח"
english_slug: gradiometer-detecting-changing-gravity
category: "מדעים מדויקים / פיזיקה"
tags: [כבידה, גרדיומטר, גאופיזיקה, מדידה, מדעי כדור הארץ, אינטראקטיבי]
---
# הגרדיומטר: העיניים שרואות את הכבידה המשתנה מתחת לפני השטח

איך מוצאים אוצרות נסתרים מתחת לאדמה, כמו נפט, מינרלים יקרים או אפילו עתיקות קבורות, בלי לחפור באדמה? זה נשמע כמו קסם, אבל התשובה טמונה בכוח טבעי שכולנו מרגישים – הכבידה! מסתבר ששינויים זעירים אך משמעותיים בכוח הכבידה המקומי יכולים לרמוז לנו בדיוק מה מסתתר שם למטה. בואו נצא למסע מרתק ונגלה איך כלי מדידה מדהים, הגרדיומטר, מנצל את השינויים הזעירים הללו כדי לחשוף את סודות כדור הארץ עמוק בפנים.

<div id="gradiometer-app">
    <div class="controls">
        <h3>כווננו את האנומליה התת-קרקעית:</h3>
        <div class="control-group">
            <label for="anomaly-depth">עומק:</label>
            <input type="range" id="anomaly-depth" min="30" max="150" value="80">
            <span id="anomaly-depth-value">80</span> יחידות עומק
        </div>
        <div class="control-group">
            <label for="anomaly-density">סוג חומר (צפיפות):</label>
            <select id="anomaly-density">
                <option value="-1">חלל ריק (צפיפות נמוכה)</option>
                <option value="1" selected>גוש סלע צפוף (צפיפות גבוהה)</option>
            </select>
        </div>
    </div>
    <div class="simulation-area">
        <div class="sky"></div>
        <div class="ground-surface"></div>
        <div class="subsurface">
            <div id="anomaly"></div>
        </div>
        <div id="gradiometer">
            <div class="mass mass-top"></div>
            <div class="mass mass-bottom"></div>
            <div class="gradiometer-line"></div>
            <div class="gradiometer-housing"></div>
            <div class="gradiometer-label">גרדיומטר</div>
        </div>
        <!-- Gravity vectors will be added dynamically or positioned -->
         <div id="vector-top" class="gravity-vector"></div>
         <div id="vector-bottom" class="gravity-vector"></div>
    </div>
    <div class="graph-area">
        <canvas id="gradiometer-graph"></canvas>
        <div class="graph-labels">
            <div class="x-label">מיקום גרדיומטר אופקי לאורך המסלול</div>
            <div class="y-label">גרדיאנט כבידה אנכי (הפרש משיכה)</div>
        </div>
    </div>
</div>

<button id="toggle-explanation">הצגת ההסבר המלא: איך זה עובד?</button>

<div id="explanation" class="hidden">
    <h2>הסבר מורחב: לגלות את הכוח הנסתר</h2>

    <h3>כוח הכבידה: המשיכה הבלתי נראית שמחזיקה אותנו (ואת היקום) יחד</h3>
    כוח הכבידה הוא אחד הכוחות הבסיסיים והמופלאים ביותר בטבע. זהו כוח משיכה שפועל בין כל שתי מסות ביקום – מהתפוח שנופל מהעץ ועד לכוכבי לכת שמקיפים את השמש. ככל שהמסות גדולות יותר והמרחק ביניהן קטן יותר, כך כוח המשיכה חזק יותר. כדור הארץ, בזכות מסתו העצומה, מפעיל כוח כבידה משמעותי שמושך אליו כל מה שבסביבתו, ובזכותו אנחנו "דבוקים" לקרקע ולא עפים לחלל. הכבידה היא שגורמת לדברים ליפול, לירח להקיף את כדור הארץ, ולגלקסיות להישאר מחוברות.

    <h3>הפתעה: הכבידה משתנה! הכירו את אנומליות הכבידה</h3>
    רוב הזמן אנחנו חושבים על כוח הכבידה של כדור הארץ כקבוע – אותו 9.8 מטר לשנייה בריבוע המפורסם. אבל במציאות, הוא משתנה מעט מנקודה לנקודה על פני השטח ומתחתיו. למה זה קורה?
    *   **אתם לא שטוחים:** כדור הארץ אינו כדור מושלם, ויש הבדלים בגובה פני השטח. ככל שעולים גבוה יותר (למשל, על הר), מתרחקים ממרכז כדור הארץ, וכוח הכבידה נחלש מעט.
    *   **מבנה פנימי מגוון:** מתחת לרגלינו, כדור הארץ אינו אחיד. ישנם אזורים עם סלעים צפופים יותר (כמו עפרות ברזל), חללים ריקים (מערות), כיסי מים, או מרבצים של חומרים שונים. כל אזור כזה בעל צפיפות שונה מהסביבה שלו מפעיל כוח כבידה מעט שונה – "משיכה עודפת" אם צפוף יותר, או "משיכה חסרה" אם פחות צפוף. שינויים מקומיים אלה בכוח הכבידה נקראים **אנומליות כבידה**. הסימולציה שלפניכם מדגימה בדיוק איך מאתרים אנומליה כזו!
    *   **סיבוב כדור הארץ:** הסיבוב שלנו יוצר כוח צנטריפוגלי קטן שמתנגד לכבידה, והשפעתו משתנה קצת מנקודה לנקודה.

    <h3>גרדיאנט כבידה: לא הכבידה עצמה, אלא קצב השינוי שלה!</h3>
    כשמדברים על "גרדיאנט" במדע, מתכוונים לרוב לקצב השינוי של משהו במרחב. גרדיאנט כבידה, או מפל כבידה, הוא בדיוק זה – הוא מתאר **כמה מהר כוח הכבידה משתנה** מנקודה אחת לנקודה אחרת קרובה מאוד. במקום למדוד את הכוח הכולל בנקודה בודדת, מודדים את **ההפרש** בכוח הכבידה בין שתי נקודות קרובות, ומחלקים במרחק ביניהן. חשבו על זה כמו על שיפוע: לא גובה ההר, אלא כמה תלול הוא באותה נקודה. בסימולציה, אנו מודדים את ההפרש בכוח הכבידה האנכי (למעלה-למטה) שפועל על שתי "מסות ניסיון" הממוקמות בגרדיומטר במרחק קבוע זו מזו. אם כוח הכבידה זהה בשתי הנקודות, ההפרש יהיה אפס. אם הוא שונה, הגרדיומטר "ירגיש" את ההפרש הזה.

    <h3>הגרדיומטר בפעולה: איך מודדים את השינוי הזעיר הזה?</h3>
    גרדיומטר הוא מכשיר מתוחכם ועדין שמטרתו למדוד במדויק את גרדיאנט הכבידה. העיקרון הבסיסי, כפי שמוצג בסימולציה, פשוט יחסית: הוא מודד את הפרש הכוח הפועל על שתי מסות קטנות הממוקמות במרחק מדויק זו מזו (אחת מעל השנייה, במקרה שלנו). אם כוח הכבידה בשתי הנקודות שווה, אין הפרש והגרדיאנט אפס. אם כוח הכבידה משתנה מעט לאורך המרחק הקטן בין המסות (למשל, כי מסה אחת קרובה יותר לאנומליה תת-קרקעית), המכשיר יזהה את ההפרש הזה וימדוד גרדיאנט לא-אפסי.

    <h3>למה למדוד שינוי עדיף על מדידת הכול? כוחו של הגרדיאנט באיתור מקומי</h3>
    מכשירי מדידת כבידה פשוטים יותר (גרבימטרים) מודדים את כוח הכבידה הכולל בנקודה אחת. המדידה הזו מושפעת המון מכוח הכבידה העצום של כדור הארץ כולו, מהירח, מהשמש, ואפילו מגאות ושפל. כל "רעש" הכבידה הזה מקשה על זיהוי אנומליות מקומיות וקטנות שנוצרות ממבנים קבורים קרוב לפני השטח.
    גרדיומטרים, לעומת זאת, **רגישים בעיקר למקורות כבידה קרובים**. כוח הכבידה של עצמים רחוקים (כדור הארץ הגדול, הירח) משתנה לאט מאוד במרחב. לכן, על המרחק הקטן שבין שתי המסות בגרדיומטר, ההפרש בכוח הכבידה מהם יהיה זניח. לעומת זאת, אנומליה קטנה וקרובה (כמו זו שבסימולציה) תשפיע בצורה משמעותית יותר על המסה הקרובה אליה מאשר על המסה הרחוקה יותר, ותיצור הפרש כוח גדול ומדיד – סימן ברור לנוכחותה! לכן, גרדיומטרים מעולים ב"סינון" הרעש מרחוק ומאפשרים איתור מדויק של דברים שנסתרים ממש מתחת לרגלינו.

    <h3>מגילוי נפט ועד ניווט בצוללות: איפה פוגשים גרדיומטרים בחיים?</h3>
    גרדיומטרים הם כלים מדעיים והנדסיים יקרים ומורכבים, אך הם חיוניים במגוון עצום של יישומים:
    *   **חיפושי אוצרות תת-קרקעיים:** גאולוגים משתמשים בהם לאיתור מבנים תת-קרקעיים בעלי צפיפות שונה – מרבצי נפט וגז טבעי (לעתים קשורים למבני "כיפות מלח" צפופות), עורקי מינרלים יקרים, או אזורים בעלי פעילות וולקנית.
    *   **ארכיאולוגיה:** גרדיומטרים יכולים לגלות מבנים קבורים, קירות, או אפילו קברים, על ידי זיהוי שינויי הצפיפות בין האדמה שמילאה אותם לבין האדמה שמסביב.
    *   **ניווט מדויק:** בצוללות, למשל, שבהן GPS לא עובד, גרדיומטרים יכולים לשמש לניווט. על ידי מדידת גרדיאנט הכבידה המקומי והשוואתו למפות גרדיאנט מוכנות מראש של קרקעית הים, הצוללת יכולה לקבוע את מיקומה המדויק.
    *   **פיזיקה יסודית:** גרדיומטרים מדויקים במיוחד משמשים בניסויי קצה לבדיקת חוקי הכבידה היסודיים וחיפוש אחר כוחות פיזיקליים חדשים.

    בסימולציה, שימו לב כיצד כאשר אתם "סורקים" עם הגרדיומטר מעל האנומליה (או בסמוך אליה), הגרדיאנט הכבידה המחושב משתנה באופן דרמטי. השיא או השפל שמופיע בגרף מסמן בבירור את מיקום האנומליה ומעיד על סוגה (צפופה יותר או פחות מהסביבה). נסו לשנות את עומק וצפיפות האנומליה וראו איך הגרף משתנה – כך לומדים על המבנה התת-קרקעי בלי לחפור!
</div>

<style>
/* Basic Reset and Font */
#gradiometer-app {
    font-family: 'Arial', sans-serif;
    direction: rtl;
    text-align: right;
    margin: 20px auto;
    padding: 25px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    max-width: 850px; /* Slightly wider */
    background-color: #ffffff; /* Clean white background */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

/* Controls Styling */
.controls {
    margin-bottom: 30px;
    padding: 20px;
    background-color: #f4f7f6; /* Light grey-blue */
    border-radius: 8px;
    display: flex; /* Arrange controls side-by-side on wider screens */
    flex-wrap: wrap; /* Wrap controls on smaller screens */
    gap: 20px; /* Space between control groups */
    align-items: center;
}

.controls h3 {
    width: 100%; /* Full width for the heading */
    text-align: center;
    margin-top: 0;
    margin-bottom: 20px;
    color: #333;
}

.control-group {
    display: flex;
    align-items: center;
    flex-grow: 1; /* Allow groups to grow */
    min-width: 250px; /* Minimum width before wrapping */
}

.control-group label {
    margin-left: 12px; /* Space after label */
    font-weight: bold;
    color: #555;
    white-space: nowrap; /* Prevent label wrapping */
}

.controls input[type="range"],
.controls select {
    flex-grow: 1; /* Allow controls to take available space */
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #fff;
    font-size: 1rem;
    cursor: pointer;
    -webkit-appearance: none; /* Remove default styling for range */
    appearance: none;
    height: 8px; /* Height of the range slider track */
    outline: none;
}

/* Custom Range Slider Thumb */
.controls input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 18px; /* Increased size */
  height: 18px; /* Increased size */
  background: #007bff; /* Blue thumb */
  border: 2px solid #fff;
  border-radius: 50%;
  cursor: pointer;
  margin-top: -5px; /* Adjust to center vertically */
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  transition: background-color 0.3s ease;
}
.controls input[type="range"]::-webkit-slider-thumb:hover {
  background: #0056b3;
}
.controls input[type="range"]::-moz-range-thumb {
  width: 18px;
  height: 18px;
  background: #007bff;
  border: 2px solid #fff;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  transition: background-color 0.3s ease;
}
.controls input[type="range"]::-moz-range-thumb:hover {
   background: #0056b3;
}
.controls input[type="range"]::-webkit-slider-runnable-track {
  width: 100%;
  height: 8px;
  cursor: pointer;
  background: #d3e0ea;
  border-radius: 4px;
}
.controls input[type="range"]::-moz-range-track {
  width: 100%;
  height: 8px;
  cursor: pointer;
  background: #d3e0ea;
  border-radius: 4px;
}


.control-group span {
    margin-right: 5px; /* Space before value */
    min-width: 30px; /* Ensure space for numbers */
    text-align: left;
}


/* Simulation Area */
.simulation-area {
    position: relative;
    width: 100%;
    height: 350px; /* Increased height */
    border: 1px solid #bbb;
    margin-bottom: 20px;
    background: linear-gradient(to bottom, #a8d0e6 0%, #a8d0e6 100px, #e0f0ff 100px, #e0f0ff 100%); /* Sky and subsurface */
    overflow: hidden;
    border-radius: 8px;
}

.sky {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100px; /* Matches the sky part of the gradient */
    /* Background handled by simulation-area gradient */
    z-index: 0; /* Ensure sky is behind ground etc. */
}

.ground-surface {
    position: absolute;
    top: 100px; /* Position below the sky */
    left: 0;
    width: 100%;
    height: 10px; /* Thicker ground line */
    background-color: #8B4513; /* Earth brown */
    z-index: 2; /* Above sky, below gradiometer */
}

.subsurface {
    position: absolute;
    top: 110px; /* Immediately below the ground */
    left: 0;
    width: 100%;
    height: calc(350px - 110px); /* Rest of the height */
    /* Background handled by simulation-area gradient */
    z-index: 0; /* Behind everything */
}

#anomaly {
    position: absolute;
    width: 50px; /* Slightly larger */
    height: 50px;
    background-color: #607D8B; /* Default color for dense rock */
    border-radius: 50%;
    left: 50%; /* Initial X */
    top: 80px; /* Initial Y (relative to ground, set by JS) */
    transform: translate(-50%, -50%); /* Center the circle on its position */
    border: 2px solid #455A64;
    transition: top 0.5s ease-out, background-color 0.3s ease, border-color 0.3s ease; /* Smooth transition for depth/type change */
}

#anomaly[data-density="-1"] {
    background-color: #B0BEC5; /* Color for void */
    border: 2px dashed #78909C;
    box-shadow: none; /* No shadow for void */
}

#anomaly[data-density="1"] {
     box-shadow: 0 0 15px rgba(96, 125, 139, 0.6); /* Subtle glow for dense object */
}


#gradiometer {
    position: absolute;
    top: 75px; /* Slightly higher above ground */
    width: 40px; /* Wider */
    height: 45px; /* Taller */
    cursor: grab;
    z-index: 10; /* Ensure it's on top */
    left: 50%; /* Initial X */
    transform: translateX(-50%);
    transition: left 0.05s linear; /* Smooth movement */
    /* Add a subtle floating/pulsing animation */
    animation: floatGradiometer 3s ease-in-out infinite;
}

@keyframes floatGradiometer {
    0% { transform: translateX(-50%) translateY(0px); }
    50% { transform: translateX(-50%) translateY(-5px); }
    100% { transform: translateX(-50%) translateY(0px); }
}

#gradiometer:active {
    cursor: grabbing;
     animation: none; /* Stop float animation while dragging */
}


.mass {
    position: absolute;
    width: 10px; /* Slightly larger mass indicators */
    height: 10px;
    background-color: #333;
    border-radius: 50%;
    left: 50%;
    transform: translateX(-50%);
    z-index: 11; /* Above gradiometer housing */
    /* Add subtle animation/movement based on force */
     transition: top 0.1s ease-out; /* Smooth vertical movement */
     box-shadow: 0 0 5px rgba(0,0,0,0.3);
}

.mass-top {
    top: 5px; /* Position relative to gradiometer div */
}

.mass-bottom {
    top: 30px; /* Position relative to gradiometer div (45 - 10 - 5 = 30, roughly) */
}

.gradiometer-line {
     position: absolute;
     width: 3px; /* Thicker line */
     background-color: #555;
     top: 15px; /* Below top mass */
     bottom: 15px; /* Above bottom mass */
     left: 50%;
     transform: translateX(-50%);
     z-index: 10;
}

.gradiometer-housing {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: #fff; /* White casing */
    border: 2px solid #555;
    border-radius: 6px;
    z-index: 9; /* Behind masses and line */
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.gradiometer-label {
    position: absolute;
    top: 50px; /* Below the gradiometer icon */
    left: 50%;
    transform: translateX(-50%);
    font-size: 11px; /* Slightly larger font */
    white-space: nowrap;
    color: #333;
    font-weight: bold;
}


/* Gravity Vectors - Representing Anomaly's Pull */
.gravity-vector {
    position: absolute;
    width: 3px; /* Thicker vector line */
    background-color: red; /* Default: pulling down */
    transform-origin: top center; /* Scale from the top */
    z-index: 5; /* Behind gradiometer, above ground */
    transition: height 0.1s ease-out, background-color 0.1s ease; /* Smooth length and color change */
    opacity: 0.8;
}

.gravity-vector::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
    border-left: 6px solid transparent; /* Base of arrowhead */
    border-right: 6px solid transparent; /* Base of arrowhead */
    border-top: 8px solid red; /* Pointing down */
    z-index: 1;
}

/* Style for negative force (void pushing up) */
.gravity-vector[data-direction="-1"] {
     background-color: blue; /* Pushing up */
     transform-origin: bottom center; /* Scale from the bottom */
}

.gravity-vector[data-direction="-1"]::after {
     border-top: none;
     border-bottom: 8px solid blue; /* Pointing up */
     bottom: initial; /* Reset bottom */
     top: 0; /* Position at the top of the vector line */
}


/* Graph Area */
.graph-area {
    position: relative;
    width: 100%;
    height: 220px; /* Slightly taller graph */
    margin-top: 30px;
    border: 1px solid #bbb;
    background-color: #f8f8f8; /* Light grey background */
    border-radius: 8px;
    overflow: hidden;
}

#gradiometer-graph {
    width: 100%;
    height: 100%;
}

.graph-labels {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1; /* Ensure labels are above canvas but below potential interactive elements */
}

.x-label {
    position: absolute;
    bottom: 8px; /* Lower position */
    left: 50%;
    transform: translateX(-50%);
    font-size: 11px;
    color: #555;
}

.y-label {
    position: absolute;
    top: 50%;
    right: 8px; /* Further from edge */
    transform: translateY(-50%) rotate(90deg);
    font-size: 11px;
    color: #555;
    transform-origin: 0 0;
    white-space: nowrap;
}

/* Explanation Toggle Button */
#toggle-explanation {
    display: block;
    margin: 30px auto; /* More space */
    padding: 12px 20px; /* Larger padding */
    font-size: 1rem; /* Standard font size */
    cursor: pointer;
    background-color: #007bff; /* Blue button */
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#toggle-explanation:hover {
    background-color: #0056b3;
}

#toggle-explanation:active {
    transform: scale(0.98); /* Slight press effect */
}


/* Explanation Section */
#explanation {
    margin-top: 30px; /* More space */
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9; /* Lighter background */
    line-height: 1.7; /* Improved readability */
    color: #333;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.hidden {
    display: none;
}

#explanation h2, #explanation h3 {
    text-align: center;
    margin-bottom: 18px;
    color: #0056b3; /* Match button color */
}

#explanation h3 {
    margin-top: 25px;
    color: #007bff;
    font-size: 1.15rem;
}

#explanation p {
    margin-bottom: 15px; /* More space between paragraphs */
    text-align: justify; /* Justify text for cleaner look */
}

#explanation strong {
    color: #555; /* Slightly darker for emphasis */
}

/* Add a subtle grid to the canvas */
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const gradiometer = document.getElementById('gradiometer');
    const anomaly = document.getElementById('anomaly');
    const groundSurface = document.querySelector('.ground-surface');
    const simulationArea = document.querySelector('.simulation-area');
    const massTop = gradiometer.querySelector('.mass-top');
    const massBottom = gradiometer.querySelector('.mass-bottom');
    const vectorTop = document.getElementById('vector-top');
    const vectorBottom = document.getElementById('vector-bottom');
    const canvas = document.getElementById('gradiometer-graph');
    const ctx = canvas.getContext('2d');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const anomalyDepthSlider = document.getElementById('anomaly-depth');
    const anomalyDepthValueSpan = document.getElementById('anomaly-depth-value');
    const anomalyDensitySelect = document.getElementById('anomaly-density');

    let isDragging = false;
    let startX;
    let initialLeft;
    const simulationWidth = simulationArea.offsetWidth;
    const groundY = groundSurface.offsetTop + groundSurface.offsetHeight / 2; // Y position of the ground line
    const gradiometerHeight = gradiometer.offsetHeight;
    // Actual vertical distance between the centers of the mass elements
    const gradiometerMassDistance = massBottom.offsetTop + massBottom.offsetHeight / 2 - (massTop.offsetTop + massTop.offsetHeight / 2);


    // Simulation constants (simplified and scaled for visualization)
    const G = 1; // Gravitational constant
    const anomalyBaseMass = 500000; // Base 'mass' effect of the anomaly
    const anomalyRadius = anomaly.offsetWidth / 2;

    let graphData = [];
    // Store graph data as { simulationX: value } to handle window resize mapping
    let rawGraphData = [];


    // --- Anomaly Control Handlers ---
    const updateAnomalyPosition = () => {
         const depth = parseInt(anomalyDepthSlider.value, 10);
        // Anomaly Y position is depth *below* the ground line
        // Anomaly div top will be groundY + depth - anomalyRadius (to center the circle)
         anomaly.style.top = `${groundY + depth - anomalyRadius}px`;
         anomalyDepthValueSpan.textContent = depth;
         // Trigger update if not dragging (static state change)
         if (!isDragging) {
             // For static state, clear graph and draw only the current point
             rawGraphData = []; // Clear previous static data
             updateSimulation(); // Calculate and draw for current position
         }
    };

     const updateAnomalyDensity = () => {
        const densityFactor = parseInt(anomalyDensitySelect.value, 10);
        anomaly.dataset.density = densityFactor;
        // Update anomaly visual style based on density
        if (densityFactor === -1) {
             anomaly.style.backgroundColor = '#B0BEC5';
             anomaly.style.borderColor = '#78909C';
             anomaly.style.boxShadow = 'none';
        } else { // densityFactor === 1
             anomaly.style.backgroundColor = '#607D8B';
             anomaly.style.borderColor = '#455A64';
             anomaly.style.boxShadow = '0 0 15px rgba(96, 125, 139, 0.6)';
        }
         // Trigger update if not dragging (static state change)
         if (!isDragging) {
            rawGraphData = []; // Clear previous static data
            updateSimulation(); // Calculate and draw for current position
         }
     };


    anomalyDepthSlider.addEventListener('input', updateAnomalyPosition);
    anomalyDensitySelect.addEventListener('change', updateAnomalyDensity);


    // --- Gradiometer Drag Functionality ---
    gradiometer.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.clientX;
        initialLeft = gradiometer.offsetLeft;
        gradiometer.style.cursor = 'grabbing';
        gradiometer.style.animation = 'none'; // Pause floating animation while dragging
        rawGraphData = []; // Clear graph on new drag start
        updateSimulation(); // Update simulation state for the starting point
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const dx = e.clientX - startX;
        let newLeft = initialLeft + dx;

        // Clamp the gradiometer position within the simulation area bounds
        newLeft = Math.max(0, Math.min(newLeft, simulationWidth - gradiometer.offsetWidth));

        gradiometer.style.left = `${newLeft}px`;

        updateSimulation(); // Update simulation state dynamically
    });

    document.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;
            gradiometer.style.cursor = 'grab';
             gradiometer.style.animation = 'floatGradiometer 3s ease-in-out infinite'; // Resume animation
             // Final update might be needed if simulation state depends on mouseup (not here)
             // updateSimulation();
        }
    });

    // Prevent default drag behavior that conflicts with our custom drag
    gradiometer.ondragstart = () => false;

    // --- Physics Calculation and Visualization Update ---

    function getAnomalyPosition() {
        // Position is relative to the simulationArea top-left
        const anomalyLeft = anomaly.offsetLeft + anomalyRadius; // Center X
        const anomalyTop = anomaly.offsetTop + anomalyRadius; // Center Y
        return { x: anomalyLeft, y: anomalyTop };
    }

    function getGradiometerMassPositions() {
        const gradiometerLeft = gradiometer.offsetLeft + gradiometer.offsetWidth / 2; // Center X of gradiometer
        const gradiometerTop = gradiometer.offsetTop; // Top Y of gradiometer div

        // Mass positions relative to simulationArea top-left
        const massTopY = gradiometerTop + massTop.offsetTop + massTop.offsetHeight / 2;
        const massBottomY = gradiometerTop + massBottom.offsetTop + massBottom.offsetHeight / 2;

        return {
            top: { x: gradiometerLeft, y: massTopY },
            bottom: { x: gradiometerLeft, y: massBottomY }
        };
    }

     function calculateGravityForce(massPos, anomalyPos, anomalyDensityFactor) {
        const dx = anomalyPos.x - massPos.x;
        const dy = anomalyPos.y - massPos.y;
        const distanceSq = dx * dx + dy * dy;

        // Prevent division by zero if mass is exactly at anomaly center
        if (distanceSq < 1) return { fx: 0, fy: 0 }; // Use a small threshold

        const distance = Math.sqrt(distanceSq);
        // Gravitational force magnitude from the anomaly
        const forceMagnitude = (G * anomalyBaseMass * anomalyDensityFactor) / distanceSq;

        // Return the vertical component of the force (Fy)
        // Fy = Force * (dy / distance)
        const fy = forceMagnitude * (dy / distance); // dy is (anomaly.y - mass.y) - positive means anomaly is below mass

        return { fx: forceMagnitude * (dx / distance), fy: fy }; // Also return fx if needed later
    }


    function updateVectorsAndMasses() {
        const anomalyPos = getAnomalyPosition();
        const massPositions = getGradiometerMassPositions();
        const anomalyDensityFactor = parseInt(anomalyDensitySelect.value, 10);

        // Calculate forces from anomaly on each mass
        const forceTop = calculateGravityForce(massPositions.top, anomalyPos, anomalyDensityFactor);
        const forceBottom = calculateGravityForce(massPositions.bottom, anomalyPos, anomalyDensityFactor);

        // --- Update Gravity Vectors (Visualization of Anomaly's Pull) ---
        const vectorScale = 0.0001; // Adjust to make vectors a reasonable visual size
        const vectorMaxWidth = 80; // Max visual height for vectors

        // Top Mass Vector
        const vectorLengthTop = Math.min(Math.abs(forceTop.fy) * vectorScale, vectorMaxWidth);
        vectorTop.style.left = `${massPositions.top.x}px`;
        // Vector starts *at* the mass position and extends based on direction
        vectorTop.style.top = forceTop.fy >= 0 ? `${massPositions.top.y}px` : `${massPositions.top.y - vectorLengthTop}px`; // Adjust start Y for upward vectors
        vectorTop.style.height = `${vectorLengthTop}px`;
        vectorTop.style.backgroundColor = forceTop.fy >= 0 ? 'red' : 'blue'; // Red for pull down, Blue for pull up (void)
        vectorTop.dataset.direction = forceTop.fy >= 0 ? '1' : '-1'; // Use data attribute for CSS arrow direction

        // Bottom Mass Vector
        const vectorLengthBottom = Math.min(Math.abs(forceBottom.fy) * vectorScale, vectorMaxWidth);
        vectorBottom.style.left = `${massPositions.bottom.x}px`;
         // Vector starts *at* the mass position and extends based on direction
        vectorBottom.style.top = forceBottom.fy >= 0 ? `${massPositions.bottom.y}px` : `${massPositions.bottom.y - vectorLengthBottom}px`; // Adjust start Y for upward vectors
        vectorBottom.style.height = `${vectorLengthBottom}px`;
        vectorBottom.style.backgroundColor = forceBottom.fy >= 0 ? 'red' : 'blue';
        vectorBottom.dataset.direction = forceBottom.fy >= 0 ? '1' : '-1';

        // --- Animate Masses within Gradiometer (Visualization of Differential Force) ---
        // The masses move slightly *relative* to the gradiometer housing based on the force difference.
        // A simplified approach: move massTop up slightly if Fy_top is larger than Fy_bottom (net upward pull on top relative to bottom), and vice-versa.
        // Scale factor for mass movement visualization
        const massMoveScale = 0.00001; // Adjust this value

        // Calculate the *relative* force pushing/pulling the masses apart or together
        // If Fy_bottom > Fy_top (both positive), bottom is pulled more strongly down, masses might move slightly apart.
        // If Fy_bottom < Fy_top (both positive), top is pulled more strongly down (unlikely if anomaly is below), masses might move slightly together.
        // If density is negative, forces are negative (upward pull).
        // Let's visualize the *difference* in Fy, showing it as a relative displacement.
        // A positive gradient value (Fy_bottom - Fy_top) indicates stronger pull on the bottom mass relative to the top.
        // This might cause the bottom mass to move slightly down relative to the top mass.
        const gradientValue = forceBottom.fy - forceTop.fy;

        // Apply a small vertical displacement to the masses based on the gradient value.
        // Positive gradient: bottom mass moves down, top mass moves up (masses spread apart).
        // Negative gradient: bottom mass moves up, top mass moves down (masses come together).
        const massDisplacement = gradientValue * massMoveScale;

        // Original relative positions within the gradiometer div
        const originalMassTopY = 5; // As set in CSS
        const originalMassBottomY = 30; // As set in CSS

        // Apply displacement (exaggerated for visual effect)
        // Top mass moves up for positive gradient, down for negative.
        // Bottom mass moves down for positive gradient, up for negative.
        // Let's apply half the displacement to each mass relative to their original positions.
        const displacementMagnitude = Math.abs(massDisplacement) * 0.5; // Split the total movement

        if (gradientValue > 0) { // Bottom feels stronger pull (masses spread)
            massTop.style.top = `${originalMassTopY - displacementMagnitude}px`;
            massBottom.style.top = `${originalMassBottomY + displacementMagnitude}px`;
        } else if (gradientValue < 0) { // Top feels stronger pull (masses come together)
            massTop.style.top = `${originalMassTopY + displacementMagnitude}px`;
            massBottom.style.top = `${originalMassBottomY - displacementMagnitude}px`;
        } else { // Gradient is zero, return to original positions
             massTop.style.top = `${originalMassTopY}px`;
             massBottom.style.top = `${originalMassBottomY}px`;
        }
         // Clamp displacement slightly to prevent masses from crossing or going too far
         const maxDisplacement = 8; // Arbitrary visual limit
         const clampedDispMag = Math.min(Math.abs(massDisplacement) * 0.5, maxDisplacement/2);
         if (gradientValue > 0) { // Bottom feels stronger pull (masses spread)
             massTop.style.top = `${originalMassTopY - clampedDispMag}px`;
             massBottom.style.top = `${originalMassBottomY + clampedDispMag}px`;
         } else if (gradientValue < 0) { // Top feels stronger pull (masses come together)
             massTop.style.top = `${originalMassTopY + clampedDispMag}px`;
             massBottom.style.top = `${originalMassBottomY - clampedDispMag}px`;
         } else {
             massTop.style.top = `${originalMassTopY}px`;
             massBottom.style.top = `${originalMassBottomY}px`;
         }
    }


    function calculateGravityGradient() {
        const anomalyPos = getAnomalyPosition();
        const massPositions = getGradiometerMassPositions();
        const anomalyDensityFactor = parseInt(anomalyDensitySelect.value, 10);

        // Calculate vertical force (Fy) from anomaly on each mass
        const forceTopFy = calculateGravityForce(massPositions.top, anomalyPos, anomalyDensityFactor).fy;
        const forceBottomFy = calculateGravityForce(massPositions.bottom, anomalyPos, anomalyDensityFactor).fy;

        // The vertical gravity gradient component is the difference in vertical force (Fy)
        // measured by the two masses, divided by the vertical distance between them.
        // Gradient = (Fy_bottom - Fy_top) / Δz
        // For plotting, we can just plot the difference (Fy_bottom - Fy_top),
        // as Δz is constant and it gives the correct shape of the anomaly signature.
        // Let's return the difference directly. A positive value means the bottom mass
        // feels a stronger downward pull (or weaker upward push) than the top mass.
        // This happens when a dense anomaly is directly below or slightly to the side.
        return forceBottomFy - forceTopFy;
    }

    // --- Graphing ---
    function initializeGraph() {
        // Set canvas size to match its display size
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
        drawGraph(); // Draw axes and current data
    }

     function drawGraphAxes() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.strokeStyle = '#555';
        ctx.lineWidth = 1;
        ctx.font = '10px Arial';
        ctx.fillStyle = '#000';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        // Y-axis (vertical line on the right - RTL layout)
        const yAxisX = canvas.width - 30; // Position the Y-axis near the right edge
        ctx.beginPath();
        ctx.moveTo(yAxisX, 10); // Start near top
        ctx.lineTo(yAxisX, canvas.height - 20); // End near bottom
        ctx.stroke();

        // X-axis (horizontal line near the center)
        const xAxisY = canvas.height / 2;
        ctx.beginPath();
        ctx.moveTo(10, xAxisY); // Start near left
        ctx.lineTo(canvas.width - 40, xAxisY); // End near Y-axis
        ctx.stroke();

         // Y-axis zero label
        ctx.fillText('0', yAxisX + 15, xAxisY);

         // Draw a subtle horizontal grid line for the zero line
         ctx.strokeStyle = '#ddd';
         ctx.lineWidth = 0.5;
         ctx.beginPath();
         ctx.moveTo(10, xAxisY);
         ctx.lineTo(canvas.width - 40, xAxisY);
         ctx.stroke();

          // Add vertical grid lines for visual guidance (e.g., quarter points)
          const quarter1X = 10 + (canvas.width - 50) / 4;
          const quarter2X = 10 + (canvas.width - 50) / 2; // Center
          const quarter3X = 10 + (canvas.width - 50) * 3 / 4;

          ctx.strokeStyle = '#eee';
          ctx.beginPath();
          ctx.moveTo(quarter1X, 10); ctx.lineTo(quarter1X, canvas.height - 20);
          ctx.moveTo(quarter2X, 10); ctx.lineTo(quarter2X, canvas.height - 20);
          ctx.moveTo(quarter3X, 10); ctx.lineTo(quarter3X, canvas.height - 20);
          ctx.stroke();

    }

    function updateGraphData() {
        const currentGradiometerLeft = gradiometer.offsetLeft;
        const gradientValue = calculateGravityGradient();

        // Store raw data { simulationX: value }
        rawGraphData.push({ simulationX: currentGradiometerLeft, value: gradientValue });

        // Keep graphData sorted by simulationX for drawing
        rawGraphData.sort((a, b) => a.simulationX - b.simulationX);

        // Now map raw data to canvas coordinates for drawing
        graphData = rawGraphData.map(point => ({
             x: mapSimulationXToCanvasX(point.simulationX),
             y: point.value
        }));
    }

     function mapSimulationXToCanvasX(simulationX) {
         // Map simulationX (0 to simulationWidth) to canvasX (10 to canvas.width - 40)
         const graphPlottingWidth = canvas.width - 50; // Space between axes
         const graphPlottingStartX = 10; // X-offset for the graph line
         return graphPlottingStartX + (simulationX / simulationWidth) * graphPlottingWidth;
     }

    function drawGraph() {
        drawGraphAxes(); // Clear canvas and redraw axes

        if (graphData.length < 1) {
            return; // Need at least one point
        }

        // Find min/max gradient values for scaling the Y axis
        const yValues = graphData.map(p => p.y);
        // Calculate max absolute value, ensuring it's at least a small value to avoid division by zero
        const maxAbsY = Math.max(...yValues.map(Math.abs), 1); // Include 1 for scaling when gradient is always 0

        const graphCenterY = canvas.height / 2;
        const graphPlottingHeight = canvas.height - 30; // Allow space for labels

        // Function to scale Y value to canvas coordinate
        function scaleY(value) {
            // Scale value from [-maxAbsY, maxAbsY] range to [-1, 1]
            const normalizedValue = value / maxAbsY;
            // Map normalizedValue (-1 to 1) to canvas Y range (graphCenterY + graphPlottingHeight/2 to graphCenterY - graphPlottingHeight/2)
            // A positive normalized value should map to a lower canvas Y (upwards on graph)
            // A negative normalized value should map to a higher canvas Y (downwards on graph)
            return graphCenterY - (normalizedValue * (graphPlottingHeight / 2));
        }

        // Draw the graph line
        ctx.strokeStyle = '#007bff'; /* Blue line */
        ctx.lineWidth = 3; /* Thicker line */
        ctx.lineJoin = 'round'; /* Rounded corners for line segments */

        ctx.beginPath();
        ctx.moveTo(graphData[0].x, scaleY(graphData[0].y));

        for (let i = 1; i < graphData.length; i++) {
            ctx.lineTo(graphData[i].x, scaleY(graphData[i].y));
        }

        ctx.stroke();

         // Draw the current gradiometer position marker line on the graph
         const currentCanvasX = mapSimulationXToCanvasX(gradiometer.offsetLeft);
         ctx.strokeStyle = 'rgba(0, 0, 0, 0.4)'; // Semi-transparent black
         ctx.lineWidth = 1;
         ctx.beginPath();
         ctx.moveTo(currentCanvasX, 10); // Start near top graph boundary
         ctx.lineTo(currentCanvasX, canvas.height - 20); // End near bottom graph boundary
         ctx.stroke();

         // Draw a small circle at the current point
         if (graphData.length > 0) {
             // Find the point closest to the current gradiometer X position
             const closestPoint = graphData.reduce((prev, curr) => {
                 return (Math.abs(curr.x - currentCanvasX) < Math.abs(prev.x - currentCanvasX) ? curr : prev);
             }, graphData[0]);

             ctx.fillStyle = '#007bff'; // Match line color
             ctx.beginPath();
             ctx.arc(closestPoint.x, scaleY(closestPoint.y), 5, 0, Math.PI * 2); // Draw a circle
             ctx.fill();
         }

    }

    function updateSimulation() {
         updateVectorsAndMasses(); // Calculate forces and update vector/mass visuals
         if (isDragging) {
              updateGraphData(); // Add data points only while dragging
         } else {
             // If not dragging (e.g., controls changed), just calculate for current position
             rawGraphData = [{ simulationX: gradiometer.offsetLeft, value: calculateGravityGradient() }];
         }
         drawGraph(); // Redraw the graph with updated data
    }


    // --- Explanation Toggle ---
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.toggle('hidden');
        toggleButton.textContent = isHidden ? 'הצגת ההסבר המלא: איך זה עובד?' : 'הסתרת ההסבר המלא';
    });

    // Initial setup
    initializeGraph();
    updateAnomalyPosition(); // Position anomaly based on default slider value
    updateAnomalyDensity(); // Set anomaly style based on default select value
    updateSimulation(); // Calculate and draw for initial state

    // Update simulation and graph if window is resized
    window.addEventListener('resize', () => {
        simulationWidth = simulationArea.offsetWidth; // Update simulation width
        initializeGraph(); // Re-initialize canvas size and redraw axes
         // Need to re-map rawGraphData points to the new canvas width
         graphData = rawGraphData.map(point => ({
             x: mapSimulationXToCanvasX(point.simulationX),
             y: point.value
        }));
        updateSimulation(); // Recalculate vectors/masses and redraw graph
    });

});
</script>
```