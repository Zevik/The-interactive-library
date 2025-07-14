---
title: "אתגר החוקיות: האם תיפלו למלכודת הטיית האישוש?"
english_slug: confirmation-bias-game-discover-the-rule
category: "מדעי החברה / פסיכולוגיה"
tags: [הטיית אישוש, הטיה קוגניטיבית, חשיבה ביקורתית, שיטה מדעית, פתרון בעיות]
---
<p>ברוכים הבאים לאתגר החוקיות! נתונה לכם סדרת מספרים בודדת שמקיימת כלל סודי. משימתכם היא לגלות את הכלל הזה על ידי הצעת סדרות משלכם ובדיקה האם הן מתאימות. זה נשמע קל, נכון? האמת שרוב האנשים נופלים כאן למלכודת חשיבה פסיכולוגית נפוצה. האם אתם תצליחו להתגבר עליה ולגלות את החוקיות האמיתית?</p>

<div class="game-container" dir="rtl">
    <h2 class="game-title">צאו לדרך: גלו את הכלל הנסתר</h2>
    <p class="initial-series-text">הסדרה שבה התחלנו (היא מקיימת את הכלל!): <strong class="initial-series">2, 4, 6</strong></p>

    <div class="input-area">
        <label for="series-input" class="input-label">הציעו סדרה לבדיקה (שלושה מספרים מופרדים בפסיקים, לדוגמה: 1,2,3):</label>
        <div class="input-flex">
            <input type="text" id="series-input" class="series-input" placeholder="לדוגמה: 1,2,3">
            <button id="check-button" class="action-button">בדיקה</button>
        </div>
    </div>

    <div class="results-area">
        <h3>המסע שלכם: הסדרות שבדקתם</h3>
        <ul id="history-list" class="history-list">
            <!-- Initial series will be added dynamically by JS for consistent styling -->
        </ul>
    </div>

    <div class="guess-area">
        <h3>כשאתם מוכנים... גלו את החוקיות</h3>
        <p class="guess-text">ברגע שתלחצו, החוקיות האמיתית תיחשף ולא תוכלו לבדוק סדרות נוספות.</p>
        <button id="guess-button" class="action-button guess-button">חשפו את החוקיות!</button>
    </div>

    <div id="rule-reveal" class="rule-reveal hidden">
        <h3 class="reveal-title">⭐ החוקיות האמיתית נחשפת! ⭐</h3>
        <p id="actual-rule" class="actual-rule"></p>
        <p class="reflection-prompt">חשבו לרגע: האם החוקיות שגיליתם תואמת להיפותזה הראשונית שלכם? אילו סדרות בדקתם? אילו סדרות *לא* בדקתם?</p>
    </div>
</div>

<button id="show-explanation-button" class="action-button full-width hidden">הסבר לי הכל: הטיית האישוש והקשר למשחק</button>

<div id="explanation" class="explanation-area hidden" dir="rtl">
    <h2 class="explanation-title">הסבר מעמיק: הטיית האישוש, השיטה המדעית ומה שקרה במשחק</h2>

    <div class="explanation-section">
        <h3>מה ניסינו לעשות כאן?</h3>
        <p>במשחק הזה, קיבלתם רמז ראשון - הסדרה 2, 4, 6 - וידעתם שהיא מצייתת לכלל סודי. משימתכם הייתה לגלות את הכלל הזה בעצמכם, כמו בלשים או מדענים, על ידי הצגת סדרות נוספות ובדיקה האם הן גם מקיימות את הכלל. יכולתם לבדוק כמה סדרות שרציתם לפני שניסיתם לנחש את החוקיות.</p>
    </div>

    <div class="explanation-section">
         <h3>אז מה הייתה החוקיות האמיתית?</h3>
        <p class="actual-rule-explanation">החוקיות שהייתה מאחורי הקלעים פשוטה להפתיע: <strong>"שלושה מספרים עולים"</strong>. זה הכל! כל סדרה של שלושה מספרים שבה המספר השני גדול מהראשון, והשלישי גדול מהשני (כלומר: המספר הראשון < המספר השני < המספר השלישי) מקיימת את החוקיות הזו. דוגמאות: 1,2,3; 3,7,10; -5,-2,0; 1.5, 2.5, 3.5. גם הסדרה 2,4,6 כמובן עומדת בקריטריון הזה (2 < 4 < 6).</p>
        <p>אם החוקיות כה פשוטה, מדוע כל כך הרבה אנשים מתקשים לגלות אותה? כאן נכנסת לתמונה הטיה קוגניטיבית חזקה במיוחד...</p>
    </div>


    <div class="explanation-section">
        <h3>הכירו את הטיית האישוש (Confirmation Bias)</h3>
        <p>הטיית האישוש היא מנגנון פסיכולוגי שמשפיע על כולנו. זוהי הנטייה האוטומטית שלנו לחפש, לפרש, לזכור ולהעניק חשיבות יתרה למידע ש<strong>מאשש</strong> את האמונות, ההשערות או התיאוריות הקיימות שלנו, ובו זמנית להתעלם, להפחית בחשיבות או לשכוח מידע ש<strong>סותר</strong> אותן. זוהי הטיה עוצמתית שמעצבת את האופן שבו אנו תופסים את המציאות ומקבלים החלטות.</p>
    </div>

     <div class="explanation-section">
         <h3>איך הטיית האישוש שיחקה תפקיד במשחק?</h3>
        <p>כשראיתם את הסדרה הראשונה (2, 4, 6), המוח שלכם כמעט מיד ניסה לגבש היפותזה - השערה לגבי החוקיות. היפותזות נפוצות במקרה הזה הן: "מספרים זוגיים עולים בהפרש 2", "מספרים עולים בהפרש קבוע", "מספרים זוגיים עולים".</p>
        <p>תחת השפעת הטיית האישוש, הנטייה הטבעית היא לבדוק סדרות ש<strong>מאששות</strong> את ההיפותזה הראשונית שלכם. למשל, אם חשבתם שזה "מספרים זוגיים עולים בהפרש 2", סביר שבחנתם סדרות כמו 4,6,8 או 10,12,14. המערכת החזירה לכם "עובר בדיקה" (כי הן באמת מקיימות את הכלל הרחב "שלושה מספרים עולים"), וכל בדיקה כזו רק <strong>חיזקה</strong> אתכם באמונה שההיפותזה הצרה שלכם נכונה. גם אם היא לא!</p>
        <p>מה שרוב האנשים פחות נוטים לעשות, בגלל אותה הטיה, הוא לבדוק סדרות שיכולות <strong>להפריך</strong> את ההיפותזה הראשונית. למשל, לבדוק סדרה כמו 3,5,7 (עולה בהפרש 2, אבל לא זוגית) או 1,2,3 (עולה, אבל לא בהפרש 2). סדרות אלו היו עוברות בדיקה גם הן, והיו מאלצות אתכם לשנות או להרחיב את ההיפותזה שלכם.</p>
    </div>


    <div class="explanation-section">
        <h3>הקשר למדע: למה ניסיון הפרכה קריטי לגילוי ידע אמיתי?</h3>
        <p>המשחק הזה הוא דוגמה קלאסית לעיקרון מרכזי בפילוסופיה של המדע, שהדגיש הפילוסוף קרל פופר: חשיבות ה<strong>הפרכה (Falsification)</strong>. כדי לבדוק תיאוריה או היפותזה באופן יסודי ואמיתי, לא מספיק רק לחפש הוכחות שמאששות אותה. עלינו <strong>לחפש באופן פעיל</strong> עדויות שעלולות <strong>להפריך</strong> אותה. אם התיאוריה עומדת במבחן ואינה מופרכת למרות ניסיונות רבים להפריכה, רק אז הביטחון בה גובר (גם אז, לעולם לא נוכל להוכיח שהיא "נכונה" לחלוטין, רק שהיא "לא הופרכה עד כה").</p>
        <p>במשחק, האסטרטגיה היעילה ביותר לגילוי החוקיות הייתה דווקא לבדוק סדרות שלא "נראות" מתאימות להיפותזה הצרה הראשונית שלכם. לדוגמה, בדיקת 6,4,2 הייתה מניבה "לא עובר", ומפריכה מיידית היפותזה כמו "מספרים זוגיים עולים". בדיקת 3,5,7 או 1,2,3 הייתה מניבה "עובר", ומפריכה היפותזות כמו "רק מספרים זוגיים" או "עולה בהפרש קבוע 2".</p>
    </div>


    <div class="explanation-section">
        <h3>הטיית האישוש בחיים האמיתיים</h3>
        <p>הטיה זו אינה מוגבלת למשחקי חוקיות. היא משפיעה עלינו בכל תחומי החיים:</p>
        <ul>
            <li><strong>מדע ומחקר:</strong> חוקרים עלולים לפרש תוצאות ניסויים באופן שתומך בהשערת המחקר שלהם, תוך התעלמות מתוצאות שאינן נוחות. לכן השיטה המדעית שמה דגש רב על ביקורת עמיתים ושקיפות.</li>
            <li><strong>פוליטיקה ואמונה:</strong> אנשים נוטים לצרוך מקורות מידע וחדשות שתומכים בעמדותיהם הפוליטיות או אמונותיהם, ולהימנע או לבטל מידע שמאתגר אותן. כך נוצרות "בועות פילטר".</li>
            <li><strong>יחסים בין אישיים:</strong> אם יש לכם רושם שלילי ראשוני על אדם מסוים, אתם עשויים לשים לב רק לפעולות שמאששות את הרושם הזה, ולהתעלם מפעולות הסותרות אותו.</li>
             <li><strong>קבלה החלטות:</strong> בקבלת החלטות חשובות (קניית רכב, השקעה, בחירת קריירה), אנו עלולים לחפש רק מידע שתומך באפשרות המועדפת עלינו, ולהתעלם מחסרונותיה או מיתרונות של אפשרויות אחרות.</li>
        </ul>
        <p>הבנת הטיית האישוש היא צעד קריטי לפיתוח חשיבה ביקורתית ויכולת לקבל החלטות טובות יותר, על ידי הכרה בנטייה שלנו לחפש אישוש וניסיון מודע לחפש גם מידע שיכול להפריך את ההשערות שלנו.</p>
    </div>
</div>

<style>
    /* --- General Styles --- */
    body {
        font-family: 'Arial', sans-serif; /* Use a common system font */
        line-height: 1.7; /* Improved readability */
        margin: 0;
        background-color: #eef2f7; /* Light blue background */
        color: #333;
        padding: 20px;
        direction: rtl; /* Ensure RTL direction for Hebrew */
    }

    h1, h2, h3 {
        color: #0056b3; /* Primary blue color */
        margin-bottom: 15px;
        line-height: 1.4;
    }

    h2 {
        border-bottom: 2px solid #007bff; /* Stronger separator for main sections */
        padding-bottom: 10px;
        margin-top: 30px;
    }

    h3 {
        color: #007bff; /* Secondary blue */
        margin-bottom: 10px;
    }

    p {
        margin-bottom: 15px;
    }

    ul {
        margin-top: 10px;
        padding-right: 25px; /* Indent list */
        margin-bottom: 15px;
    }

    li {
        margin-bottom: 8px;
    }

    strong {
        color: #0056b3; /* Emphasize key terms */
    }

    /* --- Game Container Styles --- */
    .game-container {
        background-color: #ffffff; /* White background for game area */
        padding: 30px;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Stronger shadow */
        margin-bottom: 30px;
        border: 1px solid #cce5ff; /* Light blue border */
    }

     .game-title {
        text-align: center;
        margin-bottom: 25px;
        color: #004085; /* Darker blue */
        font-size: 1.8em;
    }

    .initial-series-text {
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 25px;
        padding: 10px;
        background-color: #e9ecef; /* Light grey background */
        border-radius: 6px;
    }

    .initial-series {
        font-size: 1.2em;
        color: #28a745; /* Green for the initial 'correct' series */
        font-weight: bold;
    }

    /* --- Input Area Styles --- */
    .input-area {
        margin-bottom: 25px;
        padding: 20px;
        background-color: #e0f7fa; /* Very light cyan */
        border-radius: 8px;
        border: 1px dashed #00acc1; /* Dashed border */
    }

    .input-label {
        font-weight: bold;
        display: block;
        margin-bottom: 10px;
        color: #0077c2; /* Teal-like color */
        font-size: 1.05em;
    }

    .input-flex {
        display: flex; /* Use flexbox for input and button */
        gap: 10px; /* Space between input and button */
    }

    .series-input {
        flex-grow: 1; /* Input takes available space */
        padding: 12px 15px;
        border: 1px solid #00bcd4; /* Cyan border */
        border-radius: 6px;
        font-size: 1.1em;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .series-input:focus {
        border-color: #007bff;
        box-shadow: 0 0 8px rgba(0, 123, 255, 0.25);
        outline: none;
    }

    /* --- Button Styles --- */
    .action-button {
        padding: 12px 25px;
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        flex-shrink: 0; /* Prevent button from shrinking */
    }

    .action-button:hover:not(:disabled) {
        background-color: #0056b3; /* Darker blue on hover */
    }

    .action-button:active:not(:disabled) {
        transform: scale(0.98); /* Slight press effect */
    }

    .action-button:disabled {
        background-color: #cccccc; /* Grey when disabled */
        cursor: not-allowed;
    }

    .guess-button {
         background-color: #ffc107; /* Warning yellow */
         color: #333;
         font-weight: bold;
         border: 1px solid #ffb300;
    }

     .guess-button:hover:not(:disabled) {
         background-color: #ffa000; /* Darker yellow */
     }

    .full-width {
        display: block;
        width: 100%;
        text-align: center;
        margin-top: 25px;
        background-color: #28a745; /* Success green */
         border-color: #218838;
         color: white;
    }
     .full-width:hover:not(:disabled) {
        background-color: #218838; /* Darker green */
     }


    /* --- Results Area (History) Styles --- */
    .results-area {
         margin-bottom: 25px;
    }
     .results-area h3 {
         border-bottom: 1px solid #eee; /* Lighter border */
         padding-bottom: 8px;
         margin-bottom: 15px;
         color: #0056b3;
     }

    .history-list {
        list-style: none;
        padding: 0;
         max-height: 200px; /* Limit height and add scroll */
         overflow-y: auto;
         border: 1px solid #eee;
         border-radius: 6px;
         background-color: #f8f9fa; /* Very light grey */
         padding: 5px;
    }

    .history-list li {
        padding: 10px 15px;
        margin-bottom: 8px;
        border-radius: 5px;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly below for slide-in */
        animation: fadeInSlideUp 0.4s ease forwards; /* Animation */
        border: 1px solid transparent; /* Default border */
        display: flex;
        justify-content: space-between;
        align-items: center;
         font-size: 1em;
    }

    .history-list li:nth-child(odd) { /* Alternate row colors */
        background-color: #e9ecef;
    }

    .history-list li:nth-child(even) {
        background-color: #f8f9fa;
    }

    .history-list li strong {
        font-weight: normal; /* Remove bold from the series text itself */
        color: #333;
    }

    .history-list li .result-text {
         font-weight: bold;
         padding: 3px 8px;
         border-radius: 4px;
         font-size: 0.9em;
         min-width: 80px; /* Ensure consistent button size */
         text-align: center;
    }

    .history-list li.pass .result-text {
        color: #155724; /* Dark green */
        background-color: #d4edda; /* Light green */
        border-color: #c3e6cb;
    }

    .history-list li.fail .result-text {
        color: #721c24; /* Dark red */
        background-color: #f8d7da; /* Light red */
        border-color: #f5c6cb;
    }

    /* Keyframe animation for history items */
    @keyframes fadeInSlideUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* --- Guess Area Styles --- */
    .guess-area {
         margin-bottom: 25px;
        padding: 20px;
        background-color: #fff3cd; /* Light yellow */
        border-radius: 8px;
        border: 1px solid #ffeeba; /* Yellow border */
        text-align: center; /* Center button */
    }
    .guess-area h3 {
         color: #856404; /* Dark yellow */
         margin-bottom: 10px;
    }
     .guess-text {
         margin-bottom: 20px;
         color: #856404;
     }

    /* --- Rule Reveal Styles --- */
    .rule-reveal {
        margin-top: 25px;
        padding: 25px;
        background-color: #d4edda; /* Success green background */
        border: 2px solid #28a745; /* Darker green border */
        color: #155724; /* Dark green text */
        border-radius: 8px;
        text-align: center;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px);
        animation: fadeInSlideUpReveal 0.6s ease forwards; /* Animation */
    }

     .reveal-title {
         color: #155724;
         margin-bottom: 15px;
         font-size: 1.5em;
         border-bottom: none; /* Remove border */
     }
    .actual-rule {
        font-size: 1.3em;
        font-weight: bold;
        color: #004085; /* Use a strong blue for the rule text itself */
         margin-bottom: 20px;
    }
    .reflection-prompt {
        font-style: italic;
        color: #1e7e34; /* Slightly darker green for prompt */
         margin-top: 15px;
         font-size: 0.95em;
    }

    /* Keyframe animation for rule reveal */
    @keyframes fadeInSlideUpReveal {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }


    /* --- Explanation Area Styles --- */
    .explanation-area {
        margin-top: 30px;
        padding: 30px;
        background-color: #ffffff; /* White background */
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        border: 1px solid #cce5ff;
    }

     .explanation-title {
         text-align: center;
         margin-bottom: 30px;
         font-size: 2em;
         color: #004085;
     }

    .explanation-section {
        margin-bottom: 25px;
        padding-bottom: 20px;
        border-bottom: 1px dashed #eee; /* Dashed separator */
    }
     .explanation-section:last-child {
         border-bottom: none; /* No border after the last section */
         padding-bottom: 0;
         margin-bottom: 0;
     }

    /* --- Utility Classes --- */
    .hidden {
        display: none;
    }

    /* --- Responsive Design (Basic) --- */
    @media (max-width: 600px) {
        .game-container, .explanation-area {
            padding: 20px;
        }
        .input-flex {
             flex-direction: column; /* Stack input and button on small screens */
        }
        .action-button {
            width: 100%; /* Full width buttons on small screens */
            margin-top: 10px;
        }
        .series-input {
            margin-left: 0; /* Remove margin */
        }
         .history-list li {
             flex-direction: column;
             align-items: flex-start;
             gap: 5px;
         }
          .history-list li .result-text {
             min-width: auto; /* Auto width */
             align-self: flex-end; /* Align result to the right */
         }
         .game-title {
             font-size: 1.5em;
         }
          .explanation-title {
              font-size: 1.8em;
          }
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const seriesInput = document.getElementById('series-input');
        const checkButton = document.getElementById('check-button');
        const historyList = document.getElementById('history-list');
        const guessButton = document.getElementById('guess-button');
        const ruleReveal = document.getElementById('rule-reveal');
        const actualRulePara = document.getElementById('actual-rule');
        const explanationDiv = document.getElementById('explanation');
        const showExplanationButton = document.getElementById('show-explanation-button');
        const gameContainer = document.querySelector('.game-container');
        const guessArea = document.querySelector('.guess-area');
        const inputArea = document.querySelector('.input-area');

        // The actual secret rule check function
        // Rule: Three increasing numbers (a < b < c)
        function checkRule(seriesArray) {
            // Ensure elements are numbers
            const nums = seriesArray.map(s => Number(s));
            // Check if they are valid numbers and increasing
            return seriesArray.length === 3 &&
                   !isNaN(nums[0]) && !isNaN(nums[1]) && !isNaN(nums[2]) &&
                   nums[0] < nums[1] && nums[1] < nums[2];
        }

        // Add initial series to history with specific styling/class
        function addInitialSeries() {
             const initialSeries = ['2', '4', '6'];
             const listItem = document.createElement('li');
             listItem.classList.add('pass'); // Add 'pass' class for styling
             listItem.innerHTML = `<strong>${initialSeries.join(', ')}</strong> <span class="result-text">עובר בדיקה</span>`;
             historyList.appendChild(listItem);
             // Trigger reflow to make animation work for the very first item
             void listItem.offsetWidth;
             listItem.style.opacity = 1;
             listItem.style.transform = 'translateY(0)';
        }

        // Call function to add initial series on load
        addInitialSeries();


        checkButton.addEventListener('click', () => {
            const inputValue = seriesInput.value.trim();

            if (!inputValue) {
                alert('אנא הכנס סדרה של מספרים מופרדים בפסיקים.');
                return;
            }

            const seriesArray = inputValue.split(',').map(s => s.trim());

            // Basic validation for exactly 3 items and they should look like numbers
            if (seriesArray.length !== 3 || seriesArray.some(s => s === '' || isNaN(Number(s)))) {
                 alert('אנא הכנס שלושה מספרים מופרדים בפסיקים (לדוגמה: 1,2,3).');
                 return;
            }

            const passesRule = checkRule(seriesArray);
            const resultText = passesRule ? 'עובר בדיקה' : 'לא עובר בדיקה';
            const resultClass = passesRule ? 'pass' : 'fail';

            const listItem = document.createElement('li');
            listItem.classList.add(resultClass); // Add class for pass/fail styling
            listItem.innerHTML = `<strong>${seriesArray.join(', ')}</strong> <span class="result-text">${resultText}</span>`; // Use innerHTML to add span for styling

            historyList.appendChild(listItem);

            // Animate the new list item (CSS keyframes handle the fade-in/slide-up)
            // No extra JS needed if CSS animation is set on list item creation

            seriesInput.value = ''; // Clear input field

             // Scroll history to bottom
             historyList.scrollTop = historyList.scrollHeight;
        });

        guessButton.addEventListener('click', () => {
            // Reveal the rule
            actualRulePara.textContent = 'החוקיות האמיתית היא: שלושה מספרים עולים.';
            ruleReveal.classList.remove('hidden');

            // Disable game controls
            seriesInput.disabled = true;
            checkButton.disabled = true;
            guessButton.disabled = true;
            inputArea.style.opacity = '0.6'; // Visual cue for disabled
            guessArea.style.opacity = '0.6'; // Visual cue for disabled


            // Show explanation button after a short delay (to allow rule reveal animation)
            setTimeout(() => {
                 showExplanationButton.classList.remove('hidden');
            }, 800); // Adjust delay as needed based on animation duration

             // Scroll to revealed rule smoothly
            ruleReveal.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });

        showExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.remove('hidden');
            showExplanationButton.classList.add('hidden'); // Hide the button after showing explanation
             // Scroll to explanation smoothly
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });

        // Allow pressing Enter in the input field to trigger check
         seriesInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter' && !checkButton.disabled) {
                event.preventDefault(); // Prevent default form submission if input is inside a form
                checkButton.click();
            }
        });

    });
</script>