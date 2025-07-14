---
title: "לנהל ארכיון סרטים: משחק המשאבים המוגבלים"
english_slug: managing-film-archive-limited-resources-game
category: "מדעי החברה / כלכלה התנהגותית"
tags: [ניהול משאבים, כלכלה, הקצאת משאבים, ארכיון, קבלת החלטות, סימולציה]
---
# לנהל ארכיון סרטים: האתגר הגדול של משאבים מוגבלים

דמיינו עולם קסום של סרטים נדירים, קלאסיקות נשכחות ויצירות מופת על סלילים מתפוררים. אתם מנהלים ארכיון יוקרתי, האוצר של היסטוריית הקולנוע. הרצון שלכם הוא לשמר כל יצירה בעלת ערך, אבל המציאות קשוחה: המקום מוגבל עד כאב והעלויות מרקיעות שחקים. איך תנווטו את הארכיון בתקופה של אילוצים? איך תחליטו מה ראוי להישמר לדורות הבאים ומה חייב להישאר רק בזיכרון?

צאו למסע בזמן ובמשאבים, וגלו את האתגרים העומדים בפני מנהלי ארכיונים - וכל מי שצריך לקבל החלטות תחת אילוצים.

<div id="game-container" class="game-area">
    <div id="state-panel" class="panel state-panel">
        <h2>מצב הארכיון</h2>
        <div class="state-info">
            <p>תור: <span id="current-turn" class="state-value">0</span>/<span id="total-turns" class="state-value">10</span></p>
            <p>מקום פנוי: <span id="current-space" class="state-value highlight-space"></span> יחידות</p>
            <p>תקציב שנתי: <span id="current-budget" class="state-value highlight-budget"></span> יחידות</p>
            <p>שווי ארכיון: <span id="archive-value" class="state-value highlight-value"></span> נקודות</p>
        </div>
    </div>

    <div id="new-items-panel" class="panel new-items-panel">
        <h2>פריטים חדשים לתור זה</h2>
        <div id="item-list" class="item-list">
            <!-- Items will be loaded here -->
        </div>
        <button id="next-turn-button" class="game-button next-turn-button" disabled>התקדם לתור הבא</button>
    </div>

    <div id="messages" class="game-message hidden" aria-live="polite">
        <!-- Game messages will appear here -->
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג/הסתר הסבר: ניהול משאבים ועלות אלטרנטיבית</button>

<div id="explanation" class="explanation hidden">
    <h2>הסבר: ניהול משאבים מוגבלים ועלות אלטרנטיבית</h2>
    <p>ברוכים הבאים לסימולציה של ניהול ארכיון סרטים. כמו מנהל/ת ארכיון בפועל, עליכם להתמודד עם מציאות יסודית בעולם הכלכלה והניהול: **משאבים מוגבלים** אל מול רצונות או צרכים אינסופיים (במקרה הזה, הרצון לשמר כל יצירת קולנוע אפשרית).</p>

    <h3>האתגר הבסיסי: משאבים מוגבלים לעומת רצון אינסופי</h3>
    <p>בכלכלה, משאבים הם כל מה שמשמש לייצור סחורות ושירותים או לסיפוק צרכים, והם תמיד מוגבלים ביחס לצרכים. בארכיון, המשאבים המרכזיים הם שטח אחסון ותקציב כספי. הרצון האינסופי הוא לשמר כל פריט בעל ערך, אך המציאות מכריחה אותנו לבחור – מה נשמור, מה נשקם, ועל מה נאלץ לוותר.</p>

    <h3>מהם משאבים בארכיון?</h3>
    <p>המונח "משאבים" רחב יותר מכסף בלבד. בארכיון סרטים, המשאבים הקריטיים כוללים:</p>
    <ul>
        <li>**כסף (תקציב):** נדרש לתחזוקה שוטפת, שיקום פיזי, דיגיטציה, רכישת פריטים חדשים ועוד.</li>
        <li>**מקום (שטח אחסון):** שטח פיזי יקר ומוגבל לשמירת סלילים, קופסאות וחומרים פיזיים.</li>
        <li>**זמן וכוח אדם:** צוות הארכיון זקוק לזמן ומומחיות יקרים כדי לטפל בפריטים, לקטלג, לשקם ולבצע דיגיטציה. למרות שפחות מיוצג ישירות במשחק, זהו משאב חיוני במציאות.</li>
    </ul>

    <h3>הקצאת משאבים: איך מחליטים על מה לוותר ומה לתעדף?</h3>
    <p>האתגר המרכזי של מנהל/ת משאבים הוא להקצות את המשאבים המוגבלים בצורה שתמקסם את התועלת או המטרה. בארכיון, המטרה היא בדרך כלל למקסם את שווי האוסף ההיסטורי והתרבותי. ההחלטה אילו פריטים לשמור, אילו לשקם ואילו לגנוז תלויה בשילוב מורכב של גורמים:</p>
    <ul>
        <li>**גודל הפריט:** כמה שטח הוא דורש?</li>
        <li>**מצבו הפיזי:** עד כמה הוא דחוף לטיפול וכמה תקציב שיקום/דיגיטציה יידרש?</li>
        <li>**עלויות התחזוקה השוטפת:** כמה כסף ומקום יידרשו לשמירתו לאורך זמן?</li>
        <li>**הערך הפוטנציאלי:** מה החשיבות ההיסטורית, התרבותית או האמנותית שלו?</li>
    </ul>
    <p>כל החלטה שאתם מקבלים היא למעשה בחירה. אם בחרתם לשמור סרט גדול הדורש שיקום, השתמשתם בחלק משמעותי מהשטח הפנוי ומהתקציב. משאבים אלו אינם זמינים יותר עבור פריטים אחרים או פעולות אחרות. כאן נכנס לתמונה מושג הליבה של עלות אלטרנטיבית.</p>

    <h3>עלות אלטרנטיבית: מה מפסידים כשאנחנו בוחרים באפשרות אחת?</h3>
    <p>זהו אחד המושגים העוצמתיים והחשובים ביותר בכלכלה. העלות האלטרנטיבית (Opportunity Cost) של כל פעולה היא לא רק העלות הישירה שלה, אלא **התועלת מהאפשרות הטובה ביותר שוויתרנו עליה** כדי לבצע את הפעולה שבחרנו. במשחק:</p>
    <ul>
        <li>**שמירת סרט אחד:** העלות האלטרנטיבית היא השטח והתקציב השוטף שהוקצו לו, שהיו יכולים לשמש לשמירת סרט אחר בעל ערך דומה או גבוה יותר, או למימון שיקום של פריט אחר.</li>
        <li>**שיקום סרט:** הכסף שהוצא על השיקום לא יכול לשמש לדיגיטציה של פריט אחר, לרכישת פריט חדש, או לתחזוקה שוטפת של פריטים קיימים.</li>
        <li>**גניזת סרט:** העלות האלטרנטיבית היא אובדן הערך הפוטנציאלי של הפריט בעתיד. אולי ויתרתם על יצירת מופת שתהיה שווה הון תרבותי בעוד 50 שנה?</li>
    </ul>
    <p>קבלת החלטות יעילה דורשת מכם להפנים שעליכם כל הזמן להשוות את התועלת של הבחירה שלכם מול התועלת שהתבטלה מכל האפשרויות האחרות שדחיתם.</p>

    <h3>קבלת החלטות תחת אילוצים: דוגמאות מחיי היומיום והכלכלה הגדולה</h3>
    <p>המצב שאתם מתמודדים איתו בארכיון אינו ייחודי. הוא נפוץ בכל תחומי החיים:</p>
    <ul>
        <li>**תקציב ממשלתי:** ממשלה צריכה להחליט איך להקצות תקציב מוגבל בין בריאות, חינוך, ביטחון, תשתיות וכו'. השקעה גדולה בתחום אחד באה בהכרח על חשבון האחרים.</li>
        <li>**עסק:** חברה צריכה להחליט כיצד להשקיע את ההון שלה: במחקר ופיתוח, בשיווק, בהרחבת ייצור, או אולי לשלם דיבידנדים לבעלים?</li>
        <li>**משק בית:** משפחה צריכה להחליט איך להוציא הכנסה מוגבלת: על שכירות, מזון, חינוך לילדים, בילויים, חיסכון לעתיד?</li>
        <li>**זמן אישי:** לכל אדם יש רק 24 שעות ביממה. בחירה להקדיש זמן לפעילות אחת (עבודה, לימודים, תחביב) באה על חשבון זמן שהיה יכול להיות מוקדש לפעילויות אחרות.</li>
    </ul>
    <p>בכל המקרים הללו, ההתמודדות עם משאבים מוגבלים וההבנה של עלות אלטרנטיבית הן המפתח לקבלת החלטות מיטבית שתמקסם את התועלת ביחס למטרות.</p>

    <h3>עקרונות בארכיונאות ושימור: מאזן עדין</h3>
    <p>באופן ספציפי לארכיונים, החלטות שימור והקצאת משאבים מונחות גם על ידי עקרונות מקצועיים המכתיבים את "הערך" של פריט:</p>
    <ul>
        <li>**ערך היסטורי/תרבותי:** מהי חשיבותו של הפריט לאוסף הקיים, להיסטוריה של הקולנוע, לחברה או לתרבות? פריטים נדירים, בעלי חשיבות אירועית, או כאלו המתעדים היבטים ייחודיים - לרוב יקבלו עדיפות גבוהה.</li>
        <li>**מצב פיזי:** האם הפריט במצב טוב או רע? האם הוא בסכנת אובדן מיידית? פריטים במצב גרוע דורשים טיפול יקר ודחוף יותר, אך האם ההשקעה בהם מוצדקת ביחס לערכם הפוטנציאלי או ביחס לאפשרויות אחרות?</li>
        <li>**רלוונטיות לאוסף:** עד כמה הפריט משתלב במדיניות האיסוף של הארכיון? האם הוא משלים פריטים קיימים או פותח תחום חדש?</li>
    </ul>
    <p>המשחק מדמה את הצורך לאזן בין כל הגורמים הללו תחת מגבלות תקציב ומקום, תוך הבנה עמוקה שכל בחירה כרוכה בעלות אלטרנטיבית כואבת. בהצלחה!</p>
</div>

<style>
    /* General Reset & Base Styles */
    #game-container, .explanation {
        direction: rtl;
        font-family: 'Arial', sans-serif; /* Changed font stack slightly */
        max-width: 850px; /* Increased max-width */
        margin: 20px auto;
        padding: 25px; /* Increased padding */
        border: 1px solid #dcdcdc; /* Lighter border */
        border-radius: 12px; /* More rounded corners */
        background-color: #f8f9fa; /* Light background */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Subtle shadow */
        color: #343a40; /* Dark grey text */
        line-height: 1.6;
    }

    h1, h2 {
        text-align: center;
        color: #0056b3; /* Blue headings */
        margin-bottom: 20px;
    }

    h3 {
        color: #007bff; /* Lighter blue for subheadings */
        margin-top: 20px;
        margin-bottom: 10px;
    }

    p {
        margin-bottom: 10px;
    }

    ul {
        margin-bottom: 15px;
        padding-right: 25px;
    }

    li {
        margin-bottom: 5px;
    }


    /* Panel Styles */
    .panel {
        background-color: #e9ecef; /* Light grey background */
        padding: 15px 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        border: 1px solid #ced4da;
    }

    .state-panel h2 {
        margin-bottom: 15px;
        color: #343a40;
        text-align: right; /* Align state panel title right */
    }

    .state-info {
        display: flex;
        justify-content: space-around; /* Distribute space evenly */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 10px; /* Gap between items */
    }

    .state-panel p {
         margin: 0;
         font-size: 1.1em;
         font-weight: bold;
         color: #495057;
    }

    .state-value {
        font-weight: normal;
        color: #007bff; /* Blue color for values */
        transition: color 0.3s ease, transform 0.3s ease; /* Smooth transition for value changes */
        display: inline-block; /* Needed for transform */
    }

    /* Animation for value changes */
    @keyframes flash-green {
      0%, 100% { color: #28a745; } /* Green */
      50% { color: #495057; } /* Back to normal */
    }

    @keyframes flash-red {
      0%, 100% { color: #dc3545; } /* Red */
      50% { color: #495057; } /* Back to normal */
    }

    .highlight-budget.flash-green, .highlight-value.flash-green {
        animation: flash-green 1s ease-in-out;
    }
     .highlight-budget.flash-red, .highlight-space.flash-red {
        animation: flash-red 1s ease-in-out;
    }


    .new-items-panel h2 {
         text-align: center;
         margin-bottom: 15px;
         color: #343a40;
    }

    .item-list {
        display: flex;
        flex-wrap: wrap;
        gap: 20px; /* Increased gap */
        justify-content: center;
        margin-bottom: 20px;
    }

    .item-card {
        background-color: #fff;
        border: 1px solid #dee2e6; /* Lighter border */
        border-radius: 8px;
        padding: 20px; /* Increased padding */
        width: 240px; /* Slightly wider cards */
        box-shadow: 0 2px 5px rgba(0,0,0,0.08); /* Subtle shadow */
        text-align: right;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        opacity: 0; /* Start hidden for fade-in */
        transform: translateY(20px); /* Start slightly below for slide-up */
        animation: fade-in-slide-up 0.5s ease-out forwards; /* Apply animation */
    }

    @keyframes fade-in-slide-up {
        to { opacity: 1; transform: translateY(0); }
    }

    .item-card h3 {
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.3em; /* Larger title */
        color: #0056b3;
        border-bottom: 1px solid #e9ecef; /* Separator line */
        padding-bottom: 8px;
    }

    .item-card p {
        margin: 6px 0; /* More vertical space */
        font-size: 0.95em;
        color: #495057;
    }

     .item-card p strong {
        color: #007bff;
     }


    .item-card .actions {
        margin-top: 15px;
        display: flex;
        flex-direction: column;
        gap: 8px; /* Increased gap between buttons */
    }

    /* General Button Styles */
    .game-button, .toggle-button, .item-card button {
        padding: 10px 15px; /* More padding */
        border: none;
        border-radius: 5px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1em; /* Standard font size */
        font-weight: bold;
        transition: background-color 0.2s ease, opacity 0.2s ease, transform 0.1s ease;
        text-align: center;
    }

    .game-button:hover, .toggle-button:hover, .item-card button:hover:not(:disabled) {
        opacity: 0.9;
    }

    .game-button:active, .toggle-button:active, .item-card button:active:not(:disabled) {
         transform: scale(0.98); /* Slight press effect */
    }


    .item-card button:disabled {
        opacity: 0.6; /* More visible disabled state */
        cursor: not-allowed;
        background-color: #cccccc !important; /* Ensure greyed out */
        color: #666 !important;
    }

    /* Specific Item Action Button Colors */
    .item-card .save { background-color: #28a745; color: white; } /* Green */
    .item-card .discard { background-color: #dc3545; color: white; } /* Red */
    .item-card .restore { background-color: #ffc107; color: #343a40; } /* Yellow */
    .item-card .digitize { background-color: #007bff; color: white; } /* Blue */

    /* Animation for processed card */
    .item-card.processed {
        animation: fade-out-slide 0.4s ease-in forwards;
    }

    @keyframes fade-out-slide {
        from { opacity: 1; transform: translateX(0); }
        to { opacity: 0; transform: translateX(100px); } /* Slide right on removal */
    }


    /* Next Turn Button */
    #next-turn-button {
        display: block;
        margin: 20px auto 0;
        padding: 12px 25px; /* Larger button */
        font-size: 1.2em;
        background-color: #28a745; /* Green to emphasize progress */
        color: white;
        width: fit-content; /* Adjust width to content */
    }

    #next-turn-button:disabled {
        background-color: #cccccc;
    }

    /* Messages Area */
    #messages {
        margin-top: 20px;
        padding: 15px;
        border-radius: 5px;
        text-align: center;
        opacity: 0; /* Start hidden */
        transition: opacity 0.4s ease-in-out;
    }

    #messages.show {
         opacity: 1;
    }

    #messages:not(.error) { /* Default/Success message style */
        background-color: #d4edda; /* Light green */
        color: #155724; /* Dark green */
        border: 1px solid #c3e6cb;
    }

    #messages.error { /* Error message style */
        background-color: #f8d7da; /* Light red */
        color: #721c24; /* Dark red */
        border: 1px solid #f5c6cb;
    }


    #messages.hidden {
        display: none; /* Still use display: none when completely hidden */
    }

    /* Explanation Toggle Button */
    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 10px 15px;
        background-color: #e9ecef; /* Light grey */
        border: 1px solid #ced4da;
        color: #495057;
        width: fit-content;
    }

    /* Explanation Section */
    .explanation {
        background-color: #e9ecef; /* Match panels */
        border: 1px solid #ced4da;
    }

    .explanation.hidden {
        display: none;
    }

    .explanation h2, .explanation h3 {
        color: #343a40; /* Match panel titles */
        text-align: right;
    }

    .explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Adjust indentation */
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        #game-container, .explanation {
            padding: 15px;
        }

        .state-info {
             flex-direction: column; /* Stack state items vertically */
             align-items: center;
        }

         .state-panel p {
             margin: 5px 0;
         }

        .item-list {
            gap: 15px;
        }

        .item-card {
            width: 90%; /* Allow cards to take more width on small screens */
            max-width: 280px; /* But don't let them get too wide */
            padding: 15px;
        }

        .game-button, .toggle-button, .item-card button {
            font-size: 0.9em;
            padding: 8px 10px;
        }

        #next-turn-button {
             font-size: 1.1em;
             padding: 10px 20px;
        }
    }

</style>

<script>
    const state = {
        space: 1000,
        budget: 5000, // Annual budget
        archiveValue: 0,
        currentTurn: 0,
        totalTurns: 10,
        savedItems: [], // Items kept in the archive (physical or digital)
        newItems: [], // Items for the current turn's consideration (unprocessed)
        itemCounter: 0, // To generate unique IDs
        annualOngoingCost: 0 // Track cumulative ongoing cost of saved physical items
    };

    const config = {
        itemsPerTurn: { min: 3, max: 5 },
        itemSizeRange: { min: 10, max: 100 },
        itemConditionRange: { min: 1, max: 5 }, // 1 = bad, 5 = good
        itemValueRange: { min: 20, max: 100 }, // Increased value range for better score variation
        itemOngoingCostRange: { min: 5, max: 20 }, // Annual physical storage cost
        restoreCostRange: { min: 100, max: 400 }, // Increased restoration cost
        digitizeCostRange: { min: 200, max: 500 }, // Increased digitization cost
        ongoingCostReductionDigitized: 0.9, // e.g., 90% reduction in ongoing cost for digital
        spaceReductionDigitized: 1 // e.g., 100% reduction in space for digital (takes negligible space)
    };

    const elements = {
        currentTurn: document.getElementById('current-turn'),
        totalTurns: document.getElementById('total-turns'),
        currentSpace: document.getElementById('current-space'),
        currentBudget: document.getElementById('current-budget'),
        archiveValue: document.getElementById('archive-value'),
        itemList: document.getElementById('item-list'),
        nextTurnButton: document.getElementById('next-turn-button'),
        messages: document.getElementById('messages'),
        toggleExplanationButton: document.getElementById('toggle-explanation'),
        explanationDiv: document.getElementById('explanation')
    };

    function updateStateDisplay(changedStats = {}) {
        elements.currentTurn.textContent = state.currentTurn;
        elements.totalTurns.textContent = state.totalTurns;
        elements.currentSpace.textContent = state.space.toFixed(0);
        elements.currentBudget.textContent = state.budget.toFixed(0);
        elements.archiveValue.textContent = state.archiveValue.toFixed(0);

        // Add flash animation to changed stats
        for (const [stat, type] of Object.entries(changedStats)) {
            const element = elements[stat];
            if (element) {
                element.classList.remove('flash-green', 'flash-red'); // Reset animation
                // Trigger reflow
                void element.offsetWidth;
                element.classList.add(type === 'increase' ? 'flash-green' : 'flash-red');
            }
        }
    }

    function showMessage(msg, type = 'info') { // type: 'info', 'success', 'error'
        elements.messages.textContent = msg;
        elements.messages.className = 'game-message show'; // Base class + show
        if (type === 'error') elements.messages.classList.add('error');
        // Hide after a delay
        setTimeout(() => {
            elements.messages.classList.remove('show');
            // Use transitionend or a longer timeout before display: none if message has fade-out animation
            setTimeout(() => elements.messages.classList.add('hidden'), 400); // Match CSS transition duration
        }, 5000); // Message stays for 5 seconds
    }

    function hideMessage() {
        elements.messages.classList.remove('show');
        setTimeout(() => elements.messages.classList.add('hidden'), 400); // Match CSS transition duration
    }


    function generateRandomItem() {
        state.itemCounter++;
        const id = state.itemCounter;
        const type = Math.random() > 0.4 ? 'סרט קולנוע' : 'אוסף ארכיוני'; // More likely to be a film
        const size = Math.floor(Math.random() * (config.itemSizeRange.max - config.itemSizeRange.min + 1)) + config.itemSizeRange.min;
        const condition = Math.floor(Math.random() * (config.itemConditionRange.max - config.itemConditionRange.min + 1)) + config.itemConditionRange.min;
        const value = Math.floor(Math.random() * (config.itemValueRange.max - config.itemValueRange.min + 1)) + config.itemValueRange.min;
        // Ongoing cost scales slightly with size
        const ongoingCost = Math.floor(Math.random() * (config.itemOngoingCostRange.max - config.itemOngoingCostRange.min + 1)) + config.itemOngoingCostRange.min + Math.floor(size / 20);
        const restoreCost = Math.floor(Math.random() * (config.restoreCostRange.max - config.restoreCostRange.min + 1)) + config.restoreCostRange.min + (6 - condition) * 50; // More expensive to restore bad condition
         const digitizeCost = Math.floor(Math.random() * (config.digitizeCostRange.max - config.digitizeCostRange.min + 1)) + config.digitizeCostRange.min + item.size * 2; // Digitizing larger items costs more


        return {
            id,
            type,
            size,
            condition,
            value,
            ongoingCost, // Physical ongoing cost
            restoreCost,
            digitizeCost,
            status: 'new' // 'new', 'saved-physical', 'saved-digital', 'discarded', 'pending-action' (transient)
        };
    }

    function renderNewItems() {
        elements.itemList.innerHTML = '';
        if (state.newItems.length === 0) {
             elements.itemList.innerHTML = '<p style="text-align:center; color: #555;">כל הפריטים לתור זה טופלו. לחץ על "התקדם לתור הבא".</p>';
             elements.nextTurnButton.disabled = false;
             return;
        }
        state.newItems.forEach(item => {
            const card = document.createElement('div');
            card.classList.add('item-card');
            card.dataset.itemId = item.id;

            let conditionText = '';
            switch(item.condition) {
                case 1: conditionText = 'גרוע מאוד (בסכנת אובדן!)'; break;
                case 2: conditionText = 'גרוע'; break;
                case 3: conditionText = 'בינוני'; break;
                case 4: conditionText = 'טוב'; break;
                case 5: conditionText = 'מעולה'; break;
            }

            // Disable restore/digitize if condition is already 5 or not enough budget
            const canRestore = item.condition < 5 && state.budget >= item.restoreCost;
            const canDigitize = state.budget >= item.digitizeCost;
            const canSave = state.space >= item.size;


            card.innerHTML = `
                <h3>${item.type} #${item.id}</h3>
                <p><strong>גודל:</strong> ${item.size} יחידות</p>
                <p><strong>מצב פיזי:</strong> ${conditionText}</p>
                <p><strong>ערך פוטנציאלי:</strong> ${item.value} נקודות</p>
                <p><strong>עלות אחסון שוטפת:</strong> ${item.ongoingCost} תקציב שנתי</p>
                 ${item.condition < 5 ? `<p><strong>עלות שיקום חד פעמית:</strong> ${item.restoreCost} תקציב</p>` : ''}
                 <p><strong>עלות דיגיטציה חד פעמית:</strong> ${item.digitizeCost} תקציב</p>
                <div class="actions">
                    <button class="save" data-action="save" ${!canSave ? 'disabled' : ''}>שמור פיזית (${item.size} מקום, +${item.ongoingCost} עלות שוטפת)</button>
                    ${item.condition < 5 ? `<button class="restore" data-action="restore" ${!canRestore ? 'disabled' : ''}>שקם ושמור פיזית (${item.restoreCost} תקציב)</button>` : ''}
                     <button class="digitize" data-action="digitize" ${!canDigitize ? 'disabled' : ''}>העבר לדיגיטל (${item.digitizeCost} תקציב)</button>
                    <button class="discard" data-action="discard">גנוז</button>
                </div>
            `;

             // Add event listeners using event delegation on the list container
             // This is more efficient than adding listeners to each button
             // Handled below main renderNewItems call

            elements.itemList.appendChild(card);
        });

         // Disable next turn button until all items are processed
         elements.nextTurnButton.disabled = true;
    }

     function updateArchiveValue() {
        state.archiveValue = state.savedItems.reduce((total, item) => {
             let effectiveCondition = item.condition;
             if (item.status === 'saved-digital') {
                 effectiveCondition = 5; // Assume digitization implies perfect long-term preservation state for value calculation
             } else if (item.status === 'saved-physical' && item.condition < 1) {
                 // Optional: Value penalty if condition drops too low for physical items
                 effectiveCondition = 0; // Lost value if condition hits rock bottom
             }
             // Value is weighted by condition / 5
             return total + (item.value * (effectiveCondition / 5));
        }, 0);
     }

     function findItemIndex(id, list) {
        return list.findIndex(item => item.id === id);
     }

     function removeItemFromNewItems(itemId) {
        const index = findItemIndex(itemId, state.newItems);
        if (index !== -1) {
            state.newItems.splice(index, 1);
        }
     }

    function handleAction(itemId, actionType) {
        const itemIndex = findItemIndex(itemId, state.newItems);
        if (itemIndex === -1) {
             // Item was likely already processed via another action or is gone
             console.log(`Item ${itemId} not found in newItems or already processed.`);
             return;
        }

        const item = state.newItems[itemIndex];
        let success = false;
        let message = '';
        let changedStats = {}; // Track which stats changed for animation

        // Disable all buttons on the card immediately to prevent double actions
        const cardElement = elements.itemList.querySelector(`.item-card[data-item-id='${itemId}']`);
        if (cardElement) {
             cardElement.querySelectorAll('button').forEach(btn => btn.disabled = true);
             cardElement.classList.add('pending-action'); // Optional class for visual feedback
        }


        switch (actionType) {
            case 'save':
                if (state.space >= item.size) {
                    state.space -= item.size;
                    state.annualOngoingCost += item.ongoingCost;
                    item.status = 'saved-physical';
                    state.savedItems.push(item); // Add the item reference
                    success = true;
                    message = `שמרת פיזית את "${item.type} #${item.id}". נצרכו ${item.size} יחידות מקום ויצירת עלות שוטפת של ${item.ongoingCost} לשנה.`;
                    changedStats.currentSpace = 'red'; // Space decreased
                } else {
                    message = `אין מספיק מקום לשמור פיזית את "${item.type} #${item.id}". נדרש ${item.size} יחידות. נותרו רק ${state.space.toFixed(0)}.`;
                }
                break;

            case 'discard':
                item.status = 'discarded';
                success = true;
                message = `גנזת את "${item.type} #${item.id}". ויתרת על הערך הפוטנציאלי שלו (${item.value}).`;
                break;

            case 'restore': // Assumes restoration is followed by physical saving
                if (item.condition < 5) {
                     if (state.budget >= item.restoreCost) {
                         if (state.space >= item.size) {
                             state.budget -= item.restoreCost;
                             state.space -= item.size;
                              state.annualOngoingCost += item.ongoingCost;
                             item.condition = 5; // Restoration brings to perfect condition
                             item.status = 'saved-physical';
                             state.savedItems.push(item); // Add the item reference
                             success = true;
                             message = `שיקמת ושמרת פיזית את "${item.type} #${item.id}". עלה ${item.restoreCost} תקציב, נצרך ${item.size} מקום, ונוספה עלות שוטפת של ${item.ongoingCost}. הפריט במצב מעולה!`;
                              changedStats.currentBudget = 'red'; // Budget decreased
                              changedStats.currentSpace = 'red'; // Space decreased
                         } else {
                              message = `אין מספיק מקום לשמור את "${item.type} #${item.id}" גם אחרי השיקום. נדרש ${item.size} יחידות.`;
                         }
                     } else {
                         message = `אין מספיק תקציב כדי לשקם את "${item.type} #${item.id}". נדרש ${item.restoreCost}. נותרו רק ${state.budget.toFixed(0)}.`;
                     }
                } else {
                     message = `"${item.type} #${item.id}" כבר במצב מעולה, אין צורך בשיקום. בחר "שמור פיזית" או "העבר לדיגיטל".`;
                }
                break;

            case 'digitize':
                 if (state.budget >= item.digitizeCost) {
                      state.budget -= item.digitizeCost;
                      // Digitized items take negligible space and have reduced ongoing cost
                      item.status = 'saved-digital';
                      item.size = item.size * (1 - config.spaceReductionDigitized); // Reduce space significantly (or to 0)
                       // item.ongoingCost = item.ongoingCost * (1 - config.ongoingCostReductionDigitized); // Reduced ongoing cost (applied later in annual costs if needed)
                      state.savedItems.push(item); // Add the item reference
                      success = true;
                      message = `העברת את "${item.type} #${item.id}" לדיגיטל. עלה ${item.digitizeCost} תקציב. הפריט אינו תופס מקום פיזי ועלויות האחסון השוטפות שלו מופחתות משמעותית (או בוטלו).`;
                      changedStats.currentBudget = 'red'; // Budget decreased
                      // Space might 'increase' effectively, but we don't add back, just don't subtract. Let's not animate space for this action for simplicity.
                 } else {
                     message = `אין מספיק תקציב כדי להעביר את "${item.type} #${item.id}" לדיגיטל. נדרש ${item.digitizeCost}. נותרו רק ${state.budget.toFixed(0)}.`;
                 }
                 break;
        }

        // Only remove from newItems and trigger animation if action was successful
        if (success) {
             removeItemFromNewItems(itemId);
             // Trigger the card removal animation
             if (cardElement) {
                cardElement.classList.remove('pending-action');
                cardElement.classList.add('processed');
                // Use the transitionend event to remove the element and check if the turn is over
                cardElement.addEventListener('animationend', () => {
                     cardElement.remove();
                     // After the element is removed from the DOM, check if all are gone
                     checkIfAllItemsProcessed();
                 }, { once: true }); // Remove the listener after it fires once
             } else {
                // Fallback if card element wasn't found (shouldn't happen with delegation)
                checkIfAllItemsProcessed();
             }
        } else {
            // If action failed, re-enable buttons and remove pending class
            if (cardElement) {
                cardElement.querySelectorAll('button').forEach(btn => {
                    // Re-enable buttons based on current state (budget, space)
                     const btnAction = btn.dataset.action;
                     if (btnAction === 'save') btn.disabled = state.space < item.size;
                     else if (btnAction === 'restore') btn.disabled = item.condition === 5 || state.budget < item.restoreCost;
                     else if (btnAction === 'digitize') btn.disabled = state.budget < item.digitizeCost;
                     else if (btnAction === 'discard') btn.disabled = false; // Discard is always possible
                });
                cardElement.classList.remove('pending-action');
            }
        }

        // Update displays and value calculation regardless of success (budget/space might change even on fail if logic allowed, but here only on success)
        updateStateDisplay(changedStats);
        updateArchiveValue();

        // Show the message
        showMessage(message, success ? 'success' : 'error');

        // Note: checkIfAllItemsProcessed is now called *after* the removal animation completes
    }


    function checkIfAllItemsProcessed() {
        // Re-check if the displayed item list is empty
        if (elements.itemList.children.length === 0 || elements.itemList.querySelector('.item-card') === null) {
             // Also ensure the internal state confirms no new items are pending processing
             if (state.newItems.length === 0) {
                elements.itemList.innerHTML = '<p style="text-align:center; color: #555;">כל הפריטים לתור זה טופלו. לחץ על "התקדם לתור הבא".</p>';
                elements.nextTurnButton.disabled = false;
                hideMessage(); // Hide action messages when turn is ready to end
             }
        }
    }

    function applyOngoingCosts() {
        // Recalculate total ongoing cost based on currently saved physical items
        state.annualOngoingCost = state.savedItems.reduce((total, item) => {
            // Only count ongoing cost for physical items
            return item.status === 'saved-physical' ? total + item.ongoingCost : total;
        }, 0);

        const budgetBefore = state.budget;
        state.budget -= state.annualOngoingCost;
        const budgetAfter = state.budget;

        let changedStats = {};
        if (budgetAfter < budgetBefore) changedStats.currentBudget = 'red';


        updateStateDisplay(changedStats);
        showMessage(`עלות אחסון שוטפת לתור זה עבור ${state.savedItems.filter(item => item.status === 'saved-physical').length} פריטים פיזיים: ${state.annualOngoingCost.toFixed(0)}. נותרו ${state.budget.toFixed(0)} בתקציב.`, 'info');
    }

    function checkGameOver() {
        if (state.budget < 0) {
             // Ensure budget display is updated before showing game over
             updateStateDisplay({ currentBudget: 'red' });
             showMessage(`נגמר לך התקציב בתור ${state.currentTurn}! המשחק הסתיים. שווי הארכיון הסופי שלך הוא ${state.archiveValue.toFixed(0)} נקודות. נסה שוב כדי לראות אם תוכל לנהל את המשאבים טוב יותר!`, 'error');
             elements.nextTurnButton.disabled = true;
             elements.itemList.innerHTML = '<p style="text-align:center; color: #dc3545; font-weight: bold;">המשחק הסתיים עקב חריגה בתקציב.</p>'; // Clear items
             return true;
        }
         // Can add game over on space full if that's a desired mechanic, but budget is the main one here.

        if (state.currentTurn >= state.totalTurns) {
            showMessage(`סוף המשחק! סיימת בהצלחה ${state.totalTurns} תורות. שווי הארכיון הסופי שלך הוא ${state.archiveValue.toFixed(0)} נקודות. כל הכבוד על ניהול המשאבים!`, 'success');
            elements.nextTurnButton.disabled = true;
            elements.itemList.innerHTML = '<p style="text-align:center; color: #28a745; font-weight: bold;">המשחק הסתיים.</p>'; // Clear items
            return true;
        }

        return false;
    }


    function nextTurn() {
        if (checkGameOver()) return;

        state.currentTurn++;
        hideMessage(); // Hide previous general messages

        if (state.currentTurn > 1) { // Don't apply cost on turn 1
             applyOngoingCosts();
             if (checkGameOver()) return; // Check game over again after applying costs
        }

        // Generate new items for the turn
        state.newItems = []; // Clear items from previous turn
        const numberOfNewItems = Math.floor(Math.random() * (config.itemsPerTurn.max - config.itemsPerTurn.min + 1)) + config.itemsPerTurn.min;
        for (let i = 0; i < numberOfNewItems; i++) {
            state.newItems.push(generateRandomItem());
        }

        renderNewItems();
        updateStateDisplay(); // Update turn number and initial state

        // The next turn button is disabled by renderNewItems, enabled by checkIfAllItemsProcessed after items are acted upon
    }

    function startGame() {
        state.space = 1000;
        state.budget = 5000;
        state.archiveValue = 0;
        state.currentTurn = 0;
        state.savedItems = [];
        state.newItems = [];
        state.itemCounter = 0; // Reset ID counter
        state.annualOngoingCost = 0; // Reset annual cost

        elements.messages.classList.add('hidden');
        elements.nextTurnButton.textContent = 'התקדם לתור הבא'; // Reset button text
         // Re-enable button if it was disabled by game over
        elements.nextTurnButton.disabled = false;


        updateStateDisplay();
        nextTurn(); // Start the first turn
    }

     function toggleExplanation() {
        elements.explanationDiv.classList.toggle('hidden');
        const isHidden = elements.explanationDiv.classList.contains('hidden');
        elements.toggleExplanationButton.textContent = isHidden
            ? 'הצג/הסתר הסבר: ניהול משאבים ועלות אלטרנטיבית'
            : 'הסתר הסבר'; // Change button text
     }

    // Event listeners
    elements.nextTurnButton.addEventListener('click', nextTurn);
    elements.toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Use event delegation for item card buttons
    elements.itemList.addEventListener('click', (event) => {
        const target = event.target;
        // Check if the clicked element is a button within an item card
        if (target.tagName === 'BUTTON' && target.closest('.item-card')) {
            const card = target.closest('.item-card');
            const itemId = parseInt(card.dataset.itemId);
            const action = target.dataset.action;
            if (itemId && action && !target.disabled) {
                handleAction(itemId, action);
            }
        }
    });


    // Initial setup
    startGame();

</script>
```