---
title: "סודות הניווט הפולינזי: מסע אל מפות המקלות"
english_slug: polynesian-navigation-secrets-stick-map-exploration
category: "סוציולוגיה"
tags: [פולינזיה, ניווט עתיק, מפות מקלות, אתנוגרפיה, היסטוריה]
---
# סודות הניווט הפולינזי: מסע אל מפות המקלות

כיצד הצליחו יורדי ים פולינזים אמיצים לחצות אלפי קילומטרים של אוקיינוס פתוח לפני מאות ואלפי שנים, ללא מצפן, מפה רגילה או GPS? הסוד טמון בטכניקות ניווט גאוניות וב"מפות" ייחודיות שלא דומות לשום דבר שאנחנו מכירים. בואו נצלול פנימה ונחקור את המסתורין של מפות המקלות!

<div id="interactive-map-explorer">
    <h2>צא למסע: חקור את מפות המקלות הפולינזיות</h2>
    <div id="exploration-container" class="fade-in">
        <img id="map-image" src="" alt="מפת מקלות פולינזית">
        <p id="item-description" class="exploration-text"></p>
        <div id="options-container">
            <!-- Buttons will be inserted here by JS -->
        </div>
        <div id="feedback" class="feedback"></div>
        <button id="continue-button" class="hidden primary-button">המשך למסע</button>
    </div>
    <div id="exploration-end" class="hidden fade-in">
        <h3>משימת החקר הושלמה!</h3>
        <p>התנסית בחקר מפות המקלות הייחודיות של הפולינזים. כעת תוכל לעבור להסבר המלא כדי להעמיק את ההבנה.</p>
        <button id="restart-button" class="secondary-button">התחל את החקר מחדש</button>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

    #interactive-map-explorer {
        font-family: 'Rubik', sans-serif;
        max-width: 700px;
        margin: 30px auto;
        padding: 30px;
        border: 1px solid #bde0fe; /* Light blue border */
        border-radius: 12px; /* More rounded corners */
        background-color: #f0f8ff; /* Very light blue background */
        direction: rtl;
        text-align: right;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer shadow */
        overflow: hidden; /* Clear floats/margins */
        position: relative; /* Needed for potential animations */
    }

    #interactive-map-explorer h2 {
        text-align: center;
        color: #0077be; /* Ocean blue */
        margin-bottom: 25px;
        font-size: 1.8em;
        font-weight: 700;
    }

    #exploration-container, #exploration-end {
         /* Base styles - animation handled by class */
         padding-top: 10px; /* Add some space above */
    }

    #map-image {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 0 auto 30px auto;
        border: 5px solid #0077be; /* Thicker ocean blue border */
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* More prominent shadow */
        transition: transform 0.5s ease-out; /* Smooth scale transition */
    }

    #item-description {
        font-size: 1.2em;
        margin-bottom: 20px;
        font-weight: 500;
        color: #333; /* Darker text */
        line-height: 1.6;
    }

     #options-container {
        display: flex;
        flex-direction: column;
        gap: 12px; /* More space between buttons */
        margin-bottom: 20px;
    }

    #options-container button {
        padding: 14px 20px; /* Larger padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none; /* No default border */
        border-radius: 25px; /* Pill shape */
        background-color: #00b4d8; /* Lighter blue button */
        color: white;
        text-align: right;
        transition: all 0.3s ease; /* Smooth transitions for hover effects */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* Button shadow */
    }

    #options-container button:hover {
        background-color: #0077be; /* Darker blue on hover */
        transform: translateY(-2px); /* Lift effect */
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }

    #options-container button:active {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    #options-container button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        background-color: #ccc; /* Grey when disabled */
        transform: none;
        box-shadow: none;
    }

    .feedback {
        margin-top: 20px;
        padding: 15px; /* Larger padding */
        border-radius: 8px;
        min-height: 2em; /* Ensure space even if empty */
        font-weight: 500;
        line-height: 1.5;
        opacity: 0; /* Start hidden for animation */
    }

    .feedback.correct {
        background-color: #d4edda; /* Pale green */
        color: #155724; /* Dark green */
        border-left: 6px solid #28a745; /* Green border highlight */
    }

    .feedback.incorrect {
        background-color: #f8d7da; /* Pale red */
        color: #721c24; /* Dark red */
        border-left: 6px solid #dc3545; /* Red border highlight */
    }

    /* Animation for feedback */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .feedback.animate {
        animation: fadeInUp 0.4s ease-out forwards;
    }


    .primary-button { /* Continue button style */
        display: block;
        width: 100%;
        padding: 14px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 25px;
        background-color: #28a745; /* Success green */
        color: white;
        margin-top: 25px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }

     .primary-button:hover {
        background-color: #218838; /* Darker green on hover */
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
     .primary-button:active {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
     }

    .secondary-button { /* Restart button style */
        display: block;
        width: 100%;
        padding: 14px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 25px;
        background-color: #007bff; /* Primary blue */
        color: white;
        margin-top: 25px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }

     .secondary-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .secondary-button:active {
        transform: translateY(0);
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .hidden {
        display: none;
    }

    /* Fade-in animation for sections */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .fade-in {
        animation: fadeIn 0.6s ease-out forwards;
    }


    #explanation-button {
        display: block;
        width: auto; /* Allow natural width */
        margin: 30px auto; /* Center the button */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px;
        background-color: #e9c46a; /* Sandy yellow */
        color: #333; /* Dark text */
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        font-weight: 500;
    }
     #explanation-button:hover {
         background-color: #d4af57; /* Darker yellow */
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.3);
     }
     #explanation-button:active {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
     }

    #full-explanation {
        margin-top: 40px;
        padding: 30px;
        border: 1px solid #ddd;
        border-radius: 12px;
        background-color: #fff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        font-family: 'Rubik', sans-serif;
        line-height: 1.7;
        color: #333;
    }

    #full-explanation h2 {
        color: #0077be;
        border-bottom: 2px solid #eee;
        padding-bottom: 12px;
        margin-bottom: 20px;
        font-size: 1.6em;
        font-weight: 700;
    }

    #full-explanation h3 {
         color: #00b4d8; /* Lighter blue */
         margin-top: 25px;
         margin-bottom: 12px;
         font-size: 1.3em;
         font-weight: 500;
    }

     #full-explanation p {
         margin-bottom: 15px;
         /* line-height: 1.6; */ /* Already in parent */
     }

    #full-explanation ul {
        margin-bottom: 15px;
        padding-right: 25px; /* Adjusted padding */
    }

    #full-explanation li {
        margin-bottom: 10px; /* More space */
        line-height: 1.6;
    }

     #full-explanation small {
         display: block; /* Ensure small text is on its own line */
         margin-top: 5px;
         color: #555;
         font-size: 0.9em;
     }
</style>

<button id="explanation-button">הצג הסבר מורחב על הניווט הפולינזי</button>

<div id="full-explanation" class="hidden">
    <h2>הסבר מורחב: סודות הניווט הפולינזי ומפות המקלות</h2>

    <h3>הקדמה: הפולינזים - המאסטרים הקדומים של האוקיינוס</h3>
    <p>דמיינו לרגע עשרות אלפי איים הפזורים על פני מרחבי האוקיינוס השקט, שטח ענק יותר מכל יבשת! במשך מאות ואלפי שנים, הצליחו תושבי פולינזיה לנווט במיומנות מופלאה בין נקודות זעירות אלו, ליישב מקומות מרוחקים כמו הוואי, ניו זילנד (או טכנית, אאוטארואה בפי המאורים) ואי הפסחא (ראפה נוי). הישג ימי כביר זה, שקדם בהרבה למסעות האירופים הגדולים, נחשב לאחד מפלאי ההיסטוריה האנושית.</p>

    <h3>העולם בעיני נווט פולינזי: לא רק כוכבים!</h3>
    <p>הניווט הפולינזי המסורתי לא הסתמך על מצפנים ממתכת או מכשירים נוצצים, אלא על אינטליגנציה תצפיתית עמוקה ויכולת זכרון פנומנלית. הנווטים היו אומנים בקריאת שפת הים והשמיים:</p>
    <ul>
        <li>**נתיבי כוכבים (Star Paths):** בלילה, השמים היו מפה חיה. הנווטים הכירו מאות כוכבים וידעו בדיוק היכן כל קבוצה זורחת ושוקעת באופק, נקודה שהצביעה על כיוונים קבועים לאיים שונים.</li>
        <li>**שמש וירח:** מיקום השמש במהלך היום ומיקום הירח בלילה, יחד עם מופעיו, סיפקו נקודות ייחוס קריטיות.</li>
        <li>**שפת הגלים והזרמים (Ocean Swells and Currents):** אולי הסוד הגדול ביותר! האוקיינוס אינו משטח חלק. גלים ארוכים ועקביים (swells) נעים באוקיינוס באופנים מוכרים, והתנהגותם משתנה כשהם נתקלים באיים (הם מתעקלים, נשברים, או יוצרים דפוסים מיוחדים). נווט מיומן יכול "לקרוא" את הדפוסים הללו אפילו מבטן הקאנו שלו, ולהסיק מהם את מיקומו ונוכחות יבשה קרובה.</li>
        <li>**עננים וצבע השמיים:** עננים מסוימים נוטים להצטבר מעל יבשה, וצבע השמים מעל אי רחוק יכול להיות בהיר יותר עקב החזר אור מהלגונה או החוף.</li>
        <li>**עולם החי (Wildlife):** מעקב אחר מעוף ציפורים ימיות מסוימות בשעות מסוימות של היום (הן יוצאות מהאי בבוקר וחוזרות אליו בערב) או נוכחות מינים ספציפיים של דגים יכולו לספק רמזים קריטיים למיקום יחסי.</li>
    </ul>

    <h3>מפות המקלות (Stick Charts): לא מפות, אלא סיפורים חזותיים של הים</h3>
    <p>שכחו מפות נייר עם קווים מדויקים וסקאלות. מפות המקלות, המכונות באיי מרשל "מדדו", "רבלליב" או "מאטנג", הן ייצוגים מופשטים של ידע האוקיינוס. הן לא מראות "איפה אני נמצא", אלא "כיצד הים מתנהג פה" ו"איך לנווט דרך הגלים והזרמים הללו כדי להגיע לאי ההוא". הן למעשה תרשימי זיכרון ולימוד של דפוסי הגלים והאינטראקציה שלהם עם איים. הידע המגולם בהן היה קדוש וסודי, והועבר מדור לדור בעל פה רק לנווטים נבחרים.</p>
    <p>המפות עשויות ממקלות עץ גמישים (לרוב ענפי קוקוס או פנדנוס) הקשורים בקשרים מורכבים מסיבי קוקוס, ועליהן משובצים צדפים קטנים או אבנים.</p>

    <h3>השוואה למפות מודרניות: תפיסות עולם שונות של מרחב</h3>
    <p>בניגוד למפות מודרניות המתבססות על נקודת מבט "מלמעלה" ורשת קואורדינטות גלובלית, מפות המקלות הן ייצוג פנומנולוגי וחווייתי. הן מתארות את העולם מנקודת מבטו של הנווט בתוך האוקיינוס – כיצד הגלים מגיעים אליו וממנו, כיצד הם מתנהגים סביב איים, ואיך להשתמש בתבניות אלו כדי למצוא את הדרך. זוהי מפה שאתה לא קורא, אלא "מרגיש" ולומד לחיות בתוכה.</p>

    <h3>סוגי מפות המקלות העיקריים באיי מרשל</h3>
    <p>כדי להבין טוב יותר, נכיר את שלושת הסוגים המרכזיים שפגשת בחקר הראשוני:</p>
    <ul>
        <li>
            **Mattang (מאטנג):** חושב עליהן כעל "לוחות תרגול" מופשטים. המאטנגים לא שימשו לתכנון מסע ליעד ספציפי, אלא ללמד נווטים צעירים את הפיזיקה הבסיסית של הגלים – כיצד גלים מתנהגים ומשתקפים מאיים, כיצד נוצרים דפוסי גלים מורכבים בשפכי גלים שונים. המבנה שלהם לרוב גאומטרי ומסוגנן מאוד, עם מעט צדפים (או ללא כלל).
            <br><small><i>(המפות שחקרת מסוג מאטנג היו הגיאומטריות יותר, ששימשו ללימוד עקרונות ולא לניווט ספציפי).</i></small>
        </li>
        <li>
            **Meddo (מדדו):** אלו היו מפות "אזוריות". הן התמקדו בקבוצה קטנה של איים סמוכים יחסית והציגו את המיקום היחסי של האיים הללו ואת דפוסי הגלים והזרמים הספציפיים באזור שביניהם וסביבם. שימשו לניווט במסעות קצרים יחסית בין איים קרובים.
            <br><small><i>(המפות שחקרת מסוג מדדו הציגו קבוצת איים (צדפים) קטנה ומקלות שחיברו ביניהם).</i></small>
        </li>
        <li>
            **Rebbelib (רבלליב):** הגדולות והשאפתניות ביותר. אלו היו מפות "ארכיפלג". הן כיסו שטח נרחב, כללו איים רבים ומסלולי ניווט ארוכים. שימשו לתכנון מסעות מורכבים וארוכי טווח בין קבוצות איים מרוחקות בארכיפלג איי מרשל העצום.
             <br><small><i>(המפות שחקרת מסוג רבלליב היו המפות הגדולות עם מספר רב יותר של צדפים ומקלות).</i></small>
        </li>
    </ul>

    <h3>האלמנטים הסודיים: מה המקלות והצדפים באמת מספרים?</h3>
    <ul>
        <li>**מקלות (Sticks):** לא סתם קישוטים! המקלות, ישרים ומעוגלים, מייצגים את כיווני הגלים הדומיננטיים (swells) באזור וכיצד הם נשברים, מתעקלים או משפיעים זה על זה כשהם פוגשים איים או זרמים. מקלות מעוגלים יכלו לסמל שינויים בכיוון הגל סביב אי.</li>
        <li>**צדפים או אבנים קטנות (Shells/Stones):** אלו הם ה"איים". מיקומם היחסי על המפה מייצג את מיקום האיים בעולם האמיתי ביחס לדפוסי הגלים המיוצגים על ידי המקלות.</li>
    </ul>

    <h3>שימוש ולימוד: המפות ככלי זכרון חי</h3>
    <p>נקודה חשובה: ברוב המקרים, הנווטים לא לקחו את מפות המקלות איתם לים! הן היו יקרות ופגיעות. הן שימשו בעיקר ככלי לימוד ותרגול על היבשה. הנווטים הצעירים היו מבלים שעות בלימוד המפות, שינון דפוסי הגלים, האזינו לסיפורי מסעות של נווטים ותיקים, ותרגלו את הידע במים רדודים ובהדרגה באוקיינוס הפתוח. המפה ה"אמיתית" הייתה למעשה בראשו של הנווט.</p>

     <h3>מורשת של גאונות</h3>
     <p>מפות המקלות הן לא רק חפצים אתנוגרפיים מרתקים, אלא עדות מרשימה לגאונות האנושית וליכולת לפתח מערכות ידע מורכבות המבוססות על התבוננות עמוקה וחיים בהרמוניה עם הטבע. הן מראות לנו שיש דרכים רבות ומגוונות להבין ולנווט את העולם, ושמערכות ידע שאינן מבוססות על מדע מערבי יכולות להיות מדויקות ומוצלחות להפליא בתנאים שלהן. זוהי הצצה נדירה לעולמם של יורדי הים הגדולים ביותר בהיסטוריה.</p>
</div>

<script>
    const explorationItems = [
        {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Mattang-stick-chart.jpg/400px-Mattang-stick-chart.jpg',
            description: "צא למסע החקר הראשון! התבונן במפת המקלות הזו. שים לב למבנה הגיאומטרי המאורגן והמופשט שלה. סוג זה של מפה שימש בעיקר ככלי לימוד ותרגול של עקרונות התנהגות הגלים. איזה סוג מפה זו?",
            options: ["Mattang (מפת תרגול עקרונות)", "Meddo (מפת ניווט אזורי)", "Rebbelib (מפת ניווט למרחקים)"],
            correctOptionIndex: 0,
            feedback: {
                correct: "מצוין! זוהי אכן מפת <strong>Mattang</strong>. הן לא היו מפות מסע בפועל, אלא שימשו להתמחות בדפוסי הגלים (swells) והבנת האינטראקציה שלהם עם איים, כחלק מהכשרת נווטים.",
                incorrect: "כמעט! זוהי מפת <strong>Mattang</strong>. המבנה המופשט שלה והשימוש העיקרי בה ללימוד עקרונות גלים מופשטים (ולא לניווט לאי ספציפי) מייחד אותה. המשיכו הלאה כדי לגלות את הסוגים האחרים!"
            }
        },
        {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Meddo-stick-chart.jpg/400px-Meddo-stick-chart.jpg',
            description: "התבונן מקרוב במפה הבאה. היא מציגה קבוצה מצומצמת יחסית של איים סמוכים (הצדפים) ומתארת את הגלים והזרמים המקומיים ביניהם. סוג מפה זה שימש לניווט מעשי באזור מצומצם. איזה סוג של מפת מקלות זו?",
            options: ["Mattang (מפת תרגול עקרונות)", "Meddo (מפת ניווט אזורי)", "Rebbelib (מפת ניווט למרחקים)"],
            correctOptionIndex: 1,
            feedback: {
                correct: "נכון מאוד! זוהי מפת <strong>Meddo</strong>. מפות אלו שימשו נווטים למסעות קצרים יותר, תוך התמקדות בקבוצת איים קטנה והצגת המידע הקריטי על הגלים והזרמים באזור ספציפי זה.",
                incorrect: "לא מדויק הפעם. מפה זו היא מפת <strong>Meddo</strong>. היא התמקדה בקבוצה מצומצמת של איים סמוכים ונועדה לניווט באזור מצומצם, בניגוד למפות התרגול המופשטות או מפות הארכיפלג הגדולות. המשיכו כדי לראות את הסוג האחרון!"
            }
        },
        {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Rebbelib_Stick_Chart_from_the_Marshall_Islands.jpg/500px-Rebbelib_Stick_Chart_from_the_Marshall_Islands.jpg',
            description: "עכשיו נחקור מפה גדולה ומורכבת יותר. מפה זו מכסה שטח נרחב מאוד וכוללת איים רבים. היא שימשה לתכנון מסעות ארוכים וחוצי-אוקיינוס בין קבוצות איים מרוחקות. איזה סוג של מפת מקלות זו?",
            options: ["Mattang (מפת תרגול עקרונות)", "Meddo (מפת ניווט אזורי)", "Rebbelib (מפת ניווט למרחקים)"],
            correctOptionIndex: 2,
            feedback: {
                correct: "פשוט מדהים! זוהי מפת <strong>Rebbelib</strong>. אלו היו מפות הארכיפלג הגדולות והמורכבות ביותר, שכללו מידע על איים רבים ודפוסי גלים בשטח רחב, והיו חיוניות לתכנון מסעות ימיים ארוכים במיוחד.",
                incorrect: "לא בדיוק. מפה גדולה ומורכבת זו היא מפת <strong>Rebbelib</strong>. היא נועדה לניווט למרחקים ארוכים בין קבוצות איים שונות בארכיפלג איי מרשל. כעת אתם מכירים את שלושת הסוגים העיקריים!"
            }
        },
        {
             image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Rebbelib_Stick_Chart_from_the_Marshall_Islands.jpg/500px-Rebbelib_Stick_Chart_from_the_Marshall_Islands.jpg', // Reusing Rebbelib image
             description: "שימו לב לאלמנטים הקטנים המשובצים במפות המקלות – לרוב צדפים או אבנים קטנות. מה סימלו אלמנטים אלו עבור הנווטים הפולינזים?",
             options: ["כיווני רוח דומיננטיים", "ספינות קאנו במסע", "מיקומם היחסי של האיים", "נקודות זריחה/שקיעה של כוכבים"],
             correctOptionIndex: 2,
             feedback: {
                 correct: "מדויק לחלוטין! הצדפים או האבנים הקטנות <strong>סימלו את האיים</strong>. מיקומם על המפה הציג את המיקום היחסי של האיים בתוך רשת הגלים והזרמים שמיוצגת על ידי המקלות.",
                 incorrect: "לא המקלות או אלמנטים ימיים אחרים. הצדפים או האבנים הקטנות במפות המקלות הם שסימלו את <strong>האיים</strong>. המקלות עצמם ייצגו את דפוסי הגלים והזרמים. נסו את הפריט הבא!"
             }
         },
         {
             image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Mattang-stick-chart.jpg/400px-Mattang-stick-chart.jpg', // Reusing Mattang image
             description: "האלמנט המרכזי בכל מפות המקלות הם המקלות עצמם, המחוברים בקשרים שונים. מה ייצגו בעיקר המקלות, שהיו קריטיים לנווטים כדי 'לקרוא' את הים?",
             options: ["מרחקים מדויקים בסאוט מייל ימי", "נתיבי מסחר בין איים", "דפוסי גלים וזרמי אוקיינוס", "סוגי עננים המעידים על יבשה"],
             correctOptionIndex: 2,
             feedback: {
                 correct: "מעולה! המקלות הם הלב של המפה והם ייצגו בעיקר את <strong>דפוסי הגלים הדומיננטיים (swells) והזרמים</strong>, וכיצד הם מושפעים מנוכחות האיים. זהו המידע המרכזי שסייע לנווטים להבין את 'שפת' האוקיינוס.",
                 incorrect: "לא בדיוק. המקלות במפות המקלות ייצגו בעיקר את <strong>דפוסי הגלים והזרמים</strong>. זהו המידע המורכב שאיפשר לנווטים 'לקרוא' את האוקיינוס ולדעת כיצד לנוע דרכו. המקלות לא ייצגו מרחקים מדידים, מסלולים או רמזי מזג אוויר ישירים."
             }
         }
    ];

    let currentItemIndex = 0;
    const mapImage = document.getElementById('map-image');
    const itemDescriptionText = document.getElementById('item-description');
    const optionsContainer = document.getElementById('options-container');
    const feedbackDiv = document.getElementById('feedback');
    const continueButton = document.getElementById('continue-button');
    const explorationEndDiv = document.getElementById('exploration-end');
    const explorationContainerDiv = document.getElementById('exploration-container');
    const restartButton = document.getElementById('restart-button');
    const explanationButton = document.getElementById('explanation-button');
    const fullExplanationDiv = document.getElementById('full-explanation');

    // Function to apply fade-in animation class
    function applyFadeIn(element) {
        element.classList.remove('fade-in'); // Remove class to reset animation
        void element.offsetWidth; // Trigger reflow
        element.classList.add('fade-in'); // Add class to restart animation
    }


    function loadItem(index) {
        if (index >= explorationItems.length) {
            endExploration();
            return;
        }
        const item = explorationItems[index];
        mapImage.src = item.image;
        itemDescriptionText.innerHTML = item.description; // Use innerHTML to allow bold tags
        optionsContainer.innerHTML = '';
        feedbackDiv.textContent = '';
        feedbackDiv.className = 'feedback'; // Reset classes
        continueButton.classList.add('hidden');
        explorationEndDiv.classList.add('hidden');
        explorationContainerDiv.classList.remove('hidden');

        // Apply fade-in animation to the container when loading a new item
        applyFadeIn(explorationContainerDiv);


        item.options.forEach((option, i) => {
            const button = document.createElement('button');
            button.textContent = option;
            button.addEventListener('click', () => handleSelection(i, item, button));
            optionsContainer.appendChild(button);
        });
    }

    function handleSelection(selectedIndex, currentItem, clickedButton) {
        const buttons = optionsContainer.querySelectorAll('button');
        buttons.forEach((button, i) => {
             button.disabled = true; // Disable all buttons
             if (i === currentItem.correctOptionIndex) {
                 // Optional: Highlight correct answer subtly
                 // button.style.borderColor = '#28a745';
                 // button.style.backgroundColor = '#e2f0e7';
             } else if (i === selectedIndex) {
                  // Optional: Highlight incorrect selection subtly
                  // button.style.borderColor = '#dc3545';
                  // button.style.backgroundColor = '#f0e2e3';
             }
        });

        let feedbackText = "";
        if (selectedIndex === currentItem.correctOptionIndex) {
            feedbackText = "✅ " + currentItem.feedback.correct;
            feedbackDiv.className = 'feedback correct';
        } else {
            feedbackText = "❌ " + currentItem.feedback.incorrect;
            feedbackDiv.className = 'feedback incorrect';
        }

        feedbackDiv.innerHTML = feedbackText; // Use innerHTML to allow bold tags

         // Trigger feedback animation
         feedbackDiv.classList.add('animate');

        // Use a slight delay before showing continue button for better flow
        setTimeout(() => {
             continueButton.classList.remove('hidden');
        }, 500); // Show continue button 0.5s after feedback appears

    }

    function nextItem() {
         // Reset feedback animation class before moving to next item
        feedbackDiv.classList.remove('animate');

        currentItemIndex++;
        loadItem(currentItemIndex);
    }

    function endExploration() {
        explorationContainerDiv.classList.add('hidden');
        explorationEndDiv.classList.remove('hidden');
         applyFadeIn(explorationEndDiv); // Animate end screen
    }

    function restartExploration() {
        currentItemIndex = 0;
        explorationEndDiv.classList.add('hidden'); // Hide end screen immediately
        loadItem(currentItemIndex);
    }

     function toggleExplanation() {
         fullExplanationDiv.classList.toggle('hidden');
         if (fullExplanationDiv.classList.contains('hidden')) {
             explanationButton.textContent = 'הצג הסבר מורחב על הניווט הפולינזי';
         } else {
              explanationButton.textContent = 'הסתר הסבר מורחב על הניווט הפולינזי';
              // Optional: Scroll to explanation section
              // fullExplanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
     }

    continueButton.addEventListener('click', nextItem);
    restartButton.addEventListener('click', restartExploration);
    explanationButton.addEventListener('click', toggleExplanation);


    // Initialize exploration
    loadItem(currentItemIndex);

</script>