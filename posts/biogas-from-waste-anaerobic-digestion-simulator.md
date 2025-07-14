---
title: "ביוגז מהפסולת: סימולטור בלב הדייג'סטר"
english_slug: biogas-from-waste-anaerobic-digestion-simulator
category: "מדעי הסביבה / הנדסה סביבתית"
tags: [ביוגז, תסיסה אנאירובית, אנרגיה מתחדשת, טיפול בפסולת, קיימות]
---
# ביוגז מהפסולת: סימולטור בלב הדייג'סטר

דמיינו עולם שבו כל שארית מזון הופכת לאנרגיה נקייה! תהליך התסיסה האנאירובית הוא קסם ביולוגי שהופך את זה למציאות, אבל הוא דורש איזון עדין של תנאים. האם יש לך את מה שנדרש כדי להפעיל דייג'סטר ביוגז בהצלחה? צלול לתוך הסימולטור וגלה!

<div class="simulator-container">
    <div class="controls">
        <h3>מפקדת הדייג'סטר</h3>
        <p>בחר את חומר הגלם והגדר את תנאי הפעולה כדי להפעיל את הדייג'סטר שלך.</p>
        <div class="control-group">
            <label for="material">חומר הגלם:</label>
            <select id="material" aria-label="בחר סוג חומר גלם">
                <option value="organic_waste">פסולת אורגנית עירונית</option>
                <option value="sludge">בוצה ממתקני שפכים</option>
                <option value="animal_manure">זבל בעלי חיים</option>
                <option value="energy_crops">גידולי אנרגיה יעודיים</option>
            </select>
        </div>
        <div class="control-group">
            <label>טמפרטורת עבודה:</label><br>
            <input type="radio" id="mesophilic" name="temperature" value="mesophilic" checked aria-label="מצב מזופילי">
            <label for="mesophilic">מזופילית (30-40°C) - יציב יותר</label><br>
            <input type="radio" id="thermophilic" name="temperature" value="thermophilic" aria-label="מצב תרמופילי">
            <label for="thermophilic">תרמופילית (50-60°C) - מהיר יותר, רגיש יותר</label>
        </div>
        <div class="control-group">
            <label for="olr">קצב הזנה (OLR): <span id="olr-value">5</span></label>
            <input type="range" id="olr" min="1" max="10" value="5" aria-label="בחר קצב הזנה">
            <p class="control-hint">ככל שקצב ההזנה גבוה יותר, כך פוטנציאל הייצור גדל, אך גם הסיכון לקריסה.</p>
        </div>
        <div class="button-group">
            <button id="start-sim" class="sim-button start">התחל מחזור</button>
            <button id="stop-sim" class="sim-button stop" disabled>עצור</button>
            <button id="reset-sim" class="sim-button reset">אפס הכל</button>
        </div>
    </div>
    <div class="results">
        <h3>מצב הדייג'סטר</h3>
        <div class="digester-visual">
            <div class="biogas-bubble"></div>
            <div class="biogas-bubble delay-1"></div>
            <div class="biogas-bubble delay-2"></div>
             <div class="digester-text">פעיל</div>
        </div>
        <div id="sim-time" class="result-item">זמן סימולציה: יום 0</div>
        <div id="total-biogas" class="result-item">סה"כ ביוגז מיוצר: 0.00 מ"ק</div>
        <div id="methane-percent" class="result-item">אחוז מתאן בביוגז: --%</div>
        <div id="current-ph" class="result-item">pH נוכחי בתא: --</div>

        <div class="status-indicators">
             <div class="status-indicator good" id="status-biogas"><i class="icon">💡</i> ייצור ביוגז</div>
             <div class="status-indicator good" id="status-ph"><i class="icon">💧</i> pH</div>
             <div class="status-indicator good" id="status-stability"><i class="icon">⚙️</i> יציבות תהליך</div>
        </div>
         <p class="status-message" id="overall-status-message">הדייג'סטר מוכן להתחלה. בחר הגדרות והתחל.</p>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">🤔 מה בדיוק קורה כאן? הסבר על תהליך התסיסה האנאירובית</button>
<div id="explanation" style="display: none;">
    <h2>📘 סוד הביוגז: מסע בתוך הדייג'סטר האנאירובי</h2>

    <h3>ביוגז ותסיסה אנאירובית - הקדמה קצרה</h3>
    דמיינו מיכל סגור, חשוך וללא אוויר. בתוך המיכל הזה, המכונה דייג'סטר, קהילה תוססת של מיקרואורגניזמים (חיידקים וארכאונים) עובדת מסביב לשעון. המשימה שלהם: לפרק חומרים אורגניים מורכבים ולהפוך אותם לתערובת גזים בעלי ערך - הביוגז! הביוגז מורכב בעיקר ממתאן (CH<sub>4</sub>), שהוא דלק יקר ערך, ומפחמן דו-חמצני (CO<sub>2</sub>). התהליך הביולוגי המופלא הזה נקרא תסיסה אנאירובית (Anaerobic Digestion - AD).

    <h3>המסע המיקרוביאלי: ארבעת השלבים של הפירוק</h3>
    התסיסה האנאירובית אינה תהליך חד-שלבי, אלא סדרה של שלבים המבוצעים על ידי קבוצות שונות של "עובדים זעירים" החיים בדייג'סטר ופועלים בשיתוף פעולה מורכב (סינרגיה). כל שלב מכין את החומר לשלב הבא:
    <ol>
        <li>**הידרוליזה (Hydrolysis):** השלב הראשון, שבו "מפרקי הענק" (אנזימים שמפרישים החיידקים) שוברים מולקולות אורגניות מורכבות (כמו חלבונים ארוכים, פחמימות מורכבות ושומנים) ל"אבני בניין" קטנות ופשוטות יותר (חומצות אמינו, סוכרים פשוטים, חומצות שומן). רק לאחר השלב הזה, החומר "אכיל" לשאר המיקרואורגניזמים.</li>
        <li>**אסידוגנזה (Acidogenesis):** בשלב זה, "יצרני החומצות" (חיידקים אסידוגניים) לוקחים את אבני הבניין הפשוטות מההידרוליזה והופכים אותן לחומצות אורגניות קצרות שרשרת (כמו חומצה אצטית - החומצה בחומץ, חומצה פרופיונית, חומצה בוטירית), לצד אלכוהולים, מימן (H<sub>2</sub>) ופחמן דו-חמצני (CO<sub>2</sub>). שלב זה פעיל מאוד ויכול להוביל לירידה ב-pH של הנוזל בדייג'סטר אם לא יטופל.</li>
        <li>**אצטוגנזה (Acetogenesis):** כאן נכנסים לפעולה "אצטט-מייקרים" (חיידקים אצטוגניים), שמפרקים את החומצות והאלכוהולים שנוצרו באסידוגנזה, ומייצרים בעיקר חומצה אצטית (Acetate), מימן ופחמן דו-חמצני. שלב זה "תקוע" אם יש יותר מדי מימן; לכן, הוא תלוי באופן קריטי בכך שקבוצת המיקרואורגניזמים הבאה תצרוך מימן במהירות.</li>
        <li>**מתנוגנזה (Methanogenesis):** השלב הסופי והמכריע, המבוצע על ידי "מייצרי המתאן" (מתנוגנים - שהם ארכאונים, לא חיידקים אמיתיים!). הם הופכים את התוצרים הסופיים של השלבים הקודמים – בעיקר חומצה אצטית, מימן ופחמן דו-חמצני – לביוגז: המון מתאן וקצת פחמן דו-חמצני. המתנוגנים הם החוליה הרגישה ביותר בשרשרת, ותנאי סביבה שאינם אופטימליים, במיוחד pH נמוך מדי או טמפרטורה לא יציבה, עלולים לפגוע בהם קשות ולגרום ל"קריסת" התהליך ולירידה דרסטית בייצור הביוגז (ובפרט המתאן).</li>
    </ol>

    <h3>חומרי גלם: המזון של הדייג'סטר</h3>
    כמעט כל חומר אורגני יכול לעבור תסיסה אנאירובית! ה"מזון" הפופולרי ביותר כולל:
    <ul>
        <li>פסולת אורגנית שמגיעה מהבתים ומהמסעדות (שאריות מזון).</li>
        <li>בוצה הנוצרת במתקני טיהור שפכים.</li>
        <li>זבל מחוות בעלי חיים (בקר, לולים, חזירים).</li>
        <li>שאריות גידולים חקלאיים ופסולת ממפעלי מזון.</li>
        <li>גידולים שזרעו במיוחד לצורך הפקת אנרגיה (למשל, זנים מסוימים של תירס).</li>
    </ul>
    איכות חומר הגלם (למשל, יחס פחמן-חנקן C:N מאוזן) והרכבו משפיעים מאוד על יעילות התהליך וכמות הביוגז שיתקבל.

    <h3>הפרמטרים שחייבים לשלוט בהם (המפתחות להצלחה בסימולטור!)</h3>
    כדי שהקהילה המיקרוביאלית בדייג'סטר תעבוד ביעילות ובאושר, יש לשמור על תנאים אופטימליים. הסימולטור מתמקד בכמה מהחשובים ביותר:
    <ul>
        <li>**טמפרטורה:** ישנם שני "בתי גידול" מועדפים למיקרואורגניזמים:
            <ul>
                <li>*מזופילי (30-40°C):* טווח טמפרטורה נפוץ ויחסית יציב. התהליך מעט איטי יותר, אך הקהילה המיקרוביאלית עמידה יותר לשינויים.</li>
                <li>*תרמופילי (50-60°C):* טווח חם יותר, המאיץ את תהליך הפירוק ויכול להביא לייצור ביוגז גבוה יותר. עם זאת, הקהילה רגישה יותר לשינויי טמפרטורה ו-pH, והתהליך פחות יציב. יתרון נוסף לטמפרטורה תרמופילית הוא חיסול טוב יותר של פתוגנים.</li>
            </ul>
        </li>
        <li>**pH (חומציות/בסיסיות):** המתנוגנים, החוליה החשובה ביותר לייצור מתאן, מאושרים בעיקר בטווח pH ניטרלי עד בסיסי קל (6.5-8). אם ה-pH יורד נמוך מדי (למשל בגלל הצטברות חומצות משלבי האסידוגנזה כאשר קצב ההזנה גבוה מדי או כשיש בעיה במתנוגנים), ייצור המתאן ייפגע קשות והתהליך עלול לקרוס. בסימולטור תראה איך שינוי ה-pH משפיע דרמטית על הביצועים!</li>
        <li>**קצב הזנה (OLR - Organic Loading Rate):** כמה "מזון" אורגני מכניסים לדייג'סטר ביחס לנפחו, ביום. OLR גבוה מדי מכניס יותר מדי חומר שמתפרק מהר לשלב החומצי (אסידוגנזה), ועלול להציף את המערכת ולגרום לירידת pH וקריסה לפני שהמתנוגנים מספיקים להפוך הכל למתאן. בסימולטור, שליטה ב-OLR היא קריטית!</li>
        <li>**מעכבים:** חומרים מסוימים (כמו אמוניה בריכוזים גבוהים, סולפידים, מתכות כבדות, אנטיביוטיקה) יכולים להפריע לפעילות המיקרוביאלית ולעכב או לעצור את התהליך. (בסימולטור הנוכחי אנו לא מתמודדים עם מעכבים, אך במציאות זהו גורם חשוב).</li>
    </ul>

    <h3>המוצרים של התסיסה: לא רק ביוגז!</h3>
    *   **ביוגז:** האוצר! ניתן לשרוף אותו להפקת חשמל וחום, לשדרג אותו לגז טבעי לכל דבר (ביומתאן) ולהזריק לרשת הגז, או להשתמש בו כדלק לתחבורה.
    *   **דיג'סטט (Digestate):** החומר שנשאר בדייג'סטר לאחר שהתהליך הסתיים. זהו לא "זבל", אלא דשן אורגני מעולה! הוא עשיר בנוטריינטים (חנקן, זרחן, אשלגן) בצורה זמינה יותר לצמחים לעומת חומר הגלם המקורי, ויכול להחליף דשנים כימיים, מה שתורם לכלכלה מעגלית בתחום החקלאות.

    <h3>לסיכום: יתרונות ואתגרים</h3>
    הפקת ביוגז היא טכנולוגיה מנצחת בהיבטים רבים: היא מייצרת אנרגיה מתחדשת, מטפלת בפסולת אורגנית, מפחיתה פליטות מזיקות (כמו מתאן ממזבלות), ומייצרת דשן איכותי. עם זאת, הקמה ותפעול של מתקני ביוגז דורשים ידע, השקעה כלכלית, וניטור קפדני של התהליך כדי למנוע קריסות.

    עכשיו שאתה מבין את העקרונות, חזור לסימולטור ובדוק כיצד הגדרות שונות משפיעות על בריאות הדייג'סטר ותפוקת הביוגז!
</div>

<style>
    /* Overall Layout and Containers */
    .simulator-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        margin-bottom: 30px;
        padding: 30px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background: linear-gradient(to bottom right, #f0f0f0, #e0e0e0);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        direction: rtl; /* Ensure RTL layout */
        text-align: right;
        font-family: 'Arial', sans-serif; /* Consistent font */
        color: #333;
    }

    .controls, .results {
        flex: 1;
        min-width: 300px; /* Slightly larger minimum width */
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    /* Headings */
    .controls h3, .results h3 {
        color: #2c3e50; /* Dark blue/grey */
        border-bottom: 2px solid #3498db; /* Bright blue underline */
        padding-bottom: 10px;
        margin-bottom: 20px;
        font-size: 1.5em;
    }
    .controls p {
        margin-bottom: 20px;
        color: #555;
    }

    /* Control Groups */
    .control-group {
        margin-bottom: 25px; /* More space */
    }

    .control-group label {
        display: block;
        margin-bottom: 8px; /* More space */
        font-weight: bold;
        color: #555;
        font-size: 1.1em;
    }
     .control-group select,
     .control-group input[type="range"] {
         padding: 10px;
         border: 1px solid #ccc;
         border-radius: 5px;
         font-size: 1em;
         box-sizing: border-box; /* Include padding and border in element's total width and height */
     }
    .control-group select {
         width: 100%; /* Full width */
         background-color: #f9f9f9;
         cursor: pointer;
    }


    .control-group input[type="range"] {
        width: 100%;
        margin-top: 5px;
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 8px;
        background: #ddd;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #3498db;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #3498db;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .control-hint {
        font-size: 0.9em;
        color: #777;
        margin-top: 8px;
        line-height: 1.4;
    }


    /* Radio Buttons */
    .control-group input[type="radio"] {
        margin-left: 5px; /* Space between radio and label */
    }
     .control-group label[for="mesophilic"],
     .control-group label[for="thermophilic"] {
         display: inline-block; /* Align label next to radio */
         font-weight: normal;
         margin-bottom: 0;
         cursor: pointer;
     }
     .control-group label[for="thermophilic"] {
         margin-right: 15px; /* Space between radio groups */
     }


    /* Buttons */
    .button-group {
        margin-top: 30px;
        display: flex; /* Align buttons in a row */
        gap: 15px; /* Space between buttons */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .sim-button {
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        flex-grow: 1; /* Allow buttons to grow and fill space */
        text-align: center;
    }

    .sim-button.start { background-color: #2ecc71; color: white; } /* Green */
    .sim-button.stop { background-color: #e74c3c; color: white; } /* Red */
    .sim-button.reset { background-color: #f39c12; color: white; } /* Orange */

    .sim-button:hover:not(:disabled) {
        opacity: 0.9;
    }

    .sim-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.6;
    }

    /* Results Section */
    .results {
        display: flex;
        flex-direction: column;
        align-items: center; /* Center results content */
    }
    .result-item {
        margin-bottom: 10px;
        font-size: 1.2em;
        color: #555;
        width: 100%; /* Ensure text items take full width */
        text-align: center; /* Center text */
    }

    /* Digester Visual */
    .digester-visual {
        width: 150px;
        height: 150px;
        background-color: #a0a0a0; /* Default grey */
        border-radius: 50%; /* Circle shape */
        margin: 20px auto; /* Center circle */
        position: relative;
        overflow: hidden; /* Hide bubbles outside */
        border: 5px solid #777;
        transition: background-color 0.8s ease; /* Smooth color transition */
         display: flex;
         justify-content: center;
         align-items: center;
         color: white;
         font-size: 1.2em;
         font-weight: bold;
         text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    /* Biogas bubbles animation */
    .biogas-bubble {
        position: absolute;
        bottom: 0;
        width: 10px;
        height: 10px;
        background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white */
        border-radius: 50%;
        opacity: 0;
        animation: bubble-up 3s infinite ease-in-out;
    }

    .biogas-bubble:nth-child(1) { left: 20%; }
    .biogas-bubble:nth-child(2) { left: 50%; animation-delay: 1s; } /* Stagger animation */
    .biogas-bubble:nth-child(3) { left: 80%; animation-delay: 2s; }

    @keyframes bubble-up {
        0% { bottom: 0; opacity: 0; transform: scale(0.5); }
        50% { opacity: 1; }
        100% { bottom: 100%; opacity: 0; transform: scale(1.2); }
    }
     .digester-visual.active .biogas-bubble {
         opacity: 0.8; /* Bubbles are visible when active */
         animation-play-state: running;
     }
      .digester-visual .digester-text {
          z-index: 1; /* Ensure text is above bubbles */
      }

    /* Status Indicators */
    .status-indicators {
        display: flex;
        gap: 15px; /* More space */
        margin-top: 25px;
        flex-wrap: wrap;
        justify-content: center; /* Center indicators */
        width: 100%;
    }

    .status-indicator {
        padding: 8px 15px; /* More padding */
        border-radius: 20px; /* Pill shape */
        font-size: 1em;
        color: white;
        text-align: center;
        min-width: 90px; /* Wider pills */
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: background-color 0.5s ease; /* Smooth color change */
        display: flex;
        align-items: center;
        justify-content: center;
    }
     .status-indicator .icon {
         margin-left: 8px; /* Space between icon and text */
         font-size: 1.1em;
     }


    .status-indicator.good { background-color: #2ecc71; } /* Green */
    .status-indicator.warning { background-color: #f39c12; } /* Orange */
    .status-indicator.danger { background-color: #e74c3c; } /* Red */

    .status-message {
        margin-top: 20px;
        text-align: center;
        font-size: 1.1em;
        color: #34495e;
        min-height: 1.5em; /* Reserve space to prevent layout shifts */
    }
     .status-message.warning { color: #f39c12; font-weight: bold; }
     .status-message.danger { color: #e74c3c; font-weight: bold; animation: pulse-red 1s infinite; }

     @keyframes pulse-red {
         0% { box-shadow: 0 0 0 0 rgba(231, 76, 60, 0.7); }
         70% { box-shadow: 0 0 0 10px rgba(231, 76, 60, 0); }
         100% { box-shadow: 0 0 0 0 rgba(231, 76, 60, 0); }
     }


    /* Explanation Section */
    .toggle-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #3498db; /* Bright blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 25px; /* More space */
        text-align: center;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .toggle-button:hover {
        background-color: #2980b9; /* Darker blue */
    }

    #explanation {
        margin-top: 25px;
        padding: 25px;
        border: 1px solid #dcdcdc;
        border-radius: 10px;
        background-color: #f9f9f9;
        direction: rtl;
        text-align: right;
        line-height: 1.7; /* Improved readability */
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: #2c3e50;
        margin-bottom: 15px;
        border-bottom: 1px dotted #ccc;
        padding-bottom: 5px;
    }

    #explanation h2 {
        font-size: 1.8em;
    }
    #explanation h3 {
        font-size: 1.4em;
    }


    #explanation p, #explanation ul, #explanation ol {
        margin-bottom: 15px;
    }

    #explanation ul, #explanation ol {
        padding-right: 25px; /* More indentation */
    }

    #explanation li {
        margin-bottom: 8px;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .simulator-container {
            flex-direction: column; /* Stack columns */
            gap: 20px;
            padding: 15px;
        }
        .controls, .results {
            padding: 15px;
        }
        .button-group {
            flex-direction: column; /* Stack buttons */
            gap: 10px;
        }
        .sim-button {
            flex-grow: 0; /* Don't force grow when stacked */
            width: 100%;
        }
         .status-indicators {
            gap: 10px;
         }
         .status-indicator {
             min-width: unset; /* Allow width to be content-driven */
             padding: 8px 10px;
         }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const materialSelect = document.getElementById('material');
        const tempRadios = document.querySelectorAll('input[name="temperature"]');
        const olrRange = document.getElementById('olr');
        const olrValueSpan = document.getElementById('olr-value');
        const startBtn = document.getElementById('start-sim');
        const stopBtn = document.getElementById('stop-sim');
        const resetBtn = document.getElementById('reset-sim');

        const simTimeDiv = document.getElementById('sim-time');
        const totalBiogasDiv = document.getElementById('total-biogas');
        const methanePercentDiv = document.getElementById('methane-percent');
        const currentPhDiv = document.getElementById('current-ph');

        const statusBiogas = document.getElementById('status-biogas');
        const statusPh = document.getElementById('status-ph');
        const statusStability = document.getElementById('status-stability');
        const overallStatusMessage = document.getElementById('overall-status-message');

        const digesterVisual = document.querySelector('.digester-visual');

        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let simulationInterval = null;
        let simDay = 0;
        let totalBiogas = 0;
        let currentPh = 7.2; // Starting pH
        let currentMethane = 0; // Will be set based on material
        let dailyBiogasRate = 0; // Keep track of daily rate for status

        const params = {
            materials: {
                organic_waste: {
                    baseYieldFactor: 0.2, // Relative yield per unit OLR m3/kg_organic/day approx
                    methanePercent: 60,
                    bufferCapacity: 6, // Resistance to pH drop (1-10, 10 is high)
                    pH_impact_base: 0.15 // How much OLR stress impacts pH drop potential
                },
                sludge: {
                    baseYieldFactor: 0.15,
                    methanePercent: 55,
                    bufferCapacity: 8,
                    pH_impact_base: 0.1
                },
                animal_manure: {
                    baseYieldFactor: 0.1,
                    methanePercent: 58,
                    bufferCapacity: 9,
                    pH_impact_base: 0.08
                },
                 energy_crops: {
                    baseYieldFactor: 0.3,
                    methanePercent: 62,
                    bufferCapacity: 5,
                    pH_impact_base: 0.2
                }
            },
            temperatures: {
                mesophilic: {
                    speedFactor: 1.0,
                    stabilityFactor: 1.2 // Higher means more resistant to pH swings
                },
                thermophilic: {
                    speedFactor: 1.3,
                    stabilityFactor: 0.8 // Lower means more sensitive to pH swings
                }
            },
            ph: {
                initial: 7.2,
                optimalMin: 6.9, // Slightly adjusted optimal range
                warningThreshold: 6.5,
                crashThreshold: 6.0,
                recoveryRate: 0.03 // pH points per day tendency towards initial/optimal
            },
            simulation: {
                intervalMs: 200, // Time step in milliseconds (slower for clarity)
                 maxDays: 180 // Simulate up to 180 days
            }
        };

        function getSelectedMaterial() {
            return params.materials[materialSelect.value];
        }

        function getSelectedTemperature() {
            const selectedTemp = document.querySelector('input[name="temperature"]:checked').value;
            return params.temperatures[selectedTemp];
        }

        function updateOlrValueDisplay() {
            olrValueSpan.textContent = olrRange.value;
        }

        function updateDisplay() {
            simTimeDiv.textContent = `זמן סימולציה: יום ${simDay}`;
            totalBiogasDiv.textContent = `סה"כ ביוגז מיוצר: ${totalBiogas.toFixed(2)} מ"ק`;
            methanePercentDiv.textContent = `אחוז מתאן בביוגז: ${currentMethane.toFixed(1)}%`;
            currentPhDiv.textContent = `pH נוכחי בתא: ${currentPh.toFixed(2)}`;

            // Update status indicators and messages
            updateStatusIndicators();
            updateDigesterVisual();
            updateOverallStatusMessage();
        }

         function updateStatusIndicators() {
             // Reset classes
             statusBiogas.className = 'status-indicator';
             statusPh.className = 'status-indicator';
             statusStability.className = 'status-indicator';

             // pH Status
             if (currentPh >= params.ph.optimalMin) {
                 statusPh.classList.add('good');
             } else if (currentPh >= params.ph.warningThreshold) {
                 statusPh.classList.add('warning');
             } else {
                 statusPh.classList.add('danger');
             }

             // Stability Status (based on pH and recent changes/tendency)
             // Simplified: Use pH as primary stability indicator
             if (currentPh >= params.ph.optimalMin) {
                 statusStability.classList.add('good');
             } else if (currentPh >= params.ph.warningThreshold) {
                 statusStability.classList.add('warning');
             } else {
                 statusStability.classList.add('danger');
             }

             // Biogas Production Status (based on recent rate and pH)
             // Assume good production when pH is good
             if (currentPh >= params.ph.optimalMin && dailyBiogasRate > (getSelectedMaterial().baseYieldFactor * parseInt(olrRange.value) * getSelectedTemperature().speedFactor * 0.5)) { // Require at least 50% of potential when pH is good
                 statusBiogas.classList.add('good');
             } else if (currentPh >= params.ph.warningThreshold && dailyBiogasRate > (getSelectedMaterial().baseYieldFactor * parseInt(olrRange.value) * getSelectedTemperature().speedFactor * 0.2)) { // Require at least 20% when pH is warning
                 statusBiogas.classList.add('warning');
             } else {
                 statusBiogas.classList.add('danger'); // Very low or zero production
             }
         }

         function updateDigesterVisual() {
             digesterVisual.classList.remove('good', 'warning', 'danger');
             if (currentPh >= params.ph.optimalMin) {
                 digesterVisual.classList.add('good');
                 digesterVisual.style.backgroundColor = '#5cb85c'; /* Success green */
                 digesterVisual.querySelector('.digester-text').textContent = 'יציב';
                 digesterVisual.classList.add('active');
             } else if (currentPh >= params.ph.warningThreshold) {
                 digesterVisual.classList.add('warning');
                 digesterVisual.style.backgroundColor = '#f0ad4e'; /* Warning orange */
                  digesterVisual.querySelector('.digester-text').textContent = 'התראה';
                 digesterVisual.classList.add('active'); // Still active but stressed
             } else {
                 digesterVisual.classList.add('danger');
                 digesterVisual.style.backgroundColor = '#d9534f'; /* Danger red */
                  digesterVisual.querySelector('.digester-text').textContent = 'קריסה!';
                 digesterVisual.classList.remove('active'); // Not active when crashed
             }
         }

        function updateOverallStatusMessage() {
             overallStatusMessage.className = 'status-message'; // Reset classes
             if (simDay === 0) {
                 overallStatusMessage.textContent = 'הדייג\'סטר מוכן לפעולה. בחר הגדרות והתחל מחזור.';
             } else if (currentPh >= params.ph.optimalMin && dailyBiogasRate > 0) {
                  overallStatusMessage.textContent = '🚀 הדייג\'סטר פועל ביציבות ומייצר ביוגז!';
             } else if (currentPh >= params.ph.warningThreshold) {
                 overallStatusMessage.classList.add('warning');
                 overallStatusMessage.textContent = '⚠️ שימו לב: ה-pH יורד. הדייג\'סטר תחת עומס!';
             } else {
                 overallStatusMessage.classList.add('danger');
                  overallStatusMessage.textContent = '💥 קריסה! ה-pH נמוך מדי, התהליך נעצר. אנא אפס.';
             }

            if (simDay >= params.simulation.maxDays && simulationInterval) {
                 overallStatusMessage.textContent = '✅ מחזור סימולציה הסתיים בהצלחה. סה"כ ביוגז: ' + totalBiogas.toFixed(2) + ' מ"ק.';
                 overallStatusMessage.classList.add('good');
             } else if (simDay >= params.simulation.maxDays && !simulationInterval && currentPh < params.ph.warningThreshold) {
                 overallStatusMessage.textContent = '😢 מחזור סימולציה הסתיים בקריסה. נסה הגדרות אחרות.';
                 overallStatusMessage.classList.add('danger');
            }
        }


        function calculateBiogasProduction() {
             const material = getSelectedMaterial();
             const temp = getSelectedTemperature();
             const olr = parseInt(olrRange.value);

             // Base production based on OLR and material potential
             let biogas_day = material.baseYieldFactor * olr * temp.speedFactor;

             // Adjust production based on pH - significant drop below optimalMin
             let ph_factor = 0;
             if (currentPh >= params.ph.optimalMin) {
                 ph_factor = 1.0; // Optimal production
             } else if (currentPh > params.ph.crashThreshold) {
                 // Production drops sharply between optimalMin and crashThreshold
                 ph_factor = (currentPh - params.ph.crashThreshold) / (params.ph.optimalMin - params.ph.crashThreshold);
                  ph_factor = Math.max(0.05, ph_factor); // Don't drop to exactly 0 unless pH is below crash
             } else {
                 ph_factor = 0; // Process crashed
             }
             biogas_day *= ph_factor;

             // Methane percentage is also affected by pH
             let methane_ph_factor = 1.0;
              if (currentPh < params.ph.warningThreshold) {
                  methane_ph_factor = Math.max(0.3, (currentPh - params.ph.crashThreshold) / (params.ph.warningThreshold - params.ph.crashThreshold));
              }
              currentMethane = material.methanePercent * methane_ph_factor;


             dailyBiogasRate = biogas_day; // Store for status check
             return biogas_day;
        }

        function simulateDay() {
            simDay++;

            const material = getSelectedMaterial();
            const temp = getSelectedTemperature();
            const olr = parseInt(olrRange.value);

            // --- pH Calculation ---
            let pH_change_tendency = (params.ph.initial - currentPh) * params.ph.recoveryRate; // Tendency towards initial pH

            // Stress from OLR relative to a conceptual balanced OLR (e.g., slider 5)
            // OLR stress is only significant when OLR is high
            let olr_stress = 0;
            if (olr > 5) {
                olr_stress = (olr - 5) / 5; // 0 to 1.0 for OLR 5-10
            } else if (olr < 5) {
                // Low OLR might allow faster recovery if pH is low
                 if (currentPh < params.ph.optimalMin) {
                     pH_change_tendency += (5 - olr) / 5 * params.ph.recoveryRate * 0.5; // Small boost to recovery
                 }
            }

            // pH drop due to OLR stress. Amplified by material's pH_impact_base and inverse of bufferCapacity.
            // Reduced by temperature stability factor (higher stabilityFactor -> less pH drop).
             let ph_drop_from_stress = olr_stress * material.pH_impact_base * (10 / material.bufferCapacity) * (2 - temp.stabilityFactor); // Formula adjustment

            // Combine changes
            currentPh += pH_change_tendency - ph_drop_from_stress;


            // Clamp pH within reasonable bounds, but allow it to go quite low on crash
            currentPh = Math.max(3.5, Math.min(8.5, currentPh)); // Lower min bound to show crash severity

            // --- Biogas Production Calculation ---
            const biogas_day = calculateBiogasProduction();
            totalBiogas += biogas_day;

            updateDisplay();

             // Stop simulation if crashed (pH too low for too long)
             if (currentPh < params.ph.crashThreshold && simDay > 5) { // Allow few days before crash
                 stopSimulation();
                 startBtn.disabled = true; // Prevent starting again until reset
                  overallStatusMessage.classList.add('danger');
                  overallStatusMessage.textContent = '💥 קריסה! ה-pH נמוך מדי והתהליך נעצר. אנא אפס כדי לנסות שוב.';
                  digesterVisual.classList.remove('active');
             }


             // Stop simulation after max days
             if (simDay >= params.simulation.maxDays && simulationInterval) {
                 stopSimulation();
                 startBtn.disabled = true; // Prevent starting again until reset
             }
        }

        function startSimulation() {
            if (!simulationInterval) {
                startBtn.disabled = true;
                stopBtn.disabled = false;
                // Reset display before starting if not already reset
                if (simDay === 0) {
                     resetSimulationState(); // Ensure state is clean
                }
                 digesterVisual.classList.add('active'); // Start bubble animation
                simulationInterval = setInterval(simulateDay, params.simulation.intervalMs);
                 overallStatusMessage.textContent = '🔄 מתחילים את מחזור הסימולציה...';
                 overallStatusMessage.classList.remove('warning', 'danger');
            }
        }

        function stopSimulation() {
            if (simulationInterval) {
                clearInterval(simulationInterval);
                simulationInterval = null;
                startBtn.disabled = false;
                stopBtn.disabled = true;
                digesterVisual.classList.remove('active'); // Stop bubble animation
                 updateOverallStatusMessage(); // Update message to 'Paused' or final status
            }
        }

        function resetSimulationState() {
            stopSimulation();
            simDay = 0;
            totalBiogas = 0;
            currentPh = params.ph.initial;
            currentMethane = getSelectedMaterial().methanePercent; // Reset methane to base material value
            dailyBiogasRate = 0; // Reset daily rate
            startBtn.disabled = false; // Enable start button
             stopBtn.disabled = true; // Disable stop button
             digesterVisual.classList.remove('good', 'warning', 'danger', 'active'); // Reset visual state
             digesterVisual.style.backgroundColor = '#a0a0a0'; // Reset visual color
             digesterVisual.querySelector('.digester-text').textContent = 'מוכן'; // Reset visual text
        }

        function resetSimulation() {
             resetSimulationState();
             updateDisplay(); // Update UI with reset state
             updateOverallStatusMessage(); // Update message to initial state
        }


        // Event Listeners
        startBtn.addEventListener('click', startSimulation);
        stopBtn.addEventListener('click', stopSimulation);
        resetBtn.addEventListener('click', resetSimulation);

        olrRange.addEventListener('input', updateOlrValueDisplay);

        // Reset simulation state when material or temperature changes
        materialSelect.addEventListener('change', resetSimulation);
        tempRadios.forEach(radio => {
            radio.addEventListener('change', resetSimulation);
        });


        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? '🙈 הסתר הסבר תהליך התסיסה האנאירובית' : '🤔 מה בדיוק קורה כאן? הסבר על תהליך התסיסה האנאירובית';
        });


        // Initial setup
        updateOlrValueDisplay();
        resetSimulation(); // Set initial state and display
        updateOverallStatusMessage(); // Set initial message
        updateDigesterVisual(); // Set initial visual
         digesterVisual.querySelector('.digester-text').textContent = 'מוכן'; // Initial text
    });
</script>