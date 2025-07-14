---
title: "החיים המופלאים של שושנת הים: מסע הרבייה הסודי"
english_slug: the-amazing-life-of-the-sea-anemone-journey-of-reproduction
category: "ביולוגיה"
tags:
  - שושנת ים
  - מחזור חיים
  - רבייה
  - ביולוגיה ימית
  - רבייה אל-זוויגית
  - רבייה זוויגית
---
# החיים המופלאים של שושנת הים: מסע הרבייה הסודי

שושנות ים... הן נראות כמו יצירות אמנות של הטבע, פורחות בשלל צבעים על קרקעית הים, נכון? אבל אל תתנו למראה הצמחי לבלבל אתכם – הן בעלי חיים אמיתיים! ואף על פי שהן נראות מעוגנות ונייחות, הן מצאו דרכים מדהימות להתפשט ולשגשג ברחבי האוקיינוסים. מוכנים לצלול למסע הרבייה המרתק שלהן?

<div id="anemone-simulation">
    <div class="controls mode-selection">
        <h2>בחרו את מסלול ההתרבות:</h2>
        <button id="asexual-btn" class="active">שיבוט (אל-זוויגית)</button>
        <button id="sexual-btn">מסע הדורות (זוויגית)</button>
    </div>
    <div class="simulation-area">
        <canvas id="anemone-canvas" width="700" height="450"></canvas>
        <div id="stage-text"></div>
         <div id="sea-floor"></div> <!-- Added for visual depth -->
    </div>
    <div class="controls animation-controls">
        <h2>שליטה בזמן:</h2>
        <button id="play-pause-btn" class="control-btn">התחל</button>
        <button id="step-btn" class="control-btn">צעד הבא</button>
        <button id="reset-btn" class="control-btn">התחל מחדש</button>
        <label for="speed-slider">מהירות:</label>
        <input type="range" id="speed-slider" min="1" max="10" value="5">
    </div>
</div>

<style>
    /* הוספת גופנים מודרניים */
    body {
        font-family: 'Arial', sans-serif; /* Keep Arial as fallback */
    }

    #anemone-simulation {
        direction: rtl; /* Ensure RTL layout */
        font-family: 'Arial', sans-serif;
        border: 1px solid #b3e5fc; /* Light blue border */
        padding: 20px;
        margin: 30px auto; /* More margin */
        max-width: 850px; /* Slightly wider container */
        background-color: #e1f5fe; /* Lighter blue background */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 4px 4px 15px rgba(0,0,0,0.1); /* Enhanced shadow */
        overflow: hidden; /* Prevent content overflow */
        position: relative;
    }

    h1, h2 {
        color: #01579b; /* Darker blue for headers */
        text-align: center;
        margin-bottom: 20px;
    }

    .controls {
        margin-top: 20px; /* Space from simulation */
        text-align: center;
    }

    .controls.mode-selection button {
        padding: 10px 20px; /* Larger buttons */
        margin: 0 10px;
        cursor: pointer;
        border: 2px solid #0277bd; /* Medium blue border */
        background-color: #b3e5fc; /* Light blue button background */
        color: #01579b; /* Dark blue text */
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition and slight press effect */
        font-size: 1.1em;
        font-weight: bold;
    }

    .controls.mode-selection button:hover:not(.active) {
        background-color: #81d4fa; /* Lighter blue on hover */
        transform: translateY(-2px); /* Slight lift on hover */
    }

    .controls.mode-selection button.active {
        background-color: #0277bd; /* Medium blue active */
        color: white;
        border-color: #01579b; /* Dark blue border for active */
        box-shadow: inset 0 0 8px rgba(0,0,0,0.2); /* Inner shadow for active */
    }

     .controls.animation-controls {
         background-color: #ffffff; /* White background for controls */
         padding: 15px;
         border-radius: 8px;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
         display: flex; /* Use flexbox for layout */
         justify-content: center; /* Center items horizontally */
         align-items: center; /* Vertically align items */
         flex-wrap: wrap; /* Allow wrapping on smaller screens */
         gap: 15px; /* Space between items */
     }

    .controls.animation-controls .control-btn {
        padding: 10px 20px;
        cursor: pointer;
        border: none; /* No border */
        background-color: #4fc3f7; /* Light cyan */
        color: #004d40; /* Dark cyan */
        border-radius: 5px;
        font-size: 1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .controls.animation-controls .control-btn:hover {
        background-color: #29b6f6; /* Slightly darker cyan on hover */
        transform: translateY(-2px);
    }

    .controls.animation-controls .control-btn:active {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

     .controls.animation-controls label {
         font-weight: bold;
         color: #01579b;
     }


    .simulation-area {
        position: relative;
        margin: 20px auto;
        border: 2px solid #0288d1; /* Deeper blue border */
        background: linear-gradient(to bottom, #e0f7fa 0%, #b2ebf2 50%, #80deea 100%); /* Gradient for water depth */
        overflow: hidden;
        width: 700px; /* Match canvas width */
        height: 450px; /* Match canvas height */
        border-radius: 8px; /* Rounded corners */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow */
    }

    #anemone-canvas {
        display: block;
        background-color: transparent;
        position: relative; /* Allows canvas to be part of the flow */
         z-index: 2; /* Ensure canvas is above background elements */
    }

    #sea-floor {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 60px; /* Height of the floor */
        background: linear-gradient(to top, #5d4037 0%, #795548 50%, #a1887f 100%); /* Brown/grey gradient for floor */
        z-index: 1; /* Ensure floor is below canvas drawing */
    }

    #stage-text {
        position: absolute;
        top: 15px; /* Position at the top */
        left: 15px; /* Position on the left */
        background-color: rgba(255, 255, 255, 0.85); /* More opaque background */
        padding: 8px 15px;
        border-radius: 6px;
        font-size: 1em;
        font-weight: bold;
        color: #01579b;
        z-index: 3; /* Ensure text is above everything */
        /* Add a simple fade transition if possible via JS, otherwise rely on content change */
    }

    #speed-slider {
        vertical-align: middle;
        width: 120px; /* Fixed width for slider */
         accent-color: #0277bd; /* Color the slider thumb/track */
    }


    #explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More margin */
        padding: 12px 25px; /* Larger button */
        cursor: pointer;
        background-color: #388e3c; /* Green */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #explanation-button:hover {
        background-color: #2e7d32; /* Darker green */
        transform: translateY(-2px);
    }
     #explanation-button:active {
         transform: translateY(0);
     }

    #explanation {
        margin-top: 20px;
        padding: 25px; /* More padding */
        border: 1px solid #b3e5fc;
        background-color: #e1f5fe; /* Match simulation background */
        border-radius: 12px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
        line-height: 1.7; /* Improved readability */
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: #01579b;
        margin-bottom: 15px;
        border-bottom: 1px solid #b3e5fc; /* Subtle separator */
        padding-bottom: 5px;
    }

    #explanation p {
        margin-bottom: 18px;
    }

     #explanation ul {
         margin-bottom: 18px;
         padding-right: 20px; /* Add padding for list markers */
     }

     #explanation li {
         margin-bottom: 8px;
     }


    /* Rule added for hiding explanation */
    .hidden {
        display: none;
        opacity: 0; /* Use opacity for potential fade effect */
        transition: opacity 0.5s ease;
    }

     /* Show state for potential fade-in */
     .visible {
         display: block;
         opacity: 1;
     }


</style>

<button id="explanation-button">גלו את הסודות: הסבר מפורט</button>

<div id="explanation" class="hidden">
    <h2>צלילה לעומק: המסע המופלא של שושנת הים</h2>

    <p>שושנות ים (Sea Anemones) הן אולי אחד היצורים הימיים הכי פוטוגניים שיש! הן שייכות למערכת הנבוביתיים (Cnidaria), משפחה שכוללת גם את המדוזות המרחפות ואת האלמוגים בוני השוניות. למרות המראה העדין והדומם שלהן, הן טורפות פעילות, רובן מקובעות לקרקעית הים (בשלב הפוליפ) ומשתמשות בזרועותיהן המצוידות בתאי עוקץ (נמטוציסטים) כדי ללכוד טרף קטן.</p>

    <p>היותן יצורים ישיבים מציבה בפניהן אתגר מיוחד בכל הקשור להתרבות והתפשטות. הטבע העניק להן מגוון מדהים של אסטרטגיות רבייה, המבטיחות את המשך קיומן בבתי גידול מגוונים באוקיינוס.</p>

    <h3>רבייה ללא שותף: קסם השיבוט (רבייה אל-זוויגית)</h3>
    <p>דמיינו ששושנת ים יכולה פשוט לשכפל את עצמה! רבייה אל-זוויגית מאפשרת בדיוק את זה – יצירת עותקים גנטיים מושלמים (שיבוטים) של שושנת האם. זוהי אסטרטגיה יעילה ביותר כאשר התנאים הסביבתיים אידיאליים, והתכונות של שושנת האם מוצלחות במיוחד. שתי שיטות עיקריות בולטות:</p>
    <ul>
        <li>**הנצה (Budding):** כמו צמח שמצמיח ניצן חדש. שושנת הים מפתחת בליטה קטנה על גופה. הבליטה גדלה, מקבלת צורה של שושנה מיניאטורית עם זרועות ופה, ולבסוף נפרדת משושנת האם והופכת לפוליפ עצמאי וזהה לה לחלוטין.</li>
        <li>**חלוקה (Fission):** פשוטו כמשמעו - שושנת הים מתחלקת! החלוקה יכולה להיות לאורך (אורכית), ואז השושנה נמתחת ומתפצלת לשתיים, או לרוחב (רוחבית), ואז חלק עליון נפרד מהתחתון. כל חלק משלים את האיברים החסרים ומתפתח לשושנה שלמה ועצמאית.</li>
    </ul>
    <p>היתרון הגדול ברבייה אל-זוויגית הוא המהירות והיכולת לייצר הרבה צאצאים מפרט אחד בלי לחפש שותף. אבל יש גם חיסרון – כל הצאצאים זהים גנטית, מה שהופך אותם לפגיעים יותר למחלות או שינויים סביבתיים שהמין לא מותאם אליהם.</p>

    <h3>רבייה עם שותף: מסע התקווה (רבייה זוויגית)</h3>
    <p>כמו רוב בעלי החיים המוכרים לנו, גם שושנות ים יכולות להתרבות באופן זוויגי, מה שמוסיף גיוון גנטי קריטי לאוכלוסייה ומאפשר פיזור למרחקים. זהו מסע ארוך ומורכב יותר:</p>
    <ul>
        <li>**טקס שחרור תאי רבייה (Spawning):** בזמנים מסוימים בשנה, שושנות ים (זכרים ונקבות, תלוי במין) משחררות כמויות עצומות של תאי רבייה (זרע וביציות) ישירות למי הים. לעיתים קרובות זה קורה בו זמנית אצל שושנות רבות כדי להגדיל את הסיכוי למפגש.</li>
        <li>**פגישה במים: הפריה (Fertilization):** בתוך המים הפתוחים, תאי הזרע פוגשים את הביציות ומפרים אותן. מהאיחוי נוצרת הזיגוטה – התא הראשון של שושנת הים החדשה.</li>
        <li>**מפלאנולה לפוליפ: המטמורפוזה הגדולה:** הזיגוטה מתחילה להתחלק ומתפתחת לפגית זעירה, דמוית ריסנית ושחיינית, הנקראת פלאנולה (Planula). הפלאנולה היא שלב "הנוודות" של שושנת הים. היא נסחפת בזרמי הים, לעיתים למרחקים אדירים, ומאפשרת למין להתיישב במקומות חדשים.</li>
        <li>**התיישבות והתבגרות:** לאחר תקופת שחייה, הפלאנולה מוצאת משטח מתאים (סלע, אלמוג, קונכייה) להתיישב עליו. מרגע ההתיישבות מתרחשת מטמורפוזה דרמטית – הפלאנולה משנה את צורתה מפגית שחיינית לפוליפ זעיר, המעגן את עצמו למצע ומתחיל לפתח זרועות. פוליפ צעיר זה גדל לאט לאט לשושנת ים בוגרת, מוכנה למסע הרבייה של הדור הבא.</li>
    </ul>
    <p>היתרונות של רבייה זוויגית ברורים: היא מייצרת גיוון גנטי שמסייע למנוע להסתגל לשינויים, ושלב הפגית השחיינית מאפשר פיזור נרחב ויכולת כיבוש בתי גידול חדשים.</p>

    <h3>האסטרטגיה המנצחת: גם וגם!</h3>
    <p>רוב שושנות הים מסוגלות להשתמש בשתי שיטות הרבייה. הגמישות הזו היא ככל הנראה אחד הסודות להצלחתן האקולוגית. רבייה אל-זוויגית מאפשרת גידול מהיר של אוכלוסיות במקום נוח, בעוד שרבייה זוויגית מבטיחה עמידות לאורך דורות ויכולת הגעה למקומות חדשים. הצצה למחזורי החיים הללו היא תזכורת מופלאה לכוחה ולמגוון של האבולוציה בעולם התת-ימי!</p>
</div>


<script>
    const canvas = document.getElementById('anemone-canvas');
    const ctx = canvas.getContext('2d');
    const asexualBtn = document.getElementById('asexual-btn');
    const sexualBtn = document.getElementById('sexual-btn');
    const playPauseBtn = document.getElementById('play-pause-btn');
    const stepBtn = document.getElementById('step-btn');
    const resetBtn = document.getElementById('reset-btn');
    const speedSlider = document.getElementById('speed-slider');
    const stageTextDiv = document.getElementById('stage-text');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('explanation');
    const seaFloorDiv = document.getElementById('sea-floor');


    let currentMode = 'asexual'; // 'asexual' or 'sexual'
    let animationState = 0; // 0: stopped, 1: playing, 2: paused
    let currentStep = 0;
    let animationSpeed = 5; // Corresponds to slider value
    let lastTimestamp = 0;
    let frameDuration = 2000 / animationSpeed; // milliseconds per step progression

    // Animation Variables (for smooth transitions within steps)
    let animationProgress = 0; // 0 to 1, progress within the current step
    let animationDuration = 1000; // Base duration for step animations
    let isAnimatingStep = false;


    const asexualSteps = [
        "התחלה: שושנת ים בוגרת עוגנת",
        "שיבוט מתחיל: הנצה או חלוקה",
        "התהליך מתקדם: ניצן גדל / הגוף מתחלק",
        "שושנות חדשות נוצרות: כמעט עצמאיות",
        "דור חדש: שושנות עצמאיות וזהות"
    ];

    const sexualSteps = [
        "הורים בוגרים: מוכנים למסע",
        "שחרור תאי רבייה: המים מתמלאים בחיים",
        "הפריה: זרע פוגש ביצית, נוצרת זיגוטה",
        "התפתחות לפגית: מתחילים לקרום עור וגידים",
        "שלב הניידות: פגית פלאנולה שחיינית נודדת",
        "נחיתה רכה: הפגית מוצאת בית ומתיישבת",
        "מטמורפוזה: הפגית הופכת לפוליפ צעיר",
        "גדילה: הפוליפ הצעיר הופך לשושנה בוגרת"
    ];

     // Anemone colors
     const ANEMONE_COLORS = {
         body: '#ff69b4', // Hot pink
         base: '#a0522d', // Sienna
         tentacles: '#ffb6c1' // Light pink
     };
     const ANEMONE_COLORS_VARIANT = {
         body: '#90ee90', // Light green
         base: '#8fbc8f', // Dark sea green
         tentacles: '#98fb98' // Pale green
     };


    function drawAnemone(ctx, x, y, size, colors = ANEMONE_COLORS, tentacles = 12, baseHeight = 0.3, sway = 0) {
         // Base (simple, slightly conical)
         const baseWidth = size * 1.2;
         const baseBottomY = y + size * baseHeight * 2; // Base bottom position
         const baseTopY = y + size * baseHeight; // Base top position
         ctx.fillStyle = colors.base;
         ctx.beginPath();
         ctx.moveTo(x - baseWidth/2, baseBottomY);
         ctx.lineTo(x + baseWidth/2, baseBottomY);
         ctx.lineTo(x + size * 0.6, baseTopY); // Slightly narrower top
         ctx.lineTo(x - size * 0.6, baseTopY);
         ctx.closePath();
         ctx.fill();

        // Body (more rounded top)
        const bodyTopY = y + size * 0.2;
        ctx.beginPath();
        // Adjust control points for more organic shape, add sway effect
         const swayAmount = size * 0.1 * sway; // Sway based on progress
        ctx.moveTo(x - size * 0.8 + swayAmount, baseTopY);
        ctx.quadraticCurveTo(x - size + swayAmount, bodyTopY, x - size * 0.7 + swayAmount, bodyTopY - size * 0.4); // Left side curve
        ctx.quadraticCurveTo(x + swayAmount, y - size, x + size * 0.7 + swayAmount, bodyTopY - size * 0.4); // Top curve
        ctx.quadraticCurveTo(x + size + swayAmount, bodyTopY, x + size * 0.8 + swayAmount, baseTopY); // Right side curve
        ctx.closePath();
        ctx.fillStyle = colors.body;
        ctx.fill();
        ctx.strokeStyle = colors.body; // Match border to fill for soft look
        ctx.lineWidth = 1;
        ctx.stroke();

        // Tentacles (swaying)
        const tentacleBaseY = bodyTopY - size * 0.2; // Position above the body peak
        const tentacleLength = size * 0.8;
        const tentacleSway = size * 0.05 * sway; // Tentacle sway based on progress

        for (let i = 0; i < tentacles; i++) {
            const angle = (i / tentacles) * Math.PI * 2 - Math.PI / 2; // Start from top, go clockwise
            const startX = x + Math.cos(angle) * size * 0.7 + swayAmount;
            const startY = tentacleBaseY + Math.sin(angle) * size * 0.4; // Starting slightly lower on the body
            const endX = x + Math.cos(angle) * (size * 0.7 + tentacleLength) + swayAmount + tentacleSway * Math.cos(angle + Math.PI/2); // Add sway perpendicular to angle
            const endY = tentacleBaseY + Math.sin(angle) * (size * 0.4 + tentacleLength) + tentacleSway * Math.sin(angle + Math.PI/2);

            ctx.beginPath();
            ctx.moveTo(startX, startY);
            ctx.quadraticCurveTo(
                 startX + (endX - startX) * 0.3 + Math.cos(angle) * size * 0.2, // Control point 1
                 startY + (endY - startY) * 0.3 + Math.sin(angle) * size * 0.2,
                 endX,
                 endY
             );
            ctx.strokeStyle = colors.tentacles;
            ctx.lineWidth = 3;
            ctx.lineCap = 'round';
            ctx.stroke();
        }

         // Mouth (optional, simple dot)
         ctx.fillStyle = '#000';
         ctx.beginPath();
         ctx.arc(x + swayAmount, tentacleBaseY + size * 0.1, size * 0.05, 0, Math.PI * 2);
         ctx.fill();
    }

    function drawBackgroundElements(ctx) {
         // Simple bubbles rising
         const bubbleCount = 20;
         const bubbleSize = 1 + Math.random() * 3;
         ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
         for(let i = 0; i < bubbleCount; i++) {
             const x = Math.random() * canvas.width;
             const y = canvas.height - 60 - Math.random() * (canvas.height - 60); // Avoid sea floor
             ctx.beginPath();
             ctx.arc(x, y, bubbleSize, 0, Math.PI * 2);
             ctx.fill();
         }
         // Note: For a real animation loop, bubbles would need position state and update.
         // This static draw just adds visual texture.
    }

    function drawAsexualStep(step, progress) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // drawBackgroundElements(ctx); // Add background elements
        stageTextDiv.textContent = asexualSteps[step];

        const centerX = canvas.width / 2;
        const centerY = (canvas.height - 60) / 2; // Center above floor
        const size = 60; // Base size
        const floorY = canvas.height - 60; // Top of the sea floor

        // Ensure the sea floor is always visible if the step needs it
        if (step >= 0) { // All asexual steps are on the floor
             seaFloorDiv.style.display = 'block';
        }


        switch (step) {
            case 0: // Adult Anemone
                drawAnemone(ctx, centerX, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2)); // Sway slightly
                break;
            case 1: // Budding / Fission starts
                 if (Math.random() < 0.5) { // Simulate budding
                     drawAnemone(ctx, centerX, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
                     // Draw bud growing near base
                     const budSize = size * 0.2 + size * 0.4 * progress; // Grows from 0.2 to 0.6
                     const budX = centerX + size * 0.8;
                     const budY = floorY - size * 0.1;
                     ctx.fillStyle = 'rgba(255, 105, 180, 0.7)'; // Semi-transparent pink
                     ctx.beginPath();
                     ctx.arc(budX, budY, budSize, 0, Math.PI * 2);
                     ctx.fill();
                 } else { // Simulate fission (elongation/constriction)
                     const stretchFactor = 1 + progress * 0.3; // Stretch up to 30%
                     const constrictionFactor = 1 - progress * 0.2; // Constrict down to 80%
                     const currentSizeX = size * stretchFactor;
                     const currentSizeY = size * constrictionFactor;
                      // Simple oval representation for fission
                      ctx.fillStyle = 'rgba(255, 105, 180, 0.7)';
                      ctx.beginPath();
                      ctx.ellipse(centerX, floorY - currentSizeY/2 - size*0.3, currentSizeX * 0.7, currentSizeY * 0.7, 0, 0, Math.PI*2);
                      ctx.fill();
                      // Draw original anemone shape fading out? Or just replace?
                      // Let's redraw a stretched version
                     drawAnemone(ctx, centerX, floorY - currentSizeY/2 - size * 0.3, currentSizeY, ANEMONE_COLORS, 16, 0.3 * stretchFactor, Math.sin(progress * Math.PI * 4)); // Sway faster
                 }
                break;
            case 2: // Bud grows / Fission progresses
                 if (Math.random() < 0.5) { // Simulate budding
                     drawAnemone(ctx, centerX, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
                     // Draw more developed bud
                     const budSize = size * 0.6 + size * 0.3 * progress; // Grows from 0.6 to 0.9
                     const budX = centerX + size * 1.5;
                     const budY = floorY - size * 0.2;
                     // Maybe draw a mini anemone shape
                     drawAnemone(ctx, budX, budY - budSize/2 - budSize * 0.3, budSize, ANEMONE_COLORS_VARIANT, Math.max(4, Math.floor(16 * progress)), 0.3, Math.sin(progress * Math.PI * 6)); // More tentacles appear, sway more
                 } else { // Simulate fission
                     const stretchFactor = 1.3 - progress * 0.1; // Stretches less
                     const constrictionFactor = 0.8 - progress * 0.2; // Constricts more
                     const currentSizeX = size * stretchFactor;
                     const currentSizeY = size * constrictionFactor;

                      // Draw two parts forming
                      const gap = size * 0.4 * progress;
                      drawAnemone(ctx, centerX - size * 0.7 - gap/2, floorY - currentSizeY/2 - size*0.3, currentSizeY * 0.9, ANEMONE_COLORS, Math.max(8, Math.floor(16 * progress)), 0.3, Math.sin(progress * Math.PI * 8)); // Sway fastest
                      drawAnemone(ctx, centerX + size * 0.7 + gap/2, floorY - currentSizeY/2 - size*0.3, currentSizeY * 0.9, ANEMONE_COLORS, Math.max(8, Math.floor(16 * progress)), 0.3, Math.sin(progress * Math.PI * 8));
                 }
                break;
            case 3: // Young polyp formed / Fission completed (still potentially attached)
                 if (Math.random() < 0.5) { // Simulate budding
                    drawAnemone(ctx, centerX, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
                    // Draw young anemone, almost detached
                    const youngSize = size * 0.9;
                    const youngX = centerX + size * 2.2;
                    const youngY = floorY - size * 0.3;
                    // Animate detachment movement
                    const detachDist = size * 0.5 * progress;
                    drawAnemone(ctx, youngX + detachDist, youngY - youngSize/2 - youngSize * 0.3, youngSize, ANEMONE_COLORS_VARIANT, 16, 0.3, Math.sin(progress * Math.PI * 4));
                 } else { // Simulate fission
                    // Draw two nearly separate anemones
                     const gap = size * 0.8;
                     const moveDist = size * 0.5 * progress; // Animate separation movement
                    drawAnemone(ctx, centerX - size * 1.5 - moveDist, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 4));
                    drawAnemone(ctx, centerX + size * 1.5 + moveDist, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 4));
                 }
                break;
            case 4: // Independent Anemones
                 if (Math.random() < 0.5) { // Simulate budding
                    drawAnemone(ctx, centerX, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
                    drawAnemone(ctx, centerX + size * 3, floorY - size/2 - size * 0.3, size * 0.9, ANEMONE_COLORS_VARIANT, 16, 0.3, Math.sin(progress * Math.PI * 2)); // Fully independent young
                 } else { // Simulate fission
                    drawAnemone(ctx, centerX - size * 2, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
                    drawAnemone(ctx, centerX + size * 2, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
                 }
                break;
            default:
                 drawAnemone(ctx, centerX, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
                break;
        }
    }

    // Planula state variables (for sexual mode step 4)
    let planulaX = 50;
    let planulaY = canvas.height * 0.6; // Start higher up
    let planulaSpeed = 2;
    let planulaDirection = 1; // 1 for right, -1 for left
    let planulaTargetY = canvas.height - 70; // Target Y near the floor


    function drawSexualStep(step, progress) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // drawBackgroundElements(ctx); // Add background elements
        stageTextDiv.textContent = sexualSteps[step];

        const centerX = canvas.width / 2;
        const centerY = (canvas.height - 60) / 2;
        const size = 60; // Base size
        const floorY = canvas.height - 60;

        // Draw parent anemones if applicable (fading out after spawning)
        if (step <= 1) {
             drawAnemone(ctx, centerX - size * 1.5, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
             drawAnemone(ctx, centerX + size * 1.5, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS_VARIANT, 16, 0.3, Math.sin(progress * Math.PI * 2));
             seaFloorDiv.style.display = 'block';
        } else if (step === 2 && progress < 1) { // Fade out parents during fertilization
             ctx.save();
             ctx.globalAlpha = 1 - progress;
             drawAnemone(ctx, centerX - size * 1.5, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));
             drawAnemone(ctx, centerX + size * 1.5, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS_VARIANT, 16, 0.3, Math.sin(progress * Math.PI * 2));
             ctx.restore();
              seaFloorDiv.style.display = 'block';
        } else if (step >= 5) {
             seaFloorDiv.style.display = 'block';
        } else {
             seaFloorDiv.style.display = 'none'; // Hide floor when planula is swimming higher
        }


        switch (step) {
            case 0: // Adult Anemones - Drawn above
                break;
            case 1: // Spawning - Animate gametes appearing and moving
                 const gameteCount = 80;
                 const spawnAreaRadius = size * 2;
                 const gameteSize = 2;
                 const spawnCenterX1 = centerX - size * 1.5;
                 const spawnCenterX2 = centerX + size * 1.5;
                 const spawnCenterY = floorY - size/2;

                 // Gametes appearing and swirling
                 for(let i=0; i<gameteCount; i++) {
                     const angle = (i / gameteCount) * Math.PI * 4 * progress; // Swirl effect
                     const radius = spawnAreaRadius * Math.sqrt(i / gameteCount); // Distribute outwards
                     let x, y;
                     if (i < gameteCount / 2) { // Sperm from right anemone (blue)
                         x = spawnCenterX2 + Math.cos(angle) * radius;
                         y = spawnCenterY + Math.sin(angle) * radius * 0.5; // Slightly flattened swirl
                         ctx.fillStyle = 'rgba(0, 150, 255, 0.7)';
                     } else { // Eggs from left anemone (yellow/orange)
                          x = spawnCenterX1 + Math.cos(angle + Math.PI) * radius; // Swirl in opposite direction?
                          y = spawnCenterY + Math.sin(angle + Math.PI) * radius * 0.5;
                          ctx.fillStyle = 'rgba(255, 200, 0, 0.7)';
                     }
                     ctx.beginPath();
                     ctx.arc(x, y, gameteSize, 0, Math.PI * 2);
                     ctx.fill();
                 }

                break;
            case 2: // Fertilization - Gametes moving towards center, forming zygotes
                 const zygoteCount = 40;
                 const driftAreaWidth = canvas.width * 0.6;
                 const driftAreaHeight = canvas.height * 0.4;
                 const driftCenterX = canvas.width * 0.5;
                 const driftCenterY = canvas.height * 0.4; // Higher than floor

                 // Animate gametes moving towards center
                 const gameteSpeed = size * 0.1 * progress; // Speed increases with progress
                 for(let i=0; i<zygoteCount; i++) {
                     let startX, startY;
                     if (i < zygoteCount / 2) { // Sperm origins
                         startX = centerX + size * 1.5 + (Math.random() - 0.5) * size * 2;
                         startY = floorY - size/2 + (Math.random() - 0.5) * size * 2;
                         ctx.fillStyle = 'rgba(0, 150, 255, 0.5)';
                     } else { // Egg origins
                          startX = centerX - size * 1.5 + (Math.random() - 0.5) * size * 2;
                          startY = floorY - size/2 + (Math.random() - 0.5) * size * 2;
                         ctx.fillStyle = 'rgba(255, 200, 0, 0.5)';
                     }
                      // Move towards the fertilization area (simplified)
                     const targetX = driftCenterX + (Math.random() - 0.5) * driftAreaWidth * 0.5;
                     const targetY = driftCenterY + (Math.random() - 0.5) * driftAreaHeight * 0.5;

                     const currentX = startX + (targetX - startX) * progress;
                     const currentY = startY + (targetY - startY) * progress;

                     ctx.beginPath();
                     ctx.arc(currentX, currentY, gameteSize * (1 - progress * 0.5), 0, Math.PI * 2); // Shrink slightly
                     ctx.fill();
                 }

                 // Draw zygotes appearing (fading in)
                 const zygoteSize = 4;
                 ctx.fillStyle = 'rgba(250, 128, 114, ' + progress + ')'; // Salmon, fade in
                 for(let i=0; i<zygoteCount; i++) {
                     let x = driftCenterX + (Math.random() - 0.5) * driftAreaWidth * 0.7;
                     let y = driftCenterY + (Math.random() - 0.5) * driftAreaHeight * 0.7;
                     ctx.beginPath();
                     ctx.arc(x, y, zygoteSize, 0, Math.PI * 2);
                     ctx.fill();
                 }

                break;
            case 3: // Planula Development - Zygotes developing and drifting
                 const larvaeCount = 15;
                 const developAreaWidth = canvas.width * 0.7;
                 const developAreaHeight = canvas.height * 0.5;
                 const developCenterX = canvas.width * 0.5;
                 const developCenterY = canvas.height * 0.4;

                  // Draw developing larvae (slightly larger dots/ovals)
                  const larvaSize = 6 + progress * 4; // Grow slightly
                  ctx.fillStyle = 'rgba(255, 160, 122, ' + (0.5 + progress * 0.5) + ')'; // Light Salmon, becoming more opaque
                  for(let i=0; i<larvaeCount; i++) {
                      let x = developCenterX + (Math.random() - 0.5) * developAreaWidth;
                      let y = developCenterY + (Math.random() - 0.5) * developAreaHeight;
                      ctx.beginPath();
                      ctx.arc(x, y, larvaSize, 0, Math.PI * 2);
                      ctx.fill();
                  }

                break;
            case 4: // Motile Planula - Swimming animation happens here
                // Draw a distinct planula shape
                ctx.fillStyle = '#ff7f50'; // Coral
                ctx.beginPath();
                 const planulaBodyWidth = 20;
                 const planulaBodyHeight = 10;
                 const planulaAngle = planulaDirection === 1 ? 0 : Math.PI; // Rotate based on direction
                 // Add slight bobbing or wobble
                 const bobbing = Math.sin(performance.now() / 100) * 3;
                ctx.ellipse(planulaX, planulaY + bobbing, planulaBodyWidth, planulaBodyHeight, planulaAngle, 0, Math.PI * 2);
                ctx.fill();
                // Simple cilia lines (more stylized)
                ctx.strokeStyle = '#d2691e'; // Chocolate
                ctx.lineWidth = 1;
                const ciliaCount = 15;
                for(let i=0; i<ciliaCount; i++) {
                     const angle = (i / ciliaCount) * Math.PI * 2;
                     const startX = planulaX + Math.cos(angle) * planulaBodyWidth * 0.8;
                     const startY = planulaY + bobbing + Math.sin(angle) * planulaBodyHeight * 0.8;
                     const endX = planulaX + Math.cos(angle) * (planulaBodyWidth + 5);
                     const endY = planulaY + bobbing + Math.sin(angle) * (planulaBodyHeight + 5);
                     ctx.beginPath();
                     ctx.moveTo(startX, startY);
                     ctx.lineTo(endX, endY);
                     ctx.stroke();
                }
                 // Note: Planula X/Y updates happen in updateAnimation for continuous movement.
                break;
            case 5: // Settlement - Planula settles and starts metamorphosis
                 // Animate planula moving down to floor and flattening
                 const settlementY = planulaY + (planulaTargetY - planulaY) * progress;
                 const flatFactor = 1 - progress * 0.5; // Flattens as it settles

                 ctx.fillStyle = '#ff7f50'; // Coral
                 ctx.beginPath();
                 ctx.ellipse(planulaX, settlementY, 20, 10 * flatFactor, planulaDirection === 1 ? 0 : Math.PI, 0, Math.PI * 2);
                 ctx.fill();

                 // Draw a small polyp base appearing
                 const baseSize = 15 * progress;
                 const baseX = planulaX;
                 const baseY = floorY - baseSize/2;
                 ctx.fillStyle = ANEMONE_COLORS.base;
                 ctx.beginPath();
                 ctx.arc(baseX, baseY, baseSize, 0, Math.PI * 2);
                 ctx.fill();

                break;
            case 6: // Young Polyp Development - Polyp grows
                 const youngSizeStep6 = 15 + (30 - 15) * progress; // Grows from 15 to 30
                 const youngXStep6 = canvas.width / 2;
                 const youngYStep6 = floorY - youngSizeStep6/2 - youngSizeStep6 * 0.3;
                 drawAnemone(ctx, youngXStep6, youngYStep6, youngSizeStep6, ANEMONE_COLORS_VARIANT, Math.max(6, Math.floor(10 * progress)), 0.3, Math.sin(progress * Math.PI * 4)); // Grows tentacles

                break;
            case 7: // Adult Anemone (Mature) - Full size
                 const finalSize = size;
                 const finalX = canvas.width / 2;
                 const finalY = floorY - finalSize/2 - finalSize * 0.3;
                 drawAnemone(ctx, finalX, finalY, finalSize, ANEMONE_COLORS, 16, 0.3, Math.sin(progress * Math.PI * 2));

                break;
            default: // Should not happen, draw initial state
                 drawAnemone(ctx, centerX - size * 1.5, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS, 16, 0.3);
                 drawAnemone(ctx, centerX + size * 1.5, floorY - size/2 - size * 0.3, size, ANEMONE_COLORS_VARIANT, 16, 0.3);
                 seaFloorDiv.style.display = 'block';
                break;
        }
    }


    function updateAnimation(timestamp) {
        if (animationState === 1) { // Only update if playing
            if (!lastTimestamp) lastTimestamp = timestamp;
            const elapsed = timestamp - lastTimestamp;

            // Calculate duration based on speed slider
            frameDuration = 2500 / (parseInt(speedSlider.value, 10) * 2); // Faster/slower steps

            // Special handling for Planula movement in Step 4 (Sexual)
             if (currentMode === 'sexual' && currentStep === 4) {
                  // Planula movement is time-based, not just step progress
                 const moveAmount = (elapsed / 60) * planulaSpeed * planulaDirection * (parseInt(speedSlider.value, 10) / 5); // Move amount scaled by speed
                 planulaX += moveAmount;
                 // Bounce off walls, but avoid floor area for now
                 if (planulaX > canvas.width - 30 || planulaX < 30) {
                      planulaDirection *= -1;
                      planulaX = planulaX > canvas.width - 30 ? canvas.width - 30 : (planulaX < 30 ? 30 : planulaX); // Prevent sticking
                 }
                  // Add random vertical movement, trying to drift downwards slightly
                  planulaY += (Math.random() - 0.6) * 5 * (parseInt(speedSlider.value, 10) / 5); // Bias downwards slightly
                  if (planulaY < 30) planulaY = 30;
                  if (planulaY > canvas.height - 100) planulaY = canvas.height - 100; // Keep above floor area

                  // Continue animating the planula's movement regardless of step duration
                 drawSexualStep(currentStep, 0); // Draw at 0 progress for the step, as movement is continuous
                 lastTimestamp = timestamp; // Update timestamp immediately for smooth movement

                 // Check if enough time has passed to move to the next step (Settlement)
                 const stepProgressThreshold = 0.95; // Move to next step when animation progress (time) reaches this
                 if (elapsed > frameDuration * stepProgressThreshold) { // Use overall step duration for progression logic
                      nextStep();
                      lastTimestamp = timestamp; // Reset timestamp for the new step
                 }


            } else {
                 // For steps with fixed animations, advance based on duration
                 animationProgress += elapsed / animationDuration; // Increment progress (duration is fixed per step type animation)

                 if (animationProgress >= 1) {
                     animationProgress = 1; // Cap at 1
                     // Now advance to the next step and reset progress
                     nextStep();
                     animationProgress = 0; // Reset for the next step's animation
                     lastTimestamp = timestamp; // Reset timestamp for the new step
                 } else {
                     // If not yet at the end of the step animation, redraw current step with progress
                      if (currentMode === 'asexual') {
                         drawAsexualStep(currentStep, animationProgress);
                      } else { // sexual mode, but not step 4
                          drawSexualStep(currentStep, animationProgress);
                      }
                      lastTimestamp = timestamp;
                 }
            }
        } else if (animationState === 0) {
            // Reset timestamp when animation stops
            lastTimestamp = 0;
        } else if (animationState === 2) {
             // If paused on planula step (4), keep redrawing for bobbing effect
             if (currentMode === 'sexual' && currentStep === 4) {
                  drawSexualStep(currentStep, 0);
             }
             lastTimestamp = timestamp; // Keep timestamp updated even when paused for bobbing/sway calculations
        }


        // Always request next frame if state is playing or paused on a state with continuous drawing
        if (animationState !== 0 || (currentMode === 'sexual' && currentStep === 4) || (currentMode === 'asexual' && currentStep !== asexualSteps.length -1 && animationState === 2) || (currentMode === 'sexual' && currentStep !== sexualSteps.length -1 && animationState === 2) ) {
             requestAnimationFrame(updateAnimation);
        }
    }


    function startAnimation() {
        if (animationState !== 1) {
            animationState = 1;
            playPauseBtn.textContent = 'השהה';
            // If resuming, ensure timestamp is current to calculate elapsed time correctly
            if (lastTimestamp === 0) {
                 lastTimestamp = performance.now();
                 animationProgress = 0; // Reset progress if starting fresh
            }
            requestAnimationFrame(updateAnimation); // Start/resume loop
        }
    }

    function pauseAnimation() {
        if (animationState === 1) { // Only pause if playing
             animationState = 2; // Paused state
             playPauseBtn.textContent = 'המשך';
             // Keep lastTimestamp to calculate elapsed when resuming
        }
    }

    function resetAnimation() {
        animationState = 0;
        currentStep = 0;
        playPauseBtn.textContent = 'התחל';
        animationProgress = 0; // Reset step animation progress
        lastTimestamp = 0; // Ensure timer resets
        planulaX = 50; // Reset planula position for sexual mode
        planulaY = canvas.height * 0.6;
        planulaDirection = 1;

        // Draw the initial state of the currently selected mode
        if (currentMode === 'asexual') {
            drawAsexualStep(currentStep, animationProgress);
        } else {
            drawSexualStep(currentStep, animationProgress);
        }
         // Ensure canvas is cleared before drawing initial state
         ctx.clearRect(0, 0, canvas.width, canvas.height);
         if (currentMode === 'asexual') drawAsexualStep(currentStep, animationProgress); else drawSexualStep(currentStep, animationProgress);

    }

    function nextStep() {
        let stepsArray = currentMode === 'asexual' ? asexualSteps : sexualSteps;
        // Prevent stepping past the end if manually stepping while paused
        if (currentStep >= stepsArray.length - 1 && animationState !== 1) {
             // Already at the last step, don't increment. Suggest reset visually.
             playPauseBtn.textContent = 'התחל מחדש?';
             return;
        }

        currentStep++;
        animationProgress = 0; // Reset progress for the new step

        // Check if reached the end while playing
        if (currentStep >= stepsArray.length) {
            resetAnimation(); // Loop back to start or stop? Let's loop for now
            // To stop at the end:
            // currentStep = stepsArray.length - 1; // Stay on last step
            // pauseAnimation();
            // playPauseBtn.textContent = 'התחל מחדש';
        } else {
             // Draw the first frame of the new step
             if (currentMode === 'asexual') {
                 drawAsexualStep(currentStep, animationProgress);
             } else {
                 drawSexualStep(currentStep, animationProgress);
             }
        }
        lastTimestamp = performance.now(); // Update timestamp for the new step's duration calculation
        // If paused but manually stepped, request frame to draw the new step's initial state
         if (animationState === 2) {
             requestAnimationFrame(updateAnimation);
         }
    }

    function togglePlayPause() {
        let stepsArray = currentMode === 'asexual' ? asexualSteps : sexualSteps;
        if (animationState === 1) {
            pauseAnimation();
        } else {
            // If currently on the last step and paused, reset first
             if (currentStep >= stepsArray.length - 1 && animationState === 2) {
                 resetAnimation(); // Reset to step 0
                 startAnimation(); // Start playing from step 0
             } else {
                startAnimation(); // Start playing from current step
             }
        }
    }

    function selectMode(mode) {
        if (currentMode !== mode) { // Only change if different mode selected
             currentMode = mode;
             resetAnimation(); // Reset simulation state when mode changes
             if (mode === 'asexual') {
                 asexualBtn.classList.add('active');
                 sexualBtn.classList.remove('active');
             } else {
                 asexualBtn.classList.remove('active');
                 sexualBtn.classList.add('active');
             }
             // resetAnimation draws the first step of the new mode
        }
    }

    // Event Listeners
    asexualBtn.addEventListener('click', () => selectMode('asexual'));
    sexualBtn.addEventListener('click', () => selectMode('sexual'));
    playPauseBtn.addEventListener('click', togglePlayPause);
    stepBtn.addEventListener('click', () => {
         // Only allow manual step if not currently playing
         if (animationState !== 1) {
              nextStep();
         }
    });
    resetBtn.addEventListener('click', resetAnimation);
    speedSlider.addEventListener('input', (e) => {
        animationSpeed = parseInt(e.target.value, 10);
        // frameDuration is calculated in updateAnimation based on current speedSlider value
         animationDuration = 1000 / (animationSpeed / 5); // Adjust base animation duration
    });

    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('hidden');
        if (isHidden) {
             explanationDiv.classList.remove('hidden');
             // Use a small timeout to allow display:block before transitioning opacity
             setTimeout(() => {
                  explanationDiv.classList.add('visible');
             }, 10);
             explanationButton.textContent = 'הסתר הסבר מפורט';
        } else {
             explanationDiv.classList.remove('visible');
             // Use timeout matching transition duration before hiding completely
             setTimeout(() => {
                  explanationDiv.classList.add('hidden');
             }, 500); // Should match CSS transition duration
             explanationButton.textContent = 'גלו את הסודות: הסבר מפורט';
        }
    });


    // Initial setup
    resetAnimation(); // Draw the initial state
    requestAnimationFrame(updateAnimation); // Start the animation loop (it will be paused initially)


</script>