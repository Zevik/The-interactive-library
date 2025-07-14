---
title: "סימולציית ברירה טבעית של עשים"
english_slug: moth-natural-selection-game
category: "מדעי החיים / ביולוגיה"
tags: [אבולוציה, ברירה טבעית, סימולציה]
---
# סימולציית ברירה טבעית של עשים: משחק ההישרדות

מה קובע מי שורד ומי נטרף במשחק החיים של עולם הטבע? איך סביבה משתנה מכתיבה את גורלם של יצורים שונים? היכנסו לסימולציה מרתקת שתאפשר לכם לשחק עם אוכלוסיית עשים בגוונים שונים החיים על גזעי עצים, ולראות כיצד צבעם משפיע ישירות על סיכויי ההישרדות וההתרבות שלהם לאורך דורות. זו לא רק הדמיה, זה משחק הישרדות אבולוציוני שאתם מנהלים!

<div id="simulation-container">
    <div id="tree-area">
        <!-- Moths will be added here by JavaScript -->
        <div id="moth-template" class="moth" style="display: none;"></div>
    </div>
    <div id="controls-panel">
        <div class="control-group">
            <label for="tree-color-select">סביבת עץ:</label>
            <select id="tree-color-select">
                <option value="dark">כהה (עץ מזוהם / כהה)</option>
                <option value="light">בהיר (עץ נקי / בהיר)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="starting-moths">עשים התחלתיים (סה"כ):</label>
            <input type="number" id="starting-moths" value="100" min="20" max="500">
        </div>
         <div class="control-group">
            <label for="predation-rate">עדיפות טריפה (עשים בולטים):</label>
            <input type="number" id="predation-rate" value="75" min="10" max="95">%
        </div>
        <button id="start-sim-button">התחל סימולציה</button>
        <button id="reset-sim-button" disabled>אתחל</button>
        <div id="simulation-status">
            <p>דור: <span id="generation-count">0</span></p>
            <p>עשים בהירים: <span id="light-moths-count">0</span></p>
            <p>עשים כהים: <span id="dark-moths-count">0</span></p>
        </div>
        <div id="graph-container">
            <h4>אוכלוסיית עשים לאורך דורות:</h4>
            <canvas id="population-graph"></canvas>
        </div>
    </div>
</div>

<button id="toggle-explanation-button" aria-expanded="false">הסבר מדעי: מה קורה כאן בעצם?</button>

<div id="explanation-section" style="display: none;">
    <h2>ברירה טבעית בפעולה: הסבר מעמיק</h2>
    <p>הסימולציה שחוויתם מדגימה את אחד המנועים החזקים ביותר של שינוי בטבע: **ברירה טבעית**. דמיינו אוכלוסייה של עשים (סוג של פרפרים ליליים) בשני צבעים - בהיר וכהה - החיים בסביבה של גזעי עצים המשמשים להם בית ומחסה מפני טורפים.</p>
    <p>בסביבה שבה גזעי העצים בהירים (כמו יער לפני שהזיהום התעשייתי שינה את צבעם, או באזורים נקיים), העשים הבהירים נהנים מיתרון עצום: הם מוסווים היטב על הרקע הבהיר. הטורפים שלהם, לרוב ציפורים, מתקשים להבחין בהם. לעומת זאת, העשים הכהים בולטים על הרקע הבהיר, מה שהופך אותם למטרה קלה עבור הטורפים.</p>
    <p>כשהטורפים פעילים, רוב העשים הכהים נאכלים, בעוד שעשים בהירים רבים יותר שורדים. העשים שנותרים בחיים הם אלה שמתרבים ומעבירים את תכונת הצבע שלהם לצאצאים. עם כל דור שעובר, היחס באוכלוסייה משתנה: מספר העשים הבהירים גדל, בעוד שמספר העשים הכהים קטן. זהו תהליך של **הסתגלות**: האוכלוסייה הופכת מותאמת יותר לסביבה הבהירה.</p>
    <p>ומה קורה כשהסביבה משתנה? דמיינו את המהפכה התעשייתית שהביאה לזיהום אוויר נרחב. הפיח כיסה את גזעי העצים והפך אותם לכהים. לפתע, היתרון התהפך! העשים הכהים הפכו למוסווים על הרקע הכהה, בעוד שהעשים הבהירים הפכו לבולטים ופגיעים. הטורפים החלו לטרוף יותר עשים בהירים, ואילו העשים הכהים ששרדו התרבו. לאורך דורות, אוכלוסיית העשים באזורים המזוהמים נעשתה כהה יותר ויותר.</p>
    <p>הסימולציה שלכם מאפשרת לראות באופן ויזואלי ואינטראקטיבי כיצד שינוי פשוט בצבע העץ (הסביבה) משפיע באופן דרמטי על סיכויי ההישרדות של הפרטים השונים באוכלוסייה, ובכך מעצב את גורל האוכלוסייה כולה לאורך זמן. זהו העיקרון הבסיסי של ברירה טבעית: הסביבה "בוררת" את התכונות (כמו צבע העש) המאפשרות סיכוי הישרדות והתרבות גבוה יותר, והתכונות הללו הופכות שכיחות יותר באוכלוסייה מדור לדור. זהו אחד המנגנונים המרכזיים המניעים את תהליך האבולוציה.</p>
</div>

<style>
    :root {
        --color-light-moth: #f0e6d6; /* Soft white/beige */
        --color-dark-moth: #333;     /* Dark gray/nearly black */
        --color-light-bark: #d4c7b6; /* Light brown/grey bark */
        --color-dark-bark: #4a3b2d;  /* Dark brown bark */
        --color-ui-bg: #eef;        /* Light blueish-gray for controls */
        --color-border: #ccc;
        --color-success-button: #4CAF50;
        --color-success-button-hover: #45a049;
        --color-info-button: #008CBA;
        --color-info-button-hover: #007bb5;
        --color-disabled: #cccccc;
        --border-radius-base: 8px;
        --spacing-base: 15px;
    }

    body {
        font-family: 'Arial', sans-serif; /* Use a common sans-serif font */
        line-height: 1.6;
        color: #333;
    }

    #simulation-container {
        display: flex;
        flex-direction: column;
        gap: var(--spacing-base);
        max-width: 900px;
        margin: 20px auto;
        padding: var(--spacing-base);
        border: 1px solid var(--color-border);
        border-radius: var(--border-radius-base);
        background-color: #fff; /* White background for container */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #tree-area {
        width: 100%;
        height: 400px;
        position: relative;
        border-radius: var(--border-radius-base);
        overflow: hidden;
        background-size: cover;
        background-position: center;
        transition: background-image 1.5s ease-in-out, background-color 1.5s ease-in-out; /* Smoother transition */
        border: 1px solid var(--color-border);
    }

    #tree-area.dark {
        /* Using Unsplash Source for varied textures - check license if for production use */
        /* Or simpler: background-image: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.1)), url('https://via.placeholder.com/800x400/4a3b2d/4a3b2d?text=');*/
         background-image: url('https://source.unsplash.com/800x400/?dark-bark,tree-texture');
         background-color: var(--color-dark-bark);
    }

    #tree-area.light {
        /* background-image: linear-gradient(rgba(255,255,255,0.1), rgba(255,255,255,0.1)), url('https://via.placeholder.com/800x400/d4c7b6/d4c7b6?text='); */
        background-image: url('https://source.unsplash.com/800x400/?light-bark,tree-texture');
        background-color: var(--color-light-bark);
    }

    .moth {
        position: absolute;
        width: 15px; /* Slightly larger */
        height: 15px;
        border-radius: 50%;
        /* Removed default black */
        box-shadow: 0 0 4px rgba(0,0,0,0.4); /* Stronger shadow */
        transition: transform 0.7s ease-out, opacity 0.7s ease-out; /* Animation for movement/removal */
         /* Add a slight random initial rotation */
        transform: translate(-50%, -50%) rotate(calc(var(--random-rotation, 0) * 1deg)); /* Use CSS variable for random initial rotation */
    }

    .moth.light { background-color: var(--color-light-moth); border: 1px solid rgba(0,0,0,0.1); } /* Add subtle border */
    .moth.dark { background-color: var(--color-dark-moth); border: 1px solid rgba(255,255,255,0.1); } /* Add subtle border */

    /* Animation for moths being eaten */
    .moth.eaten {
        opacity: 0;
        transform: scale(0.2) rotate(calc(var(--random-rotation, 0) * 1deg)); /* Shrink and rotate */
    }

     /* Animation for new moths appearing */
    .moth.new {
         opacity: 0;
         transform: scale(0.5) rotate(calc(var(--random-rotation, 0) * 1deg));
         animation: fade-in-moth 0.5s ease-out forwards;
    }

    @keyframes fade-in-moth {
        to {
            opacity: 1;
            transform: scale(1) rotate(calc(var(--random-rotation, 0) * 1deg));
        }
    }


    #controls-panel {
        display: flex;
        flex-wrap: wrap;
        gap: var(--spacing-base);
        padding: var(--spacing-base);
        background-color: var(--color-ui-bg);
        border-radius: var(--border-radius-base);
        align-items: flex-end; /* Align items to bottom */
        justify-content: center;
        font-size: 0.95em;
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 5px;
        min-width: 120px; /* Give controls some minimum width */
    }

    .control-group label {
        font-weight: bold;
        font-size: 0.9em; /* Slightly smaller labels */
        color: #555;
    }

    .control-group select,
    .control-group input[type="number"] {
        padding: 10px; /* More padding */
        border: 1px solid var(--color-border);
        border-radius: 5px; /* Slightly larger radius */
        font-size: 1em;
        width: 100%; /* Make inputs fill container */
        box-sizing: border-box; /* Include padding and border in width */
    }

    #controls-panel button {
        padding: 10px 15px; /* More padding */
        border: none;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        min-width: 100px; /* Minimum width for buttons */
        text-align: center;
    }

    #start-sim-button {
        background-color: var(--color-success-button);
        color: white;
    }

    #start-sim-button:hover:not(:disabled) {
        background-color: var(--color-success-button-hover);
    }

     #reset-sim-button {
         background-color: #e74c3c; /* Red color for reset */
         color: white;
     }

     #reset-sim-button:hover:not(:disabled) {
         background-color: #c0392b;
     }


     #controls-panel button:active:not(:disabled) {
        opacity: 0.8;
    }

     #controls-panel button:disabled {
        background-color: var(--color-disabled);
        cursor: not-allowed;
        opacity: 0.6;
    }


    #simulation-status {
        margin-top: 10px;
        font-weight: bold;
        text-align: center;
        min-width: 150px;
        background-color: #fff;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid var(--color-border);
    }

    #simulation-status p {
        margin: 5px 0;
        font-size: 0.9em;
    }

     #simulation-status span {
         color: #007bb5; /* Highlight the numbers */
     }


    #graph-container {
        width: 100%;
        max-width: 450px; /* Slightly wider graph */
        margin-top: 20px;
        text-align: center;
        background-color: #fff;
        padding: var(--spacing-base);
        border-radius: var(--border-radius-base);
        border: 1px solid var(--color-border);
        box-sizing: border-box; /* Include padding in width */
    }

    #graph-container h4 {
        margin-top: 0;
        margin-bottom: 15px; /* More space below title */
        font-size: 1.1em;
        color: #555;
    }

    #population-graph {
        width: 100% !important; /* Ensure canvas takes full width */
        height: 200px !important; /* Increased height */
    }

    #toggle-explanation-button {
        display: block;
        margin: 30px auto; /* More margin top/bottom */
        padding: 12px 20px; /* More padding */
        background-color: var(--color-info-button);
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-align: center;
    }

    #toggle-explanation-button:hover {
        background-color: var(--color-info-button-hover);
    }

    #explanation-section {
        margin-top: 20px;
        padding: var(--spacing-base) 25px; /* More padding, especially horizontal */
        border: 1px solid var(--color-border);
        border-radius: var(--border-radius-base);
        background-color: #f8f8ff; /* Very light purple/blue */
        line-height: 1.7; /* Increased line height */
        color: #333;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }

    #explanation-section h2 {
        margin-top: 0;
        color: #005662; /* Darker shade of blue/green */
        border-bottom: 2px solid var(--color-info-button);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    #explanation-section p {
        margin-bottom: 18px; /* More space between paragraphs */
        text-align: justify;
    }

    #explanation-section strong {
        color: #007bb5; /* Highlight strong text */
    }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        #controls-panel {
            flex-direction: column;
            align-items: stretch; /* Stretch items in narrow view */
        }
        .control-group {
            min-width: 100%; /* Full width on small screens */
        }
        #graph-container {
            max-width: 100%;
        }
         #tree-area {
             height: 300px; /* Reduce height on smaller screens */
         }
    }
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    const treeArea = document.getElementById('tree-area');
    const startButton = document.getElementById('start-sim-button');
    const resetButton = document.getElementById('reset-sim-button');
    const treeColorSelect = document.getElementById('tree-color-select');
    const startingMothsInput = document.getElementById('starting-moths');
    const predationRateInput = document.getElementById('predation-rate');
    const generationCountSpan = document.getElementById('generation-count');
    const lightMothsCountSpan = document.getElementById('light-moths-count');
    const darkMothsCountSpan = document.getElementById('dark-moths-count');
    const mothTemplate = document.getElementById('moth-template');
    const toggleExplanationButton = document.getElementById('toggle-explanation-button');
    const explanationSection = document.getElementById('explanation-section');
    const graphCanvas = document.getElementById('population-graph');

    let lightMoths = [];
    let darkMoths = [];
    let generation = 0;
    let simulationInterval = null;
    let chart = null;
    let chartData = {
        labels: [],
        datasets: [{
            label: 'עשים בהירים',
            data: [],
            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-light-moth'),
            backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--color-light-moth') + '80', /* 50% opacity */
            tension: 0.3, /* Add tension for smoother lines */
            pointRadius: 3 /* Smaller points */
        }, {
            label: 'עשים כהים',
            data: [],
            borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-dark-moth'),
            backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--color-dark-moth') + '80',
            tension: 0.3,
             pointRadius: 3
        }]
    };

    const maxMoths = 700; // Increased max moths
    const reproductionFactor = 1.8; // Slightly increased reproduction rate

    function createMothElement(type) {
        const moth = mothTemplate.cloneNode();
        moth.style.display = 'block';
        moth.classList.remove('moth-template');
        moth.classList.add(type);
        moth.classList.add('new'); // Add class for new moth animation
        moth.style.setProperty('--random-rotation', Math.random() * 360); // Set random initial rotation
        setPosition(moth);
        treeArea.appendChild(moth);

         // Remove 'new' class after animation to allow other transitions
         setTimeout(() => {
             moth.classList.remove('new');
         }, 600); // Match animation duration

        return moth;
    }

    function setPosition(mothElement) {
         const containerRect = treeArea.getBoundingClientRect();
         // Position randomly within the container padding a bit
         const padding = 15;
         const randomX = Math.random() * (containerRect.width - 2 * padding) + padding;
         const randomY = Math.random() * (containerRect.height - 2 * padding) + padding;
         // Use transform: translate(-50%, -50%) to position based on center
         mothElement.style.left = `${randomX}px`;
         mothElement.style.top = `${randomY}px`;
          // Keep the subtle random initial movement/rotation consistent or update slightly
         // mothElement.style.transform = `translate(${Math.random() * 8 - 4}px, ${Math.random() * 8 - 4}px) rotate(${Math.random() * 360}deg)`;
          // Let's just rely on the left/top and a slight random rotation for now
          // The CSS transition handles smooth movement if left/top changes
    }

    function initSimulation() {
        resetSimulation(); // Ensure a clean slate
        generation = 0;
        const startingCount = parseInt(startingMothsInput.value);
        const treeColor = treeColorSelect.value;

        treeArea.className = ''; // Clear existing classes
        treeArea.classList.add(treeColor);

        lightMoths = [];
        darkMoths = [];

        // Ensure total starting moths is startingCount, split between light and dark
        const initialLight = Math.floor(startingCount / 2);
        const initialDark = startingCount - initialLight;


        for (let i = 0; i < initialLight; i++) {
            lightMoths.push(createMothElement('light'));
        }
         for (let i = 0; i < initialDark; i++) {
            darkMoths.push(createMothElement('dark'));
        }


        updateDisplay();
        initChart(); // Initialize chart with starting data
        updateChart();
    }

    function runGeneration() {
        generation++;
        const treeColor = treeColorSelect.value;
        const predationRate = parseInt(predationRateInput.value) / 100; // Rate for the *disadvantaged* color

        let lightSurvivors = [];
        let darkSurvivors = [];
        let eatenMoths = []; // Keep track of elements to remove after animation

        // Predation phase
        lightMoths.forEach(moth => {
            const isCamouflaged = treeColor === 'light';
            // Survival chance: 100% if camouflaged, (100-predationRate)% if exposed
            const survivalChance = isCamouflaged ? 1 : (1 - predationRate);

             if (Math.random() < survivalChance) {
                 lightSurvivors.push(moth);
             } else {
                 // Animate removal
                 moth.classList.add('eaten');
                 eatenMoths.push(moth);
             }
        });

         darkMoths.forEach(moth => {
            const isCamouflaged = treeColor === 'dark';
            const survivalChance = isCamouflaged ? 1 : (1 - predationRate);

            if (Math.random() < survivalChance) {
                 darkSurvivors.push(moth);
             } else {
                 // Animate removal
                 moth.classList.add('eaten');
                 eatenMoths.push(moth);
             }
        });

         // Remove eaten moths from DOM after animation
         eatenMoths.forEach(moth => {
             setTimeout(() => moth.remove(), 700); // Match animation duration
         });


        // Reproduction phase
        // Simplify: each survivor has a chance to produce offspring
        let nextGenLight = [];
        let nextGenDark = [];

        lightSurvivors.forEach(moth => {
             nextGenLight.push(moth); // Survivor remains
             const numOffspring = Math.floor(Math.random() * reproductionFactor); // 0, 1, or 2 offspring
             for(let i=0; i < numOffspring; i++) {
                 if ((nextGenLight.length + nextGenDark.length + darkSurvivors.length) < maxMoths) {
                     nextGenLight.push(createMothElement('light'));
                 } else break; // Stop adding if max population reached
            }
        });

        darkSurvivors.forEach(moth => {
             nextGenDark.push(moth); // Survivor remains
             const numOffspring = Math.floor(Math.random() * reproductionFactor); // 0, 1, or 2 offspring
             for(let i=0; i < numOffspring; i++) {
                if ((nextGenLight.length + nextGenDark.length + lightSurvivors.length) < maxMoths) {
                    nextGenDark.push(createMothElement('dark'));
                } else break; // Stop adding if max population reached
            }
        });

        lightMoths = nextGenLight;
        darkMoths = nextGenDark;

         // Reposition all surviving moths and newly created ones randomly
        lightMoths.forEach(setPosition);
        darkMoths.forEach(setPosition);


        updateDisplay();
        updateChart();

        // Stop condition: population extinction or max generations
        if ((lightMoths.length === 0 && darkMoths.length === 0) || generation >= 200) { // Increased max generations
            stopSimulation();
            if (lightMoths.length === 0 && darkMoths.length === 0) {
                 simulationInterval = 'extinct'; // Use a string to indicate extinction
                 startButton.textContent = 'האוכלוסייה נכחדה!';
                 startButton.disabled = true;
            } else {
                 startButton.textContent = 'סימולציה הסתיימה';
                 startButton.disabled = true;
            }
        }
    }

    function updateDisplay() {
        generationCountSpan.textContent = generation;
        lightMothsCountSpan.textContent = lightMoths.length;
        darkMothsCountSpan.textContent = darkMoths.length;
    }

    function startSimulation() {
        startButton.disabled = true;
        startButton.textContent = 'רץ...';
        resetButton.disabled = false;
        treeColorSelect.disabled = true;
        startingMothsInput.disabled = true;
        predationRateInput.disabled = true;

        // Initialize if it's the very first run
        if (generation === 0 && lightMoths.length === 0 && darkMoths.length === 0) {
            initSimulation();
             // Allow chart update before starting interval
             setTimeout(() => {
                  simulationInterval = setInterval(runGeneration, 800); // Faster generations for quicker results
             }, 500); // Small delay before starting generations
        } else if (simulationInterval === null || simulationInterval === 'extinct') {
             // If stopped or extinct, but not reset, start again
             startButton.textContent = 'רץ...';
              simulationInterval = setInterval(runGeneration, 800);
        }

    }

    function stopSimulation() {
        if (simulationInterval !== null && simulationInterval !== 'extinct') {
            clearInterval(simulationInterval);
            simulationInterval = null;
            startButton.disabled = false;
            startButton.textContent = 'המשך סימולציה';
            treeColorSelect.disabled = false; // Allow changing environment mid-sim
            startingMothsInput.disabled = false; // Allow changing input (though values only affect init)
            predationRateInput.disabled = false; // Allow changing predation rate mid-sim
        }
    }

    function resetSimulation() {
        stopSimulation(); // Stop any running simulation
        generation = 0;
        lightMoths = [];
        darkMoths = [];
        simulationInterval = null;
        startButton.textContent = 'התחל סימולציה';

        // Remove all moth elements from the DOM except the template
        treeArea.querySelectorAll('.moth:not(#moth-template)').forEach(moth => moth.remove());

        updateDisplay();
         // Reset chart
        if (chart) {
            chart.destroy();
        }
        chartData.labels = [];
        chartData.datasets[0].data = [];
        chartData.datasets[1].data = [];
        initChart(); // Initialize a fresh, empty chart

        resetButton.disabled = true;
        startButton.disabled = false;
        treeColorSelect.disabled = false;
        startingMothsInput.disabled = false;
        predationRateInput.disabled = false;

        // Reset tree color visually
        treeArea.className = '';
        treeArea.classList.add(treeColorSelect.value);

    }

     function initChart() {
        const ctx = graphCanvas.getContext('2d');
        if (chart) {
             chart.destroy(); // Destroy existing chart before creating a new one
        }
        chart = new Chart(ctx, {
            type: 'line',
            data: chartData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 400 // Animation duration for chart updates
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'דור',
                             font: { size: 12 }
                        },
                        grid: { display: false } /* Hide x-axis grid lines */
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'מספר עשים',
                            font: { size: 12 }
                        },
                        beginAtZero: true,
                        suggestedMax: parseInt(startingMothsInput.value) * 2, /* Suggest max based on starting count */
                        ticks: {
                             stepSize: parseInt(startingMothsInput.value) / 4 || 50 /* Suggest tick step */
                         },
                         grid: { color: '#eee' } /* Light gray y-axis grid */
                    }
                },
                plugins: {
                    legend: {
                        display: true,
                        position: 'bottom' /* Legend at the bottom */
                    },
                    tooltip: {
                        mode: 'index',
                        intersect: false
                    }
                },

            }
        });
     }

    function updateChart() {
        chartData.labels.push(generation);
        chartData.datasets[0].data.push(lightMoths.length);
        chartData.datasets[1].data.push(darkMoths.length);
         // Adjust suggestedMax if population grows significantly
         const currentMax = Math.max(...chartData.datasets[0].data, ...chartData.datasets[1].data);
         if (currentMax > chart.options.scales.y.suggestedMax * 0.8) { // If population reaches 80% of suggested max
             chart.options.scales.y.suggestedMax = currentMax * 1.2; // Increase suggested max by 20%
             chart.options.scales.y.ticks.stepSize = currentMax / 5 || 50; // Adjust step size
         }

        chart.update();
    }


    function toggleExplanation() {
        const isHidden = explanationSection.style.display === 'none';
        // Use CSS classes for smoother transition if desired, but direct display toggle is also fine here
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.setAttribute('aria-expanded', !isHidden);
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מדעי' : 'הסבר מדעי: מה קורה כאן בעצם?';
    }

    // Event Listeners
    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', toggleExplanation);
    treeColorSelect.addEventListener('change', () => {
        // Change tree color immediately if simulation is not running
        if (simulationInterval === null || simulationInterval === 'extinct') {
             treeArea.className = '';
             treeArea.classList.add(treeColorSelect.value);
        }
        // If simulation is running, the environment changes next generation
         // Optional: Add visual feedback that change will apply next generation
    });


    // Initial state setup
     initChart(); // Initialize empty chart on load
     treeArea.classList.add(treeColorSelect.value); // Set initial tree color visually


</script>