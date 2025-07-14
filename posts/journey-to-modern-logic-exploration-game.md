---
title: "המסע אל הלוגיקה המודרנית: משחק חקירה"
english_slug: journey-to-modern-logic-exploration-game
category: "מדעים מדויקים / מתמטיקה"
tags:
  - לוגיקה
  - פילוסופיה
  - אריסטו
  - תחשיב פסוקים
  - היסטוריה של המדע
  - חשיבה ביקורתית
---
# המסע אל הלוגיקה המודרנית: משחק חקירה

הצטרפו אלינו למסע מרתק אל יסודות החשיבה הלוגית! נגלה יחד כיצד התמודדו הוגי עבר עם ניתוח טיעונים, ואיך כלים חדשים שפותחו שינו את פני הלוגיקה ואפשרו לנו להבין טוב יותר את העולם.

במשחק הזה, תתנסו בעצמכם באתגרים לוגיים ותראו ממקור ראשון למה נזקקנו למעבר מהלוגיקה העתיקה של אריסטו אל הלוגיקה המודרנית. האם אתם מוכנים לאתגר?

<div id="game-area" dir="rtl">
    <h2 id="phase-title">שלב 1: בזירה האריסטוטלית (סילוגיזם)</h2>
    <div id="score-area">
        <div id="score-display">ניקוד: <span id="current-score">0</span></div>
        <div id="progress-display">שאלה <span id="current-arg-index">1</span> מתוך <span id="total-args"></span></div>
    </div>
    <div id="instruction">
        <p>ברוכים הבאים לשלב הראשון! כאן נתנסה בניתוח טיעונים על פי הכללים הנוקשים של הסילוגיזם האריסטוטלי. מטרתכם: לקבוע האם המסקנה נובעת בהכרח מההנחות <strong>על פי כללי הסילוגיזם בלבד</strong>.</p>
        <p class="note">(התעלמו בשלב זה מהאינטואיציה היומיומית. האם הטיעון תקף *סילוגיסטית*?)</p>
    </div>
    <div id="argument-card">
        <div id="argument-display"></div>
    </div>
    <div id="buttons">
        <button id="valid-button" class="answer-button">תקף</button>
        <button id="invalid-button" class="answer-button">לא תקף</button>
    </div>
    <div id="feedback"></div>
    <button id="next-button" class="game-button" style="display: none;">המשך לאתגר הבא</button>
</div>

<button id="toggle-explanation">הצג/הסתר מסע הרקע הלוגי</button>

<div id="explanation" style="display: none;" dir="rtl">
    <h2>מסע הרקע הלוגי: מהסילוגיזם לתחשיב הפסוקים</h2>

    <h3>המסע מתחיל: יסודות בלוגיקה</h3>
    <p>לוגיקה היא המצפן שלנו בעולם הטיעונים. היא עוסקת בזיהוי היסקים תקפים – מתי מסקנה נובעת באופן ודאי מהנחות נתונות. היא הכרחית לכל תחום הדורש חשיבה מסודרת וביקורתית: פילוסופיה, מדע, מתמטיקה, משפטים, ואפילו תכנות.</p>

    <h3>התחנה הראשונה: הלוגיקה האריסטוטלית</h3>
    <p>אריסטו, הפילוסוף היווני הדגול, היה מהראשונים ליצור מערכת לוגית פורמלית. מערכתו, המתמקדת בסילוגיזמים, שלטה בחשיבה הלוגית במשך למעלה מאלפיים שנה!</p>

    <h4>בניית סילוגיזם</h4>
    <p>סילוגיזם אריסטוטלי תקני הוא כמו מבנה עם שלושה קומות: שתי הנחות בקומות התחתונות ומסקנה בקומה העליונה. כל קומה מקשרת שני מושגים מתוך שלושה מושגים שונים בסך הכל, תוך שימוש בכמתים כמו 'כל', 'שום', או 'חלק מ...'.</p>
    <p><strong>דוגמה קלאסית:</strong></p>
    <ul>
        <li>כל בני האדם (M) הם בני תמותה (P) [הנחה 1]</li>
        <li>כל היוונים (S) הם בני אדם (M) [הנחה 2]</li>
        <li>לכן, כל היוונים (S) הם בני תמותה (P) [מסקנה]</li>
    </ul>
    <p>במבנה זה, S הוא 'המושג הקטן' (נושא המסקנה), P הוא 'המושג הגדול' (נשוא המסקנה), ו-M הוא 'המושג האמצעי' (הגשר בין ההנחות).</p>

    <h4>תקפות סילוגיסטית</h4>
    <p>סילוגיזם תקף מבטיח שאם ההנחות נכונות, גם המסקנה *חייבת* להיות נכונה. הדוגמה לעיל ("ברברה" - AAA-1) היא תקפה. לעומת זאת, סילוגיזם לא תקף מאפשר מצב שבו ההנחות נכונות אך המסקנה שקרית. למשל: "כל החתולים יונקים; חלק מהיונקים הם כלבים; לכן חלק מהחתולים הם כלבים". גם אם שתי ההנחות נכונות, המסקנה שקרית, ולכן הטיעון לא תקף סילוגיסטית.</p>

    <h4>גבולות עולם הסילוגיזם</h4>
    <p>על אף חשיבותה ההיסטורית, הלוגיקה האריסטוטלית הייתה מוגבלת:</p>
    <ul>
        <li>היא התמקדה בעיקר ביחסים בין קבוצות.</li>
        <li>היא התקשתה לנתח טיעונים המבוססים על קשרים לוגיים פנימיים או חיצוניים למשפטים, כמו 'אם-אז', 'או', 'וגם', 'לא'.</li>
        <li>היא לא התאימה לטיעונים מורכבים יותר או לטיעונים מתמטיים.</li>
    </ul>

    <h3>הצורך בשדרוג: לוגיקה מודרנית</h3>
    <p>עם התפתחות המדע והמתמטיקה, התברר שהכלים האריסטוטליים אינם מספיקים לניתוח טיעונים מורכבים ומגוונים. היה צורך במערכת שתטפל ביעילות בקשרים לוגיים בין משפטים שלמים ובמבנה הפנימי שלהם.</p>

    <h3>התחנה השנייה: תחשיב הפסוקים</h3>
    <p>בסוף המאה ה-19 ובתחילת המאה ה-20, הוגים כמו בול, פרגה וראסל פיתחו את הלוגיקה המודרנית. תחשיב הפסוקים הוא אבן היסוד של מהפכה זו.</p>

    <h4>פסוקים וקשרים לוגיים</h4>
    <p>בניגוד לסילוגיזם, תחשיב הפסוקים רואה במשפטים השלמים יחידות בעלות ערך אמת (אמת או שקר). הוא מתמקד באופן שבו קשָרים לוגיים (כמו אופרטורים מתמטיים) מחברים פסוקים פשוטים לפסוקים מורכבים, ואיך זה משפיע על ערך האמת הסופי.</p>
    <p><strong>הקשרים העיקריים:</strong></p>
    <ul>
        <li><strong>שלילה (¬):</strong> "לא נכון ש...". הופך אמת לשקר ושקר לאמת.</li>
        <li><strong>קוניונקציה (∧):</strong> "גם... וגם...". נכון רק אם שני הפסוקים נכונים.</li>
        <li><strong>דיסיונקציה (∨):</strong> "או... או... (כולל)". נכון אם לפחות אחד הפסוקים נכון.</li>
        <li><strong>אימפליקציה (→):</strong> "אם... אז...". שקרי רק אם התנאי נכון והתוצאה שקרית.</li>
    </ul>

    <h4>כלי הקסם: טבלאות אמת</h4>
    <p>כלי מרכזי בתחשיב הפסוקים הוא טבלת האמת, המאפשרת לבדוק באופן שיטתי את כל צירופי ערכי האמת האפשריים לפסוקים בטיעון, ולקבוע את ערך האמת של ההנחות והמסקנה בכל מקרה. טיעון תקף הוא כזה שבו לעולם לא תהיה שורה בטבלה שבה כל ההנחות נכונות והמסקנה שקרית.</p>

    <h3>יתרונות המהלך: תחשיב הפסוקים כמנוע</h3>
    <p>תחשיב הפסוקים מציע יתרונות עצומים:</p>
    <ul>
        <li>**טווח רחב:** הוא מטפל במגוון רחב בהרבה של טיעונים.</li>
        <li>**דיוק ופורמליות:** הוא מספק כלים פורמליים וחד-משמעיים לקביעת תקפות.</li>
        <li>**בסיס לקידמה:** הוא הבסיס למערכות לוגיות מורכבות וחזקות יותר, המאפשרות לנתח טיעונים במדע, מתמטיקה ומדעי המחשב ברמה חסרת תקדים.</li>
    </ul>

    <h3>המסע נמשך...</h3>
    <p>תחשיב הפסוקים הוא רק ההתחלה. לוגיקות מתקדמות יותר, כמו תחשיב הפרדיקטים, מאפשרות לנתח גם את המבנה הפנימי של המשפטים עצמם (עם כמתים ויחסים). הלוגיקה ממשיכה להתפתח ולהיות כלי חיוני להבנת העולם ולבניית מערכות חשיבה.</p>
</div>


<style>
    /* General body styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6; /* Soft background */
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure RTL is default */
        text-align: right; /* Ensure text alignment */
    }

    /* Game Container */
    #game-area {
        border: 1px solid #a0c3d2; /* Soft blue border */
        padding: 25px;
        max-width: 650px; /* Slightly wider */
        margin: 20px auto;
        background: linear-gradient(145deg, #ffffff, #e9f3f7); /* Subtle gradient */
        border-radius: 15px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer shadow */
        text-align: center;
        overflow: hidden; /* Clear floats/margins */
    }

    #phase-title {
        color: #1a5276; /* Darker blue */
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.8em;
        font-weight: bold;
        animation: fadeInDown 0.8s ease-out; /* Simple animation for title */
    }

    /* Score and Progress Display */
    #score-area {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
        padding: 10px 15px;
        background-color: #d6eaf8; /* Light blue background */
        border-radius: 8px;
        font-size: 1em;
        color: #1a5276;
        font-weight: bold;
    }

    #score-display, #progress-display {
        flex-grow: 1;
        text-align: center;
    }
     #score-display {
        border-left: 1px solid #a0c3d2; /* Separator */
        padding-left: 15px;
         margin-left: 15px;
    }
    #progress-display {
         padding-right: 15px;
         margin-right: 15px;
    }

    /* Instruction Box */
    #instruction {
        margin-bottom: 25px;
        padding: 20px;
        background-color: #eaf2f8; /* Lighter blue */
        border-right: 6px solid #3498db; /* More prominent border */
        border-radius: 8px;
        text-align: right;
        animation: fadeIn 1s ease-out; /* Fade in animation */
    }

    #instruction p {
         margin: 0 0 10px 0;
         padding: 0;
    }
     #instruction p:last-child {
         margin-bottom: 0;
     }

    #instruction .note {
        font-size: 0.95em;
        color: #555;
        margin-top: 12px;
        font-style: italic;
    }

    /* Argument Card */
    #argument-card {
        white-space: pre-wrap; /* Preserve line breaks */
        text-align: center; /* Center the card itself */
        border: 2px dashed #3498db; /* Matching border color */
        padding: 20px;
        margin-bottom: 25px;
        background-color: #ffffff;
        font-size: 1.2em; /* Larger text */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.07);
        min-height: 120px; /* Give it some minimum height */
        display: flex; /* Use flexbox to center text vertically/horizontally if needed */
        align-items: center;
        justify-content: center;
        transition: transform 0.3s ease-out; /* Animation for shake/pulse */
        font-weight: bold;
    }

     #argument-display {
        text-align: right; /* Ensure text within card is right-aligned */
        width: 100%; /* Take full width of flex container */
     }


    /* Answer Buttons */
    #buttons {
        margin-bottom: 20px;
    }
    .answer-button {
        padding: 12px 25px; /* Larger padding */
        margin: 0 15px; /* More margin */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 8px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s ease; /* Add transform for press effect */
        font-weight: bold;
        min-width: 120px; /* Minimum width */
    }

    #valid-button {
        background-color: #2ecc71; /* Emerald Green */
        color: white;
    }

    #valid-button:hover {
        background-color: #27ae60; /* Darker green */
        transform: translateY(-2px); /* Lift effect */
    }
     #valid-button:active {
         transform: scale(0.98); /* Press effect */
     }


    #invalid-button {
        background-color: #e74c3c; /* Alizarin Red */
        color: white;
    }

    #invalid-button:hover {
        background-color: #c0392b; /* Darker red */
         transform: translateY(-2px); /* Lift effect */
    }
    #invalid-button:active {
         transform: scale(0.98); /* Press effect */
     }


    /* Feedback Display */
    #feedback {
        margin-top: 20px;
        padding: 18px; /* More padding */
        min-height: 1.5em; /* Reserve space */
        text-align: right;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: bold;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly lower */
        animation: fadeInUp 0.5s ease-out forwards; /* Animation for feedback */
    }

    .feedback-correct {
        background-color: #e9f8ee; /* Very light green */
        border: 2px solid #2ecc71; /* Green border */
        color: #186a3b; /* Dark green text */
    }

    .feedback-incorrect {
        background-color: #fdedec; /* Very light red */
        border: 2px solid #e74c3c; /* Red border */
        color: #943126; /* Dark red text */
    }
     .feedback-info { /* For 'not applicable' cases */
        background-color: #ebf5fb; /* Very light blue */
        border: 2px solid #3498db; /* Blue border */
        color: #21618c; /* Dark blue text */
     }

    /* Next Button */
    #next-button {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 8px;
        background-color: #3498db; /* Peter River Blue */
        color: white;
        margin-top: 20px; /* More space */
        display: block;
        margin-left: auto;
        margin-right: auto;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #next-button:hover {
        background-color: #2980b9; /* Darker blue */
         transform: translateY(-2px); /* Lift effect */
    }
     #next-button:active {
         transform: scale(0.98); /* Press effect */
     }


    /* Explanation Section */
    #toggle-explanation {
        display: block;
        margin: 30px auto 20px auto; /* More vertical space */
        padding: 12px 20px;
        font-size: 1em;
        cursor: pointer;
        border: 1px solid #a0c3d2;
        border-radius: 8px;
        background-color: #eaf2f8; /* Light blue */
        color: #1a5276;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    #toggle-explanation:hover {
        background-color: #d6eaf8; /* Slightly darker blue */
        border-color: #3498db;
    }

    #explanation {
        border: 1px solid #a0c3d2;
        padding: 25px;
        max-width: 650px;
        margin: 20px auto;
        background-color: #f8f9f9; /* Very light gray */
        border-radius: 15px;
        text-align: right;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }

    #explanation h2 {
        color: #1a5276;
        border-bottom: 2px solid #3498db; /* Matching border */
        padding-bottom: 8px;
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.6em;
    }
     #explanation h3 {
        color: #21618c; /* Medium blue */
        border-bottom: 1px solid #a0c3d2;
        padding-bottom: 5px;
        margin-top: 20px;
        margin-bottom: 15px;
        font-size: 1.3em;
     }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Adjust for RTL */
        padding-right: 0;
        margin-bottom: 15px;
    }
     #explanation li {
        margin-bottom: 8px;
        padding-right: 0;
     }
      #explanation li::marker { /* Style for bullet points */
        color: #3498db;
     }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

     @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

     @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      10% { transform: translateX(-5px); }
      20% { transform: translateX(5px); }
      30% { transform: translateX(-5px); }
      40% { transform: translateX(5px); }
      50% { transform: translateX(-5px); }
      60% { transform: translateX(5px); }
      70% { transform: translateX(-5px); }
      80% { transform: translateX(5px); }
      90% { transform: translateX(-5px); }
    }

     /* Class to apply shake animation */
     .shake {
        animation: shake 0.8s;
     }

</style>

<script>
    const arguments = [
        {
            text: "כל בני האדם בני תמותה.\nסוקרטס הוא בן אדם.\nלכן, סוקרטס בן תמותה.",
            syllogismValid: true,
            propositionalValid: true,
            syllogismFeedback: "מעולה! זהו אכן סילוגיזם תקף לחלוטין מהצורה הקלאסית 'ברברה' (AAA-1). המסקנה נובעת באופן הכרחי מההנחות על פי כללי הסילוגיזם.",
            propositionalFeedback: "יופי! גם בלוגיקה מודרנית, טיעון זה תקף. אם תכונה X חלה על כל מי שמשתייך לקבוצה Y, וסוקרטס משתייך לקבוצה Y, אז תכונה X חלה על סוקרטס.",
            type: "standard-syllogism"
        },
        {
            text: "כל החתולים יונקים.\nחלק מהיונקים הם כלבים.\nלכן, חלק מהחתולים הם כלבים.",
            syllogismValid: false,
            propositionalValid: false,
            syllogismFeedback: "הממ... לא מדויק. זהו סילוגיזם *לא* תקף. יש כאן כשל נפוץ הנקרא 'אמצע בלתי מפוזר'. המושג האמצעי ('יונקים') לא 'מכסה' את כל הקבוצה בשתי ההנחות, ולכן אין גשר לוגי מחייב בין 'חתולים' ל'כלבים'.",
            propositionalFeedback: "צדקת, הטיעון לא תקף. העובדה שחלק מהיונקים הם כלבים לא אומרת שהיונקים שהם כלבים הם בהכרח גם החתולים. תיתכן חפיפה חלקית אחרת בין קבוצות היונקים, החתולים והכלבים.",
            type: "standard-syllogism"
        },
        {
            text: "שום דג אינו ציפור.\nכל הסלמונים הם דגים.\nלכן, שום סלמון אינו ציפור.",
            syllogismValid: true,
            propositionalValid: true,
            syllogismFeedback: "מצוין! זהו סילוגיזם תקף לחלוטין מהצורה 'קלרנט' (Celarent-1). אם להיות דג שולל מלהיות ציפור, ולהיות סלמון מחייב מלהיות דג, אז להיות סלמון שולל מלהיות ציפור.",
            propositionalFeedback: "נכון מאוד! הטיעון מחזיק גם בלוגיקה מודרנית.",
            type: "standard-syllogism"
        },
        {
            text: "חלק מהסטודנטים חכמים.\nחלק מהחכמים עשירים.\nלכן, חלק מהסטודנטים עשירים.",
            syllogismValid: false,
            propositionalValid: false,
            syllogismFeedback: "לא, זה אינו סילוגיזם תקף. בלוגיקה האריסטוטלית, סילוגיזם עם שתי הנחות 'חלקיות' (כמו 'חלק מ...') תמיד נחשב ללא תקף. שוב מדובר גם בכשל 'אמצע בלתי מפוזר'.",
            propositionalFeedback: "יפה! הטיעון אכן לא תקף. ייתכן שקבוצת הסטודנטים החכמים שונה מקבוצת החכמים העשירים, ואין חפיפה ביניהן.",
            type: "standard-syllogism"
        },
        // Propositional arguments start here
        {
            text: "אם יורד גשם, אז הרחוב רטוב.\nיורד גשם.\nלכן, הרחוב רטוב.",
            syllogismValid: 'n/a',
            propositionalValid: true,
            syllogismFeedback: "אהה, הנה האתגר! טיעון כזה, המבוסס על קשר 'אם-אז' בין משפטים שלמים ולא על יחסים בין קבוצות, אינו מתאים בקלות לניתוח בסילוגיזם האריסטוטלי הקלאסי. זה מראה את מגבלות השיטה הישנה.",
            propositionalFeedback: "נכון מאוד! זהו טיעון תקף בלוגיקה מודרנית, דוגמה קלאסית ל'מודוס פוננס'. אם A גורר B, ו-A נכון, אז B נכון - פשוט ויעיל!",
            type: "propositional"
        },
         {
            text: "ג'ון נמצא בבית או שהוא נמצא בספרייה.\nג'ון אינו נמצא בבית.\nלכן, ג'ון נמצא בספרייה.",
            syllogismValid: 'n/a',
            propositionalValid: true,
            syllogismFeedback: "שוב, טיעון כזה עם קשר 'או' ושלילה ('אינו') חורג ממבנה הסילוגיזם האריסטוטלי. הכלים של אריסטו פשוט לא נועדו לטפל בקשרים לוגיים מסוג זה בין פסוקים שלמים.",
            propositionalFeedback: "מצוין! זהו טיעון תקף בלוגיקה מודרנית, המכונה 'סילוגיזם דיסיונקטיבי'. אם אחת משתי אפשרויות נכונה (A או B), ואפשרות אחת (A) שגויה, אז השנייה (B) חייבת להיות נכונה.",
            type: "propositional"
        },
         {
            text: "אם יורד גשם, אז הרחוב רטוב.\nהרחוב רטוב.\nלכן, יורד גשם.",
            syllogismValid: 'n/a',
            propositionalValid: false,
            syllogismFeedback: "כמו קודם, טיעון 'אם-אז' כזה לא נכנס למסגרת הניתוח הסילוגיסטי התקנית.",
            propositionalFeedback: "לא נכון... היזהר מכשל! הטיעון הזה *אינו* תקף בלוגיקה מודרנית. זהו כשל נפוץ הנקרא 'אישור התוצאה'. רק בגלל שהתוצאה (הרחוב רטוב) נכונה, זה לא אומר שהתנאי המקורי (ירד גשם) חייב להיות הסיבה! ייתכן שהרחוב רטוב מהשקיה, לדוגמה.",
            type: "propositional"
        },
         {
            text: "יורד גשם וקר בחוץ.\nלכן, יורד גשם.",
            syllogismValid: 'n/a',
            propositionalValid: true,
            syllogismFeedback: "טיעון המבוסס על קשר 'וגם' (קוניונקציה) אינו טיפוסי לניתוח בסילוגיזם אריסטוטלי.",
            propositionalFeedback: "נכון! זהו טיעון תקף בלוגיקה מודרנית, המכונה 'סימפליפיקציה'. אם חיבור ב-'וגם' (A ו-B) נכון, אז כל אחד מהמרכיבים (A, ובמקרה זה 'יורד גשם') חייב להיות נכון.",
            type: "propositional"
        }
    ];

    const phase1Arguments = arguments.filter(arg => arg.type === "standard-syllogism");
    // Phase 2 includes propositional arguments and re-uses some syllogisms to highlight the difference in analysis
    const phase2Arguments = arguments.filter(arg => arg.type === "propositional").concat(arguments.filter(arg => arg.type === "standard-syllogism").slice(0, 2)); // Include first 2 syllogisms in phase 2 as well


    let currentPhase = 1; // 1: Syllogism, 2: Propositional Logic
    let currentArgumentIndex = 0;
    let currentArgumentList; // Will be set based on phase
    let score = 0;

    // Get elements
    const phaseTitle = document.getElementById('phase-title');
    const instructionDiv = document.getElementById('instruction');
    const argumentCard = document.getElementById('argument-card');
    const argumentDisplay = document.getElementById('argument-display');
    const validButton = document.getElementById('valid-button');
    const invalidButton = document.getElementById('invalid-button');
    const feedbackDiv = document.getElementById('feedback');
    const nextButton = document.getElementById('next-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const scoreDisplay = document.getElementById('current-score');
    const progressIndexDisplay = document.getElementById('current-arg-index');
    const totalArgsDisplay = document.getElementById('total-args');


    function startPhase(phaseNum) {
        currentPhase = phaseNum;
        currentArgumentIndex = 0;
        if (currentPhase === 1) {
            currentArgumentList = phase1Arguments;
            phaseTitle.innerText = 'שלב 1: בזירה האריסטוטלית (סילוגיזם)';
             instructionDiv.innerHTML = '<p>ברוכים הבאים לשלב הראשון! כאן נתנסה בניתוח טיעונים על פי הכללים הנוקשים של הסילוגיזם האריסטוטלי. מטרתכם: לקבוע האם המסקנה נובעת בהכרח מההנחות <strong>על פי כללי הסילוגיזם בלבד</strong>.</p><p class="note">(התעלמו בשלב זה מהאינטואיציה היומיומית. האם הטיעון תקף *סילוגיסטית*?)</p>';
             feedbackDiv.innerText = ''; // Clear feedback
             feedbackDiv.className = '';
             nextButton.style.display = 'none';
        } else { // Phase 2
            currentArgumentList = phase2Arguments;
            phaseTitle.innerText = 'שלב 2: המעבר ללוגיקה מודרנית (תחשיב פסוקים)';
            instructionDiv.innerHTML = '<p>יופי! עברנו למגרש המשחקים של הלוגיקה המודרנית - תחשיב הפסוקים. כאן ננתח טיעונים על בסיס קשרים לוגיים בין משפטים שלמים. מטרתכם: לקבוע האם הטיעון תקף <strong>על פי כללי הלוגיקה המודרנית</strong>.</p>';
            feedbackDiv.innerText = 'התחלת את שלב 2!'; // Clear feedback
             feedbackDiv.className = '';
             nextButton.style.display = 'none';
        }
         totalArgsDisplay.innerText = currentArgumentList.length;
        displayArgument();
    }

    function displayArgument() {
        if (currentArgumentIndex < currentArgumentList.length) {
            const arg = currentArgumentList[currentArgumentIndex];
            argumentDisplay.innerText = arg.text;
            feedbackDiv.innerText = '';
            feedbackDiv.className = ''; // Clear feedback class
            feedbackDiv.style.opacity = 0; // Hide feedback
            argumentCard.classList.remove('shake'); // Remove shake class
            nextButton.style.display = 'none';
            validButton.style.display = 'inline-block';
            invalidButton.style.display = 'inline-block';

            progressIndexDisplay.innerText = currentArgumentIndex + 1; // Update progress

        } else {
            endPhase();
        }
    }

    function checkAnswer(userAnswer) {
        const arg = currentArgumentList[currentArgumentIndex];
        let correctAnswer, feedbackText;
        let isCorrect = false;

        if (currentPhase === 1) {
            correctAnswer = arg.syllogismValid;
            if (correctAnswer === 'n/a') {
                 feedbackText = arg.syllogismFeedback;
                 feedbackDiv.className = 'feedback-info'; // Use info class for 'not applicable' feedback
                 // Do not change score for N/A in phase 1, but count as 'incorrect' interpretation of syllogism rules
                 isCorrect = false; // User couldn't apply syllogism rules correctly if they tried valid/invalid on an N/A
            } else if ((userAnswer === 'valid' && correctAnswer === true) || (userAnswer === 'invalid' && correctAnswer === false)) {
                feedbackText = "יופי! " + arg.syllogismFeedback;
                feedbackDiv.className = 'feedback-correct';
                isCorrect = true;
            } else {
                feedbackText = "הממ... לא מדויק. " + arg.syllogismFeedback;
                feedbackDiv.className = 'feedback-incorrect';
                isCorrect = false;
            }
        } else { // Phase 2 (Propositional Logic)
            correctAnswer = arg.propositionalValid;
             if ((userAnswer === 'valid' && correctAnswer === true) || (userAnswer === 'invalid' && correctAnswer === false)) {
                feedbackText = "מצוין! " + arg.propositionalFeedback;
                feedbackDiv.className = 'feedback-correct';
                 isCorrect = true;
            } else {
                feedbackText = "אופס! לא נכון. " + arg.propositionalFeedback;
                feedbackDiv.className = 'feedback-incorrect';
                 isCorrect = false;
            }
        }

        // Update score and provide visual feedback
        if (isCorrect) {
            score += 1;
            scoreDisplay.innerText = score;
        } else {
            // Optional: shake animation for incorrect answer
            argumentCard.classList.add('shake');
        }


        feedbackDiv.innerText = feedbackText;
        feedbackDiv.style.opacity = 1; // Show feedback with animation
        validButton.style.display = 'none';
        invalidButton.style.display = 'none';
        nextButton.style.display = 'block';
    }

    function nextArgument() {
        currentArgumentIndex++;
        if (currentArgumentIndex < currentArgumentList.length) {
            displayArgument();
        } else {
            endPhase();
        }
    }

    function endPhase() {
        if (currentPhase === 1) {
            // Transition to Phase 2
            feedbackDiv.innerText = `סיימת את שלב 1 עם ניקוד של ${score} מתוך ${phase1Arguments.length} נקודות. עכשיו נעבור לשלב 2: תחשיב הפסוקים!`;
            feedbackDiv.className = 'feedback-info'; // Use info style for phase transition message
            feedbackDiv.style.opacity = 1;
            nextButton.innerText = 'התחל שלב 2';
            nextButton.onclick = function() {
                 startPhase(2); // Start phase 2
                 nextButton.onclick = nextArgument; // Reset button action for subsequent arguments
            };
            nextButton.style.display = 'block'; // Make sure 'next' is visible to start phase 2
            validButton.style.display = 'none'; // Hide judgment buttons
            invalidButton.style.display = 'none';


        } else { // End of Phase 2 (End of Game)
            argumentDisplay.innerText = "סיימת את המסע! הניקוד הסופי שלך הוא " + score + ".";
             argumentCard.style.borderColor = '#2ecc71'; /* Green border for completion */
             argumentCard.style.boxShadow = '0 4px 8px rgba(46, 204, 113, 0.2)'; /* Green shadow */

            feedbackDiv.innerText = `מקווה שההתנסות עזרה לך להבין טוב יותר את ההבדלים והמעבר המשמעותי מהלוגיקה האריסטוטלית לתחשיב הפסוקים. כל הכבוד על ההשתתפות!`;
             feedbackDiv.className = 'feedback-correct'; /* Use correct style for final message */
             feedbackDiv.style.opacity = 1;

            validButton.style.display = 'none';
            invalidButton.style.display = 'none';
            nextButton.style.display = 'none';
            instructionDiv.style.display = 'none';
            phaseTitle.innerText = 'המסע הסתיים!';
             scoreDisplay.parentElement.style.display = 'none'; // Hide score area at the end
        }
    }

    // Event Listeners
    validButton.addEventListener('click', () => checkAnswer('valid'));
    invalidButton.addEventListener('click', () => checkAnswer('invalid'));
    nextButton.addEventListener('click', nextArgument);
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.innerText = 'הסתר מסע הרקע הלוגי';
             toggleExplanationButton.style.backgroundColor = '#d6eaf8'; /* Darker on open */
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.innerText = 'הצג/הסתר מסע הרקע הלוגי';
            toggleExplanationButton.style.backgroundColor = '#eaf2f8'; /* Light on close */
        }
    });

    // Initialize the game
    startPhase(1); // Start with phase 1

</script>