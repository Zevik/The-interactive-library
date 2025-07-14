---
title: "ריקוד הגלים: הדמיית התאבכות"
english_slug: wave-interference-simulation
category: "מדעים מדויקים / פיזיקה"
tags:
  - גלים
  - התאבכות
  - הדמיה
---
<h1>ריקוד הגלים: הצצה לתופעת ההתאבכות משני מקורות</h1>

<p>הצטרפו למסע ויזואלי מרתק אל לב תופעת ההתאבכות! ראו במו עיניכם כיצד גלים היוצאים משני מקורות שונים נפגשים, מתלכדים, ויוצרים יחד תבניות עוצרות נשימה במרחב. שחקו עם המרחק בין המקורות, אורך הגל, ואפילו הזזת הפאזה בין המקורות, וגלו כיצד כל שינוי קטן משפיע על הריקוד המורכב של הגלים.</p>

<div class="simulation-container">
    <div class="controls">
        <div>
            <label for="distance">מרחק בין מקורות:</label>
            <input type="range" id="distance" min="50" max="300" value="150">
            <span id="distanceValue">150</span> יחידות
        </div>
        <div>
            <label for="wavelength">אורך גל:</label>
            <input type="range" id="wavelength" min="10" max="100" value="40">
            <span id="wavelengthValue">40</span> יחידות
        </div>
         <div>
            <label for="phase">הפרש פאזה:</label>
            <input type="range" id="phase" min="0" max="360" value="0">
            <span id="phaseValue">0°</span>
        </div>
        <div>
             <label for="amplitude">אמפליטודה:</label>
             <input type="range" id="amplitude" min="1" max="10" value="5" disabled>
             <span id="amplitudeValue">5</span> יחידות (קבועה)
        </div>
       
        <button id="resetButton">איפוס הגדרות</button>
    </div>
    <canvas id="waveCanvas"></canvas>
</div>

<button id="toggleExplanation">חשיפת הסוד מאחורי התבנית: לחצו להסבר</button>

<div class="explanation">
    <h2>מה ראינו? פירוק התבנית המסתורית</h2>
    <p>התבנית המרהיבה שראיתם היא תוצאה של <strong>התאבכות גלים</strong>. זה קורה כאשר שני גלים (או יותר) נפגשים באותה נקודה במרחב והאנרגיה שלהם מתלכדת. האמפליטודה (עוצמת הגל המרבית) של הגל השקול בנקודת המפגש היא פשוט סכום האמפליטודות של הגלים הנפגשים – זהו <strong>עיקרון הסופרפוזיציה</strong>.</p>
    
    <h3>שני סוגי מפגשים גורליים:</h3>
    <ul>
        <li><strong>התאבכות בונה:</strong> דמיינו שתי פסגות גלים נפגשות בדיוק באותו רגע, או שני שפלים. במקרה זה, הן מחזקות זו את זו! האמפליטודות מתחברות והגל השקול חזק יותר (בעל אמפליטודה מקסימלית). זה מתרחש בנקודות בהן הפרש הדרכים שהגלים עברו מהמקורות שווה למספר שלם של אורכי גל (Δr = nλ) <strong>וגם</strong> כאשר הגלים נפגשים באותה פאזה (או בהפרש פאזה שהוא כפולה שלמה של 360°). באזורים אלו בהדמיה, הצבע מתחלף במהירות ובאופן אינטנסיבי בין כחול עמוק לאדום בוהק, המייצגים את שיא האמפליטודה החיובית והשלילית של הגל השקול בכל רגע.</li>
        <li><strong>התאבכות הורסת:</strong> ומה קורה כשפסגה פוגשת שפל? הם מבטלים זה את זה! האמפליטודות מחסירות זו מזו, ובנקודת המפגש האמפליטודה יכולה להיות קטנה משמעותית, ואפילו אפסית לגמרי אם הגלים זהים ונפגשים בפאזה הפוכה (הפרש פאזה של 180°, 540°, וכו'). זה קורה בנקודות בהן הפרש הדרכים שהגלים עברו שווה למספר חצי שלם של אורכי גל (Δr = (n + 1/2)λ) <strong>או</strong> כאשר הפרש הפאזה ההתחלתי בין המקורות גורם להם להיפגש בפאזה הפוכה. באזורים אלו בהדמיה, הצבע נשאר קרוב ללבן/אפור ניטרלי, המצביע על אמפליטודה קרובה לאפס שאינה משתנה משמעותית בזמן.</li>
    </ul>
    
    <p>השינוי <strong>במרחק בין המקורות</strong> משנה את הפרשי הדרכים לכל נקודה במרחב, וכך מעצב מחדש את מיקום פסי ההתאבכות הבונה וההורסת. שינוי <strong>באורך הגל</strong> (או תדר הגל) משנה את קנה המידה של התבנית - אורכי גל קצרים יותר יוצרים תבנית צפופה יותר. שינוי <strong>בהפרש הפאזה ההתחלתי</strong> בין המקורות מזיז את התבנית כולה במרחב, ולעיתים אף יכול להחליף אזורי בונה והורסת!</p>
    <p>חקרו, שחקו, וגלו את הפיזיקה היפהפייה שמאחורי ריקוד הגלים!</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap'); /* Using Heebo font for a modern Hebrew feel */

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7; /* Slightly increased line height */
        margin: 0; /* Remove default margin */
        padding: 20px;
        background-color: #f8f9fa; /* Very light gray/blue */
        color: #212529; /* Darker gray for better contrast */
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2 {
        color: #003f7f; /* Deep blue */
        text-align: center;
        margin-bottom: 25px; /* More space below headings */
        font-weight: 700; /* Bold headings */
        line-height: 1.4;
    }
    
    h1 {
        font-size: 2em; /* Larger main heading */
    }

    p {
        margin-bottom: 20px; /* More space below paragraphs */
        text-align: justify;
        direction: rtl;
    }
    
    label {
        font-weight: bold;
        color: #003f7f; /* Match headings color */
        direction: rtl; /* Ensure labels are RTL */
        text-align: right;
        margin-left: 5px; /* Space between label and input */
    }

    .simulation-container {
        display: flex;
        flex-direction: column; /* Stack controls above canvas */
        align-items: center;
        background: linear-gradient(145deg, #ffffff, #eef2f7); /* Subtle gradient background */
        padding: 25px;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* More prominent shadow */
        margin-bottom: 30px; /* More space below container */
        width: 100%;
        max-width: 850px; /* Slightly wider max width */
        margin-left: auto;
        margin-right: auto;
        box-sizing: border-box; /* Include padding in width */
    }

    .controls {
        margin-bottom: 25px; /* More space below controls */
        padding: 20px; /* More padding */
        background-color: #e9ecef; /* Light gray background */
        border-radius: 8px; /* Rounded corners for controls */
        width: 100%; /* Take full width of container */
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 20px; /* Increased space between control items */
        justify-content: center; /* Center controls horizontally */
        box-sizing: border-box;
    }

    .controls > div { /* Wrapper for label+input+span */
        display: flex;
        align-items: center;
        gap: 8px; /* Space between elements in a control group */
        flex-basis: 280px; /* Slightly larger minimum width for each control group */
        flex-grow: 1; /* Allow growing */
    }

    .controls input[type="range"] {
        flex-grow: 1; /* Allow range input to take available space */
        cursor: pointer;
        accent-color: #007bff; /* Highlight color for range slider */
    }
    
    .controls input[type="range"]:disabled {
        opacity: 0.5; /* Less opacity for disabled */
        cursor: not-allowed;
    }

    .controls span {
        min-width: 40px; /* Space for value display */
        text-align: left; /* Align text left within the span */
        color: #495057; /* Darker gray for values */
        font-weight: bold;
    }

    .controls button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 12px 25px; /* More padding */
        border-radius: 6px; /* Slightly more rounded button */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease; /* Added box-shadow transition */
        margin-top: 15px; /* Space above button */
        font-size: 1em;
        font-weight: bold;
        flex-shrink: 0; /* Prevent button from shrinking */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* Subtle button shadow */
    }

    .controls button:hover {
        background-color: #0056b3;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Lift button on hover */
    }
     .controls button:active {
        transform: scale(0.97); /* Slightly more pronounced press effect */
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }


    #waveCanvas {
        border: 1px solid #b0bec5; /* Softer border color */
        background-color: #e3f2fd; /* Very light blue background for water effect */
        display: block; /* Remove extra space below canvas */
        width: 100%; /* Canvas takes full width of container */
        height: 450px; /* Slightly increased default height */
        border-radius: 8px; /* Match container rounded corners */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05); /* Subtle inner shadow */
    }

    button#toggleExplanation {
        display: block; /* Button on its own line */
        margin: 30px auto; /* Center the button with more margin */
        background-color: #28a745; /* Green button */
        color: white;
        border: none;
        padding: 14px 30px; /* More padding */
        border-radius: 6px; /* Match other buttons */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    button#toggleExplanation:hover {
        background-color: #218838;
         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
     button#toggleExplanation:active {
        transform: scale(0.97);
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    .explanation {
        background-color: #e9ffe9; /* Light green background */
        padding: 25px; /* More padding */
        border: 1px solid #c3e6cb; /* Green border */
        border-radius: 8px; /* Rounded corners */
        margin-top: 25px; /* More space above */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* More prominent shadow */
        direction: rtl;
        text-align: right;
        width: 100%;
        max-width: 850px; /* Match container width */
        margin-left: auto;
        margin-right: auto;
        box-sizing: border-box;
    }

    .explanation.hidden {
        display: none;
    }

    .explanation h3 {
        color: #155724; /* Dark green for subheadings */
        margin-top: 20px; /* More space above subheadings */
        margin-bottom: 12px; /* More space below subheadings */
        font-weight: 700;
        direction: rtl;
        text-align: right;
    }

    .explanation ul {
        margin-bottom: 20px; /* More space below list */
        padding-right: 25px; /* Indent list items */
    }

    .explanation li {
        margin-bottom: 10px; /* More space between list items */
        direction: rtl;
        text-align: right;
    }
    
    /* Optional: Style for source dots on canvas */
    /* Cannot style canvas content directly with CSS, handled in JS */
</style>

<script>
    const canvas = document.getElementById('waveCanvas');
    const ctx = canvas.getContext('2d');
    const distanceInput = document.getElementById('distance');
    const distanceValueSpan = document.getElementById('distanceValue');
    const wavelengthInput = document.getElementById('wavelength');
    const wavelengthValueSpan = document.getElementById('wavelengthValue');
    const phaseInput = document.getElementById('phase'); // New phase control
    const phaseValueSpan = document.getElementById('phaseValue'); // New phase value span
    const amplitudeInput = document.getElementById('amplitude'); // Amplitude input (still disabled)
    const amplitudeValueSpan = document.getElementById('amplitudeValue'); // Amplitude value span
    const resetButton = document.getElementById('resetButton');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.querySelector('.explanation');

    // Initially hide the explanation div using the class and set button text
    explanationDiv.classList.add('hidden');
    // Button text is set in HTML and updated by JS on click

    let time = 0; // Time variable for animation
    let animationFrameId; // To store the request ID for cancelling animation

    // Function to update canvas size based on its container
    const updateCanvasSize = () => {
        const container = canvas.parentElement;
        canvas.width = container.clientWidth;
        // Maintain an aspect ratio (e.g., 4:3) but clamp height to avoid excessively tall canvas on very wide screens
        canvas.height = Math.min(container.clientWidth * 0.75, 600); // Adjusted aspect ratio and max height
         // Redraw immediately after resizing to avoid empty canvas briefly
        if (!animationFrameId) { // Only draw if animation isn't running (e.g., on initial load before animate())
             drawWaves();
        }
    };

    // Update canvas size initially and whenever the window is resized
    updateCanvasSize();
    window.addEventListener('resize', updateCanvasSize);

    // Main drawing function
    const drawWaves = () => {
        // No need to clearRect if we're filling the whole canvas with the pattern
        // ctx.clearRect(0, 0, canvas.width, canvas.height);
        // Background color set by CSS, so no need to fill background here either

        const sourceDistance = parseInt(distanceInput.value);
        const wavelength = parseInt(wavelengthInput.value);
        const amplitude = parseInt(amplitudeInput.value); // Get amplitude value (should be 5)
        const phaseDegrees = parseInt(phaseInput.value); // Get phase value in degrees
        const phaseRadians = phaseDegrees * Math.PI / 180; // Convert phase to radians

        // Ensure valid wavelength and amplitude to avoid issues
        const validWavelength = Math.max(wavelength, 1);
        const validAmplitude = Math.max(amplitude, 1); // Ensure amplitude is at least 1 for normalization

        const k = 2 * Math.PI / validWavelength; // Wave number
        const waveSpeed = 40; // Arbitrary wave speed - adjust for animation speed
        const omega = k * waveSpeed; // Angular frequency

        // Source positions centered vertically on the canvas
        const source1X = canvas.width / 2 - sourceDistance / 2;
        const source2X = canvas.width / 2 + sourceDistance / 2;
        const sourceY = canvas.height / 2;

        const resolution = 1.5; // Pixels per step for calculation grid (reduced for smoother appearance)

        // Calculate and draw interference pattern pixel by pixel (or block by block)
        // Iterate through the canvas grid based on the chosen resolution
        for (let y = 0; y < canvas.height; y += resolution) {
            for (let x = 0; x < canvas.width; x += resolution) {
                // Calculate distance from each source to the current point (x, y)
                const r1 = Math.sqrt((x - source1X) ** 2 + (y - sourceY) ** 2);
                const r2 = Math.sqrt((x - source2X) ** 2 + (y - sourceY) ** 2);

                // Calculate the instantaneous displacement (amplitude) from each wave at point (x, y) at time 'time'
                // Using a sinusoidal wave model (can be cosine as well)
                // Wave from source 1: amplitude * sin(k*r1 - omega*time)
                // Wave from source 2: amplitude * sin(k*r2 - omega*time + phase_offset) - added phase offset here
                const wave1 = validAmplitude * Math.sin(k * r1 - omega * time);
                const wave2 = validAmplitude * Math.sin(k * r2 - omega * time + phaseRadians); // Apply phase offset

                // Principle of Superposition: The total displacement is the sum of individual displacements
                const superposition = wave1 + wave2;

                // Map the superposition value [-2*validAmplitude, 2*validAmplitude] to a color scale
                // Normalize the value to the range [-1, 1] for color mapping
                const colorValue = superposition / (2 * validAmplitude); // Divide by max possible amplitude (sum of individual max amps)

                // Interpolate colors: Blue (-1, destructive minimum), White (0, equilibrium), Red (1, constructive maximum)
                // This creates a dynamic visualization where constructive areas flash between blue and red,
                // and destructive areas remain near white.
                let r, g, b;
                if (colorValue < 0) {
                    // Map [-1, 0] to Blue (0,0,255) towards White (255,255,255)
                    // As colorValue goes from -1 to 0, r, g increase from 0 to 255, b stays 255
                    r = 255 + colorValue * 255; // e.g., at -1, r=0; at 0, r=255
                    g = 255 + colorValue * 255; // e.g., at -1, g=0; at 0, g=255
                    b = 255;
                } else {
                    // Map [0, 1] to White (255,255,255) towards Red (255,0,0)
                    // As colorValue goes from 0 to 1, g, b decrease from 255 to 0, r stays 255
                    r = 255;
                    g = 255 - colorValue * 255; // e.g., at 0, g=255; at 1, g=0
                    b = 255 - colorValue * 255; // e.g., at 0, b=255; at 1, b=0
                }

                // Set the fill color and draw a small rectangle (pixel)
                ctx.fillStyle = `rgb(${Math.round(r)}, ${Math.round(g)}, ${Math.round(b)})`;
                ctx.fillRect(x, y, resolution, resolution);
            }
        }
        
        // Draw sources on top of the pattern for clarity
        ctx.fillStyle = '#343a40'; // Dark color for sources
        ctx.beginPath();
        ctx.arc(source1X, sourceY, 7, 0, Math.PI * 2); // Slightly larger dots for sources
        ctx.fill();
        ctx.beginPath();
        ctx.arc(source2X, sourceY, 7, 0, Math.PI * 2);
        ctx.fill();

        // Increment time for the next frame of the animation
        // The speed of this increment controls the animation speed
        time += 0.04; // Adjusted animation speed slightly
    };

    // Animation loop function using requestAnimationFrame for smooth rendering
    const animate = () => {
        drawWaves(); // Draw the current frame
        animationFrameId = requestAnimationFrame(animate); // Request the next frame
    };

    // Event Listeners for controls: Update value displays and the animation loop will handle the changes automatically
    distanceInput.addEventListener('input', () => {
        distanceValueSpan.textContent = distanceInput.value;
        // The animate loop is running and calls drawWaves, which reads the latest input values. No need to manually call drawWaves.
    });
    wavelengthInput.addEventListener('input', () => {
        wavelengthValueSpan.textContent = wavelengthInput.value;
    });
    phaseInput.addEventListener('input', () => {
        phaseValueSpan.textContent = `${phaseInput.value}°`; // Display phase with degree symbol
    });

    // Reset Button Event Listener
    resetButton.addEventListener('click', () => {
        // Reset all control values to their defaults
        distanceInput.value = 150;
        distanceValueSpan.textContent = 150;
        wavelengthInput.value = 40;
        wavelengthValueSpan.textContent = 40;
        phaseInput.value = 0; // Reset phase
        phaseValueSpan.textContent = '0°'; // Reset phase display
        // Amplitude input is disabled, but reset its internal value just in case
        amplitudeInput.value = 5; 
        // No need to update amplitude span if input is disabled
        
        // The animate loop will pick up the new values in the next frame
    });

    // Event Listener for explanation button
    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden'); // Toggle the 'hidden' class
        const isNowHidden = explanationDiv.classList.contains('hidden'); // Check the state *after* toggling
        // Update button text based on whether the explanation is now hidden or visible
        toggleExplanationButton.textContent = isNowHidden ? 'חשיפת הסוד מאחורי התבנית: לחצו להסבר' : 'הסתרת ההסבר';
    });

    // Start the animation loop when the script loads
    animate();
</script>