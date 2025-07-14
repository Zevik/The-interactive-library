---
title: "אתגר חשיבה: פענוח חוקיות סדרת מספרים (הטיית האישוש)"
english_slug: confirmation-bias-guessing-game-enhanced
category: "מדעי החברה / פסיכולוגיה"
tags: ["פסיכולוגיה", "הטיית אישוש", "ניסוי", "חשיבה ביקורתית"]
---
# אתגר חשיבה: פענוח חוקיות סדרת מספרים

צאו למסע גילוי מרתק שחושף איך המוח שלנו מנסה לפתור תעלומות. לפני שתקבלו כל הסבר, קבלו את האתגר: לפענח את החוק הנסתר מאחורי סדרות מספרים. המטרה היא לאסוף מספיק מידע באמצעות בדיקות יצירתיות, כדי לנחש נכונה את החוקיות הספציפית. האם תצליחו לחשוב מחוץ לקופסה?

<div id="game-container">
    <div class="game-header">
        <h2>המשימה: גלו את החוק הסודי</h2>
        <p>הסדרה הבאה *מקיימת* חוקיות סודית אחת ויחידה שאני חושב עליה:</p>
        <div id="initial-sequence" class="sequence-display">2, 4, 6</div>
    </div>

    <div class="game-section">
        <h3>בדקו את ההשערות שלכם</h3>
        <p>הציעו סדרת מספרים משלכם (3 מספרים מופרדים בפסיקים, לדוגמה: 3,6,9) כדי לבדוק אם היא מקיימת את החוקיות הסודית:</p>
        <div class="input-area">
            <input type="text" id="user-sequence-input" placeholder="הכנס סדרה (לדוגמה: 3, 6, 9)">
            <button id="test-sequence-button">בדוק סדרה</button>
        </div>
        <div id="input-validation-message" class="validation-message"></div>
    </div>

    <div class="game-section">
        <h3>היסטוריית בדיקות</h3>
        <div id="history-area" class="history-display">
            <!-- Tested sequences and results will appear here -->
            <div class="history-placeholder">עדיין לא בוצעו בדיקות... נסו להכניס סדרה!</div>
        </div>
         <button id="hint-button" class="hint-button" style="display: none;">צריכים רמז?</button>
    </div>


    <div class="game-section">
        <h3>כשאתם בטוחים, נחשו את החוק</h3>
        <p>לאחר שאספתם מספיק מידע, נסו לנסח את החוקיות הנסתרת במילים שלכם.</p>
        <div class="input-area">
            <input type="text" id="user-rule-guess-input" placeholder="הכנס את ניחוש החוקיות שלך במילים">
            <button id="guess-rule-button">נחשו את החוק!</button>
        </div>
         <div id="guess-result" class="result-display">
            <!-- Result of rule guess appears here -->
        </div>
    </div>

</div>

<button id="show-explanation-button" class="explanation-toggle-button">הצג הסבר על התופעה</button>

<div id="explanation" class="explanation-area" style="display: none;">
    <h2>מאחורי הקלעים: הטיית האישוש נחשפת</h2>
    <p>המשחקון ששיחקתם הוא הדגמה חיה לניסוי המפורסם "2-4-6" של הפסיכולוג פיטר ואסון (Peter Wason). מטרתו לחשוף בפנינו הטיה קוגניטיבית עוצמתית ורווחת: "הטיית האישוש" (Confirmation Bias).</p>

    <p><strong>מהי הטיית האישוש?</strong> זוהי הנטייה המובנית שלנו לחפש, לפרש ולזכור מידע באופן שמאשש (מאשר) את האמונות, ההשערות או התיאוריות שכבר קיימות לנו. אנו נוטים להתמקד בעדויות התומכות בנקודת המבט הנוכחית שלנו ולהתעלם, להמעיט בערכן או לשכוח עדויות שסותרות אותה.</p>

    <p><strong>כיצד זה בא לידי ביטוי במשחק?</strong> רוב המשתתפים, כשהם רואים את הסדרה הראשונית (2, 4, 6), מניחים מייד שהחוק הוא "מספרים זוגיים עוקבים", "קפיצות של 2", או משהו דומה. בהשפעת הטיית האישוש, הם נוטים לבדוק רק סדרות שמתאימות להשערה שלהם (למשל: 8, 10, 12 או 20, 22, 24). כשהמערכת מחזירה "כן" עבור סדרות אלו, השערתם מתחזקת, אך הם למעשה אינם לומדים דבר על החוק האמיתי.</p>

    <p><strong>סוד ההצלחה: חשיבה הפוכה!</strong> החוק האמיתי במשחק הזה היה פשוט להפליא (בדקו את הקוד או את תוצאת הניחוש האחרונה אם עדיין לא גיליתם! בדרך כלל בניסוי המקורי החוק היה: "כל שלושה מספרים בסדר עולה"). כדי לגלות אותו, לא מספיק לבדוק סדרות שאתם *חושבים* שמקיימות את החוק שלכם. הדרך היעילה היא דווקא לבדוק סדרות שאתם *חושבים* *שלא* מקיימות את ההשערה הראשונית שלכם, אך עשויות בכל זאת לקיים את החוק *האמיתי*. למשל, לבדוק סדרות כמו (1, 2, 3), (10, 15, 20) או אפילו (1, 100, 101).</p>

    <p><strong>הפרכה ככלי חשיבה:</strong> כדי להתגבר על הטיית האישוש, עלינו לאמץ גישה אקטיבית של חיפוש עדויות שיכולות *להפריך* (לשלול) את ההשערות שלנו, לא רק לאשש אותן. גישה זו, המכונה "עקרון ההפרכה" (Falsification) וקודמה על ידי הפילוסוף קרל פופר, היא יסוד חשוב במדע ובחשיבה ביקורתית.</p>

    <p>הטיית האישוש משפיעה עלינו בתחומים רבים בחיי היומיום – החל מדעות פוליטיות ותפיסות חברתיות, ועד להחלטות אישיות. מודעות לקיומה וניסיון אקטיבי לחפש עדויות סותרות יכולים לעזור לנו לגבש תפיסת עולם מדויקת ומאוזנת יותר.</p>
</div>

<style>
    /* Base Styles */
    body {
        font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.7;
        color: #333;
        max-width: 800px;
        margin: 20px auto;
        padding: 0 20px;
        background-color: #f4f7f6;
        direction: rtl;
        text-align: right;
        unicode-bidi: embed; /* Ensure correct handling of LTR elements like numbers */
    }

    h1, h2, h3 {
        color: #004085; /* Dark blue */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        margin-top: 0;
        font-size: 2em;
    }

    h2 {
         font-size: 1.7em;
         border-bottom: 2px solid #007bff;
         padding-bottom: 5px;
         margin-bottom: 20px;
    }

     h3 {
         font-size: 1.4em;
         color: #0056b3;
         margin-bottom: 10px;
    }

    p {
        margin-bottom: 15px;
    }

    /* Game Container */
    #game-container {
        background: linear-gradient(145deg, #ffffff, #e9f3f7);
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        border: 1px solid #d0e3e8;
    }

    .game-header {
        margin-bottom: 25px;
    }

    .game-section {
        background-color: #eef7fc;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        border: 1px solid #d0e3e8;
    }

    /* Sequence Display */
    .sequence-display {
        font-size: 1.8em;
        font-weight: bold;
        color: #007bff; /* Primary blue */
        text-align: center;
        margin: 20px 0;
        padding: 15px;
        border: 2px dashed #007bff;
        border-radius: 8px;
        background-color: #cce5ff; /* Light blue background */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    /* Input Area */
    .input-area {
        display: flex;
        gap: 10px;
        margin-bottom: 10px; /* Adjusted for validation message */
        flex-direction: row-reverse; /* RTL */
        align-items: center;
    }

    .input-area input[type="text"] {
        flex-grow: 1;
        padding: 12px 15px;
        border: 1px solid #ccc;
        border-radius: 6px;
        font-size: 1.1em;
        text-align: right; /* RTL */
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

     .input-area input[type="text"]:focus {
        border-color: #007bff;
        box-shadow: 0 0 8px rgba(0, 123, 255, 0.2);
        outline: none;
    }

    .input-area button {
        padding: 12px 20px;
        background-color: #28a745; /* Success green */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .input-area button:hover {
        background-color: #218838; /* Darker green */
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
    }

    .input-area button:active {
        background-color: #1e7e34; /* Even darker green */
        transform: translateY(1px);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

     button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        background-color: #ccc;
        box-shadow: none;
        transform: none;
    }


    .validation-message {
        color: #dc3545; /* Danger red */
        font-size: 0.9em;
        min-height: 1em; /* Reserve space */
        margin-top: -5px; /* Pull up slightly */
        margin-bottom: 10px;
        text-align: right;
    }

    /* History Display */
    .history-display {
        border: 1px solid #b8daff; /* Light blue border */
        border-radius: 8px;
        padding: 10px;
        max-height: 200px; /* Increased height */
        overflow-y: auto;
        background-color: #ffffff;
        margin-bottom: 15px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .history-placeholder {
        text-align: center;
        color: #6c757d; /* Muted color */
        padding: 20px;
        font-style: italic;
    }

    .history-item {
        padding: 10px 0;
        border-bottom: 1px dashed #e9ecef; /* Light grey dash */
        display: flex;
        justify-content: space-between;
        align-items: center;
        animation: slideInFromRight 0.4s ease-out; /* Entry animation */
    }

    .history-item:first-child { /* Subtle highlight for the first item added */
         /* animation: pulseHighlight 1s ease-out; */ /* Maybe too distracting */
    }

    .history-item:last-child {
        border-bottom: none;
    }

    .history-item span {
        font-weight: normal;
        color: #555;
    }

     .history-item .sequence-text {
        font-weight: bold;
         color: #0056b3;
     }


    .history-item .result-icon {
        font-size: 1.3em;
        margin-left: 8px; /* Space between text and icon */
    }

    .history-item .result-yes .result-icon {
        color: #28a745; /* Success green */
    }

    .history-item .result-no .result-icon {
        color: #dc3545; /* Danger red */
    }

    /* Result Display (Guess) */
    #guess-result {
        margin-top: 15px;
        font-size: 1.2em;
        font-weight: bold;
        text-align: center;
        padding: 15px;
        border-radius: 8px;
        min-height: 1.5em; /* Reserve space */
        opacity: 0; /* Initially hidden */
        transition: opacity 0.5s ease-out, background-color 0.5s ease;
    }

    #guess-result.show {
         opacity: 1;
    }

    .result-correct {
        color: white;
        background-color: #28a745; /* Success green */
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.2);
    }

    .result-incorrect {
        color: white;
        background-color: #dc3545; /* Danger red */
         box-shadow: 0 4px 8px rgba(220, 53, 69, 0.2);
    }

    /* Hint Button */
     .hint-button {
        display: block;
        width: fit-content; /* Adjust width to content */
        margin: 15px auto 0; /* Center the button below history */
        padding: 8px 15px;
        background-color: #ffc107; /* Warning yellow */
        color: #343a40; /* Dark text */
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 0.95em;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
     }

     .hint-button:hover {
        background-color: #ffb300; /* Darker yellow */
         box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
     }

      .hint-button:active {
        background-color: #ffa000; /* Even darker yellow */
        transform: translateY(1px);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }


    /* Explanation Area */
    .explanation-toggle-button {
        display: block;
        width: 100%;
        padding: 15px 20px;
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.2em;
        text-align: center;
        margin-bottom: 25px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
    }

    .explanation-toggle-button:hover {
        background-color: #0056b3; /* Darker blue */
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.3);
    }

    .explanation-area {
        background-color: #e9f5ff; /* Light blue background */
        border-right: 5px solid #007bff; /* Blue accent border */
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        opacity: 0; /* Initially hidden */
        max-height: 0;
        overflow: hidden;
        transition: opacity 0.8s ease-out, max-height 0.8s ease-out;
    }

    .explanation-area.show {
        opacity: 1;
        max-height: 1000px; /* Sufficiently large value for smooth reveal */
    }

    .explanation-area p {
        margin-bottom: 15px;
        text-align: justify; /* Justify text for better readability */
    }

    .explanation-area strong {
        color: #0056b3; /* Match section header color */
    }


    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

     @keyframes slideInFromRight {
        from {
            opacity: 0;
            transform: translateX(20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    /*
    @keyframes pulseHighlight {
        0% { background-color: transparent; }
        50% { background-color: #fffacd; } /* Light yellow */
        100% { background-color: transparent; }
    }
    */

    /* Add RTL support for icons/elements that might flip */
     .history-item {
        flex-direction: row-reverse; /* Flip direction for RTL */
     }

     .history-item .result-icon {
        margin-right: 8px; /* Space between text and icon in RTL */
        margin-left: 0; /* Remove LTR margin */
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const initialSequenceDiv = document.getElementById('initial-sequence');
        const userSequenceInput = document.getElementById('user-sequence-input');
        const testSequenceButton = document.getElementById('test-sequence-button');
        const historyArea = document.getElementById('history-area');
        const historyPlaceholder = historyArea.querySelector('.history-placeholder');
        const inputValidationMessageDiv = document.getElementById('input-validation-message');
        const userRuleGuessInput = document.getElementById('user-rule-guess-input');
        const guessRuleButton = document.getElementById('guess-rule-button');
        const guessResultDiv = document.getElementById('guess-result');
        const showExplanationButton = document.getElementById('show-explanation-button');
        const explanationDiv = document.getElementById('explanation');
        const hintButton = document.getElementById('hint-button');

        let testCount = 0; // Track number of tests for hint

        // Define the secret rule
        // Rule: Any three numbers in strictly increasing order
        const secretRule = (sequence) => {
            if (!Array.isArray(sequence) || sequence.length !== 3) {
                return false;
            }
            // Check if all elements are valid numbers and finite
            if (!sequence.every(num => typeof num === 'number' && isFinite(num))) {
                 return false;
            }
            // Check if they are strictly increasing
            return sequence[0] < sequence[1] && sequence[1] < sequence[2];
        };

        // Helper function to parse user input
        const parseSequenceInput = (inputString) => {
            const parts = inputString.split(',').map(s => s.trim());
            if (parts.length !== 3) {
                return null; // Needs exactly 3 parts
            }
            const numbers = parts.map(s => parseFloat(s));
            // Check if all parsed values are indeed numbers and not NaN
            if (numbers.some(isNaN)) {
                return null;
            }
            return numbers;
        };

        // Function to show validation message
        const showValidationMessage = (message) => {
            inputValidationMessageDiv.textContent = message;
            // Add a temporary class for styling if needed
            // inputValidationMessageDiv.classList.add('active');
        };

        // Function to clear validation message
        const clearValidationMessage = () => {
             inputValidationMessageDiv.textContent = '';
             // inputValidationMessageDiv.classList.remove('active');
        };


        // Handle testing a sequence
        testSequenceButton.addEventListener('click', () => {
            const inputString = userSequenceInput.value.trim();
            clearValidationMessage(); // Clear previous messages

            if (!inputString) {
                showValidationMessage('אנא הכנס סדרה לבדיקה (3 מספרים).');
                return;
            }

            const sequence = parseSequenceInput(inputString);

            if (sequence === null) { // parseSequenceInput now handles length and number check
                 showValidationMessage('פורמט קלט לא חוקי. אנא הכנס 3 מספרים מופרדים בפסיקים (לדוגמה: 3,6,9).');
                 return;
            }

            // Hide placeholder if visible
            if (historyPlaceholder) {
                historyPlaceholder.style.display = 'none';
            }

            const followsRule = secretRule(sequence);
            const resultText = followsRule ? 'כן' : 'לא';
            const resultClass = followsRule ? 'result-yes' : 'result-no';
            const resultIcon = followsRule ? '✓' : '✗'; // Using simple characters as icons

            const historyItem = document.createElement('div');
            historyItem.classList.add('history-item');
            historyItem.innerHTML = `
                <span class="sequence-text">${inputString}</span>
                <span>מקיימת את החוק? <span class="${resultClass}"><span class="result-icon">${resultIcon}</span>${resultText}</span></span>
            `;
            historyArea.appendChild(historyItem);

            testCount++;
            // Show hint button after a few tests if not already visible
            if (testCount >= 3 && hintButton.style.display === 'none') {
                 hintButton.style.display = 'block';
                 // Add a subtle animation to the hint button
                  hintButton.style.animation = 'fadeIn 0.5s ease-out';
            }


            // Clear input after testing
            userSequenceInput.value = '';

            // Scroll history to bottom smoothly
            historyArea.scrollTo({
                 top: historyArea.scrollHeight,
                 behavior: 'smooth'
            });
        });

        // Handle guessing the rule
        guessRuleButton.addEventListener('click', () => {
            const userGuess = userRuleGuessInput.value.trim();
            const actualRuleExplanation = "החוקיות האמיתית הייתה: <strong>כל שלושה מספרים בסדר עולה</strong>.";

            // Clear previous result display state
            guessResultDiv.classList.remove('show', 'result-correct', 'result-incorrect');


            if (!userGuess) {
                guessResultDiv.textContent = 'אנא הכנס ניחוש לחוקיות כדי לבדוק אותו!';
                guessResultDiv.classList.add('show', 'result-incorrect'); // Use incorrect style for "please enter"
                return;
            }

            // Simple check for demonstration - does the guess contain words related to "increasing order"?
            const lowerGuess = userGuess.toLowerCase();
            const isGuessCorrect = lowerGuess.includes('סדר עולה') || lowerGuess.includes('עולה') || lowerGuess.includes('increasing') || lowerGuess.includes('גדול מהקודם'); // Added more terms

            if (isGuessCorrect) {
                guessResultDiv.innerHTML = `🎉 ניחוש <strong>נכון</strong>! ${actualRuleExplanation}`;
                guessResultDiv.classList.add('show', 'result-correct');
                 showExplanationButton.textContent = 'הסבר על ניסוי ואסון והטיית האישוש'; // Update button text
            } else {
                guessResultDiv.innerHTML = `😞 ניחוש <strong>שגוי</strong>. ${actualRuleExplanation}`;
                guessResultDiv.classList.add('show', 'result-incorrect');
                 showExplanationButton.textContent = 'הסבר על ניסוי ואסון והטיית האישוש'; // Update button text
            }
             // Disable guess button and input after one guess
             guessRuleButton.disabled = true;
             userRuleGuessInput.disabled = true;
             userRuleGuessInput.placeholder = 'אין אפשרות לנחש שוב.'; // Update placeholder

             // Ensure explanation button is visible after guess, if not already
             showExplanationButton.style.display = 'block'; // Assuming it might have been hidden before
        });


        // Handle showing/hiding the explanation with transition
        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.maxHeight === '0px' || explanationDiv.style.maxHeight === '';
            if (isHidden) {
                explanationDiv.classList.add('show');
                showExplanationButton.textContent = 'הסתר הסבר';
                 // Scroll to explanation area
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                explanationDiv.classList.remove('show');
                showExplanationButton.textContent = 'הצג הסבר על התופעה';
            }
        });

         // Handle hint button click
         hintButton.addEventListener('click', () => {
             alert('רמז: נסו לבדוק סדרות שאתם חושבים ש*לא* מקיימות את החוק שלכם. מה קורה אז?');
             hintButton.style.display = 'none'; // Hide hint after showing
         });


        // Allow pressing Enter in the input field to test
        userSequenceInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault(); // Prevent default form submission if any
                testSequenceButton.click();
            }
        });

         // Allow pressing Enter in the guess field to submit
         userRuleGuessInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter' && !guessRuleButton.disabled) {
                event.preventDefault();
                guessRuleButton.click();
            }
        });

        // Initial state setup: Hide explanation and guess result
        explanationDiv.style.maxHeight = '0px';
        explanationDiv.style.opacity = '0';
        guessResultDiv.style.opacity = '0';

         // Initial state for hint button
         hintButton.style.display = 'none'; // Ensure it's hidden initially

    });
</script>