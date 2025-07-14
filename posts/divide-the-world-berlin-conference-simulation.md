---
title: "משחק החלוקה הגדול: ועידת ברלין"
english_slug: divide-the-world-berlin-conference-simulation
category: "ארכאולוגיה"
tags:
  - אימפריאליזם
  - קולוניאליזם
  - ועידת ברלין
  - אפריקה
  - היסטוריה מודרנית
---
# משחק החלוקה הגדול: ועידת ברלין

דמיינו יבשת עצומה על שולחן הדיונים. קווי גבול נמתחים בעפרון, בלי לשאול את מי שחי בפועל על האדמה הזו. כך התנהלה ועידת ברלין ב-1884. המעצמות האירופיות התכנסו כדי "לסדר" את "המירוץ לאפריקה" וקבעו את גורל היבשת לעשרות שנים קדימה. האם תוכלו לחוות את האופן שבו העולם חולק מחדש?

<div id="berlin-conference-app">
    <div id="game-info">
        <h2>מצב המירוץ</h2>
        <p>תור נוכחי: <span id="current-turn">1</span> מתוך 10</p>
        <p>האימפריה שלך: <span id="player-power-name"></span></p>
        <p>עתודות תביעה: <span id="player-claim-points"></span></p>
        <div id="player-objectives">
            <h3>יעדים אימפריאליים:</h3>
            <ul id="objectives-list">
                <!-- Objectives will be populated here -->
            </ul>
        </div>
    </div>

    <div id="map-container">
        <!-- Map regions will be generated here by JS -->
        <div id="map-overlay"></div> <!-- For potential animations/effects -->
    </div>

    <div id="game-controls">
        <button id="end-turn-button" disabled>סיים תור ></button>
    </div>

    <div id="turn-results">
        <h3>יומן אירועים:</h3>
        <ul id="results-list">
            <!-- Turn results will appear here -->
        </ul>
    </div>

    <div id="game-end-modal" class="modal">
        <div class="modal-content">
            <span class="close-button">&times;</span>
            <h2>וילונות יורדים!</h2>
            <div id="final-scores">
                <!-- Final scores will be displayed here -->
            </div>
            <p>ההשפעות של חלוקה זו נמשכו עשרות שנים. למדו עוד על ההקשר ההיסטורי למטה.</p>
             <button class="modal-button" onclick="window.location.reload()">התחל מירוץ חדש</button>
        </div>
    </div>

    <div id="start-modal" class="modal">
        <div class="modal-content">
            <h2>ברוכים הבאים לועידת ברלין!</h2>
            <p>אתה עומד לחוות סימולציה פשטנית של האופן שבו המעצמות האירופיות חילקו את אפריקה ביניהן בשלהי המאה ה-19. כל תור מייצג תקופה קצרה של התרחבות ותביעות.</p>
            <p>הקלק על אזורים ניטרליים במפה כדי לתבוע אותם עבור האימפריה שלך. יש לך מספר מוגבל של תביעות ועתודות בכל תור. השלם את היעדים האימפריאליים שלך לפני שהזמן אוזל!</p>
             <button class="modal-button" id="start-game-button">התחל את המירוץ!</button>
        </div>
    </div>

</div>

<button id="toggle-explanation-button">הצג/הסתר הסיפור שמאחורי המשחק</button>

<div id="historical-explanation" style="display: none;">
    <h2>הסיפור שמאחורי המשחק: ועידת ברלין והמירוץ לאפריקה</h2>

    <p>סוף המאה ה-19 היה תקופה של תחרות עזה בין מעצמות אירופה. לא רק באירופה עצמה, אלא גם מעבר לים. אפריקה, שהייתה עד אז מוכרת לאירופאים בעיקר דרך קווי החוף ומסעות מחקר פנימה, הפכה למוקד עניין מרכזי. הצורך בחומרי גלם לתעשייה המשתוללת, החיפוש אחר שווקים חדשים למוצרים המוגמרים, והרצון לצבור יוקרה לאומית וכוח אסטרטגי - כל אלו הובילו ל"מירוץ לאפריקה" (The Scramble for Africa).</p>

    <h3>המירוץ מתחמם: למה אפריקה הפכה לפתע אטרקטיבית?</h3>
    <ul>
        <li>**בטן מלאה וכיסים עמוקים:** המהפכה התעשייתית יצרה צורך עצום בחומרי גלם כמו גומי, כותנה, מינרלים יקרים ומוצרי חקלאות טרופית. אפריקה נתפסה כמקור בלתי נדלה למשאבים אלו, וגם כשוק פוטנציאלי למוצרים אירופיים.</li>
        <li>**יוקרה על המפה:** שליטה על מושבות הפכה לסמל לכוח ולמעמד בעולם. כל מעצמה שאפה ש"השמש לעולם לא תשקע על האימפריה שלה".</li>
        <li>**יתרון טכנולוגי מוחץ:** פיתוחים כמו רובה המקסימ (מקלע ראשון), אניות קיטור שאיפשרו תנועה בנהרות פנימה, הטלגרף שאיפשר תקשורת מהירה עם המטרופולין, ותרופות כמו כינין למלריה - כל אלו הפכו את הכיבוש והשליטה לאפשריים יותר מאשר בעבר.</li>
        <li>**תירוצים אידיאולוגיים:** אידיאולוגיות של עליונות גזעית ו"הנטל של האדם הלבן" שימשו להצדקת הכיבוש, בטענה שהאירופאים מביאים "תרבות" ו"קידמה" לעמים ה"פרימיטיביים".</li>
    </ul>

    <p>התחרות הפרועה על אזורים באפריקה איימה להצית סכסוכים בין המעצמות באירופה עצמה. כדי למנוע זאת, יזם הקנצלר הגרמני אוטו פון ביסמרק כינוס בינלאומי - ועידת ברלין.</p>

    <h3>ועידת ברלין (1884-1885): "התייעצות ידידותית" ששינתה עולם</h3>
    <p>14 מדינות, בעיקר אירופיות, התכנסו בברלין. המטרה הרשמית הייתה לדון בסחר ובניווט באפריקה. המטרה הלא-רשמית, והחשובה בהרבה, הייתה לקבוע את הכללים לחלוקת היבשת כדי למנוע התנגשויות בין המעצמות. נציגים אפריקאים לא הוזמנו או נכחו - ההחלטות התקבלו על אפריקה, לא איתה או עבורה.</p>

    <p>עיקרי ההחלטות:</p>
    <ul>
        <li>**"כיבוש אפקטיבי":** נקבע שלא מספיק לתבוע בעלות על אזור על המפה. כדי שתביעה תוכר על ידי המעצמות האחרות, המדינה הטוענת הייתה חייבת להוכיח שהיא שולטת בשטח "בפועל" - כלומר, יש לה שם נוכחות מנהלית, צבאית או כלכלית כלשהי. עיקרון זה הגביר עוד יותר את הבהילות והאגרסיביות של המירוץ.</li>
        <li>**חופש שיט:** נהרות מרכזיים כמו קונגו וניז'ר הוכרזו כנתיבי שיט פתוחים לסחר בינלאומי.</li>
        <li>**מדינת קונגו החופשית:** אגן קונגו העצום הוכר כמדינת חסות תחת שלטונו האישי של המלך ליאופולד השני מבלגיה (לא תחת ממשלת בלגיה). השלטון בקונגו הפך לאחד ממשטרי הניצול האכזריים ביותר בהיסטוריה.</li>
    </ul>

    <h3>קוים על המפה, צלקות על היבשת</h3>
    <p>החלטות הוועידה נתנו לגיטימציה בינלאומית לחלוקה שרירותית של אפריקה. הגבולות ששורטטו בבירות אירופה התעלמו לחלוטין ממבנים חברתיים, תרבויות, קבוצות אתניות וממלכות אפריקאיות קיימות. עמים שונים, לעיתים עוינים זה לזה, אוחדו תחת שלטון קולוניאלי אחד, בעוד קבוצות אתניות אחרות נחתכו בין מספר קולוניות שונות. חלוקה מלאכותית זו הותירה צלקות עמוקות שרבות מהן משפיעות על יציבות וגבולות מדינות אפריקה עד היום.</p>

    <h3>ההשלכות - מחיר הכיבוש</h3>
    <p>ההשלכות על אפריקה היו קשות מנשוא:</p>
    <ul>
        <li>**אובדן ריבונות ועצמאות:** מדינות וממלכות אפריקאיות איבדו את שלטונן העצמי.</li>
        <li>**ניצול כלכלי אכזרי:** משאבי טבע וכוח אדם נוצלו באופן אינטנסיבי לטובת המעצמות. כלכלות מקומיות עוצבו מחדש כדי לשרת את הצרכים האימפריאליים.</li>
        <li>**דיכוי ואלימות:** משטרים קולוניאליים רבים היו אכזריים ודיכאו באלימות התקוממויות ודרישות לעצמאות.</li>
        <li>**ערעור חברתי ותרבותי:** מבנים מסורתיים שובשו, ולעיתים קרובות הוטלו בכוח נורמות וערכים אירופיים.</li>
    </ul>

    <p>ועידת ברלין לא החלה את המירוץ, אך היא הסדירה אותו, האיצה אותו, וסיפקה לו מסגרת ו"חוקים" מוסכמים (אירופית). היא הייתה רגע מכונן בהיסטוריה של הקולוניאליזם באפריקה, וסימלה את הפסגה של שליטת המעצמות האירופיות על העולם.</p>
</div>

<style>
    :root {
        --color-primary: #0056b3; /* Darker blue */
        --color-secondary: #e9ecef; /* Light grey background */
        --color-background: #f8f9fa; /* White background */
        --color-border: #ced4da; /* Border color */
        --color-success: #28a745; /* Green for success */
        --color-danger: #dc3545; /* Red for danger */
        --color-warning: #ffc107; /* Yellow/Orange for warning */
        --color-info: #17a2b8; /* Cyan for info */
        --color-unclaimed: #a0a0a0; /* Unclaimed region */
        --map-bg: #d3e9d3; /* Light green map background */

        --color-britain: #c93a3a; /* Muted Red */
        --color-france: #4a7ed9; /* Muted Blue */
        --color-germany: #4caf50; /* Muted Green */
        --color-belgium: #ff9800; /* Muted Orange */
        /* Add more power colors if adding powers */
    }

    #berlin-conference-app {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        max-width: 960px; /* Increased max width */
        margin: 30px auto; /* More margin */
        padding: 25px; /* More padding */
        border: 1px solid var(--color-border);
        border-radius: 12px; /* More rounded corners */
        background-color: var(--color-background);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        display: grid;
        grid-template-areas:
            "info map"
            "controls map"
            "results results";
        grid-template-columns: 300px 1fr; /* Adjusted column width */
        gap: 25px; /* Increased gap */
    }

    #game-info {
        grid-area: info;
        background-color: var(--color-secondary);
        padding: 20px;
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
    }

    #game-info h2 {
        margin-top: 0;
        color: var(--color-primary);
        border-bottom: 2px solid var(--color-border);
        padding-bottom: 10px;
    }
     #game-info h3 {
         color: #555;
         margin-top: 15px;
         margin-bottom: 10px;
     }

    #player-objectives ul {
        padding-right: 20px;
        list-style-type: "✓ "; /* Custom bullet for completed */
    }
     #player-objectives li {
         margin-bottom: 8px;
         line-height: 1.4;
         list-style-type: "☐ "; /* Custom bullet for pending */
     }
     #player-objectives li.complete {
         text-decoration: line-through;
         color: #666;
         list-style-type: "✅ ";
     }


    #map-container {
        grid-area: map;
        display: grid;
        grid-template-columns: repeat(10, 1fr); /* More fixed grid for better shape simulation */
        grid-template-rows: repeat(12, 1fr); /* More rows */
        gap: 3px; /* Reduced gap for denser map */
        border: 1px solid var(--color-border);
        padding: 10px;
        background-color: var(--map-bg);
        /* aspect-ratio: 1.2 / 1; Removing fixed aspect ratio, rely on grid rows/columns */
        max-height: 600px; /* Allow map to grow taller */
        overflow: hidden;
        border-radius: 8px;
        position: relative; /* Needed for overlay */
    }

    /* Manual shaping of the map using grid-area for a more Africa-like feel */
    #map-container .map-region:nth-child(1) { grid-area: 1 / 5 / auto / 6; } /* Top tip */
    #map-container .map-region:nth-child(2) { grid-area: 1 / 6 / auto / 7; }
    #map-container .map-region:nth-child(3) { grid-area: 2 / 4 / auto / 5; }
    #map-container .map-region:nth-child(4) { grid-area: 2 / 5 / auto / 6; }
    #map-container .map-region:nth-child(5) { grid-area: 2 / 6 / auto / 7; }
    #map-container .map-region:nth-child(6) { grid-area: 2 / 7 / auto / 8; }
    #map-container .map-region:nth-child(7) { grid-area: 3 / 3 / auto / 4; }
    #map-container .map-region:nth-child(8) { grid-area: 3 / 4 / auto / 5; }
    #map-container .map-region:nth-child(9) { grid-area: 3 / 5 / auto / 6; }
    #map-container .map-region:nth-child(10) { grid-area: 3 / 6 / auto / 7; }
    #map-container .map-region:nth-child(11) { grid-area: 3 / 7 / auto / 8; }
    #map-container .map-region:nth-child(12) { grid-area: 3 / 8 / auto / 9; }
    #map-container .map-region:nth-child(13) { grid-area: 4 / 2 / auto / 3; }
    #map-container .map-region:nth-child(14) { grid-area: 4 / 3 / auto / 4; }
    #map-container .map-region:nth-child(15) { grid-area: 4 / 4 / auto / 5; }
    #map-container .map-region:nth-child(16) { grid-area: 4 / 5 / auto / 6; }
    #map-container .map-region:nth-child(17) { grid-area: 4 / 6 / auto / 7; }
    #map-container .map-region:nth-child(18) { grid-area: 4 / 7 / auto / 8; }
    #map-container .map-region:nth-child(19) { grid-area: 4 / 8 / auto / 9; }
    #map-container .map-region:nth-child(20) { grid-area: 5 / 1 / auto / 2; }
    #map-container .map-region:nth-child(21) { grid-area: 5 / 2 / auto / 3; }
    #map-container .map-region:nth-child(22) { grid-area: 5 / 3 / auto / 4; }
    #map-container .map-region:nth-child(23) { grid-area: 5 / 4 / auto / 5; }
    #map-container .map-region:nth-child(24) { grid-area: 5 / 5 / auto / 6; }
    #map-container .map-region:nth-child(25) { grid-area: 5 / 6 / auto / 7; }
    #map-container .map-region:nth-child(26) { grid-area: 5 / 7 / auto / 8; }
    #map-container .map-region:nth-child(27) { grid-area: 5 / 8 / auto / 9; }
    #map-container .map-region:nth-child(28) { grid-area: 5 / 9 / auto / 10; }
    #map-container .map-region:nth-child(29) { grid-area: 6 / 1 / auto / 2; }
    #map-container .map-region:nth-child(30) { grid-area: 6 / 2 / auto / 3; }
    #map-container .map-region:nth-child(31) { grid-area: 6 / 3 / auto / 4; }
    #map-container .map-region:nth-child(32) { grid-area: 6 / 4 / auto / 5; }
    #map-container .map-region:nth-child(33) { grid-area: 6 / 5 / auto / 6; }
    #map-container .map-region:nth-child(34) { grid-area: 6 / 6 / auto / 7; }
    #map-container .map-region:nth-child(35) { grid-area: 6 / 7 / auto / 8; }
    #map-container .map-region:nth-child(36) { grid-area: 6 / 8 / auto / 9; }
    #map-container .map-region:nth-child(37) { grid-area: 6 / 9 / auto / 10; }
    #map-container .map-region:nth-child(38) { grid-area: 7 / 2 / auto / 3; }
    #map-container .map-region:nth-child(39) { grid-area: 7 / 3 / auto / 4; }
    #map-container .map-region:nth-child(40) { grid-area: 7 / 4 / auto / 5; }
    #map-container .map-region:nth-child(41) { grid-area: 7 / 5 / auto / 6; }
    #map-container .map-region:nth-child(42) { grid-area: 7 / 6 / auto / 7; }
    #map-container .map-region:nth-child(43) { grid-area: 7 / 7 / auto / 8; }
    #map-container .map-region:nth-child(44) { grid-area: 7 / 8 / auto / 9; }
    #map-container .map-region:nth-child(45) { grid-area: 8 / 3 / auto / 4; }
    #map-container .map-region:nth-child(46) { grid-area: 8 / 4 / auto / 5; }
    #map-container .map-region:nth-child(47) { grid-area: 8 / 5 / auto / 6; }
    #map-container .map-region:nth-child(48) { grid-area: 8 / 6 / auto / 7; }
    #map-container .map-region:nth-child(49) { grid-area: 9 / 4 / auto / 5; }
    #map-container .map-region:nth-child(50) { grid-area: 9 / 5 / auto / 6; }
    /* If NUM_REGIONS is > 50, need to add more grid-area definitions */


    .map-region {
        background-color: var(--color-unclaimed); /* Unclaimed color */
        border: 1px solid #666;
        cursor: pointer;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px; /* Larger icons/text */
        color: rgba(255, 255, 255, 0.9);
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        font-weight: bold;
        position: relative; /* For animation */
        border-radius: 3px;
         overflow: hidden; /* Hide overflowing text/icons if they get big */
    }

    .map-region .region-icon {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        opacity: 0.8;
        transition: opacity 0.3s ease;
    }
     .map-region.claimed .region-icon {
         display: none; /* Hide icons once claimed */
     }


    .map-region.claimed {
        cursor: default;
        border-color: transparent; /* Hide border when claimed */
    }

    .map-region:not(.claimed):hover {
        background-color: #b0b0b0; /* Darker grey on hover */
         transform: scale(1.05); /* Slightly enlarge on hover */
         z-index: 1; /* Bring to front on hover */
    }
     .map-region:not(.claimed):active {
         transform: scale(0.98); /* Squash effect on click */
     }

     /* Animation for claiming */
     @keyframes pulse {
         0% { box-shadow: 0 0 0 0 rgba(255, 255, 0, 0.7); }
         70% { box-shadow: 0 0 0 10px rgba(255, 255, 0, 0); }
         100% { box-shadow: 0 0 0 0 rgba(255, 255, 0, 0); }
     }
     .map-region.claiming {
         animation: pulse 0.8s ease-out forwards;
         border: 2px dashed var(--color-warning); /* Visual cue for claimed this turn */
     }

     /* Animation for AI claiming */
     @keyframes ai-pulse {
         0% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.5); }
         70% { box-shadow: 0 0 0 8px rgba(255, 0, 0, 0); }
         100% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0); }
     }
     .map-region.ai-claiming {
         animation: ai-pulse 0.6s ease-out forwards;
          border: 2px dashed var(--color-danger); /* Visual cue for claimed by AI this turn */
     }


    #game-controls {
        grid-area: controls;
        display: flex;
        flex-direction: column;
        gap: 15px; /* Increased gap */
        align-items: center;
         padding: 15px;
         background-color: var(--color-secondary);
         border-radius: 8px;
         box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
    }

    #end-turn-button {
        width: 80%; /* Wider button */
        padding: 12px 25px; /* More padding */
        font-size: 18px; /* Larger font */
        cursor: pointer;
        background-color: var(--color-primary);
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #end-turn-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
         transform: none;
    }

    #end-turn-button:hover:not(:disabled) {
        background-color: #004085; /* Darker shade on hover */
         transform: translateY(-2px); /* Lift effect on hover */
    }
     #end-turn-button:active:not(:disabled) {
         transform: translateY(0); /* Press effect */
     }


    #turn-results {
        grid-area: results;
        margin-top: 0; /* No top margin needed due to grid */
        padding: 20px;
        border: 1px solid var(--color-border);
        border-radius: 8px;
        background-color: #fff; /* White background for log */
        max-height: 200px; /* Increased height */
        overflow-y: auto;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    #turn-results h3 {
         margin-top: 0;
         color: #333;
         border-bottom: 1px solid var(--color-border);
         padding-bottom: 8px;
         margin-bottom: 10px;
    }

     #turn-results ul {
        list-style: none;
        padding: 0;
        margin: 0;
     }
    #turn-results li {
        margin-bottom: 8px;
        padding-bottom: 8px;
        border-bottom: 1px dotted #e0e0e0;
        font-size: 15px;
         line-height: 1.5;
    }
     #turn-results li:last-child {
         border-bottom: none;
         margin-bottom: 0;
     }
     #turn-results li:first-child {
         font-weight: bold; /* Make newest entry stand out */
     }


    .modal {
        display: none;
        position: fixed;
        z-index: 10; /* Higher z-index */
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.6); /* Darker overlay */
        padding-top: 80px; /* Pushed down slightly */
        backdrop-filter: blur(5px); /* Blur effect */
    }

    .modal-content {
        background-color: #fefefe;
        margin: 5% auto;
        padding: 30px; /* More padding */
        border: 1px solid #888;
        width: 90%;
        max-width: 500px; /* Slightly wider modal */
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        position: relative; /* For close button positioning */
    }
     .modal-content h2 {
         color: var(--color-primary);
         margin-top: 0;
         margin-bottom: 20px;
     }
     .modal-content p {
         margin-bottom: 15px;
         line-height: 1.6;
     }


    .close-button {
        color: #aaa;
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 30px;
        font-weight: bold;
        cursor: pointer;
        transition: color 0.2s ease;
    }

    .close-button:hover,
    .close-button:focus {
        color: #333;
        text-decoration: none;
    }

     .modal-button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        background-color: var(--color-success);
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 15px;
     }
      .modal-button:hover {
          background-color: #218838;
           transform: translateY(-1px);
      }
       .modal-button:active {
          transform: translateY(0);
       }


    #toggle-explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 18px;
        cursor: pointer;
        background-color: #6c757d; /* Grey button */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
     #toggle-explanation-button:hover {
         background-color: #5a6268;
          transform: translateY(-2px);
     }
     #toggle-explanation-button:active {
         transform: translateY(0);
     }


    #historical-explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid var(--color-border);
        border-radius: 8px;
        background-color: #fefefe;
        direction: rtl;
        font-family: 'Arial', sans-serif;
        max-width: 960px;
        margin: 20px auto;
        line-height: 1.7; /* Increased line height */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.07);
    }

    #historical-explanation h2,
    #historical-explanation h3 {
        color: #333;
        margin-bottom: 15px;
        padding-bottom: 5px;
        border-bottom: 1px dotted #ccc;
    }
    #historical-explanation h2 {
        color: var(--color-primary);
         border-bottom: 2px solid var(--color-primary);
          margin-bottom: 20px;
    }


    #historical-explanation ul {
        padding-right: 25px; /* Adjusted padding */
        margin-bottom: 15px;
    }
    #historical-explanation li {
        margin-bottom: 8px;
    }
     #historical-explanation p {
         margin-bottom: 15px;
     }

     /* Specific colors for powers */
     .owner-britain { background-color: var(--color-britain); }
     .owner-france { background-color: var(--color-france); }
     .owner-germany { background-color: var(--color-germany); }
     .owner-belgium { background-color: var(--color-belgium); }
     /* Add more classes for more powers */


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const mapContainer = document.getElementById('map-container');
        const gameInfo = document.getElementById('game-info');
        const currentTurnSpan = document.getElementById('current-turn');
        const playerPowerNameSpan = document.getElementById('player-power-name');
        const playerClaimPointsSpan = document.getElementById('player-claim-points');
        const objectivesList = document.getElementById('objectives-list');
        const endTurnButton = document.getElementById('end-turn-button');
        const resultsList = document.getElementById('results-list');
        const gameEndModal = document.getElementById('game-end-modal');
        const startModal = document.getElementById('start-modal'); // Added start modal
        const startGameButton = document.getElementById('start-game-button'); // Added start button
        const finalScoresDiv = document.getElementById('final-scores');
        const closeModalButton = gameEndModal.querySelector('.close-button');

        const toggleExplanationButton = document.getElementById('toggle-explanation-button');
        const historicalExplanation = document.getElementById('historical-explanation');

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = historicalExplanation.style.display === 'none';
            historicalExplanation.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסיפור שמאחורי המשחק' : 'הצג/הסתר הסיפור שמאחורי המשחק';
        });


        // --- Game Setup ---
        const NUM_REGIONS = 50; // Simplified number of regions
        const MAX_TURNS = 10; // Max turns for the simulation

        const playerPowers = [
            { name: 'בריטניה', id: 'britain', color: 'var(--color-britain)' },
            { name: 'צרפת', id: 'france', color: 'var(--color-france)' },
            { name: 'גרמניה', id: 'germany', color: 'var(--color-germany)' },
            { name: 'בלגיה', id: 'belgium', color: 'var(--color-belgium)' },
            // Add more powers as needed
        ];

        const userPlayerId = playerPowers[0].id; // User plays as the first power

        let regions = []; // Array to hold region state
        let turn = 0; // Start at turn 0 before the first turn begins
        let playerClaimPoints = 0;
        const STARTING_CLAIM_POINTS = 3; // Points per turn - Adjusted for smaller map
        let userClaimsThisTurn = 0;
        const MAX_CLAIMS_PER_TURN = 2; // Limit user claims per turn

        // Simple Objectives (can be expanded)
        const OBJECTIVE_TYPES = {
             COASTAL: 'coastal', // Icon: 🌊
             RICH_RESOURCES: 'resources', // Icon: 💎
             INLAND_CONTROL: 'inland' // Icon: 🌳
        };

        // Distribution of region types - Ensure total matches NUM_REGIONS
        const REGION_TYPES = [
             { type: OBJECTIVE_TYPES.COASTAL, count: 12 }, // Approx coastal regions
             { type: OBJECTIVE_TYPES.RICH_RESOURCES, count: 10 }, // Approx resource regions
             { type: OBJECTIVE_TYPES.INLAND_CONTROL, count: NUM_REGIONS - 22 } // Remaining inland regions
        ];


        let playerObjectives = {};
        const NUM_OBJECTIVES_PER_PLAYER = 2; // Number of objectives each player gets
        const OBJECTIVE_POINTS = 10; // Points awarded for completing an objective

        // --- Initialize Game ---
        function initializeGame() {
            regions = [];
            mapContainer.innerHTML = ''; // Clear map
            resultsList.innerHTML = ''; // Clear results
            userClaimsThisTurn = 0; // Reset claims for turn 1
            playerClaimPoints = STARTING_CLAIM_POINTS; // Initial points

            // Assign region types randomly
            const regionTypesPool = [];
             REGION_TYPES.forEach(rt => {
                 for(let i = 0; i < rt.count; i++) {
                     regionTypesPool.push(rt.type);
                 }
             });
             // Shuffle the pool
             for (let i = regionTypesPool.length - 1; i > 0; i--) {
                 const j = Math.floor(Math.random() * (i + 1));
                 [regionTypesPool[i], regionTypesPool[j]] = [regionTypesPool[j], regionTypesPool[i]];
             }


            for (let i = 0; i < NUM_REGIONS; i++) {
                const region = {
                    id: i,
                    owner: null, // null means unclaimed
                    type: regionTypesPool[i] || 'inland', // Assign type from shuffled pool
                    claimedThisTurn: null // Player ID who claimed it this turn
                };
                regions.push(region);

                const regionElement = document.createElement('div');
                regionElement.classList.add('map-region');
                regionElement.dataset.regionId = i;
                regionElement.dataset.regionType = region.type; // Store type on element

                // Add visual indicator for type (emoji/icon)
                 const iconSpan = document.createElement('span');
                 iconSpan.classList.add('region-icon');
                 switch(region.type) {
                     case OBJECTIVE_TYPES.COASTAL: iconSpan.textContent = '🌊'; break;
                     case OBJECTIVE_TYPES.RICH_RESOURCES: iconSpan.textContent = '💎'; break;
                     case OBJECTIVE_TYPES.INLAND_CONTROL: iconSpan.textContent = '🌳'; break;
                     default: iconSpan.textContent = '';
                 }
                 regionElement.appendChild(iconSpan);


                regionElement.addEventListener('click', handleRegionClick);
                mapContainer.appendChild(regionElement);
            }

             // Assign Objectives
             playerObjectives = {}; // Reset objectives
             playerPowers.forEach(power => {
                 playerObjectives[power.id] = [];
                 const availableObjectives = Object.values(OBJECTIVE_TYPES);
                 // Shuffle available objective types for *this player*
                 const playerSpecificObjectivesPool = [...availableObjectives]; // Copy
                  for (let i = playerSpecificObjectivesPool.length - 1; i > 0; i--) {
                     const j = Math.floor(Math.random() * (i + 1));
                     [playerSpecificObjectivesPool[i], playerSpecificObjectivesPool[j]] = [playerSpecificObjectivesPool[j], playerSpecificObjectivesPool[i]];
                 }

                 // Assign N random unique objectives
                 for(let i = 0; i < NUM_OBJECTIVES_PER_PLAYER && i < playerSpecificObjectivesPool.length; i++){
                     playerObjectives[power.id].push({ type: playerSpecificObjectivesPool[i], complete: false });
                 }
             });


            turn = 1; // Game starts on turn 1
            updateGameInfo();
            updateMapDisplay();
            endTurnButton.disabled = false;

             // Update UI for user objectives
             updateObjectivesDisplay();
             addResult(`--- ועידת ברלין נפתחה! תור ${turn} מתחיל. ---`, '#0056b3');
        }

         function updateObjectivesDisplay() {
             objectivesList.innerHTML = '';
             const userObjectives = playerObjectives[userPlayerId];
             userObjectives.forEach(obj => {
                 const li = document.createElement('li');
                 li.classList.toggle('complete', obj.complete);
                 let typeText = '';
                 let typeIcon = '';
                 switch(obj.type) {
                     case OBJECTIVE_TYPES.COASTAL: typeText = 'אזורי חוף'; typeIcon = '🌊'; break;
                     case OBJECTIVE_TYPES.RICH_RESOURCES: typeText = 'אזורי משאבים'; typeIcon = '💎'; break;
                     case OBJECTIVE_TYPES.INLAND_CONTROL: typeText = 'אזורים פנימיים'; typeIcon = '🌳'; break;
                     default: typeText = obj.type; typeIcon = '';
                 }
                  // Simple objective: Own at least 2 of the specific region type
                 const regionsOfType = regions.filter(r => r.type === obj.type);
                 const ownedRegionsOfType = regionsOfType.filter(r => r.owner === userPlayerId);
                 const required = 2; // Threshold can be adjusted
                 li.textContent = `שליטה ב-${required} ${typeText} ${typeIcon} (${ownedRegionsOfType.length}/${required})`;

                 objectivesList.appendChild(li);
             });
         }

        function updateGameInfo() {
            const userPower = playerPowers.find(p => p.id === userPlayerId);
            currentTurnSpan.textContent = turn;
            playerPowerNameSpan.textContent = userPower.name;
            playerClaimPointsSpan.textContent = playerClaimPoints;
        }

        function updateMapDisplay() {
            regions.forEach(region => {
                const regionElement = mapContainer.querySelector(`[data-region-id="${region.id}"]`);
                regionElement.className = 'map-region'; // Reset classes

                if (region.owner) {
                    const ownerPower = playerPowers.find(p => p.id === region.owner);
                    regionElement.style.backgroundColor = ownerPower.color;
                    regionElement.classList.add('claimed', `owner-${region.owner}`);
                     // Remove any temporary claim classes
                     regionElement.classList.remove('claiming', 'ai-claiming');
                     // Ensure icon is hidden
                     const iconSpan = regionElement.querySelector('.region-icon');
                     if(iconSpan) iconSpan.style.display = 'none';

                } else {
                    regionElement.style.backgroundColor = var(--color-unclaimed); // Unclaimed color
                    regionElement.classList.remove('claimed', ...playerPowers.map(p => `owner-${p.id}`));
                     // Ensure icon is visible
                    const iconSpan = regionElement.querySelector('.region-icon');
                    if(iconSpan) iconSpan.style.display = 'block';


                    // Handle temporary claim highlights
                     if (region.claimedThisTurn === userPlayerId) {
                        regionElement.classList.add('claiming');
                     } else if (region.claimedThisTurn !== null) {
                          regionElement.classList.add('ai-claiming');
                     } else {
                         regionElement.classList.remove('claiming', 'ai-claiming');
                     }
                }
            });
        }

        function addResult(text, color = 'black') {
            const li = document.createElement('li');
            li.textContent = text;
            li.style.color = color;
             li.style.opacity = 0; // Start invisible for animation
             li.style.transform = 'translateY(10px)'; // Start slightly down
             li.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';

            resultsList.prepend(li); // Add to the top

             // Trigger animation
             setTimeout(() => {
                 li.style.opacity = 1;
                 li.style.transform = 'translateY(0)';
             }, 50); // Small delay

            // Limit results list length
             while (resultsList.childElementCount > 15) { // Allow a few more results
                 resultsList.removeChild(resultsList.lastChild);
             }
        }

        // --- Player Turn ---
        function handleRegionClick(event) {
            const regionElement = event.target.closest('.map-region'); // Use closest in case icon is clicked
            if (!regionElement) return;

            const regionId = parseInt(regionElement.dataset.regionId);
            const region = regions.find(r => r.id === regionId);

            // Check if click is valid for claiming
            if (region.owner === null && region.claimedThisTurn === null && userClaimsThisTurn < MAX_CLAIMS_PER_TURN && playerClaimPoints > 0) {
                // Simple claiming rule: 1 point per claim
                region.claimedThisTurn = userPlayerId;
                playerClaimPoints--;
                userClaimsThisTurn++;

                 // Add claiming class for animation
                 regionElement.classList.add('claiming');

                addResult(`האימפריה שלך תבעה את אזור מספר ${region.id + 1}!`, 'blue');
                updateGameInfo();
                 updateMapDisplay(); // Update map to show claim highlight


            } else if (region.owner === userPlayerId) {
                // addResult(`אזור מספר ${region.id + 1} כבר בשליטתך.`, '#555'); // Too chatty?
            } else if (region.owner !== null) {
                 const ownerPower = playerPowers.find(p => p.id === region.owner);
                addResult(`אזור מספר ${region.id + 1} כבר נתבע על ידי ${ownerPower.name}!`, 'red');
            } else if (region.claimedThisTurn !== null) {
                const claimedByPower = playerPowers.find(p => p.id === region.claimedThisTurn);
                 addResult(`אזור מספר ${region.id + 1} כבר נתבע על ידי ${claimedByPower.name} בתור זה!`, 'red');
             } else if (userClaimsThisTurn >= MAX_CLAIMS_PER_TURN) {
                 addResult(`הגעת למכסת התביעות שלך בתור זה (${MAX_CLAIMS_PER_TURN}). סיים תור.`, 'orange');
            } else if (playerClaimPoints <= 0) {
                 addResult('אין לך מספיק עתודות תביעה לתבוע אזורים נוספים בתור זה.', 'orange');
             }
        }

        endTurnButton.addEventListener('click', endTurn);

        // --- End Turn / AI Turn / Resolve ---
        function endTurn() {
            endTurnButton.disabled = true;
            addResult(`--- מסתיים תור ${turn} ---`, '#333');

            // AI Claims
            const aiPowers = playerPowers.filter(p => p.id !== userPlayerId);
             // Simple AI: Each AI claims random unclaimed regions if points allow
             aiPowers.forEach(aiPower => {
                 let availableRegionsForAI = regions.filter(r => r.owner === null && r.claimedThisTurn === null);
                 let aiClaimPoints = STARTING_CLAIM_POINTS; // AI also gets points
                 let aiClaims = 0;
                 const aiMaxClaims = 1; // Simple AI claims fewer regions per turn

                 // Shuffle available regions for this AI to make it less predictable
                 for (let i = availableRegionsForAI.length - 1; i > 0; i--) {
                     const j = Math.floor(Math.random() * (i + 1));
                     [availableRegionsForAI[i], availableRegionsForAI[j]] = [availableRegionsForAI[j], availableRegionsForAI[i]];
                 }


                 while(aiClaims < aiMaxClaims && availableRegionsForAI.length > 0 && aiClaimPoints > aiClaims) { // AI uses 1 point per claim
                      // Pick the first available region after shuffle
                     const regionToClaim = availableRegionsForAI.shift(); // Use shift to remove it

                     regionToClaim.claimedThisTurn = aiPower.id;
                     aiClaims++;
                     addResult(`${aiPower.name} נכנסה למירוץ ותבעה את אזור מספר ${regionToClaim.id + 1}.`, aiPower.color);

                      // Add AI claiming class for animation
                     const regionElement = mapContainer.querySelector(`[data-region-id="${regionToClaim.id}"]`);
                     if(regionElement) regionElement.classList.add('ai-claiming');
                 }
             });


             // Resolve claims after a short delay to allow animations to start
             setTimeout(() => {
                 resolveClaims();
             }, 800); // Delay matches animation duration

        }

        function resolveClaims() {
             const claimedRegionsThisTurn = regions.filter(r => r.claimedThisTurn !== null);
            // Resolution priority: User first, then AI in playerPowers order.
            // This simulates user having initiative or a slight advantage in their turn.
             claimedRegionsThisTurn.sort((a, b) => {
                  const order = playerPowers.map(p => p.id);
                  const orderA = order.indexOf(a.claimedThisTurn);
                  const orderB = order.indexOf(b.claimedThisTurn);

                 if (orderA === orderB) {
                     // If same power claimed, potentially a conflict or double claim (handle simply by first processed wins)
                     return 0;
                 }
                 // User gets highest priority (index 0)
                 return orderA - orderB;
             });

            claimedRegionsThisTurn.forEach(region => {
                const claimingPowerId = region.claimedThisTurn;
                const claimingPower = playerPowers.find(p => p.id === claimingPowerId);
                 const regionElement = mapContainer.querySelector(`[data-region-id="${region.id}"]`);


                if (region.owner === null) { // Only assign if not already owned
                    region.owner = claimingPowerId;
                     // Add success animation/class?
                    addResult(`התביעה של ${claimingPower.name} על אזור מספר ${region.id + 1} הצליחה! (כיבוש אפקטיבי!)`, claimingPower.color);
                } else if (region.owner === claimingPowerId) {
                     // This case can happen if AI claims a region user already claimed this turn (lower priority)
                     // Or if AI claims a region AI already claimed this turn (lower priority)
                     // No message needed here, the region is already owned by this power.
                }
                else {
                     // Claim failed because another power already owns it
                     const ownerPower = playerPowers.find(p => p.id === region.owner);
                     addResult(`התביעה של ${claimingPower.name} על אזור מספר ${region.id + 1} נכשלה - האזור בשליטת ${ownerPower.name}.`, 'red');
                 }

                 // Clean up claiming state and classes
                 region.claimedThisTurn = null;
                 if(regionElement) {
                     regionElement.classList.remove('claiming', 'ai-claiming');
                     // Ensure map display is updated after resolution
                      setTimeout(() => {
                          updateMapDisplay();
                      }, 100); // Short delay for final color update
                 }
            });

             // Update objectives status
             playerPowers.forEach(power => {
                 playerObjectives[power.id].forEach(obj => {
                     if (!obj.complete) {
                          const regionsOfType = regions.filter(r => r.type === obj.type);
                          const ownedRegionsOfType = regionsOfType.filter(r => r.owner === power.id);
                         const required = 2; // Threshold
                         if (ownedRegionsOfType.length >= required) {
                             obj.complete = true;
                             if (power.id === userPlayerId) {
                                 addResult(`השלמת יעד אימפריאלי: שליטה ב-${obj.type}ים! (+${OBJECTIVE_POINTS} נקודות סיום)`, 'green');
                             } else {
                                addResult(`${power.name} השלים יעד אימפריאלי: שליטה ב-${obj.type}ים!`, '#555'); // Less prominent for AI
                             }
                         }
                     }
                 });
             });


            // Prepare for next turn
            turn++;
            playerClaimPoints += STARTING_CLAIM_POINTS; // Replenish points
            userClaimsThisTurn = 0;

            updateGameInfo();
            updateObjectivesDisplay(); // Update objective status


            // Check end game conditions
            if (turn > MAX_TURNS || regions.every(r => r.owner !== null)) {
                // Game ends after MAX_TURNS or when all regions are claimed
                endGame();
            } else {
                 addResult(`--- תור ${turn} התחיל! זמן לתביעות חדשות. ---`, '#0056b3');
                endTurnButton.disabled = false;
            }
        }

        // --- End Game ---
        function endGame() {
            endTurnButton.disabled = true;
            addResult("--- ועידת ברלין הסתיימה! המפה נחרצה. ---", 'purple');

            let scores = {};
            playerPowers.forEach(p => scores[p.id] = { regions: 0, objectives: 0, total: 0 });

            regions.forEach(region => {
                if (region.owner) {
                    scores[region.owner].regions++;
                }
            });

             playerPowers.forEach(p => {
                 playerObjectives[p.id].forEach(obj => {
                     if (obj.complete) {
                         scores[p.id].objectives += OBJECTIVE_POINTS; // Points for objectives
                     }
                 });
                 scores[p.id].total = scores[p.id].regions + scores[p[id]].objectives; // Each region is 1 point
             });

             // Calculate points for user - user gets 1 point per region owned
             scores[userPlayerId].total = scores[userPlayerId].regions + scores[userPlayerId].objectives;

             // AI also gets points for regions (optional, depends on desired scoring complexity)
             // Simple score: regions + objectives for everyone
             playerPowers.forEach(p => {
                  if (p.id !== userPlayerId) {
                     scores[p.id].total = scores[p.id].regions + scores[p.id].objectives;
                 }
             });


            // Sort scores for display
            const sortedScores = Object.entries(scores).sort(([, a], [, b]) => b.total - a.total);

            finalScoresDiv.innerHTML = '<h3>תוצאות סופיות:</h3>';
            sortedScores.forEach(([playerId, score]) => {
                 const powerName = playerPowers.find(p => p.id === playerId).name;
                 finalScoresDiv.innerHTML += `<p><strong>${powerName}</strong>: אזורים בשליטה - ${score.regions}, נקודות יעדים - ${score.objectives}, סך הכל - ${score.total} נקודות</p>`;
            });

             // Determine winner
             const winnerId = sortedScores[0][0];
             const winnerName = playerPowers.find(p => p.id === winnerId).name;
             const userPower = playerPowers.find(p => p.id === userPlayerId).name;

             let endMessage = "";
             if (winnerId === userPlayerId) {
                 endMessage = `כל הכבוד! האימפריה של ${userPower} ניצחה במירוץ לאפריקה!`;
             } else {
                  endMessage = `האימפריה של ${winnerName} ניצחה במירוץ! ${userPower} סיימה במקום #${sortedScores.findIndex(([id,]) => id === userPlayerId) + 1}.`;
             }
             finalScoresDiv.innerHTML = `<h3>${endMessage}</h3>` + finalScoresDiv.innerHTML;


            gameEndModal.style.display = "block";
        }

        // Close modal
        closeModalButton.onclick = function() {
            gameEndModal.style.display = "none";
             // Can add logic here to reset or go to a main menu
        }

        // Close modal if clicking outside
        window.onclick = function(event) {
            if (event.target == gameEndModal) {
                gameEndModal.style.display = "none";
            }
             if (event.target == startModal) { // Also close start modal
                startModal.style.display = "none";
            }
        }

         // Start game button in modal
        startGameButton.addEventListener('click', () => {
            startModal.style.display = 'none';
            initializeGame(); // Start the actual game
        });

        // Show start modal when page loads
        startModal.style.display = "block";

        // Initial map display might be needed even before game starts if not using modal
        // updateMapDisplay();
    });
</script>
```