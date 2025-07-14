---
title: "הבלש הבוטני: זיהוי עצים לפי סימנים"
english_slug: botanical-detective-tree-identification-by-signs
category: "מדעי החיים / ביולוגיה"
tags: עצים, זיהוי, עלים, פירות, קליפה, בוטניקה, חידון, אינטראקטיבי
---
# הבלש הבוטני: זיהוי עצים לפי סימנים

יצאתם לטבע, ועיניכם נחו על עץ מסתורי שאינכם מכירים? האם אפשר לפענח את זהותו רק לפי המראה החיצוני שלו? בואו נצא למסע גילוי מרתק! גלו אילו סימנים בוטניים יהפכו אתכם לבלשים סביבתיים מיומנים ויעזרו לכם לזהות את העצים הפזורים בנוף.

<div id="tree-quiz-container">
    <div id="tree-quiz">
        <div id="challenge-images">
            <!-- Images will be loaded here by JavaScript -->
        </div>
        <p id="question-text"></p>
        <div id="answer-buttons">
            <!-- Answer buttons will be generated here by JavaScript -->
        </div>
        <div id="feedback-area">
            <p id="feedback"></p>
            <button id="next-challenge-button">האתגר הבא</button>
        </div>
        <p id="quiz-end-message"></p>
    </div>
</div>

<style>
    /* Import a nice font */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6; /* Soft background */
        direction: rtl; /* Ensure Hebrew is RTL */
        text-align: right;
    }

    #tree-quiz-container {
         max-width: 750px; /* Slightly wider container */
         margin: 30px auto; /* More margin */
         padding: 0;
         background: linear-gradient(to bottom, #eef2f1, #dce3e1); /* Subtle gradient */
         border-radius: 12px; /* More rounded corners */
         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Deeper shadow */
         overflow: hidden; /* Keep shadow and border contained */
         border: 1px solid #d3dce0;
    }

    #tree-quiz {
        padding: 30px; /* More internal padding */
        text-align: center; /* Centered content within */
    }

    h1 {
        color: #0056b3; /* Match explanation color */
        text-align: center;
        margin-bottom: 25px; /* More space below title */
    }

    .intro-text {
        font-size: 1.1em;
        margin-bottom: 30px;
        text-align: center; /* Center the intro text */
        color: #555;
    }


    #challenge-images {
        display: flex;
        justify-content: center;
        gap: 20px; /* Increased gap */
        margin-bottom: 25px;
        flex-wrap: wrap;
        min-height: 120px; /* Reserve space to prevent layout shifts */
    }

    #challenge-images img {
        max-width: 180px; /* Slightly larger images */
        max-height: 180px; /* Limit max height */
        width: auto;
        height: auto;
        border: 2px solid #d3dce0; /* Thicker border */
        border-radius: 8px; /* More rounded image corners */
        box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.1); /* Enhanced shadow */
        transition: transform 0.3s ease-in-out; /* Smooth hover effect */
        opacity: 0; /* Start hidden for fade-in animation */
        transform: scale(0.95); /* Start slightly smaller */
        animation: fadeInScale 0.6s ease forwards; /* Apply animation */
    }

     /* Delay animation for subsequent images */
    #challenge-images img:nth-child(1) { animation-delay: 0.1s; }
    #challenge-images img:nth-child(2) { animation-delay: 0.3s; }
    #challenge-images img:nth-child(3) { animation-delay: 0.5s; }


    @keyframes fadeInScale {
        to { opacity: 1; transform: scale(1); }
    }

    #challenge-images img:hover {
        transform: scale(1.05); /* Enlarge slightly on hover */
        border-color: #4a90e2; /* Highlight on hover */
    }

    #question-text {
        font-size: 1.3em; /* Larger question text */
        margin-bottom: 20px;
        color: #333;
        font-weight: bold;
    }

    #answer-buttons {
        display: flex;
        flex-direction: column;
        gap: 12px; /* Increased gap */
        margin-bottom: 20px;
    }

    #answer-buttons button {
        padding: 12px 20px; /* More padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none; /* No default border */
        border-radius: 6px; /* Slightly more rounded */
        background-color: #4a90e2; /* Primary blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle button shadow */
    }

    #answer-buttons button:hover:not(:disabled) {
        background-color: #357bd8; /* Darker blue on hover */
        transform: translateY(-1px); /* Lift effect on hover */
    }

     #answer-buttons button:active:not(:disabled) {
        transform: translateY(0); /* Press effect */
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    #answer-buttons button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }

    /* Styles for selected/correct/incorrect buttons */
    #answer-buttons button.selected {
         transform: scale(1.02); /* Slightly larger when selected */
         font-weight: bold;
    }

    #answer-buttons button.correct {
        background-color: #7ed321; /* Green for correct */
        color: white;
        box-shadow: 0 0 10px rgba(126, 211, 33, 0.5); /* Glow effect */
    }

    #answer-buttons button.incorrect {
        background-color: #d0021b; /* Red for incorrect */
        color: white;
        box-shadow: 0 0 10px rgba(208, 2, 27, 0.5); /* Glow effect */
    }


    #feedback-area {
        min-height: 3em; /* Reserve more space for feedback and button */
        margin-bottom: 20px;
        opacity: 0; /* Start hidden */
        transform: translateY(10px); /* Start slightly lower */
        transition: opacity 0.4s ease-out, transform 0.4s ease-out;
    }

    #feedback-area.visible {
        opacity: 1;
        transform: translateY(0);
    }


    #feedback {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 15px; /* Space below feedback */
        min-height: 1.5em; /* Reserve space */
    }

    .feedback-correct {
        color: #28a745; /* Darker green for text */
    }

    .feedback-incorrect {
        color: #dc3545; /* Darker red for text */
    }

    #next-challenge-button {
        padding: 12px 25px; /* More padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #28a745; /* Success green */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.4s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        display: none; /* Hidden by default */
        margin-top: 15px; /* Space above button */
    }

    #next-challenge-button:hover {
        background-color: #218838;
        transform: translateY(-1px);
    }

     #next-challenge-button:active {
        transform: translateY(0);
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    #quiz-end-message {
        font-size: 1.5em; /* Larger text */
        font-weight: bold;
        color: #0056b3; /* Matching title color */
        margin-top: 30px;
        display: none; /* Hidden by default */
        animation: scaleIn 0.5s ease forwards; /* Animation for end message */
    }

     @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }


    #explanation-toggle {
        display: block;
        margin: 30px auto; /* More margin */
        padding: 12px 25px; /* More padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #6c757d; /* Secondary grey */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
     #explanation-toggle:hover {
        background-color: #5a6268;
        transform: translateY(-1px);
     }
      #explanation-toggle:active {
        transform: translateY(0);
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
     }


    #explanation {
        max-width: 800px;
        margin: 30px auto;
        padding: 30px; /* More padding */
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #fff;
        line-height: 1.7; /* Increased line height */
        text-align: right;
        display: none; /* Hidden by default */
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start slightly lower */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out; /* Animation for reveal */
    }

    #explanation.visible {
         opacity: 1;
         transform: translateY(0);
    }

    #explanation h2 {
        color: #0056b3;
        border-bottom: 2px solid #0056b3;
        padding-bottom: 8px; /* More padding */
        margin-bottom: 20px; /* More margin */
        font-size: 1.6em;
    }

    #explanation h3 {
        color: #333;
        margin-top: 25px; /* More margin */
        margin-bottom: 12px; /* More margin */
        font-size: 1.3em;
    }

    #explanation p, #explanation ul {
         margin-bottom: 18px; /* More margin */
         font-size: 1.05em;
    }

    #explanation ul {
        padding-right: 25px; /* More padding for list items */
        list-style: disc;
    }
    #explanation li {
        margin-bottom: 10px; /* More space between list items */
    }

    /* Ensure RTL for specific elements if needed, though body RTL should handle most */
    #feedback, #quiz-end-message, #question-text {
        direction: rtl;
        text-align: center;
    }

</style>

<button id="explanation-toggle">הצג הסבר על זיהוי עצים</button>

<div id="explanation">
    <h2>הסבר: זיהוי עצים צעד אחר צעד</h2>

    <p>זיהוי עצים אינו רק משימה בוטנית מרתקת, אלא גם שער להבנת עולמנו הטבעי. עצים הם לב המערכת האקולוגית: הם מספקים מחסה, מזון, ומשפיעים עמוקות על הנוף והאקלים סביבנו. היכולת לזהות את שכנינו העציים מאפשרת לנו להתחבר עמוק יותר לטבע ולהעריך את העושר הביולוגי שמקיף אותנו.</p>

    <h3>סימני זיהוי קריטיים:</h3>

    <ul>
        <li>
            <strong>עלים:</strong> העלים הם לעיתים קרובות הרמז המיידי והברור ביותר. התבוננו היטב ב:
            <ul>
                <li><strong>צורה וגודל:</strong> האם העלה פשוט (עלה אחד על הפטוטרת) או מורכב (כמה עלים קטנים על פטוטרת אחת)? האם הוא דמוי מחט (כמו באורן), דמוי קשקש (כמו בברוש), מאונה (עם "אצבעות" כמו באלון), או בעל צורה אחרת? מה גודלו?</li>
                <li><strong>שוליים:</strong> האם שפת העלה חלקה לגמרי, משוננת (כמו מסור), משורית (שינון עדין), או גלונית?</li>
                <li><strong>עורקים:</strong> התבוננו במבנה העורקים הבולטים בעלה – האם הם מסועפים, מקבילים, או בעלי תבנית ייחודית אחרת?</li>
                <li><strong>סידור על הענף:</strong> איך העלים מסודרים? לסירוגין (אחד בכל מפרק, כל פעם מצד אחר), נגדית (זוג עלים זה מול זה בכל מפרק), או בדורים (קבוצת עלים מסודרים סביב המפרק)?</li>
            </ul>
        </li>
        <li>
            <strong>פירות וזרעים:</strong> אלו הם 'תעודת הזהות' של העץ ומופיעים בעונה מסוימת בשנה, אך הם מזהים חד משמעית.
            <ul>
                <li><strong>סוג הפרי:</strong> האם מדובר בבלוט (כמו באלון), אצטרובל (כמו באורן וברוש), ענבה, תרמיל (כמו בחרוב), בית גלעין (כמו בזית או שקד), תפוח, אגס ועוד רבים?</li>
                <li><strong>מראה:</strong> שימו לב לצבע, לגודל, למרקם ולמבנה הפנימי של הפרי או הזרע. הפרטים הקטנים האלה קריטיים!</li>
            </ul>
        </li>
        <li>
            <strong>קליפת הגזע:</strong> מרקם, צבע ותבנית ההתבקעות של הקליפה משתנים מאוד בין מינים שונים, ואף משתנים עם גיל העץ. קליפת עץ צעיר יכולה להיות שונה מאוד מקליפת אותו עץ בוגר.
            <ul>
                <li><strong>מרקם:</strong> האם הקליפה חלקה ומתוחה, מחוספסת, סדוקה עמוקות, מתקלפת ברצועות או פיסות, או בעלת תבנית ייחודית אחרת?</li>
                <li><strong>צבע:</strong> הגוונים יכולים לנוע בין אפור, חום, אדמדם, ירוק (אם מכוסה באצות או חזזיות), ואפילו לבן או צהבהב במינים מסוימים.</li>
                <li><strong>תבנית:</strong> שימו לב אם הסדקים או ההתבקעות הם לאורכיים, לרוחביים, יוצרים "ריבועים" קטנים או גדולים, או בעלי מראה רשת.</li>
            </ul>
        </li>
    </ul>

    <h3>רמזים נוספים לזיהוי:</h3>
    <p>בלש בוטני טוב משתמש בכל הכלים שברשותו. מעבר לסימנים העיקריים, חפשו גם את אלה:</p>
    <ul>
        <li><strong>פרחים:</strong> אם העץ פורח, צורת הפרח, צבעו, גודלו, מספר עלי הכותרת ועונת הפריחה הם סימנים חשובים.</li>
        <li><strong>ניצנים:</strong> במיוחד בחורף כשהעץ ערום מעליו, צורת הניצנים, צבעם וסידורם על הענף יכולים לחשוף את זהותו.</li>
        <li><strong>צורת שלד העץ:</strong> המבנה הכללי של העץ - האם הוא עגול, פירמידלי, מתפשט לרוחב, או זקוף וגבוה? גם צורת הענפים והתפצלותם ייחודית.</li>
        <li><strong>ריח:</strong> שפשפו עלה או חתיכת קליפה קטנה ורחרחו. למינים רבים (כמו אקליפטוס או אורן) יש ריח אופייני שיכול לסייע בזיהוי.</li>
        <li><strong>בית גידול:</strong> היכן העץ צומח? סוג הקרקע (חול, חרסית, סלע), כמות המים הזמינים (עץ ליד נחל מול עץ במדבר), והאזור הגאוגרפי או האקלים בו אתם נמצאים - כל אלה מצמצמים מאוד את רשימת המינים האפשריים.</li>
    </ul>

    <h3>דוגמאות להמחשה:</h3>
    <p>כדי לחדד את יכולות הזיהוי, בואו נראה איך הסימנים מתחברים במינים נפוצים:</p>
    <ul>
        <li><strong>אלון תבור/מצוי:</strong> עלים קשים, לרוב מאונים או משוננים עמוק. הפרי הוא הבלוט המוכר. קליפת הגזע מחוספסת מאוד ומחורצת בתבנית כמעט ריבועית.</li>
        <li><strong>אורן ירושלים:</strong> עלים דמויי מחטים ארוכות ודקות, המסודרות תמיד בזוגות. הפרי הוא אצטרובל עצי וקשיח. גזע בעל קליפה מתקלפת בפיסות לא סדירות בצבע אדמדם-חום, במיוחד בענפים צעירים.</li>
        <li><strong>זית אירופי:</strong> עלים קטנים, צרים, דמויי רומח, ירוקים כהים ממעלה וכסופים בהירים מתחת, מסודרים נגדית. הפרי הוא בית גלעין (הזית). גזע צעיר חלק יחסית, אך עם הגיל הופך מפותל, מחורץ ומחוספס באופן דרמטי.</li>
    </ul>

    <h3>משאבים נוספים לבלש המתחיל:</h3>
    <p>אל תהססו להיעזר בכלים חיצוניים:</p>
    <ul>
        <li><strong>מדריכי שדה:</strong> ספרים או חוברות המתמקדים בצמחים ועצים ספציפיים לאזור הגיאוגרפי שלכם הם כלי עזר קלאסי ויעיל.</li>
        <li><strong>אפליקציות זיהוי:</strong> קיימות אפליקציות נהדרות לטלפון המאפשרות לצלם עלה, פרח, פרי או קליפה ולקבל הצעות לזיהוי מהקהילה או ממנועי זיהוי ויזואליים (לדוגמה, iNaturalist, PictureThis, PlantNet).</li>
        <li><strong>מומחים וחובבים:</strong> צאו לסיורים מודרכים, הצטרפו לקבוצות טיול בטבע, או התייעצו עם אנשי מקצוע ומומחים מקומיים. הידע והניסיון שלהם יסייעו לכם רבות.</li>
    </ul>

    <p>תרגול, התבוננות סבלנית וסקרנות הם המפתחות לזיהוי מוצלח. בהצלחה במסע הגילוי הבוטני שלכם!</p>
</div>

<script>
    const quizData = [
        {
            images: ['https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Quercus_calliprinos_leaves.jpg/320px-Quercus_calliprinos_leaves.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Quercus_ithaburensis_acorn_at_Alon_Hagilboa.jpg/320px-Quercus_ithaburensis_acorn_at_Alon_Hagilboa.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Quercus_calliprinos_trunk.JPG/320px-Quercus_calliprinos_trunk.JPG'],
            question: 'איזה עץ מסתתר מאחורי העלים המשוננים, הבלוט המוכר והגזע המחוספס?',
            options: ['אורן', 'אלון', 'ברוש', 'זית'],
            correctAnswer: 'אלון',
            correctFeedback: 'מעולה! זיהוי מדויק. אלו אכן סימני ההיכר של עץ האלון (כמו אלון מצוי או תבור).',
            incorrectFeedback: {
                'אורן': 'לא נכון. לאורן יש עלים דמויי מחטים ואצטרובלים קוצניים, לא בלוטים חלקים ומעוגלים.',
                'ברוש': 'זה לא ברוש. הברוש הוא עץ מחטני ובעל מבנה גזע ופירות שונים לגמרי.',
                'זית': 'זה לא זית. עץ הזית מתאפיין בעלים קטנים יותר, פירות קטנים בצורת זיתים, ובגזע מפותל מאוד עם הגיל.'
            }
        },
        {
            images: ['https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Pinus_halepensis_leaves.jpg/320px-Pinus_halepensis_leaves.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Pinus_halepensis_cone.jpg/320px-Pinus_halepensis_cone.jpg'],
            question: 'המחטים הארוכות והאצטרובל הקשיח לא משאירים הרבה מקום לספק... איזה עץ פגשתם?',
            options: ['אלון', 'אקליפטוס', 'אורן', 'חרוב'],
            correctAnswer: 'אורן',
            correctFeedback: 'בינגו! אלו סימנים מובהקים של עץ האורן, שממלא את היערות שלנו (למשל, אורן ירושלים).',
            incorrectFeedback: {
                'אלון': 'לא מדויק. לאלון יש עלים רחבים (לרוב מאונים) ופירות בצורת בלוטים.',
                'אקליפטוס': 'זה לא אקליפטוס. לאקליפטוס עלים בצורת ביצה ופירות קטנים דמויי קופסה.',
                'חרוב': 'לא חרוב. לחרוב עלים מורכבים ופירות שהם תרמילים ארוכים ומתוקים.'
            }
        },
         {
            images: ['https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Olea_europaea_leaves.jpg/320px-Olea_europaea_leaves.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Olive_fruit.jpg/320px-Olive_fruit.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Olea_europaea_trunk_2.jpg/320px-Olea_europaea_trunk_2.jpg'],
            question: 'עלים קטנים בצבע ירוק-כסוף, פרי מוארך ומוכר וגזע עתיק ומפותל... מי זה?',
            options: ['ברוש', 'אלה', 'שקד', 'זית'],
            correctAnswer: 'זית',
            correctFeedback: 'נכון מאוד! כל הסימנים האלה מובילים היישר לעץ הזית, סמל לנוף הים תיכוני.',
            incorrectFeedback: {
                'ברוש': 'הברוש הוא עץ מחטני בעל מראה שונה לחלוטין.',
                'אלה': 'לא אלה. לאלה עלים מורכבים, והפירות שלה קטנים ואדומים או שחורים, לא זיתים.',
                'שקד': 'זה לא שקד. לעץ השקד עלים ארוכים יותר, והפרי שלו הוא קליפה קשה המכילה את השקד שאנו מכירים.'
            }
        }
        // Add more challenges here
    ];

    let currentChallengeIndex = 0;
    const treeQuizDiv = document.getElementById('tree-quiz'); // Use the inner container for transitions
    const challengeImagesDiv = document.getElementById('challenge-images');
    const questionTextP = document.getElementById('question-text');
    const answerButtonsDiv = document.getElementById('answer-buttons');
    const feedbackP = document.getElementById('feedback');
    const feedbackAreaDiv = document.getElementById('feedback-area'); // Wrapper for feedback and next button
    const nextButton = document.getElementById('next-challenge-button');
    const quizEndMessageP = document.getElementById('quiz-end-message');
    const explanationToggleBtn = document.getElementById('explanation-toggle');
    const explanationDiv = document.getElementById('explanation');

    function loadChallenge() {
        if (currentChallengeIndex >= quizData.length) {
            endQuiz();
            return;
        }

        const challenge = quizData[currentChallengeIndex];

        // Clear previous challenge and reset states
        // Use a transition for smooth loading
        treeQuizDiv.style.opacity = 0;
        treeQuizDiv.style.transform = 'translateY(20px)';

        setTimeout(() => {
            challengeImagesDiv.innerHTML = '';
            answerButtonsDiv.innerHTML = '';
            feedbackP.textContent = '';
            feedbackP.className = ''; // Clear feedback class
            feedbackAreaDiv.classList.remove('visible');
            nextButton.style.display = 'none';
            quizEndMessageP.style.display = 'none';
             quizEndMessageP.classList.remove('visible'); // Remove animation class
             nextButton.classList.remove('visible'); // Remove animation class

            // Load images
            challenge.images.forEach(imageUrl => {
                const img = document.createElement('img');
                img.src = imageUrl;
                img.alt = 'מאפיין של עץ'; // Alt text for accessibility
                // Image fade-in animation handled by CSS on load
                challengeImagesDiv.appendChild(img);
            });

            // Set question text
            questionTextP.textContent = challenge.question;

            // Create answer buttons
            challenge.options.forEach(option => {
                const button = document.createElement('button');
                button.textContent = option;
                button.addEventListener('click', () => checkAnswer(button, option)); // Pass button element
                answerButtonsDiv.appendChild(button);
            });

            // Re-enable buttons (they should be disabled by checkAnswer in prev round)
            setButtonsState(false);

            // Animate in the new challenge content
             treeQuizDiv.style.opacity = 1;
             treeQuizDiv.style.transform = 'translateY(0)';

        }, 400); // Match the fade-out transition duration
    }

    function checkAnswer(selectedButton, selectedAnswer) {
        const challenge = quizData[currentChallengeIndex];
        setButtonsState(true); // Disable all buttons after selection

        // Add a class to the selected button immediately
        selectedButton.classList.add('selected');


        if (selectedAnswer === challenge.correctAnswer) {
            feedbackP.textContent = challenge.correctFeedback;
            feedbackP.className = 'feedback-correct';
            selectedButton.classList.add('correct');
        } else {
            feedbackP.textContent = challenge.incorrectFeedback[selectedAnswer] || `תשובה שגויה. התשובה הנכונה היא: ${challenge.correctAnswer}.`;
            feedbackP.className = 'feedback-incorrect';
            selectedButton.classList.add('incorrect');

             // Find and highlight the correct button
            const buttons = answerButtonsDiv.querySelectorAll('button');
            buttons.forEach(button => {
                if (button.textContent === challenge.correctAnswer) {
                    button.classList.add('correct'); // Highlight the correct answer
                }
            });
        }

         // Animate feedback area visibility
        feedbackAreaDiv.classList.add('visible');
        // Delay showing the next button slightly after feedback appears
        setTimeout(() => {
             nextButton.style.display = 'block'; // Show the button
             // Add a class to trigger CSS animation for the button itself if needed
        }, 300); // Small delay
    }

    function setButtonsState(disabled) {
        const buttons = answerButtonsDiv.querySelectorAll('button');
        buttons.forEach(button => {
            button.disabled = disabled;
            // Optional: remove state classes when re-enabling for next round
            if (!disabled) {
                 button.classList.remove('selected', 'correct', 'incorrect');
            }
        });
    }

    function nextChallenge() {
        currentChallengeIndex++;
        loadChallenge();
    }

    function endQuiz() {
         // Animate fade out current quiz content
        treeQuizDiv.style.opacity = 0;
        treeQuizDiv.style.transform = 'translateY(20px)';

        setTimeout(() => {
            challengeImagesDiv.innerHTML = '';
            questionTextP.textContent = '';
            answerButtonsDiv.innerHTML = '';
            feedbackP.textContent = '';
            feedbackAreaDiv.classList.remove('visible');
            nextButton.style.display = 'none';
            nextButton.classList.remove('visible'); // Remove animation class


            quizEndMessageP.textContent = 'סיימת את כל האתגרים! בלש בוטני מצטיין!';
            quizEndMessageP.style.display = 'block';
            quizEndMessageP.classList.add('visible'); // Trigger animation


            // Animate in the end message container
             treeQuizDiv.style.opacity = 1;
             treeQuizDiv.style.transform = 'translateY(0)';

        }, 400); // Match fade-out duration
    }

    // Event listener for the "Next Challenge" button
    nextButton.addEventListener('click', nextChallenge);

    // Event listener for the "Show Explanation" button
    explanationToggleBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            // Use a small delay to allow display:block to apply before animating
            setTimeout(() => {
                 explanationDiv.classList.add('visible');
            }, 10);
            explanationToggleBtn.textContent = 'הסתר הסבר על זיהוי עצים';
        } else {
            explanationDiv.classList.remove('visible');
            // Hide after the animation finishes
            setTimeout(() => {
                 explanationDiv.style.display = 'none';
            }, 500); // Match CSS transition duration
            explanationToggleBtn.textContent = 'הצג הסבר על זיהוי עצים';
        }
    });


    // Initial load
    loadChallenge();

</script>
```