---
title: "מתי ימי ההולדת נפגשים? סימולטור בעיית יום ההולדת"
english_slug: birthday-probability-simulator
category: "מדעים מדויקים / מתמטיקה"
tags: [סימולציה, אינטראקטיבי, מתמטיקה, סטטיסטיקה, הדמיה, בעיית יום ההולדת]
---
# מתי ימי ההולדת נפגשים? סימולטור בעיית יום ההולדת

האם ידעתם שלא צריך הרבה אנשים בחדר כדי שיהיה סיכוי מפתיע שלפחות לשניים מהם יש יום הולדת באותו יום? בואו נראה את זה קורה! לחצו על כפתור "הוסף משתתף" ובחנו איך ההסתברות עולה עם כל אדם חדש שמצטרף לקבוצה.

<div class="simulator-container">
    <div class="controls">
        <button id="addPersonBtn">הוסף משתתף</button>
        <button id="resetBtn">התחל סימולציה מחדש</button>
    </div>
    <div class="display-area">
        <div class="display-box">
            <span class="label">משתתפים בקבוצה:</span>
            <span id="peopleCount" class="value">0</span>
        </div>
        <div class="display-box">
            <span class="label">הסתברות למפגש יום הולדת:</span>
            <span id="probability" class="value">0.00%</span>
        </div>
        <div class="display-box match-status">
            <span class="label">סטטוס:</span>
            <span id="matchStatus" class="value">ממתינים למפגש...</span>
        </div>
    </div>
    <div id="peopleVisualContainer" class="people-visual-container">
        <!-- People divs will be added here -->
    </div>
     <div class="limit-message" id="limitMessage" style="display: none;">
        הגענו למספר המשתתפים המקסימלי (60). לחץ "התחל סימולציה מחדש" כדי לנסות שוב!
    </div>
</div>

<button id="toggleExplanationBtn" class="explanation-toggle-btn">מה עומד מאחורי התופעה הזו? (הצג הסבר)</button>

<div id="explanation" class="explanation" style="display: none;">
    <h2>הסבר: התובנה המפתיעה של בעיית יום ההולדת</h2>
    <p>בעיית יום ההולדת היא אחת התוצאות האינטואיטיביות פחות בתורת ההסתברות. היא עוסקת בסיכוי שלפחות לשניים מתוך קבוצה אקראית של אנשים יש יום הולדת באותו יום בשנה (בהנחה פשוטה של 365 ימים בשנה, התעלמות משנה מעוברת ותאריכים נדירים).</p>
    <p>ההפתעה נובעת מכך שרובנו נוטים לחשוב שהסיכוי הזה יהיה נמוך מאוד אלא אם כן מדובר בקבוצה ענקית, אולי אפילו בגודל של מספר ימי השנה (365). אולם, החישוב מגלה שהסיכוי עולה במהירות מסחררת גם בקבוצות קטנות יחסית.</p>
    <h3>איך מחשבים זאת?</h3>
    <p>כדי לחשב את ההסתברות שלפחות לשני אנשים יש יום הולדת משותף, קל יותר לחשב דווקא את ההסתברות ההפוכה: של **אף** שני אנשים אין יום הולדת משותף. אם יש N אנשים בקבוצה:</p>
    <ul>
        <li>לאדם הראשון יכול להיות כל יום הולדת (365 מתוך 365 אפשרויות).</li>
        <li>לאדם השני צריך להיות יום הולדת שונה מזה של הראשון (364 מתוך 365 אפשרויות).</li>
        <li>לאדם השלישי צריך להיות יום הולדת שונה משני הראשונים (363 מתוך 365 אפשרויות).</li>
        <li>וכן הלאה, עד האדם ה-N, שלו צריך להיות יום הולדת שונה מכל N-1 האנשים לפניו ((365 - N + 1) מתוך 365 אפשרויות).</li>
    </ul>
    <p>ההסתברות של**אף** שני אנשים אין יום הולדת משותף היא מכפלת ההסתברויות הללו:</p>
    <p class="math-formula">P(אין מפגש) = (365/365) * (364/365) * (363/365) * ... * ((365 - N + 1)/365)</p>
    <p>ולכן, ההסתברות של**לפחות** לשני אנשים יש יום הולדת משותף היא:</p>
    <p class="math-formula">P(יש מפגש) = 1 - P(אין מפגש)</p>
    <p>הסימולטור ממחיש באופן ויזואלי כיצד הסיכוי הזה מתקרב במהירות ל-50% עבור קבוצה של כ-23 אנשים בלבד, ומגיע לסיכוי גבוה מאוד (מעל 99%) בקבוצות של 50-60 אנשים. נסו בעצמכם!</p>
</div>

<style>
    /* Importing a clean, modern font */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #eef2f7; /* Soft background */
        color: #333;
        line-height: 1.7;
        padding: 20px;
        margin: 0;
    }

    h1, h2 {
        color: #0056b3; /* Deep blue */
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700;
    }

    h1 {
        font-size: 2em;
    }

    h2 {
        font-size: 1.5em;
        margin-top: 30px;
        border-bottom: 1px solid #007bff;
        padding-bottom: 10px;
    }

    p {
        margin-bottom: 1em;
    }

    ul {
        margin-bottom: 1em;
        padding-right: 20px;
    }

    .math-formula {
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        background-color: #f8f9fa;
        padding: 10px 15px;
        border-radius: 5px;
        overflow-x: auto; /* Scroll for long formulas */
        text-align: left;
        direction: ltr; /* Formulas are LTR */
    }

    .simulator-container {
        background-color: #ffffff; /* White background */
        border-radius: 15px;
        padding: 30px;
        margin: 20px auto;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* More prominent shadow */
        max-width: 850px;
        display: flex;
        flex-direction: column;
        align-items: center;
        border: 1px solid #dcdcdc;
    }

    .controls {
        margin-bottom: 25px;
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
        justify-content: center;
    }

    button {
        padding: 12px 25px;
        font-size: 1.1rem;
        color: #fff;
        background-color: #007bff; /* Primary blue */
        border: none;
        border-radius: 30px; /* Pill shape */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
        font-weight: 500;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    button:hover:not(:disabled) {
        background-color: #0056b3;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    button:active:not(:disabled) {
        transform: scale(0.98);
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
        box-shadow: none;
    }

    #resetBtn {
        background-color: #6c757d; /* Secondary grey */
    }
    #resetBtn:hover:not(:disabled) {
        background-color: #5a6268;
    }

    .explanation-toggle-btn {
        display: block;
        margin: 30px auto 20px;
        background-color: #28a745; /* Green for 'show explanation' */
        border-radius: 8px; /* Slightly less rounded */
        padding: 10px 20px;
        font-size: 1rem;
    }
     .explanation-toggle-btn:hover:not(:disabled) {
        background-color: #218838;
    }


    .display-area {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin-bottom: 25px;
        width: 100%;
    }

    .display-box {
        background-color: #e9f5ff; /* Light blue */
        border-radius: 10px;
        padding: 15px 20px;
        text-align: center;
        flex: 1;
        min-width: 180px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
        border: 1px solid #b3d7ff;
    }

    .display-box .label {
        display: block;
        font-size: 0.95rem;
        color: #555;
        margin-bottom: 5px;
        font-weight: 400;
    }

    .display-box .value {
        font-size: 1.6rem;
        font-weight: 700;
        color: #007bff; /* Primary blue */
        transition: color 0.3s ease, transform 0.3s ease;
        display: inline-block; /* Needed for transform */
    }

    .match-status .value {
        color: #ffc107; /* Warning yellow initially */
        font-size: 1.4rem; /* Slightly smaller */
    }

    .match-status.match-found .value {
        color: #dc3545; /* Danger red when match is found */
        font-size: 1.6rem;
        animation: pulse 1.5s infinite ease-in-out; /* Slower, smoother pulse */
    }

     @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.9; }
    }


    .people-visual-container {
        width: 100%;
        min-height: 150px; /* More initial height */
        border: 2px dashed #a0c0e0; /* Dashed border */
        border-radius: 10px;
        padding: 15px;
        display: flex;
        flex-wrap: wrap;
        gap: 8px; /* Larger gap */
        justify-content: center;
        align-items: flex-start;
        overflow: hidden;
        background-color: #f8f9fa; /* Very light grey */
    }

     .limit-message {
        margin-top: 15px;
        font-size: 1rem;
        color: #dc3545;
        font-weight: 500;
        text-align: center;
     }


    .person-visual {
        width: 35px; /* Larger circles */
        height: 35px;
        background-color: #007bff; /* Primary blue */
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 0.9em;
        font-weight: 500;
        transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
        opacity: 0; /* Start invisible for fade-in */
        animation: fadeInScale 0.6s forwards cubic-bezier(0.25, 0.46, 0.45, 0.94); /* Smoother fade-in scale */
        cursor: help; /* Indicate hover info */
        position: relative; /* Needed for tooltip */
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .person-visual:hover {
        transform: translateY(-3px) scale(1.1);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Tooltip for birthday - Optional but adds insight */
    /* .person-visual::after {
        content: attr(data-birthday);
        position: absolute;
        bottom: 100%;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.7em;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s ease;
        margin-bottom: 5px;
    }

    .person-visual:hover::after {
        opacity: 1;
    } */


    .person-visual.match {
        background-color: #dc3545; /* Red for matching people */
        box-shadow: 0 0 15px #ff073a; /* Glow effect */
        animation: highlightMatch 1.5s ease infinite, fadeInScale 0.6s forwards cubic-bezier(0.25, 0.46, 0.45, 0.94); /* Keep fade-in, add highlight */
    }

     @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.5); }
        to { opacity: 1; transform: scale(1); }
    }

    @keyframes highlightMatch {
        0% { transform: scale(1); }
        50% { transform: scale(1.15); } /* Scale up more noticeably */
        100% { transform: scale(1); }
    }

     .person-visual span {
         user-select: none; /* Prevent text selection on numbers */
     }


    .explanation {
        background-color: #e9f5ff; /* Light blue background, matching display boxes */
        border: 1px solid #b3d7ff;
        border-radius: 10px;
        padding: 25px;
        margin: 20px auto;
        max-width: 850px;
        line-height: 1.8;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    .explanation p, .explanation ul {
        margin-bottom: 1em;
    }

    .explanation ul {
        list-style: disc inside;
        padding-right: 0;
    }

     @media (max-width: 600px) {
        .controls {
            flex-direction: column;
            align-items: stretch;
        }

        button {
            width: 100%;
            margin-bottom: 10px;
        }

         .display-area {
             flex-direction: column;
         }

         .display-box {
             width: 100%;
             min-width: auto;
         }

         .people-visual-container {
             min-height: 100px;
             padding: 10px;
             gap: 5px;
         }

         .person-visual {
             width: 30px;
             height: 30px;
             font-size: 0.7em;
         }

         h1 {
             font-size: 1.7em;
         }

         h2 {
             font-size: 1.3em;
         }
    }

</style>

<script>
    const addPersonBtn = document.getElementById('addPersonBtn');
    const resetBtn = document.getElementById('resetBtn');
    const peopleCountSpan = document.getElementById('peopleCount');
    const probabilitySpan = document.getElementById('probability');
    const matchStatusSpan = document.getElementById('matchStatus');
    const matchStatusBox = document.querySelector('.match-status');
    const peopleVisualContainer = document.getElementById('peopleVisualContainer');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationDiv = document.getElementById('explanation');
    const limitMessageDiv = document.getElementById('limitMessage');

    const MAX_PEOPLE = 60; // Set a reasonable limit for visualization

    let peopleCount = 0;
    let birthdays = []; // Array to store birthdays (1-365)
    let matchFound = false;
    let isAddingPerson = false; // Flag to prevent rapid clicks

    // Function to calculate probability of at least one match
    function calculateProbability(n) {
        if (n <= 1) return 0;
        if (n > 365) return 1; // Guarantee a match if more than 365 people

        let p_no_match = 1.0;
        for (let i = 0; i < n; i++) {
            // Handle case where n > 365 early, though the loop condition `i < n` would handle it
            // The formula inherently results in 0 if i reaches 365
            if (365 - i <= 0) {
                p_no_match = 0;
                break;
            }
             p_no_match *= (365 - i) / 365;
        }
        return 1.0 - p_no_match;
    }

    // Function to add a person
    function addPerson() {
        if (matchFound || peopleCount >= MAX_PEOPLE || isAddingPerson) {
            return; // Do nothing if match found, limit reached, or already adding
        }

        isAddingPerson = true; // Set flag
        addPersonBtn.disabled = true; // Temporarily disable button

        peopleCount++;
        peopleCountSpan.textContent = peopleCount;

        // Generate a random birthday (1 to 365)
        const newBirthday = Math.floor(Math.random() * 365) + 1;

        // Add the new birthday to the list *before* checking for match visually
        birthdays.push(newBirthday);

        // Check for match among ALL current birthdays
        const existingMatchIndex = birthdays.indexOf(newBirthday);
        // A match occurs if the new birthday already exists *before* the last element (which is the new one)
        const currentMatchFound = (existingMatchIndex !== -1 && existingMatchIndex < birthdays.length - 1);

        if (currentMatchFound) {
            matchFound = true;
        }

        // Update probability display with the *new* count
        const probability = calculateProbability(peopleCount);
        probabilitySpan.textContent = `${(probability * 100).toFixed(2)}%`; // Format to 2 decimal places

        // Add visual representation of the person
        const personVisual = document.createElement('div');
        personVisual.classList.add('person-visual');
        personVisual.dataset.birthday = newBirthday; // Store birthday in data attribute

        // Add the birthday number inside the circle
        const birthdaySpan = document.createElement('span');
        birthdaySpan.textContent = newBirthday;
        personVisual.appendChild(birthdaySpan);

        peopleVisualContainer.appendChild(personVisual);

        // Use a small timeout to allow the fade-in animation to start before highlighting
        // This also provides a visual delay for the user
        setTimeout(() => {
             // Update match status display
            if (matchFound) {
                // Add 'match' class to ALL visual elements with the matching birthday
                peopleVisualContainer.querySelectorAll('.person-visual').forEach(pv => {
                    if (parseInt(pv.dataset.birthday) === newBirthday) {
                         pv.classList.add('match');
                    }
                });
                matchStatusSpan.textContent = `🎉 נמצאה התאמה! יום הולדת מספר ${newBirthday} חוזר על עצמו!`;
                matchStatusBox.classList.add('match-found');
                addPersonBtn.disabled = true; // Keep button disabled after match
                limitMessageDiv.style.display = 'none'; // Hide limit message if match found
            } else {
                 matchStatusSpan.textContent = `ממתינים למפגש...`;
                 matchStatusBox.classList.remove('match-found');

                 if (peopleCount >= MAX_PEOPLE) {
                     addPersonBtn.disabled = true;
                     limitMessageDiv.style.display = 'block';
                     matchStatusSpan.textContent = `הגענו למספר המקסימלי`;
                 } else {
                     addPersonBtn.disabled = false; // Re-enable button if no match and not at limit
                      limitMessageDiv.style.display = 'none';
                 }
            }
            isAddingPerson = false; // Reset flag after animations/updates

        }, 600); // Match timeout to animation duration
    }

    // Function to reset the simulation
    function resetSimulation() {
        peopleCount = 0;
        birthdays = [];
        matchFound = false;
        isAddingPerson = false;

        peopleCountSpan.textContent = peopleCount;
        probabilitySpan.textContent = "0.00%";
        matchStatusSpan.textContent = "ממתינים למפגש...";
        matchStatusBox.classList.remove('match-found');
        peopleVisualContainer.innerHTML = ''; // Clear visual elements
        addPersonBtn.disabled = false; // Re-enable button
        limitMessageDiv.style.display = 'none';
    }

    // Toggle explanation visibility
    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'מה עומד מאחורי התופעה הזו? (הצג הסבר)';
    }

    // Event Listeners
    addPersonBtn.addEventListener('click', addPerson);
    resetBtn.addEventListener('click', resetSimulation);
    toggleExplanationBtn.addEventListener('click', toggleExplanation);

    // Initial state on load
    resetSimulation();

</script>