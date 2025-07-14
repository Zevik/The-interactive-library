---
title: "שפת השמיים: מדריך מרתק לזיהוי עננים"
english_slug: what-the-sky-tells-us-a-visual-guide-to-cloud-identification
category: "מדעי האטמוספרה"
tags: ["עננים", "מזג אוויר", "חיזוי", "אטמוספירה", "מדע", "אינטראקטיבי"]
---
<div class="interactive-container">
    <h1>שפת השמיים: מדריך מרתק לזיהוי עננים</h1>
    <p>השמיים מעלינו הם קנבס דינמי המשתנה ללא הרף, וכל ענן הוא מילה בסיפור שמספר לנו על מזג האוויר. האם ענן לבן ורך מבשר יום שמשי, או שמא גוש אפור כהה מסמן משהו אחר לגמרי? בעזרת המדריך הוויזואלי הזה, תלמדו לקרוא את שפת העננים ולהבין מה מסתתר מאחורי המראה שלהם.</p>

    <div id="app-container" class="app-quiz-section">
        <div id="cloud-image-container">
            <img id="cloud-image" src="" alt="תמונה של ענן">
            <div class="image-overlay">זיהוי ענן</div>
        </div>

        <div id="question-area">
            <p class="question-text">איזה גובה אופייני לבסיס הענן הזה?</p>
            <div id="height-choices" class="choices-group">
                <button data-choice="גבוה">גבוה (> 6 ק"מ)</button>
                <button data-choice="בינוני">בינוני (2 - 6 ק"מ)</button>
                <button data-choice="נמוך">נמוך (< 2 ק"מ)</button>
            </div>

            <p class="question-text">איזה סוג מזג אוויר סביר מקושר בדרך כלל לענן כזה?</p>
            <div id="weather-choices" class="choices-group">
                <button data-choice="שמיים בהירים">שמיים בהירים / עננות קלה</button>
                <button data-choice="גשם קל / טפטוף">גשם קל / טפטוף</button>
                <button data-choice="גשם מתמשך / סופה">גשם מתמשך / סופה</button>
                <button data-choice="שלג / ברד">שלג / ברד</button>
                <button data-choice="ערפל">ערפל (קרוב לקרקע)</button>
            </div>
            
            <button id="submit-answer" class="submit-button" disabled>בדיקה</button>
        </div>

        <div id="feedback-area" class="feedback-section hidden">
            <div id="feedback-text"></div>
            <button id="next-cloud" class="next-button hidden">ענן הבא</button>
        </div>
    </div>
</div>

<style>
    /* כללי */
    .interactive-container {
        direction: rtl;
        font-family: 'Heebo', sans-serif; /* שימוש בפונט מודרני יותר אם זמין */
        max-width: 700px;
        margin: 20px auto;
        padding: 20px;
        background-color: #f0f8ff; /* אקווה בהיר */
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        text-align: center;
        overflow: hidden; /* לוודא ששום דבר לא יוצא מגבולות הקונטיינר */
        position: relative;
    }

     .interactive-container h1 {
        color: #0056b3; /* כחול כהה יותר */
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.8em;
        font-weight: bold;
    }

    .interactive-container p {
        color: #333;
        margin-bottom: 20px;
        line-height: 1.6;
        font-size: 1.1em;
    }

    /* אזור האפליקציה (חידון) */
    .app-quiz-section {
        background-color: #ffffff; /* רקע לבן לחידון עצמו */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
        position: relative; /* למיקום האלמנטים הפנימיים */
    }

    #cloud-image-container {
        margin-bottom: 25px;
        position: relative; /* למיקום האוברליי */
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    #cloud-image {
        max-width: 100%;
        height: auto;
        display: block; /* למנוע רווח לבן מתחת לתמונה */
        border-radius: 8px;
        transition: transform 0.5s ease-in-out; /* אנימציית זום עדין */
    }

    #cloud-image-container:hover #cloud-image {
         transform: scale(1.03); /* זום קל במעבר עכבר */
    }

    .image-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0) 50%); /* הצללה למטה */
        color: white;
        display: flex;
        align-items: flex-end; /* הצמד לכיוון מטה */
        justify-content: flex-start; /* הצמד לימין (בגלל RTL) */
        padding: 15px;
        font-size: 1.2em;
        font-weight: bold;
        opacity: 0; /* התחל כהמוס */
        transition: opacity 0.3s ease; /* אנימציית הופעה */
        pointer-events: none; /* ודא שלא מפריע לקליקים */
         direction: rtl;
    }

     #cloud-image-container:hover .image-overlay {
         opacity: 1; /* הצג במעבר עכבר */
     }


    #question-area p.question-text {
        margin-top: 20px;
        margin-bottom: 15px;
        font-weight: bold;
        color: #0056b3; /* צבע השאלה */
        font-size: 1.1em;
    }

    .choices-group {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin-bottom: 20px;
        gap: 8px; /* רווח בין הכפתורים */
    }

    #height-choices button,
    #weather-choices button {
        padding: 10px 20px;
        border: 2px solid #007bff;
        border-radius: 25px; /* כפתורים מעוגלים יותר */
        background-color: #e9f5ff; /* כחול בהיר מאוד */
        color: #007bff; /* כחול רגיל */
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
        min-width: 120px; /* רוחב מינימלי אחיד */
        text-align: center;
    }

    #height-choices button:hover,
    #weather-choices button:hover:not(.selected) {
        background-color: #cce5ff; /* כחול בהיר יותר במעבר עכבר */
        border-color: #0056b3;
    }

     #height-choices button:active,
     #weather-choices button:active {
         transform: scale(0.98); /* אנימציית לחיצה */
     }
    
    #height-choices button.selected,
    #weather-choices button.selected {
        background-color: #007bff; /* כחול מלא */
        color: white;
        border-color: #0056b3; /* כחול כהה יותר */
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3); /* צל לכפתור הנבחר */
    }

    .submit-button {
        display: block;
        width: 60%; /* רחב יותר */
        max-width: 250px;
        margin: 30px auto 10px auto;
        padding: 12px 20px; /* פדינג גדול יותר */
        background-color: #28a745; /* ירוק */
        color: white;
        border: none;
        border-radius: 25px; /* כפתור מעוגל */
        font-size: 1.2rem;
        cursor: pointer;
        transition: background-color 0.3s ease, opacity 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(40, 167, 69, 0.3); /* צל לכפתור */
    }
     .submit-button:disabled {
        background-color: #cccccc; /* אפור כשהוא לא פעיל */
        cursor: not-allowed;
        opacity: 0.7; /* שקיפות קלה */
        box-shadow: none;
    }

    .submit-button:hover:not(:disabled) {
        background-color: #218838; /* ירוק כהה יותר במעבר עכבר */
        box-shadow: 0 4px 12px rgba(33, 136, 56, 0.4);
    }

     .submit-button:active:not(:disabled) {
         transform: scale(0.98);
     }
    
    /* אזור פידבק */
    .feedback-section {
        margin-top: 25px;
        padding: 20px;
        border-top: 1px solid #eee;
        text-align: right;
        background-color: #fff; /* רקע לבן */
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        transition: opacity 0.5s ease-in-out, max-height 0.7s ease-in-out; /* אנימציה להופעה */
        overflow: hidden; /* חתוך תוכן בזמן אנימציה */
        max-height: 0; /* התחל מוסתר */
        opacity: 0; /* התחל שקוף */
        padding-top: 0;
        padding-bottom: 0;
    }

     .feedback-section:not(.hidden) {
         max-height: 500px; /* גובה מקסימלי כשגלוי */
         opacity: 1; /* גלוי לחלוטין */
         padding-top: 20px;
         padding-bottom: 20px;
         margin-top: 20px; /* רווח עליון כשגלוי */
     }


    #feedback-text p {
        margin: 0 0 12px 0;
        line-height: 1.7;
        font-size: 1em;
        color: #444; /* צבע טקסט כללי לפידבק */
    }
    
    #feedback-text .correct {
        color: #28a745; /* ירוק */
        font-weight: bold;
    }
    
    #feedback-text .incorrect {
        color: #dc3545; /* אדום */
        font-weight: bold;
    }

     #feedback-text strong { /* הדגשת סוג הענן המדויק */
         color: #0056b3;
     }


    .hidden {
        display: none; /* אל תציג כלל, לא רק שקוף/קטן */
    }
    
    .next-button {
        display: block;
        width: 180px;
        margin: 20px auto 0 auto;
        padding: 10px 15px;
        background-color: #007bff; /* כחול */
        color: white;
        border: none;
        border-radius: 25px;
        font-size: 1.1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }
    
    .next-button:hover {
        background-color: #0056b3; /* כחול כהה יותר */
    }

     .next-button:active {
         transform: scale(0.98);
     }

    /* הסבר כללי */
    #show-explanation {
        display: block;
        width: 250px; /* רוחב קבוע */
        margin: 30px auto 15px auto;
        padding: 10px 15px;
        background-color: #6c757d; /* אפור */
        color: white;
        border: none;
        border-radius: 25px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }
    
    #show-explanation:hover {
        background-color: #5a6268; /* אפור כהה יותר */
    }

     #show-explanation:active {
         transform: scale(0.98);
     }


    #explanation-section {
        direction: rtl;
        text-align: right;
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 8px;
        background-color: #f9f9f9; /* רקע בהיר */
        transition: max-height 0.7s ease-in-out, opacity 0.5s ease-in-out; /* אנימציה להופעה */
        overflow: hidden; /* חתוך תוכן בזמן אנימציה */
        max-height: 0; /* התחל מוסתר */
        opacity: 0; /* התחל שקוף */
        padding-top: 0;
        padding-bottom: 0;
    }

    #explanation-section:not(.hidden) {
        max-height: 2000px; /* גובה מקסימלי גדול מספיק לכל התוכן */
        opacity: 1; /* גלוי לחלוטין */
        padding-top: 20px;
        padding-bottom: 20px;
        margin-top: 20px; /* רווח עליון כשגלוי */
    }
    
    #explanation-section h2, #explanation-section h3, #explanation-section h4 {
        color: #333;
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: bold;
    }

     #explanation-section h2 { font-size: 1.5em; color: #0056b3; }
     #explanation-section h3 { font-size: 1.3em; color: #007bff; }
     #explanation-section h4 { font-size: 1.1em; color: #555; }


    #explanation-section p {
        margin-bottom: 15px;
        line-height: 1.7;
        color: #444;
    }
    
    #explanation-section ul {
        margin-bottom: 15px;
        padding-right: 25px; /* פדינג מימין לרשימה */
        list-style: disc; /* סוג התבליט */
        color: #444;
    }
    
    #explanation-section li {
        margin-bottom: 8px;
        line-height: 1.6;
    }

     #explanation-section li strong {
         color: #007bff; /* הדגשת שמות העננים ברשימות */
     }

</style>

<button id="show-explanation">הצג הסבר מלא על זיהוי עננים</button>

<div id="explanation-section" class="hidden">
    <h2>הסבר מלא: מה העננים מספרים לנו?</h2>

    <h3>מבוא: למה חשוב להכיר עננים?</h3>
    <p>עננים אינם רק קישוט לשמיים – הם למעשה אינדיקטורים ויזואליים מרתקים למצב האטמוספירה ממש מעלינו. צורתם, הגובה שבו הם נמצאים והרכבם יכולים לספר לנו סיפור שלם על כמות הלחות באוויר, על מידת היציבות (או חוסר היציבות) שלו, וכפועל יוצא מכך – על מזג האוויר הצפוי בשעות ובימים הקרובים. זיהוי עננים הוא כלי יסודי ומרתק לכל מי שמתעניין במטאורולוגיה, בחיזוי מקומי, או פשוט רוצה להתבונן בשמיים בעיניים מבינות יותר.</p>

    <h3>סיווג עננים עיקרי לפי גובה הבסיס</h3>
    <p>השיטה המקובלת והיעילה ביותר לסווג עננים היא לפי גובה הבסיס שלהם באטמוספירה. הגובה משפיע באופן ישיר על הטמפרטורה שבה נוצרים העננים, וזו משפיעה על הרכבם – האם הם מורכבים מטיפות מים נוזליים, מגבישי קרח, או משניהם. נהוג לחלק את העננים לשלוש קטגוריות גובה עיקריות:</p>

    <h4>עננים גבוהים (High Clouds)</h4>
    <ul>
        <li><strong>שמות נפוצים:</strong> <strong>צירוס</strong> (Cirrus), <strong>צירוסטרטוס</strong> (Cirrostratus), <strong>צירוקומולוס</strong> (Cirrocumulus).</li>
        <li><strong>גובה טיפוסי:</strong> לרוב מעל 6 ק"מ (כ-20,000 רגל) מעל פני הקרקע, באזורים קרים מאוד של האטמוספירה.</li>
        <li><strong>מאפיינים ויזואליים:</strong> עננים אלו נוצרים אך ורק מגבישי קרח ולכן הם לרוב דקים, שקופים למחצה, או בעלי מראה סיבי עדין, לעיתים נראים כמו נוצות, שערות סוס או כתמים קטנים מסודרים בשורות.</li>
        <li><strong>מזג אוויר מקושר:</strong> עננים גבוהים לרוב קשורים למזג אוויר בהיר, אך הופעתם יכולה לעיתים לבשר על שינוי מתקרב, במיוחד אם הם הופכים צפופים יותר. ענני צירוס מצביעים לעיתים על התקרבות של חזית חמה. ענני צירוסטרטוס יכולים ליצור תופעות אופטיות יפות כמו הילה סביב השמש או הירח. עננים אלו אינם מורידים משקעים שמגיעים לקרקע.</li>
    </ul>

    <h4>עננים בינוניים (Mid-level Clouds)</h4>
    <ul>
        <li><strong>שמות נפוצים:</strong> <strong>אלטוקומולוס</strong> (Altocumulus), <strong>אלטוסטרטוס</strong> (Altostratus).</li>
        <li><strong>גובה טיפוסי:</strong> בין 2 ל-6 ק"מ (כ-6,500 עד 20,000 רגל). בגבהים אלו העננים יכולים להיות מורכבים מטיפות מים, גבישי קרח, או שילוב של שניהם, תלוי בטמפרטורה הספציפית.</li>
        <li><strong>מאפיינים ויזואליים:</strong> ענני <strong>אלטוקומולוס</strong> נראים בדרך כלל ככתמים או גושים לבנים עד אפורים, לעיתים קרובות מסודרים בשורות או קבוצות (דמוי "כבשים" או "גלים"). ענני <strong>אלטוסטרטוס</strong> יוצרים שכבה אחידה ורחבה של עננות אפרפרה או כחלחלה, שיכולה לטשטש את השמש או הירח ולהפוך אותם לדיסק בהיר ומטושטש ("שמש או ירח חלבי").</li>
        <li><strong>מזג אוויר מקושר:</strong> עננים בינוניים קשורים לעננות בולטת יותר ומהווים לעיתים קרובות אינדיקציה לשינוי במזג האוויר. אלטוסטרטוס יכול להוריד גשם או שלג קל, אך לרוב הוא אינו כבד או ממושך. אלטוקומולוס בדרך כלל אינו מוריד משקעים, אך יכול להעיד על אי יציבות באטמוספירה.</li>
    </ul>

    <h4>עננים נמוכים (Low Clouds)</h4>
    <ul>
        <li><strong>שמות נפוצים:</strong> <strong>סטרטוס</strong> (Stratus), <strong>סטרטוקומולוס</strong> (Stratocumulus), <strong>נימבוסטרטוס</strong> (Nimbostratus).</li>
        <li><strong>גובה טיפוסי:</strong> מתחת ל-2 ק"מ (כ-6,500 רגל). מורכבים בעיקר מטיפות מים נוזליים (אלא אם הטמפרטורה קרובה לאפס או מתחתיה, ואז יכולים להכיל גם גבישי קרח).</li>
        <li><strong>מאפיינים ויזואליים:</strong> ענני <strong>סטרטוס</strong> הם שכבה אחידה, שטוחה ונמוכה של עננות אפורה, דמוית ערפל שלא הגיע עד לקרקע. ענני <strong>סטרטוקומולוס</strong> נראים כגושים, גלילים או פסים אפורים או לבנבנים המסודרים בשכבה די נמוכה. ענני <strong>נימבוסטרטוס</strong> הם שכבה אפורה, כהה ועבה המכסה את כל השמיים וממנה יורדים משקעים.</li>
        <li><strong>מזג אוויר מקושר:</strong> סטרטוס קשור לעיתים קרובות לטפטוף קל מאוד (מזרעה) או ערפל קל. סטרטוקומולוס בדרך כלל לא מוריד משקעים משמעותיים, אך יכול להתפתח לענני גשם. <strong>נימבוסטרטוס</strong> הוא ענן הגשם הטיפוסי של גשם קל עד בינוני, אך מתמשך לאורך שעות.</li>
    </ul>

    <h3>עננים בעלי התפתחות אנכית משמעותית</h3>
    <p>ישנם גם עננים שלא משתלבים באופן מלא בסיווג לפי גובה הבסיס בלבד, מכיוון שהם מתפתחים לגובה רב מאוד, לעיתים על פני כל שכבות הגובה. ענני <strong>קומולוס</strong> (Cumulus) נוצרים עקב הסעת חום אנכית (קונבקציה).</p>
    <ul>
        <li><strong>קומולוס:</strong> לענני קומולוס יש בסיס נמוך (בדרך כלל מתחת ל-2 ק"מ) ופסגות כיפתיות או "כרוביות" המתנשאות לגובה משתנה. ענני קומולוס קטנים ומבודדים ("קומולוס הומליס") הם סימן מובהק למזג אוויר בהיר ונעים. אם תנאי האטמוספירה יציבים פחות, הם יכולים לגדול ל"קומולוס קונג'סטוס" – עננים גדולים יותר שיכולים להוריד ממטרים קצרים ועזים.</li>
        <li><strong>קומולונימבוס:</strong> אלו הם "מלכי העננים" וענני הסערה המפוארים והמסוכנים ביותר. ענני קומולונימבוס (Cumulonimbus) מתחילים מבסיס נמוך מאוד (לעיתים קרובות פחות מק"מ), אך מתנשאים לגובה רב מאוד, לעיתים עד לשכבות הגבוהות ביותר של האטמוספירה, ואף מגיעים לצורת "סדן" אופיינית בפסגתם כשהם נתקלים בטרופופאוזה. הם קשורים לגשם כבד מאוד, ברד, ברקים, רעמים, רוחות סוערות ואף טורנדו. ראיית קומולונימבוס היא אינדיקציה ברורה לסופה מתקרבת או מתפתחת.</li>
    </ul>

    <h3>סיכום: השמיים כמפה למזג האוויר</h3>
    <p>היכולת לזהות את סוגי העננים העיקריים מאפשרת לנו לקבל תמונת מצב מיידית על מה שקורה באטמוספירה מעלינו ולהסיק מסקנות שימושיות לגבי מזג האוויר הצפוי בסביבתנו הקרובה. שמיים המכוסים בשכבת אלטוסטרטוס אפורה עשויים לבשר גשם קל, בעוד ענני קומולוס יום יפה מבטיחים יום שמשי. ראיית ענן קומולונימבוס אדיר באופק היא קריאת כיוון ברורה לחפש מחסה אם מתפתחת סופה. התבוננות קבועה בשמיים ולמידת שפת העננים היא דרך מרתקת להתחבר לעולם הטבע ולהבין טוב יותר את הכוחות המעצבים את מזג האוויר.</p>
</div>


<script>
    document.addEventListener('DOMContentLoaded', () => {
        const cloudImage = document.getElementById('cloud-image');
        const heightChoices = document.getElementById('height-choices').querySelectorAll('button');
        const weatherChoices = document.getElementById('weather-choices').querySelectorAll('button');
        const submitButton = document.getElementById('submit-answer');
        const feedbackArea = document.getElementById('feedback-area');
        const feedbackText = document.getElementById('feedback-text');
        const nextCloudButton = document.getElementById('next-cloud');
        const showExplanationButton = document.getElementById('show-explanation');
        const explanationSection = document.getElementById('explanation-section');

        let currentCloudIndex = 0;
        let selectedHeight = null;
        let selectedWeather = null;

        // Data for cloud examples - Added a few more examples for variety
        const cloudsData = [
             {
                image: 'https://res.cloudinary.com/dqk165j3e/image/upload/v1719334708/cirrus_i7vgs7.jpg', // Placeholder URL for Cirrus
                correctHeight: 'גבוה',
                correctWeather: 'שמיים בהירים / עננות קלה', // Slightly refined weather description
                exactType: 'צירוס (Cirrus)',
                explanation: 'ענני <strong>צירוס</strong> הם עננים גבוהים ודקים המורכבים מגבישי קרח. לרוב הם מופיעים בשמיים בהירים או קשורים לשינוי עדין במזג האוויר. אינם מורידים משקעים שמגיעים לקרקע.'
            },
            {
                image: 'https://res.cloudinary.com/dqk165j3e/image/upload/v1719334708/altostratus_n5yixu.jpg', // Placeholder URL for Altostratus
                correctHeight: 'בינוני',
                correctWeather: 'גשם קל / טפטוף', // Made weather more specific to Altostratus potential
                exactType: 'אלטוסטרטוס (Altostratus)',
                explanation: 'ענני <strong>אלטוסטרטוס</strong> הם עננים בינוניים היוצרים שכבה אחידה ואפרפרה. הם יכולים לטשטש את השמש או הירח. עשויים להוריד גשם קל או שלג קל אך לרוב לא משמעותי או ממושך.'
            },
             {
                image: 'https://res.cloudinary.com/dqk165j3e/image/upload/v1719334708/stratus_cz4i2j.jpg', // Placeholder URL for Stratus
                correctHeight: 'נמוך',
                correctWeather: 'גשם קל / טפטוף', // Or ערפל
                exactType: 'סטרטוס (Stratus)',
                explanation: 'ענני <strong>סטרטוס</strong> הם עננים נמוכים מאוד היוצרים שכבה אחידה ושטוחה, דמוית ערפל שאינו נוגע בקרקע. קשורים לעיתים קרובות לטפטוף קל מאוד (מזרעה) או ערפל קל.'
            },
            {
                image: 'https://res.cloudinary.com/dqk165j3e/image/upload/v1719334708/nimbostratus_ix4j3e.jpg', // Placeholder URL for Nimbostratus
                correctHeight: 'נמוך', // Base is low
                correctWeather: 'גשם מתמשך / סופה', // Nimbostratus brings continuous rain
                exactType: 'נימבוסטרטוס (Nimbostratus)',
                explanation: 'ענני <strong>נימבוסטרטוס</strong> הם שכבה עבה וכהה של עננים נמוכים, המורידה גשם או שלג קל עד בינוני ומתמשך לאורך שעות. הם מכסים את השמיים לחלוטין.'
            },
             {
                image: 'https://res.cloudinary.com/dqk165j3e/image/upload/v1719334708/altocumulus_k6m9a8.jpg', // Placeholder URL for Altocumulus
                correctHeight: 'בינוני',
                correctWeather: 'שמיים בהירים / עננות קלה', // Altocumulus often doesn't bring rain itself
                exactType: 'אלטוקומולוס (Altocumulus)',
                explanation: 'ענני <strong>אלטוקומולוס</strong> הם עננים בינוניים הנראים כמו כתמים או גושים מעוגלים. לעיתים קרובות מסודרים בשורות. מצביעים על עננות ויכולים להקדים שינוי, אך בדרך כלל אינם מורידים משקעים.'
            },
             {
                image: 'https://res.cloudinary.com/dqk165j3e/image/upload/v1719334708/cumulus_humilis_u97u1b.jpg', // Placeholder for small Cumulus
                correctHeight: 'נמוך',
                correctWeather: 'שמיים בהירים / עננות קלה',
                exactType: 'קומולוס הומליס (Cumulus Humilis)',
                explanation: 'ענני <strong>קומולוס הומליס</strong> הם ענני יום יפה טיפוסיים. יש להם בסיס שטוח ונמוך וכיפות קטנות. הם מעידים על מזג אוויר יציב ואינם מורידים משקעים.'
            },
             {
                image: 'https://res.cloudinary.com/dqk165j3e/image/upload/v1719334708/cumulus_congestus_b0t8k4.jpg', // Placeholder for larger Cumulus
                correctHeight: 'נמוך', // Base is low
                correctWeather: 'גשם קל / טפטוף', // Can bring showers
                exactType: 'קומולוס קונג\'סטוס (Cumulus Congestus)',
                explanation: 'ענני <strong>קומולוס קונג\'סטוס</strong> הם התפתחות של ענני קומולוס קטנים יותר, עם כיפות גבוהות ובולטות יותר. הם מעידים על אי יציבות גוברת באטמוספירה ויכולים להוריד ממטרים קצרים וקלים עד בינוניים.'
            },
            {
                image: 'https://res.cloudinary.com/dqk165j3e/image/upload/v1719334708/cumulonimbus_z9k8j0.jpg', // Placeholder URL for Cumulonimbus
                correctHeight: 'נמוך', // Classify by base height for the quiz
                correctWeather: 'גשם מתמשך / סופה', // The most significant weather
                exactType: 'קומולונימבוס (Cumulonimbus)',
                explanation: 'ענני <strong>קומולונימבוס</strong> הם ענני סערה אדירים בעלי התפתחות אנכית עצומה, עם בסיס נמוך מאוד ופסגה שיכולה להגיע לגבהים קיצוניים. הם קשורים לגשם כבד, ברקים, רעמים, ברד ורוחות חזקות. ענן זה הוא סמן מובהק לסופה.'
            }
        ];

        function loadCloud(index) {
            if (index >= cloudsData.length) {
                // End of quiz
                feedbackHTML = '<p class="correct" style="font-size: 1.3em;"><strong>מדהים! סיימת את כל העננים בהצלחה!</strong></p>';
                feedbackHTML += '<p>עכשיו אתה מוכן לקרוא את שפת השמיים בעצמך!</p>';
                 feedbackText.innerHTML = feedbackHTML;
                 feedbackArea.classList.remove('hidden');
                 feedbackArea.style.maxHeight = '300px'; // Adjust height for final message
                 feedbackArea.style.opacity = '1';
                 submitButton.classList.add('hidden');
                 nextCloudButton.classList.add('hidden');
                 // Hide question area or disable
                 document.getElementById('question-area').style.display = 'none';

                 // Optional: Reset button for new quiz
                 // const resetButton = document.createElement('button');
                 // resetButton.textContent = 'התחל מחדש';
                 // resetButton.classList.add('next-button'); // Use same style
                 // resetButton.addEventListener('click', () => {
                 //     document.getElementById('question-area').style.display = 'block';
                 //     loadCloud(0);
                 // });
                 // feedbackArea.appendChild(resetButton);


                 return; // Exit function
            }

            currentCloudIndex = index;
            const cloud = cloudsData[currentCloudIndex];
             // Animate image fade-in or position change? Simple fade for now.
             cloudImage.style.opacity = '0'; // Start faded
             cloudImage.src = cloud.image; // Change source
             cloudImage.onload = () => { // Fade in after load
                 cloudImage.style.opacity = '1';
             };


            // Reset selections and feedback display
            selectedHeight = null;
            selectedWeather = null;
            heightChoices.forEach(button => button.classList.remove('selected'));
            weatherChoices.forEach(button => button.classList.remove('selected'));

            // Animate feedback area hiding
             feedbackArea.style.maxHeight = '0';
             feedbackArea.style.opacity = '0';
             // Add a delay before actually hiding to allow animation
             setTimeout(() => {
                 feedbackArea.classList.add('hidden');
                 feedbackText.innerHTML = '';
                 submitButton.classList.remove('hidden');
                 nextCloudButton.classList.add('hidden');
                 submitButton.disabled = true; // Disable submit until choices are made
             }, 700); // Matches max-height transition duration


        }

        function handleChoiceClick(event, type) {
            const button = event.target;
            const choice = button.getAttribute('data-choice');
            
            // Deselect previous choice of this type and apply effect
            const choiceButtons = type === 'height' ? heightChoices : weatherChoices;
            choiceButtons.forEach(btn => {
                 if (btn !== button && btn.classList.contains('selected')) {
                     btn.classList.remove('selected');
                     // Optional: add deselect animation class briefly
                 }
             });
            
            // Select the current choice and apply effect
            if (button.classList.contains('selected')) {
                // If already selected, deselect it
                button.classList.remove('selected');
                 if (type === 'height') selectedHeight = null;
                 else selectedWeather = null;
            } else {
                // If not selected, select it
                button.classList.add('selected');
                 if (type === 'height') selectedHeight = choice;
                 else selectedWeather = choice;
            }

            // Enable submit if both choices are made
            submitButton.disabled = !(selectedHeight && selectedWeather);
             // Optional: Add a visual cue when button becomes enabled - handled by CSS :disabled
        }

        heightChoices.forEach(button => {
            button.addEventListener('click', (e) => handleChoiceClick(e, 'height'));
        });

        weatherChoices.forEach(button => {
            button.addEventListener('click', (e) => handleChoiceClick(e, 'weather'));
        });

        submitButton.addEventListener('click', () => {
            if (!selectedHeight || !selectedWeather) {
                // Should not happen if button is disabled, but good as a fallback
                // Use a more styled modal or message later if needed
                alert('אנא בחר גם גובה וגם סוג מזג אוויר כדי לבדוק את תשובתך.');
                return;
            }

            const cloud = cloudsData[currentCloudIndex];
            let feedbackHTML = '';
            let isHeightCorrect = (selectedHeight === cloud.correctHeight);

             // Allow multiple correct weather options if defined in data (current data uses string, so Array.isArray is false)
             const correctWeatherOptions = Array.isArray(cloud.correctWeather) ? cloud.correctWeather : [cloud.correctWeather];
             const isWeatherCorrect = correctWeatherOptions.includes(selectedWeather);

            // Check Height
            if (isHeightCorrect) {
                feedbackHTML += `<p class="correct">✅ <strong>זיהוי גובה נכון!</strong> בחרת: "${selectedHeight}". הגובה האופייני לבסיס ענן זה הוא אכן בקטגוריית ${selectedHeight}.</p>`;
            } else {
                feedbackHTML += `<p class="incorrect">❌ <strong>זיהוי גובה שגוי.</strong> בחרת: "${selectedHeight}". הגובה האופייני לבסיס ענן זה הוא בקטגוריית ${cloud.correctHeight}.</p>`;
            }

             // Check Weather
            if (isWeatherCorrect) {
                feedbackHTML += `<p class="correct">✅ <strong>זיהוי מזג אוויר נכון!</strong> בחרת: "${selectedWeather}". מזג אוויר זה אכן קשור לענן מסוג זה.</p>`;
            } else {
                 const weatherFeedbackText = correctWeatherOptions.length > 1 ? `אחת מהאפשרויות הבאות: "${correctWeatherOptions.join('", "')}"` : `"${correctWeatherOptions[0]}"`;
                feedbackHTML += `<p class="incorrect">❌ <strong>זיהוי מזג אוויר שגוי.</strong> בחרת: "${selectedWeather}". מזג האוויר הסביר ביותר המקושר לענן זה הוא: ${weatherFeedbackText}.</p>`;
            }

            // Add general info and explanation
            feedbackHTML += `<p><strong>סוג הענן המדויק:</strong> ${cloud.exactType}</p>`;
            feedbackHTML += `<p>${cloud.explanation}</p>`; // Includes HTML bold tags from data

            feedbackText.innerHTML = feedbackHTML;

            // Animate feedback area appearance
            feedbackArea.classList.remove('hidden');
            // Trigger reflow to restart transition if already displayed
            void feedbackArea.offsetWidth;
            feedbackArea.style.maxHeight = '500px'; // Set to a value larger than content
            feedbackArea.style.opacity = '1';


            submitButton.classList.add('hidden');
             // Add a slight delay before showing next button for smoother flow
             setTimeout(() => {
                 nextCloudButton.classList.remove('hidden');
             }, 500); // Show next button after feedback animation starts
        });

        nextCloudButton.addEventListener('click', () => {
            loadCloud(currentCloudIndex + 1);
        });
        
        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationSection.classList.contains('hidden');
            if (isHidden) {
                explanationSection.classList.remove('hidden');
                 // Trigger reflow for animation
                 void explanationSection.offsetWidth;
                 explanationSection.style.maxHeight = '2000px'; // A large value to ensure it fits
                 explanationSection.style.opacity = '1';

                showExplanationButton.textContent = 'הסתר הסבר מלא על זיהוי עננים';
                 showExplanationButton.style.backgroundColor = '#dc3545'; /* צבע אדום להסתרה */
                 showExplanationButton.style.boxShadow = '0 4px 10px rgba(220, 53, 69, 0.3)';
            } else {
                 explanationSection.style.maxHeight = '0';
                 explanationSection.style.opacity = '0';
                 // Delay adding 'hidden' class until animation is complete
                 setTimeout(() => {
                     explanationSection.classList.add('hidden');
                 }, 700); // Matches transition duration

                showExplanationButton.textContent = 'הצג הסבר מלא על זיהוי עננים';
                 showExplanationButton.style.backgroundColor = '#6c757d'; /* צבע אפור רגיל */
                 showExplanationButton.style.boxShadow = '0 4px 10px rgba(108, 117, 125, 0.3)';
            }
        });

        // Initial load
        loadCloud(0);
    });
</script>
```