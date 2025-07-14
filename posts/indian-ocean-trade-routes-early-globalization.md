---
title: "נתיבי הסחר של האוקיינוס ההודי: סיפורה של גלובליזציה עתיקה ורשת עולם"
english_slug: indian-ocean-trade-routes-early-globalization
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags: [היסטוריה, סחר ימי, אוקיינוס הודי, מונסונים, נתיבי סחר עתיקים, גלובליזציה]
---
# נתיבי הסחר של האוקיינוס ההודי: סיפורה של גלובליזציה עתיקה ורשת עולם

דמיינו עולם שבו ספינות עץ עמוסות בתבלינים אקזוטיים, משי נוצץ, מתכות יקרות ורעיונות פורצי דרך חוצות ימים ואוקיינוסים, הרבה לפני שבכלל חשבו על המהפכה התעשייתית או עידן התגליות האירופאי. זהו עולמם של נתיבי הסחר באוקיינוס ההודי – רשת עצומה ומשגשגת שחיברה במשך אלפי שנים תרבויות, כלכלות ויבשות, כשהמנוע הבלתי מעורער שלה הוא כוח טבעי עוצמתי: רוחות המונסון העונתיות.

בואו נצא למסע אינטראקטיבי בזמן ועל פני המפה כדי לחשוף את סודותיה של גלובליזציה מוקדמת זו.

<div id="app-container">
    <div id="map-container">
        <svg id="indian-ocean-map" viewBox="0 0 1000 600" preserveAspectRatio="xMidYMid meet">
             <image href="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Indian_Ocean_bathymetry.svg/1000px-Indian_Ocean_bathymetry.svg.png" x="0" y="0" width="1000" height="600" />
            <defs>
                <marker id="arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto">
                    <path d="M 0 0 L 10 5 L 0 10 z" fill="#4CAF50" />
                </marker>
                 <!-- Define path for monsoon animation -->
                 <path id="summer-monsoon-path" d="M 300 400 C 400 350, 500 300, 600 350 C 700 400, 800 450, 900 450"></path>
                 <path id="winter-monsoon-path" d="M 900 450 C 800 450, 700 400, 600 350 C 500 300, 400 350, 300 400"></path>
            </defs>
            <!-- Layers for different elements -->
            <g id="monsoon-layer"></g>
            <g id="routes-layer"></g>
            <g id="cities-layer"></g>
        </svg>
        <div id="info-panel" class="info-panel hidden">
            <h3 class="info-title"></h3>
            <p class="info-text"></p>
        </div>
    </div>
    <div id="controls-panel">
        <div class="control-group">
            <label for="period-slider">בחר תקופה:</label>
            <input type="range" id="period-slider" min="0" max="3" value="0" step="1">
            <span id="current-period-label">תקופה עתיקה (3000 לפנה"ס - 300 לספירה)</span>
        </div>
        <div class="control-group">
            <label for="monsoon-select">כיוון מונסון (למסע):</label>
            <select id="monsoon-select">
                <option value="summer">מונסון קיץ (מזרחה)</option>
                <option value="winter">מונסון חורף (מערבה)</option>
            </select>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג הסבר מורחב</button>

<div id="explanation" class="explanation-content hidden">
    <h2>הסבר מורחב: פעימות הלב של הסחר באוקיינוס ההודי</h2>
    <p>האוקיינוס ההודי, נרחב ככל שיהיה, לא שימש כמחסום, אלא ככביש מהיר ימי שוקק חיים. במשך אלפי שנים, הוא חיבר בין עמים וציוויליזציות מאסיה, אפריקה והמזרח התיכון, יוצר קשרים כלכליים, חברתיים ותרבותיים עמוקים שעיצבו את העולם הרבה לפני עידן הקולוניאליזם האירופאי.</p>

    <h3>סוד המונסון: הרוח שמניעה עולמות</h3>
    <p>הקסם והיעילות של הסחר באוקיינוס ההודי טמונים ביכולת לרתום את כוחן של רוחות המונסון. רוחות אלו משנות את כיוונן בגלל שינויי טמפרטורה בין היבשה לים: בקיץ (מאי-ספטמבר), כשהיבשה חמה יותר, הרוחות נושבות מהים הקריר יחסית לכיוון היבשה – מדרום-מערב לכיוון הודו ודרום מזרח אסיה. בחורף (אוקטובר-אפריל), כשהים חם יותר, הרוחות מתהפכות ונושבות מצפון-מזרח לכיוון הים האדום ומזרח אפריקה. ספנים מנוסים ידעו לנצל את המחזוריות הקבועה הזו לתכנון מסעות הלוך ושוב, להגיע ליעדם עם רוח גבית ולחזור כשהרוח מתהפכת. זו הייתה מערכת ניווט טבעית ואמינה.</p>

    <h3>מסע בזמן: נתיבים, שחקנים וסחורות לאורך ההיסטוריה</h3>
    <p>רשת הסחר התפתחה והשתנתה עם עלייתן ושקיעתן של אימפריות ותרבויות:</p>
    <ul>
        <li>**תקופה עתיקה (3000 לפנה"ס - 300 לספירה):** ניצני הסחר הראשונים, קשרים בין עמק האינדוס למסופוטמיה, סחר יוקרתי של מצרים עם ארץ פונט (מזרח אפריקה). עם עליית רומא, הביקוש לסחורות מזרחיות גבר, מה שהאיץ את התנועה בים האדום ובין הודו לאימפריה הרומית.</li>
        <li>**ימי הביניים המוקדמים (300 - 1000 לספירה):** פריחה אדירה בהובלת סוחרים הודים, פרסים (האימפריה הסאסאנית) וערבים. עליית האסלאם סיפקה מסגרת מאוחדת לאזור רחב והגבירה את הסחר. מרכזים כמו בצרה, סיראף, עדן וערים בהודו ודרום מזרח אסיה שגשגו.</li>
        <li>**ימי הביניים המאוחרים (1000 - 1500 לספירה):** תור הזהב של הסחר. סוחרים ערבים ופרסים המשיכו להיות הדומיננטיים, אך הצטרפו שחקנים חדשים כמו סין (מסעותיו האדירים של ג'נג חה במאה ה-15), סוחרי גוג'אראט וטמיל בהודו, וממלכות ימיות בדרום מזרח אסיה ששלטו על מצרי מלאקה. זהו שיאה של רשת הסחר לפני הגעת האירופאים.</li>
        <li>**העת החדשה המוקדמת (1500 - 1700 לספירה):** עידן חדש עם הגעת הפורטוגזים, ההולנדים, הבריטים והצרפתים שניסו להשתלט על נתיבי הסחר. הם הקימו עמדות מסחר מבוצרות וחברות ענק (כמו חברת הודו המזרחית). למרות זאת, רשתות הסחר האסייתיות המשיכו לפעול, לעיתים בשיתוף פעולה ולעיתים בעימות עם הכוחות האירופאים. המערכת הפכה מורכבת ותחרותית יותר.</li>
    </ul>

    <h3>אוצרות הים: מה עבר בנתיבים?</h3>
    <p>המגוון היה עצום: תבלינים (פלפל, קינמון, ציפורן, מוסקט) היו המטען היוקרתי ביותר והמניע העיקרי של הסחר עם אירופה והמזרח התיכון. טקסטיל הודי (כותנה, קטיפה, משי), חרסינה מסין, זהב ואבנים יקרות מאפריקה והודו, שנהב, עבדים, בושם, מור, קטורת, מוצרי עץ יקרים, ואפילו מזון – חיטה, אורז ושמן. אך לא רק חפצים: ידע טכנולוגי (ניווט, בניית ספינות), דתות (בודהיזם, הינדואיזם, אסלאם), שפות ורעיונות פילוסופיים עברו גם הם בנתיבים אלו, ויצרו אזור המושפע הדדית.</p>

    <h3>ערי נמל קוסמופוליטיות: לב הפעילות</h3>
    <p>לאורך חופי האוקיינוס קמו ושגשגו ערי נמל שהיו יותר מסתם תחנות עגינה – הן היו מרכזים כלכליים, תרבותיים ומדעיים. ערים כמו אלכסנדריה, עדן, הורמוז, קאליקוט, סוראט, גואה, קילווה, מוגדישו, מלאקה וגואנגג'ואו משכו סוחרים, ימאים ומלומדים מכל רחבי העולם הידוע. בערים אלו נפגשו שפות, מנהגים, דתות ורעיונות, ויצרו חברות רב-תרבותיות תוססות.</p>

    <h3>טכנולוגיה וידע: כלים למסע</h3>
    <p>המסחר באוקיינוס הפתוח דרש טכנולוגיות ניווט ובניית ספינות מתקדמות. ספינות ה"דאו" הערביות, עם המפרש המשולש הייחודי שלהן, וה"ג'ונקה" הסינית, הגדולות והחזקות יותר, היו מותאמות למים העמוקים ולניצול רוחות המונסון. ידע אסטרונומי לניווט לילי, שימוש באצטרולבים ובמצפן (שהגיע מסין), ומפות ימיות מדויקות היו חיוניים להצלחה ולבטיחות המסעות הארוכים.</p>

    <h3>מורשת עולמית: יצירת רשת עולמית מוקדמת</h3>
    <p>נתיבי הסחר באוקיינוס ההודי היוו אבן יסוד למערכת כלכלית עולמית עוד לפני שאירופה הפכה לכוח דומיננטי. הם לא רק העבירו סחורות, אלא גם יצרו קשרים עמוקים בין תרבויות, תרמו להפצת דתות וידע, והניחו את היסודות לרשתות הגלובליות של ימינו. הבנת ההיסטוריה המפוארת של האוקיינוס ההודי כמרכז עולמי עוזרת לנו לראות את ההיסטוריה הגלובלית באור רחב ומחובר יותר.</p>
</div>

<style>
/* כללי */
#app-container {
    direction: rtl; /* Hebrew support */
    font-family: 'Arial', sans-serif;
    max-width: 1000px;
    margin: 20px auto;
    border: 1px solid #ddd;
    border-radius: 12px;
    overflow: hidden;
    background-color: #eef; /* Light blue background hinting at water */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

#map-container {
    position: relative;
    width: 100%;
    background-color: #aed6f1; /* A slightly darker blue for the ocean areas not covered by image */
}

#indian-ocean-map {
    display: block;
    width: 100%;
    height: auto;
}

#indian-ocean-map image {
     opacity: 0.8; /* Make map slightly transparent to see layers better */
}


/* שכבות SVG */
#routes-layer path {
    fill: none;
    stroke: #e67e22; /* Earthy orange for routes */
    stroke-width: 2.5;
    opacity: 0.8;
    transition: stroke-width 0.3s ease-in-out, opacity 0.3s ease-in-out, stroke-dashoffset 5s linear; /* Added transition for animation */
    cursor: pointer;
    stroke-dasharray: 1000; /* For dash animation */
    stroke-dashoffset: 1000; /* Start dashed off */
}

#routes-layer path:hover {
    stroke-width: 4;
    opacity: 1;
    stroke: #d35400; /* Darker orange on hover */
}

/* Highlight active route */
#routes-layer path.active-route {
    stroke-width: 5;
    opacity: 1;
    stroke: #d35400;
     animation: draw 2s ease-in-out forwards; /* Animation on activation */
}

@keyframes draw {
    to {
        stroke-dashoffset: 0;
    }
}


#cities-layer circle {
    fill: #3498db; /* Blue for cities */
    stroke: #fff;
    stroke-width: 1.5;
    r: 6; /* Radius */
    cursor: pointer;
    transition: r 0.2s ease-in-out, fill 0.2s ease-in-out;
    filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.3)); /* Add shadow */
}

#cities-layer circle:hover {
    r: 9;
    fill: #2980b9; /* Darker blue on hover */
}

/* Highlight active city */
#cities-layer circle.active-city {
     r: 10;
     fill: #c0392b; /* Red for active city */
     stroke: #fff;
     stroke-width: 2;
     animation: pulse 1.5s infinite ease-in-out; /* Add pulse animation */
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}


/* Monsoon Arrows (Static representation for now, animation added via JS) */
#monsoon-layer path {
    stroke: #2ecc71; /* Green for winds */
    stroke-width: 3;
    opacity: 0.7;
    marker-end: url(#arrowhead); /* Use defined arrowhead marker */
    transition: opacity 0.3s ease-in-out;
}

#monsoon-layer path:hover {
    opacity: 1;
    stroke: #27ae60; /* Darker green on hover */
}

/* Styling for the animated dots (handled in JS) */
.monsoon-dot {
    fill: #4CAF50; /* Green color for dots */
    r: 3; /* Radius of the dot */
    opacity: 0.9;
    filter: drop-shadow(0 0 3px rgba(0,0,0,0.5));
}


/* Info Panel */
.info-panel {
    position: absolute;
    top: 15px;
    right: 15px;
    background-color: rgba(255, 255, 255, 0.95); /* Slightly more opaque */
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 15px;
    max-width: 280px; /* Slightly wider */
    z-index: 10;
    box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
    transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
    transform: translateY(10px); /* Start slightly lower for animation */
}

.info-panel.hidden {
    opacity: 0;
    pointer-events: none; /* Allow clicks on elements behind it when hidden */
    transform: translateY(0);
}

.info-title {
    margin-top: 0;
    font-size: 1.2em;
    color: #333;
    border-bottom: 2px solid #eee;
    padding-bottom: 8px;
    margin-bottom: 10px;
}

.info-text {
    margin-bottom: 0;
    font-size: 0.95em;
    line-height: 1.5;
    color: #555;
}


/* Controls Panel */
#controls-panel {
    padding: 15px;
    background-color: #f0f4f8; /* Light grey-blue */
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    border-top: 1px solid #ddd;
}

.control-group {
    margin: 8px 15px; /* Increased margin */
    display: flex;
    align-items: center;
    background-color: #fff; /* White background for groups */
    padding: 8px 15px;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

.control-group label {
    margin-left: 10px; /* Increased margin */
    font-weight: bold;
    color: #555;
    white-space: nowrap; /* Prevent wrapping */
}

#period-slider {
    flex-grow: 1;
    min-width: 150px; /* Ensure slider has enough space */
    margin-right: 10px;
}

#current-period-label {
    font-weight: bold;
    min-width: 200px; /* Keep label width consistent */
    text-align: right;
    color: #333;
}

#monsoon-select {
    padding: 5px 8px;
    border-radius: 4px;
    border: 1px solid #ccc;
    font-size: 1em;
    cursor: pointer;
}


/* Explanation Section */
.toggle-button {
    display: block;
    margin: 25px auto; /* Increased margin */
    padding: 12px 25px; /* Increased padding */
    font-size: 1.1em; /* Slightly larger font */
    cursor: pointer;
    border: none; /* Remove default border */
    border-radius: 6px;
    background-color: #3498db; /* Blue button */
    color: white;
    transition: background-color 0.3s ease-in-out, box-shadow 0.2s ease-in-out;
    box-shadow: 0 2px 5px rgba(0,0,0,0.15);
}

.toggle-button:hover {
    background-color: #2980b9; /* Darker blue on hover */
    box-shadow: 0 3px 7px rgba(0,0,0,0.2);
}

.explanation-content {
    max-width: 1000px;
    margin: 20px auto;
    padding: 25px; /* Increased padding */
    border: 1px solid #ddd;
    border-radius: 12px;
    background-color: #fff;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    line-height: 1.7; /* Improved readability */
    color: #333;
}

.explanation-content h2 {
    text-align: center;
    color: #2c3e50; /* Dark blue-grey */
    margin-top: 0;
    margin-bottom: 25px;
    font-size: 1.8em;
}

.explanation-content h3 {
    color: #3498db; /* Blue headers */
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 1.3em;
}

.explanation-content p, .explanation-content ul {
    margin-bottom: 18px;
    text-align: justify;
}

.explanation-content ul {
    padding-right: 30px;
    list-style: disc outside; /* Use discs for list items */
}

.explanation-content li {
    margin-bottom: 10px;
}

/* Utilities */
.hidden {
    display: none;
}

/* Basic responsiveness */
@media (max-width: 768px) {
    #app-container, .explanation-content {
        margin: 10px;
        border-radius: 8px;
    }

    #controls-panel {
        flex-direction: column;
        align-items: stretch;
    }
    .control-group {
        flex-direction: column;
        align-items: flex-start;
        margin: 5px 0;
        padding: 10px;
    }
    .control-group label {
        margin-bottom: 5px;
        margin-left: 0;
    }
    #period-slider {
        width: 100%;
        min-width: auto;
        margin-right: 0;
    }
    #current-period-label {
        width: 100%;
        text-align: right;
        margin-top: 8px;
    }
    #monsoon-select {
         width: 100%;
         margin-top: 5px;
     }

    .info-panel {
        max-width: 95%;
        left: 2.5%;
        right: 2.5%;
        top: 10px;
        padding: 10px;
    }
     .info-title {
         font-size: 1.1em;
         padding-bottom: 5px;
         margin-bottom: 5px;
     }
     .info-text {
         font-size: 0.9em;
     }

     .toggle-button {
         padding: 10px 20px;
         font-size: 1em;
         margin: 15px auto;
     }

    .explanation-content {
        padding: 15px;
    }
     .explanation-content h2 {
         font-size: 1.5em;
         margin-bottom: 15px;
     }
     .explanation-content h3 {
         font-size: 1.2em;
         margin-top: 15px;
     }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const mapSvg = document.getElementById('indian-ocean-map');
    const routesLayer = document.getElementById('routes-layer');
    const citiesLayer = document.getElementById('cities-layer');
    const monsoonLayer = document.getElementById('monsoon-layer');
    const infoPanel = document.getElementById('info-panel');
    const infoTitle = infoPanel.querySelector('.info-title');
    const infoText = infoPanel.querySelector('.info-text');
    const periodSlider = document.getElementById('period-slider');
    const currentPeriodLabel = document.getElementById('current-period-label');
    const monsoonSelect = document.getElementById('monsoon-select');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Geographic data - simplified coordinates for demonstration
    // Coordinates are relative to the SVG viewBox (0-1000, 0-600)
    const cities = {
        alexandria: { name: 'אלכסנדריה (מצרים)', coords: { x: 150, y: 180 }, info: 'מרכז סחר רומי, ביזנטי וערבי מרכזי, שער ימי לאירופה וים התיכון. נקודת קצה מערבית לנתיב הים האדום.' },
        aden: { name: 'עדן (תימן)', coords: { x: 300, y: 350 }, info: 'נמל מפתח בחצי האי ערב, נקודת מפגש ופיצול אסטרטגית לנתיבים מהים האדום והמפרץ הפרסי לכיוון הודו ואפריקה.' },
        hormuz: { name: 'הורמוז (מפרץ פרסי)', coords: { x: 420, y: 250 }, info: 'אי ושער הכניסה למפרץ הפרסי, מרכז לסחר פרסי וערבי. חיברה את הסחר עם מסופוטמיה ופרס.' },
        calicut: { name: 'קאליקוט (הודו)', coords: { x: 600, y: 380 }, info: 'עיר נמל שגשגת בחוף מלבר בהודו, ידועה בתבלינים (במיוחד פלפל). יעד מרכזי לספינות מונסון מזרחיות.' },
        malacca: { name: 'מלאקה (מלזיה)', coords: { x: 850, y: 450 }, info: 'שולטת על המצרים האסטרטגיים בעלי השם הזהה, המחברים את האוקיינוס ההודי לים סין הדרומי. מרכז סחר רב-לאומי.' },
        zeila: { name: 'זיילה (סומליה)', coords: { x: 250, y: 350 }, info: 'נמל חשוב בקרן אפריקה, מרכז לסחר זהב, שנהב, עבדים ומור. קשר עם הים האדום וחצי האי ערב.' },
        muscat: { name: 'מוסקט (עומאן)', coords: { x: 450, y: 300 }, info: 'נמל חשוב בעומאן, קשר בין המפרץ הפרסי והחוף המזרחי של אפריקה/הודו. ידועה בסחר קטורת וסחורות מערביות.' },
        surat: { name: 'סוראט (הודו)', coords: { x: 550, y: 280 }, info: 'נמל גדול בחוף המערבי של הודו (גוג\'אראט), מרכז ענק לסחר טקסטיל, תבלינים וסחורות נוספות. שער כניסה לצפון הודו.' },
        goa: { name: 'גואה (הודו)', coords: { x: 580, y: 350 }, info: 'נמל חשוב בחוף המערבי של הודו. מאוחר יותר הפך לבסיס פורטוגזי מרכזי במאה ה-16.' },
        palembang: { name: 'פלמבאנג (אינדונזיה)', coords: { x: 900, y: 500 }, info: 'מרכז ממלכת סריוויג\'איה בסומטרה, ששלטה על נתיבי הסחר הימיים החשובים באזור המצרים לפני עליית מלאקה.' },
        guangzhou: { name: 'גואנגג\'ואו (סין)', coords: { x: 950, y: 300 }, info: 'נמל סיני מרכזי לאורך ההיסטוריה, שער הכניסה לסחורות הסיניות היקרות כמו משי, חרסינה ותה.' },
        kilwa: { name: 'קילווה (טנזניה)', coords: { x: 400, y: 500 }, info: 'עיר מדינה סווהילית שגשגת בחוף מזרח אפריקה, מרכז לסחר זהב מזימבבואה ואבני חן. שיא פריחתה בימי הביניים המאוחרים.' },
        mogadishu: { name: 'מוגדישו (סומליה)', coords: { x: 350, y: 450 }, info: 'עיר נמל חשובה בחוף מזרח אפריקה, חלק מרשת ערי המדינה הסווהיליות. קשר עם הים האדום, המפרץ הפרסי והודו.' },
         indus_valley: { name: 'עמק האינדוס (אזור)', coords: { x: 500, y: 200 }, info: 'אחד ממרכזי הציוויליזציה הראשונים בעולם עם קשרים ימיים מוקדמים (כמו לדילמון ומסופוטמיה) כבר באלף ה-3 לפנה"ס.' },
         rhapta: { name: 'רפטא (מזרח אפריקה)', coords: { x: 400, y: 550 }, info: 'נמל קדום חשוב בחוף מזרח אפריקה, מוזכר במקורות רומיים כמרכז לסחר עם האימפריה. מיקומו המדויק עדיין נתון לוויכוח מחקרי.' }
    };

    // Define major routes with start/end city keys and sample path coordinates
    // Path coordinates are simplified control points for curves (x1, y1 x2, y2 x, y)
    const routes = {
        red_sea_india: { name: 'ים סוף - הודו', periods: [0, 1, 2, 3], path: 'M 170 180 C 200 250, 250 300, 300 350 C 350 400, 450 450, 600 380', info: 'נתיב עיקרי בין הים התיכון (דרך אלכסנדריה וים סוף) להודו (קאליקוט). נשלט בתקופות שונות ע"י רומאים, ערבים ואירופאים.' },
        gulf_india: { name: 'המפרץ הערבי - הודו', periods: [0, 1, 2, 3], path: 'M 420 250 C 500 300, 550 350, 600 380', info: 'נתיב חשוב בין המפרץ הפרסי (הורמוז) להודו (סוראט/קאליקוט). מרכז לסחר פרסי וערבי.' },
        e_africa_red_sea_gulf: { name: 'מזרח אפריקה - ים סוף/מפרץ', periods: [0, 1, 2], path: 'M 400 550 C 350 480, 300 400, 300 350 C 300 300, 350 280, 420 250', info: 'חיבור בין ערי החוף המשגשגות של מזרח אפריקה (קילווה, מוגדישו, זיילה) לים האדום (עדן) והמפרץ הפרסי (הורמוז).' },
         india_se_asia: { name: 'הודו - דרום מזרח אסיה', periods: [1, 2, 3], path: 'M 600 380 C 700 450, 800 500, 850 450', info: 'מסלול חיוני בין הודו (קאליקוט, גואה) למרכזים בדרום מזרח אסיה (מלאקה, פלמבאנג) דרך מפרץ בנגל. שער הכניסה למזרח הרחוק.' },
         se_asia_china: { name: 'דרום מזרח אסיה - סין', periods: [1, 2, 3], path: 'M 850 450 C 900 400, 920 350, 950 300', info: 'המשך הנתיב מזרחה ממרכזי הסחר בדרום מזרח אסיה (מלאקה) לסין (גואנגג\'ואו) דרך ים סין הדרומי. נתיב המשי הימי.' },
         indus_gulf: { name: 'עמק האינדוס - המפרץ', periods: [0], path: 'M 500 200 C 480 230, 450 240, 420 250', info: 'קשרים ימיים עתיקים מאוד (החל מהאלף ה-3 לפנה"ס) בין הציוויליזציה בעמק האינדוס למסופוטמיה דרך המפרץ הפרסי.' }
    };

    const periods = [
        { label: 'תקופה עתיקה (3000 לפנה"ס - 300 לספירה)', key: 0, cities: ['alexandria', 'aden', 'hormuz', 'indus_valley', 'zeila', 'rhapta'], routes: ['red_sea_india', 'gulf_india', 'e_africa_red_sea_gulf', 'indus_gulf'] },
        { label: 'ימי הביניים המוקדמים (300 - 1000 לספירה)', key: 1, cities: ['alexandria', 'aden', 'hormuz', 'calicut', 'malacca', 'zeila', 'muscat', 'surat', 'palembang', 'guangzhou', 'kilwa', 'mogadishu'], routes: ['red_sea_india', 'gulf_india', 'e_africa_red_sea_gulf', 'india_se_asia', 'se_asia_china'] },
        { label: 'ימי הביניים המאוחרים (1000 - 1500 לספירה)', key: 2, cities: ['alexandria', 'aden', 'hormuz', 'calicut', 'malacca', 'zeila', 'muscat', 'surat', 'goa', 'palembang', 'guangzhou', 'kilwa', 'mogadishu'], routes: ['red_sea_india', 'gulf_india', 'e_africa_red_sea_gulf', 'india_se_asia', 'se_asia_china'] },
        { label: 'העת החדשה המוקדמת (1500 - 1700 לספירה)', key: 3, cities: ['alexandria', 'aden', 'hormuz', 'calicut', 'malacca', 'muscat', 'surat', 'goa', 'guangzhou', 'kilwa'], routes: ['red_sea_india', 'gulf_india', 'india_se_asia', 'se_asia_china'] }
    ];

    // Keep track of animated dots
    let monsoonDots = [];
    let currentMonsoonDirection = monsoonSelect.value;
    let currentPeriodIndex = parseInt(periodSlider.value);


    function renderMap(periodIndex, monsoonDirection) {
        const currentPeriod = periods[periodIndex];
        currentPeriodLabel.textContent = currentPeriod.label;

        // Clear previous elements and animations
        routesLayer.innerHTML = '';
        citiesLayer.innerHTML = '';
        monsoonLayer.innerHTML = '';
        monsoonDots.forEach(dot => dot.remove()); // Remove previous animated dots
        monsoonDots = []; // Clear the array
        hideInfo(); // Hide info panel on map change

        currentMonsoonDirection = monsoonDirection; // Update state
        currentPeriodIndex = periodIndex;

        // Draw routes for the current period
        Object.keys(routes).forEach(routeKey => {
            if (routes[routeKey].periods.includes(currentPeriod.key)) {
                const pathElem = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                pathElem.setAttribute('d', routes[routeKey].path);
                pathElem.setAttribute('data-info-type', 'route');
                pathElem.setAttribute('data-info-key', routeKey);
                routesLayer.appendChild(pathElem);
            }
        });

        // Draw cities for the current period
        currentPeriod.cities.forEach(cityKey => {
             if (cities[cityKey]) {
                const city = cities[cityKey];
                const circleElem = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                circleElem.setAttribute('cx', city.coords.x);
                circleElem.setAttribute('cy', city.coords.y);
                circleElem.setAttribute('r', 6); // Base radius
                circleElem.setAttribute('data-info-type', 'city');
                circleElem.setAttribute('data-info-key', cityKey);
                citiesLayer.appendChild(circleElem);

                // Optional: Add city names (can clutter the map)
                // const textElem = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                // textElem.setAttribute('x', city.coords.x);
                // textElem.setAttribute('y', city.coords.y);
                // textElem.textContent = city.name;
                // textElem.classList.add('city-label');
                // citiesLayer.appendChild(textElem);
            }
        });

         // Add click listeners to elements
        routesLayer.querySelectorAll('path').forEach(path => {
            path.addEventListener('click', handleElementClick);
        });
        citiesLayer.querySelectorAll('circle').forEach(circle => {
            circle.addEventListener('click', handleElementClick);
        });

        // Draw and animate monsoon arrows/dots
        drawMonsoon(monsoonDirection);

    }

    function drawMonsoon(direction) {
        const mainMonsoonPathId = direction === 'summer' ? 'summer-monsoon-path' : 'winter-monsoon-path';
        const mainPath = document.getElementById(mainMonsoonPathId);
        const mainPathD = mainPath.getAttribute('d'); // Use the defined path D

        // Draw a visible, clickable path for info
        const infoPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        infoPath.setAttribute('d', mainPathD);
        infoPath.setAttribute('data-info-type', 'monsoon');
        infoPath.setAttribute('data-info-key', direction);
        // Style the info path to be invisible or minimal, click target
        infoPath.setAttribute('stroke', 'transparent'); // Invisible stroke
        infoPath.setAttribute('stroke-width', '20'); // Large click area
        infoPath.setAttribute('fill', 'none');
        infoPath.style.cursor = 'pointer';
        monsoonLayer.appendChild(infoPath);

         // Add listener to the info path
        infoPath.addEventListener('click', handleElementClick);


        // Create and animate multiple dots along the main path
        const numDots = 8; // Number of dots to animate
        const duration = 8; // Animation duration in seconds

        for (let i = 0; i < numDots; i++) {
            const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            dot.classList.add('monsoon-dot'); // Apply CSS styling
            monsoonLayer.appendChild(dot); // Append to the monsoon layer

            const animateMotion = document.createElementNS('http://www.w3.org/2000/svg', 'animateMotion');
            animateMotion.setAttribute('dur', `${duration}s`);
            animateMotion.setAttribute('repeatCount', 'indefinite');
            // Offset the start time for each dot
            animateMotion.setAttribute('begin', `${-duration / numDots * i}s`);

            const mpath = document.createElementNS('http://www.w3.org/2000/svg', 'mpath');
            mpath.setAttribute('href', `#${mainMonsoonPathId}`);
            animateMotion.appendChild(mpath);

            dot.appendChild(animateMotion);
            monsoonDots.push(dot); // Store dot element to remove later
        }
    }


    function handleElementClick(event) {
        // Clear previous active states
        routesLayer.querySelectorAll('path').forEach(path => path.classList.remove('active-route'));
        citiesLayer.querySelectorAll('circle').forEach(circle => circle.classList.remove('active-city'));

        const target = event.target;
        const type = target.getAttribute('data-info-type');
        const key = target.getAttribute('data-info-key');
        let data;

        if (type === 'route') {
            data = routes[key];
            infoTitle.textContent = `נתיב: ${data.name}`;
            infoText.textContent = data.info;
            target.classList.add('active-route'); // Highlight the route
            // Restart route drawing animation on click
             target.style.strokeDashoffset = 1000;
             target.style.animation = 'none'; // Reset animation
             void target.offsetWidth; // Trigger reflow
             target.style.animation = 'draw 2s ease-in-out forwards'; // Restart animation

        } else if (type === 'city') {
            data = cities[key];
            infoTitle.textContent = `עיר: ${data.name}`;
            infoText.textContent = data.info;
            target.classList.add('active-city'); // Highlight the city
        } else if (type === 'monsoon') {
             // Info for monsoon comes from a hardcoded description
             const monsoonInfo = direction === 'summer'
                ? 'רוחות מונסון קיץ (מאי-ספטמבר) נושבות מדרום-מערב, מאפשרות מסע מהים האדום/אפריקה לכיוון הודו ודרום מזרח אסיה.'
                : 'רוחות מונסון חורף (אוקטובר-אפריל) נושבות מצפון-מזרח, מאפשרות מסע מהודו ודרום מזרח אסיה לכיוון הים האדום ומזרח אפריקה.';
             infoTitle.textContent = `רוחות מונסון (${key === 'summer' ? 'קיץ' : 'חורף'})`;
             infoText.textContent = monsoonInfo;
         }

        showInfo();
    }

    function showInfo() {
        infoPanel.classList.remove('hidden');
    }

    function hideInfo() {
        infoPanel.classList.add('hidden');
        // Clear info content slightly delayed to allow fade-out
        setTimeout(() => {
             infoTitle.textContent = '';
             infoText.textContent = '';
             // Also clear active states when hiding info
             routesLayer.querySelectorAll('path').forEach(path => path.classList.remove('active-route'));
             citiesLayer.querySelectorAll('circle').forEach(circle => circle.classList.remove('active-city'));
        }, 300); // Match CSS transition duration
    }

    // Event listeners for controls
    periodSlider.addEventListener('input', (event) => {
        const periodIndex = parseInt(event.target.value);
        renderMap(periodIndex, currentMonsoonDirection); // Use current monsoon direction
    });

    monsoonSelect.addEventListener('change', (event) => {
        const monsoonDirection = event.target.value;
        renderMap(currentPeriodIndex, monsoonDirection); // Use current period index
    });

    toggleExplanationBtn.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (explanationDiv.classList.contains('hidden')) {
             toggleExplanationBtn.textContent = 'הצג הסבר מורחב';
         } else {
             toggleExplanationBtn.textContent = 'הסתר הסבר מורחב';
         }
         // Scroll to explanation if showing it
         if (!explanationDiv.classList.contains('hidden')) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });


    // Initial render
    renderMap(currentPeriodIndex, currentMonsoonDirection);
    toggleExplanationBtn.textContent = 'הצג הסבר מורחב'; // Set initial button text


    // Close info panel when clicking on the map background itself
    mapSvg.addEventListener('click', (event) => {
        // Check if the click target is the SVG itself, not one of its children
        if (event.target === mapSvg) {
            hideInfo();
        }
    });

    // Allow clicking on layers that don't have data-info-type to hide panel
    monsoonLayer.addEventListener('click', (event) => {
        if (!event.target.closest('[data-info-type="monsoon"]')) {
             hideInfo();
        }
    });
     routesLayer.addEventListener('click', (event) => {
        if (!event.target.closest('[data-info-type="route"]')) {
             hideInfo();
        }
    });
     citiesLayer.addEventListener('click', (event) => {
         if (!event.target.closest('[data-info-type="city"]')) {
              hideInfo();
         }
     });

});
</script>
```