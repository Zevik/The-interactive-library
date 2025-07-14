---
title: "אינטראקציה אטמוספרית: מודל אפקט החממה"
english_slug: greenhouse-effect-model-enhanced
category: "פיזיקה"
tags:
  - אקלים
  - פיזיקה
  - הדמיה
  - אינטראקטיבי
---
# אינטראקציה אטמוספרית: מודל אפקט החממה

דמיינו את כדור הארץ שלנו עטוף בשמיכה בלתי נראית. איך השמיכה הזו, האטמוספירה שלנו, משפיעה על הטמפרטורה שמאפשרת חיים? בואו נשחק עם אנרגיית השמש והאטמוספירה בסימולציה ויזואלית מרתקת, ונראה איך הן מנהלות ריקוד שקובע את האקלים שלנו.

<div id="simulation-container">
    <div id="space"></div>
    <div id="sun"></div>
    <div id="earth">
        <div id="surface"></div>
    </div>
    <div id="atmosphere"></div>
    <div id="temperature-display">טמפרטורה ממוצעת: <span id="temp-value"></span>°C</div>
    <div id="controls">
        <label for="ghg-slider">צפיפות שמיכת החום<br>(ריכוז גזי חממה)</label>
        <input type="range" id="ghg-slider" min="0" max="100" value="20">
        <span id="ghg-value">20%</span>
    </div>

    <!-- Radiation elements will be added dynamically by JS -->
</div>

<style>
/* Reset and general body styles */
body {
    font-family: 'Heebo', sans-serif; /* A more modern Hebrew-friendly font */
    direction: rtl;
    text-align: right;
    background: linear-gradient(to bottom, #e0f2f7, #b3e5fc); /* Light blue gradient background */
    padding: 20px;
    line-height: 1.7;
    color: #333;
    margin: 0;
}

h1 {
    color: #01579b; /* Deep blue */
    text-align: center;
    margin-bottom: 20px;
    font-size: 2em;
}

/* Simulation Container */
#simulation-container {
    position: relative;
    width: 100%;
    max-width: 680px; /* Slightly wider container */
    height: 500px; /* Taller container */
    margin: 30px auto;
    border: 1px solid #b0bec5;
    overflow: hidden;
    background: linear-gradient(to bottom, #0d47a1, #1976d2); /* Deep blue to medium blue space */
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

/* Space background elements - maybe subtle stars? */
#space {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: transparent; /* Background handled by container */
    z-index: 1;
}
/* Add stars via pseudo-elements or JS if needed - keeping it simple for now */


/* Sun */
#sun {
    position: absolute;
    top: 40px;
    left: 60px;
    width: 90px;
    height: 90px;
    background: radial-gradient(circle, #ffff8d, #ffea00); /* Brighter yellow */
    border-radius: 50%;
    box-shadow: 0 0 40px 10px rgba(255, 235, 59, 0.7); /* More prominent glow */
    z-index: 3; /* Bring sun forward slightly */
    animation: sun-pulse 3s infinite alternate; /* Subtle pulsing animation */
}

@keyframes sun-pulse {
    from { transform: scale(1); opacity: 1; }
    to { transform: scale(1.05); opacity: 0.9; }
}


/* Earth */
#earth {
    position: absolute;
    bottom: -80px; /* More of Earth visible */
    left: 50%;
    transform: translateX(-50%);
    width: 280px; /* Larger Earth */
    height: 280px;
    background: radial-gradient(circle at 30% 30%, #a5d6a7, #43a047); /* Green gradient for land */
    border-radius: 50%;
    overflow: hidden;
    z-index: 3;
    box-shadow: 0 0 50px rgba(67, 160, 71, 0.6); /* Greenish glow */
}

#surface {
     position: absolute;
     top: 60%; /* Higher water level */
     left: 0;
     width: 100%;
     height: 40%;
     background: radial-gradient(circle at 70% 70%, #81d4fa, #29b6f6); /* Blue gradient for water */
     border-radius: 0 0 140px 140px; /* Rounded bottom matching earth curve */
}

/* Atmosphere */
#atmosphere {
    position: absolute;
    bottom: 0px; /* Sits on top of Earth */
    left: 50%;
    transform: translateX(-50%);
    width: 340px; /* Wider than Earth */
    height: 180px; /* Taller layer */
    background: radial-gradient(ellipse at center, rgba(179, 229, 252, 0.3) 0%, rgba(41, 182, 246, 0.1) 70%, rgba(41, 182, 246, 0) 100%); /* Faded elliptical gradient */
    border-radius: 170px / 90px; /* Elliptical shape matching dimensions */
    z-index: 4;
    /* border: 1px solid rgba(100, 149, 237, 0.3); */ /* Remove border for softer look */
    box-shadow: 0 0 40px rgba(41, 182, 246, 0.5); /* Soft blue glow */
    animation: atmosphere-shimmer 5s infinite ease-in-out alternate; /* Subtle shimmering effect */
}

@keyframes atmosphere-shimmer {
    from { opacity: 0.8; transform: translateX(-50%) scale(1); }
    to { opacity: 1; transform: translateX(-50%) scale(1.01); }
}


/* Temperature Display */
#temperature-display {
    position: absolute;
    top: 20px;
    right: 20px;
    color: #fff; /* White text */
    font-size: 1.4em; /* Larger font */
    font-weight: bold;
    background-color: rgba(0, 0, 0, 0.6); /* Darker semi-transparent background */
    padding: 10px 15px;
    border-radius: 8px;
    z-index: 10;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    min-width: 180px; /* Ensure consistent width */
    text-align: center;
}

#temperature-display span {
    color: #ffeb3b; /* Highlight temperature value */
}


/* Controls */
#controls {
    position: absolute;
    bottom: 20px;
    right: 20px;
    background-color: rgba(255, 255, 255, 0.95); /* Almost opaque white */
    padding: 15px;
    border-radius: 8px;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 220px; /* Wider control panel */
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

#controls label {
    color: #0277bd; /* Darker blue */
    margin-bottom: 8px;
    font-size: 1em;
    font-weight: bold;
}

#controls input[type="range"] {
    width: 100%;
    margin-bottom: 5px;
    cursor: pointer;
    -webkit-appearance: none; /* Remove default styles */
    appearance: none;
    height: 8px;
    background: #bbdefb; /* Light blue track */
    outline: none;
    border-radius: 5px;
}

#controls input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #03a9f4; /* Medium blue thumb */
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    margin-top: -6px; /* Center thumb vertically */
}

#controls input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #03a9f4;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
}

#ghg-value {
    align-self: center; /* Center the percentage text */
    font-size: 1.1em;
    color: #0288d1; /* Medium blue */
    font-weight: bold;
}


/* Radiation elements */
.radiation {
    position: absolute;
    width: 6px; /* Slightly larger */
    height: 6px;
    border-radius: 50%;
    z-index: 5;
    opacity: 0.9; /* Slightly more opaque */
    filter: brightness(1.2); /* Make them brighter */
}

.radiation.solar {
    background-color: #ffeb3b; /* Bright yellow */
    box-shadow: 0 0 8px 2px rgba(255, 235, 59, 0.8); /* Glowing effect */
}

.radiation.infrared {
    background-color: #ff9800; /* Vivid orange */
    box-shadow: 0 0 8px 2px rgba(255, 152, 0, 0.8); /* Glowing effect */
}

/* Visual states for IR interaction */
.radiation.infrared-absorbed {
    background-color: #ef5350; /* Reddish-orange, visually distinct */
    box-shadow: 0 0 10px 3px rgba(239, 83, 80, 0.9);
    opacity: 1;
}

/* Optional: a subtle effect when a ray passes through */
.radiation.infrared-passthrough {
    /* No significant change, maybe a slight pulse? */
     opacity: 0.7;
}

/* Explanation styles */
#toggle-explanation {
    display: block;
    margin: 20px auto;
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    background-color: #03a9f4; /* Medium blue */
    color: white;
    border: none;
    border-radius: 8px;
    transition: background-color 0.3s ease;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

#toggle-explanation:hover {
    background-color: #0288d1; /* Darker blue on hover */
}

#explanation {
    display: none;
    max-width: 680px;
    margin: 20px auto;
    background-color: #ffffff; /* White background */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    border-top: 5px solid #03a9f4; /* Blue top border */
}

#explanation h2 {
    color: #0277bd; /* Dark blue */
    margin-top: 0;
    border-bottom: 2px solid #e0f2f7; /* Light blue separator */
    padding-bottom: 10px;
    margin-bottom: 15px;
}

#explanation p {
    margin-bottom: 15px;
    color: #555;
}

#explanation ol {
    margin-bottom: 15px;
    padding-right: 20px;
    color: #555;
}

#explanation li {
    margin-bottom: 8px;
}

#explanation strong {
    color: #0288d1; /* Medium blue */
}

</style>

<button id="toggle-explanation">הצג הסבר על אפקט החממה</button>

<div id="explanation" style="display: none;">
    <h2>ריקוד האנרגיה: אפקט החממה בפעולה</h2>
    <p>אפקט החממה הוא לא דבר "רע" מטבעו – הוא תהליך טבעי שהופך את כדור הארץ למקום שאפשר לחיות בו! האטמוספירה שלנו מתנהגת כמו שמיכה דקה, לוכדת מספיק חום כדי לשמור על טמפרטורה ממוצעת נוחה, במקום שהכל יהיה קפוא.</p>
    <p>הסימולציה כאן מדגימה את ה"איך":</p>
    <ol>
        <li><strong>קרני השמש (צהובות):</strong> אנרגיה עוצמתית מגיעה מהשמש ב"מנות" קטנות (בעיקר אור), ורובה הגדול עובר בקלות דרך האטמוספירה השקופה יחסית עבורה.</li>
        <li><strong>כדור הארץ מתחמם ופולט:</strong> פני כדור הארץ (יבשה ומים) בולעים חלק מהאנרגיה הזו ומתחממים. כגוף חם, כדור הארץ חייב לפלוט אנרגיה בחזרה, אבל הוא עושה זאת בצורה שונה – כ"קרני חום" אינפרה-אדום (אדום/כתום), שהן פחות אנרגטיות מאור השמש.</li>
        <li><strong>השמיכה התרמית (אטמוספירה):</strong> שכבת האטמוספירה אמנם דקה, אבל היא מכילה מולקולות מיוחדות שנקראות "גזי חממה" (כמו פחמן דו-חמצני, מתאן, אדי מים). מולקולות אלו <strong>מאוד טובות בבליעת</strong> קרני החום האינפרה-אדום שכדור הארץ פולט.</li>
        <li><strong>לכידה ושחרור:</strong> כשמולקולת גז חממה בולעת קרן חום, היא "מתרגשת" לרגע ואז פולטת את האנרגיה שוב - אבל <strong>לכל הכיוונים באקראי!</strong> חלק מהאנרגיה נפלטת לחלל (טוב!), אבל חלק משמעותי <strong>נפלט חזרה כלפי מטה</strong>, אל פני כדור הארץ והשכבות התחתונות של האטמוספירה.</li>
    </ol>
    <p>קרני החום שחוזרות כלפי מטה "נתקעות" במערכת, וזה מוסיף אנרגיה ומעלה את הטמפרטורה. ככל שנגביר את צפיפות שמיכת החום (נשנה את המחוון לגז חממה גבוה יותר), כך גדל הסיכוי שקרני החום ייבלעו באטמוספירה וייפלטו חזרה מטה. יותר קרני חום חוזרות מטה = יותר אנרגיה נלכדת = טמפרטורה גבוהה יותר.</p>
</div>


<script>
const simulationContainer = document.getElementById('simulation-container');
const ghgSlider = document.getElementById('ghg-slider');
const ghgValueSpan = document.getElementById('ghg-value');
const tempValueSpan = document.getElementById('temp-value');
const explanationDiv = document.getElementById('explanation');
const toggleExplanationButton = document.getElementById('toggle-explanation');
const atmosphereElement = document.getElementById('atmosphere');

// Simulation constants and parameters
const SUN_POS = { x: 105, y: 85 }; // Center of sun
const EARTH_CENTER_X = simulationContainer.offsetWidth / 2;
const EARTH_SURFACE_Y = simulationContainer.offsetHeight - 80 - (280/2) + (280*0.6) ; // Approximate Y level of visible Earth surface
const ATMOSPHERE_INTERACTION_Y_MIN = simulationContainer.offsetHeight - 80 - 180 ; // Bottom of atmosphere
const ATMOSPHERE_INTERACTION_Y_MAX = simulationContainer.offsetHeight - 80 - 180 + 180; // Top of atmosphere

const RADIATION_SPEED_MS = 2000; // Duration in ms for a typical ray travel
const SOLAR_EMISSION_INTERVAL = 3000; // Interval for bursts of solar rays
const INFRARED_EMISSION_INTERVAL = 800; // Interval for bursts of infrared rays (more frequent)
const SOLAR_RAY_COUNT = 4;
const INFRARED_RAY_COUNT = 6; // More IR rays emitted initially

// Temperature mapping (simplified)
const BASE_TEMP_NO_GHG = -18; // Approx temperature without greenhouse effect
const TEMP_PER_100_GHG = 38; // Approx temperature increase for max GHG (makes it ~20°C)

// Function to create and animate a radiation ray
function createRadiation(type, startX, startY, endX, endY, duration, ghgAbsorptionChance = 0) {
    const radiation = document.createElement('div');
    radiation.classList.add('radiation', type);
    simulationContainer.appendChild(radiation);

    // Set initial position
    radiation.style.left = `${startX}px`;
    radiation.style.top = `${startY}px`;

    // Use WAAPI for animation
    const animation = radiation.animate([
        { left: `${startX}px`, top: `${startY}px`, opacity: type === 'infrared-absorbed' ? 1 : 0.9 }, // Start with higher opacity if absorbed
        { left: `${endX}px`, top: `${endY}px`, opacity: 0.1 } // Fade out slightly at the end
    ], {
        duration: duration,
        iterations: 1,
        easing: 'linear'
    });

    animation.onfinish = () => {
        radiation.remove(); // Clean up the element
    };

    // Interaction logic only for infrared rays moving upwards
    if (type === 'infrared' && endY < startY) {
        // Check if the ray path intersects the atmosphere band
        const intersectsAtmosphereBand = (startY > ATMOSPHERE_INTERACTION_Y_MIN && startY < ATMOSPHERE_INTERACTION_Y_MAX) || // Starts within
                                         (endY > ATMOSPHERE_INTERACTION_Y_MIN && endY < ATMOSPHERE_INTERACTION_Y_MAX) || // Ends within
                                         (startY > ATMOSPHERE_INTERACTION_Y_MAX && endY < ATMOSPHERE_INTERACTION_Y_MIN) || // Crosses downwards
                                         (startY < ATMOSPHERE_INTERACTION_Y_MIN && endY > ATMOSPHERE_INTERACTION_Y_MAX) ; // Crosses upwards

        if (intersectsAtmosphereBand) {
            // Calculate approximate intersection time/position with the core atmosphere interaction level (simplified to a Y band)
             // Find the points where the line segment crosses the min and max Y of the atmosphere band
            const intersectionPoints = [];

            // Check intersection with the top boundary (ATMOSPHERE_INTERACTION_Y_MIN)
            if ((startY <= ATMOSPHERE_INTERACTION_Y_MIN && endY >= ATMOSPHERE_INTERACTION_Y_MIN) || (startY >= ATMOSPHERE_INTERACTION_Y_MIN && endY <= ATMOSPHERE_INTERACTION_Y_MIN)) {
                const t = (ATMOSPHERE_INTERACTION_Y_MIN - startY) / (endY - startY);
                if (t >= 0 && t <= 1) {
                     intersectionPoints.push({ t: t, y: ATMOSPHERE_INTERACTION_Y_MIN });
                }
            }
             // Check intersection with the bottom boundary (ATMOSPHERE_INTERACTION_Y_MAX)
             if ((startY <= ATMOSPHERE_INTERACTION_Y_MAX && endY >= ATMOSPHERE_INTERACTION_Y_MAX) || (startY >= ATMOSPHERE_INTERACTION_Y_MAX && endY <= ATMOSPHERE_INTERACTION_Y_MAX)) {
                const t = (ATMOSPHERE_INTERACTION_Y_MAX - startY) / (endY - startY);
                 if (t >= 0 && t <= 1) {
                     intersectionPoints.push({ t: t, y: ATMOSPHERE_INTERACTION_Y_MAX });
                 }
            }

            // Find the earliest intersection point if multiple exist
            if (intersectionPoints.length > 0) {
                 const firstIntersection = intersectionPoints.reduce((min, p) => p.t < min.t ? p : min, intersectionPoints[0]);
                 const intersectionTime = firstIntersection.t * duration;
                 const intersectionY = firstIntersection.y;
                 const intersectionX = startX + (endX - startX) * firstIntersection.t;

                 // Set a timeout to trigger interaction when the ray reaches the atmosphere visually
                 setTimeout(() => {
                    // Check if the ray still exists (wasn't removed by another interaction)
                    if (simulationContainer.contains(radiation)) {
                         triggerAtmosphereInteraction(radiation, intersectionX, intersectionY, ghgAbsorptionChance);
                    }
                 }, intersectionTime);
            }
        }
    } else if (type === 'solar' && endY > startY) {
         // Solar rays hitting Earth - no special interaction shown currently, they just disappear.
         // Could add a visual "hit" effect on Earth later if desired.
    }
}

// Function to handle the absorption/re-emission logic
function triggerAtmosphereInteraction(radiationElement, interactionX, interactionY, absorptionChance) {
    // Stop the original animation
    radiationElement.getAnimations().forEach(anim => anim.cancel());

    if (Math.random() < absorptionChance) {
        // ABSORBED!
        // Visually mark the ray as absorbed
        radiationElement.classList.remove('infrared');
        radiationElement.classList.add('infrared-absorbed');

        // Keep the absorbed element briefly at the interaction point
        radiationElement.style.left = `${interactionX}px`;
        radiationElement.style.top = `${interactionY}px`;
        radiationElement.style.width = '8px'; // Make it slightly larger
        radiationElement.style.height = '8px';
        radiationElement.style.opacity = 1;


        // Re-emit rays after a short visual delay
        const reEmitDelay = 100; // ms
        const reEmitDuration = RADIATION_SPEED_MS * 0.6; // Re-emitted rays travel faster

        setTimeout(() => {
             radiationElement.remove(); // Remove the absorbed visual


            // Re-emit 2 new rays from the interaction point
            // Ray 1: Upwards to space
            const endX_up = interactionX + (Math.random() - 0.5) * 300;
            const endY_up = interactionY - 300;
            createRadiation('infrared', interactionX, interactionY, endX_up, endY_up, reEmitDuration);

            // Ray 2: Downwards to Earth
            const endX_down = interactionX + (Math.random() - 0.5) * 150;
            const endY_down = EARTH_SURFACE_Y + (Math.random() - 0.5) * 50; // Aim towards Earth surface area
            createRadiation('infrared', interactionX, interactionY, endX_down, endY_down, reEmitDuration);

        }, reEmitDelay);

    } else {
        // PASSED THROUGH
        // Let the original ray continue its path from the interaction point
        const originalEndKeyframe = radiationElement.getAnimations()[0]?.effect?.getKeyframes().pop();
         if (originalEndKeyframe) {
             const endX = parseFloat(originalEndKeyframe.left);
             const endY = parseFloat(originalEndKeyframe.top);

             // Calculate remaining duration
             const totalDuration = radiationElement.getAnimations()[0].duration;
             const elapsed = radiationElement.getAnimations()[0].currentTime;
             const remainingDuration = totalDuration - elapsed;


             radiationElement.animate([
                 { left: `${interactionX}px`, top: `${interactionY}px`, opacity: 0.9 },
                 { left: `${endX}px`, top: `${endY}px`, opacity: 0.1 }
             ], {
                 duration: remainingDuration,
                 iterations: 1,
                 easing: 'linear'
             }).onfinish = () => radiationElement.remove(); // Ensure it's removed when done

             radiationElement.classList.add('infrared-passthrough'); // Visual cue for pass-through
         } else {
              // Fallback if animation data is somehow missing
             radiationElement.remove();
         }
    }
}


// Emission functions
function emitSolarRadiation() {
    const sunCenterX = SUN_POS.x;
    const sunCenterY = SUN_POS.y;

    for (let i = 0; i < SOLAR_RAY_COUNT; i++) {
        // Emit rays towards the Earth's visible area
        const targetAngle = Math.PI/2 - 0.3 + i * (0.6 / (SOLAR_RAY_COUNT - 1)); // Angle range towards Earth
        const targetDistance = Math.random() * 100 + 250; // Distance from sun center
        const targetX = sunCenterX + Math.cos(targetAngle) * targetDistance;
        const targetY = sunCenterY + Math.sin(targetAngle) * targetDistance;

        // Vary end point slightly around Earth
        const finalTargetX = EARTH_CENTER_X + (i - (SOLAR_RAY_COUNT-1)/2) * 40 + (Math.random() - 0.5) * 30;
        const finalTargetY = EARTH_SURFACE_Y + (Math.random() - 0.5) * 20;

        createRadiation('solar', sunCenterX, sunCenterY, finalTargetX, finalTargetY, RADIATION_SPEED_MS);
    }
}

function emitInfrared() {
    // Emit rays outwards from the Earth's upper surface area
    const earthRadius = 140; // Approx visual radius
    const startAngleRad = Math.PI * 0.1; // Start above horizontal
    const endAngleRad = Math.PI * 0.9; // End above horizontal
    const angleStep = (endAngleRad - startAngleRad) / (INFRARED_RAY_COUNT - 1);

    const ghgLevel = parseInt(ghgSlider.value);
    const absorptionChance = ghgLevel / 100; // 0% to 100% absorption chance

    for (let i = 0; i < INFRARED_RAY_COUNT; i++) {
        const currentAngle = startAngleRad + i * angleStep;
        // Start position slightly above the theoretical Earth surface circle
        const startX = EARTH_CENTER_X + Math.cos(currentAngle) * (earthRadius - 20) + (Math.random() - 0.5) * 30;
        const startY = EARTH_CENTER_Y + Math.sin(currentAngle) * (earthRadius - 20) - 50 + (Math.random() - 0.5) * 20; // Adjusted Y for visible surface

        // End points going upwards and outwards into space
        const endAngle = currentAngle + (Math.random() - 0.5) * 0.5; // Vary angle
        const endDistance = 400 + Math.random() * 100; // Travel distance
        const endX = startX + Math.cos(endAngle - Math.PI/2) * endDistance; // Adjust angle for upward direction
        const endY = startY + Math.sin(endAngle - Math.PI/2) * endDistance; // Adjust angle for upward direction


        const duration = RADIATION_SPEED_MS * (1 + Math.random() * 0.5); // Vary duration

        // Create the infrared ray; interaction logic is within createRadiation
        createRadiation('infrared', startX, startY, endX, endY, duration, absorptionChance);
    }
}

// Update temperature display based on GHG slider value
function updateTemperatureDisplay(ghgValue) {
    // Map GHG value (0-100) to temperature range (-18 to ~20)
    const currentTemp = BASE_TEMP_NO_GHG + (ghgValue / 100) * TEMP_PER_100_GHG;
    tempValueSpan.textContent = currentTemp.toFixed(1); // Show one decimal place
    ghgValueSpan.textContent = `${ghgValue}%`; // Update percentage text
}

// Start the simulation intervals
let solarInterval;
let infraredInterval;

function startSimulation() {
    // Clear any existing intervals
    clearInterval(solarInterval);
    clearInterval(infraredInterval);

    // Periodically emit radiation bursts
    solarInterval = setInterval(emitSolarRadiation, SOLAR_EMISSION_INTERVAL);
    infraredInterval = setInterval(emitInfrared, INFRARED_EMISSION_INTERVAL); // More frequent IR

    // Initial temperature and GHG display update
    updateTemperatureDisplay(parseInt(ghgSlider.value));
}

// Event listener for the slider input (fires continuously while sliding)
ghgSlider.addEventListener('input', (event) => {
    const ghgValue = parseInt(event.target.value);
    updateTemperatureDisplay(ghgValue);
    // The interaction logic for active IR rays will use the *current* slider value
    // when they reach the atmosphere band, so we don't need to restart intervals here.
});

// Event listener for the explanation button
toggleExplanationButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על אפקט החממה' : 'הצג הסבר על אפקט החממה';
     // Scroll to explanation if showing it
     if (isHidden) {
        explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
     }
});


// Initial setup
// Need to wait for DOM to be ready to calculate element positions correctly
document.addEventListener('DOMContentLoaded', () => {
    // Recalculate positions after DOM is loaded and dimensions are set
    // (Although fixed pixel values are used, slight variations might occur,
    // this is more robust for future layout changes)
    const containerRect = simulationContainer.getBoundingClientRect();
    EARTH_CENTER_X = containerRect.width / 2;
    // Re-calculate EARTH_SURFACE_Y and ATMOSPHERE_INTERACTION_Y values relative to the container's top
    // Assuming the bottom of the earth div is 80px below the container bottom
    // Earth height is 280px. Surface starts at 60% of Earth height.
    // Container Height - 80 (offset) - (280 * 0.4) (distance from earth bottom to surface start)
    EARTH_SURFACE_Y = containerRect.height - 80 - (280 * 0.4);

    // Atmosphere bottom is at 0px from container bottom. Height is 180px.
    ATMOSPHERE_INTERACTION_Y_MIN = containerRect.height - 180; // Top of atmosphere layer
    ATMOSPHERE_INTERACTION_Y_MAX = containerRect.height; // Bottom of atmosphere layer (aligns with container bottom)


    startSimulation(); // Start the intervals
});


</script>