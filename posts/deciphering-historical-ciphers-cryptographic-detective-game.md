---
title: "מסתורי צפנים: הרפתקה בלשית בעולם הקריפטוגרפיה"
english_slug: deciphering-historical-ciphers-cryptographic-detective-game
category: "מדעי המחשב"
tags: ["קריפטוגרפיה", "צפנים היסטוריים", "פיצוח צפנים", "ויז'נר", "אניגמה", "משחק בלשי"]
---
# מסתורי צפנים: הרפתקה בלשית בעולם הקריפטוגרפיה

מימי קדם ועד מלחמות העולם הגדולות, צפנים היו הלב הפועם של ריגול, אסטרטגיה צבאית ותקשורת סודית. אך איך הצליחו הבלשים הגדולים של ההיסטוריה לפצח את המסרים הסמויים הללו לפני המצאת המחשבים? הצטרפו למסע, הפכו לבלשי צפנים בעצמכם, ונסו לפענח מסר עתיק!

<div id="cipher-game-app" class="game-container">
    <div class="game-section">
        <h2 class="section-title"><span class="icon">🕵️‍♀️</span> המסר המסתורי:</h2>
        <div id="ciphertext-display" class="cipher-text fade-in"></div>
        <p class="section-description">זהו המסר המוצפן שהגיע אלינו ממעמקי הארכיון הסודי. הוא ממתין שתחשפו את סודו.</p>
    </div>

    <div class="game-section">
        <h2 class="section-title"><span class="icon">🛠️</span> ארגז הכלים של הבלש:</h2>

        <div class="tool-section">
            <h3 class="tool-title">כלי 1: ניתוח תדירויות אותיות <span class="icon">📊</span></h3>
            <p class="tool-description">כל שפה מכילה דפוסים סודיים. האותיות הנפוצות ביותר יכולות לשמש כנקודת פתיחה לפיצוח. השוו את תדירויות האותיות בטקסט המוצפן לתדירויות האותיות הנפוצות בעברית (טיפ: י, ו, א, ל, ה בדרך כלל מובילות!).</p>
            <div id="frequency-analysis" class="analysis-area">
                <div id="freq-chart" class="freq-chart">
                    <!-- Frequency bars will be injected here -->
                </div>
            </div>
        </div>

        <div class="tool-section">
            <h3 class="tool-title">כלי 2: מפצח ויז'נר <span class="icon">🔐</span></h3>
            <p class="tool-description">צופן ויז'נר מסתמך על 'מפתח' - רצף אותיות שחוזר על עצמו. נסו לנחש את המפתח הסודי. רמזים למפתח עשויים להגיע מניתוח התדירויות או מהקשר ההיסטורי!</p>
            <div class="decryption-area">
                <label for="vigenere-key-input">הכניסו מפתח (רצף אותיות בעברית):</label>
                <input type="text" id="vigenere-key-input" placeholder="לדוגמה: סוד או מפתח" dir="rtl" lang="he" autocomplete="off">
                <button id="decrypt-button" class="action-button">נסו לפענח!</button>
            </div>

            <div id="decrypted-output" class="cipher-text decrypted-text" dir="rtl" lang="he">
                <!-- Decrypted text will appear here -->
            </div>
            <div id="result-message" class="message-box"></div>
        </div>
    </div>
</div>

<style>
    /* כללי */
    #cipher-game-app {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        margin: 20px auto;
        padding: 30px;
        border: none;
        border-radius: 12px;
        background: linear-gradient(to bottom right, #eef2f7, #d8e1ed); /* Soft gradient */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Subtle shadow */
        max-width: 800px; /* Limit width for better readability */
    }

    .game-container {
        /* Add some flex/grid if sections need layout control */
        display: flex;
        flex-direction: column;
        gap: 25px; /* Space between main sections */
    }

    .game-section {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    .section-title, .tool-title {
        color: #2c3e50; /* Darker blue */
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.8em;
        border-bottom: 2px solid #3498db; /* Accent line */
        padding-bottom: 8px;
        display: flex;
        align-items: center;
    }

    .tool-title {
         font-size: 1.4em;
         border-bottom: 1px dashed #bdc3c7; /* Lighter accent */
    }

    .icon {
        margin-left: 10px;
        font-size: 1.2em; /* Adjust size relative to title */
    }

    .section-description, .tool-description {
        color: #555;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .cipher-text {
        border: 2px dashed #3498db; /* Vibrant blue dashed border */
        padding: 20px;
        margin-bottom: 20px;
        background-color: #ecf0f1; /* Light gray/blue background */
        font-family: 'Courier New', monospace;
        white-space: pre-wrap;
        word-break: break-word;
        font-size: 1.1em;
        color: #2c3e50;
        border-radius: 6px;
        overflow-x: auto; /* Prevent overflow on small screens */
    }

    .decrypted-text {
         background-color: #d5e5f0; /* Slightly different shade */
         min-height: 3em; /* Ensure space for output */
    }


    /* Tool-specific styles */
    .tool-section {
        margin-bottom: 25px;
        padding: 20px;
        border: 1px solid #e0e0e0; /* Light grey border */
        border-radius: 8px;
        background-color: #fcfcfc; /* White background */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05); /* Subtle inset shadow */
    }

    .analysis-area, .decryption-area {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px dashed #eee;
    }


    input[type="text"] {
        padding: 10px 12px;
        margin-left: 15px;
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        font-size: 1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        width: calc(100% - 150px); /* Adjust width */
        max-width: 300px; /* Max width for input */
    }

     input[type="text"]:focus {
         border-color: #3498db;
         box-shadow: 0 0 8px rgba(52, 152, 219, 0.3);
         outline: none; /* Remove default outline */
     }

    .action-button {
        padding: 12px 25px;
        background-color: #2ecc71; /* Green button */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .action-button:hover {
        background-color: #27ae60; /* Darker green */
        box-shadow: 0 5px 8px rgba(0, 0, 0, 0.15);
    }

    .action-button:active {
        transform: scale(0.98); /* Slight press effect */
    }

    .message-box {
        margin-top: 20px;
        padding: 15px;
        border-radius: 6px;
        font-weight: bold;
        text-align: center;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    .message-box.error {
        background-color: #fdedec; /* Light red */
        color: #c0392b; /* Dark red */
        border: 1px solid #e74c3c;
    }

    .message-box.success {
        background-color: #e8f8f5; /* Light green */
        color: #27ae60; /* Dark green */
         border: 1px solid #2ecc71;
        animation: tada 1s cubic-bezier(0.68, -0.55, 0.27, 1.55); /* Add success animation */
    }

    @keyframes tada {
      from { transform: scale3d(1, 1, 1); }
      10%, 20% { transform: scale3d(.9, .9, .9) rotate3d(0, 0, 1, -3deg); }
      30%, 50%, 70%, 90% { transform: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, 3deg); }
      40%, 60%, 80% { transform: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, -3deg); }
      to { transform: scale3d(1, 1, 1); }
    }


    /* Frequency Chart Styles */
    .freq-chart {
        display: flex;
        height: 120px; /* Taller bars */
        align-items: flex-end;
        border-bottom: 2px solid #bdc3c7;
        margin-top: 15px;
        padding-bottom: 8px;
        gap: 3px; /* More space */
        overflow-x: auto; /* Allow scrolling if too many bars */
        padding-left: 15px; /* Space for bars/labels */
         scrollbar-width: thin; /* Make scrollbar thinner */
         scrollbar-color: #3498db #ecf0f1; /* Custom scrollbar colors */
    }

    .freq-chart::-webkit-scrollbar {
        height: 8px;
    }

    .freq-chart::-webkit-scrollbar-track {
        background: #ecf0f1;
        border-radius: 10px;
    }

    .freq-chart::-webkit-scrollbar-thumb {
        background: #3498db;
        border-radius: 10px;
    }


    .freq-bar {
        flex-shrink: 0; /* Prevent bars from shrinking */
        width: 25px; /* Fixed width for bars */
        background-color: #3498db; /* Blue bars */
        position: relative;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        color: #2c3e50;
        font-size: 0.9em;
        text-align: center;
        cursor: pointer; /* Indicate interactivity */
        transition: background-color 0.3s ease, transform 0.3s ease, height 0.8s ease; /* Smooth transitions */
        border-top-left-radius: 3px;
        border-top-right-radius: 3px;
        min-height: 5px; /* Minimum height even if count is 0 */
    }

    .freq-bar:hover {
        background-color: #2980b9; /* Darker blue on hover */
        transform: translateY(-5px); /* Slight lift effect */
    }

     .freq-bar span {
        position: absolute;
        bottom: -25px; /* Position below the bar */
        font-weight: bold;
        font-size: 1em;
        color: #555;
        transition: color 0.3s ease;
    }

    .freq-bar:hover span {
         color: #000;
    }

    .freq-bar::before {
        content: attr(data-info); /* Use data-info for percentage/count */
        position: absolute;
        top: -30px; /* Position above the bar */
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(44, 62, 80, 0.9); /* Dark background */
        color: white;
        padding: 5px 8px;
        border-radius: 4px;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s ease, top 0.3s ease;
        font-size: 0.9em;
        z-index: 10; /* Ensure tooltip is above other elements */
    }

    .freq-bar:hover::before {
        opacity: 1;
        top: -40px; /* Move up slightly on hover */
    }

    .fade-in {
        animation: fadeIn 1.5s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

     /* Explanation Toggle Button */
    #toggle-explanation {
        display: block;
        margin: 30px auto 20px auto; /* More space around */
        padding: 15px 25px;
        font-size: 1.2em;
        background-color: #f39c12; /* Orange button */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
     #toggle-explanation:hover {
        background-color: #e67e22; /* Darker orange */
         box-shadow: 0 5px 8px rgba(0, 0, 0, 0.15);
    }
     #toggle-explanation:active {
        transform: scale(0.98); /* Slight press effect */
    }


    /* Explanation Section */
    #explanation {
        margin-top: 20px;
        padding: 30px;
        border: none;
        border-radius: 12px;
        background-color: #ecf0f1; /* Light background */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        display: none; /* Initially hidden */
        line-height: 1.7;
        color: #333;
         max-width: 800px;
         margin-left: auto;
         margin-right: auto;
    }

    #explanation h2 {
         color: #2c3e50;
         margin-bottom: 15px;
         font-size: 2em;
         border-bottom: 2px solid #bdc3c7;
         padding-bottom: 10px;
    }

     #explanation h3 {
         color: #34495e; /* Slightly lighter dark blue */
         margin-top: 25px;
         margin-bottom: 10px;
         font-size: 1.5em;
         border-bottom: 1px dashed #bdc3c7;
         padding-bottom: 5px;
     }


    #explanation p {
        margin-bottom: 15px;
        line-height: 1.7;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 25px; /* Hebrew list style */
        list-style-type: disc; /* Use discs */
    }

    #explanation li {
        margin-bottom: 10px;
    }

    #explanation strong {
        color: #2c3e50; /* Emphasize key terms */
    }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        #cipher-game-app, #explanation {
            padding: 20px;
        }
        .section-title {
            font-size: 1.6em;
        }
         .tool-title {
             font-size: 1.3em;
         }
        .action-button {
            width: 100%;
            margin-top: 15px;
        }
        input[type="text"] {
            width: calc(100% - 24px); /* Full width minus padding */
             margin-left: 0;
             margin-bottom: 15px;
             display: block; /* Stack input and button */
             max-width: none;
        }
         .decryption-area label {
             display: block;
             margin-bottom: 5px;
         }
        .freq-chart {
            height: 100px;
        }
        .freq-bar {
             width: 20px; /* Slightly thinner bars */
         }
         .freq-bar span {
             bottom: -20px;
             font-size: 0.9em;
         }
         .freq-bar::before {
             top: -25px;
             font-size: 0.8em;
         }
          .freq-bar:hover::before {
             top: -35px;
         }
        #toggle-explanation {
            font-size: 1em;
            padding: 12px 20px;
        }
    }

</style>

<button id="toggle-explanation">למדו עוד: מבט מעמיק על עולם הצפנים ההיסטוריים</button>

<div id="explanation">
    <h2>הסבר: צלילה לעומק עולם הצפנים ההיסטוריים</h2>

    <h3>מהי הצפנה ולמה היא הייתה כה חשובה?</h3>
    <p><strong>הצפנה</strong> היא אמנות הפיכת מידע לקוד סודי שרק הנמען המיועד יכול לקרוא. לאורך ההיסטוריה, היכולת לשלוח ולקבל מסרים סודיים שינתה את מהלך הקרבות, השפיעה על החלטות פוליטיות גורליות, ואף הכריעה מלחמות. ממגילות עתיקות במצרים ועד מכונות מסתוריות כמו האניגמה, הצפנה הייתה כלי הכרחי למי שהיה לו מידע חשוב להסתיר.</p>

    <h3>צפנים קלאסיים: מהקל למורכב</h3>
    <p>הצפנים הראשונים היו פשוטים יחסית. <strong>צופן החלפה פשוט</strong> (כמו צופן קיסר המפורסם) פשוט החליף כל אות באות אחרת באופן קבוע. למשל, כל א' הפכה ל-ד', כל ב' ל-ה', וכן הלאה. זה נשמע בטוח, אך מספיק טקסט מוצפן מאפשר להשתמש בשיטה גאונית: <strong>ניתוח תדירויות</strong>. מכיוון שגם בשפה מוצפנת תדירויות האותיות המקוריות נשמרות (האות הכי נפוצה בטקסט המוצפן היא כנראה ההצפנה של האות הכי נפוצה בשפת המקור), ניתן "לשבור" צפנים כאלה בקלות יחסית על ידי ספירת האותיות.</p>

    <p><strong>צופן ויז'נר</strong> עלה מדרגה. במקום החלפה אחת קבועה, הוא השתמש בסדרה של החלפות, המשתנות בהתאם ל"מפתח" - מילה או ביטוי סודי. כל אות בטקסט המקור הוצפנה באמצעות "הסטה" באלפבית, כשההסטה נקבעה על ידי האות המקבילה במפתח (שחוזר על עצמו). כך, אותה אות בטקסט המקור יכלה להיות מוצפנת לאותיות שונות בטקסט המוצפן, מה שהפך את ניתוח התדירויות הפשוט לבלתי יעיל. במשך מאות שנים הוא נחשב ל"בלתי ניתן לפיצוח" ("le chiffre indéchiffrable").</p>

    <h3>פיצוח ויז'נר: האשליה נשברת</h3>
    <p>האשליה של ויז'נר נשברה בזכות תובנות מתמטיות. השיטה המרכזית לפיצוח היא מציאת אורך המפתח. <strong>מבחן קסיסקי</strong> הוא טכניקה קלאסית שמזהה רצפים חוזרים בטקסט המוצפן. אם אותו רצף הופיע בטקסט המקור והוצפן עם אותה סדרה של אותיות מהמפתח, המרחק ביניהם יהיה כפולה של אורך המפתח. לאחר שמוצאים את אורך המפתח (נניח N), ניתן לפצל את הטקסט המוצפן ל-N "תת-טקסטים". כל תת-טקסט למעשה הוצפן בצופן החלפה פשוט (כי הוא מוצפן תמיד עם אותה אות מהמפתח)! עכשיו, ניתן להשתמש בניתוח תדירויות על כל אחד מהתת-טקסטים הללו בנפרד כדי לחשוף את ההחלפה המתאימה, ודרכה - את אות המפתח המתאימה.</p>

    <h3>המעבר לעידן המכונות והמחשבים</h3>
    <p>במאה ה-20, מכונות הצפנה כמו <strong>האניגמה</strong> הגרמנית הביאו את הקריפטוגרפיה הקלאסית לשיאה. מכונות אלו יצרו החלפות מורכבות שהשתנו בכל אות, מה שהפך פיצוח ידני לבלתי אפשרי. פיצוח האניגמה, מאמץ משותף שכלל גאונים כמו אלן טיורינג ושימוש בטכניקות מתמטיות מתקדמות ובמכונות חישוב ראשוניות (כמו הקולוסוס), היה הישג קריפטוגרפי אדיר שנחשב לאחד הגורמים המרכזיים לקיצור מלחמת העולם השנייה.</p>

    <p>כיום, הקריפטוגרפיה המודרנית נשענת על עקרונות מתמטיים מורכבים בהרבה (כמו תורת המספרים ואלגוריתמים קשים לפתרון חישובי) ולא על החלפות פשוטות. צפנים מודרניים (כמו AES, RSA) מאבטחים את התקשורת הדיגיטלית שלנו בכל רגע, והם חסינים בפני השיטות הקלאסיות של ניתוח תדירויות ומבחן קסיסקי. המעבר הזה הפך את עולם אבטחת המידע למורכב ובטוח פי כמה.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const ciphertextDisplay = document.getElementById('ciphertext-display');
        const freqChart = document.getElementById('freq-chart');
        const keyInput = document.getElementById('vigenere-key-input');
        const decryptButton = document.getElementById('decrypt-button');
        const decryptedOutput = document.getElementById('decrypted-output');
        const resultMessage = document.getElementById('result-message');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');

        // Hebrew alphabet - ensure consistent order
        const alphabet = "אבגדהוזחטיכלמנסעפצקרשת"; // 22 letters
        const alphabetMap = {};
        alphabet.split('').forEach((letter, index) => {
            alphabetMap[letter] = index;
        });

        // --- Game Setup ---
        // Use a more "historic" or intriguing original message
        const originalMessage = "הניצחון שייך למי שמפצח את המסר בטרם עת";
        // Use a slightly longer, but findable key related to the message or context
        const secretKey = "פיצוח"; // Key related to the message
        let ciphertext = "";
        // Normalize message to contain only Hebrew letters for encryption
        const normalizedMessage = originalMessage.split('').filter(char => alphabetMap[char] !== undefined).join('');

        // Encrypt using Vigenère
        for (let i = 0; i < normalizedMessage.length; i++) {
            const messageChar = normalizedMessage[i];
            const keyChar = secretKey[i % secretKey.length];

            const messageIndex = alphabetMap[messageChar];
            const keyIndex = alphabetMap[keyChar];

            // Check if characters are in the Hebrew alphabet map
            if (messageIndex !== undefined && keyIndex !== undefined) {
                const encryptedIndex = (messageIndex + keyIndex) % alphabet.length;
                ciphertext += alphabet[encryptedIndex];
            }
             // If the character wasn't in the normalized message, it's ignored.
             // If we normalized differently, we'd handle non-alphabet chars here.
        }

        ciphertextDisplay.textContent = ciphertext;

        // --- Frequency Analysis Tool ---
        function analyzeFrequency(text) {
            const frequency = {};
            for (const char of alphabet) {
                frequency[char] = 0;
            }
            let totalLetters = 0;
            for (const char of text) {
                if (alphabetMap[char] !== undefined) {
                    frequency[char]++;
                    totalLetters++;
                }
            }

            const freqData = Object.keys(frequency).map(char => ({
                char: char,
                count: frequency[char],
                percentage: totalLetters > 0 ? (frequency[char] / totalLetters) * 100 : 0
            })).sort((a, b) => alphabet.indexOf(a.char) - alphabet.indexOf(b.char)); // Sort by alphabet order for chart consistency

            return freqData;
        }

        function displayFrequency(freqData) {
            freqChart.innerHTML = ''; // Clear previous chart
            const maxCount = Math.max(...freqData.map(item => item.count));
            const minHeight = 5; // Minimum height for a bar (in px or percentage)

            freqData.forEach(item => {
                const bar = document.createElement('div');
                bar.classList.add('freq-bar');
                 // Calculate height: scale relative to max, ensure min height
                const barHeightPercentage = maxCount > 0 ? (item.count / maxCount) * (100 - minHeight/1.2) + minHeight/1.2 : minHeight/1.2; // Scale between minHeight and 100%
                bar.style.height = `${barHeightPercentage}%`;
                bar.setAttribute('data-count', item.count);
                bar.setAttribute('data-info', `${item.char}: ${item.count} (${item.percentage.toFixed(1)}%)`); // Info for tooltip

                const span = document.createElement('span');
                span.textContent = item.char;
                bar.appendChild(span);

                freqChart.appendChild(bar);

                // Optional: Add animation delay for staggered effect
                // bar.style.animationDelay = `${Math.random() * 0.5}s`;
            });

            // Trigger bar height animation after they are added to the DOM
            setTimeout(() => {
                 freqChart.querySelectorAll('.freq-bar').forEach(bar => {
                    // Force reflow to ensure transition works on initial height
                    // bar.offsetHeight;
                     // Height is already set, CSS transition handles it.
                 });
            }, 10); // Small delay
        }

        const ciphertextFreq = analyzeFrequency(ciphertext);
        displayFrequency(ciphertextFreq);

        // --- Decryption Tool (Vigenère) ---
        function decryptVigenere(text, key) {
            let decryptedText = "";
            const normalizedKey = key.trim().toUpperCase().split('').filter(char => alphabetMap[char] !== undefined).join(''); // Normalize and validate key
            if (normalizedKey.length === 0) {
                return "הכניסו מפתח תקין (אותיות בעברית).";
            }

            for (let i = 0; i < text.length; i++) {
                const textChar = text[i];
                // Cycle through the normalized key
                const keyChar = normalizedKey[i % normalizedKey.length];

                const textIndex = alphabetMap[textChar];
                const keyIndex = alphabetMap[keyChar];

                if (textIndex !== undefined && keyIndex !== undefined) {
                    // Vigenère decryption formula: (C - K) mod N
                    // Ensure result is non-negative: (C - K + N) mod N
                    const decryptedIndex = (textIndex - keyIndex + alphabet.length) % alphabet.length;
                    decryptedText += alphabet[decryptedIndex];
                } else {
                     // This case shouldn't happen if ciphertext only contains alphabet chars
                     // but good practice to handle potential non-alphabet chars
                     decryptedText += textChar; // Keep original char if not in alphabet
                }
            }
             // Add spaces back *roughly* based on original message length sections.
             // This is a very simple approximation for display.
             const chunkSize = Math.ceil(normalizedMessage.length / (originalMessage.split(' ').length || 1)) + 2; // Estimate chunk size
             let formattedDecrypted = "";
             for(let i = 0; i < decryptedText.length; i += chunkSize) {
                 formattedDecrypted += decryptedText.substring(i, i + chunkSize) + " ";
             }
             return formattedDecrypted.trim(); // Trim trailing space

        }

        decryptButton.addEventListener('click', () => {
            const userKey = keyInput.value.trim().toUpperCase(); // Normalize input key
            const decryptedAttempt = decryptVigenere(ciphertext, userKey);
            decryptedOutput.textContent = decryptedAttempt;

            // Check if the decryption is correct by comparing the normalized decrypted text
            // with the normalized original message. This avoids issues with spaces/punctuation.
            const normalizedDecryptedAttempt = decryptedAttempt.split('').filter(char => alphabetMap[char] !== undefined).join('');
            const isCorrect = normalizedDecryptedAttempt === normalizedMessage;


            if (userKey.length === 0 || userKey.split('').filter(char => alphabetMap[char] !== undefined).join('').length === 0) {
                 resultMessage.textContent = "בלש יקר, עליך להכניס מפתח (אותיות בעברית) כדי לנסות לפענח!";
                 resultMessage.className = 'message-box error'; // Reset classes
            } else if (isCorrect) {
                 resultMessage.textContent = `משימה הושלמה! המפתח "${secretKey}" נכון! המסר המקורי הוא: ${originalMessage}`; // Show original message on success
                 resultMessage.className = 'message-box success'; // Reset classes
                 resultMessage.classList.add('success'); // Add success class for animation/styling
            } else {
                 resultMessage.textContent = "המפתח אינו נכון. המסר עדיין מוצפן. נסו שנית או השתמשו בכלים האחרים למציאת רמזים!";
                 resultMessage.className = 'message-box error'; // Reset classes
                 resultMessage.classList.add('error'); // Add error class for styling
            }
        });

         // Allow pressing Enter in key input
         keyInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault(); // Prevent form submission
                decryptButton.click();
            }
         });


        // --- Explanation Toggle ---
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר פרטים על עולם הצפנים' : 'למדו עוד: מבט מעמיק על עולם הצפנים ההיסטוריים';
             // Optional: Scroll to explanation if showing it
             if (isHidden) {
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

         // Initialize explanation as hidden on page load
         explanationDiv.style.display = 'none';
    });
</script>
```