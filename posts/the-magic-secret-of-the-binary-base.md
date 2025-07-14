---
title: "הסוד הקסום של הבסיס הבינארי"
english_slug: the-magic-secret-of-the-binary-base
category: "טכנולוגיה / מדעי המחשב"
tags: בסיס בינארי, בסיס עשרוני, המרה, ספרות, קוד בינארי, מחשבים, מתמטיקה
---
# הסוד הקסום של הבסיס הבינארי

איך מחשבים, המבינים רק 'דלוק' ו-'כבה' (או '0' ו-'1'), מצליחים לבצע חישובים מסובכים ולהבין מספרים אדירים? התשובה מסתתרת בשיטת ספירה שונה בתכלית מזו שאנו מכירים. בואו נצלול פנימה ונגלה את הכוח הטמון ב-0 וב-1!

<div class="binary-app-container">
    <h2 class="app-title">בנה את המספר בעזרת 0 ו-1</h2>
    <div class="target-number">
        <span class="label">המספר המסתורי:</span> <span id="targetDecimal" class="number-value">?</span>
    </div>
    <div class="binary-bits" id="binaryBitsContainer">
        <!-- Binary bits (the interactive building blocks) will be added here by JS -->
    </div>
    <div class="current-sum">
        <span class="label">הקסם שבנית:</span> <span id="currentDecimalSum" class="number-value">0</span>
    </div>
    <div class="feedback" id="feedbackMessage">
        לחץ על הלבנים למעלה כדי לבנות את המספר
    </div>
    <button id="newNumberButton" class="app-button">נסה מספר אחר!</button>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #28a745; /* Green */
        --warning-color: #ffc107; /* Yellow */
        --danger-color: #dc3545; /* Red */
        --info-color: #6c757d; /* Grey */
        --background-color: #f8f9fa; /* Light grey */
        --card-background: #ffffff; /* White */
        --border-color: #e9ecef; /* Lighter grey */
        --text-color: #343a40; /* Dark grey */
        --font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .binary-app-container {
        direction: rtl;
        font-family: var(--font-family);
        background-color: var(--background-color);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        border: 1px solid var(--border-color);
        overflow: hidden; /* Needed for potential animations */
        position: relative;
    }

    .app-title {
        color: var(--primary-color);
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 1.8em;
        font-weight: bold;
        letter-spacing: 0.5px;
    }

    .target-number, .current-sum {
        font-size: 1.4em;
        margin-bottom: 15px;
        color: var(--text-color);
    }

    .target-number .number-value,
    .current-sum .number-value {
        font-weight: bold;
        color: var(--primary-color);
        font-size: 1.2em; /* Slightly larger number */
        display: inline-block; /* For potential animation */
        min-width: 30px; /* Prevent layout shift */
    }

    .target-number .label,
    .current-sum .label {
         font-size: 0.9em; /* Smaller label */
         color: #5a6268; /* Darker grey */
    }


    .binary-bits {
        display: flex;
        justify-content: center;
        gap: 12px; /* Increased gap */
        margin-bottom: 25px;
        flex-wrap: wrap;
        perspective: 1000px; /* For flip animation */
    }

    .binary-bit {
        width: 60px; /* Wider */
        height: 80px; /* Taller */
        border: 2px solid var(--border-color);
        border-radius: 8px; /* More rounded corners */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        user-select: none;
        font-size: 2.2em; /* Larger number */
        font-weight: bold;
        background-color: var(--card-background);
        color: var(--text-color);
        transition: all 0.3s ease-in-out, transform 0.1s ease-out; /* Smooth transitions */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        position: relative;
        transform-style: preserve-3d; /* For 3D flip */
    }

    .binary-bit .bit-value {
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         backface-visibility: hidden; /* Hide back during flip */
    }

     .binary-bit .power-of-2 {
        font-size: 0.8em; /* Slightly larger */
        font-weight: normal;
        color: var(--info-color); /* Grey */
        margin-top: 50px; /* Position below the number */
        position: absolute;
        bottom: 8px;
        left: 0;
        right: 0;
     }

    .binary-bit:hover {
        border-color: var(--primary-color);
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2); /* Blue shadow on hover */
    }

    .binary-bit.on {
        background: linear-gradient(135deg, var(--secondary-color), #218838); /* Gradient */
        color: white;
        border-color: var(--secondary-color);
        box-shadow: 0 4px 10px rgba(40, 167, 69, 0.3); /* Green shadow when on */
        transform: rotateY(180deg); /* Flip animation */
    }

    .binary-bit.on .bit-value {
         transform: translate(-50%, -50%) rotateY(180deg); /* Flip text back */
    }

    .binary-bit.on .power-of-2 {
        color: rgba(255, 255, 255, 0.8); /* Lighter color when on */
    }

     /* Animation for feedback messages */
    .feedback {
        font-size: 1.2em;
        min-height: 1.8em; /* Reserve more space */
        transition: color 0.4s ease-in-out, transform 0.4s ease-in-out, opacity 0.4s ease-in-out;
        opacity: 1;
        transform: translateY(0);
    }

    .feedback:empty {
        opacity: 0; /* Hide if empty */
    }

    .feedback.too-low {
        color: var(--warning-color);
        transform: translateY(-5px); /* Slight lift */
    }

    .feedback.too-high {
        color: var(--danger-color);
        transform: translateY(-5px); /* Slight lift */
    }

    .feedback.correct {
        color: var(--secondary-color);
        font-weight: bold;
        animation: pulse-glow 1.5s infinite ease-in-out; /* Winning animation */
    }

    @keyframes pulse-glow {
        0% { text-shadow: 0 0 5px rgba(40, 167, 69, 0.3); }
        50% { text-shadow: 0 0 15px rgba(40, 167, 69, 0.6); }
        100% { text-shadow: 0 0 5px rgba(40, 167, 69, 0.3); }
    }

    .app-button {
        padding: 12px 25px; /* More padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        margin-top: 25px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        transition: background-color 0.2s ease-in-out, transform 0.1s ease-out, box-shadow 0.2s ease-in-out;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
    }

    .app-button:hover {
        background-color: #0056b3; /* Darker blue */
        box-shadow: 0 5px 10px rgba(0, 123, 255, 0.3);
    }

    .app-button:active {
        transform: scale(0.98); /* Press effect */
    }


    .explanation-button {
        display: block;
        margin: 30px auto;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: var(--info-color);
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.2s ease-in-out;
    }

    .explanation-button:hover {
        background-color: #545b62;
    }

    #explanationContent {
        border-top: 1px dashed var(--border-color);
        padding-top: 25px;
        margin-top: 25px;
        text-align: right; /* Hebrew alignment */
        line-height: 1.7; /* Improved readability */
        color: var(--text-color);
    }

    #explanationContent h2 {
        color: var(--primary-color);
        margin-top: 20px;
        margin-bottom: 15px;
        font-size: 1.5em;
    }

    #explanationContent p {
        margin-bottom: 18px;
    }

    #explanationContent ul {
         margin-bottom: 18px;
         padding-right: 20px; /* Indent list */
    }

    #explanationContent li {
        margin-bottom: 10px;
    }

    #explanationContent strong {
        color: #000; /* Make strong text stand out */
    }

    /* Initially hide the explanation */
    #explanationContent {
        display: none;
    }
</style>

<button class="explanation-button" id="toggleExplanationButton">רוצה לדעת עוד? הצג הסבר מפורט</button>

<div id="explanationContent">
    <h2>מהי מערכת ספירה? הבסיס העשרוני (בסיס 10)</h2>
    <p>מערכת ספירה היא הדרך שבה אנו מייצגים מספרים. המערכת שאנו משתמשים בה כל יום היא ה"בסיס העשרוני" או "בסיס 10". היא משתמשת ב-10 ספרות קסומות (מ-0 עד 9). סוד הכוח של הבסיס העשרוני הוא שערכה של כל ספרה תלוי במיקום שלה! למשל, במספר 345, ה-'5' הוא 5 יחידות (5 כפול 10 בחזקת 0), ה-'4' הוא 4 עשרות (4 כפול 10 בחזקת 1), וה-'3' הוא 3 מאות (3 כפול 10 בחזקת 2). המספר כולו הוא פשוט הסכום: 300 + 40 + 5 = 345.</p>

    <h2>הבסיס הבינארי: העולם של 0 ו-1</h2>
    <p>בניגוד לבסיס העשרוני העשיר, הבסיס הבינארי (או בסיס 2) חי בעולם פשוט יותר – הוא משתמש בשתי ספרות בלבד: 0 ו-1. כל מספר, קטן כגדול, מיוצג באמצעות רצף ממושך של אפסים ואחדות. כל ספרה כזו בייצוג בינארי נקראת "ביט" (bit), קיצור קליט ל"binary digit".</p>

    <h2>למה דווקא 0 ו-1? הסוד של המחשבים</h2>
    <p>הסיבה שמחשבים "מדברים" בינארית היא פיזית לגמרי. מחשבים בנויים מרכיבים אלקטרוניים כמו טרנזיסטורים שיכולים להיות באחד משני מצבים יציבים בלבד: זרם עובר/לא עובר, מתח גבוה/נמוך, מצב מגנטי מסוים או ההפך. המצבים האלו מתאימים בול לייצוג שתי הספרות של הבסיס הבינארי - '0' ו-'1'. מצב אחד מייצג '0', והשני מייצג '1'. כל מה שקורה במחשב - גלישה באינטרנט, משחקים, מוזיקה, תמונות - מתורגם מאחורי הקלעים לרצפים ארוכים אינסופיים של אפסים ואחדות. קסם טכנולוגי!</p>

    <h2>כוח המיקום בבינארי: חזקות של 2 (1, 2, 4, 8...)</h2>
    <p>כמו בבסיס העשרוני, גם בבינארי, המיקום הוא הכול! רק שהפעם, המקומות מייצגים חזקות של 2, לא של 10:</p>
    <ul>
        <li>הספרה הימנית ביותר (הביט הכי פחות "משמעותי") מייצגת 2 בחזקת 0, שזה 1.</li>
        <li>הספרה הבאה משמאל מייצגת 2 בחזקת 1, שזה 2.</li>
        <li>הספרה הבאה משמאל מייצגת 2 בחזקת 2, שזה 4.</li>
        <li>הספרה הבאה משמאל מייצגת 2 בחזקת 3, שזה 8.</li>
        <li>וכן הלאה, הערכים רק מכפילים את עצמם: 16, 32, 64, 128, 256...</li>
    </ul>
    <p>רצף של 8 ביטים נקרא "בייט" (Byte), והוא יכול לייצג כל מספר מ-0 (00000000) ועד 255 (11111111).</p>

    <h2>משחק המרה: מעשרוני לבינארי</h2>
    <p>המשימה באפליקציה שלמעלה היא בדיוק זו: לקחת מספר עשרוני ולמצוא אילו "לבנים" (חזקות של 2) עליך להדליק (לשים עליהן '1') כדי שהסכום שלהן יהיה שווה למספר המטרה. זה כמו לבנות את המספר היעד באמצעות סכום של חזקות של 2 בלבד!</p>

    <h2>בואו נראה דוגמה: המספר 150</h2>
    <p>נניח שהמספר המסתורי הוא <strong>150</strong> (באמצעות 8 ביטים):</p>
    <ol>
        <li>החזקה הכי גדולה של 2 שקטנה או שווה ל-150 היא 128 (2 בחזקת 7). האם נשתמש ב-128? כן! אז הביט של ה-128 (השמאלי ביותר) יהיה '1'. נשאר לנו: 150 - 128 = 22.</li>
        <li>החזקה הבאה: 64. האם נשתמש ב-64? לא, כי 64 גדול מ-22. הביט של ה-64 יהיה '0'. נשאר 22.</li>
        <li>החזקה הבאה: 32. האם נשתמש ב-32? לא, גדול מ-22. הביט יהיה '0'. נשאר 22.</li>
        <li>החזקה הבאה: 16. האם נשתמש ב-16? כן! 16 קטן מ-22. הביט של ה-16 יהיה '1'. נשאר לנו: 22 - 16 = 6.</li>
        <li>החזקה הבאה: 8. האם נשתמש ב-8? לא, גדול מ-6. הביט יהיה '0'. נשאר 6.</li>
        <li>החזקה הבאה: 4. האם נשתמש ב-4? כן! 4 קטן מ-6. הביט של ה-4 יהיה '1'. נשאר לנו: 6 - 4 = 2.</li>
        <li>החזקה הבאה: 2. האם נשתמש ב-2? כן! בדיוק 2. הביט של ה-2 יהיה '1'. נשאר לנו: 2 - 2 = 0.</li>
        <li>החזקה האחרונה: 1. האם נשתמש ב-1? לא, כי כבר הגענו ל-0. הביט של ה-1 יהיה '0'.</li>
    </ol>
    <p>הרכבת בהצלחה את המספר הבינארי: 10010110! זהו הייצוג של 150 בבסיס בינארי.</p>

    <h2>ההמרה ההפוכה: מבינארי לעשרוני (קלה יותר!)</h2>
    <p>כדי לחזור מבינארי לעשרוני, פשוט הסתכל על המספר הבינארי וסכום את כל הערכים של החזקות של 2 שבמיקומים שבהם יש '1'.</p>
    <p>ניקח את 10010110 שקיבלנו. זוכרים את הערכים של המיקומים (מימין לשמאל): 1, 2, 4, 8, 16, 32, 64, 128?</p>
    <p>נחבר את הערכים רק עבור הביטים שדלקים ('1'):</p>
    <ul>
        <li>הביט של ה-1 (ימין) הוא '0' - לא מוסיפים.</li>
        <li>הביט של ה-2 הוא '1' - מוסיפים 2.</li>
        <li>הביט של ה-4 הוא '1' - מוסיפים 4.</li>
        <li>הביט של ה-8 הוא '0' - לא מוסיפים.</li>
        <li>הביט של ה-16 הוא '1' - מוסיפים 16.</li>
        <li>הביט של ה-32 הוא '0' - לא מוסיפים.</li>
        <li>הביט של ה-64 הוא '0' - לא מוסיפים.</li>
        <li>הביט של ה-128 (שמאל) הוא '1' - מוסיפים 128.</li>
    </ul>
    <p>הסכום הוא: 128 + 16 + 4 + 2 = 150. חזרנו למספר העשרוני המקורי!</p>
    <p>עכשיו שהבנת את הקסם, חזור לאפליקציה והפוך לאשף בינארי!</p>
</div>

<script>
    const powersOf2 = [128, 64, 32, 16, 8, 4, 2, 1];
    let targetDecimal = 0;
    let currentBinary = new Array(powersOf2.length).fill(0); // Array of 0s and 1s

    const targetDecimalEl = document.getElementById('targetDecimal');
    const binaryBitsContainerEl = document.getElementById('binaryBitsContainer');
    const currentDecimalSumEl = document.getElementById('currentDecimalSum');
    const feedbackMessageEl = document.getElementById('feedbackMessage');
    const newNumberButtonEl = document.getElementById('newNumberButton');
    const explanationContentEl = document.getElementById('explanationContent');
    const toggleExplanationButtonEl = document.getElementById('toggleExplanationButton');
    const appContainerEl = document.querySelector('.binary-app-container'); // Get the main container

    // Function to calculate the decimal value from the binary array
    function calculateDecimalSum() {
        let sum = 0;
        for (let i = 0; i < currentBinary.length; i++) {
            // Only add the power of 2 if the bit is 1
            if (currentBinary[i] === 1) {
                sum += powersOf2[i];
            }
        }
        return sum;
    }

    // Function to update the display (bits, sum, feedback)
    function updateDisplay() {
        const currentSum = calculateDecimalSum();
        currentDecimalSumEl.textContent = currentSum;

        // Remove all feedback classes first
        feedbackMessageEl.classList.remove('too-low', 'too-high', 'correct');
        appContainerEl.classList.remove('win-state'); // Remove win state from container


        if (currentSum < targetDecimal) {
            feedbackMessageEl.textContent = `צריך להוסיף קצת (${targetDecimal - currentSum} חסר...)`;
            feedbackMessageEl.classList.add('too-low');
        } else if (currentSum > targetDecimal) {
            feedbackMessageEl.textContent = `חצית את המספר! נסה להוריד (${currentSum - targetDecimal} יותר מדי...)`;
            feedbackMessageEl.classList.add('too-high');
        } else { // currentSum === targetDecimal
            feedbackMessageEl.textContent = 'מעולה! הצלחת לבנות את המספר! אתה אשף בינארי!';
            feedbackMessageEl.classList.add('correct');
             appContainerEl.classList.add('win-state'); // Add win state to container
             // Optionally disable clicks after correct answer for this number
             binaryBitsContainerEl.querySelectorAll('.binary-bit').forEach(bitEl => bitEl.style.pointerEvents = 'none');
        }
    }

    // Function to handle bit click
    function handleBitClick(index) {
         // Only allow clicking if we haven't won yet
         if (calculateDecimalSum() === targetDecimal) {
             return;
         }

        // Toggle the bit value (0 to 1, 1 to 0)
        currentBinary[index] = 1 - currentBinary[index];

        // Update the visual representation of the bit immediately
        const bitEl = binaryBitsContainerEl.children[index];
        const bitValueEl = bitEl.querySelector('.bit-value'); // Get the span holding the 0/1

        bitValueEl.textContent = currentBinary[index]; // Update the main number text
        bitEl.classList.toggle('on', currentBinary[index] === 1); // Toggle 'on' class

        // Update the sum and feedback after the click
        updateDisplay();
    }

    // Function to initialize or reset the game
    function initializeGame() {
        // Get a random number between 0 and 255
        targetDecimal = Math.floor(Math.random() * 256);
        targetDecimalEl.textContent = targetDecimal;

        // Reset binary array to all zeros
        currentBinary.fill(0);

        // Clear previous bits and create new ones with animations
        binaryBitsContainerEl.innerHTML = '';
        powersOf2.forEach((power, index) => {
            const bitEl = document.createElement('div');
            bitEl.classList.add('binary-bit');
            bitEl.dataset.index = index; // Store index

            // Create span for the 0/1 value
            const bitValueSpan = document.createElement('span');
            bitValueSpan.classList.add('bit-value');
            bitValueSpan.textContent = '0'; // Start with 0

            // Create span for the power of 2 label
            const powerSpan = document.createElement('span');
            powerSpan.classList.add('power-of-2');
            powerSpan.textContent = `( ${power} )`;

            bitEl.appendChild(bitValueSpan); // Add value span
            bitEl.appendChild(powerSpan); // Add power span

            // Add click listener using the index
            bitEl.addEventListener('click', () => handleBitClick(index));

            binaryBitsContainerEl.appendChild(bitEl);

             // Optional: Add a little staggered animation when creating
            bitEl.style.animation = `fade-in-up 0.5s ease-out ${index * 0.05}s forwards`;
            bitEl.style.opacity = 0; // Start hidden for animation
            bitEl.style.transform = 'translateY(20px)'; // Start slightly below

        });

         // Define the keyframes for the staggered animation
         const styleSheet = document.styleSheets[0];
         const fadeInUpKeyframes = `
             @keyframes fade-in-up {
                 to {
                     opacity: 1;
                     transform: translateY(0);
                 }
             }
         `;
         // Add keyframes only if they don't exist
         if (![].slice.call(styleSheet.cssRules).some(rule => rule.name === 'fade-in-up')) {
              styleSheet.insertRule(fadeInUpKeyframes, styleSheet.cssRules.length);
         }


        // Initial display update
        updateDisplay();

        // Enable bit clicks if they were disabled
        binaryBitsContainerEl.querySelectorAll('.binary-bit').forEach(bitEl => bitEl.style.pointerEvents = 'auto');

        // Reset feedback message text and class initially
        feedbackMessageEl.textContent = 'לחץ על הלבנים למעלה כדי לבנות את המספר';
        feedbackMessageEl.classList.remove('too-low', 'too-high', 'correct');
    }

    // Toggle explanation visibility
    toggleExplanationButtonEl.addEventListener('click', () => {
        const isHidden = explanationContentEl.style.display === 'none' || explanationContentEl.style.display === '';
        explanationContentEl.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButtonEl.textContent = isHidden ? 'הסתר הסבר מפורט' : 'רוצה לדעת עוד? הצג הסבר מפורט';

        // Optional: Scroll to the explanation if showing it
        if (isHidden) {
             explanationContentEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Add event listener for the new number button
    newNumberButtonEl.addEventListener('click', initializeGame);

    // Initialize the game when the page loads
    initializeGame();

</script>