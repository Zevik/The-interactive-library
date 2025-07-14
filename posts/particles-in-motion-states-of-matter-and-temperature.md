---
title: "ריקוד החלקיקים: מסע למצבי צבירה ואנרגיה"
english_slug: particles-in-motion-states-of-matter-and-temperature
category: "פיזיקה"
tags:
  - מצבי צבירה
  - חלקיקים
  - טמפרטורה
  - תנועה תרמית
  - מודל חלקיקי
---
# ריקוד החלקיקים: מסע למצבי צבירה ואנרגיה

אי פעם תהיתם מדוע קוביית קרח קשה ויציבה, מים זורמים בחופשיות, ואדי מים מתפשטים בכל מקום? הסוד אינו בחומר עצמו, אלא בכמות האנרגיה שיש לחלקיקים הזעירים המרכיבים אותו! בואו לצלול לרמה המיקרוסקופית ולגלות כיצד טמפרטורה מניעה את החלקיקים וקובעת את "מצב הריקוד" שלהם - מצב הצבירה.

<div id="simulation-container">
    <canvas id="particle-canvas"></canvas>
    <div id="controls">
        <label for="temp-slider">אנרגיה (טמפרטורה):</label>
        <input type="range" id="temp-slider" min="0" max="100" value="30">
        <div id="temp-display">30 °C (מוצק)</div>
    </div>
</div>

<style>
    /* סגנונות כלליים לקונטיינר */
    #simulation-container {
        width: 100%;
        max-width: 700px; /* Increased max width for better visual */
        margin: 20px auto;
        border: 1px solid #d0d0d0; /* Softer border */
        border-radius: 12px; /* More rounded corners */
        overflow: hidden;
        background: linear-gradient(to bottom right, #e8f5ff, #cceeff); /* Subtle gradient */
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px; /* More padding */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15); /* Deeper shadow */
        font-family: 'Arial', sans-serif; /* Standard font */
    }

    /* סגנונות לקנבס */
    #particle-canvas {
        width: 100%;
        height: 350px; /* Increased height */
        background-color: #ffffff; /* White background */
        border-radius: 8px; /* Rounded corners for canvas */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); /* Inner shadow */
        box-sizing: border-box;
        margin-bottom: 15px; /* Space below canvas */
    }

    /* סגנונות לבקרה */
    #controls {
        margin-top: 15px;
        display: flex;
        align-items: center;
        width: 100%;
        justify-content: center; /* Center controls horizontally */
        flex-wrap: wrap;
        gap: 10px; /* Spacing between items */
    }

    #controls label {
        margin-inline-end: 0; /* Reset margin */
        font-weight: bold;
        color: #333; /* Darker text */
        min-width: 80px; /* Adjust min width */
        text-align: end;
    }

    #controls input[type="range"] {
        flex-grow: 1;
        max-width: 350px; /* Limit slider width */
        accent-color: #007bff; /* Blue accent color for slider */
    }

    #temp-display {
        min-width: 150px; /* Ensure temp display has enough space */
        text-align: start;
        font-weight: bold;
        color: #0056b3; /* Match button hover color */
    }

    /* סגנונות לכפתור הסבר */
    button {
        display: block;
        margin: 25px auto; /* More space above/below */
        padding: 12px 25px; /* Larger padding */
        font-size: 17px; /* Slightly larger font */
        cursor: pointer;
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
        box-shadow: 0 3px 6px rgba(0,0,0,0.1); /* Button shadow */
    }

    button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    button:active {
        transform: scale(0.98); /* Slight press effect */
    }

    /* סגנונות לבלוק ההסבר */
    #explanation {
        margin-top: 30px; /* More space above */
        padding: 20px;
        border: 1px solid #d0d0d0;
        border-radius: 12px;
        background-color: #f9f9f9; /* Light grey background */
        display: none; /* Hidden by default */
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        line-height: 1.7; /* Improved readability */
        color: #333;
        font-family: 'Arial', sans-serif;
    }

    #explanation h2 {
        margin-top: 0;
        color: #0056b3; /* Match heading color */
        border-bottom: 2px solid #eee; /* Subtle separator */
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    #explanation h3 {
        color: #007bff; /* Primary color for subheadings */
        margin-top: 20px;
        margin-bottom: 8px;
        border-left: 4px solid #007bff; /* Accent border */
        padding-left: 10px;
    }

    #explanation p {
        margin-bottom: 15px;
        text-align: justify; /* Justify text for cleaner look */
    }

    #explanation ul {
        list-style: disc inside; /* Disc bullets */
        padding-left: 0; /* Remove default padding */
        margin-bottom: 15px;
    }

    #explanation li {
        margin-bottom: 10px;
    }

    #explanation li strong {
        color: #555; /* Slightly different color for bold text */
    }
</style>

<button id="toggle-explanation">מה קורה כאן בעצם?</button>

<div id="explanation">
    <h2>מסע אל הבלתי נראה: הבנת מצבי צבירה</h2>

    <p>כל דבר שאתם רואים, נוגעים או מרגישים עשוי מחלקיקים זעירים שנקראים אטומים ומולקולות. החלקיקים האלה אף פעם לא באמת נחים לגמרי! הם תמיד בתנועה, אבל אופי התנועה שלהם משתנה בצורה דרמטית כתלות באנרגיה שיש להם. ה<strong>טמפרטורה</strong> היא בעצם מדד לכמה אנרגיה קינטית (אנרגיית תנועה) יש לחלקיקים בממוצע.</p>

    <p><strong>בואו נראה איך האנרגיה הזו קובעת את מצב הצבירה:</strong></p>

    <h3>🕺 מוצק (אנרגיה נמוכה): הריקוד במקום</h3>
    <p>כאשר האנרגיה נמוכה, החלקיקים קרובים מאוד זה לזה ומסודרים לרוב במבנה קבוע ומאורגן, כמו חיילים במסדר או לבנים בקיר (מבנה גבישי). הם לא יכולים לשנות מקום, אבל הם בהחלט לא קופאים על שמריו! הם רוטטים ומתנדנדים בעדינות מסביב לנקודות קבועות במבנה. ככל שהטמפרטורה עולה מעט, הרטט מתגבר. בגלל המבנה הקבוע והכוחות החזקים ביניהם, למוצק יש צורה ונפח משלו.</p>

    <h3>💃 נוזל (אנרגיה בינונית): מחליקים זה לצד זה</h3>
    <p>מוסיפים עוד אנרגיה? החלקיקים מקבלים מספיק "כוח" כדי להתגבר על חלק מכוחות המשיכה החזקים שהחזיקו אותם במבנה הקבוע. הם עדיין קרובים יחסית, אבל עכשיו הם יכולים להחליק, להתגלגל ולהחליף מקומות זה עם זה. תחשבו על קהל צפוף שנע באיטיות. לנוזל אין צורה קבועה (הוא לובש את צורת הכלי), אבל יש לו נפח קבוע (בטמפרטורה ולחץ נתונים) כי החלקיקים עדיין קשורים יחסית זה לזה.</p>

    <h3>🤸‍♀️ גז (אנרגיה גבוהה): חופשיים לרוץ!</h3>
    <p>עוד ועוד אנרגיה... עכשיו לחלקיקים יש כל כך הרבה אנרגיה קינטית שהם מתגברים כמעט לחלוטין על כוחות המשיכה ביניהם. הם טסים במהירות עצומה לכל הכיוונים, מתנגשים זה בזה ובדפנות הכלי. המרחקים ביניהם גדולים בהרבה מאשר בנוזל או במוצק. אין להם לא צורה ולא נפח קבועים – הם פשוט מתפשטים וממלאים את כל החלל הפנוי.</p>

    <h3>המעבר בין ריקודים: שינויי מצב צבירה</h3>
    <p>כאשר אתם מחממים חומר (מוסיפים לו אנרגיה), אתם למעשה מעניקים אנרגיה לחלקיקים שלו, והם עוברים ממצב ריקוד אחד למשנהו: ממוצק ל נוזל (התכה), ומנוזל לגז (התאדות/רתיחה). כאשר אתם מקררים חומר (מסלקים ממנו אנרגיה), התנועה של החלקיקים מואטת, והם עוברים ממצב אנרגיה גבוהה יותר למצב אנרגיה נמוכה יותר: מגז לנוזל (התעבות), ומנוזל למוצק (קיפאון).</p>

    <p>הסימולציה שלמעלה מאפשרת לכם לשלוט באנרגיה (הטמפרטורה) ולצפות במו עיניכם איך ריקוד החלקיקים משתנה, ואיך השינוי הזה קובע אם החומר יתנהג כמו מוצק, נוזל או גז. נסו למשוך את המחוון מצד לצד וראו את הקסם קורה!</p>
</div>

<script>
    const canvas = document.getElementById('particle-canvas');
    const ctx = canvas.getContext('2d');
    const tempSlider = document.getElementById('temp-slider');
    const tempDisplay = document.getElementById('temp-display');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    // Simulation parameters
    const numParticles = 100;
    const particleRadius = 3;
    const particles = [];
    let simulationBounds = { x: 0, y: 0, width: canvas.width, height: canvas.height }; // Use let to allow reassigning on resize

    // Physics parameters (tuned for visual effect)
    let solidPullStrength = 0.05; // Strength pulling towards lattice point
    let solidRandomPush = 0.2; // Base random thermal push in solid
    let repulsionStrength = 1.5; // Force applied when particles overlap
    let liquidAttractionStrength = 0.0005; // Weak attraction towards center in liquid
    let damping = 0.99; // Base damping
    let wallRepulsion = 0.5; // Force bouncing off walls

    // State thresholds (Temperature from 0-100)
    const meltTemp = 30;
    const boilTemp = 70;

    // State-dependent variables updated by temperature
    let currentState = "מוצק";
    let currentSpeedMultiplier = 0;
    let currentVibrationAmplitude = 0;
    let currentDamping = damping;
    let currentSolidPullStrength = solidPullStrength;
    let currentRepulsionStrength = repulsionStrength;
    let currentLiquidAttractionStrength = liquidAttractionStrength;
    let currentWallRepulsion = wallRepulsion;


    // Adjust canvas size on load and resize
    function resizeCanvas() {
        const container = document.getElementById('simulation-container');
        // Set canvas size based on container width, keeping aspect ratio
        const containerWidth = container.clientWidth - 40; // Subtract padding
        canvas.width = containerWidth;
        canvas.height = containerWidth * 0.6; // Example aspect ratio
        simulationBounds.width = canvas.width;
        simulationBounds.height = canvas.height;

        // Re-initialize or adjust particle positions based on the new size
        // If in solid or transitioning to solid, reset to lattice
         if (currentState === "מוצק" || parseInt(tempSlider.value) <= meltTemp) {
             resetParticlesToLattice();
         } else {
             // For liquid/gas, just update bounds, particles redistribute naturally
             // Optionally, recenter particles if canvas aspect ratio changed significantly
             // For simplicity here, we let them redistribute.
         }
    }

    // Initialize particles (sets up lattice points)
    function initParticles() {
        particles.length = 0; // Clear existing particles
        // Calculate grid spacing based on canvas size
        const gridCols = 10;
        const gridRows = numParticles / gridCols;
        const particleSpacingX = simulationBounds.width / (gridCols + 1);
        const particleSpacingY = simulationBounds.height / (gridRows + 1);
        const startX = simulationBounds.width / 2 - (gridCols / 2 - 0.5) * particleSpacingX;
        const startY = simulationBounds.height / 2 - (gridRows / 2 - 0.5) * particleSpacingY;


        for (let i = 0; i < numParticles; i++) {
             const row = Math.floor(i / gridCols);
             const col = i % gridCols;
             const baseX = startX + col * particleSpacingX;
             const baseY = startY + row * particleSpacingY;

            particles.push({
                x: baseX, // Start exactly at base position
                y: baseY,
                vx: 0,
                vy: 0,
                baseX: baseX, // Store base position for solid state
                baseY: baseY
            });
        }
        // Update state label and initial velocities based on starting temperature
        updateParticleState(parseInt(tempSlider.value));
    }

     // Reset particles specifically to the solid lattice positions
    function resetParticlesToLattice() {
        // Recalculate grid spacing based on current canvas size
        const gridCols = 10;
        const gridRows = numParticles / gridCols;
        const particleSpacingX = simulationBounds.width / (gridCols + 1);
        const particleSpacingY = simulationBounds.height / (gridRows + 1);
        const startX = simulationBounds.width / 2 - (gridCols / 2 - 0.5) * particleSpacingX;
        const startY = simulationBounds.height / 2 - (gridRows / 2 - 0.5) * particleSpacingY;

         particles.forEach((p, i) => {
             const row = Math.floor(i / gridCols);
             const col = i % gridCols;
             p.baseX = startX + col * particleSpacingX;
             p.baseY = startY + row * particleSpacingY;
             // Snap current position to base position and zero velocity
             p.x = p.baseX;
             p.y = p.baseY;
             p.vx = 0;
             p.vy = 0;
         });
         // Ensure state is correctly set to solid if temp is in solid range
         if (parseInt(tempSlider.value) <= meltTemp) {
             currentState = "מוצק";
         }
         updateTempDisplay(); // Update display immediately
    }


    // Update simulation state based on temperature slider value
    function updateParticleState(temperature) {
        let newState;

        // Smoothly transition parameters based on temperature
        if (temperature <= meltTemp) { // Solid state
            newState = "מוצק";
            // Vibration amplitude increases with temp in solid
            currentVibrationAmplitude = (temperature / meltTemp) * particleRadius * 1.5; // Max vibration related to radius
            currentSolidPullStrength = solidPullStrength * (1 - temperature / (meltTemp * 2)); // Pull weakens slightly but stays strong
            currentSpeedMultiplier = 0; // No free motion, only vibration
            currentRepulsionStrength = repulsionStrength * 1.2; // Stronger repulsion in solid to maintain spacing
            currentLiquidAttractionStrength = 0;
            currentDamping = 0.95; // Stronger damping to prevent drift
            currentWallRepulsion = 0; // Walls don't really interact with fixed lattice
        } else if (temperature <= boilTemp) { // Liquid state
            newState = "נוזל";
            currentVibrationAmplitude = 0; // No vibration around fixed point
            currentSolidPullStrength = 0;
            // Speed increases with temp in liquid range
            currentSpeedMultiplier = 0.5 + (temperature - meltTemp) / (boilTemp - meltTemp) * 0.5; // Speed scales from 0.5 to 1.0
            currentRepulsionStrength = repulsionStrength * 0.8; // Slightly weaker repulsion than solid
            currentLiquidAttractionStrength = liquidAttractionStrength; // Weak attraction towards center
            currentDamping = damping; // Base damping
            currentWallRepulsion = wallRepulsion; // Walls bounce
        } else { // Gas state
            newState = "גז";
            currentVibrationAmplitude = 0;
            currentSolidPullStrength = 0;
            // Speed increases with temp in gas range
            currentSpeedMultiplier = 1.0 + (temperature - boilTemp) / (100 - boilTemp) * 1.0; // Speed scales from 1.0 upwards
            currentRepulsionStrength = repulsionStrength * 0.5; // Weaker repulsion (only at close range collisions)
            currentLiquidAttractionStrength = 0; // No attraction
            currentDamping = damping * 0.99; // Less damping
            currentWallRepulsion = wallRepulsion; // Walls bounce
        }

        // Handle transitions between states
        if (newState !== currentState) {
            console.log(`Transitioning from ${currentState} to ${newState}`);
            if (newState === "מוצק") {
                 // When moving to solid state, snap particles to lattice
                 resetParticlesToLattice();
            } else if (currentState === "מוצק" && (newState === "נוזל" || newState === "גז")) {
                 // When melting/boiling, give particles initial random velocities
                 particles.forEach(p => {
                     const angle = Math.random() * Math.PI * 2;
                     const speed = currentSpeedMultiplier * 3; // Base speed for freed particles
                     p.vx = Math.cos(angle) * speed;
                     p.vy = Math.sin(angle) * speed;
                 });
            }
            currentState = newState; // Update the state AFTER handling the transition logic
        }

        updateTempDisplay(); // Update the text display
    }

    function updateTempDisplay() {
         const temperature = parseInt(tempSlider.value);
         const stateLabel = currentState; // Use the determined state
         tempDisplay.textContent = `${temperature}°C (${stateLabel})`;
    }


    // Update simulation state
    function update() {
        // Apply physics rules based on current state and temperature-derived parameters
        const temperature = parseInt(tempSlider.value);

        particles.forEach(p => {
            let totalForceX = 0;
            let totalForceY = 0;

            if (currentState === "מוצק") {
                 // Pull force towards base position
                const dxBase = p.baseX - p.x;
                const dyBase = p.baseY - p.y;
                totalForceX += dxBase * currentSolidPullStrength;
                totalForceY += dyBase * currentSolidPullStrength;

                // Add random 'thermal' push (vibration)
                totalForceX += (Math.random() - 0.5) * currentVibrationAmplitude * 0.5;
                totalForceY += (Math.random() - 0.5) * currentVibrationAmplitude * 0.5;

            } else { // Liquid or Gas
                 // Apply liquid attraction towards center
                 if (currentState === "נוזל") {
                     const centerX = simulationBounds.width / 2;
                     const centerY = simulationBounds.height / 2;
                     const dxCenter = centerX - p.x;
                     const dyCenter = centerY - p.y;
                     totalForceX += dxCenter * currentLiquidAttractionStrength;
                     totalForceY += dyCenter * currentLiquidAttractionStrength;
                 }

                 // Apply random thermal motion in Liquid/Gas
                 const thermalSpeed = currentSpeedMultiplier * 0.1; // Add some random thermal push
                 totalForceX += (Math.random() - 0.5) * thermalSpeed;
                 totalForceY += (Math.random() - 0.5) * thermalSpeed;
            }


            // Particle-Particle Interaction (Repulsion for overlap)
            // O(N^2) interaction - potential bottleneck for large N
             for (let i = 0; i < particles.length; i++) {
                 const other = particles[i];
                 if (p !== other) {
                     const dx = p.x - other.x;
                     const dy = p.y - other.y;
                     const distSq = dx*dx + dy*dy;
                     const minDistSq = (particleRadius * 2) * (particleRadius * 2);

                     if (distSq < minDistSq && distSq > 0.1) { // Add small threshold to avoid division by zero
                         const dist = Math.sqrt(distSq);
                         const overlap = particleRadius * 2 - dist; // How much they overlap
                         const forceMagnitude = overlap * currentRepulsionStrength; // Repulsion strength increases with overlap

                         // Apply force proportional to overlap, away from the other particle
                         const angle = Math.atan2(dy, dx);
                         totalForceX += Math.cos(angle) * forceMagnitude;
                         totalForceY += Math.sin(angle) * forceMagnitude;
                     }
                 }
             }


            // Update velocity with applied forces
            p.vx += totalForceX;
            p.vy += totalForceY;

            // Apply damping
            p.vx *= currentDamping;
            p.vy *= currentDamping;

            // Update position
            p.x += p.vx;
            p.y += p.vy;

            // Wall Collision (applies only in Liquid/Gas states)
            if (currentState !== "מוצק") {
                 const wallForce = currentWallRepulsion;
                 const hitPadding = particleRadius; // Distance from wall when collision occurs

                if (p.x < simulationBounds.x + hitPadding) {
                    const overlap = (simulationBounds.x + hitPadding) - p.x;
                    p.x = simulationBounds.x + hitPadding; // Snap back
                    p.vx = Math.abs(p.vx) * (1 - wallForce); // Reflect and lose some energy
                } else if (p.x > simulationBounds.x + simulationBounds.width - hitPadding) {
                    const overlap = p.x - (simulationBounds.x + simulationBounds.width - hitPadding);
                     p.x = simulationBounds.x + simulationBounds.width - hitPadding; // Snap back
                    p.vx = -Math.abs(p.vx) * (1 - wallForce); // Reflect and lose some energy
                }

                if (p.y < simulationBounds.y + hitPadding) {
                    const overlap = (simulationBounds.y + hitPadding) - p.y;
                     p.y = simulationBounds.y + hitPadding; // Snap back
                    p.vy = Math.abs(p.vy) * (1 - wallForce); // Reflect and lose some energy
                } else if (p.y > simulationBounds.y + simulationBounds.height - hitPadding) {
                    const overlap = p.y - (simulationBounds.y + simulationBounds.height - hitPadding);
                     p.y = simulationBounds.y + simulationBounds.height - hitPadding; // Snap back
                    p.vy = -Math.abs(p.vy) * (1 - wallForce); // Reflect and lose some energy
                }
            }

        });
    }

    // Draw simulation
    function draw() {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw particles
        const temperature = parseInt(tempSlider.value);
        let particleColor = '#007bff'; // Base color

        if (currentState === "נוזל") {
             particleColor = '#4d94ff'; // Lighter blue for liquid
         } else if (currentState === "גז") {
             particleColor = '#99ccff'; // Even lighter blue for gas
         }
        ctx.fillStyle = particleColor; // Set fill color


        particles.forEach(p => {
            // In solid state, draw a circle around the base position indicating vibration area
            if (currentState === "מוצק") {
                 const vibrationIndicatorRadius = currentVibrationAmplitude * 1.2; // Slightly larger than actual vibration
                 ctx.strokeStyle = `rgba(150, 150, 150, ${temperature / meltTemp * 0.5})`; // Grey, fades in with temp
                 ctx.lineWidth = 1;
                 ctx.beginPath();
                 ctx.arc(p.baseX, p.baseY, vibrationIndicatorRadius, 0, Math.PI * 2);
                 ctx.stroke(); // Draw the vibration area circle
             }

            // Draw the particle itself
            ctx.beginPath();
            ctx.arc(p.x, p.y, particleRadius, 0, Math.PI * 2);
            ctx.fill();
        });
    }

    // Main animation loop
    function animate() {
        update();
        draw();
        requestAnimationFrame(animate);
    }

    // Event listeners
    tempSlider.addEventListener('input', () => {
        updateParticleState(parseInt(tempSlider.value));
    });


    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'מה קורה כאן בעצם?';
    });

    // Initialize on page load and resize
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas(); // Initial resize and setup
    initParticles(); // Initialize particle data and base positions
    // updateParticleState is called by resizeCanvas and on slider input.
    animate(); // Start the animation loop

</script>