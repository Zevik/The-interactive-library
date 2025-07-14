---
title: "החתימה הפחמנית שלך: גלה את ההשפעה האישית על האקלים"
english_slug: calculate-your-carbon-footprint-interactive
category: "אקולוגיה"
tags: [טביעת רגל פחמנית, סביבה, שינוי אקלים, קיימות, חישוב אישי, אינטראקטיבי]
---
# החתימה הפחמנית שלך: גלה את ההשפעה האישית על האקלים

האם עצרת פעם לחשוב איך הפעולות היומיומיות שלך – מאיפה האוכל על הצלחת שלך, איך הגעת הבוקר לעבודה, או אפילו החולצה שאתה לובש – משפיעות על הכדור שלנו? לכל בחירה שלנו יש 'חתימה' פחמנית, תביעת אצבע אנרגטית שמשאירה את רישומה באטמוספירה. כמה גדולה החתימה **שלך**?

התנסו במחשבון האישי הפשוט שלנו וקבלו הערכה מהירה. זו לא אנליזה מדעית מדויקת, אלא יותר הזמנה למסע אישי של מודעות והבנה.

<div class="carbon-footprint-calculator">
    <h2>מחשבון חתימה פחמנית אישית מהיר</h2>
    <p class="intro-text">ענה על מספר שאלות פשוטות כדי לקבל אומדן משוער של טביעת הרגל הפחמנית השנתית שלך בטונות של CO2e (שווה ערך פחמן דו-חמצני).</p>

    <div class="question-section">
        <h3>🚗 מסע והתניידות</h3>
        <div class="question">
            <label for="transportation-car">האם אתה משתמש ברכב פרטי על בסיס קבוע?</label>
            <select id="transportation-car">
                <option value="none">לא משתמש ברכב פרטי</option>
                <option value="petrol">כן, רכב בנזין/דיזל</option>
                <option value="hybrid">כן, רכב היברידי</option>
                <option value="electric">כן, רכב חשמלי</option>
            </select>
        </div>
        <div class="question" id="car-km-question" style="display: none;">
             <label for="transportation-car-frequency">כמה ק"מ אתה נוסע בממוצע בשבוע ברכב זה?</label>
             <input type="number" id="transportation-car-frequency" value="0" min="0" step="10" dir="ltr"> <span class="unit">ק"מ לשבוע</span>
        </div>
        <div class="question">
            <label for="transportation-public">באיזו תדירות אתה משתמש בתחבורה ציבורית (אוטובוס, רכבת, מטרונית...)?</label>
            <select id="transportation-public">
                <option value="rarely">לעיתים רחוקות מאוד / לא בכלל</option>
                <option value="weekly">פעם בשבוע או יותר</option>
                <option value="daily">כמעט כל יום</option>
            </select>
        </div>
         <div class="question">
            <label for="transportation-flights">כמה טיסות לחו"ל (הלוך ושוב) ביצעת בשנה האחרונה?</label>
            <select id="transportation-flights">
                <option value="0">0 טיסות</option>
                <option value="1">1 טיסה</option>
                <option value="2">2 טיסות</option>
                <option value="3plus">3 טיסות או יותר</option>
            </select>
        </div>
    </div>

    <div class="question-section">
        <h3>🏠 בית ואנרגיה</h3>
        <div class="question">
            <label for="home-size">כמה אנשים גרים במשק הבית (כולל אתה)?</label>
            <select id="home-size">
                <option value="1">אדם 1</option>
                <option value="2">2 אנשים</option>
                <option value="3">3 אנשים</option>
                <option value="4plus">4 אנשים או יותר</option>
            </select>
        </div>
        <div class="question">
             <label for="home-apartment-size">גודל הדירה/בית:</label>
             <select id="home-apartment-size">
                 <option value="small">קטן (עד 70 מ"ר)</option>
                 <option value="medium">בינוני (71-120 מ"ר)</option>
                 <option value="large">גדול (מעל 120 מ"ר)</option>
             </select>
         </div>
        <div class="question">
            <label for="home-heating-cooling">באיזו תדירות אתם משתמשים במיזוג אוויר או חימום?</label>
            <select id="home-heating-cooling">
                <option value="rarely">לעיתים רחוקות מאוד</option>
                <option value="seasonal">בעונות המעבר / לפי הצורך</option>
                <option value="frequent">בתדירות גבוהה (כמעט כל יום בעונה)</option>
            </select>
        </div>
    </div>

    <div class="question-section">
        <h3>🍔 תזונה</h3>
        <div class="question">
            <label for="diet-type">סוג התזונה העיקרי שלך:</label>
            <select id="diet-type">
                <option value="omnivore">אוכלי כל (כולל בשר, עוף, דגים באופן שגרתי)</option>
                <option value="flexitarian">צמחוני גמיש / אוכל בשר לעיתים רחוקות</option>
                <option value="vegetarian">צמחוני (ללא בשר ודגים)</option>
                <option value="vegan">טבעוני (ללא מוצרים מהחי כלל)</option>
            </select>
        </div>
    </div>

    <div class="question-section">
        <h3>🛍️ צריכה וסגנון חיים</h3>
        <div class="question">
            <label for="consumption-shopping">עד כמה אתה נוטה לרכוש מוצרים חדשים (בגדים, גאדג'טים, רהיטים)?</label>
            <select id="consumption-shopping">
                <option value="low">מעט מאוד / מעדיף יד שנייה / משתף</option>
                <option value="medium">לפי הצורך / כמו רוב האנשים</option>
                <option value="high">הרבה / אוהב להתחדש לעיתים קרובות</option>
            </select>
        </div>
        <div class="question">
            <label for="consumption-recycling">האם אתה ממחזר פסולת בבית (נייר, פלסטיק, זכוכית, אורגני)?</label>
            <select id="consumption-recycling">
                <option value="yes">כן, את רוב סוגי הפסולת</option>
                <option value="partial">חלקית בלבד</option>
                <option value="no">לא</option>
            </select>
        </div>
    </div>

    <button id="calculate-btn">חשב לי את החתימה הפחמנית!</button>

    <div id="result-area" class="result-area">
        <h4><span class="result-icon">🌍</span> הערכת החתימה הפחמנית השנתית שלך היא:</h4>
        <div id="footprint-result"></div>
        <p class="disclaimer"> *שימו לב: מחשבון זה מציג הערכה פשטנית ומיועד למטרות המחשה וחינוך בלבד. חישוב מדויק דורש נתונים רבים ומפורטים יותר ומורכב ממגוון רחב יותר של גורמים.</p>
    </div>
</div>

<button id="show-explanation-btn" class="explanation-toggle-btn">מהי טביעת רגל פחמנית ואיך אפשר להקטין אותה? <span class="arrow">▼</span></button>

<div id="explanation-section" class="explanation-section">
    <h2>מהי טביעת רגל פחמנית (או חתימה פחמנית)?</h2>
    <p>טביעת רגל פחמנית היא למעשה סך כל פליטות גזי החממה הנפלטות לאטמוספירה כתוצאה מפעילות מסוימת - של אדם, ארגון, מוצר או אירוע. היא נמדדת בדרך כלל בטונות של שווה ערך פחמן דו-חמצני (CO2e - Carbon Dioxide Equivalent). מדד זה כולל לא רק פליטות של CO2 כתוצאה משריפת דלקים פוסיליים, אלא גם גזי חממה נוספים כמו מתאן (CH4) ותחמוצת חנקן (N2O). כל גז מקבל "משקל" יחסי בהתאם לפוטנציאל ההתחממות הגלובלי שלו בהשוואה ל-CO2 לאורך זמן.</p>

    <h2>למה חשוב לחשב אותה?</h2>
    <p>חישוב טביעת הרגל הפחמנית, בין אם היא אישית או גלובלית, הוא כלי קריטי להבנת ההשפעה שלנו על משבר האקלים. גזי החממה הללו, כשהם מצטברים באטמוספירה, לוכדים חום וגורמים להתחממות כדור הארץ - תופעה שמובילה לשינויים אקלימיים קיצוניים: גלי חום, בצורות, שיטפונות, עליית מפלס פני הים, שינויים דרמטיים במערכות אקולוגיות ועוד. הבנה כמותית של הפליטות מאפשרת:</p>
        <ul>
            <li>העלאת מודעות אישית לאופן שבו אורח החיים שלנו משפיע על הסביבה.</li>
            <li>הצבת יעדי הפחתה ברמה האישית, העסקית והלאומית.</li>
            <li>מעקב אחר התקדמות ביעדים אלו והשוואה בינלאומית.</li>
            <li>קבלת החלטות מושכלות יותר לגבי צריכה, השקעות, פיתוח טכנולוגי ומדיניות ממשלתית.</li>
        </ul>


    <h2>מרכיבים עיקריים בטביעת הרגל האישית</h2>
    <p>טביעת הרגל הפחמנית של אדם ממוצע מורכבת מכמה תחומים מרכזיים המשקפים את אורח החיים והצריכה:</p>
        <ul>
            <li>**תחבורה:** שימוש ברכב פרטי (סוג הדלק, מרחק), תחבורה ציבורית, וכמובן - טיסות. טיסות, במיוחד ארוכות, מהוות לרוב מרכיב דומיננטי בטביעת הרגל.</li>
            <li>**בית ואנרגיה:** צריכת חשמל ואנרגיה לחימום/קירור, תאורה, ושימוש במכשירים. תלוי בגודל הבית, יעילות הבידוד, מספר הדיירים ומקור האנרגיה (דלקים פוסיליים מול אנרגיות מתחדשות).</li>
            <li>**תזונה:** ייצור המזון שאנו צורכים. גידול בקר, למשל, מייצר פליטות מתאן משמעותיות. תזונה המבוססת יותר על צומח לרוב בעלת חתימה פחמנית נמוכה יותר.</li>
            <li>**צריכה ופסולת:** מחזור החיים של המוצרים שאנו קונים - החל מהייצור, דרך האריזה והשינוע, ועד לסוף חייהם (השלכה או מיחזור). צריכה מוגברת של מוצרים חדשים, במיוחד "מהירים" או מיובאים מרחוק, מגדילה את טביעת הרגל. מיחזור מסייע חלקית בהפחתה.</li>
        </ul>

    <h2>הערכת טביעת רגל פחמנית - האתגרים והמחשבון הפשטני שלנו</h2>
    <p>חישוב מדויק ואמין של טביעת רגל פחמנית אישית הוא משימה מורכבת ביותר הדורשת נתונים מפורטים ומדויקים להפליא על כל היבטי החיים (קילומטרז' שנתי מדויק בכל סוג רכב, חשבונות חשמל ומים מפורטים, פירוט קניות מזון ומוצרים, הרגלי נסיעות ספציפיים ועוד). מחשבונים אישיים מקוונים, כמו זה שראיתם כאן, מסתמכים על הנחות רחבות והערכות גסות המבוססות על ממוצעים וטווחי השפעה. לכן, התוצאה שתקבלו היא אינדיקציה בלבד, כלי פשוט ליצירת מודעות ראשונית, ולא חישוב אבסולוטי. אל תראו בה מספר סופי, אלא נקודת פתיחה למחשבה.</p>

    <h2>איך נוכל להפחית את החתימה הפחמנית האישית שלנו?</h2>
    <p>בעוד שמשבר האקלים דורש שינויים מערכתיים רחבי היקף, ישנם צעדים משמעותיים שכל אחד ואחת מאיתנו יכולים לנקוט בחיי היומיום כדי לצמצם את ההשפעה הסביבתית האישית:</p>
        <ul>
            <li>**תחבורה:** בחרו באופציות עם פליטות נמוכות: לכו ברגל, רכבו על אופניים, השתמשו בתחבורה ציבורית. צמצמו נסיעות ברכב פרטי והשתדלו לשתף נסיעות (קארפול). שקלו מעבר לרכב חשמלי באנרגיה מתחדשת (כאשר תשתית הטעינה ירוקה). צמצמו טיסות לחו"ל, במיוחד ליעדים רחוקים, או שקלו חופשות ארוכות יותר/קרובות יותר.</li>
            <li>**בית ואנרגיה:** חסכו בחשמל: כבו אורות ומכשירים לא בשימוש, השתמשו במכשירי חשמל יעילים אנרגטית, שפרו בידוד בבית. השתמשו במיזוג/חימום בחכמה. אם יש לכם אפשרות, שקלו התקנת פאנלים סולאריים או מעבר לספק חשמל שמקורו באנרגיות מתחדשות (כאשר האופציה קיימת).</li>
            <li>**תזונה:** הפחיתו משמעותית צריכת בשר אדום ומוצרי חלב. הגדילו צריכת מזון מן הצומח - ירקות, פירות, קטניות, דגנים. העדיפו מזון מקומי ועונתי. צמצמו בזבוז מזון למינימום - תכננו קניות, השתמשו בשאריות.</li>
            <li>**צריכה:** קנו פחות - במיוחד בגדים, גאדג'טים ומוצרים "אופנתיים" בעלי תוחלת חיים קצרה. תיקנו במקום לזרוק ולקנות חדש. רכשו מוצרים יד שנייה או השתמשו בשירותי השאלה/השכרה. בחרו במוצרים עמידים, איכותיים ומיוצרים באופן בר-קיימא. הקפידו למחזר את כל סוגי הפסולת האפשריים אצלכם.</li>
        </ul>
    <p>כל שינוי קטן, כשמתרבים לו שינויים דומים אצל מיליוני אנשים, יוצר יחד השפעה מצטברת משמעותית שמסייעת במאמץ הגלובלי להאט את ההתחממות ולבנות עתיד בר-קיימא יותר.</p>

</div>


<style>
    :root {
        --primary-green: #4CAF50;
        --secondary-blue: #008CBA;
        --background-light: #f4f7f6;
        --card-background: #ffffff;
        --border-color: #e0e0e0;
        --text-dark: #333;
        --text-medium: #555;
        --success-color: #28a745;
        --success-bg: #d4edda;
        --success-border: #c3e6cb;
        --hover-green: #45a049;
        --hover-blue: #007bb5;
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        --border-radius: 8px;
        --spacing-medium: 15px;
        --spacing-large: 20px;
    }

    .carbon-footprint-calculator {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        max-width: 750px; /* Slightly wider */
        margin: var(--spacing-large) auto;
        padding: var(--spacing-large);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--background-light);
        box-shadow: var(--shadow);
        line-height: 1.6;
    }

    .carbon-footprint-calculator h2,
    .carbon-footprint-calculator h3,
    .result-area h4 {
        color: var(--text-dark);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 12px; /* Slightly more padding */
        margin-bottom: var(--spacing-medium);
        font-weight: bold;
    }

    .carbon-footprint-calculator h2 {
         font-size: 1.8em;
    }
     .carbon-footprint-calculator h3 {
        font-size: 1.3em;
     }


     .result-area h4 {
         border-bottom: none;
         margin-bottom: 8px;
         font-size: 1.4em;
         display: flex;
         align-items: center;
         justify-content: center;
     }

    .intro-text {
        color: var(--text-medium);
        margin-bottom: var(--spacing-large);
        font-size: 1.1em;
    }


    .question-section {
        margin-bottom: var(--spacing-large);
        padding: var(--spacing-medium);
        background-color: var(--card-background);
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .question {
        margin-bottom: var(--spacing-medium);
    }

    .question label {
        display: block;
        margin-bottom: 8px; /* Slightly more space */
        font-weight: 600; /* Bolder */
        color: var(--text-medium);
        font-size: 1em;
    }

    .question select,
    .question input[type="number"] {
        width: calc(100% - 24px); /* Adjust for padding and border */
        padding: 10px 12px; /* Adjust padding */
        border: 1px solid var(--border-color);
        border-radius: 4px;
        font-size: 1rem;
        color: var(--text-dark);
        background-color: #fdfdfd;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        direction: rtl; /* Ensure RTL for input text */
    }

    .question select:focus,
    .question input[type="number"]:focus {
        border-color: var(--secondary-blue);
        box-shadow: 0 0 5px rgba(0, 140, 186, 0.3);
        outline: none;
    }

    .question input[type="number"] {
        width: 90px; /* Slightly wider */
        display: inline-block;
        vertical-align: middle;
        text-align: right; /* Align number right */
    }

     .question .unit {
         color: var(--text-medium);
         font-size: 0.9em;
         margin-right: 5px;
     }


    button {
        display: block;
        width: 100%;
        padding: 12px; /* More padding */
        background-color: var(--primary-green);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        font-size: 1.3rem; /* Larger font */
        font-weight: bold;
        cursor: pointer;
        margin-top: var(--spacing-large);
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: var(--shadow);
    }

     #show-explanation-btn {
         background-color: var(--secondary-blue);
         margin-bottom: var(--spacing-large);
         margin-top: var(--spacing-large);
         display: flex;
         align-items: center;
         justify-content: center;
     }

    button:hover {
        background-color: var(--hover-green);
        transform: translateY(-2px); /* Slight lift effect */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
     #show-explanation-btn:hover {
         background-color: var(--hover-blue);
     }

     button:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
     }


    .result-area {
        margin-top: var(--spacing-large);
        padding: var(--spacing-medium);
        border: 1px solid var(--success-border);
        background-color: var(--success-bg);
        color: var(--success-color);
        border-radius: var(--border-radius);
        text-align: center;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start slightly below */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
    }

    .result-area.visible {
        opacity: 1;
        transform: translateY(0);
    }

    #footprint-result {
        font-size: 2.8em; /* Much larger */
        font-weight: 900; /* Extra bold */
        margin: 15px 0;
        color: var(--success-color);
        letter-spacing: -0.5px; /* Tighten letter spacing */
    }

    .result-area .disclaimer {
        font-size: 0.85em; /* Slightly larger disclaimer */
        color: var(--success-color);
        opacity: 0.9;
        margin-top: var(--spacing-medium);
    }

    .result-area .result-icon {
        margin-left: 10px;
        font-size: 1.2em;
        vertical-align: middle;
    }


     .explanation-toggle-btn .arrow {
         margin-right: 10px;
         transition: transform 0.3s ease;
     }

     .explanation-toggle-btn.open .arrow {
         transform: rotate(180deg);
     }


     .explanation-section {
         direction: rtl;
         font-family: 'Arial', sans-serif;
         max-width: 750px; /* Match calculator width */
         margin: 0 auto var(--spacing-large) auto; /* Adjust margin */
         padding: var(--spacing-large);
         border: 1px solid var(--border-color);
         border-radius: var(--border-radius);
         background-color: var(--card-background);
         box-shadow: var(--shadow);
         line-height: 1.7; /* More spacing */
         color: var(--text-medium);
         /* Start hidden and prepare for animation */
         opacity: 0;
         max-height: 0;
         overflow: hidden;
         transition: opacity 0.6s ease-out, max-height 0.6s ease-out;
     }

     .explanation-section.open {
         opacity: 1;
         max-height: 3000px; /* Sufficiently large value to show content */
     }


     .explanation-section h2 {
         color: var(--text-dark);
         border-bottom: 1px solid var(--border-color);
         padding-bottom: 12px;
         margin-bottom: var(--spacing-medium);
         font-size: 1.6em;
         font-weight: bold;
     }

     .explanation-section p,
     .explanation-section ul {
         margin-bottom: var(--spacing-medium);
     }

     .explanation-section ul {
         padding-right: 25px; /* Adjust padding for RTL list */
         list-style-type: disc; /* Use disk bullets */
     }

     .explanation-section li {
         margin-bottom: 10px; /* More space between list items */
     }

     .explanation-section li strong {
         color: var(--text-dark); /* Make key terms stand out */
     }

     /* Responsive Adjustments */
     @media (max-width: 768px) {
         .carbon-footprint-calculator,
         .explanation-section {
             padding: var(--spacing-medium);
             margin: var(--spacing-medium) auto;
         }

         .carbon-footprint-calculator h2 {
             font-size: 1.5em;
         }
          .carbon-footprint-calculator h3 {
             font-size: 1.1em;
          }

         button {
             font-size: 1.1rem;
             padding: 10px;
         }

         #footprint-result {
             font-size: 2em;
         }
     }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const calculateBtn = document.getElementById('calculate-btn');
        const resultArea = document.getElementById('result-area');
        const footprintResultDiv = document.getElementById('footprint-result');
        const showExplanationBtn = document.getElementById('show-explanation-btn');
        const explanationSection = document.getElementById('explanation-section');
        const carTypeSelect = document.getElementById('transportation-car');
        const carKmQuestion = document.getElementById('car-km-question');

        // Estimated annual CO2e values in tonnes per year (simplified averages for Israel context where applicable)
        // These factors are illustrative and simplified for a general educational tool.
        // Real-world values vary greatly based on specific models, grid mix, etc.
        const CO2e_FACTORS = {
            transportation: {
                // Per 1000 km driven per year
                car_petrol_per_1000km: 0.19, // Slightly adjusted
                car_diesel_per_1000km: 0.17, // Slightly adjusted
                car_hybrid_per_1000km: 0.09, // Slightly adjusted
                car_electric_per_1000km: 0.04, // Depends heavily on Israel's grid mix (~50% gas, coal still present)
                 // Base value for car ownership/maintenance/manufacturing spread over lifetime
                car_base: 0.3, // Increased base factor
                // Annual values
                public_weekly: 0.4, // Simplified, assumes mixed modes/distances
                public_daily: 0.8, // Simplified
                 // Per return flight - greatly simplified! Short/medium/long
                flight_1: 0.9, // Approx short/medium haul (e.g., Europe)
                flight_2: 1.8, // Two such trips
                flight_3plus: 4.0 // Assumes at least one long haul or multiple medium
            },
            home: {
                 // Base per person annual footprint related to size/shared resources (energy, construction footprint amortized)
                 // Scale by size then divide by people
                size_small_base: 1.5, // Total for house regardless of people
                size_medium_base: 2.2,
                size_large_base: 3.5,
                // Per person factors related to shared services, scaled by size
                 person_factor_small: 0.5,
                 person_factor_medium: 0.7,
                 person_factor_large: 1.0,

                // Additional annual footprint for heating/cooling intensity
                heating_cooling_seasonal: 0.6,
                heating_cooling_frequent: 1.5
            },
            diet: {
                omnivore: 2.5,
                flexitarian: 1.8, // Reduced slightly
                vegetarian: 1.5, // Reduced slightly
                vegan: 1.0 // Reduced slightly
            },
            consumption: {
                 // Baseline assumes "medium" consumption
                 base: 1.2,
                 // Adjustments based on selected level
                high_add: 0.8,
                low_subtract: -0.5,
                // Adjustments for recycling (partial impact on overall consumption footprint)
                recycling_partial_subtract: -0.1,
                recycling_yes_subtract: -0.2
            }
        };

        // Function to update car km question visibility
        const updateCarKmVisibility = () => {
            if (carTypeSelect.value !== 'none') {
                carKmQuestion.style.display = 'block';
            } else {
                carKmQuestion.style.display = 'none';
                 // Reset value when hiding
                 document.getElementById('transportation-car-frequency').value = 0;
            }
        };

         // Initial call to set visibility based on default value
         updateCarKmVisibility();

        // Listen for changes on car type select
        carTypeSelect.addEventListener('change', updateCarKmVisibility);


        calculateBtn.addEventListener('click', () => {
            let totalFootprint = 0;

            // 1. Transportation
            const carType = carTypeSelect.value;
            const carKmPerWeek = parseInt(document.getElementById('transportation-car-frequency').value) || 0;
            const carKmPerYear = carKmPerWeek * 52;

             if (carType !== 'none') {
                 totalFootprint += CO2e_FACTORS.transportation.car_base; // Add base for car ownership
                 if (carType === 'petrol') totalFootprint += (carKmPerYear / 1000) * CO2e_FACTORS.transportation.car_petrol_per_1000km;
                 if (carType === 'hybrid') totalFootprint += (carKmPerYear / 1000) * CO2e_FACTORS.transportation.car_hybrid_per_1000km;
                 if (carType === 'electric') totalFootprint += (carKmPerYear / 1000) * CO2e_FACTORS.transportation.car_electric_per_1000km;
             }


            const publicTransport = document.getElementById('transportation-public').value;
            if (publicTransport === 'weekly') totalFootprint += CO2e_FACTORS.transportation.public_weekly;
            if (publicTransport === 'daily') totalFootprint += CO2e_FACTORS.transportation.public_daily;

            const flights = document.getElementById('transportation-flights').value;
            if (flights === '1') totalFootprint += CO2e_FACTORS.transportation.flight_1;
            if (flights === '2') totalFootprint += CO2e_FACTORS.transportation.flight_2;
            if (flights === '3plus') totalFootprint += CO2e_FACTORS.transportation.flight_3plus;


            // 2. Home & Energy
            const householdSize = parseInt(document.getElementById('home-size').value);
            const apartmentSize = document.getElementById('home-apartment-size').value;
            const heatingCooling = document.getElementById('home-heating-cooling').value;

            // Calculate home energy based on size and per person factor
             let homeBase = 0;
             if (apartmentSize === 'small') homeBase = CO2e_FACTORS.home.size_small_base + (CO2e_FACTORS.home.person_factor_small * householdSize);
             if (apartmentSize === 'medium') homeBase = CO2e_FACTORS.home.size_medium_base + (CO2e_FACTORS.home.person_factor_medium * householdSize);
             if (apartmentSize === 'large') homeBase = CO2e_FACTORS.home.size_large_base + (CO2e_FACTORS.home.person_factor_large * householdSize);

            totalFootprint += homeBase / householdSize; // Divide total house footprint by number of people


            if (heatingCooling === 'seasonal') totalFootprint += CO2e_FACTORS.home.heating_cooling_seasonal / householdSize; // Heating/cooling impact per person
            if (heatingCooling === 'frequent') totalFootprint += CO2e_FACTORS.home.heating_cooling_frequent / householdSize;


            // 3. Diet
            const dietType = document.getElementById('diet-type').value;
            totalFootprint += CO2e_FACTORS.diet[dietType];

            // 4. Consumption & Waste
            const consumptionShopping = document.getElementById('consumption-shopping').value;
            const consumptionRecycling = document.getElementById('consumption-recycling').value;

            totalFootprint += CO2e_FACTORS.consumption.base; // Start with baseline consumption

            if (consumptionShopping === 'high') totalFootprint += CO2e_FACTORS.consumption.high_add;
            if (consumptionShopping === 'low') totalFootprint += CO2e_FACTORS.consumption.low_subtract;

            if (consumptionRecycling === 'partial') totalFootprint += CO2e_FACTORS.consumption.recycling_partial_subtract;
            if (consumptionRecycling === 'yes') totalFootprint += CO2e_FACTORS.consumption.recycling_yes_subtract;


            // Ensure footprint is not negative (shouldn't happen with these factors, but good practice)
             totalFootprint = Math.max(0, totalFootprint);


            // Display Result
            footprintResultDiv.textContent = `${totalFootprint.toFixed(1)} טון CO2e`; // Display with one decimal point for simplicity

            // Add animation class
            resultArea.classList.remove('visible'); // Remove to allow re-triggering animation
            // Use a small timeout to ensure class removal is registered before re-adding
            setTimeout(() => {
                resultArea.style.display = 'block';
                resultArea.classList.add('visible');
            }, 10); // Small delay

            // Scroll to result
             resultArea.scrollIntoView({ behavior: 'smooth', block: 'center' }); // Scroll to center of block
        });

        showExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationSection.classList.contains('open');
            explanationSection.classList.toggle('open');
            showExplanationBtn.classList.toggle('open');

             if (explanationSection.classList.contains('open')) {
                 showExplanationBtn.innerHTML = 'הסתר הסבר <span class="arrow">▲</span>';
                 // Scroll to explanation
                  explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
             } else {
                 showExplanationBtn.innerHTML = 'מהי טביעת רגל פחמנית ואיך אפשר להקטין אותה? <span class="arrow">▼</span>';
             }
        });

         // Initial state: hide result and explanation
         resultArea.style.display = 'none';
         explanationSection.classList.remove('open');
         showExplanationBtn.classList.remove('open');
         showExplanationBtn.innerHTML = 'מהי טביעת רגל פחמנית ואיך אפשר להקטין אותה? <span class="arrow">▼</span>';


    });
</script>
```