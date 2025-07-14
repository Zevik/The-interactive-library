---
title: "למה אף אחד לא עוזר במצוקה? סימולציה של אפקט העומד מן הצד"
english_slug: why-nobody-helps-bystander-effect-simulation
category: "מדעי החברה / פסיכולוגיה"
tags:
  - אפקט העומד מן הצד
  - פיזור אחריות
  - פסיכולוגיה חברתית
  - עזרה לזולת
  - התנהגות אזרחית
---

# למה אף אחד לא עוזר במצוקה? סימולציה של אפקט העומד מן הצד

דמיינו סצנת חירום ברחוב הומה אדם: מישהו מתמוטט על המדרכה, זקוק לעזרה דחופה. האם תרוצו לעזור? ומה יקרה כשיש עשרות אנשים מסביב, כולם עומדים ומסתכלים? הסימולטור הזה יעזור לכם להבין למה דווקא כשיש יותר אנשים – פחות סביר שתקבלו עזרה.

<div id="simulation-container" class="app-container">
    <div class="app-header">
        <h2>סימולטור אפקט העומד מן הצד</h2>
    </div>

    <div class="controls interactive-panel">
        <label for="bystanders">כמה עומדים מהצד נוכחים?</label>
        <div class="slider-control">
            <input type="range" id="bystanders" min="0" max="30" value="5" step="1">
            <span id="bystanders-count" class="count-display">5</span>
            <span class="range-labels">
                <span>מעט (0)</span>
                <span>הרבה (30)</span>
            </span>
        </div>
    </div>

     <div class="scene-area">
         <div class="victim">😞</div>
         <div id="bystanders-visual" class="bystanders-container">
             <!-- Bystander icons will be added here by JS -->
         </div>
          <div class="scene-labels">
            <p>אדם במצוקה</p>
            <p>...ושאר האנשים בסביבה</p>
        </div>
     </div>

    <div class="results-area interactive-panel">
        <h3>ההשפעה על הסיכוי לעזרה:</h3>
        <div class="result-item">
            <span class="result-label">תחושת אחריות אישית לעזור (של כל אדם):</span>
            <div class="gauge-container">
                 <div id="responsibility-gauge" class="gauge-bar"></div>
            </div>
             <span id="responsibility-value" class="value-text">גבוהה</span>
        </div>
        <div class="result-item">
            <span class="result-label">הסיכוי שאדם ספציפי *כלשהו* יעזור:</span>
            <div class="gauge-container">
                 <div id="specific-chance-gauge" class="gauge-bar"></div>
            </div>
             <span id="specific-chance-value" class="value-text">50%</span>
        </div>
        <div class="result-item">
            <span class="result-label">הסיכוי שלפחות אדם *אחד* יעזור (סה"כ הסיכוי לקבלת עזרה):</span>
            <div class="gauge-container">
                 <div id="overall-chance-gauge" class="gauge-bar"></div>
            </div>
             <span id="overall-chance-value" class="value-text">80%</span>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג/הסתר הסבר מעמיק</button>

<div id="explanation" class="explanation-container" style="display: none;">
    <h2>אפקט העומד מן הצד: הסבר מעמיק</h2>

    <p>כפי שראיתם בסימולציה, מספר האנשים הנוכחים במצב חירום משפיע באופן משמעותי על ההתנהגות שלנו ושל אחרים. תופעה זו נקראת 'אפקט העומד מן הצד'.</p>

    <h3>מהו אפקט העומד מן הצד?</h3>
    <p>אפקט העומד מן הצד (Bystander Effect) הוא תופעה בפסיכולוגיה חברתית שבה הסיכוי שאדם יגיש עזרה לקורבן יורד כאשר עדים נוספים נוכחים באירוע. ככל שיש יותר עדים, כך פוחת הסיכוי שאדם ספציפי יתערב ויסייע.</p>

    <h3>מאיפה הכל התחיל?</h3>
    <p>ההשראה למחקר פורץ הדרך על אפקט העומד מן הצד הגיעה מאירוע טרגי שהתרחש בשנת 1964 בניו יורק. קיטי ג'נובזה, צעירה, נרצחה מחוץ לבניין דירתה לעיני עשרות שכנים, אשר לפי הדיווחים, שמעו את זעקותיה אך לא התקשרו למשטרה או התערבו באופן פעיל. סיפור זה, למרות שפרטים מסוימים בו היו שנויים במחלוקת בדיעבד, עורר גל של שאלות מחקריות על הסיבות שבני אדם נמנעים מלעזור במצבי חירום כשיש עדים רבים.</p>

    <h3>הניסויים הקלאסיים של לאטאנה ודארלי</h3>
    <p>בעקבות מקרה קיטי ג'נובזה, הפסיכולוגים החברתיים בִּיבּ לַאטַאנֶה (Bibb Latané) וג'וֹן דַארְלִי (John Darley) ערכו סדרה של ניסויים פורצי דרך כדי לבחון אמפירית את התופעה. באחד הניסויים המפורסמים ביותר, נבדקים חשבו שהם משתתפים בדיון קבוצתי באמצעות אינטרקום, כאשר למעשה היו מבודדים. אחד ה"משתתפים" (שהיה למעשה שחקן) זייף התקף אפילפטי. התוצאות הראו באופן מובהק שככל שמספר ה"משתתפים" (העדים) בשיחה עלה, כך ירד הסיכוי שהנבדק הבודד ידווח על מקרה החירום, ולקח לו יותר זמן לעשות זאת אם כבר עשה זאת. ניסויים נוספים, כמו ניסוי "חדר העשן", הראו תוצאות דומות.</p>

    <h3>למה זה קורה? הגורמים הפסיכולוגיים המרכזיים</h3>
    <p>לאטאנה ודארלי הציעו מספר מנגנונים פסיכולוגיים שמסבירים את אפקט העומד מן הצד:</p>
    <ul>
        <li><strong>פיזור אחריות (Diffusion of Responsibility):</strong> בנוכחות עדים רבים, האחריות לעזור מתפזרת בין כולם. אדם בודד מרגיש פחות אחריות אישית לפעול, ומניח (או מקווה) שמישהו אחר ייקח על עצמו את המשימה. ככל שיש יותר אנשים, תחושת האחריות האישית של כל אחד נחלשת.</li>
        <li><strong>בורות פלורליסטית (Pluralistic Ignorance):</strong> במצב חירום עמום, אנשים מסתכלים על תגובותיהם של אחרים כדי להבין מה קורה והאם נדרשת עזרה. אם כולם נראים רגועים ולא מגיבים (אולי מתוך הסתכלות על האחרים), כל אחד יכול לטעות ולפרש את המצב כפחות חמור מכפי שהוא באמת, או להסיק שהתגובה המתאימה היא אי-תגובה. כל אחד חושב "אף אחד אחר לא נראה מודאג, אז כנראה שהכל בסדר", למרות שבלב כולם חשים אי-נוחות.</li>
        <li><strong>חשש מהערכה (Evaluation Apprehension):</strong> אנשים חוששים להיראות טיפשים, להתבייש, או לפעול בצורה שגויה בפומבי. הם חוששים שאם יתערבו, ייתכן שהם מפרשים את המצב באופן שגוי, יחמירו את המצב, או שפשוט לא יידעו מה לעשות ויתפסו כלא כשירים. החשש משיפוט שלילי על ידי העדים האחרים יכול לעכב את הפעולה.</li>
    </ul>

    <h3>כיצד ניתן להתגבר על אפקט העומד מן הצד? אסטרטגיות לעזרה במצבי חירום</h3>
    <p>למרות שהאפקט חזק, ניתן ואף חיוני להתגבר עליו. אם אתם עדים למצב חירום, הנה כמה דרכים להגדיל את הסיכוי לעזרה:</p>
    <ul>
        <li>**קחו אחריות אישית:** זכרו שהנטייה היא לפזר אחריות. מודעות לכך היא הצעד הראשון. החליטו שאתם לוקחים אחריות לפעול.</li>
        <li>**הסירו את העמימות:** אם המצב אינו ברור, אל תניחו שהכל בסדר רק כי אחרים לא מגיבים. גשו לבדוק, שאלו "הכל בסדר?" או "האם אתה צריך עזרה?".</li>
        <li>**התגברו על חשש מהערכה:** במצב חירום, עזרה כלשהי, גם אם אינה מושלמת, טובה יותר מאי-עזרה בכלל. זכרו שהמטרה היא להציל חיים או למנוע פגיעה, לא להיראות מושלמים.</li>
        <li>**הגדירו את האחריות:** אם ישנם עדים נוספים, פנו לאדם ספציפי והטילו עליו משימה ברורה. לדוגמה: "אתה, בחולצה האדומה! התקשר למד"א!" או "את, עם התיק הכחול! הישארי כאן עם האדם עד שתגיע עזרה!". הגדרה ספציפית של תפקידים מפחיתה את פיזור האחריות ואת בורות הפלורליסטית.</li>
        <li>**התחילו לעזור בעצמכם:** לעיתים קרובות, פעולה ראשונית של אדם אחד יכולה לשבור את מעגל אי-הפעולה ולעודד אחרים להצטרף.</li>
    </ul>

    <h3>מתי ואיפה האפקט פחות בא לידי ביטוי?</h3>
    <p>אפקט העומד מן הצד אינו בלתי נמנע ותמיד מתרחש. ישנם מצבים שבהם הסבירות לעזרה גבוהה יותר, גם בנוכחות עדים:</p>
    <ul>
        <li>**כאשר המצב ברור ואינו עמום:** אם ברור לחלוטין שמדובר במצב חירום ונדרשת עזרה, הסבירות לבורות פלורליסטית יורדת משמעותית.</li>
        <li>**בסביבה מוכרת או בין אנשים שמכירים זה את זה:** בקבוצה חברתית קטנה, בין חברים, שכנים או עמיתים לעבודה, תחושת האחריות ההדדית חזקה יותר, ופיזור האחריות פחות משפיע.</li>
        <li>**כאשר לעד יש הכשרה או ידע רלוונטי:** אדם עם הכשרה רפואית או עזרה ראשונה יחוש פחות בלבול וחשש מהערכה, ויטה יותר להתערב.</li>
        <li>**כאשר יש קשר כלשהו לקורבן:** אפילו קשר קלוש (למשל, אם הקורבן נראה כמו מישהו שמכירים) יכול להגביר את הסיכוי לעזרה.</li>
    </ul>
    <p>לסיכום, אפקט העומד מן הצד הוא תופעה מורכבת המושפעת מגורמים פסיכולוגיים וחברתיים. מודעות אליו והבנת מנגנוניו יכולה לסייע לנו להתגבר על הנטייה הטבעית לאי-פעולה ולהפוך לעדים אקטיביים ומועילים יותר בשעת צורך.</p>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #28a745; /* Green */
        --warning-color: #ffc107; /* Amber */
        --danger-color: #dc3545; /* Red */
        --light-bg: #f8f9fa; /* Light gray */
        --dark-text: #343a40; /* Dark gray */
        --border-color: #dee2e6; /* Light gray border */
        --card-bg: #ffffff; /* White */
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --border-radius: 8px;
        --gauge-bg: #e9ecef;
    }

    #simulation-container.app-container {
        direction: rtl;
        font-family: 'Heebo', sans-serif; /* Use a more modern font */
        background: var(--light-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        padding: 25px;
        margin: 20px auto;
        max-width: 650px; /* Increased max width */
        color: var(--dark-text);
        border: 1px solid var(--border-color);
        overflow: hidden; /* Clear floats/flex issues */
    }

    .app-header {
        text-align: center;
        margin-bottom: 25px;
    }

    .app-header h2 {
        color: var(--primary-color);
        margin: 0;
        font-size: 1.8em;
        font-weight: 600;
    }

    .interactive-panel {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: var(--shadow);
        border: 1px solid var(--border-color);
    }

    .controls {
         text-align: center; /* Center controls */
    }

    .controls label {
        font-size: 1.1em;
        margin-bottom: 15px; /* More space below label */
        display: block; /* Label on its own line */
        font-weight: 500;
        color: var(--dark-text);
    }

     .slider-control {
         display: flex;
         flex-direction: column;
         align-items: center;
         width: 100%; /* Use full width of panel */
     }

    .controls input[type="range"] {
        width: 90%; /* Slider width within its container */
        height: 8px; /* Thicker slider bar */
        background: var(--gauge-bg);
        border-radius: 5px;
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        cursor: pointer;
        margin: 10px 0; /* Vertical margin */
         direction: ltr; /* Keep slider direction left-to-right */
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* Thumb size */
        height: 20px;
        background: var(--primary-color);
        border-radius: 50%;
        cursor: pointer;
        border: 2px solid var(--card-bg); /* White border around thumb */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: background 0.3s ease;
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        border-radius: 50%;
        cursor: pointer;
         border: 2px solid var(--card-bg);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
         transition: background 0.3s ease;
    }

     .controls input[type="range"]:hover::-webkit-slider-thumb {
         background: var(--secondary-color);
     }
     .controls input[type="range"]:hover::-moz-range-thumb {
         background: var(--secondary-color);
     }


    .count-display {
        font-size: 1.2em;
        font-weight: bold;
        color: var(--primary-color);
        margin-top: 10px;
    }

     .range-labels {
         width: 90%;
         display: flex;
         justify-content: space-between;
         font-size: 0.8em;
         color: #6c757d;
     }


    .scene-area {
        text-align: center;
        margin-bottom: 25px;
        padding: 20px;
        background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* Subtle gradient background */
        border-radius: var(--border-radius);
        border: 1px dashed #00bcd4; /* Cyan dashed border */
        position: relative; /* For positioning labels */
        min-height: 150px; /* Ensure enough space */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden; /* Prevent bystander icons from overflowing */
    }

    .victim {
        font-size: 3em; /* Larger emoji/icon */
        margin-bottom: 15px;
        animation: pulse 2s infinite ease-in-out; /* Subtle animation for victim */
        display: inline-block; /* Allow animation */
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }


    .bystanders-container {
        display: flex;
        flex-wrap: wrap; /* Allow icons to wrap to next line */
        justify-content: center;
        gap: 8px; /* Space between icons */
        margin-top: 10px;
        max-width: 100%; /* Don't exceed container width */
    }

    .bystander-icon {
        width: 15px; /* Size of each icon */
        height: 15px;
        background-color: #6c757d; /* Gray color for bystanders */
        border-radius: 50%; /* Make them circles */
        opacity: 0.8;
        transition: opacity 0.3s ease;
    }
     /* Optional: Add a class to slightly highlight when the number changes */
     .bystander-icon.new {
         animation: fadeInScale 0.5s ease-out;
     }

     @keyframes fadeInScale {
         0% { opacity: 0; transform: scale(0.5); }
         100% { opacity: 0.8; transform: scale(1); }
     }


    .scene-labels {
        margin-top: 15px;
        font-size: 0.9em;
        color: var(--dark-text);
        opacity: 0.8;
    }

     .scene-labels p {
         margin: 3px 0;
     }


    .results-area h3 {
        text-align: center;
        color: var(--dark-text);
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.4em;
        font-weight: 600;
    }

    .result-item {
        margin-bottom: 20px;
        display: flex; /* Use flexbox for layout */
        flex-direction: column; /* Stack label, gauge, value */
        align-items: flex-start; /* Align content to the right (RTL) */
    }

     .result-label {
         font-weight: 500;
         margin-bottom: 8px; /* Space below label */
         color: var(--dark-text);
         font-size: 1em;
     }

     .value-text {
         font-weight: bold;
         font-size: 1.1em;
         color: var(--primary-color); /* Default color */
         margin-top: 5px; /* Space above value */
     }

     /* Color coding for value text */
     .value-text.high { color: var(--secondary-color); } /* Green */
     .value-text.medium { color: var(--warning-color); } /* Amber */
     .value-text.low { color: var(--danger-color); } /* Red */


    .gauge-container {
        width: 100%;
        height: 25px; /* Taller gauge */
        background-color: var(--gauge-bg);
        border-radius: 12.5px; /* Rounded ends */
        overflow: hidden;
        margin-top: 5px;
        border: 1px solid var(--border-color);
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); /* Inner shadow for depth */
    }

    .gauge-bar {
        height: 100%;
        width: 0%; /* Start at 0 and transition */
        transition: width 0.5s ease-in-out; /* Smooth transition for width changes */
        background: linear-gradient(to right, #a8dadc, #457b9d); /* Subtle gradient for bars */
    }

    /* Specific gauge colors - using different gradients or solid fills */
    #responsibility-gauge { background: linear-gradient(to right, #ffecb3, #ffc107); } /* Amber gradient */
    #specific-chance-gauge { background: linear-gradient(to right, #bbdefb, #2196F3); } /* Blue gradient */
    #overall-chance-gauge { background: linear-gradient(to right, #c8e6c9, #4CAF50); } /* Green gradient */


    /* Toggle Button Styling */
    .toggle-button {
        display: block;
        margin: 25px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: var(--primary-color);
        color: var(--card-bg);
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 500;
        box-shadow: var(--shadow);
    }

    .toggle-button:hover {
        background-color: #0056b3; /* Darker blue */
    }

    .toggle-button:active {
        transform: scale(0.98); /* Slightly shrink on click */
    }


    /* Explanation Styling */
    .explanation-container {
        direction: rtl;
        font-family: 'Heebo', sans-serif;
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        padding: 25px;
        margin: 20px auto;
        max-width: 650px;
        color: var(--dark-text);
        border: 1px solid var(--border-color);
        line-height: 1.7; /* Improved readability */
    }

    .explanation-container h2 {
        color: var(--primary-color);
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.6em;
        font-weight: 600;
        text-align: center;
    }

    .explanation-container h3 {
        color: var(--dark-text);
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.3em;
        font-weight: 600;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 5px;
    }

    .explanation-container p {
        margin-bottom: 15px;
    }

    .explanation-container ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list items */
    }

    .explanation-container li {
        margin-bottom: 10px;
    }


    /* Responsive Adjustments (Basic) */
    @media (max-width: 700px) {
        #simulation-container.app-container,
        .explanation-container {
            padding: 15px;
            margin: 15px auto;
        }
         .app-header h2 {
             font-size: 1.5em;
         }
        .controls input[type="range"] {
            width: 95%;
        }
        .scene-area {
            padding: 15px;
        }
         .victim {
             font-size: 2.5em;
         }
         .bystander-icon {
             width: 12px;
             height: 12px;
         }
         .result-label {
             font-size: 0.95em;
         }
         .value-text {
             font-size: 1em;
         }
         .toggle-button {
             font-size: 1em;
             padding: 10px 20px;
         }
         .explanation-container h2 {
             font-size: 1.4em;
         }
          .explanation-container h3 {
             font-size: 1.2em;
         }
    }


</style>

<script>
    const bystandersInput = document.getElementById('bystanders');
    const bystandersCountSpan = document.getElementById('bystanders-count');
    const responsibilityGauge = document.getElementById('responsibility-gauge');
    const responsibilityValueSpan = document.getElementById('responsibility-value');
    const specificChanceGauge = document.getElementById('specific-chance-gauge');
    const specificChanceValueSpan = document.getElementById('specific-chance-value');
    const overallChanceGauge = document.getElementById('overall-chance-gauge');
    const overallChanceValueSpan = document.getElementById('overall-chance-value');
    const bystandersVisualContainer = document.getElementById('bystanders-visual'); // New: Container for visual bystanders
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Function to update bystander icons
    function updateBystanderVisual(count) {
        // Clear existing icons
        bystandersVisualContainer.innerHTML = '';
        // Add new icons based on the count
        for (let i = 0; i < count; i++) {
            const icon = document.createElement('div');
            icon.classList.add('bystander-icon');
            // Optional: Add a class for initial animation if desired (more complex)
            // icon.classList.add('new'); // Requires more logic to manage 'new' class
            bystandersVisualContainer.appendChild(icon);
        }
         // Simple approach: Add all at once. For animations, would need to track changes.
         // Let's keep it simple with static visual representation.
    }


    function updateSimulation() {
        const numBystanders = parseInt(bystandersInput.value, 10);
        bystandersCountSpan.textContent = numBystanders;

        // Update scene display (visual icons instead of text)
        updateBystanderVisual(numBystanders);


        // Calculate values (simplified psychological model for visualization)
        // Total potential helpers = user (1) + bystanders
        const totalPotentialHelpers = numBystanders + 1; // User is implicitly one potential helper

        // Responsibility: Decreases significantly with more people. Non-linear.
        // Scale 0-100. With 0 bystanders (only user), responsibility is high (e.g., 95%).
        // With 30, it's very low (e.g., 5%).
        // Formula: MaxResponsibility / (TotalPotentialHelpers ^ factor)
        const maxResponsibility = 100; // Start higher
        const responsibility = Math.max(5, maxResponsibility / Math.pow(totalPotentialHelpers, 0.9)); // Use power for non-linearity, slightly steeper curve

        // Specific Chance: Probability for one *random* person decreases.
        // Simple inverse relationship scaled. With 0 bystanders (total 1 potential helper including user), let's say 70% (you are likely to help).
        // With 30 (total 31 potential helpers), much lower.
        // Formula: BaseChance / TotalPotentialHelpers
        const baseChanceSpecific = 70; // Hypothetical chance *for one person* if *they were the only one* besides the victim
        // When part of a crowd, individual chance drops due to psychological factors. Let's model this reduced individual chance.
        const individualChanceInCrowd = baseChanceSpecific / Math.pow(totalPotentialHelpers, 1.2); // Individual chance reduced further in a crowd
         const specificChance = Math.max(3, individualChanceInCrowd); // Ensure minimum


        // Overall Chance: Chance at least one person helps.
        // This is 1 - (Probability nobody helps).
        // Probability nobody helps = (Probability a specific person *in the crowd* doesn't help)^N_total
        // Let's use the calculated 'individualChanceInCrowd' for each person's probability of NOT helping.
        // Prob_not_help_individual = (100 - specificChance) / 100; // Using the calculated specificChance (which is % chance someone *specific* helps)
        // Let's rethink the model slightly to align better with the explanation points (Diffusion, Pluralistic Ignorance).
        // Assume a base individual probability 'p' if *alone*. In a crowd, this 'p' is reduced.
        // Let p_alone = 0.8 (80% chance you help if alone).
        // In a crowd, each individual's chance becomes p_crowd = p_alone * (1 / N_total^k).
        // Prob. nobody helps = (1 - p_crowd)^N_total
        // This is mathematically complex and doesn't directly give the "specific person's chance" displayed.
        // Let's stick to the simpler model that *visually* reflects the concepts.

        // Revised Simple Model:
        // 1. Responsibility: Drops sharply with N.
        // 2. Specific Person's Chance: Drops sharply with N (due to diffusion, fear of evaluation).
        // 3. Overall Chance: Rises initially as more people *could* help, but then plateaus or slightly drops due to factors like pluralistic ignorance and stronger diffusion in very large crowds.

        // Let's adjust the Overall Chance calculation to show this effect.
        // Prob. nobody helps = (1 - (effective_individual_chance / 100)) ^ TotalPotentialHelpers
        // The 'effective_individual_chance' is the specificChance we calculated.
        const effectiveIndividualChance = specificChance; // Using the calculated specific chance %
        const probSomeoneHelps = 1 - Math.pow(1 - (effectiveIndividualChance / 100), totalPotentialHelpers);
        let overallChance = probSomeoneHelps * 100;

        // Apply a factor for very large crowds to potentially show the plateau/slight dip effect
        if (numBystanders > 15) { // Effects of confusion/pluralistic ignorance amplified beyond 15
             const reductionFactor = 1 - ((numBystanders - 15) * 0.008); // Small reduction per bystander over 15
             overallChance = overallChance * reductionFactor;
        }

        overallChance = Math.max(10, overallChance); // Ensure minimum overall chance


        // Update gauge widths and text values
        responsibilityGauge.style.width = `${responsibility}%`;
        // Assign text label and color class based on percentage
        if (responsibility > 75) { responsibilityValueSpan.textContent = 'גבוהה מאד'; responsibilityValueSpan.className = 'value-text high'; }
        else if (responsibility > 50) { responsibilityValueSpan.textContent = 'גבוהה'; responsibilityValueSpan.className = 'value-text high'; }
        else if (responsibility > 30) { responsibilityValueSpan.textContent = 'בינונית'; responsibilityValueSpan.className = 'value-text medium'; }
        else if (responsibility > 15) { responsibilityValueSpan.textContent = 'נמוכה'; responsibilityValueSpan.className = 'value-text low'; }
        else { responsibilityValueSpan.textContent = 'נמוכה מאד'; responsibilityValueSpan.className = 'value-text low'; }


        specificChanceGauge.style.width = `${specificChance}%`;
         if (specificChance > 60) specificChanceValueSpan.className = 'value-text high';
         else if (specificChance > 30) specificChanceValueSpan.className = 'value-text medium';
         else specificChanceValueSpan.className = 'value-text low';
        specificChanceValueSpan.textContent = `${specificChance.toFixed(0)}%`;

        overallChanceGauge.style.width = `${overallChance}%`;
         if (overallChance > 80) overallChanceValueSpan.className = 'value-text high';
         else if (overallChance > 50) overallChanceValueSpan.className = 'value-text medium';
         else overallChanceValueSpan.className = 'value-text low';
        overallChanceValueSpan.textContent = `${overallChance.toFixed(0)}%`;
    }

    // Initial update
    updateSimulation();

    // Add event listener
    bystandersInput.addEventListener('input', updateSimulation);

     // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג/הסתר הסבר מעמיק';
         // Scroll to the explanation when shown
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

</script>
---