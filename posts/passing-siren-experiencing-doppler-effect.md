---
title: "צפירה חולפת: חווים את אפקט דופלר"
english_slug: passing-siren-experiencing-doppler-effect
category: "פיזיקה"
tags: [פיזיקה, גלים, אפקט דופלר, תדר, צליל, סימולציה]
---
# צפירה חולפת: חווים את אפקט דופלר

הקשיבו לרגע... שמעתם פעם צפירה של אמבולנס או מכונית משטרה חולפת על פניכם? יש משהו מוזר באופן שבו גובה הצליל (התדר) של הצפירה משתנה בדיוק ברגע שהרכב עובר אתכם. הצליל נשמע גבוה יותר כשהרכב מתקרב, ונמוך יותר כשהוא מתרחק. למה זה קורה? התופעה המרתקת הזו היא דוגמה יומיומית ומוחשית לאחד העקרונות היפים בפיזיקה: **אפקט דופלר**.

בואו נחקור את התופעה הזו באמצעות סימולציה אינטראקטיבית. אתם מוזמנים לשחק עם המהירות ולראות (ולשמוע!) איך התנועה משפיעה על הגלים ועל הצליל שאנחנו קולטים.

<div id="doppler-app">
    <canvas id="dopplerCanvas"></canvas>
    <div class="controls">
        <label for="speedSlider">מהירות הרכב:</label>
        <input type="range" id="speedSlider" min="0" max="100" value="50" step="1">
        <span id="currentSpeed">50 מ' / שנ'</span>
        <button id="startButton">התחל סימולציה</button>
        <button id="pauseButton" disabled>השהה</button>
        <button id="resetButton">אתחל</button>
    </div>
    <div class="info">
        <p>תדר נצפה: <span id="observedFrequency">--</span> הרץ</p>
        <p>צופה: <span id="observer-label"></span></p>
        <p class="simulation-note">הסימולציה מציגה מבט ממעוף הציפור. הקווים הכחולים הם חזיתות הגל. הצופה ממוקם בנקודה הלבנה.</p>
         <div id="sound-warning" style="display:none; color: orange; font-weight: bold;">ייתכן שאין תמיכה מלאה באודיו בחלק מהדפדפנים או המכשירים.</div>
    </div>
</div>

<style>
    /* General container styling */
    #doppler-app {
        width: 100%;
        max-width: 800px;
        margin: 20px auto;
        border: 1px solid #d3dce6; /* Softer border */
        border-radius: 12px; /* More rounded corners */
        overflow: hidden;
        background-color: #f8fafd; /* Very light blue background */
        direction: rtl; /* RTL layout */
        text-align: right;
        font-family: 'Arial', sans-serif; /* Standard clear font */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    /* Canvas styling */
    #dopplerCanvas {
        display: block;
        width: 100%;
        height: 400px; /* Fixed height for consistency */
        background: linear-gradient(to bottom, #a8d0f7 0%, #e0f0ff 100%); /* Sky gradient */
    }

    /* Controls and Info sections */
    .controls, .info {
        padding: 15px 20px; /* More padding */
        background-color: #ffffff;
        border-top: 1px solid #d3dce6;
        display: flex;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 10px 15px; /* Spacing between items */
        font-size: 0.95em;
    }

    /* Control elements */
    .controls label {
        font-weight: bold;
        color: #333;
        margin-left: 5px; /* Adjust margin for RTL */
        white-space: nowrap; /* Prevent label wrapping */
    }

    .controls input[type="range"] {
        flex-grow: 1;
        margin-right: 10px; /* Adjust margin for RTL */
        -webkit-appearance: none; /* Override default style */
        appearance: none;
        height: 8px;
        background: #e0e0e0;
        border-radius: 5px;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: #007bff;
        border-radius: 50%;
        cursor: pointer;
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: #007bff;
        border-radius: 50%;
        cursor: pointer;
    }

    .controls span {
        min-width: 80px; /* Fixed width for speed display */
        text-align: left; /* Align value left */
        color: #007bff;
        font-weight: bold;
    }


    .controls button {
        padding: 8px 18px; /* More padding */
        border: none;
        border-radius: 5px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease, opacity 0.2s ease;
        white-space: nowrap;
    }

    .controls button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }

    .controls button#startButton { background-color: #28a745; color: white; }
    .controls button#startButton:hover:not(:disabled) { background-color: #218838; }

    .controls button#pauseButton { background-color: #ffc107; color: #333; }
    .controls button#pauseButton:hover:not(:disabled) { background-color: #e0a800; }

    .controls button#resetButton { background-color: #6c757d; color: white; } /* Muted grey */
    .controls button#resetButton:hover:not(:disabled) { background-color: #5a6268; }

    /* Info section styling */
    .info {
        font-size: 0.9em;
        color: #555;
        justify-content: space-between; /* Distribute items */
    }

    .info p {
        margin: 0; /* Remove default margin */
    }

    .info span {
        font-weight: bold;
        color: #000;
    }
     .info span#observedFrequency {
        color: #007bff; /* Highlight frequency */
     }

     .simulation-note {
        font-size: 0.85em;
        color: #777;
        margin-top: 10px;
        width: 100%; /* Take full width */
     }


    /* Explanation button */
    #explanation-button {
        display: block;
        width: fit-content;
        margin: 20px auto;
        padding: 12px 25px; /* More padding */
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        background-color: #007bff; /* Primary blue */
        color: white;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.2s ease;
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.2); /* Subtle shadow */
    }
    #explanation-button:hover {
         background-color: #0056b3;
    }

    /* Explanation section */
    #doppler-explanation {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #d3dce6;
        border-radius: 12px;
        background-color: #f8fafd;
        display: none; /* Initially hidden */
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }
    #doppler-explanation h2 {
        color: #0056b3; /* Darker blue */
        border-bottom: 2px solid #007bff; /* Primary blue underline */
        padding-bottom: 8px; /* More space below heading */
        margin-bottom: 20px; /* More space after heading */
        font-size: 1.5em;
    }
    #doppler-explanation p {
        margin-bottom: 15px; /* More space between paragraphs */
        line-height: 1.7; /* Improved readability */
        color: #333;
    }
    #doppler-explanation ul {
        margin-bottom: 15px;
        padding-right: 25px; /* Adjust padding for RTL list */
        color: #333;
    }
    #doppler-explanation li {
        margin-bottom: 8px; /* More space between list items */
        line-height: 1.6;
    }
    #doppler-explanation strong {
        color: #007bff; /* Highlight key terms */
    }
</style>

<button id="explanation-button">רוצה להבין לעומק? הצג הסבר מלא על אפקט דופלר</button>

<div id="doppler-explanation">
    <h2>אפקט דופלר בפשטות: תדר שמשתנה עם התנועה</h2>
    <p>דמיינו רכבת שצופרת כשהיא מתקרבת אליכם, חולפת, ומתרחקת. צליל הצפירה נשמע גבוה יותר כשהרכבת מתקרבת, ומייד יורד לצליל נמוך יותר כשהיא חולפת. זהו אפקט דופלר בפעולה!</p>

    <p>**אז מה קורה בעצם?**</p>
    <p>גלי קול, כמו כל גל אחר, מתפשטים במרחב. כשלמקור הצליל (כמו הסירנה של הרכב בסימולציה) יש מהירות ביחס לצופה, הגלים שהוא פולט "נערמים" או "נמתחים":</p>
    <ul>
        <li>**כשהמקור מתקרב:** כל גל חדש נפלט מנקודה קרובה יותר אליכם מאשר הגל הקודם. זה גורם לחזיתות הגל להידחס יחד בכיוון התנועה. אתם קולטים את הגלים בצפיפות גבוהה יותר - כאילו הם מגיעים מהר יותר - מה שמתפרש כתדר גבוה יותר (צליל גבוה).</li>
        <li>**כשהמקור מתרחק:** כל גל חדש נפלט מנקודה רחוקה יותר אליכם מאשר הגל הקודם. זה גורם לחזיתות הגל "להימתח" ולהתרחק זו מזו בכיוון ההפוך לתנועה. אתם קולטים את הגלים בצפיפות נמוכה יותר - הם מגיעים לאט יותר - מה שמתפרש כתדר נמוך יותר (צליל נמוך).</li>
        <li>**כשהמקור נייח (או נע בניצב אליכם):** הגלים מתפשטים באופן אחיד לכל הכיוונים, ואתם קולטים אותם בדיוק בתדר שבו הם נפלטים. בסימולציה, כשהרכב בדיוק עובר מול הצופה, הרכיב הרדיאלי של המהירות הוא אפס, ולרגע קצר התדר הנצפה זהה לתדר המקור.</li>
    </ul>

    <p>השינוי בתדר תלוי גם במהירות הרכב וגם במהירות התפשטות הגל במתווך (מהירות הקול באוויר). ככל שהרכב מהיר יותר, השינוי בתדר יהיה דרמטי יותר.</p>

    <h2>אפקט דופלר הוא לא רק צליל!</h2>
    <p>העיקרון הזה חל על כל סוגי הגלים, לא רק קול:</p>
    <ul>
        <li>**רדאר משטרתי:** משתמש באפקט דופלר כדי למדוד את מהירות המכוניות באמצעות גלי רדיו.</li>
        <li>**אולטרסאונד רפואי (דופלר):** מאפשר לרופאים לראות ולמדוד את זרימת הדם בגוף.</li>
        <li>**אסטרונומיה:** האור מהכוכבים והגלקסיות מושפע גם הוא. אם גלקסיה מתרחקת מאיתנו במהירות, האור שלה "נמתח" לכיוון האדום בספקטרום (הסחה לאדום). אם היא מתקרבת, האור "נדחס" לכיוון הכחול (הסחה לכחול). זה אחד הכלים המרכזיים להבנת התפשטות היקום!</li>
    </ul>
    <p>אז בפעם הבאה שתשמעו סירנה חולפת, תזכרו שאתם עדים לתופעה פיזיקלית בסיסית ואלגנטית שמלווה אותנו בחיי היומיום ועד לקצוות היקום.</p>
</div>

<script>
    const canvas = document.getElementById('dopplerCanvas');
    const ctx = canvas.getContext('2d');
    const speedSlider = document.getElementById('speedSlider');
    const currentSpeedSpan = document.getElementById('currentSpeed');
    const observedFrequencySpan = document.getElementById('observedFrequency');
    const startButton = document.getElementById('startButton');
    const pauseButton = document.getElementById('pauseButton');
    const resetButton = document.getElementById('resetButton');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('doppler-explanation');
    const observerLabelSpan = document.getElementById('observer-label');
    const soundWarningDiv = document.getElementById('sound-warning');

    let animationFrameId;
    let running = false;
    let lastTime = 0;
    const timeScale = 0.04; // Controls the speed of simulation time relative to real time (tuned for visual flow)
    let simulationTime = 0; // Time elapsed in the simulation

    // Constants (using realistic values and scaling for display)
    const CANVAS_WIDTH = 800;
    const CANVAS_HEIGHT = 400;
    const SOUND_SPEED = 343; // Speed of sound in air (m/s)
    const SOURCE_FREQUENCY = 440; // Base frequency of the siren (Hz)
    const WAVE_INTERVAL = 1 / SOURCE_FREQUENCY; // Time between wave emissions (in real-world time)

    // Simulation scaling: Let 1 pixel = 1 meter
    const SCALE = 1; // Pixels per meter
    const scaledSoundSpeed = SOUND_SPEED * SCALE;
    let scaledCarSpeed = parseFloat(speedSlider.value) * SCALE; // Current car speed in px/s

    // Position constants (scaled to canvas coordinates)
    const OBSERVER_X = CANVAS_WIDTH / 2; // Observer is horizontally centered
    const OBSERVER_Y = CANVAS_HEIGHT * 0.75; // Observer is below the car's path
    const CAR_START_X = -CANVAS_WIDTH * 0.6; // Car starts well off-screen left
    const CAR_END_X = CANVAS_WIDTH * 1.6; // Car ends well off-screen right
    const CAR_Y = CANVAS_HEIGHT * 0.25; // Car moves along this Y coordinate
    const CAR_SIZE = 25; // px
    const CAR_COLOR = '#dc3545'; // Red
    const WAVE_COLOR = 'rgba(0, 123, 255, 0.6)'; // Semi-transparent blue
    const OBSERVER_COLOR = '#ffffff'; // White
    const OBSERVER_BORDER_COLOR = '#000000'; // Black
    const PATH_COLOR = '#555'; // Grey for path

    let carX = CAR_START_X; // Current car position (px)
    let waves = []; // Array to store wave objects { x, y, emissionTime }

    // Web Audio API for sound
    let audioContext = null;
    let oscillator = null;
    let gainNode = null;
    let soundInitialized = false;

    function initializeAudio() {
        try {
            // Attempt to create AudioContext only after user interaction
             audioContext = new (window.AudioContext || window.webkitAudioContext)();
             oscillator = audioContext.createOscillator();
             gainNode = audioContext.createGain();

             oscillator.type = 'sine'; // Simple sine wave for siren sound
             oscillator.frequency.setValueAtTime(SOURCE_FREQUENCY, audioContext.currentTime); // Start at base frequency
             oscillator.connect(gainNode);
             gainNode.connect(audioContext.destination);
             gainNode.gain.setValueAtTime(0, audioContext.currentTime); // Start silent

             oscillator.start();
             soundInitialized = true;
             soundWarningDiv.style.display = 'none'; // Hide warning if successful
             console.log("Audio initialized.");

        } catch (e) {
            soundInitialized = false;
             console.error("Web Audio API is not supported in this browser:", e);
             soundWarningDiv.style.display = 'block'; // Show warning
        }
    }

    function startSound() {
        if (soundInitialized && audioContext && gainNode) {
            // Fade in sound
             gainNode.gain.cancelScheduledValues(audioContext.currentTime);
             gainNode.gain.setValueAtTime(gainNode.gain.value, audioContext.currentTime); // Keep current value
             gainNode.gain.linearRampToValueAtTime(0.5, audioContext.currentTime + 0.1); // Fade up to volume 0.5 over 0.1s
             if (audioContext.state === 'suspended') {
                audioContext.resume(); // Resume if context was suspended
             }
        }
    }

    function stopSound() {
         if (soundInitialized && audioContext && gainNode) {
            // Fade out sound
            gainNode.gain.cancelScheduledValues(audioContext.currentTime);
            gainNode.gain.setValueAtTime(gainNode.gain.value, audioContext.currentTime); // Keep current value
            gainNode.gain.linearRampToValueAtTime(0, audioContext.currentTime + 0.2); // Fade down to 0 over 0.2s
             // Keep oscillator running but silent, ready for next start
        }
    }

    function setSoundFrequency(freq) {
        if (soundInitialized && oscillator && audioContext) {
             // Use A-rate parameter for smooth frequency changes
             oscillator.frequency.setValueAtTime(freq, audioContext.currentTime);
             // Alternative: exponentialRampToValueAtTime for smoother transitions, maybe not needed here
             // oscillator.frequency.exponentialRampToValueAtTime(freq, audioContext.currentTime + 0.05);
        }
    }


    function initializeSimulation() {
        carX = CAR_START_X;
        scaledCarSpeed = parseFloat(speedSlider.value) * SCALE;
        waves = [];
        simulationTime = 0;
        observedFrequencySpan.textContent = '--';
        observerLabelSpan.textContent = 'אתה/את כאן'; // Set observer label
        draw(); // Initial draw
        stopSound(); // Ensure sound is off on reset
    }

    function draw() {
        // Resize canvas (optional for responsiveness, but ensures correct size)
        canvas.width = CANVAS_WIDTH;
        canvas.height = CANVAS_HEIGHT;

        // Draw background gradient
        const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
        gradient.addColorStop(0, '#a8d0f7'); // Sky color
        gradient.addColorStop(1, '#e0f0ff'); // Lighter sky/ground blend
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw ground line
        ctx.strokeStyle = PATH_COLOR;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, CAR_Y + CAR_SIZE/2 + 10);
        ctx.lineTo(canvas.width, CAR_Y + CAR_SIZE/2 + 10);
        ctx.stroke();

         // Draw observer (caricature dot)
        ctx.fillStyle = OBSERVER_COLOR;
        ctx.strokeStyle = OBSERVER_BORDER_COLOR;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(OBSERVER_X, OBSERVER_Y, 10, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Draw car (simple rectangle for now)
        ctx.fillStyle = CAR_COLOR;
        ctx.fillRect(carX - CAR_SIZE / 2, CAR_Y - CAR_SIZE / 2, CAR_SIZE, CAR_SIZE);

        // Draw waves
        ctx.strokeStyle = WAVE_COLOR;
        ctx.lineWidth = 2; // Thicker waves

        // Draw waves in reverse order so inner, newer waves are on top
        for (let i = waves.length - 1; i >= 0; i--) {
             const wave = waves[i];
             const radius = scaledSoundSpeed * (simulationTime - wave.emissionTime);

             // Only draw if radius is positive and within reasonable bounds
             if (radius > 0 && radius < Math.max(canvas.width, canvas.height) * 2) {
                 ctx.beginPath();
                 // Center the circle at the car's position *when the wave was emitted*
                 ctx.arc(wave.x, wave.y, radius, 0, Math.PI * 2);
                 ctx.stroke();
             }
        }
    }

    function update(deltaTime) {
        if (!running) return;

        // Convert real deltaTime to simulation deltaTime
        const simDeltaTime = deltaTime * timeScale;
        simulationTime += simDeltaTime;

        // Update car position
        carX += scaledCarSpeed * simDeltaTime;

        // Emit new wave if enough simulation time has passed since the last emission
        // Time between emissions in simulation time: WAVE_INTERVAL * timeScale? No, it should be scaled by speed.
        // Time between emissions in real world: WAVE_INTERVAL = 1/SOURCE_FREQUENCY.
        // In simulation, this time passes scaled: WAVE_INTERVAL / timeScale.
        // Let's emit a wave every X seconds of simulation time, where X corresponds to 1/SOURCE_FREQUENCY in real time
        const simWaveInterval = WAVE_INTERVAL / timeScale; // This seems correct based on previous logic

        if (waves.length === 0 || simulationTime - waves[waves.length - 1].emissionTime >= simWaveInterval) {
             // Add the new wave at the car's CURRENT position at the emission moment
             waves.push({ x: carX, y: CAR_Y, emissionTime: simulationTime });
        }

        // Remove old waves that are off-screen or too large
        waves = waves.filter(wave => {
            const radius = scaledSoundSpeed * (simulationTime - wave.emissionTime);
            // A wave is off-screen if its bounding box is outside the canvas.
            // For a circle centered at (wave.x, wave.y) with radius, its bounds are
            // (wave.x - radius, wave.y - radius) to (wave.x + radius, wave.y + radius).
            // Keep wave if right bound > 0 AND left bound < width AND bottom bound > 0 AND top bound < height.
            // A simpler check: is the center + radius within a slightly larger area than the canvas?
             return radius > 0 && (wave.x + radius > 0 && wave.x - radius < CANVAS_WIDTH && wave.y + radius > 0 && wave.y - radius < CANVAS_HEIGHT * 2); // Check against larger area
        });


        // Calculate perceived frequency at the observer's position
        // Source velocity vector V_s = (scaledCarSpeed, 0)
        // Observer position O = (OBSERVER_X, OBSERVER_Y)
        // Source position S = (carX, CAR_Y)
        // Vector from Source TO Observer V_so = (OBSERVER_X - carX, OBSERVER_Y - CAR_Y)
        const vec_so_x = OBSERVER_X - carX;
        const vec_so_y = OBSERVER_Y - CAR_Y;
        const distance = Math.sqrt(vec_so_x * vec_so_x + vec_so_y * vec_so_y);

        let observedFreq = SOURCE_FREQUENCY; // Default when distance is 0 or speed is 0
        let V_source_towards_observer = 0;

        if (distance > 1) { // Avoid division by zero or near-zero
            // Component of source velocity vector along the S->O vector
            // V_source_towards_observer = (V_s . V_so) / |V_so|
            // V_s . V_so = (scaledCarSpeed, 0) . (vec_so_x, vec_so_y) = scaledCarSpeed * vec_so_x + 0 * vec_so_y = scaledCarSpeed * vec_so_x
            V_source_towards_observer = (scaledCarSpeed * vec_so_x) / distance;

            // Doppler formula: f_obs = f_source * Vsound / (Vsound - V_source_towards_observer)
            // Where V_source_towards_observer is positive if source moves towards observer.
            const denominator = scaledSoundSpeed - V_source_towards_observer;

            if (denominator > scaledSoundSpeed * 0.05) { // Avoid division by zero or near zero (prevents issues near Mach 1)
                 observedFreq = SOURCE_FREQUENCY * scaledSoundSpeed / denominator;
                 // Limit frequency to a reasonable audible/display range
                 const maxFreq = SOURCE_FREQUENCY * 3;
                 const minFreq = SOURCE_FREQUENCY * 0.3;
                 if (observedFreq > maxFreq) observedFreq = maxFreq;
                 if (observedFreq < minFreq) observedFreq = minFreq;
            } else {
                 // Handle near-supersonic or supersonic case
                 observedFreq = 'סילוני!'; // Indicate shockwave/sonic boom visually or textually
            }

        } else {
             // Car is very close to observer (within 1 pixel). Frequency is momentarily close to source frequency
             observedFreq = SOURCE_FREQUENCY;
        }

        // Update displayed frequency
        if (typeof observedFreq === 'number') {
             observedFrequencySpan.textContent = observedFreq.toFixed(1);
             setSoundFrequency(observedFreq); // Update sound frequency
        } else {
             observedFrequencySpan.textContent = observedFreq;
             stopSound(); // Stop sound or set to a specific indicator tone if supersonic
        }

        // Check if car is off-screen and reset or loop
        if (carX > CAR_END_X) {
            // Car went off right side, loop back to start
            initializeSimulation();
            // Keep running if it was running
             if (running) {
                // Small delay before restarting sound/animation might be good
                // For now, just reset and let the loop continue
             } else {
                // If paused, just reset state but don't resume gameLoop
             }
        }
    }

    function gameLoop(currentTime) {
        // Initialize lastTime on the first frame or after a pause
        if (lastTime === 0) {
            lastTime = currentTime;
        }

        const deltaTime = (currentTime - lastTime) / 1000; // delta time in seconds
        lastTime = currentTime;

        update(deltaTime);
        draw();

        // Continue loop only if running is true
        if (running) {
            animationFrameId = requestAnimationFrame(gameLoop);
        }
    }

    function startSimulation() {
        if (!running) {
            // Initialize audio context on first start button click due to browser policies
            if (!soundInitialized) {
                initializeAudio();
            }
            running = true;
            startButton.disabled = true;
            pauseButton.disabled = false;
            resetButton.disabled = false;
            lastTime = 0; // Reset last time for delta time calculation
            gameLoop(performance.now());
            startSound(); // Start playing sound
        }
    }

    function pauseSimulation() {
        if (running) {
            running = false;
            startButton.disabled = false;
            pauseButton.disabled = true;
            cancelAnimationFrame(animationFrameId);
            stopSound(); // Stop playing sound
        }
    }

    function resetSimulation() {
        pauseSimulation(); // Pause if running
        initializeSimulation(); // Reset simulation state (car pos, waves, time)
        startButton.disabled = false; // Enable start button
        pauseButton.disabled = true; // Disable pause button
        resetButton.disabled = false; // Keep reset enabled
        stopSound(); // Ensure sound is off
    }

    // Event Listeners
    speedSlider.addEventListener('input', (event) => {
        const speed = parseFloat(event.target.value);
        currentSpeedSpan.textContent = `${speed} מ' / שנ'`; // Update speed display with unit
        scaledCarSpeed = speed * SCALE;
         // If paused, update the drawing immediately to reflect the new speed
         if (!running) {
            // A simple redraw might not be enough, as wave spacing depends on emission time at speed.
            // It's better to just update the speed variable and have it affect the next run.
            // Or, recalculate frequency based on current pos and new speed if paused near observer.
            // Let's just update the variable and the display text.
            // Optionally, recalculate and display frequency if the car is currently visible
            // This needs checking if carX is within canvas bounds, but that's complex.
            // Simplest is to just update the variable and let it apply when simulation starts/resumes.
         }
    });

    startButton.addEventListener('click', startSimulation);
    pauseButton.addEventListener('click', pauseSimulation);
    resetButton.addEventListener('click', resetSimulation);

    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'רוצה להבין לעומק? הצג הסבר מלא על אפקט דופלר';
         // Scroll to the explanation div? optional
         // if (!isHidden) {
         //    explanationDiv.scrollIntoView({ behavior: 'smooth' });
         // }
    });


    // Initial setup
    initializeSimulation(); // Set up the initial state
    // Sound is initialized on first click of startSimulation due to browser autoplay policies.
    // Check for audio context support and show warning if needed early on.
     if (!window.AudioContext && !window.webkitAudioContext) {
         soundWarningDiv.style.display = 'block';
     }

</script>