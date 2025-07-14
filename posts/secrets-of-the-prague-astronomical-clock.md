---
title: "סודות השעון האסטרונומי המסתורי של פראג"
english_slug: secrets-of-the-prague-astronomical-clock
category: "אסטרונומיה"
tags: ["שעון אסטרונומי", "פראג", "אסטרונומיה", "זמן", "היסטוריה של המדע", "מדע ימי הביניים"]
---
# סודות השעון האסטרונומי המסתורי של פראג

ראיתם פעם את השעון האסטרונומי המפורסם בפראג? הוא לא סתם שעון – זו יצירת מופת מהמאה ה-15, לוח שמימי שמקפל בתוכו את תפיסת העולם של ימי הביניים! הוא מלא בחוגות, סמלים מסתוריים, ואפילו מופע מכני קצר כל שעה עגולה. אבל מה בדיוק הוא מראה, ולמה הוא כל כך שונה מהשעון הדיגיטלי על הטלפון שלכם?

הגיע הזמן לגלות את הסודות! שחקו עם הסימולציה למטה, שנו את השעה והתאריך, וצפו כיצד השמש, הירח, וכיפת השמיים נעים. לחצו על חלקים שונים של השעון כדי לגלות את משמעותם!

<div class="app-container">
    <div id="clock-container">
        <canvas id="astronomical-clock" width="600" height="600"></canvas>
         <div id="tooltip" class="tooltip">
            <div class="tooltip-content"></div>
            <button class="tooltip-close">&times;</button>
        </div>
    </div>
    <div class="controls">
        <div class="control-group">
            <label for="time-slider">חקרו את השעה (0-24):</label>
            <input type="range" id="time-slider" min="0" max="23.99" step="0.01" value="12">
            <span id="current-time" class="time-display">12:00</span>
             <button id="play-pause-button" class="control-button">▶️</button>
        </div>
        <div class="control-group">
            <label for="date-picker">בחרו תאריך:</label>
            <input type="date" id="date-picker" value="2023-09-23">
        </div>
    </div>

</div>

<style>
    :root {
        --clock-bg: #f0f0e0; /* Light parchment */
        --sky-day: #4682B4; /* Steel Blue */
        --sky-dawn-dusk: #ff8c00; /* Dark Orange */
        --sky-night: #000d20; /* Very dark blue/black */
        --horizon-line: #fff;
        --zodiac-ring: #a0522d; /* Saddle Brown */
        --sun-color: gold;
        --moon-color: silver;
        --center-boss: #8B4513; /* Saddle Brown */
        --control-bg: #f9f9f9;
        --control-border: #eee;
        --tooltip-bg: rgba(255, 255, 255, 0.98);
        --tooltip-border: #333;
        --text-color: #333;
        --interactive-hover: rgba(255, 255, 0, 0.2); /* Highlight on hover */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        margin: 0;
        padding: 20px;
        background-color: #f4f4f4;
    }

    h1, h2, h3 {
        color: #1a2a3a;
    }

    .app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        margin: 30px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        max-width: 650px; /* Match canvas width + padding */
    }

    #clock-container {
        position: relative;
        width: 600px;
        height: 600px;
        border: 10px solid var(--center-boss); /* Decorative border */
        border-radius: 50%;
        overflow: hidden;
        background: var(--clock-bg);
        box-shadow: inset 0 0 20px rgba(0,0,0,0.2);
    }

    #astronomical-clock {
        display: block;
        background: transparent; /* Background drawn in JS */
        cursor: pointer; /* Indicate interactivity */
    }

    .controls {
        display: flex;
        flex-direction: column; /* Stack controls */
        align-items: center;
        gap: 15px;
        padding: 20px;
        border: 1px solid var(--control-border);
        border-radius: 8px;
        background-color: var(--control-bg);
        width: 90%; /* Make controls slightly wider */
        max-width: 500px;
    }

    .control-group {
        display: flex;
        align-items: center;
        gap: 10px;
        width: 100%;
        justify-content: center; /* Center group items */
    }

    .controls label {
        font-weight: bold;
        color: var(--text-color);
        white-space: nowrap; /* Prevent wrapping */
    }

     .controls input[type="range"] {
         flex-grow: 1; /* Slider takes available space */
          -webkit-appearance: none; /* Override default appearance */
          appearance: none;
          height: 8px;
          background: var(--sky-day);
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
          background: var(--sun-color);
          border-radius: 50%;
          cursor: pointer;
          box-shadow: 0 1px 3px rgba(0,0,0,0.4);
      }

      .controls input[type="range"]::-moz-range-thumb {
          width: 20px;
          height: 20px;
          background: var(--sun-color);
          border-radius: 50%;
          cursor: pointer;
           box-shadow: 0 1px 3px rgba(0,0,0,0.4);
      }

    .time-display {
        font-weight: bold;
        min-width: 50px; /* Reserve space */
         text-align: center;
    }

    .control-button {
        background-color: var(--sky-day);
        color: white;
        border: none;
        border-radius: 4px;
        padding: 5px 10px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease;
    }

    .control-button:hover {
        background-color: #3a72a4;
    }

    #tooltip {
        position: absolute;
        background-color: var(--tooltip-bg);
        border: 1px solid var(--tooltip-border);
        border-radius: 8px;
        padding: 15px;
        max-width: 250px; /* Smaller for better fit */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        z-index: 10;
        display: none;
        pointer-events: none; /* Allows clicks to pass through to canvas */
        opacity: 0;
        transition: opacity 0.3s ease;
        transform: translate(-50%, -100%); /* Position above cursor */
        white-space: normal; /* Allow text wrapping */
         direction: rtl; /* Ensure Hebrew is right-to-left */
         text-align: right;
    }

     #tooltip.visible {
         display: block; /* Show via JS */
         opacity: 1; /* Animate opacity */
     }

    .tooltip-content strong {
        color: #1a2a3a;
    }

    .tooltip-close {
        position: absolute;
        top: 5px;
        left: 5px; /* Position on left for RTL */
        background: none;
        border: none;
        font-size: 1.5em;
        cursor: pointer;
        color: var(--tooltip-border);
        line-height: 1;
         padding: 0;
    }

     .tooltip-close:hover {
         color: #f00;
     }

    #toggle-explanation {
        display: block; /* Ensure it's on its own line */
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #e0e0e0;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease;
    }

    #toggle-explanation:hover {
        background-color: #d0d0d0;
    }

    #explanation-section {
        display: none; /* Hidden by default */
        margin-top: 20px;
        padding: 20px;
        border-top: 1px solid #eee;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }

    #explanation-section h2 {
        margin-bottom: 20px;
        color: #1a2a3a;
    }

    #explanation-section h3 {
         color: #3a72a4;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    #explanation-section p, #explanation-section li {
        line-height: 1.7;
        margin-bottom: 10px;
        color: #555;
    }

    #explanation-section ul {
        margin-bottom: 15px;
    }

    #explanation-section li {
        margin-bottom: 5px;
    }
</style>

<button id="toggle-explanation">לחשוף את הסודות המלאים</button>

<div id="explanation-section">
    <h2>צלילה עמוקה אל נבכי השעון האסטרונומי</h2>

    <p>השעון האסטרונומי בפראג, ה"אורלוי" (Orloj), הוא לא רק מודד זמן – הוא דיאגרמה קוסמית חיה. הוא מספר את סיפור היקום כפי שהבינו אותו באותם ימים, עם כדור הארץ במרכז, ומציג מגוון מערכות זמן שונות ששימשו את אנשי פראג לאורך ההיסטוריה.</p>

    <h3>לוח השעון: מפה של השמיים מפראג</h3>
    <p>הלוח המרכזי, העגול והצבעוני, הוא הלב של השעון. הוא מייצג את כיפת השמיים מעל פראג, מנקודת מבט גאוצנטרית (כדור הארץ במרכז, כידוע). הצבעים אינם סתם קישוט:</p>
    <ul>
        <li><strong>הכחול המרכזי:</strong> השמיים מעל האופק – היום.</li>
        <li><strong>הכתום/אדמדם מסביב לכחול:</strong> אזורי הדמדומים – שחר (Aurola) ושקיעה (Crepusculum).</li>
        <li><strong>השחור החיצוני:</strong> השמיים מתחת לאופק – הלילה.</li>
    </ul>
    <p>על הלוח מצוירים קווים מיוחדים: קו אופקי שמסמן את האופק (נקודת הזריחה משמאל, השקיעה מימין) וקווים מעגליים שמסמנים את הזניט (הנקודה הגבוהה ביותר בשמיים) וקווים נוספים הקשורים לשעות הבבליות.</p>
     <p>מיקום השמש והירח על לוח זה מראה אם הם נמצאים מעל או מתחת לאופק, ומה גובהם בשמיים באותו רגע.</p>

    <h3>מחוג השמש: לא רק השעה המודרנית</h3>
    <p>מחוג השמש הוא אולי המורכב ביותר. הוא מסתיים בסמל שמש מוזהב ונע בשלושה אופנים שונים בו זמנית:</p>
    <ul>
        <li><strong>מיקום יומי:</strong> השמש נעה על פני הלוח הכחול במהלך היום ומתחתיו בלילה. מיקומה על פני הלוח מראה את השעה היומית.</li>
        <li><strong>מיקום שנתי:</strong> המחוג מחובר לגלגל המזלות ומצביע על המזל האסטרולוגי שבו נמצאת השמש באותו תאריך בשנה. תנועה זו קשורה לעונות השנה.</li>
        <li><strong>מערכות זמן עתיקות:</strong>
            <ul>
                <li><strong>שעון מרכז אירופה (CET):</strong> השעה המודרנית (0-24), מוצגת על טבעת חיצונית עם ספרות רומיות מוזהבות. המחוג מצביע עליה.</li>
                <li><strong>שעון בבלי:</strong> מחלק את שעות האור ל-12 חלקים שווים. אורך "שעה" בבלית משתנה עם עונות השנה (קצר יותר בחורף, ארוך יותר בקיץ). מערכת זו מסומנת על ידי קווים מעוקלים על הלוח הכחול הפנימי.</li>
                <li><strong>שעון צ'כי עתיק (או "שעון איטלקי"):</strong> סופר שעות מהשקיעה. שעה 1 היא שעה אחרי השקיעה, ושעה 24 היא רגע השקיעה ביום שלמחרת. מערכת זו מוצגת על טבעת חיצונית נפרדת עם ספרות גותיות עתיקות.</li>
            </ul>
        </li>
    </ul>
    <p>היכולת של השעון להציג את כל אלו במקביל הייתה הישג טכנולוגי ותאולוגי עצום, והקלה על החיים בזמנים שבהם לא היה סטנדרט זמן אחיד.</p>

    <h3>מחוג הירח: תנועה ופזה שמימית</h3>
    <p>מחוג הירח, שמסתיים בכדור כסף-שחור, נע על הלוח בדומה למחוג השמש ומציין את מיקומו היומי של הירח בשמיים ביחס לאופק ולגלגל המזלות. הייחוד שלו הוא הכדור עצמו: הוא מסתובב סביב צירו ומשנה את כמות האור עליו כדי להציג את הפאזה המדויקת של הירח באותו רגע (מולד, חצי, מלא וכו').</p>

    <h3>גלגל המזלות: מסלול השמש השנתי</h3>
    <p>הטבעת החיצונית ביותר שנעה היא גלגל המזלות האסטרולוגי (האקליפטיקה). היא מסומנת בסימני המזלות ומייצגת את המסלול הנתיב שבו נראית השמש כשהיא נעה בשמיים לאורך השנה. הגלגל הזה מסתובב לאט לאורך 24 שעות כדי לשקף את תנועת הכוכבים ביחס לזמן המקומי, בעוד השמש והירח נעים על פניו.</p>

    <h3>מדוע שעון כזה? אסטרונומיה, אסטרולוגיה ועוד</h3>
    <p>בימי הביניים, האסטרונומיה והאסטרולוגיה היו שזורות זו בזו, ושתיהן נחשבו לחלק חשוב בהבנת סדר היקום כפי שנקבע על ידי האל. שעונים אסטרונומיים נבנו לא רק כדי לדעת מה השעה, אלא גם כדי לדגמן את התנועות השמימיות המורכבות, לחשב מיקומים אסטרולוגיים, ולהציג את התמונה הקוסמולוגית העדכנית. השעון של פראג היה כלי מדעי, חינוכי, ציבורי ואפילו פילוסופי.</p>

    <h3>הלב הפועם: המנגנון המכני</h3>
    <p>כל המופע השמימי המרהיב הזה מתאפשר הודות למנגנון מכני גאוני ומורכב להפליא, חבוי בתוך מגדל העירייה הישן. מערכת מסועפת של גלגלי שיניים מחוברים זה לזה ביחסים מתמטיים מדויקים מחשבת באופן מכני את התנועות היומיות והשנתיות של השמש, הירח, גלגל המזלות, ואפילו את פאזת הירח וזמני הזריחה/שקיעה המשתנים. זו היתה פסגת הטכנולוגיה של ימי הביניים.</p>
</div>

<script>
    const canvas = document.getElementById('astronomical-clock');
    const ctx = canvas.getContext('2d');
    const timeSlider = document.getElementById('time-slider');
    const datePicker = document.getElementById('date-picker');
    const currentTimeSpan = document.getElementById('current-time');
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationSection = document.getElementById('explanation-section');
    const tooltip = document.getElementById('tooltip');
    const tooltipContent = tooltip.querySelector('.tooltip-content');
    const tooltipClose = tooltip.querySelector('.tooltip-close');
    const playPauseButton = document.getElementById('play-pause-button');

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = Math.min(centerX, centerY) * 0.85; // Make it slightly smaller for outer rings

    let animationFrameId = null;
    let isPlaying = false;
    const animationSpeed = 0.05; // Hours per frame (approx)

    // Simplified Clickable Areas with improved hit testing metadata
    const clickableElements = [
        { name: 'לוח השעון (השמיים)', explanation: 'הלוח הצבעוני הוא ייצוג של כיפת השמיים מעל פראג: כחול ליום, שחור ללילה, וכתום לדמדומים. הוא מראה אם גרמי השמיים מעל או מתחת לאופק.', shape: 'circle', priority: 1, /* More specific bounds needed */ bounds: { x: centerX, y: centerY, r: radius * 0.7 } }, // Inner day/night area
        { name: 'מחוג השמש', explanation: 'מחוג השמש מראה את מיקום השמש היומי והשנתי ביחס לכיפת השמיים וגלגל המזלות, ואת השעה במערכות זמן שונות. הוא עוזר לזהות זריחה ושקיעה.', shape: 'hand', priority: 3, handType: 'sun', hitRadius: 15 }, // hitRadius for hand symbol
        { name: 'מחוג הירח', explanation: 'מחוג הירח עוקב אחר מיקום הירח בשמיים ומציג באופן חזותי את הפאזה הנוכחית שלו (מולד, רבע, מלא).', shape: 'hand', priority: 3, handType: 'moon', hitRadius: 12 }, // hitRadius for hand symbol
         { name: 'גלגל המזלות', explanation: 'הטבעת החיצונית שנעה. מציגה את סימני המזלות ומסמלת את מסלול השמש השנתי בשמיים (האקליפטיקה). מיקום השמש והירח עליו משתנה במהלך השנה.', shape: 'ring', priority: 2, bounds: { x: centerX, y: centerY, innerR: radius * 0.75, outerR: radius * 0.9 } }, // Zodiac ring area
        { name: 'קווי האופק', explanation: 'הקווים האופקיים על הלוח הכחול מסמלים את האופק. השמש או הירח מעל הקו = מעל האופק; מתחת לקו = מתחת לאופק. צד שמאל הוא מזרח (זריחה), צד ימין הוא מערב (שקיעה).', shape: 'line-segment', priority: 2, bounds: { x1: centerX - radius * 0.7, y1: centerY, x2: centerX + radius * 0.7, y2: centerY }, hitWidth: 10 }, // Simplified horizontal line area
         { name: 'שעון מרכז אירופה (CET)', explanation: 'הטבעת החיצונית עם הספרות הרומיות (I-XXIV) מציגה את השעה המודרנית (0-24). מחוג השמש מצביע גם על שעה זו.', shape: 'ring', priority: 2, bounds: { x: centerX, y: centerY, innerR: radius * 0.92, outerR: radius * 1.0 } }, // Outer 24h ring area (approx)
          // Add more complex shapes/areas as drawing improves (Babylonian lines, Old Czech ring)
    ];


    function drawClock(hours, date) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // --- Draw Background and Sky ---
        // Gradient for sky transitions (conceptual)
         const skyGradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, radius * 0.95);
         skyGradient.addColorStop(0, varToString('--sky-day')); // Center is day
         skyGradient.addColorStop(0.5, varToString('--sky-day'));
         skyGradient.addColorStop(0.6, varToString('--sky-dawn-dusk')); // Transition to dawn/dusk
         skyGradient.addColorStop(0.8, varToString('--sky-night')); // Transition to night
         skyGradient.addColorStop(1, varToString('--sky-night')); // Outer is night

        ctx.fillStyle = skyGradient;
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius * 1.05, 0, Math.PI * 2); // Draw slightly larger than radius
        ctx.fill();

         // Mask the sky with the background parchment color
         ctx.globalCompositeOperation = 'destination-atop';
         ctx.fillStyle = varToString('--clock-bg');
         ctx.beginPath();
         ctx.arc(centerX, centerY, radius * 1.05, 0, Math.PI * 2);
         ctx.fill();
         ctx.globalCompositeOperation = 'source-over'; // Reset blending mode

        // --- Draw Fixed Features ---

        // Draw Horizon Line
        ctx.strokeStyle = varToString('--horizon-line');
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(centerX - radius * 0.8, centerY);
        ctx.lineTo(centerX + radius * 0.8, centerY);
        ctx.stroke();

         // Draw Meridian Line (Zenith/Nadir)
        ctx.strokeStyle = varToString('--horizon-line');
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(centerX, centerY - radius * 0.8);
        ctx.lineTo(centerX, centerY + radius * 0.8);
        ctx.stroke();


        // Draw Babylonian Time Lines (Conceptual - radial lines within day zone)
        ctx.strokeStyle = 'rgba(0, 0, 0, 0.2)';
        ctx.lineWidth = 1;
        // To be accurate, these depend on sunrise/sunset time, which changes with date/lat.
        // For visualization, draw 12 lines spaced within the approximate day arc (180 degrees)
        const dayArcStart = Math.PI * 0.2; // Approx angle for dawn
        const dayArcEnd = Math.PI * 0.8; // Approx angle for dusk
         for(let i=1; i<12; i++) {
             const angle = dayArcStart + (dayArcEnd - dayArcStart) * (i/12);
              ctx.beginPath();
              ctx.moveTo(centerX, centerY);
              ctx.lineTo(centerX + radius * 0.75 * Math.cos(angle), centerY + radius * 0.75 * Math.sin(angle));
              ctx.stroke();
         }


         // --- Draw Zodiac Ring ---
        // This ring should rotate based on the date.
        // Simplified rotation: 360 degrees over 365 days.
        const dayOfYear = (date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24;
        const zodiacRotation = (dayOfYear / 365.25) * Math.PI * 2; // Rotation angle for the year

        ctx.strokeStyle = varToString('--zodiac-ring');
        ctx.lineWidth = radius * 0.1; // Make the ring thicker
        ctx.lineCap = 'butt'; // Standard ends
        ctx.beginPath();
        // Draw full circle for the ring background
        ctx.arc(centerX, centerY, radius * 0.825, 0, Math.PI * 2);
        ctx.stroke();

        // Add Zodiac symbols (simplified - static positions relative to ring)
         const zodiacSigns = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"];
         ctx.font = '20px Arial';
         ctx.fillStyle = varToString('--text-color');
         ctx.textAlign = 'center';
         ctx.textBaseline = 'middle';
         const zodiacRadius = radius * 0.825;
         for (let i = 0; i < 12; i++) {
             // Position symbols around the rotating ring
             // Angle relative to the ring's rotation
             const angle = (i / 12) * Math.PI * 2 + zodiacRotation - Math.PI / 2; // Start Aries near top (approx)
             const textX = centerX + zodiacRadius * Math.cos(angle);
             const textY = centerY + zodiacRadius * Math.sin(angle);
             ctx.save();
             ctx.translate(textX, textY);
             ctx.rotate(angle + Math.PI / 2); // Rotate text to face outwards (approx)
             ctx.fillText(zodiacSigns[i], 0, 0);
             ctx.restore();
         }


        // --- Draw Outer 24-hour dial (CET) ---
        ctx.strokeStyle = varToString('--text-color');
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius * 0.95, 0, Math.PI * 2);
        ctx.stroke();

         // Add 24-hour numerals (Roman numerals)
         const romanNumerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV"];
         ctx.font = '16px serif'; // Use a serif font for classic look
         ctx.fillStyle = varToString('--text-color');
         ctx.textAlign = 'center';
         ctx.textBaseline = 'middle';
         const dialRadius = radius * 0.98;
        // The 24h dial is arranged such that 12 is at the bottom, 6 is left, 18 is right, 0/24 is top.
        // Need to map hours (0-23) to angles. 0h = top (angle -PI/2), 6h = right (0), 12h = bottom (PI/2), 18h = left (PI).
        // Angle = (hour / 24) * 2*PI - PI/2. Adjust for 0-24 cycle and 12 at bottom.
         for (let i = 0; i < 24; i++) {
             const hour = i; // 0 to 23
             // Map 0-23 to angles where 0 is up, 6 is right, 12 is down, 18 is left.
             // 0h is at top (-PI/2), 6h is at right (0), 12h is at bottom (PI/2), 18h is at left (PI), 24h is same as 0h.
             // Angle = (hour / 24) * 2*PI - PI/2
             const angle = (hour / 24) * Math.PI * 2 - Math.PI / 2;
             const textX = centerX + dialRadius * Math.cos(angle);
             const textY = centerY + dialRadius * Math.sin(angle);
              // For 0, label is XXIV
              const label = (hour === 0 ? romanNumerals[23] : romanNumerals[hour -1]);
              ctx.fillText(label, textX, textY);
         }


        // --- Calculate and Draw Hands ---

        // Get current time (hours) from slider
        const currentHours = parseFloat(hours); // 0-23.99
        const currentDate = new Date(date);

        // Sun Hand Position
        // Daily position: Based on 24 hours. 0h/24h at top, 12h at bottom. (Like 24h dial)
        // Annual position: Affects radial distance (closer to center in winter, further in summer concept).
        // Precise calculation is complex (equation of time, declination). Use a conceptual radial change.
        // Day of year approx affects radial pos. Sept 23 (value="2023-09-23") is near autumnal equinox.
        const dayOfYearForSun = (currentDate - new Date(currentDate.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24;
        const annualRadialOffset = Math.sin((dayOfYearForSun / 365.25) * Math.PI * 2) * radius * 0.05; // Sine wave approx radial change
        const sunHandRadialPos = radius * 0.75 + annualRadialOffset; // Base radial pos + seasonal change

        const sunAngle = (currentHours / 24) * Math.PI * 2 - Math.PI / 2; // Angle on the 24h cycle (0h top, 12h bottom)
        const sunX = centerX + sunHandRadialPos * Math.cos(sunAngle);
        const sunY = centerY + sunHandRadialPos * Math.sin(sunAngle);

        // Draw Sun Hand line
        ctx.strokeStyle = varToString('--sun-color');
        ctx.lineWidth = 4;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(sunX, sunY);
        ctx.stroke();

        // Draw Sun symbol
        ctx.fillStyle = varToString('--sun-color');
        ctx.beginPath();
        ctx.arc(sunX, sunY, 10, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#B8860B'; // Dark goldenrod
        ctx.lineWidth = 1;
        ctx.stroke();


         // Moon Hand Position
        // Daily position: Based on actual lunar transit time (approx 24h 50m cycle).
        // This is complex. For simplicity, let's make it follow a 24h cycle but with a slight phase offset from the sun.
        // The actual moon cycle is ~29.5 days for phases, which affects its position relative to the sun.
        // Approximate the moon's daily movement slightly delayed vs sun over a month.
        const daysSinceEpoch = currentDate.getTime() / (1000 * 60 * 60 * 24);
        const lunarCycleProgress = (daysSinceEpoch / 29.530588) % 1; // Progress through lunar phase cycle
        const moonDailyOffsetHours = lunarCycleProgress * 24; // Conceptual daily offset based on phase

        const moonAngle = ((currentHours + moonDailyOffsetHours) / 24) * Math.PI * 2 - Math.PI / 2; // Angle
        const moonHandRadialPos = radius * 0.6; // Slightly shorter hand
        const moonX = centerX + moonHandRadialPos * Math.cos(moonAngle);
        const moonY = centerY + moonHandRadialPos * Math.sin(moonAngle);

        // Draw Moon Hand line
        ctx.strokeStyle = varToString('--moon-color');
        ctx.lineWidth = 4;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(moonX, moonY);
        ctx.stroke();

        // Draw Moon symbol with phase
        ctx.fillStyle = varToString('--moon-color');
        ctx.beginPath();
        ctx.arc(moonX, moonY, 8, 0, Math.PI * 2);
        ctx.fill();
         ctx.strokeStyle = '#A9A9A9'; // Dark gray
        ctx.lineWidth = 1;
        ctx.stroke();

         // Draw the shadow for the moon phase (Simplified: uses lunarCycleProgress)
         // 0 = New Moon (fully dark), 0.5 = Full Moon (fully light), 0.25 = First Quarter, 0.75 = Third Quarter
         // We draw a circle mask over the moon symbol.
         const phaseAngle = lunarCycleProgress * Math.PI * 2; // 0..2*PI over the cycle
         const moonShadowColor = '#000d20'; // Use night sky color for shadow

         ctx.fillStyle = moonShadowColor;
         ctx.beginPath();
         // The shape of the shadow is complex (a circle masking another circle).
         // Simplification: draw a portion of a circle or a crescent.
         // Let's draw a moving half-circle mask across the moon based on phase.
         const shadowOffsetX = Math.cos(phaseAngle) * 8; // Move mask left/right
         const shadowDirection = Math.sin(phaseAngle) > 0 ? 1 : -1; // Which side is lit?
          const startAngle = phaseAngle - Math.PI/2;
          const endAngle = phaseAngle + Math.PI/2;


         if (lunarCycleProgress > 0 && lunarCycleProgress < 0.5) { // Waxing
              ctx.arc(moonX + shadowOffsetX, moonY, 8, startAngle, endAngle, true);
         } else if (lunarCycleProgress > 0.5 && lunarCycleProgress < 1) { // Waning
             ctx.arc(moonX + shadowOffsetX, moonY, 8, startAngle, endAngle, false);
         } else if (lunarCycleProgress === 0 || lunarCycleProgress === 1) { // New Moon (full shadow)
              ctx.arc(moonX, moonY, 8, 0, Math.PI * 2);
         }
         // For Full Moon (0.5), draw no shadow (implicit)

        ctx.fill();


        // --- Center Boss ---
        ctx.fillStyle = varToString('--center-boss');
        ctx.beginPath();
        ctx.arc(centerX, centerY, 15, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 1;
        ctx.stroke();


        // --- Update Clickable Element Positions ---
         const sunHandElement = clickableElements.find(el => el.handType === 'sun');
         if (sunHandElement) {
             sunHandElement.endX = sunX; // Store calculated end point
             sunHandElement.endY = sunY;
             sunHandElement.startX = centerX;
             sunHandElement.startY = centerY;
         }
          const moonHandElement = clickableElements.find(el => el.handType === 'moon');
         if (moonHandElement) {
              moonHandElement.endX = moonX; // Store calculated end point
              moonHandElement.endY = moonY;
               moonHandElement.startX = centerX;
               moonHandElement.startY = centerY;
         }
         // Zodiac ring pos is handled by the zodiacRotation calculation

         // Highlight element on hover (handled by mousemove)
    }

    function updateClock() {
        const hours = parseFloat(timeSlider.value);
        const date = new Date(datePicker.value);

        // Display current time from slider
        const displayHours = Math.floor(hours % 24);
        const displayMinutes = Math.floor((hours - displayHours) * 60);
        currentTimeSpan.textContent = `${String(displayHours).padStart(2, '0')}:${String(displayMinutes).padStart(2, '0')}`;

        drawClock(hours, date);
    }

     function varToString(variableName) {
        return getComputedStyle(document.documentElement).getPropertyValue(variableName).trim();
    }


    // --- Animation Loop ---
    function animateClock() {
        if (!isPlaying) return;

        let currentHours = parseFloat(timeSlider.value);
        currentHours += animationSpeed / 60; // Advance time slider (e.g., 1 minute simulation per animation frame)

        // Wrap around 24 hours
        if (currentHours >= 24) {
            currentHours = currentHours % 24;
            // Optionally advance date if a full day passes
            // const currentDate = new Date(datePicker.value);
            // currentDate.setDate(currentDate.getDate() + 1);
            // datePicker.value = currentDate.toISOString().split('T')[0];
        }

        timeSlider.value = currentHours; // Update slider position
        updateClock(); // Redraw clock with new time

        animationFrameId = requestAnimationFrame(animateClock); // Continue animation
    }

    function togglePlayPause() {
        isPlaying = !isPlaying;
        if (isPlaying) {
            playPauseButton.textContent = '⏸️';
            animateClock(); // Start animation loop
        } else {
            playPauseButton.textContent = '▶️';
            cancelAnimationFrame(animationFrameId); // Stop animation
        }
    }

    // --- Interaction Logic ---

    // Toggle Explanation Section
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'להסתיר את הסודות המלאים' : 'לחשוף את הסודות המלאים';
         // Scroll to the section if showing it? Optional.
         if (!isHidden) {
             explanationSection.scrollIntoView({ behavior: 'smooth' });
         }
    });


    // Handle Mouse Move for Hover Highlighting and Tooltips
    canvas.addEventListener('mousemove', (event) => {
         const rect = canvas.getBoundingClientRect();
         const x = event.clientX - rect.left;
         const y = event.clientY - rect.top;

         let hoveredElement = null;

         // Check clickable areas (more robust hit testing)
         // Iterate in reverse priority order to prefer hands/symbols over background areas
         for (const el of [...clickableElements].sort((a, b) => b.priority - a.priority)) {
             let isHovered = false;

             if (el.shape === 'circle') {
                 const dist = Math.sqrt((x - el.bounds.x)**2 + (y - el.bounds.y)**2);
                 if (dist > (el.bounds.r - 20) && dist < el.bounds.r + 20) { // Add some padding for hit area
                     isHovered = true;
                 }
             } else if (el.shape === 'ring') {
                 const dist = Math.sqrt((x - el.bounds.x)**2 + (y - el.bounds.y)**2);
                 if (dist > el.bounds.innerR && dist < el.bounds.outerR) {
                      isHovered = true;
                 }
             } else if (el.shape === 'hand') {
                 // Check distance to the line segment and the symbol at the end
                 // Distance from point to line segment (more accurate)
                 const startX = el.startX;
                 const startY = el.startY;
                 const endX = el.endX;
                 const endY = el.endY;
                 const distToSymbol = Math.sqrt((x - endX)**2 + (y - endY)**2);

                 // Check distance from click (x, y) to the line segment from (startX, startY) to (endX, endY)
                 // Uses dot product and clamping. Found from online resources for geometry.
                 const lenSq = (endX - startX)**2 + (endY - startY)**2;
                 let t = ((x - startX) * (endX - startX) + (y - startY) * (endY - startY)) / lenSq;
                 t = Math.max(0, Math.min(1, t));
                 const closestX = startX + t * (endX - startX);
                 const closestY = startY + t * (endY - startY);
                 const distToLine = Math.sqrt((x - closestX)**2 + (y - closestY)**2);

                 if (distToSymbol < el.hitRadius || distToLine < (el.lineWidth || 10)) { // Check near symbol or line
                      isHovered = true;
                 }
            } else if (el.shape === 'line-segment') {
                 // Check distance to the line segment - simplified horizontal check
                 const lineY = el.bounds.y1;
                 const lineStartX = el.bounds.x1;
                 const lineEndX = el.bounds.x2;
                  // Check if Y is within hitWidth of lineY AND X is within the segment bounds
                 if (Math.abs(y - lineY) < el.hitWidth / 2 && x >= lineStartX && x <= lineEndX) {
                      isHovered = true;
                 }
            }

            if (isHovered) {
                hoveredElement = el;
                break; // Found the highest priority element
            }
         }

        if (hoveredElement) {
            // Show tooltip
            tooltipContent.innerHTML = `<strong>${hoveredElement.name}:</strong> ${hoveredElement.explanation}`;
            // Position tooltip near cursor, but adjusted to fit
             tooltip.style.left = `${x}px`;
             tooltip.style.top = `${y}px`;
            tooltip.classList.add('visible'); // Use class for opacity transition

             // Add hover effect (re-draw or CSS) - drawing is better for canvas elements
             // For now, let's just handle the tooltip. Visual hover effect is complex to draw efficiently.
        } else {
            // Hide tooltip
             tooltip.classList.remove('visible');
             // tooltip.style.display = 'none'; // Hide after transition
             setTimeout(() => {
                 if (!tooltip.classList.contains('visible')) {
                     tooltip.style.display = 'none';
                 }
             }, 300); // Match CSS transition duration
        }
    });

     // Hide tooltip when close button is clicked
     tooltipClose.addEventListener('click', () => {
        tooltip.classList.remove('visible');
         setTimeout(() => tooltip.style.display = 'none', 300);
     });

    // Event listeners for controls
    timeSlider.addEventListener('input', () => {
        if (isPlaying) togglePlayPause(); // Pause animation on manual slider change
        updateClock();
    });
    datePicker.addEventListener('change', updateClock); // Date change triggers redraw
    playPauseButton.addEventListener('click', togglePlayPause);


    // Initial draw
    updateClock();


</script>
```