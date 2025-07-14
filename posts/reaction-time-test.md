---
title: "מבחן מהירות תגובה: כמה מהר המוח שלך מגיב?"
english_slug: reaction-time-test
category: "מדעי החיים / פיזיולוגיה"
tags: [זמן תגובה, גירוי ויזואלי, ניסוי, אינטראקטיבי, מהירות, מבחן]
---
# בדוק את המהירות שלך: מבחן זמן תגובה ויזואלי

<p>מוכנים לאתגר? בדקו כמה מהר אתם מגיבים! הכלי הפשוט הזה יחשוף את מהירות התגובה הויזואלית שלכם. האם האצבע שלכם מהירה מספיק כדי ללכוד את הרגע?</p>

<section id="reaction-test-app">
    <div class="app-container">
        <div id="test-area" class="state-initial">
            <div id="message" class="dynamic-text">לחץ כדי להתחיל</div>
            <div id="result" class="dynamic-text"></div>
        </div>
    </div>
</section>

<button id="toggle-explanation">הצג הסבר</button>

<div id="explanation" style="display: none;">
    <h2>מהו זמן תגובה ולמה זה מעניין?</h2>
    <p>זמן תגובה הוא ממש "רגע האמת" של מערכת העצבים שלכם – כמה זמן לוקח מהרגע שהעיניים קולטות מידע (הגירוי, במקרה שלנו - שינוי צבע) ועד שהמוח מעבד אותו ושולח פקודה לשרירים לפעול (התגובה, אצלנו - לחיצה). בניסוי הזה, אנחנו מודדים כמה מהר אתם עוברים מראיית המסך הירוק ללחיצה עליו.</p>

    <h2>למה כדאי לשפר את זמן התגובה?</h2>
    <p>תגובה מהירה היא לא רק מגניבה, היא גם סופר חשובה בחיים! תחשבו על זה:</p>
    <ul>
        <li>**נהיגה ובטיחות:** תגובה זריזה יכולה להיות ההבדל בין תאונה למניעתה.</li>
        <li>**ספורט ומשחקים:** קליטת המגרש, מיקום הכדור או מהלכי היריב בשבריר שנייה היא המפתח לניצחון.</li>
        <li>**קואורדינציה יומיומית:** אפילו פעולות פשוטות כמו לתפוס משהו שנופל או להקליד מהר על המקלדת תלויות בזמן תגובה טוב.</li>
    </ul>

    <h2>מה משפיע על המהירות שלך?</h2>
    <p>התוצאה שלך היא לא גזירת גורל! זמן התגובה מושפע משלל גורמים:</p>
    <ul>
        <li>**סוג הגירוי:** גירוי ברור וחזק יותר (אור ירוק בוהק לעומת שינוי צבע עדין) מקצר את זמן התגובה.</li>
        <li>**מורכבות המשימה:** ככל שיש יותר "בלבול" (למשל, תגובה שונה לשלושה צבעים שונים) – זמן התגובה מתארך. המבחן הזה פשוט במיוחד!</li>
        <li>**עייפות וריכוז:** מוח עייף או מוסח מגיב לאט יותר. נסו את המבחן כשאתם רעננים!</li>
        <li>**גיל:** באופן כללי, צעירים נוטים להיות זריזים יותר בתגובה מבוגרים.</li>
        <li>**אימון:** כן, אפשר לשפר! חשיפה חוזרת למשימות דומות יכולה לשפר את הביצועים.</li>
    </ul>

    <h2>התוצאה שלך:</h2>
    <p>המספר שקיבלת הוא מדידה לרגע ספציפי. זמן התגובה הממוצע של אדם בריא בדרך כלל נע בין 200 ל-300 מילישניות (ms) עבור גירוי ויזואלי פשוט כמו זה. תוצאות נמוכות מ-200ms מצביעות על מהירות גבוהה, ותוצאות גבוהות מ-300ms מצביעות על תגובה איטית יותר באותו רגע. נסו שוב ושוב כדי לראות את הטווח שלכם!</p>
</div>

<style>
/* גופנים - שימוש בגופן מערכת מודרני */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    direction: rtl; /* תמיכה בעברית */
    text-align: right; /* יישור לימין */
}

h1, h2 {
    text-align: center; /* כותרות ממורכזות גם ב-RTL */
}

p, ul {
    text-align: right; /* יישור לימין */
}

#reaction-test-app {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 450px; /* Ensure enough height for the app area */
    margin: 30px 0;
    perspective: 1000px; /* Add perspective for potential 3D transforms */
}

.app-container {
    width: 100%;
    max-width: 500px; /* Limit the width */
    background-color: #ffffff; /* ניטרלי בהתחלה */
    border-radius: 15px; /* פינות מעוגלות יותר */
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* צל עדין יותר ומורגש */
    overflow: hidden; /* לוודא שהפינות המעוגלות נשמרות */
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 400px; /* Height of the test area itself */
    transition: transform 0.5s ease-in-out; /* Transition for shaking/emphasis */
}

#test-area {
    width: 100%;
    height: 400px; /* Fixed height for consistency */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 1.8em; /* גודל פונט גדול יותר */
    font-weight: bold;
    color: #2c3e50; /* צבע טקסט כהה יותר ומודרני */
    cursor: pointer;
    transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out; /* Smooth color transition */
    text-align: center;
    padding: 30px; /* Padding for inner content */
    box-sizing: border-box; /* Include padding in width/height */
    user-select: none; /* מונע בחירת טקסט */
    -webkit-tap-highlight-color: rgba(0,0,0,0); /* מונע היילייט בלחיצה במובייל */
    border-radius: 15px; /* Match container radius */
}

/* Dynamic Text Styling */
.dynamic-text {
    transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
    will-change: opacity, transform; /* Performance hint */
}

#message {
    margin-bottom: 20px;
}

#result {
    font-size: 1.6em; /* גודל פונט לתוצאה */
    opacity: 0; /* Hide result initially */
    transform: translateY(20px); /* Start slightly lower */
}

/* State Styling */
.state-initial {
    background-color: #ecf0f1; /* Light neutral background */
    color: #2c3e50;
}

.state-initial #message {
    opacity: 1;
    transform: translateY(0);
}
.state-initial #result {
    opacity: 0;
    transform: translateY(20px);
}


.state-waiting_delay {
    background-color: #ffffff; /* Clean white during wait */
    color: #3498db; /* Soothing blue */
}

.state-waiting_delay #message {
     opacity: 1;
     transform: translateY(0);
}
.state-waiting_delay #result {
    opacity: 0;
    transform: translateY(20px);
}


.state-stimulus {
    background-color: #2ecc71; /* Vibrant green */
    color: #ffffff; /* White text for contrast */
    animation: pulse-green 1s infinite alternate; /* Subtle pulse animation */
}
/* Hide text elements completely in stimulus state */
.state-stimulus #message,
.state-stimulus #result {
    display: none;
}

.state-too_early {
    background-color: #e74c3c; /* Alarm red */
    color: #ffffff; /* White text */
    animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both; /* Shake animation */
    transform: translate3d(0, 0, 0); /* Ensure hardware acceleration */
    backface-visibility: hidden;
    perspective: 1000px;
}
.state-too_early #message {
     opacity: 1;
     transform: translateY(0);
}
.state-too_early #result {
    opacity: 0;
    transform: translateY(20px);
}


.state-result {
     background-color: #3498db; /* Result blue */
     color: #ffffff; /* White text */
}
.state-result #message {
    display: none; /* Hide message in result state */
}
.state-result #result {
    opacity: 1;
    transform: translateY(0); /* Slide in */
    font-size: 2.5em; /* Larger font for result */
    font-weight: bold;
}


/* Animations */
@keyframes pulse-green {
    0% { transform: scale(1); }
    100% { transform: scale(1.02); }
}

@keyframes shake {
  10%, 90% { transform: translate3d(-1px, 0, 0); }
  20%, 80% { transform: translate3d(2px, 0, 0); }
  30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
  40%, 60% { transform: translate3d(4px, 0, 0); }
}


/* Button Styling */
#toggle-explanation {
    display: block;
    margin: 30px auto;
    padding: 12px 25px; /* More padding */
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    background-color: #3498db; /* Match result blue */
    color: white;
    border: none;
    border-radius: 6px; /* Slightly more rounded */
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#toggle-explanation:hover {
    background-color: #2980b9; /* Darker blue on hover */
    transform: translateY(-2px); /* Slight lift effect */
}
#toggle-explanation:active {
     transform: translateY(0); /* Press effect */
}


/* Explanation Styling */
#explanation {
    margin-top: 40px; /* More space */
    padding: 25px; /* More padding */
    background-color: #ecf0f1; /* Light neutral background */
    border-radius: 10px; /* Rounded corners */
    line-height: 1.7; /* More space between lines */
    color: #34495e; /* Darker text */
}

#explanation h2 {
    color: #2c3e50; /* Dark heading color */
    margin-top: 0;
    margin-bottom: 15px;
    border-bottom: 2px solid #bdc3c7; /* Subtle underline */
    padding-bottom: 10px;
}

#explanation p {
    margin-bottom: 18px; /* More space between paragraphs */
}

#explanation ul {
    padding-right: 25px; /* Padding for RTL list */
    margin-bottom: 18px;
}

#explanation li {
    margin-bottom: 10px; /* More space between list items */
}

/* Responsive adjustments */
@media (max-width: 600px) {
    #test-area {
        font-size: 1.4em;
        height: 350px;
        padding: 20px;
    }
     .state-result #result {
        font-size: 2em;
    }
    #reaction-test-app {
         min-height: 400px;
    }
    .app-container {
         min-height: 350px;
    }
    #toggle-explanation {
        font-size: 1em;
        padding: 10px 20px;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const testArea = document.getElementById('test-area');
    const messageDiv = document.getElementById('message');
    const resultDiv = document.getElementById('result');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    // States: 'initial', 'waiting_delay', 'stimulus', 'too_early', 'result'
    let state = 'initial';
    let startTime = null;
    let timeoutId = null; // For the random stimulus timeout
    let fixedDelayTimeoutId = null; // For a potential fixed 'get ready' delay (decided against a visible preparing state, but keeping the variable for clean timeout management)


    function setState(newState) {
        // Clear any active timeouts before changing state
        if (timeoutId) {
            clearTimeout(timeoutId);
            timeoutId = null;
        }
         if (fixedDelayTimeoutId) {
            clearTimeout(fixedDelayTimeoutId);
            fixedDelayTimeoutId = null;
        }

        state = newState;
        // Update class for styling and animations
        testArea.className = ''; // Remove all state classes
        testArea.classList.add(`state-${state}`);

        // Update messages and display visibility based on state
        messageDiv.style.opacity = 0; // Fade out both text elements initially
        resultDiv.style.opacity = 0;
        messageDiv.style.transform = 'translateY(20px)';
        resultDiv.style.transform = 'translateY(20px)';
         // Use requestAnimationFrame to ensure smooth transitions after class change
         requestAnimationFrame(() => {
             switch (state) {
                case 'initial':
                    messageDiv.textContent = 'לחץ כדי להתחיל';
                    resultDiv.textContent = '';
                    messageDiv.style.opacity = 1;
                    messageDiv.style.transform = 'translateY(0)';
                    break;
                case 'waiting_delay':
                    messageDiv.textContent = 'המתן...';
                    resultDiv.textContent = ''; // Ensure result is hidden
                    messageDiv.style.opacity = 1;
                    messageDiv.style.transform = 'translateY(0)';
                    // Start the random delay before stimulus
                    const delay = Math.random() * 2000 + 1000; // 1 to 3 seconds
                    timeoutId = setTimeout(showStimulus, delay);
                    break;
                case 'stimulus':
                    // Text is hidden by CSS in this state
                    startTime = performance.now();
                    break;
                case 'too_early':
                    messageDiv.textContent = 'מוקדם מדי! נסה שוב?';
                    resultDiv.textContent = '';
                    messageDiv.style.opacity = 1;
                    messageDiv.style.transform = 'translateY(0)';
                    break;
                case 'result':
                    // resultDiv text is set in handleClick
                     messageDiv.textContent = ''; // Ensure message is hidden
                    // Opacity and transform handled by state-result CSS
                    break;
            }
         });
    }

    function showStimulus() {
        if (state === 'waiting_delay') { // Only transition if still waiting
            setState('stimulus');
        }
         // timeoutId was already cleared in setState if state changed before timeout
    }

    function handleClick() {
        const clickTime = performance.now();

        switch (state) {
            case 'initial':
            case 'result':
            case 'too_early':
                // Start a new test cycle
                // A short fixed delay before waiting_delay gives a "reset" feel
                // setState('waiting_delay'); // Direct transition
                // Let's add a tiny delay for states to reset visually before waiting
                setState('waiting_delay');
                break;
            case 'waiting_delay':
                // Clicked too early
                setState('too_early');
                 // Clearing timeout handled by setState
                break;
            case 'stimulus':
                // Valid click after stimulus
                const reactionTime = clickTime - startTime;
                resultDiv.textContent = `${reactionTime.toFixed(0)} ms`; // Round to whole number for simplicity
                setState('result');
                break;
        }
    }

    // Add event listener to the test area
    testArea.addEventListener('click', handleClick);

    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר';
         // Optional: Scroll to explanation when shown
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Initial state setup on load
    setState('initial');
});
</script>
---