---
title: "הכור הגרעיני העתיק של אוקלו: פעימות הלב של כדור הארץ"
english_slug: the-ancient-nuclear-reactor-of-oklo-how-it-happened
category: "פיזיקה"
tags:
  - פיזיקה גרעינית
  - כור גרעיני
  - אוקלו
  - גאולוגיה
  - היסטוריה של כדור הארץ
  - ראקטיביות
---
# הכור הגרעיני העתיק של אוקלו: פעימות הלב הגרעיניות של כדור הארץ

דמיינו לב עצום פועם עמוק בתוך האדמה, פועל מעצמו, ללא מגע יד אדם, במשך מאות אלפי שנים. נשמע כמו אגדה קדומה או מדע בדיוני מתקדם? ובכן, זה קרה באמת. לפני כ-2 מיליארד שנים, באתר נידח בשם אוקלו (Oklo) במערב אפריקה (גבון של ימינו), התגלתה תופעה מדהימה: סדרה של כורים גרעיניים שפעלו באופן טבעי לחלוטין!

איך ייתכן שפיסת סלע בכדור הארץ החלה "להתנהג" כמו כור גרעיני מודרני, להגיע לקריטיות, לשמור עליה, ואף לווסת את עצמה במחזורים של פעילות ומנוחה? הצטרפו למסע לגילוי הסודות הגרעיניים הקדומים של כדור הארץ.

<div id="simulation-container" class="interactive-widget">
    <h2>סימולטור הכור הטבעי</h2>
    <p class="subtitle">כוונן את התנאים הקדומים וצפה כיצד תגובת השרשרת מתפתחת בזמן אמת.</p>
    <div class="controls">
        <div class="control-group">
            <label for="u235-concentration">ריכוז אורניום-235 (%):</label>
            <div class="slider-wrapper">
                <input type="range" id="u235-concentration" min="0.7" max="4" value="3.5" step="0.1">
                <span id="u235-value" class="slider-value">3.5%</span>
            </div>
             <p class="control-tip">דלק הכור. ככל שהריכוז גבוה יותר, כך קל יותר להגיע לקריטיות.</p>
        </div>
        <div class="control-group">
            <label for="moderator-amount">כמות מודרטור (מים) (%):</label>
             <div class="slider-wrapper">
                <input type="range" id="moderator-amount" min="0" max="40" value="15" step="1">
                <span id="moderator-value" class="slider-value">15%</span>
             </div>
             <p class="control-tip">מאט נייטרונים. חיוני לביקוע יעיל, אך יותר מדי או מעט מדי יפגע בתגובה.</p>
        </div>
        <div class="control-group">
            <label for="poison-amount">כמות בולעי נייטרונים (רעלנים):</label>
             <div class="slider-wrapper">
                <input type="range" id="poison-amount" min="0" max="10" value="2" step="0.5">
                <span id="poison-value" class="slider-value">2</span>
             </div>
             <p class="control-tip">בולעים נייטרונים ומעכבים את תגובת השרשרת.</p>
        </div>
    </div>

    <div class="simulation-area">
        <div class="status-indicator">
            <span id="simulation-status">ממתין...</span>
            <div id="pulsing-circle" class="pulsing-circle"></div>
        </div>
         <div class="chart-container">
            <canvas id="simulation-chart"></canvas>
         </div>
    </div>

    <button id="start-simulation-button">התחל סימולציה</button>
</div>

<button id="toggle-explanation-button" class="toggle-button">גלה את הסודות: הסבר מפורט</button>

<div id="explanation" class="explanation-section">
    <h2>ההסבר המלא: סודות הכור הגרעיני הטבעי</h2>

    <p>הגילוי באוקלו היה פורץ דרך. הוא הוכיח שתגובת שרשרת גרעינית אינה המצאה אנושית בלבד, אלא תופעה טבעית אפשרית בתנאים הנכונים. אלו התנאים שאפשרו זאת:</p>

    <h3>1. המרכיב החיוני: הדלק הנכון</h3>
    <p>האורניום בטבע מורכב בעיקר משני איזוטופים: אורניום-238 (U-238) ואורניום-235 (U-235). רק U-235 הוא "בקיע" בקלות על ידי נייטרונים איטיים, והוא למעשה הדלק לכורים גרעיניים מודרניים ולכור באוקלו. ל-U-235 יש זמן מחצית חיים קצר יותר משל U-238. המשמעות היא שלאורך ההיסטוריה של כדור הארץ, כמות ה-U-235 היחסית בכלל האורניום הטבעי ירדה בהדרגה. לפני כ-2 מיליארד שנים, כפי שהיה באוקלו, ריכוז ה-U-235 באורניום טבעי היה גבוה משמעותית – כ-3-4%! זהו טווח הריכוזים המשמש כיום בכורים מודרניים מסוימים (אורניום מועשר קלות). כיום, הריכוז הוא רק כ-0.7%, נמוך מכדי לקיים תגובת שרשרת בתנאים טבעיים.</p>

    <h3>2. שותף הכרחי: המודרטור</h3>
    <p>כאשר אטום U-235 מתבקע, הוא פולט נייטרונים מהירים מאוד. נייטרונים אלו לרוב "חולפים" ליד גרעיני U-235 אחרים מבלי לגרום ביקוע נוסף. כדי לקיים תגובת שרשרת יעילה, יש להאט את הנייטרונים הללו למהירות "תרמית" (מהירות אופיינית לתנועה תרמית בטמפרטורת הסביבה). חומר המבצע האטה זו נקרא מודרטור. באוקלו, המודרטור היה פשוט... מים תת-קרקעיים! מולקולות המים (בעיקר אטומי המימן שבהן) שימשו כמועכים אידיאליים להאטת הנייטרונים.</p>

    <h3>3. האויבים השקטים: בולעי הנייטרונים (רעלנים)</h3>
    <p>חומרים מסוימים, כמו יסודות נדירים כמו גדוליניום או קאדמיום, "בולעים" נייטרונים ביעילות מבלי שהם יגרמו לביקוע. חומרים אלו נקראים "רעלנים" גרעיניים מכיוון שהם יכולים לעצור או להאט תגובת שרשרת. המרבצים באוקלו היו נקיים יחסית מרעלנים כאלה, מה שאפשר לנייטרונים להמשיך ולהתקיים מספיק זמן כדי לגרום ביקועים נוספים.</p>

    <h3>4. "מסת האקראיות": הריכוז והצפיפות</h3>
    <p>כדי שתגובת שרשרת תתקיים, לא מספיק שיהיו דלק ומודרטור; הם צריכים להיות מרוכזים מספיק במקום אחד. כמות החומר הבקיע (בצפיפות מסוימת) הדרושה לקיום תגובת שרשרת נקראת "מסה קריטית". באוקלו, גאולוגיה ייחודית יצרה ריכוזים גבוהים במיוחד של אורניום באזורים מסוימים, ואפשרה למסה קריטית להתגבש כאשר המים חדרו למרבץ.</p>

    <h3>המנגנון הפועם: ויסות טבעי</h3>
    <p>התנאים המושלמים האלו לא הובילו לפעילות גרעינית רציפה ובלתי נשלטת. הכורים באוקלו פעלו במחזורים מרתקים, בדומה ל"פעימות לב" גרעיניות:</p>
    <ol>
        <li>**הפעלה:** כאשר המים חדרו למרבץ האורניום העשיר, הם שימשו כמודרטור יעיל והאיטו את הנייטרונים.</li>
        <li>**עלייה בקריטיות:** הנייטרונים האיטיים גרמו לביקוע מוגבר של U-235, מה שהוביל לעלייה מהירה בקצב תגובת השרשרת וליצירת חום רב.</li>
        <li>**"רתיחה" וכיבוי:** החום העצום גרם למים בתוך המרבץ לרתוח ולהפוך לאדים. אדי מים הם מודרטור גרוע בהרבה ממים נוזליים. עם ירידת יעילות המודרטור, קצב תגובת השרשרת ירד באופן דרמטי (הכור "נכבה" או עבר למצב תת-קריטי).</li>
        <li>**קירור והפעלה מחדש:** ללא תגובת השרשרת, המרבץ החל להתקרר. מים נוזליים חזרו לחדור אליו, החזירו את המודרטור, והתנאים לקריטיות שוב התאימו – המחזור החל מחדש.</li>
    </ol>
    <p>כל מחזור כזה נמשך כ-30 דקות לערך (כ-30 דקות פעילות, ואז כיבוי והתקררות). הכורים פעלו כך לסירוגין במשך מאות אלפי שנים!</p>

    <h3>מעבר להיסטוריה: למה זה חשוב לנו היום?</h3>
    <p>גילוי אוקלו אינו רק אנקדוטה גאולוגית מרתקת. הוא סיפק תובנות מדעיות יקרות ערך:</p>
    <ul>
        <li>**קבועים פיזיקליים ויציבות היקום:** ניתוח מדוקדק של איזוטופים שונים, כולל תוצרי ביקוע, שנמצאו באוקלו, הראה שהם תואמים באופן מפליא את החישובים התיאורטיים המבוססים על הקבועים הפיזיקליים הידועים לנו כיום. זהו אישוש מרשים לכך שקבועי טבע בסיסיים, כמו קבוע המבנה העדין הקובע את חוזק הכוח האלקטרומגנטי, לא השתנו באופן משמעותי ב-2 מיליארד השנים האחרונות – עדות ליציבות יסודית של חוקי הפיזיקה.</li>
        <li>**אחסון פסולת רדיואקטיבית:** אוקלו משמש כמעבדת טבע ענקית לבחינת התנהגות חומרים רדיואקטיביים לאורך זמן גאולוגי. התברר שרבים מתוצרי הביקוע המסוכנים, כמו פלוטוניום, נשארו לכודים בתוך מבנה המחצב עצמו ולא נדדו אל הסביבה באופן משמעותי, גם לאחר מיליארדי שנים. תובנה זו חיונית ביותר לתכנון ופיתוח אתרים לאחסון גאולוגי ארוך טווח של פסולת רדיואקטיבית מכורים גרעיניים מודרניים. אוקלו מוכיח שהרעיון של כליאה גאולוגית של חומרים מסוכנים הוא בר קיימא לאורך תקופות זמן ארוכות להפליא.</li>
    </ul>
</div>

<style>
    :root {
        --primary-color: #4a90e2; /* A nice blue */
        --secondary-color: #50e3c2; /* A teal/mint */
        --accent-color: #f5a623; /* An orange */
        --background-light: #f0f4f8; /* Light grey blue */
        --background-dark: #dbe2ef; /* Slightly darker grey blue */
        --text-color: #333;
        --heading-color: #2c3e50; /* Dark blue/grey */
        --border-color: #c4d3e3; /* Soft border color */
        --danger-color: #e74c3c; /* Red */
        --success-color: #2ecc71; /* Green */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: #fff; /* Ensure white background if placed directly */
    }

    h1, h2, h3 {
        color: var(--heading-color);
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
         font-size: 2em;
         border-bottom: none; /* Remove default H1 border */
    }

     h2 {
         font-size: 1.6em;
         margin-top: 25px;
         padding-bottom: 5px;
         border-bottom: 1px solid var(--border-color);
     }

    h3 {
        font-size: 1.3em;
        margin-top: 20px;
        padding-bottom: 3px;
        border-bottom: 1px dotted var(--border-color);
    }


    p {
        margin-bottom: 1em;
        text-align: justify;
    }

    p.subtitle {
        font-size: 1.1em;
        color: #555;
        margin-top: -10px;
        margin-bottom: 20px;
        text-align: center;
    }

    .interactive-widget {
        border: 1px solid var(--border-color);
        padding: 25px;
        margin: 30px auto;
        background-color: var(--background-light);
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        max-width: 800px; /* Limit width */
        box-sizing: border-box; /* Include padding and border in element's total width */
    }

    .controls {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px;
        margin-bottom: 30px;
    }

    .control-group {
        background-color: #fff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        display: flex;
        flex-direction: column;
    }

    .control-group label {
        margin-bottom: 10px;
        font-weight: bold;
        color: var(--heading-color);
        font-size: 1.05em;
    }

    .slider-wrapper {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .controls input[type="range"] {
        flex-grow: 1;
        -webkit-appearance: none;
        height: 8px;
        background: var(--background-dark);
        outline: none;
        opacity: 0.9;
        transition: opacity .2s, transform 0.1s ease-in-out;
        border-radius: 5px;
        cursor: pointer;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }
     .controls input[type="range"]:active {
        transform: scale(1.01); /* Subtle scale effect on click */
     }


    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 3px solid #fff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
         transition: background-color 0.2s ease;
    }
     .controls input[type="range"]::-webkit-slider-thumb:hover {
        background-color: #3a7bd5; /* Darker shade on hover */
     }


    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
         border: 3px solid #fff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
         transition: background-color 0.2s ease;
    }
     .controls input[type="range"]::-moz-range-thumb:hover {
        background-color: #3a7bd5; /* Darker shade on hover */
     }

    .slider-value {
        font-size: 1.1em;
        font-weight: bold;
        color: var(--primary-color);
        width: 55px; /* Fixed width to prevent layout shifts */
        text-align: center;
    }

    p.control-tip {
        font-size: 0.9em;
        color: #666;
        margin-top: 10px;
        margin-bottom: 0;
        text-align: right; /* Align tip to the right */
        font-style: italic;
    }

    .simulation-area {
        background-color: #fff;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        padding: 15px;
        position: relative; /* Needed for status indicator absolute positioning */
    }

    .status-indicator {
        text-align: center;
        margin-bottom: 10px;
        font-weight: bold;
        min-height: 1.2em; /* Reserve space */
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }

    #simulation-status {
        color: #666;
         transition: color 0.5s ease;
    }

    #simulation-status.status-ready { color: var(--primary-color); }
    #simulation-status.status-running { color: var(--success-color); }
    #simulation-status.status-critical { color: var(--accent-color); animation: pulse-text 1s infinite alternate; }
    #simulation-status.status-supercritical { color: var(--danger-color); animation: blink 0.5s infinite alternate; }
    #simulation-status.status-subcritical { color: #888; }


    .pulsing-circle {
        width: 15px;
        height: 15px;
        background-color: #ccc; /* Default grey */
        border-radius: 50%;
        opacity: 0; /* Hidden by default */
        transition: background-color 0.5s ease;
    }

    .pulsing-circle.active {
        opacity: 1; /* Show when active */
        animation: pulse 1s infinite ease-out;
    }

     .pulsing-circle.active.critical { background-color: var(--accent-color); animation-duration: 0.7s; }
     .pulsing-circle.active.supercritical { background-color: var(--danger-color); animation: pulse-fast 0.3s infinite ease-out; }
     .pulsing-circle.active.subcritical { background-color: var(--primary-color); opacity: 0.5; animation-duration: 1.5s; }


    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }

     @keyframes pulse-fast {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.5); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }

    @keyframes pulse-text {
        0% { opacity: 1; }
        100% { opacity: 0.6; }
    }

     @keyframes blink {
        0% { opacity: 1; }
        100% { opacity: 0; }
    }


    .chart-container {
        width: 100%;
        height: 300px; /* Fixed height for chart */
        position: relative;
    }

    #simulation-chart {
        display: block;
        width: 100% !important;
        height: 100% !important; /* Use 100% to fill container */
    }

    #start-simulation-button {
        display: block;
        width: 250px;
        margin: 20px auto 0 auto;
        padding: 12px 25px;
        background-color: var(--success-color);
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        font-size: 1.1em;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease-in-out;
        box-shadow: 0 4px 8px rgba(46, 204, 113, 0.3);
    }

    #start-simulation-button:hover {
        background-color: #27ae60;
        box-shadow: 0 5px 10px rgba(39, 174, 96, 0.4);
    }
     #start-simulation-button:active {
         transform: scale(0.98);
         box-shadow: 0 2px 5px rgba(39, 174, 96, 0.4);
     }
     #start-simulation-button:disabled {
         background-color: #bdc3c7;
         cursor: not-allowed;
         box-shadow: none;
     }


     .toggle-button {
        display: block;
        width: 300px;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        font-size: 1.1em;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease-in-out;
        box-shadow: 0 4px 8px rgba(74, 144, 226, 0.3);
     }

     .toggle-button:hover {
         background-color: #3a7bd5;
         box-shadow: 0 5px 10px rgba(58, 123, 213, 0.4);
     }
      .toggle-button:active {
         transform: scale(0.98);
          box-shadow: 0 2px 5px rgba(58, 123, 213, 0.4);
     }


    .explanation-section {
        border: 1px solid var(--border-color);
        padding: 25px;
        margin-top: 20px;
        background-color: var(--background-dark);
        border-radius: 12px;
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        display: none; /* Hidden by default */
    }

    .explanation-section h2, .explanation-section h3 {
        color: var(--heading-color);
    }

    .explanation-section ul, .explanation-section ol {
        margin: 15px 0 15px 20px; /* Add margin and padding for list style */
        padding-left: 20px;
    }

    .explanation-section li {
        margin-bottom: 12px;
        padding-left: 5px;
         text-align: justify;
    }

     /* Responsive adjustments */
    @media (max-width: 600px) {
        .interactive-widget {
            padding: 15px;
            margin: 20px auto;
        }

        .controls {
            grid-template-columns: 1fr;
            gap: 15px;
        }

        #start-simulation-button, .toggle-button {
            width: 100%;
            max-width: 250px;
             font-size: 1em;
        }

        .chart-container {
            height: 250px; /* Reduce height on smaller screens */
        }
    }
</style>

<script>
    const u235Input = document.getElementById('u235-concentration');
    const u235ValueSpan = document.getElementById('u235-value');
    const moderatorInput = document.getElementById('moderator-amount');
    const moderatorValueSpan = document.getElementById('moderator-value');
    const poisonInput = document.getElementById('poison-amount');
    const poisonValueSpan = document.getElementById('poison-value');
    const startButton = document.getElementById('start-simulation-button');
    const canvas = document.getElementById('simulation-chart');
    const ctx = canvas.getContext('2d');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation-button');
    const statusIndicator = document.getElementById('simulation-status');
    const pulsingCircle = document.getElementById('pulsing-circle');

    let chartData = [];
    let simulationRunning = false;
    let simulationFrameId = null; // To cancel animation frame

    // --- Update span values when sliders move ---
    u235Input.addEventListener('input', () => {
        u235ValueSpan.textContent = `${parseFloat(u235Input.value).toFixed(1)}%`; // Format to 1 decimal
    });
    moderatorInput.addEventListener('input', () => {
        moderatorValueSpan.textContent = `${moderatorInput.value}%`;
    });
    poisonInput.addEventListener('input', () => {
        poisonValueSpan.textContent = `${parseFloat(poisonInput.value).toFixed(1)}`; // Format to 1 decimal
    });

    // --- Toggle explanation visibility ---
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מפורט';
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' }); // Scroll to explanation
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'גלה את הסודות: הסבר מפורט';
        }
    });

    // --- Chart Drawing Function (Optimized for Animation) ---
    function drawChart(data) {
        const width = canvas.offsetWidth;
        const height = canvas.offsetHeight;
        canvas.width = width * window.devicePixelRatio; // Support high-DPI screens
        canvas.height = height * window.devicePixelRatio;
        ctx.scale(window.devicePixelRatio, window.devicePixelRatio); // Scale context

        ctx.clearRect(0, 0, width, height);

        // Chart parameters
        const padding = { top: 20, right: 20, bottom: 40, left: 50 };
        const usableWidth = width - padding.left - padding.right;
        const usableHeight = height - padding.top - padding.bottom;

        // Find max value for scaling (add some padding above max)
        const maxVal = Math.max(5, ...data) * 1.1; // Ensure chart starts above 0, add 10% buffer
        const yScale = usableHeight / maxVal;

        const xStep = usableWidth / (data.length > 1 ? data.length - 1 : Math.max(1, 100)); // Avoid division by zero, ensure some width even with few points
        const startX = padding.left;
        const chartBottomY = height - padding.bottom;

        // Draw Axes and Labels
        ctx.strokeStyle = '#ccc'; // Lighter axis color
        ctx.lineWidth = 1;

        // Y-axis
        ctx.beginPath();
        ctx.moveTo(startX, padding.top);
        ctx.lineTo(startX, chartBottomY);
        ctx.stroke();

        // X-axis
        ctx.beginPath();
        ctx.moveTo(startX, chartBottomY);
        ctx.lineTo(width - padding.right, chartBottomY);
        ctx.stroke();

        ctx.font = '12px Arial';
        ctx.fillStyle = var(--text-color);
        ctx.textAlign = 'center';

        // Y-axis label
        ctx.save();
        ctx.translate(padding.left / 2 - 10, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('עוצמת תגובה (קצב יחסי)', 0, 0);
        ctx.restore();

        // X-axis label
        ctx.fillText('זמן סימולציה (צעדים)', width / 2, height - 10);

         // Add Y-axis ticks and labels
        const numYTicks = 5;
        for (let i = 0; i <= numYTicks; i++) {
            const value = (maxVal / numYTicks) * i;
            const y = chartBottomY - (value * yScale);
            ctx.beginPath();
            ctx.moveTo(startX - 5, y);
            ctx.lineTo(startX + 5, y);
            ctx.strokeStyle = '#ccc';
            ctx.stroke();
            ctx.textAlign = 'right';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = '#555';
            ctx.fillText(value.toFixed(value < 10 ? 1 : 0), startX - 10, y);
        }


        // Draw data line
        if (data.length > 0) {
            ctx.beginPath();
            ctx.strokeStyle = var(--primary-color);
            ctx.lineWidth = 2;
            ctx.lineJoin = 'round'; // Smoother corners

            ctx.moveTo(startX, chartBottomY - (data[0] * yScale));

            for (let i = 1; i < data.length; i++) {
                const x = startX + i * xStep;
                const y = chartBottomY - (data[i] * yScale);
                ctx.lineTo(x, y);
            }
            ctx.stroke();
        }
    }

    // --- Simulation Logic ---
    function runSimulationStep(u235, moderator, poison, currentRate, effectiveMod, clampedMod, time) {
        // Model parameters (tuned for potential pulsing)
        const u235Sensitivity = 0.05; // How much U235 affects base reactivity
        const poisonSensitivity = 0.08; // How much poison affects base reactivity
        const moderatorSensitivity = 0.06; // How much effective moderator affects reactivity
        const heatingRate = 0.005; // How fast power reduces effective moderator
        const coolingRate = 0.02; // How fast effective moderator recovers towards clamped level
        const baseGrowthFactor = 0.1; // Base multiplier for growth rate

        // Base Reactivity: Depends on U235 and Poison
        // Use Oklo-like U235 (3.5%) as a baseline reference
        const baseReactivity = (u235 - 3.5) * u235Sensitivity - poison * poisonSensitivity;

        // Moderator Effectiveness: Peaks at optimal level, reduced by heating
        const optimalModerator = 15; // Oklo's water level
        // Simple quadratic model for potential effectiveness (0-1 range)
        const potentialModEffectFactor = 1 - Math.pow((moderator - optimalModerator) / 40, 2); // Range 0 to 40 used for scaling
        clampedMod = Math.max(0, Math.min(1, potentialModEffectFactor));

        // Effective Moderator: Starts at clamped, reduced by current power, recovers over time
        // Update effectiveMod towards clampedMod, but reduce based on high power
        const heatingEffect = Math.max(0, currentRate * heatingRate);
        const coolingEffect = (clampedMod - effectiveMod) * coolingRate;

        effectiveMod += coolingEffect - heatingEffect;
        // Clamp effectiveMod to be between 0 and the maximum potential (clampedMod)
        effectiveMod = Math.max(0, Math.min(clampedMod, effectiveMod));


        // Total Reactivity: Sum of base effects and effective moderator effect
        let reactivity = baseReactivity + (effectiveMod * moderatorSensitivity);

        // Clamp reactivity to prevent explosion/collapse and make pulsing more visible
        // Limits the rate of change per step
        reactivity = Math.max(-0.15, Math.min(0.15, reactivity)); // Allows for moderate growth/decay

        // Update fission rate
        let nextRate = currentRate + (currentRate * reactivity * baseGrowthFactor);

        // Ensure rate doesn't drop to zero (always potential for random fission)
        nextRate = Math.max(0.1, nextRate);

         // Limit max rate for chart visibility and stability
        nextRate = Math.min(200, nextRate); // Arbitrary upper limit for visualization

        // Determine status based on rate and change
         let status = 'running';
         let pulsingClass = '';
         const rateChange = nextRate - currentRate;

         if (nextRate > 150) { // High power
              status = 'supercritical!';
              pulsingClass = 'supercritical';
         } else if (nextRate > 50) { // Significant power
             if (rateChange > 0) status = 'critical!'; // Growing
             else if (rateChange < -5) status = 'cooling...'; // Dropping fast due to "boiling"
             else status = 'critical'; // Stable high
             pulsingClass = 'critical';
         } else if (nextRate > 5) { // Low to moderate power
             status = 'critical';
             pulsingClass = 'critical';
         }
         else { // Very low power
             status = 'subcritical';
              pulsingClass = 'subcritical';
         }

         // Update status indicator and pulsing circle
         statusIndicator.textContent = `${status} (קצב: ${nextRate.toFixed(1)})`;
         statusIndicator.className = ''; // Reset classes
         statusIndicator.classList.add('status-' + status.split(' ')[0]); // Add relevant class

         pulsingCircle.className = 'pulsing-circle'; // Reset classes
         pulsingCircle.classList.add('active'); // Always active when running
         if(pulsingClass) pulsingCircle.classList.add(pulsingClass);


        return { nextRate, effectiveMod, clampedMod };
    }


    let simulationSteps = 0;
    const maxSimulationSteps = 300; // Run for a fixed number of steps

    function animateSimulation(u235, moderator, poison, currentRate, effectiveMod, clampedMod) {
         if (!simulationRunning || simulationSteps >= maxSimulationSteps) {
             simulationRunning = false;
             startButton.disabled = false;
             startButton.textContent = 'התחל סימולציה';
              statusIndicator.textContent = 'סימולציה הסתיימה';
               statusIndicator.className = 'status-ready';
              pulsingCircle.className = 'pulsing-circle'; // Hide/reset pulsing circle
             return;
         }

         // Run one simulation step
         const result = runSimulationStep(u235, moderator, poison, currentRate, effectiveMod, clampedMod, simulationSteps);

         // Add new data point
         chartData.push(result.nextRate);

         // Limit data points shown to keep chart responsive
         const maxDataPoints = 150;
         if (chartData.length > maxDataPoints) {
             chartData.shift(); // Remove oldest point
         }

         // Redraw chart
         drawChart(chartData);

         // Schedule the next step
         simulationSteps++;
         simulationFrameId = requestAnimationFrame(() => animateSimulation(u235, moderator, poison, result.nextRate, result.effectiveMod, result.clampedMod));
    }


    startButton.addEventListener('click', () => {
        if (simulationRunning) {
            // Stop simulation if running
            cancelAnimationFrame(simulationFrameId);
            simulationRunning = false;
            startButton.disabled = false;
            startButton.textContent = 'התחל סימולציה';
             statusIndicator.textContent = 'סימולציה הושהתה';
             statusIndicator.className = 'status-ready';
            pulsingCircle.className = 'pulsing-circle'; // Hide/reset pulsing circle
            return;
        }

        // Start new simulation
        simulationRunning = true;
        startButton.disabled = true; // Disable button while running
        startButton.textContent = 'מריץ... (לחץ לעצירה)';
        simulationSteps = 0;
        chartData = []; // Clear previous data

        const u235 = parseFloat(u235Input.value);
        const moderator = parseFloat(moderatorInput.value);
        const poison = parseFloat(poisonInput.value);

        // Initial state
        let initialRate = 1; // Start with a low rate
        const optimalModerator = 15; // Oklo's water level baseline
        const potentialModEffectFactor = 1 - Math.pow((moderator - optimalModerator) / 40, 2);
        let initialClampedMod = Math.max(0, Math.min(1, potentialModEffectFactor));
        let initialEffectiveMod = initialClampedMod; // Start with effective = potential

        // Initial draw with empty data or just axes
        drawChart([]);
         statusIndicator.textContent = 'מתחיל סימולציה...';
          statusIndicator.className = 'status-running';
         pulsingCircle.className = 'pulsing-circle active subcritical'; // Indicate start state

        // Start the animation loop
        simulationFrameId = requestAnimationFrame(() => animateSimulation(u235, moderator, poison, initialRate, initialEffectiveMod, initialClampedMod));
    });

    // --- Initial Setup ---
    function initializeSimulationArea() {
         // Set initial span values
        u235ValueSpan.textContent = `${parseFloat(u235Input.value).toFixed(1)}%`;
        moderatorValueSpan.textContent = `${moderatorInput.value}%`;
        poisonValueSpan.textContent = `${parseFloat(poisonInput.value).toFixed(1)}`;

        // Draw initial empty chart
        drawChart([]);
         statusIndicator.textContent = 'מוכן להתחלה';
         statusIndicator.className = 'status-ready';
          pulsingCircle.className = 'pulsing-circle'; // Ensure hidden initially

        // Redraw chart on window resize
        window.addEventListener('resize', () => drawChart(chartData)); // Redraw current data/axes
    }

    // Run initialization when script loads
    initializeSimulationArea();

</script>
```