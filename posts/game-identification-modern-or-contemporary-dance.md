---
title: "צלול לעולם המחול: ריקוד מודרני או עכשווי?"
english_slug: game-identification-modern-or-contemporary-dance
category: "אמנויות הבמה"
tags:
  - מחול
  - ריקוד מודרני
  - ריקוד עכשווי
  - סגנונות ריקוד
  - פרפורמנס
---
# צלול לעולם המחול: ריקוד מודרני או עכשווי?

עולם המחול עשיר ומגוון, וההבחנה בין סגנונות כמו ריקוד מודרני לעכשווי יכולה להיות מאתגרת. האם אתה מוכן לצלול לעומק ולזהות את המאפיינים הייחודיים? בוא נצא למסע ויזואלי וחווייתי שיעזור לך להבחין ביניהם באמצעות קטעי וידאו ותמונות מרתקים.

<div id="game-area">
    <div id="media-container">
        <!-- Media will be loaded here -->
        <div class="loading-indicator">טוען קטע מחול...</div>
    </div>
    <div id="question-area">
        <h3>לפניך קטע מחול. האם הוא שייך ל...</h3>
        <div id="options">
            <!-- Answer buttons will be generated here -->
        </div>
    </div>
    <div id="feedback" style="display: none;">
        <h4></h4>
        <p></p>
        <button id="next-question" style="display: none;">לשאלה הבאה ></button>
    </div>
    <div id="game-progress"></div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap'); /* Attempt to load a better font */

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        color: #333;
        background-color: #f0f2f5;
        direction: rtl; /* Ensure RTL display */
        text-align: right; /* Ensure text aligns right by default */
    }

    h1, h2, h3, h4 {
        color: #2c3e50;
        text-align: center; /* Center titles */
        margin-bottom: 1rem;
    }

    #game-area {
        max-width: 750px;
        margin: 30px auto;
        padding: 25px;
        background: linear-gradient(135deg, #ffffff, #f9f9f9);
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        text-align: center;
        position: relative; /* Needed for potential absolute positioning */
        overflow: hidden; /* Clear floats/margins */
    }

    #media-container {
        margin-bottom: 25px;
        min-height: 350px; /* Reserve more space */
        background-color: #e0e0e0; /* Loading background */
        border-radius: 10px;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative; /* For loading indicator */
        transition: background-color 0.5s ease;
    }

    #media-container iframe,
    #media-container img {
        max-width: 100%;
        height: auto; /* Maintain aspect ratio */
        display: block;
        border-radius: 10px; /* Match container border-radius */
        opacity: 0; /* Start hidden for fade-in */
        transition: opacity 1s ease; /* Fade-in animation */
    }

    #media-container iframe.loaded,
     #media-container img.loaded {
        opacity: 1;
    }


    .loading-indicator {
        font-size: 1.2em;
        color: #555;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 1;
    }


    #question-area h3 {
        margin-bottom: 20px;
        color: #34495e;
    }

    #options {
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        margin-bottom: 20px;
    }

    #options button {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 30px; /* Pill shape buttons */
        background-color: #ecf0f1;
        color: #34495e;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        min-width: 120px; /* Ensure minimum size */
    }

    #options button:hover:not(:disabled) {
        background-color: #bdc3c7;
        transform: translateY(-2px); /* Slight lift on hover */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    #options button:active:not(:disabled) {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    #options button:disabled {
        opacity: 0.7;
        cursor: not-allowed;
    }

    /* Visual feedback on button selection */
    #options button.correct {
        background-color: #2ecc71; /* Green */
        color: white;
        box-shadow: 0 4px 10px rgba(46, 204, 113, 0.4);
        font-weight: bold;
    }

    #options button.incorrect {
        background-color: #e74c3c; /* Red */
        color: white;
        box-shadow: 0 4px 10px rgba(231, 76, 60, 0.4);
        font-weight: bold;
    }
     #options button:disabled:not(.correct):not(.incorrect) {
        background-color: #ecf0f1; /* Keep original color if not the chosen or correct answer */
        color: #34495e;
        box-shadow: none;
     }


    #feedback {
        margin-top: 25px;
        padding: 20px;
        border-radius: 10px;
        text-align: right;
        opacity: 0; /* Start hidden for fade-in */
        transform: translateY(20px); /* Start below for slide-up */
        transition: opacity 0.5s ease, transform 0.5s ease;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    }
     #feedback.show {
        opacity: 1;
        transform: translateY(0);
     }

    #feedback h4 {
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.3em;
    }

    #feedback p {
        margin-bottom: 15px;
        color: #555;
    }

    #feedback.correct {
        background-color: #d4edda; /* Light green */
        border-color: #c3e6cb;
        color: #155724;
    }

    #feedback.incorrect {
        background-color: #f8d7da; /* Light red */
        border-color: #f5c6cb;
        color: #721c24;
    }

    #next-question {
        margin-top: 15px;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 30px; /* Pill shape */
        background-color: #3498db; /* Blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    #next-question:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    #next-question:active {
        transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

     #game-progress {
        margin-top: 20px;
        font-size: 0.9em;
        color: #7f8c8d;
        text-align: center;
     }


    #show-explanation {
        display: block;
        margin: 40px auto 20px auto;
        padding: 15px 30px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 30px; /* Pill shape */
        background-color: #95a5a6; /* Grey */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    #show-explanation:hover {
        background-color: #7f8c8d;
        transform: translateY(-2px);
         box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    #show-explanation:active {
         transform: translateY(0);
         box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }


    #explanation {
        max-width: 750px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #ddd;
        border-radius: 15px;
        background-color: #fefefe;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        display: none; /* Start hidden */
    }

    #explanation h2 {
        color: #2c3e50;
        margin-top: 10px;
        margin-bottom: 20px;
        border-bottom: 2px solid #3498db; /* Highlight border */
        padding-bottom: 10px;
        text-align: right; /* Align heading right */
    }

     #explanation h3 {
        color: #34495e;
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.2em;
        text-align: right; /* Align subheading right */
     }

    #explanation p, #explanation ul {
        line-height: 1.8;
        color: #555;
        text-align: right;
        margin-bottom: 15px;
    }

    #explanation ul {
        padding-right: 25px; /* Add padding for bullet points */
        list-style: disc outside; /* Ensure bullet points are visible */
    }

    #explanation ul li {
        margin-bottom: 8px;
    }

</style>

<button id="show-explanation">הצגת הסבר מעמיק על הסגנונות</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: ריקוד מודרני מול ריקוד עכשווי</h2>

    <h3>הגדרת ריקוד מודרני</h3>
    <p>ריקוד מודרני התפתח בסוף המאה ה-19 ותחילת המאה ה-20, בעיקר בארה"ב ובגרמניה, כתגובה לשבירת מוסכמות הבלט הקלאסי. חלוצות כמו איזדורה דאנקן, מרתה גרהם, דוריס האמפרי וצ'ארלס ויידמן חיפשו שפות תנועתיות חדשות, חופשיות יותר, המחוברות לרגש ולנשימה הטבעית של הגוף. העקרונות המרכזיים כללו שימוש במשקל הגוף (נפילה והתאוששות - Fall and Recovery אצל האמפרי וויידמן; כיווץ ושחרור - Contraction and Release אצל גרהם), עבודה עם הרצפה, ביטוי אישי והתמקדות בחוויה האנושית. מרס קנינגהם, שהגיע מאוחר יותר, שבר גם הוא מוסכמות והכניס אלמנטים של אקראיות וניתוק הקשר המסורתי בין תנועה למוזיקה או לעלילה.</p>
    <ul>
        <li><strong>מקורות:</strong> סוף המאה ה-19 - תחילת המאה ה-20, כתגובה לבלט.</li>
        <li><strong>עקרונות יסוד:</strong> שימוש במשקל, עבודה עם הרצפה, חיבור לנשימה, ביטוי רגשי/אישי.</li>
        <li><strong>חלוצות בולטות:</strong> מרתה גרהם, דוריס האמפרי, מרס קנינגהם, איזדורה דאנקן.</li>
    </ul>

    <h3>הגדרת ריקוד עכשווי</h3>
    <p>ריקוד עכשווי החל להתפתח באמצע המאה ה-20 ואילך, והוא נחשב במידה רבה ליורש הטבעי של הריקוד המודרני, אך הוא אקלקטי ופתוח הרבה יותר. הוא שואב השראה מסגנונות רבים (בלט, ג'אז, היפ הופ, אמנויות לחימה, סגנונות אתניים ותיאטרון פיזי) ואינו כבול לטכניקה אחת או עקרון יסוד דומיננטי. הדגש בריקוד העכשווי הוא לעיתים קרובות על קונספט, חדשנות, שיתופי פעולה בין-תחומיים (עם וידאו, סאונד ארט, עיצוב תפאורה ייחודי) והגבולות בין הבמה לקהל מיטשטשים. יש בו חופש גדול להתנסות ולשלב אלמנטים מגוונים.</p>
    <ul>
        <li><strong>התפתחות:</strong> אמצע המאה ה-20 ואילך, התפתח מהמודרני.</li>
        <li><strong>אקלקטיות והשפעות:</strong> שילוב אלמנטים מבלט, ג'אז, היפ הופ, תיאטרון פיזי ועוד.</li>
        <li><strong>דגש מרכזי:</strong> קונספט, חדשנות, שיתופי פעולה בין-תחומיים, פחות כבול לטכניקה ספציפית.</li>
    </ul>

    <h3>מאפיינים ויזואליים והבדלים תנועתיים מרכזיים</h3>
    <p>למרות שיש חפיפה רבה, ניתן להבחין בהבדלים מסוימים:</p>
    <ul>
        <li><strong>שימוש ברצפה:</strong> בשני הסגנונות נעשה שימוש נרחב ברצפה, אך במודרני (בעיקר בטכניקות כמו גרהם או האמפרי) יש לרוב מערכת מוגדרת יותר של תנועות רצפה, בעוד שבעכשווי השימוש יכול להיות חופשי ומגוון יותר.</li>
        <li><strong>נשימה ומשקל:</strong> המודרני שם דגש חזק על חיבור התנועה לנשימה ולשימוש מודע במשקל (נפילה, שחרור). בעכשווי, בעוד שאלמנטים אלו קיימים, הם עשויים להיות משולבים עם קווים וצורה הלקוחים מהבלט או עם תנועות מהירות ושבורות יותר.</li>
        <li><strong>מבנה כוריאוגרפי:</strong> כוריאוגרפיה מודרנית קלאסית (למשל גרהם) נוטה להיות דרמטית ובעלת קו עלילתי או נושאי ברור (גם אם מופשט). כוריאוגרפיה עכשווית יכולה להיות הרבה פחות נרטיבית, לעיתים אבסטרקטית לחלוטין, ומתמקדת יותר באיכות התנועה, האינטראקציה בין הרקדנים, או הקשר לקונספט.</li>
        <li><strong>יחס למוזיקה:</strong> בעוד שבמודרני המסורתי לרוב יש קשר ברור למוזיקה (גם אם לא תמיד נגינה חיה), בעכשווי נפוץ יותר שימוש בשקט, סאונד ארט, מוזיקה אלקטרונית, או ניתוק מוחלט בין התנועה לצליל (בהשפעת קנינגהם).</li>
        <li><strong>מנעד תנועתי:</strong> ריקוד עכשווי נוטה להיות בעל מנעד תנועתי רחב יותר, המשלב קווים ארוכים ומוגבהים מהבלט יחד עם תנועות גרוטסקיות, שבורות או יומיומיות. המודרני הקלאסי נוטה להיות בעל אוצר תנועתי יותר מוגדר לטכניקה הספציפית.</li>
    </ul>

    <h3>האתגר בזיהוי</h3>
    <p>ההבחנה אינה תמיד פשוטה כי:</p>
    <ul>
        <li><strong>קווי דמיון:</strong> שניהם סגנונות לא-קלאסיים ששברו את חוקי הבלט ומאופיינים בחופש ביטוי.</li>
        <li><strong>התפתחות מתמדת:</strong> הסגנונות אינם סטטיים וכל הזמן מתפתחים ומשפיעים זה על זה.</li>
        <li><strong>כוריאוגרפים משלבים:</strong> אמנים רבים כיום אינם "טהורים" בסגנונם ומשלבים אלמנטים ממודרני, עכשווי, בלט, ג'אז ועוד, מה שיוצר סגנונות היברידיים.</li>
    </ul>

    <h3>דוגמאות קצרות ויצירות מפתח</h3>
    <ul>
        <li><strong>ריקוד מודרני:</strong> יצירות של מרתה גרהם ("Steps in the Street" מתוך Chronicle), דוריס האמפרי ("The Shakers"), מרס קנינגהם (עבודות משנות ה-60 וה-70).</li>
        <li><strong>ריקוד עכשווי:</strong> עבודות של פינה באוש (טאנץ'-תיאטר), אוהד נהרין (גאגא), אקראם קאן (שילוב קאטאק עם עכשווי), שרון אייל.</li>
    </ul>
</div>

<script>
    const questions = [
        {
            media: 'https://www.youtube.com/embed/n5J1c6F_fWk?si=abcdefg&controls=0', // Placeholder - Replace with actual URLs
            type: 'video',
            style: 'מודרני',
            options: ['מודרני', 'עכשווי', 'בלט קלאסי'],
            explanation: 'קטע זה מציג שימוש רב ברצפה, עבודה עם משקל ונשימה, ודרמטיות המאפיינים את טכניקת מרתה גרהם, שהיא אבן יסוד בריקוד המודרני. שימו לב לכיווץ (Contraction) המפורסם שלה.'
        },
        {
            media: 'https://via.placeholder.com/600x350.png?text=תמונת+ריקוד+עכשווי+-+אינטראקציה', // Placeholder - Replace with actual URLs
            type: 'image',
            style: 'עכשווי',
            options: ['מודרני', 'ג\'אז', 'עכשווי'],
            explanation: 'התמונה מציגה שילוב של קווים מודרניים עם עבודה אקלקטית על הרצפה וצורות פחות קונבנציונליות, המצביעים על סגנון עכשווי הפתוח להשפעות מגוונות. לרוב יש דגש על קונספט ואינטראקציה בין הרקדנים.'
        },
        {
            media: 'https://www.youtube.com/embed/PAGmQ_Yn31o?si=abcdefg&controls=0', // Placeholder - Replace with actual URLs - FIND A CLEAR BALLET EXAMPLE
            type: 'video',
            style: 'בלט קלאסי', // Example of a distractor
            options: ['מודרני', 'בלט קלאסי', 'עכשווי'],
            explanation: 'הקטע מציג תנועות אלגנטיות, קווים מוגבהים, עבודה על האצבעות ויציבה זקופה - מאפיינים מובהקים של הבלט הקלאסי. סגנונות מודרני ועכשווי נוצרו במקור כדי לשבור את המוסכמות הללו.'
        },
        {
            media: 'https://via.placeholder.com/600x350.png?text=תמונת+ריקוד+מודרני+(Humphrey)+-+נפילה', // Placeholder - Replace with actual URLs - FIND A GOOD FALL/RECOVERY EXAMPLE
            type: 'image',
            style: 'מודרני',
            options: ['היפ הופ', 'מודרני', 'עכשווי'],
            explanation: 'התמונה לוכדת רגע של "נפילה והתאוששות" (Fall and Recovery) ושימוש באנרגיה קינטית, שהם עקרונות יסוד בטכניקת דוריס האמפרי, מחלוצות הריקוד המודרני. יש דגש על שימוש מודע במשקל.'
        },
         {
            media: 'https://via.placeholder.com/600x350.png?text=תמונת+ריקוד+עכשווי+(פינה+באוש)', // Placeholder - Replace with actual URLs - FIND A BAUSCH-LIKE IMAGE
            type: 'image',
            style: 'עכשווי',
            options: ['מודרני', 'עכשווי', 'בלט קלאסי'],
            explanation: 'ריקוד עכשווי, במיוחד בגישות כמו "טאנץ\'-תיאטר", משלב תנועה עם אלמנטים תיאטרליים, הבעה רגשית עמוקה, ולעיתים קרובות עוסק בנושאים אנושיים או חברתיים בצורה חופשית ואקלקטית.'
        }
         // Add more questions for variety
         // { media: '...', type: 'video', style: 'עכשווי', options: ['מודרני', 'עכשווי', 'בלט'], explanation: '...' }
         // { media: '...', type: 'image', style: 'מודרני', options: ['מודרני', 'ג\'אז', 'עכשווי'], explanation: '...' }
    ];

    let currentQuestionIndex = 0;

    const gameArea = document.getElementById('game-area');
    const mediaContainer = document.getElementById('media-container');
    const questionArea = document.getElementById('question-area');
    const optionsDiv = document.getElementById('options');
    const feedbackDiv = document.getElementById('feedback');
    const feedbackTitle = feedbackDiv.querySelector('h4');
    const feedbackText = feedbackDiv.querySelector('p');
    const nextQuestionButton = document.getElementById('next-question');
    const showExplanationButton = document.getElementById('show-explanation');
    const explanationDiv = document.getElementById('explanation');
    const gameProgressDiv = document.getElementById('game-progress'); // New element

    function updateProgress() {
        gameProgressDiv.textContent = `שאלה ${currentQuestionIndex + 1} מתוך ${questions.length}`;
    }

    function loadQuestion(index) {
        if (index >= questions.length) {
            endGame();
            return;
        }

        currentQuestionIndex = index;
        const q = questions[currentQuestionIndex];

        // Clear previous media and feedback, reset animations
        mediaContainer.innerHTML = '<div class="loading-indicator">טוען קטע מחול...</div>'; // Show loading
        mediaContainer.style.backgroundColor = '#e0e0e0'; // Reset background
        feedbackDiv.style.display = 'none';
        feedbackDiv.classList.remove('show', 'correct', 'incorrect'); // Remove classes
        nextQuestionButton.style.display = 'none';
        optionsDiv.innerHTML = ''; // Clear previous options

        updateProgress(); // Update progress counter

        // Load new media
        const loadMediaElement = (element) => {
             mediaContainer.innerHTML = ''; // Remove loading indicator
             mediaContainer.appendChild(element);
             // Wait a moment for potential render before fading in
             setTimeout(() => {
                element.classList.add('loaded');
                mediaContainer.style.backgroundColor = 'transparent'; // Set background transparent after loading
             }, 50);
        };


        if (q.type === 'video') {
            const iframe = document.createElement('iframe');
            // Note: Setting autoplay is tricky and often blocked. controls=0 means custom controls needed, or rely on default iframe behavior.
            // For simplicity, relying on user to click play. Adding `autoplay=1` might not work.
            iframe.src = `${q.media}${q.media.includes('?') ? '&' : '?'}autoplay=0&controls=1`; // Ensure controls are visible now
            iframe.width = '600'; // Adjust size as needed
            iframe.height = '350'; // Adjust size as needed
            iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
            iframe.allowFullscreen = true;
            iframe.frameBorder = '0';
            iframe.loading = 'lazy'; // Add lazy loading attribute

            // Simple way to detect load for iframe (might not work reliably cross-browser/content)
            iframe.onload = () => loadMediaElement(iframe);
             // Fallback in case onload doesn't fire
            setTimeout(() => { if (!iframe.classList.contains('loaded')) loadMediaElement(iframe); }, 3000); // Assume loaded after 3s


        } else if (q.type === 'image') {
            const img = document.createElement('img');
            img.src = q.media;
            img.alt = `תמונה המציגה ${q.style} ריקוד`;
            img.loading = 'lazy'; // Add lazy loading attribute
            img.onload = () => loadMediaElement(img);
             // Fallback
            setTimeout(() => { if (!img.classList.contains('loaded')) loadMediaElement(img); }, 3000); // Assume loaded after 3s
        }

        // Load options
        q.options.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option;
            button.onclick = () => checkAnswer(button, option); // Pass button element
            optionsDiv.appendChild(button);
        });

         // Enable options (redundant if cleared and recreated, but good practice)
        optionsDiv.querySelectorAll('button').forEach(button => {
            button.disabled = false;
            button.classList.remove('correct', 'incorrect'); // Ensure no previous classes
        });

        // Hide explanation if shown
        if (explanationDiv.style.display !== 'none') {
             explanationDiv.style.display = 'none';
             showExplanationButton.textContent = 'הצגת הסבר מעמיק על הסגנונות';
        }
    }

    function checkAnswer(selectedButton, selectedAnswer) {
        const q = questions[currentQuestionIndex];
        const isCorrect = selectedAnswer === q.style;

        // Disable all options after selection
        optionsDiv.querySelectorAll('button').forEach(button => {
            button.disabled = true;
             // Add class to the *selected* button
            if (button === selectedButton) {
                 button.classList.add(isCorrect ? 'correct' : 'incorrect');
             }
             // Always highlight the correct answer button
             if (button.textContent === q.style && button !== selectedButton) {
                 button.classList.add('correct');
             }
             // Add 'fade' class to non-selected/non-correct buttons? (Optional, might make it too busy)
             // if (button !== selectedButton && button.textContent !== q.style) { button.style.opacity = '0.5'; }
        });


        feedbackDiv.style.display = 'block';
        feedbackDiv.classList.remove('correct', 'incorrect'); // Remove previous state class
        feedbackDiv.classList.add(isCorrect ? 'correct' : 'incorrect');
        feedbackTitle.textContent = isCorrect ? '🎉 מעולה! זיהוי מדויק.' : '🤔 כמעט! בוא נבין למה...'; // More engaging titles
        feedbackText.textContent = q.explanation;

        // Animate feedback in
        setTimeout(() => { feedbackDiv.classList.add('show'); }, 50);


        nextQuestionButton.style.display = 'block';
        // Animate next button in
         setTimeout(() => { nextQuestionButton.style.opacity = '1'; nextQuestionButton.style.transform = 'translateY(0)'; }, 500); // Delayed fade/slide in

    }

    function endGame() {
        gameArea.innerHTML = `
            <h2>👏 סיימת את ההתנסות בהצלחה!</h2>
            <p>עכשיו, אחרי שהתנסית בזיהוי, אתה מוכן לצלול עמוק יותר.</p>
            <p>לחץ על הכפתור למטה כדי לקרוא הסבר מפורט על ההבדלים הדקים והמשמעותיים בין הסגנונות.</p>
             <button id="restart-game" style="
                margin-top: 20px;
                padding: 12px 25px;
                font-size: 1.1em;
                cursor: pointer;
                border: none;
                border-radius: 30px;
                background-color: #f39c12; /* Orange */
                color: white;
                transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                התנסות מחדש
            </button>
        `; // More engaging end game text and a restart button

        document.getElementById('restart-game').onclick = () => {
             gameArea.innerHTML = `
                 <div id="media-container">
                     <div class="loading-indicator">טוען קטע מחול...</div>
                 </div>
                 <div id="question-area">
                     <h3>לפניך קטע מחול. האם הוא שייך ל...</h3>
                     <div id="options">
                         <!-- Answer buttons will be generated here -->
                     </div>
                 </div>
                 <div id="feedback" style="display: none;">
                     <h4></h4>
                     <p></p>
                     <button id="next-question" style="display: none;">לשאלה הבאה ></button>
                 </div>
                 <div id="game-progress"></div>
             `; // Re-create inner structure
             // Re-get references
             const gameAreaRe = document.getElementById('game-area');
             const mediaContainerRe = document.getElementById('media-container');
             const questionAreaRe = document.getElementById('question-area');
             const optionsDivRe = document.getElementById('options');
             const feedbackDivRe = document.getElementById('feedback');
             const feedbackTitleRe = feedbackDivRe.querySelector('h4');
             const feedbackTextRe = feedbackDivRe.querySelector('p');
             const nextQuestionButtonRe = document.getElementById('next-question');
             const gameProgressDivRe = document.getElementById('game-progress');

             // Re-assign global variables (or pass them)
             // This is a simple implementation, in a larger app, class or objects are better
             window.mediaContainer = mediaContainerRe;
             window.optionsDiv = optionsDivRe;
             window.feedbackDiv = feedbackDivRe;
             window.feedbackTitle = feedbackTitleRe;
             window.feedbackText = feedbackTextRe;
             window.nextQuestionButton = nextQuestionButtonRe;
             window.gameProgressDiv = gameProgressDivRe;

             currentQuestionIndex = 0; // Reset index
             loadQuestion(currentQuestionIndex); // Start over
        };

         // Ensure explanation button remains visible
         showExplanationButton.style.display = 'block';
         explanationDiv.style.display = 'none'; // Hide explanation when game ends
         showExplanationButton.textContent = 'הצגת הסבר מעמיק על הסגנונות';
    }

    // Event listeners
    nextQuestionButton.onclick = () => {
        nextQuestionButton.style.opacity = '0'; // Animate out
        nextQuestionButton.style.transform = 'translateY(20px)'; // Animate out
        feedbackDiv.classList.remove('show'); // Animate feedback out
         setTimeout(() => {
             loadQuestion(currentQuestionIndex + 1); // Load next question after animation starts
         }, 300); // Delay matches transition duration
    };

    showExplanationButton.onclick = () => {
        const isHidden = explanationDiv.style.display === 'none';
        if (isHidden) {
            explanationDiv.style.display = 'block';
             // Optional: scroll to explanation
            // explanationDiv.scrollIntoView({ behavior: 'smooth' });
        } else {
            explanationDiv.style.display = 'none';
        }
        showExplanationButton.textContent = isHidden ? 'הסתרת הסבר מעמיק' : 'הצגת הסבר מעמיק על הסגנונות';
    };

    // Initial load
    loadQuestion(currentQuestionIndex);

</script>
---