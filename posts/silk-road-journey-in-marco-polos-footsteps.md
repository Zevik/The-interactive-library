---
title: "מסע על דרך המשי: בעקבות מרקו פולו"
english_slug: silk-road-journey-in-marco-polos-footsteps
category: "ארכאולוגיה"
tags: היסטוריה, גאוגרפיה, דרך המשי, ימי הביניים, מסעות, מרקו פולו
---
# מסע על דרך המשי: בעקבות מרקו פולו

דמיינו עולם ללא מטוסים, רכבות או אינטרנט. כיצד העז אדם לצאת למסע חובק עולם, בין תרבויות שונות ומרוחקות, דרך נופים מסוכנים ולא נודעים? הצטרפו למסע המרתק והמסוכן ביותר של ימי הביניים. האם תצליחו להגיע בחזית אחת לחצר קובלאי חאן ולהפוך לסוחרים עשירים ומפורסמים?

<div id="game-container">
    <div id="map-area">
        <div id="current-location" class="location current pulse">ונציה</div>
         <div id="map-connector"></div> <!-- Visual connector -->
        <div id="destinations">
            <!-- Destinations will be added here -->
        </div>
         <div id="travel-progress" class="hidden">
             <div id="progress-bar"></div>
         </div>
    </div>
    <div id="status-area">
        <h2>סטטוס המשלחת:</h2>
        <div class="status-row"><span class="status-label">מיקום נוכחי:</span> <span id="status-location" class="status-value">ונציה</span></div>
        <div class="status-row"><span class="status-label">ממון בקופה:</span> $<span id="status-money" class="status-value">2000</span></div>
        <div class="status-row"><span class="status-label">טובין במלאי:</span> <span id="status-inventory" class="status-value inventory-items"></span></div>
        <div class="status-row"><span class="status-label">ימים במסע:</span> <span id="status-days" class="status-value">0</span></div>
    </div>
    <div id="decision-area">
        <h2>מה עושים עכשיו?</h2>
        <div id="choices">
            <!-- Choices will be added here -->
        </div>
        <div id="event-log">
            <div class="log-title">יומן מסע:</div>
            <!-- Events and messages will be added here -->
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Alef:wght@400;700&family=Frank+Ruhl+Libre:wght@400;700&display=swap');

    #game-container {
        display: flex;
        flex-direction: column;
        font-family: 'Alef', sans-serif;
        border: 1px solid #a08a7b; /* Earthy, historical feel */
        padding: 20px;
        border-radius: 12px;
        max-width: 800px;
        margin: 20px auto;
        background-color: #fefdfb; /* Off-white, parchment-like */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }

    h1, h2 {
        font-family: 'Frank Ruhl Libre', serif;
        color: #4a3b31; /* Darker earthy tone */
    }

    h1 {
        text-align: center;
        margin-bottom: 10px;
    }

    #map-area {
        position: relative;
        height: 120px; /* Increased height for better visualization */
        border-bottom: 2px solid #d3c7b8;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        background: linear-gradient(to right, #e6e0d8, #f2eee9); /* Soft gradient */
        border-radius: 8px;
        padding: 10px 20px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
    }

    #map-connector {
         position: absolute;
         left: 0;
         right: 0;
         top: 50%;
         height: 2px;
         background-color: #d3c7b8;
         z-index: 0;
    }

     #current-location {
         position: relative; /* Needed for z-index */
         z-index: 2;
         transition: left 1s ease-in-out; /* Animation for movement */
     }

    .location {
        background-color: #ffffff;
        border: 2px solid #7b6a5c; /* Match earthy theme */
        padding: 8px 15px;
        border-radius: 20px; /* Pill shape */
        font-weight: bold;
        font-size: 0.9em;
        color: #4a3b31;
        white-space: nowrap; /* Prevent wrapping */
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        text-align: center;
    }

    #current-location {
         background-color: #a8d8a8; /* More vibrant green */
         border-color: #5a8b5a;
         color: #305a30;
    }

     .pulse {
         animation: pulse 1.5s infinite ease-in-out;
     }

     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.05); }
         100% { transform: scale(1); }
     }

     #destinations {
         display: flex;
         gap: 15px; /* Increased gap */
         align-items: center;
         z-index: 1; /* Above connector */
         position: relative;
     }

     #travel-progress {
        position: absolute;
        bottom: 5px;
        left: 20px;
        right: 20px;
        height: 8px;
        background-color: #d3c7b8;
        border-radius: 4px;
        overflow: hidden;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
     }

     #progress-bar {
         height: 100%;
         width: 0%;
         background-color: #5a8b5a; /* Matching current location green */
         transition: width 0.5s ease-out;
         border-radius: 4px;
     }

     .hidden {
         display: none;
     }


    #status-area, #decision-area {
        margin-bottom: 20px;
        padding: 15px;
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #d3c7b8;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    #status-area h2, #decision-area h2 {
        margin-top: 0;
        font-size: 1.3em;
        border-bottom: 2px solid #eee;
        padding-bottom: 8px;
        margin-bottom: 15px;
        color: #4a3b31;
    }

     .status-row {
         display: flex;
         justify-content: space-between;
         margin-bottom: 8px;
         line-height: 1.4;
     }

     .status-label {
         font-weight: bold;
         color: #5c4b40;
     }

     .status-value {
         color: #333;
     }

     .inventory-items {
         word-break: break-word; /* Allow breaking long inventory list */
         text-align: end;
         flex-grow: 1; /* Allow it to take space */
         padding-left: 10px; /* Space between label and value */
     }


    #choices button {
        display: block;
        width: 100%;
        padding: 12px;
        margin-bottom: 10px;
        border: none;
        background-color: #5cb85c; /* Original green, good for primary action */
        color: white;
        cursor: pointer;
        border-radius: 6px;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
    }

    #choices button:hover {
        background-color: #4cae4c;
         transform: translateY(-1px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

     #choices button:active {
         background-color: #419641;
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }

     #choices button:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
         box-shadow: none;
         transform: none;
     }

     #trade-options button { /* Style buy/sell buttons differently */
          background-color: #0275d8; /* Blueish for trade */
     }
     #trade-options button:hover {
         background-color: #025aa5;
     }

     #trade-options {
         margin-top: 10px;
     }
     #trade-options p {
         margin-bottom: 5px;
         font-weight: bold;
         color: #5c4b40;
     }

    #event-log {
        margin-top: 20px;
        padding: 15px;
        border: 1px dashed #d3c7b8;
        min-height: 80px;
        max-height: 180px;
        overflow-y: auto;
        background-color: #fff;
        border-radius: 8px;
        font-size: 0.95em;
        line-height: 1.5;
    }

    .log-title {
        font-weight: bold;
        margin-bottom: 10px;
        color: #4a3b31;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }


    #event-log p {
        margin-bottom: 8px;
        padding-bottom: 5px;
        border-bottom: 1px dotted #eee;
    }
     #event-log p:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }


    .event-message {
        color: #333; /* Standard message */
    }

    .event-success {
        color: #28a745; /* Green for success */
         font-weight: bold;
    }

    .event-fail {
        color: #dc3545; /* Red for failure */
         font-weight: bold;
    }

     .event-neutral {
         color: #ffc107; /* Orange/yellow for neutral/warning */
     }


    #game-over {
        text-align: center;
        margin-top: 25px;
        font-size: 1.8em;
        font-weight: bold;
        color: #dc3545; /* Bootstrap danger color */
         animation: shake 0.8s cubic-bezier(.36,.07,.19,.97) both;
         transform: translate3d(0, 0, 0);
         backface-visibility: hidden;
         perspective: 1000px;
    }
     @keyframes shake {
         10%, 90% { transform: translate3d(-1px, 0, 0); }
         20%, 80% { transform: translate3d(2px, 0, 0); }
         30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
         40%, 60% { transform: translate3d(4px, 0, 0); }
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto 20px auto; /* More space above */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #7b6a5c; /* Earthy button */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 3px 6px rgba(0,0,0,0.1);
    }

    #toggle-explanation:hover {
        background-color: #5c4b40;
         transform: translateY(-1px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

     #toggle-explanation:active {
          background-color: #4a3b31;
          transform: translateY(0);
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }


    #explanation {
        display: none; /* Hidden by default */
        border: 1px solid #a08a7b;
        padding: 20px;
        border-radius: 12px;
        max-width: 800px;
        margin: 20px auto;
        background-color: #fefdfb;
        line-height: 1.7;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
         color: #333;
         font-family: 'Alef', sans-serif;
    }

    #explanation h2 {
        color: #4a3b31;
        margin-top: 0; /* Adjusted margin */
        border-bottom: 2px solid #d3c7b8;
        padding-bottom: 8px;
         margin-bottom: 15px;
    }
     #explanation h3 {
        color: #5c4b40;
        margin-top: 20px;
        padding-bottom: 5px;
        border-bottom: 1px dotted #d3c7b8;
        margin-bottom: 10px;
     }

     #explanation p {
         margin-bottom: 15px;
     }

</style>

<button id="toggle-explanation">הצג הסבר על דרך המשי</button>

<div id="explanation">
    <h2>הסבר: מסע על דרך המשי: בעקבות מרקו פולו</h2>

    <p>מסע על דרך המשי היה הרפתקה של ממש, דורש אומץ, חוסן, ויכולת התמודדות עם אתגרים בלתי צפויים. הוא חיבר עולמות, תרבויות, וידע - והשפיע עמוקות על ההיסטוריה העולמית. הסימולציה הזו מאפשרת לכם לחוות קמצוץ מהקשיים וההזדמנויות שעמדו בפני סוחרים ומגלי ארצות כמו מרקו פולו.</p>

    <h3>מי היה מרקו פולו ומדוע מסעו היה יוצא דופן?</h3>
    <p>מרקו פולו (1254–1324) היה סוחר וחוקר ארצות ונציאני. הוא נודע בעיקר בזכות מסעו הארוך והמפורסם לאסיה, שהתחיל בשנת 1271 ונמשך 24 שנים. יחד עם אביו ניקולו ודודו מאפאו, הוא הגיע לחצר קובלאי חאן, שליט האימפריה המונגולית בסין. מסעו היה יוצא דופן לא רק בגלל אורכו הקיצוני באותה תקופה, אלא בעיקר בשל הספר "מסעות מרקו פולו" (Il Milione) שנכתב על ידי רוסטיקלו דה פיזה על סמך סיפוריו של מרקו בזמן שהיה בשבי בג'נובה. הספר תיאר בפני אירופים עולם רחוק ולא מוכר - תרבויות, מנהגים, בעלי חיים, צמחים וטכנולוגיות מדהימות מסין (המכונה בספר קאתאי), הודו ופרס. תיאורים אלו היו לעיתים כה פנטסטיים לאוזן האירופית עד שרבים הטילו בהם ספק, אך לימים הוכחו כנכונים בחלקם הגדול והשפיעו עמוקות על הידע הגיאוגרפי והתרבותי באירופה.</p>

    <h3>מהי דרך המשי? (היסטוריה, חשיבות, מסלולים מרכזיים)</h3>
    <p>דרך המשי לא הייתה דרך אחת סלולה, אלא רשת של דרכי מסחר יבשתיות וימיות שחיברו את מזרח אסיה (בעיקר סין) עם המזרח התיכון ואירופה. שמה ניתן לה בזכות המשי הסיני, שהיה אחד המוצרים היקרים והנחשקים ביותר שנסחרו לאורכה. הדרך פעלה באופן משמעותי מתקופת שושלת האן בסין (המאה ה-2 לפנה"ס) ועד המאה ה-15, כאשר עליית האימפריה העות'מאנית והחיפוש אחר נתיבי ים חדשים הובילו לירידת קרנה של הדרך היבשתית. חשיבותה הייתה עצומה: היא לא רק אפשרה מסחר בסחורות יוקרתיות כמו משי, תבלינים, נייר ואבני חן, אלא גם היוותה ערוץ מרכזי לחילופי ידע, טכנולוגיה, דתות (בודהיזם, נצרות, אסלאם), רעיונות ואפילו מחלות (כמו המוות השחור). מסלולים מרכזיים כללו נתיבים צפוניים (עוברים דרך הרי טיאן שאן), מרכזיים (עוברים דרך המדבריות של מרכז אסיה ופרס) ודרומיים (דרך הרי ההימלאיה והודו, לעיתים משולבים עם נתיבי ים).</p>

    <h3>אתגרי המסע על דרך המשי (גאוגרפיה, אקלים, סכנות, שפות ותרבויות שונות)</h3>
    <p>מסע על דרך המשי היה משימה קשה ומסוכנת מאין כמותה. האתגרים הגיאוגרפיים כללו חציית מדבריות עצומים (כמו מדבר טקלה מקאן ומדבר גובי) עם מחסור במים ומזון, מעבר בהרי ענק (הימלאיה, טיאן שאן) עם מזג אוויר קיצוני ודרכים מסוכנות, וחציית נהרות גדולים. האקלים לאורך הדרך השתנה מקצה לקצה, ממדבריות לוהטים בקיץ וקפואים בחורף, דרך פסגות מושלגות ויערות צפופים. סכנות אורבות בכל פינה: שודדים (שלקחו את הטובין ואף את החיים), מחלות קשות שהתפשטו במהירות (כמו הדבר), חיות טרף, ולעיתים גם סכנות פוליטיות או מלחמות בין ממלכות מקומיות. בנוסף, המסע הצריך התמודדות עם עשרות שפות ותרבויות שונות, מנהגים זרים, ובמקרים רבים גם דעות קדומות או עוינות מצד האוכלוסיות המקומיות. היכולת למצוא מדריכים נאמנים, להשיג ציוד מתאים ולהתנהל בחכמה במשא ומתן הייתה קריטית להישרדות והצלחה.</p>

    <h3>מסחר וחילופי ידע ותרבות לאורך הדרך</h3>
    <p>מעבר למשי, עברו בדרך המשי מגוון עצום של סחורות: תבלינים, בשמים, אבני חן, זכוכית, שנהב, צמר, זהב, כסף, עבדים, ובהמשך גם אבק שריפה ונייר מסין. המסחר התנהל לרוב בשיטת "מקטעים", כאשר סוחרים מקומיים העבירו סחורות רק לאורך חלק מסוים מהדרך ומכרו אותן לסוחרים אחרים. הערים הגדולות לאורך הדרך (כמו סמרקנד, בוכרה, בגדאד) הפכו למרכזי מסחר שוקקים ומרכזי תרבות בהם נפגשו אנשים מרחבי העולם. חילופי הידע היו לא פחות חשובים מהמסחר בסחורות. טכנולוגיות סיניות כמו ייצור נייר, הדפסה ואבק שריפה הגיעו למערב. מדע ופילוסופיה מהעולם המוסלמי הגיעו לאירופה. דתות כמו בודהיזם, נצרות נסטוריאנית ואסלאם התפשטו לאורך הדרך. סיפורים, אגדות וצורות אמנות עברו מיד ליד, והשפיעו על התרבויות השונות שבאו במגע. דרך המשי הייתה למעשה ציר גלובלי ראשון מסוגו של קשר ואינטראקציה בין תרבויות מזרח ומערב.</p>

    <h3>השפעת מסעות וספרים כמו 'מסעות מרקו פולו' על אירופה</h3>
    <p>ספרו של מרקו פולו, למרות הספקות הראשוניים, פתח צוהר עבור האירופים אל עולם לא נודע. הוא עורר סקרנות עצומה לגבי המזרח, עושרה, תרבויותיה ואפשרויות המסחר איתה. הספר תרם לגידול העניין בגיאוגרפיה ובמפות, סיפק מידע מעשי (גם אם לא תמיד מדויק) על מקומות רחוקים, והיווה השראה לחוקרים ומגלי ארצות עתידיים. יש הטוענים שאפילו כריסטופר קולומבוס החזיק עותק של הספר והושפע ממנו בחיפושיו אחר נתיב ימי למזרח. סיפורו של מרקו פולו הדגים את האפשרויות הגלומות במסעות ארוכי טווח, ואת הפוטנציאל הכלכלי והתרבותי הטמון בקשר עם תרבויות רחוקות. הוא תרם בעקיפין לתהליכים שהובילו לעידן התגליות הגדולות במאות הבאות.</p>
</div>


<script>
    const locations = {
        venice: { name: 'ונציה', goods: { silk: 100, spices: 80, gems: 150 }, routes: ['constantinople'] },
        constantinople: { name: 'קונסטנטינופול', goods: { silk: 120, spices: 90, gems: 140, textiles: 30 }, routes: ['antioch', 'trebizond'] },
        antioch: { name: 'אנטיוכיה', goods: { silk: 130, spices: 100, textiles: 40, glass: 50 }, routes: ['baghdad', 'palmyra'] },
        trebizond: { name: 'טרבזון', goods: { silk: 125, spices: 95, timber: 20 }, routes: ['tabriz'] },
        tabriz: { name: 'תבריז', goods: { silk: 140, spices: 110, carpets: 60, gems: 130 }, routes: ['samarkand', 'baghdad'] },
        palmyra: { name: 'תדמור', goods: { spices: 115, textiles: 45 }, routes: ['baghdad'] },
        baghdad: { name: 'בגדאד', goods: { silk: 150, spices: 120, gems: 120, books: 70 }, routes: ['tabriz', 'samarkand'] },
        samarkand: { name: 'סמרקנד', goods: { silk: 180, spices: 150, gems: 100, paper: 90 }, routes: ['bukhara', 'kashgar'] },
        bukhara: { name: 'בוכרה', goods: { silk: 170, spices: 140, cotton: 25 }, routes: ['samarkand', 'urgench'] },
        urgench: { name: 'אורגנץ\'', goods: { silk: 165, fish: 15 }, routes: ['astrakhan', 'bukhara'] },
        astrakhan: { name: 'אסטרחן', goods: { furs: 80, honey: 40 }, routes: [] }, // Dead end for this simple example route
        kashgar: { name: 'קאשגר', goods: { silk: 200, jade: 100, spices: 180 }, routes: ['yarkand', 'samarkand', 'khotan'] }, // Added Khotan route option
        yarkand: { name: 'יארקנד', goods: { silk: 210, jade: 110 }, routes: ['khotan', 'kashgar'] },
        khotan: { name: 'חוטאן', goods: { silk: 220, jade: 120, carpets: 70 }, routes: ['dunhuang', 'yarkand'] }, // Southern edge of Taklamakan
        dunhuang: { name: 'דונחואנג', goods: { silk: 250, spices: 220, buddhastatues: 80 }, routes: ['lanzhou', 'khotan'] }, // After crossing desert
        lanzhou: { name: 'לנג\'ואו', goods: { silk: 270, paper: 100, porcelain: 120 }, routes: ['xingqing', 'dunhuang'] }, // Entering China proper
        xingqing: { name: 'שינגצ\'ינג (נינגשיה)', goods: { silk: 300, paper: 110, porcelain: 130, tea: 50 }, routes: ['khanbaliq', 'lanzhou'] },
        khanbaliq: { name: 'חאנבליק (בייג\'ינג)', goods: { silk: 500, paper: 200, porcelain: 300, tea: 150, gunpowder: 250 }, routes: [] } // Destination
    };

     // Increased risks for specific routes for more challenge
    const routes = {
        constantinople: { name: 'לקונסטנטינופול (ים ואדמה)', days: 30, risk: 0.1, to: 'constantinople' },
        antioch: { name: 'לאנטיוכיה (דרך אסיה הקטנה)', days: 20, risk: 0.15, to: 'antioch' },
        palmyra: { name: 'לתדמור (דרך המדבר הסורי)', days: 15, risk: 0.25, to: 'palmyra', event: 'desert_travel' }, // Higher desert risk
        trebizond: { name: 'לטרבזון (דרך הים השחור)', days: 25, risk: 0.12, to: 'trebizond' },
        tabriz: { name: 'לתבריז (דרך פרס)', days: 35, risk: 0.2, to: 'tabriz' },
        baghdad: { name: 'לבגדאד (מרכז הסחר)', days: 30, risk: 0.18, to: 'baghdad' },
        samarkand: { name: 'לסמרקנד (לב המרכז אסיה)', days: 40, risk: 0.25, to: 'samarkand' },
        bukhara: { name: 'לבוכרה (עיר מדע)', days: 35, risk: 0.22, to: 'bukhara' },
        urgench: { name: 'לאורגנץ\' (דרך הצפון)', days: 40, risk: 0.23, to: 'urgench' },
        astrakhan: { name: 'לאסטרחן (נמל על וולגה)', days: 50, risk: 0.28, to: 'astrakhan' },
        kashgar: { name: 'לקאשגר (שער המדבר)', days: 50, risk: 0.3, to: 'kashgar', event: 'mountains_travel' }, // Crossing mountains to enter Tarim Basin
        yarkand: { name: 'ליארקנד (נאת מדבר)', days: 15, risk: 0.15, to: 'yarkand' },
        khotan: { name: 'חוטאן (על שפת טקלה מקאן)', days: 30, risk: 0.4, to: 'khotan', event: 'desert_travel' }, // Very high risk desert edge
        dunhuang: { name: 'לדונחואנג (עיר המערות)', days: 40, risk: 0.35, to: 'dunhuang', event: 'desert_travel' }, // Risk crossing desert/mountain edge
        lanzhou: { name: 'ללנג\'ואו (מעבר הנהר הצהוב)', days: 25, risk: 0.1, to: 'lanzhou' },
        xingqing: { name: 'לשינגצ\'ינג (ליד החומה הגדולה)', days: 20, risk: 0.08, to: 'xingqing' },
        khanbaliq: { name: 'לחאנבליק (בייג\'ינג, חצר החאן!)', days: 15, risk: 0.05, to: 'khanbaliq' } // Final stretch
    };

    const availableGoods = [
        { id: 'silk', name: 'משי', basePrice: 200 },
        { id: 'spices', name: 'תבלינים', basePrice: 100 },
        { id: 'gems', name: 'אבני חן', basePrice: 300 },
        { id: 'textiles', name: 'אריגים', basePrice: 50 },
        { id: 'glass', name: 'זכוכית ונציאנית', basePrice: 60 },
        { id: 'carpets', name: 'שטיחים פרסיים', basePrice: 120 },
        { id: 'timber', name: 'עץ משובח', basePrice: 30 },
        { id: 'books', name: 'כתבי יד יקרי ערך', basePrice: 150 },
        { id: 'paper', name: 'נייר סיני', basePrice: 180 },
        { id: 'cotton', name: 'כותנה', basePrice: 40 },
        { id: 'fish', name: 'דגים מומלחים', basePrice: 20 },
        { id: 'furs', name: 'פרוות יקרות', basePrice: 160 },
        { id: 'honey', name: 'דבש', basePrice: 70 },
        { id: 'jade', name: 'אבן ג\'ייד', basePrice: 200 },
        { id: 'buddhastatues', name: 'פסלי בודהה', basePrice: 150 },
        { id: 'porcelain', name: 'חרסינה סינית', basePrice: 250 },
        { id: 'tea', name: 'תה', basePrice: 100 },
        { id: 'gunpowder', name: 'אבק שריפה', basePrice: 300 }
    ];

    let gameState = {
        currentLocation: 'venice',
        money: 2000,
        inventory: {}, // { goodsId: quantity }
        days: 0
    };

    const statusLocation = document.getElementById('status-location');
    const statusMoney = document.getElementById('status-money');
    const statusInventory = document.getElementById('status-inventory');
    const statusDays = document.getElementById('status-days');
    const choicesDiv = document.getElementById('choices');
    const eventLogDiv = document.getElementById('event-log');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const mapArea = document.getElementById('map-area');
    const currentLocationMap = document.getElementById('current-location');
    const destinationsMap = document.getElementById('destinations');
    const travelProgressBar = document.getElementById('progress-bar');
    const travelProgressContainer = document.getElementById('travel-progress');

    function updateStatus() {
        statusLocation.textContent = locations[gameState.currentLocation].name;
        statusMoney.textContent = formatMoney(gameState.money);
        statusDays.textContent = gameState.days;

        let inventoryText = '';
        const inventoryItems = Object.entries(gameState.inventory).filter(([item, quantity]) => quantity > 0);

        if (inventoryItems.length > 0) {
             inventoryItems.forEach(([item, quantity], index) => {
                 const goodsName = availableGoods.find(g => g.id === item).name;
                 inventoryText += `${goodsName}: ${quantity}${index < inventoryItems.length - 1 ? ', ' : ''}`;
             });
        } else {
            inventoryText = 'אין טובין';
        }
        statusInventory.textContent = inventoryText;

        // Update map visualization
        currentLocationMap.textContent = locations[gameState.currentLocation].name;
        currentLocationMap.classList.add('pulse'); // Keep pulsing at location

        destinationsMap.innerHTML = '';
        const nextRoutes = locations[gameState.currentLocation].routes;
        if (nextRoutes.length > 0) {
             destinationsMap.style.display = 'flex';
             mapArea.style.justifyContent = 'space-between';
             nextRoutes.forEach(routeId => {
                 const route = routes[routeId];
                 const nextLocId = route.to;
                 const nextLoc = locations[nextLocId];
                 const destElement = document.createElement('div');
                 destElement.classList.add('location');
                 destElement.textContent = nextLoc.name;
                 destinationsMap.appendChild(destElement);
            });
        } else {
            destinationsMap.style.display = 'none';
            mapArea.style.justifyContent = 'center'; // Center current location if no routes
        }

         travelProgressContainer.classList.add('hidden'); // Hide progress bar when at a location
         travelProgressBar.style.width = '0%'; // Reset progress bar
    }

    function formatMoney(amount) {
         return new Intl.NumberFormat('en-US').format(amount); // Add commas for readability
    }

    function addMessage(message, type = 'event-message') {
        const p = document.createElement('p');
        p.textContent = message;
        p.classList.add(type);
        eventLogDiv.prepend(p); // Add to top
        // Optional: limit log length
        if (eventLogDiv.children.length > 30) { // Keep slightly more history
            eventLogDiv.removeChild(eventLogDiv.lastChild);
        }
        // Scroll to top of log if not already scrolling (optional)
        // eventLogDiv.scrollTop = 0;
    }

    function renderLocationChoices() {
        choicesDiv.innerHTML = ''; // Clear previous choices
        const currentLocation = locations[gameState.currentLocation];

        // Check for game over conditions FIRST
        if (gameState.money <= 0) {
             addMessage(`אזל כספך! אין באפשרותך לממן את המשך המסע או לרכוש ציוד. מסעך הסתיים כאן.`, 'event-fail');
             choicesDiv.innerHTML = '<div id="game-over">המסע הסתיים בפשיטת רגל.</div>';
             disableChoices();
             return;
        }

        if (gameState.currentLocation === 'khanbaliq') {
             addMessage(`הגעת לחאנבליק! חצר קובלאי חאן מקבלת את פניך. מסעך הארוך הסתיים בהצלחה לאחר ${gameState.days} ימים מרתקים!`, 'event-success');
             choicesDiv.innerHTML = '<div id="game-over">הגעת ליעד! המסע הסתיים בהצלחה.</div>';
             disableChoices();
             return;
        }


        // Option 1: Trade
        const tradeButton = document.createElement('button');
        tradeButton.textContent = `בצע מסחר ב${currentLocation.name}`;
        tradeButton.addEventListener('click', renderTradeChoices);
        choicesDiv.appendChild(tradeButton);

        // Option 2: Choose Route
         if (currentLocation.routes && currentLocation.routes.length > 0) {
            const routeButton = document.createElement('button');
            routeButton.textContent = 'בחר מסלול ליעד הבא';
            routeButton.addEventListener('click', renderRouteChoices);
            choicesDiv.appendChild(routeButton);
         } else {
             // If not Khanbaliq and no routes, it's a dead end
              addMessage(`המסע הגיע למבוי סתום ב${currentLocation.name}. אין נתיבים ידועים להמשיך מהם.`, 'event-fail');
               choicesDiv.innerHTML = '<div id="game-over">המסע הסתיים (מבוי סתום).</div>';
               disableChoices();
               return; // Prevent adding other buttons
         }

         // Ensure pulse animation is active when at a location
         currentLocationMap.classList.add('pulse');
    }

    function renderTradeChoices() {
        choicesDiv.innerHTML = ''; // Clear previous choices
        choicesDiv.innerHTML += '<h3>מסחר ב' + locations[gameState.currentLocation].name + ':</h3>';
        choicesDiv.innerHTML += '<div id="trade-options"></div>'; // Container for buy/sell buttons
        const tradeOptionsDiv = document.getElementById('trade-options');

        const cityGoods = locations[gameState.currentLocation].goods || {};

        // Display goods to SELL
        const inventoryItems = Object.entries(gameState.inventory).filter(([item, quantity]) => quantity > 0);
        if (inventoryItems.length > 0) {
             const sellTitle = document.createElement('p');
             sellTitle.innerHTML = '<strong>טובין למכירה:</strong>';
             tradeOptionsDiv.appendChild(sellTitle);

            inventoryItems.forEach(([item, quantity]) => {
                const goodsInfo = availableGoods.find(g => g.id === item);
                // Calculate potential sale price - slightly randomizes based on city price or base
                 const cityPrice = cityGoods[item];
                 let sellPrice;
                 if (cityPrice !== undefined) {
                      // Sell at city price +/- 10%
                     sellPrice = Math.max(1, Math.floor(cityPrice * (0.9 + Math.random() * 0.2)));
                 } else {
                      // If city doesn't list it, sell at base price * 0.6-0.9 (less profit)
                     sellPrice = Math.max(1, Math.floor(goodsInfo.basePrice * (0.6 + Math.random() * 0.3)));
                 }

                const sellButton = document.createElement('button');
                sellButton.textContent = `מכור ${quantity} יחידות ${goodsInfo.name} ($${sellPrice} ליחידה)`;
                 sellButton.classList.add('trade-button');
                 sellButton.addEventListener('click', () => sellGoods(item, quantity, sellPrice));
                 tradeOptionsDiv.appendChild(sellButton);
            });
        } else {
             const noSell = document.createElement('p');
             noSell.textContent = 'אין לך טובין למכירה כרגע.';
             tradeOptionsDiv.appendChild(noSell);
        }

        // Display goods to BUY
         const buyTitle = document.createElement('p');
         buyTitle.innerHTML = '<strong>טובין לקנייה:</strong>';
         tradeOptionsDiv.appendChild(buyTitle);

        if (Object.keys(cityGoods).length > 0) {
             for (const [item, price] of Object.entries(cityGoods)) {
                 const goodsInfo = availableGoods.find(g => g.id === item);
                 const buyButton = document.createElement('button');
                 buyButton.textContent = `קנה יחידת ${goodsInfo.name} ($${price})`;
                  buyButton.classList.add('trade-button');
                 buyButton.addEventListener('click', () => buyGoods(item, price));
                 tradeOptionsDiv.appendChild(buyButton);
             }
        } else {
            const noBuy = document.createElement('p');
            noBuy.textContent = 'אין טובין זמינים לקנייה בעיר זו.';
            tradeOptionsDiv.appendChild(noBuy);
        }

        const backButton = document.createElement('button');
        backButton.textContent = 'חזרה לבחירת פעולה';
        backButton.addEventListener('click', renderLocationChoices);
        choicesDiv.appendChild(backButton); // Add back button outside trade-options
    }

    function buyGoods(itemId, price) {
        if (gameState.money >= price) {
            gameState.money -= price;
            gameState.inventory[itemId] = (gameState.inventory[itemId] || 0) + 1;
            addMessage(`רכשת יחידת ${availableGoods.find(g => g.id === itemId).name} ב-$${price} ב${locations[gameState.currentLocation].name}.`, 'event-success');
            updateStatus();
            renderTradeChoices(); // Re-render trade options to reflect changes
        } else {
            addMessage(`אין לך מספיק ממון ($${formatMoney(gameState.money)}) לקנות יחידת ${availableGoods.find(g => g.id === itemId).name} ($${price}).`, 'event-fail');
        }
    }

     function sellGoods(itemId, quantity, pricePerUnit) {
         // Assuming the button click sells ALL quantity of that item
        if (gameState.inventory[itemId] >= quantity) {
            const totalSalePrice = pricePerUnit * quantity;
            gameState.money += totalSalePrice;
            gameState.inventory[itemId] -= quantity;
            if (gameState.inventory[itemId] <= 0) {
                 delete gameState.inventory[itemId]; // Remove from inventory if quantity is zero or less
            }
            addMessage(`מכרת ${quantity} יחידות ${availableGoods.find(g => g.id === itemId).name} ב-$${formatMoney(totalSalePrice)} ב${locations[gameState.currentLocation].name}.`, 'event-success');
            updateStatus();
            renderTradeChoices(); // Re-render trade options
        } else {
            addMessage(`שגיאה: אין לך מספיק יחידות של ${availableGoods.find(g => g.id === itemId).name} למכירה.`, 'event-fail');
             renderTradeChoices(); // Re-render in case of logic error
        }
     }


    function renderRouteChoices() {
        choicesDiv.innerHTML = ''; // Clear previous choices
        choicesDiv.innerHTML += '<h3>בחר מסלול ליעד הבא:</h3>';
        const currentLocation = locations[gameState.currentLocation];

        currentLocation.routes.forEach(routeId => {
            const route = routes[routeId];
            const destination = locations[route.to];
            const routeButton = document.createElement('button');
            routeButton.textContent = `מסע ${route.name} (${route.days} ימים, סיכון ~${Math.round(route.risk * 100)}%)`;
            routeButton.addEventListener('click', () => travel(routeId));
            choicesDiv.appendChild(routeButton);
        });

        const backButton = document.createElement('button');
        backButton.textContent = 'חזרה לבחירת פעולה';
        backButton.addEventListener('click', renderLocationChoices);
        choicesDiv.appendChild(backButton);
    }

    function travel(routeId) {
        const route = routes[routeId];
        addMessage(`יצאת למסע אל ${locations[route.to].name} דרך המסלול ${route.name}. צפויים ${route.days} ימי מסע.`, 'event-message');
        choicesDiv.innerHTML = `<p>במסע אל ${locations[route.to].name}...</p>`;
        disableChoices();
        currentLocationMap.classList.remove('pulse'); // Stop pulsing during travel
        travelProgressContainer.classList.remove('hidden'); // Show progress bar

        let daysPassedOnRoute = 0;
        const totalDays = route.days;

        const travelInterval = setInterval(() => {
            gameState.days++;
            daysPassedOnRoute++;
            updateStatus();

             // Update progress bar
             travelProgressBar.style.width = `${(daysPassedOnRoute / totalDays) * 100}%`;

            // Random event check each day
            // Adjust risk probability per day: total risk / total days in route
            if (Math.random() < route.risk / totalDays) {
                 handleRandomEvent(route.event); // Pass route event type for context
            }

            if (daysPassedOnRoute >= totalDays) {
                clearInterval(travelInterval);
                gameState.currentLocation = route.to;
                addMessage(`הגעת בשלום ל${locations[gameState.currentLocation].name}!`, 'event-success');
                 // Handle arrival events if needed (e.g., find unique goods)
                updateStatus();
                renderLocationChoices(); // Render new choices for the arrived location
                enableChoices(); // Ensure buttons are clickable again
                 travelProgressContainer.classList.add('hidden'); // Hide progress bar on arrival
            }

             // Check for game over during travel
             if (gameState.money <= 0) {
                 clearInterval(travelInterval); // Stop interval
                 addMessage(`אזל כספך במהלך המסע. השיירה התפזרה. מסעך הסתיים באכזבה בדרך ל${locations[route.to].name}.`, 'event-fail');
                 choicesDiv.innerHTML = '<div id="game-over">המסע הסתיים בפשיטת רגל.</div>';
                 disableChoices();
                 travelProgressContainer.classList.add('hidden');
             }

        }, 200); // Simulate a day every 200ms for a quick demo
    }

     function disableChoices() {
         choicesDiv.querySelectorAll('button').forEach(btn => btn.disabled = true);
     }

     function enableChoices() {
         choicesDiv.querySelectorAll('button').forEach(btn => btn.disabled = false);
     }


    function handleRandomEvent(routeEventType = null) {
        const eventRoll = Math.random();
        let eventHappened = false;

        // Prioritize events based on route type
        if (routeEventType === 'desert_travel' && eventRoll < 0.4) { // Higher chance of desert events
             if (Math.random() < 0.5) {
                 addMessage('סופת חול מאיימת! השיירה מתעכבת ביום.', 'event-neutral');
                 gameState.days++;
             } else {
                  const lostMoney = Math.floor(gameState.money * 0.08) + 20;
                  gameState.money = Math.max(0, gameState.money - lostMoney);
                 addMessage(`קשיי המדבר גובים מחיר: הוצאות בלתי צפויות של ${lostMoney}$ למים ותיקונים.`, 'event-fail');
             }
             eventHappened = true;
        } else if (routeEventType === 'mountains_travel' && eventRoll < 0.4) { // Higher chance of mountain events
            if (Math.random() < 0.5) {
                 addMessage('דרך קשה בהרים: המסע מתארך ביום.', 'event-neutral');
                 gameState.days++;
             } else {
                  const lostMoney = Math.floor(gameState.money * 0.08) + 20;
                  gameState.money = Math.max(0, gameState.money - lostMoney);
                 addMessage(`מעבר הרים מסוכן: ציוד ניזוק, הוצאת ${lostMoney}$ על תיקונים.`, 'event-fail');
             }
            eventHappened = true;
        }


        // General events (lower chance if specific event happened)
        if (!eventHappened && eventRoll < 0.6) {
            if (eventRoll < 0.2) { // Mild events
                const eventType = Math.random();
                if (eventType < 0.6) {
                    addMessage('פגשת שיירת סוחרים ידידותית. שמעת על מחירים טובים ביעד הבא!', 'event-message');
                    // No game effect yet, just flavor
                } else {
                     const lostMoney = Math.floor(gameState.money * 0.03) + 5; // Smaller loss
                     gameState.money = Math.max(0, gameState.money - lostMoney);
                    addMessage(`נתקלת בקשיים קטנים בדרך ואיבדת ${lostMoney}$ בהוצאות בלתי צפויות.`, 'event-fail');
                }
            } else if (eventRoll < 0.4) { // Moderate events
                 const eventType = Math.random();
                 if (eventType < 0.5) {
                    // Find goods - simplified
                     const gainedGoods = availableGoods[Math.floor(Math.random() * availableGoods.length)];
                     const quantityGained = 1; // Simplified to 1 item
                     gameState.inventory[gainedGoods.id] = (gameState.inventory[gainedGoods.id] || 0) + quantityGained;
                     addMessage(`מצאת סחורה נטושה בדרך! הרווחת יחידת ${gainedGoods.name}.`, 'event-success');
                 } else {
                     // Attempt to lose goods
                     const lostGoodsAmount = Math.floor(Math.random() * 2) + 1;
                     const inventoryItems = Object.keys(gameState.inventory).filter(item => gameState.inventory[item] > 0);
                     if (inventoryItems.length > 0) {
                          const lostItemId = inventoryItems[Math.floor(Math.random() * inventoryItems.length)];
                          const numToLose = Math.min(lostGoodsAmount, gameState.inventory[lostItemId]);
                           gameState.inventory[lostItemId] -= numToLose;
                           if (gameState.inventory[lostItemId] <= 0) {
                             delete gameState.inventory[lostItemId];
                           }
                           addMessage(`שודדים קטנים תקפו! איבדת ${numToLose} יחידות ${availableGoods.find(g => g.id === lostItemId).name}.`, 'event-fail');
                     } else {
                         addMessage(`שודדים ניסו לתקוף, אך לא היה לך דבר לגנוב.`, 'event-neutral'); // Less severe if no goods
                     }
                 }
            } else { // More severe events (less likely overall)
                const eventType = Math.random();
                if (eventType < 0.6) { // Sickness/Injury
                     const lostMoney = Math.floor(gameState.money * 0.1) + 30;
                     gameState.money = Math.max(0, gameState.money - lostMoney);
                     addMessage(`מחלה פרצה בשיירה! נאלצת להוציא ${lostMoney}$ על טיפול ותרופות יקרות.`, 'event-fail');
                } else { // Bandit attack
                     const lostMoney = Math.floor(gameState.money * 0.15) + 50;
                      const inventoryItems = Object.keys(gameState.inventory).filter(item => gameState.inventory[item] > 0);
                       let goodsLostCount = 0;
                       if (inventoryItems.length > 0 && Math.random() > 0.5) { // Also lose some goods potentially
                           const lostItemId = inventoryItems[Math.floor(Math.random() * inventoryItems.length)];
                           const numToLose = Math.floor(Math.random() * Math.min(3, gameState.inventory[lostItemId])) + 1;
                            gameState.inventory[lostItemId] -= numToLose;
                           if (gameState.inventory[lostItemId] <= 0) {
                             delete gameState.inventory[lostItemId];
                           }
                           goodsLostCount = numToLose;
                            addMessage(`שודדים גדולים תקפו! איבדת ${lostMoney}$ בממון ו${goodsLostCount} יחידות ${availableGoods.find(g => g.id === lostItemId).name}.`, 'event-fail');
                       } else {
                            addMessage(`שודדים גדולים תקפו! איבדת ${lostMoney}$ בממון.`, 'event-fail');
                       }
                     gameState.money = Math.max(0, gameState.money - lostMoney);

                }
            }
        }

        updateStatus(); // Update status after event
    }

    // Toggle Explanation Visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר על דרך המשי';
    });

    // Start the game
    initGame();

    function initGame() {
        updateStatus();
        renderLocationChoices();
         addMessage("ברוכים הבאים למסע על דרך המשי! התחילו את מסעכם בוונציה.", 'event-message');
    }

</script>
```