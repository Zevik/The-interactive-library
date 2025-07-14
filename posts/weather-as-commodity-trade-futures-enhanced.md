---
title: "מזג אוויר כסחורה: נסה לסחור בחוזים עתידיים"
english_slug: weather-as-commodity-trade-futures-enhanced
category: "מדעי החברה / כלכלה ופיננסים"
tags:
  - חוזים עתידיים
  - מסחר
  - מזג אוויר
  - סימולציה
  - כלכלה התנהגותית
  - שוק ההון
---
# מזג אוויר כסחורה: האם תצליח לסחור בהצלחה בחוזים עתידיים?

האם דמיינת פעם שאפשר "לסחור" במזג האוויר בדיוק כמו שמסחרים במניות או בסחורות? הכירו את שוק החוזים העתידיים על מזג אוויר - זירה גלובלית בה סוחרים מהמרים (או מגדרים סיכון!) על טמפרטורות עתידיות, כמות משקעים ועוד. זה נשמע דמיוני, אבל זה שוק אמיתי שמשפיע על חברות ענק! בואו נצלול לסימולציה אינטראקטיבית ונראה אם יש לכם מה שצריך כדי להרוויח מהתחזית.

<style>
/* Enhanced General Styles */
body {
    background-color: #eef4f8; /* Light background */
    margin: 0;
    padding: 20px;
    direction: rtl;
    font-family: 'Arial', sans-serif; /* Use a common, clean font */
    color: #333;
}

#app, #explanation {
    max-width: 750px; /* Slightly wider */
    margin: 20px auto;
    padding: 25px; /* More padding */
    border: none; /* Remove default border */
    border-radius: 12px; /* More rounded corners */
    background-color: #ffffff; /* White background for content boxes */
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    overflow: hidden; /* Clear floats */
}

/* Headings */
h1 {
    color: #1a237e; /* Deep blue */
    text-align: center;
    margin-bottom: 30px;
}

#app h2, #explanation h2 {
    text-align: center;
    color: #303f9f; /* Slightly lighter blue */
    margin-top: 0;
    margin-bottom: 25px;
    font-size: 1.8em;
    position: relative; /* For underline effect */
    padding-bottom: 10px;
}
#app h2::after, #explanation h2::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 3px;
    background-color: #5c6bc0; /* Accent blue */
    border-radius: 2px;
}

#trading-area h3, #result h2 {
    color: #455a64; /* Dark grey-blue */
    margin-top: 0;
    margin-bottom: 20px;
    font-size: 1.4em;
    text-align: center; /* Center section titles */
}

/* State, Trading, and Result areas - Card-like appearance */
#game-state, #trading-area, #result {
    margin-bottom: 25px;
    padding: 20px;
    border: none;
    border-radius: 8px;
    background-color: #f5f5f5; /* Light grey background for sections */
    box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.08); /* Subtle inner shadow */
}

#result {
    text-align: center;
    display: none; /* Hidden by default */
    background-color: #e8f5e9; /* Light green for result */
}
#result.loss {
     background-color: #ffebee; /* Light red for loss result */
}
#result.neutral {
     background-color: #e3f2fd; /* Light blue for neutral result */
}


/* Divs inside state and result */
#game-state div, #result div {
    margin-bottom: 12px; /* Increased spacing */
    padding: 5px 0;
    border-bottom: 1px dashed #cfd8dc; /* Subtle separator */
}
#game-state div:last-child, #result div:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

/* State variables display */
#game-state div strong {
    color: #546e7a; /* Darker grey-blue for labels */
    display: inline-block; /* Ensure alignment */
    width: 150px; /* Fixed width for labels */
    margin-left: 10px; /* Space between label and value */
    text-align: right; /* Align labels to the right */
}
#game-state div span {
     font-weight: normal; /* Value is not bold by default */
     color: #333;
}

/* Specific state value styles */
#cash, #position-value, #profit-loss { font-weight: bold; }
#cash.positive, #profit-loss.positive { color: #4CAF50; } /* Green for positive */
#cash.negative, #profit-loss.negative { color: #f44336; } /* Red for negative */
#cash.neutral, #profit-loss.neutral { color: #555; } /* Grey for neutral */

#market-price {
    font-weight: bold;
    font-size: 1.1em;
}
.price-change-up { color: #4CAF50; } /* Green */
.price-change-down { color: #f44336; } /* Red */
.price-change-icon {
    display: inline-block;
    margin-right: 5px;
    font-size: 0.9em;
    vertical-align: middle;
}

/* Trading area controls layout */
#trading-area > div {
    display: flex;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
    align-items: center;
    gap: 15px; /* More space between items */
    justify-content: center; /* Center controls */
    margin-bottom: 15px;
}

/* Label style */
#trading-area label {
    white-space: nowrap;
    color: #546e7a;
    font-weight: bold;
}

/* Input field style */
#trading-area input[type="number"] {
    padding: 10px 12px; /* Increased padding */
    border: 1px solid #b0bec5; /* Lighter border */
    border-radius: 6px; /* More rounded */
    width: 90px; /* Slightly wider */
    font-size: 1em;
    text-align: center;
    -moz-appearance: textfield; /* Hide stepper arrows in Firefox */
}
/* Hide stepper arrows in Chrome, Safari, Edge */
#trading-area input[type="number"]::-webkit-outer-spin-button,
#trading-area input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}


/* Common button styles */
.sim-button {
    padding: 10px 25px; /* More padding */
    border: none;
    border-radius: 6px; /* More rounded */
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
    font-weight: bold;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
    text-shadow: 0 1px 1px rgba(0,0,0,0.1);
}
.sim-button:hover {
    transform: translateY(-1px); /* Slight lift on hover */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.sim-button:active {
    transform: translateY(0); /* Press effect */
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
.sim-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

/* Specific button styles */
#trading-area button#buy-btn {
    background-color: #4CAF50; /* Green */
    color: white;
}
#trading-area button#sell-btn {
    background-color: #f44336; /* Red */
    color: white;
}
#controls button#next-day-btn {
    background-color: #03a9f4; /* Light blue */
    color: white;
    width: 100%; /* Full width in controls area */
    padding: 12px 0;
    margin-bottom: 10px;
}
#result button#reset-btn, #toggle-explanation {
     background-color: #607d8b; /* Blue-grey */
     color: white;
     display: block; /* Make them block elements */
     margin: 20px auto 10px auto; /* Center buttons */
     width: fit-content; /* Adjust width to content */
}

/* Trade message style */
#trade-message {
    margin-top: 15px;
    padding: 10px;
    border-radius: 4px;
    font-size: 0.95em;
    min-height: 1.2em; /* Reserve space */
    text-align: center;
}
#trade-message.success {
    background-color: #e8f5e9; /* Light green */
    color: #2e7d32; /* Dark green */
    border: 1px solid #a5d6a7;
}
#trade-message.error {
    background-color: #ffebee; /* Light red */
    color: #c62828; /* Dark red */
    border: 1px solid #ef9a9a;
}
#trade-message.info {
     background-color: #e3f2fd; /* Light blue */
     color: #1565c0; /* Dark blue */
     border: 1px solid #90caf9;
}


/* Controls area style */
#controls {
    text-align: center;
    margin-bottom: 25px;
}

/* Result specific styles */
#result span {
    font-weight: bold;
}
#result .actual-temp { color: #03a9f4; } /* Blue for actual temp */
#result .contract-met { font-weight: bold; }


/* Toggle Explanation button style */
#toggle-explanation {
    margin-top: 30px;
    margin-bottom: 20px;
}

/* Explanation div style */
#explanation {
    display: none; /* Hidden by default */
    background-color: #e1f5fe; /* Very light blue */
    border: 1px dashed #b3e5fc; /* Dashed border */
    box-shadow: none; /* No shadow for explanation */
}
#explanation h2::after {
    background-color: #4fc3f7; /* Lighter blue accent */
}
#explanation h3 {
    color: #0277bd; /* Darker blue */
    margin-top: 25px;
    margin-bottom: 10px;
    border-bottom: 1px solid #b3e5fc;
    padding-bottom: 5px;
}
#explanation p {
    margin-bottom: 15px;
    line-height: 1.7;
}
#explanation ul {
    margin-bottom: 15px;
    padding-right: 20px; /* Adjust for RTL */
}
#explanation ul li {
     margin-bottom: 8px;
}

/* Animation for number updates */
@keyframes fadeNumber {
    from { opacity: 0.5; }
    to { opacity: 1; }
}
.fade-update {
    animation: fadeNumber 0.5s ease-out;
}

/* Simple loading/processing indicator (optional) */
.loading-indicator {
    display: inline-block;
    width: 1em;
    height: 1em;
    border: 2px solid #f3f3f3;
    border-top: 2px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-right: 5px;
    vertical-align: middle;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>

<div id="app">
    <h2>סימולציית מסחר בחוזים עתידיים על טמפרטורה</h2>

    <div id="game-state">
        <div><strong>עיר:</strong> <span id="city"></span></div>
        <div><strong>ימים לפקיעה:</strong> <span id="days-to-expiry"></span></div>
        <div><strong>תחזית נוכחית (ליום הפקיעה):</strong> <span id="current-forecast"></span>°C</div>
        <div><strong>סוג החוזה:</strong> תשלום אם הטמפרטורה בפועל ביום הפקיעה <span id="condition-text"></span> <span id="threshold"></span>°C</div>
        <div><strong>שווי החוזה בפקיעה (אם התנאי מתקיים):</strong> $<span id="payout"></span></div>
        <div><strong>מחיר שוק נוכחי לחוזה:</strong> $<span id="market-price"></span> <span id="price-change-indicator"></span></div>
        <div><strong>יתרה במזומן:</strong> $<span id="cash"></span></div>
        <div><strong>פוזיציה (חוזים בבעלותך):</strong> <span id="position"></span></div>
        <div><strong>שווי פוזיציה נוכחי:</strong> $<span id="position-value"></span></div>
    </div>

    <div id="trading-area">
        <h3>בצע מסחר</h3>
        <div>
            <label for="num-contracts">מספר חוזים:</label>
            <input type="number" id="num-contracts" value="1" min="1">
            <button id="buy-btn" class="sim-button">קנה</button>
            <button id="sell-btn" class="sim-button">מכור</button>
        </div>
        <div id="trade-message"></div>
    </div>

    <div id="controls">
        <button id="next-day-btn" class="sim-button">התקדם ליום הבא</button>
    </div>

    <div id="result">
        <h2>תוצאות הפקיעה</h2>
        <div>הטמפרטורה בפועל ביום הפקיעה הייתה: <span id="actual-temp" class="actual-temp"></span>°C</div>
        <div>תוצאת החוזה: <span id="contract-met"></span></div>
        <div>הסדר פוזיציה בפקיעה: $<span id="settlement-amount"></span></div>
        <div>רווח/הפסד כולל מהמסחר: $<span id="profit-loss"></span></div>
        <button id="reset-btn" class="sim-button">שחק שוב</button>
    </div>
</div>

<button id="toggle-explanation" class="sim-button">הצג / הסתר הסבר על חוזי מזג אוויר</button>

<div id="explanation">
    <h2>מה למדנו על חוזים עתידיים למזג אוויר?</h2>

    <h3>מה הם חוזים עתידיים (Futures Contracts)?</h3>
    <p>חוזה עתידי הוא הסכם לקנות או למכור "נכס" מסוים - שיכול להיות סחורה פיזית (חיטה, נפט), מכשיר פיננסי (מטבע, ריבית), או במקרה הייחודי שלנו - אירוע מזג אוויר ספציפי - במחיר שנקבע *היום*, אך עם מועד ביצוע ("פקיעה") *עתידי*. זהו כלי מרכזי בשווקים הפיננסיים לניהול סיכונים (גידור) ולהשקעה ספקולטיבית.</p>

    <h3>כיצד עובד שוק החוזים העתידיים על מזג אוויר?</h3>
    <p>בניגוד למסחר בחיטה, כאן סוחרים קונים ומוכרים חוזים שמשלמים סכום קבוע (למשל, 100$) אם תנאי מזג אוויר מסוים מתקיים במועד עתידי (למשל, טמפרטורה מעל סף מסוים ביום הפקיעה בעיר נתונה). מחיר החוזה בשוק משקף את ההסתברות הנתפסת על ידי כלל הסוחרים לכך שהתנאי יקרה. אם השוק מאמין שהסיכוי גבוה, המחיר יהיה קרוב ל-100$. אם הסיכוי נמוך, המחיר יתקרב ל-0$. הסימולציה שלנו מדגימה זאת: כשהתחזית מתעדכנת ומשתנה (ובכך משפיעה על הסתברות קרות התנאי), גם מחיר החוזה משתנה.</p>

    <h3>מי משתמש בחוזים אלו ולמה?</h3>
    <p>גורמים עסקיים רבים שרווחיהם מושפעים ישירות ממזג האוויר משתמשים בחוזים אלו כדי <strong>לגדר</strong> (להגן על) את עצמם מפני תנודות בלתי צפויות במזג האוויר:</p>
    <ul>
        <li><strong>חברות אנרגיה:</strong> חורף חם מפחית ביקוש לחימום; קיץ קר מפחית ביקוש לקירור. חברה יכולה לקנות חוזים שישלמו לה אם הטמפרטורות יהיו מתונות מהרגיל, וכך לקזז חלק מההפסד בהכנסותיה.</li>
        <li><strong>חברות חקלאיות ומשקיעים בתוצרת:</strong> בצורת, קרה, או גשמים עזים יכולים להרוס יבולים. חקלאי יכול לגדר סיכון זה.</li>
        <li><strong>חברות ביטוח:</strong> יכולות לגדר סיכון מפני אירועי מזג אוויר קיצוניים שיגרמו להן לתביעות רבות.</li>
        <li><strong>מפיקי אירועים תלויי מזג אוויר:</strong> פסטיבלים באוויר הפתוח, אתרי סקי, וכו', יכולים לגדר סיכון לגשם או חוסר שלג.</li>
    </ul>
    <p>בנוסף לגופים המגדרים, ישנם <strong>ספקולנטים</strong> - אלו שסוחרים בחוזים במטרה להרוויח מתחזיות טובות יותר משל השוק, או פשוט משינויים צפויים במחיר החוזה ככל שמתקבל מידע חדש (כמו עדכוני תחזית).</p>

    <h3>ההבדל בין גידור (Hedging) לספקולציה (Speculation)</h3>
    <p>נניח שאתם חברת גלידה. אתם חוששים מקיץ קר שבו המכירות ירדו. אתם יכולים "לגדר" את הסיכון על ידי קניית חוזי "טמפרטורה קרה" שישלמו לכם כסף אם הקיץ אכן יהיה קר. אם הקיץ קר, הרווח מחוזי מזג האוויר יקזז חלק מההפסד במכירות הגלידה. זהו <strong>גידור</strong>.</p>
    <p>לעומת זאת, אם אין לכם עסק גלידה, אבל אתם עוקבים אחרי תחזיות מזג האוויר ומאמינים שהשוק "מפספס" - לדעתכם הקיץ יהיה חם יותר ממה שהשוק חושב - אתם יכולים לקנות חוזי "טמפרטורה חמה" בתקווה שמחירם יעלה ככל שהתחזית החמה יותר תתממש, או כדי להרוויח את ה-100$ בפקיעה אם אכן יהיה חם. זהו <strong>ספקולציה</strong>.</p>

    <h3>כיצד ציפיות ומידע (כמו עדכוני תחזית) משפיעים על מחירי החוזים?</h3>
    <p>מחירי החוזים משקפים את הציפיות המצטברות של כלל הסוחרים בשוק לגבי ההסתברות שהתנאי יתקיים. ככל שמתקרבים למועד הפקיעה, התחזיות נהיות מדויקות יותר. עדכון תחזית שמעלה את הסיכוי לתנאי החוזה (למשל, תחזית שפתאום מראה טמפרטורה גבוהה יותר ביום הפקיעה) יגרום ליותר סוחרים לרצות לקנות את החוזה, מה שיעלה את מחירו. עדכון שמוריד את הסיכוי יגרום לירידת מחיר. הסימולציה מדגימה זאת: בכל יום שעובר, התחזית (ומכאן גם מחיר השוק) מתעדכנת ומתקרבת לטמפרטורה שתימדד בפועל.</p>

    <h3>סיכונים וסיכויים במסחר בחוזים על מזג אוויר.</h3>
    <p>הסיכויים: אם אתם מגדרים, תוכלו להפחית את ההפסדים הכספיים שלכם כתוצאה ממזג אוויר גרוע לעסק שלכם. אם אתם ספקולנטים, ישנה אפשרות לרווח משמעותי אם הצלחתם לחזות את מזג האוויר או את תנועת המחירים טוב יותר משל השוק.</p>
    <p>הסיכונים: מחירי החוזים יכולים להיות תנודתיים מאוד, במיוחד רחוק ממועד הפקיעה כשהתחזית אינה ודאית. אם טעיתם בתחזית שלכם או שהשוק נע בכיוון ההפוך ממה שציפיתם, אתם עלולים להפסיד את כל הכסף שהשקעתם בחוזים שקניתם (אם מחירם יורד ל-0$ בפקיעה) או לעמוד בפני "קריאת מרג'ין" והפסד גדול יותר אם מכרתם (עשיתם Short) חוזים שמחירם קפץ ל-100$ בפקיעה. זהו שוק מתוחכם שדורש הבנה וזהירות.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Game State Variables
        let initialCash = 10000;
        let cash = initialCash;
        let position = 0; // Positive for long (bought), negative for short (sold)
        let totalDays = 7; // Let's make it 7 days for more trading opportunities
        let daysToExpiry = totalDays;
        let city = "לונדון";
        let threshold = 25; // Celsius
        let payout = 100; // $ payout if condition is met
        let actualTemperature; // Set on game start, revealed on expiry
        let currentForecast; // Updates daily
        let marketPrice; // Updates daily, based on forecast and noise
        let previousMarketPrice = 0; // To track price changes
        const contractCondition = 'מעל'; // 'מעל'

        // DOM Elements
        const cityEl = document.getElementById('city');
        const daysToExpiryEl = document.getElementById('days-to-expiry');
        const currentForecastEl = document.getElementById('current-forecast');
        const conditionTextEl = document.getElementById('condition-text');
        const thresholdEl = document.getElementById('threshold');
        const payoutEl = document.getElementById('payout');
        const marketPriceEl = document.getElementById('market-price');
        const priceChangeIndicatorEl = document.getElementById('price-change-indicator');
        const cashEl = document.getElementById('cash');
        const positionEl = document.getElementById('position');
        const positionValueEl = document.getElementById('position-value'); // Added for mark-to-market
        const numContractsInput = document.getElementById('num-contracts');
        const buyBtn = document.getElementById('buy-btn');
        const sellBtn = document.getElementById('sell-btn');
        const nextDayBtn = document.getElementById('next-day-btn');
        const resultDiv = document.getElementById('result');
        const actualTempEl = document.getElementById('actual-temp');
        const contractMetEl = document.getElementById('contract-met');
        const settlementAmountEl = document.getElementById('settlement-amount'); // Added for settlement clarity
        const profitLossEl = document.getElementById('profit-loss');
        const resetBtn = document.getElementById('reset-btn');
        const tradeMessageEl = document.getElementById('trade-message');
        const tradingArea = document.getElementById('trading-area');
        const controlsArea = document.getElementById('controls');

        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');

        // --- Game Logic ---

        function initGame() {
            cash = initialCash;
            position = 0;
            daysToExpiry = totalDays;
            tradeMessageEl.textContent = ''; // Clear message
            tradeMessageEl.className = ''; // Clear classes

            // Generate actual temperature around the threshold, but with a bias towards one side
            // Let's make it slightly more likely to be above or below each game
            let bias = (Math.random() - 0.5) * 4; // Bias between -2 and 2
            actualTemperature = threshold + (Math.random() * 6 - 3) + bias; // Around threshold +/- 3, plus bias
            actualTemperature = Math.max(threshold - 5, Math.min(threshold + 5, actualTemperature)); // Keep it within a reasonable range around threshold

            // Generate initial forecast - less accurate, further from actual
            let initialForecastNoise = (Math.random() - 0.5) * 10; // Noise between -5 and 5
            currentForecast = actualTemperature + initialForecastNoise;
            // Clamp forecast to a wider but still reasonable range
            currentForecast = Math.max(threshold - 10, Math.min(threshold + 10, currentForecast));

            previousMarketPrice = 0; // Reset previous price for indicator
            updateMarketPrice(); // Calculate initial market price
            positionValueEl.textContent = (position * marketPrice).toFixed(2); // Initial position value is 0

            updateUI();
            resultDiv.style.display = 'none';
            tradingArea.style.display = 'block';
            controlsArea.style.display = 'block';
            nextDayBtn.disabled = false;
            resetBtn.style.display = 'none'; // Hide reset button initially
            resultDiv.className = ''; // Remove result classes
        }

        function updateUI() {
            cityEl.textContent = city;
            daysToExpiryEl.textContent = daysToExpiry;
            currentForecastEl.textContent = currentForecast.toFixed(1);
            conditionTextEl.textContent = contractCondition;
            thresholdEl.textContent = threshold;
            payoutEl.textContent = payout;

            // Update market price display with change indicator
            marketPriceEl.textContent = marketPrice.toFixed(2);
            if (previousMarketPrice !== 0) {
                if (marketPrice > previousMarketPrice) {
                    priceChangeIndicatorEl.innerHTML = '▲'; // Up arrow
                    priceChangeIndicatorEl.className = 'price-change-icon price-change-up';
                } else if (marketPrice < previousMarketPrice) {
                    priceChangeIndicatorEl.innerHTML = '▼'; // Down arrow
                    priceChangeIndicatorEl.className = 'price-change-icon price-change-down';
                } else {
                    priceChangeIndicatorEl.innerHTML = '—'; // No change
                    priceChangeIndicatorEl.className = 'price-change-icon';
                }
            } else {
                 priceChangeIndicatorEl.innerHTML = ''; // No indicator on first day
                 priceChangeIndicatorEl.className = '';
            }
             previousMarketPrice = marketPrice; // Store current price for next update

            // Update cash display with color
            cashEl.textContent = cash.toFixed(2);
            cashEl.className = ''; // Reset class
            if (cash > initialCash) cashEl.classList.add('positive');
            else if (cash < initialCash) cashEl.classList.add('negative');
            else cashEl.classList.add('neutral');


            positionEl.textContent = position;
            positionValueEl.textContent = (position * marketPrice).toFixed(2); // Update mark-to-market value


            // Disable trading if 0 days left (expiry) or if cash is insufficient for 1 contract
            if (daysToExpiry <= 0) {
                buyBtn.disabled = true;
                sellBtn.disabled = true;
                numContractsInput.disabled = true;
                nextDayBtn.disabled = true;
            } else {
                 // Check if can afford at least 1 contract to enable buy
                 buyBtn.disabled = cash < marketPrice;
                 sellBtn.disabled = false; // Always allow selling (including shorting)
                 numContractsInput.disabled = false;
                 nextDayBtn.disabled = false;
            }

            // Apply fade-update animation to changing elements
            [cashEl, positionEl, marketPriceEl, positionValueEl].forEach(el => {
                 el.classList.add('fade-update');
                 setTimeout(() => el.classList.remove('fade-update'), 600); // Remove class after animation
            });
             // Only animate forecast if it changed significantly
             if (Math.abs(currentForecast - parseFloat(currentForecastEl.textContent)) > 0.05) {
                  currentForecastEl.classList.add('fade-update');
                  setTimeout(() => currentForecastEl.classList.remove('fade-update'), 600);
             }

        }

        function updateForecast() {
            // Forecast becomes more accurate as days to expiry decrease
            // Move forecast closer to actual temp, reduce noise
            let accuracyFactor = 1 - (daysToExpiry / totalDays); // Goes from ~0 to 1
            let remainingGap = actualTemperature - currentForecast;

            // Smaller steps initially, larger steps closer to expiry
            let movementSpeed = 0.2 + accuracyFactor * 0.6; // Moves 20%-80% of remaining gap
            let forecastMovement = remainingGap * movementSpeed;

            // Noise decreases significantly as expiry nears
            let maxNoise = 3; // Max noise when daysToExpiry = totalDays
            let noise = (Math.random() - 0.5) * maxNoise * (daysToExpiry / totalDays + 0.1); // Added 0.1 to keep some noise even near expiry

            currentForecast = currentForecast + forecastMovement + noise;

            // Clamp forecast to a reasonable range around threshold
            currentForecast = Math.max(threshold - 8, Math.min(threshold + 8, currentForecast));
        }

        function updateMarketPrice() {
             // Price reflects perceived probability based on current forecast
             // For 'מעל' condition, higher forecast -> higher price
             // Use a sigmoid-like function mapping forecast deviation to probability (0-1)
             // Simple approach: Price is linear function of deviation from threshold, clamped 0-100
             // Deviation from threshold: forecast - threshold
             // Let's assume a difference of 5 degrees is significant
             let deviation = currentForecast - threshold;
             // Map deviation to a probability factor between 0 and 1
             // Sigmoid approximation: factor = 1 / (1 + exp(-k * deviation))
             // A simple linear map with clamping:
             let priceFactor = deviation * 10 + 50; // 0 at threshold-5, 100 at threshold+5
             priceFactor = Math.max(0, Math.min(100, priceFactor)); // Clamp between 0 and 100

             // Add random market noise, decreases as expiry nears
             let maxMarketNoise = 15; // Max noise further out
             let marketNoise = (Math.random() - 0.5) * maxMarketNoise * (daysToExpiry / totalDays + 0.1); // Noise decreases

             marketPrice = priceFactor + marketNoise;

             // Clamp price between 0.01 and 99.99 before expiry
             if (daysToExpiry > 0) {
                 marketPrice = Math.max(0.01, Math.min(99.99, marketPrice));
             } else {
                  // On expiry day, price is the payout if condition met, 0 otherwise
                  marketPrice = (actualTemperature > threshold) ? payout : 0;
             }
        }

        function showTradeMessage(message, type) {
            tradeMessageEl.textContent = message;
            tradeMessageEl.className = ''; // Clear previous classes
            tradeMessageEl.classList.add(type); // Add new class (success, error, info)
             tradeMessageEl.style.opacity = 1;
             setTimeout(() => {
                 tradeMessageEl.style.opacity = 0; // Start fade out
             }, 3000); // Message stays for 3 seconds
             setTimeout(() => {
                 tradeMessageEl.textContent = '';
                 tradeMessageEl.className = '';
                 tradeMessageEl.style.opacity = 1; // Reset opacity for next message
            }, 3500); // Clear message element completely after fade
        }


        function buyContracts() {
            const numToBuy = parseInt(numContractsInput.value);
            if (isNaN(numToBuy) || numToBuy <= 0) {
                 showTradeMessage('הכנס מספר חוזים תקין (מספר חיובי שלם).', 'info');
                 return;
            }
            const cost = numToBuy * marketPrice;

            if (cash >= cost) {
                cash -= cost;
                position += numToBuy;
                showTradeMessage(`קנית ${numToBuy} חוזים במחיר $${marketPrice.toFixed(2)} לחוזה. עלות כוללת: $${cost.toFixed(2)}.`, 'success');
                updateUI();
            } else {
                showTradeMessage(`אין מספיק מזומן לביצוע הקנייה. נדרש $${cost.toFixed(2)}, יש לך רק $${cash.toFixed(2)}.`, 'error');
            }
        }

        function sellContracts() {
             const numToSell = parseInt(numContractsInput.value);
             if (isNaN(numToSell) || numToSell <= 0) {
                 showTradeMessage('הכנס מספר חוזים תקין (מספר חיובי שלם).', 'info');
                 return;
             }
             const proceeds = numToSell * marketPrice;

             // Allow selling even if position is 0 or positive (short selling is allowed)
             cash += proceeds;
             position -= numToSell; // Position becomes negative for short
             showTradeMessage(`מכרת ${numToSell} חוזים במחיר $${marketPrice.toFixed(2)} לחוזה. תקבול כולל: $${proceeds.toFixed(2)}.`, 'success');

             updateUI();
        }

        function nextDay() {
            if (daysToExpiry <= 0) return; // Should be disabled by UI, but safety check

            daysToExpiry--;
            showTradeMessage('מתקדם ליום הבא...', 'info');
            // Add a small delay to simulate time passing
            nextDayBtn.disabled = true; // Disable button during transition
            buyBtn.disabled = true; // Disable trading during transition
            sellBtn.disabled = true;
            numContractsInput.disabled = true;


            setTimeout(() => {
                 if (daysToExpiry > 0) {
                     updateForecast();
                     updateMarketPrice();
                     updateUI();
                     showTradeMessage('התחזית והמחיר התעדכנו!', 'info');
                 } else {
                     // Last day reached - calculate expiry
                     updateMarketPrice(); // Update price one last time (it becomes the payout)
                     updateUI(); // Show final price (payout value or 0)
                     showTradeMessage('הגענו ליום הפקיעה!', 'info');
                     setTimeout(endGame, 1500); // Small delay before showing results
                 }
                 // Re-enable buttons after update, unless game ended
                 if (daysToExpiry > 0) {
                     nextDayBtn.disabled = false;
                     buyBtn.disabled = cash < marketPrice;
                     sellBtn.disabled = false;
                     numContractsInput.disabled = false;
                 }
            }, 1500); // 1.5 second delay for next day transition
        }

        function endGame() {
            tradingArea.style.display = 'none';
            controlsArea.style.display = 'none';
            resultDiv.style.display = 'block';
            tradeMessageEl.style.display = 'none'; // Hide trade message area

            actualTempEl.textContent = actualTemperature.toFixed(1);

            let contractActualOutcome = 0; // What a single contract pays out
            let conditionMet = false;

            if (contractCondition === 'מעל') {
                if (actualTemperature > threshold) {
                    contractActualOutcome = payout;
                    conditionMet = true;
                    contractMetEl.textContent = 'התנאי התקיים!';
                    contractMetEl.style.color = 'green';
                } else {
                    contractActualOutcome = 0;
                    contractMetEl.textContent = 'התנאי לא התקיים.';
                    contractMetEl.style.color = 'red';
                }
            }
            // Add other conditions here if needed

            // Calculate settlement based on final position and actual contract outcome
            // If pos > 0 (long): Receive pos * contractActualOutcome
            // If pos < 0 (short): Pay |pos| * contractActualOutcome
            let settlement = position * contractActualOutcome;

            settlementAmountEl.textContent = settlement.toFixed(2);

            // Apply settlement to cash
            cash += settlement;

            const profitLoss = cash - initialCash; // Compare final cash to starting cash

            profitLossEl.textContent = profitLoss.toFixed(2);
            profitLossEl.className = ''; // Reset class
            if (profitLoss > 0) {
                profitLossEl.classList.add('positive');
                 resultDiv.className = 'success'; // Green result box
                 contractMetEl.textContent += ' 🎉'; // Add emoji for fun
            } else if (profitLoss < 0) {
                profitLossEl.classList.add('negative');
                 resultDiv.className = 'loss'; // Red result box
                 contractMetEl.textContent += ' 😟'; // Add emoji for fun
            } else {
                 profitLossEl.classList.add('neutral');
                 resultDiv.className = 'neutral'; // Blue result box
            }


             resetBtn.style.display = 'inline-block';
             nextDayBtn.style.display = 'none';
        }

        function resetGame() {
            resultDiv.style.display = 'none';
            tradingArea.style.display = 'block';
            controlsArea.style.display = 'block';
            nextDayBtn.style.display = 'inline-block';
            resetBtn.style.display = 'none';
             tradeMessageEl.style.display = 'block'; // Show message area again
            initGame(); // Start a new game
        }

        function toggleExplanation() {
            if (explanationDiv.style.display === 'none') {
                explanationDiv.style.display = 'block';
                toggleExplanationBtn.textContent = 'הסתר הסבר על חוזי מזג אוויר';
            } else {
                explanationDiv.style.display = 'none';
                 toggleExplanationBtn.textContent = 'הצג / הסתר הסבר על חוזי מזג אוויר';
            }
        }

        // --- Event Listeners ---
        buyBtn.addEventListener('click', buyContracts);
        sellBtn.addEventListener('click', sellContracts);
        nextDayBtn.addEventListener('click', nextDay);
        resetBtn.addEventListener('click', resetGame);
        toggleExplanationBtn.addEventListener('click', toggleExplanation);

        // Initialize the game on page load
        initGame();
    });
</script>
```