---
title: "כדור הארץ המגנטי: מסע מרתק אל נדידת הקטבים"
english_slug: magnetic-earth-pole-wandering
category: "מדעי הסביבה / כדור הארץ"
tags:
  - מגנטיות
  - גיאופיזיקה
  - קטבים מגנטיים
  - נדידת קטבים
  - שדה מגנטי של כדור הארץ
---
# כדור הארץ המגנטי: מסע מרתק אל נדידת הקטבים

דמיינו שהמצפן שלכם הוא רק רמז, לא יעד מדויק. ידעתם שהנקודה אליה מצביע המצפן שלכם – הקוטב הצפוני המגנטי – נמצאת בתנועה מתמדת? כן, ממש כך, היא נודדת על פני הגלובוס שנה אחר שנה! בואו נצא למסע אינטראקטיבי כדי לחזות בתנועה המסתורית הזו, להבין מה גורם לה, ואיך היא משפיעה על העולם שלנו.

<div class="interactive-container">
    <div id="map-container">
        <!-- World map image centered on the Arctic region or suitable Mercator -->
        <!-- Using the provided image, assuming the coordinate logic aligns reasonably -->
        <img id="world-map" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mercator_projection_SW.svg/1024px-Mercator_projection_SW.svg.png" alt="מפת עולם עם דגש על חצי הכדור הצפוני" style="width: 100%; height: 100%; object-fit: cover;">

        <!-- Geographic North Pole (Fixed) -->
        <div id="geographic-north-pole" class="pole-marker geographic" title="הקוטב הצפוני הגיאוגרפי (ציר הסיבוב - קבוע)">
             <span class="marker-label">צפון גיאוגרפי</span>
        </div>

        <!-- Magnetic North Pole (Dynamic) -->
        <div id="magnetic-north-pole" class="pole-marker magnetic" title="הקוטב הצפוני המגנטי (יעד המצפנים - נודד)">
            <span class="marker-label">צפון מגנטי</span>
        </div>

        <!-- SVG for drawing the path -->
        <svg id="pole-path-svg"></svg>
    </div>

    <div id="controls">
        <div id="year-display">שנה: 1900</div>
        <input type="range" id="year-slider" min="1900" max="2023" value="1900" step="0.5"> <!-- Increased granularity -->
        <div class="control-buttons">
             <button id="play-pause-button">▶ נגן</button>
             <button id="step-back-button" title="שנה אחת אחורה">-1 שנה</button>
             <button id="step-forward-button" title="שנה אחת קדימה">+1 שנה</button>
        </div>
    </div>
</div>

<button id="toggle-explanation">מה עומד מאחורי התנועה הזו? הצג הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>מסע אל לב כדור הארץ: סוד השדה המגנטי ונדידת הקטבים</h2>

    <h3>מנוע הדינמו הפלנטרי: הולדת השדה המגנטי</h3>
    כדור הארץ אינו רק סלע גדול בחלל; הוא גם מגנט ענק! השדה המגנטי העוצמתי שעוטף את הפלנטה שלנו, המכונה המגנטוספרה, הוא שריון בלתי נראה המגן עלינו מפני קרינה קוסמית וחלקיקים טעונים מהשמש. שלא כמו מגנט קבוע, השדה שלנו נוצר על ידי תהליך דינמי ומורכב בלב כדור הארץ: תנועת מתכת מותכת (בעיקר ברזל וניקל) בגלעין החיצוני הנוזלי. זרמים ענקיים אלו יוצרים אפקט של "דינמו" – בדומה למחולל חשמלי – המייצר שדה מגנטי משתנה.

    <h3>הניווט הקוסמי: קטבים גיאוגרפיים מול מגנטיים</h3>
    חשוב להבדיל בין הצפון/דרום הגיאוגרפי לבין הצפון/דרום המגנטי. הקטבים הגיאוגרפיים הם נקודות קבועות לחלוטין: אלו הקצוות הצפוני והדרומי של ציר הסיבוב של כדור הארץ. לעומת זאת, הקטבים המגנטיים הם הנקודות על פני השטח שבהן קווי השדה המגנטי נכנסים (בצפון המגנטי) או יוצאים (בדרום המגנטי) כמעט אנכית. נקודות אלו אינן יציבות והן זזות ללא הפסקה. לכן, המצפן המגנטי שלכם (שמצביע לאורך קווי השדה) לא תמיד מצביע בדיוק לצפון הגיאוגרפי האמיתי.

    <h3>הריקוד הגעשי: למה הקטבים המגנטיים נודדים?</h3>
    התנועה שצפיתם בה באינטראקטיב היא תופעת 'נדידת הקטבים' המגנטיים. היא תוצאה ישירה של ה"סערה" הבלתי פוסקת בגלעין החיצוני הנוזלי. הזרמים הקונבקטיביים בברזל המותך משתנים כל הזמן בעוצמה ובכיוון, ושינויים אלו משפיעים באופן ישיר על השדה המגנטי כולו – ועל מיקום הקטבים המגנטיים על פני השטח. זהו ריקוד אדיר ממדים המתרחש אלפי קילומטרים מתחת לרגלינו!

    <h3>קצב מהיר להפליא: התנועה המואצת בעשורים האחרונים</h3>
    נדידת הקטבים אינה אחידה. למעשה, בעשורים האחרונים, ובמיוחד מאז שנות ה-90, אנו עדים להאצה דרמטית בתנועת הקוטב הצפוני המגנטי. אם בעבר הוא נע בקצב של כ-10-15 ק"מ בשנה, כיום הקצב מגיע לכ-50-60 ק"מ בשנה! הוא עשה את דרכו מקנדה לכיוון סיביר, וחצה את קו התאריך הבינלאומי המגנטי בסביבות שנת 2020. זוהי עדות לשינויים משמעותיים המתרחשים כעת עמוק בתוך הפלנטה.

    <h3>עיניים בשמיים ועל הקרקע: איך עוקבים אחרי התנועה?</h3>
    אנו לא משאירים את תנועת הקטבים בגדר תעלומה. מדענים עוקבים אחריה באמצעות שילוב של טכניקות:
    *   **מסעות חקר היסטוריים:** תיעוד מיקום הקוטב החל מהמאה ה-19.
    *   **רשת מגנומטרים גלובלית:** תחנות קרקע שמודדות את השדה המגנטי ברציפות.
    *   **לוויינים מיוחדים:** לוויינים כמו סדרת Swarm של ESA מספקים נתונים מדויקים על השדה המגנטי מכל פינה בכדור הארץ, ומאפשרים בניית מודלים עדכניים ותחזיות.

    <h3>השפעות בעולם האמיתי: מניווט ועד נדידת בעלי חיים</h3>
    למרות שנדידת הקטבים אינה גורמת לרעידות אדמה או אסונות מיידיים, יש לה השלכות:
    *   **ניווט:** מערכות ניווט המסתמכות על המצפן המגנטי (כמו מפות טיסה וימיות מסוימות) דורשות עדכונים תכופים. מערכות GPS מודרניות אינן מושפעות, אך ניווט מגנטי עדיין חשוב במקרי חירום או כגיבוי.
    *   **ביולוגיה:** יצורים רבים, מציפורים נודדות ועד צבי ים, משתמשים בשדה המגנטי של כדור הארץ כחלק ממערכת הניווט הפנימית שלהם. שינויים בשדה עשויים להשפיע על מסלולי ההגירה שלהם.

    <h3>רמז לאירועים גדולים יותר: היפוכי קטבים</h3>
    נדידת הקטבים הנוכחית היא חלק מתהליך רחב יותר שיכול להוביל (בסולם זמן גיאולוגי של אלפי שנים) גם להיפוך קטבים מגנטי. היפוך קוטב הוא אירוע דרמטי בו הקוטב הצפוני המגנטי והדרומי המגנטי מחליפים מקומות. אירועים כאלו קרו פעמים רבות בהיסטוריה של כדור הארץ (יש לכך עדויות בסלעים געשיים ומשקעים ימיים). נדידת הקטבים המואצת אינה אינדיקציה מיידית להיפוך, אך היא בהחלט תזכורת לשדה המגנטי הדינמי והמשתנה שלנו.

</div>

<style>
/* גופנים בסיסיים וצבעים */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f7f6; /* רקע עדין לגוף העמוד */
}

h1, h2, h3 {
    color: #004080; /* כותרות בצבע כחול כהה */
    margin-bottom: 15px;
}

/* עיצוב הקונטיינר האינטראקטיבי */
.interactive-container {
    margin: 30px auto; /* ריווח עליון/תחתון גדול יותר */
    max-width: 850px; /* רוחב מקסימלי מעט גדול יותר */
    border: none; /* מסגרת הוסרה לטובת צל */
    border-radius: 12px; /* פינות מעוגלות יותר */
    padding: 20px; /* ריפוד פנימי גדול יותר */
    background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* רקע עם גרדיאנט עדין */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* צל בולט יותר */
    text-align: center;
    overflow: hidden; /* לוודא שום דבר לא יוצא */
    position: relative; /* לטובת אנימציות רקע אם נדרש */
}

/* מיכל המפה */
#map-container {
    width: 100%;
    height: 550px; /* גובה מפה מותאם */
    position: relative;
    overflow: hidden;
    margin-bottom: 20px; /* ריווח מהבקרים */
    border-radius: 8px; /* פינות מעוגלות למפה */
    background-color: #e0f2f7; /* רקע למקרה שהתמונה לא נטענת */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* צל עדין למפה */
}

#world-map {
    display: block;
    user-drag: none;
    user-select: none;
    -moz-user-select: none;
    -webkit-user-drag: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    /* לוודא שהתמונה מכסה את כל הקונטיינר ללא מריחה */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    object-fit: cover; /* חשוב לשמירה על יחס גובה-רוחב */
}

/* סמני הקטבים */
.pole-marker {
    position: absolute;
    width: 24px; /* גודל סמן גדול יותר */
    height: 24px; /* גודל סמן גדול יותר */
    border-radius: 50%;
    z-index: 10;
    transform: translate(-50%, -50%); /* מרכוז הסמן */
    border: 3px solid rgba(255, 255, 255, 0.8); /* מסגרת בהירה ובולטת */
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.5); /* צל סמן בולט יותר */
    transition: left 0.5s ease-out, top 0.5s ease-out; /* אנימציית תנועה חלקה */
    display: flex; /* כדי למרכז את התווית */
    justify-content: center;
    align-items: center;
    font-size: 10px; /* גודל פונט קטן לתווית */
    font-weight: bold;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5); /* צל לטקסט התווית */
    cursor: pointer; /* סימן שהאלמנט אינטראקטיבי (למרות שאין קליק) */
}

/* אנימציית פעימה עדינה לסמנים */
.pole-marker::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: inherit; /* צבע רקע כמו הסמן */
    opacity: 0.7;
    transform: translate(-50%, -50%) scale(1);
    animation: pulse 2s infinite ease-out; /* אנימציית פעימה */
    z-index: -1; /* מתחת לסמן עצמו */
}

@keyframes pulse {
    0% { transform: translate(-50%, -50%) scale(1); opacity: 0.7; }
    50% { transform: translate(-50%, -50%) scale(1.5); opacity: 0.2; }
    100% { transform: translate(-50%, -50%) scale(1); opacity: 0.7; }
}


.pole-marker.geographic {
    background-color: #e74c3c; /* אדום בולט יותר */
}

.pole-marker.magnetic {
    background-color: #3498db; /* כחול בולט יותר */
}

.pole-marker .marker-label {
     position: absolute;
     bottom: -20px; /* מיקום התווית מתחת לסמן */
     left: 50%;
     transform: translateX(-50%);
     white-space: nowrap; /* למנוע שבירת שורה */
     font-size: 12px;
     font-weight: normal;
     color: #333;
     text-shadow: none;
}


/* שביל התנועה */
#pole-path-svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 5;
    pointer-events: none; /* מאפשר קליקים דרך ה-SVG */
}

#pole-path-svg polyline {
    fill: none;
    stroke: #3498db; /* צבע השביל כצבע הסמן המגנטי */
    stroke-width: 3; /* עובי שביל גדול יותר */
    opacity: 0.9; /* אטימות גבוהה יותר */
    stroke-linecap: round; /* קצוות קווים מעוגלים */
    stroke-linejoin: round; /* חיבורי קווים מעוגלים */
    /* ניתן להוסיף אנימציה כאן אם נדרש, אך זה דורש חישוב אורך המסלול */
}


/* בקרות */
#controls {
    margin-top: 15px;
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.7); /* רקע שקוף עדין לבקרות */
    border-radius: 8px;
    display: flex; /* פריסה גמישה לשליטה באלמנטים */
    flex-direction: column; /* סידור אנכי */
    align-items: center; /* מרכוז אופקי */
}

#year-display {
    margin-bottom: 10px; /* ריווח מהסליידר */
    font-size: 1.2em; /* גודל פונט גדול יותר */
    font-weight: bold;
    color: #004080; /* צבע כותרות */
    min-width: 100px; /* לוודא רוחב מינימלי למניעת קפיצות */
}

#year-slider {
    width: 95%; /* סליידר רחב יותר */
    margin: 0 auto;
    display: block;
    -webkit-appearance: none; /* הסתרת מראה ברירת המחדל של הדפדפן */
    appearance: none;
    height: 8px; /* גובה סליידר */
    background: #ddd; /* צבע רקע הסליידר */
    outline: none; /* הסרת קונטור ברירת מחדל */
    opacity: 0.7;
    transition: opacity .2s;
    border-radius: 4px;
}

#year-slider:hover {
    opacity: 1;
}

/* סגנון הידית של הסליידר */
#year-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px; /* גודל ידית */
    height: 20px; /* גודל ידית */
    background: #007bff; /* צבע ידית */
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    transition: background .2s;
}

#year-slider::-webkit-slider-thumb:hover {
     background: #0056b3;
}

#year-slider::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    transition: background .2s;
}

#year-slider::-moz-range-thumb:hover {
    background: #0056b3;
}

.control-buttons {
    margin-top: 15px;
    display: flex;
    gap: 10px; /* רווח בין כפתורים */
    justify-content: center;
}

.control-buttons button {
    padding: 8px 15px; /* ריפוד כפתורים */
    font-size: 1em;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #007bff; /* כחול כפתורים ראשי */
    color: white;
    transition: background-color 0.2s ease, transform 0.1s ease;
    min-width: 80px; /* רוחב מינימלי לכפתור */
}

.control-buttons button:hover {
    background-color: #0056b3; /* כחול כהה יותר בלחיצה */
}

.control-buttons button:active {
    transform: scale(0.98); /* אפקט לחיצה עדין */
}

.control-buttons button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    opacity: 0.8;
}


/* כפתור הצג/הסתר */
#toggle-explanation {
    display: block;
    margin: 30px auto; /* ריווח גדול יותר */
    padding: 12px 25px; /* ריפוד גדול יותר */
    font-size: 1.1em; /* פונט גדול יותר */
    cursor: pointer;
    border: none;
    border-radius: 6px;
    background-color: #17a2b8; /* כחול ירקרק */
    color: white;
    transition: background-color 0.2s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#toggle-explanation:hover {
    background-color: #138496;
}

#toggle-explanation:active {
    transform: scale(0.98);
}


/* קונטיינר ההסבר */
#explanation {
    margin-top: 20px;
    padding: 20px; /* ריפוד פנימי גדול יותר */
    border: none; /* מסגרת הוסרה לטובת צל */
    border-radius: 12px; /* פינות מעוגלות יותר */
    background-color: #ffffff; /* רקע לבן */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* צל עדין יותר */
    text-align: justify; /* יישור לשוליים */
    opacity: 0; /* התחלה שקופה לאנימציה */
    max-height: 0; /* גובה 0 להתחלה */
    overflow: hidden; /* הסתרת תוכן מעבר לגובה 0 */
    transition: opacity 0.5s ease-out, max-height 0.5s ease-out; /* אנימציה לחשיפה */
}

#explanation.visible {
    opacity: 1; /* אטימות מלאה */
    max-height: 2000px; /* גובה מקסימלי מספיק כדי להכיל את התוכן (אפשר להשתמש ב-auto אם לא רוצים אנימציית גובה) */
    /* הערה: אנימציית גובה ל-auto אינה נתמכת, לכן משתמשים בערך גדול מספיק */
}

#explanation h2, #explanation h3 {
    color: #0056b3; /* צבע כחול כהה יותר לכותרות הסבר */
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid #eee; /* קו תחתון עדין לכותרות H3 */
    padding-bottom: 5px;
}

#explanation h2 {
    text-align: center;
    border-bottom: none;
}

#explanation p, #explanation ul {
    line-height: 1.7; /* מרווח שורות גדול יותר */
    margin-bottom: 15px;
    text-align: justify;
    color: #555; /* צבע טקסט אפור כהה עדין */
}

#explanation ul {
    padding-left: 20px; /* ריפוד לרשימות */
}

#explanation li {
    margin-bottom: 8px;
}

/* התאמות למסכים קטנים */
@media (max-width: 768px) {
    .interactive-container {
        padding: 15px;
    }

    #map-container {
        height: 400px; /* הקטנת גובה המפה במסכים קטנים */
    }

    .pole-marker {
        width: 20px;
        height: 20px;
    }

    .pole-marker .marker-label {
        font-size: 10px;
        bottom: -18px;
    }

    #year-display {
        font-size: 1em;
    }

    .control-buttons button {
        padding: 6px 10px;
        font-size: 0.9em;
    }

    #toggle-explanation {
        padding: 10px 20px;
        font-size: 1em;
    }

    #explanation {
        padding: 15px;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const mapContainer = document.getElementById('map-container');
    const geographicPoleMarker = document.getElementById('geographic-north-pole');
    const magneticPoleMarker = document.getElementById('magnetic-north-pole');
    const yearSlider = document.getElementById('year-slider');
    const yearDisplay = document.getElementById('year-display');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const pathElement = document.querySelector('#pole-path-svg polyline') || document.createElementNS("http://www.w3.org/2000/svg", "polyline");
    const svgElement = document.getElementById('pole-path-svg');
    const playPauseButton = document.getElementById('play-pause-button');
    const stepBackButton = document.getElementById('step-back-button');
    const stepForwardButton = document.getElementById('step-forward-button');

    // Add polyline if it doesn't exist (should be in HTML, but safety check)
    if (!svgElement.contains(pathElement)) {
        svgElement.appendChild(pathElement);
    }

    // Approximate historical Magnetic North Pole positions (Latitude, Longitude)
    // Data points based on various historical charts and models (simplified)
    // Added intermediate points for potentially smoother path representation
    const polePositions = {
        1900: { lat: 71.3, lon: -96.3 },
        1910: { lat: 71.9, lon: -97.8 },
        1920: { lat: 72.7, lon: -100.5 },
        1930: { lat: 73.3, lon: -103.0 },
        1940: { lat: 73.7, lon: -102.7 },
        1950: { lat: 74.5, lon: -101.0 },
        1960: { lat: 75.3, lon: -100.5 },
        1970: { lat: 76.2, lon: -101.0 },
        1980: { lat: 77.1, lon: -102.1 },
        1990: { lat: 78.6, lon: -103.7 },
        2000: { lat: 81.0, lon: -109.6 },
        2005: { lat: 82.7, lon: -117.5 },
        2010: { lat: 85.0, lon: -135.0 },
        2015: { lat: 86.2, lon: -161.0 },
        2020: { lat: 86.5, lon: -169.0 }, // Approaching International Date Line
        2023: { lat: 87.0, lon: 175.0 }  // Crossed into Eastern Hemisphere (represented by positive longitude)
    };

    // Geographic North Pole position (Fixed at 90N, 0E)
    const geographicNorthPole = { lat: 90, lon: 0 };

    // Get map container dimensions (dynamic)
    let mapWidth = mapContainer.offsetWidth;
    let mapHeight = mapContainer.offsetHeight;

    // Update dimensions on window resize
    window.addEventListener('resize', () => {
        mapWidth = mapContainer.offsetWidth;
        mapHeight = mapContainer.offsetHeight;
        // Re-calculate pole positions and redraw path on resize
        updatePolePositionAndPath(parseFloat(yearSlider.value), true); // true to force redraw
        positionGeographicPole(); // Reposition fixed pole
    });


    // --- Mapping Latitude/Longitude to Pixel Coordinates (Simplified Mapping) ---
    // This mapping is an approximation designed to fit the Mercator projection visually
    // It is NOT a mathematically correct projection transformation but positions
    // the points reasonably well on a Mercator map focused on the Northern Hemisphere.
    // Refined Y mapping: Assume 90N maps near the top (y=20), and 0N maps towards the bottom (y=mapHeight-50).
    // Pole moves from ~70N to ~87N, which should fall within the upper part of the map.
    const mapCenterLon = -10; // Approximate center longitude of the map image visual area
    const lonScale = mapWidth / 360; // Degrees per pixel for longitude

    // Simple linear interpolation for X, adjusted for map center
    function getX(lon) {
        // Map longitude (-180 to 180) to x (0 to mapWidth)
        // Adjust for the map's apparent center if needed, but basic (lon + 180) / 360 * width is standard for Mercator edges
        // Let's refine: map -180 to 0px, 180 to mapWidth px
        return (lon + 180) / 360 * mapWidth;
    }

     // Simple linear interpolation for Y focused on the Northern Hemisphere range
     // Maps 90N to a fixed offset from top, and 0N to a fixed offset from bottom.
     // Pole movement range ~70N to ~87N should scale linearly between these.
    const topY = 20; // Pixels from the top edge for 90N
    const equatorY = mapHeight - 50; // Pixels from the top edge for 0N (approximate)

    function getY(lat) {
        if (lat > 90) lat = 90; // Cap latitude
        if (lat < -90) lat = -90;

        // Linear interpolation between 90N (topY) and 0N (equatorY)
        // Adjusting scale so 90N is at topY, 0N is at equatorY
        // The scale factor is (equatorY - topY) / (90 - 0)
        const y = topY + (90 - lat) / 90 * (equatorY - topY);
        // This maps: 90N -> topY, 0N -> equatorY, -90N -> equatorY + (180/90)*(equatorY - topY)
        // This is still a simple linear approx, better than the previous one for visual Mercator feel.
         return y;
     }

    // Position Geographic Pole (fixed)
    function positionGeographicPole() {
         const geoPoleX = getX(geographicNorthPole.lon); // Should be mapWidth / 2
         const geoPoleY = getY(geographicNorthPole.lat); // Use the refined getY function
        // Adjust slightly for visual marker centering at the very top point
         geographicPoleMarker.style.left = `${geoPoleX}px`;
         geographicPoleMarker.style.top = `${getY(90) - geographicPoleMarker.offsetHeight/2 + 5}px`; // Position near the top edge, slightly offset
    }
    positionGeographicPole(); // Set initial position


    // Function to interpolate pole position for any given year
    function interpolatePosition(year) {
        const years = Object.keys(polePositions).map(Number).sort((a, b) => a - b);

        // Handle years outside the known range
        if (year <= years[0]) return polePositions[years[0]];
        if (year >= years[years.length - 1]) return polePositions[years[years.length - 1]];

        // Find the two closest known years
        let y1, y2;
        for (let i = 0; i < years.length - 1; i++) {
            if (year >= years[i] && year < years[i + 1]) {
                y1 = years[i];
                y2 = years[i + 1];
                break;
            }
        }

        const pos1 = polePositions[y1];
        const pos2 = polePositions[y2];
        const fraction = (year - y1) / (y2 - y1);

        // Linear interpolation for latitude
        const lat = pos1.lat + fraction * (pos2.lat - pos1.lat);

        // Interpolation for longitude, handling wrap around 180/-180
        let lonDiff = pos2.lon - pos1.lon;
        // If the difference is greater than 180 degrees, the shortest path crosses the anti-meridian
        if (lonDiff > 180) lonDiff -= 360;
        if (lonDiff < -180) lonDiff += 360;

        let lon = pos1.lon + fraction * lonDiff;

        // Ensure longitude stays within -180 to 180 range
        if (lon > 180) lon -= 360;
        if (lon < -180) lon += 360;

        return { lat: lat, lon: lon };
    }

    // Function to update the magnetic pole marker position and redraw the path
    // redrawAll flag forces recalculation of all path points (e.g., on resize)
    function updatePolePositionAndPath(year, redrawAll = false) {
        const pos = interpolatePosition(year);
        const x = getX(pos.lon);
        const y = getY(pos.lat);

        // Update marker position using CSS transition
        magneticPoleMarker.style.left = `${x}px`;
        magneticPoleMarker.style.top = `${y}px`;

        // Update year display
        yearDisplay.textContent = `שנה: ${Math.round(year)}`;

        // Redraw path up to the current year
        const years = Object.keys(polePositions).map(Number).sort((a, b) => a - b);
        let points = '';
        const startYear = years[0];
        const endYear = Math.floor(year); // Draw path up to the current full year
        const fractionalPart = year - endYear;

        // Calculate points for full years
        for (let y = startYear; y <= endYear; y++) {
             const currentPos = interpolatePosition(y);
             const currentX = getX(currentPos.lon);
             const currentY = getY(currentPos.lat);
             points += `${currentX},${currentY} `;
        }

        // Add point for the current fractional year position
        if (fractionalPart > 0 && endYear < years[years.length - 1]) {
             const currentPos = interpolatePosition(year);
             const currentX = getX(currentPos.lon);
             const currentY = getY(currentPos.lat);
             // Check if this point is very close to the last added full-year point to avoid duplicates
             const lastPointCoords = points.trim().split(' ').pop();
             if (!lastPointCoords || lastPointCoords !== `${currentX},${currentY}`) {
                  points += `${currentX},${currentY} `;
             }
        }


        // Simple redraw: just update the points attribute
        pathElement.setAttribute('points', points.trim());

         // Optional: Animate path drawing by animating stroke-dashoffset
        // This would require calculating path length and is more complex with polyline as length changes.
        // Sticking to simple redraw for now to maintain structure adherence.
    }

    // --- Animation (Play/Pause) Logic ---
    let animationFrameId = null;
    let startTime = null;
    const animationDuration = 20000; // Animate from min to max year in 20 seconds

    function animateSlider(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = elapsed / animationDuration;

        if (progress < 1) {
            const minYear = parseFloat(yearSlider.min);
            const maxYear = parseFloat(yearSlider.max);
            const currentYear = minYear + progress * (maxYear - minYear);
            yearSlider.value = currentYear;
            updatePolePositionAndPath(currentYear); // Update based on fractional year
            animationFrameId = requestAnimationFrame(animateSlider);
        } else {
            // Animation finished
            yearSlider.value = yearSlider.max;
             updatePolePositionAndPath(parseFloat(yearSlider.max)); // Final update
            stopAnimation();
            playPauseButton.textContent = '▶ נגן';
        }
    }

    function startAnimation() {
        if (animationFrameId) return; // Already animating
        // If at the end, reset to the start
        if (parseFloat(yearSlider.value) >= parseFloat(yearSlider.max)) {
            yearSlider.value = yearSlider.min;
            updatePolePositionAndPath(parseFloat(yearSlider.min));
        }
        startTime = null; // Reset start time to begin animation from current value
        playPauseButton.textContent = '❚❚ השהה';
        animationFrameId = requestAnimationFrame(animateSlider);
    }

    function stopAnimation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
            startTime = null; // Reset start time
            playPauseButton.textContent = '▶ נגן';
        }
    }

    // --- Event Listeners ---

    // Slider input updates position and path
    yearSlider.addEventListener('input', (event) => {
        const selectedYear = parseFloat(event.target.value);
        updatePolePositionAndPath(selectedYear);
        stopAnimation(); // Stop animation if user interacts with slider manually
    });

    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.maxHeight === '0px';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            // Use a timeout to allow display change before starting transition
            setTimeout(() => {
                 explanationDiv.classList.add('visible');
                 toggleButton.textContent = 'הסתר הסבר';
            }, 10); // Small delay
        } else {
             explanationDiv.classList.remove('visible');
             // Use a timeout to allow transition to finish before hiding
            setTimeout(() => {
                explanationDiv.style.display = 'none';
                toggleButton.textContent = 'מה עומד מאחורי התנועה הזו? הצג הסבר מפורט';
            }, 500); // Match transition duration
        }
    });

    // Play/Pause button
    playPauseButton.addEventListener('click', () => {
        if (animationFrameId) {
            stopAnimation();
        } else {
            startAnimation();
        }
    });

    // Step Back button
    stepBackButton.addEventListener('click', () => {
        stopAnimation();
        let currentYear = parseFloat(yearSlider.value);
        const minYear = parseFloat(yearSlider.min);
        const step = parseFloat(yearSlider.step);
        currentYear = Math.max(minYear, currentYear - step);
        yearSlider.value = currentYear;
        updatePolePositionAndPath(currentYear);
    });

    // Step Forward button
    stepForwardButton.addEventListener('click', () => {
        stopAnimation();
        let currentYear = parseFloat(yearSlider.value);
        const maxYear = parseFloat(yearSlider.max);
        const step = parseFloat(yearSlider.step);
         currentYear = Math.min(maxYear, currentYear + step);
        yearSlider.value = currentYear;
        updatePolePositionAndPath(currentYear);
    });


    // Initial setup
    const initialYear = parseFloat(yearSlider.value);
    // Wait for potential image load and DOM readiness
    // Using requestAnimationFrame for initial draw ensures mapContainer dimensions are available
    requestAnimationFrame(() => {
        mapWidth = mapContainer.offsetWidth; // Get final dimensions
        mapHeight = mapContainer.offsetHeight;
        positionGeographicPole(); // Position fixed pole based on final dimensions
        updatePolePositionAndPath(initialYear, true); // Draw initial state and full path
    });


    // Optional: Add a subtle "pulse" animation class to markers periodically or on hover
    // Let's use CSS :hover and the existing CSS animation for simplicity initially.
});
</script>
---
```