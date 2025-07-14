---
title: "ממה עשויה האות? המסע המרתק מדפוס גוטנברג למהפכת המידע"
english_slug: from-type-to-text-gutenbergs-printing-revolution
category: "מדעי הרוח / היסטוריה של המדע"
tags:
  - דפוס
  - גוטנברג
  - מהפכת המידע
  - היסטוריה
  - טכנולוגיה
  - המצאות
---
# ממה עשויה האות? המסע המרתק מדפוס גוטנברג למהפכת המידע

דמיינו עולם שבו כל עותק של ספר נכתב ביד, אות אחר אות. עבודה איטית, יקרה ועם המון מקום לטעויות. זה היה העולם לפני שהופיעה המצאה אחת גאונית ששינתה הכל. המצאה שאפשרה לשכפל ידע במהירות מסחררת, לפתוח שערים למידע וליצור את הבסיס לעולם המודרני שלנו. איך זה עבד? בואו נחווה את הקסם בעצמנו!

<div id="gutenberg-app" dir="rtl">
    <div class="app-header">
        <h2>סימולציה: לחוות את מכבש הדפוס העתיק</h2>
         <p>הזינו טקסט קצר ובואו נצא למסע מרתק דרך שלבי ההדפסה של גוטנברג.</p>
    </div>

    <div class="input-stage stage" id="stage-0">
        <div class="stage-content">
            <label for="textToPrint">הזינו את הטקסט המהפכני שלכם (עד 15 תווים, אותיות, מספרים, רווחים):</label>
            <input type="text" id="textToPrint" maxlength="15" placeholder="לדוגמה: ידע הוא כוח">
            <button id="startSimulationBtn" class="action-button">התחילו את התהליך!</button>
        </div>
    </div>

    <div class="simulation-area">
        <div id="stage-1" class="stage-area stage-1" style="display: none;">
            <div class="stage-header">
                 <h3>1. אוספים את האותיות המתאימות (Types)</h3>
                 <p>בוחרים מתוך אלפי אותיות המתכת (Types) את אלו שמרכיבות את הטקסט שלכם. לכל אות יש עותק בולט הפוך.</p>
            </div>
            <div id="individual-types" class="types-container">
                <!-- Individual type blocks will appear here -->
            </div>
            <button class="next-stage-button action-button" data-next-stage="2">לאסוף אותיות</button>
        </div>

        <div id="stage-2" class="stage-area stage-2" style="display: none;">
             <div class="stage-header">
                <h3>2. מסדרים את הטקסט (Composing Stick)</h3>
                <p>האותיות מסודרות זו ליד זו בתוך מסגרת ידנית ("Composing Stick"). כדי שההדפסה תצא נכון, צריך לסדר אותן **הפוך והפוך**! (גם היפוך אופקי וגם אנכי).</p>
            </div>
            <div id="composed-text" class="composed-stick stage-visual-container">
                 <!-- Arranged types will appear here -->
            </div>
            <button class="next-stage-button action-button" data-next-stage="3">סיימתי לסדר אותיות</button>
        </div>

        <div id="stage-3" class="stage-area stage-3" style="display: none;">
            <div class="stage-header">
                <h3>3. מעבירים למסגרת ההדפסה (Chase)</h3>
                <p>מעבירים את שורות הטקסט המסודרות למסגרת הדפסה גדולה יותר ("Chase") ומהדקים היטב כדי שאף אות לא תזוז!</p>
            </div>
            <div id="chase-frame" class="chase stage-visual-container">
                <div id="text-in-chase" class="text-in-chase">
                     <!-- Arranged types in chase -->
                </div>
            </div>
             <button class="next-stage-button action-button" data-next-stage="4">העבר למסגרת</button>
        </div>

         <div id="stage-4" class="stage-area stage-4" style="display: none;">
             <div class="stage-header">
                <h3>4. מורחים דיו</h3>
                <p>באמצעות כריות מיוחדות, מורחים דיו שחור ועשיר על פני האותיות הבולטות.</p>
            </div>
            <div id="inked-type" class="text-in-chase stage-visual-container">
                 <!-- Inked type in chase -->
            </div>
            <button class="next-stage-button action-button" data-next-stage="5">מרח דיו</button>
        </div>

         <div id="stage-5" class="stage-area stage-5" style="display: none;">
             <div class="stage-header">
                <h3>5. שמים נייר ולוחצים! (The Press)</h3>
                <p>מניחים גיליון נייר נקי על האותיות המוכנות ומפעילים לחץ עצום באמצעות המכבש כדי שהדיו יעבור לנייר.</p>
            </div>
            <div id="paper-overlay" class="paper-overlay stage-visual-container">
                 <p>גיליון נייר מחכה...</p>
             </div>
             <button id="pressBtn" class="action-button" disabled>הדפס!</button>
        </div>

        <div id="stage-6" class="stage-area stage-6" style="display: none;">
            <div class="stage-header">
                <h3>6. מציצים... התוצאה הסופית!</h3>
                 <p>והנה, הטקסט המודפס מופיע על הנייר, הפעם בצורה נכונה וקריאה.</p>
            </div>
            <div id="printed-output" class="printed-output stage-visual-container">
                 <!-- Final printed text -->
            </div>
             <button class="action-button" id="resetSimulationBtn">הדפיסו טקסט נוסף!</button>
        </div>

         <div id="error-message" class="error-message"></div>
    </div>

</div>

<button id="toggleExplanationBtn" class="toggle-button">הצג / הסתר הסבר מפורט</button>

<div id="explanation" class="explanation" style="display: none;">
    <h2>הסבר מפורט: מהפכת הדפוס של גוטנברג</h2>

    <h3>מי היה יוהן גוטנברג ולמה המצאתו הייתה כל כך חשובה?</h3>
    <p>יוהן גוטנברג (בערך 1398–1468) היה צורף, ממציא, ומדפיס גרמני. לפני המצאתו, ספרים ומסמכים שוכפלו ידנית על ידי סופרים או באמצעות דפוס בלוקים (שבו חרטו עמוד שלם על גוש עץ אחד), תהליכים שהיו איטיים, יקרים ומועדים לטעויות. המצאתו הגדולה של גוטנברג הייתה שיטת הדפסה באמצעות "אותיות נעות" (Movable Type) מתכת יצוקה. טכניקה זו אפשרה לסדר מחדש את האותיות עבור כל עמוד חדש, מה שהפך את תהליך ההדפסה למהיר, יעיל וכלכלי בהרבה.</p>

    <h3>איך עבדה מכונת הדפוס של גוטנברג?</h3>
    <p>המערכת של גוטנברג כללה מספר מרכיבים עיקריים:</p>
    <ul>
        <li>**אותיות הבלטה נעות (Movable Type):** יציקות קטנות של מתכת (בדרך כלל סגסוגת עופרת, בדיל ואנטימון) שעליהן הובלטה אות בודדת (או סימן פיסוק). לכל אות היו כמה וכמה יציקות.</li>
        <li>**כלי סידור (Composing Stick):** מסגרת ידנית שבה סודרו האותיות הבודדות זו ליד זו כדי ליצור שורות טקסט.</li>
        <li>**מסגרת (Chase):** מסגרת מתכת גדולה יותר שאליה הוכנסו השורות המסודרות מכלי הסידור, והן קובעו בתוכה היטב כדי שלא יזוזו במהלך ההדפסה.</li>
        <li>**דיו:** גוטנברג פיתח דיו על בסיס שמן, שהיה עמיד יותר ונצמד טוב יותר למתכת מאשר הדיו על בסיס מים ששימש לכתיבה ידנית.</li>
        <li>**מכבש הדפסה:** מכשיר המבוסס על מנגנון בורג (בדומה למכבשי יין או שמן) שהפעיל לחץ אחיד וחזק על הנייר המונח על האותיות המורכבות והמכורות, כדי להעביר את הדיו.</li>
    </ul>

    <h3>מהם השלבים העיקריים בתהליך הדפסה בשיטה זו?</h3>
    <ol>
        <li>**סידור אותיות (Typesetting/Composing):** סידור ידני של האותיות הבודדות (Type) בכלי סידור (Composing Stick) ליצירת מילים, שורות ופסקאות.</li>
        <li>**איגוד (Imposition):** העברת השורות המסודרות לכלי סידור גדול יותר או ישירות למסגרת (Chase) וקיבוע של כל האותיות יחד.</li>
        <li>**מריחת דיו (Inking):** מריחת דיו על פני השטח הבולטים של האותיות המורכבות, בדרך כלל באמצעות כריות עור מצופות בדיו.</li>
        <li>**הנחת נייר:** הנחת גיליון נייר על האותיות המכורות והמכורות.</li>
        <li>**הפעלת לחץ (Pressing):** הפעלת לחץ חזק באמצעות המכבש כדי להעביר את הדיו מהאותיות לנייר.</li>
        <li>**ייבוש וקיפול:** הסרת הנייר המודפס, ייבושו, וקיפולו (במידת הצורך) ליצירת דפים של ספר.</li>
        <li>**פירוק ושימוש חוזר:** לאחר הדפסת הכמות הנדרשת, האותיות פורקו, נוקו, והוחזרו לקופסאות המתאימות שלהן (לכל אות ותו היה תא משלו בקופסת ה-Typecase) כדי שניתן יהיה להשתמש בהן שוב עבור טקסט אחר.</li>
    </ol>

    <h3>למה היה צריך לסדר את האותיות הפוך והפוך?</h3>
    <p>כדי שהטקסט יופיע בצורה נכונה על הנייר, האותיות המתכת עצמן היו צריכות להיות מעוצבות כ"תמונת מראה" (הפוכות אופקית) וגם הפוכות אנכית (ראש כלפי מטה) כשהן מסודרות בכלי הסידור ומוכנות להדפסה. הסיבה היא שתהליך ההדפסה מעביר את הדיו מהמשטח הבולט של האות ישירות לנייר. אם האות הייתה ישרה, הטקסט על הנייר היה יוצא הפוך. בנוסף, מכיוון שהשפה העברית ורבות אחרות נכתבות מימין לשמאל, בסדר האותיות בכלי הסידור יש להתחיל מהסוף, כך שהמילה הראשונה במשפט היא בפועל האות האחרונה שמונחת בכלי הסידור (הכי שמאלה), והאות הראשונה במילה היא הכי ימנית בתוך רצף האותיות למילה זו. הדבר דורש חשיבה מורכבת מצד הסדר.</p>

    <h3>איך המצאת הדפוס שינתה את העולם?</h3>
    <p>המצאת הדפוס חוללה שינויים עצומים בחברה האנושית, והיא נחשבת לאחד הגורמים המרכזיים למעבר מימי הביניים לעת החדשה:</p>
    <ul>
        <li>**הפצת ידע מהירה והמונית:** לראשונה, ניתן היה לשכפל טקסטים במהירות ובהיקף גדול בהרבה מאשר בעבר.</li>
        <li>**הורדת עלויות:** הדפסה הייתה זולה בהרבה מהעתקה ידנית, מה שהפך ספרים ליותר נגישים.</li>
        <li>**עליית האוריינות:** הנגישות הגבוהה יותר לספרים ולחומר קריאה עודדה יותר אנשים ללמוד לקרוא ולכתוב.</li>
        <li>**הפצת רעיונות:** רעיונות חדשים, דתיים, פוליטיים ומדעיים, יכלו להתפשט במהירות רבה יותר. הדפוס היה קריטי להצלחת הרפורמציה הפרוטסטנטית, למשל.</li>
        <li>**מהפכה מדעית:** מדענים יכלו לפרסם ולשתף את ממצאיהם במהירות וביעילות, מה שהאיץ את התפתחות המדע.</li>
        <li>**אחידות טקסטואלית:** הדפסה הבטיחה שאף שהיו שגיאות דפוס, כל העותקים של אותה מהדורה היו זהים, בניגוד להעתקות ידניות שבהן שגיאות השתלשלו והצטברו.</li>
    </ul>

    <h3>האם הטכנולוגיה של גוטנברג עדיין רלוונטית היום?</h3>
    <p>מכונת הדפוס המכאנית של גוטנברג שימשה בשינויים מסוימים במשך מאות שנים, אך הטכנולוגיה עצמה כבר אינה בשימוש מסחרי נרחב כיום. שיטות דפוס מודרניות כמו דפוס אופסט (Offset Printing), דפוס דיגיטלי, ושיטות נוספות החליפו אותה. אולם, העקרונות הבסיסיים של העברת דיו ממשטח מוגבה (או אחר) לנייר תחת לחץ, והרעיון המהפכני של ייצור המוני של טקסטים אחידים, הם יסודות שהניחה המצאת גוטנברג. מהפכת המידע הנוכחית, המבוססת על טכנולוגיה דיגיטלית, היא במידה רבה המשך למהפכה שהחלה גוטנברג – שתיהן הגדילו באופן דרמטי את היכולת של האנושות לשכפל, להפיץ ולצרוך מידע.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');

    #gutenberg-app {
        font-family: 'Varela Round', sans-serif;
        direction: rtl;
        text-align: right;
        background: linear-gradient(to bottom, #f4e7d8, #e0d3c3);
        border: 1px solid #c0b2a1;
        border-radius: 10px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: 20px auto;
    }

     .app-header {
         text-align: center;
         margin-bottom: 30px;
     }

     .app-header h2 {
         color: #5a3c1f; /* Dark wood/metal color */
         margin-bottom: 10px;
         font-size: 1.8em;
     }

     .app-header p {
         color: #666;
         font-size: 1.1em;
     }

    .stage {
        margin-bottom: 25px;
        padding: 20px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        border: 1px solid #dcdcdc;
         opacity: 1;
         transition: opacity 0.5s ease-in-out;
    }

    .stage.hidden {
        opacity: 0;
        height: 0;
        padding: 0 20px;
        margin: 0;
        overflow: hidden;
    }


    .stage-area .stage-header {
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }

    .stage-area h3 {
        margin-top: 0;
        color: #5a3c1f;
        font-size: 1.5em;
    }
    .stage-area p {
        color: #555;
        line-height: 1.5;
    }

    .input-stage .stage-content {
         display: flex;
         flex-direction: column;
         align-items: center;
    }

    .input-stage label {
        font-size: 1.1em;
        color: #333;
        margin-bottom: 15px;
    }

    #textToPrint {
        padding: 12px 15px;
        border: 2px solid #ccc;
        border-radius: 5px;
        font-size: 1.2em;
        margin-bottom: 20px;
        text-align: center;
    }

    .action-button, .toggle-button {
        padding: 12px 20px;
        background-color: #8b4513; /* SaddleBrown - wood color */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        display: block;
        margin: 20px auto 0;
    }

     .action-button:hover, .toggle-button:hover {
        background-color: #a0522d; /* Siena - slightly lighter wood */
         transform: translateY(-1px);
     }

    .action-button:active, .toggle-button:active {
        transform: translateY(0);
    }

    .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
    }

    .stage-visual-container {
        min-height: 80px;
        border: 2px dashed #d3bfa0; /* Lighter wood dashed border */
        padding: 15px;
        margin-top: 15px;
        overflow-x: auto;
        white-space: nowrap;
        background-color: #f8f0e3; /* Creamy background */
        border-radius: 5px;
         display: flex;
         align-items: center;
         justify-content: flex-start; /* Start from left for LTR containers */
    }

    .types-container {
        /* Specific style for step 1 - show individual types */
        display: flex;
        flex-wrap: wrap; /* Allow wrapping if many types */
        justify-content: center; /* Center the individual types */
        direction: ltr; /* Display blocks LTR visually */
    }

    .type-block {
        display: inline-flex; /* Use inline-flex */
        justify-content: center;
        align-items: center;
        width: 35px; /* Slightly larger */
        height: 45px;
        background-color: #4a321f; /* Dark metal color */
        color: #eee; /* Light color for raised letter */
        font-weight: bold;
        font-size: 1.4em; /* Larger font */
        margin: 3px; /* Smaller margin */
        border: 2px outset #6f533e; /* Metal bevel effect */
        box-sizing: border-box;
        flex-shrink: 0; /* Prevent shrinking */
        user-select: none; /* Prevent selecting text */
    }

    /* Styles for composed, chase, inked - representing the actual type setup */
    .composed-stick .type-block,
    .chase .type-block,
    .text-in-chase .type-block,
    .inked-type .type-block {
         transform: scaleX(-1) rotate(180deg); /* Backwards and Upside Down */
         color: #eee; /* Still light metal */
         background-color: #5a3c1f; /* Slightly lighter metal when composed */
         border: 2px outset #7b5b43;
         direction: ltr; /* Critical: Layout the reversed types LTR in the stick/chase */
    }

    .types-container .type-block {
         transform: none; /* Show them normally in stage 1 */
         background-color: #7b5b43; /* Slightly different color before composing */
         border: 2px outset #a08a72;
          color: white;
    }

    .composed-stick, .chase, .text-in-chase {
         direction: ltr; /* The container is LTR */
          justify-content: flex-start; /* Start adding blocks from the left */
    }

    .chase {
        border-color: #8b4513; /* Stronger wood border */
        border-width: 4px;
    }

     .text-in-chase {
         border: none; /* Remove dashed border inside chase */
         padding: 0;
         min-height: 50px;
         display: flex;
         flex-wrap: wrap;
         align-items: flex-start;
         justify-content: flex-start;
         direction: ltr; /* Still LTR layout of the block */
     }

     #inked-type {
         background-color: #40342b; /* Darker background to show ink */
     }

     #inked-type .type-block {
         background-color: #1a1a1a; /* Dark ink color */
         color: rgba(255, 255, 255, 0.1); /* Make the letter barely visible */
         border-color: #0d0d0d;
         box-shadow: inset 0 0 8px rgba(0,0,0,0.8); /* Inked look */
     }

    .paper-overlay {
         width: calc(100% - 30px); /* Adjust for padding */
         height: 120px; /* More substantial paper area */
         background-color: #fffff0; /* Off-white paper color */
         border: 1px solid #ccc;
         margin: 15px auto; /* Center the paper */
         display: flex;
         align-items: center;
         justify-content: center;
         font-size: 1.3em;
         color: #555;
         border-radius: 5px;
         position: relative; /* For potential future animations */
    }


    .printed-output {
        min-height: 100px;
        border: 3px solid #333;
        background-color: #fff;
        font-size: 2em; /* Larger printed text */
        color: #1a1a1a; /* Ink color */
        padding: 25px;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        direction: rtl; /* Printed text is read RTL */
        font-family: serif; /* Simulate classic print font */
         box-shadow: inset 0 0 10px rgba(0,0,0,0.2); /* Impression effect */
         line-height: 1.4;
         white-space: normal; /* Allow text to wrap */
    }

    .error-message {
        color: #d9534f; /* Bootstrap danger color */
        font-weight: bold;
        margin-top: 20px;
        text-align: center;
        font-size: 1.1em;
    }

    .toggle-button {
        margin-top: 30px;
        background-color: #5cb85c; /* Bootstrap success color */
    }

     .toggle-button:hover {
         background-color: #4cae4c;
     }

    .explanation {
        border-top: 3px solid #007bff;
        margin-top: 30px;
        padding-top: 25px;
        direction: rtl;
        color: #333;
    }

    .explanation h2 {
        color: #0056b3;
        margin-bottom: 15px;
        font-size: 1.8em;
    }
     .explanation h3 {
         color: #007bff;
         margin-bottom: 10px;
         font-size: 1.4em;
     }

    .explanation p, .explanation ul, .explanation ol {
        line-height: 1.7;
        margin-bottom: 15px;
        text-align: justify;
    }

    .explanation ul, .explanation ol {
         padding-right: 25px; /* Indent list items */
    }

    .explanation li {
        margin-bottom: 10px;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideInFromLeft {
        from { transform: translateX(-50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
     @keyframes slideInFromRight {
        from { transform: translateX(50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    @keyframes inkedPulse {
        0% { box-shadow: inset 0 0 8px rgba(0,0,0,0.8); }
        50% { box-shadow: inset 0 0 12px rgba(0,0,0,1); }
        100% { box-shadow: inset 0 0 8px rgba(0,0,0,0.8); }
    }

    .stage-area.visible {
         animation: fadeIn 0.8s ease-out forwards;
    }

    .types-container .type-block,
    .composed-stick .type-block,
    .text-in-chase .type-block,
    .inked-type .type-block {
        animation: slideInFromRight 0.3s ease-out forwards; /* Animate type appearance */
         opacity: 0; /* Start hidden */
    }

     #inked-type .type-block {
         animation: inkedPulse 1.5s infinite ease-in-out, slideInFromRight 0.3s ease-out forwards;
     }

     .paper-overlay {
         animation: fadeIn 0.8s ease-out forwards;
     }

     .printed-output {
         animation: fadeIn 1.5s ease-out forwards; /* Slower fade for final result */
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const appContainer = document.getElementById('gutenberg-app');
        const textToPrintInput = document.getElementById('textToPrint');
        const startSimulationBtn = document.getElementById('startSimulationBtn');
        const individualTypesDiv = document.getElementById('individual-types');
        const composedTextDiv = document.getElementById('composed-text');
        const textInChaseDiv = document.getElementById('text-in-chase');
        const inkedTypeDiv = document.getElementById('inked-type');
        const paperOverlayDiv = document.getElementById('paper-overlay');
        const pressBtn = document.getElementById('pressBtn');
        const printedOutputDiv = document.getElementById('printed-output');
        const errorMessageDiv = document.getElementById('error-message');
        const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
        const explanationDiv = document.getElementById('explanation');
        const resetSimulationBtn = document.getElementById('resetSimulationBtn');

        let currentText = '';
        let composedLetters = [];
        let currentStage = 0; // 0: input, 1: prepared, 2: composed, 3: in chase, 4: inked, 5: paper, 6: pressed

        const stages = [
            { id: 'stage-0', areaId: null, buttonSelector: '#startSimulationBtn' },
            { id: 'stage-1', areaId: 'individual-types', buttonSelector: '.stage-1 .next-stage-button' },
            { id: 'stage-2', areaId: 'composed-text', buttonSelector: '.stage-2 .next-stage-button' },
            { id: 'stage-3', areaId: 'chase-frame', buttonSelector: '.stage-3 .next-stage-button' },
            { id: 'stage-4', areaId: 'inked-type', buttonSelector: '.stage-4 .next-stage-button' },
            { id: 'stage-5', areaId: 'paper-overlay', buttonSelector: '#pressBtn' },
            { id: 'stage-6', areaId: 'printed-output', buttonSelector: '#resetSimulationBtn' },
        ];

        function updateSimulationStage(newStage) {
            currentStage = newStage;

            // Hide all stages first
            document.querySelectorAll('.stage').forEach(stageEl => {
                 if (!stageEl.classList.contains('input-stage')) { // Keep input stage potentially visible or handle its hiding explicitly
                    stageEl.classList.add('hidden');
                    stageEl.style.display = 'none';
                    stageEl.classList.remove('visible'); // Remove animation class
                 }
            });

            // Show the current stage
            const currentStageElement = document.getElementById(stages[currentStage].id);
            if (currentStageElement) {
                 currentStageElement.style.display = 'block';
                 // Use a timeout to allow display:block to take effect before animation
                 setTimeout(() => {
                     currentStageElement.classList.remove('hidden');
                     currentStageElement.classList.add('visible'); // Add animation class
                 }, 10);
            }

            // Enable/disable buttons based on stage
            document.querySelectorAll('.action-button').forEach(button => {
                button.style.display = 'none'; // Hide all action buttons by default
            });

            const currentStageButtonSelector = stages[currentStage].buttonSelector;
             if (currentStageButtonSelector) {
                  const button = document.querySelector(currentStageButtonSelector);
                  if (button) {
                       button.style.display = 'block';
                       button.disabled = false; // Enable the button for the current stage
                  }
             }

             // Specific button states
             pressBtn.disabled = currentStage !== 5;


             // Clear content of future stages
             if (currentStage < 6) printedOutputDiv.innerHTML = '';
             if (currentStage < 5) paperOverlayDiv.innerHTML = '<p>גיליון נייר מחכה...</p>'; paperOverlayDiv.style.display = 'none';
             if (currentStage < 4) inkedTypeDiv.innerHTML = '';
             if (currentStage < 3) textInChaseDiv.innerHTML = '';
             if (currentStage < 2) composedTextDiv.innerHTML = '';
             if (currentStage < 1) individualTypesDiv.innerHTML = '';

             errorMessageDiv.textContent = ''; // Clear errors on stage change

        }

        function resetSimulation() {
            currentText = '';
            composedLetters = [];
            textToPrintInput.value = '';
            updateSimulationStage(0);
            document.getElementById('stage-0').classList.remove('hidden'); // Ensure input stage is visible
             document.getElementById('stage-0').style.display = 'block';
             document.getElementById('stage-0').classList.add('visible');
             resetSimulationBtn.style.display = 'none'; // Hide reset button until stage 6
        }


        startSimulationBtn.addEventListener('click', () => {
            const text = textToPrintInput.value.trim();
            if (!text) {
                errorMessageDiv.textContent = 'אנא הזן טקסט להדפסה כדי להתחיל.';
                return;
            }

            // Basic validation: only letters, numbers, spaces, common punctuation
             const validChars = /^[a-zA-Z0-9\sא-ת.,!?"']*$/;
             if (!validChars.test(text)) {
                 errorMessageDiv.textContent = 'הטקסט מכיל תווים שאינם נתמכים במכונת הדפוס הפשוטה הזו.';
                 return;
             }

            currentText = text;
            errorMessageDiv.textContent = ''; // Clear previous errors

             // Prepare Individual Types (Stage 1)
             individualTypesDiv.innerHTML = '';
            for (const char of currentText) {
                const typeBlock = document.createElement('div');
                typeBlock.classList.add('type-block');
                typeBlock.textContent = char === ' ' ? '' : char; // Show space as empty block
                typeBlock.title = char === ' ' ? 'אות רווח' : `האות ${char}`;
                typeBlock.setAttribute('data-char', char); // Store original character
                individualTypesDiv.appendChild(typeBlock);
            }

             // Prepare Composed Text (Stage 2 - visually reversed and upside down)
             // Keep the simplified reversal logic for visual representation
             const reversedText = currentText.split('').reverse().join('');
             composedLetters = reversedText.split('');

             composedTextDiv.innerHTML = ''; // Clear previous content
             composedLetters.forEach(char => {
                 const typeBlock = document.createElement('div');
                 typeBlock.classList.add('type-block');
                 typeBlock.textContent = char === ' ' ? '' : char; // Space is empty block
                 typeBlock.title = char === ' ' ? 'אות רווח (הפוך)' : `האות ${char} (הפוך והפוך)`;
                 typeBlock.setAttribute('data-char', char);
                 composedTextDiv.appendChild(typeBlock);
             });


            updateSimulationStage(1); // Move to stage 1 (Collect Types)
        });

        // Handle clicks on next stage buttons
        document.querySelectorAll('.next-stage-button').forEach(button => {
            button.addEventListener('click', (e) => {
                const nextStage = parseInt(e.target.getAttribute('data-next-stage'), 10);

                if (currentStage === 1) {
                    // Animation for gathering types can go here
                     animateBlocks(individualTypesDiv.querySelectorAll('.type-block'), composedTextDiv, true); // Animate to composed stage
                } else if (currentStage === 2) {
                    // Animation for transferring to chase
                     animateBlocks(composedTextDiv.querySelectorAll('.type-block'), textInChaseDiv);
                } else if (currentStage === 3) {
                     // Animation for inking
                    animateBlocks(textInChaseDiv.querySelectorAll('.type-block'), inkedTypeDiv, false, true); // Indicate inking
                } else if (currentStage === 4) {
                     // Simulate placing paper
                     paperOverlayDiv.style.display = 'flex';
                     updateSimulationStage(nextStage);
                     return; // Avoid default stage update
                }


                // Default stage update
                updateSimulationStage(nextStage);
            });
        });

        pressBtn.addEventListener('click', () => {
            if (currentStage < 5) return; // Only press if ready

            // Simulate pressing animation
            const pressAnimation = document.createElement('div');
            pressAnimation.classList.add('press-animation');
            appContainer.style.position = 'relative'; // Ensure relative positioning for absolute animation overlay
            pressAnimation.style.cssText = `
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                background-color: rgba(0, 0, 0, 0.2);
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 3em;
                z-index: 10;
                opacity: 0;
                pointer-events: none;
                transition: opacity 0.5s ease-in-out;
            `;
             pressAnimation.textContent = 'לוחץ...';
             appContainer.appendChild(pressAnimation);

             // Start fade-in animation
             setTimeout(() => { pressAnimation.style.opacity = 1; }, 10);

             // Simulate pressing duration
             setTimeout(() => {
                 // Fade out animation
                 pressAnimation.style.opacity = 0;
                 pressAnimation.addEventListener('transitionend', () => {
                     appContainer.removeChild(pressAnimation);
                      appContainer.style.position = 'static'; // Restore position
                 });

                 // Display the correctly oriented text after press
                 const printedText = currentText; // The original text is the correct output

                 printedOutputDiv.textContent = printedText;
                 updateSimulationStage(6); // Show result
                 resetSimulationBtn.style.display = 'block'; // Show reset button
             }, 1500); // Animation duration

        });


        resetSimulationBtn.addEventListener('click', () => {
            resetSimulation();
        });

        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
             explanationDiv.classList.toggle('hidden', !isHidden);
             explanationDiv.classList.toggle('visible', isHidden);

            toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג / הסתר הסבר מפורט';
        });

        // Simple animation helper function (placeholder, could be more sophisticated)
        function animateBlocks(sourceNodes, targetContainer, applyTransform = false, applyInk = false) {
             targetContainer.innerHTML = ''; // Clear target immediately for transition effect
             sourceNodes.forEach((node, index) => {
                 const clonedBlock = node.cloneNode(true);
                  // Remove previous animation class if any
                 clonedBlock.classList.remove('slideInFromRight');
                  // Apply new styles based on destination stage
                 if (applyTransform) {
                     clonedBlock.style.transform = 'scaleX(-1) rotate(180deg)';
                     clonedBlock.style.backgroundColor = '#5a3c1f';
                     clonedBlock.style.borderColor = '#7b5b43';
                     clonedBlock.style.color = '#eee';
                      clonedBlock.textContent = clonedBlock.getAttribute('data-char') === ' ' ? '' : clonedBlock.getAttribute('data-char');
                      clonedBlock.title = clonedBlock.getAttribute('data-char') === ' ' ? 'אות רווח (הפוך)' : `האות ${clonedBlock.getAttribute('data-char')} (הפוך והפוך)`;
                 } else {
                      // Styles for chase/inking stages (already transformed)
                       clonedBlock.style.transform = 'scaleX(-1) rotate(180deg)';
                       clonedBlock.style.backgroundColor = '#5a3c1f';
                       clonedBlock.style.borderColor = '#7b5b43';
                       clonedBlock.style.color = '#eee';
                       clonedBlock.textContent = clonedBlock.getAttribute('data-char') === ' ' ? '' : clonedBlock.getAttribute('data-char');
                        clonedBlock.title = clonedBlock.getAttribute('data-char') === ' ' ? 'אות רווח (במסגרת)' : `האות ${clonedBlock.getAttribute('data-char')} (במסגרת)`;
                 }

                  if (applyInk) {
                     clonedBlock.classList.add('inked');
                      clonedBlock.style.backgroundColor = '#1a1a1a';
                      clonedBlock.style.color = 'rgba(255, 255, 255, 0.1)';
                      clonedBlock.style.borderColor = '#0d0d0d';
                      clonedBlock.title = clonedBlock.getAttribute('data-char') === ' ' ? 'אות רווח (מכור)' : `האות ${clonedBlock.getAttribute('data-char')} (מכור)`;
                 }

                 // Animate appearance with a slight delay
                 clonedBlock.style.opacity = 0; // Start hidden for animation
                 targetContainer.appendChild(clonedBlock);
                 setTimeout(() => {
                     clonedBlock.style.opacity = 1;
                      clonedBlock.style.transform = applyTransform || applyInk ? 'scaleX(-1) rotate(180deg)' : 'none'; // Apply final transform state
                      // Re-apply animation for subtle effect
                      clonedBlock.style.animation = 'slideInFromRight 0.3s ease-out forwards';
                       if (applyInk) {
                            clonedBlock.style.animation = 'inkedPulse 1.5s infinite ease-in-out, slideInFromRight 0.3s ease-out forwards';
                       }

                 }, index * 30); // Stagger animation
             });
        }


        // Initial setup
        resetSimulation();
    });
</script>
---