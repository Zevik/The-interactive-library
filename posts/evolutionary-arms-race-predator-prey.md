---
title: "מירוץ חימוש אבולוציוני: קרב ההישרדות בין טורף לנטרף"
english_slug: evolutionary-arms-race-predator-prey
category: "ביולוגיה"
tags:
  - אבולוציה
  - אקולוגיה
  - ברירה טבעית
  - קו-אבולוציה
  - טורף-נטרף
---
# מירוץ חימוש אבולוציוני: קרב ההישרדות בין טורף לנטרף
כיצד פיתחו הצבועים לסתות כה חזקות והקיפודים קוצים חדים? האם ההתאמות הללו הן תגובה הדדית בלתי פוסקת? צללו לסימולציה מרתקת וגלו כיצד המאבק הבלתי פוסק על ההישרדות בין טורפים לנטרפים מעצב את תהליך האבולוציה בשני הצדדים, במירוץ חימוש עוצר נשימה.

<div class="simulation-container">
    <div class="simulation-header">
        <h2>סימולציית מירוץ החימוש האבולוציוני</h2>
        <p class="subtitle">ראו כיצד התאמות מתפתחות לאורך דורות</p>
    </div>

    <div class="sim-layout">
        <div class="controls panel">
            <h3>הגדרות התחלתיות</h3>
            <div class="control-group">
                <label for="initialPreyPop">גודל אוכלוסיית נטרפים:</label>
                <input type="number" id="initialPreyPop" value="500" min="10" step="50">
                <span class="control-hint">כמה נטרפים מתחילים?</span>
            </div>
            <div class="control-group">
                <label for="initialPredatorPop">גודל אוכלוסיית טורפים:</label>
                <input type="number" id="initialPredatorPop" value="50" min="5" step="10">
                <span class="control-hint">כמה טורפים מתחילים?</span>
            </div>
            <div class="control-group">
                <label for="initialPreySpeed">זריזות התחלתית (נטרף):</label>
                <input type="range" id="initialPreySpeed" value="10" min="1" max="20" step="0.5">
                <span class="range-value" id="initialPreySpeedValue">10.0</span>
                <span class="control-hint">יכולת בריחה והתחמקות.</span>
            </div>
            <div class="control-group">
                <label for="initialPreyDefense">הגנה התחלתית (נטרף):</label>
                <input type="range" id="initialPreyDefense" value="10" min="1" max="20" step="0.5">
                 <span class="range-value" id="initialPreyDefenseValue">10.0</span>
                <span class="control-hint">יכולת הגנה פיזית או רעל.</span>
            </div>
            <div class="control-group">
                <label for="initialPredatorSpeed">מהירות התחלתית (טורף):</label>
                <input type="range" id="initialPredatorSpeed" value="10" min="1" max="20" step="0.5">
                 <span class="range-value" id="initialPredatorSpeedValue">10.0</span>
                <span class="control-hint">מהירות מרדף.</span>
            </div>
             <div class="control-group">
                <label for="initialPredatorAttack">עוצמת התקפה (טורף):</label>
                <input type="range" id="initialPredatorAttack" value="10" min="1" max="20" step="0.5">
                 <span class="range-value" id="initialPredatorAttackValue">10.0</span>
                <span class="control-hint">יכולת הכנעה וצייד.</span>
            </div>
            <div class="button-group">
                 <button id="startSimBtn">התחל את המירוץ!</button>
            </div>
        </div>

        <div class="results panel">
            <h3>תוצאות דור נוכחי</h3>
             <p id="generation"><span class="label">דור:</span> <span class="value">0</span></p>
            <p id="preyPop"><span class="label">אוכלוסיית נטרפים:</span> <span class="value">0</span> <span class="pop-indicator prey"></span></p>
            <p id="predatorPop"><span class="label">אוכלוסיית טורפים:</span> <span class="value">0</span> <span class="pop-indicator predator"></span></p>
            <div class="trait-results">
                 <h4>התאמות ממוצעות:</h4>
                <p id="avgPreySpeed"><span class="label">זריזות (נטרף):</span> <span class="value trait-value">0.00</span> <span class="trait-arrow"></span></p>
                <p id="avgPreyDefense"><span class="label">הגנה (נטרף):</span> <span class="value trait-value">0.00</span> <span class="trait-arrow"></span></p>
                <p id="avgPredatorSpeed"><span class="label">מהירות (טורף):</span> <span class="value trait-value">0.00</span> <span class="trait-arrow"></span></p>
                <p id="avgPredatorAttack"><span class="label">התקפה (טורף):</span> <span class="value trait-value">0.00</span> <span class="trait-arrow"></span></p>
            </div>
            <p id="preyEaten"><span class="label">נטרפים נאכלו בדור הקודם:</span> <span class="value">0</span></p>
            <div class="button-group">
                 <button id="nextGenBtn" disabled>הרץ דור הבא</button>
                 <button id="runAutoBtn" disabled>הרץ אוטומטית (100 דורות)</button>
                 <button id="stopAutoBtn" style="display: none;">עצור ריצה</button>
            </div>
             <div id="extinctionMessage" class="message" style="display: none;">סימולציה הסתיימה: אחת האוכלוסיות נכחדה. התחילו מירוץ חדש!</div>
             <div id="stableMessage" class="message" style="display: none;">האוכלוסיות נראות יציבות. מעניין מה יקרה בעוד דורות?</div>
        </div>
    </div>

    <div class="chart-container">
         <!-- Placeholder for a simple chart/visualization if implemented -->
         <p>כאן יוצגו נתונים ויזואליים לאורך דורות (בגרסה עתידית).</p>
    </div>
</div>

<button id="showExplanationBtn" class="toggle-explanation-btn">הצג הסבר על מירוץ חימוש אבולוציוני</button>

<div id="explanation" class="explanation-container" style="display: none;">
    <h2>הסבר: מירוץ חימוש אבולוציוני</h2>

    <div class="explanation-section">
        <h3>יחסי טורף-נטרף בטבע - קרב ההישרדות היומיומי</h3>
        <p>יחסי טורף-נטרף הם אחת האינטראקציות האקולוגיות הדינמיות והמשפיעות ביותר בטבע. הטורפים תלויים בנטרפים כמקור אנרגיה חיוני, בעוד שהנטרפים מקדישים מאמצים עצומים כדי לחמוק מגורל אכזר. המאבק המתמיד הזה יוצר לחץ ברירתי עצום שמעצב את האבולוציה של שתי האוכלוסיות במקביל.</p>
    </div>

     <div class="explanation-section">
        <h3>ברירה טבעית בפעולה: מנוע השינוי</h3>
        <p>ברירה טבעית היא המנגנון האלגנטי והעוצמתי שמוביל את האבולוציה. היא פועלת בשלושה שלבים פשוטים אך גורליים:</p>
        <ul>
            <li>**שונות:** אף פריט אינו זהה לחלוטין. קיימים הבדלים קטנים אך משמעותיים בתכונות (פיזיות, התנהגותיות) בין פרטים באוכלוסייה.</li>
            <li>**תורשה:** חלק מהשונות המגוונת הזו מועבר מהורים לצאצאים באמצעות גנים.</li>
            <li>**התאמה והישרדות:** בסביבה נתונה, תכונות מסוימות מקנות לפרט סיכויים טובים יותר לשרוד, למצוא מזון, לחמוק מאויבים ולהתרבות. פרטים עם תכונות "מותאמות" יותר משאירים אחריהם יותר צאצאים, שנושאים גם הם את התכונות הללו.</li>
        </ul>
        <p>וכך, מדור לדור, התכונות המותאמות לסביבה הופכות נפוצות יותר באוכלוסייה, ומתרחש שינוי אבולוציוני.</p>
    </div>

    <div class="explanation-section">
        <h3>התאמות טורפים: אמנות הציד</h3>
        <p>טורפים מפתחים שלל אסטרטגיות ותכונות כדי לשפר את יכולתם לאתר, לרדוף, ולגבור על הטרף שלהם:</p>
        <ul>
            <li>**מהירות, כוח וזריזות:** כמו הברדלס המהיר ביותר או האריה האדיר.</li>
            <li>**חושים מחודדים:** ראיית לילה של ינשופים, חוש הריח המדהים של זאבים, השמיעה הרגישה של עטלפים.</li>
            <li>**כלי צייד קטלניים:** טפרים חדים, שיניים מחודדות, ארס משתק, רשתות דביקות.</li>
            <li>**הסוואה ותחבולה:** התמזגות עם הסביבה (דוב קוטב בשלג) או שימוש בפיתוי (דג החכאי).</li>
            <li>**שיתוף פעולה:** ציד בלהקות או עדרים (זאבים, לווייתנים קטלנים) להכנעת טרף גדול יותר.</li>
        </ul>
    </div>

    <div class="explanation-section">
        <h3>התאמות נטרפים: אסטרטגיות הישרדות נועזות</h3>
        <p>מנגד, הנטרפים אינם חסרי אונים כלל. הם מפתחים טקטיקות והתאמות מתוחכמות כדי להימנע מלהפוך לארוחה:</p>
        <ul>
            <li>**מהירות בריחה וסיבולת:** כמו הצבי הבורח מהטורף או האנטילופה הרצה למרחקים ארוכים.</li>
            <li>**הסוואה מושלמת:** התמזגות מופלאה עם הרקע (זיקיות, חרקי מקל, דגים מסוימים).</li>
            <li>**חיקוי (מימיקרי) והרתעה:** חיקוי מראה של מין מסוכן או רעיל כדי להבריח טורפים, או הצגת צבעי אזהרה בולטים (פרפרים, דו-חיים).</li>
            <li>**מנגנוני הגנה פיזיים/כימיים:** קוצים (קיפוד), שריון (צב), רעלים קטלניים בעור או בבלוטות (צפרדעים מסוימות, מיני חרקים).</li>
            <li>**עירנות וחיים בקבוצה:** עיניים רבות רואות יותר (עדרים, להקות), והסיכוי של פרט בודד להיטרף נמוך יותר בקבוצה גדולה (אפקט "עדר הביטחון").</li>
        </ul>
    </div>

    <div class="explanation-section">
        <h3>קו-אבולוציה: ריקוד הדדי של שינוי</h3>
        <p>קו-אבולוציה היא תופעה מרתקת שבה שני מינים או יותר משפיעים הדדית, כמו בריקוד, על מסלול האבולוציה זה של זה. כשתכונה חדשה מתפתחת במין אחד (למשל, טורף מהיר יותר), היא מפעילה לחץ ברירתי חזק על המין השני (הנטרף), וגורמת לפרטים המותאמים יותר (המהירים יותר) לשרוד ולהתרבות. בתגובה, גם הטורף יעבור ברירה, ורק המהירים ביותר יצליחו לתפוס את הטרף המהיר יותר. כך נוצר מעגל אינסופי לכאורה של התאמות והתאמות-נגד.</p>
    </div>

    <div class="explanation-section">
        <h3>מירוץ חימוש אבולוציוני: כמו המלכה האדומה</h3>
        <p>מירוץ חימוש אבולוציוני הוא דוגמה קיצונית לקו-אבולוציה, לרוב בין טורף לנטרף, או טפיל למאכסן. הוא מתרחש כאשר כל צד מפתח כל הזמן התאמות משופרות בתגובה ישירה לאבולוציה של הצד השני. זהו מאבק אבולוציוני תמידי שבו אין מנצח מוחלט לאורך זמן - יתרון זמני נמחק במהירות על ידי התפתחות של הצד השני. הקונספט הזה מתואר לעיתים קרובות על ידי "השערת המלכה האדומה", בהשראת דמות מספרו של לואיס קרול, שאומרת: "עליך לרוץ הכי מהר שאתה יכול, רק כדי להישאר באותו מקום". בהקשר האבולוציוני, מינים חייבים להמשיך ולהתפתח רק כדי לשרוד בסביבה שבה "אויביהם" (טורפים, טפילים, וכו') מתפתחים גם הם.</p>
    </div>

     <div class="explanation-section">
        <h3>דוגמאות מהטבע: לא רק בספרים</h3>
        <ul>
            <li>**סלמנדרות ונחשי בירית:** סלמנדרות מייצרות רעל קטלני, ונחשים פיתחו עמידות אליו. ככל שהסלמנדרה רעילה יותר, הנחש צריך להיות עמיד יותר - וזהו מירוץ מתמשך בין עוצמת הרעל לעמידות.</li>
            <li>**צ'יטות וצבאים:** המרדף הקלאסי הוא דוגמה למירוץ חימוש על מהירות וזריזות. רק הצ'יטות המהירות ביותר מצליחות לצוד, ורק הצבאים המהירים ביותר מצליחים לברוח.</li>
            <li>**עשים ועטלפים:** עטלפים פיתחו מערכת אקולוקציה (סונאר) מתוחכמת לאיתור טרף בלילה. עשים רבים, בתגובה, פיתחו יכולת שמיעה לקלוט את צלילי העטלפים ולהתחמק, וחלקם אף פיתחו יכולת "לשדר" צלילים משלהם כדי לשבש את הסונאר של העטלף!</li>
        </ul>
    </div>

     <div class="explanation-section">
        <h3>חשיבות מירוצי החימוש: מגוון חיים ותמורות</h3>
        <p>מירוצי חימוש אבולוציוניים הם כוח מרכזי מאחורי יצירת המגוון הביולוגי העשיר שאנו רואים סביבנו. הם דוחפים את האבולוציה ליצירת תכונות חדשות ומורכבות, ושומרים על שונות גנטית באוכלוסיות. הם תזכורת לכך שהחיים על פני כדור הארץ אינם סטטיים, אלא נמצאים בתנועה מתמדת, במירוץ אינסופי של התאמה והתמודדות.</p>
    </div>
</div>

<style>
    :root {
        --primary-color: #4CAF50; /* Green */
        --secondary-color: #FF9800; /* Orange */
        --bg-color: #f4f7f6; /* Light Grey-Blue */
        --panel-bg: #ffffff; /* White */
        --border-color: #e0e0e0; /* Light Grey */
        --text-color: #333; /* Dark Grey */
        --highlight-color: #2196F3; /* Blue */
        --prey-color: #4CAF50; /* Green */
        --predator-color: #F44336; /* Red */
        --extinction-color: #f44336;
        --stable-color: #2196F3;
    }

    body {
         font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--bg-color);
        margin: 0;
        padding: 20px;
    }

     h1, h2, h3, h4 {
        color: #333;
        margin-top: 0;
    }

    .simulation-container {
        max-width: 1000px;
        margin: 20px auto;
        padding: 30px;
        background-color: var(--panel-bg);
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        border: 1px solid var(--border-color);
    }

     .simulation-header {
        text-align: center;
        margin-bottom: 30px;
    }

     .simulation-header h2 {
        color: var(--primary-color);
        font-size: 2em;
        margin-bottom: 5px;
     }

     .simulation-header .subtitle {
         font-size: 1.1em;
         color: #555;
         margin-top: 0;
     }


    .sim-layout {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
    }

    .panel {
        flex: 1;
        min-width: 300px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #fcfcfc;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

     .panel h3 {
        margin-bottom: 20px;
        color: var(--highlight-color);
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 10px;
     }

     .controls .control-group {
        margin-bottom: 15px;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 10px;
     }

    .controls label {
        flex: 1 1 180px; /* Flex-grow, Flex-shrink, Basis */
        font-weight: bold;
        color: #555;
    }

    .controls input[type="number"] {
        flex: 0 0 80px;
        padding: 8px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        font-size: 1em;
        text-align: center;
    }

    .controls input[type="range"] {
        flex: 1 1 150px;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: var(--border-color);
        outline: none;
        opacity: 0.7;
        -webkit-transition: .2s;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--panel-bg);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--panel-bg);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

     .controls .range-value {
         flex: 0 0 40px;
         text-align: right;
         font-weight: bold;
         color: var(--text-color);
     }

     .control-hint {
        flex: 1 1 100%; /* Takes full width on smaller screens */
        font-size: 0.9em;
        color: #777;
        margin-top: -5px;
        margin-left: calc(180px + 10px); /* Align hint below label/input */
        padding-right: calc(40px + 10px); /* Align with range value */
     }
      .controls .control-group:last-of-type {
          margin-bottom: 25px;
      }


    .button-group {
        margin-top: 25px;
        text-align: center;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
    }

    button {
        padding: 12px 20px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    button:hover:not(:disabled) {
        background-color: #45a049;
        transform: translateY(-1px);
    }

     button:active:not(:disabled) {
         transform: translateY(0);
     }

     button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
     }

    #startSimBtn {
        background-color: var(--highlight-color);
    }
     #startSimBtn:hover:not(:disabled) {
         background-color: #1e88e5;
     }

    #runAutoBtn {
        background-color: var(--secondary-color);
    }
     #runAutoBtn:hover:not(:disabled) {
        background-color: #fb8c00;
     }
     #stopAutoBtn {
         background-color: var(--predator-color);
     }
     #stopAutoBtn:hover:not(:disabled) {
         background-color: #e53935;
     }


    .results p {
        margin-bottom: 10px;
        font-size: 1.1em;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 5px 0;
        border-bottom: 1px dashed #eee;
    }

     .results p:last-child {
         border-bottom: none;
         margin-bottom: 0;
     }

     .results .label {
         font-weight: bold;
         color: #555;
         flex-basis: 60%; /* Give labels more space */
     }
      .results .value {
          flex-basis: 40%; /* Give values less space */
          text-align: left;
          font-weight: normal;
      }

    .results .trait-results {
         margin-top: 15px;
         padding-top: 15px;
         border-top: 1px solid var(--border-color);
    }

     .results .trait-results h4 {
         margin-bottom: 10px;
         color: #555;
         font-size: 1.05em;
     }

     .results p .trait-value {
         min-width: 50px; /* Ensure space for the number */
     }

     .trait-arrow {
         display: inline-block;
         width: 1em;
         text-align: center;
         font-weight: bold;
         margin-left: 5px;
         animation: fade-in 0.5s ease-out;
     }

     .trait-arrow.up { color: var(--primary-color); } /* Green for increase */
     .trait-arrow.down { color: var(--predator-color); } /* Red for decrease */
     .trait-arrow.neutral { color: #777; } /* Grey for no change */


     .pop-indicator {
         display: inline-block;
         width: 15px;
         height: 15px;
         border-radius: 50%;
         margin-left: 8px;
         opacity: 0.8;
         animation: pulse 1.5s infinite ease-in-out;
     }
    .pop-indicator.prey { background-color: var(--prey-color); }
    .pop-indicator.predator { background-color: var(--predator-color); }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }

    @keyframes fade-in {
        from { opacity: 0; }
        to { opacity: 1; }
    }


    .chart-container {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #fcfcfc;
        text-align: center;
        min-height: 100px; /* Placeholder */
        color: #777;
        font-style: italic;
    }

    .toggle-explanation-btn {
         display: block;
         width: fit-content;
         margin: 30px auto 20px auto;
         background-color: #607D8B; /* Blue Grey */
         color: white;
         padding: 12px 25px;
         font-size: 1.1em;
         border-radius: 6px;
         border: none;
         cursor: pointer;
         transition: background-color 0.3s ease;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .toggle-explanation-btn:hover {
         background-color: #546E7A;
    }


    .explanation-container {
        margin: 20px auto;
        max-width: 1000px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--panel-bg);
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
    }

    .explanation-container h2 {
        color: var(--primary-color);
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 15px;
        margin-bottom: 25px;
        text-align: center;
    }

     .explanation-section {
         margin-bottom: 30px;
         padding-bottom: 20px;
         border-bottom: 1px dashed #eee;
     }
      .explanation-section:last-child {
          border-bottom: none;
          margin-bottom: 0;
          padding-bottom: 0;
      }


    .explanation-container h3 {
        color: var(--highlight-color);
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.3em;
    }

     .explanation-container h4 {
         color: #555;
         margin-top: 15px;
         margin-bottom: 10px;
         font-size: 1.1em;
     }

    .explanation-container p {
        line-height: 1.7;
        margin-bottom: 15px;
         color: #444;
    }

     .explanation-container ul {
        margin-bottom: 15px;
        padding-left: 25px;
        list-style-type: disc;
     }

     .explanation-container li {
         margin-bottom: 8px;
         line-height: 1.5;
         color: #444;
     }

     .message {
         margin-top: 20px;
         padding: 15px;
         border-radius: 8px;
         font-weight: bold;
         text-align: center;
         font-size: 1.1em;
         animation: fade-in 0.8s ease-out;
     }
      #extinctionMessage {
          background-color: #ffebee; /* Light Red */
          color: var(--extinction-color);
          border: 1px solid var(--extinction-color);
      }
      #stableMessage {
          background-color: #e3f2fd; /* Light Blue */
          color: var(--stable-color);
           border: 1px solid var(--stable-color);
      }

     @media (max-width: 768px) {
         .sim-layout {
             flex-direction: column;
         }
          .controls .control-group {
             flex-direction: column;
             align-items: flex-start;
         }
          .controls label, .controls input[type="number"], .controls input[type="range"], .controls .range-value, .control-hint {
              flex-basis: auto;
              width: 100%;
               margin-left: 0;
          }
           .controls .control-group input[type="range"] {
               margin-top: 5px;
           }
           .controls .range-value {
                text-align: left;
                margin-top: -10px; /* Adjust spacing */
           }
            .control-hint {
                margin-top: 0;
                font-size: 0.85em;
            }
     }
</style>

<script>
    let generation = 0;
    let currentPreyPop = 0;
    let currentPredatorPop = 0;
    let avgPreySpeed = 0;
    let avgPreyDefense = 0;
    let avgPredatorSpeed = 0;
    let avgPredatorAttack = 0;
    let preyEatenLastGen = 0;

    // Store previous traits to show change
    let prevAvgPreySpeed = 0;
    let prevAvgPreyDefense = 0;
    let prevAvgPredatorSpeed = 0;
    let prevAvgPredatorAttack = 0;

    let simulationRunning = false; // Flag to prevent multiple simulations
    let autoRunInterval = null; // To store the interval ID for auto run
    const autoRunGenerations = 100; // Number of generations for auto run

    // Simulation parameters
    const preyBaseBirthRate = 0.1; // Proportion added per generation
    const preyBaseDeathRate = 0.02; // Proportion dying regardless of predation
    const predatorBaseDeathRate = 0.08; // Proportion dying if no food
    const predatorReproductionRatePerKill = 0.01; // Predators gain this much "reproduction potential" per prey kill
    const evolutionRate = 0.04; // How quickly traits change in response to selection pressure
    const mutationMagnitude = 0.05; // Magnitude of random trait change
    const minTrait = 1; // Minimum trait value

    // UI elements
    const initialPreyPopInput = document.getElementById('initialPreyPop');
    const initialPredatorPopInput = document.getElementById('initialPredatorPop');
    const initialPreySpeedInput = document.getElementById('initialPreySpeed');
    const initialPreyDefenseInput = document.getElementById('initialPreyDefense');
    const initialPredatorSpeedInput = document.getElementById('initialPredatorSpeed');
    const initialPredatorAttackInput = document.getElementById('initialPredatorAttack');

    const initialPreySpeedValueSpan = document.getElementById('initialPreySpeedValue');
    const initialPreyDefenseValueSpan = document.getElementById('initialPreyDefenseValue');
    const initialPredatorSpeedValueSpan = document.getElementById('initialPredatorSpeedValue');
    const initialPredatorAttackValueSpan = document.getElementById('initialPredatorAttackValue');

    const startSimBtn = document.getElementById('startSimBtn');
    const nextGenBtn = document.getElementById('nextGenBtn');
    const runAutoBtn = document.getElementById('runAutoBtn');
    const stopAutoBtn = document.getElementById('stopAutoBtn');
    const showExplanationBtn = document.getElementById('showExplanationBtn');
    const explanationDiv = document.getElementById('explanation');

    const generationText = document.getElementById('generation').querySelector('.value');
    const preyPopText = document.getElementById('preyPop').querySelector('.value');
    const predatorPopText = document.getElementById('predatorPop').querySelector('.value');
    const avgPreySpeedText = document.getElementById('avgPreySpeed').querySelector('.trait-value');
    const avgPreyDefenseText = document.getElementById('avgPreyDefense').querySelector('.trait-value');
    const avgPredatorSpeedText = document.getElementById('avgPredatorSpeed').querySelector('.trait-value');
    const avgPredatorAttackText = document.getElementById('avgPredatorAttack').querySelector('.trait-value');
     const preyEatenText = document.getElementById('preyEaten').querySelector('.value');

     const preyPopIndicator = document.getElementById('preyPop').querySelector('.pop-indicator');
     const predatorPopIndicator = document.getElementById('predatorPop').querySelector('.pop-indicator');

    const avgPreySpeedArrow = document.getElementById('avgPreySpeed').querySelector('.trait-arrow');
    const avgPreyDefenseArrow = document.getElementById('avgPreyDefense').querySelector('.trait-arrow');
    const avgPredatorSpeedArrow = document.getElementById('avgPredatorSpeed').querySelector('.trait-arrow');
    const avgPredatorAttackArrow = document.getElementById('avgPredatorAttack').querySelector('.trait-arrow');

    const extinctionMessage = document.getElementById('extinctionMessage');
    const stableMessage = document.getElementById('stableMessage');


    // Event Listeners
    startSimBtn.addEventListener('click', initializeSimulation);
    nextGenBtn.addEventListener('click', simulateGeneration);
    runAutoBtn.addEventListener('click', startAutoRun);
    stopAutoBtn.addEventListener('click', stopAutoRun);
    showExplanationBtn.addEventListener('click', toggleExplanation);

    // Add listeners for range inputs to update spans
    initialPreySpeedInput.addEventListener('input', () => { initialPreySpeedValueSpan.textContent = parseFloat(initialPreySpeedInput.value).toFixed(1); });
    initialPreyDefenseInput.addEventListener('input', () => { initialPreyDefenseValueSpan.textContent = parseFloat(initialPreyDefenseInput.value).toFixed(1); });
    initialPredatorSpeedInput.addEventListener('input', () => { initialPredatorSpeedValueSpan.textContent = parseFloat(initialPredatorSpeedInput.value).toFixed(1); });
    initialPredatorAttackInput.addEventListener('input', () => { initialPredatorAttackValueSpan.textContent = parseFloat(initialPredatorAttackInput.value).toFixed(1); });


    // Initialize simulation state
    function initializeSimulation() {
        if (simulationRunning) return;
        simulationRunning = true;

        generation = 0;
        currentPreyPop = parseInt(initialPreyPopInput.value) || 500;
        currentPredatorPop = parseInt(initialPredatorPopInput.value) || 50;
        avgPreySpeed = parseFloat(initialPreySpeedInput.value) || 10;
        avgPreyDefense = parseFloat(initialPreyDefenseInput.value) || 10;
        avgPredatorSpeed = parseFloat(initialPredatorSpeedInput.value) || 10;
        avgPredatorAttack = parseFloat(initialPredatorAttackInput.value) || 10;
        preyEatenLastGen = 0;

        // Store initial traits as previous for the first update display call
        prevAvgPreySpeed = avgPreySpeed;
        prevAvgPreyDefense = avgPreyDefense;
        prevAvgPredatorSpeed = avgPredatorSpeed;
        prevAvgPredatorAttack = avgPredatorAttack;


        // Enable/Disable buttons
        nextGenBtn.disabled = false;
        runAutoBtn.disabled = false;
        startSimBtn.disabled = true;
        stopAutoBtn.style.display = 'none'; // Hide stop button initially

        // Hide messages
        extinctionMessage.style.display = 'none';
        stableMessage.style.display = 'none';

        updateDisplay();
    }

    // Simulate one generation
    function simulateGeneration() {
        if (currentPreyPop <= 0 || currentPredatorPop <= 0) {
             endSimulation("extinction");
             return;
        }

        generation++;

        // Store current traits before calculation for display comparison
        prevAvgPreySpeed = avgPreySpeed;
        prevAvgPreyDefense = avgPreyDefense;
        prevAvgPredatorSpeed = avgPredatorSpeed;
        prevAvgPredatorAttack = avgPredatorAttack;


        // --- Population Dynamics ---
        // Base prey increase
        let newPrey = currentPreyPop * (1 + preyBaseBirthRate);
        // Base prey decrease
        newPrey *= (1 - preyBaseDeathRate); // Apply base death rate


        // Calculate hunting success based on relative traits and population sizes
        // Simplified probability of a single encounter leading to a kill
        // Higher predator stats vs lower prey stats = higher probability
        const effectivePredatorPower = avgPredatorSpeed + avgPredatorAttack;
        const effectivePreyEvasion = avgPreySpeed + avgPreyDefense;

        // Probability of a predator successfully killing a prey in an encounter
        // Using a logistic-like function to keep probability between 0 and 1
        // Let's use a simpler ratio model that still allows arms race
        // Success is higher if predator advantage is higher
        const traitAdvantage = (effectivePredatorPower - effectivePreyEvasion);
        // Probability is related to how much stronger the predator is relative to the combined stats
        // Simplified: prob = predator_power / (predator_power + prey_evasion)
        let huntSuccessProbability = effectivePredatorPower / (effectivePredatorPower + effectivePreyEvasion + 0.1); // Add small constant to avoid div by zero/extreme values

        // How many potential encounters happen? Scales with both populations
        // Let's simplify: total potential interactions scale linearly with predator pop and slightly less than linear with prey pop (density effect)
        const interactionFactor = currentPreyPop / (currentPreyPop + 100); // More prey = more potential interactions, but plateaus
        let potentialTotalKills = currentPredatorPop * huntSuccessProbability * 5 * interactionFactor; // 5 is an arbitrary scaling factor

        // Actual prey eaten is limited by the available prey population
        let actualPreyEaten = Math.min(potentialTotalKills, currentPreyPop * 0.9); // Cannot eat more than 90% of available prey in one go

        // Update prey population: subtract those eaten
        newPrey -= actualPreyEaten;
        currentPreyPop = Math.max(0, Math.round(newPrey));

        preyEatenLastGen = Math.round(actualPreyEaten);


        // Update predator population
        let newPredators = currentPredatorPop * (1 - predatorBaseDeathRate); // Base predator death
        newPredators += preyEatenLastGen * predatorReproductionRatePerKill; // Predators reproduce based on food
        currentPredatorPop = Math.max(0, Math.round(newPredators));


        // --- Trait Evolution ---
        // Traits of the next generation are influenced by the survivors and random mutation
        // Selection pressure: Higher for prey if many were eaten relative to population size. Higher for predators if they got lots of food relative to their population size.
        const preySelectionPressure = preyEatenLastGen / (Math.max(1, currentPreyPop + preyEatenLastGen)); // Proportion of original prey population (survivors + eaten) that was eaten
        const predatorSelectionPressure = (currentPredatorPop > 0) ? (preyEatenLastGen / currentPredatorPop) / 10 : 0; // Food gained per predator, scaled down (arbitrary factor 10) - Pressure is higher if per-capita food is high


        // Prey evolve: Pressure to increase speed against fast predators, defense against high attack predators
        // The change is proportional to the difference in trait and the selection pressure on prey
        let deltaPreySpeed = evolutionRate * (avgPredatorSpeed - avgPreySpeed) * preySelectionPressure;
        let deltaPreyDefense = evolutionRate * (avgPredatorAttack - avgPreyDefense) * preySelectionPressure;

        // Predators evolve: Pressure to increase speed against fast prey, attack against high defense prey
        // The change is proportional to the difference in trait and the selection pressure on predators
        let deltaPredatorSpeed = evolutionRate * (avgPreySpeed - avgPredatorSpeed) * predatorSelectionPressure;
        let deltaPredatorAttack = evolutionRate * (avgPreyDefense - avgPredatorAttack) * predatorSelectionPressure;

        // Add random mutation (small random change)
        deltaPreySpeed += (Math.random() - 0.5) * mutationMagnitude;
        deltaPreyDefense += (Math.random() - 0.5) * mutationMagnitude;
        deltaPredatorSpeed += (Math.random() - 0.5) * mutationMagnitude;
        deltaPredatorAttack += (Math.random() - 0.5) * mutationMagnitude;

        // Update traits, ensuring they don't fall below minimum
        avgPreySpeed = Math.max(minTrait, avgPreySpeed + deltaPreySpeed);
        avgPreyDefense = Math.max(minTrait, avgPreyDefense + deltaPreyDefense);
        avgPredatorSpeed = Math.max(minTrait, avgPredatorSpeed + deltaPredatorSpeed);
        avgPredatorAttack = Math.max(minTrait, avgPredatorAttack + deltaPredatorAttack);

        updateDisplay();

         // Check for extinction after updates
        if (currentPreyPop <= 0 || currentPredatorPop <= 0) {
             endSimulation("extinction");
        } else if (preyEatenLastGen === 0 && currentPredatorPop > 0 && currentPreyPop > 0 && generation > 10) {
             // Potential stability check - very basic: no kills means predators will likely starve unless they have a high base survival rate
             // A more robust check would look at population changes over several generations
             // For this sim, let's just add a message if kills are zero for a while and pops exist
              if (currentPredatorPop < 10 || currentPreyPop < 20) {
                  // Don't show stable message if populations are tiny
              } else {
                   stableMessage.style.display = 'block';
              }
        } else {
            stableMessage.style.display = 'none'; // Hide if conditions for stability message are not met
        }
    }

    // Update the display with current state
    function updateDisplay() {
        generationText.textContent = generation;
        preyPopText.textContent = currentPreyPop;
        predatorPopText.textContent = currentPredatorPop;

        updateTraitDisplay(avgPreySpeedText, avgPreySpeed, prevAvgPreySpeed, avgPreySpeedArrow);
        updateTraitDisplay(avgPreyDefenseText, avgPreyDefense, prevAvgPreyDefense, avgPreyDefenseArrow);
        updateTraitDisplay(avgPredatorSpeedText, avgPredatorSpeed, prevAvgPredatorSpeed, avgPredatorSpeedArrow);
        updateTraitDisplay(avgPredatorAttackText, avgPredatorAttack, prevAvgPredatorAttack, avgPredatorAttackArrow);

        preyEatenText.textContent = preyEatenLastGen;

        // Simple visual indicators for population trends (can be improved)
        if (generation > 0) {
            const preyChange = currentPreyPop - (currentPreyPop + preyEatenLastGen) * (1 + preyBaseBirthRate - preyBaseDeathRate); // Approximate previous population before eating
            const predatorChange = currentPredatorPop - (currentPredatorPop * (1 - predatorBaseDeathRate) + preyEatenLastGen * predatorReproductionRatePerKill); // Approximate previous population before reproduction/death

            // These indicators are just stylistic pulses, not trend indicators
            // For actual trend indicators, we'd need to store history or compare current vs previous
            // Let's keep the pulsing indicators for life sign and maybe add color for trend
             preyPopIndicator.style.backgroundColor = currentPreyPop > (currentPreyPop + preyEatenLastGen) * (1 + preyBaseBirthRate - preyBaseDeathRate) ? var(--primary-color) : var(--predator-color); // Green if increasing, Red if decreasing
             predatorPopIndicator.style.backgroundColor = currentPredatorPop > (currentPredatorPop * (1 - predatorBaseDeathRate) + preyEatenLastGen * predatorReproductionRatePerKill) ? var(--primary-color) : var(--predator-color); // Green if increasing, Red if decreasing

            // Reset animation
             preyPopIndicator.style.animation = 'none';
             predatorPopIndicator.style.animation = 'none';
             requestAnimationFrame(() => {
                  preyPopIndicator.style.animation = 'pulse 1.5s infinite ease-in-out';
                  predatorPopIndicator.style.animation = 'pulse 1.5s infinite ease-in-out';
             });
        }


    }

    function updateTraitDisplay(textElement, currentValue, previousValue, arrowElement) {
        textElement.textContent = currentValue.toFixed(2);
        // Update arrow indicator based on change from previous generation
        arrowElement.textContent = ''; // Clear previous arrow
        arrowElement.className = 'trait-arrow'; // Reset classes
        if (currentValue > previousValue + 0.001) { // Check for meaningful increase
            arrowElement.textContent = '↑';
            arrowElement.classList.add('up');
        } else if (currentValue < previousValue - 0.001) { // Check for meaningful decrease
            arrowElement.textContent = '↓';
             arrowElement.classList.add('down');
        } else {
             arrowElement.textContent = '•';
             arrowElement.classList.add('neutral');
        }
         // Reset and restart animation
        arrowElement.style.animation = 'none';
        requestAnimationFrame(() => {
             arrowElement.style.animation = 'fade-in 0.5s ease-out';
        });
    }


    // Toggle explanation visibility
    function toggleExplanation() {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            showExplanationBtn.textContent = 'הסתר הסבר';
        } else {
            explanationDiv.style.display = 'none';
            showExplanationBtn.textContent = 'הצג הסבר על מירוץ חימוש אבולוציוני';
        }
    }

    // Automatic run functionality
    function startAutoRun() {
        let count = 0;
        runAutoBtn.disabled = true;
        nextGenBtn.disabled = true;
        stopAutoBtn.style.display = 'inline-block';
        stableMessage.style.display = 'none'; // Hide stable message during auto run

        autoRunInterval = setInterval(() => {
            if (count < autoRunGenerations && currentPreyPop > 0 && currentPredatorPop > 0) {
                simulateGeneration();
                count++;
            } else {
                stopAutoRun();
                 if (currentPreyPop <= 0 || currentPredatorPop <= 0) {
                     endSimulation("extinction");
                 } else {
                     // Auto run finished without extinction, check for stability message
                     if (preyEatenLastGen === 0 && currentPredatorPop > 0 && currentPreyPop > 0 && generation > 10) {
                         if (currentPredatorPop < 10 || currentPreyPop < 20) { /* Do nothing */ }
                         else { stableMessage.style.display = 'block'; }
                    }
                 }
            }
        }, 150); // Run every 150ms
    }

    function stopAutoRun() {
        clearInterval(autoRunInterval);
        autoRunInterval = null;
        runAutoBtn.disabled = false;
        nextGenBtn.disabled = false;
        stopAutoBtn.style.display = 'none';
         // Re-check for stability message after manual stop if populations exist
        if (currentPreyPop > 0 && currentPredatorPop > 0 && generation > 10) {
            if (preyEatenLastGen === 0 && currentPredatorPop > 0 && currentPreyPop > 0) {
                 if (currentPredatorPop < 10 || currentPreyPop < 20) { /* Do nothing */ }
                 else { stableMessage.style.display = 'block'; }
            }
        }
    }

     function endSimulation(reason) {
        stopAutoRun(); // Ensure auto run stops
        simulationRunning = false; // Allow starting a new simulation

        nextGenBtn.disabled = true;
        runAutoBtn.disabled = true;
        startSimBtn.disabled = false; // Allow starting again

        if (reason === "extinction") {
            extinctionMessage.style.display = 'block';
             stableMessage.style.display = 'none';
        }
        // No specific action for "stable" state on end, message is shown in updateDisplay or autoRun logic
     }


    // Initial state on page load
     nextGenBtn.disabled = true; // Disable "Next Gen" until simulation starts
     runAutoBtn.disabled = true; // Disable "Run Auto" until simulation starts
    updateDisplay(); // Display initial placeholder values from HTML
     // Update range value spans initially
     initialPreySpeedValueSpan.textContent = parseFloat(initialPreySpeedInput.value).toFixed(1);
     initialPreyDefenseValueSpan.textContent = parseFloat(initialPreyDefenseInput.value).toFixed(1);
     initialPredatorSpeedValueSpan.textContent = parseFloat(initialPredatorSpeedInput.value).toFixed(1);
     initialPredatorAttackValueSpan.textContent = parseFloat(initialPredatorAttackInput.value).toFixed(1);


</script>
```