---
title: "שוק הסחורות: זירת מסחר גלובלית"
english_slug: commodity-market-global-trading
category: "כלכלה"
tags:
  - סחורות
  - בורסה
  - שווקים פיננסיים
  - היצע וביקוש
  - השקעות
---
# שוק הסחורות: זירת מסחר גלובלית
האם תמיד רצית להבין איך אירועים בקצה השני של העולם משפיעים על מחירי מוצרי יסוד? נפט עולה, חיטה נופלת, זהב מזנק? שוק הסחורות הוא המקום שבו נקבעים המחירים של חומרי הגלם המניעים את הכלכלה העולמית. היכנסו לסימולטור, שחקו אותה משקיעים והרגישו את הדופק של השוק בזמן אמת!

<div id="app-container">
    <div class="header">
        <h1>סימולטור סוחר הסחורות</h1>
        <div class="stats">
            <div class="stat-item">
                <span class="stat-label">יום מסחר:</span>
                <span id="current-step" class="stat-value">0</span> / <span id="total-steps" class="stat-value"></span>
            </div>
            <div class="stat-item">
                 <span class="stat-label">מזומן זמין:</span>
                 <span id="cash" class="stat-value">$</span>
             </div>
            <div class="stat-item">
                <span class="stat-label">שווי פורטפוליו:</span>
                <span id="portfolio-value" class="stat-value">$</span>
             </div>
        </div>
    </div>

    <div class="events-section">
        <h3><i class="fas fa-globe-americas"></i> חדשות מהשווקים:</h3>
        <div id="event-display" class="event-text">ברוכים הבאים לזירת הסחר הגלובלית! עקבו אחר החדשות ובצעו מהלכים אסטרטגיים.</div>
    </div>

    <div class="commodities-section">
        <h3><i class="fas fa-chart-line"></i> סחורות נסחרות:</h3>
        <div id="commodities-list">
            <!-- Commodity cards will be populated here by JS -->
        </div>
    </div>

    <button id="next-step-btn" class="action-button primary">יום מסחר הבא <i class="fas fa-arrow-right"></i></button>
    <button id="reset-btn" class="action-button secondary" style="display: none;"><i class="fas fa-redo"></i> התחל סימולציה מחדש</button>

    <div class="portfolio-section">
        <h3><i class="fas fa-wallet"></i> הפורטפוליו שלך:</h3>
        <div id="portfolio-display">
            <!-- Portfolio holdings will be displayed here -->
             <p class="empty-portfolio">הפורטפוליו ריק. בצעו קנייה ראשונה!</p>
        </div>
    </div>
</div>

<style>
    /* Global Styles */
    #app-container {
        direction: rtl;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
        max-width: 900px;
        margin: 20px auto;
        padding: 30px; /* More padding */
        border: none; /* Remove border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #ffffff, #f0f2f5); /* Subtle gradient */
        box-shadow: 0 8px 16px rgba(0,0,0,0.1); /* Stronger shadow */
        color: #333;
    }

    /* Header & Stats */
    .header h1 {
        text-align: center;
        color: #0056b3; /* Brand color */
        margin-bottom: 25px;
        font-size: 2em;
    }

    .stats {
        display: flex;
        justify-content: space-around;
        margin-bottom: 30px;
        padding: 15px;
        background-color: #e9ecef; /* Light background */
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.08);
        flex-wrap: wrap; /* Allow wrapping on small screens */
        gap: 15px; /* Space between stat items */
    }

    .stat-item {
        text-align: center;
        min-width: 150px; /* Give items space */
    }

    .stat-label {
        display: block;
        font-size: 0.9em;
        color: #555;
        margin-bottom: 3px;
    }

    .stat-value {
        font-size: 1.4em;
        font-weight: bold;
        color: #007bff; /* Highlight color */
    }

    /* Events Section */
    .events-section {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid #ffeeba; /* Warm border */
        background-color: #fff3cd; /* Warm background */
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }

    .events-section h3 {
        margin-top: 0;
        color: #856404; /* Dark yellow color */
        font-size: 1.3em;
        display: flex;
        align-items: center;
    }
    .events-section h3 i {
        margin-left: 10px; /* Space for icon */
        color: #856404;
    }

    .event-text {
        font-style: italic;
        color: #6a040f; /* Dark red */
        line-height: 1.6;
        font-size: 1.1em;
        animation: fadeIn 1s ease-out; /* Fade in animation */
    }

    /* Commodities Section */
    .commodities-section h3 {
         margin-top: 30px;
         margin-bottom: 20px;
         color: #28a745; /* Green color */
         border-bottom: 2px solid #28a745;
         padding-bottom: 8px;
         font-size: 1.4em;
         display: flex;
         align-items: center;
    }
     .commodities-section h3 i {
        margin-left: 10px; /* Space for icon */
        color: #28a745;
    }


    #commodities-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Slightly wider cards */
        gap: 25px; /* More space between cards */
    }

    .commodity-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px; /* More rounded */
        padding: 20px; /* More padding */
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08); /* Stronger shadow */
        display: flex;
        flex-direction: column;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out; /* Add transitions */
    }

    .commodity-card:hover {
        transform: translateY(-5px); /* Subtle lift on hover */
        box-shadow: 0 6px 12px rgba(0,0,0,0.12);
    }

    .commodity-card h4 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #007bff; /* Primary color */
        font-size: 1.3em;
    }

    .commodity-price {
        font-size: 1.5em; /* Larger price font */
        font-weight: bold;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
    }

    .price-change {
        font-size: 1em; /* Slightly larger change font */
        margin-right: 8px; /* Space */
        font-weight: normal;
        transition: color 0.3s ease; /* Smooth color change */
    }

    .price-up {
        color: #28a745; /* Green */
    }

    .price-down {
        color: #dc3545; /* Red */
    }

    .price-flash-up {
        animation: priceFlashUp 0.5s ease-out; /* Animation for price increase */
    }

     .price-flash-down {
        animation: priceFlashDown 0.5s ease-out; /* Animation for price decrease */
    }


    .trade-controls {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-top: auto; /* Push controls to the bottom */
        padding-top: 20px; /* Add more space */
        border-top: 1px solid #eee;
    }

    .trade-controls input[type="number"] {
        width: 70px; /* Wider input */
        padding: 8px; /* More padding */
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1em;
        text-align: center;
    }

    .trade-controls button {
        padding: 8px 15px; /* More padding */
        border: none;
        border-radius: 5px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease; /* Add transitions */
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .trade-controls button:active {
        transform: scale(0.98); /* Subtle press effect */
    }


    .trade-controls .buy-btn {
        background-color: #28a745; /* Green */
        color: white;
    }

    .trade-controls .buy-btn:hover {
         background-color: #218838; /* Darker green */
    }

     .trade-controls .sell-btn {
        background-color: #dc3545; /* Red */
        color: white;
    }

    .trade-controls .sell-btn:hover {
        background-color: #c82333; /* Darker red */
    }

    /* Action Buttons */
    .action-button {
        display: block;
        width: 100%;
        padding: 12px; /* More padding */
        margin-top: 25px; /* More margin top */
        font-size: 1.3em; /* Larger font */
        border: none;
        border-radius: 8px; /* More rounded */
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
         display: flex; /* Align icon */
         justify-content: center;
         align-items: center;
    }

    .action-button i {
        margin-left: 10px; /* Space for icon */
    }

    .primary {
        background-color: #007bff; /* Blue */
        color: white;
    }

    .primary:hover {
        background-color: #0056b3; /* Darker blue */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

     .secondary {
        background-color: #6c757d; /* Gray */
        color: white;
     }

    .secondary:hover {
        background-color: #5a6268; /* Darker gray */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }


    /* Portfolio Section */
    .portfolio-section h3 {
         margin-top: 30px;
         margin-bottom: 15px;
         color: #ffc107; /* Yellow */
         border-bottom: 2px solid #ffc107;
         padding-bottom: 8px;
         font-size: 1.4em;
         display: flex;
         align-items: center;
    }

    .portfolio-section h3 i {
        margin-left: 10px; /* Space for icon */
        color: #ffc107;
    }

    #portfolio-display {
        background-color: #e9ecef;
        padding: 15px;
        border-radius: 8px;
        min-height: 50px; /* Ensure space even if empty */
    }

    .portfolio-item {
        display: flex;
        justify-content: space-between;
        border-bottom: 1px solid #dee2e6;
        padding-bottom: 8px;
        margin-bottom: 8px;
        font-size: 1.1em;
    }

    .portfolio-item:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
    }

    .empty-portfolio {
        text-align: center;
        color: #777;
        font-style: italic;
        margin: 10px 0;
    }


    /* Explanation Section */
    #show-explanation-btn {
        display: block;
        width: 100%;
        padding: 12px;
        margin-top: 40px; /* More margin */
        font-size: 1.1em;
        background-color: #17a2b8; /* Teal */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #show-explanation-btn:hover {
        background-color: #138496; /* Darker teal */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    #explanation {
        margin-top: 30px; /* More margin */
        padding: 25px; /* More padding */
        border: none; /* Remove border */
        border-radius: 10px; /* More rounded */
        background-color: #e9ecef; /* Light background */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        line-height: 1.7; /* Better readability */
    }

    #explanation.hidden {
        display: none;
    }

    #explanation h2 {
        margin-top: 0;
        color: #0056b3; /* Brand color */
        border-bottom: 2px solid #ffc107; /* Yellow accent */
        padding-bottom: 8px;
        margin-bottom: 20px;
        font-size: 1.6em;
    }

     #explanation h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: #333;
        font-size: 1.3em;
    }


    #explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* More space for RTL list */
        padding-right: 0;
    }

    #explanation li {
        margin-bottom: 12px; /* More space between list items */
        line-height: 1.6;
    }

    #explanation li strong {
        color: #555;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes priceFlashUp {
        0% { background-color: #d4edda; } /* Light green */
        50% { background-color: transparent; }
        100% { background-color: transparent; }
    }

     @keyframes priceFlashDown {
        0% { background-color: #f8d7da; } /* Light red */
        50% { background-color: transparent; }
        100% { background-color: transparent; }
    }

     /* FontAwesome Icons (requires a link to the library in the head of the HTML page) */
     /* Assuming this is provided by the platform */
    .fas {
        font-family: "Font Awesome 5 Free";
        font-weight: 900;
    }


</style>

<button id="show-explanation-btn">מהו שוק הסחורות? לחץ להרחבה</button>

<div id="explanation" class="hidden">
    <h2>שוק הסחורות: זירת סחר גלובלית ומורכבת</h2>
    <p>דמיינו שוק ענק, גלובלי, שבו לא נסחרות טלוויזיות או מכוניות, אלא חומרי הגלם שמהם מייצרים אותן – נפט, חיטה, זהב, סוכר ועוד. זהו שוק הסחורות. הוא משפיע על מחיר הדלק שאתם מתדלקים, הלחם שאתם אוכלים ואפילו הטלפון שבו אתם משתמשים.</p>
    <p>הבנת שוק הסחורות חיונית להבנת הכלכלה העולמית. כאן, כוחות ההיצע והביקוש נפגשים, ומושפעים מאינספור גורמים – החל ממזג אוויר קיצוני וכלה במלחמות ומשברים פוליטיים. בואו נצלול לעומק:</p>
    <h3>עמודי התווך של שוק הסחורות:</h3>
    <ul>
        <li><strong>מה זה בדיוק?</strong>
            שוק עולמי שבו סוחרים ב"דברים אמיתיים" – חומרי גלם בסיסיים. המסחר נעשה לרוב באמצעות חוזים עתידיים, שמאפשרים לקבוע מחיר לעסקה שתתרחש בעתיד. זה כלי חיוני ליצרנים (להבטיח מחיר למכירה) ולצרכנים גדולים (להבטיח מחיר לקנייה), וגם זירה למשקיעים ספקולטיביים שמנסים להרוויח מתנודות מחירים.</li>
        <li><strong>השחקנים המרכזיים:</strong>
            שוק הסחורות מחולק לקטגוריות עיקריות:
            <ul>
                <li>**אנרגיה (נפט, גז):** הדלק של הכלכלה המודרנית. מלחמות, הסכמי תפוקה, תגליות חדשות או פיתוח אנרגיות חלופיות משפיעים עמוקות.</li>
                <li>**חקלאות (חיטה, תירס, קפה, סוכר, בקר):** המזון שלנו. מזג אוויר, מחלות, התקדמות טכנולוגית בחקלאות או שינויים בהרגלי אכילה קובעים את המחיר.</li>
                <li>**מתכות (זהב, כסף, נחושת, ברזל):** אבני הבניין של התעשייה וגם נכסי מקלט (זהב). צמיחה כלכלית (ביקוש לנחושת/ברזל), אינפלציה ואי-ודאות גלובלית (ביקוש לזהב) הם גורמים מרכזיים.</li>
            </ul>
            המחירים של סחורות אלו משפיעים באופן ישיר על עלות ייצור של מגוון עצום של מוצרים, ולכן גם על יוקר המחיה.</li>
        <li><strong>ריקוד ההיצע והביקוש:</strong>
            זה הלב הפועם של השוק. אם יש פחות סחורה (היצע נמוך) ורבים רוצים לקנות אותה (ביקוש גבוה) - המחיר יעלה. ולהפך. סימולטור זה מדגים כיצד אירועים שונים משפיעים על הכוחות הללו.</li>
        <li><strong>גורמים סודיים (פחות):</strong>
            על **ההיצע** משפיעים: אסונות טבע (בצורת, שיטפונות), בעיות ייצור (תקלות טכניות, שביתות), סכסוכים פוליטיים באזורי ייצור, ועלויות הובלה.
            על **הביקוש** משפיעים: קצב הצמיחה הכלכלית בעולם (כשכלכלות גדלות, צריך יותר חומרי גלם), שינויים דמוגרפיים, טכנולוגיות חדשות שמשנות צריכה (רכבים חשמליים מפחיתים ביקוש לנפט), ומדיניות ממשלות.</li>
        <li><strong>אירועים, מחירים, ומה שביניהם:</strong>
            דוגמאות מהחיים שמודל ההיצע והביקוש מסביר:
            <ul>
                <li>מלחמה במזרח התיכון פוגעת באספקת נפט = היצע נמוך = מחיר נפט עולה.</li>
                <li>יבול חיטה ענק עקב מזג אוויר מושלם = היצע גבוה = מחיר חיטה יורד.</li>
                <li>משבר פיננסי גלובלי גורם למשקיעים לחפש מקלט = ביקוש לזהב עולה = מחיר זהב עולה.</li>
            </ul>
        </li>
        <li><strong>למה זה חשוב לנו?</strong>
            מעבר להיותו זירת רווח והפסד למשקיעים, שוק הסחורות הוא ברומטר כלכלי חשוב. תנודות מחירים בו מספקות מידע על ציפיות לגבי אינפלציה, על קצב הצמיחה העולמית, ועל סיכונים גיאופוליטיים. הוא מאפשר "לנעול" מחירים עתידיים ומקטין אי-ודאות עבור עסקים רבים, אך תנודתיות בו יכולה גם לגרום לזעזועים כלכליים.</li>
    </ul>
    <p>כעת, כשאתם מצוידים בידע, חזרו לסימולטור ונסו ליישם את העקרונות הלכה למעשה. בהצלחה!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const appContainer = document.getElementById('app-container');
        const currentStepSpan = document.getElementById('current-step');
        const totalStepsSpan = document.getElementById('total-steps');
        const cashSpan = document.getElementById('cash');
        const portfolioValueSpan = document.getElementById('portfolio-value');
        const eventDisplayDiv = document.getElementById('event-display');
        const commoditiesListDiv = document.getElementById('commodities-list');
        const nextStepBtn = document.getElementById('next-step-btn');
        const resetBtn = document.getElementById('reset-btn');
        const portfolioDisplayDiv = document.getElementById('portfolio-display');
        const showExplanationBtn = document.getElementById('show-explanation-btn');
        const explanationDiv = document.getElementById('explanation');

        let gameState = {};
        const TOTAL_STEPS = 25; // Slightly longer simulation
        const INITIAL_CASH = 15000; // More initial cash
        const RANDOM_FLUCTUATION_PERCENT = 0.02; // +/- 2% random fluctuation per step

        const commodities = {
            oil: { name: 'נפט גולמי', initialPrice: 75, unit: 'חביות', description: 'חיוני לתחבורה ותעשייה.' },
            wheat: { name: 'חיטה', initialPrice: 520, unit: 'טון', description: 'מרכיב יסוד במזון.' },
            gold: { name: 'זהב', initialPrice: 1850, unit: 'אונקיות', description: 'נכס מקלט ומשמש בתעשייה.' },
            coffee: { name: 'קפה', initialPrice: 160, unit: 'שקים', description: 'משקה פופולרי ברחבי העולם.' },
            sugar: { name: 'סוכר', initialPrice: 22, unit: 'טון', description: 'ממתיק חיוני בתעשיית המזון.' }
        };

        // Define events and their impact (price change multiplier)
        // Added more events and varied impacts
        const events = [
            { step: 3, text: 'גל חום כבד פוגע ביבול החיטה בארה"ב!', effect: { wheat: 1.18 } },
            { step: 5, text: 'מדינות אופ"ק מפתיעות בהחלטה להגדיל את תפוקת הנפט!', effect: { oil: 0.92 } },
            { step: 7, text: 'ביקושים חזקים מסין לדברי מזון מקפיצים מחירי חיטה וסוכר.', effect: { wheat: 1.07, sugar: 1.09 } },
            { step: 9, text: 'מתח גיאופוליטי עולה במזרח התיכון - משקיעים נהרים לזהב ונפט.', effect: { gold: 1.1, oil: 1.08 } },
            { step: 11, text: 'עודף היצע עולמי מוריד את מחירי הקפה.', effect: { coffee: 0.88 } },
            { step: 13, text: 'פריצת דרך בטכנולוגיית הפקת סוכר חדשה מגדילה את ההיצע.', effect: { sugar: 0.93 } },
            { step: 15, text: 'דוח משרות חזק בארה"ב מחזק את הדולר ומעיק על מחירי הסחורות.', effect: { oil: 0.97, gold: 0.98, wheat: 0.99, coffee: 0.99, sugar: 0.98 } }, // General downward pressure
            { step: 17, text: 'סופת הוריקן פוגעת במתקני נפט במפרץ מקסיקו.', effect: { oil: 1.12 } },
            { step: 19, text: 'גילוי שדה זהב משמעותי חדש בצפון אמריקה.', effect: { gold: 0.94 } },
            { step: 21, text: 'עלייה בצריכת קפה בעולם כחלק מהתאוששות כלכלית.', effect: { coffee: 1.08 } },
            { step: 23, text: 'מלחמת סחר גלובלית מאטה את הביקוש לחומרי גלם תעשייתיים.', effect: { oil: 0.96, gold: 1.05 } } // Gold as safe haven
        ];

        function initializeGame() {
            gameState = {
                currentStep: 0,
                cash: INITIAL_CASH,
                portfolio: {},
                prices: {} // Stores prices AT THE END of the current step
            };

            // Initialize prices and portfolio (start with 0 of each commodity)
            for (const key in commodities) {
                gameState.prices[key] = commodities[key].initialPrice;
                gameState.portfolio[key] = 0;
            }

            totalStepsSpan.textContent = TOTAL_STEPS;
            resetBtn.style.display = 'none';
            nextStepBtn.style.display = 'block';
            render();
        }

        function render() {
            currentStepSpan.textContent = gameState.currentStep;
            cashSpan.textContent = gameState.cash.toFixed(2);

            let totalPortfolioValue = 0;
            commoditiesListDiv.innerHTML = ''; // Clear existing cards

            for (const key in commodities) {
                const commodity = commodities[key];
                const currentPrice = gameState.prices[key];

                // To calculate change, we need the price BEFORE the current step's price calculation finished.
                // The price update happens in nextStep(). Let's store the *previous* step's final price in nextStep.
                // For step 0, the previous price is the initial price.
                 const previousPrice = gameState.currentStep > 0 && gameState.previousPrices ? gameState.previousPrices[key] : commodity.initialPrice;


                const priceChange = currentPrice - previousPrice;
                const priceChangePercent = previousPrice === 0 ? 0 : (priceChange / previousPrice) * 100; // Prevent division by zero

                const changeClass = priceChange > 0 ? 'price-up' : (priceChange < 0 ? 'price-down' : '');
                const changeArrow = priceChange > 0 ? '▲' : (priceChange < 0 ? '▼' : '');
                const changeAnimationClass = priceChange > 0 ? 'price-flash-up' : (priceChange < 0 ? 'price-flash-down' : '');


                // Render commodity card
                const card = document.createElement('div');
                card.classList.add('commodity-card');
                // Add a data attribute for easy access in JS
                card.dataset.commodityKey = key;

                card.innerHTML = `
                    <h4>${commodity.name}</h4>
                    <p class="commodity-description">${commodity.description}</p>
                    <div class="commodity-price ${changeAnimationClass}">
                        מחיר: $${currentPrice.toFixed(2)}
                        <span class="price-change ${changeClass}">
                             (${changeArrow} ${Math.abs(priceChangePercent).toFixed(2)}%)
                        </span>
                    </div>
                     <div class="trade-controls">
                         <input type="number" min="0" value="0" id="${key}-qty" aria-label="Quantity to trade">
                         <button class="buy-btn" data-commodity="${key}">קנה</button>
                         <button class="sell-btn" data-commodity="${key}">מכור</button>
                     </div>
                `;
                commoditiesListDiv.appendChild(card);

                // Calculate portfolio value for this commodity
                totalPortfolioValue += gameState.portfolio[key] * currentPrice;
            }

            gameState.portfolioValue = totalPortfolioValue;
            portfolioValueSpan.textContent = gameState.portfolioValue.toFixed(2);

            // Render portfolio display - clear and re-populate
            portfolioDisplayDiv.innerHTML = '';
            let portfolioIsEmpty = true;
             for (const key in commodities) {
                if (gameState.portfolio[key] > 0) {
                     portfolioIsEmpty = false;
                    const commodity = commodities[key];
                    const portfolioItem = document.createElement('p');
                    portfolioItem.classList.add('portfolio-item');
                    portfolioItem.innerHTML = `
                        <span>${commodity.name}:</span>
                        <span>${gameState.portfolio[key]} ${commodity.unit}</span>
                    `;
                    portfolioDisplayDiv.appendChild(portfolioItem);
                 }
             }
             if (portfolioIsEmpty) {
                 portfolioDisplayDiv.innerHTML = '<p class="empty-portfolio">הפורטפוליו ריק. בצעו קנייה ראשונה!</p>';
             }


            // Update event display
            const currentEvent = events.find(e => e.step === gameState.currentStep);
            if (currentEvent) {
                eventDisplayDiv.textContent = currentEvent.text;
            } else {
                // Keep the previous event text visible if no new event
                 if (gameState.currentStep === 0) {
                     eventDisplayDiv.textContent = 'ברוכים הבאים לסימולטור סוחר הסחורות! התחל לסחור או לחץ "יום מסחר הבא".';
                 } else {
                      // Find the latest event up to the current step
                      const latestEvent = events.slice().reverse().find(e => e.step <= gameState.currentStep);
                      eventDisplayDiv.textContent = latestEvent ? `אחרוני החדשות: ${latestEvent.text}` : 'אין אירועים משמעותיים חדשים היום.';
                 }
            }

            // Check end condition
            if (gameState.currentStep >= TOTAL_STEPS) {
                endGame();
            }
        }

         function handleTrade(event) {
            const button = event.target;
            const commodityKey = button.dataset.commodity;
            const type = button.classList.contains('buy-btn') ? 'buy' : 'sell';
            const quantityInput = document.getElementById(`${commodityKey}-qty`);
            const quantity = parseInt(quantityInput.value, 10);

            if (isNaN(quantity) || quantity <= 0) {
                alert('אנא הזן כמות חוקית (גדולה מ-0) לביצוע הפעולה.');
                return;
            }

            const currentPrice = gameState.prices[commodityKey];
            const totalAmount = quantity * currentPrice;

            let success = false;
            let message = '';

            if (type === 'buy') {
                if (gameState.cash >= totalAmount) {
                    gameState.cash -= totalAmount;
                    gameState.portfolio[commodityKey] += quantity;
                    message = `קנית ${quantity} ${commodities[commodityKey].unit} של ${commodities[commodityKey].name} בעלות כוללת של $${totalAmount.toFixed(2)}.`;
                    success = true;
                } else {
                    message = 'אין מספיק מזומן זמין בפורטפוליו לביצוע הקנייה.';
                }
            } else if (type === 'sell') {
                if (gameState.portfolio[commodityKey] >= quantity) {
                    gameState.cash += totalAmount;
                    gameState.portfolio[commodityKey] -= quantity;
                     message = `מכרת ${quantity} ${commodities[commodityKey].unit} של ${commodities[commodityKey].name} וקיבלת $${totalAmount.toFixed(2)}.`;
                    success = true;
                } else {
                    message = `אין מספיק ${commodities[commodityKey].name} למכירה בפורטפוליו (${gameState.portfolio[commodityKey]} זמינים).`;
                }
            }

             // Provide feedback (using alert for now, matching original structure)
             alert(message);

             // Reset input field only on success
             if(success) {
                 quantityInput.value = 0;
                 render(); // Re-render on successful trade
             } else {
                 // Maybe highlight input or button on failure? For now, just the alert.
             }
        }

        function nextStep() {
            if (gameState.currentStep < TOTAL_STEPS) {
                // Store current prices before updating them for the new step
                gameState.previousPrices = { ...gameState.prices };

                gameState.currentStep++;

                // Update prices based on events and random fluctuations
                 for (const key in commodities) {
                     let currentPrice = gameState.prices[key]; // Start with the price from the end of the previous step

                     // Apply event effect if any
                    const currentEvent = events.find(e => e.step === gameState.currentStep);
                     if (currentEvent && currentEvent.effect[key]) {
                        currentPrice *= currentEvent.effect[key];
                     }

                     // Apply random fluctuation
                     const randomFactor = 1 + (Math.random() * (2 * RANDOM_FLUCTUATION_PERCENT) - RANDOM_FLUCTUATION_PERCENT); // +/- RANDOM_FLUCTUATION_PERCENT
                     currentPrice *= randomFactor;

                     // Ensure prices don't go below a minimum
                     gameState.prices[key] = Math.max(0.01, currentPrice);
                 }


                render(); // Re-render after price update
            }
        }

        function endGame() {
            nextStepBtn.style.display = 'none';
            resetBtn.style.display = 'block';
            // Calculate final performance
            const finalValue = gameState.cash + gameState.portfolioValue;
            const gainLoss = finalValue - INITIAL_CASH;
            const performanceMessage = gainLoss >= 0
                ? `כל הכבוד! סיימת את הסימולציה ברווח של $${gainLoss.toFixed(2)}.`
                : `הפסדת $${Math.abs(gainLoss).toFixed(2)}. נסה שוב ושפר את האסטרטגיה שלך.`;

            eventDisplayDiv.innerHTML = `
                <p style="font-weight: bold; color: #007bff;">הסימולציה הסתיימה!</p>
                <p>שווי הפורטפוליו הסופי שלך (מזומן + סחורות): <span style="font-size: 1.2em; font-weight: bold; color: ${gainLoss >= 0 ? '#28a745' : '#dc3545'};">$${finalValue.toFixed(2)}</span>.</p>
                <p>${performanceMessage}</p>
                <p>לחץ "התחל סימולציה מחדש" כדי לשחק שוב.</p>
            `;
             eventDisplayDiv.style.fontWeight = 'normal'; // Override italic from event-text

            // Disable trade buttons and inputs
            document.querySelectorAll('.trade-controls button').forEach(btn => btn.disabled = true);
             document.querySelectorAll('.trade-controls input[type="number"]').forEach(input => input.disabled = true);

             // Hide explanation button at the very end? Or keep it? Let's keep it.
        }

        function resetGame() {
             // Re-enable buttons just in case
             document.querySelectorAll('.trade-controls button').forEach(btn => btn.disabled = false);
             document.querySelectorAll('.trade-controls input[type="number"]').forEach(input => input.disabled = false);
             // Reset event display
             eventDisplayDiv.style.fontWeight = 'normal';
             // Remove previous prices from gameState before initializing
             delete gameState.previousPrices;

             initializeGame();
        }

        // Attach listeners once outside render
        nextStepBtn.addEventListener('click', nextStep);
        resetBtn.addEventListener('click', resetGame);

        // Use event delegation for buy/sell buttons on the list container
        commoditiesListDiv.addEventListener('click', (event) => {
            const button = event.target;
            if (button.tagName === 'BUTTON' && (button.classList.contains('buy-btn') || button.classList.contains('sell-btn'))) {
                // Pass the event object to handleTrade
                handleTrade(event);
            }
        });

         showExplanationBtn.addEventListener('click', () => {
             const isHidden = explanationDiv.classList.toggle('hidden');
             if (isHidden) {
                 showExplanationBtn.textContent = 'מהו שוק הסחורות? לחץ להרחבה';
             } else {
                  showExplanationBtn.textContent = 'הסתר הסבר';
             }
         });

        // Initial game setup
        initializeGame();

        // Optional: Add Font Awesome CSS link dynamically if not provided by platform
        // This code is commented out because the critical instruction is ONLY the markdown file.
        /*
        if (!document.querySelector('link[href*="font-awesome"]')) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css';
            document.head.appendChild(link);
        }
        */
    });
</script>
---
```