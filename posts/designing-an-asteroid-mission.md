---
title: "מתכננים משימה לאסטרואיד"
english_slug: designing-an-asteroid-mission
category: "טכנולוגיה / אווירונאוטיקה וחלל"
tags:
  - אסטרואידים
  - רובוטיקה
  - תכנון משימה
  - חלל
  - הנדסת מערכות
---
# מתכננים משימה לאסטרואיד

האם אתם מוכנים לאתגר? הצטרפו אלינו למרכז בקרת המשימה וצאו למסע אל עומק החלל! משימה קריטית לפנינו: שליחת רובוט חלל לאסוף דגימות יקרות מפז מאסטרואיד רחוק. משימות כאלו הן פסגת ההנדסה האנושית ודורשות תכנון מדוקדק תחת מגבלות קשוחות. מהם השיקולים המכריעים שעליכם לקחת בחשבון כדי שהרובוט יצליח במשימתו ויחזור עם שלל מדעי, מבלי לחרוג מהתקציב? המפה לפניכם, המשאבים מוגבלים, והאסטרואיד מחכה. בואו נתחיל לתכנן!

<div class="app-container">
    <div class="map-area">
        <h2>מפת אסטרואיד: אזורי חקר</h2>
        <div id="asteroid-map">
            <!-- Asteroid surface background -->
            <div class="poi-marker" id="poi-1" data-poi-id="1" style="top: 10%; left: 15%;">
                <div class="poi-icon"></div>
                <div class="poi-label">אבן מגנטית</div>
                 <div class="poi-value">ערך: 30</div>
            </div>
            <div class="poi-marker" id="poi-2" data-poi-id="2" style="top: 30%; left: 60%;">
                <div class="poi-icon"></div>
                <div class="poi-label">רגולית עדין</div>
                 <div class="poi-value">ערך: 10</div>
            </div>
            <div class="poi-marker" id="poi-3" data-poi-id="3" style="top: 55%; left: 30%;">
                 <div class="poi-icon"></div>
                <div class="poi-label">סלע פחמני</div>
                 <div class="poi-value">ערך: 40</div>
            </div>
            <div class="poi-marker" id="poi-4" data-poi-id="4" style="top: 70%; left: 80%;">
                 <div class="poi-icon"></div>
                <div class="poi-label">מכתש אימפקט</div>
                 <div class="poi-value">ערך: 20</div>
            </div>
            <div class="poi-marker" id="poi-5" data-poi-id="5" style="top: 85%; left: 45%;">
                 <div class="poi-icon"></div>
                <div class="poi-label">צבר חלקיקים</div>
                 <div class="poi-value">ערך: 25</div>
            </div>
             <div id="rover" class="rover-icon" style="display: none;"></div>
        </div>
    </div>
    <div class="planning-area">
        <h2>מרכז תכנון משימה: ניהול משאבים</h2>
        <div class="budget-display">
            <h3>בנק משאבים:</h3>
            <p>זמן זמין: <span id="budget-time">100</span> יחידות</p>
            <p>אנרגיה זמינה: <span id="budget-energy">150</span> יחידות</p>
            <p>אחסון דגימות זמין: <span id="budget-storage">5</span> יחידות נפח</p>
        </div>
        <div class="budget-display planned-costs">
            <h3>עלות מתוכננת:</h3>
            <p>זמן כולל: <span id="planned-time">0</span></p>
            <p>אנרגיה כוללת: <span id="planned-energy">0</span></p>
            <p>אחסון נדרש: <span id="planned-storage">0</span></p>
            <p>ערך מדעי מצופה: <span id="planned-value">0</span></p>
        </div>
        <div id="mission-sequence" class="sequence-drop-target">
            <h3>רצף פעולות: גרור נקודות עניין לכאן</h3>
            <ul id="sequence-list">
                <!-- Planned steps will appear here -->
            </ul>
        </div>
        <button id="run-simulation">הרץ סימולציה!</button>
        <div id="simulation-output" class="log-output"></div>
    </div>
</div>

<button id="toggle-explanation">מעוניינים לדעת עוד? לחצו להסבר מלא</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: מתכננים משימה לאסטרואיד</h2>

    <h3>מהם אסטרואידים ומדוע כדאי לחקור אותם?</h3>
    <p>אסטרואידים הם שרידים קדומים מימי היווצרות מערכת השמש לפני כ-4.6 מיליארד שנים. הם משמשים כ"קפסולות זמן" קוסמיות, השומרות מידע על החומרים מהם נוצרו הכוכבים וכוכבי הלכת. חקר הרכבם יכול לשפוך אור על מקור המים והחומרים האורגניים שהגיעו לכדור הארץ ואפשרו את החיים. מעבר לערך המדעי העצום, הבנת האסטרואידים חיונית גם להגנה פלנטרית - זיהוי ומעקב אחר אסטרואידים קרובי ארץ בעלי פוטנציאל סיכון.</p>

    <h3>האתגרים הייחודיים של משימות לאסטרואידים</h3>
    <p>שליחת חללית לאסטרואיד אינה עניין של מה בכך. המרחק העצום אומר שנים של מסע ותקשורת עם השהייה ארוכה (דקות ואף שעות לכל כיוון), מה שמחייב אוטונומיה גבוהה של הרובוט. כבידת האסטרואיד זעירה, מה שהופך נחיתה לפעולת "עגינה" או ריחוף עדין, ומקשה על היצמדות לפני השטח. סביבת החלל הקשה (קרינה, טמפרטורות קיצוניות) דורשת חומרה עמידה במיוחד. לבסוף, פני השטח של רוב האסטרואידים אינם מוכרים במלואם לפני ההגעה, ולרוב מכוסים בשכבת רגולית (אבק וסלעים) העלולה להסתיר סיכונים (סלעים גדולים, מדרונות, אזורים לא יציבים).</p>

    <h3>רכיבים מרכזיים של משימה רובוטית לאיסוף דגימות</h3>
    <p>משימה טיפוסית כוללת:</p>
    <ul>
        <li>**חללית האם:** כלי התחבורה הראשי, מוביל את הרובוט הלוך ושוב (במשימות החזרה), אחראי על תמרונים קרובים לאסטרואיד ותקשורת.</li>
        <li>**נחתת/רחפת:** רכב קטן יותר היורד לפני השטח. בכבידה נמוכה, לעיתים מדובר ב"נגיעה קצרה" (Touch-and-Go) בלבד.</li>
        <li>**רובר/זרוע רובוטית:** מאפשרת תנועה מוגבלת על פני השטח או גישה לנקודות עניין קרובות ממקום הנחיתה/עגינה.</li>
        <li>**מכשור מדעי:** מצלמות למיפוי תלת-ממדי והרכבי, ספקטרומטרים לניתוח מרחוק, וכלי איסוף ייעודיים.</li>
    </ul>

    <h3>שלבי תכנון משימה על פני האסטרואיד</h3>
    <p>לאחר ההגעה ליעד, מתחיל שלב התכנון המבצעי המפורט:</p>
    <ol>
        <li>**סיור ובחירת אתר:** סריקה מפורטת של פני השטח לזיהוי אזורים מבטיחים מבחינה מדעית ובטוחים לפעולה.</li>
        <li>**מיפוי מדויק:** יצירת מודלים תלת-ממדיים ומפות הרכב כימי לניווט מדויק ומיקום נקודות העניין.</li>
        <li>**תכנון מסלול ורצף פעולות:** הגדרת סדר הביקור בנקודות העניין שנבחרו, המסלול ביניהן, והפעולות שיבוצעו בכל נקודה (צילום, ניתוח, איסוף דגימה).</li>
        <li>**הערכת משאבים וביצוע סימולציה:** חישוב עלות המשימה המתוכננת (זמן, אנרגיה, אחסון) ווידוא שהיא עומדת במגבלות התקציב.</li>
    </ol>

    <h3>שיקולים בתכנון המסלול ורצף הפעולות</h3>
    <p>תכנון המשימה הוא פאזל מורכב. יש למצוא את האיזון האופטימלי בין:</p>
    <ul>
        <li>**יעילות:** מינימום זמן ואנרגיה למקסימום הישגים מדעיים.</li>
        <li>**בטיחות:** הימנעות ממעבר או פעולה באזורים מסוכנים.</li>
        <li>**ערך מדעי:** נתינת עדיפות לנקודות עניין מבטיחות יותר, גם אם הן דורשות יותר משאבים או כרוכות בסיכון מחושב.</li>
        <li>**מגבלות טכניות:** יכולות התנועה של הרובוט, סוגי הכלים הזמינים, קיבולת האחסון לדגימות.</li>
    </ul>

    <h3>חשיבות ניהול המשאבים</h3>
    <p>במשימות חלל, כל יחידת זמן או אנרגיה היא קריטית. יש לתכנן בקפידה כדי לוודא שהמשימה כולה ניתנת לביצוע במסגרת המשאבים הזמינים. חריגה באחד הפרמטרים (זמן ארוך מדי, צריכת אנרגיה גבוהה מדי, נפח אחסון מלא) עלולה להביא לסיום מוקדם של המשימה או לאי-השלמת היעדים המדעיים העיקריים.</p>

    <h3>כלי איסוף דגימות נפוצים ויתרונות/חסרונות</h3>
    <ul>
        <li>**כף איסוף:** מצוינת לאיסוף מהיר של רגולית רופף ואבק. קלה ומהירה, אך מוגבלת לחומר פני שטח.</li>
        <li>**מקדח:** חודר לעומק כדי לאסוף דגימות "בתוליות" שלא נחשפו לקרינה. דורש אנרגיה רבה ואיטי יותר.</li>
        <li>**זרוע אוספת:** גמישה, יכולה לתפוס סלעים קטנים או לאסוף במגע עדין. מורכבת ודורשת דיוק בתמרון.</li>
    </ul>
    <p>כל כלי מתאים לסוגי חומרים שונים ובעל עלויות שונות מבחינת זמן ואנרגיה. בחירת הכלי הנכון לכל נקודת עניין היא חלק מהתכנון האופטימלי.</p>

    <h3>משימות אסטרואידים לדוגמה והישגיהן</h3>
    <ul>
        <li>**הייאבוסה 1 ו-2 (יפן):** הביאו דגימות בהצלחה מהאסטרואידים איטוקוואה וריוגו. הייאבוסה 2 אף השתמשה בחומר נפץ קטן כדי לחשוף חומר תת-קרקעי ולאסוף אותו, והוכיחה נוכחות מים וחומרים אורגניים בריוגו.</li>
        <li>**אוסיריס-רקס (ארה"ב):** אספה כמות דגימות גדולה במיוחד מהאסטרואיד בנו בטכניקת נגיעה קצרה (TAG), והחזירה אותן לכדור הארץ ב-2023. דגימות אלו צפויות לספק תובנות חסרות תקדים על הרכב אסטרואידים עשירים בפחמן.</li>
    </ul>

    <h3>הצורך בתכנון גמיש ויכולת תגובה לבלתי צפוי</h3>
    <p>גם התכנון הטוב ביותר אינו חסין מהפתעות. פני השטח יכולים להיות שונים מהצפוי, ציוד עלול להתקלקל, או שתתגלה נקודת עניין חדשה ומרתקת. צוותי המשימה חייבים להיות מוכנים להתאים את התוכנית בזמן אמת, לעיתים קרובות בהתבסס על מידע חלקי בלבד. היכולת לקבל החלטות מהירות ואפקטיביות תחת אי-ודאות היא מפתח להצלחת המשימה.</p>
</div>

<style>
/* --- General Styling --- */
body {
    font-family: 'Arial Hebrew', sans-serif; /* Hebrew friendly font */
    line-height: 1.6;
    color: #333;
    background-color: #eef; /* Light bluish background */
    margin: 0;
    padding: 20px;
    direction: rtl; /* Ensure RTL */
    text-align: right; /* Ensure right alignment */
}

h1, h2, h3 {
    color: #1a237e; /* Deep indigo for headings */
    margin-bottom: 15px;
}

h1 {
    text-align: center;
    margin-bottom: 30px;
    color: #0d47a1; /* Dark blue for main title */
}

p, ul, ol {
    margin-bottom: 15px;
}

/* --- App Container Layout --- */
.app-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px; /* Increased gap */
    margin-top: 20px;
    background-color: #fff; /* White background for the app box */
    border: 1px solid #c5cae9; /* Light indigo border */
    border-radius: 12px; /* More rounded corners */
    padding: 25px; /* Increased padding */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}

.map-area, .planning-area {
    flex: 1;
    min-width: 300px; /* Ensure minimum width */
    padding: 15px;
    border-radius: 8px;
    background-color: #f8f9fa; /* Very light grey background */
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05); /* Inner shadow */
    display: flex; /* Use flex for internal layout */
    flex-direction: column;
}

.map-area {
    flex: 2; /* Map takes more space */
}

/* --- Asteroid Map --- */
#asteroid-map {
    width: 100%;
    height: 400px; /* Fixed height */
    background-image: url('https://images.unsplash.com/photo-1534796636687-78b9c30923d8?auto=format&fit=crop&q=80&w=1974&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'); /* Space/asteroid background */
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
    border-radius: 8px; /* Match container border radius */
    border: 1px solid #455a64; /* Dark grey border */
}

.poi-marker {
    position: absolute;
    transform: translate(-50%, -50%); /* Center based on top/left */
    z-index: 1;
    text-align: center;
    color: white;
    cursor: grab;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out; /* Smooth transitions */
    width: 100px; /* Fixed width for marker area */
    font-size: 0.9em;
    display: flex;
    flex-direction: column;
    align-items: center;
    user-select: none; /* Prevent text selection during drag */
}

.poi-marker:hover {
    transform: translate(-50%, -50%) scale(1.1); /* Slight scale up on hover */
    z-index: 5; /* Bring to front on hover */
}

.poi-icon {
    width: 25px;
    height: 25px;
    background-color: #ffeb3b; /* Bright yellow marker */
    border: 3px solid #f57f17; /* Darker yellow border */
    border-radius: 50%; /* Round marker */
    box-shadow: 0 0 10px rgba(255, 235, 59, 0.7); /* Glowing effect */
    margin-bottom: 5px;
    transition: background-color 0.2s ease-in-out;
}

.poi-marker:hover .poi-icon {
     background-color: #fbc02d; /* Darker yellow on hover */
}

.poi-label {
    background-color: rgba(0, 0, 0, 0.6); /* Semi-transparent dark background for text */
    padding: 3px 8px;
    border-radius: 4px;
    white-space: nowrap; /* Prevent wrapping */
    font-weight: bold;
}
.poi-value {
     background-color: rgba(0, 0, 0, 0.6); /* Semi-transparent dark background for text */
    padding: 2px 5px;
    border-radius: 4px;
    white-space: nowrap;
    font-size: 0.8em;
    margin-top: 2px;
}


.poi-marker:active {
    cursor: grabbing;
    transform: translate(-50%, -50%) scale(1.15); /* More scale up when active */
}

/* Rover Icon */
.rover-icon {
    position: absolute;
    width: 30px;
    height: 30px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!-- Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial Copyright) Copyright 2023 Fonticons, Inc. --><path fill="%234caf50" d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zm0-384c13.3 0 24 10.7 24 24V264c0 13.3-10.7 24-24 24s-24-10.7-24-24V152c0-13.3 10.7-24 24-24zm32 224c0-13.3-10.7-24-24-24s-24 10.7-24 24v72c0 13.3 10.7 24 24 24s24-10.7 24-24V352z"/></svg>'); /* Simple green dot/icon */
    background-size: contain;
    background-repeat: no-repeat;
    transform: translate(-50%, -50%);
    z-index: 2;
    transition: top 1s ease-in-out, left 1s ease-in-out; /* Smooth movement */
}


/* --- Planning Area --- */
.planning-area {
     background-color: #e3f2fd; /* Light blue for planning area */
     border: 1px solid #90caf9; /* Light blue border */
}

.budget-display {
    border: 1px dashed #1e88e5; /* Blue dashed border */
    padding: 12px;
    border-radius: 6px;
    background-color: #bbdefb; /* Lighter blue background */
    margin-bottom: 15px;
}

.budget-display h3 {
    margin-top: 0;
    font-size: 1.1em;
    color: #1565c0; /* Darker blue for budget titles */
}

.budget-display p {
    margin: 5px 0;
    font-size: 1em;
    color: #0d47a1; /* Dark blue text */
}

.budget-display span {
    font-weight: bold;
    color: #333; /* Default color */
}

/* Highlight planned costs */
.planned-costs span {
     color: #333; /* Default color */
}

.planned-costs #planned-time[style*="red"],
.planned-costs #planned-energy[style*="red"],
.planned-costs #planned-storage[style*="red"] {
    color: #e53935 !important; /* Red for exceeding budget */
    font-weight: bold;
}

/* Sequence Drop Target */
.sequence-drop-target {
    border: 2px dashed #42a5f5; /* Blue dashed border */
    padding: 20px; /* More padding */
    min-height: 180px; /* Increased min height */
    border-radius: 8px;
    background-color: #e1f5fe; /* Very light blue */
    text-align: center; /* Center the drag message */
    transition: background-color 0.3s ease;
}

.sequence-drop-target.drag-over {
    background-color: #b3e5fc; /* Highlight when dragging over */
    border-color: #039be5;
}

.sequence-drop-target h3 {
    margin-top: 0;
    font-size: 1.1em;
    color: #0277bd; /* Blue title */
    text-align: right; /* Align title right */
}

#sequence-list {
    list-style: none;
    padding: 0;
    margin: 15px 0 0 0; /* Space after title */
    display: flex;
    flex-direction: column;
    gap: 10px; /* Space between list items */
}

#sequence-list li {
    background-color: #ffffff; /* White background for steps */
    border: 1px solid #e0e0e0; /* Light grey border */
    padding: 12px 15px; /* Increased padding */
    border-radius: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08); /* Subtle shadow */
    transition: background-color 0.2s ease;
}

#sequence-list li:hover {
    background-color: #f5f5f5; /* Light grey on hover */
}


#sequence-list li span {
    font-weight: bold;
    color: #3f51b5; /* Indigo color for step label */
    flex-grow: 1; /* Allow label to take space */
}

#sequence-list li select {
    padding: 6px 8px;
    border-radius: 4px;
    border: 1px solid #ccc;
    background-color: #fff;
    font-size: 0.9em;
    cursor: pointer;
}

#sequence-list li select:focus {
    outline: none;
    border-color: #42a5f5; /* Highlight on focus */
    box-shadow: 0 0 0 2px rgba(66, 165, 245, 0.2);
}


#sequence-list li .remove-step {
    background-color: #ef5350; /* Red color */
    color: white;
    border: none;
    border-radius: 4px;
    padding: 6px 12px;
    cursor: pointer;
    font-size: 0.9em;
    transition: background-color 0.2s ease;
}

#sequence-list li .remove-step:hover {
    background-color: #e53935; /* Darker red on hover */
}


/* --- Simulation Button --- */
#run-simulation {
    display: block;
    width: 100%;
    padding: 12px; /* Increased padding */
    background-color: #4caf50; /* Green color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.2em; /* Larger font */
    margin-top: 20px; /* More space above */
    transition: background-color 0.2s ease, transform 0.1s ease;
    font-weight: bold;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

#run-simulation:hover {
    background-color: #43a047; /* Darker green on hover */
}

#run-simulation:active {
    transform: scale(0.98); /* Slightly shrink on click */
}


/* --- Simulation Output --- */
.log-output {
    margin-top: 20px;
    padding: 15px;
    border: 1px solid #b0bec5; /* Light grey border */
    border-radius: 6px;
    min-height: 80px; /* Increased min height */
    background-color: #eceff1; /* Very light grey */
    white-space: pre-wrap; /* Preserve line breaks */
    font-family: 'Courier New', Courier, monospace; /* Monospaced font for log */
    font-size: 0.9em;
    color: #263238; /* Dark grey text */
    overflow-y: auto; /* Add scroll if content is too long */
    max-height: 200px; /* Optional: limit max height */
}

.log-output h3 {
    margin-top: 0;
    color: #37474f; /* Dark grey title */
}

.log-output p {
    margin: 5px 0;
    padding-right: 10px; /* Indent log lines */
    border-right: 2px solid #b0bec5; /* Visual separator for log lines */
}

.log-output p strong {
    color: #1a237e; /* Highlight summary */
}

.log-output p[style*="green"] {
    color: #388e3c !important; /* Green for success messages */
    font-weight: bold;
}

.log-output p[style*="orange"] {
    color: #f57c00 !important; /* Orange for warning/incomplete */
     font-weight: bold;
}

.log-output p[style*="red"] {
    color: #d32f2f !important; /* Red for errors */
     font-weight: bold;
}


/* --- Explanation Section --- */
#toggle-explanation {
    display: block;
    margin: 30px auto; /* Center button and provide space */
    padding: 12px 20px;
    background-color: #78909c; /* Blue grey */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.2s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

#toggle-explanation:hover {
    background-color: #607d8b; /* Darker blue grey */
}

#explanation {
    margin-top: 20px;
    padding: 25px;
    border: 1px solid #cfd8dc; /* Light grey border */
    border-radius: 8px;
    background-color: #f5f5f5; /* Light grey background */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

#explanation h2, #explanation h3 {
    color: #37474f; /* Dark grey headings */
    border-bottom: 1px solid #b0bec5; /* Light grey separator */
    padding-bottom: 8px;
    margin-top: 20px;
    margin-bottom: 10px;
}

#explanation ul {
    list-style-type: disc;
    margin-right: 20px; /* RTL list bullet alignment */
    padding-right: 0; /* Reset default padding */
}
#explanation ol {
     list-style-type: decimal;
     margin-right: 20px; /* RTL list number alignment */
     padding-right: 0; /* Reset default padding */
}


#explanation li {
    margin-bottom: 8px;
    color: #455a64; /* Darker grey text */
}

/* --- Responsive Adjustments --- */
@media (max-width: 768px) {
    .app-container {
        flex-direction: column;
        padding: 15px;
        gap: 20px;
    }

    .map-area, .planning-area {
        min-width: unset; /* Allow smaller width */
    }

     #asteroid-map {
        height: 300px; /* Smaller map on small screens */
     }

     .poi-marker {
        width: 80px; /* Smaller markers */
        font-size: 0.8em;
     }

     .poi-icon {
        width: 20px;
        height: 20px;
     }

    #sequence-list li {
        flex-direction: column; /* Stack items vertically in list */
        align-items: flex-end; /* Align items to the right */
    }

    #sequence-list li span {
        width: 100%; /* Full width for label */
        margin-bottom: 5px;
         text-align: right;
    }
     #sequence-list li select,
     #sequence-list li .remove-step {
         width: auto; /* Auto width for select/button */
     }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const budget = {
        time: 100,
        energy: 150,
        storage: 5
    };

    const currentCosts = {
        time: 0,
        energy: 0,
        storage: 0,
        value: 0
    };

    // Enhanced POI data with descriptive names and costs
    const poisData = [
        { id: 1, name: 'שדה מגנטי חזק', value: 30, location: { top: '10%', left: '15%' }, compatibleTools: ['scoop', 'arm'], costs: { scoop: { time: 5, energy: 10, storage: 1 }, arm: { time: 7, energy: 12, storage: 1 } }, description: 'דגימת סלע מגנטי בעל ערך מדעי גבוה.' },
        { id: 2, name: 'אזור רגולית עדין', value: 10, location: { top: '30%', left: '60%' }, compatibleTools: ['scoop'], costs: { scoop: { time: 3, energy: 5, storage: 1 } }, description: 'איסוף דגימת אבק דק ורגולית.' },
        { id: 3, name: 'סלע פחמני עשיר', value: 40, location: { top: '55%', left: '30%' }, compatibleTools: ['drill', 'arm'], costs: { drill: { time: 10, energy: 25, storage: 2 }, arm: { time: 15, energy: 20, storage: 2 } }, description: 'קידוח ואיסוף דגימת ליבה מסלע פחמני עתיק.' },
        { id: 4, name: 'שפת מכתש אימפקט', value: 20, location: { top: '70%', left: '80%' }, compatibleTools: ['scoop', 'arm'], costs: { scoop: { time: 6, energy: 8, storage: 1 }, arm: { time: 8, energy: 10, storage: 1 } }, description: 'דגימה משפת מכתש אימפקט לחקר האירוע.' },
        { id: 5, name: 'צבר חלקיקים רופפים', value: 25, location: { top: '85%', left: '45%' }, compatibleTools: ['arm'], costs: { arm: { time: 5, energy: 10, storage: 1 } }, description: 'איסוף עדין של צבר חלקיקים נדירים.' }
    ];

     // Enhanced Tool data with names and base costs (movement added separately)
    const toolsData = {
        scoop: { name: 'כף איסוף' },
        drill: { name: 'מקדח' },
        arm: { name: 'זרוע אוספת' },
        move: { name: 'תנועה', cost: { time: 2, energy: 3, storage: 0 } } // Base movement cost per step
    };

    let missionSequence = []; // Array of { poiId: number, tool: string }

    // --- DOM Elements ---
    const asteroidMap = document.getElementById('asteroid-map');
    const sequenceList = document.getElementById('sequence-list');
    const budgetTimeSpan = document.getElementById('budget-time');
    const budgetEnergySpan = document.getElementById('budget-energy');
    const budgetStorageSpan = document.getElementById('budget-storage');
    const plannedTimeSpan = document.getElementById('planned-time');
    const plannedEnergySpan = document.getElementById('planned-energy');
    const plannedStorageSpan = document.getElementById('planned-storage');
    const plannedValueSpan = document.getElementById('planned-value');
    const runSimulationButton = document.getElementById('run-simulation');
    const simulationOutputDiv = document.getElementById('simulation-output');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const missionSequenceDiv = document.getElementById('mission-sequence'); // Get the drop target div
    const roverIcon = document.getElementById('rover'); // Get the rover icon

    // --- Initialize App ---
    function initializeApp() {
        // Map initialization is now static HTML, but we might want to add listeners
        const poiElements = asteroidMap.querySelectorAll('.poi-marker');
        poiElements.forEach(poiEl => {
             poiEl.draggable = true;
             poiEl.addEventListener('dragstart', drag);
             // Add hover description (optional, maybe too complex for strict constraints)
             // Add click listener? (maybe to show more info or add to sequence directly?) - Stick to drag/drop for now.
        });

        // Set initial budget display
        budgetTimeSpan.textContent = budget.time;
        budgetEnergySpan.textContent = budget.energy;
        budgetStorageSpan.textContent = budget.storage;

        // Setup drop target
        missionSequenceDiv.addEventListener('drop', drop);
        missionSequenceDiv.addEventListener('dragover', allowDrop);
        missionSequenceDiv.addEventListener('dragenter', addDragOverClass);
        missionSequenceDiv.addEventListener('dragleave', removeDragOverClass);
        missionSequenceDiv.addEventListener('drop', removeDragOverClass); // Also remove class on drop

        // Add event listener for the run simulation button
        runSimulationButton.addEventListener('click', runSimulation);

         // Explanation toggle
         toggleExplanationButton.addEventListener('click', toggleExplanation);

         // Initial cost update
         updateCosts();
    }


    // --- Drag and Drop Handlers ---
    function allowDrop(event) {
        event.preventDefault(); // Necessary to allow dropping
         event.dataTransfer.dropEffect = 'copy'; // Show a "copy" icon
    }

     function addDragOverClass() {
         missionSequenceDiv.classList.add('drag-over');
     }

     function removeDragOverClass() {
         missionSequenceDiv.classList.remove('drag-over');
     }

    function drag(event) {
        event.dataTransfer.setData("text", event.target.dataset.poiId);
         // Add visual feedback for the dragged item (optional, via CSS :active or JS class)
    }

    function drop(event) {
        event.preventDefault();
        const poiId = parseInt(event.dataTransfer.getData("text"));
        addStepToSequence(poiId);
    }

    // --- Sequence Management ---
    function addStepToSequence(poiId) {
        const poi = poisData.find(p => p.id === poiId);
        if (!poi) return;

        // Add move cost from previous point (or base if first) + tool cost
        const newStep = { poiId: poi.id, tool: poi.compatibleTools[0] }; // Default to first compatible tool
        missionSequence.push(newStep);
        renderSequence();
        updateCosts();
        updateRoverPosition(); // Update rover position visually
    }

     function removeStepFromSequence(index) {
        missionSequence.splice(index, 1);
        renderSequence();
        updateCosts();
        updateRoverPosition(); // Update rover position visually
    }

    function changeStepTool(index, tool) {
        if (missionSequence[index]) {
            missionSequence[index].tool = tool;
            renderSequence(); // Re-render to update tool name display
            updateCosts();
        }
    }

    function renderSequence() {
        sequenceList.innerHTML = ''; // Clear existing elements
        if (missionSequence.length === 0) {
             const placeholder = document.createElement('li');
             placeholder.textContent = 'גרור נקודות עניין מהמפה לכאן לתכנון המסלול';
             placeholder.style.textAlign = 'center';
             placeholder.style.color = '#666';
             placeholder.style.fontStyle = 'italic';
             placeholder.style.backgroundColor = 'transparent';
             placeholder.style.border = 'none';
             placeholder.style.boxShadow = 'none';
             sequenceList.appendChild(placeholder);
        } else {
            missionSequence.forEach((step, index) => {
                const poi = poisData.find(p => p.id === step.poiId);
                if (!poi) return;

                const listItem = document.createElement('li');
                listItem.dataset.index = index;

                const stepLabel = document.createElement('span');
                // Add step number and POI name
                stepLabel.textContent = `שלב ${index + 1}: בקר ב "${poi.name}"`;
                listItem.appendChild(stepLabel);

                const toolSelect = document.createElement('select');
                 toolSelect.setAttribute('aria-label', `בחר כלי לנקודת עניין ${poi.name}`); // Accessibility
                poi.compatibleTools.forEach(toolKey => {
                    const option = document.createElement('option');
                    option.value = toolKey;
                    option.textContent = toolsData[toolKey].name;
                    if (step.tool === toolKey) {
                        option.selected = true;
                    }
                    toolSelect.appendChild(option);
                });
                toolSelect.addEventListener('change', (e) => changeStepTool(index, e.target.value));
                listItem.appendChild(toolSelect);

                 const removeButton = document.createElement('button');
                removeButton.classList.add('remove-step');
                removeButton.textContent = 'הסר שלב';
                removeButton.setAttribute('aria-label', `הסר שלב ${index + 1}`); // Accessibility
                removeButton.addEventListener('click', () => removeStepFromSequence(index));
                listItem.appendChild(removeButton);


                sequenceList.appendChild(listItem);
            });
        }

    }

     // --- Rover Visual Update ---
    function updateRoverPosition() {
        if (missionSequence.length > 0) {
            const lastStep = missionSequence[missionSequence.length - 1];
            const poi = poisData.find(p => p.id === lastStep.poiId);
            if (poi) {
                roverIcon.style.display = 'block';
                roverIcon.style.top = poi.location.top;
                roverIcon.style.left = poi.location.left;
            }
        } else {
            roverIcon.style.display = 'none'; // Hide rover if sequence is empty
            // Or set it to a base location if desired
            // roverIcon.style.top = '50%'; roverIcon.style.left = '50%';
        }
    }


    // --- Cost Calculation ---
    function updateCosts() {
        let totalTime = 0;
        let totalEnergy = 0;
        let totalStorage = 0;
        let totalValue = 0;

        const moveCost = toolsData.move.cost;

        missionSequence.forEach((step, index) => {
            const poi = poisData.find(p => p.id === step.poiId);
            if (!poi) return; // Should not happen with valid sequence data

            // Add movement cost if it's not the first step
            if (index > 0) {
                 totalTime += moveCost.time;
                 totalEnergy += moveCost.energy;
                 // Storage does not change during movement
            }

            // Add tool usage cost specific to the POI
            const toolCost = poi.costs[step.tool];
            if (toolCost) { // Ensure the selected tool is valid for this POI
                totalTime += toolCost.time;
                totalEnergy += toolCost.energy;
                totalStorage += toolCost.storage;
                totalValue += poi.value;
            } else {
                 // This case indicates an invalid tool was somehow selected/persisted
                 console.error(`Invalid tool "${step.tool}" for POI ID ${step.poiId}`);
            }
        });

        currentCosts.time = totalTime;
        currentCosts.energy = totalEnergy;
        currentCosts.storage = totalStorage;
        currentCosts.value = totalValue;

        plannedTimeSpan.textContent = currentCosts.time;
        plannedEnergySpan.textContent = currentCosts.energy;
        plannedStorageSpan.textContent = currentCosts.storage;
        plannedValueSpan.textContent = currentCosts.value;

        // Visual feedback if budget exceeded
        plannedTimeSpan.style.color = currentCosts.time > budget.time ? 'red' : '#0d47a1'; // Use theme color if ok
        plannedEnergySpan.style.color = currentCosts.energy > budget.energy ? 'red' : '#0d47a1';
        plannedStorageSpan.style.color = currentCosts.storage > budget.storage ? 'red' : '#0d47a1';
    }

    // --- Simulation ---
    function runSimulation() {
        simulationOutputDiv.innerHTML = '<h3>יומן סימולציה:</h3>';
        if (missionSequence.length === 0) {
            simulationOutputDiv.innerHTML += '<p style="color: orange;">אין פעולות מתוכננות. גרור נקודות עניין למפת המשימה כדי להתחיל בתכנון.</p>';
            return;
        }

        let simTime = 0;
        let simEnergy = 0;
        let simStorage = 0;
        let simValue = 0;
        let simulationSuccessful = true;

        const moveCost = toolsData.move.cost;

        missionSequence.forEach((step, index) => {
             if (!simulationSuccessful) return; // Stop if a previous step failed

             const poi = poisData.find(p => p.id === step.poiId);
             const toolData = toolsData[step.tool];
            if (!poi || !poi.costs[step.tool] || !toolData) {
                 simulationOutputDiv.innerHTML += `<p style="color: red;">שלב ${index + 1}: שגיאה קריטית בתכנון - פעולה לא חוקית או כלי לא מתאים. המשימה בוטלה.</p>`;
                 simulationSuccessful = false;
                 return;
            }

            const toolOperationCost = poi.costs[step.tool];

            let stepMoveTime = 0;
            let stepMoveEnergy = 0;
            if (index > 0) {
                stepMoveTime = moveCost.time;
                stepMoveEnergy = moveCost.energy;
                 simulationOutputDiv.innerHTML += `<p>שלב ${index + 1} - מסע: הרובר נע לעבר "${poi.name}"...</p>`;
            } else {
                 simulationOutputDiv.innerHTML += `<p>שלב ${index + 1} - התחלה: הרובר מתמקם בנקודה הראשונה "${poi.name}".</p>`;
            }


            // Check budget for movement + current tool operation *before* performing the step
             const timeAfterMove = simTime + stepMoveTime;
             const energyAfterMove = simEnergy + stepMoveEnergy;
             const timeAfterTool = timeAfterMove + toolOperationCost.time;
             const energyAfterTool = energyAfterMove + toolOperationCost.energy;
             const storageAfterTool = simStorage + toolOperationCost.storage;


             if (timeAfterMove > budget.time || energyAfterMove > budget.energy) {
                 simulationOutputDiv.innerHTML += `<p style="color: orange;">שלב ${index + 1}: לא ניתן להגיע לנקודה "${poi.name}" עקב מגבלות מסע (זמן ${timeAfterMove}/${budget.time}, אנרגיה ${energyAfterMove}/${budget.energy}). המשימה הסתיימה בטרם עת.</p>`;
                 simulationSuccessful = false;
                 return; // Stop simulation here
             }

            // Simulate movement cost (if not first step)
            simTime = timeAfterMove;
            simEnergy = energyAfterMove;


            // Now check budget for tool operation *after* reaching the point
             if (timeAfterTool > budget.time || energyAfterTool > budget.energy || storageAfterTool > budget.storage) {
                 simulationOutputDiv.innerHTML += `<p style="color: orange;">שלב ${index + 1}: הגיע לנקודה "${poi.name}", אך לא ניתן להשלים את פעולת "${toolData.name}" עקב מגבלות משאבים (זמן ${timeAfterTool}/${budget.time}, אנרגיה ${energyAfterTool}/${budget.energy}, אחסון ${storageAfterTool}/${budget.storage}). המשימה הסתיימה בנקודה זו.</p>`;
                 simulationSuccessful = false;
                 return; // Stop simulation here
            }

            // Simulate tool usage cost
            simTime = timeAfterTool;
            simEnergy = energyAfterTool;
            simStorage = storageAfterTool;
            simValue += toolOperationCost.value; // Value is only gained on successful operation


             simulationOutputDiv.innerHTML += `<p>שלב ${index + 1} - פעולה: מפעיל "${toolData.name}" בנקודה "${poi.name}". (+ זמן ${toolOperationCost.time}, + אנרגיה ${toolOperationCost.energy}, + אחסון ${toolOperationCost.storage}, + ערך ${poi.value}).</p>`;
             simulationOutputDiv.innerHTML += `<p>   - מצב נוכחי: זמן ${simTime}, אנרגיה ${simEnergy}, אחסון ${simStorage}, ערך ${simValue}.</p>`;

        });

        if (simulationSuccessful) {
             simulationOutputDiv.innerHTML += `<p style="color: green;">** סימולציה הסתיימה בהצלחה! הרובוט השלים את כל השלבים המתוכננים. **</p>`;
        } else {
             simulationOutputDiv.innerHTML += `<p style="color: orange;">** סימולציה הופסקה בטרם עת עקב חריגה ממשאבים זמינים. **</p>`;
        }
        simulationOutputDiv.innerHTML += `<p><strong>תוצאה סופית של הסימולציה:</strong></p>`;
        simulationOutputDiv.innerHTML += `<p>זמן כולל שנצרך: ${simTime} (מגבלה: ${budget.time})</p>`;
        simulationOutputDiv.innerHTML += `<p>אנרגיה כוללת שנצרכה: ${simEnergy} (מגבלה: ${budget.energy})</p>`;
        simulationOutputDiv.innerHTML += `<p>נפח אחסון שנוצל: ${simStorage} (מגבלה: ${budget.storage})</p>`;
        simulationOutputDiv.innerHTML += `<p>ערך מדעי כולל שנצבר: ${simValue}</p>`;

    }

    // --- Explanation Toggle ---
    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'מעוניינים לדעת עוד? לחצו להסבר מלא';
    }

    // --- Initial Call ---
    initializeApp();
     renderSequence(); // Render the initial empty sequence list

});
</script>