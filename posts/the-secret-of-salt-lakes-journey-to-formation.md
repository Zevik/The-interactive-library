---
title: "סוד אגמי המלח: מסע אינטראקטיבי אל תהליך ההיווצרות"
english_slug: the-secret-of-salt-lakes-journey-to-formation
category: "מדעי הסביבה / כדור הארץ"
tags: אגמי מלח, מישורי מלח, התאדות, גיאולוגיה, הידרולוגיה, סימולציה
---
<h1>סוד אגמי המלח: מסע אינטראקטיבי אל תהליך ההיווצרות</h1>
<p>הצטרפו אלינו למסע מרתק אל לב התופעה הגיאולוגית וההידרולוגית שיוצרת פלאי טבע כמו ים המלח ומישורי המלח הבוהקים. כאן, באגן סגור משלנו, תוכלו לראות במו עיניכם איך שילוב של מים, שמש וזמן בלתי נגמר בונה נופים מלוחים וייחודיים.</p>

<div class="simulation-container">
    <h2>בנו את אגם המלח שלכם:</h2>
    <div class="controls">
        <div class="control-group">
            <label for="inflow">קצב כניסת מים טריים (<span class="unit">יחידות/שנייה</span>):</label>
            <input type="range" id="inflow" min="0" max="10" value="2" step="0.1">
            <span class="value" id="inflowValue">2.0</span>
            <div class="control-description">כמה מים נושאים מלחים זורמים לאגן</div>
        </div>

        <div class="control-group">
            <label for="evaporation">קצב התאדות השמש החזקה (<span class="unit">יחידות/שנייה</span>):</label>
            <input type="range" id="evaporation" min="0" max="10" value="1" step="0.1">
            <span class="value" id="evaporationValue">1.0</span>
             <div class="control-description">כמה מים (נקיים ממלח) מתאדים לאוויר</div>
        </div>

        <div class="button-group">
            <button id="startButton" class="action-button">התחילו את המסע!</button>
            <button id="resetButton" class="secondary-button">אפסו את האגן</button>
        </div>

        <div class="status">
            <h3>מצב האגם הנוכחי</h3>
            <p>זמן סימולציה: <span id="simulationTime">0</span> <span class="unit">שניות</span></p>
            <p>גובה המים באגן: <span id="waterLevel">0.00</span> <span class="unit">יחידות גובה</span></p>
            <p>ריכוז המלחים במים: <span id="saltConcentration">0.00</span> <span class="unit">יחידות מלח/יחידת מים</span></p>
            <p>שכבת מלח שהצטברה בקרקעית: <span id="saltLayerHeight">0.00</span> <span class="unit">יחידות גובה</span></p>
             <div id="precipitationIndicator" class="indicator hidden">מלח שוקע!</div>
        </div>
    </div>

    <div class="basin-container">
        <div class="inflow-indicator"></div>
        <div class="evaporation-indicator"></div>
        <div class="basin-border">
             <div class="precipitation-animation"></div> <!-- For salt precipitation animation -->
            <div class="salt-layer" id="saltLayer"></div>
            <div class="water-layer" id="waterLayer">
                 <div class="water-surface-waves"></div> <!-- For water surface animation -->
            </div>
        </div>
        <div class="basin-label">אגן ניקוז סגור</div>
    </div>
</div>

<button id="toggleExplanation" class="explanation-toggle">גלו את הסוד מאחורי המסע (הסבר מפורט)</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר מעמיק: כך נולדים אגמי מלח ומישוריהם</h2>
    <h3>הגדרה: ממלכות המלח של הטבע</h3>
    <p>**אגמי מלח** אינם סתם אגמים מלוחים; הם גופי מים יבשתיים עם ריכוז מלחים גבוה כל כך, שלעיתים קרובות עולה על זה של מי האוקיינוס. **מישורי מלח** (המכונים גם Salt Flats או Playa) הם שרידים יבשים, שטוחים ומרהיבים של אגמי מלח שהתייבשו, המכוסים בשכבות עבות של מלח טהור.</p>

    <h3>המתכון הסודי: תנאים להיווצרות</h3>
    <p>נדרש שילוב מדויק של תנאים כדי שממלכות מלח אלו יראו אור:</p>
    <ul>
        <li>**אזור אקלים צחיח או צחיח למחצה:** קצב ההתאדות כאן גבוה בהרבה מקצב הגעת המים הטריים. השמש עובדת שעות נוספות!</li>
        <li>**אגן ניקוז סגור (אנדוראי):** זהו סיר הלחץ של המלחים. מים נכנסים אליו מכל עבר, אך אין להם דרך משמעותית לצאת החוצה (מלבד התאדות). כל המלחים שהמים נושאים נשארים לכודים בפנים.</li>
        <li>**מקור מים עשיר במלחים מומסים:** נהרות, נחלים ונגר עילי הזורמים לתוך האגן אוספים בדרכם מינרלים ומלחים מהסלעים והקרקע. הם מגיעים לאגן כשהם "טעונים" במלחים.</li>
    </ul>

    <h3>מאין מגיעים כל המלחים האלה?</h3>
    <p>המלחים הם למעשה עדים למסע הארוך שעשו המים על פני הקרום היבשתי. מי גשם מחלחלים לקרקע ויוצרים מי תהום, או זורמים על פני השטח כנחלים ונהרות. בדרכם, המים ממיסים בהדרגה מינרלים מסיסים שנמצאים בסלעים (כמו הליט - מלח נתרן כלורי) ובקרקע. המים הללו, כשהם כבר מלוחים מעט, מתנקזים בסופו של דבר אל האגן הסגור.</p>

    <h3>הדרמה באגן: תהליך ההצטברות</h3>
    <p>התהליך מתחיל עם כניסת המים ה"מלוחים" לאגן. כאן נכנסת לתמונה השמש הקופחת: המים ה"טהורים" (מולקולות H2O) מתאדים ועולים לאטמוספרה, בעוד שהמלחים הכבדים יותר נשארים מאחור. עם כל טיפה של מים שמתאדה, ריכוז המלחים במים הנותרים עולה ועולה. זה קצת כמו לצמצם רוטב - הטעם (או המליחות) מתגבר.</p>
    <p>כאשר ריכוז המלחים מגיע לנקודת השיא שבה המים כבר לא יכולים להחזיק יותר מלח מומס (נקודת הרוויה), המלחים "מתעייפים" ומתחילים לשקוע מחוץ לתמיסה. הם יוצרים גבישים קטנים השוקעים לאט לקרקעית האגם. תהליך זה נמשך ללא הרף כל עוד מים נכנסים ומתאדים, ומוביל להצטברות איטית אך איתנה של שכבות מלח עבות על גבי הקרקעית - לעיתים בעובי של עשרות ואף מאות מטרים!</p>

    <h3>כשמלך המלח מתייבש: לידת מישור המלח</h3>
    <p>מישור מלח נולד כאשר אגם המלח חווה תקופות יובש קיצוניות או מתייבש לחלוטין, בין אם עונתית או כתוצאה משינויי אקלים ארוכי טווח. כשהמים נעלמים, שכבות המלח שהצטברו נחשפות לעולם. הן יוצרות את אותם משטחים לבנים, מהפנטים ורחבי ידיים הנראים כאילו נלקחו מכוכב אחר, חלקם כה שטוחים עד שהם משמשים מסלולי נחיתה טבעיים או אתרי שיא עולמיים למרוצי מכוניות מהירות.</p>

    <h3>פלאי מלח בעולם: דוגמאות אייקוניות</h3>
    <ul>
        <li>**ים המלח (ישראל/ירדן):** המקום הנמוך ביותר על פני כדור הארץ ואחד האגמים המלוחים בעולם. סקרן? נסו לראות בסימולציה שלנו מה קורה כשיש הרבה כניסת מים ומעט התאדות מול הרבה התאדות ומעט כניסה!</li>
        <li>**סאלאר דה אויוני (בוליביה):** מישור המלח הגדול בעולם. גן עדן לצלמים ומקור עשיר לליתיום.</li>
        <li>**אגם סולט לייק הגדול (ארה"ב):** שריד לאגם ענק מהתקופה הפלייסטוקנית, הידוע במליחותו המשתנה בהתאם לכניסת מים והתאדות.</li>
    </ul>
</div>

<style>
    /* כללי בסיסי ועיצוב כולל */
    body {
        font-family: 'Arial Hebrew', sans-serif;
        line-height: 1.6;
        color: #333;
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
        background-color: #f4f4f4; /* רקע בהיר כללי */
    }

    h1, h2, h3 {
        color: #0e4f6e; /* כחול כהה / ירקרק */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        margin-top: 0;
        font-size: 2em;
        border-bottom: 2px solid #0e4f6e;
        padding-bottom: 10px;
        display: inline-block;
        width: auto;
        margin-right: auto;
        margin-left: auto;
    }

    p {
        margin-bottom: 1em;
    }

    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        padding: 30px;
        border: 1px solid #ccc;
        border-radius: 12px;
        background: linear-gradient(to bottom, #e0f2f7, #b2ebf2); /* רקע בהיר עם גרדיאנט עדין */
        max-width: 800px;
        margin: 20px auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .simulation-container h2 {
        text-align: center;
        width: 100%;
        margin-bottom: 20px;
        color: #0056b3;
    }

    .controls {
        width: 100%;
        max-width: 450px; /* רוחב גדול יותר לבקרים */
        text-align: right;
        background-color: #ffffff; /* רקע לבן לקונטרולים */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }

    .control-group {
        margin-bottom: 20px;
    }

    .controls label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
    }

    .controls input[type="range"] {
        width: calc(100% - 60px); /* מותאם לרוחב כולל ה-span */
        margin-bottom: 5px;
        direction: ltr; /* מחוון תמיד משמאל לימין */
        -webkit-appearance: none; /* הסרת עיצוב ברירת מחדל */
        appearance: none;
        height: 8px;
        background: #ddd;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    .controls .value {
        display: inline-block;
        width: 50px;
        text-align: left;
        margin-right: 5px; /* שינוי ל margin-right בשביל RTL */
        font-weight: bold;
        color: #007bff;
    }

     .control-description {
         font-size: 0.9em;
         color: #777;
         margin-top: 4px;
     }

    .button-group {
        text-align: center;
        margin-top: 25px;
    }

    .action-button, .secondary-button {
        padding: 10px 20px;
        margin: 0 8px;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* כפתורים מעוגלים יותר */
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .action-button {
        background-color: #007bff;
        color: white;
    }

    .action-button:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }

    .secondary-button {
        background-color: #6c757d;
        color: white;
    }

    .secondary-button:hover {
        background-color: #5a6268;
         transform: translateY(-1px);
    }

     .action-button:disabled, .secondary-button:disabled {
         opacity: 0.6;
         cursor: not-allowed;
         transform: none;
     }

    .status {
        margin-top: 25px;
        padding: 15px;
        border: 1px solid #eee;
        border-radius: 8px;
        background-color: #e9ecef; /* רקע אפור בהיר לסטטוס */
        text-align: right;
        font-size: 0.95em;
    }

    .status h3 {
        margin-top: 0;
        border-bottom: 1px solid #ccc;
        padding-bottom: 8px;
        margin-bottom: 10px;
        color: #333;
        text-align: right;
    }

    .status p {
        margin-bottom: 8px;
        display: flex; /* שימוש בפלקס כדי להפריד תוכן מיחידות */
        justify-content: space-between;
        align-items: center;
    }

    .status p span {
         font-weight: bold;
         color: #007bff;
         flex-grow: 1; /* מאפשר לערך לתפוס מקום */
         text-align: left; /* יישור הערך לשמאל */
         margin-left: 5px; /* רווח בין הערך ליחידה */
    }

     .status .unit {
         font-weight: normal;
         color: #555;
         font-size: 0.9em;
         text-align: right;
         margin-left: 0; /* ביטול מרווח משמאל ליחידה */
     }

     #precipitationIndicator {
         text-align: center;
         margin-top: 15px;
         padding: 8px;
         background-color: #ffc107; /* צהוב */
         color: #333;
         border-radius: 5px;
         font-weight: bold;
         animation: pulse 1.5s infinite; /* הבהוב */
     }

     #precipitationIndicator.hidden {
         display: none;
     }

     @keyframes pulse {
         0% { opacity: 1; }
         50% { opacity: 0.5; }
         100% { opacity: 1; }
     }


    .basin-container {
        width: 100%;
        max-width: 350px; /* קצת רחב יותר לוויזואליזציה */
        height: 350px; /* גובה גדול יותר לוויזואליזציה */
        display: flex;
        flex-direction: column-reverse; /* שכבות נערמות מלמטה */
        align-items: center;
        position: relative;
        margin-top: 20px;
        perspective: 1000px; /* עומק לתחושה תלת מימדית */
    }

     .basin-container::before { /* רקע הרים או נוף */
         content: '';
         position: absolute;
         top: -50px;
         left: 0;
         right: 0;
         height: 100px; /* גובה הנוף */
         background: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxNTAlIiB2aWV3Qm94PSIwIDAgMzAwIDIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cGF0aCBkPSJNMCAxNTBsMzAtMzBsMzAtNDBsNDAtMjBsNTAtMzBsNTAtMTBsMzAgMjBsMjAgNDBMIDMwMCAyMDBIMCBMIDAgMTUweiIgZmlsbD0iI2FjY2JkNyIgdHJhbnNmb3JtPSJzY2FsZSgxLjIgMC42KSB0cmFuc2xhdGUoLTEwIDIwKSIvPgogIDxwYXRoIGQ9Ik0wIDE3MGwzMC0yMGw0MC0yMGw0MC0xMGw0MC0xMGw1MCAwTDwgMzAwIDEwMGwzMCAyMGwyMCAzMEwgMzAwIDIwMEgwIEwgMCAxNzB6IiBmaWxsPSIjYjNjNGNlIiB0cmFuc2Zvcm09InNjYWxlKDEuMSAwLjgpIHRyYW5zbGF0ZSgwIDEwKSIvPgogIDxwYXRoIGQ9Ik0wIDIwMEw0MCAxODBsNDAgLTEwbDUwIC01bDQwIC01bDQwIDBMIDMwMCAxNTBsNDAgMjBMIDMwMCAyMDBIMCBMIDAgMjAweiIgZmlsbD0iI2Q0ZDNjZSIgdHJhbnNmb3JtPSJzY2FsZSgxIDAuOSkgdHJhbnNsYXRlKDAgMCkiLz4KPC9zdmc+'); /* הרים סכמטיים */
         background-size: cover;
         background-repeat: no-repeat;
         z-index: 0; /* לוודא שמאחורי האגן */
         opacity: 0.7;
     }


    .basin-border {
        width: 85%; /* רוחב של האגן עצמו */
        height: 100%;
        border: 4px solid #6d4c41; /* מסגרת חומה כהה */
        border-top-color: transparent; /* פתוח למעלה */
        border-bottom-left-radius: 50px; /* פינות תחתונות מעוגלות יותר */
        border-bottom-right-radius: 50px;
        position: relative;
        overflow: hidden; /* להשאיר את השכבות בפנים */
        display: flex;
        flex-direction: column-reverse; /* שכבות נערמות מלמטה */
        align-items: center;
        background-color: #f0d8b9; /* צבע חול/אדמה לקרקעית */
        z-index: 1; /* מעל הנוף */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.2); /* צל פנימי לתחושת עומק */
    }


    .water-layer {
        width: 100%;
        /* הגובה נקבע ע"י JS */
        background-color: rgba(173, 216, 230, 0.7); /* תכלת עדין התחלתי */
        transition: height 0.5s ease-out, background-color 0.5s ease-out; /* מעברים חלקים וארוכים יותר */
        position: relative;
        overflow: hidden; /* להכיל גלים ואפקטים אחרים */
    }

    .water-surface-waves {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 10px; /* גובה הגלים */
        background: linear-gradient(to bottom, rgba(255,255,255,0.3), rgba(255,255,255,0)); /* אפקט ברק על המים */
        animation: waves 2s ease-in-out infinite alternate; /* אנימציית גלים */
         opacity: 0.8;
    }

    @keyframes waves {
        0% { transform: translateY(0); }
        100% { transform: translateY(2px); } /* תנועה קלה למעלה ולמטה */
    }


     .salt-layer {
        width: 100%;
        /* הגובה נקבע ע"י JS */
        background-color: #f8f8f8; /* לבן בוהק למלח */
        background-image: linear-gradient(45deg, #f8f8f8 25%, #eee 25%, #eee 50%, #f8f8f8 50%, #f8f8f8 75%, #eee 75%, #eee 100%); /* טקסטורת מלח עדינה */
        background-size: 10px 10px;
        border-top: 2px solid #ccc; /* קו הפרדה עליון למלח */
        transition: height 0.5s ease-out; /* מעבר חלק לגובה */
        position: relative;
        z-index: 2; /* מעל רקע האגן */
        box-shadow: inset 0 5px 10px rgba(0,0,0,0.1); /* צל עדין על שכבת המלח */
     }

    .basin-label {
        position: absolute;
        bottom: -35px;
        left: 50%;
        transform: translateX(-50%);
        font-weight: bold;
        color: #555;
        font-size: 0.9em;
    }

    .inflow-indicator, .evaporation-indicator {
        position: absolute;
        pointer-events: none; /* לא להפריע לקליקים */
        z-index: 3; /* מעל הכל */
    }

    .inflow-indicator {
        top: 20%;
        left: 5%; /* מגיע מהצד */
        width: 30px;
        height: 30px;
        background: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTMgMTJsMTgtNXY1bC0xOCAxdi02LjV6IiBmaWxsPSIjMDQ5MkZmIi8+PC9zdmc+'); /* אייקון מים */
        background-size: contain;
        background-repeat: no-repeat;
        animation: inflow 1.5s linear infinite; /* אנימציית זרימה */
        opacity: 0; /* התחל שקוף */
         filter: drop-shadow(0 0 3px rgba(0, 150, 255, 0.5));
    }

    @keyframes inflow {
        0% { transform: translateX(0) translateY(0); opacity: 0; }
        20% { opacity: 1; }
        80% { transform: translateX(calc(100% - 10%)) translateY(30%); opacity: 1; } /* נע לכיוון מרכז האגן */
        100% { transform: translateX(calc(100% - 10%)) translateY(30%); opacity: 0; }
    }

    .evaporation-indicator {
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 50px;
        height: 50px;
        background: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMOC4xOSA2LjgyQTEwLjAwNCAxMC4wMDQgMCAwIDAgMiAxNmgyQThBOCAwIDAgMCAxMiA4YTggOCAwIDAgMCA4IDhoMmE5Ljk4IDEwLjk4IDAgMCAwLTYuMTktOS4xOEwxMiAyWiIgc3R5bGU9ImZpbGw6ICNhZmEzbWEiLz48L3N2Zz4='); /* אייקון ענן/אדים */
        background-size: contain;
        background-repeat: no-repeat;
        animation: evaporate 2s linear infinite; /* אנימציית התאדות */
        opacity: 0; /* התחל שקוף */
         filter: drop-shadow(0 0 5px rgba(175, 163, 163, 0.5));
    }

    @keyframes evaporate {
        0% { transform: translateX(-50%) translateY(0); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateX(-50%) translateY(-50px); opacity: 0; } /* עולה למעלה ונעלם */
    }

     .precipitation-animation {
         position: absolute;
         bottom: 0;
         left: 0;
         width: 100%;
         height: 100%; /* מכסה את כל גובה האגן */
         pointer-events: none;
         z-index: 2; /* מעל שכבת המלח */
         opacity: 0; /* מוסתר כברירת מחדל */
     }

     .precipitation-animation::before {
         content: '';
         position: absolute;
         bottom: 0;
         left: 0;
         width: 100%;
         height: 100%;
         background: radial-gradient(circle, rgba(255,255,255,0.5) 0%, rgba(255,255,255,0) 70%); /* אפקט הילה עדין */
         animation: precipitate-shine 1.5s ease-out forwards; /* אנימציית הבהוב */
     }
     .precipitation-animation.active {
         opacity: 1; /* הופך גלוי */
     }

    @keyframes precipitate-shine {
        0% { opacity: 0; transform: scale(0.5); }
        50% { opacity: 1; transform: scale(1); }
        100% { opacity: 0; transform: scale(1.2); }
    }


    .explanation-toggle {
         display: block;
         margin: 30px auto;
         padding: 12px 25px;
         cursor: pointer;
         border: none;
         border-radius: 25px;
         background-color: #0e4f6e; /* כחול כהה/ירקרק */
         color: white;
         font-size: 1.1em;
         transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .explanation-toggle:hover {
        background-color: #0a3c54;
        transform: translateY(-1px);
    }

    .explanation-section {
        margin: 20px auto;
        padding: 30px;
        border: 1px solid #ccc;
        border-radius: 12px;
        background-color: #fff; /* רקע לבן להסבר */
        max-width: 800px;
        font-family: Arial, sans-serif;
        line-height: 1.7;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .explanation-section h2, .explanation-section h3 {
        color: #0056b3;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

    .explanation-section ul {
        margin-top: 10px;
        padding-right: 25px; /* הזחה לרשימה */
        list-style: disc outside; /* סוג התבליט ומקומו */
    }

    .explanation-section li {
        margin-bottom: 10px;
    }

     .explanation-section p b {
         color: #0e4f6e; /* צבע מודגש להדגשים בהסבר */
     }

    /* התאמות RTL */
    .controls input[type="range"] {
        margin-left: 5px; /* רווח קטן בין המחוון לערך */
        margin-right: 0;
    }
     .controls .value {
         text-align: left;
         margin-left: 0;
         margin-right: 5px;
     }
    .status p span {
         text-align: left;
         margin-left: 5px;
         margin-right: 0;
     }
     .status .unit {
          text-align: right;
          margin-left: 0;
          margin-right: auto; /* דחיפת היחידה ימינה */
     }
    #explanation ul {
        padding-right: 25px;
        padding-left: 0;
    }


</style>

<script>
    const inflowSlider = document.getElementById('inflow');
    const evaporationSlider = document.getElementById('evaporation');
    const inflowValueSpan = document.getElementById('inflowValue');
    const evaporationValueSpan = document.getElementById('evaporationValue');
    const startButton = document.getElementById('startButton');
    const resetButton = document.getElementById('resetButton');
    const simulationTimeSpan = document.getElementById('simulationTime');
    const waterLevelSpan = document.getElementById('waterLevel');
    const saltConcentrationSpan = document.getElementById('saltConcentration');
    const saltLayerHeightSpan = document.getElementById('saltLayerHeight');
    const waterLayerDiv = document.getElementById('waterLayer');
    const saltLayerDiv = document.getElementById('saltLayer');
    const basinBorderDiv = document.querySelector('.basin-border');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const inflowIndicator = document.querySelector('.inflow-indicator');
    const evaporationIndicator = document.querySelector('.evaporation-indicator');
    const precipitationIndicatorText = document.getElementById('precipitationIndicator');
    const precipitationAnimationDiv = document.querySelector('.precipitation-animation');


    // Simulation parameters
    const timeStep = 0.1; // seconds per simulation step
    let simulationRunning = false;
    let simulationInterval = null;
    let simulationTime = 0;

    // Basin state (using abstract units)
    const basinArea = 100; // Abstract area
    const maxBasinVisualHeight = 350; // Max height for visualization in pixels (matches .basin-container height)

    // Define reasonable maximums in abstract units for scaling visual height
    const maxExpectedWaterLevel = 50; // Abstract units of height
    const maxExpectedSaltThickness = 30; // Abstract units of height

    const incomingSaltConcentration = 0.02; // Salt concentration in incoming water (increased slightly)
    const saturationConcentration = 0.8; // Concentration at which salt precipitates (increased for effect)
    const saltDensity = 2.16; // Approximate density of halite (abstract equivalent)

    // Calculate scaling factors for visual height (pixels per abstract height unit)
    const visualHeightScaleWater = maxBasinVisualHeight / maxExpectedWaterLevel;
    // Salt mass needs conversion to volume (mass/density), then to height (volume/area), then to visual pixels
    // depositedMass -> depositedVolume (depositedMass / saltDensity) -> depositedHeight (depositedVolume / basinArea) -> visualHeight (depositedHeight * visualHeightScaleSalt)
    // Let's simplify visual salt scaling directly from deposited mass for intuitiveness.
    // We need depositedSaltMass to reach a visual height of maxBasinVisualHeight. How much mass is needed?
    // Let's assume a certain total salt mass represents maxExpectedSaltThickness.
    // Total salt mass = maxExpectedSaltThickness * basinArea * saltDensity
    const maxExpectedSaltMass = maxExpectedSaltThickness * basinArea * saltDensity; // Mass needed to fill up to maxExpectedSaltThickness
    const visualHeightScaleSalt = maxBasinVisualHeight / maxExpectedSaltMass; // Pixels per unit of deposited salt mass


    // State variables
    let waterVolume = 0; // abstract volume units (Volume = Area * Height)
    let dissolvedSaltMass = 0; // abstract salt mass units
    let depositedSaltMass = 0; // abstract salt mass units
    let previousWaterLevel = 0; // To detect changes for animation


    // Initial UI updates
    inflowValueSpan.textContent = parseFloat(inflowSlider.value).toFixed(1);
    evaporationValueSpan.textContent = parseFloat(evaporationSlider.value).toFixed(1);

    inflowSlider.oninput = function() {
        inflowValueSpan.textContent = parseFloat(this.value).toFixed(1);
    }

    evaporationSlider.oninput = function() {
        evaporationValueSpan.textContent = parseFloat(this.value).toFixed(1);
    }

    startButton.onclick = function() {
        if (simulationRunning) {
            stopSimulation();
        } else {
            startSimulation();
        }
    }

    resetButton.onclick = function() {
        resetSimulation();
    }

    toggleExplanationButton.onclick = function() {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתירו את ההסבר המפורט';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'גלו את הסוד מאחורי המסע (הסבר מפורט)';
        }
    }

    function startSimulation() {
        if (simulationRunning) return; // Prevent multiple intervals
        simulationRunning = true;
        startButton.textContent = 'השהה את המסע';
        startButton.classList.remove('action-button');
        startButton.classList.add('secondary-button');
         resetButton.disabled = true; // Disable reset while running


        simulationInterval = setInterval(runSimulationStep, timeStep * 1000); // timeStep is in abstract seconds, setInterval is in milliseconds
    }

    function stopSimulation() {
        simulationRunning = false;
        startButton.textContent = 'המשיכו במסע';
        startButton.classList.remove('secondary-button');
        startButton.classList.add('action-button');
        clearInterval(simulationInterval);
        resetButton.disabled = false; // Enable reset after stopping
        // Stop visual indicators/animations if any
        inflowIndicator.style.animationPlayState = 'paused';
        evaporationIndicator.style.animationPlayState = 'paused';
        // Keep pulse animation for precipitation if active
        // precipitationAnimationDiv.classList.remove('active'); // Don't hide it immediately, let it finish? Or hide? Let's hide.
         precipitationAnimationDiv.classList.remove('active');
         precipitationIndicatorText.classList.add('hidden');
    }

    function resetSimulation() {
        stopSimulation();
        simulationTime = 0;
        waterVolume = 0;
        dissolvedSaltMass = 0;
        depositedSaltMass = 0;
        previousWaterLevel = 0;

        // Reset button text and state
        startButton.textContent = 'התחילו את המסע!';
        startButton.classList.remove('secondary-button');
        startButton.classList.add('action-button');
         startButton.disabled = false;
         resetButton.disabled = false;


        // Hide indicators
        inflowIndicator.style.opacity = 0;
        evaporationIndicator.style.opacity = 0;
        precipitationAnimationDiv.classList.remove('active');
         precipitationIndicatorText.classList.add('hidden');

        updateUI();
    }

    function runSimulationStep() {
        const inflowRate = parseFloat(inflowSlider.value);
        const evaporationRate = parseFloat(evaporationSlider.value);
        let precipitationOccurred = false;


        // 1. Inflow
        const deltaVolumeIn = inflowRate * timeStep;
        const deltaSaltIn = deltaVolumeIn * incomingSaltConcentration;

        waterVolume += deltaVolumeIn;
        dissolvedSaltMass += deltaSaltIn;

        // Trigger inflow animation (if needed)
         if (inflowRate > 0) {
             inflowIndicator.style.opacity = 1;
              inflowIndicator.style.animationPlayState = 'running';
         } else {
              inflowIndicator.style.opacity = 0;
              inflowIndicator.style.animationPlayState = 'paused';
         }


        // 2. Evaporation
        let deltaVolumeEvap = evaporationRate * timeStep;

        // Evaporation cannot remove more water than is currently present
        deltaVolumeEvap = Math.min(deltaVolumeEvap, waterVolume);

        waterVolume -= deltaVolumeEvap;

        // Trigger evaporation animation (if water is present and evaporating)
        if (waterVolume > 0 && evaporationRate > 0) {
            evaporationIndicator.style.opacity = 1;
            evaporationIndicator.style.animationPlayState = 'running';
        } else {
             evaporationIndicator.style.opacity = 0;
              evaporationIndicator.style.animationPlayState = 'paused';
        }


        // 3. Handle complete drying
        if (waterVolume <= 0) {
            // If it dries out, all remaining dissolved salt precipitates
            depositedSaltMass += dissolvedSaltMass;
            dissolvedSaltMass = 0;
            waterVolume = 0; // Ensure volume is exactly 0
            precipitationOccurred = true; // Drying implies precipitation of remaining salt
        } else {
             // 4. Handle saturation and precipitation (only if water is present)
            let currentConcentration = dissolvedSaltMass / waterVolume;

            if (currentConcentration > saturationConcentration) {
                // Calculate the mass of salt that is in excess of the saturation limit
                const excessSaltMass = dissolvedSaltMass - saturationConcentration * waterVolume;

                // This excess salt precipitates
                depositedSaltMass += excessSaltMass;
                dissolvedSaltMass -= excessSaltMass; // The remaining dissolved salt is now at saturation
                 precipitationOccurred = true; // Precipitation happened
            }
            // Re-calculate concentration after potential precipitation (should be <= saturationConcentration)
            currentConcentration = dissolvedSaltMass / waterVolume;
        }

        // Trigger precipitation animation/indicator
        if (precipitationOccurred) {
            precipitationAnimationDiv.classList.add('active');
            precipitationIndicatorText.classList.remove('hidden');
            // Animation will handle hiding itself via CSS timing
            // Or use JS timeout if CSS animation doesn't fully handle hiding
            setTimeout(() => {
                 precipitationAnimationDiv.classList.remove('active');
                 precipitationIndicatorText.classList.add('hidden');
            }, 1500); // Hide after 1.5 seconds (matches precipitate-shine animation duration)

        }


        // 5. Update time
        simulationTime += timeStep;

        // 6. Update UI
        updateUI();
    }

    function updateUI() {
        // Calculate current concentration for display
        let currentConcentration = 0;
        if (waterVolume > 0) {
             currentConcentration = dissolvedSaltMass / waterVolume;
        } else if (depositedSaltMass > 0 || dissolvedSaltMass > 0) {
             // If water is 0 but there's salt, it's effectively "saturated" or dry salt
             currentConcentration = saturationConcentration; // Indicate high/saturation level
        }

        // Calculate abstract water level (Height = Volume/Area)
        const abstractWaterLevel = waterVolume / basinArea;
         // Calculate abstract salt layer height (Height = Volume/Area = Mass/Density/Area)
        const abstractSaltLayerHeight = depositedSaltMass > 0 ? depositedSaltMass / saltDensity / basinArea : 0;

        // Calculate visual heights in pixels
        const visualSaltLayerHeight = abstractSaltLayerHeight * visualHeightScaleSalt; // Using the simplified mass-to-height scaling

        // Water visual height sits on top of salt, capped by basin height
        const spaceAboveSalt = maxBasinVisualHeight - visualSaltLayerHeight;
        const visualWaterLayerHeight = Math.min(abstractWaterLevel * visualHeightScaleWater, spaceAboveSalt);

        // Ensure heights are not negative
        const finalVisualSaltHeight = Math.max(0, visualSaltLayerHeight);
        const finalVisualWaterHeight = Math.max(0, visualWaterLayerHeight);


        // Update UI text elements
        simulationTimeSpan.textContent = simulationTime.toFixed(1);
        waterLevelSpan.textContent = abstractWaterLevel.toFixed(2);
        saltConcentrationSpan.textContent = currentConcentration > 0 ? currentConcentration.toFixed(2) : (waterVolume <= 0 && depositedSaltMass > 0 ? "יבש (מלח)" : "0.00"); // More informative when dry

        saltLayerHeightSpan.textContent = abstractSaltLayerHeight.toFixed(2); // Display abstract height


        // Update visual representation heights
        saltLayerDiv.style.height = `${Math.min(finalVisualSaltHeight, maxBasinVisualHeight)}px`;
        waterLayerDiv.style.height = `${finalVisualWaterHeight}px`;

        // Update water color based on concentration (only if water exists)
        if (waterVolume > 0) {
             const concentrationRatio = Math.min(currentConcentration / saturationConcentration, 1.5); // Allow slightly above 1 for visual difference
             // Interpolate color from light blue/teal to a more concentrated/briny color
             const startColor = [173, 216, 230]; // light blue
             const endColor = [0, 100, 150]; // darker blue/teal brine
             const r = startColor[0] + (endColor[0] - startColor[0]) * concentrationRatio;
             const g = startColor[1] + (endColor[1] - startColor[1]) * concentrationRatio;
             const b = startColor[2] + (endColor[2] - startColor[2]) * concentrationRatio;

             // Adjust opacity: less water volume, potentially less opaque or different texture
             const startOpacity = 0.7;
             const endOpacity = 0.9;
             // Base opacity on height ratio relative to max water height
             const heightRatio = abstractWaterLevel / maxExpectedWaterLevel;
             const opacity = startOpacity + (endOpacity - startOpacity) * Math.min(heightRatio, 1);


             waterLayerDiv.style.backgroundColor = `rgba(${r}, ${g}, ${b}, ${opacity})`;
             waterLayerDiv.style.backgroundImage = 'none'; // Remove any background image for color blend
             // Show water surface waves only if water level is visible
             waterLayerDiv.querySelector('.water-surface-waves').style.display = 'block';


        } else {
             // Dry state: hide water, adjust visuals
             waterLayerDiv.style.height = '0px';
             waterLayerDiv.style.backgroundColor = 'transparent';
             waterLayerDiv.style.backgroundImage = 'none';
             waterLayerDiv.querySelector('.water-surface-waves').style.display = 'none';
             // Adjust salt layer appearance when fully dry?
             // saltLayerDiv.style.backgroundColor = '#f0f0f0'; // Maybe slightly less white
             // basinBorderDiv.style.borderTopColor = '#6d4c41'; // Show top border? (currently transparent)
             saltLayerDiv.style.boxShadow = '0 0 15px rgba(255,255,255,0.5)'; // Add shine effect to salt when dry? Or different shadow
             saltLayerDiv.style.backgroundImage = 'linear-gradient(45deg, #fff 25%, #f8f8f8 25%, #f8f8f8 50%, #fff 50%, #fff 75%, #f8f8f8 75%, #f8f8f8 100%)'; // Stronger texture when dry?
             evaporationIndicator.style.opacity = 0; // Stop evaporation animation if no water
        }

        // Handle case where salt layer fills the basin entirely
         if (finalVisualSaltHeight >= maxBasinVisualHeight) {
              saltLayerDiv.style.height = `${maxBasinVisualHeight}px`;
              waterLayerDiv.style.height = '0px';
              waterVolume = 0; // Ensure state is zeroed if visually full of salt
              dissolvedSaltMass = 0;

              waterLevelSpan.textContent = "יבש (מלא מלח)";
              saltConcentrationSpan.textContent = "יבש (מלא מלח)";
              saltLayerHeightSpan.textContent = abstractSaltLayerHeight.toFixed(2) + " (מלא)";
              stopSimulation(); // Stop simulation if basin is full of salt
              startButton.textContent = 'האגן מלא!';
              startButton.disabled = true;
              evaporationIndicator.style.opacity = 0; // Stop all animations
              inflowIndicator.style.opacity = 0;

         } else {
              // Ensure start button is enabled if simulation was stopped due to filling but reset
               if (!simulationRunning && startButton.disabled && depositedSaltMass * visualHeightScaleSalt < maxBasinVisualHeight) {
                  startButton.disabled = false;
                  startButton.textContent = 'המשיכו במסע'; // Or 'התחילו את המסע' based on state
                   startButton.classList.remove('secondary-button');
                   startButton.classList.add('action-button');
               }
         }

        // Update previous water level for wave animation or other future effects
        previousWaterLevel = abstractWaterLevel;

    }

    // Initial update on page load
    updateUI();

    // Add a class to the body or container when JS is active to apply JS-dependent styles if needed
    document.body.classList.add('js-active');


</script>
---