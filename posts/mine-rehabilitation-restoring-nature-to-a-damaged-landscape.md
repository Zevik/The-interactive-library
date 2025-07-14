---
title: "שיקום מכרות: הפיכת פצע בנוף לגן פורח"
english_slug: mine-rehabilitation-restoring-nature-to-a-damaged-landscape
category: "מדעי הסביבה / כללי"
tags: [שיקום אקולוגי, כריה, סביבה, קיימות, מערכות אקולוגיות, גאולוגיה]
---
# שיקום מכרות: הפיכת פצע בנוף לגן פורח

נוף שבו פעלה מחצבה או מכרה וננטש נראה לרוב כפצע פתוח: עפר חשוף, בורות עמוקים, מים עכורים וצמחייה כמעט בלתי קיימת. זהו אתר פגוע סביבתית, ולעיתים קרובות גם מסוכן. האם יש דרך להחזיר את החיים והצבע למקום כזה? מסע השיקום הוא משימה מורכבת, הדורשת ידע, תכנון, תקציב... וזמן. האם תצליחו במשימה?

<div class="rehab-simulator-container">
    <h2 class="simulator-title">סימולטור שיקום מכרות נטוש</h2>
    <div class="game-area">
        <div class="controls">
            <div class="stats-panel">
                <h3>משאבים:</h3>
                <p>💰 תקציב: <span id="budget" class="stat-value">1,000,000</span> ש"ח</p>
                <p>🗓️ ימים נותרו: <span id="time" class="stat-value">365</span></p>
            </div>
            <div class="metrics-panel">
                <h3>מדדי התאוששות סביבתית:</h3>
                <p>💧 איכות מים: <span id="water-quality" class="metric-value">10</span> / 100</p>
                <p>🌿 כיסוי צמחייה: <span id="vegetation-cover" class="metric-value">5</span> %</p>
                <p>🦋 מגוון ביולוגי: <span id="biodiversity" class="metric-value">2</span> / 10</p>
            </div>
            <div class="actions-panel">
                <h3>בחר משימת שיקום:</h3>
                <button class="action-btn" data-action="soil-treatment" data-cost="50000" data-time="30">
                    <span class="action-name">🧱 טיפול וייצוב קרקע מזוהמת</span>
                    <span class="action-cost-time">(עלות: 50,000 ש"ח, זמן: 30 ימים)</span>
                </button>
                <button class="action-btn" data-action="slope-stabilization" data-cost="70000" data-time="45">
                     <span class="action-name">⛰️ ייצוב מדרונות ושחזור תוואי שטח</span>
                    <span class="action-cost-time">(עלות: 70,000 ש"ח, זמן: 45 ימים)</span>
                </button>
                <button class="action-btn" data-action="water-treatment" data-cost="60000" data-time="40">
                    <span class="action-name">🌊 טיהור מקורות מים חומציים/מזוהמים</span>
                    <span class="action-cost-time">(עלות: 60,000 ש"ח, זמן: 40 ימים)</span>
                </button>
                <button class="action-btn" data-action="planting" data-cost="40000" data-time="60">
                    <span class="action-name">🌱 שתילת צמחייה חלוצית ומינים מקומיים</span>
                    <span class="action-cost-time">(עלות: 40,000 ש"ח, זמן: 60 ימים)</span>
                </button>
                <button class="action-btn" data-action="wildlife-intro" data-cost="30000" data-time="90">
                    <span class="action-name">🦊 עידוד חזרת בעלי חיים מקומיים</span>
                    <span class="action-cost-time">(עלות: 30,000 ש"ח, זמן: 90 ימים)</span>
                </button>
                 <button class="action-btn" data-action="monitoring" data-cost="10000" data-time="15">
                    <span class="action-name">🔬 ניטור והערכה סביבתית</span>
                    <span class="action-cost-time">(עלות: 10,000 ש"ח, זמן: 15 ימים)</span>
                </button>
            </div>
        </div>
        <div class="mine-map">
            <div class="mine-background"></div> <!-- Optional: for background effects -->
            <div class="problem-area problem-pollution" id="area-pollution" title="אזור מזוהם מאוד, קרקע רעילה">
                 <span class="problem-label">זיהום קרקע</span>
            </div>
            <div class="problem-area problem-erosion" id="area-erosion" title="מדרונות לא יציבים, סכנת קריסה ושחיקה">
                <span class="problem-label">שחיקת קרקע</span>
            </div>
            <div class="problem-area problem-water" id="area-water" title="מקורות מים חומציים ומזוהמים">
                 <span class="problem-label">מים מזוהמים</span>
            </div>
            <div class="problem-area problem-barren" id="area-barren" title="קרקע עקרה, חסרת חיים">
                 <span class="problem-label">קרקע עקרה</span>
            </div>
            <div class="mine-center" title="ליבת המכרה הנטוש"></div>
            <div class="map-legend">
                <h4>מקרא המפה:</h4>
                <p><span class="legend-color legend-pollution"></span> זיהום קרקע</p>
                <p><span class="legend-color legend-erosion"></span> שחיקת קרקע/מדרונות</p>
                <p><span class="legend-color legend-water"></span> מים מזוהמים</p>
                <p><span class="legend-color legend-barren"></span> קרקע עקרה</p>
                <p><span class="legend-color legend-addressed"></span> אזור שוקם חלקית/מטופל</p>

            </div>
             <div class="map-overlay-effect" id="map-effect"></div>
        </div>
    </div>
    <div id="game-status" class="status-message"></div>
    <button id="restart-btn" class="restart-button">התחל משימה חדשה</button>
</div>

<style>
/* General Styles */
.rehab-simulator-container {
    direction: rtl;
    font-family: 'Arial', sans-serif; /* Or a more modern sans-serif */
    max-width: 1100px; /* Slightly wider */
    margin: 30px auto;
    padding: 25px;
    border: 1px solid #e0e0e0;
    border-radius: 12px; /* Softer corners */
    background-color: #fefefe; /* Lighter background */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    display: flex;
    flex-direction: column;
    gap: 25px;
}

.rehab-simulator-container h2.simulator-title {
    width: 100%;
    text-align: center;
    color: #2c3e50; /* Darker, richer blue/grey */
    margin-bottom: 15px;
    font-size: 1.8em; /* Slightly larger title */
}

.game-area {
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
}

.controls {
    flex: 1 1 350px; /* Give controls more space */
    display: flex;
    flex-direction: column;
    gap: 25px;
}

.stats-panel, .metrics-panel, .actions-panel {
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    background-color: #ffffff;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.stats-panel h3, .metrics-panel h3, .actions-panel h3 {
    margin-top: 0;
    margin-bottom: 15px;
    color: #34495e; /* Dark blue/grey */
    font-size: 1.1em;
    border-bottom: 1px solid #eee;
    padding-bottom: 8px;
}

.stats-panel p, .metrics-panel p {
    margin: 8px 0;
    font-size: 1em; /* Slightly larger font */
    color: #555;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.stat-value, .metric-value {
    font-weight: bold;
    color: #2980b9; /* Blue */
}

.metric-value {
    font-family: 'Courier New', Courier, monospace; /* Monospaced for clarity */
}


.actions-panel .action-btn {
    display: flex; /* Use flex for name and cost/time */
    flex-direction: column; /* Stack name and cost/time */
    width: 100%;
    padding: 12px 15px; /* More padding */
    margin-bottom: 10px; /* More space between buttons */
    border: none;
    border-radius: 6px; /* Softer button corners */
    background-color: #2ecc71; /* Green - nature */
    color: white;
    cursor: pointer;
    font-size: 0.95em;
    text-align: right;
    transition: background-color 0.3s ease, opacity 0.3s ease, transform 0.1s ease;
    line-height: 1.4;
}

.action-btn .action-name {
    font-weight: bold;
    margin-bottom: 4px;
}

.action-btn .action-cost-time {
    font-size: 0.8em;
    opacity: 0.9;
}

.action-btn:hover:not(:disabled) {
    background-color: #27ae60; /* Darker green on hover */
    transform: translateY(-2px); /* Subtle lift effect */
}

.action-btn:disabled {
    background-color: #bdc3c7; /* Light grey */
    color: #7f8c8d; /* Dark grey text */
    cursor: not-allowed;
    opacity: 0.8;
}

/* Mine Map Styles */
.mine-map {
    flex: 1 1 500px; /* Give map more space */
    position: relative;
    background: linear-gradient(to bottom, #aaddff, #77aaff); /* Simple sky gradient */
    border: 1px solid #ccc;
    border-radius: 8px;
    aspect-ratio: 16 / 10;
    overflow: hidden;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    min-height: 300px; /* Ensure minimum size */
}

.mine-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgoJPGZlYXR1cmU+CgkJPGZlQ3R1cmVUdXJidWxlIHR5cGU9InR1cmJ1bGVudCIgYmFzZUZyZXF1ZW5jeT0iMC4wNSAwLjEiIG51bW9jdGF2ZXM9IjMiIHNlZWQ9IjEiIHN0aXRjaFRpbGVzPSJzdGl0Y2hIYWxmMjQiIGlkPSJmdXJyb3dTeW50aGVzaXMiPjwvZmVDdHVyYmxlPgoJCTxmZUNvbG9yTWF0cml4IHR5cGU9InNhdHVyYXRlIiB2YWx1ZXM9IjAiIHNpdGNoVGlsZXM9InN0aXRjaEhhbGYyNCIgaWQ9ImZ1cnJvd0NvbG9yU2F0dXJhdGlvbiI+PC9mZUNvbG9yTWF0cml4PgoJPC9mZWF0dXJlPgoJPHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0icmdiYSgyMzAsIDIyMCwgMjAwLDAuMykiIC8+Cgk8cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI2Z1cnJvd1N5bnRoZXNlcykiPjw1cmVjdD4KPC9zdmc+'); /* Subtle noise texture */
    opacity: 0.5; /* Semi-transparent */
    pointer-events: none; /* Allow clicks on elements below */
}


.mine-map .problem-area, .mine-map .mine-center {
    position: absolute;
    border-radius: 15px; /* Slightly rounded rectangles/blobs */
    opacity: 0.9;
    transition: background-color 1s ease, transform 0.5s ease; /* Smooth transition on fix and effects */
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    font-size: 0.9em;
    font-weight: bold;
    text-align: center;
}

.problem-label {
    opacity: 1; /* Ensure label is visible */
    pointer-events: none; /* Don't interfere with clicks */
}


/* Initial problem colors */
.problem-pollution {
    top: 20%;
    left: 30%;
    width: 25%; /* Larger */
    height: 20%;
    background-color: rgba(101, 67, 33, 0.8); /* Dark earthy brown */
    border-radius: 15px;
}

.problem-erosion {
    top: 55%; /* Lower */
    left: 60%;
    width: 25%;
    height: 18%; /* Slightly taller */
    background-color: rgba(205, 92, 92, 0.8); /* Terracotta/burnt orange */
    border-radius: 15px;
}

.problem-water {
    top: 70%;
    left: 20%;
    width: 20%; /* Slightly larger */
    height: 15%; /* Shorter, more like a pond shape */
    border-radius: 10px; /* More rectangular */
    background-color: rgba(70, 130, 180, 0.8); /* Steely blue */
}

.problem-barren {
     top: 35%; /* Higher */
     left: 10%;
     width: 25%;
     height: 25%;
     background-color: rgba(180, 175, 160, 0.8); /* Light grey/tan */
     border-radius: 50%; /* Make it more circular */
}

.mine-center {
     top: 40%;
     left: 45%;
     width: 20%;
     height: 30%;
     background-color: rgba(50, 50, 50, 0.9); /* Darker grey */
     border-radius: 10px;
     box-shadow: inset 0 0 15px rgba(0,0,0,0.5);
}


/* Style for addressed areas */
.problem-area.addressed {
    background-color: rgba(144, 238, 144, 0.8); /* Light green */
     /* Add a subtle animation or border to show it's recovering */
    box-shadow: 0 0 10px rgba(144, 238, 144, 0.6);
}


/* Temporary effect on map area when action is clicked */
.mine-map .problem-area.effect {
    animation: pulse 1s ease-out forwards;
    transform-origin: center;
}

@keyframes pulse {
    0% { transform: scale(1); opacity: 0.9; }
    50% { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(1); opacity: 0.9; }
}


/* Map Legend Styles */
.map-legend {
    position: absolute;
    bottom: 15px; /* More space from bottom */
    right: 15px; /* Positioned right for RTL */
    background: rgba(255, 255, 255, 0.9); /* Slightly less transparent */
    padding: 10px 15px;
    border-radius: 8px;
    font-size: 0.9em;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.map-legend h4 { /* Use h4 for legend title */
    margin: 0 0 8px 0;
    font-size: 1em;
    color: #34495e;
    border-bottom: 1px dashed #ccc;
    padding-bottom: 5px;
}

.map-legend p {
    margin: 5px 0; /* More space between items */
    display: flex;
    align-items: center;
}

.legend-color {
    display: inline-block;
    width: 18px; /* Larger color swatch */
    height: 18px;
    margin-left: 8px; /* Space from text */
    border-radius: 4px; /* Slightly rounded swatch */
    border: 1px solid rgba(0,0,0,0.1);
}

.legend-pollution { background-color: rgba(101, 67, 33, 0.8); }
.legend-erosion { background-color: rgba(205, 92, 92, 0.8); }
.legend-water { background-color: rgba(70, 130, 180, 0.8); }
.legend-barren { background-color: rgba(180, 175, 160, 0.8); }
.legend-addressed { background-color: rgba(144, 238, 144, 0.8); }


/* Status Message Styles */
.status-message {
    width: 100%;
    text-align: center;
    font-size: 1.2em; /* Larger font */
    margin-top: 15px;
    min-height: 1.8em; /* Ensure height */
    padding: 10px;
    border-radius: 6px;
     transition: color 0.5s ease;
}

.status-message:empty { /* Hide if no message */
    display: none;
}


.status-message.win {
    color: #27ae60; /* Green */
    font-weight: bold;
    background-color: #e8f5e9; /* Light green background */
    border: 1px solid #a5d6a7;
}

.status-message.lose {
    color: #c0392b; /* Red */
    font-weight: bold;
    background-color: #ffebee; /* Light red background */
    border: 1px solid #ef9a9a;
}

/* Restart Button Styles */
.restart-button {
    display: block;
    margin: 15px auto 0; /* Center button */
    padding: 12px 25px; /* More padding */
    border: none;
    border-radius: 6px;
    background-color: #3498db; /* Blue */
    color: white;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.restart-button:hover {
    background-color: #2980b9; /* Darker blue */
    transform: translateY(-2px);
}

/* Explanation Section Styles */
#toggle-explanation {
    display: block;
    width: fit-content;
    margin: 25px auto; /* More space */
    padding: 10px 20px;
    background-color: #7f8c8d; /* Greyish button */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
}

#toggle-explanation:hover {
    background-color: #95a5a6; /* Lighter grey on hover */
}

#explanation-content {
    display: none; /* Initially hidden */
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #fefefe;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

#explanation-content h2 {
    color: #2c3e50;
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.5em;
    border-bottom: 1px solid #eee;
    padding-bottom: 8px;
}

#explanation-content h3 {
    color: #34495e;
    margin-top: 15px;
    margin-bottom: 8px;
    font-size: 1.2em;
}

#explanation-content p {
    line-height: 1.7; /* Improved readability */
    margin-bottom: 12px;
    color: #555;
}

#explanation-content ul {
    margin-bottom: 12px;
    padding-right: 20px; /* RTL list padding */
}

#explanation-content li {
    margin-bottom: 8px; /* More space between list items */
    line-height: 1.5;
    color: #555;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .game-area {
        flex-direction: column;
    }

    .controls, .mine-map {
        flex: 1 1 100%; /* Take full width */
    }

    .map-legend {
        position: static; /* Make legend static below map */
        margin-top: 15px;
        width: 100%;
        box-shadow: none;
        background: none;
        border: none;
        padding: 0;
        font-size: 0.9em;
    }
     .map-legend h4 {
         text-align: center;
         border-bottom: none;
         padding-bottom: 0;
     }
}


</style>

<button id="toggle-explanation">למד עוד: מהו שיקום מכרות ולמה הוא חשוב?</button>

<div id="explanation-content">
    <h2>שיקום מכרות: להחזיר את הריאות הירוקות לנוף הפגוע</h2>
    <p>כשפעילות כריה מסתיימת, לעיתים קרובות נותר נוף צלקתי ופגוע סביבתית. שיקום מכרות הוא תהליך מדעי והנדסי מורכב שמטרתו להחזיר את האתר למצב יציב ובטוח, ובהמשך - לשקם ככל הניתן את המערכת האקולוגית שנפגעה.</p>

    <h3>הנזקים שמותירה הכריה בנוף:</h3>
    <p>פעילות כריה גורמת לשורה ארוכה של פגיעות סביבתיות:</p>
    <ul>
        <li>**פגיעה פיזית וטופוגרפית:** שינוי דרמטי של צורת הנוף, יצירת בורות ענק, מדרונות תלולים ולא יציבים של עפר ופסולת (שכתוצאה נקראים "דמפים").</li>
        <li>**זיהום קרקע:** שחרור מתכות כבדות (כמו עופרת, ארסן) וחומרים רעילים אחרים מפסולת הכריה שמחלחלים לקרקע.</li>
        <li>**זיהום מים:** תופעה נפוצה ומסוכנת היא "ניקוז מכרות חומצי" (Acid Mine Drainage - AMD), שנוצר כשמי גשם ומקורות מים אחרים באים במגע עם סלעים מינרליים במכרה החשופים לחמצן, יוצרים חומצה גופרתית וממיסים מתכות כבדות. מים אלו מזהמים נחלים, אגמים ומי תהום.</li>
        <li>**אובדן כיסוי צמחייה ובתי גידול:** הסרת הצמחייה המקורית הורסת בתי גידול ומובילה לשחיקת קרקע מוגברת.</li>
        <li>**פגיעה במגוון הביולוגי:** הרס בתי גידול ישירים ועקיפים (דרך זיהום מים וקרקע) גורם לדלדול או היעלמות של מיני צמחים ובעלי חיים מקומיים, ולעיתים קרובות מאפשר פלישת מינים לא רצויים.</li>
    </ul>

    <h3>אתגרים מרכזיים בשיקום אתרי מכרה:</h3>
    <p>שיקום מוצלח דורש התמודדות עם קשיים רבים:</p>
    <ul>
        <li>**התמודדות עם חומציות ומתכות כבדות:** נטרול ה-pH הנמוך במים ובקרקע וקיבוע המתכות המזהמות כך שלא יהיו זמינות לאורגניזמים חיים.</li>
        <li>**ייצוב פיזי:** מניעת שחיקת קרקע, קריסת מדרונות ובורות.</li>
        <li>**שיקום פוריות הקרקע:** קרקע באתר מכרה לעיתים חסרה חומרי מזון חיוניים, דחוסה ואינה מאפשרת צמיחת צמחים. נדרש טיוב ושיפור מבנה הקרקע.</li>
        <li>**החזרת צמחייה מקומית:** בחירת מינים מתאימים שיכולים לשרוד בתנאים קשים, שתילתם ודאגה להישרדותם הראשונית.</li>
        <li>**זמן ועלות:** תהליכי שיקום הם יקרים ואורכים שנים, לעיתים עשרות שנים, עד שהמערכת האקולוגית מתאוששת באופן משמעותי.</li>
    </ul>

    <h3>טכניקות ואסטרטגיות לשיקום:</h3>
    <p>הגישה לשיקום משלבת מספר דיסציפלינות:</p>
    <ul>
        <li>**שחזור פיזי והנדסי:** עיצוב מחדש של הנוף (לדוגמה, החלקת מדרונות תלולים), יצירת מערכות ניקוז מבוקרות, כיסוי פסולת מכרה בשכבות קרקע או חומרים סינטטיים למניעת חלחול.</li>
        <li>**טיפול כימי וביולוגי:**
            <ul>
                <li>נטרול כימי (למשל, הוספת גיר) לטיפול במים וקרקע חומציים.</li>
                <li>פיטורמדיאציה (Phytoremediation): שימוש בצמחים מסוימים שיכולים לספוג או לנטרל מזהמים מהקרקע והמים.</li>
                <li>ביורמדיאציה (Bioremediation): שימוש במיקרואורגניזמים לפירוק או שינוי מזהמים.</li>
            </ul>
        </li>
        <li>**שיקום אקולוגי (ביולוגי):**
            <ul>
                <li>טיוב קרקע והוספת חומר אורגני.</li>
                <li>שתילת מיני צמחים מקומיים חלוצים ועמידים.</li>
                <li>הדרגתית - עידוד חזרת בעלי חיים מקומיים שיסייעו בתהליכים אקולוגיים (האבקה, פיזור זרעים וכו').</li>
            </ul>
        </li>
    </ul>
    <p>שיקום מוצלח דורש ניטור מתמשך והתאמת הגישות בהתאם להתקדמות ולשינויים בתנאי האתר.</p>
</div>

<script>
    // Get DOM elements
    const budgetEl = document.getElementById('budget');
    const timeEl = document.getElementById('time');
    const waterQualityEl = document.getElementById('water-quality');
    const vegetationCoverEl = document.getElementById('vegetation-cover');
    const biodiversityEl = document.getElementById('biodiversity');
    const actionBtns = document.querySelectorAll('.action-btn');
    const gameStatusEl = document.getElementById('game-status');
    const restartBtn = document.getElementById('restart-btn');
    const explanationBtn = document.getElementById('toggle-explanation');
    const explanationContent = document.getElementById('explanation-content');
    const mapEffectEl = document.getElementById('map-effect');


    // Mapping of action keys to problem area IDs they primarily address
    const actionToAreaMap = {
        'soil-treatment': 'area-pollution',
        'slope-stabilization': 'area-erosion',
        'water-treatment': 'area-water',
        'planting': 'area-barren'
        // wildlife-intro and monitoring don't target a specific area visually in this sim
    };

     // Mapping of problem area IDs to their DOM elements
    const problemAreas = {
        'area-pollution': document.getElementById('area-pollution'),
        'area-erosion': document.getElementById('area-erosion'),
        'area-water': document.getElementById('area-water'),
        'area-barren': document.getElementById('area-barren')
    };

    // Initial game state definition
    const initialGameState = {
        budget: 1000000,
        time: 365, // Days
        metrics: {
            waterQuality: 10, // out of 100
            vegetationCover: 5, // percentage
            biodiversity: 2 // out of 10
        },
        problemsAddressed: { // Track if the *primary* problem in an area is addressed
            'area-pollution': false,
            'area-erosion': false,
            'area-water': false,
            'area-barren': false
        },
        // Define actions, their costs, time, and effects on metrics and addressed areas
        actions: {
            'soil-treatment': {
                 name: 'טיפול וייצוב קרקע מזוהמת',
                 cost: 50000, time: 30,
                 effects: { waterQuality: 10, vegetationCover: 15, biodiversity: 1 },
                 addresses: 'area-pollution', // Primarily addresses pollution
                 message: 'הקרקע עוברת תהליך טיהור וטיוב. המזהמים מנוטרלים והבסיס לצמחייה חדשה נוצר.'
             },
            'slope-stabilization': {
                name: 'ייצוב מדרונות ושחזור תוואי שטח',
                cost: 70000, time: 45,
                effects: { vegetationCover: 20, biodiversity: 2 },
                addresses: 'area-erosion', // Primarily addresses erosion
                message: 'המדרונות עובדו ויוצבו למניעת שחיקה. הנוף נראה יציב יותר.'
            },
            'water-treatment': {
                 name: 'טיהור מקורות מים חומציים/מזוהמים',
                cost: 60000, time: 40,
                effects: { waterQuality: 30, biodiversity: 3 },
                addresses: 'area-water', // Primarily addresses water
                 message: 'המים עוברים תהליך טיהור. החומציות יורדת וריכוז המתכות פוחת.'
            },
            'planting': {
                name: 'שתילת צמחייה חלוצית ומינים מקומיים',
                cost: 40000, time: 60,
                effects: { vegetationCover: 30, biodiversity: 4, waterQuality: 5 }, // Planting helps all metrics
                addresses: 'area-barren', // Primarily addresses barren land
                message: 'הצמחים הראשונים נקלטו! הם יסייעו בייצוב הקרקע ויתחילו למשוך חרקים ובעלי חיים קטנים.'
            },
            'wildlife-intro': {
                 name: 'עידוד חזרת בעלי חיים מקומיים',
                cost: 30000, time: 90,
                effects: { biodiversity: 5, vegetationCover: 5 }, // Wildlife helps biodiversity most, slightly vegetation
                addresses: null, // Doesn't target one area visually
                message: 'נוצרו תנאים מתאימים לחזרת בעלי חיים. צפו ליותר סימני חיים בקרוב!'
            },
            'monitoring': {
                 name: 'ניטור והערכה סביבתית',
                cost: 10000, time: 15,
                effects: {}, // No direct metric effect in this simple sim
                addresses: null, // Doesn't target one area visually
                message: 'צוותי ניטור אוספים נתונים כדי להעריך את קצב השיקום וההתקדמות.'
            }
        }
    };

    let gameState = {};

    // Function to update the visual display based on gameState
    function updateDisplay() {
        budgetEl.textContent = gameState.budget.toLocaleString();
        timeEl.textContent = gameState.time;
        waterQualityEl.textContent = `${gameState.metrics.waterQuality}`;
        vegetationCoverEl.textContent = `${gameState.metrics.vegetationCover}`;
        biodiversityEl.textContent = `${gameState.metrics.biodiversity}`;

        // Update map visuals based on problems addressed
        for (const areaId in problemAreas) {
            if (gameState.problemsAddressed[areaId]) {
                problemAreas[areaId].classList.add('addressed'); // Add class for green/addressed style
            } else {
                 problemAreas[areaId].classList.remove('addressed'); // Ensure class is removed on restart
                 // Optional: Add initial problem class back if needed, though CSS handles default
            }
        }

        // Update button disabled state based on budget and time
         actionBtns.forEach(button => {
            const actionKey = button.dataset.action;
            const action = gameState.actions[actionKey];
            if (gameState.budget < action.cost || gameState.time < action.time) {
                button.disabled = true;
            } else {
                button.disabled = false;
            }
        });
    }

    // Function to check if game is over (win or lose)
    function checkGameStatus() {
        let isGameOver = false;
        let winReason = null;

        if (gameState.time <= 0 || gameState.budget < 0) {
            isGameOver = true;
            winReason = false; // Lose
        } else {
             // Win condition: Reach certain metric thresholds AND address *all key* problem areas
             // Note: Monitoring/Wildlife don't mark an area as "addressed" in problemAreas logic,
             // but we might want them for a 'better' win. Let's stick to the 4 main areas for the addressed check.
            const winThresholds = { waterQuality: 80, vegetationCover: 70, biodiversity: 7 };
            const allProblemsAddressed = Object.values(gameState.problemsAddressed).every(addressed => addressed === true); // Ensure all marked areas are addressed

             if (gameState.metrics.waterQuality >= winThresholds.waterQuality &&
                 gameState.metrics.vegetationCover >= winThresholds.vegetationCover &&
                 gameState.metrics.biodiversity >= winThresholds.biodiversity &&
                 allProblemsAddressed) {
                 isGameOver = true;
                 winReason = true; // Win
             }
        }


        if (isGameOver) {
            endGame(winReason);
            return true; // Game is over
        }

        return false; // Game continues
    }

    // Function to handle game end (win or lose)
    function endGame(isWin) {
        actionBtns.forEach(btn => btn.disabled = true); // Disable all buttons
        let finalMessage = '';

        if (isWin) {
            finalMessage = `🥳 הצלחתם בגדול! המכרה שוקם והטבע חזר לנוף הפגוע!\n\n סיימתם את המשימה תוך ${initialGameState.time - gameState.time} ימים ובעלות של ${initialGameState.budget - gameState.budget} ש"ח. המערכת האקולוגית מתאוששת, והאתר בטוח וירוק שוב. כל הכבוד!`;
            gameStatusEl.className = 'status-message win';
        } else {
             const reason = gameState.time <= 0 ? 'נגמר הזמן' : 'נגמר התקציב';
            finalMessage = `💔 המשימה הסתיימה בכשלון. ${reason}.\n\n לא הצלחתם לשקם את המכרה באופן מלא ולעמוד ביעדים. המערכת האקולוגית עדיין בסכנה.`;
            gameStatusEl.className = 'status-message lose';
        }

        gameStatusEl.textContent = finalMessage;
        restartBtn.style.display = 'block'; // Show restart button
    }

    // Function to apply an action and update state
    function applyAction(actionKey) {
        const action = gameState.actions[actionKey];

        // Check if action is affordable/possible
        if (gameState.budget < action.cost || gameState.time < action.time) {
            gameStatusEl.textContent = '⚠️ אין מספיק תקציב או זמן למשימה זו!';
            gameStatusEl.className = 'status-message';
            return; // Exit if not possible
        }

        // Deduct cost and time
        gameState.budget -= action.cost;
        gameState.time -= action.time;

        // Apply effects on metrics
        for (const metric in action.effects) {
            gameState.metrics[metric] = Math.min(initialGameState.metrics[metric] > 10 ? 100 : 10, gameState.metrics[metric] + action.effects[metric]); // Cap at max value
        }

        // Mark problem area as addressed (if applicable and if it wasn't already)
        const areaId = action.addresses;
        if (areaId && problemAreas[areaId] && !gameState.problemsAddressed[areaId]) {
             gameState.problemsAddressed[areaId] = true;
             // Add temporary visual effect class to the area
             problemAreas[areaId].classList.add('effect');
             // Remove the effect class after a short duration
             setTimeout(() => {
                 problemAreas[areaId].classList.remove('effect');
             }, 1000); // Animation duration
        }


        // Update display
        updateDisplay();

        // Provide feedback message
        gameStatusEl.textContent = `✅ ${action.name} בוצע בהצלחה!\n\n${action.message}`;
        gameStatusEl.className = 'status-message'; // Reset class for neutral message

        // Check if game ended
        checkGameStatus();
    }

    // Function to start or restart the game
    function startGame() {
        // Deep copy initial state to reset
        gameState = JSON.parse(JSON.stringify(initialGameState));

        // Reset visual states
        for (const areaId in problemAreas) {
             problemAreas[areaId].classList.remove('addressed', 'effect');
        }

        // Update display for the initial state
        updateDisplay();

        // Reset game status message and hide restart button
        gameStatusEl.textContent = 'בחר משימת שיקום כדי להתחיל במסע...';
        gameStatusEl.className = 'status-message';
        restartBtn.style.display = 'none';

        // Ensure buttons are enabled
        actionBtns.forEach(btn => btn.disabled = false);
    }

    // Event Listeners
    actionBtns.forEach(button => {
        button.addEventListener('click', (e) => {
            const actionKey = e.currentTarget.dataset.action; // Use currentTarget in case span is clicked
            applyAction(actionKey);
        });
    });

    restartBtn.addEventListener('click', startGame);

    explanationBtn.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        explanationBtn.textContent = isHidden ? 'הסתר הסבר על שיקום מכרות' : 'למד עוד: מהו שיקום מכרות ולמה הוא חשוב?';
    });

    // Initial game start when the script loads
    startGame();

</script>
---
```