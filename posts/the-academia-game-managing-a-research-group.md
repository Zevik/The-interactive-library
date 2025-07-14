---
title: "משחק האקדמיה: המסע לפרופסורה"
english_slug: the-academia-game-managing-a-research-group
category: "חשיבה ביקורתית"
tags: [אקדמיה, ניהול מחקר, מימון מדעי, פרסום אקדמי, סימולציה, משחק]
---
<h1>משחק האקדמיה: המסע לפרופסורה</h1>
<p>צא/י למסע מרתק אל פסגת האקדמיה! האם הצלחה מדעית טמונה רק בתגליות גאוניות, או שמא ניהול תקציב חכם, גיוס משאבים בלתי פוסק, ובניית מוניטין דרך פרסומים הם המפתח? התנסה/י בניהול קבוצת מחקר אקדמית והבן/י את האתגרים, הסיכונים וההזדמנויות הנסתרות במסע לפרופסורה.</p>

<div id="academia-game-app">
    <div id="dashboard" class="game-panel">
        <h2>לוח בקרה אקדמי</h2>
        <div class="stats-grid">
            <div><strong>שנה אקדמית:</strong> <span id="current-year" class="stat-value">1</span></div>
            <div><strong>מאזן תקציבי:</strong> $<span id="budget" class="stat-value">0</span></div>
            <div><strong>צוות מחקר:</strong> <span id="team-size" class="stat-value">0</span> חברי צוות</div>
            <div><strong>עלות צוות שנתית:</strong> $<span id="yearly-cost" class="stat-value">0</span></div>
            <div><strong>פרסומים מוכרים:</strong> <span id="publications" class="stat-value">0</span></div>
            <div><strong>ידע ופוטנציאל מדעי:</strong> <span id="research-points" class="stat-value">0</span> נקודות</div>
            <div><strong>מוניטין אקדמי:</strong> <span id="reputation" class="stat-value">0</span> נקודות מוניטין</div>
             <div><strong>פעילויות בהמתנה:</strong> <span id="pending-submissions" class="stat-value">0</span> (בקשות מימון ומאמרים)</div>
        </div>
    </div>

    <div id="decision-area" class="game-panel">
        <h2>החלטות אסטרטגיות לשנה <span class="current-year-label stat-value">1</span></h2>
        <div class="decision-section">
            <h3><i class="icon-money"></i> גיוס מימון למחקר:</h3>
            <p>השקע/י בפנייה לקרנות מחקר יוקרתיות:</p>
            <button class="action-button grant-button" data-grant-id="1">מענק בסיסי (עלות הגשה: $5k, פוטנציאל זכייה: $100k, סיכוי בסיסי: 60%)</button>
            <button class="action-button grant-button" data-grant-id="2">מענק תחרותי (עלות הגשה: $20k, פוטנציאל זכייה: $500k, סיכוי בסיסי: 30%)</button>
            <button class="action-button grant-button" data-grant-id="3">מענק יוקרתי (עלות הגשה: $50k, פוטנציאל זכייה: $2M, סיכוי בסיסי: 10%)</button>
             <p class="decision-status" id="grant-decision-status"></p>
        </div>

        <div class="decision-section">
            <h3><i class="icon-team"></i> בניית צוות מחקר:</h3>
             <p>גייס/י מוחות מבריקים שיניעו את המחקר:</p>
            <button class="action-button hire-button" data-researcher-type="phd">צרף/י דוקטורנט/ית (עלות שנתית: $40k, תרומה למחקר: +5 נקודות ידע לשנה)</button>
            <button class="action-button hire-button" data-researcher-type="postdoc">צרף/י פוסט-דוקטורנט/ית (עלות שנתית: $70k, תרומה למחקר: +15 נקודות ידע לשנה)</button>
             <p class="decision-status" id="hire-decision-status"></p>
        </div>

         <div class="decision-section">
            <h3><i class="icon-publish"></i> פרסום תגליות מדעיות:</h3>
             <p>הפוך/י את הידע שצברת/ה להכרה בינלאומית:</p>
            <button id="publish-button" class="action-button" disabled>נסה/י לפרסם מאמר (עלות תהליך: $10k, דורש 50 נקודות ידע)</button>
             <p class="decision-status" id="publish-decision-status"></p>
        </div>

        <button id="next-year-button" class="action-button primary-button">עבור/י לשנה האקדמית הבאה »</button>
    </div>

    <div id="events-log" class="game-panel">
        <h2>יומן אירועים אקדמי</h2>
        <ul id="event-list">
            <li class="event-info">התחלת את דרכך כחוקר/ת בכיר/ה חדש/ה!</li>
             <li class="event-success">קיבלת תקציב התחלתי בסך $100,000 להקמת קבוצת המחקר.</li>
        </ul>
    </div>
</div>

<style>
    :root {
        --primary-color: #0056b3;
        --secondary-color: #f0f8ff;
        --panel-bg: #ffffff;
        --panel-border: #e0e0e0;
        --button-bg: #e9ecef;
        --button-hover-bg: #ced4da;
        --button-primary-bg: #28a745;
        --button-primary-hover-bg: #218838;
        --text-color: #343a40;
        --header-color: #004085;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --warning-color: #ffc107;
        --info-color: #17a2b8;
        --font-family: 'Arial', sans-serif;
    }

    #academia-game-app {
        font-family: var(--font-family);
        direction: rtl;
        text-align: right;
        max-width: 900px;
        margin: 30px auto;
        padding: 20px;
        background-color: var(--secondary-color);
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        display: grid;
        grid-template-columns: 1fr; /* Stack panels on smaller screens */
        gap: 20px;
    }

    @media (min-width: 768px) {
         #academia-game-app {
            grid-template-columns: 1fr 1fr; /* Two columns on larger screens */
         }
         #dashboard {
            grid-column: 1 / 3; /* Dashboard spans two columns */
         }
         #decision-area {
            grid-column: 1 / 3; /* Decision area spans two columns */
         }
         #events-log {
             grid-column: 1 / 3; /* Events log spans two columns */
         }
    }


    .game-panel {
        background-color: var(--panel-bg);
        border: 1px solid var(--panel-border);
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }

    h1 {
        text-align: center;
        color: var(--primary-color);
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    h2 {
        color: var(--header-color);
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 2px solid var(--panel-border);
        padding-bottom: 10px;
        font-size: 1.4em;
    }

    h3 {
        color: var(--text-color);
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.1em;
    }

    p {
        color: var(--text-color);
        line-height: 1.6;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
    }

    .stats-grid > div {
         padding: 8px 0;
         border-bottom: 1px dotted var(--panel-border);
    }

     .stats-grid > div:last-child {
         border-bottom: none;
     }


    .stat-value {
        font-weight: bold;
        color: var(--primary-color);
    }

    .decision-section {
        margin-bottom: 25px;
        padding: 15px;
        border: 1px solid var(--panel-border);
        border-radius: 8px;
        background-color: #f8f9fa;
    }

    .action-button {
        margin: 5px;
        padding: 12px 20px;
        cursor: pointer;
        border: none; /* Use background/box-shadow instead of border */
        border-radius: 5px;
        background-color: var(--button-bg);
        color: var(--text-color);
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .action-button:hover:not(:disabled) {
        background-color: var(--button-hover-bg);
        transform: translateY(-1px);
    }

    .action-button:active:not(:disabled) {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    }

    .action-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        box-shadow: none;
    }

    .primary-button {
        background-color: var(--button-primary-bg);
        color: white;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .primary-button:hover:not(:disabled) {
        background-color: var(--button-primary-hover-bg);
    }

    #next-year-button {
        display: block;
        width: 100%;
        margin-top: 30px;
        padding: 15px;
        font-size: 1.2em;
    }

    .decision-status {
        margin-top: 10px;
        font-style: italic;
        color: var(--text-color);
        font-size: 0.9em;
    }

    #events-log {
        max-height: 300px; /* Make log scrollable */
        overflow-y: auto;
    }

    #event-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    #event-list li {
        margin-bottom: 10px;
        padding-bottom: 8px;
        border-bottom: 1px dotted var(--panel-border);
        font-size: 0.95em;
        line-height: 1.5;
        opacity: 0; /* Start invisible for animation */
        transform: translateY(10px); /* Start slightly below */
        animation: fadeSlideIn 0.5s ease forwards; /* Animation applied by JS, but define here */
    }

    #event-list li:last-child {
         border-bottom: none;
     }

     .event-info { color: var(--info-color); }
     .event-success { color: var(--success-color); font-weight: bold; }
     .event-danger { color: var(--danger-color); font-weight: bold; }
     .event-warning { color: var(--warning-color); }

     /* Add simple icons (using text for now) */
     .decision-section h3 i {
         margin-left: 5px;
         color: var(--primary-color);
     }
     .icon-money::before { content: '💰'; }
     .icon-team::before { content: '👥'; }
     .icon-publish::before { content: '📚'; }


     /* Animations */
    @keyframes fadeSlideIn {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes flashGreen {
        0% { background-color: inherit; }
        50% { background-color: rgba(40, 167, 69, 0.3); } /* success-color with alpha */
        100% { background-color: inherit; }
    }

     @keyframes flashRed {
        0% { background-color: inherit; }
        50% { background-color: rgba(220, 53, 69, 0.3); } /* danger-color with alpha */
        100% { background-color: inherit; }
    }

     .flash-green { animation: flashGreen 1s ease; }
     .flash-red { animation: flashRed 1s ease; }


     /* Explanation Section */
     #explanation-toggle {
        display: block;
        width: 100%;
        padding: 15px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        font-size: 1.1em;
        margin-top: 30px;
        margin-bottom: 20px;
        cursor: pointer;
        border-radius: 8px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
     }

    #explanation-toggle:hover {
        background-color: #004085;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }


    #explanation {
        display: none; /* Initially hidden */
        margin-top: 20px;
        padding: 25px;
        border: 1px solid var(--panel-border);
        border-radius: 8px;
        background-color: #f8f9fa;
        direction: rtl;
        text-align: right;
        line-height: 1.7;
    }

    #explanation h2, #explanation h3 {
        color: var(--header-color);
        margin-bottom: 10px;
        border-bottom: none;
        padding-bottom: 0;
    }

    #explanation h2 { font-size: 1.5em; border-bottom: 2px solid var(--panel-border); padding-bottom: 10px; margin-bottom: 15px;}
    #explanation h3 { font-size: 1.2em; margin-top: 20px; }

    #explanation p, #explanation ul {
        margin-bottom: 15px;
        line-height: 1.6;
    }

    #explanation ul {
        padding-right: 20px;
        list-style: disc;
    }

     #explanation li {
         margin-bottom: 8px;
         line-height: 1.5;
     }
</style>

<button id="explanation-toggle">הצג/הסתר: מדריך למסע האקדמי</button>

<div id="explanation">
    <h2>מדריך למסע האקדמי: ניהול קבוצת מחקר</h2>
    <p>ההצלחה בזירה האקדמית אינה מסתכמת אך ורק בגאונות מדעית טהורה. היא דורשת שילוב נדיר של חשיבה פורצת דרך עם כישורים ניהוליים, פיננסיים, ויכולת לבנות קשרים ולהציג את עבודתך לעולם. הסימולציה שזה עתה חוויתם מדמה את האתגרים וההזדמנויות המרכזיים המעצבים את מסעו של חוקר/ת בכיר/ה.</p>

    <h3>הליבה: קבוצת המחקר (הלאב)</h3>
    <p>קבוצת מחקר אקדמית (המכונה לרוב "הלאב") היא היחידה המרכזית בה מתרחש המחקר בפועל. היא מנוהלת על ידי חוקר/ת בכיר/ה (Principal Investigator - PI), לרוב פרופסור/ית. הלב הפועם של הלאב הוא צוות המחקר – תלמידי מחקר (מאסטר, דוקטורט) ופוסט-דוקטורנטים, המקדישים את זמנם וכשרונם לקידום פרויקטים מחקריים תחת הנחיית ה-PI. ככל שהצוות גדול ומנוסה יותר, כך גדל פוטנציאל יצירת הידע המדעי.</p>

    <h3>המנוע: מימון מחקר (המענקים)</h3>
    <p>מחקר מדעי הוא פעילות יקרה. הוא דורש ציוד מתקדם, חומרים יקרים, נסיעות לכנסים, ולרוב, ובעיקר, מימון למלגות ומשכורות לחברי הצוות. רוב מוחלט של מימון זה מגיע ממענקי מחקר תחרותיים. הגשת בקשה למענק היא תהליך מורכב ותחרותי ביותר, הדורש ניסוח הצעת מחקר מפורטת ומשכנעת, הצגת תקציב ריאלי, והדגשת יכולותיו המדעיות והניהוליות של ה-PI והצוות. זכייה במענק אינה רק מקור מימון חיוני, אלא גם אישור חיצוני לערך המחקר והחוקר, ובכך תורמת משמעותית למוניטין האקדמי.</p>

    <h3>ההד: פרסום מדעי</h3>
    <p>תוצר הדגל של קבוצת מחקר הוא פרסום ממצאיה בכתבי עת מדעיים מובילים. פרסום הוא הדרך המרכזית לחלוק תגליות חדשות עם הקהילה המדעית העולמית. תהליך הפרסום ארוך ומאתגר וכולל:</p>
    <ul>
        <li><strong>כתיבת המאמר:</strong> הצגה שיטתית של שאלת המחקר, השיטות, התוצאות והמסקנות.</li>
        <li><strong>הגשה לכתב עת:</strong> בחירת כתב עת מתאים והגשת המאמר.</li>
        <li><strong>שיפוט עמיתים (Peer Review):</strong> חוקרים אחרים בתחום בוחנים את המאמר בקפידה, ומספקים ביקורת והערות לעורך כתב העת. שלב זה קריטי לאיכות המדעית.</li>
        <li><strong>תיקונים:</strong> כמעט תמיד נדרשים תיקונים משמעותיים או קטנים על סמך הערות השופטים. לעיתים קרובות נדרשים גם ניסויים נוספים.</li>
        <li><strong>קבלה או דחייה:</strong> רק חלק קטן מהמאמרים שמוגשים לכתבי עת יוקרתיים מתקבלים בסופו של דבר לפרסום.</li>
    </ul>

    <h3>המשוואה האקדמית: מימון + פרסום = קידום (Publish or Perish)</h3>
    <p>קידום אקדמי - ממרצה בכיר לפרופסור חבר, וממנו לפרופסור מן המניין - תלוי באופן דרמטי ביכולתו של החוקר להראות תרומה משמעותית ומתמשכת לתחום המחקר. שני האינדיקטורים המרכזיים לכך הם: הצלחה עקבית בגיוס מימון (מענקים רבים וגדולים) ורשימת פרסומים מרשימה בכתבי עת בעלי השפעה גבוהה. מענקים מראים יכולת להוביל ולהשיג משאבים, ופרסומים מוכיחים את התרומה האמיתית לידע. ללא שניהם, הדרך לקידום, ואף לעיתים ההישארות במערכת, קשה עד בלתי אפשרית. זהו המקור לביטוי הידוע לשמצה 'Publish or Perish' (פרסם או אבד).</p>

    <h3>אתגרים לאורך הדרך</h3>
    <ul>
        <li><strong>ניהול תקציב:</strong> מענקים מגיעים לתקופות מוגבלות, ונדרש תכנון קפדני כדי לממן את פעילות הלאב לאורך שנים. הוצאות בלתי צפויות תמיד אורבות מעבר לפינה.</li>
        <li><strong>ניהול צוות:</strong> הנחיית חברי צוות, שמירה על מוטיבציה, התמודדות עם קשיים אישיים ומקצועיים, וכן עם עזיבת חוקרים לקראת השלמת לימודיהם או למשרות אחרות.</li>
        <li><strong>איזון זמנים:</strong> הקצאת זמן נכון בין מחקר בפועל, כתיבת הצעות מחקר, כתיבת מאמרים, הוראה, מטלות אדמיניסטרטיביות, בניית קשרים ועוד.</li>
        <li><strong>התמודדות עם דחיות:</strong> דחיות הן חלק בלתי נפרד מהחיים האקדמיים (דחיות מענקים, דחיות מאמרים). נדרשת עמידות נפשית גבוהה ואמונה בעבודה.</li>
        <li><strong>בחירות אסטרטגיות:</strong> אילו פרויקטים לקחת? האם להשקיע בפרויקט מסוכן ופורץ דרך פוטנציאלית, או בפרויקט בטוח יותר אך עם פוטנציאל תגלית נמוך יותר, שיניב פרסום מהיר יחסית?</li>
    </ul>

    <h3>הדרך לפרופסורה: תמהיל מנצח</h3>
    <p>מסע מוצלח לפרופסורה דורש שילוב סינרגטי של מצוינות מדעית, יצירתיות, פרודוקטיביות גבוהה (פרסומים רבים ואיכותיים), יכולת מרשימה בגיוס משאבים, כישורים ניהוליים והנחייתיים, בניית רשת קשרים ענפה, עמידות נפשית, ולבסוף, תכנון אסטרטגי ארוך טווח שמטרתו לבסס את החוקר כמוביל/ה בתחומו/ה.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // --- Game State ---
        let year = 1;
        let budget = 100000; // Initial budget
        let teamSize = 0;
        let yearlyCost = 0;
        let publications = 0;
        let researchPoints = 0;
        let reputation = 0; // New: Academic Reputation
        let pendingGrants = []; // { id, potential, chance, name }
        let pendingPublications = []; // { cost, baseChance }
        let decisionsMadeThisYear = {
            grantApplied: false,
            publishAttempted: false
        };
        let gameEnded = false;

        // --- Game Constants ---
        const grants = {
            1: { name: "מענק בסיסי", applyCost: 5000, award: 100000, baseSuccessChance: 0.6, repGain: 5 },
            2: { name: "מענק תחרותי", applyCost: 20000, award: 500000, baseSuccessChance: 0.3, repGain: 15 },
            3: { name: "מענק יוקרתי", applyCost: 50000, award: 2000000, baseSuccessChance: 0.1, repGain: 40 }
        };
        const researcherCosts = {
            phd: 40000,
            postdoc: 70000
        };
         const researcherResearchPoints = {
            phd: 5,
            postdoc: 15
        };
        const publishCost = 10000;
        const publishResearchPointsRequired = 50;
        const publishBaseSuccessChance = 0.4; // Simplified average success chance
        const publishRepGain = 10;
        const reputationFactor = 0.003; // How much reputation affects chance (0.3% per rep point) - Fine-tune this

        // Win Condition
        const winConditionYears = 20;
        const winConditionPublications = 15;
        const winConditionBudget = 2000000; // $2M

        // --- DOM Elements ---
        const yearSpan = document.getElementById('current-year');
        const budgetSpan = document.getElementById('budget');
        const teamSizeSpan = document.getElementById('team-size');
        const yearlyCostSpan = document.getElementById('yearly-cost');
        const publicationsSpan = document.getElementById('publications');
        const researchPointsSpan = document.getElementById('research-points');
        const reputationSpan = document.getElementById('reputation'); // New Reputation span
        const pendingSubmissionsSpan = document.getElementById('pending-submissions');
        const eventList = document.getElementById('event-list');
        const grantButtons = document.querySelectorAll('.grant-button');
        const hireButtons = document.querySelectorAll('.hire-button');
        const publishButton = document.getElementById('publish-button');
        const nextYearButton = document.getElementById('next-year-button');
        const currentYearLabels = document.querySelectorAll('.current-year-label');
        const grantDecisionStatus = document.getElementById('grant-decision-status');
        const hireDecisionStatus = document.getElementById('hire-decision-status');
        const publishDecisionStatus = document.getElementById('publish-decision-status');
        const explanationDiv = document.getElementById('explanation');
        const explanationToggleBtn = document.getElementById('explanation-toggle');
        const academiaGameAppDiv = document.getElementById('academia-game-app');


        // --- Update UI Functions ---
        function updateDashboard() {
            yearSpan.textContent = year;
            budgetSpan.textContent = budget.toLocaleString();
            teamSizeSpan.textContent = teamSize;
            yearlyCostSpan.textContent = yearlyCost.toLocaleString();
            publicationsSpan.textContent = publications;
            researchPointsSpan.textContent = researchPoints;
            reputationSpan.textContent = reputation; // Update reputation
            pendingSubmissionsSpan.textContent = pendingGrants.length + pendingPublications.length;

            currentYearLabels.forEach(el => el.textContent = year);

             // Update publish button state
             const canPublish = researchPoints >= publishResearchPointsRequired && budget >= publishCost;
            if (canPublish && !decisionsMadeThisYear.publishAttempted) {
                publishButton.disabled = false;
                publishButton.textContent = `נסה/י לפרסם מאמר (עלות: $${publishCost.toLocaleString()}, דורש ${publishResearchPointsRequired} ידע)`;
                publishDecisionStatus.textContent = `דרושים: ${publishResearchPointsRequired} ידע, $${publishCost.toLocaleString()}. ברשותך: ${researchPoints} ידע, $${budget.toLocaleString()}.`;
            } else {
                 publishButton.disabled = true;
                 if (decisionsMadeThisYear.publishAttempted) {
                      publishButton.textContent = `ניסית לפרסם מאמר השנה`;
                      publishDecisionStatus.textContent = "הוגשה בקשה לפרסום מאמר השנה.";
                 } else if (researchPoints < publishResearchPointsRequired && budget < publishCost) {
                     publishButton.textContent = `אין מספיק ידע (${researchPoints}/${publishResearchPointsRequired}) או תקציב ($${budget.toLocaleString()}/${publishCost.toLocaleString()})`;
                      publishDecisionStatus.textContent = `דרושים: ${publishResearchPointsRequired} ידע, $${publishCost.toLocaleString()}. ברשותך: ${researchPoints} ידע, $${budget.toLocaleString()}.`;
                 } else if (researchPoints < publishResearchPointsRequired) {
                     publishButton.textContent = `אין מספיק ידע (${researchPoints}/${publishResearchPointsRequired})`;
                     publishDecisionStatus.textContent = `דרושים: ${publishResearchPointsRequired} ידע. ברשותך: ${researchPoints}.`;
                 } else if (budget < publishCost) {
                      publishButton.textContent = `אין מספיק תקציב ($${budget.toLocaleString()}/${publishCost.toLocaleString()})`;
                      publishDecisionStatus.textContent = `דרוש: $${publishCost.toLocaleString()}. ברשותך: $${budget.toLocaleString()}.`;
                 }
            }

             // Update grant button states
             if(decisionsMadeThisYear.grantApplied) {
                 grantButtons.forEach(btn => btn.disabled = true);
                 grantDecisionStatus.textContent = "הוגשה בקשת מימון השנה. המתן/י לתוצאות בשנה הבאה.";
             } else {
                  grantButtons.forEach(btn => {
                      const grantId = btn.dataset.grantId;
                      const grant = grants[grantId];
                      btn.disabled = budget < grant.applyCost;
                      btn.textContent = `${grant.name} (עלות: $${grant.applyCost.toLocaleString()}, סיכוי משוער: ${(grant.baseSuccessChance + reputation * reputationFactor)*100}%)$`;
                  });
                   grantDecisionStatus.textContent = budget < Math.min(grants[1].applyCost, grants[2].applyCost, grants[3].applyCost) ? "אין מספיק תקציב להגשת בקשת מימון כלשהי." : "";
             }

             // Update hire button states - always enabled if budget allows yearly cost
             hireButtons.forEach(btn => {
                const type = btn.dataset.researcherType;
                const cost = researcherCosts[type];
                // Can you afford the *next* yearly cost if you hire them? Simple check.
                btn.disabled = budget < yearlyCost + cost;
                btn.textContent = `צרף/י ${type === 'phd' ? 'דוקטורנט/ית' : 'פוסט-דוקטורנט/ית'} (עלות שנתית: $${cost.toLocaleString()}, תרומה למחקר: +${researcherResearchPoints[type]} ידע)`;
             });
             hireDecisionStatus.textContent = budget < yearlyCost + Math.min(researcherCosts.phd, researcherCosts.postdoc) && teamSize > 0 ? "אין מספיק תקציב כדי לשלם לצוות קיים + לצרף חבר חדש." : "";

        }

        function addEvent(text, type = 'info') {
            const li = document.createElement('li');
            li.textContent = `שנה ${year}: ${text}`;
            li.classList.add(`event-${type}`);
            eventList.prepend(li); // Add to the top
             // Apply animation class after adding to DOM
             requestAnimationFrame(() => {
                 li.style.animation = 'none';
                 void li.offsetWidth; // Trigger reflow
                 li.style.animation = `fadeSlideIn 0.5s ease forwards`;
             });
        }

        // Animation for budget change
        function animateBudgetChange(oldBudget, newBudget) {
            const budgetElement = document.getElementById('budget');
            budgetElement.textContent = newBudget.toLocaleString(); // Update text immediately
            const animationClass = newBudget > oldBudget ? 'flash-green' : 'flash-red';
            budgetElement.classList.remove('flash-green', 'flash-red'); // Remove existing
            requestAnimationFrame(() => { // Re-add after repaint
                 budgetElement.classList.add(animationClass);
                 // Remove class after animation
                 budgetElement.addEventListener('animationend', () => {
                     budgetElement.classList.remove(animationClass);
                 }, { once: true });
            });
        }

        // --- Game Logic Functions ---
        function applyForGrant(grantId) {
            if (gameEnded) return;
            if (decisionsMadeThisYear.grantApplied) {
                 addEvent(`כבר הגשת בקשת מימון השנה.`, 'warning');
                 grantDecisionStatus.textContent = "כבר הוגשה בקשה השנה.";
                 return;
            }
            const grant = grants[grantId];
            if (budget >= grant.applyCost) {
                const oldBudget = budget;
                budget -= grant.applyCost;
                 animateBudgetChange(oldBudget, budget);
                pendingGrants.push({ id: grantId, potential: grant.award, chance: Math.min(1, grant.baseSuccessChance + reputation * reputationFactor), name: grant.name, repGain: grant.repGain });
                decisionsMadeThisYear.grantApplied = true;
                addEvent(`יצאת לציד מענקים: הוגשה בקשה ל-"${grant.name}". עלות: $${grant.applyCost.toLocaleString()}. בהצלחה!`, 'info');
                updateDashboard();
            } else {
                addEvent(`אין מספיק תקציב להגשת בקשת מימון "${grant.name}". עלות: $${grant.applyCost.toLocaleString()}.`, 'warning');
                 grantDecisionStatus.textContent = `אין מספיק תקציב להגשת בקשה זו. דרוש: $${grant.applyCost.toLocaleString()}.`;
            }
        }

        function hireResearcher(type) {
            if (gameEnded) return;
             const cost = researcherCosts[type];
             const rp = researcherResearchPoints[type];

             if (budget >= yearlyCost + cost) { // Check if next year's cost is affordable
                 teamSize++;
                 yearlyCost += cost;
                 // Research points contribution is calculated at year end
                 addEvent(`צוות מתרחב: צורפ/ה ${type === 'phd' ? 'דוקטורנט/ית' : 'פוסט-דוקטורנט/ית'} לצוות. עלות שנתית נוספת: $${cost.toLocaleString()}.`, 'info');
                 updateDashboard();
             } else {
                  addEvent(`אין מספיק תקציב לגייס ${type === 'phd' ? 'דוקטורנט/ית' : 'פוסט-דוקטורנט/ית'} בעלות שנתית של $${cost.toLocaleString()}. ודא/י שיש מספיק למשכורות של כלל הצוות בשנה הבאה.`, 'warning');
             }
             // hiring doesn't block other actions, so no decisionsMadeThisYear.hireAttempted
        }

        function attemptPublish() {
            if (gameEnded) return;
            if (decisionsMadeThisYear.publishAttempted) {
                 addEvent(`כבר ניסית לפרסם מאמר השנה. המתן/י לתוצאות.`, 'warning');
                 publishDecisionStatus.textContent = "כבר הוגשה בקשה השנה.";
                 return;
            }
            if (researchPoints >= publishResearchPointsRequired) {
                if (budget >= publishCost) {
                    const oldBudget = budget;
                    budget -= publishCost;
                     animateBudgetChange(oldBudget, budget);
                    researchPoints -= publishResearchPointsRequired;
                    pendingPublications.push({ cost: publishCost, baseChance: publishBaseSuccessChance, repGain: publishRepGain });
                     decisionsMadeThisYear.publishAttempted = true;
                    addEvent(`מעשה של ידע: ניסית לפרסם מאמר. עלות: $${publishCost.toLocaleString()}. המתן/י לשיפוט בשנה הבאה!`, 'info');
                    updateDashboard();
                } else {
                    addEvent(`אין מספיק תקציב כדי לממן את תהליך פרסום המאמר. עלות: $${publishCost.toLocaleString()}.`, 'warning');
                     publishDecisionStatus.textContent = `אין מספיק תקציב. דרוש: $${publishCost.toLocaleString()}.`;
                }
            } else {
                addEvent(`אין מספיק נקודות ידע מדעי כדי לנסות לפרסם מאמר. דרושות ${publishResearchPointsRequired} נקודות.`, 'warning');
                 publishDecisionStatus.textContent = `אין מספיק ידע מדעי. דרוש: ${publishResearchPointsRequired}.`;
            }
        }

        function advanceYear() {
            if (gameEnded) return;

            addEvent(`--- סיום שנה ${year}, לקראת שנה ${year + 1} ---`, 'info');

            // 1. Pay yearly costs (team salaries)
            const oldBudget = budget;
            budget -= yearlyCost;
            addEvent(`שולם $${yearlyCost.toLocaleString()} עבור משכורות הצוות.`);
            animateBudgetChange(oldBudget, budget);


            // Check for game over condition (negative budget)
            if (budget < 0) {
                 addEvent(`אין מספיק תקציב! המאזן התקציבי שלילי ($${budget.toLocaleString()}). נאלצת לסגור את קבוצת המחקר. המשחק הסתיים בשנה ${year}.`, 'danger');
                 endGame(false); // Lost
                 return;
            }

            // 2. Process pending grants
            addEvent(`בדיקת תוצאות בקשות מימון שהוגשו...`);
            const resolvedGrants = [];
            pendingGrants.forEach(grant => {
                 const adjustedChance = Math.min(1, grant.baseSuccessChance + reputation * reputationFactor); // Re-calculate chance based on current reputation
                 const roll = Math.random();
                 // console.log(`Grant "${grant.name}": Base Chance ${grant.baseSuccessChance}, Rep: ${reputation}, Rep Factor: ${reputationFactor}, Adjusted Chance: ${adjustedChance.toFixed(2)}, Roll: ${roll.toFixed(2)}`);

                if (roll < adjustedChance) {
                    const oldBudget = budget;
                    budget += grant.potential;
                    reputation += grant.repGain; // Gain reputation from success
                    addEvent(`פריצת דרך מימונית! בקשת המימון "${grant.name}" התקבלה! קיבלת $${grant.potential.toLocaleString()} מימון מחקר. המוניטין האקדמי עלה ב-${grant.repGain} נקודות.`, 'success');
                    animateBudgetChange(oldBudget, budget);

                } else {
                    // reputation = Math.max(0, reputation - Math.floor(grant.repGain / 4)); // Small rep loss on failure? Maybe too harsh. Let's just not gain.
                    addEvent(`חדשות פחות טובות: בקשת המימון "${grant.name}" נדחתה. המשיכו להגיש!`, 'info');
                }
                resolvedGrants.push(grant); // Mark as resolved
            });
            pendingGrants = []; // Clear pending grants

            // 3. Process pending publications
             addEvent(`בדיקת סטטוס מאמרים שהוגשו...`);
            const resolvedPublications = [];
            pendingPublications.forEach(pub => {
                const adjustedChance = Math.min(1, pub.baseChance + reputation * reputationFactor * 1.5); // Publications might be more sensitive to rep?
                 const roll = Math.random();
                 // console.log(`Publication: Base Chance ${pub.baseChance}, Rep: ${reputation}, Rep Factor: ${reputationFactor}, Adjusted Chance: ${adjustedChance.toFixed(2)}, Roll: ${roll.toFixed(2)}`);

                 if (roll < adjustedChance) {
                     publications++;
                     reputation += pub.repGain; // Gain reputation from success
                     addEvent(`הכרה אקדמית! המאמר התקבל לפרסום! מזל טוב! המוניטין האקדמי עלה ב-${pub.repGain} נקודות.`, 'success');
                 } else {
                     // reputation = Math.max(0, reputation - Math.floor(pub.repGain / 4)); // Small rep loss on failure?
                     addEvent(`נדרשים תיקונים משמעותיים/המאמר נדחה. אל ייאוש, נסה/י שוב לאחר שיפורים!`, 'info');
                 }
                 resolvedPublications.push(pub); // Mark as resolved
            });
            pendingPublications = []; // Clear pending publications

            // 4. Generate new research points based on team size
            const pointsPerTeamMember = teamSize > 0 ? (teamSize * 10) + Math.floor(Math.random() * 5) : 0; // Base + small random
             // Optional: Add a small boost from reputation to RP generation?
            const reputationBonusRP = Math.floor(reputation / 5); // 1 RP for every 5 reputation points
            const pointsGained = pointsPerTeamMember + reputationBonusRP;

            researchPoints += pointsGained;
            if (teamSize > 0) {
                 addEvent(`הצוות עבד במרץ! נוצרו ${pointsGained} נקודות ידע מדעי (כולל בונוס מוניטין של ${reputationBonusRP} נקודות).`);
            } else {
                 addEvent(`אין חברי צוות פעילים. לא נוצרו נקודות ידע מדעי השנה.`);
            }

            // 5. Handle random events
             addEvent(`בדיקת אירועים אקראיים...`);
            const randomEventRoll = Math.random(); // 0 to 1
            const eventChance = 0.1; // 10% chance of any significant random event
            const positiveEventChance = 0.5; // 50% of events are positive
            const negativeEventChance = 0.5; // 50% of events are negative

            if (randomEventRoll < eventChance) {
                 const eventTypeRoll = Math.random(); // Decide if positive or negative
                 if (eventTypeRoll < positiveEventChance) { // Positive Events
                     const positiveSpecificRoll = Math.random();
                     if (positiveSpecificRoll < 0.6) { // 60% of positive are budget bonus
                          const bonus = Math.floor(Math.random() * 60000) + 15000; // $15k - $75k
                          const oldBudget = budget;
                          budget += bonus;
                          addEvent(`אירוע משמח! זכית/ה בפרס מחקר קטן לא מתוכנן! נוספו $${bonus.toLocaleString()} למאזן.`, 'success');
                          animateBudgetChange(oldBudget, budget);
                     } else { // 40% of positive are RP/Rep bonus
                         const rpBonus = Math.floor(Math.random() * 60) + 20; // +20-80 RP
                         const repBonus = Math.floor(Math.random() * 10) + 5; // +5-15 Rep
                         researchPoints += rpBonus;
                         reputation += repBonus;
                         addEvent(`אירוע משמח! פריצת דרך מינורית פנימית העניקה ${rpBonus} נקודות ידע מדעי ופרסום בבלוג מדעי העלה את המוניטין ב-${repBonus} נקודות.`, 'success');
                     }
                 } else { // Negative Events
                      const negativeSpecificRoll = Math.random();
                      if (negativeSpecificRoll < 0.5) { // 50% of negative are unexpected costs
                          const cost = Math.floor(Math.random() * 40000) + 10000; // $10k - $50k
                           const oldBudget = budget;
                          budget -= cost;
                           addEvent(`אירוע מצער: הוצאה בלתי מתוכננת (תיקון ציוד/קנס אדמיניסטרטיבי) בסך $${cost.toLocaleString()}.`, 'danger');
                           animateBudgetChange(oldBudget, budget);

                            // Check game over again after unexpected cost
                            if (budget < 0) {
                                addEvent(`אין מספיק תקציב! המאזן התקציבי שלילי ($${budget.toLocaleString()}). נאלצת לסגור את קבוצת המחקר. המשחק הסתיים בשנה ${year}.`, 'danger');
                                endGame(false); // Lost
                                return;
                           }

                      } else { // 50% of negative are researcher leaving
                           if (teamSize > 0) {
                                // Which researcher leaves? For simplicity, just reduce team size and cost by an average amount
                                const costReduction = yearlyCost / teamSize;
                                teamSize--;
                                yearlyCost -= costReduction;
                                // Maybe a small reputation hit? Or RP loss? Let's just add event.
                                addEvent(`אירוע מצער: חבר/ת צוות מפתח/ת עזב/ה במפתיע. מספר חברי הצוות ירד. עלות שנתית פחתה ב-$${costReduction.toLocaleString()}.`, 'danger');
                           } else {
                                // If no team members, turn negative event into a minor cost or delay
                                const cost = Math.floor(Math.random() * 10000) + 2000;
                                 const oldBudget = budget;
                                budget -= cost;
                                 addEvent(`אירוע מצער: עיכוב אדמיניסטרטיבי גרם להוצאה קטנה בסך $${cost.toLocaleString()}.`, 'danger');
                                animateBudgetChange(oldBudget, budget);
                           }
                      }
                 }
            } else {
                 // addEvent(`השנה עברה ללא אירועים אקראיים מיוחדים.`); // Too chatty, remove for now
            }


            // 6. Reset decisions for the new year
            decisionsMadeThisYear = {
                grantApplied: false,
                publishAttempted: false
            };

            // 7. Check for Win Condition
            if (year >= winConditionYears || (publications >= winConditionPublications && budget >= winConditionBudget)) {
                 addEvent(`--- סיום המשחק ---`, 'info');
                 let winReason = `עברו ${year} שנים של ניהול קבוצת מחקר בהצלחה!`;
                 if (publications >= winConditionPublications && budget >= winConditionBudget) {
                     winReason = `הגעת להישג מרשים: ${publications} פרסומים ו-$${budget.toLocaleString()} תקציב!`;
                 }
                 addEvent(`ברכות! הצלחת במסע לפרופסורה! ${winReason}`, 'success');
                 endGame(true);
                 return;
            }


            // 8. Advance year counter and update dashboard
            year++;
            updateDashboard();
        }

        function endGame(isWin) {
            gameEnded = true;
            nextYearButton.disabled = true;
            grantButtons.forEach(btn => btn.disabled = true);
            hireButtons.forEach(btn => btn.disabled = true);
            publishButton.disabled = true;
             academiaGameAppDiv.classList.add(isWin ? 'game-win' : 'game-over');
        }


        // --- Event Listeners ---
        grantButtons.forEach(button => {
            button.addEventListener('click', () => {
                const grantId = button.dataset.grantId;
                applyForGrant(parseInt(grantId));
            });
        });

        hireButtons.forEach(button => {
            button.addEventListener('click', () => {
                const type = button.dataset.researcherType;
                hireResearcher(type);
            });
        });

        publishButton.addEventListener('click', attemptPublish);

        nextYearButton.addEventListener('click', advanceYear);

        explanationToggleBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            explanationToggleBtn.textContent = isHidden ? 'הסתר: מדריך למסע האקדמי' : 'הצג/הסתר: מדריך למסע האקדמי';
             explanationToggleBtn.classList.toggle('active', !isHidden);
        });


        // --- Initial Setup ---
        updateDashboard(); // Set initial dashboard state
         addEvent("בהצלחה במסע לביסוס קבוצת המחקר וההגעה לפסגת האקדמיה!", 'info');
         addEvent("המשחק מתחיל בתקציב התחלתי של $100,000.");
    });
</script>
```