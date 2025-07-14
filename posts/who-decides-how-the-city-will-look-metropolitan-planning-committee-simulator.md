---
title: "מי קובע איך תיראה העיר? סימולטור ועדת תכנון"
english_slug: who-decides-how-the-city-will-look-metropolitan-planning-committee-simulator
category: "תכנון עירוני"
tags:
  - תכנון עירוני
  - קבלת החלטות
  - מדיניות ציבורית
  - ועדות תכנון
  - מטרופולין
---
<div class="intro-section">
    <h1>ברוכים הבאים לסימולטור ועדת התכנון המטרופולינית!</h1>
    <p class="lead">רגע לפני שתצללו לתוך הדיון, דמיינו את המטרופולין שלכם. האם אתם רואים בו גורדי שחקים מתנשאים, כבישים רחבים, פארקים ירוקים או שכונות קהילתיות? ההחלטות שיעצבו את עתיד המרחב העירוני שלנו מתקבלות בחדרים סגורים, על שולחן ועדת התכנון. כאן, בסימולטור זה, אתם עומדים לחוות ממקור ראשון את הכוח, המורכבות והאיזונים העדינים הכרוכים בקבלת החלטות תכנוניות בעלות השפעה עצומה.</p>
    <p>אתם חברי ועדה. שמעתם את הטיעונים, בחנתם את ההשלכות הפוטנציאליות, ועכשיו הכדור בידיים שלכם. <strong>איך תיראה העיר מחר?</strong></p>
</div>


<div id="simulator" class="interactive-panel">
    <h2>דיון בוועדת התכנון - הגיע זמן להחליט!</h2>
    <div id="scenario-container">
        <div id="scenario-title" class="scenario-heading"></div>
        <div id="scenario-description" class="scenario-text"></div>
    </div>

    <h3>קולות מהשטח: טיעונים בפני הוועדה</h3>
    <div id="stakeholders-arguments" class="arguments-list">
        <!-- Stakeholder arguments will be added here by JS -->
    </div>

    <h3>ההחלטה הגורלית שלך כחבר/ת ועדה:</h3>
    <div id="decision-options" class="decision-buttons-container">
        <!-- Decision buttons will be added here by JS -->
    </div>

    <div id="results" class="results-panel" style="display: none;">
        <h3>העתיד נחשף: השלכות ההחלטה שבחרת</h3>
        <div id="impact-description" class="impact-text"></div>
        <div id="policy-alignment" class="policy-text"></div>
        <button id="restart-sim" class="action-button restart-button">התחל סימולציה מחדש</button>
    </div>
</div>

<button id="toggle-explanation" class="action-button toggle-button">מצד אחד למגדלים, מצד שני לפארקים: מי ומה קובע בועדות התכנון? לחצו להסבר</button>

<div id="explanation" class="explanation-panel" style="display: none;">
    <h2>הסבר: עולם ועדות התכנון המטרופוליניות - להבין את מי שמחליט</h2>

    <h3>מבוא: מהי ועדת תכנון מטרופולינית ומדוע היא קריטית?</h3>
    <p>דמיינו את המטרופולין כגוף אחד ענק. ועדות התכנון המטרופוליניות (נקראות גם ועדות מחוזיות בישראל) הן המוח שחושב ברמה האזורית הזו. הן לא רק מתמקדות ברשות מקומית בודדת, אלא רואות את התמונה הרחבה: איפה יעברו מסילות רכבת קלה שיחברו ערים שכנות? איפה נקים פארק ענק שישרת מיליוני תושבים מכל האזור? ואיפה נבנה אלפי יחידות דיור כדי להתמודד עם מצוקת הדיור? הוועדה הזו היא הגוף הסטטוטורי המכריע בשאלות אלו, ומבטיחה תיאום וחשיבה ארוכת טווח מעבר לגבולות מוניציפליים צרים.</p>

    <h3>הרכב הוועדה: מי יושב בשולחן מקבלי ההחלטות? פסיפס של אינטרסים</h3>
    <p>השולחן הזה צפוף ומגוון. תמצאו שם נציגים ממשרדי ממשלה שונים (פנים, אוצר, תחבורה, סביבה ועוד) שלכל אחד אג'נדה משלו, ראשי ערים ומועצות מקומיות שמייצגים את התושבים והקופה המקומית, וגם אנשי מקצוע ומומחים - מתכנני ערים, אדריכלים, שמאים, משפטנים - ואפילו נציגי ציבור. כל אחד מביא לשולחן זווית ראייה אחרת, אינטרסים שונים, ולפעמים גם קונפליקטים בלתי נמנעים. זהו תהליך של הידברות, שכנוע, ולבסוף - הכרעה.</p>

    <h3>השחקנים המרכזיים בזירת התכנון: קולות המשפיעים על העתיד</h3>
    <ul>
        <li><strong>יזמים נועזים:</strong> לרוב גופים פרטיים (אך לפעמים גם ציבוריים) שמביאים את החזון ואת הכסף לפרויקטים ענקיים - שכונות מגורים חדשות, מרכזי קניות, או מגדלי משרדים. הם רואים את הפוטנציאל הכלכלי והפיתוחי.</li>
        <li><strong>רשויות מקומיות - השליחים שלכם:</strong> ראשי הערים והמועצות שמתמודדים יום יום עם צרכי התושבים המקומיים - ביוב, כבישים, גנים וגם הכנסות מארנונה. הם נאבקים למען העיר שלהם.</li>
        <li><strong>משרדי ממשלה - האסטרטגים הלאומיים:</strong> לכל משרד יש תוכניות ענק בתחומו - משרד התחבורה מתכנן כבישים ורכבות, משרד הסביבה מנסה לשמור על הטבע, האוצר חושב על כסף. הם מביאים את האינטרס הלאומי או המחוזי.</li>
        <li><strong>הציבור הרחב וארגונים אזרחיים - קול העם:</strong> תושבים שמודאגים מהרעש הצפוי, ועדי שכונות שחוששים מפגיעה באיכות החיים, או עמותות סביבתיות שנאבקות לשמור על כל עץ וכל שטח פתוח. הם משתמשים בכלים דמוקרטיים כמו הגשת התנגדויות כדי להשפיע.</li>
        <li><strong>מומחים וגורמי מקצוע - העיניים המקצועיות:</strong> הם מספקים את הנתונים, את התחזיות ואת חוות הדעת המקצועיות ביותר, כדי שהוועדה תוכל לקבל החלטה מבוססת ידע.</li>
    </ul>

    <h3>שיקולים מרכזיים על הכף: איזון בלתי פוסק</h3>
    <p>אין החלטה תכנונית פשוטה. כל הכרעה היא פשרה, תוצאה של איזון (לעיתים כואב) בין שיקולים מתחרים:</p>
    <ul>
        <li><strong>כסף מול איכות חיים:</strong> האם פרויקט יכניס הרבה כסף ויצור מקומות עבודה, גם אם הוא יפגע בנוף או יצור עומס?</li>
        <li><strong>בנייה מול טבע:</strong> איפה עובר הגבול בין הצורך לגדול ולהתפתח לבין השמירה על ריאות ירוקות, טבע ובריאות הציבור?</li>
        <li><strong>נוחות אישית מול טובת הכלל:</strong> האם נמנע סלילת כביש חיוני למטרופולין כי הוא עובר קרוב מדי לבתי שכונה ספציפית?</li>
        <li><strong>דיור מול תשתיות:</strong> האם נאשר בניית אלפי דירות לפני שפתרנו את בעיות התחבורה והביוב באזור?</li>
    </ul>

    <h3>מתחים וקונפליקטים אופייניים: הדרמה שמאחורי הפרוטוקולים</h3>
    <ul>
        <li><strong>קרבות על הקרקע:</strong> כל מטר קרקע הוא נכס. האם לבנות עליו דירות (נחוץ!), משרדים (מכניס כסף!), או פארק (נחוץ לא פחות!)?</li>
        <li><strong>צפיפות מול מרחב:</strong> מצוקת הדיור דורשת לבנות גבוה וצפוף, אבל מי גר ליד מגדל ענק יודע שזה בא במחיר.</li>
        <li><strong>האינטרס המקומי נגד האינטרס האזורי:</strong> אף ראש עיר לא רוצה "מתקן מטרד" כמו תחנת מעבר לאשפה או כביש מהיר שחותך את העיר, גם אם הוא חיוני למטרופולין כולו.</li>
    </ul>

    <h3>השפעת ההחלטות: העתיד נבנה כאן ועכשיו</h3>
    <p>ההחלטות של ועדות התכנון הן לא רק ניירת בפרוטוקולים. הן מעצבות באופן יומיומי את חיינו: כמה זמן ניקח להגיע לעבודה, איפה הילדים ישחקו אחרי הצהריים, כמה זיהום אוויר ננשום, וגם כמה יעלה לקנות או לשכור דירה. הן משפיעות על הקהילות שלנו, על הסביבה הטבעית שנותרה, ועל החוסן הכלכלי של האזור. כל הכרעה כאן מהדהדת שנים קדימה ומעצבת את מחר.</p>
</div>

<style>
    /* General Body and Layout */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: #eef2f7; /* Light blue-gray background */
        color: #333;
        direction: rtl; /* Ensure right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2, h3 {
        color: #0056b3; /* Darker blue for headings */
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2.2em;
        text-align: center;
        margin-bottom: 20px;
        color: #003366;
    }

    h2 {
        font-size: 1.8em;
        border-bottom: 2px solid #0056b3;
        padding-bottom: 5px;
        margin-bottom: 20px;
    }

    h3 {
        font-size: 1.4em;
        margin-top: 25px;
        margin-bottom: 10px;
        color: #007bff; /* Medium blue */
    }

    p {
        margin-bottom: 15px;
    }

    ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Adjust padding for RTL */
    }

    li {
        margin-bottom: 8px;
    }

    .lead {
        font-size: 1.1em;
        font-weight: bold;
        color: #555;
        text-align: center;
        max-width: 800px;
        margin: 0 auto 30px auto;
    }

    /* Panels - Simulator and Explanation */
    .interactive-panel, .explanation-panel {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        transition: all 0.5s ease-in-out;
    }

    /* Simulator Specifics */
    #scenario-container {
        background-color: #e9f5ff; /* Very light blue */
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 25px;
        border: 1px solid #cce5ff;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start below for slide-in */
        animation: fadeInSlideUp 0.6s ease-out forwards 0.2s; /* Animation delay */
    }

    .scenario-heading {
        font-size: 1.6em;
        color: #003366;
        margin-bottom: 10px;
        font-weight: bold;
    }

    .scenario-text {
        font-size: 1.1em;
        color: #444;
        font-style: italic;
    }

    /* Stakeholder Arguments */
    .arguments-list div {
        background-color: #f8f9fa; /* Light light gray */
        padding: 15px;
        margin-bottom: 12px;
        border-right: 5px solid #28a745; /* Green border for arguments */
        border-radius: 6px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        opacity: 0; /* Start hidden for animation */
        transform: translateX(-20px); /* Start left for slide-in */
        animation: fadeInSlideRight 0.5s ease-out forwards; /* Animation */
    }

    .arguments-list div:nth-child(odd) {
         border-right-color: #ffc107; /* Yellow border for alternating arguments */
         animation-delay: 0.3s; /* Stagger animation */
    }
     .arguments-list div:nth-child(even) {
         border-right-color: #007bff; /* Blue border for alternating arguments */
         animation-delay: 0.5s; /* Stagger animation */
    }


    .arguments-list strong {
        color: #0056b3; /* Match heading color */
        font-size: 1.1em;
        display: block; /* Make name a block */
        margin-bottom: 5px;
    }

    /* Decision Buttons */
    .decision-buttons-container {
        display: flex;
        flex-wrap: wrap;
        gap: 15px; /* Space between buttons */
        margin-top: 20px;
        justify-content: center; /* Center buttons */
    }

    .decision-buttons-container button {
        padding: 12px 25px;
        border: none;
        border-radius: 30px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        background-color: #28a745; /* Green */
        color: white;
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.2);
        opacity: 0; /* Start hidden for animation */
        animation: scaleIn 0.4s ease-out forwards; /* Animation */
    }
     .decision-buttons-container button:nth-child(1) { animation-delay: 0.8s; }
     .decision-buttons-container button:nth-child(2) { animation-delay: 1s; background-color: #dc3545; box-shadow: 0 4px 8px rgba(220, 53, 69, 0.2); } /* Red */
     .decision-buttons-container button:nth-child(3) { animation-delay: 1.2s; background-color: #ffc107; box-shadow: 0 4px 8px rgba(255, 193, 7, 0.2); color: #333; } /* Yellow */


    .decision-buttons-container button:hover {
        transform: translateY(-3px); /* Lift effect on hover */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .decision-buttons-container button:active {
        transform: translateY(0); /* Press effect */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Results Section */
    .results-panel {
        margin-top: 30px;
        padding: 25px;
        background-color: #d4edda; /* Light green for results */
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        color: #155724; /* Dark green text */
        opacity: 0; /* Start hidden for animation */
        transform: scale(0.9); /* Start smaller for animation */
        animation: fadeInScaleUp 0.6s ease-out forwards; /* Animation */
    }

    .results-panel h3 {
        color: #0f571d; /* Darker green heading */
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 2px solid #155724;
        padding-bottom: 5px;
    }

    .impact-text {
         margin-bottom: 15px;
         font-weight: bold;
    }

    .policy-text {
        font-style: italic;
        color: #155724;
    }


    /* Action Buttons - Toggle & Restart */
    .action-button {
        display: block;
        width: fit-content;
        margin: 20px auto;
        padding: 12px 25px;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        background-color: #6c757d; /* Gray */
        color: white;
        box-shadow: 0 4px 8px rgba(108, 117, 125, 0.2);
    }

    .action-button:hover {
        background-color: #5a6268;
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .action-button:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .restart-button {
        margin-top: 20px;
        background-color: #007bff; /* Blue */
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
    }
     .restart-button:hover {
        background-color: #0056b3;
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
     }

    /* Explanation Panel */
    .explanation-panel h2 {
        border-bottom-color: #007bff; /* Match medium blue */
    }
     .explanation-panel h3 {
        color: #0056b3; /* Match darker blue */
     }

    /* Animations */
    @keyframes fadeInSlideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

     @keyframes fadeInSlideRight {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }

     @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
     }

      @keyframes fadeInScaleUp {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
      }

    /* Basic Responsiveness */
    @media (max-width: 768px) {
        body {
            padding: 15px;
        }
        h1 {
            font-size: 1.8em;
        }
        h2 {
            font-size: 1.5em;
        }
        h3 {
            font-size: 1.2em;
        }
        .interactive-panel, .explanation-panel {
            padding: 20px;
        }
        .decision-buttons-container {
            flex-direction: column; /* Stack buttons on small screens */
            gap: 10px;
        }
        .decision-buttons-container button, .action-button {
             width: 100%; /* Full width buttons */
             margin-left: 0;
             margin-right: 0;
        }
        .lead {
            font-size: 1em;
        }
    }

</style>

<script>
    const scenarios = [
        {
            title: "דיון סוער: עתיד לב המטרופולין בין פיתוח לשמירה על צביון",
            description: "על שולחן הוועדה מונחת תוכנית ענק ל'בינוי-פינוי' בשכונה ותיקה במרכז העיר. התוכנית מציעה להחליף בניינים ישנים ודליי קומה במגדלי מגורים ומסחר מודרניים וצפופים. מדובר באלפי יחידות דיור חדשות ובשטחי תעסוקה נרחבים.",
            stakeholders: [
                { name: "קול היזם", argument: "העיר חייבת לגדול! הפרויקט הזה יספק אלפי דירות במקום הכי נכון במטרופולין, ימשוך עסקים חדשים ויזרים מיליונים לקופת העירייה. זו הזדמנות חד-פעמית לחדש את התשתיות הרקובות ולייצר צמיחה כלכלית דרמטית." },
                { name: "נציגי התושבים הוותיקים", argument: "אנחנו גרים כאן עשרות שנים. זאת השכונה שלנו, הקהילה שלנו. אתם הולכים להרוס לנו את הבית, ליצור פקקי ענק שאי אפשר יהיה לנשום בהם, ולהפוך את האזור לג'ונגל בטון. תנו לנו פתרונות דיור בשכונה, תשמרו על הירוק ותתכננו כמו שצריך!" },
                { name: "הקול הירוק (ארגון סביבתי)", argument: "הצפיפות המטורפת הזו תחנוק את העיר. איפה יהיו הפארקים? איפה העצים? איכות האוויר תתדרדר, הלחץ על המערכות האקולוגיות המעטות שנותרו יהיה בלתי נסבל. חייבים לחשוב סביבה, לא רק נדל"ן!" },
                { name: "נציג משרד התחבורה", argument: "אנחנו תומכים בציפוף במרכז, אבל רק אם יש פתרונות תחבורה אמיתיים. התוכנית הנוכחית לא מטפלת מספיק בעומסים הצפויים. חייבים להבטיח סלילת נתיבי תחבורה ציבורית יעילים ושבילי אופניים רחבים כחלק בלתי נפרד מהפרויקט." }
            ],
            decisions: [
                {
                    option: "לאשר את התוכנית המקורית - קדימה פיתוח!",
                    impact: "<strong>השלכות:</strong> פיתוח מהיר ויצירת אלפי יחידות דיור חדשות במרכז העיר. הגדלת הכנסות משמעותית לרשות המקומית. <strong>אך:</strong> סכנה מיידית לעומסי תנועה אדירים, פגיעה בלתי הפיכה בצביון השכונה, התנגדות ציבורית חריפה ופוטנציאל לירידה באיכות הסביבה המקומית.",
                    policy: "<strong>התאמה למדיניות:</strong> עולה בקנה אחד עם מדיניות ארצית ומחוזית של עיבוי וציפוף במרכזי מטרופולין, אך עשויה להתנגש עם עקרונות של תכנון מקיים וצדק חלוקתי."
                },
                {
                    option: "לדחות את התוכנית - לשמור על הקיים ועל הקהילה",
                    impact: "<strong>השלכות:</strong> שמירה על צביון השכונה והמרקם הקהילתי, רגיעה זמנית מצד התושבים. <strong>אך:</strong> עצירת פיתוח הכרחי, החמרה של מצוקת הדיור האזורית, הפסד הזדמנות כלכלית ענקית והכנסות לרשות המקומית, ולחץ פוליטי וכלכלי מהיזם והממשלה.",
                    policy: "<strong>התאמה למדיניות:</strong> סוטה ממדיניות הציפוף במרכז, עשויה להתפרש ככניעה ללחצים מקומיים על חשבון האינטרס המטרופוליני הרחב."
                },
                {
                    option: "להמליץ על שינויים מהותיים בתוכנית - לאזן בין הכל",
                    impact: "<strong>השלכות:</strong> יצירת פרויקט מאוזן יותר שמשלב יחידות דיור, מסחר, שטחים ציבוריים ירוקים נרחבים ופתרונות תחבורה מתקדמים. מתן מענה טוב יותר לצרכי התושבים הוותיקים ושמירה חלקית על איכות החיים. <strong>אך:</strong> תהליך ארוך ומורכב יותר מול היזם, דחיית מועד התחלת הבנייה, וצורך בהשקעה ציבורית משמעותית בתשתיות ושטחים ציבוריים.",
                    policy: "<strong>התאמה למדיניות:</strong> תואמת עקרונות תכנון מקיים וכוללני המשלב פיתוח עם אחריות חברתית וסביבתית, אך דורשת גמישות ומשא ומתן מצד כל השחקנים."
                }
            ]
        }
        // ניתן להוסיף תרחישים נוספים כאן במבנה זהה
    ];

    let currentScenarioIndex = 0;

    // Get element references
    const simulatorDiv = document.getElementById('simulator');
    const scenarioContainerDiv = document.getElementById('scenario-container'); // Use container for animation
    const scenarioTitleDiv = document.getElementById('scenario-title');
    const scenarioDescriptionDiv = document.getElementById('scenario-description');
    const stakeholdersArgumentsDiv = document.getElementById('stakeholders-arguments');
    const decisionOptionsDiv = document.getElementById('decision-options');
    const resultsDiv = document.getElementById('results');
    const impactDescriptionDiv = document.getElementById('impact-description');
    const policyAlignmentDiv = document.getElementById('policy-alignment');
    const restartButton = document.getElementById('restart-sim');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    function loadScenario(index) {
        const scenario = scenarios[index];

        // Reset for potential animations on reload (if multiple scenarios)
        scenarioContainerDiv.style.opacity = 0;
        scenarioContainerDiv.style.transform = 'translateY(20px)';
        stakeholdersArgumentsDiv.innerHTML = ''; // Clear previous arguments
        decisionOptionsDiv.innerHTML = ''; // Clear previous buttons
        resultsDiv.style.display = 'none'; // Hide results

        // Populate content
        scenarioTitleDiv.innerText = scenario.title;
        scenarioDescriptionDiv.innerText = scenario.description;

        // Animate scenario container in
        setTimeout(() => {
             scenarioContainerDiv.style.opacity = 1;
             scenarioContainerDiv.style.transform = 'translateY(0)';
        }, 50); // Small delay after clearing

        // Add stakeholder arguments with staggered animation
        scenario.stakeholders.forEach((stakeholder, idx) => {
            const argDiv = document.createElement('div');
            argDiv.innerHTML = `<strong>${stakeholder.name}:</strong> ${stakeholder.argument}`;
            // Set initial state for animation
            argDiv.style.opacity = 0;
            argDiv.style.transform = 'translateX(-20px)';
            stakeholdersArgumentsDiv.appendChild(argDiv);

            // Trigger animation with delay
            setTimeout(() => {
                 argDiv.style.opacity = 1;
                 argDiv.style.transform = 'translateX(0)';
                 argDiv.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out'; // Add transition property
            }, 200 + idx * 150); // Staggered delay
        });

        // Add decision buttons with staggered animation
        scenario.decisions.forEach((decision, idx) => {
            const button = document.createElement('button');
            button.innerText = decision.option;
            button.addEventListener('click', () => makeDecision(idx));

            // Set initial state for animation
            button.style.opacity = 0;
            button.style.transform = 'scale(0.8)';
            // Specific colors based on index for flair (can be linked to outcome type if data had it)
            if (idx === 1) button.style.backgroundColor = '#dc3545'; // Red
            if (idx === 2) { button.style.backgroundColor = '#ffc107'; button.style.color = '#333'; } // Yellow/Orange

            decisionOptionsDiv.appendChild(button);

             // Trigger animation with delay
            setTimeout(() => {
                 button.style.opacity = 1;
                 button.style.transform = 'scale(1)';
                 button.style.transition = 'opacity 0.4s ease-out, transform 0.4s ease-out, background-color 0.3s ease, box-shadow 0.3s ease'; // Add transition property
            }, 1000 + idx * 200); // Staggered delay after arguments
        });

        decisionOptionsDiv.style.display = 'flex'; // Ensure flex display is active
    }

    function makeDecision(decisionIndex) {
        const scenario = scenarios[currentScenarioIndex];
        const chosenDecision = scenario.decisions[decisionIndex];

        // Update results content
        impactDescriptionDiv.innerHTML = chosenDecision.impact; // Use innerHTML for bold tags
        policyAlignmentDiv.innerHTML = chosenDecision.policy; // Use innerHTML for bold tags

        // Hide decision options with animation
        decisionOptionsDiv.style.opacity = 0;
        decisionOptionsDiv.style.pointerEvents = 'none'; // Disable clicks during fade
         setTimeout(() => {
            decisionOptionsDiv.style.display = 'none';
             decisionOptionsDiv.style.opacity = 1; // Reset opacity for next time
             decisionOptionsDiv.style.pointerEvents = 'auto'; // Re-enable clicks
        }, 500); // Match fade out duration

        // Show results with animation
        resultsDiv.style.display = 'block';
        resultsDiv.style.opacity = 0; // Start hidden
        resultsDiv.style.transform = 'scale(0.9)'; // Start smaller
        setTimeout(() => {
            resultsDiv.style.opacity = 1;
            resultsDiv.style.transform = 'scale(1)';
        }, 600); // Delay slightly after buttons hide
    }

    function setupEventListeners() {
         if(restartButton) {
            restartButton.addEventListener('click', () => {
                currentScenarioIndex = 0; // Always restart from the first scenario
                loadScenario(currentScenarioIndex);
            });
         }

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            // Use max-height transition for smooth toggle
            if (isHidden) {
                explanationDiv.style.display = 'block';
                setTimeout(() => { // Delay to allow display:block to take effect
                    explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 30 + 'px'; // Scroll height + padding
                    explanationDiv.style.opacity = 1;
                }, 10);
            } else {
                 explanationDiv.style.maxHeight = '0';
                 explanationDiv.style.opacity = 0;
                 setTimeout(() => {
                    explanationDiv.style.display = 'none';
                 }, 500); // Match transition duration
            }

            toggleExplanationButton.innerText = isHidden ? 'הסתר הסבר על ועדות תכנון' : 'מצד אחד למגדלים, מצד שני לפארקים: מי ומה קובע בועדות התכנון? לחצו להסבר';
        });

        // Set initial state for explanation for max-height animation
        explanationDiv.style.maxHeight = '0';
        explanationDiv.style.overflow = 'hidden';
        explanationDiv.style.opacity = 0;
        explanationDiv.style.transition = 'max-height 0.5s ease-in-out, opacity 0.5s ease-in-out';

    }

    // Initial setup and load
    setupEventListeners();
    loadScenario(currentScenarioIndex); // Load the first scenario

</script>
```