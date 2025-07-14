---
title: "קצב עולמי: אתגר זיהוי סגנונות ריקוד טקסי"
english_slug: global-dance-ritual-style-identification-challenge
category: "מדעי החברה / סוציולוגיה ואנתרופולוגיה"
tags:
  - ריקוד
  - טקס
  - תרבות
  - אנתרופולוגיה
  - מסורת
---
# קצב עולמי: אתגר זיהוי סגנונות ריקוד טקסי

לכל פינה בעולם, לכל קהילה ותרבות, יש דרכים ייחודיות לרקוד את הסיפורים, האמונות והרגשות העמוקים ביותר שלה. ריקודים טקסיים הם שער לעולם רוחני וחברתי שלם. האם העיניים שלכם יכולות לזהות את מקורו של ריקוד טקסי רק מהצצה קצרה לתיאור (ודימוי)? צאו למסע מסביב לעולם דרך הקצב - קבלו את אתגר זיהוי סגנונות הריקוד הטקסי!

<div id="dance-challenge-app">
    <div class="app-header">
        <h2 id="question-title">איזה ריקוד טקסי זה?</h2>
        <div id="score-display">ניקוד: <span id="current-score">0</span></div>
    </div>

    <div id="dance-display">
        <!-- Dynamic content (image placeholder and description) will be injected here -->
        <div id="dance-image-placeholder">
            <!-- Optional: An icon or simple animation before an image loads -->
            <svg class="dance-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13.5 1c.2-.8.7-1 1.4-1 .7 0 1.3.2 1.4 1l.8 3h.4c.9 0 1.7.7 1.7 1.7v.4l3 .8c.8.2 1 .7 1 1.4 0 .7-.2 1.3-1 1.4l-3 .8v.4c0 .9-.7 1.7-1.7 1.7h-.4l-.8 3c-.2.8-.7 1-1.4 1-.7 0-1.3-.2-1.4-1l-.8-3h-.4c-.9 0-1.7-.7-1.7-1.7v-.4l-3-.8c-.8-.2-1-.7-1-1.4 0-.7.2-1.3 1-1.4l3-.8v-.4c0-.9.7-1.7 1.7-1.7h.4l.8-3zM12 14c-3.9 0-7 3.1-7 7h14c0-3.9-3.1-7-7-7zM12 12c2.2 0 4-1.8 4-4s-1.8-4-4-4-4 1.8-4 4 1.8 4 4 4z"/>
            </svg>
        </div>
        <p id="dance-description">תיאור הריקוד יופיע כאן.</p>
        <!-- In a real app, an <img> or <video> would go here -->
        <!-- <img id="dance-image" src="" alt="Image of the dance style" style="display:none;"> -->
        <!-- <video id="dance-video" controls src="" style="display:none;"></video> -->
    </div>

    <div id="options-container" class="options-grid">
        <!-- Answer buttons will be added here by JS -->
    </div>

    <div id="feedback-area" class="feedback-area" style="display: none;">
        <p id="feedback-text" class="feedback-text"></p>
        <p id="explanation-text" class="explanation-text"></p>
        <button id="next-question-button" class="action-button primary" style="display: none;">שאלה הבאה</button>
    </div>
     <div id="quiz-complete-message" class="quiz-complete" style="display: none;">
        <h3>סיימת את האתגר!</h3>
        <p>כל הכבוד! ניקוד סופי: <span id="final-score">0</span>.</p>
        <button id="restart-quiz-button" class="action-button secondary">שחק שוב</button>
    </div>
</div>

<button id="show-explanation-button" class="toggle-explanation-button">הצג הסבר מעמיק על ריקודים טקסיים</button>

<div id="full-explanation" class="full-explanation" style="display: none;">
    <h2>הסבר מעמיק: ריקוד טקסי ברחבי העולם</h2>

    <h3>מהו ריקוד טקסי? הגדרה ומטרות.</h3>
    ריקוד טקסי הוא צורת ביטוי תנועתי המהווה חלק אינטגרלי מטקסים בעלי חשיבות דתית, חברתית או פוליטית. הוא לא רק מופע, אלא פעולה בעלת פונקציה עמוקה בתוך הקהילה – חיבור לעולם הרוח, חיזוק קשרים, ציון מעברים חשובים בחיים או הכנה לאירועים משמעותיים. ריקודים אלו לרוב מובנים ומקודדים, כוללים לבוש, אביזרים ומוזיקה ספציפיים, ונושאים מטען סמלי כבד.

    <h3>פונקציות מרכזיות של ריקודים טקסיים</h3>
    ריקודים טקסיים הם רבגוניים בפונקציות שהם ממלאים בתרבויות שונות:
    <ul>
        <li>**ריפוי ורוחניות:** גירוש אנרגיות שליליות, קריאה לכוחות מרפאים, או כניסה למצבי תודעה גבוהים לצורך תקשורת עם העל-טבעי (למשל, ריקודי שמאנים).</li>
        <li>**כוח והגנה:** הכנה לקרב, הפגנת עוצמה, הרתעת יריבים, או חיזוק רוח הלוחמים (למשל, ריקוד ה"האקה" המפורסם של המאורים).</li>
        <li>**קשר עם הטבע:** בקשה לגשם, ברכה ליבול, חגיגת הקציר, או חיקוי תנועות בעלי חיים המקושרים לכוחות טבע.</li>
        <li>**פולחן והערצה:** דרך של תפילה, כניעה או הערצה לישויות אלוהיות או רוחות קדמונים (למשל, ריקוד הסמאע המעגלי של הדרווישים).</li>
        <li>**מעברי חיים:** ליווי ותיעוד אירועי חיים מרכזיים - לידה, התבגרות, נישואין, מוות - תוך חיבור הפרט לקהילה ולמסורת.</li>
    </ul>

    <h3>דוגמאות מרתקות לריקודים טקסיים מרחבי הגלובוס</h3>
    העולם הוא פסיפס של תנועה וקצב. הנה כמה דוגמאות מייצגות:
    <ul>
        <li>**אפריקה:** ריקודי קפיצות ראוותניים כמו ה"אדמו" של המאאסאי (מזרח אפריקה), ריקודים מסכות במערב אפריקה הקשורים לרוחות האבות, וריקודי חניכה והתבגרות.</li>
        <li>**אסיה:** ריקודים קלאסיים מקודשים כמו ה"לגונג" מבאלי (אינדונזיה), ריקודי טקסים במנזרים בנפאל ובטיבט, ריקודים שאמאניים בסיביר וקוריאה, והסמאע הסופי (טורקיה, מרכז אסיה).</li>
        <li>**אוקיאניה:** ההאקה הניו זילנדי, ריקודי מלחמה ורוחות בפפואה גינאה החדשה, וריקודים מסורתיים באיי פולינזיה.</li>
        <li>**אמריקה:** ריקוד הרוח (Ghost Dance) ההיסטורי של שבטים ילידים בצפון אמריקה, ריקודים אזטקיים ומאיה ששרדו, וריקודים כמו הקפוארה בברזיל שנוצרו על ידי צאצאי עבדים וקיבלו משמעות רוחנית והגנתית.</li>
        <li>**אירופה:** ריקודי אבירים (Morris Dance) באנגליה, ריקודים עממיים קדומים הקשורים למחזורי הטבע באירופה הסלאבית והסקנדינבית.</li>
    </ul>

    <h3>כיצד הריקוד חושף ערכים ואמונות תרבותיות</h3>
    ריקוד טקסי הוא שפה חיה של תרבות. כל תנועה, צליל, לבוש או אביזר טומנים בחובם משמעות עמוקה ומספרים את סיפורה של הקהילה:
    <ul>
        <li>**מבנה חברתי:** מי רוקד, מתי ואיפה - יכול לשקף היררכיה, תפקידים מגדריים או מעמדות בתוך החברה.</li>
        <li>**קשר עם היקום:** חיקויים של חיות, תופעות טבע או גופים שמימיים מבטאים את תפיסת העולם האקולוגית והקוסמולוגית.</li>
        <li>**זיכרון היסטורי ומיתי:** הריקוד משמר ומעביר מדור לדור סיפורי בריאה, אגדות עם, מלחמות היסטוריות וזיכרונות קולקטיביים.</li>
        <li>**אתיקה וערכים:** דגש על סנכרון, שיתוף פעולה, תחרותיות בריאה או ביטוי אינדיבידואלי - משקפים את הערכים החברתיים המרכזיים.</li>
    </ul>

    <h3>שימור ריקודים טקסיים: מורשת בתנועה</h3>
    בעידן הגלובליזציה והשינוי המואץ, ריקודים טקסיים רבים ניצבים בפני אתגרים קיומיים. אובדן ידע, הגירה, שינויים באורחות חיים - כולם מאיימים על העברת המסורת. שימור ריקודים אלו אינו רק שמרנות, אלא צורך קריטי:
    <ul>
        <li>הם אוצרות תרבותיים המגלמים ידע אנושי ייחודי ומגוון.</li>
        <li>הם מחזקים את הזהות והשייכות של קהילות, ומסייעים להן לשמור על הקשר לשורשיהן.</li>
        <li>הם מהווים מקור השראה אמנותי ורוחני לעולם כולו.</li>
        <li>תיעודם, לימודם ותמיכה בקהילות המקיימות אותם הם מפתח להבנה עמוקה יותר של האנושות בכללותה.</li>
    </ul>
    תמיכה בשימור ריקודים אלו היא תמיכה בגיוון התרבותי העולמי ובזכותן של קהילות לספר את סיפורן בתנועה.
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

    :root {
        --primary-color: #4A90E2; /* A vibrant blue */
        --secondary-color: #50E3C2; /* A light teal */
        --accent-color: #F5A623; /* An orange/yellow */
        --background-light: #F8F9FA; /* Light grey background */
        --surface-card: #FFFFFF; /* White for cards/containers */
        --text-dark: #333333; /* Dark grey for main text */
        --text-medium: #555555; /* Medium grey for descriptions */
        --text-light: #888888; /* Light grey */
        --success-color: #7ED321; /* Green */
        --error-color: #D0021B; /* Red */
        --border-color: #E0E0E0; /* Light grey border */
    }

    body {
        font-family: 'Rubik', sans-serif;
        line-height: 1.6;
        color: var(--text-dark);
        background-color: var(--background-light);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure RTL for Hebrew */
        text-align: right; /* Align text to the right */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }

    #dance-challenge-app {
        max-width: 700px; /* Slightly wider container */
        margin: 20px auto;
        padding: 30px;
        background-color: var(--surface-card);
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer shadow */
        overflow: hidden; /* Clear floats/margins */
    }

    .app-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 15px;
    }

    #question-title {
        margin: 0;
        font-size: 1.5rem;
        color: var(--text-dark); /* Make title less 'primary' within app */
    }

    #score-display {
        font-size: 1.2rem;
        font-weight: 500;
        color: var(--text-medium);
    }

    #dance-display {
        min-height: 200px; /* More space for image/visuals */
        margin-bottom: 25px;
        display: flex;
        flex-direction: column; /* Stack image and description */
        justify-content: center;
        align-items: center;
        background-color: #f1f1f1; /* A slightly darker grey */
        border-radius: 8px;
        padding: 20px;
        position: relative; /* For potential absolute positioning of media */
    }

    #dance-image-placeholder {
        width: 100%;
        max-height: 250px; /* Max height for the visual area */
        background-color: #e0e0e0; /* Placeholder background */
        border-radius: 6px;
        margin-bottom: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden; /* Hide overflow if image exceeds */
        /* In a real app, this would be an <img> or <video> */
    }

     #dance-image-placeholder svg.dance-icon {
        width: 60px;
        height: 60px;
        fill: var(--text-light);
        opacity: 0.5;
     }

    /* Style for actual image/video if added later */
    /*
    #dance-display img, #dance-display video {
        display: block;
        max-width: 100%;
        max-height: 100%;
        height: auto;
        border-radius: 6px;
        object-fit: contain;
    }
    */


    #dance-description {
        font-style: italic;
        color: var(--text-medium);
        font-size: 1rem;
        text-align: center; /* Center description */
        margin-top: 0; /* Adjust margin */
    }

    .options-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* Wider minimum buttons */
        gap: 15px; /* More space between buttons */
        margin-bottom: 25px;
    }

    .options-grid button {
        padding: 12px 20px; /* More padding */
        font-size: 1.1rem; /* Larger font */
        cursor: pointer;
        border: none; /* Remove default border */
        border-radius: 8px; /* More rounded */
        background-color: var(--primary-color);
        color: var(--surface-card); /* White text */
        transition: background-color 0.3s ease, transform 0.1s ease; /* Add transform transition */
        font-weight: 500;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Button shadow */
    }

    .options-grid button:hover:not(:disabled) {
        background-color: #3A7BD5; /* Darker primary on hover */
        transform: translateY(-2px); /* Slight lift effect */
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15); /* Larger shadow on hover */
    }

     .options-grid button:active:not(:disabled) {
        transform: translateY(0); /* Press down effect */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Smaller shadow on press */
     }

     .options-grid button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        box-shadow: none;
     }


    .feedback-area {
        margin-top: 20px;
        padding: 20px;
        border-top: 1px solid var(--border-color);
        background-color: #e9ecef; /* Light grey background for feedback */
        border-radius: 8px;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px);
        transition: opacity 0.5s ease, transform 0.5s ease;
    }

    .feedback-area.visible {
        opacity: 1;
        transform: translateY(0);
    }

    .feedback-text {
        font-weight: 700; /* Bolder */
        margin-bottom: 8px;
        font-size: 1.2rem; /* Larger font */
    }

    .feedback-area .correct {
        color: var(--success-color);
    }

    .feedback-area .incorrect {
        color: var(--error-color);
    }

    .explanation-text {
        color: var(--text-dark);
        font-size: 1rem;
        margin-bottom: 15px;
    }

    .action-button {
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 500;
        margin-top: 10px;
        display: inline-block; /* Allow side-by-side if needed */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .action-button.primary {
        background-color: var(--primary-color);
        color: var(--surface-card);
    }

    .action-button.primary:hover {
        background-color: #3A7BD5;
        transform: translateY(-1px);
    }

     .action-button.primary:active {
        transform: translateY(0);
     }

    .action-button.secondary {
        background-color: var(--text-light); /* Grey button */
        color: var(--surface-card);
        margin-left: 10px; /* Space for potential multiple buttons */
    }
     .action-button.secondary:hover {
        background-color: #777;
        transform: translateY(-1px);
     }
      .action-button.secondary:active {
        transform: translateY(0);
     }


    .quiz-complete {
        text-align: center;
        margin-top: 30px;
        padding: 20px;
        background-color: var(--secondary-color);
        color: var(--text-dark);
        border-radius: 8px;
        opacity: 0;
        transform: scale(0.9);
        transition: opacity 0.5s ease, transform 0.5s ease;
    }
     .quiz-complete.visible {
        opacity: 1;
        transform: scale(1);
     }

     .quiz-complete h3 {
        margin-top: 0;
        color: var(--text-dark);
     }

    .toggle-explanation-button {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* More padding */
        font-size: 1rem;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--text-medium); /* Grey color */
        color: var(--surface-card);
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 500;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .toggle-explanation-button:hover {
        background-color: #666;
        transform: translateY(-2px);
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
    }
     .toggle-explanation-button:active {
        transform: translateY(0);
     }


    .full-explanation {
        max-width: 700px; /* Match app width */
        margin: 20px auto 40px auto; /* More bottom margin */
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--surface-card);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        line-height: 1.7;
    }

    .full-explanation h2, .full-explanation h3 {
        color: var(--primary-color);
        margin-top: 25px; /* More space above headings */
        margin-bottom: 12px;
        text-align: right; /* Align explanation text right */
    }

    .full-explanation ul {
        margin-bottom: 20px;
        padding-right: 20px; /* RTL padding */
        padding-left: 0;
        list-style: disc outside; /* Standard disc list */
    }

    .full-explanation li {
        margin-bottom: 10px;
        line-height: 1.6;
        color: var(--text-dark);
    }

    /* Optional: Add a subtle animation for elements appearing */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    /* Example usage: .feedback-area.visible { animation: fadeIn 0.5s ease forwards; } */

</style>

<script>
    // Data structure including image placeholders (replace with actual URLs in a real deployment)
    const questions = [
        {
            type: 'description',
            description: 'ריקוד שבטי ממזרח אפריקה הידוע בקפיצות לגובה מרהיבות של הרקדנים הגברים, לעיתים קרובות במעגל. משמש לעיתים קרובות כהוכחה לגבריות וכושר גופני, וגם בטקסי מעבר חשובים.',
            imageUrl: 'https://via.placeholder.com/400x200?text=Maasai+Jump+Dance', // Placeholder image URL
            options: ['ריקוד הזולו (דרום אפריקה)', 'ריקוד המאאסאי (Adumu) (מזרח אפריקה)', 'ריקוד היורובה (מערב אפריקה)'],
            correctAnswerIndex: 1,
            explanation: 'זהו תיאור מדויק של ריקוד ה-Adumu המפורסם של בני המאאסאי מקניה וטנזניה. ריקוד הקפיצה הוא מרכיב מרכזי בטקסי המעבר לבחורים צעירים.',
        },
        {
            type: 'description',
            description: 'ריקוד תיאטרלי מורכב מאינדונזיה המבוצע על ידי נערות צעירות בלבד, המאופיין בתנועות ידיים, אצבעות ועיניים עדינות, מדויקות ובעלות משמעות. הוא מספר סיפורים מיתולוגיים עשירים והיה בעבר נחלתה הבלעדית של משפחת המלוכה.',
             imageUrl: 'https://via.placeholder.com/400x200?text=Balinese+Legong+Dance', // Placeholder image URL
            options: ['ריקוד קלאסי תאילנדי', 'ריקוד באלינזי (Legong)', 'ריקוד הודי קלאסי (Bharatanatyam)'],
            correctAnswerIndex: 1,
            explanation: 'זהו תיאור של ריקוד ה-Legong מבאלי, אינדונזיה. הוא ידוע בתנועותיו המיניאטוריות והמפורטות ומבוצע על ידי רקדניות צעירות המגלמות דמויות מסיפורי המיתולוגיה ההינדואית המקומית.',
        },
        {
            type: 'description',
            description: 'תנועה רוחנית וריקוד שהתפתח בקרב שבטים ילידים באמריקה הצפונית בשלהי המאה ה-19, כתגובה לדיכוי הקולוניאלי. מטרתו הייתה להחזיר את המתים, לגרש את הפולשים הלבנים ולהשיב את דרך החיים המסורתית האבודה. בוצע לרוב במעגלים, תוך כדי שירה ותפילה אינטנסיבית.',
             imageUrl: 'https://via.placeholder.com/400x200?text=Ghost+Dance+Symbol', // Placeholder image URL
            options: ['ריקוד אזטקי עתיק', 'ריקוד הרוח (Ghost Dance)', 'ריקוד האינואיט (צפון קנדה)'],
            correctAnswerIndex: 1,
            explanation: 'זהו תיאור של ריקוד הרוח (Ghost Dance), תנועה משיחית שביטאה את הייאוש והתקווה להתחדשות בקרב שבטים ילידים רבים לאחר תבוסות צבאיות ואובדן אדמות בסוף המאה ה-19.',
        },
         {
            type: 'description',
            description: 'ריקוד מדיטטיבי טקסי שמקורו במסדר מיסטי (סופי) באנטוליה (טורקיה). הרקדנים, לבושים בבגדים מסורתיים, מסתובבים סביב צירם המרכזי באטיות ובהדרגה, כשיד ימין מושטת מעלה לקבלת ברכה מהקוסמוס, ויד שמאל כלפי מטה להעברתה לאדמה. מטרתו להגיע למצב של השתחררות רוחנית ואחדות עם הבורא.',
            imageUrl: 'https://via.placeholder.com/400x200?text=Whirling+Dervishes', // Placeholder image URL
            options: ['ריקוד פרסי מיסטי (סופי)', 'ריקוד הדרווישים המסתובבים (סמאע)', 'ריקוד מצרי עתיק (כמו ריקוד הבטן)'],
            correctAnswerIndex: 1,
            explanation: 'זהו תיאור של ריקוד הסמאע המפורסם, המבוצע על ידי הדרווישים המסתובבים של המסדר המווילוויה (Mevlevi) שנוסד על ידי ג\'לאל א-דין רומי בטורקיה. זהו ריקוד עמוק, סמלי ומדיטטיבי במסגרת הפולחן הסופי.',
        }
    ];

    let currentQuestionIndex = 0;
    let score = 0;

    // Get DOM elements
    const danceDisplayEl = document.getElementById('dance-display');
    const danceImagePlaceholderEl = document.getElementById('dance-image-placeholder');
    // const danceImageEl = document.getElementById('dance-image'); // For actual images
    const danceDescriptionEl = document.getElementById('dance-description');
    const optionsContainerEl = document.getElementById('options-container');
    const feedbackAreaEl = document.getElementById('feedback-area');
    const feedbackTextEl = document.getElementById('feedback-text');
    const explanationTextEl = document.getElementById('explanation-text');
    const nextButtonEl = document.getElementById('next-question-button');
    const showExplanationButtonEl = document.getElementById('show-explanation-button');
    const fullExplanationEl = document.getElementById('full-explanation');
    const scoreDisplayEl = document.getElementById('current-score');
    const quizCompleteMessageEl = document.getElementById('quiz-complete-message');
    const finalScoreEl = document.getElementById('final-score');
    const restartButtonEl = document.getElementById('restart-quiz-button');

    function loadQuestion(index) {
        if (index >= questions.length) {
            endQuiz();
            return;
        }

        const q = questions[index];
        // Update title for current question number (optional but adds game feel)
        document.getElementById('question-title').textContent = `שאלה ${index + 1} מתוך ${questions.length}`;


        // Display description
        danceDescriptionEl.textContent = q.description;

        // Handle potential image/video display (using placeholder for now)
        // If you had real images:
        // danceImagePlaceholderEl.style.display = 'none'; // Hide placeholder icon
        // danceImageEl.src = q.imageUrl;
        // danceImageEl.style.display = 'block';

        // Using placeholder only:
        // You might want to change the placeholder content based on the question,
        // or simply keep the icon. For this example, we'll just ensure the icon is visible.
         danceImagePlaceholderEl.innerHTML = '<svg class="dance-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 1c.2-.8.7-1 1.4-1 .7 0 1.3.2 1.4 1l.8 3h.4c.9 0 1.7.7 1.7 1.7v.4l3 .8c.8.2 1 .7 1 1.4 0 .7-.2 1.3-1 1.4l-3 .8v.4c0 .9-.7 1.7-1.7 1.7h-.4l-.8 3c-.2.8-.7 1-1.4 1-.7 0-1.3-.2-1.4-1l-.8-3h-.4c-.9 0-1.7-.7-1.7-1.7v-.4l-3-.8c-.8-.2-1-.7-1-1.4 0-.7.2-1.3 1-1.4l3-.8v-.4c0-.9.7-1.7 1.7-1.7h.4l.8-3zM12 14c-3.9 0-7 3.1-7 7h14c0-3.9-3.1-7-7-7zM12 12c2.2 0 4-1.8 4-4s-1.8-4-4-4-4 1.8-4 4 1.8 4 4 4z"/></svg>';


        optionsContainerEl.innerHTML = ''; // Clear previous options
        q.options.forEach((option, i) => {
            const button = document.createElement('button');
            button.textContent = option;
            button.addEventListener('click', () => handleAnswer(i, q));
            optionsContainerEl.appendChild(button);
        });

        // Hide feedback and complete message
        feedbackAreaEl.style.display = 'none';
        feedbackAreaEl.classList.remove('visible'); // For animation
        nextButtonEl.style.display = 'none';
        quizCompleteMessageEl.style.display = 'none';
        quizCompleteMessageEl.classList.remove('visible'); // For animation

        enableOptions(true); // Enable buttons for the new question
    }

    function handleAnswer(selectedIndex, q) {
        enableOptions(false); // Disable buttons after answering

        feedbackAreaEl.style.display = 'block';
        // Add animation class
        setTimeout(() => { feedbackAreaEl.classList.add('visible'); }, 10); // Small delay to ensure display block applies

        explanationTextEl.textContent = q.explanation;

        if (selectedIndex === q.correctAnswerIndex) {
            feedbackTextEl.textContent = 'מעולה! זו התשובה הנכונה.';
            feedbackTextEl.className = 'feedback-text correct'; // Update class for styling
            score++; // Increase score
            scoreDisplayEl.textContent = score; // Update score display
        } else {
            feedbackTextEl.textContent = 'חבל, זו לא התשובה הנכונה. התשובה הנכונה היא: ' + q.options[q.correctAnswerIndex];
            feedbackTextEl.className = 'feedback-text incorrect'; // Update class for styling
        }

        // Highlight correct/incorrect options (optional but good feedback)
        optionsContainerEl.querySelectorAll('button').forEach((button, i) => {
             if (i === q.correctAnswerIndex) {
                button.style.backgroundColor = var(--success-color);
                button.style.color = var(--text-dark); // Or white depending on contrast
             } else if (i === selectedIndex) {
                 button.style.backgroundColor = var(--error-color);
                 button.style.color = var(--surface-card);
             }
             button.style.boxShadow = 'none'; // Remove shadow after answer
        });


        // Show next button after answer
        nextButtonEl.style.display = 'block';
    }

    function enableOptions(enable) {
        optionsContainerEl.querySelectorAll('button').forEach(button => {
            button.disabled = !enable;
            // Reset button styles when enabling
            if (enable) {
                 button.style.backgroundColor = ''; // Reset to CSS default
                 button.style.color = ''; // Reset to CSS default
                 button.style.boxShadow = ''; // Reset to CSS default
            }
        });
    }

    function goToNextQuestion() {
        currentQuestionIndex++;
        loadQuestion(currentQuestionIndex);
    }

    function endQuiz() {
        document.getElementById('question-title').textContent = `האתגר הסתיים!`; // Final title
        danceDisplayEl.innerHTML = ''; // Clear dance display area
        optionsContainerEl.innerHTML = ''; // Clear options
        feedbackAreaEl.style.display = 'none'; // Hide feedback
        feedbackAreaEl.classList.remove('visible');
        nextButtonEl.style.display = 'none';
        scoreDisplayEl.style.display = 'none'; // Hide live score

        // Show quiz complete message
        quizCompleteMessageEl.style.display = 'block';
        finalScoreEl.textContent = score;
        setTimeout(() => { quizCompleteMessageEl.classList.add('visible'); }, 10); // Animate in

    }

    function restartQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        scoreDisplayEl.textContent = score;
        scoreDisplayEl.style.display = 'inline'; // Show score again
        quizCompleteMessageEl.style.display = 'none'; // Hide complete message
        quizCompleteMessageEl.classList.remove('visible');
        loadQuestion(currentQuestionIndex);
    }


    // Event listeners
    nextButtonEl.addEventListener('click', goToNextQuestion);

    showExplanationButtonEl.addEventListener('click', () => {
        const isHidden = fullExplanationEl.style.display === 'none';
        fullExplanationEl.style.display = isHidden ? 'block' : 'none';
        showExplanationButtonEl.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק על ריקודים טקסיים';
        // Optional: Add a subtle animation to the explanation section
        if(isHidden) {
             fullExplanationEl.style.opacity = 0;
             setTimeout(() => { fullExplanationEl.style.opacity = 1; }, 50); // Fade in
        } else {
             // No need to animate hiding, just hide
        }
    });

    restartButtonEl.addEventListener('click', restartQuiz);

    // Initial load
    loadQuestion(currentQuestionIndex);

</script>