---
title: "בריכות חורף: מסע אל החיים שמחכים לגשם"
english_slug: winter-ponds-life-waiting-for-rain
category: "אקולוגיה"
tags: [אקולוגיה, בריכות חורף, מערכות אקולוגיות, מגוון ביולוגי, סביבה]
---
<div class="intro">
    <h1>בריכות חורף: מסע אל החיים שמחכים לגשם</h1>
    <p>דמיינו שלולית קסומה שמתמלאת לפתע חיים אחרי הגשם, רק כדי להיעלם כשהשמש חוזרת. זהו העולם המופלא של בריכות החורף, מערכות אקולוגיות זמניות אך תוססות, שבהן אורגניזמים פיתחו אסטרטגיות הישרדות גאוניות כדי לשרוד את תקופת היובש. בואו נגלה יחד איך הם עושים זאת, ומה הופך את הבריכות הללו לאוצר טבע יקר מפז.</p>
</div>

<div id="simulation-app" class="app-container">
    <div class="app-header">
        <h2>מעבדת בריכת החורף הווירטואלית</h2>
        <p>שחקו עם תנאי הסביבה ובחרו מינים כדי לחזות כיצד בריכת חורף דמיונית עשויה להתנהג לאורך זמן.</p>
    </div>

    <div class="controls-section section">
        <h3><i class="icon icon-settings"></i> הגדרות עולמי:</h3>
        <div class="controls-grid">
            <div class="control-item">
                <label for="dry-duration">משך תקופת יובש (חודשים):</label>
                <input type="range" id="dry-duration" name="dry-duration" min="2" max="8" value="4">
                <span id="dry-duration-value" class="range-value">4</span>
            </div>
            <div class="control-item">
                <label for="wet-duration">משך תקופת רטיבות (חודשים):</label>
                <input type="range" id="wet-duration" name="wet-duration" min="1" max="6" value="3">
                <span id="wet-duration-value" class="range-value">3</span>
            </div>
            <div class="control-item">
                <label for="temperature">טמפרטורה ממוצעת (°C):</label>
                <input type="range" id="temperature" name="temperature" min="10" max="30" value="20">
                <span id="temperature-value" class="range-value">20</span>
            </div>
            <div class="control-item">
                <label for="rain-amount">כמות משקעים עונתית (מ"מ):</label>
                <input type="range" id="rain-amount" name="rain-amount" min="100" max="800" value="400">
                <span id="rain-amount-value" class="range-value">400</span>
            </div>
        </div>
    </div>

    <div class="species-selection section">
        <h3><i class="icon icon-species"></i> בחרו את כוכבי הבריכה (עד 4 מינים):</h3>
        <div class="species-list">
            <label class="species-item" data-species="fairy-shrimp">
                <input type="checkbox" name="species" value="fairy-shrimp" data-growth="0.15" data-dry-survival-base="0.98" data-initial-pop-factor="0.5" data-name="סרטן זימרגל">
                <span class="species-icon">🦐</span>
                <span class="species-name">סרטן זימרגל</span>
                <span class="species-desc">(מומחה קיימא: ביצי קיימא עמידות ליובש, גידול מהיר)</span>
            </label>
            <label class="species-item" data-species="tadpoles">
                <input type="checkbox" name="species" value="tadpoles" data-growth="0.2" data-dry-survival-base="0.05" data-initial-pop-factor="0.8" data-name="ראשנים">
                <span class="species-icon">🐸</span>
                <span class="species-name">ראשנים</span>
                <span class="species-desc">(רץ נגד הזמן: גידול מהיר, תלות במים, ביצי קיימא פחות עמידות/שורדים בתרדמה בבוץ)</span>
            </label>
            <label class="species-item" data-species="water-beetle">
                <input type="checkbox" name="species" value="water-beetle" data-growth="0.08" data-dry-survival-base="0.01" data-initial-pop-factor="1.2" data-name="חיפושית מים טורפת">
                <span class="species-icon">🪲</span>
                <span class="species-name">חיפושית מים טורפת</span>
                <span class="species-desc">(אורחת נודדת: מגיעה ממקורות אחרים, לא שורדת יובש בבריכה)</span>
            </label>
            <label class="species-item" data-species="water-plant">
                <input type="checkbox" name="species" value="water-plant" data-growth="0.05" data-dry-survival-base="0.99" data-initial-pop-factor="0.3" data-name="צמח מים">
                 <span class="species-icon">🌱</span>
                <span class="species-name">צמח מים</span>
                <span class="species-desc">(שורד באמצעות זרעים: צמיחה אטית יחסית, זרעי קיימא עמידים)</span>
            </label>
            <label class="species-item" data-species="generalist-insect">
                <input type="checkbox" name="species" value="generalist-insect" data-growth="0.1" data-dry-survival-base="0.02" data-initial-pop-factor="1.0" data-name="חרק מים כללי">
                <span class="species-icon">🦟</span>
                <span class="species-name">חרק מים כללי</span>
                <span class="species-desc">(מגיע עם הגשם: גידול בינוני, נודד, לא שורד יובש)</span>
            </label>
        </div>
        <p class="selection-message message"></p>
    </div>

    <button id="run-simulation" class="action-button"><i class="icon icon-run"></i> הרץ סימולציה (10 מחזורים)</button>

    <div class="results-section section">
        <h3><i class="icon icon-chart"></i> תוצאות הסימולציה:</h3>
        <canvas id="simulation-chart" width="600" height="300"></canvas>
        <div id="simulation-status" class="message"></div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button"><i class="icon icon-info"></i> הצג/הסתר הסבר על בריכות חורף</button>

<div id="explanation" class="explanation-section section">
    <h2><i class="icon icon-book"></i> הסבר: בריכות חורף - מערכת אקולוגית זמנית</h2>

    <div class="explanation-block">
        <h3>מהן בריכות מים זמניות (בריכות חורף) והיכן הן נמצאות?</h3>
        <p>בריכות חורף הן גופי מים רדודים המתמלאים מים בעונת הגשמים (בדרך כלל בחורף) ומתייבשים לחלוטין או כמעט לחלוטין בתקופת היובש (בדרך כלל בקיץ). הן מצויות באזורים רבים בעולם, במיוחד באזורים עם אקלים ים-תיכוני, מדברי למחצה, או אזורים עם קרקעות שאינן מנוקזות היטב. בישראל, בריכות חורף היו נפוצות בעבר במיוחד בשפלה, בעמקים ובצפון הנגב, וכיום רבות מהן נעלמו עקב פיתוח.</p>
    </div>

    <div class="explanation-block">
        <h3>מאפיינים ייחודיים של בריכות חורף</h3>
        <p>המאפיין המרכזי הוא מחזוריות קיצונית של רטיבות ויובש. הממים בבריכה יכולים להישאר שבועות, חודשים, או עונה שלמה, ואז להיעלם לחלוטין למשך חודשים ארוכים. בנוסף, בריכות אלו רדודות, ולכן רגישות מאוד לשינויי טמפרטורה ולקצב התאדות מהיר. גם הכימיה של המים משתנה באופן דרמטי בין תקופת הרטיבות לתקופת היובש (למשל, עלייה בריכוז מלחים ככל שהמים מתאדים).</p>
    </div>

    <div class="explanation-block">
        <h3>האתגרים האקולוגיים של חיים במערכת זמנית</h3>
        <p>האתגר הגדול ביותר הוא כמובן ההתמודדות עם תקופת היובש הבלתי נמנעת. רוב האורגניזמים החיים במים אינם יכולים לשרוד ללא מים נוזליים. אתגרים נוספים כוללים: צורך להתפתח ולהתרבות במהירות במהלך תקופת הרטיבות הקצרה, תנודות קיצוניות בתנאים הפיזיים והכימיים, ולעיתים גם טורפים המגיעים לבריכה כשיש ממים (כמו ציפורים). מצד שני, היובש התקופתי מונע התבססות של טורפים ומתחרים שאינם מותאמים לתנאים אלו (כמו דגים), מה שיוצר נישה אקולוגית ייחודית.</p>
    </div>

    <div class="explanation-block">
        <h3>אסטרטגיות הישרדות עיקריות של אורגניזמים בבריכות חורף</h3>
        <p>האורגניזמים בבריכות חורף פיתחו מגוון אסטרטגיות כדי לשרוד את תקופת היובש:</p>
        <ul>
            <li><strong>ביצי קיימא (Diapause eggs / Cysts):</strong> אסטרטגיה נפוצה ביותר, במיוחד בקרב סרטנים ותולעים. האורגניזם מייצר ביצים עמידות במיוחד ליובש, טמפרטורה קיצונית, ואפילו קרינה. ביצים אלו שורדות בקרקעית הבריכה היבשה ולעיתים נשארות רדומות שנים רבות עד שתנאי הרטיבות המתאימים יחזרו ויעודדו בקיעה.</li>
            <li><strong>זרעי קיימא:</strong> צמחי ממים רבים מייצרים זרעים עמידים שנובטים רק כשהבריכה מתמלאת ממים.</li>
            <li><strong>תרדמה (Aestivation):</strong> חלק מהאורגניזמים, כמו דו-חיים מסוימים או חלזונות מים, מסתתרים במחילות בקרקעית או בשולי הבריכה ונכנסים למצב תרדמה עד שהמים חוזרים.</li>
            <li><strong>קצב גידול והתרבות מהיר:</strong> אורגניזמים רבים מותאמים לגדול ולהתרבות במהירות מרגע הבקיעה ועד שהבריכה מתייבשת, כך שהם מספיקים להשאיר צאצאים (לרוב בצורת קיימא) שישרדו את תקופת היובש.</li>
            <li><strong>הגעה ממקורות מים אחרים:</strong> חלק מהמינים (בעיקר חרקים מעופפים) אינם שורדים את תקופת היובש בתוך הבריכה עצמה, אלא נודדים אליה ממקורות ממים קבועים יותר כשהיא מתמלאת.</li>
        </ul>
    </div>

    <div class="explanation-block">
        <h3>דוגמאות לאורגניזמים אופייניים וכיצד הם מתמודדים עם היובש</h3>
        <ul>
            <li><strong>סרטני זימרגל (Fairy Shrimp, Tadpole Shrimp):</strong> מפורסמים ביכולתם לייצר ביצי קיימא עמידות, שבוקעות תוך שעות ספורות מהרגע שהבריכה מתמלאת. הם גדלים במהירות ומגיעים לבגרות מינית בתוך שבוע-שבועיים כדי להספיק להטיל ביצים לפני שהבריכה מתייבשת.</li>
            <li><strong>ראשנים של דו-חיים (צפרדעים, קרפדות, טריטונים):</strong> מטילים ביצים בממים עם התמלאות הבריכה. הראשנים מתפתחים במהירות ומנסים לסיים את הגלגול למבוגרים יבשתיים לפני שהבריכה מתייבשת. אם הבריכה מתייבשת מוקדם מדי, הם לא שורדים. חלק מהמינים חופרים מחילות ושורדים בתרדמה בבוץ.</li>
            <li><strong>חרקי מים (שפיריות, חיפושיות מים, פשפשי מים):</strong> מינים מסוימים מטילים ביצי קיימא, אך רבים אחרים מגיעים לבריכה כבוגרים מעופפים ממקורות ממים אחרים. הדרגות המימיות שלהם מתפתחות בתוך הממים, אך הבוגרים עוזבים או מתים כשהבריכה מתייבשת (למעט מינים בודדים המסוגלים לשרוד בתרדמה).</li>
            <li><strong>צמחי מים:</strong> מתפתחים מזרעי קיימא או פקעות בקרקעית. הם גדלים במהירות, פורחים, ויוצרים זרעים חדשים לפני ההתייבשות.</li>
        </ul>
    </div>

    <div class="explanation-block">
        <h3>מבנה הקהילה האקולוגית בבריכות חורף</h3>
        <p>הקהילה בבריכות חורף מורכבת בעיקר ממינים "מומחים" המותאמים במיוחד לתנאים הזמניים (כמו סרטני זימרגל או מיני דו-חיים מהירי התפתחות), ולצידם מינים "כלליים" יותר המגיעים ממקורות ממים אחרים. הטורפים הגדולים (כמו דגים) כמעט ואינם קיימים, מה שמאפשר למינים קטנים יותר לשגשג בתקופת הרטיבות. הרכב המינים משתנה מאוד בהתאם למשך תקופת הרטיבות ולתנאים הסביבתיים האחרים.</p>
    </div>

    <div class="explanation-block">
        <h3>תפקידים אקולוגיים מרכזיים בבריכות חורף</h3>
        <p>למרות היותן זמניות, לבריכות חורף תפקידים אקולוגיים חשובים. הן מהוות מוקדים של פירוק חומר אורגני (כמו עלים שנאספים בהן), ובכך מחזירות נוטריינטים לקרקע ולסביבה. הן מספקות מקור מים ובית גידול חיוני למגוון רחב של בעלי חיים, ומשמשות כתחנות עצירה ורבייה לציפורים נודדות ובעלי חיים יבשתיים בתקופת הגשמים.</p>
    </div>

    <div class="explanation-block">
        <h3>חשיבות שימור בריכות חורף</h3>
        <p>בריכות חורף הן מהמערכות האקולוגיות המאוימות ביותר בעולם. הן מהוות בית גידול ייחודי למינים רבים שאינם יכולים להתקיים במערכות ממים קבועות, ובכך תורמות למגוון הביולוגי העולמי. שימורן חיוני לא רק למינים המצויים בסכנת הכחדה התלויים בהן, אלא גם לשמירה על תהליכים אקולוגיים חשובים ועל רצף בתי גידול בנוף.</p>
    </div>

    <div class="explanation-block">
        <h3>איומים עיקריים על בריכות חורף</h3>
        <p>האיומים המרכזיים כוללים: פיתוח ובנייה המכסים או מייבשים בריכות; זיהום מנגר חקלאי או עירוני; שינויים במשטר הממים (למשל, ניקוז או שאיבת ממים); הכנסת מינים פולשים (כמו דגי גמבוזיה, הטורפים את ראשני הדו-חיים); ושינויי אקלים המשפיעים על כמות ותזמון המשקעים.</p>
    </div>
</div>

<style>
    /* General App Styling */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f0f7f9; /* Light blue/grey background */
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
    }

    .intro h1 {
        color: #0056b3; /* Darker blue */
        text-align: center;
        margin-bottom: 15px;
        font-size: 2em;
    }
     .intro p {
         max-width: 800px;
         margin: 0 auto 30px auto;
         text-align: center;
         font-size: 1.1em;
         color: #555;
     }


    .app-container {
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        border-radius: 12px;
        background-color: #ffffff; /* White background for app */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Clear floats/margins */
    }

    .app-header {
        text-align: center;
        margin-bottom: 30px;
    }

    .app-header h2 {
        color: #007bff; /* Primary blue */
        margin-bottom: 10px;
        font-size: 1.8em;
    }

    .section {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #e9f5ff; /* Very light blue */
        border-radius: 8px;
        border: 1px solid #cce5ff; /* Light blue border */
    }

    .section h3 {
        color: #0056b3; /* Darker blue */
        margin-top: 0;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        font-size: 1.4em;
    }

    .icon {
         margin-left: 10px; /* Space after icon */
         font-size: 1.2em;
    }
    .icon-settings::before { content: '⚙️'; }
    .icon-species::before { content: '🦠'; } /* Or other icons like 🐸, 🦐, 🌱 */
    .icon-run::before { content: '▶️'; }
    .icon-chart::before { content: '📈'; }
    .icon-info::before { content: 'ℹ️'; }
     .icon-book::before { content: '📖'; }


    /* Controls Styling */
    .controls-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Responsive grid */
        gap: 20px;
    }

    .control-item {
        display: flex;
        align-items: center;
        background-color: #ffffff;
        padding: 10px 15px;
        border-radius: 5px;
        border: 1px solid #b8daff;
    }

    .control-item label {
        flex: 1;
        margin-left: 15px;
        font-weight: bold;
        color: #004085; /* Even darker blue */
    }

    .control-item input[type="range"] {
        flex: 2;
        appearance: none; /* Remove default styling */
        height: 8px;
        background: #007bff; /* Primary blue color */
        border-radius: 5px;
        outline: none;
        opacity: 0.8;
        transition: opacity .2s ease-in-out;
        margin-right: 15px;
    }

    .control-item input[type="range"]:hover {
        opacity: 1;
    }

    .control-item input[type="range"]::-webkit-slider-thumb {
        appearance: none;
        width: 20px;
        height: 20px;
        background: #0056b3; /* Darker thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #ffffff;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .control-item input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #0056b3;
        cursor: pointer;
        border-radius: 50%;
         border: 2px solid #ffffff;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }


    .range-value {
        flex: 0 0 30px; /* Fixed width */
        text-align: center;
        font-weight: bold;
        color: #004085;
    }

    /* Species Selection Styling */
    .species-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); /* Responsive grid */
        gap: 10px;
    }

    .species-item {
        display: flex;
        align-items: flex-start; /* Align items to the top */
        padding: 12px 15px;
        background-color: #ffffff;
        border: 1px solid #b8daff;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out;
        direction: rtl; /* Ensure inner elements flow correctly */
    }

     .species-item:hover {
         background-color: #e0f0ff;
         border-color: #9fcdff;
     }

    .species-item input[type="checkbox"] {
        margin-left: 15px; /* Space between checkbox and icon/text */
        margin-top: 3px; /* Vertically align with text start */
        flex-shrink: 0; /* Prevent checkbox from shrinking */
        width: 18px;
        height: 18px;
        accent-color: #007bff; /* Color for checked state */
    }

    .species-item .species-icon {
         margin-left: 10px; /* Space between icon and name */
         font-size: 1.5em;
         flex-shrink: 0;
    }

    .species-item .species-name {
        font-weight: bold;
        color: #004085;
        margin-left: 5px;
        flex-shrink: 0;
    }

    .species-item .species-desc {
         font-size: 0.9em;
         color: #555;
         flex-grow: 1; /* Allow description to take up space */
         text-align: right;
    }

     /* Style for selected species */
     .species-item input[type="checkbox"]:checked + .species-icon + .species-name + .species-desc {
        color: #000; /* Darker text color when selected */
     }
     .species-item input[type="checkbox"]:checked ~ .species-icon {
          transform: scale(1.1); /* Subtle scaling animation */
     }
     .species-item:has(input[type="checkbox"]:checked) {
          background-color: #d0e9ff; /* Light blue background for selected */
          border-color: #007bff; /* Primary blue border for selected */
     }


    .message {
        min-height: 1.2em; /* Reserve space to prevent layout shifts */
        text-align: center;
        margin-top: 15px;
        padding: 10px;
        border-radius: 5px;
    }

    .selection-message {
        color: #dc3545; /* Red for error messages */
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
    }
     .selection-message:empty {
         padding: 0;
         border: none;
         background: none;
     }


    /* Button Styling */
    .action-button, .toggle-button {
        display: flex; /* Use flexbox for icon+text centering */
        align-items: center;
        justify-content: center; /* Center content */
        width: 100%;
        padding: 12px 20px;
        font-size: 1.1em;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out, transform 0.1s ease-in-out;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
         margin-top: 15px;
    }

    .action-button {
        background-color: #28a745; /* Green for action */
        color: white;
    }

    .action-button:hover {
        background-color: #218838; /* Darker green */
         transform: translateY(-2px);
    }
     .action-button:active {
         background-color: #1e7e34;
         transform: translateY(0);
     }
     .action-button:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
         box-shadow: none;
          transform: none;
     }


    .toggle-button {
        background-color: #6c757d; /* Grey */
        color: white;
         margin: 20px auto; /* Center button below app */
         max-width: 800px; /* Match app width */
         display: flex; /* Override display: block */
    }

    .toggle-button:hover {
        background-color: #5a6268; /* Darker grey */
         transform: translateY(-2px);
    }
     .toggle-button:active {
         background-color: #545b62;
         transform: translateY(0);
     }

     .action-button .icon, .toggle-button .icon {
         margin-left: 8px; /* Space between icon and text */
         font-size: 1.1em; /* Adjust icon size relative to text */
     }


    /* Results Styling */
    .results-section {
        text-align: center;
    }

    #simulation-chart {
        display: block;
        margin: 10px auto 20px auto;
        background: #ffffff; /* White background for chart area */
        border: 1px solid #cce5ff;
        border-radius: 8px;
        padding: 10px; /* Inner padding */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

     #simulation-status {
         font-weight: bold;
         color: #004085; /* Dark blue */
         background-color: #d1ecf1; /* Light cyan */
         border: 1px solid #bee5eb;
     }


    /* Explanation Styling */
    #explanation {
        margin-top: 20px;
        padding: 30px;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        direction: rtl;
        text-align: right;
        display: none; /* Hidden by default */
        max-width: 800px;
        margin: 20px auto;
    }

     #explanation h2 {
         color: #007bff;
         margin-top: 0;
         margin-bottom: 20px;
         text-align: center;
         display: flex;
         align-items: center;
         justify-content: center;
         font-size: 1.8em;
     }
    #explanation h3 {
        color: #0056b3;
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.4em;
    }
    .explanation-block {
         margin-bottom: 20px;
         padding-bottom: 20px;
         border-bottom: 1px dashed #cce5ff; /* Subtle separator */
    }
     .explanation-block:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }

    #explanation p {
        margin-bottom: 15px;
        color: #333;
    }
    #explanation ul {
        list-style-type: disc;
        margin-right: 25px;
        padding-right: 0;
        margin-bottom: 15px;
    }
    #explanation li {
        margin-bottom: 8px;
        color: #333;
    }

    /* Improve Chart.js Tooltip - requires JS configuration as well */
    .chartjs-tooltip {
       direction: rtl;
       text-align: right;
    }

</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Get DOM elements
        const dryDurationInput = document.getElementById('dry-duration');
        const wetDurationInput = document.getElementById('wet-duration');
        const temperatureInput = document.getElementById('temperature');
        const rainAmountInput = document.getElementById('rain-amount');

        const dryDurationValue = document.getElementById('dry-duration-value');
        const wetDurationValue = document.getElementById('wet-duration-value');
        const temperatureValue = document.getElementById('temperature-value');
        const rainAmountValue = document.getElementById('rain-amount-value');

        const speciesCheckboxes = document.querySelectorAll('input[name="species"]');
        const speciesSelectionMessage = document.querySelector('.selection-message');
        const runSimulationButton = document.getElementById('run-simulation');
        const simulationStatus = document.getElementById('simulation-status');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const chartCanvas = document.getElementById('simulation-chart');

        let simulationChart;
        const MAX_SPECIES_SELECTION = 4;
        const POPULATION_CAP = 10000; // Increased cap for more dynamic range

        // Update displayed values for range inputs in real-time
        dryDurationInput.addEventListener('input', () => { dryDurationValue.textContent = dryDurationInput.value; });
        wetDurationInput.addEventListener('input', () => { wetDurationValue.textContent = wetDurationInput.value; });
        temperatureInput.addEventListener('input', () => { temperatureValue.textContent = temperatureInput.value; });
        rainAmountInput.addEventListener('input', () => { rainAmountValue.textContent = rainAmountInput.value; });

        // Limit species selection and provide feedback
        speciesCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                const checkedCount = document.querySelectorAll('input[name="species"]:checked').length;
                if (checkedCount > MAX_SPECIES_SELECTION) {
                    speciesSelectionMessage.textContent = `ניתן לבחור עד ${MAX_SPECIES_SELECTION} מינים בלבד.`;
                    checkbox.checked = false; // Prevent checking if limit is reached
                } else {
                    speciesSelectionMessage.textContent = ''; // Clear message if within limit
                }
                 // Add/remove selected class for styling
                 checkbox.closest('.species-item').classList.toggle('selected', checkbox.checked);
            });
        });

        // Simulation logic
        runSimulationButton.addEventListener('click', () => {
            const dryDuration = parseInt(dryDurationInput.value);
            const wetDuration = parseInt(wetDurationInput.value);
            const temperature = parseInt(temperatureInput.value);
            const rainAmount = parseInt(rainAmountInput.value);

            const selectedSpeciesElements = Array.from(speciesCheckboxes).filter(cb => cb.checked);
            if (selectedSpeciesElements.length === 0) {
                simulationStatus.textContent = 'אנא בחר לפחות מין אחד כדי להתחיל את הסימולציה.';
                simulationStatus.style.color = '#dc3545'; // Red color for error
                simulationStatus.style.backgroundColor = '#f8d7da';
                simulationStatus.style.border = '1px solid #f5c6cb';
                return;
            } else {
                 simulationStatus.style.color = '#004085'; // Reset to default
                 simulationStatus.style.backgroundColor = '#d1ecf1';
                 simulationStatus.style.border = '1px solid #bee5eb';
            }


            // --- Simulation Model Parameters & Logic ---
            // Growth Rate: Base monthly growth factor (from data-growth)
            // Dry Survival Base: Base monthly survival probability during dry (from data-dry-survival-base)
            // Initial Pop Factor: Multiplier for rainAmount effect on initial population (from data-initial-pop-factor)

            const species = selectedSpeciesElements.map(cb => ({
                id: cb.value,
                name: cb.dataset.name,
                growthRate: parseFloat(cb.dataset.growth), // Monthly growth factor during wet
                drySurvivalBase: parseFloat(cb.dataset.drySurvivalBase), // Monthly survival rate during dry (0-1)
                initialPopFactor: parseFloat(cb.dataset.initialPopFactor), // Affects initial population based on rain
                population: 0 // Will be initialized
            }));

            const numCycles = 10;
            const populationHistory = {}; // To store population data for charting
            species.forEach(s => {
                 // Initialize population based on rain amount
                 s.population = 50 + (rainAmount / 10) * s.initialPopFactor; // Base pop + rain effect
                 populationHistory[s.id] = [s.population]; // Record initial state (Cycle 0 start)
             });


            // --- Simulation Loop ---
            runSimulationButton.disabled = true; // Disable button during simulation
            simulationStatus.textContent = 'מריץ סימולציה... מחזור 1 / ' + numCycles;

            let currentCycle = 1; // Start from cycle 1 as 0 is initial state

            const runCycle = () => {
                if (currentCycle > numCycles) {
                    simulationComplete();
                    return;
                }

                simulationStatus.textContent = `מריץ סימולציה... מחזור ${currentCycle} / ${numCycles}`;

                species.forEach(s => {
                    // --- Wet Season (Iterate month by month) ---
                    let wetPop = s.population; // Population entering wet season

                    for (let month = 0; month < wetDuration; month++) {
                        // Temperature effect on growth (simple model: optimal at 20C, declines towards edges)
                        const tempGrowthMultiplier = 1 + (temperature - 20) / 20; // Example: at 10C = 0.5, at 30C = 1.5
                        const effectiveGrowthRate = s.growthRate * Math.max(0, tempGrowthMultiplier); // Ensure growth isn't negative

                        wetPop = wetPop * (1 + effectiveGrowthRate);

                        // Monthly wet season mortality (e.g., predation, disease)
                        wetPop = wetPop * 0.95; // 5% loss per wet month

                        // Apply population cap
                        wetPop = Math.min(wetPop, POPULATION_CAP);
                        wetPop = Math.max(0, wetPop); // Ensure population doesn't go below zero
                    }
                    s.population = wetPop; // Population at the end of wet season

                    // --- Dry Season (Iterate month by month) ---
                    let dryPop = s.population; // Population entering dry season (this population is now in dormant/resistant stage or dies)

                    for (let month = 0; month < dryDuration; month++) {
                        // Temperature effect on dry survival (higher temp = lower survival)
                        const tempSurvivalMultiplier = 1 - (temperature - 10) / 30; // Example: at 10C = 1, at 30C = ~0.33
                        const effectiveSurvivalRate = s.drySurvivalBase * Math.max(0, tempSurvivalMultiplier);

                        dryPop = dryPop * effectiveSurvivalRate;

                         dryPop = Math.max(0, dryPop); // Ensure population doesn't go below zero
                    }
                    s.population = dryPop; // Population at the end of dry season (ready for next cycle)

                     // If population dropped to near zero for non-dormant species, simulate re-colonization chance based on rain
                    if (s.drySurvivalBase < 0.1 && s.population < 10) { // Check for non-dormant and very low pop
                         const recolonizationChance = rainAmount / 1000; // Higher rain = higher chance
                         if (Math.random() < recolonizationChance) {
                             s.population = 20 + (rainAmount / 20); // Small initial population for re-colonizers
                         } else {
                              s.population = 0; // Still extinct if re-colonization fails
                         }
                     }
                });

                 // Record population at the end of the cycle
                 species.forEach(s => {
                      populationHistory[s.id].push(s.population);
                 });

                 currentCycle++;
                 // Use setTimeout to allow UI to update and potentially add visual cues later
                 // For now, it just creates a slight delay between cycle steps (not visual per month)
                 setTimeout(runCycle, 50); // Short delay per cycle step
            };

            // Start the simulation loop
            runCycle();

             // --- Simulation Complete Function ---
            const simulationComplete = () => {
                runSimulationButton.disabled = false;
                simulationStatus.textContent = 'סימולציה הסתיימה.';

                // Add summary message
                const survivedSpecies = species.filter(s => populationHistory[s.id][numCycles] > 1); // Consider population > 1 as survived
                const extinctSpecies = species.filter(s => populationHistory[s.id][numCycles] <= 1); // Consider population <= 1 as extinct

                let summaryText = 'תוצאות:';
                if (survivedSpecies.length > 0) {
                    summaryText += ` המינים ששרדו: ${survivedSpecies.map(s => s.name).join(', ')}.`;
                } else {
                    summaryText += ' לצערנו, אף מין לא שרד בתנאים אלו.';
                }
                if (extinctSpecies.length > 0) {
                    summaryText += ` המינים שנכחדו: ${extinctSpecies.map(s => s.name).join(', ')}.`;
                }

                simulationStatus.textContent += ' ' + summaryText;


                // Prepare data for chart
                const labels = Array.from({ length: numCycles + 1 }, (_, i) => `מחזור ${i}`); // Cycles 0 to 10
                const datasets = species.map(s => ({
                    label: s.name,
                    data: populationHistory[s.id],
                    borderColor: getRandomColor(), // Random color for each line
                    backgroundColor: 'rgba(0, 0, 0, 0.1)', // Subtle fill below line
                    fill: false, // Don't fill below the line
                    tension: 0.3, // Add some curve to the lines
                    pointRadius: 4, // Size of data points
                    pointHoverRadius: 6,
                    hidden: false, // Start visible
                }));

                const ctx = chartCanvas.getContext('2d');

                // Destroy previous chart instance if it exists
                if (simulationChart) {
                    simulationChart.destroy();
                }

                // Create new chart
                simulationChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: datasets
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        animation: {
                            duration: 1500, // Animation duration for chart redraw
                            easing: 'easeOutQuart'
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: 'גודל אוכלוסייה (יחידות יחסיות)',
                                    font: { size: 14, weight: 'bold' }
                                },
                                type: 'linear', // Explicitly set type
                                ticks: {
                                     callback: function(value) {
                                         if (value >= 1000) return value / 1000 + 'k'; // Format large numbers
                                         return value;
                                     }
                                }
                            },
                            x: {
                                 title: {
                                    display: true,
                                    text: 'מחזור רטיבות-יובש',
                                     font: { size: 14, weight: 'bold' }
                                 }
                            }
                        },
                        plugins: {
                            legend: {
                                position: 'top',
                                rtl: true,
                                labels: {
                                    usePointStyle: true,
                                    padding: 20,
                                    font: { size: 12 }
                                }
                            },
                            title: {
                                display: true,
                                text: 'דינמיקת אוכלוסיית המינים לאורך מחזורי בריכה',
                                font: { size: 16, weight: 'bold' }
                            },
                            tooltip: {
                               rtl: true,
                               callbacks: {
                                  title: function(context) {
                                      return context[0].label;
                                  },
                                  label: function(context) {
                                      const datasetLabel = context.dataset.label || '';
                                      const value = context.raw;
                                      return `${datasetLabel}: ${Math.round(value)}`;
                                  }
                               },
                               बॉडीAlign: 'right' // Align tooltip body to the right
                            }
                        }
                    }
                });
            };
        });

        // Helper function to get a random color
        function getRandomColor() {
            const letters = '0123456789ABCDEF';
            let color = '#';
            for (let i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }


        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
                explanationDiv.style.display = 'block';
                toggleExplanationButton.innerHTML = '<i class="icon icon-info"></i> הסתר הסבר על בריכות חורף';
            } else {
                explanationDiv.style.display = 'none';
                toggleExplanationButton.innerHTML = '<i class="icon icon-info"></i> הצג/הסתר הסבר על בריכות חורף';
            }
        });

         // Initial state setup (optional, ensure things are hidden/shown correctly on load)
         explanationDiv.style.display = 'none';
         toggleExplanationButton.innerHTML = '<i class="icon icon-info"></i> הצג/הסתר הסבר על בריכות חורף';
    });
</script>
```