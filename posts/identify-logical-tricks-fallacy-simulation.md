---
title: "זיהוי כשלים לוגיים: משחק סימולציה אינטראקטיבי"
english_slug: identify-logical-tricks-fallacy-simulation
category: "פילוסופיה"
tags: [כשל לוגי, חשיבה ביקורתית, ויכוח, רטוריקה, הסקה, פתרון בעיות]
---
# זיהוי כשלים לוגיים: משחק סימולציה אינטראקטיבי
האם אי פעם נכחתם בדיון או ויכוח והרגשתם שמשהו פשוט לא מסתדר בטיעון של הצד השני, אבל לא ידעתם לזהות בדיוק מה? טיעונים רבים עשויים להישמע הגיוניים ומשכנעים במבט ראשון, אך הם מסתירים בתוכם כשלים לוגיים – פגמים בהסקה שמטרתם לבלבל או להטעות.

בואו נצא למסע אינטראקטיבי שיחדד את יכולות החשיבה הביקורתית שלכם! השתמשו בסימולציה דמויית משחק זו כדי לתרגל זיהוי של כשלים לוגיים נפוצים בסצנריוז יומיומיים. ככל שתתרגלו יותר, כך יהיה לכם קל יותר לזהות אותם בזמן אמת ולהימנע מליפול למלכודות רטוריות. מוכנים לאתגר?

<div id="quiz-app">
    <div class="quiz-header">
        <h2 class="question-title">זיהוי כשל לוגי: האתגר</h2>
        <div class="progress">
            שאלה <span id="current-question-number">1</span> מתוך <span id="total-questions">5</span>
        </div>
    </div>
    <div class="question-container">
        <p class="scenario-text"></p>
        <div class="options-container">
            <button class="option-button" data-index="0">אין כשל לוגי בולט</button>
            <button class="option-button" data-index="1">כשל איש קש</button>
            <button class="option-button" data-index="2">כשל מדרון חלקלק</button>
        </div>
        <button class="submit-button" disabled>בדוק את התשובה שלי</button>
        <div class="feedback-area">
            <div class="feedback-icon"></div>
            <div class="feedback-text"></div>
        </div>
        <button class="next-button" style="display: none;">לשאלה הבאה <i class="arrow"></i></button>
    </div>
    <div class="result-container" style="display: none;">
        <h2><span class="completion-message">כל הכבוד! סיימתם את הסימולציה!</span></h2>
        <p class="score"></p>
         <p class="score-analysis"></p>
         <button class="restart-button">לשחק שוב?</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-dark: #0056b3;
        --secondary-color: #6c757d;
        --secondary-dark: #545b62;
        --success-color: #28a745;
        --success-bg: #d4edda;
        --success-border: #c3e6cb;
        --success-text: #155724;
        --danger-color: #dc3545;
        --danger-bg: #f8d7da;
        --danger-border: #f5c6cb;
        --danger-text: #721c24;
        --light-bg: #f8f9fa;
        --white-bg: #fff;
        --border-color: #dee2e6;
        --text-color: #343a40;
        --shadow-color: rgba(0, 0, 0, 0.1);
    }

    #quiz-app {
        font-family: 'Arial', sans-serif;
        max-width: 650px;
        margin: 30px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--light-bg);
        direction: rtl;
        text-align: right;
        box-shadow: 0 5px 15px var(--shadow-color);
        position: relative;
        overflow: hidden; /* Hide overflow during transitions */
    }

    .quiz-header {
        text-align: center;
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 2px solid var(--border-color);
    }

    .question-title {
        color: var(--primary-dark);
        margin: 0 0 10px 0;
        font-size: 1.8em;
    }

    .progress {
        font-size: 1em;
        color: var(--secondary-dark);
    }

    .question-container {
        margin-bottom: 20px;
        opacity: 1;
        transition: opacity 0.5s ease-in-out;
    }
     .question-container.fade-out {
         opacity: 0;
     }


    .scenario-text {
        font-size: 1.2em;
        margin-bottom: 20px;
        padding: 20px;
        background-color: var(--white-bg);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        line-height: 1.7;
        color: var(--text-color);
        box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.05);
    }

    .options-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 20px;
    }

    .option-button {
        padding: 12px 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--white-bg);
        cursor: pointer;
        font-size: 1.1em;
        text-align: right;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
        color: var(--text-color);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .option-button:hover:not(:disabled) {
        background-color: #e9ecef;
        border-color: #ced4da;
        transform: translateY(-2px);
    }

    .option-button.selected {
        background-color: var(--primary-color);
        border-color: var(--primary-dark);
        color: var(--white-bg);
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
    }

     .option-button.correct {
         background-color: var(--success-bg);
         border-color: var(--success-border);
         color: var(--success-text);
         font-weight: bold;
     }

     .option-button.incorrect {
         background-color: var(--danger-bg);
         border-color: var(--danger-border);
         color: var(--danger-text);
         font-weight: bold;
     }


    .option-button:disabled {
        opacity: 0.8;
        cursor: not-allowed;
        box-shadow: none;
    }

    .submit-button, .next-button, .restart-button, #toggle-explanation {
        display: inline-block;
        padding: 12px 25px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }
     #toggle-explanation {
         display: block;
         margin: 30px auto;
         background-color: var(--secondary-color);
         box-shadow: 0 4px 8px rgba(108, 117, 125, 0.3);
     }

    .submit-button:hover:not(:disabled), .next-button:hover:not(:disabled), .restart-button:hover, #toggle-explanation:hover {
        background-color: var(--primary-dark);
        transform: translateY(-2px);
    }
     #toggle-explanation:hover {
         background-color: var(--secondary-dark);
     }


    .submit-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
        transform: none;
    }

    .feedback-area {
        margin-top: 20px;
        padding: 15px;
        border-radius: 8px;
        min-height: 2em; /* Reserve space */
        display: flex;
        align-items: center;
        gap: 15px;
        opacity: 0; /* Start hidden */
        transition: opacity 0.5s ease-in-out;
    }

     .feedback-area.visible {
         opacity: 1;
     }

    .feedback-icon {
        font-size: 2em;
        line-height: 1;
    }

    .feedback-text {
        flex-grow: 1;
        line-height: 1.6;
    }


    .feedback-correct {
        background-color: var(--success-bg);
        color: var(--success-text);
        border: 1px solid var(--success-border);
    }
    .feedback-correct .feedback-icon::before {
        content: "✅"; /* Checkmark emoji */
    }


    .feedback-incorrect {
        background-color: var(--danger-bg);
        color: var(--danger-text);
        border: 1px solid var(--danger-border);
    }
     .feedback-incorrect .feedback-icon::before {
        content: "❌"; /* X emoji */
     }

    /* Animation for incorrect answer */
     @keyframes shake {
         0%, 100% { transform: translateX(0); }
         10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
         20%, 40%, 60%, 80% { transform: translateX(5px); }
     }

     .shake {
         animation: shake 0.5s ease-in-out;
     }


    .next-button .arrow {
        display: inline-block;
        margin-right: 8px; /* Space before text */
        width: 0;
        height: 0;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        border-right: 8px solid white; /* Arrow pointing left (in RTL) */
         transform: translateY(-2px); /* Vertically align with text */
    }


    .result-container {
        text-align: center;
        padding: 30px 20px;
        background-color: var(--white-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        box-shadow: 0 5px 15px var(--shadow-color);
        opacity: 0; /* Start hidden */
        transition: opacity 0.5s ease-in-out;
    }
     .result-container.visible {
         opacity: 1;
     }

    .result-container h2 {
        color: var(--success-color);
        margin-bottom: 15px;
        font-size: 2em;
    }

    .score {
        font-size: 1.5em;
        font-weight: bold;
        color: var(--primary-dark);
        margin-bottom: 10px;
    }
     .score-analysis {
         font-size: 1.1em;
         color: var(--text-color);
         margin-bottom: 20px;
     }

    .restart-button {
        background-color: var(--secondary-color);
         box-shadow: 0 4px 8px rgba(108, 117, 125, 0.3);
    }
    .restart-button:hover {
        background-color: var(--secondary-dark);
    }


    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--white-bg);
        direction: rtl;
        text-align: right;
        box-shadow: 0 5px 15px var(--shadow-color);
        line-height: 1.7;
    }

    #explanation h2, #explanation h3 {
        color: var(--primary-dark);
        margin-top: 25px;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px dashed var(--border-color);
    }
     #explanation h2 {
         font-size: 1.6em;
     }
      #explanation h3 {
         font-size: 1.3em;
          color: var(--text-color);
     }
     #explanation p {
         margin-bottom: 12px;
         color: var(--text-color);
     }
     #explanation ul {
         margin-bottom: 12px;
         padding-right: 20px;
     }
     #explanation li {
         margin-bottom: 8px;
     }
</style>

<button id="toggle-explanation">הצג הסבר על כשלים לוגיים</button>

<div id="explanation" style="display: none;">
    <h2>מהו, בעצם, כשל לוגי?</h2>
    <p>כשל לוגי הוא פגם מבני בטיעון שמפריע לו להיות תקף מבחינה הגיונית, ללא קשר לאם המסקנה הסופית נכונה במקרה או לא. זה לא בהכרח אומר שהמסקנה שגויה, אלא שהדרך שבה הגיעו אליה מההנחות אינה הגיונית או תקפה. זיהוי כשלים הוא כלי קריטי בארגז הכלים של חשיבה ביקורתית.</p>

    <h2>למה כדאי לנו לזהות כשלים לוגיים?</h2>
    <p>מעבר לחדוּת מחשבה, זיהוי כשלים מאפשר לנו להגן על עצמנו מפני ניסיונות שכנוע המבוססים על רטוריקה חלשה או מניפולטיבית. זה עוזר לנו להבחין בין טיעונים מוצקים ומבוססים לבין טיעונים רעועים, ולבנות טיעונים משלנו בצורה קוהרנטית, משכנעת ותקפה יותר. זהו אבן יסוד לדיונים פוריים וקבלת החלטות מושכלות.</p>

    <h3>כשל נפוץ 1: איש קש (Straw Man Fallacy)</h3>
    <p><strong>הסבר:</strong> כשל איש קש מתרחש כשמציג הטיעון מסלף, מגזים או מייצג באופן שגוי את טיעונו של יריבו (בונה 'איש קש' חלש וקל להפלה), ואז תוקף את הגרסה המעוותת במקום להתמודד עם הטיעון המקורי כפי שהוצג. קל יותר להפיל בובת קש מנייר מאשר להתמודד עם טיעון אמיתי ומורכב.</p>
    <p><strong>דוגמה קלאסית:</strong></p>
    <ul>
        <li>אליס: "אני בעד הגדלת התקציב לטיפול בפסולת כדי לשפר את איכות הסביבה בעיר."</li>
        <li>בוב: "אז אליס רוצה להוציא את כל הכסף של העירייה על מיחזור ופחים חדשים, בזמן שאנשים רעבים ברחוב? זה אבסורד וחסר אחריות!"</li>
    </ul>
    <p>בוב מסלף את עמדתה של אליס (היא דיברה על הגדלת התקציב לפסולת, לא על הוצאת *כל* הכסף והזנחת נושאים אחרים) ותוקף את הסילוף הקיצוני שיצר ('איש הקש').</p>

    <h3>כשל נפוץ 2: מדרון חלקלק (Slippery Slope Fallacy)</h3>
    <p><strong>הסבר:</strong> כשל מדרון חלקלק גורס שפעולה התחלתית, קטנה יחסית, תוביל בהכרח לסדרה בלתי נמנעת של אירועים או תוצאות נוספות, לרוב שליליות וקיצוניות, ללא הצדקה לוגית מספקת או עדויות לקשר הסיבתי החזק בין השלבים השונים. כאילו הצעד הראשון שם אותנו על מדרון תלול שסופו הידרדרות בלתי נמנעת לתהום.</p>
    <p><strong>דוגמה נפוצה:</strong></p>
    <ul>
        <li>"אם נאפשר לילדים להשתמש במחשב שעה ביום, מחר הם כבר יהיו מכורים למסכים, יזנחו את הלימודים לגמרי, לא יהיו להם חברים, והעתיד שלהם יהרס לחלוטין. לכן אסור להתחיל בכלל."</li>
    </ul>
    <p>הטיעון מציג רצף אירועים דרמטי ופסימי (התמכרות, הזנחת לימודים, בידוד חברתי, הרס העתיד) שאינו נובע בהכרח, באופן לוגי או מציאותי, מצעד ראשון קטן יחסית (שעת מחשב מבוקרת ביום).</p>

    <h3>כשלים לוגיים נפוצים נוספים שכדאי להכיר</h3>
    <p>עולם הכשלים הלוגיים רחב ומגוון. הנה עוד כמה דוגמאות בולטות:</p>
    <ul>
        <li><strong>אד הומינם (Ad Hominem):</strong> תקיפה אישית של האדם שמציג את הטיעון (הכוונה, האופי, הנסיבות שלו) במקום להתייחס לגופו של הטיעון עצמו.</li>
        <li><strong>פנייה לסמכות כוזבת (Appeal to False Authority):</strong> שימוש באדם שאינו מומחה רלוונטי בתחום הנדון כדי לתמוך בטיעון.</li>
        <li><strong>דיכוטומיה כוזבת (False Dichotomy/Dilemma):</strong> הצגת שתי אפשרויות בלבד כבחירה היחידה האפשרית, בעוד שלמעשה קיימות אפשרויות נוספות.</li>
        <li><strong>פנייה לרגש (Appeal to Emotion):</strong> ניסיון לשכנע באמצעות עוררות רגשות (כמו פחד, רחמים, שמחה) במקום הצגת ראיות או היגיון.</li>
    </ul>

    <h3>טיפים לזיהוי כשלים לוגיים בשיח היומיום</h3>
    <p>כדי לזהות כשלים, היו ערניים לאופן שבו טיעונים בנויים: האם יש קפיצות לוגיות לא מוסברות? האם מישהו מייצג את דברי הצד השני בצורה שונה מזו שהוצגו? האם המסקנה באמת נובעת מההנחות שהוצגו? היזהרו במיוחד מטענות מוחלטות ("תמיד", "אף פעם"), מקשרי סיבה-תוצאה שנשמעים מופרכים, וממעברים מהירים מדי לתחזיות קיצוניות או התקפות אישיות במקום התמודדות עניינית עם הטענות.</p>

    <h3>חשיבה ביקורתית: הכלי החשוב ביותר</h3>
    <p>זיהוי כשלים לוגיים הוא מרכיב חיוני בחשיבה ביקורתית. ככל שתרגלו לזהות אותם, כך תשתפרו ביכולתכם לנתח מידע, לקבל החלטות מושכלות, ולתקשר בצורה ברורה ויעילה יותר, הן בחייכם האישיים והן בעיסוק בנושאים ציבוריים.</p>
</div>

<script>
    const quizData = [
        {
            scenario: "שר הבריאות הציע תוכנית להגבלת מכירת משקאות ממותקים בחנויות מסוימות כדי להילחם בהשמנה בקרב בני נוער. מתנגד לתוכנית טען בלהט: 'אז אתם רוצים להגיד לאנשים מה לאכול ולשתות בכל רגע בחיים שלהם? אתם פשוט רוצים לשלוט בנו ולהפוך את המדינה למשטרה גדולה!'",
            options: ["אין כשל לוגי בולט", "כשל איש קש", "כשל מדרון חלקלק"],
            correctAnswerIndex: 1,
            feedback: "מעולה! זיהית נכון. זהו <strong>כשל איש קש</strong>. המתנגד סילף והגזים את ההצעה המקורית (הגבלה נקודתית על מכירה) לטענה קיצונית בהרבה ('להגיד לאנשים מה לאכול ולשתות בכל רגע', 'מדינת משטרה') ואז תקף את הסילוף הזה במקום להתמודד עם ההצעה המקורית.",
            shortFeedback: "כשל איש קש: סילוף עמדת היריב והתקפתה."
        },
        {
            scenario: "חבר מועצה הציע להתקין עוד פסי האטה באזורי בתי ספר כדי להגביר את בטיחות הילדים. תושב מודאג הגיב: 'אם תתחילו להתקין פסי האטה, בקרוב תהיה לנו האטה בכל רחוב בעיר, התנועה תשתק לחלוטין, אנשים יאחרו לעבודה, והכלכלה המקומית תקרוס. אל תעשו את הצעד הראשון הזה בכלל!'",
            options: ["אין כשל לוגי בולט", "כשל איש קש", "כשל מדרון חלקלק"],
            correctAnswerIndex: 2,
            feedback: "צדקת! זהו <strong>כשל מדרון חלקלק</strong>. הטיעון טוען שצעד ראשון קטן (פסי האטה ליד בתי ספר) יוביל בהכרח לסדרה של אירועים שליליים וקיצוניים (שיתוק תנועה, קריסת כלכלה) ללא הוכחה מספקת לקשר הסיבתי החזק בין השלבים.",
             shortFeedback: "כשל מדרון חלקלק: טענה שצעד אחד יוביל בהכרח לסדרת תוצאות שליליות קיצוניות."
        },
        {
            scenario: "מחקר מקיף שפורסם בכתב עת מדעי מוביל מצא קשר מובהק בין צריכה קבועה של מזון מעובד מאוד לבין סיכון מוגבר למחלות לב בטווח הארוך. מסקנת החוקרים: כדאי להגביל את צריכת המזונות הללו כחלק מאורח חיים בריא.",
            options: ["אין כשל לוגי בולט", "כשל איש קש", "כשל מדרון חלקלק"],
            correctAnswerIndex: 0,
            feedback: "נכון מאוד. במקרה זה, אין כשל לוגי בולט בטיעון עצמו כפי שהוצג. המסקנה (המלצה להגביל צריכה) נובעת באופן סביר מממצאי המחקר שהוצגו (קשר מובהק לסיכון למחלות).",
             shortFeedback: "אין כשל לוגי בולט. המסקנה נובעת באופן סביר מההנחות."
        },
         {
            scenario: "האגודה למען בעלי חיים הציגה עמדה נגד שימוש בבעלי חיים בהופעות קרקס נודדות בשל תנאי מחיה ומסעות קשים. בתגובה, בעלי הקרקס טענו בזעם: 'אתם מתנגדים לכל שמחה לילדים! אתם רוצים לבטל את כל המופעים המסורתיים שמשפחות נהנות מהן כבר דורות!'",
            options: ["אין כשל לוגי בולט", "כשל איש קש", "כשל מדרון חלקלק"],
            correctAnswerIndex: 1,
            feedback: "מעולה! זהו <strong>כשל איש קש</strong>. בעלי הקרקס סילפו את עמדת האגודה (התנגדות ספציפית לשימוש בבעלי חיים בקרקסים בשל סיבות מסוימות) לטענה רחבה וקיצונית בהרבה (התנגדות ל'כל שמחה לילדים', 'כל המופעים המסורתיים') ותקפו את הסילוף הקיצוני הזה.",
             shortFeedback: "כשל איש קש: סילוף והגזמה של עמדת היריב."
        },
         {
            scenario: "אם נאפשר לסטודנטים להגיש עבודות סמינריוניות עם שגיאות כתיב קלות ללא הורדת ציון מיידית, בקרוב הם יפסיקו להשקיע בכתיבה לגמרי, אחר כך יפסיקו להגיע להרצאות, ובסוף אף אחד לא ילמד כלום ורמת האקדמיה תרד לשפל חסר תקדים.",
            options: ["אין כשל לוגי בולט", "כשל איש קש", "כשל מדרון חלקלק"],
            correctAnswerIndex: 2,
            feedback: "צדקת! זהו <strong>כשל מדרון חלקלק</strong>. הטיעון מקשר בין צעד קטן יחסית (סלחנות על שגיאות כתיב קלות) לסדרה דרמטית ופסימית של תוצאות קיצוניות (הזנחה טוטאלית, קריסת רמת האקדמיה) ללא ביסוס הגיוני מספק של הקשר הסיבתי המחייב בין השלבים.",
             shortFeedback: "כשל מדרון חלקלק: טענה שצעד קטן יוביל בהכרח לסדרת תוצאות קיצוניות."
        }
        // Add more questions here easily following this structure
    ];

    let currentQuestionIndex = 0;
    let score = 0;
    let selectedOptionIndex = null;
    let questionAttempted = false; // Track if the current question was already attempted

    const scenarioText = document.querySelector('.scenario-text');
    const optionsContainer = document.querySelector('.options-container');
    const optionButtons = document.querySelectorAll('.option-button');
    const submitButton = document.querySelector('.submit-button');
    const feedbackArea = document.querySelector('.feedback-area');
    const feedbackText = document.querySelector('.feedback-text');
    const feedbackIcon = document.querySelector('.feedback-icon');
    const nextButton = document.querySelector('.next-button');
    const questionContainer = document.querySelector('.question-container');
    const resultContainer = document.querySelector('.result-container');
    const scoreDisplay = document.querySelector('.score');
    const scoreAnalysis = document.querySelector('.score-analysis');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const currentQuestionNumberSpan = document.getElementById('current-question-number');
    const totalQuestionsSpan = document.getElementById('total-questions');
    const restartButton = document.querySelector('.restart-button');

    totalQuestionsSpan.textContent = quizData.length;

    function loadQuestion() {
        if (currentQuestionIndex >= quizData.length) {
            displayResults();
            return;
        }

        questionAttempted = false; // Reset attempt status
        const question = quizData[currentQuestionIndex];
        scenarioText.textContent = question.scenario;

        optionButtons.forEach((button, index) => {
            button.textContent = question.options[index];
            button.classList.remove('selected', 'correct', 'incorrect', 'shake');
            button.disabled = false;
            // Reset styles applied directly
            button.style.backgroundColor = '';
            button.style.color = '';
            button.style.borderColor = '';
             button.style.transform = ''; // Reset shake
        });

        selectedOptionIndex = null;
        submitButton.disabled = true;
        submitButton.style.display = 'inline-block'; // Ensure submit button is visible
        feedbackArea.classList.remove('visible', 'feedback-correct', 'feedback-incorrect'); // Hide and reset feedback
        feedbackText.textContent = '';
        feedbackIcon.textContent = ''; // Clear icon content (used ::before)
        nextButton.style.display = 'none';

        // Update progress indicator
        currentQuestionNumberSpan.textContent = currentQuestionIndex + 1;

        // Optional: Add a fade-in animation for the new question content
         questionContainer.classList.remove('fade-out');
         questionContainer.style.opacity = '1'; // Ensure opacity is full after fade-in

    }

    function handleOptionClick(event) {
        if (questionAttempted) return; // Prevent changing selection after submitting
        optionButtons.forEach(btn => btn.classList.remove('selected'));
        event.target.classList.add('selected');
        selectedOptionIndex = parseInt(event.target.dataset.index, 10);
        submitButton.disabled = false;
    }

    function checkAnswer() {
         if (selectedOptionIndex === null || questionAttempted) return;
         questionAttempted = true; // Mark question as attempted

        const question = quizData[currentQuestionIndex];
        const correct = selectedOptionIndex === question.correctAnswerIndex;

        optionButtons.forEach(button => button.disabled = true); // Disable buttons after submission

        feedbackText.textContent = question.feedback;

        if (correct) {
            score++;
            feedbackArea.classList.add('visible', 'feedback-correct');
            optionButtons[selectedOptionIndex].classList.add('correct');

        } else {
            feedbackArea.classList.add('visible', 'feedback-incorrect');
            optionButtons[selectedOptionIndex].classList.add('incorrect');
             optionButtons[selectedOptionIndex].classList.add('shake'); // Add shake animation
             // Highlight the correct answer
             optionButtons[question.correctAnswerIndex].classList.add('correct');
        }

        submitButton.style.display = 'none';
        // Use a small delay before showing next button to allow feedback to be processed/animated
        setTimeout(() => {
            nextButton.style.display = 'block';
        }, 800); // Delay in ms
    }

    function nextQuestion() {
        // Start fade out animation for current question
         questionContainer.classList.add('fade-out');

        // Wait for fade out before loading next question
         setTimeout(() => {
             currentQuestionIndex++;
             loadQuestion();
              questionContainer.classList.remove('fade-out'); // Remove class immediately after timeout
         }, 500); // Match CSS transition duration
    }

    function displayResults() {
        questionContainer.style.display = 'none';
        resultContainer.style.display = 'block';
         resultContainer.classList.add('visible'); // Fade in results

        scoreDisplay.textContent = `הציון הסופי שלך: ${score} מתוך ${quizData.length}`;

         let analysis = '';
         if (score === quizData.length) {
             analysis = 'מצוין! זיהית את כל הכשלים הלוגיים בהצלחה! אתה בלש לוגי אמיתי!';
             resultContainer.querySelector('.completion-message').textContent = 'תוצאה מושלמת!';
             resultContainer.querySelector('h2').style.color = var(--success-color);
         } else if (score >= quizData.length * 0.8) {
             analysis = 'יפה מאוד! זיהית את רוב הכשלים. אתה בדרך הנכונה להיות מומחה בזיהוי כשלים!';
              resultContainer.querySelector('.completion-message').textContent = 'כל הכבוד!';
               resultContainer.querySelector('h2').style.color = var(--primary-dark);
         } else if (score >= quizData.length * 0.5) {
             analysis = 'טוב מאוד. זיהית חלק מהכשלים. המשך לתרגל והשתפר!';
              resultContainer.querySelector('.completion-message').textContent = 'תוצאות הסימולציה';
               resultContainer.querySelector('h2').style.color = var(--secondary-dark);
         } else {
             analysis = 'התחלה טובה! זיהוי כשלים דורש אימון. קרא שוב את ההסברים ונסה שוב!';
              resultContainer.querySelector('.completion-message').textContent = 'תוצאות הסימולציה';
               resultContainer.querySelector('h2').style.color = var(--danger-color);
         }
        scoreAnalysis.textContent = analysis;

    }

    function toggleExplanation() {
         if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
             explanationDiv.style.display = 'block';
             toggleExplanationButton.textContent = 'הסתר הסבר על כשלים לוגיים';
         } else {
             explanationDiv.style.display = 'none';
             toggleExplanationButton.textContent = 'הצג הסבר על כשלים לוגיים';
         }
     }

    function restartQuiz() {
         currentQuestionIndex = 0;
         score = 0;
         resultContainer.classList.remove('visible');
         resultContainer.style.display = 'none';
         questionContainer.style.display = 'block'; // Show question container
         loadQuestion(); // Load the first question
     }


    optionButtons.forEach(button => button.addEventListener('click', handleOptionClick));
    submitButton.addEventListener('click', checkAnswer);
    nextButton.addEventListener('click', nextQuestion);
    toggleExplanationButton.addEventListener('click', toggleExplanation);
    restartButton.addEventListener('click', restartQuiz);


    // Initial load
    loadQuestion();
</script>
```