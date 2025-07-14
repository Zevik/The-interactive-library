---
title: "ריקוד קוסמי: מסלולים אליפטיים וכוח המשיכה"
english_slug: elliptical-orbits-and-gravity
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה
  - אסטרונומיה
  - כוח משיכה
  - חוקי קפלר
  - מסלולים
---
<h1>ריקוד קוסמי: מסלולים אליפטיים וכוח המשיכה</h1>

<p>התכוננו למסע בחלל! האם תהיתם אי פעם למה כוכבי הלכת לא נופלים פנימה לתוך השמש, או בורחים החוצה אל האינסוף? בואו נגלה יחד איך כוח המשיכה מעצב מסלולים מדהימים!</p>

<div class="simulation-container">
    <div class="controls">
        <button id="addCentralBodyBtn" class="control-button">הוסף כוכב</button>
        <button id="addPlanetBtn" class="control-button" disabled>הוסף כוכב לכת</button>
        <button id="runSimulationBtn" class="control-button primary" disabled>הפעל סימולציה!</button>
        <button id="resetSimulationBtn" class="control-button secondary">איפוס</button>
        <div id="velocityControls" class="control-message" style="display: none;">
            <p>גרור מכוכב הלכת כדי להגדיר מהירות התחלתית (ככל שאתה גורר רחוק יותר, המהירות גדולה יותר!)</p>
        </div>
    </div>
     <div id="messageArea" class="status-message"></div>
    <canvas id="physicsCanvas"></canvas>
</div>

<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        line-height: 1.7; /* Improved readability */
        color: #eee; /* Lighter text for dark background theme */
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background: linear-gradient(to bottom, #0a0a1a, #1a1a3a); /* Dark cosmic gradient background */
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: #64b5f6; /* Lighter blue for headings */
        text-align: center; /* Center main title */
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2.2em;
        margin-top: 0;
    }

     p {
        text-align: right;
        margin-bottom: 15px;
     }

    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
        background-color: #1e1e3f; /* Darker panel background */
        padding: 20px;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 5px 15px rgba(0,0,0,0.3); /* Stronger shadow */
         border: 1px solid #3a3a5a; /* Subtle border */
    }

    .controls {
        margin-bottom: 20px;
        text-align: center;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px; /* Space between buttons */
    }

    .control-button {
        padding: 12px 20px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        min-width: 120px; /* Give buttons a minimum width */
    }

    .control-button.primary {
        background-color: #4caf50; /* Green */
        color: white;
    }
     .control-button.primary:hover:enabled {
        background-color: #388e3c; /* Darker green */
     }

    .control-button.secondary {
         background-color: #fbc02d; /* Yellow/Amber */
         color: #333;
    }
    .control-button.secondary:hover:enabled {
         background-color: #f9a825; /* Darker yellow */
    }

    /* Default button style */
     .control-button:not(.primary):not(.secondary) {
        background-color: #2196f3; /* Blue */
        color: white;
    }
    .control-button:not(.primary):not(.secondary):hover:enabled {
         background-color: #1976d2; /* Darker blue */
    }


    .control-button:disabled {
        background-color: #607d8b; /* Greyed out */
        color: #bdbdbd;
        cursor: not-allowed;
        transform: none; /* No hover effect when disabled */
    }

    .control-button:active:enabled {
        transform: scale(0.98); /* Subtle press effect */
    }


    .control-message {
         margin: 10px 0;
         font-weight: bold;
         color: #b3e5fc; /* Light blue */
         text-align: center;
         width: 100%;
         font-size: 1.1em;
         min-height: 1.5em; /* Reserve space */
    }

     .control-message p {
         margin: 0;
         text-align: center;
     }

     .status-message {
        color: #ffb74d; /* Light orange for status */
        min-height: 1.5em; /* Reserve space */
        margin-bottom: 10px;
        font-weight: bold;
        text-align: center;
        width: 100%;
        font-size: 1.1em;
     }

    canvas {
        border: 2px solid #5a5a7a; /* Subtle border */
        background: radial-gradient(circle at center, #0d0d25 0%, #050515 100%); /* Darker radial gradient for canvas */
        display: block;
        margin: 0 auto;
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5); /* Inner shadow for depth */
    }

    .explanation-button {
        display: block;
        margin: 30px auto; /* More vertical space */
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        background-color: #00796b; /* Teal */
        color: white;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        min-width: 200px;
    }

    .explanation-button:hover {
        background-color: #004d40; /* Darker teal */
    }
     .explanation-button:active {
        transform: scale(0.98);
    }


    .explanation {
        margin-top: 20px;
        padding: 20px;
        background-color: #2a2a4a; /* Dark blue-grey for explanation */
        border-radius: 12px;
        display: none;
         border: 1px solid #4a4a6a; /* Subtle border */
        color: #ccc; /* Lighter text for explanation body */
    }

    .explanation h2, .explanation h3 {
        color: #b39ddb; /* Lavender color for explanation headings */
        text-align: right;
        margin-bottom: 10px;
    }

     .explanation h2 {
         margin-top: 0;
         font-size: 1.8em;
     }
     .explanation h3 {
         font-size: 1.4em;
         margin-top: 15px;
     }

    .explanation p, .explanation ul {
        margin-bottom: 15px;
        text-align: right;
    }

    .explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Use right margin for RTL list */
        margin-left: 0;
        padding-right: 0; /* Ensure no default left padding */
    }

     .explanation li {
         margin-bottom: 8px;
     }

     .explanation strong {
         color: #ffecb3; /* Light yellow for emphasis */
     }

    /* Styles for interactive elements drawn on canvas */
     /* Velocity arrow - handled in JS draw function */
     /* Trajectory - handled in JS draw function */

</style>

<button class="explanation-button" id="toggleExplanationBtn">מה בעצם קורה כאן? (הסבר)</button>

<div class="explanation" id="explanationContent">
    <h2>קסם כוח המשיכה: כך נשארים במסלול!</h2>
    <p>מסע בין כוכבים דורש הבנה של כוחות אדירים הפועלים ביקום. התנועה המרהיבה של כוכבי לכת סביב שמשות, או של לוויינים סביב כדור הארץ, היא תוצאה של ריקוד עדין בין שני גורמים עיקריים:</p>

    <h3>אינרציה מול משיכה: הדינמיקה הקוסמית</h3>
    <ul>
        <li><strong>דחף ראשוני (אינרציה):</strong> כל גוף שנע בחלל שואף להמשיך בתנועה קו ישר ובמהירות קבועה. דמיינו כדור שנזרק בריק מוחלט - הוא ימשיך לטוס לנצח באותו קו! מהירות זו היא ה"זיכרון" של הכיוון והעוצמה הראשוניים שקיבל הגוף.</li>
        <li><strong>משיכת הענק (כוח המשיכה):</strong> גופים מסיביים (כמו כוכבים וכוכבי לכת) מושכים אליהם גופים אחרים. כוח זה תמיד פועל כלפי המרכז המושך, ועוצמתו תלויה במסה של שני הגופים ובמרחק ביניהם (ככל שהמרחק קטן יותר, המשיכה חזקה יותר!).</li>
    </ul>
    <p>השילוב הגאוני של הדחף הקווי וכוח המשיכה המרכזי גורם לגוף הנע "להתעקל" כל הזמן לכיוון הגוף המסיבי, במקום להמשיך בקו ישר. אם המהירות ההתחלתית נכונה - לא חזקה מדי (בריחה מהמערכת) ולא חלשה מדי (התרסקות) - נוצר מסלול יציב!</p>

    <h3>חוקי קפלר: המפה של תנועת הפלנטות</h3>
    <p>הרבה לפני ניוטון, האסטרונום יוהנס קפלר פענח את דפוסי תנועת כוכבי הלכת על בסיס תצפיות מדויקות. הוא ניסח שלושה חוקים המתארים את התנועה, ולימים ניוטון הוכיח אותם מתמטית באמצעות חוק כוח המשיכה שלו:</p>
    <ul>
        <li><strong>החוק הראשון: המסלולים הם אליפסות!</strong><br>
            בניגוד לאמונה העתיקה שהמסלולים חייבים להיות מעגלים מושלמים, קפלר גילה שכל כוכב לכת נע סביב השמש במסלול אליפטי (צורה אליפסה או "ביצה פחוסה"), כשהשמש נמצאת באחד משני ה"מוקדים" של האליפסה. מעגל הוא מקרה פרטי של אליפסה. בסימולטור שלנו, תוכלו לראות איך שינוי המהירות ההתחלתית משנה את צורת האליפסה (או גורם למסלול בריחה / התרסקות!).
        </li>
        <li><strong>החוק השני: שטחים שווים בזמנים שווים!</strong><br>
            קו דמיוני המחבר את כוכב הלכת לשמש "מטאטא" שטחים שווים בחלל בזמני תנועה שווים. זה אולי נשמע מסובך, אבל המשמעות פשוטה ומרתקת: כוכב הלכת נע מהר יותר כשהוא קרוב לשמש (כי המשיכה חזקה יותר ומאיצה אותו!) ולאט יותר כשהוא רחוק ממנה (כי המשיכה חלשה יותר). תצפו בסימולציה - האם אתם רואים שהכוכב לכת מאיץ כשהוא קרוב לכוכב?
        </li>
        <li><strong>החוק השלישי: מחזור קשור למרחק!</strong><br>
            יש קשר מתמטי קבוע בין זמן המחזור של כוכב לכת (כמה זמן לוקח לו להשלים הקפה אחת) לבין מרחקו הממוצע מהשמש. כוכבי לכת רחוקים יותר נעים לאט יותר ומשלימים הקפה בזמן ארוך משמעותית. החוק הזה מאפשר לאסטרונומים לחשב מרחקים וזמנים במערכות כוכבים אחרות!</li>
    </ul>

    <h3>הסימולטור ככלי גילוי</h3>
    <p>הסימולטור הזה הוא מגרש המשחקים הקוסמי שלכם! התנסו במיקומים ובעיקר במהירויות התחלתיות שונות כדי לראות במו עיניכם כיצד הם קובעים את גורל כוכב הלכת: האם הוא ינוע במסלול מעגלי כמעט מושלם, באליפסה פחוסה, יתרסק לתוך הכוכב, או אולי יקבל דחיפה חזקה מספיק כדי לברוח מהשפעת המשיכה לגמרי?</p>

    <h3>מגבלות והיקום האמיתי</h3>
    <p>כמו כל סימולציה, גם זו מפשטת את המציאות הקוסמית המורכבת. אנחנו מתמקדים במערכת של שני גופים בלבד (רוב הזמן), פועלים בממד דו-ממדי, ומתעלמים מכוחות נוספים (כמו משיכה בין כוכבי הלכת עצמם, לחץ קרינה מהכוכב, ואפקטים של תורת היחסות). ובכל זאת, הסימולטור הזה מספק הצצה עוצמתית ואינטואיטיבית לעקרונות הבסיסיים ביותר שמניעים את הריקוד הקוסמי של גופים בחלל!</p>
</div>

<script>
    const canvas = document.getElementById('physicsCanvas');
    const ctx = canvas.getContext('2d');
    const addCentralBodyBtn = document.getElementById('addCentralBodyBtn');
    const addPlanetBtn = document.getElementById('addPlanetBtn');
    const velocityControlsDiv = document.getElementById('velocityControls');
    const runSimulationBtn = document.getElementById('runSimulationBtn');
    const resetSimulationBtn = document.getElementById('resetSimulationBtn');
    const messageArea = document.getElementById('messageArea');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationContent = document.getElementById('explanationContent');

    canvas.width = 600;
    canvas.height = 400;

    // --- Simulation Constants ---
    const G = 0.1; // Gravitational constant (scaled for simulation)
    const SCALE = 50; // Pixels per simulated unit (adjust for size of orbits)
    const DT = 0.1; // Time step for simulation (smaller is more accurate but slower)
    const VELOCITY_DRAG_SCALE = 30; // Divisor for drag distance to get initial velocity magnitude. Higher = less velocity for same drag.
    const TRAIL_MAX_LENGTH = 1500; // Max points in the trajectory trail

    // --- Simulation State ---
    let centralBody = null;
    let planet = null;
    let simulationRunning = false;
    // States: 'initial', 'placingCentral', 'placingPlanet', 'settingVelocity', 'readyToRun', 'running', 'crashed'
    let simulationState = 'initial';
    let velocityStartPosCanvas = null; // In canvas pixels
    let velocityEndPosCanvas = null;   // In canvas pixels
    let trajectory = []; // Stores simulation coordinates {x, y}

    // --- Body Class ---
    class Body {
        constructor(x, y, mass, radius, color, type, name = '') {
            this.position = { x: x, y: y }; // In simulation units
            this.velocity = { x: 0, y: 0 }; // In simulation units per time unit
            this.mass = mass;
            this.radius = radius; // In pixels (for drawing)
            this.color = color;
            this.type = type; // 'central' or 'planet'
            this.name = name;
            this.acceleration = { x: 0, y: 0 }; // In simulation units per time unit squared
            this.trailColor = type === 'planet' ? color : null; // Color for the trail
        }

        // Convert simulation position to canvas position
        getCanvasPosition() {
             return {
                 x: this.position.x * SCALE + canvas.width / 2,
                 y: -this.position.y * SCALE + canvas.height / 2 // Canvas Y is inverted
             };
        }

        draw(context) {
            const canvasPos = this.getCanvasPosition();

            // Draw body
            context.fillStyle = this.color;
            context.beginPath();
            context.arc(canvasPos.x, canvasPos.y, this.radius, 0, Math.PI * 2);
            context.fill();

             // Optional: Draw a subtle ring for planets/stars
             if (this.type === 'central') {
                 context.strokeStyle = 'rgba(255, 193, 7, 0.3)'; // Subtle yellow ring
                 context.lineWidth = 2;
                 context.beginPath();
                 context.arc(canvasPos.x, canvasPos.y, this.radius + 5, 0, Math.PI * 2);
                 context.stroke();
             }
              if (this.type === 'planet') {
                 context.strokeStyle = 'rgba(23, 162, 184, 0.3)'; // Subtle blue ring
                 context.lineWidth = 1.5;
                 context.beginPath();
                 context.arc(canvasPos.x, canvasPos.y, this.radius + 3, 0, Math.PI * 2);
                 context.stroke();
             }

             // Optional: Draw name/label (simple for now)
            //  context.fillStyle = '#fff';
            //  context.font = '12px Arial';
            //  context.textAlign = 'center';
            //  context.fillText(this.name, canvasPos.x, canvasPos.y - this.radius - 5);
        }

        update(bodies, dt) {
             if (this.type === 'central') return; // Central body is fixed

            let totalForceX = 0;
            let totalForceY = 0;

            for (const body of bodies) {
                if (body === this) continue;

                const dx = body.position.x - this.position.x;
                const dy = body.position.y - this.position.y;
                const distanceSquared = dx * dx + dy * dy;
                const distance = Math.sqrt(distanceSquared);

                // Collision detection - check if distance is less than sum of radii (in sim units)
                 // Convert radii to sim units for collision check
                 const thisRadiusSim = this.radius / SCALE;
                 const otherRadiusSim = body.radius / SCALE;

                 if (distance < thisRadiusSim + otherRadiusSim) {
                     // Handle collision
                     if (body.type === 'central') {
                          // Planet crashed into central body
                          console.log(`${this.name} crashed into ${body.name}!`);
                          simulationRunning = false;
                          simulationState = 'crashed'; // Set a crashed state
                          // messageArea will be updated by updateControls
                     }
                     // For planet-planet collision (not implemented here with only one planet): elastic collision physics would be needed.
                     return; // Stop updating this frame if collision occurred
                 }


                // Prevent division by zero or excessive force at very small distances
                const minDistance = 0.1; // Minimum distance to consider (in simulation units)
                const clampedDistance = Math.max(distance, minDistance);
                const clampedDistanceSquared = clampedDistance * clampedDistance;


                const forceMagnitude = (G * this.mass * body.mass) / clampedDistanceSquared;

                const forceX = forceMagnitude * (dx / distance); // Use actual distance for direction
                const forceY = forceMagnitude * (dy / distance);

                totalForceX += forceX;
                totalForceY += forceY;
            }

            this.acceleration.x = totalForceX / this.mass;
            this.acceleration.y = totalForceY / this.mass;

            this.velocity.x += this.acceleration.x * dt;
            this.velocity.y += this.acceleration.y * dt;

            this.position.x += this.velocity.x * dt;
            this.position.y += this.velocity.y * dt;
        }
    }

    // --- Simulation Logic ---

    function draw() {
        // Clear canvas with gradient background
        const backgroundGradient = ctx.createRadialGradient(canvas.width/2, canvas.height/2, 50, canvas.width/2, canvas.height/2, canvas.width/2);
        backgroundGradient.addColorStop(0, '#0d0d25');
        backgroundGradient.addColorStop(1, '#050515');
        ctx.fillStyle = backgroundGradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);

         // Optional: Draw subtle stars (simple dots)
         drawStars(ctx); // Need a function for this

        // Draw trajectory trail
        if (planet && trajectory.length > 1) {
             ctx.strokeStyle = planet.trailColor || '#aaa'; // Use planet's color or default
             ctx.lineWidth = 1;
             ctx.beginPath();
             // Convert first point to canvas coordinates
             ctx.moveTo(trajectory[0].x * SCALE + canvas.width / 2, -trajectory[0].y * SCALE + canvas.height / 2);
             // Connect subsequent points
             for (let i = 1; i < trajectory.length; i++) {
                  // Add fading effect by changing alpha along the trail? More complex.
                  // For now, just draw the line.
                  ctx.lineTo(trajectory[i].x * SCALE + canvas.width / 2, -trajectory[i].y * SCALE + canvas.height / 2);
             }
             ctx.stroke();
         }


        // Draw bodies (Central body first, then planet)
        if (centralBody) centralBody.draw(ctx);
        if (planet) planet.draw(ctx);

        // Draw velocity arrow if setting velocity
        if (simulationState === 'settingVelocity' && velocityStartPosCanvas && velocityEndPosCanvas) {
            ctx.strokeStyle = '#0f0'; // Green color for velocity vector
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(velocityStartPosCanvas.x, velocityStartPosCanvas.y);
            ctx.lineTo(velocityEndPosCanvas.x, velocityEndPosCanvas.y);
            ctx.stroke();

            // Draw arrow head (simple triangle)
            const angle = Math.atan2(velocityEndPosCanvas.y - velocityStartPosCanvas.y, velocityEndPosCanvas.x - velocityStartPosCanvas.x);
            const headLength = 15; // Length of arrowhead sides
            const headAngle = Math.PI / 7; // Angle of arrowhead sides

            ctx.beginPath();
            ctx.moveTo(velocityEndPosCanvas.x, velocityEndPosCanvas.y);
            ctx.lineTo(velocityEndPosCanvas.x - headLength * Math.cos(angle - headAngle), velocityEndPosCanvas.y - headLength * Math.sin(angle - headAngle));
            ctx.moveTo(velocityEndPosCanvas.x, velocityEndPosCanvas.y);
            ctx.lineTo(velocityEndPosCanvas.x - headLength * Math.cos(angle + headAngle), velocityEndPosCanvas.y - headLength * Math.sin(angle + headAngle));
            ctx.stroke();
        }

         // Draw temporary body outline during placing states
         if (simulationState === 'placingCentral' || simulationState === 'placingPlanet') {
              const rect = canvas.getBoundingClientRect();
              const mouseX = lastMousePos.x - rect.left; // Use last recorded mouse pos
              const mouseY = lastMousePos.y - rect.top;
              const radius = simulationState === 'placingCentral' ? 15 : 5; // Match body radius
              ctx.strokeStyle = '#ffffff50'; // Semi-transparent white
              ctx.lineWidth = 2;
              ctx.beginPath();
              ctx.arc(mouseX, mouseY, radius, 0, Math.PI * 2);
              ctx.stroke();
         }
    }

     // Simple stars drawing function
     const stars = [];
     function initStars(numStars) {
         for(let i = 0; i < numStars; i++) {
             stars.push({
                 x: Math.random() * canvas.width,
                 y: Math.random() * canvas.height,
                 radius: Math.random() * 1.5 + 0.5,
                 alpha: Math.random() * 0.5 + 0.3 // Subtle alpha
             });
         }
     }

     function drawStars(context) {
         context.fillStyle = '#ffffff'; // White stars
         stars.forEach(star => {
             context.globalAlpha = star.alpha;
             context.beginPath();
             context.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
             context.fill();
         });
         context.globalAlpha = 1; // Reset alpha
     }
     initStars(100); // Initialize 100 stars

    function update() {
        if (!simulationRunning || !centralBody || !planet) return;

        // Update planet position based on force from central body
        planet.update([centralBody], DT); // Pass centralBody in an array

        // Add current planet position to trajectory *if* simulation is running
         if (simulationRunning) {
            trajectory.push({ x: planet.position.x, y: planet.position.y });

            // Keep trajectory length reasonable
            if (trajectory.length > TRAIL_MAX_LENGTH) {
                trajectory.shift(); // Remove the oldest point
            }
         }

         // Collision check is now inside Body.update, which sets simulationState to 'crashed'
         if (simulationState === 'crashed') {
              simulationRunning = false;
              updateControls(); // Update buttons/message for crash state
         }

         // Optional: Check if planet goes too far off-screen and stop?
         const canvasPos = planet.getCanvasPosition();
         const offscreenThreshold = 100; // Pixels outside canvas border
         if (canvasPos.x < -offscreenThreshold || canvasPos.x > canvas.width + offscreenThreshold ||
             canvasPos.y < -offscreenThreshold || canvasPos.y > canvas.height + offscreenThreshold) {
               if (simulationState === 'running') { // Only stop if running
                   simulationRunning = false;
                   simulationState = 'readyToRun'; // Maybe revert to ready or a 'escaped' state?
                   messageArea.textContent = 'כוכב הלכת ברח מהמערכת!';
                    updateControls();
               }
         }
    }

    function gameLoop() {
        update();
        draw();
        requestAnimationFrame(gameLoop);
    }

    function resetSimulation() {
        centralBody = null;
        planet = null;
        simulationRunning = false;
        simulationState = 'initial';
        velocityStartPosCanvas = null;
        velocityEndPosCanvas = null;
        trajectory = [];
        updateControls();
        //messageArea.textContent = ''; // Message updated by updateControls
        draw(); // Redraw empty canvas (with stars)
    }

    function updateControls() {
        // Disable/Enable buttons based on state
        addCentralBodyBtn.disabled = simulationState !== 'initial';
        addPlanetBtn.disabled = !(simulationState === 'placingPlanet' && centralBody && !planet);
        runSimulationBtn.disabled = simulationState !== 'readyToRun';
        // resetSimulationBtn is generally always enabled

        // Show/Hide velocity message
        velocityControlsDiv.style.display = simulationState === 'settingVelocity' ? 'block' : 'none';

        // Update instructional message based on state
        switch(simulationState) {
            case 'initial':
                messageArea.textContent = 'שלב 1: בחר "הוסף כוכב" ואז מקם אותו בחלל.';
                break;
            case 'placingCentral':
                messageArea.textContent = 'שלב 1: לחץ איפה למקם את הכוכב המסיבי!';
                break;
            case 'placingPlanet':
                messageArea.textContent = 'שלב 2: כוכב מוקם בהצלחה! בחר "הוסף כוכב לכת" ואז מקם אותו.';
                 addPlanetBtn.disabled = false; // Ensure button is enabled after central body placed
                break;
            case 'settingVelocity':
                messageArea.textContent = 'שלב 3: גרור מכוכב הלכת כדי לתת לו דחיפה ראשונית!';
                break;
            case 'readyToRun':
                messageArea.textContent = 'הכל מוכן! הפעל סימולציה, או שנה את הדחיפה הראשונית (גרור שוב).';
                break;
            case 'running':
                messageArea.textContent = 'הריקוד הקוסמי בעיצומו...';
                break;
            case 'crashed':
                 messageArea.textContent = 'התרסקות! כוכב הלכת נפל לתוך הכוכב. לחץ "איפוס" כדי להתחיל מחדש.';
                 break;
             // case 'escaped': Handled in update, message set there
            default:
                messageArea.textContent = '';
        }

         // Disable interaction buttons while running or crashed
         if (simulationState === 'running' || simulationState === 'crashed') {
             addCentralBodyBtn.disabled = true;
             addPlanetBtn.disabled = true;
             runSimulationBtn.disabled = true;
         }
    }

    // --- Event Listeners ---
    let lastMousePos = { x: 0, y: 0 }; // To track mouse position for placing preview

    addCentralBodyBtn.addEventListener('click', () => {
        if (simulationState === 'initial') {
            simulationState = 'placingCentral';
            updateControls();
        }
    });

    addPlanetBtn.addEventListener('click', () => {
        // Button is only enabled if state is 'placingPlanet' and centralBody exists
        if (simulationState === 'placingPlanet' && centralBody && !planet) {
             // Clicking the button just indicates intent, the next canvas click places it.
             updateControls(); // Message updates here
        }
    });

    runSimulationBtn.addEventListener('click', () => {
        if (simulationState === 'readyToRun' && planet && centralBody) {
            simulationRunning = true;
            simulationState = 'running';
            // Reset trajectory on run to show only the current path
            trajectory = [{ x: planet.position.x, y: planet.position.y }]; // Start trajectory at current position
            updateControls();
             // Buttons are disabled by updateControls in 'running' state
        }
    });

    resetSimulationBtn.addEventListener('click', () => {
        resetSimulation();
    });

    canvas.addEventListener('mousemove', (event) => {
         const rect = canvas.getBoundingClientRect();
         lastMousePos = { x: event.clientX, y: event.clientY }; // Store global mouse position

        if (simulationState === 'settingVelocity' && velocityStartPosCanvas) {
            velocityEndPosCanvas = { x: event.clientX - rect.left, y: event.clientY - rect.top };
            draw(); // Redraw continuously while dragging the arrow
        } else if (simulationState === 'placingCentral' || simulationState === 'placingPlanet') {
             draw(); // Redraw to show the placing preview
        }
    });


    canvas.addEventListener('mousedown', (event) => {
         const rect = canvas.getBoundingClientRect();
         const mouseX = event.clientX - rect.left;
         const mouseY = event.clientY - rect.top;
         // Convert mouse position to simulation coordinates (relative to center)
         const simX = (mouseX - canvas.width / 2) / SCALE;
         const simY = -(mouseY - canvas.height / 2) / SCALE; // Y is inverted in canvas

        if (simulationState === 'placingCentral') {
            // Place central body with large mass and size
            centralBody = new Body(simX, simY, 10000, 15, '#ffc107', 'central', 'כוכב'); // Yellow star
            simulationState = 'placingPlanet'; // Move to next step: place planet
            updateControls();
            // No need to draw here, mousemove/mouseup or next gameLoop frame will draw
        } else if (simulationState === 'placingPlanet' && centralBody && !planet) {
            // Place planet with small mass and size
            planet = new Body(simX, simY, 10, 5, '#17a2b8', 'planet', 'כוכב לכת'); // Blue planet
            // Check if planet is placed too close to central body initially to avoid immediate collision/instability
             const dx = centralBody.position.x - planet.position.x;
             const dy = centralBody.position.y - planet.position.y;
             const distance = Math.sqrt(dx*dx + dy*dy);
             const centralBodyRadiusSim = centralBody.radius / SCALE;
             const planetRadiusSim = planet.radius / SCALE;

             if (distance < centralBodyRadiusSim + planetRadiusSim + 0.5) { // Add a small buffer
                 messageArea.textContent = 'מיקום קרוב מדי לכוכב! בחר מיקום אחר.';
                 planet = null; // Discard the badly placed planet
                 // State remains placingPlanet
                 draw(); // Redraw without the planet
                 return; // Exit mouse down handler
             }

            simulationState = 'settingVelocity'; // Move to next step: set velocity
            updateControls();
            draw(); // Draw the newly placed planet

        } else if ((simulationState === 'settingVelocity' || simulationState === 'readyToRun') && planet) {
            // Allow starting velocity drag if clicked near the planet
             const planetCanvasPos = planet.getCanvasPosition();
             const clickDistanceToPlanet = Math.sqrt(
                 Math.pow(mouseX - planetCanvasPos.x, 2) +
                 Math.pow(mouseY - planetCanvasPos.y, 2)
             );
             // Check if click is close to the planet (simple hit test with buffer)
             if (clickDistanceToPlanet < planet.radius * 3) { // Allow clicking somewhat near the planet
                 simulationState = 'settingVelocity'; // Go back to setting velocity state
                 updateControls();
                 // The arrow starts at the planet's current canvas position
                 velocityStartPosCanvas = { x: planetCanvasPos.x, y: planetCanvasPos.y };
                 velocityEndPosCanvas = { x: mouseX, y: mouseY }; // Arrow points to current mouse position
                 trajectory = []; // Clear trajectory when setting new velocity
                 // Velocity will be set on mouseup
                 draw(); // Draw the initial arrow
             } else if (simulationState === 'readyToRun') {
                 // If state is readyToRun and user clicked *not* near the planet, do nothing or show a message
                 // For now, do nothing. Clicking Run button starts sim.
             }
        }
    });

    canvas.addEventListener('mouseup', (event) => {
        if (simulationState === 'settingVelocity' && velocityStartPosCanvas && velocityEndPosCanvas) {
            // Velocity was set via drag - calculate it
            const rect = canvas.getBoundingClientRect();
            const endMouseX = event.clientX - rect.left;
            const endMouseY = event.clientY - rect.top;

            // Calculate the velocity vector based on the drag
            // The vector goes from planet's center (start) to the mouse release point (end) on canvas
            const planetCanvasX = velocityStartPosCanvas.x; // This is the planet's canvas pos when drag started
            const planetCanvasY = velocityStartPosCanvas.y;

            const velocityVectorX_pixels = endMouseX - planetCanvasX;
            const velocityVectorY_pixels = endMouseY - planetCanvasY;

            // Scale the pixel vector to simulation velocity units
            // Note: The velocity vector points FROM the start point TO the end point.
            // This means a drag RIGHT applies velocity RIGHT.
            // However, convention for setting initial velocity often uses the vector *away* from the drag start.
            // Let's stick to the vector from start to end for now - drag direction == velocity direction.
            // The Y axis is inverted in canvas, so velocity.y needs adjustment.
            // A drag DOWN (positive Y pixels) should result in negative sim Y velocity.
            planet.velocity.x = velocityVectorX_pixels / SCALE / VELOCITY_DRAG_SCALE; // Sim units / time unit
            planet.velocity.y = -velocityVectorY_pixels / SCALE / VELOCITY_DRAG_SCALE; // Sim units / time unit (Y inverted)

            // Reset velocity drag state
            velocityStartPosCanvas = null;
            velocityEndPosCanvas = null;
            simulationState = 'readyToRun'; // Simulation is now ready to be run with this velocity
            updateControls();
            draw(); // Redraw without the arrow
        }
    });

     // Handle window resize to keep canvas centered and potentially resize it
     function resizeCanvas() {
         // Keep fixed size for simplicity in this structure, just redraw
         draw();
     }
     // window.addEventListener('resize', resizeCanvas); // Consider adding if layout is complex


    // --- Explanation Toggle ---
    toggleExplanationBtn.addEventListener('click', () => {
        if (explanationContent.style.display === 'none' || explanationContent.style.display === '') {
            explanationContent.style.display = 'block';
             toggleExplanationBtn.textContent = 'הסתר הסבר';
        } else {
            explanationContent.style.display = 'none';
             toggleExplanationBtn.textContent = 'מה בעצם קורה כאן? (הסבר)'; // Reset text
        }
    });


    // Initial setup
    resetSimulation(); // Set initial state and draw empty canvas
    gameLoop(); // Start the animation loop (it won't run physics updates until simulationRunning is true)

</script>
```