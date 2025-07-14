---
title: "מסע אל הקוטור: מהסקיצה לתפירה ידנית"
english_slug: journey-to-couture-from-sketch-to-hand-sewing
category: "אמנות ועיצוב / אופנה וטקסטיל"
tags:
  - קוטור
  - אופנה עילית
  - עיצוב אופנה
  - תפירה ידנית
  - מלאכת יד
---
# מסע אל הסטודיו: כך נולדת יצירת קוטור

שמלת קוטור אינה סתם בגד יוקרתי; היא יצירת אמנות הדורשת מאות שעות של עבודה ידנית מדויקת וחזון עיצובי. מהם השלבים שהופכים בד פשוט ליצירת מופת יחידה במינה? הצטרפו אלינו למסע מקוצר אל עולם הקוטור!

<div class="couture-simulator app-container">
    <h2 class="app-title">הסטודיו הדיגיטלי: צור יצירת קוטור משלך</h2>
    <p class="app-intro">בוא/י לחוות את הלב הפועם של יצירת קוטור דרך סימולציה אינטראקטיבית.</p>

    <div id="step-selection" class="app-step active">
        <h3 class="step-title">שלב 1: החזון - בחירת סקיצה</h3>
        <p class="step-instruction">כל יצירת קוטור מתחילה בחזון ובסקיצה ראשונית. איזו סקיצה תעורר לחיים?</p>
        <div class="sketch-options option-group">
            <div class="option interactive" data-sketch="A">
                <img src="https://via.placeholder.com/120x180?text=Sketch+A" alt="סקיצה A">
                <p>סקיצה A: שמלת נשף רומנטית</p>
            </div>
            <div class="option interactive" data-sketch="B">
                <img src="https://via.placeholder.com/120x180?text=Sketch+B" alt="סקיצה B">
                <p>סקיצה B: חליפת כוח מודרנית</p>
            </div>
            <div class="option interactive" data-sketch="C">
                <img src="https://via.placeholder.com/120x180?text=Sketch+C" alt="סקיצה C">
                <p>סקיצה C: שמלת קוקטייל עדינה</p>
            </div>
        </div>
        <p id="selected-sketch-info" class="selection-info">לחץ/י על סקיצה כדי לבחור אותה ולהתחיל את התהליך.</p>
    </div>

    <div id="step-materials" class="app-step">
        <h3 class="step-title">שלב 2: המגע היוקרתי - בחירת בדים וגימורים</h3>
        <p class="step-instruction">בחירת חומרי הגלם היא קריטית בקוטור. בחר/י את הבד הראשי והגימורים שיעניקו ליצירה את המראה והתחושה הייחודיים שלה.</p>
        <h4>בדים עיקריים (בחר/י אחד):</h4>
        <div class="material-options option-group" data-type="fabric">
            <div class="option interactive material-visual silk" data-material="silk">
                <p>משי טבעי</p>
            </div>
            <div class="option interactive material-visual lace" data-material="lace">
                <p>תחרה עדינה</p>
            </div>
            <div class="option interactive material-visual velvet" data-material="velvet">
                <p>קטיפה מלכותית</p>
            </div>
        </div>
        <h4>גימורים אמנותיים (ניתן לבחור מספר אפשרויות):</h4>
         <div class="material-options option-group" data-type="embellishment">
            <div class="option interactive material-visual embroidery" data-material="embroidery">
                <p>רקמת יד</p>
            </div>
            <div class="option interactive material-visual beads" data-material="beads">
                <p>חרוזים קריסטליים</p>
            </div>
             <div class="option interactive material-visual feathers" data-material="feathers">
                <p>נוצות קלילות</p>
            </div>
        </div>
         <p id="selected-materials-info" class="selection-info">בחר/י בד ראשי ולפחות גימור אחד כדי להמשיך.</p>
         <button id="next-to-sewing" class="app-button disabled" disabled>המשך לשלב התפירה והמלאכה</button>
    </div>

    <div id="step-sewing" class="app-step">
        <h3 class="step-title">שלב 3: ידי הזהב - תפירה וגימור ידניים</h3>
        <p class="step-instruction">כאן הקסם קורה: כל תפר, כל חיבור, מבוצע בקפידה אין קץ ביד. 'בצע/י' את המשימות המרכזיות בדרך ליצירה מושלמת.</p>
        <div class="sewing-tasks option-group">
            <div class="task interactive" data-task="seam">תפירת קווי תפר פנימיים עדינים <span class="task-status"></span></div>
            <div class="task interactive" data-task="lining">חיבור בטנה בתפר נסתר <span class="task-status"></span></div>
            <div class="task interactive" data-task="zipper">תפירת רוכסן נסתר ללא רבב <span class="task-status"></span></div>
            <div class="task interactive" data-task="embellish">חיבור גימורים דקורטיביים <span class="task-status"></span></div>
            <div class="task interactive" data-task="finishing">גימור קצוות ופרטים אחרונים בדיוק מרבי <span class="task-status"></span></div>
        </div>
        <p id="sewing-progress-info" class="selection-info">משימות שבוצעו: 0/5</p>
         <button id="next-to-fitting" class="app-button disabled" disabled>המשך לשלב המדידות וההתאמה</button>
    </div>

     <div id="step-fitting" class="app-step">
        <h3 class="step-title">שלב 4: ההתאמה המושלמת - מדידות ופינישים</h3>
        <p class="step-instruction">בקוטור, הבגד 'נולד' על גוף הלקוחה. מספר מדידות והתאמות מבטיחים התאמה אישית מדויקת. בצע/י את המדידה הראשונה.</p>
         <button id="simulate-fitting" class="app-button">סימולציה: ביצוע מדידה והתאמה</button>
         <p id="fitting-info" class="selection-info"></p>
          <button id="next-to-final" class="app-button disabled" disabled>המשך לחשיפת היצירה הסופית!</button>
    </div>

     <div id="step-final" class="app-step">
        <h3 class="step-title">הרגע הגדול: היצירה הושלמה!</h3>
        <p id="final-creation-info" class="selection-info">הנה פרי העבודה שלך!</p>
        <div id="final-garment-display">
            <!-- Placeholder, could be updated dynamically -->
            <img src="https://via.placeholder.com/250x380?text=Your+Couture+Masterpiece" alt="Your Couture Piece">
            <p id="final-garment-description"></p>
        </div>
         <button id="start-over" class="app-button secondary">התחל מחדש</button>
    </div>


    <div id="app-progress">
        <h4>התקדמות הפרויקט:</h4>
        <div class="progress-bar-container">
            <div class="progress-bar" style="width: 0%;"></div>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="app-button secondary centered">הצג/הסתר הסבר מעמיק על קוטור</button>

<div id="explanation" class="explanation-section hidden">
    <h2>המסע האמיתי אל הקוטור: עולם של אומנות ודיוק</h2>
    <p>סימולטור זה נתן טעימה קטנה מהתהליך, אך המציאות הרבה יותר מורכבת ומעמיקה. הנה סקירה של העולם המופלא של אופנת קוטור:</p>

    <h3>מהי אופנת קוטור (Haute Couture) ומהם כללי הפדרציה הצרפתית?</h3>
    <p>האוט קוטור (מצרפתית: תפירה עילית) אינה רק תפירה יוקרתית, אלא תואר המוענק ע"י הפדרציה הצרפתית לאופנה עילית (Fédération de la Haute Couture et de la Mode) לבתי אופנה העומדים בקריטריונים מחמירים ביותר: עיצוב וייצור בהזמנה אישית עבור לקוחות פרטיים, עם לפחות מדידה אחת; קיום סדנה (Atelier) בפריז המעסיקה לפחות 15 עובדים במשרה מלאה; הצגת קולקציה הכוללת לפחות 50 עיצובים (שמלות יום וערב) בכל עונה (פעמיים בשנה); ועוד. זהו עולם אקסקלוסיבי המייצג את פסגת היצירה האופנתית.</p>

    <h3>שלבי התהליך: מהסקיצה ועד ליצירה הסופית</h3>
    <p>התהליך ארוך ומורכב, וכולל לרוב: פגישת הכרות עם הלקוחה והבנת רצונותיה, יצירת סקיצות ראשוניות, בחירת עיצוב סופי, בחירת בדים וגימורים, לקיחת מידות מדויקות, בניית דגם ראשוני (מוסלין) ובדיקות ראשוניות, תפירת הבגד בבד הסופי, מספר רב של מדידות והתאמות על גוף הלקוחה, וגימורים אחרונים.</p>

    <h3>חשיבות הסקיצה והחזון של המעצב</h3>
    <p>הכל מתחיל מחזון המעצב, המתבטא בסקיצה. הסקיצה היא הבסיס - היא קובעת את הצללית, הקווים, הפרטים המרכזיים ואת האופי הכללי של הבגד. סקיצה טובה היא לא רק ציור יפה, אלא גם תכנית עבודה ראשונית לצוות המתפרה.</p>

    <h3>בחירת בדים: חומרי גלם יוקרתיים ונדירים</h3>
    <p>בקוטור משתמשים רק בחומרי הגלם המשובחים והנדירים ביותר: משי טהור, תחרות עבודת יד, בדים ארוגים במיוחד, עורות אקזוטיים, ועוד. בחירת הבד קריטית - היא משפיעה על הנפילה, התנועה והמראה הכללי של הבגד.</p>

    <h3>מלאכת התפירה הידנית: טכניקות מסורתיות וחדשנות</h3>
    <p>רוב מוחלט של העבודה בבגד קוטור נעשית ביד. התופרים (petites mains) הם אמנים בתחומם, המשתמשים בטכניקות תפירה בנות מאות שנים לצד טכניקות חדשניות שפותחו בתוך בתי הקוטור. הדיוק והסבלנות הנדרשים לביצוע תפרים בלתי נראים, חיבורי בדים עדינים, ויצירת מבנה פנימי תומך - הם יוצאי דופן.</p>

    <h3>תפקיד מתפרת הקוטור (Atelier)</h3>
    <p>האטלייה הוא הלב הפועם של בית הקוטור. זוהי הסדנה שבה מתבצעת כל עבודת התפירה והגימור. האטלייה מחולק בדרך כלל לפי סוגי העבודה (למשל, אטלייה לז'קטים ומעילים, ואטלייה לשמלות נשף), וכל אטלייה מאויש באמנים מומחים בתחומם.</p>

    <h3>רקמות, עיטורים וגימורים - האמנות בפרטים הקטנים</h3>
    <p>חלק נכבד מהשעות המושקעות בבגד קוטור מוקדש לרקמות, חרוזים, אבני חן, נוצות ועיטורים אחרים. עבודות אלו, המבוצעות לרוב ע"י בתי מלאכה מומחים (כמו Lesage לרקמות), הן יצירות אמנות בפני עצמן ומוסיפות ממד של פאר וייחודיות לבגד.</p>

    <h3>מדידות והתאמות: הבגד שמתאים בדיוק לגוף הלקוחה</h3>
    <p>בניגוד לייצור המוני, בגד קוטור נתפר בהתאמה אישית מלאה ללקוחה. לכן נדרשות מספר רב של מדידות (לעתים 3-5 ואף יותר), החל משלב דגם הבד הפשוט (מוסלין) ועד לשלבים הסופיים. כל מדידה מאפשרת התאמה מושלמת של הבגד לקימורים, ליציבה ולצרכים הספציפיים של הלקוחה.</p>

    <h3>קוטור מול Ready-to-Wear: ההבדלים המהותיים בייצור, בעלות ובערך</h3>
    <p>Ready-to-Wear (מוכן ללבישה) הוא אופנה בייצור סדרתי, בגדלים סטנדרטיים, הנמכר בחנויות. קוטור, לעומת זאת, הוא יצירה חד-פעמית, בהזמנה אישית, הנתפרת ביד ומותאמת בדיוק לגוף אחד. ההבדלים מתבטאים במחיר (בגדי קוטור יקרים פי עשרות ואף מאות מונים), בזמן הייצור (חודשים לעומת ימים/שבועות), בכמות (אחד לעומת אלפים/מיליונים), ובערך - קוטור הוא פסגת האמנות והאומנות, בעוד Ready-to-Wear הוא מוצר אופנה יוקרתי (או עממי).</p>

    <h3>מדוע קוטור נחשב לשיא היצירה האופנתית?</h3>
    <p>קוטור הוא המקום שבו אין פשרות על איכות, חומרים, זמן עבודה או יצירתיות. זוהי מעבדה לרעיונות, טכניקות וחידושים שחלקם מחלחלים בהמשך גם לאופנת Ready-to-Wear. זהו ביטוי טהור של אומנות התפירה, המעניק כבוד למלאכת היד המסורתית ומאפשר למעצבים לחקור גבולות יצירתיים ללא המגבלות של ייצור המוני.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    :root {
        --primary-color: #6b4d4d; /* Deep Rosy Brown */
        --secondary-color: #c2a2a2; /* Dusty Rose */
        --accent-color: #e0c2c2; /* Light Pinkish Brown */
        --background-color: #f8f0f0; /* Very Light Pink */
        --border-color: #d4c4c4; /* Muted Pinkish Grey */
        --text-color: #3a2d2d; /* Dark Brown */
        --success-color: #4CAF50; /* Green */
        --disabled-color: #a0a0a0; /* Grey */
        --hover-color: #8e7171;
    }

    body {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: var(--text-color);
        background-color: #fff; /* Keep body background white for contrast */
        padding: 20px;
    }

    h1, h2, h3, h4 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        margin-bottom: 40px;
        font-weight: 700;
    }

    h2.app-title {
        text-align: center;
        margin-bottom: 10px;
        font-weight: 700;
        color: var(--primary-color);
    }
     h3.step-title {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 15px;
        color: var(--primary-color);
        font-weight: 700;
    }

    .app-container {
        margin-bottom: 30px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--background-color);
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        overflow: hidden; /* Hide overflowing content during transitions */
        position: relative; /* For positioning absolute elements if needed */
    }

    .app-intro, .step-instruction {
        text-align: center;
        margin-bottom: 25px;
        color: var(--text-color);
    }

    .app-step {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        position: absolute; /* Position absolutely for smooth transitions */
        top: 0;
        left: 0;
        width: 100%;
        padding: 30px; /* Match container padding */
        box-sizing: border-box;
        pointer-events: none; /* Disable interaction when hidden */
    }

    .app-step.active {
        opacity: 1;
        transform: translateY(0);
        position: static; /* Restore flow when active */
        pointer-events: auto; /* Enable interaction */
    }

    .option-group {
        text-align: center;
        margin-bottom: 25px;
    }

    .option, .task {
        display: inline-block;
        margin: 8px;
        padding: 15px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        text-align: center;
        background-color: #fff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        min-width: 100px; /* Ensure consistent size */
        vertical-align: top; /* Align items nicely in line */
    }

     .interactive {
         cursor: pointer;
         transition: all 0.3s ease;
     }


    .option img {
        display: block;
        margin: 0 auto 10px;
        border-radius: 4px;
        border: 1px solid #eee;
    }

    .option p, .task p {
        margin: 0;
        font-size: 0.95em;
        color: var(--text-color);
        font-weight: 400;
    }

    .interactive:hover {
        border-color: var(--secondary-color);
        box-shadow: 0 3px 12px rgba(0,0,0,0.1);
         transform: translateY(-3px); /* Subtle hover effect */
    }

    .option.selected {
        border-color: var(--primary-color);
        background-color: var(--accent-color);
        box-shadow: 0 2px 8px rgba(0,0,0,0.15), inset 0 0 8px rgba(0,0,0,0.2);
        transform: scale(1.03); /* Indicate selection */
    }

     .task {
         position: relative; /* For status icon */
         display: block; /* Make tasks block for clearer list */
         width: 80%; /* Adjust width */
         margin: 10px auto; /* Center tasks */
         text-align: right;
         padding: 15px 20px;
     }

     .task-status {
        position: absolute;
        left: 15px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.2em;
        color: var(--disabled-color);
        transition: color 0.3s ease, transform 0.3s ease;
     }


     .task.completed {
        border-color: var(--success-color);
        background-color: #e8f5e9; /* Light green */
        box-shadow: 0 2px 8px rgba(0,0,0,0.05), inset 0 0 5px rgba(0,0,0,0.1);
        cursor: default;
        text-decoration: none; /* Remove line-through */
        color: #555; /* Slightly muted text */
    }

     .task.completed .task-status {
         content: '✔'; /* Checkmark icon */
         color: var(--success-color);
         transform: translateY(-50%) scale(1.1);
     }

     .interactive.completed:hover {
          transform: none; /* No hover transform on completed */
           border-color: var(--success-color); /* Keep success border */
     }


    .hidden {
        display: none;
    }

    .selection-info {
        margin-top: 20px;
        font-style: italic;
        color: var(--text-color);
        text-align: center;
        min-height: 1.2em; /* Reserve space to prevent layout shifts */
    }

    .app-button {
        display: block;
        margin: 25px auto 15px;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--primary-color);
        color: white;
        transition: background-color 0.3s ease, opacity 0.3s ease, transform 0.2s ease;
        font-weight: 700;
    }

     .app-button.secondary {
         background-color: var(--secondary-color);
         color: var(--text-color);
     }

     .app-button.secondary:hover:not(:disabled) {
          background-color: #b09090;
          color: white;
     }

    .app-button:hover:not(:disabled) {
        background-color: var(--hover-color);
        transform: translateY(-2px);
    }

     .app-button:active:not(:disabled) {
         transform: translateY(0);
     }

     button.disabled, .app-button.disabled {
        opacity: 0.5;
        cursor: not-allowed;
        transform: none;
     }

    #toggle-explanation {
         margin-top: 40px;
    }

     .centered {
         display: block;
         margin-left: auto;
         margin-right: auto;
     }


    #app-progress {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid var(--border-color);
        text-align: center;
    }
     #app-progress h4 {
         margin-bottom: 10px;
         color: var(--text-color);
         font-weight: 400;
     }


    .progress-bar-container {
        width: 90%;
        max-width: 400px;
        margin: 10px auto;
        background-color: #eee;
        border-radius: 10px;
        overflow: hidden;
        height: 20px;
    }

    .progress-bar {
        height: 100%;
        background-color: var(--secondary-color);
        width: 0%; /* Initial width */
        transition: width 0.7s ease-in-out;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8em;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
     .progress-bar::after {
         content: attr(data-label);
     }


    #final-garment-display {
        text-align: center;
        margin: 30px auto;
    }

    #final-gariment-display img {
        display: block;
        margin: 0 auto 15px;
        border: 1px solid var(--border-color);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-radius: 8px;
    }

     #final-garment-description {
         font-size: 1.1em;
         color: var(--primary-color);
         font-weight: 700;
         min-height: 1.5em; /* Reserve space */
     }


    .explanation-section {
        margin-top: 40px;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--background-color);
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: opacity 0.5s ease-in-out;
    }

    .explanation-section.hidden {
        opacity: 0;
        height: 0;
        padding-top: 0;
        padding-bottom: 0;
        margin-top: 0;
        overflow: hidden;
        border-color: transparent;
    }


    .explanation-section h2, .explanation-section h3 {
        color: var(--primary-color);
        text-align: right;
    }

    .explanation-section p {
        line-height: 1.7;
        margin-bottom: 15px;
        color: var(--text-color);
    }

    /* Material Visual Hints */
    .material-visual.silk { background-color: #f8f0f0; border: 1px solid #d4c4c4; }
    .material-visual.lace { background-image: url('https://via.placeholder.com/60x60?text=Lace'); background-size: cover; background-position: center; }
    .material-visual.velvet { background-color: #5a3a3a; color: white; }
    .material-visual.velvet p { color: white; }
    .material-visual.embroidery { background-image: url('https://via.placeholder.com/60x60?text=Emb'); background-size: cover; background-position: center; }
    .material-visual.beads { background-image: url('https://via.placeholder.com/60x60?text=Bds'); background-size: cover; background-position: center; }
    .material-visual.feathers { background-image: url('https://via.placeholder.com/60x60?text=Fthrs'); background-size: cover; background-position: center; }


</style>

<script>
    let selectedSketch = null;
    let selectedFabric = null;
    let selectedEmbellishments = new Set();
    const totalSewingTasks = 5;
    let completedSewingTasks = 0;
    let fittingDone = false;
    const totalAppSteps = 5; // Selection, Materials, Sewing, Fitting, Final
    let currentStep = 0; // 0: Initial, 1: Sketch, 2: Materials, 3: Sewing, 4: Fitting, 5: Final

    const sketchOptions = document.querySelectorAll('#step-selection .option');
    const materialOptions = document.querySelectorAll('#step-materials .option');
    const sewingTasks = document.querySelectorAll('#step-sewing .task');
    const simulateFittingButton = document.getElementById('simulate-fitting');
    const nextToSewingButton = document.getElementById('next-to-sewing');
    const nextToFittingButton = document.getElementById('next-to-fitting');
    const nextToFinalButton = document.getElementById('next-to-final');
    const startOverButton = document.getElementById('start-over');

    const sketchInfo = document.getElementById('selected-sketch-info');
    const materialsInfo = document.getElementById('selected-materials-info');
    const sewingProgressInfo = document.getElementById('sewing-progress-info');
    const fittingInfo = document.getElementById('fitting-info');
    const finalCreationInfo = document.getElementById('final-creation-info');
    const finalGarmentDescription = document.getElementById('final-garment-description');

    const appSteps = document.querySelectorAll('.app-step');
    const stepSelectionDiv = document.getElementById('step-selection');
    const stepMaterialsDiv = document.getElementById('step-materials');
    const stepSewingDiv = document.getElementById('step-sewing');
    const stepFittingDiv = document.getElementById('step-fitting');
    const stepFinalDiv = document.getElementById('step-final');

    const progressBar = document.querySelector('#app-progress .progress-bar');

    const stepMap = {
        'step-selection': 1,
        'step-materials': 2,
        'step-sewing': 3,
        'step-fitting': 4,
        'step-final': 5
    };

    function updateProgress() {
        const progress = (currentStep / totalAppSteps) * 100;
        progressBar.style.width = progress + '%';
         progressBar.setAttribute('data-label', `${currentStep}/${totalAppSteps}`);
    }

    function showStep(stepId) {
        appSteps.forEach(step => {
            step.classList.remove('active');
        });
        const targetStep = document.getElementById(stepId);
        if (targetStep) {
            targetStep.classList.add('active');
             currentStep = stepMap[stepId];
             updateProgress();
        }
    }

    function enableButton(button) {
        button.classList.remove('disabled');
        button.disabled = false;
    }

    function disableButton(button) {
         button.classList.add('disabled');
         button.disabled = true;
    }

    function resetSimulation() {
        selectedSketch = null;
        selectedFabric = null;
        selectedEmbellishments = new Set();
        completedSewingTasks = 0;
        fittingDone = false;
        currentStep = 0;

        // Reset UI elements
        sketchOptions.forEach(opt => opt.classList.remove('selected'));
        materialOptions.forEach(opt => opt.classList.remove('selected'));
        sewingTasks.forEach(task => {
            task.classList.remove('completed');
            task.querySelector('.task-status').textContent = ''; // Clear checkmark
        });

        sketchInfo.textContent = 'לחץ/י על סקיצה כדי לבחור אותה ולהתחיל את התהליך.';
        materialsInfo.textContent = 'בחר/י בד ראשי ולפחות גימור אחד כדי להמשיך.';
        sewingProgressInfo.textContent = `משימות שבוצעו: 0/${totalSewingTasks}`;
        fittingInfo.textContent = '';
        finalCreationInfo.textContent = 'הנה פרי העבודה שלך!';
        finalGarmentDescription.textContent = '';
         simulateFittingButton.textContent = 'סימולציה: ביצוע מדידה והתאמה';
         simulateFittingButton.disabled = false;


        disableButton(nextToSewingButton);
        disableButton(nextToFittingButton);
        disableButton(nextToFinalButton);

        // Show the first step and reset progress
        showStep('step-selection');
        updateProgress();
    }


    // Step 1: Sketch Selection
    sketchOptions.forEach(option => {
        option.addEventListener('click', () => {
            if (currentStep !== 1 && currentStep !== 0) return; // Only clickable at step 1 or initial

            sketchOptions.forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');
            selectedSketch = option.dataset.sketch;
            sketchInfo.textContent = `נבחרה סקיצה: ${option.querySelector('p').textContent}. נהדר!`;

            // Animate transition to next step
             setTimeout(() => {
                 showStep('step-materials');
             }, 600); // Delay matches CSS transition
        });
    });

    // Step 2: Materials Selection
    materialOptions.forEach(option => {
        option.addEventListener('click', () => {
             if (currentStep !== 2) return; // Only clickable at step 2

            const type = option.parentElement.dataset.type;
            const material = option.dataset.material;
            const materialName = option.querySelector('p').textContent;

            if (type === 'fabric') {
                materialOptions.forEach(opt => {
                    if (opt.parentElement.dataset.type === 'fabric') {
                        opt.classList.remove('selected');
                    }
                });
                option.classList.add('selected');
                selectedFabric = material;
            } else if (type === 'embellishment') {
                if (selectedEmbellishments.has(material)) {
                    selectedEmbellishments.delete(material);
                    option.classList.remove('selected');
                } else {
                     // Optional: Limit number of embellishments? For now, no limit.
                    selectedEmbellishments.add(material);
                    option.classList.add('selected');
                }
            }

            const fabricText = selectedFabric ? `בד ראשי: ${materialOptions.find(opt => opt.dataset.material === selectedFabric && opt.parentElement.dataset.type === 'fabric').querySelector('p').textContent}` : 'בד ראשי: לא נבחר';
            const embellishmentsText = selectedEmbellishments.size > 0 ? ` | גימורים: ${Array.from(selectedEmbellishments).map(e => materialOptions.find(opt => opt.dataset.material === e && opt.parentElement.dataset.type === 'embellishment').querySelector('p').textContent).join(', ')}` : ' | גימורים: לא נבחרו';

            materialsInfo.textContent = `הבחירות שלך: ${fabricText}${embellishmentsText}`;

            if (selectedFabric && selectedEmbellishments.size > 0) {
                enableButton(nextToSewingButton);
            } else {
                disableButton(nextToSewingButton);
            }
        });
    });

     nextToSewingButton.addEventListener('click', () => {
         if (currentStep === 2 && selectedFabric && selectedEmbellishments.size > 0) {
              showStep('step-sewing');
         }
     });


    // Step 3: Sewing Tasks
    sewingTasks.forEach(task => {
        task.addEventListener('click', () => {
             if (currentStep !== 3) return; // Only clickable at step 3

            if (!task.classList.contains('completed')) {
                task.classList.add('completed');
                task.querySelector('.task-status').textContent = '✔'; // Add checkmark
                 task.style.backgroundColor = '#e8f5e9'; // Apply completed background instantly
                 task.style.borderColor = var(--success-color); // Apply completed border instantly

                completedSewingTasks++;
                sewingProgressInfo.textContent = `משימות שבוצעו: ${completedSewingTasks}/${totalSewingTasks}`;

                if (completedSewingTasks === totalSewingTasks) {
                     sewingProgressInfo.textContent += " - כל המשימות הושלמו! עבודה מדהימה.";
                     enableButton(nextToFittingButton);
                }
                 // Update progress bar immediately on task completion
                 updateProgress();
            }
        });
    });

     nextToFittingButton.addEventListener('click', () => {
          if (currentStep === 3 && completedSewingTasks === totalSewingTasks) {
             showStep('step-fitting');
          }
     });

    // Step 4: Fitting
    simulateFittingButton.addEventListener('click', () => {
         if (currentStep !== 4 || fittingDone) return; // Only clickable at step 4 and not done yet

        fittingInfo.textContent = "מעצבים ואמני האטלייה מבצעים מדידות והתאמות קפדניות על מודל/גוף הלקוחה...";
        simulateFittingButton.disabled = true;
        simulateFittingButton.textContent = "מתבצעת מדידה...";


        setTimeout(() => { // Simulate time
             fittingInfo.textContent = "המדידה וההתאמות הסתיימו בהצלחה! הבגד מותאם באופן מושלם.";
             fittingDone = true;
             simulateFittingButton.textContent = "מדידה בוצעה בהצלחה";
             enableButton(nextToFinalButton);
             updateProgress(); // Update progress after fitting
        }, 2000); // Simulate 2 seconds
    });

     nextToFinalButton.addEventListener('click', () => {
         if (currentStep === 4 && fittingDone) {
              showStep('step-final');
             const sketchText = sketchOptions.find(opt => opt.dataset.sketch === selectedSketch).querySelector('p').textContent;
             const fabricText = materialOptions.find(opt => opt.dataset.material === selectedFabric && opt.parentElement.dataset.type === 'fabric').querySelector('p').textContent;
             const embellishmentsText = Array.from(selectedEmbellishments).map(e => materialOptions.find(opt => opt.dataset.material === e && opt.parentElement.dataset.type === 'embellishment').querySelector('p').textContent).join(', ');

             finalGarmentDescription.textContent = `יצרת: ${sketchText} עשויה מ${fabricText}, מקושטת ב${embellishmentsText}. יצירת קוטור אמיתית שנוצרה עם לב ונשמה!`;
              updateProgress(); // Final progress update
         }
     });

    // Start Over Button
    startOverButton.addEventListener('click', resetSimulation);


    // Toggle Explanation
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    toggleButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (explanationDiv.classList.contains('hidden')) {
            toggleButton.textContent = 'הצג הסבר מעמיק על קוטור';
        } else {
            toggleButton.textContent = 'הסתר הסבר מעמיק על קוטור';
        }
    });

    // Initial Setup: Show first step and hide others
    appSteps.forEach(step => {
        if (step.id !== 'step-selection') {
            step.classList.add('hidden'); // Use hidden class for initial display: none
        }
    });
    stepSelectionDiv.classList.add('active'); // Activate the first step
    stepSelectionDiv.classList.remove('hidden'); // Ensure it's not display: none
    currentStep = 1; // Set initial step for progress
    updateProgress();


    // Use a MutationObserver to handle step transitions
    const observer = new MutationObserver((mutations) => {
        mutations.forEach(mutation => {
            if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                const target = mutation.target;
                const stepId = target.id;
                const isActive = target.classList.contains('active');

                if (isActive) {
                    // A step became active, remove the 'hidden' class if present
                     target.classList.remove('hidden');
                    // Find previous step and add 'hidden' class after its transition
                    const previousStepElement = Array.from(appSteps).find(step =>
                        step.id !== stepId && !step.classList.contains('hidden')
                    );
                     if (previousStepElement) {
                         setTimeout(() => {
                             previousStepElement.classList.add('hidden');
                         }, 600); // Match active transition duration
                     }
                }
            }
        });
    });

    // Observe class changes on each step element
    appSteps.forEach(step => {
        observer.observe(step, { attributes: true });
    });


</script>
```