---
title: "למידת העברה: כוח העבר ליצירת AI יעיל יותר"
english_slug: transfer-learning-shortcut-ai-training
category: "טכנולוגיה / בינה מלאכותית"
tags:
  - למידת מכונה
  - למידת העברה
  - רשתות נוירונים
  - AI
  - למידה עמוקה
---
<h1>למידת העברה: כוח העבר ליצירת AI יעיל יותר</h1>
<p>האם ידעתם שכמו בני אדם המשתמשים בידע קיים ללמידת מיומנויות חדשות, גם מודלי בינה מלאכותית יכולים "להעביר" ידע? זוהי טכניקת קסם אמיתית שמאפשרת לנו לאמן מודלים חדשים במהירות וביעילות חסרות תקדים. בואו נגלה איך זה עובד באמצעות הדמיה.</p>

<div class="interactive-app">
    <h2>בחנו בעצמכם: הדמיית אימון מודלי AI</h2>

    <div id="task1-section" class="step-container">
        <h3>משימה 1: הכרת הבסיס (זיהוי ריבועים מול עיגולים)</h3>
        <p>נתחיל במסע האימון שלנו. אנו מאמנים מודל AI קטן מאפס לזהות צורות פשוטות במיוחד.</p>
        <button id="start-task1" class="action-button">התחילו את האימון הראשון!</button>
        <div id="task1-progress" class="progress-container" style="display: none;">
             <div class="progress-label">המודל לומד...</div>
            <div class="progress-bar-container"><div id="task1-progress-bar" class="progress-bar"></div></div>
            <div class="progress-details">
                <span>אפוכים: <span id="task1-epochs">0</span> / <span id="task1-total-epochs"></span></span>
                <span>דיוק נוכחי: <span id="task1-accuracy">0.0%</span></span>
            </div>
        </div>
        <div id="task1-results" class="results-container" style="display: none;">
            <h4>&#x2705; משימה 1 הושלמה בהצלחה!</h4>
            <p>המודל סיים את האימון לאחר <span id="task1-completed-epochs"></span> אפוכים.</p>
            <p>דיוק סופי: <span id="task1-final-accuracy"></span>%</p>
            <button id="continue-to-task2" class="action-button">המשך לאתגר הבא</button>
        </div>
    </div>

    <div id="task2-intro" class="step-container" style="display: none;">
        <h3>משימה 2: האתגר הבא (זיהוי משולשים מול מלבנים)</h3>
        <p>כעת עומדת בפנינו משימה דומה אך שונה: סיווג צורות אחרות. האם נאמן מודל חדש לחלוטין, או ננצל את הידע שצבר המודל מהמשימה הקודמת?</p>
         <div class="choice-buttons">
            <button id="choose-scratch" class="action-button secondary">אפשרות א': אימון מאפס</button>
            <button id="choose-transfer" class="action-button primary">אפשרות ב': למידת העברה (מומלץ!)</button>
        </div>
    </div>

    <div id="task2-options" class="step-container" style="display: none;">
         <h3>הכנת המודל ללמידת העברה</h3>
         <p>בחר אילו 'שכבות' מהמודל המאומן (ממשימה 1) תרצה להשאיר 'קפואות' (משקולות שלא ישתנו באימון החדש). שכבות קדומות (קרוב לקלט) בדרך כלל לומדות תכונות גנריות שניתן להעביר בקלות. השכבות האחרונות (הקרובות לפלט) יוחלפו ויתאמנו בכל מקרה למשימה החדשה.</p>
         <div class="layer-options">
            <label class="checkbox-label"><input type="checkbox" class="freeze-layer" checked> השאר שכבה 1 קפואה (מזהה קווים ותכונות בסיס)</label>
            <label class="checkbox-label"><input type="checkbox" class="freeze-layer" checked> השאר שכבה 2 קפואה (מזהה צורות פשוטות)</label>
            <label class="checkbox-label"><input type="checkbox" class="freeze-layer"> השאר שכבה 3 קפואה (מזהה צורות מורכבות יותר)</label>
         </div>
         <button id="start-task2-transfer" class="action-button">התחילו את אימון למידת ההעברה!</button>
    </div>


     <div id="task2-scratch-progress" class="progress-container" style="display: none;">
        <h3>משימה 2: אימון מאפס</h3>
        <div class="progress-label">בונה הכל מחדש...</div>
        <div class="progress-bar-container"><div id="task2-scratch-progress-bar" class="progress-bar"></div></div>
        <div class="progress-details">
            <span>אפוכים: <span id="task2-scratch-epochs">0</span> / <span id="task2-scratch-total-epochs"></span></span>
            <span>דיוק נוכחי: <span id="task2-scratch-accuracy">0.0%</span></span>
        </div>
    </div>

    <div id="task2-transfer-progress" class="progress-container" style="display: none;">
         <h3>משימה 2: למידת העברה</h3>
         <div class="progress-label">מנצל ידע קיים...</div>
         <div class="progress-bar-container"><div id="task2-transfer-progress-bar" class="progress-bar"></div></div>
         <div class="progress-details">
             <span>אפוכים: <span id="task2-transfer-epochs">0</span> / <span id="task2-transfer-total-epochs"></span></span>
             <span>דיוק נוכחי: <span id="task2-transfer-accuracy">0.0%</span></span>
         </div>
    </div>

    <div id="task2-results" class="step-container results-comparison" style="display: none;">
        <h3>&#x1F3C1; סיימנו! השוואת ביצועים:</h3>
        <div class="comparison-grid">
             <div id="task2-scratch-final" class="comparison-pane" style="display: none;">
                 <h4>אימון מאפס</h4>
                 <p>&#x23F1; זמן אימון: <span id="task2-scratch-completed-epochs"></span> אפוכים</p>
                 <p>&#x1F4C8; דיוק סופי: <span id="task2-scratch-final-accuracy"></span>%</p>
            </div>
             <div id="task2-transfer-final" class="comparison-pane" style="display: none;">
                 <h4>למידת העברה</h4>
                 <p>&#x23F1; זמן אימון: <span id="task2-transfer-completed-epochs"></span> אפוכים</p>
                 <p>&#x1F4C8; דיוק סופי: <span id="task2-transfer-final-accuracy"></span>%</p>
             </div>
         </div>
         <p class="insight-text"><strong>&#x1F4A1; תובנה:</strong> שימו לב להבדל המרשים בזמן האימון (מספר האפוכים) ולעיתים גם בדיוק הסופי. למידת העברה מקצרת דרך ומאיצה את הלמידה!</p>
    </div>

</div>

<button id="toggle-explanation" class="action-button secondary">הצג הסבר מורחב</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר מורחב: למידת העברה (Transfer Learning)</h2>

    <h3>מהי למידת העברה?</h3>
    <p>למידת העברה היא טכניקה מהפכנית בלמידת מכונה, המאפשרת למודל AI לרתום ידע שצבר במשימה אחת כדי להצטיין מהר יותר במשימה אחרת, קשורה. במקום להתחיל "ריק", המודל מתחיל מנקודת זינוק מתקדמת, ומכוונן את עצמו למשימה החדשה. זה כמו ללמוד לנהוג באופנוע אחרי שכבר למדתם לרכוב על אופניים – חלק מהמיומנויות הבסיסיות כבר קיימות!</p>

    <h3>השוואה ללמידה מאפס (Training from Scratch)</h3>
    <p>כשאנחנו מאמנים מודל מאפס, כל הפרמטרים שלו מתחילים מערכים אקראיים. המודל חייב ללמוד הכל בעצמו, מהיסוד. בלמידת העברה, אנו משתמשים במודל שכבר "ראה" הרבה נתונים ולמד לזהות תבניות ותכונות חשובות (למשל, קווים, קצוות, מרקמים בתמונות). הידע הזה משמש כבסיס חזק.</p>

    <h3>למה למידת העברה היא סופר יעילה?</h3>
    <ul>
        <li><strong>סילון לזמן האימון:</strong> המודל מתכנס לביצועים טובים הרבה יותר מהר כי הוא לא צריך ללמוד הכל מאפס. זה חוסך שעות, ימים או אפילו שבועות של חישוב.</li>
        <li><strong>צריכת נתונים נמוכה יותר:</strong> למשימות רבות אין מספיק נתונים זמינים לאימון מודל גדול מאפס. למידת העברה מאפשרת להשיג ביצועים מעולים גם עם מערך נתונים קטן יחסית למשימה החדשה, כי המודל כבר מבין את "העולם" הבסיסי.</li>
        <li><strong>שיפור בביצועים:</strong> לעיתים קרובות, במיוחד עם נתונים מוגבלים, מודל שעבר למידת העברה ישיג דיוק גבוה יותר ממודל שאומן מאפס.</li>
    </ul>

    <h3>איך זה מיושם ברשתות נוירונים עמוקות?</h3>
    <p>הקסם מתרחש בשכבות המודל. מודלים עמוקים (בעלי שכבות רבות) לומדים לזהות תכונות הולכות ומורכבות ככל שמתקדמים לעומק הרשת:</p>
    <ol>
        <li>השכבות הראשונות לומדות תכונות גנריות מאוד (קצוות, קווים, נקודות).</li>
        <li>שכבות אמצעיות לומדות שילובים של תכונות אלו ליצירת צורות פשוטות ואובייקטים חלקיים.</li>
        <li>השכבות האחרונות לומדות שילובים ספציפיים למשימה שעליה אומן המודל המקורי (למשל, זיהוי פנים מסוימות, או סוגי מכוניות).</li>
    </ol>
    <p>בלמידת העברה, אנו מנצלים את השכבות הקדומות (שכבר "מכירות" תכונות גנריות) ו"מקפיאים" אותן – מונעים ממשקולותיהן להשתנות. אנו מחליפים את השכבות האחרונות ומוסיפים חדשות שמותאמות למשימה החדשה, ומאמנים רק אותן (לצד שכבות אמצעיות שבחרנו לא להקפיא). תהליך זה נקרא Fine-tuning.</p>

    <h3>דוגמאות מהעולם האמיתי</h3>
    <ul>
        <li><strong>רפואה:</strong> מודל שאומן לזהות אלפי אובייקטים בתמונות רגילות יכול בקלות להיות מותאם לזהות גידולים קטנים בצילומי רנטגן, גם אם יש מעט צילומי רנטגן זמינים.</li>
        <li><strong>שפה:</strong> מודל ענק שאומן על כל האינטרנט להבין מבנה שפה יכול להשתמש בידע זה כדי לתרגם טקסט בתחום ספציפי או לסכם מסמכים משפטיים, עם הרבה פחות נתונים ספציפיים.</li>
    </ul>

    <h3>מתי להשתמש בלמידת העברה?</h3>
    <p>זוהי הגישה המועדפת לרוב כשיש לכם:</p>
    <ul>
        <li>משימה קשורה למשימה שעליה קיים מודל מאומן מראש.</li>
        <li>מערך נתונים קטן יחסית למשימה החדשה.</li>
        <li>צורך לחסוך זמן ומשאבי חישוב.</li>
    </ul>

    <h3>סיכום</h3>
    <p>למידת העברה היא כלי קסם בארגז הכלים של ה-AI, המאפשר לנו לבנות מודלים חזקים ויעילים במשימות חדשות על ידי רתימת הידע והעבודה הקשה שהושקעו באימון מודלים קודמים. היא לא רק מקצרת את הדרך, אלא גם פותחת אפשרויות חדשות לפיתוח AI בתחומים עם נתונים מוגבלים.</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-hover: #0056b3;
        --secondary-color: #6c757d;
        --secondary-hover: #5a6268;
        --success-color: #28a745;
        --background-light: #f8f9fa;
        --border-color: #e9ecef;
        --text-color: #343a40;
        --heading-color: #1a1a1a;
        --card-background: #ffffff;
        --card-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        --border-radius: 8px;
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Hebrew direction */
        text-align: right; /* Align text to the right */
        background-color: var(--background-light);
        color: var(--text-color);
    }

    h1, h2, h3, h4, h5 {
        color: var(--heading-color);
        margin-bottom: 1rem;
        text-align: right;
    }

    h1 { font-size: 2rem; }
    h2 { font-size: 1.75rem; }
    h3 { font-size: 1.5rem; }
    h4 { font-size: 1.25rem; }

    p {
        margin-bottom: 1rem;
    }

    .interactive-app, .explanation-section {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        padding: 30px;
        margin-bottom: 25px;
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
    }

    .step-container, .progress-container, .results-container {
        margin-bottom: 20px;
        padding: 20px;
        background-color: #e9ecef; /* Light grey background for steps */
        border-radius: var(--border-radius);
        border: 1px dashed var(--border-color);
    }

    .progress-container {
        background-color: #d4edda; /* Light green for active progress */
         border-color: #c3e6cb;
    }

     .results-container {
        background-color: #cce5ff; /* Light blue for results */
         border-color: #b8daff;
         font-size: 1.1rem;
    }
     .results-container h4 {
         color: var(--success-color);
         margin-top: 0;
     }

     .results-comparison .comparison-grid {
         display: grid;
         grid-template-columns: 1fr 1fr;
         gap: 20px;
         margin-top: 15px;
         margin-bottom: 15px;
     }

     .comparison-pane {
         background-color: var(--card-background);
         padding: 15px;
         border-radius: var(--border-radius);
         border: 1px solid var(--border-color);
     }
      .comparison-pane h4 {
          margin-bottom: 10px;
          color: var(--primary-color);
      }
       .comparison-pane p {
           margin-bottom: 5px;
           font-size: 1rem;
       }

    .action-button {
        display: inline-block;
        background-color: var(--primary-color);
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: var(--border-radius);
        cursor: pointer;
        margin-top: 15px;
        margin-left: 10px; /* Adjust margin for RTL */
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .action-button:hover {
        background-color: var(--primary-hover);
    }
     .action-button:active {
         transform: scale(0.98);
     }

    .action-button.secondary {
        background-color: var(--secondary-color);
    }
     .action-button.secondary:hover {
        background-color: var(--secondary-hover);
    }

    .choice-buttons {
        display: flex;
        gap: 15px;
        margin-top: 20px;
    }

    .progress-label {
        font-weight: bold;
        margin-bottom: 5px;
        color: var(--heading-color);
    }

    .progress-bar-container {
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 5px;
        margin: 10px 0;
        overflow: hidden; /* Ensure inner bar stays within bounds */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    .progress-bar {
        height: 25px;
        background-color: var(--success-color);
        width: 0%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        text-align: center;
        border-radius: 5px;
        transition: width 0.6s ease; /* Smooth animation */
        background-image: linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
        background-size: 40px 40px;
         animation: progress-animation 2s linear infinite; /* Add subtle movement */
    }

    @keyframes progress-animation {
      0% { background-position: 40px 0; }
      100% { background-position: 0 0; }
    }


     .progress-details {
         display: flex;
         justify-content: space-between;
         font-size: 0.9rem;
         color: var(--text-color);
     }

    .layer-options {
        margin-top: 15px;
        margin-bottom: 20px;
        padding: 15px;
        background-color: #f1f1f1;
        border-radius: var(--border-radius);
         border: 1px solid #ddd;
    }

     .checkbox-label {
         display: block; /* Each checkbox on a new line */
         margin-bottom: 10px;
         cursor: pointer;
     }
      .checkbox-label input[type="checkbox"] {
          margin-left: 8px; /* Space between checkbox and text */
           vertical-align: middle;
      }
       .checkbox-label span {
            vertical-align: middle;
       }

    .explanation-section {
        margin-top: 25px;
        border-top: 1px solid var(--border-color);
        padding-top: 25px;
    }
    .explanation-section h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: var(--primary-color);
    }
     .explanation-section ul, .explanation-section ol {
        padding-right: 25px; /* Indent lists for RTL */
        margin-bottom: 15px;
     }
     .explanation-section li {
        margin-bottom: 10px;
     }

     .insight-text {
         margin-top: 20px;
         padding: 15px;
         background-color: #fff3cd; /* Light yellow for insights */
         border: 1px solid #ffeeba;
         border-radius: var(--border-radius);
         color: #856404;
     }

     /* Animation for fading elements */
     .fade-in {
         opacity: 0;
         animation: fadeIn 0.5s ease-out forwards;
     }
      @keyframes fadeIn {
          to { opacity: 1; }
      }

      .slide-in {
          transform: translateY(20px);
          opacity: 0;
          animation: slideIn 0.6s ease-out forwards;
      }
       @keyframes slideIn {
           to {
               transform: translateY(0);
               opacity: 1;
           }
       }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const task1Section = document.getElementById('task1-section');
        const startTask1Button = document.getElementById('start-task1');
        const task1Progress = document.getElementById('task1-progress');
        const task1ProgressBar = document.getElementById('task1-progress-bar');
        const task1EpochsSpan = document.getElementById('task1-epochs');
        const task1TotalEpochsSpan = document.getElementById('task1-total-epochs');
        const task1AccuracySpan = document.getElementById('task1-accuracy');
        const task1Results = document.getElementById('task1-results');
        const task1CompletedEpochsSpan = document.getElementById('task1-completed-epochs');
        const task1FinalAccuracySpan = document.getElementById('task1-final-accuracy');
        const continueToTask2Button = document.getElementById('continue-to-task2');

        const task2Intro = document.getElementById('task2-intro');
        const chooseScratchButton = document.getElementById('choose-scratch');
        const chooseTransferButton = document.getElementById('choose-transfer');

        const task2Options = document.getElementById('task2-options');
        const startTask2TransferButton = document.getElementById('start-task2-transfer');

        const task2ScratchProgress = document.getElementById('task2-scratch-progress');
        const task2ScratchProgressBar = document.getElementById('task2-scratch-progress-bar');
        const task2ScratchEpochsSpan = document.getElementById('task2-scratch-epochs');
        const task2ScratchTotalEpochsSpan = document.getElementById('task2-scratch-total-epochs');
        const task2ScratchAccuracySpan = document.getElementById('task2-scratch-accuracy');

        const task2TransferProgress = document.getElementById('task2-transfer-progress');
        const task2TransferProgressBar = document.getElementById('task2-transfer-progress-bar');
        const task2TransferEpochsSpan = document.getElementById('task2-transfer-epochs');
        const task2TransferTotalEpochsSpan = document.getElementById('task2-transfer-total-epochs');
        const task2TransferAccuracySpan = document.getElementById('task2-transfer-accuracy');

        const task2Results = document.getElementById('task2-results');
        const task2ScratchFinalDiv = document.getElementById('task2-scratch-final');
        const task2ScratchCompletedEpochsSpan = document.getElementById('task2-scratch-completed-epochs');
        const task2ScratchFinalAccuracySpan = document.getElementById('task2-scratch-final-accuracy');

        const task2TransferFinalDiv = document.getElementById('task2-transfer-final');
        const task2TransferCompletedEpochsSpan = document.getElementById('task2-transfer-completed-epochs');
        const task2TransferFinalAccuracySpan = document.getElementById('task2-transfer-final-accuracy');


        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        // --- Simulation Parameters ---
        const TASK1_TOTAL_EPOCHS = 50;
        const TASK1_FINAL_ACCURACY = 95; // Simulated final accuracy

        const TASK2_SCRATCH_TOTAL_EPOCHS = 70; // Scratch needs significantly more epochs
        const TASK2_SCRATCH_FINAL_ACCURACY = 92; // Maybe slightly lower or similar

        const TASK2_TRANSFER_TOTAL_EPOCHS = 30; // Transfer needs significantly fewer epochs
        const TASK2_TRANSFER_FINAL_ACCURACY = 94; // Often achieves similar or slightly higher accuracy faster

        const SIMULATION_SPEED = 50; // Milliseconds per epoch (lower = faster simulation)

        // --- Helper Functions ---
        function showElement(element) {
            element.style.display = 'block';
             element.classList.remove('fade-in'); // Reset animation if needed
             element.classList.remove('slide-in');
             void element.offsetWidth; // Trigger reflow for animation
             element.classList.add('slide-in'); // Apply entry animation
        }

         function hideElement(element) {
             element.style.display = 'none';
              element.classList.remove('slide-in');
         }


        function simulateTraining(epochsSpan, totalEpochsSpan, accuracySpan, progressBar, totalEpochs, finalAccuracy, onComplete) {
            let currentEpoch = 0;
            epochsSpan.textContent = currentEpoch;
            totalEpochsSpan.textContent = totalEpochs;
            accuracySpan.textContent = (0).toFixed(1);
            progressBar.style.width = '0%';
            progressBar.textContent = ''; // Clear text initially

            const interval = setInterval(() => {
                currentEpoch++;
                const progress = (currentEpoch / totalEpochs); // Use ratio for calculation
                const percentage = progress * 100;

                 // Simulate a slightly different accuracy curve for transfer vs scratch
                 let accuracy;
                 if (progressBar.id === 'task2-transfer-progress-bar') {
                     // Transfer Learning: Faster initial gain, maybe plateaus higher/sooner
                     accuracy = (finalAccuracy * (1 - Math.exp(-progress * 4))).toFixed(1); // Exponential rise
                 } else {
                     // Scratch Training: Slower initial gain, more linear
                     accuracy = (finalAccuracy * progress * (0.8 + Math.random() * 0.4)).toFixed(1); // More linear with noise
                 }


                epochsSpan.textContent = currentEpoch;
                accuracySpan.textContent = Math.min(parseFloat(accuracy), finalAccuracy).toFixed(1); // Ensure accuracy doesn't exceed final
                progressBar.style.width = percentage + '%';
                 progressBar.textContent = `${Math.round(percentage)}%`;


                if (currentEpoch >= totalEpochs) {
                    clearInterval(interval);
                    accuracySpan.textContent = finalAccuracy.toFixed(1); // Ensure final accuracy is exact
                    progressBar.style.width = '100%';
                     progressBar.textContent = '100%';
                    onComplete(totalEpochs, finalAccuracy);
                }
            }, SIMULATION_SPEED); // Simulate speed
        }

        function resetProgressBars() {
             task1ProgressBar.style.width = '0%';
             task2ScratchProgressBar.style.width = '0%';
             task2TransferProgressBar.style.width = '0%';
              task1ProgressBar.textContent = '';
              task2ScratchProgressBar.textContent = '';
              task2TransferProgressBar.textContent = '';
        }


        // --- Task 1 Logic ---
        startTask1Button.addEventListener('click', () => {
            hideElement(startTask1Button);
            showElement(task1Progress);
            resetProgressBars();

            simulateTraining(
                task1EpochsSpan,
                task1TotalEpochsSpan,
                task1AccuracySpan,
                task1ProgressBar,
                TASK1_TOTAL_EPOCHS,
                TASK1_FINAL_ACCURACY,
                (completedEpochs, finalAccuracy) => {
                    hideElement(task1Progress);
                    showElement(task1Results);
                    task1CompletedEpochsSpan.textContent = completedEpochs;
                    task1FinalAccuracySpan.textContent = finalAccuracy.toFixed(1);
                }
            );
        });

        continueToTask2Button.addEventListener('click', () => {
            hideElement(task1Section);
            showElement(task2Intro);
             resetProgressBars();
             // Hide previous results if displayed
             hideElement(task2ScratchFinalDiv);
             hideElement(task2TransferFinalDiv);
             hideElement(task2Results);
        });


        // --- Task 2 Choice ---
        chooseScratchButton.addEventListener('click', () => {
             hideElement(task2Intro);
             showElement(task2ScratchProgress);
             resetProgressBars();

             simulateTraining(
                 task2ScratchEpochsSpan,
                 task2ScratchTotalEpochsSpan,
                 task2ScratchAccuracySpan,
                 task2ScratchProgressBar,
                 TASK2_SCRATCH_TOTAL_EPOCHS,
                 TASK2_SCRATCH_FINAL_ACCURACY,
                 (completedEpochs, finalAccuracy) => {
                     hideElement(task2ScratchProgress);
                     showElement(task2Results);
                     showElement(task2ScratchFinalDiv); // Show Scratch results pane
                 }
             );
        });

        chooseTransferButton.addEventListener('click', () => {
            hideElement(task2Intro);
            showElement(task2Options);
        });

        startTask2TransferButton.addEventListener('click', () => {
             hideElement(task2Options);
             showElement(task2TransferProgress);
             resetProgressBars();

             // In a real app, layer selection would influence training dynamics.
             // Here, we just use the pre-defined parameters for the Transfer Learning simulation.
             simulateTraining(
                 task2TransferEpochsSpan,
                 task2TransferTotalEpochsSpan,
                 task2TransferAccuracySpan,
                 task2TransferProgressBar,
                 TASK2_TRANSFER_TOTAL_EPOCHS,
                 TASK2_TRANSFER_FINAL_ACCURACY,
                 (completedEpochs, finalAccuracy) => {
                     hideElement(task2TransferProgress);
                     showElement(task2Results);
                      showElement(task2TransferFinalDiv); // Show Transfer results pane
                 }
             );
        });


        // --- Explanation Toggle Logic ---
        toggleExplanationButton.addEventListener('click', () => {
            if (explanationDiv.style.display === 'none') {
                showElement(explanationDiv);
                toggleExplanationButton.textContent = 'הסתר הסבר מורחב';
            } else {
                hideElement(explanationDiv);
                toggleExplanationButton.textContent = 'הצג הסבר מורחב';
            }
        });
    });
</script>