---
title: "לזהות כשלים קוגניטיביים בפרסומות: משחק חשיבה ביקורתית"
english_slug: identifying-cognitive-biases-in-advertisements-game
category: "מדעי החברה / פסיכולוגיה"
tags:
  - כשלים קוגניטיביים
  - פרסום
  - פסיכולוגיה
  - כלכלה התנהגותית
  - חשיבה ביקורתית
---
# לזהות כשלים קוגניטיביים בפרסומות: משחק חשיבה ביקורתית

האם אי פעם הרגשתם דחף לקנות משהו רק בגלל התחושה שהזמן אוזל, או כי נראה שכולם כבר קנו אותו? עולם הפרסום הוא זירת קרב על תשומת הלב והארנק שלנו, ומפרסמים מודעים היטב ל"באגים" בחיווט המנטלי שלנו. הם משתמשים בטכניקות פסיכולוגיות מתוחכמות כדי לעקוף את החשיבה הרציונלית ולדחוף אותנו לפעולה. האם אתם מוכנים לאמן את מערכת 2 שלכם ולזהות את המלכודות הקוגניטיביות שהם מציבים? שחקו וגלו כמה אתם עמידים בפני מניפולציות שיווקיות!

<div id="cognitiveBiasGame">
    <div class="game-area">
        <div id="progressIndicator" class="progress"></div>
        <div id="adDisplay" class="card ad-card">
            <p id="adText" class="ad-text"></p>
        </div>
        <div id="biasOptions" class="options-card">
            <p class="options-prompt">איזה כשל קוגניטיבי הפרסומת מנצלת **בעיקר**?</p>
            <!-- Bias options will be populated here -->
        </div>
        <button id="submitAnswer" class="game-button primary">בדיקה</button>
    </div>

    <div id="feedback" class="card feedback-card" style="display: none;">
        <p id="feedbackText" class="feedback-message"></p>
        <div id="feedbackDetails">
             <p id="biasExplanation" class="explanation"></p>
             <p id="adAnalysis" class="analysis"></p>
        </div>
        <button id="nextAd" class="game-button secondary" style="display: none;">הפרסומת הבאה →</button>
    </div>
</div>

<style>
    /* Global Styles */
    :root {
        --primary-color: #007bff;
        --primary-hover: #0056b3;
        --secondary-color: #6c757d;
        --secondary-hover: #5a6268;
        --success-color: #28a745;
        --danger-color: #dc3545;
        --background-color: #f4f7f6;
        --card-background: #ffffff;
        --border-color: #e0e0e0;
        --text-color: #333;
        --subtle-text: #555;
        --font-family: 'Arial', sans-serif;
    }

    #cognitiveBiasGame {
        font-family: var(--font-family);
        max-width: 650px;
        margin: 25px auto;
        padding: 25px;
        border-radius: 12px;
        background-color: var(--background-color);
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Ensure animations stay within bounds */
    }

    #cognitiveBiasGame h2 {
        text-align: center;
        color: var(--text-color);
        margin-top: 0;
        margin-bottom: 25px;
    }

    /* Game Elements */
    .game-area, .feedback-card {
        opacity: 1;
        transition: opacity 0.6s ease-in-out;
    }

    .progress {
        text-align: center;
        color: var(--subtle-text);
        margin-bottom: 15px;
        font-size: 0.9em;
    }

    .card {
        background-color: var(--card-background);
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .ad-card {
        min-height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-style: italic;
        background-color: #eef2f3; /* Slightly different background */
        color: var(--subtle-text);
        font-size: 1.1em;
    }

    .ad-text {
        margin: 0;
        line-height: 1.6;
    }

    .options-card .options-prompt {
        margin-top: 0;
        margin-bottom: 15px;
        font-weight: bold;
        color: var(--text-color);
    }

    #biasOptions label {
        display: block;
        margin-bottom: 10px;
        cursor: pointer;
        padding: 12px 15px;
        border: 1px solid var(--border-color);
        border-radius: 6px;
        background-color: var(--card-background);
        transition: background-color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        align-items: center;
    }

    #biasOptions label:hover {
        background-color: #f8f8f8;
        border-color: #c0c0c0;
    }

    #biasOptions input[type="radio"] {
        margin-left: 10px;
        /* Hide default radio button */
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        border: 2px solid var(--subtle-text);
        border-radius: 50%;
        outline: none;
        cursor: pointer;
        position: relative;
        flex-shrink: 0; /* Prevent shrinking */
    }

    #biasOptions input[type="radio"]:checked {
        border-color: var(--primary-color);
    }

    #biasOptions input[type="radio"]:checked::before {
        content: '';
        width: 10px;
        height: 10px;
        background-color: var(--primary-color);
        border-radius: 50%;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    /* Visual feedback on options after check */
    #biasOptions label.correct-answer {
        border-color: var(--success-color);
        background-color: #e9f7ef; /* Light green */
        box-shadow: 0 0 8px rgba(40, 167, 69, 0.3);
    }

    #biasOptions label.correct-answer input[type="radio"] {
        border-color: var(--success-color);
    }
     #biasOptions label.correct-answer input[type="radio"]:checked::before {
        background-color: var(--success-color);
     }


    #biasOptions label.incorrect-choice {
        border-color: var(--danger-color);
        background-color: #fdedee; /* Light red */
        box-shadow: 0 0 8px rgba(220, 53, 69, 0.3);
        text-decoration: line-through; /* Optional: strike through incorrect text */
        opacity: 0.7;
    }
     #biasOptions label.incorrect-choice input[type="radio"] {
        border-color: var(--danger-color);
     }
     #biasOptions label.incorrect-choice input[type="radio"]:checked::before {
         background-color: var(--danger-color);
     }


    .game-button {
        display: block;
        width: 100%;
        padding: 12px 20px;
        font-size: 17px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        margin-top: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
    }

    .game-button.primary {
        background-color: var(--primary-color);
        color: white;
    }

    .game-button.primary:hover:not(:disabled) {
        background-color: var(--primary-hover);
        transform: translateY(-1px);
    }

    .game-button.secondary {
        background-color: var(--secondary-color);
        color: white;
        margin-top: 20px; /* More space after feedback */
    }
     .game-button.secondary:hover:not(:disabled) {
        background-color: var(--secondary-hover);
        transform: translateY(-1px);
     }


    .game-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
    }

    /* Feedback Section */
    .feedback-card {
        background-color: #e9ecef; /* Lighter background for feedback */
        border-color: #ced4da;
        padding: 25px;
    }

    .feedback-message {
        font-size: 1.3em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .feedback-message::before {
        content: '';
        margin-left: 10px;
        width: 24px;
        height: 24px;
        background-size: contain;
        background-repeat: no-repeat;
    }

    .feedback-message.correct {
        color: var(--success-color);
    }

    .feedback-message.correct::before {
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%2328a745"><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/></svg>');
    }


    .feedback-message.incorrect {
        color: var(--danger-color);
    }
     .feedback-message.incorrect::before {
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%23dc3545"><path d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41z"/></svg>');
     }

    #feedbackDetails {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px dashed var(--border-color);
    }

    #feedbackDetails p {
        margin-bottom: 12px;
        line-height: 1.6;
        color: var(--subtle-text);
    }

    #feedbackDetails strong {
        color: var(--text-color);
    }

    .explanation {
         font-style: italic;
         font-size: 0.95em;
    }

    .analysis {
        font-size: 0.95em;
    }


    /* Explanation Section */
    #explanationSection {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: #eef2f3; /* Matches ad background */
        direction: rtl;
        text-align: right;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    #explanationSection h3 {
        color: var(--text-color);
        margin-top: 0;
        margin-bottom: 20px;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
    }

    #explanationSection h4 {
         color: var(--subtle-text);
         margin-top: 20px;
         margin-bottom: 10px;
    }

    #explanationSection p {
        margin-bottom: 15px;
        line-height: 1.7;
        color: var(--text-color);
    }

     #explanationSection ul {
        margin-bottom: 15px;
        padding-right: 20px;
        color: var(--text-color);
     }

    #explanationSection li {
        margin-bottom: 10px;
        line-height: 1.6;
    }

     #explanationSection li strong {
        color: var(--subtle-text);
     }

    #toggleExplanationButton {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 16px;
        cursor: pointer;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #toggleExplanationButton:hover {
        background-color: var(--secondary-hover);
         transform: translateY(-1px);
    }

</style>

<button id="toggleExplanationButton">הצגת/הסתרת הסבר מורחב</button>

<div id="explanationSection" style="display: none;">
    <h3>הסבר: כשלים קוגניטיביים בפרסומות</h3>

    <h4>מהם כשלים קוגניטיביים?</h4>
    <p>כשלים קוגניטיביים הם דפוסי חשיבה או קיצורי דרך מנטליים (היוריסטיקות) שמוחנו מפתח כדי לעבד מידע במהירות וביעילות. למרות שהם שימושיים בדרך כלל, הם עלולים להוביל להטיות שיטתיות בקבלת החלטות ובשיפוט, ולגרום לנו לסטות מחשיבה רציונלית או לוגית.</p>

    <h4>כיצד המוח שלנו מקבל החלטות במהירות? (מערכת 1 ומערכת 2)</h4>
    <p>דניאל כהנמן, זוכה פרס נובל לכלכלה, מתאר שתי מערכות חשיבה עיקריות:</p>
    <ul>
        <li><strong>מערכת 1:</strong> מהירה, אינטואיטיבית, אוטומטית, ופועלת ללא מאמץ מודע. היא אחראית לתגובות מיידיות ולשיפוטים מהירים (למשל, זיהוי פנים כעוסות). מערכת זו נוטה להשתמש בהיוריסטיקות ולהיות מושפעת מכשלים קוגניטיביים.</li>
        <li><strong>מערכת 2:</strong> איטית, מחושבת, אנליטית, ודורשת מאמץ מודע. היא אחראית לפתרון בעיות מורכבות ולחשיבה לוגית (למשל, חישוב מסובך). מערכת זו יכולה לתקן את ההטיות של מערכת 1, אך היא "עצלנית" ודורשת אנרגיה קוגניטיבית.</li>
    </ul>
    <p>פרסומות רבות מכוונות ישירות למערכת 1 שלנו, מנצלות את קיצורי הדרך שלה כדי לעודד קבלת החלטות מהירה ואינטואיטיבית, לעתים קרובות תוך עקיפת המערכת האנליטית והביקורתית (מערכת 2).</p>

    <h4>למה כשלים קוגניטיביים מהווים נקודת תורפה שניתן לנצל בפרסום?</h4>
    <p>הנטייה הטבעית של המוח לשימוש בקיצורי דרך הופכת אותו לפגיע למניפולציות. מפרסמים מבינים שהצרכנים לרוב לא מקדישים זמן ומאמץ (של מערכת 2) לניתוח יסודי של כל פרסומת או מוצר. לכן, הם מעצבים מסרים שנועדו לעורר תגובה אוטומטית דרך מערכת 1, תוך ניצול כשלים מוכרים שמשפיעים על הרצון, התפיסה וההחלטה לקנות.</p>

    <h4>סקירה של הכשלים הקוגניטיביים הנפוצים ביותר בפרסומות:</h4>
    <ul>
        <li><strong>אפקט העדר (Bandwagon Effect):</strong> הנטייה לאמץ אמונות או התנהגויות רק בגלל ש... אנשים רבים אחרים עושים זאת. פרסומות מנצלות זאת באמצעות סיסמאות כמו "המוצר הנמכר ביותר", "מיליוני לקוחות מרוצים", או הצגת אנשים רבים משתמשים במוצר. המסר הסמוי הוא: "אם כולם עושים את זה, זה בטח טוב ונכון".</li>
        <li><strong>עוגן (Anchoring Bias):</strong> הנטייה להסתמך יתר על המידה על... פיסת המידע הראשונה (ה"עוגן") שמוצגת בעת קבלת החלטה. פרסומות מציגות מחיר מקורי גבוה (העוגן) ואז מחיר מבצע נמוך יותר, כדי לגרום למחיר המבצע להיראות אטרקטיבי יותר, גם אם הוא עדיין גבוה יחסית.</li>
        <li><strong>מחסור (Scarcity Heuristic):</strong> התפיסה שדברים נדירים או זמינים לזמן מוגבל... הם יקרים יותר או בעלי ערך גבוה יותר. פרסומות משתמשות בביטויים כמו "מלאי מוגבל", "מבצע ל-24 שעות בלבד", "הזדמנות אחרונה", כדי ליצור תחושת דחיפות ולדחוף לקנייה מיידית לפני שההזדמנות "תברח".</li>
        <li><strong>אפקט המסגור (Framing Effect):</strong> הנטייה להגיע למסקנות שונות מאותו המידע, תלוי... באיך המידע מוצג ("מסוגר"). הצגת מוצר כ"99% ללא שומן" נתפסת חיובית יותר מאשר הצגתו כ"מכיל 1% שומן", למרות שמדובר באותו מידע. פרסומות ממסגרות את המוצר או ההצעה באור החיובי ביותר האפשרי.</li>
        <li><strong>היוריסטיקת הזמינות (Availability Heuristic):</strong> הנטייה להעריך את הסבירות של אירוע מסוים... לפי הקלות שבה דוגמאות או מידע קופצים לראשנו. פרסומות המשתמשות בעדויות אישיות מרגשות, סיפורי הצלחה קיצוניים, או דימויים ויזואליים חזקים וזכירים, גורמות לתוצאה החיובית של שימוש במוצר להיראות זמינה, סבירה וקרובה יותר.</li>
        <li><strong>הטיית האישור (Confirmation Bias):</strong> הנטייה לחפש, לפרש, להעדיף ולזכור מידע... שמאשר את האמונות או ההשערות הקיימות שלנו. פרסומות המכוונות לפלחי שוק ספציפיים עם מסרים שתואמים את ערכיהם או תפיסותיהם העצמיות, או המציגות ביקורות חיוביות בלבד, מחזקות את הנטייה של הצרכן לאשר דעות קדומות חיוביות שיש לו (או שנוצרו אצלו) לגבי המוצר או המותג.</li>
    </ul>

    <h4>איך חשיבה ביקורתית וזיהוי כשלים משפרים את העמידות שלנו בפני מניפולציות שיווקיות</h4>
    <p>מודעות לכשלים הקוגניטיביים ולדרך שבה הם מנוצלים בפרסום היא הצעד הראשון בחשיבה ביקורתית. כאשר אנו מזהים טקטיקה כזו בפעולה, אנו יכולים לעצור, להפעיל את מערכת 2, ולשאול שאלות כמו: האם אני באמת צריך את המוצר? האם המחיר המקורי רלוונטי? האם כולם באמת משתמשים בזה, ומה זה אומר על המוצר עצמו ולא על הפופולריות שלו? האם אני קונה בגלל תחושת הדחיפות או בגלל שהמוצר עונה על צורך אמיתי? זיהוי הכשלים מאפשר לנו לקבל החלטות מודעות יותר, המבוססות על צרכים ורציונל, ולא על מניפולציות פסיכולוגיות.</p>
</div>

<script>
    const advertisements = [
        {
            adText: "מבצע מיוחד! נותרו רק 3 פריטים במלאי! אל תפספסו!",
            correctBias: "מחסור",
            potentialBiases: ["מחסור", "אפקט העדר", "עוגן", "אפקט המסגור"],
            biasExplanation: "<strong>מחסור:</strong> הנטייה להעריך דברים יקר יותר כשהם נדירים או זמינים לזמן מוגבל.",
            adAnalysis: "הפרסומת משתמשת בכשל המחסור על ידי יצירת תחושת דחיפות ('נותרו רק 3') כדי לדרבן קנייה מיידית לפני שהמלאי ייגמר. זה מעודד פעולה אימפולסיבית במקום חשיבה רציונלית."
        },
        {
            adText: "מחיר השקה מיוחד: ₪199 (במקום ₪399)! חיסכון מדהים!",
            correctBias: "עוגן",
            potentialBiases: ["עוגן", "היוריסטיקת הזמינות", "הטיית האישור", "אפקט המסגור"],
            biasExplanation: "<strong>עוגן:</strong> הנטייה להסתמך על פיסת המידע הראשונה (העוגן) בעת הערכת ערך או מחיר.",
            adAnalysis: "המחיר המקורי הגבוה (₪399) משמש כעוגן שיוצר תחושה שהמחיר החדש (₪199) הוא מציאה גדולה וחיסכון משמעותי. המוח נאחז ב'עוגן' הגבוה כדי להעריך את המחיר הנוכחי, לעיתים קרובות בלי לבדוק האם המחיר המקורי היה אי פעם ריאלי, או מהו הערך האמיתי של המוצר."
        },
        {
            adText: "המוצר שכבש את המדינה! הצטרפו למיליוני הלקוחות שכבר נהנים ממנו!",
            correctBias: "אפקט העדר",
            potentialBiases: ["אפקט העדר", "מחסור", "עוגן", "היוריסטיקת הזמינות"],
            biasExplanation: "<strong>אפקט העדר:</strong> הנטייה לאמץ התנהגות רק בגלל שאנשים רבים אחרים עושים זאת.",
            adAnalysis: "המסר מתבסס על הרעיון שפופולריות מעידה על איכות. ההתייחסות ל'מיליוני הלקוחות' מעודדת אנשים להצטרף ל'עדר' מתוך הנחה שמה שטוב לאחרים יהיה טוב גם להם, תוך עקיפת הצורך להעריך את המוצר לגופו."
        },
         {
            adText: "השתמשו בקרם הפנים שלנו ותראו שיפור ב-90% מהמקרים!",
            correctBias: "אפקט המסגור",
            potentialBiases: ["אפקט המסגור", "הטיית האישור", "עוגן", "מחסור"],
            biasExplanation: "<strong>אפקט המסגור:</strong> תגובה שונה לאותו מידע בהתאם לאופן הצגתו (מסגור).",
            adAnalysis: "המספר 90% נשמע חיובי ומעודד מאוד ('90% שיפור'). מסגור חלופי, כמו 'ב-10% מהמקרים אין שיפור' או 'המוצר עובד רק ב-90% מהמקרים', היה נשמע פחות אטרקטיבי, למרות שמדובר באותה סטטיסטיקה בדיוק. הפרסומת ממסגרת את הנתון בצורה שתעורר תגובה חיובית אוטומטית."
        },
         {
            adText: "ראית את הפרסומת המרגשת בטלוויזיה? אנשים בכו מאושר משימוש במוצר שלנו!",
            correctBias: "היוריסטיקת הזמינות",
            potentialBiases: ["היוריסטיקת הזמינות", "אפקט העדר", "עוגן", "מחסור"],
            biasExplanation: "<strong>היוריסטיקת הזמינות:</strong> הערכת סבירות לפי קלות היזכרות בדוגמאות רלוונטיות.",
            adAnalysis: "התיאור הדרמטי והרגשי ('אנשים בכו מאושר') יוצר תמונה חזקה וזכירה שגורמת לתוצאה החיובית הקיצונית להיראות זמינה, קלה לדמיין, וכתוצאה מכך - סבירה יותר עבור הצרכן הפוטנציאלי. המוח נוטה לייחס סבירות גבוהה יותר לאירועים שהוא יכול לשלוף בקלות מהזיכרון, במיוחד אם הם מלווים ברגש חזק."
        },
         {
            adText: "אם אתם שייכים לאנשים שמעריכים איכות אמיתית... המוצר הזה בשבילכם.",
            correctBias: "הטיית האישור",
            potentialBiases: ["הטיית האישור", "אפקט העדר", "עוגן", "אפקט המסגור"],
            biasExplanation: "<strong>הטיית האישור:</strong> נטייה לחפש, לפרש, ולזכור מידע שמאשר אמונות קיימות.",
            adAnalysis: "הפרסומת פונה ישירות לאנשים שרואים את עצמם כמעריכי איכות. היא מנצלת את הנטייה שלנו לאשר את התפיסה העצמית שלנו ('אני מעריך איכות, ולכן המוצר הזה מתאים לי') ולהתעלם ממידע שסותר אותה. היא מחזקת את האמונה של קהל היעד בעצמו וקושרת אותה למוצר."
        }
    ];

    // Map from bias value to user-friendly name (already in biasDefinitions structure now)
    const biasDefinitions = {
        "אפקט העדר": "הנטייה לאמץ אמונות/התנהגויות כי אחרים עושים זאת.",
        "עוגן": "הסתמכות על פיסת המידע הראשונה בקבלת החלטה.",
        "מחסור": "הערכת ערך גבוה יותר לדברים נדירים או זמינים לזמן מוגבל.",
        "אפקט המסגור": "תגובה שונה לאותו מידע בהתאם לאופן הצגתו.",
        "היוריסטיקת הזמינות": "הערכת סבירות לפי קלות היזכרות בדוגמאות רלוונטיות.",
        "הטיית האישור": "נטייה לחפש, לפרש, ולזכור מידע שמאשר אמונות קיימות."
    };


    let currentAdIndex = 0;
    const totalAds = advertisements.length;

    const gameAreaElement = document.querySelector('.game-area');
    const adTextElement = document.getElementById('adText');
    const biasOptionsElement = document.getElementById('biasOptions');
    const submitButton = document.getElementById('submitAnswer');
    const feedbackElement = document.getElementById('feedback');
    const feedbackTextElement = document.getElementById('feedbackText');
    const biasExplanationElement = document.getElementById('biasExplanation');
    const adAnalysisElement = document.getElementById('adAnalysis');
    const nextAdButton = document.getElementById('nextAd');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');
    const explanationSection = document.getElementById('explanationSection');
    const progressIndicator = document.getElementById('progressIndicator');


    function loadAd(index) {
        if (index < totalAds) {
            const currentAd = advertisements[index];

            // Update progress
            progressIndicator.textContent = `שאלה ${index + 1} מתוך ${totalAds}`;

            // Reset and prepare for new ad
            adTextElement.textContent = ''; // Clear text for animation
            biasOptionsElement.innerHTML = '<p class="options-prompt">איזה כשל קוגניטיבי הפרסומת מנצלת **בעיקר**?</p>'; // Reset options
            feedbackElement.style.display = 'none';
            nextAdButton.style.display = 'none';
            submitButton.style.display = 'block';
            submitButton.disabled = false;
            submitButton.classList.remove('hidden'); // Ensure button is visible

            // Populate options with animation
            currentAd.potentialBiases.forEach((bias, i) => {
                const label = document.createElement('label');
                const input = document.createElement('input');
                input.type = 'radio';
                input.name = 'bias';
                input.value = bias;
                label.appendChild(input);
                label.appendChild(document.createTextNode(bias));
                label.style.opacity = 0; // Start hidden
                label.style.transform = 'translateY(10px)'; // Start slightly lower
                biasOptionsElement.appendChild(label);

                // Fade-in and slide-up animation for options
                setTimeout(() => {
                     label.style.transition = 'opacity 0.4s ease-out, transform 0.4s ease-out';
                     label.style.opacity = 1;
                     label.style.transform = 'translateY(0)';
                }, 100 + i * 70); // Stagger animation

                 // Add event listener for visual feedback on selection
                 input.addEventListener('change', handleOptionSelect);
            });

             // Fade-in ad text
             setTimeout(() => {
                 adTextElement.style.opacity = 0;
                 adTextElement.textContent = currentAd.adText;
                 adTextElement.style.transition = 'opacity 0.8s ease-in-out';
                 adTextElement.style.opacity = 1;
             }, 200); // Slightly delay ad text animation


             // Ensure game area is visible after potential feedback section hiding
             gameAreaElement.style.opacity = 1;


        } else {
            // Game finished
            progressIndicator.textContent = `סיימת את המשחק! 🎉`;
            adTextElement.textContent = "זהו זה! סיימת את המשחק. מקווה שלמדת לזהות טוב יותר כשלים קוגניטיביים בפרסומות ולהיות צרכן ביקורתי יותר.";
            biasOptionsElement.innerHTML = ""; // Clear options
            submitButton.style.display = 'none';
            feedbackElement.style.display = 'none';
            nextAdButton.style.display = 'none';
        }
    }

    function handleOptionSelect(event) {
        // Remove 'selected' class from all labels first
        biasOptionsElement.querySelectorAll('label').forEach(label => {
            label.classList.remove('selected');
        });
        // Add 'selected' class to the parent label of the checked radio button
        if (event.target.checked) {
            event.target.parentElement.classList.add('selected');
        }
    }


    function checkAnswer() {
        const selectedInput = document.querySelector('#biasOptions input[name="bias"]:checked');
        if (!selectedInput) {
            // Basic alert for now, could be a nicer modal/tooltip
            alert('אנא בחר כשל קוגניטיבי לפני הבדיקה.');
            return;
        }

        const userChoice = selectedInput.value;
        const currentAd = advertisements[currentAdIndex];
        const isCorrect = userChoice === currentAd.correctBias;

        // Disable options and submit
        document.querySelectorAll('#biasOptions input[name="bias"]').forEach(input => input.disabled = true);
        submitButton.disabled = true;
        submitButton.classList.add('hidden'); // Hide submit button

        // Add visual feedback to labels
         document.querySelectorAll('#biasOptions label').forEach(label => {
             const input = label.querySelector('input');
             if (input.value === currentAd.correctBias) {
                 label.classList.add('correct-answer');
             } else if (input.value === userChoice) {
                 label.classList.add('incorrect-choice');
             }
         });


        // Prepare and display feedback
        if (isCorrect) {
            feedbackTextElement.textContent = 'נכון מאוד! כל הכבוד! 🎉';
            feedbackTextElement.className = 'feedback-message correct';
        } else {
            feedbackTextElement.textContent = `אופס, לא בדיוק. 🤔`;
             feedbackTextElement.className = 'feedback-message incorrect';
        }

        biasExplanationElement.innerHTML = `<strong>הכשל שבחרת (${userChoice}):</strong> ${biasDefinitions[userChoice] || "אין הסבר זמין לכשל זה."}`;
        adAnalysisElement.innerHTML = `<strong>ניתוח הפרסומת (הכשל העיקרי הוא ${currentAd.correctBias}):</strong> ${currentAd.adAnalysis}`;

        // Animate transition
        gameAreaElement.style.opacity = 0;
        setTimeout(() => {
            gameAreaElement.style.display = 'none'; // Hide the game area after fading

            feedbackElement.style.display = 'block'; // Make feedback visible
            // Trigger fade-in for feedback
            feedbackElement.style.opacity = 0; // Start hidden
            setTimeout(() => {
                 feedbackElement.style.transition = 'opacity 0.6s ease-in-out';
                 feedbackElement.style.opacity = 1;
            }, 50); // Small delay to ensure display: block is processed

            nextAdButton.style.display = 'block'; // Show next button

        }, 600); // Wait for game area fade-out

    }

    function nextAd() {
        currentAdIndex++;
        // Animate feedback out before loading next ad
        feedbackElement.style.opacity = 0;
         setTimeout(() => {
            feedbackElement.style.display = 'none'; // Hide feedback after fading
            gameAreaElement.style.display = 'block'; // Make game area visible again
            loadAd(currentAdIndex);
         }, 600); // Wait for feedback fade-out
    }

     function toggleExplanation() {
        const isHidden = explanationSection.style.display === 'none';
        if (isHidden) {
            explanationSection.style.display = 'block';
            // Simple fade-in animation
             explanationSection.style.opacity = 0;
             setTimeout(() => {
                 explanationSection.style.transition = 'opacity 0.5s ease-in-out';
                 explanationSection.style.opacity = 1;
             }, 50);

            toggleExplanationButton.textContent = 'הסתרת הסבר מורחב';
        } else {
             // Simple fade-out animation
             explanationSection.style.opacity = 1;
             setTimeout(() => {
                 explanationSection.style.transition = 'opacity 0.5s ease-in-out';
                 explanationSection.style.opacity = 0;
             }, 50);
             setTimeout(() => {
                explanationSection.style.display = 'none';
                 toggleExplanationButton.textContent = 'הצגת/הסתרת הסבר מורחב';
             }, 550); // Match duration
        }
    }

    // Initial Event Listeners
    submitButton.addEventListener('click', checkAnswer);
    nextAdButton.addEventListener('click', nextAd);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Initial load
    loadAd(currentAdIndex);

</script>
```