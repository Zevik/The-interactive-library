---
title: "הסוד ההידראולי: כך עוצרים רכב בלחיצת רגל קלה"
english_slug: the-hydraulic-secret-how-car-brakes-work
category: "פיזיקה"
tags:
  - בלמים
  - הידראוליקה
  - חוק פסקל
  - לחץ נוזלים
  - מערכות רכב
---
# הסוד ההידראולי: כך עוצרים רכב בלחיצת רגל קלה

איך זה שבלחיצה קלה בלבד על דוושת הבלם, אתם מצליחים לעצור רכב ששוקל מעל טון ונוסע במהירות גבוהה? נשמע כמו קסם, אבל זה עקרון פיזיקלי מבריק שפועל מאחורי הקלעים, והגיע הזמן לגלות אותו!

<div id="hydraulic-app">
    <div class="app-container">
        <div class="piston-container small-piston-container">
            <div class="piston-label">בוכנה קטנה (מחוברת לדוושת הבלם)</div>
             <div class="force-input">
                <label for="force-small-input">כוח נכנס (F₁):</label>
                <input type="range" id="force-small-input" min="0" max="100" value="20">
                <span id="force-small-value">20</span> ניוטון
            </div>
            <div class="piston small-piston">
                <div class="piston-rod"></div>
                <div class="piston-head"></div>
                <div class="force-arrow small-force-arrow"></div>
            </div>
             <div class="area-label">שטח A₁: <span id="area-small-value">5</span> יחידות</div>
        </div>

        <div class="tube">
            <div class="fluid" id="fluid-pressure"></div>
        </div>

        <div class="piston-container large-piston-container">
             <div class="piston-label">בוכנה גדולה (מחוברת למנגנון הבלם)</div>
            <div class="piston large-piston">
                 <div class="piston-rod"></div>
                <div class="piston-head"></div>
                 <div class="force-arrow large-force-arrow"></div>
            </div>
             <div class="area-label">שטח A₂: <span id="area-large-value">50</span> יחידות</div>
            <div class="force-output">
                <label>כוח יוצא (F₂):</label>
                <span id="force-large-value">200.0</span> ניוטון
            </div>
        </div>
    </div>
     <div class="parameters">
        <div class="param-group">
            <label for="area-small-input">שנה שטח בוכנה קטנה (A₁):</label>
            <input type="range" id="area-small-input" min="1" max="20" value="5">
            <span id="area-small-display">5</span> יחידות
        </div>
        <div class="param-group">
            <label for="area-large-input">שנה שטח בוכנה גדולה (A₂):</label>
            <input type="range" id="area-large-input" min="10" max="200" value="50">
            <span id="area-large-display">50</span> יחידות
        </div>
    </div>
    <div class="pressure-display">
        לחץ בנוזל (P): <span id="pressure-value">4.0</span> פסקל (יחידות מדומות)
    </div>
</div>

<style>
#hydraulic-app {
    font-family: 'Arial', sans-serif;
    direction: rtl;
    text-align: right;
    margin: 30px auto;
    padding: 25px;
    border: none; /* Remove default border */
    border-radius: 15px; /* More rounded corners */
    background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft background gradient */
    max-width: 900px; /* Wider container */
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* Add depth */
    position: relative;
    overflow: hidden; /* Clip fluid animation */
}

.app-container {
    display: flex;
    align-items: center;
    justify-content: space-between; /* Distribute space */
    margin-bottom: 30px;
    gap: 30px; /* Increase gap */
    position: relative; /* For positioning elements */
    z-index: 1; /* Ensure elements are above background */
}

.piston-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 200px; /* Fixed width for better control */
    flex-shrink: 0;
}

.piston-label {
    font-weight: bold;
    margin-bottom: 15px; /* More space */
    text-align: center;
    color: #004d40; /* Dark teal color */
    font-size: 1.1em;
}

.piston {
    display: flex;
    align-items: center;
    position: relative; /* For force arrow positioning */
    transform: translateX(0px); /* Base transform for animation */
    transition: transform 0.3s ease-out; /* Smooth piston movement */
    will-change: transform; /* Hint for performance */
}

.small-piston {
     flex-direction: row; /* Rod points right */
}

.large-piston {
     flex-direction: row-reverse; /* Rod points left */
}

.piston-head {
    background-color: #00796b; /* Teal color */
    border: 2px solid #004d40;
    box-sizing: border-box;
    border-radius: 5px; /* Slightly rounded head */
    transition: width 0.3s ease-out, height 0.3s ease-out; /* Smooth size transition */
    will-change: width, height;
}

.small-piston .piston-head {
    width: 40px; /* Base size */
    height: 40px; /* Base size */
}

.large-piston .piston-head {
     width: 80px; /* Base size */
    height: 80px; /* Base size */
}

.piston-rod {
    background-color: #757575; /* Grey */
    width: 40px; /* Length of the rod */
    transition: height 0.3s ease-out; /* Smooth thickness transition */
    will-change: height;
}

.small-piston .piston-rod {
     height: 8px; /* Base thickness */
}
.large-piston .piston-rod {
    height: 12px; /* Base thickness */
}


.force-arrow {
    position: absolute;
    background-color: #e53935; /* Red */
    width: 8px; /* Thickness */
    bottom: -20px; /* Position below piston */
    left: 50%; /* Center horizontally */
    transform: translateX(-50%);
     transition: height 0.3s ease-out, background-color 0.3s ease-out; /* Smooth transition */
     will-change: height, background-color;
     border-radius: 2px;
}

.small-force-arrow {
     transform: translate(-50%, 100%); /* Position below head */
     left: calc(50% + 20px); /* Adjust to be below the head center */
     bottom: auto;
     top: calc(100% + 5px);
}

.large-force-arrow {
    transform: translate(-50%, 100%); /* Position below head */
     left: calc(50% - 20px); /* Adjust to be below the head center */
     bottom: auto;
     top: calc(100% + 5px);
}


/* Arrowhead using pseudo-elements - More complex with height, skip for now or use simple visuals */
/* Example for small arrow: */
.small-force-arrow::after {
    content: '';
    position: absolute;
    bottom: -8px; /* Position below the main arrow rect */
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 8px solid #e53935; /* Color of the arrow */
}

.large-force-arrow::after {
    content: '';
    position: absolute;
    bottom: -8px; /* Position below the main arrow rect */
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 8px solid #e53935; /* Color of the arrow */
}


.area-label {
    font-size: 0.95em;
    margin-top: 8px; /* More space */
    text-align: center;
    color: #006064; /* Cyan */
}

.force-input, .force-output {
    margin-top: 10px;
    text-align: center;
    font-size: 1em;
    color: #333;
}

.tube {
    width: 250px; /* Length of the tube */
    height: 50px; /* Base height */
    background-color: #b2ebf2; /* Light fluid background */
    position: relative;
    overflow: hidden;
     border: 2px solid #00bcd4; /* Cyan border */
     border-radius: 10px; /* Rounded tube */
     box-sizing: border-box;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-grow: 1; /* Allow tube to grow */
      transition: height 0.3s ease-out; /* Smooth height transition */
}

.fluid {
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, #b2ebf2, #4fb3bf); /* Fluid gradient */
     transition: background 0.5s ease-out, transform 0.3s ease-out; /* Smooth background transition */
     will-change: background, transform;
     transform: scaleX(1); /* Base scale for pressure effect */
     transform-origin: center;
}

/* Optional: Add a subtle animation for pressure */
@keyframes fluidPulse {
    0% { transform: scaleX(1); opacity: 1; }
    50% { transform: scaleX(1.02); opacity: 0.9; }
    100% { transform: scaleX(1); opacity: 1; }
}

.fluid.pressurized {
    background: linear-gradient(to right, #4fb3bf, #00838f); /* More intense gradient */
     animation: fluidPulse 1s infinite alternate ease-in-out; /* Apply pulse animation */
}

.parameters {
    text-align: center;
    margin-top: 25px; /* More space */
    padding-top: 20px;
    border-top: 1px dashed #b0bec5; /* Dashed separator */
    display: flex;
    justify-content: center;
    gap: 30px; /* Gap between parameter groups */
    flex-wrap: wrap; /* Allow wrapping on small screens */
}

.param-group {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.parameters label {
    display: block; /* Display on separate line */
    margin-bottom: 8px;
    font-weight: normal;
    color: #333;
    font-size: 1em;
}

.parameters input[type="range"] {
    width: 180px; /* Wider sliders */
    margin: 0 auto 5px auto; /* Center slider */
    vertical-align: middle;
    -webkit-appearance: none; /* Remove default styling */
    appearance: none;
    height: 8px;
    background: #00bcd4; /* Cyan track */
    outline: none;
    opacity: 0.7;
    transition: opacity .2s;
    border-radius: 5px;
}

.parameters input[type="range"]:hover {
    opacity: 1;
}

.parameters input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #004d40; /* Dark teal thumb */
    cursor: pointer;
    border-radius: 50%; /* Round thumb */
}

.parameters input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #004d40; /* Dark teal thumb */
    cursor: pointer;
    border-radius: 50%; /* Round thumb */
}


.parameters span {
    display: inline-block;
    width: 40px; /* More space for value */
    text-align: center; /* Center value */
    vertical-align: middle;
    font-weight: bold;
    color: #00796b;
}

.pressure-display {
    text-align: center;
    margin-top: 20px;
    font-size: 1.1em;
    font-weight: bold;
    color: #004d40; /* Dark teal */
}

#toggle-explanation {
    display: block;
    margin: 30px auto; /* More space */
    padding: 12px 25px; /* Larger button */
    font-size: 1.1em;
    cursor: pointer;
    border: none;
    background-color: #00796b; /* Teal button */
    color: white;
    border-radius: 8px; /* Rounded corners */
    text-align: center;
    transition: background-color 0.3s ease;
}

#toggle-explanation:hover {
    background-color: #004d40; /* Darker teal on hover */
}

#explanation {
    margin-top: 25px; /* More space */
    padding-top: 25px;
    border-top: 1px dashed #b0bec5; /* Dashed separator */
    display: none; /* Initially hidden */
    color: #333; /* Standard text color */
}

#explanation h2 {
    margin-top: 20px; /* More space */
    margin-bottom: 15px;
    color: #004d40; /* Dark teal */
    font-size: 1.6em;
    border-bottom: 2px solid #00796b; /* Underline heading */
    padding-bottom: 5px;
}
#explanation h3 {
     margin-top: 15px;
     margin-bottom: 10px;
     color: #006064; /* Cyan */
     font-size: 1.3em;
}

#explanation p {
    margin-bottom: 15px; /* More space between paragraphs */
    line-height: 1.7; /* Increased line height */
}

#explanation ul {
    margin-bottom: 15px;
    padding-right: 25px; /* More padding */
}
#explanation li {
    margin-bottom: 8px;
    line-height: 1.6;
}

/* Style the math formula */
#explanation p code {
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    background-color: #e0f2f7; /* Light blue background */
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 1.1em;
}
</style>

<button id="toggle-explanation">הצג/הסתר הסבר מפורט</button>

<div id="explanation">
    <h2>הסבר מפורט: מערכת הבלמים ההידראולית וחוק פסקל</h2>

    <p>מערכת הבלמים ברכב היא אחד המנגנונים הקריטיים לבטיחות. היא מאפשרת לנו להאט ואף לעצור מסה גדולה שנע במהירות באמצעות לחיצה קלה יחסית על דוושת הבלם. איך קסם כזה מתאפשר? בזכות עקרון פיזיקלי גאוני: הידראוליקה, וליתר דיוק - חוק פסקל.</p>

    <h3>מהי מערכת בלמים הידראולית ולמה היא כה יעילה?</h3>
    <p>מערכת הידראולית משתמשת בנוזל (במקרה של בלמים, שמן בלמים מיוחד) כדי להעביר כוח מנקודה אחת לנקודה אחרת. היתרון המרכזי של מערכת כזו הוא היכולת שלה **להגביר כוח**! לחיצה קטנה על הדוושה מתורגמת לכוח עצירה גדול בהרבה בגלגלים, וכל זאת באופן מדויק, מהיר ואמין. בנוסף, נוזל יכול לעבור בצינורות מפותלים, מה שמאפשר גמישות בעיצוב הרכב.</p>

    <h3>מבנה המערכת הבסיסי (כמו בסימולציה שלנו)</h3>
    <p>בפשטות, המערכת כוללת את הרכיבים הבאים:</p>
    <ul>
        <li>**דוושת הבלם + הבוכנה הראשית (Master Cylinder):** הממשק עם הנהג. לחיצת הדוושה דוחפת בוכנה זו (ה'קטנה' בסימולציה), שמכניסה לחץ לנוזל הבלמים בתוך הצינורות.</li>
        <li>**נוזל הבלמים:** נוזל מיוחד (לרוב על בסיס גליקול או סיליקון) שתפקידו להעביר את הלחץ. הוא חייב להיות **בלתי דחיס** כמעט לחלוטין (במציאות הוא דחיס מעט מאוד, אבל למטרת הבנה נתייחס אליו כבלתי דחיס).</li>
        <li>**הצינורות:** מעבירים את נוזל הבלמים והלחץ מהבוכנה הראשית אל הבוכנות בגלגלים.</li>
        <li>**הבוכנות בגלגלים (Wheel Cylinders/Caliper Pistons):** ממוקמות בכל גלגל. הלחץ המגיע מהצינורות דוחף בוכנות אלו (ה'גדולות' בסימולציה), שמפעילות את מנגנון הבלם (למשל, לוחצות רפידות על דיסק) וגורמות לגלגל להאט או לעצור.</li>
    </ul>

    <h3>עקרון הלחץ בנוזלים סגורים: חוק פסקל הוא המפתח!</h3>
    <p>זהו לב המערכת והסימולציה שלנו. חוק פסקל קובע ש**לחץ המופעל על נוזל הנמצא בכלי סגור מועבר באופן אחיד ובכל הכיוונים בתוך הנוזל, וללא הפסד** (בהנחה שהנוזל אידיאלי ובלתי דחיס).</p>
    <p>מתמטית, לחץ מוגדר ככוח ליחידת שטח: <code>P = F / A</code></p>
    <p>במערכת הבלמים, הכוח <code>F₁</code> שאתם מפעילים על הבוכנה הקטנה בשטח <code>A₁</code> יוצר לחץ <code>P₁ = F₁ / A₁</code> בנוזל הבלמים. לפי חוק פסקל, לחץ זה <code>P₁</code> מועבר באופן אחיד לכל חלקי המערכת, כולל הבוכנות הגדולות בגלגלים. לכן, הלחץ על הבוכנה הגדולה בשטח <code>A₂</code> הוא אותו לחץ: <code>P₂ = P₁</code>.</p>

    <h3>איך יחס השטחים מגביר את הכוח? הפלא ההידראולי!</h3>
    <p>מאחר שהלחץ שווה בשתי הבוכנות <code>P₁ = P₂</code>, נוכל לכתוב:</p>
    <p><code>F₁ / A₁ = F₂ / A₂</code></p>
    <p>מכאן ניתן לבודד את הכוח <code>F₂</code> המופעל על הבוכנה הגדולה:</p>
    <p><code>F₂ = F₁ × (A₂ / A₁)</code></p>
    <p>הנוסחה הזו מראה את הקסם! הכוח המופעל על הבוכנה הגדולה <code>F₂</code> שווה לכוח שאתם מפעילים <code>F₁</code> כפול **יחס השטחים** בין הבוכנה הגדולה לקטנה <code>A₂ / A₁</code>. אם שטח הבוכנה הגדולה גדול פי 10 משטח הבוכנה הקטנה (כמו בהגדרת ברירת המחדל בסימולציה), הרי שכוח העצירה שתקבלו יהיה גדול פי 10 מהכוח שהפעלתם על הדוושה!</p>
     <p>שימו לב גם שבגלל שיחס השטחים קובע את הגברת הכוח, הוא קובע גם את היחס ההפוך בתנועה: הבוכנה הגדולה תזוז למרחק קטן יותר לעומת הבוכנה הקטנה (<code>Δx₂ = Δx₁ × (A₁ / A₂)</code>). כך כוח גדול מופעל על מרחק קצר במנגנון הבלם עצמו.</p>


    <h3>יישומים נוספים של חוק פסקל</h3>
    <p>עקרון הגברת הכוח ההידראולית אינו ייחודי רק למערכות בלמים. הוא משמש גם במגבה הידראולי (ג'ק) להרמת רכבים, במכבשים הידראוליים תעשייתיים לעיצוב חומרים, במערכות היגוי כוח ועוד שלל יישומים בתעשייה וטכנולוגיה.</p>
     <p>**טיפ אחרון:** הסימולציה מאפשרת לכם לשחק עם הכוח שאתם מפעילים ועם גודל הבוכנות. נסו לשנות את שטח הבוכנה הגדולה ולהבין איך זה משפיע דרמטית על כוח העצירה שמקבלים בגלגל! תראו איך ככל שהבוכנה הגדולה יחסית לקטנה - כך ההגברה גדולה יותר.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const forceSmallInput = document.getElementById('force-small-input');
    const forceSmallValueSpan = document.getElementById('force-small-value');
    const forceLargeValueSpan = document.getElementById('force-large-value');
    const areaSmallValueSpan = document.getElementById('area-small-value');
    const areaLargeValueSpan = document.getElementById('area-large-value');
    const areaSmallInput = document.getElementById('area-small-input');
    const areaLargeInput = document.getElementById('area-large-input');
    const areaSmallDisplay = document.getElementById('area-small-display');
    const areaLargeDisplay = document.getElementById('area-large-display');
    const smallForceArrow = document.querySelector('.small-force-arrow');
    const largeForceArrow = document.querySelector('.large-force-arrow');
    const fluidElement = document.getElementById('fluid-pressure');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const smallPiston = document.querySelector('.small-piston');
    const largePiston = document.querySelector('.large-piston');
    const smallPistonHead = document.querySelector('.small-piston .piston-head');
    const largePistonHead = document.querySelector('.large-piston .piston-head');
    const smallPistonRod = document.querySelector('.small-piston .piston-rod');
    const largePistonRod = document.querySelector('.large-piston .piston-rod');
    const tubeElement = document.querySelector('.tube');
    const pressureValueSpan = document.getElementById('pressure-value');


    const maxSmallPistonPush = 40; // Max visual push distance for small piston in pixels
    const maxLargePistonPull = -20; // Max visual pull distance for large piston in pixels (negative for left)

    function updateSimulation() {
        const forceSmall = parseFloat(forceSmallInput.value);
        const areaSmall = parseFloat(areaSmallInput.value);
        const areaLarge = parseFloat(areaLargeInput.value);

        // Update displayed values
        forceSmallValueSpan.textContent = forceSmall;
        areaSmallValueSpan.textContent = areaSmall;
        areaLargeValueSpan.textContent = areaLarge;
        areaSmallDisplay.textContent = areaSmall;
        areaLargeDisplay.textContent = areaLarge;

        // Calculate pressure (P = F/A) - Handle division by zero
        const pressure = areaSmall > 0 ? forceSmall / areaSmall : 0;
        pressureValueSpan.textContent = pressure.toFixed(1);

        // Calculate force on large piston (F = P * A)
        const forceLarge = pressure * areaLarge;
        forceLargeValueSpan.textContent = forceLarge.toFixed(1);

        // --- Animations & Visuals ---

        // 1. Force Arrows Scaling
        // Scale arrow height based on force input and output relative to max possibilities
        const maxPossibleForceSmall = parseFloat(forceSmallInput.max);
         // Estimate max possible F2 based on max F1 and max Area ratio
        const maxPossibleForceLarge = (maxPossibleForceSmall / parseFloat(areaSmallInput.min)) * parseFloat(areaLargeInput.max);

        const smallArrowHeight = (forceSmall / maxPossibleForceSmall) * 60 + 15; // Scale height, add base height
        const largeArrowHeight = (forceLarge / maxPossibleForceLarge) * 120 + 25; // Scale height, add base height

        smallForceArrow.style.height = `${Math.min(smallArrowHeight, 100)}px`; // Cap max height
        largeForceArrow.style.height = `${Math.min(largeArrowHeight, 200)}px`; // Cap max height

        // Change arrow color slightly based on force magnitude
        const smallForceIntensity = forceSmall / maxPossibleForceSmall;
        const largeForceIntensity = forceLarge / maxPossibleForceLarge; // Use maxPossibleForceLarge for consistent scaling

        smallForceArrow.style.backgroundColor = `rgb(${229 + smallForceIntensity * 20}, ${57 - smallForceIntensity * 57}, ${53 - smallForceIntensity * 53})`; // Go from red towards darker red
        largeForceArrow.style.backgroundColor = `rgb(${229 + largeForceIntensity * 20}, ${57 - largeForceIntensity * 57}, ${53 - largeForceIntensity * 53})`;


        // 2. Piston Head & Rod Size Scaling based on Area Input
        // Map area values to visual dimensions. Use square root for radius/diameter scaling for better visual representation of area.
        const smallAreaRatio = areaSmall / parseFloat(areaSmallInput.max);
        const largeAreaRatio = areaLarge / parseFloat(areaLargeInput.max);

        const baseSmallSize = 40; // px
        const baseLargeSize = 80; // px
        const maxSmallScale = 1.5; // Scale up to 1.5 times base size
        const maxLargeScale = 1.5; // Scale up to 1.5 times base size

        const smallHeadSize = baseSmallSize * (1 + Math.sqrt(smallAreaRatio) * (maxSmallScale - 1));
        const largeHeadSize = baseLargeSize * (1 + Math.sqrt(largeAreaRatio) * (maxLargeScale - 1));


        smallPistonHead.style.width = `${smallHeadSize}px`;
        smallPistonHead.style.height = `${smallHeadSize}px`;
        smallPistonRod.style.height = `${smallHeadSize * 0.2}px`; // Rod thickness scales with piston head

        largePistonHead.style.width = `${largeHeadSize}px`;
        largePistonHead.style.height = `${largeHeadSize}px`;
         largePistonRod.style.height = `${largeHeadSize * 0.2}px`; // Rod thickness scales with piston head

        // Adjust tube height to match scaled small piston head
        tubeElement.style.height = `${smallHeadSize * 0.9}px`; // Make tube slightly smaller than piston head

         // Adjust arrow position slightly based on head size
        smallForceArrow.style.left = `calc(50% + ${smallHeadSize/2}px)`;
        largeForceArrow.style.left = `calc(50% - ${largeHeadSize/2}px)`;


        // 3. Piston Movement (Displacement)
        // Visual displacement is proportional to input force slider value and inverse area ratio
        const forceInputRatio = forceSmall / maxPossibleForceSmall; // 0 to 1
        const areaRatio = areaSmall / areaLarge; // How much smaller is A1 than A2 (0 to ~2)

        // Small piston moves based on how much force is "applied" (mapped from slider)
        const smallPistonDisplacement = forceInputRatio * maxSmallPistonPush; // Moves right

        // Large piston moves less distance, proportional to the inverse area ratio
        // The total volume displaced is Area * Displacement
        // Volume_small = Volume_large => A1 * Dx1 = A2 * Dx2
        // Dx2 = Dx1 * (A1 / A2)
        // We link Dx1 conceptually to smallPistonDisplacement
        const largePistonDisplacement = smallPistonDisplacement * areaRatio * -1; // Moves left (-1 for direction)

        smallPiston.style.transform = `translateX(${smallPistonDisplacement}px)`;
        largePiston.style.transform = `translateX(${largePistonDisplacement}px)`;


        // 4. Fluid Pressure Visualization
        const pressureNormalized = Math.min(pressure / 10, 1); // Normalize pressure (adjust divisor for desired sensitivity)

        if (pressure > 0.1) { // Only show pressure effect if force is applied
            fluidElement.classList.add('pressurized');
            // Adjust background gradient based on pressure intensity
             fluidElement.style.background = `linear-gradient(to right, rgba(79, 179, 191, ${0.7 + pressureNormalized * 0.3}), rgba(0, 131, 143, ${0.7 + pressureNormalized * 0.3}))`;
        } else {
            fluidElement.classList.remove('pressurized');
             fluidElement.style.background = ''; // Reset to default CSS gradient
        }

        // Optional: Fluid 'flow' animation - this is tricky to do purely with CSS/JS without more complex graphics.
        // A subtle shift or ripple could be added, but let's stick to the current pressure visualization.
    }

    // Add event listeners
    forceSmallInput.addEventListener('input', updateSimulation);
    areaSmallInput.addEventListener('input', updateSimulation);
    areaLargeInput.addEventListener('input', updateSimulation);

    // Initial update
    updateSimulation();

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מפורט';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג/הסתר הסבר מפורט';
        }
    });
});
</script>
---