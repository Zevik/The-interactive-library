---
title: "מליחות, חיים וניהול: סימולטור האסטואר"
english_slug: salinity-life-management-estuary-simulator
category: "כללי"
tags: [אסטואר, מליחות, מערכת אקולוגית, ניהול סביבתי, מים מליחים]
---
<h1>לב פועם של טבע: סימולטור האסטואר הדינמי</h1>

דמיינו רגע קסום שבו נהר שוצף פוגש את הים העצום – זהו האסטואר, אזור מעבר תוסס אך פגיע להפליא. כאן, מים מתוקים ומלוחים מתערבבים ליצירת עולם ייחודי. אבל איך האיזון העדין הזה שומר על אוכלוסיית היצורים המדהימה שחיה בו, ומה קורה כשקצה חוט בטבע נמשך רחוק מדי? צללו פנימה וגלו בעצמכם!

<div id="estuary-simulator">
    <div class="controls">
        <label for="riverFlow">זרימת נהר (כוח המים המתוקים):</label>
        <input type="range" id="riverFlow" min="0" max="100" value="50">
        <span id="riverFlowValue">50%</span>
        <br>
        <label for="seaInfluence">השפעת ים (כוח הגאות והשפל):</label>
        <input type="range" id="seaInfluence" min="0" max="100" value="50">
        <span id="seaInfluenceValue">50%</span>
    </div>
    <div class="estuary-representation">
        <div class="zone river">
            <h3>1. נהר (מתוק)</h3>
            <div class="salinity" data-zone="0">מליחות: <span></span> ppt</div>
            <div class="species">
                <div class="species-group fresh">🐟</div>
                <div class="species-group brackish">🦀</div>
                <div class="species-group salt">🐠</div>
            </div>
        </div>
        <div class="zone upper-estuary">
            <h3>2. שפך עליון</h3>
            <div class="salinity" data-zone="1">מליחות: <span></span> ppt</div>
            <div class="species">
                 <div class="species-group fresh">🐟</div>
                <div class="species-group brackish">🦀</div>
                <div class="species-group salt">🐠</div>
            </div>
        </div>
        <div class="zone mid-estuary">
            <h3>3. שפך אמצעי</h3>
             <div class="salinity" data-zone="2">מליחות: <span></span> ppt</div>
             <div class="species">
                 <div class="species-group fresh">🐟</div>
                <div class="species-group brackish">🦀</div>
                <div class="species-group salt">🐠</div>
            </div>
        </div>
        <div class="zone lower-estuary">
            <h3>4. שפך תחתון</h3>
            <div class="salinity" data-zone="3">מליחות: <span></span> ppt</div>
            <div class="species">
                 <div class="species-group fresh">🐟</div>
                <div class="species-group brackish">🦀</div>
                <div class="species-group salt">🐠</div>
            </div>
        </div>
        <div class="zone sea">
            <h3>5. ים (מלוח)</h3>
             <div class="salinity" data-zone="4">מליחות: <span></span> ppt</div>
             <div class="species">
                 <div class="species-group fresh">🐟</div>
                <div class="species-group brackish">🦀</div>
                <div class="species-group salt">🐠</div>
            </div>
        </div>
    </div>
    <p class="legend">
        <span class="species-group fresh">🐟</span> מינים מותאמים למים מתוקים | <span class="species-group brackish">🦀</span> מינים מותאמים למים מליחים | <span class="species-group salt">🐠</span> מינים מותאמים למים מלוחים. גודל ושקיפות האייקון מייצגים התאמה/שכיחות יחסית באזור זה.
    </p>
</div>

<button id="toggleExplanation" class="explanation-button">רוצים לדעת עוד? לחצו להסבר מעמיק</button>

<div id="explanation" style="display: none;">
    <h2>עולם של ניגודים מתערבבים: הצצה עמוקה לאסטוארים</h2>

    <h3>מהו בעצם אסטואר? מעבר בין שני עולמות</h3>
    אסטואר (שפך נהר) הוא כמו סף קסום בין היבשה והים. דמיינו גוף מים חופי, מוגן חלקית, שאליו נשפכים מים צלולים מנהרות, ופוגשים את הגלים המלוחים של האוקיינוס. התוצאה? תערובת ייחודית של מים מליחים, שיוצרת סביבה דינמית ומשתנה תמיד, רדודה יחסית, ומלאה בחיים. הצורות שלהם משתנות - מעמקי נהרות ששקעו ועד לגונות חופיות - אבל המאפיין המרכזי הוא המים המליחים והתנאים שמשתנים ללא הרף.

    <h3>למה האסטוארים כה חשובים? משתלות טבעיות ומרכזי חיים</h3>
    האסטוארים אינם רק אזורי מעבר יפים, הם מנועים אקולוגיים אדירים! הם נחשבים למערכות האקולוגיות הפוריות ביותר בעולם, ומתפקדים כ"משתלות" ענק עבור אינספור יצורים ימיים. דגים וחסרי חוליות רבים שחשובים לנו כלכלית מבלים דווקא במים המליחים המוגנים הללו את השלבים הרגישים של חייהם. בנוסף, הם מהווים בית גידול קריטי לעופות מים נודדים, יונקים ימיים, וצמחים עמידים כמו מנגרובים. כלכלית, הם תומכים בדיג מקומי, חקלאות ימית, משיכת תיירים, ומשמשים עורקי תחבורה ימית חשובים. מעבר לכך, הם פועלים כמסננים טבעיים, בולעים מזהמים ומגינים על החופים משחיקה.

    <h3>תעלומת המליחות המשתנה: הגרדיאנט ומי מזיז אותו?</h3>
    הקסם הייחודי של האסטואר טמון ב"גרדיאנט המליחות" - מפל מליחות מובהק שמתחיל כמעט במים מתוקים גמורים ליד הנהר, ומגיע למליחות ים ככל שמתקרבים לאוקיינוס. המפל הזה נוצר מהקרב המתמיד בין המים המתוקים לדוחף מהנהר לבין המים המלוחים שחודרים מהים. מי מנצח בקרב? זה תלוי בכמה גורמים:
    <ul>
        <li><b>כוח הנהר (זרימה):</b> נהר חזק דוחף את המים המלוחים החוצה, מוריד את המליחות ומרחיב את האזור המתוק יותר. נהר חלש מאפשר לים לפלוש פנימה.</li>
        <li><b>כוח הים (גאות ושפל):</b> תנועת הגלים והגאות מכניסה מים מלוחים, מערבלת אותם, וגאות חזקה יכולה לדחוף מליחות עמוק פנימה.</li>
        <li><b>צורת האסטואר:</b> אסטואר צר ועמוק יתנהג שונה מאסטואר רחב ורדוד.</li>
        <li><b>רוח ושמש:</b> רוחות יכולות לערבל את המים, ושמש חזקה יכולה להעלות מליחות דרך אידוי.</li>
    </ul>

    <h3>אתגר הישרדות במים מליחים: אלופי ההסתגלות</h3>
    לחיות באסטואר זה לא קל! רוב היצורים המימיים רגישים מאוד לשינויים במליחות. אבל החיים באסטואר לימדו את המקומיים להיות אלופי הסתגלות:
    <ul>
        <li><b>אוסמו-קונפורמרים:</b> רוב היצורים הימיים הרגילים (כמו כוכבי ים בים הפתוח) פשוט נותנים למליחות גופם להשתנות עם המים החיצוניים. הם לא שורדים שינויים דרסטיים במליחות ונשארים באזורים יציבים.</li>
        <li><b>אוסמו-רגולטורים:</b> אלו הם גיבורי האסטואר! יצורים כמו סרטנים ודגים רבים פיתחו מנגנונים מדהימים לשמור על מליחות פנימית יציבה, גם כשהמים בחוץ משתנים כל הזמן. הם יכולים להפריש מלחים דרך בלוטות מיוחדות, לספוג מלחים מהמים, או להשתמש בחומרים כימיים בתאים כדי לשמור על מאזן. הם המותאמים ביותר לחיים באזור המליח של האסטואר.</li>
    </ul>
    לכל מין יש טווח סבילות שונה, וזה מה שקובע איפה באסטואר סביר למצוא אותו.

    <h3>תושבי האסטואר: מי גר איפה?</h3>
    דמיינו את האסטואר כשכונות שונות, כל אחת עם האוכלוסייה האופיינית לה בהתאם למליחות:
    <ul>
        <li><b>שכונת הנהר (מים מתוקים, <5 ppt):</b> כאן תמצאו את הדגים והיצורים שמכירים מהנחלים והאגמים. הם לא סובלים מליחות כמעט בכלל.</li>
        <li><b>שכונת המליחים (מים מליחים, 5-18 ppt):</b> זוהי ה"שכונה" הייחודית ביותר. כאן פורחים המינים האוסמו-רגולטורים בעלי הסבילות הרחבה. אולי יש פחות מינים סך הכל מאשר בים או בנהר, אבל אלו שחיים כאן מופיעים בשפע גדול והם מותאמים באופן מושלם לתנאים המשתנים. זוהי המשתלה הגדולה!</li>
        <li><b>שכונת הים (מים מלוחים, >18 ppt):</b> ככל שמתקרבים לים, תמצאו יותר ויותר מינים ימיים "רגילים" שחודרים לאסטואר, חלקם בעלי סבילות מסוימת לשינויי מליחות קלים, לצד המינים האוסמו-רגולטורים שעמידים גם במליחות גבוהה.</li>
    </ul>

    <h3>כשהאיזון מופר: השפעות שינויי המליחות</h3>
    האיזון העדין באסטואר פגיע מאוד לשינויים, בין אם הם טבעיים (בצורת, שיטפונות) או נגרמים על ידינו (סכרים, שאיבת מים, זיהום, עליית מפלס הים). שינויים אלו משפיעים דרמטית:
    <ul>
        <li><b>החלשות הנהר:</b> כשזורמים פחות מים מתוקים (בגלל בצורת או שימוש אנושי), המים המלוחים פולשים פנימה עמוק יותר. זה מאיים על יצורי מים מתוקים ומליחים שלא עמידים למליחות גבוהה, פוגע בצמחיית גדות, והורס את אזורי הגידול של דגים צעירים.</li>
        <li><b>התחזקות הנהר:</b> שיטפונות יכולים לדחוף את המים המלוחים החוצה, להוריד מליחות מהר מדי ולפגוע במינים מהים שחדרו לאסטואר.</li>
        <li><b>עליית מפלס הים:</b> מגדילה את חדירת המליחות באופן קבוע, ומאיימת על בתי הגידול המתוקים והמליחים במעלה האסטואר.</li>
    </ul>

    <h3>שמירה על הלב הפועם: אתגרי הניהול הסביבתי</h3>
    ניהול אסטוארים הוא משימה מורכבת ביותר, כמו הליכה על חבל דק. צריך לאזן בין הצרכים שלנו (שתייה, חקלאות, נמל) לבין שמירה על המערכת האקולוגית הפלאית הזו. האתגרים עצומים:
    <ul>
        <li><b>להשאיר מספיק מים בנהר:</b> לוודא שלא שואבים יותר מדי מים מתוקים לשימושים שונים, כדי שהנהר ימשיך לדחוף את המים המלוחים החוצה וישמור על הגרדיאנט.</li>
        <li><b>להילחם בזיהום:</b> לצמצם חומרים רעילים שמגיעים לאסטואר ומזיקים לחיים בו.</li>
        <li><b>לשקם בתי גידול:</b> לעזור למנגרובים, עשבי ים וביצות מליחות לשגשג מחדש, כי הם ביתם של רבים.</li>
        <li><b>להתכונן לעליית מפלס הים:</b> לתכנן כיצד להגן על האזורים הנמוכים ועל בתי הגידול הרגישים מפני הצפה במים מלוחים.</li>
        <li><b>לחקור ולנטר:</b> להבין מה קורה באסטואר כל הזמן, למדוד מליחות וטמפרטורה ולעקוב אחר היצורים שחיים בו, כדי לקבל החלטות ניהול מושכלות.</li>
    </ul>
    ההצלחה תלויה בשיתוף פעולה אמיתי בין ממשלות, מדענים, הקהילות שחיות ליד האסטואר, וכל מי שאכפת לו מהעתיד של המקומות המדהימים הללו.

</div>

<style>
    /* כללי */
    #estuary-simulator {
        font-family: 'Arial', sans-serif;
        margin: 20px auto;
        max-width: 900px;
        padding: 25px; /* הגדלה קלה של הריפוד */
        border: 1px solid #d3d3d3; /* גבול עדין יותר */
        border-radius: 12px; /* פינות מעוגלות יותר */
        background-color: #ffffff; /* רקע לבן נקי */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* הצללה עדינה */
        direction: rtl;
        text-align: right;
    }

    /* בקרות משתמש */
    .controls {
        margin-bottom: 40px; /* מרווח תחתון גדול יותר */
        text-align: center;
        padding: 10px;
        background-color: #eef; /* רקע בהיר לבקרות */
        border-radius: 8px;
    }

    .controls label {
        margin-left: 20px; /* מרווח גדול יותר */
        font-weight: bold;
        display: inline-block;
        width: 160px; /* יישור לייבלים */
        text-align: right;
        color: #333;
        font-size: 1.1em;
    }

    .controls input[type="range"] {
        width: 250px; /* רוחב גדול יותר לסליידר */
        vertical-align: middle;
        -webkit-appearance: none; /* הסרת עיצוב ברירת מחדל */
        appearance: none;
        height: 8px;
        background: linear-gradient(to right, #add8e6, #00008b); /* גרדיאנט כחול לסליידר */
        border-radius: 5px;
        outline: none;
        margin: 0 10px;
    }

     .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #0056b3; /* כחול כהה לאגודל */
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }

      .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #0056b3;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }


     .controls span {
        display: inline-block;
        width: 50px; /* רוחב להצגת ערך */
        text-align: left;
        font-weight: bold;
        color: #0056b3;
     }

    /* ייצוג האסטואר החזותי */
    .estuary-representation {
        display: flex;
        height: 250px; /* גובה גדול יותר */
        border: 2px solid #0056b3; /* גבול כחול כהה */
        border-radius: 10px;
        overflow: hidden;
        position: relative; /* מאפשר מיקום אבסולוטי של הגרדיאנט */
        background: linear-gradient(to right, #add8e6 0%, #87ceeb 25%, #4682b4 50%, #1e90ff 75%, #00008b 100%); /* גרדיאנט בסיסי */
        transition: background 0.5s ease; /* אנימציה לשינוי רקע */
    }

    /* אזורים (Zones) - שכבות שקופות מעל הרקע */
    .zone {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-around; /* פיזור אחיד יותר של האלמנטים */
        align-items: center;
        padding: 15px; /* ריפוד פנימי גדול יותר */
        border-left: 1px solid rgba(255,255,255,0.4); /* קו הפרדה עדין */
        color: #fff; /* טקסט לבן */
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5); /* צל חזק יותר לטקסט */
        background-color: rgba(0, 0, 0, 0.1); /* שכבה שקופה כהה קלה */
        transition: background-color 0.3s ease; /* אנימציה לרקע (אם ישתנה) */
        position: relative; /* מאפשר Z-index */
        z-index: 1; /* מעל הרקע של האסטואר */
    }

    .zone:first-child {
         border-left: none;
    }

     .zone h3 {
        margin-top: 0;
        margin-bottom: 8px; /* מרווח קל אחרי הכותרת */
        font-size: 1.1em;
        text-align: center;
     }

    .salinity {
        font-size: 1em;
        margin-bottom: 15px; /* מרווח גדול יותר אחרי המליחות */
        font-weight: bold;
    }

    /* ייצוג מינים */
    .species {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        font-size: 2.2em; /* גודל אייקון גדול יותר */
        text-align: center;
        width: 100%; /* וודא שהקונטיינר משתמש ברוחב זמין */
    }

    .species .species-group {
        margin: 5px 0; /* מרווח בין אייקונים */
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out; /* אנימציה לשקיפות ושינוי גודל */
        opacity: 0; /* נסתר בתחילה */
        transform: scale(0.8); /* גודל התחלתי קטן יותר */
    }

     /* צבעי אייקונים מותאמים לנושא */
     .species .species-group.fresh { color: #66cdaa; /* ירוק-כחול עדין */ }
     .species .species-group.brackish { color: #ffc300; /* כתום-צהוב */ }
     .species .species-group.salt { color: #9932cc; /* סגול בישופס */ }


     /* אגדה */
     .legend {
         text-align: center;
         font-size: 0.95em;
         margin-top: 20px; /* מרווח גדול יותר */
         color: #555;
     }

     .legend span {
         font-size: 1.4em; /* גודל אייקון באגדה */
         vertical-align: middle;
         margin: 0 3px;
     }

      .legend .fresh { color: #66cdaa; }
      .legend .brackish { color: #ffc300; }
      .legend .salt { color: #9932cc; }


    /* כפתור הסבר */
    .explanation-button {
        display: block;
        margin: 30px auto 20px auto; /* מרווחים משופרים */
        padding: 12px 20px; /* ריפוד גדול יותר */
        font-size: 1.1em;
        cursor: pointer;
        border: none; /* הסרת גבול ברירת מחדל */
        border-radius: 25px; /* פינות עגולות מאוד */
        background-color: #007bff; /* כחול כפתור ראשי */
        color: white;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציית לחיצה */
    }

    .explanation-button:hover {
        background-color: #0056b3; /* כחול כהה יותר בריחוף */
    }

    .explanation-button:active {
        transform: scale(0.98); /* התכווצות בלחיצה */
    }


    /* איזור הסבר */
    #explanation {
        margin: 20px auto;
        max-width: 900px;
        padding: 25px; /* ריפוד משופר */
        border: 1px solid #d3d3d3;
        border-radius: 12px;
        background-color: #f8f8f8; /* רקע אפור בהיר מאוד */
        direction: rtl;
        text-align: right;
        line-height: 1.7; /* מרווח שורות גדול יותר */
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: #0056b3; /* כותרות בצבע כחול */
        margin-bottom: 15px;
        line-height: 1.4;
    }

    #explanation h2 {
        text-align: center;
        margin-bottom: 25px;
        font-size: 1.6em;
    }
     #explanation h3 {
        font-size: 1.3em;
        border-bottom: 1px solid #eee; /* קו תחתון עדין לכותרת תת-נושא */
        padding-bottom: 5px;
        margin-top: 25px;
     }


    #explanation p, #explanation ul {
        margin-bottom: 20px;
        line-height: 1.7;
    }

    #explanation ul {
        padding-right: 25px; /* הזחה גדולה יותר לרשימה */
    }

    #explanation li {
        margin-bottom: 10px;
    }
    #explanation li::before {
        content: '•'; /* נקודה יפה יותר לתחילת פריט רשימה */
        color: #007bff; /* צבע הנקודה */
        font-weight: bold;
        display: inline-block;
        width: 1em;
        margin-right: 0.5em;
        margin-left: -1.5em; /* הזזה שמאלה לפי הנקודה */
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const riverFlowSlider = document.getElementById('riverFlow');
        const seaInfluenceSlider = document.getElementById('seaInfluence');
        const riverFlowValueSpan = document.getElementById('riverFlowValue');
        const seaInfluenceValueSpan = document.getElementById('seaInfluenceValue');
        const salinitySpans = document.querySelectorAll('.salinity span');
        const speciesContainers = document.querySelectorAll('.zone .species');
        const estuaryRepresentationDiv = document.querySelector('.estuary-representation'); // לקבל את אלמנט הייצוג
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');

        // Base salinities for zones (approximate center values 0-35 ppt)
        const baseSalinity = [1, 6, 15, 25, 32]; // River, Upper, Mid, Lower, Sea

        // Sensitivity factors for how sliders affect salinity (per 100 units of slider)
        // Negative means reduction by river flow, positive means increase by sea influence
        const riverEffectFactor = [ -3, -8, -10, -6, -2]; // River flow pushes fresh water
        const seaEffectFactor = [ 3, 5, 9, 7, 1]; // Sea influence pushes salt water

        // Salinity thresholds for species (ppt)
        const freshThreshold = 4; // Highly suitable below this
        const freshUpperLimit = 8; // Less suitable above this, until 0 opacity

        const brackishMin = 5;
        const brackishPeak = 12; // Optimal for brackish species
        const brackishMax = 20;

        const saltThreshold = 18; // Highly suitable above this
        const saltLowerLimit = 15; // Less suitable below this, until 0 opacity


        function updateSimulation() {
            const riverFlow = parseInt(riverFlowSlider.value); // 0-100
            const seaInfluence = parseInt(seaInfluenceSlider.value); // 0-100

            riverFlowValueSpan.textContent = `${riverFlow}%`;
            seaInfluenceValueSpan.textContent = `${seaInfluence}%`;

            // Update background gradient based on slider values
            // Shift the midpoint of the gradient based on the balance of fresh/sea influence
            const gradientMidPoint = 30 + (seaInfluence - riverFlow) * 0.3; // Adjust factor for sensitivity
            estuaryRepresentationDiv.style.background = `linear-gradient(to right,
                #add8e6 0%, /* Fresh */
                #87ceeb ${Math.max(0, gradientMidPoint - 20)}%,
                #4682b4 ${gradientMidPoint}%, /* Transition point */
                #1e90ff ${Math.min(100, gradientMidPoint + 20)}%,
                #00008b 100% /* Salt */
            )`;


            salinitySpans.forEach((span, index) => {
                // Calculate salinity for the zone based on base + weighted slider effects
                let calculatedSalinity = baseSalinity[index] +
                                         (riverFlow / 100) * riverEffectFactor[index] +
                                         (seaInfluence / 100) * seaEffectFactor[index];

                // Clamp salinity between 0 and 35 (typical open sea maximum)
                calculatedSalinity = Math.max(0, Math.min(35, calculatedSalinity));

                // Update salinity display (rounded to 1 decimal place)
                span.textContent = calculatedSalinity.toFixed(1);

                // Update species visibility/opacity/size
                const speciesDivs = speciesContainers[index].querySelectorAll('.species-group');
                const freshDiv = speciesDivs[0];
                const brackishDiv = speciesDivs[1];
                const saltDiv = speciesDivs[2];

                // Calculate suitability (0-1) for each species group based on salinity
                let freshSuitability = 0;
                if (calculatedSalinity <= freshThreshold) {
                    freshSuitability = 1; // Full suitability below threshold
                } else if (calculatedSalinity < freshUpperLimit) {
                    freshSuitability = 1 - (calculatedSalinity - freshThreshold) / (freshUpperLimit - freshThreshold); // Linear decrease
                }
                freshDiv.style.opacity = freshSuitability;
                freshDiv.style.transform = `scale(${0.8 + freshSuitability * 0.5})`; // Scale grows with suitability

                let brackishSuitability = 0;
                if (calculatedSalinity >= brackishMin && calculatedSalinity <= brackishMax) {
                     // Suitability peaks at brackishPeak, decreases towards min/max
                     if (calculatedSalinity <= brackishPeak) {
                         brackishSuitability = (calculatedSalinity - brackishMin) / (brackishPeak - brackishMin);
                     } else {
                         brackishSuitability = (brackishMax - calculatedSalinity) / (brackishMax - brackishPeak);
                     }
                     brackishSuitability = Math.max(0, Math.min(1, brackishSuitability)); // Clamp between 0 and 1

                }
                brackishDiv.style.opacity = brackishSuitability;
                brackishDiv.style.transform = `scale(${0.8 + brackishSuitability * 0.5})`; // Scale grows with suitability


                let saltSuitability = 0;
                 if (calculatedSalinity >= saltThreshold) {
                     saltSuitability = 1; // Full suitability above threshold
                 } else if (calculatedSalinity > saltLowerLimit) {
                     saltSuitability = (calculatedSalinity - saltLowerLimit) / (saltThreshold - saltLowerLimit); // Linear increase
                 }
                saltSuitability = Math.max(0, Math.min(1, saltSuitability)); // Ensure value is between 0 and 1
                saltDiv.style.opacity = saltSuitability;
                saltDiv.style.transform = `scale(${0.8 + saltSuitability * 0.5})`; // Scale grows with suitability

                // Set a minimum opacity for visibility even when suitability is low, if desired
                // freshDiv.style.opacity = Math.max(0.1, freshSuitability);
                // brackishDiv.style.opacity = Math.max(0.1, brackishSuitability);
                // saltDiv.style.opacity = Math.max(0.1, saltSuitability);

            });
        }

        // Event listeners for sliders
        riverFlowSlider.addEventListener('input', updateSimulation);
        seaInfluenceSlider.addEventListener('input', updateSimulation);

        // Event listener for explanation button
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            // Use a simple fade-in/out effect if possible with CSS transitions or JS animation
            if (isHidden) {
                 explanationDiv.style.opacity = '0';
                 explanationDiv.style.display = 'block';
                 setTimeout(() => { explanationDiv.style.opacity = '1'; }, 10); // Small delay for transition
            } else {
                 explanationDiv.style.opacity = '0';
                 setTimeout(() => { explanationDiv.style.display = 'none'; }, 500); // Delay hiding until fade out
            }

            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'רוצים לדעת עוד? לחצו להסבר מעמיק';
        });

        // Initial simulation update on page load
        updateSimulation();

        // Add CSS for fade transition to explanation div (can also add to the style block)
        explanationDiv.style.transition = 'opacity 0.5s ease-in-out';

    });
</script>