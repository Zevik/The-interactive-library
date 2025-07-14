---
title: "בונה ספינות בוונציה: סימולציה היסטורית"
english_slug: venetian-shipbuilder-historical-simulation
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags: [היסטוריה, ונציה, ימי-הביניים, סימולציה, משחק תפקידים, רנסנס, ארסנלה]
---
# בונה ספינות בוונציה: סימולציה היסטורית

שנת 1480, רפובליקת ונציה. אינך סוחר עשיר או דוכס יושב ארמון, אלא אומן עמל בלב הפועם של העיר - הארסנלה האדירה. אלפי בוני ספינות כמוך הופכים עצים גולמיים לעורק החיים של ונציה. האם תצליח לבנות את דרכך להצלחה, או שתטבע בים העבודה הקשה והאתגרים? שבוע אחד בארסנלה יקבע את גורלך.

<div id="game-container">
    <div id="stats">
        <div class="stat-item">יום: <span id="day"></span></div>
        <div class="stat-item">זמן: <span id="time"></span></div>
        <div class="stat-item">התקדמות ספינה: <span id="progress" data-stat="progress"></span>%</div>
        <div class="stat-item">איכות עבודה: <span id="quality" data-stat="quality"></span>%</div>
        <div class="stat-item">מצב רוח: <span id="mood" data-stat="mood"></span>%</div>
        <div class="stat-item">כסף: <span id="money" data-stat="money"></span> דוקטים</div>
    </div>
    <div id="game-area">
        <div id="scenario-text">טוען את קצב החיים בארסנלה...</div>
        <div id="choices">
            <!-- Choices will be loaded here -->
        </div>
    </div>
    <div id="message-area">
        <!-- Game messages will appear here -->
    </div>
     <div id="end-screen" style="display: none;">
        <h2>השבוע הסתיים!</h2>
        <div id="final-summary"></div>
        <div id="outcome-text"></div>
        <button id="restart-button">התחל שבוע חדש</button>
    </div>
</div>

<style>
    /* General Styles */
    #game-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 800px;
        margin: 20px auto;
        border: 1px solid #ccc;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        background-color: #fdfdfd; /* Softer white */
        border-radius: 10px;
        position: relative; /* For potential animations */
        overflow: hidden; /* Clean up potential overflows */
    }

    /* Stats Area */
    #stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
        gap: 15px;
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 2px solid #eee;
        color: #333;
    }

    .stat-item {
        background-color: #eef;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-size: 0.95em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

     .stat-item span {
        display: inline-block; /* Allows transform */
         margin-right: 5px;
         transition: color 0.4s ease, transform 0.2s ease; /* Animation for number change */
    }

     /* Animation for stat change */
    @keyframes stat-change-highlight {
        0% { color: inherit; transform: scale(1); }
        50% { color: #007bff; transform: scale(1.1); } /* Highlight color */
        100% { color: inherit; transform: scale(1); }
    }

     @keyframes stat-change-positive {
        0% { color: inherit; }
        50% { color: #28a745; transform: scale(1.1); } /* Green for positive */
        100% { color: inherit; transform: scale(1); }
    }

    @keyframes stat-change-negative {
        0% { color: inherit; }
        50% { color: #dc3545; transform: scale(1.1); } /* Red for negative */
        100% { color: inherit; transform: scale(1); }
    }


    /* Game Area */
    #game-area {
        margin-bottom: 25px;
        min-height: 150px; /* Ensure space */
        display: flex;
        flex-direction: column;
        justify-content: center; /* Center content vertically */
        align-items: center; /* Center content horizontally */
         text-align: center; /* Center text */
    }

    #scenario-text {
        font-size: 1.2em;
        margin-bottom: 20px;
        line-height: 1.6;
        color: #555;
        font-style: italic;
        min-height: 60px; /* Reserve space */
    }

    #choices {
        width: 100%;
    }

    #choices button {
        display: block;
        width: 100%;
        padding: 12px;
        margin-bottom: 12px;
        border: none;
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 1.05em;
        cursor: pointer;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        text-align: center; /* Ensure text is centered */
    }

    #choices button:hover:not(:disabled) {
        background-color: #45a049;
        transform: translateY(-2px);
    }

    #choices button:active:not(:disabled) {
         transform: translateY(0);
    }

    #choices button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.6;
        box-shadow: none;
    }

    /* Message Area */
    #message-area {
        margin-top: 20px;
        padding: 12px;
        background-color: #e9ecef; /* Light grey */
        border: 1px solid #ced4da;
        color: #495057;
        min-height: 1.5em; /* Ensure space even when empty */
        border-radius: 5px;
        font-size: 0.9em;
        opacity: 0; /* Start hidden */
        transition: opacity 0.5s ease-in-out;
    }

    #message-area.visible {
         opacity: 1;
    }

    /* Explanation Toggle Button */
    #toggleExplanation {
        display: block;
        width: fit-content;
        margin: 25px auto;
        padding: 12px 25px;
        background-color: #007bff; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    #toggleExplanation:hover {
         background-color: #0056b3;
         transform: translateY(-1px);
    }

     #toggleExplanation:active {
         transform: translateY(0);
     }

    /* Historical Explanation Area */
    #historicalExplanation {
        margin-top: 25px;
        padding: 20px;
        border: 1px solid #ddd;
        background-color: #f8f9fa; /* Very light grey */
        border-radius: 8px;
        color: #333;
        line-height: 1.7;
        transition: all 0.5s ease-in-out; /* Add transition for appearance */
    }

     #historicalExplanation.hidden {
         opacity: 0;
         max-height: 0;
         padding-top: 0;
         padding-bottom: 0;
         overflow: hidden;
     }

    #historicalExplanation h2, #historicalExplanation h3 {
        color: #007bff; /* Blue titles */
        margin-top: 20px;
        margin-bottom: 12px;
    }

    #historicalExplanation h2 {
        font-size: 1.8em;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }

    #historicalExplanation h3 {
         font-size: 1.4em;
    }

    #historicalExplanation p {
        margin-bottom: 15px;
        text-align: justify;
    }

     /* End Screen */
    #end-screen {
        text-align: center;
        padding: 30px 20px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        z-index: 10; /* Bring to front */
        margin-top: 20px; /* Add some space */
         opacity: 0; /* Start hidden */
        transform: translateY(20px);
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }

     #end-screen.visible {
         opacity: 1;
         transform: translateY(0);
     }


    #end-screen h2 {
        color: #28a745; /* Green success color */
        font-size: 2em;
        margin-bottom: 15px;
         animation: pulse 1.5s infinite alternate; /* Subtle pulse animation */
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.02); }
    }


    #final-summary {
        font-size: 1.1em;
        margin-bottom: 15px;
        color: #555;
    }

    #outcome-text {
        font-size: 1.2em;
        font-weight: bold;
        color: #333;
        min-height: 40px; /* Reserve space */
    }

    #restart-button {
        padding: 12px 25px;
        background-color: #007bff; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    #restart-button:hover {
         background-color: #0056b3;
         transform: translateY(-1px);
    }

     #restart-button:active {
         transform: translateY(0);
     }


</style>

<button id="toggleExplanation">הצג/הסתר רקע היסטורי</button>

<div id="historicalExplanation" class="hidden">
    <h2>רקע היסטורי על בוני ספינות בוונציה</h2>

    <h3>חשיבותה של ונציה כמעצמה ימית ומסחרית במאה ה-15</h3>
    <p>במאה ה-15, ונציה הייתה אחת מהרפובליקות הימיות החזקות והעשירות ביותר בים התיכון. מיקומה האסטרטגי כנקודת מפגש בין מזרח למערב, יחד עם הצי החזק והמיומן שלה, אפשרו לה לשלוט בנתיבי סחר ימיים ולהקים אימפריה ימית שהשתרעה ממזרח הים התיכון ועד צפון איטליה. המסחר במוצרי מותרות, תבלינים, טקסטיל וסחורות נוספות היה לב ליבה של כלכלת ונציה, והוא היה תלוי לחלוטין ביכולתה לבנות, לתחזק ולהפעיל צי גדול ויעיל של ספינות סוחר וספינות מלחמה.</p>

    <h3>הארסנלה (Arsenale) של ונציה: מבנה, ארגון ותפקיד כלכלי וצבאי</h3>
    <p>הארסנלה של ונציה הייתה המפעל התעשייתי המרכזי והגדול ביותר בימי הביניים ובראשית הרנסנס. זה היה למעשה מתחם ענק וסודי (למעט עובדיו) ששימש לבנייה, חימוש ותיקון של ספינות הצי הוונציאני. הארסנלה פעלה כמו סוג מוקדם של פס ייצור: חלקים שונים של הספינה יוצרו במקביל על ידי קבוצות שונות של בעלי מלאכה מומחים (נגרים, מסגרים, חבלנים, תופרי מפרשים ועוד), והספינות הורכבו באופן סדרתי. יעילות זו אפשרה לוונציה לבנות ספינה בקצב מסחרר יחסית (לפעמים תוך ימים בודדים בעת חירום). הארסנלה העסיקה אלפי עובדים והייתה עמוד תווך בכלכלה ובהגנה של הרפובליקה.</p>

    <h3>חיי היומיום של בעלי מלאכה בארסנלה: תנאי עבודה, שכר, ומעמד חברתי</h3>
    <p>בוני הספינות ועובדי הארסנלה האחרים, הידועים כ"ארסנלוטי" (Arsenalotti), היו קבוצה מקצועית מכובדת. תנאי העבודה היו קשים פיזית, שעות העבודה היו ארוכות, והסיכונים הבטיחותיים היו גבוהים. למרות זאת, עובדי הארסנלה נהנו ממעמד מיוחד: הם קיבלו שכר יציב (לרוב יומי או שבועי), נהנו מהטבות מסוימות, והיו מאורגנים בגילדות חזקות שהגנו על זכויותיהם. הם היו נאמנים לרפובליקה ולעתים קרובות גויסו גם לכוח שמירת הסדר בוונציה עצמה. העבודה בארסנלה סיפקה ביטחון כלכלי יחסי בתקופה שבה רוב האוכלוסייה נאבקה על קיומה.</p>

    <h3>מבנה הספינות הוונציאניות (למשל, הגליאה) ותהליך הבנייה</h3>
    <p>הספינה האייקונית ביותר של ונציה הייתה הגליאה (Galley) - ספינת משוטים ארוכה וצרה, מצוידת גם במפרשים, ששימשה הן למסחר (גליאת סוחר) והן למלחמה (גליאת מלחמה). בניית הגליאה הייתה תהליך מורכב שדרש מומחיות רבה. ראשית, נבנה השלד (קיל, צלעות). לאחר מכן הותקנו לוחות העץ החיצוניים (הציפוי). במקביל, יוצרו התרנים, הסיפונים, התרנים, המפרשים, החבלים וההגאים. בארסנלה, חלקים אלו יוצרו מראש בכמויות גדולות ואוכסנו במחסנים ענקיים (Cordage House, Sail House ועוד), מוכנים להרכבה מהירה. בניית גליאה דרשה תיאום בין מאות בעלי מלאכה שונים.</p>

    <h3>האתגרים וההזדמנויות במקצוע בונה הספינות</h3>
    <p>האתגרים כללו את הקושי הפיזי של העבודה עם עץ וחומרים כבדים, הסכנות הבטיחותיות (נפילה, פציעה מכלים, שריפות), הצורך לעמוד בלחצי זמן כשהרפובליקה נזקקה לספינות במהירות (בעיקר בעת מלחמה), והצורך לבצע עבודה מדויקת ואיכותית כדי להבטיח שהספינה תהיה יציבה ועמידה בים. ההזדמנויות כללו ביטחון תעסוקתי, שכר יציב יחסית, יוקרה מסוימת הנובעת מהחשיבות האסטרטגית של מקצועם, ואפשרות להתקדם בתוך ההיררכיה של הארסנלה.</p>

    <h3>השוואה בין עבודה בארסנלה למודלים ארגוניים מודרניים (פס ייצור, תעשייה)</h3>
    <p>הארסנלה נחשבת לעיתים קרובות למבשרת המודרנית של פס הייצור והמפעל התעשייתי. בדומה לפס ייצור, היא השתמשה בייצור חלקים סטנדרטיים מראש, התמחות של עובדים במשימות ספציפיות, ותהליך הרכבה סדרתי. עם זאת, היו הבדלים מהותיים: העבודה הייתה ידנית לחלוטין, ללא שימוש במכונות מורכבות (מעבר למנופים פשוטים), וההיקף אמנם היה גדול במונחי התקופה, אך לא דומה למפעלי התעשייה המודרנית. כמו כן, היחסים בין העובדים למעסיק (הרפובליקה) היו שונים, עם דגש רב יותר על גילדות ומבנים חברתיים מסורתיים.</p>
</div>

<script>
    const state = {
        day: 1,
        timeIndex: 0,
        money: 50,
        progress: 0,
        quality: 75, // Starting quality
        mood: 75, // Starting mood
        scenariosCompleted: 0
    };

    const timeLabels = ["בוקר מוקדם", "אמצע היום", "שלהי אחר הצהריים"]; // 3 time slots per day
    const totalDays = 5; // Total days in the week simulation

    const scenarios = [
        // Day 1
        { day: 1, time: "בוקר מוקדם", text: "שחר עולה מעל לגגות הארסנלה הענקית. ריח עץ טרי ומלח באוויר. עוד יום של עמל מתחיל. איך אתה פותח אותו?", choices: [
            { text: "מתייצב מוקדם ועובר מיד לעבודה קשה", effects: { progress: 15, quality: 2, mood: -10, money: 0 }, message: "התחלה נמרצת! גופך עייף קמעה אך העבודה מתקדמת בקצב מרשים." },
            { text: "מגיע בזמן, מתארגן בנחת ומתחיל בקצב רגיל", effects: { progress: 10, quality: 5, mood: 0, money: 0 }, message: "יום עבודה סטנדרטי לבונה ספינות ותיק מתחיל. הכל זורם כרגיל." },
            { text: "מאחר מעט, מוצא זמן לקפה ומילה עם חברים לפני שמתחיל ברצינות", effects: { progress: 5, quality: -5, mood: 5, money: -2 }, message: "הגעת מאוחר. המנהל רשם הערה חמורה. חלק משכרך היומי קוזז. אך מצב רוחך מרומם יותר." }
        ]},
        { day: 1, time: "אמצע היום", text: "אתה עובד על קיבוע לוחות הציפוי לגוף הספינה. האם עליך להתמקד במהירות כדי לעמוד בזמנים, או בדקדקנות מירבית להבטחת אטימה מושלמת?", choices: [
            { text: "ממהר לסיים את הלוחות, 'יהיה בסדר'", effects: { progress: 12, quality: -8, mood: 0, money: 0 }, message: "הציפוי מתקדם מהר, אך אתה חושש שיש פערים קטנים שיצטרכו תיקון אחר כך. האיכות נפגעת." },
            { text: "משקיע זמן רב בכל לוח, בודק ומוודא אטימה הרמטית", effects: { progress: 8, quality: 10, mood: 5, money: 0 }, message: "העבודה איטית יותר, אך כל לוח יושב במקומו באופן מושלם. הספינה תהיה יציבה וחזקה להפליא." }
        ]},
         { day: 1, time: "שלהי אחר הצהריים", text: "עמית לעבודה, פייטרו שמו, מתקשה להרים קורה כבדה במיוחד לבדו. גבו נראה כפוף תחת המאמץ. הוא זקוק לעזרה.", choices: [
            { text: "ניגש מיד לעזור לו, גם אם זה פוגע בהתקדמות האישית שלך", effects: { progress: -5, quality: 0, mood: 10, money: 0 }, message: "עזרת לפייטרו להרים את הקורה. הוא מודה לך בחום. איבדת זמן עבודה אך רכשת חבר ומצב רוחך השתפר." },
            { text: "מתנצל ואומר שאתה חייב להתמקד במשימה שלך כדי לעמוד בלוח זמנים", effects: { progress: 5, quality: 0, mood: -5, money: 0 }, message: "התקדמת בעבודה שלך, אך פייטרו נראה מאוכזב ואתה חש אי נוחות קלה." }
        ]},
        // Day 2
        { day: 2, time: "בוקר מוקדם", text: "התחיל יום שני. אתה מרגיש את עייפות היום הראשון בשרירים. איך תתמודד עם ההתחלה?", choices: [
            { text: "קונה קפה שחור חזק ממריה הזקנה בפינה ומתחיל במרץ שיא", effects: { progress: 13, quality: 3, mood: -8, money: -1 }, message: "הקפה עזר, אך הוא מותיר אותך מעט עצבני. העבודה מהירה אך יש סיכוי קל לטעויות קטנות." },
            { text: "מתחיל לאט יותר, מחמם את השרירים ומתארגן בהדרגה", effects: { progress: 8, quality: 5, mood: 5, money: 0 }, message: "התחלה נינוחה. הגוף נכנס לקצב בהדרגה, מה שמבטיח דיוק רב יותר ומצב רוח טוב." }
        ]},
         { day: 2, time: "אמצע היום", text: "אחד ממנהלי העבודה, בעל המוניטין המחמיר ביותר, עובר בסדנה שלך ומסתכל על העבודה שביצעת על הציפוי.", choices: [
            { text: "מציג לו את ההתקדמות בביטחון, מדגיש את האיכות והדיוק", effects: { progress: 0, quality: 5, mood: 5, money: 1 }, message: "מנהל העבודה בוחן את הציפוי, מהנהן בשביעות רצון ומציין לשבח את עבודתך. קיבלת בונוס קטן על המאמץ." },
            { text: "ממשיך לעבוד כרגיל, מנסה לא למשוך תשומת לב מיוחדת", effects: { progress: 0, quality: 0, mood: -3, money: 0 }, message: "מנהל העבודה עבר לידך בלי להקדיש מבט מיוחד. הוא לא העיר, אבל גם לא שיבח. אתה חש הקלה קלה לצד תחושת פספוס." }
        ]},
        { day: 2, time: "שלהי אחר הצהריים", text: "היום כמעט נגמר. האם אתה דוחף קדימה בכל הכוח כדי לסיים משימה חשובה, או שומר אנרגיה למחר?", choices: [
            { text: "עובד עד הרגע האחרון, מותש אך נחוש", effects: { progress: 8, quality: -3, mood: -10, money: 0 }, message: "סיימת משימה משמעותית, אך אתה מותש לחלוטין והדבר עלול להשפיע על מחר. האיכות נפגעה מעט בלחץ." },
            { text: "אוסף את הכלים קצת מוקדם, מנקה את סביבת העבודה ויוצא לדרכך", effects: { progress: -3, quality: 2, mood: 8, money: 0 }, message: "התקדמת פחות היום, אבל תגיע לעבודה מחר רענן ואנרגטי. יש זמן לנקות ולשמור על הכלים, מה שמשפיע לטובה על איכות העבודה הכללית." }
        ]},
        // Day 3
        { day: 3, time: "בוקר מוקדם", text: "יום שלישי. המשימה היא התקנת הסיפון הראשי. זו עבודה שדורשת דיוק רב בגובה.", choices: [
            { text: "עובד בזהירות מירבית, כל לוח סיפון מונח במקומו המושלם", effects: { progress: 8, quality: 10, mood: 5, money: 0 }, message: "הסיפון יוצא איתן, ישר ויפהפה. עבודה של אומן אמיתי! מצב רוחך משתפר מגאוות יצירה." },
            { text: "מניח את הלוחות בקצב מהיר, דוחף קדימה כדי להספיק כמה שיותר", effects: { progress: 12, quality: -7, mood: -3, money: 0 }, message: "הסיפון הונח במהירות, אך ישנם פערים קטנים ועץ שדורש ליטוש רב יותר. האיכות נפגעת והעבודה פחות מספקת." }
        ]},
         { day: 3, time: "אמצע היום", text: "שמועות רצות בארסנלה על התגברות המתיחות עם אימפריה ימית יריבה. יש לחץ גובר לסיים ספינות בהקדם האפשרי.", choices: [
            { text: "נלחץ מהשמועות ומנסה להגביר קצב באופן דרמטי", effects: { progress: 15, quality: -10, mood: -10, money: 0 }, message: "הלחץ משפיע לרעה. העבודה מהירה בטירוף אך מלאה בטעויות קטנות ופספוסים. אתה מתוח ועצבני כל הזמן." },
            { text: "שומר על קור רוח ומתמקד בעבודה איכותית למרות הלחץ באוויר", effects: { progress: 8, quality: 8, mood: 5, money: 0 }, message: "אתה שומר על רמת עבודה גבוהה ודיוק, מבין שזו הדרך הנכונה לבנות ספינה עמידה. הלחץ פחות משפיע עליך אישית." }
        ]},
        { day: 3, time: "שלהי אחר הצהריים", text: "קיבלת מקדמה על שכרך השבועי. יש לך הזדמנות לקנות חומרים איכותיים יותר בשוק הסמוך (עץ מיוחד, מסמרים טובים יותר) שיקלו על העבודה או ישפרו את איכותה. זה יעלה לך 10 דוקטים.", choices: [
            { text: "משקיע 10 דוקטים בחומרים מעולים", effects: { progress: 5, quality: 15, mood: 10, money: -10 }, message: "החומרים האיכותיים מקלים פלאים על העבודה והתוצאה הסופית נראית נהדר. הארנק נפגע קשות אך שביעות רצונך מהתוצר עולה." },
            { text: "שומר את הכסף, משתמש בחומרים הרגילים שמספקת הארסנלה", effects: { progress: 7, quality: 3, mood: 0, money: 0 }, message: "עבודה רגילה עם חומרים רגילים. לא נעים במיוחד, לא קשה במיוחד. הכסף נשאר איתך." }
        ]},
        // Day 4
        { day: 4, time: "בוקר מוקדם", text: "אתה עובד על התקנת התרנים הראשיים. זו משימה גבוהה, מסוכנת ודורשת כוח ומיומנות.", choices: [
            { text: "עובד בזהירות מירבית, בודק כל קשר, חבל ותמיכה פעמיים", effects: { progress: 7, quality: 10, mood: 5, money: 0 }, message: "התרנים עומדים יציבים ובטוחים כמו סלעים. מרגישים הקלה גדולה בידיעה שהעבודה בוצעה באופן מושלם." },
            { text: "ממהר לסיים את התקנת התרנים כדי לעבור למשימות קלות יותר על הסיפון", effects: { progress: 10, quality: -8, mood: -5, money: 0 }, message: "התרנים הותקנו במהירות שיא, אך יש תחושת אי נוחות קלה לגבי יציבותם. סיכון קטן עשוי להיות כרוך בכך." }
        ]},
        { day: 4, time: "אמצע היום", text: "שעת הצהריים. אתם יכולים לנוח היטב בצל ולאכול ארוחה מלאה (תעלה 2 דוקטים), או לנשנש משהו קטן ולהמשיך לעבוד כדי לצמצם פערים?", choices: [
            { text: "אוכל ארוחה טובה ונח היטב בצל", effects: { progress: -3, quality: 0, mood: 15, money: -2 }, message: "אתה מרגיש מחודש, אנרגטי ומלא כוח להמשך היום. שווה כל דוקט." },
            { text: "מנשנש חטיף קטן ליד כלי העבודה וממשיך לעבוד", effects: { progress: 5, quality: -2, mood: -10, money: 0 }, message: "התקדמת בעבודה כשכולם נחים, אך אתה רעב, עייף ומצב רוחך ירוד. האיכות נפגעת מעט מחוסר ריכוז." }
        ]},
        { day: 4, time: "שלהי אחר הצהריים", text: "סנאטור מכובד, לבוש בגלימות ארגמן, מגיע לסיור בארסנלה ומגיע לסדנה שלך. האם תנסה למשוך את תשומת ליבו?", choices: [
            { text: "מציג לו בהתלהבות ועם גאוות יחידה את העבודה האיכותית שעשית על הספינה", effects: { progress: 0, quality: 5, mood: 8, money: 3 }, message: "הסנאטור התרשם מאוד מהמקצועיות שלך ומהאיכות שהצגת. הוא השאיר טיפ קטן ושם לב לשמך. המוניטין שלך בארסנלה עולה." },
            { text: "מתעלם וממשיך לעבוד כרגיל כאילו הוא לא קיים", effects: { progress: 0, quality: 0, mood: 0, money: 0 }, message: "הסנאטור עבר לידך בלי לשים לב. עבודה כרגיל. לא הרווחת דבר, אך גם לא איבדת." }
        ]},
        // Day 5
        { day: 5, time: "בוקר מוקדם", text: "היום האחרון בשבוע העבודה! הספינה כמעט מוכנה להשקה. המשימות האחרונות כוללות ליטושים עדינים והתקנת אביזרים קטנים.", choices: [
            { text: "עובד בקצב שיא, ממהר לסיים הכל לפני הצהריים", effects: { progress: 15, quality: -5, mood: -5, money: 0 }, message: "סיימת במהירות מדהימה, אך כנראה שפספסת כמה פרטים קטנים באיכות העבודה. אתה מותש לקראת סיום היום." },
            { text: "משקיע את הזמן בפרטים הקטנים, מוודא שהכל מושלם למרות שהקצב איטי יותר", effects: { progress: 10, quality: 10, mood: 5, money: 0 }, message: "העבודה איטית יותר, אך הספינה נראית ומרגישה מושלמת לפרטי פרטיה. שביעות רצונך עצומה." }
        ]},
         { day: 5, time: "אמצע היום", text: "שוליית בונה ספינות חדש וצעיר מגיע ושואל שאלות רבות, חלקן נשמעות לך טיפשיות. האם יש לך סבלנות ללמד אותו?", choices: [
            { text: "מקדיש לו זמן, מסביר ומדגים בסבלנות", effects: { progress: -5, quality: 0, mood: 10, money: 0 }, message: "השוליה למד ממך שיעור חשוב. מרגיש טוב שעזרת למשיהדור הבא של בוני הספינות. איבדת מעט זמן עבודה." },
            { text: "גוער בו ואומר לו לחזור לעבודה ולהפסיק להפריע", effects: { progress: 3, quality: 0, mood: -8, money: 0 }, message: "השוליה התרחק מפוחד. התקדמת מעט בעבודה ללא הפרעה, אבל אתה מרגיש קצת רע עם עצמך." }
        ]},
        { day: 5, time: "שלהי אחר הצהריים", text: "השבוע הסתיים! הספינה כמעט מוכנה להשקה הטקסית. הגיע הזמן לאסוף את כלי העבודה, לקבל את יתרת השכר וללכת הביתה.", choices: [
             { text: "אוסף כלי עבודה ויוצא משערי הארסנלה", effects: { progress: 0, quality: 0, mood: 5, money: 5 }, message: "סיים את שבוע העבודה בארסנלה!" } // End scenario
        ]}
    ];

    const dayLabels = ["ראשון", "שני", "שלישי", "רביעי", "חמישי"];


    // Function to update the display and add animation effects
    function updateDisplay(oldState = {}) {
        document.getElementById('day').textContent = dayLabels[state.day - 1];
        document.getElementById('time').textContent = timeLabels[state.timeIndex];

        // Animate stat changes
        animateStatChange('progress', oldState.progress, state.progress);
        animateStatChange('quality', oldState.quality, state.quality);
        animateStatChange('mood', oldState.mood, state.mood);
        animateStatChange('money', oldState.money, state.money);
    }

     function animateStatChange(statId, oldValue, newValue) {
        const element = document.getElementById(statId);
        if (!element) return;

        const clampedNewValue = Math.max(0, Math.min(100, newValue)); // Clamp for display
        element.textContent = (statId === 'money' ? clampedNewValue.toFixed(0) : clampedNewValue.toFixed(0)); // Display clamped value

        if (oldValue !== undefined && oldValue !== newValue) {
            const animationClass = newValue > oldValue ? 'stat-change-positive' : 'stat-change-negative';
            element.style.animation = 'none'; // Reset animation
            void element.offsetWidth; // Trigger reflow
            element.style.animation = `${animationClass} 0.6s ease-out`;

             // Remove animation class after animation ends
            const onAnimationEnd = () => {
                element.style.animation = '';
                element.removeEventListener('animationend', onAnimationEnd);
            };
            element.addEventListener('animationend', onAnimationEnd);
        }
    }


    function displayScenario(scenario) {
         // Hide end screen if visible
         document.getElementById('end-screen').classList.remove('visible');
         document.getElementById('end-screen').style.display = 'none';

         // Ensure game area is visible
         document.getElementById('game-area').style.display = 'flex';

        document.getElementById('scenario-text').textContent = scenario.text;
        const choicesDiv = document.getElementById('choices');
        choicesDiv.innerHTML = ''; // Clear previous choices

        scenario.choices.forEach(choice => {
            const button = document.createElement('button');
            button.textContent = choice.text;
            button.onclick = () => handleChoice(choice);
            choicesDiv.appendChild(button);
        });

        const messageArea = document.getElementById('message-area');
        messageArea.textContent = ''; // Clear message area
        messageArea.classList.remove('visible'); // Hide message area initially
    }

    function handleChoice(choice) {
        // Store old state for animation comparison
        const oldState = {...state};

        // Apply effects
        state.money += choice.effects.money || 0;
        state.progress += choice.effects.progress || 0;
        state.quality += choice.effects.quality || 0;
        state.mood += choice.effects.mood || 0;

        // Clamp stats within reasonable bounds (0-100 for quality/mood/progress, money can be negative but clamped for display)
        state.progress = Math.max(0, Math.min(100, state.progress));
        state.quality = Math.max(0, Math.min(100, state.quality));
        state.mood = Math.max(0, Math.min(100, state.mood));
        state.money = Math.max(0, state.money); // Don't allow negative money for simplicity, maybe change later? Let's allow negative, but display clamped. No, original didn't clamp money. Let's keep it unclamped in state, but clamp progress/quality/mood on display.

        // Update display with potentially old values first to see change, then update
        updateDisplay(oldState); // Pass old state to animation function


        // Display message
        const messageArea = document.getElementById('message-area');
        if (choice.message) {
            messageArea.textContent = choice.message;
            messageArea.classList.add('visible'); // Make message area visible with transition
        } else {
             messageArea.classList.remove('visible');
        }


        // Disable buttons until next scenario loads
        document.querySelectorAll('#choices button').forEach(btn => btn.disabled = true);

        // Move to next scenario after a short delay
        setTimeout(nextScenario, 2000); // Wait 2 seconds before next event
    }

    function nextScenario() {
        state.scenariosCompleted++;

         // Hide message area as we transition
         document.getElementById('message-area').classList.remove('visible');

        // Check if game is over (completed all scenarios)
        if (state.scenariosCompleted >= scenarios.length) {
            endGame();
            return;
        }

        // Advance time/day
        state.timeIndex++;
        if (state.timeIndex >= timeLabels.length) {
            state.timeIndex = 0;
            state.day++;
        }

        // Find the next scenario for the current scenario index
        const nextScen = scenarios[state.scenariosCompleted]; // Assuming scenarios are ordered chronologically

        if (nextScen) {
             updateDisplay({...state}); // Update time/day display immediately
             displayScenario(nextScen);

        } else {
            // Should not happen if scenarios array is built correctly
            endGame();
        }
    }

    function endGame() {
        document.getElementById('game-area').style.display = 'none'; // Hide game area
        document.getElementById('message-area').classList.remove('visible'); // Ensure message area is hidden

        const endScreen = document.getElementById('end-screen');
        endScreen.style.display = 'block'; // Make end screen visible
        endScreen.classList.add('visible'); // Trigger fade-in animation

        const finalSummary = document.getElementById('final-summary');
        finalSummary.innerHTML = `סיכום סופי לשבוע עמל בארסנלה:<br>
                                התקדמות בניית ספינה: <span class="stat-value">${Math.max(0, Math.min(100, state.progress)).toFixed(0)}%</span>,
                                איכות עבודה כוללת: <span class="stat-value">${Math.max(0, Math.min(100, state.quality)).toFixed(0)}%</span>,
                                מצב רוח אישי: <span class="stat-value">${Math.max(0, Math.min(100, state.mood)).toFixed(0)}%</span>,
                                רווח/הפסד כספי: <span class="stat-value">${state.money.toFixed(0)}</span> דוקטים.`;

        const outcomeText = document.getElementById('outcome-text');
        let outcome = "שרדת את השבוע כבונה ספינות בוונציה!";

        // More nuanced outcomes based on combined stats
        if (state.quality < 50 && state.progress < 50) {
            outcome = "העבודה שלך לא עמדה בסטנדרטים הנדרשים בארסנלה. עתידך כאן בסכנה.";
            outcomeText.style.color = '#dc3545'; // Red for poor outcome
             document.querySelector('#end-screen h2').style.color = '#dc3545';
        } else if (state.quality < 60 || state.progress < 60) {
            outcome = "סיימת את השבוע, אך ההתקדמות או האיכות אינן מספיקות. עליך להשתפר.";
             outcomeText.style.color = '#ffc107'; // Yellow for mediocre outcome
              document.querySelector('#end-screen h2').style.color = '#ffc107';
               document.querySelector('#end-screen h2').style.animation = 'none'; // Remove pulse for non-great outcome
        } else if (state.mood < 40 && state.money < 30) {
             outcome = "שרדת, אך במחיר אישי גבוה. אתה מותש, מרושש, ומדוכא. האם זה שווה את זה?";
              outcomeText.style.color = '#6c757d'; // Grey for survival outcome
               document.querySelector('#end-screen h2').style.color = '#6c757d';
                document.querySelector('#end-screen h2').style.animation = 'none';
        } else if (state.quality > 85 && state.progress > 85 && state.money > 70 && state.mood > 70) {
             outcome = "הצלחת לשרוד ואף לשגשג מעבר למצופה! היית בונה ספינות מוכשר, יעיל, מאושר ועשיר יחסית. מקומך מובטח בארסנלה!";
             outcomeText.style.color = '#28a745'; // Green for excellent outcome
             document.querySelector('#end-screen h2').style.color = '#28a745'; // Keep green pulse
        } else {
             outcome = "סיימת את השבוע בצורה סבירה. עבודה קשה, אתגרים אישיים, אך הצלחת לשרוד באחד המפעלים הגדולים בעולם.";
             outcomeText.style.color = '#17a2b8'; // Teal for average outcome
              document.querySelector('#end-screen h2').style.color = '#17a2b8';
               document.querySelector('#end-screen h2').style.animation = 'none';
        }

        outcomeText.textContent = outcome;

         document.getElementById('restart-button').onclick = restartGame;
    }

    function restartGame() {
         // Reset state
         state.day = 1;
         state.timeIndex = 0;
         state.money = 50;
         state.progress = 0;
         state.quality = 75;
         state.mood = 75;
         state.scenariosCompleted = 0;

         // Hide end screen with animation
         const endScreen = document.getElementById('end-screen');
         endScreen.classList.remove('visible');
         // Wait for animation before hiding completely and showing game area
         setTimeout(() => {
             endScreen.style.display = 'none';
             // Clear end game content
             document.getElementById('final-summary').innerHTML = '';
             document.getElementById('outcome-text').textContent = '';

             // Show game area
             document.getElementById('game-area').style.display = 'flex';

             // Restart the game flow
             startGame();
         }, 600); // Match CSS transition duration
    }

    function startGame() {
        updateDisplay();
        displayScenario(scenarios[state.scenariosCompleted]);
    }

    // Toggle explanation visibility
    document.getElementById('toggleExplanation').onclick = function() {
        const explanationDiv = document.getElementById('historicalExplanation');
        const isHidden = explanationDiv.classList.toggle('hidden'); // Toggle class
        this.textContent = isHidden ? 'הצג/הסתר רקע היסטורי' : 'הסתר רקע היסטורי';
    }

    // Initialize the game on page load
    window.onload = startGame;

</script>