---
title: "להציל שפה: סימולטור קבלת החלטות בשימור לשוני"
english_slug: saving-a-language-linguistic-preservation-decision-simulator
category: "בלשנות"
tags: ["שפות בסכנה", "שימור שפות", "בלשנות שדה", "קבלת החלטות", "אנתרופולוגיה"]
---
# להציל שפה: מסע אל לב המאמץ לשימור

**כל שפה היא יקום שלם.** יקום המכיל בתוכו את ההיסטוריה, התרבות, התפיסות והידע הייחודי של קהילה אנושית. אבל עולמות לשוניים רבים הולכים ונעלמים. כשיותר ויותר דוברי שפה מסוימת עוזבים אותה, או כשהדור הצעיר מפסיק לרכוש אותה, היא נמצאת בסכנת הכחדה קריטית.

דמיינו את עצמכם בראש צוות הצלה מיוחד, היוצא למשימה קדחתנית לתיעוד ולשימור שפה עתיקה לפני שהיא שוקעת בתהום הנשייה. תצטרכו לקבל החלטות קשות, לאזן בין משאבים מוגבלים, זמן אוזל, הצורך בנתונים לשוניים והחשיבות העליונה של בניית אמון עם הקהילה. **האם תצליחו להציל את מה שאפשר?**

<div class="simulation-container">
    <div class="resources-panel">
        <h3>מאזן המשאבים</h3>
        <div class="resource-item">
            <label for="time-meter">זמן שנותר:</label>
            <progress id="time-meter" value="100" max="100"></progress>
            <span id="time-value" class="resource-value">100%</span>
             <span class="resource-change" id="time-change"></span>
        </div>
        <div class="resource-item">
            <label for="budget-meter">תקציב פרויקט:</label>
            <progress id="budget-meter" value="100" max="100"></progress>
            <span id="budget-value" class="resource-value">100%</span>
             <span class="resource-change" id="budget-change"></span>
        </div>
        <div class="resource-item">
            <label for="trust-meter">אמון קהילה:</label>
            <progress id="trust-meter" value="100" max="100"></progress>
            <span id="trust-value" class="resource-value">100%</span>
             <span class="resource-change" id="trust-change"></span>
        </div>
         <div class="data-collected">
            <h4>נתונים שתיעדתם:</h4>
            <p><i class="icon-book"></i> דקדוק: <span id="data-grammar">0</span></p>
            <p><i class="icon-font"></i> אוצר מילים: <span id="data-lexicon">0</span></p>
            <p><i class="icon-chat"></i> נרטיבים וסיפורים: <span id="data-narratives">0</span></p>
            <p><i class="icon-music"></i> ידע מסורתי/טקסי: <span id="data-traditionalKnowledge">0</span></p>
         </div>
    </div>

    <div class="simulation-area">
        <div id="dilemma-context" class="context-box"></div>
        <div id="options" class="options-panel"></div>
        <div id="summary-area" class="summary-area" style="display: none;"></div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap'); /* More modern Hebrew-friendly font */

    body {
         font-family: 'Heebo', sans-serif;
         line-height: 1.7;
         color: #333;
         background-color: #f0f2f5; /* Light background */
         padding: 20px;
    }

    h1, h3, h4 {
        color: #1a237e; /* Dark blue for headings */
        font-weight: 700;
    }

    .simulation-container {
        direction: rtl;
        text-align: right;
        max-width: 900px;
        margin: 30px auto;
        border: none; /* Remove border */
        padding: 30px;
        border-radius: 12px;
        background-color: #ffffff; /* White background */
        box-shadow: 0 8px 16px rgba(0,0,0,0.1); /* Softer shadow */
        display: flex;
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
    }

    .resources-panel {
        flex: 1;
        min-width: 220px; /* Wider min-width */
        padding: 20px;
        border: none; /* Remove border */
        border-radius: 10px;
        background-color: #e8eaf6; /* Light blueish background */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.08); /* Inner shadow */
        display: flex;
        flex-direction: column;
        gap: 15px; /* Space between resource items */
    }

    .resources-panel h3 {
        margin-top: 0;
        text-align: center;
        color: #1a237e;
        border-bottom: 2px solid #c5cae9; /* Blueish border */
        padding-bottom: 15px;
        margin-bottom: 20px;
        font-size: 1.3em;
    }

    .resource-item {
        margin-bottom: 5px; /* Less space here, more from gap */
        display: flex;
        align-items: center;
        position: relative; /* For positioning resource changes */
    }

    .resource-item label {
        flex-grow: 1; /* Take available space */
        margin-bottom: 0; /* Remove margin-bottom */
        font-weight: bold;
        color: #3f51b5; /* Blue */
        font-size: 0.95em;
    }

     .resource-item progress {
        width: 120px; /* Fixed width for progress bar */
        height: 18px;
        vertical-align: middle;
        margin-left: 10px;
        border-radius: 5px;
        overflow: hidden; /* Ensure accent-color works visually */
        -webkit-appearance: none;
        appearance: none;
    }

    .resource-item progress::-webkit-progress-bar {
        background-color: #e0e0e0;
        border-radius: 5px;
    }

    .resource-item progress::-webkit-progress-value {
         transition: width 0.5s ease-in-out, background-color 0.3s ease; /* Animate width and color */
    }

     .resource-item progress::-moz-progress-bar {
         transition: width 0.5s ease-in-out, background-color 0.3s ease; /* Animate width and color */
    }


    .resource-value {
        display: inline-block;
        width: 50px; /* Fixed width for value */
        text-align: left; /* Align left for RTL */
        font-size: 0.9em;
        color: #1a237e; /* Dark blue value */
        vertical-align: middle;
        font-weight: bold;
         transition: color 0.3s ease; /* Animate value color */
    }

     .resource-change {
        position: absolute;
        left: 0; /* Position near the value */
        top: 50%;
        transform: translateY(-50%);
        font-size: 0.8em;
        font-weight: bold;
        opacity: 0;
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
        pointer-events: none; /* Don't interfere with clicks */
     }

    .resource-change.show {
        opacity: 1;
        transform: translateY(-100%); /* Float up */
    }

     .resource-change.positive { color: #4CAF50; } /* Green */
     .resource-change.negative { color: #f44336; } /* Red */


    .data-collected {
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px dashed #c5cae9; /* Dotted separator */
    }

    .data-collected h4 {
        text-align: center;
        color: #3f51b5;
        margin-bottom: 10px;
        font-size: 1.1em;
    }

    .data-collected p {
        margin-bottom: 8px;
        color: #555;
        font-size: 0.9em;
        display: flex;
        align-items: center;
    }

    .data-collected p i {
        margin-left: 8px; /* Space for icon */
        color: #7986cb; /* Lighter blue icon */
    }

    .data-collected p span {
        font-weight: bold;
        color: #1a237e; /* Dark blue value */
    }

     /* Basic icons - using characters as a fallback */
     .icon-book::before { content: '📖'; margin-left: 5px; }
     .icon-font::before { content: '🅰️'; margin-left: 5px; }
     .icon-chat::before { content: '🗣️'; margin-left: 5px; }
     .icon-music::before { content: '🎶'; margin-left: 5px; }


    .simulation-area {
        flex: 2;
        min-width: 350px; /* Wider min-width */
        display: flex;
        flex-direction: column;
        gap: 20px; /* Space between context and options */
    }

    .context-box {
        background-color: #e3f2fd; /* Light blue */
        border: 1px solid #bbdefb; /* Lighter blue border */
        padding: 20px;
        margin-bottom: 0; /* Removed margin, using gap */
        border-radius: 8px;
        line-height: 1.7;
        color: #1a237e; /* Dark blue text */
        box-shadow: inset 0 1px 4px rgba(0,0,0,0.06);
        animation: fadeIn 0.8s ease-out; /* Fade in animation */
    }

    .context-box h3 {
        margin-top: 0;
        color: #1a237e;
        margin-bottom: 10px;
        font-size: 1.2em;
    }

    .options-panel {
        display: flex;
        flex-direction: column;
        gap: 10px; /* Space between buttons */
    }

    .options-panel button {
        display: block;
        width: 100%;
        padding: 15px 20px; /* More padding */
        margin-bottom: 0; /* Removed margin, using gap */
        border: none;
        border-radius: 8px; /* Rounded corners */
        background-color: #5c6bc0; /* Medium blue */
        color: white;
        font-size: 1.05em;
        cursor: pointer;
        text-align: right;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Button shadow */
    }

    .options-panel button:hover:not(:disabled) {
        background-color: #3949ab; /* Darker blue on hover */
         box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        transform: translateY(-2px); /* Lift button slightly */
    }

     .options-panel button:active:not(:disabled) {
        background-color: #283593; /* Even darker on click */
        transform: translateY(0); /* Press button down */
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }

     .options-panel button:disabled {
        background-color: #bdbdbd; /* Gray for disabled */
        cursor: not-allowed;
        box-shadow: none;
        transform: none;
        opacity: 0.7;
    }

    .summary-area {
        background-color: #e8f5e9; /* Light green */
        border: 1px solid #c8e6c9; /* Lighter green border */
        padding: 25px;
        border-radius: 10px;
        color: #2e7d32; /* Dark green text */
        text-align: center;
        animation: fadeIn 0.8s ease-out; /* Fade in */
    }

    .summary-area h3 {
        margin-top: 0;
        color: #1b5e20; /* Darker green heading */
        margin-bottom: 15px;
        font-size: 1.4em;
    }

    .summary-area h4 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: #388e3c; /* Medium green heading */
        font-size: 1.1em;
        border-bottom: 1px solid #a5d6a7;
        padding-bottom: 5px;
        display: inline-block; /* Shrink border to content */
    }

    .summary-area p {
        margin-bottom: 8px;
        color: #424242; /* Dark gray for general text */
        font-size: 0.95em;
    }

     .summary-area p strong {
         color: #1b5e20; /* Bold parts darker */
     }

     /* Specific summary result styling */
     .summary-area .result-poor { color: #d32f2f; font-weight: bold; } /* Red for poor */
     .summary-area .result-fair { color: #fbc02d; font-weight: bold; } /* Orange for fair */
     .summary-area .result-good { color: #388e3c; font-weight: bold; } /* Green for good */
     .summary-area .result-excellent { color: #1b5e20; font-weight: bold; } /* Dark green for excellent */


    .explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* More padding */
        background-color: #00796b; /* Teal */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .explanation-button:hover {
        background-color: #004d40; /* Darker teal */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
     .explanation-button:active {
         background-color: #00332e;
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }


    .explanation-content {
        display: none;
        margin-top: 25px;
        padding: 25px;
        border: none; /* Remove border */
        border-radius: 10px;
        background-color: #e1f5fe; /* Very light blue */
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        line-height: 1.8;
        animation: fadeIn 0.8s ease-out; /* Fade in */
    }

    .explanation-content h2 {
        border-bottom: 2px solid #0288d1; /* Blue border */
        padding-bottom: 12px;
        margin-top: 0;
        color: #01579b; /* Darker blue */
        font-size: 1.5em;
    }

    .explanation-content h3 {
        margin-top: 25px;
        margin-bottom: 10px;
        color: #0277bd; /* Medium blue */
        font-size: 1.2em;
    }

    .explanation-content p, .explanation-content ul {
         color: #424242; /* Dark gray */
    }

    .explanation-content ul {
        list-style: disc inside;
        padding-right: 20px;
    }

    .explanation-content li {
        margin-bottom: 8px;
    }

     /* Keyframe animations */
     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }

      @keyframes slideUpFadeOut {
         0% { opacity: 1; transform: translateY(0); }
         100% { opacity: 0; transform: translateY(-20px); }
     }

</style>

<button class="explanation-button" onclick="toggleExplanation()">הצגת הסבר נוסף על שימור שפות</button>

<div id="explanation" class="explanation-content">
    <h2>הסבר נוסף: מאחורי הקלעים של שימור שפות</h2>
    <p>שימור שפות הוא מאמץ קריטי לא רק למען השפה עצמה, אלא למען עולמות שלמים של תרבות, ידע והיסטוריה שהיא מכילה.</p>

    <h3>מהי שפה בסכנת הכחדה ומדוע חשוב לשמר אותה?</h3>
    <p>שפה נחשבת בסכנת הכחדה כאשר הדור הצעיר מפסיק ללמוד אותה או להשתמש בה באופן פעיל. הסיבות לכך מגוונות: הגירה, לחץ חברתי-כלכלי לשימוש בשפה דומיננטית, מדיניות ממשלתית, או אובדן דוברי השפה בשל אסונות או גיל. חשיבות השימור נובעת מכך ששפות הן מאגר ידע ייחודי על העולם, על צמחים, חיות, היסטוריה מקומית, מיתולוגיה ועוד. כל שפה היא גם מבנה קוגניטיבי ייחודי ותפיסת עולם אחרת. אובדן שפה הוא אובדן בלתי הפיך של ידע וגיוון תרבותי ואנושי.</p>

    <h3>האתגרים הייחודיים של תיעוד שפות בסכנה</h3>
    <p>עבודה עם שפות בסכנה מציבה אתגרים רבים: **זמן** הוא משאב מוגבל, לרוב עקב גילם המתקדם של הדוברים האחרונים. **משאבים** (כספיים ואנושיים) כמעט תמיד אינם מספיקים למשימה העצומה של תיעוד מלא. **נגישות** פיזית ולוגיסטית לקהילות מרוחקות עלולה להיות קשה ויקרה. אתגרים **אתיים** כוללים רגישות תרבותית, שמירה על פרטיות הדוברים, והבטחת הסכמה מדעת ושיתוף פעולה אמיתי מהקהילה, כולל החזרת חומרים מתועדים לקהילה.</p>

    <h3>סוגי תיעוד לשוני</h3>
    <p>תיעוד שפה שואף לתפוס כמה שיותר היבטים שלה: **לקסיקון** (אוצר מילים) הוא הבסיס, לרוב בצורת מילון. **דקדוק** מתעד את מבנה השפה – פונולוגיה (צלילים), מורפולוגיה (מבנה מילים), ותחביר (מבנה משפטים). **נרטיבים** (סיפורים, שיחות) חיוניים להבנת השפה בהקשר טבעי ולקסיקתם עשירה. **ידע מסורתי**, **שירים**, **פולקלור** – אלו משמרים ידע תרבותי יקר ערך המבוטא בשפה.</p>

    <h3>שחקנים מרכזיים בתהליך</h3>
    <p>צוות התיעוד כולל בדרך כלל **בלשנים** המתמחים בלשנות שדה. **חברי הקהילה** הם הדוברים והידענים המרכזיים, ושותפותם חיונית. **מוסדות מחקר** (אוניברסיטאות) מספקים מסגרת אקדמית ותמיכה. **ארגונים** בינלאומיים ומקומיים עשויים לספק מימון ולסייע בלוגיסטיקה.</p>

    <h3>קבלת החלטות וסדרי עדיפויות בשימור לשוני</h3>
    <p>כיוון שמשאבים תמיד מוגבלים, יש צורך מתמיד לקבוע סדרי עדיפויות. האם להתמקד בתיעוד המבנה הלשוני (דקדוק/לקסיקון) או בתוכן התרבותי (סיפורים/ידע מסורתי)? האם לעבוד עם הדוברים המבוגרים ביותר ששפתם עשירה אך קשה יותר להבנה, או עם צעירים יותר שנגישים יותר אך שפתם אולי כבר מושפעת יותר משפות אחרות? כיצד מאזנים בין תיעוד לבין פעולות החייאה?</p>

    <h3>תפקיד הקהילה דוברת השפה בתהליך התיעוד וההחייאה</h3>
    <p>מעורבות הקהילה אינה רק הכרח אתי אלא קריטית להצלחת הפרויקט. הקהילה היא המקור לידע, והיא גם הבעלים האמיתיים של השפה. שיתוף חברי קהילה בתהליך התיעוד (כעוזרי מחקר, מתמללים) ובתהליך ההחייאה (יצירת חומרי לימוד, סדנאות) מבטיח את המשך השימוש בחומרים המתועדים ואת הסיכוי לשמר את השפה לאורך זמן, גם אם רק בצורה מתועדת.</p>

    <h3>השלכות של אי-תיעוד או תיעוד חלקי</h3>
    <p>אם שפה נכחדת ללא תיעוד מספק, אובד איתה עולם שלם של ידע, תרבות, והיסטוריה שאין לו תחליף. תיעוד חלקי משמעו שחלקים מהשפה או מהידע המקודד בה הולכים לאיבוד לנצח. זהו לא רק הפסד אקדמי, אלא אובדן למורשת האנושית כולה.</p>

    <h3>הצלחה בשימור לשוני: הגדרות ומדדים שונים</h3>
    <p>הצלחה אינה בהכרח 'החייאה מלאה' והחזרת השפה לשימוש יומיומי רחב (אף שזה היעד האידיאלי). הצלחה יכולה להימדד גם ביצירת ארכיון מקיף שמאפשר לחוקרים עתידיים ללמוד את השפה, או על ידי העלאת מודעות לחשיבות השפה בתוך הקהילה ומחוצה לה, או אפילו בהצלחת פרוייקטי תיעוד ספציפיים.</p>
</div>


<script>
    const resources = {
        time: 100,
        budget: 100,
        trust: 100,
        data: {
            grammar: 0,
            lexicon: 0,
            narratives: 0,
            traditionalKnowledge: 0
        }
    };

    const dilemmas = [
        {
            context: "אתם מגיעים לכפר נידח באזור מרוחק. הדוברים הפעילים היחידים של שפת 'ליסנה' הם קבוצה קטנה של זקנים מעל גיל 70. הם סקפטיים לגבי זרים, אך מוכנים לשקול לעזור. הזמן דוחק, ורכישת אמון הקהילה היא קריטית אך צורכת משאבים יקרים.",
            options: [
                {
                    text: "השקיעו זמן ותקציב משמעותיים בבניית אמון עם הקהילה ורק אחר כך התחילו בתיעוד לשוני רשמי.",
                    effects: { time: -15, budget: -5, trust: +25, data: {}}
                },
                {
                    text: "התחילו מיד בעבודה לשונית ממוקדת עם הדוברים הזמינים ביותר, התמקדו באיסוף אוצר מילים בסיסי. פעולה זו עלולה להיתפס כחוסר כבוד או סבלנות.",
                    effects: { time: -10, budget: -10, trust: -10, data: { lexicon: +15 }}
                },
                {
                    text: "נסו למצוא חברי קהילה צעירים יותר (אם קיימים) שאולי זוכרים קצת מהשפה. השקעה זו עשויה להשתלם בעתיד אך גוזלת זמן יקר כרגע.",
                    effects: { time: -15, budget: -10, trust: +5, data: {}} // Might find future speakers, but initial data collection is slow
                }
            ]
        },
         {
            context: "אמון הקהילה נמוך אך הצלחתם להתחיל לעבוד עם כמה דוברים מבוגרים. הדוברים הטובים ביותר פנויים רק בבקרים, מה שפוגע בלוח הזמנים של הצוות. בנוסף, הדוברים מבקשים תשלום הוגן עבור זמנם וידעם, דבר שלא היה מתוכנן במלואו בתקציב הראשוני. כיצד תנהלו את המצב?",
            options: [
                {
                    text: "שלמו לדוברים בנדיבות, גם אם זה חורג מהתקציב המתוכנן. עדיפות עליונה היא הנתונים הטובים ביותר והיחסים עם הקהילה.",
                    effects: { time: -5, budget: -20, trust: +15, data: {}}
                },
                {
                    text: "נסו לשכנע את הדוברים לעבוד גם בשעות אחר הצהריים, ולהציע להם תשלום סמלי יותר. ייתכן שתפגעו באמון או ביכולת להשיג את הדוברים הטובים ביותר.",
                    effects: { time: -10, budget: -5, trust: -10, data: {}} // Risk losing trust/data
                },
                 {
                    text: "התמקדו בתיעוד חומרים שאינם דורשים נוכחות ישירה תמיד, כמו ניתוח הקלטות קיימות או עבודה על תוכנה. פתרון זה פחות תלוי בלוח הזמנים של הדוברים אך עלול להאט את איסוף הנתונים החדשים.",
                    effects: { time: -5, budget: -5, trust: -5, data: { grammar: +10 }} // Less dependency on speakers, but slower data input
                }
            ]
        },
         {
            context: "גיליתם שדובר זקן במיוחד זוכר שירים טקסיים נדירים בשפה – אוצר תרבותי שאין לו תחליף. תיעודם ידרוש ציוד הקלטה איכותי יותר וזמן התמחות בהבנת הקשרים תרבותיים, מה שיגזול משאבים יקרים שהוקצו לתיעוד דקדוקי שיטתי.",
            options: [
                {
                    text: "הקצו את המשאבים הדרושים לתיעוד מעמיק של השירים הטקסיים הייחודיים, גם במחיר פגיעה בקצב תיעוד הדקדוק.",
                    effects: { time: -15, budget: -15, trust: +10, data: { traditionalKnowledge: +25 }}
                },
                {
                    text: "ותרו על התיעוד המעמיק של השירים והמשיכו להתמקד בתיעוד הדקדוק ואוצר המילים הבסיסי. זו החלטה פרגמטית אך עלולה להיות אובדן בלתי הפיך.",
                    effects: { time: -5, budget: -5, trust: -5, data: { grammar: +10, lexicon: +10 }}
                },
                 {
                    text: "נסו לגייס מימון נוסף במיוחד עבור פרויקט תיעוד השירים. זהו הימור שיכול להרוויח לכם משאבים ייעודיים, אך גם עלול לעלות לכם בזמן ובמאמץ ללא הצלחה.",
                    effects: { time: -10, budget: -5, trust: +5, data: {}} // Might gain resources, or lose time/trust
                }
            ]
        },
        {
            context: "אחד הדוברים המרכזיים והידענים חלה ואינו יכול לעבוד יותר ביעילות. הוא מציע שבן משפחה צעיר יותר, שזוכר מעט מהשפה (גרסה מודרנית יותר), יחליף אותו. הצעיר נלהב לעזור אך שפת הליסנה שבפיו שונה ומכילה השפעות רבות משפת הרוב האזורית. מה עדיף כעת?",
            options: [
                 {
                    text: "עבדו בעיקר עם הדובר החולה ככל הניתן, גם במחיר האטה משמעותית בקצב איסוף הנתונים. האיכות עדיפה על הכמות.",
                    effects: { time: -20, budget: -5, trust: +10, data: { grammar: +5, lexicon: +5 }} // Slower data collection from best source
                },
                {
                    text: "עבדו עם בן המשפחה הצעיר. אמנם הנתונים יהיו 'פחות טהורים' מבחינה היסטורית, אבל תהליך התיעוד יהיה מהיר ונגיש יותר.",
                    effects: { time: -10, budget: -5, trust: +5, data: { grammar: +15, lexicon: +15, narratives: +10 }} // Faster data, but potentially less authentic
                },
                 {
                    text: "השקיעו זמן בהכשרת בן המשפחה הצעיר על מנת שיוכל לעבוד טוב יותר עם הדובר המבוגר החולה, בתקווה שישמר את איכות הנתונים ויאפשר המשך עבודה בעתיד.",
                    effects: { time: -25, budget: -10, trust: +15, data: {}} // High investment, potential long-term gain but immediate cost
                }
            ]
        },
         {
            context: "הזמן אוזל במהירות והתקציב בשפל. עד כה אספתם בעיקר אוצר מילים ודוגמאות משפטים בסיסיות. חברי הקהילה מבקשים שתשקיעו את הזמן והמשאבים המעטים שנותרו בפיתוח חומרי לימוד בסיסיים עבור הילדים, על מנת להחיות את השפה, במקום להמשיך בתיעוד דקדוקי מורכב.",
            options: [
                {
                    text: "התעלמו מהבקשה המיידית והתמקדו בתיעוד עד הרגע האחרון, במיוחד על מבנים דקדוקיים מורכבים שעוד לא תועדו. זה עלול לפגוע באמון הקהילה אך ימקסם את התיעוד האקדמי.",
                    effects: { time: -20, budget: -10, trust: -20, data: { grammar: +25 }} // Prioritize documentation over revitalization request
                },
                {
                    text: "הקצו את הזמן והמשאבים שנותרו ליצירת חומרי לימוד בסיסיים בשיתוף הקהילה. פעולה זו תחזק את אמון הקהילה ותיתן תקווה להחייאה, גם אם התיעוד הלשוני לא יהיה מושלם.",
                    effects: { time: -15, budget: -15, trust: +25, data: {}} // Prioritize community request and revitalization effort
                },
                 {
                    text: "נסו לשלב: עבדו במהירות על תיעוד הדקדוק הבסיסי ביותר, ובמקביל עזרו לקהילה להתחיל לפתח חומרי לימוד. נסו להשיג את כל העולמות, אך עלולים להתקשות להצליח במלואם באף אחד מהם.",
                    effects: { time: -20, budget: -10, trust: +10, data: { grammar: +10 }} // Attempt to balance, may not fully succeed at either
                }
            ]
        },
        // Add more dilemmas for a richer simulation
    ];

    let currentDilemmaIndex = 0;

    const resourceMeters = {
        time: document.getElementById('time-meter'),
        budget: document.getElementById('budget-meter'),
        trust: document.getElementById('trust-meter')
    };

    const resourceValues = {
        time: document.getElementById('time-value'),
        budget: document.getElementById('budget-value'),
        trust: document.getElementById('trust-value')
    };

     const resourceChanges = {
        time: document.getElementById('time-change'),
        budget: document.getElementById('budget-change'),
        trust: document.getElementById('trust-change')
    };


    const dataDisplays = {
        grammar: document.getElementById('data-grammar'),
        lexicon: document.getElementById('data-lexicon'),
        narratives: document.getElementById('data-narratives'),
        traditionalKnowledge: document.getElementById('data-traditionalKnowledge')
    };

    const dilemmaContextDiv = document.getElementById('dilemma-context');
    const optionsDiv = document.getElementById('options');
    const summaryAreaDiv = document.getElementById('summary-area');
    const simulationAreaDiv = document.getElementById('simulation-area');
    const simulationContainer = document.querySelector('.simulation-container');


    function updateResourcesUI(animate = false, effects = {}) {
         const resourcesKeys = ['time', 'budget', 'trust'];
         resourcesKeys.forEach(key => {
             const meter = resourceMeters[key];
             const valueSpan = resourceValues[key];
             const changeSpan = resourceChanges[key];
             const effect = effects[key] || 0;

             if (animate) {
                 // Show change value animation
                 if (effect !== 0) {
                     changeSpan.textContent = (effect > 0 ? '+' : '') + effect;
                     changeSpan.className = 'resource-change show ' + (effect > 0 ? 'positive' : 'negative');
                     // Reset animation
                     void changeSpan.offsetWidth;
                     changeSpan.className = 'resource-change ' + (effect > 0 ? 'positive' : 'negative');
                     setTimeout(() => { changeSpan.classList.add('show'); }, 10); // Trigger animation
                 }

                 // Animate value text change (optional, can be done with CSS transition on span color)
                 // For a counting animation, would need more complex JS
                 valueSpan.style.transition = 'color 0.5s ease';
                 valueSpan.style.color = effect > 0 ? '#4CAF50' : (effect < 0 ? '#f44336' : '#1a237e'); // Flash color
             }

             // Update value and meter
             meter.value = resources[key];
             valueSpan.textContent = `${resources[key]}%`;

             // Update meter color based on level immediately or after animation
             meter.style.accentColor = resources[key] > 60 ? '#4CAF50' : (resources[key] > 30 ? '#ff9800' : '#f44336');

              if (animate) {
                 setTimeout(() => {
                     valueSpan.style.transition = ''; // Remove transition
                      valueSpan.style.color = '#1a237e'; // Reset color
                 }, 800); // Match animation duration
             }
         });


         // Update data display
         for (const dataType in resources.data) {
             if (dataDisplays[dataType]) {
                 dataDisplays[dataType].textContent = resources.data[dataType];
             }
         }
    }

    function displayDilemma(index) {
        if (index >= dilemmas.length || resources.time <= 0 || resources.budget <= 0 || resources.trust <= 0) {
            endSimulation();
            return;
        }

        const dilemma = dilemmas[index];
        dilemmaContextDiv.innerHTML = `<h3>דילמה ${index + 1}:</h3><p>${dilemma.context}</p>`;
        optionsDiv.innerHTML = '';
        dilemmaContextDiv.style.animation = 'none'; // Reset animation
        void dilemmaContextDiv.offsetWidth; // Trigger reflow
        dilemmaContextDiv.style.animation = 'fadeIn 0.8s ease-out'; // Apply animation

        dilemma.options.forEach((option, optionIndex) => {
            const button = document.createElement('button');
            button.textContent = option.text;
            button.addEventListener('click', () => handleDecision(option));

            // Check if option is affordable BEFORE applying
            const canAfford = (resources.time + (option.effects.time || 0) >= 0) &&
                             (resources.budget + (option.effects.budget || 0) >= 0) &&
                             (resources.trust + (option.effects.trust || 0) >= 0);

            if (!canAfford) {
                button.disabled = true;
                //button.textContent += " (אין מספיק משאבים לבחירה זו)"; // Optional: Add text to disabled button
            }
            optionsDiv.appendChild(button);
        });

        // Initial UI update (no animation for first display or between dilemmas)
        updateResourcesUI(false);
    }

    function handleDecision(option) {
        // Disable all buttons while processing
         Array.from(optionsDiv.children).forEach(button => button.disabled = true);

        // Apply effects for animation feedback BEFORE updating resources permanently
        const effects = option.effects; // Store effects
        updateResourcesUI(true, effects); // Animate based on potential effects

        // Apply effects to resources AFTER animation starts
        setTimeout(() => {
            resources.time = Math.max(0, resources.time + (effects.time || 0));
            resources.budget = Math.max(0, resources.budget + (effects.budget || 0));
            resources.trust = Math.max(0, resources.trust + (effects.trust || 0));

            for (const dataType in effects.data) {
                if (resources.data.hasOwnProperty(dataType)) {
                    resources.data[dataType] += (effects.data[dataType] || 0);
                }
            }

            // Update UI to final state after effects are applied
             updateResourcesUI(false); // Update final values

            // Move to next dilemma or end simulation
            currentDilemmaIndex++;
            setTimeout(() => { // Delay slightly to allow animation to show
                 displayDilemma(currentDilemmaIndex);
            }, 800); // Delay matches animation duration
        }, 500); // Small delay before applying effects and triggering next step
    }


    function endSimulation() {
        simulationAreaDiv.style.animation = 'fadeOut 0.8s ease-out forwards'; // Fade out simulation area (needs CSS fadeOut keyframe)

         // Define fadeOut keyframe if not already in CSS
        const styleSheet = document.styleSheets[0];
        const fadeOutKeyframes = `@keyframes fadeOut { from { opacity: 1; } to { opacity: 0; display: none; } }`;
        styleSheet.insertRule(fadeOutKeyframes, styleSheet.cssRules.length);


        setTimeout(() => {
             dilemmaContextDiv.style.display = 'none';
             optionsDiv.style.display = 'none';
             summaryAreaDiv.style.display = 'block';
             simulationAreaDiv.style.animation = ''; // Remove fadeOut animation
             simulationAreaDiv.style.opacity = 1; // Ensure it's visible for the summary
              summaryAreaDiv.style.animation = 'fadeIn 0.8s ease-out'; // Fade in summary
        }, 700); // Wait for fade out


        let summaryHTML = '<h3>סוף המסע: דו"ח סיכום המשימה</h3>';

        let gameEndedReason = '';
        if (resources.time <= 0) {
            gameEndedReason = "נגמר לכם הזמן! הקצב היה איטי מדי או שהשקעתם זמן רב מדי בפעולות מסוימות.";
        } else if (resources.budget <= 0) {
            gameEndedReason = "נגמר לכם התקציב! ההוצאות היו גבוהות מדי ולא הצלחתם לגייס משאבים נוספים.";
        } else if (resources.trust <= 0) {
            gameEndedReason = "איבדתם את אמון הקהילה! ללא שיתוף פעולה, התיעוד הפך לבלתי אפשרי.";
        } else if (currentDilemmaIndex >= dilemmas.length) {
             gameEndedReason = "הצלחתם לעבור את כל הדילמות במסע התיעוד!";
        }

        summaryHTML += `<p>${gameEndedReason}</p>`;


        summaryHTML += "<h4>מאזן סופי של משאבים:</h4>";
        summaryHTML += `<p>זמן: <strong class="${resources.time > 60 ? 'result-good' : (resources.time > 30 ? 'result-fair' : 'result-poor')}">${resources.time}%</strong></p>`;
        summaryHTML += `<p>תקציב: <strong class="${resources.budget > 60 ? 'result-good' : (resources.budget > 30 ? 'result-fair' : 'result-poor')}">${resources.budget}%</strong></p>`;
        summaryHTML += `<p>אמון קהילה: <strong class="${resources.trust > 60 ? 'result-good' : (resources.trust > 30 ? 'result-fair' : 'result-poor')}">${resources.trust}%</strong></p>`;

        summaryHTML += "<h4>היקף הנתונים שתיעדתם:</h4>";
        let totalData = 0;
        for(const type in resources.data) {
            totalData += resources.data[type];
        }

        summaryHTML += `<p>סה"כ נקודות תיעוד: <strong>${totalData}</strong></p>`;
        summaryHTML += `<p>דקדוק: ${resources.data.grammar} | אוצר מילים: ${resources.data.lexicon} | נרטיבים: ${resources.data.narratives} | ידע מסורתי: ${resources.data.traditionalKnowledge}</p>`;

        let dataAssessment = "";
         if (totalData < 50) {
             dataAssessment = `<span class="result-poor">התיעוד שביצעתם מצומצם מאוד.</span> חלקים רבים מהשפה והתרבות שלה אבדו ללא תיעוד.`;
         } else if (totalData < 150) {
             dataAssessment = `<span class="result-fair">אספתם כמות סבירה של נתונים.</span> יש עדיין פערים משמעותיים, אך הבסיס קיים.`;
         } else if (totalData < 250) {
             dataAssessment = `<span class="result-good">תיעדתם כמות נכבדת של נתונים.</span> יש לכם ארכיון טוב שיכול לשמש ללמידה ומחקר עתידיים.`;
         } else {
              dataAssessment = `<span class="result-excellent">הישג מרשים בתיעוד!</span> אספתם כמות עשירה ומגוונת של נתונים לשוניים ותרבותיים.`;
         }
        summaryHTML += `<p>${dataAssessment}</p>`;

        summaryHTML += "<h4>השפעת הבחירות שלכם על הסיכוי לשימור:</h4>";

        let impactAssessment = "";
        if (resources.trust > 70 && totalData > 100) {
            impactAssessment = `<span class="result-excellent">השקעתם בהצלחה גם בתיעוד וגם ביחסים עם הקהילה.</span> זהו הבסיס הטוב ביותר הן לתיעוד עשיר והן לשיתוף פעולה עתידי, אולי אפילו להחייאת השפה!`;
        } else if (resources.trust > 50 && totalData > 50) {
            impactAssessment = `<span class="result-good">שמרתם על איזון סביר.</span> יש לכם נתונים מתועדים ויחסים טובים יחסית עם הקהילה, מה שמשאיר דלת פתוחה לאפשרויות עתידיות.`;
        } else if (totalData > 150) {
             impactAssessment = `<span class="result-fair">התמקדתם בעיקר בתיעוד.</span> אספתם נתונים רבים, אך אמון הקהילה הנמוך עלול להקשות על השימוש בהם או על יוזמות החייאה עתידיות מצד הקהילה עצמה.`;
        } else if (resources.trust > 50) {
            impactAssessment = `<span class="result-fair">בניתם יחסים טובים עם הקהילה, אך התיעוד מועט.</span> הקהילה סומכת עליכם, אך ללא נתונים רבים, יהיה קשה מאוד לבצע תיעוד נוסף או להחיות את השפה בעתיד.`;
        }
        else {
            impactAssessment = `<span class="result-poor">גם התיעוד וגם אמון הקהילה נמוכים.</span> לצערי, סיכויי שימור השפה במצב זה נמוכים מאוד.`;
        }

        summaryHTML += `<p>${impactAssessment}</p>`;


        summaryAreaDiv.innerHTML = summaryHTML;
    }


    function toggleExplanation() {
        const explanationDiv = document.getElementById('explanation');
        const button = document.querySelector('.explanation-button');
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            button.textContent = 'הסתרת הסבר נוסף';
            explanationDiv.style.animation = 'fadeIn 0.8s ease-out';
        } else {
             explanationDiv.style.animation = 'fadeOut 0.8s ease-out forwards';
             setTimeout(() => {
                explanationDiv.style.display = 'none';
                button.textContent = 'הצגת הסבר נוסף על שימור שפות';
                 explanationDiv.style.animation = ''; // Reset animation
                 explanationDiv.style.opacity = 1; // Ensure it's ready for next fadeIn
             }, 700); // Match animation duration
        }
    }


    // Initial display
    displayDilemma(currentDilemmaIndex);
    updateResourcesUI(); // Initial UI state without animation

</script>
---