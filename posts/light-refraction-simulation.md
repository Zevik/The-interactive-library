---
title: "המסע המדהים של האור: הדמיית שבירה"
english_slug: light-refraction-simulation
category: "פיזיקה"
tags: ['אופטיקה', 'שבירה', 'חוק סנל', 'אור']
---

<div class="simulation-container">
    <canvas id="refractionCanvas"></canvas>
    <div class="controls-and-display">
        <div class="controls">
            <label for="angleSlider">שנו את זווית הפגיעה:</label>
            <input type="range" id="angleSlider" min="0" max="89" value="30">
        </div>
        <div class="angle-display">
            <p>זווית פגיעה: <span id="incidenceAngleDisplay">0</span>°</p>
            <p>זווית שבירה: <span id="refractionAngleDisplay">0</span>°</p>
        </div>
    </div>
</div>

<button id="toggleExplanation">הצצה אל מאחורי הקלעים (הסבר)</button>

<div id="explanation" class="hidden">
    <h2>הסבר: מה גורם לאור להתכופף?</h2>
    <p>האם אי פעם שאלתם למה קש ששמים בכוס מים נראה 'שבור'? או איך עדשות במשקפיים או במיקרוסקופ עובדות? הסוד טמון בתופעה מדהימה שנקראת **שבירת אור**!</p>
    <p>זה קורה כשאור עובר ממקום אחד שבו הוא מטייל במהירות מסוימת (למשל, אוויר) למקום אחר שבו המהירות שלו שונה (למשל, מים). שינוי המהירות הזה גורם לשינוי בכיוון התנועה של האור – הוא פשוט מתכופף!</p>
    <p>דמיינו גלגל של מכונית שנוסע על כביש חלק (מדיום 1, כמו אוויר) ופוגע בזווית בבוץ (מדיום 2, כמו מים). הצד של הגלגל שפוגע בבוץ ראשון מאט, בעוד הצד השני עדיין על הכביש המהיר. זה גורם לגלגל 'לשבור' לכיוון הבוץ, כלומר לשנות את כיוונו. בדיוק ככה פועל האור! כאשר הוא עובר ממדיום שבו הוא מהיר (מקדם שבירה נמוך, $n$) למדיום שבו הוא איטי (מקדם שבירה גבוה), הוא 'נשבר' לכיוון הקו הדמיוני האנכי שנקרא ה**נורמל**.</p>
    <p>בסימולציה הזו, הקו האופקי המרכזי הוא הגבול בין אוויר למים. הקו המקוקו האנכי הוא ה**נורמל** – תמיד ניצב למשטח הפגיעה. זוויות הפגיעה והשבירה נמדדות תמיד ביחס לקו החשוב הזה.</p>
    <p>הקרן הכתומה היא **הקרן הפוגעת** (באוויר). הקרן הירוקה היא **הקרן הנשברת** (במים). תמיד יש גם קרן כחולה שמוחזרת מהמשטח – זו **הקרן המוחזרת** (זווית ההחזרה שווה תמיד לזווית הפגיעה).</p>
    <p>הקשר המדויק בין זווית הכניסה ($\theta_1$) לזווית היציאה ($\theta_2$) נתון על ידי נוסחה אלגנטית שנקראת **חוק סנל**:</p>
    <p class="math-equation">$n_1 \cdot \sin(\theta_1) = n_2 \cdot \sin(\theta_2)$</p>
    <p>כאן, $n_1$ ו-$n_2$ הם 'מקדמי השבירה' של המדיומים (עד כמה הם 'מעכבים' את האור). בסימולציה שלנו, האור עובר מאוויר ($n_1 \approx 1$, מהיר) למים ($n_2 \approx 1.33$, איטי יותר). מכיוון שהאור מאט כשהוא נכנס למים ($n_2 > n_1$), חוק סנל אומר שהוא נשבר קרוב יותר לנורמל, ולכן זווית השבירה ($\theta_2$) תמיד קטנה מזווית הפגיעה ($\theta_1$) (כל עוד הפגיעה אינה ניצבת).</p>
    <p>שחקו עם הסליידר, צפו בקרני האור ובזווית השבירה המחושבת, וראו את חוק סנל בפעולה!</p>
</div>

<style>
    /* Overall Page Styling */
    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* Soft sky blue gradient */
        color: #333;
        padding: 20px;
        line-height: 1.7; /* Slightly more relaxed line height */
        margin: 0;
    }

    h1, h2 {
        color: #007bff; /* Primary blue */
        text-align: center;
        margin-bottom: 20px;
        font-weight: normal;
    }

    h2 {
        color: #0056b3; /* Darker blue for section headers */
    }

    p {
        margin-bottom: 15px;
    }

    strong {
        color: #007bff; /* Highlight important terms */
    }

    /* Simulation Container Styling */
    .simulation-container {
        background-color: #ffffff; /* White background */
        border-radius: 12px; /* More rounded corners */
        padding: 25px; /* More padding */
        margin: 25px auto;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Stronger, softer shadow */
        max-width: 650px; /* Slightly wider container */
        display: flex;
        flex-direction: column;
        align-items: center;
        border: 1px solid #e0e0e0; /* Subtle border */
    }

    #refractionCanvas {
        width: 100%;
        height: 350px; /* Increased height */
        display: block; /* Prevent extra space below canvas */
        margin-bottom: 25px;
        border-radius: 8px; /* Rounded corners for canvas */
        /* Background handled by CSS gradient for visual separation */
        background: linear-gradient(to bottom, #87CEEB 50%, #4682B4 50%); /* Air (sky blue) over Water (steel blue) */
        overflow: hidden; /* Ensure nothing draws outside */
    }

    /* Controls and Display Layout */
    .controls-and-display {
        width: 100%;
        display: flex;
        flex-direction: column; /* Stack controls and display vertically */
        align-items: center;
    }

    .controls {
        width: 90%; /* Adjust width */
        text-align: center;
        margin-bottom: 15px;
    }

    .controls label {
        font-weight: bold;
        margin-bottom: 8px;
        display: block; /* Label on its own line */
        color: #555;
        font-size: 1.1em;
    }

    /* Slider Styling */
    #angleSlider {
        width: 100%; /* Full width within controls div */
        -webkit-appearance: none;
        appearance: none;
        height: 10px; /* Thicker slider track */
        background: linear-gradient(to right, #007bff, #00c6ff); /* Gradient track */
        outline: none;
        opacity: 0.9; /* Slightly less opaque default */
        -webkit-transition: opacity .2s ease-in-out;
        transition: opacity .2s ease-in-out;
        border-radius: 5px;
        cursor: grab; /* Indicates drag action */
        margin-top: 5px;
    }

     #angleSlider:hover {
        opacity: 1;
        cursor: grabbing;
     }

    #angleSlider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 24px; /* Larger thumb */
        height: 24px;
        background: #ffffff; /* White thumb */
        cursor: grab;
        border-radius: 50%;
        border: 3px solid #007bff; /* Blue border */
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2); /* More prominent shadow */
         transition: border-color 0.2s ease-in-out;
    }

    #angleSlider:hover::-webkit-slider-thumb {
         cursor: grabbing;
         border-color: #0056b3; /* Darker blue on hover */
    }

    #angleSlider::-moz-range-thumb {
        width: 24px;
        height: 24px;
        background: #ffffff;
        cursor: grab;
        border-radius: 50%;
        border: 3px solid #007bff;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
         transition: border-color 0.2s ease-in-out;
    }

    #angleSlider:hover::-moz-range-thumb {
         cursor: grabbing;
         border-color: #0056b3;
    }


    .angle-display {
        width: 90%; /* Match controls width */
        text-align: center;
        margin-bottom: 10px;
        font-size: 1.1em;
        color: #555;
        display: flex; /* Arrange angle display items side by side */
        justify-content: space-around;
        padding-top: 10px;
        border-top: 1px dashed #e0e0e0; /* Separator */
    }

    .angle-display p {
        margin: 0; /* Remove paragraph margin */
    }

    .angle-display span {
        font-weight: bold;
        color: #007bff; /* Match primary blue */
        font-variant-numeric: tabular-nums; /* Align numbers */
    }

    /* Toggle Button Styling */
    #toggleExplanation {
        display: block;
        margin: 25px auto; /* Center button with larger margin */
        padding: 12px 25px; /* More padding */
        background-color: #17a2b8; /* Info blue/teal */
        color: white;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 17px; /* Slightly larger font */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    #toggleExplanation:hover {
        background-color: #138496; /* Darker teal on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* More pronounced shadow on hover */
    }

    #toggleExplanation:active {
        transform: scale(0.98);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); /* Depressed shadow on active */
    }

    /* Explanation Section Styling */
    #explanation {
        background-color: #e9ecef; /* Light grey */
        border: 1px solid #ced4da;
        border-radius: 10px;
        padding: 25px;
        margin-top: 20px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        transition: opacity 0.5s ease-in-out, max-height 0.5s ease-in-out, padding 0.5s ease-in-out, border-color 0.5s ease-in-out;
        overflow: hidden;
        opacity: 1;
        max-height: 2000px; /* Sufficient height for expansion */
    }

    #explanation.hidden {
        opacity: 0;
        max-height: 0;
        padding-top: 0;
        padding-bottom: 0;
        border-color: transparent;
         margin-top: 0; /* Collapse margin when hidden */
    }

    .math-equation {
        text-align: center;
        font-style: italic;
        font-size: 1.2em; /* Larger math equation */
        margin: 20px 0;
        color: #0056b3; /* Blue color for equation */
        direction: ltr; /* Ensure correct rendering of equation */
    }

     /* Canvas drawing styles - handled in JS */
</style>

<script>
    const canvas = document.getElementById('refractionCanvas');
    const ctx = canvas.getContext('2d');
    const angleSlider = document.getElementById('angleSlider');
    const incidenceAngleDisplay = document.getElementById('incidenceAngleDisplay');
    const refractionAngleDisplay = document.getElementById('refractionAngleDisplay');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggleExplanation');

    const n1 = 1.0; // Refractive index of Air (approx)
    const n2 = 1.33; // Refractive index of Water (approx)

    // Canvas dimensions
    let canvasWidth, canvasHeight;
    let centerX, centerY;

    // Animation variables
    let animationFrameId = null;
    let lastUpdateTime = 0;
    const particleSpeed = 0.00005; // percentage of ray length per millisecond
    const numberOfParticles = 8; // More particles for a smoother flow

    // Particle data structure: { rayType: 'incident'|'reflected'|'refracted', position: 0-1, color: string }
    let particles = [];

    function setupParticles() {
        particles = [];
        const colors = {
            incident: '#ff8c00', // Dark Orange
            reflected: '#1e90ff', // Dodger Blue
            refracted: '#32cd32'  // Lime Green
        };

        for (let i = 0; i < numberOfParticles; i++) {
            particles.push({ rayType: 'incident', position: i / numberOfParticles, color: colors.incident });
            particles.push({ rayType: 'reflected', position: i / numberOfParticles, color: colors.reflected });
            particles.push({ rayType: 'refracted', position: i / numberOfParticles, color: colors.refracted });
        }
    }

    function updateParticles(deltaTime) {
        particles.forEach(p => {
            p.position += particleSpeed * deltaTime;
            if (p.position > 1) {
                p.position = 0; // Loop the particle
            }
        });
    }

    function drawParticles() {
        const incidenceAngleRad = parseFloat(angleSlider.value) * Math.PI / 180;
        let refractionAngleRad = Math.asin((n1 / n2) * Math.sin(incidenceAngleRad));
        if (isNaN(refractionAngleRad)) refractionAngleRad = 0; // Handle edge cases like TIR (though not possible n1<n2) or angle 90

        const rayLength = Math.min(centerX, centerY) * 0.9;

        particles.forEach(p => {
            let startX = centerX, startY = centerY;
            let endX, endY;

            if (p.rayType === 'incident') {
                endX = centerX - rayLength * Math.sin(incidenceAngleRad);
                endY = centerY - rayLength * Math.cos(incidenceAngleRad);
            } else if (p.rayType === 'reflected') {
                endX = centerX + rayLength * Math.sin(incidenceAngleRad);
                endY = centerY - rayLength * Math.cos(incidenceAngleRad);
            } else if (p.rayType === 'refracted') {
                endX = centerX + rayLength * Math.sin(refractionAngleRad);
                endY = centerY + rayLength * Math.cos(refractionAngleRad);
            }

            const currentX = startX + (endX - startX) * p.position;
            const currentY = startY + (endY - startY) * p.position;

            ctx.beginPath();
            ctx.arc(currentX, currentY, 4, 0, Math.PI * 2); // Draw a slightly larger circle
            ctx.fillStyle = p.color;
            ctx.shadowColor = p.color; // Add a glow effect
            ctx.shadowBlur = 8; // Adjust glow intensity
            ctx.fill();
             ctx.shadowColor = 'transparent'; // Reset shadow
            ctx.shadowBlur = 0; // Reset shadow
        });
    }

    // Function to draw static elements (boundary, normal, arcs, labels)
    function drawStaticElements() {
        ctx.clearRect(0, 0, canvasWidth, canvasHeight); // Clear the entire canvas

        // Background is handled by CSS gradient

        // Draw boundary line
        ctx.beginPath();
        ctx.moveTo(0, centerY);
        ctx.lineTo(canvasWidth, centerY);
        ctx.strokeStyle = '#555'; // Boundary color
        ctx.lineWidth = 3;
        ctx.stroke();

        // Draw Normal line
        ctx.beginPath();
        ctx.moveTo(centerX, 0);
        ctx.lineTo(centerX, canvasHeight);
        ctx.strokeStyle = '#dc3545'; // Red normal
        ctx.lineWidth = 2;
        ctx.setLineDash([8, 8]); // Dashed line
        ctx.stroke();
        ctx.setLineDash([]); // Reset dash

        // Get angles
        const incidenceAngleDeg = parseFloat(angleSlider.value);
        const incidenceAngleRad = incidenceAngleDeg * Math.PI / 180;
        let refractionAngleRad = Math.asin((n1 / n2) * Math.sin(incidenceAngleRad));
         if (isNaN(refractionAngleRad)) refractionAngleRad = 0;
        const refractionAngleDeg = refractionAngleRad * 180 / Math.PI;

        // Draw angle arcs
        drawAngleArc(ctx, centerX, centerY, incidenceAngleRad, 'incidence', '#6a0dad'); // Purple
        drawAngleArc(ctx, centerX, centerY, incidenceAngleRad, 'reflection', '#007bff'); // Blue
        drawAngleArc(ctx, centerX, centerY, refractionAngleRad, 'refraction', '#28a745'); // Green

        // Add angle labels on canvas near arcs
        drawAngleLabel(ctx, centerX, centerY, incidenceAngleRad, 'incidence', incidenceAngleDeg.toFixed(0) + '°', '#6a0dad');
        drawAngleLabel(ctx, centerX, centerY, incidenceAngleRad, 'reflection', incidenceAngleDeg.toFixed(0) + '°', '#007bff');
        drawAngleLabel(ctx, centerX, centerY, refractionAngleRad, 'refraction', refractionAngleDeg.toFixed(1) + '°', '#28a745');
    }

    // Main animation loop
    function animate(currentTime) {
        if (!lastUpdateTime) {
            lastUpdateTime = currentTime;
        }
        const deltaTime = currentTime - lastUpdateTime;
        lastUpdateTime = currentTime;

        drawStaticElements(); // Redraw static parts every frame
        updateParticles(deltaTime); // Update particle positions
        drawParticles(); // Draw particles

        animationFrameId = requestAnimationFrame(animate);
    }

    // Helper function to draw angle arcs
    function drawAngleArc(ctx, cx, cy, angleRad, type, color) {
        const radius = 45; // Larger arcs
        ctx.beginPath();
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        let startAngle, endAngle;
        let counterClockwise = false;

        if (type === 'incidence' || type === 'reflection') {
            startAngle = -Math.PI / 2; // Normal (up)
            if (type === 'incidence') {
                endAngle = startAngle - angleRad;
                counterClockwise = true;
            } else { // reflection
                endAngle = startAngle + angleRad;
                counterClockwise = false;
            }
        } else if (type === 'refraction') {
            startAngle = Math.PI / 2; // Normal (down)
            endAngle = startAngle + angleRad;
            counterClockwise = false;
        } else {
            return;
        }

        // Ensure correct arc drawing direction
         if (startAngle > endAngle && !counterClockwise) {
             [startAngle, endAngle] = [endAngle, startAngle];
         } else if (startAngle < endAngle && counterClockwise) {
             [startAngle, endAngle] = [endAngle, startAngle];
         }

        ctx.arc(cx, cy, radius, startAngle, endAngle, counterClockwise);
        ctx.stroke();
    }

    // Helper function to draw angle labels on canvas
    function drawAngleLabel(ctx, cx, cy, angleRad, type, text, color) {
        const labelRadius = 65; // Distance from center, adjusted for larger arcs
        let labelAngle;

        // Calculate angle for text placement (midpoint of the arc angle relative to the center)
        if (type === 'incidence') {
            labelAngle = -Math.PI / 2 - angleRad / 2;
        } else if (type === 'reflection') {
            labelAngle = -Math.PI / 2 + angleRad / 2;
        } else if (type === 'refraction') {
            labelAngle = Math.PI / 2 + angleRad / 2;
        } else {
            return;
        }

        const labelX = cx + labelRadius * Math.cos(labelAngle);
        const labelY = cy + labelRadius * Math.sin(labelAngle);

        ctx.fillStyle = color;
        ctx.font = 'bold 16px Arial'; // More prominent font
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        // Add a subtle text shadow for readability
        ctx.shadowColor = 'rgba(255,255,255,0.8)';
        ctx.shadowBlur = 4;
        ctx.fillText(text, labelX, labelY);
        ctx.shadowColor = 'transparent'; // Reset shadow
        ctx.shadowBlur = 0;
    }


    // Function to handle canvas resizing and initial setup
    function resizeCanvas() {
        const container = canvas.parentElement;
        canvasWidth = container.clientWidth;
        canvasHeight = 350; // Keep fixed height
        canvas.width = canvasWidth;
        canvas.height = canvasHeight;
        centerX = canvasWidth / 2;
        centerY = canvasHeight / 2;

        // Setup particles and start animation loop if not already running
        setupParticles();
        if (!animationFrameId) {
             lastUpdateTime = 0; // Reset timer for smooth start
            animationFrameId = requestAnimationFrame(animate);
        }
    }

    // Event listener for slider - update HTML displays immediately
    angleSlider.addEventListener('input', () => {
        const incidenceAngleDeg = parseFloat(angleSlider.value);
        incidenceAngleDisplay.textContent = incidenceAngleDeg;

        const incidenceAngleRad = incidenceAngleDeg * Math.PI / 180;
        let refractionAngleRad = Math.asin((n1 / n2) * Math.sin(incidenceAngleRad));
        if (isNaN(refractionAngleRad)) refractionAngleRad = 0; // Handle edge cases

        const refractionAngleDeg = refractionAngleRad * 180 / Math.PI;
        refractionAngleDisplay.textContent = refractionAngleDeg.toFixed(2);

        // The animation loop automatically redraws with the new slider value
    });


    // Event listeners
    window.addEventListener('resize', resizeCanvas);

    toggleButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
         // Smooth scroll to explanation if showing it
        if (!explanationDiv.classList.contains('hidden')) {
            // Use setTimeout to allow the max-height transition to start before scrolling
            setTimeout(() => {
                explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 50); // Short delay
        }
    });

    // Initial setup
    resizeCanvas(); // Set initial size, setup particles, and start animation
    explanationDiv.classList.add('hidden'); // Ensure hidden initially

</script>