---
title: "השד של מקסוול: האם אפשר לנצח את האנטרופיה?"
english_slug: maxwells-demon-breaking-physics-laws
category: "פיזיקה"
tags: [תרמודינמיקה, אנטרופיה, ניסוי מחשבתי, החוק השני של התרמודינמיקה, השד של מקסוול]
---
# השד של מקסוול: האם אפשר לנצח את האנטרופיה?

תארו לעצמכם יקום שבו בלגן רק הולך וגובר – זהו לב לבו של החוק השני של התרמודינמיקה, הקובע שהאנטרופיה (מידת אי-הסדר) במערכת סגורה תמיד שואפת למקסימום. אבל מה אם יצור זעיר ופיקח יכול היה להתערב, למיין חלקיקים, וליצור סדר מתוך הכאוס? גלו את ניסוי המחשבה האגדי שאתגר את עקרונות היסוד של הפיזיקה, והצית דיונים סוערים למעלה ממאה וחמישים שנה! הצטרפו לשד של מקסוול ובדקו בעצמכם האם אפשר באמת להערים על חוקי הטבע.

<div class="simulation-container">
    <div class="simulation-area">
        <canvas id="gasCanvas"></canvas>
        <div class="partition" id="partition"></div>
         <div class="gate" id="gate">
            <div class="gate-door"></div>
         </div>
        <div class="demon" id="demon">
            <span class="demon-icon">😈</span>
        </div>
    </div>
    <div class="controls">
        <button id="startButton">התחל מיון</button>
        <button id="stopButton">הפסק מיון</button>
        <button id="resetButton">אפס הכל</button>
    </div>
    <div class="metrics">
        <div class="side-metrics left-side">
            <h4>צד קר (שמאל)</h4>
            <p><span class="metric-label">מולקולות:</span> <span id="countLeft">0</span></p>
            <p><span class="metric-label">"טמפרטורה":</span> <span id="tempLeft">0.0</span></p>
        </div>
        <div class="side-metrics right-side">
            <h4>צד חם (ימין)</h4>
            <p><span class="metric-label">מולקולות:</span> <span id="countRight">0</span></p>
            <p><span class="metric-label">"טמפרטורה":</span> <span id="tempRight">0.0</span></p>
        </div>
        <div class="global-metrics">
             <h4>מערכת כוללת</h4>
             <p><span class="metric-label">הפרש "טמפרטורה" (אנטרופיה נאמדת):</span> <span id="tempDiff">0.0</span></p>
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: 'Heebo', sans-serif;
        margin: 30px auto;
        max-width: 550px;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        padding: 20px;
        box-sizing: border-box;
    }

    .simulation-area {
        position: relative;
        width: 500px;
        height: 300px;
        border: 2px solid #333;
        background: linear-gradient(to bottom, #e0f2f7, #b3e5fc); /* Softer, dynamic background */
        margin-bottom: 20px;
        overflow: hidden; /* Crucial for molecule confinement */
        border-radius: 8px;
    }

    #gasCanvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
    }

    .partition {
        position: absolute;
        top: 0;
        left: 50%;
        width: 4px; /* Thicker partition */
        height: 100%;
        background-color: #333;
        transform: translateX(-2px);
        z-index: 2;
    }

    .gate {
        position: absolute;
        top: 45%;
        left: 50%;
        width: 24px; /* Slightly wider gate */
        height: 50px; /* Taller gate */
        transform: translate(-12px, 0); /* Center */
        z-index: 3; /* Above partition */
        overflow: hidden; /* Hide gate-door when outside gate area */
    }

    .gate-door {
         position: absolute;
         top: 0;
         left: 0; /* Or start slightly inside */
         width: 100%;
         height: 100%;
         background-color: #555; /* Color of the door */
         border: 1px solid #222;
         box-sizing: border-box;
         transition: transform 0.2s ease-in-out; /* Smooth animation */
    }

    .gate.open .gate-door.left {
        transform: translateX(-100%); /* Move left half out */
    }
     .gate.open .gate-door.right {
        transform: translateX(100%); /* Move right half out */
    }
     .gate:not(.open) .gate-door {
         transform: translateX(0); /* Ensure closed state */
     }

     /* Let's simplify the gate door for now - just a single element that moves */
    .gate-door {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         background-color: rgba(85, 85, 85, 0.8); /* Semi-transparent door */
         border: 1px solid #222;
         box-sizing: border-box;
         transition: transform 0.2s ease-in-out;
         transform: translateX(0); /* Default closed */
    }

     .gate.open .gate-door {
         transform: translateX(100%); /* Simple animation: slide door out */
     }


     .demon {
        position: absolute;
        top: 50%;
        left: 50%; /* Start at the center */
        transform: translate(-50%, -50%);
        font-size: 2.5em; /* Slightly larger */
        z-index: 4; /* Above everything */
        pointer-events: none;
        transition: transform 0.3s ease-out; /* Smooth movement */
     }

     .demon.observing-left {
         transform: translate(-80%, -50%); /* Move left to observe */
     }
     .demon.observing-right {
         transform: translate(-20%, -50%); /* Move right to observe */
     }
      .demon.deciding {
         animation: pulse 0.5s infinite alternate; /* Visual cue for decision */
     }

     @keyframes pulse {
         from { transform: translate(-50%, -50%) scale(1); }
         to { transform: translate(-50%, -50%) scale(1.1); }
     }


    .controls {
        margin-bottom: 20px;
        display: flex;
        gap: 10px; /* Space between buttons */
    }

    .controls button {
        padding: 10px 20px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Heebo', sans-serif;
        font-weight: 700;
    }

    #startButton {
        background-color: #4CAF50; /* Green */
        color: white;
    }

    #startButton:hover {
        background-color: #45a049;
        transform: translateY(-2px);
    }
    #startButton:active {
         transform: translateY(0);
    }

    #stopButton {
        background-color: #f44336; /* Red */
        color: white;
    }

    #stopButton:hover {
        background-color: #da190b;
         transform: translateY(-2px);
    }
     #stopButton:active {
         transform: translateY(0);
    }


    #resetButton {
        background-color: #ff9800; /* Orange */
        color: white;
    }

    #resetButton:hover {
        background-color: #f57c00;
         transform: translateY(-2px);
    }
     #resetButton:active {
         transform: translateY(0);
    }


    .metrics {
        display: flex;
        width: 100%; /* Full width of container */
        justify-content: space-around;
        text-align: center;
        font-size: 0.95em;
        gap: 10px; /* Space between metric blocks */
    }

    .side-metrics, .global-metrics {
        border: 1px solid #ddd;
        padding: 15px 10px;
        border-radius: 8px;
        flex-grow: 1;
        background-color: #e1f5fe; /* Light blue background */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

     .side-metrics.left-side {
         background-color: #e3f2fd; /* Lighter blue */
         color: #0d47a1; /* Darker blue text */
     }
      .side-metrics.right-side {
         background-color: #ffebee; /* Light red */
         color: #b71c1c; /* Darker red text */
     }
       .global-metrics {
         background-color: #f0f4c3; /* Light yellow/green */
         color: #33691e; /* Dark green text */
         flex-basis: 180px; /* Give global a fixed width preference */
         flex-grow: 0; /* Prevent growing */
     }


    .side-metrics h4, .global-metrics h4 {
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.15em;
        color: #333; /* Darker heading color */
    }

     .metric-label {
         font-weight: bold;
         margin-right: 5px;
     }

    .side-metrics p, .global-metrics p {
        margin: 8px 0;
    }

    #tempDiff {
         font-weight: bold;
         color: inherit; /* Use parent color */
    }

    #explanation {
        display: none; /* Initially hidden */
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #eee;
        background-color: #f9f9f9;
        border-radius: 8px;
        line-height: 1.7;
        font-size: 1.05em;
    }

    #explanation h2 {
        border-bottom: 2px solid #b0bec5; /* Light greyish-blue */
        padding-bottom: 10px;
        margin-top: 0;
        color: #263238; /* Dark header color */
    }
     #explanation h3 {
         color: #455a64; /* Slightly lighter header */
         margin-top: 20px;
         margin-bottom: 10px;
     }

     #explanation p {
         margin-bottom: 15px;
     }
     #explanation ul {
         margin-top: 10px;
         margin-bottom: 15px;
         padding-left: 20px;
     }
     #explanation li {
         margin-bottom: 8px;
     }


     #toggleExplanationButton {
        display: block; /* Make button full width */
        width: 100%;
        max-width: 550px;
        margin: 20px auto;
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        border: 1px solid #b0bec5;
        border-radius: 6px;
        background-color: #eceff1; /* Light grey */
        color: #263238;
        transition: background-color 0.3s ease, border-color 0.3s ease;
        font-family: 'Heebo', sans-serif;
        font-weight: 700;
     }

      #toggleExplanationButton:hover {
          background-color: #cfd8dc;
          border-color: #90a4ae;
      }

      /* Molecule colors - improve vibrancy */
     .molecule.fast {
         fill: #e53935; /* Red */
     }
     .molecule.slow {
         fill: #1e88e5; /* Blue */
     }
     .molecule.medium {
         fill: #424242; /* Dark grey */
     }


</style>

<button id="toggleExplanationButton">גלו עוד: מידע על השד של מקסוול</button>

<div id="explanation">
    <h2>השד של מקסוול: מבט עמוק על אנטרופיה וסדר</h2>

    <h3>מהי אנטרופיה? הבלגן האוניברסלי</h3>
    <p>אנטרופיה היא אחד המושגים המרתקים והחמקמקים ביותר בפיזיקה. בפשטות, היא מדד למידת אי-הסדר או האקראיות במערכת פיזיקלית. חשבו על חדר מסודר להפליא לעומת חדר שהוריקן עבר בו – החדר המבולגן הוא בעל אנטרופיה גבוהה יותר. בפיזיקה, אנו מדברים על התפלגות מולקולות, מהירויותיהן, ומיקומן. מצב שבו כל החלקיקים מפוזרים באופן אחיד ומהירויותיהם מגוונות באקראי (כמו במצב שיווי משקל תרמי) הוא מצב בעל אנטרופיה מקסימלית.</p>

    <h3>החוק השני של התרמודינמיקה: גורל של בלגן?</h3>
    <p>חוק טבע עוצמתי זה קובע שבכל מערכת סגורה (כמו היקום כולו, או לפחות החלק שאנו מתייחסים אליו בניסוי), האנטרופיה לעולם אינה יורדת. היא יכולה רק לעלות בתהליכים ספונטניים (כמו קוביית קרח שנמסה) או להישאר קבועה בתהליכים אידיאליים והפיכים. המשמעות הדרמטית היא שהיקום שלנו, באופן טבעי, נוטה לעבר אי-סדר הולך וגובר. חוק זה הוא הבסיס לחץ הזמן שאנו חווים – דברים מתקדמים באופן שמעלה את האנטרופיה.</p>

    <h3>הפרובוקציה: ניסוי המחשבה של השד של מקסוול (1867)</h3>
    <p>הפיזיקאי הענק ג'יימס קלרק מקסוול לא קיבל את החוק השני כגזירה משמיים ללא עוררין, ולכן הגה ניסוי מחשבתי מבריק. הוא דמיין מיכל סגור מלא בגז בטמפרטורה אחידה, המחולק לשניים על ידי מחיצה עם פתח קטן הנשלט על ידי דלתית זעירה. ליד הפתח ניצב "שד" תיאורטי – יצור מיניאטורי בעל יכולת ראיית-על, שמסוגל למדוד את המהירות של כל מולקולת גז המתקרבת לפתח.</p>
    <p>מה עושה השד? הוא מפעיל מדיניות מיון מחמירה:
    <ul>
        <li>כאשר מולקולה <strong>מהירה</strong> מגיעה מצד שמאל אל הפתח, הוא פותח את הדלתית ונותן לה לעבור לצד ימין.</li>
        <li>כאשר מולקולה <strong>איטית</strong> מגיעה מצד ימין אל הפתח, הוא פותח את הדלתית ונותן לה לעבור לצד שמאל.</li>
        <li>לכל מולקולה אחרת, הוא משאיר את הדלתית סגורה.</li>
    </ul>
    </p>

    <h3>הפרדוקס המטריד: נראה שהשד שובר את החוקים!</h3>
    <p>אם השד יפעל כך לאורך זמן, התוצאה הבלתי נמנעת תהיה שכל המולקולות המהירות (ה"חמות") יצטברו בצד ימין, וכל המולקולות האיטיות (ה"קרות") יצטברו בצד שמאל. המערכת תגיע למצב של הפרדת טמפרטורות – צד אחד חם וצד שני קר. מצב כזה, עם הפרש טמפרטורות שניתן לנצל לביצוע עבודה (למשל, על ידי מנוע חום), הוא מצב מסודר בהרבה ממצב התחלתי של טמפרטורה אחידה. במילים אחרות, נראה שהשד הצליח להפחית את האנטרופיה של המערכת הסגורה, כביכול מפר את החוק השני של התרמודינמיקה באופן בוטה!</p>

    <h3>הפתרון האלגנטי: אינפורמציה היא לא חינם</h3>
    <p>הפרדוקס של מקסוול הטריד פיזיקאים עשרות שנים. התשובה נמצאה לבסוף, והיא קשורה קשר הדוק לתורת המידע. ההבנה היא שפעולת השד אינה תהליך "חינמי" או נטול אנטרופיה. כדי למיין, השד חייב קודם כל למדוד את מהירות המולקולות – כלומר, לרכוש מידע. המידע הזה צריך להיאחס, להיות מעובד, ואז להימחק כדי לפנות מקום למידע חדש. הפיזיקאי רולף לאנדאואר הראה שפעולת *מחיקת* המידע היא תהליך פיזיקלי הכרוך בהכרח בגידול באנטרופיה של השד עצמו וסביבתו, וגידול זה תמיד גדול או שווה לירידה באנטרופיית הגז שנוצרה על ידי המיון. למעשה, השד לא מפר את החוק השני, אלא רק מעביר את הנטל האנטרופי לתהליך החישובי והמידעני שלו. האנטרופיה *הכוללת* (גז + שד + סביבה) עדיין עולה או נשארת קבועה.</p>

    <h3>חשיבות הניסוי: הגשר בין מידע לפיזיקה</h3>
    <p>ניסוי המחשבה של מקסוול היה הרבה יותר מסתם חידה תרמודינמית. הוא היה אחד הניצוצות הראשונים שהראו שלמידע וחישוב יש השלכות פיזיקליות עמוקות, ושהם קשורים קשר בל יינתק לאנטרופיה ולאנרגיה. הוא סלל את הדרך לפיתוח תחומים חדשים בפיזיקה, כמו תרמודינמיקה של מידע וגבולות פיזיקליים של חישוב, ואף השפיע על מחקר בחישוב קוונטי. הוא לימד אותנו שיעור יסודי: סדר אינו נוצר יש מאין – הוא תמיד בא במחיר אנרגטי או מידעני.</p>
</div>


<script>
    const canvas = document.getElementById('gasCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const resetButton = document.getElementById('resetButton');
    const countLeftSpan = document.getElementById('countLeft');
    const countRightSpan = document.getElementById('countRight');
    const tempLeftSpan = document.getElementById('tempLeft');
    const tempRightSpan = document.getElementById('tempRight');
    const tempDiffSpan = document.getElementById('tempDiff');
    const demonElement = document.getElementById('demon');
    const gateElement = document.getElementById('gate');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');

    const canvasWidth = 500;
    const canvasHeight = 300;
    const partitionX = canvasWidth / 2;
    const gateHeight = 50;
    const gateWidth = 24;
    const gateTop = canvasHeight * 0.45;
    const gateBottom = gateTop + gateHeight;
    const gateLeft = partitionX - gateWidth / 2;
    const gateRight = partitionX + gateWidth / 2;

    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    const numMolecules = 200; // Increased molecules for better stats
    const moleculeRadius = 3;
    const minSpeed = 0.5;
    const maxSpeed = 3.5; // Increased speed range
    const fastThreshold = 2.5; // Higher threshold for 'fast'
    const slowThreshold = 1.0; // Lower threshold for 'slow'
    const moleculeColorFast = '#e53935'; // Red
    const moleculeColorSlow = '#1e88e5'; // Blue
    const moleculeColorMedium = '#424242'; // Dark grey

    let molecules = [];
    let animationFrameId;
    let isDemonActive = false;
    let gateState = 'closed'; // 'closed', 'opening', 'open', 'closing'
    const gateAnimationDuration = 200; // ms
    let gateAnimationStartTime = 0;

    // Helper function for random number within range
    function getRandom(min, max) {
        return Math.random() * (max - min) + min;
    }

    // Get molecule color based on speed
    function getMoleculeColor(speed) {
        if (speed > fastThreshold) return moleculeColorFast;
        if (speed < slowThreshold) return moleculeColorSlow;
        return moleculeColorMedium;
    }

    // Initialize molecules
    function initMolecules() {
        molecules = [];
        for (let i = 0; i < numMolecules; i++) {
            let speed = getRandom(minSpeed, maxSpeed);
            let angle = getRandom(0, 2 * Math.PI);
            molecules.push({
                x: getRandom(moleculeRadius, canvasWidth - moleculeRadius),
                y: getRandom(moleculeRadius, canvasHeight - moleculeRadius),
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                speed: speed, // Store speed magnitude
                color: getMoleculeColor(speed)
            });
        }
    }

    // Draw everything
    function draw() {
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Draw molecules
        molecules.forEach(mol => {
            ctx.beginPath();
            ctx.arc(mol.x, mol.y, moleculeRadius, 0, Math.PI * 2);
            ctx.fillStyle = mol.color;
            ctx.fill();
        });

        // Partition and Gate are now handled by CSS divs
        // The gate 'open' state is managed by JS adding/removing a class

        // Update metrics display
        updateMetrics();
    }

    // Update metrics
    function updateMetrics() {
        let countLeft = 0;
        let countRight = 0;
        let speedSumLeft = 0; // Using sum of speeds as temperature proxy
        let speedSumRight = 0;

        molecules.forEach(mol => {
            if (mol.x < partitionX) {
                countLeft++;
                speedSumLeft += mol.speed;
            } else {
                countRight++;
                speedSumRight += mol.speed;
            }
        });

        const avgSpeedLeft = countLeft > 0 ? speedSumLeft / countLeft : 0;
        const avgSpeedRight = countRight > 0 ? speedSumRight / countRight : 0;

        countLeftSpan.textContent = countLeft;
        countRightSpan.textContent = countRight;
        // Display average speed as temperature proxy, formatted
        tempLeftSpan.textContent = avgSpeedLeft.toFixed(1);
        tempRightSpan.textContent = avgSpeedRight.toFixed(1);
        tempDiffSpan.textContent = Math.abs(avgSpeedLeft - avgSpeedRight).toFixed(1);

        // Update demon position based on activity (optional but adds life)
        if (isDemonActive) {
            // Simple logic: if more fast on left or slow on right, focus on gate
            if (countLeft > 0 && avgSpeedLeft > fastThreshold * 0.8) demonElement.classList.add('observing-left');
            else if (countRight > 0 && avgSpeedRight < slowThreshold * 1.2) demonElement.classList.add('observing-right');
             else { // Default center position
                 demonElement.classList.remove('observing-left', 'observing-right');
             }

             // Add decision animation if a molecule is near the gate and demon is processing
             const moleculeNearGate = molecules.some(mol =>
                 Math.abs(mol.x - partitionX) < moleculeRadius * 3 && // Check proximity
                 mol.y > gateTop - moleculeRadius && mol.y < gateBottom + moleculeRadius // Check if aligned with gate
             );
             if(moleculeNearGate) {
                demonElement.classList.add('deciding');
             } else {
                 demonElement.classList.remove('deciding');
             }

        } else {
            // Demon inactive, reset position and animations
             demonElement.classList.remove('observing-left', 'observing-right', 'deciding');
        }


    }


    // Move molecules and handle collisions
    function update(currentTime) {
        const deltaTime = (currentTime - (update.lastTime || currentTime)) / 1000; // Delta time in seconds
        update.lastTime = currentTime;
        const dt = 1; // Fixed step for simulation logic, adjust velocity scale if needed

        // Update gate animation state
        if (gateState === 'opening' || gateState === 'closing') {
            const elapsed = currentTime - gateAnimationStartTime;
            if (elapsed >= gateAnimationDuration) {
                gateState = (gateState === 'opening') ? 'open' : 'closed';
                gateElement.classList.toggle('open', gateState === 'open');
            }
        }


        molecules.forEach(mol => {
            // Store previous position for collision handling
            const prevX = mol.x;
            const prevY = mol.y;

            // Move
            mol.x += mol.vx * dt;
            mol.y += mol.vy * dt;

            // Wall collisions
            if (mol.x < moleculeRadius) {
                mol.x = moleculeRadius;
                mol.vx = Math.abs(mol.vx); // Ensure positive vx
            } else if (mol.x > canvasWidth - moleculeRadius) {
                mol.x = canvasWidth - moleculeRadius;
                mol.vx = -Math.abs(mol.vx); // Ensure negative vx
            }
            if (mol.y < moleculeRadius) {
                 mol.y = moleculeRadius;
                mol.vy = Math.abs(mol.vy); // Ensure positive vy
            } else if (mol.y > canvasHeight - moleculeRadius) {
                mol.y = canvasHeight - moleculeRadius;
                mol.vy = -Math.abs(mol.vy); // Ensure negative vy
            }

            // Partition/Gate collision
            const crossedPartition = (prevX < partitionX && mol.x >= partitionX) || (prevX >= partitionX && mol.x < partitionX);
            const nearGateHeight = mol.y > gateTop && mol.y < gateBottom; // Check if molecule is *within* the gate opening height

            if (crossedPartition && nearGateHeight) {
                // Molecule crossed the partition line AND is within the gate height
                 let decision = 'reflect'; // Default decision is to reflect

                 if (isDemonActive) {
                     const movingRight = mol.vx > 0;
                     const movingLeft = mol.vx < 0;
                     const isFast = mol.speed > fastThreshold;
                     const isSlow = mol.speed < slowThreshold;

                     // Demon's Rule: Fast from Left -> Right, Slow from Right -> Left
                     if (movingRight && mol.x >= partitionX && isFast) { // Came from left (prevX < partitionX) and wants to go right (mol.x >= partitionX) and is Fast
                         decision = 'pass';
                     } else if (movingLeft && mol.x < partitionX && isSlow) { // Came from right (prevX >= partitionX) and wants to go left (mol.x < partitionX) and is Slow
                         decision = 'pass';
                     } else {
                         decision = 'reflect'; // Not meeting the criteria
                     }
                 } else {
                     decision = 'reflect'; // Demon not active, gate is always closed
                 }

                 if (decision === 'reflect') {
                     // Revert position and reflect velocity
                     mol.x = prevX;
                     mol.y = prevY; // Also revert Y just in case boundary logic is tricky
                     mol.vx *= -1;
                      // Visual cue for gate closed/blocked
                      if (gateState !== 'closed') {
                           gateState = 'closing';
                           gateAnimationStartTime = currentTime;
                           gateElement.classList.remove('open'); // Start closing visual
                      }

                 } else { // Decision is 'pass'
                     // Allow passage, no velocity change needed, position is already updated
                      // Visual cue for gate opening/open
                      if (gateState !== 'open') {
                          gateState = 'opening';
                          gateAnimationStartTime = currentTime;
                          gateElement.classList.add('open'); // Start opening visual
                      }
                 }

            } else if (crossedPartition && !nearGateHeight) {
                 // Molecule crossed partition line BUT is NOT within gate height
                 // Always reflect, partition is solid here
                  mol.x = prevX;
                  mol.y = prevY;
                  mol.vx *= -1;
                  // Ensure gate looks closed if molecule hits solid partition
                   if (gateState !== 'closed') {
                       gateState = 'closing';
                       gateAnimationStartTime = currentTime;
                       gateElement.classList.remove('open'); // Start closing visual
                   }

            } else {
                 // No partition crossing, but check collision with partition if near
                 // This handles molecules approaching but not yet crossing
                 const isNearPartition = Math.abs(mol.x - partitionX) < moleculeRadius + Math.abs(mol.vx); // Simple check for proximity in X
                 if (isNearPartition && !nearGateHeight) {
                      if ((mol.vx > 0 && mol.x < partitionX) || (mol.vx < 0 && mol.x > partitionX)) { // Moving towards partition
                          mol.x = prevX; // Revert position
                          mol.vy = prevY;
                           mol.vx *= -1; // Reflect
                            // Ensure gate looks closed if molecule hits solid partition
                           if (gateState !== 'closed') {
                               gateState = 'closing';
                               gateAnimationStartTime = currentTime;
                               gateElement.classList.remove('open'); // Start closing visual
                           }
                      }
                 }
            }


        });

        draw();
        animationFrameId = requestAnimationFrame(update);
    }

    // Stop animation
    function stopSimulation() {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null; // Allow starting again
        isDemonActive = false; // Stop the demon's logic
        // Ensure gate closes visually when stopped
        if (gateState !== 'closed') {
            gateState = 'closing';
            gateAnimationStartTime = performance.now(); // Use performance.now() for animation timing
            gateElement.classList.remove('open');
             // Need one final update call to process the gate closing animation frame(s)
             // Or just force the state visually:
             gateState = 'closed';
             gateElement.classList.remove('open');
        }
        updateMetrics(); // Update one last time to reflect final state
    }

    // Start simulation with demon active
    function startSimulation() {
        if (!animationFrameId) { // Prevent starting multiple times
            isDemonActive = true;
            // Reset gate state visually at start
            gateState = 'closed';
            gateElement.classList.remove('open');
            update.lastTime = performance.now(); // Initialize lastTime
            update(); // Start the update loop
        }
    }

     // Reset simulation
    function resetSimulation() {
        stopSimulation();
        initMolecules();
        // Reset metrics display immediately
        countLeftSpan.textContent = numMolecules / 2;
        countRightSpan.textContent = numMolecules / 2;
        tempLeftSpan.textContent = '0.0'; // Will be updated on first draw
        tempRightSpan.textContent = '0.0';
        tempDiffSpan.textContent = '0.0';
        draw(); // Draw initial state
    }

    // Toggle explanation visibility
    function toggleExplanation() {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'גלו עוד: מידע על השד של מקסוול';
        }
    }


    // Event Listeners
    startButton.addEventListener('click', startSimulation);
    stopButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Initial setup
    initMolecules();
    draw(); // Draw the initial state before starting
    // Update metrics after initial draw to show initial counts
    updateMetrics();


</script>
---
```