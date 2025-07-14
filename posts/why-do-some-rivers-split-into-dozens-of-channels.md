---
title: "מדוע נהרות מסוימים מתפצלים לעשרות ערוצים?"
english_slug: why-do-some-rivers-split-into-dozens-of-channels
category: "מדעי כדור הארץ"
tags:
  - גיאומורפולוגיה
  - נהרות
  - זרימת מים
  - משקעים
  - עיצוב נוף
---
# מדוע נהרות מסוימים מתפצלים לעשרות ערוצים?

האם אי פעם ראיתם תמונה של נהר שנראה כאילו הוא שזור כמו צמה ענקית, מתפצל לעשרות ערוצים זורמים ומתאחד שוב ושוב? זוהי תופעה גיאולוגית מרהיבה הנקראת "נהר קלוע" (Braided River). מה גורם למים לפלס את דרכם בצורה כל כך מורכבת, במקום לזרום בערוץ יחיד וברור?

התשובה נמצאת במשחק דינמי ומרתק בין כוחם של המים לכמות וסוג החומר שהם סוחפים. בואו נצלול לסימולציה אינטראקטיבית שתאפשר לכם לחקור בעצמכם את הגורמים המשפיעים על התפתחות נהר קלוע!

<div class="simulation-container">
    <div class="simulation-header">
        <h2>מעבדת הנהר הקלוע האינטראקטיבית</h2>
        <p>שנו את הפרמטרים ובחנו בזמן אמת כיצד הם מעצבים את אפיק הנהר!</p>
    </div>
    <div class="controls">
        <div class="control-group">
            <label for="flow-rate" title="כמות המים הנכנסת למערכת בכל צעד זמן. זרימה גבוהה יותר מעבירה יותר סחף ויכולה לפתח ערוצים רחבים יותר.">עוצמת זרימה:</label>
            <input type="range" id="flow-rate" min="1" max="15" value="7" step="1">
            <span id="flow-rate-value" class="param-value">7</span>
        </div>
        <div class="control-group">
            <label for="sediment-load" title="כמות הסחף (חול, חצץ וכו') שהמים יכולים לשאת. עומס סחף גבוה מגדיל את כמות החומר הזמין לבניית איים בתוך האפיק.">עומס סחף מקסימלי:</label>
            <input type="range" id="sediment-load" min="1" max="15" value="7" step="1">
            <span id="sediment-load-value" class="param-value">7</span>
        </div>
        <div class="control-group">
            <label for="slope" title="משפיע על מהירות המים וכוח השחיקה/שיקוע. שיפוע גדול יותר = זרימה מהירה יותר = שחיקה חזקה יותר. שיפוע קטן יותר = זרימה איטית יותר = שיקוע קל יותר.">כוח שחיקה/שיקוע:</label>
            <input type="range" id="slope" min="1" max="15" value="7" step="1">
            <span id="slope-value" class="param-value">7</span>
        </div>
        <div class="button-group">
            <button id="start-stop-btn" class="action-button">התחילו את הזרימה!</button>
            <button id="reset-btn" class="action-button secondary">אפסו את הנהר</button>
        </div>
    </div>
    <canvas id="river-canvas"></canvas>
</div>

<style>
    :root {
        --primary-color: #4A90E2; /* A nice blue */
        --primary-color-dark: #357ABD;
        --secondary-color: #50E3C2; /* A calming green-blue */
        --background-color: #ECF0F1; /* Light grey/blue background */
        --container-background: #FFFFFF; /* White for the simulation box */
        --control-background: #F8F9FA; /* Off-white for controls */
        --border-color: #DDDDDD;
        --text-color: #333333;
        --canvas-land-base: #A0A0A0; /* Base land grey */
        --canvas-bar-color: #C19A6B; /* Sandy/brownish bar color */
        --canvas-water-shallow: #AEEEEE; /* Light blue for shallow water */
        --canvas-water-deep: #0077BE; /* Darker blue for deep water */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure RTL layout */
        text-align: right;
    }

    h1, h2, h3 {
        color: var(--primary-color-dark);
    }

    .simulation-container {
        margin: 30px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--container-background);
        max-width: 900px; /* Limit container width */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        text-align: center; /* Center the canvas and controls block */
    }

    .simulation-header h2 {
        margin-top: 0;
        color: var(--primary-color);
    }

    .simulation-header p {
        font-size: 1.1em;
        color: #555;
        margin-bottom: 25px;
    }

    .controls {
        margin-bottom: 30px;
        padding: 20px;
        background-color: var(--control-background);
        border-radius: 8px;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid */
        gap: 20px;
        text-align: right; /* Align controls text right */
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align label and slider to the start */
    }

    .controls label {
        display: block; /* Make label take its own line */
        width: auto; /* Override fixed width */
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
        text-align: right; /* Ensure text alignment */
        cursor: help; /* Indicate tooltip */
    }

    .controls input[type="range"] {
        width: 100%; /* Make sliders fill their container */
        vertical-align: middle;
        -webkit-appearance: none; /* Override default styles */
        appearance: none;
        height: 8px;
        background: var(--border-color);
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .param-value {
        display: block; /* Value below the slider */
        text-align: center;
        margin-top: 5px;
        font-weight: bold;
        color: var(--primary-color-dark);
    }

    .button-group {
        grid-column: 1 / -1; /* Span across all columns */
        text-align: center; /* Center buttons */
        margin-top: 15px;
    }

    .action-button {
        padding: 12px 25px;
        margin: 0 10px;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--primary-color);
        color: white;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .action-button:hover {
        background-color: var(--primary-color-dark);
        transform: translateY(-2px);
    }

     .action-button.secondary {
        background-color: #6c757d; /* Muted grey */
     }
     .action-button.secondary:hover {
         background-color: #5a6268;
     }


    canvas {
        border: 1px solid #888; /* Softer border */
        background-color: var(--canvas-land-base); /* Represents base sediment/land */
        display: block; /* Removes extra space below canvas */
        margin: 20px auto 0; /* Center the canvas below controls */
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow for depth */
    }

    #explanation-toggle {
        display: block;
        width: fit-content;
        margin: 30px auto 20px;
        padding: 12px 25px;
        cursor: pointer;
        border: 1px solid var(--secondary-color);
        border-radius: 6px;
        background-color: #E0F7FA; /* Very light secondary color */
        color: var(--secondary-color);
        font-size: 1.1em;
        text-align: center;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #explanation-toggle:hover {
        background-color: #B2EBF2; /* Lighter secondary color */
        transform: translateY(-2px);
    }

    #explanation-content {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--container-background);
        display: none; /* Initially hidden */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }

    #explanation-content h2,
    #explanation-content h3 {
        color: var(--primary-color-dark);
        margin-top: 1em;
        margin-bottom: 0.6em;
        border-bottom: 1px solid #eee; /* Subtle separator */
        padding-bottom: 5px;
    }

    #explanation-content p,
    #explanation-content ul,
    #explanation-content ol {
        margin-bottom: 1em;
        color: #444;
    }

    #explanation-content ul,
    #explanation-content ol {
        padding-right: 20px; /* Indent lists */
    }

    #explanation-content li {
        margin-bottom: 0.5em;
    }

    /* Tooltip styles */
    [title]:hover::after {
        content: attr(title);
        position: absolute;
        top: calc(100% + 5px); /* Position below the element */
        right: 0; /* Align to the right */
        background-color: #333;
        color: white;
        padding: 8px;
        border-radius: 4px;
        font-size: 0.9em;
        white-space: nowrap; /* Prevent wrapping */
        z-index: 10;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        direction: rtl;
        text-align: right;
    }
    [title] {
        position: relative; /* Needed for absolute positioning of ::after */
    }
    /* Adjust tooltip position for labels to avoid covering them */
    .controls label[title]:hover::after {
         right: auto; /* Reset right alignment */
         left: 0; /* Align to the left side of the label */
         transform: translateX(-100%); /* Shift left by its own width */
    }


</style>

<button id="explanation-toggle">הצגת הסיפור המלא: מדוע נהרות מתקלעים?</button>

<div id="explanation-content">
    דמיינו נהר רחב, אך במקום ערוץ יחיד וברור, הוא מתפצל לאינספור זרמים קטנים, כמו צמה ענקית שדינמית משנה את צורתה. מה גורם לתופעה הגיאומורפולוגית המרהיבה הזו להתרחש בנהרות מסוימים ולא באחרים? התשובה טמונה במשחק מורכב ומרתק של מים, סחף (אדמה, חצץ, חול) וזמן, המתרחש לנגד עינינו בקנה מידה גיאולוגי.

    <h2>הסבר מורחב: לידתם וחייהם של נהרות קלועים</h2>

    <h3>אנטומיה של נהר קלוע</h3>
    נהר קלוע (Braided River) אינו סתם נהר עם כמה איים. הוא מאופיין ברשת צפופה ומסועפת של ערוצי מים קטנים, המתפצלים ומתאחדים שוב ושוב מסביב לגופי סחף שנבנים בתוך האפיק עצמו. גופי סחף אלו, הנקראים 'איים' או 'סוללות סחף' (bars), לרוב מורכבים מחצץ או חול גס. המראה הכולל, כפי שהשם מרמז, דומה למראה צמה. חשוב להבין: צורתם של הערוצים והאיים אינה קבועה לרגע. היא משתנה כל העת, לפעמים בצורה דרמטית במהלך שיטפון בודד, בתגובה לשינויים בכמות ומהירות הזרימה ובתנועת הסחף.

    <h3>התנאים ההכרחיים למתכון הנהר הקלוע</h3>
    נהרות קלועים אינם נפוצים בכל נוף. הם דורשים שילוב ספציפי של תנאים כדי להיווצר ולהתקיים:
    <ul>
        <li><strong>עומס סחף *גבוה* במיוחד:</strong> זהו אולי הגורם המשמעותי ביותר. הנהר חייב לשאת כמות עצומה של חומר מוצק – חצץ, חול, ולעיתים גם טין – שנגרף מהאזורים העליונים של אגן הניקוז (למשל, מהרי קרחונים או אזורי שחיקה אינטנסיבית). חומר זה הוא חומר הגלם לבניית איי הסחף.</li>
        <li><strong>שיפוע *מתון* יחסית אך מספיק לשאת סחף גס:</strong> נדרש שיפוע המאפשר למים לנוע במהירות מספקת כדי לשאת סחף *גס* (בניגוד לנהרות מפותלים הנושאים בעיקר סחף עדין בשיפועים מישוריים כמעט), אך *לא* תלול מדי. בשיפוע מתון, שינויים קטנים במהירות הזרימה גורמים בקלות לשיקוע של סחף גס, בניית איים והתפצלות הזרם סביבם. נהרות בשיפוע תלול מדי פשוט סוחפים הכל ונוטים לחפור ערוץ יחיד עמוק.</li>
        <li><strong>גדות אפיק *לא יציבות וקלות לשחיקה*:</strong> כדי שהנהר יוכל לשנות את אפיקו בקלות יחסית, לשטוף סביב איים חדשים ולהרחיב את רשת הערוצים, חומר הגדות חייב להיות קל לשחיקה (חצץ, חול, או אדמה לא מגובשת) ולא סלע קשה או גדות מיוצבות על ידי צמחייה עבותה.</li>
        <li><strong>זרימת מים *משתנה באופן משמעותי*:</strong> נהרות בהם יש שינויים גדולים בקצב הזרימה בין עונות השנה או בין אירועים (למשל, נהרות המוזנים מהפשרת שלגים עונתית, או באזורים עם עונתיות גשמים בולטת) נוטים יותר להתקלעות. בזרימה גבוהה (שיטפון), המים סוחפים כמויות אדירות של סחף מהאפיק והגדות. כשהזרימה נחלשת, הנהר "מאבד כוח", ושיקוע מואץ של הסחף הכבד מתרחש בתוך האפיק, מה שבונה במהירות את איי הסחף המפצלים את הזרם.</li>
    </ul>

    <h3>מסעו של הסחף: תהליך ההיווצרות הדינמי</h3>
    תהליך יצירת ושינוי הנהר הקלוע הוא מעגל אינסופי של שחיקה (Erosion) ושיקוע (Deposition):
    <ol>
        <li><strong>התחלה:</strong> נהר מהיר יחסית הנושא עומס סחף גבוה זורם במורד שיפוע מתון.</li>
        <li><strong>שיקוע ראשוני:</strong> בנקודות בהן מהירות הזרימה יורדת מעט (אפילו בגלל הפרעה קטנה באפיק או שינוי זעיר בשיפוע), המים מאבדים חלק מכושר הנשיאה שלהם. החומר הכבד יותר – החצץ והחול הגס – מתחיל לשקוע ולהצטבר בקרקעית האפיק.</li>
        <li><strong>לידת האיים:</strong> הצטברויות הסחף הללו גדלות בהדרגה ויוצרות גופי סחף תת-מימיים או בולטים מעל פני המים בזרימה נמוכה – אלו הם ה'איים' הראשוניים (bars).</li>
        <li><strong>פיצול הזרם:</strong> האיים החלקיים חוסמים חלק מהזרם הראשי. המים נאלצים לעקוף אותם, ובכך מחלקים את הזרם הראשי לערוצים קטנים ומסועפים העוברים משני צידי האיים או ביניהם.</li>
        <li><strong>שחיקת גדות ובניית איים נוספים:</strong> כשהמים מתפצלים וזורמים במהירות סביב האיים, הם שוחקים את גדות האפיק הלא יציבות וסוחפים חומר נוסף. החומר הנסחף נישא הלאה ומשתקע במקומות אחרים בהם המהירות שוב יורדת, מה שמוביל ליצירת איים חדשים או הגדלת איים קיימים.</li>
        <li><strong>מעגל השינוי הנצחי:</strong> התהליך ממשיך ללא הרף. איים חדשים נוצרים, איים קיימים נשחקים או נשטפים בזרימות גבוהות, ערוצים מתפצלים, מתאחדים מחדש, ננטשים כשהאיים גדלים וחוסמים אותם, ונוצרים מחדש במקומות אחרים. הנהר הקלוע הוא מערכת דינמית במיוחד, הנמצאת בשינוי מתמיד.</li>
    </ol>

    <h3>שלושת המופעים של נהרות (בפשטות גסה)</h3>
    בעוד שבמציאות יש מגוון רחב של צורות נהרות, ניתן לפשט לשלושה סוגים עיקריים מבחינת צורת האפיק:
    <ul>
        <li><strong>נהרות ישרים:</strong> נדירים למדי בטבע לאורך קטעים ארוכים, אלא אם הם נחפרים בכוח רב דרך סלע קשה או נובעים בשיפועים תלולים *מאוד* (כמו מפלי מים או קניונים צרים).</li>
        <li><strong>נהרות מפותלים (Meandering rivers):</strong> מאופיינים בערוץ יחיד שמתפתל בצורה של "נחשים". נוצרים בדרך כלל באזורים מישוריים עם שיפוע *מתון מאוד*, גדות יציבות יחסית, ועומס סחף *עדין* יותר (טין וחרסית). התהליך העיקרי הוא שחיקה מתמשכת בצד החיצוני (הקמור) של העיקול ושיקוע בצד הפנימי (הקעור), מה שגורם לעיקול לנדוד ולהתפתח עם הזמן.</li>
        <li><strong>נהרות קלועים (Braided rivers):</strong> כפי שתואר, מאופיינים בריבוי ערוצים מסועפים ושזורים סביב איים זמניים/קבועים למחצה. נוצרים באזורים עם שיפוע מתון אך לא מישורי לגמרי, עומס סחף *גבוה* (בדרך כלל גס יותר), גדות *לא יציבות*, וזרימה *משתנה*.</li>
    </ul>

    <h3>היכן נפגוש נהרות קלועים?</h3>
    נהרות קלועים נפוצים במיוחד באזורים שבהם יש אספקה מאסיבית של סחף גס ויבשתי, ושינויים גדולים בזרימה. דוגמאות קלאסיות הן:
    <ul>
        <li><strong>נהרות קרחוניים:</strong> במורדות קרחונים או מיד לאחר אזורים מכוסים קרחונים, שם הקרחון גורס סלעים ויוצר כמויות עצומות של סחף גס, והזרימה משתנה עונתית עם הפשרת השלגים והקרחונים.</li>
        <li><strong>מורדות הרי געש:</strong> חומר געשי (אפר, טוף, סלעים) יכול לספק כמויות גדולות של סחף בקלות.</li>
        <li><strong>אזורים בעלי בליה מהירה:</strong> באזורים יבשים למחצה או הרריים בהם יש שחיקה מהירה של פני הקרקע ואירועי גשם עזים אך קצרים.</li>
    </ul>
    דוגמאות מפורסמות ניתן למצוא בנהרות רבים באלסקה, איסלנד, ניו זילנד, הרי ההימלאיה והאלפים.

    כעת, חזרו לסימולציה ושחקו עם הפרמטרים. נסו לראות כיצד שינוי קטן בעומס הסחף או בעוצמת הזרימה משנה באופן דרמטי את צורת הנהר המתפתחת לנגד עיניכם. התנסו, התבוננו ולמדו מה הכוחות הגיאולוגיים החזקים הללו מסוגלים לחולל!
</div>

<script>
    const canvas = document.getElementById('river-canvas');
    const ctx = canvas.getContext('2d');
    const flowRateSlider = document.getElementById('flow-rate');
    const sedimentLoadSlider = document.getElementById('sediment-load');
    const slopeSlider = document.getElementById('slope');
    const flowRateValue = document.getElementById('flow-rate-value');
    const sedimentLoadValue = document.getElementById('sediment-load-value');
    const slopeValue = document.getElementById('slope-value');
    const startStopBtn = document.getElementById('start-stop-btn');
    const resetBtn = document.getElementById('reset-btn');
    const explanationToggle = document.getElementById('explanation-toggle');
    const explanationContent = document.getElementById('explanation-content');

    // Simulation parameters
    let GRID_WIDTH = 250; // Increased width for better visualization
    let GRID_HEIGHT = 120; // Increased height
    const CELL_SIZE = 3; // Pixels per cell
    canvas.width = GRID_WIDTH * CELL_SIZE;
    canvas.height = GRID_HEIGHT * CELL_SIZE;

    let grid = []; // 2D array for sediment height
    let waterFlow = []; // 2D array for water amount/flow in each cell
    let isRunning = false;
    let animationFrameId = null;
    let simulationSpeed = 50; // Milliseconds per simulation step (adjust for faster/slower)
    let lastTimestamp = 0;

    // Simulation constants (adjusted by sliders)
    let baseFlowRate = 7; // Amount of water entering per step (influenced by slider)
    let maxSedimentCapacity = 7; // Max sediment water can carry per unit (influenced by slider)
    let erosionDepositionSensitivity = 7; // Influences erosion/deposition rate (influenced by slider)

    // Fixed simulation parameters
    const MAX_SEDIMENT_HEIGHT = 100;
    const INITIAL_SEDIMENT_HEIGHT = 40; // Base land height, slightly lower to encourage early channel formation
    const EROSION_RATE_FACTOR = 0.05; // How efficiently sediment is eroded
    const DEPOSITION_RATE_FACTOR = 0.08; // How efficiently sediment is deposited
    const MAX_WATER = 10; // Max water level in a cell before overflowing (conceptually)
    const WATER_DISSIPATION = 0.95; // Factor for water dissipation in stagnant cells

    // Initialize the grid
    function initGrid() {
        grid = [];
        waterFlow = [];
        for (let y = 0; y < GRID_HEIGHT; y++) {
            grid[y] = [];
            waterFlow[y] = [];
            for (let x = 0; x < GRID_WIDTH; x++) {
                // Create a base slope with some random variation
                let initialHeight = INITIAL_SEDIMENT_HEIGHT - (y / GRID_HEIGHT) * INITIAL_SEDIMENT_HEIGHT * 0.5; // Gentle slope down
                initialHeight += (Math.random() - 0.5) * 8; // Add some initial noise for variation
                grid[y][x] = Math.max(5, Math.min(MAX_SEDIMENT_HEIGHT - 5, initialHeight)); // Clamp height within a reasonable range
                waterFlow[y][x] = 0;
            }
        }
        // Create a more defined starting channel area
        const channelWidth = Math.floor(GRID_WIDTH * 0.05); // Starting channel is 5% of width
        const channelStartX = Math.floor(GRID_WIDTH / 2 - channelWidth / 2);
         for (let y = 0; y < Math.min(20, GRID_HEIGHT); y++) { // Start channel affects top 20 rows
            for (let x = channelStartX; x < channelStartX + channelWidth; x++) {
                 if (x >= 0 && x < GRID_WIDTH) {
                    grid[y][x] = Math.max(5, grid[y][x] * 0.8); // Make the channel floor slightly lower
                 }
            }
        }
    }

    // Update simulation parameters from sliders
    function updateParameters() {
        baseFlowRate = parseInt(flowRateSlider.value);
        maxSedimentCapacity = parseInt(sedimentLoadSlider.value);
        erosionDepositionSensitivity = parseInt(slopeSlider.value);

        flowRateValue.textContent = flowRateSlider.value;
        sedimentLoadValue.textContent = sedimentLoadSlider.value;
        slopeValue.textContent = slopeSlider.value;
    }

    // Draw the grid
    function drawGrid() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        for (let y = 0; y < GRID_HEIGHT; y++) {
            for (let x = 0; x < GRID_WIDTH; x++) {
                const height = grid[y][x];
                const water = waterFlow[y][x];

                let color;
                if (water > 0.1) { // If there's significant water (threshold adjusted)
                     // Color based on water level (deeper blue for more water)
                     // Use HSL for smoother transitions
                     const waterDepthRatio = Math.min(1, water / MAX_WATER);
                     // Hue: 200-220 (blues), Saturation: 80-100%, Lightness: 40-80% (deeper=darker, shallower=lighter)
                     const hue = 210;
                     const saturation = 90;
                     const lightness = 80 - (waterDepthRatio * 40); // 80% for shallow, 40% for deep
                     color = `hsl(${hue}, ${saturation}%, ${lightness}%)`;

                } else { // If it's land/sediment
                     // Color based on sediment height (lighter/browner for higher sediment/bars, greyer/greener for lower land/banks)
                     const landHeightRatio = height / MAX_SEDIMENT_HEIGHT;
                     // Hue: 30-60 (browns/yellows) for high, 80-120 (greens/greys) for low
                     // Saturation: 20-60%
                     // Lightness: 40-70%
                     const landHue = 90 - (landHeightRatio * 60); // From green-grey (90) towards brown (30)
                     const landSaturation = 20 + (landHeightRatio * 40); // More saturated for higher/browner
                     const landLightness = 40 + (landHeightRatio * 30); // Lighter for higher
                     color = `hsl(${landHue}, ${landSaturation}%, ${landLightness}%)`;
                }

                ctx.fillStyle = color;
                ctx.fillRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
            }
        }
    }

    // Simulation step
    function simulateStep() {
        let nextWaterFlow = new Array(GRID_HEIGHT).fill(0).map(() => new Array(GRID_WIDTH).fill(0));
        let sedimentTransport = new Array(GRID_HEIGHT).fill(0).map(() => new Array(GRID_WIDTH).fill(0)); // Net change in sediment height

        // Introduce water at the top center
        const waterEntryWidth = Math.max(5, Math.min(GRID_WIDTH, Math.floor(baseFlowRate * 1.5))); // Entry width based on flow rate
        const entryStartX = Math.floor(GRID_WIDTH / 2 - waterEntryWidth / 2);
        for (let x = entryStartX; x < entryStartX + waterEntryWidth; x++) {
             if (x >= 0 && x < GRID_WIDTH) {
                 // Distribute incoming water based on baseFlowRate
                waterFlow[0][x] = baseFlowRate / waterEntryWidth;
             }
        }


        // Process flow and sediment transport
        // Use a temporary buffer for water movement to avoid processing water multiple times per step
        let waterOutflow = new Array(GRID_HEIGHT).fill(0).map(() => new Array(GRID_WIDTH).fill(0));

        for (let y = 0; y < GRID_HEIGHT; y++) {
            for (let x = 0; x < GRID_WIDTH; x++) {
                let currentWater = waterFlow[y][x];
                if (currentWater < 0.01) { // Skip if no significant water
                    // Water dissipation for shallow or stagnant water
                    if (currentWater > 0) {
                         waterFlow[y][x] *= WATER_DISSIPATION;
                    }
                    continue;
                }

                let currentHeight = grid[y][x];
                let currentLevel = currentHeight + currentWater; // Total surface level
                let neighbors = [];
                let totalFlowPotential = 0; // Sum of positive height differences to neighbors

                // Consider neighbors (including diagonals)
                const dx = [-1, 0, 1, -1, 1, -1, 0, 1];
                const dy = [-1, -1, -1, 0, 0, 1, 1, 1];

                for (let i = 0; i < dx.length; i++) {
                    const nx = x + dx[i];
                    const ny = y + dy[i];

                    if (nx >= 0 && nx < GRID_WIDTH && ny >= 0 && ny < GRID_HEIGHT) {
                        const neighborLevel = grid[ny][nx] + waterFlow[ny][nx];
                        const heightDifference = currentLevel - neighborLevel;
                        if (heightDifference > 0) {
                            neighbors.push({ nx, ny, heightDifference });
                            totalFlowPotential += heightDifference;
                        }
                    }
                }

                // Distribute water and calculate sediment change
                let waterToDistribute = currentWater; // Water available to move from this cell
                let sedimentCarried = Math.min(currentWater * (maxSedimentCapacity / 10), currentWater * 5); // How much sediment this water *can* carry

                if (totalFlowPotential > 0) {
                     // The amount of water flowing out of the cell is proportional to the total height difference.
                     // A simple approach: send a fraction of water proportional to height difference
                    let flowAmountTotal = Math.min(currentWater, totalFlowPotential * 0.5); // Don't move *all* water, max flow based on potential

                    neighbors.forEach(neighbor => {
                        const flowFraction = neighbor.heightDifference / totalFlowPotential;
                        const flowAmount = flowAmountTotal * flowFraction; // Amount of water flowing to this neighbor

                        // Water movement update - add to neighbor's incoming buffer
                        nextWaterFlow[neighbor.ny][neighbor.nx] += flowAmount;
                        waterOutflow[y][x] += flowAmount; // Track water leaving this cell

                        // Sediment transport logic: Erosion/Deposition depends on flow speed and sediment load relative to capacity
                        // Simplified speed proxy: heightDifference to neighbor
                        const speedProxy = neighbor.heightDifference; // Higher diff = faster flow towards neighbor

                        // How much sediment is currently in the cell *relative* to the water
                        const currentSedimentInCell = grid[y][x] - INITIAL_SEDIMENT_HEIGHT * 0.5; // Rough measure above base
                        const currentSedimentLoadRatio = currentSedimentInCell > 0.1 ? sedimentCarried / currentSedimentInCell : maxSedimentCapacity; // Avoid division by zero

                        // Erosion happens if the water can carry more sediment and is flowing fast
                        // Deposition happens if the water is overloaded or slows down (e.g., flows into a higher cell relative to its own level)

                        // Erosion from current cell to neighbor: occurs if flowing downhill & below capacity
                         let erosionAmount = 0;
                         if (speedProxy > 0.1 && sedimentCarried < maxSedimentCapacity * currentWater) { // Flowing downhill and capacity not full
                             // Erosion rate depends on speed proxy, sensitivity, and how empty the capacity is
                             erosionAmount = speedProxy * (erosionDepositionSensitivity / 15) * EROSION_RATE_FACTOR * (maxSedimentCapacity * currentWater - sedimentCarried) / (maxSedimentCapacity * currentWater + 1e-6);
                             erosionAmount = Math.min(erosionAmount, grid[y][x] - 5); // Don't erode below minimal height
                             sedimentTransport[y][x] -= erosionAmount; // Erosion from current cell
                         }


                        // Deposition to neighbor cell: occurs if flowing uphill (relative level) or overloaded
                         let depositionAmount = 0;
                         const neighborLevel = grid[neighbor.ny][nx] + waterFlow[neighbor.ny][nx];
                         if (currentLevel < neighborLevel) { // Flowing "uphill" relative to neighbor's surface level
                              // Deposition occurs because water slows down or pools
                              // Rate depends on height diff, sensitivity, and sediment already carried
                              depositionAmount = (neighborLevel - currentLevel) * (erosionDepositionSensitivity / 15) * DEPOSITION_RATE_FACTOR * sedimentCarried / (currentWater + 1e-6); // More sediment = more deposition
                              depositionAmount = Math.min(depositionAmount, MAX_SEDIMENT_HEIGHT - grid[neighbor.ny][nx] - 5); // Don't deposit above max height
                              sedimentTransport[neighbor.ny][nx] += depositionAmount; // Deposition at neighbor cell
                         } else if (sedimentCarried > maxSedimentCapacity * currentWater * 0.8) { // If heavily loaded, deposit a little regardless of slope
                             depositionAmount = sedimentCarried * DEPOSITION_RATE_FACTOR * 0.1;
                             depositionAmount = Math.min(depositionAmount, MAX_SEDIMENT_HEIGHT - grid[neighbor.ny][nx] - 5);
                              sedimentTransport[neighbor.ny][nx] += depositionAmount; // Deposition at neighbor cell
                         }


                        // Simple sediment redistribution: A portion of carried sediment moves with the water
                        // This is difficult with this simple model, the erosion/deposition logic above handles the net change.
                        // Let's rely primarily on the erosion/deposition based on speed/load.
                    });

                    // After calculating outflows, remove that water from the current cell for the next step calculation
                    waterFlow[y][x] -= waterOutflow[y][x];

                } else if (currentWater > 0) {
                    // No downhill flow potential - water is pooling or stagnant
                    // Slow dissipation already handled at the start of the loop
                    // If water is stagnant and carries sediment, some deposition occurs
                     if (sedimentCarried > maxSedimentCapacity * currentWater * 0.5) { // If carrying significant load while stagnant
                         const depositionAmount = sedimentCarried * DEPOSITION_RATE_FACTOR * 0.5;
                         sedimentTransport[y][x] += Math.min(depositionAmount, MAX_SEDIMENT_HEIGHT - grid[y][x] - 5);
                     }
                }
            }
        }

        // Apply water movement from nextWaterFlow (buffer)
        for (let y = 0; y < GRID_HEIGHT; y++) {
             for (let x = 0; x < GRID_WIDTH; x++) {
                 waterFlow[y][x] += nextWaterFlow[y][x];
                 // Clamp water level
                 waterFlow[y][x] = Math.max(0, Math.min(waterFlow[y][x], MAX_WATER));
             }
        }


        // Update sediment heights based on transport
        for (let y = 0; y < GRID_HEIGHT; y++) {
            for (let x = 0; x < GRID_WIDTH; x++) {
                grid[y][x] += sedimentTransport[y][x];
                // Clamp sediment height
                grid[y][x] = Math.max(5, Math.min(MAX_SEDIMENT_HEIGHT - 5, grid[y][x])); // Keep min/max limits slightly away from edges
            }
        }

        // Ensure water leaves the bottom edge
         for (let x = 0; x < GRID_WIDTH; x++) {
             waterFlow[GRID_HEIGHT - 1][x] = 0; // Water reaching bottom leaves
         }
    }

    // Animation loop
    function animate(timestamp) {
        if (!isRunning) {
             lastTimestamp = 0; // Reset timestamp when stopped
             return;
        }

        if (!lastTimestamp) lastTimestamp = timestamp;
        const elapsed = timestamp - lastTimestamp;

        // Run multiple simulation steps per frame if elapsed time is large
        // Or run a step only when enough time has passed for a smoother slower animation
        if (elapsed > simulationSpeed) {
             const stepsToRun = Math.floor(elapsed / simulationSpeed);
             for(let i = 0; i < stepsToRun; i++) {
                 simulateStep();
             }
             drawGrid();
             lastTimestamp = timestamp - (elapsed % simulationSpeed); // Adjust lastTimestamp to keep animation steady
        } else {
             // If not enough time has passed, just draw the current state (optional, can skip drawing)
             // drawGrid(); // Drawing every frame makes it smoother even if sim logic isn't updated
        }


        animationFrameId = requestAnimationFrame(animate);
    }

    // Start/Stop simulation
    startStopBtn.addEventListener('click', () => {
        isRunning = !isRunning;
        if (isRunning) {
            startStopBtn.textContent = 'השהיית הזרימה';
            startStopBtn.classList.remove('secondary');
            animate(0); // Start the animation loop
        } else {
            startStopBtn.textContent = 'המשך הזרימה';
            startStopBtn.classList.add('secondary');
            cancelAnimationFrame(animationFrameId);
            lastTimestamp = 0; // Reset timestamp
        }
    });

    // Reset simulation
    resetBtn.addEventListener('click', () => {
        isRunning = false;
        cancelAnimationFrame(animationFrameId);
        startStopBtn.textContent = 'התחילו את הזרימה!';
        startStopBtn.classList.remove('secondary'); // Reset button style
        lastTimestamp = 0; // Reset timestamp
        initGrid();
        updateParameters(); // Apply current slider values
        drawGrid();
    });

    // Slider event listeners
    flowRateSlider.addEventListener('input', updateParameters);
    sedimentLoadSlider.addEventListener('input', updateParameters);
    slopeSlider.addEventListener('input', updateParameters);

    // Explanation toggle
    explanationToggle.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        explanationToggle.textContent = isHidden ? 'הסתר את הסיפור המלא' : 'הצגת הסיפור המלא: מדוע נהרות מתקלעים?';
    });


    // Initial setup
    initGrid();
    updateParameters(); // Set initial values and display them
    drawGrid(); // Draw the initial state

    // Optional: Auto-start simulation on page load
    // isRunning = true;
    // startStopBtn.textContent = 'השהיית הזרימה';
    // animate(0);

</script>