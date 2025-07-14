---
title: "קוד ויזואלי: עקרונות הגשטאלט בחוויה אינטראקטיבית"
english_slug: gestalt-principles-in-action-proximity-similarity-closure
category: "מדעי החברה / פסיכולוגיה"
tags:
  - גשטאלט
  - תפיסה חזותית
  - פסיכולוגיה קוגניטיבית
  - עיצוב גרפי
  - UX
---
# קוד ויזואלי: עקרונות הגשטאלט בפעולה

האם אי פעם עצרת לחשוב למה המוח שלך מקבץ אוטומטית צורות או משלים קווים חסרים? תפיסה חזותית היא לא רק ראייה פסיבית, אלא תהליך פעיל של ארגון ופירוש. עקרונות הגשטאלט הם כללי האצבע הפסיכולוגיים שהמוח שלנו מפעיל כדי ליצור סדר מתוך כאוס ויזואלי. צלול למעבדה הווירטואלית שלנו, שחק עם האלמנטים וגלה ממקור ראשון איך שינויים קטנים משנים לגמרי את מה שאתה תופס!

<div class="gestalt-app-container">
  <canvas id="gestaltCanvas" width="600" height="400"></canvas>
  <div class="controls">
    <h3>שחק עם עקרונות הגשטאלט:</h3>

    <div class="control-section" id="proximity-controls">
      <h4>קירבה (Proximity)</h4>
      <p>שנה את המרווחים וראה איך המוח שלך יוצר קבוצות מאלמנטים קרובים.</p>
      <div class="button-group">
        <button id="proximityGroupRowsBtn">קבץ שורות</button>
        <button id="proximityGroupColsBtn">קבץ עמודות</button>
        <button id="proximityUniformBtn">מרווח אחיד</button>
      </div>
    </div>

    <div class="control-section" id="similarity-controls">
      <h4>דמיון (Similarity)</h4>
      <p>שנה צבעים או צורות וגלה איך המוח מקבץ אלמנטים דומים.</p>
       <div class="button-group">
        <button id="similarityColorBtn">צבע לסירוגין</button>
        <button id="similarityShapeBtn">צורה לסירוגין</button>
        <button id="similarityUniformBtn">אחיד</button>
       </div>
    </div>

    <div class="control-section" id="closure-controls">
      <h4>סגירות (Closure)</h4>
      <p>המוח שלך משלים אוטומטית צורות חלקיות. בחר צורה וקבע את גודל הפער.</p>
      <div class="closure-controls-flex">
        <label for="closureShapeSelect">צורה:</label>
        <select id="closureShapeSelect">
          <option value="square">ריבוע</option>
          <option value="circle">עיגול</option>
          <option value="triangle">משולש</option>
        </select>
      </div>
      <div class="closure-controls-flex">
        <label for="closureGapSlider">גודל הפער:</label>
        <input type="range" id="closureGapSlider" min="0" max="80" value="30">
        <span id="closureGapValue">30%</span>
      </div>
      <div class="button-group">
         <button id="closureToggleCompleteBtn">הצג/הסתר צורה שלמה</button>
      </div>
    </div>
      <button id="resetAppBtn">איפוס הכל</button>
  </div>
</div>

<button id="toggleExplanationBtn" class="toggle-button">רוצה להבין את הקסם? הקלק להסבר מורחב!</button>

<div id="explanation" class="hidden">
  <h2>הצצה עמוקה: עקרונות הגשטאלט בפעולה</h2>

  <h3>מה זה בכלל גשטאלט?</h3>
  <p>פסיכולוגיית הגשטאלט, שנולדה בגרמניה בתחילת המאה ה-20, שינתה את האופן שבו אנו מבינים תפיסה. במקום לראות את העולם כאוסף של גירויים בודדים, הגשטאלט טוען שהמוח שלנו מארגן אותם באופן אקטיבי לתבניות, צורות ושלמים בעלי משמעות. הרעיון המרכזי: "השלם גדול מסכום חלקיו". האופן שבו האלמנטים מסודרים יחד חשוב לא פחות (ואף יותר) מהאלמנטים עצמם. ההתנסות האינטראקטיבית שלמעלה נותנת לך כוח לשחק עם שלושה מעקרונות הארגון החזותי החשובים ביותר:</p>

  <h3>1. עקרון הקירבה (Proximity)</h3>
  <p>זה פשוט כמו שזה נשמע: דברים קרובים נתפסים כקבוצה אחת. גם אם כל הנקודות שראית בהתנסות היו זהות לחלוטין, שינוי המרחק ביניהן גרם למוח שלך לראות מיד שורות או עמודות. זה עיקרון בסיסי, אבל סופר עוצמתי בארגון ויזואלי, מקבוצות אייקונים ועד פסקאות טקסט.</p>

  <h3>2. עקרון הדמיון (Similarity)</h3>
  <p>כשאובייקטים חולקים מאפיין משותף – צבע, צורה, גודל, מרקם – המוח מקבץ אותם יחד, גם אם הם לא קרובים פיזית. בהתנסות, ראית איך שינוי צבע או צורה של חלק מהנקודות יצר באופן מיידי חלוקה לקבוצות שונות. דמיון הוא כלי מפתח ליצירת היררכיה ויזואלית והפרדה בין קבוצות מידע.</p>

  <h3>3. עקרון הסגירות (Closure)</h3>
  <p>המוח שלנו שונא אי-ודאות ונוטה להשלים מידע חסר כדי ליצור תמונה שלמה ומוכרת. זה עיקרון הסגירות בפעולה. גם כשהצגה לך צורה עם פערים גדולים, המוח שלך "מילא" אוטומטית את החסר וזיהה ריבוע, עיגול או משולש. הצגת הצורה המלאה רק אישרה את מה שהמוח כבר תפס. זה מה שמאפשר לנו לזהות לוגואים או אייקונים גם כשהם מופשטים או חלקיים.</p>

  <h3>לא רק בנפרד: כוחם המשולב</h3>
  <p>חשוב לזכור שעקרונות הגשטאלט לא תמיד פועלים בוואקום. הם יכולים להתחרות, לחזק זה את זה, וליצור תפיסות מורכבות. לדוגמה, אם יש לך נקודות קרובות (קירבה) אבל חלקן כחולות וחלקן אדומות (דמיון), האופן שבו תתפוס אותן יהיה שילוב של שני העקרונות, בהתאם לעוצמת כל אחד מהם בסידור הספציפי.</p>

  <h3>למה זה חשוב? יישומים בעולם האמיתי</h3>
  <p>הבנת עקרונות הגשטאלט היא כלי קריטי לכל מי שעוסק בתקשורת חזותית:</p>
  <ul>
    <li>**עיצוב גרפי:** ליצירת קומפוזיציות ברורות, קריאות, ולוגואים זכירים.</li>
    <li>**עיצוב ממשקי משתמש (UI/UX):** לארגון אלמנטים במסך (כפתורים, תפריטים, טפסים) באופן אינטואיטיבי, יצירת היררכיה ברורה והנחיית המשתמש.</li>
    <li>**שיווק ופרסום:** ליצירת מודעות ואריזות שמושכות את העין ומעבירות את המסר ביעילות.</li>
    <li>**אמנות:** לפיסול התפיסה של הצופה ויצירת עניין חזותי.</li>
  </ul>
  <p>הבנת עקרונות אלו מאפשרת לנו לעצב לא רק דברים שנראים טוב, אלא דברים ש"עובדים" עם המוח שלנו באופן טבעי.</p>
</div>

<style>
  :root {
    --primary-color: #5e35b1; /* Deep purple */
    --secondary-color: #7e57c2; /* Medium purple */
    --accent-color: #ffca28; /* Amber */
    --background-light: #f3e5f5; /* Light purple background */
    --surface-color: #ffffff; /* White cards */
    --text-color: #212121; /* Dark grey */
    --text-secondary: #757575; /* Medium grey */
    --border-color: #e0e0e0; /* Light grey border */
    --error-color: #ef5350; /* Red for reset */
    --border-radius: 8px;
    --padding-base: 15px;
    --margin-base: 20px;
    --transition-speed: 0.3s;
  }

  body {
      font-family: 'Arial', sans-serif;
      line-height: 1.6;
      color: var(--text-color);
      background-color: var(--background-light);
      padding: 0 var(--padding-base); /* Add some padding on sides */
  }

  h1, h2, h3, h4 {
      color: var(--primary-color);
      margin-bottom: var(--padding-base);
  }

  p {
      margin-bottom: var(--padding-base);
  }

  .gestalt-app-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: var(--margin-base) auto; /* Center block */
    padding: var(--padding-base) * 1.5;
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    background-color: var(--surface-color);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    max-width: 800px; /* Limit max width */
  }

  #gestaltCanvas {
    border: 1px solid var(--border-color);
    background-color: #fff;
    margin-bottom: var(--padding-base) * 1.5;
    max-width: 100%;
    height: auto; /* Maintain aspect ratio */
    border-radius: 4px;
     box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
  }

  .controls {
    width: 100%;
    max-width: 600px; /* Controls max width */
  }

  .controls h3 {
      text-align: center;
      margin-bottom: var(--padding-base);
      color: var(--secondary-color);
  }

  .control-section {
    margin-bottom: var(--margin-base);
    padding: var(--padding-base);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius) - 4px; /* Slightly smaller radius */
    background-color: #f9f9f9; /* Lighter background for sections */
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
  }

  .control-section h4 {
      text-align: center;
      margin-top: 0;
      margin-bottom: var(--padding-base) / 2;
      color: var(--primary-color);
  }

  .control-section p {
      text-align: center;
      margin-top: 0;
      margin-bottom: var(--padding-base);
      font-size: 0.95em;
      color: var(--text-secondary);
  }

  .button-group {
      display: flex;
      flex-wrap: wrap; /* Allow wrapping on small screens */
      justify-content: center;
      gap: 10px; /* Space between buttons */
      margin-top: var(--padding-base) / 2;
  }

  .control-section button,
  .control-section select {
    padding: 10px 18px;
    border: none; /* Remove default border */
    border-radius: 4px;
    background-color: var(--secondary-color);
    color: white;
    cursor: pointer;
    font-size: 1em;
    transition: background-color var(--transition-speed) ease, transform 0.1s ease;
    text-align: center;
    flex-grow: 1; /* Allow buttons to grow */
    max-width: 180px; /* Limit max width */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
   .control-section select {
       flex-grow: 0; /* Prevent select from growing */
       max-width: none; /* Allow select to take natural width */
       background-color: #eee; /* Different background for select */
       color: var(--text-color);
       border: 1px solid var(--border-color);
   }

  .control-section button:hover {
      background-color: #673ab7; /* Darker purple */
       box-shadow: 0 4px 8px rgba(0,0,0,0.15);
  }
  .control-section button:active {
      transform: scale(0.98); /* Visual feedback on click */
  }

  .control-section label {
      margin-right: 10px;
      font-weight: bold;
      color: var(--text-color);
      flex-shrink: 0; /* Prevent shrinking */
  }

  .closure-controls-flex { /* Wrapper for slider and value */
      display: flex;
      align-items: center;
      justify-content: center; /* Center horizontally */
      width: 100%;
      margin-bottom: var(--padding-base) / 2;
  }

  .closure-controls-flex input[type="range"] {
      flex-grow: 1; /* Slider takes available space */
      margin: 0 10px;
      padding: 0; /* Remove range padding */
      height: 8px; /* Make slider thinner */
      background: var(--border-color);
      border-radius: 4px;
      -webkit-appearance: none; /* Override default styles */
      appearance: none;
      cursor: pointer;
  }

   .closure-controls-flex input[type="range"]::-webkit-slider-thumb {
     -webkit-appearance: none;
     appearance: none;
     width: 20px;
     height: 20px;
     background: var(--accent-color);
     border-radius: 50%;
     cursor: pointer;
     transition: background var(--transition-speed) ease;
     box-shadow: 0 2px 4px rgba(0,0,0,0.1);
   }

   .closure-controls-flex input[type="range"]::-moz-range-thumb {
     width: 20px;
     height: 20px;
     background: var(--accent-color);
     border-radius: 50%;
     cursor: pointer;
     transition: background var(--transition-speed) ease;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
   }


  #closureGapValue {
      min-width: 45px; /* Give value span space */
      text-align: left;
      color: var(--text-secondary);
  }


  #resetAppBtn {
      display: block; /* Make it a block element */
      width: auto; /* Fit content */
      margin: var(--margin-base) auto 0 auto; /* Center block with top margin */
      padding: 10px 20px;
      background-color: var(--error-color);
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 1em;
      transition: background-color var(--transition-speed) ease, transform 0.1s ease;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  #resetAppBtn:hover {
      background-color: #d32f2f;
       box-shadow: 0 4px 8px rgba(0,0,0,0.15);
  }
   #resetAppBtn:active {
      transform: scale(0.98);
  }


  .toggle-button {
    display: block;
    width: auto;
    margin: var(--margin-base) auto; /* Center button */
    padding: 12px 25px;
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color var(--transition-speed) ease, transform 0.1s ease, box-shadow var(--transition-speed) ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }

  .toggle-button:hover {
    background-color: var(--secondary-color);
     box-shadow: 0 6px 12px rgba(0,0,0,0.15);
  }
   .toggle-button:active {
      transform: scale(0.98);
   }


  #explanation {
    margin: var(--margin-base) auto;
    padding: var(--padding-base) * 1.5;
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    background-color: var(--surface-color);
     box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
     max-width: 800px; /* Align with app container */
  }

  #explanation h2, #explanation h3 {
    color: var(--primary-color);
    margin-bottom: var(--padding-base) / 2;
  }
   #explanation h3 {
       margin-top: var(--padding-base);
       color: var(--secondary-color);
   }


  #explanation p, #explanation li {
    line-height: 1.6;
    color: var(--text-secondary);
    font-size: 1em;
  }

  #explanation ul {
      margin-top: var(--padding-base);
      padding-left: var(--padding-base);
  }
   #explanation li {
       margin-bottom: var(--padding-base) / 2;
   }


  .hidden {
    display: none;
  }

  /* Responsive Adjustments */
  @media (max-width: 600px) {
      .gestalt-app-container, #explanation {
          padding: var(--padding-base); /* Less padding on small screens */
      }
      .button-group button,
      .button-group select {
          flex-basis: 100%; /* Stack buttons */
          max-width: none; /* Allow full width */
      }
       .closure-controls-flex {
           flex-direction: column; /* Stack items vertically */
           align-items: stretch;
       }
       .closure-controls-flex label {
           text-align: center;
           margin-bottom: 5px;
           margin-right: 0;
       }
       .closure-controls-flex input[type="range"] {
            margin: 0 auto 10px auto; /* Center slider */
            width: calc(100% - 20px); /* Adjust width for thumb */
       }
        #closureGapValue {
            text-align: center;
        }
       .control-section p {
           margin-bottom: var(--padding-base) / 1.5;
       }
  }
</style>

<script>
  const canvas = document.getElementById('gestaltCanvas');
  const ctx = canvas.getContext('2d');

  // Control Buttons/Inputs
  const proximityGroupRowsBtn = document.getElementById('proximityGroupRowsBtn');
  const proximityGroupColsBtn = document.getElementById('proximityGroupColsBtn');
  const proximityUniformBtn = document.getElementById('proximityUniformBtn');

  const similarityColorBtn = document.getElementById('similarityColorBtn');
  const similarityShapeBtn = document.getElementById('similarityShapeBtn');
  const similarityUniformBtn = document.getElementById('similarityUniformBtn');

  const closureShapeSelect = document.getElementById('closureShapeSelect');
  const closureGapSlider = document.getElementById('closureGapSlider');
  const closureGapValue = document.getElementById('closureGapValue');
  const closureToggleCompleteBtn = document.getElementById('closureToggleCompleteBtn');

  const resetAppBtn = document.getElementById('resetAppBtn');
  const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
  const explanationDiv = document.getElementById('explanation');

  // --- App State ---
  let currentPrinciple = 'proximity'; // proximity, similarity, closure
  let proximityState = 'uniform'; // uniform, rows, cols
  let similarityState = 'uniform'; // uniform, color, shape
  let closureShape = 'square'; // square, circle, triangle
  let closureGap = 30; // Percentage (0-100)
  let showCompleteClosure = false;

  // --- Animation State ---
  let animationStartTime = 0;
  let animationDuration = 600; // milliseconds
  let animating = false;
  let startPoints = []; // Store points state at the start of animation

  // --- Config ---
  const numRowsCols = 6; // Increased slightly for richer patterns
  const pointSize = 6;   // Slightly smaller points
  const baseSpacing = 45; // Adjusted base spacing
  const pointData = [];

  // Initialize point data (fixed number of points)
  for(let r = 0; r < numRowsCols; r++) {
      for(let c = 0; c < numRowsCols; c++) {
          pointData.push({
              id: `p-${r}-${c}`, // Unique ID for tracking
              initialRow: r,
              initialCol: c,
              currentX: 0, // Will be calculated
              currentY: 0, // Will be calculated
              targetX: 0,
              targetY: 0,
              currentColor: 'black', // Use RGB array or string
              targetColor: 'black',
              currentShape: 'circle', // circle, square
              targetShape: 'circle'
          });
      }
  }

  // --- Helper Functions ---
  function lerp(a, b, t) { // Linear interpolation
      return a + (b - a) * t;
  }

   function hexToRgb(hex) {
        const bigint = parseInt(hex.slice(1), 16);
        const r = (bigint >> 16) & 255;
        const g = (bigint >> 8) & 255;
        const b = bigint & 255;
        return [r, g, b];
    }

    function rgbToHex(r, g, b) {
        return '#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
    }

    function lerpColor(color1, color2, t) {
        const rgb1 = hexToRgb(color1);
        const rgb2 = hexToRgb(color2);
        const r = Math.round(lerp(rgb1[0], rgb2[0], t));
        const g = Math.round(lerp(rgb1[1], rgb2[1], t));
        const b = Math.round(lerp(rgb1[2], rgb2[2], t));
        return rgbToHex(r, g, b);
    }


  // --- Calculation Functions ---
  function calculatePointTargetState(point, currentProximityState, currentSimilarityState) {
      const numPointsInRowCol = numRowsCols;
      let horizontalSpacing, verticalSpacing;

      // Calculate target spacing based on proximity state
      if (currentProximityState === 'uniform') {
          horizontalSpacing = baseSpacing;
          verticalSpacing = baseSpacing;
      } else if (currentProximityState === 'rows') {
          horizontalSpacing = baseSpacing * 0.6; // Closer horizontally
          verticalSpacing = baseSpacing * 1.4;   // Further vertically
      } else if (currentProximityState === 'cols') {
          horizontalSpacing = baseSpacing * 1.4; // Further horizontally
          verticalSpacing = baseSpacing * 0.6;   // Closer vertically
      }

      // Calculate target position to center the grid based on target spacing
      const totalGridWidth = (numPointsInRowCol - 1) * horizontalSpacing;
      const totalGridHeight = (numPointsInRowCol - 1) * verticalSpacing;
      const startX = (canvas.width - totalGridWidth) / 2;
      const startY = (canvas.height - totalGridHeight) / 2;

      // Assign target position
      point.targetX = startX + point.initialCol * horizontalSpacing;
      point.targetY = startY + point.initialRow * verticalSpacing;

      // Assign target color and shape based on similarity state
      point.targetColor = 'black';
      point.targetShape = 'circle';

      const index = point.initialRow * numPointsInRowCol + point.initialCol; // Calculate flat index

      if (currentSimilarityState === 'color') {
          point.targetColor = index % 2 === 0 ? '#007bff' : '#dc3545'; // Blue and Red
          point.targetShape = 'circle'; // Uniform shape
      } else if (currentSimilarityState === 'shape') {
          point.targetShape = index % 2 === 0 ? 'circle' : 'square';
          point.targetColor = 'black'; // Uniform color
      } else { // similarityUniform or any proximity state
           point.targetColor = 'black';
           point.targetShape = 'circle';
      }
       // Store the current state of the point before calculating the target
       // This is needed for the start of the animation
       if (!animating) {
           point.currentX = point.targetX;
           point.currentY = point.targetY;
           point.currentColor = point.targetColor;
           point.currentShape = point.targetShape;
       }
  }


  // --- Drawing Functions ---
  function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  function drawPoint(point, alpha = 1) {
      ctx.save(); // Save context state
      ctx.globalAlpha = alpha; // Apply opacity

      ctx.fillStyle = point.currentColor; // Use current color for animation
      const x = point.currentX;
      const y = point.currentY;

      if (point.currentShape === 'circle') { // Use current shape for animation
        ctx.beginPath();
        ctx.arc(x, y, pointSize, 0, Math.PI * 2);
        ctx.fill();
      } else if (point.currentShape === 'square') {
        // Adjust rect position to be centered around x,y
        ctx.fillRect(x - pointSize, y - pointSize, pointSize * 2, pointSize * 2);
      }
       ctx.restore(); // Restore context state
  }

  function drawClosureShape(shapeType, gapPercent, showComplete) {
      clearCanvas();
      ctx.strokeStyle = varToHex('--primary-color'); // Use defined color
      ctx.lineWidth = 4; // Thicker line for closure
      ctx.lineCap = 'round'; // Round caps for segments

      const centerX = canvas.width / 2;
      const centerY = canvas.height / 2;

      if (showComplete) {
          ctx.beginPath();
          if (shapeType === 'square') {
              const size = 150; // Slightly larger
              const halfSize = size / 2;
              ctx.strokeRect(centerX - halfSize, centerY - halfSize, size, size);
          } else if (shapeType === 'circle') {
              const radius = 75; // Slightly larger
              ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
              ctx.stroke();
          } else if (shapeType === 'triangle') {
             const size = 170; // Slightly larger
             const height = size * Math.sqrt(3) / 2;
             const p1 = { x: centerX, y: centerY - height / 2 };
             const p2 = { x: centerX - size / 2, y: centerY + height / 2 };
             const p3 = { x: centerX + size / 2, y: centerY + height / 2 };
             ctx.moveTo(p1.x, p1.y);
             ctx.lineTo(p2.x, p2.y);
             ctx.lineTo(p3.x, p3.y);
             ctx.closePath();
             ctx.stroke();
          }
      } else {
          // Draw partial shape with a gap
          if (shapeType === 'square') {
              const size = 150;
              const halfSize = size / 2;
              const totalPerimeter = size * 4;
              const gapLength = totalPerimeter * (gapPercent / 100);
              const segmentLength = (totalPerimeter - gapLength) / 4; // Length of each of the 4 drawn segments

               // Define start/end points for drawing, leaving gaps at corners
               // (start from middle of top side, go counter-clockwise)
               const start = { x: centerX, y: centerY - halfSize };
               const p1 = { x: centerX + halfSize, y: centerY - halfSize };
               const p2 = { x: centerX + halfSize, y: centerY + halfSize };
               const p3 = { x: centerX - halfSize, y: centerY + halfSize };
               const p4 = { x: centerX - halfSize, y: centerY - halfSize };
               const end = { x: centerX, y: centerY - halfSize }; // Back to start

               const pointsList = [start, p1, p2, p3, p4, end];

               let currentLength = 0;
               ctx.beginPath();
               ctx.moveTo(pointsList[0].x, pointsList[0].y);

               for (let i = 0; i < pointsList.length - 1; i++) {
                   const pStart = pointsList[i];
                   const pEnd = pointsList[i+1];
                   const sideTotalLength = Math.sqrt(Math.pow(pEnd.x - pStart.x, 2) + Math.pow(pEnd.y - pStart.y, 2));

                    // Calculate how much length to draw on this segment
                    let drawOnThisSegment = Math.min(segmentLength, sideTotalLength - currentLength);
                    if (drawOnThisSegment <= 0) continue;

                    // Calculate end point for the drawn segment
                    const t = drawOnThisSegment / sideTotalLength;
                    const endX = lerp(pStart.x, pEnd.x, t);
                    const endY = lerp(pStart.y, pEnd.y, t);

                    ctx.lineTo(endX, endY);

                    currentLength += drawOnThisSegment;
                    if (currentLength >= totalPerimeter - gapLength) break; // Stop if total drawn length is reached

                    // If we reached the end of a side, start a new path after the gap
                    if (currentLength < totalPerimeter - gapLength && Math.abs(currentLength - sideTotalLength) < 0.001) {
                         ctx.stroke(); // Stroke the segment
                         ctx.beginPath();
                         // Move to the start of the next segment after the gap
                         const remainingGap = totalPerimeter - gapLength - currentLength; // This logic is still complex.
                         // Let's simplify the drawing approach: Draw 4 separate segments.
                         // Each segment is length 'segmentLength', separated by a gap 'gapLength/4' at corners.

                         const sideGap = gapLength / 4;

                         // Segment 1 (Top): From left gap edge to right gap edge
                         ctx.beginPath();
                         ctx.moveTo(centerX - halfSize + sideGap/2, centerY - halfSize);
                         ctx.lineTo(centerX + halfSize - sideGap/2, centerY - halfSize);
                         ctx.stroke();

                         // Segment 2 (Right): From top gap edge to bottom gap edge
                         ctx.beginPath();
                         ctx.moveTo(centerX + halfSize, centerY - halfSize + sideGap/2);
                         ctx.lineTo(centerX + halfSize, centerY + halfSize - sideGap/2);
                         ctx.stroke();

                         // Segment 3 (Bottom): From right gap edge to left gap edge
                         ctx.beginPath();
                         ctx.moveTo(centerX + halfSize - sideGap/2, centerY + halfSize);
                         ctx.lineTo(centerX - halfSize + sideGap/2, centerY + halfSize);
                         ctx.stroke();

                         // Segment 4 (Left): From bottom gap edge to top gap edge
                         ctx.beginPath();
                         ctx.moveTo(centerX - halfSize, centerY + halfSize - sideGap/2);
                         ctx.lineTo(centerX - halfSize, centerY - halfSize + sideGap/2);
                         ctx.stroke();

                         break; // Drawing 4 segments is done
                    }
               }


          } else if (shapeType === 'circle') {
              const radius = 75;
              const totalCircumference = 2 * Math.PI * radius;
              const gapRadians = (2 * Math.PI) * (gapPercent / 100);
              // Start/End angles for the arc (leaving a gap at the top)
              // Adjust angles slightly to leave gap centered at the top (-PI/2)
              const startAngle = -Math.PI / 2 + gapRadians / 2;
              const endAngle = -Math.PI / 2 + (2 * Math.PI - gapRadians); // Ensure arc length is full circle minus gap

              ctx.beginPath();
              // arc(x, y, radius, startAngle, endAngle, counterclockwise)
              ctx.arc(centerX, centerY, radius, startAngle, endAngle);
              ctx.stroke();

          } else if (shapeType === 'triangle') {
             const size = 170;
             const height = size * Math.sqrt(3) / 2;
             const totalPerimeter = size * 3;
             const gapLength = totalPerimeter * (gapPercent / 100);
             const segmentLength = (totalPerimeter - gapLength) / 3; // Length of each of the 3 drawn segments
             const sideGap = gapLength / 3; // Gap distributed at ends of each side segment

             // Define points (Top, Bottom-Left, Bottom-Right)
             const p1 = { x: centerX, y: centerY - height / 2 };
             const p2 = { x: centerX - size / 2, y: centerY + height / 2 };
             const p3 = { x: centerX + size / 2, y: centerY + height / 2 };

             // Segment 1 (p1 to p2): From point near p1 towards p2, to point near p2 towards p1
             const dist1 = Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2)); // Length of this side (should be 'size')
             const t1_start = sideGap / 2 / dist1;
             const t1_end = (dist1 - sideGap / 2) / dist1;
             ctx.beginPath();
             ctx.moveTo(lerp(p1.x, p2.x, t1_start), lerp(p1.y, p2.y, t1_start));
             ctx.lineTo(lerp(p1.x, p2.x, t1_end), lerp(p1.y, p2.y, t1_end));
             ctx.stroke();

             // Segment 2 (p2 to p3): From point near p2 towards p3, to point near p3 towards p2
              const dist2 = Math.sqrt(Math.pow(p3.x - p2.x, 2) + Math.pow(p3.y - p2.y, 2)); // Length of this side (should be 'size')
             const t2_start = sideGap / 2 / dist2;
             const t2_end = (dist2 - sideGap / 2) / dist2;
             ctx.beginPath();
             ctx.moveTo(lerp(p2.x, p3.x, t2_start), lerp(p2.y, p3.y, t2_start));
             ctx.lineTo(lerp(p2.x, p3.x, t2_end), lerp(p2.y, p3.y, t2_end));
             ctx.stroke();

             // Segment 3 (p3 to p1): From point near p3 towards p1, to point near p1 towards p3
              const dist3 = Math.sqrt(Math.pow(p1.x - p3.x, 2) + Math.pow(p1.y - p3.y, 2)); // Length of this side (should be 'size')
             const t3_start = sideGap / 2 / dist3;
             const t3_end = (dist3 - sideGap / 2) / dist3;
             ctx.beginPath();
             ctx.moveTo(lerp(p3.x, p1.x, t3_start), lerp(p3.y, p1.y, t3_start));
             ctx.lineTo(lerp(p3.x, p1.x, t3_end), lerp(p3.y, p1.y, t3_end));
             ctx.stroke();
          }
      }
  }

  // Helper to get CSS variable color (useful for drawing shapes with them)
  function varToHex(variableName) {
      const color = getComputedStyle(document.documentElement).getPropertyValue(variableName).trim();
      // Basic check if it's a hex color
      if (color.startsWith('#')) {
          return color;
      }
      // Add logic here if you need to convert rgb(x,y,z) to hex
       // For now, assume primary-color and secondary-color are hex in CSS
       console.warn(`Color variable ${variableName} might not be a hex value: ${color}`);
       return color; // Return as is, hope it works
  }


  // --- Animation Loop ---
  function animate(timestamp) {
      if (!animationStartTime) {
          animationStartTime = timestamp;
          startPoints = pointData.map(p => ({ // Deep copy start state
              x: p.currentX,
              y: p.currentY,
              color: p.currentColor,
              shape: p.currentShape // Shape doesn't animate, but good to store
          }));
           // Calculate target state *before* animation starts
           pointData.forEach(p => calculatePointTargetState(p, proximityState, similarityState));
      }

      const elapsed = timestamp - animationStartTime;
      let progress = Math.min(elapsed / animationDuration, 1); // Animation progress 0 to 1

      // Use an easing function (e.g., easeInOutQuad)
      // progress = progress < 0.5 ? 2 * progress * progress : 1 - Math.pow(-2 * progress + 2, 2) / 2;

      clearCanvas();

      // Interpolate and draw each point
      pointData.forEach((point, index) => {
          // Interpolate position
          point.currentX = lerp(startPoints[index].x, point.targetX, progress);
          point.currentY = lerp(startPoints[index].y, point.targetY, progress);

          // Interpolate color (only if target color is different)
          if (startPoints[index].color !== point.targetColor) {
              point.currentColor = lerpColor(startPoints[index].color, point.targetColor, progress);
          } else {
               point.currentColor = point.targetColor; // If no change, just use target
          }

          // Shape doesn't animate, just snap at the end or beginning
           point.currentShape = progress >= 1 ? point.targetShape : startPoints[index].shape;


          drawPoint(point);
      });

      if (progress < 1) {
          requestAnimationFrame(animate);
          animating = true;
      } else {
          animationStartTime = 0; // Reset for next animation
           animating = false;
          // Ensure points are exactly at target after animation
          pointData.forEach(p => {
              p.currentX = p.targetX;
              p.currentY = p.targetY;
              p.currentColor = p.targetColor;
              p.currentShape = p.targetShape;
          });
      }
  }


  // --- Render Function (calls animate for points, or draws closure directly) ---
  function render() {
      if (currentPrinciple === 'closure') {
          clearCanvas(); // Clear any previous points animation
          drawClosureShape(closureShape, closureGap, showCompleteClosure);
           animating = false; // Stop any ongoing point animation
           animationStartTime = 0; // Reset animation time
      } else {
           // Ensure points are in the correct *starting* position before new animation
           // based on the *previous* state
           pointData.forEach(p => calculatePointTargetState(p, proximityState, similarityState));
           // Now start the animation towards the new target state
           requestAnimationFrame(animate);
      }
  }

  // --- Update Functions (change state and trigger render) ---
  function updateProximity(state) {
      currentPrinciple = 'proximity';
      proximityState = state;
      similarityState = 'uniform'; // Proximity overrides similarity appearance
      render();
  }

  function updateSimilarity(state) {
      currentPrinciple = 'similarity';
      similarityState = state;
      proximityState = 'uniform'; // Similarity defaults to uniform proximity
      render();
  }

   function updateClosureDisplay() {
       currentPrinciple = 'closure';
       closureShape = closureShapeSelect.value;
       closureGap = parseInt(closureGapSlider.value);
       closureGapValue.textContent = `${closureGap}%`;
       render(); // Closure is redrawn directly, not animated via points
   }


  // --- Event Listeners ---

  // Proximity Controls
  proximityGroupRowsBtn.addEventListener('click', () => updateProximity('rows'));
  proximityGroupColsBtn.addEventListener('click', () => updateProximity('cols'));
  proximityUniformBtn.addEventListener('click', () => updateProximity('uniform'));

  // Similarity Controls
  similarityColorBtn.addEventListener('click', () => updateSimilarity('color'));
  similarityShapeBtn.addEventListener('click', () => updateSimilarity('shape'));
   similarityUniformBtn.addEventListener('click', () => updateSimilarity('uniform'));


  // Closure Controls
  closureShapeSelect.addEventListener('change', updateClosureDisplay);
  closureGapSlider.addEventListener('input', updateClosureDisplay);

  closureToggleCompleteBtn.addEventListener('click', () => {
      showCompleteClosure = !showCompleteClosure;
      closureToggleCompleteBtn.textContent = showCompleteClosure ? 'הסתר צורה שלמה' : 'הצג צורה שלמה';
      currentPrinciple = 'closure'; // Ensure state
      render();
  });

  // Reset Button
  resetAppBtn.addEventListener('click', () => {
      currentPrinciple = 'proximity';
      proximityState = 'uniform';
      similarityState = 'uniform';
      closureShape = 'square';
      closureGap = 30;
      showCompleteClosure = false;

      // Reset controls visually
      closureShapeSelect.value = 'square';
      closureGapSlider.value = 30;
      closureGapValue.textContent = '30%';
      closureToggleCompleteBtn.textContent = 'הצג/הסתר צורה שלמה';


      render(); // Initial render with default state
  });

  // Explanation Toggle
  toggleExplanationBtn.addEventListener('click', () => {
    explanationDiv.classList.toggle('hidden');
    if (explanationDiv.classList.contains('hidden')) {
      toggleExplanationBtn.textContent = 'רוצה להבין את הקסם? הקלק להסבר מורחב!';
    } else {
      toggleExplanationBtn.textContent = 'הסתר הסבר מורחב';
    }
  });

  // --- Initial Setup ---
   // Ensure canvas dimensions match the HTML attributes initially (important for high-res screens later)
   const setCanvasDimensions = () => {
        const rect = canvas.getBoundingClientRect();
        canvas.width = rect.width;
        canvas.height = rect.height;
         // Redraw after resize
        render();
   };
    // Initial set and add resize listener
    setCanvasDimensions();
    window.addEventListener('resize', setCanvasDimensions);


  // Set initial state and render the default view
  currentPrinciple = 'proximity';
  proximityState = 'uniform';
  similarityState = 'uniform'; // Default for proximity view
  render(); // Initial render


</script>
```