---
title: "קרב ההישרדות של הנגיף: סימולטור עמידות לתרופות"
english_slug: virus-survival-battle-drug-resistance-simulator
category: "מדעי החיים / ביולוגיה"
tags:
- ביולוגיה
- נגיפים
- עמידות לתרופות
- אבולוציה
- אנטי-ויראליות
- סימולציה
---
# קרב ההישרדות של הנגיף: סימולטור עמידות לתרופות
תרופות אנטי-ויראליות הן מהכלים החזקים ביותר שלנו נגד מחלות נגיפיות, אך לעיתים קרובות הניצחון אינו מוחלט. נגיפים יכולים לפתח עמידות, ולהפוך את התרופה ליעילה פחות או לא יעילה כלל. איך ייתכן שהאויב שדוכא אתמול, פורח היום? צאו למסע מרתק לתוך עולם הנגיפים המשתנה והבינו בעצמכם את המכניזם המדהים (והמדאיג!) של התפתחות עמידות. הסימולטור האינטראקטיבי הזה הוא שדה הקרב שלכם.

<div class="simulator-container">
    <div class="visualization">
        <h2>אוכלוסיית הנגיפים בשדה הקרב</h2>
        <div id="virusCanvasContainer">
             <canvas id="virusCanvas"></canvas>
             <div class="round-counter">סבב: <span id="currentRoundDisplay">0</span> / <span id="totalRoundsDisplay">30</span></div>
             <div class="progress-bar-container">
                <div class="progress-bar" id="roundProgressBar"></div>
             </div>
        </div>

        <div class="legend">
            <span class="virus-dot sensitive-virus"></span> נגיף רגיש לתרופה (פגיע!)
            <span class="virus-dot resistant-virus"></span> נגיף עמיד לתרופה (שורד!)
        </div>
    </div>
    <div class="controls">
        <h2>הגדרות הקרב</h2>
        <div class="control-group">
            <label for="initialResistant">חיילים עמידים התחלתיים:</label>
            <input type="number" id="initialResistant" value="1" min="0" max="20" step="0.5">% (מומלץ 0-5%)
            <p class="control-hint">אחוז הנגיפים שכבר עמידים מהרגע הראשון.</p>
        </div>
        <div class="control-group">
            <label for="drugConcentration">עוצמת הטיפול התרופתי:</label>
            <select id="drugConcentration">
                <option value="high">גבוה (התקפה חזקה ויעילה)</option>
                <option value="low">נמוך (התקפה חלשה / הזנחת מינון)</option>
            </select>
             <p class="control-hint">השפעת התרופה על הנגיפים הרגישים.</p>
        </div>
        <div class="control-group">
            <label for="numRounds">משך הקרב (מספר סבבים):</label>
            <input type="number" id="numRounds" value="30" min="10" max="100" step="1">
             <p class="control-hint">כמה סבבי טיפול ושכפול יתקיימו.</p>
        </div>
        <div class="control-group">
             <label>קצב המוטציה:</label>
             <span class="mutation-rate-display">0.2%</span>
             <p class="control-hint">סיכוי של נגיף רגיש שעובר שכפול להפוך לעמיד.</p>
        </div>
        <button id="startSimulation">התחילו את הקרב!</button>
        <button id="resetSimulation">התחלה מחדש</button>
    </div>
    <div class="graph-container">
        <h2>שליטה בשדה הקרב: אחוז עמידות לאורך זמן</h2>
        <canvas id="resistanceGraph"></canvas>
    </div>
</div>

<button id="toggleExplanation" class="toggle-button">פענוח השדה: הצג/הסתר הסבר</button>

<div id="explanation" style="display: none;">
    <h2>פענוח שדה הקרב: מדוע נגיפים מפתחים עמידות?</h2>

    <h3>האויב: מי הם הנגיפים ואיך הם מתרבים?</h3>
    <p>דמיינו את הנגיפים כפיראטים זעירים. הם לא יכולים לייצר לעצמם אוניות, הם חייבים להשתלט על ספינות קיימות (תאי הגוף שלנו). כשהם פולשים לתא, הם משתלטים על מערכות הייצור שלו ומכריחים אותו לייצר רק עוד פיראטים כמוהם. התהליך מהיר ואלים, מרוקן את התא ממשאביו ובסופו של דבר לרוב מפוצץ אותו, משחרר אלפי "פיראטים" חדשים לים הדם, מוכנים להשתלט על התא הבא.</p>

    <h3>הנשק: תרופות אנטי-ויראליות בפעולה</h3>
    <p>התרופות שלנו הן כמו כלי נשק ממוקדים. הן לא יורות לכל עבר, אלא מחפשות נקודות תורפה ספציפיות במחזור החיים של הפיראטים בתוך התא. אולי הן חוסמות את כניסתם לספינה מלכתחילה, אולי הן משבשות את מנגנון השכפול שלהם (מונעות מהם "לשכפל את מפת האוצר"), או אולי הן מונעות מהם להתארגן ולצאת מהתא בספינות חדשות. המטרה היא לנטרל את הנגיף בלי לפגוע בתאי הגוף עצמם – המאבק הוא בטפיל, לא במארח.</p>

    <h3>השגיאות הקריטיות: מוטציות – מנוע השינוי</h3>
    <p>בכל פעם שהפיראטים הנגיפיים משכפלים את "מפת האוצר" הגנטית שלהם, האנזים המעתיק עושה טעויות קטנות. הוא מחליף אות אחת באחרת בקוד. רוב השגיאות האלה לא משמעותיות, חלקן אפילו מזיקות לפיראט עצמו, אבל מדי פעם, שגיאה אחת (מוטציה) משנה בדיוק את המבנה של חלבון מסוים – אולי את "מנעול הכניסה" של התא, אולי את "מכונת השכפול" שלהם. כשהנגיפים מתרבים בקצב מסחרר ובמספרים אסטרונומיים, גם מוטציות נדירות מאוד צפויות להתרחש.</p>

    <h3>השינוי שמקנה יתרון: מוטציות עמידות לתרופות</h3>
    <p>עכשיו, דמיינו שמוטציה אחת שינתה קלות את "מכונת השכפול" של נגיף מסוים, בדיוק במקום שהתרופה אמורה להיקשר אליו ולשתק אותו. כעת, התרופה כבר לא מתאימה "למפתח" הזה כמו קודם. היא לא מצליחה לשתק את המכונה ביעילות. הנגיף הזה, למרות הטיפול, מצליח לשכפל את עצמו בקצב גבוה יותר מאחיו הרגישים. הוא הפך ל"פיראט" עמיד בפני הנשק הספציפי הזה.</p>

    <h3>הברירה הטבעית בשדה הקרב: הטיפול ככלי סינון</h3>
    <p>כשאדם נוטל תרופה אנטי-ויראלית, הוא יוצר מצב שנקרא "לחץ סלקטיבי". זה כמו שדה קרב שבו נשק מסוים מופעל ללא הפסקה. כל ה"חיילים" הרגישים (הנגיפים הרגישים) נפגעים קשות ומתקשים לשרוד ולהתרבות. אבל אותם פיראטים נדירים שנושאים את המוטציה שהקנתה עמידות? הם כמעט ולא מושפעים! הם ממשיכים לשגשג, להתרבות ולתפוס את מקומם של הנגיפים הרגישים שנעלמים.</p>

    <h3>התהליך: צמיחת אוכלוסיית העמידים</h3>
    <p>סבב אחר סבב של טיפול ושכפול, אחוז הנגיפים הרגישים באוכלוסייה יורד דרמטית, בעוד שאחוז הנגיפים העמידים עולה בהתמדה. הסימולטור מדגים בדיוק את זה: הטיפול "מנקה" את הנגיפים הרגישים, אך מאפשר לעמידים להכפיל את עצמם יחסית בחופשיות, ועל ידי כך להשתלט בהדרגה על כלל אוכלוסיית הנגיפים בגוף. קצב המוטציה "מזרים" כל הזמן חיילים עמידים חדשים (גם אם מעטים) לשדה הקרב, ומאפשר לתהליך להתחיל גם אם לא היו עמידים בכלל בהתחלה.</p>

    <h3>ההשלכות: כישלון הטיפול והדרך למניעה</h3>
    <p>ברגע שרוב או כל הנגיפים בגוף המטופל הפכו עמידים, התרופה הופכת לחסרת תועלת. הנגיפים יכולים לשוב ולהתרבות ללא מעצור, והמחלה עלולה לחזור בעוצמה. זהו כישלון טיפולי שמצריך מעבר לתרופות אחרות.</p>
    <p>כדי למנוע מצב כזה, אנו נוקטים בטקטיקות מלחמה חכמות:
    <ul>
        <li>**טיפול משולב (קוקטייל):** תקיפה מכמה כיוונים! שימוש ב-2 תרופות או יותר בו-זמנית, כל אחת פועלת על מנגנון אחר של הנגיף. הסיכוי של נגיף בודד לפתח עמידות לשתי התרופות בבת אחת הוא זעיר ביותר.</li>
        <li>**הקפדה על מינון וזמנים:** עוצמה נכונה לאורך זמן! שמירה על ריכוז תרופה קבוע ויעיל בגוף חיונית לדיכוי מקסימלי של הנגיפים הרגישים. פספוס מנות או טיפול חלקי מאפשרים לנגיפים עמידים (אפילו המעטים) להתחיל להתרבות ולהשתלט ללא הפרעה משמעותית.</li>
        <li>**פיתוח נשק חדש:** מחקר ופיתוח תמידיים של תרופות חדשות נגד מטרות חדשות בנגיף.</li>
    </ul>
    הסימולטור ממחיש באופן דרמטי את החשיבות העצומה של הקפדה על הוראות הטיפול ואת הכוח העצום של טיפולים משולבים במלחמה המתמשכת נגד נגיפים מתפתחים.</p>
</div>

<style>
    /* Overall Body & RTL */
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Rubik', sans-serif; /* Using Rubik as a pleasant RTL-friendly font */
        line-height: 1.7; /* Slightly increased line height */
        color: #333;
        background-color: #f0f4f8; /* Light background */
        padding: 20px;
    }

    h1, h2, h3 {
        text-align: center;
        color: #2c3e50; /* Dark blue-gray heading color */
        margin-bottom: 0.8em;
    }

    h1 {
        font-size: 2.5em;
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }

    h2 {
         font-size: 1.8em;
         border-bottom: 2px solid #3498db; /* Underline headings */
         padding-bottom: 5px;
         margin-top: 1.5em;
         margin-bottom: 0.5em;
         display: inline-block; /* Underline only the text */
         text-align: center;
         width: 100%; /* Center the inline-block */
    }

    h3 {
        font-size: 1.4em;
        color: #3498db; /* Blue heading color */
        margin-top: 1.2em;
        margin-bottom: 0.5em;
    }

    p {
        margin-bottom: 1em;
    }

    ul {
        margin-top: 10px;
        padding-right: 25px; /* RTL list padding */
        padding-left: 0;
        list-style-type: disc; /* Default disc style */
    }

    li {
        margin-bottom: 0.8em;
    }


    /* Simulator Container */
    .simulator-container {
        display: flex;
        flex-wrap: wrap;
        gap: 25px; /* Increased gap */
        justify-content: center;
        margin: 30px auto; /* Centered with larger margins */
        padding: 30px; /* Increased padding */
        border: none; /* Remove border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* White background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Stronger shadow */
        max-width: 1200px; /* Max width for large screens */
    }

    .visualization, .controls, .graph-container {
        padding: 20px; /* Increased padding */
        border: none; /* Remove inner borders */
        border-radius: 8px; /* Rounded corners */
        background-color: #ecf0f1; /* Light gray background for sections */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05); /* Subtle inner shadow */
         flex-grow: 1; /* Allow sections to grow */
         min-width: 300px; /* Minimum width */
         display: flex; /* Use flexbox for internal layout */
         flex-direction: column;
    }

    .visualization {
         flex-basis: 400px; /* Preferred width for visualization */
         min-width: 350px;
         align-items: center; /* Center content */
    }

     .controls {
        flex-basis: 300px; /* Preferred width for controls */
         min-width: 280px;
        display: flex;
        flex-direction: column;
        gap: 18px; /* Increased gap */
    }

    .graph-container {
        flex-basis: 500px; /* Preferred width for graph */
        min-width: 350px;
        /* flex-grow: 1; */
        align-items: center; /* Center content */
    }


    /* Canvas Styling */
    #virusCanvasContainer {
        position: relative;
        width: 100%;
        height: 350px; /* Increased height */
        margin-bottom: 15px;
        border: 1px solid #bdc3c7; /* Soft border */
        border-radius: 8px;
        overflow: hidden; /* Hide potential overflow */
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Gradient background */
    }

    #virusCanvas {
        display: block; /* Remove extra space below canvas */
        width: 100%;
        height: 100%;
    }

    #resistanceGraph {
        display: block; /* Remove extra space below canvas */
        width: 100%;
        height: 350px; /* Consistent height */
        border: 1px solid #bdc3c7; /* Soft border */
        border-radius: 8px;
         background-color: #ffffff; /* White graph background */
    }


    /* Legend Styling */
    .legend {
        margin-top: 15px; /* Increased margin */
        font-size: 1em;
        text-align: center;
        padding-top: 10px;
        border-top: 1px dashed #bdc3c7; /* Separator */
        width: 100%; /* Take full width of parent */
    }

    .legend span.virus-dot {
        display: inline-block;
        width: 18px; /* Larger color dot */
        height: 18px; /* Larger color dot */
        margin: 0 8px; /* Spacing */
        vertical-align: middle;
        border-radius: 50%; /* Round dots */
        border: 1px solid rgba(0,0,0,0.2); /* Outline for clarity */
    }

    .sensitive-virus {
        background-color: #3498db; /* Distinct blue */
    }

    .resistant-virus {
        background-color: #e74c3c; /* Strong red */
    }


    /* Controls Styling */
    .controls .control-group {
        display: flex;
        flex-direction: column;
        gap: 8px; /* Slightly increased gap */
        padding-bottom: 15px;
        border-bottom: 1px dotted #bdc3c7; /* Separator */
    }
     .controls .control-group:last-child {
         border-bottom: none; /* No border for the last group */
         padding-bottom: 0;
     }


    .controls label {
        font-weight: bold;
        margin-bottom: 5px; /* Increased margin */
        color: #555;
        font-size: 1.1em;
    }

     .control-hint {
         font-size: 0.9em;
         color: #7f8c8d; /* Subtle gray text */
         margin-top: 5px;
         margin-bottom: 0;
     }


    .controls input[type="number"],
    .controls select {
        padding: 10px; /* Increased padding */
        border: 1px solid #bdc3c7; /* Soft border */
        border-radius: 5px; /* Slightly more rounded */
        font-size: 1.1em;
        width: 100%; /* Make inputs fill container */
        box-sizing: border-box; /* Include padding and border in element's total width */
    }

     .controls input[type="number"] {
         /* Specific styling for number input if needed */
         direction: ltr; /* Ensure numbers are displayed left-to-right */
         text-align: left;
     }
     .controls input[type="number"]::-webkit-outer-spin-button,
     .controls input[type="number"]::-webkit-inner-spin-button {
         -webkit-appearance: none;
         margin: 0;
     }
     .controls input[type="number"] {
         -moz-appearance: textfield;
     }


    /* Button Styling */
    button {
        padding: 12px 20px; /* Increased padding */
        background-color: #2ecc71; /* Greenish */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 10px; /* Increased margin */
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
        width: 100%; /* Full width buttons */
        box-sizing: border-box;
    }

     button:hover {
        background-color: #27ae60; /* Darker green on hover */
    }

    button:active {
        background-color: #229954; /* Even darker green on active */
        transform: scale(0.98); /* Slightly shrink on click */
    }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
    }


    #resetSimulation {
         background-color: #e74c3c; /* Red */
         margin-top: 8px; /* Smaller margin between buttons */
    }
    #resetSimulation:hover {
         background-color: #c0392b; /* Darker red */
    }
     #resetSimulation:active {
         background-color: #a93226; /* Even darker red */
    }


    .toggle-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* Centered with larger margins */
        background-color: #3498db; /* Blue */
        font-size: 1.2em;
        padding: 15px 25px;
        border-radius: 8px;
    }
     .toggle-button:hover {
         background-color: #2980b9;
    }
     .toggle-button:active {
         background-color: #2471a3;
    }


    /* Explanation Section */
    #explanation {
        margin: 30px auto; /* Centered with larger margins */
        padding: 30px; /* Increased padding */
        border: none;
        border-radius: 12px;
        background-color: #e8f5e9; /* Very light green background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        max-width: 1200px;
    }


    /* Game-like / Animation Elements */
    .round-counter {
        position: absolute;
        top: 10px;
        right: 10px; /* RTL position */
        background-color: rgba(0,0,0,0.5);
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 1em;
        z-index: 10; /* Ensure it's above canvas */
    }

     .progress-bar-container {
        position: absolute;
        bottom: 10px;
        left: 10px; /* RTL position */
        width: calc(100% - 20px); /* Adjust width with padding */
        height: 10px;
        background-color: #bdc3c7; /* Gray background */
        border-radius: 5px;
        overflow: hidden;
        z-index: 10;
     }

    .progress-bar {
        height: 100%;
        width: 0%; /* Starts empty */
        background-color: #2ecc71; /* Green progress */
        transition: width 0.3s ease; /* Smooth transition on width change */
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .simulator-container {
            flex-direction: column; /* Stack vertically on small screens */
            padding: 20px;
            gap: 20px;
        }

        .visualization, .controls, .graph-container {
             min-width: 100%; /* Take full width */
             flex-basis: auto; /* Auto size */
        }

         h1 {
            font-size: 2em;
         }
         h2 {
             font-size: 1.5em;
         }
          h3 {
             font-size: 1.2em;
          }

         .controls input[type="number"],
         .controls select,
         button {
             font-size: 1em;
         }

         .legend span.virus-dot {
             width: 15px;
             height: 15px;
         }

         #virusCanvasContainer, #resistanceGraph {
             height: 300px; /* Slightly smaller height on small screens */
         }
    }


</style>

<script>
    const virusCanvas = document.getElementById('virusCanvas');
    const ctx = virusCanvas.getContext('2d');
    const graphCanvas = document.getElementById('resistanceGraph');
    const graphCtx = graphCanvas.getContext('2d');

    const initialResistantInput = document.getElementById('initialResistant');
    const drugConcentrationSelect = document.getElementById('drugConcentration');
    const numRoundsInput = document.getElementById('numRounds');
    const startSimulationButton = document.getElementById('startSimulation');
    const resetSimulationButton = document.getElementById('resetSimulation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
    const currentRoundDisplay = document.getElementById('currentRoundDisplay');
    const totalRoundsDisplay = document.getElementById('totalRoundsDisplay');
    const roundProgressBar = document.getElementById('roundProgressBar');


    const VISUAL_POP_SIZE = 250; // Increased number of viruses to visualize
    const VIRUS_RADIUS = 6; // Smaller radius for more viruses
    const MUTATION_RATE_SENSITIVE_SURVIVOR = 0.002; // 0.2% chance a *surviving sensitive* virus mutates to resistant during reproduction

    // Survival rates for sensitive viruses under drug pressure (proportion of sensitive that *reproduce* in the next generation's pool)
    // These values are relative to the total survivor pool, then normalized.
    // A higher number means more sensitive survive and reproduce relative to resistant.
    const SENSITIVE_REPRODUCTION_HIGH_DRUG = 0.1; // Low chance for sensitive to reproduce effectively with high drug
    const SENSITIVE_REPRODUCTION_LOW_DRUG = 0.5; // Higher chance for sensitive to reproduce with low drug (relative to resistant)

    // Assume resistant viruses always reproduce effectively regardless of drug
    const RESISTANT_REPRODUCTION_RATE = 1.0;

    let simulationState = {
        sensitive_prop: 1.0,
        resistant_prop: 0.0
    };
    let graphData = [];
    let currentRound = 0;
    let totalRounds = 30; // Default, will be updated from input
    let simulationInterval = null;

    // --- Drawing Functions ---
    function drawViruses() {
        const canvasWidth = virusCanvas.width;
        const canvasHeight = virusCanvas.height;
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);
        ctx.fillStyle = '#e0f7fa'; // Light blue background
        ctx.fillRect(0, 0, canvasWidth, canvasHeight);

        const totalViruses = VISUAL_POP_SIZE;
        const resistantCount = Math.round(simulationState.resistant_prop * totalViruses);
        const sensitiveCount = totalViruses - resistantCount;

        // Create an array of virus types for visualization
        const virusTypes = Array(resistantCount).fill('resistant').concat(Array(sensitiveCount).fill('sensitive'));
        // Shuffle the array for random placement
        for (let i = virusTypes.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [virusTypes[i], virusTypes[j]] = [virusTypes[j], virusTypes[i]];
        }

        // Draw the viruses in a grid-like pattern with some randomness
        const areaPerVirus = (canvasWidth * canvasHeight) / totalViruses;
        const approxSpacing = Math.sqrt(areaPerVirus);
        const cols = Math.floor(canvasWidth / approxSpacing);
        const rows = Math.ceil(totalViruses / cols);

        const x_step = canvasWidth / cols;
        const y_step = canvasHeight / rows;

        for (let i = 0; i < totalViruses; i++) {
            const col = i % cols;
            const row = Math.floor(i / cols);

            // Calculate base position
            const baseX = col * x_step + x_step / 2;
            const baseY = row * y_step + y_step / 2;

            // Add some random jitter
            const x = baseX + (Math.random() - 0.5) * (x_step * 0.6);
            const y = baseY + (Math.random() - 0.5) * (y_step * 0.6);

            // Ensure position is within bounds
            const finalX = Math.max(VIRUS_RADIUS, Math.min(canvasWidth - VIRUS_RADIUS, x));
            const finalY = Math.max(VIRUS_RADIUS, Math.min(canvasHeight - VIRUS_RADIUS, y));


            ctx.beginPath();
            ctx.arc(finalX, finalY, VIRUS_RADIUS, 0, Math.PI * 2);
            ctx.fillStyle = virusTypes[i] === 'resistant' ? '#e74c3c' : '#3498db';
            ctx.shadowColor = 'rgba(0,0,0,0.3)'; /* Add subtle shadow */
            ctx.shadowBlur = 3;
            ctx.fill();
            ctx.shadowColor = 'transparent'; /* Reset shadow */
            ctx.shadowBlur = 0;
        }
    }

    function drawGraph() {
        const canvasWidth = graphCanvas.width;
        const canvasHeight = graphCanvas.height;
        graphCtx.clearRect(0, 0, canvasWidth, canvasHeight);
        graphCtx.fillStyle = '#ffffff'; // White background
        graphCtx.fillRect(0, 0, canvasWidth, canvasHeight);


        const padding = 35; // Increased padding for labels
        const graphWidth = canvasWidth - 2 * padding;
        const graphHeight = canvasHeight - 2 * padding;

        // Draw axes
        graphCtx.beginPath();
        graphCtx.strokeStyle = '#7f8c8d'; // Axis color
        graphCtx.lineWidth = 1.5;
        graphCtx.moveTo(padding, padding);
        graphCtx.lineTo(padding, canvasHeight - padding); // Y-axis
        graphCtx.lineTo(canvasWidth - padding, canvasHeight - padding); // X-axis
        graphCtx.stroke();

        // Labels
        graphCtx.fillStyle = '#555';
        graphCtx.font = '12px Rubik, sans-serif';
        graphCtx.textAlign = 'center';
        graphCtx.fillText("סבב טיפול", canvasWidth / 2, canvasHeight - padding + 28); // Adjusted Y position
        graphCtx.save(); // Save current context state
        graphCtx.translate(padding - 25, canvasHeight / 2); // Move origin for Y-axis label
        graphCtx.rotate(-Math.PI / 2); // Rotate text
        graphCtx.fillText("אחוז עמידות (%)", 0, 0);
        graphCtx.restore(); // Restore context state

         // Y-axis markers (0%, 25%, 50%, 75%, 100%)
        for(let i=0; i<=4; i++) {
            const y = canvasHeight - padding - (graphHeight / 4) * i;
            graphCtx.beginPath();
            graphCtx.moveTo(padding, y);
            graphCtx.lineTo(padding - 6, y); // Adjusted line length
            graphCtx.strokeStyle = '#bdc3c7'; // Marker color
            graphCtx.stroke();
            graphCtx.textAlign = 'right';
             graphCtx.font = '11px Rubik, sans-serif';
            graphCtx.fillText(i * 25 + "%", padding - 12, y + 4); // Adjusted position
        }

         // X-axis markers (based on max rounds)
         const maxRounds = parseInt(numRoundsInput.value, 10) || 30;
         const numMarkersX = Math.min(maxRounds, 10); // Show up to 10 markers
         const stepX = maxRounds <= 10 ? 1 : Math.max(1, Math.floor(maxRounds / numMarkersX)); // Ensure at least step 1

         for (let i = 0; i * stepX <= maxRounds; i++) {
             const round = i * stepX;
             const x = padding + (graphWidth / maxRounds) * round;
             graphCtx.beginPath();
             graphCtx.moveTo(x, canvasHeight - padding);
             graphCtx.lineTo(x, canvasHeight - padding + 6); // Adjusted line length
             graphCtx.strokeStyle = '#bdc3c7'; // Marker color
             graphCtx.stroke();
             graphCtx.textAlign = 'center';
             graphCtx.font = '11px Rubik, sans-serif';
             graphCtx.fillText(round, x, canvasHeight - padding + 18); // Adjusted position
         }


        // Draw the line graph
        graphCtx.beginPath();
        graphCtx.strokeStyle = '#2980b9'; /* Darker blue line */
        graphCtx.lineWidth = 3; /* Thicker line */

        graphData.forEach((point, index) => {
            const x = padding + (graphWidth / maxRounds) * point.round;
            const y = canvasHeight - padding - (graphHeight / 100) * point.resistance_percent;
            if (index === 0) {
                graphCtx.moveTo(x, y);
            } else {
                graphCtx.lineTo(x, y);
            }
        });
        graphCtx.stroke();

         // Draw points
         graphData.forEach(point => {
            const x = padding + (graphWidth / maxRounds) * point.round;
            const y = canvasHeight - padding - (graphHeight / 100) * point.resistance_percent;
            graphCtx.fillStyle = '#3498db'; /* Point color matching sensitive virus */
            graphCtx.beginPath();
            graphCtx.arc(x, y, 4, 0, Math.PI * 2); /* Larger points */
            graphCtx.fill();
             graphCtx.strokeStyle = '#ffffff'; /* White border for points */
             graphCtx.lineWidth = 1.5;
             graphCtx.stroke();
        });
    }

    // --- Simulation Logic ---
    function initializeSimulation() {
        const initialResistantPercent = parseFloat(initialResistantInput.value) || 0;
        simulationState.resistant_prop = Math.max(0, Math.min(1, initialResistantPercent / 100)); // Clamp between 0 and 1
        simulationState.sensitive_prop = 1.0 - simulationState.resistant_prop;

        graphData = [];
        currentRound = 0;
        totalRounds = parseInt(numRoundsInput.value, 10) || 30;
        graphData.push({ round: currentRound, resistance_percent: simulationState.resistant_prop * 100 });

        updateVisualization();
        drawGraph(); // Initial graph state
        updateRoundDisplay(); // Update round counter
        updateProgressBar(); // Update progress bar

        startSimulationButton.disabled = false;
        resetSimulationButton.disabled = false;

        console.log(`Initialized: Resistant ${simulationState.resistant_prop.toFixed(2)}, Sensitive ${simulationState.sensitive_prop.toFixed(2)}`);
    }

    function simulateRound() {
        currentRound++;
        const drugConcentration = drugConcentrationSelect.value;
        // Get effective reproduction rate multiplier for sensitive viruses based on drug concentration
        const sensitiveReproductionMultiplier = drugConcentration === 'high' ? SENSITIVE_REPRODUCTION_HIGH_DRUG : SENSITIVE_REPRODUCTION_LOW_DRUG;

        const currentSensitiveProp = simulationState.sensitive_prop;
        const currentResistantProp = simulationState.resistant_prop;

        // Calculate the 'weight' of each type in contributing to the next generation *before* considering mutation
        const potentialSensitiveContribution = currentSensitiveProp * sensitiveReproductionMultiplier;
        const potentialResistantContribution = currentResistantProp * RESISTANT_REPRODUCTION_RATE;

        const totalPotentialContribution = potentialSensitiveContribution + potentialResistantContribution;

         // If total potential contribution is zero (e.g., 0 sensitive * 0 survival + 0 resistant * 1 survival), population is extinct
         if (totalPotentialContribution <= 1e-9) { // Use a small threshold for floating point comparison
             console.log("Population extinct!");
             simulationState.sensitive_prop = 0;
             simulationState.resistant_prop = 0;
             graphData.push({ round: currentRound, resistance_percent: 0 });
             stopSimulation();
             updateVisualization();
             drawGraph();
             updateRoundDisplay();
             updateProgressBar();
             return;
         }


        // Calculate proportions in the 'survivor and reproducing' pool
        const sensitiveReproducingProp = potentialSensitiveContribution / totalPotentialContribution;
        const resistantReproducingProp = potentialResistantContribution / totalPotentialContribution;


        // Apply mutation chance: some sensitive reproducers become resistant in the next generation
        const newResistantFromMutation = sensitiveReproducingProp * MUTATION_RATE_SENSITIVE_SURVIVOR;

        // Calculate new proportions for the next generation
        let nextResistantProp = resistantReproducingProp + newResistantFromMutation;
        let nextSensitiveProp = sensitiveReproducingProp * (1 - MUTATION_RATE_SENSITIVE_SURVIVOR);

        // The sum `nextResistantProp + nextSensitiveProp` should ideally be 1, as we normalized the reproducing pool.
        // Re-normalize just in case of minor floating point drift, although it shouldn't significantly deviate from 1.
        const totalNextProp = nextResistantProp + nextSensitiveProp;

         // Re-normalize to ensure proportions sum to 1, but only if the total population isn't effectively zero
         if (totalNextProp > 1e-9) {
             simulationState.resistant_prop = nextResistantProp / totalNextProp;
             simulationState.sensitive_prop = nextSensitiveProp / totalNextProp;
         } else {
              simulationState.resistant_prop = 0;
              simulationState.sensitive_prop = 0;
         }


        graphData.push({ round: currentRound, resistance_percent: simulationState.resistant_prop * 100 });

        updateVisualization();
        drawGraph();
        updateRoundDisplay();
        updateProgressBar();

        console.log(`Round ${currentRound}: Resistant ${(simulationState.resistant_prop*100).toFixed(1)}%, Sensitive ${(simulationState.sensitive_prop*100).toFixed(1)}%`);


        if (currentRound >= totalRounds || simulationState.resistant_prop >= 0.995) {
            console.log("Simulation finished.");
            stopSimulation();
             // Ensure final state is drawn
             updateVisualization();
             drawGraph();
        }
    }

    function startSimulation() {
        if (simulationInterval) {
            clearInterval(simulationInterval);
        }
        initializeSimulation(); // Reset state for a new run
        startSimulationButton.disabled = true;
        // Allow changing settings only when simulation is not running
        initialResistantInput.disabled = true;
        drugConcentrationSelect.disabled = true;
        numRoundsInput.disabled = true;


        // Run one round immediately, then set interval
        simulateRound();
        if (currentRound < totalRounds && simulationState.sensitive_prop + simulationState.resistant_prop > 0) { // Only start interval if simulation is not immediately finished
             simulationInterval = setInterval(simulateRound, 300); // Simulate a round every 300ms
        } else {
             stopSimulation(); // Ensure button is re-enabled even if simulation ended on first round
        }

    }

    function stopSimulation() {
        if (simulationInterval) {
            clearInterval(simulationInterval);
            simulationInterval = null;
        }
        startSimulationButton.disabled = false;
         // Re-enable settings
         initialResistantInput.disabled = false;
         drugConcentrationSelect.disabled = false;
         numRoundsInput.disabled = false;
    }

    function resetSimulation() {
        stopSimulation();
        initializeSimulation();
         resetSimulationButton.disabled = false; // Stay enabled
         // Re-enable settings
         initialResistantInput.disabled = false;
         drugConcentrationSelect.disabled = false;
         numRoundsInput.disabled = false;
    }

    function updateVisualization() {
         // Resize canvas to fit container (important on load and resize)
        virusCanvas.width = virusCanvas.clientWidth;
        virusCanvas.height = virusCanvas.clientHeight;
        drawViruses();
    }

    function updateGraph() {
         // Resize canvas (important on load and resize)
        graphCanvas.width = graphCanvas.clientWidth;
        graphCanvas.height = graphCanvas.clientHeight;
        drawGraph();
    }

    function updateRoundDisplay() {
        currentRoundDisplay.textContent = currentRound;
        totalRoundsDisplay.textContent = totalRounds;
    }

    function updateProgressBar() {
        const progress = (currentRound / totalRounds) * 100;
        roundProgressBar.style.width = `${progress}%`;
    }


    // --- Event Listeners ---
    startSimulationButton.addEventListener('click', startSimulation);
    resetSimulationButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        // Button text is static now, no need to change
    });

     // Update total rounds display immediately when input changes
     numRoundsInput.addEventListener('input', () => {
        totalRounds = parseInt(numRoundsInput.value, 10) || 30;
        totalRoundsDisplay.textContent = totalRounds;
        // Also re-draw graph axes if max rounds change while stopped
        if (!simulationInterval) {
             drawGraph();
        }
     });


     // Resize canvases when the window is resized
     window.addEventListener('resize', () => {
         updateVisualization();
         updateGraph();
     });


    // --- Initial Setup ---
    initializeSimulation(); // Set up on page load

     // Display the mutation rate
     document.querySelector('.mutation-rate-display').textContent = `${(MUTATION_RATE_SENSITIVE_SURVIVOR * 100).toFixed(1)}%`;


</script>
```