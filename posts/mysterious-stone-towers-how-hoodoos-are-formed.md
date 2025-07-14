---
title: "מסע אל מגדלי האבן הקסומים: סוד היווצרות 'ארובות הפיות'"
english_slug: mysterious-stone-towers-how-hoodoos-are-formed
category: "מדעי הסביבה / גיאולוגיה"
tags: [גאולוגיה, בלייה, סחיפה, גאומורפולוגיה, ארובות פיות, עיצוב נוף]
---
# מסע אל מגדלי האבן הקסומים: סוד היווצרות "ארובות הפיות"

דמיינו נוף פראי, צחיח, ובו עומדים עמודי סלע גבוהים וצרים, עטורי "כובעים" סלע קשה יותר. איך הטבע מפסל צורות כל כך מפעימות? מה מגן על קודקודם בזמן שהסלע שמסביב נעלם כלא היה? הצטרפו אלינו למסע מרתק במעבה האדמה (תרתי משמע!) וגלו את הקסם הגאולוגי שמאחורי התופעה המרהיבה הזו, המכונה "ארובות פיות".

<div id="simulation-container">
    <div id="simulation-area">
        <div class="ground-layer"></div> <!-- Added for visual ground line -->
        <div id="surrounding-rock-left" class="rock surrounding"></div>
        <div id="hoodoo-area">
            <div id="caprock" class="rock hoodoo-part"></div>
            <div id="soft-rock" class="rock hoodoo-part"></div>
             <!-- Optional: Add an element for dust/crumbling effect -->
             <div id="collapse-dust"></div>
        </div>
        <div id="surrounding-rock-right" class="rock surrounding"></div>
    </div>
    <div id="controls">
        <button id="play-pause-button">התחל מסע בזמן</button>
        <button id="reset-button">אפס למצב התחלתי</button>
        <label for="time-slider">התקדמות הזמן הגאולוגי:</label>
        <input type="range" id="time-slider" min="0" max="100" value="0">
        <span id="current-time-display">0</span> יחידות זמן
    </div>
</div>

<style>
#simulation-container {
    width: 100%;
    max-width: 700px; /* Slightly wider container */
    margin: 30px auto;
    border: none; /* Remove border */
    border-radius: 12px; /* Rounded corners */
    padding: 25px; /* More padding */
    background: linear-gradient(to bottom right, #f8f8f8, #e8e8e8); /* Subtle gradient background */
    text-align: center;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2); /* Enhanced shadow */
    overflow: hidden; /* Hide overflow from shadow/border-radius */
    font-family: 'Arial', sans-serif; /* Modern font */
}

#simulation-area {
    display: flex;
    align-items: flex-end;
    height: 350px; /* Taller simulation area */
    background: linear-gradient(to top, #c3eaff, #aaddff); /* Sky gradient */
    position: relative;
    overflow: hidden;
    border-radius: 8px; /* Rounded corners for simulation area */
    box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow */
}

.ground-layer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 30px; /* Visual ground height */
    background: linear-gradient(to top, #a0522d, #8b4513); /* Earth gradient */
    z-index: 0; /* Ensure ground is behind rocks */
}

.rock {
    position: absolute;
    bottom: 30px; /* Rocks sit on the ground layer */
    transition: height 0.4s ease-out, width 0.4s ease-out, background-color 0.4s ease-out, opacity 0.4s ease-out; /* Smooth transitions for changes */
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1); /* Subtle shadow on rocks */
}

.rock.surrounding {
    width: 35%;
    height: calc(100% - 30px); /* Initially fill height above ground */
    background: linear-gradient(to top, #d2b48c, #8b4513); /* Varied brown/earth texture */
}

#surrounding-rock-left {
    left: 0;
}

#surrounding-rock-right {
    right: 0;
}

#hoodoo-area {
    width: 30%;
    height: calc(100% - 30px); /* Same height as surrounding rocks above ground */
    position: absolute;
    left: 35%;
    bottom: 30px;
    display: flex;
    flex-direction: column-reverse; /* Stack from bottom */
    align-items: center; /* Center hoodoo parts */
    justify-content: flex-end; /* Align parts to the bottom within hoodoo-area */
    /* overflow: hidden; */ /* Needed if soft rock width exceeds hoodoo-area width initially */
    z-index: 1; /* Ensure hoodoo is above ground and maybe slighty above surroundings visually */
}

#soft-rock {
    width: 90%; /* Start slightly wider, imagine it's part of a continuous layer */
    height: 90%; /* Initial height relative to hoodoo-area height */
    background: linear-gradient(to top, #e0c9a6, #d2b48c); /* Lighter, erodible rock color */
    border-radius: 3px 3px 0 0; /* Slightly rounded top corners */
    position: relative; /* For potential inner elements or effects */
    flex-shrink: 0; /* Prevent shrinking in flex container */
    margin-bottom: -1px; /* Prevent small gap if heights don't align perfectly */
}

#caprock {
    width: 100%; /* Initially covers the width of hoodoo-area */
    height: 10%; /* Initial height */
    background: linear-gradient(to top, #7a3f1f, #a0522d); /* Darker, harder rock color */
    border-radius: 5px 5px 3px 3px; /* Rounded cap corners */
    z-index: 2; /* Ensure cap is on top */
    flex-shrink: 0;
}

/* State classes for simulation area */
#simulation-area.collapsing .hoodoo-part {
    opacity: 0.2; /* Fade out hoodoo parts */
    transform: scale(0.95); /* Slight shake/shrink effect */
    transition: opacity 0.5s ease-out, transform 0.5s ease-out;
}

#simulation-area.collapsed .hoodoo-part {
    display: none; /* Hide collapsed hoodoo */
}

#collapse-dust {
     position: absolute;
     bottom: 30px; /* Above ground */
     left: 35%; /* Centered under hoodoo-area */
     width: 30%; /* Same width as hoodoo-area */
     height: calc(100% - 30px);
     background: radial-gradient(circle, rgba(139, 69, 19, 0.5) 0%, rgba(139, 69, 19, 0) 70%); /* Brown radial gradient for dust */
     opacity: 0; /* Hidden initially */
     pointer-events: none; /* Don't interfere with clicks */
     transition: opacity 0.5s ease-out;
     z-index: 3; /* Above other rocks */
}

#simulation-area.collapsing #collapse-dust {
    opacity: 1; /* Show dust */
}

#simulation-area.collapsed #collapse-dust {
     opacity: 0; /* Fade out dust after animation */
}


#controls {
    margin-top: 25px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    flex-wrap: wrap;
    padding: 0 10px; /* Add horizontal padding */
}

#time-slider {
    flex-grow: 1;
    max-width: 350px; /* Wider slider */
    -webkit-appearance: none; /* Remove default styling */
    appearance: none;
    height: 8px;
    background: #ddd;
    outline: none;
    opacity: 0.8;
    transition: opacity .2s;
    border-radius: 4px;
}

#time-slider:hover {
    opacity: 1;
}

#time-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#time-slider::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}


button {
    padding: 10px 18px; /* More padding */
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px; /* More rounded */
    font-size: 1rem; /* Slightly larger font */
    transition: background-color 0.2s ease, transform 0.1s ease; /* Smooth hover/active */
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

button:hover {
    background-color: #0056b3;
}

button:active {
    transform: scale(0.98); /* Visual press effect */
}

#reset-button {
    background-color: #dc3545; /* Red color for reset */
}
#reset-button:hover {
    background-color: #c82333;
}


#current-time-display {
    font-weight: bold;
    min-width: 20px; /* Prevent text jump */
    display: inline-block;
}

#toggle-explanation {
     display: block; /* Make it a block element */
     margin: 30px auto 15px auto; /* Center it, add space */
     padding: 12px 20px;
     background-color: #6c757d; /* Grey color */
     color: white;
     border: none;
     border-radius: 5px;
     cursor: pointer;
     font-size: 1rem;
     transition: background-color 0.2s ease;
     box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#toggle-explanation:hover {
    background-color: #5a6268;
}


#explanation {
    margin-top: 30px;
    border-top: 1px solid #ccc;
    padding-top: 20px;
    text-align: right; /* Right-to-left text */
    line-height: 1.7; /* More space between lines */
    color: #333; /* Darker text */
}

#explanation h2 {
    text-align: center;
    color: #0056b3; /* Blue heading */
    margin-bottom: 20px;
}

#explanation p {
    margin-bottom: 15px;
}

/* Responsive adjustments */
@media (max-width: 600px) {
    #simulation-container {
        padding: 15px;
    }
    #simulation-area {
        height: 280px;
    }
    #controls {
        flex-direction: column;
        gap: 10px;
    }
    #time-slider {
        width: 95%;
        max-width: none;
    }
    button {
        width: 95%; /* Full width buttons */
        max-width: 250px; /* Max width for buttons */
    }
     #toggle-explanation {
         width: 95%;
         max-width: 250px;
     }
}

</style>

<button id="toggle-explanation">הצג הסבר מלא</button>

<div id="explanation" style="display: none;">
    <h2>הסבר גאולוגי: כך נולדות ארובות הפיות</h2>
    <p>ארובות פיות (Hoodoos) הן תצורות סלע מרהיבות, דמויות עמודים גבוהים וצרים, הנפוצות במיוחד באזורים יבשים או מדבריים עם שכבות סלע משתנות, כמו ברייס קניון שבארה"ב. הן עדות חיה לכוחם הבלתי פוסק של תהליכי הטבע הפועלים במשך מיליוני שנים.</p>

    <h3>השלב ההתחלתי: שכבות של סיפור</h3>
    <p>הכל מתחיל באזורים בהם קיימות שכבות סלע שונות זו על גבי זו. לרוב, אלו שכבות רכות יותר (כמו אבן חול או אבן בוץ) מכוסות בשכבה עליונה קשה ועמידה יותר, הנקראת "סלע כיפה" (Caprock). סלע הכיפה משמש כמגן טבעי.</p>

    <h3>פעולת הטבע הפיסולית: בלייה וסחיפה</h3>
    <p>כוחות הטבע, בעיקר מים (גשם, קפאון-הפשרה) ורוח, פועלים ללא הרף על פני השטח. תהליך ה"בלייה" מפורר את הסלע במקומו, וה"סחיפה" מסירה את החלקיקים המפוררים. המפתח לארובות הפיות הוא ששני התהליכים הללו פועלים בקצב שונה על סוגי סלע שונים - זה נקרא "בלייה וסחיפה דיפרנציאלית".</p>

    <h3>היווצרות העמוד המוגן</h3>
    <p>הסלע הרך שמסביב לאזור המיועד לארובת פיה נשחק ונסחף בקצב מהיר יחסית. לעומתו, סלע הכיפה העליון, בהיותו קשה יותר, מתבלה ונסחף לאט מאוד. החשוב מכל: סלע הכיפה מספק הגנה לשכבת הסלע הרך שמתחתיו מפני פגיעה ישירה של גשם ורוח. בזמן שהסלע החשוף מסביב נשחק ומפלסו יורד משמעותית, הסלע הרך שמתחת ל"כובע" נשחק בקצב אטי בהרבה. כך נוצר בהדרגה עמוד סלע צר מתחת לסלע הכיפה, הולך ומתרומם מעל השטח שמסביב.</p>

    <h3>גורל הארובה: לא לנצח</h3>
    <p>ארובות פיות אינן מבנים קבועים. הן ממשיכות להתבלות ולהישחק לאורך זמן. סלע הכיפה עצמו נשחק אט אט, ובסופו של דבר יכול להישבר או ליפול. ברגע שסלע הכיפה נופל, הסלע הרך שנותר חשוף מאבד את הגנתו ונשחק במהירות מסחררת. ללא התמיכה וההגנה של הכיפה, עמוד הסלע הצר קורס לבסוף, ותצורת ארובת הפיה נעלמת, הופכת לחלק ממסע הסחיפה האינסופי של הטבע.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const softRock = document.getElementById('soft-rock');
    const caprock = document.getElementById('caprock');
    const surroundingLeft = document.getElementById('surrounding-rock-left');
    const surroundingRight = document.getElementById('surrounding-rock-right');
    const simulationArea = document.getElementById('simulation-area');
    const playPauseButton = document.getElementById('play-pause-button');
    const resetButton = document.getElementById('reset-button'); // Get the new reset button
    const timeSlider = document.getElementById('time-slider');
    const currentTimeDisplay = document.getElementById('current-time-display');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const collapseDust = document.getElementById('collapse-dust'); // Get dust element


    // Store initial dimensions after DOM load and CSS applied
    // Use clientHeight/clientWidth or offsetHeight/offsetWidth depending on exact need, offset includes borders/padding
    // Let's use offsetHeight/offsetWidth for simplicity matching the original
    let initialSoftRockHeight;
    let initialSoftRockWidth;
    let initialCaprockHeight;
    let initialCaprockWidth;
    let initialSurroundingHeight;
    let initialSimulationAreaHeight; // Total simulation height above ground

    // Erosion rates (percentage reduction of initial dimension per simulation step, scaled by timeRatio)
    // Max time is 100 steps (slider max)
    const erosionRateSurroundingHeight = 0.95; // Surrounding loses 95% height over 100 steps
    const erosionRateSoftRockProtectedHeight = 0.5; // Soft rock under cap loses 50% height
    const erosionRateSoftRockWidth = 0.7; // Soft rock loses 70% width (sides erode faster)
    const erosionRateCaprockHeight = 0.15; // Caprock loses 15% height
    const erosionRateCaprockWidth = 0.2; // Caprock loses 20% width (edges chip)

    let simulationTime = 0;
    let simulationInterval = null;
    const maxSimulationTime = 100; // Corresponds to slider max value

    function updateSimulationFromTime(time) {
         const timeRatio = time / maxSimulationTime; // 0 to 1

         // Retrieve initial dimensions from data attributes
         const initialSRH = parseFloat(surroundingLeft.dataset.initialHeight);
         const initialSRW = parseFloat(softRock.dataset.initialWidth);
         const initialSNH = parseFloat(softRock.dataset.initialHeight);
         const initialCRH = parseFloat(caprock.dataset.initialHeight);
         const initialCRW = parseFloat(caprock.dataset.initialWidth);
         // const initialSAH = parseFloat(simulationArea.dataset.initialHeight); // Not needed for calculation, just reference

         // Calculate current dimensions based on initial size and erosion rate scaled by time
         const erodedSurroundingHeight = initialSRH * (1 - timeRatio * erosionRateSurroundingHeight);
         const erodedSoftRockHeight = initialSNH * (1 - timeRatio * erosionRateSoftRockProtectedHeight);
         const erodedSoftRockWidth = initialSRW * (1 - timeRatio * erosionRateSoftRockWidth);
         const erodedCaprockHeight = initialCRH * (1 - timeRatio * erosionRateCaprockHeight);
         const erodedCaprockWidth = initialCRW * (1 - timeRatio * erosionRateCaprockWidth);

         // Apply new dimensions, ensuring they don't go below a minimum visible size
         const minVisibleHeight = 5; // pixels
         const minVisibleWidth = 5; // pixels
         const minCaprockWidth = initialCRW * 0.2; // Cap must retain at least 20% width to be effective

         surroundingLeft.style.height = Math.max(minVisibleHeight, erodedSurroundingHeight) + 'px';
         surroundingRight.style.height = Math.max(minVisibleHeight, erodedSurroundingHeight) + 'px';

         // Ensure soft rock height doesn't exceed the height of the hoodoo area container minus caprock height
         const currentCaprockHeight = Math.max(minVisibleHeight, erodedCaprockHeight); // Use calculated caprock height
         const hoodooAreaHeight = parseFloat(hoodooArea.dataset.initialHeight); // Use initial hoodoo area height above ground
         const maxSoftRockHeight = hoodooAreaHeight - currentCaprockHeight;

         softRock.style.height = Math.max(minVisibleHeight, Math.min(maxSoftRockHeight, erodedSoftRockHeight)) + 'px';
         softRock.style.width = Math.max(minVisibleWidth, erodedSoftRockWidth) + 'px';

         caprock.style.height = currentCaprockHeight + 'px';
         caprock.style.width = Math.max(minCaprockWidth, erodedCaprockWidth) + 'px';

         // Check for collapse conditions: Soft rock too short OR Caprock too small/gone
         const collapseThresholdHeight = initialSNH * 0.1; // Collapse if soft rock height is < 10% of original
         const collapseThresholdCapWidth = initialCRW * 0.15; // Collapse if caprock width is < 15% of original

         if (softRock.offsetHeight <= collapseThresholdHeight || caprock.offsetWidth <= collapseThresholdCapWidth) {
              if (!simulationArea.classList.contains('collapsed') && !simulationArea.classList.contains('collapsing')) {
                  pauseSimulation();
                  simulationArea.classList.add('collapsing'); // Start collapsing animation
                  // After animation, add 'collapsed' class to potentially hide elements entirely
                   setTimeout(() => {
                       simulationArea.classList.add('collapsed');
                       // You could hide elements here if not handled by CSS .collapsed
                       softRock.style.opacity = 0;
                       caprock.style.opacity = 0;
                   }, 500); // Match CSS transition duration
               }
          } else {
               // If somehow conditions reverse (e.g. scrubbing slider back), remove collapse state
               simulationArea.classList.remove('collapsing', 'collapsed');
               softRock.style.opacity = 1;
               caprock.style.opacity = 1;
          }
     }

    function stepSimulation() {
         simulationTime += 1;
         if (simulationTime > maxSimulationTime) {
             simulationTime = maxSimulationTime;
             pauseSimulation();
         }
         updateSimulationFromTime(simulationTime);
         timeSlider.value = simulationTime;
         currentTimeDisplay.textContent = simulationTime;
    }

     function startSimulation() {
        if (simulationInterval === null) {
            if (simulationTime >= maxSimulationTime) {
                 // If at the end, reset before starting
                 resetSimulation();
            }
            simulationInterval = setInterval(stepSimulation, 150); // Slower step for better visualization
            playPauseButton.textContent = 'השהה מסע';
        }
    }

    function pauseSimulation() {
        clearInterval(simulationInterval);
        simulationInterval = null;
        playPauseButton.textContent = 'המשך מסע';
    }

    function resetSimulation() {
        pauseSimulation();
        simulationTime = 0;
        timeSlider.value = 0;
        currentTimeDisplay.textContent = 0;

        // Reset element dimensions using stored initial values
        softRock.style.height = softRock.dataset.initialHeight + 'px';
        softRock.style.width = softRock.dataset.initialWidth + 'px';
        caprock.style.height = caprock.dataset.initialHeight + 'px';
        caprock.style.width = caprock.dataset.initialWidth + 'px';
        surroundingLeft.style.height = surroundingLeft.dataset.initialHeight + 'px';
        surroundingRight.style.height = surroundingRight.dataset.initialHeight + 'px';

        // Ensure opacity is 1 if it was set to 0 during collapse
        softRock.style.opacity = 1;
        caprock.style.opacity = 1;
        // Remove collapse classes
        simulationArea.classList.remove('collapsing', 'collapsed');

        playPauseButton.textContent = 'התחל מסע בזמן';
        // Update display to the initial state
        updateSimulationFromTime(0);
    }


    timeSlider.addEventListener('input', (event) => {
        pauseSimulation(); // Pause automatic simulation when user interacts
        simulationTime = parseInt(event.target.value);
        currentTimeDisplay.textContent = simulationTime;
        updateSimulationFromTime(simulationTime); // Update display to match slider time
         // playPauseButton.textContent = 'התחל מסע בזמן'; // Or maybe 'המשך מסע' if time < max
         // Decision: Keep "התחל מסע בזמן" until play is pressed, then it becomes "השהה"
         if (simulationTime < maxSimulationTime) {
              playPauseButton.textContent = 'התחל מסע בזמן';
         } else {
               playPauseButton.textContent = 'המסע הסתיים (אפס)'; // Indicate end state
         }

    });

    playPauseButton.addEventListener('click', () => {
        if (simulationInterval === null) {
            startSimulation();
        } else {
            pauseSimulation();
        }
    });

    // Add event listener for the reset button
     resetButton.addEventListener('click', resetSimulation);


    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג הסבר מלא';
    });

    // --- Initial Setup ---
    // Get and store initial dimensions after DOM is ready and styles are applied
    // Get hoodoo area height above ground for max soft rock height calculation later
    const hoodooArea = document.getElementById('hoodoo-area');
    hoodooArea.dataset.initialHeight = hoodooArea.offsetHeight;

    initialSoftRockHeight = softRock.offsetHeight;
    initialSoftRockWidth = softRock.offsetWidth;
    initialCaprockHeight = caprock.offsetHeight;
    initialCaprockWidth = caprock.offsetWidth;
    initialSurroundingHeight = surroundingLeft.offsetHeight;

    // Store these initial dimensions as data attributes
     softRock.dataset.initialHeight = initialSoftRockHeight;
     softRock.dataset.initialWidth = initialSoftRockWidth;
     caprock.dataset.initialHeight = initialCaprockHeight;
     caprock.dataset.initialWidth = initialCaprockWidth;
     surroundingLeft.dataset.initialHeight = initialSurroundingHeight;
     surroundingRight.dataset.initialHeight = initialSurroundingHeight;
     // simulationArea.dataset.initialHeight = simulationArea.offsetHeight; // Store total simulation height

    // Set initial state based on slider default (0)
    updateSimulationFromTime(0);
});

</script>
---
```