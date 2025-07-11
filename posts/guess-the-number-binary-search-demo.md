---
title: "האתגר: לנחש מספר במינימום מהלכים (הדגמת חיפוש בינארי)"
english_slug: guess-the-number-binary-search-demo
category: "אלגוריתמים"
tags: [מבני-נתונים, חיפוש, הדמיה, אינטראקטיבי, אלגוריתם-חיפוש-בינארי]
---
# האתגר: לנחש מספר במינימום מהלכים

האם אתם מוכנים לאתגר את המחשב במשחק ניחוש מספרים? חשבו על מספר סודי, ואני אנסה לנחש אותו במהירות שיא באמצעות אסטרטגיה מדהימה! בואו נראה כמה מהלכים אצטרך...

<div id="app-container">
    <div class="game-area">
        <h2>המהלך שלי:</h2>
        <p class="instructions">חשוב/י על מספר שלם <strong class="highlight-text">בין 1 ל-100</strong>. לחץ/י "התחל את האתגר!" כשתהיה מוכן/ה.</p>
        <div id="range-display" class="display-box range-box">
            <span class="label">טווח החיפוש:</span> <span class="value">[1 - 100]</span>
        </div>
        <div id="computer-guess" class="display-box guess-box">
            <span class="label">הניחוש הנוכחי:</span> <span class="value">...מחכה לאתגר...</span>
        </div>
         <div id="guess-count-display" class="display-box count-box hidden">
            <span class="label">מהלך מס':</span> <span class="value">0</span>
        </div>

        <div class="feedback-buttons">
            <button id="btn-too-low" class="btn-feedback btn-too-low" disabled><span class="emoji">👇</span> נמוך מדי</button>
            <button id="btn-correct" class="btn-feedback btn-correct" disabled><span class="emoji">🎯</span> בול!</button>
            <button id="btn-too-high" class="btn-feedback btn-too-high" disabled><span class="emoji">👆</span> גבוה מדי</button>
        </div>
        <button id="btn-start-game" class="btn-primary">התחל את האתגר!</button>
        <p id="game-message" class="game-message"></p>
    </div>
    <div class="history-area">
        <h3>יומן הניחושים:</h3>
        <ul id="guess-history">
            <li class="history-placeholder">...כאן תופיע היסטוריית המהלכים...</li>
        </ul>
    </div>
</div>

<button id="toggle-explanation" class="btn-secondary explanation-button">מה קרה כאן? (הצג/הסתר הסבר)</button>

<div id="explanation" class="explanation-section hidden">
    <h2>מאחורי הקלעים: סוד החיפוש הבינארי המהיר!</h2>
    <p>המשחק ששיחקתם הרגע מדגים עיקרון יסודי ויעיל במדעי המחשב שנקרא <b>חיפוש בינארי</b> (Binary Search). זו לא סתם ניחוש אקראי – זו אסטרטגיה חכמה שמאפשרת למצוא פריטים במהירות שיא בתוך רשימה ממוינת (ובמקרה שלנו, המספרים 1-100 הם רשימה כזו).</p>
    <p>איך זה עובד?</p>
    <ol>
        <li>**מתחילים רחב:** קובעים את הטווח ההתחלתי שבו המספר הסודי יכול להימצא (אצלנו, [1 - 100]).</li>
        <li>**תמיד האמצע!** במקום לנחש סתם, האלגוריתם תמיד מנחש את המספר שנמצא בדיוק באמצע הטווח הנוכחי. זה המהלך האסטרטגי המרכזי!</li>
        <li>**קבלת משוב מדויק:** אתם נותנים למחשב מידע קריטי - האם המספר הסודי שלכם גבוה, נמוך, או זהה לניחוש.</li>
        <li>**חותכים את הטווח בחצי!** זה הקסם!
            <ul>
                <li>אם אמרתם שהמספר <span class="highlight-too-low">גבוה יותר</span> ("נמוך מדי" על הניחוש), המחשב מבין שהמספר שלכם חייב להיות בחצי ה<span class="highlight-too-low">עליון</span> של הטווח הנוכחי. הוא זורק את החצי התחתון ומתמקד רק בחלק שמעל הניחוש (ועד סוף הטווח הישן).</li>
                <li>אם אמרתם שהמספר <span class="highlight-too-high">נמוך יותר</span> ("גבוה מדי" על הניחוש), המחשב זורק את החצי ה<span class="highlight-too-high">עליון</span> ומתמקד רק בחלק שמתחת לניחוש (מתחילת הטווח הישן ועד מתחת לניחוש).</li>
            </ul>
            בכל שלב, הטווח הפוטנציאלי שבו המספר הסודי יכול להיות <b>נחתך בערך בחצי!</b> תחשבו על זה - כמה מהר אפשר לצמצם טווח של 100 מספרים כשבכל פעם נשארים רק עם חצי מהם?</li>
        <li>**חוזרים על התהליך:** עכשיו, כשהטווח קטן בהרבה, חוזרים לשלב 2 - מנחשים שוב את האמצע של הטווח ה<span class="highlight-text">חדש והמצומצם</span>.</li>
    </ol>
    <p>זו הסיבה שחיפוש בינארי יעיל כל כך! הוא מבטיח שתמצאו את המספר (או תגלו שהוא לא בטווח) במספר מינימלי של מהלכים. זה כמו לשחק "חם-קר", אבל בשיטה מדעית!</p>
    <p>הביטו שוב ב"יומן הניחושים" - תוכלו לראות איך הטווח [min - max] הלך והצטמצם דרמטית בכל מהלך. מרשים, נכון?</p>
</div>

<style>
    /* Importing a Google Font for better typography */
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

    body {
        font-family: 'Rubik', sans-serif;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); /* Subtle gradient background */
        color: #333;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    h1, h2, h3 {
        color: #0d47a1; /* Darker blue */
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700;
    }

    h1 {
        font-size: 2.5em;
        margin-top: 0;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    h2 {
        font-size: 1.8em;
        border-bottom: 2px solid #0d47a1;
        padding-bottom: 5px;
        display: inline-block; /* To make border-bottom fit content */
        margin-left: auto; /* Center the inline block */
        margin-right: auto;
    }

    #app-container {
        display: flex;
        flex-wrap: wrap;
        gap: 40px; /* Increased gap */
        justify-content: center;
        width: 100%;
        max-width: 1000px; /* Max width for container */
        margin: 20px auto;
    }

    .game-area, .history-area {
        background-color: #ffffff;
        border-radius: 16px; /* More rounded corners */
        padding: 30px; /* More padding */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* More prominent shadow */
        flex: 1;
        min-width: 320px; /* Allow wrapping on smaller screens */
        max-width: 550px; /* Slightly increased max width */
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

     .history-area {
         text-align: right;
         align-items: flex-start;
     }

    .instructions {
        font-size: 1.1em;
        color: #555;
        margin-bottom: 25px;
    }

    .highlight-text {
        color: #e65100; /* Orange highlight */
        font-weight: 700;
    }
     .highlight-too-low { color: #ff9800; font-weight: 700; } /* Orange */
     .highlight-too-high { color: #f44336; font-weight: 700; } /* Red */


    .display-box {
        font-size: 1.3em; /* Larger font */
        margin: 15px 0;
        padding: 15px; /* More padding */
        border: 1px solid #ccc;
        border-radius: 8px; /* Rounded corners */
        width: 100%; /* Fill container width */
        box-sizing: border-box; /* Include padding in width */
        min-height: 2.5em; /* Ensure stable height */
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px; /* Space between label and value */
    }

     .display-box .label {
         font-weight: 500;
         color: #555;
     }
     .display-box .value {
         font-weight: 700;
         color: #0d47a1; /* Default value color */
     }

    .range-box {
        background-color: #e3f2fd; /* Light blue */
        border-color: #bbdefb;
        border-left: 8px solid #2196f3; /* Blue accent */
    }
     .range-box .value { color: #2196f3; } /* Blue value */


    .guess-box {
        background-color: #e8f5e9; /* Light green */
        border-color: #c8e6c9;
        border-left: 8px solid #4caf50; /* Green accent */
    }
     .guess-box .value {
         color: #4caf50; /* Green value */
         font-size: 1.5em; /* Slightly larger guess value */
     }


     .count-box {
         background-color: #fff9c4; /* Light yellow */
         border-color: #fff59d;
         border-left: 8px solid #ffeb3b; /* Yellow accent */
     }
      .count-box .value { color: #fbc02d; } /* Darker yellow value */

    .feedback-buttons {
        margin: 25px 0; /* More margin */
        display: flex;
        justify-content: center;
        gap: 15px; /* More space between buttons */
        flex-wrap: wrap; /* Allow buttons to wrap */
    }

    button {
        padding: 12px 20px; /* More padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        transition: background-color 0.3s ease, opacity 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        min-width: 100px;
        font-weight: 500;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    button:hover:not(:disabled) {
        opacity: 0.95;
        transform: translateY(-2px); /* Slight lift effect */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
     button:active:not(:disabled) {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
     }


    button:disabled {
        opacity: 0.6; /* Make disabled more distinct */
        cursor: not-allowed;
        box-shadow: none;
    }

    .btn-primary {
        background-color: #4caf50; /* Green */
        color: white;
        margin-top: 20px;
        font-size: 1.3em; /* Larger start button */
        padding: 15px 30px;
    }

    .btn-primary:hover:not(:disabled) {
        background-color: #388e3c; /* Darker green */
    }

    .btn-feedback {
         color: #333; /* Default feedback button text color */
         display: flex;
         align-items: center;
         justify-content: center;
         gap: 5px;
    }

    .btn-too-low {
        background-color: #ffb300; /* Amber */
    }
    .btn-too-low:hover:not(:disabled) {
         background-color: #fb8c00; /* Darker amber */
    }

    .btn-correct {
        background-color: #4caf50; /* Green */
        color: white;
    }
    .btn-correct:hover:not(:disabled) {
        background-color: #388e3c; /* Darker green */
    }

    .btn-too-high {
        background-color: #e53935; /* Red */
        color: white;
    }
    .btn-too-high:hover:not(:disabled) {
        background-color: #c62828; /* Darker red */
    }

    .emoji {
        font-size: 1.2em;
    }

    .game-message {
        margin-top: 20px;
        font-size: 1.2em;
        font-weight: 700;
        color: #0d47a1; /* Default message color */
        min-height: 1.5em; /* Reserve space */
    }
     .game-message.success { color: #388e3c; } /* Green for success */
     .game-message.error { color: #c62828; } /* Red for error */


    .history-area ul {
        list-style: none;
        padding: 0;
        width: 100%; /* Ensure list takes full width */
    }

    .history-area li {
        background-color: #f5f5f5; /* Light grey background */
        margin-bottom: 12px; /* More space */
        padding: 12px; /* More padding */
        border-radius: 8px; /* Rounded corners */
        border-right: 6px solid #2196f3; /* Accent border */
        opacity: 0; /* Start hidden for animation */
        transform: translateY(15px); /* Start lower for animation */
        animation: fadeInSlideUp 0.5s ease forwards; /* Apply animation */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
         font-size: 0.95em;
    }
    .history-area li:last-child {
        margin-bottom: 0; /* No margin for last item */
    }

    /* Animation for history items */
    @keyframes fadeInSlideUp {
        to { opacity: 1; transform: translateY(0); }
    }

     .history-placeholder {
         text-align: center;
         color: #777;
         font-style: italic;
         border-right: none;
         background-color: transparent;
         box-shadow: none;
         transform: none;
         animation: none;
     }

    .btn-secondary {
        display: block;
        width: fit-content;
        margin: 40px auto 20px auto; /* More vertical margin */
        background-color: #78909c; /* Blue grey */
        color: white;
        font-size: 1.1em;
        padding: 12px 25px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .btn-secondary:hover:not(:disabled) {
        background-color: #546e7a; /* Darker blue grey */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }


    .explanation-section {
        background-color: #fff9c4; /* Light warm background */
        border: 1px solid #ffecb3; /* Matching border */
        border-radius: 12px; /* Rounded corners */
        padding: 30px; /* More padding */
        margin-top: 20px;
        color: #5d4037; /* Dark brown text */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        max-width: 960px;
        width: 100%;
        box-sizing: border-box;
        opacity: 0; /* Start hidden for fade-in */
        transform: translateY(20px); /* Start lower */
        animation: fadeInSlideUp 0.6s ease forwards; /* Fade-in animation */
    }
    /* Override animation for the explanation section itself */
    .explanation-section.hidden {
        display: none;
        animation: none;
        opacity: 0;
        transform: translateY(0);
    }
     /* Specific styles within explanation */
     .explanation-section h2 {
         color: #f57c00; /* Orange heading */
         border-bottom-color: #f57c00;
     }
     .explanation-section ol,
     .explanation-section ul {
         margin-bottom: 20px;
         padding-right: 25px; /* Adjust padding for list markers */
     }
      .explanation-section li {
          margin-bottom: 10px;
          line-height: 1.8;
          background-color: transparent; /* Override history list style */
          border: none;
          box-shadow: none;
          opacity: 1; /* Override history animation */
          transform: none;
          animation: none;
      }
       .explanation-section li::marker {
           color: #f57c00; /* Color list markers */
           font-weight: bold;
       }
     .explanation-section b {
         color: #e65100; /* Highlight bold text */
         font-weight: 700;
     }


    .hidden {
        display: none;
    }

    /* Animations */
     @keyframes pulseHighlight {
         0% { background-color: #e3f2fd; border-left-color: #2196f3; }
         50% { background-color: #bbdefb; border-left-color: #1976d2; } /* Darker blue */
         100% { background-color: #e3f2fd; border-left-color: #2196f3; }
     }

     .range-box.highlight-range {
         animation: pulseHighlight 1.5s ease-in-out;
     }

     @keyframes guessFadeIn {
         from { opacity: 0; transform: scale(0.9); }
         to { opacity: 1; transform: scale(1); }
     }

     .guess-box .value {
         display: inline-block; /* Needed for transform */
         animation: guessFadeIn 0.5s ease-out; /* Apply animation to the guess value */
     }


     /* Responsive adjustments */
     @media (max-width: 768px) {
         #app-container {
             flex-direction: column;
             align-items: center;
             gap: 30px;
         }

         .game-area, .history-area {
             width: 95%;
             max-width: none;
         }

         .feedback-buttons {
             flex-direction: column;
             gap: 10px;
         }

         button {
             width: 100%;
             max-width: 250px; /* Limit button width on small screens */
             margin-left: auto;
             margin-right: auto;
         }

         .btn-primary {
             max-width: 300px;
         }
         .btn-secondary {
             max-width: 300px;
         }

         h1 { font-size: 2em; }
         h2 { font-size: 1.5em; }
         .display-box { font-size: 1.1em; }
         .guess-box .value { font-size: 1.3em; }
     }


</style>

<script>
    const rangeValueSpan = document.querySelector('#range-display .value');
    const computerGuessValueSpan = document.querySelector('#computer-guess .value');
    const guessCountValueSpan = document.querySelector('#guess-count-display .value');
    const guessCountDisplay = document.getElementById('guess-count-display');
    const guessHistoryList = document.getElementById('guess-history');
    const btnStart = document.getElementById('btn-start-game');
    const btnTooLow = document.getElementById('btn-too-low');
    const btnCorrect = document.getElementById('btn-correct');
    const btnTooHigh = document.getElementById('btn-too-high');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const gameMessagePara = document.getElementById('game-message');

    let minRange = 1;
    let maxRange = 100;
    let computerGuess = 0;
    let gameActive = false;
    let guessCount = 0;

    function updateRangeDisplay() {
        rangeValueSpan.textContent = `[${minRange} - ${maxRange}]`;
        // Add highlight animation class, then remove it
        const rangeDisplayBox = document.getElementById('range-display');
        rangeDisplayBox.classList.remove('highlight-range'); // Reset animation
        // Use setTimeout to ensure class is removed before adding it again for re-triggering
        setTimeout(() => {
            rangeDisplayBox.classList.add('highlight-range');
        }, 10); // Small delay to re-trigger animation
    }

    function makeComputerGuess() {
        if (minRange > maxRange) {
             displayGameMessage("אופס, משהו השתבש בטווח! הטווח הפוטנציאלי ריק. האם המספר הסודי היה בטווח המקורי (1-100)?", 'error');
             endGame();
             return;
        }
        guessCount++;
        guessCountValueSpan.textContent = guessCount;
        computerGuess = Math.floor((minRange + maxRange) / 2);
        computerGuessValueSpan.textContent = computerGuess; // Update immediately for animation
        displayGameMessage("...מחשב על המהלך הבא...", null); // Clear previous message

        enableFeedbackButtons(true);
        btnStart.disabled = true; // Disable start button while waiting for feedback

        // Add guess to history AFTER updating guessCount
        const historyItem = document.createElement('li');
        historyItem.textContent = `מהלך ${guessCount}: ניחשתי ${computerGuess}. הטווח היה [${minRange} - ${maxRange}]`; // Show range *before* update
        // Remove placeholder if it exists
        if (guessHistoryList.querySelector('.history-placeholder')) {
             guessHistoryList.innerHTML = '';
        }
        guessHistoryList.appendChild(historyItem);
        // Scroll to bottom with a slight delay to allow animation
        setTimeout(() => {
            guessHistoryList.scrollTop = guessHistoryList.scrollHeight;
        }, 100);
    }

    function handleFeedback(feedback) {
        if (!gameActive) return;

        const currentGuess = computerGuess; // Store guess before potential update

        if (feedback === 'too-low') {
            minRange = currentGuess + 1;
            updateRangeDisplay();
             if (minRange > maxRange) { // Check if range collapsed incorrectly
                 displayGameMessage(`חשבתי שזה ${currentGuess}, אבל אמרת שזה נמוך מדי. כעת הטווח ריק ([${minRange} - ${maxRange}]). האם המספר היה בטווח המקורי (1-100)?`, 'error');
                 endGame();
                 return;
            }
            makeComputerGuess();
        } else if (feedback === 'too-high') {
            maxRange = currentGuess - 1;
            updateRangeDisplay();
            if (minRange > maxRange) { // Check if range collapsed incorrectly
                 displayGameMessage(`חשבתי שזה ${currentGuess}, אבל אמרת שזה גבוה מדי. כעת הטווח ריק ([${minRange} - ${maxRange}]). האם המספר היה בטווח המקורי (1-100)?`, 'error');
                 endGame();
                 return;
            }
            makeComputerGuess();
        } else if (feedback === 'correct') {
            displayGameMessage(`מדהים! ניחשתי את המספר שלך: ${currentGuess}! לקח לי רק ${guessCount} מהלכים.`, 'success');
            endGame();
        }
    }

    function startGame() {
        minRange = 1;
        maxRange = 100;
        guessCount = 0;
        gameActive = true;
        guessHistoryList.innerHTML = '<li class="history-placeholder">...כאן תופיע היסטוריית המהלכים...</li>'; // Clear history and add placeholder
        gameMessagePara.textContent = ''; // Clear game message
        gameMessagePara.className = 'game-message'; // Reset message class
        guessCountValueSpan.textContent = '0'; // Reset count display
        guessCountDisplay.classList.remove('hidden'); // Show guess count display
        updateRangeDisplay(); // Display initial range
        btnStart.textContent = 'התחל אתגר חדש';
        makeComputerGuess();
    }

    function endGame() {
        gameActive = false;
        enableFeedbackButtons(false);
        btnStart.textContent = 'התחל אתגר חדש'; // Ensure button text is "new game"
        btnStart.disabled = false; // Re-enable start button at the end
    }

    function enableFeedbackButtons(enable) {
        btnTooLow.disabled = !enable;
        btnCorrect.disabled = !enable;
        btnTooHigh.disabled = !enable;
    }

    function displayGameMessage(message, type = null) {
        gameMessagePara.textContent = message;
        gameMessagePara.className = 'game-message'; // Reset class
        if (type) {
            gameMessagePara.classList.add(type); // Add success or error class for styling
        }
    }


    // Event Listeners
    btnStart.addEventListener('click', startGame);
    btnTooLow.addEventListener('click', () => handleFeedback('too-low'));
    btnCorrect.addEventListener('click', () => handleFeedback('correct'));
    btnTooHigh.addEventListener('click', () => handleFeedback('too-high'));

    toggleExplanationBtn.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (explanationDiv.classList.contains('hidden')) {
            toggleExplanationBtn.textContent = 'מה קרה כאן? (הצג הסבר)';
             // Scroll up smoothly when hiding explanation
             explanationDiv.style.animation = 'none'; // Disable fade-in animation when hiding
             window.scrollTo({ top: 0, behavior: 'smooth' });

        } else {
            toggleExplanationBtn.textContent = 'מה קרה כאן? (הסתר הסבר)';
            // Scroll to explanation section smoothly when showing it
            explanationDiv.style.animation = ''; // Re-enable fade-in animation
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial state setup
    function initialize() {
        updateRangeDisplay(); // Display initial range [1 - 100]
        enableFeedbackButtons(false); // Buttons disabled initially
        explanationDiv.classList.add('hidden'); // Ensure explanation is hidden on load
        toggleExplanationBtn.textContent = 'מה קרה כאן? (הצג הסבר)'; // Ensure button text is correct on load
        guessCountDisplay.classList.add('hidden'); // Hide guess count initially
        guessHistoryList.innerHTML = '<li class="history-placeholder">...כאן תופיע היסטוריית המהלכים...</li>'; // Add placeholder
    }

    // Run initialization when script loads
    initialize();


</script>