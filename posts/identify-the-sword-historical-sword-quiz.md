---
title: "אמן החרבות: אתגר זיהוי כלי נשק היסטוריים"
english_slug: identify-the-sword-historical-sword-quiz
category: "ארכאולוגיה"
tags:
    - חרבות
    - רומא העתיקה
    - ימי הביניים
    - ארכיאולוגיה
    - היסטוריה צבאית
---
<h1>אמן החרבות: אתגר זיהוי כלי נשק היסטוריים</h1>
<p>האם אתה יכול לזהות חרב היסטורית ממבט ראשון? האם תבדיל בין הלהב הקטלני של לגיון רומאי לחרב האדירה של אביר ימי הביניים? שים את הידע שלך במבחן באתגר האינטראקטיבי הזה!</p>

<div class="interaction-container">
    <div id="interaction-area">
        <div class="image-wrapper">
             <img id="sword-image" src="" alt="תמונה של חרב היסטורית לזיהוי">
        </div>

        <p id="question-text">איזו חרב זו?</p>
        <div id="options-container">
            <!-- Buttons will be inserted here by JS -->
        </div>
        <div id="feedback"></div>
        <button id="next-button" class="control-button">האתגר הבא</button>
         <div id="progress-tracker"></div>
    </div>
    <div id="summary-area" class="fade-in">
        <h2>סיום האתגר!</h2>
        <p id="final-score"></p>
        <button id="restart-button" class="control-button">התחל מחדש</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #4a2c2a; /* Dark earthy brown */
        --secondary-color: #d4a373; /* Lighter brown/tan */
        --accent-color: #a98467; /* Medium brown */
        --background-color: #f5f5dc; /* Creamy white / Parchment */
        --text-color: #333;
        --correct-color: #38a169; /* Forest green */
        --incorrect-color: #e53e3e; /* Muted red */
        --button-bg-color: var(--secondary-color);
        --button-hover-bg-color: var(--accent-color);
    }

    body {
        font-family: 'Arial', sans-serif; /* Consider a more historical-feeling font if available */
        background-color: var(--background-color);
        color: var(--text-color);
        direction: rtl;
        text-align: right;
        line-height: 1.6;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 1em;
    }

    .interaction-container {
        border: 2px solid var(--accent-color);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 30px;
        border-radius: 12px;
        max-width: 650px; /* Slightly wider */
        margin: 30px auto;
        background-color: #fff; /* White background for contrast */
        position: relative; /* For potential absolute positioning */
    }

    #interaction-area {
        transition: opacity 0.5s ease-in-out; /* Fade effect */
    }

    .image-wrapper {
        width: 100%;
        max-width: 400px; /* Control image max size better */
        margin: 0 auto 20px;
        border: 1px solid var(--accent-color);
        padding: 10px;
        background-color: #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        border-radius: 8px;
        overflow: hidden; /* Ensures shadow/border is around the image */
    }

    #sword-image {
        display: block;
        width: 100%;
        height: auto;
        object-fit: contain; /* Ensure image fits within the wrapper */
        transition: opacity 0.8s ease-in-out; /* Fade in effect for images */
    }

    #question-text {
        font-size: 1.3em; /* Slightly larger */
        margin-bottom: 20px;
        font-weight: bold;
        text-align: center;
        color: var(--primary-color);
    }

    #options-container {
         text-align: center;
         margin-bottom: 20px;
         display: flex; /* Use flexbox for button layout */
         flex-wrap: wrap; /* Allow buttons to wrap on smaller screens */
         justify-content: center;
    }

    #options-container button {
        margin: 8px; /* Slightly more margin */
        padding: 12px 25px; /* Larger padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        background-color: var(--button-bg-color);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Add transform for press effect */
        font-weight: bold;
        min-width: 120px; /* Ensure minimum button width */
    }

    #options-container button:hover:not(:disabled) {
        background-color: var(--button-hover-bg-color);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }

     #options-container button:active:not(:disabled) {
        transform: scale(0.98); /* Simple press effect */
     }

    #options-container button:disabled {
        background-color: #ccc;
        color: #666;
        cursor: not-allowed;
        opacity: 0.7;
    }

    #options-container button.selected-correct {
         background-color: var(--correct-color);
         color: white;
         border: 2px solid darken(var(--correct-color), 10%);
         box-shadow: 0 0 8px rgba(56, 161, 105, 0.5); /* Glow effect */
    }

    #options-container button.selected-incorrect {
         background-color: var(--incorrect-color);
         color: white;
         border: 2px solid darken(var(--incorrect-color), 10%);
    }

     #options-container button.correct-answer {
         background-color: var(--correct-color);
         color: white;
         border: 2px dashed white; /* Indicate the correct answer after wrong choice */
         opacity: 0.9;
     }


    #feedback {
        font-size: 1.2em; /* Larger feedback text */
        margin-top: 15px;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        min-height: 2em; /* Ensure space even when empty */
        opacity: 0; /* Start hidden, fade in with JS */
        transform: translateY(10px); /* Start slightly below, slide up */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    #feedback.visible {
        opacity: 1;
        transform: translateY(0);
    }

    #feedback.correct {
        color: var(--correct-color);
        /* background-color: rgba(56, 161, 105, 0.1); */
    }

    #feedback.incorrect {
        color: var(--incorrect-color);
        /* background-color: rgba(229, 62, 62, 0.1); */
    }

    .control-button {
        margin-top: 20px;
        display: block;
        width: fit-content;
        margin-left: auto;
        margin-right: auto;
        padding: 12px 25px; /* Larger padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--primary-color);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .control-button:hover:not(:disabled) {
        background-color: darken(var(--primary-color), 10%);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    .control-button:active:not(:disabled) {
        transform: scale(0.98);
    }


     #summary-area {
        text-align: center;
        margin-top: 20px;
        padding: 20px;
        /* display: none; Handled by JS animation */
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }

     #summary-area.visible {
        opacity: 1;
        transform: translateY(0);
     }


    #summary-area h2 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    #final-score {
        font-size: 1.4em;
        font-weight: bold;
        color: var(--text-color);
        margin-bottom: 20px;
    }

    #progress-tracker {
        text-align: center;
        margin-top: 15px;
        font-size: 1em;
        color: #555;
    }


    #explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More margin */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--accent-color); /* Different color for explanation */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    #explanation-button:hover {
        background-color: darken(var(--accent-color), 10%);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
     #explanation-button:active {
        transform: scale(0.98);
     }


    #explanation {
        margin-top: 30px;
        padding: 30px; /* More padding */
        border: 2px solid var(--accent-color);
        border-radius: 12px;
        background-color: #fff;
        direction: rtl;
        text-align: right;
        /* display: none; Handled by JS */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
         opacity: 0; /* Start hidden, fade in */
        transform: translateY(20px);
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }
     #explanation.visible {
        opacity: 1;
        transform: translateY(0);
     }

    #explanation h2, #explanation h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
        text-align: center;
    }

    #explanation p {
        margin-bottom: 18px; /* More spacing */
        line-height: 1.7; /* Improved readability */
    }

     #explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Adjust for RTL */
        margin-bottom: 18px;
     }

     #explanation li {
        margin-bottom: 10px;
     }

     /* Responsive Adjustments */
     @media (max-width: 600px) {
        .interaction-container, #explanation {
            padding: 20px;
            margin: 20px auto;
        }
        #options-container button {
            width: 100%; /* Stack buttons on small screens */
            margin: 5px 0;
        }
        .image-wrapper {
            padding: 5px;
        }
     }
</style>

<button id="explanation-button">הצג הסבר מקיף על החרבות</button>

<div id="explanation">
    <h2>הסבר מורחב: הכירו את החרבות</h2>

    <p>החרב, כלי נשק וסמל רב עוצמה, עיצבה את מהלך ההיסטוריה האנושית. צורתה, חומריה וטכניקות השימוש בה התפתחו ללא הרף, משקפים שינויים בטכנולוגיה, באסטרטגיה צבאית ובחברה. הכרת המאפיינים הייחודיים של סוגי חרבות מרכזיים אינה רק מסע אל עולם הנשק, אלא הצצה מרתקת אל התקופות שבהן שלטו בשדה הקרב.</p>

    <h3>גלדיוס (Gladius)</h3>
    <p>הגלדיוס היה החרב הסטנדרטית והאיקונית של הלגיונרים הרומאים בעידן הרפובליקה והאימפריה המוקדמת. חרב קצרה (כ-50-60 ס"מ), רחבה, בעלת שפיץ משולש חד ביותר. היא עוצבה לדקירה קטלנית ויעילה בלחימה הצפופה של המערך הרומאי (טקטיקת ה"פוש והדקור" מאחורי המגן הגדול, הסקוטום). הגלדיוס היה נשק הכרעה בקרב פנים אל פנים, שנועד לגרום לפציעות חמורות במהירות.</p>

    <h3>ספאטה (Spatha)</h3>
    <p>הספאטה מייצגת את הדור הבא של חרבות באימפריה הרומית המאוחרת ולאחר מכן בתקופת נדידת העמים ותחילת ימי הביניים. היא ארוכה משמעותית מהגלדיוס (כ-70-100 ס"מ) והפכה לנשק העיקרי של פרשים ולוחמי חי"ר כבדים. האורך הנוסף הפך אותה ליעילה יותר לחיתוך מהיר תוך כדי תנועה או רכיבה. הספאטה הייתה חרב רב-תכליתית שאפשרה גם דקירה וגם חיתוך, והיוותה גשר בין החרבות הקצרות של העת העתיקה לחרבות הארוכות של ימי הביניים.</p>

    <h3>חרב ארוכה (Longsword)</h3>
    <p>החרב הארוכה, הידועה לעיתים גם כחרב "יד וחצי" או חרב דו-ידנית (במקרים מסוימים), הייתה נפוצה בימי הביניים הגבוהים והמאוחרים (בערך המאה ה-13 עד ה-16). היא התאפיינה בלהב ארוך וישר (לרוב מעל 80 ס"מ, ולעיתים אף מעל מטר), וידית ארוכה שנועדה לאחיזה בשתי ידיים לשליטה ועוצמה מרבית. החרב הארוכה הייתה נשק מתוחכם ששימש לשילוב של דקירות חזקות (נגד שריון לוחות כבד) וחיתוכים עוצמתיים. לימוד השימוש בה היווה ענף לחימה מורכב בפני עצמו.</p>

    <h3>איך לזהות במבט חטוף: טיפים ויזואליים</h3>
    <ul>
        <li>**גלדיוס:** חפשו להב קצר ורחב במיוחד, עם שפיץ מחודד וברור. זו החרב הקומפקטית והקשוחה של הלגיונר.</li>
        <li>**ספאטה:** ארוכה יותר מהגלדיוס, אך לרוב בעלת פרופורציות להב דומות יותר לחרב עתיקה מאשר לחרב ימי-ביניימית מאוחרת. ידיתה לרוב מיועדת ליד אחת. היא שלב המעבר הגדול.</li>
        <li>**חרב ארוכה:** סימן הזיהוי הבולט ביותר הוא הידית הארוכה, המאפשרת אחיזה בשתי ידיים. הלהב ארוך, ישר ולעיתים קרובות צר יותר יחסית לגלדיוס, ומלווה במוט שמירה (crossguard) ארוך ישר. זו החרב האייקונית של האביר.</li>
    </ul>

    <h3>מדוע הן השתנו?</h3>
    <p>ההתפתחות של החרבות מספרת את סיפור ההיסטוריה הצבאית: מהלוחמה הצפופה והמבוססת על חי"ר כבד של רומא (גלדיוס), דרך עליית חשיבות הפרשים ושינויים בטקטיקות חי"ר (ספאטה), ועד ללוחמה המורכבת נגד שריון לוחות בימי הביניים המאוחרים (חרב ארוכה). כל חרב היא קפסולת זמן טכנולוגית וטקטית.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const interactionArea = document.getElementById('interaction-area');
        const summaryArea = document.getElementById('summary-area');
        const swordImage = document.getElementById('sword-image');
        const questionText = document.getElementById('question-text');
        const optionsContainer = document.getElementById('options-container');
        const feedbackElement = document.getElementById('feedback');
        const nextButton = document.getElementById('next-button');
        const finalScoreElement = document.getElementById('final-score');
        const explanationButton = document.getElementById('explanation-button');
        const explanationSection = document.getElementById('explanation');
        const restartButton = document.getElementById('restart-button');
        const progressTracker = document.getElementById('progress-tracker');

        // IMPORTANT: Replace these placeholder image paths with actual image URLs hosted on your site
        // Use high-quality, clear images that highlight the key visual differences!
        const identificationData = [
            {
                image: '/assets/images/swords/gladius_pompeii_style.jpg', // Example: Pompeii style Gladius
                options: ['גלדיוס', 'ספאטה', 'חרב ארוכה'],
                correctAnswer: 'גלדיוס',
                feedback: 'נכון! זהו הגלדיוס הרומי הקלאסי, קצר ורחב - מושלם לדקירה בקרב צפוף.',
                incorrectFeedback: 'שגוי. זו לא ספאטה ולא חרב ארוכה. זהו הגלדיוס הרומי, קצר ורחב - מושלם לדקירה בקרב צפוף.'
            },
            {
                image: '/assets/images/swords/spatha_late_roman.jpg', // Example: Late Roman Spatha
                options: ['גלדיוס', 'ספאטה', 'חרב ארוכה'],
                correctAnswer: 'ספאטה',
                feedback: 'מצוין! זוהי ספאטה. שימו לב לאורך הגדול יותר לעומת הגלדיוס - מתאימה יותר לחיתוך ולשימוש מתוך סוס.',
                 incorrectFeedback: 'טעות. זו לא חרב ארוכה מימי הביניים. זוהי ספאטה, האבולוציה הרומית של הגלדיוס, ארוכה יותר ומתאימה לחיתוך.'
            },
            {
                image: '/assets/images/swords/longsword_oakeshott_type_xv.jpg', // Example: Longsword (Type XV or XVI)
                options: ['גלדיוס', 'ספאטה', 'חרב ארוכה'],
                correctAnswer: 'חרב ארוכה',
                feedback: 'קליעה בול! זוהי חרב ארוכה מימי הביניים. הידית הארוכה והלהב הישר מאפשרים שימוש בשתי ידיים לדקירה עוצמתית נגד שריון.',
                 incorrectFeedback: 'לא מדויק. זו לא חרב קצרה כמו הגלדיוס. זוהי חרב ארוכה מימי הביניים, שתוכננה לשימוש בשתי ידיים נגד שריון.'
            },
             {
                image: '/assets/images/swords/gladius_mainz_style.jpg', // Example: Mainz style Gladius
                options: ['ספאטה', 'גלדיוס', 'חרב ארוכה'],
                correctAnswer: 'גלדיוס',
                feedback: 'Bingo! זה שוב גלדיוס, הפעם בסגנון מיינץ עם להב רחב במיוחד. נשק ההכרעה של הלגיון!',
                 incorrectFeedback: 'נסה שוב. האורך הקצר והלהב הרחב מצביעים על הגלדיוס הרומי, לא על הספאטה הארוכה יותר או החרב הארוכה הדו-ידנית.'
            },
             {
                image: '/assets/images/swords/spatha_migration_period.jpg', // Example: Migration Period Spatha
                options: ['חרב ארוכה', 'גלדיוס', 'ספאטה'],
                correctAnswer: 'ספאטה',
                feedback: 'מעולה! זו ספאטה מתקופת נדידת העמים. רואים את המעבר מאורך הגלדיוס ללהב ארוך יותר וידית פשוטה יחסית.',
                 incorrectFeedback: 'כמעט! זו לא חרב ימי-ביניימית טיפוסית. זהו דוגמה מוקדמת יותר - ספאטה, ארוכה יותר מהגלדיוס אך לפני התפתחות החרבות הדו-ידניות.'
            },
             {
                image: '/assets/images/swords/longsword_two_handed.jpg', // Example: Another Longsword, clearly two-handed
                options: ['גלדיוס', 'חרב ארוכה', 'ספאטה'],
                correctAnswer: 'חרב ארוכה',
                feedback: 'בול פגיעה! זו חרב ארוכה קלאסית עם ידית ברורה לשתי ידיים ומוט שמירה ארוך וישר.',
                 incorrectFeedback: 'לא מדויק. אורך הידית והלהב מצביעים בבירור על חרב ארוכה מימי הביניים, לא על חרב קצרה יותר כמו הגלדיוס או הספאטה.'
            }
            // Add more questions if desired following the same structure, remember to replace image paths
            // For better "game-like" feel, aim for 8-10 questions minimum.
        ];

        let currentItemIndex = 0;
        let correctIdentifications = 0;
        let shuffledIdentificationData = [];

        function shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]]; // Swap elements
            }
            return array;
        }

        function startInteraction() {
             shuffledIdentificationData = shuffleArray([...identificationData]);
             currentItemIndex = 0;
             correctIdentifications = 0;

             summaryArea.classList.remove('visible');
             summaryArea.style.display = 'none';
             interactionArea.style.display = 'block';
             interactionArea.classList.remove('fade-out'); // Ensure it's not faded out
             interactionArea.classList.add('fade-in'); // Start faded in (handled by CSS transition initially)


             loadItem();
        }


        function loadItem() {
            if (currentItemIndex >= shuffledIdentificationData.length) {
                endInteraction();
                return;
            }

            const currentItem = shuffledIdentificationData[currentItemIndex];

            // Reset elements
            feedbackElement.textContent = ''; // Clear previous feedback
            feedbackElement.className = ''; // Clear feedback classes
            feedbackElement.classList.remove('visible'); // Hide feedback initially
            nextButton.style.display = 'none'; // Hide next button
            optionsContainer.innerHTML = ''; // Clear previous options

            // Fade out current image before loading new one (optional, can be jarring)
            // swordImage.style.opacity = 0;


            // Load new image
            swordImage.src = currentItem.image;
             // Add fade-in effect for the new image
            swordImage.style.opacity = 0; // Start transparent
            swordImage.onload = () => { // Fade in when loaded
                 swordImage.style.opacity = 1;
             };
             swordImage.onerror = () => {
                 console.error("Failed to load image: " + currentItem.image);
                 // Optionally load a placeholder or skip the item
             };


            questionText.textContent = 'איזו חרב זו?'; // Reset question text if needed

            // Shuffle options and create buttons
            const shuffledOptions = shuffleArray([...currentItem.options]);

            shuffledOptions.forEach(option => {
                const button = document.createElement('button');
                button.textContent = option;
                button.classList.add('option-button'); // Add a class for easier targeting
                button.addEventListener('click', () => checkIdentification(button, option));
                optionsContainer.appendChild(button);
            });

            updateProgress();
        }

        function checkIdentification(selectedButton, selectedOption) {
            const currentItem = shuffledIdentificationData[currentItemIndex];
            const buttons = optionsContainer.querySelectorAll('button');

            // Disable all buttons after an answer is selected
            buttons.forEach(button => button.disabled = true);

            let feedbackText = '';
            let feedbackClass = '';
            let correctButton = null;

            buttons.forEach(button => {
                if (button.textContent === currentItem.correctAnswer) {
                    correctButton = button;
                }
            });


            if (selectedOption === currentItem.correctAnswer) {
                feedbackText = currentItem.feedback;
                feedbackClass = 'correct';
                correctIdentifications++;
                selectedButton.classList.add('selected-correct');
                 // Simple animation feedback on correct button (optional, CSS hover covers some)
                 // selectedButton.style.transform = 'scale(1.1)';
                 // setTimeout(() => selectedButton.style.transform = '', 300);

            } else {
                feedbackText = currentItem.incorrectFeedback;
                feedbackClass = 'incorrect';
                selectedButton.classList.add('selected-incorrect');
                 // Highlight the correct answer
                 if(correctButton) {
                     correctButton.classList.add('correct-answer');
                 }
            }

            feedbackElement.textContent = feedbackText;
            feedbackElement.className = feedbackClass; // Set color class
            feedbackElement.classList.add('visible'); // Make feedback visible with animation

            nextButton.style.display = 'block'; // Show the next button
        }

        function nextItem() {
            // Fade out interaction area before moving to next item or summary
            interactionArea.classList.remove('fade-in');
            interactionArea.classList.add('fade-out');

             // Wait for fade-out animation to complete before changing content
            setTimeout(() => {
                 currentItemIndex++;
                 if (currentItemIndex < shuffledIdentificationData.length) {
                     loadItem();
                     interactionArea.classList.remove('fade-out');
                     interactionArea.classList.add('fade-in');
                 } else {
                    endInteraction();
                 }
            }, 500); // Match this duration to the CSS transition duration
        }

        function endInteraction() {
            interactionArea.style.display = 'none';
            summaryArea.style.display = 'block'; // Make summary visible
             // Trigger summary fade-in animation
            setTimeout(() => { // Small delay to ensure display:block is processed
                 summaryArea.classList.add('visible');
            }, 50);


            finalScoreElement.textContent = `זיהית נכונה ${correctIdentifications} מתוך ${shuffledIdentificationData.length} חרבות.`;
            progressTracker.style.display = 'none'; // Hide progress tracker in summary
        }

        function updateProgress() {
             progressTracker.style.display = 'block';
             progressTracker.textContent = `שאלה ${currentItemIndex + 1} מתוך ${shuffledIdentificationData.length}`;
        }


        function toggleExplanation() {
            const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
            if (isHidden) {
                explanationSection.style.display = 'block';
                 // Trigger explanation fade-in
                setTimeout(() => { // Small delay
                    explanationSection.classList.add('visible');
                }, 50);

                explanationButton.textContent = 'הסתר הסבר מקיף על החרבות';
            } else {
                 // Trigger explanation fade-out
                explanationSection.classList.remove('visible');
                 // Hide after fade-out animation completes
                setTimeout(() => {
                    explanationSection.style.display = 'none';
                }, 800); // Match this duration to the CSS transition duration

                explanationButton.textContent = 'הצג הסבר מקיף על החרבות';
            }
        }

        // Event listeners
        nextButton.addEventListener('click', nextItem);
        explanationButton.addEventListener('click', toggleExplanation);
        restartButton.addEventListener('click', startInteraction);


        // Initial setup
        summaryArea.style.display = 'none'; // Ensure summary is hidden initially
        explanationSection.style.display = 'none'; // Ensure explanation is hidden initially
        startInteraction(); // Start the first item
    });
</script>