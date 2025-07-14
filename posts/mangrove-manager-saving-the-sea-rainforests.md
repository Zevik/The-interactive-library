---
title: "מנהל מנגרובים: הצלת יערות הגשם של הים"
english_slug: mangrove-manager-saving-the-sea-rainforests
category: "אקולוגיה"
tags:
  - מנגרובים
  - אקולוגיה ימית
  - שימור טבע
  - מערכות אקולוגיות
  - שינויי אקלים
---
# מנהל מנגרובים: הצלת יערות הגשם של הים

החוף עומד מולך. יערות המנגרובים שלו, יערות הגשם של הים, שוקקים חיים - או שוקעים לתוך שקט מדאיג. ההחלטות שלך כאן יקבעו את גורל המערכת האקולוגית הייחודית הזו. האם תצליח לאזן בין פיתוח כלכלי הכרחי לבין שימור טבע קריטי? גלה את ההשלכות של כל פעולה - או היעדר פעולה - בסימולטור החוף.

<div id="simulation-container">
    <div id="simulation">
        <div id="map-area">
            <h2>מצב אזור החוף</h2>
            <div id="map-visual">
                 <div id="mangrove-layer" class="visual-layer"></div>
                 <div id="pollution-layer" class="visual-layer"></div>
                 <div id="development-layer" class="visual-layer"></div>
                 <div id="reserve-layer" class="visual-layer"></div>
                 <div id="wildlife-layer" class="visual-layer"></div>
                 <div id="storm-layer" class="visual-layer"></div>
            </div>
             <div class="indicator-grid">
                <div id="mangrove-health" class="indicator-bar">
                    <div class="fill"></div>
                    <span>בריאות מנגרובים: <span id="health-value">100</span>%</span>
                </div>
                 <div id="biodiversity" class="indicator-bar">
                    <div class="fill"></div>
                    <span>מגוון ביולוגי: <span id="biodiversity-value">100</span>%</span>
                </div>
                 <div id="pollution" class="indicator-bar">
                    <div class="fill"></div>
                    <span>זיהום: <span id="pollution-value">0</span>%</span>
                </div>
                 <div id="protection" class="indicator-bar">
                    <div class="fill"></div>
                    <span>הגנה מפני סופות: <span id="protection-value">100</span>%</span>
                </div>
             </div>
        </div>

        <div id="stats-area">
            <h2>נתוני ניהול</h2>
            <p>שנה: <span id="current-year">1</span> מתוך 25</p>
            <p>תקציב: $<span id="budget">5000</span></p>
            <p>הכנסות שנתיות: $<span id="income">100</span></p>
            <p>הוצאות שנתיות: $<span id="expenses">50</span></p>
            <div id="messages"></div>
        </div>

        <div id="controls-area">
            <h2>בחר פעולה</h2>
            <button id="action-hotel" data-cost="2000" data-income="300" data-health="-20" data-biodiversity="-15" data-dev="+10" title="עלות: $2000, הכנסה מיידית: +$300, השפעה מיידית: -20% בריאות, -15% מגוון. תופס 10% שטח פיתוח.">בנה אתר נופש (מלון)</button>
            <button id="action-port" data-cost="3000" data-income="500" data-health="-30" data-biodiversity="-25" data-pollution="+10" data-dev="+15" title="עלות: $3000, הכנסה מיידית: +$500, השפעה מיידית: -30% בריאות, -25% מגוון, +10% זיהום. תופס 15% שטח פיתוח.">בנה נמל מסחרי</button>
            <button id="action-reserve" data-cost="1000" data-expenses="100" data-health="+10" data-biodiversity="+5" data-res="+15" title="עלות: $1000, הוצאה שנתית: +$100, השפעה מיידית: +10% בריאות, +5% מגוון. הופך 15% לשמורת טבע (משפר התאוששות לאורך זמן).">הכרז שמורת טבע</button>
            <button id="action-clean" data-cost="1500" data-pollution="-50" title="עלות: $1500, השפעה מיידית: -50% זיהום קיים.">צא למבצע ניקוי זיהום</button>
            <button id="action-plant" data-cost="500" data-plant="+1" title="עלות: $500. שתילת מנגרובים חדשים (השפעה חיובית על הבריאות בעתיד הרחוק).">שתול מנגרובים חדשים</button>

            <button id="next-year">התקדם לשנה הבאה (<span id="years-left">24</span> שנים נותרו)</button>
        </div>

        <div id="game-status" class="overlay" style="display: none;">
            <div class="status-box">
                <h2 id="status-title"></h2>
                <p id="status-message"></p>
                <button id="restart-game">התחל משחק חדש</button>
            </div>
        </div>
    </div>
</div>


<button id="toggle-explanation">הצג הסבר על מנגרובים</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: העולם המופלא של המנגרובים</h2>

    <h3>מהם מנגרובים?</h3>
    <p>מנגרובים הם קבוצה של עצים ושיחים מיוחדים במינם, המסוגלים לשרוד ולשגשג בסביבות מלוחות ובוציות לאורך חופי ימים ושפכי נהרות באזורים טרופיים וסוב-טרופיים. תארו לעצמכם יער שמסוגל לחיות במי מלח!</p>
    <ul>
        <li>**אדפטיציות מדהימות:** כדי לשרוד בתנאים קיצוניים אלה, המנגרובים פיתחו מנגנונים מיוחדים כמו שורשי אוויר (פנאומטופורים) לנשימה ושורשי תמיכה (Stilt roots) ליציבות בקרקע הרכה, ויכולת לסנן או להפריש מלחים.</li>
        <li>**מגוון מינים:** בעולם קיימים למעלה מ-80 מינים שונים של מנגרובים, כל אחד מותאם לנישה מעט שונה בסביבת החוף. בישראל, המנגרובים היחידים נמצאים בפינה קטנה ומיוחדת במפרץ אילת.</li>
    </ul>

    <h3>מדוע מנגרובים חיוניים לכדור הארץ?</h3>
    <p>מערכות המנגרובים הן לא סתם יערות - הן "יערות הגשם של הים", נקודות חמות של מגוון ביולוגי וספקיות שירותים אקולוגיים ואנושיים שלא יסולאו בפז:</p>
    <ul>
        <li>**גן עדן ימי:** שורשיהם המסועפים והאווירים יוצרים סביבה תלת-ממדית מורכבת, המשמשת כבית גידול בטוח, אזור רבייה, משתלה טבעית, ומקום מסתור לאינספור יצורים: דגים צעירים (כולל כאלה החשובים לשוניות אלמוגים ולדיג מסחרי), סרטנים, צדפות, ציפורים נודדות, זוחלים וחרקים. הם הבסיס למארג מזון ימי עשיר.</li>
        <li>**חומה ירוקה:** יערות המנגרובים מהווים מחסום טבעי עוצמתי המגן על קווי החוף והיישובים האנושיים מפני שחיקת קרקע (ארוזיה), גלים גבוהים, סופות טרופיות ואף צונאמי. הם בולמים את עוצמת הים ומייצבים את הקרקע.</li>
        <li>**ספוגי פחמן ומסנני מים:** המנגרובים קולטים כמויות אדירות של פחמן דו-חמצני מהאטמוספירה (פי כמה וכמה יותר מיערות יבשתיים), וקוברים אותו בקרקע הבוצית, ובכך תורמים משמעותית למאבק בשינויי האקלים. בנוסף, הם מסננים מזהמים ומשקעים שמגיעים מהיבשה לפני שהם מגיעים לים הפתוח או לשוניות האלמוגים.</li>
        <li>**פרנסה ובריאות:** המערכות האקולוגיות הבריאות שתומכים בהן המנגרובים חיוניות לתעשיית הדיג המקומית ולתיירות אקולוגית, ומספקות משאבים חיוניים לקהילות חוף.</li>
    </ul>

    <h3>איומים על גן העדן הזה:</h3>
    <p>לצערנו, יערות המנגרובים נעלמים בקצב מדאיג, בעיקר עקב לחצים אנושיים:</p>
    <ul>
        <li>**הרס ישיר:** המרה של אזורי מנגרובים לבריכות חקלאיות (בעיקר שרימפס), אזורי תיירות, נמלים, תשתיות עירוניות ותעשייתיות.</li>
        <li>**זיהום:** שפכים, פסולת תעשייתית ופלסטיק, נפט וחומרי הדברה פוגעים ישירות בעצים ובחיים שבמנגרובים.</li>
        <li>**שינויי אקלים:** עליית מפלס הים מאיימת להטביע אזורים מסוימים, שינויים בטמפרטורה ובמליחות משבשים את יכולת המנגרובים לשרוד ולהתרבות. סופות חזקות יותר גורמות לנזק פיזי ישיר.</li>
        <li>**ניצול יתר:** כריתת עצים לדלק או חומרי בניין ודיג לא מבוקר פוגעים במערכת.</li>
    </ul>

    <h3>הדרך לשיקום והגנה:</h3>
    <p>שימור המנגרובים דורש שילוב של פעולות:</p>
    <ul>
        <li>**הגנה חוקית:** הכרזה על אזורים כמוגנים ושמורות טבע.</li>
        <li>**שיקום פעיל:** שתילה מחדש של מנגרובים באזורים שנפגעו.</li>
        <li>**ניהול חכם:** תכנון אזורי חוף המתחשב בכלל המערכת והצרכים.</li>
        <li>**מניעת זיהום:** אכיפת חוקים ושיפור תשתיות טיפול בשפכים.</li>
        <li>**מעורבות קהילתית:** חינוך והעלאת מודעות לחשיבות המנגרובים.</li>
    </ul>

    <h3>איך זה קשור למשחק?</h3>
    <p>הסימולטור מדגים את הדילמות המורכבות שבניהול אזור חוף עם מנגרובים. כל החלטה שלך משפיעה על מדדים שונים - כלכליים (תקציב, הכנסות/הוצאות) וסביבתיים (בריאות מנגרובים, מגוון ביולוגי, זיהום, הגנה). מטרתך היא לשרוד את המשחק (25 שנים) ולהשאיר את החוף במצב הטוב ביותר האפשרי, תוך הבנה שהחלטות כלכליות מיידיות עלולות לגרום לנזק סביבתי יקר לתיקון בעתיד, וששימור סביבתי דורש השקעה אך מספק הגנה ושירותים חיוניים לאורך זמן.</p>
</div>


<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    :root {
        --color-primary: #28a745; /* Green */
        --color-secondary: #007bff; /* Blue */
        --color-danger: #dc3545; /* Red */
        --color-warning: #ffc107; /* Yellow */
        --color-info: #17a2b8; /* Cyan */
        --color-dark: #343a40; /* Dark Grey */
        --color-light: #f8f9fa; /* Light Grey */
        --color-background: #e9ecef; /* Lighter Grey */
        --color-card: #ffffff; /* White */
        --color-border: #ced4da; /* Border Grey */
        --color-water: #a0e0ff; /* Light Blue Water */
        --color-mangrove-healthy: #28a745;
        --color-mangrove-unhealthy: #6c757d; /* Greyish */
        --color-pollution: rgba(139, 69, 19, 0.5); /* Brownish semi-transparent */
        --color-development: rgba(108, 117, 125, 0.6); /* Dark grey semi-transparent */
        --color-reserve: rgba(40, 167, 69, 0.3); /* Green semi-transparent */
    }

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: var(--color-dark);
        background-color: var(--color-background);
        padding: 20px;
    }

    h1, h2, h3 {
        color: var(--color-dark);
        margin-bottom: 15px;
    }

    #simulation-container {
        max-width: 960px;
        margin: 20px auto;
        background-color: var(--color-card);
        border: 1px solid var(--color-border);
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        position: relative; /* Needed for absolute positioning of overlay */
    }

    #simulation {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        padding: 25px;
    }

    #map-area {
        flex: 2;
        min-width: 300px;
        display: flex;
        flex-direction: column;
    }

     #stats-area {
        flex: 1;
        min-width: 250px;
        background-color: var(--color-light);
        padding: 20px;
        border-radius: 8px;
        height: fit-content;
        border: 1px solid var(--color-border);
    }

    #stats-area p {
        margin-bottom: 8px;
        font-size: 1.1em;
    }
    #stats-area span {
        font-weight: bold;
        color: var(--color-secondary);
    }

    #controls-area {
        flex-basis: 100%;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 12px;
        margin-top: 20px;
        border-top: 1px solid var(--color-border);
        padding-top: 20px;
    }

    #controls-area h2 {
        grid-column: 1 / -1; /* Span all columns */
        margin-bottom: 10px;
    }

    #controls-area button {
         grid-column: auto; /* Reset span for buttons */
         font-size: 0.95em;
         text-align: center;
    }


    #map-visual {
        width: 100%;
        height: 280px;
        background-color: var(--color-water);
        border: 1px solid var(--color-border);
        border-radius: 8px;
        position: relative;
        overflow: hidden;
        margin-top: 10px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }

    .visual-layer {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%; /* Will be adjusted by JS */
        transition: all 1s ease-in-out; /* Smooth transitions for changes */
        pointer-events: none; /* Allow clicks to pass through layers */
    }

    #mangrove-layer {
        background: linear-gradient(to top, var(--color-mangrove-healthy), transparent);
        background-size: 100% 200%; /* Control visibility via background-position */
        background-position: 0 100%; /* Initially fully visible from bottom */
         opacity: 0.9;
    }

    #pollution-layer {
        background-color: var(--color-pollution);
        height: 0%; /* Initially no pollution */
        opacity: 0;
        transition: height 0.5s ease-in-out, opacity 0.5s ease-in-out;
    }

    #development-layer {
        background-color: var(--color-development);
        height: 0%; /* Initially no development */
         opacity: 0;
        transition: height 0.5s ease-in-out, opacity 0.5s ease-in-out;
         top: 0; /* Development often encroaches from top/land side */
         bottom: auto;
    }

     #reserve-layer {
        background-color: var(--color-reserve);
        height: 100%; /* Represents an overlay on the whole map */
        opacity: 0; /* Initially no reserve */
        transition: opacity 0.5s ease-in-out;
     }

     #wildlife-layer {
         /* Placeholder for potential future wildlife icons/animations */
         z-index: 5;
     }
     #storm-layer {
         background-color: rgba(100, 100, 100, 0.3); /* Grey overlay */
         opacity: 0;
         z-index: 6;
         transition: opacity 0.3s ease-in-out;
     }


    .indicator-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-top: 15px;
    }

    .indicator-bar {
        width: 100%;
        background-color: var(--color-light);
        border-radius: 20px;
        margin-bottom: 0; /* Adjusted for grid */
        overflow: hidden;
        position: relative;
        height: 30px;
        text-align: center;
        border: 1px solid var(--color-border);
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .indicator-bar .fill {
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        transition: width 0.6s ease-in-out, background-color 0.6s ease-in-out;
        border-radius: 20px 0 0 20px; /* Match parent curve */
         box-shadow: inset 0 1px 3px rgba(255, 255, 255, 0.3);
    }

    #mangrove-health .fill { background: linear-gradient(to right, #4CAF50, #8BC34A); } /* Green */
    #biodiversity .fill { background: linear-gradient(to right, #03A9F4, #81D4FA); } /* Blue */
    #pollution .fill { background: linear-gradient(to right, #F44336, #E57373); } /* Red */
    #protection .fill { background: linear-gradient(to right, #FF9800, #FFB74D); } /* Orange */

    /* Color scale for fills based on value (basic implementation) */
    /* Could add more complex gradients or step changes via JS */
    #mangrove-health .fill[style*="width"] { background: linear-gradient(to right, var(--color-primary), var(--color-primary)); }
    #mangrove-health .fill[style*="width: 50"] { background: linear-gradient(to right, var(--color-warning), var(--color-warning)); }
    #mangrove-health .fill[style*="width: 20"] { background: linear-gradient(to right, var(--color-danger), var(--color-danger)); }


    .indicator-bar span {
        position: relative;
        z-index: 1;
        line-height: 30px;
        color: var(--color-dark);
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.6);
        font-size: 0.9em;
    }

    button {
        padding: 10px 15px;
        background-color: var(--color-secondary);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
    }

    button:active:not(:disabled) {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
        box-shadow: none;
    }


    #next-year {
        grid-column: 1 / -1; /* Full width */
        background-color: var(--color-primary);
        margin-top: 10px;
        font-size: 1.1em;
        font-weight: bold;
    }

    #next-year:hover:not(:disabled) {
        background-color: #218838;
    }


    #messages {
        margin-top: 15px;
        padding: 10px;
        border: 1px solid var(--color-border);
        background-color: var(--color-card);
        min-height: 80px;
        font-size: 0.9em;
        border-radius: 8px;
        overflow-y: auto; /* Scroll if many messages */
        max-height: 150px;
    }

    #messages h3 {
        margin-top: 0;
        margin-bottom: 5px;
        color: var(--color-secondary);
    }

    #messages p {
        margin-bottom: 5px;
        padding-bottom: 5px;
        border-bottom: 1px dashed var(--color-light);
        opacity: 0; /* Start hidden */
        animation: fadeIn 0.5s ease-out forwards; /* Fade in effect */
    }
     #messages p:last-child {
         border-bottom: none;
     }

    @keyframes fadeIn {
        to { opacity: 1; }
    }

     .overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(var(--color-dark-rgb, 52, 58, 64), 0.8); /* Semi-transparent dark overlay */
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10;
        backdrop-filter: blur(5px); /* Blur effect */
        -webkit-backdrop-filter: blur(5px); /* Safari support */
     }

    .status-box {
        background-color: var(--color-card);
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        max-width: 500px;
        width: 90%;
    }

     #status-title {
         font-size: 2em;
         margin-bottom: 15px;
     }
     #status-message {
         font-size: 1.2em;
         margin-bottom: 25px;
         color: var(--color-dark);
     }

     #status-title.win { color: var(--color-primary); }
     #status-title.partial { color: var(--color-warning); }
     #status-title.lose { color: var(--color-danger); }


     #restart-game {
         background-color: var(--color-info);
         font-size: 1.1em;
     }
     #restart-game:hover {
         background-color: #138496;
     }


    #toggle-explanation {
         display: block;
         margin: 30px auto;
         padding: 12px 25px;
         background-color: var(--color-info);
         color: white;
         border: none;
         border-radius: 5px;
         cursor: pointer;
         font-size: 1em;
         transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: #138496;
         transform: translateY(-1px);
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
    }
     #toggle-explanation:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
     }


    #explanation {
        max-width: 800px;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid var(--color-border);
        border-radius: 8px;
        background-color: var(--color-card);
        line-height: 1.7;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }

    #explanation h2, #explanation h3 {
        color: var(--color-dark);
        margin-top: 20px;
        margin-bottom: 10px;
    }
     #explanation h2 { color: var(--color-secondary); }
     #explanation h3 { color: var(--color-primary); }


    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* RTL adjust */
    }

    #explanation li {
        margin-bottom: 8px;
    }

    @media (max-width: 768px) {
        #simulation {
            flex-direction: column;
        }
        #map-area, #stats-area {
            flex: auto;
            min-width: auto;
        }
        .indicator-grid {
             grid-template-columns: 1fr;
        }
         #controls-area {
             grid-template-columns: 1fr;
         }
    }

    /* Basic animation for indicator bars filling */
    .indicator-bar .fill {
      animation: fillAnimation 0.6s ease-in-out forwards;
    }

    /* Note: This animation will run every time the element's style is set.
             For more complex animations on change, JS might be needed
             to toggle classes or manage animation state.
             Keeping it simple with CSS transition on width for now. */


</style>

<script>
    const maxYears = 25;

    let gameState = {
        year: 1,
        budget: 5000,
        income: 100,
        expenses: 50,
        mangroveHealth: 100, // 0-100
        biodiversity: 100,    // 0-100
        pollution: 0,         // 0-100
        stormProtection: 100, // 0-100 (Calculated based on health/reserve)
        developedArea: 0,     // % of area developed (max 50%)
        reserveArea: 0,       // % of area is reserve (max 50%)
        plantedMangroves: 0,  // Counter for long-term effect (max 10 actions)
        messages: []
    };

    const elements = {
        year: document.getElementById('current-year'),
        yearsLeft: document.getElementById('years-left'),
        budget: document.getElementById('budget'),
        income: document.getElementById('income'),
        expenses: document.getElementById('expenses'),
        health: document.getElementById('health-value'),
        biodiversity: document.getElementById('biodiversity-value'),
        pollution: document.getElementById('pollution-value'),
        protection: document.getElementById('protection-value'),
        healthFill: document.querySelector('#mangrove-health .fill'),
        biodiversityFill: document.querySelector('#biodiversity .fill'),
        pollutionFill: document.querySelector('#pollution .fill'),
        protectionFill: document.querySelector('#protection .fill'),
        mangroveLayer: document.getElementById('mangrove-layer'),
        pollutionLayer: document.getElementById('pollution-layer'),
        developmentLayer: document.getElementById('development-layer'),
        reserveLayer: document.getElementById('reserve-layer'),
        stormLayer: document.getElementById('storm-layer'),
        messages: document.getElementById('messages'),
        actionHotel: document.getElementById('action-hotel'),
        actionPort: document.getElementById('action-port'),
        actionReserve: document.getElementById('action-reserve'),
        actionClean: document.getElementById('action-clean'),
        actionPlant: document.getElementById('action-plant'),
        nextYearButton: document.getElementById('next-year'),
        gameStatus: document.getElementById('game-status'),
        statusTitle: document.getElementById('status-title'),
        statusMessage: document.getElementById('status-message'),
        restartButton: document.getElementById('restart-game'),
        explanationDiv: document.getElementById('explanation'),
        toggleExplanationButton: document.getElementById('toggle-explanation')
    };

    function updateSimulationDisplay() {
        elements.year.textContent = gameState.year;
        elements.yearsLeft.textContent = maxYears - gameState.year;
        elements.budget.textContent = Math.round(gameState.budget);
        elements.income.textContent = Math.round(gameState.income);
        elements.expenses.textContent = Math.round(gameState.expenses);

        const health = Math.max(0, Math.round(gameState.mangroveHealth));
        const biodiversity = Math.max(0, Math.round(gameState.biodiversity));
        const pollution = Math.max(0, Math.round(gameState.pollution));
        const protection = Math.max(0, Math.round(gameState.stormProtection));


        elements.health.textContent = health;
        elements.biodiversity.textContent = biodiversity;
        elements.pollution.textContent = pollution;
        elements.protection.textContent = protection;

        // Update fill bars width and color based on value
        elements.healthFill.style.width = health + '%';
        elements.biodiversityFill.style.width = biodiversity + '%';
        elements.pollutionFill.style.width = pollution + '%';
        elements.protectionFill.style.width = protection + '%';

        // Optional: Change fill bar color based on value thresholds
        elements.healthFill.style.backgroundColor = health > 70 ? 'var(--color-primary)' : (health > 40 ? 'var(--color-warning)' : 'var(--color-danger)');
        elements.biodiversityFill.style.backgroundColor = biodiversity > 70 ? 'var(--color-info)' : (biodiversity > 40 ? 'orange' : 'red');
        elements.pollutionFill.style.backgroundColor = pollution < 30 ? 'var(--color-primary)' : (pollution < 60 ? 'var(--color-warning)' : 'var(--color-danger)');
        elements.protectionFill.style.backgroundColor = protection > 70 ? 'var(--color-primary)' : (protection > 40 ? 'var(--color-warning)' : 'var(--color-danger)');


        // Update visual representation layers
        // Mangroves: Higher health means background-position closer to 100% (fully green from bottom)
        const mangroveVisualPercentage = gameState.mangroveHealth * 0.7 + (100 - gameState.developedArea) * 0.3; // Mix health and undeveloped area
        elements.mangroveLayer.style.backgroundPosition = `0 ${100 - mangroveVisualPercentage}%`;

        // Pollution: Height of layer represents pollution level
        elements.pollutionLayer.style.height = gameState.pollution + '%';
        elements.pollutionLayer.style.opacity = gameState.pollution > 5 ? (gameState.pollution / 100) : 0; // Fade in based on level

        // Development: Height of layer from top represents developed area
        elements.developmentLayer.style.height = gameState.developedArea + '%';
         elements.developmentLayer.style.opacity = gameState.developedArea > 5 ? (gameState.developedArea / 50) * 0.8 : 0; // Fade in based on level, max 50% dev

        // Reserve: Opacity of layer represents reserve area
        elements.reserveLayer.style.opacity = gameState.reserveArea > 5 ? (gameState.reserveArea / 50) * 0.4 : 0; // Fade in based on level, max 50% reserve


        // Update messages with fade-in animation
        const messagesHtml = '<h3>הודעות מהשטח:</h3>' + gameState.messages.map(msg => `<p>${msg}</p>`).join('');
        elements.messages.innerHTML = messagesHtml;

        // Apply fade-in animation to newly added messages
        const messageElements = elements.messages.querySelectorAll('p');
        messageElements.forEach((p, index) => {
            p.style.animationDelay = `${index * 0.1}s`; // Stagger the animation
        });

        gameState.messages = []; // Clear messages after displaying


        // Update button availability
        elements.actionHotel.disabled = gameState.budget < 2000 || gameState.developedArea >= 50;
        elements.actionPort.disabled = gameState.budget < 3000 || gameState.developedArea >= 50;
        elements.actionReserve.disabled = gameState.budget < 1000 || gameState.reserveArea >= 50;
        elements.actionClean.disabled = gameState.budget < 1500 || gameState.pollution < 15; // Need minimum pollution to clean
        elements.actionPlant.disabled = gameState.budget < 500 || gameState.plantedMangroves >= 10; // Limit planting efforts


        if (gameState.year > maxYears || gameState.mangroveHealth <= 5 || gameState.budget < -15000 || (gameState.developedArea >= 50 && gameState.reserveArea < 10 && gameState.mangroveHealth < 30)) {
            endGame();
        }
    }

    function addMessage(message, type = 'info') {
         // type can be 'info', 'warning', 'danger', 'success' - for future styling
        gameState.messages.push(message);
    }

    function advanceYear() {
        if (gameState.year > maxYears || elements.gameStatus.style.display !== 'none') {
             // Game already ended or is showing status
             return;
        }

        gameState.year++;
        let yearlySummary = `**סיכום שנה ${gameState.year}:** `;

        // Apply yearly financials
        gameState.budget += gameState.income;
        gameState.budget -= gameState.expenses;
        yearlySummary += `תקציב נוכחי $${Math.round(gameState.budget)}. `;


        // --- Environmental Changes & Long-Term Effects ---

        let healthChange = 0;
        let biodiversityChange = 0;
        let pollutionChange = 0;

        // Base environmental degradation (natural + minimal impact from low dev/poll)
        healthChange -= 1;
        biodiversityChange -= 0.5;
        pollutionChange += 1; // Slow baseline pollution increase

        // Impact of Development (cumulative and ongoing)
        const devHealthImpact = (gameState.developedArea / 50) * -5; // Max -5% per year at 50% development
        const devBiodiversityImpact = (gameState.developedArea / 50) * -4; // Max -4% per year
        const devPollutionIncrease = (gameState.developedArea / 50) * 3; // Max +3% per year
        healthChange += devHealthImpact;
        biodiversityChange += devBiodiversityImpact;
        pollutionChange += devPollutionIncrease;
        if (gameState.developedArea > 0) {
             yearlySummary += `הפיתוח האנושי פוגע בסביבה (${devHealthImpact.toFixed(1)} בריאות, ${devBiodiversityImpact.toFixed(1)} מגוון, +${devPollutionIncrease.toFixed(1)} זיהום). `;
        }


        // Impact of Reserve (cumulative and ongoing)
        const reserveHealthBoost = (gameState.reserveArea / 50) * 4; // Max +4% per year at 50% reserve
        const reserveBiodiversityBoost = (gameState.reserveArea / 50) * 3; // Max +3% per year
         const reservePollutionReduction = (gameState.reserveArea / 50) * -1; // Max -1% pollution reduction
        healthChange += reserveHealthBoost;
        biodiversityChange += reserveBiodiversityBoost;
         pollutionChange += reservePollutionReduction;
        if (gameState.reserveArea > 0) {
             yearlySummary += `השמורה מסייעת להתאוששות (+${reserveHealthBoost.toFixed(1)} בריאות, +${reserveBiodiversityBoost.toFixed(1)} מגוון, ${reservePollutionReduction.toFixed(1)} זיהום). `;
        }


        // Impact of Existing Pollution on health/biodiversity
        const pollutionHealthDamage = (gameState.pollution / 100) * -8; // Max -8% per year at 100% pollution
        const pollutionBiodiversityDamage = (gameState.pollution / 100) * -10; // Max -10% per year
        healthChange += pollutionHealthDamage;
        biodiversityChange += pollutionBiodiversityDamage;
         if (gameState.pollution > 10) {
             yearlySummary += `הזיהום הקיים מחליש את המערכת (${pollutionHealthDamage.toFixed(1)} בריאות, ${pollutionBiodiversityDamage.toFixed(1)} מגוון). `;
         }


        // Impact of Planted Mangroves (delayed and cumulative effect)
        if (gameState.year > 5 && gameState.plantedMangroves > 0) { // Assume 5 years for them to establish
             const plantingEffect = gameState.plantedMangroves * 0.4; // Each planting action adds 0.4% health per year after 5 years
             healthChange += plantingEffect;
             yearlySummary += `השתילות הישנות של מנגרובים מתפתחות (+${plantingEffect.toFixed(1)} בריאות). `;
        }

        // Sea Level Rise & Storms (increases over time)
        const seaLevelBaseEffect = (gameState.year / maxYears) * 1.5; // Base effect increases over 25 years
        // Sea level rise damage is higher if mangrove health AND storm protection are low
        const seaLevelDamage = seaLevelBaseEffect * (100 - gameState.mangroveHealth / 2 - gameState.stormProtection / 2) / 100 ;
        healthChange -= seaLevelDamage;
        if (seaLevelDamage > 0.1) {
             yearlySummary += `עליית מפלס הים מתגברת ופוגעת בחוף (${-seaLevelDamage.toFixed(1)} בריאות). `;
         }


        // Random Storm Event (chance increases over time, damage depends on protection)
        const stormChance = 5 + (gameState.year / maxYears) * 20; // Chance starts at 5%, up to 25%
        if (Math.random() * 100 < stormChance) {
             const stormDamage = Math.random() * 20 * (100 - gameState.stormProtection) / 100; // Random damage up to 20, scaled by protection
             healthChange -= stormDamage;
             biodiversityChange -= stormDamage * 0.5;
              addMessage(`**אירוע סופה:** סופה עזה פקדה את האזור! נזק משמעותי עקב הגנה נמוכה.`, 'danger');
              elements.stormLayer.style.opacity = 0.5; // Visual storm effect
              setTimeout(() => { elements.stormLayer.style.opacity = 0; }, 1000); // Fade out storm effect

        } else {
             elements.stormLayer.style.opacity = 0; // Ensure storm layer is off
        }

        // Add base income/expenses message
        addMessage(`שנה חדשה החלה! ההכנסות השנתיות התקבלו ($${Math.round(gameState.income)}), ההוצאות שולמו ($${Math.round(gameState.expenses)}).`);


        // Apply aggregated changes
        gameState.mangroveHealth += healthChange;
        gameState.biodiversity += biodiversityChange;
        gameState.pollution += pollutionChange;

        // Recalculate Storm Protection (more nuanced: health, reserve, AND low pollution help)
        gameState.stormProtection = Math.min(100, Math.max(0, gameState.mangroveHealth * 0.4 + gameState.reserveArea * 0.4 + (100 - gameState.pollution) * 0.2));


        // Clamp values to be within bounds
        gameState.mangroveHealth = Math.max(0, Math.min(100, gameState.mangroveHealth));
        gameState.biodiversity = Math.max(0, Math.min(100, gameState.biodiversity));
        gameState.pollution = Math.max(0, Math.min(100, gameState.pollution));
        gameState.stormProtection = Math.max(0, Math.min(100, gameState.stormProtection));
        gameState.budget = Math.max(-20000, gameState.budget); // Set a hard bankruptcy limit


        addMessage(yearlySummary, 'info');
        updateSimulationDisplay();
    }

    function takeAction(actionType) {
        let cost = 0;
        let message = '';
        let canPerform = false;

        const actionButton = document.getElementById(`action-${actionType}`);
        if (!actionButton) return; // Should not happen

        cost = parseFloat(actionButton.dataset.cost) || 0;

        if (gameState.budget < cost) {
            addMessage(`אין מספיק כסף לפעולה '${actionButton.textContent}'. נדרש $${cost}, יש לך $${Math.round(gameState.budget)}.`, 'warning');
            return;
        }

        // Check specific conditions for actions
        switch (actionType) {
            case 'hotel':
            case 'port':
                 const devIncrease = parseFloat(actionButton.dataset.dev) || 0;
                 if (gameState.developedArea + devIncrease > 50) {
                      addMessage(`לא ניתן לבנות עוד. שטח הפיתוח המירבי הושג (${gameState.developedArea}% מתוך 50%).`, 'warning');
                      return;
                 }
                 canPerform = true;
                 break;
            case 'reserve':
                 const resIncrease = parseFloat(actionButton.dataset.res) || 0;
                 if (gameState.reserveArea + resIncrease > 50) {
                      addMessage(`לא ניתן להכריז על עוד שמורות. שטח השמורה המירבי הושג (${gameState.reserveArea}% מתוך 50%).`, 'warning');
                      return;
                 }
                 canPerform = true;
                 break;
            case 'clean':
                 if (gameState.pollution < 15) {
                      addMessage(`אין מספיק זיהום לנקות. רמת זיהום נוכחית: ${Math.round(gameState.pollution)}%.`, 'warning');
                      return;
                 }
                 canPerform = true;
                 break;
            case 'plant':
                 if (gameState.plantedMangroves >= 10) {
                      addMessage(`השנה כבר בוצע פרויקט שתילה נרחב. חכה לשנה הבאה לשתול עוד.`, 'warning');
                      return;
                 }
                 canPerform = true;
                 break;
            default:
                 canPerform = false;
        }

        if (canPerform) {
            gameState.budget -= cost;
            let actionImpactSummary = `**פעולה בוצעה:** '${actionButton.textContent}' (עלות: $${cost}).`;

            // Apply immediate effects
            if (actionButton.dataset.income) {
                 const incomeIncrease = parseFloat(actionButton.dataset.income);
                 gameState.income += incomeIncrease;
                 actionImpactSummary += ` ההכנסה השנתית עלתה ב-$${incomeIncrease}.`;
            }
            if (actionButton.dataset.expenses) {
                 const expensesIncrease = parseFloat(actionButton.dataset.expenses);
                 gameState.expenses += expensesIncrease;
                  actionImpactSummary += ` ההוצאה השנתית עלתה ב-$${expensesIncrease}.`;
            }
            if (actionButton.dataset.health) {
                 const healthChange = parseFloat(actionButton.dataset.health);
                 gameState.mangroveHealth += healthChange;
                 actionImpactSummary += ` בריאות המנגרובים השתנתה ב-${healthChange.toFixed(1)}%.`;
            }
            if (actionButton.dataset.biodiversity) {
                 const biodiversityChange = parseFloat(actionButton.dataset.biodiversity);
                 gameState.biodiversity += biodiversityChange;
                 actionImpactSummary += ` מגוון ביולוגי השתנה ב-${biodiversityChange.toFixed(1)}%.`;
            }
            if (actionButton.dataset.pollution) {
                const pollutionEffect = parseFloat(actionButton.dataset.pollution);
                if (actionType === 'clean') {
                    gameState.pollution = Math.max(0, gameState.pollution + pollutionEffect); // pollutionEffect is negative for clean
                    actionImpactSummary += ` רמת הזיהום ירדה ב-${Math.abs(pollutionEffect)}%.`;
                } else {
                    gameState.pollution += pollutionEffect;
                    actionImpactSummary += ` רמת הזיהום עלתה ב-${pollutionEffect.toFixed(1)}%.`;
                }
            }
            if (actionButton.dataset.dev) {
                 const devIncrease = parseFloat(actionButton.dataset.dev);
                 gameState.developedArea += devIncrease;
                 actionImpactSummary += ` שטח הפיתוח גדל ב-${devIncrease}%.`;
            }
            if (actionButton.dataset.res) {
                 const resIncrease = parseFloat(actionButton.dataset.res);
                 gameState.reserveArea += resIncrease;
                 actionImpactSummary += ` שטח השמורה גדל ב-${resIncrease}%.`;
            }
             if (actionButton.dataset.plant) {
                 gameState.plantedMangroves += 1; // Increment planting counter
                 actionImpactSummary += ` בוצעה שתילת מנגרובים. השפעתה תהיה ניכרת בעוד מספר שנים.`;
            }


             // Recalculate protection after action
             gameState.stormProtection = Math.min(100, Math.max(0, gameState.mangroveHealth * 0.4 + gameState.reserveArea * 0.4 + (100 - gameState.pollution) * 0.2));

            addMessage(actionImpactSummary, 'success');
            updateSimulationDisplay();
        }
    }

    function endGame() {
        // Disable all buttons
        elements.nextYearButton.disabled = true;
        elements.actionHotel.disabled = true;
        elements.actionPort.disabled = true;
        elements.actionReserve.disabled = true;
        elements.actionClean.disabled = true;
        elements.actionPlant.disabled = true;

        elements.gameStatus.style.display = 'flex'; // Show end game screen

        let statusTitle = '';
        let statusMessage = '';
        let titleClass = '';

        if (gameState.year > maxYears) {
            // Game reached the end year
            statusTitle = 'סוף המשחק!';
            if (gameState.mangroveHealth >= 75 && gameState.biodiversity >= 75 && gameState.budget >= 0) {
                statusMessage = `הצלחת לנהל את החוף למשך ${maxYears} שנים תוך שמירה מצוינת על הסביבה וניהול תקציבי נכון! בריאות מנגרובים: ${Math.round(gameState.mangroveHealth)}%, מגוון ביולוגי: ${Math.round(gameState.biodiversity)}%, תקציב סופי: $${Math.round(gameState.budget)}. כל הכבוד, אתה מנהל בר-קיימא אמיתי!`;
                titleClass = 'win';
            } else if (gameState.mangroveHealth >= 50 && gameState.biodiversity >= 50 && gameState.budget >= -5000) {
                 statusMessage = `סיימת את ${maxYears} השנים. האזור שרד והמערכת האקולוגית יציבה יחסית, אך יש מקום לשיפור. בריאות מנגרובים: ${Math.round(gameState.mangroveHealth)}%, מגוון ביולוגי: ${Math.round(gameState.biodiversity)}%, תקציב סופי: $${Math.round(gameState.budget)}. עבודה סבירה, המשך לשפר!`;
                 titleClass = 'partial';
            }
            else {
                statusMessage = `סיימת את ${maxYears} השנים, אך מצב החוף קשה. הנזק הסביבתי או הקשיים הכלכליים יקשו על עתיד האזור. בריאות מנגרובים: ${Math.round(gameState.mangroveHealth)}%, מגוון ביולוגי: ${Math.round(gameState.biodiversity)}%, תקציב סופי: $${Math.round(gameState.budget)}. נדרש שיפור ניכר בניהול.`;
                 titleClass = 'lose';
            }
        } else if (gameState.mangroveHealth <= 5) {
            statusTitle = 'הפסדת!';
            statusMessage = `מערכת המנגרובים קרסה לחלוטין (בריאות ${Math.round(gameState.mangroveHealth)}%). המגוון הביולוגי אבד, וההגנה על החוף נעלמה. הנזק בלתי הפיך.`;
            titleClass = 'lose';
        } else if (gameState.budget < -15000) {
             statusTitle = 'פשיטת רגל!';
            statusMessage = `הגעת לגרעון תקציבי עצום ($${Math.round(gameState.budget)}). אזור החוף פשט רגל ואין לך יותר משאבים לנהל אותו או לתקן נזקים.`;
             titleClass = 'lose';
        } else if (gameState.developedArea >= 50 && gameState.reserveArea < 10 && gameState.mangroveHealth < 30) {
             statusTitle = 'הפסדת!';
             statusMessage = `פיתוח יתר והזנחת הסביבה הובילו לקריסה אקולוגית למרות שהגעת לסוף השנים. בריאות המנגרובים נמוכה מדי (${Math.round(gameState.mangroveHealth)}%) כדי לקיים את המערכת לאורך זמן.`;
             titleClass = 'lose';
        }


        elements.statusTitle.textContent = statusTitle;
        elements.statusTitle.className = ''; // Clear previous classes
        elements.statusTitle.classList.add(titleClass); // Add the relevant class for color
        elements.statusMessage.textContent = statusMessage;
    }

    function restartGame() {
         gameState = {
            year: 1,
            budget: 5000,
            income: 100,
            expenses: 50,
            mangroveHealth: 100,
            biodiversity: 100,
            pollution: 0,
            stormProtection: 100,
            developedArea: 0,
            reserveArea: 0,
            plantedMangroves: 0,
            messages: []
        };
        elements.gameStatus.style.display = 'none';
        elements.nextYearButton.disabled = false;
        elements.stormLayer.style.opacity = 0; // Reset storm visual
        updateSimulationDisplay(); // Initial display
         addMessage('ברוכים הבאים למנהל המנגרובים! התחל את השנה הראשונה...');
    }


    // Event Listeners
    elements.actionHotel.addEventListener('click', () => takeAction('hotel'));
    elements.actionPort.addEventListener('click', () => takeAction('port'));
    elements.actionReserve.addEventListener('click', () => takeAction('reserve'));
    elements.actionClean.addEventListener('click', () => takeAction('clean'));
    elements.actionPlant.addEventListener('click', () => takeAction('plant'));
    elements.nextYearButton.addEventListener('click', advanceYear);
    elements.restartButton.addEventListener('click', restartGame);

    elements.toggleExplanationButton.addEventListener('click', () => {
        if (elements.explanationDiv.style.display === 'none') {
            elements.explanationDiv.style.display = 'block';
            elements.toggleExplanationButton.textContent = 'הסתר הסבר על מנגרובים';
        } else {
            elements.explanationDiv.style.display = 'none';
            elements.toggleExplanationButton.textContent = 'הצג הסבר על מנגרובים';
        }
    });


    // Initial setup
    restartGame(); // Start the first game on load

</script>