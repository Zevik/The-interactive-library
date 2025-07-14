---
title: "הסוד השמימי של נמלי המדבר: ניווט באמצעות אור מקוטב"
english_slug: the-heavenly-secret-of-desert-ants-navigation-using-polarized-light
category: "מדעי החיים / ביולוגיה"
tags: ["ביולוגיה התנהגותית", "ניווט", "נמלים", "אור מקוטב", "מדבר"]
---
# הסוד השמימי של נמלי המדבר: ניווט באמצעות אור מקוטב

דמיינו שאתם עומדים במדבר אינסופי, שמש יוקדת מעל, אין צל, ואין שום סימן מוכר באופק. אתם בלב שטח פתוח וקשה לזיהוי. איך, לעזאזל, תצליחו למצוא את הדרך חזרה לנקודת המוצא? זהו האתגר היומיומי של נמלי המדבר הזעירות, היוצאות למסעות חיפוש אחר מזון על אדמה לוהטת, ולמרות זאת, הן תמיד מוצאות את דרכן חזרה לקן הקטן שלהן בדיוק מדהים. הסוד שלהן חבוי בשמיים מעל - הן מנווטות באמצעות אור! לא סתם אור, אלא אור מקוטב, סוג של "מפה שמימית" שנסתרת מעיני רוב היצורים, כולל בני אדם. הצטרפו אלינו לגלות את היכולת המדהימה הזו.

<div id="ant-navigation-app">
    <h2 class="app-title">צפו במפת הקיטוב השמימית</h2>
    <p class="app-description">
        הסימולציה הזו מדגימה את דפוס הקיטוב בשמיים. גררו את השמש ☀️ כדי לשנות את מיקומה וצפו כיצד הדפוס המופלא משתנה. רחפו עם העכבר מעל נקודה בשמיים 🐜 כדי לדמות את "מבט הנמלה" ולראות את כיוון הקיטוב באותה נקודה.
    </p>
    <div class="sky-container">
        <canvas id="sky-canvas"></canvas>
        <div id="sun">☀️</div> <!-- Using emoji for visual appeal -->
        <div id="ant-eye-indicator" style="display: none;">🐜</div>
        <div id="polarization-info" style="display: none;"></div>
    </div>
    <div class="controls">
        <label for="polarization-density" class="control-label">צפיפות "קריאת" הקיטוב:</label>
        <input type="range" id="polarization-density" min="20" max="120" value="60">
        <span class="control-value">בינונית</span>
    </div>
</div>

<style>
    #ant-navigation-app {
        font-family: 'Arial', sans-serif; /* Use a common, clear font */
        margin: 20px auto; /* Center the app */
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* White background */
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        max-width: 650px; /* Max width for better readability */
    }

    .app-title {
        color: #2c3e50; /* Darker blue-grey */
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.8em;
    }

    .app-description {
        color: #555;
        font-size: 1em;
        margin-bottom: 20px;
        line-height: 1.5;
    }

    .sky-container {
        position: relative;
        width: 100%;
        max-width: 600px; /* Match app max-width consideration */
        height: 350px; /* Slightly taller sky */
        margin: 20px auto;
        background: linear-gradient(to bottom, #4682B4 0%, #87CEEB 50%, #ADD8E6 80%, #F0E68C 100%); /* More complex, appealing gradient */
        border-radius: 15px; /* More rounded sky container */
        overflow: hidden;
        cursor: grab; /* Indicate draggable */
        border: 1px solid #c0c0c0;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow */
        transition: transform 0.3s ease; /* Smooth transition on hover/drag */
    }

    .sky-container:hover {
         transform: scale(1.01); /* Slight hover effect */
    }

    .sky-container.dragging {
        cursor: grabbing;
        transform: scale(1.01); /* Keep effect while dragging */
    }

    #sky-canvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1; /* Below sun and ant eye */
        opacity: 0.7; /* Make pattern slightly transparent */
    }

    #sun {
        position: absolute;
        font-size: 40px; /* Emoji size */
        cursor: grab;
        z-index: 10;
        user-select: none; /* Prevent text selection */
        transition: left 0.3s ease-out, top 0.3s ease-out; /* Smooth movement */
    }

    #sun.dragging {
         cursor: grabbing;
    }

    #ant-eye-indicator {
        position: absolute;
        font-size: 28px;
        text-align: center;
        cursor: pointer;
        z-index: 20;
        pointer-events: none; /* Does not block clicks on canvas */
        transition: left 0.1s ease-out, top 0.1s ease-out; /* Smooth follow */
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.5); /* Subtle glow */
    }

    #polarization-info {
        position: absolute;
        bottom: 15px;
        left: 15px;
        background-color: rgba(255, 255, 255, 0.95); /* More opaque background */
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 0.9em;
        color: #333;
        z-index: 30;
        pointer-events: none;
        min-width: 150px; /* Ensure minimum width */
        text-align: right;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .controls {
        margin-top: 20px;
        font-size: 1em;
        color: #333;
        display: flex; /* Use flexbox for better alignment */
        justify-content: center;
        align-items: center;
    }

    .controls label {
        margin-left: 10px;
        font-weight: bold;
    }

    .controls input[type="range"] {
        flex-grow: 0; /* Don't let the slider grow */
        width: 150px; /* Fixed width for slider */
        margin-right: 10px;
        cursor: pointer;
    }

     .controls .control-value {
         min-width: 60px; /* Allocate space for the value text */
         text-align: left;
         font-size: 0.9em;
         color: #555;
     }


    #explanation-button {
        display: block;
        margin: 30px auto 20px auto; /* More space */
        padding: 12px 25px; /* Larger padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        background-color: #007bff; /* Primary blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #explanation-button:hover {
        background-color: #0056b3;
        transform: translateY(-2px); /* Slight lift effect */
    }
     #explanation-button:active {
         transform: translateY(0);
     }

    #full-explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #f8f9fa; /* Light grey background */
        text-align: right;
        display: none; /* Initially hidden */
        line-height: 1.7;
        color: #333;
    }

    #full-explanation h3 {
        color: #0056b3; /* Match button hover color */
        margin-top: 1.5em; /* More space above headings */
        margin-bottom: 0.8em;
        font-size: 1.3em;
        border-bottom: 1px solid #cce5ff; /* Subtle underline */
        padding-bottom: 5px;
    }
    #full-explanation h3:first-child {
         margin-top: 0;
    }

    #full-explanation p {
        margin-bottom: 1em;
    }

    /* Responsive adjustments */
    @media (max-width: 700px) {
        #ant-navigation-app {
            margin: 10px;
            padding: 15px;
        }
        .sky-container {
            height: 250px;
        }
        .app-title {
            font-size: 1.5em;
        }
        .app-description {
            font-size: 0.95em;
        }
        .controls {
             flex-direction: column; /* Stack controls on small screens */
             align-items: flex-end;
        }
        .controls label {
             margin-bottom: 5px;
             margin-left: 0;
        }
        .controls input[type="range"] {
             width: 100%; /* Make slider full width */
             margin-right: 0;
        }
        .controls .control-value {
             width: 100%;
             text-align: center;
             margin-top: 5px;
        }
        #explanation-button {
            padding: 10px 20px;
            font-size: 1em;
        }
         #polarization-info {
             left: 50%;
             transform: translateX(-50%);
             bottom: 5px;
             top: auto; /* Ensure it's anchored to the bottom */
         }
    }

</style>

<button id="explanation-button">איך נמלים רואות אור מקוטב? הצג הסבר מלא</button>

<div id="full-explanation">
    <h3>המדבר כאתגר ניווט בלתי נתפס</h3>
    נמלי המדבר מהסוג *Cataglyphis* הן אלופות הישרדות בסביבות קיצוניות. הן יוצאות ממחילתן התת-קרקעית אל פני השטח הלוהטים של המדבר כדי לחפש מזון מפוזר. הטמפרטורה על הקרקע יכולה לטפס עד 70 מעלות צלזיוס! שהות ארוכה מדי בחוץ היא גזר דין מוות. הן חייבות למצוא את דרכן חזרה לקן הקטנטן במהירות שיא, לעיתים לאחר מסע מפותל וארוך של עשרות ואף מאות מטרים בשטח שכולו דיונות או סלעים אחידים למראה. איך הן עושות זאת ללא GPS, ללא שובל ריח קבוע (שמתפוגג בחום הקיצוני), ולרוב ללא סימני דרך בולטים? זהו פלא ביולוגי.

    <h3>אור מקוטב: מצפן שמימי נסתר</h3>
    הסוד טמון באופן שבו הן "קוראות" את האור המגיע אליהן מהשמיים. אור השמש, כשהוא חודר לאטמוספרה, פוגע במולקולות האוויר ומתפזר. פיזור זה (פיזור ריילי, שגם גורם לשמיים להיראות כחולים) גורם לאור להפוך ל"מקוטב". משמעות הדבר היא שגלי האור מתנודדים בכיוון מועדף אחד, ולא באופן אקראי בכל הכיוונים. דמיינו חבל שאתם מניעים למעלה-למטה (קיטוב אנכי) לעומת חבל שאתם מניעים ימינה-שמאלה (קיטוב אופקי). האור המפוזר בשמיים יוצר תבנית קיטוב קבועה וצפויה ביחס למיקום השמש, מעין "מפת קיטוב" על כיפת השמיים. גם אם השמש עצמה מוסתרת חלקית (למשל מאחורי אבן או בשעת שקיעה), מפת הקיטוב הזו נשארת יציבה יחסית ומספקת מידע על כיוון השמש.

    <h3>עיני הנמלה: מפענחות את שפת האור</h3>
    כדי לנצל את המצפן השמימי הזה, נמלי המדבר מצוידות במערכת ראייה מיוחדת. בחלק העליון של כל עין מורכבת יש להן אזור קטן המכיל תאים קולטי אור (פוטורצפטורים) המסודרים בצורה ייחודית ביותר. תאים אלה "רגישים לכיוון" - הם מגיבים בעוצמה שונה לאור בהתאם לכיוון הקיטוב שלו. כל תא כזה מכוון לזיהוי קיטוב בזווית מסוימת. על ידי השוואת האותות המתקבלים ממספר תאים המכוונים לזוויות שונות, הנמלה יכולה לחשב במדויק את כיוון הקיטוב השולט באותה נקודה בשמיים. זה כאילו יש להן מצפן פנימי מובנה, המבוסס על ניתוח אור השמיים.

    <h3>ניווט לפי קיטוב: השימוש במפת השמיים</h3>
    נמלה שיוצאת מהקן יכולה "לקרוא" את כיוון הקיטוב בחלק מסוים של השמיים ולשמור על זווית קבועה ביחס אליו כדי לנוע בקו ישר מהקן. כשהיא מוצאת מזון ורוצה לחזור הביתה, היא פשוט משנה את הזווית ביחס לאותו כיוון קיטוב (או לנקודה אחרת בשמיים, תלוי באסטרטגיה המדויקת) כדי לפנות חזרה לכיוון הקן. מפת הקיטוב השמימית, הנוצרת על ידי השמש, מספקת לה כיוון אבסולוטי (צפון/דרום/מזרח/מערב יחסית למיקום השמש) גם בסביבה חסרת תוואי שטח.

    <h3>לא רק קיטוב: ארגז כלים ניווטי מגוון</h3>
    חשוב לציין שניווט באמצעות קיטוב האור אינו שיטת הניווט היחידה של נמלי המדבר. הן משלבות אותה עם יכולות נוספות שיוצרות יחד מערכת ניווט סופר-יעילה:
    *   **אינטגרציית מסלול ("מונה צעדים" פנימי):** הנמלה עוקבת אחרי מספר הצעדים שעשתה והכיוונים אליהם פנתה בדרכה החוצה, ובכך מחשבת באופן רציף את מיקומה היחסי לקן. מערכת הקיטוב מסייעת לה לשמור על כיוון ישר ולעדכן את ה"מונה" הזה.
    *   **סימני דרך חזותיים (קרובים לקן):** בסמוך לקן, שם עשויים להיות אבנים או צמחים בולטים, הן משתמשות גם בזיכרון חזותי כדי לזהות את הסביבה הקרובה ולוודא שהן הגיעו ליעד המדויק.
    *   **רמזי ריח (בסמוך מאוד לקן):** ממש ליד פתח הקן, הן עשויות להיעזר ברמזי ריח עדינים כדי למצוא את הכניסה המדויקת.
    השילוב של מנגנונים אלה מאפשר לנמלה למצוא את דרכה הביתה באמינות כמעט מוחלטת, גם לאחר מסעות ארוכים בשטח עוין.

    <h3>ללמוד מהטבע: השראה לטכנולוגיה</h3>
    המחקר המרתק על ניווט נמלי המדבר לא רק חושף בפנינו פלאים ביולוגיים, אלא גם משמש השראה לטכנולוגיה אנושית. היכולת לזהות קיטוב אור ולנצל אותו לניווט היא תחום פעיל בפיתוח, וישנם ניסיונות לבנות חיישני קיטוב שישמשו מערכות ניווט אוטונומיות, במיוחד במצבים בהם GPS אינו זמין או מדויק. זהו עוד מקרה בו הטבע הקדים את הטכנולוגיה האנושית, וממשיך לספק לנו רעיונות יצירתיים.
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const skyContainer = document.querySelector('.sky-container');
    const skyCanvas = document.getElementById('sky-canvas');
    const sun = document.getElementById('sun');
    const antEyeIndicator = document.getElementById('ant-eye-indicator');
    const polarizationInfo = document.getElementById('polarization-info');
    const densityInput = document.getElementById('polarization-density');
    const densityValueSpan = document.querySelector('.controls .control-value');
    const ctx = skyCanvas.getContext('2d');

    let sunDragging = false;
    // Initial sun position - slightly offset from center top
    let sunPosition = { x: skyContainer.offsetWidth / 2 + 50, y: 80 };

    // Apply initial sun position style
    sun.style.left = `${sunPosition.x}px`;
    sun.style.top = `${sunPosition.y}px`;
    sun.style.transform = 'translate(-50%, -50%)'; // Center the emoji/div

    const updateCanvasSize = () => {
        skyCanvas.width = skyContainer.offsetWidth;
        skyCanvas.height = skyContainer.offsetHeight;
        // No need to reposition sun on resize if using percentage?
        // Let's keep absolute for simpler drag clamping.
        // Re-draw pattern on resize
        drawPolarizationPattern();
    };

    const drawPolarizationPattern = () => {
        ctx.clearRect(0, 0, skyCanvas.width, skyCanvas.height);

        const sunX = sunPosition.x;
        const sunY = sunPosition.y;

        const density = parseInt(densityInput.value);
        // Adjust step based on density and canvas size
        const stepX = skyCanvas.width / density;
        const stepY = skyCanvas.height / density * (skyCanvas.width / skyCanvas.height); // Maintain aspect ratio effect on density


        ctx.strokeStyle = 'rgba(70, 130, 180, 0.5)'; // SteelBlue with transparency
        ctx.lineWidth = 0.7; // Thinner lines

        for (let i = 0; i < density; i++) {
            for (let j = 0; j < density; j++) {
                const pX = (i + 0.5) * stepX;
                const pY = (j + 0.5) * stepY;

                // Simplified model: Polarization direction is perpendicular to the line
                // from the point (pX, pY) to the sun (sunX, sunY).
                const dx_sun = pX - sunX;
                const dy_sun = pY - sunY;
                let angle = Math.atan2(dy_sun, dx_sun); // Angle from point to sun

                // Polarization is perpendicular to this vector
                angle += Math.PI / 2;

                // Adjust line length based on density for better visual spread
                const lineLength = Math.min(stepX, stepY) * 0.4;

                const x1 = pX - lineLength * Math.cos(angle);
                const y1 = pY - lineLength * Math.sin(angle);
                const x2 = pX + lineLength * Math.cos(angle);
                const y2 = pY + lineLength * Math.sin(angle);

                ctx.beginPath();
                ctx.moveTo(x1, y1);
                ctx.lineTo(x2, y2);
                ctx.stroke();
            }
        }
         // Optional: Draw anti-sun point (for better visualization if needed)
         // const antiSunX = skyCanvas.width - sunX;
         // const antiSunY = skyCanvas.height - sunY;
         // ctx.fillStyle = 'rgba(255,0,0,0.5)';
         // ctx.beginPath();
         // ctx.arc(antiSunX, antiSunY, 5, 0, Math.PI * 2);
         // ctx.fill();
    };

    // Sun Drag functionality
    const startDragging = (e) => {
        sunDragging = true;
        skyContainer.classList.add('dragging');
        sun.classList.add('dragging');
        // Prevent default drag behavior for images etc.
        if (e.target.tagName === 'IMG') e.preventDefault();

        // Add event listeners to the whole document to ensure dragging continues
        // even if the cursor leaves the sun element.
        document.addEventListener('mousemove', onDrag);
        document.addEventListener('mouseup', stopDragging);
        document.addEventListener('touchmove', onDrag);
        document.addEventListener('touchend', stopDragging);
    };

    const onDrag = (e) => {
        if (!sunDragging) return;
        e.preventDefault(); // Prevent scrolling on touch devices

        const rect = skyContainer.getBoundingClientRect();
        let clientX, clientY;

        // Determine clientX and clientY based on event type
        if (e.type.startsWith('touch')) {
            clientX = e.touches[0].clientX;
            clientY = e.touches[0].clientY;
        } else {
            clientX = e.clientX;
            clientY = e.clientY;
        }

        let x = clientX - rect.left;
        let y = clientY - rect.top;

        // Clamp sun position within container bounds
        // Adjust clamping slightly to keep the center of the sun visible
        x = Math.max(10, Math.min(x, skyContainer.offsetWidth - 10));
        y = Math.max(10, Math.min(y, skyContainer.offsetHeight - 10));


        sunPosition = { x, y };
        // Update position immediately for smooth dragging
        sun.style.left = `${x}px`;
        sun.style.top = `${y}px`;

        drawPolarizationPattern(); // Redraw pattern based on new sun position
    };

    const stopDragging = () => {
        if (!sunDragging) return; // Check flag just in case
        sunDragging = false;
        skyContainer.classList.remove('dragging');
        sun.classList.remove('dragging');
        // Remove event listeners from the document
        document.removeEventListener('mousemove', onDrag);
        document.removeEventListener('mouseup', stopDragging);
        document.removeEventListener('touchmove', onDrag);
        document.removeEventListener('touchend', stopDragging);
    };

    // Attach drag listeners
    sun.addEventListener('mousedown', startDragging);
    sun.addEventListener('touchstart', (e) => {
         // Prevent default touch behavior which might interfere with dragging (e.g., scrolling)
         e.preventDefault();
         // Simulate mouse event for touch handling simplicity in startDragging
         const touch = e.touches[0];
         startDragging({ clientX: touch.clientX, clientY: touch.clientY, target: sun, type: 'touchstart' });
     });


    // Ant Eye/Polarization Info functionality (using mousemove/touchmove on canvas)
    const updateAntEye = (e) => {
         e.preventDefault(); // Prevent potential touch issues

        const rect = skyCanvas.getBoundingClientRect();
        let clientX, clientY;

        if (e.type.startsWith('touch')) {
             if (e.touches.length === 0) return; // No active touch
             clientX = e.touches[0].clientX;
             clientY = e.touches[0].clientY;
         } else {
             clientX = e.clientX;
             clientY = e.clientY;
         }

        const x = clientX - rect.left;
        const y = clientY - rect.top;

        // Clamp ant eye position within container bounds slightly
         const eyeSize = 15; // Approximate size for clamping
         const clampedX = Math.max(eyeSize, Math.min(x, skyCanvas.width - eyeSize));
         const clampedY = Math.max(eyeSize, Math.min(y, skyCanvas.height - eyeSize));


        // Position the ant eye indicator
        antEyeIndicator.style.display = 'block';
        antEyeIndicator.style.left = `${clampedX}px`;
        antEyeIndicator.style.top = `${clampedY}px`;
        // Adjust transform to center emoji (emoji baseline is not centered)
        antEyeIndicator.style.transform = 'translate(-50%, -70%)';


        // Calculate and display polarization direction
        const sunX = sunPosition.x;
        const sunY = sunPosition.y;

        const dx_sun = clampedX - sunX;
        const dy_sun = clampedY - sunY;
        let angle = Math.atan2(dy_sun, dx_sun); // Angle from point to sun

        // Polarization direction is perpendicular to the point-to-sun line
        let polarizationAngle = angle + Math.PI / 2;

        // Normalize angle to be between 0 and PI (polarization is bidirectional)
        polarizationAngle = (polarizationAngle + Math.PI) % Math.PI; // Normalize to 0 to PI

        // Convert to degrees (0-180)
        let polarizationAngleDeg = polarizationAngle * 180 / Math.PI;

        // Update info box position - try to keep it near the indicator but avoid edges
        const infoWidth = 160; // Estimate info box width
        const infoHeight = 50; // Estimate info box height
        let infoLeft = clampedX + 20;
        let infoTop = clampedY - 40;

        // Adjust if too close to right edge
        if (infoLeft + infoWidth > rect.width - 10) {
            infoLeft = clampedX - infoWidth - 10; // Position to the left
        }
        // Adjust if too close to top edge
        if (infoTop < 10) {
            infoTop = clampedY + 20; // Position below
        }
         // Adjust if too close to bottom edge
         if (infoTop + infoHeight > rect.height - 10) {
             infoTop = rect.height - infoHeight - 10; // Anchor to bottom
         }


        polarizationInfo.style.display = 'block';
        polarizationInfo.style.left = `${infoLeft}px`;
        polarizationInfo.style.top = `${infoTop}px`;


        // Update text - A simplified textual description based on the angle
        let directionText;
        if (polarizationAngleDeg >= 170 || polarizationAngleDeg < 10) {
            directionText = "כמעט אופקי";
        } else if (polarizationAngleDeg >= 10 && polarizationAngleDeg < 80) {
            directionText = "אלכסוני";
        } else if (polarizationAngleDeg >= 80 && polarizationAngleDeg < 100) {
             directionText = "כמעט אנכי";
        }
         else if (polarizationAngleDeg >= 100 && polarizationAngleDeg < 170) {
             directionText = "אלכסוני";
         } else {
             directionText = ""; // Should not happen with 0-180 range
         }

        polarizationInfo.innerHTML = `כיוון קיטוב: ${directionText}<br>(${Math.round(polarizationAngleDeg)}°)`;
    };

     skyCanvas.addEventListener('mousemove', updateAntEye);
     skyCanvas.addEventListener('touchmove', updateAntEye);


     skyCanvas.addEventListener('mouseout', () => {
         antEyeIndicator.style.display = 'none';
         polarizationInfo.style.display = 'none';
     });
      skyCanvas.addEventListener('touchend', () => {
         antEyeIndicator.style.display = 'none';
         polarizationInfo.style.display = 'none';
     });


    // Density control
    const updateDensityValueLabel = () => {
        const value = parseInt(densityInput.value);
        let text;
        if (value < 40) text = "נמוכה";
        else if (value < 80) text = "בינונית";
        else text = "גבוהה";
        densityValueSpan.textContent = text;
    };

    densityInput.addEventListener('input', () => {
        drawPolarizationPattern();
        updateDensityValueLabel();
    });


    // Explanation toggle functionality
    const explanationButton = document.getElementById('explanation-button');
    const fullExplanation = document.getElementById('full-explanation');

    explanationButton.addEventListener('click', () => {
        if (fullExplanation.style.display === 'none') {
            fullExplanation.style.display = 'block';
            explanationButton.textContent = 'הסתר הסבר מלא';
             // Optional: Scroll to explanation or make it smooth
             fullExplanation.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            fullExplanation.style.display = 'none';
            explanationButton.textContent = 'איך נמלים רואות אור מקוטב? הצג הסבר מלא';
        }
    });

    // Initialize app
    updateCanvasSize(); // Set initial size and draw pattern
    updateDensityValueLabel(); // Set initial density label

    // Add resize observer if needed for more complex layouts, but simple window resize is enough here
    window.addEventListener('resize', updateCanvasSize);

    // Initial sun position requires canvas size to be set
    // Re-position sun once canvas size is known (after initial updateCanvasSize)
     // sun.style.left = `${sunPosition.x}px`;
     // sun.style.top = `${sunPosition.y}px`;
     // sun.style.transform = 'translate(-50%, -50%)';

});
</script>
---