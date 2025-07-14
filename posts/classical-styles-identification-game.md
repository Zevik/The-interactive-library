---
title: "מזהים את הסגנון: בארוק, קלאסי או רומנטי?"
english_slug: classical-styles-identification-game
category: "אמנות ועיצוב / מוזיקה"
tags:
  - מוזיקה קלאסית
  - היסטוריה של המוזיקה
  - בארוק
  - קלאסי
  - רומנטי
---
<h1>מזהים את הסגנון: בארוק, קלאסי או רומנטי?</h1>

<p>האם כל המוזיקה הקלאסית נשמעת לכם אותו דבר? האם תוכלו להבחין בהבדלים העדינים בין יצירות שנכתבו במאות ה-17, ה-18 וה-19? בואו נצא למסע מרתק בזמן! האזינו לקטעים קצרים מיצירות מופת ובדקו האם תוכלו לזהות את הסגנון: בארוק, קלאסי או רומנטי. זה לא רק משחק, זו הרפתקה שתחדד לכם את האוזן ותגלה עולם של הבדלים מרתקים.</p>

<div id="app">
    <div id="game-header">
        <div id="score"></div>
        <div id="progress"></div>
    </div>
    <div id="question-area">
        <audio id="audio-player" src="" preload="auto"></audio>
        <div id="audio-control">
            <button id="play-button" disabled>האזנה לקטע</button>
            <div id="audio-status" class="status-message" style="display: none;">טוען קטע...</div>
        </div>
        <div id="choices" class="interactive-area" style="display: none;">
            <p class="instruction">בחר את הסגנון:</p>
            <div class="button-container">
                <button class="style-button" data-style="בארוק">בארוק</button>
                <button class="style-button" data-style="קלאסי">קלאסי</button>
                <button class="style-button" data-style="רומנטי">רומנטי</button>
            </div>
        </div>
    </div>
    <div id="feedback" class="feedback-message"></div>
    <div id="question-info" class="info-box" style="display: none;">
        <h3>על היצירה:</h3>
        <p><strong>היצירה:</strong> <span id="piece-title"></span></p>
        <p><strong>מלחין:</strong> <span id="composer"></span></p>
        <p><strong>תקופה:</strong> <span id="year"></span></p>
        <p><strong>הסגנון הנכון:</strong> <span id="correct-style"></span></p>
        <p><strong>רמז לזיהוי:</strong> <span id="style-hint"></span></p>
    </div>
    <button id="next-button" class="control-button primary" style="display: none;">הבא</button>
</div>

<div id="end-game" class="end-game-screen" style="display: none;">
    <h2>המשחק הסתיים!</h2>
    <p class="final-score-text">הניקוד הסופי שלך: <span id="final-score"></span> מתוך <span id="total-questions-end"></span></p>
    <button id="restart-button" class="control-button secondary">שחק שוב</button>
</div>

<button id="toggle-explanation" class="control-button tertiary">הצג/הסתר הסבר על הסגנונות</button>

<div id="explanation" class="info-box explanation-box" style="display: none;">
    <h2>למה חשוב להבדיל בין סגנונות במוזיקה קלאסית?</h2>
    <p>הבנת ההבדלים בין הסגנונות השונים במוזיקה הקלאסית (בארוק, קלאסי, רומנטי ואחרים) מאפשרת לנו להעריך טוב יותר את ההקשר ההיסטורי, התרבותי והאמנותי שבו יצירה נוצרה. כל תקופה הציגה חידושים ומאפיינים ייחודיים מבחינת הרמוניה, מלודיה, קצב, מבנה, תזמור, ואף הפילוסופיה שמאחורי המוזיקה. זיהוי הסגנון עוזר לנו להקשיב באופן מודע יותר, לצפות (ולפעמים להיות מופתעים) מההתפתחויות בתוך היצירה, ולהתחבר לעולם המחשבה והרגש של המלחין.</p>

    <h2>סגנון הבארוק (בערך 1600-1750)</h2>
    <h3>מאפיינים מרכזיים</h3>
    <ul>
        <li>**קונטרפונקט (פוליפוניה):** ריבוי קווים מלודיים עצמאיים הנשזרים זה בזה בו זמנית (כמו בפוגה).</li>
        <li>**ריתמיות יציבה:** דופק או קצב מנועתי קבוע לאורך רוב היצירה.</li>
        <li>**קישוטיות:** שימוש נרחב בקישוטים מלודיים (טרילים, מורדנטים וכו').</li>
        <li>**בס ממוספר (Basso Continuo):** ליווי הרמוני שמבוצע לרוב על ידי כלי בס (צ'לו, בסון) וכלי אקורדים (צ'מבלו, עוגב), כאשר המלחין מציין את האקורדים באמצעות ספרות מעל תו הבס.</li>
        <li>**דינמיקה מדורגת (טרסית):** מעברים חדים בין עוצמה חזקה לחלשה, ולא מעברים הדרגתיים (קרשנדו/דקרשנדו).</li>
        <li>**רגש אחיד:** לרוב, פרק שלם או קטע ביצירה מבטא "אפקט" (רגש) אחד דומיננטי.</li>
    </ul>
    <h3>מלחינים בולטים</h3>
    <p>יוהאן סבסטיאן באך, גאורג פרידריך הנדל, אנטוניו ויולדי, גאורג פיליפ טלמן, הנרי פרסל, קלאודיו מונטוורדי.</p>
    <h3>דוגמאות שמיעתיות (סוגי יצירות)</h3>
    <p>קונצ'רטו גרוסו, סוויטה, פוגה, טוקטה, קנטטה, אורטוריה, אופרה מוקדמת.</p>

    <h2>הסגנון הקלאסי (בערך 1750-1820)</h2>
    <h3>מאפיינים מרכזיים</h3>
    <ul>
        <li>**מלודיה ברורה וקליטה:** דגש על מנגינות סימטריות, לרוב בעלות אופי "שירתי" או "פופולרי" לתקופתן.</li>
        <li>**מרקם הומופוני דומיננטי:** מלודיה אחת מובילה עם ליווי אקורדי (פחות דגש על ריבוי קולות עצמאיים כמו בבארוק).</li>
        <li>**איזון, סימטריה ובהירות:** מבנה פורמלי מוגדר (צורת סונטה, מינואט וטריו, רונדו) והתפתחות לוגית של הרעיונות המוזיקליים.</li>
        <li>**פיתוח הדרגתי:** שימוש בקרשנדו ודקרשנדו ליצירת מתח ושחרור.</li>
        <li>**הפסנתר:** הופעתו והתפתחותו של הפסנתר ככלי מרכזי, מחליף בהדרגה את הצ'מבלו.</li>
        <li>**תזמור ברור:** שימוש סטנדרטי יותר בתזמורת עם חטיבות כלי קשת, נשיפה מעץ, נשיפה ממתכת (מוגבלת) וכלי הקשה (טימפני).</li>
    </ul>
    <h3>מלחינים בולטים</h3>
    <p>וולפגנג אמדאוס מוצרט, יוזף היידן, לודוויג ואן בטהובן (יצירותיו המוקדמות והאמצעיות), כריסטוף ויליבלד גלוק.</p>
    <h3>דוגמאות שמיעתיות (סוגי יצירות)</h3>
    <p>סימפוניה, קונצ'רטו סולו (עם כלי אחד), סונטה לפסנתר, רביעיית מיתרים, אופרה (קומית ורצינית).</p>

    <h2>הסגנון הרומנטי (בערך 1820-1910)</h2>
    <h3>מאפיינים מרכזיים</h3>
    <ul>
        <li>**דגש על רגש וביטוי אישי:** חיפוש אחר עוצמה רגשית, דרמה, וביטוי סובייקטיבי של המלחין.</li>
        <li>**הרמוניה עשירה, כרומטית ומורכבת:** שימוש באקורדים מורחבים, דיסוננסים חריפים יותר ומעברים הרמוניים מפתיעים.</li>
        <li>**מלודרמטיות וליריות:** מלודיות אקספרסיביות, לעיתים ארוכות ולא סימטריות כמו בתקופה הקלאסית.</li>
        <li>**תזמור גדול ומגוון יותר:** הרחבת התזמורת, הוספת כלים חדשים (פיקולו, קונטרה-בסון, קרן אנגלית, טובה, כלי הקשה מגוונים), ושימוש מבריק בצבעי הכלים.</li>
        <li>**מגוון צורות:** לצד צורות קלאסיות שהורחבו (סימפוניה, סונטה), התפתחו צורות חדשות כמו הפואמה הסימפונית, יצירות קצרות לפסנתר (נוקטורן, פרלוד, אטיוד), שירים (ליד).</li>
        <li>**מוזיקה תוכניתית:** יצירות שמבוססות על סיפור, שיר, ציור או רעיון חוץ-מוזיקלי.</li>
        <li>**קצב וטמפו גמישים (רובאטו):** שינויים חופשיים יותר בטמפו להדגשת הביטוי.</li>
    </ul>
    <h3>מלחינים בולטים</h3>
    <p>פרדריק שופן, פרנץ ליסט, פיוטר איליץ' צ'ייקובסקי, יוהנס ברהמס, ריכרד ואגנר, ג'וזפה ורדי, הקטור ברליוז, רוברט שומאן, פרנץ שוברט (המאוחר).</p>
    <h3>דוגמאות שמיעתיות (סוגי יצירות)</h3>
    <p>פואמה סימפונית, אופרה רומנטית (גדולה), סימפוניה מאוחרת, קונצ'רטו ויצירות וירטואוזיות, שירים לפסנתר וקול (ליד), יצירות אופייניות לפסנתר סולו.</p>

    <h2>טבלת השוואה מסכמת</h2>
    <table>
        <tr>
            <th>מאפיין</th>
            <th>בארוק (כ-1600-1750)</th>
            <th>קלאסי (כ-1750-1820)</th>
            <th>רומנטי (כ-1820-1910)</th>
        </tr>
        <tr>
            <td>**מרקם**</td>
            <td>פוליפוניה (קונטרפונקט) דומיננטית</td>
            <td>הומופוניה דומיננטית (מלודיה + ליווי)</td>
            <td>מגוון, לרוב הומופוני עשיר או הטרופוני</td>
        </tr>
        <tr>
            <td>**מלודיה**</td>
            <td>לרוב ארוכה, זורמת, מורכבת, מנועתיות</td>
            <td>ברורה, קליטה, סימטרית (משפטים באורך 4 או 8 תיבות)</td>
            <td>לירית, אקספרסיבית, לעיתים ארוכה ולא סדירה, כרומטית</td>
        </tr>
        <tr>
            <td>**הרמוניה**</td>
            <td>פונקציונלית, ברורה, בס ממוספר</td>
            <td>ברורה, דיאטונית בעיקרה, קאדנצות מוגדרות</td>
            <td>עשירה, כרומטית, דיסוננסים נועזים, מודולציות תכופות</td>
        </tr>
        <tr>
            <td>**קצב / ריתמוס**</td>
            <td>מנועתי, דופק קבוע לאורך פרק</td>
            <td>ברור, מגוון, שינויים בתוך הפרק</td>
            <td>גמיש, רובאטו, שינויים קיצוניים בטמפו וקצב</td>
        </tr>
        <tr>
            <td>**כלי נגינה בולטים**</td>
            <td>צ'מבלו, עוגב, כלי קשת בארוקיים, חלילית, חצוצרות טבעיות</td>
            <td>פסנתר, תזמורת קלאסית (קשת, נשיפה מעץ, קרנות, טימפני)</td>
            <td>פסנתר, תזמורת גדולה (כלי נשיפה וכלי הקשה רבים), כלים וירטואוזיים (כינור, פסנתר)</td>
        </tr>
         <tr>
            <td>**מבנה**</td>
            <td>מגוון, צורות קטנות יותר, פרקים קצרים יותר (פוגה, סוויטה)</td>
            <td>ברור, פורמלי (צורת סונטה, סימפוניה, קונצ'רטו), מבנה גדול יותר</td>
            <td>מגוון (פואמה סימפונית, יצירות אופי), צורות קלאסיות מורחבות, חופש רב יותר</td>
        </tr>
         <tr>
            <td>**אווירה / רגש**</td>
            <td>"אפקט" אחיד לפרק/קטע, רטוריקה</td>
            <td>איזון, אצילות, קונטרסט בין נושאים</td>
            <td>עוצמה רגשית, דרמה, ליריות, אינדיבידואליזם, חיבור לטבע ולסיפורים</td>
        </tr>
    </table>

    <h2>טיפים להקשבה אקטיבית וזיהוי סגנונות</h2>
    <ul>
        <li>**הקשיבו למרקם:** האם יש מלודיה אחת בולטת עם ליווי (הומופוניה), או כמה קווים מלודיים שווי חשיבות שמשתלבים זה בזה (פוליפוניה)? פוליפוניה עשירה מרמזת על בארוק.</li>
        <li>**שימו לב למלודיה:** האם היא קליטה, סימטרית ומאוזנת (קלאסי)? האם היא ארוכה, זורמת ומנועתיות (בארוק), או אקספרסיבית, כרומטית ודרמטית (רומנטי)?</li>
        <li>**הקשיבו להרמוניה:** האם היא נשמעת "פשוטה" וברורה (קלאסי)? האם היא עשירה, כרומטית וכוללת אקורדים "צבעוניים" או דיסוננסים חריפים (רומנטי)?</li>
        <li>**שימו לב לקצב:** האם יש דופק קבוע ומנועתי (בארוק)? האם הקצב משתנה וגמיש, עם האצות והאטות (רומנטי)?</li>
        <li>**זהו כלי נגינה בולטים:** האם אתם שומעים צ'מבלו? (בארוק). האם אתם שומעים פסנתר ככלי מרכזי, או תזמורת "סטנדרטית" יחסית (קלאסי)? האם התזמורת נשמעת גדולה מאוד ועשירה בצבעים, עם כלי נשיפה ממתכת רבים וכלי הקשה מגוונים? (רומנטי).</li>
        <li>**התרשמו מהאווירה הכללית:** האם היצירה נשמעת מתונה, ברורה ומאוזנת (קלאסי)? האם היא מנועתיות ומלאת קישוטים (בארוק)? האם היא נשמעת דרמטית, רגשית, "סוערת" או חולמנית (רומנטי)?</li>
    </ul>
</div>

<style>
    :root {
        --primary-color: #007bff; /* Blue */
        --secondary-color: #28a745; /* Green */
        --tertiary-color: #6c757d; /* Gray */
        --background-light: #f8f9fa;
        --surface-light: #ffffff;
        --border-color: #dee2e6;
        --text-color: #343a40;
        --correct-color: #28a745;
        --incorrect-color: #dc3545;
        --shadow: rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Arial Hebrew', 'David', sans-serif;
        direction: rtl;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-light);
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #0056b3; /* Darker primary */
        text-align: center;
        margin-bottom: 1em;
    }

    h1 {
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
    }

    #app, .explanation-box {
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        background-color: var(--surface-light);
        border-radius: 12px;
        box-shadow: 0 4px 15px var(--shadow);
        text-align: center;
        opacity: 1;
        transform: translateY(0);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    #app.fade-out {
        opacity: 0;
        transform: translateY(20px);
    }

    #game-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 1px solid var(--border-color);
    }

    #score, #progress {
        font-size: 1.3em;
        font-weight: bold;
        color: var(--primary-color);
    }

    #score {
        animation: scoreUpdate 0.3s ease-out;
    }

    @keyframes scoreUpdate {
        0% { transform: scale(1); color: var(--primary-color); }
        50% { transform: scale(1.1); color: var(--secondary-color); }
        100% { transform: scale(1); color: var(--primary-color); }
    }


    #question-area {
        margin-bottom: 30px;
        min-height: 150px; /* Reserve space */
    }

    #audio-control {
        margin-bottom: 20px;
        min-height: 45px; /* Prevent jump when status appears */
    }

    #play-button, .control-button {
        padding: 12px 25px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
        font-family: inherit;
    }

    #play-button {
         background-color: var(--secondary-color);
         color: white;
         box-shadow: 0 2px 5px rgba(40, 167, 69, 0.3);
    }
    #play-button:hover:not(:disabled) {
        background-color: #218838;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.4);
    }
    #play-button:active:not(:disabled) {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(40, 167, 69, 0.3);
    }


    #play-button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
        background-color: var(--tertiary-color);
        box-shadow: none;
    }

    .status-message {
        font-size: 1.1em;
        color: var(--tertiary-color);
        margin-top: 10px;
        animation: fadeIn 0.5s ease-out;
    }


    .interactive-area {
        animation: fadeIn 0.8s ease-out;
    }

    .instruction {
        font-size: 1.1em;
        margin-bottom: 15px;
        color: var(--text-color);
    }

    .button-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px; /* Space between buttons */
    }

    #choices button {
        flex-grow: 1; /* Allow buttons to grow */
        max-width: 150px; /* Limit max width */
        padding: 12px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3);
        font-family: inherit;
    }

    #choices button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.4);
    }
    #choices button:active:not(:disabled) {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3);
    }

    #choices button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }

    #choices button.selected {
        box-shadow: 0 0 0 3px var(--primary-color), 0 0 0 6px rgba(0, 123, 255, 0.3); /* Highlight selected */
    }
    #choices button.correct-answer {
         background-color: var(--correct-color);
         box-shadow: 0 2px 5px rgba(40, 167, 69, 0.3);
    }
    #choices button.incorrect-answer {
        background-color: var(--incorrect-color);
         box-shadow: 0 2px 5px rgba(220, 53, 69, 0.3);
    }


    .feedback-message {
        margin-top: 20px;
        padding: 15px;
        font-size: 1.2em;
        min-height: 1.5em; /* Prevent layout shift */
        border-radius: 8px;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    .feedback-message.show {
        opacity: 1;
        transform: translateY(0);
    }

    .feedback-message.correct {
        color: var(--correct-color);
        border: 1px solid var(--correct-color);
        background-color: #d4edda; /* Light green */
    }

    .feedback-message.incorrect {
        color: var(--incorrect-color);
        border: 1px solid var(--incorrect-color);
        background-color: #f8d7da; /* Light red */
    }

    .info-box {
        margin-top: 25px;
        padding: 20px;
        border-top: 1px solid var(--border-color);
        text-align: right;
        font-size: 0.95em;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    .info-box.show {
        opacity: 1;
        transform: translateY(0);
    }

     .info-box h3 {
        text-align: right;
        margin-top: 0;
        margin-bottom: 15px;
        color: #0056b3; /* Darker primary */
        font-size: 1.1em;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
     }

     .info-box p {
        margin: 8px 0;
        line-height: 1.5;
     }

     .info-box strong {
        color: #555;
     }

    .control-button {
        display: inline-block; /* Ensure padding works */
        margin-top: 25px;
    }

    .control-button.primary {
        background-color: var(--primary-color);
        color: white;
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3);
    }
     .control-button.primary:hover {
         background-color: #0056b3;
         transform: translateY(-1px);
         box-shadow: 0 4px 8px rgba(0, 123, 255, 0.4);
     }

    .control-button.secondary {
        background-color: var(--secondary-color);
        color: white;
         box-shadow: 0 2px 5px rgba(40, 167, 69, 0.3);
    }
     .control-button.secondary:hover {
        background-color: #218838;
        transform: translateY(-1px);
         box-shadow: 0 4px 8px rgba(40, 167, 69, 0.4);
     }

     .control-button.tertiary {
        background-color: var(--tertiary-color);
        color: white;
         box-shadow: 0 2px 5px rgba(108, 117, 125, 0.3);
        margin: 20px auto; /* Center the toggle button */
        display: block; /* Make it a block element to center */
        max-width: 300px;
     }
      .control-button.tertiary:hover {
         background-color: #5a6268;
         transform: translateY(-1px);
         box-shadow: 0 4px 8px rgba(108, 117, 125, 0.4);
      }


    #end-game {
        margin-top: 40px;
        padding: 30px;
        border-top: 1px solid var(--border-color);
        background-color: #e9ecef; /* Light gray */
        border-radius: 12px;
        box-shadow: 0 4px 15px var(--shadow);
        text-align: center;
        opacity: 0;
        transform: scale(0.9);
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }

    #end-game.show {
         opacity: 1;
         transform: scale(1);
    }

    #end-game h2 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    .final-score-text {
        font-size: 1.5em;
        font-weight: bold;
        color: var(--secondary-color);
        margin-bottom: 20px;
    }

    /* Explanation Section Styling */
    .explanation-box h2, .explanation-box h3 {
         text-align: right;
         color: #0056b3;
         margin-bottom: 0.8em;
    }
    .explanation-box h2 {
        border-bottom: 1px solid #dee2e6;
        padding-bottom: 5px;
        margin-top: 20px;
    }
     .explanation-box h3 {
        color: #555;
        margin-top: 15px;
     }

    .explanation-box p {
        line-height: 1.7;
        margin-bottom: 1em;
        text-align: right;
    }

    .explanation-box ul {
        text-align: right;
        padding-right: 20px;
        margin-bottom: 1em;
    }

     .explanation-box ul li {
        margin-bottom: 0.5em;
     }


    .explanation-box table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        overflow: hidden; /* Ensures border-radius is applied */
    }

    .explanation-box th, .explanation-box td {
        border: 1px solid var(--border-color);
        padding: 12px;
        text-align: right;
    }

    .explanation-box th {
        background-color: #e9ecef; /* Light gray header */
        font-weight: bold;
        color: var(--text-color);
    }

    .explanation-box tr:nth-child(even) {
        background-color: #f8f9fa; /* Alternate row color */
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .show-animation {
        animation: slideUp 0.5s ease-out forwards;
    }


</style>

<script>
    const questions = [
        {
            audioSrc: 'https://www.dropbox.com/scl/fi/t37p2829e06k77v89e6t0/Bach-Brandenburg-Concerto-No3-1st-Mvt-excerpt.mp3?rlkey=c957v43j26m779o8c3319e71j&raw=1',
            correctStyle: 'בארוק',
            title: 'קונצ\'רטו ברנדנבורג מס\' 3, פרק ראשון (קטע)',
            composer: 'יוהאן סבסטיאן באך',
            year: 'תקופת הבארוק (~1721)',
            hint: 'הקשיבו לריבוי הקווים המלודיים הנשזרים זה בזה (קונטרפונקט) ולדופק הריתמי המנועתי הקבוע והחזק.'
        },
        {
            audioSrc: 'https://www.dropbox.com/scl/fi/w9o3j23v01387r6b67jkw/Mozart-Symphony-No40-1st-Mvt-excerpt.mp3?rlkey=v8c6m52lkmw6m9v4g2w9c26r6&raw=1',
            correctStyle: 'קלאסי',
            title: 'סימפוניה מס\' 40 ברה מינור, פרק ראשון (קטע)',
            composer: 'וולפגנג אמדאוס מוצרט',
            year: 'תקופת הקלאסיקה (1788)',
            hint: 'המלודיה ברורה וקליטה, המרקם לרוב הומופוני עם ליווי ברור, והמבנה מאוזן עם משפטים קצרים ומוגדרים.'
        },
        {
            audioSrc: 'https://www.dropbox.com/scl/fi/5v8f507t202v1u8v04z20/Chopin-Nocturne-Op9No2-excerpt.mp3?rlkey=2x0v7o9u6o6u9t8c7n5d6b4a3&raw=1',
            correctStyle: 'רומנטי',
            title: 'נוקטורן במי במול מז\'ור, אופ. 9 מס\' 2 (קטע)',
            composer: 'פרדריק שופן',
            year: 'תקופת הרומנטיקה (1830-1832)',
            hint: 'הקשיבו למלודיה הלירית והאקספרסיבית מאוד, להרמוניה העשירה והכרומטית ולשימוש בפסנתר ככלי מרכזי.'
        },
        {
            audioSrc: 'https://www.dropbox.com/scl/fi/4y2e1w6l3t4v1w9p8j0r7/Vivaldi-Four-Seasons-Spring-1st-Mvt-excerpt.mp3?rlkey=4q6y8e7v2w0o1i5d3c9a8f7b6&raw=1',
            correctStyle: 'בארוק',
            title: 'ארבע העונות: "האביב", פרק ראשון (קטע)',
            composer: 'אנטוניו ויולדי',
            year: 'תקופת הבארוק (~1721)',
            hint: 'מאופיין בתיבת קצב יציבה מאוד, מוטיבים שחוזרים על עצמם (ריטורנלו) וירטואוזיות סולו כינורית האופיינית לקונצ\'רטו הבארוקי.'
        },
        {
            audioSrc: 'https://www.dropbox.com/scl/fi/r2a0v8q3d2w1p0o9u7y6e/Haydn-Symphony-No94-Surprise-2nd-Mvt-excerpt.mp3?rlkey=8i7j6h5g4f3e2d1c0b9a8z&raw=1',
            correctStyle: 'קלאסי',
            title: 'סימפוניה מס\' 94 "ההפתעה", פרק שני (קטע)',
            composer: 'יוזף היידן',
            year: 'תקופת הקלאסיקה (1791)',
            hint: 'מלודיה פשוטה וקליטה, מבנה של וריאציות על נושא, ומרקם הומופוני ברור. יש רגע "הפתעה" קלאסי באמצע.'
        },
        {
            audioSrc: 'https://www.dropbox.com/scl/fi/l0x9c8v7u6t5r4p3o2i1y/Tchaikovsky-Swan-Lake-Scene-excerpt.mp3?rlkey=0k1j2i3h4g5f6e7d8c9b0a&raw=1',
            correctStyle: 'רומנטי',
            title: 'אגם הברבורים, סצנה (קטע)',
            composer: 'פיוטר איליץ\' צ\'ייקובסקי',
            year: 'תקופת הרומנטיקה (1875-1876)',
            hint: 'הקשיבו לתזמור העשיר והדרמטי, השימוש הנרחב בכלי נשיפה ממתכת ולביטוי הרגשי העוצמתי שיוצר אווירה תיאטרלית.'
        },
         {
            audioSrc: 'https://www.dropbox.com/scl/fi/f8d7c6b5a4z3y2x1w0v9u/Brahms-Hungarian-Dance-No5-excerpt.mp3?rlkey=z9y8x7w6v5u4t3s2r1q0p&raw=1',
            correctStyle: 'רומנטי',
            title: 'ריקוד הונגרי מס\' 5 (קטע)',
            composer: 'יוהנס ברהמס',
            year: 'תקופת הרומנטיקה (1868-1869)',
            hint: 'מאופיין בקצב נמרץ ומשתנה, השפעות פולקלוריות, דינמיקה משתנה מאוד וצבעי תזמור עשירים האופייניים למוזיקה רומנטית לאומית.'
        }
    ];

    let shuffledQuestions = [];
    let currentQuestionIndex = 0;
    let score = 0;
    const totalQuestions = 5; // Play a fixed number of questions

    // Get elements
    const app = document.getElementById('app');
    const audioPlayer = document.getElementById('audio-player');
    const playButton = document.getElementById('play-button');
    const audioStatusDiv = document.getElementById('audio-status');
    const choicesDiv = document.getElementById('choices');
    const feedbackDiv = document.getElementById('feedback');
    const scoreDiv = document.getElementById('score');
    const progressDiv = document.getElementById('progress');
    const questionInfoDiv = document.getElementById('question-info');
    const pieceTitleSpan = document.getElementById('piece-title');
    const composerSpan = document.getElementById('composer');
    const yearSpan = document.getElementById('year');
    const correctStyleSpan = document.getElementById('correct-style');
    const styleHintSpan = document.getElementById('style-hint');
    const styleButtons = document.querySelectorAll('.style-button');
    const nextButton = document.getElementById('next-button');
    const endGameDiv = document.getElementById('end-game');
    const finalScoreSpan = document.getElementById('final-score');
    const totalQuestionsEndSpan = document.getElementById('total-questions-end');
    const restartButton = document.getElementById('restart-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Utility function to shuffle an array
    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
        return array;
    }

    // Function to hide elements with animation
    function hideElement(el) {
        el.classList.remove('show-animation');
        // Use a slight delay before hiding completely to allow animation to start (if needed)
        // For simple opacity/transform, hiding immediately might be fine.
        el.style.display = 'none';
    }

     // Function to show elements with animation
    function showElement(el) {
        el.style.display = 'block';
        // Force reflow to allow transition to work when changing from display: none
        el.offsetWidth;
        el.classList.add('show-animation');
    }


    function loadQuestion() {
        // Reset states
        hideElement(choicesDiv);
        hideElement(feedbackDiv);
        hideElement(questionInfoDiv);
        hideElement(nextButton);
        audioStatusDiv.style.display = 'none';
        playButton.style.display = 'block'; // Show play button
        playButton.disabled = true;
        feedbackDiv.textContent = ''; // Clear previous feedback
        feedbackDiv.className = 'feedback-message'; // Reset feedback classes


        if (currentQuestionIndex < totalQuestions && currentQuestionIndex < shuffledQuestions.length) {
            const question = shuffledQuestions[currentQuestionIndex];
            audioPlayer.src = question.audioSrc;
            audioPlayer.load(); // Preload audio

            // Show loading status
            playButton.style.display = 'none';
            audioStatusDiv.style.display = 'block';
             audioStatusDiv.textContent = 'טוען קטע...';
             audioStatusDiv.className = 'status-message'; // Reset status class

            styleButtons.forEach(button => {
                button.disabled = false;
                button.classList.remove('selected', 'correct-answer', 'incorrect-answer');
                button.style.opacity = 1; // Reset opacity
                button.style.transform = 'none'; // Reset transform
                button.style.boxShadow = ''; // Reset shadow
            });

            // Update progress display
            progressDiv.textContent = `שאלה ${currentQuestionIndex + 1} מתוך ${totalQuestions}`;

            audioPlayer.oncanplaythrough = () => {
                 playButton.disabled = false;
                 audioStatusDiv.style.display = 'none';
                 playButton.style.display = 'block';
                 playButton.textContent = 'האזנה לקטע'; // Reset text after loading
            };
             audioPlayer.onerror = (e) => {
                 console.error("Audio loading error", e);
                 audioStatusDiv.textContent = 'שגיאה בטעינת קטע האודיו.';
                 audioStatusDiv.className = 'status-message incorrect';
                 playButton.style.display = 'block'; // Show button but keep disabled
                 playButton.disabled = true;
                 playButton.textContent = 'שגיאה';
             }


        } else {
            endGame();
        }
    }

    function playAudio() {
        playButton.disabled = true;
        playButton.textContent = 'מנגן...'; // Indicate playing state
        audioPlayer.play().catch(error => {
             console.error("Error playing audio:", error);
             feedbackDiv.textContent = 'שגיאה בהפעלת האודיו. נסה שוב.';
             feedbackDiv.className = 'feedback-message incorrect show';
             playButton.disabled = false; // Re-enable play if playback fails immediately
             playButton.textContent = 'האזנה לקטע'; // Reset text
        });

        audioPlayer.onended = () => {
            playButton.textContent = 'האזנה לקטע שוב'; // Change text for replay
            playButton.disabled = false; // Allow replay
            showElement(choicesDiv); // Show choices after listening
        };
    }

    function checkAnswer(selectedStyle, clickedButton) {
        // Prevent multiple clicks
        styleButtons.forEach(button => button.disabled = true);

        const question = shuffledQuestions[currentQuestionIndex];
        const isCorrect = selectedStyle === question.correctStyle;

        // Highlight selected and correct buttons
        styleButtons.forEach(button => {
             if (button === clickedButton) {
                 button.classList.add('selected');
             } else {
                 button.style.opacity = 0.6; // Dim unselected
             }
             if (button.getAttribute('data-style') === question.correctStyle) {
                 button.classList.add('correct-answer'); // Highlight correct
             } else if (button === clickedButton && !isCorrect) {
                 button.classList.add('incorrect-answer'); // Highlight incorrect choice
             }
        });


        if (isCorrect) {
            score++;
            feedbackDiv.textContent = 'מדהים! זיהוי מדויק!';
            feedbackDiv.className = 'feedback-message correct';
             scoreDiv.classList.add('score-update'); // Trigger animation
             scoreDiv.addEventListener('animationend', () => {
                 scoreDiv.classList.remove('score-update');
             }, { once: true });

        } else {
            feedbackDiv.textContent = `לא נורא! זו הזדמנות ללמוד.`;
            feedbackDiv.className = 'feedback-message incorrect';
        }

        // Show feedback and info
        showElement(feedbackDiv);
        showElement(questionInfoDiv);

        // Display question info
        pieceTitleSpan.textContent = question.title;
        composerSpan.textContent = question.composer;
        yearSpan.textContent = question.year;
        correctStyleSpan.textContent = question.correctStyle;
        styleHintSpan.textContent = question.hint;

        // Update score display (will be animated by CSS class)
        scoreDiv.textContent = `ניקוד: ${score} / ${totalQuestions}`;

        // Show next button after a slight delay
        setTimeout(() => {
             showElement(nextButton);
        }, 500); // Delay matches feedback animation
    }

    function nextQuestion() {
        currentQuestionIndex++;
        loadQuestion();
    }

    function endGame() {
        app.classList.add('fade-out'); // Add fade out animation class
        // Wait for fade out before showing end screen
        setTimeout(() => {
            app.style.display = 'none'; // Hide app
            endGameDiv.style.display = 'block'; // Show end game screen
             // Trigger show animation for end game
            endGameDiv.classList.add('show');

            finalScoreSpan.textContent = score;
            totalQuestionsEndSpan.textContent = totalQuestions;
        }, 500); // Match app fade-out duration
    }

    function resetGame() {
        score = 0;
        currentQuestionIndex = 0;
        shuffledQuestions = shuffleArray([...questions]).slice(0, totalQuestions); // Shuffle and take the first N
        scoreDiv.textContent = `ניקוד: ${score} / ${totalQuestions}`; // Set initial score display
        endGameDiv.classList.remove('show'); // Remove show class for potential animation on next end
        endGameDiv.style.display = 'none'; // Hide end screen
        app.style.display = 'block'; // Show app
        app.classList.remove('fade-out'); // Remove fade out class
        loadQuestion();
    }

    // Event Listeners
    playButton.addEventListener('click', playAudio);

    styleButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            checkAnswer(event.target.getAttribute('data-style'), event.target);
        });
    });

    nextButton.addEventListener('click', nextQuestion);
    restartButton.addEventListener('click', resetGame);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        if (isHidden) {
            explanationDiv.style.display = 'block';
             // Optional: Add show animation class if desired, but might conflict with display:block transition
            // explanationDiv.classList.add('show-animation');
            toggleExplanationButton.textContent = 'הסתר הסבר על הסגנונות';
        } else {
             // Optional: Add hide animation class before setting display:none
             // explanationDiv.classList.remove('show-animation');
             // Maybe use a timeout if using hide animation class
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג/הסתר הסבר על הסגנונות';
        }
    });

    // Initial game start
    resetGame();

</script>