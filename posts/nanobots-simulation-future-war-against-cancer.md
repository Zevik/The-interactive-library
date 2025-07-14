---
title: "הננו-רובוטים באים: סימולציה של מלחמת העתיד נגד הסרטן"
english_slug: nanobots-simulation-future-war-against-cancer
category: "מדעי החיים / רפואה"
tags:
  - ננוטכנולוגיה
  - סרטן
  - רפואה
  - סימולציה
  - ננו-רובוטים
  - רפואה ממוקדת
  - חינוך מדעי
---
<h1>הננו-רובוטים באים: סימולציה של מלחמת העתיד נגד הסרטן</h1>

<p>דמיינו צבא בלתי נראה של רובוטים מיניאטוריים, הזורם בתוך העורקים שלכם, מחפש, מזהה ומשמיד אך ורק תאים סרטניים חתרניים, מבלי לפגוע אפילו לרגע באף תא בריא. נשמע כמו מדע בדיוני? הצטרפו אלינו למסע ויזואלי לתוך זרם הדם ובחנו מקרוב את הפוטנציאל המדהים של ננו-רפואה במלחמה נגד הסרטן.</p>

<div id="simulation-area">
    <canvas id="bloodCanvas" width="900" height="350"></canvas>
    <div id="controls">
        <button id="injectNanobotsBtn" class="control-button">שגר ננו-רובוטים</button>
        <div class="control-group">
            <label for="nanobotDensity">צפיפות ננו-רובוטים:</label>
            <input type="range" id="nanobotDensity" name="nanobotDensity" min="1" max="15" value="7">
        </div>
        <div class="control-group">
            <label for="flowSpeed">מהירות זרימה:</label>
            <input type="range" id="flowSpeed" name="flowSpeed" min="0.8" max="4" step="0.1" value="2">
        </div>
        <button id="resetSimulationBtn" class="control-button">אפס סימולציה</button>
        <div id="status-area">
             <span id="cancerCellCount">תאים סרטניים נותרו: </span><span id="cancerCellNumber">?</span>
        </div>
    </div>
</div>

<style>
    body {
        font-family: 'Arial Hebrew', sans-serif;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: #333;
    }
    h1, h2, h3 {
        color: #0056b3;
        text-align: center;
        margin-bottom: 20px;
    }
    p {
        margin-bottom: 15px;
    }

    #simulation-area {
        margin: 30px auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 900px;
    }

    #bloodCanvas {
        display: block;
        margin: 0 auto 20px auto;
        border: 1px solid #ddd;
        border-radius: 8px;
        background: linear-gradient(to left, #ffdddd, #ffeeee); /* Subtle gradient for artery */
    }

    #controls {
        text-align: center;
        margin-top: 15px;
        padding: 10px;
        background-color: #e9ecef;
        border-radius: 8px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px; /* Space between control items */
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    #controls label {
        font-size: 0.9em;
        margin-bottom: 5px;
        color: #555;
    }

    #controls input[type="range"] {
        -webkit-appearance: none;
        appearance: none;
        width: 150px;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        -webkit-transition: .2s;
        transition: opacity .2s;
        border-radius: 5px;
    }

    #controls input[type="range"]:hover {
        opacity: 1;
    }

    #controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
    }

    #controls input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
    }

    .control-button {
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    .control-button:hover {
        background-color: #0056b3;
    }

     #status-area {
        font-size: 1em;
        color: #333;
        font-weight: bold;
        padding: 5px 10px;
        background-color: #fff;
        border-radius: 5px;
        border: 1px solid #ccc;
     }

     #win-message {
         font-size: 1.5em;
         color: green;
         font-weight: bold;
         text-align: center;
         margin-top: 20px;
         display: none; /* Hidden initially */
     }

    #toggleExplanationBtn {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    #toggleExplanationBtn:hover {
        background-color: #5a6268;
    }

    #explanation {
        border-top: 1px solid #ddd;
        padding-top: 30px;
        margin-top: 30px;
        display: none; /* Initially hidden */
        direction: rtl;
        text-align: right;
        font-family: 'Arial Hebrew', sans-serif;
        line-height: 1.8;
        color: #333;
    }
    #explanation h2 {
        text-align: center;
        margin-bottom: 25px;
        color: #0056b3;
    }
    #explanation h3 {
        margin-top: 25px;
        margin-bottom: 12px;
        color: #007bff;
        border-bottom: 1px dotted #ccc;
        padding-bottom: 3px;
    }
    #explanation p {
        margin-bottom: 15px;
    }

     /* Canvas drawing styles (handled in JS, but these define visual cues) */
     /* Cancer cell pulsing effect (handled partially in JS drawing + potential CSS animation, but JS is simpler here) */
</style>

<button id="toggleExplanationBtn">הצג הסבר מעמיק / הסתר</button>

<div id="explanation">
    <h2>מסע אל הלא נודע: כיצד ננו-רובוטים עשויים לשנות את המלחמה בסרטן</h2>

    <h3>האויב מבפנים: מבנה הסרטן והאתגר הטיפולי</h3>
    <p>סרטן אינו מחלה אחת, אלא אוסף מחלות המשותף להן הוא גידול בלתי מבוקר של תאים בעקבות שינויים גנטיים. תאים אלו רוכשים יכולות הרסניות: פלישה לרקמות סמוכות ואף נדידה דרך מערכת הדם והלימפה ליצירת גרורות באזורים מרוחקים. האתגר הגדול ברפואה המודרנית הוא להשמיד את התאים הסרטניים האגרסיביים מבלי לפגוע בתאים הבריאים והחיוניים לתפקוד הגוף.</p>

    <h3>המלכוד: טיפולים קיימים ותופעות לוואי</h3>
    <p>טיפולים קונבנציונליים כמו כימותרפיה והקרנות אכן יעילים בהשמדת תאים המתחלקים במהירות, אך טכניקות אלו אינן מבחינות באופן מושלם בין תאי סרטן לתאים בריאים בעלי קצב חלוקה גבוה (כמו תאי מח עצם, זקיקי שיער או רירית מערכת העיכול). חוסר ספציפיות זה הוא הגורם העיקרי לתופעות לוואי קשות כמו אנמיה, נשירת שיער, בחילות וזיהומים, הפוגעות קשות באיכות חיי המטופל ומגבילות לעיתים את מינון הטיפול.</p>

    <h3>לידתה של מהפכה: היכרות עם עולם הננו-רפואה</h3>
    <p>ננו-רפואה היא שדה פורץ דרך המגשר בין ננו-טכנולוגיה (מניפולציה הנדסית בקנה מידה של מיליארדית המטר) לעולם הרפואה. הרעיון המרכזי הוא לרתום את היכולות הייחודיות של חומרים ומכשירים זעירים אלו ליצירת גישות חדשות לאבחון, ניטור וטיפול במחלות ברזולוציה חסרת תקדים, ממש ברמת התא והמולקולה.</p>

    <h3>שליחים זעירים עם משימה קטלנית: קונספט הננו-רובוטים הרפואיים</h3>
    <p>ננו-רובוטים רפואיים (שאמנם עדיין נמצאים בחיתוליהם המחקריים) הם קונספט עתידי של מכשירים ננומטריים מתוכנתים לביצוע משימות ספציפיות בתוך הגוף. הם יכולים לשאת מטען טיפולי (כמו תרופה כימותרפית), לזהות סמנים מולקולריים, לנווט לרקמות חולות, ולשחרר את מטענם אך ורק היכן שנדרש. הסימולציה שלפניכם מציגה מודל פוטנציאלי לאופן שבו צבא ננו-רובוטים כזה יכול לפעול במלחמה ישירה וממוקדת נגד תאים סרטניים בתוך זרם הדם.</p>

    <h3>מנגנוני זיהוי והתבייתות: הצמד לנכון!</h3>
    <p>האופן שבו ננו-רובוטים אמורים להבחין בין תא סרטני לתא בריא הוא המפתח לטיפול ממוקד. תאי סרטן נוטים להציג על פני השטח שלהם סמנים מולקולריים (חלבונים, קולטנים) בכמות גדולה יותר או מסוג שונה לעומת תאים בריאים. הננו-רובוטים ניתנים לציפוי במולקולות קישור (כמו נוגדנים או ליגנדים אחרים) בעלות ספציפיות גבוהה לסמנים אלו. מפגש בין ננו-רובוט לסמן מתאים על פני תא סרטני גורם ל"התבייתות" והתחברות פיזית של הננו-רובוט לתא.</p>

    <h3>פגיעה מדויקת: שחרור ממוקד של המטען הקטלני</h3>
    <p>לאחר ההתחברות לתא הסרטני, הננו-רובוט יכול לשחרר את התרופה האצורה בו. שחרור זה אינו אקראי אלא מתוזמן ומבוקר. מנגנוני שחרור נפוצים כוללים תגובה לתנאים הסביבתיים הייחודיים של הגידול (כגון רמת pH נמוכה יותר, טמפרטורה גבוהה מעט, או נוכחות אנזימים מסוימים) או הפעלה באמצעות גירוי חיצוני (אור, שדה מגנטי, קול). ריכוז גבוה של התרופה המשוחררת באופן מבוקר, ממש בסמוך לתא הסרטני, מגביר דרמטית את יעילות הטיפול באותו תא ספציפי ומצמצם למינימום את החשיפה הסיסטמית של הגוף כולו לתרופה.</p>

    <h3>הבטחה לעתיד טוב יותר: יתרונות הננו-רפואה</h3>
    <p>היתרון הבולט ביותר של גישה מבוססת ננו-רובוטים הוא הפוטנציאל למיקוד טיפולי אולטימטיבי. היכולת לפגוע רק בתאים החולים יכולה להוביל להשמדה יעילה יותר של הגידול תוך מזעור דרמטי של תופעות הלוואי המערכתיות הקשות. בנוסף, ננו-רובוטים יכולים לשאת סוגי מטענים שונים (תרופות שונות, חומרים לדימות), מה שיאפשר אבחון וטיפול משולבים ואף ניטור ההתקדמות בזמן אמת.</p>

    <h3>הדרך עוד ארוכה: אתגרים ומכשולים</h3>
    <p>על אף הפוטנציאל העצום, הפיכת חזון הננו-רובוטים למציאות קלינית כרוכה באתגרים טכנולוגיים וביולוגיים משמעותיים: איך לנווט ביעילות בתוך מערכת כלי הדם הסבוכה? כיצד להבטיח שהרובוטים יזהו את כל התאים הסרטניים, כולל גרורות בודדות? האם הגוף לא ידחה וישמיד את הננו-רובוטים כתאים זרים? מה קורה לננו-רובוטים לאחר שסיימו את משימתם? בנוסף, ישנם אתגרים טכניים בייצור המוני ובקנה מידה ננומטרי, וכן סוגיות רגולטוריות ואתיות.</p>

    <h3>מבט אל האופק: מחקר ופיתוח מתמשך</h3>
    <p>המחקר בתחום נמצא בעיצומו וממשיך לחקור ולפתח חומרים ננומטריים חדשים בעלי יכולות משופרות, שילוב ננו-טכנולוגיה עם דימות, דרכים להתגבר על מחסומים ביולוגיים, ושימוש בננו-טכנולוגיה לאבחון מוקדם ומדויק. בעוד שננו-רובוטים אוטונומיים דמויי רובוטון עדיין רחוקים מיישום, חלקיקים ננומטריים נושאי תרופה (nanoparticles) כבר עושים את דרכם לשימוש קליני ומבשרים את המהפכה הננו-רפואית.</p>
</div>

<script>
    const canvas = document.getElementById('bloodCanvas');
    const ctx = canvas.getContext('2d');
    const injectBtn = document.getElementById('injectNanobotsBtn');
    const densitySlider = document.getElementById('nanobotDensity');
    const speedSlider = document.getElementById('flowSpeed');
    const resetBtn = document.getElementById('resetSimulationBtn');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationDiv = document.getElementById('explanation');
    const cancerCellNumberSpan = document.getElementById('cancerCellNumber');
    const winMessageDiv = document.getElementById('win-message'); // Need to add this div in HTML

    let redBloodCells = [];
    let cancerCells = [];
    let nanobots = [];
    let animationFrameId = null;
    let flowSpeed = parseFloat(speedSlider.value);
    let nanobotDensity = parseInt(densitySlider.value);
    let lastTime = 0;
    const flowDirection = -1; // Flow is right to left in RTL layout

    const settings = {
        redBloodCellCount: 60, // Slightly more cells
        cancerCellCount: 7, // More cancer cells for more targets
        redBloodCellRadius: 7,
        cancerCellRadius: 10, // Slightly smaller cancer cells
        nanobotSize: 2.5, // Slightly smaller nanobots
        nanobotTargetingRange: 60, // Increased targeting range
        nanobotSpeedFactor: 0.2, // Nanobots move faster towards target
        attachmentDistance: 6, // Attachment radius
        cancerCellHealth: 200, // Increased health for more visible damage process
        damagePerNanobot: 1.2, // Damage per nanobot per second (adjusted for delta time)
        flowInfluenceOnNanobot: 0.5 // How much flow affects nanobot movement when targeting (0 = none, 1 = full flow)
    };

    class Cell {
        constructor(x, y, radius, baseColor, type) {
            this.x = x;
            this.y = y;
            this.radius = radius;
            this.baseColor = baseColor;
            this.color = baseColor;
            this.type = type; // 'redblood' or 'cancer'
            this.attachedNanobots = 0;
            if (type === 'cancer') {
                this.initialHealth = settings.cancerCellHealth;
                this.health = this.initialHealth;
                this.isTargeted = false;
                this.isDestroyed = false; // New state
            }
        }

        draw() {
            if (this.isDestroyed) return; // Don't draw destroyed cells

            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();

            if (this.type === 'cancer') {
                 // Draw health bar
                 if (this.health < this.initialHealth) {
                     const barWidth = this.radius * 2;
                     const barHeight = 3;
                     const healthRatio = Math.max(0, this.health / this.initialHealth);
                     const currentBarWidth = barWidth * healthRatio;

                     ctx.fillStyle = '#eee'; // Background
                     ctx.fillRect(this.x - this.radius, this.y - this.radius - barHeight - 2, barWidth, barHeight);

                     ctx.fillStyle = healthRatio > 0.5 ? '#28a745' : (healthRatio > 0.2 ? '#ffc107' : '#dc3545'); // Green, Yellow, Red
                     ctx.fillRect(this.x - this.radius, this.y - this.radius - barHeight - 2, currentBarWidth, barHeight);

                     ctx.strokeStyle = '#555';
                     ctx.strokeRect(this.x - this.radius, this.y - this.radius - barHeight - 2, barWidth, barHeight);
                 }

                // Draw target outline
                if (this.isTargeted && this.health > 0) {
                     ctx.strokeStyle = 'rgba(255, 0, 0, 0.8)';
                     ctx.lineWidth = 2;
                     ctx.beginPath();
                     ctx.arc(this.x, this.y, this.radius + 3, 0, Math.PI * 2);
                     ctx.stroke();
                }
            }
        }

        update(deltaTime) {
            if (this.isDestroyed) return;

            this.x += flowSpeed * flowDirection * deltaTime * 30; // Adjust speed based on flow

            // Loop around if it goes off screen
             if (flowDirection === -1) { // Flowing right to left
                 if (this.x + this.radius < 0) {
                     this.x = canvas.width + this.radius;
                      // Reset health/state if it's a cancer cell and wrapped around
                     if (this.type === 'cancer') {
                         this.health = this.initialHealth;
                         this.color = this.baseColor;
                         this.isDestroyed = false;
                         this.isTargeted = false; // Reset targeting
                     }
                 }
             } else { // Flowing left to right (not current direction but good for robustness)
                  if (this.x - this.radius > canvas.width) {
                     this.x = -this.radius;
                      if (this.type === 'cancer') {
                         this.health = this.initialHealth;
                         this.color = this.baseColor;
                         this.isDestroyed = false;
                         this.isTargeted = false; // Reset targeting
                     }
                 }
             }


            if (this.type === 'cancer') {
                // Check if health is depleted
                if (this.health <= 0 && !this.isDestroyed) {
                    this.health = 0;
                    this.color = 'rgba(128, 128, 128, 0.5)'; // Indicate it's 'destroyed' visually
                    this.isDestroyed = true;
                    // Nanobots targeting this cell will lose their target
                    nanobots.forEach(nb => {
                        if (nb.targetCell === this) {
                            nb.targetCell = null;
                        }
                    });
                    updateCancerCellCount();
                }
            }
        }
    }

    class Nanobot {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            this.size = settings.nanobotSize;
            this.baseColor = '#007bff'; // Bright blue
            this.attackingColor = '#dc3545'; // Red when attacking
            this.color = this.baseColor;
            this.targetCell = null; // The cancer cell it's targeting
        }

        draw() {
            ctx.beginPath();
            // Draw a small shape instead of just a circle? Triangle or diamond? Circle is safest with current size.
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();
            // Optional: Draw a small line indicating direction or 'tail'
            // ctx.fillRect(this.x - this.size, this.y - this.size, this.size*2, this.size*2); // Square alternative
        }

        update(deltaTime) {
            let closestCancer = null;
            let minDist = Infinity;

            // Find the closest living cancer cell within targeting range
            for (const cell of cancerCells) {
                if (!cell.isDestroyed) {
                    const dist = Math.sqrt(Math.pow(cell.x - this.x, 2) + Math.pow(cell.y - this.y, 2));
                    if (dist < settings.nanobotTargetingRange && dist < minDist) {
                        minDist = dist;
                        closestCancer = cell;
                    }
                }
            }
            this.targetCell = closestCancer; // Update target based on proximity and health

            if (this.targetCell) {
                // Mark target cell
                this.targetCell.isTargeted = true;

                // Move towards the target cell
                const dx = this.targetCell.x - this.x;
                const dy = this.targetCell.y - this.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < settings.attachmentDistance) {
                    // Attached to cell, stay close and apply damage
                    // Add some random jitter while attached
                    this.x = this.targetCell.x + (Math.random() - 0.5) * settings.attachmentDistance * 1.5;
                    this.y = this.targetCell.y + (Math.random() - 0.5) * settings.attachmentDistance * 1.5;
                    // Limit nanobots moving outside the artery visually - simplified
                     this.y = Math.max(this.size, Math.min(canvas.height - this.size, this.y));

                    this.targetCell.health -= settings.damagePerNanobot * deltaTime; // Apply damage over time
                    this.color = this.attackingColor; // Change color to indicate attack
                } else {
                    // Move towards target, also affected by flow
                    const moveX = dx / dist * settings.nanobotSpeedFactor * deltaTime * 100;
                    const moveY = dy / dist * settings.nanobotSpeedFactor * deltaTime * 100;

                    // Blend movement towards target with flow
                    this.x += (moveX * (1 - settings.flowInfluenceOnNanobot)) + (flowSpeed * flowDirection * deltaTime * 30 * settings.flowInfluenceOnNanobot);
                    this.y += moveY; // Flow doesn't affect Y movement in this model

                    this.color = this.baseColor; // Not attached/attacking yet
                }

            } else {
                // No target or target destroyed, just flow with blood
                 this.color = this.baseColor;
                 this.x += flowSpeed * flowDirection * deltaTime * 30;

                 // Limit nanobots moving outside the artery visually
                 this.y = Math.max(this.size, Math.min(canvas.height - this.size, this.y));

                 // Loop around if it goes off screen
                 if (flowDirection === -1) { // Flowing right to left
                     if (this.x + this.size < 0) {
                        this.x = canvas.width + this.size;
                         // If wrapped, potentially scan for new targets on arrival? Or just keep flowing.
                         // Keeping flowing is simpler.
                     }
                 } else { // Flowing left to right
                      if (this.x - this.size > canvas.width) {
                         this.x = -this.size;
                      }
                 }
            }
        }
    }


    function initSimulation() {
        stopSimulation(); // Stop any existing animation

        redBloodCells = [];
        cancerCells = [];
        nanobots = [];
        lastTime = 0; // Reset time

        // Create blood cells
        for (let i = 0; i < settings.redBloodCellCount; i++) {
            redBloodCells.push(new Cell(
                Math.random() * canvas.width,
                Math.random() * canvas.height,
                settings.redBloodCellRadius,
                '#d62828', // Deeper red
                'redblood'
            ));
        }

        // Create cancer cells
        for (let i = 0; i < settings.cancerCellCount; i++) {
            cancerCells.push(new Cell(
                 Math.random() * canvas.width * 0.6 + canvas.width * 0.2, // Closer to center initially
                Math.random() * canvas.height * 0.6 + canvas.height * 0.2,
                settings.cancerCellRadius,
                '#ff8c00', // Vibrant orange
                'cancer'
            ));
        }

        updateCancerCellCount(); // Update display
        if (winMessageDiv) winMessageDiv.style.display = 'none'; // Hide win message

        startSimulation(); // Start animation loop
    }

    function injectNanobots() {
         if (nanobots.length > nanobotDensity * 20) return; // Limit total nanobots
        const numToInject = nanobotDensity * 5; // Inject based on density setting
        for (let i = 0; i < numToInject; i++) {
            // Inject from the right side (start of the artery relative to flow)
            // Distribute them slightly vertically
            nanobots.push(new Nanobot(canvas.width - 20 - Math.random()*20, Math.random() * (canvas.height - settings.nanobotSize*2) + settings.nanobotSize));
        }
    }

    function updateCancerCellCount() {
        const remaining = cancerCells.filter(cell => !cell.isDestroyed).length;
        cancerCellNumberSpan.textContent = remaining;
        if (remaining === 0) {
             stopSimulation();
             if (winMessageDiv) winMessageDiv.style.display = 'block';
             // Optional: Trigger animation or visual effect for win state
        }
    }

    function drawSimulation(deltaTime) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // Background is handled by canvas CSS or initial fill if needed

        // Reset targeting visual state for cancer cells at the start of the draw cycle
        cancerCells.forEach(cell => {
            if (!cell.isDestroyed) cell.isTargeted = false;
        });

        // Update and draw cells
        // Draw non-cancer cells first
        redBloodCells.forEach(cell => {
            cell.update(deltaTime);
            cell.draw();
        });

         // Draw cancer cells (living ones first, then destroyed ones last if still in array)
        cancerCells.filter(cell => !cell.isDestroyed).forEach(cell => {
            cell.update(deltaTime);
            cell.draw();
        });
         cancerCells.filter(cell => cell.isDestroyed).forEach(cell => {
             // Destroyed cells might have a fading animation or shrink
             cell.update(deltaTime); // Still update position if they flow
             cell.draw(); // Draw their destroyed state
         });


        // Update and draw nanobots
        nanobots.forEach(nano => {
            nano.update(deltaTime);
            nano.draw();
        });
    }


    function update(currentTime) {
        if (!lastTime) lastTime = currentTime;
        const deltaTime = (currentTime - lastTime) / 1000; // Delta time in seconds
        lastTime = currentTime;

        drawSimulation(deltaTime);

        animationFrameId = requestAnimationFrame(update);
    }

    function startSimulation() {
         if (!animationFrameId) { // Prevent multiple loops
            lastTime = 0; // Reset time on start
            animationFrameId = requestAnimationFrame(update);
         }
    }

     function stopSimulation() {
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
             animationFrameId = null;
         }
     }

    // Event Listeners
    injectBtn.addEventListener('click', injectNanobots);

    densitySlider.addEventListener('input', (event) => {
        nanobotDensity = parseInt(event.target.value);
    });

    speedSlider.addEventListener('input', (event) => {
        flowSpeed = parseFloat(event.target.value);
    });

    resetBtn.addEventListener('click', () => {
        initSimulation(); // This also starts the simulation
    });

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק';
    });


    // Add the win message div dynamically or ensure it's in the HTML
    // For simplicity, let's assume it's added in HTML if not present.
    // Example of adding dynamically if needed:
    // if (!winMessageDiv) {
    //     winMessageDiv = document.createElement('div');
    //     winMessageDiv.id = 'win-message';
    //     winMessageDiv.textContent = 'כל התאים הסרטניים הושמדו! משימה הושלמה.';
    //     winMessageDiv.style.cssText = 'font-size: 1.5em; color: green; font-weight: bold; text-align: center; margin-top: 20px; display: none;';
    //     simulationArea.parentNode.insertBefore(winMessageDiv, simulationArea.nextSibling);
    // }


    // Initial setup
    initSimulation(); // Initialize and start on page load

</script>
---