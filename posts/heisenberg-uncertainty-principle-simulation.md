---
title: "ריקוד אי-הוודאות: סימולציה קוונטית"
english_slug: heisenberg-uncertainty-principle-simulation
category: "פיזיקה"
tags: [סימולציה, קוונטים, ודאות, מיקום, תנע, הייזנברג, חלקיקים, גלי]
---
# ריקוד אי-הוודאות: הדמיית עקרון הייזנברג

דמיינו שאתם מנסים לתפוס חלקיק קוונטי זעיר. אם תנסו "לנעוץ" את מיקומו בדיוק מושלם, מה יקרה למהירות ולכיוון התנועה שלו? ואם תנסו לדעת בדיוק לאן הוא הולך, האם תוכלו לומר היכן הוא ברגע נתון?

בעולם היומיום שלנו, מדידת תכונה אחת לא מפריעה למדידת אחרת. אבל בעולם הקוונטים, לניסיון למדוד מיקום ותנע (מסה כפול מהירות) בו זמנית יש השלכות מפתיעות. עקרון אי-הוודאות של הייזנברג חושף לנו סוד עמוק של הטבע: יש גבול בסיסי לדיוק שבו אנו יכולים לדעת את שני הדברים *בבת אחת*.

בואו נשחק עם "ניסיון המדידה" הזה ונראה את ריקוד אי-הוודאות לנגד עינינו.

<div id="simulation-app">
    <div class="controls">
        <label for="precisionSlider">קבע את רמת "המיקוד" על מיקום החלקיק:</label>
        <input type="range" id="precisionSlider" min="0" max="100" value="50">
        <div class="values">
            <span>פחות מיקוד (יותר אי-ודאות במיקום)</span>
            <span>יותר מיקוד (פחות אי-ודאות במיקום)</span>
        </div>
    </div>
    <div class="output-values">
        <p>אי-ודאות במיקום (Δx): <span id="deltaX"></span></p>
        <p>אי-ודאות בתנע (Δp): <span id="deltaP"></span></p>
        <p>מכפלת אי-הוודאויות (Δx · Δp): <span id="product"></span></p>
    </div>
    <div class="canvas-container">
        <canvas id="heisenbergCanvas"></canvas>
    </div>
     <div class="graph-labels">
        <div class="label">התפלגות ההסתברות למציאת החלקיק (מרחב המיקום)</div>
        <div class="label">התפלגות ההסתברות למציאת התנע של החלקיק (מרחב התנע)</div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    #simulation-app {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
        padding: 25px;
        background-color: #eef2f7; /* Soft blue background */
        border-radius: 12px;
        max-width: 800px;
        margin: 30px auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        overflow: hidden; /* Clear floats/margins */
    }

    .controls {
        margin-bottom: 25px;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        border: 1px solid #d0d9e6;
    }

    .controls label {
        display: block;
        margin-bottom: 12px;
        font-weight: 700; /* Heebo Semibold */
        color: #333;
        font-size: 1.1em;
    }

    .controls input[type="range"] {
        width: calc(100% - 40px); /* Adjust width considering padding */
        margin: 0 20px; /* Center the slider visually */
        -webkit-appearance: none;
        appearance: none;
        height: 10px;
        background: linear-gradient to right, #a0c4ff, #4a90e2); /* Gradient track */
        outline: none;
        border-radius: 5px;
        transition: background-color .3s ease;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 24px;
        height: 24px;
        background: #0077cc; /* Bright blue thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3);
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 24px;
        height: 24px;
        background: #0077cc;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3);
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
    
    .controls input[type="range"]::-webkit-slider-thumb:hover {
        background: #005bb5;
    }
     .controls input[type="range"]::-webkit-slider-thumb:active {
        transform: scale(1.1);
     }


     .values {
        display: flex;
        justify-content: space-between;
        font-size: 0.9em;
        color: #555;
        margin-top: 10px;
        padding: 0 20px; /* Align with slider track */
     }

    .output-values {
        margin-bottom: 25px;
        background-color: #dce4ef; /* Slightly darker blue */
        padding: 20px;
        border-radius: 10px;
        color: #1a1a1a;
        border: 1px solid #c0c8d6;
    }

    .output-values p {
        margin: 8px 0;
        font-size: 1.1em;
        line-height: 1.4;
    }

    .output-values strong {
         font-weight: 700;
    }

    .output-values span {
        font-weight: 700;
        color: #005bb5; /* Darker blue for emphasis */
    }

    .canvas-container {
        width: 100%;
        padding-top: 50%; /* Maintain aspect ratio using padding-top based on width */
        position: relative;
        margin-bottom: 15px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        border: 1px solid #d0d9e6;
        overflow: hidden;
    }

    #heisenbergCanvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: block;
        background-color: transparent; /* Use container background */
        border-radius: 10px;
    }

    .graph-labels {
        display: flex;
        justify-content: space-around;
        font-size: 0.95em;
        color: #555;
        margin-top: 10px;
        font-weight: 400;
        line-height: 1.4;
        text-align: center;
    }

    .graph-labels .label {
        width: 48%; /* Slightly less than 50% to avoid overflow/wrapping */
        padding: 0 5px;
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto 10px auto; /* More space above, less below */
        padding: 12px 25px;
        font-size: 1.1em;
        color: #fff;
        background-color: #1e8b52; /* Green */
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: 700;
        box-shadow: 0 4px 8px rgba(0, 128, 0, 0.2);
    }

    #toggle-explanation:hover {
        background-color: #187445;
        box-shadow: 0 5px 10px rgba(0, 128, 0, 0.3);
    }

     #toggle-explanation:active {
        transform: scale(0.98);
        box-shadow: 0 2px 5px rgba(0, 128, 0, 0.3);
    }

    #explanation {
        margin-top: 20px;
        padding: 25px;
        background-color: #dce4ef; /* Same as output values */
        border-radius: 10px;
        border: 1px solid #c0c8d6;
        color: #1a1a1a;
        line-height: 1.7;
        opacity: 0; /* Start hidden */
        max-height: 0;
        overflow: hidden;
        transition: opacity 0.5s ease-out, max-height 0.5s ease-out;
    }

    #explanation.visible {
        opacity: 1;
        max-height: 1000px; /* Sufficiently large value */
    }


    #explanation h2 {
        margin-top: 0;
        color: #005bb5; /* Darker blue */
        font-weight: 700;
        font-size: 1.5em;
        margin-bottom: 15px;
    }

    #explanation p {
        margin-bottom: 1.2em;
        font-weight: 400;
    }

    #explanation strong {
        color: #004080; /* Even darker blue */
        font-weight: 700;
    }

    #explanation ul {
        margin-bottom: 1.2em;
        padding-right: 20px;
    }

    #explanation li {
        margin-bottom: 0.6em;
        font-weight: 400;
    }

    /* Add a subtle animation for the canvas */
    @keyframes pulse {
        0% { box-shadow: 0 4px 10px rgba(0,0,0,0.08); }
        50% { box-shadow: 0 4px 12px rgba(0,0,0,0.12); }
        100% { box-shadow: 0 4px 10px rgba(0,0,0,0.08); }
    }

    .canvas-container {
       animation: pulse 4s infinite ease-in-out;
    }


    /* Responsiveness */
    @media (max-width: 600px) {
        #simulation-app {
            padding: 15px;
            margin: 15px auto;
        }
        .controls, .output-values, #explanation {
            padding: 15px;
        }
        .controls input[type="range"] {
             width: calc(100% - 30px);
             margin: 0 15px;
        }
        .values {
             padding: 0 15px;
        }
        .graph-labels {
            flex-direction: column;
            align-items: center;
        }
        .graph-labels .label {
            width: 90%;
            margin-bottom: 10px;
        }
         #toggle-explanation {
            padding: 10px 20px;
            font-size: 1em;
         }
          #explanation h2 {
            font-size: 1.3em;
          }
           .output-values p {
            font-size: 1em;
           }
    }

</style>

<button id="toggle-explanation">גלו את הסוד: הצג הסבר על עקרון אי-הוודאות</button>

<div id="explanation">
    <h2>עקרון אי-הוודאות של הייזנברג - מה ראיתם?</h2>
    <p>ההדמיה שבה שיחקתם ממחישה את אחד הרעיונות המרכזיים והמוזרים ביותר בפיזיקה הקוונטית, שנוסח על ידי ורנר הייזנברג. בניגוד לעולם הקלאסי בו ניתן למדוד תכונות בדיוק בלתי מוגבל (בתיאוריה לפחות), בקנה מידה קוונטי קיים גבול יסודי.</p>
    <p><strong>העיקרון קובע בפשטות:</strong> ככל שאנחנו יודעים את מיקומו של חלקיק מסוים <strong>בדיוק רב יותר</strong> (כלומר, אי-הוודאות במיקום, Δx, קטנה יותר), כך הידע שלנו לגבי התנע שלו (Δp) הופך <strong>לפחות מדויק</strong> (אי-הוודאות בתנע גדלה יותר) - ולהיפך! אי-הוודאות מתפלגת כמו על נדנדה קוונטית.</p>
    <p>זה לא עניין של מכשירים לא מספיק טובים. זו תכונה מהותית של חלקיקים קוונטים, המתוארים כ"חבילות גלים". חבילת גלים שידועה במיקומה המדויק (צרה במרחב המיקום) מורכבת מהרבה מאוד אורכי גל שונים (ולכן התנע שלה פחות מוגדר). לעומת זאת, חבילת גלים עם תנע מוגדר היטב (אורך גל יחיד או טווח צר של אורכי גל) היא רחבה מאוד במרחב המיקום.</p>
    <p>מתמטית, העיקרון מתבטא בנוסחה האלגנטית:</p>
    <p><strong>Δx ⋅ Δp ≥ ħ/2</strong></p>
    <p>כאשר ħ (h-bar) הוא קבוע פלאנק המצומצם, מספר קטן אך יסודי המגדיר את "גודל הנדנדה" הקוונטית הזו.</p>
    <p>כששיחקתם עם ה"מיקוד", למעשה שיניתם את רוחב "חבילת הגל" המייצגת את החלקיק. ככל שמיקדתם יותר במיקום (Δx קטן, הגרף השמאלי נהיה צר), ראיתם שהגרף הימני, המייצג את התנע, התרחב (Δp גדל). ולהיפך. שימו לב שמכפלת אי-הוודאויות (Δx ⋅ Δp) נשארה תמיד מעל ערך מסוים.</p>
    <p>עקרון אי-הוודאות הוא אחד מעמודי התווך של הפיזיקה הקוונטית ואחראי לתופעות רבות המוזרות לכאורה בעולם התת-אטומי.</p>
</div>


<script>
    const slider = document.getElementById('precisionSlider');
    const deltaXSpan = document.getElementById('deltaX');
    const deltaPSpan = document.getElementById('deltaP');
    const productSpan = document.getElementById('product');
    const canvas = document.getElementById('heisenbergCanvas');
    const ctx = canvas.getContext('2d');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Canvas dimensions - will be set dynamically by CSS, get actual computed values
    let canvasWidth;
    let canvasHeight;

    // Simulation parameters (Arbitrary units for visualization)
    const HBAR_OVER_2 = 2000; // Analogous to ħ/2 in arbitrary units
    const MIN_DELTA_DISPLAY = 10; // Minimum display value for DeltaX or DeltaP to avoid division by zero or extreme visual representations
    const MAX_DELTA_DISPLAY = 150; // Maximum display value

    let currentDeltaX, currentDeltaP; // Store current values for animation

    // Function to calculate DeltaX and DeltaP based on slider value
    function calculateUncertainties(sliderValue) {
        // Map slider value (0 to 100) to DeltaX range (MAX_DELTA_DISPLAY to MIN_DELTA_DISPLAY)
        // Sliding right increases precision in position (smaller DeltaX)
        const deltaX = MAX_DELTA_DISPLAY - (sliderValue / 100) * (MAX_DELTA_DISPLAY - MIN_DELTA_DISPLAY);
        // DeltaP is then determined by the uncertainty principle: DeltaX * DeltaP approx HBAR_OVER_2
        const deltaP = HBAR_OVER_2 / deltaX; // This gives a constant product example

        return { deltaX, deltaP };
    }

    // Function to draw a Gaussian-like curve representing probability density
    function drawProbabilityDistribution(ctx, centerX, baseY, width, height, stdDev, label) {
        const startX = centerX - width / 2;
        const endX = centerX + width / 2;
        const numPoints = 200; // More points for smoother curve
        const curveColor = 'rgba(0, 119, 204, 0.8)'; // Blue with transparency
        const areaColor = 'rgba(0, 119, 204, 0.4)'; // Lighter blue for fill
        const axisColor = '#555';

        // Draw the filled area under the curve
        ctx.beginPath();
        ctx.moveTo(startX, baseY);
        for (let i = 0; i < numPoints; i++) {
            const x = startX + (i / (numPoints - 1)) * width;
            // Use Gaussian function: A * exp(-(x-mu)^2 / (2*sigma^2))
            // Scale 'sigma' based on stdDev, center 'mu' at centerX
            // Scale amplitude 'A' such that peak relates to 'height' and curve width
            // We need to find a scaling factor 'A' for the height and width.
            // The integral of the Gaussian is A * sigma * sqrt(2*pi). We want the area to represent total probability (1).
            // But here we just want to visualize the shape, so scale A to make peak height proportional to overall height and inversely proportional to width.
            // A simpler approach for visualization: scale sigma directly based on stdDev. Peak height depends on A/sigma. If A is constant, peak is 1/sigma.
            // Let's fix the integral (total probability "area") and let height/width vary.
            // Integral of exp(-(x-mu)^2 / (2*sigma^2)) is sigma * sqrt(2*pi).
            // To keep integral constant (representing total probability = 1), A must be 1 / (sigma * sqrt(2*pi)).
            // The peak height is then A = 1 / (sigma * sqrt(2*pi)).
            // So, peak height is inversely proportional to sigma (and thus stdDev).
            // Let's scale stdDev to fit the canvas width. stdDev should map to the visual width of the curve.
            // The curve width is visually represented by maybe 3-4 times stdDev.
            // Let's map stdDev to sigma. If stdDev is MIN_DELTA_DISPLAY, sigma is small (narrow curve). If stdDev is MAX_DELTA_DISPLAY, sigma is large (wide curve).
            // Use a mapping like sigma = stdDev * width / (4 * MAX_DELTA_DISPLAY) to keep it within bounds visually.
            // Peak height should be proportional to height and inversely proportional to sigma.
            // Peak height = height_scale / sigma. Let's pick a height_scale.
            const sigma = stdDev * (width / 5) / MAX_DELTA_DISPLAY; // Scale stdDev to canvas width, adjust multiplier (5) for visual spread
            const peakHeight = height * (MAX_DELTA_DISPLAY / (stdDev + MIN_DELTA_DISPLAY)); // Peak height inversely related to stdDev
             // Ensure peak height doesn't go off canvas
            const scaledPeakHeight = Math.min(peakHeight, height);


            const y = baseY - scaledPeakHeight * Math.exp(-Math.pow(x - centerX, 2) / (2 * Math.pow(sigma, 2)));


            if (i === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        ctx.lineTo(endX, baseY); // Close the curve to the x-axis on the right
        ctx.lineTo(startX, baseY); // Close the curve to the x-axis on the left
        ctx.fillStyle = areaColor;
        ctx.fill();

        // Draw the curve outline
        ctx.beginPath();
        ctx.moveTo(startX, baseY);
         for (let i = 0; i < numPoints; i++) {
            const x = startX + (i / (numPoints - 1)) * width;
             const sigma = stdDev * (width / 5) / MAX_DELTA_DISPLAY;
             const peakHeight = height * (MAX_DELTA_DISPLAY / (stdDev + MIN_DELTA_DISPLAY));
             const scaledPeakHeight = Math.min(peakHeight, height);
            const y = baseY - scaledPeakHeight * Math.exp(-Math.pow(x - centerX, 2) / (2 * Math.pow(sigma, 2)));
             if (i === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
         }
        ctx.strokeStyle = curveColor;
        ctx.lineWidth = 2;
        ctx.stroke();


        // Draw the base line (x-axis)
        ctx.beginPath();
        ctx.moveTo(startX, baseY);
        ctx.lineTo(endX, baseY);
        ctx.strokeStyle = axisColor;
        ctx.lineWidth = 1;
        ctx.stroke();

         // Optional: Draw lines indicating standard deviation (approximate)
         ctx.setLineDash([5, 5]); // Dashed lines
         const sigma = stdDev * (width / 5) / MAX_DELTA_DISPLAY;
         const stdDevMarkerHeight = baseY - scaledPeakHeight * Math.exp(-Math.pow(sigma, 2) / (2 * Math.pow(sigma, 2))); // Height at +/- 1 sigma
         if (stdDevMarkerHeight < baseY) { // Only draw if it's above the base line
            ctx.beginPath();
            ctx.moveTo(centerX - sigma, baseY);
            ctx.lineTo(centerX - sigma, stdDevMarkerHeight);
            ctx.moveTo(centerX + sigma, baseY);
            ctx.lineTo(centerX + sigma, stdDevMarkerHeight);
             ctx.strokeStyle = '#888';
            ctx.lineWidth = 1;
            ctx.stroke();
         }
         ctx.setLineDash([]); // Reset dash pattern

          // Draw center line
         ctx.beginPath();
         ctx.moveTo(centerX, baseY);
         ctx.lineTo(centerX, baseY - scaledPeakHeight);
         ctx.strokeStyle = '#888';
         ctx.lineWidth = 1;
         ctx.stroke();
    }

    // Animation variables
    let animationFrameId = null;
    let startTime = null;
    const animationDuration = 300; // ms

    // Function to draw the current state
    function drawState(deltaX, deltaP) {
         ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Draw Position Space (left half)
        const posXCanvasWidth = canvasWidth / 2;
        const posXCenterX = posXCanvasWidth / 2;
        const baseY = canvasHeight - 25; // Base line slightly above bottom
        const graphHeight = canvasHeight - 40; // Max height of the peak
        drawProbabilityDistribution(ctx, posXCenterX, baseY, posXCanvasWidth, graphHeight, deltaX, 'Δx');

        // Draw Momentum Space (right half)
        const momXCanvasWidth = canvasWidth / 2;
        const momXCenterX = canvasWidth / 2 + momXCanvasWidth / 2;
        drawProbabilityDistribution(ctx, momXCenterX, baseY, momXCanvasWidth, graphHeight, deltaP, 'Δp');

        // Draw separating line
        ctx.beginPath();
        ctx.moveTo(canvasWidth / 2, 0);
        ctx.lineTo(canvasWidth / 2, canvasHeight);
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        ctx.stroke();
    }


    // Animation loop
    function animateSimulation(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = Math.min(elapsed / animationDuration, 1); // Animation progress (0 to 1)

        // Calculate target values
        const targetSliderValue = parseInt(slider.value);
        const targetUncertainties = calculateUncertainties(targetSliderValue);
        const targetDeltaX = targetUncertainties.deltaX;
        const targetDeltaP = targetUncertainties.deltaP;

        // Interpolate values (use ease-out effect)
        const easedProgress = 1 - Math.pow(1 - progress, 3); // Ease-out cubic

        const animatedDeltaX = currentDeltaX + (targetDeltaX - currentDeltaX) * easedProgress;
        const animatedDeltaP = currentDeltaP + (targetDeltaP - currentDeltaP) * easedProgress;

        // Update display values
        deltaXSpan.textContent = animatedDeltaX.toFixed(2);
        deltaPSpan.textContent = animatedDeltaP.toFixed(2);
        productSpan.textContent = (animatedDeltaX * animatedDeltaP).toFixed(2);

        // Draw the animated state
        drawState(animatedDeltaX, animatedDeltaP);

        // Continue animation if not finished
        if (progress < 1) {
            animationFrameId = requestAnimationFrame(animateSimulation);
        } else {
             // Animation finished, update current values
             currentDeltaX = targetDeltaX;
             currentDeltaP = targetDeltaP;
             startTime = null; // Reset start time for next animation
        }
    }


    // Function to start or update animation
    function startAnimation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        startTime = null; // Reset animation timer
        animationFrameId = requestAnimationFrame(animateSimulation);
    }


    // Event listener for slider - trigger animation
    slider.addEventListener('input', startAnimation);

    // Initial setup
    function initializeSimulation() {
         // Get actual canvas dimensions after CSS is applied
        const container = canvas.parentElement;
        canvasWidth = container.clientWidth;
        canvasHeight = container.clientHeight;
        canvas.width = canvasWidth;
        canvas.height = canvasHeight;

        // Calculate initial values based on slider's initial position
        const initialSliderValue = parseInt(slider.value);
        const initialUncertainties = calculateUncertainties(initialSliderValue);
        currentDeltaX = initialUncertainties.deltaX;
        currentDeltaP = initialUncertainties.deltaP;

        // Draw the initial state immediately
        drawState(currentDeltaX, currentDeltaP);

        // Update initial output text
        deltaXSpan.textContent = currentDeltaX.toFixed(2);
        deltaPSpan.textContent = currentDeltaP.toFixed(2);
        productSpan.textContent = (currentDeltaX * currentDeltaP).toFixed(2);
    }

    // Initialize simulation on window load or DOMContentLoaded
    window.addEventListener('load', initializeSimulation);
    window.addEventListener('resize', initializeSimulation); // Re-initialize on resize

    // Toggle explanation visibility with animation
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = !explanationDiv.classList.contains('visible');
        if (isHidden) {
             explanationDiv.style.display = 'block'; // Make display block before adding class
             // Force reflow to apply display: block before transition
             explanationDiv.offsetHeight;
             explanationDiv.classList.add('visible');
             toggleExplanationButton.textContent = 'הסתר הסבר על עקרון אי-הוודאות';
        } else {
             explanationDiv.classList.remove('visible');
             toggleExplanationButton.textContent = 'גלו את הסוד: הצג הסבר על עקרון אי-הוודאות';
              // Hide after transition ends (optional, managed by max-height)
             // setTimeout(() => { explanationDiv.style.display = 'none'; }, 500); // Match transition duration
        }
    });

    // Ensure initial state is drawn even if load event is missed
    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        initializeSimulation();
    }

</script>