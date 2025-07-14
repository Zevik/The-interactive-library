---
title: "סודות הקרח: מסע אל לב התבניות המופלאות של קרחונים"
english_slug: glacier-patterns-how-ice-languages-form
category: "מדעי כדור הארץ"
tags:
  - קרחונים
  - קרח
  - דפוסים
  - בקיעים
  - זרימה
  - גיאולוגיה
  - פיזיקה
---
# סודות הקרח: מסע אל לב התבניות המופלאות של קרחונים

דמיינו נהר עצום, עשוי קרח. הוא זורם באיטיות בלתי נתפסת, מעצב את הנוף סביבו בכוח אדיר. כשאנו מביטים מקרוב על פני השטח שלו, אנו מגלים תבניות מורכבות של בקיעים, קמטים וצורות גיאומטריות. האם אלו סימנים מקריים, או שהם למעשה "השפה" של הקרחון, סיפור חרוט על פניו שמגלה לנו את הכוחות הפיזיקליים האדירים הפועלים בתוכו? בואו נחקור יחד.

<div class="interactive-app">
    <h2>סימולציית דינמיקת קרחון: צפו בתבניות נגלות</h2>
    <p class="app-intro">שחקו עם המחוונים למטה וראו כיצד שינויים בסביבה משפיעים על שדות המתח והלחץ בקרחון, וכיצד אלו "מציירים" את דפוסי הבקיעים האופייניים.</p>

    <div class="controls">
        <div class="control-group">
            <label for="slope">שיפוע המדרון:</label>
            <input type="range" id="slope" name="slope" min="0" max="15" value="5" step="0.5">
            <span id="slopeValue">5°</span>
            <p class="control-hint">מדרון תלול יותר = זרימה מהירה יותר.</p>
        </div>

        <div class="control-group">
             <label for="obstacleSize">גודל מכשול תת-קרחוני:</label>
             <input type="range" id="obstacleSize" name="obstacleSize" min="0" max="60" value="0" step="5">
             <span id="obstacleSizeValue">אין מכשול</span>
             <p class="control-hint">בליטה גדולה בקרקעית משנה את דפוס הזרימה.</p>
        </div>

        <div class="control-group" id="obstaclePositionGroup">
             <label for="obstaclePosition">מיקום מכשול (לאורך):</label>
             <input type="range" id="obstaclePosition" name="obstaclePosition" min="0" max="100" value="50" step="1">
             <span id="obstaclePositionValue">50% לאורך</span>
             <p class="control-hint">היכן ממוקם המכשול במסלול הקרחון?</p>
        </div>

        <div class="control-group">
            <label for="iceViscosity">צמיגות הקרח:</label>
            <input type="range" id="iceViscosity" name="iceViscosity" min="1" max="10" value="5">
            <span id="iceViscosityValue">בינונית</span>
             <p class="control-hint">קרח "רך" (צמיגות נמוכה) נסדק בקלות, קרח "קשה" פחות.</p>
        </div>
    </div>

    <div class="canvas-container">
        <canvas id="glacierCanvas" width="800" height="400"></canvas>
    </div>
    <p class="simulation-notes">
        <span class="stress-indicator-tension">אדום</span> מציין אזורי מתיחה (שם הקרח "נמתח").
        <span class="stress-indicator-compression">כחול</span> מציין אזורי לחיצה (שם הקרח "נדחס").
        <span class="stress-indicator-shear">ירוק-צהוב</span> מציין אזורי גזירה (שם שכבות הקרח מחליקות זו על גבי זו).
        <br>
        הקווים הלבנים מסמלים בקיעים (Crevasses) שנוצרים היכן שהמתח עולה על חוזק הקרח.
        צפו כיצד צבעי המתח והבקיעים משתנים עם הפרמטרים!
    </p>
     <p class="simulation-tip"><strong>טיפ לחקירה:</strong> נסו להוסיף מכשול (גודל > 0) ולשנות את מיקומו. שימו לב לדפוסי הבקיעים המורכבים שנוצרים סביבו. </p>
</div>

<button id="explanation-button">הצגת/הסתרת הסיפור שמאחורי התבניות</button>

<div id="glacier-explanation">
    <h2>הסיפור שמאחורי התבניות: כיצד הקרח חורט את סודותיו?</h2>

    <h3>מפלצתו הזורמת של הטבע: הכירו את הקרחון</h3>
    קרחון הוא לא רק גוש קרח ענק. הוא מערכת דינמית וחיה (במובן הגיאולוגי, כמובן) שזורמת בכוח אדיר ואיטי. הוא נולד מהצטברות אינסופית של שלג שנדחס לקרח מוצק לאורך אלפי שנים. הזרימה שלו למורד המדרון, גם אם בקצב של סנטימטרים או מטרים ביום, היא שמעצבת עמקים, פיורדים ונופים עוצרי נשימה. הזרימה הזו מתרחשת בשני אופנים עיקריים:
    <ul>
        <li>**זחילה פלסטית:** עומס הקרח העצום גורם לקרח, שהתנהגותו קרובה לנוזל צמיג תחת לחץ קיצוני, "לזחול" ולהתעוות לאט.</li>
        <li>**החלקה בבסיס:** אם יש שכבת מים בין הקרחון לקרקע (בגלל לחץ שמוריד את נקודת הקיפאון או חום פנימי), הקרחון יכול פשוט להחליק על כרית המים הזו. זהו מנגנון שיכול להאיץ משמעותית את הזרימה.</li>
    </ul>
    מהירות הזרימה תלויה בשיפוע, עובי הקרחון, טמפרטורתו וגם בצורת הקרקע שמתחתיו.

    <h3>הצלקות על פני הענק הלבן: הבקיעים (Crevasses)</h3>
    הבקיעים העמוקים שחוצים את פני הקרחון הם לא סתם סדקים. הם "פצעים" שנוצרים בשכבה העליונה והשבירה של הקרח (עד עומק של כ-30-50 מטר), כאשר הכוחות הפועלים על הקרח חזקים מדי. חשבו על זה: קרח חזק בלחיצה (קשה למחוץ אותו) אך חלש במתיחה (קל יחסית לשבור אותו כשמותחים). לכן, בקיעים נפתחים היכן שהקרחון נמתח.

    <h3>ריקוד הכוחות הבלתי נראה: שדות הלחץ, המתיחה והגזירה</h3>
    הזרימה הלא אחידה של הקרחון יוצרת בתוכו "שדות אנרגיה" בלתי נראים של כוחות:
    <ul>
        <li>**מתח מתיחה:** כוח המנסה למתוח את הקרח. הוא שולט באזורים בהם הקרח מאיץ (למשל, כשהמדרון מתחדד) או נפרש. בקיעים רוחביים נפתחים בדיוק בניצב לכיוון המתיחה המרבי.</li>
        <li>**לחץ לחיצה:** כוח המנסה לדחוס את הקרח. מופיע באזורים בהם הקרח מאיט (למשל, בסוף מדרון תלול או מאחורי מכשול). כאן בקיעים נסגרים, ולעיתים נוצרים רכסי לחץ.</li>
        <li>**כוחות גזירה:** פועלים במקביל לשכבות הקרח, גורמים להן להחליק אחת על השנייה. חזקים בשולי הקרחון (החיכוך עם דפנות העמק) וסביב מכשולים. גורמים לבקיעים אורכיים או אלכסוניים.</li>
    </ul>

    <h3>פסיפס הבקיעים: מפה חיה של דינמיקת הקרחון</h3>
    הצורות והכיוונים של הבקיעים הם כמו מפה המוצפנת על פני הקרח. הם מספרים לנו היכן וכיצד פועלים הכוחות העיקריים:
    <ul>
        <li>**בקיעים רוחביים:** רצועות סדקים בניצב לכיוון הזרימה, כמו מדרגות. נוצרים כשהקרחון נמתח במעבר מעל בליטה או שינוי שיפוע.</li>
        <li>**בקיעים אורכיים:** סדקים מקבילים לכיוון הזרימה. נוצרים כשקרחון מתרחב לרוחב או באזורי גזירה חזקים במיוחד.</li>
        <li>**בקיעים אלכסוניים/שוליים (En Échelon):** מערכים של סדקים קצרים ואלכסוניים בשולי הקרחון. תוצאה קלאסית של כוחות גזירה חזקים לאורך הדפנות.</li>
        <li>**דפוסים סבוכים:** סביב מכשולים תת-קרחוניים, הקרחון נאלץ לעקוף. זה יוצר אזור דחיסה לפני המכשול, מתיחה עזה מעליו ובמורדו, וגזירה חזקה בצדדים. התוצאה היא מערך מרהיב ומורכב של בקיעים מכל הסוגים.</li>
    </ul>

    <h3>מדוע זה חשוב לנו? מעבר ליופי</h3>
    הבנת דפוסי הבקיעים היא לא רק מרתקת מבחינה מדעית. זוהי דרך חשובה לעקוב אחר "בריאותו" והתנהגותו של הקרחון. שינויים בדפוסים יכולים להעיד על האצה או האטה בזרימה – מידע קריטי בעידן של שינויי אקלים והשפעתם על עליות מפלס הים. בנוסף, אזורים עתירי בקיעים (כמו "מפלי קרח" קפואים) מסוכנים ביותר למטיילים ומדענים, והבנת היווצרותם מאפשרת תכנון בטוח יותר. כל בקיע הוא רמז, כל תבנית היא סיפור – והקרחון ממשיך לחרוט את ההיסטוריה הדינמית שלו על פני השטח הלבנים.

</div>

<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #eef5f9;
        padding: 0 10px;
    }

    h1, h2, h3 {
        color: #0a3d62; /* Deep blue */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        margin-top: 30px;
        font-size: 2em;
    }

    .interactive-app {
        border: 1px solid #b0c4de; /* Light steel blue */
        padding: 25px;
        margin-bottom: 30px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .app-intro {
        text-align: center;
        margin-bottom: 25px;
        color: #555;
        font-size: 1.1em;
    }

    .controls {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #f0f8ff; /* Alice blue */
        border-radius: 8px;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .controls label {
        font-weight: bold;
        margin-bottom: 8px;
        color: #0a3d62;
    }

    .controls input[type="range"] {
        width: 100%;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 5px;
        margin-bottom: 5px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff; /* Primary blue */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #ffffff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #ffffff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .controls span {
        align-self: flex-end;
        font-size: 0.9em;
        color: #555;
        min-width: 80px; /* Give space for text */
        text-align: right;
    }

     .control-hint {
         font-size: 0.8em;
         color: #666;
         margin-top: 5px;
     }

    .canvas-container {
        text-align: center;
        margin-bottom: 20px;
        background-color: #e0f2f7; /* Very light blue */
        border-radius: 8px;
        overflow: hidden; /* Ensure canvas fits */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
    }

    #glacierCanvas {
        display: block;
        margin: 0 auto;
        background: linear-gradient(to bottom, #b3e5fc, #e1f5fe); /* Arctic blues */
    }

    .simulation-notes {
        font-size: 0.95em;
        color: #555;
        text-align: center;
        margin-bottom: 20px;
        padding-top: 15px;
        border-top: 1px dashed #ccc;
    }

     .simulation-tip {
        font-size: 0.95em;
        color: #0056b3;
        text-align: center;
        font-style: italic;
     }

    .stress-indicator-tension { color: #ff0000; font-weight: bold;}
    .stress-indicator-compression { color: #0000ff; font-weight: bold;}
    .stress-indicator-shear { color: #ffa500; font-weight: bold;} /* Orange for Shear */


    #explanation-button {
        display: block;
        margin: 25px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    #explanation-button:hover {
        background-color: #0056b3; /* Darker blue */
    }

    #explanation-button:active {
        transform: scale(0.98);
    }

    #glacier-explanation {
        display: none; /* Initially hidden */
        border-top: 2px solid #b0c4de; /* Light steel blue */
        padding-top: 25px;
        margin-top: 30px;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #glacier-explanation h2,
    #glacier-explanation h3 {
        color: #0a3d62;
        margin-top: 1.5em;
        margin-bottom: 1em;
    }

    #glacier-explanation ul {
        list-style: disc inside;
        margin-bottom: 1.5em;
    }

    #glacier-explanation li {
        margin-bottom: 0.8em;
    }

     /* Responsive adjustments */
    @media (max-width: 768px) {
        .controls {
            grid-template-columns: 1fr;
        }
         .controls span {
             align-self: flex-start;
             margin-top: -10px; /* Pull value closer to slider */
             margin-bottom: 5px;
         }
          .control-group {
              padding-bottom: 15px; /* Add space between groups */
              border-bottom: 1px dashed #eee;
          }
          .control-group:last-child {
              border-bottom: none;
              padding-bottom: 0;
          }
    }

</style>

<script>
    const canvas = document.getElementById('glacierCanvas');
    const ctx = canvas.getContext('2d');
    const slopeInput = document.getElementById('slope');
    const slopeValueSpan = document.getElementById('slopeValue');
    const obstacleSizeInput = document.getElementById('obstacleSize');
    const obstacleSizeValueSpan = document.getElementById('obstacleSizeValue');
    const obstaclePositionInput = document.getElementById('obstaclePosition');
    const obstaclePositionValueSpan = document.getElementById('obstaclePositionValue');
    const obstaclePositionGroup = document.getElementById('obstaclePositionGroup'); // To hide/show
    const iceViscosityInput = document.getElementById('iceViscosity');
    const iceViscosityValueSpan = document.getElementById('iceViscosityValue');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('glacier-explanation');

    // Simulation parameters
    const simulationWidth = canvas.width;
    const simulationHeight = canvas.height;
    const numStressPoints = 150; // More points for smoother stress visualization
    const maxCracks = 200; // Limit number of cracks
    const crackGrowthRate = 0.5; // How much cracks grow per frame
    const crackProbMultiplier = 0.0005; // Base probability for new cracks per point per frame

    let cracks = []; // Array to store crack objects {x, y, angle, length, type}
    let animationFrameId = null;

    // Map viscosity value to description
    const viscosityLabels = ['קשיחה מאוד', 'קשיחה', 'קצת קשיחה', 'בינונית-קשיחה', 'בינונית', 'בינונית-רכה', 'קצת רכה', 'רכה', 'רכה מאוד', 'נוזלית כמעט'];

    // Function to map stress values to colors (smoother transitions)
    function getStressColor(tension, compression, shear) {
        const maxStress = Math.max(tension, compression, shear);
        if (maxStress < 1) return 'rgba(0,0,0,0)'; // Below threshold

        const totalStress = tension + compression + shear;
        const r = tension / totalStress;
        const b = compression / totalStress;
        const g = shear / totalStress;

        // Blend colors: Red (tension), Blue (compression), Orange/Yellow (shear)
        // Let's use more specific hues: Red (0), Blue (240), Yellow (60) in HSL?
        // Or simpler RGB blending:
        let colorR = Math.min(255, r * 255 + g * 255 * 0.5); // Red + some yellow
        let colorG = Math.min(255, g * 255 * 0.8); // Primarily yellow/green
        let colorB = Math.min(255, b * 255); // Blue

         // Adjust intensity based on total stress magnitude
        const intensity = Math.min(1, maxStress / 10); // Max stress of 10 is full intensity
        colorR = Math.floor(colorR * intensity);
        colorG = Math.floor(colorG * intensity);
        colorB = Math.floor(colorB * intensity);


        return `rgba(${colorR}, ${colorG}, ${colorB}, ${intensity * 0.6 + 0.1})`; // Alpha between 0.1 and 0.7
    }


    // Function to simulate stress and draw
    function drawGlacier(time) {
        ctx.clearRect(0, 0, simulationWidth, simulationHeight);

        // Draw glacier background (dynamic gradient based on slope)
        const slope = parseFloat(slopeInput.value);
        const baseColor = `hsl(210, 60%, ${98 - slope * 0.8}%)`; // Lighter, more saturated blue at higher slope
        const peakColor = `hsl(210, 40%, ${85 - slope * 1.5}%)`; // Deeper blue at lower slope
        const gradient = ctx.createLinearGradient(0, 0, 0, simulationHeight);
        gradient.addColorStop(0, baseColor); // Top
        gradient.addColorStop(0.6 + slope * 0.02, peakColor); // Mid
        gradient.addColorStop(1, `hsl(210, 30%, ${70 - slope * 0.5}%)`); // Bottom, darker blue
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, simulationWidth, simulationHeight);

        // Simulate Stress Fields and Draw Patterns
        const obstacleSize = parseFloat(obstacleSizeInput.value);
        const obstaclePosition = parseFloat(obstaclePositionInput.value) / 100; // 0-1
        const iceViscosity = parseFloat(iceViscosityInput.value); // 1-10 (lower = more brittle, more cracks)

        const baseFlowSpeed = 0.1 + slope * 0.08; // Flow increases with slope
        const brittleness = 12 - iceViscosity; // Higher brittleness means more cracks

        const obstacleX = obstaclePosition * simulationWidth;
        const obstacleRadius = obstacleSize * 0.8; // Scale obstacle size to canvas

        // Draw stress zones and generate new cracks
        // Simulate stress over a grid for smoother visualization
        const gridSizeX = 40; // Fewer points for drawing stress colors
        const gridSizeY = 20;
        const cellWidth = simulationWidth / gridSizeX;
        const cellHeight = simulationHeight / gridSizeY;

        for (let i = 0; i < gridSizeX; i++) {
            for (let j = 0; j < gridSizeY; j++) {
                const x = i * cellWidth + cellWidth/2;
                const y = j * cellHeight + cellHeight/2;

                let tension = (slope / 15) * 4; // Base tension from slope
                let compression = (1 - (slope / 15)) * 2; // Base compression
                let shear = 0;

                // Obstacle effect
                if (obstacleSize > 0) {
                     const dx = x - obstacleX;
                     const dy = y - simulationHeight * 0.8; // Assume obstacle is near the bottom
                     const distToObstacleCenter = Math.sqrt(dx * dx + dy * dy);
                     const influenceRadius = obstacleRadius * 2.5;

                     if (distToObstacleCenter < influenceRadius) {
                         const influence = (influenceRadius - distToObstacleCenter) / influenceRadius; // 1 at center, 0 at edge

                         // Simplified flow field around obstacle
                         // Before obstacle: compression
                         if (x < obstacleX - obstacleRadius/2) {
                             const approachInfluence = Math.max(0, (obstacleX - obstacleRadius/2 - x) / (simulationWidth * 0.2)); // Influence increases closer to obstacle front
                             compression += influence * 8 * approachInfluence;
                             tension = Math.max(0, tension - influence * 4 * approachInfluence);
                         }
                         // After obstacle: tension
                         if (x > obstacleX + obstacleRadius/2) {
                              const retreatInfluence = Math.max(0, (x - (obstacleX + obstacleRadius/2)) / (simulationWidth * 0.3)); // Influence decreases away from obstacle back
                             tension += influence * 10 * retreatInfluence;
                             compression = Math.max(0, compression - influence * 5 * retreatInfluence);
                         }

                         // Sides of obstacle: shear
                         const sideInfluence = Math.max(0, influence - Math.abs(dx/influenceRadius)); // Strongest influence on the sides
                         shear += influence * 7 * (Math.abs(dx) / (influenceRadius/2)) ; // Shear increases with distance *sideways* from center flow line

                          // Local compression directly over/behind obstacle
                         if (distToObstacleCenter < obstacleRadius * 1.2 && x > obstacleX - obstacleRadius/2) {
                             compression += influence * 5;
                             tension = Math.max(0, tension - influence * 3);
                         }
                     }
                }

                // Draw stress color
                ctx.fillStyle = getStressColor(tension, compression, shear);
                ctx.fillRect(i * cellWidth, j * cellHeight, cellWidth, cellHeight);

                 // Crack generation probability (simplified, based on dominant stress exceeding threshold)
                 const threshold = 3; // Stress threshold to create a crack
                 let crackProbability = 0;
                 let crackAngle = 0; // Angle of the crack relative to horizontal
                 let stressMagnitude = 0;


                if (tension > threshold * (brittleness/10)) {
                    crackProbability = (tension - threshold) * crackProbMultiplier * brittleness * 0.5;
                    crackAngle = Math.PI / 2; // Transverse cracks are vertical (perpendicular to flow=horizontal)
                    stressMagnitude = tension;
                } else if (shear > threshold * (brittleness/10) * 0.8) { // Shear needs lower threshold for cracks
                     crackProbability = (shear - threshold * 0.8) * crackProbMultiplier * brittleness * 0.8;
                     // Angle depends on the local flow/shear direction. Simplified: diagonal around obstacles
                     if (obstacleSize > 0) {
                          const dx = x - obstacleX;
                          const dy = y - simulationHeight * 0.8;
                          const distToObstacleCenter = Math.sqrt(dx * dx + dy * dy);
                          const influenceRadius = obstacleRadius * 2.5;
                           if (distToObstacleCenter < influenceRadius) {
                                const angleAroundObstacle = Math.atan2(dy, dx); // Angle from obstacle center
                                crackAngle = angleAroundObstacle + Math.PI/2 ; // Perpendicular to radial direction, roughly
                                // Adjust angle slightly for en-echelon effect, and align with shear direction
                                crackAngle += (Math.random() - 0.5) * Math.PI/8; // Random variation
                                if (x < obstacleX) crackAngle = Math.PI - crackAngle; // Mirror on upstream side
                                stressMagnitude = shear;
                           } else { // Far from obstacle, longitudinal cracks from general shear
                               crackAngle = 0; // Longitudinal cracks are horizontal (parallel to flow)
                               crackProbability *= 0.5; // Less likely far from obstacle
                               stressMagnitude = shear * 0.5;
                           }
                     } else { // No obstacle, general longitudinal cracks
                           crackAngle = 0; // Horizontal
                           crackProbability *= 0.3; // Less likely without specific shear zones
                            stressMagnitude = shear * 0.5;
                     }
                }


                 // Generate new crack based on probability
                if (Math.random() < crackProbability && cracks.length < maxCracks) {
                    cracks.push({
                        x: x + (Math.random() - 0.5) * cellWidth, // Random position within cell
                        y: y + (Math.random() - 0.5) * cellHeight,
                        angle: crackAngle,
                        length: 1, // Start small
                        type: tension > shear ? 'tension' : 'shear',
                        birthTime: time // Track when it was created
                    });
                }
            }
        }

         // Animate existing cracks
         const currentTime = time;
         cracks = cracks.filter(crack => currentTime - crack.birthTime < 1000); // Remove old cracks (arbitrary lifespan)

         ctx.strokeStyle = 'white';
         ctx.lineWidth = 2;
         ctx.lineCap = 'round'; // Rounded ends for cracks

         cracks.forEach(crack => {
             // Grow crack based on its type and local stress? Or just grow over time?
             // Simple growth over time:
             crack.length += crackGrowthRate;

             // Make cracks slightly curved? (More complex, maybe skip for this iteration)

             // Draw crack segment (simplified)
             const halfLength = crack.length / 2;
             const dx = halfLength * Math.cos(crack.angle);
             const dy = halfLength * Math.sin(crack.angle);

             ctx.beginPath();
             ctx.moveTo(crack.x - dx, crack.y - dy);
             ctx.lineTo(crack.x + dx, crack.y + dy);
             ctx.stroke();
         });


         // Draw obstacle representation (more realistic shape)
        if (obstacleSize > 0) {
            ctx.fillStyle = '#4a4a4a'; // Dark grey rock color
            ctx.beginPath();
            // Draw an oval slightly flattened at the top
            ctx.ellipse(obstacleX, simulationHeight * 0.85, obstacleRadius, obstacleRadius * 0.6, 0, 0, 2 * Math.PI);
            ctx.fill();
             // Add some texture/shading? (Complex for canvas)

             // Add text for the obstacle
            ctx.fillStyle = '#222';
            ctx.font = '14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('מכשול תת-קרחוני', obstacleX, simulationHeight * 0.85 - obstacleRadius * 0.6 - 10);

             // Show obstacle position control only if size > 0
             obstaclePositionGroup.style.display = 'flex';

        } else {
             obstaclePositionGroup.style.display = 'none'; // Hide position control if no obstacle
        }


        // Add dynamic flow direction indicator
         ctx.strokeStyle = '#333';
         ctx.lineWidth = 2;
         ctx.setLineDash([8, 6]); // Dashed line
         const arrowLength = 50 + baseFlowSpeed * 200;
         const arrowStartX = 40;
         const arrowStartY = simulationHeight * 0.5;
         ctx.beginPath();
         ctx.moveTo(arrowStartX, arrowStartY);
         ctx.lineTo(arrowStartX + arrowLength, arrowStartY);
         ctx.lineTo(arrowStartX + arrowLength - 15, arrowStartY - 8);
         ctx.moveTo(arrowStartX + arrowLength, arrowStartY);
         ctx.lineTo(arrowStartX + arrowLength - 15, arrowStartY + 8);
         ctx.stroke();
         ctx.setLineDash([]); // Reset dash

         ctx.fillStyle = '#333';
         ctx.font = '16px Arial';
         ctx.textAlign = 'left';
         ctx.fillText('כיוון הזרימה', arrowStartX, arrowStartY - 20);


         // Request the next frame
         animationFrameId = requestAnimationFrame(drawGlacier);
    }

    // Update values and restart animation
    function updateSimulation() {
        slopeValueSpan.textContent = `${parseFloat(slopeInput.value).toFixed(1)}°`;
        obstacleSizeValueSpan.textContent = obstacleSizeInput.value > 0 ? `${obstacleSizeInput.value} יח'` : 'אין מכשול';
        obstaclePositionValueSpan.textContent = `${obstaclePositionInput.value}% לאורך`;
        iceViscosityValueSpan.textContent = viscosityLabels[parseInt(iceViscosityInput.value) - 1];

        // Reset cracks when parameters change significantly
        cracks = []; // Clear existing cracks for a fresh start

        // Stop any existing animation frame
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        // Start a new animation loop
        animationFrameId = requestAnimationFrame(drawGlacier);
    }

     // Initial check for obstacle visibility
    if (parseFloat(obstacleSizeInput.value) === 0) {
        obstaclePositionGroup.style.display = 'none';
    } else {
         obstaclePositionGroup.style.display = 'flex';
    }


    // Event Listeners for controls
    slopeInput.addEventListener('input', updateSimulation);
    obstacleSizeInput.addEventListener('input', updateSimulation);
    obstaclePositionInput.addEventListener('input', updateSimulation);
    iceViscosityInput.addEventListener('input', updateSimulation);


    // Toggle explanation visibility
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתרת הסיפור שמאחורי התבניות' : 'הצגת/הסתרת הסיפור שמאחורי התבניות';
    });

    // Initial draw and start animation
    updateSimulation();

    // Ensure animation stops if page is hidden
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        if (animationFrameId) {
          cancelAnimationFrame(animationFrameId);
          animationFrameId = null;
        }
      } else {
        if (!animationFrameId) {
          updateSimulation(); // Restart animation
        }
      }
    });


</script>
```