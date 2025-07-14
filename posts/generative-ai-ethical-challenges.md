---
title: "AI יוצרת: צומת הדרכים האתי"
english_slug: generative-ai-ethical-challenges
category: "מדעי המחשב"
tags:
  - בינה מלאכותית
  - אתיקה
  - AI יוצרת
  - דיפייק
  - זכויות יוצרים
---
<div class="intro-section">
  <h1>AI יוצרת: צומת הדרכים האתי</h1>
  <p>רגע... מה שאני רואה/שומע/קורא עכשיו... זה אמיתי? בעידן בו כל אחד יכול להפוך רעיון למציאות דיגיטלית שנראית ומרגישה אמיתית בלחיצת כפתור, הכוח ליצור תוכן בקלות מדהימה מעלה שאלות עמוקות על אחריות, אמת וקניין רוחני. בואו נצלול פנימה ונראה אילו החלטות הייתם מקבלים כשאתם עומדים בצומת הדרכים האתי של AI יוצרת.</p>
</div>

<div class="app-container">
    <div id="scenario-container" class="screen active">
        <h2 class="screen-title">הדילמה של היוצר</h2>
        <p id="scenario-text" class="scenario-text"></p>
        <div id="choices-container" class="choices-grid"></div>
    </div>
    <div id="result-container" class="screen">
        <h2 class="screen-title">תוצאות המעשה הדיגיטלי שלך</h2>
        <div class="result-box">
            <h3>הדמיית התוצאה:</h3>
            <div id="result-content" class="result-content"></div>
        </div>
        <div class="feedback-box">
            <h3>הזווית האתית:</h3>
            <div id="feedback-content" class="feedback-content"></div>
        </div>
        <button id="next-scenario-btn" class="action-button">לדילמה הבאה</button>
    </div>
    <div id="end-container" class="screen">
        <h2 class="screen-title">סוף המסע... בינתיים</h2>
        <p>סיימת את התרחישים. זכור: הכוח ליצור מגיע עם אחריות גדולה. בכל פעם שאתה משתמש ב-AI יוצרת, עצור וחשוב - האם זה אחראי? האם זה הוגן? האם זה אמיתי? שימוש ביקורתי ואתי ב-AI מעצב את העתיד הדיגיטלי של כולנו.</p>
        <button id="restart-btn" class="action-button">התחל אתגר חדש</button>
    </div>
</div>

<button id="toggle-explanation-btn" class="toggle-button">מה מסתתר מאחורי הקלעים? (הסבר מורחב)</button>

<div id="explanation-container" class="explanation-container" style="display: none;">
    <h2>הסבר מעמיק: האתגרים האתיים של AI יוצרת</h2>

    <section>
        <h3>מהי בינה מלאכותית יוצרת (Generative AI)?</h3>
        <p>תחשבו עליה כעל אמן דיגיטלי שיכול לייצר משהו חדש לגמרי – טקסטים מרתקים, תמונות מרהיבות, קטעי קול ריאליסטיים, מוזיקה, קוד ועוד – והכול על בסיס אימונים על כמויות אדירות של נתונים קיימים. היא לא רק מנתחת; היא בוראת (או לכל הפחות, מחקה ביצירתיות רבה).</p>
    </section>

    <section>
        <h3>דיפייק (Deepfake): כשמראה עיניים מטעה</h3>
        <p>דיפייק היא טכנולוגיה עוצמתית של AI שיכולה ליצור סרטונים, הקלטות קוליות או תמונות מזויפים שנראים ומרגישים אמיתיים לחלוטין. היא יכולה לגרום לאדם להגיד או לעשות דברים שמעולם לא אמר או עשה.</p>
        <ul>
            <li><strong>פגיעה הרסנית באנשים:</strong> דיפייקים זדוניים הם כלי נשק דיגיטלי. הם יכולים לשמש להכפשה, סחיטה, פגיעה בפרטיות ובהרס מוניטין של כל אדם – מפורסם או אנונימי.</li>
            <li><strong>ערעור האמון הציבורי:</strong> כשקשה להבדיל בין תיעוד אמיתי למזויף, האמון בחדשות, בעדויות ובמידע בכלל נפגע אנושות. זה כר פורה להפצת פייק ניוז בקנה מידה חסר תקדים.</li>
            <li><strong>סוגיית ההסכמה:</strong> יצירת דיפייק של אדם ללא ידיעתו או הסכמתו היא פלישה אלימה למרחב האישי שלו ושימוש בדמותו ללא רשות.</li>
        </ul>
    </section>

    <section>
        <h3>קניין רוחני וזכויות יוצרים: מבוך דיגיטלי חדש</h3>
        <p>AI יוצרת מטלטלת את עולם הקניין הרוחני ומעלה שאלות משפטיות ואתיות מורכבות:</p>
        <ul>
            <li><strong>למי שייכת היצירה?:</strong> אם AI יצרה תמונה מדהימה לפי הפרומפט שלך, מי הבעלים? אתה שנתת את ההוראה? החברה שפיתחה את המודל? או של-AI יש סוג של זכות? החוק עוד מתלבט.</li>
            <li><strong>הצל של נתוני האימון:</strong> המודלים אומנו על מיליוני יצירות קיימות, רבות מהן מוגנות בזכויות יוצרים. האם התוצרים של ה-AI 'נגועים' בזכויות אלה? האם שימוש ביצירות להכשרת AI נחשב שימוש הוגן או הפרה?</li>
            <li><strong>"בסגנון של..." - גבול דק:</strong> חיקוי סגנון הוא לגיטימי באמנות אנושית. אבל כש-AI מחקה סגנון של אמן ספציפי בצורה מדויקת להפליא, עד כדי הטעיה או ניצול המוניטין שלו – האם זה הוגן? היכן עובר הקו האדום?</li>
        </ul>
    </section>

     <section>
        <h3>עוד אתגרים בדרך...</h3>
        <p>AI יוצרת אינה חפה מבעיות נוספות: היא יכולה לשכפל ולהעצים הטיות קיימות בנתוני האימון, לייצר תוכן פוגעני בקלות מדאיגה, ומקשה עלינו עוד יותר לדעת מה אמת ומה שקר בעולם הדיגיטלי.</p>
     </section>

    <section>
        <h3>הדרך קדימה: אחריות וביקורתיות</h3>
        <p>ככל שכלי ה-AI הופכים לנגישים וחזקים יותר, כך גדלה חשיבות החינוך, המודעות והפיתוח של כלים לזיהוי תוכן סינתטי. כיוצרים, עלינו לשקול היטב את ההשפעה של התוכן שאנו מייצרים. כצרכנים, עלינו לצרוך מידע דיגיטלי בעין ביקורתית ולזכור: לא כל מה שנראה אמיתי, באמת קיים.</p>
    </section>
</div>

<style>
    /* --- עיצוב כללי --- */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: #f4f7f6; /* רקע עדין */
        color: #333;
    }

    h1, h2, h3 {
        color: #0a4f6f; /* כחול כהה יותר לכותרות */
        margin-bottom: 15px;
        font-weight: bold;
    }

    h1 {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 20px;
        color: #00334e; /* כחול כהה ראשי */
    }

    h2 {
        font-size: 1.8rem;
        border-bottom: 2px solid #a0d2db; /* קו תחתון דקורטיבי */
        padding-bottom: 5px;
        margin-top: 25px;
    }

    h3 {
        font-size: 1.4rem;
        margin-top: 20px;
        color: #0a4f6f;
    }

    p {
        margin-bottom: 15px;
    }

    /* --- מבנה האפליקציה והמעברים --- */
    .app-container {
        background-color: #ffffff; /* רקע לבן נקי לאפליקציה */
        padding: 30px;
        border-radius: 12px;
        margin: 20px auto; /* מרכוז */
        max-width: 700px; /* רוחב מקסימלי */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* צל עדין */
        overflow: hidden; /* לוודא שאנימציות לא פורצות גבולות */
        position: relative; /* למיקום מוחלט של מסכים */
    }

    .screen {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        padding: 30px; /* פאדינג זהה ל-app-container */
        transition: transform 0.6s ease-in-out, opacity 0.6s ease-in-out; /* אנימציית מעבר */
        opacity: 0;
        pointer-events: none; /* לא ניתן ללחוץ כשהוא נסתר */
        transform: translateX(100%); /* התחל מימין */
        box-sizing: border-box; /* ודא פאדינג בפנים */
        background-color: #ffffff; /* רקע לבן גם למסכים הפנימיים */
        display: flex; /* שימוש בפלקס לריכוז או סידור תוכן */
        flex-direction: column;
        justify-content: flex-start; /* התוכן מתחיל למעלה */
    }

    .screen.active {
        position: static; /* מסך פעיל חוזר לזרימה רגילה */
        opacity: 1;
        pointer-events: auto; /* ניתן ללחוץ */
        transform: translateX(0); /* חוזר למרכז */
         transition: transform 0.6s ease-in-out, opacity 0.6s ease-in-out; /* אנימציית כניסה */
         height: auto; /* גובה אוטומטי */
    }

     /* טיפול במסכים שאינם פעילים - למקרה שלא משתמשים ב-position:absolute */
     /* alternative handling if absolute positioning causes issues */
     /*
     .screen:not(.active) {
         display: none;
     }
     */


    .screen-title {
        text-align: center;
        margin-top: 0;
        margin-bottom: 30px;
        color: #0a4f6f;
        font-size: 1.6rem;
    }


    /* --- תוכן האפליקציה --- */
    .scenario-text {
        font-size: 1.1rem;
        font-weight: normal; /* לא מודגש מדי */
        margin-bottom: 25px;
        color: #555;
        text-align: center;
    }

    .choices-grid {
        display: grid; /* שימוש בגריד לסידור כפתורים */
        gap: 15px; /* רווח בין כפתורים */
        grid-template-columns: 1fr; /* כפתור אחד בטור */
        width: 100%; /* מילוי רוחב */
        margin-top: auto; /* דחיפה לתחתית המסך */
    }

    .choice-btn {
        padding: 15px 20px;
        font-size: 1rem;
        cursor: pointer;
        border: none;
        border-radius: 8px;
        background-color: #0077b6; /* כחול בהיר */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    .choice-btn:hover {
        background-color: #023e8a; /* כחול כהה יותר */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    .choice-btn:active {
        transform: scale(0.98); /* אפקט לחיצה */
    }

    .result-box, .feedback-box {
        margin-top: 20px;
        padding: 20px;
        border-radius: 8px;
        background-color: #e9ecef; /* רקע אפור בהיר */
        border: 1px solid #ced4da; /* גבול עדין */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05); /* צל פנימי */
    }
     .result-box h3, .feedback-box h3 {
        margin-top: 0;
        color: #00334e; /* כותרת כהה יותר */
        font-size: 1.2rem;
        border-bottom: 1px solid #ced4da;
        padding-bottom: 8px;
        margin-bottom: 15px;
     }

    .result-content {
         color: #555;
         font-style: italic;
     }

    .feedback-content {
         color: #333;
         font-weight: normal;
     }

    .action-button {
        display: block; /* כפתור מילוי רוחב */
        width: 100%;
        padding: 12px 20px;
        font-size: 1.1rem;
        cursor: pointer;
        border: none;
        border-radius: 8px;
        margin-top: 30px;
        background-color: #28a745; /* ירוק להצלחה/המשך */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    .action-button:hover {
        background-color: #218838; /* ירוק כהה יותר */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    .action-button:active {
        transform: scale(0.98);
    }

    #restart-btn {
        background-color: #0077b6; /* כחול לאתחול */
    }
    #restart-btn:hover {
        background-color: #023e8a;
    }


    /* --- כפתור הצגת הסבר --- */
    .toggle-button {
        display: block;
        width: auto;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 1rem;
        cursor: pointer;
        border: 1px solid #6c757d;
        border-radius: 8px;
        background-color: #e9ecef; /* רקע בהיר */
        color: #333;
        transition: background-color 0.3s ease, border-color 0.3s ease;
        text-align: center;
    }
    .toggle-button:hover {
        background-color: #ced4da;
        border-color: #5a6268;
    }
    .toggle-button:active {
         transform: scale(0.98);
    }


    /* --- הסבר מורחב --- */
    .explanation-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        margin: 20px auto;
        max-width: 700px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid #ced4da;
    }

    .explanation-container section {
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px dashed #e9ecef;
    }
     .explanation-container section:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }

    .explanation-container h2 {
        text-align: center;
        border-bottom: 2px solid #a0d2db;
        padding-bottom: 10px;
        margin-bottom: 25px;
        color: #00334e;
    }

    .explanation-container h3 {
         color: #0a4f6f;
         font-size: 1.3rem;
     }

    .explanation-container ul {
        margin-top: 10px;
        padding-right: 25px; /* Hebrew RTL list indent */
        list-style: disc outside; /* Standard disc bullets */
    }
    .explanation-container li {
        margin-bottom: 10px;
        color: #555;
    }

    /* --- אנימציות נוספות (אופציונליות) --- */
    .fade-in {
        animation: fadeIn 0.8s ease-out forwards;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

     /* --- התאמה למובייל --- */
    @media (max-width: 600px) {
        body {
            padding: 15px;
        }
        h1 {
            font-size: 1.8rem;
        }
        h2 {
            font-size: 1.4rem;
        }
        h3 {
             font-size: 1.2rem;
         }
        .app-container, .explanation-container {
            padding: 20px;
             margin: 15px auto;
        }
        .screen {
            padding: 20px;
        }
        .choice-btn {
            font-size: 0.95rem;
            padding: 12px 15px;
        }
        .action-button {
            font-size: 1rem;
            padding: 10px 15px;
        }
         .toggle-button {
             font-size: 0.9rem;
             padding: 10px 20px;
         }
         .choices-grid {
             gap: 10px;
         }
    }

</style>

<script>
    const scenarios = [
        {
            id: 1,
            dilemma: "אתה עיתונאי החוקר שחיתות מקומית. ראיות קיימות, אבל כדי להמחיש את הבעיה לציבור, היית רוצה להראות פוליטיקאי מרכזי מודה בפה מלא. אין לך הקלטה אמיתית כזו. איך תשתמש ב-AI?",
            choices: [
                {
                    text: "צור וידאו דיפייק פוטו-ריאליסטי של הפוליטיקאי 'מודה' בדיוק בדברים שמצאת בראיות.",
                    result: "<p><b>הדמיית תוצאה:</b> סרטון מזויף ומטלטל שרץ ברשת ויוצר סערה, רבים מאמינים שהוא אמיתי. מוניטין הפוליטיקאי נהרס בן לילה. האם זה שירת את האמת או יצר שקר חדש?</p>",
                    feedback: "<b>משוב אתי:</b> 🚫 <b>בעייתי ביותר!</b> יצירת דיפייק ריאליסטי של אדם ללא הסכמתו, במיוחד לצרכים עיתונאיים, היא הפרה אתית ואף פלילית חמורה. זהו זיוף מסוכן הפוגע באדם, מערער את אמון הציבור במדיה, ומשחק לידי מפיצי פייק ניוז. גם אם המטרה 'טובה' (חשיפת שחיתות), האמצעי רעיל ומזיק."
                },
                {
                    text: "השתמש ב-AI ליצירת איור סמלי או קריקטורה שמייצגת את רעיון השחיתות והקשר לפוליטיקאי (בלי ליצור מצג שווא של אמירה אמיתית).",
                    result: "<p><b>הדמיית תוצאה:</b> איור ויזואלי ברור אך סמלי, המצורף לכתבה החושפנית המבוססת על ראיות אמיתיות. הציבור מבין את המסר, והכתבה זוכה לתשומת לב בזכות האילוסטרציה המקורית.</p>",
                    feedback: "<b>משוב אתי:</b> ✅ <b>בחירה אחראית.</b> שימוש ב-AI ככלי עזר ויזואלי ליצירת ייצוגים סמליים הוא דרך לגיטימית ואתית. אתה מעביר את המסר החשוב מבלי לזייף מציאות או לפגוע באדם באופן אישי באמצעות דיפייק. זהו שימוש יצירתי ואחראי בטכנולוגיה בשירות האמת העיתונאית (המבוססת על ראיות!)."
                }
            ]
        },
        {
            id: 2,
            dilemma: "אתה מעצב גרפי עצמאי שמכין פוסטר קמפיין למותג גדול. הלקוח דורש עיצוב חדשני בסגנון ספציפי מאוד, שמאפיין אמן דיגיטלי מפורסם שכולכם מעריצים (שמו XYZ). איך תשתמש ב-AI ליצירת הרקע לפוסטר?",
            choices: [
                {
                    text: "הכנס לפרומפט: 'צור רקע בסגנון המדויק של האמן XYZ'.",
                    result: "<p><b>הדמיית תוצאה:</b> ה-AI יוצרת רקע שנראה כמעט זהה ליצירות של XYZ - אותם צבעים, אותם מוטיבים, אותה תחושה. הלקוח מתלהב מהתוצאה ה'מושלמת'.</p>",
                    feedback: "<b>משוב אתי:</b> ⚠️ <b>גבולי ומסוכן.</b> למרות שסגנון כשלעצמו אינו מוגן בזכויות יוצרים, יצירה שמחקה סגנון של אמן ספציפי בצורה כל כך קרובה עלולה להיחשב כניצול בלתי הוגן של המוניטין שלו, הטעיית הציבור לגבי מקור היצירה, ואף עלולה לגעת בהפרת זכויות אם נתוני האימון כללו יצירות ספציפיות שלו. זה פוגע במקוריות ועלול לעורר בעיות משפטיות ואתיות קשות."
                },
                {
                    text: "הכנס לפרומפט: 'צור רקע בסגנון (תיאור מפורט של הסגנון) בהשראת אמנות דיגיטלית מודרנית', תוך הדגשה שזו לא אמנות של אמן ספציפי.",
                    result: "<p><b>הדמיית תוצאה:</b> ה-AI יוצרת רקע מקורי ששואב השראה מהמאפיינים הכלליים של הסגנון הנדרש (צבעים, טקסטורות, אווירה), אך אינו חיקוי ישיר של אמן ספציפי. הלקוח מרוצה מהיצירתיות והמקוריות.</p>",
                    feedback: "<b>משוב אתי:</b> ✅ <b>בחירה מומלצת.</b> שימוש ב-AI ככלי ליצירת השראה או יישום מאפייני סגנון כלליים, מבלי להתמקד בחיקוי אמן ספציפי, הוא שימוש אתי. אתה משתמש בטכנולוגיה כדי להאיץ את תהליך היצירה ולקבל רעיונות חדשים, תוך כיבוד זכויות הקניין הרוחני והאמנותי של אמנים אחרים ויצירת משהו שהוא שלך (או של הלקוח) באופן ברור יותר."
                }
            ]
        }
        // ניתן להוסיף תרחישים נוספים כאן כדי להעשיר את החוויה
        /*
        ,
        {
             id: 3,
             dilemma: "אתה מפתח משחקים קטנים. לפרויקט חדש אתה צריך קולות לדמויות. אין לך תקציב לשחקנים מקצועיים. איך תשתמש ב-AI?",
             choices: [
                 {
                     text: "השתמש ב-AI להפקת קולות שנשמעים בדיוק כמו שחקני דיבוב מפורסמים מהוליווד שאתה אוהב.",
                     result: "<p><b>הדמיית תוצאה:</b> הדמויות במשחק מדברות בקולות מוכרים של כוכבים. שחקנים רבים מתלהבים מהדמיון, אך כמה שמים לב שזה לא 'אמיתי'. עולות שאלות ברשת לגבי השימוש בדמות קולית של האמנים ללא הסכמה.</p>",
                     feedback: "<b>משוב אתי:</b> 🚫 <b>מסוכן ולא אתי.</b> קולו של אדם הוא חלק מזהותו ומוגדר לעיתים קרובות כקניין רוחני. שימוש ב-AI כדי לחקות קול של שחקן מפורסם ללא הסכמתו הוא פגיעה בזכויותיו, ניצול מסחרי של דמותו הקולית, ועלול להיתפס כהטעיית הציבור. זה מזיק לתעשיית הדיבוב ופוגע בפרנסת שחקנים."
                 },
                 {
                     text: "השתמש ב-AI להפקת קולות מקוריים בסגנון מסוים (למשל, 'קול גברי עמוק ומסתורי', 'קול אישה צעירה ועליזה') מבלי לכוון לחיקוי אדם ספציפי.",
                     result: "<p><b>הדמיית תוצאה:</b> הדמויות במשחק מקבלות קולות ייחודיים המתאימים לאופיין, גם אם הם לא קולות מוכרים. השחקנים נהנים מהאווירה, והפרויקט חסך עלויות דיבוב משמעותיות בצורה לגיטימית.</p>",
                     feedback: "<b>משוב אתי:</b> ✅ <b>שימוש אחראי ונכון.</b> ניצול יכולות ה-AI ליצירת קולות חדשים לגמרי, על בסיס תיאורים כלליים או סגנונות קוליים שאינם מקושרים לאנשים ספציפיים, הוא דרך מצוינת להשתמש בטכנולוגיה. זה מאפשר לך להפיק תוכן קולי איכותי לפרויקט שלך מבלי לפגוע בזכויות או בפרנסה של אמנים אנושיים ספציפיים."
                 }
             ]
        }
        */
    ];

    let currentScenarioIndex = 0;

    const scenarioTextEl = document.getElementById('scenario-text');
    const choicesContainerEl = document.getElementById('choices-container');
    const resultContainerEl = document.getElementById('result-container');
    const resultContentEl = document.getElementById('result-content');
    const feedbackContentEl = document.getElementById('feedback-content');
    const nextScenarioBtn = document.getElementById('next-scenario-btn');
    const endContainerEl = document.getElementById('end-container');
    const restartBtn = document.getElementById('restart-btn');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
    const explanationContainerEl = document.getElementById('explanation-container');
    const scenarioContainerEl = document.getElementById('scenario-container'); // Get scenario screen

    function switchScreen(currentScreen, nextScreen) {
         // Assume currentScreen is active
         currentScreen.classList.remove('active');
         currentScreen.style.transform = 'translateX(-100%)'; // Animate out to the left
         currentScreen.style.opacity = '0';
         currentScreen.style.pointerEvents = 'none';

         // Set up nextScreen for animation
         nextScreen.style.transform = 'translateX(100%)'; // Start from the right
         nextScreen.style.opacity = '0';
         nextScreen.style.position = 'absolute'; // Position over the container

         // A small delay to allow styles to apply before animating
         setTimeout(() => {
              nextScreen.classList.add('active');
              nextScreen.style.transform = 'translateX(0)'; // Animate in
              nextScreen.style.opacity = '1';
              nextScreen.style.pointerEvents = 'auto';
              // After animation, change position back to static if needed
              // (Or keep absolute if container has fixed height/overflow hidden)
              setTimeout(() => {
                  if(nextScreen !== resultContainerEl) { // Keep result absolute for flow after it
                       nextScreen.style.position = 'static';
                   }
              }, 600); // Match transition duration
         }, 50);
    }


    function displayScenario(index) {
        if (index >= scenarios.length) {
            showEndScreen();
            return;
        }

        const scenario = scenarios[index];
        scenarioTextEl.textContent = scenario.dilemma;
        choicesContainerEl.innerHTML = ''; // Clear previous choices

        scenario.choices.forEach(choice => {
            const button = document.createElement('button');
            button.textContent = choice.text;
            button.classList.add('choice-btn');
             // Add animation class when buttons are created
            button.style.opacity = '0';
            button.style.transform = 'translateY(20px)';
            button.style.transition = 'opacity 0.4s ease-out, transform 0.4s ease-out';

            button.addEventListener('click', () => handleChoice(choice));
            choicesContainerEl.appendChild(button);
        });

         // Animate choices in
         setTimeout(() => {
             const choiceButtons = choicesContainerEl.querySelectorAll('.choice-btn');
             choiceButtons.forEach((btn, i) => {
                 setTimeout(() => {
                     btn.style.opacity = '1';
                     btn.style.transform = 'translateY(0)';
                 }, i * 100); // Stagger animation
             });
         }, 100); // Small delay after screen transition

        // Ensure correct screen is active and others are hidden
        if (scenarioContainerEl.classList.contains('active')) {
             // If already on scenario screen, no transition needed
             resultContainerEl.classList.remove('active');
             endContainerEl.classList.remove('active');
              // Reset result screen styles if it was the previous one
             resultContainerEl.style.position = 'absolute';
             resultContainerEl.style.transform = 'translateX(100%)';
             resultContainerEl.style.opacity = '0';
             resultContainerEl.style.pointerEvents = 'none';

         } else {
             // Transition from result/end screen to scenario screen
             if(resultContainerEl.classList.contains('active')) {
                 switchScreen(resultContainerEl, scenarioContainerEl);
             } else if (endContainerEl.classList.contains('active')) {
                  switchScreen(endContainerEl, scenarioContainerEl);
             } else {
                  // Initial load
                 scenarioContainerEl.classList.add('active');
                 scenarioContainerEl.style.opacity = '1';
                 scenarioContainerEl.style.transform = 'translateX(0)';
                 scenarioContainerEl.style.position = 'static'; // Ensure it's in flow
                 scenarioContainerEl.style.pointerEvents = 'auto';
             }
         }
    }

    function handleChoice(choice) {
        resultContentEl.innerHTML = choice.result;
        feedbackContentEl.innerHTML = choice.feedback;

         // Hide scenario elements with slight fade/slide out
         const scenarioElements = [scenarioTextEl, choicesContainerEl];
          scenarioElements.forEach(el => {
             el.style.opacity = '0';
             el.style.transform = 'translateX(-20px)'; // Slide out left
             el.style.transition = 'opacity 0.4s ease-out, transform 0.4s ease-out';
         });


         // Switch to result screen after animation starts
         setTimeout(() => {
             switchScreen(scenarioContainerEl, resultContainerEl);
             // Reset styles for next scenario
             scenarioElements.forEach(el => {
                 el.style.transition = 'none'; // Remove transition for reset
                 el.style.opacity = '1';
                 el.style.transform = 'translateX(0)';
              });

             // Animate result elements in
             const resultElements = [resultContentEl, feedbackContentEl, nextScenarioBtn];
             resultElements.forEach((el, i) => {
                  el.style.opacity = '0';
                  el.style.transform = 'translateY(20px)';
                  el.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
                  setTimeout(() => {
                      el.style.opacity = '1';
                      el.style.transform = 'translateY(0)';
                  }, 100 + i * 150); // Stagger animation
              });


         }, 400); // Allow scenario elements to start fading out

        currentScenarioIndex++;
    }

    function showEndScreen() {
         switchScreen(resultContainerEl, endContainerEl);

         // Animate end screen elements in
         const endElements = [endContainerEl.querySelector('p'), restartBtn];
          endElements.forEach((el, i) => {
              el.style.opacity = '0';
              el.style.transform = 'translateY(20px)';
              el.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
              setTimeout(() => {
                  el.style.opacity = '1';
                  el.style.transform = 'translateY(0)';
              }, 100 + i * 150); // Stagger animation
          });
    }

    function restartApp() {
        currentScenarioIndex = 0;
         // Transition from end screen back to scenario screen
         switchScreen(endContainerEl, scenarioContainerEl);

         // Clear result/feedback content from previous run
         resultContentEl.innerHTML = '';
         feedbackContentEl.innerHTML = '';

         // Start the first scenario after transition
         setTimeout(() => {
              displayScenario(currentScenarioIndex);
         }, 600); // Wait for screen transition
    }

    nextScenarioBtn.addEventListener('click', () => {
         // Animate result elements out before switching screen
         const resultElements = [resultContentEl, feedbackContentEl, nextScenarioBtn];
         resultElements.forEach((el, i) => {
              el.style.opacity = '0';
              el.style.transform = 'translateX(-20px)'; // Slide out left
              el.style.transition = 'opacity 0.4s ease-out, transform 0.4s ease-out';
          });

          // Switch screen after animation starts
          setTimeout(() => {
              displayScenario(currentScenarioIndex);
               // Reset styles for next iteration
              resultElements.forEach(el => {
                 el.style.transition = 'none';
                 el.style.opacity = '1';
                 el.style.transform = 'translateX(0)';
              });
          }, 400); // Allow result elements to start fading out

    });

    restartBtn.addEventListener('click', restartApp);

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationContainerEl.style.display === 'none';
        if (isHidden) {
             explanationContainerEl.style.display = 'block';
             // Optional: smooth reveal animation (requires more complex CSS/JS)
             // For now, just change button text
             toggleExplanationBtn.textContent = 'הסתר הסבר מורחב';
         } else {
             explanationContainerEl.style.display = 'none';
              toggleExplanationBtn.textContent = 'מה מסתתר מאחורי הקלעים? (הסבר מורחב)';
         }
    });

    // Initialize the app
    displayScenario(currentScenarioIndex);

     // Handle initial screen display
     document.addEventListener('DOMContentLoaded', () => {
          scenarioContainerEl.classList.add('active');
          scenarioContainerEl.style.opacity = '1';
          scenarioContainerEl.style.transform = 'translateX(0)';
          scenarioContainerEl.style.position = 'static';
          scenarioContainerEl.style.pointerEvents = 'auto';
           displayScenario(currentScenarioIndex); // Load content after screen is active
     });

</script>
```