---
title: "הרי געש בוציים: הצצה להתפרצות הקרה מהמעמקים"
english_slug: mud-volcanoes-cold-eruption-from-the-depths
category: "מדעי הסביבה / גיאולוגיה"
tags:
  - הרי געש
  - גיאולוגיה
  - בוץ
  - תהליכים גיאולוגיים
  - מתאן
---
# הרי געש בוציים: הצצה להתפרצות הקרה מהמעמקים

שכחו מלבה אדומה ואפר לוהט. עכשיו נצלול לעולם הרי הגעש הבוציים – תופעה גיאולוגית מסקרנת, שונה בתכלית, ומונעת מכוחות מסתוריים מהמעמקים הקרים של כדור הארץ. הצטרפו למסע כדי להבין איך בוץ, מים וגזים נלכדים עמוק מתחת לפני השטח, בונים לחץ אדיר, ומוצאים דרך החוצה בהתפרצות קרה ומפתיעה.

<div id="mud-volcano-app">
    <div class="app-container">
        <div class="simulation-area">
            <div class="layer surface">
                 <span class="layer-label">פני השטח</span>
                 <div class="surface-eruption-effect"></div>
            </div>
            <div class="layer top-sediments">
                 <span class="layer-label">שכבות משקע עליונות</span>
            </div>
            <div class="layer impermeable-layer">
                 <span class="layer-label">שכבה אטומה</span>
            </div>
            <div class="layer trapped-zone">
                <span class="layer-label">אזור לכידה (נוזלים וגזים)</span>
                <div class="trapped-fluids-gas"></div>
                <div class="pressure-indicator">לחץ: <span id="pressure-value">0%</span></div>
            </div>
            <div class="layer deep-sediments">
                 <span class="layer-label">שכבות משקע עמוקות</span>
            </div>
            <div class="weak-point"></div>
            <div class="conduit"></div>
            <div class="mud-cone"></div>
        </div>

        <div class="controls-panel">
            <h3>שליטה בכוחות הטבע</h3>
            <div class="control-group">
                <label for="sediment-load">עומס סלע (כובד השכבות מעל):</label>
                <input type="range" id="sediment-load" min="0" max="100" value="30">
                <span id="sediment-load-value">30</span>%
            </div>

            <div class="control-group">
                <label for="fluid-gas-volume">כמות נוזלים וגזים כלואים:</label>
                <input type="range" id="fluid-gas-volume" min="0" max="100" value="30">
                <span id="fluid-gas-volume-value">30</span>%
            </div>

            <div class="control-group">
                <label for="weak-point-present">קיום נקודת חולשה (סדק / העתק):</label>
                <input type="checkbox" id="weak-point-present">
            </div>

            <!-- Removed the "Simulate" button as simulation updates live -->
        </div>
         <p class="simulation-hint">שנו את ערכי המחוונים או סמנו את תיבת הסימון וראו כיצד הלחץ משתנה והאם מתרחשת התפרצות!</p>
    </div>
</div>

<style>
    #mud-volcano-app {
        font-family: 'Arial', sans-serif;
        max-width: 800px;
        margin: 20px auto;
        background: linear-gradient(to bottom, #f8f8f8, #e8e8e8);
        border: 1px solid #d0d0d0;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        overflow: hidden;
        color: #333;
    }

    .app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }

    .simulation-area {
        width: 95%;
        height: 450px; /* Increased height slightly */
        border: 3px solid #4a3a2a; /* Darker, richer brown */
        position: relative;
        overflow: hidden;
        background-color: #e0d8c3; /* Earthy background */
        box-sizing: border-box;
        margin-bottom: 25px;
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.2);
    }

    .layer {
        position: absolute;
        width: 100%;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #fff;
        text-shadow: 1px 1px 2px #000;
        font-size: 0.9em;
        text-align: center;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        transition: background-color 0.5s ease; /* Add transition for potential color changes */
    }

    .layer-label {
         background-color: rgba(0, 0, 0, 0.3);
         padding: 2px 8px;
         border-radius: 4px;
         font-size: 0.8em;
         pointer-events: none; /* Don't interfere with clicks */
    }


    .surface {
        top: 0;
        left: 0;
        width: 100%;
        height: 15px; /* Thicker surface */
        background-color: #70a060; /* Greener earth */
        z-index: 10; /* Bring to front */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .top-sediments {
        top: 15px;
        height: 90px; /* Adjusted height */
        background-color: #c0a080; /* Brown */
        background-image: linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.05) 75%, rgba(0,0,0,0.05)), linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.05) 75%, rgba(0,0,0,0.05));
        background-size: 20px 20px;
        background-position: 0 0, 10px 10px;
    }

    .impermeable-layer {
        top: 105px; /* Adjusted position */
        height: 35px; /* Slightly thicker */
        background-color: #5a4a8c; /* Deeper purple/blue */
        background-image: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 8px 8px;
    }

    .trapped-zone {
        top: 140px; /* Adjusted position */
        height: 180px; /* Increased height */
        background-color: #d2b48c; /* Tan */
        overflow: hidden;
        position: relative; /* Needed for absolute children */
         box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .deep-sediments {
        top: 320px; /* Adjusted position */
        height: 130px; /* Adjusted height */
        background-color: #a08060; /* Darker Brown */
         background-image: linear-gradient(45deg, rgba(0,0,0,0.07) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.07) 75%, rgba(0,0,0,0.07)), linear-gradient(45deg, rgba(0,0,0,0.07) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.07) 75%, rgba(0,0,0,0.07));
        background-size: 25px 25px;
        background-position: 0 0, 12.5px 12.5px;
    }

    .trapped-fluids-gas {
        position: absolute;
        bottom: 0; /* Start from bottom of trapped zone */
        left: 5%; /* Slightly narrower */
        width: 90%; /* Slightly narrower */
        height: 0%; /* Initial height */
        background: linear-gradient(to top, rgba(0, 100, 255, 0.7), rgba(100, 180, 255, 0.7), rgba(173, 216, 230, 0.8)); /* More vibrant blue gradient */
        transition: height 0.8s ease-out; /* Slower, smoother transition */
        box-sizing: border-box;
        border-top: 3px dashed rgba(255, 255, 255, 0.8);
         box-shadow: inset 0 5px 10px rgba(0,0,0,0.2);
    }

    .pressure-indicator {
        position: absolute;
        top: 15px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.95);
        padding: 5px 10px;
        border-radius: 6px;
        font-size: 1em; /* Slightly larger */
        font-weight: bold;
        color: #333;
        z-index: 15;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        min-width: 80px;
        text-align: center;
    }

     .pressure-indicator span {
        font-weight: bold;
        color: #32cd32; /* LimeGreen - Default */
     }

    .pressure-indicator span.medium {
        color: #ff8c00; /* DarkOrange */
         animation: pulse-medium 1.5s infinite ease-in-out;
    }
    .pressure-indicator span.high {
        color: #dc143c; /* Crimson */
         animation: pulse-high 1s infinite ease-in-out;
    }
     .pressure-indicator span.critical {
        color: #ff0000; /* Red */
        animation: pulse-critical 0.8s infinite ease-in-out;
     }

     @keyframes pulse-medium { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
     @keyframes pulse-high { 0% { transform: scale(1); } 50% { transform: scale(1.08); } 100% { transform: scale(1); } }
     @keyframes pulse-critical { 0% { transform: scale(1); } 50% { transform: scale(1.12); } 100% { transform: scale(1); } }


    .weak-point {
        position: absolute;
        top: 100px; /* Just above the impermeable layer */
        left: 48%; /* Centered */
        width: 4%;
        height: 220px; /* Extends through layers */
        background-color: rgba(255, 50, 50, 0.3); /* More vibrant red transparency */
        z-index: 8; /* Below conduit, above layers */
        display: none; /* Hidden by default */
        transform-origin: top center;
        transform: rotate(3deg); /* Representing a subtle fault */
        border-left: 3px dashed rgba(255, 0, 0, 0.6);
        border-right: 3px dashed rgba(255, 0, 0, 0.6);
         transition: opacity 0.5s ease-in-out;
    }

    .weak-point.high-risk {
         animation: weak-point-pulse 1s infinite alternate;
    }

    @keyframes weak-point-pulse {
        from { opacity: 1; }
        to { opacity: 0.6; }
    }


    .conduit {
        position: absolute;
        top: 15px; /* Starts just below the surface */
        left: 49%; /* Centered */
        width: 2%; /* Thinner conduit */
        height: 305px; /* Extends down to bottom of trapped zone (320px - 15px surface) */
        background-color: rgba(100, 50, 0, 0.8); /* Darker, richer brown */
        z-index: 9; /* Above weak point */
        display: none; /* Hidden by default */
        overflow: hidden;
         border-radius: 4px;
         box-shadow: 0 0 8px rgba(100, 50, 0, 0.5);
         transition: height 0.5s ease-out; /* Animate if height changes */
    }

    .conduit::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 200%; /* Make the pattern longer for smoother loop */
        background: repeating-linear-gradient(
            to bottom,
            rgba(139, 69, 19, 0.9),
            rgba(139, 69, 19, 0.9) 15px,
            rgba(0, 0, 0, 0.1) 15px,
            rgba(0, 0, 0, 0.1) 30px
        );
        animation: mudflow 1s linear infinite; /* Faster animation */
    }

    @keyframes mudflow {
        from { background-position: 0 0; }
        to { background-position: 0 60px; } /* Adjusted based on gradient size */
    }

     .surface-eruption-effect {
        position: absolute;
        bottom: -5px; /* Position just above surface bottom */
        left: 48%;
        width: 4%; /* Match conduit width approx */
        height: 15px; /* Match surface height */
        background: radial-gradient(circle, rgba(139, 69, 19, 0.8) 20%, transparent 80%);
        z-index: 11; /* Above surface */
        display: none;
        animation: mud-bubble 1.5s infinite ease-out;
         transform: translateX(-50%);
     }

     @keyframes mud-bubble {
         0% { transform: translateX(-50%) scale(0.5); opacity: 0.5; }
         50% { transform: translateX(-50%) scale(1.2); opacity: 1; }
         100% { transform: translateX(-50%) scale(0.5); opacity: 0.5; }
     }


    .mud-cone {
        position: absolute;
        bottom: 440px; /* Positioned just above the simulation area bottom (450 - 10px) */
        left: 50%;
        transform: translateX(-50%) translateY(100%); /* Start off-screen below where it will land */
        width: 0px; /* Starts small */
        height: 0px;
        background-color: rgba(100, 50, 0, 0.95); /* Darker, prominent brown */
        clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
        z-index: 12; /* Above conduit and surface effects */
        display: none; /* Hidden by default */
        transition: width 1.5s ease-out, height 1.5s ease-out, transform 1.5s ease-out; /* Smoother growth */
        transform-origin: bottom center;
         box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }

    .mud-cone.erupting {
         transform: translateX(-50%) translateY(0%); /* Move into position */
    }


    .controls-panel {
        width: 95%;
        padding: 20px;
        background-color: #ffffff; /* White panel background */
        border: 1px solid #d0d0d0;
        border-radius: 8px;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05);
        text-align: center;
         margin-bottom: 15px;
    }

    .controls-panel h3 {
        color: #4a3a2a; /* Match border color */
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.3em;
    }

    .control-group {
         display: flex;
         align-items: center;
         margin-bottom: 15px;
         justify-content: center; /* Center controls */
    }

    .controls-panel label {
        display: inline-block;
        margin-bottom: 0; /* Removed bottom margin */
        font-weight: bold;
        width: 250px; /* Fixed width for alignment */
        text-align: right;
        margin-right: 15px;
        font-size: 1em;
        color: #555;
    }

    .controls-panel input[type="range"] {
        flex-grow: 1; /* Allow slider to take available space */
        max-width: 200px; /* Max width for slider */
        vertical-align: middle;
        margin-right: 10px;
    }
     .controls-panel input[type="checkbox"] {
         margin-left: 10px;
         transform: scale(1.3); /* Slightly larger checkbox */
     }


    .controls-panel span {
        font-weight: normal;
        min-width: 30px; /* Ensure alignment of values */
        text-align: left;
    }

    .simulation-hint {
        font-size: 0.9em;
        color: #666;
        margin-top: 0;
        text-align: center;
    }


    #toggle-explanation-button {
        display: block;
        width: 250px; /* Wider button */
        margin: 20px auto;
        padding: 12px; /* More padding */
        text-align: center;
        background-color: #1e90ff; /* DodgerBlue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

     #toggle-explanation-button:hover {
        background-color: #007bb5;
        transform: translateY(-1px);
     }
      #toggle-explanation-button:active {
        background-color: #005f8a;
        transform: translateY(1px);
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
      }


    #explanation {
        margin-top: 30px; /* More space */
        padding: 20px;
        border: 1px solid #d0d0d0;
        border-radius: 12px;
        background-color: #fdfdfd; /* Very light background */
        display: none; /* Hidden by default */
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
         max-width: 800px;
         margin-left: auto;
         margin-right: auto;
    }

    #explanation h2 {
        color: #4a3a2a; /* Match theme */
        border-bottom: 2px solid #1e90ff; /* Match button color */
        padding-bottom: 8px;
        margin-top: 15px;
        font-size: 1.6em;
    }

     #explanation h3 {
        color: #5a4a8c; /* Match impermeable layer */
        margin-top: 15px;
        margin-bottom: 8px;
        font-size: 1.3em;
     }

     #explanation p, #explanation ul {
        line-height: 1.7; /* Increased line spacing */
        margin-bottom: 15px; /* More space between paragraphs/lists */
        color: #444;
        font-size: 1.05em;
     }

     #explanation ul {
        padding-left: 30px; /* Increased padding */
     }

      #explanation li {
          margin-bottom: 8px;
      }
</style>

<button id="toggle-explanation-button">מה עומד מאחורי התופעה? הסבר מלא</button>

<div id="explanation">
    <h2>קסם הרי הגעש הבוציים: לא מה שחשבתם!</h2>
    <p>שלא כמו אחיהם המפורסמים שפולטים לבה לוהטת מהמעמקים הרותחים של כדור הארץ, הרי געש בוציים הם תופעה "קרה". הם מתפרצים ללא חום גבוה משמעותי (בדרך כלל הטמפרטורה זהה לטמפרטורת הסביבה או מעט חמה יותר), ופולטים תערובת מרתקת של בוץ, מים וגזים, שמקורה בשכבות סלע ומשקע קבורות עמוק תחתנו.</p>

    <h2>מסע בעקבות הרי הגעש הבוציים: איפה הם אורבים?</h2>
    <p>הרי געש בוציים אינם נדירים כלל! הם מעדיפים להופיע באזורים גיאולוגיים מסוימים, בעיקר כאלה עם אגני משקע עמוקים שבהם הצטברו כמויות אדירות של בוץ וחומר אורגני לאורך מיליוני שנים. אזורי התנגשות לוחות טקטוניים (אזורי הפחתה), או אזורים עשירים במאגרי נפט וגז טבעי, הם מועמדים עיקריים, שכן הם מספקים את התנאים המושלמים: חומר גלם (משקעים), כוח דוחף (לחץ טקטוני), ודלק (גז מתאן שנוצר מפירוק חומר אורגני).</p>
    <ul>
        <li><strong>מוקדים גלובליים:</strong> אזרבייג'ן מחזיקה בתואר "ארץ הרי הגעש הבוציים" עם אלפיים מהם, אך ניתן למצוא אותם גם באינדונזיה, טרינידד וטובגו, איטליה, קליפורניה (ארה"ב), פקיסטן, ובמקומות רבים נוספים, כולל במעמקי הים.</li>
    </ul>

    <h2>המנוע הסודי: לחץ יתר (Overpressure)</h2>
    <p>מה גורם לבוץ הזה לפרוץ החוצה? הסיבה היא הצטברות אדירה של לחץ תת-קרקעי, המכונה לחץ יתר. דמיינו בקבוק שמפניה סגור היטב – הגז והנוזל בפנים נדחסים, והלחץ עולה. בהרי געש בוציים, ה"בקבוק" הוא קרום כדור הארץ, וה"שמפניה" הם נוזלים וגזים שנלכדים מתחת לשכבות אטומות. הלחץ הזה נבנה מכמה גורמים מרכזיים:</p>
    <h3>מקורות הלחץ התת-קרקעי:</h3>
    <ul>
        <li><strong>עומס השכבות (Lithostatic Load):</strong> פשוט כובד! שכבות משקע חדשות שנקברות מעל דוחסות בכוח את השכבות התחתונות יותר, סוחטות מהן נוזלים וגזים ומגבירות את הלחץ.</li>
        <li><strong>ייצור גזים (מתאן הוא הכוכב):</strong> עמוק למטה, חומר אורגני (שרידי צמחים ובעלי חיים ימיים) עובר תהליכי פירוק. התוצר העיקרי? גז מתאן. גז זה מצטבר, יוצר בועות, ומוסיף נפח ולחץ עצום למערכת.</li>
        <li><strong>שחרור מים ממינרלים (Dehydration):</strong> סלעי משקע מכילים מינרלים שבנויים עם מים כלואים בתוכם. כאשר סלעים אלו נקברים עמוק יותר והטמפרטורה עולה מעט (אפילו עשרות מעלות בודדות), המים האלה משתחררים, ומגדילים עוד יותר את נפח הנוזלים והלחץ הכלוא.</li>
    </ul>
    <p>כאשר נוזלים וגזים אלו נתקלים בשכבה אטומה (כמו סלע חרסית דחוס מאוד או סלע גיר בלתי חדיר), הם נלכדים ואין להם לאן לברוח. הלחץ ממשיך לגדול, לפעמים עד שהוא עולה על הלחץ של כל הסלע שמעל, ואף על חוזק הסלע עצמו!</p>

    <h2>רגע ההתפרצות: הסיפור המלא</h2>
    <ol>
        <li><strong>בניית המתח:</strong> הלחץ הכלוא עולה ועולה, דוחף כנגד ה"פקק" האטום שמעליו.</li>
        <li><strong>פריצת הדרך:</strong> כשהלחץ מגיע לשיא, הוא חייב למצוא נתיב בריחה. הוא "מחפש" את נקודות התורפה בקרום - אלה יכולים להיות סדקים קיימים, העתקים גיאולוגיים שבהם הסלע מרוסק, או אפילו סדקים חדשים שהלחץ עצמו יוצר בכוח (שבירה הידראולית).</li>
        <li><strong>המסע כלפי מעלה:</strong> ברגע שנפתח נתיב, הנוזלים והגזים בלחץ העצום מזנקים כלפי מעלה במהירות, כאילו נפתחה פתאום פקק השמפניה.</li>
        <li><strong>הפיכה לבוץ:</strong> בדרכם למעלה, הנוזלים והגזים פוגשים וסוחפים איתם חומר משקע רך (בעיקר חרסית וסילט) מהשכבות שהם חוצים. הם מערבלים את החומר הזה עם המים והגז, ויוצרים תערובת סמיכה דמוית דייסה – ה"בוץ" הגעשי.</li>
        <li><strong>ההתפרצות:</strong> הלחץ דוחף את תערובת הבוץ והגז אל פני השטח דרך הפתח שנוצר. פליטת הגז יכולה להיות אלימה מאוד, ולפעמים הגז (בעיקר מתאן) נדלק ויוצר להבות קבועות או התלקחויות נקודתיות!</li>
        <li><strong>בניית הנוף:</strong> הבוץ שנפלט מתייבש סביב הפתח ומצטבר, ועם הזמן בונה מבנה שמזכיר הר געש קטן – קונוס בוץ. לפעמים הוא יוצר מישורי בוץ רחבים או סלסלות בוץ מבעבעות.</li>
    </ol>

    <h2>הרי געש בוציים: לא רק סקרנות גיאולוגית</h2>
    <p>הרי געש בוציים הם יותר מסתם תופעה מוזרה. הם מעבדות טבעיות לחקר מעמקי כדור הארץ, חלון הצצה לתהליכים גיאולוגיים המתרחשים הרחק מתחת לרגלינו. הפליטות שלהם מכילות לעיתים קרובות גז טבעי ואף נפט, מה שהופך אותם לאינדיקטורים חשובים לחיפושי אנרגיה. עם זאת, הם יכולים להיות גם מסוכנים, ולגרום נזק לתשתיות וסביבה בעת התפרצויות גדולות.</p>
</div>

<script>
    const sedimentLoadInput = document.getElementById('sediment-load');
    const sedimentLoadValueSpan = document.getElementById('sediment-load-value');
    const fluidGasInput = document.getElementById('fluid-gas-volume');
    const fluidGasValueSpan = document.getElementById('fluid-gas-volume-value');
    const weakPointCheckbox = document.getElementById('weak-point-present');

    const trappedFluidsGasDiv = document.querySelector('.trapped-fluids-gas');
    const pressureValueSpan = document.getElementById('pressure-value');
    const weakPointDiv = document.querySelector('.weak-point');
    const conduitDiv = document.querySelector('.conduit');
    const mudConeDiv = document.querySelector('.mud-cone');
    const surfaceEruptionEffectDiv = document.querySelector('.surface-eruption-effect');

    const toggleExplanationButton = document.getElementById('toggle-explanation-button');
    const explanationDiv = document.getElementById('explanation');

    const basePressure = 10; // Minimal inherent pressure
    const loadFactor = 0.5; // How much load contributes to pressure (increased)
    const fluidGasFactor = 0.7; // How much fluid/gas contributes to pressure (increased)
    const eruptionThreshold = 70; // Pressure needed to erupt (if weak point exists) - Increased for challenge
    const highRiskThreshold = 50; // Pressure level showing risk

    let currentPressure = 0;

    function updateSimulation() {
        const load = parseInt(sedimentLoadInput.value);
        const fluidGas = parseInt(fluidGasInput.value);
        const weakPoint = weakPointCheckbox.checked;

        sedimentLoadValueSpan.textContent = load;
        fluidGasValueSpan.textContent = fluidGas;

        // Calculate pressure (improved scaling)
        currentPressure = basePressure + (load * loadFactor * 0.8) + (fluidGas * fluidGasFactor * 1.2); // Fluid/Gas has more impact

        const pressurePercent = Math.min(100, Math.max(0, Math.round(currentPressure))); // Clamp between 0 and 100

        pressureValueSpan.textContent = pressurePercent + '%';

        // Update pressure indicator color and animation
        pressureValueSpan.classList.remove('medium', 'high', 'critical');
        if (pressurePercent > eruptionThreshold - 10 && pressurePercent <= eruptionThreshold + 10) {
            pressureValueSpan.classList.add('high');
        } else if (pressurePercent > eruptionThreshold + 10) {
             pressureValueSpan.classList.add('critical');
        } else if (pressurePercent > highRiskThreshold) {
            pressureValueSpan.classList.add('medium');
        }


        // Update fluid/gas visualization height and color hint
        const fluidHeightPercent = Math.min(100, Math.max(0, fluidGas)); // Simple 1:1 scaling for visualization
        trappedFluidsGasDiv.style.height = fluidHeightPercent + '%';

        // Optional: Change background of trapped zone based on pressure (subtle)
        const trappedZone = document.querySelector('.trapped-zone');
         const pressureColorIntensity = Math.min(1, (currentPressure - basePressure) / (100 - basePressure));
         trappedZone.style.backgroundColor = `rgb(${210 + pressureColorIntensity * 45}, ${180 - pressureColorIntensity * 30}, ${140 - pressureColorIntensity * 40})`; // Shift towards slightly redder/darker

        // Weak point visibility and risk indication
        if (weakPoint) {
             weakPointDiv.style.display = 'block';
             if (currentPressure >= highRiskThreshold) {
                 weakPointDiv.classList.add('high-risk');
             } else {
                 weakPointDiv.classList.remove('high-risk');
             }
        } else {
             weakPointDiv.style.display = 'none';
             weakPointDiv.classList.remove('high-risk');
        }


        // Eruption Logic
        if (currentPressure >= eruptionThreshold && weakPoint) {
             // Start eruption sequence (if not already erupting)
             if (conduitDiv.style.display === 'none') {
                 conduitDiv.style.display = 'block';
                 surfaceEruptionEffectDiv.style.display = 'block';
                 mudConeDiv.style.display = 'block'; // Make it visible instantly but off-screen

                 // Animate cone growth after a short delay
                 setTimeout(() => {
                     mudConeDiv.classList.add('erupting'); // Trigger the translateY and size transition
                     mudConeDiv.style.width = '120px'; // Final cone width (larger)
                     mudConeDiv.style.height = '80px'; // Final cone height (larger)
                 }, 100); // Delay slightly after conduit appears

             }
             // Ensure conduit animation is running (handled by CSS animation-play-state if paused)


        } else {
             // Stop eruption sequence
             if (mudConeDiv.classList.contains('erupting')) {
                  // Animate cone shrinking before hiding
                 mudConeDiv.classList.remove('erupting');
                 mudConeDiv.style.width = '0px';
                 mudConeDiv.style.height = '0px';
                 // Hide after transition
                 setTimeout(() => {
                      mudConeDiv.style.display = 'none';
                 }, 1500); // Match cone transition duration

             } else {
                  // If not erupting but visible (shouldn't happen with current logic, but good cleanup)
                 mudConeDiv.style.display = 'none';
             }
             conduitDiv.style.display = 'none';
             surfaceEruptionEffectDiv.style.display = 'none';
        }
    }

    // Initial state setup
    updateSimulation();

    // Event listeners for controls - Update live
    sedimentLoadInput.addEventListener('input', updateSimulation);
    fluidGasInput.addEventListener('input', updateSimulation);
    weakPointCheckbox.addEventListener('change', updateSimulation);


    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'מה עומד מאחורי התופעה? הסבר מלא';
    });


</script>
```