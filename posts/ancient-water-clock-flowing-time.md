---
title: "שעון מים עתיק: זמן שזורם"
english_slug: ancient-water-clock-flowing-time
category: "פיזיקה"
tags: ["שעון מים", "קלפסידרה", "טכנולוגיה עתיקה", "מדידת זמן", "פיזיקה", "טוריצ'לי"]
---
<style>
:root {
    --container-width: 120px;
    --container-height: 350px;
    --water-color: #46b5d1;
    --water-color-dark: #3a9acb;
    --container-border: 3px solid #555;
    --container-bg: #f0f0f0;
    --controls-bg: #e8e8e8;
    --button-bg: #d8d8d8;
    --button-hover-bg: #cccccc;
    --button-border: 1px solid #555;
    --clock-border: 1px solid #aaa;
    --clock-bg: #ffffff;
    --hole-color: #333;
    --sim-bg: #f9f9f9;
    --explanation-bg: #f0f0f0;
    --explanation-border: 1px solid #ccc;
    --text-color: #333;
    --header-color: #222;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

h1, h2 {
    color: var(--header-color);
    text-align: center;
    margin-bottom: 1em;
}

h1 {
    font-size: 2em;
    margin-top: 0;
}

h2 {
    font-size: 1.5em;
    border-bottom: 1px dashed #aaa;
    padding-bottom: 5px;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
}

p {
    margin-bottom: 1em;
}

#simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px auto;
    padding: 30px 20px;
    background-color: var(--sim-bg);
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    max-width: 500px; /* Limit width for better layout */
}

.sim-title {
    font-size: 1.6em;
    margin-bottom: 20px;
    color: var(--header-color);
    text-align: center;
}

.container-wrapper {
     position: relative;
     width: var(--container-width);
     height: var(--container-height);
     margin-bottom: 25px;
     display: flex;
     justify-content: center; /* Center the container visually */
}

.container {
    width: 100%; /* Takes full width of wrapper */
    height: 100%; /* Takes full height of wrapper */
    border: var(--container-border);
    border-radius: 8px;
    position: relative;
    overflow: hidden;
    background-color: var(--container-bg);
    box-sizing: border-box;
    display: flex; /* Use flex to center water if needed */
    flex-direction: column-reverse; /* Keep water at the bottom */
}

.water {
    width: 100%;
    background: linear-gradient(to top, var(--water-color-dark), var(--water-color));
    transition: height linear; /* Smoothness applied via JS simulation steps */
    box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.2);
}

.hole {
    position: absolute;
    bottom: -8px; /* Position below container */
    left: 50%;
    transform: translateX(-50%);
    width: 18px;
    height: 18px;
    background-color: var(--hole-color);
    border-radius: 50%;
    z-index: 2; /* Above water */
    border: 3px solid var(--sim-bg); /* 'Cutout' effect */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

.time-marks {
    position: absolute;
    top: 0;
    left: calc(100% + 5px); /* Position to the right of the container */
    height: 100%;
    width: 40px; /* Space for marks and labels */
    display: flex;
    flex-direction: column-reverse; /* Bottom is 0, top is max */
    pointer-events: none; /* Allow clicks to pass through */
}

.time-mark {
    position: absolute;
    width: 15px;
    height: 2px;
    background-color: #888;
    right: 0; /* Align to the right edge of .time-marks */
    transform: translateY(50%); /* Center the line on the calculated height */
    box-sizing: border-box;
    transition: background-color 0.3s ease;
}

.time-mark.passed {
    background-color: #e74c3c; /* Highlight color */
}

.time-mark-label {
    position: absolute;
    right: 20px; /* Position label to the right of the line */
    top: 50%; /* Vertically align with the line */
    transform: translateY(-50%);
    font-size: 0.9em;
    color: #555;
}


.controls {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    margin-bottom: 15px;
    flex-wrap: wrap;
    padding: 10px;
    background-color: var(--controls-bg);
    border-radius: 8px;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

#digital-clock {
    font-size: 1.6em;
    font-family: 'Courier New', monospace;
    border: var(--clock-border);
    padding: 8px 15px;
    background-color: var(--clock-bg);
    border-radius: 5px;
    min-width: 120px;
    text-align: center;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

button {
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
    border: var(--button-border);
    background-color: var(--button-bg);
    border-radius: 5px;
    transition: background-color 0.2s ease, transform 0.1s ease;
    min-width: 100px;
}
button:hover:not(:disabled) {
    background-color: var(--button-hover-bg);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}
button:active:not(:disabled) {
    transform: scale(0.98);
}
button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

#sim-message {
    margin-top: 15px;
    font-style: italic;
    color: #666;
    text-align: center;
    min-height: 1.2em; /* Reserve space to prevent layout shift */
}

#toggle-explanation {
     display: block; /* Ensure button takes its own line */
     margin: 20px auto; /* Center the button */
     padding: 10px 20px;
     font-size: 1.1em;
     cursor: pointer;
     border: var(--button-border);
     background-color: var(--button-bg);
     border-radius: 5px;
     transition: background-color 0.2s ease, transform 0.1s ease;
}
#toggle-explanation:hover {
    background-color: var(--button-hover-bg);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}
#toggle-explanation:active {
    transform: scale(0.98);
}


#explanation {
    margin: 20px auto;
    padding: 20px;
    border: var(--explanation-border);
    background-color: var(--explanation-bg);
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    max-width: 800px; /* Limit explanation width */
}

#explanation h2 {
    margin-top: 1em;
    margin-bottom: 0.5em;
    font-size: 1.3em;
    border-bottom: 1px dashed #aaa;
    padding-bottom: 4px;
}

#explanation h2:first-child {
     margin-top: 0;
}

#explanation p {
    margin-bottom: 1em;
    line-height: 1.5;
}

#explanation ul {
    margin-top: 0.5em;
    margin-bottom: 1em;
    padding-left: 25px;
}

#explanation li {
    margin-bottom: 0.5em;
}
</style>

<h1>שעון מים עתיק: זמן שזורם</h1>
<p>הצטרפו אלינו למסע בזמן אל העידן שלפני השעונים המודרניים! איך יכלו ציוויליזציות קדומות כמו המצרים, היוונים והרומאים למדוד זמן בדיוק מספק כדי לנהל את חייהן, לתזמן טקסים, או אפילו למדוד זמני נאום בבתי משפט? גלו את הקסם ההנדסי מאחורי אחד ממכשירי מדידת הזמן הראשונים בהיסטוריה – הקלפסידרה, או שעון המים.</p>

<div id="simulation-container">
    <div class="sim-title">צפו בזמן זורם: קלפסידרה פשוטה</div>
    <div class="container-wrapper">
        <div class="container">
            <div class="water"></div>
        </div>
        <div class="hole"></div>
        <div class="time-marks">
            <!-- Time marks will be added here by JavaScript -->
        </div>
    </div>
    <div class="controls">
        <div id="digital-clock">00:00:00</div>
        <button id="start-sim">התחל זרימה</button>
        <button id="reset-sim">אפס</button>
    </div>
    <div id="sim-message">לחצו "התחל זרימה" כדי לראות איך שעון מים עובד!</div>
</div>

<button id="toggle-explanation">מה בעצם קורה כאן? הסבר על שעון מים</button>

<div id="explanation" style="display: none;">
    <h2>מהי קלפסידרה (שעון מים)?</h2>
    <p>קלפסידרה (מיוונית: "גונבת מים") היא מכשיר עתיק למדידת זמן המשתמש בזרימת מים. בשיאה, בימי קדם, היא הייתה אחד ממכשירי מדידת הזמן המדויקים ביותר שהיו קיימים, במיוחד כאשר השמש לא הייתה זמינה (בלילה או ביום מעונן).</p>
    <h2>עקרון הפעולה הפשוט... והבעיה</h2>
    <p>הדגם הבסיסי ביותר, כמו זה שאתם רואים בסימולציה, הוא כלי קיבול עם חור קטן בתחתיתו. ממלאים את הכלי במים, והם מתחילים לזרום החוצה דרך החור. באופן אינטואיטיבי, אפשר לחשוב שאם הכלי יתרוקן בקצב אחיד, אפשר יהיה לחלק את הדופן שלו לסימני שעות שווים.</p>
    <p>אבל כפי שאתם בוודאי רואים בסימולציה (שימו לב למרווחים בין קווי הזמן ולמהירות ירידת המים ביחס אליהם), קצב זרימת המים <strong>אינו קבוע!</strong> למה? ככל שיש יותר מים בכלי, הלחץ בתחתית גדול יותר. לחץ גבוה גורם למים לזרום מהר יותר החוצה דרך החור. ככל שמפלס המים יורד, הלחץ קטן, וקצב הזרימה מאט משמעותית. עקרון פיזיקלי זה מתואר ע"י חוק טוריצ'לי, שקושר את מהירות הזרימה לשורש הריבועי של גובה עמוד הנוזל.</p>
    <p><strong>התוצאה:</strong> פרק הזמן שלוקח למפלס לרדת יחידת גובה אחת כשהכלי מלא קצר בהרבה מאשר כשהכלי כמעט ריק. אם תשימו לב לסימני "השעות" בצד הכלי בסימולציה, תראו שהמרחק ביניהם הולך וגדל כלפי מטה - כך שהמים עוברים את המרווחים העליונים מהר יותר מהמרווחים התחתונים. זה הופך את השעון ה"פשוט" הזה ללא מדויק למדידת פרקי זמן שווים!</p>
    <h2>פתרונות גאוניים מהעת העתיקה</h2>
    <p>כדי ליצור שעוני מים מדויקים יותר, המהנדסים הקדומים פיתחו פתרונות יצירתיים:</p>
    <ul>
        <li><strong>כלי קיבול בעל צורה מיוחדת:</strong> במקום גליל ישר, ייצרו כלים שדפנותיהם מתרחבות כלפי מעלה בצורה מדויקת. צורה זו פיצתה על קצב הזרימה המשתנה, ויצרה ירידת מפלס שהיא אחידה יותר ביחס לזמן.</li>
        <li><strong>מערכות מורכבות עם מנגנון זרימה קבועה:</strong> המציאו שעונים בעלי שני מיכלים או יותר. מיכל עליון גדול שימש כ"מאגר" ששמר על מפלס כמעט קבוע, וסיפק מים בקצב אחיד למיכל המדידה התחתון. מפלס המים במיכל התחתון עלה אז בצורה לינארית, והיה קל לסמן עליו שעות במרווחים שווים. שעונים מורכבים אלו כללו לעיתים גם מנגנונים נוספים כמו מצופים שהפעילו פעמונים או צלמיות קטנות לציון השעה.</li>
    </ul>
    <h2>החשיבות ההיסטורית</h2>
    <p>שעוני המים לא היו רק צעצועים טכנולוגיים; הם היו כלים חיוניים לניהול חברתי ומנהלי בעת העתיקה. הם שימשו בבתי משפט להגבלת זמני דיבור (וכך להבטיח הליך הוגן יותר), לתיזמון טקסים דתיים מדויקים, לארגון משמרות צבאיות, ובאופן כללי אפשרו רמה חדשה של ארגון בחיי היום-יום עד להופעת השעונים המכניים המודרניים.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const water = document.querySelector('.water');
    const clock = document.getElementById('digital-clock');
    const startButton = document.getElementById('start-sim');
    const resetButton = document.getElementById('reset-sim');
    const explanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const containerElement = document.querySelector('.container');
    const timeMarksContainer = document.querySelector('.time-marks');
    const simMessage = document.getElementById('sim-message');

    const containerHeight = containerElement.offsetHeight;
    const maxWaterHeight = containerHeight;

    let currentWaterHeight = 0; // px
    let simulationInterval = null;
    let timerInterval = null;
    let elapsedRealSeconds = 0;

    // Simulation parameters
    // These control the *visual* speed and the *simulated* total duration representation
    const totalRealDurationSeconds = 30; // Total real time it takes for water to drain in simulation
    const totalSimulatedHours = 12; // Total hours represented by a full container
    const simulationTimeStep = 50; // ms - determines smoothness and update frequency

    // Flow rate factor derived from Torricelli's Law dh/dt = -k * sqrt(h)
    // Integrating gives total drain time T = (2/k) * sqrt(H_max)
    // So k = 2 * sqrt(H_max) / T
    // In our simulation: dh/dt is approximated as delta_h / delta_t
    // delta_h = -k * sqrt(h_ratio) * H_max * delta_t
    // flowRateFactor is our k in this discrete approximation.
    // We need k such that total drain time is totalRealDurationSeconds
    // Approximating k: (total drain time) approx (maxWaterHeight / average_speed). Avg speed is proportional to sqrt(maxWaterHeight/2).
    // This is tricky with discrete steps. Let's find k experimentally or by tuning.
    // Let's target totalRealDurationSeconds. The rate is proportional to sqrt(h).
    // A simpler approach is to directly calculate the height at a given time t
    // The analytical solution for height h(t) for draining cylinder is h(t) = (sqrt(H_max) - (k/2) * t)^2
    // Where k relates orifice area, container area, and gravity.
    // Total time T = 2 * sqrt(H_max) / k. So k = 2 * sqrt(H_max) / T
    // Let's choose k such that T = totalRealDurationSeconds when H_max is maxWaterHeight.
    // k_physical = 2 * Math.sqrt(maxWaterHeight) / totalRealDurationSeconds;
    // Our simulation step: height -= rate * dt. Rate is proportional to sqrt(height).
    // Let rate = C * sqrt(currentWaterHeight).
    // We want total drain time T. Integral of dt = Integral( -dh / (C * sqrt(h)) )
    // T = (2/C) * sqrt(H_max). So C = 2 * sqrt(H_max) / T.
    const simFlowFactor = 2 * Math.sqrt(maxWaterHeight) / totalRealDurationSeconds;


    let markHeights = []; // Store the pixel height for each hour mark
    const numMarks = totalSimulatedHours; // Number of hour marks (e.g., 1 to 12)
    let passedMarks = new Set(); // Keep track of marks that have been passed

    // Function to calculate the height of the water at a specific real time point
    // based on the analytical solution h(t) = (sqrt(H_max) - (k/2) * t)^2
    // where k = 2 * sqrt(H_max) / T_total_real
    function calculateHeightAtTime(timeInSeconds) {
        const sqrtHmax = Math.sqrt(maxWaterHeight);
        const k_eff = 2 * sqrtHmax / totalRealDurationSeconds; // Effective k for this height scale
        const height = Math.max(0, (sqrtHmax - (k_eff / 2) * timeInSeconds));
        return height * height;
    }

    // Calculate the height for each hour mark (0 to 12 hours)
    // Mark 0 is at the top (full), Mark 12 is at the bottom (empty).
    // We place marks for 1 hour, 2 hours, ..., 12 hours.
    // The time for mark 'i' is i * (totalRealDurationSeconds / totalSimulatedHours)
    function calculateMarkPositions() {
        markHeights = [];
        // We need positions for marks 1 through 12.
        // Mark i is the height when i "simulated hours" have passed.
        // This corresponds to (i / totalSimulatedHours) * totalRealDurationSeconds real seconds.
        for (let i = 1; i <= numMarks; i++) {
            const realTimeForMark = (i / totalSimulatedHours) * totalRealDurationSeconds;
            const height = calculateHeightAtTime(realTimeForMark);
             // Store height from the BOTTOM (like CSS height property)
            markHeights.push({
                 hour: i,
                 height: height // height in pixels from the bottom
            });
        }
         // Add the 0 hour mark at the top (for clarity, though not strictly needed for timing)
         markHeights.unshift({hour: 0, height: maxWaterHeight}); // 0 hours -> full height

        renderTimeMarks();
    }

    function renderTimeMarks() {
        timeMarksContainer.innerHTML = ''; // Clear existing marks
        markHeights.forEach((markInfo, index) => {
            const markElement = document.createElement('div');
            markElement.classList.add('time-mark');
             // Position from the bottom, adjusting for the line height itself
             // CSS 'bottom' property refers to the bottom edge of the element.
             // We want the center of the line to be at markInfo.height.
             // So, bottom = markInfo.height - (line_height/2). Since height is 2px, -1px offset.
            markElement.style.bottom = `${markInfo.height - 1}px`;
            markElement.dataset.hour = markInfo.hour; // Store the hour number

            if (markInfo.hour > 0) { // Don't label the 0 hour mark usually
                 const labelElement = document.createElement('span');
                 labelElement.classList.add('time-mark-label');
                 labelElement.textContent = `${markInfo.hour} שעות`;
                 markElement.appendChild(labelElement);
            }

            timeMarksContainer.appendChild(markElement);
        });
    }


    function updateClock() {
        elapsedRealSeconds++;

        // Calculate simulated time based on percentage of real duration completed
        const completionRatio = elapsedRealSeconds / totalRealDurationSeconds;
        const simulatedTotalSeconds = completionRatio * totalSimulatedHours * 3600; // Total seconds in simulated time

        const h = String(Math.floor(simulatedTotalSeconds / 3600)).padStart(2, '0');
        const m = String(Math.floor((simulatedTotalSeconds % 3600) / 60)).padStart(2, '0');
        const s = String(Math.floor(simulatedTotalSeconds % 60)).padStart(2, '0'); // Use floor for whole seconds
        clock.textContent = `${h}:${m}:${s}`;

        // Check and highlight passed marks
        markHeights.forEach(markInfo => {
             // MarkInfo.height is height from the BOTTOM.
             // currentWaterHeight is height from the BOTTOM.
             // A mark is passed if water level drops below it AND it hasn't been passed yet.
             if (markInfo.hour > 0 && currentWaterHeight <= markInfo.height && !passedMarks.has(markInfo.hour)) {
                 const markElement = timeMarksContainer.querySelector(`.time-mark[data-hour="${markInfo.hour}"]`);
                 if (markElement) {
                     markElement.classList.add('passed');
                     simMessage.textContent = `עברה שעה ${markInfo.hour} לפי שעון המים!`;
                 }
                 passedMarks.add(markInfo.hour);
             }
        });

         // Check if simulation is complete
        if (elapsedRealSeconds >= totalRealDurationSeconds) {
            stopSimulation();
            currentWaterHeight = 0;
            water.style.height = '0px';
            clock.textContent = String(totalSimulatedHours).padStart(2, '0') + ':00:00'; // Final clock value
            simMessage.textContent = 'המים אזלו! הסימולציה הסתיימה.';
            // Ensure all marks are marked as passed at the end
            timeMarksContainer.querySelectorAll('.time-mark').forEach(markEl => markEl.classList.add('passed'));
        }
    }

    // Simulate water flow based on h(t) = (sqrt(H_max) - (k_eff/2) * t)^2
    // Update height based on the *current elapsed time*
    function simulateWaterFlow() {
        // This function is called every simulationTimeStep (e.g., 50ms)
        // elapsedRealSeconds is updated separately every 1000ms by updateClock.
        // We need a more precise timekeeper for the simulation physics.
        // Let's use the setInterval trigger time itself as the time step.
        // elapsedRealSeconds will still track the 'wall clock' time for the digital display update rate.

        // Let's calculate height based on the total real time elapsed since start
        // using the analytical formula for height at time 't'.
        // This makes the simulation smoothly follow the true physics, independent of step size.
        const timeNowInSeconds = (elapsedRealSeconds * 1000 + (performance.now() - simulationStartTime)) / 1000;
        currentWaterHeight = calculateHeightAtTime(timeNowInSeconds);

        water.style.height = `${currentWaterHeight}px`;

        // Manual check for end condition if relying purely on height
         if (currentWaterHeight <= 0) {
             // Let the timer interval handle the end state
             // but stop the height updates immediately
             water.style.height = '0px';
         }
    }

    let simulationStartTime = 0; // To track start time for precise calculation

    function startSimulation() {
        if (simulationInterval) return; // Already running

        // Reset if starting from empty or near empty
        if (currentWaterHeight < 1 || elapsedRealSeconds >= totalRealDurationSeconds) {
            resetSimulation(); // Full reset before starting
        }

        passedMarks = new Set(); // Clear passed marks on start
        timeMarksContainer.querySelectorAll('.time-mark').forEach(markEl => markEl.classList.remove('passed'));
         markHeights.forEach(markInfo => {
             if (markInfo.hour === 0) { // Mark 0 is 'passed' at the very start
                  timeMarksContainer.querySelector(`.time-mark[data-hour="0"]`).classList.add('passed');
             }
         });


        simulationStartTime = performance.now(); // Record start time
        // Update water level based on elapsed time
        simulationInterval = setInterval(simulateWaterFlow, simulationTimeStep);
        // Update digital clock and check marks every second
        timerInterval = setInterval(updateClock, 1000);


        startButton.disabled = true;
        resetButton.disabled = false;
        simMessage.textContent = 'מים זורמים... שימו לב לקצב!';
    }

    function stopSimulation() {
        clearInterval(simulationInterval);
        clearInterval(timerInterval);
        simulationInterval = null;
        timerInterval = null;
        startButton.disabled = false;
        // Keep resetButton enabled
        simMessage.textContent = 'הסימולציה מושהית.';
    }

    function resetSimulation() {
        stopSimulation();
        currentWaterHeight = maxWaterHeight;
        water.style.height = `${currentWaterHeight}px`;
        elapsedRealSeconds = 0;
        clock.textContent = '00:00:00';
        startButton.disabled = false;
        resetButton.disabled = false; // Reset button is always available after first start
        simMessage.textContent = 'לחצו "התחל זרימה" כדי לראות איך שעון מים עובד!';
        passedMarks = new Set(); // Clear passed marks
        timeMarksContainer.querySelectorAll('.time-mark').forEach(markEl => markEl.classList.remove('passed'));
         // Mark 0 is 'passed' immediately on reset/full
         const mark0 = timeMarksContainer.querySelector(`.time-mark[data-hour="0"]`);
         if(mark0) mark0.classList.add('passed');
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'מה בעצם קורה כאן? הסבר על שעון מים';
        simMessage.style.display = isHidden ? 'none' : 'block'; // Hide message when explanation is open? Maybe not. Keep message.
         // Adjust button text based on state
         explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'מה בעצם קורה כאן? הסבר על שעון מים';
    }

    // --- Initialization ---
    calculateMarkPositions(); // Calculate where the hour marks should be
    resetSimulation(); // Start with full water and reset state

    // Add event listeners
    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);
    explanationButton.addEventListener('click', toggleExplanation);
});
</script>
```