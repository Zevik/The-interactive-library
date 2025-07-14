---
title: "חיים על הכף: הדילמה האתית של ניסויים בבעלי חיים"
english_slug: lives-in-the-balance-ethical-dilemma-animal-testing
category: "פילוסופיה"
tags: [אתיקה, ניסויים בבעלי חיים, פילוסופיה של המדע, רווחת בעלי חיים, הכרעה מוסרית]
---
# חיים על הכף: הדילמה האתית של ניסויים בבעלי חיים

במרדף הבלתי פוסק אחר פריצות דרך מדעיות ורפואיות שיכולות להציל ולשפר חיי אדם, אנו ניצבים שוב ושוב בפני צומת דרכים מוסרי מורכב וכואב. האם מותר לנו לגרום סבל ליצורים חיים אחרים למען תועלתנו? שאלה זו עומדת בלב הדיון האתי סביב שימוש בבעלי חיים למטרות ניסוי.

<div id="animal-testing-simulation" class="simulation-container">
    <h2 class="simulation-title">ועדת האתיקה לניסויים בבעלי חיים</h2>
    <p class="simulation-intro">את/ה מוזמן/ת לגלם חבר/ה בוועדת האתיקה המרכזית. תפקידך הוא לבחון בקשות מדעיות לביצוע ניסויים בבעלי חיים ולהכריע האם לאשרן או לדחותן, תוך איזון קפדני בין שיקולים מוסריים, מדעיים וחברתיים. כל החלטה נושאת משקל כבד.</p>

    <div id="scenario-area">
        <div class="scenario-counter">תרחיש <span id="current-scenario-num">1</span> מתוך <span id="total-scenarios"></span></div>
        <div id="scenario-container" class="card">
            <div id="scenario-details">
                <h3 class="scenario-title">בקשת ניסוי: <span id="scenario-title-text"></span></h3>
                <p><strong>מטרת הניסוי:</strong> <span id="scenario-purpose"></span></p>
                <p><strong>מידת הסבל הצפוי לבעלי החיים:</strong> <span id="scenario-suffering"></span></p>
                <p><strong>מספר בעלי החיים המעורבים:</strong> <span id="scenario-animals"></span></p>
                <p><strong>סיכויי ההצלחה המוערכים:</strong> <span id="scenario-success"></span></p>
            </div>
            <div id="decision-buttons" class="decision-buttons">
                <button id="approve-btn" class="decision-button approve-button">אשר ניסוי</button>
                <button id="reject-btn" class="decision-button reject-button">דחה ניסוי</button>
            </div>
        </div>
    </div>

    <div id="feedback-container" class="card hidden feedback-container">
        <div class="feedback-icon-area">
             <!-- Icons will be added here by JS -->
        </div>
        <h3 class="feedback-title">השלכות והנימוקים להחלטתך:</h3>
        <p id="feedback-text"></p>
        <button id="next-scenario-btn" class="nav-button hidden">המשך לתרחיש הבא</button>
        <button id="restart-btn" class="nav-button hidden">התחל מחדש</button>
    </div>

    <div id="end-message" class="card hidden end-message">
        <h3 class="end-title">הסימולציה הסתיימה.</h3>
        <p>עברת על כל הבקשות. כפי שראית, ההחלטות בתחום ניסויים בבעלי חיים מורכבות ורבות ניואנסים. אין להן לרוב תשובה חד משמעית, והן מחייבות שקלול עדין וקשה של התועלת המדעית או הרפואית הפוטנציאלית אל מול המחיר המוסרי הכבד הנגרם לבעלי החיים המעורבים.</p>
         <button id="end-restart-btn" class="nav-button">התחל מחדש</button>
    </div>

</div>

<style>
    /* --- General Styling --- */
    .simulation-container {
        font-family: 'Arial', sans-serif; /* More specific font */
        max-width: 700px;
        margin: 30px auto; /* More vertical margin */
        padding: 25px; /* More padding */
        border: none; /* Remove default border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #eef2f7, #dce4f0); /* Subtle gradient background */
        direction: rtl;
        text-align: right;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Add shadow for depth */
        color: #333;
    }

    .simulation-container h2, .simulation-container h3 {
        color: #2c3e50; /* Darker, more professional heading color */
        text-align: center;
        margin-bottom: 15px; /* Space below headings */
    }

    .simulation-title {
        font-size: 2em; /* Larger title */
        font-weight: bold;
        margin-bottom: 10px;
    }

    .simulation-intro {
        font-size: 1.1em;
        line-height: 1.7;
        text-align: center;
        margin-bottom: 30px; /* More space before scenarios */
        color: #555;
    }

    /* --- Card Styling (for Scenario, Feedback, End Message) --- */
    .card {
        margin-top: 20px;
        padding: 20px; /* More padding */
        border: 1px solid #dcdcdc; /* Lighter border */
        border-radius: 8px; /* Consistent border radius */
        background-color: #ffffff; /* White background for cards */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Card specific shadow */
        transition: all 0.5s ease-in-out; /* Smooth transition */
        opacity: 1; /* Default visible state */
        transform: translateY(0); /* Default position */
    }

    .card.hidden {
        opacity: 0;
        max-height: 0; /* Collapse element */
        padding-top: 0;
        padding-bottom: 0;
        margin-top: 0;
        margin-bottom: 0;
        overflow: hidden; /* Hide content during collapse */
        border: none; /* Hide border when collapsed */
        pointer-events: none; /* Disable clicks */
        transition: all 0.5s ease-in-out, max-height 0.6s ease-in-out;
    }

    /* Style for the area containing the scenario details */
    #scenario-area {
         min-height: 250px; /* Ensure minimum height to prevent layout shifts */
    }


    .scenario-counter {
        text-align: center;
        font-size: 1.1em;
        font-weight: bold;
        color: #0056b3; /* A blue accent */
        margin-bottom: 15px;
    }

    .scenario-title {
        border-bottom: 2px solid #007bff; /* Highlight title */
        padding-bottom: 10px;
        margin-bottom: 15px;
        color: #007bff; /* Blue title */
    }

    #scenario-details p {
        margin-bottom: 12px; /* More space between details */
        line-height: 1.8; /* Improved readability */
        font-size: 1.05em;
        color: #444;
    }

    #scenario-details strong {
        color: #0056b3; /* Highlight labels */
    }

    /* --- Button Styling --- */
    .decision-buttons {
        text-align: center;
        margin-top: 25px; /* More space above buttons */
        padding-top: 15px;
        border-top: 1px solid #eee; /* Separator line */
    }

    .decision-button, .nav-button {
        padding: 12px 25px; /* More padding */
        margin: 8px; /* More margin */
        font-size: 1em; /* Base font size */
        cursor: pointer;
        border: none;
        border-radius: 5px; /* Slightly more rounded */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease; /* Smooth transitions */
        font-weight: bold;
        min-width: 120px; /* Minimum width for buttons */
    }

    .decision-button:hover, .nav-button:hover {
        transform: translateY(-2px); /* Subtle lift on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

     .decision-button:active, .nav-button:active {
        transform: translateY(0); /* Press effect */
        box-shadow: none;
    }

    .approve-button {
        background-color: #28a745; /* Bootstrap success green */
        color: white;
    }

    .approve-button:hover {
        background-color: #218838; /* Darker green on hover */
    }

    .reject-button {
        background-color: #dc3545; /* Bootstrap danger red */
        color: white;
    }

    .reject-button:hover {
        background-color: #c82333; /* Darker red on hover */
    }

    .nav-button {
         background-color: #007bff; /* Bootstrap primary blue */
         color: white;
         display: block; /* Make nav buttons block */
         margin: 20px auto 0 auto; /* Center block buttons */
         width: fit-content; /* Fit width to content */
         min-width: 150px; /* Ensure wider nav buttons */
    }

    .nav-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }

    /* --- Feedback Styling --- */
    .feedback-container {
        text-align: center; /* Center feedback text */
        background-color: #e9ecef; /* Light grey background for feedback */
        border-color: #ced4da;
        position: relative; /* Needed for icon positioning */
        min-height: 150px; /* Ensure feedback section has some height */
        display: flex; /* Use flexbox to center content vertically */
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

     .feedback-icon-area {
        position: absolute;
        top: 15px;
        left: 15px;
        font-size: 3em; /* Large icon */
        opacity: 0; /* Start hidden */
        transition: opacity 0.5s ease; /* Fade in */
     }

     .feedback-icon-area.visible {
         opacity: 1;
     }

    .feedback-icon-area .icon {
        display: inline-block; /* Or flex item */
     }

     .feedback-icon-area .approve-icon {
         color: #28a745; /* Green */
         content: "✅"; /* Checkmark icon */
     }

     .feedback-icon-area .reject-icon {
         color: #dc3545; /* Red */
         content: "❌"; /* Cross icon */
     }


    .feedback-title {
         color: #0056b3; /* Match nav button blue */
         margin-bottom: 10px;
    }

    #feedback-text {
        font-size: 1.1em;
        line-height: 1.7;
        color: #444;
        max-width: 80%; /* Limit text width for better centering */
        margin: 0 auto 20px auto; /* Center text block */
         text-align: center;
    }


    /* --- End Message Styling --- */
    .end-message {
         text-align: center; /* Center end message text */
         background-color: #cfe2ff; /* Lighter blue background */
         border-color: #b9d2ee;
    }

    .end-title {
        color: #0d6efd; /* Darker blue */
    }

     .end-message p {
        font-size: 1.1em;
        line-height: 1.7;
        color: #444;
        margin-bottom: 20px;
         text-align: center;
     }

    /* --- Explanation Styling --- */
    #toggle-explanation {
        display: block;
        margin: 30px auto; /* Center and add space */
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        background-color: #6c757d; /* Grey button */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
         width: fit-content;
    }

    #toggle-explanation:hover {
        background-color: #5a6268;
    }

    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #ccc;
        border-radius: 8px;
        background-color: #f8f9fa; /* Light grey background */
        direction: rtl;
        text-align: right;
         box-shadow: 0 4px 8px rgba(0,0,0,0.05);
         transition: all 0.5s ease-in-out;
         max-height: 1000px; /* Max height for transition */
         overflow: hidden;
    }

     #explanation.hidden {
         max-height: 0;
         padding-top: 0;
         padding-bottom: 0;
         margin-top: 0;
         margin-bottom: 0;
         opacity: 0;
     }

    #explanation h2 {
        color: #007bff;
        margin-bottom: 20px;
    }

     #explanation h3 {
        color: #0056b3;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px dotted #a0c0e0; /* Dotted separator */
        padding-bottom: 5px;
     }

    #explanation p {
        line-height: 1.8;
        margin-bottom: 15px;
        color: #333;
        font-size: 1.05em;
    }

     #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list */
     }

     #explanation li {
        margin-bottom: 8px;
        line-height: 1.6;
        color: #333;
     }

     #explanation strong {
        color: #0056b3;
     }


    /* --- Responsive Adjustments --- */
    @media (max-width: 600px) {
        .simulation-container, #explanation {
            padding: 15px;
            margin: 20px auto;
        }

        .decision-buttons button {
            width: calc(100% - 16px); /* Full width minus margin */
            margin: 5px 8px;
        }

         .decision-button, .nav-button {
             min-width: auto; /* Allow buttons to shrink */
             padding: 10px 15px;
         }

        .simulation-title {
            font-size: 1.6em;
        }

        .simulation-intro, #scenario-details p, #explanation p, #explanation li {
            font-size: 1em;
        }

        .feedback-icon-area {
             font-size: 2.5em;
             top: 10px;
             left: 10px;
        }
    }
</style>

<button id="toggle-explanation">הצג/הסתר רקע והסבר</button>

<div id="explanation" class="hidden">
    <h2>ניסויים בבעלי חיים: היבטים אתיים ומדעיים</h2>

    <h3>מהם ניסויים בבעלי חיים ומדוע הם נפוצים במרחב?</h3>
    <p>ניסויים בבעלי חיים הם הליכים מחקריים או בדיקות שונות המבוצעים על בעלי חיים חיים. השימוש בהם נפוץ במגוון תחומים: מחקר בסיסי להבנת תהליכים ביולוגיים, פיתוח ובדיקת בטיחות של תרופות וטיפולים רפואיים, בדיקת רעלנות של כימיקלים וחומרים, ופיתוח חיסונים. בעלי חיים משמשים במחקר מסיבות שונות, ביניהן: דמיון פיזיולוגי וגנטי לבני אדם (בעיקר יונקים כמו עכברים וחולדות), האפשרות לשלוט בסביבתם וגנטיקה שלהם בצורה מבוקרת, ומחזורי חיים קצרים יחסית המאפשרים מחקר על פני דורות.</p>

    <h3>טיעונים מרכזיים בעד ניסויים בבעלי חיים</h3>
    <p>הטיעון העיקרי בעד ניסויים בבעלי חיים הוא התועלת הפוטנציאלית העצומה לבריאות ולרווחת האדם. תרופות רבות, חיסונים, פרוצדורות כירורגיות והבנות בסיסיות של מחלות התפתחו בזכות מחקרים שכללו ניסויים בבעלי חיים. התומכים טוענים שבמקרים רבים, אין עדיין חלופות אמינות ובטוחות מספיק לבדיקת השפעות מורכבות של חומרים או טיפולים על מערכות ביולוגיות שלמות ואינטראקטיביות, כפי שקיימות בגוף חי. הם גם מציינים שהמחקר מתבצע תחת מגבלות רגולטוריות שמטרתן לצמצם את סבלם של בעלי החיים.</p>

    <h3>טיעונים מרכזיים נגד ניסויים בבעלי חיים</h3>
    <p>המתנגדים לניסויים בבעלי חיים מעלים טיעונים אתיים חזקים. הם מדגישים את הסבל הרב שנגרם למיליוני בעלי חיים מדי שנה כתוצאה מהניסויים - כאב, פחד, מצוקה פיזית ונפשית. טיעון נוסף הוא שיש לבעלי חיים זכויות בסיסיות, כולל הזכות שלא לשמש ככלי למטרות אדם, ושהשימוש בהם הוא הפרה של זכויות אלו. יש הטוענים גם שהתוצאות מניסויים בבעלי חיים אינן תמיד ניתנות להכללה מלאה לבני אדם עקב הבדלים ביולוגיים, ושעובדה זו מפחיתה מהתועלת הנטענת.</p>

    <h3>מסגרות רגולטוריות ואתיות: עקרון 3 ה-R ותפקידן של ועדות האתיקה</h3>
    <p>כדי לצמצם את ההשפעות השליליות של ניסויים בבעלי חיים, התפתחו בעולם מסגרות רגולטוריות ואתיות. עיקרון מרכזי הוא "עקרון 3 ה-R" (באנגלית: The 3 Rs):</p>
    <ul>
        <li><strong>Reduction (צמצום):</strong> שימוש במספר מינימלי של בעלי חיים הנדרש לקבלת תוצאות מהימנות.</li>
        <li><strong>Refinement (עידון):</strong> שיפור שיטות הניסוי כדי למזער כאב, מצוקה וסבל של בעלי החיים (למשל, שימוש במשככי כאבים, שיפור תנאי המחיה).</li>
        <li><strong>Replacement (החלפה):</strong> שימוש בשיטות חלופיות לניסויים בבעלי חיים בכל הזדמנות אפשרית (למשל, תרביות תאים, מודלים ממוחשבים).</li>
    </ul>
    <p>בישראל ובעולם, ניסויים בבעלי חיים דורשים אישור של ועדות אתיקה ייעודיות. ועדות אלו בוחנות כל בקשה לניסוי, מוודאות שהיא עומדת בעקרונות 3 ה-R, שהיא בעלת הצדקה מדעית, ושאין לה חלופות סבירות. תפקידן הוא לאזן בין התועלת המדעית או הרפואית הצפויה לבין המחיר המוסרי והסבל הנגרם לבעלי החיים.</p>

    <h3>הדילמה הפילוסופית: גישות אתיות שונות</h3>
    <p>הדיון על ניסויים בבעלי חיים נוגע בשאלות פילוסופיות עמוקות. גישות אתיות שונות מציעות דרכים שונות לגשת לדילמה:</p>
    <ul>
        <li><strong>תועלתנות (Utilitarianism):</strong> גישה זו מתמקדת בתוצאות. החלטה נכונה היא זו שממקסמת את מירב הטוב למירב האנשים (או היצורים בעלי היכולת לחוש כאב/הנאה). לפי גישה זו, ניסויים בבעלי חיים עשויים להיות מוצדקים אם התועלת לאדם (הפחתת סבל, הצלת חיים) עולה משמעותית על הסבל הנגרם לבעלי החיים.</li>
        <li><strong>דאונטולוגיה (Deontology):</strong> גישה זו מתמקדת בחובות ובזכויות, ללא קשר לתוצאות. לפי גישה זו, ליצורים מסוימים (אולי לכל היצורים בעלי התודעה או היכולת לחוש כאב) יש זכויות בסיסיות שאסור להפר אותן, כמו הזכות שלא להיות מנוצל או שיגרם לו סבל. מנקודת מבט דאונטולוגית, ניסויים בבעלי חיים עשויים להיות פסולים מעצם הפעולה, גם אם הם מביאים לתועלת רבה.</li>
    </ul>
    <p>ההכרעה בוועדות האתיקה ובחברה משקפת לעיתים קרובות ניסיון לאזן או לשלב שיקולים משתי הגישות הללו.</p>

    <h3>חלופות לניסויים בבעלי חיים והתקדמות טכנולוגית</h3>
    <p>התקדמות טכנולוגית פותחת אפיקים חדשים ומצמצמת את התלות בניסויים בבעלי חיים. חלופות כוללות: תרביות תאים (In Vitro), שימוש ברקמות אנושיות (למשל, עור מלאכותי), מודלים ממוחשבים מתוחכמים (In Silico) המדמים תהליכים ביולוגיים, ואף "איברים על שבב" (Organs-on-a-Chip) המדמים את המבנה והתפקוד של איברים אנושיים. למרות ההתקדמות, חלופות אלו עדיין אינן יכולות לחקות את המורכבות של אורגניזם שלם במקרים רבים, ולכן ניסויים בבעלי חיים עדיין נחשבים הכרחיים בשלבים מסוימים של מחקר ופיתוח, במיוחד לבדיקת בטיחות ויעילות מערכתית.</p>

    <h3>סיכום: הצורך בהמשך דיון ציבורי ומדעי</h3>
    <p>השימוש בבעלי חיים במחקר ופיתוח נשאר סוגיה אתית רגישה ומורכבת. בעוד שהם תרמו תרומה עצומה לרפואה ולבריאות הציבור, המחיר המוסרי הוא משמעותי. הדיון המתמשך, הן בקרב מדענים ואתיקנים והן בציבור הרחב, יחד עם השקעה בפיתוח חלופות, חיוניים להמשך התקדמות מדעית תוך מזעור הפגיעה בבעלי חיים.</p>
</div>

<script>
    const scenarios = [
        {
            title: "פיתוח תרופה למחלת הסרטן",
            purpose: "פיתוח ובדיקת יעילות ובטיחות של תרופה ניסיונית למחלת סרטן קטלנית שאין לה כיום טיפול יעיל. התרופה הראתה פוטנציאל מבטיח במחקרי מעבדה על תרביות תאים סרטניים.",
            suffering: "גבוהה מאוד (חשיפה לתרופה רעילה, גידולים, ירידה במשקל, כאב משמעותי)",
            animals: 200,
            success: "30%",
            feedback: {
                approve: "<strong>אושר:</strong> ועדת האתיקה שקלה את התועלת הפוטנציאלית להצלת חיי אדם רבים אל מול הסבל הצפוי לבעלי החיים המעטים יחסית. למרות הסיכון המשמעותי לבעלי החיים, סיכויי התגלית פורצת הדרך, במקרה של מחלה חשוכת מרפא, הכריעו את הכף.",
                reject: "<strong>נדחה:</strong> ועדת האתיקה קבעה כי סבלם הקיצוני של בעלי החיים בתרחיש זה נתפס כבלתי נסבל, גם נוכח הפוטנציאל התאורטי. ההחלטה מדגישה את הצורך למצות חלופות מחקר נוספות מעבר לתרביות תאים לפני שימוש בחיות בסבל כה גבוה."
            }
        },
        {
            title: "בדיקת בטיחות חומר קוסמטי חדש",
            purpose: "בדיקת גירוי עור ועיניים של רכיב חדש המיועד לשימוש בקרם לחות עממי. הבדיקה נדרשת ע\"פ תקנות בינלאומיות מסוימות טרם שיווק המוצר לציבור הרחב.",
            suffering: "בינונית (גירוי עור קל, אדמומיות, נפיחות זמנית באזור המריחה או הטפטוף)",
            animals: 50,
            success: "95%",
            feedback: {
                approve: "<strong>אושר:</strong> ההחלטה התבססה על העובדה שהבדיקה נדרשת רגולטורית להבטחת בטיחות הציבור הרחב המשתמש במוצר. הסבל הצפוי נתפס כסביר יחסית לתועלת במניעת נזק למשתמשים רבים, וצוין שנעשה מאמץ להשתמש במינימום בעלי חיים הנדרש ע\"פ פרוטוקול.",
                reject: "<strong>נדחה:</strong> ועדת האתיקה קבעה כי למרות הסיכוי הגבוה שהחומר בטוח והסבל הבינוני הצפוי, התועלת (מוצר קוסמטי שאינו מציל חיים) אינה מצדיקה גרימת סבל לבעלי חיים. ההחלטה דורשת מהחברה לבחון לעומק ולהשתמש בחלופות קיימות לבדיקות גירוי, כגון רקמות מלאכותיות."
            }
        },
        {
            title: "חקר תהליך התפתחותי מוקדם",
            purpose: "הבנת תהליכים מולקולריים וגנטיים המתרחשים בשלבים המוקדמים ביותר של התפתחות עוברים ביונקים. ידע בסיסי זה קריטי להבנה של מומים מולדים, בעיות פוריות ומחלות התפתחותיות.",
            suffering: "מינימלית עד בינונית (איסוף עוברים בשלבי התפתחות שונים, לעיתים לקיחת דגימות מיקרוסקופיות)",
            animals: 30,
            success: "60%",
             feedback: {
                approve: "<strong>אושר:</strong> ועדת האתיקה הכירה בחיוניות המחקר הבסיסי להתקדמות המדעית והרפואית העתידית, גם אם התועלת אינה מיידית. הסבל הצפוי נתפס כנמוך יחסית לפוטנציאל הידע העצום שייצבר, אשר עשוי להשפיע על תחומים רפואיים רבים בעתיד.",
                reject: "<strong>נדחה:</strong> ההחלטה נימקה כי אף שהידע הפוטנציאלי חשוב, הוא אינו בעל תועלת רפואית או יישומית מיידית. גרימת סבל, אפילו מינימלי/בינוני, נתפסה כבלתי מוצדקת בשלב זה, ונדרש מהחוקרים למצות באופן מלא חלופות מחקר אפשריות בתרביות תאים, מודלים ממוחשבים או אורגניזמים פשוטים יותר."
            }
        },
         {
            title: "בדיקת תופעות לוואי של תרופה קיימת במינון חדש",
            purpose: "בדיקת בטיחות (רעילות כרונית) של תרופה מאושרת לשימוש במחלה אחת, המועמדת כעת לטיפול במחלה כרונית אחרת הדורשת מינון גבוה משמעותית ולאורך זמן רב יותר. הבדיקה נדרשת רגולטורית על ידי משרד הבריאות טרם אישור השימוש החדש.",
            suffering: "בינונית עד גבוהה (מתן התרופה לאורך זמן רב, מעקב קבוע אחר תופעות לוואי, אפשרות לירידה הדרגתית במצב בריאותי)",
            animals: 150,
            success: "80%",
             feedback: {
                approve: "<strong>אושר:</strong> בדיקת בטיחות (רעילות כרונית) היא קריטית ומחויבת רגולטורית להרחבת שימוש בתרופה קיימת שיכולה לסייע לחולים רבים הסובלים ממחלה כרונית. ועדת האתיקה שקלה את הסבל הפוטנציאלי אל מול הצורך הרפואי הברור והתועלת הריאלית הפוטנציאלית לחולים, והאחרונים גברו. צוין שהפרוטוקול כלל אמצעים למזעור הסבל.",
                reject: "<strong>נדחה:</strong> ועדת האתיקה קבעה כי אף שהתרופה קיימת והצורך הרפואי קיים, הסבל הצפוי לבעלי החיים לאורך זמן כה רב ובמינון גבוה נתפס כבלתי מוצדק ללא עדות מוקדמת חזקה יותר ליעילות משמעותית של התרופה למחלה החדשה במינון זה. נדרש מחקר פרה-קליני מעמיק יותר או במינונים נמוכים יותר, או חיפוש חלופות לבדיקת רעילות כרונית."
            }
        }
    ];

    let currentScenarioIndex = 0;

    // Get DOM elements
    const scenarioTitleEl = document.getElementById('scenario-title-text');
    const scenarioPurposeEl = document.getElementById('scenario-purpose');
    const scenarioSufferingEl = document.getElementById('scenario-suffering');
    const scenarioAnimalsEl = document.getElementById('scenario-animals');
    const scenarioSuccessEl = document.getElementById('scenario-success');

    const scenarioAreaEl = document.getElementById('scenario-area'); // Wrapper for scenario and counter
    const scenarioContainerEl = document.getElementById('scenario-container'); // The card itself
    const scenarioCounterNumEl = document.getElementById('current-scenario-num');
    const totalScenariosEl = document.getElementById('total-scenarios');

    const decisionButtonsEl = document.getElementById('decision-buttons');
    const feedbackContainerEl = document.getElementById('feedback-container');
    const feedbackTextEl = document.getElementById('feedback-text');
    const feedbackIconAreaEl = document.getElementById('feedback-icon-area');

    const nextScenarioBtn = document.getElementById('next-scenario-btn');
    const restartBtn = document.getElementById('restart-btn');
    const endMessageEl = document.getElementById('end-message');
    const endRestartBtn = document.getElementById('end-restart-btn');

    const approveBtn = document.getElementById('approve-btn');
    const rejectBtn = document.getElementById('reject-btn');

    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationEl = document.getElementById('explanation');

    // Set total scenarios count initially
    totalScenariosEl.textContent = scenarios.length;

    function displayScenario(index) {
         // Hide previous elements with transition
        if (scenarioContainerEl.classList.contains('visible')) {
             scenarioContainerEl.classList.remove('visible');
             scenarioContainerEl.classList.add('hidden');
        }
         if (feedbackContainerEl.classList.contains('visible')) {
             feedbackContainerEl.classList.remove('visible');
             feedbackContainerEl.classList.add('hidden');
         }
         if (endMessageEl.classList.contains('visible')) {
             endMessageEl.classList.remove('visible');
             endMessageEl.classList.add('hidden');
         }


        // Add a slight delay before showing the next scenario to allow transition
        setTimeout(() => {
            if (index >= scenarios.length) {
                endSimulation();
                return;
            }

            const scenario = scenarios[index];
            scenarioTitleEl.textContent = scenario.title;
            scenarioPurposeEl.textContent = scenario.purpose;
            scenarioSufferingEl.textContent = scenario.suffering;
            scenarioAnimalsEl.textContent = scenario.animals;
            scenarioSuccessEl.textContent = scenario.success;

            scenarioCounterNumEl.textContent = index + 1; // Update counter

            // Hide other containers and show scenario
            feedbackContainerEl.classList.add('hidden');
            feedbackContainerEl.classList.remove('visible');
            endMessageEl.classList.add('hidden');
             endMessageEl.classList.remove('visible');

            scenarioContainerEl.classList.remove('hidden');
            scenarioContainerEl.classList.add('visible'); // Add visible class for transition

            decisionButtonsEl.classList.remove('hidden');
            nextScenarioBtn.classList.add('hidden');
            restartBtn.classList.add('hidden'); // Hide restart on scenario view
            endRestartBtn.classList.add('hidden');

            // Remove feedback icon from previous state
            feedbackIconAreaEl.innerHTML = '';
            feedbackIconAreaEl.classList.remove('visible');

        }, 600); // Delay matches CSS transition duration
    }

    function handleDecision(decision) {
        const scenario = scenarios[currentScenarioIndex];
        feedbackTextEl.innerHTML = scenario.feedback[decision]; // Use innerHTML to support bold tags

        // Add icon feedback
        feedbackIconAreaEl.innerHTML = ''; // Clear previous icon
        const iconSpan = document.createElement('span');
        iconSpan.classList.add('icon');
        if (decision === 'approve') {
             iconSpan.classList.add('approve-icon');
             iconSpan.textContent = '✅'; // Checkmark emoji
             feedbackIconAreaEl.appendChild(iconSpan);
        } else { // reject
             iconSpan.classList.add('reject-icon');
             iconSpan.textContent = '❌'; // Cross emoji
             feedbackIconAreaEl.appendChild(iconSpan);
        }
        feedbackIconAreaEl.classList.add('visible'); // Make icon visible

        // Hide scenario and show feedback with transition
        scenarioContainerEl.classList.remove('visible');
        scenarioContainerEl.classList.add('hidden');

        setTimeout(() => {
            feedbackContainerEl.classList.remove('hidden');
            feedbackContainerEl.classList.add('visible'); // Add visible for transition
            decisionButtonsEl.classList.add('hidden');

            if (currentScenarioIndex < scenarios.length - 1) {
                nextScenarioBtn.classList.remove('hidden');
                 restartBtn.classList.remove('hidden'); // Show restart after decision
            } else {
                 // Last scenario, only show restart
                 restartBtn.classList.remove('hidden');
                 nextScenarioBtn.classList.add('hidden');
            }
        }, 600); // Delay matches CSS transition duration
    }

    function endSimulation() {
         // Hide containers with transition
         if (scenarioContainerEl.classList.contains('visible')) {
             scenarioContainerEl.classList.remove('visible');
             scenarioContainerEl.classList.add('hidden');
         }
         if (feedbackContainerEl.classList.contains('visible')) {
             feedbackContainerEl.classList.remove('visible');
             feedbackContainerEl.classList.add('hidden');
         }

         // Remove feedback icon
        feedbackIconAreaEl.innerHTML = '';
        feedbackIconAreaEl.classList.remove('visible');

        // Show end message with transition
        setTimeout(() => {
             endMessageEl.classList.remove('hidden');
             endMessageEl.classList.add('visible'); // Add visible for transition
             restartBtn.classList.add('hidden'); // Hide the mid-sim restart button
        }, 600); // Delay matches CSS transition
    }

    function restartSimulation() {
         // Hide end message or feedback with transition
         if (endMessageEl.classList.contains('visible')) {
             endMessageEl.classList.remove('visible');
             endMessageEl.classList.add('hidden');
         }
         if (feedbackContainerEl.classList.contains('visible')) {
             feedbackContainerEl.classList.remove('visible');
             feedbackContainerEl.classList.add('hidden');
         }

        currentScenarioIndex = 0;
        // Start displaying the first scenario after a slight delay
         setTimeout(() => {
             displayScenario(currentScenarioIndex);
         }, 600); // Delay matches CSS transition
    }

    // Event Listeners
    approveBtn.addEventListener('click', () => handleDecision('approve'));
    rejectBtn.addEventListener('click', () => handleDecision('reject'));

    nextScenarioBtn.addEventListener('click', () => {
        currentScenarioIndex++;
        displayScenario(currentScenarioIndex);
    });

    restartBtn.addEventListener('click', restartSimulation);
    endRestartBtn.addEventListener('click', restartSimulation);

    toggleExplanationBtn.addEventListener('click', () => {
        explanationEl.classList.toggle('hidden');
        // Optional: Change button text based on state
        if (explanationEl.classList.contains('hidden')) {
             toggleExplanationBtn.textContent = 'הצג רקע והסבר';
        } else {
             toggleExplanationBtn.textContent = 'הסתר רקע והסבר';
        }
    });

    // Initial display of the first scenario when the page loads
    document.addEventListener('DOMContentLoaded', () => {
        displayScenario(currentScenarioIndex);
    });

</script>
---