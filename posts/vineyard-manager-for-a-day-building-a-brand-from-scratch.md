---
title: "מנהל יקב ליום אחד: מסע לבניית אימפריית יין"
english_slug: vineyard-manager-for-a-day-building-a-brand-from-scratch
category: "ניהול"
tags: ["יקב", "ניהול", "שיווק", "חקלאות", "יין", "סימולציה עסקית", "מותג"]
---
<div class="app-container">
    <header class="app-header">
        <h1>מנהל יקב ליום אחד: מסע לבניית אימפריית יין</h1>
        <p class="subtitle">האם יש לך את היכולת להפוך אדמה, מים ושמש, למוניטין בינלאומי? צאו למסע מרתק שחושף את כל הגורמים הסודיים שמעצבים בקבוק יין בלתי נשכח, ובנו את מותג היין הבא שיכבוש את העולם.</p>
    </header>

    <div id="simulation-app" class="simulation-section">
        <div class="simulation-intro">
            <h2>האתגר: יקב וירטואלי משלך</h2>
            <p>קיבלתם לידכם יקב צעיר עם הון התחלתי. ההצלחה תלויה כעת בהחלטות האסטרטגיות שתקבלו בכל שנה – מהאדמה ועד הבקבוק, ומשם לשוק.</p>
        </div>

        <div id="status" class="status-panel">
            <h3>מצב היקב הנוכחי</h3>
            <div class="status-grid">
                <div class="status-item">
                    <span class="status-label">שנה:</span>
                    <span id="current-year" class="status-value">1</span>
                </div>
                <div class="status-item">
                    <span class="status-label">כסף:</span>
                    <span id="money" class="status-value">$10,000</span>
                </div>
                <div class="status-item">
                    <span class="status-label">מוניטין:</span>
                    <span id="reputation" class="status-value">50</span>
                </div>
                <div class="status-item">
                    <span class="status-label">מלאי יין:</span>
                    <span id="inventory" class="status-value">0</span> בקבוקים
                </div>
            </div>
        </div>

        <div id="decisions" class="decisions-panel">
            <h3>החלטות לשנה הנוכחית</h3>
            <div class="decision-area vineyard-decision">
                <h4><i class="icon-grape"></i> כרם: הלב הפועם של היין</h4>
                <p>בחרו את זן הענבים שיתאים לאדמה ולחזון שלכם. כל זן מביא איתו פוטנציאל ואתגרים משלו.</p>
                <div class="control-group">
                    <label for="grape-variety">בחר זן ענבים לשתילה:</label>
                    <select id="grape-variety" class="control-input">
                        <option value="cabernet">קברנה סוביניון (יוקרתי, דורשני, פוטנציאל גבוה)</option>
                        <option value="merlot">מרלו (פופולרי, גמיש, מסחרי)</option>
                        <option value="chardonnay">שרדונה (לבן, מתאים למגוון סגנונות, צמיחה מהירה)</option>
                         <option value="syrah">סירה (ארומטי, אקלים חם, יינות עוצמתיים)</option>
                    </select>
                    <button class="btn plant-btn"><i class="icon-plant"></i> שתול כרם</button>
                </div>
                <p class="decision-placeholder">...החלטות עתידיות: טיפוח, השקיה, ניהול יבול, בציר - כל שלב ישפיע על איכות הפרי והיין.</p>
            </div>

            <div class="decision-area production-decision">
                <h4><i class="icon-barrel"></i> ייצור יין: אמנות ומדע</h4>
                 <p class="decision-placeholder">...החלטות עתידיות: שיטות תסיסה, בחירת שמרים, סוג ומשך יישון בחביות, טכניקות סינון ויציבות - כל החלטה תשפיע על טעם ואופי היין הסופי.</p>
            </div>

            <div class="decision-area marketing-decision">
                <h4><i class="icon-tag"></i> שיווק ומכירה: לבנות את המותג</h4>
                 <p class="decision-placeholder">...החלטות עתידיות: בניית סיפור המותג, עיצוב בקבוק ותווית, קביעת אסטרטגיית תמחור, בחירת ערוצי מכירה (חנויות, מסעדות, ייצוא) - האופן בו תציגו את היין לעולם יכריע את הצלחתו בשוק.</p>
            </div>
        </div>

        <div id="reports" class="reports-panel">
            <h3>דוחות שנתיים ותוצאות</h3>
            <p class="reports-placeholder">...בסוף כל שנה תקבלו דו"ח מפורט על ביצועי היקב, מכירות, רווחים/הפסדים, שינויים במוניטין ואירועים מיוחדים שהתרחשו (כמו מזג אוויר קיצוני או מחלות). כאן תלמדו מה עבד ומה פחות, ותתכוננו לשנה הבאה!</p>
        </div>

         <button id="next-year-btn" class="btn next-year-btn"><i class="icon-calendar"></i> התקדם לשנה הבאה</button>
         <p class="coming-soon-note">(פונקציונליות מלאה של הסימולציה, כולל קבלת החלטות מורכבות ודוחות מפורטים, נמצאת בשלבי פיתוח מתקדמים. בינתיים, התנסו במעבר בין השנים וצפו בשינויים בסטטוס)</p>

    </div>

    <button id="toggle-explanation" class="btn explanation-toggle-btn">הצג/הסתר את סודות עולם היין</button>

    <div id="explanation" class="explanation-section">
        <h2>הסבר מורחב: מאחורי הקלעים של עולם היין</h2>

        <div class="explanation-area">
            <h3>מחזור החיים של יין: מהשורש לבקבוק</h3>
            <p>תהליך יצירת היין הוא מסע ארוך ומרתק, החל מהנביטה באדמה ועד הרגע שהבקבוק נפתח. הוא דורש סבלנות, ידע מדעי ומגע של אמנות. השלבים המרכזיים כוללים את הקמת הכרם וטיפוח הגפנים במשך שנים, קביעת מועד הבציר המושלם, בציר ידני או מכני, מעבר ליקב לתהליכי ריסוק ותסיסה, סחיטה, יישון במיכלים או חביות, ייצוב, סינון ולבסוף - ביקבוק ואריזה.</p>
        </div>

        <div class="explanation-area">
            <h3>מה עושה יין לגדול? הגורמים הקריטיים לאיכות</h3>
            <ul>
                <li><strong>טרור (Terroir):</strong> מושג קסום שמקיף את כל מה שהופך מקום מסוים לייחודי עבור יין: אקלים, הרכב הקרקע, טופוגרפיה, ואפילו צורת ניהול הכרם המקומית. טרור יוצא דופן הוא מתנה של הטבע שקובעת את הבסיס לאיכות.</li>
                <li><strong>זן הענבים:</strong> לכל זן טביעת אצבע גנטית משלו שקובעת את מאפייניו הבסיסיים - צבע, ארומות, טאנינים, חומציות. התאמת הזן הנכון לטרור הנכון היא החלטה גורלית.</li>
                <li><strong>עבודת הכרם:</strong> לא מספיק לשתול - צריך לטפח באהבה ובמקצועיות. גיזום מדויק, דילול יבול קפדני, והתמודדות נבונה עם מחלות ומזיקים מבטיחים פרי בריא ומרוכז בטעמים.</li>
                <li><strong>ידי היינן:</strong> הקסם קורה ביקב. החלטות לגבי טמפרטורת תסיסה, סוגי שמרים, משך המגע עם הקליפות, ובחירת חביות היישון (עץ אלון צרפתי? אמריקאי? חדשות? ישנות?) - כל אלו מעצבות את היין הסופי והופכות אותו מיבול גולמי ליצירת אמנות.</li>
            </ul>
        </div>

        <div class="explanation-area">
            <h3>הצד העסקי: להפוך תשוקה לאימפריה</h3>
            <p>יקב הוא הרבה יותר מעשיית יין; הוא עסק לכל דבר. ההיבטים הכלכליים והשיווקיים קריטיים להצלחה ארוכת טווח:</p>
            <ul>
                <li><strong>עלויות והשקעות:</strong> רכישת קרקע, נטיעה, בניית יקב, רכישת ציוד, עלויות עבודה שוטפות, חומרי גלם (בקבוקים, פקקים, תוויות), שיווק, מכירות ומיסוי - כל אלו דורשים תכנון פיננסי קפדני.</li>
                <li><strong>תמחור ואסטרטגיית שוק:</strong> קביעת המחיר הנכון לכל בקבוק היא אמנות בפני עצמה, המשלבת את עלויות הייצור, תפיסת האיכות של היין, מוניטין היקב והמחירים בשוק התחרותי.</li>
                <li><strong>מיתוג וסיפור המותג:</strong> מה הופך יקב למותג אהוב? סיפור מרתק, עיצוב ויזואלי שובה לב, חווית מבקרים בלתי נשכחת, ובניית קהילה נאמנה סביב ערכי היקב.</li>
                <li><strong>ערוצי הפצה ומכירה:</strong> איך היין מגיע מהיקב לצרכן? דרך חנויות יין, מסעדות יוקרה, רשתות שיווק גדולות, מכירה ישירה מהיקב (דלת למכירה, אתר אינטרנט), או ייצוא לשווקים בינלאומיים. כל ערוץ דורש אסטרטגיה שונה.</li>
            </ul>
        </div>

         <div class="explanation-area">
            <h3>אתגרים באופק: לנווט בנוף המשתנה</h3>
            <p>ענף היין אינו חף מקשיים:</p>
            <ul>
                <li><strong>שינויי אקלים:</strong> מזג אוויר קיצוני הופך תדיר יותר ומאיים על יבול ואיכות. נדרשת גמישות ויכולת הסתגלות, ולעיתים גם השקעה בטכנולוגיות הגנה או שינוי זנים.</li>
                <li><strong>תחרות גלובלית:</strong> העולם מלא ביינות מצוינים. לבלוט בשוק רווי דורש איכות יוצאת דופן, מיתוג חזק ויכולת שיווקית גבוהה.</li>
                <li><strong>רגולציה ומנהלות:</strong> חוקים ותקנות שונים הנוגעים לייצור, שיווק, מכירה ומיסוי יכולים להוות מכשול, במיוחד בשווקים בינלאומיים.</li>
                <li><strong>מחלות ומזיקים:</strong> גפנים חשופות למגוון איומים ביולוגיים הדורשים ניטור וטיפול מתמיד ויקר.</li>
            </ul>
        </div>

         <div class="explanation-area">
            <h3>השורה התחתונה: זו לא רק שתייה, זו תרבות ועסק</h3>
            <p>הבנת הניואנסים החקלאיים, התעשייתיים והעסקיים היא המפתח להצלחה בתעשיית היין. הסימולציה הזו נועדה לתת לכם טעימה (תרתי משמע!) מהאתגרים והסיפוקים של בניית מותג יין מאפס. בהצלחה!</p>
         </div>
    </div>
</div> <!-- /app-container -->

<style>
    @import url('https://fonts.googleapis.com/css2?family=Alef:wght@400;700&family=Frank+Ruhl+Libre:wght@400;500;700&display=swap');

    :root {
        --vineyard-green: #4a6b5a; /* Dark earthy green */
        --wine-burgundy: #8a2b3d; /* Rich wine red */
        --grape-purple: #6a4c93; /* Deep purple */
        --earth-brown: #a17a69; /* Warm brown */
        --cream-white: #f5f5dc; /* Off-white/parchment */
        --gold-accent: #cfb53b; /* Subtle gold for highlights */
        --text-color: #333;
        --background-color: #eef2eb; /* Light earthy background */
        --panel-background: #fff;
        --border-color: #ddd;
        --shadow-color: rgba(0, 0, 0, 0.1);
        --transition-speed: 0.3s ease-in-out;
    }

    body {
        font-family: 'Alef', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 0;
        background-color: var(--background-color);
        color: var(--text-color);
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: flex-start; /* Align items to the top */
        padding: 20px;
        box-sizing: border-box;
    }

    h1, h2, h3, h4 {
        font-family: 'Frank Ruhl Libre', serif;
        color: var(--vineyard-green);
        margin-bottom: 1rem;
    }

    h1 {
        color: var(--wine-burgundy);
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        text-align: center;
        color: #555;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    .app-container {
        max-width: 900px;
        width: 100%;
        background-color: var(--panel-background);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 20px var(--shadow-color);
        margin-bottom: 20px;
        overflow: hidden; /* Clear floats/margins */
    }

    .simulation-section, .explanation-section {
        margin-top: 25px;
        padding-top: 25px;
        border-top: 1px solid var(--border-color);
    }

    .simulation-intro h2, .explanation-section h2 {
        text-align: center;
        margin-bottom: 1.5rem;
        color: var(--grape-purple);
    }

    .status-panel {
        margin-bottom: 30px;
        padding: 20px;
        background-color: var(--cream-white);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform var(--transition-speed), box-shadow var(--transition-speed);
    }

    .status-panel:hover {
         transform: translateY(-3px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .status-panel h3 {
        margin-top: 0;
        color: var(--earth-brown);
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    .status-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
    }

    .status-item {
        background-color: #fff;
        padding: 10px 15px;
        border-radius: 5px;
        border: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 1.1rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    }

     .status-label {
         font-weight: bold;
         color: #555;
     }

     .status-value {
         font-weight: 700;
         color: var(--vineyard-green);
         font-family: 'Frank Ruhl Libre', serif;
     }
     #money .status-value {
         color: var(--gold-accent);
     }
      #reputation .status-value {
         color: var(--grape-purple);
     }


    .decisions-panel {
        margin-bottom: 30px;
    }

    .decisions-panel h3 {
        color: var(--vineyard-green);
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .decision-area {
        background-color: #f8f9f7;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.07);
        position: relative;
        overflow: hidden;
    }

    .decision-area:before { /* Simple visual divider */
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 5px;
        height: 100%;
        background: linear-gradient(to bottom, var(--grape-purple), var(--wine-burgundy));
    }
     .vineyard-decision:before { background: linear-gradient(to bottom, var(--vineyard-green), var(--earth-brown)); }
     .production-decision:before { background: linear-gradient(to bottom, var(--wine-burgundy), var(--grape-purple)); }
     .marketing-decision:before { background: linear-gradient(to bottom, var(--gold-accent), var(--earth-brown)); }


    .decision-area h4 {
        margin-top: 0;
        color: #555;
        display: flex;
        align-items: center;
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 1px dashed var(--border-color);
    }
     .decision-area h4 i {
         margin-left: 10px;
         font-size: 1.3em;
         color: var(--grape-purple);
     }
      .vineyard-decision h4 i { color: var(--vineyard-green); }
      .production-decision h4 i { color: var(--wine-burgundy); }
      .marketing-decision h4 i { color: var(--gold-accent); }


    .control-group {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .control-group label {
        font-weight: bold;
        color: var(--text-color);
        flex-shrink: 0; /* Prevent label from shrinking */
    }

    .control-input {
        padding: 10px 15px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        font-size: 1rem;
        font-family: 'Alef', sans-serif;
        background-color: #fff;
        flex-grow: 1; /* Allow input to grow */
        min-width: 150px; /* Minimum width for input */
        transition: border-color var(--transition-speed), box-shadow var(--transition-speed);
    }
    .control-input:focus {
        outline: none;
        border-color: var(--grape-purple);
        box-shadow: 0 0 5px rgba(106, 76, 147, 0.3);
    }


    .btn {
        display: inline-flex; /* Use flex for icon alignment */
        align-items: center;
        justify-content: center;
        background-color: var(--vineyard-green);
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1rem;
        font-family: 'Alef', sans-serif;
        transition: background-color var(--transition-speed), transform var(--transition-speed), box-shadow var(--transition-speed);
        margin-top: 10px; /* Keep some margin */
        text-decoration: none; /* For toggle button which might be treated as link */
    }

    .btn i {
        margin-left: 8px;
        font-size: 1.1em;
    }

    .btn:hover {
        background-color: #3d5c4c;
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }

    .btn:active {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

     .plant-btn { background-color: var(--grape-purple); }
     .plant-btn:hover { background-color: #5a3e81; }

     .explanation-toggle-btn {
         background-color: var(--wine-burgundy);
         display: block; /* Make it a block element */
         margin: 25px auto; /* Center the button */
         width: fit-content; /* Adjust width to content */
     }
     .explanation-toggle-btn:hover { background-color: #7a202f; }


    .reports-panel {
         margin-bottom: 30px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--cream-white);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
     .reports-panel h3 {
        margin-top: 0;
        color: var(--earth-brown);
         border-bottom: 1px dashed var(--border-color);
        padding-bottom: 10px;
        margin-bottom: 15px;
     }

    .reports-placeholder, .decision-placeholder {
        font-style: italic;
        color: #888;
        margin-top: 15px;
        font-size: 0.95rem;
        padding: 10px;
        background-color: #f0f0f0;
        border-left: 3px solid #ccc;
        border-radius: 4px;
    }


    .next-year-btn {
        display: block; /* Make it a block element */
        margin: 25px auto 15px auto; /* Center the button */
        width: fit-content; /* Adjust width to content */
        background-color: var(--earth-brown);
    }
    .next-year-btn:hover {
        background-color: #8a6857;
    }


    .coming-soon-note {
        font-style: italic;
        color: #888;
        margin-top: 10px;
        text-align: center;
        font-size: 0.9rem;
    }

    /* Explanation Section Styling */
     .explanation-section {
        background-color: var(--cream-white);
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        display: none; /* Hidden by default */
        opacity: 0; /* Start with hidden opacity */
        transform: translateY(20px); /* Start slightly below */
        transition: opacity var(--transition-speed) ease-out, transform var(--transition-speed) ease-out;
    }

    .explanation-section.visible { /* Class added by JS */
        display: block;
        opacity: 1;
        transform: translateY(0);
    }


    .explanation-area {
         margin-bottom: 25px;
         padding-bottom: 25px;
         border-bottom: 1px dashed var(--border-color);
    }
    .explanation-area:last-child {
        border-bottom: none;
        padding-bottom: 0;
        margin-bottom: 0;
    }


    .explanation-section h3 {
        color: var(--vineyard-green);
        margin-top: 0;
        margin-bottom: 12px;
        font-size: 1.4rem;
    }

    .explanation-section ul {
        list-style-type: disc;
        padding-right: 20px; /* Indent list items */
        margin-top: 15px;
    }

    .explanation-section li {
        margin-bottom: 10px;
    }

    /* Basic Icons (replace with real icon font like Font Awesome if possible) */
     .icon-grape:before { content: "🍇 "; } /* Unicode grape */
     .icon-plant:before { content: "🌿 "; } /* Unicode herb */
     .icon-barrel:before { content: "🍷 "; } /* Unicode wine glass (closest) */
     .icon-tag:before { content: "🏷️ "; } /* Unicode label */
     .icon-calendar:before { content: "📅 "; } /* Unicode calendar */


    /* Responsive adjustments */
    @media (max-width: 600px) {
        .app-container {
            padding: 15px;
        }

        .status-grid {
            grid-template-columns: 1fr; /* Stack items on small screens */
        }

        .control-group {
            flex-direction: column;
            align-items: flex-start;
            gap: 10px;
        }

        .control-group label {
            margin-bottom: 5px;
        }

        .btn {
             width: 100%; /* Full width buttons on small screens */
             text-align: center;
             justify-content: center;
             margin-top: 0;
        }
         .btn i {
             margin-left: 0; /* Remove margin for centered icon */
             margin-right: 8px;
         }

        .next-year-btn, .explanation-toggle-btn {
            width: 100%;
            margin-left: 0;
            margin-right: 0;
        }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        toggleButton.addEventListener('click', () => {
            const isVisible = explanationDiv.classList.contains('visible');
            if (isVisible) {
                explanationDiv.style.opacity = '0';
                explanationDiv.style.transform = 'translateY(20px)';
                explanationDiv.addEventListener('transitionend', function handler() {
                    explanationDiv.style.display = 'none';
                    explanationDiv.classList.remove('visible');
                    explanationDiv.removeEventListener('transitionend', handler);
                });
            } else {
                explanationDiv.style.display = 'block';
                // Force reflow to enable transition
                explanationDiv.offsetHeight;
                explanationDiv.style.opacity = '1';
                explanationDiv.style.transform = 'translateY(0)';
                explanationDiv.classList.add('visible');
            }
        });

        // Basic simulation display update with animations
        const currentYearSpan = document.getElementById('current-year');
        const moneySpan = document.getElementById('money');
        const reputationSpan = document.getElementById('reputation');
        const inventorySpan = document.getElementById('inventory');
        const nextYearBtn = document.getElementById('next-year-btn');

        let year = 1;
        let money = 10000;
        let reputation = 50;
        let inventory = 0; // Representing bottled wine ready for sale

        // Function to animate status updates
        function updateStatusDisplay(newYear, newMoney, newReputation, newInventory) {
            // Simple fade/scale animation for status panel
            const statusPanel = document.getElementById('status');
             statusPanel.style.opacity = '0.5';
             statusPanel.style.transform = 'scale(0.98)';

            setTimeout(() => {
                currentYearSpan.textContent = newYear;
                moneySpan.textContent = `$${newMoney}`;
                reputationSpan.textContent = newReputation;
                inventorySpan.textContent = newInventory;

                // Add subtle pulse animation to values that change
                const elementsToUpdate = [];
                if (year !== newYear) elementsToUpdate.push(currentYearSpan);
                if (money !== newMoney) elementsToUpdate.push(moneySpan);
                if (reputation !== newReputation) elementsToUpdate.push(reputationSpan);
                if (inventory !== newInventory) elementsToUpdate.push(inventorySpan);

                 elementsToUpdate.forEach(el => {
                     el.classList.add('pulse');
                     el.addEventListener('animationend', () => {
                         el.classList.remove('pulse');
                     }, { once: true });
                 });


                statusPanel.style.opacity = '1';
                statusPanel.style.transform = 'scale(1)';

                // Update state variables
                year = newYear;
                money = newMoney;
                reputation = newReputation;
                inventory = newInventory;


            }, 300); // Match CSS transition duration

        }

        nextYearBtn.addEventListener('click', () => {
             // This is just a placeholder for advanced simulation logic.
            const nextYear = year + 1;
            // Simulate basic operational costs and random events
            let nextMoney = money - 2000; // Basic operating costs
            let nextReputation = reputation;
            let nextInventory = inventory; // Assume no new wine produced yet in this basic demo

            // Simulate a random event affecting reputation
            const randomEvent = Math.random();
            if (randomEvent > 0.8) { // Good year
                nextReputation += Math.floor(Math.random() * 5) + 1; // Gain 1-5 rep
                 nextMoney += 1000; // Small bonus from visitors/basic sales
                 alert(`שנה ${nextYear} החלה! הייתה שנה מוצלחת בכרם. המוניטין עלה מעט.`);
            } else if (randomEvent < 0.3) { // Bad year
                 nextReputation -= Math.floor(Math.random() * 4); // Lose 0-3 rep
                 if (nextReputation < 0) nextReputation = 0;
                 nextMoney -= 500; // Minor unexpected costs
                 alert(`שנה ${nextYear} החלה! מזג אוויר לא אידיאלי השפיע על היבול. המוניטין ירד מעט.`);
            } else { // Average year
                 alert(`שנה ${nextYear} החלה. עברה עלינו שנה רגועה יחסית ביקב.`);
                 nextMoney -= 200; // Just base costs
            }


            // In a real app, you'd process decisions made by the user, calculate yield, produce wine based on decisions and yield, sell wine based on inventory, marketing and reputation, update reports, etc.

            // Update the display with potential changes
             updateStatusDisplay(nextYear, nextMoney, nextReputation, nextInventory);

             // Example: Add a placeholder report entry (optional, could be more complex)
             const reportsDiv = document.getElementById('reports');
             if (reportsDiv.querySelector('.reports-placeholder')) {
                 reportsDiv.querySelector('.reports-placeholder').style.display = 'none'; // Hide initial placeholder
             }
             const reportEntry = document.createElement('div');
             reportEntry.classList.add('report-entry'); // Add a class for styling
             reportEntry.innerHTML = `
                 <h4>דו"ח שנה ${year} (בסיסי)</h4>
                 <p><strong>אירועים מרכזיים:</strong> ${randomEvent > 0.8 ? "שנה חקלאית טובה מהצפוי." : randomEvent < 0.3 ? "אתגרי מזג אוויר." : "שנה שגרתית."}</p>
                 <p><strong>שינוי בכסף:</strong> ${nextMoney - money}$</p>
                 <p><strong>שינוי במוניטין:</strong> ${nextReputation - reputation}</p>
                 <p>...דוח מורחב (בפיתוח) יכלול ניתוח החלטות, יבול, ייצור ומכירות.</p>
             `;
             reportsDiv.appendChild(reportEntry);

             // Simple styling for report entry (can be moved to CSS)
             reportEntry.style.borderBottom = '1px dashed #ccc';
             reportEntry.style.paddingBottom = '15px';
             reportEntry.style.marginBottom = '15px';
             reportEntry.style.backgroundColor = '#fcfcfc';
             reportEntry.style.padding = '15px';
             reportEntry.style.borderRadius = '5px';


        });

        // Add simple hover effect to decision areas
        document.querySelectorAll('.decision-area').forEach(area => {
            area.addEventListener('mouseenter', () => {
                area.style.transform = 'translateY(-5px)';
                area.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
            });
            area.addEventListener('mouseleave', () => {
                 area.style.transform = 'translateY(0)';
                 area.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.07)';
            });
        });

         // Add simple animation for the plant button click (visual feedback only)
         const plantBtn = document.querySelector('.plant-btn');
         const grapeVarietySelect = document.getElementById('grape-variety');

         plantBtn.addEventListener('click', () => {
             const selectedVarietyText = grapeVarietySelect.options[grapeVarietySelect.selectedIndex].text;
             plantBtn.classList.add('clicked');
             plantBtn.textContent = `(${selectedVarietyText.split('(')[0].trim()}) נשתל!`; // Show selection feedback
             plantBtn.disabled = true; // Disable for this "year" (placeholder)

             setTimeout(() => {
                 plantBtn.classList.remove('clicked');
                 // Reset text, maybe re-enable or change appearance for next year's action
                 plantBtn.innerHTML = `<i class="icon-plant"></i> שתול כרם`;
                 plantBtn.disabled = false; // Re-enable for next year demo
             }, 1500); // Animation duration

             // Add subtle animation/feedback to the vineyard decision area
             const vineyardArea = document.querySelector('.vineyard-decision');
             vineyardArea.style.transition = 'background-color 0.5s ease-in-out';
             vineyardArea.style.backgroundColor = '#e0f0d9'; // Light green background
             setTimeout(() => {
                 vineyardArea.style.backgroundColor = '#f8f9f7'; // Reset background
             }, 1000);
         });

          // Add pulsing animation for status values when they change
          const style = document.createElement('style');
          style.innerHTML = `
              @keyframes pulse {
                  0% { transform: scale(1); color: inherit; }
                  50% { transform: scale(1.1); color: var(--grape-purple); font-weight: 800; }
                  100% { transform: scale(1); color: inherit; }
              }
              #money .pulse { color: var(--gold-accent) !important; }
              #reputation .pulse { color: var(--wine-burgundy) !important; }
              .status-value.pulse {
                  animation: pulse 0.6s ease-in-out;
              }
          `;
          document.head.appendChild(style);


    });
</script>
```