---
title: "סימולציית אפקט דופלר קסומה"
english_slug: doppler-effect-interactive-magic
category: "פיזיקה"
tags: [סימולציה, דופלר, גלים, תנועה, קול, אינטראקטיבי, פיזיקה של גלים]
---
# אפקט דופלר: ההדמיה המרתקת

האם עצרתם פעם לשים לב איך הצליל של משהו שזז מהר, כמו אמבולנס או מכונית מירוץ, משתנה כשהוא מתקרב אליכם ואז מתרחק? זו לא אשליה שמיעתית, אלא תופעה פיזיקלית אמיתית ומרתקת בשם "אפקט דופלר". בואו נחקור יחד איך זה קורה דרך הדמיה ויזואלית מרהיבה!

<div id="simulation-container">
    <div id="simulation-area">
        <div id="car" class="entity">
             <div class="car-body"></div>
             <div class="siren">🚨</div>
        </div>
        <div id="observer" class="entity">
            <div class="ear">👂</div>
            <div class="perception-indicator"></div>
        </div>
        <!-- Waves will be added here by JavaScript -->
        <div id="frequency-display">
            <span id="frequency-icon"></span>
            <span id="frequency-text"></span>
        </div>
    </div>
    <div id="controls">
        <button id="start-sim">צא לדרך!</button>
        <button id="reset-sim" disabled>התחל מחדש</button>
    </div>
</div>

<style>
/* כל הסגנונות מרוכזים כאן - יופי של אפליקציה! */
:root {
    --primary-color: #007bff;
    --secondary-color: #28a745;
    --background-color: #f0f8ff;
    --card-background: #ffffff;
    --border-color: #e0e0e0;
    --approaching-color: #00aced; /* Sky Blue */
    --receding-color: #ff4136;    /* Red */
    --neutral-color: #ffc107;     /* Amber */
    --wave-color: rgba(0, 123, 255, 0.6);
    --wave-pulse-color: rgba(255, 193, 7, 0.8); /* Pulsing effect color */
    --text-color: #333;
}

body {
    font-family: 'Arial', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start; /* Align to top for better layout */
    min-height: 100vh;
    background-color: var(--background-color);
    color: var(--text-color);
    padding: 20px;
    line-height: 1.6;
    overflow-x: hidden; /* Prevent horizontal scroll on small screens */
}

h1 {
    color: var(--primary-color);
    margin-bottom: 15px;
    text-align: center;
    font-size: 2.2em;
    font-weight: bold;
}

p {
    margin-bottom: 25px;
    max-width: 800px;
    text-align: center;
    font-size: 1.1em;
}

#simulation-container {
    background-color: var(--card-background);
    border-radius: 15px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
    padding: 25px;
    margin-bottom: 30px;
    width: 100%;
    max-width: 850px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: hidden; /* Prevent waves from going outside */
}

#simulation-area {
    position: relative;
    width: 100%;
    height: 350px; /* Slightly taller */
    border: 2px solid var(--border-color);
    border-radius: 10px;
    overflow: hidden;
    background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* Subtle gradient */
    margin-bottom: 25px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
}

.entity {
    position: absolute;
    bottom: 50%;
    transform: translate(-50%, 50%);
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px; /* Larger icons */
}

#car {
    left: -10%; /* Start further off-screen */
    width: 60px; /* Make car container slightly wider */
    transition: left linear; /* JS controls speed, CSS adds smoothness */
}

.car-body {
     /* Optional: add car shape visually if not just emoji */
}

.siren {
    font-size: 30px; /* Adjust emoji size */
    animation: pulse 1.5s infinite ease-in-out; /* Simple pulse animation for siren */
}

#observer {
    left: 50%;
    width: 50px;
}

.ear {
     font-size: 35px;
}

.perception-indicator {
    position: absolute;
    top: -25px; /* Position above the ear */
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background-color: transparent; /* Default */
    transition: background-color 0.5s ease, transform 0.3s ease;
    pointer-events: none;
    opacity: 0.8;
}

@keyframes pulse-high {
    0% { transform: scale(1); opacity: 0.8; background-color: var(--approaching-color); }
    50% { transform: scale(1.2); opacity: 1; background-color: var(--approaching-color); }
    100% { transform: scale(1); opacity: 0.8; background-color: var(--approaching-color); }
}

@keyframes pulse-low {
    0% { transform: scale(1); opacity: 0.8; background-color: var(--receding-color); }
    50% { transform: scale(1.2); opacity: 1; background-color: var(--receding-color); }
    100% { transform: scale(1); opacity: 0.8; background-color: var(--receding-color); }
}

.perception-high {
    animation: pulse-high 0.8s infinite ease-out; /* Faster pulse for high freq */
}

.perception-low {
     animation: pulse-low 1.2s infinite ease-out; /* Slower pulse for low freq */
}


.wave {
    position: absolute;
    border-width: 2px;
    border-style: solid;
    border-color: var(--wave-color); /* Default wave color */
    border-radius: 50%;
    transform: translate(-50%, -50%); /* Center the circle on its position */
    pointer-events: none; /* Don't interfere with clicks */
    opacity: 0; /* Start hidden */
    box-sizing: border-box; /* Include border in size */
    transition: opacity 0.5s ease, border-color 0.5s ease; /* Smooth fade/color change */
}

/* Optional: Add a subtle gradient or inner glow to waves */
.wave::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 80%; /* Inner glow size */
    height: 80%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    box-shadow: 0 0 15px 5px var(--wave-pulse-color); /* Subtle glow */
    opacity: 0; /* Initially hidden */
    transition: opacity 0.5s ease;
}


#frequency-display {
    position: absolute;
    top: 20px; /* Positioned at the top */
    left: 50%;
    transform: translateX(-50%);
    font-size: 1.4em;
    font-weight: bold;
    color: var(--text-color);
    z-index: 15;
    text-align: center;
    min-width: 250px; /* Ensure space for text */
    background-color: rgba(255, 255, 255, 0.9);
    padding: 8px 15px;
    border-radius: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    transition: color 0.5s ease;
}

#frequency-icon {
    margin-left: 8px; /* Space between text and icon */
    font-size: 1.1em;
    transition: transform 0.3s ease;
    display: inline-block; /* Allows transform */
}


#controls {
    display: flex;
    gap: 15px; /* More space between buttons */
    justify-content: center;
}

#controls button {
    padding: 12px 25px; /* Larger buttons */
    font-size: 1.1em; /* Larger text */
    cursor: pointer;
    border: none;
    border-radius: 8px; /* More rounded corners */
    transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
    font-weight: bold;
}

#start-sim {
    background-color: var(--secondary-color);
    color: white;
}

#start-sim:hover:not(:disabled) {
    background-color: #218838;
    transform: translateY(-2px); /* Subtle lift on hover */
}

#reset-sim {
     background-color: #6c757d; /* Grey */
    color: white;
}
#reset-sim:hover:not(:disabled) {
    background-color: #5a6268;
     transform: translateY(-2px);
}


#controls button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    opacity: 0.7;
    transform: none; /* No lift when disabled */
}

#toggle-explanation {
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #17a2b8; /* Info Blue */
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
     margin-top: 20px;
     margin-bottom: 20px;
}

#toggle-explanation:hover {
    background-color: #138496;
     transform: translateY(-2px);
}


#explanation {
    margin-top: 20px;
    padding: 25px; /* More padding */
    background-color: #e9ecef; /* Light Grey */
    border-radius: 10px;
    max-width: 850px; /* Match container width */
    display: none; /* Initially hidden */
    text-align: right;
    line-height: 1.7;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#explanation h2 {
    color: var(--primary-color);
    margin-bottom: 20px; /* More space */
    text-align: center;
    font-size: 1.8em;
}

#explanation p {
    text-align: right;
    margin-bottom: 18px; /* More space */
    font-size: 1.05em;
}

#explanation p:last-child {
    margin-bottom: 0;
}

</style>

<button id="toggle-explanation">רוצים להבין לעומק? לחצו כאן להסבר!</button>

<div id="explanation">
    <h2>אפקט דופלר: קסם הצליל והתנועה</h2>
    <p>אז מה בעצם קורה כאן? אפקט דופלר הוא תופעה מדהימה שבה התדירות (וזה אומר גם אורך הגל) של גל משתנה בגלל שיש <strong>תנועה יחסית</strong> בין המקור שפולט את הגל (במקרה שלנו, המכונית עם הסירנה) לבין הצופה שמקבל את הגל (אתם!).</p>
    <p>תארו לעצמכם את המכונית פולטת גלי קול כמו טיפות שנופלות לאגם. כשהמכונית נוסעת לעברכם, היא "רודפת" אחרי הגלים הקודמים שהיא פלטה בכיוון שלכם. זה גורם לכך שהמרחק בין פסגות הגלים (אורך הגל) נהיה קטן יותר, ולכם זה נשמע כאילו הגלים מגיעים מהר יותר – כלומר, <strong>התדירות נתפסת כגבוהה יותר</strong> והצליל חד וגבוה יותר (כמו "וואי-וואי").</p>
    <p>לעומת זאת, כשהמכונית מתרחקת מכם, היא בעצם "בורחת" מהגלים שהיא פולטת בכיוון ההפוך. זה גורם לכך שהמרחק בין פסגות הגלים בכיוון התנועה גדל. לכן, הגלים מגיעים אליכם בקצב איטי יותר – <strong>התדירות נתפסת כנמוכה יותר</strong> והצליל נשמע נמוך ועמום יותר (כמו "ווהה-ווהה").</p>
    <p>חשוב להבין שאפקט דופלר לא משנה את התדירות המקורית שהמקור פולט, אלא רק את <strong>התדירות שנתפסת</strong> על ידי הצופה בזמן שהמקור בתנועה. התופעה הזו לא מוגבלת רק לגלי קול; היא קורית גם עם גלי אור (מה שמאפשר לאסטרונומים לדעת אם כוכבים מתרחקים או מתקרבים אלינו דרך ה"הסחה לאדום/כחול") ועם כל סוג אחר של גלים. זהו כלי רב עוצמה במדע ובטכנולוגיה!</p>
</div>

<script>
// כל הלוגיקה והאינטראקציה ב-JavaScript - כמו מנוע של משחק!
const simulationArea = document.getElementById('simulation-area');
const car = document.getElementById('car');
const observer = document.getElementById('observer');
const frequencyDisplay = document.getElementById('frequency-display');
const frequencyIcon = document.getElementById('frequency-icon');
const frequencyText = document.getElementById('frequency-text');
const perceptionIndicator = document.querySelector('#observer .perception-indicator');
const startButton = document.getElementById('start-sim');
const resetButton = document.getElementById('reset-sim');
const explanationDiv = document.getElementById('explanation');
const toggleExplanationButton = document.getElementById('toggle-explanation');

// Simulation parameters - משתנים שמגדירים את "חוקי המשחק"
const SIM_WIDTH = simulationArea.offsetWidth;
const CAR_START_X = -0.1 * SIM_WIDTH; // Start off-screen left (10% of width)
const CAR_END_X = 1.1 * SIM_WIDTH; // End off-screen right (10% of width)
const CAR_TRAVEL_DURATION = 12000; // Total time for car to cross the visual area (milliseconds)
const SOUND_SPEED_RELATIVE = 1.8; // Sound speed relative to Car speed *over the duration*. Higher = waves expand faster relative to car movement.
const EMISSION_INTERVAL = 100; // Emit a wave every X milliseconds (determines source frequency)
const WAVE_LIFETIME = 6000; // Waves disappear after X milliseconds (prevents memory issues)

let animationFrameId = null;
let lastEmissionTime = 0;
let waves = [];
let startTime = null;
let simRunning = false;

// Function to reset the simulation to its initial state
function resetSimulation() {
    cancelAnimationFrame(animationFrameId);
    animationFrameId = null;
    simRunning = false;

    // Reset car position
    car.style.left = `${CAR_START_X}px`;

    // Remove all wave elements from the DOM
    waves.forEach(wave => wave.element.remove());
    waves = []; // Clear the waves array

    // Reset time tracking
    lastEmissionTime = 0;
    startTime = null;

    // Reset frequency indicator display
    frequencyText.textContent = 'מוכן להתחלה';
    frequencyIcon.textContent = '▶️'; // Play icon
    frequencyDisplay.style.color = 'var(--text-color)';
    perceptionIndicator.style.backgroundColor = 'transparent';
    perceptionIndicator.classList.remove('perception-high', 'perception-low');


    // Update button states
    startButton.disabled = false;
    resetButton.disabled = true;
}

// Function to emit a new wave from the car's current position
function emitWave(carX, carY, currentTime) {
    const waveElement = document.createElement('div');
    waveElement.classList.add('wave');
    simulationArea.appendChild(waveElement);

    waves.push({
        element: waveElement,
        emissionX: carX,
        emissionY: carY,
        startTime: currentTime
    });

    // Visual feedback on emission (optional: subtle car shake or siren flash)
     car.style.transform = 'translate(-50%, 50%) scale(1.02)';
     setTimeout(() => { car.style.transform = 'translate(-50%, 50%) scale(1)'; }, 50); // Quick reset
}


// Main simulation update loop
function updateSimulation(currentTime) {
    if (!startTime) startTime = currentTime;
    const elapsedTime = currentTime - startTime;

    // Calculate car position based on elapsed time and duration
    // Linear movement for simplicity
    const totalTravelDistance = CAR_END_X - CAR_START_X;
    let carX = CAR_START_X + (totalTravelDistance * (elapsedTime / CAR_TRAVEL_DURATION));

    // Stop simulation when car is fully off screen
    if (carX > CAR_END_X) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
        simRunning = false;
        frequencyText.textContent = 'הסימולציה הסתיימה';
        frequencyIcon.textContent = '✅';
        frequencyDisplay.style.color = var(--primary-color);
        perceptionIndicator.style.backgroundColor = 'transparent';
        perceptionIndicator.classList.remove('perception-high', 'perception-low');


        startButton.disabled = false;
        resetButton.disabled = false; // Allow reset after finish
        return; // Stop updating
    }

    // Update car position
    car.style.left = `${carX}px`;
    const carY = car.offsetTop + car.offsetHeight / 2; // Y position of car center

    // Emit waves at regular intervals
    if (currentTime - lastEmissionTime > EMISSION_INTERVAL && carX < SIM_WIDTH * 1.05) { // Stop emitting slightly after leaving screen
        emitWave(carX, carY, currentTime);
        lastEmissionTime = currentTime;
    }

    // Calculate observer position (fixed)
    const observerX = observer.offsetLeft + observer.offsetWidth / 2;
    const observerY = observer.offsetTop + observer.offsetHeight / 2;

    // Calculate speed of sound in pixels per millisecond, scaled relative to car speed and simulation area/duration
    // We need a consistent speed unit. Let's define SOUND_SPEED as pixels per frame based on a nominal frame rate (e.g., 60fps)
    // A wave emitted at carX at time t will have radius (currentTime - t) * (SOUND_SPEED_RELATIVE * base_speed)
    // Base speed could be pixels car moves per ms or frame. Let's simplify.
    // Let's scale SOUND_SPEED_RELATIVE to the simulation area and duration.
    // If car travels SIM_WIDTH in CAR_TRAVEL_DURATION ms, car speed is SIM_WIDTH / CAR_TRAVEL_DURATION px/ms
    // Sound speed could be (SIM_WIDTH / CAR_TRAVEL_DURATION) * SOUND_SPEED_RELATIVE px/ms
    const baseSpeed_px_per_ms = totalTravelDistance / CAR_TRAVEL_DURATION; // Average car speed
    const soundSpeed_px_per_ms = baseSpeed_px_per_ms * SOUND_SPEED_RELATIVE;

    // Update waves: expand and fade, remove old waves
    const newWaves = [];
    waves.forEach(wave => {
        const timeSinceEmission = currentTime - wave.startTime;
        const radius = timeSinceEmission * soundSpeed_px_per_ms; // Radius based on time and sound speed

        // Check if wave is still relevant (within bounds or not faded out)
        const waveDiameter = radius * 2;
        const waveRightEdge = wave.emissionX + radius;
        const waveLeftEdge = wave.emissionX - radius;

        // Keep wave if not too old and potentially visible
        if (timeSinceEmission < WAVE_LIFETIME && (waveRightEdge > 0 && waveLeftEdge < SIM_WIDTH)) {
             wave.element.style.width = `${waveDiameter}px`;
             wave.element.style.height = `${waveDiameter}px`;
             wave.element.style.left = `${wave.emissionX}px`; // Position from emission point
             wave.element.style.top = `${wave.emissionY}px`; // Position from emission point

             // Fade out based on age
             const opacity = Math.max(0, 1 - timeSinceEmission / WAVE_LIFETIME);
             wave.element.style.opacity = opacity;

             // Optional: visual effect when passing observer
             const distanceToObserver = Math.sqrt(Math.pow(wave.emissionX - observerX, 2) + Math.pow(wave.emissionY - observerY, 2));
             const distanceTravelledByWave = radius;
             const distanceThreshold = 20; // Pixels threshold around observer for effect

             if (Math.abs(distanceTravelledByWave - distanceToObserver) < distanceThreshold) {
                  // Wave is passing the observer! Add a temporary visual cue.
                   wave.element.style.borderColor = var(--wave-pulse-color); // Change color
                   // Maybe make the inner glow visible briefly
                    const innerGlow = wave.element.querySelector('::before');
                    if (innerGlow) innerGlow.style.opacity = 1; // Show glow
             } else {
                   wave.element.style.borderColor = var(--wave-color); // Revert color
                   const innerGlow = wave.element.querySelector('::before');
                   if (innerGlow) innerGlow.style.opacity = 0; // Hide glow
             }


            newWaves.push(wave); // Keep this wave
        } else {
             wave.element.remove(); // Remove element from DOM
        }
    });
    waves = newWaves; // Update the waves array


    // Update frequency indicator and observer perception based on car position relative to observer
    const approachingThreshold = observerX - (car.offsetWidth / 2); // Car approaches center of observer
    const recedingThreshold = observerX + (car.offsetWidth / 2); // Car recedes from center of observer

    if (carX < approachingThreshold) {
        frequencyText.textContent = 'מתקרב: תדירות גבוהה ⬆️';
        frequencyDisplay.style.color = var(--approaching-color);
        perceptionIndicator.classList.add('perception-high');
        perceptionIndicator.classList.remove('perception-low');
    } else if (carX > recedingThreshold) {
        frequencyText.textContent = 'מתרחק: תדירות נמוכה ⬇️';
        frequencyDisplay.style.color = var(--receding-color);
         perceptionIndicator.classList.add('perception-low');
         perceptionIndicator.classList.remove('perception-high');

    } else {
        // Car is directly in front of or passing the observer
        frequencyText.textContent = 'עובר ליד הצופה: תדירות משתנה';
        frequencyDisplay.style.color = var(--neutral-color);
         perceptionIndicator.classList.remove('perception-high', 'perception-low');
         // Maybe add a quick pulse or change color temporarily here?
          // perceptionIndicator.style.backgroundColor = var(--neutral-color); // Neutral color briefly
           // setTimeout(() => perceptionIndicator.style.backgroundColor = 'transparent', 300); // Fade back
    }


    // Continue the animation loop
    if (simRunning) {
       animationFrameId = requestAnimationFrame(updateSimulation);
    }
}

// Function to start the simulation
function startSimulation() {
    if (!simRunning) {
        resetSimulation(); // Ensure clean start
        simRunning = true;
        startButton.disabled = true;
        resetButton.disabled = false;
        startTime = performance.now();
        lastEmissionTime = startTime - EMISSION_INTERVAL; // Emit first wave immediately
        frequencyText.textContent = 'מתחיל...';
        frequencyIcon.textContent = '⏳';
        frequencyDisplay.style.color = var(--neutral-color);

        animationFrameId = requestAnimationFrame(updateSimulation); // Start the animation loop
    }
}

// Event Listeners for controls
startButton.addEventListener('click', startSimulation);
resetButton.addEventListener('click', resetSimulation);

// Event Listener for the explanation toggle button
toggleExplanationButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'רוצים להבין לעומק? לחצו כאן להסבר!';
});

// Initialize simulation state when the script loads
resetSimulation();

// Optional: Handle window resize to potentially re-calculate SIM_WIDTH and reset
window.addEventListener('resize', () => {
    // For simplicity, a full reset on resize is easiest.
    // In a complex app, you might recalculate positions and speeds.
    resetSimulation();
    SIM_WIDTH = simulationArea.offsetWidth; // Update simulation width
    // Re-set CAR_START_X, CAR_END_X based on new SIM_WIDTH if needed
});

// Ensure elements are rendered before initial calculations (like SIM_WIDTH)
// requestAnimationFrame ensures the DOM is ready for layout calculations
requestAnimationFrame(() => {
     SIM_WIDTH = simulationArea.offsetWidth;
     // Recalculate start/end positions based on the initial SIM_WIDTH
     CAR_START_X = -0.1 * SIM_WIDTH;
     CAR_END_X = 1.1 * SIM_WIDTH;
     // Ensure car is in the correct initial position after potential resize/load
     car.style.left = `${CAR_START_X}px`;
});

</script>