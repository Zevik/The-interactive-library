---
title: "הצלילים המסתוריים: גלה את פיבונאצ'י ויחס הזהב במוזיקה"
english_slug: the-mathematical-sounds-fibonacci-in-music
category: "מדעים מדויקים / מתמטיקה"
tags: [מוזיקה, מתמטיקה, פיבונאצ'י, תאוריה מוזיקלית, יחס הזהב, אסתטיקה]
---
<h1>הצלילים המסתוריים: גלה את פיבונאצ'י ויחס הזהב במוזיקה</h1>
<p>האם ידעת שהמנגינות שאתה הכי אוהב עשויות להכיל סודות מתמטיים עתיקים? צלול לתוך הקשר המרתק שבין סדרת המספרים של פיבונאצ'י ויחס הזהב לבין המבנה והיופי של יצירות מוזיקליות אהובות. התנסה בוויזואליזציה אינטראקטיבית וגלה בעצמך!</p>

<div class="app-container">
    <h2>חקור ויזואלית את הקשר</h2>
    <p class="app-intro">השתמש בפקדים לבחירת יצירה או הגדרת אורך מותאם אישית, וצפה בנקודות מבנה מרכזיות ביצירה (צבעוניות) לעומת נקודות מחושבות לפי יחסי פיבונאצ'י ויחס הזהב (כסופות). שימו לב האם יש נקודות שנמצאות קרוב או מתלכדות!</p>
    <div class="controls-area">
        <div class="controls">
            <label for="music-piece">בחר יצירה לדוגמה:</label>
            <select id="music-piece">
                <option value="beethoven_5_1">בטהובן, סימפוניה מס' 5, פרק 1</option>
                <option value="mozart_40_1">מוצרט, סימפוניה מס' 40, פרק 1</option>
                <option value="debussy_clair_de_lune">דביסי, אור ירח</option>
                 <option value="custom">אורך מותאם אישית (חקור יחסים)</option>
            </select>
        </div>
        <div class="controls custom-length" style="display: none;">
            <label for="total-length">הגדר אורך וירטואלי:</label>
            <input type="range" id="total-length" min="100" max="1000" value="618"> <!-- Default closer to Golden Ratio -->
            <span id="length-value">618</span> יחידות
        </div>
    </div>
    <div class="timeline-container">
        <div id="timeline">
            <div class="start-marker marker">0%</div>
            <!-- Points will be added here by JS -->
            <div class="end-marker marker">100%</div>
        </div>
        <div class="labels">
            <div class="label structure-label">
                <span class="label-color-box structure-color"></span> מבנה מוזיקלי
            </div>
            <div class="label fibonacci-label">
                <span class="label-color-box fibonacci-color"></span> פיבונאצ'י / יחס הזהב
            </div>
            <div class="label highlight-label" style="display:none;">
                 <span class="label-color-box highlight-color"></span> התאמה קרובה!
             </div>
        </div>
    </div>
     <p class="note">הציר מייצג את אורך היצירה או הקטע (0% עד 100%). קווים צבעוניים מורים על נקודות מבנה משמעותיות (לפי אנליזות קיימות), וקווים כסופים מורים על מיקומים לפי יחסי פיבונאצ'י ויחס הזהב. רחף עם העכבר על הקווים לפרטים נוספים. קווים המופיעים בירוק מצביעים על התאמה קרובה בין מבנה מוזיקלי ליחס מתמטי!</p>
</div>

<style>
    :root {
        --primary-color: #3498db; /* Blue */
        --secondary-color: #e74c3c; /* Red/Orange */
        --fibonacci-color: #bdc3c7; /* Silver/Gray */
        --structure-color: var(--secondary-color);
        --highlight-color: #2ecc71; /* Green */
        --background-color: #f0f4f8; /* Light blue-gray */
        --container-background: #ffffff;
        --border-color: #dcdcdc;
        --text-color: #333;
        --note-color: #666;
    }

    .app-container {
        font-family: 'Segoe UI', Roboto, Arial, sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--container-background);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        color: var(--text-color);
    }

    .app-container h2 {
        text-align: center;
        color: var(--primary-color);
        margin-bottom: 15px;
        font-size: 1.8em;
        font-weight: 600;
    }

     .app-intro {
         text-align: center;
         margin-bottom: 30px;
         color: var(--note-color);
         font-size: 1em;
     }

     .controls-area {
         margin-bottom: 25px;
         padding: 15px;
         background-color: #ecf0f1; /* Lighter background for controls */
         border-radius: 8px;
         display: flex;
         flex-direction: column;
         gap: 15px;
     }

    .controls {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .controls label {
        font-weight: 600;
        color: var(--text-color);
        white-space: nowrap; /* Prevent label wrapping */
    }

     .controls select, .controls input[type="range"] {
         padding: 8px 10px;
         border: 1px solid var(--border-color);
         border-radius: 5px;
         font-size: 1em;
         flex-grow: 1; /* Allow input to grow */
         min-width: 100px; /* Ensure input has minimum width */
     }

     .controls input[type="range"] {
          padding: 0; /* Range input styling is different */
          margin: 0 5px;
          -webkit-appearance: none; /* Override default styles */
          appearance: none;
          background: var(--border-color);
          outline: none;
          height: 8px;
          border-radius: 5px;
     }

     .controls input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: var(--primary-color);
         border-radius: 50%;
         cursor: pointer;
         transition: background 0.3s ease;
     }
      .controls input[type="range"]::-webkit-slider-thumb:hover {
          background: #2980b9; /* Darker primary */
      }

     .controls input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: var(--primary-color);
         border-radius: 50%;
         cursor: pointer;
          transition: background 0.3s ease;
     }
     .controls input[type="range"]::-moz-range-thumb:hover {
         background: #2980b9;
     }


     .custom-length {
         margin-top: 0; /* Adjusted spacing with flex container */
     }
      .custom-length span {
          white-space: nowrap;
      }


    .timeline-container {
        margin-top: 30px;
        margin-bottom: 25px;
        position: relative; /* Needed for labels absolute positioning */
    }

    #timeline {
        position: relative;
        width: 100%;
        height: 20px; /* Timeline height */
        background: linear-gradient(to right, #ecf0f1, #bdc3c7); /* Subtle gradient */
        border-radius: 10px;
        overflow: visible; /* Allow markers outside for text */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px; /* Space below timeline before labels */
    }

    .marker {
        position: absolute;
        top: 0;
        bottom: 0;
        width: 2px; /* Marker line thickness */
        background-color: var(--text-color);
        text-align: center;
        font-size: 0.85em;
        color: var(--note-color);
        padding-top: 25px; /* Position text below timeline */
        box-sizing: border-box;
        transform: translateX(-50%); /* Center marker line */
        line-height: 1.2;
    }

    .start-marker { left: 0; }
    .end-marker { left: 100%; } /* Use left 100% and transform to align */

    /* Points */
     .timeline-point {
         position: absolute;
         top: -5px; /* Extend above timeline */
         bottom: -5px; /* Extend below timeline */
         width: 3px; /* Point line thickness */
         transition: opacity 0.5s ease, transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease;
         cursor: pointer;
         border-radius: 2px;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
     }

    .structure-point {
        background-color: var(--structure-color);
        z-index: 3; /* Above fibonacci and base timeline */
    }

    .fibonacci-point {
        background-color: var(--fibonacci-color);
        z-index: 2; /* Below structure, above timeline */
    }

    /* Highlight for points near each other */
    .timeline-point.highlight-match {
        background-color: var(--highlight-color);
        box-shadow: 0 0 10px var(--highlight-color);
        z-index: 4; /* Bring highlighted points to front */
        transform: scaleX(1.5); /* Slightly wider to emphasize */
    }

    /* Highlight for type selection */
    .timeline-point.highlight-type {
         box-shadow: 0 0 8px rgba(52, 152, 219, 0.8); /* Blue glow for type highlight */
         z-index: 5; /* Even higher */
    }
     .fibonacci-point.highlight-type { background-color: var(--primary-color); } /* Change color slightly */
     .structure-point.highlight-type { background-color: #c0392b; } /* Change color slightly */


    .labels {
        display: flex;
        justify-content: center; /* Center labels */
        gap: 25px;
        margin-top: 20px;
        font-size: 0.95em;
        flex-wrap: wrap; /* Allow wrapping */
    }

    .label {
        display: flex;
        align-items: center;
        gap: 8px;
        cursor: pointer;
        transition: color 0.3s ease;
    }
     .label:hover {
         color: var(--primary-color);
     }


    .label-color-box {
        content: '';
        display: inline-block;
        width: 18px;
        height: 18px;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .structure-color { background-color: var(--structure-color); }
    .fibonacci-color { background-color: var(--fibonacci-color); }
    .highlight-color { background-color: var(--highlight-color); }


    .note {
        font-size: 0.9em;
        color: var(--note-color);
        margin-top: 20px;
        text-align: center;
        line-height: 1.5;
    }


    #toggleExplanation {
        display: block;
        width: 250px;
        margin: 30px auto;
        padding: 12px 20px;
        text-align: center;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #toggleExplanation:hover {
        background-color: #2980b9; /* Darker primary */
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    }

    #toggleExplanation:active {
        transform: scale(0.98);
    }


    #explanation {
        display: none;
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--background-color); /* Different background for contrast */
        direction: rtl;
        text-align: right;
        color: var(--text-color);
        line-height: 1.7;
    }

    #explanation h2, #explanation h3 {
        color: var(--primary-color);
        margin-bottom: 12px;
        font-weight: 600;
    }

    #explanation h2 {
        font-size: 1.6em;
        text-align: center;
        margin-bottom: 20px;
    }

    #explanation h3 {
        font-size: 1.3em;
        margin-top: 20px;
    }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        list-style: disc inside;
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list */
    }

    #explanation li {
        margin-bottom: 8px;
    }

    #explanation a {
         color: var(--primary-color);
         text-decoration: none;
         transition: color 0.3s ease;
    }
     #explanation a:hover {
         text-decoration: underline;
         color: #2980b9;
     }

</style>

<button id="toggleExplanation">הצג הסבר מורחב על הקשר בין מתמטיקה למוזיקה</button>

<div id="explanation">
    <h2>הקסם המתמטי מאחורי המוזיקה: פיבונאצ'י, יחס הזהב ועוד</h2>

    <h3>סדרת פיבונאצ'י ויחס הזהב: מסדרה לפרופורציה האולטימטיבית</h3>
    <p>סדרת פיבונאצ'י, שנקראת על שם המתמטיקאי האיטלקי לאונרדו מפיזה (פיבונאצ'י), מתחילה בפשטות עם 0 ו-1. כל מספר עוקב הוא פשוט סכום שני קודמיו: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, וכך הלאה, לעד. מה שהופך את הסדרה הזו למרתקת באמת הוא היחס בין מספרים עוקבים בה. ככל שמתקדמים בסדרה, היחס בין כל מספר לקודמו (למשל, 13/8, 21/13) מתקרב יותר ויותר לערך קבוע, מיוחד במינו, המכונה 'יחס הזהב' (מסומן באות היוונית φ - פי). ערכו הוא בקירוב 1.6180339887... יחס זה מוגדר גם באופן גיאומטרי: אם מחלקים קטע לשני חלקים כך שהיחס בין הקטע כולו לחלק הגדול שווה ליחס בין החלק הגדול לחלק הקטן, אז הם נמצאים ביחס הזהב. זהו יחס ייחודי היוצר איזון אסתטי.</p>

    <h3>טביעת אצבע מתמטית: הופעת פיבונאצ'י ויחס הזהב בטבע ובאמנות</h3>
    <p>אי אפשר להתעלם מהנוכחות המדהימה של סדרת פיבונאצ'י ויחס הזהב סביבנו. בטבע, הם מופיעים שוב ושוב במבנים אופטימליים ויעילים: בסידור העלים סביב גבעול, בארגון הזרעים בחמנייה או באצטרובל (לרוב בשתי ספירלות בכיוונים שונים, שמספרן הוא מספרי פיבונאצ'י עוקבים!), במבנה הספירלי המושלם של קונכיית הנאוטילוס, ובהתפצלות ענפי עצים. האמנות והאדריכלות אימצו אף הן את הפרופורציות הללו לאורך ההיסטוריה. מיוון העתיקה (בפרתנון?) דרך הרנסנס ועד ימינו, אמנים רבים האמינו שיחס הזהב יוצר הרמוניה ויזואלית ונעימות לעין, ושילבו אותו במודע או שלא במודע בקומפוזיציות ובמבנים שלהם.</p>

    <h3>הקשר המוזיקלי: האם מלחינים חשבו על מתמטיקה?</h3>
    <p>הקשר בין מתמטיקה למוזיקה אינו המצאה מודרנית. כבר פיתגורס היווני הקדום גילה שהרמוניות נעימות (כמו אוקטבה או קווינטה) נוצרות מיחסים פשוטים בין אורכי מיתרים רוטטים (1:2, 2:3). אולם, האם מלחינים השתמשו דווקא בסדרת פיבונאצ'י ויחס הזהב באופן מפורש ושיטתי ביצירותיהם? כאן הדעות חלוקות. רוב המחקרים שמוצאים יחסים אלו ביצירות קלאסיות עושים זאת באמצעות אנליזה רטרוספקטיבית – הם בודקים בדיעבד היכן נמצאות נקודות מבנה מרכזיות (שיא דרמטי, שינוי טמפו, כניסת נושא חדש, סוף קטע) ומחשבים את מיקומן היחסי באורך היצירה. לעיתים קרובות, נקודות אלו נופלות בקירוב לנקודות המוגדרות על ידי יחס הזהב (כ-61.8% או 38.2% מהאורך הכולל) או יחסי פיבונאצ'י מוקדמים יותר (כמו 1:2, 2:3, 3:5, 5:8). ייתכן שמלחינים מסוימים, כמו בארטוק במאה ה-20, שילבו יחסים אלו באופן מודע. אצל אחרים, כמו בטהובן או מוצרט, ייתכן שהשימוש היה אינטואיטיבי, שכן יחסים אלו נעימים לאוזן ולתפיסה, או שאלו פשוט התאמות מקריות שאינן מעידות על כוונה.</p>

    <h3>היכן ניתן למצוא אותם? דוגמאות אנליטיות</h3>
    <ul>
        <li><strong>חלוקת זמן:</strong> הנקודה הדרמטית ביותר או המרכז המבני של פרק סימפוניה ארוך עשויה להופיע בנקודה שהיא כ-61.8% מאורך הפרק הכולל (או כ-38.2% מהסוף). לדוגמה, באנליזות של הסימפוניה החמישית של בטהובן, סוף הרפריזה (חזרת החומר המוזיקלי הראשוני) נמצא לעיתים קרובות קרוב לנקודת יחס הזהב.</li>
        <li><strong>מבנה קטעים קצרים:</strong> ניתן למצוא שימוש במספרי פיבונאצ'י ממש ב"אבני הבניין" של המוזיקה: מספר תיבות בפסוק מוזיקלי, מספר פעימות בחלק קצבי, מספר צלילים במוטיב מלודי, או חלוקה של קטע קצר יותר לשניים או שלושה תת-קטעים שאורכם מתייחס במספרי פיבונאצ'י.</li>
        <li><strong>מרווחים ואקורדים:</strong> ישנם תיאוריות שמקשרות גם יחסים בין תדרי צלילים או מספר הצלילים באקורד לסדרת פיבונאצ'י, אך קשרים אלו מורכבים יותר ופחות מוסכמים.</li>
    </ul>

    <h3>למה זה קורה? הסברים אפשריים לקשר</h3>
    <p>גם אם השימוש לא היה תמיד מודע, מדוע דווקא מבנים מוזיקליים התואמים יחסי פיבונאצ'י ויחס הזהב נשמעים לנו לעיתים קרובות מאוזנים, פרופורציונליים ונעימים? ההסבר כנראה מורכב ורב-גורמי:</p>
    <ul>
        <li><strong>תפיסה קוגניטיבית אנושית:</strong> המוח שלנו רגיל לעבד דפוסים ויחסים שמופיעים באופן תדיר בטבע ובסביבה החזותית שלנו. ייתכן שהיכרות (לא מודעת) זו עם יחסי הזהב והפיבונאצ'י גורמת לנו להגיב אליהם בחיוב גם בעולם השמע.</li>
        <li><strong>איזון אסתטי:</strong> יחס הזהב מייצג איזון ייחודי - הוא אינו סימטריה מושלמת (שעלולה להיות סטטית ומשעממת), אך גם אינו אסימטריה פרועה. זהו איזון דינמי, "אסימטריה מאוזנת" שרבים מוצאים אותה מושכת מבחינה ויזואלית ואולי גם שמיעתית.</li>
        <li><strong>פשטות ויעילות:</strong> סדרת פיבונאצ'י מייצגת לעיתים קרובות את הדרך היעילה ביותר למלא מרחב או להתפצל (כמו בעלי כותרת או ענפים). ייתכן שעקרונות היעילות והפשטות הללו מתבטאים גם במבנים זמניים במוזיקה ונשמעים טבעיים ונעימים לאוזן.</li>
    </ul>
    <p>חשוב לזכור שמוזיקה היא בראש ובראשונה ביטוי אומנותי ורגשי. אנליזה מתמטית יכולה לשפוך אור על חלק מהמבנים הבסיסיים שלה, אך היא אינה מסבירה את מלוא העושר והמורכבות של החוויה המוזיקלית.</p>

    <h3>מעבר לפיבונאצ'י: העולם המתמטי של המוזיקה</h3>
    <p>פיבונאצ'י ויחס הזהב הם רק דוגמה אחת לקשר העמוק בין מתמטיקה למוזיקה. הקשר קיים בכל רמה:</p>
    <ul>
        <li><strong>הרמוניה טבעית:</strong> הצלילים העיליים (אוברטונים) שמרכיבים כל צליל בסיסי יוצרים סדרה הרמונית המבוססת לחלוטין על יחסים פשוטים בין מספרים שלמים (1:1 - יוניסון, 1:2 - אוקטבה, 2:3 - קווינטה, 3:4 - קוורטה). יחסים אלו הם הבסיס האקוסטי להרמוניות שאנו מוצאים נעימות לאוזן.</li>
        <li><strong>מבנה סולמות:</strong> חלוקת האוקטבה בסולמות המוזיקליים המערביים (למשל, 12 חצאי טונים במזג שווה) היא חלוקה לוגריתמית מדויקת, בה כל חצי טון הוא כפול של השורש ה-12 של 2 מתדר הצליל הקודם.</li>
        <li><strong>קצב ומשקל:</strong> מבנים ריתמיים ומשקלים (כמו 4/4 או 3/4) מבוססים על חלוקות מתמטיות מדויקות של זמן ופעימות.</li>
    </ul>
    <p>המוזיקה, אם כן, היא שילוב מרתק של פיזיקה, מתמטיקה, פסיכולוגיה אנושית וביטוי יצירתי. האנליזה המתמטית רק מגלה עוד שכבה של יופי וסדר עמוק ביצירות שנשמעות לנו לעיתים פשוט יפהפיות.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const timeline = document.getElementById('timeline');
        const musicPieceSelect = document.getElementById('music-piece');
        const customLengthDiv = document.querySelector('.custom-length');
        const totalLengthInput = document.getElementById('total-length');
        const lengthValueSpan = document.getElementById('length-value');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');
        const fibonacciPointsDiv = document.createElement('div'); // Use a single container for points
        const structurePointsDiv = document.createElement('div');
        const labelsContainer = document.querySelector('.labels');
        const structureLabel = document.querySelector('.structure-label');
        const fibonacciLabel = document.querySelector('.fibonacci-label');
        const highlightLabel = document.querySelector('.highlight-label');


        // Append point containers to timeline
        fibonacciPointsDiv.id = 'fibonacci-golden-points';
        structurePointsDiv.id = 'music-structure-points';
        timeline.appendChild(fibonacciPointsDiv);
        timeline.appendChild(structurePointsDiv);


        // Define Golden Ratio (Phi)
        const phi = (1 + Math.sqrt(5)) / 2;
        const phiRatio = 1 / phi; // Approx 0.618
        const phiComplement = 1 - phiRatio; // Approx 0.382

        // Define relevant Fibonacci and Golden Ratio points as percentages (0 to 100)
        // Based on ratios like Fib(n-1)/Fib(n) or 1-Fib(n-1)/Fib(n)
        const baseRatios = [
            phiRatio,       // Golden Ratio (approx 0.618)
            phiComplement,  // 1 - Golden Ratio (approx 0.382)
            1/3, 2/3,       // Simple thirds
            0.5,            // Midpoint
            2/5, 3/5,       // 0.4, 0.6
            3/8, 5/8,       // 0.375, 0.625
            5/13, 8/13,     // approx 0.385, 0.615
             8/21, 13/21,    // approx 0.381, 0.619
        ];

        // Calculate unique percentages and sort them
        const fibonacciGoldenPercentages = [...new Set(baseRatios.map(ratio => (ratio * 100).toFixed(1)).map(Number))].sort((a, b) => a - b);


        // Example structure points for selected music pieces (as percentages)
        // These are simplified examples for visualization purposes based on common analyses
        const musicStructures = {
            'beethoven_5_1': [
                { name: 'סוף אקספוזיציה (קרוב ל-40%)', percent: 40 },
                { name: 'תחילת רפריזה (קרוב ל-62%)', percent: 63 }, // Adjusted slightly closer to 0.618
                { name: 'שיא דרמטי', percent: 75 },
                { name: 'תחילת קודה', percent: 80 }
            ],
            'mozart_40_1': [
                { name: 'סוף אקספוזיציה', percent: 45 },
                { name: 'תחילת רפריזה (קרוב ל-62%)', percent: 68 }, // Adjusted slightly closer to 0.618
                { name: 'שיא', percent: 78 }
            ],
            'debussy_clair_de_lune': [
                 { name: 'חלק א (קרוב ל-38%)', percent: 38 },
                 { name: 'כניסת נושא חדש (קרוב ל-62%)', percent: 62 },
                 { name: 'חלק א חזרה', percent: 80 },
                 { name: 'קודה', percent: 90 }
             ],
            'custom': [] // No predefined points for custom length
        };

        // Threshold for considering points "near" each other (in percentage points)
        const highlightThresholdPercent = 1.8; // e.g., within 1.8% difference

        function updateTimeline() {
            const timelineWidth = timeline.offsetWidth;

            // Clear previous points
            fibonacciPointsDiv.innerHTML = '';
            structurePointsDiv.innerHTML = '';
             highlightLabel.style.display = 'none'; // Hide highlight label by default

            const selectedPiece = musicPieceSelect.value;
            const currentStructurePoints = musicStructures[selectedPiece];

            // Add Fibonacci/Golden Ratio points
            fibonacciGoldenPercentages.forEach(percent => {
                const position = (percent / 100) * timelineWidth;
                const pointDiv = document.createElement('div');
                pointDiv.classList.add('timeline-point', 'fibonacci-point');
                pointDiv.style.left = `${position}px`;
                pointDiv.title = `${percent.toFixed(1)}% (פיבונאצ'י/יחס הזהב)`; // Tooltip
                pointDiv.dataset.percent = percent.toFixed(1);
                 pointDiv.dataset.type = 'fibonacci';
                fibonacciPointsDiv.appendChild(pointDiv);

                 // Simple fade-in animation
                 pointDiv.style.opacity = 0;
                 requestAnimationFrame(() => { // Use rAF to ensure element is in DOM
                     setTimeout(() => {
                         pointDiv.style.opacity = 1;
                         pointDiv.style.transform = 'translateY(0)'; // Ensure transform is reset if used for animation
                     }, 10); // Small staggered delay
                 });
            });

            // Add Music Structure points if piece is selected
            if (selectedPiece !== 'custom') {
                currentStructurePoints.forEach(point => {
                    const position = (point.percent / 100) * timelineWidth;
                    const pointDiv = document.createElement('div');
                    pointDiv.classList.add('timeline-point', 'structure-point');
                    pointDiv.style.left = `${position}px`;
                    pointDiv.title = `${point.name} - ${point.percent.toFixed(1)}%`; // Tooltip
                    pointDiv.dataset.percent = point.percent.toFixed(1);
                     pointDiv.dataset.type = 'structure';
                    structurePointsDiv.appendChild(pointDiv);

                     // Simple fade-in animation
                     pointDiv.style.opacity = 0;
                     requestAnimationFrame(() => {
                         setTimeout(() => {
                            pointDiv.style.opacity = 1;
                            pointDiv.style.transform = 'translateY(0)';
                         }, 10); // Small staggered delay
                     });
                });
            }

            // Highlight nearby points (check structure vs fibonacci)
            let foundMatch = false;
            const structureElements = structurePointsDiv.querySelectorAll('.timeline-point');
            const fibonacciElements = fibonacciPointsDiv.querySelectorAll('.timeline-point');

            structureElements.forEach(structEl => {
                const structPercent = parseFloat(structEl.dataset.percent);
                fibonacciElements.forEach(fibEl => {
                    const fibPercent = parseFloat(fibEl.dataset.percent);
                    if (Math.abs(structPercent - fibPercent) <= highlightThresholdPercent) {
                        structEl.classList.add('highlight-match');
                        fibEl.classList.add('highlight-match');
                        foundMatch = true;
                    }
                });
            });

             if(foundMatch) {
                 highlightLabel.style.display = 'flex'; // Show highlight label
             }
        }

        // --- Event Listeners ---

        // Event listener for music piece selection
        musicPieceSelect.addEventListener('change', (event) => {
            const selectedPiece = event.target.value;
            if (selectedPiece === 'custom') {
                customLengthDiv.style.display = 'flex';
                 // Update timeline based on current slider value when switching to custom
                 updateTimeline(); // Length value doesn't change pixel position, percentages are relative
            } else {
                customLengthDiv.style.display = 'none';
                 // Update timeline for predefined piece (always treated as 100% length)
                updateTimeline();
            }
             // Remove type highlights when changing piece
             document.querySelectorAll('.highlight-type').forEach(el => el.classList.remove('highlight-type'));
        });

        // Event listener for custom length slider (only updates the displayed value and triggers timeline redraw)
        totalLengthInput.addEventListener('input', (event) => {
            const length = event.target.value;
            lengthValueSpan.textContent = length;
             // The updateTimeline function uses the current timeline width,
             // so changing the 'length' value here is just for display in the custom mode.
             // The percentage calculation remains relative to the visual timeline width.
             // No need to call updateTimeline here just for the number display.
             // If we wanted the timeline *visual length* to change, that would be different,
             // but the prompt implies keeping the technical structure, which means the timeline
             // div likely has a fixed or max-width.
        });
         // Re-draw on slider *change* or *mouseup* if visual recalculation was needed,
         // but since it's percentages, only the initial load and resize matter for geometry.
         // The 'input' listener is sufficient for the value display.

        // Event listener for explanation toggle button
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            if (isHidden) {
                explanationDiv.style.display = 'block';
                toggleExplanationButton.textContent = 'הסתר הסבר מורחב';
            } else {
                explanationDiv.style.display = 'none';
                toggleExplanationButton.textContent = 'הצג הסבר מורחב על הקשר בין מתמטיקה למוזיקה';
            }
             // Optional: Scroll to the explanation section
             if(isHidden) {
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

        // Event listeners for label clicks to highlight points of that type
        structureLabel.addEventListener('click', () => {
            document.querySelectorAll('.structure-point').forEach(el => el.classList.toggle('highlight-type'));
            // Remove highlight from other type
            document.querySelectorAll('.fibonacci-point').forEach(el => el.classList.remove('highlight-type'));
        });

        fibonacciLabel.addEventListener('click', () => {
             document.querySelectorAll('.fibonacci-point').forEach(el => el.classList.toggle('highlight-type'));
             // Remove highlight from other type
             document.querySelectorAll('.structure-point').forEach(el => el.classList.remove('highlight-type'));
        });


         // Handle window resize to update marker positions
         let resizeTimer;
         window.addEventListener('resize', () => {
             clearTimeout(resizeTimer);
             resizeTimer = setTimeout(updateTimeline, 100); // Debounce resize
         });

         // --- Initial Setup ---

         // Initial state of custom length input based on default select value
         if (musicPieceSelect.value === 'custom') {
             customLengthDiv.style.display = 'flex';
             lengthValueSpan.textContent = totalLengthInput.value; // Set initial value display
         }

         // Initial render after DOM is ready and layout is calculated
         requestAnimationFrame(() => {
             updateTimeline();
         });

    });
</script>
```