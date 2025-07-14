---
title: "איזון עדין: משחק ניהול משאבי טבע"
english_slug: delicate-balance-natural-resource-management-game
category: "כללי"
tags:
  - משאבי טבע
  - קיימות
  - מערכת אקולוגית
  - משחק סימולציה
  - קריסה אקולוגית
---
# איזון עדין: משחק ניהול משאבי טבע

ברוכים הבאים לאי הטרופי הציורי "איזון"! כאן, שגשוג האדם תלוי לחלוטין בשמירה על בריאותה של המערכת האקולוגית העשירה אך העדינה. כראש האי, ההחלטות שלך לגבי ניצול יערות, דגה וחיות בר יקבעו אם האי ישגשג לדורות, או יקרוס תחת עומס ניצול היתר. האם תוכל למצוא את האיזון הנכון?

<div id="game-container" dir="rtl">
    <div id="island-header">
        <h2>שנה: <span id="year">1</span></h2>
    </div>

    <div id="island-map">
        <div class="resource forest">
            <div class="resource-icon">🌳</div>
            <div class="resource-name">יער</div>
            <div class="resource-level"><span id="forest-level"></span> עצים</div>
            <div class="resource-bar"><div id="forest-bar" class="bar"></div></div>
        </div>
        <div class="resource fish">
            <div class="resource-icon">🐟</div>
            <div class="resource-name">דגים</div>
            <div class="resource-level"><span id="fish-level"></span> טון</div>
            <div class="resource-bar"><div id="fish-bar" class="bar"></div></div>
        </div>
        <div class="resource wildlife">
            <div class="resource-icon">🦌</div>
            <div class="resource-name">חיות בר</div>
            <div class="resource-level"><span id="wildlife-level"></span> פרטים</div>
            <div class="resource-bar"><div id="wildlife-bar" class="bar"></div></div>
        </div>
    </div>

    <div id="controls">
        <h3>החלטות ניצול לשנה זו:</h3>
        <div class="control">
            <label for="cut-trees">כריתת עצים (אלפי עצים):</label>
            <input type="range" id="cut-trees" value="0" min="0" max="500" step="1">
            <span id="cut-trees-value">0</span>
        </div>
        <div class="control">
            <label for="catch-fish">דיג (טון):</label>
            <input type="range" id="catch-fish" value="0" min="0" max="500" step="1">
            <span id="catch-fish-value">0</span>
        </div>
        <div class="control">
            <label for="hunt-wildlife">ציד חיות בר (פרטים):</label>
            <input type="range" id="hunt-wildlife" value="0" min="0" max="500" step="1">
             <span id="hunt-wildlife-value">0</span>
        </div>
        <button id="next-year">התקדם לשנה הבאה</button>
    </div>

    <div id="status-messages">
        <h3>מצב המערכת האקולוגית:</h3>
        <p id="game-status"></p>
        <div id="resource-status">
             <p>קצב התחדשות יער בשנה הבאה: <span id="forest-regeneration"></span> אלפי עצים</p>
             <p>קצב התחדשות דגים בשנה הבאה: <span id="fish-regeneration"></span> טון</p>
             <p>קצב התחדשות חיות בר בשנה הבאה: <span id="wildlife-regeneration"></span> פרטים</p>
        </div>
    </div>

    <div id="game-over-screen" style="display: none;">
        <div class="game-over-content">
            <h2>המשחק הסתיים!</h2>
            <p id="final-message"></p>
            <p>האי שרד <span id="final-year"></span> שנים תחת ניהולך.</p>
            <button id="restart-game">התחל אי חדש</button>
        </div>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר הסבר מעמיק</button>

<div id="explanation" style="display: none;" dir="rtl">
    <h2>איזון עדין: מדריך למנהל אי בר-קיימא</h2>
    <p>ברוכים הבאים לאיזון! המשחק הזה מדמה את המורכבות והאתגרים הכרוכים בניהול משאבי טבע מתחדשים. הוא נועד להמחיש כיצד פעולות הניצול שלנו משפיעות על הבריאות ארוכת הטווח של המערכת האקולוגית ועל יכולתה להתחדש.</p>

    <h3>מהם משאבי טבע? מתחדשים מול בלתי מתחדשים</h3>
    <p>משאבי טבע הם אוצרות כדור הארץ - חומרים ואנרגיה שמגיעים ישירות מהסביבה הטבעית ומשמשים אותנו לחיי היומיום. ישנם משאבים <strong>מתחדשים</strong>, כמו היערות, הדגים באוקיינוס, המים המתוקים או אנרגיית השמש והרוח. אלה מתחדשים בקצב טבעי, בתנאי שניצולם אינו עולה על קצב ההתחדשות. לעומתם, יש משאבים <strong>בלתי מתחדשים</strong>, כמו נפט, גז טבעי, פחם ומינרלים. אלה נוצרו בתהליכים גאולוגיים איטיים מאוד, וקיימים בכמות סופית על פני כדור הארץ. ניצולם מוביל לדלדול מלאי שאינו מתחדש בקנה מידה אנושי.</p>

    <h3>מערכות אקולוגיות: רשתות חיים מורכבות</h3>
    <p>מערכת אקולוגית אינה רק אוסף של צמחים ובעלי חיים, אלא רשת דינמית של יחסי גומלין סבוכים בין יצורים חיים לבין סביבתם הדוממת (אדמה, מים, אוויר, אור שמש). כל רכיב במערכת קשור לאחרים - עצים ביער מספקים מזון ומחסה לחיות הבר, יערות משפיעים על איכות המים ומונעים סחף קרקע שיכול לפגוע בשוניות אלמוגים ודגה בחוף, וכו'. שינוי בחלק אחד של המערכת יכול להדהד ולהשפיע על חלקים אחרים בצורות בלתי צפויות ולעיתים הרסניות.</p>

    <h3>כושר נשיאה וקצבי התחדשות: גבולות הצמיחה</h3>
    <p>לכל סביבה יש יכולת טבעית מוגבלת לתמוך באוכלוסיות או במשאבים מסוימים. זוהי ה"כושר נשיאה" הביולוגי שלה. למשל, יער מסוים יכול לקיים מספר מסוים של עצים, או אגם יכול לתמוך באוכלוסיית דגים בגודל מסוים. במקביל, לכל משאב מתחדש יש "קצב התחדשות טבעי" - המהירות שבה הוא מתרבה או גדל מחדש (למשל, כמה טון דגים חדשים נולדים בשנה, או כמה עץ גדל ביער בשנה). אם ניצול המשאב עולה על קצב ההתחדשות, המלאי יחל להתדלדל. אם הניצול עולה גם על כושר הנשיאה לטווח ארוך, המערכת כולה עלולה להיפגע.</p>

    <h3>ספים קריטיים וקריסה אקולוגית: כשהאיזון נשבר</h3>
    <p>מערכות אקולוגיות רבות יכולות להתמודד עם מידה מסוימת של לחץ או ניצול, אך יש להן "סף קריטי" (או "נקודת מפנה"). אם הלחץ חוצה סף זה, המערכת עלולה לעבור שינוי פתאומי, מהיר ולעיתים קרובות בלתי הפיך. לדוגמה, דיג יתר אינטנסיבי עלול להקטין את אוכלוסיית הדגים לרמה כה נמוכה, עד שהיא מאבדת את יכולת ההתאוששות שלה גם אם הדיג פוסק לגמרי. היער יכול להפוך למדבר, ואוכלוסיות חיות בר יכולות להיכחד במהירות. קריסה כזו משפיעה כמובן גם על האדם התלוי במשאבים אלה.</p>

    <h3>ניהול בר קיימא: ראייה ארוכת טווח</h3>
    <p>"ניהול בר קיימא" של משאבי טבע פירושו ניצול שלהם בקצב שאינו פוגע ביכולתם לשרת גם את הדורות הבאים. המטרה היא לחיות "בתוך האמצעים" של הטבע, ולשמור על בריאותה ותפקודה של המערכת האקולוגית. זה דורש לא רק הבנה של קצבי התחדשות וכושר נשיאה, אלא גם חשיבה לטווח ארוך, מעקב צמוד אחר מצב המשאבים (ניטור), ונכונות להתאים את מדיניות הניצול בהתאם לממצאים (ניהול אדפטיבי).</p>

    <h3>שיעורים מהעבר ומההווה</h3>
    <p>ההיסטוריה האנושית וגם ימינו אנו עדים לקריסות אקולוגיות שהיו תוצאה של ניהול משאבים כושל: קריסת דגת הבקלה באוקיינוס האטלנטי, מדבור שטחים נרחבים באפריקה, וקריסתן (החלקית או המלאה) של תרבויות עתיקות שפגעו אנושות בסביבתן. משחקי סימולציה כמו זה נועדו לעזור לנו להבין את הדינמיקה המורכבת של מערכות אקולוגיות ואת ההשלכות של ניצול לא מושכל, כדי שנוכל ללמוד מהטעויות הללו.</p>

    <h3>הקשר האנושי: רווחה וכלכלה</h3>
    <p>ניהול בר קיימא אינו רק עניין סביבתי, אלא גם כלכלי וחברתי מהמעלה הראשונה. בריאותן של מערכות אקולוגיות מספקת לנו "שירותי מערכת אקולוגית" חיוניים כמו מים נקיים, אוויר נקי, אדמה פורייה, האבקה וכו'. פגיעה במערכות אלה עלולה לערער את היציבות הכלכלית, ליצור מחסור במזון ומים, ואף להוביל לסכסוכים חברתיים ואזוריים. ניהול מושכל של המשאבים הוא הבסיס לשגשוג אנושי בר קיימא.</p>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: #e0f0f0; /* Light blue-green background */
        color: #333;
    }

    #game-container {
        border: 1px solid #ccc;
        padding: 30px;
        margin: 20px auto;
        border-radius: 12px;
        background-color: #ffffff; /* White background for game */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 700px; /* Limit game width */
    }

    #island-header {
        text-align: center;
        margin-bottom: 20px;
        color: #0056b3; /* Darker blue */
    }
    #island-header h2 {
        margin: 0;
        font-size: 2em;
    }

    #island-map {
        display: flex;
        justify-content: space-around;
        margin-bottom: 30px;
        padding: 15px;
        background: linear-gradient(to bottom, #a8e6cf, #dcedc1); /* Light green gradient */
        border-radius: 8px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .resource {
        flex: 1;
        margin: 0 10px;
        padding: 15px;
        border-radius: 8px;
        color: white;
        text-align: center;
        min-width: 100px;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Add transition */
    }
    .resource:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25);
    }

    .resource-icon {
        font-size: 2em;
        margin-bottom: 5px;
    }
    .resource-name {
        font-size: 1.1em;
        margin-bottom: 8px;
    }
    .resource-level {
         font-size: 0.9em;
         margin-bottom: 10px;
         min-height: 1.2em; /* Prevent jump when text changes */
    }

    .resource-bar {
        width: 90%;
        height: 10px;
        background-color: rgba(255, 255, 255, 0.3); /* Semi-transparent white background for bar */
        border-radius: 5px;
        overflow: hidden;
        margin-top: 5px;
    }
    .resource-bar .bar {
        height: 100%;
        width: 100%; /* Initial width */
        background-color: white; /* Default bar color */
        transition: width 0.5s ease-out; /* Smooth bar animation */
    }

    /* Resource specific colors */
    .forest { background-color: #388E3C; } /* Green */
    .fish { background-color: #1976D2; } /* Blue */
    .wildlife { background-color: #F57C00; } /* Orange */

     /* Warning and Critical colors - overrides default */
    .forest.warning { background-color: #FBC02D; } /* Yellow */
    .forest.critical { background-color: #D32F2F; } /* Red */
    .fish.warning { background-color: #4FC3F7; } /* Light Blue */
    .fish.critical { background-color: #D32F2F; } /* Red */
    .wildlife.warning { background-color: #FFB74D; } /* Light Orange */
    .wildlife.critical { background-color: #D32F2F; } /* Red */


    #controls {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid #eee;
        border-radius: 8px;
        background-color: #f9f9f9;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }
    #controls h3 {
        margin-top: 0;
        color: #0056b3;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }
    .control {
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }
    .control label {
        display: inline-block;
        margin-left: 10px; /* Space between label and slider */
        font-weight: bold;
        width: 150px; /* Fixed width for alignment */
    }
    .control input[type="range"] {
        flex-grow: 1; /* Slider takes available space */
        margin: 0 10px; /* Space around slider */
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 8px;
        background: #ddd;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 5px;
    }
    .control input[type="range"]:hover {
        opacity: 1;
    }
     .control input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #4CAF50; /* Green thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }
     .control input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #4CAF50; /* Green thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }
    .control span {
        display: inline-block;
        min-width: 30px; /* Ensure space for value */
        text-align: left; /* Align value to the left of the number */
         font-weight: bold;
         color: #555;
    }


    button {
        display: block; /* Make button take full width */
        width: 100%;
        padding: 12px 20px;
        background-color: #2196F3; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
    button:hover {
        background-color: #0b7dda; /* Darker blue */
    }
    button:active {
        transform: scale(0.98);
    }
     button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
     }

    #toggle-explanation {
         background-color: #607D8B; /* Greyish blue */
         margin: 20px auto; /* Center button */
         display: block;
         width: auto; /* Allow width to be determined by content/padding */
         padding: 10px 15px;
         font-size: 1em;
         border-radius: 5px;
    }
     #toggle-explanation:hover {
         background-color: #455A64;
    }


    #status-messages {
        margin-bottom: 20px;
        padding: 20px;
        border: 1px solid #eee;
        border-radius: 8px;
        background-color: #f9f9f9;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }
    #status-messages h3 {
        margin-top: 0;
        color: #0056b3;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }
    #game-status {
        font-weight: bold;
        color: #333;
        margin-bottom: 15px;
        min-height: 1.2em; /* Prevent layout shifts */
    }
    #resource-status p {
        margin: 8px 0;
        font-size: 0.9em;
        color: #555;
    }

     #game-over-screen {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.9); /* Darker overlay */
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        z-index: 1000;
        animation: fadeIn 0.5s ease-out;
    }
    .game-over-content {
        background-color: #ffffff;
        color: #333;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
         max-width: 90%;
    }
    #game-over-screen h2 {
        font-size: 2.8em;
        margin-top: 0;
        margin-bottom: 20px;
        color: #D32F2F; /* Red color for Game Over */
         animation: scaleUp 0.5s ease-out;
    }
    #game-over-screen p {
        font-size: 1.2em;
        margin-bottom: 15px;
    }
     #game-over-screen button {
        margin-top: 30px;
        background-color: #FF5722; /* Deep Orange */
        width: auto;
        padding: 12px 25px;
        display: inline-block; /* Make button fit content */
     }
     #game-over-screen button:hover {
        background-color: #E64A19;
     }

     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }

      @keyframes scaleUp {
         from { transform: scale(0.8); opacity: 0.8; }
         to { transform: scale(1); opacity: 1; }
     }


    #explanation {
        border: 1px solid #ccc;
        padding: 30px;
        margin: 20px auto;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 700px;
    }
    #explanation h2 {
         color: #0056b3;
         margin-top: 0;
         margin-bottom: 20px;
         border-bottom: 2px solid #eee;
         padding-bottom: 10px;
    }
    #explanation h3 {
        margin-top: 25px;
        margin-bottom: 10px;
        color: #555;
        border-bottom: 1px dashed #eee;
        padding-bottom: 5px;
    }
     #explanation p {
        margin-bottom: 15px;
        text-align: justify; /* Justify text for readability */
     }

</style>

<script>
    let year = 1;
    // Starting levels - considered initial capacity
    const initialForest = 500; // thousands of trees
    const initialFish = 500; // tons
    const initialWildlife = 500; // population

    let forest = initialForest;
    let fish = initialFish;
    let wildlife = initialWildlife;


    // Base Regeneration rates (per year, multiplicative factor)
    // These represent the potential growth rate if resources are not depleted
    const baseForestRegenRate = 0.1; // Base potential to grow 10% per year
    const baseFishRegenRate = 0.15; // Base potential to grow 15% per year
    const baseWildlifeRegenRate = 0.12; // Base potential to grow 12% per year

    // Collapse thresholds (below this, regeneration is severely impacted)
    const forestCollapseThreshold = 100; // Below 100k trees
    const fishCollapseThreshold = 50; // Below 50 tons
    const wildlifeCollapseThreshold = 80; // Below 80 individuals

    // Factors affecting regeneration when below threshold
    const collapseRegenFactor = 0.1; // Regeneration is only 10% of base rate below threshold

     // Interdependencies (how resources affect each other)
     const wildlifeForestDependency = 0.8; // Wildlife regen is scaled by forest level relative to initial (80% impact)

    const maxYears = 50; // Goal: Survive 50 years

    // --- DOM Elements ---
    const yearSpan = document.getElementById('year');
    const forestLevelSpan = document.getElementById('forest-level');
    const fishLevelSpan = document.getElementById('fish-level');
    const wildlifeLevelSpan = document.getElementById('wildlife-level');

    const forestBar = document.getElementById('forest-bar');
    const fishBar = document.getElementById('fish-bar');
    const wildlifeBar = document.getElementById('wildlife-bar');

    const cutTreesInput = document.getElementById('cut-trees');
    const catchFishInput = document.getElementById('catch-fish');
    const huntWildlifeInput = document.getElementById('hunt-wildlife');

     const cutTreesValueSpan = document.getElementById('cut-trees-value');
     const catchFishValueSpan = document.getElementById('catch-fish-value');
     const huntWildlifeValueSpan = document.getElementById('hunt-wildlife-value');


    const nextYearButton = document.getElementById('next-year');
    const gameStatusP = document.getElementById('game-status');
    const forestRegenP = document.getElementById('forest-regeneration');
    const fishRegenP = document.getElementById('fish-regeneration');
    const wildlifeRegenP = document.getElementById('wildlife-regeneration');

    const gameOverScreen = document.getElementById('game-over-screen');
    const finalMessageP = document.getElementById('final-message');
    const finalYearSpan = document.getElementById('final-year');
    const restartGameButton = document.getElementById('restart-game');

    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

     const forestResourceDiv = document.querySelector('.resource.forest');
     const fishResourceDiv = document.querySelector('.resource.fish');
     const wildlifeResourceDiv = document.querySelector('.resource.wildlife');


    // --- Game Logic ---

    function calculateRegeneration(currentLevel, initialCapacity, baseRate, collapseThreshold, dependencyFactor = 1, dependencyResourceLevel = initialCapacity) {
        if (currentLevel <= 0) return 0;

        // Simple logistic-like growth approximation: slower growth near limits (0 and initialCapacity)
        // Regeneration peaks somewhere in the middle
        let regenBasedOnCurrent = currentLevel * baseRate * (1 - currentLevel / (initialCapacity * 1.5)); // Peak regen might be slightly above initial

        // Apply threshold penalty
        let effectiveRegenRate = regenBasedOnCurrent;
        if (currentLevel < collapseThreshold) {
            effectiveRegenRate = regenBasedOnCurrent * collapseRegenFactor;
            // Add a small fixed minimum regen to avoid being stuck at 0 if somehow it's slightly negative
            effectiveRegenRate = Math.max(effectiveRegenRate, initialCapacity * baseRate * 0.01); // minimum 1% of base potential
        }

         // Apply interdependency (e.g., wildlife depends on forest)
         const dependencyScale = dependencyResourceLevel / initialCapacity;
         effectiveRegenRate *= (1 - dependencyFactor + dependencyFactor * dependencyScale);


        // Cap regeneration at a reasonable level (e.g., cannot grow more than 15% of initial capacity in one go, or cannot exceed initial capacity quickly)
        const maxPossibleRegen = initialCapacity * baseRate * 2; // Don't allow explosive growth
        return Math.max(0, Math.min(effectiveRegenRate, maxPossibleRegen));
    }

    function updateDisplay() {
        // Update text values
        yearSpan.textContent = year;
        forestLevelSpan.textContent = forest.toFixed(0);
        fishLevelSpan.textContent = fish.toFixed(0);
        wildlifeLevelSpan.textContent = wildlife.toFixed(0);

        // Update resource bars
        forestBar.style.width = `${Math.max(0, Math.min(100, (forest / initialForest) * 100))}%`;
        fishBar.style.width = `${Math.max(0, Math.min(100, (fish / initialFish) * 100))}%`;
        wildlifeBar.style.width = `${Math.max(0, Math.min(100, (wildlife / initialWildlife) * 100))}%`;

        // Update resource color indicators
        forestResourceDiv.classList.remove('warning', 'critical');
        if (forest < forestCollapseThreshold * 2 && forest > 0) forestResourceDiv.classList.add('warning');
        if (forest <= forestCollapseThreshold && forest > 0) forestResourceDiv.classList.add('critical');
        if (forest <= 0) forestResourceDiv.style.backgroundColor = '#424242'; // Dark grey when depleted

        fishResourceDiv.classList.remove('warning', 'critical');
        if (fish < fishCollapseThreshold * 2 && fish > 0) fishResourceDiv.classList.add('warning');
        if (fish <= fishCollapseThreshold && fish > 0) fishResourceDiv.classList.add('critical');
        if (fish <= 0) fishResourceDiv.style.backgroundColor = '#424242';

        wildlifeResourceDiv.classList.remove('warning', 'critical');
        if (wildlife < wildlifeCollapseThreshold * 2 && wildlife > 0) wildlifeResourceDiv.classList.add('warning');
        if (wildlife <= wildlifeCollapseThreshold && wildlife > 0) wildlifeResourceDiv.classList.add('critical');
         if (wildlife <= 0) wildlifeResourceDiv.style.backgroundColor = '#424242';


        // Update regeneration status messages (calculate regen for *next* year based on *current* levels)
         let currentForestRegen = calculateRegeneration(forest, initialForest, baseForestRegenRate, forestCollapseThreshold);
         let currentFishRegen = calculateRegeneration(fish, initialFish, baseFishRegenRate, fishCollapseThreshold);
         // Wildlife regeneration depends on forest level
         let currentWildlifeRegen = calculateRegeneration(wildlife, initialWildlife, baseWildlifeRegenRate, wildlifeCollapseThreshold, wildlifeForestDependency, forest);


        forestRegenP.textContent = currentForestRegen.toFixed(1);
        fishRegenP.textContent = currentFishRegen.toFixed(1);
        wildlifeRegenP.textContent = currentWildlifeRegen.toFixed(1);


        // Update general status message
        let statusText = "המערכת האקולוגית באי יציבה. כל המשאבים מתחדשים היטב.";
        if (forest < forestCollapseThreshold || fish < fishCollapseThreshold || wildlife < wildlifeCollapseThreshold) {
            statusText = "שימו לב! מלאי של משאב אחד או יותר נמוך. כושר ההתחדשות הטבעי עלול להיפגע!";
        }
         if (forest <= 0 || fish <= 0 || wildlife <= 0) {
              statusText = "קריסה אקולוגית מתחילה! משאב אחד או יותר דולל עד קצה גבול היכולת.";
         }
         if (forest <= 0 && fish <= 0 && wildlife <= 0) {
             statusText = "האי קרס לחלוטין. כל המשאבים הטבעיים דוללו.";
         }


        gameStatusP.textContent = statusText;

        // Update slider max values and displayed values
        cutTreesInput.max = forest.toFixed(0);
        cutTreesValueSpan.textContent = cutTreesInput.value;
        catchFishInput.max = fish.toFixed(0);
        catchFishValueSpan.textContent = catchFishInput.value;
        huntWildlifeInput.max = wildlife.toFixed(0);
        huntWildlifeValueSpan.textContent = huntWildlifeInput.value;

    }

    function nextYear() {
        // Get user input (ensure non-negative and not exceeding available)
        const treesCut = Math.max(0, Math.min(parseInt(cutTreesInput.value) || 0, forest));
        const fishCaught = Math.max(0, Math.min(parseInt(catchFishInput.value) || 0, fish));
        const wildlifeHunted = Math.max(0, Math.min(parseInt(huntWildlifeInput.value) || 0, wildlife));

        // Apply extraction
        forest -= treesCut;
        fish -= fishCaught;
        wildlife -= wildlifeHunted;

         // Ensure resources don't go below zero before regeneration
         forest = Math.max(0, forest);
         fish = Math.max(0, fish);
         wildlife = Math.max(0, wildlife);


        // Calculate and apply regeneration *based on levels at the start of the year before extraction*
        // Or based on levels *after* extraction but before next year's growth? Let's use after extraction, as this is the "stock" that will regrow.
         let forestRegen = calculateRegeneration(forest, initialForest, baseForestRegenRate, forestCollapseThreshold);
         let fishRegen = calculateRegeneration(fish, initialFish, baseFishRegenRate, fishCollapseThreshold);
         // Wildlife regeneration depends on current forest level
         let wildlifeRegen = calculateRegeneration(wildlife, initialWildlife, baseWildlifeRegenRate, wildlifeCollapseThreshold, wildlifeForestDependency, forest);


        forest += forestRegen;
        fish += fishRegen;
        wildlife += wildlifeRegen;

        // Prevent resources from exceeding initial capacity (simple cap)
        forest = Math.min(forest, initialForest);
        fish = Math.min(fish, initialFish);
        wildlife = Math.min(wildlife, initialWildlife);

         year++; // Increment year *after* calculations

        // Check for collapse or win
        if (forest <= 0 || fish <= 0 || wildlife <= 0) {
            endGame(false); // Collapse
        } else if (year > maxYears) {
            endGame(true); // Survived
        } else {
            updateDisplay();
             // Reset input values or keep them? Keeping them makes it easier for steady state management
             // cutTreesInput.value = 0;
             // catchFishInput.value = 0;
             // huntWildlifeInput.value = 0; // Keep values
        }
    }

    function endGame(success) {
        nextYearButton.disabled = true; // Disable button to prevent further clicks
        let message = "";
        if (success) {
            message = "ברכות! הצלחת לנהל את משאבי האי 'איזון' באופן בר קיימא ולהגיע לשנת " + maxYears + "! ניהול מושכל והסתגלות השתלמו!";
             // Add confetti or win animation? (Beyond basic JS/CSS/HTML capabilities here)
        } else {
            message = "האי 'איזון' קרס עקב ניצול יתר של משאבים. לא ניתן לשמור על האי במצבו הנוכחי.";
             if (forest <= 0) message += "<br>- היער נעלם כמעט לחלוטין.";
             if (fish <= 0) message += "<br>- אוכלוסיית הדגים בים קרסה.";
             if (wildlife <= 0) message += "<br>- חיות הבר נכחדו.";
        }
        finalMessageP.innerHTML = message; // Use innerHTML to allow line breaks
        finalYearSpan.textContent = year -1; // Show the year *before* the game ended/won
        gameOverScreen.style.display = 'flex'; // Show the screen
    }

    function restartGame() {
        year = 1;
        forest = initialForest;
        fish = initialFish;
        wildlife = initialWildlife;

        nextYearButton.disabled = false; // Re-enable button
        gameOverScreen.style.display = 'none'; // Hide screen

        // Reset input values and update display
        cutTreesInput.value = 0;
        catchFishInput.value = 0;
        huntWildlifeInput.value = 0;

         // Reset resource div colors
        forestResourceDiv.classList.remove('warning', 'critical');
        fishResourceDiv.classList.remove('warning', 'critical');
        wildlifeResourceDiv.classList.remove('warning', 'critical');
         forestResourceDiv.style.backgroundColor = null; // Reset inline style
         fishResourceDiv.style.backgroundColor = null;
         wildlifeResourceDiv.style.backgroundColor = null;


        updateDisplay(); // Initialize game display
    }

    function toggleExplanation() {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מעמיק';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג הסבר מעמיק';
        }
    }

    // --- Event Listeners ---
    nextYearButton.addEventListener('click', nextYear);
    restartGameButton.addEventListener('click', restartGame);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Add listeners to update slider value display in real-time
     cutTreesInput.addEventListener('input', () => {
         cutTreesValueSpan.textContent = cutTreesInput.value;
     });
     catchFishInput.addEventListener('input', () => {
         catchFishValueSpan.textContent = catchFishInput.value;
     });
     huntWildlifeInput.addEventListener('input', () => {
         huntWildlifeValueSpan.textContent = huntWildlifeInput.value;
     });


    // --- Initialize the game ---
    updateDisplay(); // Initial render

</script>