---
title: "לאמן בינה מלאכותית להלחין: סימולטור מסע הלמידה של מודל מוזיקה"
english_slug: training-ai-to-compose-a-music-model-learning-journey-simulator
category: "טכנולוגיה / מדעי המחשב"
tags: [בינה מלאכותית, למידת מכונה, מוזיקה גנרטיבית, אימון מודלים, רשתות נוירונים, סימולציה]
---

# לאמן בינה מלאכותית להלחין: סימולטור מסע הלמידה של מודל מוזיקה

איך מכונה לומדת ליצור משהו יפה, אמנותי ורגשי כמו מוזיקה? דמיינו מודל AI שקשוב לאלפי שעות של מנגינות וצלילים, סופג את ההרמוניות, המקצבים והמבנים – ואז, לפתע, מתחיל להלחין בעצמו. הסימולטור הזה מאפשר לכם לצאת למסע אימון כזה, לראות איך פרמטרים שונים משפיעים על תהליך הלמידה של מודל מוזיקה וכיצד ה"שגיאות" שלו הולכות ומצטמצמות בדרכו להפוך למלחין דיגיטלי.

<div class="simulator-container">
    <div class="simulator-header">
         <h2>צאו למסע אימון מודל מוזיקה!</h2>
         <p>בחרו את סגנון המוזיקה ואת גודל הדאטה (כמה שירים המודל יקשיב להם) ומספר תקופות האימון (כמה פעמים הוא יעבור על כל הדאטה). לחצו "התחל אימון" וצפו בתהליך!</p>
    </div>

    <div class="controls">
        <div class="control-group">
            <label for="music-style">סגנון מוזיקלי:</label>
            <select id="music-style">
                <option value="classical">קלאסי (בסגנון באך)</option>
                <option value="jazz">ג'אז (בסגנון מיילס דיוויס)</option>
                <option value="rock">רוק (בסגנון לד זפלין)</option>
                <option value="electronic">אלקטרוני (בסגנון דאפט פאנק)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="data-size">גודל דאטה-סט (אלפי שירים):</label>
            <input type="number" id="data-size" value="5" min="1" max="20"> <span class="range-hint">(1-20)</span>
        </div>
        <div class="control-group">
            <label for="epochs">תקופות אימון (מעברים על הדאטה):</label>
            <input type="number" id="epochs" value="10" min="1" max="50"> <span class="range-hint">(1-50)</span>
        </div>
        <button id="start-training" class="action-button">התחל אימון מודל</button>
    </div>

    <div class="training-area">
        <h3>התקדמות וביצועי המודל:</h3>
        <div class="progress-section">
            <div class="progress-label">התקדמות אימון:</div>
            <div class="progress-bar-container">
                <div class="progress-bar"></div>
            </div>
             <span id="progress-text">0%</span>
        </div>

        <div class="loss-section">
            <div class="loss-label">שגיאת מודל (Loss):</div>
             <div class="loss-visualizer">
                 <span id="current-loss">...</span>
                 <div class="loss-graph">
                     <div class="loss-graph-bar"></div>
                 </div>
             </div>
            <small class="hint-text">(גובה הקו האדום מדמה את גודל השגיאה - קו נמוך יותר = מודל טוב יותר)</small>
        </div>

        <div class="music-output-section">
            <div class="output-label">מה המודל "מלחין" כעת (סימולציה):</div>
            <div id="generated-music-snippet" class="music-snippet">[...ממתין לתחילת האימון...]</div>
        </div>
    </div>
</div>

<style>
    /* כללי */
    .simulator-container {
        direction: rtl; /* לוודא כיווניות נכונה */
        text-align: right; /* לוודא יישור נכון */
        font-family: 'Arial', sans-serif; /* פונט כללי */
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* רקע נעים */
        border: 1px solid #b2ebf2;
        border-radius: 12px; /* פינות מעוגלות יותר */
        padding: 30px;
        margin-bottom: 30px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* צל עדין */
        overflow: hidden; /* למנוע גלישה של אנימציות */
    }

    .simulator-header h2 {
        color: #00796b; /* כותרת ראשית צבע ירוק-כחול */
        margin-top: 0;
        margin-bottom: 10px;
        text-align: center; /* ממורכז */
    }

     .simulator-header p {
         color: #333;
         text-align: center; /* ממורכז */
         margin-bottom: 25px;
         line-height: 1.5;
     }

    /* בקרה */
    .controls {
        display: flex; /* סידור באלמנטים בשורה */
        flex-wrap: wrap; /* גלישה לשורה חדשה במידת הצורך */
        gap: 20px; /* מרווח בין האלמנטים */
        margin-bottom: 25px;
        padding: 15px;
        background-color: #e0f2f7; /* רקע בהיר לבקרות */
        border-radius: 8px;
        border: 1px solid #b4dfe5;
        align-items: flex-end; /* יישור אלמנטים בחלק התחתון */
    }

    .control-group {
         flex: 1; /* מאפשר לכל קבוצת בקרה לתפוס מקום שווה */
         min-width: 220px; /* רוחב מינימלי למניעת התכווצות יתר */
         display: flex;
         flex-direction: column; /* סידור תווית ושדה קלט בטור */
    }

    .controls label {
        display: block; /* כל תווית בשורה משלה */
        margin-bottom: 8px; /* מרווח מתחת לתווית */
        font-weight: bold;
        color: #004d40; /* צבע כהה יותר לתוויות */
    }

     .controls input[type="number"],
     .controls select {
        padding: 10px 12px; /* ריפוד פנימי */
        border: 1px solid #b4dfe5;
        border-radius: 6px; /* פינות מעוגלות */
        font-size: 1em;
        box-sizing: border-box; /* גודל כולל כולל ריפוד וגבול */
        width: 100%; /* מתיחה לרוחב הקבוצה */
     }

     .range-hint {
         font-size: 0.85em;
         color: #555;
         margin-top: 4px;
         display: block; /* בשורה נפרדת */
     }

    .action-button {
        padding: 12px 25px;
        background-color: #00796b; /* צבע כפתור ראשי */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease; /* מעברי אנימציה */
        flex-shrink: 0; /* מונע מהכפתור להתכווץ */
    }

    .action-button:hover:not(:disabled) {
        background-color: #004d40; /* צבע כהה יותר בריחוף */
        transform: translateY(-2px); /* אפקט קפיצה קלה */
    }

     .action-button:active:not(:disabled) {
         transform: translateY(0); /* חוזר למקום בלחיצה */
     }

     .action-button:disabled {
         background-color: #ccc;
         cursor: not-allowed;
         box-shadow: none;
         transform: none;
     }

    /* אזור אימון */
    .training-area {
        margin-top: 25px;
        padding-top: 25px;
        border-top: 2px dashed #b4dfe5; /* גבול מפריד מעוצב */
        position: relative; /* עבור אנימציות פנימיות */
    }

    .training-area h3 {
        color: #00796b;
        margin-top: 0;
        margin-bottom: 20px;
    }

    /* אנימציית "אימון" */
    @keyframes pulse-border {
        0% { border-color: #b4dfe5; }
        50% { border-color: #00796b; }
        100% { border-color: #b4dfe5; }
    }

    .training-area.is-training {
         animation: pulse-border 2s infinite ease-in-out; /* אנימציה בזמן אימון */
         border-radius: 8px; /* לוודא שהאנימציה על מסגרת עגולה */
    }


    /* מד התקדמות */
    .progress-section {
         margin-bottom: 20px;
         display: flex;
         align-items: center; /* יישור רכיבים אנכית */
    }

     .progress-label {
         font-weight: bold;
         color: #333;
         min-width: 100px; /* רוחב קבוע לתווית */
     }

    .progress-bar-container {
        flex-grow: 1; /* מאפשר להתפשט לרוחב הפנוי */
        background-color: #e0e0e0;
        border-radius: 5px;
        overflow: hidden;
        height: 20px; /* גובה קבוע */
        margin: 0 15px; /* מרווח מצדדים */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2); /* צל פנימי למראה שקוע */
    }

    .progress-bar {
        height: 100%; /* גובה מלא של המכולה */
        width: 0%;
        background: linear-gradient(to right, #80cbc4, #00796b); /* גרדיאנט נעים */
        text-align: center;
        line-height: 20px; /* ממורכז אנכית */
        color: white;
        transition: width 0.7s ease-out; /* אנימציה חלקה וקצת מהירה יותר */
        font-size: 0.9em;
        font-weight: bold;
        display: flex; /* כדי למרכז את הטקסט אם היה בפנים */
        justify-content: center;
        align-items: center;
    }

     #progress-text {
         font-weight: bold;
         color: #004d40;
         min-width: 40px; /* רוחב קבוע למנוע שינוי בפריסה */
         text-align: left; /* יישור שמאלה */
     }

    /* הצגת שגיאה (Loss) */
    .loss-section {
        margin-top: 20px;
        margin-bottom: 20px;
        display: flex;
        align-items: flex-start; /* יישור למעלה */
    }

    .loss-label {
        font-weight: bold;
        color: #333;
        min-width: 100px; /* רוחב קבוע לתווית */
        padding-top: 5px; /* יישור עם הערך */
    }

    .loss-visualizer {
         display: flex;
         align-items: center;
         flex-grow: 1;
    }

     #current-loss {
         font-size: 1.2em;
         font-weight: bold;
         color: #d32f2f; /* צבע אדום לשגיאה */
         min-width: 80px; /* רוחב קבוע */
         text-align: left; /* יישור שמאלה */
     }

     .loss-graph {
         width: 150px; /* רוחב ויזואליזציית גרף */
         height: 60px; /* גובה מקסימלי לגרף */
         border-left: 1px solid #ccc;
         border-bottom: 1px solid #ccc;
         position: relative;
         margin-left: 15px; /* מרווח מהערך המספרי */
         overflow: hidden;
         background-color: #fff; /* רקע לבן לגרף */
         box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.1); /* צל פנימי עדין */
         border-radius: 4px;
     }

     .loss-graph-bar {
         position: absolute;
         bottom: 0;
         left: 0;
         width: 100%;
         background-color: #ef9a9a; /* אדום בהיר */
         height: 100%; /* מתחיל מהגובה המקסימלי */
         transition: height 0.7s ease-out, background-color 0.7s ease; /* אנימציית גובה וצבע */
     }

     .loss-graph-bar.low-loss {
         background-color: #a5d6a7; /* ירוק בהיר כשנמוך */
     }

     .hint-text {
         display: block; /* בשורה נפרדת */
         margin-top: 5px;
         color: #555;
         font-size: 0.8em;
         flex-basis: 100%; /* תופס את כל הרוחב למטה */
         text-align: right;
     }


    /* פלט מוזיקלי */
    .music-output-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px dashed #b4dfe5;
    }

    .output-label {
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }

     .music-snippet {
         min-height: 50px; /* גובה מינימלי */
         padding: 15px;
         background-color: #fff;
         border: 2px dashed #ccc;
         border-radius: 8px;
         font-style: italic;
         color: #555;
         transition: border-color 0.5s ease; /* אנימציית גבול */
         position: relative; /* עבור ספינר טעינה */
         overflow: hidden; /* למנוע גלישה של טקסט ארוך */
     }

     .music-snippet.is-training::after {
          content: '';
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          width: 20px;
          height: 20px;
          border: 3px solid #f3f3f3; /* Light grey */
          border-top: 3px solid #00796b; /* Blue */
          border-radius: 50%;
          animation: spin 1s linear infinite; /* אנימציית סיבוב */
     }

     @keyframes spin {
         0% { transform: translate(-50%, -50%) rotate(0deg); }
         100% { transform: translate(-50%, -50%) rotate(360deg); }
     }

     .music-snippet.is-training {
         color: transparent; /* להסתיר את הטקסט בזמן הטעינה */
         text-align: center; /* מרכז את הספינר */
     }


    /* כפתור הסבר */
    #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 30px auto; /* מרווח גדול יותר וממורכז */
        padding: 12px 25px;
        background-color: #607d8b; /* צבע אפור כחלחל */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: #455a64; /* צבע כהה יותר בריחוף */
        transform: translateY(-2px);
    }

    #toggle-explanation:active {
         transform: translateY(0);
    }

    /* הסבר מפורט */
    .explanation {
        display: none; /* Hidden by default */
        margin-top: 30px;
        padding-top: 25px;
        border-top: 2px dashed #ccc;
        background-color: #f5f5f5; /* רקע בהיר יותר להסבר */
        padding: 25px;
        border-radius: 8px;
        line-height: 1.7; /* מרווח שורות גדול יותר */
        color: #333;
    }

    .explanation h2, .explanation h3 {
        color: #004d40; /* צבע כהה יותר לכותרות הסבר */
        margin-top: 25px;
        margin-bottom: 12px;
        border-bottom: 1px solid #eee; /* קו תחתון עדין */
        padding-bottom: 5px;
    }

    .explanation p {
        margin-bottom: 18px;
    }

    .explanation ul {
        margin-bottom: 18px;
        padding-right: 25px; /* ריפוד בצד ימין לרשימות */
        list-style-type: disc; /* נקודות לרשימה */
    }

    .explanation li {
        margin-bottom: 10px;
    }

     .explanation li strong {
         color: #004d40; /* הדגשה בצבע כהה */
     }

     .explanation small {
         display: block; /* בשורה נפרדת */
         margin-top: 15px;
         color: #666;
         font-size: 0.9em;
         font-style: italic;
     }

</style>

<button id="toggle-explanation">הצג הסבר מפורט על התהליך</button>

<div class="explanation" id="detailed-explanation">
    <h2>מהי הלחנת מוזיקה גנרטיבית באמצעות AI? מסע יצירתי של מכונה</h2>
    <p>הלחנת מוזיקה גנרטיבית היא תחום מרתק המאפשר למחשבים ליצור יצירות מוזיקליות חדשות לחלוטין. במקום להיות רק כלי בידי מלחין אנושי, ה-AI הופך בעצמו ל"מלחין", הלומד להבין ולהפיק מוזיקה על בסיס דאטה קיים. הוא מנתח אלפי יצירות בסגנון מסוים – החל מיצירות מופת קלאסיות ועד ללהיטים עכשוויים – סופג את הכללים, הדפוסים, ההרמוניות והמבנים, ואז משתמש בידע הזה כדי לייצר מוזיקה מקורית שנאמנה לסגנון.</p>

    <h2>המוח מאחורי המוזיקה: סוגי מודלי AI</h2>
    <p>כמו שלמלחינים שונים יש גישות שונות, גם עולם מודלי המוזיקה הגנרטיבית מציע מגוון טכניקות:</p>
    <ul>
        <li>**שרשראות מרקוב (Markov Chains):** אלו מודלים פשוטים יחסית, הלומדים מהי ההסתברות שתו מסוים יופיע לאחר רצף תווים קודם. הם מצוינים ליצירת רצפים קצרים שנשמעים הגיוניים באופן מקומי, אך לרוב מתקשים לבנות מבנים מורכבים וארוכי טווח שיש להם "נרטיב" מוזיקלי שלם. המוזיקה שהם יוצרים יכולה להישמע מעט אקראית או חסרת כיוון.</li>
        <li>**רשתות נוירונים עמוקות (Deep Learning Models):** כאן נכנסים המודלים המורכבים יותר, כמו RNNs (Recurrent Neural Networks) ובעיקר **טרנספורמרים (Transformers)**. מודלים אלו מסוגלים ללמוד תלויות מורכבות וארוכות טווח לאורך יצירה שלמה. הם יכולים "לזכור" תמות מוזיקליות שהופיעו בתחילת הקטע ולהתייחס אליהן בהמשך. מודלי טרנספורמרים, הודות למנגנון ה-"Attention" שלהם, מסוגלים להתמקד בחלקים הרלוונטיים ביותר של היצירה הקודמת כדי לחזות את התו הבא, מה שמוביל ליצירת מוזיקה קוהרנטית ומרתקת יותר.</li>
    </ul>

    <h2>חדר הכושר של ה-AI: תהליך האימון</h2>
    <p>אימון מודל AI להלחנת מוזיקה הוא תהליך איטרטיבי של למידה מטעויות ושיפור מתמיד. דמיינו זאת כילד הלומד שפה - הוא מקשיב, מנסה לחקות, טועה, ומקבל משוב כדי לשפר את יכולותיו:</p>
    <ul>
        <li>**ה"ספרייה": נתוני אימון (Data-set):** הלב של כל מודל AI. בלי דאטה איכותי וגדול מספיק בסגנון הרצוי (אלפי קובצי MIDI או תמלולים של מוזיקה), המודל פשוט לא יקבל מספיק חומר ללמידה מעמיקה. ככל שהספרייה גדולה ומגוונת יותר, כך המודל ילמד טוב יותר את כל הניואנסים והוריאציות בסגנון.</li>
        <li>**ה"מוח": ארכיטקטורת המודל:** בחירת סוג המודל (שרשרת מרקוב, RNN, טרנספורמר וכו') קובעת את היכולות הבסיסיות שלו ללמוד ולהפיק. זה כמו לבחור אם ללמד את הילד לזהות מילים בודדות (מרקוב) או לכתוב סיפורים מורכבים (טרנספורמר).</li>
        <li>**מד ה"טעות": פונקציית ההפסד (Loss Function):** זהו המדד הקריטי ביותר בתהליך האימון. בכל פעם שהמודל מנסה לחזות את התו הבא ברצף ו"טועה" (כלומר, הניחוש שלו שונה מהתו האמיתי בדאטה-סט), פונקציית ההפסד "מתריעה" על גודל הטעות. ככל שההפסד גבוה יותר, המודל רחוק יותר מלהבין את הנתונים. המטרה של האימון היא למזער את הערך הזה.</li>
        <li>**ה"מורה": תהליך האופטימיזציה:** אלגוריתמים מתמטיים מתוחכמים (כמו Gradient Descent) פועלים כמו מורה שמכוונן את הפרמטרים הפנימיים של המודל (ה"מוח" שלו) בהתבסס על מד הטעות. הם מזהים באיזה כיוון יש "לעדכן" את המודל כדי שבפעם הבאה שיתקל ברצף דומה, הוא יטעה פחות. תהליך זה מתרחש על פני תקופות אימון רבות (Epochs).</li>
        <li>**"שעות הלימוד": תקופות אימון (Epochs):** כל תקופת אימון מייצגת מעבר מלא על כל נתוני האימון. המודל "מקשיב" לכל השירים בדאטה-סט פעם נוספת, משווה את תחזיותיו למציאות, ומשפר את עצמו. מעט מדי תקופות (תת-אימון) - המודל לא ילמד מספיק והשגיאה תישאר גבוהה. יותר מדי תקופות עלולות לגרום ל"שינון" במקום ל"הבנה" (Overfitting) - המודל ישנן את הדאטה-סט הספציפי במקום ללמוד את העקרונות הכלליים של המוזיקה, ויתקשה להלחין משהו חדש באמת.</li>
    </ul>

    <h2>השפעת הפרמטרים: כיצד לבנות מלחין AI מוצלח?</h2>
    <p>הסימולטור מאפשר לכם לשחק עם שני פרמטרים מרכזיים המשפיעים באופן דרמטי על תוצאות האימון:</p>
    <ul>
        <li>**כמות נתוני אימון:** דאטה-סט גדול יותר חושף את המודל למגוון רחב יותר של דפוסים, וריאציות ומבנים בסגנון הנבחר. ככל שיש יותר שירים בסגנון, כך המודל יכול ללמוד את ה"שפה" המוזיקלית על בוריה, ולהיות מסוגל ליצור יצירות מגוונות ועשירות יותר, עם סיכון נמוך יותר לחזור על עצמו או "להמציא" דפוסים לא קיימים. כמות גדולה יותר של דאטה לרוב מאיצה גם את ירידת השגיאה ההתחלתית.</li>
        <li>**מספר תקופות אימון:** קובע את "עומק" הלמידה. בכל תקופה, המודל מחדד את הבנתו ומקטין את שגיאותיו. מספר גבוה יותר של תקופות מאפשר לו להגיע לרמת דיוק גבוהה יותר ולהקטין את ההפסד בצורה משמעותית. עם זאת, כאמור, מספר מוגזם עלול לגרום להתאמת יתר. המטרה היא למצוא את "נקודת האיזון" שבה ההפסד נמוך והמודל עדיין יודע להכליל.</li>
    </ul>

    <h2>איך נדע אם המודל "הבין"?</h2>
    <p>מודל שאומן בהצלחה על דאטה-סט גדול ומגוון, עם מספר תקופות אופטימלי, יציג שגיאת אימון נמוכה משמעותית לעומת ההתחלה. שגיאה נמוכה מצביעה על כך שהמודל "הבין" טוב יותר את המבנה, ההרמוניה, והקצב של הסגנון הנבחר. כאשר משתמשים בו ליצירת מוזיקה חדשה (תהליך שנקרא "סמפול" או Generation), הוא נוטה להפיק יצירות שנשמעות קוהרנטיות, בעלות מבנה הגיוני, ויותר חשוב - נאמנות לסגנון שעל בסיסו אומן. בסימולטור, ירידת השגיאה ושיפור קטע המוזיקה המדומה משקפים את ההתקדמות הזו.</p>

    <h2>האתגרים שבדרך ליצירת מופת דיגיטלית</h2>
    <p>למרות ההתקדמות המדהימה, הלחנת AI עדיין מתמודדת עם אתגרים רבים שהסימולציה הזו מדמה באופן חלקי:</p>
    <ul>
        <li>**מבנה ארוך טווח:** קשה למודלים לשמור על קו מלודי, הרמוני או ריתמי שמתפתח באופן הגיוני ומרתק לאורך יצירה שלמה, מעבר לכמה תיבות בודדות.</li>
        <li>**רגש ואקספרסיביות:** מודלים מצליחים לחקות מבנים, אך הוספת "רגש", דינמיקה, ופרשנות אמנותית שמאפיינים מלחין או מבצע אנושי היא עדיין אתגר משמעותי.</li>
        <li>**מקוריות מול חיקוי:** לעיתים קרובות, המודל מייצר יצירות שנשמעות כמו קומפילציה או חיקוי ישיר של נתוני האימון, במקום ליצור משהו מקורי באמת שמרחיב את גבולות הסגנון.</li>
        <li>**הקשר תרבותי:** מוזיקה קשורה עמוקות להקשר תרבותי, היסטורי ורגשי. מודל AI אינו מבין את המשמעויות העמוקות הללו, אלא רק דפוסים סטטיסטיים בנתונים.</li>
    </ul>
     <small>הסימולטור הנ"ל הוא הדמיה פשטנית של תהליך אימון מורכב בהרבה, ונועד להמחיש את הקשר בין גודל הדאטה, תקופות האימון, ירידת שגיאת המודל ושיפור איכות הפלט הסימולטיבי. הוא אינו מריץ מודל AI אמיתי.</small>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const startButton = document.getElementById('start-training');
        const musicStyleSelect = document.getElementById('music-style');
        const dataSizeInput = document.getElementById('data-size');
        const epochsInput = document.getElementById('epochs');
        const progressBar = document.querySelector('.progress-bar');
        const progressText = document.getElementById('progress-text');
        const currentLossSpan = document.getElementById('current-loss');
        const lossGraphBar = document.querySelector('.loss-graph-bar');
        const generatedMusicSnippetDiv = document.getElementById('generated-music-snippet');
        const explanationDiv = document.getElementById('detailed-explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const trainingArea = document.querySelector('.training-area');
        const inputs = [musicStyleSelect, dataSizeInput, epochsInput, startButton];

        const initialLoss = 100; // Simulate a high starting loss
        let currentLoss = initialLoss;
        let animationFrameId = null; // To manage animation loop

        const musicSnippets = {
            initial: "[...ממתין לתחילת אימון...]",
            random: "[רעש דיגיטלי... צלילים אקראיים ולא קשורים...]",
            earlyTraining: "[מתחילים להופיע רמזים למקצב או מלודיה, אבל מבולגן וחסר קוהרנטיות...]",
            midTraining: "[ישנם אלמנטים מוזיקליים בסגנון הנבחר, כמו הרמוניות פשוטות או דפוסים ריתמיים, אך היצירה עדיין לא מובנית...]",
            lateTraining: "[נשמע כמו מוזיקה בסגנון הנבחר, עם מלודיות ואקורדים הגיוניים, אך עדיין יש טעויות מבניות או מעברים צורמים...]",
            trainedClassical: "[מנגינה קצרה ואלגנטית בסגנון באך, עם מבנה הרמוני צפוי וקונטרפונקט...]",
            trainedJazz: "[קטע ג'אז קצבי עם סווינג, אקורדים מורכבים ומוטיב מלודי שמתפתח...]",
            trainedRock: "[ריף גיטרה עוצמתי בסגנון רוק קלאסי, עם קצב תופים פשוט...]",
            trainedElectronic: "[ביט אלקטרוני חוזר ומדבק, עם קו בס וצלילי סינתיסייזר מלודיים...]"
        };

        function updateSimulatorState(progress, loss, musicText, isTraining = false) {
            progressBar.style.width = progress + '%';
            // Update text only for full percentage points
            progressText.textContent = Math.round(progress) + '%';

            currentLossSpan.textContent = loss.toFixed(2);

            // Scale loss bar height: max loss (initialLoss) = 100% height, minimum realistic loss (e.g., 5) = 0% height
            const minLoss = 5; // Assume loss can drop down to this minimum
            const maxLossRange = initialLoss - minLoss;
            const lossHeightPercent = Math.max(0, Math.min(100, ((loss - minLoss) / maxLossRange) * 100));
            // Invert height because 100% loss should be full bar, 0% loss should be empty bar
            lossGraphBar.style.height = lossHeightPercent + '%';

            // Change loss bar color based on loss value
            if (loss < initialLoss * 0.3) { // Lower third is green
                 lossGraphBar.classList.add('low-loss');
            } else {
                 lossGraphBar.classList.remove('low-loss');
            }


            // Update music snippet text more dynamically during simulation
             if (!isTraining || progress === 0 || progress === 100) {
                  generatedMusicSnippetDiv.textContent = musicText;
             } else {
                  // During training, update snippet based on progress intervals
                  if (progress < 20) {
                       generatedMusicSnippetDiv.textContent = musicSnippets.random;
                  } else if (progress < 45) {
                      generatedMusicSnippetDiv.textContent = musicSnippets.earlyTraining;
                  } else if (progress < 75) {
                       generatedMusicSnippetDiv.textContent = musicSnippets.midTraining;
                  } else {
                       generatedMusicSnippetDiv.textContent = musicSnippets.lateTraining;
                  }
             }

             // Add or remove training animation class
             if (isTraining) {
                 trainingArea.classList.add('is-training');
                 generatedMusicSnippetDiv.classList.add('is-training');
             } else {
                 trainingArea.classList.remove('is-training');
                 generatedMusicSnippetDiv.classList.remove('is-training');
             }
        }

        function runTrainingSimulation() {
            const dataSize = parseInt(dataSizeInput.value);
            const epochs = parseInt(epochsInput.value);
            const selectedStyle = musicStyleSelect.value;

            // Basic validation
            if (isNaN(dataSize) || dataSize < 1 || dataSize > 20 || isNaN(epochs) || epochs < 1 || epochs > 50) {
                 alert('אנא הכניסו ערכים תקינים לפרמטרים (גודל דאטה 1-20, תקופות 1-50).');
                 return;
            }

            // Disable controls during training
            inputs.forEach(input => input.disabled = true);

            currentLoss = initialLoss; // Reset loss
            updateSimulatorState(0, currentLoss, musicSnippets.random, true); // Start training state

            const totalSteps = 200; // More animation steps for smoother feel
            let currentStep = 0;
            const baseSimulationDuration = 8000; // Base total duration in ms
            // Adjust duration based on parameters - more data/epochs might simulate faster learning initially,
            // but overall training takes longer in reality. Let's simplify and make it a fixed time for animation.
            const simulationDuration = baseSimulationDuration;

            const startTime = performance.now();

            function simulateStep(currentTime) {
                const elapsedTime = currentTime - startTime;
                const progress = Math.min(1, elapsedTime / simulationDuration);

                // Simulate loss decrease based on progress and parameters
                // Faster initial drop, tapers off. Parameters influence the final loss level.
                // Loss decreases from initialLoss towards a minimum influenced by dataSize and epochs.
                const simulatedFinalMinLoss = Math.max(5, initialLoss * 0.2 - (dataSize * 0.5 + epochs * 0.4)); // A bit more sensitive to params
                const lossRange = initialLoss - simulatedFinalMinLoss;
                // Use a non-linear function for loss decrease (e.g., exponential decay or similar curve)
                const easedProgress = 1 - Math.pow(1 - progress, 3); // Cubic easing out
                currentLoss = initialLoss - (lossRange * easedProgress);

                updateSimulatorState(progress * 100, currentLoss, null, true); // Pass null for music text to let updateSimulatorState handle it

                currentStep++;
                if (progress < 1) {
                    animationFrameId = requestAnimationFrame(simulateStep);
                } else {
                    // Training finished
                    let finalLoss = Math.max(5, currentLoss); // Ensure it doesn't go below 5
                    let finalMusicSnippet;

                    if (finalLoss < initialLoss * 0.15) { // High quality
                        finalMusicSnippet = musicSnippets[`trained${selectedStyle.charAt(0).toUpperCase() + selectedStyle.slice(1)}`] || musicSnippets.lateTraining;
                    } else if (finalLoss < initialLoss * 0.3) { // Good quality
                         finalMusicSnippet = musicSnippets.lateTraining;
                    } else if (finalLoss < initialLoss * 0.5) { // Acceptable quality
                         finalMusicSnippet = musicSnippets.midTraining;
                    } else { // Poor quality
                         finalMusicSnippet = musicSnippets.earlyTraining;
                    }

                    updateSimulatorState(100, finalLoss, finalMusicSnippet, false); // End training state

                    // Re-enable controls
                    inputs.forEach(input => input.disabled = false);
                     cancelAnimationFrame(animationFrameId); // Stop the animation loop
                }
            }

             // Cancel any existing animation before starting a new one
             if (animationFrameId) {
                 cancelAnimationFrame(animationFrameId);
             }
             requestAnimationFrame(simulateStep); // Start the simulation loop
        }

        startButton.addEventListener('click', runTrainingSimulation);

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט על התהליך' : 'הצג הסבר מפורט על התהליך';
        });

        // Initial state setup
        updateSimulatorState(0, initialLoss.toFixed(2), musicSnippets.initial, false);
         lossGraphBar.style.height = '100%'; // Start loss bar at max height
         currentLossSpan.textContent = initialLoss.toFixed(2); // Display initial loss correctly
    });
</script>