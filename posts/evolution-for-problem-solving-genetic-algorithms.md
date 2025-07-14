---
title: "אבולוציה לפתרון בעיות: כוחם של אלגוריתמים גנטיים בפעולה"
english_slug: evolution-for-problem-solving-genetic-algorithms
category: "טכנולוגיה / מדעי המחשב"
tags: ["אלגוריתמים", "אופטימיזציה", "בינה מלאכותית", "אבולוציה", "מדעי המחשב תיאורטיים"]
---
# אבולוציה לפתרון בעיות: כוחם של אלגוריתמים גנטיים בפעולה

הטבע, המעבדה הגדולה ביותר בעולם, בונה ומשפר פתרונות מדהימים לבעיות מורכבות באמצעות תהליך פשוט אך עוצמתי: אבולוציה וברירה טבעית. האם נוכל לרתום את החוכמה הזו כדי ללמד מחשבים לפתור אתגרים חישוביים קשים, כמו מציאת המסלול הקצר ביותר בשטח מורכב או אופטימיזציה של מערכות מורכבות? הסימולציה הזו מציגה כיצד **אלגוריתמים גנטיים** (Genetic Algorithms) מחקים את מנגנוני האבולוציה כדי "לפתח" פתרונות טובים לבעיות. צאו למסע אינטראקטיבי וגלו איך "אוכלוסיות" של פתרונות מתפתחות מדור לדור!

<div id="ga-app">
    <div id="ga-controls">
        <h2>מעבדת האבולוציה</h2>
        <div class="control-group">
            <label for="popSize">גודל אוכלוסייה:</label>
            <input type="number" id="popSize" value="150" min="50" max="1000">
            <span class="tooltip-info">מספר הפתרונות הפוטנציאליים בכל דור. אוכלוסייה גדולה יותר מגדילה את השונות אך דורשת יותר חישוב.</span>
        </div>
        <div class="control-group">
            <label for="mutationRate">קצב מוטציה (%):</label>
            <input type="number" id="mutationRate" value="3" min="0" max="20" step="0.1">
             <span class="tooltip-info">הסיכוי שכל "צעד" במסלול ישתנה אקראית בדור הבא. חיוני להכנסת שונות חדשה.</span>
        </div>
        <div class="control-group">
            <label for="crossoverRate">קצב הכלאה (%):</label>
            <input type="number" id="crossoverRate" value="85" min="50" max="100">
             <span class="tooltip-info">הסיכוי ששני מסלולים "יתערבבו" ליצירת מסלולים חדשים. מעביר תכונות טובות בין פתרונות.</span>
        </div>
         <div class="control-group">
            <label for="maxPathLength">אורך מסלול מקסימלי:</label>
            <input type="number" id="maxPathLength" value="70" min="20" max="300">
            <span class="tooltip-info">האורך המרבי של רצף הצעדים שמרכיב כל מסלול.</span>
        </div>
        <div class="button-group">
            <button id="startBtn" class="btn primary">התחל אבולוציה</button>
            <button id="stopBtn" class="btn secondary" disabled>עצור</button>
            <button id="resetBtn" class="btn tertiary">איפוס מפה</button>
        </div>
        <div id="ga-status">
            <h3>סטטוס התפתחות:</h3>
            <p><strong>דור נוכחי:</strong> <span id="currentGeneration">0</span></p>
            <p><strong>ציון התאמה הטוב ביותר:</strong> <span id="bestFitness">---</span> <span class="tooltip-info">ככל שציון ההתאמה גבוה יותר, כך המסלול טוב יותר (קצר יותר, מגיע ליעד, נמנע ממכשולים).</span></p>
            <p><strong>אורך המסלול הטוב ביותר:</strong> <span id="bestPathLength">---</span></p>
             <p><strong>האם הגיע ליעד?</strong> <span id="reachedEndStatus">לא</span></p>
        </div>
        <p class="note">לחצו על הריבועים הריקים במפה כדי להוסיף/להסיר מכשולים (אפשר רק לפני התחלת הסימולציה).</p>
    </div>
    <div id="ga-grid-container">
        <h2>מפת הבעיה</h2>
        <canvas id="ga-canvas"></canvas>
        <div id="legend">
            <div class="legend-item start-legend">התחלה</div>
            <div class="legend-item end-legend">סיום</div>
            <div class="legend-item obstacle-legend">מכשול</div>
            <div class="legend-item path-legend">מסלול הטוב ביותר</div>
        </div>
    </div>
</div>

<style>
:root {
    --primary-color: #4A90E2; /* Blue */
    --secondary-color: #50E3C2; /* Teal */
    --accent-color: #F5A623; /* Orange */
    --obstacle-color: #4A4A4A; /* Dark Grey */
    --start-color: #7ED321; /* Green */
    --end-color: #D0021B; /* Red */
    --path-color: #4A90E2; /* Primary Blue for path */
    --bg-color: #F9F9F9;
    --card-bg-color: #FFFFFF;
    --border-color: #E0E0E0;
    --text-color: #333333;
    --subtle-text-color: #666666;
    --shadow-light: 0 2px 5px rgba(0,0,0,0.1);
    --shadow-medium: 0 5px 15px rgba(0,0,0,0.15);
    --border-radius: 8px;
    --padding-medium: 15px;
    --gap-medium: 20px;
}

#ga-app {
    display: flex;
    flex-wrap: wrap;
    gap: var(--gap-medium);
    font-family: 'Heebo', sans-serif; /* Use Heebo for Hebrew */
    color: var(--text-color);
    line-height: 1.6;
    direction: rtl; /* Right-to-left */
    text-align: right;
}

#ga-controls {
    flex: 1;
    min-width: 280px; /* Slightly wider */
    border: 1px solid var(--border-color);
    padding: var(--padding-medium);
    border-radius: var(--border-radius);
    background-color: var(--card-bg-color);
    box-shadow: var(--shadow-light);
}

#ga-controls h2, #ga-status h3 {
    text-align: center;
    color: var(--primary-color);
    margin-top: 0;
    margin-bottom: var(--padding-medium);
    font-weight: bold;
}

.control-group {
    margin-bottom: var(--padding-medium);
    display: flex;
    align-items: center;
    gap: 10px; /* Space between label, input, tooltip */
}

.control-group label {
    flex-basis: 130px; /* Fixed width for labels */
    font-weight: bold;
    color: var(--subtle-text-color);
}

.control-group input[type="number"] {
    flex-grow: 1;
    padding: 8px;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    max-width: 100px; /* Limit input width */
    text-align: left; /* Numbers align left */
}

.tooltip-info {
    font-size: 0.8em;
    color: var(--subtle-text-color);
    cursor: help;
    position: relative;
    flex-grow: 1;
}

.tooltip-info::before {
    content: 'ⓘ'; /* Information icon */
    margin-left: 5px;
    font-weight: bold;
    color: var(--accent-color);
}


.button-group {
    margin-top: var(--padding-medium);
    text-align: center;
}

.btn {
    padding: 10px 20px;
    margin: 5px; /* Add margin between buttons */
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, opacity 0.3s ease;
    font-weight: bold;
}

.btn.primary {
    background-color: var(--primary-color);
    color: white;
}

.btn.primary:hover:not(:disabled) {
    background-color: #3A7BD5; /* Darker shade */
}

.btn.secondary {
    background-color: var(--accent-color);
    color: white;
}

.btn.secondary:hover:not(:disabled) {
    background-color: #E0951A; /* Darker shade */
}

.btn.tertiary {
    background-color: #CCCCCC;
    color: var(--text-color);
}
.btn.tertiary:hover:not(:disabled) {
    background-color: #B3B3B3;
}


.btn:disabled {
    background-color: #e0e0e0;
    color: #a0a0a0;
    cursor: not-allowed;
    opacity: 0.7;
}

#ga-status {
    margin-top: var(--padding-medium);
    padding-top: var(--padding-medium);
    border-top: 1px solid var(--border-color);
}

#ga-status p {
    margin: 8px 0;
    font-size: 0.95em;
    color: var(--subtle-text-color);
}
#ga-status p strong {
     color: var(--text-color);
}

#ga-grid-container {
    flex: 2;
    min-width: 300px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center; /* Center items in the column */
}

#ga-grid-container h2 {
    color: var(--primary-color);
    margin-top: 0;
    margin-bottom: var(--padding-medium);
    font-weight: bold;
}

#ga-canvas {
    border: 1px solid var(--border-color);
    display: block;
    margin: 0 auto var(--padding-medium) auto; /* Add margin below canvas */
    cursor: pointer;
    background-color: #ffffff; /* White background for grid */
    box-shadow: var(--shadow-medium);
}

#legend {
    display: flex; /* Use flex for horizontal legend */
    justify-content: center;
    flex-wrap: wrap; /* Allow wrapping */
    font-size: 0.9em;
    color: var(--subtle-text-color);
    margin-top: 10px;
}

.legend-item {
    margin: 5px 10px;
    display: flex; /* Align icon and text */
    align-items: center;
}

.legend-item::before {
    content: '';
    display: inline-block;
    width: 18px; /* Larger swatch */
    height: 18px;
    margin-left: 8px; /* Space between swatch and text */
    border: 1px solid var(--border-color);
    box-sizing: border-box; /* Include border in size */
    vertical-align: middle;
}

.start-legend::before { background-color: var(--start-color); border-color: darken(var(--start-color), 10%); }
.end-legend::before { background-color: var(--end-color); border-color: darken(var(--end-color), 10%); }
.obstacle-legend::before { background-color: var(--obstacle-color); border-color: darken(var(--obstacle-color), 10%); }
.path-legend::before { background-color: var(--path-color); border-color: darken(var(--path-color), 10%); }


.note {
    font-size: 0.8em;
    color: var(--subtle-text-color);
    margin-top: var(--padding-medium);
    text-align: center;
}

/* Explanation Section */
#explanation-button {
    display: block;
    margin: 30px auto 10px auto; /* More space above, less below */
    padding: 12px 25px;
    background-color: var(--secondary-color);
    color: var(--text-color); /* Changed color for better contrast */
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: bold;
    transition: background-color 0.3s ease;
    box-shadow: var(--shadow-light);
}

#explanation-button:hover {
    background-color: #44C7AA; /* Darker shade */
}

#explanation {
    display: none; /* Initially hidden */
    margin-top: var(--gap-medium);
    padding-top: var(--gap-medium);
    border-top: 1px solid var(--border-color);
    color: var(--text-color);
    direction: rtl;
    text-align: right;
}

#explanation h2, #explanation h3 {
    color: var(--primary-color);
    margin-bottom: var(--padding-medium);
}

#explanation h3 {
    margin-top: var(--padding-medium);
}

#explanation p {
    margin-bottom: var(--padding-medium);
}

#explanation ul {
    list-style-type: disc;
    margin-right: 20px; /* Use margin-right for RTL */
    margin-bottom: var(--padding-medium);
}

#explanation li {
    margin-bottom: 10px;
    line-height: 1.6;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    #ga-app {
        flex-direction: column;
        gap: var(--padding-medium);
    }

    #ga-controls, #ga-grid-container {
        min-width: 100%;
        flex: none;
    }

    .control-group {
        flex-direction: column; /* Stack label and input */
        align-items: flex-start;
    }

    .control-group label {
        flex-basis: auto;
        margin-bottom: 5px;
    }

    .control-group input[type="number"] {
         max-width: 100%; /* Allow full width */
         width: 100%;
         box-sizing: border-box; /* Include padding in width */
    }

    .button-group {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
     .btn {
         flex-grow: 1;
         margin: 5px;
     }
}
</style>

<button id="explanation-button">רוצים להבין איך הקסם עובד? לחצו כאן להסבר על אלגוריתמים גנטיים</button>

<div id="explanation">
    <h2>מהם אלגוריתמים גנטיים ואיך הם פותרים בעיות?</h2>
    <p>דמיינו עולם שבו פתרונות לבעיות הם יצורים חיים, הנלחמים על הישרדותם ומעבירים את תכונותיהם הטובות לדור הבא. זהו הרעיון שמאחורי אלגוריתמים גנטיים (GA - Genetic Algorithms). זוהי טכניקת אופטימיזציה חישובית מבריקה, המושפעת ישירות מתהליכי האבולוציה והברירה הטבעית שאנו רואים בטבע.</p>
    <p>מטרתם העיקרית היא למצוא פתרונות משופרים (אופטימליים או קרובים לכך) לאתגרים שקשה לפתור בדרכים קונבנציונליות – למשל, כאשר יש אינסוף אפשרויות או כשהבעיה מורכבת מדי לניתוח ישיר. הם חלק ממשפחת "אלגוריתמים אבולוציוניים".</p>

    <h3>השראה ישירות מהטבע: אבולוציה במיטבה</h3>
    <p>הבסיס ל-GA נמצא בתהליכים הביולוגיים המוכרים לנו:</p>
    <ul>
        <li><strong>שונות גנטית:</strong> באוכלוסיית יצורים קיימים הבדלים מולדים (גנטיים).</li>
        <li><strong>מאבק קיומי:</strong> יצורים מתמודדים עם אתגרי הסביבה (מחסור במזון, טורפים, אקלים).</li>
        <li><strong>ברירה טבעית:</strong> ליצורים ש"מתוכנתים" טוב יותר להתמודד עם אתגרים אלו (בעלי "כושר הישרדות" גבוה יותר) יש סיכוי רב יותר לשרוד ולהעמיד צאצאים.</li>
        <li><strong>תורשה והכלאה:</strong> הצאצאים מקבלים שילוב של תכונות מהוריהם.</li>
        <li><strong>מוטציה:</strong> לעיתים רחוקות מתרחש שינוי אקראי וקטן במטען הגנטי של הצאצא – שינוי שיכול להיות מזיק, ניטרלי, או לפעמים (במזל!) מועיל.</li>
        <li><strong>התפתחות:</strong> לאורך דורות רבים, התכונות המועילות הופכות נפוצות יותר באוכלוסייה, והאוכלוסייה כולה הופכת מותאמת יותר לסביבה.</li>
    </ul>
    <p>אלגוריתם גנטי מיישם עקרונות אלו כדי "לגדל" פתרונות משופרים לבעיה חישובית נתונה.</p>

    <h3>מילון מונחים גנטי-חישובי:</h3>
    <ul>
        <li><strong>כרומוזום או פרט:</strong> זהו השם לפתרון פוטנציאלי אחד לבעיה. בסימולציה שלנו, כל כרומוזום הוא רצף של "צעדים" המייצגים מסלול אפשרי על הרשת.</li>
        <li><strong>גן:</strong> יחידת המידע הקטנה ביותר בכרומוזום. אצלנו, כל "גן" הוא צעד בודד במסלול (למעלה, למטה, ימינה, שמאלה).</li>
        <li><strong>אוכלוסייה:</strong> קבוצה של כרומוזומים (פתרונות) שמתפתחים יחד בכל דור.</li>
        <li><strong>פונקציית התאמה (Fitness Function):</strong> הלב הפועם של האלגוריתם! זוהי פונקציה שמדרגת את "איכות" או "טיב" הפתרון שמייצג כל פרט. ציון התאמה גבוה פירושו שהפתרון טוב יותר. בסימולציה, הציון מחושב לפי כמה המסלול קרוב ליעד, האם הוא נתקל במכשולים, ומה אורכו (מסלול קצר שמגיע ליעד בלי מכשולים יקבל ציון גבוה במיוחד).</li>
    </ul>

    <h3>כלי האבולוציה: האופרטורים הגנטיים</h3>
    <p>אלו הם הכלים שאיתם האלגוריתם בונה את הדור הבא של הפתרונות:</p>
    <ul>
        <li><strong>סלקציה (Selection):</strong> בוחרים את הפרטים ה"מוצלחים" מהדור הנוכחי שיהפכו ל"הורים" של הדור הבא. הסיכוי להיבחר גבוה יותר ככל שציון ההתאמה גבוה יותר. זה מחקה את הברירה הטבעית.</li>
        <li><strong>קרוסאובר או הכלאה (Crossover):</strong> לוקחים מידע משני הורים (למשל, חצי מסלול מהורה א' וחצי מהורה ב') ומחברים אותו ליצירת צאצא חדש. זה מאפשר שילוב תכונות טובות משני פתרונות קיימים.</li>
        <li><strong>מוטציה (Mutation):</strong> שינוי אקראי קטן באחד ה"גנים" (צעדים) של הצאצא. זהו מרכיב קריטי שמבטיח שהאלגוריתם לא "יתקע" בפתרון בינוני ומאפשר גילוי פתרונות חדשים לגמרי.</li>
    </ul>

    <h3>מעגל החיים של אלגוריתם גנטי:</h3>
    <ol>
        <li><strong>אתחול:</strong> יוצרים אוכלוסייה התחלתית של פתרונות אקראיים לחלוטין.</li>
        <li><strong>הערכה:</strong> מחשבים את ציון ההתאמה (Fitness) של כל פתרון באוכלוסייה באמצעות פונקציית ההתאמה.</li>
        <li><strong>סלקציה:</strong> בוחרים את הפתרונות הטובים ביותר מהדור הנוכחי שיהיו הורים לדור הבא.</li>
        <li><strong>הכלאה:</strong> משלבים (מכליאים) את הפתרונות של ההורים כדי ליצור פתרונות חדשים (צאצאים).</li>
        <li><strong>מוטציה:</strong> מכניסים שינויים אקראיים קטנים בחלק מהצאצאים.</li>
        <li><strong>החלפה:</strong> מחליפים את האוכלוסייה הישנה באוכלוסייה החדשה (שילוב של ההורים הטובים ביותר והצאצאים החדשים).</li>
        <li><strong>חזרה:</strong> ממשיכים לחזור על שלבים 2-6 שוב ושוב (יוצרים דורות חדשים) עד שמוצאים פתרון מספיק טוב או שעובר מספר דורות מוגדר מראש.</li>
    </ol>

    <h3>בעיית המסלול ברשת: איך הסימולציה ממחישה זאת?</h3>
    <p>הסימולציה שלפניכם מציגה GA שמנסה למצוא את המסלול הטוב ביותר מנקודת ההתחלה (ירוק) לנקודת הסיום (אדום) על רשת, תוך הימנעות ממכשולים שהצבתם (אפור כהה). כל "פרט" באוכלוסייה הוא מסלול פוטנציאלי (רצף של צעדים). האלגוריתם מתחיל עם אוסף מסלולים אקראיים, ודור אחר דור "מפתח" מסלולים הולכים ומשתפרים, המתקרבים יותר ויותר ליעד תוך עקיפת המכשולים.</p>

    <h3>למה אלגוריתמים גנטיים שימושיים? יתרונות וחסרונות</h3>
    <p><strong>יתרונות מרכזיים:</strong></p>
    <ul>
        <li><strong>כוח חיפוש:</strong> מצוינים באיתור פתרונות טובים גם בבעיות סבוכות עם מרחבי חיפוש עצומים ומורכבים.</li>
        <li><strong>גמישות:</strong> לא דורשים ידע מעמיק על המבנה המדויק של הפתרון הטוב ביותר או על פונקציית ההתאמה – הם פשוט עובדים מול ציון ההתאמה של כל פתרון.</li>
        <li><strong>עמידות:</strong> בזכות מנגנוני ההכלאה והמוטציה, הם נוטים פחות "להיתקע" בפתרונות מקומיים (טובים אבל לא הטובים ביותר גלובלית) בהשוואה לשיטות אופטימיזציה אחרות.</li>
        <li><strong>מקביליות:</strong> קלים יחסית ליישום בסביבות חישוביות מקבילות, מה שיכול לזרז מאוד את פעולתם.</li>
    </ul>
    <p><strong>חסרונות שכדאי להכיר:</strong></p>
    <ul>
        <li><strong>אין הבטחת אופטימליות גלובלית:</strong> לא תמיד מובטח שיגיעו לפתרון הטוב ביותר *מכל* הפתרונות האפשריים (בפרט בזמן ריצה סביר).</li>
        <li><strong>זמן ריצה:</strong> יכולים להיות איטיים בקצב ההתכנסות שלהם לפתרון.</li>
        <li><strong>רגישות לפרמטרים:</strong> ביצועיהם תלויים מאוד בהגדרת הפרמטרים כמו גודל אוכלוסייה, קצבי מוטציה והכלאה, ובאופן שבו מקודדים את הפתרון (ייצוג הכרומוזום).</li>
        <li><strong>קושי בניתוח:</strong> מסובך לנתח אותם תיאורטית ולקבוע מראש את זמן הריצה המדויק או את איכות הפתרון שיימצא.</li>
    </ul>

    <h3>איפה פוגשים אלגוריתמים גנטיים בחיים?</h3>
    <ul>
        <li><strong>לוגיסטיקה ותזמון:</strong> אופטימיזציה של מסלולים (מכוניות משלוח, טיסות), קביעת לוחות זמנים (ייצור, פרויקטים).</li>
        <li><strong>תכנון ועיצוב:</strong> אופטימיזציית תכנון שבבים אלקטרוניים, עיצוב אנטנות, אופטימיזציית מבנים הנדסיים.</li>
        <li><strong>פיננסים:</strong> בניית תיקי השקעות אופטימליים, מודלים לחיזוי.</li>
        <li><strong>בינה מלאכותית ולמידת מכונה:</strong> אופטימיזציה של פרמטרים במודלים מורכבים.</li>
        <li><strong>ביו-אינפורמטיקה:</strong> יישור רצפי DNA/חלבון, חיזוי מבנה חלבון.</li>
        <li><strong>אומנות ומוזיקה:</strong> יצירת אומנות או מנגינות באמצעות תהליך אבולוציוני.</li>
    </ul>
    <p>הסימולציה הקטנה הזו מספקת רק הצצה ראשונה לעולם המרתק של אבולוציה חישובית. נסו לשנות את ההגדרות ולראות כיצד הן משפיעות על קצב ואיכות מציאת המסלול!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('ga-canvas');
    const ctx = canvas.getContext('2d');
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const resetBtn = document.getElementById('resetBtn'); // Added reset button
    const popSizeInput = document.getElementById('popSize');
    const mutationRateInput = document.getElementById('mutationRate');
    const crossoverRateInput = document.getElementById('crossoverRate');
    const maxPathLengthInput = document.getElementById('maxPathLength');
    const currentGenerationSpan = document.getElementById('currentGeneration');
    const bestFitnessSpan = document.getElementById('bestFitness');
    const bestPathLengthSpan = document.getElementById('bestPathLength');
    const reachedEndStatusSpan = document.getElementById('reachedEndStatus'); // Added reached end status
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('explanation');

    const GRID_SIZE = 25; // Increased grid size for more complex problems
    const CELL_SIZE = 18; // Adjusted cell size
    canvas.width = GRID_SIZE * CELL_SIZE;
    canvas.height = GRID_SIZE * CELL_SIZE;

    let startNode = { x: 0, y: 0 };
    let endNode = { x: GRID_SIZE - 1, y: GRID_SIZE - 1 };
    let obstacles = {}; // Use an object for faster lookups { "x,y": true }

    let population = [];
    let generation = 0;
    let running = false;
    let simulationInterval = null; // Interval for generations
    let animationFrameId = null; // For path animation

    // --- Grid Interaction (Obstacles) ---
    canvas.addEventListener('click', (event) => {
        if (running) return; // Don't change grid while running

        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width; // Handle potential scaling
        const scaleY = canvas.height / rect.height;
        const x = Math.floor(((event.clientX - rect.left) * scaleX) / CELL_SIZE);
        const y = Math.floor(((event.clientY - rect.top) * scaleY) / CELL_SIZE);
        const pos = `${x},${y}`;

        // Prevent placing obstacles on start or end
        if ((x === startNode.x && y === startNode.y) || (x === endNode.x && y === endNode.y)) {
            return;
        }

        if (obstacles[pos]) {
            delete obstacles[pos];
        } else {
            obstacles[pos] = true;
        }
        drawGrid(); // Redraw the grid with new obstacles
         // Clear potential previous path drawings
        // drawGrid(); should already clear, but good to be explicit if needed
    });

    resetBtn.addEventListener('click', () => {
        if (running) return;
        obstacles = {};
        generation = 0; // Reset status display
        currentGenerationSpan.textContent = 0;
        bestFitnessSpan.textContent = '---';
        bestPathLengthSpan.textContent = '---';
        reachedEndStatusSpan.textContent = 'לא';
        population = []; // Clear population
        drawGrid(); // Redraw empty grid
    });


    // --- Drawing & Animation Functions ---
    function drawGrid() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.strokeStyle = varDict['--border-color']; // Use CSS variable
        ctx.lineWidth = 1;

        for (let i = 0; i < GRID_SIZE; i++) {
            for (let j = 0; j < GRID_SIZE; j++) {
                // Draw cell background if obstacle
                const pos = `${i},${j}`;
                if (obstacles[pos]) {
                     ctx.fillStyle = varDict['--obstacle-color'];
                    ctx.fillRect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE);
                }
                 // Draw grid lines
                ctx.strokeRect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE);
            }
        }

        // Draw Start
        ctx.fillStyle = varDict['--start-color'];
        ctx.fillRect(startNode.x * CELL_SIZE, startNode.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);

        // Draw End
        ctx.fillStyle = varDict['--end-color'];
        ctx.fillRect(endNode.x * CELL_SIZE, endNode.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);

         // Add subtle border/outline for start/end for clarity
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 2;
        ctx.strokeRect(startNode.x * CELL_SIZE, startNode.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
        ctx.strokeRect(endNode.x * CELL_SIZE, endNode.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
         ctx.lineWidth = 1; // Reset line width
    }

    // Animated path drawing
    function animatePath(path, color = varDict['--path-color'], duration = 1000) {
        let currentX = startNode.x;
        let currentY = startNode.y;
        let stepIndex = 0;
        const startTime = performance.now();

        function drawStep(timestamp) {
            const elapsed = timestamp - startTime;
            // Determine how many steps to draw based on elapsed time
            const stepsToDraw = Math.min(path.length, Math.floor((elapsed / duration) * path.length));

             // Redraw grid first
            drawGrid();

            // Draw path up to stepsToDraw
            ctx.strokeStyle = color;
            ctx.lineWidth = 3; // Thicker path line
            ctx.lineCap = 'round'; // Rounded ends
            ctx.lineJoin = 'round'; // Rounded corners

            ctx.beginPath();
            ctx.moveTo(startNode.x * CELL_SIZE + CELL_SIZE / 2, startNode.y * CELL_SIZE + CELL_SIZE / 2);

            let tempX = startNode.x;
            let tempY = startNode.y;

            for (let i = 0; i < stepsToDraw; i++) {
                 const move = path[i];
                 let nextX = tempX;
                 let nextY = tempY;

                 if (move === 0) nextY--; // Up
                 else if (move === 1) nextY++; // Down
                 else if (move === 2) nextX--; // Left
                 else if (move === 3) nextX++; // Right

                 // Check boundaries and obstacles for drawing validity
                 const pos = `${nextX},${nextY}`;
                 if (nextX < 0 || nextX >= GRID_SIZE || nextY < 0 || nextY >= GRID_SIZE || obstacles[pos]) {
                      // Path hits obstacle or boundary, stop drawing segment
                      break;
                 }

                 ctx.lineTo(nextX * CELL_SIZE + CELL_SIZE / 2, nextY * CELL_SIZE + CELL_SIZE / 2);
                 tempX = nextX;
                 tempY = nextY;
            }
            ctx.stroke();

            if (stepsToDraw < path.length && elapsed < duration) {
                animationFrameId = requestAnimationFrame(drawStep);
            } else {
                 // Animation finished
                 animationFrameId = null;
            }
        }

        // Cancel any previous animation frame
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        animationFrameId = requestAnimationFrame(drawStep);
    }


    // --- GA Core Logic ---

    // Path representation: 0: Up, 1: Down, 2: Left, 3: Right
    // Individual: { path: [moves], fitness: number, hitObstacle: boolean, reachedEnd: boolean, actualLength: number }

    function createRandomPath(maxLength) {
        const path = [];
        for (let i = 0; i < maxLength; i++) {
            path.push(Math.floor(Math.random() * 4)); // 0, 1, 2, or 3
        }
        return path;
    }

    function evaluateFitness(individual) {
        let currentX = startNode.x;
        let currentY = startNode.y;
        let hitObstacle = false;
        let reachedEnd = false;
        let actualLength = 0;
        let pathSegments = []; // To store valid path coordinates

        // Start point
        pathSegments.push({x: currentX, y: currentY});

        for (const move of individual.path) {
            let nextX = currentX;
            let nextY = currentY;

            if (move === 0) nextY--; // Up
            else if (move === 1) nextY++; // Down
            else if (move === 2) nextX--; // Left
            else if (move === 3) nextX++; // Right

            // Check boundaries
            if (nextX < 0 || nextX >= GRID_SIZE || nextY < 0 || nextY >= GRID_SIZE) {
                hitObstacle = true; // Treat hitting boundary as hitting obstacle
                break; // Path is invalid from here
            }

            // Check obstacles
            const pos = `${nextX},${nextY}`;
            if (obstacles[pos]) {
                hitObstacle = true;
                break; // Path hit obstacle, stop
            }

            currentX = nextX;
            currentY = nextY;
            actualLength++; // Count step only if valid
            pathSegments.push({x: currentX, y: currentY});


            // Check if reached end
            if (currentX === endNode.x && currentY === endNode.y) {
                reachedEnd = true;
                break; // Reached end, no need to follow rest of path
            }
        }

        individual.hitObstacle = hitObstacle;
        individual.reachedEnd = reachedEnd;
        individual.actualLength = actualLength; // Length until obstacle/end/max length
        individual.currentPos = {x: currentX, y: currentY}; // Store final valid position

        // Fitness calculation:
        // Higher is better. Max possible length is `maxPathLengthInput.value`.
        // Use Manhattan distance to end
        const manhattanDistanceToEnd = Math.abs(individual.currentPos.x - endNode.x) + Math.abs(individual.currentPos.y - endNode.y);
        // Max possible Manhattan distance on the grid
        const maxGridDistance = Math.abs(startNode.x - endNode.x) + Math.abs(startNode.y - endNode.y);


        let fitness = 0;

        if (reachedEnd) {
            // High score for reaching the end + bonus for shorter path
            // Base score for reaching end + points inversely proportional to length
            fitness = 10000 + (maxPathLengthInput.value - actualLength); // Reward shorter path if reached
        } else if (hitObstacle) {
             // Heavy penalty for hitting an obstacle/boundary
             // Still give some credit for getting closer before hitting
             fitness = -1000 + (maxGridDistance - manhattanDistanceToEnd) * 10; // Reward getting closer even if obstacle hit
        }
        else {
             // Haven't reached end, haven't hit obstacle (yet)
             // Reward getting closer to the end
             fitness = (maxGridDistance - manhattanDistanceToEnd) * 20; // Stronger reward for reducing distance
             // Penalize long paths that haven't reached the end
             fitness -= actualLength;
        }

        individual.fitness = fitness;
    }


    function initializePopulation(popSize, maxPathLength) {
        population = [];
        for (let i = 0; i < popSize; i++) {
            const individual = { path: createRandomPath(maxPathLength), fitness: 0 };
            // No need to evaluate fitness during initialization based on original structure
            // Will evaluate the whole population after creation
            population.push(individual);
        }
         // Evaluate initial population
        population.forEach(evaluateFitness);
    }

    // Selection: Tournament Selection (slightly refined)
    function selectParent(tournamentSize = 5) {
        let best = null;
        // Ensure tournament size doesn't exceed population size
        const currentTournamentSize = Math.min(tournamentSize, population.length);
        for (let i = 0; i < currentTournamentSize; i++) {
            const randomIndex = Math.floor(Math.random() * population.length);
            const randomIndividual = population[randomIndex];
            if (best === null || randomIndividual.fitness > best.fitness) {
                best = randomIndividual;
            }
        }
        return best;
    }

    // Crossover: Single Point Crossover
    function crossover(parent1, parent2, crossoverRate) {
        // Return copies if crossover doesn't happen
        if (Math.random() * 100 > crossoverRate) { // Use rate directly
            return [{ path: [...parent1.path] }, { path: [...parent2.path] }];
        }

        const pathLength = Math.min(parent1.path.length, parent2.path.length); // Use min length in case of different lengths
        const crossoverPoint = Math.floor(Math.random() * (pathLength)); // Point can be 0 up to length-1

        const child1Path = [...parent1.path.slice(0, crossoverPoint), ...parent2.path.slice(crossoverPoint)];
        const child2Path = [...parent2.path.slice(0, crossoverPoint), ...parent1.path.slice(crossoverPoint)];

         // Pad paths if necessary to maxPathLength (this shouldn't be needed if parents had same length)
         const maxLength = parseInt(maxPathLengthInput.value);
         while(child1Path.length < maxLength) child1Path.push(Math.floor(Math.random() * 4));
         while(child2Path.length < maxLength) child2Path.push(Math.floor(Math.random() * 4));


        return [{ path: child1Path.slice(0, maxLength) }, { path: child2Path.slice(0, maxLength) }]; // Ensure max length
    }

    // Mutation
    function mutate(individual, mutationRate) {
        // Mutate based on percentage rate * per gene
        for (let i = 0; i < individual.path.length; i++) {
            if (Math.random() * 100 < mutationRate) { // Use rate directly
                // Change the gene (move) randomly
                individual.path[i] = Math.floor(Math.random() * 4);
            }
        }
    }

     // Get CSS variables
    const varDict = {};
    const style = getComputedStyle(document.documentElement);
    ['--primary-color', '--secondary-color', '--accent-color', '--obstacle-color', '--start-color', '--end-color', '--path-color', '--border-color', '--text-color', '--subtle-text-color', '--bg-color', '--card-bg-color'].forEach(prop => {
        varDict[prop] = style.getPropertyValue(prop).trim();
    });


    // Main GA loop step
    function nextGeneration() {
        generation++;
        const newPopulation = [];
        const popSize = parseInt(popSizeInput.value);
        const mutationRate = parseFloat(mutationRateInput.value); // Use float
        const crossoverRate = parseInt(crossoverRateInput.value);
        const maxPathLength = parseInt(maxPathLengthInput.value);

        // Elitism: Keep the best individual from the previous generation
        let bestIndividualThisGen = population.reduce((best, current) => (current.fitness > best.fitness ? current : best), population[0]);
        newPopulation.push({...bestIndividualThisGen}); // Add a copy of the best

        // Generate new individuals
        while (newPopulation.length < popSize) {
            // Selection
            const parent1 = selectParent();
            const parent2 = selectParent();

            // Crossover (returns 2 children potentially)
            const children = crossover(parent1, parent2, crossoverRate);

            // Mutation for children
            mutate(children[0], mutationRate);
            // Only mutate and add the second child if there's room
             if (newPopulation.length + 1 < popSize) { // Check if there's space for a second child
                mutate(children[1], mutationRate);
                 if (newPopulation.length < popSize) newPopulation.push(children[1]); // Add second child if space
             }


            // Add first child
             if (newPopulation.length < popSize) newPopulation.push(children[0]);


        }

        // Ensure population size is exactly popSize (in case rounding or elitism added too many)
         while (newPopulation.length > popSize) {
             newPopulation.pop(); // Remove excess from the end
         }


        // Evaluate new population
        newPopulation.forEach(evaluateFitness);

        population = newPopulation;

        // Find the absolute best individual across all generations (optional, but common)
        // For this demo, let's just track the best of the current generation
        const bestIndividualOverall = population.reduce((best, current) => (current.fitness > best.fitness ? current : best), population[0]);


        // Update status display
        currentGenerationSpan.textContent = generation;
        bestFitnessSpan.textContent = bestIndividualOverall.fitness.toFixed(2); // Display fitness with 2 decimal places
        bestPathLengthSpan.textContent = bestIndividualOverall.reachedEnd ? bestIndividualOverall.actualLength : '---';
        reachedEndStatusSpan.textContent = bestIndividualOverall.reachedEnd ? 'כן!' : 'לא';
         reachedEndStatusSpan.style.color = bestIndividualOverall.reachedEnd ? varDict['--start-color'] : varDict['--subtle-text-color'];


        // Draw the grid and ANIMATE the best path
        animatePath(bestIndividualOverall.path);

        // Optional: Stop condition (e.g., reached optimal fitness, reached max generations)
         if (bestIndividualOverall.reachedEnd && bestIndividualOverall.actualLength <= maxPathLength) { // Check if reached AND within path length limit
            console.log(`Goal reached at generation ${generation}! Best fitness: ${bestIndividualOverall.fitness}`);
            stopSimulation();
             // Draw the final winning path without animation after stopping
            drawGrid(); // Clear grid
            drawPath(bestIndividualOverall.path); // Draw path statically
         }
         // Removed arbitrary max generations stop for more open-ended simulation,
         // but could add back: `if (generation >= 1000) { stopSimulation(); }`

    }

     // Static draw path function (for final result display)
     function drawPath(path, color = varDict['--path-color']) {
         ctx.strokeStyle = color;
         ctx.lineWidth = 3;
         ctx.lineCap = 'round';
         ctx.lineJoin = 'round';
         ctx.beginPath();
         ctx.moveTo(startNode.x * CELL_SIZE + CELL_SIZE / 2, startNode.y * CELL_SIZE + CELL_SIZE / 2);

         let currentX = startNode.x;
         let currentY = startNode.y;

         for (const move of path) {
             let nextX = currentX;
             let nextY = currentY;
             if (move === 0) nextY--; // Up
             else if (move === 1) nextY++; // Down
             else if (move === 2) nextX--; // Left
             else if (move === 3) nextX++; // Right

             const pos = `${nextX},${nextY}`;
             // Only draw valid steps within bounds and not hitting obstacles
             if (nextX >= 0 && nextX < GRID_SIZE && nextY >= 0 && nextY < GRID_SIZE && !obstacles[pos]) {
                  ctx.lineTo(nextX * CELL_SIZE + CELL_SIZE / 2, nextY * CELL_SIZE + CELL_SIZE / 2);
                  currentX = nextX;
                  currentY = nextY;
                  // Stop drawing if reached end, even if path is longer
                  if (currentX === endNode.x && currentY === endNode.y) {
                      break;
                  }
             } else {
                  // Path hit obstacle or boundary, stop drawing the rest of the path
                  break;
             }
         }
         ctx.stroke();
     }


    function startSimulation() {
        if (running) return;
        running = true;
        generation = 0; // Ensure generation starts from 0 on new run
        const popSize = parseInt(popSizeInput.value);
        const maxPathLength = parseInt(maxPathLengthInput.value);

        // Basic validation
        if (popSize < 50 || maxPathLength < 20) {
            alert("גודל אוכלוסייה חייב להיות לפחות 50 ואורך מסלול מקסימלי לפחות 20.");
            running = false;
            return;
        }

        initializePopulation(popSize, maxPathLength); // Initialize population for the first time
        nextGeneration(); // Run the first generation immediately

        startBtn.disabled = true;
        stopBtn.disabled = false;
        resetBtn.disabled = true; // Disable reset while running
        popSizeInput.disabled = true;
        mutationRateInput.disabled = true;
        crossoverRateInput.disabled = true;
        maxPathLengthInput.disabled = true;
        canvas.style.cursor = 'default'; // Prevent clicking obstacles while running

        // Run simulation steps periodically
        // Run faster if possible, maybe 50ms per generation
        simulationInterval = setInterval(nextGeneration, 50); // Run a generation every 50ms
    }

    function stopSimulation() {
        if (!running) return;
        running = false;
        clearInterval(simulationInterval);
        simulationInterval = null;
         // Cancel any pending animation frame
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
             animationFrameId = null;
         }

        startBtn.disabled = false;
        stopBtn.disabled = true;
        resetBtn.disabled = false; // Enable reset after stopping
        popSizeInput.disabled = false;
        mutationRateInput.disabled = false;
        crossoverRateInput.disabled = false;
        maxPathLengthInput.disabled = false;
        canvas.style.cursor = 'pointer'; // Allow clicking obstacles again

         // Draw the final best path statically
        const bestIndividualOverall = population.reduce((best, current) => (current.fitness > best.fitness ? current : best), population[0]);
        drawGrid(); // Clear animation artifacts
        if(bestIndividualOverall) {
             drawPath(bestIndividualOverall.path);
        } else {
             drawGrid(); // If population is empty, just redraw grid
        }
    }

    // --- Initial Setup ---
    drawGrid(); // Draw the initial empty grid

    startBtn.addEventListener('click', startSimulation);
    stopBtn.addEventListener('click', stopSimulation);


    // --- Explanation Toggle ---
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר על אלגוריתמים גנטיים' : 'רוצים להבין איך הקסם עובד? לחצו כאן להסבר על אלגוריתמים גנטיים';
         // Scroll to the explanation section if opening it
         if (isHidden) {
              explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Initialize explanation state
    explanationDiv.style.display = 'none';

});
</script>