---
title: "דיו טבעי: מסע לתוך ייצור דיו הספיה מתמנונים"
english_slug: natural-ink-sepia-production-from-octopuses
category: "מדעי החיים / ביולוגיה"
tags: ["דיו ספיה", "תמנונים", "ביולוגיה ימית", "היסטוריה של אמנות", "צבענים טבעיים"]
---
<h1>דיו טבעי: מסע לתוך ייצור דיו הספיה מתמנונים</h1>

<p>האם ידעתם שהדיו המפורסם ששימש אמנים וסופרים במשך מאות שנים הגיע... מתמנונים? כיצד בעל חיים ימי פשוט מייצר חומר כה ייחודי, ואיך הפכו אותו בני האדם לצבע אמנותי יקר ערך? הצטרפו אלינו למסע אינטראקטיבי מרתק לתוך עולם יצירת דיו הספיה!</p>

<!-- Interactive Application Section -->
<div class="interactive-app">
    <h2>המעבדה הסודית: הכינו דיו ספיה בעצמכם!</h2>

    <div id="step1" class="step active">
        <h3>שלב 1: איסוף שק הדיו (מודל)</h3>
        <div class="octopus-model-container">
            <img id="octopus-img" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Common_Octopus_Model_ME_002.JPG/320px-Common_Octopus_Model_ME_002.JPG" alt="מודל תמנון" class="octopus-img">
            <button id="collect-ink-sac" class="action-button">לאסוף את שק הדיו</button>
            <div class="instruction-text">מוכנים למסע? לחצו על הכפתור והתחילו באיסוף שק הדיו מהתמנון (הדמיה ידידותית, כמובן!)</div>
        </div>
    </div>

    <div id="step2" class="step">
        <h3>שלב 2: כתישה והפקת הפיגמנט</h3>
        <div class="grinding-area">
             <img id="ink-sac-img" src="https://via.placeholder.com/80x80?text=Ink+Sac" alt="שק דיו" class="grinding-item">
             <div class="grinding-animation"></div>
             <button id="grind-ink-sac" class="action-button">לכתוש את הפיגמנט</button>
             <div id="grind-progress" class="progress-text">נותר ללחוץ: 5</div>
             <div class="instruction-text">כתשו את שק הדיו בלחיצות חוזרות כדי לשחרר את הפיגמנט הכהה ולהפוך אותו לאבקה.</div>
        </div>
    </div>

    <div id="step3" class="step">
        <h3>שלב 3: דילול במים ושליטה על הגוון</h3>
        <div class="dilution-control">
            <div class="control-row">
                <label for="water-ratio">שחקו עם כמות המים:</label>
                <input type="range" id="water-ratio" min="0" max="100" value="10" step="1">
                <span id="water-ratio-value" class="ratio-value">10</span>% מים
            </div>
            <div class="color-preview">
                <h4>תצוגה מקדימה של הדיו:</h4>
                <div id="ink-color-swatch" class="color-swatch"></div>
            </div>
            <div class="instruction-text">הזזת המחוון משנה את ריכוז הדיו במים - ראו כיצד הגוון משתנה בזמן אמת! בחרו את הגוון המושלם שלכם.</div>
        </div>
    </div>

     <div id="final-step" class="step">
        <h3>הדיו מוכן! יצירת מופת בדרך...</h3>
        <p>הנה הדגמה מודרנית של תהליך הפקת דיו הספיה. זכרו, במציאות התהליך מורכב ועדין יותר.</p>
         <div class="color-preview">
            <h4>הגוון הסופי שבחרתם:</h4>
            <div id="final-ink-color-swatch" class="color-swatch"></div>
        </div>
         <button id="reset-app" class="action-button secondary">להתחיל מחדש</button>
         <div class="instruction-text">רוצים לנסות ליצור גוון אחר? לחצו על "להתחיל מחדש".</div>
     </div>
</div>

<!-- CSS Styling -->
<style>
    :root {
        --primary-color: #4a3b33; /* Deep Sepia Brown */
        --secondary-color: #8b5e3c; /* Medium Sepia Brown */
        --accent-color: #5a7d7d; /* Muted Teal/Blue for highlights */
        --background-color: #f8f0e3; /* Creamy off-white */
        --card-background: #fffaf0; /* Lighter Cream */
        --border-color: #d3c1ae; /* Light brown border */
        --text-color: #333;
        --instruction-color: #666;
        --button-bg: var(--secondary-color);
        --button-hover-bg: var(--primary-color);
    }

    body {
        font-family: 'Arial Hebrew', 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: var(--background-color);
        color: var(--text-color);
        overflow-x: hidden; /* Prevent horizontal scroll due to animations */
    }

    h1, h2, h3, h4 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 1em;
    }

    h1 { font-size: 2em; }
    h2 { font-size: 1.6em; }
    h3 { font-size: 1.3em; margin-top: 0; }
    h4 { font-size: 1.1em; margin-top: 0.8em; margin-bottom: 0.5em; }

    p {
        margin-bottom: 1.5em;
    }

    .interactive-app {
        background-color: var(--card-background);
        padding: 30px;
        border-radius: 12px;
        margin-bottom: 30px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        position: relative; /* Needed for step transitions */
    }

    .step {
        margin-bottom: 25px;
        padding: 25px;
        border: 2px dashed var(--border-color);
        border-radius: 8px;
        background-color: #fff;
        box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.05);
        opacity: 0; /* Start hidden for transitions */
        transform: translateY(20px);
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        position: absolute; /* Position absolutely for overlap during transition */
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        height: 100%; /* Occupy full container height during transition */
        overflow: auto; /* Allow scrolling if content is tall */
        box-sizing: border-box; /* Include padding in height */
    }

    .step.active {
        opacity: 1;
        transform: translateY(0);
        position: static; /* Take up space when active */
        height: auto; /* Auto height when active */
    }

     .instruction-text {
         font-style: italic;
         color: var(--instruction-color);
         margin-top: 15px;
         font-size: 0.95em;
         text-align: center;
     }

    .octopus-model-container, .grinding-area, .dilution-control, .color-preview {
        margin-bottom: 20px;
        padding: 15px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #fcfcfc;
        text-align: center; /* Center contents within these divs */
    }

    .octopus-img {
        width: 180px;
        display: block;
        margin: 0 auto 20px auto;
        transition: transform 0.3s ease-in-out; /* Smooth movement */
    }

    /* Animations for octopus image */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }

    .octopus-img.pulsing {
        animation: pulse 0.8s ease-in-out;
    }

    .grinding-area {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .grinding-item {
         width: 70px;
         height: 70px;
         object-fit: contain; /* Ensure image fits */
         margin-bottom: 15px;
         transition: transform 0.2s ease-out, opacity 0.3s ease-out;
    }

     .grinding-animation {
         width: 100px;
         height: 20px;
         background-color: rgba(139, 94, 60, 0.3); /* Semi-transparent sepia */
         border-radius: 10px;
         margin-bottom: 10px;
         overflow: hidden;
         display: none; /* Hidden until grinding starts */
         position: relative;
     }

     .grinding-animation::after {
         content: '';
         position: absolute;
         top: 0;
         left: 0;
         width: 0%;
         height: 100%;
         background-color: var(--secondary-color);
         transition: width 0.3s ease-out;
     }

     .grinding-animation.grinding::after {
         width: 100%; /* Animated by JS setting width */
     }

     .progress-text {
         font-weight: bold;
         color: var(--primary-color);
         margin-top: 5px;
     }

    .control-row {
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
    }

    .control-row label {
        margin-left: 10px;
        white-space: nowrap;
    }

    #water-ratio {
        flex-grow: 1; /* Allow slider to take available space */
        max-width: 300px; /* Limit slider width */
        margin: 0 10px;
        cursor: pointer;
    }

     .ratio-value {
         font-weight: bold;
         color: var(--primary-color);
         min-width: 30px; /* Reserve space to prevent layout shifts */
         text-align: left; /* Align numbers consistently */
     }

    .color-preview {
        text-align: center;
        padding-top: 10px; /* Add space above swatch */
    }

    .color-swatch {
        width: 180px;
        height: 60px;
        background-color: black; /* Default state */
        border: 2px solid var(--border-color);
        margin: 10px auto 0 auto;
        border-radius: 5px;
        transition: background-color 0.5s ease-in-out; /* Smooth color change */
    }

    .action-button {
        padding: 12px 25px;
        background-color: var(--button-bg);
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 15px;
        transition: background-color 0.3s ease, transform 0.1s active;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
    }

    .action-button:hover {
        background-color: var(--button-hover-bg);
        box-shadow: 0 3px 7px rgba(0, 0, 0, 0.2);
    }

    .action-button:active {
         transform: scale(0.98);
         box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
    }

    .secondary {
        background-color: var(--accent-color);
    }
     .secondary:hover {
         background-color: #4c6a6a;
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #007bff; /* Standard blue for info button */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    #toggle-explanation:hover {
        background-color: #0056b3;
        box-shadow: 0 3px 7px rgba(0, 0, 0, 0.2);
    }

     .explanation {
        display: none; /* Initially hidden */
        background-color: var(--card-background);
        padding: 30px;
        border-radius: 12px;
        margin-bottom: 30px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        border-top: 4px solid var(--accent-color); /* Highlight top border */
     }
     .explanation h2, .explanation h3 {
         color: var(--accent-color);
     }
     .explanation p, .explanation ul {
         margin-bottom: 1.5em;
         text-align: justify; /* Justify text for explanation */
     }
     .explanation ul {
         padding-right: 25px; /* RTL list padding */
         list-style-type: disc; /* Use discs for list items */
     }
     .explanation li {
         margin-bottom: 0.8em;
     }

     /* Responsive adjustments */
    @media (max-width: 600px) {
        body { padding: 10px; }
        .interactive-app, .explanation { padding: 20px; }
        .step { padding: 20px; }
        .action-button, #toggle-explanation {
            width: 100%;
            padding: 12px 15px;
            font-size: 1em;
        }
         .control-row {
             flex-direction: column;
         }
         .control-row label {
             margin: 0 0 10px 0;
         }
         #water-ratio {
             width: 100%;
             max-width: none;
             margin: 0;
         }
         .ratio-value {
             margin-top: 10px;
             text-align: center;
             min-width: auto;
         }
          .color-swatch {
              width: 100%;
          }
    }

</style>

<!-- JavaScript -->
<script>
    const collectInkSacButton = document.getElementById('collect-ink-sac');
    const octopusImg = document.getElementById('octopus-img');
    const grindInkSacButton = document.getElementById('grind-ink-sac');
    const inkSacImg = document.getElementById('ink-sac-img');
    const grindProgressText = document.getElementById('grind-progress');
    const waterRatioSlider = document.getElementById('water-ratio');
    const waterRatioValueSpan = document.getElementById('water-ratio-value');
    const inkColorSwatch = document.getElementById('ink-color-swatch');
    const finalInkColorSwatch = document.getElementById('final-ink-color-swatch');
    const stepDivs = [
        document.getElementById('step1'),
        document.getElementById('step2'),
        document.getElementById('step3'),
        document.getElementById('final-step')
    ];
    const resetButton = document.getElementById('reset-app');

    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const fullExplanationDiv = document.getElementById('full-explanation');

    let currentStepIndex = 0; // 0: collect, 1: grind, 2: dilute, 3: final
    const totalGrindClicks = 5;
    let currentGrindClicks = 0;

     // Sound effects (simple placeholders)
     const collectSound = new Audio('https://file-examples-com.github.io/uploads/2017/11/file_example_WAV_1MG.wav'); // Example sound 1
     const grindSound = new Audio('https://file-examples-com.github.io/uploads/2017/11/file_example_WAV_2MG.wav'); // Example sound 2
     const mixSound = new Audio('https://file-examples-com.github.io/uploads/2017/11/file_example_WAV_5MG.wav'); // Example sound 3
     const finishSound = new Audio('https://file-examples-com.github.io/uploads/2017/11/file_example_WAV_5MG.wav'); // Example sound 4

     // Helper to play sound
     function playSound(sound) {
         // Check if sound is loaded and ready to play
         if (sound && sound.readyState >= 2) {
             sound.currentTime = 0; // Rewind to start
             sound.play().catch(e => console.error("Sound playback failed:", e)); // Handle potential errors
         } else {
             console.warn("Sound not ready:", sound);
         }
     }


    // Function to update the ink color based on water ratio
    function updateInkColor() {
        const ratio = waterRatioSlider.value; // 0 to 100
        waterRatioValueSpan.textContent = ratio;

        // Interpolate between a very dark sepia and a light sepia brown/yellowish-brown
        // Ratio 0: Very dark sepia (almost black-brown)
        // Ratio 100: Lighter, more transparent brown
        const darkR = 25, darkG = 15, darkB = 5; // Dark brown-black
        const lightR = 160, lightG = 120, lightB = 80; // Medium-light brown

        const r = darkR + (lightR - darkR) * (ratio / 100);
        const g = darkG + (lightG - darkG) * (ratio / 100);
        const b = darkB + (lightB - darkB) * (ratio / 100);

        const color = `rgb(${Math.round(r)}, ${Math.round(g)}, ${Math.round(b)})`;
        inkColorSwatch.style.backgroundColor = color;

         // If on the final step, update the final swatch as well
         if(currentStepIndex === 3) {
             finalInkColorSwatch.style.backgroundColor = color;
         }
         // Play mix sound on significant change (optional, might be annoying)
         // playSound(mixSound);
    }

    // Step transition function with animations
    function goToStep(index) {
        if (index < 0 || index >= stepDivs.length) return;

        // Hide current step with animation
        if (currentStepIndex < stepDivs.length) {
             stepDivs[currentStepIndex].classList.remove('active');
             // No need for explicit fade-out class if position:absolute handles overlap and opacity transition is on 'active'
        }

        currentStepIndex = index;

        // Show next step with animation after a short delay
        // Delay matches CSS transition duration for smooth change
        setTimeout(() => {
            stepDivs[currentStepIndex].classList.add('active');

            // Specific step initialization logic
            if (currentStepIndex === 2) { // Step 3: Dilution
                updateInkColor(); // Initialize color preview
            } else if (currentStepIndex === 3) { // Final Step
                // Set the final swatch color to the current preview color
                 finalInkColorSwatch.style.backgroundColor = inkColorSwatch.style.backgroundColor;
                 playSound(finishSound); // Play finish sound
            }

        }, 500); // Delay matches transition duration
    }

    function resetApp() {
         currentGrindClicks = 0;
         grindProgressText.textContent = `נותר ללחוץ: ${totalGrindClicks}`;
         grindInkSacButton.disabled = false;
         inkSacImg.style.opacity = 1; // Reset ink sac image
         // Optionally reset ink sac image src if it changed during grinding
         inkSacImg.src = "https://via.placeholder.com/80x80?text=Ink+Sac";


         waterRatioSlider.value = 10; // Reset slider
         // Color swatch will be updated when step 3 is entered

         goToStep(0); // Go back to the first step
    }

    // Event Listeners

    // Step 1: Collect Ink Sac
    collectInkSacButton.addEventListener('click', () => {
        playSound(collectSound);
        octopusImg.classList.add('pulsing'); // Add pulse animation class
        collectInkSacButton.disabled = true; // Prevent multiple clicks
        setTimeout(() => {
            octopusImg.classList.remove('pulsing');
            collectInkSacButton.disabled = false; // Re-enable button for potential reset
            goToStep(1); // Go to Step 2
        }, 800); // Delay slightly longer than animation
    });


    // Step 2: Grind Ink Sac
    grindInkSacButton.addEventListener('click', () => {
        if (currentGrindClicks < totalGrindClicks) {
            currentGrindClicks++;
            grindProgressText.textContent = `נותר ללחוץ: ${totalGrindClicks - currentGrindClicks}`;
            playSound(grindSound);

            // Simple visual feedback for grinding
            inkSacImg.style.transform = `scale(${1 - (currentGrindClicks / totalGrindClicks) * 0.2})`; // Scale down slightly
             inkSacImg.style.opacity = 1 - (currentGrindClicks / totalGrindClicks) * 0.5; // Fade out slightly

            if (currentGrindClicks >= totalGrindClicks) {
                grindProgressText.textContent = "טחינה הושלמה!";
                grindInkSacButton.disabled = true; // Disable button after completion
                inkSacImg.style.opacity = 0; // Fully hide the ink sac image
                // Optionally change the image to powder here
                // inkSacImg.src = "https://via.placeholder.com/80x80?text=Ink+Powder"; // Example
                // inkSacImg.style.opacity = 1; // Show powder image if changed

                setTimeout(() => {
                    goToStep(2); // Go to Step 3 after a short delay
                }, 1000); // Delay before moving to next step
            }
        }
    });

    // Step 3: Dilute
    // Use 'input' for real-time updates as slider is dragged
    waterRatioSlider.addEventListener('input', updateInkColor);
    // No specific button click needed to "finish" dilution in this flow,
    // the user proceeds whenever they are ready by clicking the next button if one existed,
    // or the flow could automatically proceed after a delay, or a "Done Diluting" button could be added.
    // Let's make the color swatch clickable to proceed, or maybe a button appears?
    // Adding a button aligns better with the current structure.
     const proceedAfterDilutionButton = document.createElement('button');
     proceedAfterDilutionButton.textContent = 'סיימתי לדלל, הדיו מוכן!';
     proceedAfterDilutionButton.classList.add('action-button');
     proceedAfterDilutionButton.style.marginTop = '20px';
     // Find step 3 div and append the button
     stepDivs[2].appendChild(proceedAfterDilutionButton);

     proceedAfterDilutionButton.addEventListener('click', () => {
         goToStep(3); // Go to Final Step
     });


    // Final Step: Reset
    resetButton.addEventListener('click', resetApp);


    // Explanation Toggle
    toggleExplanationButton.addEventListener('click', function() {
        const isHidden = fullExplanationDiv.style.display === 'none' || fullExplanationDiv.style.display === '';
        if (isHidden) {
            fullExplanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מורחב';
        } else {
            fullExplanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג/הסתר הסבר מורחב';
        }
    });

    // Initial state setup - Ensure only step 1 is visible on load and steps are positioned correctly
    stepDivs.forEach((step, index) => {
        step.style.display = 'none'; // Hide all initially
        step.style.position = 'absolute'; // Position for transitions
        step.style.top = '0'; step.style.left = '0'; step.style.right = '0'; step.style.bottom = '0';
        step.style.height = '100%'; // Fill container
        step.style.boxSizing = 'border-box';
    });

    // Show the first step after a slight delay to allow CSS to apply
    setTimeout(() => {
         stepDivs[0].style.display = 'block'; // Show the first step
         stepDivs[0].classList.add('active'); // Apply active class for initial visibility/position
         stepDivs[0].style.position = 'static'; // Set step 1 to static after initial load/transition
         stepDivs[0].style.height = 'auto'; // Set step 1 to auto height
    }, 10); // Small delay


     // Preload sounds (optional but good practice)
     collectSound.load();
     grindSound.load();
     mixSound.load();
     finishSound.load();

</script>
```