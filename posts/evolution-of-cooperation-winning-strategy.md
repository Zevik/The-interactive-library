---
title: "האבולוציה של שיתוף הפעולה: מהי האסטרטגיה המנצחת?"
english_slug: evolution-of-cooperation-winning-strategy
category: "ביולוגיה"
tags: [שיתוף פעולה, אלטרואיזם הדדי, אבולוציה, תיאוריית המשחקים, דילמת האסיר]
---
# האבולוציה של שיתוף הפעולה: משחק ההישרדות האולטימטיבי

בעולם שבו רק החזקים והאנוכיים שורדים, נדמה שאין מקום לנדיבות. ובכל זאת, בטבע – ובחיינו שלנו – שיתוף פעולה ואפילו מעשי "אלטרואיזם" פורחים. איך ייתכן שבתוך מלחמת הישרדות תמידית, שבה כל פרט נאבק על משאבים והתרבות, בעל חיים אחד יעזור לאחר, גם כשזה כרוך במחיר אישי? כיצד הברירה הטבעית, שלכאורה מעדיפה את האנוכיים ביותר, הולידה מנגנונים מורכבים של עזרה הדדית?

<div id="app-container">
    <h2>סימולציית "הדילמה של האסיר החוזרת": שדה הקרב האבולוציוני</h2>
    <p class="intro-text">חקור כיצד אסטרטגיות התנהגות שונות מתחרות ומתפתחות לאורך דורות במשחק קלאסי של אמון ובגידה.</p>

    <div class="controls panel">
        <h3>הגדרות הסימולציה</h3>
        <div class="control-group">
            <label>הרכב אוכלוסייה התחלתי (%):</label>
            <div class="strategy-inputs">
                <div>
                    <label for="initial-ac">🤝 משתפי פעולה (AC):</label>
                    <input type="number" id="initial-ac" value="25" min="0" max="100" step="1">
                </div>
                <div>
                    <label for="initial-ad">🔪 בוגדים (AD):</label>
                    <input type="number" id="initial-ad" value="25" min="0" max="100" step="1">
                </div>
                <div>
                    <label for="initial-tft">⚖️ עין תחת עין (TFT):</label>
                    <input type="number" id="initial-tft" value="25" min="0" max="100" step="1">
                </div>
                 <div>
                    <label for="initial-rand">🎲 אקראי (RAND):</label>
                    <input type="number" id="initial-rand" value="25" min="0" max="100" step="1">
                </div>
            </div>
            <p class="input-hint">סך הכל חייב להיות 100%. <span id="total-percent-display">סה"כ: 100%</span></p>
        </div>

        <div class="control-group">
             <label>ערכי שכר (Payoffs):</label>
             <div class="payoff-inputs">
                 <div>
                     <label for="payoff-t">T: פיתוי (בגידה נגד שיתוף):</label>
                     <input type="number" id="payoff-t" value="5" min="1" step="0.1">
                 </div>
                 <div>
                     <label for="payoff-r">R: שכר (שיתוף הדדי):</label>
                     <input type="number" id="payoff-r" value="3" min="1" step="0.1">
                 </div>
                 <div>
                      <label for="payoff-p">P: עונש (בגידה הדדית):</label>
                     <input type="number" id="payoff-p" value="1" min="0" step="0.1">
                 </div>
                 <div>
                     <label for="payoff-s">S: פראייר (שיתוף נגד בגידה):</label>
                     <input type="number" id="payoff-s" value="0" min="-5" step="0.1">
                 </div>
             </div>
             <p class="input-hint">בדילמת האסיר סטנדרטית: T > R > P > S ו- 2R > T + S</p>
        </div>

        <div class="control-group">
             <label for="num-interactions">מספר מפגשים (סיבובים) לזוג:</label>
             <input type="number" id="num-interactions" value="10" min="1" step="1">
             <p class="input-hint">ככל שהמספר גבוה יותר, למוניטין יש משקל רב יותר.</p>
        </div>

        <div class="buttons">
            <button id="start-sim" class="btn-play">▶️ התחל סימולציה</button>
            <button id="step-sim" class="btn-step">⏩ דור הבא</button>
            <button id="reset-sim" class="btn-reset">🔄 איפוס</button>
        </div>
    </div>

    <div class="simulation-output panel">
        <h3>תוצאות - התפלגות האוכלוסייה</h3>
        <p class="generation-counter">דור נוכחי: <span id="current-generation">0</span></p>
        <div id="population-chart-container">
             <!-- Strategy bars will be rendered here by JS -->
            <div class="strategy-bar" id="bar-ac"></div>
            <div class="strategy-bar" id="bar-ad"></div>
            <div class="strategy-bar" id="bar-tft"></div>
            <div class="strategy-bar" id="bar-rand"></div>
        </div>
        <div class="strategy-labels">
            <span class="label-ac">🤝 AC (<span id="percent-ac">0.0</span>%)</span>
            <span class="label-ad">🔪 AD (<span id="percent-ad">0.0</span>%)</span>
            <span class="label-tft">⚖️ TFT (<span id="percent-tft">0.0</span>%)</span>
            <span class="label-rand">🎲 RAND (<span id="percent-rand">0.0</span>%)</span>
        </div>
        <div id="simulation-status" class="status-message"></div>
    </div>
</div>

<style>
    /* Global styles for better typography and box model */
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #f8f9fa; /* Light background */
    }

    h1 {
        text-align: center;
        color: #212529;
        margin-bottom: 30px;
        font-size: 2em;
    }

    #app-container {
        max-width: 900px;
        margin: 20px auto;
        padding: 30px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Clear floats/margins */
    }

    #app-container h2 {
        text-align: center;
        color: #0056b3; /* A nice blue */
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.7em;
    }

    .intro-text {
        text-align: center;
        color: #555;
        margin-bottom: 30px;
        font-size: 1.1em;
    }


    .panel {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background-color: #fefefe;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

     .panel h3 {
         margin-top: 0;
         color: #444;
         border-bottom: 1px solid #eee;
         padding-bottom: 10px;
         margin-bottom: 20px;
     }

    .control-group {
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 1px dashed #eee;
    }
     .control-group:last-child {
         border-bottom: none;
         padding-bottom: 0;
         margin-bottom: 0;
     }

    .control-group > label { /* Style for the main label of the group */
        display: block;
        font-weight: bold;
        margin-bottom: 10px;
        color: #555;
    }

    .strategy-inputs, .payoff-inputs {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); /* Adjust minmax */
        gap: 15px; /* Increased gap */
        margin-top: 5px;
    }

    .strategy-inputs div, .payoff-inputs div {
        display: flex;
        align-items: center;
        gap: 8px; /* Increased gap */
    }

    .strategy-inputs label, .payoff-inputs label {
         flex-shrink: 0;
         font-size: 1em; /* Slightly larger font */
         width: 160px; /* Wider fixed width for labels */
         color: #444;
    }
     .strategy-inputs input, .payoff-inputs input {
         flex-grow: 1;
         padding: 8px 10px; /* Increased padding */
         border: 1px solid #ccc;
         border-radius: 5px; /* More rounded corners */
         font-size: 1em;
         box-sizing: border-box; /* Include padding/border in element's total width/height */
         transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
     .strategy-inputs input:focus, .payoff-inputs input:focus, #num-interactions input:focus {
         border-color: #007bff;
         box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
         outline: none; /* Remove default outline */
     }


     #num-interactions { /* Specific styling for this input */
         padding: 8px 10px;
         border: 1px solid #ccc;
         border-radius: 5px;
         font-size: 1em;
         box-sizing: border-box;
         transition: border-color 0.2s ease, box-shadow 0.2s ease;
         display: inline-block; /* Make it behave nicely */
         width: 80px; /* Give it a fixed width */
         vertical-align: middle; /* Align with label */
     }


    .input-hint { /* Changed from small to p with class */
        display: block;
        margin-top: 8px;
        color: #777;
        font-size: 0.9em;
        text-align: right;
    }
     #total-percent-display {
         font-weight: bold;
         color: #007bff; /* Highlight total */
     }
     .percent-warning {
         color: #dc3545 !important; /* Red for warning */
     }


    .buttons {
        text-align: center;
        margin-top: 30px;
    }

    button {
        padding: 12px 25px; /* Larger padding */
        margin: 0 8px; /* Increased margin */
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
        min-width: 120px; /* Minimum width for buttons */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

     button:hover:not(:disabled) {
        transform: translateY(-1px); /* Subtle lift effect */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
     }
     button:active:not(:disabled) {
         transform: translateY(0); /* Press down effect */
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }

     button:disabled {
         opacity: 0.6;
         cursor: not-allowed;
     }

    .btn-play {
        background-color: #28a745; /* Success green */
        color: white;
    }
     .btn-play:hover:not(:disabled) { background-color: #218838; }

    .btn-step {
         background-color: #007bff; /* Primary blue */
         color: white;
    }
     .btn-step:hover:not(:disabled) { background-color: #0056b3; }


    .btn-reset {
        background-color: #dc3545; /* Danger red */
        color: white;
    }
     .btn-reset:hover:not(:disabled) { background-color: #c82333; }


    button#show-explanation {
         display: block;
         margin: 30px auto 10px auto; /* More space above/below */
         background-color: #6c757d; /* Secondary grey */
         color: white;
         font-size: 1em; /* Slightly smaller than control buttons */
          padding: 10px 20px;
         box-shadow: none; /* Less emphasis */
         min-width: auto;
    }
     button#show-explanation:hover:not(:disabled) {
         background-color: #5a6268;
          transform: none; /* No lift effect */
          box-shadow: none;
     }
     button#show-explanation:active:not(:disabled) {
         transform: none;
         box-shadow: none;
     }


    .simulation-output {
        margin-top: 30px;
    }

    .simulation-output h3 {
        text-align: center;
        margin-bottom: 15px;
    }

    .generation-counter {
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 15px;
        color: #555;
    }

    #current-generation {
        font-weight: bold;
        color: #007bff; /* Highlight generation number */
    }

    #population-chart-container {
        display: flex;
        width: 100%;
        height: 30px;
        border: 1px solid #ccc;
        margin-top: 10px;
        overflow: hidden;
        border-radius: 5px; /* Rounded ends for the bar */
        background-color: #e9ecef; /* Light background for empty space */
    }

    .strategy-bar {
        height: 100%;
        transition: width 0.7s ease-in-out; /* Smoother transition */
        box-sizing: border-box;
        /* Removed border-right from here, handle separator with pseudo-elements or box-shadow if needed */
    }

    /* Strategy Specific Colors */
    #bar-ac { background-color: #2ecc71; } /* Emerald Green */
    #bar-ad { background-color: #e74c3c; } /* Alizarin Red */
    #bar-tft { background-color: #3498db; } /* Peter River Blue */
    #bar-rand { background-color: #f39c12; } /* Orange */

     /* Add subtle separators */
     .strategy-bar:not(:last-child) {
         box-shadow: 1px 0 0 0 rgba(255, 255, 255, 0.5) inset; /* Inner shadow for separator */
     }
     /* Alternative for separator: border-right works but complicates rounded ends. Inner shadow is cleaner. */


     .strategy-labels {
        display: flex;
        justify-content: space-around;
        margin-top: 12px; /* More space */
        font-size: 0.95em;
        font-weight: bold;
     }

     /* Strategy Specific Label Colors */
     .label-ac { color: #2ecc71; }
     .label-ad { color: #e74c3c; }
     .label-tft { color: #3498db; }
     .label-rand { color: #f39c12; }


    .status-message { /* Changed from #simulation-status */
        margin-top: 20px; /* More space */
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-style: italic;
        color: #555;
        background-color: #e9ecef; /* Light background for status */
         min-height: 1.5em; /* Reserve space */
    }


    #explanation {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #dcdcdc;
        border-radius: 8px;
        background-color: #f0f3f5; /* Soft background */
        display: none; /* Initially hidden */
        line-height: 1.7; /* More comfortable reading */
    }

    #explanation h2, #explanation h3 {
        color: #333;
        margin-top: 20px;
        margin-bottom: 12px;
        border-bottom: 1px dotted #ccc;
        padding-bottom: 5px;
    }
     #explanation h2 { margin-top: 0; }

    #explanation p {
        margin-bottom: 15px; /* More space between paragraphs */
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-left: 25px; /* Indent list */
    }

    #explanation li {
        margin-bottom: 8px;
    }

    /* Responsive Adjustments */
    @media (max-width: 600px) {
        .strategy-inputs, .payoff-inputs {
             grid-template-columns: 1fr; /* Stack inputs on small screens */
        }
        .strategy-inputs div, .payoff-inputs div {
            flex-direction: column; /* Stack label and input */
            align-items: flex-start;
        }
        .strategy-inputs label, .payoff-inputs label {
            width: auto; /* Remove fixed width */
            margin-bottom: 3px; /* Space between label and input */
        }
        button {
            display: block; /* Stack buttons */
            width: calc(100% - 16px); /* Full width minus margin */
            margin: 8px auto; /* Center stacked buttons */
        }
         .strategy-labels {
             flex-direction: column; /* Stack labels */
             align-items: center;
             gap: 5px;
         }
          .strategy-labels span { width: 100%; text-align: center; }
           #app-container { padding: 20px; }
           h1 { font-size: 1.6em; }
           #app-container h2 { font-size: 1.4em; }
    }

</style>

<button id="show-explanation" class="btn-info">הצג הסבר מפורט על דילמת האסיר ושיתוף פעולה</button>

<div id="explanation">
    <h2>הסבר מעמיק: הדילמה של האסיר ואבולוציית שיתוף הפעולה</h2>

    <p>בניגוד להיגיון הפשוט, שבו נצפה שהברירה הטבעית תעדיף פרטים אנוכיים תמיד, אנו עדים לשפע של דוגמאות לשיתוף פעולה בטבע ובחברה האנושית. מדוע נמלים עובדות יחד למען הקן? כיצד עטלפי ערפד חולקים מזון? מדוע בני אדם יוצרים קהילות ומוסדות המבוססים על אמון והדדיות? התשובה טמונה, בין השאר, בכך שאינטראקציות אינן חד-פעמיות. בחיים, כמו במשחק, לרוב נפגשים שוב ושוב עם אותם "שחקנים".</p>

    <h3>בעיית האלטרואיזם באבולוציה: פרדוקס לכאורה</h3>
    <p>ברירה טבעית פועלת ברמת הפרט (לרוב). פרטים המותאמים יותר, שצוברים יותר משאבים ומתרבים בהצלחה, מעבירים את הגנים שלהם. התנהגות אלטרואיסטית, שבה פרט נושא בעלות (זמן, אנרגיה, סיכון) כדי להיטיב עם אחר, נראית כחידה אבולוציונית. אם נדיבות פוגעת בסיכויי הפרט הנותן, איך גנים "נדיבים" יכולים להתפשט באוכלוסייה?</p>

    <h3>תיאוריית המשחקים: כלי לחשיפת סודות האסטרטגיה האבולוציונית</h3>
    <p>כאן נכנסת לתמונה תיאוריית המשחקים - ענף מתמטי שחוקר קבלת החלטות באינטראקציות שבהן התוצאה עבור שחקן אחד תלויה גם בהחלטות של שחקנים אחרים. בהקשר ביולוגי, "שחקנים" הם פרטים, ו"אסטרטגיות" הן התנהגויות שעוצבו על ידי האבולוציה. תיאוריית המשחקים עוזרת לחזות אילו אסטרטגיות יהיו יציבות לאורך זמן באוכלוסייה (אסטרטגיות יציבות אבולוציונית - ESS).</p>

    <h3>'הדילמה של האסיר': המלכוד הקלאסי של האנוכיות</h3>
    <p>'הדילמה של האסיר' היא המשחק המפורסם ביותר בתחום זה. דמיינו שני עבריינים שנתפסו ונחקרים בנפרד. לכל אחד שתי אפשרויות: לשתף פעולה עם שותפו (לשמור על שתיקה) או לבגוד בו (להעיד נגדו). התוצאות (שנות מאסר, כלומר שכר שלילי) הן:
    <ul>
        <li>שניהם שיתפו פעולה: מאסר קצר לשניהם (שכר R - Reward)</li>
        <li>אחד בגד, השני שיתף פעולה: הבוגד יוצא לחופשי (שכר T - Temptation), המשתף מקבל מאסר ארוך מאוד (שכר S - Sucker)</li>
        <li>שניהם בגדו: מאסר בינוני לשניהם (שכר P - Punishment)</li>
    </ul>
    בתנאי הדילמה הסטנדרטית: T > R > P > S. המשמעות היא שלכל שחקן, ללא קשר לבחירת השני, עדיף לבגוד (כי T > R וגם P > S). התוצאה "הרציונלית" במשחק חד-פעמי היא ששניהם יבגדו, למרות ששניהם ירוויחו יותר משיתוף פעולה הדדי (R > P). האנוכיות גוברת.</p>

    <h3>'הדילמה של האסיר החוזרת': כשהעבר משפיע על העתיד</h3>
    <p>מה קורה כשהמשחק משוחק שוב ושוב? ב'דילמה של האסיר החוזרת', שחקנים נפגשים שוב ושוב ויכולים "לזכור" את ההתנהגות הקודמת של היריב ולהגיב בהתאם. כאן, אסטרטגיות המבוססות על היסטוריה, כמו "עין תחת עין", הופכות להיות רלוונטיות. שחקן יכול להעניש בוגד או לתגמל משתף פעולה.</p>

    <h3>אסטרטגיות מפתח בטורניר האבולוציוני</h3>
    <p>הסימולציה למעלה מאפשרת לכם לראות כיצד ארבע אסטרטגיות בסיסיות מתחרות באוכלוסייה לאורך דורות, כאשר הצלחתן (הניקוד הממוצע שצברו) קובעת את מספר "הצאצאים" שלהן בדור הבא:</p>
    <ul>
        <li><strong>Always Cooperate (AC):</strong> אסטרטגיה "תמימה" שתמיד בוחרת לשתף פעולה. פגיעה ביותר מול בוגדים.</li>
        <li><strong>Always Defect (AD):</strong> אסטרטגיה אגרסיבית שתמיד בוחרת לבגוד. מצליחה מול תמימים, אך כושלת מול עצמה ומול אסטרטגיות נקמניות.</li>
        <li><strong>Tit-for-Tat (TFT):</strong> אסטרטגיית "הדדיות פשוטה". מתחילה בשיתוף פעולה, ולאחר מכן מחקה את מה שהיריב עשה בסיבוב הקודם. היא נחמדה (לא בוגדת ראשונה), נקמנית (מענישה בגידה מיד) וסלחנית (חוזרת לשתף פעולה אם היריב חוזר לשתף פעולה).</li>
        <li><strong>Random (RAND):</strong> אסטרטגיה שבוחרת לשתף פעולה או לבגוד באופן אקראי לחלוטין.</li>
    </ul>

    <h3>הניסויים המפורסמים של רוברט אקסלרוד</h3>
    <p>בשנות ה-80 ערך רוברט אקסלרוד סדרה של טורנירים ממוחשבים שבהם התמודדו אסטרטגיות שונות זו מול זו במשחק החוזר. להפתעת רבים, האסטרטגיה הפשוטה "עין תחת עין" (TFT) זכתה בשני הטורנירים. הצלחתה הדגימה כי שיתוף פעולה, המבוסס על הדדיות ותגובה להתנהגות יריבים, יכול להיות אסטרטגיה יציבה ואף כזו שיכולה לפלוש לאוכלוסייה של בוגדים טהורים בתנאים מסוימים.</p>

    <h3>מתי שיתוף פעולה אבולוציוני משתלם?</h3>
    <p>הצלחתן של אסטרטגיות כמו TFT תלויה במספר גורמים, אותם תוכלו לחקור בסימולציה:
    <ul>
        <li><strong>סבירות למפגשים חוזרים:</strong> ככל שגבוהה יותר הסבירות ששני פרטים ייפגשו שוב, כך גדל התמריץ לשמור על יחסים טובים ולא לבגוד. מספר מפגשים גבוה בסימולציה מגדיל את משקל העתיד.</li>
        <li><strong>יכולת זיהוי וזיכרון:</strong> פרטים צריכים להיות מסוגלים לזהות זה את זה ולזכור אינטראקציות קודמות. האסטרטגיות בסימולציה מניחות יכולת זו.</li>
        <li><strong>ערכי השכר:</strong> היחס בין T, R, P, ו-S קובע כמה "משתלם" לבגוד לעומת לשתף פעולה בכל סיבוב. שינוי ערכים אלה יכול להשפיע דרמטית על האסטרטגיה המנצחת.</li>
    </ul></p>

    <h3>דוגמאות מהטבע והחיים</h3>
    <p>עקרונות דילמת האסיר החוזרת מסייעים להבין מגוון התנהגויות:
    <ul>
        <li><strong>עטלפי ערפד:</strong> חולקים דם עם חברים רעבים, ומקבלים עזרה כשהם זקוקים לה.</li>
        <li><strong>טיפוח הדדי אצל קופים:</strong> קופים מטפחים אלה את אלה כתגמול על עזרה קודמת או כדי לבסס יחסים לעזרה עתידית.</li>
        <li><strong>בריתות פוליטיות ומסחר בינלאומי:</strong> מבוססים על אמון, גמול, והענשת הפרות הסכם.</li>
        <li><strong>יחסים בינאישיים:</strong> אמון, סלחנות, וכעס על בגידה מעצבים את היחסים שלנו עם חברים, משפחה ובני זוג.</li>
    </ul></p>
    <p>הסימולטור הוא כלי עוצמתי לחקור את הדינמיקה של אמון ובגידה ולראות במו עיניכם כיצד, בתנאים הנכונים, שיתוף פעולה יכול לא רק לשרוד, אלא אף לשגשג בעולם תחרותי.</p>
</div>

<script>
    // Game logic
    const COOPERATE = 'C';
    const DEFECT = 'D';

    // Strategy functions: take opponent's history and return C or D
    // Each strategy also has a display name and color
    const strategies = {
        'AC': {
            name: 'משתף פעולה',
            color: '#2ecc71', // Emerald Green
            strategy: (selfHistory, opponentHistory, payoffs) => COOPERATE
        },
        'AD': {
            name: 'בוגד',
             color: '#e74c3c', // Alizarin Red
            strategy: (selfHistory, opponentHistory, payoffs) => DEFECT
        },
        'TFT': {
             name: 'עין תחת עין',
             color: '#3498db', // Peter River Blue
             strategy: (selfHistory, opponentHistory, payoffs) => {
                // Start by cooperating
                if (opponentHistory.length === 0) {
                    return COOPERATE;
                } else {
                    // Do what the opponent did last turn
                    return opponentHistory[opponentHistory.length - 1];
                }
            }
        },
        'RAND': {
             name: 'אקראי',
             color: '#f39c12', // Orange
            strategy: (selfHistory, opponentHistory, payoffs) => Math.random() < 0.5 ? COOPERATE : DEFECT
        }
    };

    // Payoffs based on standard Prisoner's Dilemma notation (T > R > P > S, 2R > T + S)
    // T: Temptation (Defect vs Cooperate) - Defector's score
    // R: Reward (Cooperate vs Cooperate) - Both scores
    // P: Punishment (Defect vs Defect) - Both scores
    // S: Sucker's Payoff (Cooperate vs Defect) - Cooperator's score

    const defaultPayoffs = {
        T: 5, // Temptation to defect
        R: 3, // Reward for mutual cooperation
        P: 1, // Punishment for mutual defection
        S: 0  // Sucker's payoff
    };
    let currentPayoffs = { ...defaultPayoffs }; // Clone default

    // Simulation state
    let population = []; // Array of strategy keys (e.g., ['TFT', 'AD', 'TFT', ...])
    const populationSize = 100; // Fixed population size for simplicity
    let generation = 0;
    let isSimulationRunning = false;
    let simulationInterval = null;
    const numOpponentsPerIndividual = 10; // Each individual plays against this many random opponents per generation


    // DOM Elements - Get elements more robustly
    const initialACInput = document.getElementById('initial-ac');
    const initialADInput = document.getElementById('initial-ad');
    const initialTFTInput = document.getElementById('initial-tft');
    const initialRANDInput = document.getElementById('initial-rand');
    const initialInputs = [initialACInput, initialADInput, initialTFTInput, initialRANDInput];
    const totalPercentDisplay = document.getElementById('total-percent-display');


    const payoffTInput = document.getElementById('payoff-t');
    const payoffRInput = document.getElementById('payoff-r');
    const payoffPInput = document.getElementById('payoff-p');
    const payoffSInput = document.getElementById('payoff-s');

    const numInteractionsInput = document.getElementById('num-interactions');

    const startButton = document.getElementById('start-sim');
    const stepButton = document.getElementById('step-sim');
    const resetButton = document.getElementById('reset-sim');

    const currentGenerationSpan = document.getElementById('current-generation');
    const simulationStatusDiv = document.getElementById('simulation-status');

    const barAC = document.getElementById('bar-ac');
    const barAD = document.getElementById('bar-ad');
    const barTFT = document.getElementById('bar-tft');
    const barRAND = document.getElementById('bar-rand');
    const strategyBars = { 'AC': barAC, 'AD': barAD, 'TFT': barTFT, 'RAND': barRAND }; // Map keys to bars

    const percentAC = document.getElementById('percent-ac');
    const percentAD = document.getElementById('percent-ad');
    const percentTFT = document.getElementById('percent-tft');
    const percentRAND = document.getElementById('percent-rand');
    const percentSpans = { 'AC': percentAC, 'AD': percentAD, 'TFT': percentTFT, 'RAND': percentRAND }; // Map keys to spans


    const explanationDiv = document.getElementById('explanation');
    const showExplanationButton = document.getElementById('show-explanation');


    // --- Core Simulation Functions ---

    // Plays one round of the Prisoner's Dilemma
    function playRound(move1, move2, payoffs) {
        if (move1 === COOPERATE && move2 === COOPERATE) {
            return [payoffs.R, payoffs.R]; // Mutual Cooperation (R, R)
        } else if (move1 === DEFECT && move2 === COOPERATE) {
            return [payoffs.T, payoffs.S]; // Player 1 defects, Player 2 cooperates (T, S)
        } else if (move1 === COOPERATE && move2 === DEFECT) {
            return [payoffs.S, payoffs.T]; // Player 1 cooperates, Player 2 defects (S, T)
        } else if (move1 === DEFECT && move2 === DEFECT) {
            return [payoffs.P, payoffs.P]; // Mutual Defection (P, P)
        }
        return [0, 0]; // Should not happen
    }

    // Plays N rounds of the Iterated Prisoner's Dilemma between two strategies
    // Returns total scores for player1 and player2
    function playMatch(strategyKey1, strategyKey2, numRounds, payoffs) {
        const stratFunc1 = strategies[strategyKey1]?.strategy;
        const stratFunc2 = strategies[strategyKey2]?.strategy;

        if (!stratFunc1 || !stratFunc2) {
             console.error("Invalid strategy key provided to playMatch");
             return [0, 0];
        }

        let history1 = []; // History of player1's moves
        let history2 = []; // History of player2's moves
        let score1 = 0;
        let score2 = 0;

        for (let i = 0; i < numRounds; i++) {
            // Strategy function gets its *own* history and *opponent's* history
            const move1 = stratFunc1(history1, history2, payoffs);
            const move2 = stratFunc2(history2, history1, payoffs); // Pass histories in reversed order for player2

            const [s1, s2] = playRound(move1, move2, payoffs);

            score1 += s1;
            score2 += s2;

            // Record the moves that just happened for the *next* round
            history1.push(move1);
            history2.push(move2);
        }

        return [score1, score2];
    }

    // Shuffles an array (Fisher-Yates algorithm) - Not strictly needed with random opponent selection
    // function shuffleArray(array) {
    //     for (let i = array.length - 1; i > 0; i--) {
    //         const j = Math.floor(Math.random() * (i + 1));
    //         [array[i], array[j]] = [array[j], array[i]]; // Swap elements
    //     }
    //     return array;
    // }

    // Simulates one generation
    function runGeneration() {
        if (population.length === 0) {
             setStatus("האוכלוסייה ריקה. אנא אפס והתחל מחדש.", 'warning');
             stopSimulation();
             return;
        }
         if (population.length !== populationSize) {
              console.warn(`Population size mismatch: Expected ${populationSize}, got ${population.length}. Adjusting.`);
              // Attempt to fix population size if it drifted (shouldn't happen with current init/evolution logic)
              while(population.length < populationSize) population.push(Object.keys(strategies)[Math.floor(Math.random() * Object.keys(strategies).length)]);
              while(population.length > populationSize) population.pop(); // Remove last element
          }


        generation++;
        currentGenerationSpan.textContent = generation;
        setStatus(`מחשב דור ${generation}... 🧬`, 'info');


        const numInteractions = parseInt(numInteractionsInput.value, 10) || 10;
        const currentPopulationSize = population.length; // Should be populationSize
        let individualScores = Array(currentPopulationSize).fill(0); // Scores for each individual instance

        // Each individual plays against a fixed number of random opponents
         for(let i = 0; i < currentPopulationSize; i++) {
             const player1StrategyKey = population[i];
             let opponentsPlayed = 0;
             while (opponentsPlayed < numOpponentsPerIndividual) {
                 const randomOpponentIndex = Math.floor(Math.random() * currentPopulationSize);
                 // Allow playing against self if population is small, but ideally pick a different one
                 // if (randomOpponentIndex !== i || currentPopulationSize === 1) {
                    const player2StrategyKey = population[randomOpponentIndex];
                    const [score1, score2] = playMatch(player1StrategyKey, player2StrategyKey, numInteractions, currentPayoffs);
                    individualScores[i] += score1; // Add score earned by individual i
                    opponentsPlayed++;
                 // }
             }
         }

        // Calculate total score per strategy type and average fitness
        let strategyTotalScores = {};
        let strategyCounts = {};
        let totalPopulationScore = 0;

        Object.keys(strategies).forEach(key => {
            strategyTotalScores[key] = 0;
            strategyCounts[key] = 0;
        });

        for(let i = 0; i < currentPopulationSize; i++) {
            const stratKey = population[i];
            strategyTotalScores[stratKey] += individualScores[i];
            strategyCounts[stratKey]++;
            totalPopulationScore += individualScores[i];
        }

        // Determine the next generation's population based on fitness (total score)
        let nextPopulation = [];

        if (totalPopulationScore === 0) {
             setStatus("סך הניקוד באוכלוסייה הוא 0. הסימולציה נעצרת.", 'warning');
             stopSimulation();
             return;
        }

        // Proportional selection: The number of offspring of a strategy is proportional to its total score
        Object.keys(strategies).forEach(key => {
             const totalScoreForStrategy = strategyTotalScores[key];
             // Avoid division by zero if no individuals of this strategy existed
             if (strategyCounts[key] > 0) {
                 // Calculate the expected number of individuals of this strategy in the next generation
                 const expectedIndividuals = (totalScoreForStrategy / totalPopulationScore) * populationSize;

                 // Add individuals to the next population (use Math.round for integer counts)
                 const numToAdd = Math.round(expectedIndividuals);
                 for (let i = 0; i < numToAdd; i++) {
                    // Ensure we don't exceed the target population size during addition
                    if (nextPopulation.length < populationSize) {
                         nextPopulation.push(key);
                    } else {
                         // If we've already reached the size, stop adding
                         break;
                    }
                 }
             }
        });

        // Final population size adjustment to ensure it's exactly populationSize
        // This might be necessary due to rounding, especially if one strategy dominates completely or disappears.
        while (nextPopulation.length < populationSize) {
            // If population is too small, add a random strategy *from the ones that had some score*.
             // This biases towards strategies that were somewhat successful.
             const keysWithScore = Object.keys(strategyTotalScores).filter(key => strategyTotalScores[key] > 0);
             if (keysWithScore.length > 0) {
                  nextPopulation.push(keysWithScore[Math.floor(Math.random() * keysWithScore.length)]);
             } else {
                 // Fallback: if NO strategy had score > 0 (should be caught above), add random from all.
                 const allKeys = Object.keys(strategies);
                 nextPopulation.push(allKeys[Math.floor(Math.random() * allKeys.length)]);
             }
        }
         while (nextPopulation.length > populationSize) {
             // If population is too large, remove a random strategy
             nextPopulation.splice(Math.floor(Math.random() * nextPopulation.length), 1);
         }

        // Shuffle the next population to mix them for the next generation's pairings (important!)
        population = shuffleArray(nextPopulation);


        // Update UI
        updatePopulationDisplay();
         // Simple check for outcome
        const currentPercentages = calculatePopulationPercentages();
        let outcomeMessage = "האוכלוסייה התפתחה.";
        if (currentPercentages['AD'] > 95) outcomeMessage = "⚔️ הבוגדים השתלטו על האוכלוסייה!";
        else if (currentPercentages['AC'] > 95) outcomeMessage = "😇 המשתפים השתלטו (ייתכן שאין בוגדים או תנאים מתאימים).";
        else if (currentPercentages['TFT'] > 95) outcomeMessage = "👑 'עין תחת עין' שולטת! שיתוף פעולה הדדי יציב.";
         else if (currentPercentages['AD'] < 5 && currentPercentages['AC'] < 5 && currentPercentages['TFT'] < 5 && currentPercentages['RAND'] < 5) outcomeMessage = "אוכלוסייה נכחדה? התאפס והתחל מחדש.";
         else if (Object.keys(currentPercentages).filter(key => currentPercentages[key] > 1).length === 1) {
             const dominantStrat = Object.keys(currentPercentages).find(key => currentPercentages[key] > 95);
             if (dominantStrat) outcomeMessage = `🎉 האסטרטגיה '${strategies[dominantStrat].name}' השתלטה על האוכלוסייה!`;
         }
         else if (generation > 0) {
             outcomeMessage = `דור ${generation} הסתיים. האוכלוסייה התפתחה.`;
         }


        setStatus(`${outcomeMessage} לחץ 'דור הבא' או 'עצור'.`, 'success');
    }

     // Helper to calculate percentages for display
     function calculatePopulationPercentages() {
         const counts = {};
         Object.keys(strategies).forEach(key => counts[key] = 0);
         population.forEach(strat => counts[strat]++);

         const total = population.length || 1; // Avoid division by zero
         const percentages = {};
         Object.keys(strategies).forEach(key => {
             percentages[key] = (counts[key] / total) * 100;
         });
         return percentages;
     }


    // Updates the visual representation of the population
    function updatePopulationDisplay() {
        const percentages = calculatePopulationPercentages();

         // Update bar widths and percentages
         Object.keys(strategies).forEach(key => {
             const bar = strategyBars[key];
             const percentSpan = percentSpans[key];
             const percentage = percentages[key];

             if (bar) bar.style.width = percentage + '%';
             if (percentSpan) percentSpan.textContent = percentage.toFixed(1);
         });
          // Also update the total percent display
          updateTotalPercentDisplay();

    }

    // Helper to set status message
    function setStatus(message, type = 'info') {
         simulationStatusDiv.textContent = message;
         // Optional: Add classes for different status types (e.g., info, warning, success) for styling
         simulationStatusDiv.className = `status-message status-${type}`;
    }

     // Update total percentage display and validation message
    function updateTotalPercentDisplay() {
         let total = 0;
         initialInputs.forEach(input => {
             total += parseInt(input.value, 10) || 0;
         });
         totalPercentDisplay.textContent = `סה"כ: ${total}%`;

         if (total !== 100) {
              totalPercentDisplay.classList.add('percent-warning');
              setStatus("⚠️ סך האחוזים אינו 100%. האוכלוסייה תותאם לגודל 100 על בסיס היחסים.", 'warning');
              // Disable start/step buttons if total is 0, even if we adjust
              if (total === 0) {
                  startButton.disabled = true;
                  stepButton.disabled = true;
                  setStatus("יש להזין אחוז התחלתי הגדול מ-0 עבור אסטרטגיה כלשהי.", 'warning');
              } else {
                   startButton.disabled = false;
                   stepButton.disabled = false;
              }

         } else {
              totalPercentDisplay.classList.remove('percent-warning');
              setStatus("מוכן לסימולציה. לחץ 'התחל' או 'דור הבא'.", 'info');
              startButton.disabled = false;
              stepButton.disabled = false;
         }
     }


    // --- Button Event Handlers ---

    function startSimulation() {
        if (!isSimulationRunning) {
            if (generation === 0) {
                const initialized = initializeSimulation();
                if (!initialized) return; // Don't start if init failed
            }
             isSimulationRunning = true;
             startButton.textContent = '⏹️ עצור סימולציה';
             startButton.classList.replace('btn-play', 'btn-stop');
             stepButton.disabled = true; // Disable step while running
             resetButton.disabled = true; // Disable reset while running
             // Determine speed: faster for more interactions, up to a limit? Or fixed? Fixed is simpler.
             // const intervalTime = Math.max(100, 500 - (parseInt(numInteractionsInput.value, 10) * 10)); // Example speed logic
             simulationInterval = setInterval(runGeneration, 400); // Run a generation every 400ms
             setStatus(`הסימולציה פועלת... דור ${generation} 🏃`, 'info');
        } else {
            stopSimulation();
        }
    }

    function stopSimulation() {
        if (isSimulationRunning) {
            isSimulationRunning = false;
            startButton.textContent = '▶️ המשך סימולציה';
            startButton.classList.replace('btn-stop', 'btn-play');
            stepButton.disabled = false; // Enable step when stopped
            resetButton.disabled = false; // Enable reset when stopped
            clearInterval(simulationInterval);
            setStatus(`הסימולציה הושהתה בדור ${generation}.`, 'info');
        }
    }

    function stepSimulation() {
        if (!isSimulationRunning) { // Only step if not continuously running
             if (generation === 0) {
                 const initialized = initializeSimulation();
                 if (!initialized) return;
             }
             runGeneration();
        }
    }

    function resetSimulation() {
        stopSimulation();
        generation = 0;
        population = []; // Clear population array
        currentGenerationSpan.textContent = generation;

        // Reset initial percentages in inputs to default
        initialACInput.value = 25;
        initialADInput.value = 25;
        initialTFTInput.value = 25;
        initialRANDInput.value = 25;
        updateTotalPercentDisplay(); // Update display immediately

         // Reset payoffs to default values and internal state
         payoffTInput.value = defaultPayoffs.T;
         payoffRInput.value = defaultPayoffs.R;
         payoffPInput.value = defaultPayoffs.P;
         payoffSInput.value = defaultPayoffs.S;
         currentPayoffs = { ...defaultPayoffs };

         // Reset interactions input
         numInteractionsInput.value = 10;

        // Update display to show 0% or initial setup state
        updatePopulationDisplay(); // This will show 0% for all bars initially
        setStatus("🔄 סימולציה אותחלה מחדש. הגדר פרמטרים והתחל.", 'info');
        startButton.textContent = '▶️ התחל סימולציה';
        startButton.classList.replace('btn-stop', 'btn-play');
        stepButton.disabled = false;
        resetButton.disabled = false;
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        showExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט 🔽' : 'הצג הסבר מפורט ▶️';
        showExplanationButton.classList.toggle('active', isHidden); // Optional: add active state styling
    }


    // --- Initialize on page load ---
    window.onload = () => {
        // Add event listeners
        startButton.addEventListener('click', startSimulation);
        stepButton.addEventListener('click', stepSimulation);
        resetButton.addEventListener('click', resetSimulation);
        showExplanationButton.addEventListener('click', toggleExplanation);

         // Add input event listeners to update total percentage display
         initialInputs.forEach(input => {
             input.addEventListener('input', updateTotalPercentDisplay);
         });


        // Initial setup
        resetSimulation(); // Call reset to set initial state and UI

         // Ensure explanation is hidden on load even if CSS fails or JS runs late
         explanationDiv.style.display = 'none';
         showExplanationButton.textContent = 'הצג הסבר מפורט ▶️';
    };

    // Helper to shuffle array (Fisher-Yates) - moved here to be defined before use
    function shuffleArray(array) {
        let currentIndex = array.length, randomIndex;
        // While there remain elements to shuffle.
        while (currentIndex != 0) {
            // Pick a remaining element.
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex--;
            // And swap it with the current element.
            [array[currentIndex], array[randomIndex]] = [
                array[randomIndex], array[currentIndex]];
        }
        return array;
    }


</script>
```