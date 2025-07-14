---
title: "סוד הבלסמי: מסע התסיסה והיישון הקסום"
english_slug: secret-of-balsamic-fermentation-over-time
category: "מדעים מדויקים / כימיה"
tags: ["תסיסה", "חומץ בלסמי", "כימיה אורגנית", "מיקרוביולוגיה", "מדעי המזון"]
---
# סוד הבלסמי: מסע התסיסה והיישון הקסום

דמיינו מסע בזמן: ענבים עסיסיים נקטפים בשיא מתיקותם, אך במקום להפוך ליין, הם עוברים תהליך קסום וארוך שנים. נעולים בחביות עץ עתיקות, מיקרואורגניזמים חרוצים והזמן עצמו פועלים יחד כדי להפוך את רכז הענבים הנוזלי לנוזל כהה, סמיך, ומפוצץ בטעמים מורכבים - חומץ בלסמי מסורתי אמיתי. הצטרפו אלינו לחשוף את הסודות הכימיים והביולוגיים שמאחורי אחת מפלאי הקולינריה של איטליה!

<div class="simulation-app">
    <h2>צאו למסע: סימולציית יצירת חומץ בלסמי</h2>
    <div class="controls">
        <h3>הגדירו את תנאי ההתחלה:</h3>
        <div class="control-group">
            <div>
                <label for="sugar-concentration">ריכוז סוכר ראשוני (רכז ענבים):</label>
                <input type="range" id="sugar-concentration" min="18" max="35" value="25">
                <span id="sugar-value" class="value-display">25%</span>
            </div>
            <div>
                <label for="initial-temp">טמפרטורת סביבה (התחלתית):</label>
                <input type="range" id="initial-temp" min="15" max="30" value="25">
                <span id="temp-value" class="value-display">25°C</span>
            </div>
            <div>
                <label for="yeast-concentration">כמות שמרי יין:</label>
                <select id="yeast-concentration">
                    <option value="low">נמוכה (תסיסה איטית)</option>
                    <option value="medium" selected>בינונית (קצב אופטימלי)</option>
                    <option value="high">גבוהה (תסיסה מהירה)</option>
                </select>
            </div>
            <div>
                <label for="bacteria-concentration">כמות חיידקי חומצה אצטית:</label>
                <select id="bacteria-concentration">
                    <option value="low">נמוכה (חומציות חלשה)</option>
                    <option value="medium" selected>בינונית (קצב אופטימלי)</option>
                    <option value="high">גבוהה (חומציות מהירה)</option>
                </select>
            </div>
        </div>
        <h3>בחרו את תנאי היישון:</h3>
        <div class="control-group">
            <div>
                <label for="barrel-type">סוג חבית עיקרי:</label>
                <select id="barrel-type">
                    <option value="oak">אלון (וניל, מבנה)</option>
                    <option value="cherry">דובדבן (פירותיות עדינה)</option>
                    <option value="chestnut">ערמון (גוון אגוזי/מעושן)</option>
                    <option value="mixed">מעורב (מורכבות טעמים)</option>
                </select>
            </div>
            <div>
                <label for="barrel-size">גודל חביות (מערכת 'Batteria'):</label>
                <select id="barrel-size">
                    <option value="large">גדולות (אידוי איטי)</option>
                    <option value="medium" selected>בינוניות (אידוי בינוני)</option>
                    <option value="small">קטנות (אידוי מהיר, ריכוז)</option>
                </select>
            </div>
            <div>
                <label for="aging-time">משך יישון (שנים):</label>
                <input type="number" id="aging-time" min="1" max="50" value="12">
            </div>
        </div>
        <button id="run-simulation">התחל את המסע בזמן!</button>
        <p id="simulation-status" class="status-message"></p>
    </div>

    <div class="results">
        <h3>המצב הנוכחי של הבלסמי במסע:</h3>
        <div class="time-display">זמן הסימולציה: <span id="current-time">0.0</span> שנים</div>

        <div class="progress-bars-container">
            <div class="graph">
                <h4>סוכר</h4>
                <div class="bar-container"><div id="sugar-bar" class="bar"></div></div>
                <span id="sugar-level" class="level-text">גבוה מאוד</span>
            </div>
            <div class="graph">
                <h4>אלכוהול</h4>
                <div class="bar-container"><div id="alcohol-bar" class="bar"></div></div>
                <span id="alcohol-level" class="level-text">אפס</span>
            </div>
            <div class="graph">
                <h4>חומצה אצטית</h4>
                <div class="bar-container"><div id="acid-bar" class="bar"></div></div>
                <span id="acid-level" class="level-text">עקבות</span>
            </div>
        </div>

        <div class="visual-indicators">
            <h4>מאפיינים מתפתחים:</h4>
            <div class="indicator">
                <span class="indicator-label">צבע:</span>
                <span id="color-indicator" class="visual-box"></span>
                <span id="color-text" class="level-text">שקוף/בהיר</span>
            </div>
            <div class="indicator">
                 <span class="indicator-label">צמיגות:</span>
                 <span id="viscosity-icon" class="material-icons">water_drop</span>
                 <span id="viscosity-text" class="level-text">נוזלית מאוד</span>
             </div>
             <div class="indicator">
                 <span class="indicator-label">ריכוז חומר יבש:</span>
                 <span id="dry-matter-icon" class="material-icons">filter_drama</span>
                 <span id="dry-matter-text" class="level-text">נמוך יחסית</span>
             </div>
        </div>
        <div class="flavor-notes">
             <h4>הערות טעם מתפתחות:</h4>
             <p id="flavor-text">הטעמים יתפתחו עם הזמן והיישון בחביות.</p>
        </div>

        <div class="final-result">
            <h3>התוצאה הסופית של המסע:</h3>
            <p id="final-description">הפעל את הסימולציה כדי לראות מה קורה בסוף המסע הארוך.</p>
             <p id="quality-rating" class="quality"></p>
        </div>
    </div>
</div>

<style>
    /* Import Google Fonts & Icons */
    @import url('https://fonts.googleapis.com/css2?family=Alef:wght@400;700&family=Rubik:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/icon?family=Material+Icons');

    .simulation-app {
        font-family: 'Rubik', sans-serif;
        max-width: 960px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background: linear-gradient(to bottom right, #fefefe, #f0f0f0);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        color: #333;
    }
    .simulation-app h2 {
        text-align: center;
        color: #5a3a2b; /* Rich brown */
        font-family: 'Alef', sans-serif;
        margin-bottom: 25px;
    }
     .simulation-app h3 {
        color: #705545; /* Slightly lighter brown */
        margin-top: 20px;
        margin-bottom: 15px;
        padding-bottom: 5px;
        border-bottom: 1px solid #eee;
     }

    .controls, .results {
        margin-bottom: 25px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }
    .control-group {
        margin-bottom: 20px;
    }
    .controls div {
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }
    .controls label {
        display: inline-block;
        width: 220px; /* Increased width for labels */
        margin-right: 15px;
        font-weight: 500; /* Medium weight */
        color: #555;
        flex-shrink: 0; /* Prevent label from shrinking */
    }
    .controls input[type="range"], .controls select, .controls input[type="number"] {
        vertical-align: middle;
        flex-grow: 1; /* Allow inputs to take available space */
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1em;
    }
     .controls input[type="number"] {
        flex-grow: 0;
        width: 80px; /* Fixed width for number input */
     }
    .value-display {
        display: inline-block;
        min-width: 50px; /* Ensure space for value */
        text-align: right;
        margin-left: 10px;
        font-weight: bold;
        color: #666;
    }

    .controls button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #8b4513; /* SaddleBrown - balsamic color */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.2em;
        font-weight: 700;
        cursor: pointer;
        margin-top: 25px;
        transition: background-color 0.3s ease;
    }
    .controls button:hover {
        background-color: #a0522d; /* Siennna */
    }
     .controls button:disabled {
         background-color: #ccc;
         cursor: not-allowed;
     }

    .status-message {
        text-align: center;
        margin-top: 15px;
        font-size: 1em;
        color: #5a3a2b;
        min-height: 1.5em; /* Reserve space */
    }

    .progress-bars-container {
        display: flex;
        justify-content: space-around;
        margin-bottom: 20px;
        gap: 15px; /* Space between bars */
    }
    .graph {
        text-align: center;
        width: 32%; /* Slightly less than 1/3 to account for gap */
        font-weight: 500;
    }
     .graph h4 {
         margin-top: 0;
         margin-bottom: 8px;
         color: #555;
     }
    .bar-container {
        width: 100%;
        height: 25px; /* Taller bars */
        border: 1px solid #ccc;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 8px;
        background-color: #eee;
    }
    .bar {
        height: 100%;
        width: 0%; /* Initial state */
        transition: width 0.1s linear; /* Smooth animation */
    }
    #sugar-bar { background: linear-gradient(to right, #ffda63, #f7b731); } /* Warm yellow/orange */
    #alcohol-bar { background: linear-gradient(to right, #87ceeb, #4682b4); } /* SkyBlue/SteelBlue */
    #acid-bar { background: linear-gradient(to right, #e9967a, #cd5c5c); } /* Light red/IndianRed */

    .level-text {
        font-weight: bold;
        color: #666;
    }

    .visual-indicators {
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px dashed #ccc;
    }
    .visual-indicators h4 {
         margin-top: 0;
         margin-bottom: 15px;
         color: #555;
    }
    .indicator {
        margin-bottom: 12px;
        font-weight: 500;
        display: flex;
        align-items: center;
        color: #555;
    }
     .indicator-label {
         display: inline-block;
         width: 150px; /* Align labels */
         flex-shrink: 0;
     }
     .material-icons {
         font-size: 1.4em;
         margin-right: 8px;
         color: #8b4513; /* Balsamic color for icons */
     }
    .visual-box {
        display: inline-block;
        width: 40px; /* Larger color box */
        height: 25px;
        border: 1px solid #333;
        vertical-align: middle;
        margin-right: 10px;
        background-color: #fff; /* Default light color */
        transition: background-color 0.5s ease; /* Smooth color transition */
         box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
    }
     #viscosity-icon { color: #007bff; /* Blueish for liquid flow */ }
     #dry-matter-icon { color: #8b4513; /* Brown for concentration */ }


    .flavor-notes {
        margin-top: 20px;
         padding-top: 15px;
        border-top: 1px dashed #ccc;
    }
     .flavor-notes h4 {
         margin-top: 0;
         margin-bottom: 10px;
          color: #555;
     }
     #flavor-text {
         font-style: italic;
         color: #777;
     }

    .final-result {
        margin-top: 25px;
        padding-top: 20px;
        border-top: 2px solid #8b4513; /* Stronger separator */
        text-align: center;
    }
     .final-result h3 {
         color: #5a3a2b;
         margin-bottom: 15px;
         border-bottom: none;
     }
    #final-description {
        font-size: 1.1em;
        line-height: 1.6;
        color: #444;
    }
     .quality {
         font-size: 1.2em;
         font-weight: bold;
         margin-top: 10px;
         min-height: 1.5em; /* Reserve space */
     }
    .quality.good { color: #28a745; } /* Green */
    .quality.medium { color: #ffc107; } /* Yellow */
    .quality.poor { color: #dc3545; } /* Red */

    #toggleExplanation {
        display: block;
        width: 100%;
        padding: 12px;
        margin-top: 30px;
        background-color: #6c757d; /* Gray */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        cursor: pointer;
        text-align: center;
        transition: background-color 0.3s ease;
        font-family: 'Rubik', sans-serif;
        font-weight: 500;
    }
    #toggleExplanation:hover {
        background-color: #5a6268;
    }

    .explanation-section {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background: #f9f9f9;
        color: #333;
        font-family: 'Rubik', sans-serif;
        line-height: 1.6;
    }
    .explanation-section h2, .explanation-section h3 {
         color: #5a3a2b;
         font-family: 'Alef', sans-serif;
    }
    .explanation-section h3 {
        margin-top: 20px;
        margin-bottom: 10px;
         border-bottom: 1px dashed #ccc;
         padding-bottom: 3px;
         color: #705545;
    }
     .explanation-section ul {
         margin-top: 10px;
         margin-bottom: 15px;
         padding-left: 20px;
     }
     .explanation-section li {
         margin-bottom: 8px;
     }
    .hidden {
        display: none;
    }

     /* Responsive adjustments */
     @media (max-width: 768px) {
         .controls label {
             width: 100%; /* Full width for labels on smaller screens */
             margin-right: 0;
             margin-bottom: 5px;
         }
         .controls div {
             flex-direction: column;
             align-items: flex-start;
         }
         .controls input[type="range"], .controls select, .controls input[type="number"] {
              width: 100%; /* Full width for inputs */
         }
          .value-display {
              text-align: left;
              margin-left: 0;
              margin-top: 5px;
              width: 100%;
          }
         .progress-bars-container {
             flex-direction: column;
             gap: 20px;
         }
         .graph {
             width: 100%;
         }
         .indicator {
             flex-direction: column;
             align-items: flex-start;
         }
         .indicator-label {
             width: 100%;
             margin-bottom: 5px;
         }
         .visual-box {
             margin-right: 5px;
         }
     }

</style>

<button id="toggleExplanation">מה בעצם קורה שם בפנים? לחצו להסבר המדעי המלא</button>

<div id="explanation" class="explanation-section hidden">
    <h2>המסע המולקולרי: הסבר מעמיק על קסם הבלסמי</h2>

    <h3>הבסיס: רכז ענבים מבושל ('Mosto Cotto')</h3>
    <p>המסע מתחיל לא מענבים שלמים, אלא מרכז ענבים טרי שבושל ארוכות על אש נמוכה. הבישול מרכז את הסוכרים, מעקר אותו באופן חלקי, ומתחיל תגובות מאיאר ראשוניות שתורמות לצבע ולטעמים ראשוניים. התוצר הוא נוזל מתוק ועשיר, אך עדיין לא חומץ.</p>

    <h3>השלב הראשון: מתיקות הופכת לאלכוהול (תסיסה כוהלית)</h3>
    <p>כשהרכז המבושל מתקרר ומועבר לחבית הראשונה (או למכל), נכנסים לפעולה שמרים - בעיקר <i>Saccharomyces cerevisiae</i>, אותם שמרים ותיקים שמשמשים לייצור יין. הם מוצאים ברכז סוכר בשפע ומתחילים "לאכול" אותו, תוך פליטת אלכוהול (אתנול) ופחמן דו-חמצני כתוצרי לוואי. זהו תהליך אנאירובי (שאינו דורש חמצן רב).</p>
    <ul>
        <li><strong>הגיבורים המיקרוסקופיים:</strong> שמרים חרוצים.</li>
        <li><strong>ההמרה הכימית:</strong> סוכרים (גלוקוז, פרוקטוז) &rarr; אתנול + פחמן דו-חמצני.</li>
        <li><strong>גורמים קריטיים:</strong> טמפרטורה נוחה לשמרים, ריכוז סוכר (יותר סוכר = פוטנציאל ליותר אלכוהול), זמינות חומרים מזינים לשמרים. השלב הזה קצר יחסית, בעיקר בחודשים הראשונים.</li>
    </ul>

    <h3>השלב השני: האלכוהול הופך לחומציות (תסיסה אצטית)</h3>
    <p>לאחר שרוב הסוכר הומר לאלכוהול, נכנסים לתמונה גיבורים אחרים: חיידקי חומצה אצטית (כמו <i>Acetobacter</i> ו-<i>Gluconobacter</i>). חיידקים אלו הם אירוביים - הם זקוקים לחמצן כדי לפעול. הם לוקחים את האלכוהול שנוצר בשלב הראשון ובתהליך חימצון ממירים אותו לחומצה אצטית - המרכיב העיקרי בחומץ.</p>
    <ul>
        <li><strong>הגיבורים המיקרוסקופיים:</strong> חיידקים נושמי חמצן.</li>
        <li><strong>ההמרה הכימית:</strong> אתנול + חמצן &rarr; חומצה אצטית + מים.</li>
        <li><strong>גורמים קריטיים:</strong> נוכחות חמצן (פתחי החביות קריטיים כאן!), טמפרטורה מתאימה לחיידקים, ריכוז אלכוהול (חייבים אלכוהול כדי לייצר חומצה!), וגם ריכוז החומצה עצמה (ריכוז חומצה גבוה מדי יכול לעכב ואף להרוג את החיידקים).</li>
    </ul>

    <h3>השלב המכריע: היישון הארוך במערכת החביות ('Batteria')</h3>
    <p>זהו סוד הקסם האמיתי של הבלסמי המסורתי. הנוזל, שכעת הוא תערובת של אלכוהול, חומצה אצטית, סוכרים שיוריים ותרכובות רבות מהענבים, מועבר לסדרה של חביות עץ מסוגים וגדלים שונים, המסודרות מהגדול לקטן (ה-'Batteria'). כאן מתרחש תהליך איטי, ממושך ומורכב בן שנים רבות (לפחות 12!).</p>
    <ul>
        <li><strong>התרכזות באמצעות אידוי:</strong> חביות העץ אינן אטומות לחלוטין. דרך נקבוביות העץ ובמיוחד דרך פתח קטן בחבית המכוסה ברשת למניעת כניסת חרקים, מים מתאדים באיטיות. האלכוהול והחומצות מתאדים פחות מהמים, כך שהנוזל הנותר הופך מרוכז, סמיך ועשיר יותר. קצב האידוי תלוי בגודל החבית (קטנות מתאדות מהר יותר) ובתנאי הסביבה (טמפרטורה, לחות).</li>
        <li><strong>אינטראקציה עם העץ:</strong> סוגי עץ שונים (אלון, ערמון, דובדבן, תות, אפרסק) תורמים טעמים, צבעים ותרכובות ארומטיות שונות לנוזל. אלון תורם וניל וטאנינים, דובדבן פירותיות, ערמון גוון אגוזי ועוד. החביות הקטנות יותר בעלות שטח פנים יחסית גדול לנפח, ולכן ההשפעה שלהן על הטעם והריכוז גדולה יותר.</li>
        <li><strong>פיתוח טעמים מורכבים:</strong> במהלך היישון, מתרחשות אינספור תגובות כימיות איטיות: יצירת אסטרים (תרכובות ארומטיות המעניקות ריחות פירותיים ופרחוניים), המשך תגובות מאיאר (המעמיקות את הצבע הכהה ומוסיפות טעמים קלויים וקרמליים), ופירוק איטי של חומרים מסוימים. תגובות אלו הופכות את הפרופיל הכימי והארומטי של החומץ למורכב ועשיר לאין שיעור מחומץ רגיל.</li>
        <li><strong>שיטת ה-'Transvaso' (העברה שנתית):</strong> מדי שנה, כמות קטנה של חומץ נלקחת מהחבית הקטנה ביותר ב'באטריה' לצורך בקבוק. החבית הריקה הזו מתמלאת בנוזל מהחבית הגדולה יותר שלפניה בסדרה. תהליך זה ממשיך במעלה הסדרה, עד שהחבית הגדולה ביותר מתמלאת ברכז ענבים מבושל חדש (או חומץ צעיר מהשנה הקודמת שהתחיל את המסע). שיטה זו יוצרת תהליך ערבוב הדרגתי ומבטיחה שגם החומץ הצעיר ביותר "יתחנך" על ידי החומץ הוותיק יותר, תוך שמירה על סגנון עקבי לאורך עשרות ואף מאות שנים.</li>
    </ul>

    <h3>התוצאה: נוזל זהב כהה</h3>
    <p>לאחר שנים רבות (12, 25, או אפילו יותר!), מתקבל חומץ בלסמי מסורתי אמיתי - נוזל סמיך כסירופ, כהה כמעט שחור, בעל איזון מושלם בין מתיקות, חומציות, ומורכבות טעמים וארומות שנוצרו מהענבים, התסיסה, העץ והזמן. איכותו נמדדת בצמיגותו, עומק צבעו, ובפרופיל הטעמים והריחות העשיר שלו.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Get control elements
        const sugarRange = document.getElementById('sugar-concentration');
        const sugarValueSpan = document.getElementById('sugar-value');
        const tempRange = document.getElementById('initial-temp');
        const tempValueSpan = document.getElementById('temp-value');
        const yeastSelect = document.getElementById('yeast-concentration');
        const bacteriaSelect = document.getElementById('bacteria-concentration');
        const barrelTypeSelect = document.getElementById('barrel-type');
        const barrelSizeSelect = document.getElementById('barrel-size');
        const agingTimeInput = document.getElementById('aging-time');
        const runButton = document.getElementById('run-simulation');
        const statusMessage = document.getElementById('simulation-status');

        // Get results elements
        const currentTimeSpan = document.getElementById('current-time');
        const sugarBar = document.getElementById('sugar-bar');
        const alcoholBar = document.getElementById('alcohol-bar');
        const acidBar = document.getElementById('acid-bar');
        const sugarLevelSpan = document.getElementById('sugar-level');
        const alcoholLevelSpan = document.getElementById('alcohol-level');
        const acidLevelSpan = document.getElementById('acid-level');
        const colorIndicator = document.getElementById('color-indicator');
        const colorTextSpan = document.getElementById('color-text');
        const viscosityTextSpan = document.getElementById('viscosity-text');
        const dryMatterTextSpan = document.getElementById('dry-matter-text');
        const flavorTextSpan = document.getElementById('flavor-text');
        const finalDescriptionParagraph = document.getElementById('final-description');
        const qualityRatingSpan = document.getElementById('quality-rating');

        // Get explanation elements
        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggleExplanation');

        // State variables for simulation
        let currentSugar = 0; // %
        let currentAlcohol = 0; // %
        let currentAcid = 0; // %
        let currentColor = 0; // 0=lightest, 100=darkest
        let currentViscosity = 0; // 0=lowest, 100=highest
        let currentDryMatter = 0; // Relative value, increases with concentration
        let simulationTime = 0; // in years
        let simulationInterval = null; // To hold the interval timer

        // Constants and initial setup
        const initialColorBase = 10; // Color after cooking
        const initialAcidBase = 0.1; // Trace acid initially
        const maxAcidPotential = 10; // Theoretical max acid percentage

        // Update range value displays dynamically
        sugarRange.addEventListener('input', () => {
            sugarValueSpan.textContent = sugarRange.value + '%';
        });
        tempRange.addEventListener('input', () => {
            tempValueSpan.textContent = tempRange.value + '°C';
        });

        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            toggleButton.textContent = explanationDiv.classList.contains('hidden') ? 'מה בעצם קורה שם בפנים? לחצו להסבר המדעי המלא' : 'הסתר את ההסבר המדעי';
        });

        // Function to update the display elements
        const updateDisplay = () => {
            currentTimeSpan.textContent = simulationTime.toFixed(1);

            // Update bars (scaled relative to plausible max values)
            sugarBar.style.width = Math.max(0, Math.min(100, (currentSugar / (parseInt(sugarRange.value) * 1.2)) * 100)) + '%'; // Scale relative to initial sugar + buffer
            alcoholBar.style.width = Math.max(0, Math.min(100, (currentAlcohol / (parseInt(sugarRange.value) * 0.6))) * 100) + '%'; // Scale relative to potential max alcohol
            acidBar.style.width = Math.max(0, Math.min(100, (currentAcid / maxAcidPotential) * 100)) + '%'; // Scale relative to potential max acid

            // Update text levels
            sugarLevelSpan.textContent = currentSugar > parseInt(sugarRange.value) * 0.5 ? 'גבוה מאוד' : (currentSugar > parseInt(sugarRange.value) * 0.2 ? 'גבוה' : (currentSugar > 2 ? 'בינוני' : 'נמוך'));
            if (currentSugar <= 2) sugarLevelSpan.textContent = 'נמוך מאוד';

            alcoholLevelSpan.textContent = currentAlcohol < 1 ? 'אפס' : (currentAlcohol < parseInt(sugarRange.value) * 0.1 ? 'נמוך מאוד' : (currentAlcohol < parseInt(sugarRange.value) * 0.3 ? 'נמוך' : (currentAlcohol < parseInt(sugarRange.value) * 0.5 ? 'בינוני' : 'גבוה')));
            if (currentAlcohol >= parseInt(sugarRange.value) * 0.5) alcoholLevelSpan.textContent = 'גבוה מאוד';


            acidLevelSpan.textContent = currentAcid < 0.5 ? 'עקבות' : (currentAcid < 2 ? 'נמוך מאוד' : (currentAcid < 5 ? 'נמוך' : (currentAcid < 8 ? 'בינוני' : 'גבוה')));
            if (currentAcid >= 8) acidLevelSpan.textContent = 'גבוה מאוד';


            // Update visuals
            const colorIntensity = Math.min(255, Math.max(0, Math.round(currentColor * 2.55))); // Scale 0-100 to 0-255
            // Create a color gradient from light (like must) to dark balsamic
            const r = Math.max(0, Math.min(255, 255 - colorIntensity * 1.5));
            const g = Math.max(0, Math.min(255, 200 - colorIntensity * 1));
            const b = Math.max(0, Math.min(255, 100 - colorIntensity * 0.5));
            colorIndicator.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;

            colorTextSpan.textContent = currentColor < 15 ? 'שקוף/בהיר' : (currentColor < 40 ? 'זהוב/ענברי' : (currentColor < 75 ? 'חום עמוק' : 'כהה מאוד'));
            if (currentColor >= 75) colorTextSpan.textContent = 'שחור כמעט';


            viscosityTextSpan.textContent = currentViscosity < 10 ? 'נוזלית מאוד' : (currentViscosity < 30 ? 'נוזלית' : (currentViscosity < 60 ? 'צמיגית בינונית' : (currentViscosity < 90 ? 'סמיכה' : 'סמיכה מאוד')));
            if (currentViscosity >= 90) viscosityTextSpan.textContent = 'דמוית סירופ';

            dryMatterTextSpan.textContent = currentDryMatter < initialSugar * 1.5 ? 'נמוך יחסית' : (currentDryMatter < initialSugar * 2.5 ? 'בינוני' : (currentDryMatter < initialSugar * 4 ? 'גבוה' : 'גבוה מאוד'));
             if (currentDryMatter >= initialSugar * 4) dryMatterTextSpan.textContent = 'גבוה מאוד';

             // Update flavor notes during aging (simplified)
             if (simulationTime > 1) {
                 let notes = [];
                  const baseAgingFlavor = simulationTime > 5 ? 'ניחוחות מיושנים' : '';
                 if(baseAgingFlavor) notes.push(baseAgingFlavor);

                 if (currentSugar > 5) notes.push('מתיקות ראשונית');
                 if (currentAcid > 4 && currentAcid < 9) notes.push('חומציות מאוזנת');
                  else if (currentAcid >= 9) notes.push('חומציות חזקה');
                  else if (currentAcid > 1) notes.push('חומציות עדינה');


                 if (currentAlcohol > 1) notes.push('רמז אלכוהולי');


                 const barrel = barrelTypeSelect.value;
                 if (simulationTime > 3) { // Barrel influence grows over time
                     if (barrel === 'oak' || barrel === 'mixed') notes.push('רמזים לווניל/עץ קלוי');
                     if (barrel === 'cherry' || barrel === 'mixed') notes.push('תווים פירותיים אדומים');
                     if (barrel === 'chestnut' || barrel === 'mixed') notes.push('גוון אגוזי/מעושן');
                 }

                  if (currentViscosity > 50 && simulationTime > 8) notes.push('מרקם סמיך ועשיר');
                  if (currentDryMatter > initialSugar * 3 && simulationTime > 10) notes.push('מתיקות מרוכזת מאוד');


                 if (notes.length > 0) {
                      flavorTextSpan.textContent = notes.join(', ') + '...';
                  } else {
                       flavorTextSpan.textContent = 'הטעמים מתחילים להתפתח...';
                  }
             } else {
                 flavorTextSpan.textContent = 'טעמים בסיסיים (סוכר, אלכוהול ראשוני).';
             }
        };

        // Simulation core logic (step-by-step)
        const simulateStep = () => {
            const initialSugar = parseInt(sugarRange.value);
            const initialTemp = parseInt(tempRange.value);
            const yeastConc = yeastSelect.value;
            const bacteriaConc = bacteriaSelect.value;
            const barrelType = barrelTypeSelect.value;
            const barrelSize = barrelSizeSelect.value;
            const totalAgingTime = parseInt(agingTimeInput.value);

            let timeStep = 1/12; // Default to monthly steps for the first year
            if (simulationTime >= 1) timeStep = 1; // Yearly steps after the first year

            // Adjust time step based on remaining time to finish exactly at totalAgingTime
             const remainingTime = totalAgingTime - simulationTime;
             const stepsPerSec = 20; // Target steps per second
             const totalStepsNeeded = remainingTime * stepsPerSec; // Rough estimate
             //timeStep = Math.max(timeStep, remainingTime / (stepsPerSec * 1)); // Ensure we finish within reasonable time? No, fixed step is better for animation

             // --- Process Calculations for the current time step ---

             // Phase 1: Alcoholic Fermentation (active mostly in the first year)
             let sugarConsumptionRate = 0;
             if (simulationTime < 1.5 && currentSugar > 2 && currentAlcohol < initialSugar * 0.6) { // Can still ferment if sugar > 2% and Alcohol < potential max
                  let tempFactor = initialTemp / 25; // Base temp factor
                  let yeastFactor = yeastConc === 'high' ? 1.5 : yeastConc === 'medium' ? 1.0 : 0.6;
                  let sugarFactor = Math.max(0, (currentSugar - 2) / initialSugar); // Slow down as sugar decreases
                  sugarConsumptionRate = (sugarFactor * tempFactor * yeastFactor * 15) * timeStep; // Arbitrary rate constant
                  sugarConsumptionRate = Math.min(sugarConsumptionRate, currentSugar - 2); // Don't consume below 2%
                  sugarConsumptionRate = Math.min(sugarConsumptionRate, (initialSugar * 0.6 - currentAlcohol) * 0.5); // Don't exceed alcohol potential too fast

                  currentSugar -= sugarConsumptionRate;
                  currentAlcohol += sugarConsumptionRate * 0.5; // Simplified conversion yield
             }


             // Phase 2: Acetic Fermentation (active once alcohol is present, needs oxygen)
             let alcoholConversionRate = 0;
             if (currentAlcohol > 0.5 && currentAcid < maxAcidPotential * 0.9) { // Need alcohol > 0.5 and Acid < 90% of max potential
                 let tempFactor = initialTemp / 25; // Base temp factor
                 let bacteriaFactor = bacteriaConc === 'high' ? 1.4 : bacteriaConc === 'medium' ? 1.0 : 0.7;
                 let alcoholFactor = Math.max(0, (currentAlcohol - 0.5) / (initialSugar * 0.5)); // Slow down as alcohol decreases
                 let acidInhibitionFactor = Math.max(0.1, 1 - (currentAcid / maxAcidPotential) * 0.8); // Slow down as acid increases

                 alcoholConversionRate = (alcoholFactor * tempFactor * bacteriaFactor * acidInhibitionFactor * 10) * timeStep; // Arbitrary rate constant
                 alcoholConversionRate = Math.min(alcoholConversionRate, currentAlcohol - 0.5); // Don't convert below 0.5% alcohol
                 alcoholConversionRate = Math.min(alcoholConversionRate, (maxAcidPotential * 0.9 - currentAcid) * 0.6); // Don't exceed acid potential too fast

                 currentAlcohol -= alcoholConversionRate;
                 currentAcid += alcoholConversionRate * 1.05; // Simplified conversion yield (acid is slightly heavier by mass)
             }

             // Phase 3: Aging & Concentration (continuous, dominates after first year)
             if (simulationTime >= 0) { // Aging starts immediately in the first year (monthly steps have smaller impact)
                 let evaporationRatePerYear = 0.08; // Base yearly evaporation (approx 8-10%)

                 // Adjust evaporation based on barrel size (surface area to volume ratio)
                 if (barrelSize === 'small') evaporationRatePerYear *= 1.5; // More surface area relative to volume
                 if (barrelSize === 'large') evaporationRatePerYear *= 0.6; // Less surface area relative to volume
                 // Add some variation based on temp? Higher temp = more evaporation
                 evaporationRatePerYear *= (initialTemp / 25);


                 const evaporationRateForStep = evaporationRatePerYear * timeStep;

                 // Evaporation primarily removes water, concentrating all solutes
                 // Simplification: Apply concentration factor to all current values
                 const concentrationFactor = 1 / (1 - evaporationRateForStep);

                 currentSugar *= concentrationFactor;
                 currentAlcohol *= concentrationFactor; // Alcohol also evaporates, but slower than water. This simplifies by concentrating.
                 currentAcid *= concentrationFactor;
                 currentDryMatter *= concentrationFactor;

                 // Color change over time, evaporation, and from barrel interaction
                 let colorIncreaseRate = (20 + (simulationTime * 1)) * timeStep; // Base increase over time
                 colorIncreaseRate *= (evaporationRateForStep * 50); // Higher evaporation = faster color concentration
                  if (barrelSize === 'small') colorIncreaseRate *= 1.2; // Smaller barrels influence faster

                 const barrelColorFactor = {
                     'oak': 1.2,
                     'cherry': 0.9,
                     'chestnut': 1.1,
                     'mixed': 1.1 // Mixed barrels have varied influence
                 };
                 colorIncreaseRate *= barrelColorFactor[barrelType];

                 currentColor += colorIncreaseRate;


                 // Viscosity increases mainly from concentration (linked to dry matter)
                 // It's more than just sugar/acid %, includes complex molecules formed during aging
                 // Rough formula: viscosity increases significantly with dry matter and time
                 let viscosityIncreaseRate = (currentDryMatter / initialSugar) * (simulationTime/totalAgingTime + 0.5) * 5 * timeStep; // Increase based on concentration and time progress
                 viscosityIncreaseRate *= (evaporationRateForStep * 80); // Strong link to evaporation/concentration
                 currentViscosity += viscosityIncreaseRate;

                 // Flavor development (logic handled in updateDisplay based on state)

             }


             // Clamp values to reasonable ranges (prevent negative or excessive growth)
             currentSugar = Math.max(0, currentSugar);
             currentAlcohol = Math.max(0, currentAlcohol); // Alcohol might increase first, then decrease with acetic fermentation
             currentAcid = Math.max(initialAcidBase, Math.min(maxAcidPotential * 1.2, currentAcid)); // Allow slight overshoot but clamp
             currentColor = Math.max(initialColorBase, Math.min(100, currentColor));
             currentViscosity = Math.max(0, Math.min(100, currentViscosity));
             currentDryMatter = Math.max(initialSugar * 1.1, currentDryMatter); // Dry matter starts high due to cooked must

             simulationTime += timeStep;

             updateDisplay(); // Update UI with new state

             // Check if simulation is complete
             if (simulationTime >= totalAgingTime) {
                 clearInterval(simulationInterval);
                 simulationInterval = null;
                 simulationTime = totalAgingTime; // Ensure it stops exactly at the target time
                 updateDisplay(); // Final update

                 runButton.disabled = false; // Enable the button again
                 statusMessage.textContent = "המסע הסתיים!";
                 determineFinalResult(); // Show final result description
             } else {
                  // Update status message based on current phase
                  if (simulationTime < 0.5) {
                       statusMessage.textContent = "שלב התסיסה הכוהלית בעיצומו...";
                   } else if (simulationTime < 2 && currentAlcohol > 1) {
                       statusMessage.textContent = "מתחילה התסיסה החומצית, אלכוהול הופך לחומץ...";
                   } else if (simulationTime >= 1) {
                       statusMessage.textContent = `שלב היישון בחביות מתקדם (שנה ${Math.floor(simulationTime)} מתוך ${totalAgingTime})...`;
                   } else {
                       statusMessage.textContent = "התהליך בעיצומו...";
                   }
             }
        };

        // Determine and display final result description and quality
        const determineFinalResult = () => {
            const initialSugar = parseInt(sugarRange.value);
            const totalAgingTime = parseInt(agingTimeInput.value);
            const barrelType = barrelTypeSelect.value;
            const barrelSize = barrelSizeSelect.value;


            let finalDescription = `לאחר יישון של ${totalAgingTime} שנים במערכת חביות בגודל ${barrelSize} עם דגש על עץ ${barrelType === 'mixed' ? 'מעורב' : barrelType}, החומץ שנוצר הוא: `;
            let qualityScore = 0; // Simple quality score

            // Assess quality based on final state and aging time
            if (totalAgingTime < 12) {
                 finalDescription += "חומץ צעיר יחסית, עדיין לא הגיע לפוטנציאל המלא של בלסמי מסורתי.";
                 qualityScore = 2;
            } else if (totalAgingTime < 25) {
                 // Aged Balsamic (12-24 years)
                 if (currentAcid >= 5 && currentAcid <= 8.5 && currentViscosity > 50 && currentColor > 60 && currentSugar < 10) {
                      finalDescription += "חומץ בלסמי מיושן עם איזון טוב של חומציות, מתיקות וריכוז.";
                      qualityScore = 8;
                 } else {
                      finalDescription += "חומץ בלסמי מיושן, אך עם איזון שאינו מושלם (ייתכן חומצי מדי/פחות מרוכז/מתוק מדי).";
                      qualityScore = 6;
                 }
            } else {
                 // Extra Vecchio (25+ years)
                  if (currentAcid >= 5 && currentAcid <= 8 && currentViscosity > 75 && currentColor > 80 && currentSugar < 8) {
                       finalDescription += "חומץ בלסמי אקסטרה וקיו (Extra Vecchio) - סמיך, כהה, ומורכב להפליא!";
                       qualityScore = 10;
                   } else {
                        finalDescription += "חומץ מיושן מאוד, אך ייתכן שאיבד איזון עקב יישון ארוך מדי או תנאים התחלתיים.";
                        qualityScore = 7;
                   }
            }

            // Add specific feedback based on final parameters
            if (currentAcid < 5) finalDescription += " חומציות נמוכה יחסית.";
            if (currentAcid > 8.5 && totalAgingTime < 25) finalDescription += " חומציות גבוהה יחסית.";
            if (currentViscosity < 50 && totalAgingTime >= 12) finalDescription += " צמיגות נמוכה יחסית לגילו.";
            if (currentColor < 60 && totalAgingTime >= 12) finalDescription += " צבע בהיר יחסית לגילו.";
            if (currentSugar > 10 && totalAgingTime >= 12 && currentAcid < 7) finalDescription += " מתיקות בולטת.";


            // Add flavor notes based on barrel type and aging (more detailed)
            let flavorNotes = [];
            if (currentViscosity > 60 && simulationTime > 10) flavorNotes.push('מרקם דמוי סירופ');
            if (currentDryMatter > initialSugar * 3) flavorNotes.push('מרוכז ועשיר');


            const barrel = barrelTypeSelect.value;
             if (totalAgingTime > 8) { // Barrel influence is significant after ~8 years
                 if (barrel === 'oak' || barrel === 'mixed') flavorNotes.push('תווי וניל/עץ');
                 if (barrel === 'cherry' || barrel === 'mixed') flavorNotes.push('ניחוחות פירות יבשים');
                 if (barrel === 'chestnut' || barrel === 'mixed') flavorNotes.push('גוון אגוזי עדין');
             }
             if (totalAgingTime > 15) flavorNotes.push('מורכבות ארומטית');


             if (flavorNotes.length > 0) {
                 finalDescription += " מאפיינים בולטים: " + flavorNotes.join(', ') + ".";
             }


            finalDescriptionParagraph.textContent = finalDescription;

             // Display quality rating
             qualityRatingSpan.textContent = "הערכת איכות: ";
             if (qualityScore >= 8) {
                 qualityRatingSpan.textContent += "מעולה!";
                 qualityRatingSpan.className = 'quality good';
             } else if (qualityScore >= 5) {
                 qualityRatingSpan.textContent += "טובה";
                 qualityRatingSpan.className = 'quality medium';
             } else {
                 qualityRatingSpan.textContent += "בסיסית/זקוקה לשיפור";
                 qualityRatingSpan.className = 'quality poor';
             }
             qualityRatingSpan.style.display = 'block'; // Make sure it's visible

        };


        // Run simulation button handler
        runButton.addEventListener('click', () => {
             if (simulationInterval) {
                 clearInterval(simulationInterval);
                 simulationInterval = null;
                 runButton.textContent = 'התחל סימולציה מחדש';
                 statusMessage.textContent = "הסימולציה הושהתה.";
                 return; // Pause functionality (optional)
             }

            // Reset state for new run
            currentSugar = parseInt(sugarRange.value);
            currentAlcohol = 0;
            currentAcid = initialAcidBase;
            currentColor = initialColorBase;
            currentViscosity = 0; // Starts low
            currentDryMatter = currentSugar * 1.1; // Base dry matter from cooked must
            simulationTime = 0;
            finalDescriptionParagraph.textContent = "הסימולציה פועלת...";
            qualityRatingSpan.textContent = ""; // Clear previous rating
            qualityRatingSpan.className = 'quality';
            qualityRatingSpan.style.display = 'none'; // Hide rating during run

            runButton.disabled = true; // Disable button during simulation
             runButton.textContent = 'פועל...';


            // Start the simulation loop (adjust interval for speed)
            // Simulate roughly 20 steps per second
            simulationInterval = setInterval(simulateStep, 50); // 50ms per step

            updateDisplay(); // Initial display state
        });

         // Initial display update on page load
         updateDisplay();
         finalDescriptionParagraph.textContent = "הגדירו את הפרמטרים והתחילו את הסימולציה!";
         statusMessage.textContent = "מוכן להפעלה";
         qualityRatingSpan.style.display = 'none';

    });
</script>
---