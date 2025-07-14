---
title: "האם אתם באמת יודעים כמה אתם יודעים?"
english_slug: are-you-really-as-good-as-you-think
category: "מדעי החברה / פסיכולוגיה"
tags:
  - אפקט דאנינג-קרוגר
  - הטיה קוגניטיבית
  - הערכה עצמית
  - מטא-קוגניציה
  - פסיכולוגיה חברתית
---
# מבחן ההערכה העצמית

חשבתם פעם שאתם שולטים בנושא מסוים, רק כדי לגלות שיש עומק שלא דמיינתם? עד כמה אנחנו באמת מודעים ליכולות שלנו, ובפרט - למגבלות שלנו? בואו נערוך ניסוי קצר ונגלה.

<div class="app-container">
    <div id="start-screen" class="screen active">
        <h2>הערכה עצמית: הניסוי</h2>
        <p>לפני שנתחיל ללמוד על הטיה פסיכולוגית מעניינת, בואו נבצע ניסוי קצר ופשוט. תתבקשו לענות על מספר שאלות בסיסיות, ולאחר מכן תצטרכו להעריך את ביצועיכם. היו כנים עם עצמכם, זו הדרך הטובה ביותר להפיק תובנות מהניסוי.</p>
        <button id="start-quiz-btn" class="interactive-button">התחילו את המבחן</button>
    </div>

    <div id="quiz-screen" class="screen">
        <h2>אתגרו את עצמכם</h2>
        <p class="quiz-instructions">ענו על השאלות הקצרות הבאות. בחרו את התשובה הטובה ביותר לכל שאלה.</p>
        <div id="questions-container">
            <!-- Questions will be loaded here by JS -->
        </div>
        <button id="submit-quiz-btn" class="interactive-button">סיימתי לענות</button>
         <p class="quiz-progress" style="text-align: center;"></p>
    </div>

    <div id="estimate-screen" class="screen">
        <h2>עצרו וחשבו: כמה צדקתם?</h2>
        <p>עניתם על כל השאלות. עכשיו, לפני שתראו את הציון האמיתי שלכם, קחו רגע והעריכו בכנות: מה אחוז התשובות הנכונות שלכם במבחן?</p>
        <div class="estimate-input">
            <input type="range" id="score-estimate" min="0" max="100" value="50" step="1">
            <span id="estimate-value">50%</span>
        </div>
        <button id="submit-estimate-btn" class="interactive-button">הצגת הציון שלי</button>
    </div>

    <div id="results-screen" class="screen">
        <h2>התוצאות המפתיעות (אולי)</h2>
        <div class="comparison-container">
            <div class="result-bar-container">
                <span class="bar-label">הערכה שלכם:</span>
                <div class="bar-wrapper">
                    <div class="bar" id="estimated-score-bar"></div>
                    <span class="bar-text" id="estimated-score-text"></span>
                </div>
            </div>
            <div class="result-bar-container">
                 <span class="bar-label">הציון האמיתי שלכם:</span>
                <div class="bar-wrapper">
                   <div class="bar" id="actual-score-bar"></div>
                   <span class="bar-text" id="actual-score-text"></span>
                </div>
            </div>
        </div>
        <p id="comparison-text" class="comparison-feedback"></p>
        <button id="show-explanation-btn" class="interactive-button">מה מסתתר מאחורי התוצאות האלה?</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-hover: #0056b3;
        --secondary-color: #ff9800; /* Orange for estimate */
        --success-color: #4CAF50; /* Green for actual */
        --warning-color: #f44336; /* Red for big discrepancy */
        --light-grey: #f4f4f4;
        --medium-grey: #ddd;
        --dark-grey: #333;
        --text-color: #555;
        --border-radius: 8px;
        --padding-medium: 20px;
        --animation-duration: 0.5s;
    }

    body {
         margin: 0;
         background-color: #eef2f7; /* Soft background */
         color: var(--text-color);
         font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
         direction: rtl;
         text-align: right;
         line-height: 1.6;
    }

    .app-container {
        max-width: 700px;
        margin: 40px auto;
        padding: var(--padding-medium);
        background-color: #ffffff;
        border-radius: var(--border-radius);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* For screen transitions */
        position: relative; /* For absolute positioning of screens */
    }

    h1 {
        color: var(--dark-grey);
        text-align: center;
        margin-bottom: var(--padding-medium);
        font-size: 2em;
    }

    h2 {
        color: var(--primary-color);
        text-align: center;
        margin-top: 0;
        margin-bottom: var(--padding-medium);
        font-size: 1.6em;
    }

    p {
         margin-bottom: 15px;
         color: var(--text-color);
    }

    .screen {
        width: 100%;
        opacity: 0;
        position: absolute;
        top: 0;
        left: 0; /* For potential slide animation */
        transition: opacity var(--animation-duration) ease-in-out, transform var(--animation-duration) ease-in-out;
        padding: var(--padding-medium);
        box-sizing: border-box;
        visibility: hidden;
        pointer-events: none; /* Disable interaction when not visible */
    }

    .screen.active {
        position: relative;
        opacity: 1;
        transform: translateX(0);
        visibility: visible;
        pointer-events: auto; /* Enable interaction */
    }

    #start-screen.active,
    #quiz-screen.active,
    #estimate-screen.active,
    #results-screen.active {
         /* Specific styling for active screens if needed, currently handled by .screen.active */
    }


    .interactive-button {
        display: block;
        width: auto;
        margin: var(--padding-medium) auto 10px auto;
        padding: 12px 25px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .interactive-button:hover {
        background-color: var(--primary-hover);
        transform: translateY(-2px);
    }

     .interactive-button:active {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
     }


    .quiz-instructions {
        text-align: center;
        font-style: italic;
        margin-bottom: var(--padding-medium);
    }

    .quiz-question {
        margin-bottom: var(--padding-medium);
        padding: 15px;
        border: 1px solid var(--medium-grey);
        border-radius: var(--border-radius);
        background-color: var(--light-grey);
        transition: background-color 0.3s ease;
    }

    .quiz-question p {
        margin-bottom: 10px;
        font-weight: bold;
        color: var(--dark-grey);
    }

    .quiz-options label {
        display: block;
        margin-bottom: 10px;
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background-color 0.2s ease;
    }

    .quiz-options label:hover {
         background-color: rgba(var(--primary-color, #007bff), 0.1); /* Subtle hover effect */
    }

    .quiz-options input[type="radio"] {
        margin-left: 8px; /* Space for RTL */
        vertical-align: middle;
        transform: scale(1.2); /* Slightly larger radio buttons */
    }

     .quiz-progress {
         margin-top: 15px;
         font-size: 0.9em;
         color: var(--text-color);
     }

    .estimate-input {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: var(--padding-medium);
        gap: 15px; /* Space between elements */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .estimate-input input[type="range"] {
        flex-grow: 1;
        max-width: 400px; /* Limit slider width */
         -webkit-appearance: none; /* Override default appearance */
         appearance: none;
         height: 8px;
         background: var(--medium-grey);
         border-radius: 5px;
         outline: none;
         opacity: 0.7;
         transition: opacity .2s;
         cursor: pointer;
    }

    .estimate-input input[type="range"]:hover {
        opacity: 1;
    }

    /* Custom slider thumb */
    .estimate-input input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .estimate-input input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }


    .estimate-input #estimate-value {
        min-width: 60px; /* Reserve space */
        text-align: center;
        font-weight: bold;
        color: var(--primary-color);
        font-size: 1.2em;
    }

    .comparison-container {
        margin-top: var(--padding-medium);
        display: flex;
        flex-direction: column; /* Stack bars vertically */
        gap: 15px;
    }

    .result-bar-container {
        display: flex;
        align-items: center;
        gap: 15px; /* Space between label and bar */
        flex-wrap: wrap; /* Allow wrapping */
    }

    .result-bar-container .bar-label {
        font-weight: bold;
        min-width: 120px; /* Ensure labels align */
        color: var(--dark-grey);
    }

    .bar-wrapper {
        flex-grow: 1;
        display: flex;
        align-items: center;
        gap: 10px; /* Space between bar and text */
    }

    .bar {
        height: 30px; /* Slightly taller bars */
        background-color: var(--success-color); /* Default color */
        border-radius: 4px;
        width: 0; /* Initial state for animation */
        transition: width 1.5s ease-out; /* Slower, smoother animation */
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        position: relative; /* For potential internal text */
        min-width: 5px; /* Ensure bar is visible even at 0% width */
    }

    #estimated-score-bar { background-color: var(--secondary-color); } /* Orange for estimate */
    #actual-score-bar { background-color: var(--success-color); } /* Green for actual */


    .bar-text {
        min-width: 50px; /* Space for percentage text */
        font-weight: bold;
        color: var(--dark-grey);
        text-align: left; /* Text after the bar */
    }

    .comparison-feedback {
        margin-top: var(--padding-medium);
        padding: 15px;
        border-radius: var(--border-radius);
        text-align: center;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color var(--animation-duration) ease;
    }

    .comparison-feedback.accurate {
        background-color: #e8f5e9; /* Light green */
        color: #2e7d32; /* Dark green */
    }

    .comparison-feedback.overestimate {
        background-color: #fff3e0; /* Light orange */
        color: #ef6c00; /* Dark orange */
    }

    .comparison-feedback.underestimate {
        background-color: #e3f2fd; /* Light blue */
        color: #0277bd; /* Dark blue */
    }

    .comparison-feedback.large-discrepancy {
        background-color: #ffebee; /* Light red */
        color: var(--warning-color); /* Red */
    }


    #explanation-section {
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid var(--medium-grey);
        opacity: 0; /* Initial state for fade-in */
        transition: opacity 1s ease-in-out;
        visibility: hidden;
        pointer-events: none;
    }

     #explanation-section.visible {
         opacity: 1;
         visibility: visible;
         pointer-events: auto;
     }


    #explanation-section h2 {
        color: var(--dark-grey);
        text-align: center;
        margin-bottom: 20px;
    }

    #explanation-section h3 {
        color: var(--primary-color);
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.3em;
    }

    #explanation-section p {
        margin-bottom: 15px;
    }

    #explanation-section ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list for RTL */
    }

    #explanation-section li {
        margin-bottom: 8px;
        color: var(--text-color);
    }

    @media (max-width: 600px) {
        .app-container {
            margin: 20px;
            padding: 15px;
        }
        h1 { font-size: 1.6em; }
        h2 { font-size: 1.4em; }
        .result-bar-container { flex-direction: column; align-items: flex-start; gap: 5px; }
        .result-bar-container .bar-label { min-width: auto; }
        .bar-wrapper { width: 100%; }
        .estimate-input { flex-direction: column; gap: 10px; }
        .estimate-input input[type="range"] { width: 100%; }
    }

</style>

<div id="explanation-section" style="display: none;"> <!-- display:none is just initial state before JS takes over visibility -->
    <h2>על מה זה היה? אפקט דאנינג-קרוגר בפעולה</h2>

    <h3>הבנת הפער: אפקט דאנינג-קרוגר</h3>
    <p>הניסוי הקצר שזה עתה עברתם מדגים עקרון פסיכולוגי מרתק הידוע בשם **אפקט דאנינג-קרוגר**. זוהי הטיה קוגניטיבית המתארת כיצד אנשים מעריכים את יכולותיהם בתחומים שונים.</p>
    <p>התופעה המרכזית היא שאנשים עם ידע או מיומנות **נמוכים** בתחום מסוים נוטים להעריך את יכולותיהם כ**גבוהות בהרבה** ממה שהן באמת. מדוע זה קורה? לעיתים קרובות, חוסר הידע שלהם מונע מהם להבין את המורכבות של הנושא, ולכן הם לא מבינים עד כמה הם למעשה לא יודעים. הם חסרים את ה"מטא-קוגניציה" – היכולת לחשוב על החשיבה שלהם ועל רמת הידע שלהם עצמם.</p>

    <h3>הצד השני של המטבע: "קללת הידע"</h3>
    <p>באופן מפתיע, בצד השני של הסקאלה, אנשים שהם **מומחים** או בעלי מיומנות **גבוהה** נוטים לעיתים להערכת חסר של יכולותיהם בהשוואה לאחרים. הסיבה לכך היא שהידע וההבנה העמוקה שלהם הופכים את הנושא ל"מובן מאליו" בעיניהם. הם מכירים את הדקויות, את המורכבויות ואת גודל הידע שעדיין קיים מחוץ לתחום המומחיות שלהם, וקשה להם להאמין שמה שקל וברור להם אינו כזה עבור רוב האנשים. זוהי תופעה המכונה לפעמים "קללת הידע".</p>

    <h3>למה קשה לנו להעריך את עצמנו?</h3>
    <p>הערכה עצמית מדויקת אינה משימה פשוטה. היא דורשת לא רק הבנה של הנושא עצמו, אלא גם מודעות ליכולותינו ביחס לאחרים ולסטנדרטים אובייקטיביים. הטיות קוגניטיביות אחרות, כמו הנטייה להתמקד במידע שמאשר את מה שאנחנו כבר חושבים (הטיית האישור) או הנטייה לייחס הצלחות לעצמנו וכישלונות לנסיבות חיצוניות (הטיית השירות העצמי), מקשות אף יותר על הערכה אובייקטיבית.</p>

    <h3>השפעות בחיי היום-יום</h3>
    <p>אפקט דאנינג-קרוגר משפיע עלינו בתחומים רבים: החל מבחירת קריירה והערכת ביצועים בעבודה, דרך למידה והכנה למבחנים, ועד דיונים פוליטיים וחברתיים בהם אנשים עם ידע מועט נוטים להיות הכי נחרצים בדעתם. מודעות להטיה זו קריטית כדי לקבל החלטות טובות יותר, ללמוד ביעילות ולהשתפר.</p>

    <h3>איך נוכל לשפר את ההערכה העצמית שלנו?</h3>
    <p>למרבה המזל, ניתן לצמצם את השפעת האפקט באמצעות:</p>
    <ul>
        <li>**קבלת משוב אמיתי:** לבקש חוות דעת מאנשים אחרים, במיוחד ממומחים או ממי שיש לו פרספקטיבה חיצונית.</li>
        <li>**המשך למידה והעמקה:** ככל שצוברים יותר ידע, כך גוברת גם המודעות לגודל הידע שעדיין חסר, וליתר הדקויות.</li>
        <li>**פיתוח מטא-קוגניציה:** לחשוב באופן מודע על תהליך החשיבה שלכם ועל רמת הביטחון שלכם בידע מסוים.</li>
        <li>**ספקנות בריאה:** לא לפחד להטיל ספק בידע שלכם ולחפש אימות או הפרכה.</li>
        <li>**השוואה לסטנדרטים:** במקום רק להשוות את עצמכם לאחרים, נסו להשוות את ביצועיכם לקריטריונים אובייקטיביים או למשימות ספציפיות.</li>
    </ul>
    <p>המודעות לאפקט דאנינג-קרוגר היא צעד משמעותי להבנה טובה יותר של עצמכם ושל העולם סביבכם. היא מעודדת צניעות בלמידה ושאיפה מתמדת להרחבת אופקים.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const appContainer = document.querySelector('.app-container');
        const screens = document.querySelectorAll('.screen');
        const startScreen = document.getElementById('start-screen');
        const quizScreen = document.getElementById('quiz-screen');
        const estimateScreen = document.getElementById('estimate-screen');
        const resultsScreen = document.getElementById('results-screen');
        const explanationSection = document.getElementById('explanation-section');

        const startQuizBtn = document.getElementById('start-quiz-btn');
        const submitQuizBtn = document.getElementById('submit-quiz-btn');
        const scoreEstimateSlider = document.getElementById('score-estimate');
        const estimateValueSpan = document.getElementById('estimate-value');
        const submitEstimateBtn = document.getElementById('submit-estimate-btn');
        const estimatedScoreBar = document.getElementById('estimated-score-bar');
        const actualScoreBar = document.getElementById('actual-score-bar');
        const estimatedScoreText = document.getElementById('estimated-score-text');
        const actualScoreText = document.getElementById('actual-score-text');
        const comparisonText = document.getElementById('comparison-text');
        const showExplanationBtn = document.getElementById('show-explanation-btn');
        const questionsContainer = document.getElementById('questions-container');
        const quizProgress = document.querySelector('.quiz-progress');


        let correctAnswersCount = 0;
        let totalQuestions = 0;
        let userEstimatedScore = 0;

        const questions = [
            {
                question: "מה התשובה הנכונה לתרגיל: 2 + 3 * 4?",
                options: ["20", "14", "10", "24"],
                answer: "14"
            },
            {
                question: "אם שלושה תפוחים עולים 6 שקלים, כמה יעלו 5 תפוחים מאותו סוג?",
                options: ["8 שקלים", "10 שקלים", "12 שקלים", "15 שקלים"],
                answer: "10 שקלים"
            },
            {
                question: "מהי המילה הבאה בסדרה? ינואר, פברואר, מרץ, ...",
                options: ["אפריל", "יוני", "מאי", "אוגוסט"],
                answer: "אפריל"
            },
            {
                question: "אדם קונה ספר ב-50 שקלים ומוכר אותו ב-60 שקלים. לאחר מכן קונה אותו שוב ב-70 שקלים ומוכר ב-80 שקלים. כמה סך הכל הרוויח או הפסיד האדם?",
                options: ["הפסיד 10 שקלים", "הרוויח 10 שקלים", "הרוויח 20 שקלים", "הרוויח 30 שקלים"],
                answer: "הרוויח 20 שקלים"
            },
            {
                question: "אם היום יום ראשון, איזה יום בשבוע יהיה בעוד 10 ימים?",
                options: ["יום רביעי", "יום חמישי", "יום שישי", "יום שבת"],
                answer: "יום רביעי"
            },
             {
                question: "איזו צורה שונה משלוש האחרות? (לפי מאפיין אחד או יותר)",
                options: ["ריבוע כחול", "עיגול כחול", "ריבוע אדום", "ריבוע ירוק"],
                answer: "עיגול כחול"
            }
        ];

        totalQuestions = questions.length;

        // --- Screen Management & Animation ---
        function showScreen(screenId) {
            screens.forEach(screen => {
                screen.classList.remove('active');
                 // Set initial state for transition before adding 'active'
                 screen.style.transform = 'translateX(0)'; // Reset potential transform
                 screen.style.opacity = 0;
                 screen.style.position = 'absolute'; // Position out of flow when inactive
                 screen.style.visibility = 'hidden';
                 screen.style.pointerEvents = 'none';

            });

            const activeScreen = document.getElementById(screenId);
            if (activeScreen) {
                 // Ensure it's visible and interactive before animating opacity/transform
                 activeScreen.style.position = 'relative'; // Bring back into flow
                 activeScreen.style.visibility = 'visible';
                 activeScreen.style.pointerEvents = 'auto';
                 // Allow a brief moment for display/position change before animating
                 requestAnimationFrame(() => {
                    activeScreen.classList.add('active');
                    // If doing slide animation, set initial transform here, e.g., translateX(100%)
                 });
            }
        }

        // --- Quiz Logic ---
        function displayQuestions() {
            questionsContainer.innerHTML = ''; // Clear previous questions
            questions.forEach((q, index) => {
                const questionElement = document.createElement('div');
                questionElement.classList.add('quiz-question');
                // Fade in each question with a slight delay
                questionElement.style.opacity = 0;
                questionElement.style.transform = 'translateY(20px)';
                setTimeout(() => {
                    questionElement.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
                    questionElement.style.opacity = 1;
                    questionElement.style.transform = 'translateY(0)';
                }, index * 100); // Stagger delay

                questionElement.innerHTML = `<p>שאלה ${index + 1} מתוך ${totalQuestions}: ${q.question}</p><div class="quiz-options"></div>`;
                const optionsContainer = questionElement.querySelector('.quiz-options');
                q.options.forEach((option, optionIndex) => {
                    const optionId = `q${index}-option${optionIndex}`;
                    optionsContainer.innerHTML += `
                        <div>
                            <input type="radio" id="${optionId}" name="question-${index}" value="${option}">
                            <label for="${optionId}">${option}</label>
                        </div>
                    `;
                });
                questionsContainer.appendChild(questionElement);
            });
             updateQuizProgress();
        }

        function updateQuizProgress() {
            const answeredCount = questions.filter((q, index) => document.querySelector(`input[name="question-${index}"]:checked`)).length;
            quizProgress.textContent = `ענית על ${answeredCount} מתוך ${totalQuestions} שאלות`;
        }

        function calculateScore() {
            correctAnswersCount = 0;
            questions.forEach((q, index) => {
                const selectedOption = document.querySelector(`input[name="question-${index}"]:checked`);
                if (selectedOption && selectedOption.value === q.answer) {
                    correctAnswersCount++;
                }
            });
            return Math.round((correctAnswersCount / totalQuestions) * 100);
        }

        // --- Event Listeners ---
        startQuizBtn.addEventListener('click', () => {
            showScreen('quiz-screen');
            displayQuestions();
             // Listen for radio button changes to update progress
            questionsContainer.querySelectorAll('input[type="radio"]').forEach(input => {
                input.addEventListener('change', updateQuizProgress);
            });
        });

        submitQuizBtn.addEventListener('click', () => {
             let allAnswered = true;
             for(let i = 0; i < totalQuestions; i++) {
                 if (!document.querySelector(`input[name="question-${i}"]:checked`)) {
                     allAnswered = false;
                     break;
                 }
             }

             if (!allAnswered) {
                 alert("אנא ענו על כל השאלות לפני שתמשיכו."); // Use a simple alert as per original
                 return;
             }

            showScreen('estimate-screen');
             // Calculate score here but keep it hidden
            calculateScore();
        });

        scoreEstimateSlider.addEventListener('input', () => {
            estimateValueSpan.textContent = `${scoreEstimateSlider.value}%`;
        });

        submitEstimateBtn.addEventListener('click', () => {
            userEstimatedScore = parseInt(scoreEstimateSlider.value);
            const actualScore = calculateScore(); // Recalculate just to be sure

            showScreen('results-screen');

            // Display scores immediately
            estimatedScoreText.textContent = `${userEstimatedScore}%`;
            actualScoreText.textContent = `${actualScore}%`;

            // Animate bars after a short delay to ensure screen is rendered
            setTimeout(() => {
                 estimatedScoreBar.style.width = `${userEstimatedScore}%`;
                 actualScoreBar.style.width = `${actualScore}%`;
            }, 100); // Small delay


            // Provide comparison text based on Dunning-Kruger logic
            const difference = userEstimatedScore - actualScore;
            let comparisonMsg = "";
            let feedbackClass = ""; // Class for styling the feedback text

            const absDifference = Math.abs(difference);

            if (absDifference <= 5) { // Very close
                comparisonMsg = "הערכה העצמית שלכם סופר מדויקת! כמעט זהה לציון האמיתי. יפה מאוד על המודעות העצמית.";
                feedbackClass = "accurate";
            } else if (absDifference <= 15) { // Slightly off
                 if (difference > 0) {
                     comparisonMsg = `הערכתם את עצמכם מעט גבוה יותר (${userEstimatedScore}%) מהציון האמיתי (${actualScore}%). פער קטן יחסית, אבל מעניין למה חשבתם שהציון גבוה יותר.`;
                     feedbackClass = "overestimate";
                 } else { // difference < 0
                     comparisonMsg = `הערכתם את עצמכם מעט נמוך יותר (${userEstimatedScore}%) מהציון האמיתי (${actualScore}%). הערכת חסר קלה, אולי אתם קצת קשים עם עצמכם?`;
                     feedbackClass = "underestimate";
                 }
            } else if (absDifference <= 30) { // Moderately off
                 if (difference > 0) {
                     comparisonMsg = `הערכתם את עצמכם גבוה למדי (${userEstimatedScore}%) ביחס לציון האמיתי (${actualScore}%). פער משמעותי שיכול ללמד על האופן שבו אנו תופסים את הידע שלנו.`;
                     feedbackClass = "overestimate";
                 } else { // difference < 0
                     comparisonMsg = `הערכתם את עצמכם נמוך למדי (${userEstimatedScore}%) ביחס לציון האמיתי (${actualScore}%). הערכת חסר בולטת, ייתכן שאינכם מודעים לגודל הידע שיש לכם.`;
                     feedbackClass = "underestimate";
                 }
            } else { // Significantly off
                 if (difference > 0) {
                     comparisonMsg = `וואו! יש פער גדול מאוד בין ההערכה העצמית שלכם (${userEstimatedScore}%) לציון האמיתי (${actualScore}%). הערכת יתר כה גדולה היא דוגמה קלאסית לתופעה שנדבר עליה מיד.`;
                     feedbackClass = "large-discrepancy overestimate";
                 } else { // difference < 0
                     comparisonMsg = `וואו! יש פער גדול מאוד בין ההערכה העצמית שלכם (${userEstimatedScore}%) לציון האמיתי (${actualScore}%). הערכת חסר כה גדולה פחות שכיחה אבל גם היא מרתקת.`;
                     feedbackClass = "large-discrepancy underestimate";
                 }
            }

            comparisonText.textContent = comparisonMsg;
            comparisonText.className = 'comparison-feedback ' + feedbackClass; // Apply feedback class

            // Show the button to reveal the explanation
            showExplanationBtn.style.display = 'block';
        });

        showExplanationBtn.addEventListener('click', () => {
            explanationSection.classList.add('visible');
            showExplanationBtn.style.display = 'none'; // Hide the button once clicked
            // Optional: scroll down to the explanation section
            explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });

        // Initial screen setup
        showScreen('start-screen');
         // Initially hide explanation section using JS as well to manage transitions
         explanationSection.style.display = 'block'; // Make it block initially so JS can control visibility/opacity
         explanationSection.classList.remove('visible'); // Hide it via class for transition

    });
</script>
```