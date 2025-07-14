---
title: "שוק ההימורים שמנבא את העתיד"
english_slug: prediction-markets-forecasting-future
category: "כלכלה התנהגותית"
tags: [שוקי חיזוי, חיזוי, כלכלה, קבלת החלטות, חוכמת ההמונים]
---
<p class="intro-text">האם קבוצה גדולה של אנשים אנונימיים יכולה לנבא אירועים עתידיים בדיוק גבוה יותר ממומחים? מסתבר שלפעמים כן, והכלי הוא "שוקי חיזוי" – זירת מסחר אינטראקטיבית שבה אנשים סוחרים ב"חוזים" המבוססים על תוצאות של אירועים עתידיים. בואו נתנסה בסימולטור שלנו כדי לראות איך זה עובד!</p>

<div id="app" class="prediction-market-simulator">
    <h2 class="simulator-title">🔮 סימולטור שוק חיזוי 🔮</h2>
    <div class="event-card">
        <div class="event-header">
            <h3>האירוע על הפרק:</h3>
            <span class="event-date">תאריך סגירת השוק: 31/12/2030</span>
        </div>
        <p id="event-text">האם חללית מאוישת תנחת בהצלחה על מאדים עד סוף שנת 2030?</p>
    </div>

    <div class="market-dashboard">
        <div class="info-box price-box">
            <h4>מחיר חוזה "כן":</h4>
            <p id="current-price" class="price-value">0.50 $</p>
             <span id="price-change-indicator" class="change-indicator"></span>
        </div>
        <div class="info-box balance-box">
            <h4>הכסף שלך:</h4>
            <p id="user-balance" class="balance-value">1000.00 $</p>
        </div>
         <div class="info-box holdings-box">
            <h4>חוזים שבידיך ("כן"):</h4>
            <p id="user-holdings" class="holdings-value">0</p>
        </div>
    </div>

    <div class="trade-section card">
        <h4>סחר בחוזים:</h4>
        <div class="trade-controls">
            <input type="number" id="trade-quantity" value="1" min="1" max="100" step="1" class="trade-input">
            <label for="trade-quantity" class="trade-label">כמות חוזים</label>
            <button id="buy-button" class="trade-button buy-button">קנה "כן"</button>
            <button id="sell-button" class="trade-button sell-button">מכור "כן"</button>
        </div>
         <p id="trade-feedback" class="trade-feedback"></p>
    </div>

    <div class="price-history-section card">
        <h4>📈 היסטוריית מחיר (מעודכן):</h4>
        <div id="price-chart" class="price-history-chart">
            <!-- Dynamic price history list -->
            <p class="history-placeholder">המחיר ישתנה עם המסחר...</p>
        </div>
    </div>

    <div class="simulation-controls card">
         <h4>סיום השוק (לצורך הדגמה):</h4>
         <div class="outcome-buttons">
             <button id="simulate-outcome-yes" class="simulate-button outcome-yes">סמול: האירוע התרחש ("כן") ✅</button>
             <button id="simulate-outcome-no" class="simulate-button outcome-no">סמול: האירוע לא התרחש ("לא") ❌</button>
         </div>
         <p id="outcome-message" class="outcome-message" style="display: none;"></p>
    </div>
</div>

<button id="toggle-explanation" class="explanation-toggle-button">🔍 רוצה להבין טוב יותר? הצג הסבר מלא על שוקי חיזוי 🔍</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר מלא: שוקי חיזוי - חוכמת ההמונים בפעולה</h2>

    <h3>מהם שוקי חיזוי?</h3>
    <p>דמיינו בורסה, לא של מניות וחברות, אלא של... עתיד! שוקי חיזוי (Prediction Markets) הם בדיוק כאלה – פלטפורמות מסחר מקוונות שבהן סוחרים ב"חוזים" שהערך הסופי שלהם תלוי בתוצאה של אירוע עתידי. במקום פשוט להביע דעה ("אני חושב שזה יקרה"), המשתתפים "מהמרים" כסף על התוצאה. המחיר של כל חוזה בשוק לא מבטא רק דעה, אלא את האומדן הכספי המצטבר של כל המשתתפים לגבי ההסתברות שהאירוע יקרה. בדרך כלל, המחיר הזה נע בין 0 ל-1 דולר (או 0% ל-100%), ומספר לנו כמה "בטוח" השוק בתוצאה מסוימת.</p>

    <h3>איך זה עובד בפועל?</h3>
    <p>בואו ניקח שוק שמנסה לנבא האם סרט מסוים יזכה באוסקר לסרט הטוב ביותר. נוצרים שני סוגי חוזים: "כן" (הסרט יזכה) ו"לא" (הסרט לא יזכה). נניח שאתם קונים חוזה "כן" במחיר של 0.75 דולר. זה אומר שהשוק כרגע מעריך שהסיכוי שהסרט יזכה הוא 75%.<br>
    *   **אם הסרט אכן זוכה:** החוזה "כן" הופך להיות שווה 1 דולר. הרווחתם 0.25 דולר על כל חוזה שקניתם.<br>
    *   **אם הסרט לא זוכה:** החוזה "כן" הופך להיות חסר ערך (שווה 0 דולר). הפסדתם את 0.75 דולר שהשקעתם.<br>
    באותו אופן, אם הייתם קונים חוזה "לא" במחיר של 0.25 דולר, הייתם מרוויחים אם הסרט לא יזכה ומפסידים אם יזכה. מנגנון הקנייה והמכירה המתמיד גורם למחירים להתעדכן בזמן אמת, וכך המחיר הנוכחי של החוזה הוא למעשה "תחזית ההסתברות" העדכנית של השוק, שנובעת מאיחוד הידע והציפיות של כלל המשתתפים.</p>

    <h3>למה אומרים שהם מדויקים? כוחה של חוכמת ההמונים</h3>
    <p>הדיוק המפתיע של שוקי חיזוי נובע מכמה סיבות מרכזיות:</p>
    <ul>
        <li>**איגום מידע בקנה מידה ענק:** כל סוחר בשוק מביא איתו פיסת מידע ייחודית – ניתוח, שמועה, ידע פנימי, או אפילו סתם "תחושת בטן" מבוססת. השוק, באמצעות מנגנון המחירים, מצליח לאסוף את כל פיסות המידע המבוזרות הללו ולאחד אותן לתחזית אחת מרוכזת ומדויקת יותר מכל תחזית בודדת.</li>
        <li>**תמריצים כספיים חזקים:** כאן לא מדובר בלהביע דעה בסקר אקראי. המשתתפים שמים את הכסף שלהם על השולחן! מי שתחזיותיו נכונות - מרוויח, ומי שטועה - מפסיד. התמריץ הכלכלי הזה דוחף את המשתתפים להשקיע מאמץ אמיתי באיסוף וניתוח מידע, ולהיות כנים ואובייקטיביים ככל האפשר בתחזיות שלהם. זהו הבדל קריטי לעומת סקרים או ניתוחי מומחים שעשויים להיות מוטים.</li>
        <li>**תגובה מיידית למידע חדש:** ברגע שמתפרסם מידע חדש רלוונטי (למשל, סקר פתאומי או ידיעה חדשותית), סוחרים מגיבים לו מיד על ידי קנייה או מכירה של חוזים. זה גורם למחירים להתעדכן כמעט בזמן אמת, ולתחזית של השוק להיות תמיד מעודכנת ביותר.</li>
    </ul>
    <p>מחקרים רבים, ובמיוחד הניסיון של שוקי חיזוי פוליטיים ידועים כמו ה-Iowa Electronic Markets, הראו שוב ושוב ששוקי חיזוי יכולים לנבא תוצאות אירועים (כמו בחירות לנשיאות ארה"ב) בדיוק גבוה יותר מסקרים מסורתיים ואף יותר ממרבית המומחים.</p>

    <h3>איפה משתמשים בזה היום?</h3>
    <p>הפוטנציאל של שוקי חיזוי רחב ומגוון:</p>
    <ul>
        <li>**פוליטיקה:** חיזוי תוצאות בחירות (השימוש המוכר ביותר), הסתברות לחקיקת חוקים מסוימים, סיכויים להסכמים בינלאומיים.</li>
        <li>**עסקים ותאגידים:** חיזוי הצלחת השקת מוצרים חדשים, מועדי סיום פרויקטים, תחזיות מכירות מדויקות יותר, סיכויים למיזוגים ורכישות. חברות ענק כמו גוגל ומיקרוסופט ניסו (בחלקן בהצלחה) להשתמש בשוקי חיזוי פנימיים כדי לשפר את קבלת ההחלטות שלהן.</li>
        <li>**מדע וטכנולוגיה:** חיזוי מועדי פריצות דרך טכנולוגיות, הצלחת ניסויים קליניים, התקדמות במחקר.</li>
        <li>**אירועים כלליים:** חיזוי זוכי פרסים (אוסקר, נובל), תוצאות אירועי ספורט גדולים, אפילו תחזיות מזג אוויר ארוכות טווח.</li>
    </ul>

     <h3>האם יש מגבלות? לא הכול ורוד...</h3>
     <p>למרות היתרונות, שוקי חיזוי אינם כלי מושלם:</p>
     <ul>
         <li>**סחירות נמוכה:** בשוקים קטנים מדי, או על אירועים אזוטריים שמעניינים מעט אנשים, כמות המשתתפים והמסחר עשויה להיות נמוכה מדי. זה פוגע ביכולת השוק לאגום מספיק מידע ולקבוע מחיר (תחזית) מדויק.</li>
         <li>**רגישות למניפולציה:** שוקים קטנים עלולים להיות חשופים יותר לניסיונות של משתתפים בעלי הון גדול להשפיע על המחיר (התחזית) למטרותיהם שלהם.</li>
         <li>**אירועים קיצוניים או עמומים:** חיזוי אירועים נדירים במיוחד (עם סיכויים קרובים ל-0% או 100%) או אירועים שהתוצאה שלהם אינה מוגדרת היטב עלול להיות פחות מדויק.</li>
         <li>**רגולציה:** במדינות רבות, שוקי חיזוי כספיים נחשבים להימורים ועשויים להיות אסורים או מוגבלים מאוד רגולטורית, מה שמקשה על התפתחותם וזמינותם לקהל הרחב.</li>
     </ul>
     <p>בסופו של דבר, שוקי חיזוי הם כלי רב עוצמה ויכולים להיות מדויקים להפליא, במיוחד כאשר הם מתבססים על חוכמתם של המון סוחרים בעלי תמריצים כספיים ברורים. הסימולטור שלפניכם נועד לתת לכם טעימה אינטראקטיבית מהכוח הזה.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // App Variables
        let userBalance = 1000.00;
        let userHoldings = 0; // Number of "Yes" contracts held
        let currentPrice = 0.50; // Price of one "Yes" contract (0 to 1)
        // Adjusted sensitivity: User trades move price more, simulated trades move it less/randomly
        const userPriceImpact = 0.005; // How much price changes per contract traded by USER
        const simulatedPriceImpact = 0.0005; // How much price changes per contract traded by SIMULATION
        const simulatedTradingInterval = 1500; // ms (faster simulation)
        const minSimulatedVolume = 1;
        const maxSimulatedVolume = 5; // Simulated volume can vary
        const simulatedBiasFactor = 0.1; // How much the current price influences simulated trading bias (0 to 1)
        const priceHistory = [];
        const maxPriceHistory = 8; // Max entries to show
        let lastPrice = currentPrice; // To track change direction

        // DOM Elements
        const balanceElement = document.getElementById('user-balance');
        const holdingsElement = document.getElementById('user-holdings');
        const priceElement = document.getElementById('current-price');
        const priceChangeIndicator = document.getElementById('price-change-indicator');
        const quantityInput = document.getElementById('trade-quantity');
        const buyButton = document.getElementById('buy-button');
        const sellButton = document.getElementById('sell-button');
        const tradeFeedbackElement = document.getElementById('trade-feedback');
        const priceHistoryElement = document.getElementById('price-chart');
        const simulateOutcomeYesButton = document.getElementById('simulate-outcome-yes');
        const simulateOutcomeNoButton = document.getElementById('simulate-outcome-no');
        const outcomeMessageElement = document.getElementById('outcome-message');

        // Explanation Toggle
        const explanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        explanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            explanationButton.textContent = isHidden ? '🙈 הסתר הסבר מלא' : '🔍 רוצה להבין טוב יותר? הצג הסבר מלא על שוקי חיזוי 🔍';
             if (!isHidden) { // Scroll to explanation when shown
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else { // Scroll back to top of simulator when hidden
                 document.getElementById('app').scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });

        // Update UI Function
        function updateUI() {
            balanceElement.textContent = `${userBalance.toFixed(2)} $`;
            holdingsElement.textContent = userHoldings;

            // Animate price change indicator
            if (currentPrice > lastPrice) {
                 priceChangeIndicator.textContent = '▲';
                 priceChangeIndicator.className = 'change-indicator price-up';
            } else if (currentPrice < lastPrice) {
                 priceChangeIndicator.textContent = '▼';
                 priceChangeIndicator.className = 'change-indicator price-down';
            } else {
                 priceChangeIndicator.textContent = '▪';
                 priceChangeIndicator.className = 'change-indicator';
            }
             lastPrice = currentPrice; // Update last price for next cycle

            priceElement.textContent = currentPrice.toFixed(2) + ' $'; // Add $ symbol

            // Update price history display (list)
            const historyHtml = priceHistory.map(p => {
                 const changeClass = p.change > 0 ? 'history-price-up' : (p.change < 0 ? 'history-price-down' : '');
                 const changeIndicator = p.change > 0 ? '▲' : (p.change < 0 ? '▼' : '▪');
                 return `<p class="history-item ${changeClass}">${p.price.toFixed(2)} ${changeIndicator}</p>`;
            }).join('');
            priceHistoryElement.innerHTML = historyHtml || '<p class="history-placeholder">המחיר ישתנה עם המסחר...</p>';
            priceHistoryElement.scrollTop = priceHistoryElement.scrollHeight; // Auto-scroll to bottom

            // Update button states based on balance/holdings
            const quantity = parseInt(quantityInput.value, 10) || 0;
            buyButton.disabled = userBalance < quantity * currentPrice || quantity <= 0;
            sellButton.disabled = userHoldings < quantity || quantity <= 0;
        }

        // Add Price to History
        function addPriceToHistory(price) {
             const change = price - (priceHistory.length > 0 ? priceHistory[priceHistory.length - 1].price : currentPrice);
            priceHistory.push({ price: price, change: change });
            if (priceHistory.length > maxPriceHistory) {
                priceHistory.shift(); // Remove oldest entry
            }
        }

         // Show trade feedback message
         function showTradeFeedback(message, isError = false) {
             tradeFeedbackElement.textContent = message;
             tradeFeedbackElement.className = `trade-feedback ${isError ? 'error' : 'success'}`;
             tradeFeedbackElement.style.opacity = '1';
             setTimeout(() => {
                 tradeFeedbackElement.style.opacity = '0';
             }, 3000); // Hide after 3 seconds
         }

        // Simulate Market Activity (simplified dynamic model)
        function simulateTrading() {
            // Bias the simulated trading based on current price
            // If price is low (<0.5), more likely to "buy yes" (pushing price up)
            // If price is high (>0.5), more likely to "sell yes" (pushing price down)
            // Use the simulatedBiasFactor to control how strong this effect is.
             const bias = (0.5 - currentPrice) * simulatedBiasFactor + 0.5; // Value between 0 and 1
             const isBuyingYes = Math.random() < bias;

             const quantity = Math.floor(Math.random() * (maxSimulatedVolume - minSimulatedVolume + 1)) + minSimulatedVolume;

            if (isBuyingYes) {
                currentPrice += simulatedPriceImpact * quantity * (1 + Math.random() * 0.5); // Small random boost
            } else {
                currentPrice -= simulatedPriceImpact * quantity * (1 + Math.random() * 0.5); // Small random boost
            }

            // Keep price strictly between 0.01 and 0.99 to avoid getting stuck at limits
            currentPrice = Math.max(0.01, Math.min(0.99, currentPrice));

             addPriceToHistory(currentPrice);
            updateUI();
        }

        let simulationTimer = setInterval(simulateTrading, simulatedTradingInterval);


        // Handle User Trade (Buy)
        buyButton.addEventListener('click', () => {
            const quantity = parseInt(quantityInput.value, 10);
            if (isNaN(quantity) || quantity <= 0) {
                showTradeFeedback('אנא הכנס כמות חוקית.', true);
                return;
            }

            const cost = quantity * currentPrice;

            if (userBalance >= cost) {
                userBalance -= cost;
                userHoldings += quantity;
                // Price moves up significantly when buying Yes contracts
                currentPrice += userPriceImpact * quantity;
                 currentPrice = Math.max(0.01, Math.min(0.99, currentPrice)); // Clamp

                addPriceToHistory(currentPrice);
                updateUI();
                 showTradeFeedback(`קנית ${quantity} חוזים ב- ${cost.toFixed(2)}$. יתרה: ${userBalance.toFixed(2)}$.`);
            } else {
                showTradeFeedback('אין לך מספיק כסף לביצוע עסקה זו.', true);
            }
        });

        // Handle User Trade (Sell)
        sellButton.addEventListener('click', () => {
            const quantity = parseInt(quantityInput.value, 10);
            if (isNaN(quantity) || quantity <= 0) {
                showTradeFeedback('אנא הכנס כמות חוקית.', true);
                return;
            }

            if (userHoldings >= quantity) {
                const revenue = quantity * currentPrice;
                userBalance += revenue;
                userHoldings -= quantity;
                 // Price moves down significantly when selling Yes contracts
                currentPrice -= userPriceImpact * quantity;
                 currentPrice = Math.max(0.01, Math.min(0.99, currentPrice)); // Clamp

                addPriceToHistory(currentPrice);
                updateUI();
                 showTradeFeedback(`מכרת ${quantity} חוזים ב- ${revenue.toFixed(2)}$. יתרה: ${userBalance.toFixed(2)}$.`);
            } else {
                showTradeFeedback('אין לך מספיק חוזים למכירה.', true);
            }
        });

        // Handle Outcome Simulation
        function handleOutcome(didEventHappen) {
             clearInterval(simulationTimer); // Stop market simulation

            let payout = 0;
            let message = '';
            let messageClass = '';

            if (didEventHappen) {
                // Yes contracts settle at 1.0, No contracts settle at 0.0
                 payout = userHoldings * 1.0; // Only "Yes" contracts are tracked in this simple demo
                 message = `🥳 האירוע התרחש! ("${document.getElementById('event-text').textContent}") החוזים שלך שווים 1$ ליחידה.`;
                 messageClass = 'outcome-message win';
                 // If we had "No" contracts, they would settle at 0.
            } else {
                // Yes contracts settle at 0.0, No contracts settle at 1.0
                payout = userHoldings * 0.0; // "Yes" contracts are worthless
                 message = `😞 האירוע לא התרחש. החוזים שלך חסרי ערך.`;
                 messageClass = 'outcome-message lose';
                 // If we had "No" contracts, they would settle at 1.0.
            }

            userBalance += payout;
            userHoldings = 0; // Contracts are settled

            updateUI();

            outcomeMessageElement.textContent = message;
            outcomeMessageElement.className = messageClass;
            outcomeMessageElement.style.display = 'block';

            // Disable trade buttons after outcome
            buyButton.disabled = true;
            sellButton.disabled = true;
             simulateOutcomeYesButton.disabled = true;
             simulateOutcomeNoButton.disabled = true;
             quantityInput.disabled = true;

             // Clear history display
             priceHistoryElement.innerHTML = '<p class="history-placeholder">השוק נסגר.</p>';

             // Show final balance clearly
             balanceElement.classList.add('final-balance');
        }

        simulateOutcomeYesButton.addEventListener('click', () => handleOutcome(true));
        simulateOutcomeNoButton.addEventListener('click', () => handleOutcome(false));

        // Initial setup
        addPriceToHistory(currentPrice);
        updateUI(); // Initial UI render

        // Initial quantity input validation/update button state
        quantityInput.addEventListener('input', updateUI); // Re-check button state on input change
    });
</script>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #6c757d; /* Gray */
        --success-color: #28a745; /* Green */
        --danger-color: #dc3545; /* Red */
        --warning-color: #ffc107; /* Yellow */
        --info-color: #17a2b8; /* Cyan */
        --light-color: #f8f9fa; /* Light gray */
        --dark-color: #343a40; /* Dark gray */
        --background-color: #e9ecef; /* Lighter background */
        --card-background: #ffffff;
        --border-color: #dee2e6;
        --shadow-color: rgba(0, 0, 0, 0.08);
         --price-up: #28a745; /* Green for price up */
         --price-down: #dc3545; /* Red for price down */
    }

    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: var(--dark-color);
        background-color: var(--background-color);
        padding: 20px;
    }

    .intro-text {
        max-width: 800px;
        margin: 0 auto 30px auto;
        font-size: 1.1em;
        color: var(--dark-color);
        text-align: center;
    }

    .prediction-market-simulator {
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        background-color: var(--light-color);
        border-radius: 12px;
        box-shadow: 0 8px 16px var(--shadow-color);
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3, h4 {
        color: var(--dark-color);
        margin-bottom: 15px;
    }

     .simulator-title {
         text-align: center;
         color: var(--primary-color);
         margin-bottom: 30px;
         font-size: 2em;
     }

    .card {
        margin-bottom: 25px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--card-background);
        box-shadow: 0 4px 8px var(--shadow-color);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

     .card:hover {
         transform: translateY(-3px);
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.12);
     }

    .event-card .event-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 10px;
    }

    .event-card h3 {
        margin: 0;
        color: var(--primary-color);
    }

    .event-card .event-date {
        font-size: 0.9em;
        color: var(--secondary-color);
    }

    .market-dashboard {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 15px; /* Space between info boxes */
        margin-bottom: 25px;
    }

    .info-box {
        flex: 1; /* Allow boxes to grow */
        min-width: 180px; /* Minimum width before wrapping */
        text-align: center;
        padding: 15px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--card-background);
        box-shadow: 0 2px 4px var(--shadow-color);
    }

    .info-box h4 {
        margin-bottom: 8px;
        color: var(--secondary-color);
        font-size: 1em;
    }

    .info-box p {
        font-size: 1.4em;
        font-weight: bold;
        margin: 0;
    }

     .price-box .price-value {
         color: var(--primary-color); /* Default price color */
         position: relative; /* For indicator positioning */
         display: inline-block;
     }

     .change-indicator {
         position: absolute;
         top: -5px; /* Adjust position as needed */
         left: -15px; /* Adjust position as needed */
         font-size: 0.8em;
         transition: color 0.3s ease;
     }

     .price-up { color: var(--price-up); }
     .price-down { color: var(--price-down); }

     .balance-box .balance-value { color: var(--success-color); }
     .holdings-box .holdings-value { color: var(--info-color); }

     .balance-value.final-balance {
         font-size: 1.8em;
         color: var(--dark-color);
         animation: pulse-balance 1s ease-in-out forwards;
     }

     @keyframes pulse-balance {
         0% { transform: scale(1); color: var(--success-color); }
         50% { transform: scale(1.05); color: var(--primary-color); }
         100% { transform: scale(1); color: var(--dark-color); }
     }


    .trade-section .trade-controls {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
    }

    .trade-input {
        padding: 10px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        width: 80px;
        text-align: center;
        font-size: 1em;
    }

     .trade-label {
         font-size: 1em;
         color: var(--secondary-color);
     }

    .trade-button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .trade-button:disabled {
         opacity: 0.5;
         cursor: not-allowed;
     }

    .buy-button {
        background-color: var(--success-color);
        color: white;
    }

    .buy-button:hover:not(:disabled) {
         background-color: #218838; /* Darker green */
         transform: translateY(-1px);
    }

    .sell-button {
        background-color: var(--danger-color);
        color: white;
    }
     .sell-button:hover:not(:disabled) {
        background-color: #c82333; /* Darker red */
         transform: translateY(-1px);
    }

     .trade-feedback {
         margin-top: 15px;
         padding: 10px;
         border-radius: 5px;
         font-weight: bold;
         opacity: 0;
         transition: opacity 0.5s ease;
     }

     .trade-feedback.success {
         background-color: #d4edda; /* Light green */
         color: #155724; /* Dark green text */
     }

      .trade-feedback.error {
         background-color: #f8d7da; /* Light red */
         color: #721c24; /* Dark red text */
     }


    .price-history-chart {
        max-height: 150px; /* Increased height */
        overflow-y: auto;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        padding: 10px;
        margin-top: 10px;
        background-color: var(--light-color);
        font-family: 'Courier New', monospace; /* Monospaced font for prices */
        font-size: 0.9em;
    }

    .price-history-chart .history-placeholder {
        text-align: center;
        color: var(--secondary-color);
        margin: 20px;
    }

    .price-history-chart .history-item {
        margin: 3px 0;
        padding: 2px 5px;
        border-bottom: 1px dashed #eee;
    }

     .price-history-chart .history-item:last-child {
         border-bottom: none;
     }

     .history-price-up {
         color: var(--price-up);
         font-weight: bold;
     }
     .history-price-down {
         color: var(--price-down);
         font-weight: bold;
     }


     .simulation-controls .outcome-buttons {
         display: flex;
         gap: 10px;
         flex-wrap: wrap;
     }

     .simulate-button {
         flex: 1; /* Distribute width */
         min-width: 200px;
         padding: 12px 15px;
         border: none;
         border-radius: 5px;
         cursor: pointer;
         font-size: 1em;
         font-weight: bold;
         transition: background-color 0.3s ease, transform 0.1s ease;
     }

     .simulate-button:disabled {
         opacity: 0.5;
         cursor: not-allowed;
     }

     .outcome-yes {
         background-color: var(--warning-color);
         color: var(--dark-color);
     }

     .outcome-yes:hover:not(:disabled) {
         background-color: #e0a800; /* Darker yellow */
         transform: translateY(-1px);
     }

      .outcome-no {
         background-color: var(--secondary-color);
         color: white;
     }

      .outcome-no:hover:not(:disabled) {
         background-color: #545b62; /* Darker gray */
         transform: translateY(-1px);
     }


    .outcome-message {
        margin-top: 20px;
        font-weight: bold;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 1.1em;
        display: none; /* Hidden by default */
    }

    .outcome-message.win {
        background-color: var(--success-color);
        color: white;
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
    }

     .outcome-message.lose {
        background-color: var(--danger-color);
        color: white;
        box-shadow: 0 4px 8px rgba(220, 53, 69, 0.3);
    }


    .explanation-toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: 1px solid var(--primary-color);
        border-radius: 5px;
        background-color: var(--primary-color);
        color: white;
        font-weight: bold;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
    }

     .explanation-toggle-button:hover {
         background-color: #0056b3;
         border-color: #0056b3;
         transform: translateY(-1px);
     }

    .explanation-section {
        max-width: 800px;
        margin: 30px auto;
        padding: 30px;
        border-top: 3px solid var(--primary-color);
        background-color: var(--card-background);
        border-radius: 8px;
        box-shadow: 0 8px 16px var(--shadow-color);
        direction: rtl;
        text-align: right;
    }

    .explanation-section h2 {
        color: var(--primary-color);
        margin-bottom: 20px;
        text-align: center;
    }

     .explanation-section h3 {
         color: var(--dark-color);
         margin-top: 20px;
         margin-bottom: 10px;
         border-bottom: 1px solid var(--border-color);
         padding-bottom: 5px;
     }

    .explanation-section p {
        line-height: 1.7;
        margin-bottom: 15px;
        color: var(--dark-color);
    }

     .explanation-section ul {
         margin-bottom: 15px;
         padding-right: 20px;
     }

     .explanation-section li {
         margin-bottom: 8px;
     }


     /* Responsive adjustments */
     @media (max-width: 600px) {
         .prediction-market-simulator, .explanation-section, .intro-text {
             padding: 20px;
         }

         .market-dashboard {
             flex-direction: column;
             align-items: center;
         }

         .info-box {
             width: 100%;
             min-width: auto;
         }

         .trade-section .trade-controls {
             flex-direction: column;
             align-items: stretch;
         }

         .trade-input, .trade-label, .trade-button {
             width: 100%;
             text-align: center;
         }

          .trade-label { text-align: right; margin-bottom: 5px;}

         .simulate-button {
             width: 100%;
             min-width: auto;
         }
     }

</style>