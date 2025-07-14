---
title: "אתגר זיכרון: מבחן טווח ספרות דיגיטלי"
english_slug: short-term-memory-digit-span-test
category: "מדעי החברה / פסיכולוגיה"
tags: [זיכרון, קוגניציה, מבחן, משחק]
---
# אתגר זיכרון: מבחן טווח ספרות דיגיטלי

חושבים שיש לכם זיכרון חד כמו סכין? בואו נבדוק! הזיכרון לטווח קצר הוא כמו שולחן העבודה של המוח שלנו - הוא מחזיק את המידע שאנחנו עובדים איתו ברגע נתון. אחד המבחנים הקלאסיים והמסקרנים לבדיקת "שולחן העבודה" הזה הוא מבחן "מוטת הספרות" (Digit Span). זה לא רק מבחן, זה אתגר כיפי למוח! נסו לשחק ולגלות מהו הטווח האישי שלכם.

<div id="memoryGameApp">
    <div class="game-container">
        <div id="controls">
            <div class="stat-item">
                <span>רמה:</span>
                <span id="levelDisplay">1</span>
            </div>
            <div class="stat-item">
                <span>ניקוד:</span>
                <span id="scoreDisplay">0</span>
            </div>
            <button id="startButton" class="game-button">התחל אתגר</button>
        </div>

        <div id="displayArea">
            <div id="instructionDisplay" class="instruction">זכור את הרצף...</div>
            <div id="sequenceDisplay" class="sequence-display">
                <!-- Digits will be added here -->
            </div>
            <div id="feedbackDisplay" class="feedback"></div>
        </div>

        <div id="inputArea" class="input-area" style="display: none;">
            <label for="userSequence">הקלד/י את הרצף:</label>
            <input type="text" id="userSequence" class="sequence-input" autocomplete="off" inputmode="numeric" pattern="[0-9]*">
            <button id="submitButton" class="game-button submit-button">שלח תשובה</button>
        </div>

        <div id="gameOverArea" class="game-over-area" style="display: none;">
            <h3>המשחק הסתיים!</h3>
            <p id="finalScoreDisplay"></p>
            <p id="finalSpanDisplay"></p>
            <button id="restartButton" class="game-button">שחק שוב</button>
        </div>
    </div>
    <!-- Sound effects -->
    <audio id="correctSound" src="https://www.soundjay.com/buttons/button-2.mp3" preload="auto"></audio>
    <audio id="incorrectSound" src="https://www.soundjay.com/buttons/button-3.mp3" preload="auto"></audio>

</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap'); /* Example: Using Rubik font */

    #memoryGameApp {
        font-family: 'Rubik', sans-serif;
        max-width: 600px;
        margin: 20px auto;
        padding: 25px;
        background: linear-gradient(145deg, #e0e0e0, #ffffff); /* Subtle gradient */
        border-radius: 15px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
        text-align: center;
        direction: rtl;
        color: #333;
        overflow: hidden; /* Clear floats/margins */
    }

    .game-container {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    #controls {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 25px;
        font-size: 1.1em;
        color: #555;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .stat-item {
        margin: 5px 10px; /* Add some margin */
        font-weight: 500;
    }

    .game-button {
        padding: 12px 25px;
        margin: 10px;
        border: none;
        border-radius: 30px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: 500;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        min-width: 120px; /* Ensure buttons have minimum width */
    }

    #startButton {
        background-color: #4CAF50; /* Green */
        color: white;
    }

    #startButton:hover {
        background-color: #45a049;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }

    #submitButton {
        background-color: #2196F3; /* Blue */
        color: white;
    }

    #submitButton:hover {
        background-color: #1e88e5;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }

     #restartButton {
        background-color: #ff9800; /* Orange */
        color: white;
    }

    #restartButton:hover {
        background-color: #fb8c00;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }


    .game-button:active {
        transform: scale(0.95);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    #displayArea {
        min-height: 120px; /* Increased height for sequence display */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
        position: relative; /* Needed for absolute positioning of children if desired */
    }

    .instruction {
        font-size: 1.3em;
        font-weight: 500;
        color: #666;
        margin-bottom: 15px;
        height: 1.3em; /* Reserve space */
        opacity: 0; /* Start hidden */
        animation: fadeIn 0.8s forwards;
    }


    .sequence-display {
        font-size: 2.5em; /* Larger digits */
        font-weight: 700;
        color: #000;
        min-height: 1.5em; /* Reserve space for digits */
        display: flex; /* Use flexbox for digit arrangement */
        justify-content: center;
        align-items: center;
        gap: 10px; /* Space between digits */
    }

    .digit {
        display: inline-flex; /* Use inline-flex */
        justify-content: center;
        align-items: center;
        width: 1.5em; /* Fixed width for consistent spacing */
        height: 1.5em; /* Fixed height */
        background-color: #e3f2fd; /* Light blue background for digits */
        border-radius: 8px; /* Rounded corners for digit boxes */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        opacity: 0; /* Start hidden */
        transform: scale(0.8); /* Start slightly smaller */
        animation: popIn 0.4s ease-out forwards; /* Pop-in animation */
    }

    /* Animation for sequential display */
    .sequence-display .digit:nth-child(1) { animation-delay: 0.1s; }
    .sequence-display .digit:nth-child(2) { animation-delay: 0.2s; }
    .sequence-display .digit:nth-child(3) { animation-delay: 0.3s; }
    .sequence-display .digit:nth-child(4) { animation-delay: 0.4s; }
    .sequence-display .digit:nth-child(5) { animation-delay: 0.5s; }
    .sequence-display .digit:nth-child(6) { animation-delay: 0.6s; }
    .sequence-display .digit:nth-child(7) { animation-delay: 0.7s; }
    .sequence-display .digit:nth-child(8) { animation-delay: 0.8s; }
    .sequence-display .digit:nth-child(9) { animation-delay: 0.9s; }
     /* Add more delays if span can exceed 9 */


    @keyframes popIn {
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    @keyframes fadeIn {
        to { opacity: 1; }
    }

    @keyframes fadeOut {
        to { opacity: 0; }
    }

    .hidden {
        visibility: hidden; /* Use visibility to maintain layout space */
    }

    .sequence-display.hiding .digit {
         animation: fadeOut 0.5s ease-out forwards !important; /* Override popIn */
    }


    .feedback {
        font-size: 1.4em; /* Slightly larger feedback */
        font-weight: 700; /* Bold feedback */
        min-height: 1.4em; /* Reserve space */
        margin-top: 15px;
    }

    .feedback.correct {
        color: #4CAF50; /* Green */
    }

    .feedback.incorrect {
        color: #F44336; /* Red */
    }

     .feedback.info {
        color: #2196F3; /* Blue */
        font-weight: normal;
        font-size: 1.2em;
    }

    .input-area {
        display: flex;
        flex-direction: column; /* Stack label and input */
        align-items: center;
        gap: 15px; /* Space between elements */
    }

    .input-area label {
        font-size: 1.1em;
        color: #555;
    }

    .sequence-input {
        padding: 10px 15px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1.4em; /* Larger input font */
        text-align: center;
        width: 100%; /* Make input responsive */
        max-width: 200px; /* Max width for input */
        box-sizing: border-box; /* Include padding and border in element's total width */
    }

    .game-over-area {
        padding: 20px;
        background-color: #fff9c4; /* Light yellow background */
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .game-over-area h3 {
        color: #f57c00; /* Darker orange */
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.8em;
    }

    .game-over-area p {
        font-size: 1.2em;
        color: #555;
        margin-bottom: 15px;
    }


    #explanationToggle {
        display: block;
        margin: 30px auto 20px auto; /* More margin */
        padding: 12px 25px;
        border: none;
        border-radius: 30px; /* Pill shape */
        background-color: #ff9800; /* Orange */
        color: white;
        font-size: 1.1em;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #explanationToggle:hover {
        background-color: #fb8c00;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }

     #explanationToggle:active {
        transform: scale(0.95);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }


    #explanation {
        max-width: 600px;
        margin: 20px auto;
        padding: 25px;
        background-color: #eef; /* Light blue background */
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        direction: rtl;
        text-align: right;
        border-left: 5px solid #2196F3; /* Accent border */
    }

    #explanation h3 {
        color: #1e88e5; /* Darker blue */
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.6em;
    }

    #explanation p {
        font-size: 1em;
        line-height: 1.6;
        color: #444;
        margin-bottom: 1em;
    }
</style>

<button id="explanationToggle">מה זה בעצם מבחן טווח ספרות?</button>

<div id="explanation" style="display: none;">
    <h3>מהו מבחן טווח ספרות (Digit Span)?</h3>
    <p>זהו כלי קוגניטיבי פסיכולוגי קלאסי שנועד למדוד את הקיבולת של הזיכרון לטווח קצר או הזיכרון הפעיל שלכם. הוא מופיע לעיתים קרובות במבחני אינטליגנציה וזיכרון חשובים. הרעיון פשוט: בודקים כמה פריטים (במקרה שלנו, ספרות) אתם מסוגלים לשנן ולשחזר ברצף המדויק, אחרי שראיתם או שמעתם אותם רק פעם אחת קצרה.</p>

    <h3>איך זה עובד במשחק הזה?</h3>
    <p>בגרסתו הבסיסית, המשחק מציג לכם רצף של ספרות. אתם צריכים לקלוט אותו במהירות ואז להקליד אותו בדיוק כפי שהוצג. בכל שלב שתצליחו, הרצף הבא יהיה ארוך יותר. ה"טווח" שלכם הוא האורך המקסימלי של הרצף שהצלחתם לשחזר נכונה לפני שטעות אחת הספיקה...</p>

    <h3>מה התוצאה אומרת?</h3>
    <p>בעבר, המספר הממוצע נחשב ל"מספר הקסם" של 7 ± 2 פריטים. מחקרים מודרניים מצביעים על כך שהקיבולת האמיתית עשויה להיות מעט נמוכה יותר עבור פריטים מורכבים יותר מספרות בודדות. בכל מקרה, מבחן טווח הספרות נותן לכם אינדיקציה טובה ליכולת של המוח שלכם להחזיק ולטפל במידע זמני. זה לא בהכרח משקף את האינטליגנציה הכוללת, אלא היבט ספציפי של הזיכרון.</p>

    <h3>אפשר לשפר?</h3>
    <p>קיבולת הזיכרון הבסיסית די יציבה, אבל אפשר לשפר את הביצועים במבחנים כאלה על ידי שימוש בטכניקות כמו "קיבוץ" (Chunking) - ארגון הספרות ליחידות משמעותיות יותר (למשל, לזכור "שנת 1948" במקום "אחת, תשע, ארבע, שמונה"). עם זאת, המשחק הזה נועד בעיקר לאתגר את הקיבולת הבסיסית שלכם בצורה מהנה.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const startButton = document.getElementById('startButton');
        const submitButton = document.getElementById('submitButton');
        const restartButton = document.getElementById('restartButton');
        const sequenceDisplay = document.getElementById('sequenceDisplay');
        const feedbackDisplay = document.getElementById('feedbackDisplay');
        const instructionDisplay = document.getElementById('instructionDisplay');
        const inputArea = document.getElementById('inputArea');
        const userSequenceInput = document.getElementById('userSequence');
        const levelDisplay = document.getElementById('levelDisplay');
        const scoreDisplay = document.getElementById('scoreDisplay');
        const explanationToggle = document.getElementById('explanationToggle');
        const explanationDiv = document.getElementById('explanation');
        const gameOverArea = document.getElementById('gameOverArea');
        const finalScoreDisplay = document.getElementById('finalScoreDisplay');
        const finalSpanDisplay = document.getElementById('finalSpanDisplay');
        const correctSound = document.getElementById('correctSound');
        const incorrectSound = document.getElementById('incorrectSound');

        let currentSequence = [];
        let level = 1;
        let score = 0;
        const initialSpan = 4; // Start with a slightly higher span for more challenge (e.g., 4 or 5)
        let gameActive = false;

        function playSound(soundElement) {
            if (soundElement) {
                soundElement.currentTime = 0; // Rewind to start
                soundElement.play().catch(e => console.error("Error playing sound:", e)); // Catch potential errors
            }
        }

        function generateSequence(length) {
            const sequence = [];
            for (let i = 0; i < length; i++) {
                sequence.push(Math.floor(Math.random() * 10)); // Digits 0-9
            }
            return sequence;
        }

        async function displaySequence(sequence) {
            gameActive = false; // Disable input during display
            sequenceDisplay.innerHTML = ''; // Clear previous display
            sequenceDisplay.classList.remove('hidden', 'hiding');
            feedbackDisplay.textContent = ''; // Clear feedback
            feedbackDisplay.className = 'feedback'; // Reset class
            instructionDisplay.textContent = 'זכור את הרצף:';
            instructionDisplay.style.opacity = 1; // Ensure instruction is visible

            // Add digits with animation delay
            for (let i = 0; i < sequence.length; i++) {
                const digitSpan = document.createElement('span');
                digitSpan.textContent = sequence[i];
                digitSpan.classList.add('digit');
                // Apply delay inline or use CSS nth-child, CSS is cleaner
                // digitSpan.style.animationDelay = `${i * 0.2}s`; // Alternative inline delay
                sequenceDisplay.appendChild(digitSpan);
            }

            // Wait for digits to appear and briefly stay visible
            await new Promise(resolve => setTimeout(resolve, sequence.length * 400 + 1500)); // Wait longer for longer sequences + display time

            // Start hiding animation
            sequenceDisplay.classList.add('hiding');
            instructionDisplay.style.animation = 'fadeOut 0.5s forwards'; // Fade out instruction

            await new Promise(resolve => setTimeout(resolve, 600)); // Wait for hide animation

            sequenceDisplay.classList.add('hidden'); // Fully hide after animation
            instructionDisplay.style.opacity = 0; // Ensure hidden after animation

            inputArea.style.display = 'flex'; // Show input field
            userSequenceInput.value = ''; // Clear input
            userSequenceInput.focus(); // Focus the input
            gameActive = true; // Re-enable input
        }

        function startGame() {
            gameOverArea.style.display = 'none'; // Hide game over screen
            startButton.style.display = 'none'; // Hide start button
            level = 1;
            score = 0;
            updateDisplay();
            nextLevel(); // Start the first level
        }

        function updateDisplay() {
             levelDisplay.textContent = initialSpan + (level - 1); // Display actual span length
             scoreDisplay.textContent = score;
        }

        function nextLevel() {
            const currentSpan = initialSpan + (level - 1);
            currentSequence = generateSequence(currentSpan);
            displaySequence(currentSequence);
        }

        function checkSequence() {
             if (!gameActive) return; // Prevent multiple submissions

            const userAnswerString = userSequenceInput.value.trim();
            const correctAnswerString = currentSequence.join('');

            inputArea.style.display = 'none'; // Hide input area after submission

            if (userAnswerString === correctAnswerString) {
                playSound(correctSound);
                feedbackDisplay.textContent = 'נכון מאוד!';
                feedbackDisplay.className = 'feedback correct';
                score += currentSequence.length; // Award points based on length
                level++;
                updateDisplay();
                instructionDisplay.style.animation = 'fadeIn 0.5s forwards';
                instructionDisplay.textContent = 'התכונן/י לרצף הבא...';
                instructionDisplay.style.opacity = 1;


                setTimeout(() => {
                     instructionDisplay.style.animation = 'fadeOut 0.5s forwards';
                     setTimeout(nextLevel, 600); // Wait for instruction fade out
                }, 1500);

            } else {
                playSound(incorrectSound);
                feedbackDisplay.textContent = `שגוי! הרצף הנכון היה: ${correctAnswerString}`;
                feedbackDisplay.className = 'feedback incorrect';

                instructionDisplay.style.animation = 'fadeIn 0.5s forwards';
                instructionDisplay.textContent = 'המשחק הסתיים.';
                instructionDisplay.style.opacity = 1;

                setTimeout(gameOver, 2000); // Wait before showing game over screen
            }
             gameActive = false; // Disable input until next round or game over
        }

        function gameOver() {
            sequenceDisplay.classList.add('hidden');
            instructionDisplay.style.opacity = 0;
            inputArea.style.display = 'none';
            gameOverArea.style.display = 'block';
            finalScoreDisplay.textContent = `ניקוד סופי: ${score}`;
            // The last *successful* span was level - 1. If they failed on level 1, their span is 0 or initialSpan-1 depending how you define it.
            // Let's define span as the highest length successfully recalled.
            const maxSpan = (level > 1) ? initialSpan + (level - 2) : 0;
             finalSpanDisplay.textContent = `הטווח הגבוה ביותר שלך היה: ${maxSpan}`;
            // Note: if level 1 (span initialSpan) is failed, maxSpan is 0 by this logic.
            // Maybe better: max span is initialSpan + (level - 2) if level > 1, else it's "לא הושג טווח".
             const displayedMaxSpan = (level > 1) ? initialSpan + (level - 2) : initialSpan -1; // If failed level 1 (span 4), max span is 3. If passed level 1 (span 4) and failed level 2 (span 5), max span is 4.
             finalSpanDisplay.textContent = `הטווח הגבוה ביותר שהצלחת לזכור: ${displayedMaxSpan}`;

        }

        // Event Listeners
        startButton.addEventListener('click', startGame);
        restartButton.addEventListener('click', startGame); // Restart button uses startGame logic
        submitButton.addEventListener('click', checkSequence);

        userSequenceInput.addEventListener('keypress', (event) => {
            // Allow only digits and handle Enter key for submission
            if (event.key === 'Enter') {
                event.preventDefault(); // Prevent default form submission
                checkSequence();
            } else if (!/\d/.test(event.key)) {
                event.preventDefault(); // Prevent non-digit input
            }
        });

         // Prevent pasting non-digits
         userSequenceInput.addEventListener('paste', (event) => {
             const pasteData = event.clipboardData.getData('text');
             if (/\D/.test(pasteData)) { // Check if pasted data contains non-digits
                 event.preventDefault();
             }
         });


        explanationToggle.addEventListener('click', () => {
            if (explanationDiv.style.display === 'none') {
                explanationDiv.style.display = 'block';
                explanationToggle.textContent = 'הסתר הסבר';
            } else {
                explanationDiv.style.display = 'none';
                explanationToggle.textContent = 'מה זה בעצם מבחן טווח ספרות?';
            }
        });

        // Initial state setup
        updateDisplay(); // Show initial level and score
        gameOverArea.style.display = 'none'; // Ensure game over is hidden initially
        instructionDisplay.style.opacity = 0; // Hide instruction initially
    });
</script>