---
title: "גן עדן בוטני: מסע אל לב הטבע"
english_slug: your-paradise-in-your-hands-managing-a-global-botanical-garden
category: "מדעי החיים / ביולוגיה"
tags:
  - גן בוטני
  - שימור צמחים
  - מגוון ביולוגי
  - ניהול משאבים
  - אקולוגיה
  - סימולציה
---
# גן עדן בוטני: מסע אל לב הטבע

האם אתה מוכן לקחת על עצמך את האתגר של יצירת גן בוטני ברמה עולמית? מקום שבו יפרחו הצמחים הנדירים והמרהיבים ביותר, עדות למגוון החיים המופלא על פני כדור הארץ. עליך לנווט במיומנות בין ניהול משאבים מוגבלים, מסעות מחקר מסוכנים ודרישותיהם הייחודיות של צמחים מכל קצוות תבל. גורלם של מינים רבים נמצא בידיים שלך.

<div id="simulation-area">
    <h2 class="simulation-title">הגן הבוטני שלי</h2>

    <div class="dashboard">
        <div class="resource-item">
            כסף: <span id="money" class="resource-value">1000</span> ₪
        </div>
        <div class="resource-item">
            מים: <span id="water" class="resource-value">500</span> יחידות
        </div>
        <div class="resource-item">
            רמת מחקר: <span id="research-level" class="resource-value">1</span>
        </div>
        <div class="resource-item">
             יום בגן: <span id="current-day" class="resource-value">1</span>
        </div>
        <!-- <div class="resource-item">
             שם הגן: גן הבוטני העולמי
        </div> -->
    </div>

    <div class="garden-status">
        <h3 class="section-title">הצמחים שלי:</h3>
        <ul id="plant-list" class="plant-list">
            <!-- Initial plant, styled dynamically -->
            <li data-plant-index="0">
                <span class="plant-name">עץ נפוץ</span>
                <span class="plant-details">(מים/יום: 5, קרקע: רגילה, טמפ': ממוזגת)</span>
                <span class="plant-health">בריאות: <span class="health-value">100</span>%</span>
            </li>
        </ul>
        <p id="garden-message" class="garden-message"></p>
    </div>

    <div class="actions">
        <h3 class="section-title">פעולות ניהול הגן:</h3>

        <div class="action-section">
             <h4>שגר משלחת איסוף:</h4>
             <div class="action-buttons">
                <button class="action-button expedition-button" data-area="מדבר" data-cost="150" data-duration="3000">מדבר (150 ₪)</button>
                <button class="action-button expedition-button" data-area="יער גשם" data-cost="200" data-duration="4000">יער גשם (200 ₪)</button>
                <button class="action-button expedition-button" data-area="טונדרה" data-cost="180" data-duration="3500">טונדרה (180 ₪)</button>
                <button class="action-button expedition-button" data-area="יער ממוזג" data-cost="120" data-duration="2500">יער ממוזג (120 ₪)</button>
             </div>
             <div id="expedition-progress" class="progress-bar-container" style="display: none;">
                 <div class="progress-bar-label">משלחת בדרך ל... <span id="expedition-area-label"></span></div>
                 <div class="progress-bar">
                    <div id="expedition-progress-bar" class="progress"></div>
                 </div>
             </div>
        </div>

        <div class="action-section">
            <h4>טיפול ותחזוקה:</h4>
             <div class="action-buttons">
                <button class="action-button" id="water-plants-button">השקה את כל הצמחים (צורך משתנה)</button>
                <!-- Add more plant care options later if complexity allows -->
             </div>
        </div>

         <div class="action-section">
             <h4>פיתוח והשקעה:</h4>
              <div class="action-buttons">
                <button class="action-button" id="research-button" data-cost="300">שדרג מחקר (300 ₪)</button>
                 <button class="action-button" id="next-day-button">יום חדש בגן</button>
              </div>
         </div>


    </div>

    <div class="logs">
        <h3 class="section-title">יומן הגנן:</h3>
        <ul id="log-list" class="log-list">
            <li><span class="log-time">יום 1:</span> ברוך הבא לגן הבוטני! התחל לשגר משלחות לאסוף צמחים נדירים.</li>
        </ul>
    </div>
</div>

<style>
    :root {
        --primary-green: #28a745; /* Bootstrap success green */
        --secondary-green: #218838; /* Darker green for hover */
        --light-green: #e9ffe9; /* Light background for plants */
        --dark-green-text: #006400; /* Darker green for titles */
        --highlight-yellow: #ffc107; /* Warning color */
        --error-red: #dc3545; /* Error color */
        --info-blue: #007bff; /* Info color */
        --background-light: #f8f9fa; /* Bootstrap light background */
        --border-color: #dee2e6; /* Bootstrap border color */
        --card-background: #ffffff; /* White background for sections */
        --log-background: #e9ecef; /* Light grey for logs */
        --border-radius: 8px;
        --padding-medium: 15px;
        --margin-medium: 20px;
    }

    #simulation-area {
        font-family: 'Arial Hebrew', 'Arial', sans-serif;
        border: 1px solid var(--border-color);
        padding: var(--margin-medium);
        margin-bottom: var(--margin-medium);
        background-color: var(--background-light);
        border-radius: var(--border-radius);
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        gap: var(--margin-medium);
    }

    .simulation-title {
        color: var(--dark-green-text);
        text-align: center;
        margin-bottom: 0; /* Space handled by gap */
        font-size: 2em;
        font-weight: bold;
    }

    .dashboard {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: var(--padding-medium);
        background-color: var(--card-background);
        padding: var(--padding-medium);
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
    }

    .resource-item {
        background-color: var(--light-green);
        padding: var(--padding-medium) / 2;
        border-radius: 4px;
        text-align: center;
        font-size: 1.1em;
        font-weight: bold;
        color: var(--dark-green-text);
    }

    .resource-value {
        color: var(--primary-green);
        font-size: 1.2em;
         transition: color 0.3s ease; /* Smooth color change */
    }

     .resource-value.changed {
         animation: pulse-change 0.5s ease-in-out;
     }

     @keyframes pulse-change {
         0% { transform: scale(1); color: inherit; }
         50% { transform: scale(1.1); color: var(--info-blue); }
         100% { transform: scale(1); color: inherit; }
     }


    .section-title {
        color: var(--dark-green-text);
        text-align: right;
        margin-top: 0;
        margin-bottom: var(--padding-medium);
        font-size: 1.5em;
        border-bottom: 2px solid var(--primary-green);
        padding-bottom: 5px;
    }

    .garden-status, .actions, .logs {
        background-color: var(--card-background);
        padding: var(--padding-medium);
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
    }

    .plant-list {
        list-style: none;
        padding: 0;
        margin-top: 10px;
    }

    .plant-list li {
        background-color: var(--light-green);
        padding: 10px var--padding-medium);
        margin-bottom: 8px;
        border-radius: 4px;
        border-right: 5px solid var(--primary-green); /* Accent */
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

     .plant-name {
         font-weight: bold;
         color: var(--dark-green-text);
     }

     .plant-details {
         font-size: 0.9em;
         color: #555;
         margin-right: 10px; /* Space between name and details */
     }

     .plant-health {
         font-weight: bold;
     }

     .plant-health .health-value {
         color: var(--primary-green); /* Default healthy color */
         transition: color 0.5s ease;
     }

    /* Health status colors */
    .plant-list li.health-warning .health-value { color: var(--highlight-yellow); }
    .plant-list li.health-critical .health-value { color: var(--error-red); }
    .plant-list li.health-dead {
        opacity: 0.6;
        text-decoration: line-through;
        border-color: var(--error-red);
    }


    .garden-message {
        text-align: center;
        font-size: 1.1em;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space */
        color: var(--info-blue); /* Default color */
    }
    .garden-message.warning { color: var(--highlight-yellow); }
    .garden-message.error { color: var(--error-red); }
    .garden-message.success { color: var(--primary-green); }


    .actions h4 {
        color: var(--dark-green-text);
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.2em;
    }

    .action-section {
        margin-bottom: var(--padding-medium);
        padding-bottom: var(--padding-medium);
        border-bottom: 1px dashed var(--border-color);
    }
    .action-section:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
    }

    .action-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 10px; /* Space between buttons */
    }

    .action-button {
        padding: 10px 15px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        background-color: var(--primary-green);
        color: white;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        flex-grow: 1; /* Allows buttons to grow and fill space */
        min-width: 120px; /* Minimum width before wrapping */
        text-align: center;
    }

    .action-button:hover:not(:disabled) {
        background-color: var(--secondary-green);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .action-button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        opacity: 0.7;
        box-shadow: none;
    }

    .progress-bar-container {
        width: 100%;
        margin-top: 10px;
        background-color: #e0e0e0;
        border-radius: 5px;
        overflow: hidden;
    }

    .progress-bar-label {
        text-align: center;
        font-size: 0.9em;
        color: #333;
        padding: 5px 0;
        position: relative;
        z-index: 1; /* Keep label above the bar */
    }

    .progress-bar {
        height: 25px;
        background-color: var(--border-color);
        border-radius: 5px;
        position: relative; /* For containing the progress */
        margin-top: -25px; /* Overlap label */
    }

    .progress {
        height: 100%;
        width: 0%;
        background-color: var(--info-blue);
        border-radius: 5px;
        transition: width 0.1s linear; /* Smooth progress animation */
    }


    .log-list {
        list-style: none;
        padding: 0;
        max-height: 150px; /* Increased height */
        overflow-y: auto;
        background-color: var(--log-background);
        padding: var(--padding-medium) / 2;
        border-radius: 4px;
    }

    .log-list li {
        margin-bottom: 8px;
        padding: 8px;
        background-color: var(--card-background);
        border-radius: 3px;
        font-size: 0.9em;
        border-right: 3px solid var(--border-color);
         display: flex;
         flex-direction: column;
    }

    .log-list li:last-child {
         margin-bottom: 0;
    }

    .log-time {
        font-weight: bold;
        color: #555;
        margin-bottom: 3px;
        font-size: 0.8em;
    }


    #toggle-explanation {
        display: block;
        width: 250px; /* Slightly wider */
        margin: var(--margin-medium) auto;
        padding: 12px 20px;
        background-color: var(--info-blue);
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        cursor: pointer;
        text-align: center;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: #0056b3; /* Darker blue */
        transform: translateY(-1px); /* Slight lift */
    }

     #toggle-explanation:active {
         transform: translateY(0);
     }


    #explanation-area {
        border: 1px solid var(--border-color);
        padding: var(--margin-medium);
        margin-top: var(--margin-medium);
        background-color: var(--background-light);
        border-radius: var(--border-radius);
        display: none; /* Hidden by default */
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        line-height: 1.6;
    }

    #explanation-area h2 {
        color: var(--dark-green-text);
        margin-top: 0;
        margin-bottom: var(--padding-medium);
        font-size: 1.8em;
        border-bottom: 2px solid var(--primary-green);
        padding-bottom: 5px;
    }

    #explanation-area p, #explanation-area ul {
        margin-bottom: var(--padding-medium);
    }

    #explanation-area ul {
        padding-right: 20px; /* For list bullets */
    }

    #explanation-area strong {
        color: var(--dark-green-text);
    }

    /* Scrollbar basic styling */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: var(--log-background);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: var(--primary-green);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--secondary-green);
    }

</style>

<button id="toggle-explanation">הצג/הסתר את סודות הגן הבוטני</button>

<div id="explanation-area">
    <h2>הסבר: מהו גן בוטני וכיצד הוא פועל?</h2>

    <p><strong>מסע אל לב הטבע: מהו גן בוטני ומה תפקידיו בעולם המודרני?</strong> גן בוטני הוא הרבה יותר מאוסף יפה של צמחים. בעוד שתצוגה לקהל ומתן חוויה אסתטית הם חלק חשוב, גנים בוטניים מודרניים הם חזית הפעולה בשימור עולמי, מחקר מתקדם וחינוך סביבתי. הם משמשים כארכיונים חיים המאגדים, מתעדים ומציגים מגוון עצום של צמחים מכל קצוות תבל, עם דגש מיוחד על מינים נדירים, בסכנת הכחדה או בעלי חשיבות מכרעת לאדם ולסביבה.</p>
    <p>תפקידיהם הרבים והחיוניים כוללים: קידום מחקר בוטני ואקולוגי חלוצי, שמירה אקטיבית על המגוון הביולוגי העולמי (גם באמצעות גידול אוספים חיים וגם בתמיכה בפרויקטי שימור בטבע עצמו - In Situ), העברת ידע וחינוך לקהל הרחב בכל הגילאים, אחסון בנקי זרעים חיוניים למקרה חירום עולמי, ויצירת רשת בינלאומית לשיתוף מידע, דגימות וצמחים עם גנים ומוסדות מחקר אחרים.</p>

    <p><strong>דופק כדור הארץ: חשיבות המגוון הביולוגי וצל ההכחדה:</strong> המגוון הביולוגי, אותה רשת סבוכה של כל המינים החיים והמערכות האקולוגיות המקיימות אותם, הוא עמוד התווך של החיים על פני כדור הארץ, כולל קיומנו אנו. צמחים, כמפיקי בסיס במרבית המערכות האקולוגיות היבשתיות, מספקים לנו את מרבית המזון, החמצן שאנו נושמים, חומרי גלם חיוניים לתעשייה ולרפואה, שירותי מערכת אקולוגית כמו סינון מים וייצוב קרקע, ועוד אינספור תועלות שאנו לעיתים קרובות לוקחים כמובן מאליו. למרבה הצער, אנו עדים כיום לקצב הכחדה חסר תקדים של מינים, תופעה המכונה על ידי מדענים "ההכחדה השישית", הנגרמת בעיקר מלחצים אנושיים הולכים וגוברים - הרס מסיבי של בתי גידול טבעיים, שינויי אקלים דרמטיים, זיהום סביבתי נרחב והתפשטות מינים פולשים אגרסיביים. אובדן מגוון ביולוגי זה מערער את יציבותן וחוסנן של המערכות האקולוגיות ומגביל את יכולתן לספק לנו את השירותים החיוניים שעליהם אנו כה תלויים.</p>

    <p><strong>תיבת נוח המודרנית: כיצד גנים בוטניים מסייעים בשימור Ex Situ (מחוץ לבית הגידול הטבעי):</strong> שימור Ex Situ הוא אסטרטגיה קריטית הכוללת שמירה על מיני צמחים מחוץ למקום גידולם הטבעי. גנים בוטניים הם השחקנים המרכזיים בזירה זו. הם מארגנים משלחות איסוף מיוחדות לאיזורים מרוחקים ובתי גידול מגוונים על מנת לאסוף זרעים, ייחורים או צמחים בוגרים של מינים הנמצאים בסכנת הכחדה מיידית או עתידית. אוספים יקרים אלה מטופחים במסירות בשטח הגן או נשמרים בתנאים מבוקרים בבנקי זרעים לאומיים ובינלאומיים. אוספים אלה משמשים כ"פוליסת ביטוח" חיונית למקרה טרגי שהמין ייכחד לחלוטין בטבע, ומהווים מאגר גנטי חיוני שממנו ניתן לשאוב גרעיני רבייה לצורך ניסיונות השבה עתידיים לטבע, במידה ותנאי הסביבה ישתפרו ויאפשרו זאת.</p>

    <p><strong>מסע ההישרדות: אתגרי איסוף וגידול צמחים נדירים:</strong> איסוף צמחים נדירים מסביבתם הטבעית הוא מבצע מורכב, יקר ומסוכן לעיתים קרובות, הדורש ידע בוטני מעמיק, משאבים לוגיסטיים ניכרים ולעיתים גם היתרים חוקיים מחמירים. כל צמח, במיוחד אלה המותאמים לבתי גידול קיצוניים או ספציפיים, פיתח דרישות סביבתיות ייחודיות לו (הרכב קרקע מדויק, כמות ועוצמת אור ספציפית, רמות לחות, טמפרטורות מדויקות, ולעיתים אף קשרים סימביוטיים עם מיקרואורגניזמים בקרקע). גידול צמחים אלה בסביבה מלאכותית כמו גן בוטני דורש שחזור מדויק ככל הניתן של תנאים אלה, לרוב תוך שימוש בחממות היי-טק עם בקרת אקלים ממוחשבת, הכנת מצעי גידול מיוחדים ויישום משטרי השקיה ודישון פרטניים. זהו אתגר טכני, מדעי וכלכלי עצום הדורש השקעה מתמדת.</p>

    <p><strong>מאחורי הקלעים: ניהול משאבים ואתגרים כלכליים בגן בוטני:</strong> הפעלת גן בוטני ברמה עולמית דורשת תקציב תפעולי משמעותי וניהול פיננסי קפדני. ההוצאות כוללות: תחזוקה שוטפת ופיתוח של שטחי הגן, המבנים והתשתיות המורכבות, העסקת צוות מקצועי רחב הכולל בוטנאים, גננים מומחים, אנשי חינוך ומדע, אנשי אדמיניסטרציה וניהול, אבטחה ועוד. עלויות איסוף הצמחים (משלחות מחקר ושכר צוות), עלויות הגידול והטיפוח השוטף (מים, אנרגיה לחממות, דשנים, הדברה ביולוגית), עלויות מחקר, פעילויות חינוך והסברה, ושיווק וגיוס כספים. ההכנסות מגיעות בדרך כלל ממגוון מקורות: מכירת כרטיסי כניסה, תוכניות חברות ותמיכה, תרומות מפרטים וארגונים, מענקי מחקר תחרותיים וסובסידיות ממשלתיות או עירוניות. איזון עדין בין צרכים מדעיים ושימוריים דחופים לבין מגבלות תקציביות הוא אתגר ניהולי יום-יומי.</p>

    <p><strong>קרן אור של תקווה: סיפורי הצלחה של שימור צמחים דרך גנים בוטניים:</strong> למרות האתגרים, גנים בוטניים ברחבי העולם חתומים על סיפורי הצלחה רבים ומרשימים בהצלת מיני צמחים רבים מגורל של הכחדה. דוגמאות בולטות כוללות: שימור וריבוי מיני צמחים מקומיים נדירים ואף השבתם לטבע באזורים שמהם נעלמו (כמו שימור מינים בסכנת הכחדה בישראל), שימור מינים שנחשבו אבודים ונמצאו מחדש (כמו עץ הפלפל הסיני - Metasequoia glyptostroboides, שהתגלה בטבע לאחר שנחשב נכחד והיה קיים רק באוספים של גנים בוטניים), ותפקיד מרכזי בשמירת המגוון הגנטי של גידולי חקלאות חיוניים וקרוביהם הפראיים בבנקי זרעים עולמיים. שיתוף פעולה הדוק בין גנים בוטניים, מוסדות מחקר, ארגוני שימור וקהילות מקומיות הוא המפתח להשגת הצלחות בקנה מידה עולמי במאמץ לשמור על העושר הבוטני של הפלנטה שלנו.</p>
</div>

<script>
    // --- DOM Elements ---
    const moneySpan = document.getElementById('money');
    const waterSpan = document.getElementById('water');
    const researchLevelSpan = document.getElementById('research-level');
    const currentDaySpan = document.getElementById('current-day');
    const plantListUl = document.getElementById('plant-list');
    const logListUl = document.getElementById('log-list');
    const expeditionButtons = document.querySelectorAll('.expedition-button');
    const waterPlantsButton = document.getElementById('water-plants-button');
    const researchButton = document.getElementById('research-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationArea = document.getElementById('explanation-area');
    const gardenMessage = document.getElementById('garden-message');
    const nextDayButton = document.getElementById('next-day-button'); // New button
    const expeditionProgressBarContainer = document.getElementById('expedition-progress');
    const expeditionProgressBar = document.getElementById('expedition-progress-bar');
    const expeditionAreaLabel = document.getElementById('expedition-area-label');


    // --- Game State ---
    let gameState = {
        money: 1000,
        water: 500,
        researchLevel: 1,
        currentDay: 1,
        plants: [
            { id: 1, name: "עץ נפוץ", waterNeededPerDay: 5, soil: "רגילה", temp: "ממוזגת", health: 100, area: "הגן ההתחלתי", lastWateredDay: 1 }
        ],
        expeditionsRunning: 0,
        researchCost: 300,
        baseExpeditionSuccessChance: 0.6, // Chance to find a plant on expedition
        basePlantSurvivalChance: 0.8, // Chance for collected plant to survive
        passiveWaterLossPerDay: 50, // Water lost daily due to evaporation etc.
        moneyPerDayPerPlant: 2, // Income from visitors (simplified)
         maxLogItems: 10,
         researchMaxLevel: 3
    };

    const plantsData = {
        "מדבר": { name: "קקטוס נדיר", waterNeededPerDay: 2, soil: "חולית", temp: "חמה", researchRequired: 1, survivalChance: 0.9 },
        "יער גשם": { name: "סחלב טרופי", waterNeededPerDay: 10, soil: "לחה/עשירה", temp: "חמה/לחה", researchRequired: 2, survivalChance: 0.7 },
        "טונדרה": { name: "אזוב קפוא", waterNeededPerDay: 3, soil: "קפואה", temp: "קרה", researchRequired: 2, survivalChance: 0.85 },
        "יער ממוזג": { name: "פרח ממוזג", waterNeededPerDay: 6, soil: "רגילה", temp: "ממוזגת", researchRequired: 1, survivalChance: 0.95 }
    };

    // --- Helper Functions ---

     function animateResourceChange(element, newValue, oldValue) {
        element.textContent = newValue;
        if (newValue !== oldValue) {
            element.classList.remove('changed'); // Reset animation
            void element.offsetWidth; // Trigger reflow
            element.classList.add('changed');
        }
    }

    function updateDisplay() {
        animateResourceChange(moneySpan, gameState.money, parseInt(moneySpan.textContent));
        animateResourceChange(waterSpan, gameState.water, parseInt(waterSpan.textContent));
        animateResourceChange(researchLevelSpan, gameState.researchLevel, parseInt(researchLevelSpan.textContent));
        currentDaySpan.textContent = gameState.currentDay;


        plantListUl.innerHTML = '';
        if (gameState.plants.length === 0) {
            plantListUl.innerHTML = '<li>אין עדיין צמחים בגן. שגר משלחת לאסוף!</li>';
        } else {
            gameState.plants.forEach((plant, index) => {
                const li = document.createElement('li');
                li.dataset.plantIndex = index; // Store index for potential future interaction

                const healthSpan = document.createElement('span');
                healthSpan.classList.add('plant-health');
                healthSpan.innerHTML = `בריאות: <span class="health-value">${plant.health}</span>%`;

                li.innerHTML = `
                    <span class="plant-name">${plant.name}</span>
                    <span class="plant-details">(מים/יום: ${plant.waterNeededPerDay}, קרקע: ${plant.soil}, טמפ': ${plant.temp})</span>
                `;
                 li.appendChild(healthSpan); // Append health span last

                // Add health status classes for styling
                if (plant.health < 50 && plant.health > 0) {
                    li.classList.add('health-warning');
                     healthSpan.querySelector('.health-value').style.color = 'var(--highlight-yellow)';
                }
                if (plant.health <= 20 && plant.health > 0) {
                    li.classList.remove('health-warning'); // Remove warning if critical
                    li.classList.add('health-critical');
                    healthSpan.querySelector('.health-value').style.color = 'var(--error-red)';
                }
                 if (plant.health <= 0) {
                     li.classList.add('health-dead');
                     healthSpan.querySelector('.health-value').textContent = 'מת';
                     healthSpan.querySelector('.health-value').style.color = 'var(--error-red)';
                 }

                plantListUl.appendChild(li);
            });
        }

        researchButton.textContent = `שדרג מחקר (${gameState.researchCost} ₪)`;
        researchButton.disabled = gameState.money < gameState.researchCost || gameState.researchLevel >= gameState.researchMaxLevel || gameState.expeditionsRunning > 0;
         if (gameState.researchLevel >= gameState.researchMaxLevel) {
             researchButton.textContent = 'מחקר ברמה מקסימלית';
         }


        expeditionButtons.forEach(button => {
            const area = button.dataset.area;
            const cost = parseInt(button.dataset.cost);
            const requiredLevel = plantsData[area] ? plantsData[area].researchRequired : 1;
            const isAffordable = gameState.money >= cost;
            const researchMet = gameState.researchLevel >= requiredLevel;

            button.disabled = !isAffordable || !researchMet || gameState.expeditionsRunning > 0;

            let buttonText = `${area} (${cost} ₪)`;
            if (!researchMet) {
                buttonText += ` (דרוש רמה ${requiredLevel})`;
            }
            button.textContent = buttonText;
        });

        waterPlantsButton.disabled = gameState.plants.length === 0 || gameState.expeditionsRunning > 0;
        nextDayButton.disabled = gameState.expeditionsRunning > 0;

        // Update garden message based on state
        const plantsLowHealth = gameState.plants.filter(p => p.health > 0 && p.health < 50);
        const plantsDead = gameState.plants.filter(p => p.health <= 0);

        if (plantsDead.length > 0) {
             gardenMessage.textContent = `${plantsDead.length} צמח(ים) מתו בגן... יש לטפל בצמחים היטב!`;
             gardenMessage.className = 'garden-message error'; // Reset and add error class
        } else if (plantsLowHealth.length > 0) {
             gardenMessage.textContent = `${plantsLowHealth.length} צמח(ים) סובל(ים)! יש לדאוג להם למים.`;
             gardenMessage.className = 'garden-message warning'; // Reset and add warning class
        } else if (gameState.plants.length === 0) {
             gardenMessage.textContent = "הגן ריק. שגר משלחת כדי להתחיל את האוסף שלך!";
             gardenMessage.className = 'garden-message info'; // Reset and add info class
        }
        else if (gameState.plants.length > 0 && gameState.plants.every(p => p.health >= 80)) { // "Flourishing" threshold increased
            gardenMessage.textContent = "כל הצמחים בגן פורחים ושגשגים!";
            gardenMessage.className = 'garden-message success'; // Reset and add success class
        }
         else {
             gardenMessage.textContent = ""; // Clear message if status is neutral
             gardenMessage.className = 'garden-message'; // Reset class
         }


    }

    function addLog(message) {
        const li = document.createElement('li');
         const timeSpan = document.createElement('span');
         timeSpan.classList.add('log-time');
         timeSpan.textContent = `יום ${gameState.currentDay}: `;
         li.appendChild(timeSpan);
         li.appendChild(document.createTextNode(message)); // Add message text node

        logListUl.prepend(li); // Add to the top
        // Keep log list clean (e.g., max 10 items)
        while (logListUl.children.length > gameState.maxLogItems) {
            logListUl.removeChild(logListUl.lastChild);
        }
    }

    function sendExpedition(area, cost, duration) {
        const requiredLevel = plantsData[area] ? plantsData[area].researchRequired : 1;
         if (gameState.money < cost || gameState.researchLevel < requiredLevel || gameState.expeditionsRunning > 0) {
             // Buttons should be disabled, so this check is mostly a safeguard
             return;
         }


        gameState.money -= cost;
        gameState.expeditionsRunning++;
        addLog(`שוגרה משלחת איסוף ל${area}.`);
        updateDisplay();

        // Show and animate progress bar
        expeditionProgressBarContainer.style.display = 'block';
        expeditionAreaLabel.textContent = area;
        expeditionProgressBar.style.width = '0%';
        let startTime = Date.now();

        function updateProgress() {
            const elapsed = Date.now() - startTime;
            const progressPercent = Math.min(100, (elapsed / duration) * 100);
            expeditionProgressBar.style.width = progressPercent + '%';

            if (progressPercent < 100) {
                requestAnimationFrame(updateProgress);
            }
        }
        requestAnimationFrame(updateProgress);


        // Simulate expedition time and result
        setTimeout(() => {
            gameState.expeditionsRunning--;
            expeditionProgressBarContainer.style.display = 'none';


            const foundPlantChance = gameState.baseExpeditionSuccessChance + (gameState.researchLevel - 1) * 0.1; // Research improves chance
            if (Math.random() < foundPlantChance) {
                const plantInfo = plantsData[area];
                 // Research improves survival chance too, but also base chance might be higher for some biomes
                 const baseSurvival = plantInfo.survivalChance || gameState.basePlantSurvivalChance; // Use plant-specific if available, else base
                 const survivalChance = baseSurvival * (1 + (gameState.researchLevel - 1) * 0.1); // Research gives +10% survival per level above 1
                 if (Math.random() < survivalChance) {
                    const newPlant = {
                        id: Date.now() + Math.random(), // Simple unique ID
                        name: plantInfo.name,
                        waterNeededPerDay: plantInfo.waterNeededPerDay,
                        soil: plantInfo.soil,
                        temp: plantInfo.temp,
                        health: 100,
                        area: area,
                        lastWateredDay: gameState.currentDay
                    };
                    gameState.plants.push(newPlant);
                    addLog(`המשלחת חזרה מ${area} ומצאה בהצלחה צמח חדש: ${plantInfo.name}! הוא שולב באוסף הגן.`);
                } else {
                     addLog(`המשלחת חזרה מ${area} עם ממצא מעניין, אך הצמח לא שרד את ההעברה לגן.`);
                }
            } else {
                addLog(`המשלחת ל${area} חזרה ללא ממצאים משמעותיים הפעם.`);
            }
            updateDisplay(); // Re-enable buttons here as expedition is finished
        }, duration); // Use dynamic duration
    }

    function waterPlants() {
        if (gameState.plants.length === 0) {
            gardenMessage.textContent = "אין צמחים להשקות.";
            gardenMessage.className = 'garden-message info';
            return;
        }

        let totalWaterNeeded = 0;
        // Calculate water needed for plants that haven't been watered *today*
         const plantsToWater = gameState.plants.filter(plant => plant.lastWateredDay < gameState.currentDay);

         if (plantsToWater.length === 0) {
             gardenMessage.textContent = "כל הצמחים הושקו היום!";
             gardenMessage.className = 'garden-message info';
             return;
         }

        plantsToWater.forEach(plant => {
            const daysWithoutWater = gameState.currentDay - plant.lastWateredDay;
            totalWaterNeeded += plant.waterNeededPerDay * daysWithoutWater; // Need water for days missed
        });
        totalWaterNeeded = Math.round(totalWaterNeeded); // Round to integer

        if (gameState.water < totalWaterNeeded) {
            addLog(`אין מספיק מים להשקות את הצמחים (צורך מוערך: ${totalWaterNeeded}, זמין: ${gameState.water}).`);
            gardenMessage.textContent = "אין מספיק מים להשקות את כל הצמחים הזקוקים!";
            gardenMessage.className = 'garden-message error';
            // Optional: Partially water if possible, or reduce health for ALL plants needing water
            // For simplicity now, just reduce health if watering failed entirely
             plantsToWater.forEach(plant => {
                const healthLoss = Math.round((gameState.currentDay - plant.lastWateredDay) * 10); // Lose health based on days without water
                plant.health = Math.max(0, plant.health - healthLoss);
                addLog(`${plant.name} איבד בריאות עקב מחסור במים.`);
             });

        } else {
            gameState.water -= totalWaterNeeded;
            plantsToWater.forEach(plant => {
                // Health gain depends on how long it went without water
                 const daysWithoutWater = gameState.currentDay - plant.lastWateredDay;
                 const healthGain = Math.min(100 - plant.health, Math.round(daysWithoutWater * 15 + 10)); // Gain based on days missed, max 100
                plant.health = Math.min(100, plant.health + healthGain);
                 plant.lastWateredDay = gameState.currentDay; // Mark as watered today
            });
            addLog(`השקית את הצמחים הזקוקים. נוצלו ${totalWaterNeeded} יחידות מים.`);
             gardenMessage.textContent = "הצמחים הזקוקים הושקו בהצלחה ושבו לחיים.";
             gardenMessage.className = 'garden-message success';
        }

        // Remove dead plants AFTER potential health gain/loss calculation
        const deadPlants = gameState.plants.filter(plant => plant.health <= 0);
        deadPlants.forEach(plant => {
             addLog(`${plant.name} מת עקב הזנחה או תנאים לא מתאימים.`);
        });
        gameState.plants = gameState.plants.filter(plant => plant.health > 0);

        updateDisplay();
    }

    function performResearch() {
        if (gameState.money < gameState.researchCost) {
            addLog("אין מספיק כסף למימון המחקר.");
            return;
        }
        if (gameState.researchLevel >= gameState.researchMaxLevel) {
             addLog("המחקר הגיע לרמה המקסימלית (רמה " + gameState.researchMaxLevel + ").");
             return;
         }

        gameState.money -= gameState.researchCost;
        gameState.researchLevel++;
        gameState.researchCost = Math.round(gameState.researchCost * 1.7); // Research gets significantly more expensive
        addLog(`שדרגת את רמת המחקר בגן לרמה ${gameState.researchLevel}. זה פותח אפשרויות חדשות!`);
        updateDisplay();
    }

     function nextDay() {
         // Apply daily passive effects
         gameState.currentDay++;
         addLog(`התחיל יום חדש בגן הבוטני (יום ${gameState.currentDay}).`);

         // Passive water loss
         gameState.water = Math.max(0, gameState.water - gameState.passiveWaterLossPerDay);
         addLog(`עקב אידוי ותחזוקה שוטפת, הגן איבד ${gameState.passiveWaterLossPerDay} יחידות מים.`);

         // Passive income from visitors/operations per plant
         const dailyIncome = gameState.plants.length * gameState.moneyPerDayPerPlant;
         if (dailyIncome > 0) {
             gameState.money += dailyIncome;
             addLog(`הגן הרוויח ${dailyIncome} ₪ מפעילות שוטפת (מבקרים, תרומות קטנות).`);
         }


         // Plants passively lose health if not watered (handled in waterPlants now, but could add here)
         // For this model, waterPlants action covers daily needs.
         // A plant not watered for DAYS will accrue health loss when nextDay passes,
         // and this loss is calculated when waterPlants is attempted.

         // Remove dead plants (check again after potential health loss if implemented here)
         // const deadPlants = gameState.plants.filter(plant => plant.health <= 0);
         // deadPlants.forEach(plant => { addLog(`${plant.name} מת עקב הזנחה.`); });
         // gameState.plants = gameState.plants.filter(plant => plant.health > 0);


         updateDisplay(); // Update everything for the new day
     }


    function setupEventListeners() {
        expeditionButtons.forEach(button => {
            button.addEventListener('click', () => {
                const area = button.dataset.area;
                const cost = parseInt(button.dataset.cost);
                 const duration = parseInt(button.dataset.duration);
                sendExpedition(area, cost, duration);
            });
        });

        waterPlantsButton.addEventListener('click', () => {
            waterPlants();
        });

        researchButton.addEventListener('click', () => {
            performResearch();
        });

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationArea.style.display === 'none' || explanationArea.style.display === '';
            explanationArea.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר את סודות הגן הבוטני' : 'הצג את סודות הגן הבוטני';
        });

         nextDayButton.addEventListener('click', () => {
             nextDay();
         });
    }

    // --- Initial Setup ---
    updateDisplay();
    setupEventListeners();

     // Ensure the initial plant is marked as watered on Day 1
     if (gameState.plants.length > 0) {
         gameState.plants[0].lastWateredDay = gameState.currentDay;
         updateDisplay(); // Update to reflect the initial plant's state based on day 1
     }

</script>