---
title: "המלחמה הקרה: סוכן תחת אש"
english_slug: the-cold-war-your-secret-mission
category: "ארכאולוגיה"
tags:
  - מלחמה קרה
  - ריגול
  - סוכן חשאי
  - היסטוריה מודרנית
  - סימולציה
  - ברלין
---
<h1>המלחמה הקרה: סוכן תחת אש</h1>

<p>השעה מאוחרת, גשם דק מטפטף על כיכר קודרת בברלין המזרחית. האור היחיד מגיע מפנס רחוב רעוע ומאיר מעטפה מקומטת בידך. כל צל שנע, כל פנים חולפות, עלולים להיות מלכודת. כל החלטה היא שאלה של חיים או מוות מאחורי מסך הברזל. האם תצליח לנווט בעולם הצללים ולהשלים את משימתך, או שתתגלה וההיסטוריה תשכח את שמך? היכנס לנעלי סוכן חשאי ברגעים המתוחים ביותר של המלחמה הקרה.</p>

<div id="cold-war-mission-app">
    <div id="mission-scenario">
        <!-- Scenario description and options will be loaded here -->
    </div>
    <div id="mission-result" style="display: none;">
        <!-- Final result will be shown here -->
        <h2>סוף המשימה</h2>
        <p id="result-text"></p>
        <div id="result-details">
             <p id="result-explanation-short"></p>
             <p id="result-explanation-long"></p>
        </div>
        <button id="restart-mission">התחל משימה חדשה</button>
    </div>
</div>

<style>
    /* Global styles for the body - set a background, font, etc. */
    body {
        background-color: #f0f0f0; /* Light background */
        font-family: 'Arial', sans-serif; /* More modern font */
        line-height: 1.6;
        color: #333;
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #2c3e50; /* Dark blue/grey */
        text-align: center;
        margin-bottom: 20px;
    }

    /* App Container */
    #cold-war-mission-app {
        max-width: 760px; /* Slightly wider */
        margin: 30px auto; /* More space */
        padding: 30px; /* More padding */
        border: 1px solid #bdc3c7; /* Lighter border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ecf0f1; /* Very light grey background */
        box-shadow: 0 8px 16px rgba(0,0,0,0.2); /* Deeper shadow */
        direction: rtl;
        text-align: right;
        position: relative; /* For potential absolute positioning of elements */
        overflow: hidden; /* Hide overflow during transitions */
    }

    /* Scenario styling */
    #mission-scenario h3 {
        color: #34495e; /* Darker blue/grey */
        margin-bottom: 20px;
        font-size: 1.4em; /* Larger font */
        text-align: right; /* Align right for Hebrew */
        border-bottom: 2px solid #3498db; /* Underline effect */
        padding-bottom: 10px;
    }

    #mission-scenario p {
        margin-bottom: 25px; /* More space below text */
        line-height: 1.7; /* Improved line spacing */
        color: #555;
        font-size: 1.1em;
    }

    /* Options List */
    .options-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .options-list li {
        margin-bottom: 12px; /* More space between buttons */
        opacity: 0; /* Start hidden for fade-in */
        transform: translateY(10px); /* Start slightly below */
        animation: fadeInOption 0.5s ease forwards; /* Animation */
    }
     .options-list li:nth-child(1) { animation-delay: 0.1s; }
     .options-list li:nth-child(2) { animation-delay: 0.2s; }
     .options-list li:nth-child(3) { animation-delay: 0.3s; }
      /* Add more if needed */


    /* Option Buttons */
    .option-button {
        display: block;
        width: 100%;
        padding: 15px 20px; /* More padding */
        border: none; /* No default border */
        background-color: #3498db; /* Vibrant blue */
        color: white;
        text-align: right; /* Align text right for Hebrew */
        cursor: pointer;
        border-radius: 8px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease; /* Smooth transitions */
        font-size: 1.1em; /* Larger font */
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Subtle shadow */
    }

    .option-button:hover {
        background-color: #2980b9; /* Darker blue on hover */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15); /* Deeper shadow on hover */
    }

     .option-button:active {
         transform: scale(0.98); /* Slight press effect */
         box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Flatter shadow */
     }

     /* Result Styling */
    #mission-result {
        padding-top: 20px;
        border-top: 2px dashed #bdc3c7; /* Dashed border */
        margin-top: 25px;
        text-align: center; /* Center result text */
        opacity: 0; /* Start hidden for fade-in */
        transform: translateY(20px);
        animation: fadeInResult 0.6s ease forwards;
    }

    #mission-result h2 {
        color: #2c3e50;
        margin-bottom: 15px;
        font-size: 1.8em;
    }

    #result-text {
        font-weight: bold;
        font-size: 1.5em;
        margin-bottom: 10px;
        color: #e74c3c; /* Default color for failure (Red) */
        min-height: 1.5em; /* Reserve space to prevent layout shifts */
    }

     #result-text.success {
         color: #2ecc71; /* Green for success */
     }

    #result-details {
         margin-top: 20px;
         padding: 15px;
         background-color: #f4f6f7; /* Slightly different background */
         border-radius: 8px;
         border: 1px solid #dcdcdc;
         text-align: right;
    }

     #result-explanation-short {
         font-style: italic;
         color: #555;
         margin-bottom: 10px;
         font-size: 1.1em;
     }

    #result-explanation-long {
        color: #666;
        line-height: 1.6;
        font-size: 1em;
    }


    /* Restart Button */
    #restart-mission {
        display: block;
        margin: 30px auto 0; /* Center and add more space */
        padding: 12px 25px; /* More padding */
        background-color: #2ecc71; /* Green */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.2em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #restart-mission:hover {
        background-color: #27ae60; /* Darker green on hover */
         box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

     #restart-mission:active {
         transform: scale(0.98);
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }


    /* Explanation Toggle Button */
    #explanation-button {
        display: block;
        margin: 30px auto; /* Center and add space */
        padding: 12px 25px;
        background-color: #f39c12; /* Orange */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.2em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #explanation-button:hover {
        background-color: #e67e22; /* Darker orange on hover */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

     #explanation-button:active {
         transform: scale(0.98);
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }


    /* Explanation Section */
    #explanation-section {
        margin-top: 40px; /* More space */
        padding-top: 25px;
        border-top: 2px dashed #bdc3c7;
        display: none; /* Hidden by default */
        direction: rtl;
        text-align: right;
        background-color: #ecf0f1; /* Match app background */
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    #explanation-section h2 {
        color: #2c3e50;
        margin-bottom: 20px;
        font-size: 1.6em;
    }
    #explanation-section h3 {
        color: #34495e;
        margin-bottom: 15px;
        margin-top: 25px; /* More space above subtitles */
        font-size: 1.3em;
        border-bottom: 1px solid #3498db; /* Subtle underline */
        padding-bottom: 5px;
    }
    #explanation-section p, #explanation-section ul {
        color: #666;
        line-height: 1.7;
        margin-bottom: 18px; /* More space below paragraphs/lists */
        font-size: 1.05em;
    }
    #explanation-section ul {
        padding-right: 25px; /* Adjust padding for RTL */
        padding-left: 0;
        list-style: disc; /* Use discs for list items */
    }
    #explanation-section li {
        margin-bottom: 10px; /* More space between list items */
    }

     /* CSS Animations */
     @keyframes fadeInOption {
         to {
             opacity: 1;
             transform: translateY(0);
         }
     }

     @keyframes fadeInResult {
         to {
             opacity: 1;
             transform: translateY(0);
         }
     }

</style>

<button id="explanation-button">פענוח המשימה: רקע היסטורי</button>

<div id="explanation-section">
    <h2>פענוח המשימה: עולם הריגול במלחמה הקרה</h2>
    <p>המלחמה הקרה (סוף שנות ה-40 עד תחילת שנות ה-90) לא הייתה "קרה" כלל עבור מי שפעל בצללים. זה היה עימות עולמי בין אידיאולוגיות ואינטרסים – הקפיטליזם המערבי בהנהגת ארה"ב מול הקומוניזם הסובייטי בהנהגת ברית המועצות. בלב העימות עמדו שירותי הביון: ה-CIA האמריקאי, ה-KGB הסובייטי, והשטאזי המזרח גרמני (המכונה "מגן וחרב המפלגה"), ועוד רבים אחרים. תפקידם היה חיוני: לאסוף מידע על יכולות האויב, כוונותיו ומזימותיו, ולפעול באופן אקטיבי לערעורו או להשפעה עליו, ללא גרימת עימות גלובלי ישיר שעלול היה להוביל למלחמה גרעינית.</p>

    <h3>פרופיל סוכן: זהויות ופעולות</h3>
    <p>סוכנים היו אנשי צללים שהתמחו בהסוואה, הטעיה ותמרון. הם יכלו להיות דיפלומטים, אנשי עסקים, מדענים, עיתונאים, או אפילו אזרחים מן השורה שגויסו תחת לחץ או אידיאולוגיה. המשימות נעו מאיסוף מודיעין טכנולוגי או צבאי, דרך חבלה ולוחמה פסיכולוגית, ועד למבצעי הטעיה מורכבים שנועדו לבלבל את האויב.</p>
    <ul>
        <li><strong>איסוף:</strong> גניבת מסמכים, צילום אתרים אסורים, האזנה סמויה, הפעלת מקורות בתוך ממשל האויב.</li>
        <li><strong>חבלה/לוחמה פסיכולוגית:</strong> שיבוש תשתיות, הפצת תעמולה, זריעת אי-סדר פוליטי.</li>
        <li><strong>כניסה/יציאה:</strong> חציית גבולות בלתי חוקיים, שימוש במסלולי הברחה, הסתננות למדינות אויב ויציאה מהן תחת זהות בדויה.</li>
    </ul>

    <h3>ארגז הכלים של המרגל</h3>
    <p>הישרדות בעולם הריגול דרשה שליטה במגוון טכניקות סודיות:</p>
    <ul>
        <li><strong>מעקבים ומעקבי נגד:</strong> אמנות הזיהוי של מי שעוקב אחריך והיכולת להיעלם מעיניו בסמטאות צדדיות, ברכבת התחתית, או בשינוי קצב הליכה ומסלול בלתי צפוי.</li>
        <li><strong>נפילות מתות (Dead Drops):</strong> שיטה בטוחה יחסית להעברת חפצים (מסמכים, כסף, מיקרופילם) בנקודת מסירה מוסתרת מראש, ללא מפגש ישיר בין הסוכנים.</li>
        <li><strong>תקשורת חשאית:</strong> שימוש בכתבי סתר (צפנים), מכשירי רדיו קצר גל עם מסרים מוצפנים ששודרו במהירות שיא ("burst transmissions"), מיקרופילם שמוסתר בחפצים יומיומיים.</li>
        <li><strong>מסמכים מזויפים:</strong> תעודות זהות, דרכונים, אישורי מעבר - זיוף ברמה הגבוהה ביותר היה קריטי. שירותי המודיעין השקיעו רבות בזיהוי זיופים.</li>
    </ul>

    <h3>המחיר הנפשי: בדידות, פחד ודילמות</h3>
    <p>מעבר לאימונים הטכניים, סוכן חשאי נאלץ להתמודד עם לחצים פסיכולוגיים עצומים: חיים בהסוואה מתמדת, ניתוק מהעבר ומהקרובים, חשש תמידי מחשיפה, וקבלת החלטות הרות גורל בשברירי שניה תחת איום. סיפורם של סוכנים רבים הוא גם סיפור על בדידות אינסופית.</p>

    <h3>שיקוף הסימולציה: היסטוריה במשחק</h3>
    <p>המשימה הווירטואלית שחווית נועדה להמחיש את האתגרים היומיומיים שניצבו בפני סוכנים במלחמה הקרה. כל צומת החלטה (האם לגשת ישירות לקונטקט? איך להיפטר ממעקב? האם להשתמש במסמכים מזויפים במחסום?) מבוססת על דילמות אמיתיות מעולם הריגול. הבחירות שהובילו להצלחה או לכישלון בסימולציה שיקפו את הצורך הקריטי בזהירות, תחכום, יכולת אלתור, ולעיתים גם מזל פשוט, שהיו מרכיבים הכרחיים להישרדות במקצוע המסוכן ביותר בעולם.</p>
</div>

<script>
    // JavaScript logic for the app and explanation toggle
    document.addEventListener('DOMContentLoaded', () => {
        const scenarioDiv = document.getElementById('mission-scenario');
        const resultDiv = document.getElementById('mission-result');
        const resultText = document.getElementById('result-text');
        const resultShortExplanation = document.getElementById('result-explanation-short');
        const resultLongExplanation = document.getElementById('result-explanation-long');
        const restartButton = document.getElementById('restart-mission');
        const explanationButton = document.getElementById('explanation-button');
        const explanationSection = document.getElementById('explanation-section');

        // Define the simulation nodes
        const missionNodes = {
            start: {
                description: "אתה עומד בכיכר אלכסנדרפלאץ האפורה בברלין המזרחית. המטרה: להיפגש עם קונטקט שיעביר לך מעטפה עם מודיעין קריטי. השעה 14:00 בדיוק, ליד השעון העולמי. מבעד להמון החולף, אתה מזהה את סימן ההיכר המוסכם של הקונטקט.",
                options: [
                    { text: "גש אל הקונטקט ישירות. הזמן קצר.", next: 'meet_contact_direct' },
                    { text: "שלח סימן מוסכם מרחוק לפני שאתה מתקרב. ודא שהסביבה נקייה.", next: 'meet_contact_signal' },
                    { text: "עזוב את המקום מיד. אתה חש שמשהו לא כשורה או שהפגישה מסוכנת מדי כעת.", next: 'abort_mission' }
                ]
            },
            meet_contact_direct: {
                description: "אתה ניגש במהירות אל הקונטקט. הוא נראה מתוח מאוד. רגע לפני שהוא דוחף את המעטפה לידך, אתה מבחין בתנועה חשודה בקצה הכיכר. נראה שמבחינים בכם.",
                options: [
                    { text: "קח את המעטפה בפתאומיות והסתלק מיד.", next: 'take_envelope_direct' },
                    { text: "התעלם מהקונטקט לחלוטין והתרחק כאילו הוא זר גמור.", next: 'abandon_contact_direct' }
                ]
            },
             meet_contact_signal: {
                description: "שלחת את הסימן המוסכם. הקונטקט הגיב בסימן עדין משלו והתקרב אליך בצעדים מדודים. הוא מעביר לך את המעטפה בדיסקרטיות בתוך עיתון מקופל, מחליף איתך מילה מקודדת ונבלע שוב בקהל.",
                options: [
                    { text: "קח את העיתון והיטמע בקהל מבלי להיראות נחפז.", next: 'take_paper_blend' }
                ]
            },
             take_envelope_direct: {
                description: "קלטת את המעטפה בבהלה ויצאת מהכיכר. תחושת המעקב חזקה וברורה. אתה מרגיש שהעיניים נעוצות בך מאז הרגע המתוח בכיכר. עליך להגיע לדירת המסתור בצד השני של העיר בהקדם.",
                 options: [
                    { text: "נסה להיפטר מהמעקב באמצעות נתיבים מורכבים וטכניקות מעקבי נגד (סמטאות צדדיות, שינוי קצב הליכה, כניסה ויציאה מחנויות).", next: 'evade_tail' },
                    { text: "עבור בדרך הראשית והסואנת, בתקווה שהמעקבים לא יעזו לפעול שם בגלוי.", next: 'main_road' }
                ]
            },
            abandon_contact_direct: {
                 description: "החלטת שעדיף לא להיחשף ועזבת את הקונטקט. המשימה המרכזית נכשלה, והקונטקט כנראה בסכנה חמורה. עליך להגיע לנקודת חילוץ חלופית מחוץ לעיר.",
                 options: [
                    { text: "חזור לבסיס/נקודת חילוץ בנתיב הכי בטוח שאתה מכיר.", next: 'mission_failed_escaped' }
                 ]
            },
             take_paper_blend: {
                description: "השגת את המסמכים בצורה חלקה יחסית. כעת עליך להגיע לדירת מסתור בצד השני של העיר כדי להעביר את המידע. אתה חש תחושה קלה של מישהו שעוקב אחריך, אך היא אינה ודאית כמו קודם.",
                options: [
                    { text: "נסה להיפטר מהמעקב באמצעות נתיבים מורכבים וטכניקות מעקבי נגד (סמטאות צדדיות, שינוי קצב הליכה, כניסה ויציאה מחנויות).", next: 'evade_tail' },
                    { text: "עבור בדרך הראשית והסואנת, בתקווה שהמעקבים לא יעזו לפעול שם בגלוי.", next: 'main_road' }
                ]
            },
            main_road: {
                description: "בחרת בדרך הראשית. לפתע, בזמן שאתה חולף ליד בניין משרדים, שני גברים במעילים ארוכים חוסמים את דרכך ומבקשים לראות את מסמכיך. הנימוס הקריר שלהם והמבט בעיניהם לא משאירים ספק - הם מהשטאזי.",
                options: [
                     { text: "הצג מסמכים מזויפים ברמה גבוהה שהוכנו מראש לתרחיש כזה.", next: 'show_fake_papers' },
                     { text: "נסה לברוח בריצה מיידית, תוך ניצול ההמון.", next: 'attempt_escape' },
                     { text: "שחק אותה תייר מבולבל שאיבד את דרכו, ללא המסמכים הנכונים.", next: 'act_confused' }
                ]
            },
             evade_tail: {
                description: "צללת לתוך מבוך סמטאות אחוריות, חצית חצרות פנימיות, שינית כיוון מספר פעמים. נראה שהצלחת לשבור את המעקב. אתה מותש אך הקלה ממלאה אותך. כעת עליך להגיע למחסום יציאה מהעיר (או למחסום צבאי סמוך לגבול).",
                options: [
                    { text: "עבור את המחסום עם מסמכים מזויפים שהוכנו מראש.", next: 'border_fake_papers' },
                    { text: "נסה למצוא פרצה בגדר או נתיב הברחה לא חוקי לעבור בו.", next: 'border_illegal' }
                ]
            },
             attempt_escape: {
                description: "ניסית לברוח בריצה. הצלחת להשיג יתרון קל בהתחלה, אך הרחוב נחסם במהירות על ידי אנשי שטאזי נוספים שהמתינו בסמוך. המשימה נכשלה ואתה נלכדת.",
                options: [
                     { text: "סוף המשימה.", next: 'mission_failed_caught' }
                ]
            },
             act_confused: {
                 description: "שיחקת אותה תייר אובד עצות. אנשי השטאזי חושדים בך, אך לא מוצאים סיבה מוצקה לעצור אותך מיידית. הם מלווים אותך לתחנת משטרה מקומית לבדיקה 'שגרתית'. בזמן ההמתנה הארוכה, אתה מבחין בהזדמנות בריחה קצרה ולא צפויה.",
                 options: [
                     { text: "נסה לברוח מהתחנה, תוך ניצול ההזדמנות המיידית.", next: 'escape_station' },
                     { text: "הישאר בתחנה, היצמד לסיפור הכיסוי שלך, בתקווה שישחררו אותך לאחר בדיקה.", next: 'stay_detained' }
                 ]
            },
            show_fake_papers: {
                description: "הצגת את המסמכים המזויפים. הזיוף איכותי ביותר. איש השטאזי הראשון נראה כמעט משוכנע, אך השני מעיין במסמך ושואל שאלה מפתיעה על פרט אזוטרי ולא צפוי. אתה מזהה ניצוץ קטן אך מסוכן של חשד בעיניו.",
                options: [
                     { text: "ענה בביטחון מוחלט, כאילו השאלה טריוויאלית והפרט ידוע לך היטב.", next: 'fake_papers_confident' },
                     { text: "הראה סימן קל של היסוס או בלבול, כאילו הפרט פחות מוכר לך.", next: 'fake_papers_hesitant' }
                ]
            },
             fake_papers_confident: {
                 description: "שמרת על קור רוח וענית תשובה מיידית ונחרצת. אנשי השטאזי מחליפים מבטים, מתלבטים לרגע, ולבסוף מניחים לך ללכת עם אזהרה קרה. הצלחת לחמוק ברגע האחרון! כעת עליך להגיע למחסום יציאה מהעיר או לגבול במהירות.",
                 options: [
                    { text: "עבור את המחסום עם מסמכים מזויפים (אולי מסמכים אחרים, או שוב אלו ש'עבדו').", next: 'border_fake_papers_after_detection' },
                    { text: "נסה למצוא פרצה בגדר או נתיב הברחה לא חוקי לעבור בו. זה מסוכן אך אולי פחות צפוי.", next: 'border_illegal_after_detection' }
                 ]
             },
             fake_papers_hesitant: {
                 description: "היססת בתשובה. הניצוץ בעיני איש השטאזי הפך לודאות. הזיוף אומת או שהם הבינו שאתה לא מי שאתה טוען להיות. המשימה נכשלה ואתה נלכדת.",
                 options: [
                     { text: "סוף המשימה.", next: 'mission_failed_caught' }
                 ]
             },
             escape_station: {
                 description: "ניצלת את ההזדמנות וניסית לברוח מתחנת המשטרה. רצת החוצה אל הרחוב, אך צפירת אזעקה חדה נשמעה מאחוריך. אתה נרדף ברחובות העיר הלא מוכרים לך.",
                 options: [
                     { text: "הסתתר בסמטאות חשוכות ומורכבות, תוך שימוש בטכניקות מעקבי נגד שלמדת.", next: 'hide_alleys' },
                     { text: "רוץ במהירות לכיוון כיכר הומה אדם סמוכה, בתקווה להתערבב בקהל ולהיעלם.", next: 'run_crowd' }
                 ]
             },
             stay_detained: {
                 description: "בחרת להישאר בתחנה ולהיצמד לסיפור הכיסוי. החקירה מעמיקה, והם בודקים את מסמכיך וסיפורך לעומק. בסופו של דבר, שגיאה קטנה או חוסר עקביות נחשפים. השטאזי חושפים את זהותך האמיתית. המשימה נכשלה ואתה נלכדת.",
                 options: [
                     { text: "סוף המשימה.", next: 'mission_failed_caught' }
                 ]
             },
             border_fake_papers: {
                 description: "הצגת את המסמכים המזויפים במעבר הגבול. השומרים שם מאומנים היטב בזיהוי זיופים ומבצעים בדיקות קפדניות במיוחד. הם מבחינים בחוסר התאמה קלה שנגרמה כנראה מעצם הבהילות בפגישה. המשימה נכשלה ואתה נלכדת במעבר הגבול.",
                 options: [
                     { text: "סוף המשימה.", next: 'mission_failed_caught' }
                 ]
             },
            border_fake_papers_after_detection: {
                 description: "הגעת למעבר הגבול והצגת מסמכים מזויפים משופרים (או שאותם מסמכים עבדו בזכות קור הרוח שלך קודם). השומרים בודקים אותם ביסודיות אך לא מוצאים פגם משמעותי. לאחר רגעים מורטי עצבים, הם מתירים לך לעבור. הצלחת לחמוק!",
                 options: [
                     { text: "סוף המשימה.", next: 'mission_successful' }
                 ]
             },
             border_illegal: {
                 description: "ניסית למצוא דרך לעבור את הגבול באופן לא חוקי, בנתיב הברחה צפוי. השטח פתוח יותר ממה שציפית ויש סיורים תכופים של משמר הגבול. זיהו אותך על פי תנועות חשודות כשניסית לחצות את הגדר. המשימה נכשלה ואתה נלכדת.",
                 options: [
                     { text: "סוף המשימה.", next: 'mission_failed_caught' }
                 ]
             },
             border_illegal_after_detection: {
                  description: "ניסית למצוא דרך לעבור את הגבול באופן לא חוקי, תוך בחירה בנתיב לא שגרתי ומסוכן. הסתננת בשטח מיוער תחת כיסוי החשיכה, תוך שימוש בטכניקות הישרדות. לאחר שעות של הליכה מותחת, תוך הימנעות מסיורים, הצלחת לחצות את הקו הבלתי נראה לצד השני. הצלחת!",
                 options: [
                     { text: "סוף המשימה.", next: 'mission_successful' }
                 ]
             },
             hide_alleys: {
                 description: "צללת לתוך סבך סמטאות אחוריות. מרדף הרגלים נשמע בקרבת מקום אך לא גילה אותך בחושך. הצלחת להתחמק ולהשאיר את רודפיך מאחור. כעת עליך להגיע למחסום יציאה מהעיר או לגבול במהירות.",
                 options: [
                     { text: "עבור את המחסום עם מסמכים מזויפים שהוכנו מראש.", next: 'border_fake_papers_after_detection' },
                     { text: "נסה למצוא פרצה בגדר או נתיב הברחה לא חוקי לעבור בו.", next: 'border_illegal_after_detection' }
                 ]
             },
             run_crowd: {
                 description: "רצת לכיוון כיכר הומה אדם סמוכה. אמנם הצלחת להתערבב לזמן קצר, אך המשטרה המקומית, בהוראת השטאזי, חסמה במהירות את כל היציאות מהכיכר ופתחה בסריקה שיטתית. המשימה נכשלה ואתה נלכדת בתוך הקהל ההמום.",
                 options: [
                      { text: "סוף המשימה.", next: 'mission_failed_caught' }
                 ]
             },
            // Ending nodes
            mission_successful: {
                description: "המשימה הושלמה. המסמכים הגיעו ליעדם, והמודיעין הקריטי בתוכם ישפיע על מהלכים עתידיים. חזרת בשלום לצד השני של מסך הברזל, עוד צעד מותח נרשם ביומן הריגול הארוך.",
                resultShort: "מבצע נועז הסתיים בהצלחה!",
                options: [], // No options, it's an end state
                isEnd: true,
                isSuccess: true
            },
            mission_failed_caught: {
                description: "נלכדת על ידי שירותי המודיעין של האויב. גורלך כעת בידיהם, והמסמכים שאספת (או שלא הספקת לאסוף) אבודים. פרק זה בסיפור הריגול שלך הגיע לסופו הטראגי.",
                 resultShort: "המשימה נכשלה. נלכדת.",
                options: [], // No options, it's an end state
                isEnd: true,
                isSuccess: false
            },
             mission_failed_escaped: {
                description: "החלטת להקריב את המשימה כדי לשרוד. לא השגת את המסמכים, אך הצלחת להימלט ולהגיע לנקודת החילוץ. חייך ניצלו, אך ההזדמנות לאיסוף מודיעין קריטי אבדה. תיק הישרדותך ייסגר בבסיס.",
                 resultShort: "המשימה נכשלה, אך הצלחת להיחלץ.",
                options: [], // No options, it's an end state
                isEnd: true,
                isSuccess: false
            }
        };

        function renderNode(nodeId) {
            const node = missionNodes[nodeId];
            if (!node) {
                console.error("Node not found:", nodeId);
                return;
            }

            // Clear previous content and fade in new
            scenarioDiv.style.opacity = 0;
            scenarioDiv.style.transform = 'translateY(10px)';

            setTimeout(() => {
                 scenarioDiv.innerHTML = `
                    <h3>המשימה מתקדמת... ${nodeId !== 'start' ? `(נקודה: ${nodeId})` : ''}</h3> <!-- Optional: show node ID for debugging -->
                    <p>${node.description}</p>
                    ${node.options.length > 0 ? '<ul class="options-list"></ul>' : ''}
                `;

                const optionsList = scenarioDiv.querySelector('.options-list');
                if (optionsList) {
                    node.options.forEach(option => {
                        const li = document.createElement('li');
                        const button = document.createElement('button');
                        button.classList.add('option-button');
                        button.textContent = option.text;
                        button.addEventListener('click', () => handleChoice(option));
                        li.appendChild(button);
                        optionsList.appendChild(li);
                    });
                }

                 // Fade in the new content
                 scenarioDiv.style.opacity = 1;
                 scenarioDiv.style.transform = 'translateY(0)';

                if (node.isEnd) {
                    showResult(node);
                }
            }, 300); // Match CSS transition duration
        }

        function handleChoice(option) {
             // Disable buttons briefly to prevent double clicks or changing mind
             const buttons = scenarioDiv.querySelectorAll('.option-button');
             buttons.forEach(button => button.disabled = true);

             // Trigger the next node rendering
             renderNode(option.next);
        }

        function showResult(finalNode) {
             // Fade out scenario, fade in result
            scenarioDiv.style.opacity = 0;
            scenarioDiv.style.transform = 'translateY(-10px)';

            setTimeout(() => {
                scenarioDiv.style.display = 'none';
                resultDiv.style.display = 'block';

                if (finalNode.isSuccess) {
                    resultText.textContent = "המשימה הושלמה בהצלחה!";
                    resultText.className = 'success'; // Use class for styling
                    resultShortExplanation.textContent = finalNode.resultShort || "עבודתך הקשה והחלטותיך הנכונות אפשרו לך לנווט בבטחה בעולם הריגול המסוכן ולהשיג את יעדך.";
                    resultLongExplanation.textContent = "הבחירות שלך הובילו אותך בנתיב זהיר וחמקמק, שאיפשר לך להשיג את המידע הקריטי ולהיחלץ בשלום מבעד למסך הברזל. יכולת התמרון שלך תחת לחץ ויכולתך לקבל החלטות נכונות ברגעים קריטיים היו המפתח להצלחה במשימה חיונית זו.";
                } else {
                    resultText.textContent = "המשימה נכשלה.";
                    resultText.className = 'failure'; // Use class for styling (default)
                    resultShortExplanation.textContent = finalNode.resultShort || "הבחירות שלך הובילו למצב בלתי הפיך.";

                    let explanation = "המשימה נכשלה בגלל בחירות שהובילו למבוי סתום או חשיפה. ייתכן שלקחת סיכונים גדולים מדי, לא זיהית את הסימנים הנכונים, או שהמזל פשוט לא שיחק לצידך ברגע מכריע. למד מכישלון זה לקראת המשימה הבאה.";
                    if (finalNode.next === 'mission_failed_caught') {
                        explanation = "המשימה נכשלה. הבחירות שלך הובילו לחשיפתך וללכידתך על ידי שירותי המודיעין של האויב. ברגעים קריטיים, בין אם בפגישה, בהתחמקות ממעקב או בחציית גבול, עשית טעות שזוהתה על ידי האויב. זכור תמיד: זהירות ופרנויה מבוקרת הן כלים חיוניים בשטח.";
                    } else if (finalNode.next === 'mission_failed_escaped') {
                         explanation = "המשימה נכשלה (לא הושגו המסמכים). עמדת בפני מצב קריטי שבו סיכון המשימה עלה על סיכון הישרדותך. בחירתך להיחלץ הצילה את חייך, מה שחיוני לסוכן, אך לא איפשר את השלמת היעד המרכזי. יש משימות שפשוט לא ניתן להשלים בלי סיכון עצמי, ואז נדרשת הערכת מצב מיידית וקרה.";
                    }
                     resultLongExplanation.textContent = explanation;
                }

                 // Fade in result content
                 resultDiv.style.opacity = 1;
                 resultDiv.style.transform = 'translateY(0)';

            }, 300);
        }

        function restartMission() {
            // Fade out result before restart
            resultDiv.style.opacity = 0;
            resultDiv.style.transform = 'translateY(-10px)';

            setTimeout(() => {
                resultDiv.style.display = 'none';
                scenarioDiv.style.display = 'block';
                renderNode('start');
            }, 300);
        }

        // Initial render
        renderNode('start');

        // Explanation button logic
        explanationButton.addEventListener('click', () => {
            const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
            if (isHidden) {
                 explanationSection.style.display = 'block';
                 explanationSection.style.opacity = 0;
                 explanationSection.style.transform = 'translateY(20px)';
                 setTimeout(() => {
                     explanationSection.style.opacity = 1;
                     explanationSection.style.transform = 'translateY(0)';
                 }, 50); // Small delay to ensure display change takes effect before animating
             } else {
                 explanationSection.style.opacity = 0;
                 explanationSection.style.transform = 'translateY(20px)';
                 setTimeout(() => {
                      explanationSection.style.display = 'none';
                 }, 300); // Match animation duration
             }

            explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'פענוח המשימה: רקע היסטורי';
        });

        // Restart button logic
        restartButton.addEventListener('click', restartMission);
    });
</script>
---
```