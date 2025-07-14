---
title: "מסע בזמן: זיהוי מטבעות עתיקים - יוון או רומא?"
english_slug: ancient-coin-identification-greece-or-rome
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags:
  - מטבעות עתיקים
  - יוון העתיקה
  - רומא העתיקה
  - נומיסמטיקה
  - היסטוריה קלאסית
---
# הצצה לעבר: האם תוכלו לזהות מטבע עתיק?

דמיינו שאתם ארכיאולוגים המחזיקים ממצא מרגש: מטבע עתיק בן אלפיים שנה. הוא שקט, אך טומן בחובו סיפורים רבים. האם הוא נטבע בעיר-מדינה יוונית פורחת, או באימפריה הרומית האדירה? התשובה חבויה בפרטים הקטנים החקוקים עליו. בעזרת האתגר האינטראקטיבי הבא, תוכלו לחדד את יכולות הזיהוי שלכם ולגלות כיצד מבדילים בין מטבע יווני לרומי.

<div id="coin-explorer" class="interactive-container">
    <h2 id="challenge-title">התבוננו היטב במטבע שלפניכם...</h2>
    <p id="challenge-instruction">נסו להבין מאיפה הוא הגיע: יוון העתיקה או רומא העתיקה?</p>

    <div id="coin-display">
        <img id="coin-image" src="" alt="Ancient Coin">
        <div id="image-overlay"></div> <!-- Added for potential effects -->
    </div>

    <div id="choice-buttons">
        <button data-answer="greek" class="choice-button">
            <span class="icon">🏛️</span>
            <span class="text">יווני (יוון והלניסטי)</span>
        </button>
        <button data-answer="roman" class="choice-button">
            <span class="icon">🏟️</span>
            <span class="text">רומי (רפובליקה ואימפריה)</span>
        </button>
    </div>

    <div id="feedback" class="hidden">
        <div class="feedback-icon"></div> <!-- For dynamic icon/visual -->
        <p id="feedback-text"></p>
        <button id="next-coin" class="action-button hidden">למטבע הבא <span class="arrow">➔</span></button>
        <button id="restart-challenge" class="action-button hidden">התחלה מחדש 🔄</button>
    </div>

    <div id="challenge-complete" class="hidden completion-message">
        <h3>משימה הושלמה! 🎉</h3>
        <p>כל הכבוד! זיהיתם את כל המטבעות באתגר הנוכחי.</p>
        <p>כעת, אם תרצו להעמיק את הידע שלכם, תוכלו לעבור לחלק ההסבר המפורט וללמוד על המאפיינים המרכזיים של כל סוג מטבע.</p>
         <button id="restart-challenge-end" class="action-button">התחילו אתגר חדש 🔄</button>
    </div>
</div>

<style>
    /* כללי */
    .interactive-container {
        font-family: 'Arial Hebrew', 'David', sans-serif; /* גופנים ידידותיים לעברית */
        max-width: 600px;
        margin: 30px auto;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        text-align: center;
        background: linear-gradient(to bottom, #f9f9f9, #e9e9e9); /* רקע עדין */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        position: relative; /* למיקום אבסולוטי של אלמנטים פנימיים אם צריך */
    }

    #challenge-title {
        color: #333;
        margin-bottom: 10px;
        font-size: 1.6em;
    }

    #challenge-instruction {
        color: #555;
        margin-bottom: 25px;
        font-size: 1em;
    }


    /* תצוגת מטבע */
    #coin-display {
        margin-bottom: 25px;
        height: 250px; /* הגבלת גובה קבוע לתמונה + אנימציה */
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
    }

    #coin-image {
        max-width: 100%;
        max-height: 250px; /* הגבלת גובה מקסימלי */
        height: auto;
        border: 3px solid #ccc; /* מסגרת למטבע */
        border-radius: 50%; /* ניסיון לדמות מטבע עגול */
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.2); /* צל עדין */
        opacity: 0; /* מתחיל נסתר לאנימציית טעינה */
        transform: scale(0.8); /* מתחיל קטן */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out; /* אנימציית טעינה */
    }

    #coin-image.visible {
         opacity: 1;
         transform: scale(1);
    }

     #image-overlay {
         position: absolute;
         top: 0;
         left: 0;
         right: 0;
         bottom: 0;
         background: rgba(255, 255, 255, 0); /* שקוף כברירת מחדל */
         pointer-events: none; /* לא מפריע לקליקים */
         transition: background 0.3s ease;
         border-radius: 50%; /* Overlay matches coin shape */
     }

    #coin-display.correct #image-overlay {
         background: rgba(144, 238, 144, 0.2); /* ירוק בהיר להצלחה */
    }

     #coin-display.wrong #image-overlay {
         background: rgba(255, 99, 71, 0.2); /* אדום בהיר לכישלון */
     }


    /* כפתורי בחירה */
    #choice-buttons {
        margin-bottom: 20px;
        display: flex;
        justify-content: center;
        gap: 15px; /* רווח בין הכפתורים */
    }

    .choice-button {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 30px; /* כפתורים עגולים יותר */
        background: linear-gradient(to right, #007bff, #0056b3); /* גרדיאנט כחול */
        color: white;
        transition: all 0.3s ease; /* אנימציה למעבר */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        display: flex; /* להצגת אייקון וטקסט בשורה */
        align-items: center;
        gap: 8px; /* רווח בין אייקון לטקסט */
    }

    .choice-button .icon {
        font-size: 1.3em; /* גודל אייקון */
    }

    .choice-button:hover:not(:disabled) {
        background: linear-gradient(to right, #0056b3, #003f7f); /* גרדיאנט כהה יותר בהובר */
        transform: translateY(-2px); /* אפקט קפיצה קלה */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }

     .choice-button:active:not(:disabled) {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
     }

    .choice-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        background: #cccccc; /* אפור כשהם לא פעילים */
    }


    /* אזור פידבק */
    #feedback {
        margin-top: 20px;
        padding: 20px;
        border-radius: 8px;
        min-height: 80px; /* נותן גובה מינימלי לפידבק */
        opacity: 0; /* מתחיל נסתר */
        transform: translateY(20px); /* מתחיל מעט למטה */
        transition: opacity 0.4s ease-out, transform 0.4s ease-out;
        position: relative; /* עבור מיקום אייקון פידבק */
    }

     #feedback:not(.hidden) {
         opacity: 1;
         transform: translateY(0);
     }

     .feedback-icon {
         position: absolute;
         top: -15px; /* מיקום מעל הבלוק */
         left: 50%;
         transform: translateX(-50%);
         width: 30px;
         height: 30px;
         border-radius: 50%;
         display: flex;
         align-items: center;
         justify-content: center;
         font-size: 1.5em;
         color: white;
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
     }

    #feedback.correct {
        background-color: #e9f7ef; /* ירוק בהיר מאוד */
        color: #1a5d3b; /* ירוק כהה יותר */
        border: 1px solid #c3e6cb;
    }
     #feedback.correct .feedback-icon {
         background-color: #28a745; /* ירוק */
         content: '✔️'; /* אייקון וי */
     }
      #feedback.correct .feedback-icon::before {
          content: '✔️';
      }


    #feedback.wrong {
        background-color: #fdedee; /* אדום בהיר מאוד */
        color: #721c24; /* אדום כהה יותר */
        border: 1px solid #f5c6cb;
    }
     #feedback.wrong .feedback-icon {
         background-color: #dc3545; /* אדום */
         content: '❌'; /* אייקון X */
     }
      #feedback.wrong .feedback-icon::before {
          content: '❌';
      }


    #feedback-text {
        margin-bottom: 15px;
        line-height: 1.6;
        font-size: 1em;
    }

    /* כפתורי פעולה (הבא, התחל מחדש) */
    .action-button {
        padding: 10px 20px;
        margin: 0 8px; /* רווח בין כפתורי פעולה */
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* כפתורים עגולים יותר */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
         display: inline-flex; /* להצגת אייקון וטקסט בשורה */
         align-items: center;
         gap: 5px;
    }

    #next-coin {
        background-color: #28a745; /* ירוק */
    }

    #next-coin:hover:not(:disabled) {
        background-color: #218838;
        transform: translateY(-1px);
    }

     #restart-challenge, #restart-challenge-end {
         background-color: #6c757d; /* אפור */
    }

    #restart-challenge:hover:not(:disabled), #restart-challenge-end:hover:not(:disabled) {
        background-color: #5a6268;
        transform: translateY(-1px);
    }

    .action-button:active:not(:disabled) {
         transform: translateY(0);
     }


    /* הודעת סיום אתגר */
    .completion-message {
        margin-top: 25px;
        padding: 25px;
        border: 2px solid #28a745; /* מסגרת ירוקה */
        background-color: #d4edda; /* רקע ירוק בהיר */
        border-radius: 8px;
        color: #155724; /* טקסט ירוק כהה */
        opacity: 0; /* מתחיל נסתר */
        transform: scale(0.9); /* מתחיל קטן */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

     .completion-message:not(.hidden) {
         opacity: 1;
         transform: scale(1);
     }

    .completion-message h3 {
        color: #155724;
        margin-top: 0;
        font-size: 1.5em;
    }

    .completion-message p {
        margin-bottom: 15px;
        line-height: 1.6;
    }


    /* אלמנטים מוסתרים */
    .hidden {
        display: none;
    }


    /* כפתור הסבר */
    #explanation-button {
        display: block;
        margin: 40px auto 20px;
        padding: 15px 30px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 30px;
        background: linear-gradient(to right, #ffc107, #e0a800); /* גרדיאנט צהוב */
        color: #333; /* טקסט כהה יותר */
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    #explanation-button:hover {
        background: linear-gradient(to right, #e0a800, #c79100); /* גרדיאנט כהה יותר בהובר */
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
     #explanation-button:active {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
     }


    /* אזור הסבר מפורט */
    #detailed-explanation {
        max-width: 800px;
        margin: 20px auto 40px auto;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #f9f9f9;
        line-height: 1.7; /* רווח שורה נוח לקריאה */
        color: #333;
        opacity: 0; /* מתחיל נסתר */
        transform: translateY(30px); /* מתחיל מעט למטה */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

     #detailed-explanation:not(.hidden) {
         opacity: 1;
         transform: translateY(0);
     }

    #detailed-explanation h2, #detailed-explanation h3, #detailed-explanation h4 {
        color: #333;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    #detailed-explanation h2 { font-size: 1.8em; }
    #detailed-explanation h3 { font-size: 1.4em; }
    #detailed-explanation h4 { font-size: 1.2em; }


    #detailed-explanation p, #detailed-explanation li {
        margin-bottom: 15px;
        color: #555;
    }

    #detailed-explanation ul {
        list-style-type: disc;
        padding-left: 25px;
    }

     #detailed-explanation li {
         margin-bottom: 10px; /* רווח קטן יותר בין פריטי רשימה */
     }

</style>

<button id="explanation-button">למד עוד: הצג הסבר מפורט</button>

<div id="detailed-explanation" class="hidden">
    <h2>צוללים לעומק: סודותיהם של מטבעות עתיקים</h2>

    <h3>מבוא: מטבעות - מפתחות לעבר</h3>
    <p>מטבעות עתיקים הם הרבה יותר מאמצעי תשלום ששימש בימים עברו. הם מסמכים היסטוריים זעירים, עדות אילמת לתרבויות, שליטים, כלכלה ואמנות של תקופות עתיקות. ניתוח מדוקדק שלהם, תחום המכונה נומיסמטיקה, מאפשר לנו לשחזר פאזלים היסטוריים וארכיאולוגיים ולגלות סיפורים מפתיעים.</p>

    <h3>הבדלים מהותיים בין מטבעות יוון ורומא</h3>
    <p>על אף קשרים והשפעות הדדיות לאורך ההיסטוריה, למטבעות שהוטבעו בעולם היווני (ערים ביוון, אסיה הקטנה, דרום איטליה, ממלכות הלניסטיות כמו מצרים התלמיית או הממלכה הסלווקית) ובעולם הרומי (הרפובליקה והאימפריה הרומית) היו מאפיינים ברורים שאפשרו את זיהוי מקורם:</p>

    <h4>1. סגנון אמנותי ואיכות חקיקה</h4>
    <ul>
        <li><strong>מטבעות יווניים:</strong> בשיאם (בעיקר בתקופה הקלאסית וההלניסטית), מטבעות יווניים הגיעו לאיכות אמנותית עוצרת נשימה. התבליטים עליהם מפוסלים בעדינות רבה, מדויקים ומלאי חיים. הם נוטים להציג אידיאליזציה של דמויות - אלים, גיבורים או שליטים מוצגים בשיא יופיים וכוחם, לעיתים קרובות בפרופיל מלכותי ומלא הדר.</li>
        <li><strong>מטבעות רומיים:</strong> הסגנון הרומי, בעיקר בתקופת האימפריה, התמקד יותר בריאליזם. דיוקנאות הקיסרים היו נאמנים למציאות, לעיתים עד כדי הדגשת מאפיינים אישיים (אף גדול, סנטר כפול). בעוד שהטכניקה הייתה יעילה ואיכותית מבחינת ייצור המוני, הדגש האמנותי היה פחות על יופי אידיאליסטי ויותר על הפצת תדמיתו של הקיסר וסמלי השלטון.</li>
    </ul>

    <h4>2. תיאורי דמויות וסמלים מרכזיים</h4>
     <ul>
        <li><strong>מטבעות יווניים:</strong> הצד הראשי (Obverse) לרוב מציג ראש של אל או אלה מהפנתיאון היווני (אתנה, זאוס, אפולו, ארטמיס), או גיבור מיתולוגי (הרקולס). הצד האחורי (Reverse) מציג סמלים קשורים לאל או לעיר, חיות קדושות, או סצנות מיתולוגיות. בתקופה ההלניסטית נוספו גם דיוקנאות ריאליסטיים יותר של מלכים ושליטים.</li>
        <li><strong>מטבעות רומיים:</strong> בתקופת הרפובליקה, הופיעו אלים רומיים (יופיטר, מרס, ונוס), סמלים היסטוריים (כמו הסביפה - Fasces) או תיאורים הקשורים למשפחות של המטביעים. בתקופת האימפריה, הצד הראשי הוקדש כמעט תמיד לדיוקן הקיסר המכהן או מי מבני משפחתו הקרובים (ככלי תעמולתי). הצד האחורי הציג מגוון רחב: אלים רומיים, סמלים צבאיים (נשר לגיונרי), אלגוריות מופשטות (ניצחון - ויקטוריה, צדק - יוסטיציה), מבנים מונומנטליים או סצנות המתארות אירועים היסטוריים (ניצחונות צבאיים, חלוקת מזון לאוכלוסייה).</li>
    </ul>

    <h4>3. שפה וכיתובים</h4>
    <ul>
        <li><strong>מטבעות יווניים:</strong> הכיתובים הם כמעט תמיד ביוונית עתיקה. הם יכללו לרוב את שם העיר שהטביעה את המטבע (לעיתים בראשי תיבות), שמות פקידים מקומיים, או שמו ותאריו של המלך בתקופה ההלניסטית.</li>
        <li><strong>מטבעות רומיים:</strong> הכיתובים הם כמעט תמיד בלטינית. בתקופת האימפריה, הכיתוב המקיף את דיוקן הקיסר (ה"אגדה" - legend) הוא מאפיין מרכזי וכולל את שמו המלא, תאריו ותאריו הצבאיים והפוליטיים (IMP, CAES, AUG, P M, TR P, COS, P P, S C). כיתוב זה הוא כלי חשוב לתיארוך וזיהוי הקיסר.</li>
    </ul>

    <h4>4. צורות וגדלים</h4>
     <ul>
        <li><strong>מטבעות יווניים:</strong> קיימת שונות גדולה בגדלים ובמשקלים, בהתאם למערכות המטבע השונות של מאות ערי-מדינה וממלכות. צורת המטבע יכולה להיות פחות אחידה ועגולה לחלוטין לעומת מטבעות רומיים מאוחרים. הטטרדרכמה הכסופה, במיוחד זו האתונאית, היא דוגמה למטבע יווני נפוץ ומוכר.</li>
        <li><strong>מטבעות רומיים:</strong> למערכת המטבע הרומית, במיוחד בתקופת האימפריה, הייתה סטנדרטיזציה גבוהה יותר. גדלים ומשקלים היו קבועים יחסית עבור יחידות שונות (אוראוס מזהב, דנאריוס מכסף, ססטרציוס ואס מברונזה/נחושת). צורת המטבע לרוב עגולה ואחידה יותר בזכות שיטות ייצור מרוכזות.</li>
    </ul>

    <h3>נקודות למחשבה: חפיפה והשפעות</h3>
    <p>חשוב לזכור שהגבולות אינם תמיד חדים. במאגנה גרקיה (דרום איטליה הסיציליאנית), ערים יווניות הטביעו מטבעות עם השפעות רומיות. במזרח האימפריה הרומית, מטבעות הוטבעו לעיתים עם כיתובים ביוונית (מטבעות פרובינציאליים). עם זאת, המאפיינים המרכזיים שתוארו לעיל מהווים מדריך אמין ויעיל לזיהוי ראשוני.</p>
    <p>כעת, כשאתם חמושים בידע זה, תוכלו לחזור לאתגר (או להתחיל אותו שוב) ולשים לב לפרטים הקטנים המגלים את סיפורו של כל מטבע!</p>
</div>

<script>
    // הגדרת המטבעות - שימו לב שהתמונות הן רק placeholders, במערכת אמיתית היו כאן תמונות של מטבעות אמיתיים
    const coins = [
        {
            img: "https://cdn.britannica.com/58/161858-050-B609D77D/Silver-tetradrachm-coin-head-Athena-owl-olive.jpg", // דוגמה למטבע אתונאי (תמונה אמיתית אם אפשר)
            answer: "greek",
            feedback: "נכון מאוד! זהו מטבע יווני, ספציפית טטרדרכמה אתונאית מפורסמת. שימו לב לסגנון האמנותי האידיאליסטי של אתנה בצד אחד, והינשוף (הסמל של אתנה ואתונה) והכיתוב היווני בצד השני. קלאסי לעולם היווני!",
            alt: "מטבע כסף עתיק עם ראש אישה (אתנה) וינשוף"
        },
        {
            img: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Denarius_Augustus_RIC_207.jpg/1024px-Denarius_Augustus_RIC_207.jpg", // דוגמה למטבע רומי קיסרי (אוגוסטוס)
            answer: "roman",
            feedback: "בינגו! זהו מטבע רומי מתקופת האימפריה. דיוקן הקיסר אוגוסטוס הריאליסטי והכיתוב בלטינית סביבו הם מאפיינים מובהקים של מטבעות רומיים שנועדו להפיץ את תדמית השליט ברחבי האימפריה.",
            alt: "מטבע כסף עתיק עם דיוקן גבר בפרופיל (קיסר רומי)"
        },
        {
            img: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Tetradrachm_of_Alexander_the_Great_Walcher_Collection.jpg/800px-Tetradrachm_of_Alexander_the_Great_Walcher_Collection.jpg", // דוגמה למטבע הלניסטי (אלכסנדר הגדול)
            answer: "greek",
            feedback: "מעולה! זהו מטבע יווני מהתקופה ההלניסטית, נושא את דיוקנו של אלכסנדר הגדול בצורת הירקולס (עם כיסוי ראש של אריה) בצד אחד, וזאוס יושב על כיסא עם נשר בצד השני, לצד כיתוב יווני. האמנות והסמלים מצביעים על מוצא יווני/הלניסטי.",
             alt: "מטבע כסף עתיק עם ראש עטוף בכיסוי ראש של אריה"
        },
        {
            img: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Roman_sestertius_Titus_reverse.jpg/800px-Roman_sestertius_Titus_reverse.jpg", // דוגמה למטבע רומי (ססטרציוס עם סצנה מהרוורס)
            answer: "roman",
            feedback: "נכון! זהו ססטרציוס רומי מתקופת הקיסר טיטוס. גודלו, סגנון החקיקה (ריאליסטי אך מונומנטלי) ותיאור סצנה (במקרה זה - שער טיטוס בירושלים) לצד הכיתוב הלטיני (S P Q R OPTIMO PRINCIPI) אופייניים מאוד למטבעות רומיים אימפריאליים גדולים.",
             alt: "מטבע ברונזה גדול עתיק עם תיאור מבנה או סצנה"
        },
         {
            img: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Coin_Ancient_Greece_Rhodes_4th_cent_BC_Didrachm.jpg/800px-Coin_Ancient_Greece_Rhodes_4th_cent_BC_Didrachm.jpg", // דוגמה למטבע יווני מרודוס (ראש הליוס)
            answer: "greek",
            feedback: "בדיוק! זהו מטבע יווני מהאי רודוס. ראש אל השמש הליוס עם קרניים הוא סמל מובהק של רודוס (הקולוסוס של רודוס היה פסל ענק של הליוס), והסגנון האמנותי עדין ומפורט עם כיתוב יווני. אין ספק שמדובר במטבע יווני.",
             alt: "מטבע כסף עתיק עם ראש גבר מקורן"
        },
         {
            img: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Denarius_Julius_Caesar_elephant.jpg/800px-Denarius_Julius_Caesar_elephant.jpg", // דוגמה למטבע רומי רפובליקני (יוליוס קיסר והפיל)
            answer: "roman",
            feedback: "נכון! זהו דנאריוס רומי רפובליקני, הוטבע על ידי יוליוס קיסר. למרות שהצד הראשי מציג סמל (כלי פולחן), הצד האחורי עם הפיל הדורס נחש, וכמובן הכיתוב הלטיני CAESAR, מאפיינים את המטבעות הרומיים של סוף הרפובליקה.",
             alt: "מטבע כסף עתיק עם תיאור פיל הדורס חיה אחרת"
        }
    ];

    let currentCoinIndex = 0;
    let shuffledCoins = [];
    let buttonsEnabled = true; // דגל לשליטה על מצב הכפתורים

    const coinImage = document.getElementById('coin-image');
    const coinDisplayDiv = document.getElementById('coin-display'); // קיבלנו הפניה לדיב של התצוגה
    const choiceButtonsDiv = document.getElementById('choice-buttons');
    const feedbackDiv = document.getElementById('feedback');
    const feedbackText = document.getElementById('feedback-text');
    const nextCoinButton = document.getElementById('next-coin');
    const restartChallengeButton = document.getElementById('restart-challenge');
    const restartChallengeEndButton = document.getElementById('restart-challenge-end');
    const challengeCompleteDiv = document.getElementById('challenge-complete');
    const explanationButton = document.getElementById('explanation-button');
    const detailedExplanationDiv = document.getElementById('detailed-explanation');
    const feedbackIcon = feedbackDiv.querySelector('.feedback-icon'); // הפניה לאייקון הפידבק

    // פונקציה לערבוב מערך
    function shuffleArray(array) {
        const shuffled = [...array]; // יוצר עותק כדי לא לשנות את המערך המקורי
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]; // החלפה
        }
        return shuffled;
    }

    // פונקציה לטעינת מטבע חדש
    function loadCoin() {
        if (currentCoinIndex < shuffledCoins.length) {
            const coin = shuffledCoins[currentCoinIndex];

            // אפס מצבים קודמים והסתר אלמנטים
            feedbackDiv.classList.add('hidden');
            feedbackDiv.classList.remove('correct', 'wrong');
            coinDisplayDiv.classList.remove('correct', 'wrong'); // הסרת קלאסים לתצוגה
            feedbackText.textContent = '';
            nextCoinButton.classList.add('hidden');
            restartChallengeButton.classList.add('hidden'); // הסתר כפתור התחלה מחדש באתגר
            challengeCompleteDiv.classList.add('hidden');
            coinImage.classList.remove('visible'); // התחל אנימציית היעלמות לתמונה הקודמת

            // טען תמונה חדשה והפעל אנימציית טעינה
            coinImage.src = coin.img;
            coinImage.alt = coin.alt;

            // המתן קצת שהתמונה תיטען ותתבצע אנימציית יציאה, ואז הכנס את החדשה
            setTimeout(() => {
                 coinImage.classList.add('visible'); // הפעל אנימציית כניסה
                 choiceButtonsDiv.classList.remove('hidden');
                 enableButtons(); // הפעל מחדש את הכפתורים לבחירה
            }, 400); // זמן קצר, תואם בערך לאנימציית היציאה


        } else {
            endChallenge();
        }
    }

    // פונקציה לבדיקת התשובה
    function checkAnswer(selectedAnswer) {
        if (!buttonsEnabled) return; // אם הכפתורים לא פעילים, אל תעשה כלום
        disableButtons(); // נטרל כפתורים מיד לאחר הבחירה

        const coin = shuffledCoins[currentCoinIndex];
        const isCorrect = selectedAnswer === coin.answer;

        // הכנת הפידבק
        let feedbackString = coin.feedback;
        if (!isCorrect) {
             // אם התשובה שגויה, הוסף את התשובה הנכונה להסבר הקיים
             feedbackString = `שגוי. זהו למעשה מטבע ${coin.answer === 'greek' ? 'יווני' : 'רומי'}. ${coin.feedback}`;
        }

        feedbackText.textContent = feedbackString;

        // הצגת הפידבק והפעלת אנימציות
        feedbackDiv.classList.remove('hidden');
        feedbackDiv.classList.toggle('correct', isCorrect);
        feedbackDiv.classList.toggle('wrong', !isCorrect);
        coinDisplayDiv.classList.toggle('correct', isCorrect); // הוסף קלאס לדיב התצוגה לאפקט overlay
        coinDisplayDiv.classList.toggle('wrong', !isCorrect); // הוסף קלאס לדיב התצוגה לאפקט overlay

        // עדכון כפתורי הפידבק
        if (currentCoinIndex < shuffledCoins.length - 1) {
            nextCoinButton.classList.remove('hidden');
            restartChallengeButton.classList.add('hidden'); // הסתר כפתור התחלה מחדש אחרי פידבק אם יש מטבעות נוספים
        } else {
            nextCoinButton.classList.add('hidden');
            restartChallengeButton.classList.remove('hidden'); // הצג התחלה מחדש במטבע האחרון לפני הסיום
        }
        // Show restart button also if incorrect answer was given, regardless of index?
        // Let's stick to the current logic: next if available, restart on last item or on end screen.
    }

    // פונקציה לסיום האתגר
    function endChallenge() {
        challengeCompleteDiv.classList.remove('hidden');
        coinImage.classList.remove('visible'); // הסתר תמונה בסיום
        choiceButtonsDiv.classList.add('hidden');
        feedbackDiv.classList.add('hidden');
        restartChallengeButton.classList.add('hidden'); // הסתר כפתור זה אם הופיע קודם
         coinDisplayDiv.classList.remove('correct', 'wrong'); // ודא שאין אוברליי בסיום
    }

    // פונקציה להפעלת כפתורי הבחירה
    function enableButtons() {
        buttonsEnabled = true;
        choiceButtonsDiv.querySelectorAll('button').forEach(button => {
            button.disabled = false;
        });
    }

    // פונקציה לנטרול כפתורי הבחירה
    function disableButtons() {
         buttonsEnabled = false;
         choiceButtonsDiv.querySelectorAll('button').forEach(button => {
             button.disabled = true;
         });
    }


    // פונקציה לאתחול האתגר
    function restartChallenge() {
        currentCoinIndex = 0;
        shuffledCoins = shuffleArray([...coins]); // ערבב מחדש את המטבעות
        coinImage.classList.remove('hidden'); // ודא שהתמונה גלויה
        challengeCompleteDiv.classList.add('hidden'); // הסתר הודעת סיום
        loadCoin(); // טען את המטבע הראשון
    }

    // מאזינים לאירועים
    choiceButtonsDiv.addEventListener('click', (event) => {
        if (event.target.closest('button') && buttonsEnabled) { // ודא שהקליק היה על כפתור ושהכפתורים פעילים
            const button = event.target.closest('button');
            checkAnswer(button.dataset.answer);
        }
    });

    nextCoinButton.addEventListener('click', () => {
        currentCoinIndex++;
        loadCoin();
    });

    restartChallengeButton.addEventListener('click', restartChallenge);
    restartChallengeEndButton.addEventListener('click', restartChallenge);


    explanationButton.addEventListener('click', () => {
        const isHidden = detailedExplanationDiv.classList.contains('hidden');
        detailedExplanationDiv.classList.toggle('hidden');
        if (isHidden) {
            explanationButton.textContent = 'הסתר הסבר מפורט';
             // גלול בעדינות לאזור ההסבר
             detailedExplanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            explanationButton.textContent = 'למד עוד: הצג הסבר מפורט';
        }
    });

    // הפעלת האתגר בפתיחת הדף
    restartChallenge();
</script>