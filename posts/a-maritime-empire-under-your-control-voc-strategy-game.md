---
title: "אימפריה ימית בשליטתך: מסע הסחר הגדול של ה-VOC"
english_slug: a-maritime-empire-under-your-control-voc-strategy-game
category: "היסטוריה וכלכלה"
tags:
  - VOC
  - חברת הודו המזרחית ההולנדית
  - היסטוריה קולוניאלית
  - מסחר בינלאומי
  - אסטרטגיה עסקית
---
# אימפריה ימית בשליטתך: מסע הסחר הגדול של ה-VOC

צא למסע סוער אל לב המאה ה-17, תקופת פריחתה של חברת הודו המזרחית ההולנדית (VOC). האם תוכל לנווט את החברה האדירה הזו בין סערות, שודדי ים, יריבים אירופאים ומושלים מקומיים, ולהפוך אותה לאימפריה מסחרית חסרת תקדים? גורלה של ה-VOC בידיך!

<div id="game-area">
    <h2 class="section-title">נהל את ה-VOC - המאה ה-17</h2>
    <div id="status" class="game-panel">
        <h3 class="panel-title">מצב האימפריה</h3>
        <p class="status-item"><strong>שנה:</strong> <span id="turn">1</span></p>
        <p class="status-item"><strong>אוצר החברה:</strong> <span id="cash">1,000,000</span> גילדן <span class="cash-indicator"></span></p>
        <p class="status-item"><strong>צי הספינות:</strong> <span id="ships">10</span> ספינות <span class="ships-indicator"></span></p>
        <p class="status-item"><strong>השם הטוב:</strong> <span id="reputation">גבוה</span> <span class="reputation-indicator"></span></p>
        <p class="status-item"><strong>מלאי תבלינים נדירים:</strong> <span id="spice-inventory">0</span> יחידות</p>
        <p class="status-item"><strong>מלאי משי וחרסינה:</strong> <span id="textile-inventory">0</span> יחידות</p>
    </div>

    <div id="decisions" class="game-panel">
        <h3 class="panel-title">החלטות אסטרטגיות לשנה הקרובה</h3>
        <div class="decision-group">
            <label for="route"><strong>היעד למסע הגדול של הצי:</strong></label>
            <select id="route">
                <option value="east-indies">איי התבלינים (מזרח הרחוק - סיכון/רווח <span class="highlight-high">גבוה</span>)</option>
                <option value="india">תת היבשת ההודית (טקסטיל/חרסינה - סיכון/רווח <span class="highlight-medium">בינוני</span>)</option>
                <option value="south-africa">נקודת האספקה בכף (דרום אפריקה - סיכון/רווח <span class="highlight-low">נמוך</span>)</option>
            </select>
        </div>
        <div class="decision-group">
            <label for="ships-to-send"><strong>גודל הצי הנשלח למסע:</strong></label>
            <input type="number" id="ships-to-send" min="0" value="5"> (מתוך <span id="available-ships">10</span> ספינות זמינות)
        </div>
         <div class="decision-group">
            <label for="investment"><strong>השקעה באבטחת נתיבי סחר וקשרים דיפלומטיים:</strong></label>
            <select id="investment">
                <option value="low">נמוכה (<span class="highlight-risk">סיכון גבוה</span> לאירועים שליליים)</option>
                <option value="medium">בינונית (איזון)</option>
                <option value="high">גבוהה (<span class="highlight-safe">הפחתת סיכונים</span>, <span class="highlight-cost">הגדלת עלויות</span>)</option>
            </select>
        </div>
        <button onclick="processTurn()">סיים שנה, צא למסע וקבל תוצאות</button>
    </div>

    <div id="results" class="game-panel">
        <h3 class="panel-title">דו"ח השנה החולפת</h3>
        <div id="events-log"></div>
    </div>

    <div id="game-over" class="game-panel">
        <h2 class="section-title">מסע ה-VOC הסתיים...</h2>
        <p id="game-over-message"></p>
        <button onclick="restartGame()">צא שוב למסע!</button>
    </div>
</div>

<button id="toggle-explanation" class="info-button">הצג מידע היסטורי על ה-VOC</button>

<div id="explanation" class="info-panel">
    <h2 class="section-title">אודות חברת הודו המזרחית ההולנדית (VOC)</h2>
    <p>חברת הודו המזרחית ההולנדית (Vereenigde Oostindische Compagnie - VOC) שנוסדה ב-1602, לא הייתה עוד חברת סחר רגילה. היא הייתה תאגיד פורץ דרך ובעל עוצמה חסרת תקדים, שקיבל מהפרלמנט ההולנדי סמכויות כשל מדינה לכל דבר. ה-VOC יכלה לנהל משא ומתן, לכרות בריתות, להקים צבא וצי פרטיים, לבנות מצודות, לטבוע מטבעות ואף לנהל מלחמות בשמה!</p>

    <h3>המטרות והאתגרים הגדולים</h3>
    <p>ה-VOC קמה מאיחוד של חברות סחר הולנדיות קטנות יותר, במטרה אחת מרכזית: השגת מונופול על הסחר בתבלינים היקרים מאיי אינדונזיה של ימינו (איי מאלוקו). התבלינים כמו פלפל שחור, ציפורן, אגוז מוסקט ומייס, היו מצרך מבוקש ויקר באירופה, והבטיחו רווחי עתק. אך הדרך אליהם הייתה רצופת סכנות: מסעות ימיים ארוכים ומסוכנים עקב סערות, מחלות ושודדי ים; תחרות עזה מצד מעצמות אירופאיות אחרות כמו פורטוגל ואנגליה; והצורך לנווט במערכות פוליטיות מורכבות מול שליטים מקומיים באסיה.</p>

    <h3>על כוח, עושר וצדדים אפלים</h3>
    <p>כוחה וסמכויותיה הייחודיות איפשרו ל-VOC להקים רשת ענפה של תחנות סחר, מצודות ומושבות, החל מנקודת האספקה החשובה בכף התקווה הטובה (לימים קייפטאון) ועד למאחזים מבוצרים באסיה. היא שלטה על נתיבי סחר מרכזיים, ולא היססה להשתמש בכוח צבאי כדי להבטיח את המונופול שלה ולדכא התנגדות מקומית. לצד העושר האדיר שהצטבר בקופתה והתפקיד שמילאה בעיצוב הכלכלה העולמית, פעולותיה כללו גם כיבושים אלימים, ניצול אוכלוסיות מקומיות ואף מעשי טבח, שהטילו צל כבד על מורשתה.</p>

    <h3>הדרך אל השקיעה</h3>
    <p>לאחר למעלה מ-150 שנות פעילות, החלה ה-VOC לשקוע בסוף המאה ה-18. ניהול כושל, שחיתות פנימית, עלויות צבאיות גבוהות (במיוחד עקב מלחמות מול בריטניה), ושינויים בשוקי הסחר הגלובליים, כרסמו בהדרגה בעוצמתה. בשנת 1799, חדלת פירעון, הועברו נכסיה לידי המדינה ההולנדית, והיא חדלה מלהתקיים. למרות סופה, ה-VOC נותרה דוגמה מרתקת לכוחו (ולעתים קרובות האפל) של תאגיד כלכלי בקנה מידה גלובלי.</p>
</div>

<script>
    const gameArea = document.getElementById('game-area');
    const statusDiv = document.getElementById('status');
    const decisionsDiv = document.getElementById('decisions');
    const resultsDiv = document.getElementById('results');
    const eventsLog = document.getElementById('events-log');
    const gameOverDiv = document.getElementById('game-over');
    const gameOverMessage = document.getElementById('game-over-message');

    const turnSpan = document.getElementById('turn');
    const cashSpan = document.getElementById('cash');
    const shipsSpan = document.getElementById('ships');
    const reputationSpan = document.getElementById('reputation');
    const spiceInventorySpan = document.getElementById('spice-inventory');
    const textileInventorySpan = document.getElementById('textile-inventory');
    const availableShipsSpan = document.getElementById('available-ships');

    const routeSelect = document.getElementById('route');
    const shipsToSendInput = document.getElementById('ships-to-send');
    const investmentSelect = document.getElementById('investment');

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    // Indicators for animation/visual feedback
    const cashIndicator = document.querySelector('.cash-indicator');
    const shipsIndicator = document.querySelector('.ships-indicator');
    const reputationIndicator = document.querySelector('.reputation-indicator');

    let gameState = {};
    const startingCash = 1500000; // More generous starting cash
    const startingShips = 15; // More ships
    const maxTurns = 15; // Survive 15 turns
    const minReputation = 15; // Game over if reputation drops below this

    const baseCosts = {
        shipMaintenance: 4000, // Cost per ship per turn
        investment: { low: 15000, medium: 40000, high: 80000 }
    };

    const routeModifiers = {
        'east-indies': {
            baseRevenuePerShip: 90000, // High potential revenue
            goodsPerShip: 7, // Units of spice
            baseSuccessChance: 0.6, // Base chance
            riskMultiplier: { low: 1.5, medium: 1.0, high: 0.6 }, // Investment reduces risk
            piracyChance: { low: 0.3, medium: 0.1, high: 0.02 }, // Piracy risk
            reputationEffect: { success: 7, failure: -7 } // Reputation change
        },
        'india': {
            baseRevenuePerShip: 45000, // Medium potential revenue
            goodsPerShip: 10, // Units of textile/porcelain
            baseSuccessChance: 0.8, // Base chance
            riskMultiplier: { low: 1.2, medium: 0.9, high: 0.5 }, // Investment reduces risk
            conflictChance: { low: 0.25, medium: 0.1, high: 0.03 }, // Conflict risk (influenced by low reputation)
             reputationEffect: { success: 4, failure: -5 } // Reputation change
        },
        'south-africa': {
            baseRevenuePerShip: 15000, // Low potential revenue
            goodsPerShip: 0, // Mainly resupply, minimal trade goods
            baseSuccessChance: 0.95, // High success chance
            riskMultiplier: { low: 1.0, medium: 0.8, high: 0.4 }, // Investment reduces risk
            reputationEffect: { success: 2, failure: -1 } // Reputation change
        }
    };

    let marketIndex = 1.0; // Starting market index (1.0 means base price)


    function startGame() {
        gameState = {
            turn: 1,
            cash: startingCash,
            ships: startingShips,
            reputation: 60, // starting reputation
            spiceInventory: 0,
            textileInventory: 0,
            gameOver: false
        };
        marketIndex = 1.0; // Reset market index
        updateUI();
        eventsLog.innerHTML = '<p class="event-neutral">ברוך הבא, מנהל נכבד! אימפריית ה-VOC מצפה להנחייתך. לרשותך <span class="highlight-cash">' + gameState.cash.toLocaleString() + '</span> גילדן וצי של <span class="highlight-ships">' + gameState.ships + '</span> ספינות.</p>';
        gameOverDiv.style.display = 'none';
        gameArea.style.display = 'block';
        // Ensure game panels are visible on start/restart
        statusDiv.style.display = 'block';
        decisionsDiv.style.display = 'block';
        resultsDiv.style.display = 'block';

        explanationDiv.style.display = 'none'; // Ensure explanation is hidden on start/restart
        toggleExplanationButton.textContent = 'הצג מידע היסטורי על ה-VOC'; // Reset button text
    }

    function updateUI() {
        turnSpan.textContent = gameState.turn;
        cashSpan.textContent = gameState.cash.toLocaleString();
        shipsSpan.textContent = gameState.ships;
        reputationSpan.textContent = getReputationText(gameState.reputation);
        reputationSpan.className = 'reputation-level ' + getReputationClass(gameState.reputation); // Add class for styling
        spiceInventorySpan.textContent = gameState.spiceInventory;
        textileInventorySpan.textContent = gameState.textileInventory;
        availableShipsSpan.textContent = gameState.ships;
        shipsToSendInput.max = gameState.ships;
        shipsToSendInput.value = Math.min(shipsToSendInput.value, gameState.ships);

        if (gameState.gameOver) {
            gameArea.style.display = 'none';
            gameOverDiv.style.display = 'block';
        }
    }

    function getReputationText(rep) {
        if (rep > 85) return 'אגדי';
        if (rep > 70) return 'מצוין';
        if (rep > 50) return 'טוב';
        if (rep > 30) return 'בינוני';
        if (rep > 15) return 'נמוך';
        return 'גרוע';
    }

    function getReputationClass(rep) {
        if (rep > 85) return 'rep-legendary';
        if (rep > 70) return 'rep-excellent';
        if (rep > 50) return 'rep-good';
        if (rep > 30) return 'rep-medium';
        if (rep > 15) return 'rep-low';
        return 'rep-terrible';
    }

    function addEventLog(message, type = 'neutral') {
        const p = document.createElement('p');
        p.className = 'event-' + type;
        p.innerHTML = `<span>שנה ${gameState.turn -1}:</span> ${message}`;
        eventsLog.prepend(p); // Add to top
        // Limit log size for performance/clarity (optional)
        // while (eventsLog.children.length > 20) {
        //     eventsLog.removeChild(eventsLog.lastChild);
        // }
         eventsLog.scrollTop = 0; // Scroll to top to see newest event
    }


    function processTurn() {
        if (gameState.gameOver) return;

        const selectedRoute = routeSelect.value;
        const shipsToSend = parseInt(shipsToSendInput.value);
        const investmentLevel = investmentSelect.value;

        if (shipsToSend > gameState.ships || shipsToSend < 0 || isNaN(shipsToSend)) {
            alert('מספר ספינות לא חוקי.');
            return;
        }
         if (shipsToSend === 0) {
             alert('לא שלחת אף ספינה למסע! עליך לשלוח לפחות ספינה אחת.');
             return;
         }


        // Start turn calculations
        let turnRevenue = 0;
        let shipsLost = 0;
        let cashChange = 0; // Represents net change from costs and minor events
        let reputationChange = 0;
        let goodsAcquired = { spice: 0, textile: 0 };
        let eventsSummary = []; // Collect event messages

        // Apply fixed costs (investment, maintenance for *all* ships)
        cashChange -= baseCosts.investment[investmentLevel];
        cashChange -= gameState.ships * baseCosts.shipMaintenance;
         addEventLog(`הוצאות קבועות לשנה: <span class="highlight-cost">${baseCosts.investment[investmentLevel].toLocaleString()}</span> גילדן (השקעה) + <span class="highlight-cost">${(gameState.ships * baseCosts.shipMaintenance).toLocaleString()}</span> גילדן (אחזקת צי).`, 'neutral');


        // Simulate market fluctuation (random between 0.8 and 1.2, influenced slightly by previous index)
        marketIndex = Math.max(0.7, Math.min(1.3, marketIndex + (Math.random() - 0.5) * 0.3)); // Fluctuate between 0.7 and 1.3
        addEventLog(`שוקי אירופה: שערי הסחר נעים סביב <span class="highlight-market">${(marketIndex * 100).toFixed(0)}%</span> מהממוצע.`, marketIndex > 1.05 ? 'positive' : (marketIndex < 0.95 ? 'negative' : 'neutral'));


        // Simulate route outcomes per ship sent
        const route = routeModifiers[selectedRoute];
        let successfulTrips = 0;
        let shipsEncounteringRisk = 0; // Track ships encountering non-piracy risk

        for (let i = 0; i < shipsToSend; i++) {
            let shipOutcome = 'success'; // Default outcome

            // Check for major risks (storm, conflict, etc.) first
            let riskFactor = route.riskMultiplier[investmentLevel] * (1 + (100 - gameState.reputation) / 200); // Low reputation increases risk
            if (Math.random() < (route.baseSuccessChance * (gameState.reputation/100)) * (1/riskFactor)) { // Success check includes reputation and risk
                // Ship is broadly successful (didn't encounter major disaster)
                successfulTrips++;
            } else {
                 // Ship encountered issues or failed to trade effectively
                 shipOutcome = 'failed';
                 shipsEncounteringRisk++; // This ship might be lost or just unsuccessful
            }
        }

         // Resolve outcomes based on successful trips and risk encounters
         let actualShipsLost = 0;
         let shipsReturnedEmpty = 0;

         // Piracy/Conflict resolution based on investment level and number of risky ships
         const totalRiskChance = (selectedRoute === 'india' ? route.conflictChance[investmentLevel] * (100 - gameState.reputation) / 100 : route.piracyChance[investmentLevel]);

         if (shipsEncounteringRisk > 0 && Math.random() < totalRiskChance) {
             const lostDueToEvent = Math.min(shipsEncounteringRisk, Math.floor(Math.random() * (shipsEncounteringRisk * 0.8)) + 1); // Lose some percentage of risky ships
              actualShipsLost += lostDueToEvent;
             shipsEncounteringRisk -= lostDueToEvent; // Remaining risky ships just failed trade
              reputationChange -= route.reputationEffect.failure; // Negative impact
              if(selectedRoute === 'east-indies') {
                  eventsSummary.push(`<p class="event-negative">נתיבי התבלינים היו סוערים! התקפת שודדי ים או סערה עזה טרפה <span class="highlight-loss">${lostDueDueEvent}</span> ספינות בדרך!</p>`);
                  cashChange -= lostDueToEvent * Math.floor(Math.random() * 30000 + 10000); // Lose some cargo/cash
             } else if (selectedRoute === 'india') {
                 eventsSummary.push(`<p class="event-negative">עימותים קשים באזור הודו! <span class="highlight-loss">${lostDueDueEvent}</span> ספינות אבדו בהיתקלויות עם כוחות עוינים.</p>`);
                 reputationChange -= route.reputationEffect.failure * 1.5; // Conflict hits harder
                 cashChange -= lostDueToEvent * Math.floor(Math.random() * 40000 + 15000); // Lose more cargo/cash
             } else { // South Africa - less dramatic
                 eventsSummary.push(`<p class="event-negative">אירוע מצער בכף: <span class="highlight-loss">${lostDueDueEvent}</span> ספינות לא חזרו מסיבות שאינן ברורות.</p>`);
             }
         }

        // Remaining ships that didn't have a "successfulTrip" and weren't lost are considered "returned empty" or with minimal value
        shipsReturnedEmpty = shipsToSend - successfulTrips - actualShipsLost;
        if (shipsReturnedEmpty > 0) {
             eventsSummary.push(`<p class="event-neutral">${shipsReturnedEmpty} ספינות חזרו ללא מטען משמעותי עקב תקלות או תנאי שוק קשים.</p>`);
        }


        // Calculate revenue from successful trips and goods acquired
        turnRevenue = successfulTrips * route.baseRevenuePerShip * marketIndex;
        if (route.goodsPerShip > 0) { // Only acquire goods on relevant routes
            const goods = successfulTrips * route.goodsPerShip;
             if(selectedRoute === 'east-indies') goodsAcquired.spice = goods;
             else goodsAcquired.textile = goods;
             eventsSummary.push(`<p class="event-positive">${successfulTrips} ספינות השלימו את המסע בהצלחה! נרכשו <span class="highlight-goods">${goods}</span> יחידות של <span class="highlight-positive">${selectedRoute === 'east-indies' ? 'תבלינים נדירים' : 'משי וחרסינה'}</span>.</p>`);
        } else {
             eventsSummary.push(`<p class="event-positive">${successfulTrips} ספינות השלימו את המסע בהצלחה! נתיב זה התמקד באספקה וברווחים קטנים מהמסחר המקומי.</p>`);
        }

         // Add reputation change from route success/failure
         if (successfulTrips > shipsToSend / 2) {
             reputationChange += route.reputationEffect.success;
         } else if (successfulTrips < shipsToSend / 4 && shipsToSend > 0) {
              reputationChange += route.reputationEffect.failure;
         }


        // General random events (less tied to routes)
         if (Math.random() < 0.15 * (1 + (100-gameState.reputation)/100) && investmentLevel === 'low') { // Increased chance with low reputation/investment
             const corruptionLoss = Math.floor(Math.random() * 80000 + 20000);
             cashChange -= corruptionLoss;
             reputationChange -= 8;
             eventsSummary.push(`<p class="event-negative">שחיתות בצמרת החברה באמסטרדם! נגרם הפסד כספי של <span class="highlight-loss">${corruptionLoss.toLocaleString()}</span> גילדן ופגיעה במוניטין.</p>`);
         }
         if (Math.random() < 0.1 * (1 + (100-gameState.reputation)/100) && gameState.ships > actualShipsLost) { // Only if there are ships left
            if (Math.random() > (investmentLevel === 'high' ? 0.9 : (investmentLevel === 'medium' ? 0.7 : 0.4))) { // Investment reduces positive event chance slightly (focus on risk reduction)
                 const bonusCash = Math.floor(Math.random() * 100000 + 50000);
                 cashChange += bonusCash;
                 reputationChange += 5;
                 eventsSummary.push(`<p class="event-positive">הזדמנות סחר נדירה! קשרים טובים נשאו פרי והביאו לרווח בלתי צפוי של <span class="highlight-gain">${bonusCash.toLocaleString()}</span> גילדן.</p>`);
            }
         }


        // Apply changes
        const initialCash = gameState.cash;
        const initialShips = gameState.ships;
        const initialReputation = gameState.reputation;

        gameState.cash += turnRevenue + cashChange;
        gameState.ships -= actualShipsLost;
        gameState.spiceInventory += goodsAcquired.spice;
        gameState.textileInventory += goodsAcquired.textile;
        gameState.reputation = Math.max(0, Math.min(100, gameState.reputation + reputationChange));
        gameState.turn++;

         // Add summary to log
         addEventLog(`סיכום השנה: הכנסות מסחר מהיעד שנבחר: <span class="highlight-gain">${turnRevenue.toLocaleString()}</span> גילדן. ספינות שאבדו במסע: <span class="highlight-loss">${actualShipsLost}</span>. שינוי נטו באוצר (כולל הוצאות ואירועים): <span class="${(turnRevenue + cashChange) >= 0 ? 'highlight-gain' : 'highlight-loss'}">${(turnRevenue + cashChange).toLocaleString()}</span> גילדן. שינוי בשם הטוב: ${reputationChange > 0 ? '+' : ''}${reputationChange}.`, 'summary');
         eventsSummary.reverse().forEach(msg => addEventLog(msg, msg.includes('event-positive') ? 'positive' : (msg.includes('event-negative') ? 'negative' : 'neutral'))); // Add specific events before summary


        // Animate indicators (simple pulsing for now, could be expanded with JS animation library)
        animateIndicator(cashIndicator, gameState.cash - initialCash);
        animateIndicator(shipsIndicator, initialShips - gameState.ships); // ships lost is a negative change
        animateIndicator(reputationIndicator, gameState.reputation - initialReputation);


        // Check game over conditions
        if (gameState.cash <= 0) {
            gameState.gameOver = true;
            gameOverMessage.innerHTML = `אוצר החברה התרוקן! לאחר <span class="highlight-loss">${gameState.turn - 1}</span> שנים, ה-VOC פשטה רגל. לא הצלחת לאזן בין ההוצאות העצומות והסיכונים המרובים לרווחי המסחר.`;
        } else if (gameState.ships <= 0) {
             gameState.gameOver = true;
             gameOverMessage.innerHTML = `כל ספינות הצי טבעו או אבדו בים! המסחר הגלובלי הפך לבלתי אפשרי. סוף הדרך של ה-VOC לאחר <span class="highlight-loss">${gameState.turn - 1}</span> שנים.`;
        } else if (gameState.reputation < minReputation) {
             gameState.gameOver = true;
             gameOverMessage.innerHTML = `השם הטוב של החברה התרסק! אף גורם לא מוכן לסחור איתכם והתקוממויות פורצות בכל תחנה. ה-VOC קרסה תחת נטל היריבות והעוינות לאחר <span class="highlight-loss">${gameState.turn - 1}</span> שנים.`;
        } else if (gameState.turn > maxTurns) {
             gameState.gameOver = true;
             gameOverMessage.innerHTML = `**ברכות על הצלחתך!** ניהלת את אימפריית ה-VOC ביד רמה במשך <span class="highlight-positive">${maxTurns}</span> שנים סוערות. בתום התקופה, מעמד החברה איתן: <br> אוצר - <span class="highlight-cash">${gameState.cash.toLocaleString()}</span> גילדן <br> צי - <span class="highlight-ships">${gameState.ships}</span> ספינות <br> מוניטין - <span class="highlight-positive">${getReputationText(gameState.reputation)}</span>. <br> ה-VOC נותרת הכוח המסחרי הגדול בעולם!`;
        }

        updateUI();
         // Scroll log back to top after adding new events
         eventsLog.scrollTop = 0;
    }

    function animateIndicator(element, change) {
        element.textContent = change > 0 ? '▲' : (change < 0 ? '▼' : ''); // Show arrow
        if (change > 0) {
            element.className = element.className.replace(' negative', '') + ' positive';
        } else if (change < 0) {
             element.className = element.className.replace(' positive', '') + ' negative';
        } else {
             element.className = element.className.replace(' positive', '').replace(' negative', '');
        }
        element.style.opacity = 1;
        setTimeout(() => {
            element.style.opacity = 0; // Fade out the indicator
             element.textContent = ''; // Hide arrow after fading
             element.className = element.className.replace(' positive', '').replace(' negative', ''); // Remove classes
        }, 1500); // Adjust timing for animation
    }


    function restartGame() {
        startGame();
    }

    toggleExplanationButton.addEventListener('click', function() {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר מידע היסטורי על ה-VOC';
            // Optionally, scroll to explanation
            // explanationDiv.scrollIntoView({ behavior: 'smooth' });
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג מידע היסטורי על ה-VOC';
        }
    });

    // Start the game when the page loads
    startGame();

</script>

<style>
    /* --- General Styles --- */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Hebrew support */
        text-align: right; /* Hebrew support */
        background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* Subtle gradient background */
        color: #333;
    }

    h1, h2, h3 {
        color: #004d40; /* Dark teal */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2.5em;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    h2.section-title {
        border-bottom: 2px solid #00838f; /* Blue-teal border */
        padding-bottom: 5px;
        margin-bottom: 20px;
         color: #006064; /* Stronger teal */
    }

    h3.panel-title {
        color: #006064;
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 1px solid #b2ebf2;
        padding-bottom: 5px;
    }

    /* --- Game Area Styles --- */
    #game-area {
        max-width: 900px;
        margin: 0 auto 20px auto;
        background-color: #ffffff;
        border: 1px solid #b2ebf2;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-radius: 12px;
        padding: 30px;
        display: grid;
        grid-template-areas:
            "status decisions"
            "results results";
        grid-template-columns: 1fr 1fr;
        gap: 30px;
    }

    .game-panel {
        border: 1px solid #e0f7fa;
        border-radius: 8px;
        padding: 20px;
        background-color: #f5f5f5; /* Light grey panel background */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

    #status { grid-area: status; }
    #decisions { grid-area: decisions; }
    #results { grid-area: results; grid-column: span 2; } /* Results span both columns */


    /* --- Status Panel --- */
    #status p {
        margin-bottom: 10px;
        font-size: 1.1em;
        border-bottom: 1px dashed #cfd8dc;
        padding-bottom: 8px;
         display: flex; /* Align text and indicator */
         justify-content: space-between; /* Push indicator to end */
    }
     #status p:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }
      #status strong { color: #006064; }

    /* Reputation Styling */
    .reputation-level {
        font-weight: bold;
    }
    .rep-legendary { color: #4caf50; } /* Green */
    .rep-excellent { color: #8bc34a; } /* Light Green */
    .rep-good { color: #ffeb3b; } /* Yellow */
    .rep-medium { color: #ff9800; } /* Orange */
    .rep-low { color: #ff5722; } /* Deep Orange */
    .rep-terrible { color: #f44336; } /* Red */

     /* Indicator Animation */
     .cash-indicator, .ships-indicator, .reputation-indicator {
         display: inline-block;
         width: 15px;
         text-align: center;
         opacity: 0; /* Start hidden */
         transition: opacity 0.5s ease-in-out;
         font-weight: bold;
     }
     .cash-indicator.positive, .reputation-indicator.positive { color: #4CAF50; } /* Green for gain */
     .cash-indicator.negative, .reputation-indicator.negative { color: #f44336; } /* Red for loss */
     .ships-indicator.positive { color: #f44336; } /* Red for ships lost */
     .ships-indicator.negative { color: #4CAF50; } /* Green for ships gained (if implemented) - currently only lose */


    /* --- Decisions Panel --- */
    .decision-group {
        margin-bottom: 15px;
        padding-bottom: 15px;
        border-bottom: 1px dashed #cfd8dc;
    }
     .decision-group:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }

    #decisions label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #006064;
        font-size: 1.05em;
    }

    #decisions select,
    #decisions input[type="number"] {
        width: calc(100% - 22px); /* Adjust width considering padding/border */
        padding: 10px;
        margin-right: 0; /* Remove margin-right */
        border-radius: 5px;
        border: 1px solid #b0bec5; /* Light grey-blue border */
        font-size: 1em;
        background-color: #eceff1; /* Very light blue-grey */
    }

    #decisions input[type="number"] {
         width: 80px; /* Fixed width for number input */
         text-align: center;
    }

    .highlight-high { color: #d32f2f; font-weight: bold; } /* Red */
    .highlight-medium { color: #fbc02d; font-weight: bold; } /* Yellow */
    .highlight-low { color: #388e3c; font-weight: bold; } /* Green */
    .highlight-risk { color: #d32f2f; font-weight: bold; } /* Red */
    .highlight-safe { color: #388e3c; font-weight: bold; } /* Green */
    .highlight-cost { color: #c2185b; font-weight: bold; } /* Pink-Red for costs */


    /* --- Results Panel --- */
    #results h3 {
        margin-bottom: 10px;
    }

    #events-log {
        max-height: 250px; /* Increased height */
        overflow-y: auto;
        border-top: 1px solid #b2ebf2;
        padding-top: 15px;
        margin-top: 10px;
         scrollbar-width: thin;
        scrollbar-color: #00838f #e0f7fa;
    }
     #events-log::-webkit-scrollbar { width: 8px; }
     #events-log::-webkit-scrollbar-track { background: #e0f7fa; border-radius: 10px; }
     #events-log::-webkit-scrollbar-thumb { background-color: #00838f; border-radius: 10px; border: 2px solid #e0f7fa; }


    #events-log p {
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px dashed #cfd8dc;
        font-size: 0.95em;
        line-height: 1.5;
    }
     #events-log p:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }
     #events-log p span:first-child { /* Year stamp */
         font-weight: bold;
         color: #004d40;
         margin-left: 8px;
         white-space: nowrap; /* Prevent wrapping */
     }


     /* Event message types */
     .event-positive { color: #1b5e20; /* Dark green */ }
     .event-negative { color: #c62828; /* Dark red */ }
     .event-neutral { color: #455a64; /* Blue grey */ }
     .event-summary { color: #004d40; font-weight: bold; } /* Dark teal */

     /* Highlighting specific values within events */
     .highlight-cash { color: #2e7d32; font-weight: bold; } /* Green for cash */
     .highlight-ships { color: #0277bd; font-weight: bold; } /* Blue for ships */
     .highlight-gain { color: #2e7d32; font-weight: bold; } /* Green for gains */
     .highlight-loss { color: #c62828; font-weight: bold; } /* Red for losses */
     .highlight-goods { color: #fbc02d; font-weight: bold; } /* Yellow for goods */
      .highlight-market { color: #00838f; font-weight: bold; } /* Blue-teal for market */


    /* --- Buttons --- */
    button {
        cursor: pointer;
        background-color: #00838f; /* Blue-teal */
        color: white;
        border: none;
        padding: 12px 25px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 1em;
        margin-top: 15px;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    button:hover {
        background-color: #006064; /* Darker blue-teal */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
     button:active {
         transform: scale(0.98); /* Press effect */
     }

    #toggle-explanation {
         background-color: #0277bd; /* Darker blue */
         display: block; /* Make it a block button */
         width: fit-content; /* Fit width to content */
         margin: 20px auto; /* Center block button */
         padding: 10px 20px;
         font-size: 0.9em;
         box-shadow: none; /* Less prominent shadow */
    }
     #toggle-explanation:hover {
         background-color: #01579b; /* Even darker blue */
          box-shadow: none;
     }


    /* --- Game Over Styles --- */
     #game-over {
        text-align: center;
        padding: 40px;
        border: 2px solid #e57373; /* Light red border */
        background-color: #ffebee; /* Very light red background */
        border-radius: 12px;
        margin: 20px auto;
        max-width: 600px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
     }

     #game-over h2 {
         color: #c62828; /* Dark red */
         margin-bottom: 20px;
     }

    #game-over p {
        font-size: 1.2em;
        margin-bottom: 25px;
        line-height: 1.6;
        color: #333;
    }

     #game-over button {
         background-color: #546e7a; /* Blue grey */
         margin-top: 0;
     }
      #game-over button:hover {
         background-color: #37474f; /* Dark blue grey */
     }

    /* --- Explanation Styles --- */
    #explanation {
        margin-top: 20px;
        padding: 30px;
        border: 1px solid #b2ebf2;
        background-color: #e0f7fa; /* Very light blue-teal background */
        border-radius: 8px;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #004d40; /* Dark teal text */
    }

    #explanation h2, #explanation h3 {
        text-align: right;
        color: #004d40;
    }

    #explanation p {
        margin-bottom: 15px;
        line-height: 1.7;
    }


    /* --- Responsive Design --- */
    @media (max-width: 768px) {
        #game-area {
            grid-template-areas:
                "status"
                "decisions"
                "results";
            grid-template-columns: 1fr;
            gap: 20px;
            padding: 20px;
        }

        #results {
             grid-column: span 1; /* Reset span for single column layout */
        }

        #decisions select,
        #decisions input[type="number"] {
             width: calc(100% - 22px); /* Full width minus padding */
             margin-bottom: 10px; /* Add space below inputs */
             display: block; /* Make them blocks */
        }
         #decisions input[type="number"] {
             width: 100px; /* Adjust width for mobile */
             display: inline-block; /* Allow next text on same line */
              margin-bottom: 0;
         }

         #decisions label {
             margin-bottom: 5px; /* Reduce space below labels */
         }

         button {
             width: 100%; /* Full width buttons */
             margin-right: 0;
             margin-left: 0;
         }

        #toggle-explanation {
             width: 100%;
        }
         #game-over {
             padding: 20px;
         }
          #game-over p {
              font-size: 1em;
          }
    }

</style>
```