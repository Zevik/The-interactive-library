---
title: "מו\"ל העתיד: המסע אל מעבר למילים"
english_slug: publisher-of-the-future-sci-fi-publishing-management-game
category: "ניהול"
tags:
  - הוצאה לאור
  - מדע בדיוני
  - ניהול סיכונים
  - כלכלה
  - מודל עסקי
---

# מו"ל העתיד: המסע אל מעבר למילים

העתיד כבר כאן, והוא מבוסס על סיפורים. האם יש לך את מה שנדרש כדי לנווט את ספינת הדגל של ספרות המדע הבדיוני אל כוכבים חדשים? ניהול הוצאה לאור בעולם שבו רעיונות פורצי דרך מתחרים על תשומת הלב, דורש לא רק עין חדה לכישרון, אלא גם אסטרטגיה עסקית מבריקה ויכולת ניהול סיכונים יוצאת דופן. צא למסע והפוך למו"ל האגדי שהגלקסיה מייחלת לו!

<div id="game-container">
    <section id="status-panel">
        <h2>סטטוס ההוצאה</h2>
        <div class="status-grid">
            <div class="status-item">
                <span class="label">שנה:</span>
                <span id="year" class="value animated-number">1</span>
            </div>
            <div class="status-item">
                <span class="label">מזומנים:</span>
                <span id="money" class="value animated-number">₪100,000</span>
            </div>
            <div class="status-item">
                <span class="label">מוניטין גלקטי:</span>
                <span id="reputation" class="value animated-number">50</span>
            </div>
             <div class="status-item">
                <span class="label">רווח בשנה שעברה:</span>
                <span id="last-year-profit" class="value animated-number profit">₪0</span>
            </div>
        </div>
    </section>

    <section id="manuscripts-panel">
        <h2>כתבי יד מהחלל החיצון (זמינים לשנה זו)</h2>
        <div id="manuscripts-list">
            <!-- Manuscripts will be loaded here by JS -->
            <p class="loading-message">טוען אותות מכוכבים רחוקים...</p>
        </div>
    </section>

     <section id="decisions-panel">
        <h2>החלטות מכריעות לשנה הקרובה</h2>
        <div id="decision-area">
             <!-- Decision inputs will be built here by JS based on manuscript selection -->
             <p class="placeholder-text">בחר/י כתב יד מרתק כדי לגבש תוכנית פיתוח והשקה.</p>
        </div>
         <button id="next-year-btn" class="game-button primary-button" disabled>
             <span class="button-icon">🚀</span>
             עבור לשנה הבאה
         </button>
         <div id="cost-preview" class="cost-preview hidden">
             <h4>תקציר עלויות צפויות לשנה:</h4>
             <p>סה"כ פיתוח, שיווק והדפסה: <span id="total-decision-cost">₪0</span></p>
             <p>מזומנים לאחר השקעה: <span id="money-after-investment">₪0</span></p>
             <p class="warning-text hidden" id="budget-warning">אין מספיק מזומנים!</p>
         </div>
     </section>

    <section id="published-panel">
        <h2>היסטוריית פרסומים (מבט אל העבר)</h2>
        <div id="published-books-list">
            <!-- Published books will be listed here -->
            <p class="placeholder-text">עדיין לא שוגרו ספרים למדפי הגלקסיה.</p>
        </div>
    </section>


     <section id="messages-panel">
        <h2>יומן ספינה</h2>
        <div id="messages-log">
            <!-- Game messages will appear here -->
        </div>
     </section>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --warning-color: #ffc107;
        --info-color: #17a2b8;
        --background-color: #f8f9fa;
        --card-background: #ffffff;
        --border-color: #dee2e6;
        --text-color: #343a40;
        --header-color: #0056b3;
        --dark-blue: #003d7a;
    }

    body {
        font-family: 'Arial', sans-serif; /* Consider a more modern font */
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
    }

    #game-container {
        max-width: 960px; /* Slightly wider */
        margin: 20px auto;
        padding: 30px; /* More padding */
        background: linear-gradient(145deg, #e2e6ea, #ffffff); /* Subtle gradient background */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Stronger shadow */
        display: grid; /* Use grid for layout */
        grid-template-areas:
            "status status"
            "manuscripts decisions"
            "published published"
            "messages messages";
        grid-template-columns: 1fr 1fr; /* Two columns */
        gap: 30px; /* Increased gap */
    }

    #status-panel { grid-area: status; }
    #manuscripts-panel { grid-area: manuscripts; }
    #decisions-panel { grid-area: decisions; }
    #published-panel { grid-area: published; }
    #messages-panel { grid-area: messages; }


    #game-container section {
        background-color: var(--card-background);
        padding: 25px; /* More padding */
        border-radius: 8px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 8px rgba(0,0,0,0.05); /* Inner shadow for sections */
    }

    #game-container h1 {
        text-align: center;
        color: var(--header-color);
        margin-bottom: 30px;
        font-size: 2.2em; /* Larger heading */
        position: relative; /* For underline effect */
    }

     #game-container h1::after {
         content: '';
         display: block;
         width: 80px; /* Underline width */
         height: 4px;
         background: linear-gradient(to right, var(--primary-color), var(--dark-blue)); /* Gradient underline */
         margin: 10px auto 0; /* Center underline */
         border-radius: 2px;
     }


    #game-container h2 {
        color: var(--header-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        margin-top: 0; /* Remove top margin on section headers */
        margin-bottom: 20px; /* Add bottom margin */
        font-size: 1.5em;
    }

    .status-grid {
        display: flex; /* Use flexbox for status items */
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .status-item {
        text-align: center;
        margin: 10px; /* Spacing between items */
    }

    .status-item .label {
        display: block;
        font-size: 0.9em;
        color: var(--secondary-color);
        margin-bottom: 3px;
    }

    .status-item .value {
        font-size: 1.4em; /* Larger values */
        font-weight: bold;
        color: var(--dark-blue);
    }

    .animated-number {
        transition: color 0.5s ease, transform 0.3s ease; /* Smooth transitions */
    }

     .profit { color: var(--success-color) !important; } /* !important to override default */
     .loss { color: var(--danger-color) !important; }

    #manuscripts-list, #published-books-list {
        min-height: 100px; /* Ensure some height */
    }

     .loading-message, .placeholder-text {
         text-align: center;
         color: var(--secondary-color);
         font-style: italic;
         padding: 20px;
     }

    .manuscript {
        border: 1px solid var(--border-color);
        padding: 15px; /* More padding */
        margin-bottom: 15px; /* More spacing */
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
        background-color: #fdfdfd; /* Slightly off-white */
    }

    .manuscript:hover {
        background-color: #e9ecef; /* Lighter hover state */
        border-color: var(--primary-color);
        transform: translateY(-2px); /* Subtle lift effect */
    }

    .manuscript.selected {
        background-color: #e7f1ff; /* Lighter primary blue */
        border-color: var(--primary-color);
        box-shadow: 0 0 8px rgba(0, 123, 255, 0.3); /* Glow effect */
    }

    .manuscript h3 {
        margin-top: 0;
        margin-bottom: 8px; /* Spacing */
        color: var(--primary-color);
        font-size: 1.2em;
    }

    .manuscript p {
        margin: 5px 0; /* More spacing */
        font-size: 0.95em;
        color: var(--text-color);
    }

     .manuscript-meta {
         font-size: 0.85em;
         color: var(--secondary-color);
     }

    #decision-area label {
        display: block;
        margin-bottom: 15px; /* More spacing */
        font-weight: bold;
        color: var(--dark-blue);
        font-size: 1.1em;
    }

    #decision-area input[type="number"] {
        width: 150px; /* Wider input */
        padding: 8px 12px; /* More padding */
        margin-left: 15px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        font-size: 1em;
        color: var(--text-color);
        background-color: #f8f9fa;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    #decision-area input[type="number"]:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.2);
        outline: none;
    }

    .game-button {
         display: flex; /* Use flex for icon alignment */
         align-items: center;
         justify-content: center;
         width: 100%;
         padding: 12px 20px; /* More padding */
         border: none;
         border-radius: 5px; /* Slightly less rounded */
         font-size: 1.2em; /* Larger font */
         font-weight: bold;
         cursor: pointer;
         transition: background-color 0.3s ease, transform 0.1s ease;
         text-align: center;
         text-decoration: none; /* Ensure no underline if it were a link */
    }

     .game-button .button-icon {
         margin-left: 8px; /* Space between icon and text */
         font-size: 1.3em; /* Icon size */
         line-height: 1; /* Align icon vertically */
     }

    .primary-button {
        background-color: var(--success-color); /* Green for Next Year */
        color: white;
    }

    .primary-button:hover:not(:disabled) {
        background-color: #218838; /* Darker green on hover */
        transform: translateY(-1px); /* Subtle lift */
    }

    .game-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
        transform: none;
    }

    #cost-preview {
        margin-top: 20px;
        padding: 15px;
        background-color: #e9ecef; /* Light grey */
        border: 1px solid var(--border-color);
        border-radius: 5px;
        font-size: 0.95em;
        line-height: 1.8;
    }

     #cost-preview h4 {
         margin-top: 0;
         margin-bottom: 10px;
         color: var(--dark-blue);
     }

     .warning-text {
         color: var(--danger-color);
         font-weight: bold;
     }

    #messages-log {
        margin-top: 15px;
        padding: 15px;
        background-color: #fff3cd; /* Light warning yellow */
        border: 1px solid #ffeeba; /* Darker yellow border */
        border-radius: 5px;
        color: #856404; /* Dark yellow text */
        max-height: 150px; /* Limit height */
        overflow-y: auto; /* Add scrollbar */
        direction: rtl;
        text-align: right;
    }

     #messages-log p {
         margin: 5px 0;
         padding: 5px;
         border-bottom: 1px dotted #ffeeba;
         font-size: 0.9em;
     }

     #messages-log p:last-child {
         border-bottom: none;
     }

     /* Message types - add classes via JS */
     .message-info { color: #004085; background-color: #cce5ff; border-color: #b8daff; } /* Blue */
     .message-success { color: #155724; background-color: #d4edda; border-color: #c3e6cb; } /* Green */
     .message-warning { color: #856404; background-color: #fff3cd; border-color: #ffeeba; } /* Yellow */
     .message-danger { color: #721c24; background-color: #f8d7da; border-color: #f5c6cb; } /* Red */


    #published-books-list ul {
        list-style: none; /* Remove default bullets */
        padding: 0;
    }

     #published-books-list li {
        background-color: #e9ecef; /* Light background for list items */
        padding: 10px 15px;
        margin-bottom: 10px;
        border-radius: 5px;
        border: 1px solid var(--border-color);
         font-size: 0.95em;
         display: flex; /* Arrange elements inside li */
         justify-content: space-between;
         align-items: center;
         flex-wrap: wrap; /* Allow wrapping */
     }

     #published-books-list li span {
         margin-left: 15px;
     }

     #published-books-list li span:last-child {
         margin-left: 0;
         font-weight: bold;
     }


    #show-explanation-btn {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

     #show-explanation-btn:hover {
        background-color: var(--dark-blue);
         transform: translateY(-1px);
     }

    #explanation {
        margin-top: 30px;
        padding: 25px;
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        transition: all 0.5s ease-out; /* Smooth reveal */
    }

    #explanation.hidden {
        max-height: 0; /* Collapse */
        overflow: hidden;
        padding-top: 0;
        padding-bottom: 0;
        opacity: 0; /* Fade out */
        border-color: transparent;
    }

     #explanation:not(.hidden) {
         max-height: 1000px; /* Enough height to show content */
         opacity: 1;
         padding-top: 25px;
         padding-bottom: 25px;
         border-color: var(--border-color);
     }

    #explanation h2 {
         color: var(--header-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        margin-top: 0;
        margin-bottom: 20px;
         font-size: 1.5em;
    }

    #explanation p, #explanation li {
        font-size: 1em;
        line-height: 1.8;
        color: var(--text-color);
    }

    #explanation ul {
        list-style: disc;
        margin-right: 25px; /* Space for bullets */
        padding: 0;
    }

     #explanation li {
        margin-bottom: 12px;
     }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        #game-container {
            grid-template-areas:
                "status"
                "manuscripts"
                "decisions"
                "published"
                "messages";
            grid-template-columns: 1fr; /* Single column */
            gap: 20px; /* Smaller gap */
            padding: 20px;
        }

         .status-grid {
             flex-direction: column; /* Stack status items */
         }

         .status-item {
             margin: 8px 0;
         }

        #decision-area input[type="number"] {
            width: calc(100% - 120px); /* Make inputs more responsive */
            margin-left: 0;
            margin-top: 5px;
        }

         #decision-area label {
             display: flex; /* Align label and input */
             flex-direction: column;
         }

         .game-button {
             font-size: 1.1em;
             padding: 10px 15px;
         }
    }
</style>

<button id="show-explanation-btn" class="game-button secondary-button">הצג הסבר על עולם ההוצאה לאור</button>

<div id="explanation" class="hidden">
    <h2>צלילה לעומק: המנועים מאחורי הוצאת המדע הבדיוני</h2>
    <p>הבנת המכניקה של עולם ההוצאה לאור חיונית להצלחה. הנה הצצה למנועים הפועלים מאחורי הקלעים:</p>
    <ul>
        <li><strong>ארכיטקטורת רווחים והוצאות:</strong> כל ספר הוא יקום כלכלי קטן. ההוצאות כוללות: עלות בסיס (עבודה מול סופר, קריאה ראשונית), עריכה מעמיקה (לשונית ועניינית), עיצוב (כריכה, פנים), הדפסה (תלוי בכמות העותקים הראשונית) ושיווק (קידום, פרסום). ההכנסות מגיעות ממכירת עותקים, אך נתח משמעותי הולך למפיצים וחנויות. לסופרים משולמים תמלוגים כאחוז ממחיר המכירה.</li>
        <li><strong>ניווט בשוק הנישה (מדע בדיוני):</strong> קהילת המדע הבדיוני נאמנה אך ביקורתית. זיהוי טרנדים (האם סייברפאנק או אופרת חלל בשיא הפופולריות?), הבנת העדפות הקוראים והבחנה בכתבי יד עם פוטנציאל פריצה הם מפתח. התחרות אינה רק מהוצאות אחרות, אלא גם מאינספור כותבים עצמאיים ומדיות אחרות שצורכות זמן קריאה (סדרות, משחקים).</li>
        <li><strong>תהליך הפיכת רעיון לספר:</strong> כתב יד נבחר עובר מסע טרנספורמציה: עריכה קפדנית הופכת אותו למלוטש ומותאם, עיצוב הכריכה חייב למשוך את העין ולהעיד על איכותו, והעימוד הפנימי משפיע על חווית הקריאה. תקציבי העריכה והעיצוב משפיעים ישירות על איכות המוצר הסופי.</li>
        <li><strong>אמנות השיווק והפצת הספרים:</strong> גם הספר הטוב ביותר לא ימכור את עצמו. שיווק יעיל (ברשתות, בעיתונות, אירועים) יוצר מודעות ו"באז". הפצה חזקה מבטיחה שהספר יהיה זמין פיזית ואונליין כשהקורא מחפש אותו. השקעה בשיווק מגדילה את סיכויי המכירה.</li>
        <li><strong>מערכת הסיכונים:</strong> כל ספר הוא השקעה עם אי-ודאות. כתב יד 'בסיכון גבוה' יכול להיות כישלון מהדהד, או הצלחה פנומנלית שפורצת את גבולות הז'אנר. 'פוטנציאל' מתייחס לאומדן ראשוני של טווח ההצלחה האפשרי. ניהול נבון כולל פיזור סיכונים בין כתבי יד שונים.</li>
        <li><strong>בניית מוניטין גלקטי:</strong> הוצאה עם מוניטין גבוה (איכותית, מקצועית, משלמת בזמן) מושכת סופרים טובים יותר, מקבלת יחס מועדף ממפיצים וחנויות, ויוצרת בסיס קוראים נאמן שמחכה לפרסומים הבאים. הצלחות וכישלונות משפיעים על המוניטין.</li>
        <li><strong>מדדי ליבה להצלחה:</strong> מעבר לרווח הנקי (הכנסות פחות הוצאות), חשוב לעקוב אחרי: כמות המכירות לכל ספר (האם עמד בציפיות?), תזרים מזומנים (יש מספיק כסף להשקיע בספר הבא?) ומלאי (האם נתקעתם עם אלפי ספרים שלא נמכרים?).</li>
    </ul>
    <p>בהצלחה, מו"ל העתיד! גורל הספרות טמון בידיך.</p>
</div>

<script>
    const gameData = {
        year: 1,
        money: 100000,
        reputation: 50, // Out of 100
        lastYearProfit: 0,
        availableManuscripts: [],
        publishedBooks: [],
        selectedManuscriptId: null,
        decisions: {} // { manuscriptId: { editingBudget, marketingBudget, initialPrintRun, totalCost } }
    };

    const settings = {
        manuscriptsPerYear: 4, // Offer slightly more options
        baseEditingCost: 6000, // Increased base costs to feel more realistic
        baseMarketingCost: 4000,
        basePrintRunCostPerCopy: 12, // Higher print cost
        baseSalePrice: 90, // Higher sale price
        authorRoyaltyRate: 0.1, // 10% of list price
        distributorFeeRate: 0.5, // 50% of list price goes to distribution/retail
        minReputationForGoodBooks: 75, // Reputation threshold for higher chance of quality manuscripts
        qualityManuscriptChance: 0.4, // Chance of a "Good" manuscript type appearing
        excellentManuscriptChance: 0.1, // Chance of an "Excellent" manuscript type appearing (only if high reputation)
        randomEventChance: 0.3, // Increased chance of events
        startingManuscriptPool: [
            { id: 'ms1', title: 'הערים הצפות של מאדים: שקיעה אדומה', summary: 'עתיד דיסטופי על מאדים המיושב, ספר ראשון בסדרה אפשרית', risk: 'נמוך', potential: 'בינוני', baseQuality: 'בינוני', baseCost: 18000 },
            { id: 'ms2', title: 'הקודקס הסינתטי', summary: 'תעלומת סייברפאנק מורכבת בעולם וירטואלי אפלולי', risk: 'בינוני', potential: 'בינוני', baseQuality: 'בינוני', baseCost: 22000 },
            { id: 'ms3', title: 'זמנים שבורים: כרוניקה של הכאוס', summary: 'מסע בזמן פילוסופי, דורש קריאה קפדנית', risk: 'גבוה', potential: 'גבוה', baseQuality: 'גבוה', baseCost: 28000 },
            { id: 'ms4', title: 'מלחמת הגלקסיות הגדולה: ההתקפה הראשונה', summary: 'אופרת חלל קלאסית, קרבות בין-גלקטיים וחייזרים אצילים', risk: 'נמוך', potential: 'גבוה', baseQuality: 'בינוני', baseCost: 20000 },
            { id: 'ms5', title: 'העולם שמעבר לשער: חורבות אתריס', summary: 'פורטל מוביל לממד אחר מסתורי, אלמנטים של פנטזיה', risk: 'בינוני', potential: 'נמוך', baseQuality: 'נמוך', baseCost: 15000 },
             { id: 'ms6', title: 'אקו סינתטי', summary: 'מותחן ביו-פאנק על תודעות דיגיטליות וזהות', risk: 'בינוני', potential: 'בינוני', baseQuality: 'בינוני', baseCost: 19000 },
             { id: 'ms7', title: 'הילדים של סולאריס', summary: 'סיפור התבגרות על תחנת חלל נידחת', risk: 'נמוך', potential: 'נמוך', baseQuality: 'בינוני', baseCost: 16000 },
             { id: 'ms8', title: 'זיכרון הכוכבים', summary: 'אפוס רחב יריעה על עבר היסטורי-גלקטי נשכח', risk: 'גבוה', potential: 'גבוה', baseQuality: 'גבוה', baseCost: 26000 },
        ],
         riskModifiers: {
             'נמוך': { salesVariance: 0.1, reputationVariance: 0.05 }, // Lower variance
             'בינוני': { salesVariance: 0.2, reputationVariance: 0.1 },
             'גבוה': { salesVariance: 0.4, reputationVariance: 0.2 } // Higher variance
         },
         potentialModifiers: {
             'נמוך': { baseSalesFactor: 0.4, maxSalesFactor: 0.8 }, // Lower sales cap
             'בינוני': { baseSalesFactor: 0.6, maxSalesFactor: 1.2 },
             'גבוה': { baseSalesFactor: 0.8, maxSalesFactor: 1.8 } // Higher potential sales
         },
         qualityModifiers: { // Base quality impact
             'נמוך': 0.8,
             'בינוני': 1.0,
             'גבוה': 1.2
         }
    };

    // DOM Elements
    const yearSpan = document.getElementById('year');
    const moneySpan = document.getElementById('money');
    const reputationSpan = document.getElementById('reputation');
    const lastYearProfitSpan = document.getElementById('last-year-profit');
    const manuscriptsListDiv = document.getElementById('manuscripts-list');
    const publishedBooksListDiv = document.getElementById('published-books-list');
    const decisionAreaDiv = document.getElementById('decision-area');
    const nextYearBtn = document.getElementById('next-year-btn');
    const messagesLogDiv = document.getElementById('messages-log');
    const explanationDiv = document.getElementById('explanation');
    const showExplanationBtn = document.getElementById('show-explanation-btn');
    const costPreviewDiv = document.getElementById('cost-preview');
    const totalDecisionCostSpan = document.getElementById('total-decision-cost');
    const moneyAfterInvestmentSpan = document.getElementById('money-after-investment');
    const budgetWarningSpan = document.getElementById('budget-warning');


    // Helper Functions
    function formatCurrency(amount) {
        return `₪${amount.toLocaleString('he-IL')}`; // Use Hebrew locale for formatting
    }

    function updateStatusDisplay() {
        // Animate number changes
        animateNumberChange(yearSpan, gameData.year);
        animateNumberChange(moneySpan, gameData.money, formatCurrency);
        animateNumberChange(reputationSpan, gameData.reputation);
        animateNumberChange(lastYearProfitSpan, gameData.lastYearProfit, formatCurrency);

         // Update color for profit/loss
         if (gameData.lastYearProfit >= 0) {
             lastYearProfitSpan.classList.remove('loss');
             lastYearProfitSpan.classList.add('profit');
         } else {
              lastYearProfitSpan.classList.remove('profit');
             lastYearProfitSpan.classList.add('loss');
         }
    }

    function animateNumberChange(element, newValue, formatter = (val) => val) {
        const startValue = parseFloat(element.textContent.replace(/[^0-9.-]/g, '')) || 0;
        const duration = 800; // milliseconds
        const startTime = performance.now();

        function update(currentTime) {
            const elapsedTime = currentTime - startTime;
            const progress = Math.min(elapsedTime / duration, 1);
            const currentValue = startValue + (newValue - startValue) * progress;

            element.textContent = formatter(Math.round(currentValue));

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                element.textContent = formatter(newValue); // Ensure final value is exact
            }
        }

        requestAnimationFrame(update);
    }


     function addMessage(text, type = 'info') {
        const msgElement = document.createElement('p');
        msgElement.textContent = text;
        msgElement.classList.add(`message-${type}`); // Add class for styling
        messagesLogDiv.appendChild(msgElement);
        messagesLogDiv.scrollTop = messagesLogDiv.scrollHeight; // Scroll to bottom
        // Optional: Add animation for new message
         msgElement.style.opacity = 0;
         msgElement.style.transform = 'translateY(10px)';
         setTimeout(() => {
             msgElement.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
             msgElement.style.opacity = 1;
             msgElement.style.transform = 'translateY(0)';
         }, 10); // Small delay to allow transition to work
     }

     function clearMessages() {
        messagesLogDiv.innerHTML = '';
     }

    function generateManuscripts() {
        gameData.availableManuscripts = [];
        const poolCopy = [...settings.startingManuscriptPool];
        const numToGenerate = Math.min(settings.manuscriptsPerYear, poolCopy.length);

        for (let i = 0; i < numToGenerate; i++) {
            const randomIndex = Math.floor(Math.random() * poolCopy.length);
            const selectedMs = poolCopy.splice(randomIndex, 1)[0];

            // Add potential quality variation based on reputation
            let finalQuality = selectedMs.baseQuality;
             if (gameData.reputation >= settings.minReputationForGoodBooks) {
                 if (Math.random() < settings.excellentManuscriptChance) {
                      finalQuality = 'גבוה';
                 } else if (Math.random() < settings.qualityManuscriptChance) {
                     if (finalQuality === 'נמוך') finalQuality = 'בינוני';
                     else if (finalQuality === 'בינוני') finalQuality = 'גבוה';
                 }
             } else {
                 // Small chance of lower quality if reputation is low
                  if (Math.random() < (1 - gameData.reputation / 100) * 0.2) {
                      if (finalQuality === 'גבוה') finalQuality = 'בינוני';
                      else if (finalQuality === 'בינוני') finalQuality = 'נמוך';
                  }
             }


            gameData.availableManuscripts.push({...selectedMs, finalQuality: finalQuality}); // Add a copy with potentially adjusted quality
        }
         addMessage(`אותות התקבלו: ${gameData.availableManuscripts.length} כתבי יד חדשים נחתו על שולחנך.`, 'info');
    }

    function getQualityDescription(quality) {
        switch(quality) {
            case 'נמוך': return 'איכות בסיסית';
            case 'בינוני': return 'איכות סבירה';
            case 'גבוה': return 'פוטנציאל איכות גבוה';
            default: return 'איכות לא ידועה';
        }
    }

    function renderManuscripts() {
         if (gameData.availableManuscripts.length === 0) {
              manuscriptsListDiv.innerHTML = '<p class="placeholder-text">אין כתבי יד חדשים זמינים כרגע.</p>';
              return;
         }

        manuscriptsListDiv.innerHTML = gameData.availableManuscripts.map(ms => `
            <div class="manuscript" data-id="${ms.id}">
                <h3>${ms.title}</h3>
                <p>${ms.summary}</p>
                <p class="manuscript-meta">
                    סיכון: ${ms.risk} | פוטנציאל שוק: ${ms.potential} | פוטנציאל איכות: ${getQualityDescription(ms.finalQuality)} |
                    עלות בסיס פיתוח: ${formatCurrency(ms.baseCost)}
                 </p>
            </div>
        `).join('');

         document.querySelectorAll('.manuscript').forEach(el => {
            el.addEventListener('click', handleManuscriptSelection);
         });
    }

    function handleManuscriptSelection(event) {
        const selectedElement = event.currentTarget;
        const msId = selectedElement.dataset.id;

        // Deselect previous
        if (gameData.selectedManuscriptId) {
            const prevSelected = manuscriptsListDiv.querySelector(`.manuscript[data-id="${gameData.selectedManuscriptId}"]`);
            if (prevSelected) prevSelected.classList.remove('selected');
        }

        // Select new
        gameData.selectedManuscriptId = msId;
        selectedElement.classList.add('selected');

        // Render decision area for the selected manuscript
        renderDecisionArea(msId);
        checkBudget(); // Update cost preview
    }

    function renderDecisionArea(msId) {
        const ms = gameData.availableManuscripts.find(m => m.id === msId);
        if (!ms) {
             decisionAreaDiv.innerHTML = '<p class="placeholder-text">בחר/י כתב יד מרתק כדי לגבש תוכנית פיתוח והשקה.</p>';
             costPreviewDiv.classList.add('hidden');
             nextYearBtn.disabled = true;
             return;
        }

        // Initialize decisions if not exist or load existing
        if (!gameData.decisions[msId]) {
             gameData.decisions[msId] = {
                 editingBudget: settings.baseEditingCost,
                 marketingBudget: settings.baseMarketingCost,
                 initialPrintRun: 500 // Default print run
             };
        }

        const currentDecision = gameData.decisions[msId];

        decisionAreaDiv.innerHTML = `
            <h3>תוכנית השקה עבור "${ms.title}"</h3>
            <p>עלות בסיס פיתוח (עבודה מול סופר, קריאה ראשונית): ${formatCurrency(ms.baseCost)}</p>
            <label for="editing-${msId}">
                תקציב עריכה ופיתוח תוכן (${formatCurrency(settings.baseEditingCost)}+):
                <input type="number" id="editing-${msId}" min="${settings.baseEditingCost}" step="500" value="${currentDecision.editingBudget}">
            </label>
            <label for="marketing-${msId}">
                 תקציב שיווק ופרסום (${formatCurrency(settings.baseMarketingCost)}+):
                 <input type="number" id="marketing-${msId}" min="${settings.baseMarketingCost}" step="500" value="${currentDecision.marketingBudget}">
            </label>
            <label for="printrun-${msId}">
                 מהדורה ראשונה (עותקים, מינימום 100):
                 <input type="number" id="printrun-${msId}" min="100" step="100" value="${currentDecision.initialPrintRun}">
            </label>
        `;

         // Add event listeners to update decisions object and budget preview as user types
         document.getElementById(`editing-${msId}`).addEventListener('input', (e) => {
             gameData.decisions[msId].editingBudget = parseInt(e.target.value) || settings.baseEditingCost;
             checkBudget();
         });
          document.getElementById(`marketing-${msId}`).addEventListener('input', (e) => {
             gameData.decisions[msId].marketingBudget = parseInt(e.target.value) || settings.baseMarketingCost;
              checkBudget();
         });
           document.getElementById(`printrun-${msId}`).addEventListener('input', (e) => {
             gameData.decisions[msId].initialPrintRun = parseInt(e.target.value) || 100;
              checkBudget();
         });

         costPreviewDiv.classList.remove('hidden');
         checkBudget(); // Check budget initially
    }

    function calculateTotalDecisionCost() {
        let totalCost = 0;
        const selectedMsId = gameData.selectedManuscriptId;
        if (selectedMsId && gameData.decisions[selectedMsId]) {
            const ms = gameData.availableManuscripts.find(m => m.id === selectedMsId);
            const decision = gameData.decisions[selectedMsId];
            if (ms && decision) {
                 const printCost = decision.initialPrintRun * settings.basePrintRunCostPerCopy;
                 totalCost = ms.baseCost + decision.editingBudget + decision.marketingBudget + printCost;
                 gameData.decisions[selectedMsId].totalCost = totalCost; // Store calculated cost
            }
        }
        return totalCost;
    }

    function checkBudget() {
        const totalCost = calculateTotalDecisionCost();
        const moneyLeft = gameData.money - totalCost;

        totalDecisionCostSpan.textContent = formatCurrency(totalCost);
        moneyAfterInvestmentSpan.textContent = formatCurrency(moneyLeft);

        if (moneyLeft < 0) {
             nextYearBtn.disabled = true;
             budgetWarningSpan.classList.remove('hidden');
             moneyAfterInvestmentSpan.classList.add('loss'); // Indicate negative money
        } else if (!gameData.selectedManuscriptId) {
            nextYearBtn.disabled = true;
             budgetWarningSpan.classList.add('hidden');
             moneyAfterInvestmentSpan.classList.remove('loss');
        }
        else {
            nextYearBtn.disabled = false;
             budgetWarningSpan.classList.add('hidden');
             moneyAfterInvestmentSpan.classList.remove('loss');
        }
    }


    function simulateYear() {
        clearMessages();
        addMessage(`שנה ${gameData.year} מתחילה: מנועים הופעלו...`, 'info');

        let totalProfitThisYear = 0;
        const booksPublishedThisYear = [];

        // Process selected manuscript from last year's decision
        const selectedMsId = gameData.selectedManuscriptId;
        const decision = gameData.decisions[selectedMsId];

        if (selectedMsId && decision) {
            const ms = gameData.availableManuscripts.find(m => m.id === selectedMsId); // Use available list to get adjusted quality
            if (ms) {
                addMessage(`משגרים ספר חדש: "${ms.title}" אל השוק!`, 'info');

                const totalProductionCost = decision.totalCost; // Use pre-calculated cost

                gameData.money -= totalProductionCost; // Deduct costs upfront
                 addMessage(`עלויות פיתוח, עיצוב, הדפסה ושיווק: -${formatCurrency(totalProductionCost)}. קופת ההוצאה: ${formatCurrency(gameData.money)}`, 'info');


                // --- Simulation Logic ---
                // Factors influencing sales: Base Potential, Manuscript Quality, Editing Budget, Marketing Budget, Reputation, Randomness (Risk), Print Run
                const potentialSalesFactor = settings.potentialModifiers[ms.potential].baseSalesFactor;
                const qualityModifier = settings.qualityModifiers[ms.finalQuality];

                // Influence of editing/marketing budget (diminishing returns)
                // Extra budget divided by base budget gives a ratio. Apply a sqrt or log for diminishing returns, or a simple capped multiplier.
                // Let's use a simple diminishing return: bonus = log(extra_budget / base + 1) * factor
                const editingBonus = Math.log((decision.editingBudget - settings.baseEditingCost) / settings.baseEditingCost + 1) * 0.5; // Example: doubling budget (ratio 1) -> log(2)*0.5 ~= 0.35 sales bonus
                const marketingBonus = Math.log((decision.marketingBudget - settings.baseMarketingCost) / settings.baseMarketingCost + 1) * 0.5;

                // Reputation influence on sales
                const reputationSalesBonus = (gameData.reputation - 50) / 100 * 0.5; // -0.25 to +0.25 multiplier

                let baseExpectedSalesRatio = potentialSalesFactor * qualityModifier * (1 + editingBonus) * (1 + marketingBonus) * (1 + reputationSalesBonus);

                // Apply randomness based on risk
                 const riskVariance = settings.riskModifiers[ms.risk].salesVariance;
                 const randomSalesFactor = 1 + (Math.random() * 2 - 1) * riskVariance; // Random factor between (1-variance) and (1+variance)

                 let actualSales = Math.round(decision.initialPrintRun * baseExpectedSalesRatio * randomSalesFactor);

                 // Cap sales at print run and potential maximum defined by potential modifier
                 const maxSalesBasedOnPotential = decision.initialPrintRun * settings.potentialModifiers[ms.potential].maxSalesFactor;
                 actualSales = Math.min(actualSales, decision.initialPrintRun, Math.round(maxSalesBasedOnPotential));
                 actualSales = Math.max(0, actualSales); // Ensure non-negative sales


                 // --- Calculate Revenue and Profit ---
                 const grossRevenuePerBook = settings.baseSalePrice;
                 const netRevenuePerBook = grossRevenuePerBook * (1 - settings.distributorFeeRate); // Revenue received by publisher
                 const royaltyPerBook = grossRevenuePerBook * settings.authorRoyaltyRate; // Royalty paid to author (calculated on list price)

                 // Profit per book sold = (Net Revenue per Book) - (Royalty per Book) - (Print Cost allocated per sold book)
                 // To allocate print cost per sold book: total print cost / initial print run
                 const allocatedPrintCostPerBook = (decision.initialPrintRun > 0) ? (decision.initialPrintRun * settings.basePrintRunCostPerCopy) / decision.initialPrintRun : 0;

                 const profitPerBookSold = netRevenuePerBook - royaltyPerBook - allocatedPrintCostPerBook; // This seems more accurate for profit calculation

                 const totalRevenueFromSales = actualSales * (netRevenuePerBook - royaltyPerBook);
                 const bookProfit = totalRevenueFromSales - (ms.baseCost + decision.editingBudget + decision.marketingBudget); // Profit = Revenue from Sales - Other Production Costs (Print cost already factored into allocatedPrintCostPerBook)

                 gameData.money += totalRevenueFromSales; // Add net revenue from sales (after distributor & author)
                 totalProfitThisYear += bookProfit;


                 // --- Update reputation ---
                 // Reputation change based on sales performance relative to expectations AND profit
                 const expectedSales = decision.initialPrintRun * baseExpectedSalesRatio;
                 let salesPerformanceFactor = (actualSales / expectedSales) || 0; // Ratio of actual to expected sales. Handle division by zero.

                 let reputationChange = (salesPerformanceFactor - 1) * 10; // Example: selling double expected -> +10 rep, selling half -> -5 rep
                 reputationChange += (bookProfit / 75000); // Small boost/penalty based on absolute profit (75k threshold)

                 // Add randomness to reputation change based on risk
                 const reputationVariance = settings.riskModifiers[ms.risk].reputationVariance;
                 reputationChange += (Math.random() * 2 - 1) * (reputationVariance * 10); // Random change based on risk

                 gameData.reputation = Math.max(1, Math.min(100, Math.round(gameData.reputation + reputationChange)));
                 addMessage(`המוניטין הגלקטי השתנה ב-${Math.round(reputationChange)}. מוניטין נוכחי: ${gameData.reputation}`, reputationChange >= 0 ? 'success' : 'danger');


                 booksPublishedThisYear.push({
                    id: ms.id,
                    title: ms.title,
                    yearPublished: gameData.year,
                    initialPrintRun: decision.initialPrintRun,
                    actualSales: actualSales,
                    profit: bookProfit,
                    status: 'פורסם'
                 });

                addMessage(`דוח מכירות: "${ms.title}" - נמכרו ${actualSales} עותקים מתוך מהדורה של ${decision.initialPrintRun}. רווח/הפסד נקי מהספר: ${formatCurrency(bookProfit)}.`, bookProfit >= 0 ? 'success' : 'danger');


             } else {
                  addMessage('שגיאת מנוע: לא נמצא כתב יד עבור ההחלטה שנבחרה.', 'danger');
             }
        } else {
             addMessage('שום ספר לא נבחר לפיתוח והשקה השנה. עלויות תפעול מינימליות נגרמו.', 'warning');
             // Apply a small cost for operating the publishing house
             const operatingCost = 5000;
             gameData.money -= operatingCost;
             totalProfitThisYear -= operatingCost;
              addMessage(`עלויות תפעול: -${formatCurrency(operatingCost)}. קופת ההוצאה: ${formatCurrency(gameData.money)}`, 'warning');
        }

        // Add published books to the main list
        gameData.publishedBooks = gameData.publishedBooks.concat(booksPublishedThisYear);


        // --- Random Events ---
         if (Math.random() < settings.randomEventChance) {
             const events = [
                 { text: "כתבת מגזין יוקרתית המליצה על ההוצאה שלכם! בונוס מוניטין.", effect: () => gameData.reputation = Math.min(100, gameData.reputation + 8), type: 'success' },
                 { text: "סופר ותיק עזב להוצאה מתחרה. פגיעה במוניטין.", effect: () => gameData.reputation = Math.max(1, gameData.reputation - 6), type: 'danger' },
                 { text: "בעיות בבית הדפוס עיכבו את הפצת כל הספרים החדשים. הפסד כספי.", effect: () => gameData.money -= 7000, type: 'danger' },
                 { text: "פסטיבל מדע בדיוני מקומי יצר באז גדול! הגדלה זמנית במכירות הספרים הקיימים.", effect: () => { addMessage("גלי המכירה של הספרים הקיימים גדלו זמנית."); /* No direct money effect here to keep it simple */ }, type: 'info' },
                 { text: "טרנד חדש בז'אנר פגע במכירות הספרים הקיימים שלא קשורים אליו.", effect: () => { addMessage("הספרים הקיימים הושפעו לרעה משינויים בשוק."); /* No direct money effect here to keep it simple */ }, type: 'warning' },
                 { text: "השקעה קטנה בשיפור מערכת ההפצה השתלמה.", effect: () => gameData.money += 5000, type: 'success' },
             ];
             const randomEvent = events[Math.floor(Math.random() * events.length)];
             addMessage(`אירוע קוסמי: ${randomEvent.text}`, randomEvent.type);
             randomEvent.effect();
         }


        // End of year summary & reset
        gameData.lastYearProfit = totalProfitThisYear;
        gameData.year++;
        gameData.selectedManuscriptId = null; // Reset selection
        gameData.decisions = {}; // Reset decisions for next year

        updateStatusDisplay();
        renderPublishedBooks();
        generateManuscripts(); // Generate new manuscripts for the new year
        renderManuscripts();
        renderDecisionArea(null); // Clear decision area
         checkBudget(); // Re-check budget state (should be disabled initially)
        addMessage(`ברוכים הבאים לשנה ${gameData.year}. אותות חדשים הגיעו.`, 'info');
    }

    function renderPublishedBooks() {
        if (gameData.publishedBooks.length === 0) {
            publishedBooksListDiv.innerHTML = '<p class="placeholder-text">עדיין לא שוגרו ספרים למדפי הגלקסיה.</p>';
            return;
        }

        publishedBooksListDiv.innerHTML = '<ul>' + gameData.publishedBooks.map(book => `
            <li>
                <span>"${book.title}" (${book.yearPublished})</span>
                 <span>מהדורה: ${book.initialPrintRun}</span>
                 <span>נמכרו: ${book.actualSales}</span>
                 <span>רווח/הפסד: <span class="${book.profit >= 0 ? 'profit' : 'loss'}">${formatCurrency(book.profit)}</span></span>
            </li>
        `).join('') + '</ul>';
    }


    // Event Listeners
    nextYearBtn.addEventListener('click', simulateYear);

    showExplanationBtn.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        const isHidden = explanationDiv.classList.contains('hidden');
        showExplanationBtn.textContent = isHidden ? 'הצג הסבר על עולם ההוצאה לאור' : 'הסתר הסבר';
        showExplanationBtn.classList.toggle('primary-button', !isHidden);
        showExplanationBtn.classList.toggle('secondary-button', isHidden);
    });

    // Initial Setup
    function initGame() {
        updateStatusDisplay();
        generateManuscripts();
        renderManuscripts();
        renderPublishedBooks();
        renderDecisionArea(null);
         checkBudget(); // Check initial state
         addMessage('ברוכים הבאים למשחק "מו"ל העתיד: המסע אל מעבר למילים"! בחר/י כתב יד וקצה/י תקציבים לשנה הראשונה.', 'success');
         addMessage('מטרת המשחק: להגדיל את המזומנים והמוניטין של ההוצאה שלך לאורך שנים.', 'info');
    }

    initGame(); // Start the game

</script>