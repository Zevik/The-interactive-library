---
title: "הרפתקאות מסלולים פלנטריים"
english_slug: planetary-orbit-simulator
category: "פיזיקה ואסטרונומיה"
tags:
  - פיזיקה
  - אסטרונומיה
  - הדמיה
  - כבידה
  - מסלולים
  - קפלר
  - אינטראקטיבי
---
# הרפתקאות מסלולים פלנטריים

צאו למסע אינטראקטיבי בחלל! אי פעם חשבתם מה גורם לכוכבי לכת להישאר במסלולם המסתורי סביב שמש ענקית? כיצד כוח בלתי נראה מעצב את ריקודם הקוסמי? הסימולטור הזה מזמין אתכם להיות האדריכלים של מערכת כוכבים משלכם. מקמו כוכב לכת, העניקו לו מהירות התחלתית, וצפו כיצד חוקי הפיזיקה האוניברסליים שולטים בתנועתו בחלל! נסו ליצור מסלולים שונים - אליפסות, מעגלים, ואולי אפילו בריחה מוחלטת!

<div class="simulator-container">
    <canvas id="orbitalSimulatorCanvas"></canvas>
    <div class="controls">
        <h3>הגדירו את כוכב הלכת</h3>
        <div class="control-group">
            <label for="massInput">מסה פלנטרית (ביחס לכוכב המרכזי):</label>
            <input type="number" id="massInput" value="0.001" step="0.0001" min="0.00001">
        </div>
         <div class="control-group">
            <label for="radiusInput">גודל תצוגה (רדיוס פיקסלים):</label>
            <input type="number" id="radiusInput" value="5" step="1" min="1">
        </div>
        <div class="control-group">
            <label>מיקום ראשוני (לחץ על המסך):</label>
            <input type="text" id="startPosDisplay" value="(x, y)" disabled>
        </div>
         <div class="control-group">
            <label>קטור מהירות (גרור מהנקודה):</label>
             <input type="text" id="startVelDisplay" value="(vx, vy)" disabled>
        </div>

        <button id="addPlanetBtn" disabled>הוסף כוכב לכת למערכת</button>
        <button id="startStopBtn">התחל סימולציה</button>
        <button id="resetBtn">איפוס המערכת</button>
    </div>
</div>

<button class="toggle-explanation-btn">סקרנים לדעת מה עומד מאחורי הקסם? לחצו להסבר!</button>

<div class="explanation-container" style="display: none;">
    <h2>מאחורי הקלעים: כבידה, מהירות ומסלולים</h2>
    <p>הסימולטור שבו התנסיתם מדגים את העקרונות המרתקים של <a href="https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%9B%D7%91%D7%99%D7%93%D7%94_%D7%94%D7%A2%D7%95%D7%9C%D7%9E%D7%99" target="_blank">חוק הכבידה האוניברסלי של ניוטון</a> ואת <a href="https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7%D7%99_%D7%A7%D7%A4%D7%9C%D7%A8" target="_blank">חוקי קפלר</a>, המתארים את תנועת הגופים במערכות כוכבים.</p>
    <p>בליבו של כל העניין עומד כוח הכבידה: כוח משיכה הדדי הפועל בין כל שתי מסות ביקום. חוזקו של כוח זה תלוי ישירות בגודל המסות וביחס הפוך לריבוע המרחק ביניהן. הנוסחה המפורסמת של ניוטון מתארת זאת כך: $$F = G \frac{m_1 m_2}{r^2}$$. בסימולטור שלנו, הכוכב המרכזי העצום מושך אליו את כוכבי הלכת הקטנים.</p>
    <p>כדי שכוכב לכת יישאר במסלול סביב כוכב ולא יפול עליו (או יברח לחלל), הוא זקוק לשילוב מדויק של מיקום ומהירות התחלתית. כוח הכבידה מהכוכב כל הזמן "מושך" ומכופף את מסלולו של כוכב הלכת, בעוד המהירות הראשונית שהוא קיבל מנסה להמשיך בקו ישר (על פי <a href="https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7%D7%99_%D7%A0%D7%99%D7%95%D7%98%D7%9F" target="_blank">חוק ההתמד של ניוטון</a>). ה"קרב" המתמיד הזה בין הכבידה לאינרציה הוא שיוצר את המסלולים הקסומים.</p>
    <p>בהתאם למהירות ההתחלתית שהענקתם לכוכב הלכת, יכולים להתקבל מסלולים שונים:</p>
    <ul>
        <li>**מסלול אליפטי:** זהו המסלול הנפוץ ביותר בגופים כבולים (כוכבי לכת, אסטרואידים, שביטים). האליפסה היא הצורה האופיינית לתנועה תחת כוח משיכה מרכזי, כאשר הכוכב נמצא באחד משני ה"מוקדים" שלה. ככל שהמהירות ההתחלתית נמוכה מדי (אך לא אפס), האליפסה "שטוחה" יותר והמסלול קרוב יותר לכוכב בחלקו.</li>
        <li>**מסלול מעגלי:** מקרה מיוחד ויפהפה של אליפסה, המתקבל כאשר המהירות ההתחלתית היא בדיוק "המהירות המסלולית" הנכונה למרחק הנתון, ובכיוון המאונך לקו המחבר את כוכב הלכת לכוכב.</li>
        <li>**מסלול פרבולי או היפרבולי:** מתקבל כאשר המהירות ההתחלתית גבוהה מספיק כדי להתגבר על משיכת הכבידה ("מהירות מילוט"). במקרים אלו, כוכב הלכת רק עובר ליד הכוכב ואינו נלכד במסלול סגור.</li>
    </ul>
    <p>חוקי קפלר, שניסח יוהנס קפלר במאה ה-17 על בסיס תצפיות אסטרונומיות, תיארו בדיוק את התנועות הללו עוד לפני שניוטון הסביר את הסיבה הפיזית מאחוריהן. הם הבסיס להבנת המכניקה השמימית!</p>
    <p>התנסו שוב! נסו זוויות מהירות שונות, מרחקים שונים מהכוכב, וראו כיצד כל קליק וגרור שלכם מעצבים מסלול ייחודי בחלל הווירטואלי.</p>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif; /* Keep system fonts for stability, maybe specify a few */
        display: flex;
        flex-direction: column;
        align-items: center;
        background: linear-gradient(to bottom, #0b0f18, #1a2b40); /* Dark space theme */
        color: #e0e0e0; /* Light grey text */
        padding: 20px;
        line-height: 1.6;
        min-height: 100vh; /* Full viewport height */
        box-sizing: border-box;
    }

    h1 {
        color: #8ac6ee; /* Muted blue */
        text-align: center;
        margin-bottom: 20px;
        font-size: 2.5em;
        text-shadow: 0 0 8px rgba(138, 198, 238, 0.5);
    }

     h2 {
        color: #f1c40f; /* Star yellow */
        text-align: center;
        margin-bottom: 15px;
        font-size: 2em;
     }

    p {
        text-align: justify;
        max-width: 800px;
        margin: 0 auto 15px auto;
        color: #bdc3c7; /* Lighter grey for body text */
    }

    .simulator-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #1a2b40; /* Slightly lighter dark than body */
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        padding: 25px;
        margin-bottom: 30px;
        width: 100%;
        max-width: 950px;
        box-sizing: border-box;
        border: 1px solid #34495e; /* Subtle border */
    }

    canvas {
        border: 1px solid #34495e; /* Border matching container */
        background-color: #04080f; /* Deep space black */
        display: block;
        margin-bottom: 25px;
        border-radius: 10px;
        cursor: crosshair; /* Indicate interactive area */
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5); /* Inner shadow for depth */
    }

    .controls {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid */
        gap: 20px; /* Increased gap */
        justify-items: center; /* Center items in grid */
        width: 100%;
        padding-top: 15px;
        border-top: 1px solid #34495e;
    }

    .controls h3 {
        grid-column: 1 / -1; /* Span across all columns */
        text-align: center;
        margin: 0 0 15px 0;
        color: #e0e0e0;
        font-size: 1.4em;
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 100%; /* Take full grid cell width */
        max-width: 300px; /* Limit max width */
    }

    .control-group label {
        margin-bottom: 8px; /* More space */
        font-weight: normal; /* Less bold */
        color: #bdc3c7; /* Lighter grey */
        font-size: 0.95em;
    }

    .control-group input[type="number"],
    .control-group input[type="text"] {
        padding: 10px 12px; /* Increased padding */
        border: 1px solid #555;
        border-radius: 5px; /* Slightly more rounded */
        font-size: 1em;
        width: 100%;
        box-sizing: border-box;
        background-color: #2c3e50; /* Darker input background */
        color: #ecf0f1; /* Light input text */
        transition: border-color 0.3s ease;
    }

     .control-group input[type="number"]:focus,
     .control-group input[type="text"]:focus {
         border-color: #3498db; /* Highlight on focus */
         outline: none;
     }

     .control-group input[type="text"][disabled] {
         background-color: #34495e; /* Disabled background */
         color: #7f8c8d; /* Muted disabled text */
         cursor: default;
     }


    button {
        padding: 12px 20px; /* More padding */
        background-color: #3498db; /* Blue */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    button#addPlanetBtn { background-color: #2ecc71; } /* Green */
    button#startStopBtn { background-color: #e67e22; } /* Orange */
    button#resetBtn { background-color: #c0392b; } /* Red */


    button:hover:not(:disabled) {
        background-color: #2980b9; /* Darker blue */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
     button#addPlanetBtn:hover:not(:disabled) { background-color: #27ae60; }
     button#startStopBtn:hover:not(:disabled) { background-color: #d35400; }
     button#resetBtn:hover:not(:disabled) { background-color: #a12c20; }


     button:active:not(:disabled) {
         transform: scale(0.98);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
     }

    button:disabled {
        background-color: #555; /* Darker grey */
        color: #bbb;
        cursor: not-allowed;
        box-shadow: none;
    }

     .toggle-explanation-btn {
         background-color: #9b59b6; /* Purple */
         margin-top: 20px;
         margin-bottom: 20px;
         padding: 12px 25px;
         font-size: 1.1em;
     }

     .toggle-explanation-btn:hover:not(:disabled) {
         background-color: #8e44ad; /* Darker purple */
     }


    .explanation-container {
        background-color: #1a2b40; /* Same as simulator container */
        border-radius: 15px;
        padding: 25px;
        max-width: 950px;
        margin: 0 auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        color: #bdc3c7;
        border: 1px solid #34495e;
    }

     .explanation-container h2 {
        color: #f1c40f; /* Star yellow */
     }

     .explanation-container a {
         color: #8ac6ee; /* Muted blue link */
         text-decoration: none;
         transition: color 0.2s ease;
     }
     .explanation-container a:hover {
         text-decoration: underline;
         color: #3498db; /* Brighter blue on hover */
     }

     /* Basic MathJax styling for formula */
     .explanation-container mjx-container {
         display: block;
         margin: 20px 0; /* More space */
         text-align: center;
         color: #ecf0f1; /* Light color for formulas */
         font-size: 1.1em; /* Slightly larger formula */
     }

     .explanation-container ul {
         list-style: disc;
         margin-left: 20px;
         padding-left: 0;
     }
      .explanation-container li {
          margin-bottom: 8px;
      }


     /* Responsive adjustments */
    @media (max-width: 768px) {
        h1 { font-size: 2em; }
        h2 { font-size: 1.6em; }
        .simulator-container, .explanation-container {
            padding: 20px;
        }
        .controls {
            grid-template-columns: 1fr; /* Single column on small screens */
            gap: 15px;
        }
        .control-group {
            max-width: none; /* Allow full width */
        }
        button {
             width: 100%; /* Full width buttons on small screens */
             max-width: 300px; /* But keep a max-width */
             margin: 0 auto; /* Center buttons */
        }
        .toggle-explanation-btn {
             width: auto; /* Auto width for toggle button */
             max-width: none;
        }
    }
</style>

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
    // Ensure MathJax is configured properly if needed, or just let it render defaults
    // MathJax.startup.getMathjax().then(() => { /* MathJax is ready */ });


    const canvas = document.getElementById('orbitalSimulatorCanvas');
    const ctx = canvas.getContext('2d');
    const massInput = document.getElementById('massInput');
    const radiusInput = document.getElementById('radiusInput');
    const startPosDisplay = document.getElementById('startPosDisplay');
    const startVelDisplay = document.getElementById('startVelDisplay');
    const addPlanetBtn = document.getElementById('addPlanetBtn');
    const startStopBtn = document.getElementById('startStopBtn');
    const resetBtn = document.getElementById('resetBtn');
    const explanationBtn = document.querySelector('.toggle-explanation-btn');
    const explanationDiv = document.querySelector('.explanation-container');

    canvas.width = 800; // Set explicit width
    canvas.height = 600; // Set explicit height


    // Physics constants (tuned for visual simulation)
    const G = 200; // Gravitational constant - Increased for faster orbits/more visible effects
    const dt = 0.1; // Time step for simulation

    // Objects in the simulation
    const objects = [];
    let animationFrameId;
    let isRunning = false;
    let startPos = null; // For click-and-drag planet creation
    let currentVel = null;
    let isPlacing = false; // Flag to indicate if user is in placement mode (mousedown)


    // Object constructor
    class CelestialBody {
        constructor(x, y, mass, radius, color, isFixed = false) {
            this.pos = { x: x, y: y };
            this.vel = { x: 0, y: 0 };
            this.acc = { x: 0, y: 0 };
            this.mass = mass;
            this.radius = radius;
            this.color = color;
            this.isFixed = isFixed; // If true, object doesn't move (like a star)
            this.trail = []; // For drawing orbit trail
            this.maxTrailLength = 700; // Increased trail length for clearer orbits
        }

        applyForce(forceX, forceY) {
            if (!this.isFixed) {
                // F = ma => a = F/m
                this.acc.x += forceX / this.mass;
                this.acc.y += forceY / this.mass;
            }
        }

        update(dt) {
            if (!this.isFixed) {
                // Simple Euler integration (can be improved with Verlet or Runge-Kutta for accuracy, but Euler is simpler)
                this.vel.x += this.acc.x * dt;
                this.vel.y += this.acc.y * dt;
                this.pos.x += this.vel.x * dt;
                this.pos.y += this.vel.y * dt;

                // Add current position to trail
                this.trail.push({ x: this.pos.x, y: this.pos.y });
                while (this.trail.length > this.maxTrailLength) {
                    this.trail.shift(); // Remove oldest point
                }
            }
             // Reset acceleration for next step
             this.acc = { x: 0, y: 0 };
        }

        draw(ctx) {
            // Draw trail with fading effect
            if (this.trail.length > 1) {
                ctx.beginPath();
                // Draw oldest points first with more transparency
                for (let i = 0; i < this.trail.length - 1; i++) {
                    const point = this.trail[i];
                    const nextPoint = this.trail[i+1];
                    const alpha = i / this.trail.length; // Fade from 0 (oldest) to 1 (newest)
                    ctx.strokeStyle = this.color + Math.floor(alpha * 255).toString(16).padStart(2, '0'); // Color with fading alpha
                    ctx.lineWidth = 1.5; // Slightly thicker trail
                    ctx.moveTo(point.x, point.y);
                    ctx.lineTo(nextPoint.x, nextPoint.y);
                    ctx.stroke();
                }
                ctx.closePath();
            }

            // Draw object
            ctx.beginPath();
            ctx.arc(this.pos.x, this.pos.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.shadowBlur = this.isFixed ? 20 : 10; // Glow effect for star, less for planets
            ctx.shadowColor = this.color;
            ctx.fill();
            ctx.closePath();

            ctx.shadowBlur = 0; // Reset shadow for other drawings
        }
    }

    // Initialize with a central star
    function resetSimulation() {
        objects.length = 0; // Clear array
        // Add the central star - position it exactly in the center
        objects.push(new CelestialBody(canvas.width / 2, canvas.height / 2, 5000, 15, '#f1c40f', true)); // Central Star (yellow, slightly larger)

        // Reset UI state for adding planets
        startPos = null;
        currentVel = null;
        isPlacing = false;
        startPosDisplay.value = '(x, y)';
        startVelDisplay.value = '(vx, vy)';
        addPlanetBtn.disabled = true;

        // Reset simulation state
        isRunning = false;
        stopAnimation();
        startStopBtn.textContent = 'התחל סימולציה'; // Reset button text

        draw(); // Draw initial state with just the star
    }

    // Physics simulation step
    function updateSimulation() {
        // Calculate forces between objects
        for (let i = 0; i < objects.length; i++) {
            for (let j = i + 1; j < objects.length; j++) {
                const obj1 = objects[i];
                const obj2 = objects[j];

                const dx = obj2.pos.x - obj1.pos.x;
                const dy = obj2.pos.y - obj1.pos.y;
                const distanceSq = dx * dx + dy * dy;
                const distance = Math.sqrt(distanceSq);

                // Avoid division by zero or extremely large forces if objects are too close
                // Add a small epsilon or check for collision if needed in more complex sims
                const minDistance = obj1.radius + obj2.radius; // Simple collision radius
                if (distance < minDistance) {
                    // Handle collision? For this sim, we'll let them pass through for simplicity
                    // or slightly adjust distance to minDistance to prevent extreme forces.
                    // Let's prevent extreme force by capping distanceSq
                    const safeDistanceSq = Math.max(distanceSq, minDistance * minDistance);
                     const forceMagnitude = (G * obj1.mass * obj2.mass) / safeDistanceSq;

                     // Calculate force components
                     const forceX = forceMagnitude * (dx / distance); // Use actual distance for direction
                     const forceY = forceMagnitude * (dy / distance);

                     // Apply forces
                     obj1.applyForce(forceX, forceY);
                     obj2.applyForce(-forceX, -forceY);

                } else if (distance > 0) {
                     const forceMagnitude = (G * obj1.mass * obj2.mass) / distanceSq;

                     // Calculate force components
                     const forceX = forceMagnitude * (dx / distance);
                     const forceY = forceMagnitude * (dy / distance);

                     // Apply forces
                     obj1.applyForce(forceX, forceY);
                     obj2.applyForce(-forceX, -forceY);
                }


            }
        }

        // Update positions and velocities
        for (const obj of objects) {
            obj.update(dt);

            // Basic boundary check to remove objects that fly offscreen
            if (obj.pos.x < -100 || obj.pos.x > canvas.width + 100 || obj.pos.y < -100 || obj.pos.y > canvas.height + 100) {
                 if (!obj.isFixed) { // Don't remove the star
                     objects.splice(objects.indexOf(obj), 1);
                     console.log("Object went offscreen, removed."); // Optional: log removal
                 }
            }
        }
    }

    // Drawing function
    function draw() {
        // Clear canvas
        ctx.fillStyle = '#04080f'; // Use the deep space background color
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw all objects
        for (const obj of objects) {
            obj.draw(ctx);
        }

        // Draw velocity vector preview if placing a planet
        if (startPos && isPlacing) { // Only draw while dragging (isPlacing is true)
            ctx.strokeStyle = '#3498db'; // Blue line
            ctx.lineWidth = 3; // Thicker line
            ctx.lineCap = 'round'; // Rounded ends

            ctx.beginPath();
            ctx.moveTo(startPos.x, startPos.y);
            ctx.lineTo(startPos.x + currentVel.x, startPos.y + currentVel.y);
            ctx.stroke();

            // Draw a clearer arrow head
             const arrowHeadSize = 15; // Size of the arrowhead
             const angle = Math.atan2(currentVel.y, currentVel.x);
             ctx.beginPath();
             ctx.moveTo(startPos.x + currentVel.x, startPos.y + currentVel.y);
             ctx.lineTo(startPos.x + currentVel.x - arrowHeadSize * Math.cos(angle - Math.PI / 7), startPos.y + currentVel.y - arrowHeadSize * Math.sin(angle - Math.PI / 7));
             ctx.moveTo(startPos.x + currentVel.x, startPos.y + currentVel.y);
             ctx.lineTo(startPos.x + currentVel.x - arrowHeadSize * Math.cos(angle + Math.PI / 7), startPos.y + currentVel.y - arrowHeadSize * Math.sin(angle + Math.PI / 7));
             ctx.strokeStyle = '#3498db';
             ctx.lineWidth = 3;
             ctx.stroke();
        }
    }

    // Main animation loop
    function animate() {
        if (isRunning) {
            updateSimulation();
        }
        draw(); // Always draw, even if paused, to show current state and potential vector preview
        animationFrameId = requestAnimationFrame(animate);
    }

    function startAnimation() {
        if (!isRunning) {
            isRunning = true;
            startStopBtn.textContent = 'השהה סימולציה';
            animate(); // Start the animation loop
        }
    }

    function stopAnimation() {
        isRunning = false;
        startStopBtn.textContent = 'התחל סימולציה';
        // The animate loop continues to draw the paused state
    }


    // --- Event Listeners ---

    // Toggle Explanation
    explanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'סקרנים לדעת מה עומד מאחורי הקסם? לחצו להסבר!';
    });

    // Canvas click/drag for adding planet
    canvas.addEventListener('mousedown', (e) => {
        if (!isRunning) { // Only allow placing if simulation is stopped
             const rect = canvas.getBoundingClientRect();
             const x = e.clientX - rect.left;
             const y = e.clientY - rect.top;

             // Check if clicking near an existing planet or star
             for (const obj of objects) {
                 const dist = Math.sqrt(Math.pow(x - obj.pos.x, 2) + Math.pow(y - obj.pos.y, 2));
                 if (dist < obj.radius + 5) { // Allow a small buffer
                     console.log("Clicked too close to an existing object.");
                     // Optionally, select the object for editing? Or just prevent placing.
                     // For now, just prevent placing right on top.
                     startPos = null; // Cancel placement attempt
                     isPlacing = false;
                     return;
                 }
             }


             startPos = { x: x, y: y };
             currentVel = { x: 0, y: 0 }; // Start with zero velocity vector
             isPlacing = true; // Start placing mode
             startPosDisplay.value = `(${x.toFixed(0)}, ${y.toFixed(0)})`;
             startVelDisplay.value = `(${currentVel.x.toFixed(1)}, ${currentVel.y.toFixed(1)})`;
             addPlanetBtn.disabled = true; // Disable until a velocity is defined (mousemove)
             draw(); // Draw the starting point
        }
    });

    canvas.addEventListener('mousemove', (e) => {
        if (startPos && isPlacing && !isRunning) { // Only track move if in placing mode and simulation is stopped
             const rect = canvas.getBoundingClientRect();
             const x = e.clientX - rect.left;
             const y = e.clientY - rect.top;

             // Velocity is vector from startPos to current mouse pos
             currentVel = { x: (x - startPos.x) * 0.5, y: (y - startPos.y) * 0.5 }; // Scale velocity input

             // Display velocity, limit decimals
             startVelDisplay.value = `(${currentVel.x.toFixed(1)}, ${currentVel.y.toFixed(1)})`;

             // Enable add button only if a significant velocity vector exists
             const velocityMagnitudeSq = currentVel.x * currentVel.x + currentVel.y * currentVel.y;
             const minVelocitySq = 10 * 10; // Require a minimum drag distance (10 pixels before scaling)
             addPlanetBtn.disabled = velocityMagnitudeSq < (minVelocitySq * 0.5 * 0.5); // Check squared values

             draw(); // Redraw to show updated velocity vector
        }
    });

     canvas.addEventListener('mouseup', (e) => {
        if (startPos && isPlacing && !isRunning) {
             isPlacing = false; // End placing mode
             // The velocity vector is already calculated in mousemove
             // If mouseup happens right after mousedown, velocity will be near {0,0} and button remains disabled.
             // If the button is enabled, the user can now click "Add Planet".
        }
    });


    addPlanetBtn.addEventListener('click', () => {
        // Ensure button is enabled, startPos and currentVel are set, and simulation is stopped
        if (!addPlanetBtn.disabled && startPos && currentVel && !isRunning) {
            const mass = parseFloat(massInput.value);
            const radius = parseInt(radiusInput.value, 10);

            // Validate inputs
             if (isNaN(mass) || mass <= 0 || isNaN(radius) || radius <= 0) {
                 alert("אנא הזינו מסה ורדיוס חוקיים (חיוביים).");
                 return;
             }

            // Select a cosmic color for the new planet
            const cosmicColors = [
                '#3498db', // Blue (Earth-like water)
                '#e74c3c', // Red (Mars-like, or volcanic)
                '#9b59b6', // Purple (Neptune/Uranus-like)
                '#1abc9c', // Teal (Exoplanet atmosphere)
                '#f39c12', // Orange (Gas giant storms)
                '#d35400'  // Dark Orange (Rusty surface)
            ];
            // Cycle through colors, skipping the first one which is the star's color
            const color = cosmicColors[(objects.length - 1) % cosmicColors.length];

            const newPlanet = new CelestialBody(startPos.x, startPos.y, mass, radius, color);
            newPlanet.vel = { x: currentVel.x, y: currentVel.y }; // Set initial velocity based on drag
            objects.push(newPlanet);

            console.log("Added planet:", { pos: newPlanet.pos, vel: newPlanet.vel, mass: mass, radius: radius, color: color });

            // Reset UI state for next planet placement
            startPos = null;
            currentVel = null;
            startPosDisplay.value = '(x, y)';
            startVelDisplay.value = '(vx, vy)';
            addPlanetBtn.disabled = true; // Disable again until next placement attempt
            draw(); // Draw with the new planet
        }
    });


    startStopBtn.addEventListener('click', () => {
        if (isRunning) {
            stopAnimation();
        } else {
            // Ensure there's at least the star and one planet before starting
            if (objects.length > 1) {
                startAnimation();
            } else {
                alert("אנא הוסיפו כוכב לכת למערכת לפני ההתחלה.");
            }
        }
    });

    resetBtn.addEventListener('click', () => {
        stopAnimation(); // Stop simulation first
        resetSimulation(); // Then reset everything
    });


    // Initial setup - Draw only the star and wait for user interaction
    resetSimulation();
    animate(); // Start the drawing loop, but simulation is paused initially
</script>
---