---
title: "מנהל פארק הספארי: המאבק בציד בלתי חוקי"
english_slug: safari-park-manager-the-fight-against-illegal-poaching
category: "ניהול ועסקים / ניהול"
tags: [ציד בלתי חוקי, שימור טבע, ניהול משאבים, אקולוגיה, קבלת החלטות, סימולציה, משחק חינוכי]
---
# מנהל פארק הספארי: המאבק בציד בלתי חוקי

ברוכים הבאים לפארק הספארי! גורלם של מאות בעלי חיים נדירים מונח על כתפיכם. האם תצליחו להגן עליהם מידי ציידים חסרי רחמים במשך עשור קריטי? זה ידרוש יותר מסתם רצון טוב - תצטרכו לתכנן בקפידה, להקצות משאבים בחוכמה, ולהתמודד עם תוצאות החלטותיכם. צאו למשימה וגלו את מורכבות האתגר.

<div id="safari-app">
    <h2 class="game-title">סימולציית ניהול פארק הספארי</h2>

    <div id="game-status">
        <h3>מצב נוכחי:</h3>
        <p class="status-item"><span class="status-label">שנה:</span> <span id="current-year" class="status-value">1</span> / 10</p>
        <p class="status-item"><span class="status-label">תקציב נוכחי:</span> $<span id="current-budget" class="status-value budget">0</span></p>
        <div id="animal-populations" class="status-section">
             <p class="status-item"><span class="status-label">אוכלוסיית פילים 🐘:</span> <span id="elephants" class="status-value population">0</span></p>
            <p class="status-item"><span class="status-label">אוכלוסיית קרנפים 🦏:</span> <span id="rhinos" class="status-value population">0</span></p>
            <p class="status-item"><span class="status-label">אוכלוסיית זברות 🦓:</span> <span id="zebras" class="status-value population">0</span></p>
        </div>
         <p class="status-item"><span class="status-label">פקחים זמינים (בסיס):</span> <span id="available-rangers" class="status-value">0</span></p>
    </div>

    <div id="allocation-section">
        <h3>הקצאת משאבים לשנה <span id="next-year-display">הבאה</span>:</h3>
         <p class="allocation-tip">הקצו משאבים בצורה אסטרטגית כדי להילחם בציד ולשמור על חיות הבר. שימו לב לתקציב!</p>
        <div class="resource-allocation">
            <label for="allocate-rangers">פקחים לסיורים <span class="cost">($5000 לפקח/שנה)</span>:</label>
            <input type="number" id="allocate-rangers" min="0" value="0" class="resource-input">
        </div>
         <div class="resource-allocation">
            <label for="allocate-surveillance">ציוד מעקב <span class="cost">($10000 ליחידה/שנה)</span>:</label>
            <input type="number" id="allocate-surveillance" min="0" value="0" class="resource-input">
        </div>
         <div class="resource-allocation">
            <label for="allocate-community">תוכניות קהילה וחינוך <span class="cost">($20000 לתוכנית/שנה)</span>:</label>
            <input type="number" id="allocate-community" min="0" value="0" class="resource-input">
        </div>
         <div class="resource-allocation">
            <label for="allocate-fences">תחזוקת גדרות <span class="cost">($15000 לקטע/שנה)</span>:</label>
            <input type="number" id="allocate-fences" min="0" value="0" class="resource-input">
        </div>
        <div id="budget-warning" class="warning-message" style="display: none;">אין מספיק תקציב להקצאה זו!</div>
        <button id="next-year-btn">התקדם לשנה הבאה</button>
    </div>

    <div id="results-section" class="hidden">
        <h3>תוצאות השנה <span id="current-year-results"></span>:</h3>
         <p class="status-item"><span class="status-label">השקעה כוללת השנה:</span> $<span id="yearly-spend" class="status-value spend">0</span></p>
        <div class="results-summary">
            <p><span class="status-label">אירועי ציד שנמנעו (הערכה):</span> <span id="poaching-prevented" class="status-value prevented">0</span></p>
            <p><span class="status-label">אירועי ציד שאירעו בפועל:</span> <span id="poaching-occurred" class="status-value occurred">0</span></p>
        </div>
        <div class="animal-results status-section">
            <h4>חיות שניצודו:</h4>
            <ul>
                <li><span class="status-label">פילים 🐘:</span> <span id="elephants-poached" class="status-value poached">0</span></li>
                <li><span class="status-label">קרנפים 🦏:</span> <span id="rhinos-poached" class="status-value poached">0</span></li>
                <li><span class="status-label">זברות 🦓:</span> <span id="zebras-poached" class="status-value poached">0</span></li>
            </ul>
             <h4>שינוי באוכלוסיות (כולל רבייה והשפעת ציד):</h4>
             <ul>
                <li><span class="status-label">פילים 🐘:</span> <span id="elephants-change" class="status-value change">0</span></li>
                <li><span class="status-label">קרנפים 🦏:</span> <span id="rhinos-change" class="status-value change">0</span></li>
                <li><span class="status-label">זברות 🦓:</span> <span id="zebras-change" class="status-value change">0</span></li>
            </ul>
        </div>
    </div>

     <div id="game-over" class="hidden">
        <h3 id="game-over-message"></h3>
        <button id="restart-btn">התחל מחדש</button>
    </div>
</div>

<button id="toggle-explanation">הצג הסבר מורחב</button>

<div id="explanation" class="hidden">
    <h2>הסבר מורחב: המאבק בציד בלתי חוקי</h2>

    <p>סימולציה זו מספקת הצצה מפושטת לאתגרים המורכבים העומדים בפני מנהלי שמורות טבע ופארקי ספארי ברחבי העולם. כעת נצלול לעומק הבעיה והפתרונות האפשריים.</p>

    <h3>צד אפל ליפי הטבע: היקף הבעיה וקשריה לפשיעה מאורגנת</h3>
    <p>ציד בלתי חוקי אינו סתם "ציד אסור". זוהי תעשייה עולמית אכזרית המגלגלת מיליארדי דולרים, שניזונה מביקוש לחלקי בעלי חיים (כמו קרני קרנף שנהב פיל, עצמות טיגריס) או מחיות אקזוטיות לגידול פרטי. תעשייה זו קשורה קשר הדוק לרשתות פשיעה מאורגנות, ולעיתים אף מממנת סכסוכים ואלימות. היא מערערת יציבות אזורית ופוגעת קשות בכלכלות מקומיות שיכולות היו ליהנות מתיירות אקולוגית חוקית.</p>

    <h3>מחיר אקולוגי כבד: ההשפעות ההרסניות על המערכת האקולוגית והמגוון הביולוגי</h3>
    <p>כל מין במערכת אקולוגית הוא חוליה בשרשרת. ציד יתר של מינים מרכזיים (Key Species) עלול להוביל לקריסה של מערכות שלמות. כך למשל, צניחה באוכלוסיית הטורפים עלולה לגרום לעלייה בלתי מבוקרת באוכלוסיית אוכלי העשב, מה שיוביל לפגיעה בצמחייה ולמחסור במזון עבור מינים אחרים. דמיינו פארק שבו הפילים, הנדרסים על שנהבם, נעלמים. לא רק שהעולם יאבד יצור מרהיב, אלא שגם יאבד "מהנדס נוף" שתפקידו לפלס שבילים, לפזר זרעים ולשנות את מבנה הצמחייה – פעולות חיוניות לבריאות הפארק כולו.</p>

    <h3>אתגרים בשטח: מלחמה יומיומית נגד הזרם</h3>
    <p>המאבק בציד מתנהל לרוב בשטחים עצומים, מרוחקים ומסוכנים. פקחי השמורות עובדים לרוב בתנאים קשים, עם משאבים מוגבלים ולעיתים קרובות עומדים בפני ציידים חמושים ומאורגנים היטב. אתגרים נוספים כוללים שחיתות, עוני באוכלוסיות מקומיות שנדחקות לציד כפתרון הישרדות, והביקוש העולמי הבלתי פוסק המניע את השוק השחור.</p>

    <h3>מגוון אסטרטגיות להגנה: גישה הוליסטית היא המפתח</h3>
    <ul>
        <li>**אכיפה בשטח:** זהו קו ההגנה הראשון. הגדלת מספר הפקחים, שיפור הכשרתם וציודם (נשק, רכבים, אמצעי קשר), שימוש בטכנולוגיה מתקדמת (מצלמות תרמיות, מל"טים, ניטור לווייני) ואיסוף מודיעין. המטרה היא להקטין את הסיכוי של הציידים להצליח ולהגדיל את הסיכון שלהם להיתפס.</li>
        <li>**מעורבות קהילתית:** גישה זו מכירה בכך שהקהילות המתגוררות סביב הפארקים הן חלק מהפתרון. זה כולל חינוך סביבתי, יצירת מקורות הכנסה חלופיים (כמו תיירות אקולוגית, פיתוח חקלאי בר קיימא), ושיתוף פעולה באיסוף מידע מודיעיני על פעילות חשודה. קהילה שתראה בפארק נכס ולא אויב, תהפוך לשותפה פעילה בשמירה עליו.</li>
        <li>**הפחתת הביקוש:** המאבק לא יכול להצליח ללא טיפול בשורש הבעיה – הביקוש העולמי למוצרי ציד. זה כולל העלאת מודעות ציבורית, חקיקה מחמירה יותר נגד סחר בחיות בר, ושיתוף פעולה בינלאומי לפירוק רשתות הסחר.</li>
        <li>**שיקום בתי גידול:** הגנה על שטחי המחיה הטבעיים של החיות ויצירת תנאים נוחים לרבייתן ולהתאוששות אוכלוסיות.</li>
    </ul>

    <h3>חשיבות הנתונים והתכנון האסטרטגי</h3>
    <p>ניהול פארק ספארי הוא משימה מבוססת נתונים. ניטור אוכלוסיות החיות, מיפוי אירועי ציד, ניתוח דפוסים, והערכת האפקטיביות של מאמצי האכיפה השונים – כל אלו חיוניים לקבלת החלטות מושכלות על הקצאת המשאבים המוגבלים. אסטרטגיה מבוססת ראיות מאפשרת גמישות והתאמה לאיומים המשתנים.</p>

    <h3>אור וצל: סיפורי הצלחה וכישלון</h3>
    <p>ההיסטוריה של שימור הטבע רצופה הן בסיפורי הצלחה מעוררי השראה, כמו התאוששות אוכלוסיות קרנפים לבנים בדרום אפריקה בזכות מאמצי אכיפה ותיירות אקולוגית, והן בכישלונות טרגיים, כמו היעלמות מינים מסוימים או פרקים עקובים מדם של אלימות בין פקחים לציידים. המאבק הוא אינסופי ודורש מחויבות מתמשכת, שיתוף פעולה גלובלי, ויכולת התאמה לאתגרים חדשים.</p>

    <p>כעת, חזרו לסימולציה. הנתונים שראיתם וההחלטות שתקבלו ממחישים את המורכבות של ניהול פארק ספארי. בהצלחה במשימה!</p>
</div>

<script>
    const gameState = {
        year: 1,
        budget: 1500000, // Slightly increased budget for more flexibility
        elephants: 500,
        rhinos: 300,
        zebras: 800,
        availableRangers: 50, // Base available rangers (some fixed costs are implied)
        maxYears: 10,
        criticalPopulation: {
            elephants: 200,
            rhinos: 100,
            zebras: 300
        },
        resourceCosts: {
            rangers: 5000,
            surveillance: 10000,
            community: 20000,
            fences: 15000
        },
        basePoachingProb: {
            elephants: 0.15, // Increased base probability slightly to make it more challenging
            rhinos: 0.2, // Increased base probability for rhinos significantly as they are highly targeted
            zebras: 0.08
        },
        poachingEffectiveness: { // How much each resource type reduces the probability of an incident
            rangers: 0.0012, // Slightly increased effectiveness
            surveillance: 0.0018, // Slightly increased effectiveness
            community: 0.0009,
            fences: 0.0006 // Slightly increased effectiveness
        },
        poachedAnimalsPerIncident: { // How many animals are lost per poaching incident
            elephants: 5,
            rhinos: 3,
            zebras: 10
        },
        reproductionRate: { // Natural population increase % per year (net, after natural death)
             elephants: 0.03,
            rhinos: 0.05,
            zebras: 0.1
        },
         // Added for better simulation feel - randomness factor
         randomFactor: 0.2 // +/- 20% randomness in poaching probability effect
    };

    const elements = {
        currentYear: document.getElementById('current-year'),
        nextYearDisplay: document.getElementById('next-year-display'),
        currentYearResults: document.getElementById('current-year-results'),
        currentBudget: document.getElementById('current-budget'),
        elephants: document.getElementById('elephants'),
        rhinos: document.getElementById('rhinos'),
        zebras: document.getElementById('zebras'),
        availableRangers: document.getElementById('available-rangers'),
        allocateRangers: document.getElementById('allocate-rangers'),
        allocateSurveillance: document.getElementById('allocate-surveillance'),
        allocateCommunity: document.getElementById('allocate-community'),
        allocateFences: document.getElementById('allocate-fences'),
        nextYearBtn: document.getElementById('next-year-btn'),
        resultsSection: document.getElementById('results-section'),
        yearlySpend: document.getElementById('yearly-spend'),
        poachingPrevented: document.getElementById('poaching-prevented'),
        poachingOccurred: document.getElementById('poaching-occurred'),
        elephantsPoached: document.getElementById('elephants-poached'),
        rhinosPoached: document.getElementById('rhinos-poached'),
        zebrasPoached: document.getElementById('zebras-poached'),
        elephantsChange: document.getElementById('elephants-change'),
        rhinosChange: document.getElementById('rhinos-change'),
        zebrasChange: document.getElementById('zebras-change'),
        gameOver: document.getElementById('game-over'),
        gameOverMessage: document.getElementById('game-over-message'),
        restartBtn: document.getElementById('restart-btn'),
        toggleExplanationBtn: document.getElementById('toggle-explanation'),
        explanationDiv: document.getElementById('explanation'),
        allocationSection: document.getElementById('allocation-section'),
        budgetWarning: document.getElementById('budget-warning')
    };

     const initialGameState = { ...gameState }; // Store initial state for restart

    function updateDisplay(showResults = false) {
        elements.currentYear.textContent = gameState.year;
        elements.nextYearDisplay.textContent = gameState.year + 1; // Display next year in allocation title
        elements.currentYearResults.textContent = gameState.year -1 ; // Display current year in results title
        elements.currentBudget.textContent = gameState.budget.toLocaleString();
        elements.elephants.textContent = Math.max(0, Math.round(gameState.elephants));
        elements.rhinos.textContent = Math.max(0, Math.round(gameState.rhinos));
        elements.zebras.textContent = Math.max(0, Math.round(gameState.zebras));
        elements.availableRangers.textContent = gameState.availableRangers;

        // Reset inputs and hide/show sections
        if (!showResults) {
            elements.allocateRangers.value = 0;
            elements.allocateSurveillance.value = 0;
            elements.allocateCommunity.value = 0;
            elements.allocateFences.value = 0;

             elements.resultsSection.classList.add('hidden');
             elements.allocationSection.classList.remove('hidden');
             elements.nextYearBtn.classList.remove('hidden');
        } else {
             elements.resultsSection.classList.remove('hidden');
             elements.allocationSection.classList.add('hidden');
             elements.nextYearBtn.classList.add('hidden');
        }


        elements.gameOver.classList.add('hidden');
        elements.budgetWarning.style.display = 'none'; // Hide warning

         // Add animation classes
        document.querySelectorAll('.status-value.population').forEach(el => {
            el.classList.remove('changed'); // Remove animation class
        });
         document.querySelectorAll('.status-value.change').forEach(el => {
            el.classList.remove('changed'); // Remove animation class
        });
    }

    function calculateYearOutcome() {
        const allocatedRangers = parseInt(elements.allocateRangers.value) || 0;
        const allocatedSurveillance = parseInt(elements.allocateSurveillance.value) || 0;
        const allocatedCommunity = parseInt(elements.allocateCommunity.value) || 0;
        const allocatedFences = parseInt(elements.allocateFences.value) || 0;

        const yearlyCost =
            allocatedRangers * gameState.resourceCosts.rangers +
            allocatedSurveillance * gameState.resourceCosts.surveillance +
            allocatedCommunity * gameState.resourceCosts.community +
            allocatedFences * gameState.resourceCosts.fences;

        if (yearlyCost > gameState.budget) {
            elements.budgetWarning.style.display = 'block'; // Show budget warning
            return; // Stop the year from advancing
        }

        gameState.budget -= yearlyCost;

        // Calculate total reduction in poaching probability per incident type
        let totalPoachingProbReduction =
            allocatedRangers * gameState.poachingEffectiveness.rangers +
            allocatedSurveillance * gameState.poachingEffectiveness.surveillance +
            allocatedCommunity * gameState.poachingEffectiveness.community +
            allocatedFences * gameState.poachingEffectiveness.fences;

        // Add randomness to the effectiveness
        const randomAdjustment = (Math.random() * 2 - 1) * gameState.randomFactor; // Random number between -randomFactor and +randomFactor
         totalPoachingProbReduction *= (1 + randomAdjustment);
         totalPoachingProbReduction = Math.max(0, totalPoachingProbReduction); // Ensure reduction isn't negative

        // Calculate the reduced probability for each species (cannot go below 0)
        const poachingProb = {
            elephants: Math.max(0, gameState.basePoachingProb.elephants - totalPoachingProbReduction),
            rhinos: Math.max(0, gameState.basePoachingProb.rhinos - totalPoachingProbReduction),
            zebras: Math.max(0, gameState.basePoachingProb.zebras - totalPoachingProbReduction)
        };

        let elephantsPoachedCount = 0;
        let rhinosPoachedCount = 0;
        let zebrasPoachedCount = 0;
        let poachingOccurredCount = 0;
        let poachingPreventedCount = 0;

        // Simulate potential incidents based on probability
        // Use a fixed number of 'potential' incidents, maybe proportional to total base risk?
        const totalBaseRisk = gameState.basePoachingProb.elephants + gameState.basePoachingProb.rhinos + gameState.basePoachingProb.zebras;
        const numberOfPotentialIncidents = Math.round(totalBaseRisk * 100); // Base on overall risk level

        // Simulate actual occurrences based on reduced probability
         for (let i = 0; i < numberOfPotentialIncidents; i++) {
             // Simple approach: Randomly pick a species for a potential incident
             const targetSpecies = ['elephants', 'rhinos', 'zebras'][Math.floor(Math.random() * 3)];
             const successProb = poachingProb[targetSpecies];

             if (Math.random() < successProb) {
                 poachingOccurredCount++;
                 const poached = gameState.poachedAnimalsPerIncident[targetSpecies];
                  if (targetSpecies === 'elephants') elephantsPoachedCount += poached;
                  else if (targetSpecies === 'rhinos') rhinosPoachedCount += poached;
                  else if (targetSpecies === 'zebras') zebrasPoachedCount += poached;
             }
        }

         // Estimate prevented incidents based on the difference in expected incidents
        const expectedBaseIncidents = totalBaseRisk * (numberOfPotentialIncidents / totalBaseRisk); // Should be numberOfPotentialIncidents
        const totalReducedRisk = poachingProb.elephants + poachingProb.rhinos + poachingProb.zebras;
        const expectedReducedIncidents = totalReducedRisk * (numberOfPotentialIncidents / totalBaseRisk); // Simplified linear relationship

        poachingPreventedCount = Math.round(numberOfPotentialIncidents - poachingOccurredCount);
        poachingPreventedCount = Math.max(0, poachingPreventedCount); // Ensure non-negative


        const initialElephants = gameState.elephants;
        const initialRhinos = gameState.rhinos;
        const initialZebras = gameState.zebras;

        // Natural population change (reproduction - base death rate not explicitly modeled, implied in net reproduction)
        gameState.elephants = Math.max(0, gameState.elephants * (1 + gameState.reproductionRate.elephants) - elephantsPoachedCount);
        gameState.rhinos = Math.max(0, gameState.rhinos * (1 + gameState.reproductionRate.rhinos) - rhinosPoachedCount);
        gameState.zebras = Math.max(0, gameState.zebras * (1 + gameState.reproductionRate.zebras) - zebrasPoachedCount);

        const elephantsChange = Math.round(gameState.elephants - initialElephants);
        const rhinosChange = Math.round(gameState.rhinos - initialRhinos);
        const zebrasChange = Math.round(gameState.zebras - initialZebras);


        elements.yearlySpend.textContent = yearlyCost.toLocaleString();
        elements.poachingPrevented.textContent = poachingPreventedCount;
        elements.poachingOccurred.textContent = poachingOccurredCount;
        elements.elephantsPoached.textContent = elephantsPoachedCount;
        elements.rhinosPoached.textContent = rhinosPoachedCount;
        elements.zebrasPoached.textContent = zebrasPoachedCount;

        elements.elephantsChange.textContent = elephantsChange;
        elements.elephantsChange.style.color = elephantsChange >= 0 ? '#388e3c' : '#d32f2f'; // Dark green or red
        elements.rhinosChange.textContent = rhinosChange;
        elements.rhinosChange.style.color = rhinosChange >= 0 ? '#388e3c' : '#d32f2f';
        elements.zebrasChange.textContent = zebrasChange;
        elements.zebrasChange.style.color = zebrasChange >= 0 ? '#388e3c' : '#d32f2f';

         // Add animation class to changes
         if (elephantsChange !== 0) elements.elephantsChange.classList.add('changed');
         if (rhinosChange !== 0) elements.rhinosChange.classList.add('changed');
         if (zebrasChange !== 0) elements.zebrasChange.classList.add('changed');


         updateDisplay(true); // Show results


        gameState.year++; // Advance year *after* displaying current year's results

        // Delay game over check slightly to show results first
        setTimeout(checkGameOver, 1500); // 1.5 second delay
    }

    function checkGameOver() {
        let message = '';
        let isGameOver = false;

        if (gameState.elephants <= gameState.criticalPopulation.elephants ||
            gameState.rhinos <= gameState.criticalPopulation.rhinos ||
            gameState.zebras <= gameState.criticalPopulation.zebras) {
            message = 'הפסדת! 😭 אוכלוסיית חיות מפתח ירדה מתחת לסף הקריטי עקב ציד יתר.';
            isGameOver = true;
        } else if (gameState.year > gameState.maxYears) {
             message = 'ניצחת! 🎉 הצלחת להגן על אוכלוסיות חיות המפתח למשך ' + (gameState.maxYears) + ' שנים!';
             isGameOver = true;
        } else {
             // Check budget for *next* year only if not already won/lost
             const minAllocationCost = Math.min(
                    gameState.resourceCosts.rangers,
                    gameState.resourceCosts.surveillance,
                    gameState.resourceCosts.community,
                    gameState.resourceCosts.fences
             );
             // If budget is less than the minimum possible allocation cost, you're stuck.
             if (gameState.budget < minAllocationCost) {
                message = 'הפסדת! 💸 נגמר לך התקציב ואינך יכול להקצות משאבים חיוניים נוספים לשנה הבאה.';
                isGameOver = true;
             }
        }


        if (isGameOver) {
            elements.gameOverMessage.textContent = message;
            elements.gameOver.classList.remove('hidden');
             elements.nextYearBtn.classList.add('hidden');
             elements.allocationSection.classList.add('hidden');
        } else {
            // Prepare for next year
            updateDisplay();
        }
    }

    function restartGame() {
         // Reset game state to initial values
         gameState.year = initialGameState.year;
         gameState.budget = initialGameState.budget;
         gameState.elephants = initialGameState.elephants;
         gameState.rhinos = initialGameState.rhinos;
         gameState.zebras = initialGameState.zebras;
         gameState.availableRangers = initialGameState.availableRangers;

         updateDisplay();
         elements.gameOver.classList.add('hidden');
         elements.resultsSection.classList.add('hidden');
         elements.allocationSection.classList.remove('hidden');
         elements.nextYearBtn.classList.remove('hidden');
          elements.budgetWarning.style.display = 'none';
    }

    function toggleExplanation() {
        const isHidden = elements.explanationDiv.classList.contains('hidden');
        if (isHidden) {
            elements.explanationDiv.classList.remove('hidden');
            elements.explanationDiv.style.maxHeight = elements.explanationDiv.scrollHeight + "px"; // Animate open
            elements.toggleExplanationBtn.textContent = 'הסתר הסבר מורחב';
        } else {
             elements.explanationDiv.style.maxHeight = null; // Animate close
            elements.explanationDiv.classList.add('hidden');
            elements.toggleExplanationBtn.textContent = 'הצג הסבר מורחב';
        }
    }

    // Initial setup
    updateDisplay();

    // Event Listeners
    elements.nextYearBtn.addEventListener('click', calculateYearOutcome);
    elements.restartBtn.addEventListener('click', restartGame);
    elements.toggleExplanationBtn.addEventListener('click', toggleExplanation);

</script>

<style>
    /* RTL adjustments first */
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif; /* Basic fallback */
        line-height: 1.6;
        margin: 0; /* Full viewport */
        background: linear-gradient(to bottom right, #e8f5e9, #c8e6c9); /* Gentle gradient */
        color: #333;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #1b5e20; /* Darker forest green */
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }

    h1 {
        font-size: 2.5em;
        margin-top: 0;
         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    h2.game-title {
        font-size: 1.8em;
         border-bottom: 2px solid #388e3c;
        padding-bottom: 10px;
        margin-bottom: 30px;
         color: #2e7d32; /* Medium green */
    }

    #safari-app {
        background-color: #ffffff;
        border: 1px solid #a5d6a7; /* Medium light green border */
        padding: 30px;
        border-radius: 12px;
        max-width: 800px;
        margin: 20px auto;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Stronger shadow */
        overflow: hidden; /* Clear floats/margins */
    }

    #game-status, #allocation-section, #results-section, #game-over {
        margin-bottom: 30px; /* More space */
        padding: 20px;
        border: 1px solid #c8e6c9; /* Light green border */
        border-radius: 8px;
        background-color: #f1f8e9; /* Very light green */
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out; /* Smooth transitions */
    }

    #allocation-section, #results-section {
        background-color: #ffffff; /* White background for sections */
        border: 1px solid #a5d6a7; /* Medium light green border */
    }

    #game-status h3,
    #allocation-section h3,
    #results-section h3 {
        margin-top: 0;
        margin-bottom: 15px;
        padding-bottom: 5px;
        border-bottom: 1px dashed #c8e6c9;
         color: #388e3c; /* Darker green */
         text-align: right; /* Align section titles to the right */
    }

    .status-item {
        margin-bottom: 12px; /* More space between status items */
        display: flex; /* Align label and value */
        justify-content: space-between; /* Push value to the left */
        align-items: center;
        font-size: 1.1em;
    }

    .status-label {
         font-weight: normal; /* Label is not bold */
         color: #555;
         margin-inline-end: 10px;
    }

    .status-value {
        font-weight: bold; /* Value is bold */
         color: #1b5e20; /* Dark green for values */
         flex-shrink: 0; /* Prevent shrinking */
         text-align: left; /* Keep values left-aligned for readability */
         min-width: 50px; /* Ensure values have space */
    }

     .status-value.budget {
         color: #0d47a1; /* Dark blue for budget */
     }

     .status-value.spend {
        color: #d32f2f; /* Red for spending */
     }
      .status-value.prevented {
        color: #388e3c; /* Green for prevented */
     }
      .status-value.occurred,
      .status-value.poached {
        color: #fbc02d; /* Orange for occurred/poached */
      }


     /* Animation for changing numbers */
     .status-value.changed {
         animation: flashChange 0.6s ease-out;
     }

     @keyframes flashChange {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
     }

     .status-value.change.changed {
          animation: flashChangeColor 0.6s ease-out;
     }

      @keyframes flashChangeColor {
        0% { background-color: transparent; }
        50% { background-color: rgba(0, 255, 0, 0.2); } /* Greenish tint for increase */
        50% { background-color: rgba(255, 0, 0, 0.2); } /* Reddish tint for decrease */
        100% { background-color: transparent; }
     }


    #animal-populations ul {
        list-style: none;
        padding: 0;
        margin-top: 15px;
    }
    #animal-populations li {
         margin-bottom: 8px;
          display: flex;
          justify-content: space-between;
           font-size: 1.1em;
           padding-right: 0; /* Remove custom bullet padding */
           position: static; /* Remove positioning */
    }
     #animal-populations li::before {
         content: none; /* Remove custom bullet */
     }

     .status-section {
        padding-top: 15px;
        border-top: 1px dashed #c8e6c9;
        margin-top: 15px;
     }

    .resource-allocation {
        margin-bottom: 20px; /* More space */
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        padding: 10px;
        background-color: #f9fbe7; /* Very light yellow/green */
        border-radius: 5px;
        border: 1px solid #e6ee9c; /* Light yellow border */
    }

    .resource-allocation label {
        flex-grow: 1;
        margin-inline-end: 15px; /* Increased space */
        text-align: right;
        font-weight: bold;
        color: #555;
    }

    .resource-allocation .cost {
        font-weight: normal;
        font-size: 0.9em;
        color: #777;
        display: block; /* Place cost on new line if needed */
    }


    .resource-input {
        padding: 10px; /* Larger padding */
        border: 1px solid #ccc;
        border-radius: 5px;
        width: 90px; /* Wider input */
        text-align: left;
        flex-shrink: 0;
        font-size: 1.1em;
         transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

     .resource-input:focus {
        border-color: #4caf50; /* Green focus */
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
        outline: none;
     }

    button {
        display: block;
        width: auto;
        margin: 30px auto 0 auto; /* More space */
        padding: 12px 25px; /* Larger padding */
        background-color: #4caf50; /* Green */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.2em; /* Larger font */
        transition: background-color 0.3s ease, transform 0.1s ease; /* Added transform for press effect */
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    button:hover {
        background-color: #388e3c; /* Darker green */
    }

    button:active {
         transform: scale(0.98); /* Subtle press effect */
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    #restart-btn {
        background-color: #ff9800; /* Orange */
         margin-top: 15px; /* Less margin for secondary button */
    }

    #restart-btn:hover {
         background-color: #f57c00; /* Darker Orange */
    }

     #toggle-explanation {
        display: block;
        margin: 20px auto;
        background-color: #03a9f4; /* Light blue */
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
     }

     #toggle-explanation:hover {
         background-color: #0288d1; /* Darker blue */
     }
      #toggle-explanation:active {
         transform: scale(0.98);
     }


    #results-section ul {
        list-style: none;
        padding: 0;
    }
     #results-section li {
        margin-bottom: 8px; /* More space */
        padding-right: 0; /* Remove custom bullet padding */
        position: static; /* Remove positioning */
         display: flex;
         justify-content: space-between;
          font-size: 1.1em;
     }
      #results-section li::before {
         content: none; /* Remove custom bullet */
     }

     .results-summary {
         margin-bottom: 20px;
         padding-bottom: 15px;
         border-bottom: 1px dashed #c8e6c9;
     }

     .animal-results h4 {
         margin-top: 15px;
         margin-bottom: 10px;
         color: #2e7d32; /* Medium green */
         text-align: right;
     }


    #game-over {
        text-align: center;
        background-color: #ffebee; /* Very light red */
        border-color: #ffcdd2; /* Light red border */
        padding: 30px;
        animation: fadeIn 0.8s ease-out; /* Animation */
    }

    #game-over-message {
        color: #c62828; /* Dark red text */
        font-weight: bold;
        font-size: 1.6em; /* Larger font */
        margin-bottom: 20px;
         text-shadow: 1px 1px 2px rgba(200,0,0,0.1);
    }

    #explanation {
        background-color: #e3f2fd; /* Very light blue */
        border: 1px solid #bbdefb; /* Light blue border */
        padding: 30px; /* More padding */
        border-radius: 12px;
        max-width: 800px;
        margin: 20px auto;
        line-height: 1.8;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
        overflow: hidden; /* Needed for collapse animation */
        transition: max-height 0.5s ease-in-out, opacity 0.5s ease-in-out; /* Animation */
         max-height: 0; /* Start collapsed */
         opacity: 0;
    }

    #explanation.hidden {
        max-height: 0;
        opacity: 0;
        padding-top: 0;
        padding-bottom: 0;
         border: none; /* Hide border when collapsed */
         margin-top: 0;
         margin-bottom: 0;
    }


    #explanation h3 {
        color: #0d47a1; /* Dark blue */
        margin-top: 25px; /* More space */
        text-align: right;
         border-bottom: 1px dashed #bbdefb;
         padding-bottom: 5px;
    }

    #explanation ul {
        list-style: none;
        padding: 0;
        margin-top: 15px;
    }

    #explanation li {
        margin-bottom: 12px; /* More space */
        padding-right: 1.5em; /* Space for custom bullet */
        position: relative;
    }
     #explanation li::before {
        content: "•"; /* Custom bullet */
        position: absolute;
        right: 0;
        color: #0d47a1; /* Dark blue */
        font-weight: bold;
        font-size: 1.2em;
     }

    .hidden {
        display: none;
        /* opacity: 0; */ /* Use CSS class for animation if needed */
    }

    /* Warning Message Style */
    .warning-message {
        color: #c62828; /* Dark red */
        background-color: #ffcdd2; /* Light red */
        border: 1px solid #ef9a9a; /* Red border */
        padding: 10px;
        border-radius: 5px;
        margin-top: 15px;
        text-align: center;
        font-weight: bold;
        animation: shake 0.5s ease-in-out; /* Add a little shake animation */
    }

    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }

     /* Simple fade in animation for sections */
     @keyframes fadeIn {
         from { opacity: 0; transform: translateY(20px); }
         to { opacity: 1; transform: translateY(0); }
     }

     #safari-app > div:not(.hidden) {
         animation: fadeIn 0.6s ease-out;
     }


</style>
```