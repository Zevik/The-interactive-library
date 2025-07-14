---
title: "מרוץ ההגנה: שרידת הצמחים נגד הטורפים"
english_slug: plants-defend-simulation-defense-mechanisms
category: "מדעי החיים / ביולוגיה"
tags:
  - צמחים
  - הגנה
  - אבולוציה
  - בוטניקה
  - אקולוגיה
---
<header>
    <h1>מרוץ ההגנה: שרידת הצמחים נגד הטורפים</h1>
    <p>דמיינו את זה: אתם צמח, תקועים במקום אחד. לאן שלא תסתכלו, אורבות סכנות - במיוחד חיות רעבות שרוצות לנגוס בכם. ובכל זאת, יצורים נייחים לחלוטין כמוכם לא רק שורדים, אלא משגשגים בכל פינה בעולם! איך הם עושים את זה? בואו נצלול לסימולציה שתגלה את הסודות שלהם.</p>
</header>

<div class="simulation-container">
    <h2>זירת הניסוי: בחרו את מגני הצמחים</h2>
    <p class="instructions">בחרו סוג הגנה לכל קבוצת צמחים וצפו כיצד הם שורדים מול הטורפים.</p>
    <div class="controls">
        <div class="group-control">
            <label for="groupA">קבוצה א':</label>
            <select id="groupA">
                <option value="none">ללא הגנה (הכי פשוט)</option>
                <option value="physical">הגנה פיזית (קוצים)</option>
                <option value="chemical">הגנה כימית (רעלן)</option>
            </select>
        </div>
        <div class="group-control">
            <label for="groupB">קבוצה ב':</label>
            <select id="groupB">
                <option value="none">ללא הגנה (הכי פשוט)</option>
                <option value="physical">הגנה פיזית (קוצים)</option>
                <option value="chemical">הגנה כימית (רעלן)</option>
            </select>
        </div>
        <div class="group-control">
            <label for="groupC">קבוצה ג':</label>
            <select id="groupC">
                <option value="none">ללא הגנה (הכי פשוט)</option>
                <option value="physical">הגנה פיזית (קוצים)</option>
                <option value="chemical">הגנה כימית (רעלן)</option>
            </select>
        </div>
        <button id="startSimulation" class="sim-button">התחילו במרוץ!</button>
        <button id="resetSimulation" class="sim-button" disabled>התחילו מחדש</button>
    </div>

    <div id="simulationArea">
        <!-- Plants and herbivores will be added here by JavaScript -->
        <div class="ground"></div> <!-- Visual element for the ground -->
    </div>

    <div id="results">
        <h3>תוצאות המרוץ: מי שרד?</h3>
        <p id="resultsA" class="result-line">קבוצה א': מחכה להתחיל...</p>
        <p id="resultsB" class="result-line">קבוצה ב': מחכה להתחיל...</p>
        <p id="resultsC" class="result-line">קבוצה ג': מחכה להתחיל...</p>
        <p id="status" class="status-line">סטטוס: מוכנים לניסוי?</p>
    </div>
</div>

<button id="toggleExplanation" class="info-button">גלו עוד על הגנות הצמחים</button>

<div id="explanation" style="display: none;" class="explanation-box">
    <h2>הסבר מעמיק: מאחורי מנגנוני ההגנה</h2>

    <h3>הקדמה: האתגר הגדול - לשרוד בלי לזוז</h3>
    <p>תארו לעצמכם שאתם לא יכולים לזוז ממקומכם לעולם. עכשיו תארו לכם שסביבכם מסתובבים יצורים שרוצים לאכול אתכם. זה בערך מצבם של הצמחים. בניגוד לבעלי חיים שיכולים לברוח, להתחבא או להילחם, הצמחים חייבים להשתמש באסטרטגיות אחרות כדי לשרוד מול אוכלי עשב (הרביבורים).</p>

    <h3>אוכלי עשב: איום מתמיד</h3>
    <p>אוכלי עשב הם בעלי חיים שניזונים מחלקים של צמחים – עלים, גבעולים, שורשים, פרחים או פירות. אכילה מוגזמת עלולה להחליש צמח, למנוע ממנו לבצע פוטוסינתזה, להתרבות, ובמקרים קיצוניים גם להרוג אותו. האיום מגיע מחרקים קטנטנים ועד יונקים ענקיים.</p>

    <h3>הגנות פיזיות: מחסומים טבעיים</h3>
    <p>מנגנונים אלו יוצרים קושי פיזי לאכול או להתקרב לצמח:</p>
    <ul>
        <li><strong>קוצים ודִרדרים:</strong> מבנים מחודדים על גזעים, ענפים או עלים. הם מרתיעים ואף פוצעים בעלי חיים שמנסים לנגוס או לטפס. חשבו על שושנים, קקטוסים, או שיטה. הקוצים הופכים את הארוחה לפחות כדאית ואף מכאיבה.</li>
        <li><strong>שכבת שעווה (קוטיקולה) וקליפה קשה:</strong> שכבת שעווה על עלים (קוטיקולה עבה) או קליפה עבה וקשה על גזעים, פירות או זרעים. זה מקשה על חרקים לחדור ועל בעלי חיים גדולים יותר ללעוס ביעילות. בנוסף, השעווה עוזרת לצמח לשמור על מים.</li>
    </ul>

    <h3>הגנות כימיות: "ספריי" ו"טעם רע" מהטבע</h3>
    <p>צמחים מסוימים מייצרים חומרים כימיים המשפיעים על אוכלי העשב כשהם נאכלים (או אפילו רק מורחים עליהם):</p>
    <ul>
        <li><strong>רעלנים:</strong> צמחים מייצרים חומרים רעילים (מטבוליטים משניים) שאינם חיוניים לחיי הצמח היומיומיים, אך מסוכנים או קטלניים לאוכלי עשב. רעלנים אלו יכולים להשפיע על מערכת העצבים, העיכול או לגרום לנזק פנימי. אכילת כמות קטנה גורמת לחיה תחושה לא נעימה והיא לומדת להימנע מהצמח בעתיד. דוגמאות כוללות חומרים כמו ניקוטין, קפאין, או ציאניד בצמחים שונים.</li>
        <li><strong>חומרים מרתיעים:</strong> צמחים יכולים לייצר חומרים בעלי טעם מר, חריף או ריח דוחה במיוחד (כמו בשום, בצל, או צמחי תבלין מסוימים). הטעם או הריח מונעים מהחיה לאכול את הצמח או גורמים לה להפסיק מיד אחרי הנגיסה הראשונה.</li>
        <li><strong>חומרים מעכבי עיכול:</strong> חומרים כמו טאנינים או מעכבי אנזימים שמקשים על החיה לעכל את רקמות הצמח או לספוג מהן חומרי מזון חיוניים. החיה אולי אוכלת, אבל לא מקבלת מספיק תזונה ולכן לומדת להימנע.</li>
    </ul>

    <h3>האבולוציה וה"מרוץ" הבלתי נגמר</h3>
    <p>מנגנוני ההגנה של הצמחים הם תוצאה של אבולוציה ארוכה. צמחים עם הגנות יעילות יותר שרדו, התרבו והעבירו את התכונות האלה הלאה. אבל גם אוכלי העשב לא נשארו מאחור! חלקם פיתחו יכולת לנטרל רעלנים ספציפיים, להתמודד עם קוצים, או אפילו לנצל את הרעלנים לטובתם. התהליך הזה, שבו הצמחים מפתחים הגנות ואוכלי העשב מפתחים דרכים להתגבר עליהן, מכונה "מרוץ חימוש אבולוציוני". הוא יצר את המגוון המדהים של צמחים ובעלי חיים שאנו רואים היום.</p>

    <h3>עוד אסטרטגיות שרידה (מחוץ לסימולציה)</h3>
    <p>הגנות הצמחים לא מסתכמות רק בהגנות ישירות:</p>
    <ul>
        <li><strong>הגנה עקיפה:</strong> צמחים פצועים לעיתים מפרישים ריחות המושכים טורפים טבעיים של אוכלי העשב. כך הצמח "קורא לעזרה".</li>
        <li><strong>תזמון ו"הצפה":</strong> צמחים מסוימים משחררים כמויות עצומות של זרעים או פירות בפרק זמן קצר (למשל, עצי אלון עם בלוטים). כך גם אם אוכלי הזרעים טורפים כמות גדולה, מספיק זרעים שורדים כדי להמשיך את הדור הבא.</li>
    </ul>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: #eef4f8; /* Soft background */
        color: #333;
    }

    h1, h2, h3 {
        color: #2c3e50; /* Dark blue/grey */
        text-align: center;
        margin-bottom: 15px;
    }

    header p, .instructions {
        text-align: center;
        max-width: 800px;
        margin: 10px auto 30px auto;
        font-size: 1.1em;
    }

    .simulation-container {
        border: 1px solid #bdc3c7; /* Light grey border */
        padding: 25px;
        margin-bottom: 30px;
        background-color: #ffffff;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft shadow */
    }

    .simulation-container h2 {
         margin-top: 0;
         text-align: right; /* Section title aligns right */
         color: #34495e;
    }

    .controls {
        display: flex;
        flex-wrap: wrap;
        gap: 20px; /* Increased gap */
        margin-bottom: 25px;
        align-items: flex-end;
        justify-content: center; /* Center controls */
        padding: 15px;
        background-color: #ecf0f1; /* Lighter background for controls */
        border-radius: 8px;
    }

    .group-control {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align labels/selects to the left within control */
        min-width: 150px; /* Ensure controls don't get too narrow */
    }

    .group-control label {
        margin-bottom: 8px; /* More space below label */
        font-weight: bold;
        color: #555;
        font-size: 0.95em;
    }

    .group-control select {
        padding: 8px;
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        font-size: 1em;
        background-color: #ffffff;
        cursor: pointer;
        min-width: 150px; /* Match label width */
    }

    .sim-button {
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        color: white;
        background-color: #3498db; /* Blue button */
        transition: background-color 0.3s ease, transform 0.1s ease;
        min-width: 120px; /* Consistent button width */
        text-align: center;
    }

    .sim-button:hover:not(:disabled) {
        background-color: #2980b9; /* Darker blue on hover */
    }

    .sim-button:active:not(:disabled) {
         transform: scale(0.98);
    }

    .sim-button:disabled {
        background-color: #bdc3c7;
        cursor: not-allowed;
    }

    #startSimulation {
        background-color: #2ecc71; /* Green start button */
    }
    #startSimulation:hover:not(:disabled) {
        background-color: #27ae60;
    }

     #resetSimulation {
        background-color: #e74c3c; /* Red reset button */
    }
     #resetSimulation:hover:not(:disabled) {
        background-color: #c0392b;
    }


    #simulationArea {
        width: 100%;
        height: 450px; /* Slightly taller */
        border: 1px solid #a0d468; /* Border matching ground color */
        background-color: #c8e6c9; /* Light green field */
        position: relative;
        overflow: hidden;
        box-sizing: border-box;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    #simulationArea .ground {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 50px; /* Ground height */
        background-color: #a0d468; /* Darker green for ground */
        z-index: 0; /* Ensure plants/herbivores are above */
    }


    .plant {
        width: 25px; /* Slightly larger plant */
        height: 35px; /* Slightly taller plant */
        position: absolute;
        bottom: 5px; /* Plants are on the ground layer */
        background-color: #4CAF50; /* Base green */
        border: 1px solid #388E3C; /* Darker border */
        box-sizing: border-box;
        border-radius: 5px 5px 2px 2px; /* Slightly rounded top */
        display: flex;
        justify-content: center;
        align-items: flex-start; /* Align text to the top */
        font-size: 9px;
        color: rgba(255, 255, 255, 0.9);
        font-weight: bold;
        text-shadow: 0 0 3px rgba(0,0,0,0.5);
        transition: bottom 0.3s ease-out, transform 0.3s ease-out, opacity 0.8s ease-out; /* Smoother transitions */
        z-index: 1; /* Above ground */
        padding-top: 3px;
    }

    .plant.physical {
        background-color: #66bb6a; /* Greener */
        border-color: #43a047;
    }
     .plant.physical::before { /* Add a visual hint for spikes */
        content: '🌵'; /* Cactus/spike emoji */
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 14px;
        line-height: 1;
        color: #555; /* Spike color */
     }

    .plant.chemical {
        background-color: #9ccc65; /* Yellowish green */
        border-color: #7cb342;
    }
     .plant.chemical::before { /* Add a visual hint for chemical */
        content: '🧪'; /* Test tube/chemical emoji */
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 14px;
         line-height: 1;
         color: #555;
     }

    .plant.none::before {
         content: '🌱'; /* Simple sprout emoji */
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 14px;
         line-height: 1;
         color: #555;
    }


    .plant.eaten {
        opacity: 0;
        transform: scale(0.5); /* Shrink when eaten */
        /* pointer-events: none; /* Disable interaction if needed */
    }

    .plant.being-eaten {
         /* Add a subtle animation or style when being eaten */
         transform: scale(0.95);
         filter: brightness(0.9);
    }


    .herbivore {
        width: 35px; /* Slightly larger herbivore */
        height: 35px;
        position: absolute;
        background-color: #8d6e63; /* Brown */
        border: 2px solid #5d4037;
        border-radius: 50%; /* Round shape */
        transition: left linear, top linear; /* Smooth movement */
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 14px;
        color: white;
        font-weight: bold;
        text-shadow: 0 0 3px rgba(0,0,0,0.5);
        z-index: 2; /* Above plants */
         animation: pulse 1.5s infinite alternate; /* Subtle breathing animation */
    }

    @keyframes pulse {
        from { transform: scale(1); }
        to { transform: scale(1.05); }
    }

     .herbivore.stunned {
         background-color: #ffb300; /* Orange when stunned */
         border-color: #f57c00;
         animation: shake 0.5s infinite; /* Shaking animation when stunned */
         filter: brightness(1.2);
     }

     @keyframes shake {
         0%, 100% { transform: translateX(0); }
         10%, 30%, 50%, 70%, 90% { transform: translateX(-3px); }
         20%, 40%, 60%, 80% { transform: translateX(3px); }
     }

     .herbivore.eating {
         background-color: #4caf50; /* Greenish when eating */
         border-color: #388e3c;
         animation: none; /* Stop pulse while eating */
         transform: scale(1.1); /* Slightly bigger when eating */
     }

     .herbivore.sick {
         background-color: #aed581; /* Lighter green/sick color */
         border-color: #8bc34a;
         animation: pulse 1s infinite alternate; /* Sick pulse */
         filter: grayscale(50%);
     }


    #results {
        margin-top: 25px;
        padding: 20px;
        border: 2px dashed #bdc3c7;
        background-color: #ecf0f1; /* Lighter background for results */
        border-radius: 8px;
        text-align: right;
    }
    #results h3 {
        margin-top: 0;
        color: #34495e;
         text-align: right;
    }
    .result-line {
        margin: 8px 0; /* More space between result lines */
        font-size: 1.05em;
        color: #555;
    }
    #status {
        font-weight: bold;
        color: #2c3e50;
        margin-top: 15px;
    }

    .info-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* Center and add more space */
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        cursor: pointer;
        border: 1px solid #3498db; /* Blue border */
        background-color: #3498db; /* Blue background */
        color: white;
        border-radius: 5px;
        text-align: center;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
    }
    .info-button:hover {
        background-color: #2980b9;
        border-color: #2980b9;
    }
     .info-button:active {
         transform: scale(0.98);
     }


    .explanation-box {
        border: 1px solid #bdc3c7;
        padding: 20px;
        margin-top: 25px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    }
     .explanation-box h2 {
         text-align: right;
         color: #34495e;
     }
    .explanation-box h3 {
         text-align: right;
         color: #555;
         margin-top: 20px;
    }
    .explanation-box p {
        margin-bottom: 15px;
        color: #444;
    }
    .explanation-box ul {
        margin-top: 10px;
        padding-right: 25px; /* Indent list items for RTL */
        color: #444;
    }
    .explanation-box li {
        margin-bottom: 10px; /* More space between list items */
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .controls {
            flex-direction: column;
            align-items: stretch;
        }
        .group-control {
            align-items: stretch;
        }
        .group-control select, .sim-button {
            width: 100%;
            min-width: auto;
        }
         .info-button {
             width: 90%;
         }
    }

</style>

<script>
    const simulationArea = document.getElementById('simulationArea');
    const startButton = document.getElementById('startSimulation');
    const resetButton = document.getElementById('resetSimulation');
    const groupASelect = document.getElementById('groupA');
    const groupBSelect = document.getElementById('groupB');
    const groupCSelect = document.getElementById('groupC');
    const resultsA = document.getElementById('resultsA');
    const resultsB = document.getElementById('resultsB');
    const resultsC = document.getElementById('resultsC');
    const statusElement = document.getElementById('status');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    // Ensure simulation area dimensions are calculated after layout
    let SIM_WIDTH = 0;
    let SIM_HEIGHT = 0;
    const groundHeight = 50; // Must match CSS .ground height
    const updateSimulationAreaSize = () => {
        SIM_WIDTH = simulationArea.offsetWidth;
        SIM_HEIGHT = simulationArea.offsetHeight;
    };
    window.addEventListener('resize', updateSimulationAreaSize);


    const PLANT_COUNT_PER_GROUP = 12; // More plants
    const HERBIVORE_COUNT = 3; // More herbivores
    const SIMULATION_DURATION_STEPS = 1000; // Longer simulation
    const HERBIVORE_SPEED = 1; // Slightly slower for better visual tracking
    const HERBIVORE_REACH_DISTANCE = 15; // Distance to consider eating
    const HERBIVORE_EATING_DURATION = 30; // Steps herbivore spends 'eating'
    const HERBIVORE_STUN_PHYSICAL_DURATION = 50; // Steps herbivore is stunned after physical defense
    const HERBIVORE_STUN_CHEMICAL_DURATION = 150; // Steps herbivore is stunned after chemical defense
    const HERBIVORE_PHYSICAL_AVOID_DURATION = 150; // Steps herbivore avoids that specific physical plant
    const HERBIVORE_CHEMICAL_GLOBAL_AVOID_DISTANCE = 150; // Distance herbivore avoids *any* chemical plant after being sick

    let plants = [];
    let herbivores = [];
    let simulationInterval = null;
    let currentStep = 0;

    // --- Classes ---

    class Plant {
        constructor(id, groupId, defense, x, y) {
            this.id = id;
            this.groupId = groupId;
            this.defense = defense; // 'none', 'physical', 'chemical'
            this.x = x; // Position from left
            this.y = y; // Position from bottom of simulation area (top of ground)
            this.isEaten = false;
            this.element = null; // DOM element
            this.lastAttemptedByHerbivore = {}; // Track last attempt step by herbivore ID for physical avoidance
        }

        createElement() {
            this.element = document.createElement('div');
            this.element.classList.add('plant');
            this.element.classList.add(this.defense); // Add class for styling based on defense
            this.element.style.left = `${this.x}px`;
            this.element.style.bottom = `${this.y}px`; // Position from bottom
            this.element.style.transform = `translateX(-50%)`; // Center based on left

            simulationArea.appendChild(this.element);
        }

        markAsEaten() {
            if (!this.isEaten) {
                this.isEaten = true;
                 if (this.element) {
                    this.element.classList.add('eaten');
                     // Remove element from DOM after transition
                     this.element.addEventListener('transitionend', () => {
                          if (this.element && this.element.parentNode) {
                             this.element.parentNode.removeChild(this.element);
                          }
                     });
                 }
                 console.log(`Plant ${this.id} (Group ${this.groupId}, ${this.defense}) was eaten.`);
            }
        }

         startEatingAnimation() {
             if (this.element && !this.isEaten) {
                 this.element.classList.add('being-eaten');
             }
         }

         stopEatingAnimation() {
             if (this.element && !this.isEaten) {
                 this.element.classList.remove('being-eaten');
             }
         }


        canBeTargetedBy(herbivore, currentStep) {
            // Plants already eaten cannot be targeted
            if (this.isEaten) return false;

            // Herbivores might avoid physical plants for a short duration after hitting one
             const lastAttemptStep = this.lastAttemptedByHerbivore[herbivore.id] || -Infinity;
             if (this.defense === 'physical' && currentStep - lastAttemptStep < HERBIVORE_PHYSICAL_AVOID_DURATION) {
                 return false; // Avoid this specific physical plant recently hit
             }

             // Herbivores might avoid chemical plants from a distance after being sick from ANY chemical plant
             if (this.defense === 'chemical' && herbivore.feltSickFromChemical) {
                 // Calculate distance from herbivore's current position to this plant's position
                 // Herbivore Y is from top, Plant Y is from bottom
                 const plantY_top = SIM_HEIGHT - this.y;
                 const dist = Math.sqrt((herbivore.x - this.x)**2 + (herbivore.y - plantY_top)**2);

                  if (dist < HERBIVORE_CHEMICAL_GLOBAL_AVOID_DISTANCE) {
                      return false; // Avoid *any* chemical plant within range after prior bad experience
                  }
             }

            return true;
        }

        recordAttempt(herbivoreId, currentStep) {
             this.lastAttemptedByHerbivore[herbivoreId] = currentStep;
        }
    }

    class Herbivore {
        constructor(id, x, y) {
            this.id = id;
            this.x = x;
            this.y = y; // Y is relative to the top of the container
            this.element = null; // DOM element
            this.targetPlant = null;
            this.stunDuration = 0;
            this.eatingDuration = 0;
            this.feltSickFromChemical = false; // Flag to indicate bad experience with chemical defense
             this.chemicalAvoidanceTimer = 0; // Timer for how long to apply global chemical avoidance
        }

        createElement() {
            this.element = document.createElement('div');
            this.element.classList.add('herbivore');
            // this.element.textContent = this.id; // Optional: Display ID
            this.element.style.left = `${this.x}px`;
            this.element.style.top = `${this.y}px`;
            simulationArea.appendChild(this.element);
        }

        updateElementPosition() {
            this.element.style.left = `${this.x}px`;
            this.element.style.top = `${this.y}px`;
        }

        move(plants, currentStep) {
             // Handle stun duration
            if (this.stunDuration > 0) {
                this.stunDuration--;
                if (!this.element.classList.contains('stunned')) this.element.classList.add('stunned');
                if (this.stunDuration === 0) {
                     this.element.classList.remove('stunned');
                     if(this.feltSickFromChemical) {
                         this.element.classList.add('sick'); // Stay 'sick' visually for a while
                         this.chemicalAvoidanceTimer = HERBIVORE_STUN_CHEMICAL_DURATION * 2; // Apply global avoidance timer
                     } else {
                         this.element.classList.remove('sick');
                     }
                }
                return null; // Cannot move while stunned
            }

            // Handle chemical avoidance timer
            if (this.chemicalAvoidanceTimer > 0) {
                this.chemicalAvoidanceTimer--;
                 if (this.chemicalAvoidanceTimer === 0 && this.element.classList.contains('sick')) {
                     this.element.classList.remove('sick');
                 }
            }


            // Handle eating duration
            if (this.eatingDuration > 0) {
                 this.eatingDuration--;
                 if (!this.element.classList.contains('eating')) this.element.classList.add('eating');
                 if (this.targetPlant) this.targetPlant.startEatingAnimation();

                 if (this.eatingDuration === 0) {
                     this.element.classList.remove('eating');
                     if (this.targetPlant) this.targetPlant.stopEatingAnimation();

                     // Finish eating - apply defense effect or eat plant
                     const plant = this.targetPlant;
                     this.targetPlant = null; // Clear target after interaction

                     if (plant) { // Check if plant still exists (wasn't eaten by another herbivore)
                          plant.recordAttempt(this.id, currentStep); // Record interaction attempt

                         switch (plant.defense) {
                             case 'none':
                                 plant.markAsEaten();
                                 console.log(`Herbivore ${this.id} ate plant ${plant.id} (none).`);
                                 break;
                             case 'physical':
                                 this.stunDuration = HERBIVORE_STUN_PHYSICAL_DURATION;
                                 console.log(`Herbivore ${this.id} hit physical defense on plant ${plant.id}! Stunned.`);
                                 break;
                             case 'chemical':
                                 this.stunDuration = HERBIVORE_STUN_CHEMICAL_DURATION;
                                 this.feltSickFromChemical = true; // Mark as having a bad experience
                                  this.element.classList.add('sick'); // Become visually 'sick' immediately
                                 console.log(`Herbivore ${this.id} tasted chemical defense on plant ${plant.id}! Sick and stunned.`);
                                 break;
                         }
                     }
                 }
                 return null; // Cannot move while eating
            }

            // Not stunned, not eating - find target and move
            let closestPlant = null;
            let minDist = Infinity;

            // Re-evaluate target if current one is invalid or too far
             if (this.targetPlant && !this.targetPlant.canBeTargetedBy(this, currentStep)) {
                 this.targetPlant = null; // Target is no longer valid
             }

             // If no target, find the closest valid one
            if (!this.targetPlant) {
                 let candidatePlants = plants.filter(plant => plant.canBeTargetedBy(this, currentStep));

                 for (const plant of candidatePlants) {
                     // Need plant's Y relative to top for distance calculation
                     const plantY_top = SIM_HEIGHT - plant.y;
                     const dist = Math.sqrt((this.x - plant.x)**2 + (this.y - plantY_top)**2);
                     if (dist < minDist) {
                         minDist = dist;
                         closestPlant = plant;
                     }
                 }
                 this.targetPlant = closestPlant; // Set new target
            } else {
                 // Already have a valid target, use it
                 closestPlant = this.targetPlant;
            }


            if (closestPlant) {
                 // Need plant's Y relative to top for movement calculation
                const targetY_top = SIM_HEIGHT - closestPlant.y;
                const angle = Math.atan2(targetY_top - this.y, closestPlant.x - this.x);
                const dx = Math.cos(angle) * HERBIVORE_SPEED;
                const dy = Math.sin(angle) * HERBIVORE_SPEED;

                this.x += dx;
                this.y += dy;

                // Clamp position within simulation area bounds (considering herbivore size)
                this.x = Math.max(0, Math.min(SIM_WIDTH - this.element.offsetWidth, this.x));
                this.y = Math.max(0, Math.min(SIM_HEIGHT - this.element.offsetHeight, this.y));

                this.updateElementPosition();

                 // Re-calculate distance after move
                 const plantY_top = SIM_HEIGHT - closestPlant.y;
                 const dist = Math.sqrt((this.x - closestPlant.x)**2 + (this.y - plantY_top)**2);


                // Check if close enough to start eating
                if (dist <= HERBIVORE_REACH_DISTANCE) {
                    this.eatingDuration = HERBIVORE_EATING_DURATION; // Start eating sequence
                    return null; // Didn't finish eating this step, just started
                }
            } else {
                 // No targetable plants left or found, wander randomly
                 this.x += (Math.random() - 0.5) * HERBIVORE_SPEED * 0.5; // Slower random wander
                 this.y += (Math.random() - 0.5) * HERBIVORE_SPEED * 0.5;
                 // Clamp position
                 this.x = Math.max(0, Math.min(SIM_WIDTH - this.element.offsetWidth, this.x));
                 this.y = Math.max(0, Math.min(SIM_HEIGHT - this.element.offsetHeight, this.y));
                 this.updateElementPosition();
            }

            return null; // No plant interaction resulting in state change this step (eating handled separately)
        }
    }

    // --- Simulation Logic ---

    function initializeSimulation() {
         updateSimulationAreaSize(); // Get current dimensions

        // Clear previous elements, except ground
        const existingElements = simulationArea.querySelectorAll('.plant, .herbivore');
        existingElements.forEach(el => el.remove());

        plants = [];
        herbivores = [];
        currentStep = 0;

        const defenseA = groupASelect.value;
        const defenseB = groupBSelect.value;
        const defenseC = groupCSelect.value;

        const plantGroups = [
            { id: 'A', defense: defenseA },
            { id: 'B', defense: defenseB },
            { id: 'C', defense: defenseC }
        ];

        // Create plants in groups
        let plantIdCounter = 0;
        plantGroups.forEach((group, groupIndex) => {
            for (let i = 0; i < PLANT_COUNT_PER_GROUP; i++) {
                // Distribute plants horizontally within sections based on group
                const sectionWidth = SIM_WIDTH / plantGroups.length;
                const sectionStartX = groupIndex * sectionWidth;
                // Add randomness within the section and ensure plants are within bounds
                 const x = sectionStartX + Math.random() * sectionWidth * 0.8 + sectionWidth * 0.1;
                const y = groundHeight - 5 + Math.random() * 10; // Place plants just above the ground, with slight vertical variation

                const plant = new Plant(plantIdCounter, group.id, group.defense, x, y);
                plants.push(plant);
                plant.createElement();
                plantIdCounter++;
            }
        });

        // Create herbivores
        for (let i = 0; i < HERBIVORE_COUNT; i++) {
            // Place herbivores at a starting position (e.g., left side), varied vertically
            const x = 30 + Math.random() * 70;
             const y = SIM_HEIGHT * 0.3 + (i / (HERBIVORE_COUNT - 1 || 1)) * SIM_HEIGHT * 0.4 + (Math.random() - 0.5) * 50; // Distribute vertically
            const herbivore = new Herbivore(i + 1, x, y);
            herbivores.push(herbivore);
            herbivore.createElement();
        }

        updateResultsDisplay();
        statusElement.textContent = 'סטטוס: מוכנים לניסוי? בחרו הגנות והתחילו!';
        startButton.disabled = false;
        resetButton.disabled = true;
         groupASelect.disabled = false;
        groupBSelect.disabled = false;
        groupCSelect.disabled = false;
    }

    function runSimulationStep() {
        currentStep++;
        statusElement.textContent = `סטטוס: המרוץ בעיצומו! שלב ${currentStep}/${SIMULATION_DURATION_STEPS}`;

        let livingPlants = plants.filter(p => !p.isEaten);

        // Herbivore actions
        for (const herbivore of herbivores) {
             // Herbivore's move method now handles eating and defense reactions internally
             herbivore.move(plants, currentStep);
        }

         // Clean up eaten plants' elements (redundant due to transitionend listener, but good fallback)
         plants = plants.filter(p => !p.isEaten);
         // Note: This reassigns the array, need to be careful if other things hold references.
         // A better way might be to just hide/remove the element and keep the object until reset.
         // For this simulation, filtering the main array is simpler and acceptable.

        updateResultsDisplay();

        if (currentStep >= SIMULATION_DURATION_STEPS || livingPlants.length === 0) {
             endSimulation();
        }
    }

    function startSimulation() {
        startButton.disabled = true;
        resetButton.disabled = false;
        groupASelect.disabled = true;
        groupBSelect.disabled = true;
        groupCSelect.disabled = true;

        // Check if simulation needs initialization or just needs to resume
        if (simulationInterval === null || currentStep === 0) {
             initializeSimulation(); // Setup for a fresh run
             // Give a moment for DOM elements to render before starting movement
             setTimeout(() => {
                 simulationInterval = setInterval(runSimulationStep, 50); // Run simulationStep at a set interval (faster)
             }, 100); // Short delay
        } else {
             // Resume simulation if it was paused (though there's no pause button currently)
             simulationInterval = setInterval(runSimulationStep, 50);
        }


    }

    function endSimulation() {
        clearInterval(simulationInterval);
        simulationInterval = null;
        const livingPlantsCount = plants.filter(p => !p.isEaten).length;
        if (livingPlantsCount === 0) {
             statusElement.textContent = `סטטוס: המרוץ הסתיים! כל הצמחים נאכלו לאחר ${currentStep} שלבים.`;
        } else if (currentStep >= SIMULATION_DURATION_STEPS) {
             statusElement.textContent = `סטטוס: המרוץ הסתיים לאחר ${currentStep} שלבים.`;
        } else {
             statusElement.textContent = `סטטוס: המרוץ הסתיים מוקדם.`;
        }

        updateResultsDisplay(); // Final update
        startButton.disabled = false;
        resetButton.disabled = false;
         groupASelect.disabled = false;
        groupBSelect.disabled = false;
        groupCSelect.disabled = false;
    }

    function resetSimulation() {
        endSimulation(); // Ensure interval is cleared
        initializeSimulation(); // Reset everything
    }

    function updateResultsDisplay() {
        const totalA = PLANT_COUNT_PER_GROUP;
        const totalB = PLANT_COUNT_PER_GROUP;
        const totalC = PLANT_COUNT_PER_GROUP;

        const eatenA = plants.filter(p => p.groupId === 'A' && p.isEaten).length;
        const eatenB = plants.filter(p => p.groupId === 'B' && p.isEaten).length;
        const eatenC = plants.filter(p => p.groupId === 'C' && p.isEaten).length;

        const survivedA = totalA - eatenA;
        const survivedB = totalB - eatenB;
        const survivedC = totalC - eatenC;

        const survivalRateA = totalA > 0 ? ((survivedA / totalA) * 100).toFixed(1) : 0;
        const survivalRateB = totalB > 0 ? ((survivedB / totalB) * 100).toFixed(1) : 0;
        const survivalRateC = totalC > 0 ? ((survivedC / totalC) * 100).toFixed(1) : 0;

        resultsA.textContent = `קבוצה א' (${getDefenseName(groupASelect.value)}): שרדו ${survivedA} מתוך ${totalA} (${survivalRateA}%)`;
        resultsB.textContent = `קבוצה ב' (${getDefenseName(groupBSelect.value)}): שרדו ${survivedB} מתוך ${totalB} (${survivalRateB}%)`;
        resultsC.textContent = `קבוצה ג' (${getDefenseName(groupCSelect.value)}): שרדו ${survivedC} מתוך ${totalC} (${survivalRateC}%)`;
    }

    function getDefenseName(value) {
        switch(value) {
            case 'none': return 'ללא הגנה';
            case 'physical': return 'הגנה פיזית (קוצים)';
            case 'chemical': return 'הגנה כימית (רעלן)';
            default: return ''; // Should not happen
        }
    }

     function getDefenseDescription(value) {
         switch(value) {
             case 'none': return 'פגיעים לטריפה';
             case 'physical': return 'מכאיבים לטורפים';
             case 'chemical': return 'גורמים לטורפים לחלות';
             default: return '';
         }
     }


    // --- Event Listeners ---

    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'גלו עוד על הגנות הצמחים';
    });

    // --- Initial Setup ---
    window.onload = () => {
        initializeSimulation(); // Setup the initial state on page load
    };


</script>
---
```