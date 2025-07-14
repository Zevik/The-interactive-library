---
title: "האם תזהה את החתימה? מסע בעקבות ציירים גדולים"
english_slug: can-you-recognize-the-signature-a-journey-following-great-painters
category: "אמנות ועיצוב / תולדות האמנות"
tags: [אמנות, ציירים, חתימות, זיהוי, אמנים מפורסמים]
---
<h1>האם תזהה את החתימה? מסע בעקבות ציירים גדולים</h1>
<p>ראיתם פעם חתימה קטנה, כמעט נסתרת, בפינה של ציור במוזיאון? האם ידעתם שחתימות של אמנים הן לעיתים קרובות ייחודיות כמו טביעת אצבע, ומספרות סיפור על האמן, התקופה, ואף על תהליך היצירה? האם אתם מסוגלים לזהות צייר רק על פי הדרך שבה חתם את שמו? בואו נצא למסע מרתק לגלות!</p>

<div id="signature-quiz-app" class="quiz-app-container">
    <!-- Start Screen -->
    <div id="quiz-start-screen" class="screen">
        <h2>ברוכים הבאים למסע בעקבות חתימות אמנים!</h2>
        <p>האם עינכם חדה מספיק כדי לזהות את הצייר מאחורי החתימה?</p>
        <button id="start-quiz-button" class="app-button primary">התחילו את המסע</button>
    </div>

    <!-- Question Screen -->
    <div id="quiz-question-screen" class="screen" style="display: none;">
        <div class="quiz-header">
            <div id="question-counter">שאלה <span id="current-q">1</span> מתוך <span id="total-q"></span></div>
            <div id="score-counter">ניקוד: <span id="current-score">0</span></div>
        </div>
        <div class="question-container">
            <p>לפניכם חתימה של צייר מפורסם. מי הוא?</p>
            <div class="signature-image-container">
                <img id="signature-image" src="" alt="חתימת אמן" class="signature-image">
            </div>
            <div id="artist-choices" class="choices-container">
                <!-- Buttons will be added here by JS -->
            </div>
            <div id="feedback" class="feedback-container"></div>
        </div>

        <div id="result-container" class="result-container" style="display: none;">
            <h3>פרטי התשובה והיצירה</h3>
            <div class="artwork-details">
                <div class="artwork-image-container">
                    <img id="artwork-image" src="" alt="יצירת האמנות המלאה" class="artwork-image">
                </div>
                <div class="artwork-info">
                    <h4 id="artwork-title"></h4>
                    <p><strong id="artist-name-result"></strong></p>
                    <p id="artist-info"></p>
                </div>
            </div>
            <button id="next-question-button" class="app-button secondary">לשאלה הבאה</button>
        </div>
    </div>

    <!-- End Screen -->
    <div id="quiz-end-screen" class="screen" style="display: none;">
        <h2>המסע הסתיים!</h2>
        <p>סיימתם את החידון בהצלחה.</p>
        <p>הניקוד הסופי שלכם: <span id="final-score"></span> מתוך <span id="total-q-end"></span></p>
        <button id="restart-quiz-button" class="app-button primary">התחילו מחדש</button>
    </div>

</div>

<button id="toggle-explanation" class="toggle-button">הצג הסבר על חתימות באמנות</button>

<div id="explanation-content" class="explanation-content" style="display: none;">
    <h2>הסבר: חתימות באמנות - יותר מחתימה פשוטה</h2>

    <h3>מהי חתימה אמנותית ומדוע היא כה חשובה?</h3>
    <p>חתימה של אמן על יצירתו היא הרבה יותר מחתימה פשוטה על מסמך. היא משמשת לזיהוי חד-משמעי של יוצר היצירה, מתעדת את סיומה ואותנטיותה, ומהווה הוכחה לקניין רוחני. במובנים רבים, היא החותם האישי של האמן, שמבטיח את הקשר בינו לבין עבודתו.</p>

    <h3>התפתחות החתימה לאורך ההיסטוריה של האמנות:</h3>
    <p>בעבר, אמנים לא תמיד חתמו על יצירותיהם, או השתמשו בסימנים פשוטים או מונוגרמות. עם התפתחות מעמד האמן וצמיחת שוק האמנות, החתימה הפכה נפוצה יותר ויותר, ונעשתה מורכבת ואישית יותר, לעיתים קרובות כוללת את השם המלא, ראשי תיבות, ואף תאריך. החתימה התפתחה מסימן פשוט לחותם אישי בעל משמעות.</p>

    <h3>חתימה כחלק מהיצירה:</h3>
    <p>לפעמים החתימה היא רק סימון קטן בפינה, כמעט בלתי נראה. אולם, ישנם מקרים בהם האמן משלב את חתימתו באופן יצירתי כחלק אינטגרלי מהקומפוזיציה, הופך אותה לאלמנט ויזואלי חשוב בפני עצמו, או אפילו משתמש בה כחלק מסיפור או סמל בתוך הציור. החתימה יכולה להיות נסתרת או בולטת, עדינה או דומיננטית, תמיד עם מטרה אמנותית או אישית.</p>

    <h3>סגנונות חתימה שונים:</h3>
    <p>סגנון החתימה יכול לשקף רבות על האמן ועל התקופה. חתימות פורמליות ומסודרות לעומת חתימות סוערות ודינמיות; חתימות קריאות לעומת כאלה המזכירות סמל או לוגו. הסגנון יכול להשתנות גם לאורך הקריירה של האמן, בהתאם להתפתחותו האמנותית או אפילו למצבו הפיזי. ניתוח סגנון החתימה מספק צוהר נוסף לאישיותו של האמן ולמסעו האמנותי.</p>

    <h3>אתגרי זיהוי ואותנטיקציה:</h3>
    <p>זיהוי חתימה הוא כלי חשוב, אך לא יחיד, באותנטיקציה של יצירת אמנות. זיופים הם אתגר גדול, ואספנים ומומחים בודקים לא רק את הדמיון החזותי לחתימות ידועות, אלא גם את הטכניקה, החומרים, וההקשר ההיסטורי. חשוב לזכור שחתימתו של אמן עשויה להשתנות לאורך שנות יצירתו, מה שמחייב בחינה מעמיקה ומקיפה. אותנטיקציה היא תהליך מורכב המשלב מומחיות היסטורית, טכנית וויזואלית.</p>

    <h3>סיפורים ודוגמאות בולטות:</h3>
    <p>ציירים רבים הפכו את חתימתם לאייקונית. כך למשל חתימתו המפותלת והייחודית של סלבדור דאלי, או חתימתו המשתנה של פבלו פיקאסו, או אופן החתימה של רמברנדט ששיקף שינויים בתפיסתו העצמית ובמעמדו. כל חתימה כזו נושאת סיפור ומגלה פרט נוסף על האמן והיצירה. החתימה הופכת לחלק מהנרטיב ההיסטורי של האמנות.</p>
</div>

<style>
    /* --- Variables and Base Styles --- */
    :root {
        --primary-color: #0d47a1; /* Deep Blue */
        --primary-dark: #073070;
        --secondary-color: #ff6f00; /* Vibrant Orange */
        --correct-color: #388e3c; /* Green */
        --wrong-color: #d32f2f; /* Red */
        --border-color: #e0e0e0; /* Light Grey */
        --bg-color: #f5f5f5; /* Off White */
        --card-bg: #ffffff; /* White */
        --text-color: #212121; /* Dark Grey */
        --button-text-color: #ffffff;
        --transition-speed: 0.4s;
    }

    body {
        font-family: 'Arial', sans-serif; /* Keep standard system font for compatibility */
        line-height: 1.6;
        direction: rtl;
        text-align: right;
        background-color: var(--bg-color);
        color: var(--text-color);
        padding: 20px;
        max-width: 800px;
        margin: 0 auto;
        overflow-x: hidden; /* Prevent horizontal scroll from animations */
    }

    h1, h2, h3, h4 {
        color: var(--primary-dark);
        text-align: center;
        margin-bottom: 20px;
    }

    p {
        margin-bottom: 15px;
    }

    /* --- Quiz App Structure --- */
    .quiz-app-container {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 30px 20px; /* More padding */
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* More pronounced shadow */
        position: relative; /* For screen transitions */
        overflow: hidden; /* Hide screens not in view */
    }

    .screen {
        /* Basic screen styling */
        width: 100%;
        opacity: 0; /* Start hidden */
        transition: opacity var(--transition-speed) ease-in-out;
    }

    .screen.fade-in {
        opacity: 1;
    }


    /* --- Start/End Screen Styles --- */
    #quiz-start-screen, #quiz-end-screen {
        text-align: center;
    }

    #quiz-start-screen h2, #quiz-end-screen h2 {
         margin-bottom: 15px;
    }
     #quiz-start-screen p, #quiz-end-screen p {
         font-size: 1.1em;
         margin-bottom: 25px;
     }

    /* --- Quiz Header (Score/Counter) --- */
    .quiz-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        font-size: 1em;
        color: #555;
        padding-bottom: 15px;
        border-bottom: 1px dashed var(--border-color);
    }

    #question-counter, #score-counter {
        font-weight: bold;
    }

    /* --- Question Area Styles --- */
    .question-container p {
        text-align: center;
        font-size: 1.15em; /* Slightly larger font */
        margin-bottom: 25px; /* More space */
        font-weight: bold;
    }

    .signature-image-container {
        text-align: center;
        margin-bottom: 30px; /* More space */
        min-height: 120px; /* Ensure space */
        display: flex;
        justify-content: center;
        align-items: center; /* Center vertically */
    }

    .signature-image {
        max-width: 90%; /* Slightly smaller */
        max-height: 150px; /* Limit max height */
        height: auto;
        border: 1px solid var(--border-color);
        padding: 8px; /* More padding */
        background-color: #fff;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); /* Subtle shadow */
        transition: transform var(--transition-speed) ease-in-out, opacity var(--transition-speed) ease-in-out; /* Animation */
        opacity: 0; /* Start hidden */
    }

     .signature-image.loaded {
         opacity: 1;
      }


    /* --- Choices Container and Buttons --- */
    .choices-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px; /* More space between buttons */
        margin-bottom: 25px; /* More space */
         opacity: 0; /* Start hidden */
         transition: opacity var(--transition-speed) ease-in-out;
    }

     .choices-container.slide-up {
        opacity: 1;
        animation: slideUp var(--transition-speed) ease forwards;
     }


    /* Base button style */
    .app-button {
         border: none;
         border-radius: 8px; /* More rounded corners */
         padding: 12px 20px; /* More padding */
         font-size: 1em;
         cursor: pointer;
         transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
         min-width: 120px;
         text-align: center;
         font-weight: bold;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .app-button.primary {
        background-color: var(--primary-color);
        color: var(--button-text-color);
    }
     .app-button.primary:hover:not(:disabled) {
        background-color: var(--primary-dark);
        box-shadow: 0 3px 8px rgba(0,0,0,0.15);
     }

    .app-button.secondary {
        background-color: #6c757d;
        color: var(--button-text-color);
    }
     .app-button.secondary:hover:not(:disabled) {
        background-color: #5a6268;
        box-shadow: 0 3px 8px rgba(0,0,0,0.15);
     }

     .choices-container button.app-button {
         background-color: #e0e0e0; /* Light grey for default choice */
         color: var(--text-color);
         box-shadow: none; /* Less shadow on choices */
         transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease, opacity 0.3s ease; /* Add opacity transition */
     }
      .choices-container button.app-button:hover:not(:disabled) {
         background-color: #d5d5d5;
         transform: translateY(-2px); /* Lift effect */
      }

    .choices-container button:disabled {
        opacity: 0.6; /* Dim disabled buttons */
        cursor: default;
        box-shadow: none;
        transform: none;
    }

    .choices-container button.correct-answer {
         background-color: var(--correct-color) !important; /* Override other styles */
         color: var(--button-text-color) !important;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
         animation: pulse 0.5s ease forwards; /* Animation */
    }

     .choices-container button.wrong-answer {
         background-color: var(--wrong-color) !important; /* Override other styles */
         color: var(--button-text-color) !important;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
         animation: shake 0.5s ease forwards; /* Animation */
     }

    /* --- Feedback Area --- */
    .feedback-container {
        text-align: center;
        margin-top: 15px;
        font-weight: bold;
        min-height: 1.5em; /* Reserve more space */
        font-size: 1.1em;
        padding: 10px;
        border-radius: 5px;
        opacity: 0; /* Start hidden */
        transition: opacity var(--transition-speed) ease-in-out;
    }

    .feedback-container.fade-in {
        opacity: 1;
    }


    .feedback-correct {
        color: var(--correct-color);
        background-color: #e8f5e9; /* Light green background */
    }

    .feedback-wrong {
        color: var(--wrong-color);
        background-color: #ffebee; /* Light red background */
    }

    /* --- Result Container --- */
    .result-container {
        border-top: 1px dashed var(--border-color);
        padding-top: 25px; /* More padding */
        margin-top: 25px; /* More margin */
        opacity: 0; /* Start hidden */
        transition: opacity var(--transition-speed) ease-in-out;
    }
     .result-container.visible {
         opacity: 1;
     }

    .artwork-details {
        display: flex;
        flex-direction: column;
        gap: 25px; /* More space */
        margin-bottom: 25px; /* More space */
    }

     @media (min-width: 600px) {
        .artwork-details {
            flex-direction: row;
        }
        .artwork-image-container {
            flex: 1;
            min-width: 150px; /* Ensure image container has size */
            text-align: right; /* RTL adjustment */
        }
        .artwork-info {
            flex: 2;
        }
    }

    .artwork-image-container {
        text-align: center;
    }

    .artwork-image {
        max-width: 100%;
        height: auto;
        max-height: 250px; /* Limit artwork image height */
        border: 1px solid var(--border-color);
        padding: 8px;
        background-color: #fff;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
         opacity: 0; /* Start hidden */
         transition: opacity var(--transition-speed) ease-in-out;
    }
     .artwork-image.loaded {
         opacity: 1;
      }


    .artwork-info h4 {
        text-align: right;
        margin-top: 0;
        margin-bottom: 10px;
         color: var(--primary-color);
    }
     .artwork-info p {
         text-align: right;
         margin-bottom: 8px; /* Slightly less margin */
         font-size: 0.95em;
         color: #444;
     }
    .artwork-info strong {
        color: var(--primary-dark);
    }


    .next-button.app-button {
        display: block;
        width: 100%;
    }


    /* --- Explanation Section --- */
    .toggle-button {
        display: block;
        width: 100%;
        background-color: #607d8b; /* Blue Grey */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 15px;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .toggle-button:hover {
        background-color: #546e7a;
        box-shadow: 0 3px 8px rgba(0,0,0,0.15);
    }

    .explanation-content {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        opacity: 0; /* Start hidden */
        transition: opacity var(--transition-speed) ease-in-out;
    }
     .explanation-content.fade-in {
        opacity: 1;
     }


     .explanation-content h3 {
        text-align: right;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
         color: var(--primary-color);
     }
     .explanation-content p {
        text-align: right;
        margin-bottom: 15px;
        color: #444;
     }

     /* --- Animations --- */
     @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
     }

     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.02); }
         100% { transform: scale(1); }
     }

     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }

     @keyframes slideUp {
         from { transform: translateY(20px); opacity: 0; }
         to { transform: translateY(0); opacity: 1; }
     }


</style>

<script>
    const questions = [
        {
            signature: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Signature_of_Pablo_Picasso.svg/320px-Signature_of_Pablo_Picasso.svg.png',
            correctArtist: 'פבלו פיקאסו',
            options: ['סלבדור דאלי', 'אנרי מאטיס', 'מארק שאגאל', 'פבלו פיקאסו'],
            artwork: {
                image: 'https://upload.wikimedia.org/wikipedia/he/thumb/4/4c/PicassoGuernica.jpg/500px-PicassoGuernica.jpg',
                title: 'גרניקה',
                artistInfo: 'פבלו פיקאסו (1881–1973) היה אמן ספרדי, הנחשב לאחד האמנים המשפיעים ביותר במאה ה-20. הוא היה ממייסדי התנועה הקוביסטית ונודע בזכות הרבגוניות והפרודוקטיביות שלו.'
            }
        },
        {
            signature: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Signature_of_Vincent_van_Gogh.svg/320px-Signature_of_Vincent_van_Gogh.svg.png',
            correctArtist: 'וינסנט ואן גוך',
            options: ['קלוד מונה', 'פייר-אוגוסט רנואר', 'פול סזאן', 'וינסנט ואן גוך'],
            artwork: {
                image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/450px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg',
                title: 'ליל כוכבים',
                artistInfo: 'וינסנט ואן גוך (1853–1890) היה צייר הולנדי פוסט-אימפרסיוניסטי, שנחשב לאחד מגדולי האמנים בהיסטוריה. עבודותיו מאופיינות בצבעוניות עזה ומשיכות מכחול אקספרסיביות.'
            }
        },
         {
            signature: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Signature_of_Rembrandt.svg/320px-Signature_of_Rembrandt.svg.png',
            correctArtist: 'רמברנדט ואן ריין',
            options: ['יוהנס ורמיר', 'פרנס האלס', 'פיטר פול רובנס', 'רמברנדט ואן ריין'],
            artwork: {
                image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/The_Night_Watch_-_MD.jpg/500px-The_Night_Watch_-_MD.jpg',
                title: 'משמר הלילה',
                artistInfo: 'רמברנדט ואן ריין (1606–1669) היה צייר, רשם ואמן הדפסים הולנדי, נחשב לאחד מגדולי האמנים בתולדות אירופה ובייחוד בהולנד. יצירותיו נודעות בשל הדרמה, השימוש באור-צל והעומק הרגשי.'
            }
        },
         {
            signature: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Salvador_Dal%C3%AD_signature.svg/320px-Salvador_Dal%C3%AD_signature.svg.png',
            correctArtist: 'סלבדור דאלי',
            options: ['רנה מגריט', 'מקס ארנסט', 'חואן מירו', 'סלבדור דאלי'],
            artwork: {
                image: 'https://upload.wikimedia.org/wikipedia/en/thumb/d/dd/The_Persistence_of_Memory.jpg/400px-The_Persistence_of_Memory.jpg',
                title: 'התמדתו של זיכרון',
                artistInfo: 'סלבדור דאלי (1904–1989) היה צייר סוריאליסטי ספרדי, מהבולטים והידועים שבאמני הזרם. נודע בזכות עבודותיו הדמיוניות והמוזרות ואישיותו האקסצנטרית.'
            }
        },
         {
            signature: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Michelangelo%27s_signature.svg/320px-Michelangelo%27s_signature.svg.png',
            correctArtist: 'מיכלאנג\'לו',
            options: ['לאונרדו דה וינצ\'י', 'רפאל סאנציו', 'דונטלו', 'מיכלאנג\'לו'],
            artwork: {
                image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Michelangelo%27s_Pieta_5409_cut_square.jpg/400px-Michelangelo%27s_Pieta_5409_cut_square.jpg',
                title: 'פייטה',
                artistInfo: 'מיכלאנג\'לו (1475–1564) היה פסל, צייר, אדריכל ומשורר איטלקי בן תקופת הרנסאנס, הנחשב לאחד מגדולי האמנים בכל הזמנים. "פייטה" היא יצירת הפיסול היחידה שחתם עליה.'
            }
        }
        // Add more high-quality questions here
    ];

    let currentQuestionIndex = 0;
    let score = 0;

    // DOM Elements
    const quizStartScreen = document.getElementById('quiz-start-screen');
    const quizQuestionScreen = document.getElementById('quiz-question-screen');
    const quizEndScreen = document.getElementById('quiz-end-screen');

    const startQuizButton = document.getElementById('start-quiz-button');
    const restartQuizButton = document.getElementById('restart-quiz-button');

    const questionCounterSpan = document.getElementById('current-q');
    const totalQuestionSpan = document.getElementById('total-q');
    const scoreCounterSpan = document.getElementById('current-score');
    const signatureImage = document.getElementById('signature-image');
    const artistChoicesDiv = document.getElementById('artist-choices');
    const feedbackDiv = document.getElementById('feedback');
    const resultContainer = document.getElementById('result-container');
    const artworkImage = document.getElementById('artwork-image');
    const artworkTitle = document.getElementById('artwork-title');
    const artistNameResult = document.getElementById('artist-name-result');
    const artistInfoPara = document.getElementById('artist-info');
    const nextButton = document.getElementById('next-question-button');
    const finalScoreSpan = document.getElementById('final-score');
    const totalQEndSpan = document.getElementById('total-q-end');

    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationContentDiv = document.getElementById('explanation-content');

     // Get CSS transition duration
    const style = getComputedStyle(document.documentElement);
    const transitionSpeedMs = parseFloat(style.getPropertyValue('--transition-speed')) * 1000;


    // --- State Management ---
    function showScreen(screenToShow) {
        const screens = [quizStartScreen, quizQuestionScreen, quizEndScreen];
        screens.forEach(screen => {
            screen.classList.remove('fade-in');
        });

        // Hide all first (with a slight delay to allow transitions to start if needed)
        setTimeout(() => {
             screens.forEach(screen => { screen.style.display = 'none'; });
             // Then show the desired screen
             screenToShow.style.display = 'block';
             // Add fade-in class after display is block
             setTimeout(() => { screenToShow.classList.add('fade-in'); }, 50); // Small delay for CSS display change

        }, transitionSpeedMs); // Hide after transition out
    }


    // --- Quiz Logic ---
    function startQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        totalQuestionSpan.textContent = questions.length;
        totalQEndSpan.textContent = questions.length;
        scoreCounterSpan.textContent = score;
        showScreen(quizQuestionScreen);
        loadQuestion();
    }

    function loadQuestion() {
        if (currentQuestionIndex >= questions.length) {
            endQuiz();
            return;
        }

        const question = questions[currentQuestionIndex];

        // Reset state and classes
        questionCounterSpan.textContent = currentQuestionIndex + 1;
        artistChoicesDiv.innerHTML = '';
        feedbackDiv.textContent = '';
        feedbackDiv.className = 'feedback-container'; // Reset feedback classes
        resultContainer.classList.remove('visible'); // Hide result with transition

         // Hide elements that will fade/slide in for the new question
         signatureImage.classList.remove('loaded');
         artistChoicesDiv.classList.remove('slide-up');
         resultContainer.style.display = 'none';


        // Image loading with animation
        signatureImage.onload = () => {
             signatureImage.classList.add('loaded');
             // Add slide-up animation to choices after image loads
             artistChoicesDiv.classList.add('slide-up');
        };
         signatureImage.onerror = () => {
             // Handle image loading errors visually if needed
             signatureImage.classList.add('loaded'); // Still show something even if broken? Or a placeholder?
             signatureImage.alt = "Failed to load signature image"; // Improve alt text on error
              // Still add slide-up animation even if image fails
              artistChoicesDiv.classList.add('slide-up');
         };
        signatureImage.src = question.signature;


        // Shuffle options
        const shuffledOptions = [...question.options].sort(() => Math.random() - 0.5);

        shuffledOptions.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option;
            button.classList.add('app-button'); // Use common app button style
            button.onclick = () => checkAnswer(button, option, question.correctArtist, question.artwork);
            artistChoicesDiv.appendChild(button);
        });
    }

    function checkAnswer(selectedButton, selectedArtist, correctArtist, artwork) {
        const buttons = artistChoicesDiv.querySelectorAll('button');
        let isCorrect = selectedArtist === correctArtist;

        buttons.forEach(button => {
            button.disabled = true; // Disable all buttons
            if (button.textContent === correctArtist) {
                button.classList.add('correct-answer'); // Highlight correct answer
            } else if (button.textContent === selectedArtist) {
                 if (!isCorrect) {
                    button.classList.add('wrong-answer'); // Highlight wrong answer
                 }
            }
             // Optionally dim others:
             // if (button !== selectedButton && button.textContent !== correctArtist) {
             //     button.style.opacity = '0.5';
             // }
        });

        if (isCorrect) {
            score++;
            scoreCounterSpan.textContent = score;
            feedbackDiv.textContent = 'תשובה נכונה! כל הכבוד!';
            feedbackDiv.classList.add('feedback-correct', 'fade-in');
        } else {
            feedbackDiv.textContent = `תשובה שגויה. האמן הנכון הוא ${correctArtist}.`;
            feedbackDiv.classList.add('feedback-wrong', 'fade-in');
        }

        displayResult(artwork);
    }

    function displayResult(artwork) {
         // Image loading with animation for artwork
         artworkImage.classList.remove('loaded');
         artworkImage.onload = () => {
              artworkImage.classList.add('loaded');
         };
         artworkImage.onerror = () => {
              // Handle image loading errors visually
              artworkImage.classList.add('loaded');
              artworkImage.alt = "Failed to load artwork image";
         };
        artworkImage.src = artwork.image;

        artworkTitle.textContent = `היצירה: "${artwork.title}"`; // Added quotes for title
        // Safely extract artist name before year if possible, or use full info
        const artistNameMatch = artwork.artistInfo.match(/^([^(\s]+)\s+([^(\s]+)/); // Try to get first two words before ()
        if (artistNameMatch && artistNameMatch.length > 2) {
             artistNameResult.textContent = `${artistNameMatch[1]} ${artistNameMatch[2]}`; // Use first two words
        } else {
             artistNameResult.textContent = artwork.artistInfo.split('(')[0].trim(); // Fallback to old method
        }


        artistInfoPara.textContent = artwork.artistInfo;

        resultContainer.style.display = 'block';
        setTimeout(() => { resultContainer.classList.add('visible'); }, 50); // Add slight delay for display change
    }

    function endQuiz() {
        finalScoreSpan.textContent = score;
        showScreen(quizEndScreen);
    }

    // --- Event Listeners ---
    startQuizButton.onclick = startQuiz;
    restartQuizButton.onclick = startQuiz;

    nextButton.onclick = () => {
        currentQuestionIndex++;
        loadQuestion();
    };

    toggleExplanationButton.onclick = () => {
        const isHidden = explanationContentDiv.style.display === 'none';
        if (isHidden) {
             explanationContentDiv.style.display = 'block';
             setTimeout(() => { explanationContentDiv.classList.add('fade-in'); }, 50);
        } else {
            explanationContentDiv.classList.remove('fade-in');
            setTimeout(() => { explanationContentDiv.style.display = 'none'; }, transitionSpeedMs);
        }
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על חתימות באמנות' : 'הצג הסבר על חתימות באמנות';
    };


    // Initial state: Show start screen
    showScreen(quizStartScreen);

</script>