---
title: "דילמת האסיר של סיבוב אחד"
english_slug: one-shot-prisoners-dilemma
category: "מתמטיקה"
tags:
  - משחק אסטרטגי
  - כלכלה התנהגותית
  - הדמיה
---
# משחק: התמודדות אחת על אחת בדילמת האסיר

צאו למסע מרתק ללב תיאוריית המשחקים. בסיבוב בודד זה, תתמודדו מול המחשב בהחלטה קריטית אחת. אין היסטוריה, אין עתיד - רק ההחלטה הנוכחית והתוצאה שלה. האם תבחרו בנתיב שיתוף הפעולה, או שתלכו על בגידה למען רווח אישי?

<div class="game-container">
    <h1>הדילמה עומדת בפניך</h1>
    <p class="intro-text">המשחק הזה הוא סימולציה מפושטת של דילמת האסיר הקלאסית. המחשב יקבל החלטה (קבועה מראש במשחק של סיבוב אחד, בהתאם לעקרונות רציונליים בתיאוריית המשחקים), ואתם תקבלו את ההחלטה שלכם. בסופו של דבר, התשלומים של שניכם ייקבעו על פי שילוב ההחלטות.</p>

    <h2>ההחלטה שלך</h2>
    <p class="instruction">בחר/י את האסטרטגיה שלך לסיבוב זה:</p>

    <div class="payoff-matrix">
        <h3>מטריצת התשלומים (התשלום שלך, התשלום של המחשב)</h3>
        <table>
            <thead>
                <tr>
                    <th></th>
                    <th>המחשב: שיתוף פעולה</th>
                    <th>המחשב: בגידה</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th>את/ה: שיתוף פעולה</th>
                    <td>(3, 3) - תגמול הדדי</td>
                    <td>(0, 5) - פראייר</td>
                </tr>
                <tr>
                    <th>את/ה: בגידה</th>
                    <td>(5, 0) - פיתוי</td>
                    <td>(1, 1) - עונש הדדי</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="choice-buttons">
        <button id="cooperate-btn" class="choice-btn"><i class="icon-handshake">🤝</i> שיתוף פעולה</button>
        <button id="defect-btn" class="choice-btn"><i class="icon-broken-heart">💔</i> בגידה</button>
    </div>

    <div class="visual-game-state">
        <div class="player-state you">
            <div class="label">את/ה</div>
            <div id="user-action-display" class="action-display initial">?</div>
        </div>
        <div class="vs-divider">VS</div>
        <div class="player-state computer">
            <div class="label">המחשב</div>
            <div id="computer-action-display" class="action-display initial">?</div>
        </div>
    </div>

    <div class="result-area hidden">
        <h3>רגע האמת: התוצאות!</h3>
        <p id="user-choice"></p>
        <p id="computer-choice"></p>
        <p id="outcome"></p>
        <p id="payoffs"></p>
    </div>
</div>

<style>
    body {
        font-family: 'Heebo', sans-serif; /* Enhanced font */
        line-height: 1.7;
        margin: 0;
        background: linear-gradient(135deg, #f4f7f6 0%, #e0e9e8 100%); /* Subtle gradient */
        color: #333;
        direction: rtl;
        text-align: right;
        padding-bottom: 50px; /* Add padding for footer if any */
    }

    h1, h2, h3 {
        color: #0056b3;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700; /* Bold headings */
    }

    h1 {
        font-size: 2.2em;
        color: #003366;
    }

    h2 {
         font-size: 1.8em;
         color: #004085;
    }

    .game-container {
        background-color: #ffffff;
        border-radius: 15px; /* More rounded */
        padding: 40px; /* More padding */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Deeper shadow */
        max-width: 750px; /* Slightly wider */
        margin: 30px auto; /* More margin */
        text-align: center;
        overflow: hidden; /* Clear floats */
    }

     .intro-text {
        font-size: 1.1em;
        color: #555;
        margin-bottom: 30px;
        text-align: center;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
     }

    .instruction {
        font-size: 1.2em;
        margin-bottom: 25px;
        color: #0056b3;
        font-weight: 600;
    }

    .payoff-matrix {
        margin: 30px auto; /* More margin */
        border: 1px solid #ccc; /* Slightly softer border */
        border-radius: 10px; /* More rounded */
        overflow: hidden;
        max-width: 550px; /* Wider matrix */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .payoff-matrix h3 {
        background-color: #eef2f7; /* Lighter blue */
        color: #004085; /* Darker blue */
        padding: 12px; /* More padding */
        margin: 0;
        font-size: 1.1em; /* Slightly larger */
        text-align: center;
        border-bottom: 1px solid #ccc;
    }

    .payoff-matrix table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.95em;
    }

    .payoff-matrix th, .payoff-matrix td {
        border: 1px solid #ddd;
        padding: 15px; /* More padding */
        text-align: center;
    }

    .payoff-matrix th {
        background-color: #f8f9fa; /* Light gray */
        font-weight: bold;
        color: #333;
    }

    .payoff-matrix tbody tr:nth-child(even) {
        background-color: #f2f4f7; /* Slightly darker gray */
    }

     .payoff-matrix td:first-child {
         font-weight: bold;
         background-color: #f8f9fa;
     }

    .payoff-matrix td strong {
        color: #007bff;
    }

    .choice-buttons {
        margin-top: 30px;
        margin-bottom: 30px; /* Space below buttons */
    }

    .choice-btn {
        padding: 14px 30px; /* More padding */
        margin: 0 15px; /* More margin between buttons */
        font-size: 1.2em; /* Larger text */
        cursor: pointer;
        border: none;
        border-radius: 30px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: 600;
        display: inline-flex; /* Allow icon next to text */
        align-items: center; /* Vertically center icon and text */
    }

    .choice-btn i {
        margin-left: 8px; /* Space between icon and text */
        font-size: 1.3em; /* Larger icon */
    }


    #cooperate-btn {
        background-color: #28a745; /* Green */
        color: white;
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
    }

    #cooperate-btn:hover:not(:disabled) {
        background-color: #218838; /* Darker green */
        box-shadow: 0 6px 12px rgba(40, 167, 69, 0.4);
    }

    #defect-btn {
        background-color: #dc3545; /* Red */
        color: white;
        box-shadow: 0 4px 8px rgba(220, 53, 69, 0.3);
    }

    #defect-btn:hover:not(:disabled) {
        background-color: #c82333; /* Darker red */
        box-shadow: 0 6px 12px rgba(220, 53, 69, 0.4);
    }

    .choice-btn:active:not(:disabled) {
        transform: scale(0.95); /* More pronounced press effect */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .choice-btn:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        box-shadow: none;
    }

    .visual-game-state {
        display: flex; /* Use flexbox */
        justify-content: center; /* Center content */
        align-items: center; /* Align items vertically */
        margin: 40px auto; /* Add margin */
        gap: 30px; /* Space between players and VS */
        max-width: 500px;
    }

    .player-state {
        flex-basis: 150px; /* Fixed width for player boxes */
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px 10px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }

    .player-state .label {
        font-size: 1.1em;
        font-weight: bold;
        color: #0056b3;
        margin-bottom: 10px;
    }

    .action-display {
        font-size: 2.5em; /* Larger action icon/text */
        font-weight: bold;
        color: #555; /* Default color */
        height: 1.5em; /* Reserve space */
        display: flex;
        justify-content: center;
        align-items: center;
        transition: color 0.5s ease, transform 0.5s ease, opacity 0.5s ease;
        opacity: 0; /* Hidden initially */
        transform: scale(0.8); /* Start smaller */
    }

     .action-display.initial {
         font-size: 2em;
         color: #aaa;
         opacity: 1;
         transform: none;
     }

    .action-display.revealed {
        opacity: 1;
        transform: scale(1);
    }

    .action-display.cooperate-color { color: #28a745; } /* Green for cooperate */
    .action-display.defect-color { color: #dc3545; } /* Red for defect */


    .vs-divider {
        font-size: 1.8em;
        font-weight: bold;
        color: #007bff;
        padding: 0 10px;
    }


    .result-area {
        margin-top: 40px; /* More margin */
        padding-top: 25px; /* More padding */
        border-top: 2px dashed #ccc; /* Thicker dashed border */
        text-align: right;
        opacity: 0;
        transform: translateY(30px); /* More pronounced animation */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Slower animation */
    }

    .result-area.visible {
        opacity: 1;
        transform: translateY(0);
    }

    .result-area h3 {
        text-align: center;
        color: #007bff;
        margin-bottom: 20px;
        font-size: 1.6em;
    }

    .result-area p {
        margin-bottom: 12px; /* More space between paragraphs */
        font-size: 1.1em; /* Slightly larger text */
        color: #555;
    }

    .result-area p strong {
        color: #0056b3;
        font-weight: bold;
    }

    .hidden {
        display: none; /* Keep for JS toggling */
    }

    /* Ensure elements are hidden when result-area is hidden */
    .result-area.hidden > * {
        opacity: 0;
    }


    #show-explanation-btn {
        display: block;
        margin: 40px auto; /* More margin */
        padding: 15px 30px; /* More padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 30px; /* Pill shape */
        background-color: #007bff; /* Blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }

    #show-explanation-btn:hover {
        background-color: #0056b3; /* Darker blue */
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
    }

    #show-explanation-btn:active {
        transform: scale(0.98);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }


    #explanation-area {
        background-color: #e9f7ef; /* Light green background */
        border-right: 5px solid #28a745; /* Green border on the right for RTL */
        padding: 30px; /* More padding */
        margin: 20px auto;
        max-width: 750px;
        border-radius: 8px;
        display: none; /* Initially hidden by JS */
        opacity: 0; /* For entrance animation */
        transform: translateX(-20px); /* For entrance animation */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
    }

    #explanation-area.visible {
        opacity: 1;
        transform: translateX(0);
    }


    #explanation-area h2 {
         color: #218838; /* Darker green */
         text-align: right;
         margin-top: 0;
         margin-bottom: 20px;
         font-size: 1.8em;
    }

    #explanation-area p {
        margin-bottom: 15px;
        text-align: right;
        color: #444;
        font-size: 1em;
    }

    #explanation-area strong {
        color: #0056b3;
    }

    #explanation-area ul {
        list-style-type: disc;
        margin-right: 30px; /* Indent list */
        padding-right: 0;
        margin-bottom: 15px;
    }

     #explanation-area li {
        margin-bottom: 8px;
        color: #444;
     }

     /* Optional: Basic responsiveness */
     @media (max-width: 600px) {
        .game-container, #explanation-area {
            padding: 20px;
            margin: 20px;
        }
        .choice-btn {
            padding: 10px 20px;
            margin: 5px;
            font-size: 1em;
            border-radius: 20px;
        }
         .choice-btn i {
             font-size: 1em;
             margin-left: 5px;
         }
        .payoff-matrix th, .payoff-matrix td {
            padding: 8px;
            font-size: 0.9em;
        }
        .visual-game-state {
            flex-direction: column; /* Stack on small screens */
            gap: 15px;
        }
         .vs-divider {
             font-size: 1.5em;
         }
         .player-state {
             flex-basis: auto;
             width: 80%; /* Adjust width */
             padding: 15px;
         }
         .action-display {
             font-size: 2em;
         }
         h1 { font-size: 1.8em; }
         h2 { font-size: 1.5em; }
         .result-area h3 { font-size: 1.4em; }

     }


</style>

<button id="show-explanation-btn">מה קרה כאן? הצג הסבר</button>

<div id="explanation-area" class="hidden">
    <h2>ההסבר: דילמת האסיר ונקודת שיווי המשקל</h2>
    <p>משחק דילמת האסיר הוא דוגמה קלאסית בתיאוריה של משחקים הממחישה מדוע שני פרטים עשויים שלא לשתף פעולה, גם אם נראה שזה לטובתם המשותפת. במשחק הבסיסי של סיבוב אחד (כמו ששיחקת כאן), יש שני שחקנים (את/ה והמחשב) ולכל אחד שתי אפשרויות פעולה: "שיתוף פעולה" או "בגידה".</p>
    <p>התוצאות (התשלומים) תלויות בהחלטות של שני השחקנים, כפי שראית במטריצת התשלומים:</p>
    <ul>
        <li>**תגמול הדדי (שיתוף פעולה, שיתוף פעולה):** שניכם משתפים פעולה ומקבלים תגמול סביר (3, 3).</li>
        <li>**פיתוי (בגידה, שיתוף פעולה):** אתה בוגד והמחשב משתף פעולה. אתה מקבל את התשלום הגבוה ביותר (5), והמחשב מקבל את הנמוך ביותר (0).</li>
        <li>**פראייר (שיתוף פעולה, בגידה):** אתה משתף פעולה והמחשב בוגד. אתה מקבל את הנמוך ביותר (0), והמחשב מקבל את הגבוה ביותר (5).</li>
        <li>**עונש הדדי (בגידה, בגידה):** שניכם בוגדים ומקבלים עונש נמוך (1, 1).</li>
    </ul>
    <p>ההסבר מתמקד במושג "אסטרטגיה דומיננטית" ו"שיווי משקל נאש":</p>
    <p><strong>אסטרטגיה דומיננטית:</strong> זוהי אסטרטגיה שהיא הטובה ביותר לשחקן מסוים, ללא קשר למה שהשחקן השני עושה.</p>
    <ul>
        <li>אם אתה חושב שהמחשב ישתף פעולה, האם כדאי לך לשתף פעולה (מקבל 3) או לבגוד (מקבל 5)? **כדאי לך לבגוד (5 > 3).**</li>
        <li>אם אתה חושב שהמחשב יבגוד, האם כדאי לך לשתף פעולה (מקבל 0) או לבגוד (מקבל 1)? **כדאי לך לבגוד (1 > 0).**</li>
    </ul>
    <p>בכל מקרה, ללא קשר לבחירת המחשב, האסטרטגיה הטובה ביותר עבורך היא לבגוד. לכן, "בגידה" היא האסטרטגיה הדומיננטית שלך. אותו הגיון תקף גם לגבי המחשב (בהנחה שיש לו מניעים רציונליים), ולכן גם עבורו "בגידה" היא האסטרטגיה הדומיננטית במשחק של סיבוב אחד.</p>
    <p><strong>שיווי משקל נאש (Nash Equilibrium):</strong> זהו מצב שבו אף שחקן לא יכול לשפר את מצבו על ידי שינוי חד-צדדי של האסטרטגיה שלו, בהינתן האסטרטגיה של השחקן האחר. במשחק דילמת האסיר של סיבוב אחד, שיווי המשקל נאש הוא כאשר שני השחקנים בוחרים ב"בגידה" (בגידה, בגידה).</p>
    <ul>
        <li>במצב (בגידה, בגידה), אתה מקבל 1. אם תשנה אסטרטגיה ל"שיתוף פעולה" בעוד המחשב נשאר ב"בגידה", תקבל 0. לכן, לא כדאי לך לשנות.</li>
        <li>באופן דומה, גם למחשב לא כדאי לשנות את האסטרטגיה שלו מ"בגידה" ל"שיתוף פעולה" אם אתה נשאר ב"בגידה" (יקבל 0 במקום 1).</li>
    </ul>
    <p>למרות שהמצב (בגידה, בגידה) מביא לכם תשלום נמוך (1, 1) בהשוואה למצב (שיתוף פעולה, שיתוף פעולה) שהיה מביא (3, 3), ההיגיון של האסטרטגיה הדומיננטית מוביל את שניכם באופן רציונלי לבחור ב"בגידה". זהו הלב של הדילמה: רציונליות פרטנית מובילה לתוצאה תת-אופטימלית עבור הקבוצה (שני השחקנים יחד).</p>
    <p>הדמיה זו מדגימה כיצד, בסיבוב יחיד מול שחקן אסטרטגי (המחשב במקרה זה, הפועל לפי האסטרטגיה הדומיננטית שלו), האסטרטגיה "בגידה" היא הבחירה הרציונלית מבחינה תיאורטית.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const cooperateBtn = document.getElementById('cooperate-btn');
        const defectBtn = document.getElementById('defect-btn');
        const resultArea = document.querySelector('.result-area');
        const userChoiceElem = document.getElementById('user-choice');
        const computerChoiceElem = document.getElementById('computer-choice');
        const outcomeElem = document.getElementById('outcome');
        const payoffsElem = document.getElementById('payoffs');
        const showExplanationBtn = document.getElementById('show-explanation-btn');
        const explanationArea = document.getElementById('explanation-area');
        const userActionDisplay = document.getElementById('user-action-display');
        const computerActionDisplay = document.getElementById('computer-action-display');

        // Payoff matrix: [user_choice][computer_choice] -> [user_payoff, computer_payoff, outcome_description]
        const payoffs = {
            'cooperate': {
                'cooperate': [3, 3, 'תוצאה: תגמול הדדי. שניכם הרווחתם יפה.'], // Reward
                'defect': [0, 5, 'תוצאה: אתה פראייר! המחשב בגד בך וזכה בגדול.']     // Sucker
            },
            'defect': {
                'cooperate': [5, 0, 'תוצאה: פיתוי! בגדת במחשב ששיתף פעולה וקיבלת את התשלום הגבוה ביותר.'], // Temptation
                'defect': [1, 1, 'תוצאה: עונש הדדי. שניכם בחרתם לבגוד וקיבלתם תשלום נמוך.']     // Punishment
            }
        };

        // Computer's strategy in a one-shot game (rational choice leading to Nash Equilibrium): Always Defect
        const computerChoice = 'defect';
        const computerActionText = '💔 בגידה'; // Using consistent icon/text
        const computerColorClass = 'defect-color';


        function handleChoice(userChoice) {
            // Disable buttons immediately
            cooperateBtn.disabled = true;
            defectBtn.disabled = true;
            cooperateBtn.classList.add('disabled'); // Add disabled class for styling
            defectBtn.classList.add('disabled');

            // Determine display text and color for user choice
            const userActionText = userChoice === 'cooperate' ? '🤝 שיתוף פעולה' : '💔 בגידה';
            const userColorClass = userChoice === 'cooperate' ? 'cooperate-color' : 'defect-color';

            // Animate user choice display
            userActionDisplay.textContent = userActionText;
            userActionDisplay.classList.remove('initial');
            userActionDisplay.classList.add('revealed', userColorClass);

            // Simulate computer thinking/revealing with a delay
            setTimeout(() => {
                // Animate computer choice display (always defect)
                computerActionDisplay.textContent = computerActionText;
                computerActionDisplay.classList.remove('initial');
                computerActionDisplay.classList.add('revealed', computerColorClass);

                // Determine the outcome and payoffs
                const [userPayoff, computerPayoff, outcomeDescription] = payoffs[userChoice][computerChoice];

                // Populate the result area elements
                userChoiceElem.innerHTML = `<strong>הבחירה שלך:</strong> ${userActionText}`;
                computerChoiceElem.innerHTML = `<strong>הבחירה של המחשב:</strong> ${computerActionText}`;
                outcomeElem.textContent = outcomeDescription;
                payoffsElem.innerHTML = `<strong>התשלומים:</strong> לך - <span class="payoff-score">${userPayoff}</span> נקודות, למחשב - <span class="payoff-score">${computerPayoff}</span> נקודות`;

                // Show the result area with animation after another delay
                setTimeout(() => {
                    resultArea.classList.remove('hidden');
                    resultArea.classList.add('visible');
                }, 800); // Delay showing results after choices are revealed

            }, 800); // Delay computer reveal

        }

        cooperateBtn.addEventListener('click', () => handleChoice('cooperate'));
        defectBtn.addEventListener('click', () => handleChoice('defect'));

        // Show/Hide Explanation logic
        showExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationArea.classList.contains('hidden');
            if (isHidden) {
                explanationArea.classList.remove('hidden');
                // Use timeout to allow display:block to take effect before animation
                setTimeout(() => {
                    explanationArea.style.display = 'block'; // Override display: none
                    explanationArea.classList.add('visible');
                }, 10); // Small delay
                showExplanationBtn.textContent = 'הסתר הסבר';
            } else {
                explanationArea.classList.remove('visible');
                 // Use timeout to allow animation to finish before hiding
                setTimeout(() => {
                    explanationArea.classList.add('hidden');
                     explanationArea.style.display = 'none'; // Explicitly hide
                }, 600); // Match CSS transition duration
                showExplanationBtn.textContent = 'מה קרה כאן? הצג הסבר';
            }
        });

        // Initial state: hide result area and explanation
        resultArea.classList.add('hidden');
        explanationArea.classList.add('hidden'); // Ensure it's hidden initially
        explanationArea.style.display = 'none'; // Ensure display is none initially
    });
</script>
---