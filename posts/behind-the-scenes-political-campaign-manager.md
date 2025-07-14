---
title: "מאחורי הקלעים: אמן הקמפיין הפוליטי"
english_slug: behind-the-scenes-political-campaign-manager
category: "מדעי החברה / מדע המדינה ומדיניות ציבורית"
tags: [פוליטיקה, קמפיין בחירות, אסטרטגיה, סימולציה, ייעוץ פוליטי, משחק]
---
<div id="app">
    <h1>ניהול חברת ייעוץ פוליטי: אמנות הניצחון</h1>
    <p class="intro-text">ברוכים הבאים לעולם המורכב והמרתק של ניהול קמפיינים פוליטיים. האם יש לכם את מה שצריך כדי להפוך מועמדים אפורים לגיבורים לאומיים? האם תצליחו לנווט בין מוקשים תקציביים, יריבים אכזריים ודעת קהל הפכפכה?</p>
    <p class="intro-text">בתפקיד מנהל חברת ייעוץ פוליטי, כל החלטה שלכם משפיעה. הקצו תקציבים, בחרו אסטרטגיות, וראו כיצד המוניטין והכספים שלכם עולים... או צונחים.</p>

    <div id="company-status" class="status-panel">
        <h2>מצב החברה</h2>
        <p>💰 כספים בקופה: <span id="company-funds"></span> ש"ח</p>
        <p>🌟 מוניטין החברה: <span id="company-reputation"></span> / 100</p>
        <p>📅 סבב בחירות: <span id="election-cycle"></span></p>
    </div>

    <div id="campaigns-section">
        <h3>קמפיינים נוכחיים תחת אחריותנו</h3>
        <div id="campaigns-list">
            <!-- Campaigns will be rendered here -->
        </div>
    </div>

    <button id="next-cycle-btn" class="action-button">סיים סבב וקדם בחירות</button>

    <div id="updates" class="updates-panel">
        <h3>עדכונים, תוצאות והשפעות</h3>
        <div id="updates-content">
            <!-- Updates and results will be shown here -->
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    :root {
        --primary-color: #0056b3;
        --secondary-color: #f0f0f0;
        --accent-color: #28a745;
        --warning-color: #ffc107;
        --danger-color: #dc3545;
        --background-color: #e9ecef;
        --card-background: #ffffff;
        --border-color: #dee2e6;
        --text-color: #343a40;
        --header-color: #00308f;
    }

    #app {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 950px;
        margin: 30px auto;
        padding: 30px;
        border-radius: 12px;
        background-color: var(--background-color);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        color: var(--text-color);
    }

    h1 {
        color: var(--header-color);
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700;
    }

    h2, h3 {
        color: var(--primary-color);
        margin-top: 20px;
        margin-bottom: 15px;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 5px;
    }

    .intro-text {
        text-align: center;
        margin-bottom: 20px;
        font-size: 1.1em;
        line-height: 1.6;
        color: #555;
    }

    .status-panel, .updates-panel {
        margin-bottom: 25px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--card-background);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

     .status-panel p {
         font-size: 1.1em;
         margin-bottom: 10px;
         padding-right: 10px; /* Indent slightly */
     }

     .status-panel p span {
         font-weight: bold;
         color: var(--primary-color);
     }

    #campaigns-section h3 {
         border-bottom: none; /* Remove border for this section header */
         margin-bottom: 10px;
    }

    #campaigns-list {
         display: grid;
         grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsive grid */
         gap: 20px;
    }


    .campaign {
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 20px;
        background-color: var(--secondary-color);
        display: flex;
        flex-direction: column;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .campaign:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }

    .campaign h4 {
        margin-top: 0;
        margin-bottom: 15px;
        color: var(--primary-color);
        font-weight: 700;
        font-size: 1.3em;
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 10px;
    }

    .campaign-stats {
        margin-bottom: 15px;
        font-size: 0.95em;
    }

    .campaign-stats p {
        margin: 8px 0;
        line-height: 1.4;
    }

    .campaign-stats p span {
        font-weight: bold;
        color: var(--text-color);
    }

     /* Budget status indicator */
     .campaign-stats p.budget-status {
         font-weight: bold;
         color: var(--accent-color); /* Default: Green */
     }
     .campaign-stats p.budget-status.warning {
         color: var(--warning-color); /* Yellow */
     }
     .campaign-stats p.budget-status.danger {
         color: var(--danger-color); /* Red */
     }


    .allocation-controls {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px dashed var(--border-color);
    }

    .allocation-controls div {
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .allocation-controls label {
        flex-grow: 1; /* Allows label to take available space */
        margin-left: 10px;
        font-weight: bold;
        color: #555;
    }

    .allocation-controls input[type="number"] {
        width: 100px; /* Fixed width for consistency */
        padding: 8px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        font-size: 1em;
        text-align: left; /* Align numbers to the left */
         -moz-appearance: textfield; /* Remove default number input arrows */
         appearance: textfield;
    }

     /* Hide arrows for number input */
     .allocation-controls input[type="number"]::-webkit-outer-spin-button,
     .allocation-controls input[type="number"]::-webkit-inner-spin-button {
         -webkit-appearance: none;
         margin: 0;
     }


    .allocation-controls input[type="number"]:focus {
        border-color: var(--primary-color);
        outline: none;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.2);
    }

    .action-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.2em;
        cursor: pointer;
        margin-top: 30px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 700;
    }

    .action-button:hover:not(:disabled) {
        background-color: #004080;
        transform: translateY(-2px);
    }

    .action-button:active:not(:disabled) {
         transform: translateY(0);
    }

    .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
    }

    .updates-panel h3 {
        border-bottom: 1px solid var(--border-color);
        margin-bottom: 10px;
        padding-bottom: 8px;
    }

    #updates-content {
        max-height: 250px; /* Slightly increased height */
        overflow-y: auto;
        padding-right: 15px; /* Space for scrollbar */
        scrollbar-width: thin;
        scrollbar-color: var(--primary-color) var(--secondary-color);
    }

    #updates-content::-webkit-scrollbar {
        width: 8px;
    }

    #updates-content::-webkit-scrollbar-track {
        background: var(--secondary-color);
        border-radius: 10px;
    }

    #updates-content::-webkit-scrollbar-thumb {
        background-color: var(--primary-color);
        border-radius: 10px;
        border: 2px solid var(--secondary-color);
    }


    #updates-content p {
        margin-bottom: 10px;
        line-height: 1.5;
        font-size: 0.95em;
        color: var(--text-color);
        padding: 8px;
        border-bottom: 1px dashed var(--border-color);
    }

     #updates-content p:last-child {
         border-bottom: none;
         margin-bottom: 0;
     }

    /* Specific update message styles */
     #updates-content p strong {
         color: var(--primary-color);
     }
     #updates-content p .win {
         color: var(--accent-color);
         font-weight: bold;
     }
     #updates-content p .loss {
         color: var(--danger-color);
         font-weight: bold;
     }
     #updates-content p .warning {
         color: var(--warning-color);
         font-weight: bold;
     }
     #updates-content p .info {
         color: #007bff;
         font-weight: bold;
     }


    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    #toggle-explanation:hover {
        background-color: #5a6268;
    }

    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--card-background);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        line-height: 1.7;
    }

    #explanation h2 {
        margin-top: 0;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 5px;
    }

    #explanation h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: var(--primary-color);
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 3px;
    }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px;
    }

    #explanation li {
        margin-bottom: 8px;
    }

    @media (max-width: 768px) {
        #app {
            padding: 20px;
            margin: 20px auto;
        }

        .campaign {
             padding: 15px;
        }

        .campaign h4 {
             font-size: 1.2em;
        }

        .allocation-controls div {
             flex-direction: column;
             align-items: flex-start;
        }

        .allocation-controls label {
             width: auto;
             margin-left: 0;
             margin-bottom: 5px;
        }

         .allocation-controls input[type="number"] {
             width: 100%; /* Full width on small screens */
             text-align: right;
         }

        .action-button {
            font-size: 1.1em;
            padding: 10px;
        }
    }
</style>

<button id="toggle-explanation">הצג/הסתר מילון מונחים ורקע תאורטי</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: המדע והאמנות של ניהול קמפיין</h2>
    <p>ניהול קמפיין פוליטי הוא תזמורת מורכבת הדורשת שילוב נדיר של אסטרטגיה חדה, הבנה פסיכולוגית של הבוחר, יעילות לוגיסטית וכישרון תקשורתי. חברות ייעוץ פוליטי הן המאסטרו מאחורי הקלעים, המנווטות את המועמדים בדרך אל קלפיות.</p>

    <h3>מה עושה יועץ פוליטי, באמת?</h3>
    <p>הרבה מעבר לכותרות. ייעוץ פוליטי עוסק בבניית נתיב מפורט לניצחון. זה מתחיל באבחון עמוק: הבנת הזירה הפוליטית, זיהוי חוזקות וחולשות של המועמד והיריבים, וניתוח מדוקדק של דעת הקהל. על בסיס זה בונים אסטרטגיה - מסרים, קהלי יעד, ואופן הפנייה אליהם. בהמשך, מתרגמים את האסטרטגיה לתוכנית פעולה תקציבית, לוגיסטית ותקשורתית.</p>

    <h3>שלבים מכריעים במרוץ</h3>
    <ul>
        <li><strong>מחקר ואסטרטגיה:</strong> שלב ה'מודיעין'. סקרים וקבוצות מיקוד חושפים את הלך הרוח הציבורי, מאפשרים בחינת מסרים ומיצוב המועמד. כאן מגבשים את הנרטיב ואת התוכנית הגדולה.</li>
        <li><strong>בניית מסרים:</strong> תמצית הרעיונות וההצעות של המועמד, מעוצבים באופן שידבר ללב ולראש של הבוחרים הרלוונטיים. חייבים להיות ברורים, עקביים ומבדלים.</li>
        <li><strong>גיוס משאבים ותקציב:</strong> כסף הוא דלק הקמפיין. גיוס תרומות וניהול תקציב חכם הם קריטיים. החלטה היכן להשקיע כל שקל (פרסום? שטח? דיגיטל?) יכולה לחרוץ גורלות.</li>
        <li><strong>ביצוע והפצה:</strong> הוצאת התוכנית לפועל – פרסום ממוקד, פעילות שטח אינטנסיבית (מדלת לדלת, כנסים), ניהול נוכחות ברשתות החברתיות, ויצירת אירועים שייצרו הד תקשורתי.</li>
        <li><strong>מעקב, ניתוח והתאמה:</strong> קמפיין הוא יצור חי ונושם. יש לעקוב אחר השפעת הפעולות (שוב, דרך סקרים ומדיה), לזהות משברים או הזדמנויות, ולהתאים את האסטרטגיה והטקטיקה בזמן אמת. גמישות ויכולת תגובה מהירה הן שם המשחק.</li>
    </ul>

    <h3>כלי השפעה מרכזיים (ואיך הם משפיעים בסימולציה)</h3>
    <ul>
        <li><strong>סקרים (Surveys):</strong> הכרחיים להבנת המצב ולקבלת החלטות מבוססות נתונים. אינם מניעים בוחרים ישירות, אך השקעה בהם משפרת את יעילות כל שאר הפעולות (בסימולציה: משפרים קלות את הסקר הסופי, ומקטינים את הסיכון ל'הפתעות' שליליות).</li>
        <li><strong>פרסום בטלוויזיה (TV Ads):</strong> מגיע לקהל רחב מאוד, אך יקר להחריד. יעיל לבניית מותג והעברת מסרים פשוטים לקהל הכללי (בסימולציה: השפעה חזקה על הסקר, עלות גבוהה).</li>
        <li><strong>פרסום דיגיטלי (Digital Ads):</strong> ממוקד ומדויק, מאפשר פנייה לקהלים ספציפיים ברשתות החברתיות ובאתרים. עלות נמוכה יחסית לטלוויזיה, יעיל לגיוס פעילים ושיח (בסימולציה: השפעה טובה מאוד על הסקר ביחס לעלות).</li>
        <li><strong>שלטי חוצות (Billboards):</strong> נוכחות פיזית קבועה במרחב הציבורי. טובים לחיזוק שם המועמד באזור גיאוגרפי ממוקד ולהעברת מסר ויזואלי פשוט (בסימולציה: השפעה בינונית על הסקר, עלות בינונית).</li>
        <li><strong>פעילות שטח (Field Work):</strong> המפגש הבלתי אמצעי עם הבוחרים - כנסים קטנים, דלת לדלת, שיחות טלפון מתומכים. בונה נאמנות אישית ומניע אנשים לצאת להצביע. דורש משאבים ארגוניים וכוח אדם (בסימולציה: השפעה מצוינת על הסקר, בעיקר כשהמוניטין גבוה, עלות בינונית).</li>
        <li><strong>ייעוץ אסטרטגי (Consulting):</strong> שכר הטרחה שלכם! (בסימולציה: תמיד יש לכם עלות תפעול בסיסית. הקצאת תקציב ל'ייעוץ' מייצגת השקעה ביכולות הכלליות של החברה, עם השפעה קטנה ועקבית על כל הקמפיינים).</li>
    </ul>

    <h3>תקציב: האכסניה של האסטרטגיה</h3>
    <p>התקציב הוא לב ליבו של כל קמפיין. לעולם אין מספיק כסף לכל מה שרוצים לעשות. תפקידכם הוא להחליט באילו סעיפים להשקיע ועל מה לוותר, בהתאם לאסטרטגיה ולנקודות החוזק והחולשה של הקמפיין. השקעה לא נכונה יכולה לכלות את המשאבים מבלי לייצר תנופה, או גרוע מכך – לגרום לחריגה שמסכנת את המועמד ואתכם.</p>

    <h3>השפעת המוניטין שלכם</h3>
    <p>כחברת ייעוץ, המוניטין שלכם הוא ההון העיקרי. ניצחונות בונים אותו, הפסדים שוחקים אותו, וחריגה תקציבית פוגעת בו. מוניטין גבוה מושך קמפיינים גדולים ורווחיים יותר, מקנה לכם יתרון קל במאבקי סקרים (אמינות נתפסת), ואף מגדיל את 'תקרת הזכוכית' הפוטנציאלית של המועמדים שלכם.</p>

    <h3>דילמות ומשברים</h3>
    <p>העבודה אינה רק מספרים וסקרים. לעיתים תצטרכו להתמודד עם דילמות קשות – האם לתקוף יריב? כיצד להגיב לשערורייה? האם להשקיע בקבוצת בוחרים קטנה אך חיונית או לכוון לקהל הרחב? הסימולציה הזו נועדה לתת טעימה מהאתגרים האסטרטגיים והתקציביים הללו.</p>

    <h3>המשחק</h3>
    <p>בכל 'סבב בחירות', תנהלו מספר קמפיינים במקביל. לכל קמפיין תקציב מוגדר ומצב ראשוני בסקרים מול יריב. תפקידכם להקצות את התקציב בין סעיפי הפעילות השונים (סקרים, טלוויזיה, דיגיטל וכו'). בסיום הסבב, המערכת תחשב את השפעת ההקצאות על מצב הסקרים של כל קמפיין, תוך התחשבות בהשפעות נוספות (כוח יריב, פוטנציאל מועמד, והמוניטין של חברת הייעוץ שלכם). קמפיינים שיעברו את רף הסקרים הנדרש יחשבו כניצחון, יניבו לכם כספים ומוניטין, וקמפיינים שיפסידו יעלו לכם כסף ויפגעו במוניטין. זכרו גם את עלויות התפעול השוטפות של החברה. המטרה: לשרוד, לשגשג, ולהפוך לחברת הייעוץ הפוליטי המובילה!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Simulation State
        let companyFunds = 150000; // Start with more initial funds
        let companyReputation = 60; // Start with a slightly higher base reputation
        let electionCycle = 1;
        let campaigns = [];
        let gameActive = true;

        // Simulation Parameters & Balancing
        const WINNING_POLL_THRESHOLD_MARGIN = 2; // Need to reach > Opponent + this margin to win
        const BASE_ALLOCATION_EFFECTS = { // Base points per 1000 allocated
            Surveys: 0.05, // Small direct poll effect, but crucial for accuracy/efficiency (handled in logic)
            TV_Ads: 0.2,
            Digital_Ads: 0.25, // Higher ROI than TV
            Billboards: 0.1,
            Field_Work: 0.3, // Strongest per-₪ effect, especially with high reputation
            Consulting: 0 // Cost is overhead, no direct allocation effect
        };
        const DIMINISHING_RETURNS_FACTOR = 0.000005; // How much the effect per ₪ decreases as allocation increases
        const REPUTATION_EFFECT_MULTIPLIER = 0.005; // How much reputation boosts poll effect (per 1000 allocated)
        const INITIAL_CAMPAIGN_BONUS_MULTIPLIER = 0.8; // Company gets back budget + percentage of budget as bonus for winning
        const REPUTATION_CHANGE_WIN_NATIONAL = 15;
        const REPUTATION_CHANGE_WIN_MUNICIPAL = 7;
        const REPUTATION_CHANGE_LOSE_NATIONAL = -10;
        const REPUTATION_CHANGE_LOSE_MUNICIPAL = -4;
        const REPUTATION_CHANGE_OVERBUDGET = -5; // Significant hit for mismanagement
        const BASE_COMPANY_OVERHEAD = 15000; // Increased overhead per cycle
        const MIN_POLL = 5; // Poll can't go below this
        const MAX_REPUTATION = 100;
        const MIN_REPUTATION_FOR_NEW_CAMPAIGNS = 20; // Stop getting new campaigns if reputation too low
        const GAME_OVER_FUNDS = -100000; // More forgiving bankruptcy limit

        // DOM Elements
        const companyFundsEl = document.getElementById('company-funds');
        const companyReputationEl = document.getElementById('company-reputation');
        const electionCycleEl = document.getElementById('election-cycle');
        const campaignsListEl = document.getElementById('campaigns-list');
        const nextCycleBtn = document.getElementById('next-cycle-btn');
        const updatesContentEl = document.getElementById('updates-content');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const explanationEl = document.getElementById('explanation');

        // Initial Setup
        function initializeGame() {
            campaigns = [
                { id: 1, name: "מועמד/ת עירוני/ת א'", level: "מוניציפלי", initialBudget: 40000, potential: 65, opponentStrength: 50, initialPoll: 45, currentPoll: 45, allocation: { Surveys: 0, TV_Ads: 0, Digital_Ads: 0, Billboards: 0, Field_Work: 0, Consulting: 0 } },
                { id: 2, name: "מפלגה ארצית ב'", level: "ארצי", initialBudget: 250000, potential: 55, opponentStrength: 58, initialPoll: 50, currentPoll: 50, allocation: { Surveys: 0, TV_Ads: 0, Digital_Ads: 0, Billboards: 0, Field_Work: 0, Consulting: 0 } },
                { id: 3, name: "מועמד/ת עירוני/ת ג'", level: "מוניציפלי", initialBudget: 50000, potential: 70, opponentStrength: 55, initialPoll: 52, currentPoll: 52, allocation: { Surveys: 0, TV_Ads: 0, Digital_Ads: 0, Billboards: 0, Field_Work: 0, Consulting: 0 } }
            ];
            updateUI();
            logUpdate("<span class='info'>✨ ברוכים הבאים לאמנות הניצחון! קיבלתם 3 קמפיינים ראשונים לניהול.</span>", 'info');
        }

        // Update UI
        function updateUI() {
            companyFundsEl.textContent = formatNumber(companyFunds);
            companyReputationEl.textContent = companyReputation;
            electionCycleEl.textContent = electionCycle;

            campaignsListEl.innerHTML = '';
            if (campaigns.length === 0 && gameActive) {
                 campaignsListEl.innerHTML = '<p>אין קמפיינים פעילים בסבב זה. לחצו על "קדם בחירות" לקבלת אתגרים חדשים.</p>';
            } else if (!gameActive) {
                 campaignsListEl.innerHTML = '<p>המשחק הסתיים.</p>';
            }

            campaigns.forEach(campaign => {
                const campaignDiv = document.createElement('div');
                campaignDiv.classList.add('campaign');
                campaignDiv.setAttribute('data-id', campaign.id); // Use data attribute for ID
                campaignDiv.innerHTML = `
                    <h4>${campaign.name} (${campaign.level})</h4>
                    <div class="campaign-stats">
                        <p>🎯 פוטנציאל מירבי: ${campaign.potential}%</p>
                        <p>🥊 כוח יריב נוכחי: ${campaign.opponentStrength}%</p>
                        <p>📊 מצב בסקרים: <span id="campaign-${campaign.id}-poll">${campaign.currentPoll.toFixed(1)}</span>%</p>
                        <p class="budget-status" id="campaign-${campaign.id}-budget-status">
                             <span id="campaign-${campaign.id}-budget-remaining">${formatNumber(campaign.initialBudget - getTotalAllocated(campaign))}</span> ש"ח נותרו מתוך ${formatNumber(campaign.initialBudget)} ש"ח
                        </p>

                    </div>
                    <div class="allocation-controls">
                        ${Object.keys(BASE_ALLOCATION_EFFECTS).map(key => `
                            <div class="allocation-item">
                                <label for="alloc-${campaign.id}-${key}">${key.replace('_', ' ')}:</label>
                                <input type="number" id="alloc-${campaign.id}-${key}" value="${campaign.allocation[key]}" min="0" step="1000" data-campaign-id="${campaign.id}" data-allocation-key="${key}">
                            </div>
                        `).join('')}
                    </div>
                `;
                campaignsListEl.appendChild(campaignDiv);
            });

            // Add event listeners to inputs after they are created
            campaignsListEl.querySelectorAll('.allocation-controls input[type="number"]').forEach(input => {
                input.addEventListener('input', handleAllocationInput);
            });
        }

        // Handle input changes for allocation
        function handleAllocationInput(event) {
            const campaignId = parseInt(event.target.dataset.campaignId);
            const key = event.target.dataset.allocationKey;
            const value = parseInt(event.target.value) || 0;

            const campaign = campaigns.find(c => c.id === campaignId);
            if (campaign) {
                campaign.allocation[key] = value;
                // Update budget display dynamically
                updateCampaignBudgetDisplay(campaign);
            }
        }

        // Update the budget status display for a specific campaign
        function updateCampaignBudgetDisplay(campaign) {
            const remainingEl = document.getElementById(`campaign-${campaign.id}-budget-remaining`);
            const statusEl = document.getElementById(`campaign-${campaign.id}-budget-status`);
            if (!remainingEl || !statusEl) return;

            const totalAllocated = getTotalAllocated(campaign);
            const remaining = campaign.initialBudget - totalAllocated;

            remainingEl.textContent = formatNumber(remaining);

            statusEl.classList.remove('success', 'warning', 'danger'); // Clear existing classes
            if (remaining < 0) {
                statusEl.classList.add('danger');
                statusEl.title = "חרגתם מהתקציב!";
            } else if (remaining < campaign.initialBudget * 0.1) { // Less than 10% left
                 statusEl.classList.add('warning');
                 statusEl.title = "התקציב כמעט נגמר!";
            } else {
                 statusEl.classList.add('success');
                 statusEl.title = "ניהול תקציב תקין";
            }
             statusEl.textContent = `${formatNumber(remaining)} ש"ח נותרו מתוך ${formatNumber(campaign.initialBudget)} ש"ח`; // Update full text
        }

        // Calculate total allocated for a campaign
        function getTotalAllocated(campaign) {
            return Object.values(campaign.allocation).reduce((sum, amount) => sum + amount, 0);
        }

        // Simulate Election Cycle
        nextCycleBtn.addEventListener('click', () => {
            if (!gameActive) return; // Prevent playing if game is over

            logUpdate(`--- מסכמים את סבב הבחירות ${electionCycle} ---`);

            let cycleUpdates = [];
            let campaignsResults = []; // Store results to process reputation/funds later
            let totalExpenses = BASE_COMPANY_OVERHEAD;

            campaigns.forEach(campaign => {
                let totalAllocated = getTotalAllocated(campaign);
                let pollChange = 0;
                let campaignOutcome = { id: campaign.id, name: campaign.name, level: campaign.level, didWin: false, finalPoll: campaign.currentPoll, opponentStrength: campaign.opponentStrength };

                // Check if budget was exceeded
                const overBudget = totalAllocated > campaign.initialBudget;
                if (overBudget) {
                     cycleUpdates.push({ message: `🔴 הקמפיין של <strong>${campaign.name}</strong> חרג מהתקציב (${formatNumber(totalAllocated)}/${formatNumber(campaign.initialBudget)}). הדבר פוגע במוניטין החברה ומפחית את יעילות הפעולות!`, type: 'danger' });
                     companyReputation = Math.max(0, companyReputation + REPUTATION_CHANGE_OVERBUDGET); // Apply significant reputation hit immediately
                }

                // Calculate poll changes from allocation (with diminishing returns and reputation boost)
                Object.keys(campaign.allocation).forEach(key => {
                    const amount = campaign.allocation[key];
                    if (amount > 0 && key !== 'Consulting') { // Consulting effect is constant overhead, not per campaign allocation
                         // Diminishing Returns: Effect per ₪ decreases as allocation increases
                         const baseEffect = BASE_ALLOCATION_EFFECTS[key] * (1 - DIMINISHING_RETURNS_FACTOR * amount);
                         // Reputation Boost: Higher reputation makes allocations more effective
                         const reputationBoost = REPUTATION_EFFECT_MULTIPLIER * companyReputation;
                         const effectiveMultiplier = Math.max(0, baseEffect + reputationBoost); // Ensure multiplier doesn't go below zero
                         pollChange += (amount / 1000) * effectiveMultiplier; // Effect is per 1000 ש"ח
                    }
                });

                 // Add a small base effect from company reputation even without specific campaign 'Consulting' allocation
                 pollChange += (companyReputation / 100) * 1; // Small constant poll boost based on overall reputation (e.g., 1% at max rep)


                // Apply poll change, capped by potential and min poll
                let finalPoll = campaign.initialPoll + pollChange;

                // Cap at Potential (plus a small buffer maybe influenced by rep?)
                 const effectivePotential = campaign.potential + (companyReputation / 20); // High reputation slightly increases potential reach
                 finalPoll = Math.min(finalPoll, effectivePotential);

                // Minimum Poll
                 finalPoll = Math.max(finalPoll, MIN_POLL);


                campaign.currentPoll = finalPoll; // Update for display in next cycle (if campaign continues)
                campaignOutcome.finalPoll = finalPoll;


                // Determine win/loss condition: Final poll must be above opponent strength PLUS a margin, potentially influenced by reputation (e.g., high rep overcomes small deficit?)
                const winThreshold = campaign.opponentStrength + WINNING_POLL_THRESHOLD_MARGIN - (companyReputation / 50); // High reputation slightly lowers required margin
                campaignOutcome.didWin = finalPoll > winThreshold;

                campaignsResults.push(campaignOutcome); // Store result before removing campaigns

                 // Subtract expenses from company funds immediately
                 companyFunds -= totalAllocated;


                 if(overBudget) {
                     // Additional fund penalty for severe overspending? Maybe not needed, reputation hit is significant.
                 }

            }); // End of campaigns loop

            // Process results, funds, and reputation AFTER all campaigns have been evaluated
            campaignsResults.forEach(result => {
                 if (result.didWin) {
                     const bonus = result.initialBudget * INITIAL_CAMPAIGN_BONUS_MULTIPLIER;
                     companyFunds += result.initialBudget + bonus; // Company gets back invested budget + bonus for winning
                     companyReputation = Math.min(MAX_REPUTATION, companyReputation + (result.level === 'ארצי' ? REPUTATION_CHANGE_WIN_NATIONAL : REPUTATION_CHANGE_WIN_MUNICIPAL));
                     cycleUpdates.push({ message: `<span class='win'>✅ ניצחון!</span> הקמפיין של <strong>${result.name}</strong> הצליח בבחירות! (סקר סופי: ${result.finalPoll.toFixed(1)}% מול יריב: ${result.opponentStrength}%) זכינו ב- ${formatNumber(bonus)} ש"ח בונוס.`, type: 'win' });
                 } else {
                     // Funds were already subtracted
                     companyReputation = Math.max(0, companyReputation + (result.level === 'ארצי' ? REPUTATION_CHANGE_LOSE_NATIONAL : REPUTATION_CHANGE_LOSE_MUNICIPAL));
                      // Add small text showing how close they were
                     const delta = (result.finalPoll - result.opponentStrength).toFixed(1);
                     cycleUpdates.push({ message: `<span class='loss'>❌ הפסד.</span> הקמפיין של <strong>${result.name}</strong> לא עמד ביעד. (סקר סופי: ${result.finalPoll.toFixed(1)}% מול יריב: ${result.opponentStrength}%, הפרש: ${delta}%)`, type: 'loss' });
                 }
            });

             // Subtract company overhead
             companyFunds -= BASE_COMPANY_OVERHEAD;
             logUpdate({ message: `🏢 הוצאות תפעול החברה בסבב: ${formatNumber(BASE_COMPANY_OVERHEAD)} ש"ח`, type: 'info' });
              logUpdate({ message: `💰 סך כל כספים נוכחיים בחברה: <strong style="color: ${companyFunds < 0 ? var(--danger-color) : var(--primary-color)};">${formatNumber(companyFunds)}</strong> ש"ח`, type: 'info' });
             logUpdate({ message: `🌟 מוניטין החברה התעדכן ל- <strong style="color: ${companyReputation <= 30 ? var(--danger-color) : companyReputation <= 60 ? var(--warning-color) : var(--accent-color)};">${companyReputation}</strong>`, type: 'info' });


            // Filter out completed campaigns (all campaigns end after one cycle in this simplified model)
            campaigns = []; // All campaigns are replaced in the next cycle

            // Add new campaigns for the next cycle based on company reputation
            electionCycle++;
            addNewCampaigns();

            // Log updates after campaigns are processed
             cycleUpdates.forEach(update => logUpdate(update.message, update.type));

            logUpdate(`--- מתחיל סבב בחירות ${electionCycle} ---`);


            updateUI();

            // Check for game over condition
             checkGameOver();


        });

        // Function to add new campaigns
        function addNewCampaigns() {
             if (companyReputation < MIN_REPUTATION_FOR_NEW_CAMPAIGNS && electionCycle > 1) {
                 logUpdate("<span class='warning'>⚠️ מוניטין החברה נמוך מדי! קמפיינים חדשים הפסיקו להגיע.</span>", 'warning');
                 return; // Stop adding campaigns if reputation is too low
             }

             const baseCampaignsToAdd = Math.floor(companyReputation / 15); // More reputation -> more campaigns
             const numCampaignsToAdd = Math.max(2, baseCampaignsToAdd); // Always add at least 2 if reputation allows

             for(let i = 0; i < numCampaignsToAdd; i++) {
                 const id = Date.now() + i + electionCycle * 1000; // More robust unique ID
                 const isNational = Math.random() < (companyReputation / 120); // More reputation -> higher chance of national campaigns
                 const level = isNational ? "ארצי" : "מוניציפלי";
                 const baseBudget = isNational ? 150000 + Math.random() * 300000 : 20000 + Math.random() * 60000;
                 const budget = Math.max(15000, baseBudget * (1 + (companyReputation - 50) / 150)); // Budget scales with reputation
                 const potential = 45 + Math.random() * 35; // Potential 45-80
                 const opponentStrength = Math.random() * 50 + 40; // Opponent 40-90
                 // Initial poll closer to opponent, lower than potential, influenced by reputation
                 const initialPoll = Math.max(MIN_POLL, Math.min(potential - 8, opponentStrength - 5 + Math.random() * 15 + (companyReputation / 100) * 2)); // Initial poll slightly boosted by reputation
                 const name = `${level === "ארצי" ? "מפלגה ארצית " + String.fromCharCode(65 + campaigns.length + i) : "מועמד/ת עירוני/ת " + (campaigns.length + i + 1)}`;


                 campaigns.push({
                     id: id,
                     name: name,
                     level: level,
                     initialBudget: Math.round(budget),
                     potential: Math.round(potential),
                     opponentStrength: Math.round(opponentStrength),
                     initialPoll: Math.round(initialPoll),
                     currentPoll: Math.round(initialPoll), // currentPoll starts as initialPoll
                     allocation: { Surveys: 0, TV_Ads: 0, Digital_Ads: 0, Billboards: 0, Field_Work: 0, Consulting: 0 } // Reset allocation for new campaigns
                 });
                 logUpdate({ message: `✨ קמפיין חדש הצטרף! <strong>${name}</strong> (${level}) עם תקציב של ${formatNumber(Math.round(budget))} ש"ח. מצב ראשוני בסקרים: ${Math.round(initialPoll)}%.`, type: 'info' });
             }
        }

         // Check for game over conditions
        function checkGameOver() {
             if (companyFunds < GAME_OVER_FUNDS) {
                 logUpdate("<span class='danger'>💥 פשיטת רגל! כספי החברה צנחו מתחת לרף הקריטי. המשחק הסתיים!</span>", 'danger');
                 endGame("החברה פשטה רגל!");
             } else if (companyReputation <= MIN_REPUTATION_FOR_NEW_CAMPAIGNS && electionCycle > 3 && campaigns.length === 0) { // Game over if no new campaigns come for a while and rep is low
                  logUpdate("<span class='danger'>📉 מוניטין החברה נמוך מדי ולא מגיעים קמפיינים חדשים. אין עבודה. המשחק הסתיים!</span>", 'danger');
                 endGame("מוניטין החברה נמוך מדי ואין קמפיינים חדשים.");
             } else if (electionCycle > 15) { // Add a potential win condition based on cycles or achievements?
                 logUpdate("<span class='info'>🏆 ברכות! שרדתם וצמחתם במשך 15 סבבי בחירות. אתם אשפי קמפיינים פוליטיים!</span>", 'info');
                 endGame("ניצחון! הגעתם ל-15 סבבים בהצלחה.");
             }
        }

        // End the game
        function endGame(message) {
            gameActive = false;
            nextCycleBtn.disabled = true;
            nextCycleBtn.textContent = "המשחק הסתיים";
            alert(`המשחק הסתיים! ${message}`);
        }


        // Log updates to the updates panel with basic styling
        function logUpdate(message, type = 'default') {
            const p = document.createElement('p');
            p.innerHTML = message; // Use innerHTML to allow span/strong tags
            if (type) {
                 p.classList.add(type);
            }
            updatesContentEl.prepend(p); // Add to the top
             // Optional: Limit number of messages
             while(updatesContentEl.children.length > 100) { // Keep more history
                 updatesContentEl.removeChild(updatesContentEl.lastChild);
             }
             // Scroll to top to see latest message (optional, prepend makes it visible anyway)
             // updatesContentEl.scrollTop = 0;
        }

        // Format number with commas
        function formatNumber(num) {
            return Math.round(num).toLocaleString();
        }

        // Toggle explanation visibility
        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationEl.style.display === 'none';
            explanationEl.style.display = isHidden ? 'block' : 'none';
            toggleExplanationBtn.textContent = isHidden ? 'הסתר מילון מונחים ורקע תאורטי' : 'הצג/הסתר מילון מונחים ורקע תאורטי';
             // Optional: scroll to the explanation if showing it
             if (!isHidden) {
                explanationEl.scrollIntoView({ behavior: 'smooth' });
             }
        });


        // Start the game
        initializeGame();
    });
</script>