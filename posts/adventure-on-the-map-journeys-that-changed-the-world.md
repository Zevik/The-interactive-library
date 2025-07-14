---
title: "הרפתקה על המפה: מסעות ששינו את פני העולם"
english_slug: adventure-on-the-map-journeys-that-changed-the-world
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags:
  - מגלי עולם
  - עידן התגליות
  - קולומבוס
  - מגלן
  - היסטוריה של גאוגרפיה
---
<h1>הרפתקה על המפה: מסעות ששינו את פני העולם</h1>
<p>דמיינו את עצמכם עומדים על סיפון אונייה קטנה, מולכם רק האוקיינוס האינסופי. אין לכם מושג מה מצפה מעבר לאופק, האם תיתקלו בסופות אימתניות, יצורי ים מסתוריים או ארצות חדשות שלא היו מוכרות לאיש באירופה. זו הייתה המציאות של מגלי הארצות הנועזים של "עידן התגליות". המפה האינטראקטיבית הזו מזמינה אתכם להפליג יחד איתם, לעקוב אחר צעדיהם הנועזים על פני כדור הארץ כפי שהם גילו אותו, ולחוות את האתגרים והתגליות שעיצבו את העולם המודרני.</p>

<div class="app-container">
    <div class="controls">
        <h2>צאו למסע! בחרו מגלה ארצות:</h2>
        <label class="checkbox-container columbus">
            <input type="checkbox" data-explorer="columbus">
            <span class="checkmark"></span>
            כריסטופר קולומבוס
            <span class="explorer-name">(מסע ראשון, 1492)</span>
        </label><br>
        <label class="checkbox-container magellan">
             <input type="checkbox" data-explorer="magellan">
             <span class="checkmark"></span>
             פרדיננד מגלן
             <span class="explorer-name">(הקפת העולם, 1519-1522)</span>
        </label>
        <!-- ניתן להוסיף מגלים נוספים בהמשך -->
    </div>
    <div class="map-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Mercator_projection_SW.jpg/1280px-Mercator_projection_SW.jpg" alt="מפת העולם (היטל מרקטור)" class="world-map">
        <svg class="path-overlay"></svg>
        <div class="point-markers"></div>
        <div class="info-box">
            <p class="info-content"></p>
            <button class="close-info" aria-label="סגור">&times;</button>
        </div>
    </div>
</div>

<button id="toggle-explanation">מעוניינים להעמיק? קראו על עידן התגליות והמסעות הגדולים</button>

<div id="explanation" style="display: none;">
    <h2>מסעות ששינו את העולם: מבט על עידן התגליות</h2>

    <h3>עידן התגליות: מבוא להרפתקה</h3>
    <p>בין המאה ה-15 למאה ה-17, אירופה חוותה תקופה של יציאה אל הלא נודע. מגלי ארצות נועזים, ממומנים על ידי ממלכות ששאפו להרחיב את עוצמתן, יצאו למסעות ימיים חסרי תקדים. מטרותיהם היו שאפתניות: למצוא נתיבי סחר חדשים ועשירים למזרח (התבלינים היו שווים זהב!), לגלות מקורות עושר, להפיץ את הדת, ופשוט - למפות את העולם הלא מוכר. מסעות אלו לא היו טיול נופש; הם היו מסע הישרדות יומיומי, רצוף סכנות, מחלות ואי-ודאות מוחלטת.</p>

    <h3>כריסטופר קולומבוס: המסע אל "הודו" במערב</h3>
    <p>כריסטופר קולומבוס, ימאי מג'נובה בשירות מלכי ספרד, היה משוכנע שהוא יכול להגיע למזרח הרחוק בהפלגה מערבה דרך האוקיינוס האטלנטי. הוא האמין שכדור הארץ קטן ממה שחישבו רוב המלומדים בני זמנו. באוגוסט 1492 יצא למסעו הראשון עם שלוש ספינות אגדיות: "סנטה מריה", "פינטה" ו"ניניה". לאחר הפלגה ממושכת ומותחת, ב-12 באוקטובר 1492, הוא דרך על אדמה באזור האיים הקריביים. קולומבוס, שמעולם לא הבין שהגיע ליבשת חדשה ולא לחופי אסיה, פגש באוכלוסיות ילידיות שונות. הוא ערך עוד שלושה מסעות לאזור, חקר איים שונים וקטעים מחופי יבשות אמריקה, ופתח בכך את הדלת לעידן חדש - ורב השפעות - של קשר בין אירופה לאמריקות.</p>

    <h3>פרדיננד מגלן: הראשון שהקיף את העולם</h3>
    <p>פרדיננד מגלן, ימאי פורטוגזי שגם הוא עבר לשרת את ספרד, חלם למצוא את הנתיב הימי המערבי המוביל לאיי התבלינים המפורסמים. בספטמבר 1519 יצא בראש צי של חמש ספינות למסע שיתברר כאחד המופלאים והטרגיים בהיסטוריה. המשלחת התמודדה עם תנאים בלתי נסבלים: רעב, מחלות נוראיות (כמו צפדינה שהפילה חללים רבים), סערות, קור, ותשישות. לאחר חורף קשה ודיכוי מרד, הצליח מגלן באוקטובר 1520 למצוא את המצר הימי בדרום אמריקה (היום מצר מגלן), דרכו עברה המשלחת לאוקיינוס שקט באופן מפתיע, לו קרא מגלן "הים השקט" (האוקיינוס השקט). המסע באוקיינוס זה היה ארוך ומפרך. במרץ 1521 הגיע הצי לפיליפינים, שם נהרג מגלן באפריל בקרב עם מקומיים. הניצולים, תחת פיקודו של חואן סבסטיאן אלקנו, המשיכו במסע ההישרדות דרך דרום מזרח אסיה והאוקיינוס ההודי, הקיפו את יבשת אפריקה דרך כף התקווה הטובה, ולבסוף, בספטמבר 1522, שבו לספרד. רק ספינה אחת, "ויקטוריה", ו-18 אנשי צוות שרדו את המסע הבלתי ייאמן הזה - הקפת העולם הימית הראשונה בהיסטוריה האנושית.</p>

    <h3>ניווט בעולם של סודות: הכלים של המגלים</h3>
    <p>איך ניווטו המגלים האלה בלב ים? הם השתמשו בשילוב של ידע עתיק וטכנולוגיות מתפתחות. המצפן הראה את הכיוון, האצטרולב או הסקסטנט עזרו לחשב קו רוחב באמצעות מיקום הכוכבים או השמש, ושעוני חול מדדו את הזמן. רישום מדויק ביומני הספינה על מהירות וכיוון היה קריטי. ספינות חדשות וחזקות יותר, כמו הקרוולה, אפשרו את המסעות הארוכים באוקיינוס הפתוח. למרות זאת, קביעת קו אורך נותרה חידה כמעט בלתי פתירה, והניווט היה תמיד הימור מסוכן נגד איתני הטבע.</p>

    <h3>מורשת המסעות: עולם שונה לנצח</h3>
    <p>מסעות התגלית היו רגע מכונן בתולדות האנושות. הם לא רק שינו את המפות, אלא את העולם כולו. התוצאה הדרמטית ביותר הייתה "חילופי קולומבוס" - מעבר מסיבי של צמחים (כמו תפוח אדמה ותירס שהגיעו לאירופה), בעלי חיים, מחלות (שהיו קטלניות עבור אוכלוסיות ילידיות באמריקה חסרות החיסון), ורעיונות בין העולם "הישן" (אירופה, אסיה, אפריקה) ל"חדש" (האמריקות). המסעות פתחו את עידן הקולוניאליזם האירופי, שהיה בעל השלכות הרסניות על תרבויות ילידיות ברחבי העולם, אך גם יצר לראשונה קשרים גלובליים בהיקף חסר תקדים. העולם הצטמק, התקשר, ושינה את פניו לנצח.</p>
</div>

<style>
/* כללי */
body {
    font-family: 'Arial', sans-serif; /* Use a common, clean font */
    line-height: 1.6;
    color: #333;
    background-color: #f4f7f6; /* Soft background */
    margin: 0;
    padding: 20px;
}

h1, h2, h3 {
    color: #1a4d2e; /* Deep green */
    text-align: center;
    margin-bottom: 15px;
}

h1 {
    font-size: 2em;
    margin-top: 0;
}

h2 {
    font-size: 1.5em;
    border-bottom: 2px solid #4c944c; /* Green underline */
    padding-bottom: 5px;
    margin-top: 25px;
}

h3 {
    font-size: 1.2em;
    color: #306f30; /* Slightly lighter green */
    margin-top: 20px;
    margin-bottom: 8px;
}

p {
    margin-bottom: 1em;
}

.app-container {
    display: flex;
    flex-direction: column;
    gap: 30px; /* Increased spacing */
    margin: 20px auto;
    max-width: 1000px; /* Wider container */
    background-color: #fff;
    padding: 25px;
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
}

/* בקרה - Controls */
.controls {
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    background-color: #e9f5e9; /* Light green background */
    text-align: center; /* Center control text */
}

.controls h2 {
    margin-bottom: 15px;
    color: #1a4d2e;
    font-size: 1.3em;
}

/* Custom Checkbox Styling */
.checkbox-container {
    display: inline-block; /* Align side by side */
    position: relative;
    padding-right: 35px; /* Space for custom checkbox */
    margin: 0 15px 10px 0; /* Spacing between checkboxes */
    cursor: pointer;
    font-size: 1.1em;
    user-select: none; /* Prevent text selection */
    transition: color 0.3s ease;
    color: #555;
}

.checkbox-container input[type="checkbox"] {
    position: absolute;
    opacity: 0; /* Hide default checkbox */
    cursor: pointer;
    height: 0;
    width: 0;
}

.checkmark {
    position: absolute;
    top: 0;
    right: 0;
    height: 22px;
    width: 22px;
    background-color: #eee;
    border: 2px solid #ccc;
    border-radius: 4px;
    transition: background-color 0.3s ease, border-color 0.3s ease;
}

/* Hover and Checked States */
.checkbox-container:hover input ~ .checkmark {
    background-color: #ccc;
}

.checkbox-container input:checked ~ .checkmark {
    background-color: #4CAF50; /* Green check */
    border-color: #4CAF50;
}

/* Checkmark Icon */
.checkmark:after {
    content: "";
    position: absolute;
    display: none;
    right: 7px;
    top: 3px;
    width: 5px;
    height: 10px;
    border: solid white;
    border-width: 0 3px 3px 0;
    transform: rotate(45deg);
}

/* Show checkmark when checked */
.checkbox-container input:checked ~ .checkmark:after {
    display: block;
}

.checkbox-container.columbus input:checked ~ .checkmark { background-color: #007bff; border-color: #007bff; } /* Blue */
.checkbox-container.magellan input:checked ~ .checkmark { background-color: #dc3545; border-color: #dc3545; } /* Red */
.checkbox-container.columbus:hover { color: #007bff; }
.checkbox-container.magellan:hover { color: #dc3545; }
.checkbox-container.columbus input:checked { color: #007bff; }
.checkbox-container.magellan input:checked { color: #dc3545; }


.explorer-name {
    font-size: 0.9em;
    color: #666;
    margin-right: 5px;
}


/* מפה - Map */
.map-container {
    position: relative;
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Subtle inner shadow */
    background-color: #a8d8ff; /* Ocean blue placeholder */
}

.world-map {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    user-drag: none; /* Prevent dragging image */
    user-select: none; /* Prevent selecting image */
}

.path-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none; /* Allow clicks to pass through */
    overflow: visible;
}

.path-overlay path {
    fill: none;
    stroke-width: 4px; /* Thicker lines */
    /* stroke-dasharray: 5, 5; */ /* Removed dashed for continuous animation */
    stroke-linecap: round; /* Rounded ends */
    transition: stroke-dashoffset 2s ease-in-out; /* Smoother animation */
}

.point-markers {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.point-marker {
    position: absolute;
    width: 16px; /* Larger marker */
    height: 16px;
    background-color: yellow; /* Default */
    border: 3px solid #fff; /* White border */
    border-radius: 50%;
    transform: translate(-50%, -50%);
    cursor: pointer;
    z-index: 10;
    box-shadow: 0 0 8px rgba(0,0,0,0.4); /* Stronger shadow */
    opacity: 0; /* Start hidden for animation */
    transition: opacity 0.5s ease, transform 0.3s ease;
}

.point-marker:hover {
     transform: translate(-50%, -50%) scale(1.3); /* Scale on hover */
     box-shadow: 0 0 12px rgba(0,0,0,0.6);
}

.point-marker.columbus { background-color: #007bff; } /* Blue */
.point-marker.magellan { background-color: #dc3545; } /* Red */
.point-marker.visible { opacity: 1; } /* Class added by JS */


/* Info Box */
.info-box {
    position: absolute;
    background-color: rgba(255, 255, 255, 0.98); /* More opaque white */
    border: 1px solid #bbb;
    border-radius: 8px; /* More rounded */
    padding: 15px; /* More padding */
    max-width: 250px; /* Wider */
    z-index: 20;
    /* transform handled by JS */
    pointer-events: all;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2); /* Better shadow */
    font-size: 0.95em;
    line-height: 1.5;
    display: none; /* Hidden by default */
    opacity: 0; /* For fade-in animation */
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.info-box.visible {
    display: block; /* Make block for transition */
    opacity: 1;
}


.info-box::after { /* Arrow */
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-top: 10px solid rgba(255, 255, 255, 0.98); /* Match background */
}

.info-box .close-info {
    position: absolute;
    top: 5px;
    left: 8px; /* Position on the left for RTL */
    font-size: 1.5em; /* Larger close button */
    font-weight: bold;
    cursor: pointer;
    color: #777;
    background: none;
    border: none;
    padding: 0;
    line-height: 1;
    transition: color 0.2s ease;
}
.info-box .close-info:hover {
    color: #333;
}


/* לחצן הצגת הסבר */
#toggle-explanation {
    display: block;
    margin: 30px auto 20px; /* More space */
    padding: 12px 20px; /* Larger padding */
    font-size: 1.1em;
    cursor: pointer;
    border: 1px solid #1a4d2e; /* Green border */
    border-radius: 6px;
    background-color: #4c944c; /* Green background */
    color: white; /* White text */
    transition: background-color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#toggle-explanation:hover {
    background-color: #306f30; /* Darker green on hover */
    border-color: #306f30;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

#toggle-explanation:active {
     background-color: #1a4d2e;
     box-shadow: inset 0 2px 5px rgba(0,0,0,0.3);
}


/* הסבר - Explanation */
#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    background-color: #fff;
    line-height: 1.7; /* Improved readability */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Soft shadow */
}

#explanation h2, #explanation h3 {
    text-align: right; /* Align explanation headings right */
}

#explanation h3 {
    border-bottom: 1px solid #e0e0e0; /* Subtle underline */
    padding-bottom: 5px;
    margin-bottom: 10px;
}

#explanation p {
    text-align: justify; /* Justify text for cleaner look */
    margin-bottom: 1.2em;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .app-container {
        padding: 15px;
        gap: 20px;
    }

    .controls {
        padding: 15px;
    }

    .controls h2 {
        font-size: 1.2em;
    }

    .checkbox-container {
        display: block; /* Stack checkboxes on small screens */
        margin: 0 auto 10px;
        padding-right: 30px;
        text-align: right;
        width: fit-content; /* Prevent full width */
    }

     .checkmark {
         height: 20px;
         width: 20px;
         right: 0;
     }
     .checkmark:after {
         right: 6px;
         top: 2px;
         width: 4px;
         height: 8px;
     }


    .info-box {
        max-width: 80%; /* Max width relative to container */
        padding: 10px;
        font-size: 0.9em;
    }

    #toggle-explanation {
        font-size: 1em;
        padding: 10px 15px;
    }

    #explanation {
        padding: 15px;
    }

    h1 { font-size: 1.6em; }
    h2 { font-size: 1.3em; }
    h3 { font-size: 1.1em; }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const mapContainer = document.querySelector('.map-container');
    const svgOverlay = mapContainer.querySelector('.path-overlay');
    const pointMarkersDiv = mapContainer.querySelector('.point-markers');
    const infoBox = mapContainer.querySelector('.info-box');
    const infoContent = infoBox.querySelector('.info-content');
    const closeInfoButton = infoBox.querySelector('.close-info');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explorerCheckboxes = document.querySelectorAll('.controls input[type="checkbox"]');
    const worldMapImg = mapContainer.querySelector('.world-map');

    // Data with percentage coordinates (relative to map image size)
    const explorerData = {
        columbus: {
            name: 'כריסטופר קולומבוס',
            color: '#007bff', // Blue
            path: [
                {x: 20, y: 50}, // Spain (approx)
                {x: 25, y: 55}, // Canary Islands
                {x: 40, y: 60}, // Mid-Atlantic
                {x: 58, y: 68}, // Bahamas/Cuba region
                {x: 45, y: 55}, // Azores/Return path
                {x: 20, y: 50}  // Back to Spain (approx)
            ],
            points: [
                {x: 20, y: 50, info: 'אוגוסט 1492: יציאה מספרד בראש 3 ספינות.', date: '1492-08', delay: 0}, // Delay in ms
                {x: 25, y: 55, info: 'ספטמבר 1492: עצירת התארגנות באיים הקנריים.', date: '1492-09', delay: 1000},
                {x: 58, y: 68, info: '12 באוקטובר 1492: הגעה היסטורית לאי בגני הבאהמה (סן סלבדור).', date: '1492-10-12', delay: 4000},
                {x: 60, y: 70, info: 'דצמבר 1492: חקר קובה והיספניולה.', date: '1492-12', delay: 5500},
                {x: 20, y: 50, info: 'מרץ 1493: שיבה נרגשת לספרד.', date: '1493-03', delay: 7000}
            ]
        },
        magellan: {
            name: 'פרדיננד מגלן',
            color: '#dc3545', // Red
            path: [
                {x: 20, y: 50}, // Spain
                {x: 25, y: 60}, // Canary Islands
                {x: 30, y: 80}, // Coast of Brazil/Argentina
                {x: 35, y: 90}, // Strait of Magellan area
                {x: 50, y: 70}, // South Pacific
                {x: 70, y: 55}, // Guam
                {x: 80, y: 65}, // Philippines (Magellan dies here)
                {x: 70, y: 60}, // Borneo/Spice Islands area
                {x: 50, y: 75}, // Across Indian Ocean
                {x: 30, y: 85}, // Cape of Good Hope
                {x: 20, y: 50}  // Back to Spain (Elcano arrives)
            ],
            points: [
                {x: 20, y: 50, info: 'ספטמבר 1519: יציאה מספרד בראש חמש ספינות למסע הבלתי נודע.', date: '1519-09', delay: 0},
                {x: 30, y: 80, info: '1520: חורף קשה בדרום אמריקה ודיכוי מרד קצינים.', date: '1520', delay: 2000},
                {x: 35, y: 90, info: 'אוקטובר 1520: גילוי ומעבר במצר ההיסטורי (מצר מגלן).', date: '1520-10', delay: 4000},
                {x: 50, y: 70, info: 'נובמבר 1520 - מרץ 1521: מסע מפרך ראשון באוקיינוס השקט ("הים השקט").', date: '1521-03', delay: 6000},
                {x: 70, y: 55, info: 'מרץ 1521: הגעה לגואם, טעינת אספקה נואשת.', date: '1521-03', delay: 8000},
                {x: 80, y: 65, info: 'אפריל 1521: מגלן נהרג בקרב בפיליפינים. חואן סבסטיאן אלקנו ממשיך את הפיקוד.', date: '1521-04', delay: 10000},
                {x: 70, y: 60, info: 'נובמבר 1521: הגעה ליעד - איי התבלינים!', date: '1521-11', delay: 12000},
                {x: 30, y: 85, info: 'מאי 1522: הקפת כף התקווה הטובה בדרך הביתה.', date: '1522-05', delay: 14000},
                {x: 20, y: 50, info: '6 בספטמבר 1522: הספינה היחידה, ויקטוריה, שבה לספרד והשלימה את הקפת העולם!', date: '1522-09-06', delay: 16000}
            ]
        }
    };

    let activeAnimations = {}; // To keep track of animation timeouts

    function getMapDimensions() {
        return {
            width: mapContainer.offsetWidth,
            height: mapContainer.offsetHeight
        };
    }

    function drawPath(explorerKey) {
        const data = explorerData[explorerKey];
        const dimensions = getMapDimensions();
        const pathElement = document.createElementNS('http://www.w3.org/2000/svg', 'path');

        let d = '';
        if (data.path && data.path.length > 0) {
            // Convert percentage coordinates to pixel coordinates
            const pixelPath = data.path.map(p => ({
                x: (p.x / 100) * dimensions.width,
                y: (p.y / 100) * dimensions.height
            }));

            d = `M ${pixelPath[0].x},${pixelPath[0].y}`;
            for (let i = 1; i < pixelPath.length; i++) {
                d += ` L ${pixelPath[i].x},${pixelPath[i].y}`;
            }
        }

        pathElement.setAttribute('d', d);
        pathElement.setAttribute('stroke', data.color);
        pathElement.classList.add('explorer-path');
        pathElement.setAttribute('data-explorer', explorerKey);

        // Animation: Draw the path gradually
        const pathLength = pathElement.getTotalLength();
        pathElement.style.strokeDasharray = pathLength + ' ' + pathLength;
        pathElement.style.strokeDashoffset = pathLength;

        // Force reflow to make transition work
        pathElement.getBoundingClientRect();

        requestAnimationFrame(() => {
             pathElement.style.strokeDashoffset = '0';
             // Set a unique key for this animation
             activeAnimations[explorerKey] = setTimeout(() => {
                 // Animation complete, add points
                 addPoints(explorerKey);
             }, 2000); // Match CSS transition duration
        });

        svgOverlay.appendChild(pathElement);
    }

    function addPoints(explorerKey) {
        const data = explorerData[explorerKey];

        if (data.points) {
            data.points.forEach(point => {
                 // Use setTimeout to sequence point appearance based on delay
                 const timeoutId = setTimeout(() => {
                     const pointElement = document.createElement('div');
                     pointElement.classList.add('point-marker', explorerKey);
                     pointElement.style.left = `${point.x}%`;
                     pointElement.style.top = `${point.y}%`;
                     pointElement.setAttribute('data-info', point.info);

                      // Force reflow before adding 'visible' class for transition
                      pointElement.getBoundingClientRect();
                      pointElement.classList.add('visible'); // Trigger fade-in

                     pointElement.addEventListener('click', () => {
                         showInfoBox(point.info, point.x, point.y);
                     });

                     pointMarkersDiv.appendChild(pointElement);
                 }, point.delay || 0); // Use defined delay or 0

                 // Store timeout ID to clear later if needed
                 if (!activeAnimations[explorerKey]) activeAnimations[explorerKey] = [];
                 activeAnimations[explorerKey].push(timeoutId);
            });
        }
    }

    function removePath(explorerKey) {
        const path = svgOverlay.querySelector(`.explorer-path[data-explorer="${explorerKey}"]`);
        if (path) {
             // Clear any pending point animations for this explorer
             if (activeAnimations[explorerKey]) {
                 if (Array.isArray(activeAnimations[explorerKey])) {
                      activeAnimations[explorerKey].forEach(id => clearTimeout(id));
                 } else { // It's the path animation timeout
                      clearTimeout(activeAnimations[explorerKey]);
                 }
                 delete activeAnimations[explorerKey];
             }


             // Animate path disappearance (reverse drawing)
             const pathLength = path.getTotalLength();
             // Ensure dasharray is set correctly before animating offset
             path.style.strokeDasharray = pathLength + ' ' + pathLength;
             // Start from current offset (likely 0 if animation completed)
             path.style.strokeDashoffset = path.style.strokeDashoffset === '0' ? '0' : path.style.strokeDashoffset;

              requestAnimationFrame(() => {
                 requestAnimationFrame(() => {
                      path.style.strokeDashoffset = pathLength; // Animate to hide
                 });
            });

             // Remove after animation
             setTimeout(() => {
                 path.remove();
             }, 2000); // Match transition duration
        }
    }

    function removePoints(explorerKey) {
        pointMarkersDiv.querySelectorAll(`.point-marker.${explorerKey}`).forEach(marker => {
            marker.classList.remove('visible'); // Trigger fade-out
            // Remove after fade-out animation
            setTimeout(() => {
                marker.remove();
            }, 500); // Match transition duration
        });
        // Check if the currently visible info box belongs to a point being removed
        if (infoBox.classList.contains('visible')) {
             const currentPointInfo = infoContent.textContent;
             const pointsToRemoveInfo = explorerData[explorerKey].points.map(p => p.info);
             if (pointsToRemoveInfo.includes(currentPointInfo)) {
                  hideInfoBox();
             }
        }
    }

    function showInfoBox(info, x, y) {
        infoContent.textContent = info;
        const dimensions = getMapDimensions();
        const pixelX = (x / 100) * dimensions.width;
        const pixelY = (y / 100) * dimensions.height;

        // Position the info box initially near the point
        infoBox.style.left = `${pixelX}px`;
        infoBox.style.top = `${pixelY}px`;
        // Apply base transform for positioning above the point
        infoBox.style.transform = 'translate(-50%, -100%)';

        // Use requestAnimationFrame to allow CSS transition
        requestAnimationFrame(() => {
            infoBox.classList.add('visible'); // Trigger opacity/transform transition
        });

        // --- Basic Position Adjustment (Optional but good for robustness) ---
        // Wait for the box to be visible and rendered to get its actual dimensions
        setTimeout(() => {
             const boxRect = infoBox.getBoundingClientRect();
             const containerRect = mapContainer.getBoundingClientRect();

             let adjustedLeft = pixelX;
             let adjustedTop = pixelY;

             // Check horizontal bounds
             if (boxRect.left < containerRect.left) {
                 adjustedLeft = pixelX + (containerRect.left - boxRect.left) + 10; // Push right, add padding
             }
             if (boxRect.right > containerRect.right) {
                 adjustedLeft = pixelX - (boxRect.right - containerRect.right) - 10; // Push left, add padding
             }

             // Check vertical bounds (for info box *above* point)
             if (boxRect.top < containerRect.top) {
                 // If the box is going off the top, we might need to reposition below
                 // This requires changing the arrow direction and transform.
                 // For simplicity, if it hits the top, just slightly adjust or prevent going off left/right.
                 // A more complex solution would check if placing below is better.
                 // For now, just ensure horizontal bounds are respected even if vertically clipped slightly.
             }


             // Re-apply position based on potential adjustments, keeping the translate for centering
             infoBox.style.left = `${adjustedLeft}px`;
             infoBox.style.top = `${adjustedTop}px`;
             infoBox.style.transform = 'translate(-50%, -100%)'; // Maintain transform relative to the point

             // Ensure arrow stays centered under the adjusted box position (this is tricky)
             // For this simple implementation, the arrow stays visually centered under the *initial* click point.
             // A more advanced solution would calculate the arrow position based on the final box position relative to the point.

        }, 0); // Use a small timeout to wait for render calculation
         // --- End Adjustment ---
    }

    function hideInfoBox() {
        infoBox.classList.remove('visible'); // Trigger fade-out
        // Use setTimeout to hide display: none after transition
        setTimeout(() => {
             infoBox.style.display = 'none';
             // Reset transform to base for next appearance
             infoBox.style.transform = 'translate(-50%, -100%)';
        }, 300); // Match CSS transition duration
    }

    // Event Listeners
    explorerCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', (event) => {
            const explorerKey = event.target.dataset.explorer;
            if (event.target.checked) {
                 // Draw after map image is loaded or on load if already loaded
                 if (worldMapImg.complete) {
                      drawPath(explorerKey);
                 } else {
                      // Use a flag or check again in load listener
                      worldMapImg.addEventListener('load', () => {
                           if (event.target.checked) { // Check if it's *still* checked
                                drawPath(explorerKey);
                           }
                      }, { once: true }); // Run only once for this specific load event
                 }
            } else {
                removePath(explorerKey);
                removePoints(explorerKey); // Remove points immediately when unchecked
                hideInfoBox(); // Ensure info box is hidden if path/points removed
            }
        });
    });

    closeInfoButton.addEventListener('click', hideInfoBox);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';

        // Add simple slide/fade animation
        if (isHidden) {
             explanationDiv.style.opacity = '0';
             explanationDiv.style.maxHeight = '0';
             explanationDiv.style.overflow = 'hidden';
             explanationDiv.style.display = 'block';

             // Force reflow
             explanationDiv.getBoundingClientRect();

             requestAnimationFrame(() => {
                 explanationDiv.style.transition = 'opacity 0.5s ease-out, max-height 0.5s ease-out';
                 explanationDiv.style.opacity = '1';
                 explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 'px'; // Set to full height
             });

        } else {
             explanationDiv.style.transition = 'opacity 0.5s ease-out, max-height 0.5s ease-out';
             explanationDiv.style.opacity = '0';
             explanationDiv.style.maxHeight = '0';

             setTimeout(() => {
                 explanationDiv.style.display = 'none';
                 explanationDiv.style.transition = ''; // Reset transition
                 explanationDiv.style.maxHeight = ''; // Remove inline style
             }, 500); // Match transition duration
        }

        toggleExplanationButton.textContent = isHidden ? 'הסתרת ההסבר' : 'מעוניינים להעמיק? קראו על עידן התגליות והמסעות הגדולים';
    });

    // Hide info box if clicking anywhere on the map container itself, but not on a marker or the info box
     mapContainer.addEventListener('click', (event) => {
         // Check if the click target or any of its ancestors is a point marker or the info box
         if (!event.target.closest('.point-marker') && !event.target.closest('.info-box')) {
             hideInfoBox();
         }
     });

     // Initial setup if map is already loaded
     if (worldMapImg.complete) {
        // If map is cached, handle initial checked boxes on load
         explorerCheckboxes.forEach(checkbox => {
             if (checkbox.checked) {
                 drawPath(checkbox.dataset.explorer);
             }
         });
     } else {
          // Ensure paths/points are drawn if map loads *after* DOMContentLoaded
         worldMapImg.addEventListener('load', () => {
              explorerCheckboxes.forEach(checkbox => {
                 if (checkbox.checked) {
                     drawPath(checkbox.dataset.explorer);
                 }
             });
         });
     }


     // Handle potential map resize (redraw on window resize END)
     let resizeTimer;
     window.addEventListener('resize', () => {
         clearTimeout(resizeTimer);
         resizeTimer = setTimeout(() => {
             // Clear all current animations and elements
             svgOverlay.innerHTML = ''; // Clear SVG
             pointMarkersDiv.innerHTML = ''; // Clear markers
             hideInfoBox();
             for (const key in activeAnimations) {
                  if (Array.isArray(activeAnimations[key])) {
                      activeAnimations[key].forEach(id => clearTimeout(id));
                  } else {
                      clearTimeout(activeAnimations[key]);
                  }
             }
             activeAnimations = {};


             // Redraw all currently visible paths and points based on checked boxes
             explorerCheckboxes.forEach(checkbox => {
                 if (checkbox.checked) {
                     // Redraw path, points will be added after path animation completes
                     drawPath(checkbox.dataset.explorer);
                 }
             });
         }, 250); // Wait 250ms after resize stops
     });

     // Initial check for explanation state (if it was set to block initially for some reason)
     if (explanationDiv.style.display !== 'none') {
          toggleExplanationButton.textContent = 'הסתרת ההסבר';
     }


});
</script>