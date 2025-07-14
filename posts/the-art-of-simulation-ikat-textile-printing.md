---
title: "אמנות הסימול: מסע אל קסם הדפסת טקסטיל בטכניקת איקט"
english_slug: the-art-of-simulation-ikat-textile-printing
category: "אמנות ועיצוב / כללי"
tags:
  - textile
  - ikat
  - printing
  - dyeing
  - crafts
  - simulation
---
# אמנות הסימול: מסע אל קסם הדפסת טקסטיל בטכניקת איקט

הביטו לרגע באריג איקט. דמיינו את הדוגמאות העשירות, ולצידן, את קווי המתאר המעט רכים, המטושטשים באלגנטיות. האם ידעתם שהקסם הזה נוצר *לפני* האריגה עצמה, על ידי צביעה מיוחדת של החוטים? בואו לגלות את הסוד, שלב אחר שלב, באמצעות סימולציה אינטראקטיבית.

<div id="ikat-simulation-app">
    <h2>סימולציית יצירת דוגמת איקט (איקט שתי פשוט)</h2>
    <p class="intro-text">צאו למסע מרתק בעקבות אומני האיקט: קשרו את החוטים, צבעו, הסירו קשרים, צבעו שוב – וצפו בדוגמה הקסומה שלכם מתגלה!</p>

    <div class="simulation-area">
        <div class="threads-container current-view">
            <h4 class="view-title">חוטי השתי המתוחים - הבד הלבן שלכם:</h4>
            <div id="initial-threads" class="threads"></div>
             <p class="interaction-hint">לחצו על מקטעים בחוטים כדי "לקשור" אותם. קשירה חוסמת את הצבע מלהגיע למקטע.</p>
        </div>

        <div class="controls">
            <h4 class="controls-title">שער הסודות של האיקט: השלבים שלכם</h4>
            <div id="step-1" class="step active">
                <h5><span class="step-number">1</span> שלב ראשון: קשירה - חסימת הצבע הראשון</h5>
                <p>בחרו את המקטעים שתרצו להשאיר ללא הצבע הראשון. כל לחיצה "קושרת" או "מתירה" מקטע (במצב קשירה).</p>
                <div class="button-group">
                    <button onclick="resetTies()" class="secondary-button">איפוס קשירות הכל</button>
                </div>
            </div>
            <div id="step-2" class="step">
                <h5><span class="step-number">2</span> שלב שני: הצביעה הראשונה - הטבילה בצבע</h5>
                <p>בחרו צבע ראשון. רק מקטעים שאינם קשורים ייצבעו בצבע זה. לאחר הצביעה, הקשירות של שלב 1 יוסרו אוטומטית.</p>
                <div class="button-group">
                    <select id="dye-color">
                        <option value="#e74c3c">אדום אש</option>
                        <option value="#3498db">כחול שמיים</option>
                        <option value="#2ecc71">ירוק עד</option>
                        <option value="#f1c40f">צהוב שמש</option>
                        <option value="#9b59b6">סגול מלכותי</option>
                    </select>
                    <button onclick="dyeThreads(document.getElementById('dye-color').value)" class="primary-button">צבעו עכשיו!</button>
                </div>
            </div>
            <div id="step-3" class="step">
                <h5><span class="step-number">3</span> שלב שלישי: קשירה מחדש - חסימת הצבע השני</h5>
                 <p>כעת, החוטים צבועים בצבע הראשון. קשרו מקטעים שתרצו לחסום מהצבע הבא. לחיצה "קושרת" או "מתירה".</p>
                  <div class="button-group">
                     <button onclick="resetTies()" class="secondary-button">איפוס קשירות הכל</button>
                  </div>
            </div>
             <div id="step-4" class="step">
                <h5><span class="step-number">4</span> שלב רביעי: הצביעה השנייה - עוד שכבת קסם</h5>
                <p>בחרו צבע שני. רק מקטעים שאינם קשורים כרגע ייצבעו בצבע זה (או ישתלבו עם הצבע הקיים).</p>
                <div class="button-group">
                    <select id="dye-color-2">
                         <option value="#3498db">כחול שמיים</option>
                         <option value="#e74c3c">אדום אש</option>
                        <option value="#2ecc71">ירוק עד</option>
                        <option value="#f1c40f">צהוב שמש</option>
                         <option value="#9b59b6">סגול מלכותי</option>
                         <option value="#e67e22">כתום לוהט</option>
                    </select>
                    <button onclick="dyeThreads(document.getElementById('dye-color-2').value, true)" class="primary-button">צבעו שוב!</button>
                </div>
            </div>
            <div id="step-5" class="step">
                <h5><span class="step-number">5</span> שלב אחרון: הסרת הקשרים וחשיפת הדוגמה</h5>
                <p>כל הקשרים מוסרים. זהו הרגע הקסום בו החוטים הצבועים מוכנים לאריגה. צפו בתוצאה הסופית!</p>
                <div class="button-group">
                    <button onclick="showResults()" class="primary-button">הצג את הבד שלי!</button>
                    <button onclick="resetSimulation()" class="secondary-button">התחלה חדשה</button>
                </div>
            </div>
        </div>

        <div class="results-container">
             <div class="threads-preview current-view">
                <h4 class="view-title">חוטי השתי הצבועים לאחר הסרת הקשרים:</h4>
                <div id="dyed-threads" class="threads"></div>
             </div>
             <div class="weaving-preview current-view">
                 <h4 class="view-title">והנה קסם האריגה - הדמיית אריג האיקט שלכם:</h4>
                <div id="woven-pattern"></div>
             </div>
             <div class="final-buttons button-group">
                 <button onclick="resetSimulation()" class="primary-button">צור דוגמה חדשה!</button>
             </div>
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    #ikat-simulation-app {
        font-family: 'Heebo', sans-serif;
        max-width: 960px;
        margin: 30px auto;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background: linear-gradient(to bottom right, #fcfcfc, #f0f0f0);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        color: #333;
        overflow: hidden; /* Clear floats/margins */
    }
    #ikat-simulation-app h2, #ikat-simulation-app h4, #ikat-simulation-app h5 {
        color: #5d4a66; /* Deep purple */
        text-align: center;
        margin-bottom: 15px;
    }
     #ikat-simulation-app h2 {
         margin-bottom: 5px;
         font-size: 2em;
     }
     #ikat-simulation-app h4 {
         font-size: 1.4em;
         color: #7a678f;
     }
     #ikat-simulation-app h5 {
         font-size: 1.1em;
         color: #7a678f;
         margin-bottom: 10px;
         display: flex;
         align-items: center;
         justify-content: center;
     }
     .step-number {
         display: inline-flex;
         align-items: center;
         justify-content: center;
         width: 25px;
         height: 25px;
         background-color: #5d4a66;
         color: white;
         border-radius: 50%;
         font-size: 0.9em;
         margin-left: 8px;
         font-weight: normal;
     }

     #ikat-simulation-app p {
        text-align: center;
        color: #555;
        margin-bottom: 15px;
        line-height: 1.5;
    }
    p.intro-text {
        font-size: 1.1em;
        font-style: italic;
        color: #555;
        margin-bottom: 25px;
    }

    .simulation-area {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
     .threads-container, .results-container {
         width: 100%;
         margin-bottom: 30px;
         background-color: #fff;
         padding: 15px;
         border-radius: 8px;
         box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
         box-sizing: border-box;
     }

     .threads-container.current-view {
         /* highlight current interaction area */
         border: 2px solid #a392b3; /* Purple border */
         box-shadow: 0 0 15px rgba(163, 146, 179, 0.5);
     }


    .threads {
        display: flex;
        flex-direction: row; /* Represents parallel threads */
        justify-content: center;
        align-items: stretch;
        margin: 20px 0;
        border: 1px solid #ccc;
        padding: 10px;
        background-color: #fff;
        min-height: 80px; /* Ensure visibility */
        overflow-x: auto; /* Add scroll for many threads */
        border-radius: 5px;
    }

    .thread {
        display: flex;
        flex-direction: column; /* Segments stacked vertically */
        width: 18px; /* Slightly wider threads */
        margin: 0 1.5px; /* Small gap between threads */
        /* border-left: 1px dotted #eee; */ /* Removed dotted border */
        position: relative; /* For segment outlines */
    }
     /* Add a subtle thread separator visual */
    .thread + .thread::before {
        content: '';
        position: absolute;
        left: -1.5px; /* Position between threads */
        top: 0;
        bottom: 0;
        width: 1px;
        background-color: #eee;
    }


    .segment {
        flex-grow: 1; /* Segments fill the height */
        background-color: #f8f8f8; /* Initial segment color */
        margin-bottom: 1px; /* Small gap between segments */
        cursor: pointer;
        position: relative;
        transition: background-color 0.5s ease, box-shadow 0.2s ease;
        border: 0.5px solid #eee; /* Subtle segment outline */
        box-sizing: border-box;
    }

    .segment:hover:not(.tied) {
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    }

    .segment.tied {
        /*background-color: #d3d3d3; */ /* Tied segments might retain underlying color */
         /* Use overlay for tied visual */
        position: relative; /* Ensure stacking context */
    }
    .segment.tied::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: repeating-linear-gradient(
            45deg,
            rgba(0,0,0,0.2),
            rgba(0,0,0,0.2) 3px,
            rgba(255,255,255,0.1) 3px,
            rgba(255,255,255,0.1) 6px
        ); /* Visual indication of being tied */
        z-index: 1; /* Ensure overlay is above background color */
         opacity: 0.8;
         pointer-events: none; /* Allow clicks to pass through overlay */
    }

     /* Pulsing animation for clicked segments */
    .segment.clicked {
        animation: pulse 0.3s ease-in-out;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }


    .controls {
        display: flex;
        flex-direction: column;
        gap: 20px; /* Increased gap */
        padding: 20px; /* Increased padding */
        border: 1px solid #e0e0e0;
        background-color: #fff;
        border-radius: 8px;
        width: 100%;
        box-sizing: border-box;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

     .controls-title {
         text-align: center;
         margin-bottom: 20px;
         color: #5d4a66;
     }

     .step {
         border-bottom: 1px dashed #eee;
         padding-bottom: 20px; /* Increased padding */
         margin-bottom: 20px; /* Increased margin */
         text-align: center;
         opacity: 0.5; /* Default state: dimmed */
         pointer-events: none; /* Default state: not interactive */
          transition: opacity 0.3s ease;
     }
     .step.active {
         opacity: 1; /* Active state: fully visible */
         pointer-events: auto; /* Active state: interactive */
         border-color: #a392b3; /* Highlight active step border */
     }

     .step:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }

     .button-group {
         display: flex;
         flex-wrap: wrap; /* Allow wrapping on small screens */
         justify-content: center;
         gap: 10px; /* Space between buttons */
         margin-top: 15px;
     }

     .controls button, .controls select {
         padding: 10px 20px; /* Slightly larger padding */
         border: none;
         border-radius: 5px; /* More rounded corners */
         cursor: pointer;
         font-size: 1em;
         transition: background-color 0.2s ease, transform 0.1s ease;
         font-family: 'Heebo', sans-serif;
     }
     .controls button.primary-button {
         background-color: #a392b3; /* Soft purple */
         color: white;
     }
     .controls button.primary-button:hover {
         background-color: #8e7aa1; /* Darker purple */
         transform: translateY(-1px); /* Subtle hover effect */
     }
      .controls button.primary-button:active {
         transform: translateY(0);
      }

     .controls button.secondary-button {
         background-color: #e0e0e0; /* Light grey */
         color: #555;
     }
     .controls button.secondary-button:hover {
         background-color: #d5d5d5; /* Darker grey */
         transform: translateY(-1px); /* Subtle hover effect */
     }
      .controls button.secondary-button:active {
         transform: translateY(0);
      }


     .controls select {
          background-color: #f0f0f0; /* Light background */
          color: #333;
          border: 1px solid #ccc;
          cursor: pointer;
          min-width: 120px; /* Ensure decent width */
     }
     .controls select:focus {
         outline-color: #a392b3;
     }


    .results-container {
        display: none; /* Initially hidden */
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
         padding-top: 20px;
         border-top: 1px dashed #ccc;
    }
     .results-container.visible {
          display: flex;
          animation: fadeIn 0.5s ease-out;
     }

    .threads-preview, .weaving-preview {
        margin-top: 20px;
        width: 100%;
         background-color: #fff;
         padding: 15px;
         border-radius: 8px;
         box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
         box-sizing: border-box;
    }

    #dyed-threads .segment {
         cursor: default; /* Not interactive after dyeing */
         border: none; /* No border on dyed segments */
         margin-bottom: 0; /* No gap between segments in preview */
    }

    #dyed-threads .thread {
        margin: 0 0.5px; /* Tighter packing in preview */
    }
     #dyed-threads .thread + .thread::before {
        left: -0.5px;
     }


    #woven-pattern {
        display: grid;
        /* Grid columns and rows will be set by JS based on simulation size */
        border: 1px solid #ccc;
        margin-top: 15px;
        box-sizing: border-box;
         border-radius: 5px;
        overflow: hidden; /* Hide potential fractional pixel issues */

        /* Add subtle blur for Ikat effect */
        filter: blur(0.3px); /* Small blur */
         /* Consider adding more complex gradients/shadows for perceived texture if needed */
    }

    .weave-cell {
        width: 15px; /* Width of a single cell in the pattern */
        height: 15px; /* Height of a single cell */
        background-color: #fff; /* Default color */
        box-sizing: border-box;
    }

     .final-buttons {
         margin-top: 30px;
         padding-top: 20px;
         border-top: 1px dashed #eee;
     }

    button#toggle-explanation {
        display: block;
        width: fit-content;
        margin: 30px auto 20px auto; /* More space around */
        padding: 12px 25px; /* Larger padding */
        background-color: #7a678f; /* Match theme */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
         font-family: 'Heebo', sans-serif;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    button#toggle-explanation:hover {
         background-color: #5d4a66;
          transform: translateY(-1px);
    }
     button#toggle-explanation:active {
         transform: translateY(0);
     }


    #explanation {
        display: none; /* Initially hidden */
        margin-top: 30px;
        padding: 20px;
        border-top: 1px solid #e0e0e0;
        background-color: #f9f9f9;
        border-radius: 8px;
         line-height: 1.7;
    }
    #explanation h2 {
        text-align: center;
        color: #34495e;
        margin-bottom: 20px;
        font-size: 1.8em;
    }
    #explanation h3 {
        color: #2c3e50;
        margin-top: 25px;
        margin-bottom: 12px;
         font-size: 1.3em;
         border-bottom: 1px dashed #eee;
         padding-bottom: 5px;
    }
    #explanation p {
        text-align: justify;
        margin-bottom: 15px;
        color: #555;
    }
     #explanation ul {
         margin-bottom: 15px;
         line-height: 1.6;
         padding-left: 20px; /* Indent list */
     }
     #explanation li {
         margin-bottom: 8px;
         color: #555;
         list-style-type: disc; /* Use bullet points */
     }

     /* Animations */
     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }
     @keyframes slideInFromLeft {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
     }

</style>

<button id="toggle-explanation">סקרנים? לחצו לחשיפת הסבר מקיף על טכניקת איקט</button>

<div id="explanation">
    <h2>על טכניקת האיקט - האמנות שנוצרת לפני האריגה</h2>

    <h3>מהי טכניקת איקט?</h3>
    <p>איקט (Ikat) אינה שיטת הדפסה על בד גמור, אלא טכניקת צביעת טקסטיל גאונית שבה החוטים עצמם (חוטי שתי, חוטי ערב, או שניהם גם יחד) נצבעים בשיטת ה"רזרב" (Resist dyeing) *לפני* שהם נארגים לכדי בד סופי. הרעיון דומה לשיטות צביעה כמו באטיק: אזורים בחוטים שאינם מיועדים להיצבע בצבע מסוים נאטמים ו"נחסמים" באמצעות קשרים הדוקים (בדרך כלל מחומרים כמו גומי או סיבים עמידים). החוטים הקשורים נטבלים באמבט צבע, הצבע חודר רק לאזורים החשופים, והאזורים הקשורים נשארים בצבעם המקורי (או נשמרים לצביעה בצבע אחר בהמשך התהליך המורכב). לאחר הצביעה, הקשרים מוסרים, והחוטים הצבועים נארגים ליצירת דוגמה מרהיבה. התוצאה הייחודית, המזוהה כל כך עם איקט, היא קווי מתאר מעט מטושטשים ורכים בדוגמה - אפקט הנוצר מתזוזות קלות ובלתי נמנעות של החוטים במהלך תהליך האריגה. טכניקה עתיקה זו משמשת זה אלפי שנים ומופיעה בתרבויות שונות ברחבי העולם, מדרום אמריקה, דרך מרכז ודרום מזרח אסיה (אינדונזיה ידועה במיוחד), הודו, יפן, ועד אפריקה, כשכל אזור מפתח סגנון ומוטיבים משלו.</p>

    <h3>איקט שתי, איקט ערב ואיקט כפול: וריאציות על נושא</h3>
    <p>הטכניקה הבסיסית משתנה בהתאם לסוג החוטים הנצבעים:</p>
    <ul>
        <li>**איקט שתי (Warp Ikat):** זוהי הצורה הנפוצה והפשוטה יחסית של איקט (וזו שהסימולציה שלנו מדגימה). רק חוטי השתי (החוטים האורכיים המתוחים על הנול) נצבעים מראש בטכניקת האיקט. חוטי הערב (החוטים הרוחביים הנארגים לתוך השתי) הם בדרך כלל בצבע אחיד. הדוגמה המתוכננת נראית בבירור לאורך חוטי השתי באריג הסופי.</li>
        <li>**איקט ערב (Weft Ikat):** במקרה זה, רק חוטי הערב נצבעים מראש. חוטי השתי הם בדרך כלל בצבע אחיד. יצירת דוגמה מדויקת באיקט ערב דורשת מיומנות אריגה גבוהה במיוחד, שכן האורג חייב "לקרוא" את הדוגמה על חוטי הערב וליישר אותם בדיוק רב במהלך האריגה כדי שהדוגמה הרצויה תתגלה.</li>
        <li>**איקט כפול (Double Ikat):** זוהי פסגת האומנות של האיקט, הטכניקה המורכבת והיוקרתית ביותר. גם חוטי השתי וגם חוטי הערב נצבעים מראש בטכניקת האיקט, *באופן שתואם זה לזה בצורה מושלמת*. זה דורש תיאום קיצוני הן בשלבי הקשירה והצביעה המרובים של שני סוגי החוטים והן בשלב האריגה עצמו, שבו על האורג לגרום לדוגמאות על השתי והערב להתחבר בדיוק כדי ליצור את הדוגמה השלמה באריג. בד ה"פאטולה" (Patola) המפורסם ממדינת גוג'ראט שבהודו הוא דוגמה קלאסית ונדירה לאיקט כפול.</li>
    </ul>

    <h3>מסע ארוך ומדויק: השלבים המרכזיים ביצירת בד איקט</h3>
    <p>תהליך יצירת בד איקט הוא עמלני, גוזל זמן רב, ולעיתים קרובות דורש שיתוף פעולה בין מומחים שונים – מומחי צביעה ומומחי אריגה. השלבים העיקריים כוללים:</p>
    <ul>
        <li>**בחירת והכנת החוטים:** בחירת חוטים איכותיים המתאימים לצביעה (כמו משי או כותנה) ומתיחתם על מסגרות מיוחדות או כלי עבודה שמאפשרים גישה נוחה לקשירה.</li>
        <li>**תכנון הדוגמה וסימונה:** שרטוט וסימון הדוגמה המדויקת על החוטים המתוחים. זהו שלב מכריע שקובע את מראה הבד הסופי.</li>
        <li>**שלב הקשירה (הראשון והחוזרים):** זהו לב ליבה של טכניקת האיקט. מקטעים לאורך החוטים שאמורים להישאר ללא צבע (או להיצבע בצבע אחר בשלב מאוחר יותר) נקשרים בחוזקה רבה באמצעות חומרים חוסמים. קשירה הדוקה היא המפתח למניעת חדירת צבע.</li>
        <li>**שלב הצביעה (הראשון והחוזרים):** החוטים הקשורים נטבלים באמבטיות צבע. הצבעים נצבעים בדרך כלל מהבהיר אל הכהה. אם הדוגמה כוללת מספר צבעים, התהליך חוזר על עצמו: צביעה בצבע אחד, הסרת חלק מהקשרים, קשירת אזורים אחרים, וצביעה בצבע הבא. זהו שלב מורכב שמצריך תכנון מדויק.</li>
        <li>**הסרת כל הקשרים:** לאחר סיום כל שלבי הצביעה והייבוש, כל הקשרים מוסרים בזהירות. החוטים חושפים כעת את הדוגמה המתוכננת בפסים צבועים ואזורים לא צבועים.</li>
        <li>**שלב האריגה:** החוטים הצבועים מותקנים על הנול, ומתבצעת האריגה. האורג משתמש בחוטים הצבועים כ"צבעים" על הנול כדי ליצור את הדוגמה הסופית. במיוחד באיקט ערב ואיקט כפול, שלב זה דורש מיומנות גבוהה כדי להבטיח שהדוגמה תתגלה באופן הרצוי.</li>
    </ul>

    <h3>הטשטוש המפורסם: למה דוגמאות האיקט מעט מטושטשות?</h3>
    <p>המאפיין הוויזואלי המיידי של איקט הוא הגבולות הרכים והמעט מטושטשים של הדוגמאות, בניגוד לקווים החדים של הדפסה רגילה. אפקט זה אינו "פגם", אלא חלק מהיופי והאותנטיות של הטכניקה, והוא נוצר בעיקר משתי סיבות עיקריות:</p>
    <ul>
        <li>**חדירת צבע עדינה לשוליים:** גם עם הקשירה ההדוקה ביותר, לעיתים קרובות כמות מינימלית של צבע מצליחה לחלחל אל קצוות האזורים הקשורים. חדירה קלה זו יוצרת מעבר צבע עדין והדרגתי בשולי הדוגמה, במקום קו חד ומוגדר.</li>
        <li>**תזוזה טבעית של החוטים באריגה:** לאחר הסרת הקשרים, החוטים הצבועים אינם תמיד ישרים לחלוטין, והעובי שלהם עשוי להשתנות מעט לאורך אורכם. כאשר החוטים נארגים על הנול תחת מתיחות וחיכוך, הם זזים מעט ממיקומם המדויק שתכונן מראש בשלב הצביעה. תזוזות קלות אלו גורמות לקווי הדוגמה להיראות מעט "רועדים", לא אחידים, או מטושטשים באריג הסופי. זהו הסימן המובהק לעבודת יד מורכבת ומאפיין חיוני המעניק לבד איקט את המראה האמנותי והאורגני שלו.</li>
    </ul>

    <h3>איקט בעולם: מסורות, סגנונות ודוגמאות אייקוניות</h3>
    <p>טכניקת האיקט התפתחה באופן עצמאי או נדדה בין תרבויות, ושימשה ליצירת בדים מרהיבים במגוון רחב של סגנונות:</p>
    <ul>
        <li>**אינדונזיה:** במיוחד באיים כמו באלי, סומבה, וסומטרה, נפוצים אריגי איקט מורכבים, לעיתים קרובות בשימוש טכניקת איקט כפול נדירה (כמו בד הגרינגסינג מבאלי) ובשימוש בצבעים טבעיים ומוטיבים מסורתיים בעלי משמעות רוחנית.</li>
        <li>**הודו:** מפורסמת בזכות אריגי ה"פאטולה" (Patola) מגוג'ראט – אריגי משי באיקט כפול הנחשבים ליוקרתיים ביותר, עם דוגמאות גיאומטריות צבעוניות. באוריסה נפוץ איקט שתי וערב עם מוטיבים של חיות וצמחים.</li>
        <li>**מרכז אסיה:** מדינות כמו אוזבקיסטן וטג'יקיסטן ידועות באריגי משי באיקט שתי, כמו "אדראס" (Adras) ו"אברבאנדי" (Abraband), המתאפיינים בצבעים עזים במיוחד (אדום, צהוב, סגול, כחול) ודוגמאות נועזות ומופשטות.</li>
        <li>**יפן:** טכניקת האיקט המקומית, הנקראת "קסורי" (Kasuri), מתאפיינת לרוב בדוגמאות עדינות, גיאומטריות או מופשטות, ובשימוש בצבעים מאופקים יותר, כמו אינדיגו.</li>
    </ul>
    <p>כל אחד מהסגנונות הללו מספר סיפור על המקום שבו נוצר, על חומרי הגלם הזמינים, על המסורות האמנותיות ועל העולם הרוחני של היוצרים. האיקט נותר דוגמה מרתקת לאופן שבו טכניקה בסיסית יכולה להניב אינסוף וריאציות אמנותיות ותרבותיות.</p>
</div>

<script>
    const NUM_THREADS = 20; // Number of warp threads
    const NUM_SEGMENTS = 10; // Number of segments per thread
    let threadState = []; // Array of arrays: threadState[i][j] = { tied: boolean, color: string }
    let currentStep = 1; // Track the current step in the simulation
    const stepsContainer = document.querySelector('.controls');
    const stepElements = stepsContainer.querySelectorAll('.step');
    const initialThreadsContainer = document.getElementById('initial-threads').closest('.threads-container');
    const resultsContainer = document.querySelector('.results-container');

    // --- Utility Functions ---
    function updateStepVisibility() {
        stepElements.forEach(stepEl => {
            const stepNum = parseInt(stepEl.id.replace('step-', ''));
            if (stepNum === currentStep) {
                stepEl.classList.add('active');
            } else {
                stepEl.classList.remove('active');
            }
        });

         // Update interaction area highlight
         if (currentStep >= 1 && currentStep <= 4) {
             initialThreadsContainer.classList.add('current-view');
             resultsContainer.classList.remove('visible');
         } else if (currentStep === 5) {
              initialThreadsContainer.classList.remove('current-view');
              resultsContainer.classList.add('visible');
         } else {
              initialThreadsContainer.classList.remove('current-view');
              resultsContainer.classList.remove('visible');
         }
    }

    function moveToNextStep() {
        if (currentStep < stepElements.length) {
            currentStep++;
            updateStepVisibility();
             // Scroll to controls/active step if needed? Or maybe just visually highlight
             stepElements[currentStep-1].scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

     function animateSegmentClick(segmentEl) {
         segmentEl.classList.remove('clicked'); // Reset animation
         void segmentEl.offsetWidth; // Trigger reflow
         segmentEl.classList.add('clicked'); // Add animation class
     }


    // --- Simulation Core Functions ---

    // Initialize the thread state and display initial threads
    function initializeThreads() {
        threadState = [];
        const initialThreadsDiv = document.getElementById('initial-threads');
        initialThreadsDiv.innerHTML = ''; // Clear previous content
        const dyedThreadsDiv = document.getElementById('dyed-threads');
        dyedThreadsDiv.innerHTML = '';
         const wovenPatternDiv = document.getElementById('woven-pattern');
        wovenPatternDiv.innerHTML = '';

        for (let i = 0; i < NUM_THREADS; i++) {
            threadState[i] = [];
            const threadDiv = document.createElement('div');
            threadDiv.classList.add('thread');

            for (let j = 0; j < NUM_SEGMENTS; j++) {
                const segmentDiv = document.createElement('div');
                segmentDiv.classList.add('segment');
                segmentDiv.dataset.threadIndex = i;
                segmentDiv.dataset.segmentIndex = j;
                segmentDiv.style.backgroundColor = '#f8f8f8'; // Initial color - off-white/light grey
                threadState[i][j] = { tied: false, color: '#f8f8f8' }; // Initial state
                segmentDiv.addEventListener('click', handleSegmentClick);
                threadDiv.appendChild(segmentDiv);
            }
            initialThreadsDiv.appendChild(threadDiv);
        }

         currentStep = 1; // Start at step 1
         updateStepVisibility();
         resultsContainer.classList.remove('visible'); // Hide results on reset
    }

    // Update the visual state of the initial threads display
    // Called after tying/untieing or dyeing in steps 1-4
    function updateInitialThreadsDisplay() {
        const segments = document.querySelectorAll('#initial-threads .segment');
        segments.forEach(segmentEl => {
            const i = parseInt(segmentEl.dataset.threadIndex);
            const j = parseInt(segmentEl.dataset.segmentIndex);
            const state = threadState[i][j];

            // Set color based on the current stored color state
             segmentEl.style.backgroundColor = state.color;

            // Toggle tied class
            if (state.tied && currentStep <= 3) { // Only show ties visually up to step 3
                 segmentEl.classList.add('tied');
            } else {
                 segmentEl.classList.remove('tied');
            }

            // Update cursor/interactivity based on current step
            segmentEl.style.cursor = 'default'; // Default to not interactive
            segmentEl.removeEventListener('click', handleSegmentClick); // Remove old listeners

             if (currentStep === 1 || currentStep === 3) { // Tying/Untieing steps
                 segmentEl.style.cursor = 'pointer';
                  segmentEl.addEventListener('click', handleSegmentClick);
             }
        });
    }

    // Handle clicks on segments for tying/untieing based on current step
    function handleSegmentClick(event) {
        if (currentStep !== 1 && currentStep !== 3) return; // Only interactive in tying/untieing steps

        const segmentEl = event.target;
        const i = parseInt(segmentEl.dataset.threadIndex);
        const j = parseInt(segmentEl.dataset.segmentIndex);

         // Toggle tied state
        threadState[i][j].tied = !threadState[i][j].tied;

         // Visual feedback & update display
         animateSegmentClick(segmentEl);
        updateInitialThreadsDisplay(); // Update classes/appearance
    }

     // Reset all ties - usable in step 1 and 3
    function resetTies() {
         if (currentStep !== 1 && currentStep !== 3) return; // Only allow reset in tying steps

        for (let i = 0; i < NUM_THREADS; i++) {
            for (let j = 0; j < NUM_SEGMENTS; j++) {
                threadState[i][j].tied = false;
            }
        }
        updateInitialThreadsDisplay();
         // Optional: small animation/message
         console.log('All ties removed.'); // Use console or a simple message area instead of alert
    }


    // Apply dye color to untied segments
    // `isSecondDye` flag helps decide if we're blending or just setting color
    function dyeThreads(color, isSecondDye = false) {
         if ((currentStep === 2 && !isSecondDye) || (currentStep === 4 && isSecondDye)) {
             const segmentsToDye = [];
             for (let i = 0; i < NUM_THREADS; i++) {
                 for (let j = 0; j < NUM_SEGMENTS; j++) {
                     if (!threadState[i][j].tied) {
                         segmentsToDye.push({ i, j });
                     }
                 }
             }

             if (segmentsToDye.length === 0) {
                 // Optional: message that nothing was dyed because all were tied
                 console.log('No segments were dyed as all were tied.');
                 // Still move to next step to allow user to continue
                  if (currentStep === 2 || currentStep === 4) {
                    // After dyeing (or attempting to dye), implicitly untie everything
                    // for the next potential tying step.
                    for (let i = 0; i < NUM_THREADS; i++) {
                         for (let j = 0; j < NUM_SEGMENTS; j++) {
                              threadState[i][j].tied = false;
                         }
                    }
                    updateInitialThreadsDisplay(); // Show threads without ties
                    moveToNextStep();
                 }
                 return; // Exit if nothing to dye
             }


             // Simple color setting animation
             let dyedCount = 0;
             const segmentElements = document.querySelectorAll('#initial-threads .segment');
             const animateDye = (index) => {
                if (index >= segmentsToDye.length) {
                     // Animation complete
                     if (currentStep === 2 || currentStep === 4) {
                         // After dyeing (or attempting to dye), implicitly untie everything
                         // for the next potential tying step.
                          for (let i = 0; i < NUM_THREADS; i++) {
                             for (let j = 0; j < NUM_SEGMENTS; j++) {
                                  threadState[i][j].tied = false;
                             }
                         }
                         updateInitialThreadsDisplay(); // Show threads without ties
                          moveToNextStep();
                      }
                    return;
                }

                const { i, j } = segmentsToDye[index];
                const segmentEl = segmentElements[i * NUM_SEGMENTS + j]; // Calculate index in flat list

                 // Determine final color - simple blend or override
                 let finalColor = color;
                 if (isSecondDye && threadState[i][j].color !== '#f8f8f8') {
                     // If second dye and segment already has color, try a simple blend simulation (requires color math)
                     // For simplicity here, let's just override or pick the darker color or layer?
                     // Simplest: New color replaces old if not tied. If tied, old color remains.
                     // If it's the second dye, and it was dyed in the first step (not initial color),
                     // we could simulate mixing or layering. Let's just override for clarity in a basic sim.
                     // If you wanted mixing, you'd need a color mixing function.
                     // For now, the last dye applied to an untied segment wins.
                      finalColor = color;
                 }

                 // Apply color and animate
                threadState[i][j].color = finalColor;
                segmentEl.style.backgroundColor = finalColor; // Apply color immediately for effect

                 // Minimal visual feedback during dye
                 segmentEl.classList.add('dyed-animated'); // Use a class for animation if needed (CSS transition works better)
                 // CSS transition handles the color change smoothly

                 // Process next segment after a small delay
                setTimeout(() => animateDye(index + 1), 10); // Small delay for animation effect
             };

             // Start the dyeing animation
             animateDye(0);

        } else {
             console.warn(`Dye action not available in Step ${currentStep}`);
        }
    }

    // Show the final results: dyed threads and woven pattern simulation
    function showResults() {
         if (currentStep !== 5) return; // Only available in step 5

        const dyedThreadsDiv = document.getElementById('dyed-threads');
        dyedThreadsDiv.innerHTML = ''; // Clear previous content

        // Display dyed threads preview
        for (let i = 0; i < NUM_THREADS; i++) {
             const threadDiv = document.createElement('div');
            threadDiv.classList.add('thread');
            for (let j = 0; j < NUM_SEGMENTS; j++) {
                 const segmentDiv = document.createElement('div');
                 segmentDiv.classList.add('segment');
                 segmentDiv.style.backgroundColor = threadState[i][j].color;
                 segmentDiv.classList.remove('tied'); // Ties are removed for weaving visual
                 segmentDiv.style.cursor = 'default'; // Not interactive
                 // Remove borders for final preview for smoother look
                 segmentDiv.style.border = 'none';
                 segmentDiv.style.marginBottom = '0'; // No gap
                 threadDiv.appendChild(segmentDiv);
             }
             dyedThreadsDiv.appendChild(threadDiv);
        }


        // Simulate weaving (simple warp ikat with white weft)
        const wovenPatternDiv = document.getElementById('woven-pattern');
        wovenPatternDiv.innerHTML = ''; // Clear previous content

        // Setup grid: NUM_THREADS columns, NUM_SEGMENTS * some multiplier rows (for density)
        const weavingDensity = 4; // How many weft passes per warp segment (higher = more square cells)
        const totalWeftRows = NUM_SEGMENTS * weavingDensity;

         wovenPatternDiv.style.gridTemplateColumns = `repeat(${NUM_THREADS}, 18px)`; // Match thread width
         wovenPatternDiv.style.gridTemplateRows = `repeat(${totalWeftRows}, ${18 / weavingDensity}px)`; // Rows height based on thread width for roughly square cells

         // Simple weaving simulation: grid cell color is determined by the warp thread color
         // The "blur" effect is handled by CSS filter. This just lays out the colored segments.
        for (let r = 0; r < totalWeftRows; r++) {
            for (let c = 0; c < NUM_THREADS; c++) {
                const cell = document.createElement('div');
                cell.classList.add('weave-cell');

                // Determine which segment of the warp thread 'c' this row 'r' corresponds to
                const segmentIndex = Math.floor(r / weavingDensity);
                // Ensure segmentIndex is within bounds in case of floating point issues
                 const finalSegmentIndex = Math.min(segmentIndex, NUM_SEGMENTS - 1);

                cell.style.backgroundColor = threadState[c][finalSegmentIndex].color; // Use the warp thread's color

                wovenPatternDiv.appendChild(cell);
            }
        }


         // Show results area with animation
        resultsContainer.classList.add('visible');
         // Scroll results into view
         resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Reset simulation
    function resetSimulation() {
        initializeThreads();
         // Optional: message or visual cue for reset
        console.log('Simulation reset!');
    }

    // Toggle explanation visibility
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
             explanationDiv.style.display = 'block';
             // Optional: Scroll to explanation
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
             explanationDiv.style.display = 'none';
        }

    });

    // --- Event Listeners for Step Buttons ---
    // Step 1 buttons are interactive by default because step 1 is active initially
    // Step 2: Dye button
    document.querySelector('#step-2 button').addEventListener('click', () => {
        if (currentStep === 2) {
            dyeThreads(document.getElementById('dye-color').value, false); // First dye
        }
    });
    // Step 3: Tie/Untie is handled by segment click directly when step 3 is active
     // Step 3: Reset Ties button
    document.querySelector('#step-3 button').addEventListener('click', () => {
         if (currentStep === 3) {
             resetTies(); // Reset ties in step 3
         }
    });
    // Step 4: Dye button
    document.querySelector('#step-4 button').addEventListener('click', () => {
        if (currentStep === 4) {
            dyeThreads(document.getElementById('dye-color-2').value, true); // Second dye
        }
    });
    // Step 5: Show Results button
    document.querySelector('#step-5 button:first-child').addEventListener('click', () => {
         if (currentStep === 5) {
             showResults();
         }
    });
     // Step 5: Reset Simulation button
    document.querySelector('#step-5 button:last-child').addEventListener('click', () => {
         if (currentStep === 5) {
             resetSimulation();
         }
    });

    // Final results area reset button
    document.querySelector('.final-buttons button').addEventListener('click', resetSimulation);


    // Initialize the app when the page loads
    document.addEventListener('DOMContentLoaded', () => {
        initializeThreads(); // Sets up step 1 as active
        updateInitialThreadsDisplay(); // Ensure initial appearance and click listeners for step 1
    });

</script>
---
```