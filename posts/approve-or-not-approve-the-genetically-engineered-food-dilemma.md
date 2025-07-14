---
title: "לאשר או לא לאשר? דילמת המזון המהונדס"
english_slug: approve-or-not-approve-the-genetically-engineered-food-dilemma
category: "מיומנויות וחינוך / חשיבה ומחקר"
tags: מזון מהונדס גנטית, רגולציה, קבלת החלטות, הערכת סיכונים, מדיניות ציבורית
---
<div class="simulation-wrapper">
    <header>
        <h1>לאשר או לא לאשר? דילמת המזון המהונדס</h1>
        <p>מזון מהונדס גנטית נמצא על השולחן שלנו ועל הפרק הציבורי. אבל איך הוא עובר את המחסום הרגולטורי? מי מקבל את ההחלטות הגורליות הללו, ועל בסיס אילו שיקולים? האם רק מדע יבש, או שמא ישנם כוחות ואינטרסים נוספים המשפיעים על מאזני הצדק הרגולטורי?</p>
    </header>

    <div id="app-container" class="interactive-section">
        <h2>מקרה מבחן: האתגר הרגולטורי של תירס מהונדס חדש</h2>
        <p>דמיין את עצמך יושב בחדר הדיונים. אתה חבר מפתח בצוות הרגולטורי שאמון על הכרעה גורלית: האם לאשר שיווק המוני של זן תירס חדשני שעבר הנדסה גנטית. זן זה מבטיח עמידות מוגברת בפני מזיק נפוץ, מה שיכול לצמצם משמעותית את הצורך בריסוס חומרי הדברה מסוימים. בפניך מונחות "עדויות" וטיעונים מגוונים, מדעיות, כלכליות, חברתיות וסביבתיות. עליך לשקול כל אחת מהן בכובד ראש ולבחור אילו שיקולים לדעתך בעלי המשקל המשמעותי ביותר בהחלטה כזו. כל בחירה שתבצע תשפיע על שקלול הניקוד הסופי.</p>

        <div id="considerations" class="considerations-list">
            <div class="consideration-item">
                <input type="checkbox" id="safety-positive" data-weight="2" class="consideration-checkbox">
                <label for="safety-positive" class="consideration-label">
                    <span class="label-text">
                        <b><i class="icon-science">🔬</i> ממצאי מחקרי בטיחות (בריאות האדם):</b> שורה ארוכה של מחקרים מקיפים, הן כאלה שנערכו על ידי החברה המפתחת והן מחקרים עצמאיים של גופים אקדמיים ורגולטוריים, <span class="highlight-positive">לא מצאו כל עדויות להשפעות בריאותיות שליליות</span> בצריכה של התירס המהונדס על בני אדם או חיות מעבדה במהלך תקופת הבדיקה.
                    </span>
                </label>
            </div>
            <div class="consideration-item">
                <input type="checkbox" id="nutritional-value" data-weight="0" class="consideration-checkbox">
                <label for="nutritional-value" class="consideration-label">
                    <span class="label-text">
                         <b><i class="icon-food">🌽</i> ערך תזונתי:</b> ניתוח מעמיק של הרכב התירס המהונדס מבחינת ויטמינים, מינרלים, חלבונים ופחמימות מצביע על <span class="highlight-neutral">ערך תזונתי דומה מאוד</span>, כמעט זהה, לזה של זני תירס קונבנציונליים נפוצים.
                    </span>
                </label>
            </div>
             <div class="consideration-item">
                <input type="checkbox" id="env-low-risk" data-weight="2" class="consideration-checkbox">
                <label for="env-low-risk" class="consideration-label">
                    <span class="label-text">
                         <b><i class="icon-leaf">🌿</i> הערכת סיכון סביבתי (מועיל):</b> ניתוח מומחים מצביע על <span class="highlight-positive">פוטנציאל משמעותי להפחתה בשימוש בחומרי הדברה מסוימים</span> הרעילים למזיק. הדבר צפוי להועיל לא רק לסביבה ולמגוון הביולוגי באזורים חקלאיים, אלא גם לשפר את בריאותם ובטיחותם של העובדים החקלאיים החשופים לחומרים אלו.
                    </span>
                </label>
            </div>
             <div class="consideration-item">
                <input type="checkbox" id="env-cross-pollination" data-weight="-1" class="consideration-checkbox">
                <label for="env-cross-pollination" class="consideration-label">
                    <span class="label-text">
                         <b><i class="icon-warning">⚠️</i> הערכת סיכון סביבתי (פוטנציאלי):</b> קיים <span class="highlight-negative">חשש תיאורטי</span>, שהוערך כבעל סבירות נמוכה יחסית במחקרים, לאפשרות של מעבר הגן המהונדס לזני בר קרובים באמצעות הפריה הדדית (cross-pollination), דבר שיכול ליצור עמידות במזיקים גם בזני בר.
                    </span>
                </label>
            </div>
            <div class="consideration-item">
                <input type="checkbox" id="economic-benefits" data-weight="1" class="consideration-checkbox">
                <label for="economic-benefits" class="consideration-label">
                    <span class="label-text">
                        <b><i class="icon-money">💰</i> יתרונות כלכליים:</b> החברה המפתחת מציגה תחזיות מרשימות ל<span class="highlight-positive">עלייה משמעותית ביבולי התירס</span> והפחתה בעלויות הטיפול במזיקים עבור חקלאים שיאמצו את הזן החדש. הדבר יכול להוביל לרווחה כלכלית רבה יותר למגדלים ול potentially הוזלת עלויות ייצור.
                    </span>
                </label>
            </div>
             <div class="consideration-item">
                <input type="checkbox" id="economic-concerns" data-weight="-1" class="consideration-checkbox">
                <label for="economic-concerns" class="consideration-label">
                    <span class="label-text">
                         <b><i class="icon-handshake">🤝</i> חששות כלכליים (אחרים):</b> <span class="highlight-negative">ארגוני חקלאים קטנים מביעים חשש כבד</span> מפני יצירת תלות בלעדית בחברה המפתחת, אשר מחזיקה בקניין הרוחני על הזרעים. הם חוששים מעלויות זרעים גבוהות לאורך זמן ומהשפעה שלילית על חקלאות מסורתית או אורגנית באזורים סמוכים.
                    </span>
                </label>
            </div>
            <div class="consideration-item">
                <input type="checkbox" id="health-ngo-concerns" data-weight="-2" class="consideration-checkbox">
                <label for="health-ngo-concerns" class="consideration-label">
                    <span class="label-text">
                         <b><i class="icon-users">🗣️</i> עמדת ארגוני בריאות וצרכנות:</b> ארגונים אלו מביעים <span class="highlight-negative">חשש ציבורי כבד</span> ביחס לבטיחות המזון המהונדס ודורשים מחקרים ארוכי טווח ועצמאיים נוספים (שאינם ממומנים ע"י החברות המפתחות) לפני מתן אישור לשיווק.
                    </span>
                </label>
            </div>
            <div class="consideration-item">
                <input type="checkbox" id="env-ngo-concerns" data-weight="-1" class="consideration-checkbox">
                <label for="env-ngo-concerns" class="consideration-label">
                    <span class="label-text">
                        <b><i class="icon-world">🌍</i> עמדת ארגוני סביבה:</b> למרות הערכות הסיכון הרשמיות, ארגוני סביבה ממשיכים להעלות <span class="highlight-negative">חששות לגבי השפעות ארוכות טווח ולא צפויות</span> על המערכת האקולוגית, כולל יצירת "מזיקי על" עמידים לחומר ההדברה או השפעה על חרקים שאינם מזיקים (כמו דבורים).
                    </span>
                </label>
            </div>
            <div class="consideration-item">
                <input type="checkbox" id="public-skepticism" data-weight="-1" class="consideration-checkbox">
                <label for="public-skepticism" class="consideration-label">
                    <span class="label-text">
                         <b><i class="icon-megaphone">📣</i> דעת קהל:</b> סקרים מראים כי קיים <span class="highlight-negative">סקפטיות וחוסר אמון משמעותי</span> בקרב הציבור הרחב ביחס למזון מהונדס גנטית. חלקים נרחבים בציבור דורשים סימון ברור ומפורט, וחלקם מעדיפים להימנע ממוצרים כאלה לחלוטין.
                    </span>
                </label>
            </div>
            <div class="consideration-item">
                <input type="checkbox" id="reg-precedent" data-weight="1" class="consideration-checkbox">
                <label for="reg-precedent" class="consideration-label">
                    <span class="label-text">
                        <b><i class="icon-law">⚖️</i> תקדים רגולטורי בינלאומי:</b> <span class="highlight-positive">זנים דומים מאוד</span> של תירס מהונדס גנטית לעמידות בפני מזיקים כבר <span class="highlight-positive">אושרו לשימוש ולשיווק במדינות רבות אחרות</span> ברחבי העולם, כולל במדינות עם מסגרות רגולטוריות קפדניות ודומות לשלך.
                    </span>
                </label>
            </div>
        </div>

        <button id="submit-decision" class="primary-button">קבל את ההחלטה הרגולטורית</button>

        <div id="results" class="results-section">
            <h3 class="results-title"></h3>
            <p id="final-decision-text" class="decision-text"></p>
            <div class="results-details">
                <h4>פירוט השפעת השיקולים שבחרת על ההחלטה:</h4>
                <ul id="selected-factors-list" class="selected-factors-list"></ul>
            </div>
             <p class="results-insight">כפי שראית, תהליך קבלת החלטה רגולטורית בנוגע לטכנולוגיות חדשות כמו הנדסה גנטית הוא מורכב ורב-ממדי. הוא מושפע לא רק מראיות מדעיות "טהורות", אלא גם משיקולים כלכליים, חברתיים, סביבתיים ואף פוליטיים. שקלול השיקולים המנוגדים הללו, תוך ניהול אי-ודאות ולחצים שונים, הוא הליבה של הדילמה הרגולטורית והציבורית סביב מזון מהונדס גנטית.</p>
        </div>
    </div>

    <button id="toggle-explanation" class="secondary-button">הצג/הסתר רקע והסבר על דילמת המזון המהונדס ורגולציה</button>

    <div id="explanation-content" class="explanation-section">
        <h2>הבנת הדילמה: מזון מהונדס גנטית וקבלת החלטות רגולטורית</h2>

        <h3>מהו מזון מהונדס גנטית?</h3>
        <p>מזון מהונדס גנטית (GE - Genetic Engineering, או GM - Genetically Modified) מתייחס למזון המופק מצמחים, בעלי חיים או מיקרואורגניזמים שעברו שינוי מכוון וספציפי במטען הגנטי שלהם (DNA). שינויים אלו מבוצעים באמצעות טכניקות ביוטכנולוגיה מתקדמות במטרה להקנות לאורגניזם תכונות חדשות ורצויות. דוגמאות נפוצות כוללות עמידות בפני מזיקים או מחלות, עמידות בפני קוטלי עשבים ספציפיים, שיפור הערך התזונתי, עמידות לתנאי סביבה קיצוניים, או הגדלת חיי המדף.</p>

        <h3>מדוע נדרשת רגולציה על מזון מהונדס?</h3>
        <p>פיתוח טכנולוגיית ההנדסה הגנטית במזון עורר דיונים ציבוריים ומדעיים נרחבים, שהובילו לצורך במסגרות רגולטוריות מחמירות במרבית מדינות העולם. מטרת הרגולציה היא לאזן בין הפוטנציאל הטכנולוגי והכלכלי של מזון מהונדס לבין הצורך הקריטי להגן על בריאות הציבור, בטיחות הסביבה ולקדם שקיפות לצרכנים. מטרות הרגולציה העיקריות כוללות:</p>
        <ul>
            <li><b>בטיחות הצרכן:</b> הערכה קפדנית של סיכונים בריאותיים פוטנציאליים, כגון יצירת רעלנים חדשים, הגברת אלרגניות של מזונות, או שינויים בלתי צפויים בהרכב התזונתי, הנובעים מהשינוי הגנטי.</li>
            <li><b>בטיחות הסביבה:</b> בחינת ההשפעות האפשריות על המגוון הביולוגי (biodiversity), כולל השפעה על אורגניזמים שאינם מטרה (כמו חרקים מועילים), פוטנציאל להתפשטות גנים מהונדסים לזני בר קרובים ("בריחת גנים"), והשפעה על שיטות חקלאיות (כמו התפתחות עמידות לקוטלי עשבים).</li>
            <li><b>שקיפות וזכות הציבור לדעת:</b> קביעת דרישות סימון ברורות על מוצרי מזון מהונדס, המאפשרות לצרכנים לקבל החלטות מושכלות בהתאם להעדפותיהם וערכיהם.</li>
        </ul>

        <h3>השחקנים המרכזיים בתהליך קבלת ההחלטות הרגולטורי</h3>
        <p>החלטה אם לאשר או לדחות מוצר מזון מהונדס היא לרוב תוצאה של תהליך מורכב המערב אינטראקציה ושקלול אינטרסים של גורמים שונים:</p>
        <ul>
            <li><b>גופים רגולטוריים ממשלתיים:</b> סוכנויות ורשויות ממשלתיות (דוגמת משרד הבריאות, משרד החקלאות, המשרד להגנת הסביבה) האחראיות על קביעת מדיניות, הערכת בקשות אישור, ביצוע הערכות סיכונים ופיקוח.</li>
            <li><b>קהילה מדעית ומומחי הערכת סיכונים:</b> מדענים וחוקרים באקדמיה ובמוסדות מחקר, המספקים נתונים, מבצעים מחקרים עצמאיים ומספקים חוות דעת מומחים לגופים הרגולטוריים.</li>
            <li><b>תעשיית הביוטכנולוגיה והמזון:</b> חברות מסחריות המפתחות את המוצרים המהונדסים ומגישות את בקשות האישור. הן לרוב מדגישות את היתרונות הפוטנציאליים של הטכנולוגיה - כלכליים, חקלאיים, תזונתיים וסביבתיים (למשל, הפחתת שימוש בחומרי הדברה מסוימים).</li>
            <li><b>ארגוני חברה אזרחית:</b> ארגונים ללא מטרות רווח המייצגים אינטרסים ציבוריים מגוונים, כגון ארגוני סביבה, ארגוני בריאות הציבור, ארגוני צרכנות, וארגונים העוסקים בזכויות חקלאים. הם לרוב מעלים חששות, דורשים שקיפות, מבקשים הערכות סיכון מחמירות יותר או מתנגדים עקרונית לטכנולוגיה.</li>
            <li><b>גורמים פוליטיים והציבור הרחב:</b> נבחרי ציבור ומקבלי החלטות פוליטיים מושפעים מלחצים פוליטיים, מאינטרסים כלכליים ומדעת הקהל. דעת הקהל עצמה מעוצבת על ידי תקשורת, ערכים אישיים, תפיסות סיכון (שלעיתים אינן תואמות הערכות סיכון מדעיות) ודיונים ציבוריים.</li>
        </ul>

        <h3>שקלול השיקולים: לב ליבה של הדילמה</h3>
        <p>החלטה רגולטורית אינה נגזרת אוטומטית מנתונים מדעיים בלבד. היא כוללת שקלול של מגוון רחב של היבטים:</p>
        <ul>
            <li><b>שיקולים מדעיים:</b> ראיות מבטיחות לבטיחות בריאותית וסביבתית, תוצאות מחקרים ארוכי וקצרי טווח, הערכת סיכון ספציפי למוצר.</li>
            <li><b>שיקולים כלכליים:</b> בחינת כדאיות לחקלאים, השפעה על מחירי המזון, יצוא/ייבוא, יצירת תלות טכנולוגית.</li>
            <li><b>שיקולים חברתיים ואתיים:</b> תפיסת סיכון ציבורית, דרישות סימון, התנגדויות ערכיות או דתיות, השפעה על חקלאות מקומית ומגוון זנים מסורתיים.</li>
            <li><b>שיקולים פוליטיים:</b> הסכמי סחר, יחסים בינלאומיים, לחצים מאיגודים ותעשיות, מדיניות ממשלתית רחבה יותר בנושאי חקלאות ובריאות.</li>
        </ul>

        <h3>אתגרים מרכזיים בתהליך הרגולציה</h3>
        <p>תהליך הרגולציה מורכב ורצוף אתגרים:</p>
        <ul>
            <li><b>אי-ודאות מדעית:</b> למרות המחקרים הרבים, לעיתים קיימת אי-ודאות מדעית לגבי השפעות ארוכות טווח או השפעות בלתי צפויות. הרגולציה נדרשת לפעול תחת עקרון הזהירות המונעת (Precautionary Principle).</li>
            <li><b>שקיפות ואמון ציבורי:</b> תהליך הרגולציה חייב להיות שקוף ומבוסס על מומחיות כדי לבנות אמון ציבורי, דבר שלעיתים מאותגר על ידי קמפיינים ציבוריים ואינטרסים מנוגדים.</li>
            <li><b>איזון בין חדשנות לזהירות:</b> הרגולטורים נדרשים לאזן בין הצורך לאפשר פיתוח טכנולוגי שיכול להניב תועלות (כמו הגדלת יבולים או הפחתת שימוש בחומרי הדברה) לבין הצורך להגן על הציבור והסביבה מפני סיכונים פוטנציאליים.</li>
        </ul>
        <p>האינטראקציה שבה התנסית מדגימה חלק קטן מהשיקולים הרבים שעמם מתמודדים צוותים רגולטוריים ברחבי העולם כשהם נדרשים להכריע בדילמות מורכבות מסוג זה.</p>
    </div>
</div>

<style>
    /* General Reset and Typography */
    body {
        font-family: 'Arial', sans-serif; /* Use a modern, readable font */
        line-height: 1.7; /* Improved readability */
        margin: 0;
        padding: 0; /* Use padding inside wrapper */
        background: linear-gradient(to bottom right, #eef2f7, #c9d6df); /* Subtle gradient background */
        color: #333;
        direction: rtl;
        text-align: right;
        min-height: 100vh; /* Full height background */
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding: 20px; /* Padding around the main content */
        box-sizing: border-box;
    }

    .simulation-wrapper {
        max-width: 800px; /* Max width for content */
        width: 100%;
        background-color: #ffffff; /* White background for content area */
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* Stronger shadow */
        box-sizing: border-box;
    }

    header h1 {
        color: #004085; /* Dark blue heading */
        text-align: center; /* Center the main title */
        margin-bottom: 15px;
        font-size: 2em; /* Larger title */
    }

    header p {
        text-align: center;
        margin-bottom: 30px;
        color: #555;
        font-size: 1.1em;
    }

    h2, h3, h4 {
        color: #0056b3; /* Standard blue for section titles */
        margin-top: 25px;
        margin-bottom: 15px;
        border-bottom: 1px solid #eee; /* Subtle separator */
        padding-bottom: 8px;
    }
     h3.results-title {
        border-bottom: none; /* No border for results title */
     }

    /* Interactive Section Styling */
    .interactive-section {
        background-color: #f8f9fa; /* Light grey background for interaction area */
        padding: 25px;
        border-radius: 8px;
        margin-bottom: 20px;
        border: 1px solid #e9ecef; /* Light border */
    }

    .interactive-section p {
        margin-bottom: 20px;
        color: #444;
    }

    /* Considerations List Styling */
    .considerations-list {
        margin-top: 20px;
        padding: 0; /* Remove padding, use item padding */
        list-style: none; /* Remove bullets */
    }

    .consideration-item {
        background-color: #fff; /* White background for each item */
        border: 1px solid #dee2e6; /* Light grey border */
        border-radius: 6px;
        margin-bottom: 12px; /* Space between items */
        padding: 15px;
        transition: all 0.3s ease; /* Smooth transition for hover/select */
        display: flex; /* Use flexbox for layout */
        align-items: flex-start; /* Align items to the top */
        cursor: pointer; /* Indicate clickable area */
    }

    .consideration-item:hover {
        border-color: #007bff; /* Highlight border on hover */
        box-shadow: 0 2px 8px rgba(0, 123, 255, 0.1); /* Subtle shadow on hover */
    }

    .consideration-checkbox {
        margin-left: 15px; /* Space for the checkbox */
        flex-shrink: 0; /* Prevent checkbox from shrinking */
        width: 20px; /* Standard checkbox size */
        height: 20px; /* Standard checkbox size */
        cursor: pointer;
        position: relative; /* Needed for custom styling if desired, but sticking to browser default for now */
        top: 4px; /* Adjust alignment */
    }

     .consideration-label {
         flex-grow: 1; /* Allow label to take up space */
         cursor: pointer;
         display: block; /* Make the whole label area clickable */
     }

     .consideration-label .label-text {
         display: block; /* Ensure text wraps correctly */
     }

     /* Visual feedback for selected item */
    .consideration-item.is-selected {
         background-color: #e9f7ef; /* Light green tint */
         border-color: #28a745; /* Green border */
         box-shadow: 0 2px 8px rgba(40, 167, 69, 0.15); /* Green shadow */
    }

    /* Icon Styling (using simple text characters for demonstration) */
    .consideration-label .icon-science::before { content: '🔬 '; color: #007bff; } /* Blue */
    .consideration-label .icon-food::before { content: '🌽 '; color: #ffc107; } /* Yellow/Orange */
    .consideration-label .icon-leaf::before { content: '🌿 '; color: #28a745; } /* Green */
    .consideration-label .icon-warning::before { content: '⚠️ '; color: #ff9800; } /* Orange */
    .consideration-label .icon-money::before { content: '💰 '; color: #17a2b8; } /* Teal */
    .consideration-label .icon-handshake::before { content: '🤝 '; color: #6c757d; } /* Grey */
    .consideration-label .icon-users::before { content: '🗣️ '; color: #dc3545; } /* Red */
    .consideration-label .icon-world::before { content: '🌍 '; color: #6610f2; } /* Purple */
    .consideration-label .icon-megaphone::before { content: '📣 '; color: #fd7e14; } /* Dark Orange */
    .consideration-label .icon-law::before { content: '⚖️ '; color: #6f42c1; } /* Violet */


    /* Highlight text colors */
    .highlight-positive { color: #28a745; font-weight: bold; } /* Green */
    .highlight-negative { color: #dc3545; font-weight: bold; } /* Red */
    .highlight-neutral { color: #007bff; font-weight: bold; } /* Blue */


    /* Button Styling */
    button {
        display: block; /* Full width button */
        width: 100%;
        background-color: #007bff; /* Primary blue */
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.2em; /* Larger font */
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth hover and press effect */
        font-weight: bold;
    }

    button.primary-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
    button.primary-button:active {
         transform: scale(0.98); /* Slightly shrink on press */
    }

     button.secondary-button {
         background-color: #6c757d; /* Secondary grey */
         margin-top: 30px; /* More space above toggle button */
     }
     button.secondary-button:hover {
         background-color: #5a6268; /* Darker grey on hover */
     }
     button.secondary-button:active {
         transform: scale(0.98);
     }

    /* Results Section Styling */
    .results-section {
        margin-top: 30px;
        padding: 20px;
        border-radius: 8px;
        /* Initial state for animation */
        opacity: 0;
        max-height: 0; /* Hide content */
        overflow: hidden;
        transition: opacity 0.6s ease-out, max-height 0.6s ease-out; /* Smooth transition */
        will-change: opacity, max-height; /* Performance hint */
    }

    .results-section.visible {
        opacity: 1;
        max-height: 1000px; /* Large enough max-height for content */
         /* Border and background set by JS based on decision */
    }

    .results-section.approved {
         border: 1px solid #28a745; /* Green border */
         background-color: #d4edda; /* Light green background */
         color: #155724; /* Dark green text */
    }

    .results-section.rejected {
         border: 1px solid #dc3545; /* Red border */
         background-color: #f8d7da; /* Light red background */
         color: #721c24; /* Dark red text */
    }


     .results-section h3,
     .results-section h4 {
         color: inherit; /* Inherit color from parent (.approved or .rejected) */
         border-bottom: none; /* Remove border below titles in results */
     }

    .decision-text {
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }

    .results-details {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px dashed rgba(0,0,0,0.1); /* Separator for details */
    }

    .selected-factors-list {
        list-style: disc inside; /* Keep bullet points */
        padding-right: 20px; /* Indent list */
        color: inherit; /* Inherit color */
    }
    .selected-factors-list li {
        margin-bottom: 8px;
    }

     .results-insight {
         font-style: italic;
         margin-top: 20px;
         padding-top: 15px;
         border-top: 1px dashed rgba(0,0,0,0.1);
         font-size: 0.95em;
         color: inherit;
     }


    /* Explanation Section Styling */
    .explanation-section {
        margin-top: 30px;
        padding-top: 30px;
        border-top: 2px solid #004085; /* Stronger separator */
        background-color: #eef2f7; /* Light blue background for explanation */
        padding: 25px;
        border-radius: 8px;
         /* Initial state for animation */
        opacity: 0;
        max-height: 0; /* Hide content */
        overflow: hidden;
        transition: opacity 0.6s ease-out, max-height 0.6s ease-out; /* Smooth transition */
        will-change: opacity, max-height; /* Performance hint */
    }
    .explanation-section.visible {
         opacity: 1;
         max-height: 2000px; /* Large enough max-height for content */
    }


    .explanation-section h3 {
        color: #0056b3;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px dotted #ccc;
        padding-bottom: 5px;
    }

    .explanation-section ul {
        list-style: disc inside;
        padding-right: 20px;
        margin-bottom: 20px;
    }
    .explanation-section li {
        margin-bottom: 8px;
    }

     .explanation-section p {
         margin-bottom: 15px;
         color: #444;
     }

     /* Responsive Adjustments (Basic) */
     @media (max-width: 600px) {
         .simulation-wrapper {
             padding: 20px;
         }
         header h1 {
             font-size: 1.8em;
         }
         button {
             font-size: 1.1em;
             padding: 10px 15px;
         }
         .consideration-item {
             padding: 12px;
         }
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const submitButton = document.getElementById('submit-decision');
        const resultsDiv = document.getElementById('results');
        const finalDecisionText = document.getElementById('final-decision-text');
        const selectedFactorsList = document.getElementById('selected-factors-list');
        const considerationsList = document.getElementById('considerations'); // Parent div for listeners
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationContent = document.getElementById('explanation-content');
        const resultsTitle = resultsDiv.querySelector('.results-title'); // Get the results title element

        // Add click listener to the parent div and use event delegation
        considerationsList.addEventListener('change', function(event) {
             if (event.target.classList.contains('consideration-checkbox')) {
                 const checkbox = event.target;
                 const considerationItem = checkbox.closest('.consideration-item');
                 if (checkbox.checked) {
                     considerationItem.classList.add('is-selected');
                 } else {
                     considerationItem.classList.remove('is-selected');
                 }
             }
        });


        submitButton.addEventListener('click', function() {
            const checkboxes = document.querySelectorAll('#considerations input[type="checkbox"]:checked');
            let totalWeight = 0;
            selectedFactorsList.innerHTML = ''; // Clear previous results

            checkboxes.forEach(checkbox => {
                const weight = parseInt(checkbox.getAttribute('data-weight'));
                totalWeight += weight;

                const listItem = document.createElement('li');
                // Get the text content of the label excluding the icon span if present
                const labelSpan = checkbox.nextElementSibling.querySelector('.label-text');
                const labelText = labelSpan ? labelSpan.textContent.replace(/🔬 |🌽 |🌿 |⚠️ |💰 |🤝 |🗣️ |🌍 |📣 |⚖️ /g, '').trim() : checkbox.nextElementSibling.textContent.trim(); // Basic fallback
                 const weightImpact = weight > 0 ? `+${weight} (מחזק אישור)` : (weight < 0 ? `${weight} (מחליש אישור)` : `${weight} (נטרלי)`);

                listItem.innerHTML = `<b>${labelText}</b> <span class="weight-impact">(${weightImpact})</span>`;
                selectedFactorsList.appendChild(listItem);
            });

            const threshold = 1; // Decision rule: total weight > 1 means Approved

            // Set result text and styling based on threshold
            if (totalWeight > threshold) {
                 resultsTitle.textContent = 'החלטת הצוות: אישור לשיווק!';
                finalDecisionText.textContent = `על בסיס השיקולים שבחרת, סך ההשפעה המשוקללת הוא ${totalWeight}. המסקנה הרגולטורית: המוצר עומד בקריטריונים ו<span class="highlight-positive">מאושר לשיווק</span>.`;
                resultsDiv.classList.remove('rejected');
                resultsDiv.classList.add('approved');
            } else {
                 resultsTitle.textContent = 'החלטת הצוות: דחייה או בדיקה נוספת';
                finalDecisionText.textContent = `על בסיס השיקולים שבחרת, סך ההשפעה המשוקללת הוא ${totalWeight}. המסקנה הרגולטורית: המוצר <span class="highlight-negative">אינו מאושר לשיווק בשלב זה</span> (דורש בדיקה נוספת / אינו עומד באופן מובהק בקריטריונים).`;
                 resultsDiv.classList.remove('approved');
                 resultsDiv.classList.add('rejected');
            }

            // Make results visible with animation
            resultsDiv.classList.add('visible');

            // Scroll to results smoothly after a short delay to allow animation to start
            setTimeout(() => {
                resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100); // Adjust delay as needed
        });

        toggleExplanationButton.addEventListener('click', function() {
            const isHidden = !explanationContent.classList.contains('visible'); // Check if it's currently not visible (i.e., hidden or initial state)
            if (isHidden) {
                explanationContent.classList.add('visible');
                this.textContent = 'הסתר רקע והסבר על דילמת המזון המהונדס ורגולציה';
                 // Scroll to explanation smoothly
                 setTimeout(() => {
                    explanationContent.scrollIntoView({ behavior: 'smooth', block: 'start' });
                 }, 100); // Adjust delay
            } else {
                explanationContent.classList.remove('visible');
                this.textContent = 'הצג/הסתר רקע והסבר על דילמת המזון המהונדס ורגולציה';
                // Optional: Scroll back up if hiding
                // setTimeout(() => {
                //     this.scrollIntoView({ behavior: 'smooth', block: 'start' });
                // }, 100);
            }
        });

        // Initial state: Ensure results and explanation are hidden
        resultsDiv.classList.remove('visible');
        explanationContent.classList.remove('visible');

         // Add class to consideration item when checkbox is checked initially (if page was refreshed with checkboxes checked)
         document.querySelectorAll('.consideration-checkbox:checked').forEach(checkbox => {
             checkbox.closest('.consideration-item').classList.add('is-selected');
         });

    });
</script>