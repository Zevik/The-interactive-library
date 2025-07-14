---
title: "המילים הסמויות שמשפיעות עליך"
english_slug: hidden-words-that-influence-you
category: "פסיכולוגיה"
tags:
  - הטרמה
  - פסיכולוגיה קוגניטיבית
  - תת מודע
  - עיבוד מידע
  - השפעה סמויה
---
# המילים הסמויות שמשפיעות עליך

האם ייתכן שרמזים ויזואליים שחולפים על פניך במהירות מסחררת, אפילו מבלי שתהיה מודע לכך במפורש, משפיעים עמוקות על תהליכי המחשבה והתגובה שלך? גלה כעת, בניסוי קצר ומאתגר, עד כמה המוח שלך קולט ומושפע ממידע תת-ספי!

<div id="app-container">
    <div id="initial-screen">
         <h2>ניסוי זיהוי מילים מהיר</h2>
        <p>בסימולציה זו, תשתתף/י בגרסה פשוטה של ניסוי קלאסי בפסיכולוגיה קוגניטיבית.</p>
        <p>בכל שלב, יופיע לרגע קצר מאוד רמז סמוי (מילת מטרמה - אולי כלל לא תשים/י לב אליה), ומיד אחריה תופיע מחרוזת אותיות נוספת (מילת מטרה).</p>
        <p><strong>המשימה שלך:</strong> להחליט במהירות שיא האם מחרוזת האותיות <strong>השנייה</strong> היא מילה אמיתית בעברית או סתם צירוף חסר משמעות.</p>
        <p>הקש/י על הכפתור "מילה" אם זו מילה אמיתית, ועל "לא מילה" אם לאו. נסה/י להגיב כמה שיותר מהר ומדויק!</p>
        <p class="tip">ניתן גם להשתמש במקשים <strong>מ</strong> (מילה) ו-<strong>ל</strong> (לא מילה).</p>
        <button id="start-button">התחל ניסוי</button>
    </div>

    <div id="trial-screen" style="display: none;">
        <div id="progress-bar-container"><div id="progress-bar"></div></div>
        <div id="trial-counter"></div>
         <div id="stimulus-area">
            <div id="fixation-cross" class="stimulus-item">+</div>
            <div id="prime-display" class="stimulus-item"></div>
            <div id="target-display" class="stimulus-item"></div>
        </div>
        <div id="response-buttons">
            <button id="yes-button" data-response="true">מילה</button>
            <button id="no-button" data-response="false">לא מילה</button>
        </div>
         <div id="feedback" class="feedback-text"></div>
    </div>

    <div id="results-screen" style="display: none;">
        <h2>תוצאות הניסוי שלך</h2>
        <div id="results-summary"></div>
        <button id="explanation-button" style="margin-top: 20px;">הצג הסבר</button>
    </div>
</div>

<div id="explanation-content" style="display: none;">
    <h2>מה למדנו? תופעת ההטרמה (Priming)</h2>
    <ul>
        <li><strong>מהי תופעת ההטרמה בפסיכולוגיה קוגניטיבית?</strong><br>הטרמה היא תופעה שבה חשיפה קודמת לגירוי (מילת מטרמה או Prime) משפיעה על האופן שבו המוח מעבד גירוי מאוחר יותר (מילת מטרה או Target), לרוב על ידי הפיכת העיבוד למהיר או קל יותר. ההשפעה יכולה להתרחש גם כשהחשיפה הראשונית אינה מודעת או קצרה מכדי עיבוד מלא ומודע.</li>
        <li><strong>כיצד הטרמה משפיעה על מחשבות ותגובות, אפילו ללא מודעות?</strong><br>חשיפה קצרה, אפילו לשבריר שנייה, יכולה "להפעיל" (לעשות אקטיבציה) מושגים קשורים במוח (מילים, אסוציאציות). הפעלה מוקדמת זו מקלה על זיהוי או עיבוד של מידע קשור בהמשך, וכך משפיעה על תגובות, שיפוטים והחלטות, מבלי שנהיה מודעים כלל למקור ההשפעה. המוח שלנו פועל כל הזמן ברמה אוטומטית ולא מודעת, קולט ומעבד מידע סמוי.</li>
        <li><strong>סוגי הטרמה: סמנטית, אסוציאטיבית ותפיסתית.</strong><br>הטרמה <strong>סמנטית</strong>: מילים קשורות במשמעות ("רופא" <- "אחות"). הטרמה <strong>אסוציאטיבית</strong>: מילים שנוטות להופיע יחד ("לחם" <- "חמאה"). הטרמה <strong>תפיסתית</strong>: דמיון במאפיינים פיזיים (למשל, צורה או קו). הניסוי שביצעת מתמקד בהטרמה סמנטית/אסוציאטיבית.</li>
        <li><strong>משימת ההחלטה הלקסיקלית (Lexical Decision Task).</strong><br>זו משימה ניסויית סטנדרטית שבה המשתתף מחליט במהירות האם מחרוזת אותיות היא מילה אמיתית בשפה. זו דרך מצוינת למדוד כמה מהר ויעיל המוח ניגש למאגר המילים שלו.</li>
        <li><strong>אופן ביצוע ניסויי הטרמה עם משימה זו.</strong><br>כמו בניסוי שחווית: מציגים Prime קצר מאוד (כמה עשרות מילישניות) ואז מיד את ה-Target. המשימה היא להחליט על ה-Target. לעיתים קרובות ה-Prime כה קצר שהוא לא מעובד במודע.</li>
        <li><strong>מדוע זמן התגובה (Reaction Time - RT) הוא המדד המרכזי?</strong><br>זמן התגובה הוא אינדיקטור ישיר למהירות ויעילות העיבוד הקוגניטיבי. תגובה מהירה יותר = עיבוד "זורם" יותר. הטרמה מקצרת את זמן התגובה למילים קשורות, וזהו "אפקט ההטרמה" - ה-Prime הכין את המוח לעיבוד ה-Target.</li>
        <li><strong>הממצאים הטיפוסיים.</strong><br>ברוב ניסויי ההטרמה הסמנטית/אסוציאטיבית, אנשים מגיבים מהר יותר ו/או מדויק יותר כאשר ה-Prime קשור ל-Target (למשל, "מיטה" לפני "שינה"), לעומת Prime לא קשור ("ענן" לפני "שינה"). ההפרש הזה בזמני התגובה (Priming Effect) הוא ההוכחה להשפעת הגירוי הסמוי.</li>
        <li><strong>הסבר אפשרי לתופעה: אקטיבציה של רשתות סמנטיות.</strong><br>הידע שלנו מאורגן כרשת של מושגים מקושרים במוח. חשיפה ל-Prime מפעילה את הייצוג שלו ברשת, והפעלה זו מתפשטת דרך הקשרים למושגים קשורים. כשה-Target מופיע, אם הוא כבר "מופעל למחצה" בזכות ה-Prime, הוא מזוהה ומעובד מהר יותר.</li>
        <li><strong>השלכות בחיי היומיום.</strong><br>הטרמה היא לא רק תופעת מעבדה; היא משפיעה עלינו כל הזמן! היא רלוונטית להבנת קריאה, השפעות פרסום (גם סמוי), יצירת סטריאוטיפים והשפעתם על שיפוטים, והבנת תהליכי עיבוד מידע אוטומטיים ולא מודעים שמעצבים את התפיסה והתגובות שלנו בעולם.</li>
    </ul>
</div>


<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    #app-container {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: center;
        margin: 30px auto; /* Center the container */
        padding: 30px;
        border-radius: 12px;
        max-width: 650px;
        background: linear-gradient(135deg, #e0f7fa, #ffffff); /* Subtle gradient */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        color: #333;
        overflow: hidden; /* Prevents shadow issues with internal elements */
    }

     h1, h2 {
        color: #0056b3; /* A strong blue */
        margin-bottom: 20px;
        font-weight: 700;
    }

    #initial-screen p {
        margin-bottom: 15px;
        line-height: 1.6;
    }

     .tip {
         font-size: 0.9em;
         color: #555;
         margin-top: 15px;
     }


    #start-button, #yes-button, #no-button, #explanation-button {
        padding: 12px 25px;
        font-size: 18px;
        cursor: pointer;
        margin: 8px;
        border: none;
        border-radius: 30px; /* Pill shape */
        color: white;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #start-button {
         background-color: #007bff; /* Primary blue */
    }
     #start-button:hover {
         background-color: #0056b3;
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
     }

    #yes-button {
        background-color: #28a745; /* Success green */
    }
     #yes-button:hover {
        background-color: #218838;
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
     }


    #no-button {
        background-color: #dc3545; /* Danger red */
    }
     #no-button:hover {
        background-color: #c82333;
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
     }

     #explanation-button {
        background-color: #6c757d; /* Secondary grey */
         margin-left: auto;
         margin-right: auto;
         display: block; /* Center button */
    }
     #explanation-button:hover {
        background-color: #5a6268;
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
     }

     button:active {
         transform: scale(0.98); /* Add a slight press effect */
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }


    #trial-screen {
         position: relative; /* Needed for absolute positioning of children */
         min-height: 300px; /* Ensure screen has height */
         display: flex;
         flex-direction: column;
         justify-content: center;
         align-items: center;
    }

     #progress-bar-container {
        width: 100%;
        height: 8px;
        background-color: #eee;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 20px;
     }

     #progress-bar {
        height: 100%;
        width: 0%;
        background-color: #007bff;
        transition: width 0.3s ease-in-out;
     }

    #trial-counter {
        font-size: 1em;
        color: #555;
        margin-bottom: 20px;
        min-height: 1.2em; /* Reserve space */
    }


    #stimulus-area {
        position: relative; /* Container for positioned items */
        width: 100%;
        min-height: 150px; /* Enough space for stimuli */
        display: flex; /* Use flex to center the container itself */
        justify-content: center;
        align-items: center;
        flex-grow: 1; /* Allow stimulus area to take available space */
    }

    .stimulus-item {
         position: absolute; /* Position all items in the same spot */
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         font-weight: bold;
         opacity: 0; /* Start invisible */
         transition: opacity 0.05s linear; /* Fast fade transition */
    }

     #fixation-cross {
         font-size: 36px;
         color: #555;
         transition: opacity 0.1s ease-out; /* Slightly slower fade for cross */
     }

    #prime-display {
        font-size: 28px;
        color: #007bff;
    }

    #target-display {
        font-size: 60px; /* Larger for emphasis */
        color: #333;
    }

     #response-buttons {
        margin-top: 30px;
        z-index: 10; /* Ensure buttons are clickable over stimulus area */
     }

    .feedback-text {
        margin-top: 20px;
        font-size: 20px;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space */
        opacity: 0;
        transition: opacity 0.3s ease-out;
    }

    #results-screen {
        margin-top: 20px;
        text-align: right; /* Align results text right */
        padding: 20px;
        background-color: #e9ecef; /* Light grey background */
        border-radius: 8px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    #results-screen h2 {
        text-align: center;
        margin-bottom: 15px;
        color: #0056b3;
    }

    #results-summary p {
        margin-bottom: 10px;
        line-height: 1.5;
    }

     #explanation-content {
         margin-top: 30px; /* More space from results */
         padding: 25px;
         border: 1px solid #b3e5fc; /* Light blue border */
         border-radius: 8px;
         background-color: #e1f5fe; /* Very light blue */
         text-align: right;
         line-height: 1.6;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    #explanation-content h2 {
        text-align: center;
        margin-bottom: 20px;
         color: #004085; /* Darker blue for explanation header */
    }

    #explanation-content ul {
        list-style: disc; /* Use standard bullets */
        padding-right: 20px; /* Padding for bullets */
    }

    #explanation-content li {
        margin-bottom: 20px; /* More space between points */
        padding-bottom: 15px;
        border-bottom: 1px dashed #b3e0dc; /* Dashed separator */
    }

     #explanation-content li:last-child {
         border-bottom: none; /* No border after last item */
     }

     #explanation-content li strong {
         display: block;
         margin-bottom: 8px;
         color: #0056b3; /* Highlight key terms */
     }


</style>

<script>
    const initialScreen = document.getElementById('initial-screen');
    const trialScreen = document.getElementById('trial-screen');
    const resultsScreen = document.getElementById('results-screen');
    const stimulusAreaDiv = document.getElementById('stimulus-area');
    const fixationCross = document.getElementById('fixation-cross');
    const primeDisplay = document.getElementById('prime-display');
    const targetDisplay = document.getElementById('target-display');
    const responseButtonsDiv = document.getElementById('response-buttons');
    const startButton = document.getElementById('start-button');
    const yesButton = document.getElementById('yes-button');
    const noButton = document.getElementById('no-button');
    const feedbackDiv = document.getElementById('feedback');
    const resultsSummary = document.getElementById('results-summary');
    const explanationButton = document.getElementById('explanation-button');
    const explanationContent = document.getElementById('explanation-content');
    const trialCounterDiv = document.getElementById('trial-counter');
    const progressBar = document.getElementById('progress-bar');

    let trials = [
        // Related Word Pairs
        { prime: 'אחות', target: 'בית חולים', isWord: true, relation: 'related' },
        { prime: 'לחם', target: 'חמאה', isWord: true, relation: 'related' },
        { prime: 'קפה', target: 'תה', isWord: true, relation: 'related' },
        { prime: 'שמש', target: 'יום', isWord: true, relation: 'related' },
        { prime: 'כיסא', target: 'שולחן', isWord: true, relation: 'related' },
        { prime: 'רופא', target: 'מרפאה', isWord: true, relation: 'related' },
        { prime: 'גבוה', target: 'נמוך', isWord: true, relation: 'related' }, // Antonyms
        { prime: 'ציפור', target: 'קן', isWord: true, relation: 'related' },
        { prime: 'מים', target: 'אש', isWord: true, relation: 'related' }, // Antonyms
        { prime: 'דבש', target: 'מתוק', isWord: true, relation: 'related' },
        { prime: 'תלמיד', target: 'בית ספר', isWord: true, relation: 'related' },
        { prime: 'מלחמה', target: 'שלום', isWord: true, relation: 'related' }, // Antonyms

        // Unrelated Word Pairs
        { prime: 'ענן', target: 'בית חולים', isWord: true, relation: 'unrelated' },
        { prime: 'כיסא', target: 'חמאה', isWord: true, relation: 'unrelated' },
        { prime: 'סלע', target: 'תה', isWord: true, relation: 'unrelated' },
        { prime: 'ספר', target: 'יום', isWord: true, relation: 'unrelated' },
        { prime: 'ענן', target: 'שולחן', isWord: true, relation: 'unrelated' },
        { prime: 'שעון', target: 'מרפאה', isWord: true, relation: 'unrelated' },
        { prime: 'רחב', target: 'נמוך', isWord: true, relation: 'unrelated' },
        { prime: 'מכונית', target: 'קן', isWord: true, relation: 'unrelated' },
        { prime: 'עץ', target: 'שמיים', isWord: true, relation: 'unrelated' },
        { prime: 'אבן', target: 'מתוק', isWord: true, relation: 'unrelated' },
        { prime: 'נהר', target: 'בית ספר', isWord: true, relation: 'unrelated' },
        { prime: 'פרח', target: 'שלום', isWord: true, relation: 'unrelated' },


        // Non-word targets (Prime can be anything, doesn't matter for non-words)
        { prime: 'שולחן', target: 'בלבץ', isWord: false, relation: 'nonword' },
        { prime: 'ענן', target: 'בלבץ', isWord: false, relation: 'nonword' },
        { prime: 'קפה', target: 'צקרה', isWord: false, relation: 'nonword' },
        { prime: 'סלע', target: 'צקרה', isWord: false, relation: 'nonword' },
        { prime: 'כיסא', target: 'טלקח', isWord: false, relation: 'nonword' },
        { prime: 'ענן', target: 'טלקח', isWord: false, relation: 'nonword' },
        { prime: 'רופא', target: 'שפרע', isWord: false, relation: 'nonword' },
        { prime: 'שעון', target: 'שפרע', isWord: false, relation: 'nonword' },
         { prime: 'שמש', target: 'גבבה', isWord: false, relation: 'nonword' },
         { prime: 'ספר', target: 'גבבה', isWord: false, relation: 'nonword' },
         { prime: 'לחם', target: 'דרכף', isWord: false, relation: 'nonword' },
         { prime: 'כיסא', target: 'דרכף', isWord: false, relation: 'nonword' },
         { prime: 'דבש', target: 'חנרש', isWord: false, relation: 'nonword' },
         { prime: 'תלמיד', target: 'חנרש', isWord: false, relation: 'nonword' },
         { prime: 'מלחמה', target: 'קטבל', isWord: false, relation: 'nonword' },
         { prime: 'פרח', target: 'קטבל', isWord: false, relation: 'nonword' },

    ];

    let currentTrialIndex = 0;
    let startTime = 0;
    const results = []; // Store { rt, correct, relation, isWord } for each trial
    const primeDuration = 60; // ms (Classic range is 50-100ms)
    const fixationDuration = 500; // ms - time showing the '+'
    const feedbackDuration = 700; // ms - duration to show feedback and wait before next trial

    // Preload some characters/fonts to avoid flicker? Maybe overkill for this, but good practice.

    function shuffleArray(array) {
        const shuffled = [...array]; // Create a copy
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]; // Swap elements
        }
        return shuffled;
    }

    let shuffledTrials = [];

    function startSimulation() {
        initialScreen.style.display = 'none';
        resultsScreen.style.display = 'none';
        explanationContent.style.display = 'none';
        explanationButton.style.display = 'none';
        trialScreen.style.display = 'flex'; // Use flex for trial screen layout
        responseButtonsDiv.style.display = 'none'; // Buttons start hidden
        feedbackDiv.style.opacity = 0;
        results.length = 0; // Clear previous results
        currentTrialIndex = 0;
        shuffledTrials = shuffleArray(trials); // Randomize trial order
        updateProgressBar();
        updateTrialCounter();
        runTrial();
    }

    function updateProgressBar() {
        const progress = (currentTrialIndex / shuffledTrials.length) * 100;
        progressBar.style.width = `${progress}%`;
    }

     function updateTrialCounter() {
         trialCounterDiv.textContent = `שלב ${currentTrialIndex + 1} מתוך ${shuffledTrials.length}`;
     }


    function runTrial() {
        if (currentTrialIndex >= shuffledTrials.length) {
            endSimulation();
            return;
        }

        const trial = shuffledTrials[currentTrialIndex];

        // Reset displays and hide feedback/buttons
        primeDisplay.textContent = '';
        primeDisplay.style.opacity = 0;
        targetDisplay.textContent = '';
        targetDisplay.style.opacity = 0;
        feedbackDiv.style.opacity = 0;
        responseButtonsDiv.style.display = 'none';
         fixationCross.style.opacity = 0; // Ensure cross is hidden initially


        // 1. Show Fixation Cross
        fixationCross.style.opacity = 1;
        setTimeout(() => {
            fixationCross.style.opacity = 0; // Hide cross

            // 2. Show Prime
             primeDisplay.textContent = trial.prime;
             primeDisplay.style.opacity = 1;


            setTimeout(() => {
                // 3. Hide Prime & Show Target Immediately
                primeDisplay.style.opacity = 0; // Hide prime

                 targetDisplay.textContent = trial.target;
                 targetDisplay.style.opacity = 1;

                startTime = performance.now(); // Start timing when target appears
                responseButtonsDiv.style.display = 'block'; // Show buttons
                addKeyListener(); // Add keyboard listener when buttons are visible

            }, primeDuration); // Prime duration

        }, fixationDuration); // Fixation duration
    }

    function handleResponse(isUserWord) {
        removeKeyListener(); // Remove keyboard listener immediately after response

        const endTime = performance.now();
        const reactionTime = endTime - startTime;
        const trial = shuffledTrials[currentTrialIndex];
        const isCorrect = isUserWord === trial.isWord;

        // Disable buttons immediately after response (visual cue handled by CSS active state)
         // responseButtonsDiv.style.display = 'none'; // Wait until feedback fades to hide buttons

        // Store result
        results.push({
            rt: reactionTime,
            correct: isCorrect,
            relation: trial.relation,
            isWord: trial.isWord,
            prime: trial.prime, // Store for debugging/analysis if needed
            target: trial.target // Store for debugging/analysis if needed
        });

        // Show brief feedback
        feedbackDiv.textContent = isCorrect ? 'נכון!' : 'לא נכון!';
        feedbackDiv.style.color = isCorrect ? '#28a745' : '#dc3545';
        feedbackDiv.style.opacity = 1;

        currentTrialIndex++;
        updateProgressBar();
        updateTrialCounter();

        // Clear displays and move to next trial after feedback duration
        setTimeout(() => {
             targetDisplay.style.opacity = 0; // Hide target
             feedbackDiv.style.opacity = 0; // Hide feedback
             responseButtonsDiv.style.display = 'none'; // Hide buttons
            runTrial();
        }, feedbackDuration);
    }

    function addKeyListener() {
        window.addEventListener('keydown', handleKeyPress);
    }

    function removeKeyListener() {
        window.removeEventListener('keydown', handleKeyPress);
    }

    function handleKeyPress(event) {
        // Check if buttons are currently displayed
        if (responseButtonsDiv.style.display !== 'none') {
            if (event.key === 'מ') { // Hebrew 'Mem' for 'מילה'
                handleResponse(true);
            } else if (event.key === 'ל') { // Hebrew 'Lamed' for 'לא מילה'
                handleResponse(false);
            }
        }
    }


    function endSimulation() {
        trialScreen.style.display = 'none';
        responseButtonsDiv.style.display = 'none';
        feedbackDiv.style.opacity = 0;

        // Calculate average RTs for correct word responses based on relation
        const correctWordResponses = results.filter(r => r.correct && r.isWord && (r.relation === 'related' || r.relation === 'unrelated'));

        const relatedRTs = correctWordResponses
            .filter(r => r.relation === 'related')
            .map(r => r.rt);

        const unrelatedRTs = correctWordResponses
            .filter(r => r.relation === 'unrelated')
            .map(r => r.rt);

        const avgRelatedRT = relatedRTs.length > 0 ? relatedRTs.reduce((sum, rt) => sum + rt, 0) / relatedRTs.length : 0;
        const avgUnrelatedRT = unrelatedRTs.length > 0 ? unrelatedRTs.reduce((sum, rt) => sum + rt, 0) / unrelatedRTs.length : 0;

         // Calculate accuracy for words and non-words
         const wordResponses = results.filter(r => r.isWord);
         const nonWordResponses = results.filter(r => !r.isWord);
         const correctWordCount = wordResponses.filter(r => r.correct).length;
         const correctNonWordCount = nonWordResponses.filter(r => r.correct).length;
         const wordAccuracy = wordResponses.length > 0 ? (correctWordCount / wordResponses.length) * 100 : 0;
         const nonWordAccuracy = nonWordResponses.length > 0 ? (correctNonWordCount / nonWordResponses.length) * 100 : 0;
         const overallAccuracy = results.length > 0 ? results.filter(r => r.correct).length / results.length * 100 : 0;


        resultsScreen.style.display = 'block';

        let resultsHTML = `
            <p><strong>דיוק כולל:</strong> ${overallAccuracy.toFixed(1)}%</p>
            <p><strong>דיוק בזיהוי מילים:</strong> ${wordAccuracy.toFixed(1)}%</p>
            <p><strong>דיוק בזיהוי לא-מילים:</strong> ${nonWordAccuracy.toFixed(1)}%</p>
            <br/>
        `;


        if (avgRelatedRT > 0 && avgUnrelatedRT > 0) {
             resultsHTML += `
                <p>זמן תגובה ממוצע (תגובות נכונות בלבד) עבור <strong>מילים קשורות</strong>: ${avgRelatedRT.toFixed(0)} מילישניות</p>
                <p>זמן תגובה ממוצע (תגובות נכונות בלבד) עבור <strong>מילים לא קשורות</strong>: ${avgUnrelatedRT.toFixed(0)} מילישניות</p>
                <br>
                <p><strong>הפרש זמן תגובה (אפקט הטרמה):</strong> ${Math.abs(avgUnrelatedRT - avgRelatedRT).toFixed(0)} מילישניות</p>
            `;

            if (avgRelatedRT < avgUnrelatedRT) {
                resultsHTML += `<p style="color: #28a745; font-weight: bold;">כצפוי בניסויי הטרמה, הייתה לך תגובה מהירה יותר למילים קשורות! המוח שלך עבד מהר יותר בזכות הרמז הסמוי.</p>`;
            } else if (avgRelatedRT > avgUnrelatedRT) {
                 resultsHTML += `<p style="color: #ffc107; font-weight: bold;">בניסוי זה, זמן התגובה למילים קשורות היה מעט ארוך יותר. לעיתים קרובות האפקט קטן ומשתנה מאדם לאדם. בניסויים גדולים יותר, אפקט ההטרמה הקשורה בדרך כלל ברור יותר.</p>`;
            } else {
                 resultsHTML += `<p style="color: #ffc107; font-weight: bold;">זמני התגובה למילים קשורות ולא קשורות היו דומים מאוד בניסוי זה. האפקט יכול להיות עדין ומשתנה. בניסויים גדולים יותר, הוא לרוב מובהק יותר.</p>`;
            }

        } else {
            resultsHTML += "<p>לא נאספו מספיק תגובות נכונות על מילים קשורות ולא קשורות כדי לחשב ממוצעים משמעותיים.</p>";
        }

        resultsSummary.innerHTML = resultsHTML;
        explanationButton.style.display = 'block'; // Show explanation button
    }


    // Event Listeners
    startButton.addEventListener('click', startSimulation);
    yesButton.addEventListener('click', () => handleResponse(true));
    noButton.addEventListener('click', () => handleResponse(false));
     explanationButton.addEventListener('click', () => {
        if (explanationContent.style.display === 'none') {
            explanationContent.style.display = 'block';
            explanationButton.textContent = 'הסתר הסבר';
        } else {
            explanationContent.style.display = 'none';
            explanationButton.textContent = 'הצג הסבר';
        }
    });

    // Initial state setup (optional, but good practice)
    initialScreen.style.display = 'block';
    trialScreen.style.display = 'none';
    resultsScreen.style.display = 'none';
    explanationContent.style.display = 'none';
    explanationButton.style.display = 'none';


</script>
---
```