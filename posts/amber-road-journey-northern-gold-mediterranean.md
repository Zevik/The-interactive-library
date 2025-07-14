---
title: "דרך הענבר: מסע הזהב הצפוני לים התיכון"
english_slug: amber-road-journey-northern-gold-mediterranean
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags:
  - דרך הענבר
  - סחר עתיק
  - אירופה
  - ים התיכון
  - ארכיאולוגיה
---

# דרך הענבר: מסע הזהב הצפוני לים התיכון

מה קושר בין חופי הים הבלטי הקפואים לתרבויות העשירות של הים התיכון? צאו למסע מרתק לאורך דרך הענבר, נתיב סחר עתיק שחיבר יבשות והניע חילופי תרבות, כלכלה וידע במשך אלפי שנים, הכל בזכות חומר גלם אחד: שרף עצים מאובן, המכונה גם "הזהב הצפוני". התנסו במפה האינטראקטיבית למטה כדי לחשוף את מסלולי הסחר לאורך התקופות!

<div id="app-container">
    <div id="map-area">
        <img id="amber-map-image" src="https://via.placeholder.com/900x585?text=Map+of+Europe+and+Mediterranean" alt="Map of Amber Road"> <!-- Replace with actual map image -->

        <div class="period-controls">
            <button data-period="bronze-age">תקופת הברונזה</button>
            <button data-period="roman-era">התקופה הרומית</button>
            <button data-period="all">הצג הכל</button>
        </div>

        <!-- Points - positions relative to map-area -->
        <div class="map-point source baltic" data-point="baltic-source" data-info="מקורות ענבר עיקריים: חופי הים הבלטי (אזור קלינינגרד/פומרניה). הענבר נאסף בחוף או נכרה ונחשב ל'זהב הצפוני'."></div>
        <div class="map-point demand crete" data-point="crete" data-info="כרתים המינואית/מיקנית: מרכז ביקוש עתיק לענבר בתקופת הברונזה המאוחרת. שימש לתכשיטים יוקרתיים שנמצאו בארמונות וקברים."></div>
        <div class="map-point demand mycenae" data-point="mycenae" data-info="מיקנה (יוון): מרכז כוח מיקני וצרכן מרכזי של ענבר. נמצא ענבר רב בקברים מלכותיים, המעיד על חשיבותו כסמל סטטוס."></div>
        <div class="map-point demand rome" data-point="rome" data-info="רומא העתיקה: הצרכנית הגדולה ביותר בתקופה הרומית. הענבר (succinum) היה מבוקש בטירוף לתכשיטים, קישוטים, ואף כתרופה, והניע סחר עצום."></div>
         <div class="map-point demand egypt" data-point="egypt" data-info="מצרים העתיקה: ענבר בלטי הגיע למצרים כבר בתקופות קדומות, סימן לקשרים רחוקים ויוקרה. ממצאים מפורסמים מקבר תות ענח' אמון."></div>
         <div class="map-point key-point aquileia" data-point="aquileia" data-info="אקוויליה (איטליה): עיר נמל רומית מרכזית, נקודת הקצה הראשית לנתיב היבשתי הרומי מהבלטי. מרכז עיבוד והפצת ענבר לאורך כל האימפריה."></div>
         <div class="map-point key-point vienna" data-point="vienna" data-info="וינדהבונה (וינה של היום): יישוב חשוב על נהר הדנובה, שימש כתחנה מרכזית בנתיב הענבר הרומי שחצה את פאנוניה. חלק ממערך הלוגיסטיקה הרומי."></div>
          <div class="map-point key-point maribor" data-point="maribor" data-info="פואטובו (מריבור של היום, סלובניה): עיר רומית חשובה על נהר הדראווה, מהווה נקודה מרכזית בנתיב שחצה את האלפים לכיוון אקוויליה."></div>
           <div class="map-point key-point prague" data-point="prague" data-info="אזור בוהמיה (צ'כיה): צומת דרכים פוטנציאלי בנתיבי הברונזה והרומית המוקדמת, קישר בין נהרות הצפון והדרום."></div>


        <!-- Routes - represented as simple divs to allow animation -->
        <!-- Bronze Age routes -->
        <div class="amber-route bronze-age route-style-1" data-route="baltic-crete" data-info="נתיב ימי/נהרות משוער מתקופת הברונזה. אולי דרך הוויסלה, הדנייפר והים השחור, או נתיבים מערביים יותר דרך מרכז אירופה והדנובה לים האדריאטי ומשם לכרתים."></div>
         <div class="amber-route bronze-age route-style-2" data-route="baltic-mycenae" data-info="נתיב יבשתי/נהרות משוער בתקופת הברונזה דרך פולין, צ'כיה, אוסטריה והבלקן. עדויות ארכיאולוגיות חזקות לענבר בלטי באתרים מיקניים."></div>
         <div class="amber-route bronze-age route-style-3" data-route="baltic-egypt-bronze" data-info="ענבר בלטי הגיע למצרים כבר בתקופת הברונזה, כנראה דרך רשתות הסחר המינואיות/מיקניות והלבנט. מסע ארוך ומרובה מתווכים."></div>


        <!-- Roman Era routes -->
        <div class="amber-route roman-era route-style-4" data-route="baltic-aquileia" data-info="הנתיב היבשתי הראשי והמאורגן ביותר בתקופה הרומית. יצא מחופי הבלטי, חצה את פאנוניה דרך נהרות כמו הדנובה והדראווה, והגיע לאקוויליה באיטליה. נתיב מהיר יחסית בזכות תשתיות רומיות חלקיות."></div>
         <div class="amber-route roman-era route-style-5" data-route="baltic-rome" data-info="מגוון נתיבים רומיים שהובילו לעיר רומא עצמה, לרוב דרך אקוויליה ומשם דרומה בדרכים הרומיות או בנתיבים ימיים. הביקוש העצום ברומא הפך את הסחר לממוסד."></div>
         <div class="amber-route roman-era route-style-6" data-route="baltic-egypt-roman" data-info="ענבר המשיך לזרום למצרים בתקופה הרומית, בעיקר דרך נמלי הים התיכון כמו אלכסנדריה, לאחר שהגיע לשם דרך נתיבי הענבר הרומיים או הימיים."></div>

        <div id="info-panel">
            <h3>מידע</h3>
            <p id="info-content"></p>
            <button id="close-info">סגור</button>
        </div>

        <div id="custom-tooltip" style="display: none;"></div>

    </div>
</div>

<style>
/* Global styles */
body {
    font-family: 'Arial', sans-serif; /* A common, readable font */
    line-height: 1.6;
    color: #333;
    background-color: #eef2f7; /* Light background */
}

#app-container {
    width: 100%;
    max-width: 900px;
    margin: 30px auto;
    border: 1px solid #dcdcdc;
    border-radius: 12px;
    overflow: hidden;
    background-color: #ffffff;
    box-shadow: 0 8px 16px rgba(0,0,0,0.1); /* Soft shadow */
}

/* Map Area */
#map-area {
    position: relative;
    width: 100%;
    padding-bottom: 65%; /* Maintain aspect ratio (900/585 ≈ 1.54, 1/1.54 ≈ 0.65) */
    background-color: #a0c8e8; /* Placeholder blue */
    /* Placeholder image URL is in the HTML. Replace with a high-quality map image later. */
    background-size: cover;
    background-position: center;
    border-bottom: 1px solid #dcdcdc;
}

#amber-map-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover; /* Ensures the image covers the area without distortion */
    z-index: 1; /* Below points and routes */
}


/* Controls */
.period-controls {
    position: absolute;
    top: 15px;
    left: 15px;
    z-index: 15; /* Above map elements */
    background-color: rgba(255, 255, 255, 0.9);
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.period-controls button {
    margin-left: 8px; /* Use margin-left for right-to-left languages */
    padding: 8px 15px;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #e0e0e0;
    color: #333;
    font-size: 14px;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

.period-controls button:last-child {
    margin-left: 0;
}

.period-controls button:hover {
    background-color: #d0d0d0;
}

.period-controls button.active {
    background-color: #ffcc00; /* Amber-like gold */
    font-weight: bold;
    box-shadow: 0 0 8px rgba(255,204,0,0.5);
}


/* Map Points */
.map-point {
    position: absolute;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    border: 3px solid #333;
    cursor: pointer;
    z-index: 10;
    box-shadow: 0 0 8px rgba(0,0,0,0.4);
    transition: transform 0.2s ease, opacity 0.3s ease;
    opacity: 0; /* Hidden by default, JS controls visibility */
    transform: scale(0.8); /* Start slightly smaller */
}

.map-point:hover {
    transform: scale(1.2); /* Scale up on hover */
    border-color: #007bff; /* Highlight color */
}

.map-point.active {
     opacity: 1;
     transform: scale(1); /* Scale to normal size */
}

/* Point Colors */
.map-point.source { background-color: #ff0000; /* Red */ }
.map-point.demand { background-color: #0000ff; /* Blue */ }
.map-point.key-point { background-color: #00cc00; /* Green */ }

/* Point Positioning (adjust based on your specific map image) */
.map-point[data-point="baltic-source"] { top: 8%; left: 65%; } /* Adjusted */
.map-point[data-point="crete"] { top: 75%; left: 70%; }
.map-point[data-point="mycenae"] { top: 70%; left: 65%; }
.map-point[data-point="rome"] { top: 70%; left: 50%; }
.map-point[data-point="egypt"] { top: 85%; left: 75%; }
.map-point[data-point="aquileia"] { top: 60%; left: 50%; }
.map-point[data-point="vienna"] { top: 45%; left: 52%; } /* Adjusted */
.map-point[data-point="maribor"] { top: 55%; left: 51%; } /* Adjusted */
.map-point[data-point="prague"] { top: 40%; left: 58%; } /* New point */


/* Amber Routes */
.amber-route {
    position: absolute;
    background-color: gold; /* Base color */
    z-index: 5; /* Below points, above map */
    opacity: 0; /* Hidden by default */
    pointer-events: none; /* Make them not block clicks on map points initially */
    transition: opacity 0.5s ease; /* Fade in effect */
}

.amber-route.active {
    opacity: 0.7; /* Visible when active */
    pointer-events: auto; /* Allow clicks/hovers when active */
    animation: pulse-glow 2s infinite alternate; /* Subtle animation */
}

/* Pulse/Glow Animation */
@keyframes pulse-glow {
    0% { box-shadow: 0 0 5px gold; }
    100% { box-shadow: 0 0 15px gold, 0 0 10px rgba(255, 215, 0, 0.8); }
}


/* Example Route Styles (using width/height and transform for positioning) */
/* These will need careful positioning and possibly rotation based on actual map */
.amber-route.route-style-1 { /* Baltic to Crete (via East?) */
    top: 10%; left: 65%;
    width: 5%; /* Example width */
    height: 65%; /* Example height */
    transform: rotate(10deg); /* Example rotation */
    transform-origin: top left;
}

.amber-route.route-style-2 { /* Baltic to Mycenae (via Balkan) */
    top: 10%; left: 65%;
    width: 5%;
    height: 60%;
    transform: rotate(-5deg);
    transform-origin: top left;
}

.amber-route.route-style-3 { /* Baltic to Egypt (Bronze) */
     top: 10%; left: 65%;
     width: 8%;
     height: 70%;
     transform: rotate(15deg);
     transform-origin: top left;
}


.amber-route.route-style-4 { /* Baltic to Aquileia (Roman Main) */
    top: 10%; left: 65%;
    width: 4%; /* Thinner, more direct? */
    height: 55%;
    transform: rotate(-2deg);
    transform-origin: top left;
}

.amber-route.route-style-5 { /* Baltic to Rome */
    top: 10%; left: 65%;
    width: 4%;
    height: 60%;
    transform: rotate(0deg);
    transform-origin: top left;
}

.amber-route.route-style-6 { /* Baltic to Egypt (Roman) */
     top: 10%; left: 65%;
     width: 5%;
     height: 75%;
     transform: rotate(8deg);
     transform-origin: top left;
}

/* IMPORTANT: The positioning and dimensions of routes (.route-style-X)
   are *highly* dependent on the exact map image used and will need
   significant manual adjustment to align with the map's geography.
   The current values are placeholders. */


/* Info Panel */
#info-panel {
    position: absolute;
    bottom: 20px;
    left: 20px;
    right: 20px;
    background-color: rgba(255, 255, 255, 0.98);
    border: 1px solid #b0b0b0;
    border-radius: 10px;
    padding: 15px 20px;
    z-index: 20;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    max-height: 180px; /* Slightly taller */
    overflow-y: auto;
    display: none; /* Hidden by default */
    opacity: 0; /* Start transparent for animation */
    transform: translateY(20px); /* Start slightly lower */
    transition: opacity 0.3s ease, transform 0.3s ease;
}

#info-panel.active {
    display: block; /* Make visible before animating */
    opacity: 1;
    transform: translateY(0);
}


#info-panel h3 {
    margin-top: 0;
    margin-bottom: 10px;
    color: #333;
    font-size: 1.2em;
    border-bottom: 1px solid #eee;
    padding-bottom: 8px;
}

#info-panel p {
    margin-bottom: 10px;
    line-height: 1.5;
    color: #555;
    font-size: 0.95em;
}

#info-panel button {
    float: left; /* Align to the left in RTL */
    padding: 5px 12px;
    cursor: pointer;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #eee;
    font-size: 0.9em;
    transition: background-color 0.2s ease;
}

#info-panel button:hover {
     background-color: #ddd;
}

/* Custom Tooltip */
#custom-tooltip {
    position: absolute;
    padding: 5px 10px;
    background-color: rgba(0, 0, 0, 0.7);
    color: #fff;
    border-radius: 4px;
    font-size: 0.8em;
    z-index: 25; /* Above info panel */
    pointer-events: none; /* Doesn't interfere with clicks */
    white-space: nowrap; /* Prevent wrapping */
    display: none; /* Hidden by default */
    transform: translate(-50%, -110%); /* Position above the point */
    transition: opacity 0.2s ease;
    opacity: 0;
}

#custom-tooltip.active {
    display: block; /* Make visible before animating */
    opacity: 1;
}


/* Explanation Section */
#toggle-explanation {
    display: block;
    width: 240px; /* Wider button */
    margin: 30px auto;
    padding: 12px; /* More padding */
    text-align: center;
    cursor: pointer;
    border: none;
    border-radius: 6px;
    background-color: #e0e0e0;
    font-size: 1em;
    font-weight: bold;
    color: #333;
    transition: background-color 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#toggle-explanation:hover {
    background-color: #d0d0d0;
    box-shadow: 0 3px 7px rgba(0,0,0,0.3);
}

#explanation {
    margin-top: 30px;
    padding: 20px;
    border-top: 1px solid #eee;
    line-height: 1.7;
    color: #333;
    background-color: #fcfcfc; /* Slightly different background */
    border-radius: 8px;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
}

#explanation h2 {
    color: #2a5298; /* A historical blue */
    margin-bottom: 15px;
    text-align: center;
}

#explanation ul {
    list-style: disc inside;
    padding-right: 20px; /* Adjust for RTL */
}

#explanation li {
    margin-bottom: 12px; /* More space */
    padding-right: 5px;
}

#explanation strong {
    color: #555;
}


/* Responsive adjustments */
@media (max-width: 600px) {
    #app-container {
        margin: 15px auto;
    }
    .period-controls {
        top: 10px;
        left: 10px;
        padding: 6px;
    }
    .period-controls button {
        margin-left: 4px;
        padding: 5px 10px;
        font-size: 11px;
    }
     .map-point {
        width: 14px;
        height: 14px;
        border-width: 2px;
     }
    #info-panel {
        bottom: 10px;
        left: 10px;
        right: 10px;
        padding: 12px;
        max-height: 100px;
    }
    #info-panel h3 {
        font-size: 1.1em;
    }
    #info-panel p {
        font-size: 0.9em;
    }
     #info-panel button {
        padding: 3px 8px;
        font-size: 0.8em;
     }
     #toggle-explanation {
        width: 180px;
        padding: 10px;
        font-size: 0.9em;
        margin: 20px auto;
     }
      #explanation {
        padding: 15px;
      }
      #explanation h2 {
         font-size: 1.3em;
      }
}
</style>

<button id="toggle-explanation">הצג את סיפורה המלא של דרך הענבר</button>

<div id="explanation" style="display: none;">
    <h2>סיפורה המרתק של דרך הענבר</h2>
    <p>דרך הענבר הייתה הרבה יותר מנתיב סחר; היא הייתה עורק חיים שחיבר עולמות שונים בתכלית, גשר בין הצפון הפראי לדרום המתוחכם. מסעו של גוש ענבר מחופי הים הבלטי הקודרים ועד לצווארי הפרעונים או קיסרי רומא הוא סיפור על הרפתקה, סיכון, תרבות, כלכלה עולמית קדומה וידע שעבר מיד ליד.</p>
    <ul>
        <li><strong>שרף קסום: הענבר כ'זהב הצפוני'.</strong> הענבר הבלטי (סוקיניט), שנוצר משרף עצים מאובן לפני מיליוני שנים, היה נדיר ויקר להפליא בים התיכון. יופיו הייחודי, צבעיו החמים (מצהוב דבש ועד חום עמוק, לעיתים עם חרקים קדמונים כלואים), קלות עיבודו לתכשיטים, ובעיקר תכונותיו האלקטרוסטטיות המסתוריות (שנתפסו כבעלות כוחות ריפוי או קסם) הפכו אותו למוצר יוקרה נחשק ביותר, סמל סטטוס מובהק באליטות של העולם העתיק.</li>
        <li><strong>המעיינות הבלטיים: מקור אוצר טבע.</strong> המקור העשיר והחשוב ביותר לענבר בעת העתיקה היה לאורך החופים הדרומיים והדרום-מזרחיים של הים הבלטי, במיוחד באזור פומרניה ושפך הוויסלה (כיום בפולין ורוסיה/קלינינגרד). הענבר נאסף מהחול לאחר סערות ימיות או נכרה בשכבות רדודות. שליטה על אזורים אלה ונתיבי הגישה אליהם הייתה בעלת חשיבות כלכלית אדירה.</li>
        <li><strong>הביקוש הבלתי-נדלה של הדרום הגדול.</strong> תרבויות מפוארות באגן הים התיכון - מהתרבות המינואית והמיקנית בתקופת הברונזה, דרך מצרים הפרעונית (כפי שמעידים ממצאים בקבר תות ענח' אמון), ועד לשיא הביקוש באימפריה הרומית העצומה - חמדו את הענבר הבלטי. הוא שימש לייצור חרוזים, קמעות, תכשיטים משובצים, קישוטי רהיטים יקרים, ואפילו כמרכיב בתרופות וקטורת.</li>
        <li><strong>מסע של אתגרים וסכנות.</strong> הדרך מהבלטי לים התיכון הייתה מסע עצום ומסוכן באורך של אלפי קילומטרים. היא עברה דרך יערות בתוליים, ביצות טובעניות, נהרות ענקיים (ויסלה, אודר, אלבה, דנובה, דנייפר), רכסי הרים מאתגרים (האלפים, הקרפטים). הסוחרים התמודדו עם שודדים, תנאי מזג אוויר קיצוניים, ומסעות ימיים מסוכנים. ההצלחה הייתה תלויה בשיתוף פעולה, לעיתים כפוי, של שבטים מקומיים לאורך הדרך.</li>
        <li><strong>אבולוציה של נתיבים: מרשתות מוקדמות לדרכים אימפריאליות.</strong> דרך הענבר לא הייתה 'כביש' בודד, אלא רשת דינמית שהשתנתה עם הזמן. בתקופת הברונזה, נתיבים משוערים עברו אולי במזרח אירופה (דרך הנהרות הגדולים לים השחור) או במרכזה, תוך הסתמכות על סחר חליפין בין שבטים. בתקופה הרומית, הנתיב היבשתי הראשי התבסס מאוד, עובר מפומרניה דרך פאנוניה (אוסטריה/הונגריה/סלובניה של היום) אל העיר הרומית המשגשגת אקוויליה בצפון איטליה. נתיב זה נהנה מביטחון יחסי (לפחות בחלקו הדרומי) ומתשתיות מסוימות שהאימפריה הרומית סיפקה.</li>
        <li><strong>יותר מענבר: סחר דו-כיווני והשפעות הדדיות.</strong> דרך הענבר לא שימשה רק להובלת ענבר דרומה. היא הייתה נתיב סחר דו-כיווני פעיל. מהדרום הגיעו לצפון מוצרי יוקרה נחשקים עבור האליטות השבטיות: כלי ברונזה ובדיל איכותיים, כלי זכוכית צבעוניים, מטבעות כסף וזהב, שמן זית, יין, ואריגי מותרות. חילופי סחורות אלה תרמו להתפתחות כלכלית וחברתית של השבטים הצפוניים.</li>
        <li><strong>מעבר לסחורות: זרם של ידע ותרבות.</strong> המפגשים בין עמים לאורך הדרך טיפחו לא רק סחר, אלא גם חילופי רעיונות, טכניקות וידע. שיטות חדשות לעיבוד מתכות, טכנולוגיות חקלאיות, אמונות דתיות, ואף ידע גיאוגרפי עברו לאורך דרך הענבר, והשפיעו על התפתחותן התרבותית של אוכלוסיות רבות, מצפון אירופה ועד הים התיכון.</li>
        <li><strong>עדויות מן העבר: ארכיאולוגיה והיסטוריה.</strong> המידע שאנו יודעים על דרך הענבר מגיע משילוב מרתק של ממצאים ארכיאולוגיים - גושי ענבר מעובד ולא מעובד שנמצאו רחוק ממקורותיהם (למשל, במיקנה, כרתים, מצרים, קברים אטרוסקיים ורומיים), ומוצרי ים תיכוניים שנמצאו באתרים לאורך הנתיבים המשוערים בצפון אירופה - ומקורות היסטוריים כתובים קדומים, כמו תיאוריו של פליניוס הזקן על הענבר ומקורותיו, או אזכורים בספרי גאוגרפיה רומיים.</li>
        <li><strong>שקיעה ושינוי: סופה של הדרך כפי שהכרנוה.</strong> עם שקיעת האימפריה הרומית ונדידת העמים הגדולה, הביטחון היחסי לאורך חלק מנתיבי הענבר התערער. הסחר המאורגן והגדול היקף צומצם או עבר לשליטת גורמים אחרים. למרות שהסחר בענבר מעולם לא פסק לחלוטין בימי הביניים, חשיבותם של הנתיבים היבשתיים הגדולים שדעכה. גילוי נתיבי ים יעילים יותר ושינויים כלכליים נוספים בעולם השפיעו גם הם על אופייה של דרך הענבר, שהפכה לאוסף נתיבים פחות מרכזיים ומאורגנים.</li>
    </ul>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const mapArea = document.getElementById('map-area');
    const infoPanel = document.getElementById('info-panel');
    const infoContent = document.getElementById('info-content');
    const closeInfoButton = document.getElementById('close-info');
    const periodButtons = document.querySelectorAll('.period-controls button');
    const mapPoints = document.querySelectorAll('.map-point');
    const amberRoutes = document.querySelectorAll('.amber-route');
    const customTooltip = document.getElementById('custom-tooltip');

    // --- Utility Functions ---
    function showInfo(content, sourceElement = null) {
        infoContent.textContent = content;
        infoPanel.classList.add('active');
        // Optional: Position panel relative to source? Not needed with current design.
    }

    function hideInfo() {
        infoPanel.classList.remove('active');
        // Use a slight delay to allow animation to finish before clearing content
        setTimeout(() => { infoContent.textContent = ''; }, 300);
    }

    function showTooltip(text, event) {
        customTooltip.textContent = text;
        // Position near the cursor, offset slightly
        customTooltip.style.left = `${event.clientX - mapArea.getBoundingClientRect().left}px`;
        customTooltip.style.top = `${event.clientY - mapArea.getBoundingClientRect().top}px`;
        customTooltip.classList.add('active');
    }

     function hideTooltip() {
        customTooltip.classList.remove('active');
     }

    function filterByPeriod(period) {
        // Hide all points and routes initially (use opacity for smooth transition)
        mapPoints.forEach(point => point.classList.remove('active'));
        amberRoutes.forEach(route => route.classList.remove('active'));

        // Hide info panel and tooltip
        hideInfo();
        hideTooltip();

        // Show relevant points
        mapPoints.forEach(point => {
            const pointPeriods = point.classList; // Contains classes like 'bronze-age', 'roman-era'
            if (period === 'all' || pointPeriods.contains(period)) {
                point.classList.add('active');
            }
        });

        // Show relevant routes with a slight delay or staggered animation
        let delay = 0;
        amberRoutes.forEach(route => {
             const routePeriods = route.classList;
            if (period === 'all' || routePeriods.contains(period)) {
                 setTimeout(() => {
                    route.classList.add('active');
                 }, delay);
                delay += 100; // Stagger the animation start slightly
            }
        });


        // Update button styles
        periodButtons.forEach(btn => btn.classList.remove('active'));
        document.querySelector(`.period-controls button[data-period="${period}"]`).classList.add('active');
    }


    // --- Event Listeners ---

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';

        // Use CSS transitions for smooth height change
        if (isHidden) {
             explanationDiv.style.display = 'block';
             // Force reflow to apply display: block before transition
             explanationDiv.offsetHeight;
             explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 'px'; // Animate to full height
             explanationDiv.style.opacity = 1;
        } else {
             explanationDiv.style.maxHeight = '0'; // Animate to height 0
             explanationDiv.style.opacity = 0;
             // Hide completely after transition
             explanationDiv.addEventListener('transitionend', function handler() {
                 explanationDiv.style.display = 'none';
                 explanationDiv.removeEventListener('transitionend', handler);
             });
        }


        toggleExplanationButton.textContent = isHidden ? 'הסתר את סיפורה המלא של דרך הענבר' : 'הצג את סיפורה המלא של דרך הענבר';
    });

     // Initialize explanation state for transition
     explanationDiv.style.maxHeight = '0';
     explanationDiv.style.opacity = 0;
     explanationDiv.style.overflow = 'hidden';
     explanationDiv.style.transition = 'max-height 0.5s ease-out, opacity 0.5s ease-out';


    // Point click to show info panel
    mapPoints.forEach(point => {
        point.addEventListener('click', () => {
            showInfo(point.dataset.info, point);
            hideTooltip(); // Hide tooltip if panel is shown
        });
         point.addEventListener('mouseover', (e) => {
             showTooltip(point.dataset.info, e);
         });
         point.addEventListener('mousemove', (e) => {
             // Update tooltip position on mouse move
              showTooltip(point.dataset.info, e); // Re-show and reposition
         });
         point.addEventListener('mouseout', () => {
             hideTooltip();
         });
    });

    // Route click (optional - using tooltip for routes for now, or click shows info)
    // Let's make clicking a route also show info for simplicity
     amberRoutes.forEach(route => {
         route.addEventListener('click', () => {
             showInfo(route.dataset.info, route);
              hideTooltip(); // Hide tooltip if panel is shown
         });
         route.addEventListener('mouseover', (e) => {
             showTooltip(route.dataset.info, e);
         });
          route.addEventListener('mousemove', (e) => {
             // Update tooltip position on mouse move
              showTooltip(route.dataset.info, e); // Re-show and reposition
         });
         route.addEventListener('mouseout', () => {
             hideTooltip();
         });
     });


     // Hide info panel on close button click
    closeInfoButton.addEventListener('click', hideInfo);

    // Filter routes and points by period on button click
    periodButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterByPeriod(button.dataset.period);
        });
    });

    // Set initial state (e.g., show 'bronze-age')
    // Find and click the default button
    const initialPeriod = 'bronze-age'; // Or 'all' or 'roman-era'
    const initialPeriodButton = document.querySelector(`.period-controls button[data-period="${initialPeriod}"]`);
    if (initialPeriodButton) {
        initialPeriodButton.click();
    } else if (periodButtons.length > 0) {
         periodButtons[0].click(); // Fallback
    }

    // Adjust tooltip position if it goes off-screen (basic check)
    mapArea.addEventListener('mousemove', (e) => {
        if (customTooltip.classList.contains('active')) {
             const mapRect = mapArea.getBoundingClientRect();
             const tooltipRect = customTooltip.getBoundingClientRect();
             let tooltipX = e.clientX - mapRect.left;
             let tooltipY = e.clientY - mapRect.top;

             // Basic check for right edge
             if (tooltipX + tooltipRect.width > mapRect.width) {
                 tooltipX = mapRect.width - tooltipRect.width - 10; // 10px padding from edge
             }
              // Basic check for top edge (tooltip is above mouse)
              if (tooltipY - tooltipRect.height < 0) {
                   tooltipY = e.clientY - mapRect.top + 25; // Position below mouse if not enough space above
                   customTooltip.style.transform = 'translate(-50%, 10%)'; // Adjust transform
              } else {
                   customTooltip.style.transform = 'translate(-50%, -110%)'; // Default transform above
              }

             customTooltip.style.left = `${tooltipX}px`;
             customTooltip.style.top = `${tooltipY}px`;
        }
    });


});
</script>