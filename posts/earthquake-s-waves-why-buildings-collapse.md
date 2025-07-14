---
title: "גל ההרס: איך גלי S ברעידות אדמה מפילים מבנים?"
english_slug: earthquake-s-waves-why-buildings-collapse
category: "מדעי הסביבה / גיאולוגיה"
tags:
  - גלים רוחביים
  - רעידת אדמה
  - סייסמולוגיה
  - גלים סיסמיים
  - הנדסת מבנים
---

# גל ההרס: איך גלי S ברעידות אדמה מפילים מבנים?

רעידות אדמה משחררות כוח אדיר שיכול להפוך ערים לעיי חורבות. רבים חושבים שהקרקע פשוט רועדת למעלה ולמטה, אבל האמת מורכבת ומסוכנת הרבה יותר. הכירו את הארכי-נבל של הגלים הסיסמיים – הגלים הרוחביים (גלי S) – הגורמים האמיתיים מאחורי קריסת מבנים. למה דווקא הם? כי הם גורמים לקרקע לנוע בצורה הכי הרסנית שיש למבנים.

<div id="app-container">
    <div id="simulation">
        <div id="wave-source" title="מקור גל S - מתקדם מצד שמאל לימין">גל S</div>
        <div id="ground">
             <!-- Segments will be added/managed by JS for better wave visualization -->
        </div>
        <div id="building">
            <div class="window"></div>
            <div class="window"></div>
            <div class="window"></div>
            <div class="window"></div>
        </div>
         <div id="debris-container"></div> <!-- For collapse animation debris -->
    </div>
    <div id="controls">
        <div>
            <label for="amplitude">עוצמת הגל (אמפליטודה):</label>
            <input type="range" id="amplitude" min="0" max="40" value="10"> <!-- Increased max amplitude for dramatic collapse -->
            <span id="amplitude-value">10</span>
        </div>
        <div>
            <label for="frequency">תדירות הגל:</label>
            <input type="range" id="frequency" min="0.2" max="3" step="0.1" value="0.8"> <!-- Adjusted frequency range -->
            <span id="frequency-value">0.8</span>
        </div>
        <button id="start-stop">התחל סימולציה</button>
    </div>
    <div id="message">נא התחל סימולציה לראות את השפעת הגלים.</div>
</div>

<style>
#app-container {
    font-family: 'Arial', sans-serif;
    max-width: 800px;
    margin: 30px auto;
    border: 1px solid #ddd;
    border-radius: 12px;
    padding: 25px;
    background-color: #ffffff;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    text-align: center;
}

#simulation {
    position: relative;
    width: 100%;
    height: 250px; /* Increased height */
    border-bottom: 3px solid #654321; /* Darker brown ground line */
    margin-bottom: 30px;
    overflow: hidden;
    background: linear-gradient(to bottom, #87ceeb, #b0e0e6); /* Sky gradient */
    border-radius: 8px;
}

#wave-source {
    position: absolute;
    left: 15px;
    bottom: 60px; /* Position above visual ground */
    background-color: #e74c3c; /* Red color */
    color: white;
    padding: 8px 15px;
    border-radius: 20px; /* Pill shape */
    font-size: 0.9em;
    font-weight: bold;
    z-index: 1;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    animation: pulse 1.5s infinite ease-in-out; /* Added pulse animation */
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

#ground {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 60px; /* Visual ground height */
    background-color: #8b4513; /* SaddleBrown ground */
    overflow: hidden;
    display: flex; /* Use flexbox for segments */
    align-items: center;
}

.ground-segment {
    flex-grow: 1; /* Segments fill width */
    height: 100%;
    background-color: rgba(0, 0, 0, 0.05); /* Subtle separators */
    border-right: 1px dashed rgba(255, 255, 255, 0.2); /* Lighter dashed lines */
    box-sizing: border-box;
}

.ground-segment:last-child {
    border-right: none;
}


#building {
    position: absolute;
    bottom: 60px; /* Position it on top of the visual ground height */
    left: 50%;
    transform: translateX(-50%) rotate(0deg); /* Initial state */
    width: 60px; /* Slightly wider */
    height: 100px; /* Taller */
    background-color: #bdc3c7; /* Silver/Grey building */
    border: 3px solid #34495e; /* Darker border */
    box-sizing: border-box;
    transform-origin: bottom center; /* Rotate from the base */
    z-index: 2; /* Ensure building is above ground */
    transition: transform 0.05s linear; /* Smoother but still responsive movement */
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    padding: 5px 0;
}

#building .window {
    width: 40px;
    height: 12px;
    background-color: #aed6f1; /* Light blue windows */
    border: 1px solid #2c3e50; /* Dark window frame */
    border-radius: 2px;
}

#building.cracked {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><line x1="10" y1="10" x2="90" y2="90" stroke="%23e74c3c" stroke-width="2"/><line x1="90" y1="10" x2="10" y2="90" stroke="%23e74c3c" stroke-width="2"/></svg>'); /* Simple crack pattern */
    background-repeat: repeat;
    background-size: 30% 30%; /* Scale pattern */
    opacity: 0.8;
}

#building.collapsed {
    display: none; /* Hide the main building element when collapsed */
}

#debris-container {
    position: absolute;
    bottom: 60px; /* Position above ground */
    left: 50%;
    transform: translateX(-50%);
    width: 100px; /* Area for debris spread */
    height: 80px;
    z-index: 2;
    pointer-events: none; /* Don't block clicks */
}

.debris {
    position: absolute;
    width: 5px;
    height: 5px;
    background-color: #7f8c8d; /* Grey debris color */
    border-radius: 50%; /* Make debris round */
    pointer-events: none;
    animation: fadeOutFall 1s ease-out forwards; /* Animation defined in JS/CSS */
}

@keyframes fadeOutFall {
    to {
        transform: translate(var(--dx, 0), var(--dy, 50px)) rotate(var(--dr, 0deg));
        opacity: 0;
    }
}


#controls {
    display: flex;
    flex-direction: column;
    gap: 15px; /* Increased gap */
    align-items: center;
    margin-bottom: 20px;
    padding: 15px;
    background-color: #ecf0f1; /* Light grey background for controls */
    border-radius: 8px;
    border: 1px solid #ddd;
}

#controls div {
    display: flex;
    align-items: center;
    gap: 15px; /* Increased gap */
    width: 100%;
    justify-content: center;
}

#controls label {
    width: 180px; /* Increased width for labels */
    text-align: right;
    font-weight: bold;
    color: #34495e;
}

#controls input[type="range"] {
    flex-grow: 1;
    max-width: 350px; /* Increased max width */
    accent-color: #e74c3c; /* Red accent color for sliders */
}

#controls span {
    min-width: 40px; /* Increased width for value display */
    text-align: left;
    font-weight: bold;
    color: #34495e;
}

#start-stop {
    padding: 12px 25px; /* Increased padding */
    background-color: #3498db; /* Blue color */
    color: white;
    border: none;
    border-radius: 6px; /* Slightly more rounded */
    cursor: pointer;
    font-size: 1.1em; /* Increased font size */
    margin-top: 15px;
    transition: background-color 0.2s ease;
    font-weight: bold;
}

#start-stop:hover {
    background-color: #2980b9;
}

#start-stop.reset {
    background-color: #e67e22; /* Orange for reset */
}
#start-stop.reset:hover {
    background-color: #d35400;
}


#message {
    margin-top: 15px;
    font-size: 1.1em;
    color: #555;
    min-height: 1.5em; /* Reserve space */
}

#show-explanation-button {
    display: block;
    margin: 30px auto 20px auto; /* Adjust margin */
    padding: 12px 25px;
    background-color: #2ecc71; /* Green color */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.2s ease;
    font-weight: bold;
}

#show-explanation-button:hover {
    background-color: #27ae60;
}

#explanation {
    margin-top: 20px;
    padding: 20px; /* Increased padding */
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f8f9fa; /* Lighter background */
    display: none; /* Hidden by default */
    text-align: right; /* Right-to-left text */
    line-height: 1.7; /* Improved readability */
}

#explanation h2 {
    margin-top: 0;
    color: #34495e;
    border-bottom: 2px solid #bdc3c7; /* Lighter border */
    padding-bottom: 8px;
    margin-bottom: 15px;
    font-size: 1.6em;
}

#explanation h3 {
    color: #34495e;
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 1.3em;
}


#explanation p {
    margin-bottom: 15px;
}

#explanation ul {
    margin-top: 10px;
    padding-right: 25px; /* Adjust padding for RTL */
    list-style: disc inside; /* Disc bullets inside */
}

#explanation li {
    margin-bottom: 10px;
}

#explanation strong {
    color: #e74c3c; /* Highlight key terms */
}
</style>

<button id="show-explanation-button">הצג/הסתר הסבר מפורט</button>

<div id="explanation">
    <h2>הסבר: גלים רוחביים (S-waves) וכוחות הגזירה ההרסניים</h2>

    <p>רעידות אדמה אינן רק "רעידה" אקראית, אלא שחרור מהיר של אנרגיה המתבטאת בתנועת גלים עוצמתיים דרך קרום כדור הארץ. ישנם מספר סוגי גלים סיסמיים, ולכל אחד מהם השפעה שונה לחלוטין על פני השטח ועל מבנים. בסימולציה שלמעלה חוויתם מקרוב את הגל המרכזי האחראי לקריסות מבנים – הגל הרוחבי (S-wave).</p>

    <h3>סוגי גלים סיסמיים עיקריים:</h3>
    <ul>
        <li><strong>גלי גוף (Body Waves):</strong> מטיילים עמוק בתוך כדור הארץ.
            <ul>
                <li><strong>גלי P (Primary/Compressional):</strong> אלה הגלים הראשונים והמהירים ביותר שמגיעים. הם גורמים לקרקע להידחס ולהימתח בכיוון התקדמות הגל (תנועה קדימה ואחורה). בגלל אופי זה, הם יכולים לעבור גם דרך נוזלים וגזים. לרוב גלי P פחות הרסניים למבנים ונתפסים יותר כדחיפה או נקיפה מהירה.</li>
                <li><strong>גלי S (Secondary/Shear):</strong> איטיים מגלי P, ולכן מגיעים אחריהם. בניגוד לגלי P, גלי S גורמים לחלקיקי הקרקע לנוע בניצב (בניצב!) לכיוון שבו הגל מתקדם. תנועה זו יכולה להיות למעלה-למטה או מצד-לצד, והיא זו שמפעילה כוחות גזירה אדירים על כל דבר שניצב בדרכה. <strong>נקודה קריטית: גלי S יכולים לנוע רק דרך חומר מוצק</strong>, כי נוזלים וגזים אינם מסוגלים לתמוך בכוחות הגזירה הללו.</li>
            </ul>
        </li>
        <li><strong>גלי שטח (Surface Waves):</strong> אלה הגלים האיטיים ביותר, אך לרוב גורמים לנזק הרב ביותר כי הם מתפשטים לאורך פני השטח ומשפיעים ישירות על מה שבנוי עליו. גלי Love גורמים לתנועה אופקית חזקה מצד לצד (בדומה לתנועת הגלים הרוחביים בסימולציה), וגלי Rayleigh גורמים לתנועה אליפטית דמוית גלי ים.</li>
    </ul>

    <h3>הסכנה הייחודית של גלים רוחביים (S-waves) למבנים:</h3>
    <p>ראיתם בסימולציה איך הגל הרוחבי מגיע וגורם לקרקע לזוז בעוצמה מצד לצד. תנועה זו של בסיס המבנה, כשהחלק העליון שלו שואף להישאר במקום עקב אינרציה, יוצרת <strong>כוחות גזירה (Shear Forces)</strong>. חשבו על זה כאילו מנסים לדחוף את בסיס הבניין לצד אחד ואת הגג לצד השני בו זמנית.</p>
    <ul>
        <li><strong>כוחות גזירה:</strong> אלו כוחות שפועלים במקביל לשטח מסוים וגורמים לחלקים של החומר להחליק אחד על גבי השני. בדוגמה של בניין, כוחות הגזירה פועלים על העמודים והקירות, מנסים לעוות אותם לצורה של מקבילית (מעוין).</li>
        <li><strong>למה זה מסוכן?</strong> מרבית המבנים מתוכננים לעמוד בעומסים אנכיים כבדים מאוד (כמו המשקל של הבניין עצמו, כוח הכבידה). הם חלשים באופן יחסי כנגד כוחות אופקיים שמנסים לדחוף אותם ולגזור אותם. הגלים הרוחביים, וכן גלי השטח מסוג Love, מפעילים בדיוק את הכוחות ההרסניים הללו. כפי שראיתם, ככל שעוצמת הגל גדלה, כך כוחות הגזירה מתגברים, והבניין סובל מעיוות קיצוני שיכול להוביל לסדיקה קשה ולבסוף לקריסה קטסטרופלית.</li>
    </ul>

    <h3>התמודדות הנדסית:</h3>
    <p>הבנת ההשפעה של גלי S היא קריטית להנדסת מבנים עמידים לרעידות אדמה. תכנון מודרני כולל חיזוקים מיוחדים שנועדו לעמוד בכוחות גזירה אופקיים: שימוש בקירות גזירה (קירות בטון מזוין עבים), הוספת קורות אלכסוניות (ברייסים) בתוך שלד הבניין, ואף טכנולוגיות מתקדמות יותר כמו מפרידי בסיס המאפשרים לבסיס הבניין לנוע עם הקרקע בעוד שהבניין עצמו נשאר יחסית יציב. מטרת כל הטכניקות הללו היא "לרכוב" על הגלים ההרסניים או לפזר את האנרגיה שלהם, במקום להתנגד לה ישירות עד לשבירה.</p>
    <p>שחקו עם הסימולציה, בדקו אילו שילובים של עוצמה ותדירות גורמים לבניין להתנדנד או לקרוס, והבינו בעצמכם את הכוח ההרסני הייחודי של הגלים הרוחביים ברעידות אדמה.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulation = document.getElementById('simulation');
    const ground = document.getElementById('ground');
    const building = document.getElementById('building');
    const debrisContainer = document.getElementById('debris-container');
    const amplitudeControl = document.getElementById('amplitude');
    const frequencyControl = document.getElementById('frequency');
    const amplitudeValue = document.getElementById('amplitude-value');
    const frequencyValue = document.getElementById('frequency-value');
    const startStopButton = document.getElementById('start-stop');
    const messageDiv = document.getElementById('message');
    const showExplanationButton = document.getElementById('show-explanation-button');
    const explanationDiv = document.getElementById('explanation');

    const SEGMENT_COUNT = 40; // More segments for smoother visual wave
    const GROUND_HEIGHT = 60; // Should match CSS
    const BUILDING_HEIGHT = 100; // Should match CSS
    const BUILDING_WIDTH = 60; // Should match CSS
    const COLLAPSE_THRESHOLD_TILT = 18; // Degrees, approx max tilt before collapse
    const COLLAPSE_THRESHOLD_AMPLITUDE = 25; // Collapse also if amplitude is just very high
    const BUILDING_CENTER_X_PERCENT = 50; // Building initial center %

    let isAnimating = false;
    let animationFrameId = null;
    let startTime = null;
    let isCollapsed = false;

    // Building state for smoother sway (simplified physics)
    let buildingCurrentTilt = 0; // Degrees
    let buildingAngularVelocity = 0;
    const TILT_SPRING_CONSTANT = 0.05; // How strongly it tries to follow ground tilt
    const TILT_DAMPING = 0.9; // How quickly sway dies down (lower = more damping)
    const MAX_SWAY_TILT = 30; // Cap the visual sway to prevent extreme angles before collapse animation

    // Create ground segments
    function createGroundSegments() {
        ground.innerHTML = ''; // Clear existing
        for (let i = 0; i < SEGMENT_COUNT; i++) {
            const segment = document.createElement('div');
            segment.classList.add('ground-segment');
            ground.appendChild(segment);
        }
    }

    // --- Simulation Logic (Horizontal Ground Motion -> Building Sway -> Collapse) ---

    function updateSimulation(currentTime) {
        if (!startTime) startTime = currentTime;
        const elapsed = (currentTime - startTime) / 1000; // Time in seconds
        const dt = (currentTime - (updateSimulation.lastTime || currentTime)) / 1000; // Delta time in seconds
        updateSimulation.lastTime = currentTime;

        const amplitude = parseFloat(amplitudeControl.value);
        const frequency = parseFloat(frequencyControl.value);
        const angularFrequency = 2 * Math.PI * frequency;

        const segments = ground.querySelectorAll('.ground-segment');
        const segmentCount = segments.length;
        const groundWidth = ground.offsetWidth;

        // Calculate ground displacement profile along its length
        const groundDisplacements = [];
        segments.forEach((segment, index) => {
            const phaseShift = (index / (segmentCount - 1)) * (2 * Math.PI * 2); // Phase varies across ground length, 2 full wavelengths
            const waveValue = amplitude * Math.sin(angularFrequency * elapsed - phaseShift);
             // Apply horizontal translation to segments
            segment.style.transform = `translateX(${waveValue}px)`;
            groundDisplacements.push(waveValue);
        });

        // Building reacts to the ground motion at its base
        // Approximate ground displacement under the building center
        const buildingGroundIndexApprox = Math.floor(segmentCount * (BUILDING_CENTER_X_PERCENT / 100));
        const buildingGroundIndex = Math.max(0, Math.min(segmentCount - 1, buildingGroundIndexApprox)); // Clamp index
        const baseGroundDisplacement = groundDisplacements[buildingGroundIndex];

        // --- Simplified Building Sway Physics ---
        if (!isCollapsed) {
            // Target tilt based on ground displacement
            const targetTilt = baseGroundDisplacement * 0.7; // Scale factor from displacement to tilt (tuned for visual effect)

            // Angular acceleration based on difference from target and damping
            const tiltDifference = targetTilt - buildingCurrentTilt;
            const angularAcceleration = (tiltDifference * TILT_SPRING_CONSTANT) - (buildingAngularVelocity * (1 - TILT_DAMPING));

            // Update angular velocity and tilt
            buildingAngularVelocity += angularAcceleration * dt * 100; // Scale dt effect
            buildingCurrentTilt += buildingAngularVelocity * dt * 100; // Scale dt effect

             // Apply tilt and horizontal base shift
            const effectiveTilt = Math.max(-MAX_SWAY_TILT, Math.min(MAX_SWAY_TILT, buildingCurrentTilt)); // Cap visual tilt during sway
            building.style.left = `calc(${BUILDING_CENTER_X_PERCENT}% + ${baseGroundDisplacement}px)`; // Adjust building left position based on ground shift
            building.style.transform = `translateX(-50%) rotate(${effectiveTilt}deg)`;

            // Check for collapse condition
            const totalTiltMagnitude = Math.abs(effectiveTilt);
            if (totalTiltMagnitude > COLLAPSE_THRESHOLD_TILT || amplitude > COLLAPSE_THRESHOLD_AMPLITUDE) {
                 triggerCollapse();
            }

             // Add crack visual at high stress
             if (totalTiltMagnitude > COLLAPSE_THRESHOLD_TILT * 0.6 || amplitude > COLLAPSE_THRESHOLD_AMPLITUDE * 0.7) {
                 building.classList.add('cracked');
             } else {
                 building.classList.remove('cracked');
             }

        } else {
             // If collapsed, ensure building is hidden and debris might be animating
        }
        // --- End Simplified Building Sway Physics ---


        if (isAnimating && !isCollapsed) {
            animationFrameId = requestAnimationFrame(updateSimulation);
        } else if (!isAnimating && !isCollapsed) {
             // Animation stopped, reset segments but keep building state until start is pressed
             segments.forEach(segment => {
                  segment.style.transform = `translateX(0px)`;
             });
             // Don't reset building position/tilt here, only when Start/Reset is pressed
             updateSimulation.lastTime = null; // Reset dt calculation
        } else if (isCollapsed){
            // Animation stopped due to collapse, don't reset anything except maybe clear debris after time
            updateSimulation.lastTime = null; // Reset dt calculation
        }
    }

    // --- End Simulation Logic ---

    function triggerCollapse() {
        if (isCollapsed) return;
        isCollapsed = true;
        isAnimating = false;
        cancelAnimationFrame(animationFrameId);

        building.classList.add('collapsed');
        messageDiv.textContent = 'המבנה קרס! התחל שוב לנסות עוצמות אחרות.';
        startStopButton.textContent = 'התחל סימולציה מחדש';
         startStopButton.classList.add('reset');


        // Create debris particles
        const buildingRect = building.getBoundingClientRect();
        const simulationRect = simulation.getBoundingClientRect();
        const buildingCenterX = buildingRect.left + buildingRect.width / 2 - simulationRect.left; // Center X relative to simulation
        const buildingBottomY = buildingRect.bottom - simulationRect.top; // Bottom Y relative to simulation

        for (let i = 0; i < 30; i++) {
            const debris = document.createElement('div');
            debris.classList.add('debris');
            // Position near the base of the building
            const startX = buildingCenterX + (Math.random() - 0.5) * BUILDING_WIDTH * 0.8;
            const startY = buildingBottomY - (Math.random()) * BUILDING_HEIGHT * 0.5; // Start higher up on the building
            debris.style.left = `${startX}px`;
            debris.style.top = `${startY}px`;

            // Randomize landing position and rotation
            const landingDistance = 50 + Math.random() * 100; // Spread out debris horizontally
            const landingAngle = Math.random() * Math.PI * 2; // Random direction
            const dx = Math.cos(landingAngle) * landingDistance;
            const dy = Math.abs(Math.sin(landingAngle) * landingDistance * 0.5) + 50; // More likely to fall down
             const rotation = Math.random() * 360;

            debris.style.setProperty('--dx', `${dx}px`);
            debris.style.setProperty('--dy', `${dy}px`);
             debris.style.setProperty('--dr', `${rotation}deg`);


            debrisContainer.appendChild(debris);

            // Remove debris after animation
            debris.addEventListener('animationend', () => {
                debris.remove();
            });
        }

    }

     function resetSimulation() {
        isAnimating = false;
        isCollapsed = false;
        cancelAnimationFrame(animationFrameId);
        startTime = null;
        updateSimulation.lastTime = null; // Reset delta time

        // Reset building state
        buildingCurrentTilt = 0;
        buildingAngularVelocity = 0;
        building.style.transform = 'translateX(-50%) rotate(0deg)';
        building.style.left = '50%';
        building.classList.remove('collapsed', 'cracked');

        // Reset ground segments
        ground.querySelectorAll('.ground-segment').forEach(segment => {
             segment.style.transform = `translateX(0px)`;
        });

        // Clear debris
        debrisContainer.innerHTML = '';

        // Reset UI
        startStopButton.textContent = 'התחל סימולציה';
        startStopButton.classList.remove('reset');
        messageDiv.textContent = 'נא התחל סימולציה לראות את השפעת הגלים.';

     }


    startStopButton.addEventListener('click', () => {
        if (isCollapsed) {
            resetSimulation();
        } else {
            isAnimating = !isAnimating;
            if (isAnimating) {
                startStopButton.textContent = 'עצור סימולציה';
                 startStopButton.classList.remove('reset');
                 messageDiv.textContent = 'הסימולציה פועלת... צפה בתנועה.';
                startTime = null; // Reset time on start
                animationFrameId = requestAnimationFrame(updateSimulation);
            } else {
                startStopButton.textContent = 'התחל סימולציה';
                 startStopButton.classList.remove('reset');
                 messageDiv.textContent = 'הסימולציה הופסקה. שנה הגדרות או התחל שוב.';
                cancelAnimationFrame(animationFrameId);
                // Keep building position/tilt as it was when stopped? Or reset?
                // Let's reset visuals to initial state when stopped, but keep control values.
                 resetSimulation(); // A full reset on stop makes it clearer
                 isCollapsed = false; // Ensure isCollapsed is false after a stop-reset
            }
        }
    });

    amplitudeControl.addEventListener('input', (event) => {
        amplitudeValue.textContent = event.target.value;
        // If animating, simulation picks up the new value.
        // If not animating and not collapsed, just update the text.
        if (!isAnimating && !isCollapsed) {
            // Optionally update building position once to reflect new amplitude *if it were animating*
             // This might be confusing. Let's only update visuals when animating or explicitly reset/started.
        }
    });


    frequencyControl.addEventListener('input', (event) => {
        frequencyValue.textContent = event.target.value;
        // If animating, simulation picks up new frequency on next frame.
        // If not animating, no visual change needed until started.
    });

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        // Scroll to the explanation when shown?
        if (!isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

     // --- Initialization ---
     createGroundSegments(); // Create the ground segments dynamically
     resetSimulation(); // Set initial state correctly
     // --- End Initialization ---
});
</script>
```