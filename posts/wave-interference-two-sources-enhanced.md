---
title: "קסם הגלים: התאבכות משני מקורות"
english_slug: wave-interference-two-sources-enhanced
category: "מדעים מדויקים / פיזיקה"
tags:
  - גלים
  - התאבכות
  - סופרפוזיציה
  - פיזיקה של גלים
  - הדמיית גלים
---
# קסם הגלים: התאבכות משני מקורות

תארו לעצמכם ששני גלים נפגשים – לא ככדורים שמתנגשים, אלא כהפרעות במרחב שחולפות זו דרך זו, אך בזמן המפגש משפיעות זו על זו באופן דרמטי! התופעה המרתקת הזו נקראת התאבכות, והיא מסבירה מדוע באזורים מסוימים אנרגיית הגל מתחזקת באופן מרשים, ובאזורים אחרים היא נחלשת, ואפילו נעלמת לחלוטין! בואו נצלול פנימה ונגלה איך שני מקורות גלים פשוטים יכולים ליצור תבניות מורכבות ויפהפיות.

<div class="simulation-container">
    <div class="controls">
        <h3>שחקו עם הגלים:</h3>
        <div class="control-group">
            <label for="frequency">תדירות (Hz): <span id="freqValue">2</span></label>
            <input type="range" id="frequency" min="0.5" max="10" value="2" step="0.1">
        </div>

        <div class="control-group">
             <label for="amplitude">עוצמת מקור יחסית: <span id="ampValue">1</span></label>
             <input type="range" id="amplitude" min="0.1" max="2" value="1" step="0.1">
        </div>

        <div class="control-group">
            <label for="sourceDistance">מרחק בין מקורות: <span id="distValue">50</span> יח'</label>
            <input type="range" id="sourceDistance" min="20" max="200" value="50" step="5">
        </div>

         <div class="control-group">
            <label for="waveSpeed">מהירות התפשטות: <span id="speedValue">50</span> יח'/שניה</label>
            <input type="range" id="waveSpeed" min="20" max="150" value="50" step="5">
         </div>
        
         <div class="control-group">
            <label for="showIntensity">הצג תבנית עוצמה (במקום תנודה רגעית):</label>
            <input type="checkbox" id="showIntensity">
         </div>

         <button id="resetButton">איפוס (מרכז מקורות)</button>
    </div>
    <div class="canvas-container">
        <canvas id="waveCanvas"></canvas>
    </div>
</div>

<style>
    /* Overall layout and container styling */
    .simulation-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
        margin: 20px 0;
        padding: 20px;
        background-color: #f8f9fa; /* Light background */
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        font-family: 'Arial', sans-serif; /* Modern font */
    }

    /* Controls styling */
    .controls {
        flex: 1 1 280px; /* Adjust base width */
        background-color: #e9ecef; /* Slightly darker background */
        padding: 20px;
        border-radius: 10px;
        min-width: 250px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .controls h3 {
        margin-top: 0;
        color: #343a40; /* Darker heading color */
        text-align: center;
        margin-bottom: 20px;
    }

    .control-group {
        margin-bottom: 18px; /* Space between controls */
    }

    .controls label {
        display: block;
        margin-bottom: 8px; /* Space below label */
        font-weight: bold;
        color: #495057; /* Label color */
        font-size: 0.95em;
    }

    .controls input[type="range"] {
        width: 100%;
        /* Custom slider styling */
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #ced4da;
        outline: none;
        opacity: 0.9;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff; /* Primary color */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #ffffff;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }

     .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff; /* Primary color */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #ffffff;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }


    .controls input[type="checkbox"] {
        margin-right: 8px;
        vertical-align: middle;
        width: 18px;
        height: 18px;
        cursor: pointer;
    }

    .controls button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #6c757d; /* Secondary button color */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease;
        margin-top: 10px;
    }

    .controls button:hover {
        background-color: #5a6268;
    }

    /* Canvas container styling */
    .canvas-container {
        flex: 2 1 500px; /* Adjust base width */
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #ffffff; /* White background for canvas area */
        border: 1px solid #dee2e6; /* Light border */
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Shadow for canvas */
         position: relative; /* Needed for absolute positioning of sources if drawn outside canvas context */
    }

    #waveCanvas {
        display: block;
        background-color: #f8f9fa; /* Canvas background */
         /* Ensure canvas size is set via JS attributes, not CSS for drawing accuracy */
    }

    /* Explanation section styling */
    #explanationSection {
        display: none; /* Initially hidden */
        margin-top: 30px;
        padding: 25px;
        background-color: #e9ecef; /* Matching controls background */
        border-radius: 12px;
        border-left: 5px solid #007bff; /* Highlight border */
        line-height: 1.7; /* Improve readability */
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

     #explanationSection h2 {
        margin-top: 0;
        color: #343a40;
        margin-bottom: 15px;
     }

     #explanationSection h3 {
         color: #007bff; /* Primary color for subheadings */
         margin-top: 20px;
         margin-bottom: 10px;
     }

     #explanationSection ul {
         padding-left: 20px;
     }
      #explanationSection li {
         margin-bottom: 8px;
      }


    /* Toggle button styling */
    .toggle-explanation-button {
        display: block;
        margin: 30px auto; /* Center button and add space */
        padding: 12px 25px;
        background-color: #28a745; /* Success color */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .toggle-explanation-button:hover {
        background-color: #218838;
        transform: translateY(-1px); /* Slight lift effect */
    }
     .toggle-explanation-button:active {
        background-color: #1e7e34;
        transform: translateY(0);
     }

     /* Ensure responsiveness */
     @media (max-width: 768px) {
         .simulation-container {
             flex-direction: column;
             gap: 20px;
             padding: 15px;
         }
         .controls, .canvas-container, #explanationSection {
             flex-basis: auto; /* Allow elements to take full width */
             min-width: unset;
         }
     }

</style>

<button class="toggle-explanation-button" id="toggleExplanation">הצג לי את הקסם שבפנים!</button>

<div id="explanationSection">
    <h2>הצצה אל מאחורי הקלעים של התאבכות גלים</h2>

    הסימולציה שזה עתה חוויתם מציגה תופעה יסודית בפיזיקה: התאבכות גלים. כדי להבין אותה לעומק, נפרק את המרכיבים:

    <h3>מהו בעצם גל?</h3>
    גל הוא דרך להעביר אנרגיה דרך תווך (כמו מים או אוויר) או אפילו דרך ריק (כמו גלי אור), מבלי להזיז את התווך עצמו למרחק גדול. חשבו על אצטדיון כדורגל בזמן "גל" - האוהדים קמים ומתיישבים, אבל לא זזים מהכיסא! לגלים יש מאפיינים חשובים:
    <ul>
        <li>**תדירות (f):** כמה מחזורים של הגל עוברים בנקודה מסוימת בשניה (נמדד בהרץ - Hz). ככל שהתדירות גבוהה יותר, הגל "צפוף" יותר בזמן.</li>
        <li>**אורך גל (λ):** המרחק הפיזי בין שתי נקודות זהות בגל (למשל, בין שני שיאים עוקבים). ככל שהאורך גל קצר יותר, הגל "צפוף" יותר במרחב.</li>
        <li>**משרעת (A):** "גובה" הגל, או הגודל המרבי של ההפרעה ממצב שיווי המשקל. קשורה ישירות לכמות האנרגיה שהגל נושא, ובעצם - לעוצמתו!</li>
        <li>**מהירות התפשטות (v):** כמה מהר הגל מתקדם במרחב. הקשר האלגנטי בין מאפיינים אלו הוא: \(v = f \cdot \lambda\).</li>
    </ul>
    בסימולציה זו אנו מדמים גלים דו-ממדיים (כמו גלים על פני מים), היוצאים מנקודות - אלו יכולות להיות מקורות אור קוהרנטיים, רמקולים, או אבנים שנזרקו למים.

    <h3>סופרפוזיציה: הגלים פשוט מסתכמים!</h3>
    כאשר שני גלים או יותר מגיעים לאותה נקודה בו זמנית, הם לא "מתנגשים" ומשנים זה את זה לצמיתות. במקום זאת, ההפרעה הכוללת באותה נקודה היא פשוט **סכום ההפרעות** שיוצר כל גל בנפרד. זהו עקרון הסופרפוזיציה. זה כאילו שכל גל מגיע לנקודה בלי "לשים לב" לגלים האחרים, אבל התוצאה שאנו רואים היא ההשפעה המשולבת שלהם.

    <h3>התאבכות בונה: כששיא פוגש שיא</h3>
    התאבכות בונה מתרחשת בנקודות שבהן שני הגלים מגיעים ב"תיאום" - כלומר, שיא של גל אחד נפגש עם שיא של גל אחר, ושפל פוגש שפל. במצב זה, ההפרעות של שני הגלים **מתחברות ומחזקות** זו את זו, ומשרעת הגל הכולל גדולה ממשרעת כל גל בנפרד. זה קורה כאשר הפרש הדרכים מהמקורות לנקודה הוא כפולה שלמה של אורך הגל (\(\Delta r = n \cdot \lambda\)), כאשר \(n\) הוא 0, 1, 2, וכן הלאה. נקודות אלו יהיו "בהירות" או "רועשות" יותר, או יציגו תנודה מקסימלית בסימולציה.

    <h3>התאבכות הורסת: כששיא פוגש שפל</h3>
    התאבכות הורסת מתרחשת בנקודות שבהן שני הגלים מגיעים ב"סתירה" - כלומר, שיא של גל אחד פוגש שפל של גל אחר. במצב זה, ההפרעות של שני הגלים **מבטלות** זו את זו (לפחות חלקית). אם המשרעות שוות, הביטול יכול להיות מלא לגמרי! זה קורה כאשר הפרש הדרכים מהמקורות לנקודה הוא כפולה אי-שלמה של חצי אורך גל (\(\Delta r = (n + \frac{1}{2}) \cdot \lambda\)), כאשר \(n\) הוא 0, 1, 2, וכן הלאה. נקודות אלו יהיו "חשובות" או "שקטות" יותר, או יציגו תנודה מינימלית (אפסית) בסימולציה.

    <h3>תבנית ההתאבכות</h3>
    השילוב של התאבכות בונה והורסת בנקודות שונות במרחב יוצר את תבנית ההתאבכות האופיינית - אזורים לסירוגין של חיזוק והחלשה, הנראים בסימולציה כקווים או פסים. תבנית זו תלויה במרחק בין המקורות, בתדירות הגלים (ומכאן באורך הגל), ומהירות התפשטותם. ככל שהפרש הדרכים משתנה מנקודה לנקודה ביחס לאורך הגל, כך אנו עוברים מאזור התאבכות בונה להורסת ובחזרה.

    <h3>התאבכות ביום-יום</h3>
    תופעת ההתאבכות אינה רק תרגיל פיזיקלי, אלא מופיעה סביבנו כל הזמן:
    <ul>
        <li>**גלי מים:** תבניות הריפלס המורכבות שנוצרות בבריכה או אגם כשיש שני מקורות הפרעה.</li>
        <li>**גלי קול:** אזורים שונים בחדר שבהם שומעים צליל חזק יותר או חלש יותר ממערכת סטריאו (נקודות "חמות" ו"קרות" אקוסטיות). טכנולוגיית ביטול רעשים באוזניות עושה שימוש בהתאבכות הורסת ליצירת "אנטי-רעש".</li>
        <li>**גלי אור:** הצבעים המרהיבים על בועות סבון או כתמי שמן על כביש רטוב - נובעים מהתאבכות אור המוחזר ממשטחים שונים בשכבה הדקה. ניסוי שני הסדקים המפורסם של יאנג, שהראה את האופי הגלי של האור, מבוסס על התאבכות. טכנולוגיות כמו הולוגרפיה אף הן רותמות את התאבכות האור.</li>
    </ul>
    שחקו שוב בסימולציה, ונסו לראות כיצד שינוי הפרמטרים משפיע על תבנית ההתאבכות. האם אתם מזהים את הקשרים שלמדנו עליהם?

</div>

<script>
    const canvas = document.getElementById('waveCanvas');
    const ctx = canvas.getContext('2d');

    // Control elements
    const frequencyControl = document.getElementById('frequency');
    const amplitudeControl = document.getElementById('amplitude');
    const sourceDistanceControl = document.getElementById('sourceDistance');
    const waveSpeedControl = document.getElementById('waveSpeed');
    const showIntensityControl = document.getElementById('showIntensity');
    const resetButton = document.getElementById('resetButton');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationSection = document.getElementById('explanationSection');

    // Value display spans
    const freqValueSpan = document.getElementById('freqValue');
    const ampValueSpan = document.getElementById('ampValue');
    const distValueSpan = document.getElementById('distValue');
    const speedValueSpan = document.getElementById('speedValue');

    let animationFrameId = null;
    let time = 0;
    let simulationRunning = false;

    // Simulation parameters (adjusted by controls)
    let frequency = parseFloat(frequencyControl.value);
    let amplitude = parseFloat(amplitudeControl.value);
    let sourceDistance = parseInt(sourceDistanceControl.value, 10); // Distance between sources
    let waveSpeed = parseInt(waveSpeedControl.value, 10); // Wave speed
    let showIntensity = showIntensityControl.checked;

    // Canvas setup
    const canvasWidth = 600; // Keep fixed for drawing logic
    const canvasHeight = 400; // Keep fixed for drawing logic
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    // Source positions relative to canvas center
    // These are fixed in X dimension for simplicity, can be dragged later
    let source1 = { x: canvasWidth / 2 - sourceDistance / 2, y: canvasHeight / 2 };
    let source2 = { x: canvasWidth / 2 + sourceDistance / 2, y: canvasHeight / 2 };

    // Source visual properties for animation (optional)
    const sourceRadius = 6;
    const sourceColor = 'rgba(255, 0, 0, 0.8)'; // Red with transparency

    // Store pixel data to draw efficiently
    let pixelData = ctx.createImageData(canvasWidth, canvasHeight);
    let data = pixelData.data;

    // Function to get distance between two points
    function getDistance(p1, p2) {
        const dx = p1.x - p2.x;
        const dy = p1.y - p2.y;
        return Math.sqrt(dx * dx + dy * dy);
    }

     // Function to calculate instantaneous wave displacement at a point from a source
     // Includes amplitude decrease with distance (simplified 1/sqrt(r) for 2D-like spread)
    function getWaveDisplacement(distance, freq, amp, speed, t) {
        if (distance < 0.1) distance = 0.1; // Avoid issues near source
        const wavelength = speed / freq; // λ = v / f
        // Wave function: A * sin(k*r - ω*t + initial_phase)
        // Assuming initial_phase is 0 for both sources
        // k*r = (2π/λ) * r
        // ω*t = 2πf * t
        const phase = 2 * Math.PI * ((distance / wavelength) - (freq * t));
        // Amplitude decay: A_effective = amp / sqrt(distance)
        const effectiveAmplitude = amp / Math.sqrt(distance);
        return effectiveAmplitude * Math.sin(phase);
    }

    // Helper function to map a value within a range to a color gradient
    // For displacement: value from -maxDisp to +maxDisp -> color (e.g., Blue-Gray-Red)
    // For intensity: value from 0 to maxAmp -> color (e.g., Black-Yellow)
    function mapValueToColor(value, minVal, maxVal, colors) {
         // Clamp value to range
         value = Math.max(minVal, Math.min(maxVal, value));

         // Normalize value to [0, 1] range based on min/max
         const normalized = (value - minVal) / (maxVal - minVal);

         // Map normalized value to color index
         const colorIndex = normalized * (colors.length - 1);
         const index1 = Math.floor(colorIndex);
         const index2 = Math.ceil(colorIndex);
         const fraction = colorIndex - index1;

         const c1 = colors[index1];
         const c2 = colors[index2];

         // Interpolate between the two nearest colors
         const r = Math.round(c1[0] + fraction * (c2[0] - c1[0]));
         const g = Math.round(c1[1] + fraction * (c2[1] - c1[1]));
         const b = Math.round(c1[2] + fraction * (c2[2] - c1[2]));

         return [r, g, b];
    }


    // Draw function
    function draw() {
         // Estimate a reasonable maximum displacement/amplitude for color mapping
         // This helps scale the color gradient.
         // Max possible total amplitude is sum of amplitudes from both sources.
         // Near sources, decay is minimal. Furthest points have max decay.
         // Let's scale relative to the maximum possible setting of the amplitude control,
         // considering points near the sources.
         const minPossibleDistance = Math.min(getDistance({x:0, y:0}, source1), getDistance({x:0, y:0}, source2),
                                              getDistance({x:canvasWidth, y:0}, source1), getDistance({x:canvasWidth, y:0}, source2),
                                              getDistance({x:0, y:canvasHeight}, source1), getDistance({x:0, y:canvasHeight}, source2),
                                              getDistance({x:canvasWidth, y:canvasHeight}, source1), getDistance({x:canvasWidth, y:canvasHeight}, source2));

         const baseMaxAmp = parseFloat(amplitudeControl.max); // Use max possible input amplitude value for scaling
         const estimatedMaxAmp = 2 * baseMaxAmp / Math.sqrt(Math.max(minPossibleDistance, 10)); // Estimate sum of amplitudes near edges, avoid too large values


        // Define color palettes
        const displacementColors = [
            [0, 0, 255],    // Deep Blue (min displacement)
            [128, 128, 128], // Gray (zero displacement)
            [255, 0, 0]     // Bright Red (max displacement)
        ];
        const intensityColors = [
             [0, 0, 0],       // Black (min intensity / destructive)
            // [0, 0, 255],    // Blueish (low intensity)
            // [0, 255, 0],    // Greenish (medium intensity)
             [255, 255, 0]   // Yellow (max intensity / constructive)
        ];


        for (let y = 0; y < canvasHeight; y++) {
            for (let x = 0; x < canvasWidth; x++) {
                const point = { x: x, y: y };
                const d1 = getDistance(point, source1);
                const d2 = getDistance(point, source2);

                let r, g, b;

                if (showIntensity) {
                     // Calculate the resulting amplitude at this point based on path difference
                     const wavelength = waveSpeed / frequency;
                     const pathDifference = Math.abs(d1 - d2);

                     // Calculate local amplitudes with decay
                     const localAmp1 = amplitude / Math.sqrt(d1 < 0.1 ? 0.1 : d1);
                     const localAmp2 = amplitude / Math.sqrt(d2 < 0.1 ? 0.1 : d2);

                     // The phase difference between the two waves arriving at (x,y) is 2π * |d1 - d2| / λ
                     // Assuming sources are in phase initially.
                     const phaseDiff = 2 * Math.PI * pathDifference / wavelength;

                     // Resulting amplitude formula for two waves A1, A2 with phase difference phi:
                     // A_res = sqrt(A1^2 + A2^2 + 2*A1*A2*cos(phi))
                     const resultingAmplitude = Math.sqrt(localAmp1*localAmp1 + localAmp2*localAmp2 + 2*localAmp1*localAmp2*Math.cos(phaseDiff));

                     // Map resulting amplitude to color (intensity map)
                     const color = mapValueToColor(resultingAmplitude, 0, estimatedMaxAmp, intensityColors);
                     [r, g, b] = color;

                } else {
                    // Show instantaneous total displacement
                    const displacement1 = getWaveDisplacement(d1, frequency, amplitude, waveSpeed, time);
                    const displacement2 = getWaveDisplacement(d2, frequency, amplitude, waveSpeed, time);
                    const totalDisplacement = displacement1 + displacement2;

                    // Map total displacement to color (displacement map)
                    const color = mapValueToColor(totalDisplacement, -estimatedMaxAmp, estimatedMaxAmp, displacementColors);
                    [r, g, b] = color;
                }


                const index = (y * canvasWidth + x) * 4;
                data[index + 0] = r; // Red
                data[index + 1] = g; // Green
                data[index + 2] = b; // Blue
                data[index + 3] = 255; // Alpha (opaque)
            }
        }

        ctx.putImageData(pixelData, 0, 0);

         // Draw source points *on top* of the pixel data
         // Animate source appearance based on the displacement *at the source location itself* (conceptual visual aid)
         // Note: The displacement function assumes distance > 0. Using a tiny distance or skipping calculation at source is needed.
         // Let's use a simplified visual pulse for the sources.
         const sourcePulseValue = Math.sin(2 * Math.PI * frequency * time); // Oscillates between -1 and 1

         // Draw source 1
         ctx.fillStyle = sourceColor;
         ctx.beginPath();
         // Scale radius slightly based on pulse value (e.g., 5 to 7 pixels)
         const r1 = sourceRadius + sourcePulseValue * 1.5;
         ctx.arc(source1.x, source1.y, r1, 0, Math.PI * 2);
         ctx.fill();
         // Draw a ring or border
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.arc(source1.x, source1.y, sourceRadius + 2, 0, Math.PI * 2);
          ctx.stroke();


         // Draw source 2
         ctx.fillStyle = sourceColor;
         ctx.beginPath();
         const r2 = sourceRadius + sourcePulseValue * 1.5;
         ctx.arc(source2.x, source2.y, r2, 0, Math.PI * 2);
         ctx.fill();
         // Draw a ring or border
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.arc(source2.x, source2.y, sourceRadius + 2, 0, Math.PI * 2);
          ctx.stroke();
    }

    // Animation loop
    function animate() {
        if (!simulationRunning) return;
        time += 1/60; // Increment time based on typical frame rate (approx 60fps)
        draw();
        animationFrameId = requestAnimationFrame(animate);
    }

    // Start/Stop simulation
    function startSimulation() {
        if (!simulationRunning) {
            simulationRunning = true;
            //time = 0; // Optionally reset time on start/change? Keep continuous time for smoother transitions
            animate();
        }
    }

    function stopSimulation() {
        if (simulationRunning) {
            simulationRunning = false;
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
    }

    // Update simulation parameters from controls
    function updateParameters() {
        // Read values first
        const newFrequency = parseFloat(frequencyControl.value);
        const newAmplitude = parseFloat(amplitudeControl.value);
        const newSourceDistance = parseInt(sourceDistanceControl.value, 10);
        const newWaveSpeed = parseInt(waveSpeedControl.value, 10);
        const newShowIntensity = showIntensityControl.checked;

        // Check if parameters actually changed before updating and potentially stopping/starting
        const paramsChanged = (frequency !== newFrequency ||
                               amplitude !== newAmplitude ||
                               sourceDistance !== newSourceDistance ||
                               waveSpeed !== newWaveSpeed ||
                               showIntensity !== newShowIntensity);


        if (paramsChanged) {
            // Update values
            frequency = newFrequency;
            amplitude = newAmplitude;
            sourceDistance = newSourceDistance;
            waveSpeed = newWaveSpeed;
            showIntensity = newShowIntensity;

             // Update display values
            freqValueSpan.textContent = frequency.toFixed(1);
            ampValueSpan.textContent = amplitude.toFixed(1);
            distValueSpan.textContent = sourceDistance;
            speedValueSpan.textContent = waveSpeed;

            // Update source positions if distance changed
            source1.x = canvasWidth / 2 - sourceDistance / 2;
            source2.x = canvasWidth / 2 + sourceDistance / 2;

            // Manage animation based on view mode
            if (showIntensity) {
                // Intensity map is static pattern, stop animation and draw once
                stopSimulation();
                draw();
            } else {
                // Wave displacement map is dynamic, ensure animation is running
                startSimulation();
            }
        } else if (!simulationRunning && !showIntensity) {
             // If parameters didn't change, but we are in displacement mode and simulation stopped (e.g., page load)
             startSimulation();
        }
    }

    // Event Listeners for controls - use 'input' for continuous updates on range sliders
    frequencyControl.addEventListener('input', updateParameters);
    amplitudeControl.addEventListener('input', updateParameters);
    sourceDistanceControl.addEventListener('input', updateParameters);
    waveSpeedControl.addEventListener('input', updateParameters);
    // Use 'change' for checkbox as it's not continuous
    showIntensityControl.addEventListener('change', updateParameters);


    // Event listener for reset button
    resetButton.addEventListener('click', () => {
         // Reset sources to center with current distance (already centered by updateParameters)
         // This button just triggers an update/redraw cycle
         updateParameters(); // Re-center (which is already the case) and redraw
    });


    // Toggle explanation section
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר את ההסבר' : 'הצג לי את הקסם שבפנים!';
        // Optional: scroll to the explanation section when shown
        if (isHidden) {
            explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });


    // Initial drawing and start simulation
    // Use a small timeout to ensure canvas is fully rendered before drawing
    // This can sometimes prevent issues on page load.
     setTimeout(updateParameters, 50);


    // Handle window resize - important for keeping canvas aspect ratio/centering if container changes size
    // However, our canvas size is fixed, so we only need to potentially re-center sources if we added drag.
    // With fixed canvas size, no resize handling is strictly necessary for THIS simulation.
    // If canvas size became responsive, this would be crucial.
    // window.addEventListener('resize', updateParameters);


</script>
```