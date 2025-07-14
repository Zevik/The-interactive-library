---
title: "משימה במיקרוביום: תכנון מסע לגילוי"
english_slug: microbiome-mission-research-planning
category: "ביולוגיה"
tags: ["מיקרוביום", "מחקר מדעי", "ביולוגיה", "בריאות", "תכנון ניסוי"]
---
<div class="mission-container">
    <h1>🚀 משימה במיקרוביום: תכנון מסע לגילוי</h1>
    <p class="intro-text">צאו למסע מדעי מרתק לתוך העולם הפנימי שלנו! בתוך כל אחד ואחת מאיתנו שוכנת אקולוגיה מדהימה של מיליארדי מיקרואורגניזמים - המיקרוביום. איך מדענים פורצים את דרכם לחשוף את הסודות של העולם המיקרוסקופי הזה? המשימה שלכם: לתכנן ניסוי פורץ דרך לחקר המיקרוביום האנושי. כל החלטה תשפיע על התקציב, הזמן, ואיכות התוצאות של המשימה!</p>

    <div id="app" class="mission-app">
        <div id="status" class="mission-status">
            <h2>📊 דשבורד משימה</h2>
            <p> תקציב התחלתי: $<span id="initial-budget">100,000</span></p>
            <p> זמן שהוקצב: <span id="initial-time">12</span> חודשים</p>
            <div class="status-breakdown">
                 <p> עלות משימה מצטברת: $<span id="current-cost-added" class="status-cost">0</span></p>
                 <p> זמן משימה נוסף: <span id="current-time-added" class="status-time">0</span> חודשים</p>
            </div>
        </div>

        <div id="steps-container" class="steps-container">
            <div id="step-1" class="step active">
                <h3>🎯 שלב 1: הגדרת יעד - אוכלוסיית מחקר ושאלת מפתח</h3>
                <p>את מי נחקור? בחירה זו תשפיע על מורכבות גיוס המשתתפים וההוצאות.</p>
                <div class="choice-group" data-step="1">
                    <label class="choice-label"><input type="radio" name="population" value="healthy" data-cost="0" data-time="0" data-population="אנשים בריאים (קבוצת בקרה בריאים)"> <span class="choice-text">אנשים בריאים בלבד</span> <span class="choice-meta">(פשוט לגיוס, עלות וזמן מינימליים)</span></label>
                    <label class="choice-label"><input type="radio" name="population" value="diseased" data-cost="15000" data-time="1.5" data-population="חולים במצב ספציפי + קבוצת בקרת בריאים"> <span class="choice-text">חולים במצב ספציפי (למשל, סוכרת / מחלת מעי) + בקרת בריאים</span> <span class="choice-meta">(גיוס מורכב יותר, עלות וזמן נוספים משמעותיים)</span></label>
                </div>
            </div>

            <div id="step-2" class="step">
                <h3>🔬 שלב 2: בחירת שדה איסוף - אתר דגימה ושיטה</h3>
                <p>מאין נאסוף את הדגימות? בחירה זו תשפיע על סוג המיקרוביום הנחקר ועל שיטת האיסוף (פשוטה או פולשנית).</p>
                 <div class="choice-group" data-step="2">
                    <label class="choice-label"><input type="radio" name="sampling" value="gut-stool" data-cost="1000" data-time="0.1" data-site="מעי" data-type="צואה" data-invasiveness="לא פולשנית"> <span class="choice-text">מעי (דגימת צואה)</span> <span class="choice-meta">(הנפוץ ביותר, לא פולשני, מייצג את מיקרוביום המעי)</span></label>
                    <label class="choice-label"><input type="radio" name="sampling" value="skin-swab" data-cost="500" data-time="0.05" data-site="עור" data-type="משטח" data-invasiveness="לא פולשנית"> <span class="choice-text">עור (משטח עור)</span> <span class="choice-meta">(קל לאיסוף, לא פולשני, חקר מיקרוביום העור)</span></label>
                    <label class="choice-label"><input type="radio" name="sampling" value="oral-swab" data-cost="500" data-time="0.05" data-site="פה" data-type="משטח" data-invasiveness="לא פולשנית"> <span class="choice-text">פה (משטח רוק/חניכיים)</span> <span class="choice-meta">(קל לאיסוף, לא פולשני, חקר מיקרוביום הפה)</span></label>
                    <label class="choice-label"><input type="radio" name="sampling" value="gut-biopsy" data-cost="25000" data-time="3" data-site="מעי" data-type="ביופסיה" data-invasiveness="פולשנית"> <span class="choice-text">מעי (ביופסיה - איסוף רקמה אנדוסקופי)</span> <span class="choice-meta">(פולשני, דגימה ישירה מרקמת המעי, עלות וזמן גבוהים במיוחד, דורש אישור אתי מורכב)</span></label>
                 </div>
            </div>

            <div id="step-3" class="step">
                <h3>🧬 שלב 3: פיצוח הקוד - טכנולוגיית ריצוף</h3>
                <p>איך נפענח את הזהות ותפקידי המיקרואורגניזמים בדגימות? בחירה זו תשפיע דרמטית על עלות, זמן ועומק המידע.</p>
                <div class="choice-group" data-step="3">
                    <label class="choice-label"><input type="radio" name="sequencing" value="16S" data-cost="10000" data-time="1" data-resolution="טקסונומי (מינים)" data-datatype="זיהוי מיקרואורגניזמים ושיעורם היחסי"> <span class="choice-text">ריצוף 16S rRNA</span> <span class="choice-meta">(זול ומהיר יחסית, מזהה אילו חיידקים קיימים ובאיזה שכיחות, לא מספק מידע על פונקציות)</span></label>
                    <label class="choice-label"><input type="radio" name="sequencing" value="shotgun" data-cost="60000" data-time="4" data-resolution="טקסונומי ברמת זן + פונקציונלי" data-datatype="זיהוי מדויק יותר של מיקרואורגניזמים ויכולותיהם המטבוליות/פונקציונליות"> <span class="choice-text">ריצוף Shotgun Metagenomic</span> <span class="choice-meta">(יקר וממושך משמעותית, מזהה ברמת זן, כולל מידע על גנים ותפקודים אפשריים)</span></label>
                </div>
            </div>

            <div id="step-4" class="step">
                <h3>👥 שלב 4: כוח הנתונים - גודל המדגם</h3>
                <p>כמה משתתפים יכלול המחקר? בחירה זו תשפיע ישירות על עלות, זמן ועל הכוח הסטטיסטי של המסקנות.</p>
                <div class="choice-group" data-step="4">
                    <label class="choice-label"><input type="radio" name="sample-size" value="small" data-cost="5000" data-time="0.5" data-size="קטן" data-power="נמוך" data-num-samples="20"> <span class="choice-text">מדגם קטן (כ-20 דגימות)</span> <span class="choice-meta">(זול ומהיר, סיכוי נמוך לגלות הבדלים קטנים אך משמעותיים)</span></label>
                    <label class="choice-label"><input type="radio" name="sample-size" value="medium" data-cost="15000" data-time="1.5" data-size="בינוני" data-power="בינוני" data-num-samples="50"> <span class="choice-text">מדגם בינוני (כ-50 דגימות)</span> <span class="choice-meta">(איזון טוב יחסית בין עלות/זמן לכוח סטטיסטי)</span></label>
                    <label class="choice-label"><input type="radio" name="sample-size" value="large" data-cost="30000" data-time="2.5" data-size="גדול" data-power="גבוה" data-num-samples="100"> <span class="choice-text">מדגם גדול (כ-100 דגימות)</span> <span class="choice-meta">(יקר וממושך, סיכוי גבוה יותר לגלות הבדלים משמעותיים, תוצאות אמינות יותר)</span></label>
                </div>
            </div>

            <button id="next-step" class="mission-button">המשך לשלב הבא ➡️</button>
            <button id="show-summary" class="mission-button primary" style="display: none;">סיכום תוכנית המשימה ✨</button>
        </div>

        <div id="summary" class="mission-summary" style="display: none;">
            <h2>✅ סיכום משימה: תוכנית המחקר שלך</h2>
             <p>הנה התוכנית שיצרת למסע גילוי המיקרוביום שלך:</p>

            <div class="summary-section">
                <h3>בחירות מפתח:</h3>
                <p><strong>אוכלוסיית מחקר:</strong> <span id="summary-population"></span></p>
                <p><strong>אתר ושיטת דגימה:</strong> <span id="summary-sampling"></span> (<span id="summary-invasiveness"></span>)</p>
                <p><strong>טכנולוגיית ריצוף:</strong> <span id="summary-sequencing"></span> (רזולוציה: <span id="summary-resolution"></span>)</p>
                <p><strong>גודל מדגם:</strong> <span id="summary-sample-size"></span> (<span id="summary-num-samples"></span> דגימות, כוח סטטיסטי <span id="summary-power"></span>)</p>
            </div>

            <div class="summary-section costs-times">
                <h3>משאבים ולוח זמנים:</h3>
                <p> תקציב התחלתי: $<span id="summary-initial-budget"></span></p>
                <p> עלות כוללת של הבחירות: $<span id="summary-total-cost-added"></span></p>
                <p class="summary-remaining-budget"> תקציב נותר: $<span id="summary-remaining-budget"></span></p>
                <p> זמן התחלתי: <span id="summary-initial-time"></span> חודשים</p>
                <p class="summary-total-time"> זמן נדרש כולל: <span id="summary-total-time-needed"></span> חודשים</p>
            </div>

             <div class="summary-section outcome">
                 <h3>💡 תובנות והשלכות התוכנית:</h3>
                 <p><strong>סוג הנתונים שתקבל:</strong> <span id="summary-data-type"></span></p>
                 <div id="summary-limitations" class="limitations"></div>
             </div>
        </div>
    </div>

    <button id="explanation-toggle" class="mission-button secondary">הצג/הסתר הסבר על מיקרוביום ומחקר</button>

    <div id="explanation" class="explanation-box" style="display: none;">
        <h2>הסבר על מיקרוביום ותכנון מחקר מדעי</h2>
        <p>המיקרוביום האנושי הוא אוסף כל המיקרואורגניזמים (חיידקים, פטריות, וירוסים וארכאה) החיים על ובתוך גופנו. הוא מהווה מערכת אקולוגית מורכבת וחיונית לבריאותנו.</p>
        <h3>חשיבות המיקרוביום לבריאות</h3>
        <ul>
            <li>עיכול מזון וייצור ויטמינים חיוניים.</li>
            <li>הגנה מפני פתוגנים (מחוללי מחלה) על ידי יצירת תחרות והפרשת חומרים מעכבים.</li>
            <li>התפתחות ותפקוד תקין של מערכת החיסון.</li>
            <li>השפעה על תהליכים פיזיולוגיים רבים, כולל מטבוליזם, דלקת, ואפילו על המוח והתנהגות דרך ציר המעי-מוח.</li>
            <li>קשר למגוון רחב של מצבים ומחלות, כולל מחלות מעי דלקתיות, השמנה, סוכרת, אלרגיות, מחלות אוטואימוניות, ואף הפרעות נוירולוגיות ופסיכיאטריות.</li>
        </ul>
        <h3>שאלת מחקר ותהליך תכנון במדעי החיים</h3>
        <p>כל מחקר מדעי מתחיל בשאלת מחקר ברורה וממוקדת. תכנון הניסוי הוא השלב המכריע שבו בונים את הדרך לענות על השאלה בצורה האמינה והיעילה ביותר, תוך התחשבות קפדנית במגבלות משאבים (כסף, זמן, כוח אדם) ושיקולים אתיים.</p>
        <h3>שיקולים מרכזיים בתכנון מחקר מיקרוביום</h3>
        <ul>
            <li><strong>אוכלוסיית מחקר וקבוצות בקרה:</strong> מי המשתתפים במחקר? האם נדרשת קבוצת בקרה (למשל, בריאים להשוואה לחולים)? הגדרה מדויקת חיונית לגיוס ולפרשנות נכונה.</li>
            <li><strong>אתרי דגימה שונים בגוף:</strong> לכל אתר בגוף (מעי, עור, פה, מערכת המין והשתן, ריאות וכו') יש הרכב מיקרוביום ייחודי. בחירת האתר חייבת להיות מותאמת לשאלת המחקר.</li>
            <li><strong>שיטות דגימה (פרוטוקולים, איסוף):</strong> אופן איסוף הדגימה (צואה, משטח, ביופסיה, שטיפה וכו') משפיע על סוג החיידקים שנדגמים ועל מידת הפולשנות. סטנדרטיזציה קפדנית של פרוטוקולי האיסוף והשימור (למשל, הקפאה מהירה) חיונית למניעת שינויים בהרכב המיקרוביום לפני הניתוח.</li>
            <li><strong>טכנולוגיות מעבדה לניתוח המיקרוביום:</strong>
                <ul>
                    <li><strong>ריצוף 16S rRNA:</strong> שיטה פופולרית וזולה יחסית המרצפת גן ספציפי המצוי בחיידקים. משמשת כ"ברקוד" לזיהוי טקסונומי של החיידקים הקיימים בדגימה ושיעורם היחסי. שיטה זו אינה מספקת מידע ישיר על הפונקציות שהחיידקים מבצעים.</li>
                    <li><strong>ריצוף Shotgun Metagenomic:</strong> שיטה מקיפה ויקרה יותר המרצפת את כל מקטעי ה-DNA מכל האורגניזמים בדגימה (חיידקים, פטריות, וירוסים). מספקת זיהוי טקסונומי ברזולוציה גבוהה יותר (עד רמת זן) וכן מידע עשיר על הפוטנציאל המטבולי והפונקציונלי של הקהילה המיקרוביאלית (אילו אנזימים, מסלולים מטבוליים ויכולות אחרות קיימים).</li>
                </ul>
            </li>
            <li><strong>ניתוח נתונים וביואינפורמטיקה:</strong> נתוני מיקרוביום הם עצומים ומורכבים. נדרשים כוח חישוב וכלים ביו-אינפורמטיים מתקדמים לעיבוד הנתונים, זיהוי המיקרואורגניזמים, ניתוח הרכב הקהילות והשוואתן בין קבוצות שונות, וקישור הממצאים לנתונים הקליניים או המאפיינים של המשתתפים.</li>
        </ul>
        <h3>אתגרים ושיקולים אתיים במחקר מיקרוביום</h3>
        <p>אתגרים מרכזיים כוללים את הרעש המובנה בנתונים (שונות ביולוגית וטעויות טכניות), גודל הנתונים העצום, הצורך בסטנדרטיזציה חוצת-מעבדות, ובעיקר הקושי בקביעת סיבתיות (האם שינוי במיקרוביום *גורם* למצב מסוים או שהוא רק *תוצאה* שלו?). שיקולים אתיים חיוניים במיוחד במחקרים הכוללים פרוצדורות פולשניות או איסוף נתונים אישיים רגישים (כמו נתונים בריאותיים, תזונתיים, אורח חיים). נדרשת הסכמה מדעת מלאה ושמירה קפדנית על פרטיות המשתתפים.</p>
        <h3>דוגמאות לתובנות ממחקרי מיקרוביום פורצי דרך</h3>
        <ul>
            <li>גילוי קשרים חזקים בין הרכב מיקרוביום המעי להשמנה, סוכרת מסוג 2 ותנגודת לאינסולין.</li>
            <li>הדגמת ההשפעה המזיקה והממושכת של אנטיביוטיקה על המיקרוביום והקשר לסיכון מוגבר למחלות בהמשך החיים.</li>
            <li>פיתוח טיפולים מבוססי מיקרוביום, כמו השתלת צואה (Fecal Microbiota Transplantation - FMT), שהפכה לטיפול המומלץ לזיהום חוזר בחיידק <em>Clostridioides difficile</em>, מה שמדגים קשר סיבתי ופוטנציאל טיפולי.</li>
            <li>זיהוי "חתימות" מיקרוביאליות במיקרוביום המעי, העור או הפה, הקשורות למצבים מגוונים כמו מחלות דלקתיות כרוניות, אוטיזם, דיכאון, ואף לחיזוי תגובה לטיפולים מסוימים (למשל, תגובה טובה יותר לאימונותרפיה בסרטן).</li>
        </ul>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    :root {
        --primary-color: #007bff;
        --secondary-color: #28a745;
        --accent-color: #ffc107;
        --background-color: #eef2f7;
        --card-background: #ffffff;
        --text-color: #343a40;
        --border-color: #ced4da;
        --warning-color: #dc3545;
        --info-color: #17a2b8;
        --success-color: #28a745;
        --hover-light: #f8f9fa;
    }

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: var(--background-color);
        color: var(--text-color);
    }

    .mission-container {
        max-width: 900px;
        margin: 20px auto;
        padding: 30px;
        background-color: var(--card-background);
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    h1, h2, h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        color: #0056b3;
    }

    .intro-text {
        text-align: center;
        margin-bottom: 30px;
        color: #555;
        font-size: 1.1em;
    }

    .mission-app {
        border: 1px solid var(--border-color);
        padding: 25px;
        border-radius: 8px;
        margin-bottom: 30px;
        background-color: #fefefe;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .mission-status {
        margin-bottom: 25px;
        padding: 18px;
        background-color: #e9ecef;
        border-radius: 5px;
        border: 1px solid #dee2e6;
    }

    .mission-status h2 {
        margin-top: 0;
        color: #0056b3;
        font-size: 1.4em;
        border-bottom: 1px dashed #ced4da;
        padding-bottom: 10px;
        margin-bottom: 10px;
    }

    .status-breakdown {
        display: flex;
        justify-content: space-around;
        gap: 10px;
        flex-wrap: wrap;
    }

    .status-breakdown p {
        margin: 5px 0;
        font-size: 1.1em;
    }

    .status-cost {
        color: var(--warning-color);
        font-weight: bold;
    }
     .status-time {
        color: var(--info-color);
        font-weight: bold;
    }


    .steps-container {
        position: relative; /* Needed for transitions */
    }

    .step {
        border: 1px solid var(--border-color);
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        background-color: var(--card-background);
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
        position: absolute; /* Use absolute positioning to stack steps */
        top: 0;
        left: 0;
        right: 0;
        z-index: 1; /* Ensure active step is on top */
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .step.active {
        display: block; /* Still need block to be visible */
        opacity: 1;
        transform: translateY(0);
        position: static; /* Reset position for active step */
        z-index: 2;
    }

    .step h3 {
        margin-top: 0;
        color: #0056b3;
        font-size: 1.3em;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    .choice-group {
        margin-top: 15px;
    }

    .choice-label {
        display: flex; /* Use flexbox to align text and radio */
        align-items: center;
        margin-bottom: 12px;
        padding: 12px;
        border: 1px solid #eee;
        border-radius: 5px;
        background-color: var(--hover-light);
        cursor: pointer;
        transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out;
    }

    .choice-label:hover {
         background-color: #e9ecef;
         border-color: #ced4da;
    }

    .choice-label input[type="radio"] {
        margin-left: 10px; /* Space out radio button from text */
        transform: scale(1.2); /* Slightly larger radio buttons */
         accent-color: var(--primary-color); /* Color the radio button */
    }

    .choice-label input[type="radio"]:checked + .choice-text {
         font-weight: bold;
         color: var(--primary-color);
    }
     .choice-label input[type="radio"]:checked {
        box-shadow: 0 0 5px var(--primary-color);
     }


    .choice-text {
        flex-grow: 1; /* Allow text to take up space */
    }

    .choice-meta {
        font-size: 0.9em;
        color: #6c757d;
        margin-right: 10px; /* Space out meta from text */
        white-space: nowrap; /* Prevent meta text from wrapping awkwardly */
    }


    .mission-button {
        display: block;
        width: auto; /* Auto width */
        padding: 12px 25px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center; /* Center text */
        margin-left: auto; /* Align right in RTL */
        margin-right: 0;
    }

    .mission-button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
    }

     .mission-button:active {
         transform: translateY(0);
     }

    .mission-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
         transform: none;
    }

    button#show-summary {
         background-color: var(--secondary-color);
          margin: 30px auto 0 auto; /* Center button */
          display: none; /* Handled by JS */
    }
    button#show-summary:hover {
        background-color: #218838;
    }

    button#explanation-toggle {
        background-color: var(--info-color);
        margin: 30px auto 0 auto; /* Center toggle button below app */
        display: block; /* Ensure it's centered */
        text-align: center;
    }
     button#explanation-toggle:hover {
        background-color: #138496;
    }


    .mission-summary {
        border-top: 2px dashed var(--border-color);
        padding-top: 25px;
        margin-top: 25px;
    }

     .mission-summary h2 {
        color: var(--secondary-color);
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
        margin-bottom: 20px;
     }

    .summary-section {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
        border: 1px solid #e9ecef;
    }

     .summary-section h3 {
        color: #0056b3;
        margin-top: 0;
        margin-bottom: 10px;
     }

     .costs-times p {
        font-size: 1.1em;
     }

     .summary-remaining-budget {
        font-weight: bold;
        color: var(--success-color); /* Default to green */
     }

     .summary-remaining-budget.warning {
         color: var(--warning-color); /* Red if negative */
     }

     .summary-total-time {
        font-weight: bold;
        color: var(--text-color); /* Default */
     }

     .summary-total-time.warning {
        color: var(--warning-color); /* Red if exceeds initial */
     }


    .limitations ul {
        list-style-type: "❌ "; /* Use a cross icon */
        margin-right: 20px;
        padding-right: 0; /* Reset default padding */
        color: var(--warning-color); /* Reddish color for limitations */
        margin-top: 10px;
    }

    .limitations li {
        margin-bottom: 8px;
        padding-right: 5px; /* Space after icon */
    }

     .limitations p { /* For the 'no limitations' case */
         color: var(--success-color);
         font-style: italic;
     }


    .explanation-box {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #fefefe;
        display: none; /* Hidden by default */
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .explanation-box h2 {
        color: #0056b3;
         border-bottom: 1px solid #eee;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
     .explanation-box h3 {
        color: #007bff;
        margin-top: 20px;
        margin-bottom: 10px;
     }

    .explanation-box p {
        margin-bottom: 15px;
         color: #555;
    }

    .explanation-box ul {
        list-style-type: disc;
        margin-right: 20px;
        padding-right: 0; /* Reset default padding */
        margin-bottom: 15px;
    }
    .explanation-box ul ul { /* Nested lists */
        list-style-type: circle;
        margin-right: 15px;
         margin-top: 5px;
         margin-bottom: 5px;
    }

    .explanation-box li {
        margin-bottom: 8px;
    }

    /* Responsive basic adjustments */
    @media (max-width: 600px) {
        body {
            padding: 10px;
        }
        .mission-container {
            padding: 20px;
        }
        .status-breakdown {
            flex-direction: column;
             align-items: flex-start;
        }
         .choice-label {
             flex-direction: column;
             align-items: flex-start;
         }
         .choice-meta {
             margin-right: 0;
             margin-top: 5px;
             font-size: 0.85em;
         }
         .choice-label input[type="radio"] {
             margin-left: 0;
             margin-bottom: 5px;
         }
         .mission-button {
             width: 100%;
             margin-left: 0;
             margin-right: 0;
         }
         button#show-summary, button#explanation-toggle {
             margin-left: auto; /* Still try to center if width is less than container */
             margin-right: auto;
         }

         .step {
            padding: 15px;
         }

          .mission-status {
             padding: 15px;
          }
          .mission-summary {
             padding-top: 15px;
          }
          .summary-section {
             padding: 10px;
          }
           .explanation-box {
             padding: 15px;
           }
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const initialBudget = 100000;
        const initialTime = 12; // Initial time in months
        let totalCostAdded = 0;
        let totalTimeAdded = 0;
        let currentStep = 1;
        const totalSteps = 4; // Number of decision steps

        const initialBudgetSpan = document.getElementById('initial-budget');
        const initialTimeSpan = document.getElementById('initial-time');
        const currentCostAddedSpan = document.getElementById('current-cost-added');
        const currentTimeAddedSpan = document.getElementById('current-time-added');
        const stepsContainer = document.getElementById('steps-container');
        const nextStepButton = document.getElementById('next-step');
        const showSummaryButton = document.getElementById('show-summary');
        const summaryDiv = document.getElementById('summary');
        const explanationToggle = document.getElementById('explanation-toggle');
        const explanationDiv = document.getElementById('explanation');

        // Store selected choices and their details
        const choices = {}; // key: radio button name, value: selected option's data attributes

        // Initialize status display
        initialBudgetSpan.textContent = initialBudget.toLocaleString();
        initialTimeSpan.textContent = initialTime;
        updateStatusDisplay(); // Initial display (0 added cost/time)


        // Show the first step
        document.getElementById(`step-${currentStep}`).classList.add('active');
        updateNextButtonState();


        function updateStatusDisplay() {
             currentCostAddedSpan.textContent = totalCostAdded.toLocaleString();
             currentTimeAddedSpan.textContent = totalTimeAdded.toFixed(1); // Show one decimal place
        }

        function updateNextButtonState() {
             const currentStepElement = document.getElementById(`step-${currentStep}`);
             const selectedOption = currentStepElement.querySelector('input[type="radio"]:checked');
             nextStepButton.disabled = !selectedOption;
        }

        // Add event listeners to all radio buttons
         stepsContainer.querySelectorAll('input[type="radio"]').forEach(input => {
            input.addEventListener('change', (event) => {
                const choiceName = event.target.name;
                const cost = parseInt(event.target.dataset.cost);
                const time = parseFloat(event.target.dataset.time); // Use parseFloat for potential decimals
                const value = event.target.value;

                // Find the step element this input belongs to
                 const stepElement = event.target.closest('.step');
                 const stepNumber = stepElement.id.replace('step-', ''); // Get step number from ID

                 // Remove 'selected' class from other labels in the same step/group
                 stepElement.querySelectorAll('.choice-label').forEach(label => {
                     label.classList.remove('selected');
                 });
                 // Add 'selected' class to the chosen label
                 event.target.closest('.choice-label').classList.add('selected');


                // Subtract cost/time of the previously selected option for this group
                if (choices[choiceName]) {
                    totalCostAdded -= choices[choiceName].cost;
                    totalTimeAdded -= parseFloat(choices[choiceName].time);
                }

                // Add cost/time of the newly selected option
                totalCostAdded += cost;
                totalTimeAdded += time;

                // Store the new choice details
                choices[choiceName] = {
                    value: value,
                    cost: cost,
                    time: time,
                    ...event.target.dataset // Store all data attributes
                };

                // Update status display
                updateStatusDisplay();
                updateNextButtonState(); // Re-check button state after selection
            });
        });


        // Navigation logic
        nextStepButton.addEventListener('click', () => {
            const currentStepElement = document.getElementById(`step-${currentStep}`);
            const selectedOption = currentStepElement.querySelector('input[type="radio"]:checked');

            if (!selectedOption) {
                // Should be prevented by button state, but keeping for robustness
                alert('אנא בחר/י אפשרות לפני ההמשך.');
                return;
            }

            // Remove active class and trigger hide transition
            currentStepElement.classList.remove('active');

            // Use a timeout to allow hide transition before showing next step
             setTimeout(() => {
                 currentStep++;

                if (currentStep <= totalSteps) {
                    // Show next step
                    const nextStepElement = document.getElementById(`step-${currentStep}`);
                     if (nextStepElement) { // Check if element exists
                         nextStepElement.classList.add('active');
                         updateNextButtonState(); // Check state for the new step
                     } else {
                          console.error(`Next step element step-${currentStep} not found`);
                           // Fallback to showing summary if next step element is missing
                            nextStepButton.style.display = 'none';
                            showSummaryButton.style.display = 'block';
                            showSummaryButton.click(); // Auto-click summary
                     }
                } else {
                    // All steps completed, show summary button
                    nextStepButton.style.display = 'none';
                    showSummaryButton.style.display = 'block';
                     // Scroll to the summary button/area
                     showSummaryButton.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
             }, 500); // Match CSS transition duration

        });

        // Show summary logic
        showSummaryButton.addEventListener('click', () => {
            stepsContainer.style.display = 'none'; // Hide steps container
            summaryDiv.style.display = 'block'; // Show summary

            // Populate summary details
            const remainingBudget = initialBudget - totalCostAdded;
            const totalTimeNeeded = initialTime + totalTimeAdded;

            document.getElementById('summary-initial-budget').textContent = initialBudget.toLocaleString();
            document.getElementById('summary-total-cost-added').textContent = totalCostAdded.toLocaleString();
            const remainingBudgetSpan = document.getElementById('summary-remaining-budget');
            remainingBudgetSpan.textContent = remainingBudget.toLocaleString();

            // Add warning class if budget is negative
            if (remainingBudget < 0) {
                remainingBudgetSpan.classList.add('warning');
            } else {
                 remainingBudgetSpan.classList.remove('warning');
            }


            document.getElementById('summary-initial-time').textContent = initialTime;
            const totalTimeSpan = document.getElementById('summary-total-time-needed');
            totalTimeSpan.textContent = totalTimeNeeded.toFixed(1);

             // Add warning class if total time exceeds initial time
             if (totalTimeNeeded > initialTime) {
                 totalTimeSpan.classList.add('warning');
             } else {
                 totalTimeSpan.classList.remove('warning');
             }


            // Populate choices summary
            const populationChoice = choices['population'] || {};
            const samplingChoice = choices['sampling'] || {};
            const sequencingChoice = choices['sequencing'] || {};
            const sampleSizeChoice = choices['sample-size'] || {};

            document.getElementById('summary-population').textContent = populationChoice.population || 'לא נבחר';
            document.getElementById('summary-sampling').textContent = `${samplingChoice.site || 'לא נבחר אתר'} (${samplingChoice.type || 'לא נבחרה שיטה'})`;
            document.getElementById('summary-invasiveness').textContent = samplingChoice.invasiveness || 'לא ידוע';
            document.getElementById('summary-sequencing').textContent = sequencingChoice.value === '16S' ? 'ריצוף 16S rRNA' : (sequencingChoice.value === 'shotgun' ? 'ריצוף Shotgun Metagenomic' : 'לא נבחר');
            document.getElementById('summary-resolution').textContent = sequencingChoice.resolution || 'לא ידוע';
            document.getElementById('summary-sample-size').textContent = sampleSizeChoice.size || 'לא נבחר';
            document.getElementById('summary-num-samples').textContent = sampleSizeChoice['num-samples'] || '0';
            document.getElementById('summary-power').textContent = sampleSizeChoice.power || 'לא ידוע';

            // Populate limitations/data type based on choices and budget/time constraints
            const dataType = sequencingChoice.datatype || 'לא נבחר סוג ריצוף';
            let limitations = [];
            let insights = []; // Use insights for positive/neutral points


            insights.push(`התוכנית שלך מתמקדת ב<strong>${populationChoice.population || 'אוכלוסייה לא מוגדרת'}</strong>, תוך איסוף דגימות מ<strong>${samplingChoice.site || 'אתר לא מוגדר'}</strong> בשיטת <strong>${samplingChoice.type || 'לא מוגדרת'}</strong>.`);
            insights.push(`תנתח את הדגימות באמצעות <strong>${sequencingChoice.value === '16S' ? 'ריצוף 16S rRNA' : (sequencingChoice.value === 'shotgun' ? 'ריצוף Shotgun Metagenomic' : 'טכנולוגיה לא מוגדרת')}</strong>, שתספק נתונים מסוג <strong>${dataType}</strong>.`);
            insights.push(`גודל המדגם שנבחר הוא <strong>${sampleSizeChoice.size || 'לא מוגדר'}</strong> (${sampleSizeChoice['num-samples'] || '0'} דגימות), עם כוח סטטיסטי <strong>${sampleSizeChoice.power || 'לא מוגדר'}</strong>.`);


            if (samplingChoice.invasiveness === 'פולשנית') {
                limitations.push("<strong>הדגימה פולשנית (ביופסיה)</strong>, מה שעשוי להגביל את גודל המדגם בפועל, מייקר את התהליך, ודורש אישור אתי מורכב יותר.");
            }
            if (sequencingChoice.value === '16S') {
                limitations.push("<strong>ריצוף 16S מספק מידע טקסונומי בלבד</strong> (מי החיידקים קיימים ושיעורם), ללא מידע ישיר ומעמיק על התפקידים הפונקציונליים או הפוטנציאל המטבולי של הקהילה המיקרוביאלית.");
            }
            if (sampleSizeChoice.power === 'נמוך') {
                limitations.push("<strong>גודל המדגם קטן</strong>, מה שמגביל משמעותית את הכוח הסטטיסטי ויכולת גילוי הבדלים קטנים או עדינים בין קבוצות מחקר, ומגביר את הסיכון לתוצאות שגויות (False Negative).");
            }
             if (sampleSizeChoice.power === 'בינוני') {
                 limitations.push("גודל המדגם בינוני. בעל כוח סטטיסטי סביר, אך עלול לפספס הבדלים קטנים יותר או דורש גודל אפקט גדול יותר כדי לגלות מובהקות סטטיסטית.");
             }


            if (remainingBudget < 0) {
                 limitations.push(`<strong>חריגה מהתקציב!</strong> עלות התוכנית ($${totalCostAdded.toLocaleString()}) גבוהה מהתקציב שהוקצה ($${initialBudget.toLocaleString()}) בחריגה של $${Math.abs(remainingBudget).toLocaleString()}. התוכנית כפי שתוכננה אינה ניתנת לביצוע עם המשאבים הזמינים.`);
            } else if (remainingBudget > 0) {
                 insights.push(`התוכנית עומדת בתקציב עם יתרה של $${remainingBudget.toLocaleString()}.`);
            } else {
                 insights.push(`התוכנית מנצלת את התקציב במלואו ($${totalCostAdded.toLocaleString()}).`);
            }

             if (totalTimeNeeded > initialTime) {
                 limitations.push(`<strong>זמן המחקר הנדרש ארוך מהזמן שהוקצב!</strong> התוכנית כפי שתוכננה דורשת כ-${totalTimeNeeded.toFixed(1)} חודשים לעומת ${initialTime} שהוקצבו. זה עשוי לעכב את השלמת המשימה.`);
             } else if (totalTimeNeeded <= initialTime) {
                 insights.push(`התוכנית עומדת בלוח הזמנים שהוקצב (${initialTime} חודשים).`);
             }


            document.getElementById('summary-data-type').textContent = dataType;
            const limitationsDiv = document.getElementById('summary-limitations');

            let summaryHtml = "";
            // Add insights first
            summaryHtml += "<h4>מסקנות מרכזיות:</h4><ul>";
            insights.forEach(ins => { summaryHtml += `<li>${ins}</li>`; });
            summaryHtml += "</ul>";

            // Add limitations if any
            if (limitations.length > 0) {
                summaryHtml += "<h4>🚧 אתגרים ומגבלות פוטנציאליים:</h4><ul>";
                limitations.forEach(lim => { summaryHtml += `<li>${lim}</li>`; });
                summaryHtml += "</ul>";
            } else {
                 if (remainingBudget >= 0 && totalTimeNeeded <= initialTime) {
                      summaryHtml += "<p>👍 התוכנית שלך נראית ישימה מבחינת משאבים ולוח זמנים, והבחירות שנעשו תואמות זו את זו.</p>";
                 } else {
                      summaryHtml += "<p>שיקולים נוספים ייתכנו בהתאם למטרות המדויקות של המחקר.</p>";
                 }
            }

            limitationsDiv.innerHTML = summaryHtml;

             // Scroll to the summary
             summaryDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });

        });

        // Explanation toggle logic
        explanationToggle.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            // Toggle display with basic fade effect
            if (isHidden) {
                explanationDiv.style.opacity = '0';
                explanationDiv.style.display = 'block';
                setTimeout(() => { explanationDiv.style.opacity = '1'; }, 10); // Small delay for transition
            } else {
                 explanationDiv.style.opacity = '0';
                 setTimeout(() => { explanationDiv.style.display = 'none'; }, 300); // Hide after fade out
            }

            explanationToggle.textContent = isHidden ? 'הסתר הסבר ⬆️' : 'הצג הסבר על מיקרוביום ומחקר ⬇️';
        });

        // Initial button state check
        updateNextButtonState();
    });
</script>