---
title: "זיכרון העתיד בידיים שלך: הדמיית זיכרון שינוי פאזה (PCM)"
english_slug: future-memory-phase-change-memory-simulation
category: "מדעים מדויקים / פיזיקה"
tags: [זיכרון מחשב, Phase Change Memory, מדע חומרים, אחסון נתונים, אלקטרוניקה, טכנולוגיה]
---
# זיכרון העתיד בידיים שלך: הדמיית זיכרון שינוי פאזה (PCM)

דמיינו זיכרון למחשבים ולטלפונים שלנו שיהיה מהיר כברק, שיאפשר אחסון נתונים ללא הגבלה (כמעט), וגם יצרוך פחות חשמל. נשמע כמו מדע בדיוני? הכירו את זיכרון שינוי הפאזה (PCM - Phase Change Memory), טכנולוגיה פורצת דרך שמבוססת על עיקרון פיזיקלי מדהים: שינוי מצב צבירה מבוקר של חומר זכוכיתי מיוחד.

בואו נתנסה! השתמשו בפקדים כדי לשלוח פולסים חשמליים לתא זיכרון בודד וראו כיצד הוא משנה את מצבו ואת הערך הלוגי שהוא אוגר.

<div id="pcm-simulation" class="simulation-container">
    <div class="simulation-viz">
        <div id="pcm-cell" class="amorphous">
             <div class="cell-inner"></div>
             <div class="animation-layer heat"></div>
             <div class="animation-layer cool"></div>
        </div>
        <div class="cell-label">חומר ה-PCM (סגסוגת GST)</div>
    </div>

    <div class="status-area">
        <h3>מצב התא</h3>
        <div class="status-row">
            <label>התנגדות:</label>
            <div class="resistance-bar-container">
                <div id="resistance-bar" class="high"></div>
            </div>
        </div>
        <div class="status-row">
            <label>ערך לוגי:</label>
            <div id="logical-value" class="value-0">0</div>
        </div>
        <div class="status-row">
             <label>מצב צבירה:</label>
             <div id="phase-state">אמורפי</div>
        </div>
         <div class="status-message" id="status-message">מוכן</div>
    </div>

    <div class="controls-area">
        <h3>בקרת פולס חשמלי</h3>
        <div class="control-group pulse-type-group">
            <label>סוג פעולה רצויה:</label>
            <input type="radio" id="pulse-reset" name="pulse-type" value="reset" checked>
            <label for="pulse-reset">כתיבת '0' (Reset)</label>
            <input type="radio" id="pulse-set" name="pulse-type" value="set">
            <label for="pulse-set">כתיבת '1' (Set)</label>
        </div>

        <div class="control-group">
             <label for="pulse-intensity">עוצמת הפולס:</label>
             <input type="range" id="pulse-intensity" min="1" max="10" value="7">
             <span id="intensity-value">7</span>
             <div class="slider-hint">(מייצג טמפרטורת חימום מקסימלית)</div>
        </div>

         <div class="control-group">
             <label for="pulse-duration">משך הפולס:</label>
             <input type="range" id="pulse-duration" min="1" max="10" value="4">
             <span id="duration-value">4</span>
              <div class="slider-hint">(מייצג זמן שהייה בטמפרטורה ומהירות קירור)</div>
        </div>

        <button id="apply-pulse">הפעל פולס וצפה בשינוי</button>
    </div>
</div>

<button id="toggle-explanation" class="explanation-toggle-button">הצג/הסתר הסבר מעמיק</button>

<div id="explanation" style="display: none;">
    <h2>צלילה לעומק: עקרונות הפעולה של זיכרון שינוי פאזה (PCM)</h2>
    <p>זיכרון מבוסס שינוי פאזה (PCM) הוא טכנולוגיית זיכרון מתקדמת ולא נדיפה (המידע נשמר גם ללא חשמל), שמציעה יתרונות משמעותיים על פני טכנולוגיות קיימות כמו זיכרון פלאש (Flash Memory). היתרונות הבולטים כוללים מהירות גישה גבוהה, עמידות יוצאת דופן למחזורי כתיבה ומחיקה, ויכולת אחסון צפופה.</p>

    <h3>הליבה הפיזיקלית: מצבי צבירה שונים, התנגדות שונה</h3>
    <p>הקסם של ה-PCM טמון בחומרים מיוחדים, המכונים חומרים כאלקוגניים (Chalcogenides). סגסוגת נפוצה נקראת GST (הרכב טיפוסי: Ge₂Sb₂Te₅). חומרים אלו יכולים לעבור באופן הפיך בין שני מצבי צבירה עיקריים המשמשים לאחסון מידע:</p>
    <ul>
        <li>**מצב אמורפי (Amorphous):** מבנה אטומי לא מסודר, דמוי זכוכית. במצב זה, תנועת האלקטרונים מוגבלת, ולכן החומר מציג **התנגדות חשמלית גבוהה מאוד**. מצב זה משמש בדרך כלל לייצוג הערך הלוגי **'0'**.</li>
        <li>**מצב גבישי (Crystalline):** מבנה אטומי מסודר ומחזורי. במצב זה, האלקטרונים נעים בחופשיות יחסית, מה שמקנה לחומר **התנגדות חשמלית נמוכה**. מצב זה משמש בדרך כלל לייצוג הערך הלוגי **'1'**.</li>
    </ul>
    <p>שינוי מצבי הצבירה הללו מושג באמצעות חימום וקירור מבוקרים של פיסת החומר הזעירה.</p>

    <h3>קסם הכתיבה: פולסים שמעצבים את החומר</h3>
    <p>כתיבת מידע לתא PCM בודד מתבצעת על ידי העברת פולס זרם חשמלי קצר דרך פיסת חומר ה-GST. האנרגיה החשמלית הופכת במהירות לחום, והטמפרטורה המקסימלית אליה מגיע החומר, יחד עם משך הפולס וקצב הקירור, קובעים את מצב הצבירה הסופי:</p>
    <ul>
        <li>**פעולת 'ריסט' (Reset) - כתיבת '0':** כדי להגיע למצב האמורפי (התנגדות גבוהה, '0'), שולחים פולס זרם **חזק מאוד וקצר מאוד**. פולס זה מחמם את החומר לטמפרטורה גבוהה מטמפרטורת ההתכה (מעל 600°C). מיד לאחר מכן, הפולס נפסק והחומר מתקרר **במהירות עצומה** (עשרות או מאות פיקו-שניות). קצב הקירור המסחרר אינו מאפשר לאטומים זמן מספיק להסתדר במבנה גבישי מסודר, והחומר "קופא" במצבו האמורפי הלא מסודר.</li>
        <li>**פעולת 'סט' (Set) - כתיבת '1':** כדי להגיע למצב הגבישי (התנגדות נמוכה, '1'), שולחים פולס זרם **מתון יחסית וארוך יותר**. פולס זה מחמם את החומר לטמפרטורה נמוכה יותר - טמפרטורת ההתגבשות (כ-200-300°C), הנמוכה מטמפרטורת ההתכה. בטמפרטורה זו ובמשך זמן מספיק (מספר ננו-שניות), יש לאטומים די אנרגיה וזמן לנוע ולהסתדר במבנה גבישי מסודר ויציב.</li>
    </ul>
    <p>שימו לב שבסימולציה, העוצמה מייצגת בעיקר את הטמפרטורה המקסימלית, והמשך מייצג את הזמן שהחומר שוהה בטמפרטורה גבוהה ואת קצב הקירור המושפע ממשך הפולס.</p>

    <h3>קריאת מידע: פולס עדין שמגלה את הסוד</h3>
    <p>קריאת המידע מתא PCM מתבצעת על ידי העברת פולס זרם **חלש מאוד**, שאינו חזק מספיק כדי לחמם את החומר במידה משמעותית ולגרום לשינוי פאזה. מודדים את ההתנגדות החשמלית של התא: התנגדות גבוהה משמעותה שהתא במצב אמורפי ומאחסן '0', בעוד התנגדות נמוכה מצביעה על מצב גבישי המאחסן '1'.</p>

    <h3>מעבר ל-0 ו-1: אחסון מרובה רמות (MLC)</h3>
    <p>אחד היתרונות המרתקים של PCM הוא היכולת ליישם אחסון מרובה רמות (Multi-Level Cell - MLC). על ידי שליחת פולסים בעוצמות ומשכים **ביניים**, ניתן ליצור דרגות שונות של אמורפיות או גבישיות חלקית בחומר. לכל דרגת שילוב כזו יש התנגדות חשמלית אופיינית. מדידת ההתנגדות במדויק מאפשרת להבחין בין מספר מצבים שונים מעבר ל-0 ו-1 בלבד, ולאחסן 2 ביטים (4 רמות), 3 ביטים (8 רמות) או יותר בתא פיזי בודד. הדבר מגדיל משמעותית את צפיפות האחסון.</p>

     <p>טכנולוגיית ה-PCM ממשיכה להתפתח ומבטיחה מהפכה בתחום האחסון והזיכרון בעתיד הקרוב והרחוק.</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --warning-color: #ffc107;
        --light-bg: #f8f9fa;
        --dark-bg: #343a40;
        --border-color: #dee2e6;
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --border-radius: 8px;
        --amorphous-color: #f05454; /* Soft red */
        --crystalline-color: #30475e; /* Dark blue/gray */
        --amorphous-pattern: repeating-linear-gradient(-45deg, var(--amorphous-color) 0px, var(--amorphous-color) 5px, #f5f5f5 5px, #f5f5f5 10px);
        --crystalline-pattern: repeating-linear-gradient(0deg, var(--crystalline-color) 0px, var(--crystalline-color) 5px, #e0e0e0 5px, #e0e0e0 10px);
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Hebrew */
        text-align: right; /* Hebrew */
        background-color: var(--light-bg);
        color: var(--dark-bg);
    }

    h1, h2, h3 {
        color: var(--dark-bg);
    }

    #pcm-simulation.simulation-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 30px;
        margin-top: 30px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: #ffffff;
        box-shadow: var(--shadow);
    }

    .simulation-viz, .status-area, .controls-area {
        padding: 20px;
        background-color: #fff;
        border: 1px solid #eee;
        border-radius: var(--border-radius);
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        align-items: center; /* Center content within each area */
        text-align: center;
    }

     .simulation-viz {
         justify-content: center;
     }


    #pcm-cell {
        width: 180px; /* Slightly larger */
        height: 180px; /* Slightly larger */
        border: 3px solid; /* Thicker border */
        margin-bottom: 15px;
        position: relative;
        overflow: hidden;
        border-radius: 15px; /* More rounded */
        box-shadow: inset 0 0 15px rgba(0,0,0,0.2); /* Inner shadow for depth */
        transition: border-color 0.5s ease;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .cell-inner {
        width: 100%;
        height: 100%;
        background-size: 20px 20px; /* Control pattern size */
        transition: background 1s ease-in-out; /* Smooth transition between patterns */
    }

    #pcm-cell.amorphous .cell-inner {
         background-image: var(--amorphous-pattern);
         border-color: var(--amorphous-color);
    }

    #pcm-cell.crystalline .cell-inner {
        background-image: var(--crystalline-pattern);
        border-color: var(--crystalline-color);
    }

    .cell-label {
        font-size: 0.9em;
        color: #555;
        text-align: center;
        margin-top: auto; /* Push label to bottom if area has height */
    }

    .status-area {
        text-align: right; /* Hebrew */
        align-items: flex-end; /* Align content to the right */
    }

    .status-area h3 {
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        width: 100%; /* Border spans full width */
        text-align: center;
    }

    .status-row {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 10px;
        width: 100%; /* Rows span full width */
    }

    .status-row label {
        font-weight: bold;
        min-width: 90px; /* Align labels */
        text-align: right;
    }

    .resistance-bar-container {
        flex-grow: 1;
        height: 25px; /* Taller bar */
        border: 1px solid var(--border-color);
        border-radius: 12.5px; /* Fully rounded */
        overflow: hidden;
        background-color: #eee;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    #resistance-bar {
        height: 100%;
        background-color: var(--success-color); /* Green */
        transition: width 0.8s ease; /* Slower, smoother transition */
    }

    #resistance-bar.high {
        width: 90%; /* Higher visual representation */
        background-color: var(--danger-color); /* Red */
    }

    #resistance-bar.low {
        width: 10%; /* Lower visual representation */
        background-color: var(--success-color); /* Green */
    }

    #logical-value {
        min-width: 40px; /* Larger size */
        padding: 8px 15px;
        border-radius: 6px;
        font-weight: bold;
        text-align: center;
        transition: background-color 0.5s ease, color 0.5s ease;
        font-size: 1.1em;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

     #logical-value.value-0 {
        background-color: var(--danger-color); /* Red for 0 */
        color: white;
     }

     #logical-value.value-1 {
        background-color: var(--success-color); /* Green for 1 */
        color: white;
     }

     #phase-state {
        font-weight: bold;
        color: var(--primary-color);
     }

     .status-message {
         margin-top: 15px;
         font-size: 0.9em;
         color: #555;
         min-height: 1.2em; /* Reserve space */
     }

    .controls-area {
        text-align: right; /* Hebrew */
         align-items: flex-end; /* Align content to the right */
    }

    .controls-area h3 {
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
         width: 100%; /* Border spans full width */
        text-align: center;
    }

    .control-group {
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on small screens */
        width: 100%; /* Span full width */
    }

    .control-group label {
        min-width: 150px; /* Align labels better */
        font-weight: bold;
        margin-left: 15px; /* Space between label and input */
        text-align: right;
    }

    .control-group.pulse-type-group label {
        min-width: auto; /* Don't constrain radio labels */
        margin-left: 8px;
        margin-right: 15px; /* Space after radio group label */
    }
     .control-group input[type="radio"] {
        margin-left: 5px; /* Space after radio button */
     }
     .control-group label[for="pulse-set"] {
         margin-right: 20px; /* Space between radio options */
     }


    .control-group input[type="range"] {
        flex-grow: 1;
        margin-right: 10px;
        min-width: 100px; /* Prevent slider from collapsing too much */
    }

    .control-group span {
        min-width: 25px; /* Keep space for value */
        text-align: center;
        font-weight: bold;
        color: var(--primary-color);
    }
    .slider-hint {
        width: 100%;
        text-align: center;
        font-size: 0.8em;
        color: #777;
        margin-top: 5px;
    }


    button {
        display: block;
        width: 100%;
        padding: 12px; /* Taller button */
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 15px;
        box-shadow: var(--shadow);
    }

     button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-1px);
     }
    button:active:not(:disabled) {
        background-color: #004085;
         transform: translateY(0);
    }
    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
    }

     .explanation-toggle-button {
        margin-top: 20px;
        background-color: var(--secondary-color);
     }
     .explanation-toggle-button:hover:not(:disabled) {
         background-color: #545b62;
     }
      .explanation-toggle-button:active:not(:disabled) {
         background-color: #3d4043;
     }


     /* Animation Layers */
     .animation-layer {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         border-radius: 15px; /* Match cell */
         opacity: 0;
         pointer-events: none;
     }

    .animation-layer.heat {
        background: radial-gradient(circle at center, rgba(255, 165, 0, 0.6) 0%, rgba(255, 0, 0, 0.6) 50%, transparent 80%); /* Fiery heat */
        transform: scale(0.1); /* Start small */
    }

     .animation-layer.cool {
         background: radial-gradient(circle at center, rgba(0, 191, 255, 0.5) 0%, rgba(70, 130, 180, 0.5) 50%, transparent 80%); /* Cool blue */
         transform: scale(0.1); /* Start small */
     }


    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: #ffffff;
        box-shadow: var(--shadow);
    }

    #explanation h2 {
        margin-top: 0;
        border-bottom: 1px solid #ddd;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    #explanation h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: var(--primary-color);
    }

    #explanation p {
        margin-bottom: 15px;
        text-align: justify; /* Justify text for better look */
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px;
        margin-bottom: 15px;
    }

    #explanation li {
        margin-bottom: 8px;
        line-height: 1.5;
    }

     /* Responsive adjustments */
    @media (max-width: 768px) {
         #pcm-simulation.simulation-container {
             grid-template-columns: 1fr; /* Stack columns */
         }

         .control-group {
             flex-direction: column;
             align-items: flex-end; /* Keep right alignment */
         }
         .control-group label {
             min-width: auto; /* Remove min-width on small screens */
             margin-left: 0;
             margin-bottom: 5px; /* Space below label */
         }
         .control-group input[type="range"] {
             width: 100%; /* Slider takes full width */
              margin-right: 0;
         }
         .control-group span {
              width: 100%; /* Value takes full width */
              text-align: left; /* Align value to left below slider */
              margin-top: 5px;
         }
         .control-group.pulse-type-group {
             flex-direction: row; /* Keep radios in a row if space allows */
             flex-wrap: wrap;
             justify-content: flex-end;
         }
          .control-group.pulse-type-group label {
             margin-bottom: 0;
          }
          .control-group label[for="pulse-set"] {
            margin-right: 10px; /* Reduce space */
          }
          .slider-hint {
            text-align: right;
          }
     }


</style>

<script>
    const pcmCell = document.getElementById('pcm-cell');
    const cellInner = pcmCell.querySelector('.cell-inner'); // Get the inner div for pattern transition
    const resistanceBar = document.getElementById('resistance-bar');
    const logicalValue = document.getElementById('logical-value');
    const phaseState = document.getElementById('phase-state');
    const pulseResetRadio = document.getElementById('pulse-reset');
    const pulseSetRadio = document.getElementById('pulse-set');
    const pulseIntensitySlider = document.getElementById('pulse-intensity');
    const intensityValueSpan = document.getElementById('intensity-value');
    const pulseDurationSlider = document.getElementById('pulse-duration');
    const durationValueSpan = document.getElementById('duration-value');
    const applyPulseButton = document.getElementById('apply-pulse');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const statusMessage = document.getElementById('status-message');

    const heatLayer = pcmCell.querySelector('.animation-layer.heat');
    const coolLayer = pcmCell.querySelector('.animation-layer.cool');


    // Initial state (Amorphous, High Resistance, 0)
    let currentState = 'amorphous'; // 'amorphous' or 'crystalline'
    let isAnimating = false; // Flag to prevent multiple clicks


    function updateUI() {
        if (currentState === 'amorphous') {
            pcmCell.classList.remove('crystalline');
            pcmCell.classList.add('amorphous');
            // Animate resistance bar width change
            resistanceBar.style.width = '90%'; // High resistance visual
            resistanceBar.classList.remove('low');
            resistanceBar.classList.add('high');
            logicalValue.classList.remove('value-1');
            logicalValue.classList.add('value-0');
            logicalValue.textContent = '0';
            phaseState.textContent = 'אמורפי';
             // Trigger pattern change animation on the inner div
             cellInner.style.backgroundImage = 'var(--amorphous-pattern)';

        } else { // crystalline
            pcmCell.classList.remove('amorphous');
            pcmCell.classList.add('crystalline');
             // Animate resistance bar width change
            resistanceBar.style.width = '10%'; // Low resistance visual
            resistanceBar.classList.remove('high');
            resistanceBar.classList.add('low');
             logicalValue.classList.remove('value-0');
            logicalValue.classList.add('value-1');
            logicalValue.textContent = '1';
            phaseState.textContent = 'גבישי';
             // Trigger pattern change animation on the inner div
             cellInner.style.backgroundImage = 'var(--crystalline-pattern)';
        }
    }

     function animatePulse(intensity, duration, newPhase) {
        isAnimating = true;
        applyPulseButton.disabled = true;
        statusMessage.textContent = 'מחמם...';

        // Scale intensity (1-10) to opacity/scale for heat animation
        const heatOpacity = intensity * 0.08; // Max 0.8 opacity
        const heatScale = 0.8 + intensity * 0.04; // Max scale 1.2
        const heatDuration = 200 + duration * 40; // Base 200ms + up to 400ms based on pulse duration

        // Heat Animation
        heatLayer.style.transition = `opacity ${heatDuration * 0.6}ms ease-out, transform ${heatDuration * 0.6}ms ease-out`;
        heatLayer.style.opacity = heatOpacity;
        heatLayer.style.transform = `scale(${heatScale})`;


        setTimeout(() => {
            statusMessage.textContent = 'מתקרר...';

            // Start Cooling Animation (fade heat, show cool)
            heatLayer.style.transition = `opacity ${heatDuration * 0.4}ms ease-in, transform ${heatDuration * 0.4}ms ease-in`; // Fade out faster
            heatLayer.style.opacity = 0;
            heatLayer.style.transform = `scale(0.1)`; // Shrink heat effect

            const coolDuration = 400 + (10 - duration) * 50; // Longer pulse = slower cool animation fade
             coolLayer.style.transition = `opacity ${coolDuration}ms ease-out, transform ${coolDuration}ms ease-out`;
             coolLayer.style.opacity = 0.5; // Max cool opacity
             coolLayer.style.transform = `scale(${heatScale})`; // Cool starts where heat was


            setTimeout(() => {
                 statusMessage.textContent = 'משנה מצב צבירה...';
                 currentState = newPhase; // Update state
                 updateUI(); // Trigger UI update and phase change animation

                 // Fade out cool animation
                 coolLayer.style.transition = `opacity 500ms ease-in, transform 500ms ease-in`;
                 coolLayer.style.opacity = 0;
                 coolLayer.style.transform = `scale(0.1)`;

                 setTimeout(() => {
                     // Reset transitions for next pulse
                     heatLayer.style.transition = 'none';
                     coolLayer.style.transition = 'none';
                     heatLayer.style.transform = 'scale(0.1)';
                     coolLayer.style.transform = 'scale(0.1)';
                     isAnimating = false;
                     applyPulseButton.disabled = false;
                     statusMessage.textContent = 'מוכן';
                 }, 500); // Wait for cool fade out

            }, heatDuration); // End of heat phase

        }, 50); // Small delay before starting heat animation
    }


    function applyPulse() {
        if (isAnimating) return; // Prevent multiple clicks

        const pulseType = document.querySelector('input[name="pulse-type"]:checked').value;
        const intensity = parseInt(pulseIntensitySlider.value);
        const duration = parseInt(pulseDurationSlider.value);

        // --- Refined Pulse Logic ---
        // Map Intensity (1-10) to a Heat Proxy (1-100)
        const heatProxy = intensity * 10;
        // Map Duration (1-10) to a Cool Rate Proxy (10=Fast Cool, 1=Slow Cool)
        const coolRateProxy = 11 - duration; // 10 duration -> 1 cool rate (slow), 1 duration -> 10 cool rate (fast)

        let newPhase = currentState; // Assume no change initially

        // Logic based on simulating melting/crystallization temperatures and cooling rates
        if (heatProxy < 30) {
            // Too low heat, material doesn't change phase easily, stays amorphous (if already amorphous) or crystalline (if already crystalline)
            // Simplified: Stays currentState
             newPhase = currentState;
             statusMessage.textContent = "פולס חלש מדי לשינוי משמעותי"; // Add specific feedback
        } else if (heatProxy >= 70) {
            // High Heat: Material melts completely
            if (coolRateProxy >= 6) { // Fast Cool Rate
                 // Melts then cools very fast -> freezes into Amorphous state
                 newPhase = 'amorphous';
                 statusMessage.textContent = "פולס חזק וקצר גרם להתכה וקירור מהיר (Reset)";
            } else { // Slow Cool Rate
                 // Melts then cools slowly -> atoms have time to rearrange into Crystalline state (like annealing)
                 newPhase = 'crystalline';
                 statusMessage.textContent = "פולס חזק וארוך גרם להתכה וקירור איטי (כמו חישול)";
            }
        } else { // heatProxy >= 30 && heatProxy < 70
            // Medium Heat: Material reaches crystallization temperature but doesn't melt
             if (coolRateProxy < 6) { // Slow Cool Rate
                 // Reaches crystallization temp and stays there long enough -> Crystallizes
                 newPhase = 'crystalline';
                  statusMessage.textContent = "פולס מתון וארוך איפשר התגבשות (Set)";
            } else { // Fast Cool Rate
                 // Reaches crystallization temp but cools too fast -> stays Amorphous
                 newPhase = 'amorphous';
                  statusMessage.textContent = "פולס מתון וקצר מדי לא איפשר התגבשות";
            }
        }

         // Override logic based on desired pulse type? Or let physics dictate?
         // Let's let physics dictate, but maybe add a message if physics doesn't match intent.
         let pulseOutcomeMessage = statusMessage.textContent; // Capture the physics outcome message

         // Animation starts regardless of phase change outcome
         animatePulse(intensity, duration, newPhase);

         // Add feedback if desired type didn't match outcome
         setTimeout(() => { // Wait until animation finishes to show final status message
             if (!isAnimating) { // Check if animation is truly done
                 const finalLogicalValue = (newPhase === 'amorphous' ? '0' : '1');
                 if (pulseType === 'reset' && finalLogicalValue !== '0') {
                      statusMessage.textContent = pulseOutcomeMessage + ". אזהרה: הפולס לא יצר את ה-'0' המצופה לפעולת Reset.";
                 } else if (pulseType === 'set' && finalLogicalValue !== '1') {
                     statusMessage.textContent = pulseOutcomeMessage + ". אזהרה: הפולס לא יצר את ה-'1' המצופה לפעולת Set.";
                 } else {
                     statusMessage.textContent = pulseOutcomeMessage; // Show the successful physics message
                 }
                  if(statusMessage.textContent === "מוכן") statusMessage.textContent = "מוכן. הפולס לא גרם לשינוי מצב צבירה משמעותי."
             }
         }, 200 + heatDuration + coolDuration + 500 + 100); // Wait total animation time + a little buffer for final message

    }

    // Update slider value displays
    pulseIntensitySlider.oninput = function() {
        intensityValueSpan.textContent = this.value;
    }
    pulseDurationSlider.oninput = function() {
        durationValueSpan.textContent = this.value;
    }

    // Event listener for the button
    applyPulseButton.addEventListener('click', applyPulse);

    // Event listener for explanation toggle
    toggleExplanationButton.addEventListener('click', function() {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מעמיק';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג/הסתר הסבר מעמיק';
        }
    });


    // Initial UI setup - use setTimeout to ensure CSS variables are potentially loaded
     setTimeout(updateUI, 0);

</script>
```