---
title: "פאזל הרפרטואר: אתגרי הניהול האמנותי בתיאטרון"
english_slug: art-of-decision-choosing-a-theatre-repertoire
category: "ניהול ועסקים / ניהול"
tags: [תיאטרון, ניהול אמנותי, קבלת החלטות, רפרטואר, מנהל אמנותי, סימולציה]
---
# פאזל הרפרטואר: אתגרי הניהול האמנותי בתיאטרון

המסך עולה על עונה חדשה, וכל העיניים נשואות למנהל האמנותי. הוא חייב להכריע: אילו הצגות ימלאו את האולמות, יעוררו שיח ויגדירו את זהות התיאטרון לשנה הקרובה? זו אינה רק שאלה של טעם אמנותי, אלא ריקוד מורכב בין חזון, כלכלה, קהילה ואינספור אילוצים. האם יש לכם את מה שצריך כדי לבנות עונה מנצחת? שחקו ותגלו!

<div class="theatre-repertoire-simulation">
    <h2>בניית הרפרטואר לעונה החדשה</h2>
    <p class="intro-text">כמנהל אמנותי, עליכם לבחור <span id="total-slots"></span> הצגות לעונה הקרובה, במסגרת תקציב כולל של <span id="total-budget"></span> ש"ח. איזו תמהיל תבחרו כדי לאזן בין הצלחה אמנותית, כלכלית וחברתית?</p>

    <div class="constraints-area">
        <h3><i class="icon-lock"></i> אילוצי העונה:</h3>
        <div class="constraints-display">
            <p>תקציב שנותר: <span id="remaining-budget" class="constraint-value"></span> ש"ח</p>
            <p>מקומות (סלוטים) שנותרו: <span id="remaining-slots" class="constraint-value"></span></p>
        </div>
    </div>

    <div class="potential-plays-area">
        <h3><i class="icon-list"></i> מחזות פוטנציאליים לבחירה:</h3>
        <div id="plays-list" class="plays-grid">
            <!-- Plays will be loaded here by JS -->
        </div>
    </div>

    <div class="selected-repertoire-area">
        <h3><i class="icon-check"></i> הרפרטואר שבחרת לעונה:</h3>
        <div id="selected-plays-list" class="selected-plays-container">
            <p class="placeholder">גררו לכאן מחזות מהרשימה או לחצו על כפתור "בחר".</p>
            <!-- Selected plays will appear here -->
        </div>
    </div>

    <div class="season-feedback-area">
        <h3><i class="icon-chart"></i> משוב על הרפרטואר שבניתם:</h3>
        <div id="feedback-results" class="feedback-container">
            <p>בחרו מחזות כדי לקבל משוב ולהבין את האיזונים.</p>
            <!-- Feedback will be displayed here by JS -->
        </div>
    </div>

     <div class="game-controls">
        <button id="reset-button" class="action-button">אפס בחירה</button>
        <!-- Future: Maybe a "Finalize Season" button? -->
     </div>
</div>

<button id="toggle-explanation" class="toggle-button"><i class="icon-info"></i> מה עומד מאחורי ההחלטות? הצג הסבר מעמיק</button>

<div id="explanation" class="hidden">
    <h2>אמנות ההחלטה: לבחור רפרטואר לתיאטרון - הסבר מעמיק</h2>
    <p>ניהול אמנותי בתיאטרון הוא תפקיד רב-ממדי הדורש שילוב של חזון אמנותי, הבנה עסקית ורגישות חברתית. המנהל האמנותי אינו רק אוצר התוכן, אלא גם המנוע האסטרטגי המכוון את דרכו של התיאטרון.</p>

    <h3>מורכבות בחירת רפרטואר</h3>
    <p>החלטה אילו הצגות יעלו על הבמה היא ליבת תפקיד המנהל האמנותי והיא מורכבת מאיזון עדין בין שיקולים שונים:</p>
    <ul>
        <li><strong>אמנותיים מול מסחריים:</strong> האם לבחור יצירות פורצות דרך אך קשות לקהל הרחב, או קומדיות קופתיות המבטיחות הכנסה?</li>
        <li><strong>פנים-ארגוניים מול חיצוניים:</strong> האם להשתמש בצוות שחקנים ויוצרים קיים, או להביא כישרונות חדשים? איך להתייחס ללחצים מצד תורמים, קהל או ביקורת?</li>
    </ul>

    <h3>קריטריונים מרכזיים להערכת מחזות ופרויקטים חדשים</h3>
    <p>כדי לקבל החלטה מושכלת, על המנהל האמנותי לשקול מגוון קריטריונים:</p>
    <ul>
        <li><strong>אמנותיים:</strong> איכות המחזה, רלוונטיות אמנותית, פוטנציאל בימוי ומשחק, מקוריות.</li>
        <li><strong>כלכליים:</strong> תקציב הפקה נדרש, פוטנציאל הכנסות, עלויות תפעול, יכולת גיוס משאבים.</li>
        <li><strong>חברתיים ותרבותיים:</strong> רלוונטיות חברתית, פוטנציאל השפעה על הקהילה, התאמה לקהל היעד, גיוון תרבותי.</li>
        <li><strong>הפקתיים:</strong> דרישות טכניות, זמינות שחקנים וצוות, לוחות זמנים, גודל במה מתאים.</li>
    </ul>

    <h3>אילוצים וטרייד-אופים בתהליך קבלת ההחלטות</h3>
    <p>במציאות, תמיד קיימים אילוצים המגבילים את האפשרויות. המנהל האמנותי חייב לפעול במסגרת מגבלות כמו:</p>
    <ul>
        <li>תקציב כולל לעונה.</li>
        <li>מספר מקומות (סלוטים) זמינים בלוח ההצגות.</li>
        <li>משאבי אנוש (זמינות שחקנים, צוות טכני).</li>
        <li>זמן הפקה.</li>
        <li>הצורך לאזן בין ז'אנרים שונים ופנייה לקהלים מגוונים.</li>
    </ul>
    <p>כל בחירה כרוכה בטרייד-אוף. בחירה בהצגה יקרה עשויה לבוא על חשבון מספר הצגות אחרות או להגביל את התקציב לשיווק. בחירה בהצגה ניסיונית עשויה להגדיל את היוקרה האמנותית אך להקטין את ההכנסות.</p>

    <h3>מודלים של קבלת החלטות בהקשר אמנותי</h3>
    <p>ניתן להסתכל על תהליך קבלת ההחלטות דרך מודלים שונים:</p>
    <ul>
        <li><strong>מודל רציונלי:</strong> איסוף כל המידע, הגדרת קריטריונים, שקילת כל האפשרויות ובחירה באופציה שממקסמת את התועלת הכוללת (קשה ליישום מלא באמנות).</li>
        <li><strong>רציונליות חסומה:</strong> הכרה בכך שהמידע מוגבל והזמן מוגבל, ובחירה באופציה "מספקת" (Satisficing) ולאו דווקא האופטימלית.</li>
        <li><strong>שיקול דעת אינטואיטיבי:</strong> הסתמכות על ניסיון, תחושות בטן ומומחיות, במיוחד כשהמידע חלקי והבעיה מורכבת.</li>
    </ul>
    <p>בניהול אמנותי, לרוב נעשה שימוש בשילוב של מודלים אלו, תוך דגש על אינטואיציה אמנותית מבוססת ניסיון.</p>

    <h3>תפקידם של חזון ואסטרטגיה בבניית רפרטואר</h3>
    <p>רפרטואר מוצלח הוא יותר מסך חלקיו. הוא צריך לשקף חזון אמנותי ברור ואסטרטגיה ארוכת טווח לתיאטרון. האם התיאטרון שואף להיות בית ליצירה מקורית? לשמר קלאסיקות? לפנות לקהלים חדשים? להשפיע חברתית? החזון מכוון את הבחירות ומבטיח עקביות לאורך זמן.</p>

    <h3>הגדרת הצלחה בתיאטרון</h3>
    <p>הצלחה בתיאטרון אינה נמדדת אך ורק ברווח כספי. מדדים נוספים וחשובים כוללים:</p>
    <ul>
        <li>השפעה תרבותית וחברתית.</li>
        <li>שביעות רצון אמנים וצוות התיאטרון.</li>
        <li>בניית קשר עמוק עם הקהילה.</li>
        <li>ביקורות ויוקרה אמנותית.</li>
        <li>פיתוח כישרונות חדשים.</li>
    </ul>
    <p>בניית רפרטואר היא, אם כן, מלאכת מחשבת הדורשת איזון מתמיד בין דרישות שונות, יצירתיות, ואומץ אמנותי.</p>
</div>

<script>
    const totalBudget = 500000;
    const totalSlots = 3;

    let remainingBudget = totalBudget;
    let remainingSlots = totalSlots;
    let selectedPlays = []; // Stores play objects

    const playsData = [
        { id: 'play1', title: 'בית הבובות', genre: 'דרמה קלאסית', budget: 100000, audience: 'נישה / משכיל', criticalPotential: 'גבוה', commercialPotential: 'נמוך', socialRelevance: 'בינוני', actors: 4 },
        { id: 'play2', title: 'צחוק בחדר המדרגות', genre: 'קומדיה עכשווית', budget: 150000, audience: 'רחב', criticalPotential: 'בינוני', commercialPotential: 'גבוה', socialRelevance: 'נמוך', actors: 6 },
        { id: 'play3', title: 'הסופה', genre: 'שייקספיר / פנטזיה', budget: 180000, audience: 'מעורב', criticalPotential: 'גבוה', commercialPotential: 'בינוני', socialRelevance: 'בינוני', actors: 10 },
        { id: 'play4', title: 'מונולוגים מהוואגינה', genre: 'דרמה חברתית', budget: 70000, audience: 'ספציפי (נשים)', criticalPotential: 'בינוני', commercialPotential: 'בינוני', socialRelevance: 'גבוה', actors: 3 },
        { id: 'play5', title: 'פסטיבל המחזות הקצרים', genre: 'ניסיוני / מגוון', budget: 90000, audience: 'נישה / אמנים', criticalPotential: 'גבוה', commercialPotential: 'נמוך', socialRelevance: 'בינוני', actors: 15 }, // Many actors, small roles
        { id: 'play6', title: 'פיטר פן', genre: 'מחזמר לילדים', budget: 250000, audience: 'משפחות', criticalPotential: 'בינוני', commercialPotential: 'גבוה מאוד', socialRelevance: 'נמוך', actors: 20 }
    ];

    const dom = {
        totalBudget: document.getElementById('total-budget'),
        totalSlots: document.getElementById('total-slots'),
        remainingBudget: document.getElementById('remaining-budget'),
        remainingSlots: document.getElementById('remaining-slots'),
        playsList: document.getElementById('plays-list'),
        selectedPlaysList: document.getElementById('selected-plays-list'),
        feedbackResults: document.getElementById('feedback-results'),
        explanation: document.getElementById('explanation'),
        toggleExplanationButton: document.getElementById('toggle-explanation'),
        resetButton: document.getElementById('reset-button')
    };

    // Helper function to get play data by ID
    const getPlayById = (id) => playsData.find(p => p.id === id);

    function renderPlays() {
        dom.playsList.innerHTML = playsData.map(play => `
            <div class="play-item" id="${play.id}" data-play-id="${play.id}">
                <h4>${play.title}</h4>
                <p><strong><i class="icon-tag"></i> ז'אנר:</strong> ${play.genre}</p>
                <p><strong><i class="icon-money"></i> תקציב:</strong> ${play.budget.toLocaleString()} ש"ח</p>
                <p><strong><i class="icon-users"></i> קהל יעד:</strong> ${play.audience}</p>
                <p><strong><i class="icon-star"></i> פוטנציאל ביקורתי:</strong> ${play.criticalPotential}</p>
                <p><strong><i class="icon-chart-line"></i> פוטנציאל מסחרי:</strong> ${play.commercialPotential}</p>
                <p><strong><i class="icon-globe"></i> רלוונטיות חברתית:</strong> ${play.socialRelevance}</p>
                <p><strong><i class="icon-actors"></i> שחקנים:</strong> ${play.actors}</p>
                <button class="select-play-button" data-play-id="${play.id}">בחר</button>
            </div>
        `).join('');

        attachEventListeners();
        updateConstraintsDisplay(); // Initial display
        updateFeedback(); // Initial feedback prompt
        updatePlayButtons(); // Set initial state of buttons
    }

    function attachEventListeners() {
        // Use event delegation on the plays list for selection/removal
        dom.playsList.addEventListener('click', handlePlayAction);

        // Event listener for remove buttons in selected list (delegation)
        dom.selectedPlaysList.addEventListener('click', handleSelectedPlayRemoval);

        // Toggle Explanation Button
        dom.toggleExplanationButton.addEventListener('click', toggleExplanation);

        // Reset Button
        dom.resetButton.addEventListener('click', resetSimulation);
    }

     function handlePlayAction(event) {
        const button = event.target.closest('.select-play-button');
        if (!button) return; // Not a button click

        const playId = button.dataset.playId;
        const play = getPlayById(playId);

        if (!play) return;

        const isSelected = selectedPlays.some(p => p.id === playId);

        if (isSelected) {
            // If already selected, this button should act as 'Remove'
            handlePlayRemoval(playId);
        } else {
            // If not selected, this button should act as 'Select'
            handlePlaySelection(play);
        }
    }

    function handlePlaySelection(play) {
        if (remainingBudget >= play.budget && remainingSlots > 0) {
            selectedPlays.push(play);
            remainingBudget -= play.budget;
            remainingSlots -= 1;
            updateUI();
            animatePlaySelection(play.id);
        } else {
             // Add visual feedback for failed selection
             const playItem = dom.playsList.querySelector(`.play-item[data-play-id="${play.id}"]`);
             if (playItem) {
                 playItem.classList.add('cannot-select');
                 setTimeout(() => {
                     playItem.classList.remove('cannot-select');
                 }, 800); // Remove highlight after animation
             }
            alert('אין מספיק תקציב או מקום ברפרטואר לעונה עבור מחזה זה.'); // Consider a more subtle message later
        }
    }

     function handleSelectedPlayRemoval(event) {
         const removeButton = event.target.closest('.remove-play-button');
         if (!removeButton) return; // Not a remove button click

         const playId = removeButton.dataset.playId;
         handlePlayRemoval(playId);
     }

    function handlePlayRemoval(playId) {
        const playIndex = selectedPlays.findIndex(p => p.id === playId);

        if (playIndex > -1) {
            const play = selectedPlays[playIndex];
            selectedPlays.splice(playIndex, 1);
            remainingBudget += play.budget;
            remainingSlots += 1;
            updateUI();
             animatePlayRemoval(playId);
        }
    }

    function resetSimulation() {
        selectedPlays = [];
        remainingBudget = totalBudget;
        remainingSlots = totalSlots;
        updateUI();
         // Remove selected state from all play items
        dom.playsList.querySelectorAll('.play-item').forEach(item => item.classList.remove('selected'));
         // Clear animations related classes if any
         dom.playsList.querySelectorAll('.play-item').forEach(item => item.classList.remove('selected-animation'));
         dom.selectedPlaysList.innerHTML = '<p class="placeholder">גררו לכאן מחזות מהרשימה או לחצו על כפתור "בחר".</p>'; // Restore placeholder
    }

    function updateUI() {
        updateConstraintsDisplay();
        renderSelectedPlays();
        updateFeedback();
        updatePlayButtons();
    }

    function updateConstraintsDisplay() {
        dom.totalBudget.textContent = totalBudget.toLocaleString();
        dom.totalSlots.textContent = totalSlots;
        dom.remainingBudget.textContent = remainingBudget.toLocaleString();
        dom.remainingSlots.textContent = remainingSlots;

        // Visual feedback for constraints
        dom.remainingBudget.classList.remove('low', 'critical');
        if (remainingBudget < totalBudget * 0.2) dom.remainingBudget.classList.add('critical');
        else if (remainingBudget < totalBudget * 0.5) dom.remainingBudget.classList.add('low');

        dom.remainingSlots.classList.remove('low', 'critical');
        if (remainingSlots === 0) dom.remainingSlots.classList.add('critical');
        else if (remainingSlots === 1) dom.remainingSlots.classList.add('low');
    }

    function renderSelectedPlays() {
        const selectedPlaysHtml = selectedPlays.map(play => `
            <div class="selected-play-item" id="selected-${play.id}" data-play-id="${play.id}">
                 ${play.title} <button class="remove-play-button" data-play-id="${play.id}"><i class="icon-close"></i></button>
            </div>
        `).join('');

        if (selectedPlays.length === 0) {
            dom.selectedPlaysList.innerHTML = '<p class="placeholder">גררו לכאן מחזות מהרשימה או לחצו על כפתור "בחר".</p>';
        } else {
            dom.selectedPlaysList.innerHTML = selectedPlaysHtml;
        }
         // Event listeners for remove buttons are handled by delegation on selectedPlaysList
    }

    function updatePlayButtons() {
        dom.playsList.querySelectorAll('.play-item').forEach(playItem => {
            const playId = playItem.dataset.playId;
            const selectButton = playItem.querySelector('.select-play-button');
            const play = getPlayById(playId);

            const isAlreadySelected = selectedPlays.some(p => p.id === playId);

            playItem.classList.toggle('selected', isAlreadySelected); // Add/remove 'selected' class

            if (isAlreadySelected) {
                selectButton.textContent = 'נבחר (הסר)';
                selectButton.classList.add('selected-button');
                selectButton.classList.remove('disabled');
                selectButton.disabled = false;
            } else {
                selectButton.textContent = 'בחר';
                selectButton.classList.remove('selected-button');

                const canSelect = remainingBudget >= play.budget && remainingSlots > 0;
                selectButton.classList.toggle('disabled', !canSelect);
                selectButton.disabled = !canSelect;

                // Add visual cue for plays that cannot be selected
                playItem.classList.toggle('unselectable', !canSelect && !isAlreadySelected);
            }
        });
    }


    function updateFeedback() {
        if (selectedPlays.length === 0) {
            dom.feedbackResults.innerHTML = '<p>בחרו מחזות כדי לקבל משוב ולהבין את האיזונים.</p>';
            return;
        }

        let totalBudgetUsed = totalBudget - remainingBudget;
        let genres = selectedPlays.map(p => p.genre);
        let audienceMix = selectedPlays.map(p => p.audience);
        let criticalSum = selectedPlays.reduce((sum, p) => sum + (p.criticalPotential === 'גבוה' ? 3 : p.criticalPotential === 'בינוני' ? 2 : 1), 0);
        let commercialSum = selectedPlays.reduce((sum, p) => sum + (p.commercialPotential === 'גבוה מאוד' ? 4 : p.commercialPotential === 'גבוה' ? 3 : p.commercialPotential === 'בינוני' ? 2 : 1), 0);
        let socialRelevanceSum = selectedPlays.reduce((sum, p) => sum + (p.socialRelevance === 'גבוה' ? 3 : p.socialRelevance === 'בינוני' ? 2 : 1), 0);

        // Simple diversity metrics
        let uniqueGenres = new Set(genres).size;
        let uniqueAudiences = new Set(audienceMix).size;

        // Calculate average scores
        let avgCritical = criticalSum / selectedPlays.length;
        let avgCommercial = commercialSum / selectedPlays.length;
        let avgSocial = socialRelevanceSum / selectedPlays.length;

        // Simple qualitative feedback based on scores and mix
        let criticalFeedback = avgCritical > 2.5 ? 'גבוהה מאוד' : avgCritical > 1.8 ? 'גבוהה' : 'בינונית';
        let commercialFeedback = avgCommercial > 3 ? 'גבוהה מאוד' : avgCommercial > 2.5 ? 'גבוהה' : avgCommercial > 1.5 ? 'בינונית' : 'נמוכה';
        let socialFeedback = avgSocial > 2.5 ? 'גבוהה' : avgSocial > 1.8 ? 'בינונית' : 'נמוכה';

        let diversityFeedback = '';
        if (uniqueGenres >= Math.min(3, selectedPlays.length) && uniqueAudiences >= Math.min(3, selectedPlays.length)) diversityFeedback = '<span class="feedback-good">גבוהה מאוד (מגוון רחב של ז\'אנרים וקהלים)</span>';
        else if (uniqueGenres >= Math.min(2, selectedPlays.length) && uniqueAudiences >= Math.min(2, selectedPlays.length)) diversityFeedback = '<span class="feedback-ok">גבוהה (כיסוי סביר של ז\'אנרים וקהלים)</span>';
        else diversityFeedback = '<span class="feedback-warn">בינונית (מונו-ז\'אנר או פונה לקהל מצומצם)</span>';


        let budgetUsagePercentage = (totalBudgetUsed / totalBudget) * 100;
        let budgetUsageFeedback = budgetUsagePercentage > 95 ? '<span class="feedback-good">גבוהה מאוד (כמעט ניצול מלא של התקציב)</span>' :
                                   budgetUsagePercentage > 80 ? '<span class="feedback-ok">גבוהה (ניצול יעיל של התקציב)</span>' :
                                   '<span class="feedback-warn">בינונית (נשאר תקציב משמעותי)</span>';

        let slotsUsageFeedback = `${selectedPlays.length} מתוך ${totalSlots}`;
        if (selectedPlays.length === totalSlots) slotsUsageFeedback = `<span class="feedback-good">${slotsUsageFeedback} (העונה מלאה!)</span>`;


         // Qualify critical/commercial/social feedback with colors
         const getScoreColorClass = (score) => score > 2.5 ? 'feedback-good' : score > 1.5 ? 'feedback-ok' : 'feedback-warn';

        let feedbackHTML = `
            <h4><i class="icon-summary"></i> סיכום ביצועים:</h4>
            <p><strong>ניצול תקציב:</strong> ${budgetUsageFeedback} (${totalBudgetUsed.toLocaleString()} ש"ח מתוך ${totalBudget.toLocaleString()})</p>
            <p><strong>ניצול מקומות:</strong> ${slotsUsageFeedback}</p>
            <p><strong>פוטנציאל ביקורתי כולל:</strong> <span class="${getScoreColorClass(avgCritical)}">${criticalFeedback}</span></p>
            <p><strong>פוטנציאל מסחרי כולל (הכנסות צפויות):</strong> <span class="${getScoreColorClass(avgCommercial)}">${commercialFeedback}</span></p>
             <p><strong>פוטנציאל רלוונטיות חברתית:</strong> <span class="${getScoreColorClass(avgSocial)}">${socialFeedback}</span></p>
            <p><strong>גיוון אמנותי וקהלים:</strong> ${diversityFeedback}</p>
            <h4><i class="icon-insights"></i> ניתוח נוסף:</h4>
            <ul>
                ${genres.length > 0 ? `<li>ז'אנרים ברפרטואר: ${genres.join(', ')}</li>` : ''}
                ${audienceMix.length > 0 ? `<li>קהלי יעד עיקריים: ${audienceMix.join(', ')}</li>` : ''}
            </ul>
            <p>זכרו - בניית רפרטואר היא תהליך מורכב ומלא פשרות. עליכם לאזן בחכמה בין חזון אמנותי, ריאליה כלכלית והשפעה חברתית כדי ליצור עונה מוצלחת בכל המובנים.</p>
        `;

        dom.feedbackResults.innerHTML = feedbackHTML;
    }

     // --- Animation Logic ---
     function animatePlaySelection(playId) {
        const playItem = dom.playsList.querySelector(`.play-item[data-play-id="${playId}"]`);
        if (playItem) {
             playItem.classList.add('selected-animation');
             // The selected item is rendered in the selected list by renderSelectedPlays
             // No need to move the element itself for this approach.
             // Animation can be CSS based on the 'selected-animation' class.
             playItem.addEventListener('animationend', () => {
                 playItem.classList.remove('selected-animation');
                 // Visually mark it as selected permanently via the 'selected' class handled in updatePlayButtons
             }, { once: true });
        }
     }

    function animatePlayRemoval(playId) {
        // The item is removed from the selected list by renderSelectedPlays
        // We need to visually animate the item as it *returns* or is deselected from the original list
         const playItem = dom.playsList.querySelector(`.play-item[data-play-id="${playId}"]`);
         if (playItem) {
             playItem.classList.add('deselected-animation');
              playItem.addEventListener('animationend', () => {
                 playItem.classList.remove('deselected-animation');
                 // The 'selected' class is removed by updatePlayButtons
              }, { once: true });
         }
     }


    function toggleExplanation() {
        const isHidden = dom.explanation.classList.contains('hidden');
        if (isHidden) {
             dom.explanation.style.maxHeight = dom.explanation.scrollHeight + 'px'; // Animate height
             dom.explanation.classList.remove('hidden');
            dom.toggleExplanationButton.innerHTML = '<i class="icon-close"></i> הסתר הסבר';
        } else {
            dom.explanation.style.maxHeight = '0'; // Animate height close
             dom.explanation.addEventListener('transitionend', () => {
                 dom.explanation.classList.add('hidden');
                 dom.explanation.style.maxHeight = null; // Reset max-height after animation
            }, { once: true });

            dom.toggleExplanationButton.innerHTML = '<i class="icon-info"></i> מה עומד מאחורי ההחלטות? הצג הסבר מעמיק';
        }
    }

    // Initial setup
    document.addEventListener('DOMContentLoaded', () => {
         // Injecting simple icons (optional, could use a library)
         const styleSheet = document.createElement("style");
         styleSheet.type = "text/css";
         styleSheet.innerText = `
            .icon-lock::before { content: '🔒 '; }
            .icon-list::before { content: '🎭 '; }
            .icon-check::before { content: '✅ '; }
            .icon-chart::before { content: '📊 '; }
            .icon-info::before { content: '💡 '; }
            .icon-close::before { content: '❌'; font-weight: bold;}
            .icon-tag::before { content: '🏷️ '; }
            .icon-money::before { content: '💰 '; }
            .icon-users::before { content: '👥 '; }
            .icon-star::before { content: '⭐ '; }
            .icon-chart-line::before { content: '📈 '; }
            .icon-globe::before { content: '🌍 '; }
            .icon-actors::before { content: 'ctors '; } /* Placeholder for actors icon */
            .icon-summary::before { content: '📋 '; }
            .icon-insights::before { content: '🧠 '; }
         `;
         document.head.appendChild(styleSheet);

        renderPlays();
         // Event listeners attached in renderPlays after DOM elements exist
    });

     // Simple Drag and Drop (Optional refinement for "game-like")
     // This adds complexity and might not be strictly needed based on the prompt's focus on interaction buttons.
     // Let's stick to button clicks for selection/removal as it's explicitly mentioned.

</script>

<style>
    /* General body styling */
    body {
        font-family: 'Arial', sans-serif; /* Fallback */
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: #333;
        background-color: #eef2f7; /* Light background */
        margin: 0;
        padding: 20px;
    }

    /* Main Simulation Container */
    .theatre-repertoire-simulation {
        max-width: 900px;
        margin: 20px auto;
        padding: 30px;
        background-color: #ffffff; /* White background for content */
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        border: 1px solid #d0d0d0;
        display: grid;
        gap: 25px; /* Space between main sections */
    }

    .theatre-repertoire-simulation h2 {
        color: #5a2d82; /* Theatre-like purple */
        text-align: center;
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 2em;
         line-height: 1.2;
    }

     .intro-text {
         text-align: center;
         margin-bottom: 30px;
         font-size: 1.1em;
         color: #555;
     }


    .theatre-repertoire-simulation h3 {
        color: #3a1e52; /* Darker purple */
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 8px;
        margin-bottom: 20px;
        font-size: 1.4em;
    }

    .theatre-repertoire-simulation h4 {
         color: #6b4c8e; /* Medium purple */
         margin-top: 0;
         margin-bottom: 10px;
         font-size: 1.1em;
    }


    /* Section Styling */
    .constraints-area, .potential-plays-area, .selected-repertoire-area, .season-feedback-area {
        background-color: #f8f8f8;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #eee;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

    .constraints-area {
        background-color: #e8f0f8; /* Light blue for constraints */
        border-color: #cce0f0;
    }

    .constraints-display {
         display: flex;
         justify-content: space-around;
         gap: 20px;
         font-size: 1.1em;
         font-weight: bold;
         color: #333;
    }

     .constraints-display p {
         margin: 0;
     }

     .constraint-value {
         color: #28a745; /* Green for ample */
     }

     .constraint-value.low {
         color: #ffc107; /* Yellow for low */
     }

      .constraint-value.critical {
         color: #dc3545; /* Red for critical/zero */
     }


    /* Plays Grid */
    .plays-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
    }

    .play-item {
        border: 1px solid #dcdcdc;
        border-radius: 8px;
        padding: 20px;
        background-color: #ffffff;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        position: relative; /* Needed for animations */
        overflow: hidden;
    }

    .play-item:hover:not(.selected):not(.unselectable) {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        border-color: #a0a0a0;
    }

     .play-item.unselectable {
         opacity: 0.6;
         cursor: not-allowed;
         background-color: #f0f0f0;
         border-color: #ccc;
     }
      .play-item.unselectable:hover {
         transform: none;
         box-shadow: none;
      }


     .play-item strong {
         color: #444;
     }

     .play-item p {
         margin: 5px 0;
         font-size: 0.95em;
         color: #555;
     }


    /* Buttons */
    button {
        font-family: inherit;
        cursor: pointer;
        transition: background-color 0.2s ease, opacity 0.2s ease;
    }

    .select-play-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #5a2d82; /* Purple */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1em;
        margin-top: 15px;
        font-weight: bold;
    }

    .select-play-button:hover:not(:disabled):not(.selected-button) {
        background-color: #3a1e52; /* Darker purple */
    }

    .select-play-button.disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.8;
    }

    .select-play-button.selected-button {
        background-color: #28a745; /* Green */
    }
    .select-play-button.selected-button:hover:not(:disabled) {
        background-color: #218838; /* Darker green */
    }

     .action-button {
         display: block;
         width: 180px;
         margin: 20px auto 0 auto;
         padding: 10px 20px;
         background-color: #6c757d; /* Gray */
         color: white;
         border: none;
         border-radius: 6px;
         font-size: 1em;
         text-align: center;
         font-weight: bold;
     }
     .action-button:hover {
         background-color: #5a6268;
     }

    /* Selected Plays Display */
    .selected-plays-container {
        min-height: 60px;
        border: 2px dashed #a0a0a0;
        padding: 15px;
        border-radius: 8px;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: center;
        background-color: #f0f0f0;
        transition: background-color 0.3s ease;
    }

     .selected-plays-container .placeholder {
         text-align: center;
         color: #888;
         width: 100%;
         font-style: italic;
     }

    .selected-play-item {
         background-color: #d4edda; /* Light green */
         color: #155724; /* Dark green */
         padding: 8px 15px;
         border-radius: 20px;
         font-size: 0.95em;
         display: flex;
         align-items: center;
         font-weight: bold;
         border: 1px solid #c3e6cb;
         transition: transform 0.2s ease, opacity 0.2s ease;
    }

    .selected-play-item .remove-play-button {
        background-color: #dc3545; /* Red */
        color: white;
        border: none;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        font-size: 0.9em;
        line-height: 24px;
        padding: 0;
        margin-right: 8px; /* Space between text and button */
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: background-color 0.2s ease;
    }
     .selected-play-item .remove-play-button:hover {
        background-color: #c82333;
     }
     .selected-play-item .remove-play-button i {
         /* Style for the close icon */
         font-style: normal; /* Ensure icon doesn't look italic */
     }


    /* Feedback Section */
     .feedback-container {
         background-color: #e9ecef; /* Light gray-blue */
         padding: 20px;
         border-radius: 8px;
         border: 1px solid #dee2e6;
     }

     .feedback-container h4 {
         color: #0056b3;
         margin-bottom: 15px;
         padding-bottom: 5px;
         border-bottom: 1px dashed #ccc;
     }

     .feedback-container p {
         margin: 10px 0;
         line-height: 1.5;
         color: #444;
     }

     .feedback-container ul {
         margin-top: 15px;
         padding-right: 20px;
         color: #444;
     }

     .feedback-container li {
         margin-bottom: 8px;
         font-size: 0.95em;
     }

     /* Feedback Text Colors */
     .feedback-good {
         color: #28a745; /* Green */
         font-weight: bold;
     }
      .feedback-ok {
         color: #ffc107; /* Yellow */
         font-weight: bold;
     }
      .feedback-warn {
         color: #dc3545; /* Red */
         font-weight: bold;
     }


    /* Toggle Explanation Button */
    .toggle-button {
        display: block;
        width: auto; /* Auto width based on content */
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #007bff; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        text-align: center;
        font-weight: bold;
         transition: background-color 0.3s ease, box-shadow 0.3s ease;
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .toggle-button:hover {
        background-color: #0056b3;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

     .toggle-button i {
         margin-left: 8px; /* Space between text and icon */
     }


    /* Explanation Section */
    #explanation {
        background-color: #ffffff;
        padding: 30px;
        margin-top: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        direction: rtl;
        text-align: right;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        overflow: hidden; /* Hide content when height is 0 */
        transition: max-height 0.5s ease-in-out, opacity 0.5s ease; /* Smooth transition */
        max-height: 0; /* Initially hidden */
        opacity: 0;
    }

    #explanation.hidden {
        max-height: 0 !important; /* Ensure it's hidden even if max-height is calculated */
        opacity: 0;
         padding-top: 0; /* Collapse padding */
         padding-bottom: 0;
    }
     #explanation:not(.hidden) {
         opacity: 1;
     }


    #explanation h2, #explanation h3 {
        color: #5a2d82; /* Theatre purple */
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-bottom: 15px;
        text-align: right;
    }

    #explanation p {
        margin-bottom: 15px;
        line-height: 1.7;
        color: #555;
        text-align: right;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 25px;
        color: #555;
    }

    #explanation li {
        margin-bottom: 10px;
        line-height: 1.5;
    }

     /* Animations */
     @keyframes selectFadeIn {
         from { opacity: 0; transform: translateY(10px); }
         to { opacity: 1; transform: translateY(0); }
     }

     @keyframes selectPulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.02); }
         100% { transform: scale(1); }
     }

      @keyframes cannotSelectShake {
          0%, 100% { transform: translateX(0); }
          20%, 60% { transform: translateX(-5px); }
          40%, 80% { transform: translateX(5px); }
      }

     .play-item.selected-animation {
         animation: selectPulse 0.6s ease;
     }

     .play-item.cannot-select {
         animation: cannotSelectShake 0.5s ease;
         border-color: #dc3545;
     }


     /* Basic responsive adjustment */
    @media (max-width: 768px) {
        .theatre-repertoire-simulation {
            padding: 20px;
            gap: 20px;
        }

        .plays-grid {
            grid-template-columns: 1fr;
        }

        .constraints-display {
            flex-direction: column;
            gap: 10px;
            text-align: center;
        }
    }

     /* Simple icon styling (basic - replace with a real library if needed) */
     [class^="icon-"]::before, [class*=" icon-"]::before {
        display: inline-block;
        margin-left: 5px; /* Space after icon */
        /* Add any other icon styling like font-family etc if using a library */
     }


</style>