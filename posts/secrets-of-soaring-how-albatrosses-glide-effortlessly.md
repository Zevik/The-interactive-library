---
title: "סודות הדאייה: ריחוף אלבטרוסים ללא מאמץ"
english_slug: secrets-of-soaring-how-albatrosses-glide-effortlessly
category: "מדעי החיים / ביולוגיה"
tags:
  - דאייה
  - אלבטרוס
  - תעופה ביולוגית
  - אווירודינמיקה
  - חיסכון באנרגיה
  - פיזיקה של תעופה
---
<h1>סודות הדאייה: ריחוף אלבטרוסים ללא מאמץ</h1>
<p>דמיינו מסע של אלפי קילומטרים מעל האוקיינוס הפתוח, שעות על גבי שעות באוויר, כמעט ללא מחיאת כנף אחת. זה לא חלום, זו המציאות של האלבטרוס – אלוף הדאייה הבלתי מעורער של עולם הציפורים. איך יצור כה גדול וכבד מצליח לחצות מרחקים אדירים תוך השקעת כמעט אפס אנרגיה?</p>
<p>צללו לתוך הסימולציה האינטראקטיבית שלנו כדי לגלות את הסודות המדהימים המאפשרים לאלבטרוסים לרחף בחן וביעילות מדהימה.</p>

<div id="app">
  <div id="simulation-area">
    <canvas id="albatross-canvas"></canvas>
    <div id="distance-counter">מרחק: 0 ק"מ</div>
    <div id="energy-gain-indicator" class="hidden">🎉 צובר אנרגיה! 🎉</div>
  </div>
  <div id="controls">
    <h2>שליטה בסימולציה</h2>
     <p class="controls-intro">שחקו עם התנאים כדי לראות איך האלבטרוס מגיב ומנהל את האנרגיה שלו.</p>
    <div class="control-group">
      <label for="wind-speed">עוצמת רוח:</label>
      <input type="range" id="wind-speed" min="5" max="35" value="15" step="1">
      <span id="wind-speed-value">15</span> מ"ש
    </div>
    <div class="control-group">
      <label for="wind-direction">כיוון רוח:</label>
      <input type="range" id="wind-direction" min="0" max="360" value="0" step="10">
      <span id="wind-direction-value">0</span>&deg; (0=צפון, 90=מזרח)
    </div>
    <button id="add-thermal">הוסף זרם אוויר חם (תרמיקה) ☀️</button>
    <div class="control-group">
      <label>סטטוס אנרגיה:</label>
      <div id="energy-bar-container"><div id="energy-bar"></div></div>
      <span id="energy-value">100</span>%
    </div>
    <p><small><strong>טיפים לאלופים:</strong> גררו את האלבטרוס או את התרמיקה (אם יש) כדי לשנות את מיקומם. שימו לב איך גובה ומהירות הרוח משפיעים על האנרגיה!</small></p>
  </div>
</div>

<button id="show-explanation-button" class="toggle-button">הצג הסבר מלא על סודות הדאייה</button>

<div id="explanation" style="display: none;">
  <h2>הסבר מעמיק: אמנות הריחוף של האלבטרוס</h2>

  <h3>מדוע דאייה חיונית לאלבטרוס? חיסכון הוא שם המשחק.</h3>
  <p>דמיינו את עצמכם מנסים לרוץ מרתון תוך כדי קפיצה רצופה... תעופה רצופה באמצעות מחיאות כנף היא פעילות פיזית אדירה, בפרט עבור ציפורים גדולות וכבדות כמו האלבטרוס. מסעות הציד והנדידה שלהם יכולים להשתרע על פני אלפי קילומטרים מעל אוקיינוסים רחבי ידיים. הוצאה אנרגטית עצומה כזו פשוט אינה בת קיימא. הפתרון האבולוציוני האלגנטי: לרתום את אנרגיית הסביבה. האלבטרוסים, ועופות דואים אחרים, פיתחו יכולות מדהימות לנצל זרמי אוויר ושינויי רוח כדי להישאר באוויר, לשמור על גובה ומהירות, ולכסות מרחקים אדירים תוך מינימום השקעת אנרגיה שרירית.</p>

  <h3>עקרונות היסוד של תעופה ודאייה: עילוי וגרר בפעולה</h3>
  <p>כל עצם הטס באוויר מושפע מכמה כוחות מרכזיים: <strong>כוח הכבידה</strong> שמושך אותו מטה, ו<strong>כוח העילוי (Lift)</strong> שמנסה להרים אותו מעלה. בעת תנועה באוויר, קיים גם <strong>כוח הגרר (Drag)</strong>, המתנגד לכיוון התנועה ומנסה להאט את העצם. בדאייה, הציפור אינה מייצרת עילוי באמצעות מחיאות כנף, אלא על ידי תנועה קדימה ויצירת זרם אוויר יחסית מעל ומתחת לכנף, שמתוכננת בצורה אווירודינמית מושלמת (פרופיל כנף). כדי לשמור על מהירות מספקת ליצירת עילוי, ציפורים רבות בדאייה בסיסית מאבדות גובה בהדרגה – הן ממירות אנרגיה פוטנציאלית (גובה) לאנרגיה קינטית (מהירות). דאייה "חופשית" כזו אפשרית רק לזמן מוגבל עד שהציפור חייבת לנחות או להשתמש במחיאות כנף.</p>

  <h3>המומחיות של האלבטרוס: דאייה דינמית (Dynamic Soaring)</h3>
  <p>מעל האוקיינוס הפתוח, שם אין קרקע חמה ליצירת תרמיקות, האלבטרוסים מנצלים טכניקה גאונית: דאייה דינמית. טכניקה זו מתבססת על תופעת <strong>גרדיאנט הרוח</strong> – הרוח חזקה יותר ככל שעולים בגובה מעל פני המים (בגלל פחות חיכוך). האלבטרוס מבצע סדרה מתוזמנת ומדויקת של פניות:</p>
  <ul>
    <li><strong>מגובה רב, צלילה מהירה עם הרוח:</strong> הציפור צוללת בזווית חדה יחסית לכיוון פני המים, תוך כדי פנייה עדינה עם כיוון הרוח החזקה ששוררת בגובה. היא בונה מהירות גבוהה ומאגרת אנרגיה קינטית.</li>
    <li><strong>קרוב לפני המים, פנייה חדה כנגד הרוח:</strong> רגע לפני שהיא מגיעה לגובה פני הים (שם הרוח חלשה משמעותית), הציפור מבצעת פנייה מהירה וחדה של 180 מעלות, כך שהיא פונה כעת כמעט ישירות כנגד כיוון הרוח. המעבר הפתאומי מהרוח החזקה לגבוה לרוח החלשה בנמוך, בשילוב עם המהירות הגבוהה שצברה בצלילה, יוצר "רוח יחסית" (Relative Wind) חזקה מאוד המגיעה ממול. הרוח היחסית הזו מאפשרת לה לטפס בחזרה לגובה במהירות וביעילות מדהימה, תוך שהיא "שואבת" אנרגיה מהרוח.</li>
    <li><strong>בגובה רב, פנייה חדה שוב עם הרוח:</strong> האלבטרוס פונה שוב עם כיוון הרוח כדי להתחיל את המחזור מחדש, שוב צולל ומאגר מהירות.</li>
  </ul>
  <p>בזכות סדרת תמרונים זו, האלבטרוס מצליח למעשה "לגנוב" אנרגיה מהרוח, לטפס בחזרה לגובה, ולשמור על מהירות ללא מחיאות כנף.</p>

  <h3>דאייה תרמית (Thermal Soaring)</h3>
  <p>למרות שהיא אופיינית יותר לציפורים הדואות מעל היבשה (נשרים, חסידות, עגורים) שמנצלות עמודות אוויר חם העולות מהקרקע המחוממת מהשמש, גם אלבטרוסים יכולים להשתמש בטכניקה זו בסמוך ליבשה או מעל איים. הציפור מזהה אזור של אוויר חם שעולה כלפי מעלה (תרמיקה) ומקיפה אותו במעגלים כדי להישאר בזרם האוויר העולה. הזרם נושא אותה כלפי מעלה, ומאפשר לה לצבור גובה ללא מאמץ. לאחר שהגיעה לגובה הרצוי, היא יוצאת מהתרמיקה ודואה קדימה, מאבדת גובה באיטיות, עד שתמצא תרמיקה נוספת.</p>

  <h3>ההתאמות הביולוגיות שהופכות את האלבטרוס למומחה</h3>
  <p>מעבר לטכניקות התעופה המדהימות, לאלבטרוס יש גם מבנה גוף מושלם לדאייה:</p>
  <ul>
    <li><strong>כנפיים ארוכות וצרות במיוחד:</strong> מוטת הכנפיים של אלבטרוסים גדולים יכולה לעבור את 3 מטרים! צורת כנף כזו (עם יחס גובה-רוחב גבוה - High Aspect Ratio) מפחיתה משמעותית את "גרר המושרה" (Induced Drag) - הגרר הנוצר בקצות הכנפיים עקב יצירת העילוי. כנף ארוכה וצרה יעילה במיוחד במהירויות שיוט גבוהות ודורשת פחות אנרגיה לתחזוקת העילוי.</li>
    <li><strong>מנגנון נעילה במפרק הכתף:</strong> פטנט אבולוציוני מדהים! האלבטרוסים יכולים "לנעול" את כנפיהם במצב פרוש באופן פסיבי, ללא צורך בהפעלת שרירים מתמדת. זה חוסך כמות עצומה של אנרגיה ומאפשר להם לשמור על מוטת כנף ענקית ללא עייפות שרירית לאורך שעות וימים של דאייה.</li>
  </ul>

  <h3>סיכום: אמנות הריחוף כהישג אבולוציוני</h3>
  <p>השילוב של טכניקות דאייה מתקדמות (דינמית ותרמית) והתאמות גופניות ייחודיות הופכות את האלבטרוס למכונת תעופה בלתי רגילה, המסוגלת לכסות מרחקים גלובליים תוך ניצול מדהים של אנרגיה סביבתית. הם מהווים דוגמה מרהיבה כיצד האבולוציה מוצאת פתרונות יצירתיים לחיסכון באנרגיה בסביבות מאתגרות, ומאפשרת חיים באזורים נרחבים ודלילי מזון.</p>
</div>

<style>
  :root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    --light-color: #f8f9fa;
    --dark-color: #343a40;
    --info-color: #17a2b8;
    --border-color: #dee2e6;
    --background-color: #e9ecef;
    --card-background: #fff;
    --text-color: #212529;
    --heading-color: #343a40;
  }

  body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    background-color: var(--background-color);
    color: var(--text-color);
    direction: rtl; /* Hebrew direction */
    text-align: right;
    overflow-x: hidden; /* Prevent horizontal scroll */
  }

  h1, h2, h3 {
    color: var(--heading-color);
    text-align: center;
    margin-bottom: 15px;
    font-weight: bold;
  }

  h1 {
      font-size: 2.5em;
      margin-top: 0;
      margin-bottom: 10px;
  }

  h2 {
      font-size: 1.8em;
      border-bottom: 2px solid var(--primary-color);
      padding-bottom: 5px;
      margin-top: 25px;
      margin-bottom: 15px;
      text-align: right; /* Align headings in explanation */
  }

   h3 {
       font-size: 1.4em;
       color: var(--secondary-color);
       margin-top: 20px;
       margin-bottom: 10px;
       text-align: right; /* Align headings in explanation */
   }


  p {
    margin-bottom: 15px;
    text-align: right;
  }

  .controls-intro {
      font-size: 0.9em;
      color: var(--secondary-color);
      text-align: center;
      margin-bottom: 20px;
  }

  #app {
    display: flex;
    flex-direction: column;
    gap: 20px;
    background-color: var(--card-background);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    max-width: 900px;
    margin: 20px auto;
  }

  #simulation-area {
    width: 100%;
    max-width: 860px; /* slightly less than app width */
    margin: 0 auto;
    border: 1px solid var(--border-color);
    position: relative;
    overflow: hidden;
    aspect-ratio: 16 / 9; /* Maintain aspect ratio */
    background: linear-gradient(to bottom, #a0c8f0 0%, #e0f0ff 70%, #c3d9ee 100%); /* Sky gradient */
    border-radius: 8px;
  }

   #distance-counter {
       position: absolute;
       top: 10px;
       left: 10px; /* Position on the left for LTR numbers */
       background-color: rgba(255, 255, 255, 0.8);
       padding: 5px 10px;
       border-radius: 5px;
       font-size: 1em;
       font-weight: bold;
       color: var(--dark-color);
       z-index: 10;
   }

  #energy-gain-indicator {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: var(--success-color);
      color: white;
      padding: 10px 20px;
      border-radius: 20px;
      font-size: 1.2em;
      font-weight: bold;
      z-index: 10;
      opacity: 1;
      transition: opacity 0.5s ease-out;
  }

  #energy-gain-indicator.hidden {
      opacity: 0;
      pointer-events: none; /* Allow clicking through when hidden */
  }

  #albatross-canvas {
    display: block;
    width: 100%;
    height: 100%;
  }

  #controls {
    width: 100%;
    max-width: 860px; /* Match sim area width */
    margin: 0 auto;
    padding: 15px;
    border: 1px solid var(--border-color);
    background-color: var(--light-color);
    border-radius: 8px;
  }
  .control-group {
    margin-bottom: 15px;
    padding-bottom: 15px;
    border-bottom: 1px dashed var(--border-color);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
  }
   .control-group:last-child {
     border-bottom: none;
     padding-bottom: 0;
     margin-bottom: 0;
   }
  #controls label {
    display: inline-block;
    margin-bottom: 5px;
    font-weight: bold;
    min-width: 120px; /* Align labels */
    flex-shrink: 0; /* Prevent shrinking */
  }
  #controls input[type="range"] {
    vertical-align: middle;
    flex-grow: 1; /* Take available space */
    margin-right: 10px;
    margin-left: 10px; /* Add margin for RTL */
  }
   #controls span {
     display: inline-block;
     width: 40px;
     text-align: left; /* Align number */
     font-family: monospace;
     font-weight: bold;
     color: var(--primary-color);
     flex-shrink: 0; /* Prevent shrinking */
   }

  #energy-bar-container {
    width: calc(100% - 160px); /* Adjust width based on label and value */
    height: 20px;
    background-color: var(--border-color);
    margin-top: 5px;
    border-radius: 4px;
    overflow: hidden;
    flex-grow: 1;
  }
  #energy-bar {
    height: 100%;
    width: 100%; /* Initial width */
    background-color: var(--success-color);
    transition: width 0.3s ease-out, background-color 0.3s ease-out; /* Smooth transition */
    /* Animation for low energy */
    animation: pulse-red 1.5s infinite ease-in-out alternate;
  }
   #energy-bar-container.low-energy #energy-bar {
       background-color: var(--danger-color);
       animation: pulse-red 1.5s infinite ease-in-out alternate;
   }
    #energy-bar-container.medium-energy #energy-bar {
       background-color: var(--warning-color);
        animation: pulse-orange 2s infinite ease-in-out alternate;
   }
    #energy-bar-container.high-energy #energy-bar {
       background-color: var(--success-color);
       animation: none; /* No pulse when high */
   }


   @keyframes pulse-red {
       from { transform: scaleX(1); opacity: 1; }
       to { transform: scaleX(0.98); opacity: 0.8; }
   }
    @keyframes pulse-orange {
       from { transform: scaleX(1); opacity: 1; }
       to { transform: scaleX(0.99); opacity: 0.9; }
   }


  button {
    display: block;
    margin: 20px auto; /* Center button */
    padding: 12px 20px;
    cursor: pointer;
    font-size: 1.1em;
    border: none;
    border-radius: 8px;
    background-color: var(--primary-color);
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
  }
  button:hover {
    background-color: #0056b3; /* Darker blue */
  }
   button:active {
       transform: scale(0.98);
   }

   button.toggle-button {
       background-color: var(--secondary-color);
   }
    button.toggle-button:hover {
       background-color: #545b62;
   }


  #explanation {
    margin-top: 30px;
    border-top: 1px solid var(--border-color);
    padding-top: 20px;
    background-color: var(--card-background);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    max-width: 900px;
    margin: 20px auto;
    transition: all 0.5s ease-in-out;
  }

   #explanation ul {
     margin-top: 15px;
     margin-bottom: 15px;
     padding-right: 25px; /* Indent list */
   }
   #explanation li {
     margin-bottom: 10px;
     line-height: 1.7;
   }
   #explanation strong {
     color: var(--primary-color);
   }

    canvas {
        cursor: grab; /* Indicate draggable area */
    }
     canvas:active {
        cursor: grabbing;
    }


</style>

<script>
  const canvas = document.getElementById('albatross-canvas');
  const ctx = canvas.getContext('2d');
  const windSpeedSlider = document.getElementById('wind-speed');
  const windSpeedValueSpan = document.getElementById('wind-speed-value');
  const windDirectionSlider = document.getElementById('wind-direction');
  const windDirectionValueSpan = document.getElementById('wind-direction-value');
  const addThermalButton = document.getElementById('add-thermal');
  const energyBarContainer = document.getElementById('energy-bar-container');
  const energyBar = document.getElementById('energy-bar');
  const energyValueSpan = document.getElementById('energy-value');
  const showExplanationButton = document.getElementById('show-explanation-button');
  const explanationDiv = document.getElementById('explanation');
  const simulationArea = document.getElementById('simulation-area');
  const distanceCounter = document.getElementById('distance-counter');
  const energyGainIndicator = document.getElementById('energy-gain-indicator');


  let albatross = {
    x: 100,
    y: 100,
    vx: 5, // velocity x
    vy: 0, // velocity y
    speed: 5, // magnitude of velocity
    direction: 0, // angle in radians (0=right, PI/2=down)
    energy: 100, // energy level 0-100
    path: [],
    isDragging: false,
    dragOffsetX: 0,
    dragOffsetY: 0,
    angle: 0, // Visual angle for drawing (can be different from direction)
    banking: 0, // For visual banking effect
  };

  let wind = {
    speed: parseFloat(windSpeedSlider.value),
    direction: parseFloat(windDirectionSlider.value) * Math.PI / 180, // radians (0=Up, 90=Right)
    vx: 0, // calculated
    vy: 0, // calculated
  };

  let thermals = []; // Use array for possibility of multiple later, currently limited to one

  const GRAVITY = 0.08; // pixels per frame^2 (increased slightly)
  const DRAG_COEFFICIENT = 0.0008; // affects energy loss (increased slightly)
  const LIFT_COEFFICIENT = 0.015; // affects lift based on speed and AoA (simplified, increased slightly)
  const THERMAL_STRENGTH = -0.6; // upward force in thermal (adjusted)
  const THERMAL_RADIUS = 100; // pixels (increased)
  const ENERGY_DECAY_RATE = 0.04; // energy loss per frame (basic, increased)
  const ENERGY_GAIN_THERMAL = 0.15; // energy gain per frame in thermal
  const ENERGY_GAIN_DYNAMIC_FACTOR = 0.008; // energy gain factor from dynamic soaring effect
  const DYNAMIC_SOARING_HEIGHT_LOW = 0.8; // low altitude threshold (fraction of canvas height)
  const DYNAMIC_SOARING_HEIGHT_HIGH = 0.2; // high altitude threshold (fraction of canvas height)
  const DISTANCE_SCALE = 0.01; // pixels to kilometers scale (100 pixels = 1 km)
  let totalDistance = 0;
  let lastEnergyGainType = null;
  let energyGainIndicatorTimeout = null;


  // Set canvas size based on container
  function resizeCanvas() {
    canvas.width = simulationArea.clientWidth;
    canvas.height = simulationArea.clientHeight;
     // Ensure albatross stays within bounds on resize
     albatross.x = Math.max(10, Math.min(canvas.width - 10, albatross.x));
     albatross.y = Math.max(10, Math.min(canvas.height - 10, albatross.y));
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  // Convert degrees to radians for wind direction
  // Wind direction: 0 = North (Up), 90 = East (Right). Canvas Y is down.
  // So North (0) is negative VY, East (90) is positive VX.
  function updateWindVector() {
    wind.speed = parseFloat(windSpeedSlider.value);
    let angleInRadians = (parseFloat(windDirectionSlider.value) - 90) * Math.PI / 180; // Adjust 0=Up, 90=Right to canvas (0=Right, 90=Down for +VX, +VY)
    wind.vx = wind.speed * Math.cos(angleInRadians);
    wind.vy = wind.speed * Math.sin(angleInRadians);
  }

  // Update simulation state
  function update() {
    if (albatross.isDragging) {
         // If dragging, update position directly and reduce energy decay
         albatross.energy -= ENERGY_DECAY_RATE / 3;
         albatross.energy = Math.max(0, albatross.energy);
         updateEnergyDisplay();
         // Update velocity to follow drag (smooth movement)
         const targetX = albatross.x;
         const targetY = albatross.y;
         albatross.x = mouseX - albatross.dragOffsetX; // This was already done in mousemove, but keeping logic here for clarity
         albatross.y = mouseY - albatross.dragOffsetY;

         // Calculate velocity based on how far it moved
         albatross.vx = (albatross.x - targetX); // Simple velocity calculation
         albatross.vy = (albatross.y - targetY);
         albatross.speed = Math.sqrt(albatross.vx * albatross.vx + albatross.vy * albatross.vy);
         if (albatross.speed > 1) albatross.direction = Math.atan2(albatross.vy, albatross.vx); // Update direction if moving

         return; // Skip physics simulation when dragging
    }


    // --- Physics Calculation ---

    // Air velocity relative to albatross
    let airVx = wind.vx - albatross.vx;
    let airVy = wind.vy - albatross.vy;
    let airSpeedSq = airVx * airVx + airVy * airVy;
    let airSpeed = Math.sqrt(airSpeedSq);

    // simplified Angle of Attack: Assume albatross adjusts pitch slightly.
    // A simple model could be AoA is proportional to vertical velocity relative to air
    // Let's approximate lift direction perpendicular to velocity vector for simplicity
    let liftAngle = albatross.direction - Math.PI / 2; // Perpendicular to velocity vector

    // Lift force: proportional to air speed squared and a factor related to Angle of Attack (simplified)
    // Let's make lift stronger when moving against relative wind and weaker when moving with it vertically (simplistic)
    let verticalAirVel = airVy; // How fast is the air moving *relative* to the bird vertically?
    let baseLift = LIFT_COEFFICIENT * airSpeedSq;
    // Simple AoA adjustment: If air is moving up relative to bird (bird is sinking into air), increase effective AoA.
    // If air is moving down relative to bird (bird climbing through air), decrease effective AoA.
    let aoaFactor = 1 + (-verticalAirVel * 0.05); // crude approximation, adjust factor
    let liftForce = baseLift * Math.max(0, aoaFactor); // Lift cannot be negative

    let liftAx = liftForce * Math.cos(liftAngle);
    let liftAy = liftForce * Math.sin(liftAngle);


    // Drag: always opposite to relative air velocity
    let dragForce = DRAG_COEFFICIENT * airSpeedSq;
    let relativeWindAngle = Math.atan2(airVy, airVx);
    let dragAx = -dragForce * Math.cos(relativeWindAngle);
    let dragAy = -dragForce * Math.sin(relativeWindAngle);

    // Gravity
    let gravityAy = GRAVITY;

    // Total acceleration (start with physics)
    let totalAx = dragAx + liftAx;
    let totalAy = dragAy + liftAy + gravityAy;


    // --- Environmental Effects & Energy Management ---
    let isInThermal = false;
    for (const thermal of thermals) {
      let dx = albatross.x - thermal.x;
      let dy = albatross.y - thermal.y;
      let distSq = dx * dx + dy * dy;
      if (distSq < THERMAL_RADIUS * THERMAL_RADIUS) {
        // Albatross is inside thermal
        // Add upward acceleration (negative AY) - stronger near center, weaker near edge
        let dist = Math.sqrt(distSq);
        let thermalFactor = 1 - dist / THERMAL_RADIUS; // 1 in center, 0 at edge
        totalAy += THERMAL_STRENGTH * thermalFactor;
        isInThermal = true;
        // Gain energy in thermal
         albatross.energy += ENERGY_GAIN_THERMAL * thermalFactor;
         albatross.energy = Math.min(100, albatross.energy);
         if (lastEnergyGainType !== 'thermal') {
             showEnergyGainIndicator("🎉 תרמיקה! צובר אנרגיה");
             lastEnergyGainType = 'thermal';
         }

      }
    }
     if (!isInThermal && lastEnergyGainType === 'thermal') {
         lastEnergyGainType = null; // Reset if leaving thermal
     }


    // --- Dynamic Soaring Effect ---
    // Simplified: gain energy if flying somewhat into wind gradient
    // The core idea is gaining speed when moving from slower air to faster air, or vice-versa, strategically.
    // This simulation simplifies by checking altitude and general wind direction.
    let velDotWind = albatross.vx * wind.vx + albatross.vy * wind.vy; // Positive if flying with wind, negative if against

    let isLow = albatross.y > canvas.height * DYNAMIC_SOARING_HEIGHT_LOW;
    let isHigh = albatross.y < canvas.height * DYNAMIC_SOARING_HEIGHT_HIGH;
    let altitudeFactor = 0;
    if (isLow) { // Near the 'sea' surface
        // Gain energy if flying somewhat UPWIND (velDotWind < 0) - simulating pulling up into stronger wind
        altitudeFactor = Math.max(0, -velDotWind / (wind.speed * albatross.speed)); // Factor is stronger if flying more directly against wind
    } else if (isHigh) { // High altitude
        // Gain energy if flying somewhat DOWNWIND (velDotWind > 0) - simulating diving down into weaker wind
         altitudeFactor = Math.max(0, velDotWind / (wind.speed * albatross.speed)); // Factor is stronger if flying more directly with wind
    }

    if (altitudeFactor > 0.1) { // Only gain if there's a significant strategic advantage
        let gain = ENERGY_GAIN_DYNAMIC_FACTOR * wind.speed * altitudeFactor;
        albatross.energy += gain;
        albatross.energy = Math.min(100, albatross.energy);
        if (lastEnergyGainType !== 'dynamic') {
             showEnergyGainIndicator("💨 דאייה דינמית! צובר אנרגיה");
             lastEnergyGainType = 'dynamic';
         }
    } else if (!isInThermal && lastEnergyGainType === 'dynamic') {
         lastEnergyGainType = null; // Reset if conditions no longer met
    }


    // Simulate energy loss from maneuvering and basic existence
    albatross.energy -= ENERGY_DECAY_RATE;
    albatross.energy = Math.max(0, albatross.energy);

     // Simulate flapping if energy is very low and not gaining energy naturally
     if (albatross.energy < 10 && !isInThermal && altitudeFactor < 0.1 && Math.random() < 0.05) {
         // Small upward impulse from flapping
         totalAy -= 0.3;
         albatross.energy -= 1; // Significant energy cost for flapping
         albatross.energy = Math.max(0, albatross.energy);
          // Maybe add a visual flap cue? (Too complex for this pass, stick to energy bar)
     }


    // Update velocity
    albatross.vx += totalAx;
    albatross.vy += totalAy;

    // Update position
    albatross.x += albatross.vx;
    albatross.y += albatross.vy;

    // Boundary checks (keep albatross within bounds with a small margin)
    const margin = 20;
    albatross.x = Math.max(margin, Math.min(canvas.width - margin, albatross.x));
    albatross.y = Math.max(margin, Math.min(canvas.height - margin, albatross.y));

    // If hit boundary, damp velocity to prevent sticking
    if (albatross.x <= margin || albatross.x >= canvas.width - margin) albatross.vx *= 0.8;
    if (albatross.y <= margin || albatross.y >= canvas.height - margin) albatross.vy *= 0.8;


    // Update speed and direction after movement
    let currentSpeed = Math.sqrt(albatross.vx * albatross.vx + albatross.vy * albatross.vy);
    if (currentSpeed > 0.5) { // Avoid direction changes when almost stationary
        albatross.direction = Math.atan2(albatross.vy, albatross.vx);
        // Smooth visual banking angle based on turn rate
        let targetBanking = (albatross.direction - albatross.angle) * 10; // Proportional to angle change
         albatross.banking = albatross.banking * 0.9 + targetBanking * 0.1; // Smooth banking
         albatross.angle = albatross.direction; // Update visual angle towards direction
    } else {
         albatross.banking *= 0.9; // Reduce banking when still
    }
     albatross.speed = currentSpeed;


    // Store path
    albatross.path.push({ x: albatross.x, y: albatross.y, energy: albatross.energy }); // Store energy with path point
    // Limit path length
    if (albatross.path.length > 800) { // Keep a longer trail
      albatross.path.shift();
    }

    // Update total distance
    totalDistance += albatross.speed * DISTANCE_SCALE / 60; // Rough distance based on speed per frame (assuming ~60fps)
    distanceCounter.textContent = `מרחק: ${totalDistance.toFixed(1)} ק"מ`;


    // Update energy display
    updateEnergyDisplay();
  }

    function showEnergyGainIndicator(text) {
        energyGainIndicator.textContent = text;
        energyGainIndicator.classList.remove('hidden');
        if (energyGainIndicatorTimeout) {
            clearTimeout(energyGainIndicatorTimeout);
        }
        energyGainIndicatorTimeout = setTimeout(() => {
            energyGainIndicator.classList.add('hidden');
        }, 1500); // Hide after 1.5 seconds
    }


  function updateEnergyDisplay() {
      const percentage = Math.round(albatross.energy);
      energyBar.style.width = `${percentage}%`;
      energyValueSpan.textContent = percentage;

      energyBarContainer.classList.remove('low-energy', 'medium-energy', 'high-energy');
      if (percentage < 20) {
          energyBarContainer.classList.add('low-energy');
      } else if (percentage < 50) {
          energyBarContainer.classList.add('medium-energy');
      } else {
          energyBarContainer.classList.add('high-energy');
      }
  }

  // Drawing function
  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas (background is CSS)

    // Draw wind indicators (subtle arrows)
    const arrowSize = 12;
    const gridX = 120;
    const gridY = 100;
    ctx.strokeStyle = 'rgba(0,0,0,0.2)'; // Very subtle
    ctx.lineWidth = 1;
    for (let i = gridX; i < canvas.width; i += gridX) {
      for (let j = gridY; j < canvas.height; j += gridY) {
        let windAngle = Math.atan2(wind.vy, wind.vx);
        let arrowLength = wind.speed * 0.8; // Scale arrow length by speed
        if (arrowLength > gridX/3) arrowLength = gridX/3; // Cap length
        if (arrowLength < 5) arrowLength = 0; // Don't draw tiny arrows
        if (arrowLength > 0) {
            ctx.beginPath();
            ctx.moveTo(i, j);
            ctx.lineTo(i + arrowLength * Math.cos(windAngle), j + arrowLength * Math.sin(windAngle));
            // Draw arrowhead
            ctx.lineTo(i + arrowLength * Math.cos(windAngle) - arrowSize * Math.cos(windAngle - Math.PI/7), j + arrowLength * Math.sin(windAngle) - arrowSize * Math.sin(windAngle - Math.PI/7));
            ctx.moveTo(i + arrowLength * Math.cos(windAngle), j + arrowLength * Math.sin(windAngle));
            ctx.lineTo(i + arrowLength * Math.cos(windAngle) - arrowSize * Math.cos(windAngle + Math.PI/7), j + arrowLength * Math.sin(windAngle) - arrowSize * Math.sin(windAngle + Math.PI/7));
            ctx.stroke();
        }
      }
    }


    // Draw thermals
    ctx.fillStyle = 'rgba(255, 165, 0, 0.15)'; // More translucent orange
    ctx.strokeStyle = 'rgba(255, 165, 0, 0.5)';
    ctx.lineWidth = 2;
    for (const thermal of thermals) {
      ctx.beginPath();
      // Add a subtle pulse animation effect by slightly changing radius or alpha over time
      const pulse = Math.sin(Date.now() / 500) * 5 + THERMAL_RADIUS; // Pulse between THERMAL_RADIUS-5 and THERMAL_RADIUS+5
      ctx.arc(thermal.x, thermal.y, pulse, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
       // Draw upward arrows inside thermal
       const numArrows = 6;
       const arrowSpacing = (Math.PI * 2) / numArrows;
       const arrowRadius = THERMAL_RADIUS * 0.6;
       ctx.strokeStyle = 'rgba(255, 165, 0, 0.8)';
       ctx.lineWidth = 2;
       const arrowSpeed = Date.now() / 200; // Animate arrow movement
       for(let k=0; k<numArrows; k++){
           let angle = (k * arrowSpacing + arrowSpeed) % (Math.PI * 2);
           let r = arrowRadius;
           let ax = thermal.x + r * Math.cos(angle);
           let ay = thermal.y + r * Math.sin(angle);
           ctx.beginPath();
           ctx.moveTo(ax, ay + 15); // Start slightly lower
           ctx.lineTo(ax, ay - 15); // Draw line upwards
           ctx.moveTo(ax, ay - 15); // Head
           ctx.lineTo(ax - 6, ay - 5);
           ctx.moveTo(ax, ay - 15);
           ctx.lineTo(ax + 6, ay - 5);
           ctx.stroke();
       }
    }

    // Draw albatross path with fading effect based on age/energy
    if (albatross.path.length > 1) {
        ctx.lineWidth = 2; // Thicker path
        ctx.lineCap = 'round'; // Round caps for smoother line ends
        ctx.lineJoin = 'round';
        for (let i = 1; i < albatross.path.length; i++) {
            ctx.beginPath();
            const p1 = albatross.path[i - 1];
            const p2 = albatross.path[i];
            const alpha = i / albatross.path.length; // Fade out older points
             // Optional: Color path based on energy
             let pathColor = `rgba(0, 0, 0, ${alpha * 0.6})`; // Black path, fading
             if (p2.energy < 30) pathColor = `rgba(255, 0, 0, ${alpha * 0.6})`; // Red when low energy
             else if (p2.energy < 60) pathColor = `rgba(255, 165, 0, ${alpha * 0.6})`; // Orange when medium energy

            ctx.strokeStyle = pathColor;
            ctx.moveTo(p1.x, p1.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
        }
    }


    // Draw albatross (more stylized shape)
    ctx.fillStyle = 'navy';
    ctx.strokeStyle = 'white'; // Outline for better visibility
    ctx.lineWidth = 1.5;
    ctx.save(); // Save current context state
    ctx.translate(albatross.x, albatross.y); // Move context to albatross position
    ctx.rotate(albatross.angle + albatross.banking * Math.PI / 180); // Rotate by direction + banking effect (convert banking degrees to radians)

    // Draw a simple stylized bird shape
    ctx.beginPath();
    ctx.moveTo(20, 0); // Nose (further forward)
    ctx.bezierCurveTo(15, -8, -5, -15, -15, -10); // Left wing (more curved)
    ctx.lineTo(-10, 0); // Tail (back to center)
    ctx.bezierCurveTo(-5, 15, 15, 8, 20, 0); // Right wing (symmetric curve)
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    // Optional: Draw a small eye?
    // ctx.fillStyle = 'white';
    // ctx.beginPath();
    // ctx.arc(15, -3, 2, 0, Math.PI * 2);
    // ctx.fill();


    ctx.restore(); // Restore context state

  }

  // Game loop
  function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
  }

  // Event listeners for controls
  windSpeedSlider.addEventListener('input', () => {
    windSpeedValueSpan.textContent = windSpeedSlider.value;
    updateWindVector();
  });

  windDirectionSlider.addEventListener('input', () => {
    windDirectionValueSpan.textContent = windDirectionSlider.value;
    updateWindVector();
  });

  addThermalButton.addEventListener('click', () => {
    // Remove existing thermals and add one new at a random position (avoid edges)
    thermals = [];
    thermals.push({
      x: Math.random() * (canvas.width - 2 * THERMAL_RADIUS) + THERMAL_RADIUS,
      y: Math.random() * (canvas.height - 2 * THERMAL_RADIUS) + THERMAL_RADIUS,
      isDragging: false,
      dragOffsetX: 0,
      dragOffsetY: 0,
    });
  });

  // Toggle explanation visibility
  showExplanationButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    showExplanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג הסבר מלא על סודות הדאייה';
  });

    // Variables for dragging
    let isCanvasDragging = false;
    let draggableElement = null;
    let dragStartX, dragStartY; // Mouse position at start of drag
    let elementStartX, elementStartY; // Element position at start of drag


    // Make Albatross and Thermal draggable
    canvas.addEventListener('mousedown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        // Check if click is near Albatross
        const dx = mouseX - albatross.x;
        const dy = mouseY - albatross.y;
        const distance = Math.sqrt(dx*dx + dy*dy);

        if (distance < 30) { // Increased click radius around Albatross
            isCanvasDragging = true;
            draggableElement = albatross;
            albatross.dragOffsetX = dx;
            albatross.dragOffsetY = dy;
            albatross.isDragging = true; // Flag for simulation logic
             canvas.style.cursor = 'grabbing';
        } else {
             // Check if click is near a Thermal
            for (const thermal of thermals) {
                const tdx = mouseX - thermal.x;
                const tdy = mouseY - thermal.y;
                const tdistance = Math.sqrt(tdx*tdx + tdy*tdy);
                if (tdistance < THERMAL_RADIUS) { // Click radius around Thermal
                    isCanvasDragging = true;
                    draggableElement = thermal;
                    thermal.dragOffsetX = tdx;
                    thermal.dragOffsetY = tdy;
                    thermal.isDragging = true; // Flag for simulation logic
                    canvas.style.cursor = 'grabbing';
                    break; // Only drag one element at a time
                }
            }
        }
    });

    let mouseX, mouseY; // Store current mouse position for drag update function
    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouseX = e.clientX - rect.left;
        mouseY = e.clientY - rect.top;

        if (isCanvasDragging && draggableElement) {
            // Update position based on drag
             draggableElement.x = mouseX - draggableElement.dragOffsetX;
             draggableElement.y = mouseY - draggableElement.dragOffsetY;

             // Keep dragged element within bounds
            const margin = draggableElement === albatross ? 20 : THERMAL_RADIUS;
            draggableElement.x = Math.max(margin, Math.min(canvas.width - margin, draggableElement.x));
            draggableElement.y = Math.max(margin, Math.min(canvas.height - margin, draggableElement.y));


            if (draggableElement === albatross) {
                 // Reset path and velocity when manually repositioning albatross
                 albatross.path = [{ x: albatross.x, y: albatross.y, energy: albatross.energy }];
                 albatross.vx = 0;
                 albatross.vy = 0;
                 albatross.speed = 0;
                 albatross.banking = 0; // Reset banking
            }
        }
    });

    canvas.addEventListener('mouseup', () => {
        if (isCanvasDragging && draggableElement) {
             draggableElement.isDragging = false; // Release drag flag
        }
        isCanvasDragging = false;
        draggableElement = null;
         canvas.style.cursor = 'grab';
    });

    canvas.addEventListener('mouseout', () => {
         if (isCanvasDragging && draggableElement) {
             draggableElement.isDragging = false; // Release drag flag
         }
         isCanvasDragging = false;
         draggableElement = null;
         canvas.style.cursor = 'grab';
    });


  // Initial setup
  updateWindVector(); // Set initial wind vector
  gameLoop(); // Start the simulation
</script>
```