---
title: "המלאכה העדינה: סודות כלי העבודה של הלוטייר"
english_slug: the-delicate-craft-luthiers-tools
category: "מלאכות יד"
tags: לוטייר, כלי נגינה, כלי עבודה, מלאכת יד, עץ, אמנות, מוזיקה
---
<h1>המלאכה העדינה: סודות כלי העבודה של הלוטייר</h1>

<p>מאחורי הצליל העשיר של כינור, צ'לו או גיטרה מסתתר עולם קסום של מלאכה עדינה וכלי עבודה סודיים, שלעתים קרובות נראים זרים לעין בלתי מזוינת. האם תצללו איתנו אל עולם הלוטיירים ותצליחו לזהות את הכלים הייחודיים שמעצבים את ליבת הצליל?</p>

<div id="luthier-tools-app" dir="rtl">
    <div id="game-area">
        <div id="tool-image-container">
            <img id="tool-image" src="" alt="כלי עבודה של לוטייר" class="tool-image">
        </div>
        <div id="question-area">
            <p id="tool-question" class="question-text"></p>
            <div id="options-container" class="options-grid">
                <!-- Answer options will be loaded here -->
            </div>
        </div>
        <div id="feedback-area" class="feedback-area">
            <p id="feedback-text" class="feedback-text"></p>
            <button id="next-tool-button" class="game-button next-button hidden">לכלי הבא »</button>
        </div>
        <div id="game-progress" class="progress-bar">
            <span id="current-tool-index" class="progress-current">1</span> מתוך <span id="total-tools" class="progress-total"></span> כלים
            <span class="score-display"> ניקוד: <span id="score" class="score-value">0</span> </span>
        </div>
    </div>
    <div id="game-end" class="game-end hidden">
        <h2>המסע הושלם!</h2>
        <p class="final-score-text">הניקוד הסופי שלך: <span id="final-score" class="final-score-value"></span></p>
        <button id="restart-game-button" class="game-button restart-button">למסע מחודש?</button>
    </div>
</div>

<style>
    /* --- General Styling --- */
    #luthier-tools-app {
        font-family: 'Arial', sans-serif; /* Keeping it simple for compatibility */
        max-width: 700px;
        margin: 20px auto;
        padding: 30px; /* Increased padding */
        border: 1px solid #e0e0e0; /* Softer border */
        border-radius: 12px; /* More rounded corners */
        background-color: #fcfcfc; /* Warm off-white */
        direction: rtl;
        text-align: right;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Add subtle shadow */
        color: #333; /* Darker text for readability */
        position: relative; /* For potential absolute positioning of elements */
        overflow: hidden; /* Ensure nothing leaks out */
    }

    h1 {
        text-align: center;
        color: #005f73; /* Deep blue for headings */
        margin-bottom: 20px;
        font-size: 1.8em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05); /* Subtle text shadow */
    }

    p {
        line-height: 1.7;
        margin-bottom: 15px;
    }

    /* --- Game Area Styling --- */
    #game-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: opacity 0.5s ease-in-out; /* Smooth transition for game area */
    }

    #tool-image-container {
        width: 100%;
        max-width: 450px; /* Slightly larger max width */
        height: 280px; /* Increased height */
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 25px; /* More space below image */
        overflow: hidden;
        border: 1px solid #ccc; /* Border around the image itself */
        border-radius: 8px; /* Rounded corners for image container */
        background-color: #fff; /* White background behind image */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Shadow for image container */
    }

     .tool-image {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        opacity: 1; /* Initial state */
        transition: opacity 0.5s ease-in-out; /* Fade transition for image */
     }

     .tool-image.fade-out {
         opacity: 0;
     }
     .tool-image.fade-in {
         opacity: 1;
     }


    #question-area {
        width: 100%;
        margin-bottom: 25px; /* More space */
        text-align: center;
    }

    .question-text {
        font-size: 1.2em; /* Larger font size */
        margin-bottom: 20px;
        color: #0077b6; /* Primary blue for questions */
        font-weight: bold;
    }

    #options-container {
        display: grid; /* Use grid for better layout control */
        grid-template-columns: 1fr 1fr; /* Two columns */
        gap: 12px; /* Space between buttons */
        width: 100%;
        max-width: 500px; /* Wider options container */
        margin: 0 auto; /* Center grid */
        padding: 0 10px; /* Little padding on sides */
    }

    .option-button {
        padding: 12px 18px; /* Increased padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        border: 1px solid #a0a0a0; /* Softer border */
        border-radius: 6px; /* Rounded corners */
        background-color: #e9ecef;
        color: #333;
        transition: all 0.3s ease; /* Smooth transition for hover/state changes */
        text-align: right;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); /* Subtle button shadow */
    }

    .option-button:hover:not(:disabled) {
        background-color: #d0d7dd; /* Darker hover */
        border-color: #888;
        transform: translateY(-2px); /* Slight lift effect */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

     .option-button:disabled {
        cursor: not-allowed;
        opacity: 0.8; /* Less transparent */
        box-shadow: none; /* Remove shadow when disabled */
     }

     /* --- Feedback and State Styles --- */
    .feedback-area {
        margin-top: 25px;
        min-height: 70px; /* Reserve more space for feedback */
        text-align: center;
        opacity: 0; /* Initially hidden */
        transform: translateY(10px); /* Start slightly lower */
        transition: opacity 0.4s ease-out, transform 0.4s ease-out;
    }

    .feedback-area.visible {
        opacity: 1;
        transform: translateY(0);
    }

    .feedback-text {
        font-weight: bold;
        margin-bottom: 15px;
        font-size: 1.1em;
    }

    .correct {
        color: #28a745; /* Bootstrap success green */
        background-color: #d4edda; /* Light green background */
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
    }

    .incorrect {
        color: #dc3545; /* Bootstrap danger red */
         background-color: #f8d7da; /* Light red background */
         padding: 10px;
         border-radius: 8px;
         border: 1px solid #f5c6cb;
    }

    .option-button.correct-answer {
        background-color: #d4edda; /* Highlight the correct button */
        border-color: #28a745;
        font-weight: bold;
    }

     .option-button.incorrect-answer {
        background-color: #f8d7da; /* Highlight the selected, incorrect button */
        border-color: #dc3545;
     }

    /* --- Buttons --- */
    .game-button {
        padding: 12px 25px; /* Increased padding */
        font-size: 1.1em;
        cursor: pointer;
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.2s ease;
        font-weight: bold;
    }

    .next-button {
        background-color: #0077b6; /* Primary blue */
    }

    .next-button:hover {
        background-color: #023e8a; /* Darker blue */
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .restart-button {
        background-color: #ae441a; /* Coppery brown */
        margin-top: 20px; /* Space above restart button */
    }

    .restart-button:hover {
        background-color: #8d3716; /* Darker brown */
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .hidden {
        display: none;
    }

    /* --- Progress Bar & Score --- */
    .progress-bar {
        margin-top: 30px; /* More space above progress */
        font-size: 1em; /* Slightly larger font */
        color: #555;
        width: 100%;
        text-align: center;
        padding-top: 15px;
        border-top: 1px solid #eee; /* Separator line */
    }

    .progress-current, .progress-total, .score-value {
        font-weight: bold;
        color: #005f73; /* Deep blue for numbers */
    }

    .score-display {
        margin-right: 20px; /* Space between progress and score */
        display: inline-block; /* Ensure spacing works */
    }


    /* --- Game End Screen --- */
    .game-end {
        text-align: center;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
    }

     .game-end.visible {
        opacity: 1;
        transform: translateY(0);
     }

    .game-end h2 {
        color: #005f73;
        margin-bottom: 15px;
        font-size: 2em;
    }

    .final-score-text {
        font-size: 1.2em;
        margin-bottom: 20px;
        color: #555;
    }

    .final-score-value {
        font-size: 1.5em;
        font-weight: bold;
        color: #ae441a; /* Coppery brown for final score */
    }


    /* --- Explanation Toggle & Section --- */
    #toggle-explanation-button {
        display: block;
        width: fit-content;
        margin: 40px auto 20px auto; /* More space around the button */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #28a745; /* Green for explanation toggle */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.2s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation-button:hover {
        background-color: #218838;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #f9f9f9; /* Slightly darker than app background */
        direction: rtl;
        text-align: right;
        line-height: 1.7;
        color: #333;
         opacity: 0; /* Initially hidden */
         transform: translateY(20px);
         transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
    }

     #explanation.visible {
         opacity: 1;
         transform: translateY(0);
     }

    #explanation h2, #explanation h3 {
        color: #005f73;
        margin-top: 20px;
        margin-bottom: 12px;
    }
    #explanation h2 { font-size: 1.6em; }
    #explanation h3 { font-size: 1.3em; }

    #explanation p {
        margin-bottom: 18px;
    }

    #explanation ul {
        list-style: disc inside;
        margin-bottom: 18px;
        padding-right: 20px; /* Indent list */
    }

    #explanation li {
        margin-bottom: 10px;
        line-height: 1.6;
    }

    /* --- Responsive Adjustments --- */
    @media (max-width: 600px) {
        #options-container {
            grid-template-columns: 1fr; /* Single column on small screens */
            max-width: 300px; /* Narrower column */
        }
        #luthier-tools-app {
            padding: 20px;
        }
        h1 {
            font-size: 1.5em;
        }
         .question-text {
            font-size: 1em;
         }
         .option-button, .game-button {
             font-size: 1em;
             padding: 10px 15px;
         }
         .progress-bar {
             font-size: 0.9em;
             display: flex;
             flex-direction: column;
             align-items: center;
             gap: 5px;
         }
         .score-display {
             margin-right: 0;
         }
    }

</style>

<button id="toggle-explanation-button">הצגת הסבר מורחב על המלאכה</button>

<div id="explanation" class="explanation-content hidden" dir="rtl">
    <h2>העולם המופלא של כלי הלוטייר</h2>

    <p>מלאכת הלוטרייה - יצירה ותיקון של כלי קשת ופריטה כמו כינורות, צ'לו, גיטרות ועוד - היא שילוב נדיר של אומנות, מלאכת יד מדויקת ומדע האקוסטיקה. בניגוד לנגר רגיל, לוטייר אינו עובד רק עם עץ, אלא עם צליל. כל חיתוך, כל ליטוש וכל הדבקה משפיעים על התהודה, הגוון והעוצמה של הכלי המוגמר.</p>

    <h3>הצורך בכלי עבודה מותאמים אישית ומדויקים</h3>
    <p>כלי נגינה איכותיים דורשים דיוק של מילימטרים, לעיתים אף חלקי מילימטר, במיוחד בעובי לוחות התהודה (הטופ והבק) ובזוויות החיבורים השונים. כלי עבודה סטנדרטיים מעולם הנגרות לרוב גדולים ומחוספסים מדי עבור עבודה כה עדינה. לכן, לוטיירים משתמשים, ומעתים אף מייצרים לעצמם, מגוון רחב של כלים קטנים, חדים ומדויקים להפליא, המותאמים במיוחד לעבודה על קימורים, זוויות וחללים קטנים.</p>

    <h3>סקירה של סוגי כלי עבודה מרכזיים</h3>
    <p>סדנת לוטייר כוללת מגוון כלים ייחודיים:</p>
    <ul>
        <li><strong>כלי הקצעה קטנים (Planes):</strong> משמשים לעיצוב ודילול עץ. מקצועות אצבע, למשל, הם זעירים ומעוגלים, אידיאליים לעיבוד הקימורים של גוף הכלי.</li>
        <li><strong>אזמלים וגוג'ים (Chisels & Gouges):</strong> מגיעים במגוון רחב של צורות וגדלים (ישרים, מעוגלים, אלכסוניים) ומשמשים לגילוף, פינוי עץ ויצירת חללים.</li>
        <li><strong>מגרדות (Scrapers):</strong> פלטות מתכת דקות וקשיחות המשמשות לגימור חלק במיוחד של פני העץ לפני הליטוש או הציפוי בלכה. יעילות במיוחד באזורים עם סיבים קשים או משתנים.</li>
        <li><strong>מסורים מיוחדים:</strong> כמו מסור נימה (Coping Saw / Fret Saw) עם להב דק וגמיש לחיתוך צורות מורכבות, למשל את חורי ה-F בכינורות.</li>
        <li><strong>מלחציים (Clamps):</strong> מלחציים רבים ומגוונים, כולל מלחצי סדן צדדי להדבקת ה"צלעות" (Ribs), מלחצי Purfling להדבקת הקישוט העדין בשולי הכלי, ומלחצי צוואר.</li>
        <li><strong>כלי מדידה:</strong> קליברס מיוחדים למדידת עובי לוחות התהודה בדיוק מרבי (Thickness Calipers), סרגלים, מדי זווית.</li>
        <li><strong>סכיני גילוף:</strong> סכינים חדים ומדויקים לעבודות גילוף ופירוט עדינות.</li>
    </ul>

    <h3>הקשר לאיכות הצליל והעמידות</h3>
    <p>השימוש המיומן בכלים אלו מאפשר ללוטייר לשלוט בעובי המדויק של לוחות העץ, בזוויות החיבורים ובעיצוב הפנימי והחיצוני של הכלי. עובי הלוחות, למשל, משפיע באופן דרמטי על התהודה ואיכות הצליל. חיבורים מדויקים מבטיחים שהכלי יהיה יציב ועמיד לאורך שנים רבות. כל כלי תורם ליכולת הלוטייר לממש את הפוטנציאל האקוסטי של העץ שעמו הוא עובד.</p>

    <h3>מלאכה מסורתית מול כלים מודרניים</h3>
    <p>בעוד שליבת מלאכת הלוטרייה נותרה נאמנה לכלים וטכניקות מסורתיות שהתפתחו במשך מאות שנים, במיוחד בכל הנוגע לעיבוד עדין והגעה לניואנסים אקוסטיים, כלי עבודה מודרניים מוצאים את מקומם לעיתים בשלבים הראשוניים של העבודה (כמו ניסור גס או כרסום ראשוני) או בכלי מדידה דיגיטליים. עם זאת, הקסם והאומנות של המקצוע טמונים עדיין במגע היד, בעין המיומנת וביכולת ל"הקשיב" לעץ תוך כדי עבודה, יכולות הנרכשות באמצעות שנים של ניסיון ושימוש בכלי העבודה המסורתיים.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // --- Data Definition ---
        const tools = [
            {
                image: 'https://images.unsplash.com/photo-1606433485961-4a3b3b3a0c3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80', // Replace with actual image URLs if available
                question: 'זהו כלי עבודה זעיר המשמש להקצעה עדינה של עץ, במיוחד באזורים מעוגלים כמו קשתות הכלי. מה שמו?',
                options: ['איזמל מעוגל', 'מסור נימה', 'מקצוע אצבע', 'מגרדת עץ'],
                correctAnswer: 'מקצוע אצבע',
                feedback: 'נכון! מקצוע אצבע (Finger Plane) הוא חיוני לעיצוב הקימורים העדינים של גוף הכינור או הגיטרה, ממש כמו לפסל עץ קטן עם דיוק מירבי.'
            },
            {
                image: 'https://images.unsplash.com/photo-1590030615104-a8a4c2b4c9b0?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80',
                question: 'כלי חיתוך זה עם להב ישר משמש לפינוי עץ, חיתוך מגרעות ועבודה בפרטים קטנים שדורשים קו ישר ונקי. מהו?',
                options: ['מקצוע אצבע', 'מלחצי סדן צדדי', 'אזמל ישר', 'סכין גילוף'],
                correctAnswer: 'אזמל ישר',
                feedback: 'מעולה! אזמלים ישרים (Bench Chisels) משמשים לחיתוך ופינוי עץ במגוון צורות וגדלים, ונדרשים לדיוק רב במיוחד בחיבורים - אלו הידיים המנתחות של הלוטייר.'
            },
             {
                image: 'https://images.unsplash.com/photo-1599282626227-819c5531d1e3?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80',
                question: 'איזמל זה בעל להב מעוגל משמש ליצירת חללים קעורים או גילוף קווים מעוגלים, למשל בחלק הפנימי של גוף הכלי או לעיצוב הצוואר. מה שמו?',
                options: ['אזמל ישר', 'מגרדת קמורה', 'איזמל מעוגל (גוג\')', 'סכין גילוף'],
                correctAnswer: 'איזמל מעוגל (גוג\')',
                feedback: 'בדיוק! איזמלים מעוגלים (גוג\', Gouges) מגיעים במגוון רחב של רדיוסים ומשמשים לגילוף הצד הפנימי של לוחות התהודה, הצוואר ועוד - הם מעניקים לכלי את הצורה המופלאה שלו מבפנים.'
            },
            {
                image: 'https://via.placeholder.com/400x250?text=Side+Clamps+Demo', // Placeholder - replace if actual image found
                question: 'כלי לחיצה מיוחדים אלו משמשים להדבקת ה"סדן" (Ribs) של הכלי אל קשתות הגוף העליונה והתחתונה, ויוצרים את "הצלעות" של הכלי. מה שמו?',
                options: ['מלחצי F', 'מלחצי C', 'מלחצי סדן צדדי', 'מלחצי פינה'],
                correctAnswer: 'מלחצי סדן צדדי',
                feedback: 'מצוין! מלחצי סדן צדדי (Side Clamps) הם הכרחיים להצמדה אחידה ומדויקת של הסדן לגוף הכלי במהלך ההדבקה - הם נותנים לכלי את צורתו התלת-ממדית הייחודית.'
            },
             {
                image: 'https://via.placeholder.com/400x250?text=Coping+Saw+Action', // Placeholder - replace if actual image found
                question: 'מסור זה עם להב דק וגמיש משמש לניסור צורות מורכבות ופנימיות בעץ, למשל בחורי ה-F בכינורות או בקישוטים עדינים שדורשים חיתוך צורני. מה שמו?',
                options: ['מסור עץ ידני', 'מסור נימה / מסור קשת', 'מסור סרט', 'מסור גרונג'],
                correctAnswer: 'מסור נימה / מסור קשת',
                feedback: 'אכן! מסור נימה (או מסור קשת, Coping Saw) מאפשר חיתוכים עדינים ומעוגלים במקומות שקשה להגיע אליהם עם מסורים אחרים - הוא הכלי ליצירת "העיניים" המפורסמות של הכינור.'
            },
            {
                image: 'https://via.placeholder.com/400x250?text=Card+Scraper+Texture', // Placeholder - replace if actual image found
                question: 'כלי זה בעל להב דק וקשיח עם קצה חד ומופנה (Burr) משמש להסרת כמות קטנה מאוד של חומר ולגימור עדין במיוחד של משטחי עץ, לפני הליטוש הסופי. מה שמו?',
                options: ['מקצוע עץ', 'מגרדת (Scraper)', 'נייר לטש', 'סכין גילוף'],
                correctAnswer: 'מגרדת (Scraper)',
                feedback: 'נכון מאוד! מגרדות עץ (Scrapers) משמשות לגימור חלק במיוחד של המשטח לפני הליטוש, במיוחד באזורים בהם כיוון הסיבים משתנה או באזורים מעוגלים - הן החותם האחרון של הלוטייר על פני העץ.'
            },
             {
                image: 'https://via.placeholder.com/400x250?text=Thickness+Calipers+Use', // Placeholder - replace if actual image found
                question: 'כלי מדידה זה בעל זרועות ארוכות המשמש למדידת עובי לוחות העץ (טופ ובק) בדיוק גבוה במיוחד. מה שמו?',
                options: ['מד זוית', 'סרגל מתכת', 'קליבר עובי (Thickness Calipers)', 'מכשור לייזר'],
                correctAnswer: 'קליבר עובי (Thickness Calipers)',
                feedback: 'בדיוק! קליברי עובי חיוניים להשגת העובי המדויק של לוחות התהודה, פרמטר קריטי לאיכות הצליל - כאן המדע פוגש את האומנות, כשהלוטייר "מקשיב" לעץ ומכוון את עוביו.'
            }
        ];

        // --- State Variables ---
        let currentToolIndex = 0;
        let score = 0;
        const totalTools = tools.length;
        let answerSelected = false; // Flag to prevent multiple clicks

        // --- DOM References ---
        const toolImage = document.getElementById('tool-image');
        const toolQuestion = document.getElementById('tool-question');
        const optionsContainer = document.getElementById('options-container');
        const feedbackArea = document.getElementById('feedback-area');
        const feedbackText = document.getElementById('feedback-text');
        const nextToolButton = document.getElementById('next-tool-button');
        const currentToolIndexSpan = document.getElementById('current-tool-index');
        const totalToolsSpan = document.getElementById('total-tools');
        const scoreSpan = document.getElementById('score');
        const gameArea = document.getElementById('game-area');
        const gameEndArea = document.getElementById('game-end');
        const finalScoreSpan = document.getElementById('final-score');
        const restartGameButton = document.getElementById('restart-game-button');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation-button');

        // --- Initialization ---
        totalToolsSpan.textContent = totalTools;
        loadTool();

        // --- Game Logic Functions ---

        function loadTool() {
            if (currentToolIndex < totalTools) {
                answerSelected = false; // Reset flag
                const tool = tools[currentToolIndex];

                // Animate image change
                toolImage.classList.add('fade-out');
                setTimeout(() => {
                    toolImage.src = tool.image;
                    toolImage.onload = () => { // Wait for image to load before fading in
                        toolImage.classList.remove('fade-out');
                        toolImage.classList.add('fade-in');
                         setTimeout(() => {
                             toolImage.classList.remove('fade-in'); // Clean up class
                         }, 500); // Match fade-in duration
                    };
                    toolImage.onerror = () => { // Handle image loading errors
                         toolImage.src = 'https://via.placeholder.com/400x250?text=Image+Not+Found'; // Fallback
                          toolImage.classList.remove('fade-out');
                          toolImage.classList.add('fade-in');
                           setTimeout(() => {
                                toolImage.classList.remove('fade-in');
                           }, 500);
                    };

                }, 300); // Start fade out before changing source

                toolQuestion.textContent = tool.question;
                optionsContainer.innerHTML = ''; // Clear previous options

                // Shuffle options
                const shuffledOptions = [...tool.options].sort(() => Math.random() - 0.5);

                shuffledOptions.forEach(option => {
                    const button = document.createElement('button');
                    button.classList.add('option-button');
                    button.textContent = option;
                    button.addEventListener('click', () => handleAnswerClick(option));
                    optionsContainer.appendChild(button);
                });

                // Reset feedback area
                feedbackArea.classList.remove('visible');
                feedbackText.textContent = '';
                feedbackText.className = 'feedback-text'; // Reset classes
                nextToolButton.classList.add('hidden');

                // Update progress display smoothly (optional: add count-up animation later)
                currentToolIndexSpan.textContent = currentToolIndex + 1;
                scoreSpan.textContent = score; // Ensure score is updated even if 0

                 // Enable buttons
                optionsContainer.querySelectorAll('.option-button').forEach(button => {
                     button.disabled = false;
                     button.classList.remove('correct-answer', 'incorrect-answer'); // Remove previous highlights
                });


            } else {
                endGame();
            }
        }

        function handleAnswerClick(selectedAnswer) {
            if (answerSelected) return; // Prevent multiple clicks
            answerSelected = true;

            const correctAnswer = tools[currentToolIndex].correctAnswer;
            const feedback = tools[currentToolIndex].feedback;
            const optionButtons = optionsContainer.querySelectorAll('.option-button');

            optionButtons.forEach(button => {
                button.disabled = true; // Disable all options after selection

                if (button.textContent === correctAnswer) {
                    button.classList.add('correct-answer');
                }

                if (button.textContent === selectedAnswer && selectedAnswer !== correctAnswer) {
                    button.classList.add('incorrect-answer');
                }
            });

            // Display feedback
            if (selectedAnswer === correctAnswer) {
                score++;
                feedbackText.textContent = feedback;
                feedbackText.className = 'feedback-text correct';
                scoreSpan.textContent = score; // Update score immediately
            } else {
                feedbackText.textContent = `אופס! התשובה הנכונה היא: "${correctAnswer}". ${feedback}`;
                feedbackText.className = 'feedback-text incorrect';
            }

            // Show feedback area and next button with animation
            feedbackArea.classList.add('visible');
            setTimeout(() => {
                 nextToolButton.classList.remove('hidden');
            }, 700); // Delay showing the next button slightly

        }

        function nextTool() {
            currentToolIndex++;
            loadTool(); // Load the next tool or end game
        }

        function endGame() {
            gameArea.classList.add('hidden'); // Instantly hide game area
            gameArea.style.opacity = 0; // Ensure opacity is 0 if transition didn't finish
            gameEndArea.classList.remove('hidden');
            gameEndArea.classList.add('visible'); // Trigger animation
            finalScoreSpan.textContent = `${score} מתוך ${totalTools}`;
        }

        function restartGame() {
            currentToolIndex = 0;
            score = 0;
            gameEndArea.classList.remove('visible'); // Trigger fade out
            gameEndArea.classList.add('hidden'); // Hide after animation (or instantly for simplicity)

            // Reset game area state before showing
            gameArea.classList.remove('hidden');
            gameArea.style.opacity = 1; // Reset opacity

            loadTool(); // Load the first tool
        }

        function toggleExplanation() {
            const isHidden = explanationDiv.classList.contains('hidden');
            if (isHidden) {
                explanationDiv.classList.remove('hidden');
                 // Add visible class after display block to allow transition
                requestAnimationFrame(() => {
                    explanationDiv.classList.add('visible');
                });
                toggleExplanationButton.textContent = 'הסתר הסבר מורחב';
            } else {
                 explanationDiv.classList.remove('visible'); // Trigger fade out
                 // Hide after animation completes (or instantly for simplicity)
                setTimeout(() => {
                    explanationDiv.classList.add('hidden');
                     toggleExplanationButton.textContent = 'הצגת הסבר מורחב על המלאכה';
                }, 500); // Match transition duration
            }
        }

        // --- Event Listeners ---
        nextToolButton.addEventListener('click', nextTool);
        restartGameButton.addEventListener('click', restartGame);
        toggleExplanationButton.addEventListener('click', toggleExplanation);

    });
</script>
```