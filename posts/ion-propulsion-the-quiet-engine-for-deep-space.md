---
title: "הנעה יונית: מסע שקט אל עומק החלל"
english_slug: ion-propulsion-the-quiet-engine-for-deep-space
category: "פיזיקה"
tags: ["הנעה יונית", "חלל", "פיזיקה", "מנועים", "טכנולוגיה"]
---
<div class="page-container">
    <h1>הנעה יונית: מסע שקט אל עומק החלל</h1>
    <p class="intro-text">מנועי טילים קונבנציונליים שואגים בעוצמה ושורפים טונות של דלק בשניות. אבל איך חלליות קטנות כמו הגשושית 'דון' מצליחות לטוס מיליארדי קילומטרים בחלל במשך שנים ארוכות עם מיכל דלק קטן להפתיע? הסוד טמון בטכנולוגיית הנעה שונה לחלוטין, שקטה ויעילה לאין שיעור למרחקים ארוכים.</p>

    <div id="app" class="interactive-app">
        <div class="engine-wrapper">
             <div class="component fuel-tank"><span>מכל דלק (קסנון)</span></div>
             <div class="engine-body">
                 <div class="component ionization-chamber"><span>תא יינון</span><div class="chamber-glow"></div></div>
                 <div class="grids-container">
                     <div class="component grid accel-grid"><span>סריג האצה (+)</span></div>
                     <div class="component grid decel-grid"><span>סריג האטה/האצה (-)</span></div>
                 </div>
                 <div class="component neutralizer"><span>נטרל אלקטרונים</span></div>
                 <div class="exhaust-area">
                     <!-- Particles will be added here by JS -->
                 </div>
             </div>
             <div class="thrust-indicator">
                 <div class="arrow-head"></div>
                 <div class="arrow-body"></div>
                 <span>דחף</span>
             </div>
        </div>

        <div class="controls-container">
            <h2>כוונו את מנוע היונים</h2>
            <div class="control-group">
                <label for="flow-rate">קצב הזרמת גז:</label>
                <input type="range" id="flow-rate" min="0.1" max="1" step="0.1" value="0.5">
                <span id="flow-rate-value">0.5</span> (זרימה יחסית)
            </div>
            <div class="control-group">
                <label for="voltage">מתח האצה:</label>
                <input type="range" id="voltage" min="1000" max="7000" step="250" value="3000">
                <span id="voltage-value">3000</span> V
            </div>

            <div class="display-group">
                <p>דחף נוכחי: <span id="thrust-display">0</span> µN</p>
                <p>יעילות דלק (Specific Impulse): <span id="isp-display">0</span> שניות</p>
            </div>
            <p class="hint-text">שנו את הערכים וצפו בהשפעה על זרימת החלקיקים וביצועי המנוע.</p>
        </div>
    </div>

    <button id="toggle-explanation">לגלות את הסוד: איך זה עובד?</button>

    <div id="explanation" style="display: none;">
        <h2>הסבר מעמיק על הנעה יונית</h2>
        <p><strong>מהי הנעה יונית ולמה היא שונה ממנועים רקטיים רגילים?</strong></p>
        <p>דמיינו שמנוע הטיל הרגיל הוא צינור כיבוי אש ענק שפולט המון מים במהירות סבירה. הנעה יונית, לעומת זאת, היא כמו אקדח שמתיז מעט מאוד טיפות (יונים) במהירות מדהימה. שתי השיטות מזיזות אתכם קדימה (חוק שימור התנע וחוק ניוטון השלישי), אבל המנוע היוני עושה זאת ביעילות דלק גבוהה בהרבה לאורך זמן.</p>

        <p><strong>עקרון הפעולה: פיזיקה בפעולה!</strong></p>
        <p>הבסיס הוא פשוט: דוחפים מסה (יונים) מהחללית בכיוון אחד, והחללית מקבלת "בעיטה" קטנה בכיוון ההפוך. ההבדל הוא במהירות הפליטה. מנועים יוניים מאיצים יונים באמצעות שדות חשמליים עוצמתיים למהירויות עצומות - עשרות קילומטרים בשנייה! מהירות הפליטה הגבוהה פירושה שאפשר להפיק המון "תנועה" (תנע) מכמות קטנה של חומר.</p>

        <p><strong>שלבי הפעולה במנוע היוני:</strong></p>
        <ol>
            <li><strong>הזרמת דלק (קסנון):</strong> גז הקסנון מוזרם ממכל האחסון לתוך תא היינון. קסנון הוא גז אציל, כבד יחסית ונוח לעבודה במנועים יוניים.</li>
            <li><strong>יינון:</strong> בתוך תא היינון, אטומי הקסנון "מופגזים" באלקטרונים. התנגשויות אלו מסירות אלקטרונים מהאטומים והופכות אותם ליונים חיוביים (אטומים עם מטען חשמלי חיובי).</li>
            <li><strong>האצה:</strong> היונים החיוביים נמשכים כעת אל מערכת של סריגים דקים עם אלפי חורים קטנים. בין הסריגים שורר שדה חשמלי חזק במיוחד, הנוצר על ידי הפרש מתח גבוה (אלפי וולטים). סריג אחד בעל מטען חיובי גבוה (סריג מסך) הודף את היונים, וסריג שני בעל מטען שלילי גבוה (סריג האצה) מושך אותם. יחד, הם מאיצים את היונים למהירות מדהימה כשהם עוברים דרך החורים.</li>
            <li><strong>נטרול:</strong> לאחר שהיונים המואצים עוזבים את המנוע ויוצרים קרן דחף, חשוב "לנטרל" אותם חשמלית על ידי הוספת אלקטרונים חופשיים (מ"נטרל" נפרד). למה? כדי למנוע הצטברות מטען חיובי על החללית, מה שיגרום ליונים הנפלטים להימשך בחזרה ולהרוס את האפקט.</li>
        </ol>

        <p><strong>למה זה טוב (יתרונות): יעילות שיא בדלק ויכולת פעולה מתמשכת.</strong></p>
        <p>היתרון הגדול ביותר הוא יעילות דלק מדהימה. נמדדת ב-Specific Impulse (ISP), מדד לכמה זמן מנוע יכול לייצר דחף נתון מקילוגרם אחד של דלק. מנועים יוניים מגיעים ל-ISP של אלפי ואף עשרות אלפים של שניות, פי עשרה ואף מאה ממנועים כימיים! זה אומר שמשימה יכולה לשאת הרבה פחות דלק כדי להשיג שינוי מהירות גדול לאורך זמן, חוסך משקל ענק בעלות השיגור.</p>

        <p><strong>היכן הקאץ' (חסרונות): דחף זעיר.</strong></p>
        <p>ההנעה היונית מייצרת דחף נמוך להחריד - בקושי דחף שיספיק להזיז פיסת נייר! בגלל זה, אי אפשר להשתמש בה לשיגור מהקרקע או לתמרונים מהירים במסלול קרוב לכדור הארץ. הדחף הזעיר מייצר תאוצה מינימלית, אבל מאחר שהמנוע פועל ברציפות שבועות, חודשים ואף שנים, התאוצה הקטנה מצטברת ובסופו של דבר מאפשרת להגיע למהירויות גבוהות מאוד ולשנות מסלולים ביעילות אנרגטית שאין שנייה לה.</p>

        <p><strong>יישומים בחלל:</strong></p>
        <p>הנעה יונית מושלמת למשימות שדורשות שינויי מהירות גדולים *לאורך זמן רב*, במיוחד בחלל העמוק הרחק מכוחות הכבידה הגדולים. משמשת להנעת גשושיות למרחקים עצומים (כוכבי לכת, אסטרואידים), לשמירה על מסלול מדויק של לוויינים לאורך שנים, ולמשימות הדורשות תמרונים עדינים.</p>

        <p><strong>משימות פורצות דרך:</strong></p>
        <p>גשושיות נאס"א Deep Space 1 (הראשונה לבחון את הטכנולוגיה) ו-Dawn (השתמשה במנועים היוניים למעלה מעשור לחקור את וסטה וצרס בחגורת האסטרואידים) הן דוגמאות קלאסיות. גם לווייני תקשורת רבים משתמשים במנועי יונים קטנים כדי "להישאר במקום" במסלול הגיאוסטציונרי.</p>
    </div>
</div>

<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: #e0f2f7; /* Light blueish background */
        color: #333;
        direction: rtl; /* Hebrew RTL */
        text-align: right; /* Align text to the right */
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    .page-container {
         max-width: 960px;
         margin: 0 auto;
         padding: 20px;
         background-color: #ffffff;
         border-radius: 12px;
         box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    }

    h1, h2 {
        color: #0277bd; /* Darker blue */
        text-align: center;
        margin-bottom: 20px;
        line-height: 1.3;
    }

    h1 {
        font-size: 2.2em;
        margin-top: 0;
    }

    h2 {
         font-size: 1.6em;
         border-bottom: 2px solid #e0f2f7;
         padding-bottom: 10px;
         margin-top: 30px;
    }

    .intro-text, .hint-text {
        text-align: center;
        font-size: 1.1em;
        color: #555;
        margin-bottom: 30px;
    }
     .hint-text {
         font-size: 0.95em;
         margin-top: 20px;
         color: #0277bd;
     }


    .interactive-app {
        background-color: #f1f8e9; /* Light greenish */
        padding: 30px;
        margin: 30px auto;
        border-radius: 10px;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.05);
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 850px;
        border: 1px solid #dcedc8;
    }

    .engine-wrapper {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px;
        position: relative;
        padding: 20px 0;
        box-sizing: border-box;
        /* background-color: #e8f5e9; */ /* Very light green for engine area */
        border-radius: 8px;
    }

    .component {
        border: 1px solid #a5d6a7; /* Light green border */
        padding: 10px 15px;
        text-align: center;
        border-radius: 6px;
        background-color: #c8e6c9; /* Light green background */
        white-space: nowrap;
        font-size: 0.9em;
        font-weight: bold;
        color: #333;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: center;
    }
     .component span {
         pointer-events: none; /* Allow clicks/hovers to pass through text to parent */
     }

    .fuel-tank {
        width: 120px;
        height: 70px;
        background: linear-gradient(to bottom, #bbdefb, #64b5f6); /* Blue gradient */
        border-color: #42a5f5;
        color: #fff;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        margin-left: 25px;
        position: relative; /* For potential future particle origin */
        overflow: hidden; /* Hide particles inside */
    }

    .engine-body {
        display: flex;
        align-items: center;
        flex-grow: 1;
        height: 90px; /* Consistent height */
        background-color: #e8f5e9; /* Very light green */
        position: relative;
        border: 1px solid #a5d6a7;
        border-radius: 6px;
        overflow: hidden; /* Hide particles outside */
        box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
    }

    .ionization-chamber {
        width: 150px;
        height: 100%;
        background: linear-gradient(to right, #fff9c4, #fff59d); /* Yellowish gradient */
        border-right: none;
        position: relative;
         overflow: hidden;
    }
    .chamber-glow {
         position: absolute;
         top: 10%;
         left: 10%;
         width: 80%;
         height: 80%;
         box-shadow: 0 0 15px 5px rgba(255, 235, 59, 0.6); /* Yellow glow */
         border-radius: 50%;
         opacity: 0.5;
         animation: pulse-glow 2s infinite alternate;
         pointer-events: none;
    }
     @keyframes pulse-glow {
         from { opacity: 0.4; }
         to { opacity: 0.7; }
     }


    .grids-container {
        display: flex;
        align-items: center;
        height: 100%;
        width: 60px; /* Width for both grids */
        border-left: none;
        border-right: none;
        position: relative;
        background-color: #f0f4c3; /* Pale yellow */
        overflow: hidden;
    }
    /* Simple visual representation of electric field lines */
     .grids-container::before, .grids-container::after {
         content: '';
         position: absolute;
         top: 0;
         bottom: 0;
         width: 1px;
         background-color: rgba(0, 0, 0, 0.1);
         z-index: 1; /* Below particles */
     }
    .grids-container::before { left: 15px; } /* Line near accel grid */
    .grids-container::after { right: 15px; } /* Line near decel grid */


    .grid {
        width: 30px; /* Individual grid width */
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: #fff;
        text-shadow: 0 1px 1px rgba(0,0,0,0.3);
        border: none; /* Remove component border style */
        border-radius: 0; /* Remove component border-radius */
        padding: 0; /* Remove component padding */
         box-shadow: none; /* Remove component box-shadow */
    }

    .accel-grid {
        background-color: #ef5350; /* Red for positive */
    }

    .decel-grid {
        background-color: #42a5f5; /* Blue for negative */
    }

    .neutralizer {
        width: 100px;
        height: 100%;
        background: linear-gradient(to left, #e1bee7, #ce93d8); /* Purplish gradient */
        border-left: none;
         overflow: hidden;
    }

    .exhaust-area {
         flex-grow: 1;
         height: 100%;
         position: relative;
         background-color: #e0f2f7; /* Match body background slightly */
         overflow: hidden;
         border-radius: 0 6px 6px 0; /* Round only the end */
    }


    .particle {
        position: absolute;
        border-radius: 50%;
        top: 50%; /* Vertical alignment is approximate */
        transform: translate(-50%, -50%); /* Center the div */
        will-change: transform, left; /* Optimize animation */
         z-index: 10; /* Above other elements in engine body */
    }

    .particle.atom {
        width: 8px;
        height: 8px;
        background-color: #4dd0e1; /* Cyan blue for neutral atom */
         box-shadow: 0 0 4px rgba(77, 208, 225, 0.5);
    }

    .particle.ion {
        width: 10px; /* Slightly larger */
        height: 10px;
        background-color: #ffb74d; /* Orange for positive ion */
        border: 1px solid #ffa726;
        box-shadow: 0 0 6px rgba(255, 183, 77, 0.7);
    }

    .particle.neutral {
         width: 8px; /* Back to normal size */
         height: 8px;
         background-color: #90a4ae; /* Greyish for neutral particle */
         box-shadow: 0 0 5px rgba(144, 164, 174, 0.6);
    }

     /* Visual trail effect for fast particles */
     .particle.ion::after, .particle.neutral::after {
         content: '';
         position: absolute;
         top: 50%;
         right: 0; /* Starts at the particle's right edge */
         width: 20px; /* Length of the trail */
         height: 2px; /* Thickness of the trail */
         background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.5));
         transform: translateY(-50%);
         z-index: -1; /* Behind the particle circle */
         opacity: 0.8;
     }
     .particle.neutral::after {
         background: linear-gradient(to right, rgba(144,164,174,0), rgba(144,164,174,0.5));
     }


     .thrust-indicator {
         position: absolute;
         top: 50%;
         right: -20px; /* Positioned to the right of the engine body */
         transform: translateY(-50%);
         display: flex;
         align-items: center;
         pointer-events: none; /* Don't interfere with clicks */
         opacity: 0; /* Initially hidden, shown by JS based on thrust */
         transition: opacity 0.3s ease;
         min-width: 80px; /* Ensure space for text */
     }

     .thrust-indicator span {
         font-size: 0.9em;
         font-weight: bold;
         color: #0277bd;
         margin-right: 5px;
     }

     .thrust-indicator .arrow-body {
         width: 30px; /* Base width, will be scaled */
         height: 4px;
         background-color: #0277bd;
     }
      .thrust-indicator .arrow-head {
          width: 0;
          height: 0;
          border-top: 8px solid transparent;
          border-bottom: 8px solid transparent;
          border-left: 12px solid #0277bd;
      }


    .controls-container {
        width: 100%;
        max-width: 500px;
        margin-top: 30px;
        background-color: #e3f2fd; /* Lightest blue */
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #bbdefb;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .control-group {
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
    }

    .control-group label {
        flex: 0 0 150px; /* Wider fixed width for label */
        margin-left: 10px;
        font-weight: bold;
        color: #01579b; /* Darker blue */
    }

    .control-group input[type="range"] {
        flex-grow: 1;
        margin: 0 10px;
         -webkit-appearance: none; /* Override default styles */
         appearance: none;
         height: 8px;
         background: #bbdefb; /* Light blue track */
         outline: none;
         opacity: 0.8;
         transition: opacity .2s;
         border-radius: 5px;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: #0277bd; /* Dark blue thumb */
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .control-group input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #0277bd;
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }


    .control-group span {
        flex: 0 0 80px; /* Wider fixed width for value display and unit */
        text-align: left;
        color: #01579b;
        font-weight: bold;
    }


    .display-group {
        margin-top: 25px;
        padding-top: 20px;
        border-top: 1px dashed #bbdefb; /* Dashed border */
        color: #01579b;
    }

    .display-group p {
        margin: 10px 0;
        font-size: 1.2em;
        display: flex;
        justify-content: space-between;
    }
     .display-group span {
         font-weight: bold;
     }

    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #4caf50; /* Green */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    #toggle-explanation:hover {
        background-color: #388e3c; /* Darker green */
    }
     #toggle-explanation:active {
         transform: scale(0.98);
     }


    #explanation {
        background-color: #e8f5e9; /* Lightest green, matches engine area */
        padding: 25px;
        margin: 20px auto;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        max-width: 900px;
        border: 1px solid #dcedc8;
    }

    #explanation h2 {
        text-align: right;
        color: #33691e; /* Dark green */
        border-bottom-color: #aed581;
    }

    #explanation p {
        margin-bottom: 18px;
        text-align: justify;
        color: #444;
    }
     #explanation strong {
         color: #33691e;
     }

    #explanation ul, #explanation ol {
        margin-right: 25px;
        margin-bottom: 18px;
        padding-right: 0; /* Remove default padding */
    }

    #explanation li {
        margin-bottom: 10px;
        text-align: justify;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .page-container {
            padding: 15px;
        }
        h1 { font-size: 1.8em; }
        h2 { font-size: 1.4em; }
        .interactive-app { padding: 20px; }
        .engine-wrapper { flex-direction: column; align-items: stretch;}
        .fuel-tank { margin: 0 auto 20px auto; width: 100px; height: 50px;}
        .engine-body { width: 100%; height: 70px;}
        .ionization-chamber { width: 100px; }
        .grids-container { width: 40px; }
        .grid { width: 20px;}
        .neutralizer { width: 80px; }
         .thrust-indicator {
             position: static; /* Stack below engine */
             transform: none;
             justify-content: center;
             margin-top: 20px;
             opacity: 1 !important; /* Always show on small screens if space is tight */
             flex-direction: row-reverse; /* Arrow points left */
             min-width: auto;
         }
          .thrust-indicator span { margin-left: 5px; margin-right: 0;}
         .thrust-indicator .arrow-head { border-left: none; border-right: 12px solid #0277bd;}
          .thrust-indicator .arrow-body { background-color: #0277bd;}

        .controls-container { padding: 15px; }
        .control-group { flex-direction: column; align-items: flex-end;}
        .control-group label { flex: none; margin-left: 0; margin-bottom: 5px; width: 100%; text-align: right;}
        .control-group input[type="range"] { margin: 0; width: 100%;}
        .control-group span { flex: none; width: 100%; text-align: right; margin-top: 5px;}
        .display-group p { flex-direction: column; align-items: flex-end;}
         .display-group span { margin-top: 5px;}

        #toggle-explanation { font-size: 1em; padding: 10px 20px;}
    }

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const app = document.getElementById('app');
    const flowRateInput = document.getElementById('flow-rate');
    const voltageInput = document.getElementById('voltage');
    const flowRateValueSpan = document.getElementById('flow-rate-value');
    const voltageValueSpan = document.getElementById('voltage-value');
    const thrustDisplay = document.getElementById('thrust-display');
    const ispDisplay = document.getElementById('isp-display');
    const engineBody = app.querySelector('.engine-body');
    const thrustIndicator = app.querySelector('.thrust-indicator');
     const thrustArrowBody = thrustIndicator.querySelector('.arrow-body');


    const ionizationChamber = engineBody.querySelector('.ionization-chamber');
    const accelGrid = engineBody.querySelector('.accel-grid');
    const decelGrid = engineBody.querySelector('.decel-grid');
    const neutralizer = engineBody.querySelector('.neutralizer');


    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Physics Constants (simplified for simulation)
    const AMU = 1.66054e-27; // Atomic Mass Unit in kg
    const ELEMENTARY_CHARGE = 1.60218e-19; // Elementary charge in C
    const XENON_MASS_KG = 131.29 * AMU; // Approx mass of Xenon ion (amu)
    const G0 = 9.80665; // Standard gravity in m/s^2

    // Simulation parameters (linked to controls)
    let currentFlowRate = parseFloat(flowRateInput.value); // relative units (0.1 to 1)
    let currentVoltage = parseInt(voltageInput.value); // Volts (1000 to 7000)

    // Particle management for JS animation
    const particlesJS = [];
    const maxParticles = 80; // Increased limit for denser exhaust
    const baseParticleInterval_ms = 150; // Time in ms between new particles at base flow rate (flowRate = 1)
    let particleGenerationRate_particles_per_sec = (1000 / baseParticleInterval_ms) * currentFlowRate;

    // Define pixel boundaries for component zones relative to engineBody left
    let zoneBoundaries = {};

    function updateZoneBoundaries() {
        const engineBodyRect = engineBody.getBoundingClientRect();
        const appRect = app.getBoundingClientRect(); // Use app for consistent offset reference if engineBody moves relative to app

        // Positions relative to engineBody's *left edge*
        const engineBodyLeftPx = engineBodyRect.left - appRect.left;

        const fuelTankWidth = app.querySelector('.fuel-tank').offsetWidth;
        const fuelTankRight_app = app.querySelector('.fuel-tank').getBoundingClientRect().right - appRect.left;

        const ionizationChamberRect = ionizationChamber.getBoundingClientRect();
        const accelGridRect = accelGrid.getBoundingClientRect();
        const decelGridRect = decelGrid.getBoundingClientRect();
        const neutralizerRect = neutralizer.getBoundingClientRect();
        const exhaustAreaRect = app.querySelector('.exhaust-area').getBoundingClientRect();


         zoneBoundaries = {
            // Atom starts near tank end, moves into chamber
             tankEnd: fuelTankRight_app, // Use tank end as particle origin reference point (approx)
            // Note: Particles are parented to engineBody, so their left/x is relative to engineBody's left edge
            // We need to convert global/app-relative positions to engineBody-relative positions

            chamberStart_engineBody: ionizationChamberRect.left - engineBodyRect.left,
            chamberEnd_engineBody: ionizationChamberRect.right - engineBodyRect.left,
            accelGridStart_engineBody: accelGridRect.left - engineBodyRect.left,
            decelGridEnd_engineBody: decelGridRect.right - engineBodyRect.left,
            neutralizerEnd_engineBody: neutralizerRect.right - engineBodyRect.left,
            engineBodyEnd_engineBody: engineBody.offsetWidth // End of the visual engine body
         };

         // Approx length of the acceleration region (between grids) in meters for physics scaling
         // Let's assume the two grid components and the gap between them represent the main acceleration distance
         // Roughly the width of gridsContainer element
         const gridsContainer = engineBody.querySelector('.grids-container');
         const accelDistance_px = gridsContainer.offsetWidth; // Pixels
         const assumedEngineLengthM = 0.5; // Assume the visual engine body represents approx 0.5 meters
         const pixelsPerMeterScale = engineBody.offsetWidth / assumedEngineLengthM; // Pixels per meter

         zoneBoundaries.accelDistance_m = accelDistance_px / pixelsPerMeterScale; // Acceleration distance in meters
         zoneBoundaries.pixelsPerMeterScale = pixelsPerMeterScale;

          //console.log("Zone Boundaries (engineBody relative):", zoneBoundaries);
          //console.log("Accel Distance (m):", zoneBoundaries.accelDistance_m);
          //console.log("Pixels/Meter:", zoneBoundaries.pixelsPerMeterScale);
    }


    function updateValues() {
        currentFlowRate = parseFloat(flowRateInput.value);
        currentVoltage = parseInt(voltageInput.value);

        flowRateValueSpan.textContent = currentFlowRate.toFixed(1);
        voltageValueSpan.textContent = currentVoltage;

        // Update particle generation rate based on flow rate
        particleGenerationRate_particles_per_sec = (1000 / baseParticleInterval_ms) * currentFlowRate;

        calculatePerformance();
        updateThrustIndicator(parseFloat(thrustDisplay.textContent));
    }

    function calculatePerformance() {
        // Simple model: Assume final ion speed determined by voltage across accelDistance_m
        // v_ion^2 = v_initial^2 + 2 * a * d
        // a = Q*V / (m*d_accel)
        // v_ion = sqrt(v_initial^2 + 2 * Q * V / m)
        // Assume v_initial from chamber is small, approximate final v_ion by sqrt(2*Q*V/m)

        const ionVelocity_mps = Math.sqrt(2 * ELEMENTARY_CHARGE * currentVoltage / XENON_MASS_KG); // m/s

        // Thrust F = mass_flow_rate * exhaust_velocity
        // mass_flow_rate = particles_per_second * mass_per_particle
        const massFlowRate_kgs = (particleGenerationRate_particles_per_sec / 1000) * XENON_MASS_KG; // kg/sec (rate is per ms in generator logic, so divide by 1000)

        const thrust_N = massFlowRate_kgs * ionVelocity_mps; // Thrust in Newtons
        const thrust_uN = thrust_N * 1e6; // Thrust in microNewtons

        // Specific Impulse ISP = v_e / g0
        const isp_s = ionVelocity_mps / G0; // ISP in seconds

        thrustDisplay.textContent = thrust_uN.toFixed(2);
        ispDisplay.textContent = isp_s.toFixed(0); // ISP is usually displayed as an integer
    }

    function updateThrustIndicator(thrust_uN) {
        // Map thrust value to indicator opacity and perhaps width/scale
        const maxThrust = calculatePerformance(voltageInput.max, flowRateInput.max).thrust_uN; // Calculate max possible thrust
        const minThrust = calculatePerformance(voltageInput.min, flowRateInput.min).thrust_uN; // Calculate min possible thrust
        const opacity = Math.max(0.3, (thrust_uN - minThrust) / (maxThrust - minThrust)); // Scale opacity, minimum opacity even at low thrust
        thrustIndicator.style.opacity = opacity;

        // Optional: Scale arrow body length based on thrust
        const minArrowWidth = 15; // Base width in px
        const maxArrowWidth = 45; // Max width in px
        const arrowWidth = minArrowWidth + (maxArrowWidth - minArrowWidth) * ((thrust_uN - minThrust) / (maxThrust - minThrust));
         // Apply width change carefully, potentially messing up flex layout. Let's just use opacity and position for simplicity within constraints.
         // Or, just use width for a simple visual cue. Let's scale the arrow body width.
         thrustArrowBody.style.width = `${arrowWidth}px`;
    }

    let timeSinceLastParticle = 0; // Time accumulator for particle generation
    const particleStartYOffset = 15; // Pixels offset from center for vertical distribution

    function createParticleJS(currentTime_ms) {
        if (particlesJS.length >= maxParticles) {
            return;
        }

        const particleElement = document.createElement('div');
        particleElement.classList.add('particle', 'atom');

        // Initial position: Slightly random Y within the chamber height
        const initialX_engineBody = zoneBoundaries.chamberStart_engineBody + ionizationChamber.offsetWidth * 0.1; // Start inside chamber
        const initialY_engineBody = engineBody.offsetHeight / 2 + (Math.random() - 0.5) * particleStartYOffset; // Vertical center +/- offset


        // Set initial position using 'left' and 'top' property relative to engineBody
        particleElement.style.left = `${initialX_engineBody}px`;
        particleElement.style.top = `${initialY_engineBody}px`;
        // transform: translate(-50%, -50%) is already in CSS to center the div


        engineBody.appendChild(particleElement);

        particlesJS.push({
            element: particleElement,
            state: 'atom', // atom, ion, neutral
            x_px: initialX_engineBody, // Current X position (pixels relative to engineBody left)
            y_px: initialY_engineBody, // Current Y position (pixels relative to engineBody top)
            velocity_px_per_sec: 70, // Initial slow speed (pixels/sec) for atom state
            velocity_mps: 70 / zoneBoundaries.pixelsPerMeterScale, // velocity in meters/sec
            creationTime: currentTime_ms
        });
    }

     // Calculate final ion velocity in px/sec based on current voltage
     function getIonVelocity_px_per_sec() {
         const ionVelocity_mps = Math.sqrt(2 * ELEMENTARY_CHARGE * currentVoltage / XENON_MASS_KG); // m/s
         return ionVelocity_mps * zoneBoundaries.pixelsPerMeterScale; // px/sec
     }


    function updateParticlePositionJS(particle, deltaTime_sec) {

        let stateChanged = false;

        // State machine for particle behavior
        switch (particle.state) {
            case 'atom':
                // Move at slow, constant speed
                particle.x_px += particle.velocity_px_per_sec * deltaTime_sec;

                // Transition to ion state near end of chamber
                if (particle.x_px >= zoneBoundaries.chamberEnd_engineBody - 10) { // Transition just before leaving chamber
                    particle.state = 'ion'; // or 'ion_accelerating' if simulating acceleration
                    particle.element.classList.remove('atom');
                    particle.element.classList.add('ion');
                     // Assume acceleration is 'instantaneous' for visual simplicity, happens when entering grid area
                     // Velocity is updated when state becomes 'ion' (or when it enters grid area)
                     particle.velocity_px_per_sec = getIonVelocity_px_per_sec(); // Update to high ion speed
                     particle.velocity_mps = particle.velocity_px_per_sec / zoneBoundaries.pixelsPerMeterScale;
                    stateChanged = true;
                }
                break;

            case 'ion': // This state covers movement through grids and coasting until neutralizer
                // Move at high ion speed
                 particle.x_px += particle.velocity_px_per_sec * deltaTime_sec;

                // Transition to neutral state after neutralizer
                if (particle.x_px >= zoneBoundaries.neutralizerEnd_engineBody) {
                     particle.state = 'neutral';
                     particle.element.classList.remove('ion');
                     particle.element.classList.add('neutral');
                     // Velocity remains high
                     stateChanged = true;
                }
                break;

            case 'neutral':
                // Move at high neutral speed (same as final ion speed)
                particle.x_px += particle.velocity_px_per_sec * deltaTime_sec;
                // No further state transitions
                break;
        }

        // Apply new position to element (only X changes based on velocity)
        particle.element.style.left = `${particle.x_px}px`;
        // particle.element.style.top = `${particle.y_px}px`; // Y doesn't change dynamically in this sim

        // Remove particle if it's beyond the engine body end + buffer
        if (particle.x_px > zoneBoundaries.engineBodyEnd_engineBody + 50) { // Add a buffer for particles to leave visually
            particle.element.remove();
            return true; // Indicate removal
        }

        return false; // Not removed
    }


    let lastAnimationTimeJS = performance.now();

    function animateSimulationJS(currentTime) {
        const deltaTime_ms = currentTime - lastAnimationTimeJS;
        lastAnimationTimeJS = currentTime;
        const deltaTime_sec = deltaTime_ms / 1000;

        // Update zone boundaries if necessary (e.g., window resize could change element positions)
        // For simplicity in this static layout, we might only need to call this once or on window resize
        // updateZoneBoundaries(); // Calling every frame is safe but potentially overkill

        // Accumulate time for particle generation
        timeSinceLastParticle += deltaTime_ms;
        const particleCreationInterval_ms = 1000 / particleGenerationRate_particles_per_sec; // time needed per particle

        // Create particles based on accumulated time and rate, respecting max limit
        while (timeSinceLastParticle >= particleCreationInterval_ms && particlesJS.length < maxParticles) {
             createParticleJS(currentTime);
             timeSinceLastParticle -= particleCreationInterval_ms; // Deduct the interval for one particle
             // Ensure we don't create too many if interval is tiny
             if (particleCreationInterval_ms < 16) timeSinceLastParticle = 0; // Prevent explosion at very high rates
        }


        // Update and filter particles
        for (let i = particlesJS.length - 1; i >= 0; i--) {
            const particle = particlesJS[i];
            const removed = updateParticlePositionJS(particle, deltaTime_sec);
            if (removed) {
                particlesJS.splice(i, 1);
            }
        }

        requestAnimationFrame(animateSimulationJS);
    }

    // Initial setup
    updateZoneBoundaries(); // Calculate boundaries once initially
    updateValues(); // Calculate initial performance and set displays
    lastAnimationTimeJS = performance.now(); // Initialize timer
    animateSimulationJS(performance.now()); // Start the animation loop

    // Event listeners for controls
    flowRateInput.addEventListener('input', updateValues);
    voltageInput.addEventListener('input', updateValues);

     // Update boundaries if window is resized (might affect element positions)
     window.addEventListener('resize', updateZoneBoundaries);
      // Recalculate performance and update thrust indicator on resize too
     window.addEventListener('resize', updateValues);


    // Toggle Explanation
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'לגלות את הסוד: איך זה עובד?';
         // Scroll to explanation if showing it
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Calculate initial thrust to set indicator visibility
    const initialThrust = calculatePerformance(flowRateInput.value, voltageInput.value).thrust_uN;
    updateThrustIndicator(initialThrust);


     // Helper function to calculate performance for min/max for thrust indicator scaling
     function calculatePerformance(flowRate, voltage) {
         const flow = parseFloat(flowRate);
         const volt = parseInt(voltage);
         const approxParticlesPerSecond = (1000 / baseParticleInterval_ms) * flow;
         const approxMassFlowRate_kgs = (approxParticlesPerSecond / 1000) * XENON_MASS_KG;
         const ionVelocity_mps = Math.sqrt(2 * ELEMENTARY_CHARGE * volt / XENON_MASS_KG);
         const thrust_N = approxMassFlowRate_kgs * ionVelocity_mps;
         const thrust_uN = thrust_N * 1e6;
         const isp_s = ionVelocity_mps / G0;
         return { thrust_uN, isp_s };
     }


});

</script>
---
```