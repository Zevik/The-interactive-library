---
title: "ריקוד כבידתי: צור מסלולים בחלל!"
english_slug: cosmic-dance-create-orbits-in-space
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה
  - אסטרונומיה
  - כבידה
  - מסלולים
  - קפלר
  - סימולציה
---
# ריקוד כבידתי: צור מסלולים בחלל!

הצטרפו אלינו למסע בחלל כדי לגלות את כוח הכבידה! האם אי פעם תהיתם איך כוכבי לכת נשארים במסלולם? או מה קובע את צורת המסלול שלהם? כאן תוכלו לשחק עם הכוחות הקוסמיים בעצמכם וליצור מערכות כבידה מרתקות. בואו נתחיל!

<!-- Interactive Application -->
<div class="simulator-container">
    <div class="controls">
        <h3>הוספת גוף חדש:</h3>
        <label for="bodyType">סוג גוף:</label>
        <select id="bodyType">
            <option value="star">כוכב (עצום!)</option>
            <option value="planet">כוכב לכת (קטן ומהיר)</option>
        </select>
        <label for="mass">מסה (משפיעה על הכבידה):</label>
        <input type="number" id="mass" value="1000" min="1" step="10">
        <p id="placement-hint">לחץ על המסך כדי למקם כוכב...</p>

        <h3>שליטה בסימולציה:</h3>
        <button id="startSim">התחל ריקוד</button>
        <button id="stopSim" disabled>עצור הכל</button>
        <button id="resetSim">התחל מחדש</button>
         <p class="sim-status" id="simStatus">מוכן ליצירה!</p>
    </div>
    <canvas id="simulationCanvas"></canvas>
</div>

<!-- Styling -->
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
        line-height: 1.7;
        color: #333;
        background-color: #f4f7f6;
    }

    h1, h2, h3 {
        color: #0a3d62; /* Dark blue for headings */
        text-align: right;
    }

    .simulator-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
        margin: 30px auto;
        padding: 25px;
        border-radius: 12px;
        background: linear-gradient(145deg, #e6e9eb, #ffffff);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        max-width: 900px;
    }

    .controls {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        width: 100%;
        max-width: 700px;
        text-align: right;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid */
        gap: 15px;
    }

    .controls h3 {
        grid-column: 1 / -1; /* Span full width */
        margin-top: 0;
        margin-bottom: 15px;
        color: #1c658c; /* Medium blue */
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
    }

    .controls label {
        display: block; /* Labels above inputs */
        margin-bottom: 5px;
        font-weight: bold;
        color: #555;
        font-size: 0.95em;
    }

    .controls input[type="number"],
    .controls select {
        width: 100%; /* Full width within grid item */
        padding: 10px 12px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box; /* Include padding in width */
        font-size: 1em;
    }

     .controls p {
         margin-top: 5px;
         font-size: 0.9em;
         color: #555;
         grid-column: 1 / -1; /* Span full width */
         text-align: center;
         margin-bottom: 0;
     }

     .sim-status {
         font-weight: bold;
         color: #007bff; /* Blue status */
     }


    .controls button {
        padding: 12px 20px;
        margin-top: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        text-align: center;
    }

    #startSim {
        background-color: #28a745; /* Green */
        color: white;
    }
    #startSim:hover:enabled { background-color: #218838; transform: translateY(-1px); }

    #stopSim {
        background-color: #ffc107; /* Yellow/Orange */
        color: #333;
    }
     #stopSim:hover:enabled { background-color: #e0a800; transform: translateY(-1px); }


    #resetSim {
        background-color: #dc3545; /* Red */
        color: white;
    }
     #resetSim:hover:enabled { background-color: #c82333; transform: translateY(-1px); }

    .controls button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        transform: none;
    }


    #simulationCanvas {
        border: 1px solid #555; /* Darker border */
        background-color: #0a0a2a; /* Deep space blue/black */
        width: 800px;
        height: 600px;
        display: block;
        margin: 0 auto;
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
        cursor: crosshair; /* Indicate interactivity */
    }

    .explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .explanation-button:hover {
        background-color: #0056b3;
         transform: translateY(-1px);
    }

    .explanation {
        margin: 30px auto;
        padding: 25px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        display: none; /* Initially hidden */
        max-width: 900px;
        text-align: right;
    }

    .explanation h2 {
        color: #1c658c;
        border-bottom: 1px solid #eee;
        padding-bottom: 12px;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    .explanation h3 {
        color: #0a3d62;
        margin-top: 25px;
        margin-bottom: 12px;
        font-size: 1.3em;
    }

    .explanation p {
        line-height: 1.8;
        text-align: justify;
        margin-bottom: 15px;
        color: #444;
    }

     .explanation ul {
         margin-bottom: 15px;
         padding-right: 20px;
     }

     .explanation li {
         margin-bottom: 8px;
     }

     /* Style for the velocity vector line during drag */
    #simulationCanvas.drawing-vector {
        cursor: crosshair; /* Or a specific vector cursor if possible */
    }


</style>

<!-- Show/Hide Explanation Button -->
<button class="explanation-button" onclick="toggleExplanation()">הסבר על ריקוד הגופים (קראו אחרי ששיחקתם!)</button>

<!-- Hidden Explanation -->
<div id="explanation" class="explanation">
    <h2>מאחורי הקלעים של ריקוד הכבידה</h2>

    <h3>מה מניע את הגופים? כוח הכבידה!</h3>
    <p>כפי שחוויתם בסימולציה, כוח הכבידה הוא הכוח המרכזי שמעצב את היקום בקנה מידה גדול. זהו אותו כוח שמשאיר אתכם על כסאכם, וגם אותו כוח אדיר שמחזיק גלקסיות שלמות יחד. בסימולציה, כל גוף בעל מסה מושך אליו את שאר הגופים. ככל שמסה גדולה יותר, המשיכה חזקה יותר. וככל שהמרחק בין הגופים גדל, המשיכה נחלשת - מהר מאוד!</p>

    <h3>למה נוצרים מסלולים במקום התנגשויות?</h3>
    <p>זו השאלה המרכזית! אם רק היה כוח משיכה, הכל היה נופל למרכז. אבל הגופים בחלל (כמו כוכבי הלכת ששתלתם) הם גם בעלי **מהירות התחלתית**. כשהצבתם כוכב לכת וגררתם, בעצם נתתם לו דחיפה ראשונית. שילוב של הדחיפה הזו (שגורמת לגוף לרצות לנוע בקו ישר) עם משיכת הכבידה המתמדת (שמושכת אותו לכיוון המסה הגדולה) יוצר תנועה מעגלית או אליפטית סביב המרכז הכבידתי. הגוף נופל כל הזמן לכיוון המרכז, אך בגלל מהירותו הצדדית, הוא כל הזמן 'מחמיץ' ונע סביבו!</p>

    <h3>חוקי קפלר: ריקוד מדויק</h3>
    <p>התנועה הזו אינה כאוטית, אלא מצייתת לחוקים מופלאים שגילה יוהנס קפלר לפני מאות שנים, הרבה לפני שניוטון הסביר את הכבידה. אלו "כללי הריקוד" הקוסמי:</p>
    <ul>
        <li>**חוק 1 - צורת המסלול:** כל גוף המקיף גוף אחר בגלל כבידה נע במסלול אליפטי (אליפסה היא צורה פחוסה של מעגל), והגוף המושך (כמו כוכב שמש) נמצא באחד ה'מוקדים' של האליפסה. לפעמים, אם נתתם מהירות התחלתית מדויקת, קיבלתם מסלול מעגלי מושלם - זהו מקרה מיוחד של אליפסה.</li>
        <li>**חוק 2 - המהירות המשתנה:** גופים נעים מהר יותר כשהם קרובים יותר לגוף המושך, ולאט יותר כשהם רחוקים. בסימולציה, אם יצרתם מסלול אליפטי, שימו לב איך מהירות כוכב הלכת משתנה כשהוא מתקרב ומתרחק מהכוכב המרכזי. זה קורה כי כוח הכבידה חזק יותר כשהם קרובים, והוא מאיץ את הגוף.</li>
        <li>**חוק 3 - קשר בין גודל למחזור:** ככל שהמסלול גדול יותר (או ככל שהגוף המושך פחות מאסיבי), כך לוקח לגוף המקיף יותר זמן להשלים סיבוב אחד. נסו ליצור מסלולים בגדלים שונים סביב אותו כוכב, או מסלולים דומים סביב כוכבים בעלי מסה שונה, ותראו איך זמן ההקפה משתנה!</li>
    </ul>

    <h3>מה קובע אם המסלול יהיה סגור (אליפסה/מעגל) או פתוח (היפרבולה)?</h3>
    <p>זה תלוי ב"אנרגיה" של הגוף המקיף. אם יש לו מספיק מהירות (אנרגיה קינטית) ביחס לכוח המשיכה במיקום ההתחלתי (אנרגיה פוטנציאלית), הוא ישתחרר מאחיזת הכבידה ויתרחק לנצח במסלול פתוח (נראה כמו קשת שאינה נסגרת - היפרבולה או פרבולה). אם המהירות ההתחלתית נמוכה יותר, כוח הכבידה יצליח להחזיק אותו קשור, והמסלול יהיה סגור - אליפסה או מעגל. נסו לשחק עם עוצמת הגרירה (המהירות ההתחלתית) כדי ליצור סוגי מסלולים שונים ולראות מתי גוף נשאר קרוב ומתי הוא בורח!</p>

</div>

<!-- JavaScript -->
<script>
    const canvas = document.getElementById('simulationCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startSim');
    const stopButton = document.getElementById('stopSim');
    const resetButton = document.getElementById('resetSim');
    const bodyTypeSelect = document.getElementById('bodyType');
    const massInput = document.getElementById('mass');
    const placementHint = document.getElementById('placement-hint');
    const explanationDiv = document.getElementById('explanation');
    const simStatus = document.getElementById('simStatus');


    canvas.width = 800; // Match CSS width
    canvas.height = 600; // Match CSS height

    let bodies = [];
    let simulationRunning = false;
    let animationFrameId = null;
    const G = 0.0005; // Gravitational constant - scaled for simulation
    const TIME_STEP = 0.2; // Simulation time step - smaller is more accurate but slower

    // Interaction for planet placement
    let isDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;

    // Visual tuning
    const STAR_COLOR = '#FFD700'; // Gold
    const PLANET_COLOR = '#ADD8E6'; // Light Blue
    const PATH_COLOR = 'rgba(255, 255, 255, 0.3)'; // Faint white trail
    const VECTOR_COLOR = '#32CD32'; // Lime green for velocity vector
    const STAR_BASE_RADIUS = 10;
    const PLANET_BASE_RADIUS = 3;
    const MAX_PATH_POINTS = 300; // Limit trail length


    // Event Listeners
    startButton.addEventListener('click', startSimulation);
    stopButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);
    canvas.addEventListener('mousedown', handleCanvasMousedown);
    canvas.addEventListener('mousemove', handleCanvasMousemove);
    canvas.addEventListener('mouseup', handleCanvasMouseup);
    bodyTypeSelect.addEventListener('change', updatePlacementHint);

    // Update hint text based on selected body type
    function updatePlacementHint() {
        if (bodyTypeSelect.value === 'star') {
            placementHint.textContent = 'לחץ על המסך כדי למקם כוכב (גוף מרכזי)...';
             massInput.value = 1000;
             massInput.step = 10;
        } else { // planet
            placementHint.textContent = 'לחץ וגרור על המסך כדי להשיק כוכב לכת (קבע מהירות התחלתית)...';
            massInput.value = 1;
            massInput.step = 0.1;
        }
         simStatus.textContent = 'מוכן ליצירה!';
    }

    // Handle mouse down for dragging
    function handleCanvasMousedown(event) {
        if (simulationRunning) return; // Cannot place bodies while simulating

        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        const bodyType = bodyTypeSelect.value;
        const mass = parseFloat(massInput.value);

        if (bodyType === 'star') {
            // Add star immediately on click
             addBody(x, y, mass, 0, 0, bodyType);
             draw(); // Redraw to show the new star
             simStatus.textContent = `נוסף כוכב במסה ${mass.toFixed(1)}. מוכן להוסיף גופים נוספים!`;
        } else { // planet - start drag
            isDragging = true;
            dragStartX = x;
            dragStartY = y;
            canvas.classList.add('drawing-vector'); // Visual cue for drawing
             simStatus.textContent = 'גרור כדי להגדיר מהירות...';
        }
    }

    // Handle mouse move for drawing the velocity vector
    function handleCanvasMousemove(event) {
        if (!isDragging || simulationRunning) return;

        // We don't add bodies here, just redraw to show the line
        draw(); // Redraw bodies
        const rect = canvas.getBoundingClientRect();
        const currentX = event.clientX - rect.left;
        const currentY = event.clientY - rect.top;

        // Draw the potential velocity vector
        ctx.beginPath();
        ctx.strokeStyle = VECTOR_COLOR;
        ctx.lineWidth = 2;
        ctx.moveTo(dragStartX, dragStartY);
        ctx.lineTo(currentX, currentY);
        ctx.stroke();
         ctx.closePath();

         // Draw hint text
         const dx = currentX - dragStartX;
         const dy = currentY - dragStartY;
         const speed = Math.sqrt(dx * dx + dy * dy) * 0.1; // Scale speed for display
         ctx.fillStyle = VECTOR_COLOR;
         ctx.font = '14px Heebo';
         ctx.textAlign = 'left';
         ctx.fillText(`מהירות: ${speed.toFixed(1)}`, currentX + 10, currentY - 10);
    }

    // Handle mouse up for adding the planet with velocity
    function handleCanvasMouseup(event) {
        if (!isDragging || simulationRunning) return;

        const rect = canvas.getBoundingClientRect();
        const endX = event.clientX - rect.left;
        const endY = event.clientY - rect.top;

        const mass = parseFloat(massInput.value);
        // Velocity is determined by the drag vector (scaled)
        // We want the planet to start at dragStartX, dragStartY
        // And have velocity based on the vector FROM dragStartX, dragStartY TO endX, endY
        // A longer drag = faster velocity
        const vx = (endX - dragStartX) * 0.1; // Scaling factor for velocity
        const vy = (endY - dragStartY) * 0.1;

        addBody(dragStartX, dragStartY, mass, vx, vy, 'planet');

        isDragging = false;
        canvas.classList.remove('drawing-vector'); // Remove visual cue
        draw(); // Final redraw
         simStatus.textContent = `נוסף כוכב לכת במסה ${mass.toFixed(1)} ומהירות התחלתית. מוכן להוסיף גופים נוספים!`;
    }


    // Add a body to the simulation
    function addBody(x, y, mass, vx, vy, type) {
        const radius = type === 'star' ? STAR_BASE_RADIUS + Math.log(mass) * 0.7 : PLANET_BASE_RADIUS + Math.log(Math.max(1, mass)) * 2; // Radius scaled by log mass
        const color = type === 'star' ? STAR_COLOR : PLANET_COLOR;

        bodies.push({
            x: x,
            y: y,
            mass: mass,
            vx: vx,
            vy: vy,
            type: type,
            radius: radius,
            color: color,
            path: type === 'planet' ? [{x: x, y: y}] : [], // Store path for planets
             creationTime: Date.now() // For potential pulse animation
        });

         // Simple creation pulse animation (visual feedback)
         const addedBody = bodies[bodies.length - 1];
         addedBody.pulsing = true;
         addedBody.pulseStartTime = Date.now();
         addedBody.initialRadius = radius;

    }

     // Update function - calculates forces and updates positions
    function updateSimulation() {
         // Calculate forces for each body
        const forces = bodies.map(() => ({ fx: 0, fy: 0 }));

        for (let i = 0; i < bodies.length; i++) {
            const body1 = bodies[i];
            for (let j = i + 1; j < bodies.length; j++) {
                const body2 = bodies[j];

                const dx = body2.x - body1.x;
                const dy = body2.y - body1.y;
                const distSq = dx * dx + dy * dy;
                // Add a small constant to denominator to prevent infinite force at dist=0
                const dist = Math.sqrt(distSq);
                const safeDistSq = distSq + 0.1; // Prevent division by zero/near zero

                const forceMagnitude = G * body1.mass * body2.mass / safeDistSq;

                const fx = forceMagnitude * (dx / dist); // Use actual dist for direction
                const fy = forceMagnitude * (dy / dist);

                forces[i].fx += fx;
                forces[i].fy += fy;
                forces[j].fx -= fx; // Newton's third law
                forces[j].fy -= fy;
            }
        }

        // Update velocities and positions using calculated forces
        for (let i = 0; i < bodies.length; i++) {
            const body = bodies[i];
             // Skip static bodies if any, though none are static in this setup
            // if (body.type === 'star' && body.mass > some_threshold) continue; // Example: make very large stars static

            const ax = forces[i].fx / body.mass;
            const ay = forces[i].fy / body.mass;

            // Verlet integration (more stable than simple Euler for orbits)
            // Calculate new position
            const newX = body.x + body.vx * TIME_STEP + 0.5 * ax * TIME_STEP * TIME_STEP;
            const newY = body.y + body.vy * TIME_STEP + 0.5 * ay * TIME_STEP * TIME_STEP;

            // Calculate new velocity (requires new forces, or use midpoint method)
            // Simpler Verlet: approximate velocity using (newPos - oldPos) / TIME_STEP
             body.vx = (newX - body.x) / TIME_STEP;
             body.vy = (newY - body.y) / TIME_STEP;

            body.x = newX;
            body.y = newY;

            // Store path point for planets, limit length
            if (body.type === 'planet') {
                 body.path.push({x: body.x, y: body.y});
                 if (body.path.length > MAX_PATH_POINTS) {
                     body.path.shift(); // Remove oldest point
                 }
            }
        }
    }


    // Draw the current state of the simulation
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#0a0a2a'; // Background color
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        bodies.forEach(body => {
             // Draw path for planets
             if (body.type === 'planet' && body.path.length > 1) {
                 ctx.beginPath();
                 ctx.strokeStyle = PATH_COLOR;
                 ctx.lineWidth = 1.5;
                 ctx.moveTo(body.path[0].x, body.path[0].y);
                 for (let i = 1; i < body.path.length; i++) {
                     // Add a subtle fade or thinner line towards the tail if desired (more complex)
                     ctx.lineTo(body.path[i].x, body.path[i].y);
                 }
                 ctx.stroke();
                 ctx.closePath();
             }

            // Draw body
            ctx.beginPath();
             let currentRadius = body.radius;
             // Apply pulse effect if active
             if (body.pulsing) {
                 const elapsed = Date.now() - body.pulseStartTime;
                 const pulseDuration = 500; // milliseconds
                 if (elapsed < pulseDuration) {
                     const progress = elapsed / pulseDuration;
                     const scale = 1 + Math.sin(progress * Math.PI) * 0.5; // Pulse out and back
                     currentRadius = body.initialRadius * scale;
                 } else {
                     body.pulsing = false; // End pulse
                     currentRadius = body.initialRadius; // Reset radius
                 }
             }

            ctx.arc(body.x, body.y, currentRadius, 0, Math.PI * 2);
            ctx.fillStyle = body.color;
            ctx.fill();
            ctx.closePath();

             // Optional: Add a small glow or halo to stars
             if (body.type === 'star') {
                 ctx.beginPath();
                 ctx.arc(body.x, body.y, currentRadius + 5, 0, Math.PI * 2);
                 ctx.fillStyle = 'rgba(255, 215, 0, 0.2)'; // Faint glow
                 ctx.fill();
                 ctx.closePath();
             }
        });
    }

    // Main simulation loop
    function simulate() {
        if (simulationRunning) {
            updateSimulation();
            draw();
            animationFrameId = requestAnimationFrame(simulate);
        }
    }

    // Start the simulation
    function startSimulation() {
        if (!simulationRunning && bodies.length > 0) { // Only start if not running and there are bodies
            simulationRunning = true;
            startButton.disabled = true;
            stopButton.disabled = false;
             simStatus.textContent = 'הסימולציה פועלת... צפו בריקוד!';
            simulate(); // Start the animation loop
        } else if (bodies.length === 0) {
             simStatus.textContent = 'הוסף גופים לפני ההפעלה!';
        }
    }

    // Stop the simulation
    function stopSimulation() {
        simulationRunning = false;
        startButton.disabled = false;
        stopButton.disabled = true;
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
         simStatus.textContent = 'הסימולציה הושהתה.';
    }

    // Reset the simulation
    function resetSimulation() {
        stopSimulation();
        bodies = []; // Clear all bodies
        draw(); // Clear canvas
        // Reset inputs to default
        bodyTypeSelect.value = 'star';
        massInput.value = 1000;
        massInput.step = 10;
        updatePlacementHint(); // Reset hint text
        isDragging = false;
        canvas.classList.remove('drawing-vector');
         simStatus.textContent = 'הסימולציה אופסה. התחילו ליצור!';
    }

    // Toggle explanation visibility
    function toggleExplanation() {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
             // Optional: scroll to explanation
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
        } else {
            explanationDiv.style.display = 'none';
        }
    }

    // Initial setup
    updatePlacementHint(); // Initialize hint text and input values
    draw(); // Draw initial empty canvas


</script>