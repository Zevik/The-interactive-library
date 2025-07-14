---
title: "חיפוש בינארי: משחק גילוי המספר הסודי (עם מחשב)"
english_slug: binary-search-simulation-finding-secret-number
category: "מדעי המחשב"
tags: ["מדעי המחשב", "אלגוריתמים", "חיפוש בינארי", "יעילות", "אינטראקטיבי", "הדמיה"]
---
<h1>חיפוש בינארי: משחק גילוי המספר הסודי</h1>

<p>דמיינו שיש לכם מספר סודי נסתר בטווח עצום של אפשרויות. כמה מהר תוכלו למצוא אותו בוודאות? האם יש דרך חכמה יותר מ"נחש וקווה לטוב" או בדיקה אינסופית? בואו נשחק משחק שיראה לכם שיטה מדהימה למצוא דברים במהירות שיא – חיפוש בינארי!</p>

<div class="app-container">
    <h2>אתגר את המחשב: נחש את המספר שלי!</h2>
    <p>חשבו על מספר סודי כלשהו בין 1 ל-100. אל תגלו לי אותו עדיין! המחשב שלי ינסה לנחש אותו בדרך הכי חכמה שיש.</p>
    <div id="game-area">
        <div id="range-display">
            <div id="current-range-bar">
                <!-- Colored bar represents the current possible range -->
                <div id="min-indicator" class="range-indicator min">1</div>
                <div id="max-indicator" class="range-indicator max">100</div>
                <div id="guess-indicator" class="range-indicator guess">?</div>
            </div>
             <div id="range-labels">
                <span id="min-label">1</span>
                <span id="max-label">100</span>
            </div>
        </div>
        <div id="guess-area">
            <p id="guess-text">האם אתם מוכנים להתחיל?</p>
            <div id="feedback-buttons" class="hidden">
                <p>המספר הסודי שחשבת עליו...</p>
                <button id="btn-lower" class="feedback-button lower">נמוך יותר מהניחוש</button>
                <button id="btn-correct" class="feedback-button correct">זה בדיוק הניחוש!</button>
                <button id="btn-higher" class="feedback-button higher">גבוה יותר מהניחוש</button>
            </div>
            <button id="btn-start" class="action-button start">כן, בוא נתחיל!</button>
        </div>
        <p id="attempts-counter">ניסיונות: 0</p>
        <p id="result-message" class="hidden"></p>
        <button id="btn-reset" class="action-button reset hidden">שחק שוב</button>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">רוצים להבין איך המחשב מנחש כל כך מהר? (הסבר על חיפוש בינארי)</button>

<div id="explanation" class="hidden">
    <h2>הסבר: חיפוש בינארי - המפתח ליעילות במדעי המחשב</h2>

    <h3>מבוא למשחק 'נחש את המספר'</h3>
    <p>משחק 'נחש את המספר' הוא מודל פנטסטי שמדגים את הליבה של אלגוריתמי חיפוש. צד אחד מסתיר פריט (המספר), והצד השני מנסה למצוא אותו באמצעות שאלות שמצמצמות את האפשרויות.</p>

    <h3>אסטרטגיות חיפוש: טוב, רע, ומצוין</h3>
    <p>איך אפשר למצוא פריט בטווח נתון? יש דרכים שונות, לא כולן חכמות:</p>
    <ul>
        <li>**ניחוש אקראי:** לבחור מספרים באקראי עד שפוגעים. זו הימור טהור, יכול לקחת נצח.</li>
        <li>**חיפוש סדרתי (ליניארי):** להתחיל מהפריט הראשון (1) ולשאול אם זה המספר הסודי. אם לא, לעבור ל-2, 3, וכן הלאה. מובטח שתמצאו, אבל במקרה הגרוע ביותר (אם המספר הוא 100), זה ייקח 100 שאלות. זה משעמם ואיטי!</li>
    </ul>

    <h3>הסוד: לפסול חצי מהאפשרויות בכל פעם!</h3>
    <p>השיטות הפשוטות מתעלמות ממידע קריטי שקיבלנו. אם ניחשנו 50 וקיבלנו תשובה שהמספר נמוך יותר, אנחנו <strong>יודעים בוודאות</strong> שהמספר הוא איפשהו בין 1 ל-49. <strong>כל המספרים מ-50 ומעלה נפסלו מיידית!</strong> זה הרעיון הגאוני מאחורי חיפוש יעיל: להשתמש בכל פיסת מידע כדי למחוק חלקים גדולים ממרחב החיפוש.</p>

    <h3>חיפוש בינארי: האלגוריתם שמשנה את המשחק</h3>
    <p>חיפוש בינארי (Binary Search) הוא אלגוריתם שמיישם את הרעיון הזה בצורה הכי יעילה שיש (עבור רשימות או טווחים ממוינים). ככה זה עובד (כמו שראיתם בהדמיה):</p>
    <ol>
        <li>**התחלה בטווח מלא:** יש לנו טווח התחלתי של מספרים אפשריים (למשל, 1 עד 100).</li>
        <li>**ניחוש האמצע:** בוחרים את המספר שנמצא בדיוק באמצע הטווח הנוכחי. (למשל, בטווח 1-100, הניחוש הראשון יהיה 50).</li>
        <li>**צמצום הטווח לפי המשוב:**
            <ul>
                <li>אם הניחוש הוא המספר הסודי - מצאת! סיימתם את החיפוש.</li>
                <li>אם המספר הסודי נמוך מהניחוש - זורקים את חצי הטווח העליון. הטווח החדש הוא מהמינימום הנוכחי ועד הניחוש פחות 1.</li>
                <li>אם המספר הסודי גבוה מהניחוש - זורקים את חצי הטווח התחתון. הטווח החדש הוא מהניחוש פלוס 1 ועד המקסימום הנוכחי.</li>
            </ul>
        </li>
        <li>**חוזרים על הקסם:** חוזרים לשלב 2 עם הטווח המצומצם, עד שהטווח מצטמצם למספר אחד בלבד (שחייב להיות המספר הסודי) או עד שמצאתם אותו.</li>
    </ol>
    <p><strong>בכל שלב, חיפוש בינארי מפסל פחות או יותר חצי ממרחב החיפוש הנותר!</strong> זו הסיבה למהירות המדהימה שלו.</p>

    <h3>היעילות המדהימה בפועל</h3>
    <p>כפי שראיתם במשחק, מציאת מספר בטווח 1-100 לוקחת לכל היותר 7 ניסיונות. מה לגבי טווח ענק של 1 עד 1,000,000 (מיליון)? חיפוש סדרתי יכול לקחת מיליון ניסיונות. חיפוש בינארי? לכל היותר 20 ניסיונות! (כי 2 בחזקת 20 זה קצת יותר ממיליון). היעילות גדלה דרמטית ככל שהטווח גדל.</p>
    <p>המספר המקסימלי של ניסיונות בחיפוש בינארי בטווח בגודל N הוא בערך log₂N (לוגריתם בבסיס 2 של N).</p>

    <h3>איפה פוגשים חיפוש בינארי בחיים האמיתיים?</h3>
    <p>חיפוש בינארי הוא לא רק משחק מספרים. זהו אחד מאלגוריתמי היסוד במדעי המחשב, והוא נמצא בשימוש יומיומי במקומות רבים:</p>
    <ul>
        <li>**חיפוש במילון או אנציקלופדיה:** אתם לא דפדפים עמוד-עמוד מההתחלה. אתם פותחים בערך באמצע, בודקים אם המילה לפני או אחרי, וממשיכים בחצי המתאים. זה בדיוק חיפוש בינארי ידני!</li>
        <li>**בסיסי נתונים:** כשאתר אינטרנט או אפליקציה שולפים מידע מבסיס נתונים ענק, אלגוריתמים שמבוססים על חיפוש בינארי עוזרים למצוא את המידע הנדרש במהירות מסחררת.</li>
        <li>**איתור באגים בקוד:** מפתחים משתמשים לעיתים בגישה "בינארית" (המכונה גם "bisect") כדי למצוא מתי בדיוק באג מסוים הופיע בהיסטוריית השינויים של הקוד.</li>
        <li>**חיפוש ספר ספציפי בספרייה לפי שם המחבר ברשימה ממוינת.**</li>
    </ul>

    <h3>התובנה המרכזית</h3>
    <p>התובנה העמוקה ביותר מחיפוש בינארי היא כוחו של המיון. כשיש לנו מידע ממוין, אנחנו לא צריכים לבדוק כל פריט בנפרד. אנחנו יכולים להשתמש במיון כדי לפסול חצי מהאפשרויות בכל פעם, מה שהופך בעיות חיפוש ענקיות לפתירות במספר זעיר של צעדים. זהו עיקרון יסוד באופטימיזציה ויעילות.</p>
</div>

<style>
    /* General Styling */
    .app-container, #explanation {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 700px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        direction: rtl;
        text-align: right;
        color: #333;
    }

    h1, h2 {
        text-align: center;
        color: #0056b3; /* A nice blue */
        margin-bottom: 15px;
    }

    p {
        line-height: 1.6;
        margin-bottom: 12px;
    }

    /* Game Area Styling */
    #game-area {
        margin-top: 25px;
        padding: 20px;
        border: 1px solid #eee;
        border-radius: 8px;
        background-color: #f8f9fa;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    #range-display {
        margin-bottom: 30px;
        text-align: center;
        position: relative;
        padding-top: 25px; /* Space for guess indicator above */
        padding-bottom: 25px; /* Space for labels below */
    }

    #current-range-bar {
        height: 20px;
        background-color: #e9ecef; /* Light grey background */
        border-radius: 10px;
        position: relative;
        overflow: hidden;
    }

    #current-range-bar::before {
        content: '';
        position: absolute;
        top: 0;
        bottom: 0;
        left: var(--range-start, 0%);
        right: var(--range-end, 0%);
        background-color: #6ab04c; /* Vibrant green for the valid range */
        transition: left 0.8s ease-out, right 0.8s ease-out; /* Smooth transition for range update */
    }

    .range-indicator {
        position: absolute;
        bottom: -5px; /* Position below the bar */
        transform: translateX(50%); /* Center indicator on its point */
        font-size: 0.9em;
        font-weight: bold;
        color: #000;
        z-index: 2; /* Ensure indicators are above the bar */
        transition: left 0.8s ease-out; /* Smooth transition for indicator movement */
    }

    .range-indicator.min { left: var(--min-pos, 0%); color: #212529; }
    .range-indicator.max { left: var(--max-pos, 100%); color: #212529; }
    .range-indicator.guess {
        left: var(--guess-pos, 50%);
        top: -25px; /* Position well above the bar */
        bottom: auto;
        color: #d9534f; /* Red for guess */
        font-size: 1.1em;
    }

    #range-labels {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: space-between;
        font-size: 0.8em;
        color: #555;
    }

    #guess-area {
        text-align: center;
        margin-bottom: 20px;
        min-height: 80px; /* Reserve space to prevent layout shifts */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    #guess-text {
        font-size: 1.3em;
        font-weight: bold;
        color: #333;
        margin-bottom: 15px;
    }

    #feedback-buttons {
        margin-top: 10px;
    }

    #feedback-buttons p {
         margin-bottom: 10px;
         font-weight: normal;
         font-size: 1em;
         color: #555;
    }

    .feedback-button {
        margin: 0 8px;
        padding: 10px 18px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        min-width: 120px; /* Ensure consistent button size */
    }

    .feedback-button.lower { background-color: #ffc107; color: #212529; } /* Warning yellow */
    .feedback-button.correct { background-color: #28a745; color: white; } /* Success green */
    .feedback-button.higher { background-color: #007bff; color: white; } /* Primary blue */

    .feedback-button:hover {
        opacity: 0.9;
    }

    .feedback-button:active {
        transform: scale(0.98);
    }


    .action-button {
        display: block;
        width: fit-content;
        margin: 15px auto 0; /* Center button and add top margin */
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .action-button.start { background-color: #17a2b8; color: white; } /* Info blue */
    .action-button.reset { background-color: #dc3545; color: white; } /* Danger red */

     .action-button:hover {
        opacity: 0.9;
    }

    .action-button:active {
        transform: scale(0.98);
    }

    #attempts-counter {
        text-align: center;
        font-size: 1em;
        color: #555;
        margin-top: 15px;
    }

    #result-message {
        text-align: center;
        font-size: 1.4em;
        font-weight: bold;
        color: #28a745; /* Green for success */
        margin-top: 15px;
        min-height: 1.6em; /* Reserve space */
    }

    .hidden {
        display: none;
    }

    /* Explanation Styling */
    .toggle-button {
        display: block;
        width: fit-content;
        margin: 30px auto 20px; /* Center and add margin */
        padding: 10px 20px;
        background-color: #e9ecef; /* Light grey */
        border: 1px solid #ced4da; /* Grey border */
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        color: #495057; /* Dark grey text */
        transition: background-color 0.2s ease;
    }

    .toggle-button:hover {
        background-color: #ced4da; /* Slightly darker grey on hover */
    }

    #explanation h3 {
        color: #007bff; /* Primary blue */
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }

    #explanation ul, #explanation ol {
        margin-bottom: 15px;
        padding-right: 25px; /* Adjust padding for RTL lists */
    }

    #explanation li {
        margin-bottom: 8px;
        color: #555;
    }

     /* Animation for Guess Indicator */
    .range-indicator.guess.guessing {
        animation: pulse-guess 1.5s infinite ease-in-out;
    }

    @keyframes pulse-guess {
        0% { transform: translateX(50%) scale(1); opacity: 1; }
        50% { transform: translateX(50%) scale(1.05); opacity: 0.9; }
        100% { transform: translateX(50%) scale(1); opacity: 1; }
    }


</style>

<script>
    let minRange = 1;
    let maxRange = 100;
    let currentMin = minRange;
    let currentMax = maxRange;
    let currentGuess = null;
    let attempts = 0;
    let isGuessing = false; // Flag to prevent multiple guesses

    const rangeBar = document.getElementById('current-range-bar');
    const minIndicator = document.getElementById('min-indicator');
    const maxIndicator = document.getElementById('max-indicator');
    const guessIndicator = document.getElementById('guess-indicator');
    const minLabel = document.getElementById('min-label');
    const maxLabel = document.getElementById('max-label');
    const guessText = document.getElementById('guess-text');
    const feedbackButtonsDiv = document.getElementById('feedback-buttons');
    const btnStart = document.getElementById('btn-start');
    const btnLower = document.getElementById('btn-lower');
    const btnCorrect = document.getElementById('btn-correct');
    const btnHigher = document.getElementById('btn-higher');
    const attemptsCounter = document.getElementById('attempts-counter');
    const resultMessage = document.getElementById('result-message');
    const btnReset = document.getElementById('btn-reset');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Function to update the visual representation of the range and guess
    function updateRangeDisplay() {
        const totalRangeSize = maxRange - minRange;
        if (totalRangeSize <= 0) {
            // Handle edge case of invalid or empty range
            minIndicator.style.setProperty('--min-pos', '50%');
            maxIndicator.style.setProperty('--max-pos', '50%');
             // Position guess slightly off-center or hide if range is invalid
            guessIndicator.style.setProperty('--guess-pos', '50%');
            rangeBar.style.setProperty('--range-start', '50%');
            rangeBar.style.setProperty('--range-end', '50%');
            minIndicator.textContent = currentMin;
            maxIndicator.textContent = currentMax;
            guessIndicator.textContent = currentGuess !== null ? currentGuess : '?'; // Show last guess or ?
             // Update indicator visibility if range is invalid
            minIndicator.classList.remove('hidden'); // Show boundaries
            maxIndicator.classList.remove('hidden');
            guessIndicator.classList.remove('hidden'); // Show guess indicator
            return;
        }


        // Ensure currentMin/Max/Guess are within the initial minRange/maxRange boundaries
        // This prevents indicators from going outside the visible bar area
        const clampedCurrentMin = Math.max(minRange, currentMin);
        const clampedCurrentMax = Math.min(maxRange, currentMax);
        const clampedGuess = Math.max(minRange, Math.min(maxRange, currentGuess || minRange));


        // Calculate positions as percentages relative to the *full initial range*
        const minPos = ((clampedCurrentMin - minRange) / totalRangeSize) * 100;
        const maxPos = ((clampedCurrentMax - minRange) / totalRangeSize) * 100;
        const guessPos = ((clampedGuess - minRange) / totalRangeSize) * 100;

        // Update CSS variables for smooth transitions
        minIndicator.style.setProperty('--min-pos', minPos + '%');
        maxIndicator.style.setProperty('--max-pos', maxPos + '%');
        guessIndicator.style.setProperty('--guess-pos', guessPos + '%');

        // Update the colored bar section
        rangeBar.style.setProperty('--range-start', minPos + '%');
        rangeBar.style.setProperty('--range-end', (100 - maxPos) + '%'); // distance from right edge

        // Update text labels
        minIndicator.textContent = currentMin;
        maxIndicator.textContent = currentMax;
        guessIndicator.textContent = currentGuess !== null ? currentGuess : '?'; // Show current guess or ?
        minLabel.textContent = minRange; // Initial labels remain constant
        maxLabel.textContent = maxRange;

        // Show indicators if game is active
        minIndicator.classList.remove('hidden');
        maxIndicator.classList.remove('hidden');
        guessIndicator.classList.remove('hidden');
    }

    // Function to make the computer's next guess
    async function makeGuess() {
         if (isGuessing) return; // Prevent multiple clicks triggering guesses
         isGuessing = true;

        attempts++;
        attemptsCounter.textContent = `ניסיונות: ${attempts}`;

        // Calculate the middle number (integer division)
        // For range [min, max], the middle is min + floor((max - min) / 2)
        const nextGuess = currentMin + Math.floor((currentMax - currentMin) / 2);
        currentGuess = nextGuess; // Update currentGuess

        // Add a "thinking" animation or state
        guessText.textContent = "המחשב חושב...";
        guessIndicator.textContent = '?'; // Hide previous guess briefly
        guessIndicator.classList.add('guessing'); // Add pulse animation

        // Update display with the new range boundaries before showing the guess
        updateRangeDisplay();

        // Wait for a short delay to simulate thinking and allow animation
        await new Promise(resolve => setTimeout(resolve, 1000)); // 1 second delay

        // Now reveal the guess
        guessText.textContent = `האם המספר הסודי שלך הוא ${currentGuess}?`;
        guessIndicator.textContent = currentGuess; // Show the new guess
        guessIndicator.classList.remove('guessing'); // Remove pulse animation

        feedbackButtonsDiv.classList.remove('hidden'); // Show feedback buttons
        isGuessing = false; // Allow feedback interaction
    }

    // Function to handle user feedback
    function handleFeedback(feedback) {
        if (isGuessing) return; // Don't handle feedback while guessing

        feedbackButtonsDiv.classList.add('hidden'); // Hide feedback buttons

        if (feedback === 'correct') {
            guessText.textContent = `מצוין! המחשב מצא את המספר הסודי (${currentGuess}) ב-${attempts} ניסיונות בלבד.`;
            resultMessage.textContent = "חיפוש בינארי הוא באמת שיטה מדהימה!";
            resultMessage.style.color = '#28a745'; // Green
            resultMessage.classList.remove('hidden');
            btnReset.classList.remove('hidden');
            guessIndicator.style.color = '#28a745'; // Highlight correct guess color
            // Keep guess indicator visible and showing the correct number
            guessIndicator.classList.remove('hidden');

        } else {
            if (feedback === 'lower') {
                // If the number is lower than currentGuess, the new max is currentGuess - 1
                currentMax = currentGuess - 1;
            } else if (feedback === 'higher') {
                 // If the number is higher than currentGuess, the new min is currentGuess + 1
                currentMin = currentGuess + 1;
            }

            // Check if the range is still valid
            if (currentMin > currentMax) {
                // This happens if the user gave contradictory feedback
                guessText.textContent = `נראה שיש אי-התאמה במידע שסיפקת. הטווח הפך לא חוקי (${currentMin}-${currentMax}).`;
                resultMessage.textContent = "אנא ודא שהתשובות שלך עקביות.";
                resultMessage.style.color = '#dc3545'; // Red for error
                resultMessage.classList.remove('hidden');
                btnReset.classList.remove('hidden');
                 // Hide guess indicator as there's no valid next guess state
                guessIndicator.classList.add('hidden');
                 // Update range display to show the conflicting state
                updateRangeDisplay();
            } else {
                 // If range is valid, make the next guess
                 makeGuess();
            }
        }
    }

    // Function to start a new game round
    function startGame() {
        // Fixed range for this demo
        minRange = 1;
        maxRange = 100;
        currentMin = minRange;
        currentMax = maxRange;
        attempts = 0;
        currentGuess = null; // Reset guess

        // Reset UI elements
        attemptsCounter.textContent = `ניסיונות: 0`;
        resultMessage.classList.add('hidden');
        resultMessage.style.color = '#28a745'; // Reset color
        btnReset.classList.add('hidden');
        btnStart.classList.add('hidden');
        feedbackButtonsDiv.classList.add('hidden'); // Hide feedback buttons initially
        guessText.textContent = "מתחילים..."; // Initial text
        guessIndicator.style.color = '#d9534f'; // Reset guess indicator color
        guessIndicator.classList.remove('guessing'); // Remove animation class

        // Update display to show the initial full range
        updateRangeDisplay();

        // Start the first guess after a short delay
        setTimeout(makeGuess, 500); // Delay before first guess
    }

    // Function to reset the game completely
    function resetGame() {
        minRange = 1;
        maxRange = 100;
        currentMin = minRange;
        currentMax = maxRange;
        attempts = 0;
        currentGuess = null;

        attemptsCounter.textContent = `ניסיונות: 0`;
        guessText.textContent = "בואו נשחק: 'נחש את המספר' עם מחשב";
        resultMessage.classList.add('hidden');
        btnReset.classList.add('hidden');
        feedbackButtonsDiv.classList.add('hidden');
        btnStart.classList.remove('hidden');
        guessIndicator.style.color = '#d9534f'; // Reset guess indicator color
        guessIndicator.classList.remove('guessing'); // Remove animation class

        // Reset range visualization to initial state
        updateRangeDisplay();
    }

    // Function to toggle the explanation visibility
    function toggleExplanation() {
        explanationDiv.classList.toggle('hidden');
        if (explanationDiv.classList.contains('hidden')) {
            toggleExplanationBtn.textContent = 'רוצים להבין איך המחשב מנחש כל כך מהר? (הסבר על חיפוש בינארי)';
        } else {
            toggleExplanationBtn.textContent = 'הסתר הסבר';
        }
    }

    // Event Listeners
    btnStart.addEventListener('click', startGame);
    btnLower.addEventListener('click', () => handleFeedback('lower'));
    btnCorrect.addEventListener('click', () => handleFeedback('correct'));
    btnHigher.addEventListener('click', () => handleFeedback('higher'));
    btnReset.addEventListener('click', resetGame);
    toggleExplanationBtn.addEventListener('click', toggleExplanation);

    // Initial state setup when the page loads
    resetGame();
</script>
---