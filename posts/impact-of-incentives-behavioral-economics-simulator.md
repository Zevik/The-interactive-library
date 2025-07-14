---
title: "השפעת תמריצים: גלו את הפסיכולוגיה מאחורי ההחלטות שלנו"
english_slug: impact-of-incentives-behavioral-economics-simulator
category: "מדעי החברה / כלכלה התנהגותית"
tags: [תמריצים, קבלת החלטות, כלכלה התנהגותית, פסיכולוגיה כלכלית, התנהגות צרכנים, קנסות, בונוסים]
---
<div class="intro-section">
    <h1>השפעת תמריצים: גלו את הפסיכולוגיה מאחורי ההחלטות שלנו</h1>

    <p>חשבתם פעם מה באמת מניע אנשים לקבל החלטות? למה מבצע "קנה 1 קבל 1 חינם" מרגיש כל כך משתלם גם כשלא באמת צריך את המוצר השני? או איך ייתכן שדווקא הוספת קנס קטן על איחור יכולה לגרום ליותר אנשים לאחר, במקום פחות?</p>

    <p>ברוכים הבאים לעולם המרתק של הכלכלה ההתנהגותית! במקום להניח שאנשים פועלים תמיד באופן רציונלי כדי למקסם רווחים, תחום זה חוקר כיצד גורמים פסיכולוגיים, חברתיים וקוגניטיביים משפיעים על הבחירות שלנו, במיוחד כשמדובר בתמריצים – אותם "דחיפות" כלכליות שמכוונות את ההתנהגות.</p>

    <p>הסימולטור שלפניכם יאפשר לכם להתנסות באופן פעיל עם אחד האפקטים המפתיעים של תמריצים שליליים (קנסות) – כיצד גובה הקנס יכול להשפיע על התנהגות בצורות שאינן ליניאריות ואף הפוכות מהמצופה על פי המודל הקלאסי. מוכנים לשחק ולגלות?</p>
</div>


<div id="app-container">
    <h2>סימולטור איחורים: קנס או נורמה?</h2>
    <p class="simulator-description">הסימולטור מדמה מצב בו אנשים נוטים לאחר בשיעור מסוים (למשל, איחור באיסוף ילדים בגן, החזרת ספרים לספרייה וכו'). בדקו כיצד הטלת קנס בגבהים שונים משפיעה על שיעור האיחורים הכולל, והיו עדים לאפקטים מפתיעים מהעולם האמיתי.</p>
    
    <div class="controls">
        <div class="input-group">
            <label for="baseLateness">שיעור איחורים בסיסי (ללא קנס):</label>
            <input type="number" id="baseLateness" value="15" min="0" max="100" step="1"><span>%</span>
        </div>

        <div class="input-group">
            <label for="penaltyAmount">גובה הקנס המוצע:</label>
            <input type="number" id="penaltyAmount" value="0" min="0" max="1000" step="1"><span>₪</span>
        </div>

        <button id="runSimulation">
            <span class="button-text">הרץ סימולציה</span>
            <span class="button-icon">▶️</span>
        </button>
    </div>

    <div class="results">
        <h3>תוצאות הסימולציה</h3>
        <div class="results-summary">
            <p>שיעור האיחורים הבסיסי (ללא קנס): <span id="baseLatenessResult" class="result-value"></span>%</p>
            <p>גובה הקנס שהוגדר: ₪<span id="penaltyAmountResult" class="result-value"></span></p>
            <p>שיעור האיחורים הצפוי <strong>עם הקנס</strong>: <span id="simulatedLatenessResult" class="result-value final-result"></span>%</p>
        </div>

        <div class="chart">
            <div class="bar-container">
                <div class="bar base-bar" id="baseLatenessBar" style="height: 0%;"></div>
                <span class="bar-label">ללא קנס</span>
                <span class="bar-value" id="baseBarValue"></span>
            </div>
            <div class="bar-container">
                <div class="bar simulated-bar" id="simulatedLatenessBar" style="height: 0%;"></div>
                <span class="bar-label">עם קנס</span>
                 <span class="bar-value" id="simulatedBarValue"></span>
            </div>
        </div>
        <p class="interpretation"><span id="interpretation"></span></p>
    </div>
</div>

<style>
/* General Styles */
body {
    font-family: 'Heebo', sans-serif; /* Or another modern Hebrew-friendly font */
    direction: rtl;
    line-height: 1.7;
    color: #333;
    background-color: #f8f8f8;
    margin: 0;
    padding: 20px;
}

.intro-section {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    text-align: center;
}

.intro-section h1 {
    color: #0056b3; /* Primary blue */
    font-size: 2.5em;
    margin-bottom: 15px;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
}

.intro-section p {
    font-size: 1.1em;
    color: #555;
    margin-bottom: 15px;
}


/* App Container */
#app-container {
    max-width: 650px;
    margin: 40px auto;
    padding: 30px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    background: linear-gradient(to bottom right, #ffffff, #f0f8ff); /* Subtle gradient */
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    direction: rtl;
}

#app-container h2 {
    text-align: center;
    color: #007bff; /* Lighter blue */
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 2em;
    font-weight: 700;
}

.simulator-description {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
    font-size: 1em;
    font-style: italic;
}

/* Controls Section */
.controls {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 30px;
    box-shadow: inset 0 1px 5px rgba(0,0,0,0.05);
}

.input-group {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    justify-content: space-between; /* Space out label and input */
    flex-wrap: wrap; /* Allow wrapping on small screens */
}

.input-group label {
    flex-grow: 1; /* Allow label to take space */
    margin-left: 15px; /* Space between label and input */
    font-weight: bold;
    color: #444;
    min-width: 150px; /* Ensure labels don't get too small */
    text-align: right;
}

.input-group input[type="number"] {
    width: 100px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-sizing: border-box;
    font-size: 1.1em;
    text-align: center; /* Center input text */
    -moz-appearance: textfield; /* Hide arrows in Firefox */
}

.input-group input::-webkit-outer-spin-button,
.input-group input::-webkit-inner-spin-button {
    -webkit-appearance: none; /* Hide arrows in Chrome/Safari */
    margin: 0;
}

.input-group span {
     margin-right: 10px;
     font-size: 1.1em;
     color: #555;
     font-weight: bold;
}

.controls button {
    display: flex; /* Use flexbox for icon and text */
    align-items: center;
    justify-content: center;
    width: 90%; /* Wider button */
    margin: 25px auto 10px;
    padding: 14px 25px;
    background-color: #28a745; /* Green for action */
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.3em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 10px rgba(40, 167, 69, 0.3);
}

.controls button:hover {
    background-color: #218838; /* Darker green */
    box-shadow: 0 6px 12px rgba(40, 167, 69, 0.4);
}

.controls button:active {
    transform: scale(0.98); /* Slightly shrink on click */
}

.button-icon {
    margin-right: 10px; /* Space between icon and text */
}


/* Results Section */
.results {
    margin-top: 30px;
    padding-top: 25px;
    border-top: 2px dashed #eee; /* Visually separate results */
    display: none; /* Hidden by default */
    opacity: 0; /* Start invisible for fade-in */
    transition: opacity 0.5s ease-in-out; /* Fade-in transition */
}

.results.visible {
    display: block;
    opacity: 1;
}

.results h3 {
    color: #007bff;
    text-align: center;
    margin-bottom: 25px;
    font-size: 1.8em;
    font-weight: 700;
}

.results-summary p {
    margin-bottom: 12px;
    line-height: 1.5;
    text-align: right;
    padding-right: 10px;
    font-size: 1.1em;
    color: #555;
}

.result-value {
    font-weight: bold;
    color: #333;
}

.final-result {
     font-size: 1.2em;
     color: #0056b3; /* Darker blue for emphasis */
}


/* Chart */
.chart {
    display: flex;
    justify-content: space-around;
    align-items: flex-end;
    height: 200px; /* Taller chart area */
    margin: 30px auto;
    padding-bottom: 10px;
    border-bottom: 2px solid #ddd;
    border-left: 2px solid #ddd; /* Simple chart axes */
    max-width: 400px; /* Limit chart width */
    position: relative; /* Needed for absolute positioning of values */
    background-color: #fff; /* White background for chart */
    border-radius: 8px;
    padding-top: 10px;
    direction: ltr; /* LTR for bar chart alignment */
}

/* Y-axis indicators (optional, can add later if needed) */
/* .chart::before { content: '100%'; position: absolute; top: 0; right: 100%; margin-right: 5px; font-size: 0.9em; color: #888; }
.chart::after { content: '0%'; position: absolute; bottom: -5px; right: 100%; margin-right: 5px; font-size: 0.9em; color: #888; } */


.bar-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100px; /* Wider bars */
    position: relative;
    text-align: center;
    margin: 0 10px; /* Space between bars */
}

.bar {
    width: 80px; /* Bar width */
    background-color: #007bff; /* Default blue */
    transition: height 1s ease-in-out, background-color 0.6s ease; /* Smooth transition */
    margin-bottom: 8px;
    border-radius: 5px 5px 0 0; /* Rounded top corners */
    min-height: 3px; /* Ensure bar is visible even at 0% */
}

.bar-label {
    font-size: 1em;
    color: #333;
    font-weight: bold;
    margin-top: 8px;
}

.bar-value {
    position: absolute;
    bottom: calc(100% + 5px); /* Position above the bar */
    left: 50%;
    transform: translateX(-50%); /* Center horizontally */
    font-size: 0.9em;
    font-weight: bold;
    color: #333;
    white-space: nowrap; /* Prevent wrapping */
}


/* Specific bar colors based on outcome */
.bar.increase { background-color: #dc3545; } /* Red for increase */
.bar.decrease { background-color: #28a745; } /* Green for decrease */
.bar.same { background-color: #ffc107; } /* Yellow for no change */
.base-bar { background-color: #007bff !important; } /* Base bar is always blue */


/* Interpretation */
.interpretation {
    display: block;
    margin-top: 25px;
    padding: 15px;
    background-color: #e9ecef; /* Light gray background for interpretation */
    border-left: 4px solid #007bff; /* Blue border highlight */
    border-radius: 0 8px 8px 0; /* Rounded right corners */
    font-style: italic;
    color: #555;
    text-align: right;
    min-height: 3em; /* Reserve space */
    opacity: 0; /* Start invisible for fade-in */
    transition: opacity 0.5s ease-in-out 0.3s; /* Fade-in transition after results */
}

.interpretation.visible {
    opacity: 1;
}

/* Explanation Toggle Button */
#showExplanationButton {
    display: block;
    width: 80%;
    max-width: 300px;
    margin: 40px auto 20px;
    padding: 12px 25px;
    background-color: #e9ecef; /* Light gray */
    color: #333;
    border: 1px solid #ccc;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: bold;
    text-align: center;
    transition: background-color 0.3s ease, border-color 0.3s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

#showExplanationButton:hover {
    background-color: #dee2e6;
    border-color: #bbb;
}


/* Explanation Section */
#explanation {
    direction: rtl;
    max-width: 800px;
    margin: 20px auto;
    padding: 30px;
    border: 1px solid #d0d0d0;
    border-radius: 12px;
    background-color: #fff;
    line-height: 1.8;
    color: #333;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    display: none; /* Hidden by default */
    opacity: 0; /* Start invisible for fade-in */
    transition: opacity 0.6s ease-in-out;
}

#explanation.visible {
    display: block;
    opacity: 1;
}

#explanation h2 {
    color: #0056b3;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #eee;
    font-size: 2em;
    text-align: center;
}

#explanation h3 {
    color: #007bff;
    font-size: 1.5em;
    margin-top: 25px;
    margin-bottom: 15px;
    padding-bottom: 5px;
    border-bottom: 1px solid #eee;
}

#explanation p {
    margin-bottom: 18px;
    text-align: right;
}

#explanation ul {
    margin-bottom: 18px;
    padding-right: 25px;
    list-style: disc outside; /* Use disc for list items */
}

#explanation li {
    margin-bottom: 10px;
}

#explanation strong {
    color: #0056b3;
    font-weight: bold;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .intro-section, #app-container, #explanation {
        padding: 20px;
        margin: 20px auto;
    }

    .intro-section h1 {
        font-size: 2em;
    }

    #app-container h2 {
        font-size: 1.8em;
    }

    .controls {
        padding: 15px;
    }

    .input-group {
        flex-direction: column;
        align-items: flex-end;
    }

    .input-group label {
        width: 100%;
        text-align: right;
        margin-left: 0;
        margin-bottom: 5px;
    }

    .input-group input[type="number"] {
        width: 80px; /* Allow inputs to be smaller */
        margin-right: 10px;
    }

    .controls button {
        width: 100%;
        padding: 12px 20px;
        font-size: 1.2em;
    }

    .chart {
        flex-direction: row; /* Keep as row for side-by-side bars */
        height: 180px;
        max-width: 100%;
        margin-top: 20px;
    }

    .bar-container {
        width: 80px;
        margin: 0 5px;
    }

    .bar {
        width: 60px;
    }

    .bar-value {
         font-size: 0.8em;
         bottom: calc(100% + 3px);
    }

    #showExplanationButton {
        width: 90%;
    }
}

@media (max-width: 480px) {
    body {
        padding: 10px;
    }

    .intro-section h1 {
        font-size: 1.8em;
    }

    #app-container h2 {
        font-size: 1.6em;
    }

    .input-group input[type="number"] {
        width: 70px;
    }

    .input-group span {
        margin-right: 5px;
    }

    .controls button {
         padding: 10px 15px;
         font-size: 1.1em;
    }

    .button-icon {
         margin-right: 5px;
    }

    .chart {
        height: 150px;
    }

    .bar-container {
        width: 70px;
        margin: 0 3px;
    }

    .bar {
        width: 50px;
    }

    .bar-label {
        font-size: 0.9em;
    }

    .bar-value {
         font-size: 0.7em;
    }

    #explanation h2 {
        font-size: 1.6em;
    }

    #explanation h3 {
        font-size: 1.3em;
    }
}

</style>

<button id="showExplanationButton">מה קרה פה בעצם? (הצג הסבר מעמיק)</button>

<div id="explanation">
    <h2>הסבר מעמיק: תמריצים, נורמות, ופסיכולוגיה כלכלית</h2>

    <p>הסימולטור שבו התנסיתם ממחיש נקודה מרכזית בכלכלה התנהגותית: ההשפעה של תמריצים על התנהגות אינה תמיד פשוטה וליניארית. בעוד שמודלים כלכליים קלאסיים מניחים שאנשים מגיבים לתמריצים כספיים בצורה רציונלית וצפויה (יותר עלות = פחות מהפעולה; פחות עלות/יותר תועלת = יותר מהפעולה), המציאות מורכבת יותר ומושפעת מגורמים פסיכולוגיים.</p>

    <h3>תמריצים כלכליים: כוחם ומגבלותיהם</h3>
    <p>תמריצים הם כלים רבי עוצמה לעיצוב התנהגות – מבונוסים לעובדים, דרך מבצעים ללקוחות ועד קנסות על עבירות או מסים על פעילויות מסוימות. הרעיון הוא לשנות את "המחיר" או "התועלת" של פעולה מסוימת כדי להשפיע על ההחלטה האם לבצע אותה. אולם, ההשפעה אינה רק כלכלית; היא גם פסיכולוגית וחברתית.</p>

    <h3>האפקט המפתיע של קנסות נמוכים: דחיקת מוטיבציה פנימית (Crowding Out) וכשל התמריץ</h3>
    <p>בסימולטור, ובתרחישים אמיתיים רבים (הדוגמה הקלאסית מגיעה ממחקר על איחורים באיסוף ילדים בגני ילדים בישראל), קנס נמוך לא רק שלא הפחית איחורים, אלא אף הגדיל אותם. מדוע זה קורה?</p>
    <ul>
        <li><strong>נורמה חברתית מול שיקול כלכלי:</strong> לפני הטלת הקנס, ההחלטה לא לאחר נבעה כנראה משילוב של גורמים – אכפתיות כלפי הצוות או אחרים (נורמה חברתית/מוסרית), רצון להיתפס כאחראי, ותחושת מחויבות. כל אלו הן סוגים של <strong>מוטיבציה פנימית או חברתית</strong>. ברגע שהוטל קנס כספי, במיוחד אם הוא נמוך, הוא שינה את התפיסה. איחור הפך מ"דבר לא נעים שאני לא אמור לעשות כי הוא פוגע באחרים" ל"שירות בתשלום" או "מחיר קטן ששווה לשלם עבור הנוחות".</li>
        <li><strong>אפקט דחיקת המוטיבציה (Crowding Out Effect):</strong> התמריץ החיצוני (הקנס) "דחק" החוצה את המוטיבציה הפנימית/חברתית שהייתה קיימת קודם. האנשים הפסיקו לשקול שיקולים מוסריים או חברתיים והתחילו להתייחס לאיחור כאל עסקת עלות-תועלת פשוטה. עבור קנס נמוך, התועלת (הנוחות של איחור) עלתה על העלות (הקנס), ולכן יותר אנשים בחרו לאחר.</li>
        <li><strong>הטיית מסגור (Framing Effect):</strong> הצגת הקנס "מסגרת" את המצב באופן שונה. במקום תפיסה של "אסור לאחר", נוצרת תפיסה של "מותר לאחר אם משלמים".</li>
    </ul>

    <h3>מתי קנס כן עובד? אפקט ההרתעה</h3>
    <p>כפי שהסימולטור הראה גם כן, כאשר הקנס הופך גבוה מספיק (מעבר ל"סף התפיסה" שבו הוא נחשב למחיר זניח), הוא חוזר להיות אפקטיבי כגורם מרתיע. במקרה זה, העלות הכספית של האיחור הופכת משמעותית מספיק כדי לעלות על התועלת הנתפסת מהאיחור, ואפקט ההרתעה של תמריץ שלילי נכנס לפעולה, מה שמוביל לירידה בשיעור האיחורים.</p>

    <h3>המסקנה להתנהגות כלכלית מעשית</h3>
    <p>עיצוב מדיניות המבוססת על תמריצים (בשווקים, בארגונים, או ברמת המדינה) דורש הבנה שאינה מסתמכת רק על ההנחה של רציונליות כלכלית טהורה. יש לקחת בחשבון את ההשפעות הפסיכולוגיות, האופן שבו התמריץ מתקשר לנורמות קיימות (והאם הוא עלול לדחוק אותן), וכיצד אנשים תופסים את גובה התמריץ או העונש ביחס להקשר הכללי. במקרים רבים, שילוב של תמריצים כלכליים עם אלמנטים לא-כלכליים (כמו הדגשת נורמות חברתיות, חיזוק מוטיבציה פנימית, או פידבק אישי) יניב תוצאות טובות ויציבות יותר.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const runButton = document.getElementById('runSimulation');
    const baseLatenessInput = document.getElementById('baseLateness');
    const penaltyAmountInput = document.getElementById('penaltyAmount');
    const resultsDiv = document.querySelector('.results');
    const baseLatenessResultSpan = document.getElementById('baseLatenessResult');
    const penaltyAmountResultSpan = document.getElementById('penaltyAmountResult');
    const simulatedLatenessResultSpan = document.getElementById('simulatedLatenessResult');
    const baseLatenessBar = document.getElementById('baseLatenessBar');
    const simulatedLatenessBar = document.getElementById('simulatedLatenessBar');
    const baseBarValueSpan = document.getElementById('baseBarValue');
    const simulatedBarValueSpan = document.getElementById('simulatedBarValue');
    const interpretationSpan = document.getElementById('interpretation');
    const showExplanationButton = document.getElementById('showExplanationButton');
    const explanationDiv = document.getElementById('explanation');

    // Behavioral parameters - Tuned slightly for demo clarity
    const perceivedValueThreshold = 40; // NIS - below this, penalty is 'cheap'
    const latenessIncreaseFactor = 1.6; // How much lateness increases when penalty is low (e.g., 1.6 means 60% increase from base)
    const latenessDecreaseFactor = 0.4; // How much lateness decreases when penalty is high (e.g., 0.4 means 60% decrease from base)

    runButton.addEventListener('click', () => {
        const baseLatenessPercent = parseInt(baseLatenessInput.value);
        const penaltyAmount = parseInt(penaltyAmountInput.value);

        // Input validation
        if (isNaN(baseLatenessPercent) || baseLatenessPercent < 0 || baseLatenessPercent > 100) {
            alert('אנא הזן שיעור איחורים בסיסי תקין (בין 0 ל-100).');
            return;
        }
        if (isNaN(penaltyAmount) || penaltyAmount < 0) {
             alert('אנא הזן גובה קנס תקין (מספר אי-שלילי).');
             return;
        }

        let simulatedLatenessPercent;
        let interpretationText = '';

        if (penaltyAmount === 0) {
            // No penalty - lateness is the base rate
            simulatedLatenessPercent = baseLatenessPercent;
            interpretationText = 'ללא קנס, שיעור האיחורים נשאר כפי שהוא, מושפע רק מגורמים כמו נורמות חברתיות או נוחות אישית.';
        } else if (penaltyAmount <= perceivedValueThreshold) {
            // Low penalty (> 0 and <= threshold) - lateness increases (crowding out effect)
            // Simulate a slightly smoother increase based on how close penalty is to the threshold
            // Increase is max at penalty > 0, then slightly tapers towards the threshold
            // Factor goes from latenessIncreaseFactor at penalty=1 towards 1.0 at penalty=threshold
            // Formula: base * (1 + (latenessIncreaseFactor - 1) * (1 - (penalty / (perceivedValueThreshold + 1))))
             simulatedLatenessPercent = Math.min(100, Math.round(baseLatenessPercent * (1 + (latenessIncreaseFactor - 1) * (1 - (penaltyAmount / (perceivedValueThreshold + 1))))));
             if (simulatedLatenessPercent > baseLatenessPercent) {
                 interpretationText = `הקנס הנמוך (₪${penaltyAmount}) עשוי להיתפס כ"מחיר" לגיטימי לנוחות האיחור. אפקט ה"דחיקה" של הנורמה החברתית על ידי שיקול כלכלי יכול להוביל לעלייה מפתיעה בשיעור האיחורים.`;
             } else { // Should not happen often with default values if baseLateness > 0
                 interpretationText = `הקנס הנמוך (₪${penaltyAmount}) לא יצר הרתעה מספקת ולא השפיע משמעותית על הורדת שיעור האיחורים.`;
             }

        } else {
            // High penalty (> threshold) - lateness decreases (deterrent effect)
            // Simulate a slightly smoother decrease based on how much penalty exceeds the threshold
            // Decrease is stronger the higher the penalty above the threshold
            // Factor goes from 1.0 at penalty=threshold towards latenessDecreaseFactor at higher penalties
            // Max penalty to consider for the decrease scale to avoid simulating infinite decrease: Let's use 500 for scale example
            const maxPenaltyConsideredForDecrease = 500; // Define a range for deterrent effect scaling
            const effectivePenalty = Math.min(penaltyAmount, maxPenaltyConsideredForDecrease);
            const decreaseScale = (effectivePenalty - perceivedValueThreshold) / (maxPenaltyConsideredForDecrease - perceivedValueThreshold);
            const effectiveDecreaseFactor = 1.0 - (1.0 - latenessDecreaseFactor) * decreaseScale;

             simulatedLatenessPercent = Math.max(0, Math.round(baseLatenessPercent * effectiveDecreaseFactor));

             if (simulatedLatenessPercent < baseLatenessPercent) {
                 interpretationText = `הקנס הגבוה (₪${penaltyAmount}) חוזר להיות גורם מרתיע יעיל. העלות הכספית גבוהה מספיק כדי לגרום לאנשים להימנע מאיחור ולהוביל לירידה בשיעור האיחורים.`;
            } else { // Should only happen if baseLateness is 0
                 interpretationText = `גם קנס גבוה אינו משפיע על שיעור איחורים שכבר עומד על אפס.`;
            }
        }

        // Ensure results are within 0-100%
        simulatedLatenessPercent = Math.max(0, Math.min(100, simulatedLatenessPercent));

        // Hide results initially for a cleaner reveal
        resultsDiv.classList.remove('visible');
        interpretationSpan.classList.remove('visible');

        // Update results text immediately
        baseLatenessResultSpan.textContent = baseLatenessPercent;
        penaltyAmountResultSpan.textContent = penaltyAmount;
        simulatedLatenessResultSpan.textContent = simulatedLatenessPercent;
        interpretationSpan.textContent = interpretationText;
        baseBarValueSpan.textContent = `${baseLatenessPercent}%`;
        simulatedBarValueSpan.textContent = `${simulatedLatenessPercent}%`;


        // Use a small delay before showing results and animating bars
        // This allows the opacity transition to work smoothly
        setTimeout(() => {
            // Show results section with fade-in
            resultsDiv.classList.add('visible');

            // Update chart bars height and color after displaying the div
            const chartMaxHeightPx = 200; // Corresponds to 100% lateness based on CSS height
            const maxPossiblePercentage = 100;
            const minBarHeightPx = 3; // px, minimum height for > 0% to be visible


            const baseHeightPx = (baseLatenessPercent / maxPossiblePercentage) * chartMaxHeightPx;
            const simulatedHeightPx = (simulatedLatenessPercent / maxPossiblePercentage) * chartMaxHeightPx;

            // Set height with minimum for visibility if > 0%
            baseLatenessBar.style.height = `${baseLatenessPercent > 0 && baseHeightPx < minBarHeightPx ? minBarHeightPx : baseHeightPx}px`;
            simulatedLatenessBar.style.height = `${simulatedLatenessPercent > 0 && simulatedHeightPx < minBarHeightPx ? minBarHeightPx : simulatedHeightPx}px`;


            // Change simulated bar color based on outcome
            simulatedLatenessBar.classList.remove('increase', 'decrease', 'same');
            if (simulatedLatenessPercent < baseLatenessPercent) {
                simulatedLatenessBar.classList.add('decrease'); // Green
            } else if (simulatedLatenessPercent > baseLatenessPercent) {
                simulatedLatenessBar.classList.add('increase'); // Red
            } else {
                simulatedLatenessBar.classList.add('same'); // Yellow
            }

             // Show interpretation after a slight delay
            setTimeout(() => {
                 interpretationSpan.classList.add('visible');
             }, 400); // Delay interpretation reveal slightly after bars animate

        }, 50); // Short delay before showing results div

    });

     // Toggle explanation visibility
     showExplanationButton.addEventListener('click', () => {
         const isHidden = !explanationDiv.classList.contains('visible'); // Check based on class
         if (isHidden) {
             explanationDiv.style.display = 'block'; // Ensure it's block before adding visible class
             setTimeout(() => { // Allow display:block to take effect before transition
                 explanationDiv.classList.add('visible');
             }, 10);
             showExplanationButton.textContent = 'הסתר הסבר מעמיק';
             // Scroll to the explanation when shown
              explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });

         } else {
             explanationDiv.classList.remove('visible');
              // Delay display:none until after fade out transition
             setTimeout(() => {
                explanationDiv.style.display = 'none';
             }, 600); // Match transition duration
             showExplanationButton.textContent = 'מה קרה פה בעצם? (הצג הסבר מעמיק)';
         }
     });

    // Initial state for results and explanation
    resultsDiv.classList.remove('visible'); // Ensure it's hidden on load
    explanationDiv.classList.remove('visible'); // Ensure hidden on load
    explanationDiv.style.display = 'none'; // Start with display none

    // Set initial bar values (will be 0% height but values visible)
    baseBarValueSpan.textContent = `${baseLatenessInput.value}%`;
    simulatedBarValueSpan.textContent = `?%`; // Initial state unknown
    baseLatenessBar.style.height = `${(parseInt(baseLatenessInput.value) / 100) * 200 > 0 ? Math.max(3, (parseInt(baseLatenessInput.value) / 100) * 200) : 0}px`; // Show initial base bar height


});

</script>