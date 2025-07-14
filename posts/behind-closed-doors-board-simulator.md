---
title: "מאחורי דלתות סגורות: סימולטור דירקטוריון"
english_slug: behind-closed-doors-board-simulator
category: "ניהול"
tags:
  - דירקטוריון
  - קבלת החלטות
  - חברה ציבורית
  - ממשל תאגידי
  - ניהול סיכונים
---
<h1>מאחורי דלתות סגורות: סימולטור דירקטוריון</h1>

<p class="intro-text">המסע אל לב ליבה של קבלת ההחלטות התאגידית. האם יש לך את מה שנדרש כדי לנווט בין אי-ודאות, לחצים והטיות קוגניטיביות, ולהוביל חברה ציבורית להצלחה?</p>

<div class="simulator-container board-room-theme">
    <div class="scenario-section">
        <h2 class="section-title">תרחיש מול הדירקטוריון: הזדמנות פינטק לוהטת</h2>
        <p id="scenario-description">אתה יושב סביב שולחן עץ מהגוני כבד בחדר הדירקטוריון של 'טקסטארט בע"מ', חברת טכנולוגיה ותיקה ורווחית, אך כזו המחפשת נואשות מנועי צמיחה חדשים בשוק טכנולוגיה תחרותי וסטטי. על סדר היום: רכישת 'פינטק חדשנות', סטארטאפ מבטיח ופורץ דרך בתחום הפינטק הפיננסי המקוון. הסטארטאפ צומח במהירות אך עדיין שורף מזומנים ורחוק מרווחיות. השווי המבוקש על ידם גבוה משמעותית מהכנסותיהם הנוכחיות, ומחייב את 'טקסטארט' לגייס הון או לממן את העסקה מיתרות המזומנים הגדולות שלה - מהלך שיכול להשפיע מהותית על יציבותה הפיננסית בטווח הקצר.</p>

        <div class="info-brief">
            <h3>המידע שעל השולחן:</h3>
            <ul>
                <li>מצגת ראשונית מרשימה של מנכ"ל 'פינטק חדשנות'.</li>
                <li>דוחות כספיים חלקיים ובלתי מבוקרים של הסטארטאפ.</li>
                <li>הערכת שווי פנימית ראשונית שביצע צוות פיתוח עסקי פנימי, הנאמדת בהערכת שווי נמוכה מהמבוקש על ידי הסטארטאפ.</li>
                <li>מידע על מספר חברות טק אחרות המגלות עניין ברכישת 'פינטק חדשנות'.</li>
                <li>לחץ הולך וגובר מבעלי מניות גדולים, המעוניינים ב"עסקת כותרת" שתקפיץ את מחיר המניה.</li>
            </ul>
        </div>
        
        <p>הזמן קצוב. יש להגיע להחלטה שתשרת את טובת החברה ובעלי מניותיה בטווח הארוך, תוך ניהול הסיכונים הקיימים. עיני ההנהלה ובעלי המניות נשואות אליך. מה תהיה עמדתך?</p>
    </div>

    <div class="decision-options" id="decision-options">
        <!-- Buttons will be populated by JS -->
    </div>

    <div class="outcome-container" id="outcome-container">
        <h2 id="outcome-title"></h2>
        <div id="outcome-details"></div>
        <div class="feedback-section">
            <h3>המשוב על החלטתך: ניתוח ההשלכות</h3>
            <div id="outcome-feedback"></div>
        </div>
         <button class="restart-button" id="restart-simulation" style="display: none;">חזור להתחלה / נסה שוב</button>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הסבר מעמיק: הדירקטוריון בפעולה (הצג)</button>

<div id="explanation" class="explanation-section">
    <h2 class="section-title">הסבר מעמיק: עולם הדירקטוריון</h2>
    <p>כדירקטור, החלטתך אינה רק עניין של אינטואיציה עסקית. היא מושפעת מחובות משפטיות ואתיות, מהקשר השוק, מהדינמיקה האנושית בחדר, ומעקרונות ממשל תאגידי שנועדו להגן על החברה ובעלי מניותיה.</p>

    <h3>מהו דירקטוריון ומה תפקידיו בחברה ציבורית?</h3>
    <p>הדירקטוריון הוא הגוף המנהל העליון בחברה ציבורית. הוא אינו אחראי על הניהול השוטף (זה תפקיד המנכ"ל וההנהלה), אלא על קביעת האסטרטגיה הכוללת, פיקוח על פעילות ההנהלה, אישור עסקאות מהותיות (כמו רכישות, מיזוגים, גיוסי הון), מינוי ופיטורי המנכ"ל, ואישור דוחות כספיים. תפקידו העיקרי הוא להבטיח שהחברה מנוהלת באופן תקין, אחראי ויעיל, למען טובת החברה בטווח הארוך.</p>

    <h3>האחריות המשפטית והאתית של דירקטורים (חובת אמון, חובת זהירות)</h3>
    <p>לדירקטורים חובות כבדות מכוח החוק והפסיקה. <strong>חובת האמון</strong> מחייבת אותם לפעול בתום לב, לטובת החברה ולמענה בלבד, ולהימנע מכל ניגוד עניינים אישי. <strong>חובת הזהירות</strong> מחייבת אותם להקדיש תשומת לב ראויה לענייני החברה, לבצע בדיקה ולימוד נאותים של הנושאים הנדונים (בדיקת נאותות - Due Diligence), להשתתף בישיבות, לשאול שאלות, ולדרוש את כל המידע הדרוש לקבלת החלטה מושכלת, כאדם סביר שהיה נושא באותה משרה ומתאפיין באותה מומחיות. הפרת חובות אלו עלולה לגרור אחריות אישית (אזרחית ואף פלילית במקרים חמורים).</p>

    <h3>האתגרים המרכזיים בקבלת החלטות בדירקטוריון</h3>
    <p>גם בדירקטוריון מנוסה, קבלת החלטות אינה תהליך פשוט: <strong>מידע חלקי או מוטה</strong> (ההנהלה או בעלי עניין אחרים עשויים להציג מידע באופן מגמתי); <strong>דינמיקה קבוצתית ולחץ חברתי</strong> ("חשיבת יחד" - הימנעות מהבעת דעות מנוגדות כדי לא לערער את הקונצנזוס, לחץ מצד יושב ראש הדירקטוריון או מנכ"ל); <strong>קונפליקטים וניגודי עניינים</strong> (בין דירקטורים לבין עצמם, בינם לבין ההנהלה, או בינם לבין בעלי השליטה); <strong>אי-ודאות לגבי העתיד</strong> (שווקים משתנים, טכנולוגיות חדשות, שינויים רגולטוריים); וכן <strong>הטיות קוגניטיביות</strong> אנושיות (כמו הטיית אישור - חיפוש מידע שתומך בעמדה קיימת; הטיית עוגן - היצמדות לנתון ראשוני שסופק; הטיית הימנעות מהפסד - פחד מסיכון גם כשהוא סביר וההזדמנות גדולה). דירקטוריון טוב יודע לזהות ולהתמודד עם אתגרים אלו.</p>

    <h3>סוגי החלטות אסטרטגיות שמקבל הדירקטוריון</h3>
    <p>החלטות הדירקטוריון מעצבות את עתיד החברה. הן כוללות, בין היתר: אישור עסקאות מיזוג ורכישה בקנה מידה משמעותי; מינוי, פיטורים ובקרה על עבודת המנכ"ל ובכירי ההנהלה; אישור אסטרטגיה עסקית ארוכת טווח ותוכניות עבודה שנתיות; אישור דוחות כספיים וחלוקת דיבידנדים; אישור עסקאות עם בעלי שליטה או בעלי עניין אחרים (עסקאות שעלולות לטמון בחובן ניגוד עניינים); ואישור תוכניות תגמול לבכירים.</p>

    <h3>החשיבות של מגוון בדירקטוריון וכיצד הוא יכול להשפיע על איכות ההחלטות</h3>
    <p>דירקטוריון המורכב מאנשים בעלי רקע מקצועי מגוון (פיננסים, טכנולוגיה, שיווק, משפט, רגולציה, ניהול תפעולי), ניסיון חיים שונה (גיל, מגדר, רקע תרבותי) ונקודות מבט מנוגדות, הוא נכס אדיר לחברה. מגוון כזה מעודד דיון פתוח ומאתגר, חשיפה רחבה יותר של סיכונים והזדמנויות, ומקטין את הסיכון ל"חשיבת יחד" ולהטיות קוגניטיביות. דירקטוריון מגוון מקבל לרוב החלטות טובות ומאוזנות יותר.</p>

    <h3>ממשל תאגידי (Corporate Governance) - עקרונות והשפעתם</h3>
    <p>ממשל תאגידי הוא התשתית החוקית והניהולית המבטיחה שהחברה מנוהלת ומבוקרת כראוי. עקרונות ממשל תאגידי נאות כוללים: <strong>שקיפות</strong> (גילוי נאות לבעלי המניות ולציבור); <strong>אחריותיות (Accountability)</strong> (הדירקטוריון וההנהלה אחראים לפעולותיהם בפני בעלי המניות); <strong>שוויון</strong> (התייחסות שווה לכל סוגי בעלי המניות); וקיומן של <strong>בקרות פנימיות אפקטיביות</strong> (ביקורת פנימית, ועדות ביקורת ותגמול). קיומם של דירקטורים בלתי תלויים, ועדות דירקטוריון יעילות (כמו ועדת ביקורת, ועדת תגמול, ועדת כספים/מימון), וקוד אתי ברור - כל אלו תורמים לממשל תאגידי חזק ולשיפור איכות קבלת ההחלטות.</p>
</div>

<style>
    :root {
        --boardroom-blue: #1a3a5f; /* Deep corporate blue */
        --boardroom-grey: #f4f7f6; /* Light, clean background */
        --boardroom-text: #333;
        --boardroom-accent: #e6b31e; /* Gold-like accent */
        --boardroom-hover: #0056b3;
        --boardroom-border: #ddd;
        --outcome-success: #28a745; /* Green */
        --outcome-warning: #ffc107; /* Yellow */
        --outcome-danger: #dc3545; /* Red */
        --outcome-info: #17a2b8; /* Teal */
        --transition-speed: 0.5s;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: var(--boardroom-grey);
        color: var(--boardroom-text);
    }

    h1 {
        color: var(--boardroom-blue);
        text-align: center;
        margin-bottom: 20px;
        font-size: 2.5em;
    }

    .intro-text {
        text-align: center;
        margin-bottom: 40px;
        font-size: 1.2em;
        color: #555;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    .simulator-container {
        border: 1px solid var(--boardroom-border);
        padding: 30px;
        margin-bottom: 30px;
        border-radius: 12px;
        background-color: #fff;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: all var(--transition-speed) ease-in-out;
    }

    .board-room-theme {
         /* Specific styles for the theme */
    }

    .section-title {
        color: var(--boardroom-blue);
        border-bottom: 2px solid var(--boardroom-accent);
        padding-bottom: 10px;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    .scenario-section p {
        margin-bottom: 15px;
    }

    .info-brief {
        background-color: #eef5ff; /* Light blue background */
        border-left: 4px solid var(--boardroom-blue);
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
    }

    .info-brief h3 {
        color: var(--boardroom-blue);
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.3em;
    }

    .info-brief ul {
        list-style: disc;
        margin: 0;
        padding-right: 20px;
    }

    .info-brief li {
        margin-bottom: 8px;
    }

    .decision-options {
        margin-top: 30px;
        text-align: center;
    }

    .decision-options button {
        background-color: var(--boardroom-blue);
        color: white;
        padding: 12px 25px;
        margin: 8px;
        border: none;
        border-radius: 30px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color var(--transition-speed) ease, transform 0.1s ease;
        min-width: 180px; /* Ensure consistent button width */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .decision-options button:hover {
        background-color: var(--boardroom-hover);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

     .decision-options button:active {
        transform: scale(0.98);
     }

    .decision-options button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        box-shadow: none;
    }


    .outcome-container {
        margin-top: 40px;
        padding: 25px;
        border: 2px dashed var(--boardroom-accent);
        border-radius: 8px;
        background-color: #fff; /* White background for outcome */
        opacity: 0; /* Start hidden */
        transform: translateY(20px); /* Start slightly below */
        transition: opacity var(--transition-speed) ease, transform var(--transition-speed) ease;
        display: none; /* Hidden by default */
    }

     .outcome-container.visible {
        display: block; /* Show when visible class is added */
        opacity: 1;
        transform: translateY(0);
     }


    #outcome-title {
        color: var(--boardroom-blue);
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.6em;
        text-align: center;
    }

    #outcome-details {
        font-style: italic;
        margin-bottom: 20px;
        color: #555;
    }

    .feedback-section {
        border-top: 1px solid var(--boardroom-border);
        padding-top: 20px;
    }

    .feedback-section h3 {
         color: var(--boardroom-blue);
         margin-top: 0;
         margin-bottom: 10px;
         font-size: 1.3em;
    }

    #outcome-feedback {
        font-weight: normal; /* Make feedback regular weight */
        color: var(--boardroom-text);
        line-height: 1.8; /* More readable line spacing */
    }

    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 30px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color var(--transition-speed) ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .toggle-button:hover {
        background-color: #5a6268;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

     .toggle-button:active {
        transform: scale(0.98);
     }


    .explanation-section {
        margin-top: 20px;
        padding: 30px;
        border: 1px solid var(--boardroom-border);
        border-radius: 12px;
        background-color: #fff; /* White background for explanation */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }

    .explanation-section h2 {
        color: var(--boardroom-blue);
        border-bottom: 2px solid var(--boardroom-accent);
        padding-bottom: 10px;
        margin-bottom: 20px;
         font-size: 1.8em;
    }

    .explanation-section h3 {
        color: var(--boardroom-accent);
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.4em;
    }

    .explanation-section p {
        margin-bottom: 15px;
        color: #555;
    }

     .restart-button {
        display: block;
        margin: 20px auto 0;
        padding: 10px 20px;
        background-color: var(--boardroom-accent);
        color: var(--boardroom-blue);
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
         font-weight: bold;
     }

     .restart-button:hover {
        background-color: #d4a81b;
     }

     .restart-button:active {
        transform: scale(0.98);
     }

     /* Basic responsiveness */
     @media (max-width: 768px) {
         .simulator-container, .explanation-section {
             padding: 20px;
         }
         .decision-options button {
             display: block;
             width: calc(100% - 16px); /* Adjust for margin */
             margin: 8px auto;
         }
         h1 {
             font-size: 2em;
         }
         .section-title {
             font-size: 1.5em;
         }
         .intro-text {
             font-size: 1em;
         }
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const scenarios = [
            {
                description: "אתה יושב סביב שולחן עץ מהגוני כבד בחדר הדירקטוריון של 'טקסטארט בע\"מ', חברת טכנולוגיה ותיקה ורווחית, אך כזו המחפשת נואשות מנועי צמיחה חדשים בשוק טכנולוגיה תחרותי וסטטי. על סדר היום: רכישת 'פינטק חדשנות', סטארטאפ מבטיח ופורץ דרך בתחום הפינטק הפיננסי המקוון. הסטארטאפ צומח במהירות אך עדיין שורף מזומנים ורחוק מרווחיות. השווי המבוקש על ידם גבוה משמעותית מהכנסותיהם הנוכחיות, ומחייב את 'טקסטארט' לגייס הון או לממן את העסקה מיתרות המזומנים הגדולות שלה - מהלך שיכול להשפיע מהותית על יציבותה הפיננסית בטווח הקצר.\n\n<div class=\"info-brief\"><h3>המידע שעל השולחן:</h3><ul><li>מצגת ראשונית מרשימה של מנכ\"ל 'פינטק חדשנות'.</li><li>דוחות כספיים חלקיים ובלתי מבוקרים של הסטארטאפ.</li><li>הערכת שווי פנימית ראשונית שביצע צוות פיתוח עסקי פנימי, הנאמדת בהערכת שווי נמוכה מהמבוקש על ידי הסטארטאפ.</li><li>מידע על מספר חברות טק אחרות המגלות עניין ברכישת 'פינטק חדשנות'.</li><li>לחץ הולך וגובר מבעלי מניות גדולים, המעוניינים ב\"עסקת כותרת\" שתקפיץ את מחיר המניה.</li></ul></div>\n\הזמן קצוב. יש להגיע להחלטה שתשרת את טובת החברה ובעלי מניותיה בטווח הארוך, תוך ניהול הסיכונים הקיימים. עיני ההנהלה ובעלי המניות נשואות אליך. מה תהיה עמדתך?",
                options: [
                    { text: "לאשר את הרכישה מיד", value: "approve" },
                    { text: "לדחות את הרכישה", value: "reject" },
                    { text: "להקים ועדה לבחינה מעמיקה יותר", value: "committee" },
                    { text: "לבקש הערכת שווי נוספת מצד שלישי והשלמת בדיקת נאותות", value: "valuation" }
                ],
                outcomes: {
                    approve: {
                        title: "תוצאה: אושרה הרכישה המיידית!",
                        details: "הרכישה הושלמה במהירות, מה שאפשר ל'טקסטארט' לנצח מתחרים פוטנציאליים ולהיכנס מיידית לשוק הפינטק. התגובה הראשונית בשוק הון חיובית, מחיר המניה עולה. עם זאת, התגלו קשיי אינטגרציה טכנולוגית ותרבותית בלתי צפויים עם 'פינטק חדשנות'. עלויות ההשקעה הדרושות כדי להביא את הסטארטאפ לרווחיות גבוהות מההערכה הראשונית, והצורך לגייס הון נוסף מדלל את בעלי המניות הקיימים. בנוסף, נפתחה חקירה רגולטורית בנוגע להיבטים מסוימים בעסקה שלא נבחנו לעומק.",
                        feedback: "<p><strong>ניתוח ההשלכות:</strong></p><ul><li><strong>חובת זהירות:</strong> החלטה מהירה ללא בדיקת נאותות מספקת והערכת שווי חיצונית עלולה להיחשב כהפרת חובת הזהירות. האם נאסף מספיק מידע רלוונטי ומבוסס?</li><li><strong>ניהול סיכונים:</strong> התעלמות מסיכונים בלתי ידועים ופוטנציאל לבעיות אינטגרציה ועליות מעבר לתקציב.</li><li><strong>ממשל תאגידי:</strong> החלטה תחת לחץ בעלי מניות מבלי להבטיח שהיא מבוססת על בחינה אובייקטיבית ומעמיקה עשויה להצביע על חולשה בממשל התאגידי. האם ניגודי עניינים או הטיות (כמו הטיית אישור או לחץ קבוצתי) השפיעו על התהליך?</li><li><strong>אסטרטגיה:</strong> כניסה מהירה לשוק חדש היא יתרון אסטרטגי, אך הביצוע וההשלכות הפיננסיות הפכו אותה למהלך בסיכון גבוה.</li></ul>"
                    },
                    reject: {
                        title: "תוצאה: ההצעה לרכישה נדחתה.",
                        details: "הדירקטוריון החליט שהסיכון הכספי והרגולטורי גבוה מדי ביחס למידע הקיים. חברת 'פינטק חדשנות' נרכשה בסופו של דבר על ידי חברת טק מתחרה, שהשיקה בהצלחה מוצר פינטק חדש שהפך ללהיט. 'טקסטארט' נמנעה אומנם מסיכון פיננסי מיידי ומבעיות אינטגרציה, אך נותרה בשוק הטכנולוגיה המסורתי והמאתגר, ואיבדה הזדמנות אסטרטגית משמעותית להיכנס לשוק הפינטק הצומח. מניית 'טקסטארט' רשמה ירידה קלה לאחר פרסום ידיעת הרכישה של המתחרה.",
                        feedback: "<p><strong>ניתוח ההשלכות:</strong></p><ul><li><strong>חובת זהירות:</strong> החלטה להימנע מסיכון על בסיס מידע חלקי עשויה להיתפס כזהירה בנסיבות מסוימות, אך האם נשקלו מספיק חלופות או דרכים לטפל בחוסר המידע (למשל, דחייה עם דרישה למידע נוסף)?</li><li><strong>ניהול סיכונים:</strong> ההחלטה מפחיתה סיכונים פיננסיים ותפעוליים מיידיים הקשורים לרכישה, אך מגדילה את הסיכון האסטרטגי ארוך הטווח של פיגור אחר המתחרים בשוק חדש.</li><li><strong>הטיות קוגניטיביות:</strong> האם ההחלטה הושפעה מהטיית ההימנעות מהפסד – פחד מסיכון שהאפיל על בחינה אובייקטיבית של פוטנציאל הצמיחה?</li><li><strong>אסטרטגיה:</strong> דחיית ההצעה שומרת על יציבות פיננסית קיימת, אך פוגעת באפשרות להשיג צמיחה משמעותית ומהירה. האם נשקלו מספיק חלופות אסטרטגיות לכניסה לשוק הפינטק?</li></ul>"
                    },
                    committee: {
                        title: "תוצאה: הוקמה ועדה אד-הוק לבחינה מעמיקה.",
                        details: "הדירקטוריון החליט לדחות את ההחלטה הסופית בחודש, ולהקים ועדת בחינה מיוחדת המורכבת מדירקטורים בלתי תלויים ובעלי מומחיות פיננסית וטכנולוגית. הוועדה שכרה יועצים חיצוניים מובילים לביצוע בדיקת נאותות מקיפה (Due Diligence) של 'פינטק חדשנות' והזמינה הערכת שווי בלתי תלויה. תהליך הבחינה חשף מספר סיכונים משפטיים וטכנולוגיים שלא היו גלויים בתחילה, אך גם אישש את פוטנציאל הצמיחה האדיר. הוועדה הגישה המלצה מנומקת, מבוססת על מידע מלא ומבוקר יותר.",
                        feedback: "<p><strong>ניתוח ההשלכות:</strong></p><ul><li><strong>חובת זהירות:</strong> הקמת ועדה לבחינה מעמיקה והסתייעות במומחים חיצוניים עונה באופן מצוין על חובת הזהירות של הדירקטורים ומפחיתה את הסיכון הקשור למידע חלקי או מוטה.</li><li><strong>ממשל תאגידי:</strong> הקמת ועדה אד-הוק עם דירקטורים בלתי תלויים היא פרקטיקה מומלצת בממשל תאגידי לאישור עסקאות מהותיות. זה מאפשר בחינה אובייקטיבית יותר ופחות מושפעת מלחצים חיצוניים או פנימיים (דינמיקה קבוצתית).</li><li><strong>ניהול סיכונים:</strong> התהליך חשף סיכונים קיימים ואיפשר התמודדות מושכלת יותר איתם.</li><li><strong>זמן ותזמון:</strong> דחיית ההחלטה טמנה בחובה סיכון שהעסקה תתפספס, אך בנסיבות המקרה המידע שהתקבל שווה את הסיכון הזה.</li></ul>"
                    },
                    valuation: {
                        title: "תוצאה: נתבקשה הערכת שווי חיצונית והשלמת בדיקת נאותות.",
                        details: "הדירקטוריון לא קיבל החלטה מיידית אלא דרש מההנהלה להשלים בדיקת נאותות מקיפה (פיננסית, משפטית, טכנולוגית) ולהזמין בדחיפות הערכת שווי בלתי תלויה מחברה חיצונית מוכרת. דרישות אלו עכבו את התהליך במספר שבועות. הערכת השווי החיצונית איששה כי השווי המבוקש גבוה מהשווי ההוגן על פי מדדים מקובלים, אך גם הדגישה את פוטנציאל הצמיחה. בדיקת הנאותות חשפה מספר סוגיות תאימות (Compliance) שיש לטפל בהן, אך לא העלתה דגלים אדומים המצדיקים דחייה מוחלטת.",
                        feedback: "<p><strong>ניתוח ההשלכות:</strong></p><ul><li><strong>חובת זהירות:</strong> דרישה למידע מלא יותר, לבדיקת נאותות ולהערכת שווי חיצונית עונה על חובת הזהירות ומאפשרת קבלת החלטה מבוססת נתונים ואובייקטיבית יותר.</li><li><strong>ממשל תאגידי:</strong> הסתייעות במומחים חיצוניים היא עיקרון חשוב בממשל תאגידי לטיפול בנושאים מורכבים או בעלי פוטנציאל לניגוד עניינים (הערכת שווי פנימית לעומת חיצונית). זה מגביר שקיפות ואחריותיות.</li><li><strong>ניהול סיכונים:</strong> בדיקת הנאותות מזהה סיכונים פוטנציאליים (רגולטוריים, משפטיים, תפעוליים) ומאפשרת תכנון התמודדות עמם או תמחורם בעסקה.</li><li><strong>תזמון:</strong> העיכוב היה משמעותי אך הכרחי לקבלת החלטה מושכלת. במקרים מסוימים, עיכוב כזה עלול לגרום לפספוס ההזדמנות.</li></ul>"
                    }
                }
            }
            // Add more scenarios here if needed
        ];

        const scenarioDescriptionEl = document.getElementById('scenario-description');
        const decisionOptionsEl = document.getElementById('decision-options');
        const outcomeContainerEl = document.getElementById('outcome-container');
        const outcomeTitleEl = document.getElementById('outcome-title');
        const outcomeDetailsEl = document.getElementById('outcome-details');
        const outcomeFeedbackEl = document.getElementById('outcome-feedback');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationEl = document.getElementById('explanation');
        const restartButton = document.getElementById('restart-simulation');

        const currentScenario = scenarios[0]; // Load the first scenario

        function renderScenario() {
            scenarioDescriptionEl.innerHTML = currentScenario.description; // Use innerHTML to render HTML tags from description
            decisionOptionsEl.innerHTML = ''; // Clear existing buttons
            currentScenario.options.forEach(option => {
                const button = document.createElement('button');
                button.textContent = option.text;
                button.dataset.decision = option.value;
                decisionOptionsEl.appendChild(button);
            });

            outcomeContainerEl.classList.remove('visible'); // Hide outcome container
            outcomeContainerEl.style.display = 'none';
            restartButton.style.display = 'none';

            // Re-enable buttons if they were disabled
             Array.from(decisionOptionsEl.children).forEach(button => button.disabled = false);
        }

        function showOutcome(decision) {
            const outcome = currentScenario.outcomes[decision];

            if (outcome) {
                outcomeTitleEl.textContent = outcome.title;
                outcomeDetailsEl.textContent = outcome.details;
                outcomeFeedbackEl.innerHTML = outcome.feedback; // Use innerHTML for feedback HTML
                
                outcomeContainerEl.style.display = 'block'; // Make visible for transition
                 setTimeout(() => { // Delay to allow display: block to take effect before transition
                    outcomeContainerEl.classList.add('visible');
                }, 10); // Small delay

                restartButton.style.display = 'block'; // Show restart button

                // Disable buttons after decision
                Array.from(decisionOptionsEl.children).forEach(button => button.disabled = true);
            }
        }

        // Add event listeners to decision buttons
        decisionOptionsEl.addEventListener('click', (event) => {
            if (event.target.tagName === 'BUTTON' && !event.target.disabled) {
                const decision = event.target.dataset.decision;
                showOutcome(decision);
            }
        });

        // Add event listener for explanation toggle button
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationEl.style.display === 'none';
            explanationEl.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסבר מעמיק: הדירקטוריון בפעולה (הסתר)' : 'הסבר מעמיק: הדירקטוריון בפעולה (הצג)';
        });

        // Add event listener for restart button
        restartButton.addEventListener('click', renderScenario);


        // Initial render
        renderScenario();
    });
</script>