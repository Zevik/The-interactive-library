---
title: "סודות התעופה: מסע מרתק לביומכניקה של כנפי ציפורים וחרקים"
english_slug: biomechanics-of-flight-bird-wing-vs-insect-wing
category: "מדעי החיים / ביולוגיה"
tags: ["תעופה", "ביומכניקה", "ציפורים", "חרקים", "אבולוציה", "פיזיקה", "הנדסה ביו-השראה"]
---
<h1>סודות התעופה: מסע מרתק לביומכניקה של כנפי ציפורים וחרקים</h1>
<p>הם שולטים בשמיים באלגנטיות מעוררת השראה, אך מנגנוני התעופה שלהם שונים בתכלית! הצטרפו אלינו למסע ויזואלי ואינטראקטיבי שיחשוף איך יצורים כל כך שונים מצליחים להמריא, לשייט, ולבצע תמרונים אוויריים מדהימים באותה סביבה, ומהם העקרונות הפיזיקליים והביולוגיים המאפשרים לכל אחד מהם את כושר התעופה הייחודי שלו.</p>

<div class="app-container">
    <h2>חקרו את התנועה: סימולציית כנפיים אינטראקטיבית</h2>
    <p class="app-intro">הריצו את הסימולציה כדי לראות מקרוב את ההבדלים הדרמטיים במבנה ובתנועת כנפי ציפור וכנף חרק. נסו לשלוט במהירות התנועה ולבחון כל כנף בנפרד או בסנכרון.</p>
    <div class="animation-area">
        <div class="animation-box bird">
            <h3>כנף ציפור: כוח ודיוק</h3>
            <div id="bird-animation" class="animation-placeholder">
                <!-- כאן תהיה הדמיית 3D מרהיבה של כנף ציפור בתנועה, המדגימה את קיפול ופרישת הכנף, פיתול הנוצות, ותנועת החתירה המלאה. הדגש יהיה על כוח, אווירודינמיקה קלאסית, ושינוי צורת הכנף. -->
                <p class="placeholder-text">הדמיית 3D מתקדמת של כנף ציפור</p>
            </div>
             <p class="animation-description">ראו כיצד הכנף הגרמית, המכוסה בנוצות עוצמתיות, משנה את צורתה ומנצלת את זרימת האוויר ליצירת עילוי ודחף בחתירות איטיות יחסית אך חזקות.</p>
        </div>
        <div class="animation-box insect">
            <h3>כנף חרק: מהירות ופיתול</h3>
            <div id="insect-animation" class="animation-placeholder">
                <!-- כאן תהיה הדמיית 3D מרהיבה של כנף חרק בתנועה, המדגימה את קצב החתירה המטורף, התנועה התלת-ממדית המורכבת, והפיתול הדינמי של הכנף. הדגש יהיה על קצב, תנועה מסלולית, ואווירודינמיקה של מספר ריינולדס נמוך (כמו LEV). -->
                <p class="placeholder-text">הדמיית 3D מתקדמת של כנף חרק</p>
            </div>
             <p class="animation-description">התפלאו מהתנועה המסחררת של כנף החרק הקלה, העשויה ממברנה ועורקים. גלו כיצד תנועה תלת-ממדית ופיתול הכנף מאפשרים קצב חתירה גבוה במיוחד ויצירת עילוי בדרכים לא שגרתיות.</p>
        </div>
    </div>
    <div class="controls-area">
         <h3>בקרות הסימולציה</h3>
        <div class="control-group">
            <button id="play-btn" aria-label="הרץ אנימציה">הרץ</button>
            <button id="pause-btn" aria-label="עצור אנימציה">עצור</button>
            <button id="slow-btn" aria-label="האט מהירות (פי 0.5)">האט (x0.5)</button>
            <button id="normal-btn" aria-label="מהירות רגילה (פי 1)">מהירות רגילה (x1)</button>
        </div>
        <div class="control-group">
            <input type="checkbox" id="sync-checkbox" checked aria-label="סנכרן תנועת כנף ציפור וכנף חרק">
            <label for="sync-checkbox">סנכרן אנימציות</label>
        </div>
        <!-- בקרות נוספות אפשריות בסימולציה מלאה (כגון שינוי זווית צפייה, הפעלת מסלולי תנועה, הדמיית זרימת אוויר) יוצגו כאן -->
    </div>
</div>

<style>
    /* סגנונות כלליים ופריסה */
    .app-container {
        direction: rtl;
        text-align: right;
        font-family: 'Heebo', sans-serif; /* שימוש בפונט עברי מודרני יותר */
        margin-top: 30px;
        border: none; /* הסרת border בסיסי */
        padding: 25px;
        border-radius: 12px; /* פינות מעוגלות יותר */
        background: linear-gradient(to bottom right, #eef2f7, #d9e2ec); /* רקע עם גרדיאנט עדין */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* צל עדין להדגשה */
    }

    .app-container h1, .app-container h2 {
        text-align: center; /* כותרות מרכזיות */
        color: #0a3d62; /* צבע כהה יותר לכותרות */
        margin-bottom: 15px;
    }

     .app-intro {
        text-align: center;
        margin-bottom: 30px;
        color: #333;
        font-size: 1.1em;
        line-height: 1.6;
     }

    .animation-area {
        display: flex;
        flex-direction: column; /* עמודה במובייל */
        justify-content: space-around;
        gap: 30px; /* רווח גדול יותר */
        margin-bottom: 30px;
    }

    @media (min-width: 768px) { /* פריסה בשורה במסכים גדולים */
        .animation-area {
            flex-direction: row;
        }
    }


    .animation-box {
        flex: 1;
        background-color: #ffffff; /* רקע לבן לתיבת האנימציה */
        border: 1px solid #d0d7de; /* גבול עדין */
        border-radius: 8px;
        padding: 20px; /* ריווח פנימי גדול יותר */
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); /* צל עדין */
        transition: transform 0.3s ease; /* אנימציית ריחוף קלה בהום */
    }

     .animation-box:hover {
         transform: translateY(-5px);
     }

    .animation-placeholder {
        width: 100%;
        height: 350px; /* גודל placeholder גדול יותר לאנימציה */
        background: linear-gradient(135deg, #e0e0e0, #f0f0f0); /* רקע מעודן יותר */
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1.2em;
        color: #666;
        border: 2px dashed #b0b0b0; /* גבול מקווקו מודגש יותר */
        box-sizing: border-box;
        border-radius: 6px;
        position: relative; /* להצגת טקסט ההסבר */
        overflow: hidden; /* לוודא שהתוכן לא יוצא מהגבולות */
         /* אנימציית פעימה עדינה לרמז על דינמיות */
        animation: pulse-placeholder 2s infinite ease-in-out;
    }

     @keyframes pulse-placeholder {
        0% { border-color: #b0b0b0; }
        50% { border-color: #888888; }
        100% { border-color: #b0b0b0; }
     }


    .animation-placeholder .placeholder-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 5px;
    }


    h3 {
        margin-top: 0;
        color: #145da0; /* צבע כחול כהה יותר לכותרות פנימיות */
        margin-bottom: 10px;
        font-size: 1.3em;
    }

    .animation-description {
        font-size: 0.95em;
        color: #555;
        margin-top: 15px;
        line-height: 1.5;
    }

    .controls-area {
        text-align: center;
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #eee; /* גבול עליון עדין */
    }

     .controls-area h3 {
         color: #0a3d62;
         margin-bottom: 20px;
     }

    .control-group {
        margin-bottom: 20px; /* רווח גדול יותר בין קבוצות בקרים */
         display: inline-block; /* הצגת הקבוצות בשורה במידת האפשר */
         margin: 0 15px 20px; /* רווח בין קבוצות */
    }

    .controls-area button {
        padding: 10px 20px; /* גודל כפתורים נוח יותר */
        margin: 0 8px; /* רווח בין כפתורים */
        cursor: pointer;
        border: none; /* הסרת גבול בסיסי */
        border-radius: 25px; /* כפתורים עגולים יותר */
        background-color: #007bff;
        color: white;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציות לכפתורים */
        box-shadow: 0 2px 4px rgba(0, 123, 255, 0.3); /* צל לכפתורים */
    }

    .controls-area button:hover {
        background-color: #0056b3;
        transform: translateY(-1px); /* אפקט לחיצה קל */
    }

     .controls-area button:active {
        background-color: #003f7f;
        transform: translateY(0);
        box-shadow: 0 1px 2px rgba(0, 123, 255, 0.4);
     }

    .controls-area input[type="checkbox"] {
        margin-left: 8px; /* רווח אחרי צ'קבוקס */
         transform: scale(1.2); /* גודל צ'קבוקס נוח יותר */
         vertical-align: middle; /* יישור עם הטקסט */
    }

     .controls-area label {
         font-size: 1.1em;
         color: #333;
         vertical-align: middle;
     }

    /* סגנונות לכפתור הצגת/הסתרת הסבר */
    #toggle-explanation-btn {
        display: block;
        width: fit-content;
        margin: 40px auto 20px; /* רווח גדול יותר למעלה ולמטה */
        padding: 12px 25px; /* פדינג גדול יותר */
        font-size: 1.2em; /* גודל פונט גדול יותר */
        cursor: pointer;
        border: none;
        border-radius: 30px; /* כפתור עגול יותר */
        background-color: #28a745; /* צבע ירוק רענן */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3); /* צל לכפתור */
    }

    #toggle-explanation-btn:hover {
        background-color: #218838;
        transform: translateY(-1px);
    }

     #toggle-explanation-btn:active {
        background-color: #1e7e34;
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(40, 167, 69, 0.4);
     }


    /* סגנונות לאזור ההסבר */
    .explanation-content {
        margin-top: 30px;
        padding: 30px; /* פדינג גדול יותר */
        border: none; /* הסרת גבול בסיסי */
        border-radius: 12px;
        background-color: #ffffff; /* רקע לבן נקי */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* צל עדין */
        line-height: 1.7; /* ריווח שורות נוח לקריאה */
        color: #333;
    }

    .explanation-content h2,
    .explanation-content h3 {
        color: #0a3d62; /* צבע כהה יותר */
        border-bottom: 2px solid #eef2f7; /* גבול תחתון עדין */
        padding-bottom: 8px; /* ריווח מתחת לגבול */
        margin-top: 30px;
        margin-bottom: 15px;
        font-weight: bold;
    }

     .explanation-content h2 {
         font-size: 1.8em;
         text-align: center;
     }

     .explanation-content h3 {
         font-size: 1.4em;
     }


    .explanation-content p {
        margin-bottom: 20px; /* ריווח תחתון גדול יותר לפסקאות */
        text-align: justify; /* יישור לרוחב */
     }

     .explanation-content strong {
         color: #145da0; /* הדגשת מונחים בצבע */
     }

     .explanation-content ul {
        margin-bottom: 20px;
        padding-right: 20px; /* ריווח לרשימה */
     }

     .explanation-content li {
        margin-bottom: 10px; /* ריווח בין פריטי רשימה */
     }
</style>

<button id="toggle-explanation-btn" aria-expanded="false">הצג הסבר מורחב</button>

<div id="explanation" class="explanation-content" style="display: none;">
    <h2>הסודות מאחורי הפלא: ביומכניקת התעופה לעומק</h2>
    <p>כיצד מצליחים יצורים חיים להתגבר על כוח המשיכה ולפרוץ את גבולות הקרקע? התעופה, בין אם של ציפור או של חרק, היא הישג אבולוציוני מדהים המבוסס על עקרונות פיזיקליים ואווירודינמיים מורכבים, המיושמים באמצעות מבנים ביולוגיים מתוחכמים.</p>

    <h3>עקרונות התעופה הבסיסיים: ריקוד הכוחות</h3>
    <p>כל גוף מעופף באוויר נתון להשפעת ארבעה כוחות עיקריים הנמצאים במאבק מתמיד:</p>
    <ul>
        <li><strong>משקל:</strong> הכוח המושך את הגוף ישירות מטה, כוח המשיכה הפועל על מסתו.</li>
        <li><strong>עילוי (Lift):</strong> הכוח הפועל לרוב בניצב לכיוון התנועה, בדרך כלל כלפי מעלה, ומתנגד למשקל. עילוי נוצר בעיקר בזכות צורתן המיוחדת של הכנפיים (פרופיל אווירודינמי) המאלצת אוויר לנוע מהר יותר מעל החלק העליון מאשר מתחתיו, ויוצרת הפרש לחצים (עקרון ברנולי), או באמצעות תנועת הכנף הדוחפת אוויר מטה (חוק ניוטון השלישי).</li>
        <li><strong>גרר (Drag):</strong> הכוח המתנגד לתנועה קדימה, נגרם מהתנגדות האוויר. ישנם סוגי גרר שונים, כמו גרר צורה וגרר החיכוך.</li>
        <li><strong>דחף (Thrust):</strong> הכוח הפועל בכיוון התנועה קדימה, נוצר על ידי תנועת הכנפיים או מנוע (במטוסים). הדחף מתגבר על הגרר ומאפשר תאוצה או שמירה על מהירות.</li>
    </ul>
    <p>תעופה יציבה מתרחשת כאשר העילוי מאזן את המשקל והדחף מאזן את הגרר.</p>

    <h2>ביומכניקת תעופת ציפורים: יעילות ושינוי צורה</h2>
    <p>כנף הציפור היא יצירת מופת של הנדסה טבעית. היא אינה מבנה קשיח, אלא מערכת דינמית המבוססת על שלד, שרירים רבי עוצמה, ומערך מופלא של נוצות בעלות תכונות אווירודינמיות.</p>
    <h3>המבנה המתוחכם: עצמות, שרירים רבי עוצמה ונוצות מותאמות</h3>
    <p>שלד הכנף מקביל לגפה קדמית של יונק, עם התאמות קיצוניות לתעופה. שרירי החזה הגדולים הם האחראים לחתירת מטה החזקה, יצירת עיקר העילוי והדחף. שרירים קטנים יותר מרימים את הכנף בחזרה למעלה בצורה יעילה.</p>
    <p>הנוצות (אברות) הן קריטיות. אברות היד בקצה הכנף פועלות כ"פרופלורים" המייצרים דחף קדימה וניתנות לפיתול. אברות האמה יוצרות את משטח הכנף הרחב יותר הקרוב לגוף, האחראי בעיקר ליצירת עילוי.</p>
    <h3>הכנף כדינמית משתנה: מחזור החתירה</h3>
    <p>מחזור החתירה כולל שני שלבים עיקריים:</p>
    <ul>
        <li><strong>חתירת מטה (Downstroke):</strong> הכנף נפרשת ומורדת בכוח תוך פיתול קל של אברות היד. בשלב זה נוצרת מרבית האנרגיה לתעופה - עילוי ל התגברות על המשקל ודחף להתגברות על הגרר.</li>
        <li><strong>חתירת מעלה (Upstroke):</strong> הכנף מתקפלת קרוב יותר לגוף, ואברות היד מסתובבות ומאפשרות לאוויר לזרום דרכן. תנועה זו ממזערת את הגרר השלילי ואת איבוד העילוי, ומאפשרת חזרה מהירה ויעילה למצב ההתחלה לחתירה הבאה.</li>
    </ul>
    <p>שינוי הצורה והאוריינטציה של הכנף מאפשר לציפור לבצע מגוון רחב של תמרונים - מהמראה ונחיתה, דרך דאייה יעילה, ועד תעופה במהירויות שונות.</p>
    <h3>השפעת קנה המידה: עולם האינרציה</h3>
    <p>ציפורים פועלות בעולם אווירודינמי שבו כוחות האינרציה דומיננטיים על פני כוחות הצמיגות (מספר ריינולדס גבוה). זה מאפשר להן לנצל פרופילים אווירודינמיים קלאסיים ולייצר עילוי יציב יחסית.</p>

    <h2>ביומכניקת תעופת חרקים: מהירות וחדשנות</h2>
    <p>התעופה אצל חרקים היא תופעה שונה בתכלית, המותאמת לגודלם הקטן ולסביבה האווירודינמית שונה בתכלית.</p>
    <h3>המבנה הפשוט למראה: ממברנה, עורקים, ושרירי חזה היסטריים</h3>
    <p>כנפי החרק הן מבנים קלים, לרוב שקופים, העשויים ממברנה כיטינית דקה המקבלת קשיחות ותמיכה מעורקים. הכנף עצמה אינה מכילה שרירים (ברוב המינים). הכוח מגיע משרירי חזה רבי עוצמה, שהם מהשרירים המהירים ביותר בטבע, ומסוגלים להניע את הכנפיים בקצב מטורף - מאות ואף אלפי חתירות בשנייה!</p>
    <h3>תנועה תלת-ממדית מורכבת: סוד העילוי הקטלני</h3>
    <p>בניגוד לתנועה הדו-ממדית העיקרית של ציפורים, כנף החרק מבצעת תנועה מסלולית מלאה במרחב התלת-ממדי. היא נעה קדימה-מטה ואז אחורה-מעלה, תוך כדי סיבוב מהיר סביב צירה. תנועה זו מאפשרת לחרק לייצר עילוי עצום יחסית לגודלו, ולהישאר באוויר למרות קצב התקדמות איטי יחסית (ריחוף).</p>
    <h3>יצירת עילוי באמצעות מערבולות: כנפיים חכמות</h3>
    <p>בעולם של מספרי ריינולדס נמוכים, כוחות צמיגות משפיעים יותר. חרקים רבים מנצלים זאת לטובתם. אחד המנגנונים המדהימים הוא יצירת "מערבולת קצה מוביל" (Leading Edge Vortex - LEV). המערבולת נוצרת על הצד העליון של הכנף ו"נצמדת" אליה, מגדילה דרמטית את העילוי ומאפשרת לחרק לתמרן בזוויות התקפה גבוהות שהיו גורמות הזדקרות בכנף מטוס קלאסית.</p>
    <h3>השפעת קנה המידה: עולם הצמיגות</h3>
    <p>גודלם הקטן של החרקים מכניס אותם לעולם אווירודינמי שונה, שבו הצמיגות של האוויר משמעותית יותר. תנועות הכנף המורכבות, קצב החתירה הגבוה, והשימוש במערבולות כמו ה-LEV הם התאמות אבולוציוניות חיוניות כדי לפעול ביעילות בסביבה זו.</p>

    <h2>אבולוציה של חדשנות: פתרונות גאוניים מאת הטבע</h2>
    <p>השוני הדרמטי במנגנוני התעופה של ציפורים וחרקים הוא עדות מדהימה לכוחה של האבולוציה לפתח פתרונות שונים לחלוטין לאותה בעיה פיזיקלית - כיצד לעוף? כל אחת מהשיטות מותאמת באופן מושלם לגודל היצור, למבנה גופו, ולסביבה האווירודינמית הספציפית בה הוא פועל.</p>

    <h2>השראה להנדסה ולעתיד: ביו-השראה ורובוטיקה</h2>
    <p>הבנת המנגנונים הביולוגיים של התעופה מספקת אוצר בלום של רעיונות למהנדסים. תחום ה"ביו-השראה" (Bioinspiration) או "ביו-חיקוי" (Biomimicry) מתמקד בחיקוי מבנים ותהליכים מהטבע ליצירת טכנולוגיות חדשות. מיקרו-רחפנים זעירים (MAVs) המנסים לחקות את תנועת כנפי החרקים, או כלי טיס גדולים יותר המשלבים עקרונות של שינוי צורת כנף בהשראת ציפורים, הם רק דוגמאות מעטות לאופן שבו הטבע ממשיך ללמד אותנו כיצד לכבוש את השמיים.</p>
</div>

<script>
    // קבלת הפניות לאלמנטים ב-DOM
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation-btn');
    const playBtn = document.getElementById('play-btn');
    const pauseBtn = document.getElementById('pause-btn');
    const slowBtn = document.getElementById('slow-btn');
    const normalBtn = document.getElementById('normal-btn');
    const syncCheckbox = document.getElementById('sync-checkbox');

    // משתנים פנימיים לניהול מצב הסימולציה
    let isPlaying = false;
    let currentSpeed = 1; // 1: רגיל, 0.5: איטי

    // --- פונקציות Placeholder לשליטה באנימציות 3D בפועל ---
    // **הערה למפתח:** בפיתוח אמיתי, פונקציות אלו יתקשרו עם מנוע 3D (כמו Three.js, Babylon.js, או Godot ב-WebAssembly)
    // כדי לטעון מודלים תלת-ממדיים של הכנפיים, לשלוט באנימציות שלהם (timeline, לולאות),
    // לשנות את מהירות ההשמעה, ולנהל את מצב הפלייבק (נגן/השהה).
    // ייתכן שיהיה צורך במנגנון סנכרון פנימי במנוע ה-3D אם האנימציות שונות באורכן.

    /**
     * מפעיל או ממשיך אנימציה (של ציפור, חרק, או שתיהן).
     * @param {string} target - 'bird', 'insect', או 'all'. כרגע רק 'all' נתמך בבקרות ה-UI.
     */
    function playAnimation(target = 'all') {
        console.log(`[SIMULATION Placeholder] Play command received for: ${target}. Speed: ${currentSpeed}. Sync: ${syncCheckbox.checked}`);
        isPlaying = true;
        // **הערה למפתח:** כאן ימומש הקוד להפעלת/חידוש אנימציות ה-3D.
        // לדוגמה: birdAnimation.play(currentSpeed); insectAnimation.play(currentSpeed);
        // אם syncCheckbox מסומן, ייתכן שיהיה צורך לוודא שהאנימציות מתחילות מאותו מקטע זמן או מסונכרנות לולאות.
    }

    /**
     * משהה אנימציה (של ציפור, חרק, או שתיהן).
     * @param {string} target - 'bird', 'insect', או 'all'. כרגע רק 'all' נתמך בבקרות ה-UI.
     */
    function pauseAnimation(target = 'all') {
        console.log(`[SIMULATION Placeholder] Pause command received for: ${target}.`);
        isPlaying = false;
        // **הערה למפתח:** כאן ימומש הקוד להשהיית אנימציות ה-3D.
        // לדוגמה: birdAnimation.pause(); insectAnimation.pause();
    }

    /**
     * קובע את מהירות ההשמעה של האנימציה/ות.
     * @param {number} speed - פקטור המהירות (למשל 0.5 להילוך איטי, 1 למהירות רגילה).
     */
    function setSpeed(speed) {
        currentSpeed = speed;
        console.log(`[SIMULATION Placeholder] Setting speed to: ${speed}.`);
        // **הערה למפתח:** כאן ימומש הקוד לעדכון מהירות האנימציות הפעילות.
        // אם אנימציה רצה, המהירות תתעדכן מיד. אם מושהית, המהירות תוגדר לפעם הבאה שתופעל.
        // לדוגמה: birdAnimation.setPlaybackSpeed(currentSpeed); insectAnimation.setPlaybackSpeed(currentSpeed);
        if (isPlaying) {
             // אם כבר מנגן, צריך להפעיל מחדש עם המהירות החדשה או לעדכן ישירות את אובייקט האנימציה.
             // במנועי 3D רבים, קריאה ל play לאחר שינוי מהירות מיישמת את השינוי.
             // playAnimation(); // אפשרות אחת, תלוי יישום.
        }
    }

     /**
      * מטפל בשינוי מצב הסנכרון.
      */
     function handleSyncChange() {
         const isSynced = syncCheckbox.checked;
         console.log(`[SIMULATION Placeholder] Sync toggled: ${isSynced}.`);
         // **הערה למפתח:** כאן ימומש הקוד שמטפל בסנכרון.
         // אם סונכרן: לוודא ששתי האנימציות פועלות באותה מהירות (speed * sync_factor?) ואולי מאותו רגע ב-timeline.
         // אם בוטל סנכרון: האנימציות יכולות לרוץ באופן עצמאי (אם כי בקרות ה-UI הנוכחיות מפעילות את שתיהן יחד).
         if (isPlaying) {
             // יש ליישם את לוגיקת הסנכרון במנוע ה-3D
             // לדוגמה: if (isSynced) syncAnimations(); else allowIndependentAnimations();
         }
     }

    // --- סוף פונקציות Placeholder ---


    // Event Listeners לבקרות
    playBtn.addEventListener('click', () => {
        playAnimation();
         // עדכון מצב הכפתורים (אפור/צבעוני) יכול להתווסף כאן ביישום אמיתי
    });

    pauseBtn.addEventListener('click', () => {
        pauseAnimation();
         // עדכון מצב הכפתורים
    });

    slowBtn.addEventListener('click', () => {
        setSpeed(0.5);
         // הדגשת הכפתור הפעיל (אפשר להוסיף קלאס CSS)
         slowBtn.classList.add('active-speed');
         normalBtn.classList.remove('active-speed');
    });

    normalBtn.addEventListener('click', () => {
        setSpeed(1);
         // הדגשת הכפתור הפעיל
         normalBtn.classList.add('active-speed');
         slowBtn.classList.remove('active-speed');
    });

    syncCheckbox.addEventListener('change', handleSyncChange);

    // Event Listener לכפתור הצגת/הסתרת הסבר
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            toggleButton.textContent = 'הסתר הסבר מורחב';
            toggleButton.setAttribute('aria-expanded', 'true');
        } else {
            explanationDiv.style.display = 'none';
            toggleButton.textContent = 'הצג הסבר מורחב';
             toggleButton.setAttribute('aria-expanded', 'false');
        }
    });

    // הגדרה ראשונית: האנימציות מושהות (קונספטואלית), ההסבר מוסתר
    pauseAnimation(); // ודא שהאנימציות אינן רצות עם טעינת הדף (תיאורטי)
    normalBtn.classList.add('active-speed'); // הדגשת מהירות רגילה כברירת מחדל

</script>
```