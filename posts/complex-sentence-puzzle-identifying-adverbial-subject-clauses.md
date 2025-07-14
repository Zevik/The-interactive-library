---
title: "משחק הפסוקיות: מי נגד מי במשפט המורכב?"
english_slug: complex-sentence-puzzle-identifying-adverbial-subject-clauses
category: "בלשנות"
tags: [לשון, תחביר, פסוקית, משפט מורכב, עברית, דקדוק, סימולציה, תרגול]
---
<div id="app-container" class="game-container">
    <h1 class="game-title">משחק הפסוקיות: מי נגד מי במשפט המורכב?</h1>
    <p class="game-intro">משפטים ארוכים ומפותלים הם כמו פאזל תחבירי! האם תצליחו לפענח את התפקיד הנסתר של כל "שחקן" במשפט? הסימולציה הזו תאתגר אתכם לזהות את התפקידים המרכזיים של פסוקיות במשפטים מורכבים.</p>

    <div id="sentence-area">
        <div id="sentence-display" class="sentence-display">
            <!-- Sentence parts will be loaded here -->
        </div>
        <p class="question-prompt">איזה תפקיד תחבירי ממלא החלק המודגש במשפט?</p>
    </div>

    <div id="options-container" class="options-container">
        <!-- Options will be loaded here -->
    </div>

    <div id="feedback-area">
        <div id="feedback-container" class="feedback-container">
            <!-- Feedback will be displayed here -->
        </div>
         <button id="next-question-btn" class="control-button next-button" style="display:none;">שאלה הבאה</button>
    </div>
</div>

<button id="toggle-explanation" class="control-button explanation-button">רוצים רמז? הצגת הסבר</button>

<div id="explanation" class="explanation-box" style="display: none;">
    <h2>סודות המשפט המורכב: המדריך למתחיל/ה</h2>
    <p>הנה הצצה קטנה לעולם המשפטים המורכבים, שתעזור לכם במשחק:</p>

    <h3>פשטות מול מורכבות:</h3>
    <ul>
        <li><strong>משפט פשוט:</strong> יש לו נשוא (פועל או אוגד+שם) אחד בלבד. למשל: "חתול ישן."</li>
        <li><strong>משפט מורכב:</strong> מכיל נשוא עיקרי (במשפט העיקרי) ונשוא נוסף (בפסוקית המשועבדת), שמחוברים לרוב באמצעות מילת שעבוד (כמו 'ש', 'כי', 'כאשר'). הפסוקית היא כמו "משפטון" שתלוי במשפט העיקרי וממלא בו תפקיד תחבירי. למשל: "חתול ישן <strong>כי קר לו</strong>." ('ישן' - נשוא עיקרי, 'קר' - נשוא בפסוקית 'כי קר לו').</li>
    </ul>

    <h3>הכר את הפסוקיות המרכזיות במשחק:</h3>
    <ul>
        <li><h4>פסוקית תיאור:</h4>
            <p>תפקוד: כמו תיאור במשפט פשוט.</p>
            <p>מטרה: מתארת את הנשוא (איך? מתי? היכן? למה?) או את המשפט כולו.</p>
            <p>מילות שעבוד נפוצות:
            <ul>
                <li><strong>זמן:</strong> כְּשֶׁ-, בְּשָׁעָה שֶׁ-, אַחֲרֵי שֶׁ-, לִפְנֵי שֶׁ-, כָּל עוֹד, מֵאָז שֶׁ- (עונה על: מתי?)</li>
                <li><strong>מקום:</strong> הֵיכָן שֶׁ-, אֵיפָה שֶׁ- (עונה על: היכן?)</li>
                <li><strong>סיבה:</strong> כִּי, מִפְּנֵי שֶׁ-, הוֹאִיל וְ-, מֵחֲמַת שֶׁ- (עונה על: למה? מדוע?)</li>
                <li><strong>תכלית:</strong> כְּדֵי שֶׁ-, עַל מְנָת שֶׁ- (עונה על: לאיזו מטרה?)</li>
                <li><strong>ויתור:</strong> אַף עַל פִּי שֶׁ-, לַמְרוֹת שֶׁ-, הַגַּם שֶׁ- (עונה על: למרות מה?)</li>
                <li><strong>תנאי:</strong> אִם, אִילּוּ, לוּ, לוּלֵא (עונה על: בתנאי מה?)</li>
                 <li><strong>אופן:</strong> כְּפִי שֶׁ-, כְּמוֹ שֶׁ- (עונה על: איך?)</li>
            </ul>
            </p>
        </li>
        <li><h4>פסוקית נושא:</h4>
            <p>תפקוד: כמו נושא במשפט פשוט.</p>
            <p>מטרה: היא זו שמבצעת את הפעולה או נמצאת במצב המתואר בנשוא העיקרי.</p>
            <p>זיהוי: מופיעה לרוב אחרי פעלים או ביטויים כמו: <em>חָשׁוּב שֶׁ...</em>, <em>יָדוּעַ שֶׁ...</em>, <em>נֶאֱמַר כִּי...</em>, <em>הִתְבָּרֵר שֶׁ...</em>, <em>אֶפְשָׁרִי שֶׁ...</em>, <em>מְצַעֵר שֶׁ...</em>, <em>עָצוּב כִּי...</em>. או אחרי שמות עצם מופשטים כמו: <em>הָעוּבְדָא שֶׁ...</em>, <em>הַשְּׁמוּעָה כִּי...</em>, <em>הַהַרְגָּשָׁה שֶׁ...</em>. נסו לשאול 'מי?' או 'מה?' לפני הנשוא העיקרי - התשובה היא הפסוקית.</p>
             <p>דוגמה להבחנה: <u>שאתה שמח</u> משמח אותי (<strong>פסוקית נושא</strong>: מה משמח? שאתה שמח). אני שמח <u>כי אתה כאן</u> (<strong>פסוקית תיאור סיבה</strong>: למה אני שמח? כי אתה כאן).</p>
        </li>
    </ul>
     <p>ועכשיו, חזרה למשחק! בהצלחה!</p>
</div>

<style>
    /* General Styles & Layout */
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --warning-color: #ffc107;
        --info-color: #17a2b8;
        --light-color: #f8f9fa;
        --dark-color: #343a40;
        --border-radius: 8px;
        --box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --transition-speed: 0.3s;
    }

    #app-container {
        direction: rtl;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        max-width: 750px; /* Slightly wider */
        margin: 30px auto;
        padding: 30px; /* More padding */
        border: none; /* Remove default border */
        border-radius: var(--border-radius);
        background-color: var(--light-color);
        box-shadow: var(--box-shadow); /* Add shadow */
        display: flex; /* Use flexbox for layout */
        flex-direction: column;
        gap: 25px; /* Spacing between sections */
    }

    .game-title {
        text-align: center;
        color: var(--primary-color);
        margin-bottom: 15px;
        font-size: 2em; /* Larger title */
        font-weight: bold;
    }

    .game-intro {
        text-align: center;
        color: var(--dark-color);
        margin-bottom: 25px;
        font-size: 1.1em;
        line-height: 1.6;
    }

    #sentence-area {
        background-color: #e9ecef;
        padding: 20px;
        border-radius: var(--border-radius);
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
        text-align: center; /* Center content */
    }

    .sentence-display {
        font-size: 1.3em; /* Larger font */
        margin-bottom: 20px;
        line-height: 1.8; /* More space between lines */
    }

    .sentence-part {
        display: inline; /* Keep parts inline naturally */
        transition: transform var(--transition-speed) ease; /* Animation potential */
    }

    .highlighted {
        font-weight: bold;
        color: var(--primary-color);
        text-decoration: none; /* Remove default underline */
        border-bottom: 3px solid var(--primary-color); /* Modern underline */
        padding-bottom: 2px; /* Space for underline */
        transition: border-color var(--transition-speed) ease;
    }

     .highlighted.correct-answer {
        border-bottom-color: var(--success-color);
        color: var(--success-color);
     }
     .highlighted.incorrect-answer {
         border-bottom-color: var(--danger-color);
         color: var(--danger-color);
     }


    .question-prompt {
        font-size: 1.2em; /* Larger prompt */
        margin-top: 15px;
        color: var(--dark-color);
        font-weight: normal; /* Less bold */
    }

    .options-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px; /* More space between buttons */
        margin-bottom: 25px;
    }

    .option-button {
        background-color: white; /* White background */
        border: 1px solid #ccc;
        border-radius: var(--border-radius); /* Rounded corners */
        padding: 12px 20px; /* More padding */
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        transition: background-color var(--transition-speed) ease,
                    border-color var(--transition-speed) ease,
                    transform 0.1s ease,
                    box-shadow var(--transition-speed) ease; /* Add transform & shadow */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); /* Subtle shadow */
        min-width: 120px; /* Minimum width for buttons */
        text-align: center;
    }

    .option-button:hover:not(:disabled) {
        background-color: #e9ecef; /* Light hover effect */
        border-color: #b3b3b3;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
    }

    .option-button:active:not(:disabled) {
        transform: scale(0.98); /* Press effect */
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

     .option-button:disabled {
         opacity: 0.7;
         cursor: not-allowed;
     }

    .option-button.correct {
        background-color: var(--success-color);
        border-color: var(--success-color);
        color: white; /* White text for contrast */
        font-weight: bold;
        animation: pulse-correct 0.5s ease; /* Add pulse animation */
    }

    .option-button.incorrect {
        background-color: var(--danger-color);
        border-color: var(--danger-color);
        color: white; /* White text */
        font-weight: bold;
        animation: shake 0.5s ease; /* Add shake animation */
    }

    #feedback-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        min-height: 80px; /* Ensure space is reserved */
    }


    .feedback-container {
        width: 100%; /* Take full width */
        padding: 15px; /* More padding */
        border-radius: var(--border-radius);
        min-height: 1.5em; /* Reserve space */
        text-align: center;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly lower */
        transition: opacity var(--transition-speed) ease, transform var(--transition-speed) ease;
    }

    .feedback-container.visible {
        opacity: 1;
        transform: translateY(0);
    }


    .feedback-correct {
        background-color: #d4edda; /* Light green */
        color: #155724; /* Dark green */
        border: 1px solid #c3e6cb;
    }

    .feedback-incorrect {
        background-color: #f8d7da; /* Light red */
        color: #721c24; /* Dark red */
        border: 1px solid #f5c6cb;
    }
     .feedback-explanation {
        margin-top: 10px;
        font-size: 0.95em;
        color: #555;
        line-height: 1.5;
    }

    .control-button {
        display: block;
        margin: 0 auto; /* Center buttons */
        padding: 12px 25px;
        font-size: 1.1em;
        border: none;
        border-radius: var(--border-radius);
        cursor: pointer;
        transition: background-color var(--transition-speed) ease,
                    opacity var(--transition-speed) ease,
                    transform 0.1s ease; /* Add transform */
        box-shadow: var(--box-shadow);
        font-weight: bold;
    }

     .control-button:hover {
         opacity: 0.9;
         box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15);
     }
     .control-button:active {
         transform: scale(0.98);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
     }

    .next-button {
        background-color: var(--primary-color);
        color: white;
    }

    .explanation-button {
        background-color: var(--secondary-color);
        color: white;
        margin-top: 20px; /* Space above explanation button */
         width: fit-content; /* Button fits content */
    }

    .explanation-box {
        direction: rtl;
        background-color: #e9ecef;
        padding: 25px;
        border-radius: var(--border-radius);
        margin-top: 25px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
        line-height: 1.7;
        color: var(--dark-color);
        font-size: 1em;
    }
    .explanation-box h2, .explanation-box h3, .explanation-box h4 {
        color: var(--dark-color);
        margin-top: 20px;
        margin-bottom: 12px;
        font-weight: bold;
    }
     .explanation-box h2 { font-size: 1.7em; border-bottom: 2px solid var(--primary-color); padding-bottom: 5px;}
     .explanation-box h3 { font-size: 1.4em; color: var(--primary-color);}
     .explanation-box h4 { font-size: 1.2em; color: var(--secondary-color); margin-bottom: 5px;}


    .explanation-box p, .explanation-box ul {
        margin-bottom: 15px;
    }
    .explanation-box ul {
        padding-right: 25px; /* RTL padding */
        list-style: disc;
    }
     .explanation-box ul ul {
         list-style: circle;
         margin-top: 5px;
         margin-bottom: 5px;
     }

    /* Animations */
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }

    @keyframes pulse-correct {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .feedback-container.animate-in {
        animation: fadeIn var(--transition-speed) ease forwards;
    }

     /* Optional: Add animation to highlighted part on reveal */
     .sentence-part.reveal-correct {
         animation: pulse-correct 0.8s ease;
     }
    .sentence-part.reveal-incorrect {
         animation: shake 0.5s ease;
     }


</style>

<script>
    const questions = [
        {
            sentenceParts: ["<b>כאשר הגיע האביב</b>", ", הטבע פרח."],
            highlightedIndex: 0,
            options: ["פסוקית תיאור זמן", "פסוקית נושא", "פסוקית עיקרית", "פסוקית תיאור סיבה"],
            correctAnswer: "פסוקית תיאור זמן",
            explanation: "נכון! הפסוקית 'כאשר הגיע האביב' מציינת מתי התרחשה הפעולה העיקרית ('הטבע פרח'). מילת השעבוד 'כאשר' היא רמז מובהק לפסוקית תיאור זמן. שאלה: מתי הטבע פרח? תשובה: כאשר הגיע האביב."
        },
        {
            sentenceParts: ["זה", "<b>שכולם הסכימו</b>", "הפתיע אותי."],
            highlightedIndex: 1,
            options: ["פסוקית תיאור אופן", "פסוקית נושא", "פסוקית עיקרית", "פסוקית תיאור תכלית"],
            correctAnswer: "פסוקית נושא",
            explanation: "בול! הפסוקית 'שכולם הסכימו' היא הנושא במשפט העיקרי 'זה הפתיע אותי'. היא מבצעת את הפעולה 'הפתיע'. שאלה: מה הפתיע אותי? תשובה: שכולם הסכימו. כמו כן, היא באה אחרי 'זה' - מאפיין נפוץ לפסוקיות נושא."
        },
        {
            sentenceParts: ["נסענו לים", "<b>על מנת שנוכל להירגע</b>", "."],
            highlightedIndex: 1,
            options: ["פסוקית תיאור זמן", "פסוקית נושא", "פסוקית עיקרית", "פסוקית תיאור תכלית"],
            correctAnswer: "פסוקית תיאור תכלית",
            explanation: "יופי! הפסוקית 'על מנת שנוכל להירגע' מציינת את המטרה (התכלית) של הפעולה העיקרית ('נסענו לים'). מילת השעבוד 'על מנת ש' היא סימן זיהוי מצוין לפסוקית תיאור תכלית. שאלה: לאיזו מטרה נסענו לים? תשובה: על מנת שנוכל להירגע."
        },
         {
            sentenceParts: ["העובדה", "<b>כי הוא הצליח</b>", "לא הפתיעה איש."],
            highlightedIndex: 1,
            options: ["פסוקית תיאור סיבה", "פסוקית נושא", "פסוקית עיקרית", "פסוקית תיאור ויתור"],
            correctAnswer: "פסוקית נושא",
            explanation: "מדויק! הפסוקית 'כי הוא הצליח' היא זו שמבצעת את הפעולה העיקרית 'לא הפתיעה' (או ליתר דיוק, היא מפרטת מהי ה'עובדה' שהיא הנושא הנסתר/גלוי). פסוקיות נושא מופיעות לעיתים קרובות אחרי שמות עצם מופשטים כמו 'עובדה', 'שמועה', 'הרגשה'. שאלה: מה לא הפתיע איש? תשובה: העובדה כי הוא הצליח."
        },
        {
            sentenceParts: ["הוא שמח", "<b>למרות שהתוצאה לא הייתה טובה</b>", "."],
            highlightedIndex: 1,
            options: ["פסוקית תיאור זמן", "פסוקית נושא", "פסוקית עיקרית", "פסוקית תיאור ויתור"],
            correctAnswer: "פסוקית תיאור ויתור",
            explanation: "מצוין! הפסוקית 'למרות שהתוצאה לא הייתה טובה' מתארת תנאי שממנו מתעלמים, או מצב שקורה למרות קיום התנאי הזה. מילת השעבוד 'למרות ש' היא המפתח לזיהוי פסוקית תיאור ויתור. שאלה: למרות מה הוא שמח? תשובה: למרות שהתוצאה לא הייתה טובה."
        }
    ];

    let currentQuestionIndex = 0;
    const sentenceDisplay = document.getElementById('sentence-display');
    const optionsContainer = document.getElementById('options-container');
    const feedbackContainer = document.getElementById('feedback-container');
    const nextButton = document.getElementById('next-question-btn');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
     const highlightedPart = document.querySelector('.highlighted'); // Will get updated

    function displayQuestion(index) {
        const question = questions[index];
        sentenceDisplay.innerHTML = '';
        question.sentenceParts.forEach((part, i) => {
            const span = document.createElement('span');
            span.innerHTML = part; // Use innerHTML to render potential bold tags from data
            span.classList.add('sentence-part');
            if (i === question.highlightedIndex) {
                 // Assuming the highlighted part is wrapped in <b> in the data
                 // If not, would add the class here: span.classList.add('highlighted');
            }
            sentenceDisplay.appendChild(span);
        });

         // Re-query the highlighted part after adding HTML
         const currentHighlightedSpan = sentenceDisplay.querySelector('.sentence-part b') ? sentenceDisplay.querySelector('.sentence-part b').parentElement : sentenceDisplay.querySelector('.sentence-part');
         if(currentHighlightedSpan) {
             currentHighlightedSpan.classList.add('highlighted');
         }


        optionsContainer.innerHTML = '';
        question.options.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option;
            button.classList.add('option-button');
            button.addEventListener('click', () => handleAnswer(button, option, question.correctAnswer, question.explanation));
            optionsContainer.appendChild(button);
        });

        feedbackContainer.innerHTML = '';
        feedbackContainer.className = 'feedback-container'; // Reset classes
        nextButton.style.display = 'none';
        optionsContainer.style.pointerEvents = 'auto'; // Enable buttons
        optionsContainer.querySelectorAll('.option-button').forEach(btn => btn.disabled = false); // Ensure buttons are enabled
        if(currentHighlightedSpan) {
             currentHighlightedSpan.classList.remove('correct-answer', 'incorrect-answer', 'reveal-correct', 'reveal-incorrect'); // Reset animation/color classes
        }
    }

    function handleAnswer(clickedButton, selectedOption, correctAnswer, explanation) {
        const optionButtons = optionsContainer.querySelectorAll('.option-button');
        optionButtons.forEach(button => {
            button.disabled = true; // Disable all buttons after selection
            button.classList.remove('correct', 'incorrect');
            if (button.textContent === correctAnswer) {
                button.classList.add('correct');
            } else if (button.textContent === selectedOption) {
                 button.classList.add('incorrect');
            }
        });

         const currentHighlightedSpan = sentenceDisplay.querySelector('.sentence-part b') ? sentenceDisplay.querySelector('.sentence-part b').parentElement : sentenceDisplay.querySelector('.sentence-part.highlighted');


        const feedbackText = document.createElement('p');
        const explanationText = document.createElement('p');
        explanationText.classList.add('feedback-explanation');

        feedbackContainer.innerHTML = ''; // Clear previous feedback
        feedbackContainer.classList.remove('feedback-correct', 'feedback-incorrect', 'visible'); // Reset classes before adding new ones

        if (selectedOption === correctAnswer) {
            feedbackContainer.classList.add('feedback-correct');
            feedbackText.textContent = '🎉 תשובה נכונה! 🎉';
            explanationText.textContent = explanation;
             if(currentHighlightedSpan) {
                currentHighlightedSpan.classList.add('correct-answer', 'reveal-correct');
            }
        } else {
            feedbackContainer.classList.add('feedback-incorrect');
            feedbackText.textContent = `🤔 אופס, זו לא התשובה הנכונה. התשובה הנכונה היא: "${correctAnswer}".`;
            explanationText.textContent = explanation;
             if(currentHighlightedSpan) {
                currentHighlightedSpan.classList.add('incorrect-answer', 'reveal-incorrect');
            }
        }
        feedbackContainer.appendChild(feedbackText);
        feedbackContainer.appendChild(explanationText);
        feedbackContainer.classList.add('visible'); // Trigger fade in animation


        nextButton.style.display = 'block'; // Show next button
        optionsContainer.style.pointerEvents = 'none'; // Disable buttons via pointer events
    }

    function nextQuestion() {
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            displayQuestion(currentQuestionIndex);
        } else {
            // End of quiz
            sentenceDisplay.innerHTML = '<h3 style="text-align: center; color: var(--success-color);">🥳 כל הכבוד! סיימת את כל השאלות והפכת לאלופי הפסוקיות! 🏆</h3>';
            optionsContainer.innerHTML = '';
            feedbackContainer.innerHTML = '';
            nextButton.style.display = 'none';
            // Optionally hide explanation toggle or change its text
             toggleExplanationButton.style.display = 'none';
             explanationDiv.style.display = 'none';
        }
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'רוצים רמז? הצגת הסבר';
    }

    // Initialize
    document.addEventListener('DOMContentLoaded', () => {
        displayQuestion(currentQuestionIndex);
        nextButton.addEventListener('click', nextQuestion);
        toggleExplanationButton.addEventListener('click', toggleExplanation);
    });

</script>
---