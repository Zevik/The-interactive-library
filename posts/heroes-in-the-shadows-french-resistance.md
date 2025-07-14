---
title: "גיבורים בצללים: התנגדות צרפתית"
english_slug: heroes-in-the-shadows-french-resistance
category: "ארכאולוגיה"
tags:
  - מלחמת העולם השנייה
  - התנגדות צרפתית
  - היסטוריה צבאית
  - סימולציה
  - משחקי תפקידים
---
# גיבורים בצללים: ההימור הגדול של המחתרת הצרפתית

שנת 1942, צרפת תחת כיבוש נאצי. בכל פינה אורבת סכנה, כל צעד נמדד בקפידה, וכל לחישה עשויה להגיע לאוזניים הלא נכונות. אתם חלק מתא מחתרתי קטן, שברירי, הנאבק לשרוד ולפעול ממעמקי הצללים. גורלכם, וגורל הרשת כולה, תלוי בהחלטות שתקבלו. האם תוכלו לנווט בנתיבי הסכנה, לצבור הישגים למען המאבק, ולהימנע מחשיפה קטלנית?

<div class="resistance-app interactive-container">
    <div class="app-header">
        <h2 class="app-title">פעולה מחתרתית</h2>
        <div class="stats-bar">
            <div class="stat-item risk-stat">
                <span class="stat-label">סכנה:</span>
                <span id="total-risk" class="stat-value">0</span>
                <span class="risk-level">נמוכה</span>
            </div>
            <div class="stat-item progress-stat">
                <span class="stat-label">הישגים:</span>
                <span id="total-progress" class="stat-value">0</span>
                 <span class="progress-level">התחלה</span>
            </div>
        </div>
    </div>

    <div class="scenario-area">
        <div id="scenario-image" class="scenario-image-placeholder">
            <div class="image-caption"></div>
        </div>
        <div id="scenario-description" class="scenario-description"></div>
        <div id="choices" class="choices-container">
            <!-- Buttons will be injected here -->
        </div>
        <div id="result" class="result-message"></div>
    </div>

    <div id="end-message" class="end-message" style="display:none;"></div>
    <div class="loading-indicator" style="display:none;"></div>

</div>

<style>
/* כללי */
body {
    background-color: #e8e4d9; /* רקע בצבע נייר ישן */
    color: #333;
    line-height: 1.6;
}

.interactive-container {
    font-family: 'Arial', sans-serif;
    max-width: 700px;
    margin: 30px auto;
    padding: 25px;
    border: 1px solid #a09b8d;
    border-radius: 10px;
    background-color: #f5f3ed; /* רקע מעט בהיר יותר למיכל */
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
    text-align: center;
    position: relative; /* למיקום מוחלט של אינדיקטור טעינה */
}

.app-header {
    margin-bottom: 20px;
    border-bottom: 2px solid #d3cec4;
    padding-bottom: 15px;
}

.app-title {
    color: #4a453c;
    font-size: 1.8em;
    margin-bottom: 10px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

/* אזור סטטיסטיקות */
.stats-bar {
    display: flex;
    justify-content: space-around;
    font-size: 1em;
    color: #555;
}

.stat-item {
    display: flex;
    align-items: center;
    gap: 5px;
}

.stat-label {
    font-weight: bold;
}

.stat-value {
    font-size: 1.3em;
    font-weight: bold;
    transition: color 0.5s ease, transform 0.3s ease; /* אנימציית שינוי צבע והגדלה קלה */
}

.stat-item.risk-stat .stat-value { color: #c0392b; } /* אדום לסיכון */
.stat-item.progress-stat .stat-value { color: #27ae60; } /* ירוק להתקדמות */

/* שינוי צבע רמת סיכון/הישגים */
.risk-level { color: #c0392b; font-weight: bold; }
.progress-level { color: #27ae60; font-weight: bold; }
.risk-level.low { color: #27ae60; }
.risk-level.medium { color: #f39c12; }
.risk-level.high { color: #c0392b; }

.progress-level.start { color: #7f8c8d; }
.progress-level.some { color: #f39c12; }
.progress-level.good { color: #27ae60; }
.progress-level.excellent { color: #1e8449; }
.progress-level.setback { color: #c0392b; }


/* אזור תרחיש */
.scenario-area {
    margin-top: 20px;
    padding-top: 20px;
    border-top: 1px dashed #d3cec4;
}

.scenario-image-placeholder {
    width: 90%;
    height: 150px; /* גובה קבוע לתצוגה אחידה */
    margin: 0 auto 20px auto;
    background-color: #dcdcdc; /* צבע רקע לתחליף תמונה */
    background-image: repeating-linear-gradient(45deg, #e8e8e8, #e8e8e8 10px, #dcdcdc 10px, #dcdcdc 20px); /* טקסטורה עדינה */
    border: 2px dashed #a09b8d;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-style: italic;
    color: #666;
    overflow: hidden; /* לוודא שהכיתוב לא גולש */
    position: relative; /* למיקום הכיתוב */
}

.scenario-image-placeholder .image-caption {
    position: absolute;
    bottom: 10px;
    left: 10px;
    right: 10px;
    background-color: rgba(255, 255, 255, 0.7); /* רקע לבן שקוף לכיתוב */
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 0.9em;
    text-align: left;
    color: #333;
}


.scenario-description {
    margin-bottom: 25px;
    font-size: 1.15em;
    min-height: 80px; /* Ensure space even if description is short */
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    opacity: 1; /* יתחיל שקוף וייכנס עם אנימציה */
    transform: translateY(0);
    transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.scenario-description.fade-out {
     opacity: 0;
     transform: translateY(-20px);
}


/* אפשרויות בחירה */
.choices-container {
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px; /* מרווח גדול יותר בין כפתורים */
}

.choices-container button {
    padding: 12px 20px;
    font-size: 1.1em;
    cursor: pointer;
    border: none; /* הסרת מסגרת ברירת מחדל */
    border-radius: 6px;
    background-color: #6d5c4f; /* צבע כפתור דמוי-נייר */
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    text-align: center;
    display: block; /* ודא שכפתורים תופסים רוחב מלא בגלל flex-direction column */
    width: 100%; /* ודא שכפתורים תופסים רוחב מלא */
}

.choices-container button:hover {
    background-color: #5a4c40;
    transform: translateY(-2px); /* אפקט ריחוף קל */
    box-shadow: 3px 3px 7px rgba(0, 0, 0, 0.3);
}

.choices-container button:active {
    background-color: #45382e;
    transform: translateY(0); /* חזרה למקום */
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
}

/* הודעת תוצאה */
.result-message {
    margin-top: 15px;
    padding: 10px;
    min-height: 40px; /* Ensure space */
    color: #4a453c;
    font-size: 1.1em;
    opacity: 0; /* יתחיל שקוף וייכנס עם אנימציה */
    transform: translateY(20px);
    transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    font-style: italic; /* הדגשה קלה */
}

.result-message.visible {
     opacity: 1;
     transform: translateY(0);
}


/* הודעת סיום משחק */
.end-message {
    margin-top: 30px;
    padding: 20px;
    border-radius: 8px;
    font-size: 1.3em;
    font-weight: bold;
    text-align: center;
    animation: fadeIn 1s ease-out; /* אנימציית הופעה */
}

.end-message.success {
    border: 2px solid #27ae60;
    background-color: #e9f5ee;
    color: #1a5225;
}

.end-message.failure {
    border: 2px solid #c0392b;
    background-color: #fae5e4;
    color: #641e16;
}

.end-message:not(.success):not(.failure) {
    border: 2px solid #7f8c8d;
    background-color: #ebedef;
    color: #34495e;
}


/* אינדיקטור טעינה (למעבר בין תרחישים) */
.loading-indicator {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(245, 243, 237, 0.9); /* כיסוי שקוף למחצה */
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.5em;
    color: #4a453c;
    z-index: 10; /* לוודא שהוא מעל שאר התוכן */
}

.loading-indicator::after {
    content: '...פעולה בתהליך...'; /* טקסט או אנימציה פשוטה */
     animation: pulse 1.5s infinite ease-in-out; /* אנימציית פעימה */
}

@keyframes pulse {
    0% { opacity: 0.5; }
    50% { opacity: 1; }
    100% { opacity: 0.5; }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}


/* הסבר היסטורי */
#toggle-explanation {
    display: block;
    margin: 30px auto 20px auto;
    padding: 12px 25px;
    font-size: 1em;
    cursor: pointer;
    border: 1px solid #a09b8d;
    border-radius: 6px;
    background-color: #d3cec4;
    color: #4a453c;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}

#toggle-explanation:hover {
    background-color: #c4bfb6;
    transform: translateY(-2px);
    box-shadow: 3px 3px 7px rgba(0, 0, 0, 0.2);
}

#toggle-explanation:active {
     background-color: #b6b2a9;
    transform: translateY(0);
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
}


#explanation {
    margin-top: 20px;
    padding: 25px;
    border: 1px solid #a09b8d;
    border-radius: 10px;
    background-color: #f5f3ed;
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
    display: none; /* Hidden by default */
    text-align: right; /* ישור לימין לעברית */
}

#explanation h2 {
    margin-top: 10px; /* פחות מרווח למעלה בכניסה לדיב */
    margin-bottom: 15px;
    color: #4a453c;
    border-bottom: 2px solid #d3cec4;
    padding-bottom: 8px;
    font-size: 1.6em;
}

#explanation h3 {
    margin-top: 20px;
    margin-bottom: 10px;
    color: #6d5c4f;
    font-size: 1.3em;
}

#explanation p, #explanation ul {
    line-height: 1.7;
    margin-bottom: 15px;
    color: #333;
}

#explanation ul {
    list-style: disc;
    margin-right: 20px; /* הזחה לימין ברשימות */
    margin-left: 0;
    padding-right: 0;
}

#explanation ul li {
    margin-bottom: 8px;
}

</style>

<button id="toggle-explanation">הצג רקע והסבר היסטורי</button>

<div id="explanation">
    <h2>ההימור הגדול: המחתרת הצרפתית במלחמת העולם השנייה</h2>

    <h3>רקע היסטורי: צרפת תחת כיבוש נאצי (1940-1944)</h3>
    <p>לאחר התבוסה המהירה לצבא הגרמני במאי-יוני 1940, צרפת האדירה נפלה על ברכיה. היא חולקה לשני אזורים עיקריים: אזור כבוש בצפון ובמערב (כולל פריז ההמומה) שנשלט ישירות על ידי מכונת המלחמה הנאצית, ואזור דרומי שכונה "האזור החופשי" עם ממשלה צרפתית משתפת פעולה, ממשלת וישי, שבסיסה בעיר וישי, בראשות המרשל אנרי פיליפ פטן, גיבור מלחמת העולם הראשונה שהפך לסמל השפלות. ממשלת וישי, כפופה לברלין, שיתפה פעולה ברמה רחבה, כולל ברדיפת יהודים, קומוניסטים וכל מי שנחשד כמתנגד למשטר החדש.</p>

    <h3>"לה רזיסטאנס" (La Résistance): לידתה של תנועת התקווה והמאבק</h3>
    <p>בתגובה לכיבוש המשפיל ולבגידת ממשלת וישי, החלו לצוץ ניצנים של התנגדות. "לה רזיסטאנס" לא הייתה גוף אחד ומאוחד בתחילתה, אלא פסיפס מבוזר של ארגונים וקבוצות מחתרתיות שקמו ספונטנית ברחבי הארץ. היא כללה אנשים מכל שדרות החברה והקשת הפוליטית: קומוניסטים, סוציאליסטים, ליברלים, שמרנים, אנשי דת, אינטלקטואלים, פועלים, איכרים, ופשוט אזרחים שסירבו להשלים עם המצב. מטרותיה היו ברורות: שחרור צרפת מהעול הנאצי, הפלת משטר הבוגדים בווישי, ושיקום הכבוד הלאומי והדמוקרטיה.</p>

    <h3>מגוון פעולות בצללים: הכלים של המחתרת</h3>
    <p>המאבק התנהל במישורים רבים, כולם כרוכים בסיכון חיים מיידי:</p>
    <ul>
        <li><strong>מודיעין יקר מפז:</strong> איסוף מדוקדק של מידע על כוחות האויב, תנועות צבא, ביצורים (כמו החומה האטלנטית), מורל החיילים הגרמנים ועוד. מידע זה, שהוברח לבעלות הברית בבריטניה, היה חיוני לתכנון פלישת יום ה-D.</li>
        <li><strong>חבלה אסטרטגית:</strong> פגיעה ממוקדת בתשתיות החיוניות למאמץ המלחמתי הגרמני: מסילות ברזל, גשרים, קווי תקשורת, מפעלים שעבדו עבור הגרמנים. כל עצירה של רכבת אספקה, כל פגיעה בתקשורת, הייתה ניצחון קטן בקרב הגדול.</li>
        <li><strong>סיוע ותמיכה:</strong> הענקת מקלט והסתר לטייסים של בעלות הברית שמטוסיהם הופלו, סיוע למרגלים שהוצנחו, ובשלבים המאוחרים יותר – לחימה לצד צבאות השחרור.</li>
        <li><strong>מבצעי הצלה נועזים:</strong> הסתרת יהודים שנרדפו על ידי הגרמנים ומשטר וישי, הסתרת אנשי מחתרת נרדפים, טייסי בעלות הברית. המבצעים כללו לעיתים קרובות זיוף מסמכים - תעודות זהות, אישורי מעבר - כדי לאפשר לאנשים להימלט.</li>
        <li><strong>הפצת האמת:</strong> הדפסה והפצה חשאית של עיתונים, עלונים וסיסמאות מחתרתיות. אלה היוו את ה"חדשות" האמיתיות, חשפו את שקרי התעמולה הגרמנית והוישאית, וקראו לציבור להצטרף למאבק או לפחות לא לשתף פעולה.</li>
    </ul>

    <h3>חיים על הקצה: האתגרים העצומים</h3>
    <p>הפעילות במחתרת הייתה מסע מתמיד בין חיים למוות. האתגרים היו בלתי נגמרים:</p>
    <ul>
        <li><strong>האויב הנאצי והגסטאפו:</strong> כוחות הביטחון הגרמנים, ובראשם הגסטאפו הידוע לשמצה, הפעילו רשת מרגלים ובולשים ונקטו שיטות חקירה אכזריות (עינויים) כדי לחשוף את רשתות המחתרת. לכידה כמעט תמיד הובילה למאסר, עינויים, ולרוב - להוצאה להורג או לשליחה למחנות מוות.</li>
        <li><strong>בגידה מבית: משטר וישי ומשתפי הפעולה (המיליס):</strong> לא רק הגרמנים היו האיום. משטר וישי הקים כוח משטרה ומיליציה (Milice) שהיו צרפתים ששיתפו פעולה באופן פעיל עם הגרמנים בלכידת אנשי מחתרת ורדיפת יהודים. לרוב, הם היו אף אכזריים יותר מהגרמנים בניסיונם להוכיח נאמנות.</li>
        <li><strong>צורך מוחלט בסודיות:</strong> עקרון "תאים" קטנים ומבודדים היה חיוני. חשיפה של אדם אחד יכלה להוביל לנפילת רשת שלמה כמו מגדל קלפים. אמון היה מטבע עובר לסוחר, אך גם הדבר המסוכן ביותר שכן בגידה הייתה עונשה מוות.</li>
        <li><strong>מחסור תמידי:</strong> כלי נשק, תחמושת, כסף, מזון, ציוד רפואי, ומקומות מסתור בטוחים - הכל היה במחסור חמור. המחתרת נסמכה על גניבה, תרומות (לעיתים תרומות בכפייה), וסיוע מוצנח מבעלות הברית שהגיע בטפטופים.</li>
        <li><strong>פחד יומיומי:</strong> החשש ממעקב, מלשינים, מעצרים אקראיים, או פעולות תגמול נגד אוכלוסייה אזרחית בעקבות פעולות מחתרת - היה נוכח בכל רגע.</li>
    </ul>

    <h3>אחדות הכוחות: המאבק לאיחוד</h3>
    <p>מורכבותה וביזורה של ההתנגדות הקשו על התיאום והאפקטיביות. שארל דה גול, מנהיג "צרפת החופשית" שפעל מלונדון, ראה חשיבות עליונה באיחוד הכוחות תחת פיקוד אחד. ז'אן מולן, דמות מיתולוגית במחתרת, נשלח על ידו לצרפת ופעל בנחישות, תוך סיכון עצום, לאחד את הרשתות השונות תחת מועצה אחת (Conseil National de la Résistance - CNR) שהכירה בדה גול כמנהיג. הצלחתו, על אף שנתפס ועונה למוות על ידי הגסטאפו, הייתה מרכיב קריטי בהפיכת המחתרת לכוח צבאי ומדיני משמעותי.</p>

    <h3>דילמות מוסריות: קבלת החלטות הרות גורל</h3>
    <p>הפעילות המחתרתית אילצה את אנשיה להתמודד עם דילמות מוסריות נוראיות: האם לבצע חבלה שיודעים שתסכן אזרחים חפים מפשע? את מי להסתיר ולהציל כשאין מספיק מקום או משאבים? האם להוציא להורג מלשינים או משתפי פעולה שחשיפתם עלולה להרוס רשת שלמה? השימוש באלימות, גם נגד צרפתים אחרים, היה חלק אכזרי מהמציאות.</p>

    <h3>סודיות ותקשורת: עורק החיים של הרשת</h3>
    <p>שמירה על סודיות הייתה תנאי קיום בסיסי. שימוש בשמות קוד (פסבדונים), כתובות מסתור (Boîtes aux lettres), ומגוון דרכי תקשורת סמויות (פתקים בתוך חפצים, מסרים מוצפנים, שימוש במשדרי רדיו חשאיים שנקלטו בלונדון) היו עמוד השדרה של הרשת. כל תקשורת נתפסת יכלה לחשוף חלקים גדולים ממנה. רשתות אמינות של שליחים היו חיוניות להעברת מידע פנים-צרפתי ולבריטניה.</p>

    <h3>השפעת ההתנגדות: יותר מסתם סיוע צבאי</h3>
    <p>למרות הקשיים העצומים והמחיר הכבד בנפש, ההתנגדות הצרפתית מילאה תפקיד מכריע. היא סיפקה מודיעין קריטי לבעלות הברית, ביצעה פעולות חבלה ששיבשו את התנועה הגרמנית לקראת הפלישה לנורמנדי ולאחריה. לאחר יום ה-D, כוחות ההתנגדות המאוחדים (Forces Françaises de l'Intérieur - FFI) הפכו לכוח גרילה יעיל, תקפו שיירות גרמניות, שחררו ערים ועיירות רבות עוד לפני הגעת צבאות בעלות הברית, וסייעו לכוחות המשחררים בהכרעת האויב. מעבר לתרומה הצבאית, ההתנגדות שימרה את הכבוד הלאומי הצרפתי, הוכיחה לעולם שצרפת לא נכנעה כליל, והבטיחה שבסוף המלחמה, צרפת תעמוד לצד המנצחות ותשתתף בבניית הסדר העולמי החדש, ולא רק כמדינה משוחררת על ידי אחרים.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const scenarios = [
        {
            description: "אתם בבית המסתור שלכם בפריז. לילה קר, שנת 1943. דפיקה חרישית בדלת האחורית. מדובר באדם זר, מוכר לרשת רק בכינוי הקוד שלו, 'שועל', כמקור מידע מהימן ובעל ערך מבית הממשל הוישאי, אך מעולם לא פגשתם אותו קודם. הוא נראה מבוהל, בגדיו מרופטים והוא מבקש מקלט מיידי ללילה אחד בלבד. הישארותו מסוכנת לכם ולרשת כולה - אם הוא נרדף, אתם מסתכנים בחשיפה. אם הוא בוגד, אתם בסכנה מיידית.",
            image: "דלת עץ ישנה, צללית אדם מחוץ לזגוגית קטנה",
            choices: [
                {
                    text: "פיתחו את הדלת בזהירות, הכניסו אותו והסתירו אותו. האמון ברשת קודם לכל חשש.",
                    result: "הכנסתם את 'שועל'. הלילה עבר במתח רב, אך בשקט מוחלט. בבוקר, לפני שעזב בחשאי, הוא העביר לכם מסמכים ומידע קריטי על תנועות צבא גרמניות ועל תוכניות מעצר וישאיות. הסיכון הגדול השתלם והניב פרי אסטרטגי.",
                    riskChange: 2, // Increased risk significantly
                    progressChange: 4, // Very significant progress from high-value intel
                    nextScenario: 1
                },
                {
                    text: "סרבו לפתוח את הדלת בטענה שזה מסוכן מדי כרגע. אולי תנסו ליצור קשר בדרך אחרת.",
                    result: "סירבתם לפתוח את הדלת. 'שועל' נאלץ למצוא מקלט אחר בבהילות. אולי הצלתם את עצמכם הפעם מסיכון מיידי, אך איבדתם הזדמנות קריטית למידע יקר ערך. קולות ייאוש שנשמעו מהדלת לפני שהתרחק רדפו אתכם כל הלילה. נוצר סדק קטן באמון ברשת.",
                    riskChange: -1, // Reduced immediate risk slightly
                    progressChange: -2, // Significant setback/lost opportunity
                    nextScenario: 1
                }
            ]
        },
        {
            description: "עליכם להעביר מסר מוצפן, הוראה מפקדת המחתרת בלונדון, לאיש קשר מרכזי בעיירה סמוכה. המסר מודפס על נייר דק ומוסתר בתוך כיכר לחם טרי. בדרך לעיירה, המרוחקת כ-30 ק\"מ, יש מחסום דרכים גרמני ידוע לשמצה, המוצב על הגשר הראשי בכניסה לעיירה. הגרמנים שם ידועים בקפדנותם ובאכזריותם. אתם רכובים על אופניים בלויי שמש, מנסים להיראות כמו איכר תמים.",
            image: "מחסום גרמני מאולתר, חייל גרמני במדים בודק תעודות של עוברים ושבים ליד הגשר",
            choices: [
                {
                    text: "נסו לעבור דרך המחסום כרגיל, בחזות תמימה לחלוטין, מקווים שהלחם לא יעורר חשד ושתעודותיכם יראו תקינות.",
                    result: "ניגשתם למחסום בדפיקות לב מואצות. חייל גרמני עצר אתכם, בדק את התעודות שזייפתם במיומנות, ועיניו נחו על כיכר הלחם. הוא שקל לרגע, אך לבסוף הניף יד לאישור מעבר. הרגעים היו נצח, אך הצלחתם לעבור ולהעביר את המסר הקריטי בזמן.",
                    riskChange: 3, // Very high risk, but successful
                    progressChange: 3, // Mission accomplished well
                    nextScenario: 2
                },
                {
                    text: "נסו לעקוף את המחסום. יש דרך עפר עוקפת דרך יער סמוך, אך היא ארוכה יותר, בוצית, וכוללת חציית נחל רדוד. לא בטוח שתצליחו עם האופניים והסיכון להיתקל בסיור גרמני קטן או משתפי פעולה עדיין קיים.",
                    result: "בחרתם בעקיפה. המסלול דרך היער היה קשה ומפרך. האופניים התקלקלו באמצע הדרך, ונאלצתם ללכת ברגל, כשהלחם מתחיל להתפורר קלות. הגעתם לעיירה כשהחושך יורד, באיחור ניכר, אך ללא מפגש עם הגרמנים. המסר הגיע, אך מאוחר יותר מהמתוכנן, מה שגרם לשיבושים קטנים בתיאום הרשת.",
                    riskChange: 1, // Moderate risk from alternative route/travel
                    progressChange: 1, // Less progress due to delay and minor issues
                    nextScenario: 2
                },
                {
                    text: "וותרו על המשימה להיום. הסיכון נראה גבוה מדי, אולי ניתן להעביר את המסר בדרך אחרת ביום אחר, גם אם זה יקח יותר זמן.",
                    result: "הסתובבתם חזרה הביתה, דחיתם את המשימה למועד בטוח יותר. המסר הקריטי לא הגיע. ייתכן שהימנעתם מסיכון מיידי, אך איבדתם הזדמנות מכרעת ותיאום עם לונדון השתבש. תחושת כישלון קלה צובעת את היום.",
                    riskChange: -2, // Reduced immediate risk significantly
                    progressChange: -3, // Significant setback - mission failed
                    nextScenario: 2
                }
            ]
        },
        {
            description: "אתם וחבריכם מתא המחתרת מתכננים מבצע חבלה משמעותי: פיצוץ קטע ממסילת רכבת אסטרטגית המשמשת את הגרמנים להעברת שריון ואספקה לחזית. אך לצערכם, המסילה עוברת במרחק קצר מקבוצת בתים בכפר קטן ועני. פעולת חבלה במיקום זה עלולה לסכן ישירות את התושבים המקומיים ואף להביא לפעולת תגמול גרמנית נוראה נגדם - מעצרים המוניים, הוצאות להורג אקראיות, ואף שריפת בתים. הדילמה המוסרית קורעת.",
            image: "קרונות רכבת על מסילה, ברקע בתי כפר קטנים ליד עצים",
            choices: [
                {
                    text: "בצעו את החבלה כמתוכנן במיקום זה. המטרה הצבאית - פגיעה באספקה גרמנית חיונית - חשובה יותר מסיכון התושבים. זו המלחמה.",
                    result: "הפעלתם את מטעני החבלה בחסות החשיכה. הרכבת הגרמנית יצאה מפסיה ברעש אימים, נזק כבד נגרם למטען ולקרונות. אך, כפי שחששתם, הדף הפיצוץ פגע גם בכמה בתים סמוכים וחייל גרמני ששמר במקום נהרג. הגרמנים הגיעו בזעם עצום, ערכו חיפושים אכזריים בכפר, איימו על התושבים וביצעו מעצרים אקראיים, אך נמנעו מפעולת תגמול כוללת הפעם. ההישג הצבאי גדול, אך מלווה במחיר כבד ובפחד נורא אצל התושבים.",
                    riskChange: 4, // Very high risk due to reprisal potential
                    progressChange: 4, // Very significant military impact
                    nextScenario: 3
                },
                {
                    text: "החליטו לוותר על החבלה במיקום זה. הסיכון לחיי אזרחים חפים מפשע ולישוב כולו גבוה מדי ובלתי מתקבל על הדעת. הערכים קודמים למטרה הצבאית הזו.",
                    result: "ויתרתם על הפעולה המתוכננת במיקום המסוכן. תושבי הכפר נותרו בטוחים וניצלו מאימת התגמול הגרמני. אך הרכבת הגרמנית המשיכה בדרכה ללא הפרעה, וההזדמנות לפגוע באספקה חיונית אבדה. תחושת החמצה וחוסר אונים מלווה אתכם.",
                    riskChange: -2, // Reduced risk significantly
                    progressChange: -1, // Moderate setback - lost opportunity
                    nextScenario: 3
                },
                 {
                    text: "חפשו יעד חבלה אלטרנטיבי, מרוחק מספיק מאוכלוסייה אזרחית, גם אם זה יקח יותר זמן ויהיה קשה יותר מבחינה לוגיסטית.",
                    result: "יצאתם לסקור אזורים אחרים למסילות רכבת. זה לקח כמה ימים מסוכנים של סיורים חשאיים, אך מצאתם קטע מסילה אחר, פחות מרכזי, אך רחוק מספיק מכל יישוב. החבלה שביצעתם שם הייתה פחות אפקטיבית מבחינה צבאית מהתוכנית המקורית, אך היא בוצעה ללא סיכון מידי לאזרחים. הישג חלקי, ללא פגיעה בערכים.",
                    riskChange: 1, // Moderate risk from scouting/planning
                    progressChange: 2, // Moderate military impact
                    nextScenario: 3
                }
            ]
        },
         {
            description: "סיימתם סדרת פעולות והחלטות הרות גורל. זהו סוף מסעכם בפרק זה של ההתנגדות. נותרה רק השאלה - האם פעולותיכם קידמו את המאבק או סיכנו את הרשת עד כדי נקודת שבירה?",
            image: "דגל צרפת חופשית מתנופף ברוח",
            choices: [], // No choices at the end
            result: "", // Result displayed in end message
            riskChange: 0,
            progressChange: 0,
            nextScenario: -1 // Indicates end
        }
    ];

    let currentScenarioIndex = 0;
    let totalRisk = 0;
    let totalProgress = 0;

    const scenarioDescriptionElement = document.getElementById('scenario-description');
    const scenarioImageElement = document.getElementById('scenario-image');
    const imageCaptionElement = scenarioImageElement.querySelector('.image-caption');
    const choicesElement = document.getElementById('choices');
    const resultElement = document.getElementById('result');
    const totalRiskElement = document.getElementById('total-risk');
    const totalProgressElement = document.getElementById('total-progress');
    const riskLevelElement = document.querySelector('.risk-level');
    const progressLevelElement = document.querySelector('.progress-level');
    const endMessageElement = document.getElementById('end-message');
    const loadingIndicator = document.querySelector('.loading-indicator');
    const interactiveContainer = document.querySelector('.interactive-container');


    function updateStatsDisplay() {
        // Animate stats numbers
        animateStat(totalRiskElement, parseInt(totalRiskElement.textContent || '0'), totalRisk);
        animateStat(totalProgressElement, parseInt(totalProgressElement.textContent || '0'), totalProgress);

        // Update risk level text and color
        if (totalRisk <= 1) {
            riskLevelElement.textContent = 'נמוכה';
            riskLevelElement.className = 'risk-level low';
        } else if (totalRisk <= 4) {
            riskLevelElement.textContent = 'בינונית';
             riskLevelElement.className = 'risk-level medium';
        } else {
            riskLevelElement.textContent = 'גבוהה';
             riskLevelElement.className = 'risk-level high';
        }

        // Update progress level text and color
         if (totalProgress <= 0) {
            progressLevelElement.textContent = 'התחלה';
            progressLevelElement.className = 'progress-level start';
        } else if (totalProgress <= 3) {
            progressLevelElement.textContent = 'התקדמות קלה';
             progressLevelElement.className = 'progress-level some';
        } else if (totalProgress <= 6) {
            progressLevelElement.textContent = 'התקדמות טובה';
             progressLevelElement.className = 'progress-level good';
        } else {
             progressLevelElement.textContent = 'התקדמות משמעותית';
             progressLevelElement.className = 'progress-level excellent';
        }
         if (totalProgress < 0) { // Handle negative progress explicitly
             progressLevelElement.textContent = 'נסיגה';
             progressLevelElement.className = 'progress-level setback';
         }
    }

    // Simple animation for stat numbers
    function animateStat(element, start, end) {
        const duration = 600; // milliseconds
        const range = end - start;
        const startTime = performance.now();

        function step(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const currentValue = Math.floor(start + range * progress);
            element.textContent = currentValue;

            if (progress < 1) {
                requestAnimationFrame(step);
            } else {
                 element.textContent = end; // Ensure final value is set
            }
        }
         // Trigger a slight visual emphasis on change
        element.style.transform = 'scale(1.1)';
        requestAnimationFrame(step);
        setTimeout(() => { element.style.transform = 'scale(1)'; }, duration);

    }


    function displayScenario(index) {
         // Hide previous content with fade-out animation
        if (currentScenarioIndex !== null && scenarios[currentScenarioIndex]) {
             scenarioDescriptionElement.classList.add('fade-out');
             resultElement.classList.remove('visible'); // Fade out previous result
        }


        // Set loading indicator
        loadingIndicator.style.display = 'flex';
        choicesElement.innerHTML = ''; // Clear choices immediately

        // Wait for fade-out, then load new content
        setTimeout(() => {
            loadingIndicator.style.display = 'none'; // Hide loading
            scenarioDescriptionElement.classList.remove('fade-out'); // Reset class for next animation

            if (index < 0 || index >= scenarios.length) {
                endGame();
                return;
            }

            currentScenarioIndex = index;
            const scenario = scenarios[currentScenarioIndex];

            // Update content
            scenarioDescriptionElement.textContent = scenario.description; // Use textContent to avoid issues with final HTML
            imageCaptionElement.textContent = scenario.image; // Display image text as caption

            resultElement.textContent = ''; // Clear previous result

            if (scenario.choices.length > 0) {
                 scenario.choices.forEach((choice, choiceIndex) => {
                    const button = document.createElement('button');
                    button.textContent = choice.text;
                    button.addEventListener('click', () => handleChoice(choiceIndex));
                    choicesElement.appendChild(button);
                });
                endMessageElement.style.display = 'none'; // Hide end message if not end screen
                 document.getElementById('stats').style.display = 'flex'; // Show stats bar
            } else {
                 // If no choices, it's the end scenario
                 endGame();
                 return;
            }

            updateStatsDisplay();

             // Animate in new content
             scenarioDescriptionElement.style.opacity = '0';
             scenarioDescriptionElement.style.transform = 'translateY(20px)';
             setTimeout(() => {
                  scenarioDescriptionElement.style.opacity = '1';
                  scenarioDescriptionElement.style.transform = 'translateY(0)';
             }, 50); // Small delay to ensure display property is set before transition

        }, 800); // Wait for fade-out animation duration
    }

    function handleChoice(choiceIndex) {
        const scenario = scenarios[currentScenarioIndex];
        const choice = scenario.choices[choiceIndex];

         // Disable buttons to prevent multiple clicks
        Array.from(choicesElement.children).forEach(button => button.disabled = true);
        Array.from(choicesElement.children).forEach(button => button.style.opacity = '0.5'); // Visual cue


        totalRisk += choice.riskChange;
        totalProgress += choice.progressChange;

        resultElement.textContent = choice.result;
        resultElement.classList.add('visible'); // Animate in result
        updateStatsDisplay();

        // Move to the next scenario after a brief delay to allow reading the result and seeing stats change
        setTimeout(() => {
            displayScenario(choice.nextScenario);
        }, 2000); // 2 second delay before transitioning to next scenario
    }

    function endGame() {
        // Fade out current elements
        scenarioDescriptionElement.classList.add('fade-out');
        scenarioImageElement.style.opacity = '0';
        choicesElement.style.opacity = '0';
        resultElement.classList.remove('visible');

        // Wait for fade out, then show end message
        setTimeout(() => {
            scenarioDescriptionElement.style.display = 'none';
            scenarioImageElement.style.display = 'none';
            choicesElement.style.display = 'none';
            resultElement.style.display = 'none';
            document.getElementById('stats').style.display = 'none'; // Hide stats bar at the end

            endMessageElement.style.display = 'block';
             endMessageElement.style.opacity = '0'; // Start faded out

            let message = `סוף הסימולציה. מסעכם בצללים הגיע לסיומו.`;

            // Determine outcome based on final stats
            if (totalRisk > totalProgress * 2.5 && totalRisk > 5) { // Higher threshold for clear failure
                message += `<br><strong>תוצאה: חשיפה!</strong><br>הסיכון המצטבר (${totalRisk}) גבר על ההישגים (${totalProgress}). כנראה שפעולותיכם הנועזות, או אלו של חבריכם, גרמו לחשיפת התא או הרשת. המחיר של חופש אינו נמדד רק בהצלחות, אלא גם בזהירות. לרוע המזל, נלכדתם או שהייתם עדים לקריסת חלק מהרשת.`;
                endMessageElement.className = 'end-message failure';
            } else if (totalProgress >= totalRisk * 1.8 && totalProgress > 4) { // Higher threshold for clear success
                 message += `<br><strong>תוצאה: הצלחה יחסית!</strong><br>הישגיכם (${totalProgress}) עלו משמעותית על הסיכון שצברתם (${totalRisk}). פעלתם בתבונה, תרמתם רבות למאבק, וסייעתם לקידום שחרור צרפת תוך ניהול סיכונים סביר יחסית. מעשיכם עשויים בהחלט להציל חיים ולקצר את הכיבוש. קומץ אנשים כמוכם הם עמוד השדרה של ההתנגדות.`;
                 endMessageElement.className = 'end-message success';
            } else { // Mixed or neutral outcome
                 message += `<br><strong>תוצאה: מסע מורכב.</strong><br>סיימתם את הפרק הזה של פעילותכם המחתרתית עם הישגים צנועים יחסית (${totalProgress}) וסיכון מצטבר לא מבוטל (${totalRisk}). פעלתם תחת לחץ ודילמות קשות. השפעתכם על המאבק הייתה מעורבת - היו הצלחות קטנות לצד כישלונות או סיכונים מיותרים. הדרך לשחרור עוד ארוכה ומסוכנת.`;
                 endMessageElement.className = 'end-message'; // Neutral styling
            }

            endMessageElement.innerHTML = message; // Use innerHTML to allow line breaks

            // Animate in the end message
            setTimeout(() => {
                endMessageElement.style.opacity = '1';
            }, 50);


        }, 800); // Wait for previous elements to fade out
    }

    // Toggle explanation visibility
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    toggleButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleButton.textContent = 'הסתר רקע והסבר היסטורי';
        } else {
            explanationDiv.style.display = 'none';
            toggleButton.textContent = 'הצג רקע והסבר היסטורי';
        }
    });


    // Start the game
     currentScenarioIndex = 0; // Ensure starting from 0
    displayScenario(currentScenarioIndex);
});
</script>
---
```