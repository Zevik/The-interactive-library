---
title: "מעבדת גלגלי השיניים האינטראקטיבית: איזון בין מהירות וכוח"
english_slug: "interactive-gear-lab"
category: "מדעים מדויקים / פיזיקה"
tags: ["גלגלי שיניים", "מכניקה", "מהירות", "כוח", "מומנט", "סימולציה", "אינטראקטיבי", "ניסוי"]
---
<div id="gear-simulator">
    <div class="controls">
        <div class="control-group">
            <label for="teethA">גלגל א' (המניע):</label>
            <input type="number" id="teethA" value="20" min="5" max="100">
            <input type="range" id="sliderA" value="20" min="5" max="100">
        </div>
        <div class="control-group">
            <label for="teethB">גלגל ב' (המונע):</label>
            <input type="number" id="teethB" value="40" min="5" max="100">
            <input type="range" id="sliderB" value="40" min="5" max="100">
        </div>
    </div>
    <div class="simulation-area">
        <div id="gearA" class="gear">
            <!-- Teeth and marker will be added by JS -->
        </div>
        <div id="gearB" class="gear">
            <!-- Teeth and marker will be added by JS -->
        </div>
    </div>
    <div class="results">
        <p>יחס מהירויות (גלגל ב' / גלגל א'): <span id="speedRatio"></span></p>
        <p>יחס מומנט כוח (גלגל ב' / גלגל א'): <span id="torqueRatio"></span></p>
    </div>
</div>

<style>
    /* גלובלי ואזורי הסימולציה */
    #gear-simulator {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        margin: 20px auto;
        padding: 30px;
        background: linear-gradient(to bottom right, #e0eafc, #cfdef3);
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        max-width: 700px;
        overflow: hidden;
    }

    /* אזור הבקרות */
    .controls {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-bottom: 40px;
        flex-wrap: wrap;
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .controls label {
        margin-bottom: 10px;
        font-weight: bold;
        color: #333;
        font-size: 1.1em;
    }

    .controls input[type="number"] {
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
        width: 70px;
        text-align: center;
        font-size: 1em;
        margin-bottom: 10px;
    }

     .controls input[type="range"] {
         -webkit-appearance: none;
         appearance: none;
         width: 120px;
         height: 8px;
         background: #ddd;
         outline: none;
         opacity: 0.7;
         transition: opacity .2s;
         border-radius: 5px;
     }

     .controls input[type="range"]:hover {
         opacity: 1;
     }

     .controls input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: #007BFF;
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }

      .controls input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #007BFF;
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }


    /* אזור הסימולציה הויזואלית */
    .simulation-area {
        position: relative;
        width: 100%;
        max-width: 650px; /* Adjust width */
        height: 350px; /* Adjust height */
        margin: 0 auto 40px auto;
        display: flex;
        justify-content: center;
        align-items: center;
        /* overflow: hidden; /* Keep if gears should not exceed boundary */
    }

    .gear {
        position: absolute;
        border-radius: 50%;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
        /* Default animation */
        animation-timing-function: linear;
        animation-iteration-count: infinite;
        transform-style: preserve-3d; /* For 3D effects if needed */
        will-change: transform; /* Performance hint */
    }

     .gear::before { /* Inner circle/hole */
        content: '';
        position: absolute;
        width: 40%;
        height: 40%;
        border-radius: 50%;
        background-color: #f4f7f6; /* Matches background */
        border: 3px solid #388E3C;
        box-sizing: border-box;
        z-index: 1;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
    }

    /* Gear teeth styling */
    .tooth {
        position: absolute;
        background-color: #555;
        box-shadow: 0 1px 2px rgba(0,0,0,0.3);
        /* Dimensions, position, and transform will be set by JS */
        z-index: 2; /* Above inner circle */
    }

    /* Marker styling */
     .marker {
         position: absolute;
         background-color: #FF0000; /* Bright Red marker */
         border-radius: 50%;
         z-index: 3; /* Ensure marker is on top */
         box-shadow: 0 0 8px rgba(255,0,0,0.7);
         /* Dimensions and position set by JS */
     }


    /* סגנון גלגלי השיניים השונים */
    #gearA {
        z-index: 4; /* Ensure the driving gear is visually prominent */
        animation-name: rotateClockwise;
        background: radial-gradient(circle, #f0f0f0 0%, #ccc 50%, #4CAF50 80%, #388E3C 100%);
        border: 5px solid #2E7D32;
    }

    #gearB {
        animation-name: rotateCounterClockwise; /* Rotates opposite to A */
        background: radial-gradient(circle, #f0f0f0 0%, #ccc 50%, #4CAF50 80%, #388E3C 100%);
        border: 5px solid #2E7D32;
    }

     /* צבעי גלגל B לפי יחס הכוח/מהירות */
     .gear-b-slower-more-torque { /* larger B */
         background: radial-gradient(circle, #fff9c4 0%, #ffe082 50%, #FF9800 80%, #F57C00 100%) !important;
         border-color: #EF6C00 !important;
     }

     .gear-b-faster-less-torque { /* smaller B */
         background: radial-gradient(circle, #b3e5fc 0%, #81d4fa 50%, #03A9F4 80%, #0288D1 100%) !important;
         border-color: #0277BD !important;
     }


    /* אזור התוצאות */
    .results {
        text-align: center;
        font-size: 1.2em;
        color: #333;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .results span {
        font-weight: bold;
        color: #0056b3;
        font-size: 1.3em;
    }

    /* אנימציות סיבוב */
    @keyframes rotateClockwise {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    @keyframes rotateCounterClockwise {
        from { transform: rotate(0deg); }
        to { transform: rotate(-360deg); }
    }

    /* כפתור הסבר והסבר */
    #show-explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        color: #fff;
        background-color: #007BFF;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        font-weight: bold;
    }

    #show-explanation-button:hover {
        background-color: #0056b3;
    }
     #show-explanation-button:active {
        transform: scale(0.98);
     }


    #explanation {
        margin-top: 30px;
        padding: 20px;
        background-color: #e9ecef;
        border-left: 5px solid #007BFF;
        border-radius: 8px;
        color: #333;
        display: none; /* Hidden by default */
        direction: rtl;
        line-height: 1.7;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    #explanation h2 {
        margin-top: 0;
        color: #0056b3;
        border-bottom: 2px solid #007BFF;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    #explanation p {
        margin-bottom: 15px;
    }

     #explanation ul {
         margin-bottom: 15px;
     }

     #explanation li {
         margin-bottom: 8px;
     }

    #explanation strong {
        color: #0056b3;
    }

</style>

<button id="show-explanation-button">גלו את סוד גלגלי השיניים!</button>

<div id="explanation">
    <h2>הסוד מאחורי גלגלי השיניים: לשחק עם מהירות ומומנט</h2>
    <p>דמיינו שמכונית לא הייתה צריכה להחליף הילוכים. היא הייתה מתקשה לטפס בעליות (חוסר בכוח!) או מגיעה למהירות מקסימלית נמוכה מאוד (חוסר במהירות!). גלגלי שיניים הם הגיבורים שמצילים את המצב, ומאפשרים לנו להחליף בצורה חכמה בין מהירות למומנט כוח.</p>
    <p>כאשר גלגל שיניים אחד מסובב גלגל שיניים אחר שמשולב בו, הנקודה שבה השיניים נפגשות נעה באותה מהירות לינארית בשני הגלגלים. אבל מה קורה למהירות הסיבוב ולכוח?</p>
    <p>אם לגלגל המניע (גלגל א') יש N<sub>א</sub> שיניים, ולגלגל המונע (גלגל ב') יש N<sub>ב</sub> שיניים:</p>
    <ul>
        <li><strong>קסם המהירות:</strong> מהירות הסיבוב של הגלגלים (כמה מהר הם מסתובבים על צירם) הולכת הפוך למספר השיניים שלהם. אם גלגל א' עושה סיבוב אחד, כמה סיבובים יעשה גלגל ב'? זה תלוי ביחס השיניים!
            <br> יחס מהירויות (V<sub>ב</sub> / V<sub>א</sub>) = N<sub>א</sub> / N<sub>ב</sub>.
            <br> **משמעות:** גלגל מונע קטן יותר (פחות שיניים) מגלגל מניע - יסתובב מהר יותר! גלגל מונע גדול יותר (יותר שיניים) - יסתובב לאט יותר.</li>
        <li><strong>כוח המומנט:</strong> מומנט הכוח, או ה"כוח המסובב" שהגלגל יכול להפעיל, מתנהג הפוך מהמהירות, ויחס ישר למספר השיניים:
            <br> יחס מומנט כוח (M<sub>ב</sub> / M<sub>א</sub>) = N<sub>ב</sub> / N<sub>א</sub>.
            <br> **משמעות:** גלגל מונע גדול יותר (יותר שיניים) מגלגל מניע - יקבל מומנט כוח גדול יותר (כוח רב יותר לסיבוב עצמים כבדים), אך יסתובב לאט יותר. גלגל מונע קטן יותר - יקבל מומנט כוח קטן יותר, אך יסתובב מהר יותר!</li>
    </ul>
    <p>זוהי הפשרה הגאונית שגלגלי שיניים מאפשרים: אתם יכולים "להחליף" מהירות תמורת כוח, ולהפך. בתיבות הילוכים של מכוניות, למשל, הילוכים נמוכים משתמשים בגלגלים גדולים יותר כדי לקבל מומנט גבוה (ליציאה מהמקום ולעליות), והילוכים גבוהים משתמשים בגלגלים קטנים יותר כדי לקבל מהירות גבוהה (לשיוט). עכשיו התנסו בעצמכם במעבדה ובדקו איך שינוי מספר השיניים משפיע על היחסים!</p>
</div>

<script>
    const teethAInput = document.getElementById('teethA');
    const teethBInput = document.getElementById('teethB');
    const sliderA = document.getElementById('sliderA');
    const sliderB = document.getElementById('sliderB');
    const gearA = document.getElementById('gearA');
    const gearB = document.getElementById('gearB');
    const speedRatioSpan = document.getElementById('speedRatio');
    const torqueRatioSpan = document.getElementById('torqueRatio');
    const showExplanationButton = document.getElementById('show-explanation-button');
    const explanationDiv = document.getElementById('explanation');
    const simulationArea = document.querySelector('.simulation-area'); // Get the simulation area element

    // Function to create and position teeth and marker for a gear
    function updateGearVisuals(gearElement, teethCount, radius) {
        // Clear existing teeth and marker
        gearElement.innerHTML = '';

        // Add marker first so it's under teeth if needed (though z-index handles it)
        const marker = document.createElement('div');
        marker.classList.add('marker');
        gearElement.appendChild(marker);

        const toothWidth = radius * 0.12; // Width relative to radius
        const toothHeight = radius * 0.2; // Height relative to radius

        for (let i = 0; i < teethCount; i++) {
            const tooth = document.createElement('div');
            tooth.classList.add('tooth');
            tooth.style.width = `${toothWidth}px`;
            tooth.style.height = `${toothHeight}px`;

            const angle = (360 / teethCount) * i;

            // Position tooth at the top-center of the gear div (which is the gear's outer edge)
            // and set the rotation origin to the gear's center (radius px down from tooth's top edge)
            tooth.style.position = 'absolute';
            tooth.style.left = `calc(50% - ${toothWidth / 2}px)`;
            tooth.style.top = `0px`;
            tooth.style.transformOrigin = `${toothWidth / 2}px ${radius}px`;
            tooth.style.transform = `rotate(${angle}deg)`;

            gearElement.appendChild(tooth);
        }

        // Position the marker correctly *after* teeth are potentially added
        const markerSize = Math.max(8, Math.min(20, radius * 0.15));
        marker.style.width = `${markerSize}px`;
        marker.style.height = `${markerSize}px`;
        // Position marker at the top edge, centered horizontally
        marker.style.left = `calc(50% - ${markerSize/2}px)`;
        marker.style.top = `${markerSize/2}px`; // Slightly inset from the very top edge
        marker.style.zIndex = 3;
    }


    function updateSimulation() {
        let teethA = parseInt(teethAInput.value);
        let teethB = parseInt(teethBInput.value);

        // Basic validation
        if (isNaN(teethA) || teethA < 5) teethA = 5;
        if (isNaN(teethB) || teethB < 5) teethB = 5;

        // Sync slider values with number inputs
        teethAInput.value = teethA;
        sliderA.value = teethA;
        teethBInput.value = teethB;
        sliderB.value = teethB;

        const baseSize = 80; // Base radius in pixels for a reference tooth count (e.g., 20)
        const referenceTeeth = 20;

        const radiusA = baseSize * (teethA / referenceTeeth);
        const radiusB = baseSize * (teethB / referenceTeeth);

        // Update gear size
        gearA.style.width = `${radiusA * 2}px`;
        gearA.style.height = `${radiusA * 2}px`;
        gearB.style.width = `${radiusB * 2}px`;
        gearB.style.height = `${radiusB * 2}px`;

        // Position gears side-by-side, centered and touching at edges
        const centerDistance = radiusA + radiusB;
        const simulationCenterX = simulationArea.offsetWidth / 2;

        // Position left edge of gearA relative to center line of the combined system
        gearA.style.left = `${simulationCenterX - centerDistance / 2 - radiusA}px`;
        // Position left edge of gearB relative to center line of the combined system
        gearB.style.left = `${simulationCenterX + centerDistance / 2 - radiusB}px`;

        gearA.style.top = `calc(50% - ${radiusA}px)`; // Center vertically
        gearB.style.top = `calc(50% - ${radiusB}px)`; // Center vertically

        // Update gear visuals (teeth and marker)
        updateGearVisuals(gearA, teethA, radiusA);
        updateGearVisuals(gearB, teethB, radiusB);

        // Calculate ratios
        const speedRatio = teethA / teethB;
        const torqueRatio = teethB / teethA;

        speedRatioSpan.textContent = speedRatio.toFixed(2);
        torqueRatioSpan.textContent = torqueRatio.toFixed(2);

        // Update animation speed (duration)
        // Gear A rotates at a constant speed (e.g., 4 seconds per rotation for referenceTeeth)
        // Duration is proportional to teeth count / radius
        const baseDurationA = 4; // seconds for one rotation of gear A with referenceTeeth
        const durationA = baseDurationA * (teethA / referenceTeeth); // Adjust duration based on A's size (optional, can keep A const)
        const durationB = durationA / speedRatio; // B's duration relative to A's speed and ratio

        // Apply animation durations - remove and re-add animation to restart smoothly
        gearA.style.animation = 'none';
        gearB.style.animation = 'none';
        void gearA.offsetWidth; // Trigger reflow
        void gearB.offsetWidth; // Trigger reflow
        gearA.style.animation = `rotateClockwise ${durationA}s linear infinite`;
        gearB.style.animation = `rotateCounterClockwise ${durationB}s linear infinite`;


        // Update gear B color based on the torque/speed relationship
        // Remove previous color classes
        gearB.classList.remove('gear-b-slower-more-torque', 'gear-b-faster-less-torque');
        // Reset gear A color (it's the input/driver, stays consistent)
        gearA.style.backgroundColor = ''; // Reset to CSS default
        gearA.style.borderColor = ''; // Reset to CSS default


        if (teethB > teethA) {
             // Gear B is larger - Slower, more torque
             gearB.classList.add('gear-b-slower-more-torque');
        } else if (teethB < teethA) {
             // Gear B is smaller - Faster, less torque
             gearB.classList.add('gear-b-faster-less-torque');
        } else {
             // Same size - Speed and torque ratios are 1:1 - Use default green styles for B
             // No class needed, default styles apply
        }
    }

    // Initial update to set up the simulation on load
    updateSimulation();

    // Add event listeners
    teethAInput.addEventListener('input', updateSimulation);
    teethBInput.addEventListener('input', updateSimulation);
    sliderA.addEventListener('input', updateSimulation);
    sliderB.addEventListener('input', updateSimulation);

    // Explanation button logic
    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        showExplanationButton.textContent = isHidden ? 'הסתרת הסוד' : 'גלו את סוד גלגלי השיניים!';
    });

    // Optional: Update simulation on window resize to adjust gear positioning
    window.addEventListener('resize', updateSimulation);

</script>