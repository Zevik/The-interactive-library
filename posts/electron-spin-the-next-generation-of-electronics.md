---
title: "ספין אלקטרוני: הדור הבא של האלקטרוניקה?"
english_slug: electron-spin-the-next-generation-of-electronics
category: "פיזיקה"
tags: [ספינטרוניקה, ספין, אלקטרון, מגנטיות, ננוטכנולוגיה]
---
<h1>ספין אלקטרוני: הדור הבא של האלקטרוניקה?</h1>
<p>תחשבו מחדש על האלקטרון. הוא לא רק נושא מטען חשמלי, אלא גם מחזיק בסוד קוונטי: ה<b>ספין</b>. תכונה פנימית זו, מעין "כיוון סיבוב" זעיר, עשויה לשנות את פני הטכנולוגיה. הכירו את הספינטרוניקה - שדה פורץ דרך שמנצל את הספין כדי ליצור אלקטרוניקה מהירה, חסכונית ולא נדיפה.</p>

<div class="simulation-container">
    <h2>סימולציה: רכיב ספינטרוני בסיסי (אפקט GMR)</h2>
    <p>בחנו כיצד התנגדות הרכיב והזרם דרכו משתנים כפונקציה של כיוון הספין היחסי.</p>
    <div class="device">
        <div class="electron-source">
            <span>זרם<br>אלקטרונים</span>
            <div class="electron-stream">
                 <!-- Electrons will be added/managed by JS for animation -->
             </div>
        </div>
        <div class="layer fixed-layer">
            <div class="layer-label">שכבה פרומגנטית<br>מקובעת</div>
            <div class="magnetization-arrow fixed-arrow">↑</div>
        </div>
        <div class="layer non-magnetic-layer">
            <div class="layer-label">שכבה לא-מגנטית<br>(מפריד)</div>
        </div>
        <div class="layer free-layer">
            <div class="layer-label">שכבה פרומגנטית<br>חופשית</div>
            <div class="magnetization-arrow free-arrow">↑</div>
        </div>
        <div class="electron-output">
            <div class="output-label">התנגדות: <span id="resistance-value">...</span> Ω</div>
             <div class="output-label">זרם: <span id="current-value">...</span> A</div>
        </div>

    </div>

    <div class="controls">
        <label for="free-layer-angle">כיוון המגנטיזציה של השכבה החופשית:</label>
         <span class="angle-label parallel-label">מקביל (0°)</span>
        <input type="range" id="free-layer-angle" min="0" max="180" value="0">
        <span id="angle-display" class="angle-label current-angle-display">0°</span>
        <span class="angle-label anti-parallel-label">אנטי-מקביל (180°)</span>
    </div>

    <div class="graph-container">
        <h3>התנגדות המבנה כפונקציה של הזווית היחסית</h3>
        <canvas id="resistance-graph" width="450" height="250"></canvas>
    </div>
</div>

<style>
    /* Basic Reset and Font */
    .simulation-container * {
        box-sizing: border-box;
    }

    .simulation-container {
        font-family: 'Heebo', sans-serif; /* Example of a better font */
        direction: rtl;
        text-align: center;
        margin: 30px auto;
        border: none; /* Remove basic border */
        padding: 25px;
        max-width: 750px; /* Slightly wider */
        background: linear-gradient(to bottom right, #ffffff, #e9eff7); /* Soft gradient background */
        border-radius: 12px; /* Rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Subtle shadow */
        color: #333;
    }

    .simulation-container h1 {
        color: #004080; /* Deep blue */
        margin-bottom: 15px;
        font-size: 2em;
    }

     .simulation-container h2 {
        color: #0056b3; /* Medium blue */
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.6em;
        border-bottom: 2px solid #007bff; /* Underline */
        display: inline-block; /* Fit underline to text */
        padding-bottom: 5px;
     }

     .simulation-container h3 {
        color: #007bff; /* Brighter blue */
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.3em;
     }

     .simulation-container p {
         font-size: 1.1em;
         line-height: 1.6;
         color: #555;
         margin-bottom: 20px;
     }

    .device {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 30px 0;
        position: relative;
         height: 180px; /* More height */
        padding: 0 10px; /* Add some padding to ends */
    }

    .electron-source, .electron-output {
        padding: 15px 10px; /* Increased padding */
        font-weight: bold;
        text-align: center;
        width: 120px; /* Wider */
        font-size: 1em;
        color: #0056b3; /* Blue text */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative; /* Needed for electron stream positioning */
    }
     .electron-source {
         text-align: right;
          padding-right: 20px;
          width: 150px; /* Even wider source */
     }
     .electron-output {
         text-align: left;
         padding-left: 20px;
         width: 150px; /* Wider output */
     }

    .layer {
        border: none; /* Remove borders, use shadows */
        margin: 0 5px; /* Increased margin */
        padding: 20px 10px; /* Increased padding */
        width: 110px; /* Wider layers */
        text-align: center;
        position: relative;
         height: 120px; /* Fixed height for layers */
         display: flex;
         flex-direction: column;
         justify-content: center;
         align-items: center;
         overflow: hidden;
         border-radius: 8px; /* Rounded layer corners */
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Layer shadow */
    }

    .fixed-layer {
        background: linear-gradient(to bottom, #a0a0a0, #808080); /* Gradient */
        color: #fff; /* White text on dark layer */
    }

    .non-magnetic-layer {
        background-color: #e0e0e0; /* Light gray */
        width: 50px; /* Thinner */
        padding: 20px 8px;
        color: #333;
    }

    .free-layer {
        background: linear-gradient(to bottom, #c0c0c0, #a0a0a0); /* Gradient */
         color: #fff;
    }

    .layer-label {
        font-size: 0.85em; /* Slightly larger font for labels */
        margin-bottom: 8px;
         line-height: 1.3;
         font-weight: bold;
         text-shadow: 0 1px 2px rgba(0,0,0,0.1); /* Text shadow for readability */
    }

    .magnetization-arrow {
        font-size: 2.5em; /* Larger arrow */
        font-weight: bold;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        transform-origin: center;
        color: #00ffff; /* Cyan for visibility */
         pointer-events: none;
         transition: transform 0.3s ease-out; /* Smooth arrow rotation */
    }

     /* Adjust initial position slightly for better centering */
    .fixed-arrow {
         transform: translate(-50%, -50%) rotate(0deg);
    }

    .free-arrow {
         transform: translate(-50%, -50%) rotate(0deg);
    }


    .output-label {
        font-size: 1em;
        margin-top: 8px; /* Increased margin */
        color: #0056b3;
    }
    .output-label span {
        font-weight: bold;
        color: #007bff; /* Highlight values */
    }


    .controls {
        margin-top: 30px; /* More space */
        margin-bottom: 25px;
        display: flex; /* Use flexbox for alignment */
        align-items: center;
        justify-content: center;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }
    .controls label {
        display: inline-block;
        margin-bottom: 5px; /* Adjust for flex layout */
        font-weight: bold;
        font-size: 1em;
        margin-right: 15px; /* Space after label */
        color: #333;
    }
    .controls input[type="range"] {
        width: 250px; /* Wider slider */
        margin: 0 15px; /* Space around slider */
        vertical-align: middle;
        -webkit-appearance: none; /* Remove default styles */
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
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }
      .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }

     .controls .angle-label {
         vertical-align: middle;
         font-size: 0.9em;
         color: #555;
         min-width: 80px; /* Give labels space */
         text-align: center;
     }
     .controls .current-angle-display {
         font-weight: bold;
         color: #007bff; /* Highlight current value */
         font-size: 1.1em;
     }


    .graph-container {
        margin-top: 35px; /* More space */
    }

    canvas {
        border: 1px solid #ccc;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05); /* Inner shadow for depth */
    }

     /* Electron flow visualization */
    .electron-flow {
         /* This container spans across the device visually */
         position: absolute;
         top: 50%; /* Vertically center the stream */
         left: 0;
         width: 100%;
         height: 30px; /* Height of the visual stream area */
         transform: translateY(-50%);
         pointer-events: none;
         overflow: hidden;
         /* Background or effects can go here */
         background-color: rgba(0, 123, 255, 0.05); /* Very subtle blue tint */
         border-radius: 15px; /* Rounded flow ends */
    }

     .electron-stream {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%; /* Stream covers the flow container */
         height: 100%;
         display: flex;
         align-items: center;
         opacity: 1; /* Base opacity */
         transition: opacity 0.5s ease-out; /* Smooth opacity transition */
     }

    .electron {
        font-size: 1.5em; /* Larger electrons */
        position: absolute;
        left: 0%;
        /* Animation properties handled by JS */
        color: #00cc00; /* Default color (e.g., spin-up) */
        transition: left linear; /* Smooth position transition */
         text-shadow: 0 0 3px rgba(0, 204, 0, 0.5); /* Subtle glow */
         font-weight: bold;
    }
     .electron.spin-down {
         color: #ff6666; /* Reddish for spin-down */
         text-shadow: 0 0 3px rgba(255, 102, 102, 0.5);
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto 20px auto; /* More space */
        padding: 12px 25px; /* Larger padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none; /* Remove border */
        background-color: #007bff;
        color: white;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    #toggle-explanation:hover {
        background-color: #0056b3;
        transform: translateY(-2px); /* Lift effect on hover */
    }
     #toggle-explanation:active {
         background-color: #004080;
         transform: translateY(0); /* Press effect */
     }


    .explanation {
        display: none;
        margin-top: 25px;
        padding: 20px; /* More padding */
        border: 1px solid #b3d9ff; /* Lighter border */
        background-color: #e9f7ff; /* Light blue background */
        text-align: right;
        direction: rtl;
        border-radius: 10px; /* Rounded corners */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .explanation h2 {
        text-align: center;
        margin-bottom: 20px; /* More space */
        color: #0056b3;
        border-bottom: none; /* Remove underline from explanation title */
        font-size: 1.8em;
    }
     .explanation h3 {
         margin-top: 20px; /* More space */
         margin-bottom: 8px;
         color: #007bff;
         border-bottom: 1px dashed #007bff; /* Dashed underline */
         padding-bottom: 4px;
         font-size: 1.2em;
     }
     .explanation p {
         margin-bottom: 15px;
         font-size: 1em; /* Slightly smaller font in explanation */
         color: #444;
     }
     .explanation ul {
         margin-right: 25px; /* More indent */
         list-style-type: disc;
         margin-bottom: 15px;
     }
      .explanation li {
          margin-bottom: 8px; /* More space between list items */
          line-height: 1.5;
          color: #444;
      }
</style>

<button id="toggle-explanation">הצג הסבר מעמיק</button>

<div class="explanation">
    <h2>הסבר מעמיק: הצצה לעולם הספינטרוניקה</h2>

    <h3>מהו ספין אלקטרוני בפשטות?</h3>
    <p>דמיינו אלקטרון לא רק ככדור זעיר עם מטען, אלא גם כבעל "סיבוב פנימי". סיבוב זה אינו תנועה פיזית במרחב אלא תכונה קוונטית יסודית, המכונה ספין. עבור אלקטרונים, הספין יכול להיות בעל שני כיוונים בלבד ביחס לציר חיצוני - לרוב אנו קוראים להם "ספין למעלה" (↑) ו"ספין למטה" (↓). תכונה קבועה זו היא מעין "מצפן" פנימי של האלקטרון.</p>

    <h3>מעבר מאלקטרוניקה לספינטרוניקה: המטען פוגש את הספין</h3>
    <p>בעוד שהאלקטרוניקה המסורתית מתבססת כולה על שליטה בתנועת המטען החשמלי של האלקטרונים (הזרם), הספינטרוניקה מוסיפה מימד נוסף: היכולת לשלוט, למדוד, ולנצל את כיוון הספין עצמו. הספין הופך להיות נושא מידע, בדומה למטען, ואף מעניק יכולות חדשות שלא קיימות באלקטרוניקה הקונבנציונלית.</p>

    <h3>איך עובדים רכיבים ספינטרוניים בסיסיים?</h3>
    <p>הסימולציה מדגימה מבנה דומה לרכיב המנצל את <strong>אפקט ההתנגדות המגנטית הענקית (GMR)</strong>. רכיבים אלו מורכבים משכבות דקות של חומרים שונים, לרוב בקנה מידה ננומטרי:</p>
    <ul>
        <li><strong>שכבה פרומגנטית מקובעת:</strong> שכבה עשויה מחומר מגנטי (כמו ברזל, ניקל, קובלט או סגסוגותיהם) שהמגנטיזציה שלה ("כיוון המצפנים הפנימיים" של האטומים בה) קבועה בכיוון מסוים. שכבה זו משמשת כ"מקטב ספין" - היא מאפשרת לאלקטרונים עם ספין מקביל למגנטיזציה שלה לעבור בקלות יחסית, בעוד אלקטרונים עם ספין אנטי-מקביל נתקלים בהתנגדות גדולה יותר ומתפזרים.</li>
        <li><strong>שכבה לא-מגנטית (מפריד):</strong> שכבה דקה מאוד של חומר לא מגנטי (כמו נחושת) המפרידה בין השכבות הפרומגנטיות. היא דקה מספיק כדי שהאלקטרונים יוכלו לעבור דרכה תוך שמירה על כיוון הספין המקורי שלהם מהשכבה המקובעת.</li>
        <li><strong>שכבה פרומגנטית חופשית:</strong> שכבה פרומגנטית נוספת, אך הפעם כיוון המגנטיזציה שלה יכול להשתנות (למשל, תחת השפעת שדה מגנטי חיצוני או זרם חשמלי). שכבה זו משמשת כ"מנתח ספין" - היא מגיבה לאלקטרונים המגיעים מהשכבה המקובעת בהתאם לכיוון הספין שלהם ביחס למגנטיזציה שלה.</li>
    </ul>

    <h3>הקשר בין ספין להתנגדות (פיזור תלוי ספין)</h3>
    <p>הקסם מתרחש בתוך השכבות הפרומגנטיות. הסיכוי של אלקטרון להתפזר (ולהתנגד בכך לזרימת הזרם) תלוי בכיוון הספין שלו ביחס לכיוון המגנטיזציה של החומר בו הוא נמצא. אלקטרון שספינו "מקביל" למגנטיזציה של השכבה יעבור בה בקלות יחסית (ערוץ התנגדות נמוכה), בעוד אלקטרון שספינו "אנטי-מקביל" למגנטיזציה יתפזר יותר ויחווה התנגדות גבוהה (ערוץ התנגדות גבוהה).</p>

    <h3>אפקט ה-GMR בפעולה: מתג התנגדות ענק</h3>
    <p>אפקט ה-GMR הוא השינוי הדרמטי בהתנגדות הכוללת של המבנה כולו, כתלות בזווית בין כיווני המגנטיזציה של השכבה המקובעת והשכבה החופשית:</p>
    <ul>
        <li><strong>מגנטיזציה מקבילה (זווית 0°):</strong> השכבה המקובעת "מקטבת" את רוב האלקטרונים העוברים דרכה לספין בכיוון מסוים. כיוון שמגנטיזציית השכבה החופשית גם היא באותו כיוון, האלקטרונים המקוטבים עוברים גם דרכה בקלות יחסית דרך ערוץ ההתנגדות הנמוכה בשתי השכבות. <strong>ההתנגדות הכוללת נמוכה, והזרם גבוה.</strong> מצב זה יכול לייצג מידע בינארי, למשל '1'.</li>
        <li><strong>מגנטיזציה אנטי-מקבילה (זווית 180°):</strong> השכבה המקובעת עדיין מקטבת את האלקטרונים לאותו כיוון ספין. אולם, כשהם מגיעים לשכבה החופשית שכיוון המגנטיזציה שלה הפוך, אותם אלקטרונים מקוטבים מוצאים את עצמם עם ספין "אנטי-מקביל" למגנטיזציה של השכבה החופשית. הם חווים פיזור חזק והתנגדות גבוהה מאוד במעבר דרכה. <strong>ההתנגדות הכוללת גבוהה, והזרם נמוך.</strong> מצב זה יכול לייצג '0'.</li>
    </ul>
    <p>השינוי המשמעותי הזה בהתנגדות (מכאן השם "התנגדות מגנטית ענקית") מאפשר לרכיב לשמש כמתג אלקטרוני שנשלט על ידי כיוון המגנטיזציה.</p>

     <h3>עוד אפקט חשוב: TMR (Tunnel Magnetoresistance)</h3>
     <p>עקרון דומה, אך במקום שכבה לא-מגנטית מוליכה, יש שכבה מבודדת דקה במיוחד (עד כדי מנהור קוונטי של אלקטרונים דרכה). גם כאן, מעבר האלקטרונים והתנגדות המבנה תלויים מאוד בכיוון המגנטיזציה היחסי של שתי השכבות הפרומגנטיות הסוגרות על המבודד.</p>

    <h3>איפה פוגשים ספינטרוניקה היום?</h3>
    <ul>
        <li><strong>דיסקים קשיחים (HDD):</strong> טכנולוגיית ה-GMR וה-TMR חוללו מהפכה ביכולת לקרוא מידע מדיסקים קשיחים בצפיפות גבוהה. ראשי הקריאה בדיסקים מודרניים מבוססים על אפקט זה, המזהה שינויים זעירים בשדה המגנטי המייצגים את סיביות המידע.</li>
        <li><strong>זיכרון MRAM:</strong> סוג מבטיח של זיכרון מחשב לא-נדיף (המידע נשמר גם ללא חשמל) המשתמש בתאי TMR לאחסון ביטים. ל-MRAM פוטנציאל להיות מהיר, חסכוני ובעל צפיפות גבוהה.</li>
    </ul>

    <h3>עתיד מבטיח</h3>
    <p>הספינטרוניקה עדיין בחיתוליה יחסית לאלקטרוניקה, אך היא מציעה דרכים חדשות לעבד מידע ואף פותחת פתח לחישובים קוונטיים. היכולת לשלוט גם במטען וגם בספין באותו התקן עשויה להוביל לרכיבים אלקטרוניים בעלי ביצועים ויעילות חסרי תקדים.</p>
</div>

<script>
    const angleControl = document.getElementById('free-layer-angle');
    const angleDisplay = document.getElementById('angle-display');
    const freeArrow = document.querySelector('.free-arrow');
    const resistanceValueSpan = document.getElementById('resistance-value');
    const currentValueSpan = document.getElementById('current-value');
    const explanationDiv = document.querySelector('.explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const canvas = document.getElementById('resistance-graph');
    const ctx = canvas.getContext('2d');
    const electronStreamContainer = document.querySelector('.electron-stream'); // Container for electron divs
    const electronSourceDiv = document.querySelector('.electron-source'); // Source div for stream start point

    const R_min = 80; // Minimum resistance (arbitrary units) - adjusted for better range
    const R_max = 300; // Maximum resistance (arbitrary units) - increased range for visual effect
    const V_supply = 1; // Constant voltage supply (arbitrary units, e.g., Volts)
    const animationDurationMin = 1.5; // seconds - for high current (low R)
    const animationDurationMax = 6; // seconds - for low current (high R)
    const numberOfElectrons = 8; // Number of electrons to simulate in the stream

    // --- Electron Animation Setup ---
    // Create electron elements dynamically
    for (let i = 0; i < numberOfElectrons; i++) {
        const electron = document.createElement('div');
        electron.classList.add('electron');
        // Assign alternating spins for visual variety
        if (i % 2 === 0) {
            electron.classList.add('spin-up');
            electron.textContent = '↑';
        } else {
            electron.classList.add('spin-down');
            electron.textContent = '↓';
        }
        // Set initial random positions and stagger animations
        const delay = (i / numberOfElectrons) * (animationDurationMax * 0.8); // Stagger delays
        electron.style.transitionDelay = `${delay}s`;
        electron.style.left = `-20px`; // Start off-screen
        electronStreamContainer.appendChild(electron);
    }

     const electrons = electronStreamContainer.querySelectorAll('.electron');

     // Function to start electron animation
     function startElectronAnimation(duration) {
         electrons.forEach((electron, index) => {
             // Remove existing transition to reset position instantly before starting new one
            electron.style.transition = 'none';
            electron.style.left = '-20px'; // Reset position to start

            // Use requestAnimationFrame to re-enable transition after reset
            requestAnimationFrame(() => {
                requestAnimationFrame(() => { // Double RAF for guaranteed transition reset
                    electron.style.transition = `left linear ${duration}s`;
                    electron.style.left = 'calc(100% + 20px)'; // Move to end
                });
            });
         });
     }

     // Function to restart electron animation with updated duration
     function restartElectronAnimation(duration) {
         // Stop current animations by resetting transition and position
         electrons.forEach(electron => {
             electron.style.transition = 'none';
             // Capture current computed left before changing
             const currentLeft = getComputedStyle(electron).left;
             electron.style.left = currentLeft; // Set left to its current computed value
         });

         // Use a small timeout or RAF to ensure the style change registers before applying new transition
         requestAnimationFrame(() => {
             electrons.forEach((electron, index) => {
                 // Calculate how far into the animation the electron was (based on current 'left')
                 // This is complex because 'left' is in px and depends on container width.
                 // A simpler approach is to just restart with staggered delays, which is visually acceptable.

                 // Calculate a new delay based on its current position relative to stream width
                 const streamWidth = electronStreamContainer.offsetWidth;
                 const currentLeftPx = parseFloat(getComputedStyle(electron).left);
                 const progress = (currentLeftPx + 20) / (streamWidth + 40); // Normalize position [0, 1]

                 // Ensure progress is within [0, 1]
                 const safeProgress = Math.max(0, Math.min(1, progress));

                 // Calculate remaining time based on progress
                 const remainingTime = duration * (1 - safeProgress);

                 // Set the transition with the new duration and a potential delay offset
                 electron.style.transition = `left linear ${duration}s`;
                 // To make it look like it continues, set the delay to the remaining time but negative.
                 // If an electron was 50% through a 4s animation, its remaining time is 2s.
                 // Setting transitionDelay to -2s makes it start 2s *into* the 4s animation, effectively continuing.
                 electron.style.transitionDelay = `-${remainingTime}s`; // Start animation from current 'logical' position


                 // Set the final position
                 electron.style.left = 'calc(100% + 20px)';

                  // Add an event listener to loop the animation
                 electron.addEventListener('transitionend', function handler() {
                    // When one animation ends, reset its position and start again with a full duration and delay
                    electron.style.transition = 'none';
                    electron.style.left = '-20px';

                    requestAnimationFrame(() => {
                        requestAnimationFrame(() => {
                             electron.style.transition = `left linear ${duration}s`;
                             // Randomize start delay slightly to avoid clumping over time
                             const randomDelay = Math.random() * duration * 0.2; // up to 20% of duration
                             electron.style.transitionDelay = `${randomDelay}s`;
                             electron.style.left = 'calc(100% + 20px)';
                        });
                    });
                     // Remove the event listener so it doesn't fire multiple times for the same electron
                     electron.removeEventListener('transitionend', handler);
                 });
             });
         });
     }


    // Function to calculate resistance based on relative angle (0-180 degrees)
    // Using R = R_min + (R_max - R_min) * sin^2(angle / 2)
    function calculateResistance(angle) {
        const angleInRadians = angle * Math.PI / 180;
        const sinSqHalfAngle = Math.sin(angleInRadians / 2) ** 2;
        return R_min + (R_max - R_min) * sinSqHalfAngle;
    }

    // Function to calculate current based on resistance (Ohm's Law: I = V/R)
    function calculateCurrent(resistance) {
        if (resistance <= 0) return V_supply / 0.001; // Prevent division by zero, return a large value
        return V_supply / resistance;
    }

    // Function to update simulation display
    function updateSimulation(angle) {
        // Update free arrow rotation
        freeArrow.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`;
        angleDisplay.textContent = `${angle}°`;

        // Calculate and display resistance and current
        const resistance = calculateResistance(angle);
        const current = calculateCurrent(resistance);

        resistanceValueSpan.textContent = resistance.toFixed(1);
        currentValueSpan.textContent = current.toFixed(3);

        // Update visual flow cue: Electron animation speed and opacity
        // Map current [V_supply/R_max, V_supply/R_min] to animation duration [durationMax, durationMin]
        const currentRange = (V_supply/R_min) - (V_supply/R_max);
        const normalizedCurrent = (current - (V_supply/R_max)) / currentRange; // 0 for min current, 1 for max current

        // Map normalized current [0, 1] to duration [durationMax, durationMin]
        const animationDuration = animationDurationMax - normalizedCurrent * (animationDurationMax - animationDurationMin);
        // Ensure duration is within bounds
        const safeDuration = Math.max(animationDurationMin, Math.min(animationDurationMax, animationDuration));

        // Map normalized current [0, 1] to opacity [0.4, 1]
        const opacity = 0.4 + normalizedCurrent * 0.6; // Opacity from 0.4 (low current) to 1 (high current)
        electronStreamContainer.style.opacity = opacity;

        // Restart electron animations with the new duration
        restartElectronAnimation(safeDuration);


        // Update graph
        drawGraph(angle, resistance);
    }

    // Graph drawing function
    function drawGraph(currentAngle, currentResistance) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Graph dimensions and padding
        const padding = 40; // More padding for labels
        const graphWidth = canvas.width - 2 * padding;
        const graphHeight = canvas.height - 2 * padding;
        const originX = padding;
        const originY = canvas.height - padding;

        // Draw Axes
        ctx.beginPath();
        ctx.moveTo(originX, padding); // Y-axis start (Resistance)
        ctx.lineTo(originX, originY); // Y-axis end
        ctx.lineTo(canvas.width - padding, originY); // X-axis end (Angle)
        ctx.strokeStyle = '#555';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        // Labels
        ctx.font = '14px Arial';
        ctx.fillStyle = '#333';
        ctx.textAlign = 'center';
        ctx.fillText('זווית יחסית (°)', originX + graphWidth / 2, canvas.height - padding / 2 + 10);
        ctx.save();
        ctx.translate(padding / 2 - 5, originY - graphHeight / 2); // Adjusted position for Y label
        ctx.rotate(-Math.PI / 2);
        ctx.textAlign = 'center';
        ctx.fillText('התנגדות (Ω)', 0, 0);
        ctx.restore();

        // X-axis ticks (0, 90, 180)
        ctx.textAlign = 'center';
        ctx.fillText('0', originX, originY + 18);
        ctx.fillText('90', originX + graphWidth / 2, originY + 18);
        ctx.fillText('180', originX + graphWidth, originY + 18);

        // Y-axis ticks (R_min, R_max)
        ctx.textAlign = 'right';
        ctx.textBaseline = 'middle';

         // Mapping Resistance values [R_min, R_max] to Y coordinates [originY, padding]
         const resistanceRange = R_max - R_min;
         const yRange = originY - padding;

         const getYpos = (resistance) => {
             if (resistanceRange === 0) return originY; // Avoid division by zero if R_min == R_max
              // Linear mapping: R_min maps to originY, R_max maps to padding
             return originY - (resistance - R_min) / resistanceRange * yRange;
         }

        ctx.fillText(R_min.toFixed(0), originX - 8, getYpos(R_min));
        ctx.fillText(R_max.toFixed(0), originX - 8, getYpos(R_max));
         ctx.textBaseline = 'alphabetic'; // Reset baseline


        // Draw the resistance curve
        ctx.beginPath();
        ctx.strokeStyle = '#007bff';
        ctx.lineWidth = 3; // Thicker line

        for (let angle = 0; angle <= 180; angle += 1) { // More points for smoothness
            const resistance = calculateResistance(angle);
            const x = originX + (angle / 180) * graphWidth;
            const y = getYpos(resistance);

            if (angle === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        ctx.stroke();

        // Draw current point on the graph
        ctx.beginPath();
        const currentX = originX + (currentAngle / 180) * graphWidth;
        const currentResistanceY = getYpos(currentResistance);
        ctx.arc(currentX, currentResistanceY, 6, 0, Math.PI * 2); // Larger point
        ctx.fillStyle = 'red';
        ctx.shadowBlur = 8; // Add glow to the point
        ctx.shadowColor = 'red';
        ctx.fill();
        ctx.closePath();

        // Draw a vertical line from the point to the x-axis
        ctx.beginPath();
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]); // Dashed line
        ctx.moveTo(currentX, currentResistanceY);
        ctx.lineTo(currentX, originY);
        ctx.stroke();
        ctx.setLineDash([]); // Reset line style
        ctx.shadowBlur = 0; // Reset shadow
    }


    // Event listener for slider
    angleControl.addEventListener('input', (event) => {
        const angle = parseInt(event.target.value);
        updateSimulation(angle);
    });

    // Event listener for toggle button
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק';
    });

    // Initial setup
    updateSimulation(parseInt(angleControl.value)); // Update on page load
     // Start the electron animation loop initially
     startElectronAnimation(animationDurationMax); // Start with slowest animation

     // Make electrons loop when they finish the transition
    electrons.forEach(electron => {
        electron.addEventListener('transitionend', function handler() {
            // When one animation ends, reset its position and start again
            const currentDuration = parseFloat(electron.style.transitionDuration); // Get current speed
            electron.style.transition = 'none'; // Remove transition to reset instantly
            electron.style.left = '-20px'; // Reset position to start

            // Use requestAnimationFrame to re-enable transition after reset
            requestAnimationFrame(() => {
                 requestAnimationFrame(() => { // Double RAF for guaranteed transition reset
                    electron.style.transition = `left linear ${currentDuration}s`;
                    // Randomize start delay slightly to avoid clumping over time
                    const randomDelay = Math.random() * currentDuration * 0.2; // up to 20% of duration
                    electron.style.transitionDelay = `${randomDelay}s`;
                    electron.style.left = 'calc(100% + 20px)'; // Move to end
                 });
            });
        });
    });

</script>
---
```