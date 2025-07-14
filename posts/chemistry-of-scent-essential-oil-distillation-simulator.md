---
title: "מסע אל לב הריח: סימולטור זיקוק שמנים אתריים"
english_slug: chemistry-of-scent-essential-oil-distillation-simulator
category: "כימיה"
tags: שמנים אתריים, זיקוק, כימיה אורגנית, תהליכים תעשייתיים, צמחי מרפא, מעבדה
---
# מסע אל לב הריח: סימולטור זיקוק שמנים אתריים

האם אי פעם תהיתם איך לוכדים את המהות הריחנית של צמחים כמו לבנדר, ורד או מנטה? מאחורי התהליך המסתורי של זיקוק בקיטור מסתתרים עקרונות מדעיים מרתקים שקובעים את איכות ועוצמת הריח בבקבוקון הקטן. בואו לצלול למעבדה הדיגיטלית שלנו ולגלות איך טמפרטורה, זמן וכמות חומר גלם משפיעים על התוצאה. האם תצליחו להפוך למומחי זיקוק ולמצוא את הנוסחה לשמן האתרי המושלם?

<div id="simulator-container">
    <div class="controls panel">
        <h2>קבע את תנאי הזיקוק</h2>
        <div class="param-group">
            <label for="material-amount">כמות חומר גלם צמחי (גרם):</label>
            <input type="range" id="material-amount" value="500" min="100" max="1000" step="50">
            <span class="param-value" id="material-amount-value">500</span> גרם
        </div>
        <div class="param-group">
            <label for="steam-temp">טמפרטורת קיטור (צלזיוס):</label>
             <input type="range" id="steam-temp" value="105" min="100" max="150" step="1">
             <span class="param-value" id="steam-temp-value">105</span> °C
        </div>
        <div class="param-group">
            <label for="distillation-time">זמן זיקוק (דקות):</label>
            <input type="range" id="distillation-time" value="60" min="10" max="120" step="5">
            <span class="param-value" id="distillation-time-value">60</span> דקות
        </div>
        <button id="run-simulation">התחל זיקוק</button>
    </div>

    <div class="visualization panel">
        <h2>מערכת הזיקוק בפעולה</h2>
        <div class="apparatus">
            <div class="boiler apparatus-item">
                <div class="liquid"></div>
                <div class="steam-outlet"></div>
                <div class="label">דוד<br>חימום</div>
                <div class="animation steam"></div>
            </div>
            <div class="connector right steam-pipe"></div>
            <div class="plant-vessel apparatus-item">
                <div class="plant"></div>
                <div class="steam-inlet"></div>
                <div class="vapor-outlet"></div>
                <div class="label">כלי הצמח</div>
                <div class="animation vapor"></div>
            </div>
            <div class="connector right vapor-pipe"></div>
            <div class="condenser apparatus-item">
                 <div class="cooling-jacket"></div>
                 <div class="vapor-inlet"></div>
                 <div class="liquid-outlet"></div>
                <div class="label">מעבה</div>
                <div class="animation drops"></div>
            </div>
             <div class="connector right liquid-pipe"></div>
            <div class="receiver apparatus-item">
                <div class="liquid-inlet"></div>
                <div class="liquid-container">
                    <div id="oil-layer" class="layer oil">שמן</div>
                    <div id="hydrosol-layer" class="layer hydrosol">הידרוסול</div>
                </div>
                <div class="label">פירנז</div>
            </div>
        </div>
        <div id="sim-status" class="status-message">מוכן להפעלה... נסה לשנות את הפרמטרים.</div>
    </div>

    <div class="results panel">
        <h2>תוצאות הזיקוק</h2>
        <p>כמות שמן אתרי שהתקבלה: <span id="oil-result">-</span> מ"ל</p>
        <p>איכות השמן: <span id="quality-result">-</span> / 5 כוכבים</p>
        <div class="feedback-message" id="feedback-message"></div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;600&display=swap');

    #simulator-container {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        display: flex;
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
        padding: 30px; /* Increased padding */
        border: none; /* Remove outer border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Gentle gradient background */
        max-width: 1000px; /* Wider container */
        margin: 30px auto;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Stronger shadow */
        position: relative; /* For potential background elements */
        overflow: hidden;
    }

    #simulator-container::before {
        content: '';
        position: absolute;
        top: -50px;
        left: -50px;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 70%);
        z-index: 0;
    }


    .panel {
        flex: 1;
        min-width: 300px; /* Adjusted min-width */
        padding: 20px; /* Increased padding */
        border: none; /* Remove border */
        border-radius: 10px; /* Rounded corners */
        background-color: rgba(255, 255, 255, 0.95); /* Semi-transparent white */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        display: flex;
        flex-direction: column;
    }

    .controls h2, .visualization h2, .results h2 {
        text-align: center;
        color: #00796b; /* Teal color */
        margin-top: 0;
        margin-bottom: 20px; /* More space below heading */
        border-bottom: 2px solid #00796b; /* Matching border */
        padding-bottom: 10px;
        font-weight: 600;
    }

    .param-group {
        margin-bottom: 20px; /* More space between params */
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .param-group label {
        display: block;
        margin-bottom: 8px; /* More space below label */
        font-weight: 600;
        color: #333;
    }

    .param-group input[type="range"] {
        width: 100%;
        -webkit-appearance: none; /* Override default appearance */
        appearance: none;
        height: 8px; /* Thicker slider */
        background: #b2ebf2; /* Light blue track */
        outline: none;
        opacity: 0.8;
        transition: opacity 0.2s ease;
        border-radius: 4px;
        margin-bottom: 5px;
    }

     .param-group input[type="range"]:hover {
        opacity: 1;
     }

     .param-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* Larger thumb */
        height: 20px; /* Larger thumb */
        background: #00796b; /* Teal thumb */
        cursor: pointer;
        border-radius: 50%; /* Round thumb */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
     }

     .param-group input[type="range"]::-moz-range-thumb {
        width: 20px; /* Larger thumb */
        height: 20px; /* Larger thumb */
        background: #00796b; /* Teal thumb */
        cursor: pointer;
        border-radius: 50%; /* Round thumb */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
     }

    .param-value {
        font-weight: 600;
        color: #004d40; /* Darker teal */
        min-width: 40px; /* Reserve space */
        text-align: left; /* Align value to the left */
        display: inline-block;
        margin-right: 5px; /* Space between value and unit */
    }


    #run-simulation {
        display: block;
        width: 100%;
        padding: 12px; /* More padding */
        background-color: #00796b; /* Teal button */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        font-size: 1.2rem; /* Larger font */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 600;
        margin-top: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    #run-simulation:hover {
        background-color: #004d40; /* Darker teal on hover */
    }

    #run-simulation:active {
        transform: scale(0.98); /* Press effect */
    }

     #run-simulation:disabled {
         background-color: #b2dfdb; /* Lighter teal when disabled */
         cursor: not-allowed;
         box-shadow: none;
     }


    .visualization {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between; /* Distribute space */
    }

    .apparatus {
        display: flex;
        align-items: flex-end; /* Align items to bottom */
        justify-content: center; /* Center the apparatus horizontally */
        width: 100%;
        margin-bottom: 20px;
        gap: 5px; /* Space between components and connectors */
    }

    .apparatus-item {
        position: relative;
        text-align: center;
        min-width: 80px; /* Fixed min-width */
        width: 15%; /* Flex width */
        height: 120px; /* Fixed height for visualization area */
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        border: 2px solid #ccc; /* Border */
        border-radius: 8px;
        background-color: #fff; /* White background */
        overflow: hidden; /* Hide overflow from animations */
        box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
    }

    .apparatus-item .label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #555;
        padding: 5px;
        background-color: rgba(255,255,255,0.8);
        border-top: 1px solid #eee;
        width: 100%;
        text-align: center;
        z-index: 10; /* Ensure label is on top */
        position: relative; /* Needed for z-index */
    }

    /* Specific item styles */
    .boiler { background: #ffe0b2; } /* Light orange */
    .plant-vessel { background: #c8e6c9; } /* Light green */
    .condenser { background: #bbdefb; } /* Light blue */
    .receiver {
         background: #e1bee7; /* Light purple */
         display: flex;
         flex-direction: column-reverse; /* Layers fill from bottom */
         justify-content: flex-start; /* Align items to start (top) */
         align-items: center;
    }

    .boiler .liquid {
        width: 100%;
        height: 30%; /* Water level */
        background: #4fc3f7; /* Blue water */
        position: absolute;
        bottom: 30px; /* Above the label */
        left: 0;
        box-shadow: inset 0 -5px 5px rgba(0,0,0,0.2);
        z-index: 1;
    }
     .boiler .steam-outlet, .plant-vessel .steam-inlet,
     .plant-vessel .vapor-outlet, .condenser .vapor-inlet,
     .condenser .liquid-outlet, .receiver .liquid-inlet {
         position: absolute;
         width: 10px;
         height: 10px;
         background: #757575; /* Grey pipe connector */
         border-radius: 3px;
         z-index: 5;
     }

    .boiler .steam-outlet { top: 10%; right: -5px; }
    .plant-vessel .steam-inlet { top: 10%; left: -5px; }
    .plant-vessel .vapor-outlet { top: 10%; right: -5px; }
    .condenser .vapor-inlet { top: 10%; left: -5px; }
    .condenser .liquid-outlet { bottom: 30px; right: -5px; } /* Exit above label */
     .receiver .liquid-inlet { bottom: 30px; left: -5px; } /* Entry above label */


     .connector {
         width: 20px; /* Width of pipes */
         height: 5px;
         background-color: #757575; /* Grey pipe */
         position: relative;
         margin: 0 -10px; /* Overlap with items */
         z-index: 4; /* Below connectors */
     }
    .steam-pipe { top: -45px; } /* Position vertically */
    .vapor-pipe { top: -45px; } /* Position vertically */
    .liquid-pipe { top: -5px; } /* Position vertically */


    /* Animation Elements */
    .animation {
        position: absolute;
        width: 100%;
        height: calc(100% - 30px); /* Area above label */
        top: 0;
        left: 0;
        overflow: hidden;
        z-index: 2;
    }

    /* Steam Animation */
    .animation.steam {
        /* Style for steam particles */
    }

    .steam-particle {
        position: absolute;
        bottom: 0;
        left: 50%;
        width: 5px;
        height: 5px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 50%;
        opacity: 0;
        animation: steam-flow 1s linear infinite forwards;
    }

    @keyframes steam-flow {
        0% { transform: translate(-50%, 0) scale(0.5); opacity: 0.5; }
        50% { opacity: 1; }
        100% { transform: translate(-50%, -100px) scale(1.2); opacity: 0; } /* Adjust -100px to height of animation area */
    }

     /* Vapor Animation (similar to steam but maybe tinted?) */
    .animation.vapor {
        /* Style for vapor particles */
    }
    .vapor-particle {
         position: absolute;
         bottom: 0; /* Or top? Depends on flow direction */
         left: 50%;
         width: 5px;
         height: 5px;
         background: rgba(255, 250, 200, 0.8); /* Slightly yellow tint */
         border-radius: 50%;
         opacity: 0;
         animation: vapor-flow 1s linear infinite forwards;
    }
     @keyframes vapor-flow {
         0% { transform: translate(-50%, 0) scale(0.5); opacity: 0.5; }
         50% { opacity: 1; }
         100% { transform: translate(-50%, -100px) scale(1.2); opacity: 0; } /* Adjust -100px */
     }


     /* Condenser Drops Animation */
     .animation.drops {
         /* Style for drops */
     }
     .drop-particle {
         position: absolute;
         top: 0;
         left: 50%; /* Center initially */
         width: 6px;
         height: 6px;
         background: rgba(173, 216, 230, 0.9); /* Light blue */
         border-radius: 50%;
         opacity: 0;
         animation: drop-fall 1s linear infinite forwards;
     }

     @keyframes drop-fall {
         0% { transform: translate(-50%, 0); opacity: 0.8; }
         20% { opacity: 1; }
         100% { transform: translate(-50%, 120px); opacity: 0; } /* Adjust 120px to fill height */
     }


    /* Receiver layers */
    .receiver .liquid-container {
        width: 100%;
        height: calc(100% - 30px); /* Area above label */
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column-reverse; /* Fill from bottom */
    }

    .receiver .layer {
        width: 100%;
        text-align: center;
        font-size: 0.7rem; /* Smaller text */
        font-weight: 600;
        color: #333;
        position: relative; /* Relative within flex container */
        height: 0; /* Initially empty */
        flex-shrink: 0; /* Prevent shrinking */
        transition: height 2s ease-out; /* Smooth fill animation */
        display: flex; /* Center text vertically */
        align-items: center;
        justify-content: center;
    }

    .receiver .layer.hydrosol {
        background-color: rgba(173, 216, 230, 0.7); /* Light blue */
        border-top: 1px solid rgba(0,0,0,0.1);
    }

    .receiver .layer.oil {
        background-color: rgba(255, 255, 0, 0.7); /* Yellow */
        border-top: 1px solid rgba(0,0,0,0.1);
        z-index: 2;
    }


    .status-message {
        margin-top: 20px; /* More space */
        font-style: italic;
        color: #004d40; /* Dark teal */
        text-align: center;
        min-height: 1.5em; /* Prevent layout shift */
        font-size: 1rem;
        animation: pulse 1.5s infinite alternate; /* Add a subtle pulse effect */
    }
     @keyframes pulse {
         0% { opacity: 0.8; }
         100% { opacity: 1; }
     }
     .status-message.active {
        font-weight: 600;
        color: #d32f2f; /* Red during simulation */
        animation: none; /* Remove pulse during active sim */
     }


    .results p {
        font-size: 1.2rem; /* Larger font */
        margin-bottom: 12px;
        color: #333;
    }

    .results span {
        font-weight: 600;
        color: #00796b; /* Teal */
    }

    #quality-result {
        color: #fbc02d; /* Amber for quality stars */
        font-size: 1.4rem; /* Larger star rating */
    }

    .feedback-message {
        margin-top: 20px;
        padding: 15px;
        border-radius: 6px;
        background-color: #e0f2f7; /* Very light blue */
        border: 1px solid #b2ebf2; /* Light blue border */
        color: #004d40; /* Dark teal text */
        min-height: 1.5em;
        font-style: italic;
        opacity: 0; /* Hide initially */
        transition: opacity 0.5s ease-in-out;
    }
     .feedback-message.visible {
         opacity: 1;
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 10px 20px;
        background-color: #607d8b; /* Blue grey */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
        font-weight: 400;
    }

    #toggle-explanation:hover {
        background-color: #455a64; /* Darker blue grey */
    }

    #explanation-section {
        max-width: 900px; /* Same width as simulator container */
        margin: 0 auto 30px auto;
        padding: 30px;
        border: none; /* Remove border */
        border-radius: 12px;
        background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        display: none; /* Initially hidden */
        line-height: 1.7; /* More comfortable reading */
        color: #333;
    }

    #explanation-section h2 {
        color: #00796b; /* Matching title color */
        margin-top: 25px; /* More space above headings */
        padding-bottom: 8px;
        border-bottom: 2px dashed #b2dfdb; /* Light dashed border */
        font-weight: 600;
    }
     #explanation-section h2:first-child {
         margin-top: 0;
     }


    #explanation-section p {
        margin-bottom: 18px;
    }

    #explanation-section ul {
        margin-bottom: 18px;
        padding-right: 25px; /* More padding */
    }
    #explanation-section li {
        margin-bottom: 10px;
        line-height: 1.5;
    }

    #explanation-section strong {
        color: #004d40; /* Darker teal for emphasis */
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        #simulator-container, #explanation-section {
            padding: 20px;
            gap: 20px;
        }

        .panel {
            padding: 15px;
            min-width: 100%; /* Stack panels */
        }

        .apparatus {
            flex-direction: column; /* Stack apparatus vertically */
            align-items: center;
            gap: 10px;
        }

        .apparatus-item {
            width: 80%; /* Wider stacked items */
            height: 100px; /* Slightly shorter */
        }
         .connector {
             width: 5px;
             height: 20px; /* Vertical connectors */
             margin: -10px 0;
         }
         .steam-pipe, .vapor-pipe, .liquid-pipe {
             top: auto; /* Remove vertical positioning */
             left: auto;
         }
        .boiler .steam-outlet { top: auto; right: 50%; bottom: -5px; transform: translateX(50%); }
        .plant-vessel .steam-inlet { top: auto; left: 50%; transform: translateX(-50%); bottom: -5px; }
        .plant-vessel .vapor-outlet { bottom: auto; right: 50%; top: -5px; transform: translateX(50%);}
        .condenser .vapor-inlet { bottom: auto; left: 50%; transform: translateX(-50%); top: -5px;}
        .condenser .liquid-outlet { right: auto; bottom: 50%; left: -5px; transform: translateY(50%); } /* Side exit */
        .receiver .liquid-inlet { left: auto; bottom: 50%; right: -5px; transform: translateY(-50%); } /* Side entry */

        /* Adjust vertical animation ranges for stacked layout */
         @keyframes steam-flow {
             0% { transform: translate(-50%, 0) scale(0.5); opacity: 0.5; }
             50% { opacity: 1; }
             100% { transform: translate(-50%, -70px) scale(1.2); opacity: 0; } /* Adjust -70px */
         }
         @keyframes vapor-flow {
             0% { transform: translate(-50%, 0) scale(0.5); opacity: 0.5; }
             50% { opacity: 1; }
             100% { transform: translate(-50%, -70px) scale(1.2); opacity: 0; } /* Adjust -70px */
         }
         @keyframes drop-fall {
             0% { transform: translate(-50%, 0); opacity: 0.8; }
             20% { opacity: 1; }
             100% { transform: translate(-50%, 90px); opacity: 0; } /* Adjust 90px */
         }
         .receiver .liquid-container {
              height: calc(100% - 30px); /* Area above label */
              flex-direction: column-reverse; /* Still fill from bottom */
         }
    }

</style>

<button id="toggle-explanation">הסבר על זיקוק שמנים אתריים: צלילה לעומק</button>

<div id="explanation-section">
    <h2>מה הופך צמח ל"ריחני"? הכירו את השמנים האתריים</h2>
    <p>שמנים אתריים הם לב הריח של צמחים רבים - תרכובות אורגניות מרוכזות ונדיפות שמקנות להם את ניחוחם הייחודי. הם לא סתם נעימים לאף; הם כלי הישרדות עבור הצמח, המשמשים למשיכת מאביקים, הגנה מפני מזיקים או מחלות, ואפילו תקשורת. בתוך בלוטות זעירות בעלים, בפרחים, בקליפה או בשורשים, אצור עולם שלם של מולקולות ארומטיות.</p>

    <h2>מולקולות עם אישיות: מבט על ההרכב הכימי</h2>
    <p>כל שמן אתרי הוא קוקטייל מורכב של עשרות ואף מאות תרכובות שונות, לרוב ממשפחת ה**טרפנים** וה**טרפנואידים**. לינאלול ולינאלול אצטט הם גיבורי הריח בלבנדר, מנטול ומנטון שולטים במנטה, ולימונן הוא סוד הקסם של פירות ההדר. האיזון המדויק בין המולקולות השונות הוא זה שיוצר את הניחוח הייחודי וההשפעות המגוונות של כל שמן.</p>

    <h2>זיקוק בקיטור: קסם של מים ואדים</h2>
    <p>זיקוק בקיטור הוא שיטה עתיקה וחכמה להפרדת שמנים אתריים עדינים מהמטריצה הצמחית. העיקרון פשוט אך גאוני: שמנים אתריים אוהבים להתאדות בטמפרטורות נמוכות יחסית כשהם נמצאים בסביבת קיטור. כשהקיטור עובר דרך חומר צמחי מחומם, הוא סוחף איתו את מולקולות השמן הנדיפות. התערובת האדירה הזו מקוררת במעבה, מתעברת חזרה לנוזל, ונאספת בכלי שבו השמן (הקל יותר מהמים) נפרד מההידרוסול (מי הפרחים).</p>

    <h2>שלבים במסע הריח: המערכת והתהליך</h2>
    <p>מערכת זיקוק קלאסית כוללת:</p>
    <ul>
        <li>**הדוד הרותח (Boiler):** שם המים הופכים לקיטור חם ואנרגטי.</li>
        <li>**כלי הגיבור הצמחי (Still/Alembic):** הבית הזמני של חומר הגלם הצמחי, שם הוא פוגש את הקיטור.</li>
        <li>**המעבה הקר (Condenser):** ה"מקלחת הקרה" של האדים, שם הם הופכים בחזרה לנוזל ריחני.</li>
        <li>**מפריד הקסם (Receiver/Separator):** לרוב פירנז שקוף, בו מתרחש הפלא: השמן צף למעלה, ההידרוסול נשאר למטה, והתוצר הסופי נאסף בקלות.</li>
    </ul>
    <p>התהליך כולו הוא ריקוד כימי-פיזיקלי המבוסס על נדיפות, לחצי אדים חלקיים, והעובדה הפשוטה ששמן ומים לא מתערבבים.</p>

    <h2>כמו שף במטבח: הגורמים המכריעים להצלחה</h2>
    <p>כדי להפיק שמן אתרי איכותי בכמות מרשימה, יש לשלוט בכמה "מתגים" קריטיים:</p>
    <ul>
        <li>**טמפרטורה ולחץ הקיטור:** חום ואדים מגבירים את קצב המיצוי, אך חום גבוה מדי עלול "לשרוף" או לפרק מולקולות עדינות בריח. נדרשת טמפרטורה "מתוקה" ואחידה.</li>
        <li>**זמן הזיקוק:** זיקוק קצר מדי משאיר שמן בצמח. זיקוק ארוך מדי עלול לפגוע באיכות, למצות מולקולות פחות נדיפות (שפוגעות בריח) או להרוס את הרגישות שכן יצאה.</li>
        <li>**כמות ואיכות חומר הגלם:** ככל שיש יותר צמח איכותי וטרי, כך הפוטנציאל גדול יותר.</li>
        <li>**הכנת הצמח:** גודל חלקיקי הצמח משפיע על נגישות הקיטור לבלוטות השמן.</li>
    </ul>
    <p>כמו במתכון מנצח, השילוב הנכון של כל המרכיבים האלה הוא הסוד.</p>

    <h2>יותר מריח טוב: שימושים מפתיעים</h2>
    <p>שמנים אתריים הם הרבה יותר מאשר רק "בושם טבעי". הם משמשים ב:**ארומתרפיה** להשפעה על הגוף והנפש, ב**רפואה מסורתית** בזכות תכונות אנטי-בקטריאליות ואנטי-דלקתיות, ב**תעשיית הקוסמטיקה והבשמים**, ב**מזון** כחומרי טעם טבעיים, ואפילו ב**ניקיון**. כל בקבוקון מכיל עוצמה מרוכזת מהטבע.</p>

    <h2>לכל שיטה יתרונות וחסרונות</h2>
    <p>זיקוק בקיטור הוא מצוין לשמנים רבים, הוא "נקי" יחסית (ללא ממסים כימיים) ויעיל לקנה מידה גדול. עם זאת, הוא לא מתאים לכל צמח (יש שמנים שלא נדיפים מספיק או עדינים מדי לחום), וחלק מהתרכובות נשארות בהידרוסול. שיטות אחרות כמו כבישה קרה (להדרים) או מיצוי ב-CO2 סופר-קריטי מתאימות לשמנים אחרים או מפיקות תוצרים עם פרופיל מעט שונה.</p>
     <p>עכשיו כשאתם מכירים את העקרונות, חזרו לסימולטור והפכו את הידע למעשה! נסו שילובים שונים של פרמטרים וגלו את נקודת האיזון שמובילה לתוצאות הטובות ביותר.</p>
</div>


<script>
    const materialInput = document.getElementById('material-amount');
    const tempInput = document.getElementById('steam-temp');
    const timeInput = document.getElementById('distillation-time');
    const runButton = document.getElementById('run-simulation');
    const oilResultSpan = document.getElementById('oil-result');
    const qualityResultSpan = document.getElementById('quality-result');
    const simStatusDiv = document.getElementById('sim-status');
    const oilLayerDiv = document.getElementById('oil-layer');
    const hydrosolLayerDiv = document.getElementById('hydrosol-layer');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationSection = document.getElementById('explanation-section');
    const materialValueSpan = document.getElementById('material-amount-value');
    const tempValueSpan = document.getElementById('steam-temp-value');
    const timeValueSpan = document.getElementById('distillation-time-value');
    const feedbackMessageDiv = document.getElementById('feedback-message');

    // Animation elements
    const boilerAnimation = document.querySelector('.boiler .animation.steam');
    const plantAnimation = document.querySelector('.plant-vessel .animation.vapor');
    const condenserAnimation = document.querySelector('.condenser .animation.drops');
    const receiverLiquidContainer = document.querySelector('.receiver .liquid-container');

    // Update value displays when sliders change
    materialInput.addEventListener('input', () => { materialValueSpan.textContent = materialInput.value; });
    tempInput.addEventListener('input', () => { tempValueSpan.textContent = tempInput.value; });
    timeInput.addEventListener('input', () => { timeValueSpan.textContent = timeInput.value; });


    const baseYieldPerGram = 0.08; // ml per gram max possible - Increased slightly for better numbers
    const extractionRateFactorBase = 0.0015; // Base extraction rate ml/g/min at 100C - Increased

    runButton.addEventListener('click', () => {
        const materialAmount = parseInt(materialInput.value);
        const steamTemp = parseInt(tempInput.value);
        const distillationTime = parseInt(timeInput.value);

        // Reset visual state
        oilLayerDiv.style.height = '0px';
        // Let hydrosol fill initially, it will be pushed down by oil
         const maxLiquidHeight = receiverLiquidContainer.clientHeight; // Use actual height of container
         hydrosolLayerDiv.style.height = `${maxLiquidHeight}px`;
         oilLayerDiv.textContent = ''; // Clear text during sim
         hydrosolLayerDiv.textContent = ''; // Clear text during sim
         oilResultSpan.textContent = '-';
         qualityResultSpan.textContent = '-';
         feedbackMessageDiv.textContent = '';
         feedbackMessageDiv.classList.remove('visible');


        // Disable controls and indicate active simulation
        runButton.disabled = true;
        simStatusDiv.textContent = 'מתחיל זיקוק...';
        simStatusDiv.classList.add('active');
        document.querySelectorAll('.param-group input').forEach(input => input.disabled = true);

        // --- Animation Start ---
        startAnimations(distillationTime);


        // --- Simulation Logic (delayed for animation) ---
        const simulationDuration = distillationTime * 20; // Scale visual time (e.g., 60 min sim = 1200ms = 1.2s real time)
                                                        // Let's make it a fixed minimum + scaled time for smoother feel
        const minSimDuration = 2000; // Minimum 2 seconds
        const scaledSimDuration = distillationTime * 10; // 10ms per simulated minute
        const actualSimDuration = Math.max(minSimDuration, scaledSimDuration);


        setTimeout(() => {
            // --- Calculation after "simulation" ---

            // Max possible oil from the material
            const maxPossibleOil = materialAmount * baseYieldPerGram; // ml

            // Extraction rate influenced by temperature (faster at higher temps)
            // Use a factor that increases, but maybe plateaus slightly at very high temps?
            // Simple linear for now: Factor of 1 at 100C, 3 at 150C -> (steamTemp - 100) / 25
            // Let's make it slightly non-linear to show diminishing returns on speed?
            // e.g., factor = 1 + Math.log10(steamTemp - 99); - Log grows slower
             const tempEffectFactor = 1 + (steamTemp - 100) / 20; // Factor of 1 at 100C, 3.5 at 150C - slightly faster extraction potential

            // Total potential oil extracted based on time and temperature *rate*
            // Rate is ml/gram/min * material * time
            const instantaneousExtractionRateMlPerMin = materialAmount * extractionRateFactorBase * tempEffectFactor; // ml/min potentially extracted
            const totalPotentialExtraction = instantaneousExtractionRateMlPerMin * distillationTime; // ml potentially extracted over time


            // Actual oil extracted is limited by the maximum possible from the material
            let actualOilExtracted = Math.min(totalPotentialExtraction, maxPossibleOil); // ml


            // --- Quality Logic ---
            let quality = 5; // Start with perfect quality

            // Optimal Temperature Range: 105-115 C
            const optimalTempMin = 105;
            const optimalTempMax = 115;

            if (steamTemp < optimalTempMin) {
                // Penalty for too low temp: inefficient extraction, maybe misses light volatile notes
                 const tempPenalty = (optimalTempMin - steamTemp) * 0.4; // Lose 0.4 quality for each C below 105
                 quality -= tempPenalty;
            } else if (steamTemp > optimalTempMax) {
                // Penalty for too high temp: degradation of delicate compounds
                const tempPenalty = (steamTemp - optimalTempMax) * 0.5; // Lose 0.5 quality for each C above 115
                quality -= tempPenalty;
            }

            // Optimal Time based on how fast extraction *could* happen at this temp with this material
            // Calculate time needed to get 90% of max possible oil at the given rate
            let theoreticalFullExtractionTime = 0;
             if (instantaneousExtractionRateMlPerMin > 0) {
                 theoreticalFullExtractionTime = maxPossibleOil * 0.9 / instantaneousExtractionRateMlPerMin;
             } else {
                 theoreticalFullExtractionTime = 10000; // Effectively infinite if rate is zero
             }

            // Adjust theoretical time minimum to avoid zero/very small numbers causing issues
            theoreticalFullExtractionTime = Math.max(10, theoreticalFullExtractionTime); // Minimum theoretical time 10 mins


            // Define ideal time window around the theoretical time
            const idealTimeMin = theoreticalFullExtractionTime * 0.8; // Should run at least 80% of theoretical time
            const idealTimeMax = theoreticalFullExtractionTime * 1.2; // Not longer than 120% of theoretical time

            if (distillationTime < idealTimeMin) {
                 // Penalty for too short time: Incomplete extraction, maybe only lightest notes captured, not full spectrum
                 const timePenalty = (idealTimeMin - distillationTime) * 0.2; // Lose 0.2 quality for each min too short
                 quality -= timePenalty;
                 // Also reduce yield slightly if time is too short compared to theoretical full extraction
                 actualOilExtracted = actualOilExtracted * Math.max(0.5, distillationTime / idealTimeMin); // Reduce yield if time is less than ideal min (cap at 50% yield loss)
            } else if (distillationTime > idealTimeMax) {
                 // Penalty for too long time: Extraction of less desirable/heavier compounds, degradation
                 const timePenalty = (distillationTime - idealTimeMax) * 0.3; // Lose 0.3 quality for each min too long
                 quality -= timePenalty;
            }


            // Ensure quality is between 1 and 5
            quality = Math.max(1, Math.min(5, Math.round(quality)));


            // --- Feedback Messages ---
            let feedback = "נסה לשנות את הפרמטרים כדי לראות איך הם משפיעים על התוצאות!";
            if (quality >= 4.5 && actualOilExtracted > maxPossibleOil * 0.8) {
                feedback = "מצוין! הצלחת להפיק כמות טובה של שמן באיכות גבוהה!";
            } else if (quality < 3) {
                 feedback = "השמן שהתקבל באיכות נמוכה. נסה להתאים את הטמפרטורה והזמן לטווח אופטימלי יותר.";
                 if (steamTemp < optimalTempMin) feedback += ` הטמפרטורה נמוכה מדי (${steamTemp}°C), שקול להעלות אותה.`;
                 if (steamTemp > optimalTempMax) feedback += ` הטמפרטורה גבוהה מדי (${steamTemp}°C), שקול להוריד אותה.`;
                 if (distillationTime < idealTimeMin) feedback += ` זמן הזיקוק קצר מדי (${distillationTime} דק'). נסה להאריך אותו.`;
                 if (distillationTime > idealTimeMax) feedback += ` זמן הזיקוק ארוך מדי (${distillationTime} דק'). נסה לקצר אותו.`;

            } else if (actualOilExtracted < maxPossibleOil * 0.6 && quality >= 3) {
                 feedback = "השמן באיכות טובה, אך הכמות נמוכה. האם הזיקוק היה קצר מדי או שהטמפרטורה לא אפשרה מיצוי מלא?";
                 if (distillationTime < theoreticalFullExtractionTime * 0.9) feedback += ` זמן הזיקוק קצר יחסית לקצב המיצוי. נסה להאריך אותו.`;
                 if (steamTemp < 105) feedback += ` טמפרטורת הקיטור נמוכה יחסית, מה שמאט את המיצוי.`;
            } else if (quality >= 4 && actualOilExtracted < maxPossibleOil * 0.8) {
                 feedback = "השמן באיכות גבוהה, אך הכמות לא מקסימלית. אולי ניתן להאריך מעט את זמן הזיקוק?";
            } else if (quality < 4 && actualOilExtracted > maxPossibleOil * 0.8) {
                 feedback = "קיבלת כמות יפה של שמן, אך האיכות יכולה להשתפר. שים לב לטמפרטורה ולזמן הזיקוק - אולי אחד מהם היה קיצוני מדי?";
                 if (steamTemp > optimalTempMax) feedback += ` טמפרטורת הקיטור גבוהה יחסית.`;
                 if (distillationTime > idealTimeMax) feedback += ` זמן הזיקוק ארוך יחסית לקצב המיצוי.`;
            } else {
                 feedback = "תוצאות טובות! בחינה נוספת של הפרמטרים יכולה להוביל לשיפור.";
            }


            // --- Update Display ---
            simStatusDiv.textContent = 'הזיקוק הסתיים בהצלחה!';
            simStatusDiv.classList.remove('active');

            oilResultSpan.textContent = actualOilExtracted.toFixed(2); // Display with 2 decimal places
            qualityResultSpan.textContent = '⭐'.repeat(quality); // Display stars

            // Update visualization (layers fill smoothly)
            // Total visual height for liquid in receiver is container height
            const liquidContainerHeight = receiverLiquidContainer.clientHeight; // Height excluding label

            // Scale visual oil height based on amount relative to max possible in this sim
            const visualOilHeight = Math.min(actualOilExtracted / maxPossibleOil * liquidContainerHeight * 0.8, liquidContainerHeight * 0.8); // Max 80% fill with oil

            oilLayerDiv.style.height = `${visualOilHeight}px`;
            // Hydrosol fills the rest below the oil
            hydrosolLayerDiv.style.height = `${liquidContainerHeight - visualOilHeight}px`;
             // Add text back after animation
             setTimeout(() => {
                oilLayerDiv.textContent = 'שמן';
                hydrosolLayerDiv.textContent = 'הידרוסול';
             }, 2000); // Add text after layers finish animating


            feedbackMessageDiv.textContent = feedback;
            feedbackMessageDiv.classList.add('visible');


            // Re-enable controls
            runButton.disabled = false;
             document.querySelectorAll('.param-group input').forEach(input => input.disabled = false);

            // Stop animations
            stopAnimations();

        }, actualSimDuration); // Simulation processing time

    });

    // Function to start animations
    function startAnimations(duration) {
        // Boiler steam animation (simple particle system)
        boilerAnimation.innerHTML = ''; // Clear previous particles
        for (let i = 0; i < 30; i++) { // Fewer particles
            const particle = document.createElement('div');
            particle.classList.add('steam-particle');
            // Stagger animation start slightly
            particle.style.animationDelay = `${(i * 0.05)}s`; // Adjust delay for timing
             particle.style.animationDuration = '2s'; // Slower animation
             particle.style.left = `${20 + Math.random() * 60}%`; // Random horizontal position
             particle.style.bottom = `${10 + Math.random() * 20}%`; // Start slightly above bottom liquid
            boilerAnimation.appendChild(particle);
        }

         // Plant vessel vapor animation (similar)
         plantAnimation.innerHTML = '';
         for (let i = 0; i < 30; i++) {
             const particle = document.createElement('div');
             particle.classList.add('vapor-particle');
             particle.style.animationDelay = `${(i * 0.05)}s`;
             particle.style.animationDuration = '2s';
              particle.style.left = `${20 + Math.random() * 60}%`; // Random horizontal position
             particle.style.bottom = `${10 + Math.random() * 20}%`; // Start slightly above bottom
             plantAnimation.appendChild(particle);
         }

        // Condenser drops animation
         condenserAnimation.innerHTML = '';
         for (let i = 0; i < 15; i++) { // Fewer drops
             const particle = document.createElement('div');
             particle.classList.add('drop-particle');
              particle.style.animationDelay = `${(i * 0.1)}s`; // Slower drop rate
              particle.style.animationDuration = '1.5s'; // Slower fall
             particle.style.left = `${30 + Math.random() * 40}%`; // Random horizontal position, more centered
             particle.style.top = `${Math.random() * 10}%`; // Start near the top
             condenserAnimation.appendChild(particle);
         }
    }

    // Function to stop animations
    function stopAnimations() {
        document.querySelectorAll('.animation-element').forEach(el => el.style.animation = 'none');
        // A better way is to remove elements or change display, but removing nodes might be complex with infinite animation
        // Simpler: let the infinite animations finish their current cycle or hide the containers
         boilerAnimation.innerHTML = ''; // Clear particles
         plantAnimation.innerHTML = '';
         condenserAnimation.innerHTML = '';
    }


    // Initial visualization setup (fill hydrosol, oil empty, layers take full height)
     const maxLiquidHeightInit = receiverLiquidContainer ? receiverLiquidContainer.clientHeight : 90; // Fallback if container not measured yet
     if(hydrosolLayerDiv) hydrosolLayerDiv.style.height = `${maxLiquidHeightInit}px`;
     if(oilLayerDiv) oilLayerDiv.style.height = '0'; // Start with no oil
     if(oilLayerDiv) oilLayerDiv.textContent = ''; // Clear text
     if(hydrosolLayerDiv) hydrosolLayerDiv.textContent = 'הידרוסול';


    // Toggle explanation section
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הסבר על זיקוק שמנים אתריים: צלילה לעומק';

         // Scroll to the explanation section if it's revealed
         if (isHidden) {
             explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

     // Initial state of toggle button text
    toggleExplanationButton.textContent = 'הסבר על זיקוק שמנים אתריים: צלילה לעומק';


    // Initial slider value displays
    materialValueSpan.textContent = materialInput.value;
    tempValueSpan.textContent = tempInput.value;
    timeValueSpan.textContent = timeInput.value;

</script>