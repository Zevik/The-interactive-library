---
title: "מנוע סילון: קסם של הנדסה באוויר"
english_slug: how-a-jet-engine-works-full-explanation
category: "מדעים מדויקים / פיזיקה"
tags: [מנוע סילון, פיזיקה, אווירודינמיקה, תרמודינמיקה, הנדסת תעופה]
---
# מנוע סילון: קסם של הנדסה באוויר

מפלצות הפלדה האדירות שחוצות את השמיים שוקלות מאות טונות וטסות במהירות עוצרת נשימה. מהו הכוח המסתורי שדוחף אותן קדימה ומנצח את כוח המשיכה? התשובה טמונה בליבן הפועם – מנועי הסילון העוצמתיים. בואו נצלול פנימה ונחשוף את ההנדסה הגאונית שהופכת אוויר ודלק לדחף אימתני.

<div class="jet-engine-app">
    <h2>סימולציה אינטראקטיבית: ליבת מנוע הטורבו-פאן</h2>
    <div class="engine-diagram">
        <div class="engine-part fan" data-name="מניפה קדמית">
            <div class="fan-blades"></div>
            <div class="air-inflow flow-animation"></div>
        </div>
        <div class="engine-part compressor" data-name="מדחס">
            <div class="core-blades compressor-blades"></div>
            <div class="air-flow compressed flow-animation"></div>
            <div class="pressure-temp-indicator compressed-indicator">לחץ↑ טמפ↑</div>
        </div>
        <div class="engine-part combustor" data-name="תא בעירה">
            <div class="air-flow burning flow-animation"></div>
            <div class="flame-effect"></div>
            <div class="pressure-temp-indicator burning-indicator">לחץ↑↑ טמפ↑↑↑</div>
        </div>
        <div class="engine-part turbine" data-name="טורבינה">
            <div class="core-blades turbine-blades"></div>
            <div class="air-flow expanded flow-animation"></div>
             <div class="pressure-temp-indicator turbine-indicator">לחץ↓ טמפ↓</div>
        </div>
        <div class="engine-part nozzle" data-name="נחיר פליטה">
            <div class="air-flow exhaust flow-animation"></div>
             <div class="pressure-temp-indicator exhaust-indicator">מהירות↑↑</div>
        </div>
    </div>
    <div class="controls">
        <button id="playPauseBtn">הפעל סימולציה</button>
        <label for="speedSlider">מהירות מנוע:</label>
        <input type="range" id="speedSlider" min="1" max="10" value="5">
    </div>
    <div class="part-info">לחצו על חלק במנוע כדי להבין את תפקידו</div>
    <div id="popup-info" class="popup-info"></div>
</div>

<button id="showExplanationBtn">הצג הסבר מלא: מסע בתוך המנוע</button>

<div id="fullExplanation" style="display: none;">
    <h2>מסע בתוך המנוע: איך כל חלק עובד?</h2>

    <p>מנוע סילון, ובמיוחד מנוע הטורבו-פאן הנפוץ במטוסי נוסעים מודרניים, הוא מפעל כוח ממוזער המיישם את החוקים הבסיסיים של הפיזיקה ליצירת דחף אדיר. הוא שואב כמות עצומה של אוויר מהחזית, מאיץ אותו בצורה דרמטית ופולט אותו מאחור במהירות גבוהה. השינוי העצום בתנע של האוויר הנע הוא שיוצר את הכוח המניע את המטוס.</p>

    <h3>העיקרון המנחה: החוק השלישי של ניוטון בפעולה</h3>
    <p>פעולת מנוע הסילון היא המחשה מרהיבה של החוק השלישי של ניוטון: "לכל פעולה קיימת תגובה שווה ומנוגדת". המנוע דוחף ומאיץ מסה אדירה של אוויר בכיוון אחד (אחורה), וכתוצאה מכך מקבל כוח דחף שווה בגודלו ומנוגד בכיוונו (קדימה) שמניע את המטוס כולו.</p>

    <h3>ארבעת הצעדים לדחף</h3>
    <p>האוויר שעובר דרך ליבת המנוע עובר סדרה של תהליכים מרכזיים, המכונים לעיתים "מחזור ברייטון" או "מחזור ג'ול":</p>
    <ol>
        <li><strong>יניקה (Intake):</strong> אוויר נכנס לחזית המנוע במהירות גבוהה אך בלחץ וטמפרטורה רגילים (אוויר הסביבה).</li>
        <li><strong>דחיסה (Compression):</strong> האוויר נדחס בסדרה של שלבים ללחץ גבוה מאוד, דבר שמעלה גם את הטמפרטורה שלו משמעותית.</li>
        <li><strong>בעירה (Combustion):</strong> דלק מוזרק לאוויר הדחוס והחם ונשרף בלחץ קבוע (או כמעט קבוע). שריפה זו מעלה את הטמפרטורה של הגזים לרמות קיצוניות.</li>
        <li><strong>התפשטות (Expansion) ופליטה (Exhaust):</strong> הגזים החמים והדחוסים מתפשטים במהירות, עוברים דרך הטורבינה (שמפיקה אנרגיה להנעת המדחס והמניפה) ולבסוף מואצים החוצה דרך נחיר הפליטה ליצירת הדחף העיקרי.</li>
    </ol>

    <h3>רכיבי הליבה: שחקני המפתח</h3>
    <ul>
        <li><strong>כונס אוויר (Inlet):</strong> הפתח הקדמי דרכו נכנס האוויר. מתוכנן להאט את האוויר ולאפשר זרימה אחידה לתוך המניפה.</li>
        <li><strong>מניפה קדמית (Fan):</strong> החלק הגדול והבולט ביותר בחזית מנועי טורבו-פאן מודרניים. להביה הענקיים יונקים אוויר רב. רוב האוויר (ה"בייפס") עובר במסלול חיצוני, עוקף את ליבת המנוע ויוצר חלק ניכר מהדחף הכולל. חלק קטן יותר נכנס לליבה להמשך התהליך.</li>
        <li><strong>מדחס (Compressor):</strong> סדרה של דיסקים מסתובבים עם להבים (רוטורים) ודיסקים קבועים עם להבים (סטטורים). כל שלב מעלה את לחץ וטמפרטורת האוויר. מדחסים מודרניים יכולים להעלות את הלחץ פי 30 ואף יותר!</li>
        <li><strong>תא בעירה (Combustor):</strong> מבנה טבעתי או קני שבו מתרחשת שריפת הדלק באופן רציף ויציב. דלק מוזרק דרך מזרקים ומעורבב עם האוויר הדחוס והחם. השריפה מייצרת גזי פליטה לוהטים בטמפרטורות שיכולות להגיע ל-1500-2000 מעלות צלזיוס ויותר.</li>
        <li><strong>טורבינה (Turbine):</strong> ממוקמת מיד לאחר תא הבעירה. הגזים הלוהטים עוברים דרך סדרה של להבי טורבינה ומסובבים אותם במהירות עצומה. הטורבינה למעשה "שואבת" אנרגיה מהגזים המתפשטים. ציר הטורבינה מחובר ישירות לציר המדחס (ולעיתים גם לציר המניפה) ומספק את האנרגיה הדרושה להנעתם - הישג הנדסי מדהים, שכן הטורבינה מייצרת יותר אנרגיה ממה שהמדחס והמניפה צורכים!</li>
        <li><strong>נחיר פליטה (Nozzle):</strong> החלק האחורי והצר יחסית של המנוע. כאן גזי הפליטה המואצים יוצאים לחלל החיצון במהירות גבוהה מאוד. צורת הנחיר (מתכנסת או מתרחבת) משפיעה על מהירות ויצירת הדחף הסופי.</li>
    </ul>

    <h3>זרימת האנרגיה והכוח</h3>
    <p>כפי שצוין, הטורבינה היא זו שמניעה את חלקי המנוע הקדמיים. היא מפיקה אנרגיה מהתפשטות הגזים החמים, והאנרגיה הזו מועברת דרך ציר מרכזי לסיבוב המדחס והמניפה. המנוע למעשה מקיים את עצמו אנרגטית לאחר ההצתה הראשונית, כאשר כל האנרגיה לתפעול החלקים הפנימיים מגיעה מגזי הפליטה הלוהטים עצמם, לפני שהם מייצרים את הדחף העיקרי.</p>

    <h3>סוגים שונים של מנועי סילון</h3>
    <p>בעוד שהעיקרון הבסיסי דומה, קיימים סוגים שונים של מנועי סילון המותאמים לצרכים שונים: טורבו-ג'ט (הסוג המקורי, כל האוויר עובר דרך הליבה, יעיל במהירויות על-קוליות), טורבו-פאן (הנפוץ ביותר במטוסי נוסעים, בעל יחס בייפס גבוה, יעיל במהירויות תת-קוליות), טורבו-פרופ (הטורבינה מניעה מדחף רגיל, יעיל במהירויות נמוכות), וטורבו-שפט (הטורבינה מניעה ציר המחובר לגוף אחר, כמו רוטור של מסוק).</p>

    <h3>לסיכום: פלא של פיזיקה והנדסה</h3>
    <p>מנוע הסילון הוא דוגמה מופתית לשילוב של פיזיקה תרמודינמית, מכניקה ואווירודינמיקה. על ידי שליטה מדויקת על זרימת האוויר, דחיסתו, שריפת דלק בו, והאצת התוצר החוצה, המנוע מצליח לייצר כוח דחף אדיר המאפשר למטוסים מודרניים לכבוש את השמיים במהירות וביעילות מרשימות.</p>
</div>

<style>
    :root {
        /* CSS Variables for JS control */
        --airflow-duration: 5s; /* Default medium speed */
        --airflow-slow-duration: 7.5s; /* Default slower for fan */
        --rotation-duration: 1s; /* Base rotation speed */
        --flame-intensity: 1; /* Base flame effect intensity */
        --indicator-intensity: 1; /* Base indicator visibility/animation */
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f4f4;
    }

    .jet-engine-app {
        border: 1px solid #ccc;
        border-radius: 12px;
        padding: 30px 20px;
        margin: 30px 0;
        background: linear-gradient(to bottom, #e0e0e0, #ffffff);
        text-align: center;
        overflow: hidden;
        position: relative;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }

    .jet-engine-app h2 {
        color: #004080;
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 1.8em;
    }

    .engine-diagram {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px;
        height: 180px; /* Slightly taller */
        position: relative;
        perspective: 800px; /* For 3D effects */
    }

    .engine-part {
        height: 100px; /* Base height */
        border: 1px solid #555;
        position: relative;
        display: flex;
        flex-direction: column; /* Stack internal elements */
        align-items: center;
        justify-content: center;
        font-size: 0.8em;
        cursor: pointer;
        transition: all 0.3s ease; /* Smooth transitions for hover/state changes */
        color: #333;
        box-sizing: border-box; /* Include border in size */
        text-shadow: 0 0 2px rgba(255, 255, 255, 0.7);
    }

    .engine-part:hover {
        background-color: #dcdcdc;
        transform: translateY(-5px); /* Slight lift on hover */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    /* Specific part styling */
    .fan {
        width: 100px; /* Wider fan */
        height: 150px; /* Much taller */
        border-radius: 15px 0 0 15px;
        background: linear-gradient(to right, #b0b0b0, #e0e0e0);
        z-index: 2; /* Place fan in front */
        overflow: hidden; /* Hide rotating blades overflow */
    }

     .fan-blades, .core-blades {
         position: absolute;
         width: 100%;
         height: 100%;
         background-size: cover; /* Or contain depending on image/pattern */
         animation: rotate var(--rotation-duration) linear infinite paused; /* Initial state paused */
         z-index: 1; /* Below airflow */
     }

    .fan-blades {
         /* Using a simple striped pattern to represent blades */
         background: repeating-linear-gradient(45deg, transparent, transparent 5%, rgba(0, 0, 0, 0.2) 5%, rgba(0, 0, 0, 0.2) 10%);
         width: 150%; /* Make it larger than parent for rotation effect */
         height: 150%;
         top: -25%;
         left: -25%;
         border-radius: 50%; /* Spin effect */
         animation-timing-function: ease-out; /* Slower start/end */
    }

     .compressor-blades {
         background: repeating-linear-gradient(90deg, transparent, transparent 3%, rgba(50, 50, 150, 0.1) 3%, rgba(50, 50, 150, 0.1) 6%);
     }

     .turbine-blades {
         background: repeating-linear-gradient(90deg, transparent, transparent 3%, rgba(150, 50, 50, 0.1) 3%, rgba(150, 50, 50, 0.1) 6%);
     }


    .compressor {
        width: 120px;
        background: linear-gradient(to right, #d0d0d0, #f0f0f0);
        border-left: none;
        border-right: none;
        overflow: hidden;
    }

    .combustor {
        width: 90px;
        background: linear-gradient(to right, #ffc000, #ff8000); /* Warmer colors */
        color: white;
        text-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
        overflow: hidden;
    }

     .flame-effect {
         position: absolute;
         width: 100%;
         height: 100%;
         background: radial-gradient(circle at center, rgba(255, 165, 0, 0.8) 0%, rgba(255, 69, 0, 0.6) 40%, rgba(255, 0, 0, 0.4) 70%, transparent 100%);
         opacity: calc(0.5 + var(--flame-intensity) * 0.5); /* Opacity based on intensity */
         animation: pulse-flame 1s infinite alternate paused; /* Initial state paused */
         z-index: 1;
     }

     @keyframes pulse-flame {
        0% { transform: scale(0.9); opacity: 0.7; }
        100% { transform: scale(1); opacity: 1; }
     }


    .turbine {
        width: 120px;
        background: linear-gradient(to right, #f0e0d0, #d0c0a0);
        border-left: none;
        border-right: none;
         overflow: hidden;
    }

    .nozzle {
        width: 80px; /* Wider nozzle */
        height: 100px; /* Base height */
        border-radius: 0 15px 15px 0;
        background: linear-gradient(to right, #e0e0e0, #b0b0b0);
        position: relative;
        overflow: hidden; /* Hide airflow overflow */
    }

    /* Airflow animation styling */
    .flow-animation {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        z-index: 2; /* Above blades/flames */
    }

    .flow-animation::before {
        content: ' ';
        position: absolute;
        width: 200%; /* Wider than parent */
        height: 100%;
        animation: airflow linear infinite paused; /* Initial state paused */
        background-size: 50% 100%; /* Control pattern density */
    }

    /* Specific airflow colors/patterns */
    .air-inflow.flow-animation::before {
         background: repeating-linear-gradient(90deg, rgba(150, 150, 255, 0.2), rgba(150, 150, 255, 0.2) 5%, transparent 5%, transparent 10%);
         animation-duration: var(--airflow-slow-duration);
    }

    .compressed.flow-animation::before {
         background: repeating-linear-gradient(90deg, rgba(50, 50, 200, 0.3), rgba(50, 50, 200, 0.3) 8%, transparent 8%, transparent 16%);
         animation-duration: var(--airflow-duration);
    }

    .burning.flow-animation::before {
         background: repeating-linear-gradient(90deg, rgba(255, 100, 0, 0.5), rgba(255, 100, 0, 0.5) 10%, transparent 10%, transparent 20%);
         animation-duration: var(--airflow-duration);
    }

    .expanded.flow-animation::before {
         background: repeating-linear-gradient(90deg, rgba(255, 150, 50, 0.4), rgba(255, 150, 50, 0.4) 8%, transparent 8%, transparent 16%);
         animation-duration: var(--airflow-duration);
    }

    .exhaust.flow-animation::before {
         background: repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5) 5%, transparent 5%, transparent 10%);
         animation-duration: var(--airflow-duration); /* Exhaust speed directly linked to airflow */
    }


    @keyframes airflow {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }

     @keyframes rotate {
         0% { transform: rotate(0deg); }
         100% { transform: rotate(360deg); }
     }


    .pressure-temp-indicator {
        position: absolute;
        top: -25px; /* Position above the part */
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.95);
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8em;
        white-space: nowrap;
        border: 1px solid #555;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        z-index: 3; /* Above other elements */
        opacity: calc(0.8 + var(--indicator-intensity) * 0.2); /* Intensity based on speed */
        transition: opacity 0.3s ease;
    }

     .compressed-indicator { border-color: #3232c8; color: #1e1e7a; }
     .burning-indicator { border-color: #ff6600; color: #cc5200; font-weight: bold; }
     .turbine-indicator { border-color: #d08032; color: #a46728; }
     .exhaust-indicator { border-color: #a0a0a0; color: #555; font-weight: bold; }


    .controls {
        margin-top: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .controls button {
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #007bff;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .controls button:hover {
        background-color: #0056b3;
    }
     .controls button:active {
         transform: scale(0.98);
     }


    .controls label {
        font-size: 1em;
        color: #555;
    }

    .controls input[type="range"] {
        width: 150px;
        cursor: grab;
    }
     .controls input[type="range"]:active {
         cursor: grabbing;
     }


    .part-info {
        margin-top: 20px;
        font-style: italic;
        color: #666;
        min-height: 20px; /* Reserve space */
    }

    .popup-info {
        position: absolute;
        bottom: 10px; /* Position below the diagram */
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(0, 0, 0, 0.85);
        color: white;
        padding: 10px 15px;
        border-radius: 8px;
        font-size: 0.9em;
        z-index: 10;
        display: none; /* Hidden by default */
        white-space: nowrap;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: opacity 0.3s ease;
    }

    #showExplanationBtn {
        display: block;
        width: fit-content;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #28a745;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
     #showExplanationBtn:hover {
         background-color: #218838;
     }
     #showExplanationBtn:active {
         transform: scale(0.98);
     }


    #fullExplanation {
        border-top: 2px solid #007bff;
        margin-top: 40px;
        padding-top: 30px;
        text-align: left;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    #fullExplanation h2 {
        text-align: center;
        color: #004080;
        margin-bottom: 20px;
        font-size: 1.6em;
    }
     #fullExplanation h3 {
         text-align: left;
         color: #0056b3;
         margin-top: 20px;
         margin-bottom: 10px;
         font-size: 1.3em;
         border-bottom: 1px dotted #ccc;
         padding-bottom: 5px;
     }

    #fullExplanation p, #fullExplanation ul, #fullExplanation ol {
        margin-bottom: 15px;
        color: #555;
    }

     #fullExplanation ul li, #fullExplanation ol li {
         margin-bottom: 8px;
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const playPauseBtn = document.getElementById('playPauseBtn');
        const speedSlider = document.getElementById('speedSlider');
        const engineParts = document.querySelectorAll('.engine-part');
        const popupInfo = document.getElementById('popup-info');
        const showExplanationBtn = document.getElementById('showExplanationBtn');
        const fullExplanationDiv = document.getElementById('fullExplanation');
        const animatableElements = document.querySelectorAll('.flow-animation::before, .fan-blades, .core-blades, .flame-effect, .pressure-temp-indicator'); // Correct selector for parent elements that contain animatable children/pseudo elements


        let isPlaying = false; // Start paused
        let animationSpeed = 5; // Default speed (1-10)
        let popupTimeoutId = null;

        // Function to update animation speeds using CSS variables
        function updateAnimationSpeed() {
             // Speed slider value 1-10 maps to duration (slower=longer duration)
             // Let's map 10 (max speed) to 1s duration, 1 (min speed) to 10s duration
             const duration = 11 - animationSpeed; // 10 -> 1s, 5 -> 6s, 1 -> 10s
             const slowDuration = duration * 1.5; // Fan/Inflow is relatively slower
             const rotationDuration = (11 - animationSpeed) / 2; // Blades spin faster
             const flameDuration = (11 - animationSpeed) / 5; // Flame flickers faster at high speed
             const indicatorIntensity = animationSpeed / 10; // Indicators brighter/more active at high speed

             document.documentElement.style.setProperty('--airflow-duration', `${duration}s`);
             document.documentElement.style.setProperty('--airflow-slow-duration', `${slowDuration}s`);
             document.documentElement.style.setProperty('--rotation-duration', `${rotationDuration < 0.2 ? 0.2 : rotationDuration}s`); // Prevent extremely fast rotation
             document.documentElement.style.setProperty('--flame-intensity', `${indicatorIntensity}`);
             document.documentElement.style.setProperty('--indicator-intensity', `${indicatorIntensity}`);


             // Update animation-duration for elements where it's set directly (like the flame pulse)
             document.querySelector('.flame-effect').style.animationDuration = `${flameDuration < 0.1 ? 0.1 : flameDuration}s`;
             document.querySelectorAll('.pressure-temp-indicator').forEach(el => {
                 // Could add specific indicator pulse animations here and control their speed/intensity
             });
        }

        // Function to toggle animation play state
        function toggleAnimation(play) {
             isPlaying = play !== undefined ? play : !isPlaying; // Allow forcing state
             playPauseBtn.textContent = isPlaying ? 'השהה סימולציה' : 'הפעל סימולציה';

             const playState = isPlaying ? 'running' : 'paused';

             // Apply play state to parent elements whose children/pseudo elements are animated
             document.querySelectorAll('.flow-animation, .fan-blades, .core-blades, .flame-effect, .pressure-temp-indicator').forEach(el => {
                  if(el.style.animationPlayState !== undefined) { // Check if supported
                       el.style.animationPlayState = playState;
                  }
             });
        }

        // Initial state: Start paused, set initial speed visuals
        updateAnimationSpeed();
        toggleAnimation(false); // Ensure initial state is paused

        // Event listeners
        playPauseBtn.addEventListener('click', () => toggleAnimation());

        speedSlider.addEventListener('input', (event) => {
            animationSpeed = parseInt(event.target.value);
            updateAnimationSpeed();
            // Animation play state is maintained by the toggle button click state
        });

        engineParts.forEach(part => {
            part.addEventListener('click', () => {
                const partName = part.getAttribute('data-name');
                let info = '';
                switch (partName) {
                    case 'מניפה קדמית':
                        info = 'הלב שנושם: יונקת אוויר עצום; רובו עוקף (דחף בייפאס).';
                        break;
                    case 'מדחס':
                        info = 'המכווץ העוצמתי: דוחס אוויר ללחץ וטמפרטורה קיצוניים.';
                        break;
                    case 'תא בעירה':
                        info = 'הכור הלוהט: דלק + אוויר דחוס = גזים לוהטים בלחץ גבוה.';
                        break;
                    case 'טורבינה':
                        info = 'מכונת הכוח: מופעלת ע"י גזים לוהטים, מניעה מדחס ומניפה.';
                        break;
                    case 'נחיר פליטה':
                        info = 'המאיץ הסופי: פולט גזים במהירות שיא ליצירת הדחף האדיר.';
                        break;
                    default:
                        info = 'לחץ על חלק במנוע לקבלת מידע';
                }
                popupInfo.textContent = partName + ": " + info;
                popupInfo.style.display = 'block';

                // Clear previous timeout if exists
                if (popupTimeoutId) {
                    clearTimeout(popupTimeoutId);
                }
                // Set new timeout to hide popup after 4 seconds
                popupTimeoutId = setTimeout(() => {
                    popupInfo.style.display = 'none';
                    popupTimeoutId = null; // Reset timeout ID
                }, 4000);
            });
        });

        // Hide popup if clicking anywhere else besides parts/popup
        document.addEventListener('click', (event) => {
            if (!event.target.closest('.engine-part') && !event.target.closest('.popup-info') && popupInfo.style.display !== 'none') {
                 if (popupTimeoutId) {
                     clearTimeout(popupTimeoutId);
                     popupTimeoutId = null;
                 }
                 popupInfo.style.display = 'none';
            }
        });


        showExplanationBtn.addEventListener('click', () => {
            const isHidden = fullExplanationDiv.style.display === 'none';
            fullExplanationDiv.style.display = isHidden ? 'block' : 'none';
            showExplanationBtn.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג הסבר מלא: מסע בתוך המנוע';
        });

    });
</script>
---
```