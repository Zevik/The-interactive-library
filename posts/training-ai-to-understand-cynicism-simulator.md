---
title: "לאמן בינה מלאכותית להבין ציניות: סימולטור האימון"
english_slug: training-ai-to-understand-cynicism-simulator
category: "טכנולוגיה / בינה מלאכותית"
tags: עיבוד שפה טבעית, למידת מכונה, סרקזם, אירוניה, מדעי הנתונים, אינטראקטיבי
---
# לאמן בינה מלאכותית להבין ציניות: סימולטור האימון

האם עצרתם פעם לחשוב כמה מסובך זה עבור רובוט להבין שכשמשהו נכשל כישלון חרוץ, המשפט 'איזו הצלחה מסחררת!' הוא לא באמת שבח, אלא ביקורת נוקבת? בינה מלאכותית (AI) שולטת בהבנת משמעות מילולית וישירה, אך שפה מורכבת ועשירה בניואנסים כמו סרקזם ואירוניה – שבהם לעיתים קרובות יש פער ואף סתירה בין הנאמר למשמעות האמיתית – מציבה בפניה אתגר עצום. איך גורמים למכונה לעקוף את המלכודות הלשוניות המתוחכמות האלה?

צאו למסע מרתק והפכו למאמני AI! בסימולטור זה, אתם תספקו את ה"דאטה" החיוני לאימון מודל פשוט לזיהוי ציניות. ראו כיצד המודל לומד (או מתקשה ללמוד) מתוך הסיווגים שלכם, וגלו את האתגרים העומדים בפני AI בניסיון להבין את השפה האנושית על כל מורכבותה.

<div id="ai-trainer-app" class="trainer-app">
    <h2 class="app-title">משימת אימון: סווגו את המשפטים עבור ה-AI</h2>
    <p class="app-intro">כ'מאמן AI' המנוסה שלנו, סווגו במדויק את המשפטים הבאים. כל סיווג שלכם הוא נקודת אימון חשובה למודל. לאחר מספר דוגמאות שתסווגו, ה-AI יתחיל לנסות לחזות בעצמו, ותוכלו לראות עד כמה הוא הצליח ללמוד מכם!</p>

    <div id="example-area" class="example-container">
        <p id="example-text" class="example-text">טוען משימה...</p>
        <div id="ai-prediction-feedback" class="prediction-feedback">
             <!-- AI prediction result will appear here -->
        </div>
    </div>

    <div id="classification-buttons" class="button-group">
        <button id="classify-sarcastic" class="classify-button sarcastic-button">סרקזם / אירוניה</button>
        <button id="classify-not-sarcastic" class="classify-button not-sarcastic-button">לא סרקזם / אירוניה</button>
    </div>

    <div id="stats" class="stats-area">
        <div class="stat-item">
            <span>סיווגים שסיפקתם:</span> <span id="user-count" class="stat-value">0</span>
        </div>
        <div id="ai-stats-container" class="stat-item ai-stats">
             <span>הצלחת ה-AI בחיזוי:</span> <span id="ai-accuracy" class="stat-value">0%</span> (<span id="ai-predictions-count" class="stat-value">0</span> חיזויים)
        </div>
         <div id="ai-training-status" class="training-status">
             ה-AI מתאמן על הנתונים שלך...
         </div>
    </div>

     <div id="end-message" class="end-message">
        <p>משימת האימון הושלמה! סיפקתם דאטה יקר ערך למודל ה-AI. כעת עברו לחלק ההסבר המלא כדי ללמוד איך AI באמת לומד לזהות ציניות.</p>
        <button id="show-explanation-button" class="explanation-toggle-button">הצג הסבר מלא</button>
     </div>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --primary-dark: #0056b3;
        --sarcastic-color: #ff6b6b; /* Red */
        --sarcastic-dark: #ee5253;
        --not-sarcastic-color: #1dd1a1; /* Green */
        --not-sarcastic-dark: #10ac84;
        --background-color: #f4f7f6;
        --card-background: #ffffff;
        --border-color: #e0e0e0;
        --text-color: #333;
        --secondary-text-color: #555;
        --shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        --border-radius: 12px;
    }

    .trainer-app {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 700px;
        margin: 30px auto;
        padding: 25px;
        border-radius: var(--border-radius);
        background-color: var(--card-background);
        box-shadow: var(--shadow);
        text-align: right;
        direction: rtl;
        color: var(--text-color);
        overflow: hidden; /* For animations */
    }

    .app-title {
        text-align: center;
        color: var(--primary-dark);
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.8em;
    }

    .app-intro {
        text-align: center;
        margin-bottom: 25px;
        color: var(--secondary-text-color);
        line-height: 1.6;
    }

    .example-container {
        min-height: 90px;
        margin-bottom: 20px;
        padding: 20px;
        border: 1px solid var(--border-color);
        background-color: var(--background-color);
        border-radius: 8px;
        text-align: center;
        font-size: 1.3em;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: relative; /* For absolute positioning of feedback */
        transition: opacity 0.5s ease-in-out; /* Fade animation */
    }

    .example-text {
         margin: 0;
         color: var(--text-color);
         opacity: 1; /* Initial state for fade */
         transition: opacity 0.5s ease-in-out;
    }

    .prediction-feedback {
        position: absolute;
        bottom: 5px; /* Position at the bottom */
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.9em;
        font-weight: bold;
        padding: 4px 8px;
        border-radius: 4px;
        opacity: 0; /* Hidden initially */
        transition: opacity 0.5s ease-in-out, background-color 0.3s ease;
    }

    .prediction-feedback.correct {
        background-color: rgba(29, 209, 161, 0.2); /* Light green */
        color: var(--not-sarcastic-dark);
    }

    .prediction-feedback.incorrect {
        background-color: rgba(255, 107, 107, 0.2); /* Light red */
        color: var(--sarcastic-dark);
    }


    .button-group {
        text-align: center;
        margin-bottom: 25px;
    }

    .classify-button {
        padding: 12px 25px;
        margin: 5px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        color: white;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .classify-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

     .classify-button:active {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        opacity: 0.9;
     }


    .sarcastic-button {
        background-color: var(--sarcastic-color);
    }

    .sarcastic-button:hover {
        background-color: var(--sarcastic-dark);
    }

    .not-sarcastic-button {
        background-color: var(--not-sarcastic-color);
    }

    .not-sarcastic-button:hover {
        background-color: var(--not-sarcastic-dark);
    }

    .stats-area {
        text-align: center;
        font-size: 1em;
        color: var(--secondary-text-color);
        display: flex;
        justify-content: center;
        gap: 20px; /* Space between stats */
        flex-wrap: wrap; /* Allow wrapping on small screens */
        margin-bottom: 25px;
    }

    .stat-item {
        padding: 8px 15px;
        background-color: var(--background-color);
        border-radius: 20px; /* Pill shape for stats */
        display: flex;
        align-items: center;
    }

    .stat-value {
        font-weight: bold;
        color: var(--text-color);
        margin-right: 5px; /* Space between label and value */
        min-width: 20px; /* Prevent layout shift */
        text-align: left;
        transition: color 0.3s ease;
    }

    .ai-stats {
         opacity: 0; /* Hidden initially */
         transform: translateY(10px);
         transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
    }

    .ai-stats.visible {
        opacity: 1;
        transform: translateY(0);
    }

     .training-status {
         position: absolute;
         bottom: 10px;
         left: 50%;
         transform: translateX(-50%);
         font-size: 0.9em;
         color: var(--secondary-text-color);
         opacity: 1;
         transition: opacity 0.5s ease-in-out;
     }

    .end-message {
        text-align: center;
        font-weight: bold;
        color: var(--primary-dark);
        margin-top: 20px;
        opacity: 0; /* Hidden initially */
        transform: translateY(20px);
        transition: opacity 0.8s ease-in-out, transform 0.8s ease-in-out;
        line-height: 1.6;
    }

    .end-message.visible {
         opacity: 1;
         transform: translateY(0);
    }

    .explanation-toggle-button {
        display: block;
        width: fit-content;
        margin: 20px auto 0;
        padding: 10px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape */
        background-color: var(--primary-color);
        color: white;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .explanation-toggle-button:hover {
        background-color: var(--primary-dark);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    .explanation-toggle-button:active {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        opacity: 0.9;
    }


    #explanation {
        margin-top: 40px;
        padding-top: 30px;
        border-top: 1px solid var(--border-color);
        color: var(--text-color);
        display: none; /* Hidden by default */
        opacity: 0; /* For animation */
        transition: opacity 0.8s ease-in-out;
    }

     #explanation.visible {
        opacity: 1;
     }

    #explanation h2 {
        color: var(--primary-dark);
        margin-bottom: 20px;
        text-align: center;
    }

    #explanation h3 {
        color: var(--primary-color);
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.4em;
    }

    #explanation p, #explanation li {
        line-height: 1.7;
        margin-bottom: 15px;
        color: var(--secondary-text-color);
    }

    #explanation ul {
        padding-right: 20px; /* For RTL list bullets */
    }

     #explanation li {
         margin-bottom: 8px;
     }


</style>

<!-- Note: The explanation div is placed *after* the main app div in the HTML, matching the 'Experience before Explanation' structure, but is controlled by JS to be shown/hidden -->
<div id="explanation">
    <h2>הסבר מעמיק: פענוח מורכבות השפה האנושית על ידי AI</h2>

    <h3>סרקזם ואירוניה: אמנות הפער הלשוני</h3>
    <p>בבסיסם, סרקזם ואירוניה הם ביטויים שבהם המשמעות המועברת שונה באופן משמעותי, ולרוב הפוך, מהמשמעות המילולית של המילים עצמן. סרקזם נוטה להיות ישיר יותר באופיו העוקצני ומטרתו לרוב לבקר או ללעוג, בעוד שאירוניה רחבה יותר וכוללת גם פערים בין המצופה למציאות (אירוניה מצבית) או בין הנאמר למחשבה הפנימית (אירוניה דרמטית). הקסם והקושי טמונים בפער הזה.</p>

    <h3>החידה למחשבים: מעבר למשמעות המילולית</h3>
    <p>האתגר הגדול ביותר עבור AI נובע מכך שמודלים רבים של עיבוד שפה טבעית (NLP) מאומנים על הבנת משמעות מילולית וישירה. סרקזם ואירוניה דורשים הבנה עמוקה יותר:
        <ul>
            <li>**הקשר:** המשמעות תלויה בסיטואציה, בזהות הדוברים, בידע עולם משותף.</li>
            <li>**טון וסגנון:** אצל בני אדם, טון הדיבור והבעות פנים חיוניים. בטקסט, סימנים כמו שימוש מוגזם בסימני פיסוק, כפילות לשונית, או סתירה פנימית במשפט יכולים לרמז על ציניות.</li>
            <li>**ידע עולם:** הבנה שמשפט כמו "איזה מזל שהאוטובוס איחר בשעתיים" נאמר בציניות תלויה בידע כללי שאיחורים הם דבר רע.</li>
        </ul>
        מודלים פשוטים מתקשים ללכוד את הניואנסים והתלות הללו בהקשר שאינו מילולי בלבד.
    </p>

    <h3>אימון ה-AI: המפתח הוא דאטה מסומן (Labeled Data)</h3>
    <p>כדי שמודל AI ילמד לזהות דפוסים מורכבים כמו ציניות, הוא זקוק למאגר עצום של דוגמאות מסווגות. בתהליך שנקרא למידה מפוקחת (Supervised Learning), אנו מזינים למודל טקסטים רבים שסווגו מראש על ידי בני אדם (למשל, אלפי ציוצים מטוויטר שסומנו כ'סרקסטי' או 'לא סרקסטי'). המודל בוחן את הדוגמאות הללו ולומד לזהות מאפיינים סטטיסטיים ולשוניים הקשורים לכל קטגוריה – אילו מילים נוטות להופיע במשפטים סרקסטיים? האם יש מבנה תחבירי מסוים? האם יש שימוש נפוץ בסימני קריאה או מילות הגברה? עם מספיק דוגמאות, המודל בונה לעצמו "מודל פנימי" שמאפשר לו לנסות ולחזות את הסיווג הנכון עבור טקסטים חדשים שלא ראה.</p>

    <h3>החשיבות הקריטית שלכם כ"מאמני AI"</h3>
    <p>כפי שראיתם בסימולטור, הביצועים של ה-AI תלויים ישירות בכמות ובאיכות הנתונים המסומנים שהוא מקבל. דאטה מסומן הוא כמו חומרי הגלם לאימון. ככל שחומרי הגלם הללו מגוונים, מייצגים נכון את המציאות, ומסומנים במדויק, כך המודל הסופי יהיה מדויק יותר. ללא דאטה מסומן, אין ל-AI דרך ללמוד את ההבדלים הדקים והמורכבים בין סרקזם לדיבור ישיר.</p>

    <h3>אתגרים נוספים ופתרונות מתקדמים</h3>
    <p>מלבד האתגר הבסיסי, קיימים קשיים נוספים:
        <ul>
            <li>**הטיית נתונים:** אם נתוני האימון אינם מגוונים מספיק, המודל עשוי לזהות ציניות רק בהקשרים ספציפיים.</li>
            <li>**עמימות:** אפילו בני אדם לא תמיד מסכימים לגבי זיהוי ציניות, במיוחד ללא הקשר מלא. חוסר העקביות הזה בנתוני האימון מקשה על הלמידה.</li>
            <li>**שפות ותרבויות:** לכל שפה ותרבות מאפיינים ציניות ייחודיים הדורשים אימון ספציפי.</li>
        </ul>
        חוקרים בתחום NLP מפתחים שיטות מתקדמות יותר, כמו שימוש ברשתות נוירונים עמוקות (Deep Learning) שמסוגלות ללכוד קשרים סמנטיים ותחביריים מורכבים יותר בטקסט, ולשלב מידע מהקשר רחב יותר (משפטים קודמים, מידע על הדובר אם זמין). מודלים כמו Transformer (שעומדים בבסיס GPT) מצטיינים בלכידת הקשרים עדינים אלו.
    </p>

    <h3>סיכום: מסע בלתי פוסק להבנת השפה</h3>
    <p>אימון AI להבנת ציניות ואירוניה הוא דוגמה קלאסית לאתגרים שעיבוד שפה טבעית מודרני מתמודד איתם. הוא מדגיש את הצורך בדאטה איכותי, את המורכבות הטבועה בשפה האנושית, ואת הפערים שעדיין קיימים בין יכולות המכונה להבנה האנושית האינטואיטיבית. המחקר בתחום ממשיך, וכל שיפור ביכולת הזיהוי פותח דלתות ליישומים רבים, משיפור צ'אטבוטים ועד ניתוח סנטימנט חברתי מדויק יותר.</p>
</div>

<script>
    const exampleTextElement = document.getElementById('example-text');
    const classifySarcasticButton = document.getElementById('classify-sarcastic');
    const classifyNotSarcasticButton = document.getElementById('classify-not-sarcastic');
    const userCountElement = document.getElementById('user-count');
    const aiStatsContainer = document.getElementById('ai-stats-container');
    const aiAccuracyElement = document.getElementById('ai-accuracy');
    const aiPredictionsCountElement = document.getElementById('ai-predictions-count');
    const aiPredictionFeedbackElement = document.getElementById('ai-prediction-feedback'); // Use the new feedback div
    const showExplanationButton = document.getElementById('show-explanation-button'); // Use the new ID
    const explanationDiv = document.getElementById('explanation');
    const endMessageElement = document.getElementById('end-message');
    const classificationButtonsDiv = document.getElementById('classification-buttons');
     const trainingStatusElement = document.getElementById('ai-training-status');

    const examples = [
        { text: "איזה יום נפלא, הגשם לא הפסיק לרדת.", label: 'sarcastic' },
        { text: "האוכל במסעדה הזאת היה פשוט מדהים, חזרתי לשם שוב.", label: 'not-sarcastic' },
        { text: "כן בטח, כאילו שזה באמת יקרה.", label: 'sarcastic' },
        { text: "קניתי מצרכים בסופר.", label: 'not-sarcastic' },
        { text: "אני כל כך מתרגש מהעבודה הזאת שאני בקושי מצליח לקום בבוקר.", label: 'sarcastic' },
        { text: "השמש זרחה היום.", label: 'not-sarcastic' },
        { text: "ברור שאתה צודק, כמו תמיד.", label: 'sarcastic' },
        { text: "השלמתי את המשימות להיום.", label: 'not-sarcastic' },
        { text: "זה ממש קל, רק לוקח לי שעות.", label: 'sarcastic' },
        { text: "נסעתי ברכבת התחתית הבוקר.", label: 'not-sarcastic' },
        { text: "אה, עכשיו הכל ברור לגמרי, תודה על ההסבר הבהיר כל כך.", label: 'sarcastic' },
        { text: "הצמח בגינה גדל יפה.", label: 'not-sarcastic' }
        // Add more examples for better training simulation (optional but good practice)
    ];

    let currentExampleIndex = 0;
    let userClassifications = []; // Stores { text, label } for user's classifications (AI trains on this)
    let aiPredictions = []; // Stores { text, prediction, actualLabel, isCorrect } for AI's predictions
    const trainingThreshold = 3; // AI starts predicting after user classifies this many examples (Lowered slightly for faster demo)
    let aiTrained = false;

    function displayExample() {
         // Fade out current example and feedback
         exampleTextElement.style.opacity = 0;
         aiPredictionFeedbackElement.style.opacity = 0;
         trainingStatusElement.style.opacity = 1; // Show 'training...' status

         setTimeout(() => { // Wait for fade-out
            if (currentExampleIndex < examples.length) {
                exampleTextElement.textContent = examples[currentExampleIndex].text;
                classificationButtonsDiv.style.visibility = 'visible';
                endMessageElement.classList.remove('visible'); // Ensure end message is hidden
                 trainingStatusElement.style.opacity = 0; // Hide training status once example is loaded

                // Fade in new example
                exampleTextElement.style.opacity = 1;

            } else {
                // End of examples
                exampleTextElement.textContent = "אין יותר דוגמאות לסיווג.";
                classificationButtonsDiv.style.visibility = 'hidden';
                 trainingStatusElement.style.opacity = 0;
                endMessageElement.classList.add('visible'); // Show end message
                 // Show explanation button if it's hidden
                 if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
                     showExplanationButton.style.display = 'block';
                 } else {
                     showExplanationButton.style.display = 'none'; // Hide if explanation is already shown
                 }

            }
         }, 500); // Match CSS transition duration
    }

    function updateStats() {
        userCountElement.textContent = userClassifications.length;

        if (aiTrained) {
            aiStatsContainer.classList.add('visible'); // Animate stats visibility
            const correctAIPredictions = aiPredictions.filter(p => p.isCorrect).length;
            const totalAIPredictions = aiPredictions.length;
            if (totalAIPredictions > 0) {
                 const accuracy = ((correctAIPredictions / totalAIPredictions) * 100).toFixed(0);
                 aiAccuracyElement.textContent = `${accuracy}%`;
                 aiPredictionsCountElement.textContent = totalAIPredictions;
                 // Optional: Change color based on accuracy
                 aiAccuracyElement.style.color = accuracy >= 80 ? var_not_sarcastic_dark : (accuracy >= 50 ? var_primary_dark : var_sarcastic_dark);

            } else {
                 aiAccuracyElement.textContent = `0%`;
                 aiPredictionsCountElement.textContent = 0;
                 aiAccuracyElement.style.color = var_secondary_text_color;
            }
        }
    }

    function simulateAITrainingAndPrediction(userClassifiedLabel) {
         // AI simulation happens *after* the user classifies the current example.
         // The AI *predicts* on the example the user just saw, using the data *including* the user's latest classification.
         if (userClassifications.length >= trainingThreshold) {
             if (!aiTrained) {
                 aiTrained = true;
                 aiStatsContainer.classList.add('visible'); // Make stats visible with animation
             }

             // Simple AI logic: Predict the majority class from the data the user has provided so far.
             // This is a simplified simulation of training on labeled data.
             const sarcasticCount = userClassifications.filter(c => c.label === 'sarcastic').length;
             const notSarcasticCount = userClassifications.filter(c => c.label === 'not-sarcastic').length;

             let aiPredictedLabel;
             if (sarcasticCount > notSarcasticCount) {
                 aiPredictedLabel = 'sarcastic';
             } else if (notSarcasticCount > sarcasticCount) {
                 aiPredictedLabel = 'not-sarcastic';
             } else {
                 // 50/50 split or no dominant data, default to 'not-sarcastic' (can be randomized too)
                 aiPredictedLabel = 'not-sarcastic';
             }

             // Evaluate the AI's prediction against the *true* label of the example the user just saw.
             const currentExampleData = examples[currentExampleIndex - 1]; // The example user just finished classifying
             const actualLabel = currentExampleData.label;
             const isCorrect = (aiPredictedLabel === actualLabel);

             aiPredictions.push({
                 text: currentExampleData.text,
                 prediction: aiPredictedLabel,
                 actualLabel: actualLabel,
                 isCorrect: isCorrect
             });

             // Display the result of the AI's prediction for the JUST CLASSIFIED example
             const outcomeText = isCorrect ? 'נכון! 😊' : 'טעות 😟';
             const predictionText = aiPredictedLabel === 'sarcastic' ? 'סרקזם / אירוניה' : 'לא סרקזם / אירוניה';

             aiPredictionFeedbackElement.textContent = `ה-AI חזה: ${predictionText} (${outcomeText})`;
             aiPredictionFeedbackElement.className = 'prediction-feedback'; // Reset classes
             aiPredictionFeedbackElement.classList.add(isCorrect ? 'correct' : 'incorrect');

              // Trigger fade-in animation for feedback
             requestAnimationFrame(() => {
                aiPredictionFeedbackElement.style.opacity = 1;
             });
         }
    }


    function handleClassification(label) {
        if (currentExampleIndex < examples.length) {
            const currentExampleData = examples[currentExampleIndex];

            // Record user classification *before* simulating AI and moving to next example
            userClassifications.push({
                text: currentExampleData.text,
                label: label
            });

            currentExampleIndex++; // Move to the next example index immediately

            // Simulate AI training and prediction based on the *data up to this point* for the *just classified* example
            simulateAITrainingAndPrediction(label);

            // Update stats
            updateStats();

            // Display the *next* example after a short delay to allow feedback to be seen
            setTimeout(displayExample, aiTrained ? 1500 : 500); // Delay more if AI feedback was shown
        }
    }


    classifySarcasticButton.addEventListener('click', () => handleClassification('sarcastic'));
    classifyNotSarcasticButton.addEventListener('click', () => handleClassification('not-sarcastic'));

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
         requestAnimationFrame(() => { // Trigger fade-in after display block
            explanationDiv.classList.toggle('visible', isHidden);
         });

        showExplanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג הסבר מלא';
        // Hide the button itself once explanation is shown (optional)
         if (!isHidden) {
              // showExplanationButton.style.display = 'none';
         }
    });

    // Initialize the first example when the page loads
    document.addEventListener('DOMContentLoaded', () => {
        updateStats(); // Initialize stats display (0 user, AI hidden)
        displayExample(); // Load the first example
        aiStatsContainer.classList.remove('visible'); // Ensure AI stats are hidden on load
         trainingStatusElement.style.opacity = 0; // Hide training status initially
         aiPredictionFeedbackElement.style.opacity = 0; // Hide feedback initially
    });

</script>
---