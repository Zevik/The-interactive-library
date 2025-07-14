---
title: "כשמחשבים חושבים כמו מוח: מבט על חישוב נוירומורפי"
english_slug: when-computers-think-like-brains-neuromorphic-computing
category: "מדעי המחשב"
tags:
  - חישוב נוירומורפי
  - בינה מלאכותית
  - ארכיטקטורת מחשב
  - רשתות נוירונים
  - נוירו-מדע
---
# כשמחשבים חושבים כמו מוח: מבט על חישוב נוירומורפי

תארו לעצמכם מחשב שלא רק מבצע הוראות במהירות בזק, אלא מסוגל באמת ללמוד, להסתגל ולזהות תבניות בצורה אינטואיטיבית, ממש כמו המוח האנושי. מחשבים קלאסיים בנויים לעולם החישובים המדויקים, אך דרך העיבוד שלהם שונה בתכלית מזו של המוח שלנו. בואו נצלול לתוך עולם החישוב הנוירומורפי – טכנולוגיה פורצת דרך שמנסה לגשר על הפער ולהעניק למחשבים "ניצוץ" מוחי.

<div class="neuromorphic-app-container">
    <h2>סימולציה פשטנית: איך רשת נוירומורפית "חושבת"</h2>
    <div class="simulation-area">
        <!-- SVG layer for connections -->
        <svg class="connections-layer"></svg>

        <div class="input-area">
            <h3>קלט (חיישנים)</h3>
            <button class="node input-node" data-input-id="0">עורר קלט 1 <br>(חיישן ראייה)</button>
            <button class="node input-node" data-input-id="1">עורר קלט 2 <br>(חיישן שמיעה)</button>
            <button class="node input-node" data-input-id="2">עורר קלט 3 <br>(חיישן מגע)</button>
        </div>
        <div class="neuron-layer-area">
            <h3>שכבת עיבוד <br>(נוירונים פולסניים)</h3>
            <div class="neuron-layer" id="hidden-layer">
                <div class="node neuron" data-neuron-id="0"><span class="node-label">נוירון 1</span><span class="current-sum">0</span></div>
                <div class="node neuron" data-neuron-id="1"><span class="node-label">נוירון 2</span><span class="current-sum">0</span></div>
                <div class="node neuron" data-neuron-id="2"><span class="node-label">נוירון 3</span><span class="current-sum">0</span></div>
            </div>
        </div>
        <div class="output-area">
            <h3>פלט <br>(פעולה/תגובה)</h3>
            <div class="node output-node" id="output-node"> ממתין לקלט...</div>
        </div>
    </div>

    <div class="controls-area">
        <h3>הגדרות הרשת (מודל למידה פשטני)</h3>
        <div class="control-group">
            <label for="threshold-neuron1">סף "ירי" נוירון 1:</label>
            <input type="range" id="threshold-neuron1" min="0.1" max="3" step="0.1" value="1.5">
            <span id="threshold-neuron1-value" class="control-value">1.5</span>
        </div>
        <div class="control-group">
             <label for="weight-input0-to-neuron0">חוזק קשר (משקל) קלט 1 לנוירון 1:</label>
             <input type="range" id="weight-input0-to-neuron0" min="0" max="2" step="0.1" value="1">
             <span id="weight-input0-to-neuron0-value" class="control-value">1.0</span>
         </div>
         <div class="control-group">
              <label for="weight-neuron1-to-output">חוזק קשר (משקל) נוירון 2 לפלט:</label>
              <input type="range" id="weight-neuron1-to-output" min="0" max="2" step="0.1" value="1">
              <span id="weight-neuron1-to-output-value" class="control-value">1.0</span>
          </div>
    </div>
     <div class="explanation-prompt">
         **איך לשחק:** לחצו על אחד מלחצני הקלט (חיישנים) כדי לשלוח "פולס" לרשת. צפו איך הפולס עובר דרך הנוירונים. נוירון "יורה" פולס משלו אם סך הקלט שקיבל (מושפע מ"חוזק הקשר") עולה על ה"סף" שלו. נסו לשנות את ההגדרות (סף וחוזק קשר) ולחצו שוב על הקלטים לראות איך ההתנהגות משתנה!
     </div>
</div>

<style>
    .neuromorphic-app-container {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        margin: 20px auto;
        padding: 30px;
        border: none; /* Remove outer border */
        border-radius: 12px;
        max-width: 950px;
        background: linear-gradient(to bottom right, #e0f7fa, #e1bee7); /* Soft gradient background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        position: relative; /* Needed for absolute positioning of SVG */
        overflow: hidden; /* Keep everything inside the container */
    }

    h2 {
        text-align: center;
        color: #4a148c; /* Deep purple */
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 1.8em;
        font-weight: bold;
    }

    h3 {
        margin-top: 0;
        color: #6a1b9a; /* Medium purple */
        border-bottom: 2px solid #e1bee7; /* Lighter purple */
        padding-bottom: 8px;
        margin-bottom: 15px;
        font-size: 1.2em;
        text-align: center; /* Center header */
    }

    .simulation-area {
        display: flex;
        justify-content: space-around;
        align-items: flex-start;
        gap: 30px; /* Increased gap */
        margin-bottom: 30px;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        position: relative; /* Needed for SVG overlay */
        padding: 20px 0; /* Add some vertical padding */
    }

    .connections-layer {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none; /* Allow clicks to pass through to nodes */
         z-index: 1; /* Draw below the nodes */
    }

    .connection-path {
         stroke: rgba(128, 0, 128, 0.5); /* Purple with some transparency */
         stroke-width: 3;
         fill: none;
         transition: stroke 0.3s ease, stroke-width 0.3s ease;
         /* Animation properties added by JS */
    }

    .connection-path.active {
         stroke: #ffb300; /* Amber */
         stroke-width: 5;
         animation: pulse-signal 0.8s ease-out forwards;
         /* For path animation */
          stroke-dasharray: 1000; /* Arbitrary large value */
          stroke-dashoffset: 1000;
          animation: dash 1s linear forwards;
           stroke-linecap: round;
    }

    @keyframes pulse-signal {
         0% { stroke-width: 3; stroke: rgba(128, 0, 128, 0.5); }
         50% { stroke-width: 6; stroke: #ffb300; }
         100% { stroke-width: 3; stroke: rgba(128, 0, 128, 0.5); }
    }

    @keyframes dash {
        from {
            stroke-dashoffset: 1000;
        }
        to {
            stroke-dashoffset: 0;
        }
    }


    .input-area, .neuron-layer-area, .output-area {
        flex: 1;
        padding: 20px;
        border: 1px solid #d1c4e9; /* Light purple border */
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent white */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        min-width: 180px; /* Ensure areas don't get too small */
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative; /* Needed for node positioning */
        z-index: 2; /* Ensure nodes are above SVG */
    }

     .neuron-layer-area {
         justify-content: center; /* Center neurons vertically if space allows */
     }

    .node {
        margin: 12px 0; /* Adjusted margin */
        padding: 12px 20px; /* Adjusted padding */
        border: 1px solid;
        border-radius: 25px; /* More rounded */
        text-align: center;
        transition: all 0.3s ease; /* Smoother transitions */
        user-select: none;
        position: relative; /* For positioning sum text */
        font-weight: bold;
        font-size: 1em;
        display: flex; /* For centering label and sum */
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

     .node-label {
         display: block;
     }

     .current-sum {
         display: block;
         font-size: 0.7em;
         color: #555;
         margin-top: 3px;
         opacity: 0; /* Hidden by default */
         transition: opacity 0.3s ease;
     }

     .node.show-sum .current-sum {
         opacity: 1; /* Shown when active/processing */
     }


    .input-node {
        border-color: #4fc3f7; /* Light blue */
        background-color: #e1f5fe; /* Very light blue */
        cursor: pointer;
    }

    .input-node:hover {
        background-color: #b3e5fc; /* Lighter blue */
        transform: translateY(-2px); /* Subtle lift on hover */
    }

    .input-node:active {
         transform: scale(0.95); /* Press effect */
         background-color: #81d4fa; /* Even lighter blue */
    }

     .input-node.activated {
         animation: input-activate 0.5s ease-out;
          border-color: #03a9f4; /* Blue */
          background-color: #4fc3f7; /* Light blue */
     }

    @keyframes input-activate {
         0% { transform: scale(1); background-color: #e1f5fe; }
         50% { transform: scale(1.05); background-color: #4fc3f7; }
         100% { transform: scale(1); background-color: #e1f5fe; }
    }


    .neuron {
         border-color: #81c784; /* Light green */
         background-color: #e8f5e9; /* Very light green */
         cursor: default;
    }

    .neuron.firing {
        background-color: #fff9c4; /* Light yellow */
        border-color: #ffeb3b; /* Yellow */
        box-shadow: 0 0 12px #ffeb3b; /* Glow effect */
        transform: scale(1.1); /* Expand slightly */
        animation: neuron-fire 0.8s ease-out forwards;
    }

     @keyframes neuron-fire {
         0% { transform: scale(1); background-color: #e8f5e9; box-shadow: none; }
         50% { transform: scale(1.1); background-color: #fff9c4; box-shadow: 0 0 12px #ffeb3b; }
         100% { transform: scale(1); background-color: #e8f5e9; box-shadow: none; }
     }


    .output-node {
        border-color: #ef9a9a; /* Light red */
        background-color: #ffebee; /* Very light red */
        min-height: 50px; /* Give it more size */
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.1em;
        color: #c62828; /* Dark red */
    }

     .output-node.active {
         background-color: #ffcdd2; /* Lighter red */
         border-color: #e53935; /* Red */
         box-shadow: 0 0 15px #e53935; /* Stronger glow */
         animation: output-active 1s ease-out forwards;
         color: #b71c1c; /* Even darker red */
     }

     @keyframes output-active {
         0% { transform: scale(1); background-color: #ffebee; box-shadow: none; }
         50% { transform: scale(1.05); background-color: #ffcdd2; box-shadow: 0 0 15px #e53935; }
         100% { transform: scale(1); background-color: #ffebee; box-shadow: none; }
     }


    .controls-area {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #d1c4e9; /* Light purple border */
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent white */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    .control-group {
        margin-bottom: 20px; /* Increased margin */
        display: flex;
        align-items: center;
        gap: 15px; /* Increased gap */
        flex-wrap: wrap;
    }

    .control-group label {
        flex-basis: 220px; /* Give labels more width */
        text-align: right; /* Labels aligned right */
        font-weight: bold;
        color: #4a148c; /* Deep purple */
    }

     .control-group input[type="range"] {
         flex-grow: 1;
         min-width: 120px; /* Prevent it from becoming too narrow */
         -webkit-appearance: none;
         appearance: none;
         height: 8px;
         background: #d1c4e9; /* Light purple track */
         outline: none;
         opacity: 0.7;
         transition: opacity .2s;
         border-radius: 4px;
     }

     .control-group input[type="range"]:hover {
         opacity: 1;
     }

     .control-group input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: #6a1b9a; /* Medium purple thumb */
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }

     .control-group input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #6a1b9a; /* Medium purple thumb */
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }

     .control-value {
         display: inline-block;
         min-width: 30px;
         text-align: center;
         font-weight: bold;
         color: #4a148c;
     }


    .explanation-prompt {
        margin-top: 30px;
        padding: 15px;
        background-color: #fff9c4; /* Light yellow */
        border: 1px solid #ffeb3b; /* Yellow */
        border-radius: 8px;
        text-align: center;
        font-size: 1em; /* Slightly larger */
        color: #333;
        line-height: 1.5;
    }


    #show-explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Rounded button */
        background-color: #6a1b9a; /* Medium purple */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    #show-explanation-button:hover {
        background-color: #4a148c; /* Darker purple */
        transform: translateY(-2px);
    }

    #show-explanation-button:active {
         transform: scale(0.98);
    }


    #explanation {
        margin-top: 20px;
        padding: 25px; /* Increased padding */
        border: none;
        border-radius: 12px;
        background-color: rgba(255, 255, 255, 0.95); /* Slightly transparent white */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        direction: rtl;
        text-align: right;
        color: #333;
    }

    #explanation h2 {
        color: #4a148c; /* Deep purple */
        border-bottom: 2px solid #e1bee7; /* Light purple */
        padding-bottom: 12px;
        margin-bottom: 20px;
        font-size: 1.6em;
        text-align: right; /* Align explanation header right */
    }

    #explanation p, #explanation ul {
        line-height: 1.7; /* Increased line height */
        margin-bottom: 20px; /* Increased margin */
    }

    #explanation ul {
        padding-right: 25px; /* Increased padding */
    }

    #explanation li {
        margin-bottom: 10px; /* Increased margin */
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .simulation-area {
            flex-direction: column;
            align-items: center;
            gap: 40px; /* More vertical space when stacked */
        }

        .input-area, .neuron-layer-area, .output-area {
            width: 80%; /* Take more width on smaller screens */
            min-width: auto;
        }

        .neuron-layer {
            flex-direction: row; /* Arrange neurons horizontally in column layout */
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
        }

        .node {
            width: auto; /* Let content define width */
            min-width: 100px;
        }

        .control-group {
             flex-direction: column;
             align-items: flex-start;
             gap: 8px;
        }

        .control-group label {
             flex-basis: auto;
             width: 100%;
             text-align: right;
        }

        .control-group input[type="range"] {
            width: 100%;
            min-width: auto;
        }
    }
</style>

<button id="show-explanation-button">מה קורה כאן בעצם? (הסבר מפורט)</button>

<div id="explanation" style="display: none;">
    <h2>מהו חישוב נוירומורפי ומדוע הוא שונה ממחשוב קלאסי?</h2>
    <p>חישוב נוירומורפי הוא גישת מחשוב חדשנית המבקשת לחקות את המבנה ואופן הפעולה של המוח האנושי, עם דגש מיוחד על יעילות אנרגטית ומהירות במשימות של זיהוי תבניות בזמן אמת. בניגוד למחשבים קלאסיים המבוססים על ארכיטקטורת פון נוימן המפרידה בין יחידת עיבוד לזיכרון ומעבדת מידע בסדר לינארי קפדני, מערכות נוירומורפיות משלבות זיכרון ועיבוד באותה יחידה ומעבדות מידע באופן מקבילי ומבוזר, בדומה לאופן שבו מיליארדי הנוירונים במוח פועלים בו-זמנית.</p>

    <h2>הלב של המודל: חיקוי נוירונים וסינפסות</h2>
    <p>הבסיס לחישוב נוירומורפי הוא חיקוי היחידות הביולוגיות הבסיסיות של המוח: נוירונים (תאי עצב) וסינפסות (הקשרים ביניהם). שבבים נוירומורפיים מכילים אלפי עד מיליוני "נוירונים מלאכותיים" ו"סינפסות מלאכותיות" המחוברים זה לזה ברשת צפופה. כל "סינפסה" מחזיקה ב"משקל" שמייצג את חוזק הקשר שלה - עד כמה היא מעבירה את ה"אות". שינוי המשקלים האלה, לעיתים קרובות בתגובה לאופן שבו פולסים עוברים ברשת, הוא המקבילה לתהליך הלמידה במוח.</p>

    <h2>עיבוד מבוסס אירועים: המפתח ליעילות</h2>
    <p>רוב המערכות הנוירומורפיות המודרניות מתבססות על מודל הנקרא רשתות נוירונים "פולסניות" (Spiking Neural Networks - SNNs). ברשתות אלו, המידע אינו עובר כערכים רציפים (כמו במחשב קלאסי או אפילו ברשתות נוירונים עמוקות מסורתיות), אלא כ"פולסים" או "ספייקים" דיגיטליים קצרים, המחקים את האותות החשמליים בנוירונים ביולוגיים. נוירון מלאכותי "יורה" פולס רק כאשר סך האותות (פולסים כפול משקלי הסינפסות) הנכנסים אליו מגיעים ל"סף" מסוים. גישה זו, המכונה "עיבוד מבוסס אירועים", היא מקבילית (נוירונים רבים פועלים בו זמנית) וחסכונית באנרגיה, מכיוון שפעולה מתרחשת רק כשיש פולס רלוונטי, ולא באופן רציף.</p>

    <h2>יתרונות בולטים: מהירות, יעילות ואפילו עמידות</h2>
    <ul>
        <li>**יעילות אנרגטית קיצונית:** בזכות העיבוד מבוסס האירועים, שבבים נוירומורפיים צורכים הרבה פחות אנרגיה ממחשבים קלאסיים או מאיצי AI מסורתיים, מה שהופך אותם אידיאליים ליישומים במכשירים ניידים, חיישנים או רובוטים.</li>
        <li>**מהירות תגובה ועיבוד בזמן אמת:** הארכיטקטורה המקבילית והמבוססת אירועים מתאימה באופן טבעי למשימות הדורשות תגובה מהירה ומיידית לזרם נתונים, כמו זיהוי עצמים ברכב אוטונומי, ניתוח נתונים מחיישנים תעשייתיים, או עיבוד אותות שמע ווידאו בזמן אמת.</li>
        <li>**עמידות לתקלות:** בדומה למוח הביולוגי, שיש לו יתירות מובנית, פגיעה בנוירון או קשר יחיד ברשת נוירומורפית לרוב לא תגרום לכשל מוחלט של המערכת כולה.</li>
    </ul>

    <h2>הדרך עוד ארוכה, אך הפוטנציאל עצום</h2>
    <p>למרות היתרונות המרשימים, חישוב נוירומורפי עדיין נמצא בשלבי פיתוח מוקדמים יחסית. האתגרים העיקריים כוללים:</p>
    <ul>
        <li>**פיתוח חומרה מתקדמת:** בניית שבבים נוירומורפיים גדולים, גמישים ויעילים היא משימה טכנולוגית מורכבת.</li>
        <li>**אלגוריתמים ותוכנה חדשניים:** נדרשת פיתוח של אלגוריתמים ושיטות תכנות שונות מהמקובל, שיוכלו לנצל ביעילות את הארכיטקטורה המבוססת אירועים.</li>
        <li>**מודלי למידה יעילים:** פיתוח מודלים של למידה (המקבילה ל"אימון") עבור רשתות פולסניות עדיין מאתגר במשימות מסוימות בהשוואה לרשתות עמוקות קלאסיות.</li>
    </ul>
    <p>עם זאת, היישומים הפוטנציאליים מרתקים: רובוטיקה שתופסת ומגיבה לסביבתה באופן אינטואיטיבי, מכשירים לבישים עם יכולות AI מתקדמות, מערכות אבטחה שמזהות אנומליות בזמן אמת, מכשירי שמיעה וראייה אלקטרוניים יעילים, ואפילו כלי חזק יותר להבנת המוח הביולוגי עצמו. העתיד שבו מחשבים "חושבים" יותר כמונו קרוב מתמיד.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {

        // --- DOM Elements and Network Structure ---
        const svgLayer = document.querySelector('.connections-layer');
        const network = {
            inputs: [
                { id: 0, element: document.querySelector('.input-node[data-input-id="0"]') },
                { id: 1, element: document.querySelector('.input-node[data-input-id="1"]') },
                { id: 2, element: document.querySelector('.input-node[data-input-id="2"]') }
            ],
            neurons: [ // Hidden layer
                { id: 0, element: document.querySelector('.neuron[data-neuron-id="0"]'), threshold: 1.5, currentInputSum: 0, firing: false, sumElement: document.querySelector('.neuron[data-neuron-id="0"] .current-sum') },
                { id: 1, element: document.querySelector('.neuron[data-neuron-id="1"]'), threshold: 1.0, currentInputSum: 0, firing: false, sumElement: document.querySelector('.neuron[data-neuron-id="1"] .current-sum') },
                { id: 2, element: document.querySelector('.neuron[data-neuron-id="2"]'), threshold: 2.0, currentInputSum: 0, firing: false, sumElement: document.querySelector('.neuron[data-neuron-id="2"] .current-sum') }
            ],
            output: { id: 0, element: document.getElementById('output-node'), threshold: 1.0, currentInputSum: 0, active: false, sumElement: null /* Output doesn't show sum in this model */ },
            connections: [
                // Define connections with default weights
                { from: 'input', fromId: 0, to: 'neuron', toId: 0, weight: 1.0, element: null, pathElement: null }, // Input 0 -> Neuron 0
                { from: 'input', fromId: 1, to: 'neuron', toId: 1, weight: 1.0, element: null, pathElement: null }, // Input 2 -> Neuron 2 (originally Input 1 -> Neuron 1) - Corrected mapping for example controls
                { from: 'input', fromId: 2, to: 'neuron', toId: 2, weight: 1.0, element: null, pathElement: null }, // Input 3 -> Neuron 3 (originally Input 2 -> Neuron 2) - Corrected mapping
                // Add more connections
                { from: 'neuron', fromId: 0, to: 'neuron', toId: 1, weight: 0.5, element: null, pathElement: null }, // Neuron 0 -> Neuron 1
                { from: 'neuron', fromId: 1, to: 'neuron', toId: 0, weight: 0.5, element: null, pathElement: null }, // Neuron 1 -> Neuron 0 (recurrent/feedback)
                { from: 'neuron', fromId: 0, to: 'output', toId: 0, weight: 1.0, element: null, pathElement: null }, // Neuron 0 -> Output
                { from: 'neuron', fromId: 1, to: 'output', toId: 0, weight: 1.0, element: null, pathElement: null }, // Neuron 1 -> Output
                { from: 'neuron', fromId: 2, to: 'output', toId: 0, weight: 1.0, element: null, pathElement: null }  // Neuron 2 -> Output
            ]
        };

        // Map control elements to network structure
        const controls = {
            thresholdNeuron1: {
                input: document.getElementById('threshold-neuron1'),
                valueSpan: document.getElementById('threshold-neuron1-value'),
                target: network.neurons.find(n => n.id === 0), // Neuron 1 (ID 0)
                property: 'threshold'
            },
            weightInput0Neuron0: {
                input: document.getElementById('weight-input0-to-neuron0'),
                valueSpan: document.getElementById('weight-input0-to-neuron0-value'),
                target: network.connections.find(c => c.from === 'input' && c.fromId === 0 && c.to === 'neuron' && c.toId === 0),
                 property: 'weight'
            },
             weightNeuron1Output: {
                 input: document.getElementById('weight-neuron1-to-output'),
                 valueSpan: document.getElementById('weight-neuron1-to-output-value'),
                 target: network.connections.find(c => c.from === 'neuron' && c.fromId === 1 && c.to === 'output' && c.toId === 0),
                  property: 'weight'
             }
        };


        // --- Connection Drawing Logic ---

        // Helper to get center coordinates of an element
        function getElementCenter(element) {
            const rect = element.getBoundingClientRect();
            const containerRect = svgLayer.parentElement.getBoundingClientRect(); // Use simulation-area for offset
            return {
                x: rect.left + rect.width / 2 - containerRect.left,
                y: rect.top + rect.height / 2 - containerRect.top
            };
        }

        // Draw or update all connections
        function drawConnections() {
            // Clear previous connections
            svgLayer.innerHTML = '';

            network.connections.forEach(conn => {
                const fromNode = conn.from === 'input' ? network.inputs.find(n => n.id === conn.fromId) : network.neurons.find(n => n.id === conn.fromId);
                const toNode = conn.to === 'neuron' ? network.neurons.find(n => n.id === conn.toId) : network.output;

                if (fromNode && toNode) {
                    const start = getElementCenter(fromNode.element);
                    const end = getElementCenter(toNode.element);

                    // Create SVG path element
                    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');

                    // Use a small curve for better visualization, especially for recurrent connections
                    let pathData;
                     if (conn.from === 'neuron' && conn.to === 'neuron' && conn.fromId !== conn.toId) { // Curve between different neurons
                         const midX1 = start.x + (end.x - start.x) * 0.3;
                         const midY1 = start.y + (end.y - start.y) * 0.3 + 30; // Control point offset
                         const midX2 = start.x + (end.x - start.x) * 0.7;
                         const midY2 = start.y + (end.y - start.y) * 0.7 + 30; // Control point offset
                          pathData = `M ${start.x},${start.y} C ${midX1},${midY1} ${midX2},${midY2} ${end.x},${end.y}`;
                     } else if (conn.from === conn.to && conn.fromId === conn.toId) { // Self-loop (not in this specific simplified model, but good practice)
                         // Simple loop - might not be needed for this structure
                          pathData = `M ${start.x},${start.y} C ${start.x - 30},${start.y - 30} ${start.x + 30},${start.y - 30} ${start.x},${start.y}`;
                     }
                     else { // Straight line
                         pathData = `M ${start.x},${start.y} L ${end.x},${end.y}`;
                     }


                    path.setAttribute('d', pathData);
                    path.setAttribute('class', 'connection-path');
                    path.style.strokeWidth = 3 * conn.weight; // Visualize weight with thickness (simple)
                    svgLayer.appendChild(path);

                    // Store the path element back in the connection object
                    conn.pathElement = path;
                }
            });
        }

        // Redraw connections on window resize to handle responsiveness
        window.addEventListener('resize', drawConnections);


        // --- Simulation Logic ---

        function resetSimulation() {
            network.neurons.forEach(n => {
                n.currentInputSum = 0;
                n.firing = false;
                n.element.classList.remove('firing', 'show-sum');
                n.sumElement.textContent = n.currentInputSum.toFixed(1);
            });
            network.output.currentInputSum = 0;
            network.output.active = false;
            network.output.element.classList.remove('active');
             network.output.element.textContent = 'ממתין לקלט...'; // Reset output text

            // Reset connection animations
            network.connections.forEach(conn => {
                if (conn.pathElement) {
                     conn.pathElement.classList.remove('active');
                     // Reset dash offset animation state if needed (more complex with restarts)
                     conn.pathElement.style.animation = 'none'; // Clear previous animation
                     void conn.pathElement.offsetWidth; // Trigger reflow
                     conn.pathElement.style.animation = null; // Re-enable default animation
                }
            });
        }

        // Main activation function
        function activateNetwork(inputIndex) {
            resetSimulation();

            // Step 1: Input Layer Activation
            const signalFromInput = 1.0; // Assume input sends a pulse signal of strength 1
            const activatedInputElement = network.inputs.find(input => input.id === inputIndex).element;
             activatedInputElement.classList.add('activated'); // Animate input node

            const inputConnections = network.connections.filter(conn => conn.from === 'input' && conn.fromId === inputIndex);

            // Animate signal propagation from input
            inputConnections.forEach(conn => {
                 if(conn.pathElement) conn.pathElement.classList.add('active');
            });

            // Use timeouts to simulate signal propagation delay
            setTimeout(() => {
                 activatedInputElement.classList.remove('activated');

                // Distribute signal from input to connected neurons
                inputConnections.forEach(conn => {
                    if (conn.to === 'neuron') {
                        const targetNeuron = network.neurons.find(n => n.id === conn.toId);
                        if (targetNeuron) {
                            targetNeuron.currentInputSum += signalFromInput * conn.weight;
                             targetNeuron.sumElement.textContent = targetNeuron.currentInputSum.toFixed(1);
                             targetNeuron.element.classList.add('show-sum'); // Show sum while processing
                        }
                    }
                });

                // Step 2: Process Hidden Layer (after receiving input signals)
                setTimeout(() => {
                    const firingNeurons = [];
                    network.neurons.forEach(neuron => {
                        neuron.element.classList.remove('show-sum'); // Hide sum after processing attempt
                        if (neuron.currentInputSum >= neuron.threshold) {
                            neuron.firing = true;
                            neuron.element.classList.add('firing');
                            firingNeurons.push(neuron);
                        }
                    });

                    // Step 3: Propagate signals from firing neurons
                    firingNeurons.forEach(firingNeuron => {
                        const signalFromNeuron = 1.0; // Firing neuron sends a pulse of strength 1

                        const connectionsFromNeuron = network.connections.filter(conn => conn.from === 'neuron' && conn.fromId === firingNeuron.id);

                         // Animate signal propagation from firing neuron
                        connectionsFromNeuron.forEach(conn => {
                            if(conn.pathElement) conn.pathElement.classList.add('active');
                        });

                        // Distribute signal to connected neurons/output (in this simple model, it goes directly to output)
                        connectionsFromNeuron.forEach(conn => {
                            if (conn.to === 'output') {
                                 // Accumulate input at the output node
                                 network.output.currentInputSum += signalFromNeuron * conn.weight;
                            }
                             // Note: In a real SNN, this could trigger subsequent layer neurons.
                             // This simple model fires hidden neurons and then immediately calculates output.
                        });
                    });

                     // Step 4: Process Output Layer (after receiving signals from hidden layer)
                     setTimeout(() => {
                         // Remove firing state after propagation delay
                          firingNeurons.forEach(neuron => neuron.element.classList.remove('firing'));
                          // Remove signal animation from connections
                          network.connections.forEach(conn => conn.pathElement?.classList.remove('active'));

                         if (network.output.currentInputSum >= network.output.threshold) {
                             network.output.active = true;
                             network.output.element.classList.add('active');
                             network.output.element.textContent = '🔥 פלט: פעולה/זיהוי הופעל! 🔥';
                         } else {
                              network.output.element.textContent = '💤 פלט: ללא פעולה 💤';
                         }
                     }, 600); // Delay for output visualization

                }, 500); // Delay for hidden layer processing and firing
            }, 400); // Delay for signal propagation from input
        }

        // --- Event Listeners ---

        // Add event listeners to input buttons
        network.inputs.forEach(input => {
            input.element.addEventListener('click', () => {
                activateNetwork(input.id);
            });
        });

        // Add event listeners for controls
        for (const key in controls) {
             const control = controls[key];
             if (control.input && control.target) {
                 control.input.addEventListener('input', (event) => {
                     const value = parseFloat(event.target.value);
                     control.valueSpan.textContent = value.toFixed(1);
                     control.target[control.property] = value;

                     // If changing weight, update connection line thickness visually
                     if (control.property === 'weight' && control.target.pathElement) {
                          control.target.pathElement.style.strokeWidth = 3 * value; // Simple visual feedback
                     }
                 });
                  // Initialize the control value display
                 control.valueSpan.textContent = control.target[control.property].toFixed(1);
             }
        }


        // Explanation toggle
        const explanationDiv = document.getElementById('explanation');
        const showExplanationButton = document.getElementById('show-explanation-button');

        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            showExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט ⬆️' : 'מה קורה כאן בעצם? (הסבר מפורט) ⬇️';
        });

        // --- Initialization ---

        // Initial drawing of connections
        drawConnections();

        // Initialize simulation state and output text
         resetSimulation();

    });
</script>
```