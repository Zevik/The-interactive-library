---
title: "אתגר המוח: מבחן סטרופ הקלאסי"
english_slug: stroop-test-color-naming
category: "פסיכולוגיה ניסויית"
tags: ["מבחן סטרופ", "קשב", "עיבוד מידע", "הסחות קשב", "פסיכולוגיה קוגניטיבית", "אתגר מוחי"]
---
# אתגר המוח: מבחן סטרופ הקלאסי

מוכנים לאתגר את המוח שלכם? במבחן הפשוט אך המפתיע הזה, תגלו כמה קשה יכול להיות לפעמים להתעלם ממה שאנחנו רגילים לעשות באופן אוטומטי. המשימה פשוטה: אמרו בקול (או לחצו על הכפתור המתאים) את **צבע הדיו** שבו כתובה המילה, והתעלמו לגמרי ממה שהמילה *אומרת*. נשמע קל? בואו נראה!

<div id="stroop-app">
    <div id="intro-screen">
        <p>לחצו על 'התחל' כדי להתחיל את האתגר. תתבקשו לזהות את צבע המילה שמופיעה על המסך. נסו להגיב הכי מהר ומדויק שאתם יכולים!</p>
        <button id="start-button">התחל את האתגר!</button>
    </div>
    <div id="game-screen" style="display: none;">
        <div id="stats">
            <span id="score-display">ניקוד: 0</span> | <span id="trial-counter">משימה: 0/10</span>
        </div>
        <div id="word-display"></div>
        <div id="color-buttons">
            <button data-color="red">אדום</button>
            <button data-color="blue">כחול</button>
            <button data-color="green">ירוק</button>
            <button data-color="yellow">צהוב</button>
        </div>
        <div id="feedback"></div>
        <div id="timer-display">זמן תגובה: -- סמ</div>
    </div>
     <div id="results-screen" style="display: none;">
        <h2>סיימתם את האתגר!</h2>
        <p id="final-score-text"></p>
        <p id="average-time-text"></p>
        <button id="restart-button">לנסות שוב?</button>
    </div>
</div>

<button id="show-explanation-button">לגלות מה קרה? הצג הסבר מדעי</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: הכירו את אפקט סטרופ</h2>
    מה הרגשתם כשניסיתם לענות? אם הרגשתם קונפליקט או איטיות מסוימת, אתם לא לבד! חוויתם את **אפקט סטרופ (Stroop Effect)**, תופעה קלאסית בפסיכולוגיה ניסויית שמדגימה כיצד המוח שלנו מתמודד (ולפעמים מתקשה) עם מידע מתחרה. במשימה שביצעתם, היה קונפליקט בין שתי פיסות מידע: המשמעות של המילה הכתובה (תהליך אוטומטי עבור קוראים מנוסים) וצבע הדיו שלה (תהליך פחות אוטומטי ומבוקר).

    <h3>למה המשימה הזו מאתגרת?</h3>
    <p>קריאת מילים היא מיומנות שרכשנו ואוטמטית מאוד. המוח שלנו "מקודד" את משמעות המילה כמעט מיד, עוד לפני שהספקנו לעבד את צבע הדיו. כשהמילה וצבע הדיו אינם תואמים (למשל, המילה "אדום" כתובה בדיו כחול), המידע האוטומטי (הקריאה) מפריע למשימה המבוקרת שנדרשת מכם (זיהוי וקריאת צבע הדיו). המוח צריך להתאמץ כדי לדכא את התגובה האוטומטית ולהתמקד במשימה הנכונה.</p>

    <h3>מה אפשר ללמוד מאפקט סטרופ?</h3>
    אפקט זה הוא חלון הצצה מרתק לאופן שבו המוח שלנו מעבד מידע:
    <ul>
        <li>**אוטומטי מול מבוקר:** הוא מדגים את ההבדל בין תהליכים קוגניטיביים מהירים ואוטומטיים לבין תהליכים איטיים ומבוקרים הדורשים מאמץ.</li>
        <li>**קשב סלקטיבי:** קשה לנו "לכבות" או להתעלם לחלוטין ממידע מסוים כשאנחנו מנסים למקד את הקשב במידע אחר, במיוחד כשהמידע המתחרה אוטומטי וחזק.</li>
        <li>**בקרה קוגניטיבית:** האפקט ממחיש את הצורך במשאבים קוגניטיביים (כמו קשב ובקרה מעכבת) כדי לנהל קונפליקטים קוגניטיביים ולבחור את התגובה הנכונה.</li>
    </ul>
    מבחן סטרופ הוא כלי בסיסי בחקר הקשב, הזיכרון העבודה, והתפקודים הניהוליים של המוח, והבנתו עוזרת לנו להבין טוב יותר קשיים בלמידה ובהפרעות קשב.
</div>

<style>
    body {
        font-family: 'Heebo', sans-serif; /* או גופן עברי מודרני אחר */
        display: flex;
        flex-direction: column;
        align-items: center;
        background: linear-gradient(to bottom, #e0f2f7, #b3e5fc); /* רקע נעים */
        padding: 20px;
        direction: rtl; /* עברית */
        text-align: center;
        min-height: 100vh;
        margin: 0;
    }

    h1 {
        color: #0277bd; /* כחול עמוק */
        margin-bottom: 30px;
        font-size: 2.5em;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }

    #stroop-app {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        width: 95%;
        max-width: 550px;
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 400px; /* גובה מינימלי לשמירת יציבות פריסה */
        justify-content: center;
        position: relative; /* למיקום אלמנטים בתוך הקונטיינר */
        overflow: hidden; /* לחיתוך אנימציות שיוצאות מגבולות */
    }

    #intro-screen, #game-screen, #results-screen {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%; /* ימלא את גובה הקונטיינר */
        position: absolute; /* למיקום מוחלט בתוך stroop-app */
        top: 0;
        left: 0;
        padding: 30px; /* פדינג פנימי למסכים */
        box-sizing: border-box; /* כלול פדינג בגודל */
    }

    #intro-screen p, #results-screen p {
        font-size: 1.2em;
        color: #333;
        margin-bottom: 20px;
        line-height: 1.5;
    }

    #start-button, #restart-button {
        padding: 15px 30px;
        font-size: 1.3em;
        background-color: #00bcd4; /* טורקיז חי */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    #start-button:hover, #restart-button:hover {
        background-color: #00acc1; /* טורקיז מעט כהה יותר */
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.25);
    }
    #start-button:active, #restart-button:active {
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }


    #stats {
        position: absolute;
        top: 20px;
        left: 20px;
        right: 20px;
        display: flex;
        justify-content: space-between;
        font-size: 1em;
        color: #555;
        width: calc(100% - 40px);
    }
    #trial-counter {
         position: absolute;
         left: 20px; /* בצד שמאל בעברית */
         top: 20px;
    }
    #score-display {
         position: absolute;
         right: 20px; /* בצד ימין בעברית */
         top: 20px;
    }


    #word-display {
        font-size: 5em; /* גודל גדול יותר */
        font-weight: bold;
        margin-bottom: 40px;
        min-height: 1.8em; /* שמירת מקום */
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%; /* וודא שהמילה ממורכזת */
        transition: color 0.3s ease-in-out, transform 0.2s ease-out; /* אנימציה צבע ושינוי גודל/מיקום */
    }

    /* אנימציות ל-word-display */
    @keyframes correct-pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; } /* יחזור לגודל רגיל וקצת ידהה לפני המשימה הבאה */
    }
    @keyframes incorrect-shake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-10px); }
        40%, 80% { transform: translateX(10px); }
    }

    #word-display.correct {
        animation: correct-pulse 0.6s ease-out forwards; /* forwards ישמור על המצב הסופי של האנימציה */
        opacity: 0.8; /* ידהה קצת בסוף אנימציה */
    }
    #word-display.incorrect {
        animation: incorrect-shake 0.5s ease-out;
    }


    #color-buttons {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); /* התאמה לגודל מסך */
        gap: 15px;
        width: 100%;
        max-width: 350px; /* רוחב מקסימלי לכפתורים */
        margin-top: 20px;
        margin-bottom: 20px;
    }

    #color-buttons button {
        padding: 18px 25px; /* פדינג גדול יותר */
        font-size: 1.2em;
        font-weight: bold;
        border: none;
        border-radius: 10px; /* פינות עגולות יותר */
        cursor: pointer;
        transition: all 0.2s ease; /* מעבר חלק יותר */
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
    }

    #color-buttons button[data-color="red"] { background-color: #e74c3c; }
    #color-buttons button[data-color="blue"] { background-color: #3498db; }
    #color-buttons button[data-color="green"] { background-color: #2ecc71; }
    #color-buttons button[data-color="yellow"] { background-color: #f1c40f; }

     /* הוספת גרדיאנטים וריחוף קל */
    #color-buttons button[data-color="red"] { background: linear-gradient(to bottom right, #e74c3c, #c0392b); }
    #color-buttons button[data-color="blue"] { background: linear-gradient(to bottom right, #3498db, #2980b9); }
    #color-buttons button[data-color="green"] { background: linear-gradient(to bottom right, #2ecc71, #27ae60); }
    #color-buttons button[data-color="yellow"] { background: linear-gradient(to bottom right, #f1c40f, #f39c12); color: #333; text-shadow: none;} /* צהוב עם טקסט כהה */


    #color-buttons button:hover:not(:disabled) {
        opacity: 0.95;
        transform: translateY(-3px); /* ריחוף קל */
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }

    #color-buttons button:active:not(:disabled) {
        transform: scale(0.95);
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
     #color-buttons button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
     }


    #feedback {
        margin-top: 15px; /* מרווח קטן יותר */
        font-size: 1.1em;
        font-weight: bold;
        min-height: 1.2em; /* שמירת מקום */
        color: #555;
        opacity: 0; /* התחלה שקופה */
        transition: opacity 0.3s ease-in-out; /* אנימציית הופעה */
    }
    #feedback.visible {
         opacity: 1;
    }

    #feedback.correct {
        color: #2ecc71; /* ירוק */
    }

    #feedback.incorrect {
        color: #e74c3c; /* אדום */
    }

    #timer-display {
        margin-top: 10px;
        font-size: 0.9em;
        color: #777;
        min-height: 1em;
    }

    #results-screen h2 {
        color: #0277bd;
        margin-bottom: 15px;
    }
     #results-screen p {
        font-size: 1.2em;
        color: #333;
        margin-bottom: 10px;
     }


    #show-explanation-button {
        padding: 12px 25px;
        font-size: 1em;
        background-color: #555;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    #show-explanation-button:hover {
        background-color: #777;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
     #show-explanation-button:active {
        transform: scale(0.98);
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
     }


    #explanation {
        margin-top: 30px;
        padding: 25px;
        background-color: #e9e9e9;
        border-radius: 10px;
        text-align: justify;
        max-width: 700px;
        line-height: 1.6;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: all 0.4s ease-in-out; /* אנימציה להופעה/הסתרה */
        opacity: 0; /* התחלה מוסתרת */
        max-height: 0; /* התחלה מוסתרת */
        overflow: hidden; /* חתוך תוכן מוסתר */
        transform: translateY(20px); /* התחלה מעט למטה */
    }
     #explanation.visible {
         opacity: 1;
         max-height: 1000px; /* ערך גדול מספיק להכיל את התוכן */
         transform: translateY(0); /* חזרה למיקום רגיל */
     }


    #explanation h2, #explanation h3 {
        color: #0277bd;
        text-align: center;
        margin-bottom: 15px;
    }

    #explanation ul {
        margin-top: 15px;
        padding-right: 20px;
        list-style: disc;
    }

    #explanation li {
        margin-bottom: 10px;
    }

     /* רספונסיביות בסיסית */
    @media (max-width: 600px) {
        h1 { font-size: 2em; margin-bottom: 20px; }
        #stroop-app { padding: 20px; min-height: 350px; }
        #intro-screen, #game-screen, #results-screen { padding: 20px; }
        #word-display { font-size: 4em; margin-bottom: 30px; }
        #color-buttons { grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 10px; max-width: 300px; }
        #color-buttons button { padding: 15px 20px; font-size: 1.1em; }
        #explanation { padding: 20px; }
        #explanation h2, #explanation h3 { font-size: 1.2em; }
    }

</style>

<script>
    const introScreen = document.getElementById('intro-screen');
    const gameScreen = document.getElementById('game-screen');
    const resultsScreen = document.getElementById('results-screen');
    const startButton = document.getElementById('start-button');
    const restartButton = document.getElementById('restart-button');

    const scoreDisplay = document.getElementById('score-display');
    const trialCounterDisplay = document.getElementById('trial-counter');
    const wordDisplay = document.getElementById('word-display');
    const colorButtons = document.getElementById('color-buttons');
    const feedback = document.getElementById('feedback');
    const timerDisplay = document.getElementById('timer-display');
    const finalScoreText = document.getElementById('final-score-text');
    const averageTimeText = document.getElementById('average-time-text');


    const showExplanationButton = document.getElementById('show-explanation-button');
    const explanationDiv = document.getElementById('explanation');

    const colors = [
        { name: 'אדום', value: 'red' },
        { name: 'כחול', value: 'blue' },
        { name: 'ירוק', value: 'green' },
        { name: 'צהוב', value: 'yellow' }
    ];
    const totalTrials = 10; // Define total number of trials

    let currentTrial = {};
    let gameActive = false;
    let score = 0;
    let trialCount = 0;
    let startTime = 0;
    let reactionTimes = [];

    // --- Game State Management ---
    function showScreen(screenId) {
        introScreen.style.display = 'none';
        gameScreen.style.display = 'none';
        resultsScreen.style.display = 'none';

        document.getElementById(screenId).style.display = 'flex';
    }

    function startGame() {
        score = 0;
        trialCount = 0;
        reactionTimes = [];
        scoreDisplay.textContent = `ניקוד: ${score}`;
        trialCounterDisplay.textContent = `משימה: ${trialCount}/${totalTrials}`;
        feedback.textContent = '';
        feedback.className = 'feedback'; // Reset feedback classes
        timerDisplay.textContent = 'זמן תגובה: -- סמ';

        showScreen('game-screen');
        setTimeout(nextTrial, 500); // Short delay before first trial
    }

    function endGame() {
        gameActive = false;
        showScreen('results-screen');

        const averageTime = reactionTimes.length > 0 ? reactionTimes.reduce((a, b) => a + b, 0) / reactionTimes.length : 0;
        finalScoreText.textContent = `הניקוד הסופי שלך: ${score} מתוך ${totalTrials}`;
        averageTimeText.textContent = `זמן תגובה ממוצע: ${averageTime.toFixed(2)} סמ`;

        // Reset word display and feedback after game ends
        wordDisplay.textContent = '';
        wordDisplay.style.color = '#333'; // Default color
        wordDisplay.className = ''; // Remove animation classes
        feedback.textContent = '';
        feedback.className = 'feedback';
        timerDisplay.textContent = '';
    }


    // --- Trial Logic ---
    function getRandomInt(max) {
        return Math.floor(Math.random() * max);
    }

    function nextTrial() {
        if (trialCount >= totalTrials) {
            endGame();
            return;
        }

        gameActive = true;
        trialCount++;
        trialCounterDisplay.textContent = `משימה: ${trialCount}/${totalTrials}`;
        feedback.textContent = ''; // Clear feedback
        feedback.className = 'feedback'; // Remove correct/incorrect/visible classes
        timerDisplay.textContent = 'זמן תגובה: -- סמ';
        wordDisplay.className = ''; // Remove animation classes from previous trial

        // Randomly select a word and an ink color
        const textWord = colors[getRandomInt(colors.length)];
        const inkColor = colors[getRandomInt(colors.length)];

        currentTrial = {
            text: textWord.name,
            color: inkColor.value,
            correctAnswer: inkColor.value // The correct answer is the ink color value
        };

        // Update display
        wordDisplay.textContent = currentTrial.text;
        wordDisplay.style.color = currentTrial.color;

        // Enable buttons and reset their style
        Array.from(colorButtons.children).forEach(button => {
            button.disabled = false;
            button.style.opacity = 1;
            button.style.transform = 'none'; // Reset potential scale/translate from active state
        });

        startTime = performance.now(); // Start timing
    }

    function handleButtonClick(event) {
        if (!gameActive) return;

        const endTime = performance.now();
        const reactionTime = (endTime - startTime) / 1000; // Time in seconds
        reactionTimes.push(reactionTime);

        const selectedColor = event.target.getAttribute('data-color');
        gameActive = false; // Disable buttons after selection

        // Disable all buttons immediately and dim
        Array.from(colorButtons.children).forEach(button => {
             button.disabled = true;
             button.style.opacity = 0.7;
        });

        // Provide feedback
        let isCorrect = false;
        if (selectedColor === currentTrial.correctAnswer) {
            feedback.textContent = 'נכון!';
            feedback.className = 'feedback visible correct';
            score++;
            scoreDisplay.textContent = `ניקוד: ${score}`;
            wordDisplay.className = 'correct'; // Trigger correct animation
            isCorrect = true;
        } else {
            const correctAnswerName = colors.find(c => c.value === currentTrial.correctAnswer).name;
            feedback.textContent = `שגוי. צבע הדיו היה: ${correctAnswerName}`;
             feedback.className = 'feedback visible incorrect';
             wordDisplay.className = 'incorrect'; // Trigger incorrect animation
        }

        timerDisplay.textContent = `זמן תגובה: ${reactionTime.toFixed(2)} סמ`;


        // Move to next trial after a delay and clear animations
        setTimeout(() => {
             wordDisplay.className = ''; // Clear animation classes
             if (trialCount < totalTrials) {
                 nextTrial();
             } else {
                 endGame();
             }
        }, 1500); // Delay before next trial/end game
    }

    // --- Event Listeners ---
    startButton.addEventListener('click', startGame);
    restartButton.addEventListener('click', startGame); // Restart calls startGame

    Array.from(colorButtons.children).forEach(button => {
        button.addEventListener('click', handleButtonClick);
    });

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.maxHeight === '0px' || explanationDiv.style.maxHeight === '';
        explanationDiv.classList.toggle('visible', isHidden);
        showExplanationButton.textContent = isHidden ? 'הסתר הסבר מדעי' : 'לגלות מה קרה? הצג הסבר מדעי';
    });


    // --- Initialization ---
    document.addEventListener('DOMContentLoaded', () => {
        showScreen('intro-screen');
        // Ensure explanation starts hidden
        explanationDiv.style.maxHeight = '0';
        explanationDiv.style.opacity = '0';
        explanationDiv.style.transform = 'translateY(20px)';
    });


</script>