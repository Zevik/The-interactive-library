---
title: "מנהלים לייבל: הצלחה בתעשיית המוזיקה הדיגיטלית"
english_slug: manage-a-label-success-in-digital-music-industry
category: "ניהול"
tags:
  - תעשיית המוזיקה
  - יזמות
  - עסקים
  - דיגיטל
  - כלכלה
---
# מנהלים לייבל: המסע להצלחה בעולם הדיגיטלי

ברוכים הבאים לעולם התוסס והמאתגר של תעשיית המוזיקה הדיגיטלית! בעידן שבו זרם בלתי פוסק של מוזיקה חדשה מוצף ברשת, האם עדיין יש מקום לקולות ייחודיים? כיצד לייבל אינדי יכול לנווט בנוף המשתנה, לגלות כישרונות, לבנות קהל ולהפוך את התשוקה למוזיקה למודל עסקי בר-קיימא?

המשחק הזה שם אתכם בכיסא המנהל/ת. עם תקציב ראשוני ביד, עליכם לקבל החלטות אסטרטגיות מדי חודש: את מי להחתים? כמה להשקיע בשיווק? באילו ערוצי הכנסה להתמקד? כל החלטה משפיעה על הפופולריות של האמנים שלכם, על ההכנסות שלכם ועל יכולתכם לשרוד ואף לשגשג במשך שנה שלמה.

האם תצליחו לזהות את הלהיט הבא, לגרום לו לפרוץ ולהפוך את הלייבל שלכם לאימפריה דיגיטלית? או שמא התקציב יתאדה לפני שתגיעו לסוף השנה?

צאו למסע, בדקו את האינטואיציה העסקית שלכם ותראו אם יש לכם מה שנדרש כדי להצליח בתעשיית המוזיקה של היום!

<div id="app" class="game-container">
    <div class="status-bar">
        <div class="status-item">
            <i class="fas fa-calendar-alt"></i>
            <span class="status-label">חודש:</span>
            <span id="month">1</span> / 12
        </div>
        <div class="status-item budget-status">
             <i class="fas fa-wallet"></i>
             <span class="status-label">תקציב:</span>
             <span id="budget">₪100,000</span>
             <span id="budget-change-anim" class="budget-change-anim"></span>
        </div>
        <div class="status-item">
             <i class="fas fa-arrow-up"></i>
             <span class="status-label">הכנסה חודשית (משוערת):</span>
             <span id="monthly-income">₪0</span>
        </div>
        <div class="status-item">
             <i class="fas fa-arrow-down"></i>
             <span class="status-label">הוצאה חודשית (משוערת):</span>
             <span id="monthly-expenses">₪0</span>
        </div>
    </div>

    <h2 class="section-title">המטה הראשי של הלייבל</h2>

    <div id="artists-section" class="decision-section">
        <h3 class="section-subtitle"><i class="fas fa-users"></i> אמנים</h3>
        <div class="artist-management-container">
            <div id="current-artists" class="artist-list-container">
                <h4>האמנים בחזקתך:</h4>
                <ul id="artist-list">
                    <li class="empty-state">אין אמנים חתומים בלייבל כרגע.</li>
                </ul>
            </div>
            <div id="available-artists" class="artist-list-container">
                <h4>אמנים פוטנציאלים להחתמה:</h4>
                <ul id="available-artist-list">
                    <li class="artist-card" data-artist-name="יוני בלוז" data-potential="medium" data-cost="5000">
                        <div class="artist-info">
                            <span class="artist-name">יוני בלוז</span>
                            <span class="artist-genre">(בלוז/רוק)</span>
                             <span class="artist-potential">פוטנציאל: בינוני</span>
                             <span class="artist-cost">מקדמה: ₪5,000</span>
                        </div>
                        <button class="sign-artist button primary">החתם <i class="fas fa-signature"></i></button>
                    </li>
                    <li class="artist-card" data-artist-name="מאיה פופ" data-potential="high" data-cost="15000">
                         <div class="artist-info">
                            <span class="artist-name">מאיה פופ</span>
                             <span class="artist-genre">(פופ אלקטרוני)</span>
                             <span class="artist-potential">פוטנציאל: גבוה</span>
                             <span class="artist-cost">מקדמה: ₪15,000</span>
                        </div>
                        <button class="sign-artist button primary">החתם <i class="fas fa-signature"></i></button>
                    </li>
                     <li class="artist-card" data-artist-name="להקת רעש" data-potential="low" data-cost="2000">
                         <div class="artist-info">
                            <span class="artist-name">להקת רעש</span>
                             <span class="artist-genre">(פאנק רוק)</span>
                             <span class="artist-potential">פוטנציאל: נמוך</span>
                             <span class="artist-cost">מקדמה: ₪2,000</span>
                        </div>
                        <button class="sign-artist button primary">החתם <i class="fas fa-signature"></i></button>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <div id="marketing-section" class="decision-section">
        <h3 class="section-subtitle"><i class="fas fa-bullhorn"></i> שיווק וקידום</h3>
        <p>בחר את עוצמת הקמפיין השיווקי החודש. השקעה משפיעה על חשיפת האמנים ועל קצב צמיחת הפופולריות שלהם.</p>
        <div class="marketing-options">
            <div class="radio-option">
                <input type="radio" id="marketing-low" name="marketing-level" value="low" checked>
                <label for="marketing-low"><i class="fas fa-volume-down"></i> קטן (₪1,000)</label>
            </div>
            <div class="radio-option">
                <input type="radio" id="marketing-medium" name="marketing-level" value="medium">
                <label for="marketing-medium"><i class="fas fa-volume-up"></i> בינוני (₪5,000)</label>
            </div>
            <div class="radio-option">
                <input type="radio" id="marketing-high" name="marketing-level" value="high">
                <label for="marketing-high"><i class="fas fa-bullhorn"></i> אינטנסיבי (₪15,000)</label>
            </div>
        </div>
    </div>

     <div id="distribution-section" class="decision-section">
        <h3 class="section-subtitle"><i class="fas fa-coins"></i> מונטיזציה וערוצי הכנסה</h3>
        <p>התמקד בערוצים שונים כדי להגדיל את הכנסות הלייבל. חלקם דורשים השקעה חודשית נוספת אך בעלי פוטנציאל גבוה יותר.</p>
        <div class="monetization-options">
            <div class="checkbox-option">
                <input type="checkbox" id="focus-streaming" value="streaming" checked disabled>
                <label for="focus-streaming"><i class="fas fa-stream"></i> התמקדות בסטרימינג (ברירת מחדל, הכנסה בסיסית)</label>
            </div>
            <div class="checkbox-option">
                <input type="checkbox" id="focus-merch" value="merch">
                <label for="focus-merch"><i class="fas fa-tshirt"></i> השקעה במרצ'נדייז (₪8,000/חודש, פוטנציאל מכירות ישירות)</label>
            </div>
            <div class="checkbox-option">
                <input type="checkbox" id="focus-sync" value="sync">
                <label for="focus-sync"><i class="fas fa-film"></i> חיפוש הזדמנויות סינכרוניזציה (₪5,000/חודש, סיכון/סיכוי גבוה)</label>
            </div>
             <div class="checkbox-option">
                <input type="checkbox" id="focus-live" value="live">
                <label for="focus-live"><i class="fas fa-microphone-alt"></i> ארגון הופעות/אירועים (₪6,000/חודש, בונה קהל ומניב הכנסה ישירה)</label>
            </div>
        </div>
    </div>

    <button id="next-month" class="button success large"><i class="fas fa-forward"></i> עבור לחודש הבא</button>

    <div id="monthly-results" class="results-section" style="display: none;">
        <h3 class="section-subtitle"><i class="fas fa-chart-line"></i> סיכום חודש <span id="results-month"></span></h3>
        <div class="results-summary">
            <h4>תזרים מזומנים חודשי:</h4>
            <ul>
                <li><i class="fas fa-arrow-up income-icon"></i> הכנסה מסטרימינג: <span id="income-streaming"></span></li>
                <li><i class="fas fa-arrow-up income-icon"></i> הכנסה ממרצ'נדייז: <span id="income-merch"></span></li>
                <li><i class="fas fa-arrow-up income-icon"></i> הכנסה מסינכרוניזציה: <span id="income-sync"></span></li>
                 <li><i class="fas fa-arrow-up income-icon"></i> הכנסה מהופעות/אירועים: <span id="income-live"></span></li>
                 <li class="total-row"><i class="fas fa-coins income-icon"></i> סה"כ הכנסות: <span id="total-income"></span></li>
                <li class="separator"></li>
                <li><i class="fas fa-arrow-down expense-icon"></i> הוצאות שיווק: <span id="expenses-marketing"></span></li>
                 <li><i class="fas fa-arrow-down expense-icon"></i> הוצאות תפעול/אחר: <span id="expenses-other"></span></li>
                <li class="total-row"><i class="fas fa-money-bill-wave expense-icon"></i> סה"כ הוצאות: <span id="total-expenses"></span></li>
                <li class="separator"></li>
                <li class="budget-change-row"><i class="fas fa-wallet"></i> שינוי בתקציב החודש: <span id="budget-change"></span></li>
            </ul>
        </div>
         <div class="artist-status-summary">
            <h4>מצב אמנים בסוף החודש:</h4>
             <ul id="artist-status-list">
                 <!-- Artist status will be updated here -->
             </ul>
         </div>
        <p id="game-over-message" class="game-message" style="color: red; font-weight: bold;"></p>
        <button id="restart-game" class="button secondary large" style="display: none;"><i class="fas fa-redo"></i> התחל משחק חדש</button>
    </div>

</div>

<button id="toggle-explanation" class="button info-button large"><i class="fas fa-book-open"></i> הצג/הסתר הסבר תיאורטי על התעשייה</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2><i class="fas fa-info-circle"></i> הסבר תיאורטי: הלייבל העצמאי בעולם הדיגיטלי</h2>
    <p>תעשיית המוזיקה עברה מהפך דרמטי בעשורים האחרונים, בעיקר בזכות האינטרנט והמעבר לצריכה דיגיטלית. בעוד שחברות התקליטים הגדולות עדיין שולטות בחלקים משמעותיים מהשוק, לייבלים עצמאיים (אינדי) מצאו דרכים לשרוד ואף לפרוח, תוך התאמה לנוף המשתנה.</p>

    <h3><i class="fas fa-tools"></i> תפקידו של לייבל תקליטים עצמאי בעידן הדיגיטלי</h3>
    <p>בעידן הדיגיטלי, תפקידי הלייבל העצמאי התפתחו מעבר להקלטה והפצה פיזית. תפקידים מרכזיים כוללים:</p>
    <ul>
        <li>**אוצרות (A&R):** מציאת ופיתוח אמנים בעלי פוטנציאל. זה עדיין תפקיד קריטי בלייבלים רבים, שמחפשים קולות ייחודיים שטרם התגלו או שזקוקים לתמיכה מקצועית.</li>
        <li>**פיתוח אמנים:** סיוע לאמן בבניית קריירה לטווח ארוך - כולל סיוע יצירתי, ייעוץ עסקי, בניית מותג אישי וחיבורים מקצועיים.</li>
        <li>**שיווק וקידום:** יצירת אסטרטגיה שיווקית אפקטיבית לחשיפת המוזיקה לקהל רחב, תוך שימוש בכלים דיגיטליים (רשתות חברתיות, פרסום ממומן, אימייל מרקטינג, אסטרטגיות פלייליסטים) וגם מסורתיים (יחסי ציבור, רדיו).</li>
        <li>**הפצה:** העלאת המוזיקה לפלטפורמות הסטרימינג והחנויות הדיגיטליות (דרך מפיץ דיגיטלי) ולעיתים גם ייצור והפצה של פורמטים פיזיים (ויניל, דיסקים) ומרצ'נדייז.</li>
        <li>**ניהול זכויות ופיננסים:** טיפול בזכויות היוצרים וההקלטה (publishing & master rights), גביית תמלוגים וניהול הכנסות והוצאות.</li>
    </ul>

    <h3><i class="fas fa-money-bill-wave"></i> מודלים עסקיים ומקורות הכנסה</h3>
    <p>לייבלים עצמאיים בעידן הדיגיטלי חייבים לגוון את מקורות ההכנסה שלהם כדי לשרוד. מקורות מרכזיים כוללים:</p>
    <ul>
        <li>**סטרימינג:** ההכנסה הדומיננטית כיום, דרך פלטפורמות כמו ספוטיפיי, אפל מיוזיק, יוטיוב מיוזיק וכו'. התשלומים לכל השמעה נמוכים מאוד, אך היקף ההשמעות העולמי יכול להצטבר.</li>
        <li>**מכירת מוזיקה (דיגיטלית ופיזית):** למרות ירידה דרמטית, עדיין קיימים נישות למכירות דיגיטליות (iTunes, Bandcamp) ומכירות פיזיות (ויניל שחזר לאופנה, דיסקים לקול קהל נאמן).</li>
        <li>**מרצ'נדייז:** מכירת חולצות, פוסטרים, ומוצרים נלווים - מקור הכנסה חשוב שיכול להיות רווחי יותר ממוזיקה עצמה.</li>
        <li>**סינכרוניזציה (Sync Licensing):** השכרת זכויות שימוש במוזיקה לסרטים, סדרות טלוויזיה, פרסומות, משחקי וידאו ותוכן ויזואלי אחר. עסקה אחת כזו יכולה להכניס סכום משמעותי.</li>
        <li>**גיוס קהל (הופעות ואירועים):** אמנם לא תמיד מקור הכנסה ישיר ללייבל (תלוי בהסכם עם האמן), אך הופעות חיות הן קריטיות לבניית קהל, קידום המוזיקה ויצירת הזדמנויות הכנסה נוספות (מכירת מרצ'נדייז בהופעה).</li>
        <li>**גיוס תמיכה (פטריאון, מימון המונים):** חלק מהלייבלים והאמנים מגייסים תמיכה ישירה מהקהל באמצעות פלטפורמות אלה.</li>
    </ul>

    <h3><i class="fas fa-calculator"></i> מבנה ההוצאות</h3>
    <p>ניהול תקציב בלייבל דורש הבנה של עלויות קבועות ומשתנות:</p>
    <ul>
        <li>**עלויות הפקה:** הקלטה, מיקס, מאסטרינג, עיצוב עטיפה - ההשקעה הראשונית ביצירת המוזיקה.</li>
        <li>**עלויות שיווק וקידום:** פרסום דיגיטלי, יחסי ציבור, קמפיינים ברשתות חברתיות, עמלות למקדמים חיצוניים.</li>
        <li>**מקדמות ותמלוגים לאמנים:** תשלום מקדמות לאמנים בעת החתמתם או לפני פרויקט, ותמלוגים מכלל ההכנסות (האחוז משתנה מאוד בהסכמים שונים).</li>
        <li>**עלויות הפצה:** עמלות למפיצים דיגיטליים או פיזיים, עלויות ייצור פיזי (ויניל, דיסקים).</li>
        <li>**עלויות תפעול:** שכירות (אם יש), חשבונות, משכורות (אם יש עובדים), תוכנות, ייעוץ משפטי/פיננסי.</li>
    </ul>

    <h3><i class="fas fa-share-alt"></i> אתגרי השיווק בעידן הדיגיטלי</h3>
    <p>להגיע לקהל בעידן הדיגיטלי הוא אתגר מורכב:</p>
    <ul>
        <li>**חשיפה:** בשוק מוצף במוזיקה חדשה בכל יום, קשה "לצרוח מעל הרעש" ולהגיע לאוזניים חדשות.</li>
        <li>**בניית קהל:** דורש השקעה מתמדת בבניית נוכחות ברשתות החברתיות, יצירת קשר ישיר עם מעריצים (דרך מיילינג ליסט, קהילות), ומתן ערך מעבר למוזיקה עצמה.</li>
        <li>**אסטרטגיות פלייליסטים:** כניסה לפלייליסטים פופולריים בפלטפורמות הסטרימינג יכולה להקפיץ חשיפה, אך התחרות קשה ודורשת אסטרטגיה ממוקדת (פיצ'ינג, קשרים).</li>
        <li>**קידום עצמאי (DIY):** כלים רבים מאפשרים קידום עצמאי, אך הם דורשים ידע, זמן ותקציב.</li>
    </ul>

     <h3><i class="fas fa-hand-holding-usd"></i> חשיבות הגיוון במקורות ההכנסה</h3>
     <p>כפי שניתן לראות ממבנה ההכנסות, הסתמכות על מקור הכנסה אחד (כמו סטרימינג) עלולה להיות קטלנית ללייבל עצמאי. עלויות ההפקה והשיווק לרוב עולות על ההכנסות מהסטרימינג בלבד, לפחות בשלבים הראשונים. גיוון למרצ'נדייז, סינכרוניזציה, והופעות, מאפשר בניית בסיס כלכלי יציב יותר ויכולת להשקיע מחדש בפיתוח אמנים נוספים.</p>

     <h3><i class="fas fa-chart-area"></i> המקרה הכלכלי מאחורי הסטרימינג</h3>
     <p>המודל העסקי של הסטרימינג מבוסס על תשלום חודשי (או הכנסה מפרסומות) למשתמשים. סכום זה מתחלק בין הפלטפורמה (ספוטיפיי, אפל מיוזיק וכו') לבין בעלי הזכויות. החלוקה אינה פשוטה: חלק הולך לחברות תקליטים גדולות (לעיתים על בסיס גלובלי, לא לפי השמעה ספציפית), חלק הולך לחברות פאבלישינג (בעלי זכויות יצירה), וחלק (קטן יחסית) הולך ל"מאסטר" - בעל זכויות ההקלטה (לרוב הלייבל). הלייבל מחלק לאחר מכן את חלקו עם האמן לפי ההסכם ביניהם (לרוב האמן מקבל אחוז נמוך יחסית). עמלת התשלום פר השמעה נמוכה מאוד (פחות מסנט), ודורשת מיליוני השמעות כדי לייצר הכנסה משמעותית. זהו האתגר המרכזי שמוביל לייבלים עצמאיים לחפש מקורות הכנסה נוספים.</p>

</div>

<style>
    /* Import Font Awesome for icons */
    @import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css");

    :root {
        --primary-color: #28a745; /* Success/Go color */
        --secondary-color: #007bff; /* Button color */
        --info-color: #6c757d; /* Info/Toggle color */
        --background-color: #f0f2f5; /* Light background */
        --card-background: #ffffff; /* Card background */
        --border-color: #dcdcdc; /* Light border */
        --text-color: #333; /* Dark text */
        --positive-change: #28a745; /* Green */
        --negative-change: #dc3545; /* Red */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure Right-to-Left */
        text-align: right;
    }

    h1, h2, h3, h4 {
        color: #333;
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        color: #1a1a1a;
        margin-bottom: 30px;
    }

    .game-container, .explanation-section {
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .status-bar {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: space-between;
        margin-bottom: 30px;
        padding: 15px;
        background-color: #e9ecef; /* Lighter background for status */
        border-radius: 8px;
        font-size: 1em;
        color: #555;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
    }

    .status-item {
        display: flex;
        align-items: center;
        margin: 5px 10px; /* Spacing between items */
    }

     .status-item i {
         margin-left: 8px; /* Space after icon in RTL */
         color: var(--secondary-color);
     }

     .status-label {
         font-weight: bold;
         margin-left: 5px; /* Space after label in RTL */
     }

     .budget-status {
         position: relative; /* For animation */
     }

     .budget-change-anim {
         position: absolute;
         top: 50%;
         right: 0; /* Position relative to budget text */
         transform: translateY(-50%);
         font-weight: bold;
         pointer-events: none; /* Don't interfere with clicks */
         opacity: 0;
     }

    .decision-section {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #fdfdfd;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .section-title {
        text-align: center;
        color: #1a1a1a;
        margin-bottom: 20px;
    }

    .section-subtitle {
         color: #555;
         border-bottom: 1px solid var(--border-color);
         padding-bottom: 10px;
         margin-bottom: 15px;
    }
     .section-subtitle i {
         margin-left: 10px; /* Space after icon in RTL */
         color: var(--primary-color);
     }


    .artist-management-container {
         display: flex;
         flex-wrap: wrap; /* Wrap on smaller screens */
         gap: 20px; /* Space between containers */
    }

    .artist-list-container {
         flex: 1; /* Grow to fill space */
         min-width: 300px; /* Minimum width before wrapping */
    }

    #available-artist-list, #artist-list {
        list-style: none;
        padding: 0;
        margin-top: 10px;
    }

    .artist-card, #artist-list li {
        margin-bottom: 10px;
        padding: 15px;
        border: 1px solid #eee;
        border-radius: 6px;
        background-color: #fff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }

    .artist-card:hover {
         transform: translateY(-3px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .artist-info {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align text to the right */
    }

    .artist-name {
        font-weight: bold;
        font-size: 1.1em;
        margin-bottom: 5px;
        color: #0056b3;
    }
    .artist-genre, .artist-potential, .artist-cost {
        font-size: 0.9em;
        color: #555;
        margin-bottom: 3px;
    }

    #artist-list li {
        justify-content: flex-start; /* Align left for current artists */
         background-color: #e9f5ee; /* Light green for signed artists */
         border-color: #c8e6c9;
         box-shadow: none;
         transform: none;
    }

    .empty-state {
        text-align: center;
        color: #777;
        font-style: italic;
        padding: 20px;
    }

    .button {
        padding: 10px 15px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
     .button i {
         margin-left: 8px; /* Space after icon in RTL */
     }

    .button:hover {
        transform: translateY(-1px);
    }
     .button:active {
        transform: translateY(0);
     }

    .primary {
        background-color: var(--secondary-color);
        color: white;
    }
    .primary:hover {
        background-color: #0056b3;
    }

    .success {
        background-color: var(--primary-color);
        color: white;
    }
    .success:hover {
        background-color: #218838;
    }

     .secondary {
         background-color: var(--info-color);
         color: white;
     }
      .secondary:hover {
         background-color: #5a6268;
     }

    .button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
        transform: none;
    }

     .large {
        width: 100%;
        padding: 12px 20px;
        font-size: 1.2em;
        margin-top: 20px;
     }

     .info-button {
         background-color: var(--info-color);
         display: block;
         width: 100%;
         max-width: 800px;
         margin: 20px auto;
         padding: 12px 20px;
         text-align: center;
         font-size: 1.1em;
     }
     .info-button:hover {
         background-color: #5a6268;
     }


    .marketing-options, .monetization-options {
        display: flex;
        flex-direction: column; /* Stack options vertically */
        gap: 10px; /* Space between options */
        margin-top: 15px;
    }

     .radio-option, .checkbox-option {
         display: flex;
         align-items: center;
         background-color: #f8f9fa;
         padding: 10px;
         border-radius: 5px;
         border: 1px solid #e9ecef;
         cursor: pointer;
         transition: background-color 0.2s ease;
     }
      .radio-option:hover, .checkbox-option:hover {
         background-color: #e2e6ea;
      }

     .radio-option input[type="radio"],
     .checkbox-option input[type="checkbox"] {
         margin-left: 10px; /* Space after input in RTL */
         flex-shrink: 0; /* Prevent input from shrinking */
     }

     .radio-option label, .checkbox-option label {
         flex-grow: 1; /* Allow label to take space */
         cursor: pointer;
          display: flex;
          align-items: center;
     }
      .radio-option label i, .checkbox-option label i {
          margin-left: 8px; /* Space after icon in RTL */
          color: var(--secondary-color);
      }
      .checkbox-option input[type="checkbox"]:checked + label i {
           color: var(--primary-color); /* Highlight icon when checked */
      }


    .results-section {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #e9ecef; /* Different background for results */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        animation: fadeIn 0.5s ease-in-out; /* Animation for results appearance */
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

     .results-summary, .artist-status-summary {
         margin-bottom: 20px;
     }

    .results-section ul {
        list-style: none;
        padding: 0;
    }

    .results-section li {
        margin-bottom: 10px;
        padding: 5px 0;
        border-bottom: 1px dashed #ced4da;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
     .results-section li i {
         margin-left: 10px; /* Space after icon */
     }
     .results-section li span {
         font-weight: bold;
     }
     .income-icon { color: var(--primary-color); }
     .expense-icon { color: var(--negative-change); }


     .separator {
         border-bottom: none !important;
         height: 10px;
     }

     .total-row {
         font-size: 1.1em;
         font-weight: bold;
         border-top: 2px solid #adb5bd !important;
         padding-top: 10px !important;
         margin-top: 10px !important;
     }

     .budget-change-row span {
         font-weight: bold;
     }
     .budget-change-row .positive {
         color: var(--positive-change);
     }
     .budget-change-row .negative {
         color: var(--negative-change);
     }

    .artist-status-summary ul {
        list-style: disc;
        padding-right: 20px; /* Indent list for bullets */
    }
    .artist-status-summary li {
         border-bottom: none;
         padding: 3px 0;
         margin-bottom: 5px;
         display: list-item; /* Ensure list item style */
         justify-content: flex-start;
     }

    .game-message {
         text-align: center;
         margin-top: 20px;
         font-size: 1.2em;
    }

    .explanation-section h2, .explanation-section h3 {
        color: #333;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
        margin-top: 15px;
    }
     .explanation-section h2 i, .explanation-section h3 i {
         margin-left: 10px; /* Space after icon */
         color: var(--info-color);
     }

    .explanation-section ul {
        margin-bottom: 15px;
        list-style: disc; /* Use bullet points */
        padding-right: 20px; /* Indent list */
    }
    .explanation-section li {
        margin-bottom: 8px;
    }

     /* Responsive adjustments */
     @media (max-width: 600px) {
         body {
             padding: 10px;
         }
         .game-container, .explanation-section, .info-button {
             padding: 15px;
             margin: 10px auto;
         }
         .status-bar {
             flex-direction: column; /* Stack status items */
             align-items: flex-end; /* Align items to the right */
         }
         .status-item {
             margin: 5px 0;
         }
         .artist-management-container {
              flex-direction: column; /* Stack artist sections */
              gap: 15px;
         }
         .artist-card, #artist-list li {
             flex-direction: column; /* Stack artist info and button */
             align-items: flex-end; /* Align content to the right */
         }
         .artist-info {
             align-items: flex-end; /* Ensure text is right-aligned */
             margin-bottom: 10px;
         }
         .button {
             width: 100%; /* Full width buttons on small screens */
         }
          .large {
             padding: 10px 15px;
             font-size: 1.1em;
          }
     }

      /* Animation for popularity increase */
      .popularity-bar {
          width: 100%;
          background-color: #e0e0e0;
          border-radius: 4px;
          margin-top: 5px;
          overflow: hidden; /* Ensure bar stays within bounds */
      }

      .popularity-fill {
          height: 8px;
          background-color: #ffc107; /* Yellow/Orange color */
          width: 0%; /* Initial state */
          transition: width 1s ease-out; /* Smooth transition */
          border-radius: 4px;
      }

       /* Animation for budget change */
       @keyframes budgetChangeAnim {
           0% { opacity: 1; transform: translateY(-50%) scale(1); color: var(--text-color); }
           50% { opacity: 0.5; transform: translateY(-70%) scale(1.1); }
           100% { opacity: 0; transform: translateY(-100%) scale(1.2); }
       }

       .budget-change-anim.positive {
            color: var(--positive-change);
            animation: budgetChangeAnim 1.5s ease-out forwards;
       }
       .budget-change-anim.negative {
           color: var(--negative-change);
           animation: budgetChangeAnim 1.5s ease-out forwards;
       }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // --- Game State ---
        let budget = 100000;
        let month = 1;
        const maxMonths = 12;
        let artists = []; // { name, potential (low/medium/high), popularity, signedMonth }

        // --- Configuration & Costs ---
        const marketingCosts = { low: 1000, medium: 5000, high: 15000 };
        // Base popularity increase per month from marketing, scaled by potential and current pop
        const marketingBaseEffect = { low: 0.005, medium: 0.01, high: 0.02 }; // % increase relative to current pop
        const potentialMultipliers = { low: 0.8, medium: 1.0, high: 1.5 }; // Affects income & pop growth scaling
        const baseStreamingIncomePerPop = 0.15; // Base income multiplier per popularity point

        const merchInvestmentCost = 8000; // Cost to run merch focus
        const merchBaseIncomePerPop = 0.1; // Base income from merch per popularity point (scaled by potential)
        const merchPopularityThreshold = 30; // Pop needed for significant merch income

        const syncInvestmentCost = 5000; // Cost to run sync focus
        const syncBaseSuccessRate = 0.08; // Base chance (per artist) of sync deal if focus is on
        const syncPopularityEffect = 0.001; // Added chance per popularity point
        const syncDealValue = 50000; // Income from a successful sync deal

        const liveInvestmentCost = 6000; // Cost to organize gigs
        const liveBaseIncomePerPop = 0.12; // Base income from live per popularity point (scaled by potential)
        const livePopBoost = 0.05; // Extra popularity boost from live events IF artist has minimum pop
        const livePopularityThreshold = 20; // Pop needed for live events to be effective

        const startingPopularity = 10; // Initial popularity for new artists

        // --- DOM Elements ---
        const budgetEl = document.getElementById('budget');
        const budgetChangeAnimEl = document.getElementById('budget-change-anim');
        const monthEl = document.getElementById('month');
        const monthlyIncomeEl = document.getElementById('monthly-income');
        const monthlyExpensesEl = document.getElementById('monthly-expenses');
        const artistListEl = document.getElementById('artist-list');
        const availableArtistListEl = document.getElementById('available-artist-list');
        const availableArtistsSection = document.getElementById('available-artists');
        const nextMonthBtn = document.getElementById('next-month');
        const monthlyResultsEl = document.getElementById('monthly-results');
        const resultsMonthEl = document.getElementById('results-month');
        const incomeStreamingEl = document.getElementById('income-streaming');
        const incomeMerchEl = document.getElementById('income-merch');
        const incomeSyncEl = document.getElementById('income-sync');
        const incomeLiveEl = document.getElementById('income-live');
        const totalIncomeEl = document.getElementById('total-income');
        const expensesMarketingEl = document.getElementById('expenses-marketing');
        const expensesOtherEl = document.getElementById('expenses-other');
        const totalExpensesEl = document.getElementById('total-expenses');
        const budgetChangeEl = document.getElementById('budget-change');
        const artistStatusListEl = document.getElementById('artist-status-list');
        const gameOverMessageEl = document.getElementById('game-over-message');
        const restartGameBtn = document.getElementById('restart-game');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const explanationEl = document.getElementById('explanation');
        const signArtistButtons = document.querySelectorAll('.sign-artist');

        // --- UI Update Functions ---
        function updateUI() {
            budgetEl.textContent = `₪${Math.round(budget).toLocaleString()}`;
            monthEl.textContent = month;
            updateArtistLists();
             // Estimate next month's expenses for display (only marketing for simplicity)
             const marketingLevel = document.querySelector('input[name="marketing-level"]:checked').value;
             const estimatedExpenses = marketingCosts[marketingLevel] +
                                       (document.getElementById('focus-merch').checked ? merchInvestmentCost : 0) +
                                       (document.getElementById('focus-sync').checked ? syncInvestmentCost : 0) +
                                       (document.getElementById('focus-live').checked ? liveInvestmentCost : 0);
             monthlyExpensesEl.textContent = `₪${estimatedExpenses.toLocaleString()}`;
             // Cannot easily estimate income without running the month, so keep at 0 or last month's total
             // For now, let's reset to 0 until the next month calculation
            monthlyIncomeEl.textContent = `₪0`;


            monthlyResultsEl.style.display = 'none'; // Hide results until month ends
             gameOverMessageEl.textContent = '';
             restartGameBtn.style.display = 'none';
             nextMonthBtn.style.display = 'block'; // Ensure next month button is visible

             // Update button states
            signArtistButtons.forEach(button => {
                 const cost = parseInt(button.dataset.cost);
                 const artistName = button.dataset.artistName;
                 const isSigned = artists.some(a => a.name === artistName);
                 button.disabled = budget < cost || isSigned;
                 button.textContent = isSigned ? 'חתום <i class="fas fa-check"></i>' : `החתם ₪${cost.toLocaleString()} <i class="fas fa-signature"></i>`;
                 button.classList.toggle('primary', !isSigned);
                 button.classList.toggle('secondary', isSigned); // Style signed buttons differently
                 button.style.cursor = isSigned ? 'default' : 'pointer';
            });

             // Enable/disable monetization checkboxes if budget is too low for investment
             const focusMerchCheckbox = document.getElementById('focus-merch');
             const focusSyncCheckbox = document.getElementById('focus-sync');
             const focusLiveCheckbox = document.getElementById('focus-live');

             focusMerchCheckbox.disabled = focusMerchCheckbox.checked ? false : budget < merchInvestmentCost;
             focusSyncCheckbox.disabled = focusSyncCheckbox.checked ? false : budget < syncInvestmentCost;
             focusLiveCheckbox.disabled = focusLiveCheckbox.checked ? false : budget < liveInvestmentCost;


        }

        function updateArtistLists() {
            // Update current artists list
            artistListEl.innerHTML = '';
            if (artists.length === 0) {
                artistListEl.innerHTML = '<li class="empty-state">אין אמנים חתומים בלייבל כרגע.</li>';
            } else {
                artists.forEach(artist => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <div class="artist-info">
                            <span class="artist-name">${artist.name}</span>
                             <span class="artist-genre">(${artist.potential === 'low' ? 'פוטנציאל נמוך' : artist.potential === 'medium' ? 'פוטנציאל בינוני' : 'פוטנציאל גבוה'})</span>
                             <span class="artist-pop">פופולריות: ${Math.round(artist.popularity)}%</span>
                              <div class="popularity-bar"><div class="popularity-fill" style="width: ${artist.popularity}%;"></div></div>
                        </div>
                    `;
                    artistListEl.appendChild(li);
                });
                 // Trigger animation for popularity bars
                 setTimeout(() => {
                     artistListEl.querySelectorAll('.popularity-fill').forEach(bar => {
                         const targetWidth = bar.style.width; // Get width set above
                         bar.style.width = targetWidth; // Re-set width to trigger CSS transition
                     });
                 }, 50); // Small delay to ensure DOM is updated before triggering animation
            }

            // Hide signed artists from available list
            availableArtistListEl.querySelectorAll('.artist-card').forEach(li => {
                const artistName = li.dataset.artistName;
                if (artists.some(a => a.name === artistName)) {
                    li.style.display = 'none';
                } else {
                     li.style.display = 'flex'; // Show if not signed
                }
            });
             // If no artists are available, show a message
             const remainingAvailable = Array.from(availableArtistListEl.querySelectorAll('.artist-card')).some(li => li.style.display !== 'none');
             if (!remainingAvailable) {
                  if (!document.getElementById('no-more-artists-msg')) {
                      const msgLi = document.createElement('li');
                      msgLi.id = 'no-more-artists-msg';
                      msgLi.classList.add('empty-state');
                      msgLi.textContent = 'אין כרגע אמנים פוטנציאלים חדשים להחתמה.';
                       availableArtistListEl.appendChild(msgLi);
                  }
             } else {
                  const msgLi = document.getElementById('no-more-artists-msg');
                  if (msgLi) msgLi.remove();
             }
        }

         function animateBudgetChange(amount) {
             budgetChangeAnimEl.textContent = `${amount >= 0 ? '+' : ''}₪${Math.round(amount).toLocaleString()}`;
             budgetChangeAnimEl.className = 'budget-change-anim'; // Reset classes
             if (amount >= 0) {
                 budgetChangeAnimEl.classList.add('positive');
             } else {
                 budgetChangeAnimEl.classList.add('negative');
             }
              // Trigger reflow to restart animation
             void budgetChangeAnimEl.offsetWidth;
         }


        function calculateMonthResults() {
            const marketingLevel = document.querySelector('input[name="marketing-level"]:checked').value;
            const currentMarketingCost = marketingCosts[marketingLevel];
            const marketingPopEffectMultiplier = marketingBaseEffect[marketingLevel]; // Base % per month


            let totalMonthlyIncome = 0;
            let totalMonthlyExpenses = currentMarketingCost;
            let streamingIncome = 0;
            let merchIncome = 0;
            let syncIncome = 0;
            let liveIncome = 0;
            let otherExpenses = 0; // For merch, sync, live investment

            const focusMerch = document.getElementById('focus-merch').checked;
            const focusSync = document.getElementById('focus-sync').checked;
            const focusLive = document.getElementById('focus-live').checked;

            if (focusMerch) {
                totalMonthlyExpenses += merchInvestmentCost;
                 otherExpenses += merchInvestmentCost;
            }
             if (focusSync) {
                totalMonthlyExpenses += syncInvestmentCost;
                 otherExpenses += syncInvestmentCost;
            }
             if (focusLive) {
                totalMonthlyExpenses += liveInvestmentCost;
                 otherExpenses += liveInvestmentCost;
             }

             // Check if budget allows these investments AFTER signing artists but BEFORE spending
             // If not enough budget, deselect and don't charge/apply effect
             if(budget - totalMonthlyExpenses < 0) {
                 // Decide which focus areas to cut. Simple approach: cut from most expensive.
                 const investments = [];
                 if (focusMerch) investments.push({ type: 'merch', cost: merchInvestmentCost });
                 if (focusSync) investments.push({ type: 'sync', cost: syncInvestmentCost });
                 if (focusLive) investments.push({ type: 'live', cost: liveInvestmentCost });

                 investments.sort((a, b) => b.cost - a.cost); // Sort by cost descending

                 let currentTotalInvestment = investments.reduce((sum, inv) => sum + inv.cost, 0);
                 const availableBudgetForInvestment = budget - currentMarketingCost;

                 for (const inv of investments) {
                     if (availableBudgetForInvestment < currentTotalInvestment) {
                         // Need to cut this investment
                         if (inv.type === 'merch') {
                             document.getElementById('focus-merch').checked = false;
                             otherExpenses -= merchInvestmentCost;
                             currentTotalInvestment -= merchInvestmentCost;
                             alert(' אין מספיק תקציב להשקיע במרצ\'נדייז החודש. הפוקוס הוסר אוטומטית.');
                         } else if (inv.type === 'sync') {
                             document.getElementById('focus-sync').checked = false;
                             otherExpenses -= syncInvestmentCost;
                             currentTotalInvestment -= syncInvestmentCost;
                              alert(' אין מספיק תקציב להשקיע בחיפוש עסקאות סינכרון החודש. הפוקוס הוסר אוטומטית.');
                         } else if (inv.type === 'live') {
                             document.getElementById('focus-live').checked = false;
                             otherExpenses -= liveInvestmentCost;
                             currentTotalInvestment -= liveInvestmentCost;
                              alert(' אין מספיק תקציב להשקיע בארגון הופעות החודש. הפוקוס הוסר אוטומטית.');
                         }
                     } else {
                         break; // Budget is sufficient for remaining investments
                     }
                 }
                 totalMonthlyExpenses = currentMarketingCost + otherExpenses; // Recalculate total expenses
             }


            const artistMonthlyStatus = [];
             let monthSyncIncome = 0; // Total sync income for the month


            artists.forEach(artist => {
                // Calculate popularity growth
                 let popGrowth = (marketingPopEffectMultiplier * potentialMultipliers[artist.potential]) * (artist.popularity + 10); // Pop growth influenced by current pop, with a base boost
                 let artistIncomeFromLive = 0;

                if (focusLive && artist.popularity >= livePopularityThreshold) {
                     popGrowth += livePopBoost * (potentialMultipliers[artist.potential] * (artist.popularity + 10)); // Additional boost from live events
                     artistIncomeFromLive = artist.popularity * liveBaseIncomePerPop * potentialMultipliers[artist.potential];
                } else if (focusLive && artist.popularity < livePopularityThreshold) {
                     artistMonthlyStatus.push(`${artist.name}: פופולריות נמוכה מדי (${Math.round(artist.popularity)}%) לארגון הופעות אפקטיביות החודש.`);
                }


                artist.popularity = Math.min(100, artist.popularity + popGrowth); // Cap popularity at 100

                // Calculate income streams for artist
                const artistStreamingIncome = artist.popularity * baseStreamingIncomePerPop * potentialMultipliers[artist.potential];
                streamingIncome += artistStreamingIncome;

                if (focusMerch && artist.popularity >= merchPopularityThreshold) {
                     const artistMerchIncome = artist.popularity * merchBaseIncomePerPop * potentialMultipliers[artist.potential];
                     merchIncome += artistMerchIncome;
                } else if (focusMerch && artist.popularity < merchPopularityThreshold) {
                    // Merch investment made, but artist pop is too low for significant sales
                }


                 liveIncome += artistIncomeFromLive;


                artistMonthlyStatus.push(`${artist.name}: פופולריות עלתה ל-${Math.round(artist.popularity)}%`);

                // Calculate Sync Income (chance per artist if focus is on)
                 if (focusSync) {
                      const artistSyncChance = syncBaseSuccessRate + (artist.popularity * syncPopularityEffect);
                      if (Math.random() < artistSyncChance) {
                           monthSyncIncome += syncDealValue; // Add to total sync income for the month
                           artistMonthlyStatus.push(`${artist.name}: עסקת סינכרוניזציה שווה ₪${syncDealValue.toLocaleString()} נחתמה! 🎉`);
                      }
                 }

            });

             syncIncome = monthSyncIncome; // Assign total sync income for the month

            totalMonthlyIncome = streamingIncome + merchIncome + syncIncome + liveIncome;

            const budgetChangeAmount = totalMonthlyIncome - totalMonthlyExpenses;
            budget += budgetChangeAmount;

            // Update results display
            resultsMonthEl.textContent = month;
            incomeStreamingEl.textContent = `₪${Math.round(streamingIncome).toLocaleString()}`;
            incomeMerchEl.textContent = `₪${Math.round(merchIncome).toLocaleString()}`;
            incomeSyncEl.textContent = `₪${Math.round(syncIncome).toLocaleString()}`;
            incomeLiveEl.textContent = `₪${Math.round(liveIncome).toLocaleString()}`;
            totalIncomeEl.textContent = `₪${Math.round(totalMonthlyIncome).toLocaleString()}`;
            expensesMarketingEl.textContent = `₪${Math.round(currentMarketingCost).toLocaleString()}`;
            expensesOtherEl.textContent = `₪${Math.round(otherExpenses).toLocaleString()}`;
            totalExpensesEl.textContent = `₪${Math.round(totalMonthlyExpenses).toLocaleString()}`;

            budgetChangeEl.textContent = `₪${Math.round(budgetChangeAmount).toLocaleString()}`;
            budgetChangeEl.classList.remove('positive', 'negative');
             if (budgetChangeAmount >= 0) {
                 budgetChangeEl.classList.add('positive');
             } else {
                 budgetChangeEl.classList.add('negative');
             }


            artistStatusListEl.innerHTML = '';
            if(artistMonthlyStatus.length > 0) {
                artistMonthlyStatus.forEach(status => {
                    const li = document.createElement('li');
                    li.textContent = status;
                    artistStatusListEl.appendChild(li);
                });
            } else {
                 artistStatusListEl.innerHTML = '<li>אין אמנים חתומים.</li>';
            }


            monthlyResultsEl.style.display = 'block';
             monthlyIncomeEl.textContent = `₪${Math.round(totalMonthlyIncome).toLocaleString()}`;
             monthlyExpensesEl.textContent = `₪${Math.round(totalMonthlyExpenses).toLocaleString()}`;

             animateBudgetChange(budgetChangeAmount);


            // Check for game over or win
            if (budget < 0) {
                 gameOverMessageEl.textContent = `🚨 נגמר לך הכסף בחודש ${month}. המשחק הסתיים בכישלון! נסה שוב!`;
                 gameOverMessageEl.style.color = 'var(--negative-change)';
                 endGame();
            } else if (month >= maxMonths) {
                 gameOverMessageEl.textContent = `🏆 מזל טוב! סיימת את 12 החודשים עם תקציב של ₪${Math.round(budget).toLocaleString()}! האם הלייבל שלך הצליח לשגשג?`;
                 gameOverMessageEl.style.color = 'var(--primary-color)';
                 endGame();
            }

        }

         function endGame() {
             nextMonthBtn.style.display = 'none';
             restartGameBtn.style.display = 'block';
              // Disable all decision inputs
             document.querySelectorAll('#app input, #app button:not(#restart-game)').forEach(el => el.disabled = true);
         }


        function handleSignArtist(event) {
            const button = event.target.closest('.sign-artist'); // Use closest to handle icon clicks
            if (!button || button.disabled) return;

            const name = button.dataset.artistName;
            const potential = button.dataset.potential;
            const cost = parseInt(button.dataset.cost);

            if (budget >= cost) {
                budget -= cost;
                artists.push({
                    name: name,
                    potential: potential,
                    popularity: startingPopularity,
                    signedMonth: month
                });
                 // Remove the artist card visually immediately
                button.closest('.artist-card').style.display = 'none';
                alert(`🥳 הוחתם האמן: ${name}! העבר לחודש הבא כדי לראות את השפעתו.`);
                updateUI(); // Update budget display and artist list
            } else {
                alert('😥 אין מספיק תקציב כדי להחתים אמן זה. נסה לחסוך בחודשים הבאים.');
            }
        }

        function restartGame() {
            budget = 100000;
            month = 1;
            artists = [];
            // Reset inputs
            document.getElementById('marketing-low').checked = true;
            document.getElementById('focus-streaming').checked = true; // Streaming is always checked/disabled=false
            document.getElementById('focus-merch').checked = false;
            document.getElementById('focus-sync').checked = false;
            document.getElementById('focus-live').checked = false;

            // Re-enable all inputs
            document.querySelectorAll('#app input, #app button').forEach(el => el.disabled = false);
            document.getElementById('focus-streaming').disabled = true; // Streaming is always disabled=true

            // Show all available artists again by removing potential 'none' display and message
             availableArtistListEl.querySelectorAll('.artist-card').forEach(li => {
                    li.style.display = 'flex';
             });
            const msgLi = document.getElementById('no-more-artists-msg');
             if (msgLi) msgLi.remove();


            nextMonthBtn.disabled = false;
            monthlyResultsEl.style.display = 'none'; // Hide previous results
             updateUI(); // Set initial state UI
        }


        // --- Event Listeners ---
        signArtistButtons.forEach(button => {
            button.addEventListener('click', handleSignArtist);
        });

        nextMonthBtn.addEventListener('click', () => {
            if (month < maxMonths && budget >= 0) {
                calculateMonthResults();
                month++;
                // Check budget again after calculations before updating UI for *next* month
                 if (budget >= 0 && month <= maxMonths) {
                     updateUI();
                 } else if (budget < 0) {
                     // Game over happened, UI is already updated by calculateMonthResults
                 }
            } else if (month === maxMonths && budget >= 0) {
                 // Handle the calculation for the 12th month specifically if not already Game Over
                 if (budget >= 0) { // Ensure not already game over from the last calculation check
                      calculateMonthResults();
                 }
            }
        });

        restartGameBtn.addEventListener('click', restartGame);

         toggleExplanationBtn.addEventListener('click', () => {
             const display = explanationEl.style.display;
             explanationEl.style.display = display === 'none' ? 'block' : 'none';
             // Scroll to explanation if shown
             if (explanationEl.style.display === 'block') {
                  explanationEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
         });

         // Add event listeners to monetization checkboxes to update estimated expenses immediately
         document.querySelectorAll('#distribution-section input[type="checkbox"]').forEach(checkbox => {
             checkbox.addEventListener('change', updateUI); // updateUI also updates estimated expenses
         });
          // Add event listeners to marketing radio buttons to update estimated expenses immediately
          document.querySelectorAll('#marketing-section input[type="radio"]').forEach(radio => {
              radio.addEventListener('change', updateUI); // updateUI also updates estimated expenses
          });


        // --- Initial Setup ---
        updateUI();
    });
</script>