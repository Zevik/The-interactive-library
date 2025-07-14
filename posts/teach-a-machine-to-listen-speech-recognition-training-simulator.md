---
title: "לאמן את האוזן הדיגיטלית: סימולטור זיהוי דיבור"
english_slug: teach-a-machine-to-listen-speech-recognition-training-simulator
category: "טכנולוגיה / בינה מלאכותית"
tags: ["בינה מלאכותית", "למידת מכונה", "זיהוי דיבור", "אימון מודלים", "נתונים", "סימולטור"]
---
<h1>לאמן את האוזן הדיגיטלית: סימולטור זיהוי דיבור</h1>

<p>איך הטלפון, העוזרת הקולית או הרכב שלכם מבינים אתכם ככשאתם מדברים אליהם? זו לא קסם, זו בינה מלאכותית שעברה מסע אימון ארוך ומדויק. בסימולטור הזה, תהפכו למאמני AI ותראו בעצמכם איך בונים מודל שיודע להקשיב!</p>

<div id="app-container">
    <div id="training-section">
        <h2><i class="icon train-icon"></i> מעבדת אימון: תייגו את הקול!</h2>
        <p>כדי שהמודל שלנו ילמד להקשיב, הוא זקוק להרבה דוגמאות מתוייגות. כל דוגמה שתתייגו נכון תחזק את יכולותיו.</p>
        <div id="current-sample-card" class="card">
            <div id="sample-info">
                 <span id="sample-quality" class="quality-label"></span>
                 <span class="sample-action">
                    <span id="sample-audio-icon" class="audio-icon"></span>
                    <span id="sample-audio-placeholder">האזן לדוגמה</span>
                 </span>
            </div>
            <div class="prompt">
                 <strong>מה שמעת?</strong>
            </div>
             <input type="text" id="user-tag" autocomplete="off" placeholder="הקלד כאן את מה ששמעת...">
             <button id="submit-tag"><i class="icon check-icon"></i> שלח תיוג</button>
        </div>
        <p id="tagging-feedback" class="feedback"></p>
    </div>

    <div id="model-status" class="card">
        <h2><i class="icon status-icon"></i> דופק המודל</h2>
        <p>דוגמאות שאומנו עד כה: <span id="trained-samples-count">0</span></p>
        <p>דיוק משוער של המודל (מבוסס על האימון שלך): <span id="expected-accuracy">0%</span></p>
         <div class="progress-bar-container">
             <div id="accuracy-progress-bar" class="progress-bar"></div>
         </div>
    </div>

    <div id="testing-section" class="card">
        <h2><i class="icon test-icon"></i> מבחן ביצועים</h2>
        <p>מוכנים לבדוק את המודל שאמנתם? לאחר שתאמנו מספיק דוגמאות, נוכל לבחון איך הוא מתמודד עם נתונים חדשים שמעולם לא שמע!</p>
        <button id="run-test" disabled><i class="icon rocket-icon"></i> הרץ מבחן ביצועים (נדרשות לפחות 10 דוגמאות אימון)</button>
        <div id="test-results" class="test-results-card" style="display: none;">
            <h4><i class="icon results-icon"></i> תוצאות המבחן:</h4>
            <p>דוגמאות שזוהו נכון: <span id="correct-test-count">0</span> מתוך <span id="total-test-count">0</span></p>
            <p><strong>דיוק במבחן: <span id="test-accuracy">0%</span></strong></p>
            <div id="test-sample-list">
                <h5>פירוט הדוגמאות שנבדקו:</h5>
            </div>
        </div>
    </div>

    <button id="show-explanation-button" class="explanation-button"><i class="icon info-icon"></i> הצג הסבר: איך זיהוי דיבור עובד?</button>

    <div id="explanation" class="explanation-card" style="display: none;">
        <h2><i class="icon book-icon"></i> מאחורי הקלעים: איך מכונות לומדות להקשיב</h2>

        <h3>מה זה זיהוי דיבור אוטומטי (ASR)?</h3>
        <p>ASR (Automatic Speech Recognition) היא הטכנולוגיה המאפשרת למחשבים ולמכשירים דיגיטליים "להקשיב" לדיבור שלנו, להבין אותו ולהמיר אותו לטקסט. זהו שילוב מרתק של בלשנות, עיבוד קול ובינה מלאכותית מתקדמת.</p>

        <h3>איך מודלי AI 'לומדים' להקשיב?</h3>
        <p>מודלים אלו לומדים בעזרת אימון על כמויות ענק של הקלטות קול ותמלולים מדויקים שלהן. התהליך כולל זיהוי דפוסים עדינים באותות השמע וקישורם למילים וצלילי דיבור. ככל שהמודל נחשף ליותר דוגמאות מגוונות (עם מבטאים, רעשים, מהירויות שונות), כך הוא הופך "חכם" ומדויק יותר.</p>

        <h3>כוחם של הנתונים: איסוף, תיוג וניקוי</h3>
        <p>הנתונים הם ליבת האימון של כל מודל AI. במקרה של דיבור, אלו הקלטות אודיו מדויקות ותיוג טקסטואלי מושלם של מה שנאמר (בדיוק כמו שעשיתם בסימולטור!). עבודה זו, שלרוב נעשית ידנית, דורשת סבלנות ודיוק. גם ניקוי הנתונים מרעשים או שגיאות הוא קריטי לאיכות המודל הסופי.</p>

        <h3>ההבדל בין נתוני אימון לבדיקה</h3>
        <p>נתוני האימון הם ה"שיעורים" שהמודל לומד מהם. נתוני הבדיקה הם ה"מבחן" האמיתי – דוגמאות שהמודל <strong>אף פעם לא פגש קודם</strong>. הן משמשות כדי להעריך כמה טוב המודל מצליח ליישם את מה שלמד על מצבים חדשים ולא מוכרים. זה מודד את יכולת ההכללה (Generalization) שלו, שהיא סופר חשובה.</p>

        <h3>מדידת הצלחה: מה מסתתר מאחורי אחוזי הדיוק?</h3>
        <p>המדד הנפוץ ביותר הוא אחוז הדיוק (Accuracy) או אחוז שגיאות מילים (WER). אחוז הדיוק שראיתם בסימולטור מראה כמה דוגמאות מתוך המבחן המודל הצליח לתייג נכון. דיוק גבוה = מודל שמקשיב טוב יותר!</p>

        <h3>אתגרים בעולם האמיתי</h3>
        <p>אימון מודל זיהוי דיבור הוא משימה לא פשוטה. רעשי רקע בלתי צפויים, מבטאים שונים, אוצר מילים עצום שמשתנה, דיבור מהיר או איטי, איכות הקלטה ירודה – כל אלה מהווים אתגרים עצומים שמצריכים נתוני אימון מגוונים ביותר ואלגוריתמים חכמים במיוחד.</p>

        <h3>זיהוי דיבור מסביבנו</h3>
        <p>פגשתם אותו כבר היום: כשביקשתם מהטלפון לחייג, כשהכתבתם הודעה במקום להקליד, כשדיברתם עם הרכב, או כשקיבלתם תמלול אוטומטי של פגישה. זיהוי דיבור נמצא בכל מקום והופך את חיינו לנוחים ויעילים יותר.</p>

    </div>
</div>

<style>
    /* כל העיצוב כאן */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
        background-color: #e8f5e9; /* Light green background */
        color: #212121;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        min-height: 100vh;
    }

    #app-container {
        max-width: 800px;
        width: 100%;
        margin: 20px auto;
        padding: 30px;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        gap: 25px; /* Space between main sections */
    }

    h1 {
        color: #1b5e20; /* Dark green */
        text-align: center;
        margin-bottom: 25px;
        font-weight: 700;
        font-size: 2em;
    }

    h2, h3, h4, h5 {
        color: #388e3c; /* Medium green */
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
        font-weight: 500;
    }
     h2 .icon { font-size: 1.5em; }
     h3 .icon { font-size: 1.2em; }
     h4 .icon { font-size: 1em; }


    p {
        margin-bottom: 15px;
    }

    .card {
        background-color: #f1f8e9; /* Very light green */
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #dcedc8; /* Light border */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    #current-sample-card {
         background-color: #e8f5e9; /* Slightly darker than section background */
         border-color: #dcedc8;
         display: flex;
         flex-direction: column;
         gap: 15px;
         margin-bottom: 20px;
    }

    #sample-info {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
    }

    .quality-label {
        font-weight: 500;
        color: #689f38; /* Greenish */
        background-color: #dcedc8;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.9em;
    }

    .sample-action {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #0288d1; /* Blue */
        cursor: pointer;
        font-weight: 500;
        transition: color 0.2s ease;
    }
     .sample-action:hover {
         color: #01579b; /* Darker blue on hover */
         text-decoration: underline;
     }

    .audio-icon::before { content: '🔊'; } /* Speaker icon */
    .train-icon::before { content: '🎧'; } /* Headphones/training icon */
    .status-icon::before { content: '📊'; } /* Chart/status icon */
    .test-icon::before { content: '🔬'; } /* Microscope/test icon */
    .rocket-icon::before { content: '🚀'; } /* Rocket/run icon */
    .results-icon::before { content: '✅'; } /* Checkmark/results icon */
    .info-icon::before { content: '💡'; } /* Lightbulb/info icon */
    .book-icon::before { content: '📚'; } /* Books/explanation icon */
    .check-icon::before { content: '👍'; } /* Thumbs up for submit */
    .correct-icon::before { content: '✔️'; color: green; margin-left: 5px; }
    .incorrect-icon::before { content: '❌'; color: red; margin-left: 5px; }


    .prompt {
        font-size: 1.1em;
        color: #333;
    }

    input[type="text"] {
        padding: 12px 15px;
        border: 1px solid #bdbdbd; /* Gray border */
        border-radius: 6px;
        font-size: 1rem;
        width: calc(100% - 30px); /* Adjust width for padding */
        box-sizing: border-box; /* Include padding in width */
        margin-bottom: 10px; /* Space before button */
        transition: border-color 0.2s ease;
    }

    input[type="text"]:focus {
        border-color: #0288d1; /* Blue focus highlight */
        outline: none;
        box-shadow: 0 0 5px rgba(2, 136, 209, 0.2);
    }

    button {
        display: inline-flex; /* Allow icon next to text */
        align-items: center;
        gap: 8px;
        padding: 12px 25px;
        background-color: #4caf50; /* Green */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
        font-weight: 500;
        transition: background-color 0.3s ease, opacity 0.3s ease;
    }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
    }

    button:hover:not(:disabled) {
        background-color: #388e3c; /* Darker green */
    }

    #submit-tag {
         background-color: #0288d1; /* Blue for action */
    }
    #submit-tag:hover:not(:disabled) {
         background-color: #01579b; /* Darker blue */
    }


    .feedback {
        min-height: 1.2em;
        margin-top: 15px;
        font-weight: 500;
        font-size: 1.1em;
        opacity: 0; /* Start hidden */
        transform: translateY(10px); /* Start slightly lower */
        animation: fadeInFeedback 0.5s ease forwards; /* Animation */
    }

    .feedback.success { color: #2e7d32; } /* Dark green */
    .feedback.error { color: #d32f2f; } /* Red */
    .feedback.info { color: #f57c00; } /* Orange */

    @keyframes fadeInFeedback {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }


    .progress-bar-container {
        width: 100%;
        height: 15px;
        background-color: #e0e0e0; /* Light gray */
        border-radius: 8px;
        overflow: hidden; /* Hide overflow during animation */
        margin-top: 15px;
    }

    #accuracy-progress-bar {
        height: 100%;
        width: 0%; /* Initial width */
        background-color: #4caf50; /* Green */
        border-radius: 8px;
        transition: width 0.5s ease-in-out; /* Smooth animation */
    }

    #run-test {
        background-color: #ffb300; /* Amber */
        color: #333;
        margin-top: 15px;
         display: block; /* Make it a block button */
        width: 100%;
        text-align: center;
    }
    #run-test:hover:not(:disabled) {
         background-color: #ffa000; /* Darker amber */
    }

    .explanation-button {
        display: block;
        width: 100%;
        text-align: center;
        margin-top: 30px;
        background-color: #0288d1; /* Blue */
        font-size: 1.1rem;
    }
    .explanation-button:hover {
        background-color: #01579b; /* Darker blue */
    }

    .explanation-card {
        border-color: #c8e6c9; /* Lighter green border */
        background-color: #e8f5e9; /* Matches body background */
        color: #1b5e20; /* Dark green text */
        padding: 30px;
        box-shadow: none; /* No extra shadow */
    }
    .explanation-card h2, .explanation-card h3, .explanation-card h4 {
        color: #1b5e20; /* Dark green */
    }
     .explanation-card .icon { color: #1b5e20; } /* Dark green icons */


    .test-results-card {
        margin-top: 20px;
        padding: 20px;
        background-color: #ffffff; /* White background for results */
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    #test-sample-list {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px dashed #bdbdbd;
    }
    .sample-result {
        margin-bottom: 12px;
        padding-bottom: 12px;
        border-bottom: 1px dotted #eeeeee;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.95em;
    }
     .sample-result:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }
    .sample-result span {
        font-weight: 500;
    }
    .sample-result.correct span { color: #2e7d32; }
    .sample-result.incorrect span { color: #d32f2f; }

</style>

<script>
    // Sample data - added more variety and complexity potentials
    const allSamples = [
        { text: "שלום", quality: "ברור מאוד" },
        { text: "תודה רבה", quality: "ברור" },
        { text: "בבקשה", quality: "קצת רעש" },
        { text: "כן בטח", quality: "ברור" },
        { text: "לא יודע", quality: "המהום" },
        { text: "בוקר טוב", quality: "ברור מאוד" },
        { text: "ערב טוב לכם", quality: "קצת רעש" },
        { text: "לילה טוב", quality: "ברור" },
        { text: "מה נשמע היום", quality: "ברור" },
        { text: "הכל בסדר גמור", quality: "קצת רעש" },
        { text: "להתראות בקרוב", quality: "ברור מאוד" },
        { text: "שלום שלום", quality: "רעש חזק" }, // Example with strong noise
        { text: "תודה רבה לך", quality: "המהום חזק" }, // Example with strong mumbling
        { text: "בבקשה עזרה", quality: "ברור" },
        { text: "כן בטח שאפשר", quality: "רעש חזק" },
        { text: "לא תודה", quality: "המהום" },
        { text: "כוס מים", quality: "ברור מאוד" },
        { text: "אני רעב", quality: "ברור" },
        { text: "זקוק לעזרה", quality: "קצת רעש" },
        { text: "תודה רבה על הכל", quality: "ברור מאוד" },
        { text: "בסדר גמור תודה", quality: "רעש חזק" },
        { text: "להתראות מחר", quality: "המהום חזק" },
        { text: "שלום וברכה", quality: "ברור" },
        { text: "בבקשה באמת", quality: "קצת רעש" },
        { text: "מה נשמע אחי", quality: "המהום" },
        { text: "תודה רבה לכם", quality: "רעש חזק" },
         { text: "איך מגיעים", quality: "ברור" },
         { text: "באיזו שעה", quality: "קצת רעש" },
         { text: "זה פתוח", quality: "ברור מאוד" },
         { text: "סגור עכשיו", quality: "המהום" }
    ];

    let trainedSamples = [];
    let availableSamples = [...allSamples]; // Copy for simulation
    let currentSample = null;
    let minSamplesForTest = 10;
    let sampleLoadTimeout = null; // To manage delay before next sample

    const sampleQualityEl = document.getElementById('sample-quality');
    const userTagInput = document.getElementById('user-tag');
    const submitTagButton = document.getElementById('submit-tag');
    const taggingFeedbackEl = document.getElementById('tagging-feedback');
    const trainedSamplesCountEl = document.getElementById('trained-samples-count');
    const expectedAccuracyEl = document.getElementById('expected-accuracy');
    const accuracyProgressBar = document.getElementById('accuracy-progress-bar');
    const runTestButton = document.getElementById('run-test');
    const testResultsEl = document.getElementById('test-results');
    const correctTestCountEl = document.getElementById('correct-test-count');
    const totalTestCountEl = document.getElementById('total-test-count');
    const testAccuracyEl = document.getElementById('test-accuracy');
    const testSampleListEl = document.getElementById('test-sample-list');
    const showExplanationButton = document.getElementById('show-explanation-button');
    const explanationEl = document.getElementById('explanation');
    const sampleAudioPlaceholder = document.getElementById('sample-audio-placeholder');
    const sampleAudioIcon = document.getElementById('sample-audio-icon');


    // Simulate 'playing' audio - in a real app, this would play a sound file
    sampleAudioPlaceholder.addEventListener('click', () => {
        if (currentSample && !sampleAudioPlaceholder.classList.contains('playing')) {
            // Add a 'playing' class for potential styling/animation
            sampleAudioPlaceholder.classList.add('playing');
             sampleAudioIcon.classList.add('playing-icon'); // Optional: change icon

            taggingFeedbackEl.textContent = `(מדמה השמעת קול...)`;
            taggingFeedbackEl.className = 'feedback info';
             taggingFeedbackEl.style.opacity = 1;
             taggingFeedbackEl.style.transform = 'translateY(0)';


            // Simulate playback duration
            setTimeout(() => {
                 taggingFeedbackEl.textContent = ''; // Clear info text
                 taggingFeedbackEl.className = 'feedback'; // Reset class
                 taggingFeedbackEl.style.opacity = 0;
                 taggingFeedbackEl.style.transform = 'translateY(10px)';

                 sampleAudioPlaceholder.classList.remove('playing');
                 sampleAudioIcon.classList.remove('playing-icon');
                 userTagInput.focus(); // Return focus to input after 'playback'
            }, 1000); // Simulate 1 second playback
        }
    });


    function loadNextSample() {
         clearTimeout(sampleLoadTimeout); // Clear any pending loads

        if (availableSamples.length === 0) {
             // Attempt to replenish if some samples were skipped or failed tagging
             const successfullyTaggedTexts = new Set(trainedSamples.filter(s => s.isCorrect).map(s => s.originalText + s.quality));
             const potentiallyAvailable = allSamples.filter(s => !successfullyTaggedTexts.has(s.text + s.quality));

            if (potentiallyAvailable.length === 0) {
                taggingFeedbackEl.textContent = "מעולה! תייגת את כל הדוגמאות הזמינות. אין כרגע דוגמאות נוספות לאימון.";
                taggingFeedbackEl.className = 'feedback success';
                 taggingFeedbackEl.style.opacity = 1;
                 taggingFeedbackEl.style.transform = 'translateY(0)';
                userTagInput.disabled = true;
                submitTagButton.disabled = true;
                sampleAudioPlaceholder.style.pointerEvents = 'none'; // Disable clicking audio
                sampleAudioPlaceholder.style.opacity = 0.5;
                sampleAudioIcon.style.opacity = 0.5;
                return;
            } else {
                 // If there are potential samples, shuffle and make them available
                 availableSamples = [...potentiallyAvailable].sort(() => 0.5 - Math.random());
            }
        }

        // Select a random sample from available samples
        const randomIndex = Math.floor(Math.random() * availableSamples.length);
        currentSample = availableSamples.splice(randomIndex, 1)[0]; // Remove and get the sample

        sampleQualityEl.textContent = `[איכות: ${currentSample.quality}]`;
        userTagInput.value = '';
        taggingFeedbackEl.textContent = '';
        taggingFeedbackEl.className = 'feedback';
         taggingFeedbackEl.style.opacity = 0; // Hide feedback initially
         taggingFeedbackEl.style.transform = 'translateY(10px)';

        userTagInput.disabled = false;
        submitTagButton.disabled = false;
        sampleAudioPlaceholder.style.pointerEvents = 'auto'; // Enable clicking audio
        sampleAudioPlaceholder.style.opacity = 1;
        sampleAudioIcon.style.opacity = 1;


        // Auto-focus input but allow brief moment for user to click audio first
         // setTimeout(() => userTagInput.focus(), 200); // Debated... maybe better to require click? Let's keep focus on input after 'playback' sim.
    }

    function calculateExpectedAccuracy() {
        if (trainedSamples.length === 0) {
            accuracyProgressBar.style.width = '0%';
            return 0;
        }

        let effectiveScore = 0;
        let maxPossibleScore = trainedSamples.length * 5; // Base score per sample if perfect

        trainedSamples.forEach(sample => {
            let sampleScore = 0;
            // Scoring based on quality and correctness
            if (sample.isCorrect) {
                if (sample.quality === "ברור מאוד") sampleScore = 5;
                else if (sample.quality === "ברור") sampleScore = 4;
                else if (sample.quality === "קצת רעש") sampleScore = 3;
                 else if (sample.quality === "המהום") sampleScore = 2;
                 else if (sample.quality === "רעש חזק") sampleScore = 1;
                 else if (sample.quality === "המהום חזק") sampleScore = 1;
                 else sampleScore = 3; // Default for unforeseen qualities
            } else {
                 // Penalty for incorrect tags, more severe on clear samples
                 if (sample.quality === "ברור מאוד") sampleScore = -3;
                 else if (sample.quality === "ברור") sampleScore = -2;
                 else sampleScore = -1; // Less penalty on noisy/mumbled
            }
            effectiveScore += sampleScore;
        });

        // Add a base accuracy that comes from the number of samples, grows logarithmically or similar
        // Simple approach: Base + scaled score + bonus for volume
        let baseAccuracy = Math.min(trainedSamples.length * 2, 20); // Starts faster, caps
        let qualityScoreImpact = (effectiveScore / maxPossibleScore) * 40; // Impact up to 40% based on quality/correctness
        let volumeBonus = trainedSamples.length >= allSamples.length ? 10 : 0; // Bonus for completing all samples

        let accuracy = baseAccuracy + qualityScoreImpact + volumeBonus;


        // Clamp accuracy between reasonable bounds
        accuracy = Math.max(0, accuracy); // Cannot go below 0
        accuracy = Math.min(99, accuracy); // Cannot reach 100% (real models never perfect)

        // Smooth out rapid changes and make it feel slightly less linear? (Optional, current is fine)

        // Update progress bar
        accuracyProgressBar.style.width = `${accuracy}%`;

        // Make it look like a percentage, rounded
        return Math.round(accuracy);
    }

    function updateStatus() {
        trainedSamplesCountEl.textContent = trainedSamples.length;
        const accuracy = calculateExpectedAccuracy();
        expectedAccuracyEl.textContent = `${accuracy}%`;

        if (trainedSamples.length >= minSamplesForTest) {
            runTestButton.disabled = false;
            runTestButton.textContent = `🚀 הרץ מבחן ביצועים (${trainedSamples.length} דוגמאות אומנו)`;
        } else {
            runTestButton.disabled = true;
            runTestButton.textContent = `🔬 הרץ מבחן ביצועים (נדרשות לפחות ${minSamplesForTest} דוגמאות אימון)`;
        }
    }

    function handleSubmitTag() {
        const userTag = userTagInput.value.trim();
        if (!userTag) {
            taggingFeedbackEl.textContent = "אופס! אנא כתוב מה שמעת לפני שאתה שולח.";
            taggingFeedbackEl.className = 'feedback error';
             taggingFeedbackEl.style.opacity = 1;
             taggingFeedbackEl.style.transform = 'translateY(0)';
            return;
        }

        // Disable input and button immediately
        userTagInput.disabled = true;
        submitTagButton.disabled = true;
         sampleAudioPlaceholder.style.pointerEvents = 'none'; // Disable clicking audio again
        sampleAudioPlaceholder.style.opacity = 0.5;
        sampleAudioIcon.style.opacity = 0.5;


        const isCorrect = userTag.toLowerCase() === currentSample.text.toLowerCase();
        let feedbackText;
        let feedbackClass;

        if (isCorrect) {
             feedbackText = "מעולה! התיוג נכון. המודל למד נהדר מהדוגמה הזו.";
             feedbackClass = 'success';
        } else {
             feedbackText = `אופס! התיוג היה שגוי. הטקסט הנכון היה: "${currentSample.text}". המודל צריך עוד אימון על דוגמאות כאלה.`;
             feedbackClass = 'error';
        }

        taggingFeedbackEl.textContent = feedbackText;
        taggingFeedbackEl.className = `feedback ${feedbackClass}`;
         taggingFeedbackEl.style.opacity = 1;
         taggingFeedbackEl.style.transform = 'translateY(0)';


        trainedSamples.push({
            originalText: currentSample.text,
            userTag: userTag,
            quality: currentSample.quality,
            isCorrect: isCorrect
        });

        updateStatus();

        // Add a delay before loading the next sample to allow user to read feedback
        sampleLoadTimeout = setTimeout(loadNextSample, 2500); // 2.5 second delay
    }

    function runTest() {
         testResultsEl.style.display = 'none'; // Hide previous results instantly
         testSampleListEl.innerHTML = '<h5>פירוט הדוגמאות שנבדקו:</h5>'; // Clear list

        // Select samples for test: prioritize unused samples, supplement if needed
        const trainedSampleKeys = new Set(trainedSamples.map(s => s.originalText + s.quality));
        let potentialTestSamples = allSamples.filter(s => !trainedSampleKeys.has(s.text + s.quality));

        // Ensure a minimum number of test samples, but don't exceed total samples
        const minTestSamples = Math.min(Math.max(trainedSamples.length / 2, 10), allSamples.length - trainedSamples.length); // Test on half of trained or 10, max remaining
        const numTestSamples = Math.max(minTestSamples, potentialTestSamples.length > 0 ? minTestSamples : Math.min(trainedSamples.length, 15)); // If no unused, test on trained (max 15)


        let testSet = [];
        // First, try to pull from unused samples, shuffle first
        const shuffledPotential = [...potentialTestSamples].sort(() => 0.5 - Math.random());
        testSet = shuffledPotential.slice(0, numTestSamples);

         // If not enough from unused (unlikely with enough samples, but safe), add from trained samples
         // This part makes the test less 'pure' but ensures a test runs.
        while (testSet.length < numTestSamples && testSet.length < allSamples.length) {
             const randomTrainedSample = trainedSamples[Math.floor(Math.random() * trainedSamples.length)];
             const trainedSampleForTest = { // Create a similar object structure
                 text: randomTrainedSample.originalText,
                 quality: randomTrainedSample.quality
             };
             // Add only if not already in the test set
             if (!testSet.some(s => s.text === trainedSampleForTest.text && s.quality === trainedSampleForTest.quality)) {
                 testSet.push(trainedSampleForTest);
             }
         }


        let correctPredictions = 0;

        const expectedAccuracy = calculateExpectedAccuracy(); // Use calculated accuracy

        testSet.forEach(sample => {
            const randomChance = Math.random() * 100;
            let isPredictedCorrectly = false;

            // Simulate prediction success based on expected accuracy and quality
            let sampleSpecificChance = expectedAccuracy;

             // Adjust chance based on quality - harder samples decrease chance relative to average
             if (sample.quality === 'ברור מאוד') sampleSpecificChance = expectedAccuracy * 1.2;
             else if (sample.quality === 'ברור') sampleSpecificChance = expectedAccuracy * 1.1;
             else if (sample.quality === 'קצת רעש') sampleSpecificChance = expectedAccuracy * 0.9;
             else if (sample.quality === 'המהום') sampleSpecificChance = expectedAccuracy * 0.8;
             else if (sample.quality === 'רעש חזק') sampleSpecificChance = expectedAccuracy * 0.6;
             else if (sample.quality === 'המהום חזק') sampleSpecificChance = expectedAccuracy * 0.5;
             else sampleSpecificChance = expectedAccuracy; // Default

            // Clamp chance between a base minimum and a high maximum
            sampleSpecificChance = Math.max(5, sampleSpecificChance); // Even a bad model isn't 0%
            sampleSpecificChance = Math.min(99, sampleSpecificChance); // Hard to get 100% on a real test


            if (randomChance < sampleSpecificChance) {
                isPredictedCorrectly = true;
                correctPredictions++;
            }

            const resultClass = isPredictedCorrectly ? 'correct' : 'incorrect';
            const resultText = isPredictedCorrectly ? 'זוהה נכון' : 'זוהה שגוי';
            const resultIcon = isPredictedCorrectly ? '<span class="correct-icon"></span>' : '<span class="incorrect-icon"></span>';

            const resultDiv = document.createElement('div');
            resultDiv.className = `sample-result ${resultClass}`;
            resultDiv.innerHTML = `"${sample.text}" (${sample.quality})${resultIcon}`; // Add icon here
            testSampleListEl.appendChild(resultDiv);
        });

        const totalTestSamples = testSet.length;
        const testAccuracy = totalTestSamples > 0 ? Math.round((correctPredictions / totalTestSamples) * 100) : 0;

        correctTestCountEl.textContent = correctPredictions;
        totalTestCountEl.textContent = totalTestSamples;
        testAccuracyEl.textContent = `${testAccuracy}%`;

        // Animate results display
        testResultsEl.style.opacity = 0;
        testResultsEl.style.transform = 'translateY(20px)';
        testResultsEl.style.display = 'block';
         setTimeout(() => {
             testResultsEl.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
             testResultsEl.style.opacity = 1;
             testResultsEl.style.transform = 'translateY(0)';
         }, 10); // Small delay to allow display: block to take effect
    }

    function toggleExplanation() {
        const isHidden = explanationEl.style.display === 'none';
        if (isHidden) {
            explanationEl.style.opacity = 0;
            explanationEl.style.transform = 'translateY(20px)';
            explanationEl.style.display = 'block';
             setTimeout(() => {
                 explanationEl.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
                 explanationEl.style.opacity = 1;
                 explanationEl.style.transform = 'translateY(0)';
             }, 10);
            showExplanationButton.innerHTML = '<i class="icon info-icon"></i> הסתר הסבר: איך זיהוי דיבור עובד?';
        } else {
             explanationEl.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
            explanationEl.style.opacity = 0;
             explanationEl.style.transform = 'translateY(20px)';
             setTimeout(() => {
                 explanationEl.style.display = 'none';
                 showExplanationButton.innerHTML = '<i class="icon info-icon"></i> הצג הסבר: איך זיהוי דיבור עובד?';
                 explanationEl.style.transition = ''; // Remove transition for next show
             }, 500); // Wait for animation to finish
        }
    }

    // Event Listeners
    submitTagButton.addEventListener('click', handleSubmitTag);
    userTagInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent default form submission if inside a form
            handleSubmitTag();
        }
    });
    runTestButton.addEventListener('click', runTest);
    showExplanationButton.addEventListener('click', toggleExplanation);


    // Initial load
    loadNextSample();
    updateStatus();
</script>
```