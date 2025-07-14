---
title: "איך מכונות שלג יוצרות קסם קפוא?"
english_slug: how-snow-machines-make-cold-a-journey-into-cool
category: "מדעים מדויקים / פיזיקה"
tags: [שלג מלאכותי, פיזיקה, תרמודינמיקה, מכונות שלג, קירור אידוי, קירור אדיאבטי]
---
# איך מכונות שלג יוצרות קסם קפוא?

דמיינו אתר סקי שמשווע לשלג, ואז, לפתע, מתוך מגדלי המתכת הענקיים מתחיל לרדת מבול לבן! איך המכונות האלה מצליחות ליצור פתיתי שלג קפואים, לפעמים אפילו כשהטמפרטורה מעל האפס? בואו נחקור את הפיזיקה המפתיעה שמאחורי הקסם הזה.

<div id="snow-machine-app">
    <h2>כוונן את מכונת השלג שלך!</h2>
    <div class="controls">
        <div class="control-group">
            <label for="air-temp">טמפרטורת אוויר חיצונית (°C):</label>
            <input type="range" id="air-temp" min="-10" max="5" value="-2" step="0.1">
            <span id="air-temp-value">-2.0°C</span>
        </div>
        <div class="control-group">
            <label for="water-pressure">לחץ מים (כוח ההתזה):</label>
            <input type="range" id="water-pressure" min="1" max="10" value="5" step="0.1">
            <span id="water-pressure-value">5</span>
        </div>
        <div class="control-group">
            <label for="air-pressure">לחץ אוויר דחוס (כוח הקירור):</label>
            <input type="range" id="air-pressure" min="1" max="10" value="7" step="0.1">
            <span id="air-pressure-value">7</span>
        </div>
        <div class="control-group">
            <label for="nucleation">הוספת גרעיני התקרחות (עוזר לקפוא):</label>
            <input type="checkbox" id="nucleation" checked>
             <span class="checkbox-placeholder"></span> <!-- Placeholder for alignment -->
        </div>
         <button id="run-simulation">הפעל סימולציה</button>
    </div>
    <div class="simulation-area">
        <div class="nozzle">
            <div class="inlet water"></div>
            <div class="inlet air"></div>
            <div class="outlet"></div>
        </div>
        <div id="spray-area" class="spray-area"></div>
    </div>
    <div class="output-area">
        <h3>התוצאה:</h3>
        <p id="output-text">התאם את הפרמטרים ולחץ על 'הפעל סימולציה' לראות מה קורה!</p>
    </div>
</div>

<style>
    @keyframes sparkle {
        0% { box-shadow: 0 0 2px white; }
        50% { box-shadow: 0 0 8px rgba(255, 255, 255, 0.9); }
        100% { box-shadow: 0 0 2px white; }
    }

    #snow-machine-app {
        font-family: 'Arial', sans-serif;
        border: 1px solid #b3e5fc;
        padding: 25px;
        border-radius: 12px;
        max-width: 750px;
        margin: 30px auto;
        background: linear-gradient(to bottom, #e0f8ff, #ffffff); /* Soft gradient */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        color: #333;
        overflow: hidden; /* Ensure droplets stay inside */
    }

    #snow-machine-app h2 {
        text-align: center;
        color: #01579b; /* Darker blue */
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.8em;
        letter-spacing: 0.5px;
    }

     #snow-machine-app h3 {
         text-align: center;
         color: #0277bd; /* Medium blue */
         margin-top: 15px;
         margin-bottom: 10px;
     }


    .controls {
        margin-bottom: 25px;
        padding: 20px;
        background-color: #e1f5fe; /* Lighter blue */
        border-radius: 8px;
        border: 1px solid #b3e5fc;
    }

    .control-group {
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .controls label {
        flex-basis: 60%;
        margin-right: 15px;
        font-weight: bold;
        color: #039be5; /* Accent blue */
    }

    .controls input[type="range"] {
        flex-basis: 30%;
        -webkit-appearance: none; /* Override default */
        appearance: none;
        height: 8px;
        background: #b3e5fc; /* Light blue track */
        border-radius: 5px;
        outline: none;
        opacity: 0.9;
        transition: opacity .2s;
    }

     .controls input[type="range"]:hover {
         opacity: 1;
     }

     .controls input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: #0288d1; /* Thumb color */
         border: 1px solid #01579b;
         border-radius: 50%;
         cursor: pointer;
     }

     .controls input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #0288d1;
         border: 1px solid #01579b;
         border-radius: 50%;
         cursor: pointer;
     }


    .controls span {
        flex-basis: 10%;
        text-align: right;
        font-weight: bold;
        color: #01579b; /* Darker blue */
        min-width: 50px; /* Ensure space for value */
    }

     .controls input[type="checkbox"] {
         flex-basis: 10%;
         margin-right: 0;
         position: relative; /* For custom styling if needed later */
         width: 20px; /* Standard size */
         height: 20px;
         cursor: pointer;
     }
     .controls .checkbox-placeholder {
        flex-basis: 10%;
         min-width: 50px; /* Match span width for alignment */
         text-align: right;
     }

     #run-simulation {
         display: block;
         width: 200px;
         margin: 20px auto 0;
         padding: 12px 20px;
         text-align: center;
         background-color: #007bff;
         color: white;
         border: none;
         border-radius: 5px;
         cursor: pointer;
         font-size: 1.1em;
         transition: background-color 0.3s ease, transform 0.1s ease;
     }

     #run-simulation:hover {
         background-color: #0056b3;
     }
    #run-simulation:active {
        transform: scale(0.98);
    }


    .simulation-area {
        display: flex;
        align-items: center;
        margin-bottom: 25px;
        min-height: 200px; /* Give it some height */
    }

    .nozzle {
        width: 90px; /* Slightly larger */
        height: 110px;
        background: linear-gradient(to right, #757575, #a1a1a1); /* Metallic gradient */
        position: relative;
        border-radius: 0 15px 15px 0; /* More rounded */
        margin-right: 25px;
        flex-shrink: 0;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }

    .inlet {
        position: absolute;
        left: 0;
        width: 45px; /* Larger */
        height: 45px;
        background-color: #9e9e9e;
        border-radius: 0 8px 8px 0;
        box-shadow: inset 1px 1px 3px rgba(0,0,0,0.2);
    }

    .inlet.water {
        top: 15px;
        background-color: #03a9f4; /* Bright blue */
    }

    .inlet.air {
        bottom: 15px;
        background-color: #e0e0e0; /* Light gray */
    }

    .outlet {
        position: absolute;
        right: 0;
        top: 35px; /* Centered better */
        width: 45px; /* Larger */
        height: 40px; /* Slightly different height for visual interest */
        background-color: #616161;
        border-radius: 8px 0 0 8px;
        overflow: hidden; /* To potentially clip internal animations */
    }


    .spray-area {
        flex-grow: 1;
        height: 200px; /* More vertical space */
        border: 1px dashed #b3e5fc;
        position: relative;
        overflow: hidden;
        background-color: rgba(224, 248, 255, 0.5); /* Very light blue transparent */
        border-radius: 8px;
    }

    .droplet {
        position: absolute;
        width: 6px; /* Slightly larger */
        height: 6px;
        border-radius: 50%;
        background-color: #03a9f4; /* Initial: water blue */
        transform: translate(-50%, -50%); /* Center the droplet on its coordinates */
        opacity: 1;
        transition: transform 2s linear, background-color 0.8s ease-out, opacity 1.5s ease-out; /* Longer, smoother transitions */
        will-change: transform, background-color, opacity; /* Performance hint */
    }

    .droplet.cooling {
        background-color: #81d4fa; /* Lighter blue */
    }

    .droplet.freezing {
         background-color: #e0e0e0; /* Grayish white */
         transition: transform 2s linear, background-color 0.3s ease-out, opacity 1.5s ease-out; /* Faster color transition for freezing */
    }

    .droplet.frozen {
        background-color: #ffffff; /* Frozen white */
        box-shadow: 0 0 3px rgba(255, 255, 255, 0.7); /* Subtle glow */
    }

    .droplet.snow {
        background-color: #ffffff; /* Snowflakes white */
        box-shadow: 0 0 6px rgba(255, 255, 255, 0.9), 0 0 10px rgba(255, 255, 255, 0.5); /* Stronger glow/sparkle */
        animation: sparkle 1.5s infinite alternate; /* Sparkle animation */
    }
    
    .droplet.fade-out {
        opacity: 0;
    }


    .output-area {
        margin-top: 25px;
        padding: 20px;
        background-color: #e1f5fe; /* Lighter blue */
        border-radius: 8px;
        text-align: center;
        font-size: 1.2em;
        font-weight: bold;
        color: #01579b; /* Darker blue */
        border: 1px solid #b3e5fc;
    }

    #toggle-explanation {
        display: block;
        width: 240px; /* Wider button */
        margin: 30px auto; /* More space */
        padding: 12px;
        text-align: center;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
    }
     #toggle-explanation:active {
        transform: scale(0.98);
    }


    #explanation {
        display: none; /* Initially hidden */
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #b3e5fc;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
        color: #333;
        line-height: 1.6;
    }

    #explanation h2 {
        margin-top: 0;
        color: #01579b;
        font-size: 1.6em;
        border-bottom: 1px solid #b3e5fc;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    #explanation ul {
        list-style-type: none; /* Remove default bullet */
        padding-left: 0;
    }

    #explanation li {
        margin-bottom: 20px; /* More space between points */
        background-color: #e1f5fe; /* Light blue background for list items */
        padding: 15px;
        border-radius: 6px;
        border-left: 4px solid #0288d1; /* Accent border */
    }
     #explanation li strong {
         color: #01579b; /* Darker blue for emphasis */
     }
     #explanation li ul {
         margin-top: 10px;
         margin-bottom: 0;
         padding-left: 20px;
         list-style-type: disc; /* Disc for sub-list */
     }
      #explanation li ul li {
          margin-bottom: 10px;
          padding: 0;
          background: none; /* Remove background from sub-list items */
          border: none; /* Remove border from sub-list items */
          border-left: none;
      }
</style>

<button id="toggle-explanation">הצג הסבר על קסם השלג המלאכותי</button>

<div id="explanation">
    <h2>המסע הקפוא: הפיזיקה שמאחורי השלג המלאכותי</h2>

    <ul>
        <li>
            <strong>שלג מלאכותי מול שלג טבעי: לא אותו הדבר!</strong>
            שלג מלאכותי (טכני) נולד כשמתזים מים ואוויר בטמפרטורות הנכונות. הוא שונה מאחיו הטבעי, שנוצר בעננים מפגש של אדי מים וגרעיני התגבשות זעירים בטמפרטורות נמוכות מאוד. פתיתים מלאכותיים נוטים להיות עגולים וצפופים, לעומת המבנים הגבישיים המרהיבים של שלג טבעי.
        </li>
        <li>
            <strong>מה יש בבטן של מכונת שלג?</strong>
            היא כוללת בדרך כלל מקור מים נקיים, "ריאות" בדמות מדחס אוויר חזק, "פה" בדמות מפוח לדחיפה, ו"לשון" מורכבת – הזרבובית! בזרבובית מתערבבים המים והאוויר הדחוס, ולפעמים מוסיפים גם "זרעים קטנים" שנקראים גרעיני התקרחות.
        </li>
        <li>
            <strong>הקסם הפיזיקלי מתחיל כאן:</strong>
            יצירת שלג אינה רק הקפאת מים. זהו תהליך תרמודינמי מתוחכם:
            <ul>
                <li>
                    <strong>נשיפת הקור (התפשטות אדיאבטית):</strong>
                    האוויר הדחוס שפורץ מהזרבובית מתפשט בבת אחת. פעולה זו דורשת אנרגיה, שהאוויר "גונב" מעצמו, ומתקרר דרמטית! אוויר קר זה מתערבב עם המים ומוריד את טמפרטורתם במהירות. חשבו על ספריי דיאודורנט - התרסיס והפחית מתקררים כשהגז משתחרר.
                </li>
                <li>
                    <strong>קסם ההתאדות המקררת:</strong>
                    טיפות המים הקטנות שניתזות לאוויר (במיוחד אם הוא יבש יחסית) מתחילות להתאדות. האידוי דורש חום, והוא נלקח מהטיפות עצמן ומהאוויר סביבן. זהו אותו עקרון שגורם לכם להרגיש קור כשיצאתם מהבריכה והרוח נשבה. ככל שהטיפות קטנות יותר והאוויר יבש יותר, הקירור הזה חזק יותר.
                </li>
                <li>
                    <strong>הטמפרטורה הסודית: טמפרטורת 'הנורה הרטובה':</strong>
                    טמפרטורת האוויר והלחות היחסית קובעות עד כמה יעיל יהיה קירור האידוי. טמפרטורת ה"נורה הרטובה" היא הטמפרטורה הנמוכה ביותר שאליה טיפות המים *יכולות* להגיע על ידי אידוי בלבד. כדי ליצור שלג, הטמפרטורה הזו חייבת להיות מתחת לאפס. לפעמים, גם אם מד הטמפרטורה היבשה מראה מעט מעל האפס, אוויר יבש מספיק יאפשר טמפרטורת נורה רטובה מתחת לאפס - ויאפשר יצירת שלג!
                </li>
                <li>
                    <strong>למה צריך 'גרעינים'? מים צלולים לא קופאים בקלות!</strong>
                    מים נקיים במיוחד יכולים להישאר נוזליים גם בטמפרטורות מתחת ל-0°C - תופעה הנקראת "קירור יתר" (supercooling). הם לא יקפאו עד שימצאו משהו להתגבש עליו - גרעין התקרחות קטן (כמו אבק, מלח, או אפילו חיידק מיוחד). מכונות שלג חכמות מוסיפות חומרים המכילים גרעינים כאלה, או מייצרות בעצמן כמות קטנה של "זרעי קרח" ראשוניים.
                </li>
            </ul>
        </li>
        <li>
            <strong>הרכבת הפאזל:</strong>
            בזרבובית נפגשים האוויר הדחוס והמים. תערובת זו פורצת החוצה. קירור בזכות התפשטות האוויר והאידוי מוריד את טמפרטורת הטיפות בחדות. אם יש גרעינים בסביבה (או בתוך הטיפות) והטמפרטורה יורדת מספיק (אל מתחת לאפס או עמוק יותר במקרה של קירור יתר), הטיפות קופאות מהר. המפוח דוחף אותן למרחק, ועם התנאים הנכונים - קיבלתם שלג מלאכותי! אם לא קר מספיק או שאין מספיק קירור, הטיפות יישארו נוזליות, או יקפאו מאוחר וייפלו כברד קטן או כטיפות קרח גושיות.
        </li>
    </ul>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const airTempSlider = document.getElementById('air-temp');
        const airTempValue = document.getElementById('air-temp-value');
        const waterPressureSlider = document.getElementById('water-pressure');
        const waterPressureValue = document.getElementById('water-pressure-value');
        const airPressureSlider = document.getElementById('air-pressure');
        const airPressureValue = document.getElementById('air-pressure-value');
        const nucleationCheckbox = document.getElementById('nucleation');
        const sprayArea = document.getElementById('spray-area');
        const outputText = document.getElementById('output-text');
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const runButton = document.getElementById('run-simulation');

        const sprayAreaWidth = sprayArea.offsetWidth;
        const sprayAreaHeight = sprayArea.offsetHeight;
        const nozzleRight = 45; // Corresponds to the 'outlet' width in CSS
        const nozzleY = sprayAreaHeight / 2; // Approximate nozzle height center

        // Animation state - prevents multiple animations running at once
        let isAnimating = false;
        const animationDuration = 2000; // 2 seconds for droplet travel

        function updateValues() {
            airTempValue.textContent = `${airTempSlider.value}°C`;
            waterPressureValue.textContent = waterPressureSlider.value;
            airPressureValue.textContent = airPressureSlider.value;
             // Don't run simulation automatically on input, only on button click
            if (!isAnimating) {
                 outputText.textContent = "לחץ על 'הפעל סימולציה' לראות מה קורה!";
            }
        }

        function runSimulation() {
            if (isAnimating) return; // Prevent running while animation is active
            isAnimating = true;
            runButton.disabled = true; // Disable button while animating
            runButton.textContent = 'מייצר שלג...';

            const airTemp = parseFloat(airTempSlider.value);
            const waterPressure = parseFloat(waterPressureSlider.value);
            const airPressure = parseFloat(airPressureSlider.value);
            const nucleation = nucleationCheckbox.checked;

            // Clear previous spray with a fade-out effect
            const existingDroplets = sprayArea.querySelectorAll('.droplet');
            existingDroplets.forEach(drop => drop.classList.add('fade-out'));
            // Wait for fade-out before clearing
            setTimeout(() => {
                 sprayArea.innerHTML = '';
                 startNewSpray(airTemp, waterPressure, airPressure, nucleation);
            }, 500); // Duration of fade-out transition

        }

        function startNewSpray(airTemp, waterPressure, airPressure, nucleation) {
            // --- Simulation Logic (Enhanced Heuristics) ---
            // Factors: Adiabatic cooling (airPressure), Evaporative cooling (airTemp, waterPressure), Nucleation (checkbox)

            // Adiabatic cooling: More air pressure = more expansion = more cooling.
            const adiabaticCoolingEffect = (airPressure - 1) * 0.9; // Max ~8.1 deg C drop from this

            // Evaporative cooling potential: Higher water pressure (smaller drops) & warmer/drier air = more potential.
            // Let's assume airTemp is a proxy for dryness here (colder often means less moisture needed for saturation).
            // Evaporation is less effective below 0C, but still happens. More effective if ambient air is warmer (up to a point) and pressure is high (small drops).
            const baseEvaporationPotential = waterPressure * 0.6; // Higher pressure -> smaller drops -> more surface area
            // Actual evaporation cooling depends on ambient temp. It's LESS at very low temps, MORE at temps closer to 0C or slightly above (if dry enough).
            const tempFactor = Math.max(0, 3 - airTemp) / 3; // Factor is higher when airTemp is lower (closer to freezing or below)
            const evaporativeCoolingEffect = baseEvaporationPotential * tempFactor; // Simplified interaction

            // Total initial temperature drop right at the nozzle exit
            const initialWaterTemp = 15; // Assume water starts warmer
            const tempAfterNozzle = initialWaterTemp - adiabaticCoolingEffect - evaporativeCoolingEffect;

            // Further cooling happens as droplets travel
            const travelCoolingFactor = (sprayAreaWidth / 200) * Math.max(0, 5 - airTemp) * 0.5; // More cooling over distance, especially if ambient air isn't super cold

            // Now simulate droplets
            const numDroplets = 80; // More visual droplets
            let frozenCount = 0;
            let supercooledCount = 0;

            for (let i = 0; i < numDroplets; i++) {
                const droplet = document.createElement('div');
                droplet.classList.add('droplet');

                // Initial position near the nozzle outlet
                const startX = nozzleRight;
                const startY = nozzleY + (Math.random() - 0.5) * 15; // Small vertical variation, slightly more spread

                droplet.style.left = `${startX}px`;
                droplet.style.top = `${startY}px`;

                // Simulate temperature change and state dynamically
                const dropletInitialTemp = tempAfterNozzle + (Math.random() - 0.5) * 2; // Small variation
                let currentTemp = dropletInitialTemp;

                // Simulate travel path and cooling over time
                const travelAngle = (Math.random() - 0.5) * 60 * (airPressure/10) ; // Angle of spray, wider with more air pressure
                const endX = sprayAreaWidth - 20; // Stop before the edge
                const endY = nozzleY + Math.tan(travelAngle * Math.PI / 180) * (endX - startX); // Vertical position based on angle

                 // Ensure particles mostly stay within the area
                 const maxSpreadY = sprayAreaHeight * 0.4; // Limit vertical spread
                 const finalY = Math.max(nozzleY - maxSpreadY, Math.min(nozzleY + maxSpreadY, endY));


                // Animate position
                droplet.style.transitionDuration = `${animationDuration / 1000}s`;
                droplet.style.transform = `translate(${endX - startX}px, ${finalY - startY}px)`;


                // Determine state based on *final* temperature and nucleation after travel cooling
                const finalDropletTemp = dropletInitialTemp - travelCoolingFactor + (Math.random()-0.5)*1; // Add final random variation


                // State logic:
                // 1. Starts cooling color
                // 2. If < 0C, transitions to freezing color
                // 3. If conditions met, becomes frozen/snow color
                let finalState = 'liquid'; // Default

                // Use thresholds based on nucleation and temperature
                const freezingThreshold = nucleation ? -0.5 : -3.0; // Freeze easily near 0C with nucleation, needs colder without

                if (finalDropletTemp < 0) {
                     droplet.classList.add('cooling'); // Below 0 but maybe supercooled

                     if (finalDropletTemp <= freezingThreshold) {
                         // Schedule state change after some visual travel time
                         setTimeout(() => {
                            droplet.classList.remove('cooling');
                            droplet.classList.add('freezing'); // Transitioning to solid
                            finalState = 'frozen';

                            // Further check for 'snow' vs 'frozen drop' based on conditions and quality
                             setTimeout(() => {
                                 droplet.classList.remove('freezing');
                                 // Heuristic for snow quality: Very cold ambient AND good freezing conditions
                                 if (airTemp < -2 && finalDropletTemp < -1 && waterPressure > 3 && airPressure > 4) {
                                      droplet.classList.add('snow');
                                 } else {
                                      droplet.classList.add('frozen');
                                 }
                                 frozenCount++; // Count only when visually frozen
                                 updateResultText(numDroplets, frozenCount, supercooledCount); // Update text as droplets finish
                             }, animationDuration * 0.4 + Math.random() * animationDuration * 0.2); // Staggered freezing visual
                         }, animationDuration * 0.3 + Math.random() * animationDuration * 0.2); // Staggered cooling visual

                     } else {
                         // Remains supercooled liquid
                         supercooledCount++;
                         setTimeout(() => {
                             droplet.classList.add('cooling'); // Stays cooling color
                             updateResultText(numDroplets, frozenCount, supercooledCount);
                         }, animationDuration * 0.5 + Math.random() * animationDuration * 0.3);
                     }

                } else {
                    // Remains liquid (above 0C)
                    setTimeout(() => {
                         // No special class needed, remains default blue
                         updateResultText(numDroplets, frozenCount, supercooledCount);
                    }, animationDuration * 0.8 + Math.random() * animationDuration * 0.2); // Still update text after movement
                }

                sprayArea.appendChild(droplet);

                // Remove droplet after animation finishes
                droplet.addEventListener('transitionend', () => {
                    // Use a check to only clean up after the main transform transition
                     if (event.propertyName === 'transform') {
                         droplet.remove();
                         // Check if all droplets are removed to end animation state
                          if (sprayArea.querySelectorAll('.droplet').length === 0) {
                              isAnimating = false;
                              runButton.disabled = false;
                              runButton.textContent = 'הפעל סימולציה';
                              // Final result update if any didn't trigger the state change updates
                              updateResultText(numDroplets, frozenCount, supercooledCount);
                          }
                     }
                });
            } // End droplet loop

             // Initial result text update
             updateResultText(numDroplets, frozenCount, supercooledCount);

        } // End startNewSpray


        function updateResultText(total, frozen, supercooled) {
            const frozenRatio = frozen / total;
            const supercooledRatio = supercooled / total;
            const airTemp = parseFloat(airTempSlider.value);
            const nucleation = nucleationCheckbox.checked;

             let result = "מערבולת קרה..."; // Default while animating

            if (!isAnimating) { // Only show final result after animation
                 if (frozenRatio > 0.8 && airTemp < -2) {
                     result = "🚀 שלג מושלם! תנאים אופטימליים!";
                 } else if (frozenRatio > 0.6 && airTemp <= 0 && nucleation) {
                     result = "✨ יצירת שלג טובה! טיפות קפואות ופתיתים קטנים.";
                 } else if (frozenRatio > 0.4 && airTemp <= 1 && nucleation) {
                     result = "❄️ בעיקר טיפות קפואות וגרגירי קרח גושיים.";
                 } else if (supercooledRatio > 0.5 && airTemp < 0 && !nucleation) {
                      result = "💧 מים נוזליים בקירור יתר (חסרים גרעינים לקפיאה).";
                 } else if (airTemp > 2 && frozenRatio < 0.1) {
                     result = "☀️ חם מדי! רק מים נוזליים מתזים...";
                 }
                 else if (frozenRatio > 0.1) {
                      result = "🥶 התקררות משמעותית, אך בעיקר מים נוזליים או גרגירים בודדים.";
                 }
                 else {
                      result = "💦 מים נוזליים. אין מספיק קירור או שהטמפרטורה גבוהה מדי.";
                 }
                 // Add nuance based on parameters if needed later
            }
            outputText.textContent = result;
        }


        // Event listeners
        airTempSlider.addEventListener('input', updateValues);
        waterPressureSlider.addEventListener('input', updateValues);
        airPressureSlider.addEventListener('input', updateValues);
        nucleationCheckbox.addEventListener('change', updateValues); // Update values display
        runButton.addEventListener('click', runSimulation); // Run sim on button click

        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
             toggleButton.textContent = isHidden ? 'הסתר הסבר על קסם השלג המלאכותי' : 'הצג הסבר על קסם השלג המלאכותי';
        });


        // Initial setup
        updateValues();
         // Ensure initial state is clear and button is enabled
        isAnimating = false;
        runButton.disabled = false;
        runButton.textContent = 'הפעל סימולציה';
         sprayArea.innerHTML = ''; // Clear any initial static content if any

    });
</script>