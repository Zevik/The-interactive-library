---
title: "מנהל הקמפיין: המסע אל הניצחון (סימולטור אסטרטגיה)"
english_slug: the-campaign-manager-strategy-simulator
category: "מדעי החברה / מדע המדינה ומדיניות ציבורית"
tags: [בחירות, אסטרטגיה פוליטית, קבלת החלטות, פוליטיקה, קמפיין, סימולטור]
---
# מנהל הקמפיין: המסע אל הניצחון

האם יש לכם את מה שצריך כדי להוביל קמפיין בחירות מורכב? צללו לנעלי מנהל הקמפיין, נווטו בין אתגרים בלתי צפויים, קבלו החלטות קריטיות תחת לחץ, וראו האם תוכלו לגייס מספיק תמיכה כדי לנצח ביום הבוחר! האם תתמקדו בטלוויזיה או בדיגיטל? תשקיעו בשטח או באירועים נוצצים? ומה לגבי המועמד עצמו – האם תשמרו על מצב רוח מרומם או תדחפו אותו לקצה?

<div id="simulator-app" class="game-container">
    <div id="game-state" class="panel state-panel">
        <h2>📊 לוח המצב</h2>
        <div class="state-indicators">
            <p>שבועות לבחירות: <span id="weeks-left" class="state-value"></span></p>
            <p>כסף בקופה: <span id="budget" class="state-value budget-value"></span> ₪</p>
            <p>תמיכה נוכחית בסקרים: <span id="polls" class="state-value polls-value"></span>%</p>
        </div>
        <div id="candidate-mood" class="mood-indicator">מצב רוח המועמד: <span id="mood-text" class="mood-value"></span></div>
    </div>

    <div id="decision-area" class="panel decision-panel">
        <h2>🎯 ההחלטה לשבוע זה</h2>
        <p class="decision-prompt">איך נשקיע את המשאבים השבוע?</p>
        <div id="allocation-inputs">
            <div class="allocation-item">
                <label for="tv-spend">📺 קמפיין טלוויזיה:</label>
                <input type="number" id="tv-spend" value="0" min="0" step="1000">
                <span class="currency">₪</span>
            </div>
            <div class="allocation-item">
                <label for="digital-spend">📱 קמפיין דיגיטל:</label>
                <input type="number" id="digital-spend" value="0" min="0" step="1000">
                <span class="currency">₪</span>
            </div>
            <div class="allocation-item">
                <label for="ground-spend">🏃 פעילות שטח:</label>
                <input type="number" id="ground-spend" value="0" min="0" step="1000">
                <span class="currency">₪</span>
            </div>
            <div class="allocation-item">
                <label for="events-spend">🎉 אירועים וכנסים:</label>
                <input type="number" id="events-spend" value="0" min="0" step="1000">
                <span class="currency">₪</span>
            </div>
            <div class="allocation-item">
                <label for="candidate-care">💆 טיפול במועמד (חוסן נפשי):</label>
                <input type="number" id="candidate-care" value="0" min="0" step="1000">
                <span class="currency">₪</span>
            </div>
        </div>
        <p class="total-spend-summary"> סה"כ השקעה שבועית: <span id="total-spend" class="total-spend-value">0</span> ₪</p>
        <button id="submit-decision" class="action-button">קבל החלטה לשבוע הבא</button>
    </div>

    <div id="results-area" class="panel results-panel">
        <h2>📈 מה קרה השבוע?</h2>
        <div id="weekly-results" class="results-log"></div>
        <div id="events-log" class="events-log"></div>
    </div>

    <div id="end-game-area" class="panel end-game-panel" style="display: none;">
        <h2>🏆 תוצאות סופיות! 🏆</h2>
        <div id="final-results" class="final-message"></div>
        <button id="restart-game" class="action-button primary">התחל קמפיין חדש</button>
    </div>
</div>

<button id="show-explanation-button" class="secondary-button">הצג/הסתר הסבר תיאורטי</button>

<div id="explanation" class="explanation-panel" style="display: none;">
    <h2>הסבר תיאורטי: ניהול קמפיין בחירות</h2>

    <p><strong>מבוא: מהו קמפיין בחירות ומה תפקידו של מנהל הקמפיין.</strong><br>
    קמפיין בחירות הוא מאמץ מרוכז ומתוכנן שמטרתו להשיג את תמיכת הציבור הדרושה לבחירת מועמד או מפלגה לתפקיד ציבורי. מנהל הקמפיין הוא האדם האחראי על התכנון, הביצוע והפיקוח על כלל פעילויות הקמפיין. תפקידו כולל ניהול צוות, קבלת החלטות אסטרטגיות וטקטיות, ניהול תקציב, והתמודדות עם אתגרים ושינויים בזמן אמת.</p>

    <p><strong>היבטים מרכזיים בניהול קמפיין: הגדרת מטרות, ניתוח זירה פוליטית, בניית אסטרטגיה.</strong><br>
    כל קמפיין מתחיל בהגדרת מטרות ברורות - לרוב, אחוז תמיכה מסוים או מספר מנדטים. לאחר מכן, מתבצע ניתוח מעמיק של הזירה הפוליטית: המועמדים היריבים, הקהלים השונים, הנושאים הבוערים והלך הרוח הציבורי. על בסיס ניתוח זה, נבנית אסטרטגיה כוללת שמתווה את הדרך להשגת המטרות.</p>

    <p><strong>תהליכי קבלת החלטות אסטרטגיות: ניהול תקציב, בחירת מסרים, זיהוי קהלי יעד והגעה אליהם.</strong><br>
    ניהול תקציב הוא ליבת העשייה של מנהל קמפיין. משאבים כספיים מוגבלים דורשים החלטות קשות היכן להשקיע. בחירת מסרים נכונים לקהלים שונים חיונית לגיוס תמיכה. קמפיין יעיל מזהה את קהלי היעד המרכזיים ופונה אליהם בערוצים ובמסרים הרלוונטיים ביותר.</p>

    <p><strong>כלים תומכי החלטה: סקרים, קבוצות מיקוד, ניתוח דאטה.</strong><br>
    כדי לקבל החלטות מושכלות, מנהלי קמפיין מסתמכים על נתונים. סקרים מספקים תמונת מצב עדכנית של דעת הקהל. קבוצות מיקוד מאפשרות הבנה עמוקה יותר של תגובות הציבור למסרים. ניתוח דאטה ממאגרי מידע שונים (כמו רשתות חברתיות או רשימות מצביעים) עוזר לזהות מגמות, לפלח קהלים ולמקד מאמצים.</p>

    <p><strong>השפעת גורמים חיצוניים: אירועים בלתי צפויים, תגובת יריבים, סיקור תקשורתי.</strong><br>
    זירת הקמפיין היא דינמית מאוד. אירועים לא צפויים (משבר ביטחוני, פרשת שחיתות), פעולות של יריבים פוליטיים וסיקור תקשורתי משפיעים באופן דרמטי על התקדמות הקמפיין. מנהל הקמפיין חייב להיות ערוך להגיב במהירות וביעילות לשינויים אלו.</p>

    <p><strong>הקשר בין החלטות לתוצאות: הדגמה באמצעות הסימולטור.</strong><br>
    הסימולטור מדגים את הקשר הסיבתי בין ההחלטות שאתם מקבלים (הקצאת תקציב, תגובה לאירועים) לבין התוצאות (שינויים בסקרים, מצב התקציב, תגובת המדיה). כל החלטה נושאת בחובה סיכון וסיכוי ומשפיעה על המסלול של הקמפיין.</p>

    <p><strong>סיכום: מורכבות תהליך קבלת ההחלטות בקמפיין והחשיבות של גמישות ותגובה מהירה.</strong><br>
    ניהול קמפיין הוא אתגר מורכב הדורש חשיבה אסטרטגית, הבנה טקטית, ניהול משאבים יעיל, ויכולת להגיב מהר ובתבונה למציאות משתנה. הסימולטור מאפשר לכם להתנסות במורכבות הזו בסביבה מבוקרת וללמוד על האתגרים הייחודיים של מנהלי הקמפיין.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // --- Game State Variables ---
    let weeksLeft;
    let budget;
    let pollPercentage;
    let candidateMood; // 0 (Bad) to 100 (Excellent)

    const initialBudget = 3000000; // הגדלת תקציב התחלה לחוויה עשירה יותר
    const initialPolls = 10; // התחלה נמוכה יותר לאתגר
    const initialWeeks = 15; // יותר שבועות למשחק ארוך יותר
    const initialMood = 80; // מצב רוח התחלתי גבוה יותר

    // Cost-effectiveness and impact (per 10000 ₪)
    // Added more nuance: Digital efficiency slightly depends on mood, Ground/Events boost mood more if budget is high
    const spendingEffects = {
        tv: { pollGain: 0.07, moodEffect: -0.015, description: '📺 טלוויזיה: מגיע לקהל רחב, אך לחוץ למועמד.' },
        digital: { pollGain: 0.13, moodEffect: -0.008, description: '📱 דיגיטל: ממוקד וגמיש, פחות מעיק.' },
        ground: { pollGain: 0.09, moodEffect: 0.015, description: '🏃 שטח: בונה קשר אישי ותמיכה מקומית, מחזק את המועמד.' },
        events: { pollGain: 0.16, moodEffect: 0.025, description: '🎉 אירועים: פוטנציאל השפעה גבוה, אם מצליח -boost למורל.' },
        candidateCare: { pollGain: -0.02, moodEffect: 0.3, description: '💆 טיפול במועמד: מחזק את המועמד ישירות, בא על חשבון זמן קמפיין אחר.' }
    };

    // Event definitions
    const events = [
        {
            type: 'positive',
            text: '🎉 הצלחה מסחררת! המועמד התראיין בפריים טיים וזכה לתשואות! <br> 📈 דעת הקהל משתפרת משמעותית.',
            effect: (state) => ({ polls: state.polls + Math.random() * (6 - 3) + 3, budget: state.budget, mood: state.mood + Math.random() * 12 + 5 }) // +3-6% polls, +5-17 mood
        },
        {
            type: 'negative',
            text: '🚨 משבר! המועמד נתפס באמירה שנויה במחלוקת או שודר סרטון מביך. <br> 📉 נגרם נזק תדמיתי כבד.',
            effect: (state) => ({ polls: Math.max(state.polls * 0.8, state.polls - (Math.random() * (5 - 3) + 3)), budget: state.budget, mood: Math.max(state.mood * 0.7, state.mood - Math.random() * 20 - 10) }) // -3-5% polls or 20% drop (whichever is worse), -10-30 mood or 30% drop
        },
        {
            type: 'external',
            text: '📰 הזירה הפוליטית רותחת! היריב המרכזי עשה טעות קריטית או נקלע למשבר. <br> 🚀 זה הזמן לנצל את המומנטום!',
            effect: (state) => ({ polls: state.polls + Math.random() * (4 - 2) + 2, budget: state.budget, mood: state.mood + Math.random() * 5 }) // +2-4% polls, + up to 5 mood
        },
        {
            type: 'financial',
            text: '💰 בעיות כספיות! התגלתה תקלה בניהול הכספים / ספק מרכזי לא שולם. <br> 💸 חלק מהתקציב הלך לאיבוד או נתקע.',
            effect: (state) => ({ polls: state.polls - Math.random() * 1, budget: Math.max(0, state.budget - (Math.random() * (0.15 - 0.05) + 0.05) * initialBudget), mood: state.mood - Math.random() * 8 }) // - up to 1% polls, Lose 5-15% of initial budget, - up to 8 mood
        },
         {
            type: 'mood',
            text: '😞 המועמד קורס מהלחץ! הוא זקוק לתמיכה דחופה. <br> 📉 המצב משפיע ישירות על יכולת השכנוע.',
            effect: (state) => ({ polls: Math.max(state.polls * 0.95, state.polls - Math.random() * 3), budget: state.budget, mood: Math.max(0, state.mood - Math.random() * 15 - 5) }) // - up to 3% polls or 5% drop, -5-20 mood
        },
         {
            type: 'neutral',
            text: '🤫 שבוע שקט במיוחד. לא היו אירועים דרמטיים. <br> ✨ ההתקדמות תלויה רק בהשקעה ובתכנון שלכם.',
            effect: (state) => ({ polls: state.polls + (Math.random() - 0.5) * 0.2, budget: state.budget, mood: state.mood + (Math.random() - 0.5) * 2 }) // Tiny random fluctuation
        }
    ];
    const eventChance = 0.6; // 60% chance of a specific event per week

    // --- DOM Elements ---
    const weeksLeftSpan = document.getElementById('weeks-left');
    const budgetSpan = document.getElementById('budget');
    const pollsSpan = document.getElementById('polls');
    const candidateMoodSpan = document.getElementById('mood-text');

    const tvSpendInput = document.getElementById('tv-spend');
    const digitalSpendInput = document.getElementById('digital-spend');
    const groundSpendInput = document.getElementById('ground-spend');
    const eventsSpendInput = document.getElementById('events-spend');
    const candidateCareInput = document.getElementById('candidate-care');
    const totalSpendSpan = document.getElementById('total-spend');
    const submitButton = document.getElementById('submit-decision');

    const weeklyResultsDiv = document.getElementById('weekly-results');
    const eventsLogDiv = document.getElementById('events-log');
    const endGameAreaDiv = document.getElementById('end-game-area');
    const finalResultsDiv = document.getElementById('final-results');
    const restartButton = document.getElementById('restart-game');

    const showExplanationButton = document.getElementById('show-explanation-button');
    const explanationDiv = document.getElementById('explanation');

    const allocationInputs = document.querySelectorAll('#allocation-inputs input[type="number"]');

    // --- Game Functions ---

    function startGame() {
        weeksLeft = initialWeeks;
        budget = initialBudget;
        pollPercentage = initialPolls;
        candidateMood = initialMood;
        weeklyResultsDiv.innerHTML = '';
        eventsLogDiv.innerHTML = '';
        endGameAreaDiv.style.display = 'none';
        document.getElementById('simulator-app').style.display = 'grid'; // Ensure simulator is visible
        submitButton.disabled = false;
        resetInputs();
        renderState();
    }

    function renderState() {
        // Add animation class for smooth transitions
        document.querySelectorAll('.state-value').forEach(el => el.classList.add('animate-change'));

        weeksLeftSpan.textContent = weeksLeft;
        budgetSpan.textContent = budget.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, ","); // Format with commas
        pollsSpan.textContent = pollPercentage.toFixed(1);
        candidateMoodSpan.textContent = getMoodText(candidateMood);
        updateMoodDisplay(candidateMood); // Update mood color/icon

        // Update input max based on current budget
        allocationInputs.forEach(input => {
            input.max = budget;
             if (parseInt(input.value) > budget) { // Reset if current value exceeds new max
                input.value = budget;
            }
        });

        // Check if enough budget for any spending and if total spent is non-zero
        const totalAllocated = calculateTotalSpend();
         if (totalAllocated > budget) {
             submitButton.disabled = true;
             submitButton.textContent = '🚫 תקציב חורג!';
             submitButton.classList.add('warning');
             submitButton.classList.remove('primary');
         } else if (totalAllocated === 0) {
             submitButton.disabled = true;
             submitButton.textContent = '👈 הקצו תקציב כדי להמשיך';
             submitButton.classList.remove('warning', 'primary');
         }
          else {
            submitButton.disabled = false;
            submitButton.textContent = `🎉 קבל החלטה לשבוע הבא (${totalAllocated.toLocaleString()} ₪)`;
             submitButton.classList.remove('warning');
             submitButton.classList.add('primary');
        }

         // Remove animation class after a short delay
        setTimeout(() => {
             document.querySelectorAll('.state-value').forEach(el => el.classList.remove('animate-change'));
        }, 500); // Match CSS transition duration
    }

    function getMoodText(mood) {
        if (mood >= 90) return '😀 מצוין!';
        if (mood >= 70) return '😊 טוב';
        if (mood >= 50) return '😐 יציב';
        if (mood >= 30) return '😟 לחוץ';
        return '😩 במשבר';
    }

     function updateMoodDisplay(mood) {
        const moodElement = document.getElementById('candidate-mood');
        moodElement.classList.remove('mood-excellent', 'mood-good', 'mood-stable', 'mood-tense', 'mood-crisis');
        if (mood >= 90) moodElement.classList.add('mood-excellent');
        else if (mood >= 70) moodElement.classList.add('mood-good');
        else if (mood >= 50) moodElement.classList.add('mood-stable');
        else if (mood >= 30) moodElement.classList.add('mood-tense');
        else moodElement.classList.add('mood-crisis');
     }


    function calculateTotalSpend() {
        let total = 0;
        allocationInputs.forEach(input => {
            total += parseInt(input.value) || 0;
        });
        return total;
    }

    function resetInputs() {
        allocationInputs.forEach(input => {
            input.value = 0;
        });
        totalSpendSpan.textContent = '0';
         submitButton.disabled = true; // Disable button on reset
         submitButton.textContent = '👈 הקצו תקציב כדי להמשיך';
         submitButton.classList.remove('warning', 'primary');
    }

    function processDecision() {
        const tvSpend = parseInt(tvSpendInput.value) || 0;
        const digitalSpend = parseInt(digitalSpendInput.value) || 0;
        const groundSpend = parseInt(groundSpendInput.value) || 0;
        const eventsSpend = parseInt(eventsSpendInput.value) || 0;
        const candidateCareSpend = parseInt(candidateCareInput.value) || 0;
        const totalSpentThisWeek = tvSpend + digitalSpend + groundSpend + eventsSpend + candidateCareSpend;

        if (totalSpentThisWeek > budget) {
            alert('אין מספיק תקציב להחלטה זו!'); // Should be prevented by button state, but good fallback
            return;
        }

        budget -= totalSpentThisWeek;
        let pollChange = 0;
        let moodChange = 0;

        // Calculate impact based on spending, scaled by initial budget and current mood
        const spendingUnit = initialBudget / 10000; // Base unit for effectiveness
        const moodMultiplier = (candidateMood / 100 - 0.5) * 0.5 + 1; // 0.75 to 1.25 multiplier based on mood (50 mood = 1x)
        const currentTotalBudgetRatio = budget / initialBudget; // Ratio of current budget to initial budget

        // Apply effects with mood and potential budget influence
        pollChange += (tvSpend / 10000) * spendingEffects.tv.pollGain * moodMultiplier;
        moodChange += (tvSpend / 10000) * spendingEffects.tv.moodEffect; // TV stress less dependent on mood

        // Digital effectiveness slightly boosted by high mood
        pollChange += (digitalSpend / 10000) * spendingEffects.digital.pollGain * moodMultiplier * (1 + (candidateMood / 100) * 0.1);
        moodChange += (digitalSpend / 10000) * spendingEffects.digital.moodEffect;

        // Ground/Events mood boost is higher if overall budget is healthy (implies better resourced logistics)
        pollChange += (groundSpend / 10000) * spendingEffects.ground.pollGain * moodMultiplier;
        moodChange += (groundSpend / 10000) * spendingEffects.ground.moodEffect * (1 + currentTotalBudgetRatio * 0.5);

        pollChange += (eventsSpend / 10000) * spendingEffects.events.pollGain * moodMultiplier * (1 + currentTotalBudgetRatio * 0.3); // Events effectiveness slightly tied to budget
        moodChange += (eventsSpend / 10000) * spendingEffects.events.moodEffect * (1 + currentTotalBudgetRatio * 0.5);


        pollChange += (candidateCareSpend / 10000) * spendingEffects.candidateCare.pollGain * moodMultiplier; // Care slightly impacts polls effectiveness too
        moodChange += (candidateCareSpend / 10000) * spendingEffects.candidateCare.moodEffect;

         // Diminishing returns / scaling for very high spending in one area? (Optional - keep simple for now)
         // Example: If tvSpend > budget * 0.5, reduce its pollGain effect

        // Add variance - higher variance if mood is low
        const variance = (1 - candidateMood / 100) * 0.8 + 0.2; // Variance is 0.2x at 100 mood, 1x at 0 mood
        pollChange += (Math.random() - 0.5) * 1 * variance; // Random +/- 0.5% * variance
        moodChange += (Math.random() - 0.5) * 3 * variance; // Random +/- 1.5 mood * variance


        // Candidate mood directly affects poll change (positive mood helps, negative hurts)
        const moodDirectPollEffect = (candidateMood - 50) / 100 * 0.7; // -0.35 to +0.35 based on mood
        pollChange += moodDirectPollEffect;

        // --- Apply Changes ---
        const previousPolls = pollPercentage;
        const previousMood = candidateMood;

        pollPercentage += pollChange;
        candidateMood += moodChange;

        // Check for negative budget (shouldn't happen with checks but safety)
        if (budget < 0) budget = 0;

        // Clamp values
        pollPercentage = Math.max(0.1, Math.min(100, pollPercentage)); // Polls minimum 0.1%
        candidateMood = Math.max(0, Math.min(100, candidateMood));


        // --- Log Weekly Results ---
        const weeklyResultElement = document.createElement('div');
        weeklyResultElement.classList.add('weekly-summary');
        const pollDiff = pollPercentage - previousPolls;
        const moodDiff = candidateMood - previousMood;

        let resultHtml = `<h4>סיכום שבוע ${initialWeeks - weeksLeft + 1}:</h4>`;
        resultHtml += `<p>הוצאתם <span class="spend-summary-value">${totalSpentThisWeek.toLocaleString()} ₪</span>.</p>`;
        resultHtml += `<p class="poll-change ${pollDiff >= 0 ? 'positive' : 'negative'}">סקרים: ${pollDiff >= 0 ? '📈 עלייה' : '📉 ירידה'} של ${Math.abs(pollDiff).toFixed(1)}% (לסה"כ ${pollPercentage.toFixed(1)}%)</p>`;
        resultHtml += `<p class="mood-change ${moodDiff >= 0 ? 'positive' : 'negative'}">מצב רוח המועמד: ${moodDiff >= 0 ? '😊 שיפור' : '😟 החמרה'} של ${Math.abs(moodDiff).toFixed(1)} נקודות (לסה"כ ${candidateMood.toFixed(0)})</p>`;

         weeklyResultElement.innerHTML = resultHtml;
        weeklyResultsDiv.prepend(weeklyResultElement); // Add to the top

        // --- Process Random Event ---
        if (Math.random() < eventChance) {
            const randomEvent = events[Math.floor(Math.random() * events.length)];
             // Apply event effects relative to current state *after* spending effects
            const eventEffectResult = randomEvent.effect({ polls: pollPercentage, budget: budget, mood: candidateMood });

            // Calculate change *from* the state after spending, *to* the state after event
            const eventPollChange = eventEffectResult.polls - pollPercentage;
            const eventBudgetChange = eventEffectResult.budget - budget;
            const eventMoodChange = eventEffectResult.mood - candidateMood;

            // Update state variables based on event
            pollPercentage = Math.max(0.1, Math.min(100, eventEffectResult.polls));
            budget = Math.max(0, eventEffectResult.budget);
            candidateMood = Math.max(0, Math.min(100, eventEffectResult.mood));

             // Log event details
            const eventTextElement = document.createElement('div');
             eventTextElement.classList.add('event-message', randomEvent.type);
            let eventHtml = `<h4>אירוע השבוע (${initialWeeks - weeksLeft + 1}):</h4>`;
             eventHtml += `<p>${randomEvent.text}</p>`;
            eventHtml += `<p class="event-effect-summary">השפעת האירוע: `;
            if (eventPollChange !== 0) eventHtml += `סקרים ${eventPollChange >= 0 ? '+' : ''}${eventPollChange.toFixed(1)}% `;
            if (eventBudgetChange !== 0) eventHtml += `כסף ${eventBudgetChange >= 0 ? '+' : ''}${eventBudgetChange.toFixed(0)}₪ `;
            if (eventMoodChange !== 0) eventHtml += `מצב רוח ${eventMoodChange >= 0 ? '+' : ''}${eventMoodChange.toFixed(1)} `;
            eventHtml += `</p>`;

            eventTextElement.innerHTML = eventHtml;
            eventsLogDiv.prepend(eventTextElement); // Add to the top

        } else {
             const eventTextElement = document.createElement('div');
             eventTextElement.classList.add('event-message', 'neutral');
            eventTextElement.innerHTML = `<h4>אירוע השבוע (${initialWeeks - weeksLeft + 1}):</h4><p>🤫 שבוע שקט במיוחד. לא היו אירועים דרמטיים.</p>`;
             eventsLogDiv.prepend(eventTextElement);
        }


        weeksLeft--;

        if (weeksLeft <= 0) {
            endGame();
        } else {
            resetInputs(); // Reset inputs for the next week
            renderState(); // Render the new state
        }
    }

    function endGame() {
        document.getElementById('simulator-app').style.display = 'none';
        endGameAreaDiv.style.display = 'block';

        let resultMessage = '';
        let resultClass = '';
        if (pollPercentage >= 35) { // Example winning threshold - adjusted for starting lower
            resultMessage = `<p>🎉 ניצחון מוחץ! 🎉</p><p>הגעתם לבחירות עם <span class="final-poll-win">${pollPercentage.toFixed(1)}%</span> תמיכה! ניהול הקמפיין המבריק שלכם הוביל לניצחון גדול!</p>`;
            resultClass = 'win';
        } else if (pollPercentage >= 25) {
             resultMessage = `<p>👍 תוצאה מכובדת</p><p>הגעתם לבחירות עם <span class="final-poll-ok">${pollPercentage.toFixed(1)}%</span> תמיכה. הקמפיין הצליח לגייס תמיכה משמעותית, אך כנראה לא מספיקה לניצחון ישיר. ייתכן שתהיו לשון מאזניים.</p>`;
            resultClass = 'ok';
        } else if (pollPercentage >= 15) {
             resultMessage = `<p>😟 קמפיין מאתגר</p><p>הגעתם לבחירות עם <span class="final-poll-meh">${pollPercentage.toFixed(1)}%</span> תמיכה. התוצאה נמוכה מהצפוי. נראה שהיו קשיים לגייס מספיק מצביעים.</p>`;
             resultClass = 'meh';
        }
        else {
            resultMessage = `<p>😩 הפסד צורב</p><p>הגעתם לבחירות עם <span class="final-poll-lose">${pollPercentage.toFixed(1)}%</span> תמיכה. הקמפיין לא הצליח לזנק ואיבד תמיכה בדרך. יש לנתח את הכישלון לקראת הפעם הבאה.</p>`;
             resultClass = 'lose';
        }

        finalResultsDiv.innerHTML = `${resultMessage}<p>נותר בקופה: <span class="final-budget">${budget.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, ",")} ₪</span></p>`;
         endGameAreaDiv.classList.add(resultClass); // Add class for styling the end screen
    }

    // --- Event Listeners ---

    allocationInputs.forEach(input => {
        input.addEventListener('input', () => {
             // Ensure input is not negative
            if (input.value < 0) input.value = 0;
             // Cap input at current budget
             if (parseInt(input.value) > budget) input.value = budget;

            const total = calculateTotalSpend();
            totalSpendSpan.textContent = total.toLocaleString(); // Format with commas

            // Update button state and text dynamically
            if (total > budget) {
                 submitButton.disabled = true;
                 submitButton.textContent = '🚫 תקציב חורג!';
                  submitButton.classList.add('warning');
                  submitButton.classList.remove('primary');
             } else if (total === 0){
                 submitButton.disabled = true;
                 submitButton.textContent = '👈 הקצו תקציב כדי להמשיך';
                 submitButton.classList.remove('warning', 'primary');
             }
             else {
                 submitButton.disabled = false;
                 submitButton.textContent = `🎉 קבל החלטה לשבוע הבא (${total.toLocaleString()} ₪)`;
                  submitButton.classList.remove('warning');
                  submitButton.classList.add('primary');
             }
        });
    });


    submitButton.addEventListener('click', processDecision);
    restartButton.addEventListener('click', () => {
         endGameAreaDiv.classList.remove('win', 'ok', 'meh', 'lose'); // Remove previous result class
        startGame();
    });

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        showExplanationButton.textContent = isHidden ? 'הסתר הסבר תיאורטי' : 'הצג/הסתר הסבר תיאורטי'; // Keep consistent text
    });


    // --- Initialization ---
    startGame();
});
</script>

<style>
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.7;
    margin: 0;
    padding: 20px;
    direction: rtl; /* Right-to-left for Hebrew */
    text-align: right;
    background: linear-gradient(to bottom right, #f0f4f8, #d9e2ec); /* Subtle gradient background */
    color: #333;
    min-height: 100vh; /* Full viewport height */
}

h1 {
    color: #004085;
    text-align: center;
    margin-bottom: 20px;
    font-size: 2.2em;
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

h2 {
    color: #0056b3;
    margin-top: 0;
    padding-bottom: 8px;
    border-bottom: 2px solid #007bff; /* Stronger separator */
    margin-bottom: 15px;
    font-size: 1.5em;
}

.game-container {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    margin-bottom: 30px;
    display: grid;
    grid-template-columns: 1fr 1fr; /* Two columns */
    gap: 30px; /* More space between columns */
}

.panel {
     background-color: #f8f9fa; /* Lighter panel background */
     padding: 20px;
     border-radius: 8px;
     border: 1px solid #e9ecef;
     box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
}

.state-panel {
     grid-column: span 2; /* Spans across both columns */
     text-align: center;
     display: flex;
     flex-direction: column;
     align-items: center;
}

.state-indicators {
    display: flex;
    justify-content: center;
    gap: 30px; /* Space out indicators */
    flex-wrap: wrap; /* Allow wrapping on small screens */
}

.state-indicators p, .mood-indicator {
    margin: 5px 0;
    font-size: 1.1em;
    font-weight: normal;
    display: flex;
    align-items: center;
}

.state-indicators p span, .mood-indicator span {
    font-weight: bold;
    margin-right: 5px; /* Space between label and value */
}

.state-value {
    color: #007bff;
    transition: color 0.5s ease, transform 0.5s ease; /* Smooth transition */
}

.state-value.animate-change {
    color: #28a745; /* Highlight color when changing */
    transform: scale(1.05); /* Slight bounce effect */
}

.budget-value { color: #28a745; } /* Green for budget */
.polls-value { color: #ffc107; } /* Yellow/Orange for polls */


/* Candidate Mood Styling */
.mood-indicator {
    margin-top: 15px;
    font-style: normal; /* Remove italic */
    font-size: 1em;
     border-top: 1px dashed #ced4da;
     padding-top: 10px;
     width: 100%;
     text-align: center;
     justify-content: center;
}

.mood-value {
     font-weight: bold;
     transition: color 0.5s ease;
     margin-right: 5px;
}

.mood-excellent .mood-value { color: #28a745; } /* Green */
.mood-good .mood-value { color: #17a2b8; } /* Cyan */
.mood-stable .mood-value { color: #007bff; } /* Blue */
.mood-tense .mood-value { color: #ffc107; } /* Yellow */
.mood-crisis .mood-value { color: #dc3545; } /* Red */


.decision-panel {
    grid-column: 1; /* Takes the first column */
}

.results-panel {
     grid-column: 2; /* Takes the second column */
}

.decision-prompt {
    font-size: 1.1em;
    margin-bottom: 20px;
    color: #555;
}

#allocation-inputs {
    display: flex;
    flex-direction: column;
    gap: 15px; /* More space between input items */
    margin-bottom: 20px;
}

.allocation-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px dotted #ced4da;
}

.allocation-item:last-child {
    border-bottom: none;
}

.allocation-item label {
    flex-grow: 1;
    margin-left: 10px;
    font-weight: bold;
    color: #495057;
}

.allocation-item input[type="number"] {
    width: 100px; /* Wider input field */
    padding: 8px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    text-align: left; /* Align numbers left */
    direction: ltr; /* Force LTR for numbers/currency */
    font-size: 1em;
    -moz-appearance: textfield; /* Hide arrow buttons in Firefox */
}

.allocation-item input[type="number"]::-webkit-outer-spin-button,
.allocation-item input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none; /* Hide arrow buttons in Chrome, Safari, Edge */
    margin: 0;
}

.currency {
    margin-left: 5px;
    color: #6c757d;
}


.total-spend-summary {
    font-size: 1.1em;
    margin-top: 15px;
    padding-top: 10px;
    border-top: 1px dashed #ced4da;
}

.total-spend-value {
    font-weight: bold;
    color: #dc3545; /* Red for spend */
    font-size: 1.2em;
}

.action-button {
    display: block;
    width: 100%;
    padding: 12px 20px;
    font-size: 1.1em;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    margin-top: 20px;
    transition: background-color 0.3s ease, opacity 0.3s ease;
    font-weight: bold;
    text-align: center;
}

.action-button.primary {
    background-color: #007bff;
    color: white;
}

.action-button.primary:hover:not(:disabled) {
    background-color: #0056b3;
}

.action-button.warning {
     background-color: #ffc107;
     color: #333;
}

.action-button.warning:hover:not(:disabled) {
     background-color: #e0a800;
}

.action-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    opacity: 0.7;
}

.secondary-button {
     display: block;
    width: auto;
    padding: 10px 20px;
    margin: 20px auto; /* Center the button */
    background-color: #6c757d;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
}

.secondary-button:hover {
    background-color: #5a6268;
}


.results-log, .events-log {
    max-height: 300px; /* Increased height for more history */
    overflow-y: auto;
    padding-top: 10px;
    margin-top: 10px;
    border-top: 1px solid #cce5ff; /* Keep separator */
}

.weekly-summary, .event-message {
    margin-bottom: 15px;
    padding: 10px;
    border-radius: 6px;
    border-bottom: 1px solid #dee2e6; /* Subtle separator */
    font-size: 0.95em;
    line-height: 1.5;
}

.weekly-summary h4, .event-message h4 {
    margin-top: 0;
    margin-bottom: 8px;
    color: #004085; /* Match heading color */
    font-size: 1.1em;
    font-weight: bold;
}

.weekly-summary p, .event-message p {
    margin: 5px 0;
}

.spend-summary-value {
     font-weight: bold;
     color: #dc3545; /* Red */
}

.poll-change.positive { color: #28a745; font-weight: bold; } /* Green */
.poll-change.negative { color: #dc3545; font-weight: bold; } /* Red */
.mood-change.positive { color: #17a2b8; font-weight: bold; } /* Cyan */
.mood-change.negative { color: #ffc107; font-weight: bold; } /* Yellow */

/* Event message specific styling */
.event-message.positive { background-color: #d4edda; border-color: #c3e6cb; color: #155724; } /* Light green */
.event-message.negative { background-color: #f8d7da; border-color: #f5c6cb; color: #721c24; } /* Light red */
.event-message.external { background-color: #fff3cd; border-color: #ffeeba; color: #856404; } /* Light yellow */
.event-message.financial { background-color: #e2d9eb; border-color: #d3c0d8; color: #4f3073; } /* Light purple */
.event-message.mood { background-color: #d2f4f7; border-color: #bfecf2; color: #0c5460; } /* Light cyan */
.event-message.neutral { background-color: #e9ecef; border-color: #dee2e6; color: #495057; } /* Light gray */

.event-message p strong {
    color: inherit; /* Inherit color from parent div */
}

.event-effect-summary {
    font-style: italic;
    font-size: 0.9em;
    margin-top: 8px;
    color: #555; /* Darker gray */
}


.end-game-panel {
    text-align: center;
    padding: 30px;
    border-radius: 12px;
    margin-top: 30px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    border: none; /* Remove border */
}

.end-game-panel.win { background-color: #d4edda; color: #155724; }
.end-game-panel.ok { background-color: #fff3cd; color: #856404; }
.end-game-panel.meh { background-color: #f8d7da; color: #721c24; }
.end-game-panel.lose { background-color: #e2e3e5; color: #495057; }


.end-game-panel h2 {
    margin-bottom: 20px;
    font-size: 2em;
    border-bottom: none; /* No border in end game */
    color: inherit; /* Inherit color from parent */
}

.final-message p {
    font-size: 1.2em;
    margin-bottom: 15px;
    font-weight: bold;
}

.final-message span {
    font-size: 1.3em;
    font-weight: bold;
}

.final-poll-win { color: #28a745; }
.final-poll-ok { color: #ffc107; }
.final-poll-meh { color: #dc3545; }
.final-poll-lose { color: #6c757d; }
.final-budget { color: #007bff; }


.end-game-panel .action-button {
    width: auto;
    padding: 12px 25px;
    margin-top: 20px;
    display: inline-block; /* Make button inline-block to center */
}

.explanation-panel {
    background-color: #e9ecef;
    padding: 25px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
    border-right: 5px solid #007bff; /* Add a visual marker */
    line-height: 1.7;
    color: #333;
}

.explanation-panel h2 {
    color: #004085;
    text-align: right;
    margin-top: 0;
    border-bottom: 2px solid #007bff;
    padding-bottom: 8px;
    margin-bottom: 15px;
    font-size: 1.5em;
}

.explanation-panel p {
    margin-bottom: 18px;
}

.explanation-panel p strong {
    color: #0056b3;
    font-weight: bold;
}

/* Responsive adjustments */
@media (max-width: 992px) { /* Adjusted breakpoint for better layout */
    .game-container {
        grid-template-columns: 1fr; /* Stack columns on smaller screens */
        gap: 20px;
    }

    .decision-panel, .results-panel, .state-panel {
         grid-column: span 1; /* Ensure they stack */
    }

    .state-indicators {
        flex-direction: column; /* Stack indicators */
        gap: 10px;
    }
    .state-indicators p, .mood-indicator {
        justify-content: flex-end; /* Align text to the right */
        width: 100%;
    }
     .state-indicators p span, .mood-indicator span {
        margin-right: 0;
        margin-left: 5px;
    }
}

@media (max-width: 576px) {
    body {
        padding: 15px;
    }
    h1 {
        font-size: 1.8em;
    }
    h2 {
        font-size: 1.3em;
    }
    .game-container, .explanation-panel, .end-game-panel {
        padding: 15px;
    }
     .allocation-item input[type="number"] {
        width: 80px; /* Make inputs a bit smaller */
        padding: 6px 8px;
        font-size: 0.9em;
    }
     .action-button, .secondary-button {
        font-size: 1em;
        padding: 10px 15px;
    }
    .final-message p {
        font-size: 1.1em;
    }
     .final-message span {
        font-size: 1.2em;
    }
}
</style>
```