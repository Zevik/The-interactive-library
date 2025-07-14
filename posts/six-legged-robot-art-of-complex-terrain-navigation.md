---
title: "רובוט שש-רגלי: אמנות התנועה המדויקת בשטח הפרוע"
english_slug: six-legged-robot-art-of-complex-terrain-navigation
category: "טכנולוגיה / רובוטיקה"
tags:
  - רובוטיקה
  - הנדסה
  - תכנות רובוטים
  - ניווט אוטונומי
  - ביולוגיה
---
# רובוט שש-רגלי: אמנות התנועה המדויקת בשטח הפרוע

התבוננו רגע בנמלה קטנה החוצה שביל גינה עמוס מכשולים - אבן ענקית כאן, מקלון שבור שם, שיפוע מפתיע. איך היא עושה את זה בקלות כזו, כמעט כמו מכונה משומנת? הסוד טמון במבנה שש הרגליים ובקואורדינציית התנועה המופלאה שלה. רובוטי Hexapod (שש-רגליים) שואבים השראה בדיוק מהיכולת הביולוגית המרשימה הזו, כדי לנווט במקומות שבהם רובוטים גלגליים פשוט נכנעים. בואו נצלול לעולם המרתק של הרובוטים האלה ונגלה איך הם מתמודדים עם האתגרים שהטבע מציב בפניהם.

<div id="app-container">
    <h2 class="section-title">סימולטור ניווט Hexapod ראשוני</h2>
    <div id="simulation-area">
         <canvas id="navigationCanvas"></canvas>
        <div id="controls">
            <h3>הגדרות ניווט</h3>
            <div class="control-group">
                <label for="cautiousness">רמת זהירות:</label>
                <input type="range" id="cautiousness" min="0.1" max="1.0" value="0.5" step="0.1">
                <span id="cautiousness-value">0.5</span>
            </div>
             <div class="control-group">
                <label for="gait">סוג הליכה (ויזואלי):</label>
                <select id="gait">
                    <option value="tripod">הליכת חצובה (מהירה, 3 רגליים יציבות)</option>
                    <option value="wave">הליכת גל (איטית, 5 רגליים יציבות)</option>
                </select>
            </div>
             <div class="button-group">
                <button id="runSimulation" class="action-button">הפעל סימולציה</button>
                <button id="resetSimulation" class="secondary-button">אפס הכל</button>
            </div>
        </div>
    </div>
    <div id="results">
        <h3 class="section-title">מצב והתקדמות</h3>
        <p id="status">סטטוס: לחץ על הקנבס להגדרת התחלה.</p>
        <p id="distance-to-target" class="info-text">מרחק ליעד: -</p>
         <p id="time-elapsed" class="info-text">זמן שחלף: 0.0 שניות</p>
    </div>
     <p class="instructions">**כיצד לשחק:** לחץ על המסך להגדרת נקודת התחלה (ירוק) ונקודת סיום (אדום). לחץ על מקש 'O' להוספת מכשול עגול אקראי, 'R' למכשול מלבני. כוון את רמת הזהירות ובחר סוג הליכה. לחץ 'הפעל סימולציה' וצפה ברובוט מנווט!</p>
</div>

<button id="toggleExplanation" class="toggle-button">הצג/הסתר הסבר עומק</button>

<div id="explanation">
    <h2 class="section-title">רובוטים שש-רגליים: המהנדסים של ממלכת החרקים</h2>
    <p>רובוט Hexapod (מיוונית: hexa - שש, pod - רגל) הוא יותר מסתם רובוט עם הרבה רגליים. הוא חיקוי הנדסי מרהיב למבנה הביולוגי המושלם של חרקים רבים, שמאפשר להם להתמודד עם סביבות מורכבות בטבע. רובוטים אלו מציעים יציבות פנומנלית וגמישות תנועה שרובוטים עם גלגלים או זחלים יכולים רק לחלום עליה.</p>
    <p>כל רגל היא יחידה קינמטית בפני עצמה, המחוברת לגוף במפרקים מרובים (בדרך כלל 2 או 3 דרגות חופש) - כמו כתף, ירך וברך בזעיר אנפין. השילוב המתוזמן של תנועת כל הרגליים הוא שמוליד את ה"הליכה" ופותח עולם שלם של יכולות ניווט בשטח פרוע.</p>

    <h2 class="section-title">למה דווקא שש? כוחה של יציבות משולשת</h2>
    <p>היתרון הגדול ביותר של מבנה שש הרגליים מתבטא ביכולת לשמור על יציבות גם בתנאים קשים במיוחד. עם שש רגליים, הרובוט יכול תמיד, אבל תמיד, להבטיח שלפחות שלוש נקודות אחיזה יהיו על הקרקע בכל רגע נתון. תארו לעצמכם חצובה - היא יציבה להפליא. רובוט Hexapod משתמש בעקרון דומה, כשהוא מרים ומניח רגליים בקבוצות של שלוש, הוא תמיד נשען על "חצובה" יציבה אחרת. זה מאפשר לו לטפס על מכשולים, לרדת משיפועים, ואפילו לנווט כשרגל אחת או שתיים באוויר או תקועות.</p>
    <p>הרגליים משמשות גם כ"חיישנים" - הן יכולות לחוש את הקרקע לפני הדריכה, לאתר מדרגות, או להרגיש מתי הקרקע אינה יציבה. גמישות זו היא קריטית להסתגלות אוטונומית.</p>

    <h2 class="section-title">ריקוד הרגליים: סוגי הליכה (Gaits) ואסטרטגיות</h2>
    <p>התנועה של Hexapod היא בראש ובראשונה עניין של קואורדינציה. ה"כוריאוגרפיה" של הרמת והורדת הרגליים נקראת Gait. סוג הגייט משפיע ישירות על מהירות הרובוט, יציבותו, וצריכת האנרגיה שלו. בסימולטור ראינו שתי דוגמאות נפוצות:</p>
    <ul>
        <li><strong>הליכת חצובה (Tripod Gait):</strong> הלהיט המהיר והיעיל ביותר. הרובוט מחלק את רגליו לשתי קבוצות: רגליים קדמית-אחורית בצד אחד ורגל אמצעית בצד השני (לדוגמה: רגליים 1, 4, 5 ורגליים 2, 3, 6). בזמן שקבוצה אחת באוויר ומתקדמת קדימה, הקבוצה השנייה נשארת על הקרקע ומספקת יציבות מקסימלית (זו החצובה!). זה כמו ללכת על שתי קביים לסירוגין.</li>
        <li><strong>הליכת גל (Wave Gait):</strong> האיטי והיציב מכולם. כל רגל נעה בתור שלה, ברצף "גלי" (לדוגמה: רגל 1 עולה ויורדת, אחריה 2, 3, 4, 5, 6, ואז שוב 1...). בכל רגע נתון, לפחות 5 רגליים על הקרקע! זה אידיאלי לניווט על משטחים חלקלקים, תלולים במיוחד, או כאלה הדורשים זהירות מירבית.</li>
    </ul>
    <p>מהנדסים וחוקרים מפתחים גייטים מתוחכמים נוספים, המותאמים למשימות כמו הליכה צדדית, התגברות על מכשולים ספציפיים, או אפילו טיפוס אנכי.</p>

    <h2 class="section-title">החושים של הרובוט: העולם דרך חיישנים</h2>
    <p>כדי שהרובוט יוכל לנווט לבדו, הוא צריך להכיר את סביבתו. ממש כמו שאנו משתמשים בעיניים, באוזניים ובמישוש, רובוטים Hexapod משתמשים במערך חיישנים:</p>
    <ul>
        <li><strong>חיישני מרחק:</strong> (כמו חיישני אינפרה-אדום, אולטרה-סאונד, או מצלמות עומק כמו לידאר) הם "העיניים" של הרובוט. הם סורקים את השטח לפניו ומצדדיו, מזהים קירות, סלעים, בורות, ומודדים את המרחק אליהם. זה מאפשר לרובוט לראות את הדרך מראש ולהגיב למכשולים לפני שהוא מתנגש בהם.</li>
        <li><strong>חיישני מגע וכוח:</strong> ממוקמים לרוב בקצות הרגליים או במפרקים. הם "המישוש" של הרובוט. הם נותנים מידע חיוני על מתי רגל נגעה בקרקע, האם היא נתקלה במשהו לא צפוי, או מה הכוח שמופעל עליה. זה עוזר לרובוט לשמור על שיווי משקל ולהתאים את תנועתו באופן דינמי.</li>
         <li>**חיישני הטיה ואיזון:** (IMU - Inertial Measurement Unit) מזהים את זווית הגוף, תאוצה וקצב סיבוב. הם חיוניים כדי שהרובוט ידע אם הוא נוטה ליפול או נמצא בשיפוע חד, ויכול להתאים את מרכז הכובד שלו או את תנועת הרגליים כדי לשמור על יציבות.</li>
    </ul>
    <p>שילוב המידע מכל החיישנים הללו מספק לרובוט תמונה תלת-ממדית ומורכבת של סביבתו, המאפשרת לו לקבל החלטות ניווט בזמן אמת.</p>

    <h2 class="section-title">איך מחליטים לאן ללכת? אלגוריתמי ניווט והימנעות</h2>
    <p>לוגיקת הניווט האוטונומית משלבת את המידע מהחיישנים, את היעד המבוקש, ואת אסטרטגיית התנועה (הגייט). תהליך ניווט בסיסי (כמו זה המודגם באופן פשטני בסימולטור) כולל:</p>
    <ol>
        <li><strong>סריקת הסביבה:</strong> הרובוט משתמש בחיישני המרחק כדי לזהות מכשולים בנתיב הצפוי שלו. רמת ה"זהירות" בסימולטור קובעת עד כמה רחוק הוא "מסתכל" וכמה מוקדם הוא יגיב למכשול מתקרב.</li>
        <li><strong>תכנון תגובה:</strong> אם מזוהה מכשול, הרובוט צריך להחליט איך להתמודד: לעקוף אותו (ימינה או שמאלה?), האם הוא קטן מספיק כדי לטפס עליו? האם עדיף לעצור ולחפש נתיב חלופי?</li>
        <li><strong>התאמת תנועה (דינמית):</strong> בזמן ההליכה, אם חיישני המגע מזהים מגע לא צפוי או שהרובוט מאבד יציבות (לפי חיישני האיזון), מערכת הבקרה משנה במהירות את תנועות הרגליים כדי לייצב את הרובוט או להתגבר על המכשול המיידי.</li>
        <li><strong>התקדמות מודעת:</strong> לוגיקת הניווט מכוונת את הרובוט באופן כללי לכיוון היעד, אך ההתקדמות בפועל תלויה בזיהוי מכשולים והתמודדות איתם.</li>
    </ol>
    <p>שימו לב: הסימולטור הנוכחי מציג מנגנון הימנעות פשוט ביותר שמגיב למכשולים רק כאשר הם מתקרבים מאוד. מערכות ניווט מתקדמות יותר משתמשות באלגוריתמים מורכבים של תכנון נתיבים (Path Planning) ומיפוי סביבה (Mapping) כדי למצוא את הדרך הטובה ביותר ליעד מראש, תוך התחשבות במכשולים, סוג שטח, ואפילו יעילות אנרגטית.</p>

    <h2 class="section-title">היכן פוגשים Hexapod בעולם האמיתי?</h2>
    <p>היכולת לנוע היכן שאחרים נכשלים הופכת רובוטי Hexapod לכלי עוצמתי ושימושי במגוון תחומים:</p>
    <ul>
        <li><strong>חיפוש והצלה:</strong> הם יכולים להיכנס למבנים שקרסו, חורבות, או שטחים מסוכנים במיוחד כדי לאתר ניצולים או להעביר ציוד קטן, מבלי לסכן חיי אדם.</li>
        <li><strong>בדיקות ותחזוקה תעשייתית:</strong> לבדוק צינורות נפט בשטח קשה, לטפס על מכלים או מבנים, או לנוע בתוך מכונות גדולות לבדיקת תקינות - במקום עבודות בגובה או כניסה למקומות צפופים ומסוכנים.</li>
        <li><strong>חקירת סביבות קיצוניות:</strong> מערות בלתי נגישות, קרקעית האוקיינוס, או אפילו משטחים בכוכבי לכת אחרים (אם כי בנייה לתנאי חלל מורכבת ביותר) - Hexapod יכולים לשאת עליהם חיישנים ומצלמות למיפוי ואיסוף מידע.</li>
        <li><strong>חינוך ומחקר:</strong> הם משמשים פלטפורמות אידיאליות ללימוד רובוטיקה, תכנות מערכות בקרה, פיתוח אלגוריתמי בינה מלאכותית, וחקר ביומכניקה.</li>
    </ul>
    <p>למרות האתגרים ההנדסיים והתוכנתיים הכרוכים בבניית ותכנות Hexapod, הפוטנציאל שלהם להתמודד עם האתגרים הקשים ביותר של ניווט אוטונומי מבטיח שנמשיך לראות אותם מתפתחים ומופיעים במשימות מורכבות יותר ויותר בעתיד.</p>
</div>

<style>
/* גופנים מודרניים ואלגנטיים */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

body {
    font-family: 'Heebo', sans-serif;
    direction: rtl;
    line-height: 1.7;
    color: #333;
    background-color: #f0f2f5;
    padding: 20px;
}

h1 {
    text-align: center;
    color: #1a2e45; /* כחול כהה */
    margin-bottom: 30px;
    font-weight: 700;
}

#app-container {
    background-color: #ffffff;
    border: 1px solid #dcdfe6;
    border-radius: 12px;
    padding: 30px;
    margin: 0 auto 30px auto;
    max-width: 900px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
}

.section-title {
    color: #1a2e45;
    margin-top: 0;
    margin-bottom: 20px;
    font-weight: 700;
    text-align: center;
}

#simulation-area {
    display: flex;
    flex-direction: row-reverse; /*rtl layout*/
    gap: 30px;
    width: 100%;
    justify-content: center;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
}

#navigationCanvas {
    border-radius: 8px;
    box-shadow: 4px 4px 15px rgba(0,0,0,0.1);
    border: 1px solid #c0c4cc;
    background: linear-gradient(to bottom, #e0e0e0, #d0d0d0); /* שיפוע עדין */
    flex-shrink: 0; /* Prevent shrinking */
    width: 100%; /* Default to full width */
    max-width: 600px; /* Max width */
    height: auto; /* Maintain aspect ratio */
    /* Ensure canvas dimensions are set in JS for scaling */
}

#controls {
    background-color: #f4f4f4; /* רקע בהיר יותר לבקרות */
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #dcdfe6;
    display: flex;
    flex-direction: column;
    gap: 15px;
    min-width: 220px;
    flex-grow: 1; /* Allow controls to grow if space available */
    max-width: 300px; /* Limit max width of controls */
}

#controls h3 {
    margin-top: 0;
    text-align: center;
    color: #333;
    font-weight: 700;
    border-bottom: 1px solid #eee;
    padding-bottom: 10px;
}

.control-group {
    display: flex;
    flex-direction: column; /* Stack label and control */
    align-items: flex-start; /* Align items to the right in RTL */
    gap: 5px;
}

.control-group label {
    font-weight: 400; /* Light weight */
    color: #555;
    margin-left: 0; /* Override default margin for stacked layout */
}

.control-group input[type="range"],
.control-group select {
    width: 100%; /* Full width within control group */
    padding: 8px;
    border: 1px solid #dcdfe6;
    border-radius: 4px;
    box-sizing: border-box; /* Include padding and border in element's total width */
}

input[type="range"] {
     /* Custom styling for range input */
     -webkit-appearance: none;
     appearance: none;
     background: #e0e0e0;
     outline: none;
     opacity: 0.7;
     transition: opacity .2s;
}

input[type="range"]:hover {
    opacity: 1;
}

input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 15px;
    height: 15px;
    background: #409eff; /* כחול בהיר */
    cursor: pointer;
    border-radius: 50%;
}

input[type="range"]::-moz-range-thumb {
    width: 15px;
    height: 15px;
    background: #409eff;
    cursor: pointer;
    border-radius: 50%;
}


.button-group {
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-top: 10px;
}

.action-button, .secondary-button {
    padding: 10px 20px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    flex-grow: 1; /* Allow buttons to fill group width */
    text-align: center;
}

.action-button {
    background-color: #409eff; /* כחול בהיר לאקשן עיקרי */
    color: white;
}

.action-button:hover {
    background-color: #1a2e45; /* כחול כהה בהגפה */
    transform: translateY(-1px);
}

.secondary-button {
     background-color: #e6ebf5; /* רקע אפרפר */
     color: #1a2e45;
     border: 1px solid #dcdfe6;
}

.secondary-button:hover {
    background-color: #d3dce6;
    transform: translateY(-1px);
}


#results {
    margin-top: 25px;
    width: 100%;
    text-align: center;
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #eee;
}

#results h3 {
    margin-bottom: 10px;
    color: #1a2e45;
    font-weight: 700;
}

#status {
    font-weight: 700;
    color: #409eff; /* צבע סטטוס */
    margin-bottom: 5px;
}

.info-text {
    font-size: 0.9em;
    color: #555;
    margin-bottom: 3px;
}


.instructions {
    font-size: 0.9em;
    margin-top: 20px;
    color: #666;
    text-align: center;
    background-color: #fffbe6; /* רקע צהבהב עדין */
    border: 1px solid #faecd8;
    padding: 10px;
    border-radius: 6px;
}

.toggle-button {
    display: block;
    width: fit-content;
    margin: 20px auto; /* Center the button */
    padding: 10px 20px;
    background-color: #1a2e45; /* כחול כהה */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

.toggle-button:hover {
     background-color: #0f1d2d; /* כהה יותר בהגפה */
    transform: translateY(-1px);
}


#explanation {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #dcdfe6;
    box-shadow: 0 8px 16px rgba(0,0,0,0.08);
    display: none; /* Hidden by default */
    margin: 20px auto;
    max-width: 900px;
    line-height: 1.8; /* מרווח שורות נוח יותר */
    color: #333;
}

#explanation h2 {
    color: #1a2e45;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
    margin-top: 25px;
    font-weight: 700;
}

#explanation h2:first-child {
    margin-top: 0;
}

#explanation ul {
    margin-top: 15px;
    margin-bottom: 15px;
    padding-right: 25px; /*rtl*/
    list-style-type: disc; /* דיסקיות */
    color: #555;
}

#explanation li {
    margin-bottom: 8px;
}

#explanation p {
    margin-bottom: 20px;
}

#explanation ol {
     margin-top: 15px;
    margin-bottom: 15px;
    padding-right: 25px; /*rtl*/
    list-style-type: decimal; /* מספרים */
    color: #555;
}

#explanation ol li {
    margin-bottom: 8px;
}


/* אנימציה פשוטה לכניסה/יציאה של ההסבר */
#explanation.show {
    animation: fadeIn 0.5s ease-out forwards;
}

#explanation.hide {
    animation: fadeOut 0.5s ease-in forwards;
}

@keyframes fadeIn {
    from { opacity: 0; height: 0; padding: 0 30px; margin: 0 auto; }
    to { opacity: 1; height: auto; padding: 30px; margin: 20px auto; }
}

@keyframes fadeOut {
    from { opacity: 1; height: auto; padding: 30px; margin: 20px auto; }
    to { opacity: 0; height: 0; padding: 0 30px; margin: 0 auto; }
}


/* Responsive adjustments */
@media (max-width: 768px) {
    #simulation-area {
        flex-direction: column; /* Stack canvas and controls vertically */
        align-items: center; /* Center stacked items */
    }

     #controls {
        width: 100%; /* Full width on smaller screens */
        max-width: none;
     }

     #navigationCanvas {
         max-width: 100%;
     }
}

</style>

<script>
const canvas = document.getElementById('navigationCanvas');
const ctx = canvas.getContext('2d');
const runButton = document.getElementById('runSimulation');
const resetButton = document.getElementById('resetSimulation');
const cautiousnessSlider = document.getElementById('cautiousness');
const cautiousnessValueSpan = document.getElementById('cautiousness-value');
const gaitSelect = document.getElementById('gait');
const statusParagraph = document.getElementById('status');
const distanceToTargetSpan = document.getElementById('distance-to-target');
const timeElapsedSpan = document.getElementById('time-elapsed');
const toggleExplanationButton = document.getElementById('toggleExplanation');
const explanationDiv = document.getElementById('explanation');

// Set initial canvas size based on CSS max-width, but allow JS scaling
// Get computed style for max-width and set canvas attributes
const canvasContainer = document.getElementById('simulation-area');
const canvasStyle = window.getComputedStyle(canvas);
let canvasWidth = parseInt(canvasStyle.maxWidth, 10) || 600; // Default if max-width is not set or is 'none'
let canvasHeight = 400; // Fixed height for simplicity

// Adjust canvas size dynamically based on container width if needed
function resizeCanvas() {
    const containerWidth = canvasContainer.offsetWidth - (window.innerWidth <= 768 ? 0 : document.getElementById('controls').offsetWidth + 30); // Account for controls gap
    canvasWidth = Math.min(parseInt(canvasStyle.maxWidth, 10) || 900, containerWidth > 100 ? containerWidth : 600); // Use container width but respect max-width and a minimum
    canvas.width = canvasWidth;
    canvas.height = canvasHeight; // Keep height fixed
    draw(); // Redraw everything on resize
}

// Initial resize and add listener
resizeCanvas();
window.addEventListener('resize', resizeCanvas);


let startPoint = null;
let endPoint = null;
let obstacles = []; // [{type: 'circle', x, y, radius}, {type: 'rect', x, y, width, height}]
// Robot properties
let robot = {
    x: -1, y: -1, // -1 indicates not placed
    size: 20, // Represents the body size
    legBaseSize: 5, // Size of circles representing leg bases
    speed: 2, // Base speed
    cautiousness: 0.5, // 0.1 to 1.0
    gait: 'tripod', // 'tripod' or 'wave'
    color: '#409eff', // Robot body color
    legColor: '#1a2e45', // Leg base color
    lookAheadColor: 'rgba(64, 158, 255, 0.3)', // Color for cautiousness lookahead cone
    pathColor: 'rgba(64, 158, 255, 0.6)', // Color for path trail
    angle: 0, // Robot orientation in radians (unused in basic sim, but good for visuals)
    legs: [ // Represent leg base positions relative to robot center
        { id: 1, angle: -Math.PI / 2.5, group: 1, pulsing: false }, // Front Right (relative angle)
        { id: 2, angle: -Math.PI / 5, group: 2, pulsing: false }, // Mid Right
        { id: 3, angle: 0, group: 1, pulsing: false }, // Back Right
        { id: 4, angle: Math.PI / 2.5, group: 2, pulsing: false }, // Front Left
        { id: 5, angle: Math.PI / 5, group: 1, pulsing: false }, // Mid Left
        { id: 6, angle: 0, group: 2, pulsing: false }  // Back Left
    ]
};

// Adjust leg angles for a more hexagonal look
robot.legs = [
    { id: 1, angle: -Math.PI / 3, group: 1, pulsing: false }, // FR
    { id: 2, angle: -Math.PI, group: 2, pulsing: false }, // MR (Adjusted)
    { id: 3, angle: Math.PI / 3, group: 1, pulsing: false },  // BR
    { id: 4, angle: 2 * Math.PI / 3, group: 2, pulsing: false },  // FL (Adjusted)
    { id: 5, angle: Math.PI, group: 1, pulsing: false },  // ML (Adjusted)
    { id: 6, angle: -2 * Math.PI / 3, group: 2, pulsing: false } // BL
];


let path = []; // Simplified path visualization (robot trail)
let simulationRunning = false;
let animationFrameId = null;
let startTime = null; // For timer

// Pulse animation for gait visualization
let pulseTimer = 0;
let pulseDuration = 500; // ms
let pulseInterval = 600; // ms between pulses
let currentGaitGroup = 1; // For tripod, pulse group 1 then 2

function startGaitPulseAnimation() {
    pulseTimer = 0;
    if (robot.gait === 'tripod') {
         currentGaitGroup = 1;
         // Initial pulse setup
         robot.legs.forEach(leg => leg.pulsing = (leg.group === currentGaitGroup));
    } else if (robot.gait === 'wave') {
         // For wave, pulse sequentially
         robot.legs.forEach(leg => leg.pulsing = false);
         robot.legs[0].pulsing = true; // Start with leg 1
         // Wave sequence animation handled in animation loop
    }
}

function updateGaitPulse(deltaTime) {
    if (!simulationRunning) return;

    pulseTimer += deltaTime;

    if (robot.gait === 'tripod') {
        if (pulseTimer > pulseInterval) {
            currentGaitGroup = currentGaitGroup === 1 ? 2 : 1;
             robot.legs.forEach(leg => leg.pulsing = (leg.group === currentGaitGroup));
            pulseTimer = 0;
        }
    } else if (robot.gait === 'wave') {
         // Wave pulse is more complex - one leg finishes before next starts pulsing
         const legPulseTime = pulseInterval / robot.legs.length; // Time allocated per leg pulse
         const currentLegIndex = Math.floor(pulseTimer / legPulseTime) % robot.legs.length;

         robot.legs.forEach((leg, index) => leg.pulsing = (index === currentLegIndex));

         if (pulseTimer > pulseInterval) {
              pulseTimer = 0; // Reset timer for the next full wave cycle
         }
    }
}


// Update cautiousness value display
cautiousnessSlider.addEventListener('input', (e) => {
    robot.cautiousness = parseFloat(e.target.value);
    cautiousnessValueSpan.textContent = robot.cautiousness.toFixed(1); // Display one decimal
});

gaitSelect.addEventListener('change', (e) => {
    robot.gait = e.target.value;
    // Adjust speed based on gait (example)
    robot.speed = robot.gait === 'tripod' ? 2.5 : 1.8; // Tripod faster, Wave slower but maybe hypothetical better avoidance/stability
    startGaitPulseAnimation(); // Restart pulse animation for new gait
});

// Toggle explanation visibility
toggleExplanationButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none' || explanationDiv.classList.contains('hide');

    if (isHidden) {
        explanationDiv.style.display = 'block';
        explanationDiv.classList.remove('hide');
        explanationDiv.classList.add('show');
        toggleExplanationButton.textContent = 'הסתר הסבר עומק';
    } else {
        explanationDiv.classList.remove('show');
        explanationDiv.classList.add('hide');
        // Hide completely after animation ends
        explanationDiv.addEventListener('animationend', function handler() {
             if (!explanationDiv.classList.contains('show')) { // Ensure it was hide animation
                explanationDiv.style.display = 'none';
                toggleExplanationButton.textContent = 'הצג/הסתר הסבר עומק';
             }
            explanationDiv.removeEventListener('animationend', handler);
        });
    }
});


// Canvas Click for Start/End Points
canvas.addEventListener('click', (event) => {
    if (simulationRunning) return;

    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    if (!startPoint) {
        startPoint = { x, y };
        robot.x = x;
        robot.y = y;
        robot.angle = 0; // Reset robot angle
        path = [{x: robot.x, y: robot.y}]; // Start path trail
        statusParagraph.textContent = 'סטטוס: נקודת התחלה הוגדרה (ירוק). לחץ להגדרת נקודת סיום (אדום).';
        distanceToTargetSpan.textContent = 'מרחק ליעד: -';
        timeElapsedSpan.textContent = 'זמן שחלף: 0.0 שניות';
    } else if (!endPoint) {
        endPoint = { x, y };
        statusParagraph.textContent = 'סטטוס: נקודות התחלה וסיום הוגדרו. מוכן להפעלה!';
         distanceToTargetSpan.textContent = `מרחק ליעד: ${Math.round(Math.sqrt((robot.x - endPoint.x)**2 + (robot.y - endPoint.y)**2))} פיקסלים`;
    } else {
        // Reset if both are set - set new start point
        startPoint = { x, y };
        endPoint = null;
        robot.x = x;
        robot.y = y;
        robot.angle = 0; // Reset robot angle
        path = [{x: robot.x, y: robot.y}]; // Start path trail
        obstacles = []; // Clear obstacles on new start for cleaner reset
        statusParagraph.textContent = 'סטטוס: נקודת התחלה חדשה הוגדרה (ירוק). לחץ להגדרת נקודת סיום (אדום).';
        distanceToTargetSpan.textContent = 'מרחק ליעד: -';
        timeElapsedSpan.textContent = 'זמן שחלף: 0.0 שניות';
    }
    draw();
});

// Keyboard events for adding obstacles
document.addEventListener('keydown', (event) => {
    if (simulationRunning) return;

    const addObstacle = (type) => {
         const safeMargin = 40; // Avoid placing too close to edges or existing points
         let obX, obY;
         let attempts = 0;
         const maxAttempts = 50;
         let placed = false;

         while(!placed && attempts < maxAttempts) {
             obX = Math.random() * (canvas.width - 2 * safeMargin) + safeMargin;
             obY = Math.random() * (canvas.height - 2 * safeMargin) + safeMargin;

             let collisionWithPoints = false;
             if (startPoint && Math.sqrt((obX - startPoint.x)**2 + (obY - startPoint.y)**2) < 40) collisionWithPoints = true;
             if (endPoint && Math.sqrt((obX - endPoint.x)**2 + (obY - endPoint.y)**2) < 40) collisionWithPoints = true;

             if (!collisionWithPoints) {
                  if (type === 'circle') {
                     obstacles.push({ type: 'circle', x: obX, y: obY, radius: 20 + Math.random() * 25 }); // Slightly smaller random range
                 } else if (type === 'rect') {
                     obstacles.push({ type: 'rect', x: obX, y: obY, width: 30 + Math.random() * 30, height: 25 + Math.random() * 25 }); // Slightly smaller random range
                 }
                 placed = true;
             }
             attempts++;
         }
         if(placed) {
             statusParagraph.textContent = `סטטוס: הוסף מכשול ${type === 'circle' ? 'עגול' : 'מלבני'}.`;
             draw();
         } else {
             statusParagraph.textContent = `סטטוס: לא ניתן להוסיף מכשול. נסה שוב או אפס.`;
         }
    };

    if (event.key.toLowerCase() === 'o') {
        addObstacle('circle');
    } else if (event.key.toLowerCase() === 'r') {
         addObstacle('rect');
    }
});


// Drawing function
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw obstacles
    ctx.fillStyle = '#888'; // צבע אפור למכשולים
    obstacles.forEach(obstacle => {
        if (obstacle.type === 'circle') {
            ctx.beginPath();
            ctx.arc(obstacle.x, obstacle.y, obstacle.radius, 0, Math.PI * 2);
            ctx.fill();
        } else if (obstacle.type === 'rect') {
            ctx.fillRect(obstacle.x - obstacle.width / 2, obstacle.y - obstacle.height / 2, obstacle.width, obstacle.height);
        }
    });

    // Draw path (robot trail) with gradient or fading effect? Simpler: fixed color and opacity
     ctx.strokeStyle = robot.pathColor;
     ctx.lineWidth = 2; // Thicker path
     ctx.beginPath();
     if (path.length > 0) {
         ctx.moveTo(path[0].x, path[0].y);
         for (let i = 1; i < path.length; i++) {
             ctx.lineTo(path[i].x, path[i].y);
         }
     }
     ctx.stroke();

    // Draw start point
    if (startPoint) {
        ctx.fillStyle = 'green';
        ctx.beginPath();
        ctx.arc(startPoint.x, startPoint.y, 10, 0, Math.PI * 2); // Slightly larger
        ctx.fill();
        ctx.fillStyle = 'black'; // Text color
        ctx.font = '12px Heebo';
        ctx.textAlign = 'left';
        ctx.fillText('התחלה', startPoint.x + 15, startPoint.y + 4);
    }

    // Draw end point
    if (endPoint) {
        ctx.fillStyle = 'red';
        ctx.beginPath();
        ctx.arc(endPoint.x, endPoint.y, 10, 0, Math.PI * 2); // Slightly larger
        ctx.fill();
         ctx.fillStyle = 'black'; // Text color
         ctx.font = '12px Heebo';
         ctx.textAlign = 'left';
        ctx.fillText('סיום', endPoint.x + 15, endPoint.y + 4);
    }

     // Draw robot
    if (robot.x !== -1 && robot.y !== -1) {
        // Draw robot body (simple shape like a hexagon or just a larger circle for body)
        ctx.fillStyle = robot.color;
        ctx.beginPath();
        // Draw a hexagon shape approximation or body circle
         const bodyRadius = robot.size / 2;
         ctx.arc(robot.x, robot.y, bodyRadius, 0, Math.PI * 2); // Simple body as circle for now
        ctx.fill();

        // Draw leg bases around the body
        const legBaseDist = bodyRadius + 5; // Distance of leg base circles from center
        robot.legs.forEach(leg => {
            // Calculate leg base position relative to robot's current position and angle
            const legX = robot.x + Math.cos(robot.angle + leg.angle) * legBaseDist;
            const legY = robot.y + Math.sin(robot.angle + leg.angle) * legBaseDist;

            ctx.fillStyle = leg.pulsing ? '#ffc107' : robot.legColor; // Pulse color
            ctx.beginPath();
            ctx.arc(legX, legY, robot.legBaseSize + (leg.pulsing ? 3 : 0), 0, Math.PI * 2); // Pulse effect: larger size
            ctx.fill();
             // Optional: Draw leg number
             ctx.fillStyle = leg.pulsing ? '#333' : 'white';
             ctx.textAlign = 'center';
             ctx.textBaseline = 'middle';
             ctx.font = '10px Arial';
             ctx.fillText(leg.id, legX, legY);
        });


        // Draw robot's direction indicator (arrow)
         ctx.strokeStyle = 'white';
         ctx.lineWidth = 2;
         ctx.beginPath();
         ctx.moveTo(robot.x, robot.y);
         ctx.lineTo(robot.x + Math.cos(robot.angle) * (bodyRadius + 10), robot.y + Math.sin(robot.angle) * (bodyRadius + 10));
         ctx.stroke();

        // Draw cautiousness lookahead cone/sector if simulating
         if (simulationRunning && endPoint) {
             const lookAheadDist = 50 + robot.cautiousness * 70; // Size of the lookahead cone
             const coneAngle = Math.PI / 4 * (1 - robot.cautiousness) + Math.PI/8; // Narrower cone for higher cautiousness
             const targetAngle = Math.atan2(endPoint.y - robot.y, endPoint.x - robot.x);

             ctx.fillStyle = robot.lookAheadColor;
             ctx.beginPath();
             ctx.moveTo(robot.x, robot.y);
             ctx.arc(robot.x, robot.y, lookAheadDist, targetAngle - coneAngle/2, targetAngle + coneAngle/2);
             ctx.lineTo(robot.x, robot.y);
             ctx.fill();
         }
    }
}

// Obstacle detection (simplified)
function isColliding(x, y, checkSize, obstacle) {
    const buffer = robot.cautiousness * 15; // Buffer based on cautiousness
    if (obstacle.type === 'circle') {
        const dist = Math.sqrt((x - obstacle.x)**2 + (y - obstacle.y)**2);
        return dist < (checkSize / 2) + obstacle.radius + buffer;
    } else if (obstacle.type === 'rect') {
        // Simple AABB check with buffer
        const obHalfW = obstacle.width / 2 + buffer;
        const obHalfH = obstacle.height / 2 + buffer;
        const obCenterX = obstacle.x;
        const obCenterY = obstacle.y;
        const robotHalf = checkSize / 2; // Use checkSize (can be robot.size or lookAhead size)

        return Math.abs(x - obCenterX) < robotHalf + obHalfW &&
               Math.abs(y - obCenterY) < robotHalf + obHalfH;
    }
    return false;
}


// Basic navigation logic (simplified steering/avoidance)
let lastUpdateTime = performance.now();

function navigate(currentTime) {
    if (!simulationRunning || !startPoint || !endPoint) {
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
             animationFrameId = null;
         }
        return;
    }

    const deltaTime = (currentTime - lastUpdateTime) / 1000; // Delta time in seconds
    lastUpdateTime = currentTime;

    // Update timer display
    const elapsedTime = (currentTime - startTime) / 1000;
    timeElapsedSpan.textContent = `זמן שחלף: ${elapsedTime.toFixed(1)} שניות`;

     // Check proximity to end
     const distToEnd = Math.sqrt((robot.x - endPoint.x)**2 + (robot.y - endPoint.y)**2);
     distanceToTargetSpan.textContent = `מרחק ליעד: ${Math.round(distToEnd)} פיקסלים`;

     if (distToEnd < robot.size * 1.5) { // Reach goal if close enough
         statusParagraph.textContent = 'סטטוס: הגיע ליעד בהצלחה!';
         statusParagraph.style.color = 'green';
         simulationRunning = false;
         draw(); // Final draw
         return;
     }

     // Determine target direction
     const targetAngle = Math.atan2(endPoint.y - robot.y, endPoint.x - robot.x);
     let desiredAngle = targetAngle;

     // Simple Obstacle Avoidance logic (look ahead)
     const lookAheadDist = 30 + robot.cautiousness * 50;
     const lookAheadAngleCheck = Math.PI / 6; // Check points slightly off the direct path
     const anglesToCheck = [desiredAngle, desiredAngle + lookAheadAngleCheck, desiredAngle - lookAheadAngleCheck]; // Check straight and slightly sides
     let collisionDetected = false;
     let steerAwayAngle = null;

     for(const angle of anglesToCheck) {
         const lookAheadX = robot.x + Math.cos(angle) * lookAheadDist;
         const lookAheadY = robot.y + Math.sin(angle) * lookAheadDist;

         for (const ob of obstacles) {
             if (isColliding(lookAheadX, lookAheadY, robot.size * 0.8, ob)) { // Check with slightly less than full robot size for lookahead
                 collisionDetected = true;
                 // Simple avoidance: steer away from the obstacle center relative to robot position
                 const angleToObstacle = Math.atan2(ob.y - robot.y, ob.x - robot.x);
                 // Steer roughly perpendicular to the line to the obstacle, away from it
                 // A simple heuristic: if obstacle is to the left (angleToObstacle > robot.angle), steer right. If right, steer left.
                 // Need to handle angle wrapping (-PI to PI)
                 let angleDiff = angleToObstacle - robot.angle;
                 // Normalize angleDiff to be between -PI and PI
                 if (angleDiff > Math.PI) angleDiff -= 2 * Math.PI;
                 if (angleDiff < -Math.PI) angleDiff += 2 * Math.PI;

                 // If angleDiff is positive (obstacle left/ahead), steer right (-PI/2 relative). If negative (right/ahead), steer left (+PI/2 relative).
                 steerAwayAngle = robot.angle + (angleDiff > 0 ? -Math.PI / 2 : Math.PI / 2);

                 // Ensure steerAwayAngle is within -PI to PI
                 if (steerAwayAngle > Math.PI) steerAwayAngle -= 2 * Math.PI;
                 if (steerAwayAngle < -Math.PI) steerAwayAngle += 2 * Math.PI;

                 desiredAngle = steerAwayAngle; // Prioritize avoidance angle
                 break; // Found a collision, calculate steering and break obstacle loop
             }
         }
         if (collisionDetected) break; // Break angle check loop if collision found
     }


     // Smoothly transition robot angle towards the desired angle
     const angleDifference = desiredAngle - robot.angle;
     // Normalize angleDifference to be between -PI and PI
     let normalizedAngleDiff = angleDifference;
     if (normalizedAngleDiff > Math.PI) normalizedAngleDiff -= 2 * Math.PI;
     if (normalizedAngleDiff < -Math.PI) normalizedAngleDiff += 2 * Math.PI;

     const turnSpeed = Math.PI * 2 * (0.5 + robot.cautiousness * 0.5); // Turn faster if more cautious (or slower?) Let's say faster reaction
     const maxTurn = turnSpeed * deltaTime;
     robot.angle += Math.max(-maxTurn, Math.min(maxTurn, normalizedAngleDiff));

     // Ensure robot.angle is within -PI to PI
      if (robot.angle > Math.PI) robot.angle -= 2 * Math.PI;
      if (robot.angle < -Math.PI) robot.angle += 2 * Math.PI;


     // Calculate next position based on current angle and speed
     let nextX = robot.x + Math.cos(robot.angle) * robot.speed;
     let nextY = robot.y + Math.sin(robot.angle) * robot.speed;


     // Check for direct collision *before* moving
      let directCollision = false;
      for (const ob of obstacles) {
         if (isColliding(nextX, nextY, robot.size * 0.9, ob)) { // Check with robot size, slightly smaller buffer
             directCollision = true;
             statusParagraph.textContent = 'סטטוס: נתקל במכשול!';
             statusParagraph.style.color = 'orange';
             // If collision, stop moving this frame, rely on avoidance steering for next frame
             nextX = robot.x; // Stay put
             nextY = robot.y;
             break; // No need to check other obstacles
         }
     }

     // Update robot position if no direct collision
     if (!directCollision) {
          robot.x = nextX;
          robot.y = nextY;
          statusParagraph.textContent = 'סטטוס: מנווט...';
          statusParagraph.style.color = '#409eff';
     }


     // Add current position to path trail (optional, can limit length)
     path.push({x: robot.x, y: robot.y});
     // Keep path trail from getting too long
     while (path.length > 500) { // Use while loop for efficiency if many points added at once
         path.shift(); // Remove oldest point
     }

    // Update gait pulse animation based on time
    updateGaitPulse(deltaTime * 1000); // Pass delta time in milliseconds

     draw();

     // Continue simulation loop
     animationFrameId = requestAnimationFrame(navigate);
}

runButton.addEventListener('click', () => {
    if (!startPoint || !endPoint) {
        statusParagraph.textContent = 'סטטוס: אנא הגדר נקודת התחלה וסיום.';
         statusParagraph.style.color = 'red';
        return;
    }
    if (simulationRunning) return; // Prevent multiple runs

    simulationRunning = true;
    startTime = performance.now();
    lastUpdateTime = performance.now(); // Initialize last update time
    robot.x = startPoint.x; // Reset robot position
    robot.y = startPoint.y;
     robot.angle = Math.atan2(endPoint.y - robot.y, endPoint.x - robot.x); // Point robot towards start
    path = [{x: robot.x, y: robot.y}]; // Start path trail from the beginning
    statusParagraph.textContent = 'סטטוס: מנווט...';
     statusParagraph.style.color = '#409eff';
     startGaitPulseAnimation(); // Start gait animation

    // Start the reactive navigation loop
     navigate(performance.now()); // Pass initial time
});

resetButton.addEventListener('click', () => {
    simulationRunning = false;
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
    }
    startPoint = null;
    endPoint = null;
    obstacles = [];
    robot.x = -1; // Indicate robot is not placed
    robot.y = -1;
    path = [];
    startTime = null;
    statusParagraph.textContent = 'סטטוס: לחץ על הקנבס להגדרת התחלה.';
    statusParagraph.style.color = '#333';
    distanceToTargetSpan.textContent = 'מרחק ליעד: -';
    timeElapsedSpan.textContent = 'זמן שחלף: 0.0 שניות';
     robot.legs.forEach(leg => leg.pulsing = false); // Stop pulsing
    draw();
});

// Initial draw
draw();

</script>
```