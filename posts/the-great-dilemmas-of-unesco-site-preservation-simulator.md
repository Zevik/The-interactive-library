---
title: "דילמת פורטה מארה: סימולטור הצלת אתר מורשת"
english_slug: the-great-dilemmas-of-unesco-site-preservation-simulator
category: "אקולוגיה"
tags:
  - אונסק"ו
  - שימור אתרים
  - קבלת החלטות
  - מורשת עולמית
  - ניהול משאבים
---
# דילמת פורטה מארה: סימולטור הצלת אתר מורשת עולמית

דמיינו את עצמכם בחדר הדיונים המתוח של ועדת המורשת העולמית של אונסק"ו. על המסך מופיעה תמונה אווירית של עיירת חוף עתיקה, יפהפייה אך שוקעת. מי הים כבר נושקים לחומותיה, והצפות הן עניין של יום-יום. זו "פורטה מארה", אתר מורשת עולמית בסכנה קיומית מיידית.

המשימה שלכם: לקבל החלטה גורלית. האם להשקיע מיליארדים בניסיון להילחם בטבע? האם לוותר על האתר כולו כדי להציל את התושבים ופיסות היסטוריה? או אולי לחפש פתרון ביניים יצירתי אך לא ודאי? לכל החלטה שלכם יהיו השלכות דרמטיות – כלכליות, חברתיות, סביבתיות ותרבותיות.

איך תפעלו?

<div id="app-container" class="simulator-container">
    <div class="scenario-description">
        <h2>מקרה מבחן: העיר העתיקה "פורטה מארה"</h2>
        <p>העיר פורטה מארה, פנינת ארכיטקטורה עתיקה השוכנת לחופי ים תיכון, הוכרזה לפני 30 שנה כאתר מורשת עולמית בזכות מבניה הייחודיים, נמל הדייגים ההיסטורי בן אלפי השנים, ופסלי שיש רומיים מרהיבים. אך פניה השתנו. כיום, כתוצאה ישירה מעליית מפלס הים והתגברות אירועי מזג אוויר קיצוניים, יסודות רבים מהמבנים ההיסטוריים סובלים מבליה קשה וחלקי העיר הנמוכים כבר נמצאים מתחת למים באופן קבוע. כ-5,000 תושבים עדיין מתגוררים באזור הסיכון הגבוה, שגרת חייהם משובשת, ופרנסתם (בעיקר מדיג ותיירות) בסכנה. הרשויות המקומיות והארציות חסרות משאבים ויכולת פעולה משמעותית.</p>

        <h3>הדילמה הקריטית: איך מצילים את פורטה מארה (ואת תושביה)?</h3>
        <p>כחברי צוות המומחים הבכיר של אונסק"ו, עליכם להמליץ על דרך פעולה מרכזית וברורה. זכרו, אין כאן פתרון קסם – לכל אפשרות שתבחרו יש יתרונות וחסרונות מהותיים שישפיעו על כל המעורבים והיבטי המקרה:</p>
    </div>

    <div class="options-container">
        <div class="option-card" data-option="A">
            <input type="radio" id="optionA" name="decision" value="A">
            <label for="optionA">
                <span class="option-title">אפשרות א': הנדסה אקלימית - בניית סכר ענק וחיזוק תשתיות פיזיות.</span>
                <span class="option-subtitle">להילחם בים בכל הכוח.</span>
            </label>
            <div class="consequences-list">
                <h4>השלכות פוטנציאליות:</h4>
                <ul>
                    <li><span class="dimension">עלות כלכלית:</span> <strong>גבוהה מאוד</strong> (בנייה עצומה, תחזוקה אינסופית).</li>
                    <li><span class="dimension">על הקהילה:</span> <strong>נמוכה בטווח הקצר</strong> (תושבים נשארים במקומם).</li>
                    <li><span class="dimension">יעילות בשימור:</span> <strong>גבוהה בטווח הקצר-בינוני</strong> (הגנה פיזית מיידית).</li>
                    <li><span class="dimension">השפעה סביבתית:</span> <strong>דרמטית</strong> (שינוי רדיקלי של המערכת האקולוגית הימית והחוף).</li>
                    <li><span class="dimension">תמיכה פוליטית:</span> <strong>גבוהה</strong> (פתרון 'מוחשי' ומרשים).</li>
                </ul>
            </div>
        </div>

        <div class="option-card" data-option="B">
            <input type="radio" id="optionB" name="decision" value="B">
            <label for="optionB">
                 <span class="option-title">אפשרות ב': 'נסיגה מתוכננת' - פינוי הדרגתי של התושבים והתמקדות בחילוץ ממצאים.</span>
                 <span class="option-subtitle">לוותר על העיר, להציל את ההיסטוריה המוחשית.</span>
            </label>
            <div class="consequences-list">
                <h4>השלכות פוטנציאליות:</h4>
                <ul>
                    <li><span class="dimension">עלות כלכלית:</span> <strong>בינונית-גבוהה</strong> (עלויות פינוי, פיצויים, מבצע ארכיאולוגי).</li>
                    <li><span class="dimension">על הקהילה:</span> <strong>הרסנית</strong> (עקירה, אובדן בית, פרנסה ומורשת חיה).</li>
                    <li><span class="dimension">יעילות בשימור:</span> <strong>נמוכה לשלמות האתר</strong> (העיר כולה אובדת), <strong>גבוהה לממצאים</strong> (הצלת ארטיפקטים).</li>
                    <li><span class="dimension">השפעה סביבתית:</span> <strong>נמוכה</strong> (הטבע 'מקבל בחזרה' את השטח).</li>
                    <li><span class="dimension">תמיכה פוליטית:</span> <strong>נמוכה מאוד</strong> (פתרון לא פופולרי לחלוטין).</li>
                </ul>
            </div>
        </div>

        <div class="option-card" data-option="C">
            <input type="radio" id="optionC" name="decision" value="C">
            <label for="optionC">
                <span class="option-title">אפשרות ג': ניהול גמיש - שילוב תיירות בת-קיימא מוגבלת וטכנולוגיות הגנה מקומיות.</span>
                <span class="option-subtitle">לחיות לצד האיום, לקנות זמן.</span>
            </label>
            <div class="consequences-list">
                <h4>השלכות פוטנציאליות:</h4>
                <ul>
                    <li><span class="dimension">עלות כלכלית:</span> <strong>בינונית</strong> (פיתוח תיירות, רכישת טכנולוגיה, תחזוקה שוטפת).</li>
                    <li><span class="dimension">על הקהילה:</span> <strong>בינונית</strong> (הזדמנויות תיירותיות לצד מגבלות).</li>
                    <li><span class="dimension">יעילות בשימור:</span> <strong>בינונית</strong> (פתרון זמני, לא מתמודד עם הבעיה היסודית לטווח ארוך).</li>
                    <li><span class="dimension">השפעה סביבתית:</span> <strong>בינונית</strong> (השפעת התיירות, שימוש בחומרים).</li>
                    <li><span class="dimension">תמיכה פוליטית:</span> <strong>בינונית</strong> (דורש שיתוף פעולה והשקעה מקומית מתמשכת).</li>
                </ul>
            </div>
        </div>
    </div>

    <button id="submit-decision">שלח החלטה גורלית!</button>

    <div id="results" class="results-section hidden">
        <h3>תוצאות ההחלטה שבחרת:</h3>
        <div id="result-summary"></div>
        <div id="impact-breakdown">
            <h4>השפעה על המדדים המרכזיים:</h4>
            <ul id="impact-list">
                <!-- JS will populate this -->
            </ul>
        </div>
        <p class="reflection-text">כפי שראיתם, קבלת החלטות בשימור אתרי מורשת עולמית היא תמיד מאזן מורכב ולעיתים כואב, בין שימור האבן להישרדות האדם, בין כלכלה לאקולוגיה, ובין אינטרסים גלובליים למקומיים. לעיתים קרובות, אין פתרון 'מושלם'.</p>
    </div>
</div>

<style>
    /* General Styles */
    #app-container.simulator-container {
        font-family: 'Arial', sans-serif; /* More standard font */
        line-height: 1.7;
        max-width: 850px; /* Slightly wider for better layout */
        margin: 20px auto;
        padding: 30px;
        border: none; /* Remove default border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient background */
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1); /* More pronounced shadow */
        color: #333;
        direction: rtl; /* Ensure RTL for Hebrew */
        text-align: right; /* Ensure text aligns right */
    }

    #app-container h2, #app-container h3, #app-container h4 {
        color: #0056b3; /* Deep blue for headings */
        border-bottom: 2px solid #0056b3; /* Thicker, colored border */
        padding-bottom: 12px;
        margin-bottom: 20px;
        text-align: right;
    }

    #app-container h2 {
        color: #004085; /* Even deeper blue for main title */
        margin-top: 0;
    }

    .scenario-description p {
        margin-bottom: 15px;
        color: #555;
    }

    /* Options Styling */
    .options-container {
        display: grid; /* Use Grid for layout */
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Responsive grid */
        gap: 25px; /* Space between cards */
        margin-top: 30px;
    }

    .option-card {
        background-color: #ffffff;
        border: 1px solid #b2ebf2; /* Light blue border */
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05); /* Subtle shadow for cards */
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        cursor: pointer;
        position: relative; /* For radio button positioning */
        display: flex; /* Use flex to align content */
        flex-direction: column; /* Stack content */
    }

    .option-card:hover {
        transform: translateY(-5px); /* Lift effect on hover */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        border-color: #007bff; /* Highlight border on hover */
    }

     .option-card input[type="radio"] {
        position: absolute;
        top: 15px; /* Position top-left */
        right: 15px; /* Adjust for RTL */
        z-index: 1; /* Ensure clickable */
        cursor: pointer;
        width: 20px;
        height: 20px;
     }

    .option-card label {
        font-weight: bold;
        color: #007bff; /* Primary color for titles */
        margin-bottom: 10px;
        cursor: pointer; /* Indicate clickable area */
        flex-grow: 1; /* Allow label to take space */
        display: flex;
        flex-direction: column;
        padding-right: 30px; /* Space for radio button */
    }

    .option-title {
        font-size: 1.1em;
        margin-bottom: 5px;
        color: #0056b3; /* Darker blue */
    }
     .option-subtitle {
         font-size: 0.9em;
         font-weight: normal;
         color: #666;
     }

    .option-card:has(input:checked) {
        border-color: #28a745; /* Green border when checked */
        box-shadow: 0 4px 20px rgba(40, 167, 69, 0.2); /* Green shadow */
        background-color: #e9ffef; /* Very light green background */
    }

    .consequences-list {
        margin-top: 15px;
        font-size: 0.95em;
        color: #555;
        border-top: 1px solid #eee;
        padding-top: 15px;
    }
    .consequences-list h4 {
        color: #555; /* Dimmer color for consequence title */
        border-bottom: none;
        padding-bottom: 0;
        margin-bottom: 8px;
        font-size: 1em;
    }

    .consequences-list ul {
        margin-top: 0;
        padding-left: 0; /* Remove default padding */
        list-style: none; /* Remove bullets */
    }
    .consequences-list li {
        margin-bottom: 8px;
        padding-right: 15px; /* Space for custom bullet/icon */
        position: relative;
    }
     .consequences-list li:before {
         content: '•'; /* Custom bullet point */
         position: absolute;
         right: 0;
         color: #007bff; /* Color bullet */
         font-weight: bold;
     }

    .dimension {
        font-weight: bold;
        color: #0056b3; /* Blue color for dimension */
    }
    .consequences-list strong {
        color: #333; /* Color for consequence level */
    }


    /* Button Styling */
    button {
        display: block; /* Make button a block element */
        width: fit-content; /* Size based on content */
        min-width: 200px; /* Minimum width */
        margin: 30px auto 20px auto; /* Center the button */
        background-color: #007bff; /* Primary blue */
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0, 123, 255, 0.3);
    }

    button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        box-shadow: 0 6px 20px rgba(0, 123, 255, 0.4);
    }

    button:active {
        transform: scale(0.98); /* Slightly shrink on click */
    }


    /* Results Section Styling */
    .results-section {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #28a745; /* Green border */
        border-radius: 10px;
        background-color: #d4edda; /* Light green background */
        color: #155724; /* Dark green text */
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start slightly lower */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
        text-align: right;
    }

    .results-section.visible {
        opacity: 1;
        transform: translateY(0);
    }

    .results-section h3 {
        color: #155724; /* Dark green heading */
        border-bottom-color: #28a745; /* Green border */
    }
     .results-section h4 {
         color: #155724; /* Dark green heading */
         border-bottom: none;
         margin-bottom: 10px;
     }

    #result-summary {
        font-weight: bold;
        color: #0d4636; /* Even darker green */
        margin-bottom: 20px;
        font-size: 1.1em;
    }

    #impact-breakdown {
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px dashed #28a745;
    }

    #impact-list {
         list-style: none;
         padding: 0;
         margin-top: 10px;
    }
    #impact-list li {
        margin-bottom: 8px;
        position: relative;
        padding-right: 25px; /* Space for icon */
        display: flex; /* Use flex to align label and level */
        justify-content: space-between; /* Space out label and level */
        align-items: center; /* Vertically center */
    }
     #impact-list li:before {
         content: ''; /* Remove default bullet */
         display: inline-block;
         width: 15px;
         height: 15px;
         border-radius: 50%;
         position: absolute;
         right: 0;
         top: 50%;
         transform: translateY(-50%);
     }
     .dimension-label {
         font-weight: bold;
         color: #155724;
         flex-grow: 1; /* Allow label to take space */
     }
     .impact-level {
         font-weight: bold;
         text-align: left; /* Align level text left */
         min-width: 80px; /* Ensure consistent width */
     }

     /* Impact color coding */
     #impact-list li:before { background-color: #ccc; } /* Default grey */
     #impact-list li.impact-low:before { background-color: #28a745; } /* Green */
     #impact-list li.impact-medium:before { background-color: #ffc107; } /* Yellow */
     #impact-list li.impact-high:before,
     #impact-list li.impact-dramatic:before,
     #impact-list li.impact-ruinous:before { background-color: #dc3545; } /* Red */
     #impact-list li.impact-high-short:before,
     #impact-list li.impact-low-long:before { background-color: #ffc107; } /* Yellow/Orange for mixed results */


    .reflection-text {
        margin-top: 20px;
        font-style: italic;
        color: #0d4636;
    }

    .hidden {
        display: none;
    }

    /* Explanation Section */
    #explanation-button {
        margin-top: 30px;
        background-color: #6c757d; /* Grey color for secondary button */
        box-shadow: 0 5px 15px rgba(108, 117, 125, 0.3);
    }
     #explanation-button:hover {
         background-color: #5a6268;
         box-shadow: 0 6px 20px rgba(108, 117, 125, 0.4);
     }


    #full-explanation {
        margin-top: 30px;
        padding-top: 30px;
        border-top: 2px solid #0056b3; /* Match heading border */
        text-align: right;
    }

    #full-explanation h3 {
        color: #0056b3;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    #full-explanation p {
        margin-bottom: 15px;
        color: #555;
    }
     #full-explanation ul {
         padding-right: 20px; /* RTL list padding */
         color: #555;
     }
     #full-explanation li {
         margin-bottom: 8px;
     }
     #full-explanation li strong {
         color: #333;
     }
</style>

<button id="explanation-button">רוצים להבין לעומק? הצגת רקע והסבר מורחב</button>

<div id="full-explanation" class="hidden">
    <h2>הסבר מורחב: אונסק"ו ושימור אתרי מורשת עולמית</h2>

    <h3>מהם אתרי מורשת עולמית וכיצד הם מוגדרים?</h3>
    <p>אתרי מורשת עולמית הם מקומות בעלי ערך אוניברסלי יוצא דופן, כפי שנקבע על ידי ועדת המורשת העולמית של אונסק"ו. אתרים אלו יכולים להיות טבעיים (יערות עתיקים, רכסי הרים דרמטיים, אגמים ייחודיים) או תרבותיים (מבנים היסטוריים, ערים עתיקות, אתרים ארכיאולוגיים מרשימים). ההכרה נועדה להבטיח את שימורם לדורות הבאים באמצעות שיתוף פעולה בינלאומי. תהליך ההכרזה כולל הגשת מועמדות מפורטת ומנומקת על ידי המדינה החברה שבה נמצא האתר, הערכה מקיפה ומעמיקה על ידי גופים מייעצים מובילים (כמו ICOMOS לתרבות ו-IUCN לטבע), ולבסוף דיון והחלטה בוועדת המורשת העולמית, המורכבת מנציגי 21 מדינות.</p>

    <h3>מדוע אתרים אלו חשופים לאיומים שונים ומגוונים (אקלים, פיתוח, סכסוך, תיירות)?</h3>
    <p>איומים על אתרי מורשת נובעים משילוב קטלני של גורמים טבעיים (שפעוליהם לעיתים מואצים על ידי האדם) ומעשה ידי אדם. **שינויי אקלים** גורמים לעליית מפלס הים המאיימת על אתרי חוף ונמלים היסטוריים, הגברת אירועי מזג אוויר קיצוניים (סופות, בצורות, גלי חום) הפוגעים במבנים ומערכות אקולוגיות, והתחממות והחמצת אוקיינוסים הפוגעים בשוניות אלמוגים ואתרים תת-ימיים. **פיתוח מואץ**, כמו בניית תשתיות ענק (כבישים מהירים, סכרים הידרואלקטריים) או התרחבות אורבנית בלתי מבוקרת, עלול להרוס פיזית אתרים או לפגוע באופן בלתי הפיך בסביבה הקרובה שלהם וב"אזור החיץ" המגן עליהם. **סכסוכים צבאיים** לצערנו הופכים אתרים היסטוריים למטרות או לשדות קרב, ועלולים להוביל להרס מכוון (כמעשה טרור תרבותי) או מקרי, ובמקרים רבים גם לביזה וסחר בלתי חוקי בעתיקות. **תיירות יתר**, למרות חשיבותה הכלכלית האדירה, עלולה לגרום לשחיקה פיזית של האתר, עומס אקולוגי על הסביבה, עומס על התשתיות המקומיות, ולפגוע בחוויית המבקרים ובעיקר באותנטיות ובשלמות של האתר והקהילה המקומית.</p>

    <h3>תפקידה המורכב של אונסק"ו: בין שימור גלובלי לאינטרסים מקומיים ולאומיים.</h3>
    <p>תפקידה המרכזי של אונסק"ו הוא לסייע למדינות החברות לשמר ולהגן על אתרים אלו, בין היתר באמצעות הקצאת מימון (מקרן המורשת העולמית), תמיכה טכנית, מתן מומחיות וידע, וקידום שיתופי פעולה בינלאומיים. עם זאת, נקודה קריטית שיש לזכור היא שאונסק"ו אינה הבעלים של האתרים – הריבונות והאחריות הניהולית עליהם נשארת באופן מוחלט בידי המדינות שבהן הם נמצאים. הדבר יוצר מורכבות ניהולית ופוליטית גדולה: אונסק"ו יכולה להביע דאגה עמוקה, להמליץ בחום על דרכי פעולה, ואף להכניס אתר ל"רשימת האתרים בסיכון" (מה שעלול להשפיע על תיירות ומוניטין), אך היא תלויה לחלוטין בשיתוף הפעולה, ברצון הטוב וביכולת הביצוע של הממשלות המקומיות והאוכלוסייה החיה בקרבת האתר. לעיתים קרובות קיימים ניגודי עניינים מהותיים בין הצורך בשימור ארוך טווח של אתר בעל ערך אוניברסלי לבין צרכים כלכליים, חברתיים או פוליטיים דחופים ויומיומיים של המדינה או הקהילה המקומית. כאן בדיוק נוצרות הדילמות שפגשתם בסימולטור.</p>

    <h3>ניתוח דילמות מרכזיות: כלכלה מול שימור, פיתוח מול מורשת, זכויות קהילה מול נגישות לאתר.</h3>
    <ul>
        <li>**כלכלה מול שימור:** פרויקטים של שימור ברמה הנדרשת דורשים לעיתים קרובות משאבים כספיים עצומים, שאינם תמיד זמינים, במיוחד במדינות מתפתחות המתמודדות עם אתגרי יסוד. ישנו מתח מתמיד בין הצורך להשקיע בשימור תרבותי/טבעי לטווח ארוך לבין הצורך הדחוף להשקיע בצרכים חיוניים אחרים כמו בריאות הציבור, חינוך, תעסוקה, או פיתוח כלכלי מיידי.</li>
        <li>**פיתוח מול מורשת:** פרויקטי פיתוח מודרניים (תחבורה, אנרגיה, דיור) חיוניים לצמיחה כלכלית ולשיפור איכות החיים של האזרחים, אך הם כמעט תמיד עלולים להתנגש עם הצורך הקפדני להגן על השלמות הפיזית, הוויזואלית והאקולוגית של האתר וסביבתו הקרובה.</li>
        <li>**זכויות קהילה מול נגישות לאתר:** במקרים רבים, אתרי מורשת הם גם הבית ומרכז החיים של קהילות מקומיות החיות במקום לעיתים מאות ואלפי שנים. החלטות שימור קשות (כמו הגבלת גישה לאתר, הגבלת בנייה ופיתוח מקומי, או במקרים קיצוניים אפילו פינוי) עלולות לפגוע באופן קשה בזכויותיהן, באורח חייהן, ובתחושת השייכות שלהן למקום. מנגד, הנגשת האתר לציבור הרחב (למשל, לצורך תיירות) חיונית ללגיטימציה של השימור ולפיתוח כלכלי מקומי, אך עלולה כאמור לפגוע הן בשימור הפיזי והן באיכות החיים של הקהילה.</li>
    </ul>

    <h3>כלים ואסטרטגיות לניהול שימור אתרים בעידן המודרני: תכנון, שיתוף ציבורי, הערכת סיכונים וטכנולוגיה.</h3>
    <p>ניהול יעיל ואפקטיבי של אתרי מורשת עולמית דורש כיום גישה הוליסטית ורב-תחומית. זה מתחיל ביצירת **תוכנית ניהול** מקיפה ומפורטת המגדירה את האתגרים הספציפיים של האתר, המטרות ארוכות הטווח לשימורו, ודרכי הפעולה למימושן. **שיתוף הקהילות המקומיות** וכלל בעלי העניין (רשויות, עסקים, ארגונים אזרחיים) בתהליך התכנון והיישום הוא קריטי להשגת הסכמה ותמיכה רחבה בפעולות השימור. **הערכת סיכונים שיטתית** מסייעת לזהות איומים פוטנציאליים (מרעידות אדמה ועד שינויי חקיקה) ולהיערך אליהם מראש. שימוש ב**אזורי חיץ (Buffer zones)** סביב האתר מסייע להגן עליו מפני השפעות חיצוניות של פיתוח או שינויים סביבתיים. ולבסוף, **הטכנולוגיה והמחקר המדעי** ממלאים תפקיד הולך וגובר ומשמעותי בשימור. טכניקות כמו הדמיה תלת-ממדית וסריקה בלייזר (לתיעוד מדויק ושחזור וירטואלי), ניטור באמצעות לווינים ומזל"טים (לזיהוי שינויים ואיומים מרחוק), שימוש בחומרים חדשניים ועמידים לשימור מבנים וארטיפקטים, ומודלים חישוביים לחיזוי השפעות שינויי אקלים – כולם כלים המאפשרים התמודדות יעילה ומתוחכמת יותר עם אתגרי השימור המורכבים של ימינו. המחקר הארכיאולוגי, ההיסטורי, האקולוגי והגיאולוגי ממשיכים להעמיק את הבנתנו את האתרים ואת חשיבותם הייחודית.</p>
</div>

<script>
    document.getElementById('submit-decision').addEventListener('click', function() {
        const selectedOption = document.querySelector('input[name="decision"]:checked');
        const resultsDiv = document.getElementById('results');
        const resultSummary = document.getElementById('result-summary');
        const impactList = document.getElementById('impact-list');

        const resultsData = {
            'A': {
                text: "בחרתם באפשרות בניית סכר ענק וחיזוק תשתיות. בטווח הקצר, הסכר הצליח להגן על חלקים נרחבים מהעיר העתיקה מפני הצפות ואיפשר לתושבים להישאר במקומם. האתר שומר במידה רבה על צורתו המקורית. עם זאת, עלויות הבנייה היו עצומות ועלויות התחזוקה השוטפת מכבידות מאוד על התקציב. השינוי הפיזי האדיר בקו החוף פגע קשות במערכת האקולוגית הימית המקומית ושטחי הדיג המסורתיים הצטמצמו דרמטית, מה שפגע בפרנסת חלק מהקהילה. התמיכה הפוליטית נותרה גבוהה בזכות הפרויקט המרשים, אך היעילות לטווח הארוך מוטלת בספק אל מול קצב עליית מפלס הים העולמי.",
                impacts: {
                    'עלות כלכלית': 'High',
                    'על הקהילה': 'Low-Medium', // Mixed impact due to fishing damage
                    'יעילות בשימור': 'High-Short', // High short term, uncertain long term
                    'השפעה סביבתית': 'Dramatic',
                    'תמיכה פוליטית': 'High'
                }
            },
            'B': {
                text: "בחרתם באפשרות הנסיגה המתוכננת ופינוי התושבים. אלפי התושבים אכן פונו למגורים חלופיים, תהליך שהיה כרוך בקשיים חברתיים, כלכליים ופסיכולוגיים אדירים. הקהילה המקומית ספגה מכה קשה ואבדה את מרכז חייה ואת בסיס פרנסתה. העיר העתיקה עצמה הוצפה ברובה ונהרסה בהדרגה על ידי הים, והפכה בפועל לאתר ארכיאולוגי ימי המצריך צלילה כדי לצפות בו. במקביל, צוותים ארכיאולוגיים הצליחו לחלץ ולשמר מספר ניכר של פסלים, כתובות וממצאים חשובים במוזיאונים. האתר כשלמות אדריכלית ועירונית אבד לנצח, אך חלקים ממורשתו החומרית העיקרית נשמרו לדורות הבאים. התמיכה הפוליטית באזור ובמדינה נמוכה מאוד בעקבות הפגיעה בקהילה ובמוניטין האתר.",
                impacts: {
                    'עלות כלכלית': 'Medium-High',
                    'על הקהילה': 'Ruinous', // Using a stronger term for dramatic negative impact
                    'יעילות בשימור': 'Low-Site / High-Artifacts', // Specific breakdown
                    'השפעה סביבתית': 'Low', // Minimal human intervention left
                    'תמיכה פוליטית': 'Low'
                }
            },
            'C': {
                text: "בחרתם בניהול הגמיש, שילוב תיירות וטכנולוגיה מקומית. תוכנית התיירות המוגבלת והאחראית אכן יצרה מקור הכנסה חדש שאפשר לממן חלק מפעולות השימור השוטפות (תחזוקת משאבות, איטום). הקהילה המקומית שולבה בחלק מפעילויות התיירות והרגישה שותפה לניסיון להציל את ביתה, מה שחיזק את החוסן החברתי. הפתרונות הטכנולוגיים המקומיים הצליחו לקנות זמן משמעותי ולמנוע את ההצפות החמורות ביותר בטווח המיידי, ולהאט את קצב ההידרדרות. עם זאת, האיום היסודי של עליית מפלס הים נותר בעינו והפתרון אינו קבוע – הוא דורש השקעה כספית ותחזוקה עקבית ומתמשכת לשנים ארוכות, ללא ודאות מוחלטת לגבי העתיד הרחוק. התמיכה הפוליטית נותרה בינונית ותלויה ברצון הממשלה להמשיך להשקיע.",
                impacts: {
                    'עלות כלכלית': 'Medium',
                    'על הקהילה': 'Medium', // Mixed - some benefit, some disruption
                    'יעילות בשימור': 'Medium-Temporary', // Buys time, but not permanent
                    'השפעה סביבתית': 'Medium', // Tourism impact, material use
                    'תמיכה פוליטית': 'Medium'
                }
            }
        };

        if (selectedOption) {
            const value = selectedOption.value;
            const chosenData = resultsData[value];

            resultSummary.textContent = chosenData.text;

            // Clear previous impacts
            impactList.innerHTML = '';

            // Populate impact list
            for (const dimension in chosenData.impacts) {
                const impactLevel = chosenData.impacts[dimension];
                const listItem = document.createElement('li');

                // Add class based on the first part of the impact level for coloring
                const impactClass = 'impact-' + impactLevel.toLowerCase().split('-')[0].split('/')[0];

                listItem.classList.add(impactClass); // Add class for CSS before icon
                listItem.innerHTML = `<span class="dimension-label">${dimension}:</span> <span class="impact-level">${impactLevel}</span>`;

                impactList.appendChild(listItem);
            }


            resultsDiv.classList.remove('hidden');
            // Trigger CSS transition by adding a class after a small delay
            setTimeout(() => {
                resultsDiv.classList.add('visible');
            }, 10); // Small delay allows display:none to register first

            // Scroll to results
            resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });

        } else {
            resultSummary.textContent = "אנא בחר אפשרות אחת לפני השליחה.";
            impactList.innerHTML = ''; // Clear impacts if no option selected
            resultsDiv.classList.remove('hidden');
             setTimeout(() => {
                resultsDiv.classList.add('visible');
            }, 10);
            resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    document.getElementById('explanation-button').addEventListener('click', function() {
        const explanationDiv = document.getElementById('full-explanation');
        const button = this;
        if (explanationDiv.classList.contains('hidden')) {
            explanationDiv.classList.remove('hidden');
            button.textContent = 'הסתר רקע והסבר מורחב';
             // Scroll to explanation
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            explanationDiv.classList.add('hidden');
            button.textContent = 'רוצים להבין לעומק? הצגת רקע והסבר מורחב';
             // Optional: scroll back to the top of the simulation container
             document.getElementById('app-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

     // Add event listeners to the option cards to select the radio button when the card is clicked
     document.querySelectorAll('.option-card').forEach(card => {
         card.addEventListener('click', function() {
             const radio = this.querySelector('input[type="radio"]');
             if (radio) {
                 radio.checked = true;
             }
         });
     });

</script>