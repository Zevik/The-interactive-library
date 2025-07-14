---
title: "ברק מהר הגעש: כך נוצר חשמל בענן אפר געשי"
english_slug: volcanic-lightning-how-electricity-forms-in-ash-cloud
category: "מדעי הסביבה / כדור הארץ"
tags:
  - הרי געש
  - ברק
  - גיאולוגיה
  - פיזיקה
  - חשמל סטטי
---
<h1>ברק מהר הגעש: כך נוצר חשמל בענן אפר געשי</h1>
<p>ראית פעם תמונה עוצרת נשימה של התפרצות געשית? בתוך עמוד העשן והאפר האדיר, לפעמים מבזיקים הבזקי אור כחולים-סגולים מסתוריים. זה לא סתם ברק רגיל שנקלע לסערה – זו תופעה פיזיקלית מרתקת ומלאת עוצמה שנקראת 'ברק וולקני'. איך מתרחש מחזה כה חשמלי בתוך ענן סוער של חלקיקי סלע לוהטים ואפר?</p>
<p>היכנסו לסימולציה וגלו בעצמכם איך מתרחשת הפרדת מטענים בענן האפר, עד לרגע הפריקה החשמלית – הברק! נסו לשחק עם כמות חלקיקי האפר ועם עוצמת הערבול כדי לראות איך זה משפיע על התפתחות המטען.</p>

<div id="app-container">
    <div id="simulation">
        <canvas id="ashCloudCanvas"></canvas>
        <div id="lightning-flash" style="display: none;"></div> <!-- Background flash effect -->
    </div>
    <div id="controls">
        <div class="control-group">
            <label for="density">צפיפות חלקיקי אפר:</label>
            <input type="range" id="density" min="50" max="300" value="150">
            <span id="density-value">150</span> חלקיקים
        </div>
        <div class="control-group">
            <label for="turbulence">עוצמת הערבול (טורבולנטיות):</label>
            <input type="range" id="turbulence" min="0.5" max="8" value="3" step="0.1">
            <span id="turbulence-value">3.0</span>
        </div>
        <div class="electric-meter-container">
            <label>צבירת מטען חשמלי בענן:</label>
            <div class="electric-meter">
                <div id="meter-fill"></div>
            </div>
            <span id="charge-level">0</span>
            <span class="meter-label">סף פריקה (ברק)</span>
        </div>
        <button id="reset-button" class="control-button">התחל מחדש / אפס מטען</button>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: ההסבר המדעי לברק הוולקני</h2>

    <h3>מהו ברק וולקני ומתי הוא מופיע?</h3>
    <p>ברק וולקני, או "רעם אפר", הוא פריקה חשמלית דרמטית המתרחשת בתוך עמוד האפר והגזים הנפלט מהר געש פעיל. הוא נפוץ במיוחד בשלבים הראשונים והאינטנסיביים של התפרצויות עוצמתיות, כשאפר רב נפלט במהירות ונוצר עמוד אפר ענק וסוער.</p>

    <h3>ברק געשי מול ברק בסופת רעמים – מה ההבדל?</h3>
    <p>בעוד שברק רגיל נוצר בענני סערה כתוצאה מחיכוך בין גבישי קרח וטיפות מים, ברק וולקני מתרחש בעיקרו בענני אפר יבשים המורכבים מחלקיקי סלע ואפר געשי. מנגנוני יצירת המטען דומים במקורם (חיכוך והפרדת חלקיקים), אך הסביבה והחומרים שונים באופן מהותי.</p>

    <h3>המנגנון המרכזי: אלקטריזציה טריבואלקטרית (חיכוך!)</h3>
    <p>הסיבה העיקרית לצבירת המטען החשמלי בענן אפר היא <strong>אלקטריזציה טריבואלקטרית</strong> – תהליך בו חלקיקים ניטרליים צוברי מטענים חשמליים בעקבות חיכוך והתנגשויות ביניהם. ממש כמו ששפשוף בלון בשיער יוצר חשמל סטטי, כך גם התנגשויות מהירות בין מיליוני חלקיקי האפר בענן הסוער גורמות למטענים חשמליים לעבור מחלקיק אחד לשני.</p>
    <ul>
        <li><strong>חלקיקים קטנים מול גדולים:</strong> התנגשויות בין חלקיקי אפר בגדלים שונים הן האפקטיביות ביותר להפרדת מטענים. בדרך כלל, חלקיקים קטנים וקלים יותר נוטים לאבד אלקטרונים ולהפוך לטעונים חיובית, בעוד שחלקיקים גדולים וכבדים יותר נוטים לצבור אלקטרונים ולהפוך לטעונים שלילית (הכלל הזה יכול להשתנות מעט כתלות בהרכב המינרלי).</li>
        <li><strong>קונבקציה והפרדה:</strong> עמוד האפר העולה הוא זרם חזק של גזים ואפר חמים (קונבקציה). זרם זה סוחף את החלקיקים הקטנים (והטעונים חיובית) כלפי מעלה, בעוד שהחלקיקים הגדולים יותר (והטעונים שלילית) נוטים ליפול או להישאר בשכבות הנמוכות יותר. הפרדה פיזית זו של חלקיקים בעלי מטענים מנוגדים יוצרת מתח חשמלי עצום בתוך הענן.</li>
    </ul>

    <h3>מה משפיע על העוצמה והתדירות?</h3>
    <p>מספר גורמים מגבירים את הסיכוי לברק וולקני:</p>
    <ul>
        <li><strong>קצב הפליטה:</strong> ככל שההתפרצות אלימה ומהירה יותר, כך נפלט יותר אפר בזמן קצר, מה שמגדיל את קצב ההתנגשויות והפרדת המטענים.</li>
        <li><strong>צפיפות וגודל החלקיקים:</strong> ענני אפר צפופים יותר עם מגוון גדלי חלקיקים מייצרים יותר התנגשויות וטעינה יעילה יותר.</li>
        <li><strong>גובה עמוד האפר:</strong> עמוד אפר גבוה יותר מאפשר יותר זמן ותנועה להפרדת המטענים.</li>
        <li><strong>נוכחות מים/קרח:</strong> לעיתים, אם ענן האפר מגיע לגבהים קרים מאוד או פוגש ענני מזג אוויר רגילים, גם אינטראקציות עם מים או קרח יכולות לתרום לטעינה החשמלית.</li>
    </ul>

    <h3>למה חשוב לחקור את התופעה הזו?</h3>
    <p>מעבר להיותה מחזה מרהיב, חקר הברק הוולקני חיוני:</p>
    <ul>
        <li><strong>ניטור סכנות:</strong> זיהוי ברקים וולקניים בעזרת מכשירי ניטור מסייע למדענים לעקוב אחר עוצמת ההתפרצות והתפתחותה, גם כשהראות לקויה. זוהי דרך חשובה להתריע על שינויים מסוכנים בפעילות ההר.</li>
        <li><strong>בטיחות תעופה:</strong> ענני אפר געשי הם סכנה חמורה למטוסים. מעקב אחר ברקים מסייע בזיהוי ענני אפר מסוכנים וכך ניתן להכווין נתיבי טיסה בטוחים הרחק מהם.</li>
    </ul>

    <h3>דוגמאות מהעולם</h3>
    <p>ברק וולקני תועד בהתפרצויות מפורסמות רבות, כולל הר סנט הלנס (1980), הר פינטובו (1991), ההתפרצות באיסלנד (אייפייאטלאייקול, 2010) ששיבשה את התעופה באירופה, והתפרצות הונגה טונגה (2022).</p>
</div>

<script>
    const canvas = document.getElementById('ashCloudCanvas');
    const ctx = canvas.getContext('2d');
    const densityControl = document.getElementById('density');
    const densityValueSpan = document.getElementById('density-value');
    const turbulenceControl = document.getElementById('turbulence');
    const turbulenceValueSpan = document.getElementById('turbulence-value');
    const meterFill = document.getElementById('meter-fill');
    const chargeLevelSpan = document.getElementById('charge-level');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const lightningFlashDiv = document.getElementById('lightning-flash'); // Flash element
    const resetButton = document.getElementById('reset-button');

    let particles = [];
    let particleCount = parseInt(densityControl.value);
    let turbulence = parseFloat(turbulenceControl.value);
    let totalChargeSeparation = 0;
    const LIGHTNING_THRESHOLD = 1000; // Threshold for lightning strike
    const CHARGE_PER_COLLISION = 8; // Amount of charge transferred per relevant collision (increased for faster build-up)
    const PARTICLE_SIZE_THRESHOLD = 3; // Particles smaller than this are 'small', larger are 'large'
    const MAX_PARTICLE_SIZE = 5;
    const MIN_PARTICLE_SIZE = 1;
    const PARTICLE_DAMPING = 0.98; // Slow down particles slightly each frame
    const BOUNDARY_REPULSION = 0.5; // Force to push particles away from edges

    // Resize canvas initially and on window resize
    function resizeCanvas() {
        const simulationDiv = document.getElementById('simulation');
        canvas.width = simulationDiv.clientWidth;
        canvas.height = simulationDiv.clientHeight;
        // On resize, reposition particles? Or just let them flow? Let them flow.
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    class Particle {
        constructor(x, y, size) {
            this.x = x;
            this.y = y;
            this.size = size;
            this.charge = 0; // 0: neutral, >0: positive, <0: negative
            this.vx = (Math.random() - 0.5) * turbulence * 0.5; // Start with some initial velocity
            this.vy = (Math.random() - 0.5) * turbulence * 0.5;
            this.type = this.size < PARTICLE_SIZE_THRESHOLD ? 'small' : 'large';
            this.color = '#999'; // Default ash color (slightly lighter)
            this.baseColor = '#999';
            this.chargedColorPos = [255, 0, 0]; // Red
            this.chargedColorNeg = [0, 0, 255]; // Blue
        }

        update() {
            // Apply turbulence-based movement (random walk)
            this.vx += (Math.random() - 0.5) * turbulence * 0.2;
            this.vy += (Math.random() - 0.5) * turbulence * 0.2;

             // Apply boundary repulsion
            if (this.x < this.size) this.vx += BOUNDARY_REPULSION;
            if (this.x > canvas.width - this.size) this.vx -= BOUNDARY_REPULSION;
            if (this.y < this.size) this.vy += BOUNDARY_REPULSION;
            if (this.y > canvas.height - this.size) this.vy -= BOUNDARY_REPULSION;

            // Apply damping
            this.vx *= PARTICLE_DAMPING;
            this.vy *= PARTICLE_DAMPING;

            // Limit velocity
            const maxVel = turbulence * 0.8 + 2; // Velocity limit scales with turbulence
            this.vx = Math.max(-maxVel, Math.min(maxVel, this.vx));
            this.vy = Math.max(-maxVel, Math.min(maxVel, this.vy));

            this.x += this.vx;
            this.y += this.vy;

             // Update color based on charge intensity
            let alpha = Math.min(1, Math.abs(this.charge) / 30); // Max transparency at charge 30
            if (this.charge > 0) {
                this.color = `rgba(${this.chargedColorPos[0]}, ${this.chargedColorPos[1]}, ${this.chargedColorPos[2]}, ${alpha})`;
            } else if (this.charge < 0) {
                this.color = `rgba(${this.chargedColorNeg[0]}, ${this.chargedColorNeg[1]}, ${this.chargedColorNeg[2]}, ${alpha})`;
            } else {
                this.color = this.baseColor; // Neutral color
            }
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();
        }
    }

    function initParticles() {
        particles = [];
        totalChargeSeparation = 0; // Reset charge meter
        chargeLevelSpan.textContent = 0;
        meterFill.style.width = '0%';
        lightningFlashDiv.style.display = 'none'; // Hide lightning on reset
        // Add particles randomly
        for (let i = 0; i < particleCount; i++) {
            const size = Math.random() * (MAX_PARTICLE_SIZE - MIN_PARTICLE_SIZE) + MIN_PARTICLE_SIZE;
            const x = Math.random() * canvas.width;
            const y = Math.random() * canvas.height;
            particles.push(new Particle(x, y, size));
        }
    }

    function checkCollisions() {
        // Simple N^2 collision check - optimize if needed
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const p1 = particles[i];
                const p2 = particles[j];

                const dx = p1.x - p2.x;
                const dy = p1.y - p2.y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                // If particles are colliding or very close
                const minDistance = p1.size + p2.size;
                if (distance < minDistance) {
                     // Basic collision response (push apart)
                    const overlap = minDistance - distance;
                    const moveX = dx / distance * overlap * 0.2; // Push factor
                    const moveY = dy / distance * overlap * 0.2;
                    p1.x += moveX;
                    p1.y += moveY;
                    p2.x -= moveX;
                    p2.y -= moveY;

                    // Charge transfer based on size difference
                    if (p1.type !== p2.type) { // Only transfer charge between different sizes
                         // Determine which is small and which is large
                        const smallP = p1.type === 'small' ? p1 : p2;
                        const largeP = p1.type === 'large' ? p1 : p2;

                        smallP.charge += CHARGE_PER_COLLISION; // Small gets positive
                        largeP.charge -= CHARGE_PER_COLLISION; // Large gets negative
                        totalChargeSeparation += CHARGE_PER_COLLISION; // Increase separation metric

                        // Simple velocity exchange/bounce effect
                        let tempVx = p1.vx;
                        let tempVy = p1.vy;
                        p1.vx = p2.vx * 0.8; // Exchange with some energy loss
                        p1.vy = p2.vy * 0.8;
                        p2.vx = tempVx * 0.8;
                        p2.vy = tempVy * 0.8;

                         // Add a small random push after collision based on turbulence
                         p1.vx += (Math.random() - 0.5) * turbulence * 0.5;
                         p1.vy += (Math.random() - 0.5) * turbulence * 0.5;
                         p2.vx += (Math.random() - 0.5) * turbulence * 0.5;
                         p2.vy += (Math.random() - 0.5) * turbulence * 0.5;

                    } else {
                         // If same size, just a simpler bounce
                        let tempVx = p1.vx;
                        let tempVy = p1.vy;
                        p1.vx = p2.vx * 0.5;
                        p1.vy = p2.vy * 0.5;
                        p2.vx = tempVx * 0.5;
                        p2.vy = tempVy * 0.5;
                    }
                }
            }
        }
    }

    function drawLightning() {
        // Trigger background flash
        lightningFlashDiv.style.display = 'block';
        lightningFlashDiv.style.opacity = '0.8';
        setTimeout(() => {
             lightningFlashDiv.style.opacity = '0';
        }, 100); // Flash duration
         setTimeout(() => {
             lightningFlashDiv.style.display = 'none';
        }, 200); // Keep display block slightly longer for fade transition

        // Draw lightning bolt on canvas
        ctx.save(); // Save canvas state
        ctx.strokeStyle = 'cyan'; // Lightning color
        ctx.lineWidth = 3;
        ctx.lineCap = 'round';
        ctx.shadowBlur = 15; // Glow effect
        ctx.shadowColor = 'cyan';

        let startX = Math.random() * canvas.width;
        let startY = 0; // Start near top
        let endX = Math.random() * canvas.width;
        let endY = canvas.height; // End near bottom

        let points = [{x: startX, y: startY}];
        let segmentLength = 20; // Approx length of each segment
        let deviation = 40; // Max horizontal deviation per segment

        let currentX = startX;
        let currentY = startY;

        while (currentY < endY) {
            let nextY = Math.min(currentY + segmentLength, endY);
            let randomX = currentX + (Math.random() - 0.5) * deviation;

            // Ensure it stays roughly within horizontal bounds, but can exit slightly
            // randomX = Math.max(-deviation, Math.min(canvas.width + deviation, randomX));

            // Interpolate X towards the target endX as Y increases
            let progress = (nextY - startY) / (endY - startY);
            let targetX = startX + (endX - startX) * progress;
            let deviatedX = targetX + (Math.random() - 0.5) * deviation * (1 - progress); // Deviation decreases lower down

            points.push({x: deviatedX, y: nextY});
            currentX = deviatedX;
            currentY = nextY;
        }


        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        for (let i = 1; i < points.length; i++) {
            ctx.lineTo(points[i].x, points[i].y);
        }
        ctx.stroke();
        ctx.restore(); // Restore canvas state (remove shadow, line width)

        // Clear the lightning stroke after a short delay
        // This requires redrawing the scene *without* the lightning
         setTimeout(() => {
            // The next animation frame will redraw everything, effectively clearing the lightning
            // No explicit clear needed here if animate loop continues
        }, 150);


    }

    function updateMeter() {
        // Scale totalChargeSeparation to a percentage for the meter
        const meterPercentage = Math.min(100, (totalChargeSeparation / LIGHTNING_THRESHOLD) * 100);
        meterFill.style.width = meterPercentage + '%';
        chargeLevelSpan.textContent = Math.floor(totalChargeSeparation);

        if (totalChargeSeparation >= LIGHTNING_THRESHOLD) {
            drawLightning();
            totalChargeSeparation = 0; // Reset charge separation after strike
             // Optionally, slightly neutralize particles after lightning
             particles.forEach(p => p.charge *= 0.8); // Reduce charge by 20%
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas

        checkCollisions(); // Check and resolve collisions, update charges

        particles.forEach(particle => {
            particle.update(); // Update position
            particle.draw(); // Draw particle
        });

        updateMeter(); // Update charge meter and check for lightning

        requestAnimationFrame(animate); // Loop the animation
    }

    // Event listeners for controls
    densityControl.addEventListener('input', (event) => {
        particleCount = parseInt(event.target.value);
        densityValueSpan.textContent = particleCount;
        initParticles(); // Re-initialize particles on density change
    });

    turbulenceControl.addEventListener('input', (event) => {
        turbulence = parseFloat(event.target.value);
        turbulenceValueSpan.textContent = turbulence.toFixed(1);
        // Particle velocities will adjust over time due to random walk and damping
    });

    resetButton.addEventListener('click', () => {
        initParticles(); // Reset simulation
    });


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג/הסתר הסבר מפורט';
    });


    // Start the simulation
    initParticles(); // Initial setup
    animate(); // Start the animation loop

</script>

<style>
    body {
        font-family: 'Arial', sans-serif; /* Use a common, clean font */
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #f0f0f0; /* Light grey background for the page */
    }

    h1, h2, h3 {
        color: #222;
        margin-bottom: 10px;
        line-height: 1.3;
    }

     h1 {
        text-align: center;
        color: #5a3b2e; /* Volcanic-themed color */
        margin-bottom: 20px;
     }

     p {
        margin-bottom: 15px;
     }


    #app-container {
        display: flex;
        flex-direction: column; /* Default to column layout */
        gap: 25px; /* Increased gap */
        margin: 20px auto; /* Center the container */
        padding: 25px; /* Increased padding */
        border: 1px solid #ddd;
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #fff, #f5f5f5); /* Subtle gradient */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Soft shadow */
        max-width: 900px; /* Max width for the app */
    }

    #simulation {
        position: relative; /* Needed for absolute positioning of lightning */
        flex-grow: 1; /* Allows simulation area to take available space */
        background: radial-gradient(ellipse at center, #444 0%, #222 100%); /* Dark, moody ash cloud background */
        border-radius: 8px; /* Slightly rounded corners for sim */
        overflow: hidden; /* Hide particles that go outside */
        min-height: 400px; /* Ensure simulation has good height */
        border: 1px solid #555; /* Dark border for sim */
    }

    #ashCloudCanvas {
        display: block;
        width: 100%;
        height: 100%;
    }

     #lightning-flash {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 1); /* Full white flash */
        pointer-events: none; /* Allow clicks to pass through */
        z-index: 10; /* Above canvas */
        opacity: 0; /* Start invisible */
        transition: opacity 0.1s ease-out; /* Fade out effect */
    }


    #controls {
        display: flex;
        flex-direction: column;
        gap: 20px; /* Increased gap */
        padding: 20px; /* Increased padding */
        background-color: #e8e8e8; /* Slightly darker grey background */
        border-radius: 8px;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
    }

    .control-group label {
        display: block;
        margin-bottom: 8px; /* Increased margin */
        font-weight: bold;
        color: #555;
    }

    .control-group input[type="range"] {
        width: calc(100% - 70px); /* Adjust width considering span */
        vertical-align: middle;
        height: 25px; /* Make slider thicker */
        -webkit-appearance: none; /* Remove default styles */
        appearance: none;
        background: #d3d3d3;
        outline: none;
        opacity: 0.9;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: #ff6b6b; /* Reddish thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

     .control-group input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: #ff6b6b; /* Reddish thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }


    .control-group span {
         display: inline-block;
         width: 50px; /* Give more space */
         text-align: right;
         vertical-align: middle;
         font-weight: bold; /* Make value stand out */
         color: #444;
         margin-left: 5px;
         font-variant-numeric: tabular-nums; /* Align numbers */
    }


    .electric-meter-container {
        margin-top: 15px; /* Increased margin */
        border-top: 1px dashed #bbb;
        padding-top: 15px;
    }

    .electric-meter-container label {
         font-weight: bold;
         display: block;
         margin-bottom: 8px;
         color: #555;
    }

    .electric-meter {
        width: calc(100% - 60px); /* Adjust width considering label and value */
        height: 25px; /* Make meter taller */
        border: 1px solid #555; /* Darker border */
        border-radius: 12px; /* More rounded */
        overflow: hidden;
        position: relative;
        background-color: #fff;
        display: inline-block;
        vertical-align: middle;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    #meter-fill {
        height: 100%;
        width: 0%;
        background: linear-gradient(to right, #4CAF50, #FFEB3B, #FF9800, #F44336); /* Green to Yellow to Orange to Red */
        transition: width 0.1s linear;
        border-radius: 12px 0 0 12px; /* Match outer border */
    }

    .electric-meter-container #charge-level {
        display: inline-block;
        width: 50px; /* Give more space */
        text-align: right;
        font-weight: bold;
        vertical-align: middle;
        color: #444;
        margin-left: 5px;
        font-variant-numeric: tabular-nums; /* Align numbers */
    }

     .electric-meter-container .meter-label {
        display: block;
        text-align: right;
        font-size: 0.9em; /* Slightly larger font */
        color: #666;
        margin-top: 4px;
        padding-right: 60px; /* Align under the meter */
    }

     .control-button {
        display: block;
        width: 100%; /* Full width button */
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #007bff;
        color: white;
        transition: background-color 0.2s ease;
        margin-top: 10px;
        text-align: center;
     }

     .control-button:hover {
        background-color: #0056b3;
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        border: 1px solid #007bff;
        border-radius: 6px;
        background-color: #007bff;
        color: white;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
        transform: translateY(-1px); /* Subtle hover effect */
    }

    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #ddd;
        border-radius: 12px;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    #explanation h2, #explanation h3 {
        color: #5a3b2e; /* Match title color */
        margin-top: 20px;
        margin-bottom: 12px;
        border-bottom: 1px solid #eee; /* Subtle separator */
        padding-bottom: 5px;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-left: 20px;
    }

    #explanation li {
        margin-bottom: 8px;
        color: #555;
    }

     /* Responsive layout */
     @media (min-width: 768px) {
        #app-container {
            flex-direction: row; /* Side-by-side on larger screens */
            gap: 30px; /* More space between sections */
        }
         #simulation {
            flex: 2; /* Simulation takes more space */
         }
         #controls {
             flex: 1; /* Controls take less space */
             max-width: 350px; /* Limit controls width */
         }
         .control-button {
            width: auto; /* Auto width on wider screens */
            align-self: flex-start; /* Align button to start */
         }
          .electric-meter-container .meter-label {
            padding-right: 0; /* Remove padding */
            text-align: left; /* Align left */
            margin-top: 8px;
         }
     }
</style>