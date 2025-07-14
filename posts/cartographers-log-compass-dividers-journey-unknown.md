---
title: "יומן קרטוגרף: מצפן, פרגול ומסע אל הלא-נודע"
english_slug: cartographers-log-compass-dividers-journey-unknown
category: "ארכאולוגיה"
tags: ["קרטוגרפיה", "היסטוריה", "עידן התגליות", "מפות", "סימולציה", "מסע"]
---
# יומן קרטוגרף: מצפן, פרגול ומסע אל הלא-נודע

דמיינו את עצמכם עומדים על סיפון ספינת עץ חורקת, מוקפים בים אינסופי. אין לכם מפה מלאה, אין לוויינים מעליכם. רק מכשירים עתיקים, פיסות מידע שנאספו בקושי, ואומץ רב. איך יוצרים מפה בעולם כזה? מי היו האנשים שרשמו את קווי המתאר הראשונים של יבשות חדשות, ועם אילו חידות גיאוגרפיות הם התמודדו? הצטרפו למסע דמיוני קצר ונסו לחוות את עבודתם המדהימה של הקרטוגרפים של עידן התגליות.

<div id="cartographer-app">
    <div class="app-container">
        <div id="map-area">
            <canvas id="cartographer-canvas"></canvas>
            <div id="ship-marker" class="marker">⛵</div> <!-- Changed emoji for feel -->
            <div id="start-marker" class="marker start-marker">⚓</div> <!-- Changed emoji for feel -->
             <div id="compass-rose" class="map-overlay"></div> <!-- Added compass rose element -->
        </div>
        <div id="data-panel">
            <h3>יומן המסע:</h3>
            <div id="data-points">
                <!-- Data points will be loaded here by JS -->
                <p class="log-entry">מתחילים את המסע מנמל מוכר... הים רגוע. נשמח לכל פיסת מידע חדשה.</p>
            </div>
            <button id="next-data-btn" class="app-button primary">נתון המסע הבא</button> <!-- Added class -->
        </div>
    </div>
    <div id="simulation-controls">
        <p id="current-instruction"></p>
        <button id="apply-data-btn" class="app-button secondary" style="display: none;">החל נתונים על מפת השירטוט</button> <!-- Added class -->
        <p id="simulation-notes"></p>
    </div>
</div>

<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Lora:ital,wght@0,400..700;1แต600;1,400..700&display=swap');

    #cartographer-app {
        font-family: 'Lora', serif; /* More classic font */
        direction: rtl;
        text-align: right;
        padding: 30px; /* Increased padding */
        background: linear-gradient(to bottom, #f0e6d1, #e0d6c1); /* Parchment gradient */
        border-radius: 12px; /* More rounded corners */
        max-width: 950px; /* Increased max width */
        margin: 30px auto; /* Increased margin */
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2); /* Deeper shadow */
        border: 1px solid #d0c0b0; /* Border to define parchment edge */
    }

    h1 {
        font-family: 'Cinzel Decorative', cursive;
        text-align: center;
        color: #4a3b2d; /* Dark brown */
        margin-bottom: 25px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    p {
        color: #5c4b3b; /* Slightly lighter brown */
        line-height: 1.7;
    }

    .app-container {
        display: flex;
        flex-wrap: wrap-reverse; /* Data panel first on smaller screens */
        gap: 30px; /* Increased gap */
    }

    #map-area {
        flex: 3; /* Map takes more space */
        min-width: 350px; /* Increased min width */
        background: #a8dadc; /* Softer sea blue */
        /* background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><circle cx="50" cy="50" r="45" fill="none" stroke="%23457b9d" stroke-width="2"/><line x1="50" y1="5" x2="50" y2="95" stroke="%23457b9d" stroke-width="1"/><line x1="5" y1="50" x2="95" y2="50" stroke="%23457b9d" stroke-width="1"/><circle cx="50" cy="50" r="10" fill="%23457b9d"/></svg>'); /* Subtle compass rose pattern */ */
        /* Using inline SVG for compass rose element instead */
        border: 2px solid #457b9d; /* Darker sea border */
        position: relative;
        overflow: hidden;
        border-radius: 6px; /* Slightly rounded */
        aspect-ratio: 1.6 / 1; /* Slightly wider aspect ratio */
        max-width: 650px; /* Increased max width */
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1); /* Inner shadow for depth */
    }

     #compass-rose {
        position: absolute;
        top: 15px;
        left: 15px;
        width: 60px;
        height: 60px;
        background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="none" stroke="%23457b9d" stroke-width="3"/><path d="M50 2v18 M50 98v-18 M2 50h18 M98 50h-18" stroke="%23457b9d" stroke-width="2" vector-effect="non-scaling-stroke"/><path d="M50 2 L55 15 L50 10 L45 15 Z M50 98 L55 85 L50 90 L45 85 Z M2 50 L15 45 L10 50 L15 55 Z M98 50 L85 45 L90 50 L85 55 Z" fill="%23457b9d"/><path d="M50 2 L60 80 L50 98 L40 80 Z" fill="%23e63946"/><path d="M2 50 L80 60 L98 50 L80 40 Z" fill="%23e63946"/><circle cx="50" cy="50" r="8" fill="%23457b9d"/></svg>');
        background-size: contain;
        opacity: 0.7; /* Slightly transparent */
        z-index: 5;
     }

    #cartographer-canvas {
        display: block;
        width: 100%;
        height: 100%;
        position: relative; /* Needed for z-index */
        z-index: 2; /* Below markers */
    }

    .marker {
        position: absolute;
        transform: translate(-50%, -50%);
        font-size: 28px; /* Larger markers */
        z-index: 10;
        pointer-events: none;
        filter: drop-shadow(0 0 3px rgba(255,255,255,0.8)); /* Better shadow */
        transition: left 1s ease-in-out, top 1s ease-in-out; /* Smooth movement */
    }

    #ship-marker {
         color: #343a40; /* Darker color */
         animation: pulse 1.5s infinite; /* Add pulse animation */
    }

    @keyframes pulse {
        0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
        50% { transform: translate(-50%, -50%) scale(1.1); opacity: 0.9; }
        100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
    }


    .start-marker {
        color: #28a745; /* Nice green */
    }

    #data-panel {
        flex: 1;
        min-width: 300px; /* Increased min width */
        background-color: #fff;
        padding: 20px; /* Increased padding */
        border: 1px solid #ccc;
        border-radius: 8px; /* More rounded corners */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        max-height: 400px; /* Fixed height with scroll */
        overflow-y: auto;
        display: flex;
        flex-direction: column;
    }

     #data-panel h3 {
         font-family: 'Cinzel Decorative', cursive;
         color: #4a3b2d;
         margin-top: 0;
         margin-bottom: 15px;
         border-bottom: 2px solid #eee;
         padding-bottom: 10px;
     }

    #data-points {
        flex-grow: 1; /* Allows it to take up space */
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 1px solid #eee;
    }

    .log-entry { /* Styled data points */
        margin: 10px 0;
        padding: 12px; /* Increased padding */
        background-color: #f9f7f5; /* Off-white */
        border-right: 4px solid #a8dadc; /* Thematic border color */
        font-size: 0.95em;
        border-radius: 4px;
        transition: background-color 0.3s ease;
    }

     .log-entry:last-child {
         border-right-color: #e63946; /* Highlight latest entry */
     }


    #simulation-controls {
        text-align: center;
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px dashed #ccc; /* Separator */
    }

    #current-instruction {
        font-weight: bold;
        color: #4a3b2d; /* Dark brown */
        min-height: 30px; /* More space */
        margin-bottom: 10px;
    }

    #simulation-notes {
        color: #5c4b3b; /* Slightly lighter brown */
        font-style: italic;
        font-size: 0.9em;
        min-height: 20px; /* Reserve space */
    }

     /* Button Styles */
    .app-button {
        display: block;
        width: 100%;
        padding: 12px; /* Increased padding */
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em;
        font-family: 'Lora', serif;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
        margin-bottom: 10px; /* Space between buttons if multiple */
    }

    .app-button:hover {
        transform: translateY(-2px); /* Slight lift effect */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

     .app-button:active {
         transform: translateY(0); /* Press effect */
         box-shadow: none;
     }

    .app-button.primary {
        background-color: #457b9d; /* Sea blue */
        color: white;
    }

    .app-button.primary:hover {
        background-color: #316585;
    }

    .app-button.secondary {
         background-color: #e63946; /* Red/landish color */
         color: white;
    }

     .app-button.secondary:hover {
         background-color: #d02c3b;
     }


    .app-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
        opacity: 0.7;
    }


    /* Styles for Explanation Section */
    #explanation-button {
        display: block;
        width: 250px; /* Wider button */
        margin: 30px auto; /* More margin */
        padding: 12px 15px; /* Increased padding */
        background-color: #28a745; /* Green */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em;
        font-family: 'Lora', serif;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
    }

    #explanation-button:hover {
        background-color: #218838;
         transform: translateY(-2px); /* Slight lift effect */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

     #explanation-button:active {
         transform: translateY(0);
         box-shadow: none;
     }

    #explanation-content {
        margin-top: 30px; /* More margin */
        padding: 25px; /* Increased padding */
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 8px; /* More rounded */
        display: none; /* Initially hidden */
        text-align: right;
        direction: rtl;
        line-height: 1.7; /* Increased line height */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    #explanation-content h2 {
        font-family: 'Cinzel Decorative', cursive;
        color: #4a3b2d;
        margin-bottom: 15px;
        border-bottom: 2px solid #eee;
        padding-bottom: 8px;
    }

    #explanation-content h3 {
        font-family: 'Lora', serif; /* Use Lora for subheadings */
        color: #457b9d; /* Sea blue color */
        margin-top: 20px; /* Increased margin */
        margin-bottom: 10px;
        border-bottom: 1px dashed #eee; /* Dashed border */
        padding-bottom: 5px;
    }

     #explanation-content ul {
         margin-bottom: 15px;
     }

     #explanation-content li {
         margin-bottom: 8px;
     }


    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .app-container {
            flex-direction: column; /* Stack elements */
        }
        #map-area, #data-panel {
            min-width: unset; /* Remove min-width on smaller screens */
            width: 100%; /* Take full width */
            flex: none; /* Remove flex grow */
        }
         #cartographer-app {
             padding: 15px; /* Reduce padding */
         }
         #explanation-button {
             width: 100%; /* Full width button */
         }
    }
</style>

<button id="explanation-button">הצג הסבר מורחב על אתגרי הקרטוגרפיה</button> <!-- More descriptive text -->

<div id="explanation-content">
    <h2>עולמו של הקרטוגרף בעידן התגליות: יומן מסע מדעי</h2>

    <p>בעידן שבו גבולות העולם התרחבו בקצב מסחרר, עבודת הקרטוגרף הייתה קריטית ומלאת אתגרים. הם לא רק שירטטו קווים על נייר; הם תרגמו את הלא-נודע לידע, את הסכנה לנתיב, ואת השמועות למציאות (או לפחות ניסו). כל מפה חדשה הייתה קפיצת דרך אדירה עבור ספנים, סוחרים ומעצמות אירופה המתחרות.</p>

    <h3>מכשירי הקרטוגרף: עיניים למרחקים</h3>
    <p>הכלים שעמדו לרשותם היו פרי ההתקדמות המדעית של התקופה, אך רחוקים משלמות:</p>
    <ul>
        <li><strong>אצטרולב/סקסטנט:</strong> הכוכבים והשמש היו המצפן העיקרי לגובה. מדידת גובהם מעל האופק (בעיקר בצהרי היום או בזריחה/שקיעה) איפשרה חישוב יחסית מדויק של קו הרוחב. קו הרוחב היה לרוב הנתון הגיאוגרפי האמין ביותר במפה.</li>
        <li><strong>מצפן ימי:</strong> הכלי הבסיסי ביותר לשמירה על כיוון. אך הוא הצביע על הצפון המגנטי, לא הגיאוגרפי, והיה צריך לתקן את הנטייה הזו. גם ברזל בספינה יכול היה לשבש את פעולתו.</li>
        <li><strong>מד לוג (Log and Line) ושעון חול:</strong> שיטה פשוטה להערכת מהירות הספינה (מכאן המושג "קשר"). לוח עץ (ה"לוג") הושלך למים, חוט עם קשרים במרחקים קבועים התלפף אחריו, וספירת הקשרים שעברו ביד תוך זמן מדוד בשעון חול נתנה אומדן מהירות. שילוב מהירות (מד לוג) וכיוון (מצפן) איפשר לחשב את המיקום היחסי - שיטת "דרך מנוחה" (Dead Reckoning). זו הייתה השיטה העיקרית לניווט יחסי, אך צברה טעויות בקלות בגלל זרמים, רוחות ומדידה לא מדויקת.</li>
        <li><strong>פרגול וסרגל:</strong> הכלים של השרטט. שימשו למדידת מרחקים על המפה, תרגום סקאלות, ושרטוט קווים וצורות גיאומטריות. קריטיים להעברת הנתונים הגולמיים לייצוג ויזואלי.</li>
    </ul>

    <h3>מקורות המידע: פסיפס של אמת ושמועה</h3>
    <p>מפות נוצרו מאוסף של נתונים שהגיעו ממקורות מגוונים, לא תמיד עקביים:</p>
    <ul>
        <li><strong>יומני ספינה ותצפיות ימאים:</strong> הדיווחים הישירים מהשטח - כיווני שייט, הערכות מרחק, תצפיות על קו חוף, איים, סכנות ניווט. זה היה הבסיס העיקרי למפות הפורטולניות (מפות חוף) שקדמו לעידן זה והתפתחו במהלכו.</li>
        <li><strong>מדידות אסטרונומיות:</strong> בעיקר קו הרוחב. נתון "עוגן" יחסית אמין במפת הנתונים הלא ודאיים.</li>
        <li><strong>ראיונות עם תושבים מקומיים:</strong> לעיתים מקור למידע בעל ערך על פנים הארץ או קווי חוף בלתי מוכרים, אך לעיתים גם מקור לאגדות וסיפורים שהשתלבו במפות (כמו מפלצות ימיות).</li>
        <li><strong>מפות קודמות ותיאורים עתיקים:</strong> ידע שהצטבר לאורך הדורות, לעיתים מדויק ולעיתים מוטעה לחלוטין.</li>
    </ul>

    <h3>האתגר הגדול: קביעת קו אורך</h3>
    <p>בעוד שקביעת קו רוחב הייתה אפשרית יחסית, קו האורך היה חידה כמעט בלתי פתירה במשך רוב עידן התגליות. קו האורך דורש השוואת השעה המקומית (שנקבעה לפי השמש) לשעה מדויקת בנקודת ייחוס כלשהי (למשל, הנמל ממנו יצאת). בלב ים, ללא שעון מדויק שלא מושפע מתנועת הספינה ולחות, זה היה כמעט בלתי אפשרי. טעויות עצומות בחישוב קו האורך היו נפוצות, והובילו לעיוותים משמעותיים בצורת היבשות על המפות ולעיתים קרובות לאסונות ימיים.</p>
    <p>אתגר נוסף היה התרגום של כדור הארץ העגול למפה שטוחה (היטלים), שכל אחד מהם יצר עיוותים שונים אך הכרחיים למטרות ניווט או הצגה.</p>

    <h3>מורשת המפות: צורה חדשה לעולם</h3>
    <p>על אף הקשיים, המפות של עידן התגליות שינו את העולם. הן היו חיוניות לניווט במסעות חציית אוקיינוסים, איפשרו סחר גלובלי בקנה מידה חדש, שימשו ככלי פוליטי לתיחום אימפריות, והחשוב מכל – הן העניקו לאנושות לראשונה תמונה ויזואלית של כדור הארץ כשלם, גם אם מטושטש ולא מדויק בחלקיו. הקרטוגרפים היו גיבורים שקטים שהפכו את הדמיון הגיאוגרפי למציאות מצוירת, מילאו את השטחים הריקים, ונתנו צורה לעולמנו.</p>
</div>

<script>
    const canvas = document.getElementById('cartographer-canvas');
    const ctx = canvas.getContext('2d');
    const shipMarker = document.getElementById('ship-marker');
    const startMarker = document.getElementById('start-marker');
    const dataPointsDiv = document.getElementById('data-points');
    const nextDataBtn = document.getElementById('next-data-btn');
    const applyDataBtn = document.getElementById('apply-data-btn');
    const currentInstructionP = document.getElementById('current-instruction');
    const simulationNotesP = document.getElementById('simulation-notes');
    const explanationButton = document.getElementById('explanation-button');
    const explanationContent = document.getElementById('explanation-content');

    let mapWidth, mapHeight;
    let scale = 0.8; // Pixels per 'unit' (simulated nautical mile) - Adjusted scale
    let originX, originY; // Map origin (center)
    let shipX, shipY; // Ship position in map units relative to origin
    let path = []; // Array to store ship path points {x, y}
    let animationPath = []; // Array to store path points for animation
    let animationStartTime = null;
    let animationDuration = 1000; // ms for move animation
    let lineAnimationDuration = 800; // ms for line drawing animation
    let currentLineAnimation = null; // Object for line drawing animation state

    const simulationData = [
        {
            type: 'instruction',
            instruction: 'ברוכים הבאים ליומן הקרטוגרף! התחלנו את המסע מנמל מוכר.',
            notes: 'מיקומנו הנוכחי מסומן בעוגן במרכז המפה. עלינו לתעד את המסע ולאסוף מידע למפה חדשה.',
            actionText: 'התחל מסע',
            apply: () => { /* No map action initially */ }
        },
        {
            type: 'move',
            data: { distance: 150, bearing: 60 }, // 60 degrees is NE (0=N, 90=E)
            instruction: 'נתון יומן 1: שייטנו 150 מיל ימי בכיוון צפון-מזרח (60° מצפן).',
            notes: 'הקלידו את הנתון ל"דרך מנוחה" (Dead Reckoning) ועדכנו את מיקום הספינה המשוער על המפה.',
            actionText: 'רשום תנועה ביומן',
            apply: (x, y) => {
                const data = simulationData[currentDataIndex].data;
                 // Convert bearing (clockwise from N) to standard angle (counter-clockwise from E)
                 // N=0 -> angle=90, E=90 -> angle=0, S=180 -> angle=-90 (or 270), W=270 -> angle=-180 (or 180)
                const angleRad = (90 - data.bearing) * Math.PI / 180;
                const deltaX = data.distance * Math.cos(angleRad);
                const deltaY = -data.distance * Math.sin(angleRad); // Y is negative upwards on canvas

                const newX = x + deltaX;
                const newY = y + deltaY;

                 // Prepare animation path
                 animationPath = [{ x: x, y: y }, { x: newX, y: newY }];
                 animationStartTime = performance.now();
                 requestAnimationFrame(animateShipMovement); // Start animation

                return { newX: newX, newY: newY, draw: 'line' }; // Return new position for path storage
            }
        },
        {
             type: 'bearing',
             data: { bearing: 250 }, // Example bearing to land (SW)
             instruction: 'נתון יומן 2: התצפיתן מזהה יבשה באופק! כיוונה הוא 250° מצפן.',
             notes: 'שרטטו קו כיוון מהמיקום הנוכחי של הספינה. היבשה חייבת להיות אי שם על הקו הזה.',
             actionText: 'סמן כיוון יבשה',
             apply: (x, y) => {
                 const data = simulationData[currentDataIndex].data;
                 const angleRad = (90 - data.bearing) * Math.PI / 180;
                 const lineLength = Math.max(mapWidth, mapHeight) / scale * 1.5; // Extend line further
                 const endX = x + lineLength * Math.cos(angleRad);
                 const endY = y + lineLength * Math.sin(angleRad);

                 // Prepare line drawing animation
                 currentLineAnimation = {
                     type: 'line',
                     fromX: x,
                     fromY: y,
                     toX: endX,
                     toY: endY,
                     color: '#a0522d', // Brown for land bearings
                     width: 2,
                     startTime: performance.now(),
                     duration: lineAnimationDuration,
                     dashed: false
                 };
                 requestAnimationFrame(animateLineDrawing); // Start animation

                 // Don't add the line to drawnElements immediately, animation will add it at the end
                 return { animateLine: true };
             }
        },
         {
            type: 'move',
            data: { distance: 80, bearing: 150 }, // SE
            instruction: 'נתון יומן 3: המשכנו לשוט. שייטנו 80 מיל ימי בכיוון דרום-מזרח (150° מצפן).',
            notes: 'עדכנו את מיקום הספינה המשוער על בסיס נתון הדרך מנוחה החדש.',
            actionText: 'רשום תנועה ביומן',
            apply: (x, y) => {
                const data = simulationData[currentDataIndex].data;
                const angleRad = (90 - data.bearing) * Math.PI / 180;
                const deltaX = data.distance * Math.cos(angleRad);
                const deltaY = -data.distance * Math.sin(angleRad);

                 const newX = x + deltaX;
                const newY = y + deltaY;

                 animationPath = [{ x: x, y: y }, { x: newX, y: newY }];
                 animationStartTime = performance.now();
                 requestAnimationFrame(animateShipMovement); // Start animation

                return { newX: newX, newY: newY, draw: 'line' };
            }
        },
        {
             type: 'bearing',
             data: { bearing: 300 }, // NW
             instruction: 'נתון יומן 4: שוב נצפתה יבשה! מהמיקום הנוכחי, כיוונה הוא 300° מצפן.',
             notes: 'שרטטו קו כיוון נוסף. נקודת החיתוך המשוערת של הקווים מצביעה על מיקום החוף!',
             actionText: 'סמן כיוון יבשה',
             apply: (x, y) => {
                 const data = simulationData[currentDataIndex].data;
                 const angleRad = (90 - data.bearing) * Math.PI / 180;
                 const lineLength = Math.max(mapWidth, mapHeight) / scale * 1.5;
                 const endX = x + lineLength * Math.cos(angleRad);
                 const endY = y + lineLength * Math.sin(angleRad);

                 currentLineAnimation = {
                     type: 'line',
                     fromX: x,
                     fromY: y,
                     toX: endX,
                     toY: endY,
                     color: '#a0522d',
                      width: 2,
                     startTime: performance.now(),
                     duration: lineAnimationDuration,
                     dashed: false
                 };
                 requestAnimationFrame(animateLineDrawing);

                 // Intersection logic will run AFTER line animation finishes in animateLineDrawing
                 return { animateLine: true, checkIntersection: true }; // Indicate to check intersection later
             }
        },
        {
            type: 'astro',
            data: { latitude: -10 }, // Example Southern Latitude
            instruction: 'נתון יומן 5: מדדנו גובה שמש בצהריים. קו הרוחב המשוער הוא 10° דרום.',
            notes: 'זהו נתון "מוחלט" יותר, אך קשה לשלב אותו בקלות עם מפת ה"דרך מנוחה" היחסית שלנו.',
            actionText: 'סמן קו רוחב',
             apply: (x, y) => {
                 // To represent latitude on a relative map, we need a reference.
                 // Let's assume our start point (0,0 in map units) corresponds to 30 degrees NORTH.
                 // 1 degree of latitude is approx 60 nautical miles.
                 // So, 10 degrees SOUTH is 40 degrees (30N to 0 then 10S) * 60 miles = 2400 miles south of our reference latitude.
                 // Convert this to map units based on scale. Y increases SOUTH in standard cartesian, but our canvas Y decreases upwards.
                 // Let's assume 1 map unit = 1 nautical mile for simplicity with scale being pixels/unit.
                 // Latitude 30N is at Y=0. Latitude 10S is 40 * 60 units South.
                 // This approach is problematic because our map is relative.
                 // Instead, let's simplify: assume a certain range of Y on our map corresponds to a latitude range.
                 // If Y=0 is 30N, let Y=-100 be 31N, Y=100 be 29N etc. (1 unit = 0.01 deg lat -> 60 miles/deg * 0.01 units/mile = 0.6 units/deg lat? confusiing)
                 // Let's try a simpler approach: assume our starting point (0,0) is at a known latitude (e.g. 30N).
                 // We are now at a new latitude (10S). This is 40 degrees South of our start.
                 // We can draw a horizontal line representing this latitude *relative to our start point's latitude*.
                 // Let's say 1 map unit = 0.1 degrees latitude change. So 40 degrees = 400 map units.
                 // Since canvas Y decreases upwards, 10S (40 deg South of 30N) would be +400 units in the Y direction from the origin Y.
                 const startLatitude = 30; // Assume start point is at 30N
                 const currentLatitude = simulationData[currentDataIndex].data.latitude; // -10S
                 const latitudeDifference = startLatitude - currentLatitude; // 30 - (-10) = 40 degrees difference
                 const unitsPerDegree = 10; // Arbitrary: 10 map units per degree latitude difference
                 const latitudeLineY = originY + latitudeDifference * unitsPerDegree * scale; // Convert relative Y units to canvas pixels

                 // The line needs to be drawn across the whole map width in canvas coordinates
                 const lineCanvasY = originY + (shipY + latitudeDifference * unitsPerDegree) * scale;

                 currentLineAnimation = {
                     type: 'line',
                     // Draw horizontally across the map area
                     fromX: -mapWidth / (2 * scale), // Left edge in map units relative to origin
                     fromY: (shipY + latitudeDifference * unitsPerDegree), // Calculated Y in map units
                     toX: mapWidth / (2 * scale), // Right edge in map units relative to origin
                     toY: (shipY + latitudeDifference * unitsPerDegree), // Same Y
                     color: '#1d3557', // Dark blue for astro lines
                     width: 2,
                     dashed: true,
                     startTime: performance.now(),
                     duration: lineAnimationDuration
                 };
                 requestAnimationFrame(animateLineDrawing);

                 // This doesn't update ship position based on latitude, as that wasn't standard practice.
                 // It just adds the latitude line as a piece of data on the map.
                 return { animateLine: true };
             }
        },
         {
            type: 'instruction',
            instruction: 'סיימנו את איסוף הנתונים לקטע זה של המסע.',
            notes: 'הצלחנו לשלב נתוני "דרך מנוחה", תצפיות על יבשה ומדידת קו רוחב כדי לשער את מיקומנו ולשרטט את קטע החוף הנצפה. ראיתם כמה מידע חלקי ולא מדויק צריך לשלב כדי ליצור מפה!',
            actionText: 'סוף הסימולציה',
            apply: () => { /* End state */ }
        },
    ];

    let drawnElements = []; // Store lines/points drawn on canvas {type, data...}

    function resizeCanvas() {
        const mapArea = document.getElementById('map-area');
        mapWidth = mapArea.clientWidth;
        mapHeight = mapArea.clientHeight;
        canvas.width = mapWidth;
        canvas.height = mapHeight;

        // Set origin to center of the map initially
        originX = mapWidth / 2;
        originY = mapHeight / 2;

        // Set initial ship position relative to origin (starting at origin)
        if (shipX === undefined || shipY === undefined) {
            shipX = 0;
            shipY = 0;
            path = [{ x: shipX, y: shipY }];
             // Place start marker
            startMarker.style.left = `${originX}px`;
            startMarker.style.top = `${originY}px`;
        }

        // Redraw everything after resize
        drawMap();
        updateShipMarkerPosition();
    }

    function drawMap() {
        // Clear canvas
        ctx.clearRect(0, 0, mapWidth, mapHeight);

        // Draw grid or background if desired (skipped for cleaner look)

        // Draw ship path
        ctx.beginPath();
        ctx.strokeStyle = '#1d3557'; // Dark blue path
        ctx.lineWidth = 3; // Thicker path
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';

        if (path.length > 0) {
            ctx.moveTo(originX + path[0].x * scale, originY + path[0].y * scale);
            for (let i = 1; i < path.length; i++) {
                ctx.lineTo(originX + path[i].x * scale, originY + path[i].y * scale);
            }
        }
        ctx.stroke();

        // Draw saved elements (lines, points)
        drawnElements.forEach(el => {
            if (el.type === 'line') {
                ctx.beginPath();
                ctx.strokeStyle = el.color || '#a0522d';
                ctx.lineWidth = el.width || 2;
                if (el.dashed) {
                    ctx.setLineDash([8, 8]); /* More distinct dash */
                } else {
                     ctx.setLineDash([]);
                }

                // Convert relative coordinates to canvas coordinates
                const startCanvasX = originX + el.fromX * scale;
                const startCanvasY = originY + el.fromY * scale;
                const endCanvasX = originX + el.toX * scale;
                const endCanvasY = originY + el.toY * scale;

                ctx.moveTo(startCanvasX, startCanvasY);
                ctx.lineTo(endCanvasX, endCanvasY);
                ctx.stroke();
                 ctx.setLineDash([]); // Reset line dash
            } else if (el.type === 'point') {
                 // Draw estimated land points (intersection)
                 ctx.fillStyle = el.color || '#e63946'; // Red for intersection
                 ctx.beginPath();
                 const canvasX = originX + el.x * scale;
                 const canvasY = originY + el.y * scale;
                 ctx.arc(canvasX, canvasY, 6, 0, Math.PI * 2); /* Slightly larger point */
                 ctx.fill();
             }
        });

         // Draw the current line animation frame
         if (currentLineAnimation) {
             const progress = (performance.now() - currentLineAnimation.startTime) / currentLineAnimation.duration;
             const easedProgress = easeInOutQuad(Math.min(progress, 1)); // Apply easing
             if (easedProgress < 1) {
                 ctx.beginPath();
                 ctx.strokeStyle = currentLineAnimation.color;
                 ctx.lineWidth = currentLineAnimation.width;
                  if (currentLineAnimation.dashed) {
                    ctx.setLineDash([8, 8]);
                } else {
                     ctx.setLineDash([]);
                }

                 const startCanvasX = originX + currentLineAnimation.fromX * scale;
                 const startCanvasY = originY + currentLineAnimation.fromY * scale;
                 const endCanvasX = originX + (currentLineAnimation.fromX + (currentLineAnimation.toX - currentLineAnimation.fromX) * easedProgress) * scale;
                 const endCanvasY = originY + (currentLineAnimation.fromY + (currentLineAnimation.toY - currentLineAnimation.fromY) * easedProgress) * scale;

                 ctx.moveTo(startCanvasX, startCanvasY);
                 ctx.lineTo(endCanvasX, endCanvasY);
                 ctx.stroke();
                 ctx.setLineDash([]);

                 requestAnimationFrame(animateLineDrawing); // Continue animation
             } else {
                 // Animation finished, add the full line to drawn elements
                 drawnElements.push({
                     type: 'line',
                     fromX: currentLineAnimation.fromX,
                     fromY: currentLineAnimation.fromY,
                     toX: currentLineAnimation.toX,
                     toY: currentLineAnimation.toY,
                     color: currentLineAnimation.color,
                     width: currentLineAnimation.width,
                     dashed: currentLineAnimation.dashed
                 });
                 currentLineAnimation = null; // Clear animation state
                 drawMap(); // Redraw map with the newly added full line

                 // Check intersection if needed after line animation finishes
                 if (simulationData[currentDataIndex]?.apply(shipX, shipY)?.checkIntersection) {
                      findIntersectionOfLastTwoBrownLines(); // This will draw the point
                      drawMap(); // Redraw map to show the point
                 }
             }
         }


    }

    function updateShipMarkerPosition() {
        const canvasX = originX + shipX * scale;
        const canvasY = originY + shipY * scale;
        shipMarker.style.left = `${canvasX}px`;
        shipMarker.style.top = `${canvasY}px`;
    }

    function animateShipMovement(currentTime) {
        if (!animationStartTime) animationStartTime = currentTime;
        const progress = (currentTime - animationStartTime) / animationDuration;
        const easedProgress = easeInOutQuad(Math.min(progress, 1));

        if (easedProgress < 1) {
            const currentX = animationPath[0].x + (animationPath[1].x - animationPath[0].x) * easedProgress;
            const currentY = animationPath[0].y + (animationPath[1].y - animationPath[0].y) * easedProgress;

            // Update ship position visually during animation
            shipX = currentX;
            shipY = currentY;
            // Update path up to current point for drawing
            const currentPathSegment = { x: currentX, y: currentY };
             // Temporarily add segment for drawing animation
            path.push(currentPathSegment);

            drawMap();
            updateShipMarkerPosition();

             // Remove the temporary segment before next frame or after animation ends
             path.pop(); // Remove the temporary segment

            requestAnimationFrame(animateShipMovement);
        } else {
            // Animation finished, set final position and add to path
            shipX = animationPath[1].x;
            shipY = animationPath[1].y;
            path.push({ x: shipX, y: shipY }); // Add the final position to permanent path
            animationPath = [];
            animationStartTime = null;
            drawMap(); // Final redraw
            updateShipMarkerPosition();
             // Enable controls after animation
             applyDataBtn.disabled = true;
             applyDataBtn.style.display = 'none';
             nextDataBtn.style.display = 'block';
             simulationNotesP.textContent += ' המפה עודכנה.';
        }
    }

     function animateLineDrawing(currentTime) {
         if (!currentLineAnimation.startTime) currentLineAnimation.startTime = currentTime;
         const progress = (currentTime - currentLineAnimation.startTime) / currentLineAnimation.duration;
         const easedProgress = easeInOutQuad(Math.min(progress, 1));

         if (easedProgress < 1) {
             drawMap(); // Redraw existing elements
             // Drawing logic is inside drawMap now, triggered by requestAnimationFrame
             requestAnimationFrame(animateLineDrawing);
         } else {
              // Animation finished logic is handled inside drawMap's currentLineAnimation block
              drawMap(); // Final draw includes adding to drawnElements and clearing state
         }
     }


    function easeInOutQuad(t) {
      return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
    }


    function addDataPointToPanel(data) {
        const p = document.createElement('p');
        p.classList.add('log-entry'); // Apply log entry style
        p.innerHTML = `<strong>[${new Date().toLocaleTimeString()}]</strong> ${data.instruction}`; // Add timestamp/marker
        dataPointsDiv.appendChild(p);
        dataPointsDiv.scrollTop = dataPointsDiv.scrollHeight; // Auto-scroll to bottom
    }

    let currentDataIndex = -1; // Start before the first element

    function handleNextData() {
        currentDataIndex++;
        if (currentDataIndex < simulationData.length) {
            const data = simulationData[currentDataIndex];
            addDataPointToPanel(data);
            currentInstructionP.textContent = data.instruction;
            simulationNotesP.textContent = data.notes;

            applyDataBtn.style.display = 'block';
            applyDataBtn.textContent = data.actionText;
            applyDataBtn.disabled = false;
            nextDataBtn.style.display = 'none'; // Hide next button
        } else {
            currentInstructionP.textContent = 'המסע הסתיים.';
            simulationNotesP.textContent = 'גללו למטה להסבר מעמיק יותר על אתגרי הקרטוגרפיה בעידן התגליות.';
            applyDataBtn.style.display = 'none';
            nextDataBtn.style.display = 'none';
        }
    }

    function handleApplyData() {
        const data = simulationData[currentDataIndex];
        applyDataBtn.disabled = true; // Disable button while applying

        const result = data.apply(shipX, shipY); // Pass current ship coordinates

        if (result) {
             // Handle movement animation start
            if (result.newX !== undefined && result.newY !== undefined) {
                 // Position will be updated in the animation loop
                 // Path will be updated in the animation loop completion
            } else if (result.animateLine) {
                 // Line animation started by the apply function
                 // The drawn element is added at the end of the animation
            } else if (result.point) {
                 // Add a specific point marker instantly (e.g., a known landmark if we had one)
                 drawnElements.push({
                     type: 'point',
                     x: result.point.x,
                     y: result.point.y,
                     color: result.point.color || 'green'
                 });
                 drawMap(); // Redraw immediately for points
            } else {
                // No animation, just redraw (e.g., initial instruction)
                drawMap();
            }

            // If no animation is expected (e.g., instruction type), move to next state immediately
            if (!result.animateLine && (result.newX === undefined || result.newY === undefined)) { // If not move and not line animation
                 // Move to next step
                 applyDataBtn.disabled = true;
                 applyDataBtn.style.display = 'none';
                 nextDataBtn.style.display = 'block';
                 simulationNotesP.textContent += ' המפה עודכנה.';
            }
             // For move and line animations, the button state update happens at the end of the animation.
        }
    }

    // Simple line intersection function (assuming lines are infinite for bearing)
    // based on https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    function findIntersection(p1, p2, p3, p4) {
        const x1 = p1.x, y1 = p1.y;
        const x2 = p2.x, y2 = p2.y;
        const x3 = p3.x, y3 = p3.y;
        const x4 = p4.x, y4 = p4.y;

        const denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);

        // Lines are parallel or collinear
        if (denominator === 0) {
            return null;
        }

        const t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator;
        const u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denominator;

        // If we wanted segment intersection, we'd check 0 <= t <= 1 and 0 <= u <= 1
        // For bearing lines (infinite), we just need one intersection point
        const intersectX = x1 + t * (x2 - x1);
        const intersectY = y1 + t * (y2 - y1);

        return { x: intersectX, y: intersectY };
    }

    function findIntersectionOfLastTwoBrownLines() {
         const brownLines = drawnElements.filter(el => el.type === 'line' && el.color === '#a0522d');
         if (brownLines.length >= 2) {
             const line1 = brownLines[brownLines.length - 2];
             const line2 = brownLines[brownLines.length - 1];

             // Use start and end points relative to origin
             const p1 = { x: line1.fromX, y: line1.fromY };
             const p2 = { x: line1.toX, y: line1.toY };
             const p3 = { x: line2.fromX, y: line2.fromY };
             const p4 = { x: line2.toX, y: line2.toY };

             const intersection = findIntersection(p1, p2, p3, p4);

             if (intersection) {
                 // Add the intersection point to drawn elements
                 drawnElements.push({
                     type: 'point',
                     x: intersection.x,
                     y: intersection.y,
                     color: '#e63946' // Mark estimated land location in red
                 });
                 simulationNotesP.textContent += ' נמצאה נקודת חיתוך! זהו המיקום המשוער של קו החוף שראינו!';
             } else {
                  simulationNotesP.textContent += ' הקווים לא נחתכו. אולי הנתונים היו לא מדויקים, היבשה רחוקה מאוד, או שהתצפיות התייחסו לנקודות שונות.';
             }
         }
    }


    function setupSimulation() {
        // Initialize data and state
        // Data is already defined in simulationData array

        // Start with the first instruction
        handleNextData();

        // Add event listeners
        nextDataBtn.addEventListener('click', handleNextData);
        applyDataBtn.addEventListener('click', handleApplyData);
        explanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            explanationButton.textContent = isHidden ? 'הסתר הסבר מורחב על אתגרי הקרטוגרפיה' : 'הצג הסבר מורחב על אתגרי הקרטוגרפיה'; // Update text
        });


        // Initial resize and draw
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
    }

    // Run simulation setup on page load
    window.addEventListener('load', setupSimulation);

</script>