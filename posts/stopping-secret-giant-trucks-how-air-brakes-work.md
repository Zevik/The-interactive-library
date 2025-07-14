---
title: "סוד העצירה של משאיות ענק: איך עובדים בלמי אוויר?"
english_slug: stopping-secret-giant-trucks-how-air-brakes-work
category: "הנדסת רכב"
tags: [בלמי אוויר, משאית, בלימה, לחץ אוויר, מכניקה]
---
# סוד העצירה של משאיות ענק: איך עובדים בלמי אוויר?

דמיינו משאית ענקית ששוקלת עשרות טונות, דוהר בכביש מהיר. עכשיו דמיינו שהיא צריכה לעצור במהירות ובבטחה. איך מערכת הבלמים שלה עומדת במשימה הבלתי אפשרית הזו? התשובה טמונה במרכיב מפתיע שנמצא בכל מקום סביבנו: אוויר!

בואו נגלה את הקסם שמאפשר למפלצות הכביש האלה לעצור. התנסו בסימולציה הפשוטה למטה ושחקו עם הפרמטרים כדי להבין בעצמכם איך זה עובד, לפני שתצללו להסבר המפורט.

<div class="simulation-container">
    <div class="controls">
        <h3>שחקו עם הבלמים!</h3>
        <div class="control-group">
            <label for="initial-speed">מהירות (קמ"ש):</label>
            <input type="number" id="initial-speed" value="80" min="10" max="120">
        </div>
        <div class="control-group">
            <label for="truck-load">עומס משאית (טון):</label>
            <input type="number" id="truck-load" value="20" min="0" max="40">
        </div>
        <div class="control-group">
            <label for="air-pressure">לחץ אוויר (בר):</label>
            <input type="number" id="air-pressure" value="8" min="1" max="10" step="0.5">
        </div>
        <button id="brake-button" class="action-button">בלום!</button>
    </div>

    <div class="simulation-area">
        <div class="road">
             <div class="road-line left"></div>
             <div class="road-line right"></div>
            <div id="truck" class="truck">
                <span role="img" aria-label="משאית">🚛</span>
            </div>
            <div id="stopping-distance-marker" class="stopping-distance-marker" style="display: none;"></div>
            <div class="distance-label" id="stopping-distance-label"></div>
        </div>
        <div class="air-brake-system">
            <div class="system-title">מערכת בלמי אוויר (פשטני)</div>
            <div class="system-components">
                <div class="air-tank component">מיכל אוויר</div>
                <div class="air-line" id="air-line-1"></div>
                <div class="valve component">שסתום בלם</div>
                 <div class="air-line" id="air-line-2"></div>
                <div class="brake-chamber component">
                    תא בלם
                    <div class="piston"></div>
                </div>
            </div>
        </div>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר הסבר מפורט</button>

<div id="explanation" class="explanation-content" style="display: none;">
    <h2>הסבר מפורט: כך פועלים בלמי אוויר במשאית</h2>

    <h3>למה אוויר? היתרונות על פני בלמים הידראוליים ברכבים כבדים</h3>
    <p>במכוניות פרטיות קטנות יחסית, מערכת הבלימה הנפוצה מסתמכת על לחץ שמועבר דרך נוזל בלמים (מערכת הידראולית). זה עובד היטב למסה קטנה. אבל כשמדובר במשאית ענקית שמשקלה עשרות טונות, הכוח הנדרש לעצירה אדיר. מערכת הידראולית שתספק כוח כזה תהיה יקרה, מגושמת, ורגישה מאוד לדליפות (שאף דליפה קטנה עלולה להשבית את הבלמים לחלוטין!).</p>
    <p>מערכות בלמי אוויר הן הפתרון המועדף לרכבים כבדים. הן משתמשות באוויר דחוס ליצירת כוח עצירה עצום בצורה אמינה ועמידה. במקום נוזל שעלול לדלוף, משתמשים באוויר זמין ואינסופי (פחות או יותר!), וכשל במערכת לרוב מוביל לבלימה אוטומטית (בלמי קפיץ), לא לאובדן בלמים מוחלט.</p>

    <h3>עיקרון הזהב: לחץ אוויר = כוח עצירה אדיר</h3>
    <p>הבסיס פשוט: לחץ האוויר מופעל על שטח גדול יחסית בתוך תא אטום (תא הבלם). הכוח שנוצר (זוכרים פיזיקה? לחץ = כוח חלקי שטח!) מועבר דרך מוט שמפעיל ישירות את מנגנון הבלם בגלגל (תוף או דיסק). ככל שלחץ האוויר גבוה יותר, הכוח גדול יותר, והבלימה חזקה יותר.</p>

    <h3>המערכת בפעולה: מסע האוויר מהמדחס עד לגלגל</h3>
    <ol>
        <li><strong>מדחס אוויר:</strong> יחידה קטנה שמחוברת למנוע. תפקידה לשאוב אוויר מהסביבה ולדחוס אותו ללחץ גבוה.</li>
        <li><strong>מכלי אגירה:</strong> כמו בלונים חזקים במיוחד! אוגרים את האוויר הדחוס בלחץ גבוה (כמו 8-10 בר). זהו מאגר האנרגיה שלכם לבלימה. המדחס ממלא אותם כל הזמן כשהמנוע עובד.</li>
        <li><strong>שסתום דוושת הבלם:</strong> ה"ברז" הראשי. כשהנהג לוחץ על הדוושה, השסתום נפתח ומאפשר לאוויר מהמכלים לזרום לכל מערכת הבלמים. ככל שהלחיצה חזקה יותר, השסתום נפתח יותר והלחץ המגיע לגלגלים גבוה יותר.</li>
        <li><strong>צינורות אוויר:</strong> מעבירים את האוויר בלחץ מהמכלים, דרך שסתום הדוושה, אל תאי הבלם בכל גלגל.</li>
        <li><strong>תאי בלם:</strong> אלו גלילים קטנים שמותקנים ליד כל גלגל. בפנים יש דיאפרגמה גמישה או בוכנה וקפיץ חזק. כשהאוויר הדחוס נכנס לתא, הוא דוחף את הדיאפרגמה/בוכנה נגד כוח הקפיץ. תנועה זו של הבוכנה מפעילה מוט דחיפה.</li>
        <li><strong>מוט דחיפה (Pushrod):</strong> מחובר לבוכנה בתא הבלם. הוא זה שמעביר את הכוח שנוצר מלחץ האוויר אל מנגנון הבלם בגלגל.</li>
        <li><strong>מנגנון הבלם (תוף/דיסק):</strong> בקצה המוט נמצא מנגנון מכני (לרוב זרוע שמסובבת ציר). בבלמי תוף, זה גורם לכפות הבלם להיפתח ולהיצמד לחלק הפנימי של התוף המסתובב עם הגלגל. בבלמי דיסק, זה גורם לרפידות הבלם להיצמד משני הצדדים לדיסק המסתובב. החיכוך שנוצר בין כפות/רפידות לתוף/דיסק הוא כוח הבלימה שעוצר את המשאית.</li>
        <li><strong>שחרור בלם:</strong> כשהנהג מרפה מהדוושה, שסתום הדוושה נסגר, והאוויר מתאי הבלם משתחרר החוצה לאטמוספרה. הקפיץ בתוך תא הבלם מחזיר את הבוכנה למצב המקורי, ומוט הדחיפה משחרר את מנגנון הבלם מהגלגל.</li>
    </ol>

    <h3>בלם חניה וחירום: הקפיץ כגיבור על</h3>
    <p>ומה קורה אם יש דליפת אוויר גדולה או כשהמנוע כבוי? כאן נכנסים לתמונה בלמי החניה/חירום. בניגוד לבלמי השירות הרגילים שפועלים כשיש לחץ אוויר, בלמי החניה פועלים *כשאין* לחץ אוויר! בתאי בלמי החניה (לרוב בסרנים האחוריים), יש קפיץ אדיר שדרוך כל עוד יש לחץ אוויר במערכת (האוויר שומר עליו מכווץ). אם לחץ האוויר יורד מתחת לסף בטיחותי (בין אם הנהג מפעיל את בלם החניה ומרוקן את האוויר מהתאים הללו, או במקרה של כשל/דליפה), הקפיץ משתחרר בדרמטיות ודוחף את הבוכנה *באופן מכני* ומפעיל את הבלם. זהו מנגנון בטיחות גאוני שמבטיח שהמשאית תבלם אוטומטית במקרה חירום ולא תתגלגל ללא שליטה.</p>

    <h3>סיכום: יתרונות מול אתגרים</h3>
    <ul>
        <li><strong>יתרונות:</strong> כוח עצירה עצום, אמינות גבוהה, שימוש במשאב זמין (אוויר), מערכת בלימת חירום מובנית (בלמי קפיץ), קלות חיבור נגררים.</li>
        <li><strong>אתגרים:</strong> זמן תגובה מעט ארוך יותר מהידראוליים (האוויר דחיס ולוקח לו זמן לזרום), דורש ניקוז לחות (למנוע קפיאה/קורוזיה), מורכבות טכנית, דורש זמן ראשוני למילוי מכלי האוויר.</li>
    </ul>
    <p>אז בפעם הבאה שתראו משאית ענקית עוצרת כאילו בקסם, תזכרו שזה לא קסם, זו הנדסה חכמה שמנצלת את הכוח האדיר של אוויר דחוס!</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #28a745;
        --accent-color: #ffc107;
        --text-color: #333;
        --bg-color: #f8f9fa;
        --card-bg: #ffffff;
        --border-color: #dee2e6;
        --road-color: #555;
        --truck-color: #dc3545;
        --air-color-inactive: #adb5bd;
        --air-color-active: #007bff; /* Matches primary color */
        --system-component-bg: #e9ecef;
        --system-component-border: #ced4da;
    }

    .simulation-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        text-align: right;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* Increased gap */
        padding: 25px; /* Increased padding */
        border: 1px solid var(--border-color);
        border-radius: 12px; /* More rounded corners */
        background-color: var(--bg-color);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Added shadow */
    }

    .controls {
        background-color: var(--card-bg);
        padding: 20px; /* Increased padding */
        border-radius: 10px; /* More rounded corners */
        display: flex;
        flex-direction: column;
        gap: 15px; /* Increased gap */
        width: 100%;
        max-width: 450px; /* Slightly wider */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .controls h3 {
        margin-top: 0;
        text-align: center;
        color: var(--primary-color);
        font-size: 1.4em;
        margin-bottom: 15px;
    }

    .control-group {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 10px;
        border-bottom: 1px dashed var(--border-color); /* Separator */
    }

    .control-group:last-child {
         border-bottom: none;
         padding-bottom: 0;
    }


    .controls label {
        flex-grow: 1;
        margin-left: 15px; /* More space */
        font-weight: bold;
        color: var(--text-color);
    }

    .controls input[type="number"] {
        width: 90px; /* Slightly wider input */
        padding: 8px; /* More padding */
        border: 1px solid var(--border-color);
        border-radius: 6px; /* More rounded */
        text-align: center;
        -moz-appearance: textfield; /* Remove default number arrows */
        appearance: textfield;
    }

     .controls input::-webkit-outer-spin-button,
     .controls input::-webkit-inner-spin-button {
         -webkit-appearance: none;
         margin: 0;
     }


    .action-button {
        padding: 12px 25px; /* More padding */
        background-color: var(--secondary-color); /* Green color */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em; /* Slightly larger font */
        margin-top: 15px; /* More space above */
        transition: background-color 0.3s ease, transform 0.1s ease;
        width: 100%; /* Full width */
        font-weight: bold;
    }

    .action-button:hover:not(:disabled) {
        background-color: #218838; /* Darker green on hover */
        transform: translateY(-1px); /* Subtle lift */
    }

    .action-button:active:not(:disabled) {
         background-color: #1e7e34;
         transform: translateY(0);
    }

     .action-button:disabled {
         background-color: var(--air-color-inactive);
         cursor: not-allowed;
     }


    .simulation-area {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* Increased gap */
        max-width: 800px; /* Max width for simulation */
    }

    .road {
        position: relative;
        width: 100%;
        height: 100px; /* Increased height */
        background: linear-gradient(to bottom, var(--road-color), darken(var(--road-color), 10%)); /* Gradient asphalt */
        overflow: hidden; /* Hide overflow during animation */
        border-radius: 8px;
        box-shadow: inset 0 -3px 6px rgba(0, 0, 0, 0.2);
    }

     .road-line {
         position: absolute;
         width: 5px; /* Line thickness */
         top: 0;
         bottom: 0;
         background-color: var(--accent-color); /* Yellow lines */
     }
     .road-line.left { left: 10%; } /* Starting point */
     .road-line.right { right: 10%; } /* Placeholder for perspective? Or just use one dashed center line */

      /* Let's use a dashed center line for simplicity and animation */
     .road::after {
         content: '';
         position: absolute;
         top: 50%;
         left: 0;
         right: 0;
         height: 4px;
         background: repeating-linear-gradient(to right, var(--accent-color) 0, var(--accent-color) 15px, transparent 15px, transparent 30px); /* Dashed line */
         transform: translateY(-50%);
          animation: road-scroll 3s linear infinite; /* Animation for movement */
     }

     @keyframes road-scroll {
         from { background-position: 0% 0; }
         to { background-position: 100% 0; }
     }


    .truck {
        position: absolute;
        left: 5%; /* Starting position */
        bottom: 15px; /* Position above the road */
        width: 120px; /* Larger truck */
        height: 60px; /* Larger truck */
        font-size: 50px; /* Emoji size */
        display: flex;
        align-items: center;
        justify-content: center;
        transition: left 3s ease-out; /* Animation for braking */
        z-index: 2; /* Above road lines */
         text-shadow: 2px 2px 5px rgba(0,0,0,0.2); /* Subtle shadow for emoji */
    }

    .truck.braking {
        /* Add subtle braking animation */
        animation: truck-brake 0.3s ease-in-out infinite alternate; /* Jitter/shake slightly */
    }

     @keyframes truck-brake {
         0% { transform: translateX(0) translateY(0); }
         50% { transform: translateX(1px) translateY(-0.5px); }
         100% { transform: translateX(-1px) translateY(0.5px); }
     }

     .truck.stopped {
         animation: none; /* Stop braking animation when fully stopped */
     }


    .stopping-distance-marker {
        position: absolute;
        left: 5%; /* Will be updated by JS */
        bottom: 0;
        height: 100%; /* Full height of road */
        width: 4px; /* Thicker marker */
        background-color: var(--truck-color); /* Red color */
        z-index: 1;
         box-shadow: 0 0 8px rgba(220, 53, 69, 0.8); /* Glowing effect */
    }

    .distance-label {
        position: absolute;
        left: 5%; /* Will be updated by JS */
        bottom: calc(100% + 10px); /* Position above the road */
        transform: translateX(-50%);
        font-size: 1em; /* Larger font */
        color: var(--text-color);
        white-space: nowrap;
        background-color: var(--accent-color);
        padding: 5px 10px;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        font-weight: bold;
         min-width: 150px; /* Ensure minimum width */
         text-align: center;
    }


    .air-brake-system {
        width: 100%;
        max-width: 600px; /* Wider system diagram */
        border: 2px dashed var(--border-color); /* More prominent border */
        padding: 20px; /* More padding */
        border-radius: 12px; /* More rounded */
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px; /* Increased gap */
        background-color: var(--card-bg);
        font-size: 1em; /* Larger font */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .system-title {
        font-weight: bold;
        font-size: 1.2em;
        color: var(--primary-color);
        margin-bottom: 10px;
    }

    .system-components {
         display: flex;
         align-items: center;
         justify-content: center;
         gap: 10px; /* Gap between components */
         width: 100%;
         flex-wrap: wrap; /* Allow wrapping if needed */
    }


    .component {
        padding: 10px 15px; /* More padding */
        border: 2px solid var(--system-component-border); /* Thicker border */
        border-radius: 6px; /* More rounded */
        background-color: var(--system-component-bg);
        text-align: center;
        font-size: 0.9em;
         min-width: 80px; /* Minimum width */
         box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    }

    .air-tank { border-color: #0056b3; background-color: #cceeff; } /* Specific color for tank */
    .valve { border-color: #0056b3; background-color: #e9ecef; }
    .brake-chamber {
         border-color: #dc3545; /* Red border for brake part */
         background-color: #f8d7da; /* Light red background */
         position: relative; /* For piston animation */
         overflow: hidden; /* Keep piston inside */
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
         transition: background-color 0.4s ease;
    }

     .brake-chamber.activated {
         background-color: #dc3545; /* Darker red when active */
         color: white;
     }

     .piston {
         width: 80%; /* Width relative to chamber */
         height: 8px;
         background-color: #343a40; /* Dark piston */
         position: absolute;
         bottom: 5px; /* Start at one end */
         left: 10%;
         border-radius: 4px;
         transition: transform 0.4s ease-out; /* Animation for movement */
     }

     .brake-chamber.activated .piston {
         transform: translateX(40%); /* Move piston to the other end (adjust value based on visual) */
     }


    .air-line {
        width: 4px; /* Thicker lines */
        height: 30px; /* Longer lines */
        background-color: var(--air-color-inactive);
        transition: background-color 0.4s ease; /* Animation for air flow */
         border-radius: 2px; /* Rounded ends */
         flex-shrink: 0; /* Don't shrink */
         position: relative;
    }

     .air-line.flow {
        background-color: var(--air-color-active); /* Blue when flowing */
         box-shadow: 0 0 8px var(--air-color-active); /* Glowing effect */
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More margin */
        padding: 12px 25px; /* More padding */
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        transition: background-color 0.3s ease, transform 0.1s ease;
         font-weight: bold;
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
         transform: translateY(-1px);
    }
     #toggle-explanation:active {
         background-color: #004085;
          transform: translateY(0);
     }

    .explanation-content {
        direction: rtl;
        text-align: right;
        padding: 25px; /* More padding */
        border: 1px solid var(--border-color);
        border-radius: 12px; /* More rounded */
        background-color: var(--card-bg);
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        line-height: 1.7; /* Improved readability */
         color: var(--text-color);
    }

    .explanation-content h2, .explanation-content h3 {
        color: var(--primary-color);
        border-bottom: 2px solid var(--border-color); /* Thicker separator */
        padding-bottom: 8px; /* More padding */
        margin-top: 30px; /* More space above headings */
         margin-bottom: 15px;
    }
     .explanation-content h2 { font-size: 1.8em; }
     .explanation-content h3 { font-size: 1.4em; color: var(--secondary-color); }


    .explanation-content ul, .explanation-content ol {
        margin-right: 25px; /* More indentation */
        padding-right: 0; /* Reset padding */
    }

    .explanation-content li {
        margin-bottom: 12px; /* More space between list items */
    }

    /* Styling for code snippets within explanation (if any) */
    .explanation-content code {
        background-color: #e9ecef;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const initialSpeedInput = document.getElementById('initial-speed');
        const truckLoadInput = document.getElementById('truck-load');
        const airPressureInput = document.getElementById('air-pressure');
        const brakeButton = document.getElementById('brake-button');
        const truck = document.getElementById('truck');
        const stoppingDistanceMarker = document.getElementById('stopping-distance-marker');
        const stoppingDistanceLabel = document.getElementById('stopping-distance-label');
        const airLine1 = document.getElementById('air-line-1');
        const airLine2 = document.getElementById('air-line-2');
        const brakeChamber = document.querySelector('.brake-chamber'); // Select the brake chamber element
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
         const roadElement = document.querySelector('.road');
         const roadLine = document.querySelector('.road::after'); // Select the road line pseudo-element

        // --- Simulation Logic ---
        const baseTruckMass = 20000; // kg (20 tons)
        const pistonArea = 0.025; // Increased simplified piston area in m^2 for better braking force range
        const pressureToPascal = 100000; // 1 Bar = 100,000 Pascal (N/m^2)
        const assumedAxles = 4; // Assume 4 axles braking
        const initialTruckLeftPercent = 5; // Initial position in %
        let roadWidthPixels = 0; // Will be updated on load and resize

        // Function to update road width in pixels
        function updateRoadWidth() {
             if (roadElement) {
                 roadWidthPixels = roadElement.offsetWidth;
             }
             // Also adjust truck position if needed based on new road width - not strictly necessary with %
        }

        // Update road width on load and resize
        updateRoadWidth();
        window.addEventListener('resize', updateRoadWidth);


        function calculateStoppingDistance(initialSpeedKmh, truckLoadTon, airPressureBar) {
            const initialSpeedMs = initialSpeedKmh / 3.6; // Convert km/h to m/s
            const totalMassKg = baseTruckMass + (truckLoadTon * 1000); // Convert tons to kg

            // Calculate braking force based on air pressure and assumed axles
            // F = Pressure * Area * NumAxles * Coefficient (add a coefficient for realism, e.g., 0.8)
            const brakingForce = airPressureBar * pressureToPascal * pistonArea * assumedAxles * 0.8; // Added efficiency coefficient

            // Calculate deceleration (a = F / m). Deceleration is negative, but we use positive magnitude for calculation.
            const decelerationMagnitude = brakingForce / totalMassKg;

            // Add a small rolling resistance/air drag force component (simplified)
            // This prevents infinite stopping distance at zero pressure but keeps focus on air brake
             const rollingResistanceForce = totalMassKg * 9.81 * 0.01; // Simplified: mass * g * rolling_coeff (e.g., 0.01)
             const effectiveDecelerationMagnitude = (brakingForce - rollingResistanceForce) / totalMassKg;


            // Calculate stopping distance (v^2 = u^2 + 2as => s = (v^2 - u^2) / (2a))
            // v = 0 (final speed)
            // u = initialSpeedMs
            // a = -effectiveDecelerationMagnitude (because it's stopping)
            let stoppingDistanceMeters;
             if (effectiveDecelerationMagnitude <= 0.1 || initialSpeedMs <= 0) { // Handle cases with very low or zero deceleration/speed
                 stoppingDistanceMeters = Infinity; // Truck barely stops or doesn't stop
             } else {
                stoppingDistanceMeters = (initialSpeedMs * initialSpeedMs) / (2 * effectiveDecelerationMagnitude);
             }

            return stoppingDistanceMeters; // Distance in meters
        }

        function startSimulation() {
            const initialSpeed = parseFloat(initialSpeedInput.value);
            const truckLoad = parseFloat(truckLoadInput.value);
            const airPressure = parseFloat(airPressureInput.value);

            // Basic validation
            if (isNaN(initialSpeed) || isNaN(truckLoad) || isNaN(airPressure) ||
                initialSpeed < parseFloat(initialSpeedInput.min) || initialSpeed > parseFloat(initialSpeedInput.max) ||
                truckLoad < parseFloat(truckLoadInput.min) || truckLoad > parseFloat(truckLoadInput.max) ||
                airPressure < parseFloat(airPressureInput.min) || airPressure > parseFloat(airPressureInput.max) ) {
                 alert('אנא הכנס ערכים תקינים בטווח המותר.');
                 return;
             }

            // Disable button and inputs during simulation
            brakeButton.disabled = true;
            initialSpeedInput.disabled = true;
            truckLoadInput.disabled = true;
            airPressureInput.disabled = true;


            // Reset visual states immediately
            truck.style.transition = 'none'; // Reset transition for repositioning
            truck.style.left = initialTruckLeftPercent + '%'; // Reset truck position
            stoppingDistanceMarker.style.display = 'none'; // Hide previous marker
            stoppingDistanceLabel.textContent = ''; // Clear previous label
            truck.classList.remove('braking', 'stopped'); // Remove braking/stopped classes
             airLine1.classList.remove('flow');
             airLine2.classList.remove('flow');
             brakeChamber.classList.remove('activated');
             truck.querySelector('span').textContent = '🚛'; // Reset truck emoji


            // --- Start Animations ---

            // Animate air flow and brake chamber activation first
            requestAnimationFrame(() => {
                 airLine1.classList.add('flow');
                 airLine2.classList.add('flow');
                 brakeChamber.classList.add('activated');
                 truck.classList.add('braking'); // Start truck braking animation
            });

            // Calculate stopping distance
            const stoppingDistanceMeters = calculateStoppingDistance(initialSpeed, truckLoad, airPressure);

            // Scaling distance for visualization.
            // Assume the visible road width represents a certain maximum distance we *can* show, e.g., 300m
            // If distance is > max, truck goes off screen or shows 'does not stop'.
            const maxVisualDistance = 400; // meters represented by the majority of the road width beyond the start
            const availableRoadWidthPercent = 100 - initialTruckLeftPercent;
            const stoppingDistanceVisualPercent = (stoppingDistanceMeters / maxVisualDistance) * availableRoadWidthPercent;

            // Determine final visual position and animation duration
            let finalLeftPercent;
            let animationDurationSeconds;
            let displayDistanceText = '';
            let truckEmoji = '🚛';

             if (stoppingDistanceMeters === Infinity || stoppingDistanceMeters > maxVisualDistance * 1.5) {
                 // Truck doesn't stop or stops very far away - animate it going off screen slowly
                 finalLeftPercent = 110; // Move off screen
                 animationDurationSeconds = 5; // Long animation time
                 displayDistanceText = 'לא עוצר!';
                 truckEmoji = '😩';
             } else {
                 // Truck stops within or near the visual area
                 finalLeftPercent = initialTruckLeftPercent + stoppingDistanceVisualPercent;
                 // Ensure truck doesn't go beyond the end of the visual road area (allow a little space)
                 finalLeftPercent = Math.min(finalLeftPercent, 95);
                 // Determine animation duration based on distance and speed (make it feel right)
                 // Duration should be proportional to distance and inversely related to deceleration (or proportional to initial speed / deceleration)
                 const effectiveDecel = (stoppingDistanceMeters > 0) ? (initialSpeed / 3.6 * initialSpeed / 3.6) / (2 * stoppingDistanceMeters) : Infinity;
                 animationDurationSeconds = (effectiveDecel > 0.1) ? Math.max(1, Math.min(6, (initialSpeed / 3.6) / effectiveDecel)) : 6; // Clamp duration


                 displayDistanceText = `עוצר לאחר כ: ${stoppingDistanceMeters.toFixed(1)} מטר`;
                 truckEmoji = '🚛'; // Default happy truck
             }


            // Set the final position and start the truck animation
            requestAnimationFrame(() => {
                 // Set truck transition before changing position
                 truck.style.transition = `left ${animationDurationSeconds}s cubic-bezier(0.25, 0.46, 0.45, 0.94)`; /* Ease-out or similar curve */
                 truck.style.left = finalLeftPercent + '%';

                 // Animate road scrolling speed inversely proportional to braking
                  // Needs a more sophisticated JS animation loop or keyframes based on time
                  // For simplicity, let's control CSS animation speed.
                  // This is tricky with pure CSS animation triggered from JS based on dynamic duration.
                  // Let's skip dynamic road scroll speed for now, or use a fixed speed for 'moving' vs 'stopped'.
                   // The current road scroll is infinite and doesn't react to braking, which is a limitation of CSS background animation.

                 // Position marker and label
                 // Position marker at the calculated final position percentage relative to the *whole* road
                  const markerLeftPercent = initialTruckLeftPercent + (stoppingDistanceMeters / maxVisualDistance) * availableRoadWidthPercent;

                 // Clamp marker visually to not exceed road width
                 const visualMarkerLeftPercent = Math.min(markerLeftPercent, 98); // Max position 98%

                 stoppingDistanceMarker.style.left = visualMarkerLeftPercent + '%';

                 // Wait for the truck animation to finish to show marker/label and update emoji
                 setTimeout(() => {
                     stoppingDistanceMarker.style.display = 'block';
                     stoppingDistanceLabel.textContent = displayDistanceText;
                      truck.querySelector('span').textContent = truckEmoji; // Update emoji based on outcome
                      truck.classList.add('stopped'); // Add stopped class to remove braking animation

                     // Position label relative to marker, checking boundaries
                     const markerPosPx = (visualMarkerLeftPercent / 100) * roadWidthPixels;
                     const labelWidthPx = stoppingDistanceLabel.offsetWidth;
                     let labelLeftPx = markerPosPx;

                     // Adjust if label overflows right edge
                     if (labelLeftPx + labelWidthPx / 2 > roadWidthPixels - 10) { // 10px padding
                         labelLeftPx = roadWidthPixels - labelWidthPx - 10;
                     }
                      // Adjust if label is too close to the start position
                      const truckStartPosPx = (initialTruckLeftPercent / 100) * roadWidthPixels;
                     if (labelLeftPx - labelWidthPx / 2 < truckStartPosPx + truck.offsetWidth * 0.6) { // Place label after truck start
                         labelLeftPx = truckStartPosPx + truck.offsetWidth * 0.6;
                     }


                     stoppingDistanceLabel.style.left = (labelLeftPx / roadWidthPixels) * 100 + '%';
                     stoppingDistanceLabel.style.transform = 'translateX(-50%)'; // Keep centered relative to calculated spot


                     // Reset air flow and brake chamber animation after truck stops
                     airLine1.classList.remove('flow');
                     airLine2.classList.remove('flow');
                     brakeChamber.classList.remove('activated');

                     // Re-enable button and inputs
                     brakeButton.disabled = false;
                     initialSpeedInput.disabled = false;
                     truckLoadInput.disabled = false;
                     airPressureInput.disabled = false;

                 }, animationDurationSeconds * 1000 + 100); // Add a small buffer


            });
        }

        brakeButton.addEventListener('click', startSimulation);

        // --- Explanation Toggle Logic ---
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג/הסתר הסבר מפורט';
        });

         // Set initial truck emoji
        truck.querySelector('span').textContent = '🚛';

        // Optional: Run simulation once on load with default values? No, let user initiate.
        // startSimulation();

    });
</script>
```