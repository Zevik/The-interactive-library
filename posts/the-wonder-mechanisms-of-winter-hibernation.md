---
title: "מסע הפלא אל תרדמת החורף"
english_slug: the-wonder-mechanisms-of-winter-hibernation
category: "ביולוגיה"
tags: ["היברנציה", "תרדמת חורף", "פיזיולוגיה", "ביולוגיה", "הישרדות", "אדפטציה"]
---
# מסע הפלא אל תרדמת החורף

דמיינו יצור קטן הנאבק לשרוד בחורף קפוא, כשהמזון אוזל והטמפרטורה צונחת. במקום להיכנע, הוא יוצא למסע פיזיולוגי מדהים - תרדמת החורף. זו אינה שינה רגילה, אלא צלילה מבוקרת למצב דמוי מוות, שבו הגוף מאט כמעט לגמרי: הלב בקושי פועם, הנשימה כמעט עוצרת, וטמפרטורת הגוף יורדת באופן דרמטי, לעיתים קרוב לנקודת הקיפאון. איך הם עושים זאת? הצטרפו אלינו לסימולציה ותגלו את המנגנונים הסודיים המאפשרים את פלא ההישרדות הזה.

<div id="hibernation-simulation-app">
    <h2 class="sim-title">סימולטור כניסה ויציאה מתרדמת חורף</h2>
    <p class="sim-intro">התנסו בשליטה על מנגנונים ביולוגיים מפתח וצפו כיצד הם משפיעים על מצב הגוף של חיית מעבדה.</p>

    <div class="controls-panel">
        <h3>שליטה על פרמטרים ביולוגיים:</h3>
        <div class="control-group">
            <label for="adenosine"><span class="param-label">אדנוזין:</span> מולקולת ויסות מרכזית (רמה גבוהה ⬅️ קידום תרדמת)</label>
            <input type="range" id="adenosine" min="0" max="100" value="50">
            <span id="adenosine-value" class="value-display">50</span>
        </div>
        <div class="control-group">
            <label for="thyroid"><span class="param-label">הורמוני בלוטת התריס:</span> מאיצים מטבוליזם (רמה גבוהה ⬅️ התנגדות לתרדמת)</label>
            <input type="range" id="thyroid" min="0" max="100" value="50">
            <span id="thyroid-value" class="value-display">50</span>
        </div>
        <div class="control-group">
            <label for="setpoint"><span class="param-label">נקודת קביעה תרמית (היפותלמוס):</span> "תרמוסטט" פנימי (רמה נמוכה ⬅️ ירידת חום מבוקרת)</label>
            <input type="range" id="setpoint" min="0" max="100" value="50">
            <span id="setpoint-value" class="value-display">50</span>
        </div>
         <div class="button-group">
            <button id="start-sim" class="sim-button start">הפעל סימולציה</button>
            <button id="reset-sim" class="sim-button reset" disabled>אפס</button>
        </div>
    </div>

    <div class="graphs-display">
        <h3>מדדי גוף החיה:</h3>
        <div class="graphs">
            <div class="graph-container">
                <div class="graph-header">
                    <span class="material-icons">thermometer_half</span>
                    <h4>טמפרטורת גוף (°C)</h4>
                </div>
                <div id="temp-graph" class="graph-area">
                    <div class="graph-bar temp-bar" style="height: 50%;"></div>
                     <span id="temp-value" class="value-indicator">37.0</span>
                </div>
                <p class="graph-range">0°C <span style="float:right;">40°C</span></p>
            </div>
            <div class="graph-container">
                 <div class="graph-header">
                     <span class="material-icons">favorite</span>
                     <h4>קצב לב (פעימות/דקה)</h4>
                 </div>
                 <div id="heart-rate-graph" class="graph-area">
                      <div class="graph-bar heart-rate-bar" style="height: 80%;"></div>
                      <span id="heart-rate-value" class="value-indicator">100</span>
                 </div>
                  <p class="graph-range">0 <span style="float:right;">120</span></p>
            </div>
            <div class="graph-container">
                <div class="graph-header">
                    <span class="material-icons">lungs</span>
                    <h4>קצב נשימה (נשימות/דקה)</h4>
                </div>
                <div id="resp-rate-graph" class="graph-area">
                     <div class="graph-bar resp-rate-bar" style="height: 60%;"></div>
                    <span id="resp-rate-value" class="value-indicator">30</span>
                </div>
                 <p class="graph-range">0 <span style="float:right;">40</span></p>
            </div>
             <div class="graph-container">
                 <div class="graph-header">
                     <span class="material-icons">bolt</span>
                     <h4>צריכת אנרגיה</h4>
                 </div>
                 <div id="energy-graph" class="graph-area">
                      <div class="graph-bar energy-bar" style="height: 90%;"></div>
                     <span id="energy-value" class="value-indicator">100%</span>
                 </div>
                  <p class="graph-range">0% <span style="float:right;">150%</span></p>
            </div>
        </div>
    </div>

    <p class="sim-status" id="sim-status">מצב: מוכן להתנסות. כווננו את הפרמטרים ולחצו "הפעל".</p>
     <p class="sim-feedback" id="sim-feedback"></p>
</div>

<button id="toggle-explanation" class="explanation-button">הצג את סודות תרדמת החורף</button>

<div id="explanation" style="display: none;">
    <h2>סודות מנגנוני תרדמת החורף נחשפים!</h2>

    <p>תרדמת חורף (היברנציה) היא אחת האדפטציות המדהימות ביותר בטבע. זו לא סתם "שינה עמוקה", אלא מצב הישרדות קיצוני שבו הגוף עובר טרנספורמציה דרמטית כדי לחסוך באנרגיה ולהתמודד עם תנאי סביבה קשים ביותר.</p>

    <h3>מה באמת קורה לגוף בהיברנציה? ההבדל משינה רגילה.</h3>
    תרדמת חורף היא מצב פיזיולוגי מבוקר היטב שבו יונקים ועופות מסוימים (כמו סנאי קרקע, עטלפים, מרמיטות) מורידים באופן קיצוני את קצב חילוף החומרים. זהו דיכוי מטבולי עמוק, בניגוד לשינה רגילה שבה טמפרטורת הגוף יורדת רק במעט והפעילות המטבולית נשארת גבוהה יחסית. בהיברנציה:
    <ul>
        <li><b>טמפרטורת גוף:</b> צונחת באופן מבוקר - לעיתים קרובות מתחת ל-10 מעלות צלזיוס, ואף קרוב ל-0!</li>
        <li><b>קצב לב ונשימה:</b> מואטים עד כדי פעימות בודדות או נשימות ספורות בדקה.</li>
        <li><b>צריכת אנרגיה:</b> יכולה לרדת ב-95% ומעלה בהשוואה למצב פעיל.</li>
        <li><b>תגובתיות:</b> בעל החיים כמעט אינו מגיב לגירויים חיצוניים.</li>
    </ul>
    <p>מצב זה מאפשר להם לשרוד חודשים ללא צורך במזון או מים, כשהם מסתמכים על מאגרי שומן בלבד.</p>

    <h3>המסע מתחיל: הטריגרים לכניסה לתרדמת.</h3>
    הכניסה לתרדמת אינה החלטה פתאומית, אלא תהליך המתוזמן בקפידה על ידי רמזים סביבתיים ושינויים פנימיים:
    <ul>
        <li><b>רמזים סביבתיים קריטיים:</b> קיצור שעות האור (הטריגר העיקרי לרוב), ירידה הדרגתית בטמפרטורה, והידלדלות במקורות מזון.</li>
        <li><b>הכנה פיזיולוגית:</b> אגירת שומן חום (BAT - Brown Adipose Tissue) החיוני להתעוררות מהירה, שינויים ברמות הורמונים כמו מלטונין (הורמון השינה העונתי) והורמוני בלוטת התריס (ירידה בהם מאפשרת האטת מטבוליזם), והצטברות מולקולות כמו אדנוזין המקדמות דיכוי מטבולי ושינה עמוקה.</li>
    </ul>

    <h3>בלימת החיים: שינויים פיזיולוגיים ודיכוי מטבולי.</h3>
    השינויים הדרמטיים במדדי הגוף שהסימולציה הציגה הם תוצאה של מנגנונים מורכבים:
    <ul>
        <li><b>ירידת טמפרטורה מבוקרת:</b> ההיפותלמוס, ה"תרמוסטט" של הגוף, מוריד באופן אקטיבי את "נקודת הקביעה" שלו, מה שמאפשר לגוף להתקרר באופן בטוח. זהו לא קור קיצוני לא מבוקר (היפותרמיה), אלא תהליך מתוזמר.</li>
        <li><b>האטת קצב לב ונשימה:</b> מנגנונים עצביים והורמונליים מפחיתים את פעילות מערכות הלב והנשימה כדי לחסוך אנרגיה.</li>
        <li><b>ניתוב זרימת דם:</b> הדם מופנה בעיקר לאיברים חיוניים כמו המוח והלב, בעוד שאיברים פחות חיוניים מקבלים פחות אספקה.</li>
        <li><b>שינויים ברמה התאית:</b> פעילות אנזימים מואטת, הגוף עובר לשימוש מוגבר במאגרי שומן במקום גלוקוז היעיל פחות בטמפרטורות נמוכות, וחל שינוי במבנה ממברנות התא כדי לשמור על תפקודן בקור. משאבות יוניות הצורכות אנרגיה רבה (כמו משאבת נתרן-אשלגן) מאיטות פעילותן.</li>
    </ul>

    <h3>התעוררות דרמטית: חזרה לחיים במהירות שיא!</h3>
    התעוררות מתרדמת (Arousal) היא תהליך פלאי לא פחות מהכניסה אליה. היא אקטיבית, מהירה, וגוזלת כמות אדירה של אנרגיה (כפי שראיתם בסימולציה, צריכת האנרגיה קופצת!).
    <ul>
        <li><b>ייצור חום מהיר:</b> מתבצע בעיקר באמצעות שומן חום (BAT), רקמה מיוחדת עשירה במיטוכונדריות שיודעות "לשרוף" שומן במהירות ולייצר חום במקום אנרגיה כימית רגילה. בעל החיים גם רועד כדי לייצר חום נוסף.</li>
        <li><b>האצת מערכות הלב והנשימה:</b> חוזרות לפעילות מהירה בתיאום עם עליית טמפרטורת הגוף.</li>
        <li><b>מחזורי התעוררות:</b> רוב בעלי החיים מתעוררים לפרקי זמן קצרים (כמה שעות) כל כמה שבועות במהלך התרדמת. הסיבות לכך אינן ברורות לחלוטין, אך ייתכן שהן קשורות לחידוש מלאי כימיקלים מוחיים, תיקון נזקים, או פעילות חיסונית קצרה.</li>
    </ul>

    <h3>לא כל "ישן חורף" נולד שווה: ההבדל בין היברנטורים אמיתיים לדובים.</h3>
    חשוב לציין שיש הבדלים בין בעלי חיים שונים:
    <ul>
        <li><b>היברנטורים אמיתיים:</b> (כמו סנאי קרקע, מרמיטות) מורידים את טמפרטורת הגוף לרמות נמוכות מאוד (קרוב ל-0°C) ונכנסים לדיכוי מטבולי עמוק וקשה להתעוררות.</li>
        <li><b>דובים:</b> נכנסים למצב הנקרא לעיתים "טורפור רדוד". טמפרטורת גופם יורדת רק בכמה מעלות בודדות (בדרך כלל ל-30-34°C), וקצב חילוף החומרים שלהם יורד במידה פחות דרמטית. הם נשארים ערניים יותר ויכולים להתעורר במהירות יחסית, אדפטציה חשובה במיוחד עבור נקבות שממליטות גורים במהלך החורף. לכן, תרדמת החורף של הדובים היא ייחודית ושונה מהיברנציה "קלאסית".</li>
    </ul>
    <p>היכולת לנווט בין מצב חיים פעיל לדיכוי מטבולי קיצוני ולהתעורר בחזרה היא עדות מדהימה למורכבות ולגמישות של מערכות ביולוגיות, ומקור השראה למחקר בתחומים כמו רפואה ושימור.</p>
</div>

<style>
    /* Import Google Fonts for better typography */
    @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');
    /* Import Material Icons */
    @import url('https://fonts.googleapis.com/icon?family=Material+Icons');


    body {
        font-family: 'Varela Round', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft blue gradient */
        color: #333;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2, h3 {
        color: #00796b; /* Teal color for headings */
        margin-bottom: 15px;
        text-align: center;
    }

     h1 {
         margin-top: 0;
         padding-top: 20px;
     }


    #hibernation-simulation-app {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Deeper shadow */
        margin: 20px auto; /* Center the app */
        max-width: 900px; /* Max width for large screens */
        border: 1px solid #b2ebf2; /* Light blue border */
        overflow: hidden; /* Clear floats */
    }

    .sim-title {
        color: #004d40; /* Darker teal */
        margin-top: 0;
    }

    .sim-intro {
        text-align: center;
        margin-bottom: 30px;
        color: #555;
        font-size: 1.1em;
    }

    .controls-panel {
        margin-bottom: 40px;
        padding: 20px;
        background-color: #e0f2f7; /* Lighter blue background */
        border-radius: 8px;
        border: 1px solid #b2ebf2;
    }

     .controls-panel h3 {
         text-align: right;
         color: #004d40;
         margin-top: 0;
         margin-bottom: 20px;
     }

    .control-group {
        margin-bottom: 20px;
        display: flex; /* Align label, slider, and value */
        align-items: center;
        gap: 10px; /* Space between elements */
    }

    .control-group label {
        flex-basis: 250px; /* Fixed width for labels */
        min-width: 150px;
        font-weight: bold;
        color: #006064; /* Cyan-like color */
        font-size: 1em;
    }

     .control-group label .param-label {
         font-size: 1.1em; /* Make the main parameter name slightly larger */
         display: block; /* Put param name on its own line */
         margin-bottom: 3px;
         color: #004d40;
     }

    .control-group input[type="range"] {
        flex-grow: 1; /* Slider takes available space */
        height: 8px; /* Thicker slider */
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        background: #b2ebf2; /* Light blue track */
        outline: none;
        opacity: 0.8;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    /* Slider Thumb Styling */
    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #00796b; /* Teal thumb */
        cursor: pointer;
        border-radius: 50%; /* Round thumb */
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #00796b;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }

    .control-group .value-display {
         width: 40px; /* Fixed width for value display */
         text-align: center;
         font-weight: bold;
         color: #004d40; /* Darker teal */
         font-size: 1.1em;
     }

     .button-group {
         text-align: center;
         margin-top: 30px;
     }

    .sim-button {
        padding: 12px 25px;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        margin: 0 10px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Varela Round', sans-serif;
    }

    .sim-button.start {
        background-color: #4caf50; /* Green */
    }
    .sim-button.start:hover:not(:disabled) {
        background-color: #388e3c; /* Darker green */
        transform: translateY(-2px);
    }

    .sim-button.reset {
        background-color: #f44336; /* Red */
    }
     .sim-button.reset:hover:not(:disabled) {
        background-color: #d32f2f; /* Darker red */
         transform: translateY(-2px);
    }

     .sim-button:disabled {
         background-color: #ccc;
         cursor: not-allowed;
     }

     .graphs-display {
         margin-top: 30px;
     }

     .graphs-display h3 {
          text-align: center;
          color: #004d40;
          margin-bottom: 20px;
     }


    .graphs {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 25px; /* More space between graphs */
    }

    .graph-container {
        flex: 1 1 200px; /* Flex-grow, flex-shrink, basis */
        background-color: #f5f5f5; /* Light grey background */
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        min-width: 180px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        border: 1px solid #eee;
        position: relative; /* Needed for range positioning */
    }

    .graph-header {
        display: flex;
        align-items: center;
        justify-content: center; /* Center header content */
        margin-bottom: 10px;
    }

    .graph-header .material-icons {
        margin-left: 8px; /* Space between icon and text */
        color: #00796b;
        font-size: 1.5em;
    }

    .graph-area {
        width: 100%;
        height: 180px; /* Taller graph area */
        background-color: #e0f7fa; /* Very light blue */
        border: 1px solid #b2ebf2;
        margin-top: 10px;
        position: relative;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        overflow: hidden;
        border-radius: 5px;
    }

     .graph-area .value-indicator {
         position: absolute;
         top: 10px; /* Position value higher */
         left: 50%;
         transform: translateX(-50%);
         font-size: 1.3em; /* Larger value font */
         font-weight: bold;
         z-index: 2; /* Ensure text is above the bar */
         color: #004d40;
         text-shadow: 0 0 3px rgba(255,255,255,0.7); /* Add shadow for readability */
     }

    .graph-bar {
        width: 80%;
        background-color: #5bc0de;
        transition: height 0.8s ease-out, background-color 0.5s ease; /* Smoother transition */
        position: absolute;
        bottom: 0;
        left: 10%;
        border-radius: 3px 3px 0 0; /* Rounded top corners */
    }

    /* Specific bar colors - more vibrant */
    .temp-bar { background-color: #ff9800; } /* Orange - initially warm */
    .heart-rate-bar { background-color: #f44336; } /* Red - initially high */
    .resp-rate-bar { background-color: #2196f3; } /* Blue */
    .energy-bar { background-color: #4caf50; } /* Green - initially high consumption */

    /* Color changes based on simulated state could be added here via JS adding classes */
    .graph-area.state-hibernating .temp-bar,
    .graph-area.state-hibernating .heart-rate-bar,
    .graph-area.state-hibernating .resp-rate-bar {
         background-color: #00bcd4; /* Cyan for low values */
    }
     .graph-area.state-hibernating .energy-bar {
          background-color: #8bc34a; /* Lighter green for very low energy */
     }

     .graph-area.state-arousal .temp-bar,
     .graph-area.state-arousal .heart-rate-bar,
     .graph-area.state-arousal .resp-rate-bar {
          background-color: #ff5722; /* Deep orange for arousal */
     }
      .graph-area.state-arousal .energy-bar {
           background-color: #fbc02d; /* Yellow/orange for high energy spike */
      }

     .graph-range {
         font-size: 0.9em;
         color: #555;
         margin-top: 5px;
         display: flex;
         justify-content: space-between; /* Place min/max at ends */
     }


    .sim-status {
        text-align: center;
        margin-top: 25px;
        font-weight: bold;
        font-size: 1.2em;
        color: #004d40;
         min-height: 1.4em; /* Reserve space */
    }

    .sim-feedback {
        text-align: center;
        margin-top: 10px;
        font-size: 1em;
        color: #d32f2f; /* Red for warnings/feedback */
         min-height: 1.2em; /* Reserve space */
    }


    .explanation-button {
        display: block; /* Make button block-level */
        width: fit-content; /* Fit to content */
        margin: 30px auto; /* Center horizontally and add space */
        padding: 12px 25px;
        background-color: #0275d8; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Varela Round', sans-serif;
    }

    .explanation-button:hover {
         background-color: #025aa5; /* Darker blue */
          transform: translateY(-2px);
    }


    #explanation {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        border: 1px solid #b2ebf2;
         margin: 20px auto;
        max-width: 900px;
    }

    #explanation h2, #explanation h3 {
        color: #00796b;
        margin-top: 25px;
        margin-bottom: 15px;
        text-align: right; /* Align explanation headings right */
    }

    #explanation h2:first-child {
        margin-top: 0;
    }

    #explanation p {
        margin-bottom: 15px;
        color: #333;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Add padding for list bullets */
    }

    #explanation li {
        margin-bottom: 10px;
        color: #333;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .graphs {
            flex-direction: column; /* Stack graphs vertically on smaller screens */
            align-items: center;
        }
        .graph-container {
            width: 80%; /* Make containers wider when stacked */
            flex-basis: auto; /* Remove flex basis */
        }
         .control-group {
             flex-direction: column;
             align-items: flex-start;
         }
         .control-group label {
             flex-basis: auto;
             width: 100%;
             margin-bottom: 5px;
         }
         .control-group input[type="range"] {
             width: 100%;
             margin-right: 0;
         }
          .control-group .value-display {
             width: 100%;
             text-align: right;
             margin-top: 5px;
             font-size: 1em;
         }

         body {
             padding: 10px;
         }
         #hibernation-simulation-app, #explanation {
             padding: 20px;
             margin: 10px auto;
         }
         .sim-button {
             padding: 10px 20px;
             font-size: 1em;
         }
         .explanation-button {
              padding: 10px 20px;
              font-size: 1em;
              margin: 20px auto;
         }
    }

</style>

<script>
    const adenosineSlider = document.getElementById('adenosine');
    const adenosineValueSpan = document.getElementById('adenosine-value');
    const thyroidSlider = document.getElementById('thyroid');
    const thyroidValueSpan = document.getElementById('thyroid-value');
    const setpointSlider = document.getElementById('setpoint');
    const setpointValueSpan = document.getElementById('setpoint-value');

    const startButton = document.getElementById('start-sim');
    const resetButton = document.getElementById('reset-sim');
    const simStatus = document.getElementById('sim-status');
    const simFeedback = document.getElementById('sim-feedback'); // New feedback element

    const tempValueSpan = document.getElementById('temp-value');
    const heartRateValueSpan = document.getElementById('heart-rate-value');
    const respRateValueSpan = document.getElementById('resp-rate-value');
    const energyValueSpan = document.getElementById('energy-value');

    const tempBar = document.querySelector('.temp-bar'); // Use class for bar
    const heartRateBar = document.querySelector('.heart-rate-bar');
    const respRateBar = document.querySelector('.resp-rate-bar');
    const energyBar = document.querySelector('.energy-bar');

    const tempGraphArea = document.getElementById('temp-graph'); // Get graph areas to add state classes
    const heartRateGraphArea = document.getElementById('heart-rate-graph');
    const respRateGraphArea = document.getElementById('resp-rate-graph');
    const energyGraphArea = document.getElementById('energy-graph');


    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    let simulationInterval = null;
    let simTime = 0; // Simulated time steps
    let lastStateChangeTime = 0;

    // States: 'Ready', 'Active', 'AttemptingEnter', 'Entering', 'Hibernating', 'AttemptingArousal', 'Arousal', 'Failed'
    let currentState = 'Ready';

    // Initial & Target values (more realistic range)
    const physiologicalRanges = {
        temp: { active: [36, 38], hibernating: [0, 5], entering: [10, 20], arousal: [15, 35] },
        heartRate: { active: [80, 120], hibernating: [2, 10], entering: [15, 40], arousal: [40, 80] },
        respRate: { active: [20, 40], hibernating: [1, 5], entering: [5, 15], arousal: [10, 25] },
        energy: { active: [80, 120], hibernating: [3, 10], entering: [10, 30], arousal: [120, 180] } // %
    };

    let currentValues = {
        temp: physiologicalRanges.temp.active[0],
        heartRate: physiologicalRanges.heartRate.active[0],
        respRate: physiologicalRanges.respRate.active[0],
        energy: physiologicalRanges.energy.active[0]
    };

    // Simulation Parameters (derived from sliders)
    let paramAdenosine = 0.5; // 0 to 1
    let paramThyroid = 0.5; // 0 to 1
    let paramSetpoint = 0.5; // 0 to 1

    // Sliders setup
    const sliders = [
        { slider: adenosineSlider, span: adenosineValueSpan, param: 'paramAdenosine' },
        { slider: thyroidSlider, span: thyroidValueSpan, param: 'paramThyroid' },
        { slider: setpointSlider, span: setpointValueSpan, param: 'paramSetpoint' }
    ];

    sliders.forEach(({ slider, span, param }) => {
        slider.addEventListener('input', (event) => {
            const value = parseInt(event.target.value, 10);
            span.textContent = value;
            this[param] = value / 100; // Update corresponding param variable
             if(currentState === 'Ready' || currentState === 'AttemptingEnter' || currentState === 'Failed') {
                updateFeedback(); // Give feedback on parameter settings
             }
        });
    });


    // Function to update slider values on load and reset
    function updateSliderValues() {
        sliders.forEach(({ slider, span, param }) => {
            const value = parseInt(slider.value, 10);
            span.textContent = value;
            this[param] = value / 100;
        });
         updateFeedback(); // Update feedback on load/reset
    }

     // Function to provide feedback based on slider settings
     function updateFeedback() {
         const combinedParams = (paramAdenosine + (1 - paramThyroid) + (1 - paramSetpoint)) / 3; // Higher = more favorable for hibernation

         let feedbackText = '';
         if (combinedParams < 0.3) {
             feedbackText = 'הפרמטרים הנוכחיים אינם מתאימים לכניסה לתרדמת. נסה לשנות אותם.';
             simFeedback.style.color = '#d32f2f'; // Red
         } else if (combinedParams < 0.6) {
             feedbackText = 'הפרמטרים מעט יותר טובים, אך עדיין קשה לכניסה מוצלחת.';
             simFeedback.style.color = '#fbc02d'; // Yellow
         } else if (combinedParams < 0.8) {
             feedbackText = 'הפרמטרים תומכים בכניסה לתרדמת. כנראה תצליח!';
             simFeedback.style.color = '#fbc02d'; // Yellow
         } else {
             feedbackText = 'הפרמטרים אופטימליים לכניסה לתרדמת! צפוי תהליך מהיר וחלק.';
             simFeedback.style.color = '#4caf50'; // Green
         }
         simFeedback.textContent = feedbackText;

          // Disable sliders in certain states
         const enableSliders = currentState === 'Ready' || currentState === 'Failed' || currentState === 'AttemptingEnter';
          sliders.forEach(({ slider }) => {
              slider.disabled = !enableSliders;
          });

     }


    // Function to get target values based on state and parameters
    function getDynamicTargets() {
        const hRange = physiologicalRanges.hibernating;
        const aRange = physiologicalRanges.active;
        const eRange = physiologicalRanges.entering;
         const arRange = physiologicalRanges.arousal;

        if (currentState === 'Active' || currentState === 'Ready' || currentState === 'Failed') return {
             temp: aRange[0] + Math.random() * (aRange[1] - aRange[0]), // Slight fluctuation in active
             heartRate: aRange[0] + Math.random() * (aRange[1] - aRange[0]),
             respRate: aRange[0] + Math.random() * (aRange[1] - aRange[0]),
             energy: aRange[0] + Math.random() * (aRange[1] - aRange[0])
         };

        if (currentState === 'Hibernating') return {
            temp: hRange[0] + Math.random() * (hRange[1] - hRange[0]), // Slight fluctuation in hibernation
            heartRate: hRange[0] + Math.random() * (hRange[1] - hRange[0]),
            respRate: hRange[0] + Math.random() * (hRange[1] - hRange[0]),
            energy: hRange[0] + Math.random() * (hRange[1] - hRange[0])
        };

        if (currentState === 'Arousal') return {
             temp: arRange[1], // Arousal aims quickly for high temp
             heartRate: arRange[1],
             respRate: arRange[1],
             energy: arRange[1] // Peak energy during arousal
         };

        // Interpolate targets based on parameters when 'AttemptingEnter' or 'Entering'
        const hibernationFactor = (paramAdenosine + (1 - paramThyroid) + (1 - paramSetpoint)) / 3; // 0 (active) to 1 (hibernation)

        const targetTemp = aRange[0] + hibernationFactor * (hRange[0] - aRange[0]); // Interpolate towards low end of hibernation range
        const targetHeartRate = aRange[0] + hibernationFactor * (hRange[0] - aRange[0]);
        const targetRespRate = aRange[0] + hibernationFactor * (hRange[0] - aRange[0]);
        const targetEnergy = aRange[0] + hibernationFactor * (hRange[0] - aRange[0]);


         return {
            temp: targetTemp,
            heartRate: targetHeartRate,
            respRate: targetRespRate,
            energy: targetEnergy
        };
    }

     // Function to ease value towards target
     function easeValue(current, target, easeFactor, randomFactor = 0) {
          let eased = current + (target - current) * easeFactor;
          if (randomFactor > 0) {
              eased += (Math.random() - 0.5) * randomFactor; // Add slight random noise
          }
          return eased;
     }

    // Function to update physiological values
    function updatePhysiology() {
        const targets = getDynamicTargets();
        let ease = 0.03; // How quickly values move towards targets

         if (currentState === 'Arousal') {
             ease = 0.1; // Speed up arousal
         } else if (currentState === 'AttemptingEnter' || currentState === 'Entering') {
             // Ease depends on how favorable params are for entering
              const combinedParams = (paramAdenosine + (1 - paramThyroid) + (1 - paramSetpoint)) / 3;
             ease = 0.02 + combinedParams * 0.05; // Faster ease with better params
         }


        currentValues.temp = easeValue(currentValues.temp, targets.temp, ease, 0.1);
        currentValues.heartRate = easeValue(currentValues.heartRate, targets.heartRate, ease, 0.5);
        currentValues.respRate = easeValue(currentValues.respRate, targets.respRate, ease, 0.2);
        currentValues.energy = easeValue(currentValues.energy, targets.energy, ease, 1);

        // Clamp values within reasonable bounds (slightly outside hibernation/active ranges to show extremes)
         const allTempRange = physiologicalRanges.hibernating[0] - 5;
         const allTempMax = physiologicalRanges.active[1] + 5;
        currentValues.temp = Math.max(allTempRange, Math.min(allTempMax, currentValues.temp));

        const allHRRange = physiologicalRanges.hibernating[0] - 5;
        const allHRMax = physiologicalRanges.active[1] + 30;
        currentValues.heartRate = Math.max(allHRRange, Math.min(allHRMax, currentValues.heartRate));

         const allRRRange = physiologicalRanges.hibernating[0] - 2;
        const allRRMax = physiologicalRanges.active[1] + 15;
        currentValues.respRate = Math.max(allRRRange, Math.min(allRRMax, currentValues.respRate));

         const allEnergyRange = physiologicalRanges.hibernating[0] - 5;
        const allEnergyMax = physiologicalRanges.arousal[1] + 20;
        currentValues.energy = Math.max(allEnergyRange, Math.min(allEnergyMax, currentValues.energy));


        // Update display
        tempValueSpan.textContent = currentValues.temp.toFixed(1);
        heartRateValueSpan.textContent = Math.round(currentValues.heartRate);
        respRateValueSpan.textContent = Math.round(currentValues.respRate);
        energyValueSpan.textContent = Math.round(currentValues.energy) + '%';

         // Update graph bars (height is relative to max possible value defined by clamp)
        const maxTemp = allTempMax;
        const maxHeartRate = allHRMax;
        const maxRespRate = allRRMax;
        const maxEnergy = allEnergyMax;

        tempBar.style.height = `${((currentValues.temp - allTempRange) / (maxTemp - allTempRange)) * 100}%`;
        heartRateBar.style.height = `${((currentValues.heartRate - allHRRange) / (maxHeartRate - allHRRange)) * 100}%`;
        respRateBar.style.height = `${((currentValues.respRate - allRRRange) / (maxRespRate - allRRRange)) * 100}%`;
        energyBar.style.height = `${((currentValues.energy - allEnergyRange) / (maxEnergy - allEnergyRange)) * 100}%`;


        // Update graph area class for color changes based on state
        [tempGraphArea, heartRateGraphArea, respRateGraphArea, energyGraphArea].forEach(area => {
             area.classList.remove('state-active', 'state-entering', 'state-hibernating', 'state-arousal', 'state-failed');
             if (currentState !== 'Ready') { // Don't add state class if ready
                area.classList.add('state-' + currentState.toLowerCase().replace('attempting', '')); // Simplify class names
             }
         });
    }

    // Function to manage state transitions
    function manageState() {
        const combinedParams = (paramAdenosine + (1 - paramThyroid) + (1 - paramSetpoint)) / 3; // Higher = more favorable for hibernation

        const thresholdEnterSuccess = 0.7; // Threshold for successful entry
        const thresholdEnterFail = 0.4; // Threshold below which entry attempt fails
        const thresholdArouse = 0.3; // Threshold to trigger arousal

        const timeInState = simTime - lastStateChangeTime;

        if (currentState === 'Ready') {
            simStatus.textContent = 'מצב: מוכן להתנסות. כווננו את הפרמטרים ולחצו "הפעל".';
             simFeedback.style.color = '#333';
             simFeedback.textContent = 'נסה להעלות אדנוזין ולהוריד הורמוני תריס ונקודת קביעה תרמית כדי להיכנס לתרדמת.';

        } else if (currentState === 'AttemptingEnter') {
             simStatus.textContent = 'מצב: מנסה להיכנס לתרדמת...';
             simFeedback.textContent = 'צופה בתגובת הגוף לפרמטרים שקבעת.';
             simFeedback.style.color = '#006064'; // Cyan

            // Check if parameters are good enough to start entering
            if (combinedParams > thresholdEnterSuccess) {
                currentState = 'Entering';
                 lastStateChangeTime = simTime;
            } else if (combinedParams < thresholdEnterFail && timeInState > 50) { // Fail if params bad and not making progress after some time
                 currentState = 'Failed';
                  lastStateChangeTime = simTime;
            } else if (timeInState > 150) { // Fail if taking too long even with moderate params
                 currentState = 'Failed';
                  lastStateChangeTime = simTime;
             }


        } else if (currentState === 'Entering') {
             simStatus.textContent = 'מצב: כניסה מבוקרת לתרדמת...';
             simFeedback.textContent = 'מדדי הגוף צונחים בהדרגה. שמור על פרמטרים אופטימליים!';
              simFeedback.style.color = '#00796b'; // Teal


             // Check if successfully entered hibernation
             if (currentValues.temp <= physiologicalRanges.hibernating[1] + 1 && combinedParams > thresholdEnterFail) { // Reached low temp AND params aren't terrible
                 currentState = 'Hibernating';
                 lastStateChangeTime = simTime;
                 simFeedback.textContent = 'הצלחה! הגוף נכנס לתרדמת חורף עמוקה. כל הכבוד!';
                 simFeedback.style.color = '#4caf50'; // Green

             } else if (currentValues.temp <= physiologicalRanges.hibernating[0] - 1 || combinedParams < thresholdEnterFail * 0.8) { // Failed if too cold too fast OR params became very bad
                 currentState = 'Failed';
                  lastStateChangeTime = simTime;
             }


        } else if (currentState === 'Hibernating') {
             simStatus.textContent = 'מצב: בתרדמת חורף עמוקה';
             simFeedback.textContent = 'הגוף חוסך אנרגיה בצורה מדהימה.';
              simFeedback.style.color = '#0097a7'; // Dark Cyan

             // Check conditions to arouse (parameters become unfavorable or simulated periodic arousal)
             const randomArouseChance = 0.0005; // Small chance each step
             if (combinedParams < thresholdArouse || Math.random() < randomArouseChance || currentValues.temp > physiologicalRanges.hibernating[1] + 3) { // Arouse if params bad, random chance, or warming up unexpectedly
                 currentState = 'Arousal';
                 lastStateChangeTime = simTime;
                  simFeedback.textContent = 'מתעורר... תהליך זה דורש הרבה אנרגיה.';
                 simFeedback.style.color = '#ff9800'; // Orange
             }
              // Add a check for temperature getting *too* low (below hibernating minimum)
            if (currentValues.temp < physiologicalRanges.hibernating[0] - 2 && timeInState > 100) { // Too cold for too long
                 currentState = 'Failed'; // Forced failure due to critical cold
                 lastStateChangeTime = simTime;
            }

        } else if (currentState === 'Arousal') {
             simStatus.textContent = 'מצב: התעוררות מהירה!';
             simFeedback.textContent = 'שומן חום מייצר חום במהירות. מדדי הגוף קופצים!';
              simFeedback.style.color = '#ff5722'; // Deep Orange

              // Arousal always aims for Active state (simplified)
              const targetActiveTemp = physiologicalRanges.active[0] + (physiologicalRanges.active[1] - physiologicalRanges.active[0]) / 2;
              if (currentValues.temp >= targetActiveTemp && timeInState > 50) { // Temp is high enough and arousal took some time
                 currentState = 'Active';
                 lastStateChangeTime = simTime;
                  simFeedback.textContent = 'חזרה למצב פעיל! מוכן למחזור הבא.';
                   simFeedback.style.color = '#4caf50'; // Green
              } else if (timeInState > 200) { // Arousal taking too long might indicate a problem (simplified as just returning to active)
                   currentState = 'Active';
                   lastStateChangeTime = simTime;
                    simFeedback.textContent = 'חזרה למצב פעיל.';
                    simFeedback.style.color = '#4caf50';
              }

        } else if (currentState === 'Failed') {
            simStatus.textContent = 'מצב: כניסה לתרדמת נכשלה!';
             if (currentValues.temp < physiologicalRanges.hibernating[0] - 1) {
                  simFeedback.textContent = 'טמפרטורת הגוף ירדה יותר מדי ללא בקרה מתאימה. סכנה!';
                  simFeedback.style.color = '#f44336'; // Red
             } else {
                 simFeedback.textContent = 'הגוף לא הצליח להיכנס למצב תרדמת עם הפרמטרים שנקבעו.';
                  simFeedback.style.color = '#f44336'; // Red
             }

             clearInterval(simulationInterval); // Stop simulation on failure
             simulationInterval = null;
             startButton.disabled = false;
             resetButton.disabled = false;
             sliders.forEach(({ slider }) => { slider.disabled = false; }); // Allow adjustment after failure
        }

        // If in Active state after a cycle or reset
        if (currentState === 'Active' && timeInState > 100) { // Stay active for some time before allowing new attempt
             currentState = 'Ready'; // Return to ready state to allow re-configuring parameters
             lastStateChangeTime = simTime;
             updateFeedback(); // Enable sliders and show feedback
        } else if (currentState === 'Active') {
             simStatus.textContent = 'מצב: פעיל';
             simFeedback.textContent = 'ממתין לתחילת המחזור הבא או להתאמת פרמטרים.';
             simFeedback.style.color = '#333';
        }

    }


    // Main simulation loop
    function runSimulation() {
        simTime++;
        manageState();
        updatePhysiology();
    }

    // Start Button logic
    startButton.addEventListener('click', () => {
        if (simulationInterval) {
            clearInterval(simulationInterval);
        }
        currentState = 'AttemptingEnter'; // Start attempting to enter hibernation
        lastStateChangeTime = simTime;
        simTime = 0; // Reset simulation time
         simFeedback.textContent = ''; // Clear previous feedback

        // Run simulation loop every 100ms (faster transitions)
        simulationInterval = setInterval(runSimulation, 80);
        startButton.disabled = true; // Disable start during sim
        resetButton.disabled = false;
         // Sliders state managed by updateFeedback or manageState
    });

    // Reset Button logic
    resetButton.addEventListener('click', () => {
        if (simulationInterval) {
            clearInterval(simulationInterval);
            simulationInterval = null;
        }
        currentState = 'Ready';
        simTime = 0;
        lastStateChangeTime = 0;

        // Reset current values to active state initial
         currentValues = {
            temp: physiologicalRanges.active[0],
            heartRate: physiologicalRanges.active[0],
            respRate: physiologicalRanges.active[0],
            energy: physiologicalRanges.active[0]
        };

        // Reset sliders to default
        adenosineSlider.value = 50;
        thyroidSlider.value = 50;
        setpointSlider.value = 50;
        updateSliderValues(); // Update text spans and internal params

        updatePhysiology(); // Update display to initial active state values

        startButton.disabled = false;
        resetButton.disabled = true;
         simStatus.textContent = 'מצב: מוכן להתנסות. כווננו את הפרמטרים ולחצו "הפעל".';
         simFeedback.textContent = 'נסה להעלות אדנוזין ולהוריד הורמוני תריס ונקודת קביעה תרמית כדי להיכנס לתרדמת.';
          simFeedback.style.color = '#333';
         sliders.forEach(({ slider }) => { slider.disabled = false; }); // Enable sliders
    });

    // Toggle explanation logic
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר את סודות תרדמת החורף';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג את סודות תרדמת החורף';
        }
    });

    // Initialize the app state on load
    function initializeApp() {
        updateSliderValues(); // Sync slider values and text spans and initial feedback
        updatePhysiology(); // Set initial graph values to active state
        resetButton.disabled = true; // Reset button starts disabled
         sliders.forEach(({ slider }) => { slider.disabled = false; }); // Sliders are enabled in 'Ready' state
         simStatus.textContent = 'מצב: מוכן להתנסות. כווננו את הפרמטרים ולחצו "הפעל".';
         simFeedback.textContent = 'נסה להעלות אדנוזין ולהוריד הורמוני תריס ונקודת קביעה תרמית כדי להיכנס לתרדמת.';
         simFeedback.style.color = '#333';
    }

    // Run initialization when the page loads
    initializeApp();

</script>
```