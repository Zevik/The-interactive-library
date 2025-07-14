---
title: "שוק ההון בפעולה: סימולטור אופציות וחוזים"
english_slug: stock-market-in-action-options-futures-simulator
category: "כלכלה"
tags:
  - שוק ההון
  - אופציות
  - חוזים עתידיים
  - מסחר
  - סימולטור
---
# שוק ההון בפעולה: סימולטור אופציות וחוזים

מוכנים לצלול לעולם המרתק, המאתגר והפוטנציאלי של מסחר באופציות וחוזים עתידיים? שמעתם רבות על המכשירים הפיננסיים הממונפים הללו, על ההזדמנויות העצומות שהם מציעים, ועל הסיכונים המשמעותיים שהם טומנים בחובם. אבל האם ידע תיאורטי לבדו יכין אתכם למציאות?

הדרך הטובה ביותר להפנים את המנגנונים, הדינמיקה, ואת ההשפעה הדרמטית של הזמן והתנודתיות על שווי הפוזיציות שלכם, היא באמצעות **התנסות מעשית**.

ברוכים הבאים לסימולטור שוק ההון שלנו! כאן תוכלו להתנסות בקניית אופציות Call ו-Put, וכן במסחר (קנייה ומכירה בשורט) בחוזים עתידיים, הכל באווירה מדומה וללא סיכון כספי אמיתי. עקבו אחר תנועת נכס הבסיס, קבלו החלטות מסחר, ובחנו כיצד ההחלטות הללו משפיעות על התיק שלכם מיום ליום, עד לפקיעת החוזים. האם תצליחו לנווט בין עליות וירידות, לנצל את המינוף לטובתכם, ולהגדיל את ההון שלכם? בואו נגלה!

<div class="simulator-container">
    <div class="chart-area">
        <h2>גרף מחיר נכס הבסיס</h2>
        <canvas id="assetChart"></canvas>
    </div>

    <div class="controls-area">
        <div class="status-panel">
            <h3>סטטוס התיק</h3>
            <p>יתרת מזומנים: <span id="cash" class="status-value">10,000</span> ש"ח</p>
            <p>שווי תיק כולל (מזומן + פוזיציות): <span id="portfolio-value" class="status-value">10,000</span> ש"ח</p>
            <h4>פוזיציות פתוחות:</h4>
            <ul id="open-positions">
                <li>אין פוזיציות פתוחות.</li>
            </ul>
        </div>

        <div class="market-data">
            <h3>מחירי שוק (יום <span id="current-day">0</span>)</h3>
            <table id="market-table">
                <thead>
                    <tr>
                        <th>מכשיר</th>
                        <th>פקיעה</th>
                        <th>סטרייק</th>
                        <th>מחיר (פרמיה)</th>
                        <th>פעולה</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Market data will be populated here -->
                </tbody>
            </table>
        </div>

        <div class="actions">
            <h3>ניהול זמן</h3>
            <button id="next-day" class="action-button">יום המסחר הבא ⏩</button>
        </div>
    </div>
    <div id="notification-area" class="notification"></div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --warning-color: #ffc107;
        --info-color: #17a2b8;
        --light-bg: #f8f9fa;
        --dark-bg: #e9ecef;
        --card-bg: #ffffff;
        --border-color: #dee2e6;
        --text-color: #343a40;
        --heading-color: #212529;
        --border-radius: 8px;
        --box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
    }

    .simulator-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        font-family: 'Arial', sans-serif;
        margin-bottom: 30px;
        background-color: var(--light-bg);
        padding: 20px;
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
        color: var(--text-color);
        position: relative; /* For notification positioning */
    }

    .chart-area {
        flex: 2 1 450px; /* Increased flex-basis for chart */
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
        box-shadow: var(--box-shadow);
        display: flex;
        flex-direction: column;
    }

    .chart-area h2 {
        margin-top: 0;
        margin-bottom: 15px;
        color: var(--heading-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 10px;
    }

    .controls-area {
        flex: 1 1 300px;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .status-panel, .market-data, .actions {
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
        box-shadow: var(--box-shadow);
    }

    h2, h3, h4 {
        color: var(--heading-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 8px;
        margin-top: 0;
    }

    .status-panel p {
        margin-bottom: 8px;
        font-size: 1em;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

     .status-panel .status-value {
         font-weight: bold;
         color: var(--primary-color); /* Default color */
         transition: color 0.3s ease, background-color 0.3s ease; /* Animation */
         padding: 2px 5px;
         border-radius: 4px;
     }

    .status-panel .status-value.profit {
        color: var(--success-color);
    }

    .status-panel .status-value.loss {
        color: var(--danger-color);
    }

     /* Animation for status change */
    .status-panel .status-value.highlight {
        animation: highlight-flash 0.6s ease-out;
    }

    @keyframes highlight-flash {
        0% { background-color: var(--warning-color); }
        100% { background-color: transparent; }
    }


    .status-panel h4 {
        margin-top: 15px;
        margin-bottom: 10px;
        border-bottom: none;
        padding-bottom: 0;
    }

    .status-panel ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .status-panel li {
        margin-bottom: 10px;
        font-size: 0.95em;
        color: var(--text-color);
        line-height: 1.4;
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 8px;
    }
     .status-panel li:last-child {
         border-bottom: none;
         padding-bottom: 0;
         margin-bottom: 0;
     }

    .status-panel li span {
        font-weight: bold;
    }

    .status-panel li span[style*="green"] { color: var(--success-color) !important; }
    .status-panel li span[style*="red"] { color: var(--danger-color) !important; }


    #market-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.95em;
        margin-top: 10px;
    }

    #market-table th, #market-table td {
        border: 1px solid var(--border-color);
        padding: 10px;
        text-align: left;
    }

    #market-table th {
        background-color: var(--dark-bg);
        font-weight: bold;
        color: var(--heading-color);
    }

    #market-table tr:nth-child(even) {
        background-color: var(--light-bg);
    }
     #market-table tr:hover {
         background-color: #e9f7fe; /* Subtle hover effect */
     }


    #market-table button {
        padding: 6px 12px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 0.9em;
        transition: background-color 0.2s ease, opacity 0.2s ease;
        font-weight: bold;
    }

    #market-table button.buy {
        background-color: var(--success-color);
        color: white;
    }

    #market-table button.sell {
        background-color: var(--danger-color);
        color: white;
        margin-left: 5px;
    }
     #market-table button.close-position {
        background-color: var(--secondary-color);
        color: white;
        margin-left: 8px;
        padding: 4px 8px; /* Slightly smaller for list item */
         font-size: 0.85em;
         float: right; /* Align to right in list item */
     }

    #market-table button:hover {
        opacity: 0.9;
    }

     .actions {
         margin-top: auto; /* Push actions to the bottom of controls-area */
     }

    .action-button {
        padding: 12px 20px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        cursor: pointer;
        font-size: 1.1em;
        width: 100%;
        text-align: center;
        transition: background-color 0.2s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .action-button:hover {
        background-color: #0056b3; /* Darker shade of primary */
         transform: translateY(-1px); /* Subtle press effect */
    }
    .action-button:active {
         transform: translateY(0);
         background-color: #004085;
    }

    .explanation-container {
        margin-top: 30px;
        padding: 20px;
        background-color: var(--dark-bg);
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
        color: var(--text-color);
    }

    .explanation-container h3 {
         border-bottom: 1px solid #adb5bd;
         padding-bottom: 8px;
         margin-top: 0;
         color: var(--heading-color);
    }

    .explanation-container ul {
        padding-left: 25px;
    }

    .explanation-container li {
        margin-bottom: 15px;
        line-height: 1.6;
        color: var(--text-color);
    }
     .explanation-container li h4 {
         margin-bottom: 5px;
         color: var(--primary-color);
         border-bottom: none;
         padding-bottom: 0;
     }
     .explanation-container li ul {
         margin-top: 8px;
         margin-bottom: 0;
         padding-left: 20px;
     }
      .explanation-container li ul li {
          margin-bottom: 8px;
          line-height: 1.5;
          font-size: 0.95em;
      }


    #toggle-explanation {
        display: block;
        width: auto;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        text-align: center;
        transition: background-color 0.2s ease;
    }

     #toggle-explanation:hover {
        background-color: #5a6268;
     }

    #notification-area {
         position: absolute;
         top: 20px;
         left: 50%;
         transform: translateX(-50%);
         padding: 10px 20px;
         background-color: var(--info-color);
         color: white;
         border-radius: var(--border-radius);
         z-index: 100;
         opacity: 0;
         visibility: hidden;
         transition: opacity 0.3s ease, visibility 0.3s ease;
         font-weight: bold;
         text-align: center;
         min-width: 250px;
         box-shadow: var(--box-shadow);
     }
     #notification-area.show {
         opacity: 1;
         visibility: visible;
     }
     #notification-area.success { background-color: var(--success-color); }
     #notification-area.error { background-color: var(--danger-color); }
     #notification-area.warning { background-color: var(--warning-color); }


    @media (max-width: 992px) { /* Adjusting breakpoint slightly for better flow */
        .simulator-container {
            flex-direction: column;
        }
        .chart-area, .controls-area {
            flex: 1 1 100%;
        }
         .controls-area {
             flex-direction: column; /* Ensure columns stack */
             gap: 15px;
         }
        .status-panel, .market-data, .actions {
            padding: 15px;
        }
        #market-table th, #market-table td {
            padding: 8px;
        }
         #market-table button {
             font-size: 0.8em;
             padding: 4px 8px;
         }
    }
</style>

<button id="toggle-explanation">💡 הסבר על אופציות וחוזים עתידיים</button>

<div id="explanation" class="explanation-container" style="display: none;">
    <h3>הצצה לעולם המכשירים הפיננסיים המורכבים</h3>
    <ul>
        <li>
            <h4>אופציה (Option): הזכות, לא החובה</h4>
            דמיינו שאתם קונים כרטיס המעניק לכם את האפשרות, אך לא את ההתחייבות, לבצע עסקה עתידית על נכס כלשהו (מניה, סחורה, וכו') במחיר שנקבע מראש (מחיר המימוש), עד לתאריך מסוים (תאריך הפקיעה). זוהי אופציה. אתם משלמים "פרמיה" קטנה על הזכות הזו. המוכר של האופציה מקבל את הפרמיה הזו, אך לוקח על עצמו את הסיכון שתבחרו לממש את הזכות. קונה אופציה יודע שהפסדו המקסימלי הוא הפרמיה ששילם. מוכר האופציה יכול להרוויח את הפרמיה, אך הפסדו הפוטנציאלי גדול יותר.
        </li>
        <li>
            <h4>Call vs. Put: צופה עלייה או ירידה?</h4>
            <ul>
                <li>**אופציית Call:** מעניקה לכם את הזכות לקנות את נכס הבסיס במחיר המימוש. קונים Call כשהם אופטימיים וצופים עליית מחיר משמעותית. אם המחיר אכן עולה מעל מחיר המימוש, האופציה "בתוך הכסף" (In-the-Money) ושוויה עולה.</li>
                <li>**אופציית Put:** מעניקה לכם את הזכות למכור את נכס הבסיס במחיר המימוש. קונים Put כשהם פסימיים וצופים ירידת מחיר. אם המחיר אכן יורד מתחת למחיר המימוש, האופציה "בתוך הכסף" ושוויה עולה. Put יכול לשמש גם להגנה על פוזיציית לונג (קנייה) קיימת בנכס הבסיס.</li>
            </ul>
        </li>
        <li>
            <h4>המפתחות לאופציה: סטרייק, פרמיה, וזמן</h4>
            <ul>
                <li>**מחיר מימוש (Strike Price):** מחיר העסקה הפוטנציאלית אם תבחרו לממש את האופציה.</li>
                <li>**פרמיה (Premium):** המחיר ששילמתם (וקיבל המוכר) עבור האופציה. זו העלות של הזכות. הפרמיה מושפעת מהרבה גורמים: מחיר נכס הבסיס יחסית לסטרייק (ערך פנימי), כמה זמן נותר לפקיעה (ערך זמן), התנודתיות הצפויה בשוק (Volatility), ריבית ועוד.</li>
                <li>**תאריך פקיעה (Expiration Date):** התאריך שבו האופציה פשוט מפסיקה להתקיים. אם לא היתה שווה מימוש עד אז, היא הופכת לחסרת ערך לחלוטין. ערך הזמן של האופציה נשחק עם כל יום שעובר!</li>
            </ul>
        </li>
        <li>
            <h4>חוזה עתידי (Futures): התחייבות בלתי מתפשרת</h4>
            בניגוד לאופציה (זכות), חוזה עתידי הוא **הסכם מחייב** לקנות או למכור נכס ספציפי, בכמות ספציפית, במחיר שנקבע היום, אך עם העברה וקבלת תשלום בתאריך עתידי קבוע מראש. שני הצדדים לחוזה מחויבים לקיים אותו בתאריך הפקיעה (אלא אם כן "סגרו" את הפוזיציה לפני כן על ידי ביצוע עסקה הפוכה). חוזים עתידיים משמשים לרוב לגידור סיכונים (למשל, חקלאי המוכר עכשיו חוזה על יבול עתידי כדי לנעול מחיר) או לספקולציה על תנועות מחיר. מכשיר זה ממונף מאוד, והרווחים או ההפסדים יכולים להיות משמעותיים ביותר.
        </li>
        <li>
            <h4>הכוח והסכנה: מינוף (Leverage)</h4>
            גם אופציות וגם חוזים עתידיים הם כלים ממונפים. אתם משקיעים סכום קטן יחסית (הפרמיה או הביטחונות - Margin) כדי לשלוט על שווי גדול בהרבה של נכס בסיס. זה אומר ששינוי קטן באחוזים במחיר נכס הבסיס יכול לגרום לשינוי גדול מאוד, באחוזים, על ההשקעה המקורית שלכם! מינוף יכול להעצים רווחים בצורה פנטסטית, אבל הוא גם מעצים הפסדים באותה מידה. סוחרים חדשים חייבים להבין זאת היטב.
        </li>
        <li>
            <h4>סיכונים שאסור להתעלם מהם</h4>
            הסיכונים העיקריים כוללים: הפסד מלא של הפרמיה באופציות אם לא מומשו; הפסדים גדולים בחוזים עתידיים שעשויים אף לחייב הזרמת כסף נוסף (Margin Call); סיכון נזילות בשווקים מסוימים; ומעל הכל, המורכבות הרבה של תמחור וניהול הסיכונים במכשירים אלו. הסימולטור נועד לתת לכם טעימה מבוקרת של הדינמיקה הזו.
        </li>
    </ul>
</div>


<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        // --- Simulator State ---
        let cash = 10000;
        let initialCash = cash;
        let assetPrice = 100;
        let currentDay = 0;
        const totalDays = 90; // Extended simulation length
        const assetPrices = [assetPrice];
        const dailyVolatility = 0.015; // Increased volatility slightly for more action
        const tradingUnit = 10; // Unit size for options/futures contracts (e.g., 1 contract = 10 units)

        // Simplified Options/Futures setup
        const contracts = [
            { type: 'Call', strike: 100, expirationDays: 15 },
            { type: 'Call', strike: 105, expirationDays: 30 },
            { type: 'Call', strike: 110, expirationDays: 45 },
            { type: 'Put', strike: 100, expirationDays: 15 },
            { type: 'Put', strike: 95, expirationDays: 30 },
            { type: 'Put', strike: 90, expirationDays: 45 },
            { type: 'Futures', strike: null, expirationDays: 30 },
             { type: 'Futures', strike: null, expirationDays: 60 },
        ];

        let openPositions = []; // { contract: {type, strike, expirationDays}, quantity: 1, entryPrice: 5, entryDay: 0, direction: 'Long' }

        // --- DOM Elements ---
        const cashEl = document.getElementById('cash');
        const portfolioValueEl = document.getElementById('portfolio-value');
        const openPositionsEl = document.getElementById('open-positions');
        const marketTableBodyEl = document.querySelector('#market-table tbody');
        const currentDayEl = document.getElementById('current-day');
        const nextDayBtn = document.getElementById('next-day');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
         const notificationArea = document.getElementById('notification-area');


        // --- Chart ---
        const ctx = document.getElementById('assetChart').getContext('2d');
        const assetChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [0],
                datasets: [{
                    label: 'מחיר נכס בסיס',
                    data: assetPrices,
                    borderColor: var('--primary-color'),
                    backgroundColor: 'rgba(0, 123, 255, 0.1)',
                    borderWidth: 2, /* Slightly thicker line */
                    fill: false,
                    pointRadius: 3, /* Slightly larger points */
                    pointBackgroundColor: var('--primary-color'),
                    pointBorderColor: '#fff',
                    pointHoverRadius: 5,
                     tension: 0.1 /* Add some curve */
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false, /* Allows CSS to control size */
                 animation: {
                     duration: 800, /* Smooth transition for price changes */
                     easing: 'easeInOutQuad'
                 },
                 scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'יום מסחר',
                            color: var('--text-color')
                        },
                        ticks: { color: var('--secondary-color') },
                        grid: { color: '#eee' }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'מחיר',
                             color: var('--text-color')
                        },
                        ticks: { color: var('--secondary-color') },
                         grid: { color: '#eee' }
                    }
                },
                 plugins: {
                     legend: {
                         display: true,
                         labels: { color: var('--text-color') }
                     },
                     tooltip: {
                         backgroundColor: 'rgba(0, 0, 0, 0.7)',
                         bodyColor: '#fff',
                         titleColor: '#fff'
                     }
                 }
            }
        });

        // --- Functions ---

        function updateChart() {
            assetChart.data.labels = Array.from({ length: assetPrices.length }, (_, i) => i);
            assetChart.data.datasets[0].data = assetPrices;
            assetChart.update(); // Chart.js handles animation on update
        }

        function calculateOptionPremium(type, strike, expirationDaysRemaining, currentAssetPrice) {
            // More refined (but still simplified) Black-Scholes inspired calculation
            // This is NOT a real BS model, but attempts to capture key factors:
            // Intrinsic Value: How much "in the money"
            // Time Value: Decays over time, increases with volatility
            // Assumes a constant risk-free rate (0 for simplicity) and no dividends

            let intrinsicValue = 0;
            if (type === 'Call') {
                intrinsicValue = Math.max(0, currentAssetPrice - strike);
            } else if (type === 'Put') {
                intrinsicValue = Math.max(0, strike - currentAssetPrice);
            }

            // Simple time value model: Higher time to expiration and higher volatility increase time value.
            // Time value is highest when At-The-Money (ATM) and decays as it moves deeper ITM or OTM, and as time passes.
            const daysFactor = Math.max(0, expirationDaysRemaining) / totalDays; // Time decay component (0 to 1)
            const volatilityImpact = dailyVolatility * 100; // Base impact from volatility

            // Premium for OTM/ATM options needs a time value component
            let timeValue = 0;
            const distanceToStrike = Math.abs(currentAssetPrice - strike);
            const atmRange = volatilityImpact * 2; // Range around strike considered ATM/near ATM

            if (expirationDaysRemaining > 0) {
                 if (distanceToStrike <= atmRange) { // Near or At the Money
                     timeValue = daysFactor * volatilityImpact * 20; // Higher time value ATM
                 } else { // Out of the Money (or deep ITM)
                     // Time value exists but is less than ATM
                     timeValue = daysFactor * volatilityImpact * 5 + daysFactor * Math.sqrt(expirationDaysRemaining);
                 }
                 // Time decay acceleration near expiration
                 if (expirationDaysRemaining < 10) {
                      timeValue *= (expirationDaysRemaining / 10); // Accelerate decay in last 10 days
                 }
            }


            let premium = intrinsicValue + timeValue;

            // Ensure premium is realistic and not negative
            premium = Math.max(0.05 * tradingUnit, premium); // Minimum small premium to represent bid-ask spread / friction

            return premium;
        }

         function calculateFuturePrice(currentAssetPrice, expirationDaysRemaining) {
             // Still simplified: Futures price is spot price + simple carry cost/benefit.
             // Let's add a slight contango (futures price > spot) that reduces towards expiration.
             // This makes it slightly more realistic than Futures = Spot.
             const carryCost = (totalDays - expirationDaysRemaining) * 0.01; // Simple cost increasing with time
             return currentAssetPrice + carryCost;
         }


        function updateMarketData() {
            marketTableBodyEl.innerHTML = ''; // Clear current data

            contracts.forEach(contract => {
                const expirationDaysRemaining = contract.expirationDays - currentDay;
                if (expirationDaysRemaining < 0) {
                     // Do not list contracts that expired on previous days
                     return;
                }

                let price;
                let instrumentName;
                let strikeDisplay = '-';
                let actionsHtml = '';

                if (contract.type === 'Futures') {
                    price = calculateFuturePrice(assetPrice, expirationDaysRemaining);
                    instrumentName = `חוזה עתידי (פקיעה בעוד ${expirationDaysRemaining} ימים)`;
                     // Can only buy (long) or sell (short) futures
                     if (expirationDaysRemaining >= 0) { // Can only trade if not expired (or expiring today)
                        actionsHtml = `
                            <button class="buy" data-type="Futures" data-expiration="${contract.expirationDays}" data-price="${price}">קנה (לונג)</button>
                            <button class="sell" data-type="Futures" data-expiration="${contract.expirationDays}" data-price="${price}">מכור (שורט)</button>
                        `;
                     } else {
                          actionsHtml = 'פקע';
                     }


                } else { // Option (Call or Put)
                    price = calculateOptionPremium(contract.type, contract.strike, expirationDaysRemaining, assetPrice);
                     instrumentName = `אופציית ${contract.type === 'Call' ? 'Call' : 'Put'} (סטרייק ${contract.strike}, פקיעה בעוד ${expirationDaysRemaining} ימים)`;
                    strikeDisplay = contract.strike;
                     // Can only buy options (selling options requires margin and is more complex)
                    if (expirationDaysRemaining >= 0) { // Can only trade if not expired (or expiring today)
                         actionsHtml = `
                            <button class="buy" data-type="${contract.type}" data-strike="${contract.strike}" data-expiration="${contract.expirationDays}" data-price="${price}">קנה</button>
                        `;
                    } else {
                         actionsHtml = 'פקע';
                    }
                }

                const row = marketTableBodyEl.insertRow();
                row.innerHTML = `
                    <td>${instrumentName}</td>
                    <td>יום ${contract.expirationDays}</td>
                    <td>${strikeDisplay}</td>
                    <td>${price.toFixed(2)}</td>
                    <td>${actionsHtml}</td>
                `;
            });

             // Add event listeners to the new buttons
            marketTableBodyEl.querySelectorAll('.buy').forEach(button => {
                button.addEventListener('click', handleBuy);
            });
             marketTableBodyEl.querySelectorAll('.sell').forEach(button => {
                button.addEventListener('click', handleSellFutures);
            });
        }

         function showNotification(message, type = 'info', duration = 3000) {
             notificationArea.textContent = message;
             notificationArea.className = `notification show ${type}`; // Add type class for styling
             setTimeout(() => {
                 notificationArea.className = `notification ${type}`; // Remove show class
             }, duration);
         }


        function handleBuy(event) {
            const button = event.target;
            const type = button.dataset.type;
            const strike = button.dataset.strike ? parseFloat(button.dataset.strike) : null;
            const expirationDays = parseInt(button.dataset.expiration);
            const price = parseFloat(button.dataset.price);

            const quantity = 1; // For simplicity, buy/sell 1 unit/contract at a time

             let cost = 0;
             let marginRequired = 0;

             if (type === 'Futures') {
                 // Buying futures (longing) requires margin, not full price
                 // Let's require a small percentage of the contract value as margin
                 marginRequired = price * tradingUnit * quantity * 0.05; // e.g., 5% margin
                 cost = marginRequired; // Cost is the margin required (initially)
             } else { // Option
                 cost = price * tradingUnit * quantity; // Cost is the premium paid
             }

            if (cash >= cost) {
                cash -= cost;
                const position = {
                    contract: { type, strike, expirationDays },
                    quantity: quantity,
                    entryPrice: price, // Premium for options, price for futures (used for P/L calc)
                    entryDay: currentDay,
                    direction: 'Long',
                     initialCost: cost // Store the initial outlay (premium or margin)
                };
                openPositions.push(position);
                updateStatus();
                showNotification(`${type} נקנה: ${quantity} יחידות במחיר ${price.toFixed(2)} (סה"כ ${cost.toFixed(2)} ש"ח)`, 'success');
            } else {
                showNotification('אין מספיק מזומנים לבצע את הפעולה!', 'error');
            }
        }

         function handleSellFutures(event) {
             const button = event.target;
             const type = button.dataset.type; // Should be 'Futures'
             const expirationDays = parseInt(button.dataset.expiration);
             const price = parseFloat(button.dataset.price);

             const quantity = 1; // For simplicity
             // Selling futures (shorting) also requires initial margin.
             const marginRequired = price * tradingUnit * quantity * 0.05; // e.g., 5% margin

             if (cash >= marginRequired) {
                 cash -= marginRequired; // Deduct margin from cash
                 const position = {
                     contract: { type, strike: null, expirationDays },
                     quantity: quantity,
                     entryPrice: price, // Price at which the short position was opened
                     entryDay: currentDay,
                     direction: 'Short',
                      initialCost: marginRequired // Store the margin required
                 };
                 openPositions.push(position);
                 updateStatus();
                 showNotification(`חוזה עתידי נמכר (שורט): ${quantity} יחידות במחיר ${price.toFixed(2)} (ביטחונות נדרשו ${marginRequired.toFixed(2)} ש"ח)`, 'success');
             } else {
                 showNotification(`אין מספיק מזומנים לביטחונות (נדרש ${marginRequired.toFixed(2)} ש"ח)!`, 'error');
             }
         }


        function updateStatus() {
             const previousCash = parseFloat(cashEl.textContent);
             const previousPortfolioValue = parseFloat(portfolioValueEl.textContent);

            cashEl.textContent = cash.toFixed(2);

            let totalPortfolioValue = cash; // Start with cash

            openPositionsEl.innerHTML = '';

            if (openPositions.length === 0) {
                openPositionsEl.innerHTML = '<li>אין פוזיציות פתוחות.</li>';
            } else {
                openPositions.forEach((pos, index) => {
                    const expirationDaysRemaining = pos.contract.expirationDays - currentDay;

                     let currentValuePerUnit = 0;
                     let unrealizedPLPerUnit = 0;
                     let isExpiredToday = expirationDaysRemaining === 0;
                     let isExpiredEarlier = expirationDaysRemaining < 0;

                     if (!isExpiredEarlier) { // Only calculate for non-expired contracts
                         if (pos.contract.type === 'Futures') {
                             currentValuePerUnit = calculateFuturePrice(assetPrice, expirationDaysRemaining);
                              // Unrealized P/L for futures is current price vs entry price
                              unrealizedPLPerUnit = (pos.direction === 'Long' ? 1 : -1) * (currentValuePerUnit - pos.entryPrice);
                              // Portfolio value includes the initial margin + the accrued P/L
                              totalPortfolioValue += pos.initialCost + (unrealizedPLPerUnit * tradingUnit * pos.quantity);

                         } else { // Option
                              currentValuePerUnit = calculateOptionPremium(pos.contract.type, pos.contract.strike, expirationDaysRemaining, assetPrice);
                              // Unrealized P/L for options is current premium vs entry premium
                              unrealizedPLPerUnit = currentValuePerUnit - pos.entryPrice;
                              // Portfolio value includes the current value of the option holding
                              totalPortfolioValue += currentValuePerUnit * tradingUnit * pos.quantity;
                         }
                     } else { // Should not happen if processExpiration works, but for safety
                         currentValuePerUnit = 0;
                         unrealizedPLPerUnit = -(pos.initialCost || pos.entryPrice); // Assume loss of initial cost/premium if not settled
                         // This position should have been removed.
                     }

                    const totalUnrealizedPL = unrealizedPLPerUnit * tradingUnit * pos.quantity;

                    const listItem = document.createElement('li');

                    const entryDetail = pos.contract.type === 'Futures' ?
                        `${pos.direction === 'Long' ? 'לונג' : 'שורט'} @ ${pos.entryPrice.toFixed(2)} (ביטחונות: ${pos.initialCost.toFixed(2)})` :
                        `@ ${pos.entryPrice.toFixed(2)} (עלות: ${pos.initialCost.toFixed(2)})`;


                    listItem.innerHTML = `
                         **${pos.quantity}x** ${pos.contract.type}
                         ${pos.contract.type !== 'Futures' ? '(סטרייק ' + pos.contract.strike + '), ' : ''}
                         פקיעה יום ${pos.contract.expirationDays}.
                         כניסה ${entryDetail}.
                         שווי נוכחי ליחידה: ${currentValuePerUnit.toFixed(2)}.
                         <br>
                         **רווח/הפסד רגעי:** <span style="color:${totalUnrealizedPL >= 0 ? 'green' : 'red'};">${totalUnrealizedPL.toFixed(2)}</span> ש"ח
                         ${isExpiredToday ? `<strong>(פוקע היום!)</strong>` : isExpiredEarlier ? `<strong>(פקע)</strong>` : `(נותרו ${expirationDaysRemaining} ימים)`}
                         ${pos.contract.type === 'Futures' && expirationDaysRemaining > 0 ? `<button class="close-position" data-index="${index}">סגור פוזיציה</button>` : ''}
                    `;
                    openPositionsEl.appendChild(listItem);
                });
            }

             // Update the total portfolio value
            portfolioValueEl.textContent = totalPortfolioValue.toFixed(2);

             // Apply status color and animation based on change
            const cashChange = cash - previousCash;
             const portfolioChange = totalPortfolioValue - previousPortfolioValue;

             cashEl.classList.remove('profit', 'loss', 'highlight');
             if (cashChange > 0.01) { cashEl.classList.add('profit', 'highlight'); }
             else if (cashChange < -0.01) { cashEl.classList.add('loss', 'highlight'); }

             portfolioValueEl.classList.remove('profit', 'loss', 'highlight');
             if (portfolioChange > 0.01) { portfolioValueEl.classList.add('profit', 'highlight'); }
             else if (portfolioChange < -0.01) { portfolioValueEl.classList.add('loss', 'highlight'); }


             // Add event listeners for closing futures positions (need to re-add as list is cleared)
             openPositionsEl.querySelectorAll('.close-position').forEach(button => {
                button.addEventListener('click', handleClosePosition);
            });
        }

        function handleClosePosition(event) {
             const index = parseInt(event.target.dataset.index);
             const position = openPositions[index];

             if (!position || position.contract.type !== 'Futures' || position.contract.expirationDays <= currentDay) {
                 showNotification("שגיאה בסגירת פוזיציה או שהיא כבר פקעה.", 'warning');
                 return;
             }

             const expirationDaysRemaining = position.contract.expirationDays - currentDay;
             const currentPricePerUnit = calculateFuturePrice(assetPrice, expirationDaysRemaining);

             let finalPL = (position.direction === 'Long' ? 1 : -1) * (currentPricePerUnit - position.entryPrice) * tradingUnit * position.quantity;

             const initialMargin = position.initialCost;

             cash += initialMargin + finalPL; // Return margin + settle P/L

             showNotification(`חוזה עתידי נסגר (ידני): רווח/הפסד סופי: ${finalPL.toFixed(2)} ש"ח. הביטחונות (${initialMargin.toFixed(2)} ש"ח) שוחררו.`, finalPL >= 0 ? 'success' : 'error');

             // Remove the position
             openPositions.splice(index, 1);
             updateStatus();
             updateMarketData();
        }


        function processExpiration() {
            const activePositions = [];
            openPositions.forEach(pos => {
                if (pos.contract.expirationDays === currentDay) {
                    let finalPL = 0;
                    let alertMessage = '';

                    if (pos.contract.type === 'Call') {
                        // Options expire worthless if OTM. Settle ITM options.
                        const finalValuePerUnit = Math.max(0, assetPrice - pos.contract.strike);
                        const finalTotalValue = finalValuePerUnit * tradingUnit * pos.quantity;
                        // P/L is final value minus initial premium paid
                        finalPL = finalTotalValue - pos.initialCost;
                        // Cash changes by the final P/L
                        cash += finalPL;
                         alertMessage = `🔥 אופציית Call (סטרייק ${pos.contract.strike}) פקעה. שווי מימוש: ${finalTotalValue.toFixed(2)}. רווח/הפסד סופי: ${finalPL.toFixed(2)} ש"ח.`;

                    } else if (pos.contract.type === 'Put') {
                         // Options expire worthless if OTM. Settle ITM options.
                        const finalValuePerUnit = Math.max(0, pos.contract.strike - assetPrice);
                         const finalTotalValue = finalValuePerUnit * tradingUnit * pos.quantity;
                         // P/L is final value minus initial premium paid
                        finalPL = finalTotalValue - pos.initialCost;
                         cash += finalPL;
                         alertMessage = `🔥 אופציית Put (סטרייק ${pos.contract.strike}) פקעה. שווי מימוש: ${finalTotalValue.toFixed(2)}. רווח/הפסד סופי: ${finalPL.toFixed(2)} ש"ח.`;

                    } else if (pos.contract.type === 'Futures') {
                         // Futures are marked-to-market daily. The final P/L is just the last day's change + return of margin.
                         // For simplicity in this sim, we just return the initial margin as the P/L accumulated daily.
                         const initialMargin = pos.initialCost;
                         cash += initialMargin; // Return the margin that was held
                         alertMessage = `🔥 חוזה עתידי פקע. הביטחונות (${initialMargin.toFixed(2)} ש"ח) שוחררו. הרווח/הפסד שוקלל יומית.`;
                         finalPL = 0; // P/L was settled daily, no extra P/L on expiration itself here.
                    }

                    // Show notification for expired contract
                    showNotification(alertMessage, finalPL >= 0 ? 'success' : 'error', 7000);

                } else if (pos.contract.expirationDays < currentDay) {
                     // Position expired on a previous day and wasn't removed. This is an error state.
                     console.error("Expired position found in list:", pos);
                     // Do not add to activePositions, effectively removing it now.
                }
                else {
                    activePositions.push(pos); // Keep non-expired positions
                }
            });
            openPositions = activePositions;
        }


        function nextDay() {
            if (currentDay >= totalDays) {
                showNotification('הסימולציה הסתיימה! נגמרו ימי המסחר.', 'info');
                nextDayBtn.disabled = true;
                 // Final status update after all processing
                 updateStatus();
                return;
            }

             // Process expirations at the start of the day (contracts expiring *today*)
             processExpiration();

            currentDay++;
            currentDayEl.textContent = currentDay;

            // Simulate asset price change (Geometric Brownian Motion step)
            // Using Box-Muller transform for normal distribution
            let u = 0, v = 0;
            while(u === 0) u = Math.random(); // Converting [0,1) to (0,1)
            while(v === 0) v = Math.random();
            const z = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v); // Standard normal variable

             // Drift + Volatility component (simplified)
            const drift = 0.0005; // Slight upward drift bias
            const priceChange = assetPrice * (drift + dailyVolatility * z);

            assetPrice += priceChange;
            assetPrice = Math.max(5, assetPrice); // Ensure price doesn't go too low
            assetPrices.push(assetPrice);

            // Update UI (based on the new asset price)
            updateChart();
            updateMarketData(); // Market prices update based on new assetPrice
            updateStatus(); // Status updates based on new market prices and any expirations processed


            if (currentDay >= totalDays) {
                 showNotification('הסימולציה הסתיימה! נגמרו ימי המסחר.', 'info');
                 nextDayBtn.disabled = true;
                 // Final status update after all processing
                 updateStatus();
            }
        }

        function setupEventListeners() {
            nextDayBtn.addEventListener('click', nextDay);
            toggleExplanationBtn.addEventListener('click', () => {
                const isHidden = explanationDiv.style.display === 'none';
                explanationDiv.style.display = isHidden ? 'block' : 'none';
                toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר 👆' : '💡 הסבר על אופציות וחוזים עתידיים';
            });
        }

        // --- Initialization ---
        function initialize() {
            currentDayEl.textContent = currentDay;
             updateChart();
            updateMarketData(); // Populate initial market data
            updateStatus(); // Populate initial status (cash, empty positions)
            setupEventListeners();
             showNotification('ברוכים הבאים לסימולטור! התחילו בבחירת אופציה או חוזה וקליק על "יום המסחר הבא".', 'info', 6000);
        }

        initialize();
    });
</script>
```