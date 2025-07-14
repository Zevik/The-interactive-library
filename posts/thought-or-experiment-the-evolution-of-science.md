---
title: "מחשבה או ניסוי? מסע מרתק אל שחר המדע המודרני"
english_slug: thought-or-experiment-the-evolution-of-science
category: "מדעי הרוח / היסטוריה של המדע"
tags:
  - התפתחות המדע
  - פילוסופיה יוונית
  - אריסטו
  - גלילאו
  - השיטה המדעית
  - ניסוי
  - היגיון
---
# מחשבה או ניסוי? מסע מרתק אל שחר המדע המודרני

איך אנחנו באמת יודעים דברים על העולם? האם מספיק לשבת ולחשוב עמוק, או שחייבים לצאת ולבדוק במציאות? הצטרפו למסע קצר בזמן אל רגע מכונן בהיסטוריה האנושית, שבו השאלה הזו שינתה את הכול והניחה את היסודות לעולם המודרני שאנו מכירים.

<div id="science-evolution-app">
    <div id="app-question">
        <h2>האתגר:</h2>
        <p>דמיינו שאתם מחזיקים שני חפצים באותו גובה - אחד כבד מאוד, והשני קל מאוד. אם תשחררו אותם בו-זמנית, מה יקרה? האם אחד יגיע לקרקע לפני השני, או ששניהם יגיעו באותו רגע?</p>
        <p class="prompt-text">באיזו דרך תבחרו כדי לפתור את התעלומה הזו?</p>
    </div>

    <div id="app-choices" class="app-section">
        <button id="philosophical-btn" class="choice-btn philosophical">
            <span class="icon">🤔</span>
            גישה פילוסופית (בסגנון אריסטו)
        </button>
        <button id="scientific-btn" class="choice-btn scientific">
            <span class="icon">🧪</span>
            גישה מדעית (בסגנון גלילאו)
        </button>
    </div>

    <div id="philosophical-path" class="path-content app-section hidden">
        <h3>הגישה הפילוסופית: כוחה של המחשבה וההיגיון</h3>
        <p>בחרתם לצלול פנימה, לחשוב לעומק על השאלה, ולהתבסס על ההיגיון הפנימי ועל תצפיות יומיומיות לא מבוקרות על העולם שסביבנו.</p>

        <div class="thinking-animation">...מחשבה עמוקה מתנהלת...</div>

        <p><strong>המסקנה המתקבלת מהיגיון ותצפית פסיבית:</strong></p>
        <div class="conclusion philosophical-conclusion">
            <p>חפץ כבד מרגיש "נטייה" גדולה יותר לנוע מטה מאשר חפץ קל. זה הגיוני, כי הוא הרי כבד יותר! לכן, ברור שחפץ כבד ינוע מהר יותר ויגיע לקרקע ראשון.</p>
        </div>
        <p class="path-end-text">זה סוף ה'חקירה' בגישה הזו. ההיגיון קבע את התוצאה.</p>
        <button class="compare-btn next-step-btn">בואו נשווה מסקנות</button>
    </div>

    <div id="scientific-path" class="path-content app-section hidden">
        <h3>הגישה המדעית: כוחו של הניסוי והבדיקה</h3>
        <p>בחרתם בדרך הפעולה: לתכנן ניסוי מבוקר שיבדוק באופן אובייקטיבי מה באמת קורה.</p>

        <div id="experiment-setup" class="app-section">
            <p>תכנון הניסוי: נשחרר בו-זמנית כדור ברזל כבד וכדור עץ קל מאותו גובה, תוך ניסיון למזער את השפעת חיכוך האוויר ככל הניתן (נדמיין ואקום אידיאלי). </p>
            <p class="prompt-text">מוכנים לראות מה יקרה באמת?</p>
            <button id="perform-experiment-btn" class="next-step-btn">בצע את הניסוי המדעי</button>
        </div>

        <div id="experiment-simulation" class="app-section hidden">
            <p><strong>הניסוי מתבצע:</strong></p>
            <div class="falling-area">
                 <div class="drop-point">שחרור!</div>
                <div class="object heavy" data-label="כבד"></div>
                <div class="object light" data-label="קל"></div>
                <div class="ground"></div>
            </div>
            <div id="observation-data" class="data-box"></div>
            <div id="scientific-conclusion" class="conclusion scientific-conclusion"></div>
            <button class="compare-btn next-step-btn hidden">השווה מסקנות</button>
        </div>
    </div>

    <div id="comparison" class="app-section hidden">
        <h3>השוואת המסקנות: היגיון מול מציאות</h3>
        <div class="comparison-container">
            <div class="comparison-box philosophical-box">
                <h4>מסקנה פילוסופית (מבוססת היגיון):</h4>
                <p><span class="icon">🤔</span> חפץ כבד יותר נופל מהר יותר.</p>
            </div>
            <div class="comparison-box scientific-box">
                <h4>מסקנה מדעית (מבוססת ניסוי):</h4>
                <p><span class="icon">🧪</span> שני החפצים נפלו באותו קצב והגיעו לקרקע כמעט בו-זמנית (בהזנחת חיכוך אוויר).</p>
            </div>
        </div>
        <p class="comparison-summary">כפי שגלילאו גילה (גם אם לא בהכרח זרק כדורים ממגדל פיזה המפורסם, רוח הניסוי נכונה), הניסוי המבוקר הראה שתופעת הנפילה החופשית אינה תלויה במסת האובייקט (בהיעדר כוחות כמו חיכוך אוויר). זו דוגמה עוצמתית לכך שבמדע, האמפיריה - הבדיקה בעולם המעשי - גוברת על ההיגיון הטהור או על תצפית שטחית בלבד.</p>
        <button id="restart-btn" class="next-step-btn">התחל מסע חדש</button>
    </div>
</div>

<button id="toggle-explanation-btn" class="explanation-btn">הצג סיפור מלא: ההתפתחות ההיסטורית של המדע</button>

<div id="full-explanation" class="hidden">
    <h2>ההתפתחות ההיסטורית של הגישה המדעית: מהפכה בחשיבה האנושית</h2>

    <h3>הקדמה: איך נדע מהי האמת?</h3>
    <p>מאז ומעולם, בני האדם ניסו להבין את העולם המופלא שסביבם. השאלה הגדולה הייתה תמיד: כיצד נוכל לרכוש ידע אמין ויציב על הטבע? האם הדרך היא באמצעות חשיבה והתפלפלות אינטלקטואלית, או דווקא על ידי בדיקה מעשית של רעיונות?</p>

    <h3>העולם היווני העתיק: עידן הפילוסופיה והרציונליזם</h3>
    <ul>
        <li>בתקופה זו, ההבנה העמוקה של העולם התבססה בעיקר על **רציונליזם** (היגיון) ועל תצפיות לא שיטתיות. הפילוסופים המובילים ניסו לחדור לעומק מהות הדברים ולגלות את עקרונותיהם הראשוניים באמצעות דיון, הגות והיגיון.</li>
        <li>**אריסטו - המורה של העולם העתיק:** אריסטו (המאה ה-4 לפנה"ס) היה דמות ענקית שהשפיעה על המחשבה המערבית במשך כאלפיים שנה! הוא בנה שיטה מקיפה להבנת הטבע שהתבססה על מושגים כמו "איכויות", "טבע" ו"תכלית" (טלאולוגיה). לשיטתו, לכל דבר יש תכלית ומקום טבעי ביקום. אבן, למשל, "רוצה" להגיע למטה כי מקומה הטבעי הוא באדמה, ואש "שואפת" לעלות למעלה כי מקומה הוא בשמיים.</li>
        <li>**תפיסת הנפילה אצל אריסטו:** בהתאם לגישתו, אריסטו הסיק (מתוך היגיון ותצפית יומיומית, שבה לרוב יש חיכוך אוויר) שחפצים כבדים נופלים מהר יותר מחפצים קלים. ההסבר היה שהנטייה הטבעית שלהם לנוע למקום ה"נכון" שלהם (מטה) חזקה יותר ככל שהם כבדים יותר. תפיסה זו נראתה הגיונית להפליא ונלמדה כעובדה במשך דורות רבים.</li>
    </ul>
    <p>גישה זו, שהעדיפה היגיון על פני בדיקה אמפירית מבוקרת, שלטה בעולם המדע והפילוסופיה למשך תקופה ארוכה מאוד.</p>

    <h3>המהפכה המדעית: שינוי דרמטי</h3>
    <p>בין המאות ה-16 וה-17 התחוללה מהפכה אדירה באופן שבו בני אדם מחפשים ידע. יותר ויותר חוקרים החלו לפקפק באמיתות שהתקבלו רק על סמך סמכות (כמו זו של אריסטו) או היגיון בלבד, והחלו להדגיש את הצורך ב**תצפית מדויקת וניסוי מבוקר**.</p>
    <ul>
        <li>**ענקי המהפכה:**
            <ul>
                <li>**ניקולאוס קופרניקוס:** העז להציע מודל שבו כדור הארץ סובב סביב השמש (מודל הליוצנטרי), בניגוד לתפיסה שהייתה מקובלת אלפי שנים (מודל גיאוצנטרי, שבו כדור הארץ במרכז). הצעתו התבססה על חישובים ותצפיות אסטרונומיות.</li>
                <li>**יוהנס קפלר:** גילה את חוקי תנועת כוכבי הלכת לא על סמך פילוסופיה, אלא על בסיס ניתוח מתמטי קפדני של נתוני תצפית מדויקים שנאספו על ידי טיכו ברהה.</li>
                <li>**אייזק ניוטון:** סיכם את המהפכה עם חוקי התנועה והכבידה האוניברסלית. הוא הראה שניתן לאחד תופעות שונות (תפוח נופל, ירח מסתובב) באמצעות חוקים מתמטיים אחידים, שנבחנו ואומתו באמצעות ניסויים ותצפיות.</li>
            </ul>
        </li>
        <li>**גלילאו גליליי - אב המדע המודרני:** גלילאו היה דמות מפתח בתנועה זו. הוא הבין את החשיבות המכרעת של:
            <ul>
                <li>**המתמטיקה:** לראות בטבע לא רק אוסף של איכויות, אלא מנגנון הפועל לפי חוקים מתמטיים מדויקים שניתנים למדידה.</li>
                <li>**הניסוי המבוקר:** לא להסתפק בתצפית פסיבית, אלא לתכנן ניסויים שבהם ניתן לשלוט על התנאים, לבודד משתנים ולבצע מדידות כמותיות. באמצעות ניסויים כאלה (למשל, על גופים המתגלגלים במורד מישור משופע, שיטה שאפשרה לבחון תאוצה בצורה מדויקת יותר מאשר נפילה חופשית מהירה), גלילאו ערער על רבות מתפיסות אריסטו, כולל זו של הנפילה החופשית. הניסויים שלו הוכיחו שקצב הנפילה של גופים אינו תלוי ליניארית במסה שלהם, כפי שחשבו עד אז.</li>
            </ul>
        </li>
    </ul>

    <h3>השיטה המדעית: הדרך המודרנית לידע</h3>
    <p>המהפכה המדעית הולידה את **השיטה המדעית** - מסגרת פעולה שיטתית לרכישת ידע: </p>
    <ol>
        <li>**תצפית ושאלה:** מתחילים בלשים לב לתופעה ומנסחים שאלה ספציפית עליה.</li>
        <li>**השערה:** מציעים הסבר אפשרי לתופעה - השערה שחייבת להיות ניתנת לבדיקה.</li>
        <li>**תכנון ניסוי:** יוצרים תוכנית מדויקת לבדיקת ההשערה, תוך שליטה על גורמים שונים (משתנים) כדי לבודד את ההשפעה הנבדקת.</li>
        <li>**ביצוע ניסוי ואיסוף נתונים:** מבצעים את הניסוי ואוספים נתונים בצורה אובייקטיבית וכמותית ככל האפשר.</li>
        <li>**ניתוח נתונים והסקת מסקנות:** בוחנים את הנתונים ומחליטים האם הם תומכים בהשערה או מפריכים אותה. המסקנה מבוססת על הראיות (הנתונים), לא על דעה מוקדמת.</li>
        <li>**פרסום ובקרה עמיתים:** משתפים את התוצאות והשיטה עם חוקרים אחרים, המאפשרים שחזור של הניסוי ואימות או הפרכה עצמאית של המסקנות.</li>
    </ol>

    <h3>למה השיטה המדעית כל כך יעילה?</h3>
    <ul>
        <li>**אובייקטיביות:** היא מתבססת על ראיות (נתונים) שכל אחד יכול לבדוק, ולא על דעות או אמונות אישיות.</li>
        <li>**דיוק:** שימוש במדידה ומתמטיקה מאפשר הבנה כמותית ומדויקת של העולם.</li>
        <li>**ידע מצטבר וניתן להפרכה:** ידע מדעי נבנה שכבות-שכבות, וכל רעיון פתוח לבדיקה ולהפרכה באמצעות ראיות חדשות. זה מאפשר התקדמות מתמדת.</li>
        <li>**יישום טכנולוגי:** ההבנה המדויקת של חוקי הטבע שמתאפשרת בזכות המדע היא הבסיס לכל הטכנולוגיה המודרנית, שמקיפה אותנו בכל מקום.</li>
    </ul>
    <p>לסיכום, בעוד שהיגיון הוא כלי חיוני וחלק בלתי נפרד מהשיטה המדעית, ההבדל המכריע של המדע המודרני הוא ההתעקשות על בדיקה אמפירית שיטתית ומבוקרת כמבחן האולטימטיבי לאמיתות רעיון. המסע ממחשבה לניסוי הוא המסע שיצר את העולם שבו אנו חיים.</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #28a745;
        --warning-color: #ffc107;
        --danger-color: #dc3545;
        --info-color: #17a2b8;
        --light-bg: #f8f9fa;
        --dark-text: #343a40;
        --border-color: #dee2e6;
        --card-bg: #ffffff;
        --philosophical-color: #6f42c1; /* Purple */
        --scientific-color: #20c997; /* Teal */
    }

    #science-evolution-app {
        font-family: 'Arial', sans-serif;
        max-width: 750px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background: linear-gradient(to bottom right, var(--light-bg), #e9ecef);
        color: var(--dark-text);
        text-align: center;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        direction: rtl; /* RTL support */
        text-align: right; /* Default text align */
    }

    #science-evolution-app h2 {
        color: var(--primary-color);
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.8em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        display: inline-block; /* Border only under text */
        text-align: center;
        width: 100%;
    }

    #app-question p {
        font-size: 1.1em;
        margin-bottom: 20px;
        line-height: 1.6;
        text-align: center; /* Question text is centered */
    }

    .prompt-text {
         font-weight: bold;
         color: var(--dark-text);
         margin-top: 20px;
         font-size: 1.1em;
         text-align: center;
    }

    .app-section {
        background-color: var(--card-bg);
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
    }

    .app-section.hidden {
        opacity: 0;
        visibility: hidden;
        max-height: 0; /* Collapse height for smooth transition */
        overflow: hidden;
        padding-top: 0;
        padding-bottom: 0;
        margin-top: 0;
        margin-bottom: 0;
        transform: translateY(20px);
    }


    #app-choices {
        display: flex;
        justify-content: center;
        gap: 20px; /* Space between buttons */
        flex-wrap: wrap; /* Allow wrapping */
    }

    .choice-btn {
        padding: 15px 25px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 30px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        color: white;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
        text-align: right;
    }

    .choice-btn .icon {
        font-size: 1.5em;
    }

    #philosophical-btn {
        background-color: var(--philosophical-color);
        box-shadow: 0 4px 6px rgba(111, 66, 193, 0.3);
    }

    #philosophical-btn:hover {
        background-color: #5a37a8; /* Darker purple */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(111, 66, 193, 0.4);
    }

    #scientific-btn {
        background-color: var(--scientific-color);
        box-shadow: 0 4px 6px rgba(32, 201, 151, 0.3);
    }

    #scientific-btn:hover {
        background-color: #1a9b7a; /* Darker teal */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(32, 201, 151, 0.4);
    }


    .path-content h3 {
        color: var(--primary-color);
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 10px;
        margin-bottom: 15px;
        text-align: center;
        font-size: 1.6em;
    }

    .thinking-animation {
        font-style: italic;
        color: #666;
        margin: 20px 0;
        min-height: 1.5em; /* Reserve space */
        animation: pulse 1.5s infinite ease-in-out;
        text-align: center;
    }

    @keyframes pulse {
        0% { opacity: 0.7; }
        50% { opacity: 1; }
        100% { opacity: 0.7; }
    }


    .conclusion {
        margin: 25px 0;
        padding: 15px;
        border-left: 5px solid; /* Use border-left for emphasis */
        border-radius: 5px;
        background-color: #f0f0f0;
        font-style: italic;
        line-height: 1.5;
        text-align: right;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .philosophical-conclusion {
         border-color: var(--philosophical-color);
         background-color: #f3e5ff; /* Light purple */
    }
    .scientific-conclusion {
         border-color: var(--scientific-color);
         background-color: #e6fffa; /* Light teal */
    }

    .conclusion p {
        margin: 0;
        padding: 5px 0;
    }
     .conclusion strong {
        color: var(--dark-text);
        font-style: normal;
     }

    .path-end-text {
        font-size: 1em;
        color: #555;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
    }


    #experiment-setup {
        text-align: center;
    }

    .next-step-btn {
        padding: 12px 25px;
        font-size: 1.1em;
        border: none;
        border-radius: 25px; /* Rounded buttons */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: bold;
        margin-top: 20px;
    }

    #perform-experiment-btn {
        background-color: var(--warning-color);
        color: var(--dark-text);
        box-shadow: 0 4px 6px rgba(255, 193, 7, 0.3);
    }

    #perform-experiment-btn:hover {
        background-color: #e0a800; /* Darker warning */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(255, 193, 7, 0.4);
    }

    .compare-btn {
        background-color: var(--info-color);
        color: white;
        box-shadow: 0 4px 6px rgba(23, 162, 184, 0.3);
    }

    .compare-btn:hover {
        background-color: #138496; /* Darker info */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(23, 162, 184, 0.4);
    }

    #restart-btn {
        background-color: var(--danger-color);
        color: white;
        box-shadow: 0 4px 6px rgba(220, 53, 69, 0.3);
    }
    #restart-btn:hover {
        background-color: #c82333; /* Darker danger */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(220, 53, 69, 0.4);
    }

    #experiment-simulation {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .falling-area {
        width: 150px; /* Wider for better visual */
        height: 300px; /* Taller drop */
        border: 2px solid var(--dark-text);
        margin: 30px auto;
        position: relative;
        overflow: hidden;
        background: linear-gradient(to bottom, #87ceeb, #e0f7fa); /* Sky gradient */
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }

    .drop-point {
        position: absolute;
        top: 5px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.9em;
        color: var(--dark-text);
        font-weight: bold;
    }

    .object {
        width: 25px; /* Slightly larger */
        height: 25px;
        border-radius: 50%;
        position: absolute;
        top: -30px; /* Start slightly above view */
        left: 50%;
        transform: translateX(-50%);
        transition: top 2.5s cubic-bezier(0.4, 0, 0.2, 1); /* Ease out for realism? Or linear? Linear is physically accurate. Let's try cubic-bezier for visual feel */
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8em;
        color: white;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    .object::before {
         content: attr(data-label); /* Use data-label for text */
    }


    .heavy {
        background-color: var(--danger-color); /* Red */
        margin-left: -20px; /* Separate */
    }

    .light {
        background-color: var(--info-color); /* Cyan */
        margin-left: 20px; /* Separate */
    }

     .ground {
        width: 100%;
        height: 20px; /* Thicker ground */
        background-color: #8b4513; /* Brown */
        position: absolute;
        bottom: 0;
        left: 0;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.2);
     }

    .data-box {
        margin-top: 15px;
        padding: 10px 15px;
        border: 1px dashed var(--info-color);
        background-color: #e6f7ff;
        font-weight: bold;
        color: var(--dark-text);
        border-radius: 5px;
        min-height: 1.5em; /* Reserve space */
        text-align: center;
    }


    #comparison h3 {
         color: var(--primary-color);
         text-align: center;
         border-bottom: 1px dashed var(--border-color);
         padding-bottom: 10px;
         margin-bottom: 20px;
         font-size: 1.6em;
    }

    .comparison-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 20px; /* Space between boxes */
        margin-bottom: 20px;
    }

    .comparison-box {
        border: 2px solid;
        padding: 20px;
        flex: 1;
        min-width: 280px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .philosophical-box {
         border-color: var(--philosophical-color);
         background-color: #f3e5ff; /* Light purple */
    }
     .scientific-box {
         border-color: var(--scientific-color);
         background-color: #e6fffa; /* Light teal */
    }

     .comparison-box h4 {
         margin-top: 0;
         color: var(--dark-text);
         font-size: 1.3em;
         margin-bottom: 15px;
     }
    .comparison-box p {
        font-size: 1.1em;
        line-height: 1.5;
        margin: 0;
    }
    .comparison-box .icon {
        font-size: 1.8em;
        margin-bottom: 10px;
    }
    .philosophical-box .icon { color: var(--philosophical-color); }
    .scientific-box .icon { color: var(--scientific-color); }


    .comparison-summary {
        font-size: 1em;
        line-height: 1.6;
        color: #555;
        text-align: center;
        margin-top: 30px;
    }


    .explanation-btn {
         display: block;
         width: fit-content;
         margin: 30px auto;
         padding: 12px 25px;
         font-size: 1.1em;
         background-color: var(--info-color);
         color: white;
         border: none;
         border-radius: 25px;
         cursor: pointer;
         transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
         font-weight: bold;
         box-shadow: 0 4px 6px rgba(23, 162, 184, 0.3);
    }
     .explanation-btn:hover {
         background-color: #138496;
         transform: translateY(-2px);
         box-shadow: 0 6px 8px rgba(23, 162, 184, 0.4);
     }

    #full-explanation {
         margin-top: 20px;
         padding: 25px;
         border: 1px solid var(--border-color);
         border-radius: 10px;
         background-color: var(--light-bg);
         text-align: right; /* RTL support */
         direction: rtl; /* RTL support */
         line-height: 1.7;
         color: var(--dark-text);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
         transition: opacity 0.5s ease-in-out;
         opacity: 1;
         visibility: visible;
         max-height: 5000px; /* Sufficiently large */
         overflow: hidden;
    }
    #full-explanation.hidden {
         opacity: 0;
         visibility: hidden;
         max-height: 0; /* Collapse height */
         padding-top: 0;
         padding-bottom: 0;
         margin-top: 0;
    }


    #full-explanation h2 {
        color: var(--primary-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 8px;
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.8em;
        text-align: right; /* Align explanation title right */
        display: block;
        width: 100%;
    }
     #full-explanation h3 {
        color: var(--dark-text);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.4em;
     }
      #full-explanation strong {
          color: var(--primary-color);
      }
     #full-explanation ul, #full-explanation ol {
         margin-bottom: 15px;
         padding-right: 20px; /* Indent lists */
     }
     #full-explanation li {
         margin-bottom: 10px;
         line-height: 1.6;
     }


    /* Responsive Adjustments */
    @media (max-width: 600px) {
        #science-evolution-app {
            padding: 15px;
        }
        #app-choices {
            flex-direction: column;
            align-items: stretch;
        }
        .choice-btn {
            font-size: 1em;
            padding: 12px 20px;
            justify-content: center;
        }
        .comparison-container {
            flex-direction: column;
            align-items: stretch;
        }
        .comparison-box {
            min-width: auto; /* Allow boxes to shrink on small screens */
        }
         .next-step-btn, .explanation-btn {
             width: 100%; /* Full width buttons on small screens */
             box-sizing: border-box; /* Include padding/border in width */
         }
         .falling-area {
             width: 100px;
             height: 250px;
         }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const appQuestion = document.getElementById('app-question');
        const appChoices = document.getElementById('app-choices');
        const philosophicalPath = document.getElementById('philosophical-path');
        const scientificPath = document.getElementById('scientific-path');
        const experimentSetup = document.getElementById('experiment-setup');
        const experimentSimulation = document.getElementById('experiment-simulation');
        const observationData = document.getElementById('observation-data');
        const scientificConclusionDiv = document.getElementById('scientific-conclusion');
        const comparison = document.getElementById('comparison');
        const philosophicalBtn = document.getElementById('philosophical-btn');
        const scientificBtn = document.getElementById('scientific-btn');
        const performExperimentBtn = document.getElementById('perform-experiment-btn');
        const compareBtns = document.querySelectorAll('.compare-btn');
        const restartBtn = document.getElementById('restart-btn');
        const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
        const fullExplanation = document.getElementById('full-explanation');
        const heavyObject = document.querySelector('.object.heavy');
        const lightObject = document.querySelector('.object.light');
        const fallingArea = document.querySelector('.falling-area'); // Get the falling area element

        const fallingAreaHeight = fallingArea.offsetHeight; // Get height for animation
        const objectHeight = heavyObject.offsetHeight; // Assuming both objects are same height
        const finalTop = `${fallingAreaHeight - objectHeight}px`; // Calculate final position

        const sections = [appQuestion, appChoices, philosophicalPath, scientificPath, comparison, fullExplanation];

        function hideAllSections() {
            sections.forEach(section => {
                if (section) { // Check if element exists
                     section.classList.add('hidden');
                }
            });
        }

        function showSection(section) {
            if (section) {
                 section.classList.remove('hidden');
            }
        }

        function resetApp() {
            hideAllSections();
            showSection(appQuestion);
            showSection(appChoices);

            // Reset specific path states
            if(philosophicalPath) philosophicalPath.querySelector('.compare-btn').classList.add('hidden');
            if(scientificPath) {
                showSection(experimentSetup);
                hideSection(experimentSimulation); // Use helper function to hide with animation
                 if(scientificPath.querySelector('.compare-btn')) scientificPath.querySelector('.compare-btn').classList.add('hidden');
            }


            observationData.textContent = '';
            scientificConclusionDiv.textContent = '';

             // Reset object positions immediately without transition
            if(heavyObject) heavyObject.style.transition = 'none';
            if(lightObject) lightObject.style.transition = 'none';
             if(heavyObject) heavyObject.style.top = '-30px'; // Start slightly above
             if(lightObject) lightObject.style.top = '-30px';

             // Re-enable transition after a short delay to allow position reset to take effect
             setTimeout(() => {
                if(heavyObject) heavyObject.style.transition = 'top 2.5s cubic-bezier(0.4, 0, 0.2, 1)';
                if(lightObject) lightObject.style.transition = 'top 2.5s cubic-bezier(0.4, 0, 0.2, 1)';
             }, 50); // Small delay


             // Ensure explanation is hidden by default
             if(fullExplanation) fullExplanation.classList.add('hidden');
             if(toggleExplanationBtn) toggleExplanationBtn.textContent = 'הצג סיפור מלא: ההתפתחות ההיסטורית של המדע';
        }

        function hideSection(section) {
             if (section) {
                section.classList.add('hidden');
                // Optionally, reset scroll position if needed
                // section.scrollTop = 0;
            }
        }


        function startPhilosophicalPath() {
            hideAllSections();
            showSection(philosophicalPath);
            // Show compare button after a slight delay for effect
            setTimeout(() => {
                 if(philosophicalPath) philosophicalPath.querySelector('.compare-btn').classList.remove('hidden');
            }, 1000); // Delay showing the button
        }

        function startScientificPath() {
            hideAllSections();
            showSection(scientificPath);
            showSection(experimentSetup);
            hideSection(experimentSimulation);
        }

        function performExperiment() {
            hideSection(experimentSetup);
            showSection(experimentSimulation);

            // Trigger animation
            if(heavyObject) heavyObject.style.top = finalTop;
            if(lightObject) lightObject.style.top = finalTop;

            // After animation (simulated with timeout)
            const animationDurationMs = 2500; // Should match CSS transition duration
            setTimeout(() => {
                observationData.textContent = "נתונים מהניסוי: שני החפצים הגיעו לקרקע כמעט באותו הזמן!";
                scientificConclusionDiv.innerHTML = `
                    <p><strong>מסקנה מבוססת נתונים:</strong></p>
                    <p>כפי שניתן לראות, שני החפצים נפלו באותו קצב והגיעו לקרקע בו-זמנית, ללא תלות משמעותית במסה (בהזנחת חיכוך אוויר). המציאות הפתיעה את ההיגיון הטהור!</p>
                `;
                 // Show compare button after conclusion is visible
                setTimeout(() => {
                     if(scientificPath) scientificPath.querySelector('.compare-btn').classList.remove('hidden');
                }, 500); // Delay showing button slightly after conclusion appears

            }, animationDurationMs + 200); // Slightly longer than animation duration
        }

        function showComparison() {
            hideAllSections();
            showSection(comparison);
        }

        function toggleExplanation() {
            if (fullExplanation.classList.contains('hidden')) {
                showSection(fullExplanation);
                toggleExplanationBtn.textContent = 'הסתר סיפור מלא: ההתפתחות ההיסטורית של המדע';
            } else {
                hideSection(fullExplanation);
                toggleExplanationBtn.textContent = 'הצג סיפור מלא: ההתפתחות ההיסטורית של המדע';
            }
        }

        // Initial state
        resetApp();

        // Event Listeners
        if(philosophicalBtn) philosophicalBtn.addEventListener('click', startPhilosophicalPath);
        if(scientificBtn) scientificBtn.addEventListener('click', startScientificPath);
        if(performExperimentBtn) performExperimentBtn.addEventListener('click', performExperiment);

        compareBtns.forEach(btn => {
            btn.addEventListener('click', showComparison);
        });

        if(restartBtn) restartBtn.addEventListener('click', resetApp);
        if(toggleExplanationBtn) toggleExplanationBtn.addEventListener('click', toggleExplanation);

         // Ensure sections are hidden correctly on load after DOM is ready
         hideSection(philosophicalPath);
         hideSection(scientificPath);
         hideSection(comparison);
         hideSection(fullExplanation); // Ensure explanation is hidden initially
    });
</script>