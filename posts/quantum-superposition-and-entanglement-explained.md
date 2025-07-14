---
title: "מסע אל הלא נודע: סופרפוזיציה ושזירה קוונטית"
english_slug: quantum-superposition-and-entanglement-explained
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה קוונטית
  - סופרפוזיציה
  - שזירה קוונטית
  - מכניקת הקוונטים
  - עולם הקוונטים
---
# מסע אל הלא נודע: סופרפוזיציה ושזירה קוונטית

האם תצליחו לדמיין חלקיק שנמצא בכמה מקומות בבת אחת, או שני חלקיקים שמחוברים בקשר מיסטי, לא משנה כמה גדול המרחק שמפריד ביניהם? זה נשמע כמו פנטזיה מופרעת, אבל ברוכים הבאים לעולם הקוונטי - שבו המציאות עולה על כל דמיון. בואו נצלול לתוך הלב הפועם והמוזר של היקום ונחקור שתיים מהתופעות המסקרנות ביותר שלו: סופרפוזיציה ושזירה.

<div class="interactive-app">
    <h2>צאו למסע הקוונטי</h2>
    <p class="intro-text">בואו נחקור את סופרפוזיציה ושזירה באמצעות סימולציות אינטראקטיביות. נסו, שחקו, מדדו, וגלו את הכללים הייחודיים של העולם הקוונטי בעצמכם.</p>

    <div class="section superposition-section">
        <h3>1. סופרפוזיציה: להיות בכל מקום בבת אחת?</h3>
        <p>חלקיק קוונטי יכול להתקיים במצב מעורפל שבו הוא "גם וגם" - שילוב של כל האפשרויות האפשריות עבורו. כאן נדגים את זה על ספין של חלקיק - מצב שמתואר בדרך כלל כ"למעלה" או "למטה".</p>

        <div class="controls">
            <label for="superposition-prob">קבעו את "סיכוי ההופעה" של מצב 'למעלה' במדידה:</label>
            <div class="range-container">
                 <input type="range" id="superposition-prob" min="0" max="100" value="50" step="1">
                 <span id="prob-display" class="prob-display">50%</span>
            </div>

            <button id="measure-superposition" class="action-button">
                <span class="icon">🔬</span> בצע מדידה אחת
            </button>
            <button id="reset-superposition" class="action-button secondary">
                <span class="icon">🔄</span> אפס סטטיסטיקה
            </button>
        </div>

        <div class="results">
            <h4>תוצאת המדידה האחרונה:</h4>
            <div id="superposition-visual" class="quantum-visual">
                 <div class="superposition-state">?</div>
            </div>

            <div id="superposition-stats" class="stats-box">
                <h4>סיכום מדידות:</h4>
                <p>סה"כ מדידות: <span id="superposition-count">0</span></p>
                <p>תוצאה "למעלה" (↑): <span id="superposition-up">0</span> (<span id="superposition-up-percent">0%</span>)</p>
                <p>תוצאה "למטה" (↓): <span id="superposition-down">0</span> (<span id="superposition-down-percent">0%</span>)</p>
            </div>
        </div>
    </div>

    <div class="section entanglement-section">
        <h3>2. שזירה קוונטית: הקשר העל-חללי</h3>
        <p>שני חלקיקים שזורים חולקים גורל קוונטי משותף. מדידת חלקיק אחד קובעת באופן מידי את מצב השני, לא משנה כמה רחוק הוא! נדגים זאת עם זוג חלקיקים (למשל, פוטונים) שמצבם מתואר על ידי כיוון קיטוב.</p>

        <div class="controls">
            <h4>בחרו את "כיווני המדידה" של ה"גלאים" עבור כל חלקיק:</h4>
            <div class="basis-selects">
                <div class="basis-party">
                    <label for="entanglement-basis-a">חלקיק א':</label>
                    <select id="entanglement-basis-a">
                        <option value="0">0° (אנכי/אופקי)</option>
                        <option value="45">45° (אלכסון)</option>
                        <option value="90">90° (אנכי/אופקי)</option>
                        <option value="135">135° (אלכסון)</option>
                    </select>
                </div>
                 <div class="basis-party">
                    <label for="entanglement-basis-b">חלקיק ב':</label>
                    <select id="entanglement-basis-b">
                        <option value="0">0° (אנכי/אופקי)</option>
                        <option value="45">45° (אלכסון)</option>
                        <option value="90">90° (אנכי/אופקי)</option>
                        <option value="135">135° (אלכסון)</option>
                    </select>
                 </div>
            </div>
            <button id="measure-entangled-pair" class="action-button primary">
                <span class="icon">💥</span> מדוד 100 זוגות שזורים!
            </button>
             <button id="reset-entanglement" class="action-button secondary">
                <span class="icon">🔄</span> אפס סטטיסטיקה
            </button>
        </div>

         <div class="results">
            <h4>תוצאות המדידה האחרונה (עבור זוג אחד מתוך ה-100):</h4>
            <div id="entanglement-last-pair" class="entanglement-pair-results">
                <div class="entangled-particle">
                    <p>חלקיק א' (<span id="last-basis-a">?°</span>):</p>
                    <div id="last-result-a" class="quantum-visual small unknown">?</div>
                </div>
                 <div class="entangled-particle">
                    <p>חלקיק ב' (<span id="last-basis-b">?°</span>):</p>
                    <div id="last-result-b" class="quantum-visual small unknown">?</div>
                 </div>
            </div>
             <div id="entanglement-stats" class="stats-box">
                 <h4>סיכום מתאם התוצאות (מתוך <span id="entanglement-count">0</span> זוגות שנמדדו בבסיסים הנבחרים):</h4>
                 <p><strong>שימו לב:</strong> המתאם בין תוצאות המדידה של החלקיקים תלוי בהפרש הזווית בין כיווני המדידה שבחרתם.</p>
                 <p>תוצאות זהות: <span id="same-results">0</span> (<span id="same-results-percent">0%</span>)</p>
                 <p>תוצאות הפוכות: <span id="different-results">0</span> (<span id="different-results-percent">0%</span>)</p>
             </div>
         </div>
    </div>

</div>

<button id="toggle-explanation" class="toggle-button">הצג הסבר מפורט</button>

<div id="explanation" class="explanation hidden">
    <h2>הסבר מפורט: סופרפוזיציה ושזירה קוונטית</h2>

    <h3>מהי פיזיקה קוונטית וכיצד היא שונה מהפיזיקה הקלאסית?</h3>
    <p>הפיזיקה הקלאסית, כמו זו של ניוטון, מתארת בהצלחה עולם יומיומי צפוי והגיוני - זריקת כדור, תנועת כוכבי לכת. אולם, כשיורדים לעולם החלקיקים הזעירים (אלקטרונים, פוטונים, אטומים), הכללים משתנים באופן דרמטי. כאן שולטת הפיזיקה הקוונטית, והיא חושפת מציאות מוזרה ומלאת הפתעות. ההבדל המרכזי? במקום עולם שבו הכל מוגדר וידוע מראש (דטרמיניסטי), נכנסים לעולם של אפשרויות והסתברויות. אי אפשר לדעת בוודאות מה תהיה התוצאה של מדידה, רק מה הסיכויים לכל תוצאה.</p>

    <h3>מושג ה'מצב הקוונטי' (פונקציית גל)</h3>
    <p>בפיזיקה הקלאסית, מצב של עצם מוגדר על ידי התכונות המדויקות שלו - מיקום, מהירות וכו'. בפיזיקה הקוונטית, מצב של חלקיק מתואר על ידי 'פונקציית גל' (Ψ). זו לא מפה של מיקום מדויק, אלא מפה של הסתברויות. היא מספרת לנו מה הסיכוי למצוא את החלקיק במקום מסוים או עם תכונה מסוימת (כמו ספין או קיטוב) כאשר נמדוד אותו. לפני המדידה, החלקיק נמצא, באופן מוזר, בכל האפשרויות האלה בו-זמנית - הוא "מרוח" על פני פונקציית הגל.</p>

    <h3>סופרפוזיציה: להיות גם וגם וגם...</h3>
    <p>סופרפוזיציה היא היכולת של חלקיק קוונטי להיות בו-זמנית ביותר ממצב אחד. אלקטרון יכול להיות בו זמנית עם ספין "למעלה" וגם עם ספין "למטה". פוטון יכול להיות גם מקוטב אנכית וגם אופקית. זה לא רק שאנחנו לא יודעים את המצב שלו - הוא *באמת* נמצא בשילוב של כל המצבים האפשריים. הסימולציה הראשונה מאפשרת לכם לשחק עם ההסתברות הזו ולראות איך המדידה "מכריחה" את החלקיק לבחור מצב אחד.</p>
    <p>הדוגמה המפורסמת (והעצובה) היא 'חתול שרדינגר'. בניסוי מחשבתי זה, חתול בקופסה קשור לאטום רדיואקטיבי שעלול לדעוך. אם האטום דועך, רעל משתחרר והחתול מת. עד שפותחים את הקופסה, האטום נמצא בסופרפוזיציה של "דועך" ו"לא דועך". באופן מטריד, לפי הפיזיקה הקוונטית, זה אומר שהחתול עצמו נמצא בסופרפוזיציה של "חי" ו"מת" בו-זמנית!</p>

    <h3>מדידה וקריסת פונקציית הגל</h3>
    <p>הסופרפוזיציה נשמרת כל עוד המערכת הקוונטית מבודדת. אבל ברגע שמבצעים עליה מדידה (או שהיא מבצעת אינטראקציה משמעותית עם סביבתה), הסופרפוזיציה נהרסת. החלקיק "קופץ" למצב אחד מוגדר מבין האפשרויות. תהליך זה נקרא 'קריסת פונקציית הגל'. הסיכוי לקרוס לכל מצב מסוים נקבע על פי ההסתברות שנגזרה מפונקציית הגל המקורית (כמו שהגדרתם בסימולציה הראשונה). לאחר הקריסה, החלקיק נמצא במצב קלאסי וברור.</p>

    <h3>שזירה קוונטית: הקשר המוזר שמתעלם מהמרחק</h3>
    <p>שזירה קוונטית היא תופעה עוד יותר חידתית. שני חלקיקים שזורים מתוארים על ידי פונקציית גל אחת משותפת, כך שמצביהם תלויים זה בזה באופן מיידי. זה כאילו הם מטבעות קוונטיים תאומים - אם אחד נופל על "עץ", השני "חייב" להיות "פלי", גם אם הם בקצוות שונים של הגלקסיה!</p>

    <h3>דוגמאות והמחשה של שזירה</h3>
    <p>דמיינו שתי קוביות משחק קוונטיות ששזורות כך שסכומן תמיד 7. לפני שאתם מטילים קובייה אחת, שתי הקוביות נמצאות בסופרפוזיציה של כל הצירופים האפשריים שסכומם 7 ([1,6], [2,5], [3,4], [4,3], [5,2], [6,1]). ברגע שאתם מטילים את הקובייה הראשונה ומגלים שיצא 3, אתם מיד יודעים שהקובייה השנייה (שנמצאת רחוק) חייבת להיות 4, בלי שתצטרכו למדוד אותה בכלל! הסימולציה השנייה מדגימה זאת עם קיטוב: אם תמדדו את שני החלקיקים באותו כיוון, תמיד תקבלו תוצאות הפוכות (אחד למעלה, השני למטה; אחד אנכי, השני אופקי וכו').</p>

    <h3>תוצאות מדידה על חלקיקים שזורים: עדות למוזרות הקוונטית</h3>
    <p>העניין המרתק והמוזר באמת מתרחש כאשר מודדים את שני החלקיקים השזורים בכיוונים שונים (כמו בסימולציה השנייה כאשר אתם בוחרים זוויות שונות לגלאים). הפיזיקה הקלאסית הייתה מצפה למתאמים חלשים יותר במקרה כזה. אבל הפיזיקה הקוונטית מנבאת (ונ ו וכתה בניסויים) מתאמים חזקים בהרבה מאלה שאפשר להסביר בעזרת תיאוריות קלאסיות שמניחות שהחלקיקים היו בעלי תכונות מוגדרות מראש. הניסויים המפורסמים המבוססים על אי-שוויון בל (Bell's Inequality) הוכיחו זאת מעל לכל ספק. התוצאות מראות שהמציאות ברמה הבסיסית אינה "ריאלית מקומית" - כלומר, אי אפשר לחשוב על תכונות מוגדרות לפני המדידה, ויש סוג של קשר מידי בין חלקיקים שזורים, מה שאלברט איינשטיין כינה בזלזול "פעולה רפאים מרחוק" (spooky action at a distance).</p>

    <h3>יישומים עתידיים של סופרפוזיציה ושזירה: המהפכה הקוונטית</h3>
    <p>התופעות המדהימות האלה אינן רק שעשוע מחשבתי לפיזיקאים. הן הבסיס לטכנולוגיות פורצות דרך שמשנות וצפויות לשנות את העולם שלנו:
    <ul>
        <li><strong>מחשוב קוונטי:</strong> בניית מחשבים קוונטיים חזקים לאין שיעור ממחשבים קלאסיים עבור סוגים מסוימים של חישובים (פתרון בעיות מורכבות, חיפוש מהיר בבסיסי נתונים ענקיים, סימולציות מדעיות).</li>
        <li><strong>קריפטוגרפיה קוונטית:</strong> יצירת שיטות אבטחת מידע בלתי ניתנות לפריצה, שמבוססות על כך שמדידה של מצב קוונטי חושפת את עצמה.</li>
        <li><strong>תקשורת קוונטית:</strong> העברת מידע קוונטי למרחקים, כולל טלפורטציה קוונטית (העברת מצב קוונטי, לא חומר, מרחוק!).</li>
        <li><strong>חיישנים קוונטיים:</strong> פיתוח מכשירי מדידה בעלי רגישות ודיוק חסרי תקדים.</li>
    </ul>
    </p>
    <p>העולם הקוונטי ממשיך לחשוף את סודותיו, וכל תגלית חדשה פותחת דלת לאפשרויות טכנולוגיות ופילוסופיות מרתקות. המסע אל הלא נודע רק החל.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3, h4 {
        color: #2c3e50;
        font-weight: 700;
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
        color: #34495e;
    }

    .interactive-app, .explanation {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        padding: 30px;
        margin-bottom: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }

     .intro-text {
        font-size: 1.1em;
        color: #555;
        margin-bottom: 30px;
        text-align: center;
     }

    .section {
        margin-bottom: 40px;
        padding-bottom: 30px;
        border-bottom: 1px solid #ecf0f1;
    }

    .section:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    .controls {
        background-color: #ecf0f1;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 25px;
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .controls label {
        font-weight: 700;
        color: #34495e;
        display: block;
        margin-bottom: 5px;
    }

    .range-container {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .range-container input[type="range"] {
        flex-grow: 1;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #bdc3c7;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .range-container input[type="range"]:hover {
        opacity: 1;
    }

    .range-container input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #3498db;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .range-container input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #3498db;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .prob-display {
        font-weight: 700;
        color: #3498db;
        min-width: 50px;
        text-align: center;
    }

    .basis-selects {
         display: flex;
         justify-content: space-around;
         gap: 20px;
         margin-bottom: 15px;
    }

    .basis-party {
         flex-basis: 48%; /* Allow some flexibility */
         display: flex;
         flex-direction: column;
         gap: 5px;
    }


    .controls select {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #bdc3c7;
        background-color: #ffffff;
        font-size: 1em;
        color: #555;
        cursor: pointer;
         width: 100%; /* Make selects take full width */
    }

    .action-button {
        padding: 12px 25px;
        font-size: 1em;
        font-weight: 700;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        justify-content: center;
        margin-top: 10px;
    }

    .action-button .icon {
        font-size: 1.2em;
    }

    .action-button:hover {
        transform: translateY(-2px);
    }

    .action-button:active {
        transform: translateY(0);
    }

    .primary {
        background-color: #3498db;
        color: white;
    }

    .primary:hover {
        background-color: #2980b9;
    }

     .secondary {
        background-color: #95a5a6;
        color: white;
    }

    .secondary:hover {
        background-color: #7f8c8d;
    }


    .results {
        background-color: #ecf0f1; /* Match controls background for consistency */
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #bdc3c7;
    }

    .results h4 {
        margin-top: 0;
        color: #34495e;
    }

    .quantum-visual {
        width: 60px;
        height: 60px;
        line-height: 60px;
        text-align: center;
        border: 3px solid #555;
        border-radius: 50%;
        font-size: 2em;
        font-weight: bold;
        margin: 15px auto; /* Center the visual */
        transition: all 0.5s ease; /* Add transition for animations */
         color: #333;
    }

    .quantum-visual.small {
         width: 40px;
         height: 40px;
         line-height: 40px;
         font-size: 1.5em;
         margin: 0 10px; /* Adjust margin for pair display */
         display: inline-block;
         vertical-align: middle;
    }

    /* Initial state - can add pulse animation here */
     .quantum-visual.unknown {
        background-color: #bdc3c7; /* Grey */
        color: #7f8c8d;
        border-color: #7f8c8d;
         animation: pulse-unknown 1.5s infinite ease-in-out;
    }

     @keyframes pulse-unknown {
         0% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.05); opacity: 0.8; }
         100% { transform: scale(1); opacity: 1; }
     }


    /* Superposition States */
    .quantum-visual.up {
        background-color: #2ecc71; /* Green */
        color: white;
        border-color: #2ecc71;
        transform: scale(1.1); /* Animation on collapse */
        opacity: 1;
         animation: none; /* Stop pulsing */
    }

    .quantum-visual.down {
        background-color: #e74c3c; /* Red */
        color: white;
        border-color: #e74c3c;
         transform: scale(1.1); /* Animation on collapse */
        opacity: 1;
         animation: none; /* Stop pulsing */
    }

    /* Entanglement States (using symbols based on basis) */
     /* Vertical/Horizontal (0 or 90 degrees) */
    .quantum-visual.state-V, .quantum-visual.state-H {
         font-size: 1.2em; /* Smaller font for letters */
          animation: none; /* Stop pulsing */
          transform: scale(1.1); /* Animation on collapse */
           opacity: 1;
    }
    .quantum-visual.state-V {
         background-color: #3498db; /* Blue */
         color: white;
         border-color: #3498db;
    }
     .quantum-visual.state-H {
         background-color: #f1c40f; /* Yellow */
         color: #333;
         border-color: #f1c40f;
    }

     /* Diagonal (+ or -) (45 or 135 degrees) */
     .quantum-visual.state-plus, .quantum-visual.state-minus {
         font-size: 1.5em; /* Slightly larger for symbols */
          animation: none; /* Stop pulsing */
           transform: scale(1.1); /* Animation on collapse */
            opacity: 1;
     }
     .quantum-visual.state-plus {
         background-color: #9b59b6; /* Purple */
         color: white;
         border-color: #9b59b6;
     }
      .quantum-visual.state-minus {
         background-color: #1abc9c; /* Teal */
         color: white;
         border-color: #1abc9c;
     }


    .entanglement-pair-results {
         display: flex;
         justify-content: center;
         align-items: center;
         gap: 30px;
         margin-bottom: 20px;
    }

    .entangled-particle {
        text-align: center;
    }

     .entangled-particle p {
         margin-bottom: 5px;
         font-weight: 700;
         color: #555;
     }


    .stats-box {
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px dashed #bdc3c7;
        font-size: 0.95em;
        color: #555;
    }

    .stats-box p {
        margin-bottom: 8px;
         display: flex;
         justify-content: space-between;
    }

    .stats-box span {
        font-weight: 700;
        color: #34495e;
    }


    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        font-weight: 700;
        cursor: pointer;
        border-radius: 6px;
        border: 1px solid #3498db;
        background-color: #e7f3fd;
        color: #3498db;
        transition: background-color 0.3s ease, color 0.3s ease, transform 0.1s ease;
    }

    .toggle-button:hover {
        background-color: #d0eaff;
         transform: translateY(-2px);
    }
    .toggle-button:active {
         transform: translateY(0);
    }


    .explanation {
        line-height: 1.7;
        color: #444;
    }

    .explanation h3 {
        margin-top: 30px;
        margin-bottom: 15px;
        color: #2980b9;
    }

    .explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Adjust for RTL */
        padding-right: 0; /* Ensure no padding on the left */
        margin-top: 15px;
    }
     .explanation li {
         margin-bottom: 10px;
     }

    .hidden {
        display: none;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Superposition Simulation
        const probSlider = document.getElementById('superposition-prob');
        const probDisplay = document.getElementById('prob-display');
        const measureSuperpositionBtn = document.getElementById('measure-superposition');
        const resetSuperpositionBtn = document.getElementById('reset-superposition');
        const superpositionVisualDiv = document.querySelector('#superposition-visual .superposition-state'); // Target the inner state div
        const superpositionCountSpan = document.getElementById('superposition-count');
        const superpositionUpSpan = document.getElementById('superposition-up');
        const superpositionDownSpan = document.getElementById('superposition-down');
        const superpositionUpPercentSpan = document.getElementById('superposition-up-percent');
        const superpositionDownPercentSpan = document.getElementById('superposition-down-percent');

        let totalSuperpositionMeasures = 0;
        let upCounts = 0;
        let downCounts = 0;

        // Initial display update
        probDisplay.textContent = `${probSlider.value}%`;
        superpositionVisualDiv.textContent = '?';
        superpositionVisualDiv.className = 'superposition-state unknown';


        probSlider.addEventListener('input', () => {
            probDisplay.textContent = `${probSlider.value}%`;
        });

        measureSuperpositionBtn.addEventListener('click', () => {
            const probUp = parseInt(probSlider.value) / 100;
            const random = Math.random();
            let resultText;
            let resultClass;

            // Reset animation classes and state
            superpositionVisualDiv.className = 'superposition-state unknown';
             superpositionVisualDiv.textContent = '?'; // Show uncertainty briefly before collapse

            // Simulate the collapse after a brief delay to show the 'unknown' state
            setTimeout(() => {
                if (random < probUp) {
                    resultText = '↑';
                    resultClass = 'up';
                    upCounts++;
                } else {
                    resultText = '↓';
                    resultClass = 'down';
                    downCounts++;
                }

                superpositionVisualDiv.textContent = resultText;
                // Add the result class to trigger the final state appearance/animation
                superpositionVisualDiv.className = `superposition-state ${resultClass}`;


                totalSuperpositionMeasures++;
                superpositionCountSpan.textContent = totalSuperpositionMeasures;
                superpositionUpSpan.textContent = upCounts;
                superpositionDownSpan.textContent = downCounts;
                superpositionUpPercentSpan.textContent = totalSuperpositionMeasures > 0 ? ((upCounts / totalSuperpositionMeasures) * 100).toFixed(1) + '%' : '0%';
                superpositionDownPercentSpan.textContent = totalSuperpositionMeasures > 0 ? ((downCounts / totalSuperpositionMeasures) * 100).toFixed(1) + '%' : '0%';

            }, 200); // Small delay to show the "?" state

        });

        resetSuperpositionBtn.addEventListener('click', () => {
            totalSuperpositionMeasures = 0;
            upCounts = 0;
            downCounts = 0;
            superpositionCountSpan.textContent = 0;
            superpositionUpSpan.textContent = 0;
            superpositionDownSpan.textContent = 0;
            superpositionUpPercentSpan.textContent = '0%';
            superpositionDownPercentSpan.textContent = '0%';
            superpositionVisualDiv.textContent = '?';
            superpositionVisualDiv.className = 'superposition-state unknown'; // Reset visual
        });


        // Entanglement Simulation
        const basisASelect = document.getElementById('entanglement-basis-a');
        const basisBSelect = document.getElementById('entanglement-basis-b');
        const measureEntangledBtn = document.getElementById('measure-entangled-pair');
        const resetEntanglementBtn = document.getElementById('reset-entanglement');
        const entanglementCountSpan = document.getElementById('entanglement-count');
        const sameResultsSpan = document.getElementById('same-results');
        const differentResultsSpan = document.getElementById('different-results');
        const sameResultsPercentSpan = document.getElementById('same-results-percent');
        const differentResultsPercentSpan = document.getElementById('different-results-percent');
        const lastBasisASpan = document.getElementById('last-basis-a');
        const lastBasisBSpan = document.getElementById('last-basis-b');
        const lastResultAVisual = document.getElementById('last-result-a'); // Target the visual div
        const lastResultBVisual = document.getElementById('last-result-b'); // Target the visual div


        let totalEntanglementMeasures = 0;
        let sameResultsCount = 0;
        let differentResultsCount = 0;
        let currentMeasuredBasisA = null;
        let currentMeasuredBasisB = null;

        // Function to simulate entangled pair measurement for a Bell state like |psi-> (polarization example)
        // This simulation assumes a state like |psi-> = (|01> - |10>) / sqrt(2), where 0 and 1 are orthogonal outcomes in any basis.
        // For this state, if bases are the same, results are always opposite. If bases differ by 90 deg, results are always the same.
        // Probability of getting the *same* raw outcome (0,0 or 1,1) is sin^2(angle_diff), Different is cos^2(angle_diff).
        // However, in many practical entangled sources, the state is (|00> + |11>) / sqrt(2) or similar, where same bases give same results.
        // Let's adjust the simulation to match common experiments where same basis -> same result for simplicity, e.g., |phi+> state.
        // For |phi+>: P(Same Outcome | B_A, B_B) = cos^2(angle_diff), P(Different Outcome | B_A, B_B) = sin^2(angle_diff).

        function simulateEntangledMeasurement(basisA_deg, basisB_deg) {
             // Map raw 0/1 result back to a readable symbol/string based on the basis
             const mapResultToSymbol = (result, basis_deg) => {
                if (basis_deg === 0) return result === 0 ? { text: 'V', class: 'state-V' } : { text: 'H', class: 'state-H' }; // Vertical/Horizontal
                if (basis_deg === 90) return result === 0 ? { text: 'V', class: 'state-V' } : { text: 'H', class: 'state-H' }; // Same as 0 for this type of state correlation
                if (basis_deg === 45) return result === 0 ? { text: '+', class: 'state-plus' } : { text: '-', class: 'state-minus' }; // Diagonal +/-
                if (basis_deg === 135) return result === 0 ? { text: '+', class: 'state-plus' } : { text: '-', class: 'state-minus' }; // Same as 45 for correlation pattern
                return { text: '?', class: 'unknown' };
             };

            let rawResultA, rawResultB; // 0 or 1 representing two orthogonal outcomes

            // Simulate first particle's outcome based on its basis (50/50 chance in any basis)
            rawResultA = Math.random() < 0.5 ? 0 : 1;

            // Determine the second particle's raw 0/1 outcome based on the first's and the angle difference
            const angleDiff_rad = Math.abs(basisA_deg - basisB_deg) * Math.PI / 180;
            // Probability of getting the *same* raw outcome (0,0 or 1,1) for |phi+> state is cos^2(angle_diff)
            const probSameRawOutcome = Math.cos(angleDiff_rad) ** 2;

            const shouldBeSameRaw = Math.random() < probSameRawOutcome;

            if (shouldBeSameRaw) {
                rawResultB = rawResultA;
            } else {
                rawResultB = 1 - rawResultA; // Different outcome
            }

            const resultA = mapResultToSymbol(rawResultA, basisA_deg);
            const resultB = mapResultToSymbol(rawResultB, basisB_deg);

             // Determine if the *symbols* are the same, which depends on the basis mapping.
             // For 0/90 and 45/135, our mapping is consistent.
             // Same outcomes mean V/V, H/H, +/+, -/-
             // Different outcomes mean V/H, H/V, +/- , -/+
             const areSameSymbols = resultA.text === resultB.text;


            return {
                resultA_text: resultA.text,
                resultA_class: resultA.class,
                resultB_text: resultB.text,
                resultB_class: resultB.class,
                areSameSymbols: areSameSymbols // Use this for correlation stats
            };
        }

        // Initial state for entanglement results
        lastBasisASpan.textContent = '?°';
        lastBasisBSpan.textContent = '?°';
        lastResultAVisual.textContent = '?';
        lastResultBVisual.textContent = '?';
        lastResultAVisual.className = 'quantum-visual small unknown';
        lastResultBVisual.className = 'quantum-visual small unknown';


        measureEntangledBtn.addEventListener('click', () => {
            const basisA = parseInt(basisASelect.value);
            const basisB = parseInt(basisBSelect.value);

            // If basis changes, reset counts
            if (basisA !== currentMeasuredBasisA || basisB !== currentMeasuredBasisB) {
                 totalEntanglementMeasures = 0;
                 sameResultsCount = 0;
                 differentResultsCount = 0;
                 currentMeasuredBasisA = basisA;
                 currentMeasuredBasisB = basisB;
                 entanglementCountSpan.textContent = 0; // Update displayed count immediately
                 sameResultsSpan.textContent = 0;
                 differentResultsSpan.textContent = 0;
                 sameResultsPercentSpan.textContent = '0%';
                 differentResultsPercentSpan.textContent = '0%';

                 // Reset last pair visual
                 lastResultAVisual.className = 'quantum-visual small unknown';
                 lastResultBVisual.className = 'quantum-visual small unknown';
                 lastResultAVisual.textContent = '?';
                 lastResultBVisual.textContent = '?';
                 lastBasisASpan.textContent = '?°';
                 lastBasisBSpan.textContent = '?°';
            }


            const numTrials = 100; // As specified in the prompt concept
            let tempSameCount = sameResultsCount;
            let tempDifferentCount = differentResultsCount;
            let tempTotalCount = totalEntanglementMeasures;

            // Reset last pair visual state before running new trials
            lastResultAVisual.className = 'quantum-visual small unknown';
            lastResultBVisual.className = 'quantum-visual small unknown';
            lastResultAVisual.textContent = '?';
            lastResultBVisual.textContent = '?';

            // Simulate trials - run the loop but update display only at the end
            for (let i = 0; i < numTrials; i++) {
                const measurement = simulateEntangledMeasurement(basisA, basisB);

                tempTotalCount++;
                if (measurement.areSameSymbols) {
                    tempSameCount++;
                } else {
                    tempDifferentCount++;
                }

                 // Store results of the *last* pair for display after the loop
                if (i === numTrials - 1) {
                     lastBasisASpan.textContent = `${basisA}°`;
                     lastBasisBSpan.textContent = `${basisB}°`;
                     // Will update textContent and class after the loop for animation
                }
            }

             // Update state variables after the loop
            totalEntanglementMeasures = tempTotalCount;
            sameResultsCount = tempSameCount;
            differentResultsCount = tempDifferentCount;


            // Animate the final last pair results appearing
            setTimeout(() => {
                 const lastMeasurement = simulateEntangledMeasurement(basisA, basisB); // Re-run for the last pair for display
                 lastResultAVisual.textContent = lastMeasurement.resultA_text;
                 lastResultBVisual.textContent = lastMeasurement.resultB_text;
                 lastResultAVisual.className = `quantum-visual small ${lastMeasurement.resultA_class}`;
                 lastResultBVisual.className = `quantum-visual small ${lastMeasurement.resultB_class}`;
            }, 200); // Small delay before showing final pair

            // Update stats display
            entanglementCountSpan.textContent = totalEntanglementMeasures;
            sameResultsSpan.textContent = sameResultsCount;
            differentResultsSpan.textContent = differentResultsCount;
            sameResultsPercentSpan.textContent = totalEntanglementMeasures > 0 ? ((sameResultsCount / totalEntanglementMeasures) * 100).toFixed(1) + '%' : '0%';
            differentResultsPercentSpan.textContent = totalEntanglementMeasures > 0 ? ((differentResultsCount / totalEntanglementMeasures) * 100).toFixed(1) + '%' : '0%';
        });

        resetEntanglementBtn.addEventListener('click', () => {
            totalEntanglementMeasures = 0;
            sameResultsCount = 0;
            differentResultsCount = 0;
            currentMeasuredBasisA = null;
            currentMeasuredBasisB = null;

            entanglementCountSpan.textContent = 0;
            sameResultsSpan.textContent = 0;
            differentResultsSpan.textContent = 0;
            sameResultsPercentSpan.textContent = '0%';
            differentResultsPercentSpan.textContent = '0%';

            // Reset last pair visual
            lastBasisASpan.textContent = '?°';
            lastBasisBSpan.textContent = '?°';
            lastResultAVisual.textContent = '?';
            lastResultBVisual.textContent = '?';
            lastResultAVisual.className = 'quantum-visual small unknown';
            lastResultBVisual.className = 'quantum-visual small unknown';
        });


        // Explanation Toggle
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.classList.toggle('hidden');
            if (isHidden) {
                toggleButton.textContent = 'הצג הסבר מפורט';
            } else {
                toggleButton.textContent = 'הסתר הסבר מפורט';
            }
        });

        // Initial state of explanation
        explanationDiv.classList.add('hidden'); // Ensure it's hidden on load
        toggleButton.textContent = 'הצג הסבר מפורט'; // Set initial button text
    });
</script>
```