---
title: "חידת הדלתות של מונטי הול: התנסות אינטראקטיבית"
english_slug: monty-hall-doors-riddle
category: "מתמטיקה"
tags:
  - הסתברות
  - מתמטיקה
  - מונטי הול
  - סטטיסטיקה
  - אינטואיציה
  - סימולציה
---
<h1>חידת הדלתות של מונטי הול</h1>
<p>דמיינו שאתם בשעשועון טלוויזיה נוצץ! מולכם שלוש דלתות מסתוריות. מאחורי אחת מסתתר פרס גדול (אולי מכונית חדשה?), ומאחורי השתיים האחרות... ובכן, עז. בחרתם דלת ראשונה, והמתח בשיאו. המנחה, שיודע בדיוק מה מסתתר מאחורי כל דלת, ניגש לאחת משתי הדלתות האחרות שאינן הבחירה שלכם, ופותח אותה... והוא חושף עז! </p>
<p>עכשיו רגע ההחלטה: האם להישאר עם הדלת שבחרתם מלכתחילה, או להחליף לדלת השלישית שנותרה סגורה? האם ההחלפה באמת משפרת את הסיכויים שלכם לצאת עם הפרס?</p>
<p>בואו נשחק ונראה!</p>

<div id="game-container">
    <h2>שלב 1: בחר דלת ראשונה</h2>
    <div id="doors-container">
        <div class="door" data-door="0">
            <div class="door-inner">
                <span class="door-face front"><span class="door-number">1</span></span>
                <span class="door-face back"><span class="door-content hidden">?</span></span>
            </div>
            <div class="selection-indicator hidden">הבחירה שלך</div>
        </div>
        <div class="door" data-door="1">
             <div class="door-inner">
                <span class="door-face front"><span class="door-number">2</span></span>
                <span class="door-face back"><span class="door-content hidden">?</span></span>
            </div>
             <div class="selection-indicator hidden">הבחירה שלך</div>
        </div>
        <div class="door" data-door="2">
             <div class="door-inner">
                <span class="door-face front"><span class="door-number">3</span></span>
                <span class="door-face back"><span class="door-content hidden">?</span></span>
            </div>
             <div class="selection-indicator hidden">הבחירה שלך</div>
        </div>
    </div>

    <p id="status" class="status-message">אנא בחר דלת.</p>

    <div id="switch-prompt" class="hidden">
        <h2>שלב 2: החלטה!</h2>
        <p class="prompt-text">המנחה חשף עז מאחורי דלת אחרת. כעת, נותרו שתי דלתות סגורות. האם ברצונך להישאר עם הדלת המקורית שבחרת, או להחליף לדלת השנייה שנותרה?</p>
        <button id="stay-button" class="game-button stay">להישאר</button>
        <button id="switch-button" class="game-button switch">להחליף</button>
    </div>

    <div id="final-choice-indicator" class="hidden">
        <h2>שלב 3: תוצאה</h2>
        <p class="final-choice-text"></p>
    </div>


    <button id="restart-button" class="game-button restart hidden">שחק שוב</button>

    <div id="stats-container">
        <h3>הסתברות בפועל: תוצאות הסימולציה שלך</h3>
        <p>ככל שתשחק יותר, התוצאות יתקרבו להסתברות האמיתית.</p>
        <div class="stat-block">
            <h4>הישארות עם הבחירה הראשונה:</h4>
            <p>זכיות: <span id="stay-wins">0</span> מתוך <span id="stay-attempts">0</span> ניסיונות (<strong id="stay-percent">0%</strong>)</p>
        </div>
        <div class="stat-block">
            <h4>החלפה לדלת השנייה:</h4>
            <p>זכיות: <span id="switch-wins">0</span> מתוך <span id="switch-attempts">0</span> ניסיונות (<strong id="switch-percent">0%</strong>)</p>
        </div>
         <button id="reset-stats-button" class="game-button reset">אפס סטטיסטיקה</button>
    </div>
</div>

<button id="toggle-explanation" class="game-button toggle-exp">הצג/הסתר הסבר מתמטי</button>

<div id="explanation" class="hidden">
    <h2>ההסבר המתמטי לחידת מונטי הול: מדוע כדאי להחליף</h2>
    <p>האינטואיציה הראשונית של רוב האנשים נוטה לטעות בחידת מונטי הול, ולחשוב שלאחר שהמנחה פתח דלת, הסיכויים מתחלקים שווה בשווה (50/50) בין שתי הדלתות הסגורות שנותרו. אולם, זוהי טעות נפוצה הנובעת מהתעלמות ממידע קריטי:</p>
    <p><strong>1. הבחירה הראשונית:</strong> כשרק שלוש הדלתות סגורות, הסיכוי שלכם לבחור נכון את הדלת עם הפרס הוא <strong>1/3</strong>. מכאן נובע, שהסיכוי שהפרס נמצא מאחורי *אחת משתי הדלתות האחרות* ש<strong>לא</strong> בחרתם הוא <strong>2/3</strong>.</p>
    <p><strong>2. פעולת המנחה היא קריטית:</strong> המנחה אינו פותח דלת אקראית. הוא תמיד פותח דלת שמאחוריה יש עז, מבין שתי הדלתות ש<strong>לא</strong> בחרתם. המנחה *חייב* לפתוח דלת כזו, והוא משתמש בידע שלו על מיקום הפרס כדי לעשות זאת.</p>
    <p><strong>3. המידע מתרכז:</strong> כאשר המנחה פותח דלת "ריקה" מבין שתי הדלתות שלא בחרתם, הוא למעשה "מרכז" את כל הסיכוי המצטבר של 2/3 שהיה על קבוצת שתי הדלתות הללו - אל הדלת האחת שנותרה סגורה מבין השתיים ש<strong>לא</strong> בחרתם. </p>
    <p>חשבו על זה כך:</p>
    <ul>
        <li>אם בחרתם נכון בהתחלה (סיכוי 1/3), החלפה תמיד תוביל להפסד (כי הדלת השנייה הסגורה חייבת להיות עם עז).</li>
        <li>אם בחרתם לא נכון בהתחלה (סיכוי 2/3), כלומר הפרס נמצא מאחורי אחת משתי הדלתות האחרות - המנחה *חייב* לפתוח את דלת העז מבין השתיים הללו. במקרה כזה, הדלת שנותרת סגורה מבין השתיים האחרות *חייבת* להיות הדלת עם הפרס. לכן, אם בחרתם לא נכון בהתחלה (סיכוי 2/3), החלפה תמיד תוביל לזכייה!</li>
    </ul>
    <p>מכיוון שהסיכוי לבחור לא נכון בהתחלה הוא 2/3, זהו גם הסיכוי שתזכו אם תבחרו להחליף דלת. הסיכוי להישאר ולזכות נותר 1/3.</p>
    <p>הסימולציה כאן מאפשרת לכם לראות את ההבדל הזה מתבטא בתוצאות על פני מספר רב של משחקים. נסו לשחק 100 או 200 פעמים ותראו שהסטטיסטיקה נוטה לכיוון של 2/3 זכיות בהחלפה לעומת 1/3 בהישארות.</p>
</div>


<style>
/* General Styling */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.7;
    margin: 0;
    padding: 20px;
    background: linear-gradient(to bottom right, #ece9e6, #ffffff); /* Subtle gradient background */
    color: #333;
    direction: rtl;
    text-align: right; /* Adjust text alignment for RTL */
}

h1, h2, h3 {
    text-align: center;
    color: #1a237e; /* Deep indigo */
    margin-bottom: 15px;
}

p {
    margin-bottom: 1em;
}

/* Game Container */
#game-container {
    background-color: #ffffff; /* White background */
    border: 1px solid #e0e0e0; /* Light gray border */
    padding: 30px;
    margin: 20px auto;
    max-width: 650px; /* Slightly wider */
    text-align: center;
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 6px 12px rgba(0,0,0,0.1); /* Stronger shadow */
    position: relative; /* Needed for potential absolute positioning inside */
    overflow: hidden; /* Clear floats/margins */
}

/* Doors */
#doors-container {
    display: flex;
    justify-content: center;
    gap: 25px; /* Increased gap */
    margin-bottom: 30px;
    perspective: 1000px; /* Perspective for the flip */
}

.door {
    width: 130px; /* Slightly larger */
    height: 200px; /* Slightly taller */
    cursor: pointer;
    border: 4px solid transparent; /* Thicker border, initially transparent */
    border-radius: 15px; /* More rounded */
    background-color: #795548; /* Brown door color */
    box-shadow: 3px 3px 8px rgba(0,0,0,0.4); /* Enhanced shadow */
    transition: transform 0.5s ease-in-out, border-color 0.3s ease, box-shadow 0.3s ease;
    position: relative; /* Needed for indicator */
    overflow: hidden; /* Ensure content stays inside on flip */
}

.door:hover:not(.open):not(.selected) {
    transform: translateY(-5px) scale(1.03); /* Lift and slightly scale */
    border-color: #ffb300; /* Amber */
    box-shadow: 4px 4px 10px rgba(0,0,0,0.5);
}

.door.selected {
    border-color: #ffeb3b; /* Bright yellow */
    box-shadow: 0 0 15px rgba(255,235,59,0.8); /* Glow effect */
    transform: scale(1.05); /* Slightly larger when selected */
}

.door.open {
    cursor: default;
    /* border-color set by JS/classes like .win, .lose, .goat */
}

.door-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94); /* Smooth flip animation */
    transform-style: preserve-3d; /* Keep 3D effect */
}

.door.open .door-inner {
    transform: rotateY(180deg);
}

.door-face {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden; /* Hide the backface of the front */
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 12px; /* Match door radius */
    overflow: hidden;
}

.door-face.front {
     background-color: #795548; /* Brown */
     color: white;
     transform: rotateY(0deg);
}

.door-face.back {
    background-color: #e8f5e9; /* Very light green */
    color: #333;
    transform: rotateY(180deg); /* Start flipped */
    font-size: 50px; /* Larger emojis */
    box-shadow: inset 0 0 10px rgba(0,0,0,0.2);
}

.door-number {
    font-size: 60px; /* Larger numbers */
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.door-content {
    font-size: 50px; /* Ensure emoji size */
}

/* Specific content styles */
.door.open.goat .door-content::before {
    content: '🐐'; /* Goat emoji */
}

.door.open.car .door-content::before {
    content: '🚗'; /* Car emoji */
}

/* Indicators and Feedback */
.selection-indicator {
    position: absolute;
    bottom: 5px;
    left: 50%;
    transform: translateX(-50%);
    background-color: rgba(255, 235, 59, 0.9); /* Yellow translucent */
    color: #333;
    font-size: 0.8em;
    padding: 3px 8px;
    border-radius: 5px;
    font-weight: bold;
    z-index: 10; /* Above the door */
}


.door.open.win {
    border-color: #4caf50; /* Green */
    box-shadow: 0 0 15px rgba(76,175,80,0.8); /* Green glow */
}

.door.open.lose {
     border-color: #f44336; /* Red */
     box-shadow: 0 0 15px rgba(244,67,54,0.8); /* Red glow */
}


/* Status Messages */
.status-message {
    font-size: 1.2em; /* Larger status text */
    min-height: 1.6em; /* Reserve space */
    margin-bottom: 20px;
    color: #3f51b5; /* Indigo */
    font-weight: bold;
}

.status-message.win {
    color: #4caf50; /* Green */
}

.status-message.lose {
    color: #f44336; /* Red */
}

/* Prompt and Buttons */
#switch-prompt, #final-choice-indicator {
     margin-top: 30px;
     padding: 20px;
     background-color: #e3f2fd; /* Light blue background */
     border-radius: 8px;
     border: 1px solid #bbdefb;
}

.prompt-text, .final-choice-text {
    font-size: 1.1em;
    margin-bottom: 15px;
    color: #283593; /* Dark indigo */
}


.game-button {
    padding: 12px 20px; /* Larger buttons */
    margin: 8px; /* More space */
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    border: none;
    border-radius: 8px; /* More rounded */
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
    text-transform: uppercase;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.game-button:hover {
    transform: translateY(-2px); /* Lift on hover */
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.game-button:active {
    transform: translateY(0); /* Press down on click */
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

#stay-button {
    background-color: #ff9800; /* Orange */
    color: white;
}

#stay-button:hover {
    background-color: #f57c00;
}

#switch-button {
    background-color: #4caf50; /* Green */
    color: white;
}

#switch-button:hover {
    background-color: #388e3c;
}

#restart-button {
    background-color: #2196f3; /* Blue */
    color: white;
    margin-top: 30px;
}

#restart-button:hover {
    background-color: #1976d2;
}

#toggle-explanation {
    background-color: #757575; /* Gray */
    color: white;
    display: block;
    margin: 30px auto;
    max-width: 250px; /* Slightly wider button */
    text-align: center;
}

#toggle-explanation:hover {
     background-color: #616161;
}

#reset-stats-button {
    background-color: #f44336; /* Red */
    color: white;
    margin-top: 15px;
    font-size: 0.9em;
    padding: 8px 15px;
}
#reset-stats-button:hover {
    background-color: #d32f2f;
}

/* Statistics */
#stats-container {
    margin-top: 40px;
    padding: 20px;
    border-top: 2px solid #e0e0e0; /* Thicker border */
    text-align: right;
    background-color: #f5f5f5; /* Light gray background */
    border-radius: 8px;
}

#stats-container h3 {
    margin-top: 0;
    margin-bottom: 15px;
    color: #1a237e; /* Deep indigo */
}

.stat-block {
    margin-bottom: 15px;
    padding: 15px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    background-color: #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.stat-block h4 {
    margin: 0 0 8px 0;
    color: #3f51b5; /* Indigo */
    font-size: 1.1em;
}

.stat-block p {
    margin: 0;
    font-size: 1em;
    color: #555;
}

.stat-block strong {
    font-size: 1.1em;
    color: #1a237e; /* Highlight stats */
}

/* Explanation Section */
#explanation {
    background-color: #e8f5e9; /* Very light green */
    border: 1px solid #c8e6c9; /* Light green border */
    padding: 25px;
    margin: 20px auto;
    max-width: 700px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    text-align: right;
}

#explanation h2 {
    color: #2e7d32; /* Dark green */
}

#explanation p {
    margin-bottom: 1.2em;
    line-height: 1.8;
}

#explanation strong {
    color: #1b5e20; /* Darker green */
}

#explanation ul {
    margin-bottom: 1.2em;
    padding-right: 20px; /* Adjust padding for RTL list */
}

#explanation li {
    margin-bottom: 0.5em;
}


/* Utility */
.hidden {
    display: none;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const doors = document.querySelectorAll('.door');
    const statusDisplay = document.getElementById('status');
    const switchPrompt = document.getElementById('switch-prompt');
    const stayButton = document.getElementById('stay-button');
    const switchButton = document.getElementById('switch-button');
    const restartButton = document.getElementById('restart-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const finalChoiceIndicator = document.getElementById('final-choice-indicator');
    const finalChoiceText = document.querySelector('.final-choice-text');
    const resetStatsButton = document.getElementById('reset-stats-button');


    const totalGamesSpan = document.getElementById('total-games'); // Not strictly needed with separate attempts
    const stayAttemptsSpan = document.getElementById('stay-attempts');
    const switchAttemptsSpan = document.getElementById('switch-attempts');
    const stayWinsSpan = document.getElementById('stay-wins');
    const switchWinsSpan = document.getElementById('switch-wins');
    const stayPercentSpan = document.getElementById('stay-percent');
    const switchPercentSpan = document.getElementById('switch-percent');

    let carDoor = -1;
    let userInitialChoice = -1;
    let openedDoorByHost = -1;
    let gameActive = true; // Flag to prevent clicks during animations/transitions

    // Load stats from localStorage on page load
    let stayAttempts = parseInt(localStorage.getItem('montyHallStayAttempts') || '0');
    let switchAttempts = parseInt(localStorage.getItem('montyHallSwitchAttempts') || '0');
    let stayWins = parseInt(localStorage.getItem('montyHallStayWins') || '0');
    let switchWins = parseInt(localStorage.getItem('montyHallSwitchWins') || '0');

    function updateStatsDisplay() {
        stayAttemptsSpan.textContent = stayAttempts;
        switchAttemptsSpan.textContent = switchAttempts;
        stayWinsSpan.textContent = stayWins;
        switchWinsSpan.textContent = switchWins;

        const calculatedStayPercent = stayAttempts > 0 ? (stayWins / stayAttempts * 100).toFixed(1) : 0;
        const calculatedSwitchPercent = switchAttempts > 0 ? (switchWins / switchAttempts * 100).toFixed(1) : 0;

        stayPercentSpan.textContent = `${calculatedStayPercent}%`;
        switchPercentSpan.textContent = `${calculatedSwitchPercent}%`;
    }

    function saveStats() {
        localStorage.setItem('montyHallStayAttempts', stayAttempts);
        localStorage.setItem('montyHallSwitchAttempts', switchAttempts);
        localStorage.setItem('montyHallStayWins', stayWins);
        localStorage.setItem('montyHallSwitchWins', switchWins);
    }

    function resetStats() {
        stayAttempts = 0;
        switchAttempts = 0;
        stayWins = 0;
        switchWins = 0;
        saveStats();
        updateStatsDisplay();
        alert('סטטיסטיקות אופסו בהצלחה!');
    }


    function initializeGame() {
        gameActive = true; // Enable game interactions
        doors.forEach(door => {
            door.classList.remove('selected', 'open', 'car', 'goat', 'win', 'lose');
            const doorInner = door.querySelector('.door-inner');
            const doorContent = door.querySelector('.door-content');
            const selectionIndicator = door.querySelector('.selection-indicator');

            doorContent.classList.add('hidden');
            doorContent.textContent = ''; // Clear previous content
            doorInner.style.transform = 'rotateY(0deg)';
            door.style.borderColor = 'transparent';
            door.style.boxShadow = '3px 3px 8px rgba(0,0,0,0.4)'; /* Reset default shadow */
            door.style.cursor = 'pointer';
            selectionIndicator.classList.add('hidden');
            door.onclick = null; // Clear previous handlers

             // Re-add initial click listeners
            door.addEventListener('click', handleFirstChoice, { once: true });
        });

        carDoor = Math.floor(Math.random() * 3); // 0, 1, or 2
        userInitialChoice = -1;
        openedDoorByHost = -1;

        statusDisplay.textContent = 'שלב 1: בחר דלת ראשונה';
        statusDisplay.className = 'status-message'; // Reset status classes
        switchPrompt.classList.add('hidden');
        restartButton.classList.add('hidden');
        finalChoiceIndicator.classList.add('hidden');

         // Add click listeners for the first choice
        doors.forEach(door => {
            door.onclick = handleFirstChoice;
        });
    }

    function handleFirstChoice(event) {
        if (!gameActive || userInitialChoice !== -1) return; // Prevent clicks if game is inactive or choice made

        gameActive = false; // Pause interaction

        const chosenDoorElement = event.currentTarget;
        userInitialChoice = parseInt(chosenDoorElement.dataset.door);

        // Visual feedback for selection
        doors.forEach(door => {
             door.onclick = null; // Disable clicks on all doors
             door.classList.remove('selected'); // Remove selected from others (shouldn't happen with once:true but good practice)
              door.querySelector('.selection-indicator').classList.add('hidden'); // Hide indicators
        });

        chosenDoorElement.classList.add('selected');
        chosenDoorElement.querySelector('.selection-indicator').classList.remove('hidden');


        statusDisplay.textContent = `בחרת בדלת מספר ${userInitialChoice + 1}.`;

        // Host opens a door after a short delay
        setTimeout(openGoatDoor, 1200); // Add a delay for effect
    }

    function openGoatDoor() {
        let doorToOpen = -1;

        // Find a door to open that is not the user's choice and not the car door
        const availableDoorsToOpen = [0, 1, 2].filter(doorIndex =>
            doorIndex !== userInitialChoice && doorIndex !== carDoor
        );

        // The host must open a goat door.
        // If user chose the car, there are two goat doors left (both goats), pick one randomly.
        if (userInitialChoice === carDoor) {
             doorToOpen = availableDoorsToOpen[Math.floor(Math.random() * availableDoorsToOpen.length)];
        }
        // If user chose a goat, there's one goat door and the car door left.
        // The host must open the remaining goat door.
        else {
             doorToOpen = availableDoorsToOpen[0]; // There is only one goat option left
        }

        openedDoorByHost = doorToOpen;
        const openedDoorElement = doors[openedDoorByHost];

        // Animate door opening
        openedDoorElement.classList.add('open', 'goat'); // Add goat class immediately for content display
        openedDoorElement.querySelector('.door-content').classList.remove('hidden');
        openedDoorElement.style.cursor = 'default';
        openedDoorElement.onclick = null; // Make opened door not clickable

        // Wait for the animation to complete before showing the prompt
        setTimeout(() => {
            statusDisplay.textContent = `המנחה פתח את דלת מספר ${openedDoorByHost + 1} וחשף עז!`;
            switchPrompt.classList.remove('hidden');
            finalChoiceIndicator.classList.add('hidden'); // Hide final indicator if it was somehow visible

            // Add listeners for the second choice (stay or switch)
            stayButton.onclick = () => handleSecondChoice('stay');
            switchButton.onclick = () => handleSecondChoice('switch');

            gameActive = true; // Re-enable interaction for the next step

        }, 1000); // Delay matches/exceeds door flip animation duration
    }

    function handleSecondChoice(strategy) {
        if (!gameActive) return; // Prevent clicks during animation

        gameActive = false; // Pause interaction
        switchPrompt.classList.add('hidden');
        finalChoiceIndicator.classList.remove('hidden');


        let finalChoiceDoorIndex = userInitialChoice; // Default to stay
        let finalChoiceElement = doors[userInitialChoice];

        const initialChoiceDoorElement = doors[userInitialChoice];
        const openedDoorElement = doors[openedDoorByHost];
        let otherClosedDoorIndex = -1;
        let otherClosedDoorElement = null;


        // Find the remaining closed door
        [0, 1, 2].forEach(doorIndex => {
            if (doorIndex !== userInitialChoice && doorIndex !== openedDoorByHost) {
                otherClosedDoorIndex = doorIndex;
                otherClosedDoorElement = doors[doorIndex];
            }
        });


        if (strategy === 'switch') {
            finalChoiceDoorIndex = otherClosedDoorIndex;
            finalChoiceElement = otherClosedDoorElement;
        }

        // Update attempt counters *before* revealing to ensure stats are always updated
        if (strategy === 'stay') {
            stayAttempts++;
        } else { // switch
            switchAttempts++;
        }


        // Determine win/lose
        const hasWon = (finalChoiceDoorIndex === carDoor);

        if (hasWon) {
            if (strategy === 'stay') stayWins++;
            else switchWins++;
        }

        saveStats(); // Save stats immediately after determining outcome
        updateStatsDisplay(); // Update display


        // Animate opening of the final choice door and the other remaining closed door
        const doorsToReveal = [];
        if (!initialChoiceDoorElement.classList.contains('open')) doorsToReveal.push(initialChoiceDoorElement);
        if (!otherClosedDoorElement.classList.contains('open')) doorsToReveal.push(otherClosedDoorElement);

        doorsToReveal.forEach(doorElement => {
            const doorIndex = parseInt(doorElement.dataset.door);
            doorElement.classList.add('open');
            doorElement.querySelector('.door-content').classList.remove('hidden');
            doorElement.onclick = null; // Make door not clickable

             if (doorIndex === carDoor) {
                doorElement.classList.add('car');
            } else {
                doorElement.classList.add('goat');
            }
        });

        // Add win/lose class to the FINAL selected door and update status text after animation
        setTimeout(() => {
             finalChoiceElement.classList.add(hasWon ? 'win' : 'lose');
             finalChoiceElement.querySelector('.selection-indicator').classList.add('hidden'); // Hide indicator on final reveal

            const strategyText = strategy === 'stay' ? 'הישארת עם בחירתך הראשונה' : 'החלפת דלתות';
            if (hasWon) {
                 statusDisplay.textContent = `🎉 ניצחון! בחרת בדלת מספר ${finalChoiceDoorIndex + 1} (${strategyText}) וזכית במכונית! 🎉`;
                 statusDisplay.className = 'status-message win';
                 finalChoiceText.textContent = `בחרת להחליף לדלת מספר ${finalChoiceDoorIndex + 1}.`; // More specific final choice
                 finalChoiceText.style.color = '#4caf50'; // Green text for win
            } else {
                 statusDisplay.textContent = `😥 הפסד... בחרת בדלת מספר ${finalChoiceDoorIndex + 1} (${strategyText}) וקיבלת עז. 😥`;
                 statusDisplay.className = 'status-message lose';
                 finalChoiceText.textContent = `בחרת להחליף לדלת מספר ${finalChoiceDoorIndex + 1}.`; // More specific final choice
                 finalChoiceText.style.color = '#f44336'; // Red text for lose
            }
            finalChoiceIndicator.classList.remove('hidden');


            restartButton.classList.remove('hidden');
            restartButton.onclick = initializeGame; // Set restart handler
            gameActive = true; // Allow restart button click
        }, 1200); // Wait for final door animations
    }

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (!explanationDiv.classList.contains('hidden')) {
             // Scroll smoothly to the explanation if shown
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Reset stats button handler
    resetStatsButton.addEventListener('click', resetStats);


    // Initial game setup
    updateStatsDisplay(); // Display stats on load
    initializeGame(); // Start the first game

});
</script>
```