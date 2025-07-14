---
title: "אמן או מנהל? ניהול תיאטרון בובות"
english_slug: puppet-theatre-management-simulate
category: "ניהול ועסקים / ניהול"
tags: [ניהול, תיאטרון, סימולציה, עסקים, קבלת החלטות, תקציב, מוניטין, קהל]
---
<div class="game-intro">
    <h1>אמן או מנהל? ניהול תיאטרון בובות</h1>
    <p class="intro-text">האם תיאטרון בובות הוא רק מקדש לאמנות, או גם עסק לכל דבר? מהם האתגרים הייחודיים בניהול מוסד תרבותי שמשלב חזון יצירתי ותקציב תפעולי? היכנסו לנעליו של מנהל תיאטרון וגלו בעצמכם את האמנות שבלקבל החלטות קשות!</p>
</div>

<div id="app-container">
    <div id="game-state" class="game-panel current-state">
        <h2>מצב התיאטרון</h2>
        <div class="state-item">
            <span class="label">עונה:</span> <span id="current-season" class="value">1</span>
        </div>
        <div class="state-item">
            <span class="label">קופה:</span> <span id="current-budget" class="value budget-value"></span> <span class="currency">ש"ח</span>
             <div id="budget-change" class="change-indicator"></div>
        </div>
        <div class="state-item">
            <span class="label">מוניטין:</span>
            <div class="reputation-bar-container">
                <div id="current-reputation-bar" class="reputation-bar"></div>
                <span id="current-reputation" class="value reputation-value"></span> / 100
            </div>
             <div id="reputation-change" class="change-indicator"></div>
        </div>
         <div class="state-item">
            <span class="label">קהל פוטנציאלי:</span> כ-<span id="current-audience" class="value"></span> איש
        </div>
    </div>

    <div id="game-decisions" class="game-panel decision-making">
        <h2>החלטות לעונה הבאה</h2>
        <p>בחר את האסטרטגיה שלך לעונה הקרובה. כל החלטה משפיעה על התקציב, המוניטין ויכולת למשוך קהל.</p>
        <div class="decision-block">
            <h3><i class="icon-play"></i> בחירת הפקה</h3>
            <label class="decision-option">
                <input type="radio" name="play" value="rerun" checked>
                <span class="option-title">העלאה מחודשת</span>
                <span class="option-details">(עלות: 0 ש"ח, סיכון נמוך, מוניטין יציב)</span>
            </label><br>
            <label class="decision-option">
                <input type="radio" name="play" value="new">
                <span class="option-title">יצירה חדשה</span>
                <span class="option-details">(עלות: 3000 ש"ח, פוטנציאל למוניטין גבוה, סיכון גבוה)</span>
            </label>
        </div>
        <div class="decision-block">
             <h3><i class="icon-marketing"></i> השקעה בשיווק</h3>
            <label class="decision-option">
                <input type="radio" name="marketing" value="low" checked>
                 <span class="option-title">נמוכה</span>
                <span class="option-details">(500 ש"ח, מגיעים רק לקהל קיים)</span>
            </label><br>
            <label class="decision-option">
                <input type="radio" name="marketing" value="medium">
                <span class="option-title">בינונית</span>
                <span class="option-details">(1500 ש"ח, חשיפה מוגבלת, משיכת קהל חדש)</span>
            </label><br>
            <label class="decision-option">
                <input type="radio" name="marketing" value="high">
                <span class="option-title">גבוהה</span>
                 <span class="option-details">(3000 ש"ח, קמפיין רחב, פוטנציאל לגידול קהל ומוניטין)</span>
            </label>
        </div>
        <div class="decision-block">
             <h3><i class="icon-venue"></i> בחירת אולם</h3>
            <label class="decision-option">
                <input type="radio" name="venue" value="small" checked>
                <span class="option-title">קטן</span>
                <span class="option-details">(עלות: 1000 ש"ח, קיבולת: 50 איש)</span>
            </label><br>
            <label class="decision-option">
                <input type="radio" name="venue" value="medium">
                 <span class="option-title">בינוני</span>
                 <span class="option-details">(עלות: 2500 ש"ח, קיבולת: 150 איש)</span>
            </label><br>
            <label class="decision-option">
                <input type="radio" name="venue" value="large">
                <span class="option-title">גדול</span>
                <span class="option-details">(עלות: 5000 ש"ח, קיבולת: 300 איש)</span>
            </label>
        </div>
         <div class="decision-block">
             <h3><i class="icon-price"></i> תמחור כרטיסים</h3>
            <label class="decision-option">
                <input type="radio" name="price" value="low" checked>
                <span class="option-title">נמוך</span>
                <span class="option-details">(20 ש"ח, מושך קהל רחב, הכנסה לכרטיס נמוכה)</span>
            </label><br>
            <label class="decision-option">
                <input type="radio" name="price" value="medium">
                <span class="option-title">בינוני</span>
                <span class="option-details">(30 ש"ח, איזון בין ביקוש להכנסה)</span>
            </label><br>
            <label class="decision-option">
                <input type="radio" name="price" value="high">
                <span class="option-title">גבוה</span>
                <span class="option-details">(40 ש"ח, הכנסה גבוהה לכרטיס, עלול להרתיע חלק מהקהל)</span>
            </label>
        </div>
        <button id="end-season-button" class="game-button primary-button">סיום עונה וחישוב תוצאות</button>
    </div>

    <div id="game-results" class="game-panel season-summary" style="display: none;">
        <h2>סיכום עונה <span id="summary-season"></span></h2>
        <div class="summary-details">
            <p>ההחלטות שלך היו:</p>
            <ul>
                <li><span class="label">הפקה:</span> <span id="summary-play" class="value"></span></li>
                <li><span class="label">שיווק:</span> <span id="summary-marketing" class="value"></span></li>
                <li><span class="label">אולם:</span> <span id="summary-venue" class="value"></span></li>
                <li><span class="label">מחיר כרטיס:</span> <span id="summary-price" class="value"></span> ש"ח</li>
            </ul>
            <p><strong>הוצאות כוללות לעונה:</strong> <span id="summary-expenses" class="value loss"></span> ש"ח</p>
             <p><strong>הכנסות מכרטיסים:</strong> <span id="summary-revenue" class="value profit"></span> ש"ח</p>
            <p class="profit-loss"><strong>רווח / הפסד עונתי:</strong> <span id="summary-profit" class="value"></span> ש"ח</p>
             <p id="attendance-message" class="result-message"></p>
             <p id="event-message" class="result-message"></p>
        </div>
        <div class="updated-state-summary">
            <h3>מצב התיאטרון בתחילת עונה <span id="next-season-number"></span>:</h3>
            <p><span class="label">קופה מעודכנת:</span> <span id="updated-budget" class="value budget-value"></span> ש"ח</p>
            <p><span class="label">מוניטין מעודכן:</span> <span id="updated-reputation" class="value reputation-value"></span> / 100</p>
            <p><span class="label">קהל פוטנציאלי חדש:</span> כ-<span id="updated-audience" class="value"></span> איש</p>
        </div>

        <button id="next-season-button" class="game-button primary-button">התחל עונה <span id="button-next-season-number"></span></button>
    </div>

     <div id="game-over" class="game-panel game-end" style="display: none;">
        <h2 id="game-over-title"></h2>
        <p id="game-over-message"></p>
        <button id="restart-game-button" class="game-button secondary-button">התחל משחק חדש</button>
    </div>
</div>

<button id="explanation-toggle" class="game-button explanation-button">הצגת הסבר תיאורטי</button>

<div id="explanation" class="game-panel theoretical-explanation">
    <h2>היבטים עסקיים בניהול מוסד תרבותי</h2>
    <p>ניהול תיאטרון בובות, כמו כל ארגון אמנותי, דורש הבנה מעמיקה לא רק באמנות עצמה, אלא גם בעקרונות עסקיים בסיסיים. האתגר המרכזי הוא למצוא את האיזון הנכון בין חזון אמנותי לבין כדאיות כלכלית, תוך כדי התמודדות עם משאבים מוגבלים ואי-ודאות מובנית.</p>
    <ul>
        <li><strong>מודלים עסקיים:</strong> ארגוני תרבות אינם פועלים תמיד למטרות רווח מקסימלי, אך הם חייבים להיות בני קיימא כלכלית. המודלים העסקיים שלהם יכולים לכלול שילוב של הכנסות ממכירת כרטיסים, תמיכה ממשלתית או ציבורית, תרומות וגיוס כספים, ופעילויות מסחריות נלוות. המטרה: כיסוי הוצאות והשקעה ביצירה עתידית.</li>
        <li><strong>ניהול משאבים מוגבלים (תקציב וכוח אדם):</strong> תקציבי תרבות לרוב מוגבלים. יש לקבל החלטות קשות היכן להשקיע – האם ביצירת הצגה חדשה ויקרה, או בהעלאה מחודשת? האם להשקיע יותר בשיווק או בתשתיות? ניהול כוח אדם דורש שיקול דעת כלכלי תוך שמירה על איכות ומורל.</li>
        <li><strong>איזון אמנותי-כלכלי:</strong> זוהי הדילמה המרכזית. האם להעלות הצגה אוונגרדית ויקרה עם קהל נישה, או פופולרית ובטוחה יותר כלכלית? מנהל טוב מנווט בין הדרישות.</li>
        <li><strong>חשיבות השיווק והמיתוג:</strong> גם יצירה מעולה צריכה קהל. שיווק אפקטיבי חיוני להגעה לקהלים, בניית מותג (מוניטין), ועידוד מכירת כרטיסים (פרסום, יח"צ, סושיאל, שיתופי פעולה).</li>
        <li><strong>בניית קהל ומעורבות קהילתית:</strong> הצלחה ארוכת טווח תלויה בקהל נאמן ובהפיכת התיאטרון לחלק מהקהילה (פעילויות חינוכיות, סדנאות, מחירים נגישים). קהל מגוון ונאמן הוא נכס יקר.</li>
        <li><strong>ניהול סיכונים וקבלת החלטות באי-ודאות:</strong> עולם התרבות אינו צפוי. הצלחת הצגה תלויה בגורמים רבים (ביקורות, מזג אוויר, טרנדים). על המנהל לקבל החלטות עם מידע חלקי, להעריך סיכונים ולהיות גמיש.</li>
        <li><strong>השפעת מוניטין וביקורת:</strong> מוניטין גבוה מושך אמנים מוכשרים, תמיכה ממוסדות, ומאפשר תמחור גבוה יותר. ביקורות חיוביות מגדילות ביקוש, שליליות פוגעות קשות.</li>
    </ul>
</div>

<style>
    /* Font Imports (Example - use appropriate licensed fonts if needed) */
     @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

    :root {
        --primary-color: #6A1B9A; /* Deep Purple */
        --secondary-color: #D81B60; /* Raspberry */
        --accent-color: #FFB300; /* Amber */
        --background-color: #F3E5F5; /* Light Purple */
        --panel-background: #FFFFFF; /* White */
        --text-color: #333333; /* Dark Grey */
        --border-color: #E0E0E0; /* Light Grey */
        --success-color: #4CAF50; /* Green */
        --error-color: #F44336; /* Red */
        --info-color: #2196F3; /* Blue */
    }

    body {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: var(--background-color);
        color: var(--text-color);
        line-height: 1.6;
        padding: 20px;
        margin: 0;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 10px;
        color: var(--secondary-color);
    }

    .intro-text {
        text-align: center;
        margin-bottom: 30px;
        font-size: 1.1em;
        color: #555;
    }

    #app-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 0;
        background-color: transparent; /* Panels have their own background */
        box-shadow: none;
        border-radius: 0;
    }

    .game-panel {
        margin-bottom: 25px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px; /* More rounded corners */
        background-color: var(--panel-background);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        transition: opacity 0.5s ease-in-out;
    }

     .current-state h2, .decision-making h2, .season-summary h2, .game-end h2, .theoretical-explanation h2 {
        margin-top: 0;
        color: var(--primary-color);
        border-bottom: 2px solid var(--accent-color); /* Thicker, colored border */
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    .state-item {
        margin-bottom: 12px;
        font-size: 1.1em;
        display: flex;
        align-items: center;
         justify-content: space-between; /* Distribute label and value */
        padding-bottom: 5px;
        border-bottom: 1px dotted var(--border-color);
    }

    .state-item:last-child {
         border-bottom: none;
         padding-bottom: 0;
    }

    .state-item .label {
        font-weight: bold;
        color: #555;
    }

     .state-item .value {
        font-weight: 500;
        color: var(--primary-color); /* Default value color */
    }

    .budget-value.profit { color: var(--success-color); }
    .budget-value.loss { color: var(--error-color); }
    .reputation-value { color: var(--secondary-color); }

    .reputation-bar-container {
        flex-grow: 1; /* Allow bar to take available space */
        height: 15px;
        background-color: #eee;
        border-radius: 8px;
        margin: 0 15px; /* Space around the bar */
        overflow: hidden;
        position: relative;
    }

    .reputation-bar {
        height: 100%;
        background-color: var(--secondary-color);
        width: 50%; /* Initial width, updated by JS */
        transition: width 0.5s ease-out; /* Smooth animation */
    }

     .change-indicator {
         display: inline-block;
         width: 0;
         height: 0;
         margin-right: 5px; /* Space before indicator */
         vertical-align: middle;
         transition: opacity 0.5s ease-in-out;
     }

     .change-indicator.profit::after {
         content: '▲';
         color: var(--success-color);
         font-size: 0.8em;
     }

     .change-indicator.loss::after {
         content: '▼';
         color: var(--error-color);
         font-size: 0.8em;
     }


    .decision-block {
        margin-bottom: 20px;
        padding: 15px;
        border: 1px solid #E0F2F7; /* Lighter border */
        border-radius: 8px;
        background-color: #E1BEE7; /* Very light purple */
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    }

     .decision-block:hover {
         transform: translateY(-3px); /* Lift effect on hover */
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
     }

    .decision-block h3 {
        margin-top: 0;
        margin-bottom: 15px;
        color: var(--primary-color);
        display: flex;
        align-items: center;
    }

    .decision-block h3 i {
         margin-left: 10px; /* Space for potential icons */
         font-size: 1.2em;
         color: var(--secondary-color);
    }

     /* Example icons (replace with actual if needed) */
     .icon-play::before { content: "🎭"; }
     .icon-marketing::before { content: "📢"; }
     .icon-venue::before { content: "🏛️"; }
     .icon-price::before { content: "💰"; }


    .decision-option {
        display: block; /* Each option on new line */
        margin-bottom: 10px;
        padding: 10px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        background-color: var(--panel-background);
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .decision-option:hover {
         background-color: #f8f8f8;
    }

    .decision-option input[type="radio"] {
        margin-left: 10px; /* Space for radio button */
        vertical-align: middle;
        accent-color: var(--primary-color); /* Style radio button */
    }

    .decision-option .option-title {
        font-weight: 500;
        color: var(--text-color);
    }

    .decision-option .option-details {
        font-size: 0.9em;
        color: #666;
    }


    .game-button {
        display: block;
        width: fit-content;
        margin: 20px auto 0;
        padding: 12px 25px;
        color: white;
        border: none;
        border-radius: 8px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: 500;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .game-button:hover {
         transform: translateY(-2px); /* Slight lift */
    }
     .game-button:active {
         transform: translateY(0); /* Press effect */
     }

    .primary-button {
        background-color: var(--primary-color);
    }
    .primary-button:hover {
        background-color: #5A148E;
    }

    .secondary-button {
         background-color: var(--secondary-color);
    }
    .secondary-button:hover {
         background-color: #C01554;
    }

    .explanation-button {
        background-color: var(--accent-color);
         margin-top: 20px;
    }
    .explanation-button:hover {
        background-color: #FFA000;
    }


    .season-summary ul {
        list-style: none;
        padding: 0;
        margin-bottom: 20px;
    }

    .season-summary ul li {
        margin-bottom: 8px;
         border-bottom: 1px dotted var(--border-color);
        padding-bottom: 5px;
        display: flex;
        justify-content: space-between;
    }

    .season-summary .label {
        font-weight: bold;
        color: #555;
    }

    .season-summary .value {
        font-weight: 500;
        color: var(--primary-color);
    }

     .profit-loss .value {
         font-size: 1.2em;
         font-weight: bold;
     }

     .profit {
         color: var(--success-color);
     }

     .loss {
         color: var(--error-color);
     }

     .result-message {
         font-style: italic;
         color: #666;
         margin-top: 15px;
         padding-top: 10px;
         border-top: 1px dashed #eee;
     }

    .updated-state-summary {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 2px dashed var(--accent-color);
    }

     .updated-state-summary p {
        margin-bottom: 8px;
     }

     .updated-state-summary .label {
         font-weight: bold;
         color: #555;
     }
     .updated-state-summary .value {
         font-weight: 500;
         color: var(--primary-color);
     }


    .game-end h2 {
         color: var(--error-color); /* Or success color if won */
         text-align: center;
         font-size: 2em;
    }

     #game-over-title.win {
        color: var(--success-color);
     }
      #game-over-title.lose {
        color: var(--error-color);
     }

    .game-end p {
        font-size: 1.1em;
        text-align: center;
        margin-bottom: 20px;
    }

    .theoretical-explanation {
         display: none; /* Initially hidden */
         margin-top: 20px;
         padding: 25px;
         border: 1px solid var(--border-color);
         border-radius: 12px;
         background-color: var(--panel-background);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    .theoretical-explanation h2 {
        margin-top: 0;
        color: var(--primary-color);
        border-bottom: 2px solid var(--accent-color);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    .theoretical-explanation ul {
        list-style: disc;
        padding-right: 20px;
    }

     .theoretical-explanation li {
        margin-bottom: 15px;
        line-height: 1.7;
     }

     /* Basic fade animation utility */
     .fade-in {
         opacity: 0;
         animation: fadeIn 0.5s ease-in-out forwards;
     }

    @keyframes fadeIn {
        to { opacity: 1; }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Game State Variables
        let season = 1;
        let budget = 20000;
        let reputation = 50; // Out of 100
        let audienceBase = 150; // Potential audience pool - slightly increased base

        // Game Settings
        const maxSeasons = 10;
        const staffCostPerSeason = 1500; // Slightly increased fixed cost

        // Play Options
        const plays = {
            rerun: { name: "העלאה מחודשת", cost: 0, audienceAppealMultiplier: 0.9, reputationEffect: -2, description: "הצגה מוכרת שלא דורשת השקעה חדשה, אך גם לא תרגש במיוחד את הקהל או המבקרים." },
            new: { name: "יצירה חדשה", cost: 3500, audienceAppealMultiplier: 1.4, reputationEffect: +8, description: "השקעה ביצירה מקורית. סיכון כלכלי גבוה יותר, אך פוטנציאל אמנותי וציבורי משמעותי." }
        };

        // Marketing Options
        const marketingOptions = {
            low: { name: "נמוכה", cost: 600, audienceEffect: 0.05, reputationEffect: 0, description: "השיווק המינימלי. מגיעים בעיקר לקהל הקבוע ולמי שמחפש באופן אקטיבי." },
            medium: { name: "בינונית", cost: 1800, audienceEffect: 0.2, reputationEffect: 1, description: "מאמץ שיווקי סביר. יכול למשוך קהל חדש באופן מוגבל ולשמר נראות." },
            high: { name: "גבוהה", cost: 3500, audienceEffect: 0.4, reputationEffect: 3, description: "קמפיין שיווקי אגרסיבי. חשיפה מקסימלית, פוטנציאל גבוה למשוך קהל חדש ולחזק את המותג." }
        };

        // Venue Options
        const venueOptions = {
            small: { name: "אולם קטן", cost: 1200, capacity: 60, description: "אולם אינטימי וזול יחסית לתפעול. מגביל את מספר הצופים האפשרי." },
            medium: { name: "אולם בינוני", cost: 3000, capacity: 180, description: "אולם בגודל סטנדרטי. איזון בין עלות לקיבולת." },
            large: { name: "אולם גדול", cost: 6000, capacity: 350, description: "אולם יוקרתי ומרווח. יקר מאוד לתפעול, אך מאפשר הכנסות גבוהות במקרה של הצלחה גדולה." }
        };

        // Pricing Options
        const priceOptions = {
            low: { name: "נמוך", price: 25, demandMultiplier: 1.8, description: "מחיר נגיש מאוד. ימשוך קהל רחב, אך ההכנסה לכרטיס נמוכה." }, // Increased price slightly
            medium: { name: "בינוני", price: 35, demandMultiplier: 1.1, description: "מחיר סטנדרטי. איזון בין ביקוש להכנסה." }, // Increased price slightly
            high: { name: "גבוה", price: 45, demandMultiplier: 0.7, description: "מחיר גבוה. עלול להרתיע קהל רגיש למחיר, אך מגדיל הכנסה מכל צופה." } // Increased price slightly
        };

        // UI Elements
        const gameStateDiv = document.getElementById('game-state');
        const decisionsDiv = document.getElementById('game-decisions');
        const resultsDiv = document.getElementById('game-results');
        const gameOverDiv = document.getElementById('game-over');

        const currentSeasonSpan = document.getElementById('current-season');
        const currentBudgetSpan = document.getElementById('current-budget');
        const budgetChangeIndicator = document.getElementById('budget-change');
        const currentReputationSpan = document.getElementById('current-reputation');
        const currentReputationBar = document.getElementById('current-reputation-bar');
        const reputationChangeIndicator = document.getElementById('reputation-change');
        const currentAudienceSpan = document.getElementById('current-audience');

        // Decisions are handled by their containers and input names

        const endSeasonButton = document.getElementById('end-season-button');
        const nextSeasonButton = document.getElementById('next-season-button');
        const restartGameButton = document.getElementById('restart-game-button');

        const summarySeasonSpan = document.getElementById('summary-season');
        const summaryPlaySpan = document.getElementById('summary-play');
        const summaryMarketingSpan = document.getElementById('summary-marketing');
        const summaryVenueSpan = document.getElementById('summary-venue');
        const summaryPriceSpan = document.getElementById('summary-price');
        const summaryExpensesSpan = document.getElementById('summary-expenses');
        const summaryRevenueSpan = document.getElementById('summary-revenue');
        const summaryProfitSpan = document.getElementById('summary-profit');
        const attendanceMessage = document.getElementById('attendance-message');
        const eventMessage = document.getElementById('event-message'); // New element for random events

        const nextSeasonNumberSpan = document.getElementById('next-season-number');
        const updatedBudgetSpan = document.getElementById('updated-budget');
        const updatedReputationSpan = document.getElementById('updated-reputation');
        const updatedAudienceSpan = document.getElementById('updated-audience');
        const buttonNextSeasonNumberSpan = document.getElementById('button-next-season-number');


        const gameOverTitle = document.getElementById('game-over-title');
        const gameOverMessage = document.getElementById('game-over-message');

        const explanationToggle = document.getElementById('explanation-toggle');
        const explanationDiv = document.getElementById('explanation');

        // --- Game Functions ---

        function updateUI() {
            currentSeasonSpan.textContent = season;
            currentBudgetSpan.textContent = budget.toFixed(0);
            currentReputationSpan.textContent = reputation.toFixed(0);
             currentReputationBar.style.width = reputation + '%'; // Update reputation bar
            currentAudienceSpan.textContent = audienceBase.toFixed(0);

            // Reset change indicators
            budgetChangeIndicator.className = 'change-indicator';
            reputationChangeIndicator.className = 'change-indicator';

            // Update Next Season button text
            buttonNextSeasonNumberSpan.textContent = season + 1;
        }

        function showDecisions() {
             // Apply fade out to current view, then switch and fade in decisions
            [gameStateDiv, resultsDiv, gameOverDiv, explanationDiv].forEach(el => {
                 if (el.style.display !== 'none') el.classList.add('fade-out');
            });


            // Use a timeout to allow fade-out animation before changing display
            setTimeout(() => {
                gameStateDiv.style.display = 'block';
                decisionsDiv.style.display = 'block';
                resultsDiv.style.display = 'none';
                gameOverDiv.style.display = 'none';
                 explanationDiv.style.display = 'none'; // Hide explanation on new season
                 explanationToggle.textContent = 'הצגת הסבר תיאורטי'; // Reset explanation button text

                // Remove fade-out and add fade-in to visible elements
                [gameStateDiv, decisionsDiv].forEach(el => {
                     el.classList.remove('fade-out');
                     el.classList.add('fade-in');
                });

                 updateUI(); // Update UI after showing decisions
            }, 500); // Match timeout to transition duration
        }

        function showResults(summary) {
             // Apply fade out to current view
             [gameStateDiv, decisionsDiv].forEach(el => el.classList.add('fade-out'));

             setTimeout(() => {
                gameStateDiv.style.display = 'none'; // Keep state hidden in results view
                decisionsDiv.style.display = 'none';
                resultsDiv.style.display = 'block';
                gameOverDiv.style.display = 'none';
                 explanationDiv.style.display = 'none'; // Hide explanation
                 explanationToggle.textContent = 'הצגת הסבר תיאורטי'; // Reset explanation button text

                 // Add fade-in to results
                 resultsDiv.classList.remove('fade-out');
                 resultsDiv.classList.add('fade-in');


                summarySeasonSpan.textContent = season - 1; // Report for the season that just ended
                summaryPlaySpan.textContent = summary.playName;
                summaryMarketingSpan.textContent = summary.marketingName;
                summaryVenueSpan.textContent = summary.venueName;
                summaryPriceSpan.textContent = summary.price + ' ש"ח';
                summaryExpensesSpan.textContent = summary.expenses.toFixed(0);
                summaryRevenueSpan.textContent = summary.revenue.toFixed(0);

                summaryProfitSpan.textContent = summary.profit.toFixed(0);
                 if (summary.profit >= 0) {
                    summaryProfitSpan.classList.remove('loss');
                    summaryProfitSpan.classList.add('profit');
                } else {
                    summaryProfitSpan.classList.remove('profit');
                    summaryProfitSpan.classList.add('loss');
                }

                // Display attendance message
                const attendanceRatio = summary.actualAudience / summary.venueCapacity;
                if (attendanceRatio >= 1) {
                    attendanceMessage.textContent = `האולם היה מלא לחלוטין (${summary.actualAudience.toFixed(0)} צופים)! ביקוש גבוה!`;
                    attendanceMessage.style.color = var(--success-color);
                } else if (attendanceRatio > 0.7) {
                     attendanceMessage.textContent = `האולם היה כמעט מלא (${summary.actualAudience.toFixed(0)} צופים). הצלחה יפה!`;
                     attendanceMessage.style.color = var(--primary-color);
                } else if (attendanceRatio > 0.4) {
                    attendanceMessage.textContent = `ההצגה משכה קהל בינוני (${summary.actualAudience.toFixed(0)} צופים). יש מקום לשיפור.`;
                    attendanceMessage.style.color = var(--info-color);
                } else {
                    attendanceMessage.textContent = `הקהל היה דליל למדי (${summary.actualAudience.toFixed(0)} צופים). יש לחשוב על אסטרטגיה חדשה.`;
                    attendanceMessage.style.color = var(--error-color);
                }

                 // Display random event message if any
                 if (summary.eventMessage) {
                     eventMessage.textContent = summary.eventMessage;
                     eventMessage.style.color = summary.eventEffect > 0 ? var(--success-color) : var(--error-color);
                     eventMessage.style.display = 'block';
                 } else {
                     eventMessage.style.display = 'none';
                 }


                nextSeasonNumberSpan.textContent = season; // Display number for the NEXT season in the summary header
                updatedBudgetSpan.textContent = budget.toFixed(0);
                updatedReputationSpan.textContent = reputation.toFixed(0);
                 updatedAudienceSpan.textContent = audienceBase.toFixed(0);

                // Animate state changes in results summary (optional, can be complex)
                // For now, just update values. CSS transitions handle reputation bar.

                 // Update budget/reputation change indicators in the next season display
                if (summary.profit > 0) updatedBudgetSpan.classList.add('profit');
                else if (summary.profit < 0) updatedBudgetSpan.classList.add('loss');

                if (summary.repChange > 0) updatedReputationSpan.classList.add('profit');
                else if (summary.repChange < 0) updatedReputationSpan.classList.add('loss');


            }, 500);
        }

        function showGameOver(title, message, isWin) {
             // Apply fade out
            [gameStateDiv, decisionsDiv, resultsDiv, explanationDiv].forEach(el => {
                 if (el.style.display !== 'none') el.classList.add('fade-out');
            });

             setTimeout(() => {
                gameStateDiv.style.display = 'none';
                decisionsDiv.style.display = 'none';
                resultsDiv.style.display = 'none';
                explanationDiv.style.display = 'none';
                 gameOverDiv.style.display = 'block';

                // Add fade-in
                 gameOverDiv.classList.remove('fade-out');
                 gameOverDiv.classList.add('fade-in');


                gameOverTitle.textContent = title;
                gameOverMessage.textContent = message;

                 gameOverTitle.classList.remove('win', 'lose');
                 if (isWin) {
                     gameOverTitle.classList.add('win');
                 } else {
                     gameOverTitle.classList.add('lose');
                 }


                 explanationToggle.style.display = 'none'; // Hide explanation button at game over

            }, 500);
        }


        function calculateSeasonResults(decisions) {
            const chosenPlay = plays[decisions.play];
            const chosenMarketing = marketingOptions[decisions.marketing];
            const chosenVenue = venueOptions[decisions.venue];
            const chosenPrice = priceOptions[decisions.price];

            // Costs
            const fixedCosts = staffCostPerSeason + chosenVenue.cost;
            const playCost = chosenPlay.cost;
            const marketingCost = chosenMarketing.cost;
            const totalCosts = fixedCosts + playCost + marketingCost;

            // Audience & Revenue
            // Base potential influenced by current audience base, reputation, play appeal, marketing, and price demand
            // Add some more nuanced influence and randomness
            let potentialDemand = audienceBase *
                                    (0.7 + (reputation / 100) * 0.5) * // Reputation effect (0.7 to 1.2 multiplier)
                                    chosenPlay.audienceAppealMultiplier *
                                    (1 + chosenMarketing.audienceEffect) *
                                    chosenPrice.demandMultiplier;

            // Add seasonality/randomness (e.g., up to 20% variation)
            potentialDemand *= (0.8 + Math.random() * 0.4); // Multiplier between 0.8 and 1.2

            // Actual audience is limited by venue capacity AND potential demand
            const actualAudience = Math.min(potentialDemand, chosenVenue.capacity);

            const revenue = actualAudience * chosenPrice.price;

            // Profit
            const profit = revenue - totalCosts;

            // Update State for Next Season
            budget += profit;

            // Reputation changes based on profit, play choice, marketing, attendance ratio and a random event
            let repChange = profit / 8000; // Profitability affects reputation (less direct impact)
            repChange += chosenPlay.reputationEffect; // Play choice effect
            repChange += chosenMarketing.reputationEffect; // Marketing effect

             // Attendance vs Capacity effect on reputation
            const attendanceRatio = actualAudience / chosenVenue.capacity;
             if (attendanceRatio >= 0.95) repChange += 4; // Great success!
             else if (attendanceRatio > 0.7) repChange += 2;
             else if (attendanceRatio < 0.3) repChange -= 3; // Poor attendance hurts reputation
             else if (attendanceRatio < 0.5) repChange -= 1;


            let eventMessageText = '';
            let eventEffectValue = 0;
            // Random event: positive or negative review / external factor
            if (Math.random() < 0.2) { // 20% chance of a significant random event
                 const isPositive = Math.random() < (reputation / 100); // More likely positive with high reputation?
                 eventEffectValue = (isPositive ? 1 : -1) * (3 + Math.random() * 7); // +/- 3 to 10 points
                 repChange += eventEffectValue;

                 if (eventEffectValue > 0) eventMessageText = `חדשות מצוינות! ביקורת נלהבת או אירוע בלתי צפוי העלו את המוניטין.`;
                 else eventMessageText = `חדשות רעות! ביקורת קטלנית או תקלה פגעו קשות במוניטין.`;
            }


            reputation = Math.max(0, Math.min(100, reputation + repChange)); // Clamp reputation between 0 and 100


            // Audience Base changes slowly based on reputation and previous season's attendance ratio
            let audienceGrowthFactor = (reputation / 100) * 0.1 + // Reputation contributes to growth (up to 10%)
                                       (chosenMarketing.audienceEffect * 0.1) + // Marketing contributes (less direct here)
                                       (attendanceRatio - 0.5) * 0.2; // If venue was full, growth; if empty, decline


            audienceBase = audienceBase * (1 + audienceGrowthFactor);


            // Ensure audienceBase doesn't go below a minimum or exceed a high maximum
            audienceBase = Math.max(80, Math.min(800, audienceBase)); // Adjusted min/max


            season++;

            // Prepare summary
            const summary = {
                playName: chosenPlay.name,
                marketingName: chosenMarketing.name + ` (${chosenMarketing.cost} ש"ח)`,
                venueName: chosenVenue.name,
                price: chosenPrice.price,
                expenses: totalCosts,
                revenue: revenue,
                profit: profit,
                actualAudience: actualAudience, // Pass actual attendance for message
                venueCapacity: chosenVenue.capacity, // Pass capacity for message
                repChange: repChange, // Pass total reputation change
                eventMessage: eventMessageText,
                eventEffect: eventEffectValue
            };

            return summary;
        }

        function startGame() {
            season = 1;
            budget = 25000; // Start with a bit more budget
            reputation = 50;
            audienceBase = 150;
            showDecisions();
            // Initial state update is called within showDecisions
        }

        function endGame() {
            explanationToggle.style.display = 'none'; // Hide explanation button

            if (budget < 0) {
                showGameOver("פשיטת רגל!", `התקציב אזל לחלוטין לאחר עונה ${season - 1}. למרבה הצער, וילונות התיאטרון יורדים בפעם האחרונה.`, false);
            } else if (season > maxSeasons) {
                 let finalMessage = `הגעת לסוף ${maxSeasons} עונות! הצלחת לנווט את התיאטרון בהצלחה דרך האתגרים.`;
                 let isWin = true;

                 if (budget >= 40000 && reputation >= 75) {
                      finalMessage += ` התיאטרון פורח תחת ניהולך! סיימת עם קופה מפוארת ומוניטין זוהר. בראבו!`;
                      isWin = true;
                 } else if (budget >= 20000 && reputation >= 50) {
                     finalMessage += ` התיאטרון יציב ובריא. סיימת את התקופה עם תקציב סביר ומוניטין מכובד. עבודה טובה!`;
                     isWin = true; // Considered a win if survived and not in bad shape
                 } else {
                     finalMessage += ` סיימת את התקופה, אך התיאטרון נקלע לקשיים. עם תקציב נמוך ומוניטין ירוד, העתיד נראה מאתגר...`;
                     isWin = false; // Survived, but maybe not a 'success'
                 }
                 finalMessage += `<br>מצב סופי: קופה ${budget.toFixed(0)} ש"ח, מוניטין ${reputation.toFixed(0)}/100, קהל פוטנציאלי כ-${audienceBase.toFixed(0)} איש.`;


                showGameOver("סוף המסע!", finalMessage, isWin);
            }
        }

        // --- Event Listeners ---

        endSeasonButton.addEventListener('click', () => {
             // Check if game over conditions are already met (e.g., budget went negative during previous season's calculation display)
             if (budget < 0 || season > maxSeasons) {
                 endGame();
                 return; // Stop if game is already over
             }

            // Get user decisions
            const decisions = {
                play: document.querySelector('input[name="play"]:checked').value,
                marketing: document.querySelector('input[name="marketing"]:checked').value,
                venue: document.querySelector('input[name="venue"]:checked').value,
                price: document.querySelector('input[name="price"]:checked').value,
            };

            // Calculate results and update state
            const summary = calculateSeasonResults(decisions);

            // Show results
            showResults(summary);

            // Check end game conditions AFTER showing results
            if (budget < 0 || season > maxSeasons) {
                // Delay showing game over slightly to allow results fade in
                setTimeout(endGame, 1000);
            }
        });

        nextSeasonButton.addEventListener('click', () => {
            if (season <= maxSeasons && budget >= 0) {
                 showDecisions();
                 // updateUI is called within showDecisions
            } else {
                 // This case should ideally be caught by the endGame check after calculating results,
                 // but add a fallback just in case.
                 endGame();
            }
        });

        restartGameButton.addEventListener('click', () => {
            startGame();
            explanationToggle.style.display = 'block'; // Show explanation button again
        });

        explanationToggle.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
             // Fade out current view before showing explanation
             [gameStateDiv, decisionsDiv, resultsDiv, gameOverDiv].forEach(el => {
                if (el.style.display !== 'none') el.classList.add('fade-out');
            });

             setTimeout(() => {
                 // Hide all game panels
                 [gameStateDiv, decisionsDiv, resultsDiv, gameOverDiv].forEach(el => el.style.display = 'none');

                 // Toggle explanation visibility
                explanationDiv.style.display = isHidden ? 'block' : 'none';
                 explanationDiv.classList.remove('fade-out', 'fade-in'); // Reset animations
                 if (isHidden) explanationDiv.classList.add('fade-in');


                explanationToggle.textContent = isHidden ? 'חזרה למשחק' : 'הצגת הסבר תיאורטי';

                // If hiding explanation, return to the appropriate game state
                if (!isHidden) {
                    // Logic here is tricky - where to return?
                    // Best to simply restart the game flow or return to decisions if not game over
                    // Let's return to decisions if game isn't over
                    if (budget >= 0 && season <= maxSeasons) {
                         showDecisions(); // This will fade in decisions and state
                    } else {
                         // If game was over *before* showing explanation, show game over again
                        endGame(); // This will show game over with fade-in
                    }
                }

             }, 500); // Match timeout to transition duration
        });


        // --- Initialize Game ---
        startGame();
         // Hide results and game over sections on initial load
        resultsDiv.style.display = 'none';
        gameOverDiv.style.display = 'none';

    });
</script>