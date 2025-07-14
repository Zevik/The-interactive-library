---
title: "משבר עולמי: האם תציל/י את הכלכלה?"
english_slug: global-crisis-will-you-save-the-economy
category: "כלכלה"
tags:
  - משבר פיננסי
  - 2008
  - כלכלה מאקרו
  - רגולציה
  - מדיניות מוניטרית
  - סימולציה
---
# משבר עולמי: האם תציל/י את הכלכלה?

המערכת הפיננסית העולמית רועדת. הבנקים בסכנה, האבטלה גואה, והפחד משתק את השווקים. יש לך זמן מוגבל לנקוט פעולה. כל החלטה יכולה להוביל להתאוששות מפוארת... או לקריסה מוחלטת. האם תצליח/י לנווט את הספינה דרך הסערה?

<div id="economic-simulator">
    <div id="dashboard">
        <h2>לוח בקרה - מצב הכלכלה</h2>
        <div class="metric" id="metric-stockIndex">
            <span class="metric-label">מדד מניות:</span>
            <span id="stockIndex" class="metric-value">--</span>
             <span class="metric-indicator"></span>
        </div>
        <div class="metric" id="metric-unemploymentRate">
            <span class="metric-label">אבטלה:</span>
            <span id="unemploymentRate" class="metric-value">--</span>
            <span class="metric-indicator"></span>
        </div>
        <div class="metric" id="metric-bankStability">
            <span class="metric-label">יציבות בנקים:</span>
            <span id="bankStability" class="metric-value">--</span>
            <span class="metric-indicator"></span>
        </div>
        <div class="metric" id="metric-publicConfidence">
            <span class="metric-label">אמון הציבור:</span>
            <span id="publicConfidence" class="metric-value">--</span>
            <span class="metric-indicator"></span>
        </div>
        <div class="metric" id="metric-governmentDebt">
            <span class="metric-label">חוב ציבורי:</span>
            <span id="governmentDebt" class="metric-value">--</span>
            <span class="metric-indicator"></span>
        </div>
        <div class="metric" id="metric-interestRate">
            <span class="metric-label">ריבית:</span>
            <span id="interestRate" class="metric-value">--</span>
             <span class="metric-indicator"></span>
        </div>
        <div class="metric">
            <span class="metric-label">זמן שחלף:</span>
            <span id="simulationTime" class="metric-value">יום 0</span>
        </div>
    </div>

    <div id="news-feed">
        <h2>ערוץ חדשות חי</h2>
        <div id="news-items">
            <!-- News items will appear here -->
        </div>
    </div>

    <div id="actions">
        <h2>כלי חירום לרשותך</h2>
        <button data-action="changeInterestRate" data-value="-0.5">הורד ריבית (-0.5%)</button>
        <button data-action="changeInterestRate" data-value="+0.25">העלה ריבית (+0.25%)</button>
        <button data-action="bailoutBank">חילוץ בנק גדול</button>
        <button data-action="injectLiquidity">הזרמת נזילות חירום</button>
        <button data-action="tempRegulationChange">הקפאת שוקי נגזרים</button>
        <button data-action="fiscalStimulus">תוכנית גירוי לאבטלה</button>
    </div>

     <div id="controls">
        <button id="start-sim">התחל סימולציה</button>
        <button id="pause-sim" style="display: none;">השהה</button>
        <button id="reset-sim" style="display: none;">התחל מחדש</button>
    </div>

    <div id="outcome" style="display: none;">
        <h2>תוצאת המשבר</h2>
        <p id="outcome-text"></p>
         <button id="restart-sim-outcome">נסה שוב</button>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר: רקע על משברים כלכליים</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: משברים כלכליים וניהולם - רקע מהיר</h2>
    <p>סימולטור זה מדמה התמודדות עם משבר פיננסי מערכתי, ברוח אירועי 2008. משברים כאלה מורכבים, מתפתחים במהירות, ודורשים החלטות תחת אי-ודאות קיצונית.</p>

    <h3>איך מתחיל משבר כזה?</h3>
    <p>לרוב, זה מתחיל עם התפוצצות 'בועה' (נדל"ן, מניות) שחושפת סיכון מופרז במערכת הפיננסית. כשהאמון מתערער, בנקים מפסיקים להלוות זה לזה, שווקי האשראי קופאים, ומוסדות פיננסיים נקלעים למצוקת נזילות. זה כמו "ראן על הבנק" בקנה מידה עולמי. ההשפעה מיד זולגת לכלכלה הריאלית: עסקים לא מקבלים אשראי, מפטרים עובדים, והאבטלה מזנקת. הרגולציה שלא עמדה בקצב או הייתה חלשה מדי תורמת להתפתחות הסיכון מלכתחילה.</p>

    <h3>כלים לרשותך כמנהל/ת המשבר:</h3>
    <ul>
        <li><strong>הורדת ריבית:</strong> הופך אשראי לזול יותר, אמור לעודד השקעה וצריכה, אבל עלול להזיק לחוסכים ולייצר בועות חדשות.</li>
        <li><strong>העלאת ריבית:</strong> בדרך כלל משמש לריסון אינפלציה, לא רלוונטי בזמן משבר דפלציוני, עלול להחמיר את מצוקת האשראי.</li>
        <li><strong>חילוץ בנק גדול:</strong> מונע קריסה מיידית של מוסד "גדול מכדי ליפול" והתפשטות ההדבקה. אבל עולה כסף רב למשלם המיסים ויוצר "סיכון מוסרי" (תמריץ לבנקים לקחת סיכונים בידיעה שיחולצו).</li>
        <li><strong>הזרמת נזילות (QE):</strong> בנק מרכזי קונה נכסים (אג"ח) כדי להכניס כסף למערכת הבנקאית ולהוזיל אשראי. תומך בשווקים, אך עלול להגדיל את החוב הציבורי (באופן עקיף) ולעורר חשש מאינפלציה עתידית.</li>
        <li><strong>הקפאת שוקי נגזרים:</strong> פעולת רגולציה שמגבילה מסחר מסוכן או פעולות ספקולטיביות (כמו Short Selling) כדי להרגיע את השווקים. יכולה לפגוע בפעילות שוק תקינה.</li>
        <li><strong>תוכנית גירוי פיסקלי:</strong> ממשלה מגדילה הוצאות (פרויקטים, תשלומי אבטלה) או מורידה מיסים כדי להגדיל את הביקוש. יעיל נגד אבטלה, אך מגדיל משמעותית את החוב הציבורי.</li>
    </ul>

    <h3>דילמות קשות והשלכות:</h3>
    <p>כל פעולה כרוכה בוויתורים. האם לשלם מחיר כבד של חוב ציבורי כדי למנוע קריסה מיידית? האם להקריב עקרונות שוק חופשי לטובת התערבות ממשלתית? ההשלכות ארוכות הטווח כוללות שינויים רגולטוריים (כמו רפורמות דוד-פרנק ובאזל III אחרי 2008), ירידה באמון הציבור, ולעתים שנים של צמיחה איטית.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // --- Game State ---
    let state = {
        stockIndex: 5500, // Start higher
        unemploymentRate: 4.5, // Start lower
        bankStability: 85, // Start healthier
        publicConfidence: 75, // Start higher
        governmentDebt: 55, // Start lower
        interestRate: 2.0, // Start moderate
        time: 0, // in days
        isRunning: false,
        simulationInterval: null,
        simulationSpeed: 120, // Milliseconds per day (faster pace)
        actionCooldowns: { // Slightly adjusted cooldowns
            changeInterestRate: 25, // days
            bailoutBank: 50,
            injectLiquidity: 40,
            tempRegulationChange: 70,
            fiscalStimulus: 100
        },
        lastActionTime: {}, // Track last used time for each action
        newsFeed: [],
        events: [
            { time: 20, type: 'event', text: 'דיווחים ראשונים על הפסדים ענק בבנקים מאירועים קודמים.', severity: 'medium' },
            { time: 45, type: 'event', text: 'זינוק חד בהיקף המשכנתאות הכושלות בארה"ב.', severity: 'high' },
            { time: 70, type: 'event', text: 'בנק השקעות מרכזי עומד בפני פשיטת רגל!', severity: 'critical' },
            { time: 95, type: 'event', text: 'התפשטות הבהלה - בנקים מפסיקים להלוות זה לזה.', severity: 'critical' },
             { time: 120, type: 'event', text: 'נתוני אבטלה מפתיעים לרעה - עלייה חדה מהצפוי.', severity: 'high' },
             { time: 140, type: 'event', text: 'בורסות בעולם צוללות על רקע חשש מהדבקה פיננסית.', severity: 'high' },
             { time: 160, type: 'event', text: 'קרן גידור גדולה קורסת - חושפת חשיפות נוספות במערכת.', severity: 'medium' },
             { time: 180, type: 'event', text: 'מחאות עממיות נגד התנהלות הבנקים והסיוע הממשלתי.', severity: 'medium' },
             { time: 200, type: 'event', text: 'מדינה אירופאית גדולה נקלעת למצוקת חוב - מבקשת סיוע.', severity: 'high' },
             { time: 220, type: 'event', text: 'לחץ פוליטי כבד לקצץ בבונוסים של בנקאים.', severity: 'low' }, // Less direct economic impact, more confidence related
             { time: 240, type: 'event', text: 'דיונים סוערים על שינויים רגולטוריים ארוכי טווח.', severity: 'low' }, // Low immediate impact
             { time: 260, type: 'event', text: 'דיווחים על עלייה בפשיעה ואלימות על רקע המצב הכלכלי.', severity: 'medium' },
             { time: 280, type: 'event', text: 'חשש מ"גל שני" של מיתון.', severity: 'medium' },
             { time: 300, type: 'event', text: 'שיחות בינלאומיות מתקדמות על תיאום מדיניות.', severity: 'low' }, // Positive potential, low immediate
        ],
        gameDuration: 365 // days, a full year
    };

    // --- DOM Elements ---
    const elements = {
        stockIndex: document.getElementById('stockIndex'),
        unemploymentRate: document.getElementById('unemploymentRate'),
        bankStability: document.getElementById('bankStability'),
        publicConfidence: document.getElementById('publicConfidence'),
        governmentDebt: document.getElementById('governmentDebt'),
        interestRate: document.getElementById('interestRate'),
        simulationTime: document.getElementById('simulationTime'),
        newsItems: document.getElementById('news-items'),
        actions: document.querySelectorAll('#actions button'),
        startSimButton: document.getElementById('start-sim'),
        pauseSimButton: document.getElementById('pause-sim'),
        resetSimButton: document.getElementById('reset-sim'),
        outcomeDiv: document.getElementById('outcome'),
        outcomeText: document.getElementById('outcome-text'),
        explanationDiv: document.getElementById('explanation'),
        toggleExplanationButton: document.getElementById('toggle-explanation'),
        restartSimOutcomeButton: document.getElementById('restart-sim-outcome') // New restart button on outcome screen
    };

     // --- Initial Setup ---
     initializeSimulation();

     function initializeSimulation() {
         // Reset state to initial values
         state = {
            stockIndex: 5500,
            unemploymentRate: 4.5,
            bankStability: 85,
            publicConfidence: 75,
            governmentDebt: 55,
            interestRate: 2.0,
            time: 0,
            isRunning: false,
            simulationInterval: null,
            simulationSpeed: 120,
            actionCooldowns: {
                changeInterestRate: 25,
                bailoutBank: 50,
                injectLiquidity: 40,
                tempRegulationChange: 70,
                fiscalStimulus: 100
            },
            lastActionTime: {},
            newsFeed: [],
            events: [
                { time: 20, type: 'event', text: 'דיווחים ראשונים על הפסדים ענק בבנקים מאירועים קודמים.', severity: 'medium' },
                { time: 45, type: 'event', text: 'זינוק חד בהיקף המשכנתאות הכושלות בארה"ב.', severity: 'high' },
                { time: 70, type: 'event', text: 'בנק השקעות מרכזי עומד בפני פשיטת רגל!', severity: 'critical' },
                { time: 95, type: 'event', text: 'התפשטות הבהלה - בנקים מפסיקים להלוות זה לזה.', severity: 'critical' },
                 { time: 120, type: 'event', text: 'נתוני אבטלה מפתיעים לרעה - עלייה חדה מהצפוי.', severity: 'high' },
                 { time: 140, type: 'event', text: 'בורסות בעולם צוללות על רקע חשש מהדבקה פיננסית.', severity: 'high' },
                 { time: 160, type: 'event', text: 'קרן גידור גדולה קורסת - חושפת חשיפות נוספות במערכת.', severity: 'medium' },
                 { time: 180, type: 'event', text: 'מחאות עממיות נגד התנהלות הבנקים והסיוע הממשלתי.', severity: 'medium' },
                 { time: 200, type: 'event', text: 'מדינה אירופאית גדולה נקלעת למצוקת חוב - מבקשת סיוע.', severity: 'high' },
                 { time: 220, type: 'event', text: 'לחץ פוליטי כבד לקצץ בבונוסים של בנקאים.', severity: 'low' },
                 { time: 240, type: 'event', text: 'דיונים סוערים על שינויים רגולטוריים ארוכי טווח.', severity: 'low' },
                 { time: 260, type: 'event', text: 'דיווחים על עלייה בפשיעה ואלימות על רקע המצב הכלכלי.', severity: 'medium' },
                 { time: 280, type: 'event', text: 'חשש מ"גל שני" של מיתון.', severity: 'medium' },
                 { time: 300, type: 'event', text: 'שיחות בינלאומיות מתקדמות על תיאום מדיניות.', severity: 'low' },
            ],
            gameDuration: 365
         };

         // Clear news feed UI
         elements.newsItems.innerHTML = '';

         // Reset UI elements
         elements.startSimButton.style.display = 'inline-block';
         elements.pauseSimButton.style.display = 'none';
         elements.resetSimButton.style.display = 'none';
         elements.outcomeDiv.style.display = 'none';

         // Ensure action buttons are enabled initially
         elements.actions.forEach(button => {
             button.disabled = false;
             // Also remove any residual cooldown display if added later
             button.textContent = button.dataset.originalText || button.textContent;
         });

         // Store original button text to restore after cooldown display
         elements.actions.forEach(button => {
             button.dataset.originalText = button.textContent;
         });


         updateUI();
     }

    // --- Update UI ---
    function updateUI() {
        const prevStockIndex = parseFloat(elements.stockIndex.textContent) || state.stockIndex; // Get previous value for animation
        const prevUnemploymentRate = parseFloat(elements.unemploymentRate.textContent) || state.unemploymentRate;
        const prevBankStability = parseFloat(elements.bankStability.textContent) || state.bankStability;
        const prevPublicConfidence = parseFloat(elements.publicConfidence.textContent) || state.publicConfidence;
        const prevGovernmentDebt = parseFloat(elements.governmentDebt.textContent) || state.governmentDebt;
        const prevInterestRate = parseFloat(elements.interestRate.textContent) || state.interestRate;


        elements.stockIndex.textContent = state.stockIndex.toFixed(0);
        elements.unemploymentRate.textContent = state.unemploymentRate.toFixed(1) + '%';
        elements.bankStability.textContent = state.bankStability.toFixed(1) + '%';
        elements.publicConfidence.textContent = state.publicConfidence.toFixed(1) + '%';
        elements.governmentDebt.textContent = state.governmentDebt.toFixed(1) + '%';
        elements.interestRate.textContent = state.interestRate.toFixed(2) + '%';
        elements.simulationTime.textContent = `יום ${state.time}`;

        // Add visual indicators and animations for changes
        animateMetricChange('stockIndex', state.stockIndex, prevStockIndex);
        animateMetricChange('unemploymentRate', state.unemploymentRate, prevUnemploymentRate, true); // Higher is worse
        animateMetricChange('bankStability', state.bankStability, prevBankStability);
        animateMetricChange('publicConfidence', state.publicConfidence, prevPublicConfidence);
        animateMetricChange('governmentDebt', state.governmentDebt, prevGovernmentDebt, true); // Higher is worse
        animateMetricChange('interestRate', state.interestRate, prevInterestRate, null, true); // Just indicate change, not good/bad


        // Update action button states based on cooldowns
        const now = state.time;
        elements.actions.forEach(button => {
            const actionType = button.dataset.action;
            const lastUsed = state.lastActionTime[actionType] || -Infinity;
            const cooldown = state.actionCooldowns[actionType];
            const remaining = cooldown - (now - lastUsed);

            if (remaining > 0) {
                button.disabled = true;
                // Update button text with countdown
                button.textContent = `${button.dataset.originalText} (${remaining} ימים)`;
                button.classList.add('cooldown'); // Add class for styling
            } else {
                button.disabled = !state.isRunning; // Disable if simulation is not running
                 if (!state.isRunning && remaining <= 0) {
                    // If simulation is paused but cooldown is over, enable the button
                    button.disabled = false;
                }
                button.textContent = button.dataset.originalText; // Restore original text
                button.classList.remove('cooldown'); // Remove class
            }
        });

        // Scroll news feed to bottom smoothly if new item was added
        elements.newsItems.scrollTo({
            top: elements.newsItems.scrollHeight,
            behavior: 'smooth'
        });
    }

     // --- Animation Helper ---
     function animateMetricChange(metricId, newValue, oldValue, higherIsWorse = false, noGoodBad = false) {
        const metricElement = document.getElementById(metricId);
        const indicatorElement = document.querySelector(`#metric-${metricId} .metric-indicator`); // Get indicator span

        if (!metricElement || !indicatorElement || isNaN(oldValue)) return; // Don't animate on first load

        // Determine color/direction
        let colorClass = '';
        let indicator = '';
        if (newValue > oldValue) {
             colorClass = higherIsWorse ? 'metric-negative' : 'metric-positive';
             indicator = higherIsWorse ? '↓' : '↑';
        } else if (newValue < oldValue) {
            colorClass = higherIsWorse ? 'metric-positive' : 'metric-negative';
             indicator = higherIsWorse ? '↑' : '↓';
        } else {
            colorClass = 'metric-neutral';
             indicator = '•';
        }

        if (noGoodBad) {
            colorClass = ''; // Remove color classes for metrics like Interest Rate
            indicator = (newValue > oldValue ? '↑' : (newValue < oldValue ? '↓' : '•'));
        }


        // Apply color class and indicator, trigger animation
        metricElement.classList.remove('metric-positive', 'metric-negative', 'metric-neutral');
        metricElement.classList.add(colorClass, 'metric-flash');
        indicatorElement.textContent = indicator; // Update indicator

        // Remove animation class after it finishes
        setTimeout(() => {
            metricElement.classList.remove('metric-flash');
            metricElement.classList.remove('metric-positive', 'metric-negative', 'metric-neutral'); // Clean up classes
        }, 500); // Match animation duration in CSS

        // Optional: update indicator color (simpler approach via CSS class on parent)
        const parentMetric = document.getElementById(`metric-${metricId}`);
         parentMetric.classList.remove('is-positive', 'is-negative', 'is-neutral');
         if (noGoodBad) {
             parentMetric.classList.add('is-neutral'); // Default color for neutral
         } else if (higherIsWorse) {
             parentMetric.classList.add(newValue > oldValue ? 'is-negative' : 'is-positive');
         } else {
             parentMetric.classList.add(newValue > oldValue ? 'is-positive' : 'is-negative');
         }
     }


    // --- Add News Item ---
    function addNews(text, isEvent = false) {
        const newsItemDiv = document.createElement('div');
        newsItemDiv.classList.add('news-item');
        if (isEvent) {
            newsItemDiv.classList.add('event');
        }
        // Add a subtle animation for new news items
        newsItemDiv.style.opacity = 0;
        newsItemDiv.style.transform = 'translateY(10px)';

        newsItemDiv.textContent = `יום ${state.time}: ${text}`;
        elements.newsItems.appendChild(newsItemDiv);
        state.newsFeed.push(text);

        // Trigger fade-in animation
         requestAnimationFrame(() => {
            newsItemDiv.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
            newsItemDiv.style.opacity = 1;
            newsItemDiv.style.transform = 'translateY(0)';
         });
    }

    // --- Simulation Logic ---
    function simulateDay() {
        if (!state.isRunning) return;

        state.time++;

        // --- Apply general trends / passive changes (more complex dependencies) ---
        // Stock Index: Affected by Confidence, Bank Stability, Unemployment (neg), Interest Rate (neg if high)
        state.stockIndex += (state.publicConfidence / 100 - 0.6) * 40 + (state.bankStability / 100 - 0.7) * 30 - (state.unemploymentRate / 10) * 20 + (state.interestRate > 2.5 ? -10 : (state.interestRate < 1.5 ? 10 : 0));

        // Unemployment Rate: Tends towards a 'natural' rate (say 6%), affected by Stock Index (pos), Bank Stability (neg), Fiscal Stimulus (neg)
        const naturalUnemployment = 6;
        state.unemploymentRate += (naturalUnemployment - state.unemploymentRate) * 0.02 - (state.stockIndex / 10000) * 0.1 + (100 - state.bankStability) * 0.01; // Stocks/Banks affect it

        // Bank Stability: Affected by Confidence, Stock Index, Interest Rate (complex - high rates can stress borrowers but help margins; low rates hurt margins but ease debt)
        state.bankStability += (state.publicConfidence / 100 - 0.6) * 3 + (state.stockIndex / 10000) * 2 + (state.interestRate > 3 ? -0.5 : (state.interestRate < 1 ? -0.2 : 0.1)); // Simplified rate effect

        // Public Confidence: Affected by Bank Stability, Stock Index, Unemployment (neg), Government Debt (neg), News/Events
        state.publicConfidence += (state.bankStability / 100 - 0.7) * 3 + (state.stockIndex / 10000) * 2 - (state.unemploymentRate / 10) * 3 - (state.governmentDebt / 100 - 0.7) * 1;

        // Government Debt: Increases passively (spending, interest), increases sharply with bailouts/stimulus, might decrease slightly with strong growth (not modeled simply)
        state.governmentDebt += state.governmentDebt * (state.interestRate / 30000); // Cost of debt increases with interest
        state.governmentDebt += (100 - state.publicConfidence) * 0.005; // Low confidence might force spending

         // --- Apply inertia and small random fluctuations ---
         state.stockIndex += (Math.random() - 0.5) * 5;
         state.unemploymentRate += (Math.random() - 0.5) * 0.05;
         state.bankStability += (Math.random() - 0.5) * 0.1;
         state.publicConfidence += (Math.random() - 0.5) * 0.1;


        // --- Keep metrics within reasonable bounds ---
        state.stockIndex = Math.max(500, Math.min(12000, state.stockIndex));
        state.unemploymentRate = Math.max(2, Math.min(30, state.unemploymentRate));
        state.bankStability = Math.max(0, Math.min(100, state.bankStability));
        state.publicConfidence = Math.max(0, Math.min(100, state.publicConfidence));
        state.governmentDebt = Math.max(40, state.governmentDebt); // Debt rarely decreases in a crisis sim

        // --- Trigger events and apply event-specific effects ---
        state.events.filter(event => event.time === state.time).forEach(event => {
            addNews(event.text, true);
             // Apply event-specific effects (more impactful based on severity)
            const severityMultiplier = (event.severity === 'low' ? 0.5 : (event.severity === 'medium' ? 1 : (event.severity === 'high' ? 1.5 : 2))); // Critical events hit hardest

            if (event.text.includes('הפסדים ענק')) {
                state.bankStability *= (1 - 0.05 * severityMultiplier);
                state.stockIndex *= (1 - 0.03 * severityMultiplier);
            } else if (event.text.includes('משכנתאות כושלות')) {
                 state.bankStability *= (1 - 0.07 * severityMultiplier);
                 state.publicConfidence *= (1 - 0.05 * severityMultiplier);
                 state.stockIndex *= (1 - 0.04 * severityMultiplier);
                 state.unemploymentRate += 0.5 * severityMultiplier;
            } else if (event.text.includes('פשיטת רגל')) { // Critical Bank Collapse threat
                 state.bankStability *= (1 - 0.15 * severityMultiplier); // Major hit
                 state.stockIndex *= (1 - 0.10 * severityMultiplier);
                 state.publicConfidence *= (1 - 0.12 * severityMultiplier);
                 state.unemploymentRate += 2 * severityMultiplier;
            } else if (event.text.includes('מפסיקים להלוות')) { // Credit Freeze
                 state.bankStability *= (1 - 0.12 * severityMultiplier);
                 state.stockIndex *= (1 - 0.08 * severityMultiplier);
                 state.publicConfidence *= (1 - 0.10 * severityMultiplier);
                 state.unemploymentRate += 1.5 * severityMultiplier;
            } else if (event.text.includes('נתוני אבטלה')) {
                 state.unemploymentRate += 2 * severityMultiplier;
                 state.publicConfidence *= (1 - 0.08 * severityMultiplier);
                 state.stockIndex *= (1 - 0.05 * severityMultiplier);
            } else if (event.text.includes('בורסות בעולם צוללות')) {
                state.stockIndex *= (1 - 0.10 * severityMultiplier);
                state.publicConfidence *= (1 - 0.07 * severityMultiplier);
                 state.bankStability *= (1 - 0.05 * severityMultiplier);
            } else if (event.text.includes('קרן גידור גדולה קורסת')) {
                 state.stockIndex *= (1 - 0.05 * severityMultiplier);
                 state.bankStability *= (1 - 0.07 * severityMultiplier);
                 state.publicConfidence *= (1 - 0.04 * severityMultiplier);
            } else if (event.text.includes('מחאות עממיות')) {
                 state.publicConfidence *= (1 - 0.10 * severityMultiplier);
                 state.governmentDebt += 3 * severityMultiplier; // Political pressure -> spending?
            } else if (event.text.includes('מצוקת חוב')) {
                 state.governmentDebt += 7 * severityMultiplier; // Direct impact on debt perception/reality
                 state.publicConfidence *= (1 - 0.08 * severityMultiplier);
                 state.bankStability *= (1 - 0.05 * severityMultiplier); // Contagion risk
            } else if (event.text.includes('בונוסים של בנקאים')) {
                 state.publicConfidence = Math.min(100, state.publicConfidence + 5 * severityMultiplier); // Public likes
                 state.bankStability *= (1 - 0.02 * severityMultiplier); // Banks dislike interference
            } else if (event.text.includes('שינויים רגולטוריים')) {
                 state.publicConfidence = Math.min(100, state.publicConfidence + 3 * severityMultiplier); // Seen as positive step
                 state.bankStability *= (1 - 0.03 * severityMultiplier); // Uncertainty/cost for banks
                 state.stockIndex *= (1 - 0.02 * severityMultiplier); // Markets dislike uncertainty
            } else if (event.text.includes('פשיעה ואלימות')) {
                 state.publicConfidence *= (1 - 0.10 * severityMultiplier);
                 state.unemploymentRate += 0.8 * severityMultiplier; // Reflects underlying issues
                 state.stockIndex *= (1 - 0.03 * severityMultiplier);
            } else if (event.text.includes('"גל שני" של מיתון')) {
                 state.publicConfidence *= (1 - 0.07 * severityMultiplier);
                 state.stockIndex *= (1 - 0.05 * severityMultiplier);
                 state.unemploymentRate += 1 * severityMultiplier;
            } else if (event.text.includes('תיאום מדיניות')) {
                 state.publicConfidence = Math.min(100, state.publicConfidence + 5 * severityMultiplier); // Positive sign
                 state.bankStability = Math.min(100, state.bankStability + 3 * severityMultiplier); // Collaboration helps stability
            }
        });


        // --- Check for game over conditions (more sensitive thresholds) ---
        if (state.bankStability < 10 || state.stockIndex < 1000 || state.publicConfidence < 10 || state.unemploymentRate > 20) {
             endGame();
             elements.outcomeText.innerHTML = `<strong>כישלון!</strong> ביום ${state.time}, הכלכלה קרסה תחת הלחץ. הבנקים כשלו, השווקים התרסקו, והאבטלה הגיעה לשיא. העולם לא התאושש במהירות מההלם.`;
             elements.outcomeDiv.style.display = 'flex'; // Use flex for centering button
             return; // Stop simulation
        }


        // --- End of simulation period ---
        if (state.time >= state.gameDuration) {
             endGame();
             let outcomeHTML = `<strong>סוף הסימולציה</strong> (יום ${state.gameDuration}). ניהלת את המשבר למשך שנה.`;
             let score = (state.stockIndex * 0.1) + (state.bankStability * 1) + (state.publicConfidence * 1) - (state.unemploymentRate * 5) - (state.governmentDebt * 0.5); // Simple scoring

             if (score > 800 && state.unemploymentRate < 8 && state.bankStability > 60 && state.publicConfidence > 50) {
                 outcomeHTML += "<br><strong>הצלחה!</strong> ניווטת את המשבר בצורה יוצאת דופן. הכלכלה מתאוששת במהירות, האמון חוזר, ורוב המוסדות הפיננסיים ניצלו.";
             } else if (score > 400 && state.unemploymentRate < 12 && state.bankStability > 40 && state.publicConfidence > 30) {
                 outcomeHTML += "<br><strong>הישרדות.</strong> הצלחת למנוע קריסה מוחלטת, אך הכלכלה יצאה מהמשבר חבולה, עם אבטלה גבוהה וחוב ציבורי משמעותי. ההתאוששות צפויה להיות ארוכה וכואבת.";
             } else {
                 outcomeHTML += "<br><strong>קשה.</strong> למרות שהגעת לסוף הזמן, הכלכלה עדיין במצב רעוע. יציבות הבנקים נמוכה, האבטלה גבוהה, והאמון בשפל. המשבר אמנם לא הסתיים בקריסה מיידית, אך נראה שהגרוע מכל עדיין לפנינו.";
             }
             elements.outcomeText.innerHTML = outcomeHTML; // Use innerHTML to allow strong tag etc.
             elements.outcomeDiv.style.display = 'flex'; // Use flex for centering button
             return; // Stop simulation
        }


        updateUI();
    }

    // --- Action Handlers ---
    function handleAction(event) {
        const button = event.target;
        const actionType = button.dataset.action;
        const now = state.time;

        // Check cooldown (should be disabled by UI, but double check)
        const lastUsed = state.lastActionTime[actionType] || -Infinity;
        const cooldown = state.actionCooldowns[actionType];
        if (now - lastUsed < cooldown) {
             addNews(`המערכת עדיין מעכלת את הפעולה הקודמת. המתן עוד ${cooldown - (now - lastUsed)} ימים.`, false);
            return;
        }

        // Record action time BEFORE applying effects, to start cooldown immediately
        state.lastActionTime[actionType] = now;

        // Apply action effects (more game-like immediate impact + some delayed/propagated via simulateDay)
        switch (actionType) {
            case 'changeInterestRate':
                const delta = parseFloat(button.dataset.value);
                state.interestRate = Math.max(0, Math.min(10, state.interestRate + delta)); // Limit rate
                addNews(`הריבית שונתה ל-${state.interestRate.toFixed(2)}%.`, true); // Mark as event due to significance
                 state.publicConfidence += delta > 0 ? -5 : 4; // More significant immediate confidence reaction
                 state.stockIndex += delta > 0 ? -150 : 120; // More significant immediate stock reaction
                 state.bankStability += delta > 0 ? 3 : -2; // Small immediate bank margin effect
                 state.unemploymentRate += delta > 0 ? 0.2 : -0.1; // Small immediate unemployment trend shift
                break;
            case 'bailoutBank':
                state.bankStability = Math.min(100, state.bankStability + 25); // Bigger immediate boost to stability
                state.governmentDebt += 15; // High cost
                state.publicConfidence = Math.max(0, state.publicConfidence - 15); // Strong negative public reaction
                state.stockIndex = Math.min(12000, state.stockIndex + 200); // Strong positive market reaction
                 addNews('הממשלה אישרה חילוץ ענק לבנק מרכזי!', true);
                break;
            case 'injectLiquidity':
                state.bankStability = Math.min(100, state.bankStability + 18);
                state.stockIndex = Math.min(12000, state.stockIndex + 150);
                 state.publicConfidence = Math.min(100, state.publicConfidence + 8);
                 addNews('הבנק המרכזי הזרים מיליארדי דולרים לשוק האשראי.', true);
                break;
            case 'tempRegulationChange':
                state.bankStability = Math.min(100, state.bankStability + 10);
                state.publicConfidence = Math.min(100, state.publicConfidence + 5);
                state.stockIndex = Math.max(500, state.stockIndex - 50); // Markets dislike intervention
                 addNews('יושמו תקנות חירום זמניות להגבלת פעילות בשווקים.', true);
                break;
             case 'fiscalStimulus':
                state.unemploymentRate = Math.max(state.unemploymentRate - 2, 2); // More significant impact on unemployment trend
                state.governmentDebt += 20; // Very high cost
                state.publicConfidence = Math.min(100, state.publicConfidence + 12);
                state.stockIndex = Math.min(12000, state.stockIndex + 180);
                 addNews('הממשלה השיקה תוכנית גירוי פיסקלי רחבת היקף.', true);
                break;
        }

        updateUI(); // Update UI immediately after action to show changes and cooldown
    }

    // --- Simulation Controls ---
    function startSimulation() {
        if (!state.isRunning) {
            state.isRunning = true;
            elements.startSimButton.style.display = 'none';
            elements.pauseSimButton.style.display = 'inline-block';
            elements.resetSimButton.style.display = 'inline-block';
            elements.outcomeDiv.style.display = 'none';

             // Disable action buttons that are on cooldown, enable others
             elements.actions.forEach(button => {
                const actionType = button.dataset.action;
                 const lastUsed = state.lastActionTime[actionType] || -Infinity;
                 const cooldown = state.actionCooldowns[actionType];
                 button.disabled = state.time - lastUsed < cooldown;
            });


             addNews('הסימולציה החלה! המשבר לפניך.');

            // Run the first day immediately, then start interval
             simulateDay();
             state.simulationInterval = setInterval(simulateDay, state.simulationSpeed);
        }
    }

    function pauseSimulation() {
        if (state.isRunning) {
            state.isRunning = false;
            clearInterval(state.simulationInterval);
            elements.startSimButton.style.display = 'inline-block'; // Change text to 'Continue' perhaps?
            elements.startSimButton.textContent = 'המשך סימולציה';
            elements.pauseSimButton.style.display = 'none';

             // Ensure action buttons are enabled while paused if cooldown is over
             elements.actions.forEach(button => {
                 const actionType = button.dataset.action;
                 const lastUsed = state.lastActionTime[actionType] || -Infinity;
                 const cooldown = state.actionCooldowns[actionType];
                 if (state.time - lastUsed >= cooldown) {
                     button.disabled = false;
                     button.textContent = button.dataset.originalText; // Restore text
                     button.classList.remove('cooldown');
                 } else {
                      // If still on cooldown, update countdown while paused
                     const remaining = cooldown - (state.time - lastUsed);
                     button.textContent = `${button.dataset.originalText} (${remaining} ימים)`;
                 }
             });

             addNews('הסימולציה הושהתה.', false);
        }
    }

    function endGame() {
        state.isRunning = false;
        clearInterval(state.simulationInterval);
        elements.startSimButton.style.display = 'none';
        elements.pauseSimButton.style.display = 'none';
        elements.resetSimButton.style.display = 'inline-block';
         elements.restartSimOutcomeButton.style.display = 'inline-block'; // Show restart on outcome screen

        // Disable all action buttons at the end
        elements.actions.forEach(button => {
            button.disabled = true;
            button.textContent = button.dataset.originalText; // Restore original text
            button.classList.remove('cooldown');
        });
         addNews('הסימולציה הסתיימה.', false);
    }

     function resetSimulation() {
         clearInterval(state.simulationInterval);
         initializeSimulation();
         addNews('הסימולציה אותחלה.', false);
     }

    // --- Event Listeners ---
    elements.startSimButton.addEventListener('click', startSimulation);
    elements.pauseSimButton.addEventListener('click', pauseSimulation);
    elements.resetSimButton.addEventListener('click', resetSimulation);
     elements.restartSimOutcomeButton.addEventListener('click', resetSimulation); // Bind restart from outcome

    elements.actions.forEach(button => {
        button.addEventListener('click', handleAction);
    });

    elements.toggleExplanationButton.addEventListener('click', () => {
        const isHidden = elements.explanationDiv.style.display === 'none';
        elements.explanationDiv.style.display = isHidden ? 'block' : 'none';
        elements.toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על משברים כלכליים' : 'הצג הסבר על משברים כלכליים';
    });

     // Initial UI update
    updateUI();
});
</script>

<style>
/* General Layout & Typography */
#economic-simulator {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* More modern font */
    display: grid;
    grid-template-areas:
        "dashboard news"
        "actions actions"
        "controls controls"
        "outcome outcome";
    grid-template-columns: 1fr 1fr;
    gap: 25px; /* Increased gap */
    max-width: 1100px; /* Slightly wider */
    margin: 30px auto; /* More margin */
    padding: 30px; /* More padding */
    border: none; /* Remove outer border */
    border-radius: 12px; /* More rounded corners */
    background: linear-gradient(to bottom right, #e0f2f7, #b3e5fc); /* Subtle gradient background */
    direction: rtl;
    text-align: right;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Add subtle shadow */
}

h1, h2 {
    color: #0277bd; /* Darker blue for headings */
    font-weight: bold;
    margin-bottom: 15px;
}

#economic-simulator h2 {
    margin-top: 0;
    font-size: 1.5em; /* Larger subheadings */
    border-bottom: 2px solid #b3e5fc; /* Add subtle underline */
    padding-bottom: 8px;
}

/* Dashboard & Metrics */
#dashboard {
    grid-area: dashboard;
    background-color: #ffffff; /* White background */
    padding: 20px; /* Increased padding */
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
}

.metric {
    margin-bottom: 12px;
    font-size: 1.2em; /* Larger metric text */
    display: flex; /* Use flexbox for alignment */
    justify-content: space-between; /* Space out label and value */
    align-items: center;
    padding: 5px 0;
    border-bottom: 1px dashed #e0e0e0; /* Add subtle separator */
}

.metric:last-child {
     border-bottom: none;
}

.metric-label {
    font-weight: bold;
    color: #555; /* Slightly darker label color */
}

.metric-value {
    color: #007bff; /* Blue color for values */
    font-weight: bold;
    min-width: 60px; /* Ensure value area has minimal width */
    text-align: left; /* Align value to the left */
}

/* Metric Indicators (new element) */
.metric-indicator {
    font-size: 1.1em;
    font-weight: bold;
    width: 1em; /* Fixed width */
    text-align: center;
    margin-right: 5px; /* Space from value */
}

/* Metric value color feedback (animation/flash triggered by JS) */
.metric-flash {
    animation: flashChange 0.5s ease-out;
}

@keyframes flashChange {
    0% { background-color: transparent; }
    50% { background-color: rgba(0, 123, 255, 0.2); } /* Subtle blue flash */
    100% { background-color: transparent; }
}

/* Indicator colors based on JS class on parent */
.metric.is-positive .metric-indicator { color: #28a745; } /* Green for good */
.metric.is-negative .metric-indicator { color: #dc3545; } /* Red for bad */
.metric.is-neutral .metric-indicator { color: #6c757d; } /* Gray for no change or neutral */

/* Metric value text color feedback (based on JS class on value) */
.metric-value.metric-positive { color: #28a745; } /* Green */
.metric-value.metric-negative { color: #dc3545; } /* Red */
.metric-value.metric-neutral { color: #333; } /* Default dark gray */


/* News Feed */
#news-feed {
    grid-area: news;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    max-height: 400px; /* Increased height */
    overflow-y: auto;
    display: flex; /* Use flex for column layout */
    flex-direction: column;
}

#news-items {
    flex-grow: 1; /* Let news items area grow */
    display: flex;
    flex-direction: column; /* Stack items vertically */
    justify-content: flex-end; /* Align items to the bottom initially */
}

.news-item {
    border-bottom: 1px dashed #e0e0e0;
    padding: 10px 0; /* Increased padding */
    margin-bottom: 10px;
    font-size: 1em;
    color: #555;
     /* Initial state for animation */
     opacity: 1;
     transform: translateY(0);
}

.news-item:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

.news-item.event {
    font-weight: bold;
    color: #dc3545; /* Red for events */
    border-bottom: 2px solid #dc3545; /* More prominent border for events */
}

/* Actions */
#actions {
    grid-area: actions;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    text-align: center;
}

#actions button {
    margin: 8px; /* Increased margin */
    padding: 12px 20px; /* Larger padding */
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    border: none;
    border-radius: 6px; /* Slightly more rounded */
    background-color: #007bff; /* Primary blue */
    color: white;
    transition: background-color 0.2s ease, transform 0.1s ease; /* Added transform for press effect */
    min-width: 150px; /* Ensure buttons have minimal width */
}

#actions button:hover:not(:disabled) {
    background-color: #0056b3; /* Darker blue on hover */
    transform: translateY(-2px); /* Subtle lift effect */
}

#actions button:active:not(:disabled) {
     transform: translateY(0); /* Press effect */
}

#actions button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    opacity: 0.7; /* Indicate disabled state */
    transform: none; /* No lift/press when disabled */
}

/* Cooldown styling */
#actions button.cooldown {
     background-color: #ffc107; /* Yellow */
     color: #333;
     cursor: not-allowed;
}
#actions button.cooldown:hover {
    background-color: #e0a800;
}


/* Controls */
#controls {
    grid-area: controls;
    text-align: center;
    padding: 10px 0;
}

#controls button {
    margin: 8px;
    padding: 12px 20px;
    font-size: 1.1em;
    cursor: pointer;
    border: none;
    border-radius: 6px;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

#start-sim {
    background-color: #28a745; /* Green for start */
    color: white;
}

#start-sim:hover:not(:disabled) {
    background-color: #218838;
     transform: translateY(-2px);
}

#pause-sim {
     background-color: #ffc107; /* Yellow for pause */
     color: #333;
}

#pause-sim:hover:not(:disabled) {
    background-color: #e0a800;
     transform: translateY(-2px);
}

#reset-sim, #restart-sim-outcome { /* Apply reset style to both reset buttons */
    background-color: #dc3545; /* Red for reset */
    color: white;
}

#reset-sim:hover:not(:disabled), #restart-sim-outcome:hover:not(:disabled) {
    background-color: #c82333;
     transform: translateY(-2px);
}

#controls button:disabled {
    opacity: 0.7;
    cursor: not-allowed;
     transform: none;
}


/* Outcome */
#outcome {
     grid-area: outcome;
     background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    text-align: center;
    display: flex; /* Use flexbox */
    flex-direction: column;
    align-items: center; /* Center content */
}

#outcome h2 {
    color: #0277bd;
    margin-bottom: 15px;
}

#outcome p {
    font-size: 1.2em;
    color: #333;
    margin-bottom: 20px;
}

#restart-sim-outcome {
     margin-top: 15px;
}


/* Explanation Section */
#toggle-explanation {
    margin-top: 25px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding: 12px 20px;
    font-size: 1.1em;
    cursor: pointer;
    border: 1px solid #b3e5fc; /* Lighter blue border */
    border-radius: 6px;
    background-color: #e1f5fe; /* Lighter blue background */
    color: #0277bd; /* Dark blue text */
    transition: background-color 0.2s ease, border-color 0.2s ease;
    text-align: center;
    max-width: 400px; /* Limit width */
}

#toggle-explanation:hover {
    background-color: #b3e5fc; /* Darker blue on hover */
    border-color: #0277bd;
}

#explanation {
    margin-top: 20px;
    padding: 25px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    line-height: 1.7; /* Improved readability */
    color: #333;
    max-width: 1100px; /* Match simulator width */
    margin-left: auto;
    margin-right: auto;
    direction: rtl;
    text-align: right;
}

#explanation h2 {
     color: #0277bd;
     font-size: 1.4em;
     margin-bottom: 15px;
}

#explanation h3 {
     color: #039be5; /* Medium blue */
     font-size: 1.2em;
     margin-top: 20px;
     margin-bottom: 10px;
     border-bottom: 1px dashed #e0e0e0;
     padding-bottom: 5px;
}

#explanation p {
    margin-bottom: 15px;
    font-size: 1em;
}

#explanation ul {
    margin-bottom: 15px;
    padding-right: 20px; /* Add padding for list bullets */
}

#explanation li {
    margin-bottom: 8px;
}


/* Responsive Design */
@media (max-width: 850px) { /* Adjusted breakpoint */
    #economic-simulator {
        grid-template-areas:
            "dashboard"
            "news"
            "actions"
            "controls"
            "outcome";
        grid-template-columns: 1fr;
        gap: 20px; /* Slightly smaller gap */
        padding: 20px;
        margin: 20px auto;
    }

    #news-feed {
        max-height: 300px; /* Reduce max height on smaller screens */
    }

    .metric {
        flex-direction: column; /* Stack label and value */
        align-items: flex-start; /* Align stacked items to the right */
        border-bottom: 1px dashed #e0e0e0;
        padding-bottom: 8px;
    }

    .metric-label {
        width: auto;
        margin-bottom: 3px; /* Space between label and value */
    }

     .metric-value, .metric-indicator {
        min-width: auto;
        text-align: right; /* Align values right when stacked */
        margin-right: 0;
     }

     .metric-indicator {
         display: inline-block; /* Ensure indicator is inline with value */
         margin-left: 5px; /* Space from value */
     }

     #actions button {
         width: calc(100% - 16px); /* Full width minus margin */
         margin-left: 0;
         margin-right: 0;
     }

     #explanation {
         padding: 20px;
         margin-top: 15px;
     }

     #toggle-explanation {
         width: calc(100% - 40px); /* Full width minus padding */
         max-width: none; /* Remove max width */
     }
}
</style>