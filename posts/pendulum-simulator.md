---
title: "חקירת תנועת מטוטלת: גלו את הסודות!"
english_slug: pendulum-simulator
category: "פיזיקה"
tags:
  - מכניקה
  - תנועה מחזורית
  - הדמיה
  - אינטראקטיבי
  - ניסוי וגילוי
---
# חקירת תנועת מטוטלת: גלו את הסודות!

מוכנים למשחק? בואו נצלול פנימה ונגלה מה באמת קובע כמה מהר מטוטלת מתנדנדת. האם זה המשקל שלה? האם זה גודל התנופה שאנחנו נותנים לה? או אולי משהו אחר לגמרי? שחקו עם המטוטלת הווירטואלית הזו וגלו בעצמכם! זו הדרך הכי כיפית ללמוד!

<div class="pendulum-container">
    <div class="controls">
        <label for="length">אורך חוט (מטר):</label>
        <input type="range" id="length" min="0.5" max="3" value="1" step="0.1">
        <span id="lengthValue">1.0 מ'</span>
        <br>
        <label for="mass">מסת משקולת (ק"ג):</label>
        <input type="range" id="mass" min="0.1" max="5" value="1" step="0.1">
        <span id="massValue">1.0 ק"ג</span>
        <br>
        <label for="amplitude">משרעת התחלתית (מעלות):</label>
        <input type="range" id="amplitude" min="5" max="60" value="15" step="1">
        <span id="amplitudeValue">15°</span>
        <br>
         <button id="resetAmplitude">התחל/אפס תנודה</button>
        <div class="period-display">
            זמן מחזור (מוערך): <span id="periodValue">-</span> שניות
        </div>
    </div>
    <div class="simulation-area">
        <div id="pivot"></div>
        <div id="string"></div>
        <div id="bob"></div>
    </div>
</div>

<button id="toggleExplanation">הסבר מדעי: מאחורי הקלעים</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מדעי: מה באמת משפיע על זמן המחזור של מטוטלת?</h2>
    אחרי ששיחקתם וחקרו, הגיע הזמן להבין את הפיזיקה שמאחורי הקלעים. זמן המחזור של מטוטלת פשוטה (הזמן שלוקח לה לחזור לנקודת ההתחלה) מושפע בעיקר מגורם אחד מרכזי:
    <ol>
        <li><b>אורך החוט (L):</b> ראיתם בניסוי הווירטואלי? ככל שהחוט ארוך יותר, כך לוקח למטוטלת יותר זמן להשלים תנודה. הקשר הוא מתמטי: זמן המחזור פרופורציונלי לשורש הריבועי של האורך. חוט ארוך פי 4 ייתן זמן מחזור ארוך פי 2!</li>
        <li><b>תאוצת הכבידה (g):</b> גם כוח הכבידה משפיע! על כדור הארץ הכבידה די קבועה (כ-9.8 מטר/שנייה²), אבל אם הייתם לוקחים את המטוטלת לירח (שם הכבידה חלשה משמעותית), היא הייתה מתנדנדת הרבה יותר לאט. הסימולטור שלנו פועל בתנאי כדור הארץ.</li>
    </ol>
    עבור תנודות קטנות יחסית (פחות מ-15-20 מעלות), הנוסחה הקסומה לזמן המחזור (T) היא:
    <br>
    \[ T = 2\pi \sqrt{\frac{L}{g}} \]
    <br>
    איפה ש:
    <ul>
        <li>\( T \) הוא זמן המחזור שמדדנו.</li>
        <li>\( \pi \) הוא הקבוע המוכר (בערך 3.14159).</li>
        <li>\( L \) הוא אורך החוט במטרים.</li>
        <li>\( g \) היא תאוצת הכבידה (9.81 מ/ש² בכדור הארץ).</li>
    </ul>
    ועכשיו, המסקנות המעניינות מהניסוי שלכם:
    <ul>
        <li><b>מסת המשקולת:</b> מפתיע, נכון? משקל המשקולת כמעט ולא משפיע על זמן המחזור (בתנאים אידיאליים ולזוויות קטנות). כוח הכבידה שמושך אותה מטה גדל עם המסה, אבל גם ההתנגדות שלה לתנועה (האינרציה) גדלה באותו יחס, וההשפעות האלה מבטלות זו את זו!</li>
        <li><b>משרעת התנודה (הזווית ההתחלתית):</b> עבור זוויות קטנות, גם לזווית ההתחלתית השפעה זניחה. רק בזוויות גדולות מאוד (מעל 20-30 מעלות), זמן המחזור מתחיל לגדול מעט. הסימולטור הזה מתמקד בתחום הזוויות הקטנות שבו הנוסחה פשוטה ומדויקת.</li>
    </ul>
    אז בפעם הבאה שתראו שעון מטוטלת עתיק, תדעו שהדרך היחידה לכוון אותו היא על ידי שינוי אורך המוט, לא על ידי שינוי משקל המשקולת או גודל התנופה!

    <p style="font-size: 0.9em; color: #666; margin-top: 15px;">*הערה: סימולטור זה מבוסס על המודל של מטוטלת פשוטה ואידיאלית (חוט חסר מסה, אין חיכוך או התנגדות אוויר) ועבור משרעות קטנות. במציאות, יש השפעות קטנות נוספות.</p>
</div>

<style>
    /* General Enhancements */
    .pendulum-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: linear-gradient(to bottom right, #e0f2f7, #b3e5fc); /* Soft gradient background */
        border-radius: 15px;
        padding: 30px;
        margin: 20px auto;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* Stronger shadow */
        max-width: 600px; /* Limit max width */
        width: 95%;
        position: relative; /* Needed for potential absolute positioning inside */
        overflow: hidden; /* Clean edges */
    }

    h1 {
        color: #0277bd; /* A nice shade of blue */
        text-align: center;
        margin-bottom: 25px;
        font-size: 1.8em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }

    .controls {
        width: 100%;
        max-width: 450px; /* Wider controls */
        margin-bottom: 40px;
        background-color: #ffffff;
        padding: 25px; /* More padding */
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Nicer shadow */
        text-align: right; /* Align labels right */
    }

    .controls label {
        display: inline-block;
        width: 180px; /* Adjust width for labels */
        margin-bottom: 15px; /* More space between controls */
        font-weight: 600; /* Semi-bold */
        color: #555;
        font-size: 1em;
    }

    .controls input[type="range"] {
        width: calc(100% - 240px); /* Adjust based on label/span width */
        vertical-align: middle;
        cursor: pointer;
        -webkit-appearance: none; /* Remove default style */
        appearance: none;
        height: 8px; /* Thicker slider */
        background: #bbdefb; /* Light blue track */
        outline: none;
        opacity: 0.8;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* Larger thumb */
        height: 20px; /* Larger thumb */
        background: #039be5; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%; /* Round thumb */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #039be5;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }


    .controls span {
        display: inline-block;
        width: 60px; /* Wider span for values */
        text-align: left; /* Align values left */
        font-weight: 600;
        color: #039be5; /* Blue for values */
        font-size: 1em;
    }

    .period-display {
        margin-top: 25px;
        font-size: 1.4em; /* Larger font */
        font-weight: bold;
        text-align: center;
        color: #388e3c; /* Green */
        padding-top: 15px;
        border-top: 2px dashed #cfd8dc; /* Styled border */
    }

    .period-display span {
         color: #1b5e20; /* Darker green */
         font-size: 1.1em; /* Slightly larger than label */
    }

    #resetAmplitude {
        display: block;
        margin: 20px auto 0;
        padding: 12px 25px;
        background-color: #ff9800; /* Orange */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #resetAmplitude:hover {
        background-color: #f57c00; /* Darker orange */
    }

     #resetAmplitude:active {
        transform: scale(0.98); /* Press effect */
    }


    .simulation-area {
        position: relative;
        width: 100%; /* Use full width of container */
        max-width: 400px; /* Max width for simulation */
        height: 450px; /* Taller simulation area */
        margin-top: 30px;
        background-color: #e1f5fe; /* Very light blue */
        border-radius: 10px;
        overflow: hidden;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow */
        border: 1px solid #b3e5fc;
    }

    #pivot {
        position: absolute;
        top: 25px; /* Pivot point */
        left: 50%;
        transform: translateX(-50%);
        width: 40px; /* Wider pivot */
        height: 15px; /* Taller pivot */
        background: linear-gradient(to bottom, #757575, #424242); /* Metal gradient */
        border-radius: 7px 7px 0 0; /* Rounded top corners */
        z-index: 2;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

     /* Adding a pin/screw like element to pivot */
     #pivot::after {
         content: '';
         position: absolute;
         width: 8px;
         height: 8px;
         background-color: #bdbdbd;
         border-radius: 50%;
         top: 4px;
         left: 50%;
         transform: translateX(-50%);
         box-shadow: inset 0 1px 2px rgba(0,0,0,0.3);
     }


    #string {
        position: absolute;
        top: 25px; /* Start at pivot Y */
        left: 50%;
        width: 2px; /* String thickness */
        background-color: #424242; /* Darker string */
        transform-origin: top center; /* Rotate around the top */
        height: 100px; /* Initial height, will be set by JS */
        z-index: 1;
        transform: translateX(-1px); /* Center the 2px line */
    }

    #bob {
        position: absolute;
        width: 40px; /* Default size */
        height: 40px; /* Default size */
        background: radial-gradient(circle at top left, #ff5252, #c62828); /* Red gradient bob */
        border-radius: 50%;
        z-index: 3;
        box-shadow: 0 5px 10px rgba(0,0,0,0.3);
        transform: translate(-50%, -50%); /* Center the bob element on calculated point */
        /* Will be positioned by JS */
    }

    #toggleExplanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #toggleExplanation:hover {
        background-color: #0056b3;
    }

    #toggleExplanation:active {
         transform: scale(0.98); /* Press effect */
    }


    #explanation {
        margin-top: 30px;
        padding: 25px;
        background-color: #e1f5fe; /* Light background */
        border-left: 6px solid #0288d1; /* Blue border */
        border-radius: 10px;
        color: #333;
        line-height: 1.6;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    #explanation h2 {
        color: #0288d1; /* Darker blue */
        margin-top: 0;
        border-bottom: 2px solid #b3e5fc; /* Light blue border */
        padding-bottom: 15px;
        font-size: 1.5em;
    }

    #explanation ol, #explanation ul {
        margin-left: 25px;
        padding-left: 0;
    }

    #explanation li {
        margin-bottom: 12px;
        padding-left: 5px; /* Indent list items */
    }

    #explanation b {
        color: #01579b; /* Even darker blue for emphasis */
    }

    /* Styling for LaTeX formula if MathJax is used */
    #explanation .MathJax_Display {
        margin: 20px 0;
        overflow-x: auto; /* Allow horizontal scroll for formulas */
    }


</style>

<script>
    // Inject MathJax script for rendering LaTeX if not already present
    // This needs to be done carefully to not interfere with the page loading
    // A common pattern is to check if MathJax is defined
    if (typeof MathJax === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
        script.async = true;
        document.head.appendChild(script);
    } else {
        // If MathJax is already loaded, trigger rendering again
        if (MathJax.typesetPromise) {
            MathJax.typesetPromise();
        } else if (MathJax.Hub) { // For MathJax v2
             MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        }
    }


    const lengthSlider = document.getElementById('length');
    const massSlider = document.getElementById('mass');
    const amplitudeSlider = document.getElementById('amplitude');
    const lengthValueSpan = document.getElementById('lengthValue');
    const massValueSpan = document.getElementById('massValue');
    const amplitudeValueSpan = document.getElementById('amplitudeValue');
    const periodValueSpan = document.getElementById('periodValue');
    const stringElement = document.getElementById('string');
    const bobElement = document.getElementById('bob');
    const simulationArea = document.querySelector('.simulation-area');
    const resetAmplitudeButton = document.getElementById('resetAmplitude');


    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggleExplanation');

    const g = 9.81; // Acceleration due to gravity (m/s^2)
    const pivotY = 25; // Y position of the pivot in pixels from simulation-area top

    let animationFrameId = null;
    let startTime = null;
    let initialAngleRad = 0; // Angle in radians set by amplitude slider
    let currentAngleRad = 0; // Current angle in radians during animation
    let angularFrequency = 0; // ω = sqrt(g/L)

    // Function to update all visual elements and physics parameters
    function updatePendulumVisualsAndPhysics() {
        const length = parseFloat(lengthSlider.value);
        const mass = parseFloat(massSlider.value);
        const amplitude = parseFloat(amplitudeSlider.value); // in degrees

        // Update displayed values with units
        lengthValueSpan.textContent = `${length.toFixed(1)} מ'`;
        massValueSpan.textContent = `${mass.toFixed(1)} ק"ג`;
        amplitudeValueSpan.textContent = `${amplitude.toFixed(0)}°`;

        // Calculate and display Period (for small angles)
        const period = 2 * Math.PI * Math.sqrt(length / g);
        periodValueSpan.textContent = period.toFixed(2);

        // Update physics parameters for animation
        initialAngleRad = amplitude * Math.PI / 180; // Convert initial amplitude to radians
        angularFrequency = Math.sqrt(g / length); // ω = sqrt(g/L)

        // Calculate string pixel length based on its proportion to the maximum length allowed in the simulation area
        // This ensures the pendulum fits reasonably within the simulation area
        const maxPendulumLengthPhysics = parseFloat(lengthSlider.max); // Max length slider value
        const simulationAreaHeight = simulationArea.offsetHeight;
        const maxPendulumLengthPixels = simulationAreaHeight - pivotY - (bobElement.offsetHeight / 2) - 10; // Max available space minus pivot and bob radius

        // Calculate string pixel length scaled to the simulation area
        const stringPixelLength = (length / maxPendulumLengthPhysics) * maxPendulumLengthPixels;

        // Update visual properties based on sliders
        stringElement.style.height = `${stringPixelLength}px`;

        // Optionally update bob size based on mass (visual cue, doesn't affect physics in this simulation)
        // const bobSize = 30 + (mass / parseFloat(massSlider.max)) * 30; // Scale bob size from 30px to 60px
        // bobElement.style.width = `${bobSize}px`;
        // bobElement.style.height = `${bobSize}px`;
        // The centering transform `translate(-50%, -50%)` handles the size change correctly.

        // Position the bob at the initial amplitude before animation starts
        // Calculate initial bob position
        const pivotPixelX = simulationArea.offsetWidth / 2;
        const pivotPixelY = pivotY;

        const initialBobPixelX = pivotPixelX + stringPixelLength * Math.sin(initialAngleRad);
        const initialBobPixelY = pivotPixelY + stringPixelLength * Math.cos(initialAngleRad);

        bobElement.style.left = `${initialBobPixelX}px`;
        bobElement.style.top = `${initialBobPixelY}px`;
        // stringElement will be rotated in the animation loop based on currentAngleRad

        // Restart animation
        startAnimation();
    }

    // Animation loop
    function animate(currentTime) {
        if (!startTime) startTime = currentTime;
        const elapsed = (currentTime - startTime) / 1000; // time in seconds

        // Simple Harmonic Motion angle calculation: θ(t) = θ_max * cos(ωt)
        // Assumes starting at max amplitude (released from rest)
        currentAngleRad = initialAngleRad * Math.cos(angularFrequency * elapsed);

         // Recalculate string pixel length in case simulation area size changes or slider values changed
        const length = parseFloat(lengthSlider.value);
        const maxPendulumLengthPhysics = parseFloat(lengthSlider.max);
        const simulationAreaHeight = simulationArea.offsetHeight;
        const maxPendulumLengthPixels = simulationAreaHeight - pivotY - (bobElement.offsetHeight / 2) - 10;
        const stringPixelLength = (length / maxPendulumLengthPhysics) * maxPendulumLengthPixels;
        stringElement.style.height = `${stringPixelLength}px`;


        // Rotate the string element
        // We need to apply rotation *after* setting height for correct transform-origin scaling
        stringElement.style.transform = `translateX(-1px) rotate(${currentAngleRad}rad)`; // Rotate string around its top center

        // Calculate bob position based on rotated string endpoint
        const pivotPixelX = simulationArea.offsetWidth / 2;
        const pivotPixelY = pivotY;

        const bobPixelX = pivotPixelX + stringPixelLength * Math.sin(currentAngleRad);
        const bobPixelY = pivotPixelY + stringPixelLength * Math.cos(currentAngleRad);

        // Position the bob element center
        bobElement.style.left = `${bobPixelX}px`;
        bobElement.style.top = `${bobPixelY}px`;
        // translate(-50%, -50%) is already in CSS for centering


        animationFrameId = requestAnimationFrame(animate);
    }

    // Function to start or restart the animation
    function startAnimation() {
         // Stop any previous animation
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        startTime = null; // Reset start time
        // The animation loop will pick up the new initialAngleRad and angularFrequency
        animationFrameId = requestAnimationFrame(animate);
    }


    // Initial update and animation start
    updatePendulumVisualsAndPhysics();

    // Add event listeners to sliders - update physics and restart animation on change
    lengthSlider.addEventListener('input', updatePendulumVisualsAndPhysics);
    massSlider.addEventListener('input', updatePendulumVisualsAndPhysics); // Mass updates display and possibly bob size visual, restarts animation
    amplitudeSlider.addEventListener('input', updatePendulumVisualsAndPhysics); // Amplitude updates value, initial angle, restarts animation

    // Add event listener for the reset button
    resetAmplitudeButton.addEventListener('click', () => {
         // Reset to the current amplitude slider value
        const currentAmplitude = parseFloat(amplitudeSlider.value);
        initialAngleRad = currentAmplitude * Math.PI / 180;
        // No need to update visuals here, updatePendulumVisualsAndPhysics does that.
        startAnimation(); // Simply restart the animation from the current amplitude
    });


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתרת ההסבר המדעי' : 'הסבר מדעי: מאחורי הקלעים';

         // If showing explanation and MathJax is available, typeset
         if (isHidden && typeof MathJax !== 'undefined') {
             if (MathJax.typesetPromise) {
                MathJax.typesetPromise();
            } else if (MathJax.Hub) { // For MathJax v2
                MathJax.Hub.Queue(["Typeset",MathJax.Hub, explanationDiv]); // Typeset only the explanation div
            }
         }
    });

    // Initial state of button text
    toggleButton.textContent = 'הסבר מדעי: מאחורי הקלעים';

    // Ensure animation restarts if window is resized, as simulationArea dimensions might change
     window.addEventListener('resize', updatePendulumVisualsAndPhysics);


</script>