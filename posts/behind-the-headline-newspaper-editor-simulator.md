---
title: "עורך החדשות: סימולטור הדילמות מאחורי הכותרות"
english_slug: behind-the-headline-newspaper-editor-simulator
category: "מדעי החברה / כלכלה התנהגותית"
tags: [החלטות, עיתונות, פסיכולוגיה, הטיה קוגניטיבית, מדיה, קליקבייט, מיסגור]
---
# עורך החדשות: סימולטור הדילמות מאחורי הכותרות

עולם העיתונות הדיגיטלית הוא זירת קרב יומיומית על תשומת לב הקוראים. הכותרת היא הרושם הראשוני, השער לסיפור, ולעיתים קרובות - הדבר היחיד שהציבור הרחב ייחשף אליו. האם כותרת נאמנה לחלוטין לעובדות תנצח במאבק על הקליקים? או שמא כותרת סנסציונית או מוטה מעט תשיג את התנועה הנחוצה?

תכניסו את עצמכם לנעליים של עורך חדשות בכיר וקבלו החלטות קריטיות תחת לחץ. בכל סיבוב, תקבלו תקציר ידיעה חדשותית והנחיה עריכתית ספציפית. המשימה שלכם: לבחור את הכותרת שתואמת בצורה הטובה ביותר את המדיניות הנדרשת. כל החלטה תשפיע על גורל הסיפור, תפיסת הציבור - ואפילו על המוניטין שלכם.

<div id="app-container" class="simulator-app">
    <div id="scenario" class="card">
        <h3 class="scenario-title">תרחיש <span id="current-scenario-index">1</span> מתוך <span id="total-scenarios"></span></h3>
        <div class="scenario-details">
            <h4>📰 תקציר הידיעה:</h4>
            <div id="news-summary" class="summary"></div>
            <h4>🎯 המשימה שלך (מדיניות העריכה הנוכחית):</h4>
            <div id="editorial-policy" class="policy"></div>
        </div>
    </div>

    <div id="headline-options" class="options-list">
        <!-- Headline options will be loaded here -->
    </div>

    <div id="feedback" class="card feedback-box" style="display: none;"></div>

    <button id="next-round" class="button primary" style="display: none;">המשך לתרחיש הבא</button>
</div>

<button id="toggle-explanation" class="button secondary">הצג/הסתר הסבר תיאורטי</button>

<div id="explanation-content" class="card explanation-card" style="display: none;">
    <h2>הסבר תיאורטי: כוחן המניפולטיבי של כותרות ושיקולי עריכה</h2>
    <p>בחירת כותרת לכתבה היא תהליך מורכב הכולל שיקולים רבים, לעיתים סותרים. כותרת היא הרבה יותר מסתם סיכום של התוכן; היא השער לכתבה, הרושם הראשוני, ולעיתים קרובות - הדבר היחיד שהקורא יראה או יזכור. היא יכולה למסגר את הסיפור, לעורר רגש, ולנווט את האופן שבו המידע ייתפס.</p>

    <h3>כוחה של כותרת: רושם ראשוני, השפעה על הקריאה ועל הזיכרון</h3>
    <p>הכותרת היא הפנים של הכתבה הדיגיטלית. היא קובעת האם הקורא יבזבז את תשומת לבו עליה. כותרת חזקה ומעניינת תמשוך יותר עיניים, בעוד שכותרת חלשה עלולה להיבלע בפיד האינסופי. מעבר לכך, כותרות משפיעות עמוקות על האופן שבו אנו מפרשים את התוכן ואף על מה שאנו זוכרים ממנו. מחקרים מראים שאנשים נוטים יותר לזכור מידע שתואם את 'המסגור' הראשוני שסיפקה הכותרת, גם אם בהמשך הכתבה מופיע מידע מורכב יותר או סותר במקצת.</p>

    <h3>שיקולים שונים בבחירת כותרת: דיוק עובדתי מול עניין ציבורי, אתיקה מול רווח כלכלי</h3>
    <p>עורך עיתון דיגיטלי ניצב בפני דילמות יומיומיות במאבק על תשומת לב. מצד אחד, קיימת (או אמורה להתקיים) חובה עיתונאית לדווח במדויק ואובייקטיבי על המציאות. מצד שני, גוף חדשותי הוא לרוב גוף עסקי שצריך למשוך תנועת גולשים (קליקים, שיתופים, זמן שהייה) כדי לייצר הכנסות מפרסום. כותרת מדויקת לחלוטין עלולה להיות אנמית, וכותרת מעניינת במיוחד עלולה להיות מעט מטעה, מניפולטיבית או סנסציונית מדי. השיקולים הופכים למורכבים: רמת הדיוק מול פוטנציאל 'ויראליות', רמת סנסציוניות מול סיכון תדמיתי או משפטי, ורמת הטיה גלויה או סמויה.</p>

    <h3>הטיה קוגניטיבית והשפעתה על כותרות (הטיית אישור, היוריסטיקת הזמינות)</h3>
    <p>הטיות קוגניטיביות משפיעות לא רק על הקוראים אלא גם על מי שמייצר את התוכן. **הטיית אישור** (Confirmation Bias) גורמת לאנשים לנטות לחפש, לפרש ולזכור מידע שמאשר את אמונותיהם הקיימות. כותרות מתוחכמות יכולות "לשחק" על הטיה זו כדי למשוך קהל ספציפי שכבר נוטה להאמין לדברים מסוימים. **היוריסטיקת הזמינות** (Availability Heuristic) היא הנטייה להעריך את השכיחות או הסבירות של אירוע על סמך כמה קל לשלוף דוגמאות או מידע קשורים מהזיכרון. כותרת דרמטית על נושא מסוים (למשל, מקרה בודד של פשע או סכנה בריאותית נדירה) עלולה לגרום לקוראים להעריך יתר על המידה את הסיכון הכולל, פשוט כי הכותרת הפכה את הנושא ל"זמין" ומעורר בזיכרון הקולקטיבי.</p>

    <h3>אפקט המיסגור (Framing Effect): איך הצגה שונה של אותו מידע משנה את תפיסת הקהל</h3>
    <p>אפקט המיסגור מתייחס לאופן שבו הצגת מידע יכולה להשפיע באופן דרמטי על ההחלטות והשיפוטים שאנשים עושים, גם אם המידע הבסיסי זהה. אותה ידיעה חדשותית יכולה להיות 'ממוסגרת' (Framed) באופנים שונים לחלוטין באמצעות בחירת כותרת מסוימת. לדוגמה, דו"ח כלכלי מעורב יכול להיות מוצג תחת כותרת כמו "הכלכלה צומחת ב-X% - שיא חדש!" (מיסגור חיובי, מדגיש צמיחה) או "האינפלציה דוהרת - יוקר המחיה מרקיע שחקים!" (מיסגור שלילי, מדגיש עליית מחירים). המיסגור שבו בוחר העורך משפיע באופן ישיר על האופן שבו הקורא הממוצע יתפוס את האירוע, לעיתים ללא צורך לשנות ולו מילה אחת בתוך גוף הכתבה עצמה.</p>

    <h3>אבולוציה של כותרות: מעיתונות מודפסת לעידן ה'קליקבייט' הדיגיטלי</h3>
    <p>בעולם העיתונות המודפסת של פעם, כותרות נועדו בעיקר למשוך קוראים לרכוש את העיתון ולמצוא את הכתבה בתוכו. בעולם הדיגיטלי, המטרה המרכזית הפכה לרוב למשיכת 'קליקים' (Page Views) והשארת גולשים באתר כמה שיותר זמן. שינוי זה הוביל לפריחת תופעת ה"קליקבייט" (Clickbait) - כותרות פרובוקטיביות, מסתוריות, סנסציוניות או מטעות במקצת, שנועדו אך ורק לפתות את הגולש ללחוץ, לעיתים קרובות על חשבון דיוק או עומק עיתונאי. בעוד שקליקבייט עשוי להגביר תנועה לטווח קצר, הוא עלול לשחוק קשות את אמון הקוראים ולפגוע באמינות המותג החדשותי לטווח ארוך.</p>

    <h3>תפקידו של עורך החדשות: אומנות האיזון (הקשה) בין מטרות מתנגשות</h3>
    <p>עורך החדשות הדיגיטלי הוא 'שומר סף' (Gatekeeper) רב עוצמה בעולם המידע. הוא זה שמקבל את ההחלטות הקשות לגבי מה ידגש, כיצד יצבע, ובעיקר - איזו כותרת תלווה כל פיסת מידע שתגיע למיליוני קוראים. תפקידו דורש ללהטט באיזון עדין ומתמיד בין מחויבות עיתונאית (דיוק, אובייקטיביות, אתיקה, שירות לציבור) לבין שיקולים מסחריים-שיווקיים (משיכת קוראים, הכנסות מפרסום, תחרות אגרסיבית) ופסיכולוגיים (הבנת והשפעה על תפיסת הקהל הרחב). סימולטור זה מאפשר לכם לטעום מעט ממורכבות האתגר הזה.</p>
</div>

<style>
    /* General Styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6; /* Soft, light background */
        padding: 20px;
        margin: 0;
    }

    #app-container {
        max-width: 850px;
        margin: 20px auto;
        padding: 30px; /* Increased padding */
        background-color: #fff;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1); /* Softer, more prominent shadow */
    }

    /* Card Styling */
    .card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 25px; /* Increased padding */
        margin-bottom: 25px; /* Increased margin */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    /* Scenario Section */
    .scenario-title {
        color: #0056b3; /* Consistent blue accent */
        margin-top: 0;
        margin-bottom: 15px; /* Increased margin */
        padding-bottom: 10px;
        border-bottom: 2px solid #007bff; /* Stronger separator */
    }

    .scenario-details h4 {
        color: #555;
        margin-top: 20px; /* Space above h4 */
        margin-bottom: 8px; /* Space below h4 */
        font-size: 1.1em; /* Slightly larger */
    }

    .summary, .policy {
        background-color: #eef2f7; /* Lighter blue tint */
        padding: 15px; /* Increased padding */
        border-left: 4px solid #007bff; /* Accent border */
        border-radius: 4px; /* Slightly rounded corners */
        margin-bottom: 20px;
        font-style: italic;
        color: #444;
    }
    .policy {
        font-weight: bold;
        color: #0056b3; /* Policy stands out */
        border-left-color: #28a745; /* Green accent for policy/mission */
    }


    /* Headline Options */
    .options-list {
        margin-top: 25px;
    }

    .headline-option {
        background-color: #f9f9f9; /* Light grey for options */
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px; /* Increased padding */
        margin-bottom: 12px; /* Space between options */
        cursor: pointer;
        transition: all 0.3s ease-in-out; /* Smooth transitions */
        position: relative; /* Needed for absolute positioning of indicator */
        overflow: hidden; /* Hide overflow for indicators */
    }

    .headline-option:hover:not(.disabled) {
        background-color: #e9eef4; /* Lighter blue on hover */
        border-color: #007bff; /* Blue border on hover */
        box-shadow: 0 4px 12px rgba(0, 123, 255, 0.15); /* Subtle shadow */
        transform: translateY(-3px); /* Slight lift effect */
    }

    .headline-option h5 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #004085; /* Darker blue for headlines */
        font-size: 1.1em; /* Slightly larger headline text */
    }

    .headline-attributes {
        font-size: 0.85em; /* Slightly smaller attributes */
        color: #666; /* Grey for attributes */
        line-height: 1.5;
        padding-top: 10px; /* Space above attributes */
        border-top: 1px dashed #eee; /* Subtle separator */
        margin-top: 10px;
    }

    /* Selected/Disabled States */
    .headline-option.selected {
        border-color: #007bff;
        box-shadow: 0 0 15px rgba(0, 123, 255, 0.3); /* Stronger shadow when selected */
        background-color: #eef2f7; /* Highlight background */
    }

     .headline-option.disabled {
         opacity: 0.7; /* Slightly dimmed */
         cursor: not-allowed;
         transform: none; /* Remove lift effect */
         box-shadow: none;
     }

    .headline-option.disabled .headline-text,
    .headline-option.disabled .headline-attributes {
        color: #888; /* Dim text color */
    }

    /* Correct/Incorrect States after selection */
    .headline-option.selected.correct {
        border-color: #28a745; /* Green border */
        background-color: #d4edda; /* Light green background */
    }
    .headline-option.selected.incorrect {
        border-color: #dc3545; /* Red border */
        background-color: #f8d7da; /* Light red background */
    }

    /* Selection Indicator (Checkmark/Cross) */
    .selection-indicator {
        position: absolute;
        top: 10px;
        left: 10px; /* Position top-left */
        font-size: 1.8em; /* Larger icon */
        animation: pulse 1s infinite alternate; /* Subtle pulse animation */
        z-index: 1; /* Ensure it's above content */
    }

    .headline-option.selected.correct .selection-indicator {
        color: #155724; /* Dark green */
    }
    .headline-option.selected.incorrect .selection-indicator {
        color: #721c24; /* Dark red */
    }

    /* Animation for indicator */
    @keyframes pulse {
        from { transform: scale(1); }
        to { transform: scale(1.1); }
    }


    /* Feedback Section */
    .feedback-box {
        margin-top: 25px; /* Increased margin */
        padding: 20px;
        font-weight: bold;
        min-height: 3em; /* More reserved space */
        line-height: 1.6;
        /* Transition handled by JS class change */
    }

    .feedback-box.correct {
        background-color: #d4edda;
        color: #155724;
        border-color: #c3e6cb;
    }
    .feedback-box.incorrect {
        background-color: #f8d7da;
        color: #721c24;
        border-color: #f5c6cb;
    }

    /* Buttons */
    .button {
        display: block;
        margin: 25px auto 0; /* Increased margin */
        padding: 12px 25px; /* Increased padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
    }

    .button.primary {
        background-color: #007bff;
        color: white;
    }

    .button.primary:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }

    .button.secondary {
        background-color: #e9ecef;
        color: #495057;
        border: 1px solid #ced4da;
        margin-top: 15px; /* Space between buttons */
    }

    .button.secondary:hover {
        background-color: #d3d9df;
        transform: translateY(-1px);
    }

    /* Explanation Section */
    .explanation-card {
        margin-top: 25px;
        padding: 30px; /* Increased padding */
        background-color: #fefefe; /* Very light background */
    }

    .explanation-card h2 {
        color: #0056b3;
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
     .explanation-card h3 {
        color: #555;
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.2em;
     }
     .explanation-card p {
         margin-bottom: 15px;
         color: #444;
     }

    /* Optional: Fade in animation for feedback/explanation */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .feedback-box, .explanation-card {
         /* Apply animation when displayed by JS */
         /* This is a bit tricky to do purely in CSS on display change */
         /* Simpler to just let the JS display change handle it or add/remove a class */
    }


</style>

<script>
    const scenarios = [
        {
            summary: "חברת טק גדולה מפרסמת דוחות רווח רבעוניים שמראים גידול עצום ברווחים, אך גם ירידה קלה בהכנסות הכוללות עקב השקעות ארוכות טווח. מניית החברה מזנקת ב-5%.",
            policy: "'קליקבייט' שיהרוס את הרשת! עליך למקסם את מספר הקליקים והשיתופים ברשתות החברתיות, גם אם זה בא על חשבון דיוק מלא.",
            options: [
                {
                    headline: "ענקית הטק קורעת את השוק: רווחים מזנקים וזינוק במניה!",
                    attributes: { accuracy: "בינונית", clicks: "גבוה מאוד", sensationalism: "גבוה", risk: "נמוך", bias: "חיובי" },
                    feedback: "מצוין! כותרת סנסציונית ומעוררת הייפ שמנצלת את הפן החיובי ביותר בדוח (הרווחים והמניה), תוך התעלמות אלגנטית מהירידה בהכנסות. עמדת בהצלחה במשימה למקסם קליקים.",
                    consequence: "זרם אדיר של כניסות לאתר ורעש בלתי פוסק ברשתות החברתיות.",
                    isCorrect: true
                },
                {
                    headline: "דוחות טק: רווחים עולים, הכנסות יורדות קלות, המניה מזנקת ב-5%.",
                    attributes: { accuracy: "גבוהה מאוד", clicks: "בינוני", sensationalism: "נמוך", risk: "נמוך", bias: "ניטרלי" },
                    feedback: "אממ... כותרת מדויקת להפליא, מודה. אבל היא יבשה כמו פיתה ישנה ביום שישי בצהריים. אין בה מספיק פיתוי בשביל מדיניות 'מקסום קליקים'. פספסת את ההזדמנות לייצר באזז.",
                    consequence: "מעט מאוד קליקים, העיתון נבלע בין שאר החדשות הצעקניות. שמרת על אמינות, אבל זו לא הייתה המשימה.",
                    isCorrect: false
                },
                {
                    headline: "הצד האפל של ענקית הטק: הכנסות בירידה למרות רווחים מנופחים?",
                    attributes: { accuracy: "נמוכה", clicks: "גבוה", sensationalism: "בינוני", risk: "בינוני (תדמיתי)", bias: "שלילי" },
                    feedback: "זו כותרת שמייצרת סקרנות, אבל היא נוטה להיות שלילית מדי ומעט מטעה לגבי מהות הדוח הכולל (שכלל גם זינוק ברווחים ובמניה). היא גם עלולה לפגוע בתדמית האתר ולהיתפס כצהובה מדי. יש דרכים טובות יותר למקסם קליקים.",
                    consequence: "קליקים בינוניים-גבוהים, אבל עם סיכון תדמיתי ופגיעה אפשרית באמינות לטווח ארוך. לא הבחירה האופטימלית למשימה.",
                    isCorrect: false
                }
            ]
        },
        {
            summary: "מחקר חדש מתפרסם המצביע על קשר אפשרי (אך לא וודאי) בין צריכת מזון מסוים לעלייה קלה בסיכון למחלה נדירה בקרב קבוצה מסוימת באוכלוסייה.",
            policy: "שומר הסף האחראי. עליך לשמור על אובייקטיביות עיתונאית נוקבת, להימנע מסנסציות מיותרות ומכל דבר שעלול לגרום לפאניקה ציבורית.",
            options: [
                {
                    headline: "סכנה בצלחת? המחקר שמקשר מזון נפוץ למחלה נדירה.",
                    attributes: { accuracy: "בינונית", clicks: "גבוה", sensationalism: "גבוה", risk: "גבוה (פאניקה ציבורית)", bias: "שלילי" },
                    feedback: "כישלון במשימה! כותרת כזו היא מתכון בטוח לפאניקה ציבורית מיותרת על סמך קשר לא וודאי. היא סנסציונית ומטעה ומנוגדת לחלוטין למדיניות להימנע מפניקה ולשמור על אובייקטיביות.",
                    consequence: "גלי פאניקה ציבורית, ירידה חדה באמינות העיתון, ואפילו סיכון לתביעות משפטיות.",
                    isCorrect: false
                },
                {
                    headline: "מחקר חדש בודק קשר אפשרי בין תזונה לסיכון למחלה נדירה.",
                    attributes: { accuracy: "גבוהה מאוד", clicks: "נמוך", sensationalism: "נמוך", risk: "נמוך", bias: "ניטרלי" },
                    feedback: "מצוין! זו כותרת מדויקת, מאוזנת, שקולה ואחראית. היא משקפת נאמנה את מהות הממצאים מבלי לנפח אותם או לגרום לבהלה מיותרת. עמדת באופן מושלם במשימה להיות שומר הסף האחראי.",
                    consequence: "מעט קליקים (כצפוי מכותרת אובייקטיבית), אבל שמירה על אמינות עיתונאית מירבית ואי-גרימת פאניקה ציבורית.",
                    isCorrect: true
                },
                 {
                    headline: "חדשות טובות על המזון שאתם אוכלים: כמעט ואין קשר למחלה נדירה (מחקר).",
                    attributes: { accuracy: "נמוכה", clicks: "בינוני", sensationalism: "בינוני", risk: "נמוך", bias: "חיובי" },
                     feedback: "הכותרת הזו אולי נשמעת מרגיעה, אבל היא למעשה מעוותת את ממצאי המחקר (שמצא קשר אפשרי, גם אם לא וודאי). היא נוטה להרגיע יתר על המידה ואינה אובייקטיבית. לא עמדת במשימה לשמור על דיוק עובדתי.",
                     consequence: "קליקים בינוניים, פגיעה באמינות העיתון על ידי הצגה מוטעית של המחקר והטיה חיובית לא מבוססת.",
                     isCorrect: false
                 }
            ]
        }
        ,{
            summary: "ראש עירייה פעל לאשר בניית פרויקט נדל\"ן גדול באזור ירוק נדיר, למרות התנגדות ציבורית רחבה של תושבים וארגוני סביבה. ראש העיר טוען שהפרויקט חיוני לפיתוח הכלכלי של העיר.",
            policy: "קול הציבור והסביבה. עליך להבליט את ההתנגדות הציבורית לפרויקט ואת הפגיעה הצפויה בסביבה. זו הזווית שחשובה לנו.",
            options: [
                {
                    headline: "פיתוח כלכלי לעיר: ראש העיר מאשר פרויקט נדל\"ן ענק.",
                    attributes: { accuracy: "בינונית", clicks: "נמוך", sensationalism: "נמוך", risk: "נמוך", bias: "חיובי (לפרויקט)" },
                    feedback: "פספוס מוחלט של המטרה! הכותרת הזו מתעלמת לחלוטין מההיבטים הסביבתיים וההתנגדות הציבורית ומציגה רק את הצד של ראש העיר והפיתוח הכלכלי. היא מנוגדת לחלוטין למדיניות העריכה שקיבלת.",
                    consequence: "מעט קליקים (נושא יבש), הצגת תמונה חלקית ומעוותת של האירוע, אי-עמידה במשימה העריכתית.",
                    isCorrect: false
                },
                {
                    headline: "תושבים זועמים: ראש העיר מכריע נגד הציבור למען הנדל\"ן הירוק.",
                    attributes: { accuracy: "גבוהה", clicks: "גבוה", sensationalism: "גבוה", risk: "בינוני (האשמה אישית)", bias: "שלילי (לראש העיר)" },
                    feedback: "זו בדיוק הכותרת שהתבקשת לבחור! היא מדגישה בצורה ברורה וסנסציונית את ההתנגדות הציבורית ואת הזווית הסביבתית ("הנדל\"ן הירוק" בהקשר השלילי של פגיעה). עמדת במשימה העריכתית בהצלחה רבה.",
                    consequence: "גבוה בקליקים ושיתופים ברשתות. עלולה להיתפס כאגרסיבית מדי או מוטה אישית נגד ראש העיר על ידי חלק מהקוראים, אבל זו הייתה המשימה.",
                    isCorrect: true
                },
                {
                    headline: "דילמת ראש העיר: פיתוח כלכלי מול שימור טבע בפרויקט החדש.",
                    attributes: { accuracy: "גבוהה מאוד", clicks: "בינוני", sensationalism: "בינוני", risk: "נמוך", bias: "ניטרלי" },
                    feedback: "כותרת מדויקת ומאוזנת... אבל זו לא הייתה המשימה! התבקשת להבליט זווית ספציפית (התנגדות ציבורית וסביבה), ולא להציג את הדילמה בצורה ניטרלית. פספסת את ההזדמנות למסגר את הסיפור בהתאם למדיניות העריכה הנוכחית.",
                    consequence: "קליקים בינוניים. הצגה מאוזנת יותר, אך אי-עמידה במשימה העריכתית הספציפית.",
                    isCorrect: false
                }
            ]
        }
    ];

    let currentScenarioIndex = 0;
    const appContainer = document.getElementById('app-container');
    const newsSummaryDiv = document.getElementById('news-summary');
    const editorialPolicyDiv = document.getElementById('editorial-policy');
    const headlineOptionsDiv = document.getElementById('headline-options');
    const feedbackDiv = document.getElementById('feedback');
    const nextRoundButton = document.getElementById('next-round');
    const currentScenarioSpan = document.getElementById('current-scenario-index');
    const totalScenariosSpan = document.getElementById('total-scenarios');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationContentDiv = document.getElementById('explanation-content');

    totalScenariosSpan.textContent = scenarios.length;

    function renderScenario(index) {
        if (index >= scenarios.length) {
            appContainer.innerHTML = '<div class="card"><h2>✨ סיימת את הסימולטור! ✨</h2><p>עכשיו אתה מבין טוב יותר את המורכבות והדילמות העומדות בפני עורכי חדשות בעידן הדיגיטלי. כותרת היא כוח אדיר - השתמש בו באחריות (או בהתאם למדיניות הבוס!).</p></div>';
            // Hide the explanation button if simulator is finished
            toggleExplanationButton.style.display = 'none';
            return;
        }

        const scenario = scenarios[index];
        currentScenarioSpan.textContent = index + 1;
        newsSummaryDiv.textContent = scenario.summary;
        editorialPolicyDiv.textContent = scenario.policy;
        headlineOptionsDiv.innerHTML = ''; // Clear previous options
        feedbackDiv.style.display = 'none'; // Hide feedback
        feedbackDiv.className = 'card feedback-box'; // Reset feedback class
        nextRoundButton.style.display = 'none';

        scenario.options.forEach((option, i) => {
            const optionElement = document.createElement('div');
            optionElement.classList.add('headline-option');
            // Store index for easy access in event listener
            optionElement.dataset.index = i;

            // Create the content structure
             optionElement.innerHTML = `
                 <div class="headline-text">
                     <h5>${option.headline}</h5>
                 </div>
                 <div class="headline-attributes">
                     <strong>מאפיינים:</strong>
                     דיוק: ${option.attributes.accuracy},
                     קליקים פוטנציאליים: ${option.attributes.clicks},
                     סנסציוניות: ${option.attributes.sensationalism},
                     סיכון (תדמיתי/אחר): ${option.attributes.risk},
                     הטיה: ${option.attributes.bias}
                 </div>
                 <div class="selection-indicator" style="display: none;"></div>
             `;

            // Add click listener that checks if it's disabled
            optionElement.addEventListener('click', () => {
                if (!optionElement.classList.contains('disabled')) {
                    handleSelection(i);
                }
            });
            headlineOptionsDiv.appendChild(optionElement);
        });
    }

    function handleSelection(selectedIndex) {
        const scenario = scenarios[currentScenarioIndex];
        const selectedOption = scenario.options[selectedIndex];

        // Disable all options visually and remove interactivity
        document.querySelectorAll('.headline-option').forEach((option, i) => {
            option.classList.add('disabled');
             if (i === selectedIndex) {
                 option.classList.add('selected');
             }
             // Event listeners check for .disabled now, so no need to remove them explicitly
        });

        const isCorrect = selectedOption.isCorrect; // Use the data flag

        // Update feedback content and class
        feedbackDiv.innerHTML = `<p>${selectedOption.feedback}</p><p><strong>תוצאה:</strong> ${selectedOption.consequence}</p>`;
        feedbackDiv.classList.remove('correct', 'incorrect');
        feedbackDiv.classList.add(isCorrect ? 'correct' : 'incorrect');
        feedbackDiv.style.display = 'block'; // Show feedback

        // Add visual indicator to the selected option
        const selectedOptionElement = headlineOptionsDiv.querySelector(`.headline-option[data-index="${selectedIndex}"]`);
        const indicator = selectedOptionElement.querySelector('.selection-indicator');
        indicator.textContent = isCorrect ? '✅' : '❌';
        indicator.style.display = 'block'; // Show indicator

        // Show next round button
        nextRoundButton.style.display = 'block';

        // Scroll to feedback
        feedbackDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function nextRound() {
        currentScenarioIndex++;
        renderScenario(currentScenarioIndex);
         // Scroll to top of the simulator
        appContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Initial render
    renderScenario(currentScenarioIndex);

    // Event listeners for buttons
    nextRoundButton.addEventListener('click', nextRound);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationContentDiv.style.display === 'none';
        explanationContentDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר תיאורטי' : 'הצג/הסתר הסבר תיאורטי';
        if (isHidden) {
             explanationContentDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

</script>
---