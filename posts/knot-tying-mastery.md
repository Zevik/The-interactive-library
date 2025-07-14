---
title: "אמנות הקשרים: שליטה בחבל להצלה ולהצלחה"
english_slug: knot-tying-mastery
category: "כללי"
tags:
  - קשרים
  - חבל
  - הישרדות
  - מחנאות
  - בטיחות
  - מיומנות
---
# אמנות הקשרים: שליטה בחבל להצלה ולהצלחה

האם אי פעם מצאתם את עצמכם מול חבל, ולא הייתם בטוחים איך לקשור את הקשר הנכון למשימה? קשירה נכונה היא לא רק עניין טכני, היא אמנות עתיקה ומיומנות הישרדות בסיסית שיכולה להיות קריטית במגוון תרחישים – מטיפוס הרים, דרך שיט, ועד סתם תליית ערסל בבטחה. מה הופך קשר אחד לחזק ואמין תחת לחץ, ואחר לחסר תועלת או אף מסוכן? ואיך תוכלו לרכוש את הידע והביטחון הדרושים כדי לשלוט באומנות הזו בעצמכם? צללו לתוך הסימולציה האינטראקטיבית שלנו והתחילו לתרגל!

<div id="knot-app-container">
    <h2 class="app-title">תרגלו קשירת קשרים בעצמכם</h2>
    <label for="knot-selector" class="selector-label">בחרו קשר לתרגול:</label>
    <select id="knot-selector" class="custom-select">
        <option value="figure-eight">קשר שמינית (Figure Eight)</option>
        <option value="bowline">קשר בוולין (Bowline)</option>
        <option value="square">קשר רבוע (Square Knot)</option>
    </select>
    <div id="knot-display">
        <!-- SVG rendering area - will be dynamically populated and animated -->
        <svg id="rope-svg" width="400" height="300" viewBox="0 0 400 300"></svg>
        <div id="step-counter">שלב 1 / X</div>
    </div>
    <div id="instructions">בחרו קשר מהרשימה כדי להתחיל במסע שלכם לשליטה בחבלים!</div>
    <div id="controls">
        <button id="prev-step" class="control-button" disabled>שלב קודם</button>
        <button id="next-step" class="control-button">השלב הבא</button>
        <button id="reset-knot" class="control-button secondary">התחל מחדש</button>
    </div>
</div>

<style>
    /* Global App Styling */
    #knot-app-container {
        direction: rtl;
        text-align: right;
        font-family: 'Heebo', sans-serif; /* Using a more modern Hebrew-friendly font */
        max-width: 650px; /* Slightly wider container */
        margin: 30px auto;
        padding: 25px;
        border: none; /* Remove default border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* Clean white background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        position: relative;
        overflow: hidden; /* Ensure nothing spills out */
        transition: all 0.3s ease;
    }

    #knot-app-container::before { /* Background gradient or pattern */
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, #eef2f7 0%, #e0eafc 100%); /* Soft gradient */
        z-index: -1; /* Behind content */
        opacity: 0.8;
    }

    .app-title {
        text-align: center;
        color: #2c3e50; /* Darker, more professional color */
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    .selector-label {
        display: block;
        text-align: center;
        margin-bottom: 10px;
        color: #34495e;
        font-size: 1.1rem;
    }

    .custom-select {
        display: block;
        margin: 0 auto 25px auto;
        padding: 10px 15px;
        font-size: 1.1rem;
        border: 1px solid #bdc3c7;
        border-radius: 6px;
        background-color: #ecf0f1; /* Light grey background */
        color: #34495e;
        cursor: pointer;
        outline: none;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        appearance: none; /* Remove default select styling */
        background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2334495e%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E'); /* Custom arrow */
        background-repeat: no-repeat;
        background-position: calc(100% - 15px) center;
        background-size: 12px;
        padding-right: 35px; /* Make space for arrow */
    }
     .custom-select:hover {
        border-color: #95a5a6;
     }
    .custom-select:focus {
        border-color: #3498db;
        box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
    }


    #knot-display {
        width: 100%;
        height: 350px; /* Slightly taller display area */
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05); /* Inner shadow for depth */
    }

    #rope-svg {
        width: 95%; /* Allow some padding */
        height: 95%; /* Allow some padding */
        display: block;
        /* Preserve aspect ratio and center */
        viewBox: 0 0 400 300; /* Keep viewBox from original */
        preserveAspectRatio="xMidYMid meet";
    }

    /* Enhanced Rope Styling for SVG */
    .rope-part {
        stroke: #8B4513; /* SaddleBrown for classic rope look */
        stroke-width: 10; /* Thicker rope */
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
        transition: stroke-dashoffset 0.5s ease-in-out, opacity 0.3s ease-out; /* Animation for drawing */
        stroke-dasharray: 1000; /* Long dash array for drawing effect */
        stroke-dashoffset: 0; /* Start fully visible */
    }
    .working-end {
        stroke: #e74c3c; /* Reddish color to highlight the active part */
        stroke-width: 10;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
        transition: stroke-dashoffset 0.5s ease-in-out, opacity 0.3s ease-out;
        stroke-dasharray: 1000;
        stroke-dashoffset: 0;
    }
    .fixed-part {
         stroke: #3498db; /* Blueish color for the static part */
         stroke-width: 10;
         fill: none;
         stroke-linecap: round;
         stroke-linejoin: round;
         transition: stroke-dashoffset 0.5s ease-in-out, opacity 0.3s ease-out;
         stroke-dasharray: 1000;
         stroke-dashoffset: 0;
    }


    #step-counter {
        position: absolute;
        top: 10px;
        left: 10px;
        background-color: rgba(0, 0, 0, 0.5);
        color: white;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 0.9rem;
        z-index: 10; /* Above SVG */
    }

    #instructions {
        text-align: center;
        margin-bottom: 20px;
        padding: 15px;
        background-color: #ecf0f1; /* Light background */
        border-radius: 6px;
        min-height: 50px; /* More vertical space */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        color: #2c3e50;
        line-height: 1.5;
        border: 1px solid #bdc3c7;
    }

    #controls {
        text-align: center;
    }

    .control-button {
        padding: 12px 20px; /* Larger buttons */
        margin: 0 8px; /* More spacing */
        font-size: 1.1rem;
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 600;
        min-width: 120px; /* Ensure uniform width */
    }

    .control-button:not(:disabled) {
        background-color: #3498db; /* Primary blue */
    }

    .control-button.secondary {
        background-color: #95a5a6; /* Grey for reset */
    }

    .control-button:hover:not(:disabled) {
        background-color: #2980b9; /* Darker blue on hover */
    }
    .control-button.secondary:hover:not(:disabled) {
        background-color: #7f8c8d; /* Darker grey on hover */
    }

    .control-button:active:not(:disabled) {
        transform: scale(0.98); /* Slight press effect */
    }

    .control-button:disabled {
        background-color: #bdc3c7; /* Greyed out */
        cursor: not-allowed;
        opacity: 0.6;
    }

    /* Explanation Button Styling */
    #explanation-button {
        display: block;
        margin: 40px auto 20px auto; /* More spacing */
        padding: 14px 25px; /* Larger button */
        font-size: 1.2rem; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #2ecc71; /* Primary green */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(46, 204, 113, 0.3); /* Subtle shadow */
    }

    #explanation-button:hover {
        background-color: #27ae60; /* Darker green on hover */
        box-shadow: 0 6px 12px rgba(46, 204, 113, 0.4);
    }
    #explanation-button:active {
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(46, 204, 113, 0.2);
    }


    /* Explanation Section Styling */
    #explanation {
        direction: rtl;
        text-align: right;
        margin-top: 30px;
        padding: 25px;
        border: none;
        border-radius: 12px;
        background-color: #f9f9f9; /* Off-white background */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        display: none; /* Initially hidden */
        line-height: 1.7;
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: #2c3e50;
        border-bottom: 2px solid #3498db; /* Blue underline */
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
        font-weight: 700;
    }
    #explanation h2 { font-size: 1.6rem; }
    #explanation h3 { font-size: 1.3rem; color: #34495e;}


    #explanation p {
        margin-bottom: 20px;
    }

    #explanation ul {
        margin-bottom: 20px;
        padding-right: 20px; /* Adjust for RTL */
    }

    #explanation li {
        margin-bottom: 10px;
    }

    /* Add a simple fade-in animation for the explanation */
    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

</style>

<button id="explanation-button">הצג / הסתר הסבר מורחב</button>

<div id="explanation">
    <h2>הסבר מורחב: עקרונות ושימושים בקשירת קשרים</h2>

    <h3>מהו קשר ולמה הוא מחזיק מעמד?</h3>
    <p>בבסיסו, קשר הוא שימוש חכם בעקרונות הפיזיקה, בעיקר חיכוך, כדי לגרום לחבל לאחוז בעצמו או בחפץ אחר. הצורה הייחודית של כל קשר מכוונת את העומס המופעל עליו כך שהוא מגביר את הלחץ הפנימי בין חלקי החבל, יוצר נקודות אחיזה עצמיות ומונע החלקה בלתי רצויה. זהו ריקוד עדין בין מתיחה, לחיצה וחיכוך, המתורגם לחוזק ויציבות מפתיעים.</p>

    <h3>הכוחות בפעולה: פיזיקה של חבלים</h3>
    <ul>
        <li>**כוח החיכוך:** האשף הבלתי נראה ששומר על הקשר. כאשר החבל נכרך סביב עצמו או חפץ, נקודות המגע יוצרות חיכוך. ככל שהעומס גדל, כך גם הלחץ בין חלקי החבל עולה, ומגביר את כוח החיכוך שמונע מהם להחליק ולהשתחרר. טקסטורת החבל והחומר ממנו עשוי משפיעים ישירות על החיכוך.</li>
        <li>**כוח המתיחה:** הכוח הראשי המופעל על החבל. הקשר נועד לפזר את המתיחה הזו דרך מנגנוני כיפוף ולחיצה פנימיים. קשר יעיל מנתב את המתיחה ליצירת חיכוך פנימי, במקום לאפשר לחבל להתיישר ולהחליק.</li>
        <li>**הצורה היא הכל:** המבנה הגיאומטרי של הקשר אינו מקרי. הוא תוצר של אלפי שנים של ניסוי וטעייה. כל ליפוף, כל הצלבה, נועדו לוודא שהקשר "נועל" את עצמו בצורה כזו שגם תחת עומס, נקודות החיכוך נשמרות והחבל לא יכול לפרוק את עצמו. קשרים מסוימים אף נועדו להתהדק יותר כשהעומס גדל.</li>
    </ul>

    <h3>החבל עצמו: שותף בקשירה</h3>
    <p>בחירת החבל הנכון למשימה ולקשר היא קריטית. חומר, עובי ומבנה החבל משפיעים ישירות על אופן הקשירה, חוזק הקשר וביצועיו בתנאים שונים:</p>
    <ul>
        <li>**חומרים שונים, תכונות שונות:** חבלים טבעיים (כותנה, יוטה, קנבוס) ידידותיים יותר לאחיזה וקשירה, אך פחות עמידים. חבלים סינתטיים (ניילון, פוליאסטר) חזקים, עמידים למים ולשחיקה, ולעיתים חלקלקים יותר, מה שדורש קשרים שתוכננו במיוחד לעמידות בפני החלקה.</li>
        <li>**עובי וגמישות:** חבלים עבים יותר נוחים בדרך כלל ללמידה ולעבודה ללא כפפות. חבלים דקים יותר דורשים יותר דיוק. חבלים גמישים מאפשרים קשירה קלה יותר, בעוד שחבלים קשיחים יותר שומרים על צורתם טוב יותר אך קשים יותר לעבודה.</li>
        <li>**מבנה החבל:** חבלים קלועים (למשל, Kernmantle המשמש בטיפוס) חזקים ועמידים מאוד, עם ליבה נושאת עומס ומעטפת הגנה. חבלים שזורים (Twisted) נוטים להתפתל ופחות עמידים לשחיקה. מבנה החבל משפיע גם על האופן שבו הקשר "מתלבש" ומתהדק.</li>
    </ul>

    <h3>קשרים נבחרים וסיפורם (תרגלו אותם בסימולציה!)</h3>
    <ul>
        <li>**קשר שמינית (Figure Eight):** זהו ה"שלום" ו"להתראות" של עולם הקשרים המודרני. קל יחסית לזיהוי ויזואלי ופחות נוטה "להינעל" תחת עומס גבוה לעומת קשר בנאי (Overhand Knot). משמש כיסוד לקשירת לולאת קצה חזקה (Figure Eight Loop) או לחיבור בטיחותי לרתמת טיפוס (Figure Eight Follow Through). חיוני לכל מי שעובד עם חבלים תחת עומס.</li>
        <li>**קשר בוולין (Bowline):** "מלך הקשרים", קשר ההצלה הקלאסי. יוצר לולאה יציבה בקצה החבל שאינה מתהדקת גם תחת עומס, וקלה יחסית להתרה גם לאחר שרטבה או נשאה עומס. אידיאלי לקשירת חבל לעצם (עמוד, טבעת) או סביב אדם (בחילוץ). דורש תרגול לוודא שנקשר נכון ודורש השארת 'זנב' ארוך מספיק.</li>
        <li>**קשר רבוע (Square Knot / Reef Knot):** משמש בעיקר לחיבור שני חבלים בעובי ובסוג זהים, למטרות קשירה קלה ולא לנשיאת עומס משמעותי (למשל, קשירת אריזה או תחילת תחבושת). קל לקשירה אך חשוב להיזהר: הוא עלול להחליק ולהשתחרר תחת עומס משתנה או עם חבלים חלקלקים. אינו מומלץ למטרות בטיחות קריטיות.</li>
    </ul>

    <h3>בטיחות מעל הכל: לא רק איך לקשור, אלא איך לקשור בחוכמה</h3>
    <p>קשר שנקשר לא נכון או שאינו מטופל כראוי הוא קשר חסר תועלת, ואף מסוכן. הקפידו על העקרונות הבאים:</p>
    <ul>
        <li>**תרגול, תרגול, תרגול:** המיומנות נרכשת רק דרך חזרות רבות. קשור קשר בעיניים עצומות, בחושך, בקור. רק כך תבטח בו ברגע האמת.</li>
        <li>**השאירו זנב ארוך:** תמיד השאירו מספיק חבל בקצה העובד לאחר הידוק הקשר ('זנב'). הזנב מונע מהקשר להתפרק ולהשתחרר תחת עומס ותנועה. הכלל אצבע הוא להשאיר זנב באורך של לפחות פי 7-10 מקוטר החבל. במצבים קריטיים, כדאי אפילו לאבטח את הזנב בקשר עזר קטן ובטוח.</li>
        <li>**"הלבשת" הקשר ובדיקה ויזואלית:** לאחר הקשירה, "הלבישו" את הקשר – סדרו את החבלים כך שכל חלקי הקשר יהיו מסודרים ומקבילים היכן שצריך, ללא הצלבות מיותרות או לולאות מעוותות. קשר "לבוש" נכון לא רק נראה טוב יותר, אלא גם מתפקד חזק יותר ובטוח יותר. בדקו ויזואלית את כל חלקי הקשר לפני הפעלת עומס.</li>
        <li>**הידוק נכון:** הדקו את הקשר בהדרגה ובאחידות, משכו את כל ארבעת הקצוות (או מספרם הרלוונטי) כדי לוודא שהקשר מתהדק כראוי ו"יושב" במקומו. הידוק יתר לפני שהקשר מקבל עומס יכול להחליש סיבים או להפוך את התרת הקשר למשימה בלתי אפשרית.</li>
    </ul>

    <h3>מגרש המשחקים של החבלים: יישומים אינסופיים</h3>
    <p>שליטה באמנות הקשרים פותחת עולם של אפשרויות ויכולות:</p>
    <ul>
        <li>**טבע ושטח:** הקמת מחנה, בניית מחסה, תליית מזון הרחק מבעלי חיים, יצירת מתקנים פשוטים.</li>
        <li>**ים וימאות:** עגינה בטוחה, קשירת מפרשים, עבודה עם חבלים על כלי שיט.</li>
        <li>**גובה וסיכון:** טיפוס ספורטיבי ותעשייתי, עבודות בגובה, הצלה וחילוץ.</li>
        <li>**בטיחות ועזרה ראשונה:** קיבוע שברים, יצירת אלונקות מאולתרות.</li>
        <li>**בית וגינה:** קשירת חפצים להובלה, ארגון, עבודות גינון ותיקונים קטנים.</li>
        <li>**אמנות ויצירה:** מקרומה, יצירת חפצים שימושיים ואמנותיים.</li>
    </ul>
    <p>לימוד קשירת קשרים הוא השקעה חכמה במיומנות שתשרת אתכם בכל תחומי החיים. תרגלו, התנסו, והפכו את החבל לחבר הטוב ביותר שלכם ברגעים קריטיים וגם בשגרת היומיום.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const knotSelector = document.getElementById('knot-selector');
        const knotDisplay = document.getElementById('rope-svg');
        const instructionsDiv = document.getElementById('instructions');
        const prevBtn = document.getElementById('prev-step');
        const nextBtn = document.getElementById('next-step');
        const resetBtn = document.getElementById('reset-knot');
        const stepCounterDiv = document.getElementById('step-counter'); // Get the step counter element
        const explanationButton = document.getElementById('explanation-button');
        const explanationDiv = document.getElementById('explanation');

        let currentKnot = 'figure-eight';
        let currentStep = 0;

        // Define knot steps with more detailed SVG paths for better visualization
        // Using multiple path elements allows for showing different rope parts or highlights
        const knotData = {
            'figure-eight': {
                name: 'קשר שמינית',
                steps: [
                    { text: 'שלב 1: התחילו עם קצה החבל (הקצה העובד). צרו לולאה פשוטה עם הקצה העובד מעל החלק הארוך.', svg: '<path class="fixed-part" d="M 100 150 L 300 150" /><path class="working-end" d="M 200 150 Q 200 100 250 100 Q 300 100 300 150" opacity="0.6"/>' }, // Base rope + initial loop shape
                    { text: 'שלב 2: העבירו את הקצה העובד **מעל** החלק הארוך של החבל (מתחת ללולאה שנוצרה).', svg: '<path class="fixed-part" d="M 100 150 L 300 150" /><path class="working-end" d="M 200 150 Q 200 100 250 100 Q 300 100 300 150 M 270 130 L 330 170" />' }, // Show crossing path
                     { text: 'שלב 3: כעת העבירו את הקצה העובד **מתחת** ללולאה שנוצרה בתחילת השלב הקודם.', svg: '<path class="fixed-part" d="M 100 150 L 300 150" /><path class="working-end" d="M 200 150 Q 200 100 250 100 Q 300 100 300 150 M 330 170 C 350 220 250 220 270 130" />' }, // Show passing under the loop
                    { text: 'שלב 4: סיימו את הכריכה על ידי העברת הקצה העובד **דרך** הלולאה הראשונית, מלמטה למעלה.', svg: '<path class="fixed-part" d="M 100 150 L 300 150" /><path class="working-end" d="M 200 150 Q 200 100 250 100 Q 300 100 300 150 M 330 170 C 350 220 250 220 270 130 M 200 150 Q 230 120 250 100" />' }, // Show path entering loop
                    { text: 'שלב 5: משכו בעדינות את הקצה העובד ואת החלק הארוך כדי להדק את הקשר. ודאו שהוא נראה כמו המספר 8 מסודר!', svg: '<path class="rope-part" d="M 100 150 L 180 150 C 210 150 210 100 180 100 C 150 100 150 150 180 150 L 300 150" />' } // Simplified final knot
                ]
            },
            'bowline': {
                name: 'קשר בוולין',
                steps: [
                    { text: 'שלב 1: החזיקו את החבל כשהקצה העובד קרוב אליכם. צרו "חור של ארנב" – לולאה קטנה על החלק הארוך של החבל, כשהחלק העובד קרוב אליכם.', svg: '<path class="fixed-part" d="M 100 150 L 300 150" /><path class="working-end" d="M 300 150 L 350 150" /><path class="rope-part" d="M 200 150 Q 210 140 200 130 Q 190 140 200 150" stroke-width="8" opacity="0.7"/>' }, // Show fixed part, working end, and small loop hint
                    { text: 'שלב 2: "הארנב יוצא מהחור" - העבירו את הקצה העובד **למעלה** דרך הלולאה הקטנה שיצרתם.', svg: '<path class="fixed-part" d="M 100 150 L 300 150" /><path class="working-end" d="M 350 150 L 320 130 Q 210 120 200 130" />' }, // Show working end coming up through loop
                    { text: 'שלב 3: "הארנב רץ סביב העץ" - העבירו את הקצה העובד **מאחורי** החלק הארוך של החבל (החלק העומד).', svg: '<path class="fixed-part" d="M 100 150 L 300 150" /><path class="working-end" d="M 200 130 Q 210 120 320 130 M 320 130 Q 330 160 320 190" />' }, // Show working end going behind fixed part
                    { text: 'שלב 4: "הארנב חוזר הביתה לחור" - החזירו את הקצה העובד **למטה**, דרך אותה לולאה קטנה בה התחלתם (מהצד הנגדי של החבל העומד).', svg: '<path class="fixed-part" d="M 100 150 L 300 150" /><path class="working-end" d="M 200 130 Q 210 120 320 130 M 320 130 Q 330 160 320 190 M 320 190 Q 210 180 200 150" />' }, // Show working end going back into loop
                    { text: 'שלב 5: משכו את החלק הארוך (העץ) ואת הקצה העובד (הארנב) כדי להדק את הקשר. ודאו שהלולאה הגדולה (לולאת ההצלה) אינה מתהדקת!', svg: '<path class="rope-part" d="M 100 150 L 150 150 C 180 150 180 200 150 200 C 120 200 120 150 150 150 L 300 150" />' } // Simplified final knot with loop
                ]
            },
            'square': {
                name: 'קשר רבוע',
                steps: [
                    { text: 'שלב 1: התחילו עם שני חבלים (או שני קצוות של אותו חבל). קחו את החבל מימין (נצבע אותו באדום) והעבירו אותו **מעל** החבל משמאל (נצבע אותו בכחול).', svg: '<path class="working-end" stroke="red" d="M 100 140 L 250 160" /><path class="fixed-part" stroke="blue" d="M 100 160 L 250 140" />' }, // Red over Blue
                    { text: 'שלב 2: כעת כרכו את החבל האדום **מתחת** לחבל הכחול.', svg: '<path class="working-end" stroke="red" d="M 100 140 L 175 150" /><path class="fixed-part" stroke="blue" d="M 100 160 L 175 150" /><path class="working-end" stroke="red" d="M 175 150 L 250 160" /><path class="fixed-part" stroke="blue" d="M 175 150 L 250 140" />' }, // Show the wrap under
                     { text: 'שלב 3: עכשיו קחו את החבל שבימין (הכחול, שהיה קודם משמאל) והעבירו אותו **מעל** החבל שמשמאל (האדום).', svg: '<path class="rope-part" stroke="blue" d="M 100 150 L 175 150" /><path class="rope-part" stroke="red" d="M 100 150 L 175 150" /><path class="rope-part" stroke="blue" d="M 175 150 L 250 140" /><path class="rope-part" stroke="red" d="M 175 150 L 250 160" />' }, // Show second crossing attempt
                    { text: 'שלב 4: כרכו את החבל הכחול **מתחת** לחבל האדום, בדיוק הפוך מכפי שעשיתם בשלבים 1 ו-2.', svg: '<path class="rope-part" stroke="blue" d="M 100 150 L 175 150" /><path class="rope-part" stroke="red" d="M 100 150 L 175 150" /><path class="rope-part" stroke="blue" d="M 175 150 L 250 140" /><path class="rope-part" stroke="red" d="M 175 150 L 250 160" />' }, // Show the second wrap under
                    { text: 'שלב 5: משכו בעדינות את ארבעת הקצוות כדי להדק את הקשר. אם הקשר נראה שטוח ומרובע - הצלחתם!', svg: '<path class="rope-part" d="M 100 150 L 180 150 M 220 150 L 300 150 M 180 150 C 190 140 210 140 220 150 C 210 160 190 160 180 150" />' } // Simplified final knot
                ]
            }
        };

        // Function to draw SVG paths with a "drawing" animation effect
        function drawPaths(svgContent) {
            const parser = new DOMParser();
            const doc = parser.parseFromString(`<svg>${svgContent}</svg>`, 'image/svg+xml');
            const paths = doc.querySelectorAll('path');
            let delay = 0;

            knotDisplay.innerHTML = ''; // Clear previous SVG

            paths.forEach(path => {
                const pathElement = document.createElementNS("http://www.w3.org/2000/svg", "path");
                // Copy attributes
                Array.from(path.attributes).forEach(attr => {
                    pathElement.setAttribute(attr.name, attr.value);
                });

                // Apply drawing animation
                const length = pathElement.getTotalLength ? pathElement.getTotalLength() : 1000; // Fallback if getTotalLength fails
                pathElement.style.strokeDasharray = length;
                pathElement.style.strokeDashoffset = length; // Start invisible

                knotDisplay.appendChild(pathElement);

                // Animate drawing
                setTimeout(() => {
                    pathElement.style.transition = 'stroke-dashoffset 1s ease-in-out';
                    pathElement.style.strokeDashoffset = '0';
                     // Also fade in opacity slightly after drawing starts
                    pathElement.style.opacity = '1';
                    pathElement.style.transition += ', opacity 0.5s ease-in';

                }, delay);
                 delay += 100; // Small delay between paths

            });
        }


        function renderStep() {
            const knot = knotData[currentKnot];
            const step = knot.steps[currentStep];

            instructionsDiv.textContent = `${knot.name}: ${step.text}`;
            stepCounterDiv.textContent = `שלב ${currentStep + 1} / ${knot.steps.length}`; // Update step counter
            drawPaths(step.svg); // Use the new drawing function

            prevBtn.disabled = currentStep === 0;
            nextBtn.disabled = currentStep === knot.steps.length - 1;

             // Optional: Add a slight bounce/pulse animation to instructions when they change
             instructionsDiv.classList.add('pulse');
             setTimeout(() => {
                 instructionsDiv.classList.remove('pulse');
             }, 500);
        }

        function selectKnot(knotSlug) {
            currentKnot = knotSlug;
            currentStep = 0;
            renderStep();
        }

        // Event Listeners
        knotSelector.addEventListener('change', (event) => {
            selectKnot(event.target.value);
        });

        prevBtn.addEventListener('click', () => {
            if (currentStep > 0) {
                currentStep--;
                renderStep();
            }
        });

        nextBtn.addEventListener('click', () => {
            const knot = knotData[currentKnot];
            if (currentStep < knot.steps.length - 1) {
                currentStep++;
                renderStep();
            }
        });

        resetBtn.addEventListener('click', () => {
            selectKnot(currentKnot); // Reset to the first step of the current knot
        });

        explanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            if (isHidden) {
                explanationDiv.style.display = 'block';
                explanationDiv.classList.add('fade-in'); // Add fade-in class
                 // Remove class after animation to allow it to run again
                explanationDiv.addEventListener('animationend', () => {
                     explanationDiv.classList.remove('fade-in');
                 }, { once: true });
            } else {
                explanationDiv.style.display = 'none';
                 explanationDiv.classList.remove('fade-in'); // Ensure class is off when hidden
            }
        });

        // Initial render
        selectKnot(knotSelector.value);

        // Add pulse animation style dynamically
        const styleSheet = document.createElement("style");
        styleSheet.type = "text/css";
        styleSheet.innerText = `
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.02); }
                100% { transform: scale(1); }
            }
            #instructions.pulse {
                animation: pulse 0.5s ease-in-out;
            }
        `;
        document.head.appendChild(styleSheet);
    });
</script>
```