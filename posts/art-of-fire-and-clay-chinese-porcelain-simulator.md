---
title: "אמנות האש והבוץ: סודות הפורצלן הסיני - סימולטור"
english_slug: art-of-fire-and-clay-chinese-porcelain-simulator
category: "טכנולוגיה / הנדסת חומרים"
tags:
  - פורצלן
  - קאולין
  - קדרות
  - שריפה
  - מדע החומרים
  - היסטוריה של טכנולוגיה
  - כימיה
---
# אמנות האש והבוץ: סודות הפורצלן הסיני

דמיינו מסע אל בטן האדמה, כריית חומרים נדירים, עבודה עדינה של ידי אמן, ולבסוף - רגע האמת בתנור לוהט. כיצד הפכו הסינים לפני מאות שנים בוץ פשוט לאוצר לבן וזוהר שכבש את העולם? הסוד נמצא בריקוד עתיק של חומרים מדויקים ואש בטמפרטורה הנכונה. כל סטייה קטנה - ויצירת המופת הופכת לאבק ואכזבה.

האם תצליחו לשחזר את הקסם? היכנסו לתפקיד רב-אומן קדר ובחנו את גבולות החומר והטמפרטורה!

<div class="porcelain-simulator">
    <h2>סימולטור שריפת פורצלן</h2>
    <p class="simulator-intro">בחר את חומר הגלם ואת תנאי השריפה בתנור, ולחץ על "הפעל את הכבשן" כדי לגלות את התוצאה!</p>
    <div class="simulator-controls">
        <div class="control-group">
            <label for="material">חומר גלם:</label>
            <select id="material">
                <option value="high_purity_kaolin">קאולין טהור במיוחד (הסוד הסיני הקדום)</option>
                <option value="kaolin_with_flux">תערובת קאולין עם תוספות (כמו ממסכים)</option>
                <option value="low_grade_mix">תערובת חימר נפוץ (פחות קאולין)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="temperature">טמפרטורת שריפה (°C):</label>
            <input type="number" id="temperature" value="1300" min="800" max="1600" step="10">
        </div>
        <div class="control-group">
             <label for="time">משך שריפה (שעות):</label>
             <input type="number" id="time" value="8" min="1" max="24">
             <span class="note">(זמן השריפה חשוב במיוחד בטמפרטורות גבוליות!)</span>
        </div>
        <button id="simulate-btn">🔥 הפעל את הכבשן 🔥</button>
    </div>
    <div class="kiln-area">
         <div class="kiln">
             <div class="kiln-door"></div>
             <div class="kiln-interior">
                 <div class="clay-object"></div>
             </div>
             <div class="kiln-heat-effect"></div>
         </div>
    </div>

    <div id="result-area" class="simulator-result">
        <div class="result-icon"></div>
        <p class="result-text">לחץ על "הפעל את הכבשן" כדי לראות את התוצאה של הניסוי!</p>
    </div>
</div>

<style>
    :root {
        --color-primary: #4a90e2; /* Blue */
        --color-secondary: #f5a623; /* Orange/Gold */
        --color-success: #7ed321; /* Green */
        --color-warning: #f8e71c; /* Yellow */
        --color-danger: #d0021b; /* Red */
        --color-background: #f4f7f6;
        --color-card-background: #ffffff;
        --color-border: #e0e0e0;
        --color-text-dark: #333;
        --color-text-light: #666;
    }

    body {
        font-family: 'Arial', sans-serif; /* Replace with a more elegant font if loaded */
        line-height: 1.6;
        color: var(--color-text-dark);
        background-color: var(--color-background);
        padding: 20px;
    }

    h1, h2 {
        color: var(--color-secondary);
        text-align: center;
        margin-bottom: 20px;
    }

    .porcelain-simulator {
        background-color: var(--color-card-background);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        max-width: 700px;
        direction: rtl; /* Ensure RTL */
        text-align: right; /* Ensure RTL text alignment */
    }

    .simulator-intro {
        text-align: center;
        margin-bottom: 30px;
        color: var(--color-text-light);
        font-size: 1.1em;
    }

    .simulator-controls {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid var(--color-border);
        border-radius: 10px;
        background-color: #f9fbfb;
    }

    .control-group {
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align labels/inputs to the right */
    }

    .control-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: var(--color-text-dark);
        font-size: 1em;
    }

    .control-group select,
    .control-group input[type="number"] {
        padding: 10px 12px;
        border: 1px solid var(--color-border);
        border-radius: 6px;
        font-size: 1rem;
        width: calc(100% - 24px); /* Full width minus padding */
        box-sizing: border-box; /* Include padding and border in the element's total width */
        margin-bottom: 5px; /* Space between input and note */
    }

     .control-group input[type="number"] {
         width: 100px; /* Fixed width for number inputs */
         margin-left: 10px; /* Space for RTL */
         text-align: center;
     }


    .note {
        font-size: 0.9rem;
        color: var(--color-text-light);
        display: block; /* Ensure it's on its own line */
    }

    #simulate-btn {
        display: block; /* Make button full width or centered */
        width: fit-content; /* Adjust width based on content */
        margin: 20px auto 0 auto; /* Center button */
        padding: 12px 25px;
        background-color: var(--color-primary);
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1rem;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3);
    }

    #simulate-btn:hover {
        background-color: #0056b3; /* Darker blue */
        transform: translateY(-1px);
    }
     #simulate-btn:active {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0, 123, 255, 0.4);
     }

    #simulate-btn:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
    }

    /* Kiln Animation Area */
    .kiln-area {
        margin: 30px auto;
        width: 200px;
        height: 250px;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: flex-end;
    }

    .kiln {
        width: 150px;
        height: 200px;
        background-color: #6d4c41; /* Brown */
        border: 5px solid #4e342e; /* Darker brown */
        border-bottom: none;
        border-radius: 8px 8px 0 0;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden; /* Hide overflow from heat effect */
    }

    .kiln-door {
         width: 80px;
         height: 100px;
         background-color: #8d6e63; /* Lighter brown */
         border: 4px solid #4e342e;
         border-radius: 6px;
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         z-index: 2;
         box-shadow: inset 0 0 10px rgba(0,0,0,0.3);
    }
    .kiln-door::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 30px;
        height: 10px;
        background-color: #4e342e;
        border-radius: 5px;
        transform: translate(-50%, -50%);
    }

     .kiln-interior {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         display: flex;
         justify-content: center;
         align-items: center;
         z-index: 1; /* Behind the door */
     }

    .clay-object {
        width: 40px;
        height: 50px;
        background-color: #bcaaa4; /* Clay color */
        border-radius: 4px;
        position: relative;
        bottom: -20px; /* Position near the bottom of the kiln interior */
        opacity: 1; /* Visible initially */
        transition: opacity 0.5s ease; /* Fade out on simulation */
    }

    .kiln-heat-effect {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 0; /* Start with no height */
        background: linear-gradient(to top, rgba(255,0,0,0.8), rgba(255,165,0,0.5), rgba(255,255,0,0.2)); /* Heat gradient */
        z-index: 0; /* Behind everything */
        transition: height 1s ease-out;
        opacity: 0;
    }

    .kiln-area.firing .kiln-heat-effect {
        height: 100%; /* Grow height */
        opacity: 1;
         animation: pulsate-heat 1.5s infinite alternate; /* Add pulsing effect */
    }

    .kiln-area.firing .clay-object {
        opacity: 0; /* Hide clay object during firing */
    }


     @keyframes pulsate-heat {
         0% { opacity: 0.8; }
         100% { opacity: 1; }
     }


    .simulator-result {
        margin-top: 30px;
        padding: 20px;
        border-radius: 10px;
        background-color: var(--color-card-background);
        min-height: 80px; /* Sufficient height */
        display: flex;
        align-items: center;
        gap: 20px; /* Space between icon and text */
        border: 1px solid var(--color-border);
        transition: background-color 0.5s ease, border-color 0.5s ease;
    }

    .result-icon {
         width: 50px;
         height: 50px;
         background-size: contain;
         background-repeat: no-repeat;
         background-position: center;
         flex-shrink: 0; /* Prevent icon from shrinking */
    }
     /* Icons based on result type - using simple shapes/colors for now */
     .result-icon.perfect { background-color: var(--color-success); border-radius: 50%; }
     .result-icon.cracked { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-alert-triangle"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3.93h16.94a2 2 0 0 0 1.71-3.93L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'); } /* Warning icon */
     .result-icon.melted { background-color: var(--color-danger); border-radius: 50%; }
     .result-icon.porous { background-color: var(--color-warning); border-radius: 50%; }

    .result-text {
        margin: 0;
        font-size: 1.1em;
        color: var(--color-text-dark);
        text-align: right; /* RTL */
        flex-grow: 1; /* Allow text to take up space */
    }

     /* Styling based on result type */
    .simulator-result.perfect {
        background-color: #e9f7ef; /* Light green */
        border-color: var(--color-success);
    }
    .simulator-result.cracked {
        background-color: #fff9e6; /* Light yellow */
        border-color: var(--color-warning);
    }
    .simulator-result.melted {
        background-color: #fde9ec; /* Light red */
        border-color: var(--color-danger);
    }
    .simulator-result.porous {
        background-color: #f0f3f4; /* Light gray */
        border-color: var(--color-border);
    }


    #toggle-explanation-btn {
        display: block;
        margin: 40px auto 20px auto; /* Center button below simulator */
        padding: 10px 15px;
        background-color: var(--color-text-light);
        color: white;
        border: none;
        border-radius: 20px;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease;
    }

    #toggle-explanation-btn:hover {
         background-color: #5a6268;
    }

    #explanation-content {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--color-border);
        border-radius: 10px;
        background-color: #f9fbfb;
        direction: rtl; /* Ensure RTL */
        text-align: right; /* Ensure RTL text alignment */
    }

    #explanation-content h2, #explanation-content h3 {
        color: var(--color-secondary);
        margin-top: 15px;
        margin-bottom: 10px;
    }
     #explanation-content h2 {
         border-bottom: 2px solid var(--color-secondary);
         padding-bottom: 5px;
     }
     #explanation-content h3 {
         color: var(--color-primary);
     }

    #explanation-content p {
        line-height: 1.7;
        margin-bottom: 15px;
        color: var(--color-text-dark);
    }

    #explanation-content strong {
         color: var(--color-text-dark);
    }


</style>

<button id="toggle-explanation-btn">הצג את סודות האש והבוץ (הסבר מדעי)</button>
<div id="explanation-content" style="display: none;">
    <h2>הסבר: סודות הפורצלן הסיני</h2>
    <p>הפורצלן הסיני אינו סתם "חימר שנשרף". הוא תוצר של תהליך מורכב ומדויק, שילוב מנצח של חומרים נכונים, הכנה קפדנית, ושליטה מושלמת באש ובחום התנור. אלפי שנות ניסוי וטעייה הובילו לגילוי הסודות האלה.</p>

    <h3>מה מייחד פורצלן אמיתי?</h3>
    <p>בניגוד לכלי חרס רגילים או אבן, פורצלן אמיתי הוא:</p>
    <ul>
        <li><strong>שקוף למחצה (טרנסלוסנטי):</strong> כאשר אור עובר דרכו, במיוחד בקצוות הדקים.</li>
        <li><strong>חזק ועמיד במיוחד:</strong> הרבה יותר מכל סוג אחר של קרמיקה בטמפרטורות שריפה נמוכות יותר.</li>
        <li><strong>אטום לחלוטין:</strong> גם ללא ציפוי גלזורה. אינו סופג מים.</li>
        <li><strong>בעל צליל גבוה בנקישה:</strong> סמן לוויטריפיקציה מלאה ומבנה צפוף.</li>
    </ul>

    <h3>מפתחות הקסם: החומרים הנכונים</h3>
    <p>הפורצלן הסיני המסורתי, במקור ממרבצים ספציפיים כמו בג'ינגדז'ן, מבוסס על שילוב של שלושה מרכיבים עיקריים בכמויות מדויקות:</p>
    <ul>
        <li><strong>קאולין (Kaolin):</strong> חימר לבן, טהור ועשיר במינרל קאוליניט. זהו עמוד השדרה של הפורצלן. הקאולין מעניק את הצבע הלבן הצח, שומר על צורת הכלי בטמפרטורות קיצוניות (עמידות לאש), ונותן פלסטיות לעבודה. ככל שהקאולין טהור יותר, כך נדרשת טמפרטורה גבוהה יותר לשריפה מוצלחת, אך התוצאה תהיה איכותית יותר.</li>
        <li><strong>פלדספר (Feldspar):</strong> משמש כ"ממסך" (flux). בטמפרטורות גבוהות, הפלדספר נמס והופך לנוזל זכוכיתי. נוזל זה ממלא את החללים הריקים בין חלקיקי הקאולין והקוורץ, ובעת הקירור מתקשה לזכוכית. הוא קריטי לתהליך הויטריפיקציה (התזגוג). ככל שיש יותר ממסכים או שהם "אגרסיביים" יותר (כמו בתערובת עם זיהומים), כך טמפרטורת השריפה הנדרשת יורדת, אך הסיכון לעיוות או התכה עולה.</li>
        <li><strong>קוורץ (Quartz / Silica):</strong> מוסיף חוזק ויציבות למבנה הפורצלן הסופי לאחר השריפה.</li>
    </ul>
     <p>היחס המדויק בין רכיבים אלו משתנה ותלוי באיכות החומרים ובתוצאה הרצויה. זה היה אחד הסודות הגדולים ששמרו הסינים.</p>

    <h3>רגע האמת: תהליך השריפה (ויטריפיקציה)</h3>
    <p>השריפה היא לב התהליך. בניגוד לחרס שנשרף בטמפרטורות נמוכות (כ-900-1100 מעלות), פורצלן דורש חום אדיר - לרוב מעל 1280 מעלות צלזיוס, ולפורצלן איכותי אפילו מעל 1350 מעלות! בטמפרטורות אלו מתרחש הקסם:</p>
    <ul>
        <li><strong>הממסכים נמסים:</strong> הפלדספר ורכיבים אחרים הופכים לנוזל.</li>
        <li><strong>ויטריפיקציה (התזגוג):</strong> הנוזל הזכוכיתי חודר לכל הנקבוביות ומחבר את שאר החלקיקים.</li>
        <li><strong>שינויים מבניים:</strong> מינרלים משנים את הפאזה הגבישית שלהם (למשל, קוורץ הופך לקריסטובליט) ויוצרים מבנה פנימי חזק ויציב במיוחד.</li>
    </ul>
    <p>התוצאה היא חומר צפוף, בלתי חדיר למים, שקוף למחצה וחזק. תהליך זה דורש זמן שהייה בטמפרטורה הגבוהה ("השרייה") כדי להבטיח ויטריפיקציה אחידה ומלאה בכל עובי הכלי.</p>

    <h3>האתגר הטכנולוגי: לשלוט באש</h3>
    <p>שריפה בטמפרטורות כל כך גבוהות הייתה הישג טכנולוגי עצום בעת העתיקה ובימי הביניים. זה דרש בניית תנורים מיוחדים כמו "תנורי דרקון" (Longyao) שהיו ארוכים ונבנו על צלע גבעה כדי לנצל את זרימת האוויר, ושימוש בכמויות עצומות של עצים מתאימים כדי להגיע לחום המרבי ולשמור עליו לאורך זמן. השליטה בטמפרטורה הייתה אינטואיטיבית ודרשה ניסיון רב.</p>

    <h3>מה קורה אם הטמפרטורה שגויה?</h3>
    <ul>
        <li><strong>נמוכה מדי:</strong> הממסכים אינם נמסים מספיק. הכלי אינו עובר ויטריפיקציה מלאה, נשאר נקבובי, סופג מים, וחלש (כמו חרס או אבן).</li>
        <li><strong>גבוהה מדי:</strong> הממסכים נמסים יתר על המידה והנוזל הופך לדליל מדי. הכלי מאבד את יציבותו, מתעוות, נופל, או אפילו נמס לחלוטין והופך לגוש זכוכית מותך בתחתית התנור. גם משך שריפה ארוך מדי בטמפרטורה גבוהה יכול לגרום לתוצאות הרסניות.</li>
    </ul>

    <p>הסימולטור מאפשר לכם לחוות את האתגר הזה ממקור ראשון. נסו למצוא את שילוב החומר והטמפרטורה (וזמן השריפה) שיוביל לתוצאה מושלמת!</p>

</div>

<script>
    const simulateBtn = document.getElementById('simulate-btn');
    const materialSelect = document.getElementById('material');
    const temperatureInput = document.getElementById('temperature');
    const timeInput = document.getElementById('time');
    const resultArea = document.getElementById('result-area');
    const resultTextElement = resultArea.querySelector('.result-text');
    const resultIconElement = resultArea.querySelector('.result-icon');
    const kilnArea = document.querySelector('.kiln-area');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
    const explanationContent = document.getElementById('explanation-content');

    // Mapping result types to descriptions and required temps
    const resultsData = {
        high_purity_kaolin: {
            perfect: { range: [1300, 1380], timeBoost: 1350, text: "מזל טוב, יצרת פורצלן מושלם! לבן, שקוף למחצה, חזק, ובעל צליל פעמון. הטמפרטורה ומשך השריפה היו בדיוק בטווח הנכון לקאולין טהור.", type: 'perfect' },
            near_perfect: { range: [1280, 1300], timeBoost: 1290, text: "כמעט מושלם! הפורצלן נוצר, אבל ייתכן שהוא מעט פחות שקוף או חזק מהאידיאל. עוד קצת חום או זמן שריפה היו עוזרים.", type: 'perfect' }, // Slight variation for lower end
            porous: { range: [800, 1279], text: "הכלי יצא אטום ונקבובי, סופג מים. לא התרחשה ויטריפיקציה מלאה. הטמפרטורה נמוכה מדי עבור קאולין טהור.", type: 'porous' },
            cracked: { range: [1381, 1450], timeSensitive: 1400, text: "אוי לא, הכלי סדוק ומעוות! הטמפרטורה הייתה גבוהה מדי וגרמה למבנה לאבד יציבות בשלבים האחרונים. היה קרוב!", type: 'cracked' },
            melted: { range: [1451, 1600], text: "הכלי התפרק והתכה לגוש חסר צורה! החום היה קיצוני מדי, גם קאולין טהור לא עמד בזה.", type: 'melted' }
        },
        kaolin_with_flux: {
            perfect: { range: [1220, 1300], timeBoost: 1260, text: "הצלחת! יצרת פורצלן מצוין מהתערובת. שקוף למחצה וחזק. תוספות הממסכים הורידו את טווח הטמפרטורה האידיאלי.", type: 'perfect' },
            near_perfect: { range: [1180, 1219], timeBoost: 1190, text: "ויטריפיקציה חלקית. הכלי פחות נקבובי מחימר רגיל, אך עדיין לא פורצלן אמיתי. טמפרטורה נמוכה מדי עבור ויטריפיקציה מלאה.", type: 'porous' }, // More vitrified porous
            porous: { range: [800, 1179], text: "הכלי נשאר נקבובי וחלש. הטמפרטורה נמוכה מדי לוויטריפיקציה כלשהי.", type: 'porous' },
            cracked: { range: [1301, 1380], timeSensitive: 1340, text: "הכלי נסדק או התעוות! הממסכים התמוססו יתר על המידה והכלי איבד את צורתו בגלל הטמפרטורה הגבוהה מדי עבור תערובת זו.", type: 'cracked' },
            melted: { range: [1381, 1600], text: "הכלי התפרק לחלוטין! התערובת לא עמידה בחום קיצוני כזה.", type: 'melted' }
        },
        low_grade_mix: {
            stoneware: { range: [1150, 1250], text: "התוצאה היא אבן קרמית (Stoneware). חומר צפוף יחסית וחזק, פחות נקבובי מחרס, אך לא שקוף למחצה כמו פורצלן. לא ניתן להגיע לפורצלן מתערובת זו.", type: 'porous' }, // Classified as porous type for icon, but different text
             porous: { range: [800, 1149], text: "הכלי נשאר נקבובי וחלש (כמו חרס רגיל). התערובת לא עמידה בטמפרטורות גבוהות מספיק לוויטריפיקציה של אבן.", type: 'porous' },
            cracked: { range: [1251, 1350], timeSensitive: 1280, text: "הכלי סדוק/מעוות! התערובת לא מתאימה לשריפה בחום כזה ומתחילה להתמוסס ולאבד מבנה.", type: 'cracked' },
            melted: { range: [1351, 1600], text: "הכלי נמס לגמרי! תערובת זו אינה יכולה לעמוד בטמפרטורות גבוהות כל כך.", type: 'melted' }
        }
    };

    simulateBtn.addEventListener('click', () => {
        const material = materialSelect.value;
        const temperature = parseInt(temperatureInput.value, 10);
        const time = parseInt(timeInput.value, 10);

        // Disable button and start firing animation
        simulateBtn.disabled = true;
        kilnArea.classList.add('firing');
        resultArea.classList.remove('perfect', 'cracked', 'melted', 'porous'); // Reset previous styling
        resultIconElement.className = 'result-icon'; // Reset icon class
        resultTextElement.textContent = "הכבשן לוהט... ממתין לתוצאה...";


        // Simulate firing time (visual delay)
        setTimeout(() => {
            let result = null;
            const materialResults = resultsData[material];

            // Determine result based on temperature and material
            if (temperature >= materialResults.perfect.range[0] && temperature <= materialResults.perfect.range[1]) {
                // Perfect range, check time for subtle variations
                if (materialResults.near_perfect && temperature < materialResults.near_perfect.timeBoost && time < 6) {
                     result = materialResults.near_perfect; // Not enough time at lower end of ideal
                } else {
                     result = materialResults.perfect; // Good temperature and time
                }
            } else if (materialResults.near_perfect && temperature >= materialResults.near_perfect.range[0] && temperature < materialResults.near_perfect.range[1]) {
                 // Near perfect range, check time
                 if (time >= 5) { // Enough time might push it closer to perfect
                     result = materialResults.near_perfect; // Still near perfect, maybe slightly better
                     result.text += " (הזמן הארוך סייע לוויטריפיקציה!)";
                 } else {
                      result = materialResults.near_perfect; // Not enough time
                      result.text += " (ייתכן שנדרש זמן שריפה ארוך יותר!)";
                 }
            } else if (temperature < materialResults.porous.range[1] || (materialResults.stoneware && temperature < materialResults.stoneware.range[0])) {
                 // Too low temperature
                 result = materialResults.porous;
                 if(materialResults.stoneware && temperature >= materialResults.stoneware.range[0] && temperature < materialResults.stoneware.range[1]) {
                      result = materialResults.stoneware;
                 }
            } else if (materialResults.cracked && temperature >= materialResults.cracked.range[0] && temperature <= materialResults.cracked.range[1]) {
                 // Too high, but not melted yet - check time sensitivity
                 result = materialResults.cracked;
                 if (materialResults.cracked.timeSensitive && temperature >= materialResults.cracked.timeSensitive && time > 10) {
                     result.text += " (הזמן הארוך בטמפרטורה כזו החמיר את העיוות!)";
                 }
            }
            else if (materialResults.melted && temperature >= materialResults.melted.range[0]) {
                // Melted
                result = materialResults.melted;
            }

            // Fallback for unexpected range (shouldn't happen with proper ranges)
            if (!result) {
                result = { text: "לא הצלחנו לקבוע את התוצאה עבור שילוב זה. נסה שוב?", type: 'porous' }; // Default to porous/unknown
            }


            // Display result
            resultTextElement.textContent = result.text;
            resultArea.classList.add(result.type);
            resultIconElement.classList.add(result.type);

            // Re-enable button and stop firing animation
            simulateBtn.disabled = false;
            kilnArea.classList.remove('firing');

        }, 3000); // Simulate 3 seconds of firing time
    });

    toggleExplanationBtn.addEventListener('click', () => {
        if (explanationContent.style.display === 'none') {
            explanationContent.style.display = 'block';
            toggleExplanationBtn.textContent = 'הסתר את סודות האש והבוץ';
        } else {
            explanationContent.style.display = 'none';
            toggleExplanationBtn.textContent = 'הצג את סודות האש והבוץ (הסבר מדעי)';
        }
    });

     // Initial state
     explanationContent.style.display = 'none'; // Ensure it's hidden on load

</script>