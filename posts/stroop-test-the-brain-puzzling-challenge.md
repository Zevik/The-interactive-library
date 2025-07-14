---
title: "אפקט סטרופ: האתגר שמבלבל את המוח"
english_slug: stroop-test-the-brain-puzzling-challenge
category: "מדעי החברה / פסיכולוגיה"
tags: [פסיכולוגיה קוגניטיבית, אפקט סטרופ, זמן תגובה, קשב סלקטיבי, תפקודים ניהוליים]
---
# אפקט סטרופ: האתגר שמבלבל את המוח

האם ידעתם שקריאה היא פעולה אוטומטית כל כך, שהיא יכולה להפריע לכם אפילו במשימה פשוטה כמו זיהוי צבע? צללו לתוך אפקט סטרופ וגלו איך תחרות בין תהליכים שונים במוח חושפת את המאמץ הנדרש לקשב וריכוז, ואת הקושי להתעלם מהרגל חזק. מוכנים לאתגר?

<div id="stroop-app">
    <div id="game-container">
        <div id="word-display" class="word-transition"></div>
        <p id="instruction-text"></p>
        <p id="trial-counter"></p>
    </div>
    <div id="color-buttons">
        <button class="color-button" data-color="red">אדום</button>
        <button class="color-button" data-color="blue">כחול</button>
        <button class="color-button" data-color="green">ירוק</button>
        <button class="color-button" data-color="yellow">צהוב</button>
    </div>
    <div id="start-screen">
        <button id="start-button">התחל אתגר סטרופ</button>
    </div>
    <div id="results-screen">
        <h2>התוצאות שלכם:</h2>
        <p>ניסיונות שהושלמו: <span id="total-trials-count">0</span></p>
        <p>טעויות: <span id="error-count">0</span></p>
        <h3>זמן תגובה ממוצע (באלפיות השנייה):</h3>
        <p>תואם (מילה וצבע זהים): <span id="avg-rt-congruent">0</span> מ"ש</p>
        <p>לא תואם (מילה וצבע שונים): <span id="avg-rt-incongruent">0</span> מ"ש</p>
        <p id="results-summary"></p>
         <button id="restart-button">נסו שוב</button>
    </div>
</div>

<style>
/* משתני CSS לצבעים וטיפוגרפיה */
:root {
    --primary-blue: #007bff;
    --primary-darkblue: #0056b3;
    --success-green: #28a745;
    --danger-red: #dc3545;
    --warning-yellow: #ffc107; /* Using a lighter yellow for button, but word color will be #f0ad4e */
    --info-teal: #17a2b8;
    --background-light: #f8f9fa;
    --text-dark: #343a40;
    --text-muted: #6c757d;
    --card-background: #ffffff;
    --card-shadow: 0 4px 8px rgba(0,0,0,0.08);
    --border-light: #dee2e6;
}

#stroop-app {
    direction: rtl;
    font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 30px;
    background: linear-gradient(135deg, var(--background-light), #e9ecef); /* Subtle gradient background */
    border-radius: 12px;
    box-shadow: var(--card-shadow);
    max-width: 600px;
    margin: 30px auto;
    overflow: hidden; /* Clean corners */
    color: var(--text-dark);
}

#game-container {
    text-align: center;
    margin-bottom: 30px;
    min-height: 180px; /* Ensure space */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
}

#word-display {
    font-size: 5em; /* Slightly larger */
    font-weight: 900; /* Bolder */
    height: 1.5em; /* Fixed height */
    line-height: 1.5em; /* Center vertically */
    margin-bottom: 15px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1); /* Subtle text shadow */
    opacity: 0; /* Start invisible for fade-in */
    transform: scale(0.9); /* Start slightly smaller */
}

.word-transition {
    transition: opacity 0.4s ease-out, transform 0.4s ease-out;
}

.word-visible {
     opacity: 1;
     transform: scale(1);
}

.word-correct {
    animation: flash-green 0.5s ease-in-out;
}

.word-incorrect {
    animation: flash-red 0.5s ease-in-out;
}

@keyframes flash-green {
    0%, 100% { color: inherit; }
    50% { color: var(--success-green); }
}

@keyframes flash-red {
    0%, 100% { color: inherit; }
    50% { color: var(--danger-red); }
}


#instruction-text {
    font-size: 1.3em; /* Larger instruction */
    color: var(--text-muted);
    margin-bottom: 15px;
    height: 1.5em; /* Reserve space */
}

#trial-counter {
    font-size: 1em;
    color: var(--text-muted);
    margin-top: 0;
    height: 1.5em; /* Reserve space */
}


#color-buttons {
    display: flex;
    justify-content: center;
    gap: 15px; /* Increased gap */
    margin-bottom: 30px;
    flex-wrap: wrap; /* Allow wrapping on small screens */
    width: 100%;
}

.color-button {
    padding: 18px 30px; /* Larger buttons */
    font-size: 1.2em;
    font-weight: bold;
    cursor: pointer;
    border: none;
    border-radius: 8px; /* More rounded corners */
    color: var(--card-background); /* White text */
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    min-width: 100px; /* Ensure minimum width */
}

.color-button[data-color="red"] { background-color: var(--danger-red); }
.color-button[data-color="blue"] { background-color: var(--primary-blue); }
.color-button[data-color="green"] { background-color: var(--success-green); }
.color-button[data-color="yellow"] { background-color: var(--warning-yellow); color: var(--text-dark); } /* Yellow button needs dark text */

.color-button:hover {
    opacity: 0.9;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.color-button:active {
    transform: scale(0.98); /* Press effect */
    box-shadow: 0 1px 2px rgba(0,0,0,0.2);
}

#start-screen, #results-screen {
    width: 100%;
    text-align: center;
    padding: 20px;
    background-color: var(--card-background);
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

#start-button, #restart-button {
     padding: 15px 30px;
    font-size: 1.3em;
    cursor: pointer;
    border: none;
    border-radius: 8px;
    background-color: var(--info-teal); /* Info color for actions */
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

#start-button:hover, #restart-button:hover {
    background-color: #138496; /* Darker teal */
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

#start-button:active, #restart-button:active {
     transform: scale(0.98);
}

#results-screen h2 {
    margin-top: 0;
    color: var(--primary-blue);
    margin-bottom: 20px;
}

#results-screen p {
    font-size: 1.1em;
    margin-bottom: 10px;
    color: var(--text-dark);
}

#results-screen h3 {
     margin-top: 20px;
     margin-bottom: 10px;
     color: var(--text-muted);
     border-top: 1px solid var(--border-light);
     padding-top: 15px;
}

#results-summary {
    font-size: 1.2em;
    font-weight: bold;
    margin-top: 20px;
    color: var(--primary-blue);
}

#toggle-explanation {
    display: block;
    margin: 30px auto;
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    border: none;
    border-radius: 8px;
    background-color: var(--border-light); /* Light gray for toggle */
    color: var(--text-dark);
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

#toggle-explanation:hover {
    background-color: #ced4da; /* Darker gray */
}

#toggle-explanation:active {
    transform: scale(0.98);
}


#explanation {
    direction: rtl;
    margin-top: 30px;
    padding: 25px;
    background-color: var(--card-background);
    border-radius: 12px;
    box-shadow: var(--card-shadow);
    line-height: 1.7;
    color: var(--text-dark);
}

#explanation h2 {
    color: var(--primary-blue);
    margin-bottom: 20px;
    border-bottom: 1px solid var(--border-light);
    padding-bottom: 10px;
}

#explanation h3 {
    color: var(--text-muted);
    margin-top: 25px;
    margin-bottom: 15px;
    font-size: 1.3em;
}

#explanation p, #explanation ul {
    font-size: 1.1em;
    color: var(--text-dark);
    margin-bottom: 15px;
}

#explanation ul {
    padding-right: 25px;
}

#explanation li {
    margin-bottom: 10px;
    line-height: 1.6;
}

/* Utility class for hiding elements */
.hidden {
    display: none;
}

/* State classes handled by JS */
#start-screen.active,
#game-container.active,
#color-buttons.active,
#results-screen.active {
    display: flex; /* Use flex to maintain layout */
    flex-direction: column;
    align-items: center;
    width: 100%;
}

/* Specific overrides for elements within active states */
#game-container.active #word-display {
     display: block; /* Word display is block within game container */
}
#game-container.active #instruction-text {
    display: block;
}
#game-container.active #trial-counter {
    display: block;
}

#color-buttons.active {
     display: flex; /* Buttons flex row */
}

#start-screen, #game-container, #results-screen, #color-buttons {
    display: none; /* Hide all by default */
}

</style>

<button id="toggle-explanation">הצג/הסתר הסבר על אפקט סטרופ</button>

<div id="explanation" class="hidden">
    <h2>אפקט סטרופ: כשהמוח חושב מהר מהמילים</h2>

    <h3>מהו אפקט סטרופ וכיצד הוא עובד?</h3>
    אפקט סטרופ הוא תופעה פסיכולוגית מרתקת שמדגימה את הקושי של המוח שלנו להתעלם ממידע אוטומטי (כמו קריאה) כשהוא מנסה להתמקד במידע אחר (כמו זיהוי צבע). בניסוי סטרופ הקלאסי, נדרשים המשתתפים לזהות את צבע הדיו שבו כתובה מילה, ולא לקרוא את המילה עצמה. כשיש קונפליקט – למשל, המילה "אדום" כתובה בצבע כחול – המוח "מתבלבל", ותהליך זיהוי הצבע מתעכב וגורם לזמן תגובה ארוך יותר ולעיתים גם ליותר טעויות.

    <h3>מדוע המוח "מתנגש" עם המילים? התיאוריות המובילות</h3>
    <p>אפקט סטרופ מוסבר על ידי מספר תיאוריות מרכזיות בפסיכולוגיה קוגניטיבית:</p>
    <ul>
        <li>**אוטומטיות מול בקרה:** קריאה אצל אנשים בוגרים היא תהליך אוטומטי מאוד ומהיר. זיהוי צבע, לעומת זאת, דורש יותר מאמץ קשבי ובקרה מודעת. כשיש קונפליקט, הקריאה האוטומטית מפריעה לבקרה הנדרשת לזיהוי הצבע הנכון.</li>
        <li>**מהירות עיבוד:** המוח מעבד את משמעות המילה מהר יותר משהוא מעבד את צבע הדיו. המידע המילולי המעובד ראשון יוצר "רעש" או הפרעה לתגובה המבוססת על צבע.</li>
        <li>**קשב סלקטיבי ועכבה:** המשימה דורשת קשב סלקטיבי למימד הצבע והיכולת לעכב את התגובה האוטומטית לקריאת המילה. מצב הקונפליקט במבחן סטרופ מחייב הפעלת מנגנוני בקרה קוגניטיביים חזקים יותר כדי לעצור את התגובה הלא רלוונטית.</li>
    </ul>

    <h3>אזורי מוח ורשתות קשב בפעולה</h3>
    <p>מחקרים מתקדמים מראים שאפקט סטרופ מערב אזורי מוח חיוניים לתפקודים ניהוליים:</p>
    <ul>
        <li>**קליפת המוח הקדם-מצחית (Prefrontal Cortex):** מרכז הבקרה של המוח. אזורים אלה, במיוחד בחלק הקדמי-צדדי, פעילים במיוחד במצבי קונפליקט ומסייעים בעכבת תגובות אוטומטיות ובהגברת הקשב למידע הרלוונטי.</li>
        <li>**קליפת החגורה הקדמית (Anterior Cingulate Cortex - ACC):** מתפקדת כמערכת ניטור שגיאות וקונפליקטים. ה-ACC מזהה את ההתנגשות בין התגובה האוטומטית לתגובה הנדרשת במבחן סטרופ, ומאותת לאזורים אחרים להגביר את המאמץ הקוגניטיבי.</li>
    </ul>

    <h3>יישומים בחיי היומיום ובפסיכולוגיה</h3>
    <p>מבחן סטרופ אינו רק הדגמה מעבדתית, הוא כלי חשוב:</p>
    <ul>
        <li>**הערכה קוגניטיבית:** משמש לאבחון קשיי קשב וריכוז (ADHD), פגיעות מוחיות, סכיזופרניה, דיכאון, והפרעות נוירולוגיות ופסיכיאטריות אחרות המשפיעות על תפקודים ניהוליים ובקרה קוגניטיבית.</li>
        <li>**הבנת התפתחות:** השיפור בביצועי סטרופ לאורך הילדות מדגים את ההתפתחות של יכולות הבקרה הקוגניטיבית במוח המתבגר.</li>
        <li>**חיי היומיום:** היכולת להתעלם ממידע מסיח (כמו קריאת שלטי חוצות בזמן נהיגה, או התעלמות מרעשי רקע בעבודה) קשורה למנגנונים הפועלים במבחן סטרופ.</li>
    </ul>

    <p>אז בפעם הבאה שתתקשו במבחן סטרופ, זכרו שאתם חווים ממקור ראשון את המאבק המורכב והמרתק שמתרחש כל הזמן בתוך המוח שלכם!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const wordDisplay = document.getElementById('word-display');
    const instructionText = document.getElementById('instruction-text');
    const trialCounterDisplay = document.getElementById('trial-counter');
    const colorButtons = document.querySelectorAll('.color-button');
    const startButton = document.getElementById('start-button');
    const restartButton = document.getElementById('restart-button');
    const startScreen = document.getElementById('start-screen');
    const gameContainer = document.getElementById('game-container');
    const colorButtonsContainer = document.getElementById('color-buttons');
    const resultsScreen = document.getElementById('results-screen');
    const totalTrialsSpan = document.getElementById('total-trials-count');
    const errorCountSpan = document.getElementById('error-count');
    const avgRtCongruentSpan = document.getElementById('avg-rt-congruent');
    const avgRtIncongruentSpan = document.getElementById('avg-rt-incongruent');
    const resultsSummary = document.getElementById('results-summary');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Configuration & State
    const colors = {
        red: { name: 'אדום', hex: '#dc3545' }, /* Using danger-red for word color */
        blue: { name: 'כחול', hex: '#007bff' }, /* Using primary-blue for word color */
        green: { name: 'ירוק', hex: '#28a745' }, /* Using success-green for word color */
        yellow: { name: 'צהוב', hex: '#f0ad4e' } /* Original darker yellow for word color */
    };
    const totalTrialsPerGame = 20;
    let gameState = 'start'; // 'start', 'playing', 'feedback', 'results'
    let trials = [];
    let currentTrial = null;
    let startTime = null;
    let trialCount = 0;

    // --- Game Logic ---

    function getRandomColorKey() {
        const colorKeys = Object.keys(colors);
        return colorKeys[Math.floor(Math.random() * colorKeys.length)];
    }

    function generateTrial() {
        const wordKey = getRandomColorKey(); // The color name to display as text
        const textColorKey = getRandomColorKey(); // The actual color of the text

        return {
            word: colors[wordKey].name,
            textColor: colors[textColorKey].hex,
            correctAnswer: textColorKey,
            isCongruent: wordKey === textColorKey
        };
    }

    function updateUIState() {
        // Hide all primary screens first
        startScreen.classList.remove('active');
        gameContainer.classList.remove('active');
        colorButtonsContainer.classList.remove('active');
        resultsScreen.classList.remove('active');

        // Hide specific elements within game container
        wordDisplay.classList.remove('word-visible', 'word-correct', 'word-incorrect');
        wordDisplay.textContent = '';
        instructionText.textContent = '';
        trialCounterDisplay.textContent = '';
        colorButtons.forEach(button => button.disabled = false); // Enable buttons for playing state

        switch (gameState) {
            case 'start':
                startScreen.classList.add('active');
                break;
            case 'playing':
                gameContainer.classList.add('active');
                colorButtonsContainer.classList.add('active');
                instructionText.textContent = 'לחץ על כפתור הצבע שבו כתובה המילה:';
                trialCounterDisplay.textContent = `ניסיון ${trialCount + 1} מתוך ${totalTrialsPerGame}`;
                break;
            case 'feedback':
                 gameContainer.classList.add('active');
                 colorButtonsContainer.classList.add('active');
                 // Buttons should be disabled temporarily during feedback
                 colorButtons.forEach(button => button.disabled = true);
                 // Word display will be updated by showFeedback
                 instructionText.textContent = '...'; // Indicate processing
                 trialCounterDisplay.textContent = `ניסיון ${trialCount} מתוך ${totalTrialsPerGame}`;
                break;
            case 'results':
                resultsScreen.classList.add('active');
                break;
        }
    }

    function displayTrial() {
        if (trialCount >= totalTrialsPerGame) {
            endGame();
            return;
        }

        gameState = 'playing';
        updateUIState();

        currentTrial = generateTrial();
        wordDisplay.textContent = currentTrial.word;
        wordDisplay.style.color = currentTrial.textColor; // Apply the ink color

        // Trigger entrance animation
        // Use a slight delay to ensure display property is set before transition
        requestAnimationFrame(() => {
            wordDisplay.classList.add('word-visible');
        });

        startTime = performance.now(); // Start timing right before word appears
    }

    function showFeedback(isCorrect) {
         gameState = 'feedback';
         colorButtons.forEach(button => button.disabled = true); // Disable buttons during feedback

         // Apply feedback animation
         wordDisplay.classList.remove('word-visible'); // Hide current word
         // Re-apply color for potential flash animation
         wordDisplay.style.color = currentTrial.textColor; // Ensure color is correct for flash

         // Use a tiny delay before applying flash class for reliable animation re-trigger
         setTimeout(() => {
            if (isCorrect) {
                wordDisplay.classList.add('word-correct');
            } else {
                wordDisplay.classList.add('word-incorrect');
            }
         }, 50); // Short delay

        // Delay before moving to the next trial
        setTimeout(() => {
            trialCount++;
            displayTrial(); // Move to the next trial or end game
        }, 800); // Show feedback for 800ms
    }


    function recordResponse(selectedColorKey) {
        if (gameState !== 'playing' || !currentTrial) return;

        const reactionTime = performance.now() - startTime;
        const isCorrect = selectedColorKey === currentTrial.correctAnswer;

        trials.push({
            ...currentTrial,
            reactionTime: reactionTime,
            isCorrect: isCorrect,
            trialNumber: trialCount + 1 // Record trial number
        });

        currentTrial = null; // Prevent double clicking

        showFeedback(isCorrect); // Show visual feedback and then proceed
    }

    function startGame() {
        trialCount = 0;
        trials = [];
        gameState = 'playing'; // Will be set back to 'playing' by displayTrial
        updateUIState(); // Transition from start/results to game layout
        displayTrial(); // Start the first trial
    }

    function endGame() {
        gameState = 'results';
        updateUIState();

        // Calculate results
        const correctTrials = trials.filter(t => t.isCorrect);
        const errors = trials.length - correctTrials.length;

        const congruentCorrectTrials = correctTrials.filter(t => t.isCongruent);
        const incongruentCorrectTrials = correctTrials.filter(t => !t.isCongruent);

        const avgRtCongruent = congruentCorrectTrials.length > 0
            ? congruentCorrectTrials.reduce((sum, t) => sum + t.reactionTime, 0) / congruentCorrectTrials.length
            : 0;

        const avgRtIncongruent = incongruentCorrectTrials.length > 0
            ? incongruentCorrectTrials.reduce((sum, t) => sum + t.reactionTime, 0) / incongruentCorrectTrials.length
            : 0;

        // Display results
        totalTrialsSpan.textContent = trials.length;
        errorCountSpan.textContent = errors;
        avgRtCongruentSpan.textContent = avgRtCongruent.toFixed(0);
        avgRtIncongruentSpan.textContent = avgRtIncongruent.toFixed(0);

        // Add results summary text
        let summaryText = '';
        if (avgRtIncongruent > avgRtCongruent * 1.1) { // Arbitrary threshold for significant difference
             summaryText = `כצפוי, זמן התגובה הממוצע שלכם היה ארוך יותר במצבים שבהם צבע הדיו לא התאים למילה (${avgRtIncongruent} מ"ש) לעומת מצבים תואמים (${avgRtCongruent} מ"ש). זוהי הדגמה קלאסית של אפקט סטרופ!`;
        } else if (avgRtIncongruent > 0 && avgRtIncongruent > avgRtCongruent) {
             summaryText = `זמן התגובה הממוצע שלכם היה מעט ארוך יותר במצבי אי-התאמה (${avgRtIncongruent} מ"ש) לעומת מצבים תואמים (${avgRtCongruent} מ"ש), כפי שצפוי באפקט סטרופ.`;
        } else if (trials.length > 0) {
             summaryText = `לא נצפה הבדל משמעותי בזמני התגובה בין מצבים תואמים ולא תואמים. ייתכן שאתם מהירים במיוחד בזיהוי צבע, או שזה דורש יותר ניסיונות כדי להבחין באפקט.`;
        } else {
            summaryText = `אין מספיק נתונים להצגת תוצאות.`;
        }
        resultsSummary.textContent = summaryText;
    }

    // --- Event Listeners ---

    startButton.addEventListener('click', startGame);
    restartButton.addEventListener('click', startGame);

    colorButtons.forEach(button => {
        button.addEventListener('click', () => {
            recordResponse(button.getAttribute('data-color'));
        });
    });

    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (explanationDiv.classList.contains('hidden')) {
            toggleExplanationButton.textContent = 'הצג הסבר על אפקט סטרופ';
        } else {
             toggleExplanationButton.textContent = 'הסתר הסבר על אפקט סטרופ';
        }
    });

    // Initial state setup
    updateUIState(); // Set initial state to 'start'
});
</script>
```