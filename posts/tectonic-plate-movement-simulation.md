---
title: "הדמיית תנועת לוחות טקטוניים"
english_slug: tectonic-plate-movement-simulation
category: "מדעי הסביבה / גיאולוגיה"
tags:
  - גיאולוגיה
  - טקטוניקה
  - לוחות טקטוניים
  - רעידות אדמה
  - הרי געש
---
# תנועת כדור הארץ: הצצה אל הלוחות הטקטוניים

דמיינו לרגע את כדור הארץ לא ככדור סלע אחיד וקשה, אלא כפאזל ענקי של גושים עצומים שנמצאים בתנועה אינסופית ואיטית. התנועה הזו, שמכתיבה את הנוף הדרמטי שאנו רואים – רכסי הרים שמתרוממים לגובה, תעלות עמוקות באוקיינוס, והתפרצויות געשיות רועמות – מתרחשת עמוק מתחת לרגלינו.

הדמיה זו מאפשרת לכם לשלוט בתנועת הלוחות ולראות במו עיניכם את הכוחות הפועלים בגבולותיהם, ולגלות איך נוצרות הפלאים הגיאולוגיים של עולמנו. נסו את סוגי הגבולות השונים, הזיזו את הלוחות, וראו מה קורה!

<div id="simulation-container">
    <div id="controls">
        <h3>בחרו אינטראקציה:</h3>
        <label><input type="radio" name="boundaryType" value="convergent" checked> 🌍 התכנסות (Convergent)</label><br>
        <label><input type="radio" name="boundaryType" value="divergent"> 🌋 התרחקות (Divergent)</label><br>
        <label><input type="radio" name="boundaryType" value="transform"> ⚡ טרנספורם (Transform)</label><br>
        <button id="reset-button">🔁 איפוס הדמיה</button>
    </div>
    <div id="plates-area">
        <div id="plate1" class="plate">לוח א'</div>
        <div id="plate2" class="plate">לוח ב'</div>
        <div id="animation-effect"></div>
        <div id="transform-line" class="effect-line"></div> <!-- Added for transform boundary -->
    </div>
    <div id="interaction-feedback">הזיזו את הלוחות כדי לראות מה קורה...</div>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');

#simulation-container {
    font-family: 'Varela Round', sans-serif;
    margin-top: 30px;
    border: 1px solid #d3d3d3;
    padding: 25px;
    border-radius: 12px;
    background: linear-gradient(to bottom, #f0f0f0, #e0e0e0); /* Subtle gradient */
    max-width: 850px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    position: relative; /* Needed for absolute positioning of feedback */
}

#controls {
    margin-bottom: 25px;
    text-align: center;
    background-color: #ffffff;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

#controls h3 {
    margin-top: 0;
    color: #333;
}

#controls label {
    margin: 0 15px;
    font-size: 1.1em;
    cursor: pointer;
    color: #555;
    transition: color 0.2s ease;
}

#controls label:hover {
    color: #007bff;
}

#controls input[type="radio"] {
    margin-right: 5px;
    transform: scale(1.1); /* Slightly larger radio buttons */
}

#reset-button {
    margin-top: 15px;
    padding: 10px 25px;
    cursor: pointer;
    background-color: #ff4d4d; /* Reddish for reset */
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    font-size: 1em;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

#reset-button:hover {
    background-color: #ff3333;
    transform: translateY(-1px);
}

#plates-area {
    position: relative;
    width: 100%;
    height: 220px; /* Increased height for more space */
    border: 2px solid #8b4513; /* Earthy border */
    overflow: hidden;
    background: linear-gradient(to bottom, #a0522d, #8b4513); /* Represents the mantle/asthenosphere with gradient */
    border-radius: 8px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.2);
}

.plate {
    position: absolute;
    width: 220px; /* Slightly larger plate size */
    height: 160px; /* Slightly larger plate height */
    background: linear-gradient(to bottom right, #c0a080, #a08060); /* Gradient for plate texture */
    border: 3px solid #705030;
    cursor: grab;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    color: #333; /* Darker text for better contrast */
    text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    user-select: none;
    border-radius: 5px;
    transition: left 0.1s ease, top 0.1s ease, box-shadow 0.2s ease; /* Smooth transition for movement */
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
}

.plate:active {
    cursor: grabbing;
    box-shadow: 3px 3px 8px rgba(0,0,0,0.4); /* Shadow feedback on grab */
}

#plate1 {
    left: 40px; /* Adjusted initial position */
}

#plate2 {
     /* Positioned dynamically by JS */
}

#animation-effect {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 0; /* Initially hidden */
    z-index: 2; /* Above plates */
    pointer-events: none;
    text-align: center;
    color: white;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center; /* Center text vertically */
    overflow: hidden;
    transition: all 0.3s ease-out; /* Smooth transition for effects */
    font-size: 1.1em;
    text-shadow: 1px 1px 2px black;
}

/* Specific styles for effects */
.convergent-effect {
     background: linear-gradient(to top, #a0522d, #8b4513); /* Mantle-like color */
     color: white;
     justify-content: flex-start; /* Align text to the left side of the overlap */
     padding-left: 10px;
}

.divergent-effect {
    background: linear-gradient(to top, #ff8c00, #ff4500); /* Vibrant magma */
    color: yellow;
    justify-content: center;
}

.transform-effect {
    /* This is handled by the .effect-line now */
}

.effect-line { /* For Transform Boundary line */
    position: absolute;
    top: 50%; /* Vertically centered */
    left: 0;
    width: 100%; /* Spans the area */
    height: 3px; /* Thicker line */
    background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black */
    z-index: 1;
    pointer-events: none;
    display: none; /* Initially hidden */
}

#interaction-feedback {
    text-align: center;
    margin-top: 20px;
    font-size: 1.1em;
    color: #555;
    min-height: 1.5em; /* Reserve space */
}


#explanation-toggle {
    display: block;
    width: fit-content;
    margin: 30px auto 20px;
    padding: 12px 25px;
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    font-size: 1em;
    transition: background-color 0.2s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#explanation-toggle:hover {
    background-color: #0056b3;
    transform: translateY(-1px);
}

#explanation {
    margin-top: 20px;
    border-top: 1px solid #ccc;
    padding-top: 20px;
    display: none; /* Initially hidden */
    font-family: Arial, sans-serif; /* Different font for readability */
}

#explanation h2, #explanation h3 {
    color: #333;
    margin-bottom: 10px;
}

#explanation p {
    line-height: 1.7;
    text-align: justify;
    margin-bottom: 15px;
    color: #444;
}

#explanation ul {
    margin-bottom: 15px;
    padding-left: 20px;
}

#explanation li {
    margin-bottom: 8px;
    line-height: 1.6;
    color: #444;
}

#explanation strong {
    color: #007bff; /* Highlight key terms */
}

</style>

<button id="explanation-toggle">📚 רוצים לדעת יותר? לחצו כאן להסבר מעמיק</button>

<div id="explanation">
    <h2>מבוא מרתק לטקטוניקת הלוחות</h2>
    <p>קרום כדור הארץ והחלק העליון של המעטפת יוצרים יחד שכבה קשה וקרה יחסית הנקראת <strong>ליתוספרה</strong>. חשבו עליה כעל קליפה שבורה המקיפה את הכדור. הליתוספרה הזו אינה חתיכה אחת גדולה, אלא מפוצלת למספר רב של גושי ענק נפרדים – אלו הם <strong>הלוחות הטקטוניים</strong> שאיתם אתם משחקים למעלה.</p>

    <h3>הנהר הזורם מתחת: האסתנוספירה</h3>
    <p>מתחת לליתוספרה השבורה נמצאת שכבה חמה ו"צמיגה" יותר של המעטפת, שנקראת <strong>אסתנוספירה</strong>. למרות שהיא עדיין סלע, החום והלחץ העצומים גורמים לה להתנהג כמו נוזל סמיך מאוד בפרקי זמן ארוכים להפליא. הלוחות הטקטוניים למעשה "צפים" ומחליקים באיטיות על גבי השכבה הזו, כמו קוביות קרח על נהר קפוא למחצה.</p>

    <h3>הכוח המניע: זרמי הקונבקציה</h3>
    <p>אז מה גורם ללוחות האדירים האלה לנוע? הכוח העיקרי מגיע מ<strong>זרמי קונבקציה</strong> ענקיים בתוך המעטפת. חומר חם ועולה מהמעמקים, מתקרר קרוב לפני השטח, שוקע חזרה מטה, ויוצר מעגל זרימה עצום. זרמים אלו כמו "מערסלים" את הלוחות ומסיעים אותם איתם. כוחות נוספים כמו דחיפה מאזורים בהם נוצר קרום חדש ומשיכה באזורים בהם קרום "בולע" חזרה לתוך המעטפת, גם הם משחקים תפקיד.</p>

    <h2>המפגשים הגורליים: סוגי גבולות לוחות</h2>
    <p>רוב הפעילות הגיאולוגית הדרמטית מתרחשת היכן שהלוחות נפגשים – בגבולותיהם. האופן שבו הלוחות מתקשרים קובע את סוג ה"מופע" הגיאולוגי שנקבל:</p>

    <h3>התנגשות חזיתית: גבול מתכנס (Convergent Boundary)</h3>
    <p>בגבול זה, שני לוחות נעים *אחד אל עבר השני*. זה כמו ששני קרונות רכבת ענקיים עומדים להתנגש! התוצאה תלויה בסוג הלוחות שמתנגשים:</p>
    <ul>
        <li><strong>יבשת פוגשת יבשת:</strong> כששתי פיסות קרום יבשתי עבות ו"קלילות" יחסית מתנגשות, אף אחת מהן לא שוקעת בקלות. במקום זאת, הן מתקמטות, מתקפלות, נשברות ונערמות זו על זו. התוצאה? <strong>רכסי ההרים הגבוהים ביותר בעולם</strong> (חשבו על ההימלאיה, שם הודו מתנגשת באסיה). זו דרמטית!</li>
        <li><strong>אוקיינוס פוגש יבשת:</strong> הקרום האוקייני, שהוא צפוף וכבד יותר מהקרום היבשתי, נכנע ושוקע *מתחת* ללוח היבשתי בתהליך מרהיב הנקרא <strong>השקעה (סאבדוקציה)</strong>. זה יוצר <strong>תעלות אוקייניות</strong> עמוקות בנקודת ההשקעה, וגורם למאגמה לעלות ולפרוץ כ<strong>הרי געש</strong> על הלוח היבשתי (כמו הרי האנדים). אש וטביעה – דרמה בקנה מידה גיאולוגי!</li>
        <li><strong>אוקיינוס פוגש אוקיינוס:</strong> לוח אוקייני אחד (הצפוף יותר) שוקע מתחת לאחר. גם כאן נוצרת <strong>תעלה אוקיינית</strong> עמוקה. המאגמה שעולה יוצרת שרשרת של <strong>איים געשיים</strong> מסודרים בקשת (<strong>קשתות איים</strong>), דוגמאות קלאסיות הן יפן או האיים האלאוטיים. ארכיפלגים של אש!</li>
    </ul>
    <p>תופעת לוואי שכיחה ביותר בגבולות אלו: <strong>רעידות אדמה</strong> רבות ועמוקות, כשהלוח השוקע "מתחכך" ו"נשבר" תוך כדי מסעו מטה.</p>

    <h3>היפרדות דרמטית: גבול מתרחק (Divergent Boundary)</h3>
    <p>כאן, שני לוחות נעים *אחד מהשני*. זה כמו סדק שמתרחב והולך. תהליך זה מוביל ל<strong>יצירה מתמדת של קרום חדש</strong>:</p>
    <ul>
        <li><strong>ברכסים תת-ימיים ענקיים:</strong> במרכז האוקיינוסים, לוחות אוקייניים מתרחקים, ומאגמה לוהטת מהמעטפת עולה כדי למלא את החלל. היא מתקררת, מתגבשת, ויוצרת קרום אוקייני חדש. כך נוצרים <strong>רכסים תת-ימיים</strong> ענקיים המקיפים את כדור הארץ כמו תפר כדור בייסבול (הרכס המרכז-אטלנטי הוא הדוגמה המפורסמת ביותר), עם עמק בקע במרכזם. לידת אדמה חדשה!</li>
        <li><strong>בקעים ביבשות:</strong> לפעמים, תהליך ההתרחקות מתחיל בתוך יבשת ויוצר <strong>עמקי בקע</strong> יבשתיים (כמו הבקע הסורי-אפריקני המפורסם שלנו!). אם התהליך נמשך מספיק זמן, הוא יכול לפצל את היבשת לגמרי ולהוביל להיווצרות אוקיינוס חדש. יבשות נקרעות לגזרים!</li>
    </ul>
    <p>תופעות אופייניות: <strong>התפרצויות געשיות</strong> תכופות (לרוב זורמות ופחות "מתפוצצות" מאשר בגבולות מתכנסים), ו<strong>רעידות אדמה</strong> רדודות וחזקות פחות.</p>

    <h3>החלקה צידית: גבול טרנספורם (Transform Boundary)</h3>
    <p>בגבול זה, הלוחות לא מתנגשים ולא מתרחקים, אלא פשוט <strong>מחליקים אופקית זה לצד זה</strong>. זה כמו שני חלקים של שביל כניסה שנעים זה ליד זה בכיוונים הפוכים. כאן <strong>אין יצירה או השמדה של קרום</strong> – יש רק חיכוך אדיר.</p>
    <p>תופעות אופייניות: המתח העצום שמצטבר כשהלוחות מנסים להחליק זה לצד זה ונתקעים, משתחרר בפתאומיות באחת, וגורם ל<strong>רעידות אדמה</strong> עוצמתיות במיוחד (העתק סן אנדראס בקליפורניה הוא הדוגמה הקלאסית והמפחידה ביותר). זהו גבול של מתח מתפרץ!</p>

    <h2>האמן הגדול: השפעת תנועת הלוחות</h2>
    <p>תנועת הלוחות היא המעצב האולטימטיבי של פני כדור הארץ לאורך מיליוני שנים. היא הכוח העיקרי מאחורי:</p>
    <ul>
        <li>יצירת <strong>רכסי ההרים</strong> המרהיבים והעמקים העמוקים.</li>
        <li>היווצרות <strong>בקעים</strong> ו<strong>תעלות אוקייניות</strong> אדירות.</li>
        <li>רוב הפעילות ה<strong>געשית</strong> (הרי געש) וה<strong>סייסמית</strong> (רעידות אדמה) שמשפיעה על חיינו.</li>
        <li>ההיסטוריה הגיאולוגית המטורפת של כדור הארץ, עם יבשות שהתפצלו, התלכדו, והתנועעו על פני הכדור כמו בסרט אנימציה איטי במיוחד.</li>
    </ul>

    <h2>דוגמאות חיות מסביב לעולם</h2>
    <p>הנה כמה אתרים מפורסמים בהם תוכלו "לראות" את טקטוניקת הלוחות בפעולה:</p>
    <ul>
        <li><strong>הרי הימלאיה:</strong> הדוגמה המושלמת לגבול מתכנס (התנגשות יבשת-יבשת) שעדיין פעיל וגורם להרים לגבוה מדי שנה!</li>
        <li><strong>הרי האנדים:</strong> דוגמה קלאסית לגבול מתכנס (השקעת לוח אוקייני מתחת ללוח יבשתי) שיצר רכס הרים ארוך עם הרי געש פעילים.</li>
        <li><strong>הרכס המרכז-אטלנטי:</strong> עמוד השדרה של האוקיינוס האטלנטי, דוגמה מושלמת לגבול מתרחק שיוצר קרום אוקייני חדש. איסלנד יושבת ממש עליו!</li>
        <li><strong>הבקע הסורי-אפריקני:</strong> ה"חצר האחורית" הגיאולוגית שלנו! גבול מורכב, בעיקר טרנספורם אך גם מתרחק באזורים מסוימים, שגורם לרעידות אדמה גם בישראל.</li>
        <li><strong>העתק סן אנדראס:</strong> בחוף המערבי של ארה"ב, הדוגמה המפורסמת ביותר לגבול טרנספורם שיכול לגרום לרעידות אדמה הרסניות.</li>
    </ul>
    <p>אז בפעם הבאה שאתם שומעים על רעידת אדמה או רואים הר מרשים, זכרו שזו רק הצצה רגעית אל הריקוד האינסופי והעוצמתי של הלוחות הטקטוניים מתחת לרגלינו!</p>
</div>


<script>
const plate1 = document.getElementById('plate1');
const plate2 = document.getElementById('plate2');
const platesArea = document.getElementById('plates-area');
const boundaryTypeRadios = document.querySelectorAll('input[name="boundaryType"]');
const resetButton = document.getElementById('reset-button');
const animationEffect = document.getElementById('animation-effect');
const transformLine = document.getElementById('transform-line'); // Get the new line element
const interactionFeedback = document.getElementById('interaction-feedback'); // Get feedback element
const explanationToggle = document.getElementById('explanation-toggle');
const explanationDiv = document.getElementById('explanation');

let isDragging = false;
let currentPlate = null;
let xOffset, yOffset;
const initialPlate1Left = 40; // Keep consistent with CSS
const plateWidth = 220; // Keep consistent with CSS
const plateHeight = 160; // Keep consistent with CSS
let platesAreaWidth;
let platesAreaHeight;
let initialPlate1Top; // Will be calculated dynamically

// Ensure plates are positioned correctly on load/resize
function positionPlates() {
    platesAreaWidth = platesArea.offsetWidth;
    platesAreaHeight = platesArea.offsetHeight;

    // Center plates vertically
    initialPlate1Top = (platesAreaHeight - plateHeight) / 2;

    plate1.style.left = initialPlate1Left + 'px';
    plate1.style.top = initialPlate1Top + 'px';

    // Position plate2 relative to the right edge initially
    plate2.style.left = platesAreaWidth - initialPlate1Left - plateWidth + 'px';
    plate2.style.top = initialPlate1Top + 'px';

    resetEffect(); // Reset effects when plates are repositioned
}

// Initial positioning and add resize listener
positionPlates();
window.addEventListener('resize', positionPlates);


function dragStart(e) {
    if (e.target.classList.contains('plate')) {
        isDragging = true;
        currentPlate = e.target;
        const rect = currentPlate.getBoundingClientRect();
        const clientX = e.clientX || e.touches[0].clientX;
        const clientY = e.clientY || e.touches[0].clientY;

        xOffset = clientX - rect.left;
        yOffset = clientY - rect.top;

        currentPlate.style.cursor = 'grabbing';
        currentPlate.style.zIndex = 10; // Bring to front
        currentPlate.classList.add('active-drag'); // Add a class for visual feedback
        interactionFeedback.textContent = `מזיז את ${currentPlate.textContent}...`;
    }
}

function dragEnd(e) {
    if (isDragging) {
        isDragging = false;
        if (currentPlate) {
            currentPlate.style.cursor = 'grab';
            currentPlate.style.zIndex = 1; // Reset z-index
            currentPlate.classList.remove('active-drag');
            currentPlate = null;
        }
        interactionFeedback.textContent = 'הזיזו את הלוחות כדי לראות מה קורה...'; // Reset feedback
        // Optional: Add subtle snap-back animation here if desired
    }
}

function drag(e) {
    if (!isDragging || !currentPlate) return;

    e.preventDefault();

    const clientX = e.clientX || e.touches[0].clientX;
    const clientY = e.clientY || e.touches[0].clientY;

    const platesAreaRect = platesArea.getBoundingClientRect();
    let newX = clientX - platesAreaRect.left - xOffset;
    let newY = clientY - platesAreaRect.top - yOffset;

    // Constrain movement within the platesArea
    newX = Math.max(0, Math.min(newX, platesAreaWidth - plateWidth));
    newY = Math.max(0, Math.min(newY, platesAreaHeight - plateHeight));

    const boundaryType = document.querySelector('input[name="boundaryType"]:checked').value;

    // Always update the dragged plate's position
    currentPlate.style.left = newX + 'px';
    currentPlate.style.top = newY + 'px';

    let otherPlate = (currentPlate === plate1) ? plate2 : plate1;

    // React based on boundary type
    if (boundaryType === 'convergent') {
        // Other plate mirrors horizontal movement relative to the center point
        const centerPointX = platesAreaWidth / 2;
        const currentPlateCurrentCenter = newX + plateWidth / 2;
        const otherPlateNewCenter = centerPointX - (currentPlateCurrentCenter - centerPointX);
        otherPlate.style.left = otherPlateNewCenter - plateWidth / 2 + 'px';

        // Other plate mirrors vertical movement to keep them level
        otherPlate.style.top = newY + 'px';

        // --- Convergent Effect Logic ---
        const plate1Right = parseInt(plate1.style.left) + plateWidth;
        const plate2Left = parseInt(plate2.style.left);
        const overlap = plate1Right - plate2Left;

        // Hide transform line
        transformLine.style.display = 'none';

        if (overlap > 10) { // Show effect if plates are overlapping significantly
            const overlapStart = Math.max(parseInt(plate1.style.left), parseInt(plate2.style.left));
            const overlapWidth = overlap; // Use overlap value directly

            animationEffect.style.height = Math.min(overlap * 0.5, platesAreaHeight * 0.3) + 'px'; // Height increases with overlap
             animationEffect.style.top = platesAreaHeight - parseInt(animationEffect.style.height) + 'px'; // Position at the bottom
             animationEffect.style.left = overlapStart + 'px';
             animationEffect.style.width = overlapWidth + 'px';
             animationEffect.textContent = overlap > 50 ? 'לחץ אדיר! קימוט/השקעה' : 'לחץ מצטבר...'; // Dynamic text feedback
             animationEffect.className = 'convergent-effect';
             animationEffect.style.display = 'flex';

             // Prevent massive overlap - 'push back'
             if (currentPlate === plate1 && overlap > plateWidth * 0.7) { // Limit overlap
                 currentPlate.style.left = plate2Left - plateWidth + plateWidth * 0.7 + 'px';
             } else if (currentPlate === plate2 && overlap > plateWidth * 0.7) {
                  currentPlate.style.left = plate1Right - plateWidth * 0.7 + 'px';
             }


        } else {
            resetEffect();
        }


    } else if (boundaryType === 'divergent') {
        // Other plate mirrors horizontal movement relative to the center point
        const centerPointX = platesAreaWidth / 2;
        const currentPlateCurrentCenter = newX + plateWidth / 2;
        const otherPlateNewCenter = centerPointX - (currentPlateCurrentCenter - centerPointX);
        otherPlate.style.left = otherPlateNewCenter - plateWidth / 2 + 'px';

         // Other plate mirrors vertical movement
         otherPlate.style.top = newY + 'px';

        // --- Divergent Effect Logic ---
        const gapStart = parseInt(plate1.style.left) + plateWidth;
        const gapEnd = parseInt(plate2.style.left);
        const gapWidth = gapEnd - gapStart;

        // Hide transform line
        transformLine.style.display = 'none';

        if (gapWidth > 10) { // Show effect if there's a significant gap
             animationEffect.style.height = Math.min(gapWidth * 0.4, platesAreaHeight * 0.5) + 'px'; // Height increases with gap
             animationEffect.style.top = platesAreaHeight - parseInt(animationEffect.style.height) + 'px'; // Position at the bottom
             animationEffect.style.left = gapStart + 'px';
             animationEffect.style.width = gapWidth + 'px';
             animationEffect.textContent = gapWidth > 50 ? 'מאגמה עולה! קרום חדש נוצר' : 'מתרחקים... מתחיל להיווצר בקע'; // Dynamic text
             animationEffect.className = 'divergent-effect';
             animationEffect.style.display = 'flex';
        } else {
             resetEffect();
        }

    } else if (boundaryType === 'transform') {
        // Plates slide past each other horizontally, vertical position is fixed relative to initial
        currentPlate.style.top = initialPlate1Top + 'px'; // Lock vertical position for dragged plate

        // Other plate also fixed vertically
        otherPlate.style.top = initialPlate1Top + 'px';

        // Other plate mirrors horizontal movement
        const centerPointX = platesAreaWidth / 2;
        const currentPlateCurrentCenter = newX + plateWidth / 2;
        const otherPlateNewCenter = centerPointX - (currentPlateCurrentCenter - centerPointX);
        otherPlate.style.left = otherPlateNewCenter - plateWidth / 2 + 'px';


        // --- Transform Effect Logic ---
        resetEffect(); // Hide other effects

        // Show the transform line
        transformLine.style.display = 'block';
        // Position the line correctly (already centered vertically in CSS)
        transformLine.style.top = initialPlate1Top + plateHeight / 2 - 1.5 + 'px'; // Center line between plates

        // Calculate how much horizontal displacement there is between plates relative to their starting positions
        const plate1CurrentX = parseInt(plate1.style.left);
        const plate2CurrentX = parseInt(plate2.style.left);
        const initialPlate2Left = platesAreaWidth - initialPlate1Left - plateWidth; // Calculate initial pos of plate 2

        const initialDistanceBetweenCenters = (initialPlate2Left + plateWidth/2) - (initialPlate1Left + plateWidth/2);
        const currentDistanceBetweenCenters = (plate2CurrentX + plateWidth/2) - (plate1CurrentX + plateWidth/2);

        // The amount of "shear" or sliding is the change in distance between centers
        const shearAmount = Math.abs(currentDistanceBetweenCenters - initialDistanceBetweenCenters);

        // Optional: Add a subtle "shaking" class to plates based on shear
        if (shearAmount > 20 && shearAmount < 100) { // Start shaking after minimal movement, stop if plates get too far?
            plate1.classList.add('shaking-subtle');
            plate2.classList.add('shaking-subtle');
             interactionFeedback.textContent = 'מתח מצטבר! חיכוך לאורך העתק...';
        } else if (shearAmount >= 100) {
             plate1.classList.add('shaking-intense');
             plate2.classList.add('shaking-intense');
             interactionFeedback.textContent = '⚡ רעידת אדמה! המתח משתחרר! ⚡';
        }
        else {
            plate1.classList.remove('shaking-subtle', 'shaking-intense');
            plate2.classList.remove('shaking-subtle', 'shaking-intense');
             interactionFeedback.textContent = 'לוחות מחליקים זה לצד זה...';
        }
    }
}

// Add shaking classes to CSS (need to add this in the style block)
/*
@keyframes subtle-shake {
  0%, 100% { transform: translateX(0) translateY(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-1px) translateY(-0.5px); }
  20%, 40%, 60%, 80% { transform: translateX(1px) translateY(0.5px); }
}

@keyframes intense-shake {
  0%, 100% { transform: translateX(0) translateY(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-3px) translateY(-1.5px); }
  20%, 40%, 60%, 80% { transform: translateX(3px) translateY(1.5px); }
}

.plate.shaking-subtle {
    animation: subtle-shake 0.5s infinite;
}

.plate.shaking-intense {
    animation: intense-shake 0.2s infinite; // Faster and stronger
}
*/
// Adding shaking styles directly into the <style> block below.

function resetEffect() {
     animationEffect.style.height = '0';
     animationEffect.style.width = '0';
     animationEffect.style.backgroundColor = 'transparent';
     animationEffect.textContent = '';
     animationEffect.className = ''; // Remove specific effect class
     animationEffect.style.left = '0';
     animationEffect.style.top = '0';
     animationEffect.style.display = 'none'; // Ensure it's hidden when not active

     transformLine.style.display = 'none'; // Hide the transform line

     // Remove shaking classes
     plate1.classList.remove('shaking-subtle', 'shaking-intense');
     plate2.classList.remove('shaking-subtle', 'shaking-intense');
}

function resetSimulation() {
    positionPlates(); // Use the function that positions based on initial values and area width
    resetEffect(); // Reset any active visual effects
    interactionFeedback.textContent = 'הזיזו את הלוחות כדי לראות מה קורה...'; // Reset feedback text
}

// Event listeners for dragging
platesArea.addEventListener('mousedown', dragStart, false);
platesArea.addEventListener('mouseup', dragEnd, false);
platesArea.addEventListener('mousemove', drag, false);

platesArea.addEventListener('touchstart', dragStart, false);
platesArea.addEventListener('touchend', dragEnd, false);
platesArea.addEventListener('touchmove', drag, false);

// Event listener for boundary type change
boundaryTypeRadios.forEach(radio => {
    radio.addEventListener('change', resetSimulation);
});

// Event listener for reset button
resetButton.addEventListener('click', resetSimulation);

// Event listener for explanation toggle
explanationToggle.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    explanationToggle.textContent = isHidden ? '📚 הסתר הסבר מעמיק' : '📚 רוצים לדעת יותר? לחצו כאן להסבר מעמיק';
});

// Initial reset on page load to ensure correct positioning
resetSimulation();

</script>

<style>
/* Add these shaking animations to the CSS block */
@keyframes subtle-shake {
  0%, 100% { transform: translateX(0) translateY(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-1px) translateY(-0.5px); }
  20%, 40%, 60%, 80% { transform: translateX(1px) translateY(0.5px); }
}

@keyframes intense-shake {
  0%, 100% { transform: translateX(0) translateY(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-3px) translateY(-1.5px); }
  20%, 40%, 60%, 80% { transform: translateX(3px) translateY(1.5px); }
}

.plate.shaking-subtle {
    animation: subtle-shake 0.5s infinite;
}

.plate.shaking-intense {
    animation: intense-shake 0.2s infinite; /* Faster and stronger */
}
</style>
```