---
title: "מסע אל גבולות המהירות: סימולציה של התארכות הזמן והתכווצות האורך"
english_slug: special-relativity-simulation-time-dilation-length-contraction
category: "מדעים מדויקים / פיזיקה"
tags: ["יחסות פרטית", "התארכות זמן", "התכווצות אורך", "סימולציה", "איינשטיין"]
---
# מסע אל גבולות המהירות: סימולציה של התארכות הזמן והתכווצות האורך

האם דמיינתם פעם מה קורה כשמתקרבים, אבל ממש מתקרבים, למהירות האור? היקום מתנהג מוזר בהירויות כאלה! חוקי הפיזיקה הקלאסית שאנו מכירים מחיי היומיום מפנים את מקומם למציאות שבה זמן ואורך אינם קבועים, אלא גמישים ותלויים במהירות שבה אתם נעים. הצטרפו אלינו למסע וירטואלי כדי לחזות בתופעות המדהימות הללו דרך סימולציה אינטראקטיבית.

<div id="app-container">
    <div id="controls">
        <label for="velocity-slider">קבעו את מהירות התנועה (ביחס למהירות האור, c):</label><br>
        <input type="range" id="velocity-slider" min="0" max="0.999" step="0.001" value="0">
        <div id="velocity-display-container">
             מהירות: <span id="velocity-display">0.000c</span>
        </div>
    </div>

    <div id="simulation-area">
        <div class="frame-of-reference stationary-frame">
            <h3>נקודת מבט: צופה נייח</h3>
            <div class="visualization-objects">
                <div class="clock" id="stationary-clock">
                    <div class="hand second-hand"></div>
                </div>
                 <div class="length-object stationary" id="stationary-object">
                    <span class="object-label">אורך עצמי</span>
                 </div>
            </div>
            <p>זמן מקומי שחלף: <span id="stationary-time">0.00</span> שניות</p>
            <p>אורך נמדד: <span id="stationary-length">1.00</span> יחידות</p>
        </div>

        <div class="frame-of-reference moving-frame">
            <h3>נקודת מבט: אובייקט נע במהירות</h3>
             <div class="visualization-objects">
                <div class="clock" id="moving-clock">
                     <div class="hand second-hand"></div>
                 </div>
                 <div class="length-object moving" id="moving-object">
                     <span class="object-label" id="moving-object-label">אורך נצפה: 1.00</span>
                 </div>
            </div>
            <p>זמן מקומי שחלף (זמן עצמי): <span id="moving-time">0.00</span> שניות</p>
            <p>אורך עצמי: <span id="moving-length-proper">1.00</span> יחידות</p> <!-- Assuming proper length is 1 -->
        </div>
    </div>

     <div id="results">
         <h3>תוצאות המדידה מהמסגרת הנייחת:</h3>
        <p>פקטור לורנץ (γ): <span id="gamma-factor">1.00</span></p>
        <p>התארכות זמן: כל 1 שנייה שעוברת לאובייקט הנע נמדדת כ-<span id="time-dilation">1.00</span> שניות ע"י הצופה הנייח.</p>
        <p>התכווצות אורך: אובייקט באורך 1 יחידה כשהוא במנוחה נמדד כ-<span id="length-contraction">1.00</span> יחידות ע"י הצופה הנייח כשהוא נע.</p>
    </div>
</div>

<button id="toggle-explanation">רוצים להבין איך זה קורה? לחצו להסבר!</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: תורת היחסות הפרטית בהסבר פשוט</h2>
    <p>בתורת היחסות הפרטית, אלברט איינשטיין שינה את האופן שבו אנו מבינים את המרחב והזמן. הרעיון המרכזי הוא שמהירות האור (c) בריק היא קבועה ואוניברסלית - היא זהה לכל צופה, ללא קשר למהירות שלו. כדי שזה יהיה נכון, דברים מוזרים חייבים לקרות למרחב וזמן עצמם!</p>

    <h3>הזמן מתמתח: התארכות הזמן (Time Dilation)</h3>
    <p>אם יש לכם שני שעונים זהים, אחד לידכם ואחד נע ביחס אליכם במהירות גבוהה (v), אתם, כצופים נייחים, תראו שהשעון הנע "מתקתק" לאט יותר מהשעון שלכם. ככל שהמהירות v קרובה יותר ל-c, האפקט דרמטי יותר. נוסחת הקסם שמחברת בין הזמן שחלף בשעון הנייח (Δt) לזמן שחלף בשעון הנע (Δt₀ - הנקרא "זמן עצמי" כי הוא נמדד במסגרת המנוחה של השעון) היא: Δt = γ * Δt₀</p>
    <p>הגורם γ (אות יוונית גמא) נקרא "פקטור לורנץ" והוא מחושב כך: γ = 1 / √(1 - v²/c²). שימו לב: ככל ש-v עולה, v²/c² מתקרב ל-1, המכנה מתקרב ל-0, וגמא שואף לאינסוף! כלומר, בזמן ששנייה אחת חולפת בשעון הנע, כמות אינסופית של זמן יכולה לחלוף עבור צופה נייח כשהמהירות קרובה מאוד ל-c.</p>

    <h3>האורך מתכווץ: התכווצות האורך (Length Contraction)</h3>
    <p>באופן דומה, עצם שנע ביחס אליכם במהירות v ייראה לכם קצר יותר בכיוון התנועה מאורכו האמיתי (האורך העצמי, L₀, הנמדד כשהעצם במנוחה יחסית לצופה). הקשר כאן הפוך מהזמן: L = L₀ / γ. </p>
    <p>שוב, γ הוא פקטור לורנץ. ככל ש-v מתקרבת ל-c, גמא גדל, והאורך הנמדד (L) קטן ושואף לאפס. זה כאילו שהעצם נמעך או נדחס בכיוון התנועה מנקודת המבט של הצופה הנייח.</p>
    <p>הסימולציה שלפניכם מאפשרת לכם לשחק עם המהירות (v) ולראות באופן ויזואלי ועם מספרים כיצד פקטור לורנץ גדל, וכיצד הוא משפיע על התארכות הזמן (זמן השעון הנע עובר לאט יותר מבחינתכם) והתכווצות האורך (האובייקט הנע קצר יותר מבחינתכם).</p>
</div>

<style>
    #app-container {
        font-family: 'Heebo', sans-serif; /* Using Heebo or similar clean font */
        direction: rtl;
        text-align: right;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        max-width: 900px;
        margin: 25px auto;
        background: linear-gradient(to bottom right, #f0f4f8, #e9eef2); /* Soft gradient background */
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        overflow: hidden; /* Clear floats/margins */
    }

    h1, h2, h3 {
        color: #2c3e50; /* Dark blue/grey */
        text-align: center;
        margin-bottom: 20px;
        font-weight: 600;
    }

    h1 {
        margin-bottom: 30px;
        color: #0a3d62; /* Darker blue */
    }

    p {
        color: #34495e; /* Slightly lighter text color */
        line-height: 1.7;
    }

    #controls {
        margin-bottom: 35px;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.07);
        text-align: center;
    }

    #controls label {
        font-size: 1.1em;
        color: #2c3e50;
        margin-bottom: 10px;
        display: block;
    }

    #velocity-slider {
        width: 98%;
        margin-top: 15px;
        -webkit-appearance: none;
        appearance: none;
        height: 10px;
        background: linear-gradient(to right, #3498db, #e74c3c); /* Gradient for slider track */
        outline: none;
        opacity: 0.9;
        transition: opacity 0.2s ease-in-out;
        border-radius: 5px;
    }

    #velocity-slider:hover {
        opacity: 1;
    }

    #velocity-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 24px;
        height: 24px;
        background: #3498db; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 3px solid #ffffff;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }
     #velocity-slider:hover::-webkit-slider-thumb {
         background-color: #2980b9; /* Darker blue on hover */
     }


    #velocity-slider::-moz-range-thumb {
        width: 24px;
        height: 24px;
        background: #3498db; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 3px solid #ffffff;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }
    #velocity-slider:hover::-moz-range-thumb {
        background-color: #2980b9; /* Darker blue on hover */
    }

     #velocity-display-container {
         margin-top: 15px;
         font-size: 1.2em;
         color: #555;
     }

    #velocity-display {
        font-weight: bold;
        color: #e74c3c; /* Red color for speed */
        min-width: 80px; /* Prevent jumping */
        display: inline-block;
        text-align: left; /* Align 'c' part nicely */
    }

    #simulation-area {
        display: flex;
        justify-content: space-around;
        gap: 30px;
        margin-bottom: 35px;
        flex-wrap: wrap;
    }

    .frame-of-reference {
        flex: 1;
        min-width: 280px; /* Ensure minimum width */
        padding: 20px;
        border: 1px solid #bdc3c7; /* Light grey border */
        border-radius: 8px;
        background-color: #ffffff;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.07);
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .moving-frame {
         border-color: #3498db; /* Blue border for moving frame */
         box-shadow: 0 4px 12px rgba(52, 152, 219, 0.2); /* Blue shadow */
    }


    .visualization-objects {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin: 20px 0;
        min-height: 100px; /* Ensure space even if objects shrink */
    }

    .clock {
        width: 90px;
        height: 90px;
        border: 4px solid #333;
        border-radius: 50%;
        margin: 0 10px;
        position: relative;
        background-color: #ecf0f1; /* Light background */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
        flex-shrink: 0; /* Prevent shrinking */
    }

    .clock::after { /* Center dot */
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 8px;
        height: 8px;
        background: #333;
        border-radius: 50%;
        transform: translate(-50%, -50%);
        z-index: 2;
    }

     .clock .hand {
        position: absolute;
        bottom: 50%;
        left: 50%;
        width: 4px;
        height: 40%;
        background: #e74c3c; /* Red hand */
        transform-origin: bottom center;
        transform: translateX(-50%) rotate(0deg);
        z-index: 1;
        border-radius: 2px;
     }

    .length-object {
        height: 25px; /* Thicker bar */
        background-color: #2ecc71; /* Emerald green */
        margin: 0 10px;
        border-radius: 4px;
        transition: width 0.3s ease-out, background-color 0.3s ease; /* Smooth transitions */
        position: relative;
        display: flex; /* For centering label */
        justify-content: center;
        align-items: center;
        color: white;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
         min-width: 30px; /* Prevent it from disappearing completely at high speeds */
    }

     .object-label {
         position: absolute;
         top: -25px;
         font-size: 0.9em;
         color: #555;
         white-space: nowrap; /* Keep label on one line */
     }

    .length-object.stationary {
        width: 80%; /* Base length visualization percentage */
    }
    .length-object.moving {
         width: 80%; /* Base width, will be modified by JS */
    }

     #moving-object-label {
         top: auto; /* Override top positioning */
         bottom: -25px; /* Position label below */
         color: #3498db; /* Blue color for moving object label */
         font-size: 1em;
         font-weight: bold;
         text-shadow: none;
     }


    #results {
        margin-top: 30px;
        padding: 20px;
        background-color: #eef;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.07);
    }

    #results h3 {
         margin-bottom: 15px;
         color: #2c3e50;
    }

    #results p {
        margin: 10px 0;
        font-size: 1.15em;
        color: #34495e;
    }

    #results span {
        font-weight: bold;
        color: #e74c3c; /* Red color for result values */
    }

    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #95a5a6; /* Grey */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Heebo', sans-serif;
    }

    #toggle-explanation:hover {
        background-color: #7f8c8d; /* Darker grey */
    }

    #toggle-explanation:active {
        transform: scale(0.98); /* Press effect */
    }


    #explanation {
        margin-top: 25px;
        padding: 25px;
        border: 1px solid #bdc3c7;
        border-radius: 8px;
        background-color: #ffffff;
        line-height: 1.8;
        box-shadow: 0 4px 8px rgba(0,0,0,0.07);
    }

    #explanation h2, #explanation h3 {
        text-align: right;
        color: #2c3e50;
        margin-bottom: 15px;
        border-bottom: 2px solid #ecf0f1; /* Light line */
        padding-bottom: 8px;
    }

    #explanation p {
        margin-bottom: 18px;
        color: #34495e;
    }

    /* Add some simple responsive adjustments */
    @media (max-width: 700px) {
        #simulation-area {
            flex-direction: column;
            align-items: center;
        }
        .frame-of-reference {
            width: 95%;
            margin-bottom: 20px;
        }
    }

</style>

<script>
    const velocitySlider = document.getElementById('velocity-slider');
    const velocityDisplay = document.getElementById('velocity-display');
    const gammaFactorDisplay = document.getElementById('gamma-factor');
    const timeDilationDisplay = document.getElementById('time-dilation');
    const lengthContractionDisplay = document.getElementById('length-contraction');
    const movingObject = document.getElementById('moving-object');
    const movingObjectLabel = document.getElementById('moving-object-label');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    const stationaryClockHand = document.querySelector('#stationary-clock .hand');
    const movingClockHand = document.querySelector('#moving-clock .hand');


    // Base values for visualization (using relative units/percentages where possible)
    const baseLengthPercentage = 80; // Base width in percentage for the stationary object

    // Function to calculate Lorentz factor (gamma)
    function calculateGamma(v) {
        // Use a small epsilon to prevent division by zero near v=1
        const vSquared = v * v;
        if (vSquared >= 1) return 1000; // Return a large number for practical simulation purposes near c
        const gamma = 1 / Math.sqrt(1 - vSquared);
         // Cap gamma at a high value to avoid display issues with infinity
         return Math.min(gamma, 500); // Cap gamma at 500 for visualization
    }

    // Function to update simulation visuals and numbers based on velocity
    function updateSimulationVisuals(v) {
        const gamma = calculateGamma(v);

        // Update displays
        velocityDisplay.textContent = v.toFixed(3) + 'c';
        gammaFactorDisplay.textContent = gamma.toFixed(2);

        // Time Dilation Factor: Δt = γ * Δt₀. Display shows γ.
        timeDilationDisplay.textContent = gamma.toFixed(2);

        // Length Contraction Factor: L = L₀ / γ. Display shows 1/γ.
        const lengthContractionFactor = 1 / gamma;
        lengthContractionDisplay.textContent = lengthContractionFactor.toFixed(2);

        // Update moving object width visualization
        // Observed width is (baseLength / gamma)%
        const observedWidthPercentage = baseLengthPercentage / gamma;
        movingObject.style.width = observedWidthPercentage + '%';

        // Update moving object label
        movingObjectLabel.textContent = `אורך נצפה: ${lengthContractionFactor.toFixed(2)}`;

         // Change color based on speed for visual emphasis
         if (v > 0.95) {
             movingObject.style.backgroundColor = '#e74c3c'; // Red
             movingClockHand.style.backgroundColor = '#e74c3c';
         } else if (v > 0.8) {
             movingObject.style.backgroundColor = '#f39c12'; // Orange
             movingClockHand.style.backgroundColor = '#f39c12';
         } else if (v > 0.5) {
              movingObject.style.backgroundColor = '#f1c40f'; // Yellow
              movingClockHand.style.backgroundColor = '#f1c40f';
         }
         else {
             movingObject.style.backgroundColor = '#2ecc71'; // Green
             movingClockHand.style.backgroundColor = '#e74c3c'; // Back to red hand
         }

         // Update border color of moving frame
         if (v > 0.9) {
             document.querySelector('.moving-frame').style.borderColor = '#e74c3c'; /* Red border */
              document.querySelector('.moving-frame').style.boxShadow = '0 4px 12px rgba(231, 76, 60, 0.3)'; /* Red shadow */
         } else if (v > 0.5) {
             document.querySelector('.moving-frame').style.borderColor = '#f1c40f'; /* Yellow border */
              document.querySelector('.moving-frame').style.boxShadow = '0 4px 12px rgba(241, 196, 15, 0.3)'; /* Yellow shadow */
         }
         else {
             document.querySelector('.moving-frame').style.borderColor = '#3498db'; /* Blue border */
             document.querySelector('.moving-frame').style.boxShadow = '0 4px 12px rgba(52, 152, 219, 0.2)'; /* Blue shadow */
         }

    }

    // Event listener for slider change
    velocitySlider.addEventListener('input', (event) => {
        const v = parseFloat(event.target.value);
        updateSimulationVisuals(v);
    });

    // Initial update on page load
    updateSimulationVisuals(parseFloat(velocitySlider.value));

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'רוצים להבין איך זה קורה? לחצו להסבר!';
        }
    });

    // Clock animation and time display update (simulating passage of time)
    let stationaryTime = 0; // Time elapsed in the stationary frame (seconds)
    let movingTimeProper = 0; // Proper time elapsed in the moving frame (seconds)
    const simulationSpeed = 0.1; // Simulate 0.1 stationary seconds per interval
    const intervalMs = 100; // Update every 100ms

    const stationaryTimeDisplay = document.getElementById('stationary-time');
    const movingTimeDisplay = document.getElementById('moving-time'); // This displays proper time in moving frame

    // Total degrees for one full rotation (1 second represented by 360 degrees)
    const degreesPerSecond = 360;

    setInterval(() => {
        const v = parseFloat(velocitySlider.value);
        const gamma = calculateGamma(v);

        // Time elapsed in the stationary frame in this interval
        const deltaTimeStationary = simulationSpeed;
        stationaryTime += deltaTimeStationary;

        // Time elapsed in the moving frame in this interval (proper time)
        // Δt_moving_proper = Δt_stationary / gamma
        const deltaTimeMovingProper = deltaTimeStationary / gamma;
        movingTimeProper += deltaTimeMovingProper;

        // Update numerical time displays
        stationaryTimeDisplay.textContent = stationaryTime.toFixed(2);
        movingTimeDisplay.textContent = movingTimeProper.toFixed(2);

        // Update clock hand rotation
        // Stationary hand rotates based on stationaryTime
        const stationaryRotation = (stationaryTime % 1) * degreesPerSecond; // Calculate rotation based on fractional second
        stationaryClockHand.style.transform = `translateX(-50%) rotate(${stationaryRotation}deg)`;

        // Moving hand rotates based on movingTimeProper
         const movingRotation = (movingTimeProper % 1) * degreesPerSecond; // Calculate rotation based on fractional proper second
         movingClockHand.style.transform = `translateX(-50%) rotate(${movingRotation}deg)`;


         // Simple reset to prevent numbers from getting too large
         const resetThreshold = 30; // Reset after 30 simulated stationary seconds
         if (stationaryTime >= resetThreshold) {
             stationaryTime = stationaryTime % resetThreshold; // Keep remainder for smoother reset? Or just reset to 0. Let's reset to 0.
             stationaryTime = 0;
             movingTimeProper = 0; // Reset moving time as well
             // On reset, update displays immediately to show 0
             stationaryTimeDisplay.textContent = stationaryTime.toFixed(2);
             movingTimeDisplay.textContent = movingTimeProper.toFixed(2);
         }


    }, intervalMs); // Update every intervalMs milliseconds

    // Set initial visual properties for the stationary objects (assuming proper length is 1 unit)
    document.getElementById('stationary-object').style.width = baseLengthPercentage + '%';
    document.getElementById('stationary-length').textContent = (1).toFixed(2); // Show 1.00 unit
     document.getElementById('moving-length-proper').textContent = (1).toFixed(2); // Show 1.00 unit for proper length

</script>