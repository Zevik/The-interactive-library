---
title: "הסחר המשולש האטלנטי: מסע של עושר אדיר וסבל נורא"
english_slug: atlantic-triangular-trade-journey-wealth-slavery
category: "ארכאולוגיה"
tags: [היסטוריה, עבדות, קולוניאליזם, סחר ימי, עידן התגליות]
---
# הסחר המשולש האטלנטי: מסע של עושר אדיר וסבל נורא

כיצד נוצר מסלול ימי שהתקיים במשך מאות שנים, חיבר באכזריות שלוש יבשות, והפך למנוע כלכלי שהעשיר קומץ על חשבון סבל נורא של מיליונים? מסע הסחר המשולש האטלנטי הוא פרק מרכזי, אפל ומשפיע ביותר בהיסטוריה העולמית. התנסו בסימולציה לפני שתקראו את ההסבר המלא.

<div id="app-container">
    <div id="map-simulation">
        <div id="europe" class="region" data-region="europe">אירופה</div>
        <div id="africa" class="region" data-region="africa">אפריקה</div>
        <div id="americas" class="region" data-region="americas">אמריקות</div>

        <!-- Lines representing the routes -->
        <svg id="routes-svg" width="100%" height="100%">
            <line id="route1" class="route" x1="0" y1="0" x2="0" y2="0" data-route="1"></line> <!-- Europe to Africa -->
            <line id="route2" class="route" x1="0" y1="0" x2="0" y2="0" data-route="2"></line> <!-- Africa to Americas -->
            <line id="route3" class="route" x1="0" y1="0" x2="0" y2="0" data-route="3"></line> <!-- Americas to Europe -->
        </svg>

        <div id="ship1" class="ship hidden"></div>
        <div id="ship2" class="ship hidden"></div>
        <div id="ship3" class="ship hidden"></div>
    </div>

    <div id="sim-message"></div>

    <div id="controls">
        <button id="start-sim-btn">התחל סימולציה (3 סבבים)</button>
    </div>

    <div id="route-details" class="hidden">
        <h3>פרטי המסלול</h3>
        <div id="details-content"></div>
    </div>
</div>

<button id="toggle-explanation-btn">הצג הסבר מלא</button>

<div id="explanation-section" class="hidden">
    <h2>הסחר המשולש האטלנטי: הרקע וההשפעות</h2>

    <h3>מבוא: מחזור של עבדות, סחורות ועושר</h3>
    <p>הסחר המשולש האטלנטי היה מערכת כלכלית ענקית שפעלה באוקיינוס האטלנטי בין המאה ה-16 למאה ה-19. הוא קישר את אירופה, אפריקה והאמריקות במסלול סחר בצורת משולש. עמוד התווך המרכזי והמחריד של סחר זה היה שעבודם וטרנספורטציה הכפויה של מיליוני בני אדם מאפריקה לאמריקות, כדי שישמשו כוח עבודה במטעים הרווחיים שהקימו המעצמות האירופיות בקולוניות שלהן.</p>

    <h3>שורשי הסחר: הצורך בכוח עבודה בקולוניות</h3>
    <p>עם הקמתן של מושבות אירופיות באמריקות (בעיקר על ידי ספרד, פורטוגל, אנגליה, צרפת והולנד), נוצר צורך עצום בידיים עובדות לעיבוד שטחי ענק של גידולים כמו סוכר, טבק וכותנה. ניסיונות לנצל את האוכלוסייה הילידית נכשלו בגלל מחלות, התנגדות וידע מקומי שאפשר בריחה. האירופים פנו אז לאפריקה, שם סחר עבדים כבר היה קיים בצורות שונות (לרוב שבויים ממלחמות או עבריינים), וראו באפריקאים מקור כוח עבודה "עמיד" וזמין בכמויות אדירות. כך הפך סחר העבדים הקודם, שהיה מצומצם בהיקפו ונפוץ יותר באפריקה ובים התיכון, למנגנון תעשייתי וגלובלי בהיקף חסר תקדים.</p>

    <h3>הרגל הראשונה: מאירופה לאפריקה – "סחורות תמורת בני אדם"</h3>
    <p>ספינות אירופיות יצאו מנמלי מוצא כמו ליברפול, בריסטול, נאנט או אמסטרדם, עמוסות בסחורות ששימשו כ"תמורה" (בפועל, תשלום) עבור האנשים שישועבדו. הסחורות כללו מגוון רחב של מוצרים אירופיים, כגון כלי נשק (רובים, אבק שריפה), טקסטיל, אלכוהול (רום, ברנדי), כלי מתכת, חרוזים, ומוצרי יוקרה קטנים. סוחרים אפריקאים או שליטים מקומיים לאורך חופי מערב אפריקה (לעיתים גם מפנים היבשת) סחרו את אותם מוצרים תמורת שבויים שנלכדו במלחמות, פשיטות או חטיפות ייעודיות למטרת הסחר. סחר זה הגביר סכסוכים פנימיים באפריקה ושיבש את המבנים החברתיים והכלכליים המקומיים.</p>

    <h3>הרגל השני: "המעבר האמצעי" (Middle Passage) – מסע האימה לאמריקה</h3>
    <p>זו הייתה הרגל האכזרית וההרסנית ביותר של הסחר המשולש. האנשים שנלכדו שועבדו והועברו בכפייה אל עבר האוקיינוס האטלנטי, בבטן אוניות צפופות ומזוהמות בתנאים בלתי נתפסים. המסע ארך שבועות או חודשים, במהלכם נדחסו האסירים זה לצד זה, סבלו ממחלות קשות (דיזנטריה, אבעבועות שחורות), תת-תזונה, אלימות, דיכוי פסיכולוגי והשפלה מתמדת. שיעורי התמותה במהלך המעבר היו גבוהים ביותר, מוערכים בממוצע ב-15-25%, אך לעיתים אף הרבה יותר. על פי הערכות היסטוריות, כ-10 עד 12 מיליון אפריקאים שרדו את המסע והגיעו לאמריקות, אך מיליונים רבים אחרים מתו בתהליך הלכידה באפריקה, ההובלה לחופים, ההמתנה על החוף, ובמהלך המעבר עצמו. מסע זה השאיר צלקת עמוקה בתולדות האנושות ועיצב מחדש את הדמוגרפיה והחברה באמריקות.</p>

    <h3>הרגל השלישית: מאמריקה לאירופה – הפירות המרים של העבודה המשועבדת</h3>
    <p>לאחר פריקת האנשים המשועבדים באמריקות (בעיקר באיים הקריביים, ברזיל, וצפון אמריקה), האוניות מולאו בתוצרת שנוצרה על ידי עבודתם הכפויה. סחורות אלו כללו בעיקר סוכר (שהיה רווחי להפליא), טבק, כותנה, קפה, אינדיגו, רום, מולסה, עץ ופרוות. סחורות "קולוניאליות" אלו הובלו חזרה לאירופה ונמכרו שם ברווחים עצומים. רווחים אלה היו מנוע כלכלי אדיר, תדלקו את התפתחות התעשייה והמסחר באירופה, מימנו את המשך הסחר המשולש עצמו, והיוו בסיס לצבירת הון שעיצב את העולם המודרני. הצריכה של מוצרים כמו סוכר, קפה וטבק הפכה לנחלת הכלל בחברה האירופית.</p>

    <h3>מורשת הסחר: השפעות ארוכות טווח</h3>
    <ul>
        <li>**באפריקה:** הרס חברתי וכלכלי עצום, איבוד אוכלוסייה צעירה ופרודוקטיבית בהיקפים בלתי נתפסים, החלשת ממלכות ומבנים חברתיים, הגברת מלחמות פנימיות למטרת לכידת עבדים, ודיכוי פוטנציאל התפתחות מקומי.</li>
        <li>**באמריקות:** יצירת חברות קולוניאליות שנבנו על בסיס מוסד העבדות, עם היררכיות גזעיות נוקשות ועמוקות שעדיין משפיעות היום. הגעתם הכפויה של מיליוני אפריקאים עיצבה את התרבות (מוזיקה, דת, אמנות, שפה) של אזורים רבים באמריקות, במקביל לסבל והדיכוי הבלתי פוסקים של האוכלוסייה המשועבדת וצאצאיה.</li>
        <li>**באירופה:** צמיחה כלכלית מואצת, צבירת הון עצום, התפתחות נמלים ומרכזי מסחר, ומימון המהפכה התעשייתית. הסחר הגביר את כוחן של מעצמות ימיות והשפיע על התרבות האירופית באמצעות הנגישות למוצרים קולוניאליים.</li>
    </ul>

    <h3>קץ הסחר והמאבק לביטול העבדות</h3>
    <p>במאה ה-19 החל הסחר המשולש לדעוך בהשפעת גורמים כמו התחזקות תנועות נגד עבדות (אבולושניזם), שינויים כלכליים, ופעולות חוקיות של מדינות שונות לאסור את סחר העבדים (בריטניה ב-1807) ולבטל את מוסד העבדות עצמו (בריטניה ב-1833, צרפת ב-1848, ארה"ב ב-1865, ברזיל ב-1888). למרות ביטולו הרשמי של הסחר והעבדות, השפעותיהם ההרסניות נמשכו דורות רבים קדימה ומעצבות את העולם עד ימינו.</p>
</div>

<style>
    /* הגדרות כלליות ו-RTL */
    #app-container {
        font-family: 'Arial', 'Helvetica Neue', Helvetica, sans-serif;
        max-width: 960px; /* מעט רחב יותר */
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 12px; /* פינות מעוגלות יותר */
        background: linear-gradient(to bottom right, #f5f7fa, #c3cfe2); /* רקע גרדיאנט עדין */
        direction: rtl; /* RTL support */
        text-align: right;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1); /* צל עדין */
    }

    h1, h2, h3, p, ul, div, button {
        text-align: right; /* ודא יישור לימין */
    }

    #map-simulation {
        position: relative;
        width: 100%;
        padding-top: 55%; /* יחס גובה-רוחב מותאם יותר למפה אטלנטית */
        background: linear-gradient(to bottom right, #a1c4fd, #c2e9fb); /* גרדיאנט תכלת לאוקיינוס */
        border: 1px solid #89cff0;
        border-radius: 8px;
        box-sizing: border-box;
        margin-bottom: 20px;
        overflow: hidden; /* לוודא שהכל נשאר בפנים */
    }

    .region {
        position: absolute;
        background: linear-gradient(to bottom right, #d4fc79, #96e6a1); /* גרדיאנט ירוק ליבשות */
        border: 1px solid #388e3c;
        padding: 12px 15px; /* מרווח פנימי גדול יותר */
        border-radius: 8px; /* פינות מעוגלות */
        text-align: center;
        font-weight: bold;
        font-size: 1em; /* גודל גופן מעט גדול יותר */
        color: #333;
        z-index: 10; /* Above lines */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* צל קטן לאפקט תלת ממד */
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* אנימציית ריחוף/צל בעת אינטראקציה */
    }

    .region:hover {
         transform: translateY(-3px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.3);
         cursor: pointer; /* מראה שהן אינטראקטיביות */
    }

    /* אנימציית פעימה עבור האזור הפעיל בסימולציה */
    .region.active {
        animation: pulse 1s infinite ease-in-out alternate;
    }

    @keyframes pulse {
        from { transform: scale(1); box-shadow: 0 0 0 rgba(56, 142, 60, 0.7); }
        to { transform: scale(1.05); box-shadow: 0 0 10px rgba(56, 142, 60, 1); }
    }


    /* מיקום משוער ליבשות באוקיינוס האטלנטי */
    #europe { top: 8%; left: 70%; width: 15%; }
    #africa { top: 60%; left: 70%; width: 15%; }
    #americas { top: 30%; left: 10%; width: 20%; }


    #routes-svg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 5; /* Below regions, above background */
        /* pointer-events: none; /* Allow clicks on underlying elements if needed */
    }

    .route {
        stroke: rgba(229, 115, 115, 0.8); /* Reddish color for routes, slightly transparent */
        stroke-width: 4; /* קו עבה יותר */
        fill: none;
        opacity: 0.8;
        cursor: pointer; /* Make routes clickable */
        pointer-events: all; /* Enable click on stroke */
        transition: stroke-width 0.3s, opacity 0.3s;
    }

    .route:hover {
        stroke-width: 6;
        opacity: 1;
        stroke: rgba(198, 40, 40, 1); /* צבע אדום עז יותר בעת ריחוף */
    }

    /* אנימציית הבהוב עבור המסלול הפעיל בסימולציה */
    .route.active {
        stroke: rgba(198, 40, 40, 1); /* צבע אדום עז */
        stroke-width: 6;
        opacity: 1;
        animation: route-pulse 1.5s infinite ease-in-out alternate;
    }

    @keyframes route-pulse {
        from { stroke: rgba(198, 40, 40, 0.8); stroke-width: 4; }
        to { stroke: rgba(198, 40, 40, 1); stroke-width: 6; }
    }

    .ship {
        position: absolute;
        font-size: 2.5em; /* ספינה גדולה ובולטת יותר */
        z-index: 15; /* Above everything */
        color: #3b5998; /* צבע כחול עמוק לספינה */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3); /* צל קטן לספינה */
        /* transition property is set dynamically in JS */
    }

     /* Use specific ship emojis/icons per leg for better storytelling */
     #ship1::before { content: '📦'; /* סחורות מאירופה */ }
     #ship2::before { content: ' chains '; /* רמז לעבדים */ color: #c0392b; /* אדום עגום */ }
     #ship3::before { content: '💰'; /* סחורות רווחיות לאירופה */ }


    .hidden {
        display: none;
    }

    #sim-message {
        text-align: center;
        margin-bottom: 20px;
        font-size: 1.1em;
        color: #333;
        min-height: 2em; /* לשמור על מקום גם כשהוא ריק */
    }

    #controls {
        text-align: center;
        margin-bottom: 20px;
    }

    button {
        padding: 12px 25px; /* מרווח פנימי גדול יותר */
        font-size: 1.1em; /* גודל גופן גדול יותר */
        cursor: pointer;
        background-color: #5cb85c; /* ירוק נעים */
        color: white;
        border: none;
        border-radius: 6px; /* פינות מעוגלות */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease; /* אנימציות בלחיצה וריחוף */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    button:hover {
        background-color: #4cae4c; /* ירוק כהה יותר בריחוף */
        box-shadow: 0 3px 6px rgba(0,0,0,0.3);
    }

    button:active {
        transform: scale(0.98); /* כיווץ קל בלחיצה */
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
    }


    #route-details {
        margin-top: 20px;
        padding: 20px; /* מרווח פנימי גדול יותר */
        border: 1px solid #b0bec5;
        border-radius: 8px; /* פינות מעוגלות */
        background-color: #e0f2f7; /* רקע תכלת בהיר לאזור הפרטים */
        transition: all 0.5s ease-in-out; /* אנימציה בהצגה/הסתרה */
    }

    #route-details h3 {
        margin-top: 0;
        color: #37474f;
        border-bottom: 1px solid #b0bec5; /* קו הפרדה לכותרת */
        padding-bottom: 8px;
        margin-bottom: 10px;
    }

    #route-details p {
        margin-bottom: 10px;
        line-height: 1.5;
        color: #555;
    }


    #explanation-section {
        margin-top: 30px;
        padding: 25px; /* מרווח פנימי גדול יותר */
        border-top: 2px solid #ccc; /* קו הפרדה עבה יותר */
        background-color: #ffffff; /* רקע לבן להסבר */
        border-radius: 8px;
        direction: rtl; /* RTL support */
        text-align: right;
        line-height: 1.7; /* מרווח שורות גדול יותר */
        color: #333;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }

    #explanation-section h2 {
        color: #0277bd; /* כחול עמוק לכותרת ראשית */
        margin-bottom: 20px;
        border-bottom: 1px solid #b3e5fc;
        padding-bottom: 10px;
    }

    #explanation-section h3 {
        color: #4CAF50; /* ירוק לכותרות משנה */
        margin-top: 20px;
        margin-bottom: 10px;
    }

    #explanation-section p,
    #explanation-section ul {
        margin-bottom: 18px; /* מרווח גדול יותר בין פסקאות ורשימות */
    }

    #explanation-section ul {
        padding-left: 0; /* בטל ריפוד שמאל */
        padding-right: 25px; /* ריפוד ימין לרשימות */
        list-style-type: disc;
    }

     #explanation-section li {
         margin-bottom: 8px; /* מרווח בין פריטי רשימה */
     }

    /* התאמות נוספות ל-RTL */
    #explanation-section ul {
        padding-left: 0;
        padding-right: 20px; /* Standard RTL padding */
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const startSimBtn = document.getElementById('start-sim-btn');
        const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
        const explanationSection = document.getElementById('explanation-section');
        const europeEl = document.getElementById('europe');
        const africaEl = document.getElementById('africa');
        const americasEl = document.getElementById('americas');
        const route1El = document.getElementById('route1'); // Europe to Africa
        const route2El = document.getElementById('route2'); // Africa to Americas
        const route3El = document.getElementById('route3'); // Americas to Europe
        const ship1El = document.getElementById('ship1');
        const ship2El = document.getElementById('ship2');
        const ship3El = document.getElementById('ship3');
        const detailsDiv = document.getElementById('route-details');
        const detailsContentDiv = document.getElementById('details-content');
        const simMessageDiv = document.getElementById('sim-message');
        const svgEl = document.getElementById('routes-svg');

        let simulationRunning = false;
        const totalSimCycles = 3;
        let currentCycle = 0;

        // Get center coordinates of regions relative to the SVG
        const getCenter = (el) => {
            const rect = el.getBoundingClientRect();
            const svgRect = svgEl.getBoundingClientRect();
            // Convert coordinates relative to SVG parent
            const x = rect.left + rect.width / 2 - svgRect.left;
            const y = rect.top + rect.height / 2 - svgRect.top;
            return { x, y };
        };

        // Update line positions based on region positions
        const updateRouteLines = () => {
            const europePos = getCenter(europeEl);
            const africaPos = getCenter(africaEl);
            const americasPos = getCenter(americasEl);

            // Europe to Africa (Route 1)
            route1El.setAttribute('x1', europePos.x);
            route1El.setAttribute('y1', europePos.y);
            route1El.setAttribute('x2', africaPos.x);
            route1El.setAttribute('y2', africaPos.y);

            // Africa to Americas (Route 2 - Middle Passage)
            route2El.setAttribute('x1', africaPos.x);
            route2El.setAttribute('y1', africaPos.y);
            route2El.setAttribute('x2', americasPos.x);
            route2El.setAttribute('y2', americasPos.y);

            // Americas to Europe (Route 3)
            route3El.setAttribute('x1', americasPos.x);
            route3El.setAttribute('y1', americasPos.y);
            route3El.setAttribute('x2', europePos.x);
            route3El.setAttribute('y2', europePos.y);
        };

        // Ensure lines are positioned correctly initially and on resize
        const resizeObserver = new ResizeObserver(updateRouteLines);
        resizeObserver.observe(svgEl.parentElement); // Observe the parent container for size changes

        // Data for route details and simulation messages
        const routeDetails = {
            1: {
                title: "הרגל הראשונה: מאירופה לאפריקה (סחורות)",
                content: "<p>אוניות אירופיות הובילו סחורות כמו כלי נשק, טקסטיל, אלכוהול ועוד, כדי לסחור אותן תמורת בני אדם משועבדים באפריקה.</p>"
            },
            2: {
                title: "הרגל השני: 'המעבר האמצעי' (Middle Passage - אנשים משועבדים)",
                content: "<p>המסע האכזרי והקטלני ביותר. מיליוני אפריקאים שועבדו והועברו באוניות צפופות לאמריקות, בתנאים מחרידים שגרמו לתמותה גבוהה.</p>"
            },
            3: {
                title: "הרגל השלישית: מאמריקה לאירופה (סחורות מטעים)",
                content: "<p>אוניות חזרו לאירופה עמוסות בתוצרת רווחית שיוצרה בעבודת עבדים באמריקות: סוכר, טבק, כותנה, קפה ועוד. רווחים אלו תדלקו את כלכלות אירופה.</p>"
            }
        };

        const simMessages = {
            1: "📦 אוניות אירופיות יוצאות לאפריקה עמוסות סחורות...",
            2: "⛓️ מתחיל 'המעבר האמצעי' האכזרי: אנשים משועבדים בדרך לאמריקות...",
            3: "💰 אוניות חוזרות לאירופה עמוסות סחורות מטעים רווחיות...",
            end: "🔄 סבב הסימולציה ה- %CYCLE% מתוך %TOTAL% הסתיים.",
            final_end: "✅ הסימולציה הסתיימה. לחץ על קו במסלול לפרטים נוספים."
        };

        const showRouteDetails = (routeNum) => {
            // Only show details if simulation is not running, or if it just ended
            if (simulationRunning) return;

            detailsDiv.classList.remove('hidden');
            detailsContentDiv.innerHTML = `<h3>${routeDetails[routeNum].title}</h3>${routeDetails[routeNum].content}`;

            // Optional: Highlight the clicked route temporarily
            const routeEl = document.getElementById(`route${routeNum}`);
            routeEl.classList.add('active');
            setTimeout(() => {
                 routeEl.classList.remove('active');
            }, 1000); // Highlight for 1 second
        };

        // Add click handlers to routes to show static details
        route1El.addEventListener('click', () => showRouteDetails(1));
        route2El.addEventListener('click', () => showRouteDetails(2));
        route3El.addEventListener('click', () => showRouteDetails(3));

        // Simulation logic
        const animateShip = (shipEl, startEl, endEl, durationMultiplier, message, routeEl, startRegionEl, endRegionEl, onComplete) => {
             if (!shipEl || !startEl || !endEl || !routeEl || !startRegionEl || !endRegionEl) {
                 console.error("Missing elements for animation");
                 return;
             }

            shipEl.classList.remove('hidden');
            startRegionEl.classList.add('active'); // Highlight start region
            routeEl.classList.add('active'); // Highlight route

            const startPos = getCenter(startEl);
            const endPos = getCenter(endEl);

            // Set initial position
            shipEl.style.left = `${startPos.x}px`;
            shipEl.style.top = `${startPos.y}px`;
            shipEl.style.transform = 'translate(-50%, -50%)'; // Center ship icon
            shipEl.style.transition = 'none'; // Reset transition for immediate repositioning

            // Calculate distance for scaling duration (pixel distance on screen)
            const dx = endPos.x - startPos.x;
            const dy = endPos.y - startPos.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            // Scale duration based on distance and a multiplier. Base duration could be 1000ms per ~200px distance.
            const baseSpeed = 200; // pixels per second reference
            const actualDuration = (dist / baseSpeed) * durationMultiplier; // durationMultiplier allows some legs to be longer/shorter

            // Determine ship rotation based on direction (simple left/right flip for horizontal movement)
            // Note: Emoji ships don't rotate arbitrarily well with CSS alone based on exact angle.
            // Simple horizontal flip is achievable with transform: scaleX(-1);
            // For complex paths, this simple flip won't look right. Let's omit angle-based rotation for simplicity
            // within constraints, but we can flip for leftward movement if needed.
            // const angle = Math.atan2(dy, dx) * 180 / Math.PI;
            // shipEl.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`; // This works visually but isn't RTL-aware

            // For RTL, the ship icon might need to face the opposite direction of movement.
            // The standard ship emoji faces right. For movement to the left (Americas), we might flip it.
             if (dx < 0) { // Moving left (e.g., Africa to Americas)
                 shipEl.style.transform = 'translate(-50%, -50%) scaleX(-1)';
             } else { // Moving right or mostly vertical
                 shipEl.style.transform = 'translate(-50%, -50%) scaleX(1)';
             }


            simMessageDiv.textContent = message; // Update simulation message

            // Start animation using requestAnimationFrame for smoother visuals
            requestAnimationFrame(() => {
                 // Set the transition property *after* setting the initial position
                 shipEl.style.transition = `left ${actualDuration}ms linear, top ${actualDuration}ms linear, transform ${actualDuration}ms linear`;

                 // Set the final position to start the animation
                 shipEl.style.left = `${endPos.x}px`;
                 shipEl.style.top = `${endPos.y}px`;

                // Keep the transform logic here as well for the end state of the animation
                if (dx < 0) {
                     shipEl.style.transform = 'translate(-50%, -50%) scaleX(-1)';
                 } else {
                     shipEl.style.transform = 'translate(-50%, -50%) scaleX(1)';
                 }
            });


            // Hide ship and call complete function after animation duration
            setTimeout(() => {
                shipEl.classList.add('hidden');
                routeEl.classList.remove('active'); // Remove highlight
                startRegionEl.classList.remove('active'); // Remove highlight
                // Note: The END region is highlighted in the *next* step as the START region of the next leg.

                // Reset transition for the next animation cycle
                 shipEl.style.transition = 'none';
                 shipEl.style.left = `${startPos.x}px`; // Reset position immediately

                if (onComplete) {
                    onComplete();
                }
            }, actualDuration);
        };

        const runSimulationCycle = (cycle) => {
            if (cycle > totalSimCycles) {
                endSimulation();
                return;
            }

            currentCycle = cycle;

            // Leg 1: Europe to Africa (Goods)
            animateShip(ship1El, europeEl, africaEl, 1.0, simMessages[1], route1El, europeEl, africaEl, () => {
                // Leg 2: Africa to Americas (Enslaved People - Middle Passage)
                // Use a longer duration multiplier for this leg to emphasize the difficulty/length
                animateShip(ship2El, africaEl, americasEl, 1.8, simMessages[2], route2El, africaEl, americasEl, () => {
                    // Leg 3: Americas to Europe (Plantation Goods)
                    animateShip(ship3El, americasEl, europeEl, 1.3, simMessages[3], route3El, americasEl, europeEl, () => {
                        // Cycle complete
                        simMessageDiv.textContent = simMessages.end.replace('%CYCLE%', currentCycle).replace('%TOTAL%', totalSimCycles);
                        // Add a slight pause before the next cycle or ending
                        setTimeout(() => {
                            runSimulationCycle(cycle + 1);
                        }, 1500); // Pause for 1.5 seconds
                    });
                });
            });
        };


        const startSimulation = () => {
            if (simulationRunning) return;
            simulationRunning = true;
            startSimBtn.disabled = true; // Disable button while simulating
            detailsDiv.classList.add('hidden'); // Hide details during simulation
            simMessageDiv.textContent = "הסימולציה מתחילה...";

            runSimulationCycle(1); // Start the first cycle
        };

        const endSimulation = () => {
            simulationRunning = false;
            startSimBtn.disabled = false; // Enable button
            detailsDiv.classList.remove('hidden'); // Show details area again
            detailsContentDiv.innerHTML = `<p>${simMessages.final_end}</p>`;
            simMessageDiv.textContent = ""; // Clear simulation message
        };


        startSimBtn.addEventListener('click', startSimulation);

        // Toggle explanation visibility
        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationSection.classList.contains('hidden');
            if (isHidden) {
                explanationSection.classList.remove('hidden');
                toggleExplanationBtn.textContent = 'הסתר הסבר מלא';
            } else {
                explanationSection.classList.add('hidden');
                toggleExplanationBtn.textContent = 'הצג הסבר מלא';
                // Scroll back up to the simulation area when hiding explanation
                detailsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });

        // Initial setup
        updateRouteLines(); // Position lines correctly on load
        detailsContentDiv.innerHTML = "<p>לחץ על 'התחל סימולציה' כדי לראות את זרימת הסחר. לחץ על קו במסלול (לפני או אחרי הסימולציה) כדי לראות פרטים עליו.</p>";
        detailsDiv.classList.remove('hidden'); // Show initial message
        simMessageDiv.textContent = ""; // Ensure sim message is empty initially

         // Add a small visual cue to regions that they are clickable (even if they only show details on route click now)
         document.querySelectorAll('.region').forEach(region => {
             region.style.cursor = 'pointer';
             region.title = `אזור: ${region.textContent}`; // Add title attribute
         });


    });
</script>