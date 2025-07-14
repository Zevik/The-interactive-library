---
title: "מסע לבסיס בינארי"
english_slug: decimal-to-binary-converter
category: "טכנולוגיה / מדעי המחשב"
tags: [בינארי, עשרוני, מערכות ספרות, המרה, הדגמה אינטראקטיבית]
---
# ממיר מבסיס עשרוני לבסיס בינארי: צעד אחר צעד

המספרים שאנחנו משתמשים בהם ביום-יום הם בבסיס עשרוני (בסיס 10). לעומת זאת, המחשבים "מדברים" בשפה אחרת לגמרי: בסיס בינארי (בסיס 2). הבנת הקשר ביניהם היא סופר חשובה בעולם המחשוב!

הכלי האינטראקטיבי הזה יאפשר לך לחקור איך מספר עשרוני "מתפרק" ו"נבנה מחדש" כמספר בינארי, שלב אחרי שלב, בשיטת החסרת חזקות של 2. בוא נצא למסע הזה!

<div class="converter-container">
    <div class="input-area">
        <label for="decimalInput">בחר מספר עשרוני (0-255):</label>
        <input type="number" id="decimalInput" min="0" max="255" value="156">
        <button id="startConvertBtn" class="action-button start-button">התחל מסע!</button>
        <button id="resetBtn" class="action-button reset-button" style="display: none;">התחל מחדש</button>
    </div>

    <div class="visualization-area">
        <div class="status-area">
            <div id="currentNumberDisplay" class="status-display">
                נותר לבדוק: <span id="currentNumberValue" class="status-value"></span>
            </div>
             <div id="checkingPowerDisplay" class="status-display">
                בודקים את: <span id="checkingPowerValue" class="status-value"></span>
            </div>
        </div>

        <div id="powersOf2" class="powers-of-2-grid">
            <!-- Powers of 2 headers will be populated here -->
        </div>
        <div id="binaryDigits" class="binary-digits-grid">
            <!-- Binary digits placeholders will be populated here -->
        </div>
    </div>

    <div class="controls-area" style="display: none;">
         <button id="nextStepBtn" class="action-button step-button">השלב הבא</button>
    </div>

    <div id="binaryOutput" class="binary-output">
        תוצאה בינארית עד כה: <span id="binaryString"></span>
    </div>
     <div id="completionMessage" class="completion-message" style="display: none;">
         <p>🎉 כל הכבוד! המסע הסתיים בהצלחה! 🎉</p>
     </div>
</div>

<button id="toggleExplanationBtn" class="toggle-button">מה בעצם קורה פה? לחץ להסבר</button>
<div id="explanation" class="explanation-hidden">
    <h2>הסבר מעמיק: המרה מעשרוני לבינארי בשיטת ההחסרה</h2>
    <p>כדי להבין איך מספר עשרוני מיוצג בבינארי, נשתמש בשיטה שמבוססת על חזקות של 2. המספרים בבסיס בינארי בנויים מסכום של חזקות שונות של 2. למשל, המספר הבינארי 1011 הוא למעשה:</p>
    <p>$1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 = 1 \times 8 + 0 \times 4 + 1 \times 2 + 1 \times 1 = 8 + 0 + 2 + 1 = 11$ (בבסיס עשרוני).</p>
    <p>שיטת ההחסרה עובדת הפוך: אנו מנסים לראות אילו חזקות של 2 "נכנסות" במספר העשרוני שלנו. הנה התהליך, צעד אחר צעד:</p>
    <ol>
        <li>**התחל עם המספר העשרוני המקורי:** זה הסכום הכולל שעליך "לבנות" באמצעות חזקות של 2.</li>
        <li>**עבור על חזקות של 2 מהגבוהה לנמוכה:** עבור מספרים עד 255, החזקה הגבוהה ביותר היא $2^7 = 128$. החזקות יורדות עד $2^0 = 1$.</li>
        <li>**בדיקת החזקה הנוכחית:** שאל את עצמך: האם המספר העשרוני שנשאר גדול או שווה לחזקה הנוכחית של 2 שאותה אנו בודקים?</li>
        <li>**קבלת ספרה בינארית:**
            <ul>
                <li>**אם כן:** זה אומר שחזקה זו "נכנסת" במספר. לכן, הספרה הבינארית במקום המתאים (מקום החזקה הנוכחית) היא **1**. לאחר מכן, עליך "להשתמש" בחלק הזה של המספר על ידי **החסרת** החזקה הנוכחית מהמספר העשרוני שנשאר. זהו המספר החדש שנשאר לך לבדוק עם החזקות הבאות.</li>
                <li>**אם לא:** זה אומר שחזקה זו גדולה מדי ואינה נכנסת במספר שנשאר. לכן, הספרה הבינארית במקום המתאים היא **0**. המספר העשרוני שנשאר **אינו משתנה**.</li>
            </ul>
        </li>
        <li>**חזור על התהליך:** עבור לחזקה הבאה של 2 וחזור על שלבים 3 ו-4 עם המספר העשרוני המעודכן (או הלא-מעודכן).</li>
        <li>**סיום:** המשך כך עד שתבדוק את החזקה הנמוכה ביותר ($2^0 = 1$). רצף הספרות הבינאריות שאספת (מהחזקה הגבוהה לנמוכה) הוא ההצגה הבינארית של המספר המקורי!</li>
    </ol>
    <p>ההדגמה האינטראקטיבית למעלה מאפשרת לך לעבור על התהליך הזה צעד אחר צעד ולראות איך המספרים משתנים ואיך הספרות הבינאריות מתקבלות.</p>
</div>

<style>
    /* General Styling and Layout */
    .converter-container {
        direction: rtl;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 650px; /* Slightly wider */
        margin: 20px auto;
        padding: 30px; /* More padding */
        border-radius: 15px; /* More rounded corners */
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Stronger shadow */
        display: flex;
        flex-direction: column;
        gap: 25px; /* Increased gap */
        color: #333;
    }

    h1 {
         text-align: center;
         color: #004d40; /* Dark teal */
         margin-bottom: 20px;
         font-size: 2em;
    }

    .input-area {
        display: flex;
        align-items: center;
        justify-content: center; /* Center content */
        gap: 15px; /* Increased gap */
        padding-bottom: 15px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    }

    .input-area label {
        font-weight: bold;
        color: #00796b; /* Teal */
        font-size: 1.1em;
    }

    .input-area input[type="number"] {
        padding: 10px; /* More padding */
        border: 1px solid #00796b; /* Teal border */
        border-radius: 8px; /* More rounded */
        width: 100px; /* Wider input */
        text-align: center;
        font-size: 1.1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .input-area input[type="number"]:focus {
        border-color: #004d40; /* Darker teal on focus */
        box-shadow: 0 0 8px rgba(0, 121, 107, 0.3); /* Matching shadow */
        outline: none;
    }

    /* Action Buttons */
    .action-button {
        padding: 10px 20px;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        min-width: 120px; /* Consistent width */
        text-align: center;
    }

    .start-button {
        background-color: #4caf50; /* Green */
    }
    .start-button:hover {
        background-color: #388e3c; /* Darker green */
         box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    }

    .step-button {
         background-color: #2196f3; /* Blue */
    }
    .step-button:hover {
         background-color: #1976d2; /* Darker blue */
          box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    }

    .reset-button {
        background-color: #f44336; /* Red */
    }
     .reset-button:hover {
         background-color: #d32f2f; /* Darker red */
          box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
     }

    .action-button:disabled {
        background-color: #b0bec5; /* Light grey */
        cursor: not-allowed;
        opacity: 0.6;
        box-shadow: none;
    }

    /* Visualization Area */
    .visualization-area {
        background-color: #ffffff;
        padding: 20px; /* More padding */
        border-radius: 10px;
        border: 1px solid #e0f2f7; /* Light blue border */
        min-height: 200px; /* Ensure enough space */
        display: flex;
        flex-direction: column;
        gap: 20px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .status-area {
        display: flex;
        justify-content: space-around;
        margin-bottom: 15px;
        flex-wrap: wrap; /* Allow wrapping */
        gap: 10px;
    }

    .status-display {
        font-size: 1.2em;
        color: #00796b;
        min-width: 200px; /* Give status elements some width */
        text-align: center;
    }

    .status-value {
        font-weight: bold;
        color: #004d40; /* Dark teal */
    }

    /* Grid Layout for Powers and Digits */
    .powers-of-2-grid, .binary-digits-grid {
        display: grid;
        grid-template-columns: repeat(8, 1fr); /* 8 columns for 8 bits */
        gap: 8px; /* Gap between items */
        text-align: center;
    }

    .power-label, .binary-digit {
        padding: 8px 0; /* Padding inside */
        border-radius: 6px; /* Rounded corners */
        font-size: 0.95em;
        transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
        user-select: none; /* Prevent text selection */
    }

    .power-label {
        font-weight: bold;
        background-color: #e0f2f7; /* Light cyan */
        color: #00796b;
        border: 1px solid #b2ebf2;
    }

    .binary-digit {
        background-color: #ffffff;
        border: 1px dashed #b0bec5; /* Dashed light grey border */
        color: #546e7a; /* Greyish blue text */
        min-height: 1.5em; /* Ensure consistent height */
        display: flex; /* Center content */
        align-items: center;
        justify-content: center;
        font-size: 1.2em; /* Larger font for digits */
        font-weight: bold;
    }

    /* Animations and Highlight States */
    .power-label.highlight {
         background-color: #ffeb3b; /* Yellow for current check */
         color: #f57f17; /* Darker yellow text */
         transform: scale(1.1);
         box-shadow: 0 0 10px rgba(255, 235, 59, 0.7);
    }

     .power-label.used {
         background-color: #c8e6c9; /* Light green if used */
         color: #2e7d32;
     }

    .binary-digit.filled {
        background-color: #81c784; /* Light green if 1 */
        color: #1b5e20; /* Dark green text */
        border-color: #388e3c;
        animation: pulse 0.5s ease-out;
    }

     .binary-digit.zero {
         background-color: #ffccbc; /* Light red if 0 */
         color: #bf360c; /* Dark red text */
         border-color: #e64a19;
         animation: fadeIn 0.5s ease-out;
     }

     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.2); }
         100% { transform: scale(1); }
     }

     @keyframes fadeIn {
         0% { opacity: 0; }
         100% { opacity: 1; }
     }

    /* Output Area */
    .binary-output {
        text-align: center;
        font-size: 1.4em; /* Larger font */
        font-weight: bold;
        color: #004d40; /* Dark teal */
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid rgba(0, 0, 0, 0.1);
    }

    .binary-output span {
        color: #00796b; /* Teal */
    }

    .completion-message {
        text-align: center;
        font-size: 1.3em;
        color: #2e7d32; /* Dark green */
        font-weight: bold;
        margin-top: 15px;
        padding: 15px;
        background-color: #c8e6c9; /* Light green background */
        border-radius: 8px;
        border: 1px solid #a5d6a7;
    }

    /* Explanation Area */
    .toggle-button {
        display: block;
        margin: 25px auto; /* Increased margin */
        padding: 12px 25px; /* More padding */
        background-color: #0097a7; /* Cyan */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .toggle-button:hover {
        background-color: #006064; /* Darker cyan */
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .explanation-hidden {
        display: none;
    }

    .explanation-visible {
        direction: rtl;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 650px;
        margin: 20px auto;
        padding: 25px;
        border-radius: 12px;
        background-color: #e0f7fa; /* Light cyan background */
        border: 1px solid #b2ebf2;
        color: #004d40; /* Dark teal text */
        line-height: 1.7; /* Increased line height */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .explanation-visible h2 {
        color: #00796b; /* Teal */
        margin-top: 0;
        border-bottom: 2px solid #b2ebf2; /* Thicker border */
        padding-bottom: 12px;
        margin-bottom: 15px;
    }

     .explanation-visible p {
         margin-bottom: 12px;
     }

     .explanation-visible ul, .explanation-visible ol {
         margin-top: 15px; /* Increased margin */
         padding-right: 25px; /* More padding */
     }

     .explanation-visible li {
         margin-bottom: 10px; /* Increased margin */
         line-height: 1.6;
     }

     /* Responsive adjustments */
     @media (max-width: 700px) {
         .converter-container, .explanation-visible {
             margin: 15px;
             padding: 20px;
         }
         .input-area {
             flex-direction: column;
             gap: 10px;
         }
         .status-area {
             flex-direction: column;
             align-items: center;
             gap: 5px;
         }
          .status-display {
             min-width: unset;
             width: 100%;
          }
          .powers-of-2-grid, .binary-digits-grid {
             grid-template-columns: repeat(4, 1fr); /* 4 columns on smaller screens */
          }
     }

</style>

<script>
    const decimalInput = document.getElementById('decimalInput');
    const startConvertBtn = document.getElementById('startConvertBtn');
    const nextStepBtn = document.getElementById('nextStepBtn');
    const resetBtn = document.getElementById('resetBtn');
    const currentNumberValueSpan = document.getElementById('currentNumberValue');
    const powersOf2Div = document.getElementById('powersOf2');
    const binaryDigitsDiv = document.getElementById('binaryDigits');
    const checkingPowerValueSpan = document.getElementById('checkingPowerValue');
    const binaryStringSpan = document.getElementById('binaryString');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationDiv = document.getElementById('explanation');
    const controlsArea = document.querySelector('.controls-area');
    const completionMessageDiv = document.getElementById('completionMessage');

    // Powers of 2 from 2^7 down to 2^0 (for max 255)
    const powers = [128, 64, 32, 16, 8, 4, 2, 1];
    let currentDecimal = 0;
    let currentPowerIndex = 0;
    let binaryResultArray = [];

    // Function to initialize the visualization area
    function initializeVisualization() {
        powersOf2Div.innerHTML = '';
        binaryDigitsDiv.innerHTML = '';
        currentNumberValueSpan.textContent = '...';
        checkingPowerValueSpan.textContent = '...';
        binaryStringSpan.textContent = '';
        completionMessageDiv.style.display = 'none';

        powers.forEach(power => {
            const powerLabel = document.createElement('div');
            powerLabel.classList.add('power-label');
            powerLabel.textContent = power;
            powersOf2Div.appendChild(powerLabel);

            const binaryDigit = document.createElement('div');
            binaryDigit.classList.add('binary-digit');
            binaryDigitsDiv.appendChild(binaryDigit);
        });

        currentPowerIndex = 0;
        binaryResultArray = [];
        startConvertBtn.style.display = 'inline-block';
        resetBtn.style.display = 'none';
        controlsArea.style.display = 'none';
        nextStepBtn.disabled = false;
        decimalInput.disabled = false;
    }

    // Function to start the conversion process
    function startConversion() {
        let decimalNumber = parseInt(decimalInput.value);
        if (isNaN(decimalNumber) || decimalNumber < 0 || decimalNumber > 255) {
            alert('אוי! נא הכנס מספר שלם תקין בין 0 ל-255.');
            return;
        }

        currentDecimal = decimalNumber;
        initializeVisualization(); // Reset visualization before starting
        currentNumberValueSpan.textContent = currentDecimal;
        checkingPowerValueSpan.textContent = 'בוא נתחיל...';

        startConvertBtn.style.display = 'none';
        resetBtn.style.display = 'inline-block';
        controlsArea.style.display = 'block';
        decimalInput.disabled = true; // Disable input during conversion

        // Highlight the first power to check
        highlightPower(currentPowerIndex);
         checkingPowerValueSpan.textContent = powers[currentPowerIndex];
    }

    // Function to execute a single step of the conversion
    function performNextStep() {
        if (currentPowerIndex >= powers.length) {
            // Conversion is already complete
            return;
        }

        const currentPower = powers[currentPowerIndex];
        const powerLabel = powersOf2Div.children[currentPowerIndex];
        const binaryDigitElement = binaryDigitsDiv.children[currentPowerIndex];

        // Remove previous highlights (except for the current one)
        powersOf2Div.querySelectorAll('.power-label.highlight').forEach((el, index) => {
             if (index !== currentPowerIndex) el.classList.remove('highlight');
        });


        checkingPowerValueSpan.textContent = currentPower; // Confirm which power is being checked

        // Perform the check
        if (currentDecimal >= currentPower) {
            // Use this power
            binaryResultArray.push(1);
            binaryDigitElement.textContent = '1';
            binaryDigitElement.classList.add('filled');
            powerLabel.classList.add('used'); // Mark power as used

            // Show subtraction visually
            const previousDecimal = currentDecimal;
            currentDecimal -= currentPower;
            currentNumberValueSpan.textContent = `${previousDecimal} - ${currentPower} = ${currentDecimal}`;

        } else {
            // Don't use this power
            binaryResultArray.push(0);
            binaryDigitElement.textContent = '0';
            binaryDigitElement.classList.add('zero'); // Mark as zero

            // Show comparison visually
             currentNumberValueSpan.textContent = `${currentDecimal} < ${currentPower}`;
        }

         // Update binary output string
        binaryStringSpan.textContent = binaryResultArray.join('');

        // Move to the next step
        currentPowerIndex++;

        if (currentPowerIndex < powers.length) {
            // Highlight the next power for the next step
            highlightPower(currentPowerIndex);
            // Update checking power display for the *next* step, but only after a short delay
             setTimeout(() => {
                 checkingPowerValueSpan.textContent = powers[currentPowerIndex];
                  currentNumberValueSpan.textContent = currentDecimal; // Reset display after step calculation shown
             }, 1000); // Small delay for visual clarity
        } else {
            // Conversion is complete
            checkingPowerValueSpan.textContent = 'סיימנו!';
            currentNumberValueSpan.textContent = `נותר: ${currentDecimal}`; // Should be 0 if started < 256
            nextStepBtn.disabled = true;
            completionMessageDiv.style.display = 'block'; // Show completion message
            // Remove final highlight
             setTimeout(() => {
                 powersOf2Div.querySelectorAll('.power-label.highlight').forEach(el => el.classList.remove('highlight'));
             }, 1500);
        }
    }

    // Helper function to highlight a specific power label
    function highlightPower(index) {
         powersOf2Div.querySelectorAll('.power-label').forEach((el, i) => {
             el.classList.remove('highlight');
             if (i === index) {
                 el.classList.add('highlight');
             }
         });
    }


    // Event listeners
    startConvertBtn.addEventListener('click', startConversion);
    nextStepBtn.addEventListener('click', performNextStep);
    resetBtn.addEventListener('click', initializeVisualization);

    toggleExplanationBtn.addEventListener('click', () => {
        explanationDiv.classList.toggle('explanation-hidden');
        explanationDiv.classList.toggle('explanation-visible');
        if (explanationDiv.classList.contains('explanation-visible')) {
             toggleExplanationBtn.textContent = 'הסתר הסבר';
        } else {
             toggleExplanationBtn.textContent = 'מה בעצם קורה פה? לחץ להסבר';
        }
    });

    // Initialize on page load with default value
    document.addEventListener('DOMContentLoaded', () => {
         initializeVisualization();
         decimalInput.value = 156; // Set a default value
    });

</script>
---