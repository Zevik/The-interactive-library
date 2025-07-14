---
title: "מנהל פסטיבל הסרטים: אמנות הבחירה תחת לחץ"
english_slug: film-festival-director-the-art-of-choice-under-pressure
category: "מדעי החברה / כלכלה התנהגותית"
tags: [קבלת החלטות, כלכלה התנהגותית, הטיות קוגניטיביות, ניהול, אמנות]
---
# מנהל פסטיבל הסרטים: אמנות הבחירה תחת לחץ

ברוכים הבאים לתפקיד הנחשק (והמלחיץ!) של מנהל פסטיבל הסרטים הבינלאומי המפורסם. השנה הוגשו שיאי כל הזמנים - אלפי יצירות קולנועיות מכל העולם, הממתינות לרגע שבו שמם יופיע בתוכנית הרשמית. המשימה שלך: לאצור בקפידה את 6 הסרטים שיאפיינו את הפסטיבל השנה ויתחרו על הפרס הגדול. זוהי אינה רק בחירה מבין הטובים ביותר, אלא מסע מורכב של שיקול דעת, איזונים, פשרות - והתמודדות עם הטיות נסתרות.

<div id="app-container">
    <div id="game-header">
        <h2>אצור את תוכנית הפסטיבל</h2>
        <p>בחר/י בדיוק <span id="selected-count">0</span> מתוך <span id="total-films">15</span> סרטים כדי ליצור את ה-6 המובחרים לתחרות. כל בחירה מעצבת את גורל הפסטיבל!</p>
    </div>
    <div id="film-list">
        <!-- Film items will be loaded here by JavaScript -->
        <p class="loading-message">טוען סרטים מרחבי העולם...</p>
    </div>
    <button id="submit-selection" disabled>בחר 6 סרטים כדי לשלוח</button>
    <div id="result-area" class="hidden">
        <div class="result-header">
             <h3>תוצאת הפסטיבל:</h3>
             <p id="outcome-text"></p>
        </div>
        <div class="result-details">
             <h4>שיקולים מרכזיים שהשפיעו על התוצאה:</h4>
             <ul id="outcome-details"></ul>
        </div>
         <button id="play-again" class="hidden">שחק/י שוב</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #E53935; /* A bold red, like a red carpet */
        --secondary-color: #FFB300; /* Golden, like a film award */
        --text-color: #333;
        --subtle-text-color: #666;
        --background-color: #F5F5F5; /* Light grey, clean look */
        --card-background: #FFFFFF;
        --border-color: #E0E0E0;
        --selected-border: #4CAF50; /* Green for selection */
        --selected-background: #E8F5E9; /* Light green */
        --shadow-color: rgba(0, 0, 0, 0.1);
        --success-color: #4CAF50;
        --warning-color: #FF9800;
        --error-color: #F44336;
    }

    @font-face {
        font-family: 'Varela_Round';
        src: url('https://fonts.gstatic.com/s/varelaround/v20/w8gdH283Tvk__lukxJnEwlpp.woff2') format('woff2');
        unicode-range: U+0590-05FF, U+20AA, U+25CC, U+FB1D-FB4F; /* Hebrew glyphs */
    }

    body {
        font-family: 'Varela_Round', Arial, sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: #eceff1; /* Lighter background for the whole page */
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3, h4 {
        color: var(--primary-color);
    }

    #app-container {
        max-width: 960px;
        margin: 20px auto;
        padding: 30px;
        background-color: var(--background-color);
        border-radius: 12px;
        box-shadow: 0 8px 16px var(--shadow-color);
    }

    #game-header {
        text-align: center;
        margin-bottom: 30px;
    }

    #game-header h2 {
        margin-top: 0;
        color: var(--text-color);
    }

    #film-list {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); /* Slightly wider cards */
        gap: 20px; /* Increased gap */
        margin-top: 20px;
    }

    .loading-message {
        grid-column: 1 / -1; /* Center the message */
        text-align: center;
        font-style: italic;
        color: var(--subtle-text-color);
    }

    .film-item {
        border: 1px solid var(--border-color);
        padding: 20px; /* Increased padding */
        border-radius: 8px; /* More rounded corners */
        background-color: var(--card-background);
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 220px; /* Ensure roughly uniform height */
        box-shadow: 0 2px 5px var(--shadow-color);
    }

    .film-item:hover {
        transform: translateY(-5px); /* Lift effect on hover */
        box-shadow: 0 6px 12px var(--shadow-color);
        border-color: var(--secondary-color);
    }

    .film-item.selected {
        border-color: var(--selected-border);
        box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3); /* Green shadow */
        background-color: var(--selected-background);
         /* Add a subtle animation on selection */
        animation: popIn 0.3s ease;
    }

    @keyframes popIn {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }


    .film-item h4 {
        margin-top: 0;
        margin-bottom: 8px; /* Increased margin */
        color: var(--primary-color);
        font-size: 1.1em;
    }

    .film-item p {
        margin-bottom: 5px;
        font-size: 0.95em; /* Slightly larger font */
        color: var(--subtle-text-color);
    }

    .film-item .synopsis {
         font-style: italic;
         color: var(--text-color);
         flex-grow: 1; /* Allows synopsis to take available space */
         margin-bottom: 10px;
         font-size: 0.9em; /* Synopsis can be slightly smaller */
    }

    .film-item .review {
        font-size: 0.85em; /* Slightly larger review font */
        color: var(--secondary-color); /* Highlight reviews */
        margin-top: 10px; /* Increased margin */
        border-top: 1px dashed var(--border-color);
        padding-top: 10px;
    }

     .film-item input[type="checkbox"] {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 10; /* Ensure checkbox is clickable above all */
        width: 20px;
        height: 20px;
        cursor: pointer;
     }

    button {
        display: block;
        margin: 30px auto 20px; /* More space around buttons */
        padding: 12px 25px; /* Larger padding */
        font-size: 1.2em; /* Larger font */
        color: #fff;
        background-color: var(--primary-color);
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Varela_Round', Arial, sans-serif; /* Use the same font */
    }

    button:hover:not(:disabled) {
        background-color: #D32F2F; /* Darker red */
        transform: translateY(-2px); /* Slight lift on hover */
    }

     button:active:not(:disabled) {
         transform: translateY(0); /* Press effect */
     }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.8;
    }

    #result-area {
        margin-top: 40px; /* More space */
        padding: 30px;
        border: 1px solid var(--success-color);
        background-color: #e8f5e9; /* Light green */
        color: var(--text-color);
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(76, 175, 80, 0.2);
        animation: fadeIn 0.8s ease-out; /* Fade in animation */
    }

     @keyframes fadeIn {
         0% { opacity: 0; transform: translateY(20px); }
         100% { opacity: 1; transform: translateY(0); }
     }

    #result-area.warning {
        border-color: var(--warning-color);
        background-color: #fff3e0; /* Light orange */
        box-shadow: 0 4px 8px rgba(255, 152, 0, 0.2);
    }

    #result-area.error {
        border-color: var(--error-color);
        background-color: #ffebee; /* Light red */
        box-shadow: 0 4px 8px rgba(244, 67, 54, 0.2);
    }


    #result-area .result-header h3 {
        margin-top: 0;
        color: var(--text-color); /* Keep header text color standard */
    }
     #result-area.success .result-header h3 { color: var(--success-color); }
     #result-area.warning .result-header h3 { color: var(--warning-color); }
     #result-area.error .result-header h3 { color: var(--error-color); }


    #result-area p#outcome-text {
         font-size: 1.1em;
         font-weight: bold;
         margin-bottom: 20px;
         color: var(--text-color);
    }

    #result-area h4 {
         color: var(--text-color);
         margin-bottom: 10px;
         margin-top: 15px;
         font-size: 1em;
         border-bottom: 1px dashed var(--border-color);
         padding-bottom: 5px;
    }
     #result-area.success h4 { border-bottom-color: var(--success-color); }
     #result-area.warning h4 { border-bottom-color: var(--warning-color); }
     #result-area.error h4 { border-bottom-color: var(--error-color); }


     #result-area ul {
         list-style: none; /* Remove default list style */
         padding-left: 0;
         margin-bottom: 0;
     }
     #result-area li {
         margin-bottom: 8px;
         font-size: 0.95em;
         line-height: 1.5;
         position: relative;
         padding-right: 20px; /* Space for custom bullet */
     }

     #result-area li:before {
         content: '•'; /* Custom bullet */
         color: var(--primary-color); /* Bullet color */
         font-weight: bold;
         display: inline-block;
         width: 1em;
         margin-right: 5px;
         position: absolute;
         right: 0;
     }
     #result-area.success li:before { color: var(--success-color); }
     #result-area.warning li:before { color: var(--warning-color); }
     #result-area.error li:before { color: var(--error-color); }


    .hidden {
        display: none;
    }

    #explanation-toggle {
        display: block;
        margin: 40px auto 20px; /* More space */
        padding: 10px 20px;
        font-size: 1.1em;
        color: #fff;
        background-color: #757575; /* Grey */
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Varela_Round', Arial, sans-serif;
    }
     #explanation-toggle:hover {
         background-color: #616161; /* Darker grey */
         transform: translateY(-2px);
     }

    #explanation-area {
        margin-top: 20px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        box-shadow: 0 4px 8px var(--shadow-color);
         animation: fadeIn 0.8s ease-out; /* Fade in */
    }
     #explanation-area h2 {
         margin-top: 0;
         color: var(--text-color);
     }
     #explanation-area h3 {
         margin-bottom: 8px;
         color: var(--primary-color);
         font-size: 1.1em;
         margin-top: 20px;
     }
     #explanation-area p {
         line-height: 1.7;
         color: var(--text-color);
         margin-bottom: 15px;
     }
     #explanation-area p:last-child {
         margin-bottom: 0;
     }

     /* Responsive adjustments */
     @media (max-width: 768px) {
        #app-container {
            padding: 20px;
        }
        #film-list {
             grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
             gap: 15px;
        }
        .film-item {
            padding: 15px;
            min-height: 200px;
        }
        button {
            font-size: 1em;
            padding: 10px 20px;
        }
     }

</style>

<button id="explanation-toggle">הצג/הסתר תובנות מקצועיות</button>

<div id="explanation-area" class="hidden">
    <h2>מאחורי הקלעים: האתגר הקוגניטיבי של אוצרות קולנועית</h2>

    <p>תפקיד כמו מנהל פסטיבל סרטים הוא דוגמה קלאסית לאתגרים של קבלת החלטות בעולם האמיתי. אינך פועל בריק, ואין נוסחת קסם לבחירה "הטובה ביותר". הנה כמה נקודות למחשבה:</p>

    <h3>ניווט בעולם של ריבוי קריטריונים מתנגשים</h3>
    <p>במקום פשוט לבחור את הסרט "הכי טוב" (הגדרה סובייקטיבית כשלעצמה), עליך לשקלל אינספור גורמים: מצוינות אמנותית, פוטנציאל למשוך קהל (מבקרים, עיתונאים, חובבי קולנוע), חדשנות, רלוונטיות תרבותית, איזון ז'אנרים, אורך הסרט (משפיע על לוח הזמנים), המוניטין של הבמאי, ואפילו אילו סרטים אחרים כבר נבחרו והאם הם יוצרים תוכנית מגובשת. לעיתים קרובות, קידום קריטריון אחד (למשל, אמנותיות טהורה) בא על חשבון אחר (פופולריות), ולהיפך. זוהי פעולת איזון עדינה.</p>

    <h3>השפעת עומס המידע וקיצורי דרך קוגניטיביים (היוריסטיקות)</h3>
    <p>כשעומדים בפני אלפי סרטים, אין אפשרות לעבד את כל המידע ביעילות ובאופן רציונלי לחלוטין. המוח שלנו נוטה להשתמש ב"היוריסטיקות" - כללי אצבע וקיצורי דרך מנטליים. היוריסטיקת הזמינות, למשל, עלולה לגרום לך לתת משקל יתר לסרט ששמעת עליו לאחרונה או שקיבל ביקורת אחת סנסציונית (כי המידע זמין ובולט). היוריסטיקת הייצוגיות עשויה לגרום לך להעדיף סרט של במאי מוכר כי הוא "נראה" כמו סרט פסטיבל קלאסי, גם אם סרט אחר, פחות מוכר, עשוי להיות טוב יותר.</p>

    <h3>הטיות קוגניטיביות בפעולה</h3>
    <p>מעבר להיוריסטיקות, הטיות קוגניטיביות משפיעות על שיקול הדעת שלנו בצורה עקבית ולעיתים בלתי מודעת. <strong>הטיית הסמכות:</strong> הערכת יתר של סרט רק בגלל שמו של הבמאי או ההפקה. <strong>הטיית האישור:</strong> חיפוש או מתן משקל רב יותר לביקורות או מידע התומכים בדעה קיימת שכבר גיבשת על הסרט. <strong>אפקט ההילה:</strong> אם היבט אחד של הסרט (למשל, שחקן ראשי מפורסם) נתפס כחיובי, זה עלול לצבוע בתחושה חיובית גם היבטים אחרים של הסרט, ולהיפך. <strong>הטיית העוגן:</strong> האם הסרט הראשון שצפית בו בפסטיבל ישפיע בצורה לא פרופורציונלית על האופן שבו תעריך סרטים אחרים בהמשך? היכרות עם ההטיות הללו היא הצעד הראשון לצמצום השפעתן.</p>

    <h3>פשרות, עלות אלטרנטיבית ותכנון שלם</h3>
    <p>לבחור סרט אחד פירושו לוותר על אחר. זוהי עלות אלטרנטיבית מוחשית בפסטיבל עם מספר מוגבל של מקומות. כל בחירה היא פשרה - בין ז'אנרים, בין במאיים, בין סגנונות, בין שיקולים אמנותיים למסחריים. מנהל הפסטיבל אינו רק בוחר סרטים בודדים, אלא יוצר אוסף - תוכנית פסטיבל שלמה עם נרטיב, קצב וזהות משלה. על הסרטים לדבר זה עם זה וליצור יחדיו חוויה עשירה ומגוונת.</p>

    <h3>אי-ודאות וניהול סיכונים אמנותי</h3>
    <p>אף אחד לא יודע בוודאות אילו סרטים יהפכו ללהיטי קופות או יזכו בפרסים. יש אי-ודאות מובנית בעולם האמנות. האם לבחור בסרט נועז אך מסוכן של במאי אלמוני, או ללכת על בטוח עם סרט שגרתי אך נעים של במאי מוכר? כל בחירה נושאת סיכון פוטנציאלי - הן למוניטין של הסרט והן למוניטין של הפסטיבל עצמו. קבלת החלטות תחת אי-ודאות היא לב ליבו של התפקיד, והיא דורשת אינטואיציה, ניסיון, ויכולת להעריך סיכונים בצורה מושכלת (גם אם לא תמיד רציונלית לחלוטין).</p>

    <p>ההחלטות שלך כאן הן סימולציה פשוטה של המורכבות העצומה הזו. נסה/י לבחור שוב ושוב בדרכים שונות ושים/י לב כיצד הבחירות, ואולי ההטיות שלך, מעצבות את הצלחת הפסטיבל - או כישלונו.</p>
</div>

<script>
    const FILMS = [
        { id: 1, name: "צללים נעים", director: "אילנה כהן", director_info: "במאית מוערכת, זכתה בפרסים", genre: "דרמה", synopsis: "סיפור אינטימי על אובדן ותקווה בעיר גדולה, מצולם בשחור-לבן מרהיב.", length: 110, review: "מרגש ועוצמתי, משחק מעולה! מועמד בולט." },
        { id: 2, name: "הקוד של קסנדרה", director: "דניאל לוי", director_info: "סרט ראשון באורך מלא", genre: "מותחן מדע בדיוני", synopsis: "מדענית צעירה מגלה נוסחה שיכולה לנבא את העתיד - ההשלכות מזעזעות.", length: 140, review: "שאפתני ופורץ דרך מבחינה ויזואלית, אך מבולבל ואיטי מדי בעלילתו." },
        { id: 3, name: "צחוק ברוח", director: "יוסי אדלר", director_info: "מוכר בעיקר מקומדיות טלוויזיה", genre: "קומדיה רומנטית", synopsis: "שני זרים נפגשים בנסיבות מצחיקות במיוחד ומגלים אהבה במקומות הכי בלתי צפויים.", length: 95, review: "מצחיק וקליל, כיף לצפייה בערב. נוסחה מוכרת שעובדת." },
        { id: 4, name: "השדות המוזהבים", director: "מאיה שטיין", director_info: "במאית דוקומנטרית עטורת שבחים", genre: "דוקומנטרי", synopsis: "מסע תיעודי חודרני אל מאחורי הקלעים של תעשיית המזון המודרנית, עם ממצאים מטרידים.", length: 85, review: "מעורר מחשבה ומזעזע לפרקים, מצולם להפליא. חובה לצפייה." },
        { id: 5, name: "הקולות שבפנים", director: "נועה גורן", director_info: "עצמאית, זכתה בפסטיבלים קטנים", genre: "דרמה פסיכולוגית", synopsis: "אישה צעירה מתמודדת עם שדים פנימיים לאחר טראומה קשה, בדרך מטלטלת ומפתיעה.", length: 100, review: "משחק כובש ובימוי נועז. יצירה אישית ועמוקה." },
        { id: 6, name: "רובוטים על הירח", director: "עידן מור", director_info: "במאי של שוברי קופות הוליוודיים", genre: "אקשן-מדע בדיוני", synopsis: "צוות אסטרונאוטים נלחם ברובוטים סוררים על פני הירח הנטוש. פיצוצים ואפקטים מיוחדים לכל המשפחה.", length: 155, review: "עשוי היטב מבחינה טכנית, אבל בלי נשמה או עומק. פלופ צפוי?" },
        { id: 7, name: "סימפוניה אורבנית", director: "אנה בלום", director_info: "במאית ניסיונית, מוכרת ממיצגים", genre: "סרט אמנותי", synopsis: "מדיטציה ויזואלית וקולית על הקצב והכאוס של חיי העיר הגדולה. ללא דיאלוג.", length: 70, review: "יצירה ויזואלית מרתקת ומקורית, אבל דורשת סבלנות. בהחלט לא לכל אחד." },
        { id: 8, name: "הירושה", director: "אלון בר", director_info: "במאי דרמות טלוויזיה פופולריות", genre: "דרמה משפחתית", synopsis: "סודות ישנים וכואבים נחשפים כאשר משפחה עשירה מתכנסת לקרוא צוואה מפתיעה.", length: 120, review: "צפוי וקצת מלודרמטי, אבל משחק טוב מבטיח הנאה מסוימת. להיט טלוויזיה פוטנציאלי." },
        { id: 9, name: "מתחת לפני השטח", director: "שירה לוי", director_info: "במאית סרטי אימה עצמאיים מוצלחים", genre: "אימה", synopsis: "קבוצת חברים תועים ונקלעים למצב מסוכן במיוחד במערה נטושה, שם אורבת להם סכנה על-טבעית.", length: 90, review: "מפחיד ומותח בטירוף, בימוי אפקטיבי שמשתמש במשאבים מוגבלים בצורה גאונית." },
        { id: 10, name: "המבשלת הגדולה", director: "דניאל כץ", director_info: "זוכה תוכנית ריאליטי בישול", genre: "קומדיה", synopsis: "שף כושל בעל חלומות גדולים פותח מסעדה חדשה עם צוות עובדים מוזר לא פחות ממנו.", length: 88, review: "חמוד ושנון, בדיחות טובות. קומדיה קלילה ומהנה." },
        { id: 11, name: "גלגלים עתיקים", director: "אהרן ינאי", director_info: "במאי ותיק, יצר קלאסיקות ישראליות", genre: "דרמה היסטורית", synopsis: "סיפורם ההירואי והמרגש של חלוצים בארץ ישראל בשנות ה-30 של המאה הקודמת.", length: 135, review: "קלאסיקה מודרנית מיידית, משחק מופלא ובימוי מושלם. מועמד ודאי לפרסים." },
        { id: 12, name: "המסע לכוכב ירוק", director: "ליאת שוורץ", director_info: "סרט אנימציה ראשון באורך מלא", genre: "אנימציה", synopsis: "ילדה אמיצה והחבר הרובוטי החמוד שלה יוצאים למסע מופלא להציל את כדור הארץ הגוסס.", length: 105, review: "ויזואלית מהמם, סוחף ומרגש לילדים (ומבוגרים עם נשמה). סיפור אולי קצת פשטני למבקרים ציניים." },
        { id: 13, name: "החיים כפזל", director: "רועי שלו", director_info: "במאי צעיר ומבטיח, סרט שני", genre: "דרמה פילוסופית", synopsis: "חייו של אדם אחד מפורקים ומוקרנים בסדר כרונולוגי הפוך, חושפים את משמעות הזיכרון והזמן.", length: 115, review: "מסקרן ומקורי מבחינה מבנית, עם סוף מפתיע ומרסק. דורש ריכוז." },
        { id: 14, name: "שירת הים", director: "מאיר רובין", director_info: "דוקומנטריסט סביבתי בעל שם עולמי", genre: "דוקומנטרי", synopsis: "תיעוד מרהיב ועוצר נשימה של החיים התת-ימיים בים האדום והאיומים הנשקפים להם.", length: 75, review: "צילום עוצר נשימה שמשאיר פעורי פה. מסר חשוב ודחוף. סרט יפהפה אך קצר." },
         { id: 15, name: "המסיבה", director: "קרן טל", director_info: "מוכרת מדרמות קצרות זוכות פרסים", genre: "קומדיה שחורה", synopsis: "מסיבת יום הולדת הופכת לכאוס מוחלט כשהאמת המכוערת יוצאת לאור, בחשיפה אחר חשיפה.", length: 92, review: "מרושע, שנון ומצחיק בטירוף. תסריט מבריק ומשחק מצוין. להיט פסטיבלים פוטנציאלי." }
    ];

    const TARGET_SELECTION_COUNT = 6;
    const totalFilmsCount = FILMS.length;

    const filmListDiv = document.getElementById('film-list');
    const selectedCountSpan = document.getElementById('selected-count');
    const totalFilmsSpan = document.getElementById('total-films');
    const submitButton = document.getElementById('submit-selection');
    const resultArea = document.getElementById('result-area');
    const outcomeText = document.getElementById('outcome-text');
    const outcomeDetails = document.getElementById('outcome-details');
    const explanationToggle = document.getElementById('explanation-toggle');
    const explanationArea = document.getElementById('explanation-area');
    const playAgainButton = document.getElementById('play-again');


    let selectedFilms = [];

    function renderFilms() {
        filmListDiv.innerHTML = ''; // Clear current list
        FILMS.forEach(film => {
            const filmItem = document.createElement('div');
            filmItem.classList.add('film-item');
            filmItem.dataset.id = film.id;

            const isSelected = selectedFilms.some(f => f.id === film.id);
            if (isSelected) {
                filmItem.classList.add('selected');
            }

            filmItem.innerHTML = `
                <input type="checkbox" id="film-${film.id}" ${isSelected ? 'checked' : ''}>
                <label for="film-${film.id}">
                    <h4>${film.name}</h4>
                    <p><strong>במאי/ת:</strong> ${film.director} (${film.director_info})</p>
                    <p><strong>ז'אנר:</strong> ${film.genre}</p>
                    <p class="synopsis">${film.synopsis}</p>
                    <p><strong>אורך:</strong> ${film.length} דקות</p>
                    <p class="review">"<em>${film.review}</em>"</p>
                </label>
            `;

            // Add click listener to the item (the label) to toggle checkbox
            filmItem.querySelector('label').addEventListener('click', (e) => {
                // Prevent label click from double-toggling if clicking exactly on the checkbox within the label
                 if (e.target.type === 'checkbox') return;
                 const checkbox = filmItem.querySelector('input[type="checkbox"]');
                 checkbox.checked = !checkbox.checked;
                 toggleFilmSelection(film.id, checkbox.checked);
            });

             // Add change listener to the checkbox specifically
             filmItem.querySelector('input[type="checkbox"]').addEventListener('change', (e) => {
                 toggleFilmSelection(film.id, e.target.checked);
             });

            filmListDiv.appendChild(filmItem);
        });
        updateSelectionCount();
    }

    function toggleFilmSelection(filmId, isSelected) {
        const film = FILMS.find(f => f.id === filmId);
        const filmItemElement = filmListDiv.querySelector(`.film-item[data-id="${filmId}"]`);
        const checkbox = filmItemElement.querySelector('input[type="checkbox"]');


        if (isSelected && selectedFilms.length < TARGET_SELECTION_COUNT) {
            if (!selectedFilms.some(f => f.id === filmId)) {
                selectedFilms.push(film);
                filmItemElement.classList.add('selected');
            }
        } else if (!isSelected) {
            selectedFilms = selectedFilms.filter(f => f.id !== filmId);
            filmItemElement.classList.remove('selected');
        } else {
             // Tried to select more than allowed, reset checkbox state visually
             checkbox.checked = false;
             // Optional: add a visual shake or temporary border to indicate limit reached
             filmItemElement.style.transition = 'none'; // Disable transition for shake
             filmItemElement.style.border = `2px solid ${var(--error-color)}`;
             setTimeout(() => {
                 filmItemElement.style.border = ''; // Reset border
                 filmItemElement.style.transition = ''; // Re-enable transition
             }, 300);
        }
        updateSelectionCount();
    }

    function updateSelectionCount() {
        selectedCountSpan.textContent = selectedFilms.length;

        if (selectedFilms.length === TARGET_SELECTION_COUNT) {
             submitButton.disabled = false;
             submitButton.textContent = `שגר את תוכנית הפסטיבל! (${selectedFilms.length}/${TARGET_SELECTION_COUNT})`;
             submitButton.classList.add('ready'); // Optional class for styling when ready
         } else if (selectedFilms.length < TARGET_SELECTION_COUNT) {
             submitButton.disabled = true;
             submitButton.textContent = `בחר/י עוד ${TARGET_SELECTION_COUNT - selectedFilms.length} סרטים`;
             submitButton.classList.remove('ready');
          } else { // Should not happen with current logic, but for safety
               submitButton.disabled = true;
               submitButton.textContent = `בחר/י בדיוק ${TARGET_SELECTION_COUNT} סרטים`;
               submitButton.classList.remove('ready');
          }
    }

    function evaluateSelection() {
        if (selectedFilms.length !== TARGET_SELECTION_COUNT) {
            // This should not happen if the button is disabled, but good practice
            alert(`אנא בחר/י בדיוק ${TARGET_SELECTION_COUNT} סרטים.`);
            return;
        }

        // --- Evaluation Logic (Simulated Complexity) ---
        const selectedGenres = new Set(selectedFilms.map(f => f.genre));
        const genreDiversity = selectedGenres.size; // More genres is generally better for a festival program

        const directorTypes = {
            acclaimed: 0, // מוערכת, זוכה פרסים, עטורת שבחים, ותיק, קלאסיקות
            new_promising: 0, // סרט ראשון, עצמאית, ניסיונית, צעיר ומבטיח
            popular_commercial: 0, // שוברי קופות, טלוויזיה פופולרית, ריאליטי
            independent_niche: 0 // אימה עצמאיים, קומדיה שחורה, פילוסופית
        };

        selectedFilms.forEach(film => {
            const info = film.director_info;
            if (info.includes('מוערכת') || info.includes('פרסים') || info.includes('שבחים') || info.includes('ותיק') || info.includes('קלאסיקות')) {
                directorTypes.acclaimed++;
            } else if (info.includes('סרט ראשון') || info.includes('עצמאית') || info.includes('ניסיונית') || info.includes('מבטיח')) {
                directorTypes.new_promising++;
            } else if (info.includes('שוברי קופות') || info.includes('טלוויזיה פופולרית') || info.includes('ריאליטי')) {
                directorTypes.popular_commercial++;
            } else { // Default or less specific types
                 directorTypes.independent_niche++;
            }
        });

        const totalPopularCommercial = directorTypes.popular_commercial;
        const totalAcclaimedNew = directorTypes.acclaimed + directorTypes.new_promising + directorTypes.independent_niche; // Sum of less purely commercial types


        const avgLength = selectedFilms.reduce((sum, f) => sum + f.length, 0) / selectedFilms.length;
        const hasTooLong = selectedFilms.some(f => f.length > 145); // Adjusted threshold slightly
        const hasTooShort = selectedFilms.some(f => f.length < 85); // Adjusted threshold

        const positiveReviewKeywords = ['מעולה', 'מרגש', 'עוצמתי', 'מועורר מחשבה', 'מצחיק', 'כובש', 'נועז', 'מפחיד', 'מותח', 'שנון', 'מופלא', 'מקורי', 'עוצר נשימה', 'מרושע', 'חובה לצפייה', 'מועמד בולט', 'הירואי', 'מרסק', 'מבריק'];
        const negativeReviewKeywords = ['מבולבל', 'איטי מדי', 'בלי נשמה', 'לא לכל אחד', 'צפוי', 'מלודרמטי', 'פשטני', 'פלופ צפוי', 'דורש סבלנות'];

        let positiveReviewScore = 0;
        let negativeReviewScore = 0;

        selectedFilms.forEach(film => {
            const review = film.review.toLowerCase();
            positiveReviewKeywords.forEach(keyword => {
                if (review.includes(keyword)) positiveReviewScore++;
            });
            negativeReviewKeywords.forEach(keyword => {
                if (review.includes(keyword)) negativeReviewScore++;
            });
        });

        const overallReviewSentiment = positiveReviewScore - negativeReviewScore;

        let outcome = { text: "תוצאה ניטרלית...", details: [], class: "" }; // Add a class for styling

        // --- Determining Outcome based on combined factors ---

        // Scenario 1: Heavy on commercial/known names, low diversity
        if (totalPopularCommercial >= 3 && genreDiversity <= 3 && overallReviewSentiment >= -1) { // Allow slightly mixed reviews if popular
             outcome.text = "הפסטיבל משך קהל אדיר והיה הצלחה קופתית מסחררת! הכרטיסים נמכרו במהירות הבזק. המבקרים אמנם קטלו את חוסר המקוריות, אבל הקהל הצביע ברגליים (ובארנקים).";
             outcome.details.push("<strong>הצלחה קופתית (כסף כסף):</strong> התמקדות בבמאים מוכרים וז'אנרים פופולריים התגלתה כמנוע הכנסות אדיר.");
             outcome.details.push("<strong>ביקורות פושרות/שליליות:</strong> המבקרים התאכזבו מהיעדר חדשנות ומגוון אמנותי.");
             if (hasTooLong) outcome.details.push("<strong>קשיים לוגיסטיים:</strong> סרטים ארוכים מדי יצרו עומס בלוח ההקרנות.");
             outcome.class = "warning"; // Warning because critical acclaim is low
        }
        // Scenario 2: Heavy on new/independent/acclaimed, high diversity
        else if (totalAcclaimedNew >= 4 && genreDiversity >= 4 && overallReviewSentiment >= 2 && avgLength < 125) {
             outcome.text = "הפסטיבל זכה לשבחים היסטריים מהמבקרים ומהעיתונות הבינלאומית על תוכנית נועזת, מגוונת ואיכותית! נחשב לאחד הפסטיבלים המשמעותיים של השנה.";
             outcome.details.push("<strong>הצלחה אמנותית (פרסים והערכה):</strong> תוכנית מגוונת עם דגש על איכות אמנותית ובמאים חדשים זיכתה את הפסטיבל במוניטין יוקרתי.");
             outcome.details.push("<strong>אתגר קהל:</strong> ללא מספיק 'שמות גדולים', מכירת הכרטיסים לקהל הרחב הייתה איטית יותר מהמצופה.");
             if (hasTooShort) outcome.details.push("<strong>תלונות על אורך:</strong> חלק מהצופים התלוננו על סרטים קצרים מדי שלא הרגישו כמו "פיצ'ר" מלא.");
             outcome.class = "success";
        }
        // Scenario 3: Low diversity or poor length balance
        else if (genreDiversity <= 2 || hasTooLong || hasTooShort) {
            outcome.text = "הפסטיבל סבל מבעיות תדמית ולוגיסטיקה. הקהל והמבקרים התלוננו על תוכנית לא מאוזנת וקשיים בהקרנות.";
            if (genreDiversity <= 2) outcome.details.push("<strong>חוסר גיוון ז'אנרים:</strong> התוכנית הייתה מונוטונית ולא הצליחה למשוך פלחי קהל שונים.");
            if (hasTooLong) outcome.details.push("<strong>סרטים ארוכים מדי:</strong> יצרו בעיות קשות בלוח הזמנים וגרמו לעיכובים ותלונות.");
            if (hasTooShort) outcome.details.push("<strong>סרטים קצרים מדי:</strong> נתפסו כפחות משמעותיים ופגעו בתחושת ה'אירוע'.");
             outcome.details.push("<strong>מוניטין נפגע:</strong> הפסטיבל נתפס כלא מקצועי ולא מתוכנן היטב.");
            outcome.class = "error";
        }
        // Scenario 4: Overall poor selection based on reviews
         else if (overallReviewSentiment < 0) {
             outcome.text = "הפסטיבל היה כישלון מהדהד. רוב הסרטים שהוצגו קיבלו ביקורות פושרות עד קוטלות, והקהל הגיב באדישות.";
             outcome.details.push("<strong>איכות נמוכה:</strong> בחירה בסרטים שקיבלו ביקורות שליליות או פושרות פגעה קשות באיכות הכללית של התוכנית.");
             outcome.details.push("<strong>חוסר באזז:</strong> ללא סרטים מדוברים לחיוב, הפסטיבל לא יצר עניין ונותר בשוליים.");
             if (totalAcclaimedNew + totalPopularCommercial <= 2) outcome.details.push("<strong>העדר שמות:</strong> ללא מספיק במאיים מוכרים או סרטים עם פוטנציאל, היה קשה למשוך תשומת לב.");
             outcome.class = "error";
         }
        // Scenario 5: Balanced, moderate success
         else {
             outcome.text = "הפסטיבל נחשב להצלחה מתונה. הוא הציע איזון טוב בין אמנות לפופולריות ויצר עניין מסוים בקהל ובמבקרים.";
             outcome.details.push("<strong>איזון טוב:</strong> השילוב בין סרטים של במאיים מוכרים לסרטים חדשים יצר תוכנית מעניינת ומגוונת יחסית.");
             if (genreDiversity >= 4) outcome.details.push("<strong>מגוון ז'אנרים:</strong> כיסוי ז'אנרים שונים משך פלחי קהל רחבים יותר.");
             if (overallReviewSentiment > 0) outcome.details.push("<strong>תגובות חיוביות:</strong> רוב הסרטים הנבחרים התקבלו היטב על ידי המבקרים.");
             outcome.class = "success"; // Moderate success is still success class
         }

        displayOutcome(outcome);
    }

    function displayOutcome(outcome) {
        outcomeText.textContent = outcome.text;
        outcomeDetails.innerHTML = '';
        outcome.details.forEach(detail => {
            const li = document.createElement('li');
            li.innerHTML = detail; // Use innerHTML to allow bold text
            outcomeDetails.appendChild(li);
        });

        // Add/remove class based on outcome for dynamic styling
        resultArea.classList.remove('hidden', 'success', 'warning', 'error');
        resultArea.classList.add(outcome.class);
        resultArea.classList.remove('hidden');

         // Disable selection after submission
         document.querySelectorAll('.film-item input[type="checkbox"]').forEach(checkbox => {
              checkbox.disabled = true;
         });
         submitButton.disabled = true;
         submitButton.textContent = 'הבחירה נשלחה!';
         playAgainButton.classList.remove('hidden'); // Show play again button
         submitButton.classList.remove('ready'); // Remove ready style
    }

    function toggleExplanation() {
        explanationArea.classList.toggle('hidden');
        const isHidden = explanationArea.classList.contains('hidden');
        explanationToggle.textContent = isHidden ? 'הצג תובנות מקצועיות' : 'הסתר תובנות מקצועיות';
    }

     function resetGame() {
        selectedFilms = [];
        resultArea.classList.add('hidden');
         playAgainButton.classList.add('hidden');
         // Re-enable checkboxes and update display
         document.querySelectorAll('.film-item input[type="checkbox"]').forEach(checkbox => {
              checkbox.disabled = false;
              checkbox.checked = false;
         });
         renderFilms(); // Re-render to reset visual state
         updateSelectionCount(); // Update button state
     }


    // Initial setup
    totalFilmsSpan.textContent = totalFilmsCount;
    renderFilms();

    submitButton.addEventListener('click', evaluateSelection);
    explanationToggle.addEventListener('click', toggleExplanation);
    playAgainButton.addEventListener('click', resetGame);

</script>
```