---
title: "הגל שמפסל את החוף: מסע אל סודן של המערות הימיות"
english_slug: the-wave-that-sculpts-the-coast-journey-to-the-secret-of-sea-caves
category: "גיאולוגיה"
tags: ["גלים", "סחיפה ימית", "מערות ימיות", "קו חוף", "גיאומורפולוגיה", "סימולציה"]
---
# הגל שמפסל את החוף: מסע אל סודן של המערות הימיות

האם עצרתם פעם לחשוב איך נוצרות אותן מערות מסתוריות החצובות במצוקי החוף, כאילו יד נעלמה פיסלה אותן? מדוע הגלים, שרק נוגעים בקצה הסלע, מצליחים לאורך זמן לחצוב חללים כה גדולים? הצטרפו אלינו למסע אינטראקטיבי מרתק כדי לגלות את התשובה בעצמכם!

<div class="app-container">
    <h2>סימולציית פיסול מערה ימית</h2>
    <div class="controls">
        <div class="control-group">
            <label for="waveStrength">עוצמת גלים:</label>
            <select id="waveStrength" class="control-select">
                <option value="low">רגילה</option>
                <option value="high">חזקה</option>
            </select>
        </div>
        <div class="control-group">
            <label for="waveFrequency">תדירות גלים:</label>
            <select id="waveFrequency" class="control-select">
                <option value="low">נמוכה</option>
                <option value="high">גבוהה</option>
            </select>
        </div>
        <div class="control-group">
            <label for="rockType">סוג סלע:</label>
            <select id="rockType" class="control-select">
                <option value="resistant">עמיד (ללא סדקים)</option>
                <option value="resistant_cracked">עמיד (עם סדקים)</option>
                <option value="weak">פגיע (ללא סדקים)</option>
                <option value="weak_cracked">פגיע (עם סדקים)</option>
            </select>
        </div>
    </div>
    <canvas id="caveCanvas" width="600" height="400"></canvas>
    <div class="info">
        <button id="startSimulation" class="control-button">התחל פיסול!</button>
        <span id="yearCounter" class="year-counter">זמן וירטואלי: שנה 0</span>
    </div>
     <div id="simulationGoal" class="simulation-goal">חצוב מערה גדולה ככל האפשר!</div>
</div>

<style>
    :root {
        --color-sea-dark: #4682B4;
        --color-sea-light: #87CEEB;
        --color-cliff: #A0522D;
        --color-cliff-eroded: #CD853F; /* Medium brown */
        --color-background: #F5F5DC; /* Beige */
        --color-text: #333;
        --color-primary-button: #1E90FF; /* Dodger Blue */
        --color-primary-button-hover: #007FFF; /* Azure */
        --color-secondary-button: #3CB371; /* Medium Sea Green */
        --color-secondary-button-hover: #2E8B57; /* Sea Green */
        --color-border: #ccc;
        --color-shadow: rgba(0, 0, 0, 0.1);
    }

    .app-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 650px;
        margin: 20px auto;
        border: 1px solid var(--color-border);
        padding: 25px;
        border-radius: 12px;
        background-color: var(--color-background);
        text-align: center;
        box-shadow: 0 8px 16px var(--color-shadow);
        overflow: hidden; /* Clear floats/prevent content overflow */
    }

    .app-container h2 {
        margin-top: 0;
        color: var(--color-text);
        font-size: 1.6rem;
        margin-bottom: 20px;
    }

    .controls {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin-bottom: 25px;
        flex-wrap: wrap;
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .controls label {
        margin-bottom: 8px;
        font-weight: bold;
        color: var(--color-text);
        font-size: 0.95rem;
    }

    .control-select, .control-button {
        padding: 10px 15px;
        border-radius: 6px;
        border: 1px solid var(--color-border);
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .control-select {
        background-color: #fff;
        min-width: 150px;
        text-align: right; /* For Hebrew */
        direction: rtl; /* For Hebrew */
    }

    .control-button {
        background-color: var(--color-primary-button);
        color: white;
        border: none;
        font-weight: bold;
    }

    .control-button:hover {
        background-color: var(--color-primary-button-hover);
        box-shadow: 0 4px 8px var(--color-shadow);
    }

    #caveCanvas {
        border: 1px solid var(--color-border);
        background: linear-gradient(to bottom, var(--color-sea-light) 0%, var(--color-sea-light) 70%, var(--color-sea-dark) 100%); /* Sky to deeper sea gradient */
        display: block;
        margin: 0 auto 25px auto;
        border-radius: 8px;
        box-shadow: inset 0 2px 8px var(--color-shadow);
    }

    .info {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 25px;
        flex-wrap: wrap;
        margin-bottom: 15px;
    }

    .year-counter {
        font-size: 1.2rem;
        font-weight: bold;
        color: var(--color-text);
        min-width: 150px; /* Prevent layout shift */
    }

     .simulation-goal {
        font-size: 1rem;
        color: var(--color-text);
        margin-top: 10px;
        font-style: italic;
     }


    .explanation-button-container {
        text-align: center;
        margin-top: 30px;
    }

    #toggleExplanation {
        background-color: var(--color-secondary-button);
        color: white;
        border: none;
        font-weight: bold;
    }

    #toggleExplanation:hover {
        background-color: var(--color-secondary-button-hover);
         box-shadow: 0 4px 8px var(--color-shadow);
    }

    .explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--color-border);
        border-radius: 8px;
        background-color: #fff;
        text-align: right; /* Align text right for Hebrew */
        direction: rtl; /* Set text direction */
        box-shadow: 0 4px 8px var(--color-shadow);
        line-height: 1.7;
    }

    .explanation h3 {
        color: var(--color-text);
        margin-top: 15px;
        margin-bottom: 12px;
        font-size: 1.3rem;
        border-bottom: 2px solid var(--color-primary-button-hover);
        padding-bottom: 5px;
    }

    .explanation p {
        color: #555;
        margin-bottom: 15px;
    }

    .explanation ul {
         margin: 10px 0;
         padding-right: 25px; /* Add padding for bullets */
         list-style: disc;
    }

    .explanation li {
         margin-bottom: 10px;
         color: #555;
    }

    .hidden {
        display: none;
    }
</style>

<div class="explanation-button-container">
    <button id="toggleExplanation" class="control-button">קרא עוד על היווצרות מערות ימיות</button>
</div>

<div id="explanationContent" class="explanation hidden">
    <h3>מהי מערה ימית וכיצד היא נפסלת בטבע?</h3>
    <p>מערה ימית היא חלל טבעי וקסום הנוצר בבסיס מצוק סלעי בקו החוף, לאורך אלפי ואף מיליוני שנים. היא אינה נוצרת מהתמוססות סלע כמו מערות קרסטיות יבשתיות, אלא בעיקר מכוחם העצום של הגלים והסחיפה הימית. המערה מתפתחת באזור המושפע ישירות מעליית וירידת מפלס הים, שם אנרגיית הגלים מרוכזת.</p>

    <h3>הפסלים הראשיים: גלי הים</h3>
    <p>היווצרות מערות ימיות מתחילה לרוב בנקודות חולשה בבסיס המצוק - סדקים, שברים, או אזורים בהם הסלע רך יותר. הגלים אינם סתם 'נוגעים' בסלע, אלא מפעילים עליו כוחות אדירים דרך מספר מנגנונים עיקריים:</p>

    <ul>
        <li><strong>פעולה הידראולית (Hydraulic Action):</strong> זהו אולי הכוח המשמעותי ביותר. כאשר גל מתנפץ על המצוק, הוא דוחס אוויר בחוזקה לתוך כל סדק או חריץ בסלע. כשהגל נסוג, האוויר הדחוס משתחרר בפתאומיות, כמו פיצוץ קטן, ומפעיל לחץ פנימי על דפנות הסדק. לחץ זה יכול לפורר חתיכות סלע קטנות, להרחיב סדקים קיימים וליצור חדשים. כוחו של המים עצמו החודר לסדקים ויוצר מערבולות גם הוא תורם לסחיפה.</li>
        <li><strong>אברזיה (Abrasion):</strong> הגלים נושאים איתם מטען סלעי: חול, חלוקי נחל ואפילו גושי סלע גדולים יותר. חומרים אלה משמשים כלי שחיקה טבעיים. כשהגלים מטלטלים וזורקים אותם נגד בסיס המצוק, הם שוחקים ומפסלים את הסלע באופן מכני מתמשך. דמיינו מיליוני "ניירות זכוכית" טבעיים הפועלים ללא הרף.</li>
        <li><strong>קורוזיה (Corrosion):</strong> למרות שהיא פחות דומיננטית בפני עצמה מיצירת חללים גדולים כמו מערות ימיות טיפוסיות (בניגוד למערות קרסטיות), המסה כימית של סלעים מסוימים (בעיקר סלעי גיר) על ידי מי ים יכולה לתרום גם היא לתהליך הסחיפה, במיוחד בחופים קרים.</li>
    </ul>

    <h3>תפקיד הסלע והזמן:</h3>
    <p>סוג הסלע הוא גורם קריטי. סלעים רכים ופגיעים (כמו אבן חול, קונגלומרט או חרסית) נסחפים מהר יותר מסלעים קשים ועמידים (כמו גרניט, בזלת או גנייס). החולשות המבניות בסלע – כמו סדקים, שברים ושכבות חלשות – מהוות נקודות פתיחה אידיאליות לפעולת הגלים ומאיצות דרמטית את קצב חציבת המערה. התהליך מתחיל לרוב בחריץ קטן (Wave-cut notch) בבסיס המצוק ומתפתח לאט לאט למערה גדולה יותר ויותר.</p>

    <h3>הסימולציה מציגה:</h3>
    <p>בסימולציה זו, תוכלו לבחון כיצד שילוב של עוצמת הגלים, תדירותם וסוג הסלע (כולל נוכחות סדקים) משפיעים על קצב וצורת התפתחות המערה הימית לאורך זמן וירטואלי. נסו את האפשרויות השונות וצפו בפלא הגיאולוגי נפרש מול עיניכם.</p>
</div>


<script>
    const canvas = document.getElementById('caveCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startSimulation');
    const yearCounter = document.getElementById('yearCounter');
    const waveStrengthSelect = document.getElementById('waveStrength');
    const waveFrequencySelect = document במאי קריאייטיב ומפתח תוכן חינוכי ברמה עולמית
    const rockTypeSelect = document.getElementById('rockType');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationContent = document.getElementById('explanationContent');

    let simulationRunning = false;
    let virtualYears = 0;
    let animationFrameId = null;
    let cliffProfilePoints = [];
    let crackIndices = []; // Indices in cliffProfilePoints that represent cracks
    let particles = [];
    let wavePhase = 0; // For wave animation

    const cliffBottomY = canvas.height - 50; // Original sea level baseline
    const cliffLeftX = 50;
    const cliffRightX = canvas.width - 50;
    const cliffWidth = cliffRightX - cliffLeftX;
    const numberOfPoints = 120; // More points for smoother erosion
    const pointSpacing = cliffWidth / (numberOfPoints - 1);
    const initialCaveDepth = 5; // Small initial indentation depth (in pixels upwards from cliffBottomY)
    const initialCaveWidthPoints = 15; // Width of initial indentation in terms of number of points

    // Simulation parameters (tuned for visual speed)
    const YEARS_PER_FRAME = 50; // How many virtual years pass per animation frame
    const BASE_EROSION_RATE = 0.0008; // Base erosion amount per point per virtual year

    function resetSimulation() {
        cliffProfilePoints = [];
        crackIndices = [];
        particles = [];
        wavePhase = 0;

        // Initialize points along the cliff base at the sea level (cliffBottomY)
        // Add a small initial indentation in the center for the cave to start forming
        const centerIndex = Math.floor(numberOfPoints / 2);
        const initialIndentStartIndex = Math.max(0, centerIndex - Math.floor(initialCaveWidthPoints / 2));
        const initialIndentEndIndex = Math.min(numberOfPoints - 1, centerIndex + Math.ceil(initialCaveWidthPoints / 2));

        for (let i = 0; i < numberOfPoints; i++) {
            const x = cliffLeftX + i * pointSpacing;
            let y = cliffBottomY;

            // Apply initial indentation shape (cosine or sine curve)
            if (i >= initialIndentStartIndex && i <= initialIndentEndIndex) {
                const indentProgress = (i - initialIndentStartIndex) / (initialIndentEndIndex - initialIndentStartIndex);
                // Cosine shape peaks at the center, value goes from 0 to 1 and back to 0
                const indentMultiplier = (1 - Math.cos(indentProgress * Math.PI * 2)) / 2; // 0 to 1 and back to 0
                 y -= initialCaveDepth * indentMultiplier; // Subtract Y to move points upwards (erode)
            }
            cliffProfilePoints.push({ x: x, y: y });
        }

        // Initialize cracks if rock type is cracked
        const rockType = rockTypeSelect.value;
        if (rockType.includes('cracked')) {
             // Select a few random points within the central indented area as crack centers
             const numCracks = rockType === 'resistant_cracked' ? 2 : 3; // More cracks for weak rock? Or same number, different erosion? Let's use same number.
             const crackAreaStart = Math.max(0, centerIndex - Math.floor(numberOfPoints * 0.15)); // Cracks concentrated in central 30%
             const crackAreaEnd = Math.min(numberOfPoints - 1, centerIndex + Math.ceil(numberOfPoints * 0.15));

             for(let i = 0; i < numCracks; i++) {
                 const randomIndex = Math.floor(Math.random() * (crackAreaEnd - crackAreaStart + 1)) + crackAreaStart;
                 // Ensure unique indices
                 if (!crackIndices.includes(randomIndex)) {
                     crackIndices.push(randomIndex);
                 } else {
                    i--; // Try again
                 }
             }
        }


        virtualYears = 0;
        yearCounter.textContent = `זמן וירטואלי: שנה ${virtualYears}`;
        drawSimulation();
    }

    function drawSimulation() {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw Sea
        // Use the gradient defined in CSS background, or draw one here
        const seaGradient = ctx.createLinearGradient(0, cliffBottomY, 0, canvas.height);
        seaGradient.addColorStop(0, 'var(--color-sea-light)'); // Top (near shore)
        seaGradient.addColorStop(1, 'var(--color-sea-dark)'); // Bottom (deeper)
        ctx.fillStyle = seaGradient;
        ctx.fillRect(0, cliffBottomY, canvas.width, canvas.height - cliffBottomY);

        // Draw Waves
        const waveAmplitude = waveStrengthSelect.value === 'high' ? 6 : 3;
        const waveLength = 0.08; // How spread out waves are
        const numWaveLines = 3; // Number of lines to draw for wave effect

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)'; // Semi-transparent white
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        for(let j=0; j < numWaveLines; j++) {
             const waveBaseY = cliffBottomY - j * 2; // Stack waves slightly
             const currentWavePhase = wavePhase + j * 0.5; // Offset phase for stacked waves
             ctx.moveTo(0, waveBaseY + waveAmplitude * Math.sin(currentWavePhase));
             for (let x = 0; x <= canvas.width; x += 5) {
                 const y = waveBaseY + waveAmplitude * Math.sin(x * waveLength + currentWavePhase);
                 ctx.lineTo(x, y);
             }
        }
        ctx.stroke();


        // Draw Cliff shape including the cave profile
        ctx.fillStyle = 'var(--color-cliff)'; // Brown cliff
        ctx.beginPath();
        // Start from top-left, go right, down along right edge to the *eroded profile's* Y
        ctx.moveTo(0, 0);
        ctx.lineTo(canvas.width, 0);
        ctx.lineTo(canvas.width, cliffProfilePoints[numberOfPoints - 1].y);

        // Draw the bottom profile of the cliff (the cave shape) - drawing UP along the profile
        for (let i = numberOfPoints - 1; i >= 0; i--) {
             ctx.lineTo(cliffProfilePoints[i].x, cliffProfilePoints[i].y);
        }

        // Continue up the left edge back to the top
        ctx.lineTo(0, cliffProfilePoints[0].y);
        ctx.lineTo(0, 0);
        ctx.closePath();
        ctx.fill();

        // Draw eroded texture/color within the cave area (optional, adds visual detail)
        ctx.fillStyle = 'var(--color-cliff-eroded)';
         ctx.beginPath();
        // Draw along the cliff profile points from left to right
        ctx.moveTo(cliffProfilePoints[0].x, cliffProfilePoints[0].y);
        for (let i = 1; i < numberOfPoints; i++) {
            ctx.lineTo(cliffProfilePoints[i].x, cliffProfilePoints[i].y);
        }
        // Draw down to the original sea level baseline
        ctx.lineTo(cliffProfilePoints[numberOfPoints - 1].x, cliffBottomY);
        // Draw left along the original sea level baseline
        ctx.lineTo(cliffProfilePoints[0].x, cliffBottomY);
        ctx.closePath();
        ctx.fill();


        // Highlight cracks if rock is cracked and simulation is running
        if (simulationRunning && rockTypeSelect.value.includes('cracked')) {
             ctx.fillStyle = 'rgba(255, 0, 0, 0.5)'; // Reddish highlight
             crackIndices.forEach(index => {
                 const p = cliffProfilePoints[index];
                 ctx.beginPath();
                 // Draw a small circle or line segment
                 ctx.arc(p.x, p.y, 3, 0, Math.PI * 2); // Small circle at crack point
                 ctx.fill();
             });
         }


        // Draw particles
        ctx.fillStyle = 'rgba(210, 133, 71, 0.7)'; // Color similar to eroded rock/sand
        particles.forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2); // Size shrinks with life
            ctx.fill();
        });

    }


    function updateSimulation() {
        if (!simulationRunning) return;

        virtualYears += YEARS_PER_FRAME; // Simulate N years per frame
        yearCounter.textContent = `זמן וירטואלי: שנה ${virtualYears.toLocaleString()}`;

        const waveStrength = waveStrengthSelect.value;
        const waveFrequency = waveFrequencySelect.value;
        const rockType = rockTypeSelect.value;

        // --- Calculate erosion factors ---
        const strengthMult = waveStrength === 'high' ? 2.5 : 1.0;
        const freqMult = waveFrequency === 'high' ? 3.0 : 1.0; // Higher freq = more impacts over the simulated time frame
        const rockMult = {
            resistant: 0.7,
            resistant_cracked: 1.1, // Cracks make resistant rock erode faster at those points
            weak: 1.8,
            weak_cracked: 3.0 // Cracks make weak rock erode much faster at those points
        };
        const crackBonus = rockType.includes('cracked') ? 2.0 : 1.0; // Additional multiplier near cracks if rock is cracked
        const crackInfluenceRadius = numberOfPoints * 0.1; // Points within this distance (in point index) are influenced by cracks

        // --- Apply erosion to each point ---
        const newCliffProfilePoints = cliffProfilePoints.map(p => ({ ...p })); // Create a copy to calculate simultaneous update
        const centerIndex = Math.floor(numberOfPoints / 2);

        for (let i = 0; i < numberOfPoints; i++) {
             // Base erosion intensity based on distance from center (peak erosion in middle)
             const distanceToCenter = Math.abs(i - centerIndex);
             const maxDistance = numberOfPoints / 2;
             const centerIntensity = Math.cos((distanceToCenter / maxDistance) * Math.PI / 2); // Cosine peak at center, drops to 0 at edges

             let currentCrackBonus = 1.0;
             if (rockType.includes('cracked')) {
                 let minDistToCrack = Infinity;
                 crackIndices.forEach(crackIndex => {
                     const dist = Math.abs(i - crackIndex);
                     minDistToCrack = Math.min(minDistToCrack, dist);
                 });

                 if (minDistToCrack < crackInfluenceRadius) {
                     // Bonus tapers off with distance from crack
                     currentCrackBonus = 1.0 + (crackBonus - 1.0) * (1 - minDistToCrack / crackInfluenceRadius);
                 }
             }

             // Add randomness
             const randomFactor = 0.8 + Math.random() * 0.4; // Varies between 0.8 and 1.2

             // Calculate total erosion amount for this point for this time step
             // Erosion moves points UP (decreasing Y)
             const erosionAmount = BASE_EROSION_RATE * YEARS_PER_FRAME * strengthMult * freqMult * rockMult[rockType] * centerIntensity * currentCrackBonus * randomFactor;

             newCliffProfilePoints[i].y -= erosionAmount;

             // Create particles at eroded spot (scaled by erosion amount)
             if (erosionAmount > 0.5) { // Only create particles if erosion is significant
                 const numParticles = Math.floor(erosionAmount * 2); // More particles for more erosion
                 for(let k=0; k<numParticles; k++) {
                      particles.push({
                          x: p.x + (Math.random() - 0.5) * 5, // Slight random offset
                          y: p.y + (Math.random() - 0.5) * 5,
                          vx: (Math.random() - 0.5) * 2, // Random horizontal velocity
                          vy: -Math.random() * 1 - 0.5, // Primarily upwards velocity with some randomness
                          life: 20 + Math.random() * 10, // Particle life
                          size: 1 + Math.random() * 1 // Particle size
                      });
                 }
             }
        }

         // --- Apply point boundary checks and update original points ---
         // Ensure points don't go above the "sky" area or cross neighbors (prevent jagged edges)
         for (let i = 0; i < numberOfPoints; i++) {
             // Prevent going too high (into the sky)
             newCliffProfilePoints[i].y = Math.max(newCliffProfilePoints[i].y, 20); // Don't erode above Y=20

             // Prevent crossing neighbors (smooth the profile)
             if (i > 0) {
                 // Ensure current point is not higher than previous point + small buffer
                 newCliffProfilePoints[i].y = Math.min(newCliffProfilePoints[i].y, newCliffProfilePoints[i-1].y + 1);
             }
             if (i < numberOfPoints - 1) {
                 // Ensure current point is not higher than next point + small buffer
                 newCliffProfilePoints[i].y = Math.min(newCliffProfilePoints[i].y, newCliffProfilePoints[i+1].y + 1);
             }

             // Update the original point
             cliffProfilePoints[i].y = newCliffProfilePoints[i].y;
         }


        // --- Update particles ---
        particles = particles.filter(p => p.life > 0); // Remove dead particles
        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.05; // Gravity effect (particles fall slightly)
            p.life -= 1;
        });

        // --- Update wave animation phase ---
        const waveSpeed = waveFrequencySelect.value === 'high' ? 0.1 : 0.04; // Wave speed depends on frequency
        wavePhase += waveSpeed;


        drawSimulation(); // Redraw everything
        animationFrameId = requestAnimationFrame(updateSimulation);

         // Optional: Stop simulation after a certain number of years or cave depth
         // Example: Stop after 100,000 years or when the cave depth (max erosion) reaches a certain point
         const maxErosionDepth = cliffBottomY - Math.min(...cliffProfilePoints.map(p => p.y));
         if (virtualYears >= 100000 || maxErosionDepth > 150) { // Simulate up to 100k years or ~150px deep cave
             stopSimulation();
             yearCounter.textContent += " (הסימולציה הסתיימה)";
             // Optional: Show a "result" message
             const goalElement = document.getElementById('simulationGoal');
             if (maxErosionDepth > 150) {
                 goalElement.textContent = `מזל טוב! חצבת מערה גדולה תוך ${virtualYears.toLocaleString()} שנים וירטואליות.`;
                 goalElement.style.color = 'green';
             } else {
                  goalElement.textContent = `הסימולציה הסתיימה לאחר ${virtualYears.toLocaleString()} שנים.`;
                  goalElement.style.color = 'orange';
             }
         }
    }

    function startSimulation() {
        if (!simulationRunning) {
            simulationRunning = true;
            startButton.textContent = 'הפסק פיסול';
            document.getElementById('simulationGoal').textContent = "פיסול בתהליך...";
            document.getElementById('simulationGoal').style.color = 'var(--color-text)';
            resetSimulation(); // Start from scratch each time
            updateSimulation(); // Start the animation loop
        } else {
            stopSimulation();
        }
    }

    function stopSimulation() {
        simulationRunning = false;
        startButton.textContent = 'התחל פיסול!';
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
    }

    function toggleExplanation() {
        explanationContent.classList.toggle('hidden');
        if (explanationContent.classList.contains('hidden')) {
            toggleExplanationButton.textContent = 'קרא עוד על היווצרות מערות ימיות';
        } else {
            toggleExplanationButton.textContent = 'הסתר הסבר נוסף';
        }
    }

    // Event Listeners
    startButton.addEventListener('click', startSimulation);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Initialize the simulation display
    resetSimulation(); // Draw the initial state
</script>
```