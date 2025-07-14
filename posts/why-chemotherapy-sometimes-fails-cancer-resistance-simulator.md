---
title: "מדוע הכימותרפיה מפסיקה לעבוד? סימולטור עמידות סרטנית"
english_slug: why-chemotherapy-sometimes-fails-cancer-resistance-simulator
category: "מדעי החיים / רפואה"
tags:
  - סרטן
  - כימותרפיה
  - אבולוציה
  - עמידות לתרופות
  - ביולוגיה של הסרטן
---
# הקרב על הגידול: סימולטור עמידות סרטנית לכימותרפיה

טיפול כימותרפי הוא כלי רב עוצמה במאבק נגד סרטן, אך לעיתים קרובות אנו עדים לתופעה מדאיגה: הגידול חוזר, ולפעמים הוא כבר לא מגיב לאותו טיפול שהיה יעיל בעבר. איך תאי סרטן מצליחים לחמוק ממוות ולהפוך ל"עמידים" לתרופות? האם זו מזל רע או תהליך ביולוגי שניתן לחזות? הצטרפו אלינו למסע אינטראקטיבי אל תוך הגידול עצמו, כדי לגלות את סודות ההתפתחות של עמידות סרטנית.

<div id="simulator-app">
  <h2>חקור בעצמך: איך מתפתחת עמידות?</h2>
  <div class="controls">
    <div class="controls-section">
      <h3>הגדרות הגידול:</h3>
      <label for="initial-size">מספר תאים התחלתי בגידול:</label>
      <input type="number" id="initial-size" value="1000" min="100" step="100"><br>

      <label for="initial-resistant-percent">אחוז התאים העמידים מלכתחילה:</label>
      <input type="range" id="initial-resistant-percent" value="1" min="0" max="10" step="0.1" oninput="this.nextElementSibling.value=this.value"><output>1</output>%<br>

      <label for="mutation-rate">שכיחות מוטציות (רגיש -> עמיד):</label>
      <input type="range" id="mutation-rate" value="0.1" min="0" max="1" step="0.01" oninput="this.nextElementSibling.value=this.value"><output>0.1</output>%<br>

      <label for="growth-rate">קצב התרבות הגידול (ללא טיפול):</label>
      <input type="range" id="growth-rate" value="1.8" min="1.1" max="3" step="0.1" oninput="this.nextElementSibling.value=this.value"><output>1.8</output>x<br>
    </div>
    <div class="controls-section">
      <h3>הגדרות הטיפול:</h3>
      <label for="treatment-effectiveness">כמה תאים רגישים הטיפול מחסל:</label>
      <input type="range" id="treatment-effectiveness" value="80" min="10" max="100" step="1" oninput="this.nextElementSibling.value=this.value"><output>80</output>%<br>

      <label for="treatment-frequency">כל כמה מחזורים הטיפול ניתן:</label>
      <input type="number" id="treatment-frequency" value="3" min="1" max="10"><br>
       <div class="spacer"></div> <!-- To align columns -->
       <div class="spacer"></div>
    </div>
  </div>

  <div class="action-buttons">
    <button id="start-simulation">הפעל סימולציה</button>
    <button id="reset-simulation" disabled>אפס סימולציה</button>
  </div>


  <div class="simulation-output">
    <h3>תוצאות בזמן אמת:</h3>
    <div class="status-bar">
        <p>מחזור נוכחי: <span id="current-cycle">0</span></p>
         <p>מצב: <span id="simulation-status">מוכן</span></p>
    </div>


    <div class="cell-counts-display">
        <div class="count-box total">
            <h4>סה"כ תאים</h4>
            <p id="total-cells">0</p>
        </div>
         <div class="count-box sensitive">
            <h4>תאים רגישים</h4>
            <p id="sensitive-cells">0</p>
        </div>
         <div class="count-box resistant">
            <h4>תאים עמידים</h4>
            <p id="resistant-cells">0</p>
        </div>
    </div>


    <div id="cell-counts-graph">
        <!-- Visual representation -->
        <div id="sensitive-bar" class="cell-bar sensitive"></div>
        <div id="resistant-bar" class="cell-bar resistant"></div>
    </div>

     <div id="simulation-log"></div>
  </div>
</div>

<button id="toggle-explanation">מה קורה כאן? הסבר מפורט</button>

<div id="explanation" style="display: none;">
  <h2>הסבר מדעי: אבולוציה וברירה טבעית בגידול סרטני</h2>
  <p>כדי להבין מדוע טיפולים בסרטן לפעמים נכשלים, עלינו להסתכל על הגידול הסרטני לא רק כאוסף אקראי של תאים חולים, אלא כאוכלוסייה דינמית הנתונה לחוקי האבולוציה.</p>

  <h3>גידול סרטני: לא מושבה של תאים זהים</h3>
  <p>בניגוד לדעה הרווחת, גידול סרטני אינו מורכב מתאים זהים לחלוטין. תאי הסרטן מתחלקים במהירות, ותהליך זה מועד לשגיאות - מוטציות גנטיות. מוטציות אלו מצטברות ויוצרות שונות גנטית גדולה בין התאים בתוך אותו גידול. חלק מהתאים עשויים להיות אגרסיביים יותר, אחרים פחות, וחלקם עשויים לרכוש תכונות המשפיעות על רגישותם לטיפולים תרופתיים.</p>

  <h3>כימותרפיה: מכשיר הברירה הטבעית</h3>
  <p>תרופות כימותרפיות מסורתיות פועלות לרוב על ידי פגיעה בתאים המתחלקים במהירות. הן גורמות לנזק בדנ"א או מפריעות לתהליכים חיוניים לחלוקת התא. הבעיה היא שהן אינן מזהות רק תאי סרטן; הן פוגעות גם בתאים בריאים שמתחלקים במהירות (כמו תאי שיער, תאי מערכת העיכול ותאי מח עצם - ומכאן תופעות הלוואי הידועות).</p>
  <p>אבל ההשפעה המשמעותית ביותר של הכימותרפיה על הגידול היא פעולתה כ"כוח סלקטיבי" - היא מחסלת את התאים הרגישים אליה. אם בגידול קיימים מלכתחילה (גם אם באחוז קטן מאוד) תאים בעלי מוטציה אקראית המקנה להם עמידות מסוימת לתרופה (למשל, מוטציה שמשפיעה על אופן כניסת התרופה לתא, על מנגנוני תיקון הדנ"א שלהם, או על מסלולים מטאבוליים שהתרופה מנסה לחסום), תאים אלו שורדים טוב יותר את הטיפול.</p>

  <h3>התמונה האבולוציונית</h3>
  <p>התפתחות עמידות לתרופות היא דוגמה קלאסית לתהליך של ברירה טבעית, כפי שתואר על ידי דרווין, רק בקנה מידה מהיר וברמת תאי הגוף:</p>
  <ul>
    <li>**שונות (Variation):** בתוך אוכלוסיית תאי הגידול קיימת שונות תורשתית (גנטית) בין תאים, שנוצרת בזכות המוטציות הרבות המתרחשות.</li>
    <li>**תורשה (Inheritance):** תכונות אלו, כולל רגישות או עמידות לתרופה, עוברות בתורשה לתאי הבת במהלך החלוקה.</li>
    <li>**ברירה (Selection):** הטיפול התרופתי מהווה לחץ סלקטיבי. הוא "בורר" לטובה את התאים העמידים, ששורדים וממשיכים להתרבות, בעוד התאים הרגישים מתים.</li>
  </ul>

  <h3>מרוץ החימוש של הכימותרפיה והגידול</h3>
  <p>עם כל מחזור טיפולי, אוכלוסיית התאים בגידול משתנה. אחוז התאים הרגישים קטן באופן דרמטי, בעוד שאחוז התאים העמידים גדל יחסית (וגם אבסולוטית, כיוון שהם ממשיכים להתחלק ללא תחרות רבה). בהדרגה, הגידול הופך להיות "מועשר" בתאים עמידים. בסופו של דבר, רוב הגידול יהיה מורכב מתאים עמידים, והטיפול הספציפי יהפוך ללא יעיל - זוהי העמידות הקלינית.</p>

  <h3>למה הסימולטור רלוונטי?</h3>
  <p>הסימולטור מדגים כיצד גורמים כמו קצב הגידול המקורי, שכיחות המוטציות שיוצרות עמידות, האם היו תאים עמידים מלכתחילה וכמה (גם אחוז קטן מאוד יכול להיות קריטי!), ויעילות ותדירות הטיפול - כולם משפיעים יחד על המהירות בה תתפתח עמידות ועל הצלחת הטיפול בטווח הארוך. שחקו עם ההגדרות כדי לראות כיצד שינויים קטנים בנקודת המוצא יכולים להוביל לתוצאות שונות לחלוטין.</p>
</div>

<style>
  #simulator-app {
    font-family: 'Arial', sans-serif;
    max-width: 800px;
    margin: 20px auto;
    padding: 30px;
    border: 1px solid #dcdcdc;
    border-radius: 12px;
    background-color: #ffffff;
    direction: rtl;
    text-align: right;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    color: #333;
  }

  #simulator-app h2 {
    text-align: center;
    color: #2c3e50;
    margin-bottom: 25px;
    font-size: 1.8em;
  }

  .controls {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
    flex-wrap: wrap;
    gap: 20px; /* Add gap between sections */
  }

  .controls-section {
      border: 1px solid #eee;
      padding: 20px;
      border-radius: 8px;
      flex: 1;
      min-width: 300px; /* Ensure sections don't get too squished */
      background-color: #fdfdfd;
      box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
  }

   .controls-section h3 {
       margin-top: 0;
       color: #34495e;
       text-align: center;
       margin-bottom: 15px;
       font-size: 1.3em;
   }

  .controls label {
    display: block; /* Use block for better layout with ranges */
    margin-bottom: 8px;
    font-weight: bold;
    color: #555;
    font-size: 0.95em;
  }

  .controls input[type="number"],
  .controls input[type="range"] {
    width: calc(100% - 70px); /* Adjust width */
    padding: 8px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box; /* Include padding and border in element's total width */
    vertical-align: middle;
  }

  .controls input[type="range"] {
      padding: 0; /* Range inputs style differently */
      height: 34px; /* Match number input height */
      margin-bottom: 5px; /* Less space below range */
  }

   .controls output {
       display: inline-block;
       width: 50px; /* Fixed width for output */
       text-align: left; /* Align value to the left */
       font-weight: bold;
       color: #0077B6; /* Highlight value */
        vertical-align: middle;
   }

   .spacer {
       height: 20px; /* Used to push controls in one column down */
   }


  .action-buttons {
    text-align: center;
    margin-bottom: 30px;
  }

  button {
    padding: 12px 20px;
    margin: 0 10px;
    background-color: #3498db; /* Blue */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, opacity 0.3s ease;
  }

  button:disabled {
      background-color: #cccccc;
      cursor: not-allowed;
      opacity: 0.6;
  }

  button:hover:enabled {
    background-color: #2980b9; /* Darker blue */
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }

  #toggle-explanation {
      display: block; /* Make it a block element */
      width: fit-content; /* Adjust width to content */
      margin: 25px auto; /* Center the button with more space */
      background-color: #16a085; /* Greenish-blue */
  }

  #toggle-explanation:hover:enabled {
      background-color: #1abc9c; /* Lighter greenish-blue */
  }


  .simulation-output {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #ecf0f1; /* Light gray background */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }

  .simulation-output h3 {
      margin-top: 0;
      color: #2c3e50;
      text-align: center;
      margin-bottom: 20px;
      font-size: 1.5em;
  }

  .status-bar {
      display: flex;
      justify-content: space-around;
      margin-bottom: 15px;
      font-size: 1.1em;
      font-weight: bold;
      color: #555;
  }

  .status-bar span {
      color: #0077B6; /* Highlight status text */
  }


  .cell-counts-display {
      display: flex;
      justify-content: space-around;
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 15px;
  }

  .count-box {
      text-align: center;
      padding: 15px;
      border-radius: 8px;
      background-color: #fff;
      box-shadow: 0 1px 4px rgba(0,0,0,0.05);
      flex: 1;
      min-width: 150px;
  }

  .count-box h4 {
      margin-top: 0;
      margin-bottom: 5px;
      color: #333;
      font-size: 1em;
  }

   .count-box p {
       margin: 0;
       font-size: 1.4em;
       font-weight: bold;
   }

   .count-box.total p { color: #2c3e50; }
   .count-box.sensitive p { color: #e74c3c; } /* Red */
   .count-box.resistant p { color: #2ecc71; } /* Green */


  #cell-counts-graph {
    width: 100%;
    height: 40px; /* Increased height for better visibility */
    background-color: #dcdcdc;
    margin-top: 15px;
    display: flex;
    border-radius: 6px;
    overflow: hidden; /* Hide overflow during transitions/updates */
    position: relative; /* Needed for absolute positioning of labels */
  }

   #cell-counts-graph::before {
       content: 'רגישים';
       position: absolute;
       top: 50%;
       left: 10px;
       transform: translateY(-50%);
       color: white;
       font-weight: bold;
       font-size: 0.9em;
       z-index: 1; /* Ensure text is above bars */
       text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
       pointer-events: none; /* Allow clicks to pass through text to bar */
   }

    #cell-counts-graph::after {
       content: 'עמידים';
       position: absolute;
       top: 50%;
       right: 10px;
       transform: translateY(-50%);
       color: white;
       font-weight: bold;
        font-size: 0.9em;
       z-index: 1;
       text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        pointer-events: none;
   }


  .cell-bar {
    height: 100%;
    transition: width 0.8s ease-in-out; /* Smooth transition */
    position: relative; /* For potential future labels */
    box-sizing: border-box; /* Include border/padding in size */
    border-left: 1px solid rgba(0,0,0,0.1); /* Separator */
  }

  .sensitive {
    background: linear-gradient(to right, #e74c3c, #c0392b); /* Red gradient */
  }

  .resistant {
    background: linear-gradient(to left, #2ecc71, #27ae60); /* Green gradient */
  }

   .treatment-animation {
       animation: pulse-bar 0.5s ease-out 2; /* Pulse red bar when treated */
   }

   @keyframes pulse-bar {
       0% { transform: scaleY(1); }
       50% { transform: scaleY(0.9); }
       100% { transform: scaleY(1); }
   }


  #simulation-log {
      margin-top: 20px;
      padding: 15px;
      border: 1px solid #ccc;
      max-height: 150px; /* Slightly smaller log */
      overflow-y: auto;
      font-size: 0.9em;
      background-color: #f8f9f9; /* Lighter background */
      border-radius: 5px;
      line-height: 1.5;
      white-space: pre-wrap; /* Handle long messages */
      word-wrap: break-word;
  }

  #simulation-log p {
      margin: 5px 0;
      padding-bottom: 5px;
      border-bottom: 1px dotted #eee;
  }

  #simulation-log p:last-child {
      border-bottom: none;
  }

  #simulation-log p:nth-child(odd) {
      background-color: #f4f5f6; /* Zebra striping */
  }


  #explanation {
    max-width: 800px;
    margin: 20px auto;
    padding: 30px;
    border: 1px solid #dcdcdc;
    border-radius: 12px;
    background-color: #ffffff;
    direction: rtl;
    text-align: right;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    color: #333;
  }

  #explanation h2, #explanation h3 {
      text-align: center;
      color: #2c3e50;
      margin-bottom: 15px;
  }

    #explanation h2 {
        margin-top: 0;
        font-size: 1.8em;
    }
     #explanation h3 {
        font-size: 1.4em;
        color: #34495e;
        margin-top: 25px;
     }


  #explanation p {
      margin-bottom: 15px;
      line-height: 1.6;
      font-size: 1.05em;
  }

  #explanation ul {
      list-style-type: disc;
      margin-right: 25px; /* Hebrew list indentation */
      padding-right: 0; /* Remove default left padding */
      margin-bottom: 15px;
  }

   #explanation li {
       margin-bottom: 8px;
       line-height: 1.5;
   }

</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const initialSizeInput = document.getElementById('initial-size');
    const initialResistantPercentInput = document.getElementById('initial-resistant-percent');
    const mutationRateInput = document.getElementById('mutation-rate');
    const treatmentEffectivenessInput = document.getElementById('treatment-effectiveness');
    const treatmentFrequencyInput = document.getElementById('treatment-frequency');
    const growthRateInput = document.getElementById('growth-rate');

    const startButton = document.getElementById('start-simulation');
    const resetButton = document.getElementById('reset-simulation');

    const currentCycleSpan = document.getElementById('current-cycle');
    const simulationStatusSpan = document.getElementById('simulation-status');
    const totalCellsSpan = document.getElementById('total-cells');
    const sensitiveCellsSpan = document.getElementById('sensitive-cells');
    const resistantCellsSpan = document.getElementById('resistant-cells');
    const sensitiveBar = document.getElementById('sensitive-bar');
    const resistantBar = document.getElementById('resistant-bar');
    const simulationLogDiv = document.getElementById('simulation-log');

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    let simulationInterval = null;
    let currentCycle = 0;
    let sensitiveCells = 0;
    let resistantCells = 0;

    // Helper to format numbers nicely
    function formatNumber(num) {
        if (num === 0) return '0';
        if (Math.abs(num) < 1) return num.toFixed(2); // Show decimals for small numbers
        if (num < 1000) return Math.round(num).toLocaleString();
        if (num < 1000000) return (num / 1000).toFixed(1) + 'K';
        if (num < 1000000000) return (num / 1000000).toFixed(1) + 'M';
        return (num / 1000000000).toFixed(1) + 'B';
    }


    function logMessage(message, type = 'info') {
        const p = document.createElement('p');
        p.textContent = `[מחזור ${currentCycle}] ${message}`;
        // Add simple styling based on type
        if(type === 'treatment') p.style.color = '#c0392b'; // Red for treatment
        if(type === 'mutation') p.style.color = '#8e44ad'; // Purple for mutation
        if(type === 'status') p.style.fontWeight = 'bold'; // Bold for status changes


        simulationLogDiv.appendChild(p);
        simulationLogDiv.scrollTop = simulationLogDiv.scrollHeight; // Auto-scroll
    }

     function updateStatus(statusText, color = '#0077B6') {
         simulationStatusSpan.textContent = statusText;
         simulationStatusSpan.style.color = color;
     }


    function updateDisplay() {
      currentCycleSpan.textContent = currentCycle;
      const total = sensitiveCells + resistantCells;
      totalCellsSpan.textContent = formatNumber(total);
      sensitiveCellsSpan.textContent = formatNumber(sensitiveCells);
      resistantCellsSpan.textContent = formatNumber(resistantCells);

      // Use the initial size for the bar scale reference in early cycles, or a dynamic max
      // Let's use the maximum number of cells encountered so far to scale
      // This prevents bars from shrinking to nothing if total cells decrease significantly
      const maxCellsSeen = Math.max(parseFloat(totalCellsSpan.dataset.maxCells || 0), total, parseInt(initialSizeInput.value) * 5); // Use initial size * multiplier or peak
      totalCellsSpan.dataset.maxCells = maxCellsSeen; // Store max for next cycle

      const totalForBars = Math.max(maxCellsSeen, 1); // Scale bars relative to peak or initial*5
      const sensitiveWidth = (sensitiveCells / totalForBars) * 100;
      const resistantWidth = (resistantCells / totalForBars) * 100;

      // Ensure widths are not negative and add up to 100% if total > 0
      const totalVisible = sensitiveCells + resistantCells;
       if (totalVisible <= 0) {
           sensitiveBar.style.width = '0%';
           resistantBar.style.width = '0%';
       } else {
            sensitiveBar.style.width = `${(sensitiveCells / totalVisible) * 100}%`;
            resistantBar.style.width = `${(resistantCells / totalVisible) * 100}%`;
            // Adjust actual bar size based on total vs max seen
            const totalBarWidth = Math.min(100, (totalVisible / maxCellsSeen) * 100);
             document.getElementById('cell-counts-graph').style.width = `${totalBarWidth}%`;
             document.getElementById('cell-counts-graph').style.margin = '15px auto'; // Center the bar
             document.getElementById('cell-counts-graph').style.backgroundColor = '#eee'; // Reset background
       }


      sensitiveBar.title = `רגישים: ${formatNumber(sensitiveCells)}`;
      resistantBar.title = `עמידים: ${formatNumber(resistantCells)}`;

       // Update bar labels (if visible and space allows)
       const graphElement = document.getElementById('cell-counts-graph');
        if (sensitiveCells / totalVisible > 0.1) { // Only show if bar is wide enough
             graphElement.setAttribute('data-sensitive-label', 'רגישים');
        } else {
             graphElement.removeAttribute('data-sensitive-label');
        }
        if (resistantCells / totalVisible > 0.1) { // Only show if bar is wide enough
             graphElement.setAttribute('data-resistant-label', 'עמידים');
        } else {
             graphElement.removeAttribute('data-resistant-label');
        }
    }


    function startSimulation() {
      const initialSize = parseInt(initialSizeInput.value);
      const initialResistantPercent = parseFloat(initialResistantPercentInput.value) / 100;
      const mutationRate = parseFloat(mutationRateInput.value) / 10000; // Mutation rate is per 10,000 cells in original text? Let's check. Ah, no, percent. 0.1% = 0.001. Let's keep it as % input, but use value/100.
       const inputMutationRate = parseFloat(mutationRateInput.value);
       const mutationRateDecimal = inputMutationRate / 100; // Convert input percentage to decimal

      const treatmentEffectiveness = parseFloat(treatmentEffectivenessInput.value) / 100;
      const treatmentFrequency = parseInt(treatmentFrequencyInput.value);
      const growthRate = parseFloat(growthRateInput.value);

      if (isNaN(initialSize) || initialSize <= 0 ||
          isNaN(initialResistantPercent) || initialResistantPercent < 0 || initialResistantPercent > 1 ||
          isNaN(mutationRateDecimal) || mutationRateDecimal < 0 || mutationRateDecimal > 1 ||
          isNaN(treatmentEffectiveness) || treatmentEffectiveness < 0 || treatmentEffectiveness > 1 ||
          isNaN(treatmentFrequency) || treatmentFrequency <= 0 ||
           isNaN(growthRate) || growthRate < 1) {
            alert("אנא הכנס ערכים חוקיים להגדרות הסימולציה.");
            return;
      }

      currentCycle = 0;
      resistantCells = Math.round(initialSize * initialResistantPercent);
      sensitiveCells = initialSize - resistantCells;
      simulationLogDiv.innerHTML = ''; // Clear log
      totalCellsSpan.dataset.maxCells = initialSize * 5; // Initialize max cells seen for bar scaling

      logMessage(`--- התחלת הסימולציה! ---`, 'status');
      logMessage(`הגדרות: גידול התחלתי: ${initialSize} תאים (${Math.round(initialResistantPercent*100)}% עמידים). קצב מוטציה: ${inputMutationRate}%, קצב גידול: x${growthRate}. טיפול: יעילות ${treatmentEffectiveness*100}%, תדירות כל ${treatmentFrequency} מחזורים.`);
      logMessage(`מחזור 0: סה"כ: ${formatNumber(initialSize)}, רגישים: ${formatNumber(sensitiveCells)}, עמידים: ${formatNumber(resistantCells)}`);

      updateDisplay();
      updateStatus("פועל...");

      startButton.disabled = true;
      resetButton.disabled = false;
      disableInputs(true);

      simulationInterval = setInterval(() => {
        currentCycle++;

        // 1. Growth Phase
        const prevTotal = sensitiveCells + resistantCells;
        sensitiveCells *= growthRate;
        resistantCells *= growthRate;
         if (currentCycle <= 1) { // Log initial growth rate explicitly only once
             logMessage(`מחזור ${currentCycle}: הגידול מתרבה (x${growthRate}). סה"כ תאים עכשיו: ${formatNumber(sensitiveCells + resistantCells)}.`);
         } else {
              logMessage(`מחזור ${currentCycle}: הגידול מתרבה. סה"כ תאים עכשיו: ${formatNumber(sensitiveCells + resistantCells)}.`);
         }


        // 2. Mutation (Sensitive -> Resistant)
         // Calculate mutations based on current sensitive population BEFORE treatment
        const newResistantFromMutation = sensitiveCells * mutationRateDecimal;
        sensitiveCells -= newResistantFromMutation;
        resistantCells += newResistantFromMutation;
         if (newResistantFromMutation >= 1) { // Only log if at least one cell mutated
             logMessage(`   - ${Math.round(newResistantFromMutation)} תאים רגישים צברו מוטציה והפכו לעמידים.`, 'mutation');
         }


        // 3. Treatment Phase (if scheduled)
        if (currentCycle % treatmentFrequency === 0) {
          const killedSensitive = sensitiveCells * treatmentEffectiveness;
          sensitiveCells -= killedSensitive;
           sensitiveBar.classList.add('treatment-animation'); // Add animation class
            setTimeout(() => { sensitiveBar.classList.remove('treatment-animation'); }, 1000); // Remove after animation


           if (killedSensitive >= 1) {
              logMessage(`   - בוצע טיפול כימותרפי! נהרגו כ-${formatNumber(killedSensitive)} תאים רגישים.`, 'treatment');
           } else {
              logMessage(`   - בוצע טיפול כימותרפי, אך כמעט לא נותרו תאים רגישים להרוג.`, 'treatment');
           }
        }


        // Ensure no negative cells due to floating point issues and round to whole cells
        sensitiveCells = Math.max(0, Math.round(sensitiveCells));
        resistantCells = Math.max(0, Math.round(resistantCells));

        updateDisplay();

        // Check stopping conditions
        const total = sensitiveCells + resistantCells;
        const maxCells = 50000000; // Stop simulation if too large (increased limit)
        const maxCycles = 150; // Stop simulation after a reasonable number of cycles (increased limit)
        const eradicationThreshold = 50; // Consider eradicated if total cells below this

        if (total > maxCells) {
          logMessage(`--- סיום סימולציה: הגידול גדל מעבר למגבלה (${formatNumber(maxCells)} תאים). ככל הנראה, עמידות השתלטה. ---`, 'status');
          updateStatus("עמידות השתלטה", '#e74c3c'); // Red status
          stopSimulation();
        } else if (currentCycle >= maxCycles) {
           logMessage(`--- סיום סימולציה: הגיעה למספר מחזורים מקסימלי (${maxCycles}). ---`, 'status');
           updateStatus("הסתיימו המחזורים", '#f39c12'); // Orange status
           stopSimulation();
        } else if (total <= eradicationThreshold && sensitiveCells + resistantCells > 0) {
             logMessage(`--- סיום סימולציה: הגידול הצטמצם משמעותית, אך נותרו ${formatNumber(total)} תאים. דרוש מעקב או טיפול נוסף. ---`, 'status');
             updateStatus("הגידול הצטמצם", '#f39c12'); // Orange status
             stopSimulation();
        }
         else if (total <= 0) {
           logMessage(`--- סיום סימולציה: הטיפול הצליח! הגידול הושמד לחלוטין. ---`, 'status');
            updateStatus("הושמד בהצלחה!", '#2ecc71'); // Green status
           stopSimulation();
        }


      }, 800); // Simulate one cycle slightly faster
    }

    function stopSimulation() {
      clearInterval(simulationInterval);
      simulationInterval = null;
      startButton.disabled = false;
      resetButton.disabled = false;
      disableInputs(false);
    }

    function resetSimulation() {
        stopSimulation();
        currentCycle = 0;
        sensitiveCells = 0;
        resistantCells = 0;
        simulationLogDiv.innerHTML = '';
        totalCellsSpan.dataset.maxCells = '0'; // Reset max cells seen
        document.getElementById('cell-counts-graph').style.width = '100%'; // Reset bar width
        document.getElementById('cell-counts-graph').style.margin = '15px 0'; // Reset bar centering
         document.getElementById('cell-counts-graph').removeAttribute('data-sensitive-label');
         document.getElementById('cell-counts-graph').removeAttribute('data-resistant-label');

        updateDisplay();
        startButton.disabled = false;
        resetButton.disabled = true;
        disableInputs(false);
        updateStatus("מוכן", '#0077B6');
        logMessage(`--- הסימולציה אופסה ---`, 'status');
    }

    function disableInputs(disable) {
        const inputs = [
            initialSizeInput,
            initialResistantPercentInput,
            mutationRateInput,
            treatmentEffectivenessInput,
            treatmentFrequencyInput,
            growthRateInput
        ];
        inputs.forEach(input => input.disabled = disable);
    }


    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
      const isHidden = explanationDiv.style.display === 'none';
      explanationDiv.style.display = isHidden ? 'block' : 'none';
      toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'מה קורה כאן? הסבר מפורט';
    });

    // Add event listeners to range inputs to update output display
    document.querySelectorAll('input[type="range"]').forEach(input => {
        input.addEventListener('input', () => {
            const output = input.nextElementSibling; // Assumes output is right after input
            if (output && output.tagName === 'OUTPUT') {
                 output.value = input.value;
            }
        });
    });


    // Initial display update
    resetSimulation(); // Use reset to initialize state and display
  });
</script>