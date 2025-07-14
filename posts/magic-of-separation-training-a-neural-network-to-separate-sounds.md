---
title: "קסם ההפרדה: צלילה עמוקה אל תוך רשתות עצביות המבודדות קולות"
english_slug: magic-of-separation-training-a-neural-network-to-separate-sounds
category: "טכנולוגיה / מדעי המחשב"
tags: [רשתות עצביות, למידת מכונה, עיבוד אותות, אודיו, בינה מלאכותית]
---
# קסם ההפרדה: צלילה עמוקה אל תוך רשתות עצביות המבודדות קולות

נסו לדמיין: אתם בלב קונצרט סוער, מנסים לבודד רק את צליל הכינור הראשי מתוך בליל הצלילים העשיר של התזמורת כולה. או אולי בבית קפה רועש, מנסים להקשיב לשיחה חשובה כשלצידכם נשמעות צפירות, צחקוקים ורעש כלי מטבח. האוזן האנושית, פלא טכנולוגי בפני עצמו, מצליחה לעשות זאת בקלות מדהימה. אך עבור מחשבים, זו הייתה עד לא מזמן משימה כמעט בלתי אפשרית.

ברוכים הבאים לעולם המרתק של הפרדת מקורות קול (Source Separation) – תחום פורץ דרך שבו רשתות עצביות מאומנות לבצע את הקסם הזה בדיוק! בואו נתנסה בסימולציה כדי להבין איך זה עובד.

<div class="app-container">
    <h2>מעבד הסאונד העצבי: סימולטור אימון</h2>

    <div class="controls-panel">
        <div class="control-group">
            <label for="audio-source">האזנה לקובץ המעורב המקורי:</label>
            <audio controls src="mix.mp3" id="audio-source">
                המכשיר שלך אינו תומך בהשמעת אודיו.
            </audio>
             <small>זהו הקובץ שאיתו נעבוד, המכיל מספר מקורות צליל מעורבבים.</small>
        </div>

        <div class="control-group">
            <label for="target-source">מאיזה קול נרצה לבודד את שאר הצלילים?</label>
            <select id="target-source">
                <option value="vocals">שירה (ווקאל)</option>
                <option value="instrument">כלי נגינה</option>
            </select>
             <small>בחרו את ה"מטרה" של הרשת העצבית לאימון הנוכחי.</small>
        </div>

        <div class="control-group">
            <label for="training-time">משך ה"אימון" של הרשת (כמה סבלנות יש לנו?)</label>
            <input type="range" id="training-time" min="10" max="200" value="80">
            <span id="training-time-value">80</span>
             <small>יותר זמן = יותר הזדמנויות לרשת ללמוד ולדייק.</small>
        </div>

        <div class="control-group">
            <label for="model-complexity">עומק הרשת העצבית (כמה "חכמה" היא תהיה?)</label>
            <input type="range" id="model-complexity" min="10" max="200" value="80">
            <span id="model-complexity-value">80</span>
             <small>רשת מורכבת יותר יכולה להתמודד עם אתגרים קשים יותר.</small>
        </div>

        <button id="train-button">הפעל את המעבד העצבי!</button>
    </div>

    <div class="training-visualization" id="training-visualization">
        <div id="training-status">מוכן להפעלת המעבד...</div>
        <div class="progress-bar-container">
            <div class="progress-bar" id="progress-bar"></div>
        </div>
        <div class="spectrogram-container">
             <div class="spectrogram-label">ניתוח תדרים בזמן אמת:</div>
            <div class="spectrogram" id="spectrogram-placeholder">
                <!-- Spectrogram bars will be generated/animated here -->
            </div>
        </div>
    </div>

    <div class="results" id="results">
        <h3>תוצאות העיבוד העצבי:</h3>
        <p>הנה מה שהרשת הצליחה לבודד עבורכם:</p>
         <audio controls id="audio-separated">
            המכשיר שלך אינו תומך בהשמעת אודיו.
        </audio>
         <p>הקובץ המעורב המקורי (להשוואה קלה):</p>
         <audio controls id="audio-original-results">
            המכשיר שלך אינו תומך בהשמעת אודיו.
        </audio>
        <div id="result-message" class="result-message"></div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">רוצה להבין לעומק את הקסם מאחורי הקלעים?</button>

<div id="explanation" class="explanation-hidden">
    <h2>הסבר מעמיק: הצלילה הטכנית מאחורי הפרדת מקורות קול</h2>

    <h3>מהי הפרדת מקורות קול (Source Separation) ולמה היא כל כך שימושית?</h3>
    הפרדת מקורות קול היא היכולת לבודד צליל ספציפי או קבוצת צלילים (כמו דיבור, כלי נגינה מסוים, או רעש רקע) מתוך תמהיל שבו מספר צלילים נשמעים בו זמנית. זהו תהליך קריטי שמשנה את האופן שבו אנו מתקשרים עם אודיו בעולם הדיגיטלי. דמיינו שיחות טלפון צלולות ללא רעשי רקע, עוזרים קוליים שמבינים אתכם גם כשיש המולה סביבכם, או מוזיקאים שיכולים לפרק שיר לערוצים נפרדים לרמיקסים ויצירות חדשות.

    <h3>האתגר הגדול: כל הצלילים מתערבבים לגמרי!</h3>
    כששני מקורות קול או יותר נשמעים יחד, גלי הקול שלהם מתחברים פיזית באוויר ויוצרים גל קול אחד מורכב, בתהליך שנקרא סופרפוזיציה. מבחינת המחשב, קובץ אודיו מעורב הוא בסך הכל רצף מספרים המייצג את עוצמת הלחץ הכוללת של הגל המאוחד בכל רגע. למחשב אין באופן טבעי "ידע" איזה חלק מהמספרים הללו הגיע מכל מקור מקורי. זה כמו לקבל שייק פירות ולנסות להפריד אותו בחזרה לתפוח, בננה ותותים מקוריים – המידע מעורבב עמוק.

    <h3>איך רשת עצבית "שומעת" צלילים? פוגשים את הספקטרוגרמה</h3>
    רשתות עצביות לא "שומעות" כמונו. הן מקבלות נתונים במספרים. כדי לעבד אודיו, הופכים אותו לרוב לייצוג ויזואלי-מספרי שנקרא ספקטרוגרמה. חשבו על ספקטרוגרמה כמעין "מפה" של הצליל לאורך זמן:
    *   **ציר אופקי:** זמן, המתקדם משמאל לימין.
    *   **ציר אנכי:** תדרים, מהנמוכים (בס) בתחתית ועד לגבוהים (טרבל) למעלה.
    *   **צבע/בהירות:** מייצגים את עוצמת (אמפליטודת) הצליל בתדר מסוים ובזמן מסוים.
    דפוסים שונים בספקטרוגרמה מאפיינים מקורות קול שונים – דיבור, מוזיקה, רעש – ולרשת עצבית יש יכולת פנומנלית ללמוד לזהות את הדפוסים הללו.

    <h3>הטכניקה העצבית: ללמוד ליצור "מסכות"</h3>
    אחת הגישות הנפוצות להפרדת קולות באמצעות רשתות עצביות היא למידת "מסכה" (Mask). הרשת מקבלת את הספקטרוגרמה של האודיו המעורב. מטרתה היא ללמוד ליצור "מסיכת בינארית" או "מסיכה רכה" עבור המקור שאותו היא מנסה לבודד.
    *   **מסיכה בינארית:** ערך 1 בנקודת זמן-תדר אומר "האנרגיה כאן שייכת למקור המבוקש", וערך 0 אומר "לא שייך".
    *   **מסיכה רכה:** ערך בין 0 ל-1 מציין את ההסתברות או את החלק היחסי של האנרגיה באותה נקודה ששייכת למקור המבוקש.
    לאחר שהרשת מפיקה את המסכה, מכפילים אותה (נקודה-נקודה) בספקטרוגרמה המקורית של התמהיל. התוצאה היא ספקטרוגרמה חדשה שמכילה רק את האנרגיה שזוהתה כשייכת למקור המבוקש, תוך סינון השאר. את הספקטרוגרמה ה"מסוננת" הזו ניתן להפוך חזרה לגל קול נשמע.

    <h3>אימון הרשת: תהליך ה"הקשבה" והלמידה</h3>
    כמו כל למידת מכונה, אימון רשת עצבית להפרדה מתבצע על ידי הצגת דוגמאות ו"תיקון" הטעויות שלה שוב ושוב:
    1.  **קלט:** מזינים לרשת את הספקטרוגרמה של האודיו המעורב. חשוב שבשלב האימון, יהיה לנו גם את גרסאות ה"אמת" הנפרדות של כל מקור (אלו נתונים שהרשת לעולם לא תראה בשימוש רגיל, רק לאימון).
    2.  **ניחוש ראשוני:** הרשת, בהתחלה באופן אקראי למדי, מפיקה מסכה (או ספקטרוגרמה משוערת) עבור המקור המבוקש.
    3.  **חישוב "הפסד" (Loss):** משווים את הפלט של הרשת לגרסת ה"אמת" של המקור המבוקש. מדד מתמטי (פונקציית הפסד) מחשב עד כמה הפלט רחוק מהמטרה. שגיאה גדולה = הפסד גדול.
    4.  **למידה ושיפור:** הרשת משתמשת באלגוריתם שנקרא Backpropagation כדי להתאים את המשקולות וההטיות (הפרמטרים הפנימיים שלה) בצורה כזו שתקטין את ההפסד בניסיון הבא.
    5.  **חוזרים על התהליך:** מיליוני פעמים, על מאות אלפי ואף מיליוני דוגמאות שונות של אודיו מעורב וגרסאות האמת שלהן. לאורך האימון, ההפסד יורד בהדרגה, והרשת משתפרת ביכולתה לבודד את המקור המבוקש.

    **משך האימון** (מספר האיטרציות או ה"אפוכים") קובע כמה הזדמנויות למידה הרשת מקבלת. אימון ארוך יותר בדרך כלל משפר את התוצאות, אך קיים סיכון ל"התאמת יתר" (Overfitting) – מצב שבו הרשת זוכרת את דוגמאות האימון בעל פה במקום ללמוד עקרונות כלליים.
    **עומק הרשת** (מורכבות המודל) קובע עד כמה הרשת מסוגלת ללמוד דפוסים מורכבים ועדינים בספקטרוגרמה. רשת עמוקה ומורכבת יותר יכולה תיאורטית לבצע הפרדה טובה יותר, אך היא דורשת הרבה יותר נתונים וזמן אימון, וגם היא רגישה יותר להתאמת יתר. יש למצוא את האיזון הנכון.

    <h3>הפרדת מקורות קול בשימוש יומיומי: רק קצה הקרחון</h3>
    הטכנולוגיה הזו כבר סביבנו ומשפרת את חיינו בדרכים רבות:
    -   **שיפור איכות שמע:** סינון רעשים בשיחות, בהקלטות ובפודקאסטים.
    -   **טכנולוגיות דיבור:** שיפור זיהוי דיבור בסביבות רועשות, הפעלת עוזרים קוליים.
    -   **תעשיית המוזיקה:** יצירת גרסאות קריוקי איכותיות, רמיקסים, שחזור הקלטות היסטוריות.
    -   **רפואה:** ניתוח צלילי גוף (לב, נשימה) תוך בידודם מרעשים.
    -   **אבטחה וניטור:** ניתוח הקלטות שמע ממצלמות אבטחה לזיהוי אירועים או דיבור.

    כפי שראיתם בסימולטור, היכולת להפריד קולות תלויה בגורמים רבים כמו משך האימון ומורכבות הרשת. ככל שהמודלים משתפרים והנתונים זמינים יותר, כך "קסם ההפרדה" הופך למציאות מדויקת ויעילה יותר.

</div>

<style>
    /* General body styling */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #eef2f7; /* Light background */
        direction: rtl; /* RTL for Hebrew */
        padding: 20px;
    }

    h1, h2, h3 {
        color: #1a2e4f; /* Dark blue headings */
        text-align: center; /* Center main headings */
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2.5em;
        border-bottom: 2px solid #4a90e2; /* Blue underline */
        padding-bottom: 10px;
    }

    h2 {
        font-size: 1.8em;
        margin-top: 30px;
        text-align: right; /* RTL align */
    }

     h3 {
        font-size: 1.4em;
        margin-top: 25px;
        color: #34495e; /* Slightly lighter blue */
        text-align: right; /* RTL align */
     }


    /* App Container Styling */
    .app-container {
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        background-color: #ffffff; /* White background for the app */
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Soft shadow */
        border: 1px solid #dcdcdc;
        text-align: right; /* RTL alignment */
    }

    .controls-panel {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #f8f9fa; /* Light grey background */
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }

    .control-group {
        margin-bottom: 20px;
        padding: 15px;
        border: 1px solid #dee2e6;
        border-radius: 6px;
        background-color: #fff;
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align labels/inputs to the right */
        transition: border-color 0.3s ease;
    }

    .control-group:focus-within {
         border-color: #007bff; /* Highlight on focus */
    }

    .control-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
        font-size: 1em;
    }

    .control-group small {
        display: block;
        margin-top: 5px;
        color: #6c757d;
        font-size: 0.85em;
    }


    .control-group audio,
    .control-group select,
    .control-group input[type="range"] {
        width: 100%;
        margin-top: 5px;
        padding: 8px; /* Added padding */
        border: 1px solid #ced4da;
        border-radius: 4px;
        box-sizing: border-box; /* Include padding/border in element's total width/height */
    }

    .control-group select {
         appearance: none; /* Remove default dropdown arrow */
         background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23343a40' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
         background-repeat: no-repeat;
         background-position: left 0.75rem center; /* Position arrow on the left for RTL */
         background-size: 16px 12px;
         padding-left: 2.5rem; /* Make space for the arrow */
         cursor: pointer;
    }


    .control-group input[type="range"] {
        -webkit-appearance: none; /* Override default CSS for appearance */
        appearance: none;
        height: 8px;
        background: #e9ecef;
        border-radius: 5px;
        outline: none;
        margin: 10px 0;
        transition: opacity .2s;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        transition: background 0.3s ease, transform 0.1s ease;
    }

     .control-group input[type="range"]::-webkit-slider-thumb:hover {
         background: #0056b3;
         transform: scale(1.1);
     }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
         transition: background 0.3s ease;
    }

     .control-group input[type="range"]::-moz-range-thumb:hover {
         background: #0056b3;
     }


    .control-group span {
        align-self: flex-start; /* Align value to the left for RTL, next to the slider */
        font-weight: normal;
        font-size: 0.9em;
        color: #555;
        margin-top: -15px; /* Adjust position relative to slider */
        padding-right: 5px; /* Add space to the right */
    }

    #train-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #28a745; /* Green for Go */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.2em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        margin-top: 20px;
    }

    #train-button:hover:not(:disabled) {
        background-color: #218838;
        transform: translateY(-2px); /* Lift effect */
    }

    #train-button:active:not(:disabled) {
         background-color: #1e7e34;
         transform: translateY(0); /* Press effect */
    }


    #train-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        transform: none;
    }

    /* Training Visualization Styling */
    .training-visualization {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #e9ecef; /* Light grey background */
        min-height: 200px; /* Ensure space */
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    #training-status {
        font-size: 1.2em;
        margin-bottom: 15px;
        color: #0056b3; /* Blue color */
        font-weight: bold;
    }

    .progress-bar-container {
        width: 90%;
        height: 15px;
        background-color: #ccc;
        border-radius: 8px;
        margin-bottom: 20px;
        overflow: hidden;
        display: none; /* Hidden by default */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
    }

    .progress-bar {
        height: 100%;
        width: 0%;
        background-color: #28a745; /* Green */
        border-radius: 8px;
        transition: width linear; /* Use linear for a constant animation speed */
        background: linear-gradient(to right, #28a745, #1e7e34); /* Gradient */
    }

    .spectrogram-container {
        width: 90%;
        margin-top: 10px;
        opacity: 0; /* Hidden initially */
        transition: opacity 0.5s ease;
    }

    .spectrogram-label {
        text-align: right; /* Align label right */
        font-size: 0.9em;
        color: #555;
        margin-bottom: 5px;
    }

    .spectrogram {
        display: flex;
        justify-content: space-between;
        align-items: flex-end; /* Bars grow upwards */
        width: 100%;
        height: 80px; /* Taller spectrogram */
        background: linear-gradient(to bottom, #f0f0f0, #ffffff); /* Soft gradient background */
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 5px;
        box-sizing: border-box;
        overflow: hidden; /* In case bars exceed height */
    }

     .spectrogram-bar {
        flex-grow: 1;
        margin: 0 1px;
        background-color: #007bff; /* Blue */
        width: calc(100% / 50); /* Distribute bars evenly (assuming 50 bars initially) */
        transition: height 0.1s linear, background-color 0.3s ease; /* Faster height change, smooth color */
        min-width: 1px; /* Prevent collapse */
     }

    /* Results Styling */
    .results {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #cce5ff; /* Light blue border */
        border-radius: 8px;
        background-color: #eaf4ff; /* Very light blue background */
        display: none; /* Hidden by default */
        text-align: right;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        animation: fadeIn 0.5s ease-out forwards; /* Add fade in animation */
    }

     @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
     }


    .results h3 {
        margin-top: 0;
        color: #004085; /* Darker blue heading */
        border-bottom: 1px solid #b8daff; /* Lighter blue underline */
        padding-bottom: 8px;
    }

    .results audio {
        width: 100%;
        margin-bottom: 15px;
        margin-top: 10px;
    }

    .results p {
        margin-bottom: 8px;
        font-weight: bold;
        color: #333;
    }

    .result-message {
        margin-top: 15px;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        color: #155724; /* Default green */
        background-color: #d4edda; /* Default light green */
        border-color: #c3e6cb; /* Default green border */
    }

     .result-message.excellent {
         color: #0f6640;
         background-color: #d4edda;
         border-color: #c3e6cb;
     }

     .result-message.good {
         color: #856404;
         background-color: #fff3cd;
         border-color: #ffeeba;
     }

     .result-message.poor {
         color: #721c24;
         background-color: #f8d7da;
         border-color: #f5c6cb;
     }


    /* Explanation Toggle Button */
    .toggle-button {
        display: block;
        width: 100%;
        max-width: 800px;
        margin: 20px auto; /* Center below the app */
        padding: 12px;
        background-color: #6c757d; /* Grey */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
        font-weight: bold;
    }

    .toggle-button:hover {
        background-color: #5a6268;
         transform: translateY(-2px);
    }
    .toggle-button:active {
         background-color: #545b62;
         transform: translateY(0);
    }


    /* Explanation Styling */
    .explanation-hidden {
        display: none;
    }

    #explanation {
         max-width: 800px;
         margin: 20px auto;
         padding: 30px;
         border: 1px solid #ddd;
         border-radius: 12px;
         background-color: #ffffff;
         text-align: right;
         box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
         animation: fadeIn 0.5s ease-out forwards; /* Add fade in animation */
    }

    #explanation h2, #explanation h3 {
        color: #1a2e4f;
        text-align: right;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

     #explanation p {
        margin-bottom: 18px;
        line-height: 1.7;
        color: #333;
     }

     #explanation strong {
         color: #1a2e4f;
     }

     #explanation ul {
         list-style-type: disc;
         padding-right: 20px;
         margin-bottom: 15px;
     }
     #explanation li {
         margin-bottom: 8px;
     }


    /* Responsive adjustments */
    @media (max-width: 600px) {
        body {
            padding: 10px;
        }
        .app-container, #explanation {
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
         .control-group {
             padding: 10px;
         }
         .control-group label {
             font-size: 0.95em;
         }
         .control-group small {
             font-size: 0.8em;
         }
         #train-button, .toggle-button {
             font-size: 1em;
             padding: 10px;
         }
         .spectrogram {
             height: 60px;
         }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const trainButton = document.getElementById('train-button');
        const trainingTimeInput = document.getElementById('training-time');
        const trainingTimeValueSpan = document.getElementById('training-time-value');
        const modelComplexityInput = document.getElementById('model-complexity');
        const modelComplexityValueSpan = document.getElementById('model-complexity-value');
        const trainingVisualization = document.getElementById('training-visualization');
        const trainingStatus = document.getElementById('training-status');
        const progressBarContainer = document.querySelector('.progress-bar-container');
        const progressBar = document.getElementById('progress-bar');
        const spectrogramPlaceholder = document.getElementById('spectrogram-placeholder');
        // Dynamically create spectrogram bars for better visual representation
        const numberOfSpectrogramBars = 60; // More bars for finer visual detail
        for(let i = 0; i < numberOfSpectrogramBars; i++) {
            const bar = document.createElement('div');
            bar.classList.add('spectrogram-bar');
            // Initial random height
            bar.style.height = `${Math.random() * 20 + 10}%`;
            spectrogramPlaceholder.appendChild(bar);
        }
        const spectrogramBars = spectrogramPlaceholder.querySelectorAll('.spectrogram-bar');


        const resultsDiv = document.getElementById('results');
        const audioSeparated = document.getElementById('audio-separated');
        const audioOriginalResults = document.getElementById('audio-original-results');
        const targetSourceSelect = document.getElementById('target-source');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const audioSourceOriginal = document.getElementById('audio-source'); // Original mix audio player
        const resultMessageDiv = document.getElementById('result-message');


        // Update value spans when sliders change + add subtle pulse animation
        function updateSliderValue(input, span) {
            span.textContent = input.value;
             // Add a class for animation
            span.classList.add('pulse');
            // Remove the class after animation ends
            span.addEventListener('animationend', () => {
                span.classList.remove('pulse');
            }, { once: true });
        }

        trainingTimeInput.addEventListener('input', () => updateSliderValue(trainingTimeInput, trainingTimeValueSpan));
        modelComplexityInput.addEventListener('input', () => updateSliderValue(modelComplexityInput, modelComplexityValueSpan));

         // Add pulse animation CSS rule dynamically or assume it's in the CSS block
        const styleSheet = document.styleSheets[0];
        const pulseKeyframes = `@keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); color: #007bff; }
            100% { transform: scale(1); color: #333; }
        }`;
        styleSheet.insertRule(pulseKeyframes, styleSheet.cssRules.length);
        const pulseRule = `.control-group span.pulse { animation: pulse 0.5s ease-out; }`;
         styleSheet.insertRule(pulseRule, styleSheet.cssRules.length);


        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('explanation-hidden');
            if (explanationDiv.classList.contains('explanation-hidden')) {
                toggleExplanationButton.textContent = 'רוצה להבין לעומק את הקסם מאחורי הקלעים?';
            } else {
                 toggleExplanationButton.textContent = 'הסתר הסבר מעמיק';
            }
        });

        // Simulate spectrogram change during "training"
        function animateSpectrogram(duration, targetSource, complexity) {
            spectrogramPlaceholder.parentElement.style.opacity = 1; // Show container
             spectrogramBars.forEach(bar => bar.style.transition = 'height 0.1s linear, background-color 0.3s ease'); // Set transition

            let startTime = null;
            const maxBaseHeight = 80; // Max height for animated bars
            const minBaseHeight = 10;
            const complexityFactor = complexity / 200; // Normalize complexity (10-200 range)
            const targetFrequencySim = targetSource === 'vocals' ? 0.6 : 0.4; // Simulate target frequency range (higher for vocals, lower for instrument)

            function animate(currentTime) {
                if (!startTime) startTime = currentTime;
                const elapsedTime = currentTime - startTime;
                const progress = Math.min(elapsedTime / duration, 1); // Progress from 0 to 1

                spectrogramBars.forEach((bar, index) => {
                    const barProgress = index / (numberOfSpectrogramBars - 1); // Progress along the bars

                    // Simulate frequency activity: base wave + target emphasis + learning effect
                    let baseHeight = (Math.sin(elapsedTime / 300 + index * 0.3) * 0.4 + 0.6) * (minBaseHeight + maxBaseHeight * 0.5); // Base wave
                    // Add emphasis around simulated target frequency
                    const targetEmphasis = Math.exp(-Math.pow((barProgress - targetFrequencySim) * 5, 2)); // Gaussian emphasis around target freq
                    baseHeight += targetEmphasis * (maxBaseHeight * 0.3) * (0.5 + complexityFactor); // Add weighted emphasis


                    // Simulate convergence: bars stabilize and become more distinct/representative of the target
                    const convergenceFactor = progress * (0.5 + complexityFactor); // Stronger convergence with more training/complexity
                    const finalPattern = (Math.sin(barProgress * Math.PI * 2 * (1 + complexityFactor)) * 0.3 + 0.7) * (minBaseHeight + maxBaseHeight * 0.8 * (0.5 + complexityFactor)); // Simulated final pattern based on complexity
                    let currentHeight = baseHeight * (1 - convergenceFactor) + finalPattern * convergenceFactor;


                    bar.style.height = `${Math.max(minBaseHeight, Math.min(maxBaseHeight, currentHeight))}%`; // Ensure height is within bounds

                    // Simulate color change indicating learning/focus
                    const initialHue = 220; // Blue
                    const targetHue = targetSource === 'vocals' ? 160 : 40; // Cyan for vocals, Orange for instrument
                    const currentHue = initialHue * (1 - progress) + targetHue * progress;
                    const saturation = 70 + progress * 20;
                    const lightness = 50 + progress * 10 * (1 + complexityFactor);

                    // Add intensity based on the bar's height relative to others or a threshold?
                    const intensity = Math.min(1, currentHeight / maxBaseHeight);
                    const colorLightness = 40 + intensity * 30; // Darker for low intensity, lighter for high
                    const colorSaturation = 60 + intensity * 30;

                     bar.style.backgroundColor = `hsl(${currentHue}, ${colorSaturation}%, ${colorLightness}%)`;
                });

                if (progress < 1) {
                    requestAnimationFrame(animate);
                } else {
                    // Final state after training - lock colors and shape
                     spectrogramBars.forEach(bar => bar.style.transition = ''); // Remove transition after final state
                }
            }
            requestAnimationFrame(animate);
        }


        // Train button click handler (simulated)
        trainButton.addEventListener('click', () => {
            const trainingTime = parseInt(trainingTimeInput.value, 10);
            const modelComplexity = parseInt(modelComplexityInput.value, 10);
            const targetSource = targetSourceSelect.value;

            // Disable controls during training
            trainButton.disabled = true;
            trainButton.textContent = 'מאמן... נא להמתין';
            trainingTimeInput.disabled = true;
            modelComplexityInput.disabled = true;
            targetSourceSelect.disabled = true;
            audioSourceOriginal.disabled = true; // Disable original player too


            // Reset results and visualization
            resultsDiv.style.display = 'none';
            progressBarContainer.style.display = 'block';
            progressBar.style.width = '0%';
            spectrogramPlaceholder.parentElement.style.opacity = 0; // Start fading out spectrogram container

            // Reset spectrogram bars to initial random state
             spectrogramBars.forEach(bar => {
                bar.style.backgroundColor = '#007bff'; // Reset color
                bar.style.height = `${Math.random() * 20 + 10}%`; // Random initial heights
            });


            trainingStatus.textContent = 'הרשת מקשיבה ומנתחת...';

            // Simulate training duration (e.g., 2-10 seconds based on time input)
            // Scale duration based on parameters: longer for more time, slightly longer for more complexity
            const simulationDuration = 1500 + (trainingTime * 30) + (modelComplexity * 10); // milliseconds

            // Start progress bar animation
            setTimeout(() => {
                // Use a small setTimeout to ensure the width reset happens before animation
                progressBar.style.transitionDuration = `${simulationDuration * 0.9 / 1000}s`; // Set transition duration
                progressBar.style.width = '100%';
            }, 50);

            // Start spectrogram animation
            // Animation duration should be slightly less than total simulation to end gracefully
            animateSpectrogram(simulationDuration * 0.9, targetSource, modelComplexity);


            // End of simulated training
            setTimeout(() => {
                trainingStatus.textContent = 'אימון הסתיים בהצלחה!';
                progressBarContainer.style.display = 'none';
                spectrogramPlaceholder.parentElement.style.opacity = 1; // Ensure spectrogram is visible at the end

                // Determine result quality based on parameters and target source
                let resultQuality = 'poor';
                let message = 'הרשת התקשתה לבודד את המקור. אולי נדרשים יותר אימון ומורכבות?';

                // Simple threshold logic (can be made more complex)
                if (trainingTime >= 150 && modelComplexity >= 150) {
                    resultQuality = 'excellent';
                    message = `וואו! הרשת ביצעה הפרדה מצוינת של ה${targetSource === 'vocals' ? 'שירה' : 'כלי הנגינה'}!`;
                } else if (trainingTime >= 100 && modelComplexity >= 100) {
                     resultQuality = 'good';
                     message = `הפרדה טובה של ה${targetSource === 'vocals' ? 'שירה' : 'כלי הנגינה'}. יש עדיין מעט רעש רקע.`;
                 } else if (trainingTime >= 70 || modelComplexity >= 70) {
                      resultQuality = 'fair'; // Intermediate level
                      message = `הפרדה חלקית של ה${targetSource === 'vocals' ? 'שירה' : 'כלי הנגינה'}. יש עוד מקום לשיפור.`;
                 }


                // Set simulated audio source based on target and quality
                let separatedAudioSrc = '';
                // Using placeholders - in a real app, this would be generated or selected from pre-rendered options
                if (targetSource === 'vocals') {
                    if (resultQuality === 'excellent') separatedAudioSrc = 'vocals_excellent.mp3'; // Assume these files exist
                    else if (resultQuality === 'good') separatedAudioSrc = 'vocals_good.mp3';
                    else if (resultQuality === 'fair') separatedAudioSrc = 'vocals_fair.mp3'; // Add fair option
                    else separatedAudioSrc = 'vocals_poor.mp3';
                } else { // instrument
                    if (resultQuality === 'excellent') separatedAudioSrc = 'instrument_excellent.mp3';
                    else if (resultQuality === 'good') separatedAudioSrc = 'instrument_good.mp3';
                    else if (resultQuality === 'fair') separatedAudioSrc = 'instrument_fair.mp3'; // Add fair option
                    else separatedAudioSrc = 'instrument_poor.mp3';
                }

                audioSeparated.src = separatedAudioSrc;
                audioOriginalResults.src = audioSourceOriginal.src; // Link original mix again for comparison

                // Show results section and message
                resultsDiv.style.display = 'block';
                resultMessageDiv.textContent = message;
                // Remove previous quality classes and add the new one
                resultMessageDiv.classList.remove('excellent', 'good', 'poor', 'fair');
                resultMessageDiv.classList.add(resultQuality);


                // Re-enable controls
                trainButton.disabled = false;
                trainButton.textContent = 'הפעל את המעבד העצבי!';
                trainingTimeInput.disabled = false;
                modelComplexityInput.disabled = false;
                targetSourceSelect.disabled = false;
                audioSourceOriginal.disabled = false;

            }, simulationDuration);
        });

         // Initial setup: ensure spectrogram bars have some random heights
         spectrogramBars.forEach(bar => {
             bar.style.height = `${Math.random() * 20 + 10}%`;
             bar.style.transition = 'none'; // Disable transitions initially
         });
         spectrogramPlaceholder.parentElement.style.opacity = 1; // Keep initial spectrogram visible


    });
</script>
---