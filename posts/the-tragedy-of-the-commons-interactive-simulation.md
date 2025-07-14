---
title: "המאגר המתדלדל: סימולציה אינטראקטיבית של הטרגדייה של המאגר המשותף"
english_slug: the-tragedy-of-the-commons-interactive-simulation
category: "מדעי החברה / כלכלה התנהגותית"
tags:
  - טרגדיית המאגר המשותף
  - ניהול משאבים
  - תורת המשחקים
  - משחקים שיתופיים
  - ניהול משאבים משותפים
---
<h1>המאגר המתדלדל: סימולציה אינטראקטיבית של הטרגדייה של המאגר המשותף</h1>

דמיינו משאב יקר - אגם מלא דגים, יער עשיר בפירות, אוויר צלול לנשימה. מה קורה כשכולם מנסים להפיק ממנו את המקסימום, בלי לחשוב על מחר? הסימולציה הזו מזמינה אתכם לחוות ממקור ראשון את "הטרגדייה של המאגר המשותף" - תופעה כלכלית והתנהגותית בה אינטרס אישי רציונלי של כל פרט מוביל, באופן פרדוקסלי, לקריסה של המשאב שמשרת את כולם. האם תצליחו לנווט בין הפיתוי לרווח מיידי לצורך בשמירה על המשאב לטווח ארוך?

<div id="simulation-app">
    <h2>מצב המאגר</h2>
    <div class="pool-container">
        <div id="visual-pool">
            <div id="pool-fill"></div>
        </div>
        <div class="pool-status-text">
             <p><strong>גודל המאגר:</strong> <span id="pool-size"></span> יחידות</p>
        </div>
    </div>


    <div id="game-status" class="game-section">
        <p><strong>סיבוב:</strong> <span id="current-round">1</span> מתוך <span id="max-rounds"></span></p>
        <p><strong>הרווח הכולל שלך:</strong> <span id="total-profit">0</span> יחידות</p>
    </div>

    <div id="player-action" class="game-section">
        <label for="take-amount">כמה יחידות תרצה לקחת בסיבוב זה?</label>
        <div class="input-group">
             <input type="number" id="take-amount" min="0" value="0">
             <button id="take-button">קח מהמאגר</button>
        </div>
         <p class="help-text">זכור: כל יחידה שלוקחים הופכת לרווח אישי בסיבוב זה.</p>
    </div>

    <div id="round-results" class="game-section" style="display: none;">
        <h3>תוצאות הסיבוב <span id="previous-round-number"></span>:</h3>
        <p><strong>מהלך שלך:</strong> לקחת <span id="player-take"></span> יחידות. הרווח שלך בסיבוב זה: <span id="round-profit"></span> יחידות.</p>
        <p><strong>מהלך האחרים:</strong> השחקנים האחרים לקחו בסך הכל <span id="others-take"></span> יחידות.</p>
        <p><strong>מצב המאגר:</strong></p>
        <ul>
            <li>לאחר הלקיחה: <span id="pool-after-take"></span> יחידות</li>
            <li>לאחר ההתחדשות: <span id="pool-after-regeneration"></span> יחידות</li>
        </ul>
    </div>

    <div id="game-message" class="game-section" style="display: none;">
        <h3 id="message-title"></h3>
        <p id="message-text"></p>
        <button id="restart-button" class="button">התחל סימולציה מחדש</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #28a745;
        --warning-color: #ffc107;
        --danger-color: #dc3545;
        --info-color: #17a2b8;
        --bg-light: #f8f9fa;
        --text-dark: #343a40;
        --border-color: #dee2e6;
        --font-family: 'Arial', sans-serif;
    }

    #simulation-app {
        direction: rtl;
        text-align: right;
        font-family: var(--font-family);
        border: 1px solid var(--border-color);
        padding: 25px;
        margin: 25px auto;
        background-color: var(--bg-light);
        border-radius: 12px;
        max-width: 700px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* For visual effects */
        position: relative;
    }

    #simulation-app h1, #simulation-app h2, #simulation-app h3 {
        text-align: center;
        color: var(--text-dark);
        margin-bottom: 20px;
    }
     h1 { /* Specific style for the main h1 outside the app */
        text-align: center;
        font-family: var(--font-family);
        color: var(--text-dark);
        margin-bottom: 20px;
     }
     p {
         font-family: var(--font-family);
         color: var(--text-dark);
         line-height: 1.6;
     }


    .game-section {
        margin-bottom: 20px;
        padding: 15px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    #game-status p, #round-results p, #round-results ul, #game-message p {
        margin: 8px 0;
    }
     #round-results ul {
         list-style: none;
         padding: 0;
         margin-top: 10px;
     }
      #round-results ul li {
          margin-bottom: 5px;
      }


    #player-action .input-group {
        display: flex;
        align-items: center;
        gap: 10px; /* Space between input and button */
    }

    #player-action input[type="number"] {
        padding: 10px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        width: 100px;
        font-size: 1em;
        text-align: center;
        flex-shrink: 0; /* Prevent shrinking */
    }
    #player-action label {
        display: block;
        margin-bottom: 10px;
        font-weight: bold;
    }

    .button {
        padding: 10px 20px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease;
        flex-grow: 1; /* Allow button to grow */
        text-align: center;
    }
     .button:hover {
        background-color: #0056b3;
    }
     #restart-button {
        display: block; /* Center the button */
        margin: 20px auto 0 auto;
        background-color: var(--secondary-color);
     }
      #restart-button:hover {
        background-color: #218838;
      }


    #game-message {
        text-align: center;
        border-color: var(--danger-color);
        background-color: #ffe3e6; /* Light red background */
    }
     #game-message h3 {
        color: var(--danger-color);
        margin-top: 0;
     }
    #game-message.win {
        border-color: var(--secondary-color);
        background-color: #d4edda; /* Light green background */
    }
     #game-message.win h3 {
         color: var(--secondary-color);
     }
      #game-message.info {
        border-color: var(--info-color);
        background-color: #d9edf7; /* Light blue background */
      }
      #game-message.info h3 {
         color: var(--info-color);
      }

     .help-text {
         font-size: 0.9em;
         color: #6c757d;
         margin-top: 8px;
     }

    /* Visual Pool Styles */
    .pool-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 25px;
        gap: 20px;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    #visual-pool {
        width: 150px;
        height: 150px;
        border: 5px solid var(--primary-color);
        border-radius: 50%; /* Make it a circle */
        position: relative;
        overflow: hidden; /* Hide overflow of fill */
        background-color: #e9ecef; /* Empty state background */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
        flex-shrink: 0; /* Prevent shrinking */
    }

    #pool-fill {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 0%; /* Starts empty */
        background-color: var(--info-color); /* Water color */
        transition: height 0.5s ease-out, background-color 0.5s ease-out; /* Animate size and color */
    }

    .pool-status-text {
        text-align: center;
        font-size: 1.1em;
        font-weight: bold;
    }

    /* Animation for pool updates */
     .pool-taking {
        background-color: var(--danger-color) !important; /* Flash red when taking */
     }
      .pool-regenerating {
        background-color: var(--secondary-color) !important; /* Flash green when regenerating */
      }

    /* Explanation Section */
    #toggle-explanation {
        display: block; /* Make it block to center */
        margin: 20px auto; /* Center the button */
        padding: 12px 25px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease;
    }
    #toggle-explanation:hover {
        background-color: #218838;
    }

    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--bg-light);
        display: none; /* Start hidden */
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    #explanation h2 {
        margin-top: 0;
    }
    #explanation h3 {
        color: var(--text-dark);
        margin-top: 15px;
        margin-bottom: 8px;
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 4px;
    }
    #explanation p {
        margin-bottom: 15px;
        line-height: 1.7;
    }
     #explanation ul {
         margin-bottom: 15px;
         padding-right: 20px;
     }
      #explanation ul li {
          margin-bottom: 8px;
      }


</style>

<button id="toggle-explanation">מהי הטרגדייה של המאגר המשותף? (הצג/הסתר הסבר)</button>

<div id="explanation">
    <h2>על הטרגדייה של המאגר המשותף</h2>

    <h3>מהי טרגדיית המאגר המשותף?</h3>
    <p>טרגדיית המאגר המשותף מתארת מצב שכיח ומאתגר: קבוצה של פרטים, שכל אחד מהם פועל באופן "הגיוני" ורציונלי כדי להשיג את מירב התועלת לעצמו, מובילה בסופו של דבר לקריסה או לדלדול קיצוני של משאב משותף, למרות שהדבר פוגע אנושות באינטרס הקולקטיבי של כולם בטווח הארוך. הבעיה נעוצה בכך שהתועלת מניצול נוסף של המשאב נצברת כולה לפרט שמנצל אותו, בעוד שהעלות (הדלדול של המשאב) מתפזרת על כלל המשתמשים במאגר.</p>

    <h3>הרעיון של גארט הרדין (Garrett Hardin)</h3>
    <p>את הרעיון הפך לפופולרי הביולוג גארט הרדין במאמרו המשפיע משנת 1968. הוא השתמש במשל פשוט אך עוצמתי: שטח מרעה פתוח לרווחה המשמש מספר רועים. כל רועה רוצה להגדיל את רווחיו, ולכן יש לו תמריץ להוסיף עוד כבשים לעדרו, גם אם זה על חשבון שחיקת המרעה. מכיוון שכל רועה חושב כך, המרעה נשחק במהירות עד שהוא נהרס לחלוטין - מצב גרוע בהרבה מזה שהיה יכול להתקיים לו היו כולם מגבילים את עצמם.</p>

    <h3>דוגמאות קלאסיות ועכשוויות מהחיים</h3>
    <p>עקרון הטרגדייה אינו מוגבל רק לשטחי מרעה. הוא מסביר בעיות רבות שאנו רואים בעולם:</p>
    <ul>
        <li><strong>דייג יתר:</strong> אגם או ים פתוח לדייגים רבים מוביל לדלדול דרסטי של אוכלוסיית הדגים, כי לכל דייג משתלם לדוג כמה שיותר מהר לפני שהאחרים יקחו.</li>
        <li><strong>זיהום אוויר ומים:</strong> מפעלים ואנשים מזהמים כי עלות הטיפול בזיהום גבוהה עבורם, וה"עלות" של האוויר או המים המזוהמים מתפזרת על כלל האוכלוסייה.</li>
        <li><strong>שימוש בכבישים:</strong> עומסי תנועה נוצרים כי לכל נהג יש תמריץ להשתמש ברכב פרטי, גם כשהצפיפות פוגעת בכולם.</li>
        <li><strong>שימוש במשאבי מים:</strong> שאיבת יתר מבארות או אגמים משותפים מובילה לירידת מפלסים או התייבשות.</li>
        <li><strong>הצפת מידע ותשומת לב:</strong> בעידן האינטרנט, "המרחב הציבורי" של תשומת הלב מוצף בתוכן זול וקליקבייטים, כי לכל יצרן תוכן יש תמריץ למשוך תשומת לב מיידית על חשבון איכות כללית.</li>
    </ul>

    <h3>המתח בין הפרט לקולקטיב</h3>
    <p>הסימולציה מדגימה את הדילמה המרכזית: בטווח הקצר, לקיחה מרובה מהמאגר משתלמת לך באופן אישי. אבל אם גם ה"שחקנים" האחרים (שמייצגים פה את שאר המשתמשים במשאב) יפעלו באותה לוגיקה של מקסום רווח אישי מיידי, המאגר יתכלה מהר וכולם יפסידו בסופו של דבר. זו התנגשות בין האינטרס הרציונלי של הפרט לרווחה הקולקטיבית ארוכת הטווח.</p>

    <h3>פתרונות אפשריים לטרגדייה</h3>
    <p>גארט הרדין הציע במקור בעיקר פתרונות של רגולציה ממשלתית (חוקים, מיסים, מכסות) או הפרטה (חלוקת המשאב לבעלות פרטית). אולם מחקרה פורץ הדרך של פרופ' אלינור אוסטרום (Elinor Ostrom), כלת פרס נובל לכלכלה, הראה שקהילות רבות ברחבי העולם הצליחו לנהל בהצלחה משאבים משותפים (כמו יערות, מערכות השקיה, שטחי מרעה) באמצעות מוסדות וכללים שהן עצמן פיתחו. פתרונות אלו כוללים, בין השאר: הגדרת גבולות ברורים למשאב ולמשתמשים; כללי שימוש המותאמים למשאב המקומי; השתתפות המשתמשים בקביעת הכללים; ניטור יעיל; סנקציות הדרגתיות; ומנגנונים לפתרון סכסוכים. הסימולציה שלפניכם היא גרסה פשוטה ביותר של הבעיה. חשבו: אילו "כללים" הייתם מוסיפים לסימולציה כדי שהמאגר ישרוד לאורך זמן?</p>
</div>

<script>
    const simulationApp = document.getElementById('simulation-app');
    const currentRoundSpan = document.getElementById('current-round');
    const maxRoundsSpan = document.getElementById('max-rounds');
    const poolSizeSpan = document.getElementById('pool-size');
    const totalProfitSpan = document.getElementById('total-profit');
    const takeAmountInput = document.getElementById('take-amount');
    const takeButton = document.getElementById('take-button');
    const roundResultsDiv = document.getElementById('round-results');
    const previousRoundNumberSpan = document.getElementById('previous-round-number');
    const playerTakeSpan = document.getElementById('player-take');
    const roundProfitSpan = document במאי הקריאייטיב ומפתח התוכן החינוכי הגיש את התוכן המשודרג.
```js
    const othersTakeSpan = document.getElementById('others-take');
    const poolAfterTakeSpan = document.getElementById('pool-after-take');
    const poolAfterRegenerationSpan = document.getElementById('pool-after-regeneration');
    const gameMessageDiv = document.getElementById('game-message');
    const messageTitle = document.getElementById('message-title');
    const messageText = document.getElementById('message-text');
    const restartButton = document.getElementById('restart-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const visualPoolFill = document.getElementById('pool-fill');
    const visualPoolContainer = document.getElementById('visual-pool');


    // Game Parameters
    const initialPoolSize = 100;
    const maxPoolSize = 200; // Increased max pool size for visual effect potential
    const regenerationRate = 0.2; // Higher regeneration rate to make conservation more impactful
    const minPoolSizeForCollapse = 5; // Slightly lower collapse threshold
    const numComputerPlayers = 3; // Explicitly computer players count
    const maxRounds = 25; // Increased max rounds for longer game

    // Game State
    let currentPoolSize = initialPoolSize;
    let currentRound = 1;
    let totalProfit = 0;
    let gameEnded = false;

    // Computer Player Strategy (More reactive: take more when pool is full, less when low)
    function getComputerTakeAmount() {
        const aggressiveFactor = 0.1; // How much they try to take based on current pool
        const baseTake = 5; // Minimum they might try to take

        // Scale take amount based on current pool size, relative to maxPoolSize
        let desiredTake = Math.round((currentPoolSize / maxPoolSize) * (initialPoolSize * aggressiveFactor) + baseTake);

        // Add some random variation
        desiredTake = Math.max(1, desiredTake + Math.floor(Math.random() * 7) - 3); // Ensure minimum 1

        return Math.min(desiredTake, Math.floor(currentPoolSize / numComputerPlayers)); // Cannot take more than is available per player
    }

    function updateVisualPool() {
        const fillPercentage = (currentPoolSize / maxPoolSize) * 100;
        visualPoolFill.style.height = `${Math.max(0, Math.min(100, fillPercentage))}%`; // Clamp between 0% and 100%

        // Change color based on pool level
        if (fillPercentage > 75) {
            visualPoolFill.style.backgroundColor = var('secondary-color', '#28a745'); // Green
        } else if (fillPercentage > 30) {
             visualPoolFill.style.backgroundColor = var('info-color', '#17a2b8'); // Blue
        } else if (fillPercentage > minPoolSizeForCollapse / maxPoolSize * 100) {
             visualPoolFill.style.backgroundColor = var('warning-color', '#ffc107'); // Yellow/Orange
        }
        else {
             visualPoolFill.style.backgroundColor = var('danger-color', '#dc3545'); // Red
        }
    }
     function var(name, fallback) {
         const style = getComputedStyle(document.documentElement);
         return style.getPropertyValue(`--${name}`) || fallback;
     }


    function updateUI() {
        currentRoundSpan.textContent = currentRound;
        maxRoundsSpan.textContent = maxRounds;
        poolSizeSpan.textContent = Math.max(0, Math.round(currentPoolSize));
        totalProfitSpan.textContent = Math.round(totalProfit);
        takeAmountInput.max = Math.floor(Math.max(0, currentPoolSize)); // Cannot take more than available
        takeAmountInput.value = Math.min(parseInt(takeAmountInput.value, 10) || 0, takeAmountInput.max); // Adjust input value and handle invalid input

        updateVisualPool();


        if (gameEnded) {
            takeButton.disabled = true;
            takeAmountInput.disabled = true;
            restartButton.style.display = 'block';
            roundResultsDiv.style.display = 'none'; // Hide previous results on game end
        } else {
            takeButton.disabled = false;
            takeAmountInput.disabled = false;
            restartButton.style.display = 'none';
            gameMessageDiv.style.display = 'none'; // Hide game message during play
        }

        // Reset result display or keep it for review? Let's hide it initially for the *next* round
        if (!gameEnded && currentRound > 1) {
             // Keep results visible after a round, but hide message
             roundResultsDiv.style.display = 'block';
        } else {
             roundResultsDiv.style.display = 'none';
        }

    }

    function endGame(messageTitleText, messageBodyHTML, type = 'info') {
        gameEnded = true;
        messageTitle.textContent = messageTitleText;
        messageText.innerHTML = messageBodyHTML + `<br><br>סיימת את הסימולציה עם רווח כולל של <strong style="color:${type === 'win' ? var('secondary-color') : var('text-dark')}">${Math.round(totalProfit)}</strong> יחידות.`;
        gameMessageDiv.className = 'game-section'; // Reset classes
        gameMessageDiv.classList.add(type);
        gameMessageDiv.style.display = 'block';
        updateUI(); // Update UI to disable inputs and show restart
        takeButton.disabled = true;
        takeAmountInput.disabled = true;
         takeAmountInput.value = 0; // Reset input value display
    }

    function nextRound(playerTake) {
        if (gameEnded) return;

        const roundNumber = currentRound; // Store current round for results display

        // --- Actions Phase ---
        const playerActualTake = Math.min(playerTake, Math.floor(currentPoolSize));
        let roundProfit = playerActualTake;
        totalProfit += roundProfit;
        currentPoolSize -= playerActualTake;

        let othersTotalTake = 0;
        for (let i = 0; i < numComputerPlayers; i++) {
            const computerTake = Math.min(getComputerTakeAmount(), Math.floor(currentPoolSize));
            othersTotalTake += computerTake;
            currentPoolSize -= computerTake;
        }

        const poolAfterTake = Math.max(0, currentPoolSize);

         // --- Regeneration Phase ---
        let poolAfterRegeneration = Math.min(maxPoolSize, poolAfterTake * (1 + regenerationRate));

        // Display round results
        previousRoundNumberSpan.textContent = roundNumber;
        playerTakeSpan.textContent = playerActualTake;
        roundProfitSpan.textContent = roundProfit;
        othersTakeSpan.textContent = othersTotalTake;
        poolAfterTakeSpan.textContent = Math.round(poolAfterTake);
        poolAfterRegenerationSpan.textContent = Math.round(poolAfterRegeneration);
        roundResultsDiv.style.display = 'block'; // Show results for the round just finished

        currentPoolSize = poolAfterRegeneration;
        currentRound++;

        // Animate pool changes (simplified animation by just updating the fill, CSS transitions handle the rest)
        updateVisualPool(); // Update visual pool immediately after changes

        // Check for game end conditions
        if (currentPoolSize < minPoolSizeForCollapse) {
            endGame(
                'המאגר קרס!',
                `אוי לא! גודל המאגר ירד מתחת לסף ההתמוטטות (${minPoolSizeForCollapse} יחידות). הוא אינו יכול עוד להתחדש בצורה מספקת.`,
                'danger'
            );
        } else if (currentRound > maxRounds) {
             endGame(
                 'המשחק הסתיים - המאגר שרד!',
                 `ברכות! סיימתם בהצלחה ${maxRounds} סיבובים. המאגר עדיין קיים (בגודל של ${Math.round(currentPoolSize)} יחידות).`,
                 'win'
             );
        } else {
            // Prepare UI for next round
            takeAmountInput.value = 0; // Reset input for next round
            updateUI(); // Update round number, pool size for *next* round
        }
    }

    function startGame() {
        currentPoolSize = initialPoolSize;
        currentRound = 1;
        totalProfit = 0;
        gameEnded = false;
        roundResultsDiv.style.display = 'none';
        gameMessageDiv.style.display = 'none';
        takeAmountInput.value = 0;
        updateUI();
    }

    // Event Listeners
    takeButton.addEventListener('click', () => {
        if (gameEnded) return;
        const takeAmount = parseInt(takeAmountInput.value, 10);

        if (isNaN(takeAmount) || takeAmount < 0) {
             // Gentle feedback instead of alert
            takeAmountInput.value = 0;
            takeAmountInput.style.borderColor = var('warning-color');
            setTimeout(() => { takeAmountInput.style.borderColor = var('border-color'); }, 1000);
            return;
        }
         if (takeAmount > Math.floor(currentPoolSize)) {
            // Gentle feedback
            takeAmountInput.value = Math.floor(currentPoolSize);
            takeAmountInput.style.borderColor = var('danger-color');
             setTimeout(() => { takeAmountInput.style.borderColor = var('border-color'); }, 1000);
            return;
        }
        nextRound(takeAmount);
    });

    restartButton.addEventListener('click', startGame);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על הטרגדייה של המאגר המשותף' : 'מהי הטרגדייה של המאגר המשותף? (הצג/הסתר הסבר)';
    });

    // Initialize the game
    startGame();

</script>
```