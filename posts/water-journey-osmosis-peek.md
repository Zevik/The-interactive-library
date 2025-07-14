---
title: "מסע המים: פלירטוט עם אוסמוזה"
english_slug: water-journey-osmosis-peek
category: "ביולוגיה"
tags: [אוסמוזה, ממברנה חדירה למחצה, ריכוז תמיסה, תנועת מים, תא חי, לחץ אוסמוטי]
---
# מסע המים: פלירטוט עם אוסמוזה

דמיינו רגע את התאים הזעירים בגופכם, או את שורשי הצמח הצמא בגינה. איך הם "יודעים" כמה מים להכניס או להוציא? התשובה טמונה באחד התהליכים הכי אלגנטיים וחיוניים בטבע: אוסמוזה. זה לא סתם מעבר מים – זה מסע מים חכם שמתרחש דרך "שומר סף" סודי, ושומר על כל דבר חי במצב מאוזן. בואו נצלול פנימה ונראה את הקסם קורה!

<div class="app-container">
    <div class="controls">
        <h2>הגדירו את התנאים</h2>
        <div class="concentration-input-group">
            <div class="concentration-input left-input">
                <label for="concentration1">ריכוז מומס (צד שמאל %):</label>
                <input type="number" id="concentration1" value="10" min="0" max="50" step="1">
                <span class="validation-msg" id="validation1"></span>
            </div>
            <div class="concentration-input right-input">
                <label for="concentration2">ריכוז מומס (צד ימין %):</label>
                <input type="number" id="concentration2" value="30" min="0" max="50" step="1">
                 <span class="validation-msg" id="validation2"></span>
            </div>
        </div>
        <div class="button-group">
            <button id="start-sim" class="sim-button primary">התחל מסע</button>
            <button id="pause-sim" class="sim-button secondary" style="display: none;">השהה</button>
            <button id="reset-sim" class="sim-button secondary" style="display: none;">אפס</button>
        </div>
    </div>

    <div class="simulation-area">
        <canvas id="osmosisCanvas" width="700" height="350"></canvas>
        <div class="membrane-label">ממברנה סלקטיבית</div>
         <div class="status-overlay">
            <div class="status-left">
                <span id="conc-left">ריכוז: --%</span><br>
                <span id="particles-left">חלקיקים: --</span>
            </div>
             <div class="status-right">
                <span id="conc-right">ריכוז: --%</span><br>
                <span id="particles-right">חלקיקים: --</span>
            </div>
         </div>
         <div id="equilibrium-msg" class="equilibrium-message" style="display: none;">
             שיווי משקל כמעט הושג!
         </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">מה קרה כאן? הצג את המדע מאחורי הקסם</button>

<div id="explanation" style="display: none;">
    <h2>אוסמוזה: הצלילה העמוקה</h2>

    <h3>מה זו אוסמוזה, בעצם?</h3>
    אוסמוזה היא תנועה *ספונטנית* של מים (או כל ממס אחר) דרך קרום חדיר למחצה. התנועה הזו תמיד מתרחשת מהצד שבו ריכוז ה*מומסים* נמוך יותר (מה שאומר שריכוז ה*מים* גבוה יותר) לצד שבו ריכוז המומסים גבוה יותר (ריכוז המים נמוך יותר). המטרה של התהליך הזה היא לנסות ולאזן את ריכוזי המומסים משני הצדדים. זה כמו שמולקולות מים פשוט "נדחפות" סטטיסטית מאזור שבו יש להן יותר מקום (פחות מומסים מפריעים) לאזור שבו יש להן פחות מקום. התהליך הזה קריטי לחיים - הוא מאפשר לצמחים לשאוב מים מהאדמה, עוזר לתאים שלנו לשמור על צורתם התקינה, וחיוני לתפקוד הכליות.

    <h3>הגיבור השקט: הממברנה החדירה למחצה</h3>
    חשבו על הממברנה הזו כשומר סף חכם ובררן. היא לא סתם חור בגדר, אלא מחסום מתוחכם (בממברנות ביולוגיות, לרוב זה קרום התא) שיש בו "דלתות" או "מעברים" מיוחדים. הדלתות הללו, שנקראות לרוב אקוופורינים כשמדובר במים, קטנות מספיק כדי לאפשר למולקולות המים הקטנות והזריזות לעבור דרכן יחסית בחופשיות, אבל גדולות מדי עבור רוב מולקולות המומסים (כמו מלחים, סוכרים וחלבונים גדולים). הבררנות הזו היא סוד הקסם של אוסמוזה; בלעדיה, גם המומסים היו פשוט עוברים ומתאזנים, ולא היתה תנועת מים ייחודית.

    <h3>מפל הריכוזים: המנוע של האוסמוזה</h3>
    הכוח שמניע את אוסמוזה הוא ההבדל בריכוזי המומסים בין שני הצדדים. קל לחשוב על זה הפוך: כשיש יותר מומסים בצד אחד, יש פחות "מקום פנוי" למולקולות מים באותו נפח בהשוואה לצד עם פחות מומסים. זה אומר שריכוז המים בצד עם המומסים הגבוהים - נמוך יותר. המים, שנעים כל הזמן באקראי לכל הכיוונים, פשוט יש להם סיכוי סטטיסטי גבוה יותר "לפגוש" את הממברנה ולהצליח לעבור מהצד שבו הם צפופים יותר (ריכוז מים גבוה / מומס נמוך) לצד שבו הם פחות צפופים (ריכוז מים נמוך / מומס גבוה). זה כמו נהר שזורם מרום גבוה לנמוך – המים תמיד זורמים מאיפה שיש יותר מהם לאיפה שיש פחות, כל עוד אין מחסום מוחלט.

    <h3>הזרימה נטו: לאן המים באמת הולכים?</h3>
    חשוב להבין: מולקולות מים עוברות את הממברנה בשני הכיוונים כל הזמן! אבל כשיש מפל ריכוזים, קצב המעבר מהצד המהול (פחות מומסים) לצד המרוכז (יותר מומסים) – גבוה יותר. ההפרש הזה בקצבי המעבר הוא מה שאנחנו רואים כ"תנועת מים נטו". כלומר, בסך הכל, יותר מים עוברים מהצד עם ריכוז המומסים הנמוך לצד עם ריכוז המומסים הגבוה, וזה ממשיך להתרחש עד שמשהו משתנה.

    <h3>הסוף הטוב? מצב שיווי משקל</h3>
    המסע האוסמוטי נמשך עד שמערכת מגיעה לשיווי משקל. במערכות גמישות (כמו תא), מים ימשיכו להיכנס או לצאת עד שריכוז המומסים משתווה משני הצדדים (או שהתא מתפקע/מתכווץ). במערכת עם דפנות קשיחות (כמו בסימולציה שלנו, עם הסייג של "מפלס המים"), תנועת המים גורמת לצד המרוכז "להתמלא" יותר. המים העודפים הללו יוצרים לחץ הידרוסטטי (לחץ של נוזל) שדוחף חזרה כנגד תנועת המים הנכנסת. שיווי המשקל מושג כאשר הלחץ ההידרוסטטי הזה מתאזן עם הנטייה האוסמוטית של המים להיכנס. בנקודה זו, למרות שמולקולות מים עדיין עוברות בשני הכיוונים, קצב המעבר הפך להיות שווה, ולכן אין יותר תנועת מים נטו והמפלסים (בסימולציה) או הריכוזים (במציאות גמישה) נשארים יציבים. הלחץ שנוצר במצב שיווי משקל במערכת קשיחה נקרא "הלחץ האוסמוטי".
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    .app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: 'Heebo', sans-serif;
        margin: 20px auto; /* Center the container */
        padding: 20px;
        border-radius: 12px;
        background-color: #f0f4f8; /* Soft blue-grey background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        max-width: 750px; /* Limit max width */
        width: 95%; /* Responsive width */
        box-sizing: border-box; /* Include padding in width */
    }

    .controls {
        width: 100%; /* Full width within container */
        margin-bottom: 25px;
        text-align: center;
    }

    .controls h2 {
        color: #004080; /* Dark blue heading */
        margin-top: 0;
        margin-bottom: 20px;
        font-weight: 700;
    }

    .concentration-input-group {
        display: flex;
        justify-content: center;
        gap: 20px; /* Space between inputs */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .concentration-input {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-bottom: 15px;
        background-color: #ffffff; /* White background for inputs */
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid #cce5ff; /* Light blue border */
        position: relative; /* Needed for validation message positioning */
    }

     .concentration-input.invalid {
        border-color: #dc3545; /* Red border for invalid input */
     }


    .concentration-input label {
        margin-bottom: 8px;
        font-weight: 400;
        color: #333;
        font-size: 0.95em;
    }

    .concentration-input input[type="number"] {
        padding: 8px 12px;
        border: 1px solid #b8daff; /* Medium blue border */
        border-radius: 4px;
        font-size: 1em;
        width: 80px; /* Fixed width for input */
        text-align: center;
        -moz-appearance: textfield; /* Hide arrow buttons in Firefox */
    }

     .concentration-input input[type="number"]::-webkit-outer-spin-button,
     .concentration-input input[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none; /* Hide arrow buttons in Chrome, Safari, Edge */
        margin: 0;
     }

    .validation-msg {
        position: absolute;
        bottom: -18px; /* Position below input */
        left: 0;
        right: 0;
        text-align: center;
        font-size: 0.8em;
        color: #dc3545; /* Red color */
        height: 16px; /* Reserve space */
    }


    .button-group {
        margin-top: 10px;
    }

    .sim-button {
        padding: 10px 20px;
        font-size: 1.1em;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 700;
        margin: 0 5px; /* Space between buttons */
    }

    .sim-button.primary {
        background-color: #007bff; /* Blue */
        color: white;
    }

    .sim-button.primary:hover {
        background-color: #0056b3; /* Darker blue */
        transform: translateY(-1px); /* Slight lift effect */
    }

     .sim-button.secondary {
        background-color: #6c757d; /* Grey */
        color: white;
     }

    .sim-button.secondary:hover {
        background-color: #545b62; /* Darker grey */
         transform: translateY(-1px);
    }

    .sim-button:active {
        transform: translateY(0); /* Press effect */
    }

    .sim-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }


    .simulation-area {
        position: relative;
        width: 700px;
        height: 350px;
        border: 2px solid #004080; /* Stronger border */
        border-radius: 8px;
        overflow: hidden; /* Keep particles inside */
        background-color: #e0f7fa; /* Light blue base for water */
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1); /* Inner shadow */
    }

     /* Added for responsiveness */
    @media (max-width: 768px) {
        .simulation-area {
            width: 100%; /* Full width on smaller screens */
            height: 250px; /* Adjust height */
        }
        .app-container {
            padding: 15px;
        }
         .concentration-input-group {
             flex-direction: column; /* Stack inputs */
             align-items: center;
             gap: 10px;
         }
         .concentration-input {
             width: 80%; /* Make input areas wider */
         }
         .sim-button {
             margin-bottom: 10px; /* Space out stacked buttons */
         }
    }


    #osmosisCanvas {
        display: block;
        border: none; /* Border handled by simulation-area */
    }

    .membrane-label {
        position: absolute;
        top: 5px; /* Position above the membrane line */
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.9em;
        color: #004080; /* Dark blue */
        font-weight: bold;
        white-space: nowrap; /* Prevent wrapping */
        z-index: 10; /* Ensure it's above canvas */
    }

    .status-overlay {
        position: absolute;
        top: 10px;
        width: 100%;
        display: flex;
        justify-content: space-around;
        font-weight: bold;
        color: #004080;
        font-size: 0.9em;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5); /* White text shadow for readability */
        z-index: 10; /* Ensure it's above canvas */
    }

    .status-left, .status-right {
        width: 50%;
        text-align: center;
    }

    .equilibrium-message {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 224, 0.9); /* Light yellow with transparency */
        color: #333;
        padding: 8px 15px;
        border-radius: 20px; /* Rounded corners */
        font-size: 1em;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        z-index: 10; /* Ensure it's above canvas */
    }


    .toggle-button {
        display: block;
        margin: 25px auto;
        padding: 12px 20px;
        font-size: 1em;
        cursor: pointer;
        border: 1px solid #007bff;
        border-radius: 20px;
        background-color: #e9ecef; /* Light grey */
        color: #007bff; /* Blue text */
        transition: background-color 0.3s ease, color 0.3s ease;
        font-weight: 700;
    }

    .toggle-button:hover {
        background-color: #007bff;
        color: white;
    }

    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #cce5ff; /* Light blue border */
        border-radius: 8px;
        background-color: #ffffff; /* White background */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        font-family: 'Heebo', sans-serif;
    }

    #explanation h2 {
        color: #004080;
        margin-top: 0;
        margin-bottom: 15px;
        font-weight: 700;
        border-bottom: 2px solid #b8daff; /* Underline effect */
        padding-bottom: 5px;
    }

    #explanation h3 {
        color: #0056b3;
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: 700;
    }

    #explanation p {
        line-height: 1.7;
        color: #333;
        margin-bottom: 15px;
        font-weight: 400;
    }
</style>

<script>
    const canvas = document.getElementById('osmosisCanvas');
    const ctx = canvas.getContext('2d');
    const concentrationInput1 = document.getElementById('concentration1');
    const concentrationInput2 = document.getElementById('concentration2');
    const validationMsg1 = document.getElementById('validation1');
    const validationMsg2 = document.getElementById('validation2');
    const startButton = document.getElementById('start-sim');
    const pauseButton = document.getElementById('pause-sim');
    const resetButton = document.getElementById('reset-sim');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const concLeftSpan = document.getElementById('conc-left');
    const particlesLeftSpan = document.getElementById('particles-left');
    const concRightSpan = document.getElementById('conc-right');
    const particlesRightSpan = document.getElementById('particles-right');
    const equilibriumMsgDiv = document.getElementById('equilibrium-msg');


    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;
    const membraneX = canvasWidth / 2;
    const particleRadius = 3; // Slightly larger for better visibility
    const maxParticles = 2000; // Increased particle count for denser simulation
    const simulationSpeed = 1.5; // Adjusted speed
    const wallPadding = particleRadius; // Keep particles slightly away from edges

    const waterColor = '#4FC3F7'; // Brighter blue
    const soluteColor = '#FF7043'; // Orange-red
    const membraneColor = '#0D47A1'; // Darker blue for membrane

    let particles = [];
    let animationFrameId = null;
    let isRunning = false;
    let initialParticleCountPerTank;
    let particleCounts = {
        left: { water: 0, solute: 0, total: 0 },
        right: { water: 0, solute: 0, total: 0 }
    };
    let lastStatsUpdateTime = 0;
    const statsUpdateInterval = 100; // Update stats every 100ms

    // Store initial positions to reset smoothly
    let initialParticleStates = [];


    // Function to validate input
    function validateInput(inputElement, msgElement) {
        const value = parseFloat(inputElement.value);
        if (isNaN(value) || value < 0 || value > 50) {
            msgElement.textContent = '0-50%';
            inputElement.parentElement.classList.add('invalid');
            return false;
        } else {
            msgElement.textContent = ''; // Clear message
            inputElement.parentElement.classList.remove('invalid');
            return true;
        }
    }

    // Event listeners for input validation
    concentrationInput1.addEventListener('input', () => validateInput(concentrationInput1, validationMsg1));
    concentrationInput2.addEventListener('input', () => validateInput(concentrationInput2, validationMsg2));


    // Function to initialize particles based on concentrations
    function initializeParticles() {
        particles = [];
        initialParticleStates = []; // Clear previous states

        const conc1 = parseFloat(concentrationInput1.value) / 100; // Percentage to fraction
        const conc2 = parseFloat(concentrationInput2.value) / 100;

        // Validate inputs before proceeding
        const input1Valid = validateInput(concentrationInput1, validationMsg1);
        const input2Valid = validateInput(concentrationInput2, validationMsg2);
        if (!input1Valid || !input2Valid) {
             alert('אנא הזינו ריכוזים תקינים בין 0% ל-50%.');
             return false; // Indicate invalid input
        }

         // Distribute total particles evenly initially
        initialParticleCountPerTank = maxParticles / 2;

        const numSolute1 = Math.round(initialParticleCountPerTank * conc1);
        const numWater1 = Math.round(initialParticleCountPerTank * (1 - conc1));

        const numSolute2 = Math.round(initialParticleCountPerTank * conc2);
        const numWater2 = Math.round(initialParticleCountPerTank * (1 - conc2));

        // Adjust counts slightly if needed due to rounding, ensuring total is maxParticles
        const currentTotal = numSolute1 + numWater1 + numSolute2 + numWater2;
        const diff = maxParticles - currentTotal;
        // Distribute difference (e.g., add/remove water particles)
        if (diff > 0) { numWater1 += diff; }
        else if (diff < 0) { numWater1 += diff; } // Subtract diff (add negative)

        // Ensure counts are non-negative
        const finalNumSolute1 = Math.max(0, numSolute1);
        const finalNumWater1 = Math.max(0, numWater1);
        const finalNumSolute2 = Math.max(0, numSolute2);
        const finalNumWater2 = Math.max(0, numWater2);

        // Create particles for Tank 1 (Left)
        for (let i = 0; i < finalNumSolute1; i++) {
             const p = {
                x: wallPadding + Math.random() * (membraneX - wallPadding * 2),
                y: wallPadding + Math.random() * (canvasHeight - wallPadding * 2),
                type: 'solute', // Mומס
                vx: (Math.random() - 0.5) * simulationSpeed,
                vy: (Math.random() - 0.5) * simulationSpeed,
                tank: 1,
                color: soluteColor
            };
             particles.push(p);
             initialParticleStates.push({...p}); // Store initial state
        }
        for (let i = 0; i < finalNumWater1; i++) {
            const p = {
                x: wallPadding + Math.random() * (membraneX - wallPadding * 2),
                y: wallPadding + Math.random() * (canvasHeight - wallPadding * 2),
                type: 'water', // מים
                vx: (Math.random() - 0.5) * simulationSpeed * 1.5, // Water moves slightly faster
                vy: (Math.random() - 0.5) * simulationSpeed * 1.5,
                 tank: 1,
                 color: waterColor
            };
             particles.push(p);
             initialParticleStates.push({...p}); // Store initial state
        }

        // Create particles for Tank 2 (Right)
        for (let i = 0; i < finalNumSolute2; i++) {
            const p = {
                x: membraneX + wallPadding + Math.random() * (membraneX - wallPadding * 2),
                y: wallPadding + Math.random() * (canvasHeight - wallPadding * 2),
                type: 'solute', // Mומס
                vx: (Math.random() - 0.5) * simulationSpeed,
                vy: (Math.random() - 0.5) * simulationSpeed,
                tank: 2,
                color: soluteColor
            };
             particles.push(p);
             initialParticleStates.push({...p}); // Store initial state
        }
         for (let i = 0; i < finalNumWater2; i++) {
            const p = {
                x: membraneX + wallPadding + Math.random() * (membraneX - wallPadding * 2),
                y: wallPadding + Math.random() * (canvasHeight - wallPadding * 2),
                type: 'water', // מים
                vx: (Math.random() - 0.5) * simulationSpeed * 1.5,
                vy: (Math.random() - 0.5) * simulationSpeed * 1.5,
                 tank: 2,
                 color: waterColor
            };
             particles.push(p);
             initialParticleStates.push({...p}); // Store initial state
        }

        // Shuffle particles to mix them visually
        particles.sort(() => Math.random() - 0.5);

        updateStats(); // Calculate initial stats
        return true; // Indicate valid input and initialization
    }

    // Function to update particle counts and concentrations
    function updateStats() {
        let waterLeft = 0, soluteLeft = 0;
        let waterRight = 0, soluteRight = 0;

        particles.forEach(p => {
            if (p.tank === 1) {
                if (p.type === 'water') waterLeft++;
                else soluteLeft++;
            } else {
                if (p.type === 'water') waterRight++;
                else soluteRight++;
            }
        });

        particleCounts = {
            left: { water: waterLeft, solute: soluteLeft, total: waterLeft + soluteLeft },
            right: { water: waterRight, solute: soluteRight, total: waterRight + soluteRight }
        };

        const totalParticles = particleCounts.left.total + particleCounts.right.total;
        const totalInitialParticlesPerTank = maxParticles / 2; // Use initial for concentration calc base

        // Calculate concentration based on INITIAL number of particles that *could* fit
        // This gives a percentage relative to the total capacity, even if volume changes
        const concLeft = particleCounts.left.solute / totalInitialParticlesPerTank * 100;
        const concRight = particleCounts.right.solute / totalInitialParticlesPerTank * 100;


        // Update UI text
        concLeftSpan.textContent = `ריכוז: ${concLeft.toFixed(1)}%`;
        particlesLeftSpan.textContent = `חלקיקים: ${particleCounts.left.total}`;
        concRightSpan.textContent = `ריכוז: ${concRight.toFixed(1)}%`;
        particlesRightSpan.textContent = `חלקיקים: ${particleCounts.right.total}`;

        // Check for approximate equilibrium (net water flow slows down)
         checkEquilibrium();
    }

    // Function to draw the current state
    function draw() {
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Calculate current water levels based on particle count ratio relative to initial fill height
        const initialHeight = canvasHeight; // Initial "fill height" was the whole tank
        const initialParticlesLeft = maxParticles / 2; // Initial particles in left tank
        const initialParticlesRight = maxParticles / 2; // Initial particles in right tank

        // Current height ratio is current particles / initial particles
        const currentHeightLeft = (particleCounts.left.total / initialParticlesLeft) * initialHeight;
        const currentHeightRight = (particleCounts.right.total / initialParticlesRight) * initialHeight;

        // Draw water background based on calculated levels
        // Left tank
        ctx.fillStyle = '#E1F5FE'; // Very light blue base
        ctx.fillRect(0, canvasHeight - currentHeightLeft, membraneX, currentHeightLeft);
        // Right tank
        ctx.fillStyle = '#E1F5FE';
        ctx.fillRect(membraneX, canvasHeight - currentHeightRight, membraneX, currentHeightRight);


        // Draw membrane line
        ctx.beginPath();
        ctx.moveTo(membraneX, 0);
        ctx.lineTo(membraneX, canvasHeight);
        ctx.strokeStyle = membraneColor;
        ctx.lineWidth = 4; // Thicker line
        ctx.stroke();

        // Draw particles *within* their current tank area and calculated water level
        particles.forEach(p => {
             const currentHeight = p.tank === 1 ? currentHeightLeft : currentHeightRight;
             const tankTopY = canvasHeight - currentHeight;

             // Only draw if particle is within the calculated water level area
             if (p.y > tankTopY - particleRadius) { // Allow particle edge to slightly go above line
                ctx.beginPath();
                ctx.arc(p.x, p.y, particleRadius, 0, Math.PI * 2);
                ctx.fillStyle = p.color;
                ctx.fill();
             }
        });
    }

     // Function to check for equilibrium
     function checkEquilibrium() {
        if (!isRunning) return;

        // Simple check: if particle counts per tank are getting very close to balancing
        // or if net water flow is very slow.
        // A more accurate check would be monitoring the net water flow rate over time.
        // For this simulation, let's use particle count difference relative to total.
        const diff = Math.abs(particleCounts.left.water - particleCounts.right.water);
        const totalWater = particleCounts.left.water + particleCounts.right.water;

        // Define a threshold for equilibrium (e.g., difference is less than 2% of total water particles)
        const equilibriumThreshold = totalWater * 0.02; // 2% of total water particles

        // Also check if the *rate* of change is slow
        // This requires tracking historical counts, which adds complexity.
        // Let's simplify: if the difference is small AND simulation has run for a bit.

        const minParticlesForEquilibrium = maxParticles * 0.4; // Only check if enough particles exist (should always be true)


        if (particleCounts.left.total > minParticlesForEquilibrium && particleCounts.right.total > minParticlesForEquilibrium) {
            if (diff < equilibriumThreshold) {
                 equilibriumMsgDiv.style.display = 'block';
            } else {
                 equilibriumMsgDiv.style.display = 'none';
            }
        } else {
             equilibriumMsgDiv.style.display = 'none'; // Don't show message if tanks are nearly empty (shouldn't happen)
        }
     }


    // Function to update particle positions
    function update() {
        const now = performance.now(); // Get current time
        const elapsed = now - lastStatsUpdateTime;

        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;

            // Bounce off top/bottom walls (considering current water level)
            const currentHeight = p.tank === 1 ? (particleCounts.left.total / (maxParticles/2)) * canvasHeight : (particleCounts.right.total / (maxParticles/2)) * canvasHeight;
            const tankTopY = canvasHeight - currentHeight;


            if (p.y - particleRadius < tankTopY) { // Check if top edge is above water level top
                p.vy *= -1;
                p.y = tankTopY + particleRadius; // Snap to boundary
            } else if (p.y + particleRadius > canvasHeight) { // Check if bottom edge is below canvas bottom
                 p.vy *= -1;
                 p.y = canvasHeight - particleRadius; // Snap to boundary
            }


            // Handle membrane interaction
            if (p.tank === 1) { // Particle in left tank
                if (p.x + particleRadius > membraneX) { // Check if right edge crossed membrane line
                    if (p.type === 'water') {
                        // Water crosses
                        p.tank = 2;
                        p.x = membraneX + (membraneX - (p.x + particleRadius)) + particleRadius; // Reflect position relative to membrane line and add radius back
                        // Add a slight boost in crossing direction to emphasize movement
                        p.vx = Math.abs(p.vx) * simulationSpeed * 0.8; // Ensure moving right
                    } else {
                        // Solute bounces back
                        p.x = membraneX - (p.x + particleRadius - membraneX) - particleRadius; // Reflect position relative to membrane line
                        p.vx *= -1; // Reverse velocity
                    }
                }
                // Bounce off left wall
                 if (p.x - particleRadius < 0) {
                    p.vx *= -1;
                    p.x = particleRadius; // Snap to boundary
                 }

            } else { // Particle in right tank
                 if (p.x - particleRadius < membraneX) { // Check if left edge crossed membrane line
                    if (p.type === 'water') {
                        // Water crosses
                        p.tank = 1;
                        p.x = membraneX - (membraneX - (p.x - particleRadius)) - particleRadius; // Reflect position relative to membrane line and subtract radius back
                         // Add a slight boost in crossing direction
                        p.vx = -Math.abs(p.vx) * simulationSpeed * 0.8; // Ensure moving left

                    } else {
                        // Solute bounces back
                        p.x = membraneX + (membraneX - (p.x - particleRadius)) + particleRadius; // Reflect position relative to membrane line
                        p.vx *= -1; // Reverse velocity
                    }
                }
                 // Bounce off right wall
                 if (p.x + particleRadius > canvasWidth) {
                    p.vx *= -1;
                    p.x = canvasWidth - particleRadius; // Snap to boundary
                 }
            }

             // Gentle random walk adjustments
            p.vx += (Math.random() - 0.5) * 0.1;
            p.vy += (Math.random() - 0.5) * 0.1;

            // Limit speed
            const speed = Math.sqrt(p.vx * p.vx + p.vy * p.vy);
            const maxSpeed = p.type === 'water' ? simulationSpeed * 2.5 : simulationSpeed * 1.5;
            if (speed > maxSpeed) {
                p.vx = (p.vx / speed) * maxSpeed;
                p.vy = (p.vy / speed) * maxSpeed;
            }
        });

         // Update stats periodically
        if (elapsed > statsUpdateInterval) {
             updateStats();
             lastStatsUpdateTime = now;
        }
    }

    // Animation loop
    function animate() {
        if (!isRunning) {
            cancelAnimationFrame(animationFrameId);
            return;
        }

        update();
        draw();
        animationFrameId = requestAnimationFrame(animate);
    }

    // Start button logic
    startButton.addEventListener('click', () => {
        // Validate inputs first
        const input1Valid = validateInput(concentrationInput1, validationMsg1);
        const input2Valid = validateInput(concentrationInput2, validationMsg2);
        if (!input1Valid || !input2Valid) {
            alert('אנא תקנו את שגיאות הריכוז לפני התחלת הסימולציה.');
            return; // Stop if validation failed
        }

        if (!isRunning) {
            // Initialize only if particles are empty or inputs were re-enabled (after reset)
             if (particles.length === 0 || concentrationInput1.disabled === false) {
                 if (!initializeParticles()) {
                    return; // Stop if initialization failed (e.g., invalid input caught later)
                 }
             }
            isRunning = true;
            startButton.style.display = 'none';
            pauseButton.style.display = 'inline-block';
             resetButton.style.display = 'inline-block';
             concentrationInput1.disabled = true;
             concentrationInput2.disabled = true;
             equilibriumMsgDiv.style.display = 'none'; // Hide equilibrium message on start

             lastStatsUpdateTime = performance.now(); // Reset timer for stats
             updateStats(); // Initial stats update immediately
            animate(); // Start the animation loop
        }
    });

    // Pause button logic
    pauseButton.addEventListener('click', () => {
        if (isRunning) {
            isRunning = false;
            cancelAnimationFrame(animationFrameId);
            startButton.style.display = 'inline-block';
            pauseButton.style.display = 'none';
        }
    });

     // Reset button logic
    resetButton.addEventListener('click', () => {
        isRunning = false;
        cancelAnimationFrame(animationFrameId);

        // Restore particles to initial states if available, otherwise re-initialize
        if (initialParticleStates.length > 0) {
            particles = initialParticleStates.map(p => ({...p})); // Create deep copies
        } else {
            // If no initial state saved (e.g., direct page load), re-initialize normally
            initializeParticles(); // This also saves initial state
        }

        ctx.clearRect(0, 0, canvasWidth, canvasHeight); // Clear canvas
        updateStats(); // Update stats based on reset state
        draw(); // Draw reset state

        startButton.style.display = 'inline-block';
        pauseButton.style.display = 'none';
        resetButton.style.display = 'none';
         concentrationInput1.disabled = false;
         concentrationInput2.disabled = false;
         equilibriumMsgDiv.style.display = 'none'; // Hide equilibrium message on reset
         validateInput(concentrationInput1, validationMsg1); // Re-validate inputs to clear errors
         validateInput(concentrationInput2, validationMsg2);
    });


    // Toggle explanation
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג את המדע מאחורי הקסם';
        }
    });

    // Initial state setup
    initializeParticles(); // Initialize particles based on default input values
    updateStats(); // Calculate initial stats
    draw(); // Draw the initial state

</script>
```