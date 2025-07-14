---
title: "דילמת השימור: סימולטור החלטות צוות"
english_slug: preservation-dilemma-team-decision-simulator
category: "מיומנויות וחינוך / חשיבה ומחקר"
tags: [שימור היסטורי, עבודת צוות, פתרון בעיות, ניהול פרויקטים, תכנון עירוני]
---
# דילמת השימור: קבלו החלטות קריטיות והצילו את ההיסטוריה

**מבנה היסטורי בעל חשיבות עצומה עומד על סף קריסה.** הוא נתון לאיומים מכל כיוון: הזנחה מתמשכת, לחץ כבד מצד יזמי נדל"ן, וסכנה פיזית מיידית. אתם עומדים בראש צוות מצומצם של מומחים, כל אחד עם רקע, אג'נדה ואינטרסים שונים בתכלית. אדריכל, מהנדס, היסטוריון, כלכלן ונציג קהילה – כולם מסתכלים עליכם.

האם תצליחו לנווט בין דעות סותרות, אילוצים כלכליים וסיכונים מבניים כדי לקבל את ההחלטות שיצילו את המבנה? האם תוכלו להגיע לקונצנזוס שישרת גם את מורשת העבר וגם את צרכי ההווה והעתיד? עתיד המבנה ההיסטורי, ועמו פיסת היסטוריה חשובה, מונח על כתפיכם.

<div id="simulator-container">
    <div id="intro">
        <h2>ברוכים הבאים למשימה!</h2>
        <p>אתם רכז/ת צוות שימור האמון/ה על הצלת נכס היסטורי בקריסה. המצב קריטי, התקציב מוגבל, ולכל חבר צוות יש דעה משלו. כל החלטה שלכם תשפיע דרמטית על גורל המבנה והפרויקט. נתחו את המצב, הקשיבו לצוות, ובחרו בחוכמה. בהצלחה!</p>
        <button id="start-sim">התחל במשימה</button>
    </div>

    <div id="game" style="display: none;">
        <div id="stats">
            <h3>מצב הפרויקט:</h3>
            <div class="stat-item">
                <span class="stat-label">תקציב:</span> <span id="current-budget" class="stat-value"></span> ש"ח
            </div>
             <div class="stat-item">
                <span class="stat-label">סיכון קריסה:</span> <span id="current-risk" class="stat-value"></span>
            </div>
             <div class="stat-item">
                <span class="stat-label">מורל צוות/קהילה:</span> <span id="current-morale" class="stat-value"></span>
            </div>
        </div>
        <div id="scenario">
            <!-- Scenario text will be loaded here -->
        </div>
        <div id="options">
            <!-- Decision buttons will be loaded here -->
        </div>
        <div id="feedback">
            <p id="feedback-text"></p>
        </div>
         <div id="loading-spinner" style="display:none;"></div>
    </div>

    <div id="result" style="display: none;">
        <h2>סיכום המשימה</h2>
        <div id="final-outcome">
            <!-- Final outcome text will be loaded here -->
        </div>
        <h3>ההחלטות המרכזיות והשפעתן:</h3>
        <ul id="decisions-summary">
            <!-- Summary of decisions will be loaded here -->
        </ul>
        <button id="restart-sim" class="secondary-button">התחל מחדש</button>
    </div>
</div>

<style>
    /* Global styles and typography */
    body {
        font-family: 'Arial', sans-serif; /* Changed font */
        line-height: 1.6;
        direction: rtl;
        text-align: right;
        background-color: #f4f7f6; /* Light background */
        color: #333;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #2c3e50; /* Darker heading color */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2.2em;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
        display: inline-block; /* To make border only under text */
        margin: 0 auto 30px auto;
        width: auto;
        text-align: center;
        display: block;
    }

    h2 {
        font-size: 1.8em;
        color: #3498db; /* Primary color for section titles */
    }

    h3 {
        font-size: 1.4em;
        color: #555;
        margin-top: 20px;
    }

    p {
        margin-bottom: 15px;
    }

    /* Simulator Container */
    #simulator-container {
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* White background for content */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        border: 1px solid #e0e0e0; /* Light border */
    }

    #intro, #game, #result {
        margin-bottom: 20px;
    }

    /* Intro Screen */
    #intro {
        text-align: center;
    }
    #intro p {
        font-size: 1.1em;
        color: #555;
        margin-bottom: 25px;
    }


    /* Game Screen */
    #game {
        /* Add entry animation */
         opacity: 0;
         transform: translateY(20px);
         animation: fadeInSlideUp 0.5s ease-out forwards;
    }

    @keyframes fadeInSlideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }


    /* Stats Section */
    #stats {
        background-color: #ecf0f1; /* Light grey/blue */
        padding: 15px 20px; /* More padding */
        border-radius: 8px;
        margin-bottom: 20px;
        border-right: 4px solid #3498db; /* Accent border */
    }

     #stats h3 {
        margin-top: 0;
        color: #2c3e50;
        border-bottom: 1px dashed #bdc3c7; /* Separator */
        padding-bottom: 10px;
        margin-bottom: 15px;
        text-align: right; /* Align stats heading */
     }

    .stat-item {
        margin-bottom: 10px;
        display: flex; /* Use flexbox for layout */
        justify-content: space-between; /* Space out label and value */
        align-items: center;
        font-size: 1.1em;
    }

    .stat-label {
        font-weight: normal; /* Label is not bold */
        color: #555;
    }

    .stat-value {
        font-weight: bold;
        min-width: 80px; /* Ensure alignment */
        text-align: left; /* Align value to the left */
    }

    /* Stat color indicators */
    .stat-value.stat-green { color: #2ecc71; } /* Success */
    .stat-value.stat-orange { color: #f39c12; } /* Warning */
    .stat-value.stat-red { color: #e74c3c; } /* Danger */


    /* Scenario Section */
     #scenario {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #bdc3c7;
        margin-bottom: 20px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
     }

    #scenario h3 {
        margin-top: 0;
        color: #34495e; /* Dark blue/grey */
        margin-bottom: 15px;
    }
     #scenario p {
        color: #555;
        line-height: 1.7;
     }

    /* Options Buttons */
    #options {
        margin-top: 20px;
        display: grid;
        gap: 12px; /* More space between buttons */
    }

    #options button {
        padding: 15px 20px; /* More padding */
        border: none; /* No border */
        border-radius: 8px; /* More rounded */
        background-color: #3498db; /* Primary button color */
        color: white;
        font-size: 1.1em;
        cursor: pointer;
        text-align: right;
        direction: rtl;
        transition: background-color 0.2s ease, transform 0.1s ease; /* Smooth transitions */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Button shadow */
    }

    #options button:hover {
        background-color: #2980b9; /* Darker shade on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    #options button:active {
        background-color: #2471a3; /* Even darker on active */
        transform: translateY(1px); /* Press effect */
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    #options button:disabled {
        background-color: #bdc3c7; /* Grey out disabled buttons */
        cursor: not-allowed;
        box-shadow: none;
    }


    /* Feedback Section */
    #feedback {
        margin-top: 20px; /* More margin */
        padding: 15px; /* More padding */
        border-radius: 8px;
        /* Initial state for animation */
        opacity: 0;
        transform: translateY(10px);
        transition: opacity 0.4s ease-out, transform 0.4s ease-out;
    }

    #feedback.show {
         opacity: 1;
         transform: translateY(0);
    }

    #feedback p {
        margin: 0;
        font-size: 1.05em;
         color: #2c3e50;
    }

     /* Specific feedback colors - can add classes in JS if needed for different outcomes */
    .feedback-positive {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }

     .feedback-negative {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
     }

     .feedback-neutral {
         background-color: #fefefe;
         border: 1px solid #d0d0d0;
         color: #333;
     }

    /* Loading Spinner (basic) */
    #loading-spinner {
      border: 4px solid #f3f3f3;
      border-top: 4px solid #3498db;
      border-radius: 50%;
      width: 20px;
      height: 20px;
      animation: spin 1s linear infinite;
      margin: 20px auto;
      display: block;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }


    /* Result Screen */
    #result h2 {
        color: #2c3e50;
        text-align: center;
    }

    #final-outcome {
        margin-bottom: 25px;
        padding: 20px;
        border-radius: 8px;
        font-size: 1.2em;
        line-height: 1.8;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .outcome-success {
        border: 2px solid #28a745;
        background-color: #e9f7ef; /* Lighter green */
        color: #1e7e34;
    }

    .outcome-mixed {
        border: 2px solid #ffc107;
        background-color: #fff9eb; /* Lighter yellow */
        color: #a17c00;
    }

    .outcome-failure {
        border: 2px solid #dc3545;
        background-color: #fdedee; /* Lighter red */
        color: #c82333;
    }

    #decisions-summary {
        list-style: none; /* Remove default bullets */
        padding: 0;
        margin-right: 0;
        border-top: 1px dashed #bdc3c7;
        padding-top: 20px;
    }

    #decisions-summary li {
        margin-bottom: 20px; /* More space */
        padding-bottom: 15px;
        border-bottom: 1px solid #eee; /* Separator */
        font-size: 1em;
         color: #555;
    }
     #decisions-summary li:last-child {
        border-bottom: none;
        padding-bottom: 0;
        margin-bottom: 0;
     }

    #decisions-summary li strong {
        color: #34495e; /* Darker heading */
        display: block; /* Make heading a block */
        margin-bottom: 5px;
        font-size: 1.1em;
    }
     #decisions-summary li em {
         display: block;
         margin-top: 5px;
         font-size: 0.95em;
         color: #666;
     }


    /* Buttons */
    button {
        font-family: 'Arial', sans-serif;
    }

    #start-sim, #restart-sim {
        display: block;
        width: 100%;
        padding: 15px;
        background-color: #3498db; /* Primary button color */
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.2em; /* Larger font */
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
         margin-top: 20px;
    }

    #start-sim:hover, #restart-sim:hover {
        background-color: #2980b9;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }

    #start-sim:active, #restart-sim:active {
        background-color: #2471a3;
        transform: translateY(1px);
         box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
    }

     .secondary-button {
        background-color: #95a5a6 !important; /* Grey color */
         margin-top: 30px;
     }
      .secondary-button:hover {
        background-color: #7f8c8d !important;
      }
       .secondary-button:active {
        background-color: #738283 !important;
       }


    #toggle-explanation {
        display: block;
        width: 100%;
        margin-top: 30px; /* More space */
        padding: 15px;
        background-color: #6c757d; /* Bootstrap secondary grey */
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.1em;
        cursor: pointer;
         transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: #5a6268;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
    }
    #toggle-explanation:active {
        background-color: #545b62;
        transform: translateY(1px);
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }


    /* Explanation Section */
    #explanation {
        margin-top: 30px; /* More space */
        padding-top: 30px;
        border-top: 2px solid #ddd;
        background-color: #ecf0f1; /* Match stats background */
        padding: 25px;
        border-radius: 8px;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
         opacity: 0; /* Initial state for animation */
         transform: translateY(20px);
         transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }
     #explanation.show {
         opacity: 1;
         transform: translateY(0);
     }


    #explanation h2, #explanation h3 {
        color: #2c3e50;
        text-align: right; /* Align explanation titles */
        margin-bottom: 15px;
    }
     #explanation h2 {
        border-bottom: 1px solid #bdc3c7;
        padding-bottom: 10px;
        margin-bottom: 20px;
     }


    #explanation p, #explanation ul {
        line-height: 1.7;
        color: #555;
    }

    #explanation ul {
        list-style: disc;
        padding-right: 20px; /* Standard list padding */
        margin-right: 0;
    }
     #explanation li {
         margin-bottom: 8px;
     }

</style>

<button id="toggle-explanation">הצג/הסתר הסבר על קבלת החלטות בצוות</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: ניהול צוות וקבלת החלטות בפרויקטי שימור</h2>

    <h3>מדוע קבלת החלטות בפרויקטי שימור היא אתגר מורכב?</h3>
    פרויקטי שימור הינם מיזמים רב-תחומיים מטבעם, הדורשים שילוב של ידע הנדסי, אדריכלי, היסטורי, כלכלי, משפטי וקהילתי. כל תחום מביא עמו סדרי עדיפויות ואינטרסים שונים, ולעיתים אף מנוגדים. הצורך לשמר אותנטיות עומד מול מגבלות תקציב, דרישות בטיחות מודרניות, ורצון הקהילה להתאים את המבנה לשימושים עכשוויים. תפקיד מנהל הפרויקט הוא לנווט בין הכוחות הללו, לנהל דיון פתוח ויעיל, ולהוביל את הצוות להחלטות המשרתות בצורה הטובה ביותר את המטרה הכוללת - הצלת המבנה והבטחת עתידו.

    <h3>אתגרים מרכזיים בקבלת החלטות קבוצתית:</h3>
    *   **קונפליקט אינטרסים ודעות:** כל מומחה רואה את הפרויקט דרך הפריזמה המקצועית שלו. האדריכל ידגיש שימור אסתטי, המהנדס יתמקד בבטיחות מבנית, הכלכלן יחשב עלויות, וההיסטוריון ידאג לאותנטיות. תפקידכם לרכז, להקשיב ולהכריע או לגשר.
    *   **מידע חלקי וחוסר ודאות:** בפרויקטי שימור, המצב המבני האמיתי מתגלה לעיתים רק במהלך העבודות. החלטות רבות מתקבלות תחת אי-ודאות לגבי העתיד (גיוס כספים, התפתחויות רגולטוריות).
    *   **לחצים חיצוניים:** יזמים, שכנים, הרשויות המקומיות והקהילה יכולים להפעיל לחץ משמעותי על תהליך קבלת ההחלטות, כל אחד עם סדר יום שונה.
    *   **הטיות קוגניטיביות ופסיכולוגיה של קבוצות:** תופעות כמו "חשיבת יחד" (Groupthink), הטיית אישוש (חיפוש מידע תומך לעמדה קיימת), או הסתמכות על 'מומחה' אחד גם בתחומים שאינם שלו, יכולות לפגוע באיכות ההחלטות.

    <h3>כלים ואסטרטגיות להחלטות אפקטיביות יותר:</h3>
    *   **שקיפות ותקשורת פתוחה:** עודדו כל חבר צוות להציג את עמדתו ונימוקיה בבהירות, תוך הקשבה פעילה לעמדות אחרות. יצירת סביבה בטוחה לדיון היא קריטית.
    *   **הגדרת מטרות ברורות:** ודאו שכל חברי הצוות מבינים ומסכימים על המטרות העיקריות של הפרויקט, גם אם יש חילוקי דעות על הדרך להשיגן.
    *   **ניתוח חלופות שיטתי:** אל תסתפקו באפשרות הראשונה שעולה. בחנו מספר דרכי פעולה לכל אתגר, העריכו את היתרונות והחסרונות של כל אחת (כולל עלויות, סיכונים והשפעה על בעלי עניין שונים).
    *   **ניהול סיכונים:** זהו מראש את הסיכונים האפשריים לכל החלטה (מבניים, כלכליים, תדמיתיים) והכינו תוכניות מגירה.
    *   **שיתוף בעלי עניין:** בהתאם לצורך ולאפשרויות, שלבו נציגי קהילה ובעלי עניין רלוונטיים בתהליך הדיון וההחלטה, או לפחות קיימו עמם התייעצויות. הדבר יכול להגדיל את התמיכה בפרויקט ולמנוע התנגדויות עתידיות.
    *   **פשרה ובניית קונצנזוס:** בפרויקטים מורכבים לרוב אין 'פתרון מושלם'. היו נכונים לשקול פשרות מושכלות המאזנות בין הצרכים השונים, גם אם אינן עונות על 100% מהדרישות של גורם זה או אחר. לעיתים, פתרון המקובל על הרוב (גם אם לא כולם מרוצים לחלוטין) עדיף על קיפאון או החלטה המתעלמת מאינטרסים חיוניים.

    פרויקט שימור מוצלח הוא לרוב תוצר של עבודת צוות מצוינת, תקשורת אפקטיבית ויכולת קבלת החלטות המשלבת ידע מקצועי, רגישות לבעלי עניין ויכולת ניהול סיכונים תחת לחץ.

</div>


<script>
    const startSimButton = document.getElementById('start-sim');
    const introScreen = document.getElementById('intro');
    const gameScreen = document.getElementById('game');
    const resultScreen = document.getElementById('result');
    const scenarioElement = document.getElementById('scenario');
    const optionsElement = document.getElementById('options');
    const statsElement = document.getElementById('stats');
    const budgetElement = document.getElementById('current-budget');
    const riskElement = document.getElementById('current-risk');
    const moraleElement = document.getElementById('current-morale');
    const finalOutcomeElement = document.getElementById('final-outcome');
    const decisionsSummaryElement = document.getElementById('decisions-summary');
    const feedbackElement = document.getElementById('feedback');
    const feedbackTextElement = document.getElementById('feedback-text'); // Get the p element inside feedback
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationElement = document.getElementById('explanation');
    const restartSimButton = document.getElementById('restart-sim');
    const loadingSpinner = document.getElementById('loading-spinner');


    let currentDecisionIndex = 0;
    let budget = 1000000; // Initial budget
    let risk = 50; // Initial risk percentage (0-100, higher is worse)
    let morale = 70; // Initial morale percentage (0-100, higher is better)
    const decisionsMade = [];

    const decisions = [
        {
            text: "<h3>ההחלטה הראשונה: חיזוק מבני או קוסמטיקה מיידית?</h3><p>מבדיקה ראשונית עולה כי יסודות הבניין חלשים במיוחד באגף הצפוני ויש סכנה ממשית לקריסה אם לא יטופל מיד. במקביל, חזית הבניין ההיסטורית מתפוררת, פוגעת בתדמית הפרויקט בעיני הקהילה המקומית והתורמים הפוטנציאליים ומייצרת חוסר אמון. המהנדס בצוות מתעקש שהטיפול ביסודות הוא קריטי ודחוף ביותר, גם אם יקר (400,000 ש\"ח). נציג הקהילה וההיסטוריון לעומת זאת לוחצים לטפל קודם בחזית (150,000 ש\"ח) כדי 'לייצר ווינ' מהיר ולהראות התקדמות לציבור.</p>",
            options: [
                {
                    text: "השקיעו את רוב הכסף מיד בחיזוק היסודות הקריטי (400,000 ש\"ח). בטיחות קודמת לתדמית.",
                    consequences: {
                        budgetChange: -400000,
                        riskChange: -30, // Reduces collapse risk significantly
                        moraleChange: -10, // Public/historian might be disappointed by lack of visible progress
                        outcomeText: "היסודות הקריטיים חוזקו בהצלחה! הסיכון לקריסה מיידית פחת משמעותית, המהנדס רגוע. הקהילה וההיסטוריון מאוכזבים מחוסר שינוי חיצוני בטווח הקצר."
                    },
                     feedbackClass: 'feedback-positive' // Indicate structurally positive
                },
                {
                    text: "השקיעו בשיקום חזית הבניין (150,000 ש\"ח). חשוב לבנות אמון ותמיכה ציבורית.",
                    consequences: {
                        budgetChange: -150000,
                        riskChange: +15, // Structural risk increases as nothing is done
                        moraleChange: +20, // Community and historians are happy with visible progress
                        outcomeText: "חזית הבניין שופצה ומסנוורת! המורל בקהילה גבוה, תורמים פוטנציאליים מתעניינים. עם זאת, המהנדס נראה מודאג מאוד מהיסודות החלשים."
                    },
                     feedbackClass: 'feedback-negative' // Indicate structurally negative
                },
                 {
                    text: "פצלו את התקציב: חלק קטן ליסודות (250,000 ש\"ח), חלק קטן יותר לחזית (100,000 ש\"ח). נסו לרצות את כולם חלקית.",
                    consequences: {
                        budgetChange: -350000,
                        riskChange: -15, // Partial risk reduction
                        moraleChange: +5, // Partial morale boost
                        outcomeText: "בוצע טיפול חלקי ביסודות ובחזית. המצב התייצב מעט בשני התחומים, אך לא נפתר לחלוטין. פשרה שהתקבלה עם גבות מורמות ע"י חלק מהצוות, אך יצרה תחושת התקדמות כלשהי."
                    },
                    feedbackClass: 'feedback-neutral' // Indicate a compromise
                }
            ]
        },
        {
            text: "<h3>ההחלטה השנייה: בחירת קבלן לשיקום הגג הדולף.</h3><p>הגג במצב רע מאוד ודולף, דבר הגורם נזקי מים מתמשכים ומסכן את המבנה מבפנים. יש לטפל בו בדחיפות כדי למנוע הרעה נוספת. קיבלנו שתי הצעות מחיר: קבלן א' הוא מומחה מוכר בשימור, בעל מוניטין והמלצות מצוינות, אך הצעתו יקרה מאוד (300,000 ש\"ח). קבלן ב' זול משמעותית (180,000 ש\"ח), אך ניסיונו בשימור מוגבל, בעיקר בבנייה חדשה. האדריכל וההיסטוריון דורשים לבחור בא', הכלכלן והמהנדס נוטים ל-ב' מטעמי עלות ומהירות ביצוע לכאורה.</p>",
            options: [
                {
                    text: "בחרו בקבלן א' המנוסה והיקר (300,000 ש\"ח). איכות בשימור שווה את המחיר.",
                    consequences: {
                        budgetChange: -300000,
                        riskChange: -10, // Lower risk of future problems/damage
                        moraleChange: +15, // Experts and preservationists are happy
                        outcomeText: "קבלן א' נבחר. הגג שוקם באופן מקצועי לפי תקני שימור מחמירים. העלות גבוהה, אך התוצאה איכותית, עמידה לאורך זמן, והצוות המקצועי מרוצה מאוד. התקציב ספג מכה."
                    },
                     feedbackClass: 'feedback-positive'
                },
                {
                    text: "בחרו בקבלן ב' הזול יותר (180,000 ש\"ח). חיסכון תקציבי הוא עדיפות עליונה כעת.",
                    consequences: {
                        budgetChange: -180000,
                        riskChange: +10, // Higher risk of future leaks or non-authentic work
                        moraleChange: -10, // Experts are concerned
                        outcomeText: "קבלן ב' נבחר. העלות נמוכה משמעותית, אך איכות העבודה בשימור מפוקפקת. הגג עדיין זקוק למעקב צמוד וייתכנו נזילות עתידיות. הצוות המקצועי חושש מתוצאות הטווח הארוך."
                    },
                     feedbackClass: 'feedback-negative'
                },
                 {
                    text: "נסו לנהל משא ומתן אגרסיבי עם קבלן א' להורדת מחיר משמעותית תמורת צמצום קל באלמנטים פחות היסטוריים (260,000 ש\"ח).",
                    consequences: {
                        budgetChange: -260000,
                        riskChange: -8, // Slightly less risk reduction than full scope
                        moraleChange: +10, // Experts are mostly happy, budget is slightly better
                        outcomeText: "משא ומתן צלח מעבר לצפוי! קבלן א' הסכים למחיר נוח יותר תמורת גמישות קלה. הגג טופל ברמה גבוהה עם פשרה מינורית בלבד. פתרון התקבל בברכה על ידי רוב חברי הצוות."
                    },
                    feedbackClass: 'feedback-neutral'
                }
            ]
        },
        {
            text: "<h3>ההחלטה השלישית: גיוס תרומות המונים או צמצום היקף דרמטי?</h3> <p>התקציב מתחיל להידלדל בקצב מהיר והפרויקט זקוק לזריקת מזומנים משמעותית כדי להמשיך לטפל באיומים המבניים שנותרו ולשקם אלמנטים פנימיים. יש שתי דרכים עיקריות להשיג מימון נוסף: לפתוח בקמפיין גיוס תרומות המונים מהציבור הרחב (פוטנציאל למימון גדול מאוד ושיפור עצום במורל הקהילה, אך תהליך ארוך, יקר התחלתי ולא ודאי), או לצמצם משמעותית את היקף השימור המתוכנן ולהתמקד רק בחיוני ביותר (מהיר, חוסך כסף, אך פוגע באותנטיות, בשימושיות העתידית ובמורל הצוות המקצועי).</p>",
            options: [
                {
                    text: "צאו בקמפיין גיוס תרומות המונים ציבורי (עלות התחלתית: 20,000 ש\"ח. הצלחה לא ודאית, תוצאות בטווח הבינוני).",
                    consequences: {
                        budgetChange: -20000, // Cost to run campaign
                        riskChange: -5, // Lower risk if successful funding is secured later
                        moraleChange: +25, // High morale boost if campaign starts well
                        outcomeText: "קמפיין גיוס התרומות יצא לדרך בסערה תקשורתית! הקהילה המקומית ואוהדי שימור בארץ מגיבים בהתלהבות ראשונית ומפגינים תמיכה. האתגר הוא לשמר את המומנטום ולתרגם אותו לכסף בפועל. התקציב הנוכחי המשיך להידלדל בינתיים ללא תגבורה מיידית."
                    },
                     feedbackClass: 'feedback-neutral' // Outcome depends on future success
                },
                {
                    text: "צמצמו את היקף השימור המתוכנן, וותרו על שחזורים מורכבים ופחות קריטיים. (חיסכון מיידי: 100,000 ש\"ח).",
                    consequences: {
                        budgetChange: +100000, // Saved by cutting scope
                        riskChange: +5, // Some loss of structural integrity/authenticity for neglected parts
                        moraleChange: -20, // Team experts (especially architect, historian) are unhappy with compromises
                        outcomeText: "התקבלה החלטה קשה לצמצם את היקף השימור כדי לעמוד בתקציב. נזנחו חלקים 'פחות חשובים' לשימור המבני, דבר שהקל מיידית על הקופה אך פגע באותנטיות וגרם לתסכול ואכזבה בקרב המומחים."
                    },
                     feedbackClass: 'feedback-negative'
                },
                {
                    text: "פנו מיידית לקרנות שימור ממשלתיות ואף לקרנות פילנתרופיות בינלאומיות בבקשה למימון חירום (סיכוי נמוך ודורש עבודה רבה, אך אם יצליח - בוסט גדול ללא עלות לכם).",
                     consequences: {
                        budgetChange: 0,
                        riskChange: -15, // If successful (assume moderate chance)
                        moraleChange: +10, // If successful application is seen positively
                        outcomeText: "פנייה מפורטת ומנומקת לקרנות מימון הוגשה. הצוות עבד קשה על הבקשה. סיכויי הקבלה אינם גבוהים וזה תהליך ארוך, אך אם המימון יאושר, הוא יפתור בעיות תקציב וסיכון רבות ויאפשר את המשך השיקום המלא ללא פשרות. כעת נותר רק לחכות לתשובה..."
                    },
                    feedbackClass: 'feedback-neutral'
                }
            ]
        },
         {
            text: "<h3>ההחלטה הרביעית: שיתוף הקהילה בתכנון עתידי או קבלת החלטות מהירה בצוות מצומצם?</h3> <p>השלב הנוכחי של השיקום המבני החיוני כמעט הסתיים, והגיע הזמן להחליט על השימוש העתידי במבנה לאחר שיקומו המלא. האפשרויות רבות (מרכז קהילתי, מוזיאון קטן, שטחי מסחר, מגורים ייחודיים) וכולן משפיעות על הצורך בהשקעות נוספות ועל עתיד המבנה. הקהילה המקומית מפגינה עניין רב ודורשת להיות שותפה מלאה בתהליך התכנון העתידי (יחזק דרמטית את הקשר עם הקהילה ויגדיל את הלגיטימציה והתמיכה הציבורית בפרויקט, אך יאריך משמעותית את התהליך, ידרוש תקציב נוסף לניהול שיתוף, ועלול ליצור קונפליקטים סביב הצרכים השונים). האדריכל והכלכלן מעדיפים לקבל החלטות מהירות יותר בתוך הצוות המצומצם כדי למנוע עיכובים, לחסוך בעלויות נוספות ולהתקדם לשלב הבא מהר ככל האפשר (יעיל, אך עלול לנתק את הפרויקט מהקהילה ולייצר התנגדות עתידית לתוכניות).</p>",
            options: [
                {
                    text: "ערכו תהליך שיתוף ציבור מלא ונרחב (ארוך ומורכב, עלות נוספת של כ-30,000 ש\"ח, מחזק קשר קהילתי ותמיכה עתידית).",
                    consequences: {
                        budgetChange: -30000, // Cost of public participation process
                        riskChange: -10, // Lower risk of public opposition or future conflicts
                        moraleChange: +25, // Strong morale boost from community engagement
                        outcomeText: "תהליך שיתוף ציבור נרחב יצא לדרך. הקהילה מגיבה בחיוב, מרגישה שייכות ומעורבת. התהליך מתקדם לאט יותר מהמתוכנן וגובה מחיר תקציבי, אך התמיכה הציבורית בפרויקט גבוהה והסיכוי למימוש מוצלח של השימוש העתידי גדל משמעותית."
                    },
                     feedbackClass: 'feedback-positive' // Positive for long-term success and morale
                },
                {
                    text: "קבלו את ההחלטות על השימוש העתידי בתוך הצוות המצומצם. יעילות ומהירות מעל הכול.",
                    consequences: {
                        budgetChange: 0, // No extra cost
                        riskChange: +10, // Higher risk of future public apathy or opposition
                        moraleChange: -15, // Community feels ignored, morale drops
                        outcomeText: "ההחלטות על עתיד המבנה התקבלו במהירות בתוך הצוות. התהליך היה יעיל וחסכוני בטווח הקצר, אך הקהילה אינה שותפה, חשה שהתעלמו ממנה ועלולה לגלות אדישות, חוסר תמיכה, או אף התנגדות לתוכניות העתידיות. הסיכון שהמבנה יישאר ריק או לא מנוצל כראוי גדל."
                    },
                     feedbackClass: 'feedback-negative'
                },
                 {
                    text: "ערכו מספר סדנאות מיקוד עם נציגי קהילה נבחרים. פשרה בין שיתוף מלא לקבלת החלטות בצוות (עלות מתונה: 10,000 ש\"ח).",
                    consequences: {
                        budgetChange: -10000, // Moderate cost
                        riskChange: -3, // Slight reduction in risk of opposition
                        moraleChange: +10, // Moderate morale boost
                        outcomeText: "סדנאות מיקוד עם נציגי הקהילה התקיימו. הקהילה חשה שהיא מקבלת יחס וזכות השפעה מסוימת, והצוות קיבל פידבק חשוב. זוהי פשרה יעילה יותר ופחות יקרה משיתוף מלא, שהתקבלה יחסית טוב על ידי רוב הגורמים המעורבים, למרות שחלק מהקהילה הרחבה עדיין חשה שהיא לא שותפה באמת."
                    },
                    feedbackClass: 'feedback-neutral'
                }
            ]
        }
        // Add more decisions here if needed
    ];

    function updateStats() {
        budgetElement.textContent = budget.toLocaleString();
        riskElement.textContent = `${risk}%`;
        moraleElement.textContent = `${morale}%`;

        // Apply color classes based on status
        budgetElement.classList.remove('stat-green', 'stat-orange', 'stat-red');
        riskElement.classList.remove('stat-green', 'stat-orange', 'stat-red');
        moraleElement.classList.remove('stat-green', 'stat-orange', 'stat-red');

        budgetElement.classList.add(budget < 100000 ? 'stat-red' : (budget < 300000 ? 'stat-orange' : 'stat-green'));
        // Risk is inverse: lower risk is green
        riskElement.classList.add(risk > 70 ? 'stat-red' : (risk > 40 ? 'stat-orange' : 'stat-green'));
         // Morale: higher is green
        moraleElement.classList.add(morale < 30 ? 'stat-red' : (morale < 60 ? 'stat-orange' : 'stat-green'));
    }

     function displayDecision(index) {
        // Fade out current content if not the first decision
        if (index > 0) {
            scenarioElement.style.opacity = 0;
            optionsElement.style.opacity = 0;
            feedbackElement.classList.remove('show'); // Hide feedback
             loadingSpinner.style.display = 'block'; // Show spinner during transition
        }


        setTimeout(() => { // Delay to allow fade out
            loadingSpinner.style.display = 'none'; // Hide spinner

            if (index >= decisions.length) {
                showResult();
                return;
            }

            const decision = decisions[index];
            scenarioElement.innerHTML = decision.text;
            optionsElement.innerHTML = ''; // Clear previous options

            decision.options.forEach((option, optionIndex) => {
                const button = document.createElement('button');
                button.textContent = option.text;
                button.addEventListener('click', () => handleDecision(option, index));
                optionsElement.appendChild(button);
            });

            updateStats();
            feedbackTextElement.textContent = ''; // Clear feedback text
            feedbackElement.className = ''; // Clear feedback classes


            // Fade in new content
            scenarioElement.style.opacity = 1;
            optionsElement.style.opacity = 1;
        }, index > 0 ? 400 : 0); // Short delay for subsequent decisions, no delay for first one
    }


    function handleDecision(chosenOption, decisionIndex) {
        const consequences = chosenOption.consequences;

         // Disable all option buttons
        optionsElement.querySelectorAll('button').forEach(btn => btn.disabled = true);

        // Apply consequences
        budget += consequences.budgetChange;
        risk += consequences.riskChange;
        morale += consequences.moraleChange;

        // Clamp stats within reasonable bounds
        risk = Math.max(0, Math.min(100, risk));
        morale = Math.max(0, Math.min(100, morale));

        // Record decision
        decisionsMade.push({
            decisionText: decisions[decisionIndex].text.split('<h3>')[1].split('</h3>')[0].trim(), // Extract title
            choiceText: chosenOption.text,
            outcomeText: consequences.outcomeText
        });

        // Display feedback
        feedbackTextElement.textContent = consequences.outcomeText;
         feedbackElement.className = 'show'; // Add show class for animation
         feedbackElement.classList.add(chosenOption.feedbackClass || 'feedback-neutral'); // Add feedback color class


        updateStats(); // Update stats display immediately

        // Wait a moment before moving to the next decision or result
        setTimeout(() => {
             // Re-enable buttons (though they will be replaced)
             optionsElement.querySelectorAll('button').forEach(btn => btn.disabled = false);
             currentDecisionIndex++;
             displayDecision(currentDecisionIndex);
        }, 2500); // Display feedback for 2.5 seconds
    }

    function showResult() {
        gameScreen.style.display = 'none';
        resultScreen.style.display = 'block'; // Result screen is already styled with fade-in animation via its container

        let outcomeText = "";
        let outcomeClass = "";

        // Determine outcome based on final stats
        if (risk > 70 || budget < 0 || morale < 30) { // Failure criteria
             outcomeText = "<h3>כישלון במשימה!</h3> למרבה הצער, הפרויקט נכשל בהצלת המבנה. ";
             if (risk > 70) outcomeText += `הסיכון המבני נשאר גבוה מדי (${risk}%) וגרם לעצירת הפרויקט או לנזק בלתי הפיך. `;
             if (budget < 0) outcomeText += "ניהול התקציב היה כושל והכספים אזלו לפני השלמת העבודות החיוניות. ";
             if (morale < 30) outcomeText += "מורל הצוות והקהילה צנח כל כך נמוך (${morale}%) עד שהפרויקט איבד תמיכה חיונית. ";
             outcomeText += "ההחלטות שקיבלתם לא הצליחו לאזן בין הצרכים השונים והמורכבים, וגורל המבנה נחרץ לרעה.";
             outcomeClass = "outcome-failure";
         } else if (risk > 40 || budget < 200000 || morale < 60) { // Mixed outcome criteria
             outcomeText = "<h3>תוצאה: הצלחה חלקית, אתגרים נותרו!</h3> הפרויקט הושלם, אך לא ללא פשרות והותיר אחריו אתגרים משמעותיים לעתיד. ";
             if (risk > 40) outcomeText += `הסיכון המבני עדיין גבוה מהרצוי (${risk}%), ודורש מעקב והשקעות נוספות. `;
             if (budget < 200000) outcomeText += `נותר סכום קטן בתקציב (${budget.toLocaleString()} ש"ח), מה שמקשה על תחזוקה עתידית או השלמות נדרשות. `;
             if (morale < 60) outcomeText += `מורל הצוות והקהילה נמוך יחסית (${morale}%), מה שעלול להקשות על מימוש השימוש העתידי במבנה. `;
             outcomeText += "הצלחתם להציל את המבנה מכיליון מיידי, אך עתידו לטווח ארוך עדיין אינו מובטח ודורש מאמצים נוספים.";
             outcomeClass = "outcome-mixed";
         }
         else { // Success criteria
             outcomeText = "<h3>ברכות, הצלחתם במשימה!</h3> למרות האתגרים הרבים, הצלחתם לנווט בין האינטרסים המנוגדים ולקבל סדרת החלטות חכמות שהצילו את המבנה ההיסטורי והבטיחו את עתידו. ";
             outcomeText += `המבנה יציב (סיכון ${risk}%), ניהלתם את התקציב ביעילות (נותר ${budget.toLocaleString()} ש"ח לשימושים עתידיים או תחזוקה), ומורל הצוות והקהילה גבוה (${morale}%), מה שמבטיח תמיכה בשימוש העתידי. `;
             outcomeText += "הצלחתם לאזן בהצלחה בין הצרכים ההנדסיים, הכלכליים, הקהילתיים והשימוריים. נכס חשוב ניצל בזכותכם לדורות הבאים!";
             outcomeClass = "outcome-success";
         }


        finalOutcomeElement.innerHTML = outcomeText;
        finalOutcomeElement.className = outcomeClass; // Add class for styling

        decisionsSummaryElement.innerHTML = '';
        decisionsMade.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${item.decisionText}:</strong> ${item.choiceText} <br> <em>תוצאה: ${item.outcomeText}</em>`;
            decisionsSummaryElement.appendChild(li);
        });
    }

    function resetGame() {
        currentDecisionIndex = 0;
        budget = 1000000;
        risk = 50;
        morale = 70;
        decisionsMade.length = 0; // Clear the array
        feedbackTextElement.textContent = '';
        feedbackElement.className = ''; // Clear feedback classes
        resultScreen.style.display = 'none';
        introScreen.style.display = 'block';
        gameScreen.style.display = 'none';
        updateStats(); // Reset stats display
    }

    startSimButton.addEventListener('click', () => {
        introScreen.style.display = 'none';
        gameScreen.style.display = 'block';
         gameScreen.style.opacity = 0; // Reset opacity for fade-in on start
         gameScreen.style.transform = 'translateY(20px)';
        displayDecision(currentDecisionIndex);
    });

     toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationElement.style.display === 'none';
        if (isHidden) {
             explanationElement.style.display = 'block';
             // Use a timeout to trigger the CSS transition after display is set to block
             setTimeout(() => explanationElement.classList.add('show'), 10);
             toggleExplanationButton.textContent = 'הסתר הסבר על קבלת החלטות בצוות';
        } else {
             explanationElement.classList.remove('show');
             // Use a timeout to hide after the transition
             setTimeout(() => explanationElement.style.display = 'none', 500); // Match CSS transition duration
             toggleExplanationButton.textContent = 'הצג/הסתר הסבר על קבלת החלטות בצוות';
        }
    });

    restartSimButton.addEventListener('click', resetGame);


    // Initial setup
    updateStats(); // Display initial stats (though hidden)

</script>
---